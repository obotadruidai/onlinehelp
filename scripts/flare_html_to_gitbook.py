#!/usr/bin/env python3
"""Convert a MadCap Flare HTML5 target into GitBook Markdown.

Method A from the migration notes: BeautifulSoup plus markdownify, applied to a
whole Flare HTML5 output folder. Relative topic cross-references are rewritten
from .htm/.html to .md. External URLs, mailto links, and anchors are preserved.

Examples
--------
  # From the published or locally built HTML5 folder:
  python3 scripts/flare_html_to_gitbook.py convert \\
      --html-root "/path/to/HTML5 - Top Navigation" \\
      --out ./gitbook-out

  # Download the public Druid HTML5 target, then convert it:
  python3 scripts/flare_html_to_gitbook.py migrate \\
      --base https://docs.druidai.com/docs \\
      --mirror /tmp/flare-html \\
      --out .
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

USER_AGENT = "DruidHelpGitBookMigration/1.0"
HELP_HOSTS = {"docs.druidai.com"}
CHROME_IDS = {"mc-main-content", "offCanvas", "sf-content"}
SKIP_PREFIXES = ("skins/", "resources/scripts/", "data/")
ASSET_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".bmp",
    ".ico",
    ".pdf",
    ".zip",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".mp4",
    ".webm",
    ".mp3",
    ".wav",
    ".csv",
    ".txt",
}
SHELL_FILENAMES = {
    "index.htm",
    "index.html",
    "default.htm",
    "default.html",
    "default_csh.htm",
    "search.htm",
    "search.html",
}
ANCHOR_MARK = "data-flare-anchors"
ANCHOR_SEP = "\u001f"
NOTE_CLASSES = {"note", "tip", "warning", "important", "caution", "example", "info"}
TOKEN_RE = re.compile(r"FLAREANCHOR(\d+)ENDANCHOR")
MD_LINK_RE = re.compile(
    r"(?<!!)\[((?:\\.|[^\]])*)\]\((<[^>]+>|[^)\s]+)\)"
)
MD_IMAGE_RE = re.compile(
    r"!\[((?:\\.|[^\]])*)\]\((<[^>]+>|[^)\s]+)\)"
)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


class Corpus:
    def __init__(self, public_base: str):
        self.public_base = public_base.rstrip("/")
        self.topics: dict[str, str] = {}
        self.assets: set[str] = set()
        self.anchors: dict[str, set[str]] = {}
        self.titles: dict[str, str] = {}

    def add_topic(self, rel_htm: str) -> None:
        key = rel_htm.casefold()
        self.topics.setdefault(key, rel_htm)

    def lookup_topic(self, rel_htm: str) -> str | None:
        return self.topics.get(rel_htm.casefold())

    def has_asset(self, rel: str) -> bool:
        if rel in self.assets:
            return True
        folded = rel.casefold()
        return any(item.casefold() == folded for item in self.assets)


def norm_rel(path: str) -> str:
    path = path.replace("\\", "/").strip()
    path = urllib.parse.unquote(path)
    path = path.replace("\u00a0", " ")
    while path.startswith("./"):
        path = path[2:]
    path = posixpath.normpath(path)
    if path.startswith("./"):
        path = path[2:]
    if path == ".":
        return ""
    return path.lstrip("/")


def split_rel_href(href: str) -> tuple[str, str | None, str | None]:
    path = href
    fragment = None
    query = None
    if "#" in path:
        path, fragment = path.split("#", 1)
    if "?" in path:
        path, query = path.split("?", 1)
    return path, query, fragment


def is_id_token(text: str) -> bool:
    if not text or len(text) > 200:
        return False
    if any(ch.isspace() for ch in text):
        return False
    if text.lower() in {"closed", "open", "copy", "related topics"}:
        return False
    return True


def to_md_path(rel_htm: str) -> str:
    lower = rel_htm.lower()
    for ext in (".html", ".htm"):
        if lower.endswith(ext):
            return rel_htm[: -len(ext)] + ".md"
    return rel_htm


def encode_rel(path: str, fragment: str | None = None, query: str | None = None) -> str:
    encoded = urllib.parse.quote(path, safe="/")
    if query:
        encoded += "?" + query
    if fragment:
        encoded += "#" + urllib.parse.quote(fragment, safe="")
    return encoded


def format_external(href: str) -> str:
    if re.search(r"[\s()]", href):
        return "<" + href.replace(">", "%3E") + ">"
    return href


def public_url(public_base: str, rel: str, query: str | None, fragment: str | None) -> str:
    url = public_base.rstrip("/") + "/" + urllib.parse.quote(rel, safe="/")
    if query:
        url += "?" + query
    if fragment:
        url += "#" + urllib.parse.quote(fragment, safe="")
    return url


def help_content_path(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc.lower() not in HELP_HOSTS:
        return None
    path = urllib.parse.unquote(parsed.path)
    for marker in ("/Content/", "/MicroContent/", "/Resources/"):
        idx = path.find(marker)
        if idx != -1:
            return norm_rel(path[idx + 1 :])
    return None


def resolve_rel(source_htm: str, href_path: str) -> str:
    href_path = urllib.parse.unquote(href_path).replace("\\", "/").replace("\u00a0", " ")
    if href_path.startswith("/"):
        path = norm_rel(href_path)
        for prefix in ("docs/",):
            if path.lower().startswith(prefix):
                path = path[len(prefix) :]
        return path
    base = posixpath.dirname(source_htm)
    return norm_rel(posixpath.join(base, href_path))


def _compact_anchor(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z]+", "", value).casefold()


def repair_fragment(fragment: str | None, link_text: str, anchors: set[str]) -> str | None:
    if not fragment:
        return fragment
    if fragment in anchors:
        return fragment
    prefixed = sorted(anchor for anchor in anchors if anchor.startswith(fragment))
    if len(prefixed) == 1:
        return prefixed[0]
    text = re.sub(r"\s+", " ", link_text or "").strip()
    if text and text in anchors:
        return text
    # Flare bookmarks often drop spaces ("Explainability at Druid Conductor Level"
    # is published against id ExplainabilityatDruidConductorLevel).
    wanted = _compact_anchor(fragment)
    if wanted:
        compacted = sorted(anchor for anchor in anchors if _compact_anchor(anchor) == wanted)
        if len(compacted) == 1:
            return compacted[0]
        if len(wanted) >= 4:
            prefixed = sorted(
                anchor for anchor in anchors if _compact_anchor(anchor).startswith(wanted)
            )
            if len(prefixed) == 1:
                return prefixed[0]
    return fragment


def rewrite_url(
    href: str,
    source_htm: str,
    corpus: Corpus,
    link_text: str = "",
) -> tuple[str | None, str]:
    """Return the Markdown destination and a kind.

    None means the wrapper is not a real link (javascript, bare #) and should
    be unwrapped so the visible text remains.
    """
    raw = (href or "").strip()
    if not raw:
        return None, "dropped"
    lowered = raw.lower()
    if lowered.startswith(("javascript:", "madcap:")) or raw in {"#", "#top"}:
        return None, "dropped"
    if lowered.startswith(("mailto:", "tel:")):
        return format_external(raw), "email"

    if lowered.startswith(("http://", "https://", "//")):
        absolute = raw
        if raw.startswith("//"):
            absolute = "https:" + raw
        content = help_content_path(absolute)
        parsed = urllib.parse.urlparse(absolute)
        if content is None:
            return format_external(raw if not raw.startswith("//") else absolute), "external"
        fragment = urllib.parse.unquote(parsed.fragment) if parsed.fragment else None
        return _rewrite_resolved(
            content,
            source_htm,
            corpus,
            link_text,
            original=absolute,
            query=parsed.query or None,
            fragment=fragment,
        )

    path, query, fragment = split_rel_href(raw)
    if fragment:
        fragment = urllib.parse.unquote(fragment)
    if path == "" and fragment is not None:
        target = corpus.lookup_topic(source_htm) or source_htm
        anchors = corpus.anchors.get(target, set())
        fragment = repair_fragment(fragment, link_text, anchors)
        return "#" + urllib.parse.quote(fragment or "", safe=""), "fragment"
    if not path:
        return None, "dropped"
    resolved = resolve_rel(source_htm, path)
    if resolved.startswith(".."):
        return format_external(raw), "unresolved"
    return _rewrite_resolved(resolved, source_htm, corpus, link_text, original=raw, query=query, fragment=fragment)


def _rewrite_resolved(
    resolved: str,
    source_htm: str,
    corpus: Corpus,
    link_text: str,
    original: str,
    query: str | None,
    fragment: str | None,
) -> tuple[str, str]:
    topic = corpus.lookup_topic(resolved)
    lower = resolved.lower()
    if topic is None and lower.endswith((".htm", ".html")):
        # Case-insensitive lookup already happened. Try a shell page.
        filename = posixpath.basename(lower)
        if filename in SHELL_FILENAMES or lower.startswith(SKIP_PREFIXES):
            return public_url(corpus.public_base, resolved, query, fragment), "shell"
        # Keep the published URL when we do not have the topic, so the link
        # still opens the existing help page instead of a missing .md file.
        if original.lower().startswith(("http://", "https://")):
            return format_external(original), "unresolved"
        return public_url(corpus.public_base, resolved, query, fragment), "unresolved"

    if topic is not None:
        target_md = to_md_path(topic)
        source_md = to_md_path(source_htm)
        anchors = corpus.anchors.get(topic, set())
        fragment = repair_fragment(fragment, link_text, anchors) if fragment else fragment
        if norm_rel(target_md) == norm_rel(source_md) and fragment:
            return "#" + urllib.parse.quote(fragment, safe=""), "fragment"
        rel = posixpath.relpath(target_md, posixpath.dirname(source_md) or ".")
        return encode_rel(rel, fragment, query), "crossref"

    if corpus.has_asset(resolved):
        source_md = to_md_path(source_htm)
        rel = posixpath.relpath(resolved, posixpath.dirname(source_md) or ".")
        return encode_rel(rel, fragment, query), "asset"
    if posixpath.splitext(lower)[1] in ASSET_EXTENSIONS:
        # A picture on another published help version is not in this output.
        # Leave the absolute URL in place so the image still opens.
        if original.lower().startswith(("http://", "https://", "//")):
            return format_external(original), "external"
        source_md = to_md_path(source_htm)
        rel = posixpath.relpath(resolved, posixpath.dirname(source_md) or ".")
        return encode_rel(rel, fragment, query), "asset"

    if original.lower().startswith(("http://", "https://")):
        return format_external(original), "external"
    return format_external(original), "unresolved"


def _class_set(tag: Tag) -> set[str]:
    classes = tag.get("class") or []
    if isinstance(classes, str):
        return set(classes.split())
    return set(classes)


def _drop_tag(tag: Tag) -> None:
    tag.decompose()


def _clean_label(tag: Tag) -> str:
    return re.sub(r"\s+", " ", tag.get_text(" ", strip=True)).strip()


def _mark_anchors(tag: Tag, anchors: set[str]) -> None:
    if not anchors:
        return
    existing = tag.get(ANCHOR_MARK)
    merged: list[str] = []
    if existing:
        merged.extend(existing.split(ANCHOR_SEP))
    for anchor in anchors:
        if anchor and anchor not in merged and anchor not in CHROME_IDS:
            merged.append(anchor)
    if merged:
        tag[ANCHOR_MARK] = ANCHOR_SEP.join(merged)


def prepare_topic(html: str) -> tuple[BeautifulSoup, Tag, set[str]]:
    soup = BeautifulSoup(html, "lxml")
    main = soup.select_one("#mc-main-content")
    if main is None:
        main = soup.body or soup

    for tag in list(main.find_all(["script", "style"])):
        _drop_tag(tag)
    for tag in list(main.select(".codeSnippetCopyButton")):
        _drop_tag(tag)
    for img in list(main.find_all("img")):
        src = (img.get("src") or "").replace("\\", "/")
        classes = _class_set(img)
        if (
            "MCDropDown_Image_Icon" in classes
            or "MCHelpControl_Image_Icon" in classes
            or "/Skins/" in src
            or src.endswith("transparent.gif")
        ):
            _drop_tag(img)
    for link in list(main.select("a.MCPopupThumbnailLink")):
        link.unwrap()
    for tag in list(main.find_all(True)):
        name = tag.name or ""
        if ":" in name or "conditional" in name.lower():
            tag.unwrap()
    for span in list(main.select("span.mc-variable")):
        span.unwrap()

    # Innermost dropdowns first so nested expansions keep their own headings.
    for _guard in range(5000):
        dropdowns = [d for d in main.select(".MCDropDown") if isinstance(d, Tag)]
        if not dropdowns:
            break
        inner = [d for d in dropdowns if not d.select(".MCDropDown")] or dropdowns[:1]
        for dropdown in inner:
            _flatten_dropdown(soup, dropdown)

    for hotspot in list(main.select(".MCHelpControl-RelatedHotSpot_")):
        title = _clean_label(hotspot) or "Related Topics"
        heading = soup.new_tag("h2")
        heading.string = title
        hotspot.replace_with(heading)

    for div in list(main.find_all("div")):
        if _class_set(div) & NOTE_CLASSES:
            div.name = "blockquote"

    for snippet in list(main.select(".codeSnippet")):
        caption = snippet.select_one(".codeSnippetCaption")
        pre = snippet.select_one("pre")
        if caption is not None:
            paragraph = soup.new_tag("p")
            strong = soup.new_tag("strong")
            strong.string = _clean_label(caption)
            paragraph.append(strong)
            snippet.insert_before(paragraph)
        if pre is not None:
            snippet.insert_before(pre)
        snippet.decompose()

    for table in reversed(main.find_all("table")):
        _normalize_table(soup, table)

    for footnote in list(main.select(".under-table-footnote")):
        sup = footnote.find("sup")
        number = sup.get_text(strip=True) if sup is not None else ""
        if number.isdigit():
            _mark_anchors(footnote, {f"footnote_{number}"})

    anchors: set[str] = set()
    for tag in list(main.find_all(True)):
        found: set[str] = set()
        tag_id = tag.get("id")
        if isinstance(tag_id, str) and tag_id not in CHROME_IDS:
            found.add(tag_id)
        if tag.name == "a" and isinstance(tag.get("name"), str):
            found.add(tag["name"])
        marked = tag.get(ANCHOR_MARK)
        if isinstance(marked, str):
            found.update(item for item in marked.split(ANCHOR_SEP) if item)
        if found:
            anchors.update(item for item in found if item not in CHROME_IDS)
            _mark_anchors(tag, found)
            if tag.name == "a" and not tag.get("href"):
                tag.name = "span"
                tag.attrs.pop("name", None)
                tag.attrs.pop("id", None)

    return soup, main, anchors


def _flatten_dropdown(soup: BeautifulSoup, dropdown: Tag) -> None:
    head = dropdown.select_one(".MCDropDownHead")
    body = dropdown.select_one(".MCDropDownBody")
    anchors: set[str] = set()
    if head is not None:
        for anchor in head.find_all("a"):
            if isinstance(anchor.get("name"), str):
                anchors.add(anchor["name"])
            if isinstance(anchor.get("id"), str):
                anchors.add(anchor["id"])
        title = _clean_label(head) or "Details"
    else:
        title = "Details"
    if is_id_token(title):
        anchors.add(title)
    depth = 2
    parent = dropdown.parent
    while parent is not None:
        if isinstance(parent, Tag) and "MCDropDown" in _class_set(parent):
            depth += 1
        parent = parent.parent
    depth = min(depth, 6)
    heading = soup.new_tag(f"h{depth}")
    heading.string = title
    if anchors:
        _mark_anchors(heading, anchors)
    dropdown.insert_before(heading)
    cursor: Tag | NavigableString = heading
    if body is not None:
        for child in list(body.children):
            cursor.insert_after(child)
            cursor = child
    dropdown.decompose()


def _normalize_table(soup: BeautifulSoup, table: Tag) -> None:
    for col in list(table.find_all(["col", "colgroup"])):
        col.decompose()
    rows: list[Tag] = []

    def collect(parent: Tag) -> None:
        for child in parent.find_all(recursive=False):
            if not isinstance(child, Tag):
                continue
            if child.name == "tr":
                rows.append(child)
            elif child.name in {"thead", "tbody", "tfoot"}:
                collect(child)

    collect(table)
    if not rows:
        return
    occupied: dict[tuple[int, int], Tag] = {}
    for row_index, row in enumerate(rows):
        column = 0
        for cell in row.find_all(["td", "th"], recursive=False):
            while (row_index, column) in occupied:
                column += 1
            try:
                row_span = max(1, int(cell.get("rowspan") or 1))
            except ValueError:
                row_span = 1
            try:
                col_span = max(1, int(cell.get("colspan") or 1))
            except ValueError:
                col_span = 1
            clone = _clone_fragment(cell)
            if clone is None:
                continue
            clone.attrs.pop("rowspan", None)
            clone.attrs.pop("colspan", None)
            for d_row in range(row_span):
                for d_col in range(col_span):
                    # Keep the text in the first cell only. Repeating a
                    # rowspan paragraph on every row makes the Markdown noisy
                    # while the link is already present in that first cell.
                    occupied[(row_index + d_row, column + d_col)] = (
                        clone if d_row == 0 and d_col == 0 else None
                    )
            column += col_span
    if not occupied:
        return
    max_row = max(key[0] for key in occupied)
    max_col = max(key[1] for key in occupied)
    # Grow rows if rowspan extends past the current row list.
    parent_of_rows = rows[-1].parent
    while len(rows) <= max_row:
        extra = soup.new_tag("tr")
        parent_of_rows.append(extra)
        rows.append(extra)
    for row_index, row in enumerate(rows):
        for child in list(row.contents):
            child.extract()
        for column in range(max_col + 1):
            cell = occupied.get((row_index, column))
            if cell is None:
                row.append(soup.new_tag("td"))
            else:
                cloned = _clone_fragment(cell)
                if cloned is not None:
                    row.append(cloned)


def _clone_fragment(tag: Tag) -> Tag | None:
    parsed = BeautifulSoup(f"<div id='flare-clone-root'>{tag}</div>", "html.parser")
    root = parsed.find(id="flare-clone-root")
    if root is None:
        return None
    for child in root.find_all(recursive=False):
        if isinstance(child, Tag):
            return child
    return None


def _code_language(el: Tag) -> str:
    code = el.find("code") if el.name == "pre" else el
    if code is None:
        return ""
    for css in code.get("class") or []:
        if isinstance(css, str) and css.startswith("language-"):
            return css.split("-", 1)[1]
    return ""


class GitBookConverter(MarkdownConverter):
    def convert_a(self, el, text, parent_tags):
        href = el.get("href")
        if not href:
            return text or ""
        raw_text = text or ""
        prefix = " " if raw_text[:1].isspace() else ""
        suffix = " " if raw_text[-1:].isspace() and raw_text.strip() else ""
        inner = re.sub(r"\s+", " ", raw_text).strip()
        if not inner:
            inner = href
        inner = re.sub(r"(?<!\\)\[", r"\\[", inner)
        inner = re.sub(r"(?<!\\)\]", r"\\]", inner)
        return f"{prefix}[{inner}]({href}){suffix}"

    def convert_img(self, el, text, parent_tags):
        src = el.attrs.get("src") or ""
        if not src or src.endswith("transparent.gif") or "/Skins/" in src:
            return ""
        alt = re.sub(r"\s+", " ", el.attrs.get("alt") or "").strip()
        alt = alt.replace("[", "\\[").replace("]", "\\]")
        return f"![{alt}]({src})"


def render_markdown(soup: BeautifulSoup, main: Tag) -> str:
    anchor_ids: list[str] = []
    for tag in list(main.find_all(attrs={ANCHOR_MARK: True})):
        raw = tag.get(ANCHOR_MARK) or ""
        del tag[ANCHOR_MARK]
        for anchor_id in [item for item in raw.split(ANCHOR_SEP) if item]:
            token = f"FLAREANCHOR{len(anchor_ids)}ENDANCHOR"
            anchor_ids.append(anchor_id)
            span = soup.new_tag("span")
            span.string = token
            tag.insert_before(span)

    converter = GitBookConverter(
        heading_style="ATX",
        bullets="-",
        autolinks=False,
        escape_asterisks=True,
        escape_underscores=True,
        code_language_callback=_code_language,
        keep_inline_images_in=["p", "td", "th", "li", "a", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote"],
    )
    rendered = converter.convert_soup(main)

    def replace_token(match: re.Match[str]) -> str:
        anchor_id = anchor_ids[int(match.group(1))]
        return f'<a id="{html_lib.escape(anchor_id, quote=True)}"></a>'

    rendered = TOKEN_RE.sub(replace_token, rendered)
    rendered = rendered.replace("\r\n", "\n")
    rendered = re.sub(r"[ \t]+\n", "\n", rendered)
    rendered = re.sub(r"\n{3,}", "\n\n", rendered).strip() + "\n"
    return rendered


def apply_links(main: Tag, source_htm: str, corpus: Corpus) -> dict[str, list[str]]:
    report: dict[str, list[str]] = defaultdict(list)
    for anchor in list(main.find_all("a")):
        href = anchor.get("href")
        if not href:
            continue
        text = anchor.get_text(" ", strip=True)
        rewritten, kind = rewrite_url(href, source_htm, corpus, text)
        report[kind].append(href if kind in {"external", "email", "unresolved", "shell"} else (rewritten or href))
        if rewritten is None:
            anchor.unwrap()
        else:
            anchor["href"] = rewritten
    for image in list(main.find_all("img")):
        src = image.get("src")
        if not src:
            continue
        rewritten, kind = rewrite_url(src, source_htm, corpus)
        if kind in {"asset", "crossref"} and rewritten:
            image["src"] = rewritten
        elif kind == "external" and rewritten:
            image["src"] = rewritten
        elif kind == "dropped" or (rewritten is None):
            image.decompose()
        elif rewritten:
            image["src"] = rewritten
    return report


def page_title(soup: BeautifulSoup, main: Tag, fallback: str) -> str:
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
        if title:
            return re.sub(r"\s+", " ", title)
    heading = main.find(["h1", "h2"])
    if heading is not None:
        text = _clean_label(heading)
        if text:
            return text
    return fallback


def page_description(soup: BeautifulSoup) -> str:
    tag = soup.find("meta", attrs={"name": "description"})
    if tag is None:
        return ""
    content = tag.get("content") or ""
    return re.sub(r"\s+", " ", content).strip()


def compose_page(markdown: str, title: str, description: str) -> str:
    body = markdown.lstrip()
    if not re.search(r"(?m)^#\s+\S", body):
        body = f"# {title}\n\n{body}"
    if description:
        escaped = description.replace("\\", "\\\\").replace('"', '\\"')
        body = f'---\ndescription: "{escaped}"\n---\n\n{body}'
    if not body.endswith("\n"):
        body += "\n"
    return body


def load_amd_json(path: Path) -> dict:
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js is required to read Flare TOC files")
    script = (
        "const fs=require('fs'); const vm=require('vm');"
        "const src=fs.readFileSync(process.argv[1],'utf8');"
        "const data=vm.runInNewContext(src,{define:(x)=>x});"
        "process.stdout.write(JSON.stringify(data));"
    )
    result = subprocess.run(
        [node, "-e", script, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def load_toc(html_root: Path) -> list[tuple[int, str, str]]:
    help_system = html_root / "Data" / "HelpSystem.xml"
    toc_rel = "Data/Tocs/Online_Output.js"
    if help_system.exists():
        text = help_system.read_text(encoding="utf-8", errors="replace")
        match = re.search(r'\bToc="([^"]+)"', text)
        if match:
            toc_rel = match.group(1).lstrip("/")
    toc_path = html_root / toc_rel
    if not toc_path.exists():
        return []
    toc = load_amd_json(toc_path)
    chunks = {}
    prefix = toc.get("prefix", "Online_Output_Chunk")
    count = int(toc.get("numchunks") or 0)
    toc_dir = toc_path.parent
    for index in range(count):
        chunk_path = toc_dir / f"{prefix}{index}.js"
        if chunk_path.exists():
            chunks.update(load_amd_json(chunk_path))
    by_index: dict[int, tuple[str, str]] = {}
    for path, meta in chunks.items():
        title = ""
        titles = meta.get("t") or []
        if titles:
            title = titles[0]
        rel = str(path).lstrip("/")
        for entry_index in meta.get("i") or []:
            by_index[int(entry_index)] = (rel, title or posixpath.basename(rel))
    rows: list[tuple[int, str, str]] = []

    def walk(nodes: list, depth: int) -> None:
        for node in nodes or []:
            meta = by_index.get(int(node.get("i")))
            if meta:
                rel, title = meta
                rows.append((depth, title, to_md_path(rel)))
            walk(node.get("n") or [], depth + 1)

    walk((toc.get("tree") or {}).get("n") or [], 0)
    return rows


def escape_link_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip() or "Untitled"
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def write_summary(out_dir: Path, toc_rows: list[tuple[int, str, str]], titles: dict[str, str], pages: list[str]) -> None:
    lines = ["# Table of contents", ""]
    listed: set[str] = set()
    home = "Content/Home.md"
    if home in pages and home not in {row[2] for row in toc_rows}:
        lines.append(f"* [{escape_link_text(titles.get(home, 'Home'))}]({urllib.parse.quote(home, safe='/')})")
        listed.add(home)
    for depth, title, rel in toc_rows:
        if rel not in pages:
            continue
        indent = "  " * depth
        lines.append(
            f"{indent}* [{escape_link_text(title)}]({urllib.parse.quote(rel, safe='/')})"
        )
        listed.add(rel)
    extras = [page for page in pages if page not in listed]
    if extras:
        lines.append("* Topics linked from the help, outside the TOC")
        for rel in extras:
            label = titles.get(rel) or posixpath.splitext(posixpath.basename(rel))[0]
            lines.append(f"  * [{escape_link_text(label)}]({urllib.parse.quote(rel, safe='/')})")
    (out_dir / "SUMMARY.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_gitbook_config(out_dir: Path, readme_rel: str) -> None:
    content = (
        "root: .\n\n"
        "structure:\n"
        f"  readme: {readme_rel}\n"
        "  summary: SUMMARY.md\n"
    )
    (out_dir / ".gitbook.yaml").write_text(content, encoding="utf-8")


def strip_code(markdown: str) -> str:
    text = FENCE_RE.sub("", markdown)
    return INLINE_CODE_RE.sub("", text)


def iter_markdown_links(markdown: str):
    visible = strip_code(markdown)
    for match in MD_LINK_RE.finditer(visible):
        dest = match.group(2)
        if dest.startswith("<") and dest.endswith(">"):
            dest = dest[1:-1]
        yield dest


def iter_markdown_images(markdown: str):
    visible = strip_code(markdown)
    for match in MD_IMAGE_RE.finditer(visible):
        dest = match.group(2)
        if dest.startswith("<") and dest.endswith(">"):
            dest = dest[1:-1]
        yield dest


def validate_output(out_dir: Path) -> dict:
    broken_links = []
    broken_images = []
    broken_fragments = []
    internal_htm = []
    external = []
    pages = 0
    for path in sorted(out_dir.rglob("*.md")):
        if path.name in {"SUMMARY.md", "README.md", "MIGRATION.md"}:
            continue
        pages += 1
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(out_dir).as_posix()
        for dest in iter_markdown_links(text):
            kind, resolved, fragment = classify_output_dest(rel, dest)
            if kind == "external":
                external.append(dest)
                continue
            if kind == "fragment":
                if fragment and fragment not in anchors_in(path):
                    broken_fragments.append({"page": rel, "fragment": fragment})
                continue
            if resolved.suffix.lower() in {".htm", ".html"}:
                internal_htm.append({"page": rel, "dest": dest})
            target = out_dir / resolved
            if not target.exists():
                broken_links.append({"page": rel, "dest": dest, "resolved": resolved.as_posix()})
                continue
            if fragment and resolved.suffix.lower() == ".md" and fragment not in anchors_in(target):
                broken_fragments.append({"page": rel, "dest": dest, "fragment": fragment})
        for dest in iter_markdown_images(text):
            kind, resolved, _fragment = classify_output_dest(rel, dest)
            if kind == "external":
                continue
            target = out_dir / resolved
            if not target.exists():
                broken_images.append({"page": rel, "dest": dest})
    return {
        "pages": pages,
        "external_links": len(external),
        "broken_links": broken_links,
        "broken_images": broken_images,
        "broken_fragments": broken_fragments,
        "internal_htm_links": internal_htm,
    }


def classify_output_dest(source_md: str, dest: str) -> tuple[str, Path, str | None]:
    decoded = urllib.parse.unquote(dest)
    if decoded.startswith(("http://", "https://", "mailto:", "tel:")):
        return "external", Path(), None
    fragment = None
    path = decoded
    if "#" in path:
        path, fragment = path.split("#", 1)
    path = path.split("?", 1)[0]
    if not path:
        return "fragment", Path(source_md), fragment
    full = norm_rel(posixpath.join(posixpath.dirname(source_md), path))
    return "file", Path(full), fragment


def anchors_in(path: Path) -> set[str]:
    if not path.exists() or path.suffix.lower() != ".md":
        return set()
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r'<a id="([^"]+)"></a>', text))


def convert_tree(html_root: Path, out_dir: Path, public_base: str) -> dict:
    html_root = html_root.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    topic_files = discover_topics(html_root)
    asset_files = discover_assets(html_root)
    corpus = Corpus(public_base)
    for rel in topic_files:
        corpus.add_topic(rel)
    corpus.assets.update(asset_files)

    print(f"Collecting anchors for {len(topic_files)} topics...", flush=True)
    for index, rel in enumerate(topic_files, start=1):
        html = (html_root / rel).read_text(encoding="utf-8", errors="replace")
        _soup, _main, anchors = prepare_topic(html)
        corpus.anchors[rel] = anchors
        if index % 100 == 0:
            print(f"  anchors {index}/{len(topic_files)}", flush=True)

    link_counts: dict[str, int] = defaultdict(int)
    external_samples: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    print(f"Converting {len(topic_files)} topics...", flush=True)
    pages: list[str] = []
    for index, rel in enumerate(topic_files, start=1):
        html = (html_root / rel).read_text(encoding="utf-8", errors="replace")
        soup, main, _anchors = prepare_topic(html)
        per_link = apply_links(main, rel, corpus)
        for kind, values in per_link.items():
            link_counts[kind] += len(values)
            if kind == "external":
                for value in values:
                    if len(external_samples) < 80:
                        external_samples.append({"page": to_md_path(rel), "href": value})
            if kind in {"unresolved", "shell"}:
                for value in values[:20]:
                    unresolved.append({"page": to_md_path(rel), "href": value, "kind": kind})
        markdown = render_markdown(soup, main)
        title = page_title(soup, main, posixpath.splitext(posixpath.basename(rel))[0])
        description = page_description(soup)
        page = compose_page(markdown, title, description)
        dest = out_dir / to_md_path(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
        corpus.titles[to_md_path(rel)] = title
        pages.append(to_md_path(rel))
        if index % 100 == 0:
            print(f"  converted {index}/{len(topic_files)}", flush=True)

    print(f"Copying {len(asset_files)} assets...", flush=True)
    for rel in asset_files:
        source = html_root / rel
        dest = out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)

    toc_rows = load_toc(html_root)
    write_summary(out_dir, toc_rows, corpus.titles, pages)
    readme = "Content/Home.md" if "Content/Home.md" in pages else (pages[0] if pages else "README.md")
    write_gitbook_config(out_dir, readme)
    validation = validate_output(out_dir)
    report = {
        "topics": len(pages),
        "assets": len(asset_files),
        "link_counts": dict(link_counts),
        "external_samples": external_samples,
        "unresolved_or_shell": unresolved[:200],
        "validation": {
            "pages": validation["pages"],
            "external_links": validation["external_links"],
            "broken_links": len(validation["broken_links"]),
            "broken_images": len(validation["broken_images"]),
            "broken_fragments": len(validation["broken_fragments"]),
            "internal_htm_links": len(validation["internal_htm_links"]),
        },
        "broken_links": validation["broken_links"][:100],
        "broken_images": validation["broken_images"][:100],
        "broken_fragments": validation["broken_fragments"][:100],
        "internal_htm_links": validation["internal_htm_links"][:50],
    }
    migration_dir = out_dir / "migration"
    migration_dir.mkdir(exist_ok=True)
    (migration_dir / "link-report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_migration_notes(out_dir, report, public_base)
    write_root_readme(out_dir, report)
    return report


def discover_topics(html_root: Path) -> list[str]:
    found = []
    for path in html_root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".htm", ".html"}:
            continue
        rel = path.relative_to(html_root).as_posix()
        if rel.lower().startswith(SKIP_PREFIXES):
            continue
        if posixpath.basename(rel).lower() in SHELL_FILENAMES and "/" not in rel:
            continue
        found.append(rel)
    return sorted(found)


def discover_assets(html_root: Path) -> list[str]:
    found = []
    for path in html_root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in ASSET_EXTENSIONS:
            continue
        rel = path.relative_to(html_root).as_posix()
        lower = rel.lower()
        if lower.startswith(SKIP_PREFIXES) or "/skins/" in lower:
            continue
        found.append(rel)
    return sorted(found)


def write_root_readme(out_dir: Path, report: dict) -> None:
    text = f"""# Druid help (GitBook)

This folder is the Druid product help, migrated from a MadCap Flare HTML5 Top Navigation build to GitBook Markdown.

GitBook uses `.gitbook.yaml`, `SUMMARY.md`, and the Markdown pages under `Content/`. Topic cross-references point at `.md` files. External URLs are unchanged.

- Topics: {report["topics"]}
- Images and other assets: {report["assets"]}
- External links preserved: {report["validation"]["external_links"]}
- Internal links that still use `.htm`: {report["validation"]["internal_htm_links"]}
- Missing internal targets: {report["validation"]["broken_links"]}

See `MIGRATION.md` for how the links were rewritten and how to repeat the conversion from a local Flare output folder.
"""
    (out_dir / "README.md").write_text(text, encoding="utf-8")


def write_migration_notes(out_dir: Path, report: dict, public_base: str) -> None:
    counts = report["link_counts"]
    lines = [
        "# Flare HTML5 to GitBook migration",
        "",
        "Conversion uses Method A: a Python batch script (`scripts/flare_html_to_gitbook.py`) built on BeautifulSoup and markdownify. Pandoc (Method B) is a single-file converter and does not rebuild the Flare TOC or rewrite a whole output folder in one pass, so it was not used for this project.",
        "",
        "## What happens to links",
        "",
        "- Cross-references to other help topics (`href` ending in `.htm` or `.html`, including relative paths with spaces) become relative links to the same path with a `.md` extension. Path segments are URL-encoded so spaces and `&` survive Markdown.",
        "- Anchors are kept. Flare `name` and `id` values are written as `<a id=\"...\"></a>`. When a published fragment is a unique prefix of the real bookmark (a known Flare truncation, for example `#[[Matchi` pointing at `[[MatchingFlow]]`), the fragment is repaired.",
        "- External `http` and `https` links, `mailto:` links, and `tel:` links are copied through unchanged.",
        "- Links that point back at this help host and at a topic that was migrated are rewritten to the local Markdown page. Links to Flare shell pages (`Search.htm`, `Default.htm`, `index.htm`) stay on the published help site so they do not 404 inside GitBook.",
        "- Images keep the same relative location (in this output, `Content/Resources/`). Skin chrome (navigation, search, transparent dropdown icons) is not copied.",
        "",
        f"Published base used when a help link has no local page: `{public_base}`.",
        "",
        "## Counts",
        "",
        f"- Topics converted: {report['topics']}",
        f"- Assets copied: {report['assets']}",
        f"- Cross-reference rewrites: {counts.get('crossref', 0)}",
        f"- In-page fragments: {counts.get('fragment', 0)}",
        f"- External links: {counts.get('external', 0)}",
        f"- Email/phone links: {counts.get('email', 0)}",
        f"- Asset links: {counts.get('asset', 0)}",
        f"- Shell links left on the published site: {counts.get('shell', 0)}",
        f"- Unresolved links left on the published site: {counts.get('unresolved', 0)}",
        "",
        "## Check after conversion",
        "",
        f"- Markdown pages scanned: {report['validation']['pages']}",
        f"- External link occurrences still absolute: {report['validation']['external_links']}",
        f"- Internal links that still end in `.htm`: {report['validation']['internal_htm_links']}",
        f"- Internal link targets missing on disk: {report['validation']['broken_links']}",
        f"- Image targets missing on disk: {report['validation']['broken_images']}",
        f"- Fragments whose target page has no matching anchor: {report['validation']['broken_fragments']}",
        "",
        "Fragment misses that remain are bookmarks already absent from the Flare HTML (short names such as `#Create` or `#Extended`). The topic link still opens the right page.",
        "",
        "The full machine-readable result is `migration/link-report.json`.",
        "",
        "## Run it again on a local Flare build",
        "",
        "The HTML5 folder you generated is the converter input. Point `--html-root` at `HTML5 - Top Navigation` (the folder that contains `Content/`, `Data/`, `Resources/`, and `index.htm`):",
        "",
        "```bash",
        "python3 -m pip install -r requirements-migrate.txt",
        "python3 scripts/flare_html_to_gitbook.py convert \\",
        '  --html-root "/path/to/HTML5 - Top Navigation" \\',
        "  --out ./gitbook-out",
        "```",
        "",
        "Node.js is used only to read Flare's TOC JavaScript (`Data/Tocs/*.js`) when building `SUMMARY.md`. The page conversion itself is Python.",
        "",
    ]
    (out_dir / "MIGRATION.md").write_text("\n".join(lines), encoding="utf-8")


class Downloader:
    def __init__(self, base: str, dest: Path, workers: int = 12):
        self.base = base.rstrip("/")
        self.dest = dest
        self.workers = workers
        self.dest.mkdir(parents=True, exist_ok=True)

    def url_for(self, rel: str) -> str:
        return self.base + "/" + urllib.parse.quote(rel, safe="/")

    def fetch(self, rel: str) -> bool:
        rel = norm_rel(rel)
        if not rel or rel.startswith(".."):
            return False
        dest = self.dest.joinpath(*rel.split("/"))
        if dest.exists() and dest.stat().st_size > 0:
            return True
        url = self.url_for(rel)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        last_error = ""
        for attempt in range(4):
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    final = response.geturl()
                    if "/secure/" in final:
                        return False
                    data = response.read()
                if data.lstrip().startswith(b"<!DOCTYPE html>") and b"Secure Login" in data[:800]:
                    return False
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
                return True
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last_error = str(exc)
                time.sleep(0.4 * (attempt + 1))
        print(f"  failed {rel}: {last_error}", flush=True)
        return False

    def download_many(self, rels: list[str]) -> dict[str, bool]:
        results: dict[str, bool] = {}
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            future_map = {pool.submit(self.fetch, rel): rel for rel in rels}
            for future in as_completed(future_map):
                rel = future_map[future]
                try:
                    results[rel] = future.result()
                except Exception as exc:  # noqa: BLE001
                    print(f"  failed {rel}: {exc}", flush=True)
                    results[rel] = False
        return results


def extract_local_refs(html: str, source_rel: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    main = soup.select_one("#mc-main-content") or soup.body or soup
    raw_refs: list[str] = []
    for tag in main.find_all(True):
        for attr in ("href", "src", "data-src", "data-mc-src"):
            value = tag.get(attr)
            if isinstance(value, str) and value.strip():
                raw_refs.append(value.strip())
        style = tag.get("style")
        if isinstance(style, str) and "url(" in style:
            raw_refs.extend(re.findall(r"url\(\s*['\"]?([^'\")]+)", style))
    found: list[str] = []
    for href in raw_refs:
        lowered = href.lower()
        if lowered.startswith(("javascript:", "mailto:", "tel:", "#", "data:")):
            continue
        if lowered.startswith(("http://", "https://", "//")):
            content = help_content_path(href if not href.startswith("//") else "https:" + href)
            if not content:
                continue
            resolved = content
        else:
            path, _query, _fragment = split_rel_href(href)
            if not path:
                continue
            resolved = resolve_rel(source_rel, path)
        if not resolved or resolved.startswith(".."):
            continue
        lower = resolved.lower()
        if lower.startswith(SKIP_PREFIXES) or "/skins/" in lower:
            continue
        ext = posixpath.splitext(lower)[1]
        if ext in ASSET_EXTENSIONS or ext in {".htm", ".html"}:
            found.append(resolved)
    return found


def toc_seed_paths(html_root: Path) -> list[str]:
    rows = load_toc(html_root)
    seeds = []
    for _depth, _title, rel_md in rows:
        if rel_md.lower().endswith(".md"):
            seeds.append(rel_md[: -len(".md")] + ".htm")
    return seeds


def download_mirror(base: str, dest: Path) -> None:
    loader = Downloader(base, dest)
    print("Downloading help system and TOC...", flush=True)
    if not loader.fetch("Data/HelpSystem.xml"):
        raise RuntimeError("Could not download Data/HelpSystem.xml")
    help_text = (dest / "Data" / "HelpSystem.xml").read_text(encoding="utf-8", errors="replace")
    toc_match = re.search(r'\bToc="([^"]+)"', help_text)
    default_match = re.search(r'\bDefaultUrl="([^"]+)"', help_text)
    toc_rel = toc_match.group(1).lstrip("/") if toc_match else "Data/Tocs/Online_Output.js"
    if not loader.fetch(toc_rel):
        raise RuntimeError(f"Could not download TOC {toc_rel}")
    toc = load_amd_json(dest / toc_rel)
    prefix = toc.get("prefix", "Online_Output_Chunk")
    toc_dir = posixpath.dirname(toc_rel)
    for index in range(int(toc.get("numchunks") or 0)):
        loader.fetch(posixpath.join(toc_dir, f"{prefix}{index}.js"))
    seeds = toc_seed_paths(dest)
    if default_match:
        seeds.append(default_match.group(1).lstrip("/"))
    seeds.append("Content/Home.htm")
    pending = []
    seen: set[str] = set()
    for seed in seeds:
        rel = norm_rel(seed)
        if rel and rel not in seen:
            seen.add(rel)
            pending.append(rel)
    print(f"Crawling {len(pending)} TOC topics and their links...", flush=True)
    wave = 0
    while pending:
        wave += 1
        batch = pending
        pending = []
        print(f"  wave {wave}: {len(batch)} files", flush=True)
        results = loader.download_many(batch)
        for rel, ok in results.items():
            if not ok or not rel.lower().endswith((".htm", ".html")):
                continue
            path = dest.joinpath(*rel.split("/"))
            if not path.exists():
                continue
            html = path.read_text(encoding="utf-8", errors="replace")
            for ref in extract_local_refs(html, rel):
                if ref not in seen:
                    seen.add(ref)
                    pending.append(ref)
    print(f"Mirror ready at {dest} ({len(seen)} queued paths)", flush=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    download = sub.add_parser("download", help="Download a published Flare HTML5 target")
    download.add_argument("--base", required=True)
    download.add_argument("--dest", required=True, type=Path)

    convert = sub.add_parser("convert", help="Convert a local HTML5 folder to GitBook Markdown")
    convert.add_argument("--html-root", required=True, type=Path)
    convert.add_argument("--out", required=True, type=Path)
    convert.add_argument("--public-base", default="https://docs.druidai.com/docs")

    migrate = sub.add_parser("migrate", help="Download a published target and convert it")
    migrate.add_argument("--base", required=True)
    migrate.add_argument("--mirror", required=True, type=Path)
    migrate.add_argument("--out", required=True, type=Path)
    migrate.add_argument("--public-base", default="")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "download":
        download_mirror(args.base, args.dest)
        return 0
    if args.command == "convert":
        report = convert_tree(args.html_root, args.out, args.public_base)
    else:
        download_mirror(args.base, args.mirror)
        public_base = args.public_base or args.base
        report = convert_tree(args.mirror, args.out, public_base)
    validation = report["validation"]
    print(json.dumps(validation, indent=2), flush=True)
    if validation["broken_links"] or validation["internal_htm_links"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
