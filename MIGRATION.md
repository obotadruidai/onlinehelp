# Flare HTML5 to GitBook migration

The synced GitBook site is `gitbook-docs.yaml` at the root of `obotadruidai/onlinehelp`. The help is the Documentation space under `documentation/` (home page `documentation/Content/Home.md`, table of contents `documentation/SUMMARY.md`). The GitBook starter pages (template docs, help center, changelog, petstore API reference, and the one-page import) are not part of this help.

Conversion uses Method A: a Python batch script (`scripts/flare_html_to_gitbook.py`) built on BeautifulSoup and markdownify. Pandoc (Method B) is a single-file converter and does not rebuild the Flare TOC or rewrite a whole output folder in one pass, so it was not used for this project.

## What happens to links

- Cross-references to other help topics (`href` ending in `.htm` or `.html`, including relative paths with spaces) become relative links to the same path with a `.md` extension. Path segments are URL-encoded so spaces and `&` survive Markdown.
- Anchors are kept. Flare `name` and `id` values are written as `<a id="..."></a>`. When a published fragment is a unique prefix of the real bookmark (a known Flare truncation, for example `#[[Matchi` pointing at `[[MatchingFlow]]`), the fragment is repaired.
- External `http` and `https` links, `mailto:` links, and `tel:` links are copied through unchanged.
- Links that point back at this help host and at a topic that was migrated are rewritten to the local Markdown page. Links to Flare shell pages (`Search.htm`, `Default.htm`, `index.htm`) stay on the published help site so they do not 404 inside GitBook.
- Images keep the same relative location (in this output, `Content/Resources/`). Skin chrome (navigation, search, transparent dropdown icons) is not copied.
- Pictures that point at a different published help version, and three links to `CNN_Host_Installation_on_Linux.htm` (that file is not in this HTML5 output), stay as absolute URLs on the published site.

Published base used when a help link has no local page: `https://docs.druidai.com/docs`.

## Counts

- Topics converted: 980
- Assets copied: 4054
- Cross-reference rewrites: 1920
- In-page fragments: 236
- External links: 500
- Email/phone links: 182
- Asset links: 8
- Shell links left on the published site: 0
- Unresolved links left on the published site: 3

## Check after conversion

- Markdown pages scanned: 980
- External link occurrences still absolute: 686
- Internal links that still end in `.htm`: 0
- Internal link targets missing on disk: 0
- Image targets missing on disk: 0
- Fragments whose target page has no matching anchor: 18

Those 18 fragments are bookmarks that are already missing in the Flare HTML (short names such as `#Create`, `#Extended`, `#API`, `#PDF Extractors`). The topic link still opens the right page. Every other cross-reference, including repaired bookmarks such as `#[[Matchi` to `[[MatchingFlow]]`, resolves to a file and an anchor that exist in this tree.

The full machine-readable result is `migration/link-report.json`.

The pages were converted from the published HTML5 Top Navigation output (Flare build 10/9/2026 3:03 PM, the same target name as `HTML5 - Top Navigation`). The Windows output folder and `github.com/obotadruidai/onlinehelp` were not available in this environment. Re-run the converter on your local output folder if that build differs, then copy the Markdown into the GitBook repository.

## Run it again on a local Flare build

The HTML5 folder you generated is the converter input. Point `--html-root` at `HTML5 - Top Navigation` (the folder that contains `Content/`, `Data/`, `Resources/`, and `index.htm`):

```bash
python3 -m pip install -r requirements-migrate.txt
python3 scripts/flare_html_to_gitbook.py convert \
  --html-root "/path/to/HTML5 - Top Navigation" \
  --out ./gitbook-out
```

Node.js is used only to read Flare's TOC JavaScript (`Data/Tocs/*.js`) when building `SUMMARY.md`. The page conversion itself is Python.
