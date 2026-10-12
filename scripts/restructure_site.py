#!/usr/bin/env python3
"""Split the imported Flare TOC into GitBook sections, spaces, and page groups.

Files stay on their original Content/ paths inside each space directory, so
links between pages in the same space keep working. Links that cross spaces
are rewritten to published site URLs.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTED = ROOT / "imported-content"
SITE_BASE = "https://druidai.gitbook.io/druid-ai-docs"
SUMMARY_NAME = "SUMMARY.md"

LINK_RE = re.compile(
    r"(?<!!)\[((?:\\.|[^\]\\])*)\]\((<[^>]*>|[^)\s]+)\)"
)
FENCE_RE = re.compile(r"^[ \t]*(```|~~~)")


@dataclass
class Node:
    title: str
    path: str | None
    kind: str  # root, heading, page, group
    children: list["Node"] = field(default_factory=list)
    parent: "Node | None" = None
    synthetic: bool = False

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()


def unescape_title(title: str) -> str:
    return title.replace(r"\[", "[").replace(r"\]", "]").replace(r"\\", "\\")


def escape_title(title: str) -> str:
    return title.replace("\\", r"\\").replace("[", r"\[").replace("]", r"\]")


def split_bullet(text: str) -> tuple[str, str | None]:
    if not text.startswith("["):
        return text.strip(), None
    index = 1
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text.startswith("](", index):
            title = text[1:index]
            rest = text[index + 2 :]
            if rest.startswith("<"):
                end = rest.find(">")
                dest = rest[1:end]
            else:
                dest = rest[:-1] if rest.endswith(")") else rest
            return title, dest.strip()
        index += 1
    return text.strip(), None


def normalize_summary_path(dest: str) -> str:
    dest = urllib.parse.unquote(dest.strip())
    dest = dest.split("#", 1)[0].split("?", 1)[0]
    # SUMMARY escapes characters such as & inside link targets. Those are not separators.
    dest = re.sub(r"\\(.)", r"\1", dest)
    return dest.replace("\\", "/")


def parse_summary(text: str) -> Node:
    root = Node("root", None, "root")
    stack: list[tuple[float, Node]] = [(-1, root)]
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or (line.startswith("# ") and not line.startswith("## ")):
            continue
        if line.startswith("## "):
            node = Node(line[3:].strip(), None, "heading")
            node.parent = root
            root.children.append(node)
            stack = [(-1, root), (-0.5, node)]
            continue
        indent = len(line) - len(line.lstrip(" "))
        body = line.lstrip()
        if not body.startswith("* "):
            continue
        title, dest = split_bullet(body[2:])
        path = normalize_summary_path(dest) if dest else None
        node = Node(title, path, "page" if path else "group")
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        node.parent = parent
        parent.children.append(node)
        stack.append((indent, node))
    return root


def index_pages(root: Node) -> dict[str, Node]:
    found: dict[str, Node] = {}
    for node in root.walk():
        if node.path:
            if node.path in found:
                raise SystemExit(f"Duplicate summary path: {node.path}")
            found[node.path] = node
    return found


def demote_external_pages(node: Node) -> None:
    """GitBook exported empty groups as stub pages outside Content/. Keep the group."""
    for child in list(node.children):
        demote_external_pages(child)
        if child.path and not child.path.startswith("Content/"):
            child.kind = "group"
            child.path = None


def take(pages: dict[str, Node], path: str) -> Node:
    node = pages.get(path)
    if node is None or node.parent is None:
        if not (IMPORTED / path).exists():
            raise SystemExit(f"Missing TOC entry: {path}")
        node = Node(escape_title(Path(path).stem), path, "page")
        pages[path] = node
        return node
    node.parent.children.remove(node)
    node.parent = None
    return node


def child_by_title(node: Node, title: str) -> Node:
    for child in node.children:
        if unescape_title(child.title) == title:
            return child
    raise SystemExit(f"{node.path or node.title} has no child titled {title!r}")


def detach_child(node: Node) -> Node:
    if node.parent is None:
        return node
    node.parent.children.remove(node)
    node.parent = None
    return node


def retitle(node: Node, title: str, renames: dict[str, str]) -> Node:
    node.title = escape_title(title)
    if node.path:
        renames[node.path] = title
    return node


def heading(title: str, children: list[Node]) -> Node:
    node = Node(title, None, "heading", children=children)
    for child in children:
        child.parent = node
    return node


def slugify(text: str) -> str:
    text = unescape_title(text).replace("&", " and ")
    text = text.lower()
    # GitBook keeps underscores and dots from the file name and turns the rest into hyphens.
    text = re.sub(r"[^a-z0-9._]+", "-", text).strip("-.").strip("-")
    text = re.sub(r"-{2,}", "-", text)
    return text


def filename_slug(path: str) -> str:
    return slugify(Path(path).stem)


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def summary_link(title: str, path: str) -> str:
    dest = path if re.fullmatch(r"[A-Za-z0-9_./~-]+", path) else f"<{path}>"
    return f"* [{title}]({dest})"


def render_nodes(nodes: list[Node], indent: int = 0) -> list[str]:
    lines: list[str] = []
    pad = " " * indent
    for node in nodes:
        if node.kind == "heading":
            if indent:
                raise SystemExit(f"Nested page group is not supported: {node.title}")
            lines.append(f"## {node.title}")
            lines.append("")
            lines.extend(render_nodes(node.children, 0))
            continue
        if node.path:
            lines.append(pad + summary_link(node.title, node.path))
        else:
            lines.append(f"{pad}* {node.title}")
        if node.children:
            lines.extend(render_nodes(node.children, indent + 2))
    return lines


def render_summary(nodes: list[Node]) -> str:
    body = "\n".join(render_nodes(nodes)).rstrip() + "\n"
    return f"# Table of contents\n\n{body}"


def first_page(nodes: list[Node]) -> str:
    for node in nodes:
        for item in node.walk():
            if item.path:
                return item.path
    raise SystemExit("Space has no pages")


def page_slugs(nodes: list[Node]) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}

    def walk(items: list[Node], ancestors: list[str]) -> None:
        for node in items:
            if node.kind == "heading":
                walk(node.children, ancestors + [slugify(node.title)])
                continue
            if node.kind == "group" or (node.kind != "page" and not node.path):
                walk(node.children, ancestors)
                continue
            if node.path:
                slugs = ancestors + [filename_slug(node.path)]
                found[node.path] = slugs
                walk(node.children, slugs)

    walk(nodes, [])
    return found


def lexical_join(base_dir: str, dest: str) -> str:
    parts: list[str] = []
    for part in (Path(base_dir) / dest).parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def collect_paths(nodes: list[Node]) -> list[str]:
    paths: list[str] = []
    for node in nodes:
        for item in node.walk():
            if item.path and not item.synthetic:
                paths.append(item.path)
    return paths


def build() -> tuple[dict[str, list[Node]], dict[str, str], dict[str, dict]]:
    summary = (IMPORTED / SUMMARY_NAME).read_text(encoding="utf-8")
    root = parse_summary(summary)
    demote_external_pages(root)
    pages = index_pages(root)
    renames: dict[str, str] = {}

    def page(path: str, title: str | None = None) -> Node:
        node = take(pages, path)
        if title:
            retitle(node, title, renames)
        return node

    get_started = [
        page("Content/1_Druid AI Platform/Druid Platform.md", "Druid AI Platform"),
        page("Content/1_Druid AI Platform/Druid Portal.md"),
        page("Content/1_Druid AI Platform/Concepts and Terminology.md"),
    ]
    orchestration = [
        page("Content/AI Agent Orhestration/Druid Conductor.md", "Overview"),
        page("Content/AI Agent Orhestration/Routing Intelligence.md"),
        page("Content/AI Agent Orhestration/Set up AI Agent Orchestration.md"),
        page("Content/AI Agent Orhestration/Conversation History.md"),
    ]
    build_agents = [
        page("Content/2_AI Agents/Building AI Agent.md", "Overview"),
        page("Content/2_AI Agents/AI Authoring Agents.md"),
        page("Content/2_AI Agents/Authoring Tools.md"),
    ]
    governance = [
        page("Content/Governance & Security/Governance & Security.md", "Overview"),
        page("Content/Governance & Security/Data Security and Privacy.md"),
        page("Content/Governance & Security/AI Evaluation and Response Guardrails.md"),
        page("Content/Governance & Security/Observability and Explainability.md"),
    ]
    analytics = [
        page("Content/Data Analytics & Insights/Data Analytics & Insights.md", "Overview"),
        page("Content/Data Analytics & Insights/Track Business KPIs.md"),
        page("Content/Data Analytics & Insights/AI Quality, Testing, and Accuracy.md"),
        page("Content/Data Analytics & Insights/AI-Powered Conversational Analysis.md"),
        page("Content/Data Analytics & Insights/Operational Visibility and History.md"),
    ]
    integrations = [
        page("Content/7_Integrations/Integrations.md", "Overview"),
        page("Content/7_Integrations/Enterprise Connectors.md"),
        page("Content/Webhooks.md"),
        page("Content/Druid AI Services/Druid Vision.md"),
    ]
    conversational = [
        page("Content/CBA/Conversational AI Applications.md", "Overview"),
        page("Content/CBA/Entity Data Integration.md"),
        page("Content/CBA/Views.md"),
        page("Content/CBA/Forms.md"),
        page("Content/CBA/FileUpload.md"),
        page("Content/CBA/Fields rendering on views and forms.md"),
        page("Content/CBA/Managing entity records.md"),
        page("Content/CBA/Charts.md"),
        page("Content/CBA/Create Dashboards.md"),
        page("Content/CBA/Authoring Workspaces.md"),
    ]
    lifecycle = [
        page("Content/Working with Solutions/Release Lifecycle & Versioning.md", "Overview"),
        page("Content/Working with Solutions/Exporting and Downloading.md"),
        page("Content/Working with Solutions/Importing Solutions.md"),
        page("Content/Working with Solutions/Deleting Solutions.md"),
        page("Content/Working with Solutions/Take Snapshots.md"),
        page("Content/Working with Solutions/Download Snapshot.md"),
        page("Content/Working with Solutions/Restore Snapshot.md"),
        page("Content/Working with Solutions/Delete snapshot.md"),
    ]
    how_to = [
        page("Content/How to/Handling Authentication.md"),
        page("Content/How to/Capturing email addresses in channels.md"),
        page("Content/How to/Changing the agent user name.md"),
        page("Content/How to/Sending Email Links in the.md"),
        page("Content/How to/Execute a connector action from outside the DRUID Platform.md"),
        page("Content/How to/Start Druid conversations by API.md"),
        page("Content/How to/Start multiple DRUID conversations by API.md"),
        page("Content/How to/Generating Invoices Using Excel Templates.md"),
        page("Content/How to/Sending the conversation transcript to external systems.md"),
        page("Content/How to/Debugging and understanding contextual meaning from the chat.md"),
        page("Content/How to/Land bot page.md"),
    ]

    knowledge = [page("Content/Knowledgebase/Knowledgebase.md")]
    data_service = [
        page("Content/7_Integrations/Data Service/Druid_Data_Service.md"),
        page("Content/7_Integrations/Data Service/UiPath_Data_Service.md"),
    ]

    releases = page(
        "Content/Solution Library/Agentic Solutions/Release Notes/Business Apps Releases.md",
        "Overview",
    )
    retitle(
        pages["Content/Solution Library/Agentic Solutions/Release Notes/Druid 9.31 - Latest.md"],
        "Druid 9.31 - Latest",
        renames,
    )
    future = child_by_title(releases, "Future Releases")
    latest = child_by_title(releases, "Druid 9.31 - Latest")
    previous = child_by_title(releases, "Previous Releases")
    for child in (future, latest, previous):
        detach_child(child)
    business_releases = [releases, latest, future, previous]

    library_page = page("Content/Solution Library/Solutions Library.md", "Overview")
    business_apps = page("Content/Solution Library/Agentic Solutions/Agentic Solutions.md")
    templates = detach_child(child_by_title(library_page, "Solution Templates"))
    solution_library = [
        library_page,
        heading("Business Apps", [business_apps]),
        heading("Solution Templates", templates.children),
    ]

    voice = page("Content/Druid Voice/Druid Voice.md", "Overview")
    retitle(
        pages["Content/Druid Voice/Speech Resource Management and Governance.md"],
        "Management and Governance",
        renames,
    )
    retitle(
        pages["Content/Druid Voice/Speech Resources Metrics and Usage Monitoring.md"],
        "Metrics and Usage Monitoring",
        renames,
    )
    druid_voice = [
        voice,
        heading("Druid SIP", [page("Content/Druid Voice/Druid SIP.md")]),
        heading("webRTC", [page("Content/Druid Voice/webRTC.md")]),
        heading(
            "Speech Resources",
            [
                page("Content/Druid Voice/TTS and STT Vendors.md"),
                page("Content/Druid Voice/Speech Resource Management and Governance.md"),
                page("Content/Druid Voice/Speech Resources Metrics and Usage Monitoring.md"),
                page("Content/Druid Voice/ElevenLabs Voices.md"),
                page("Content/Druid Voice/Best Practices for Low Voice Latency.md"),
            ],
        ),
        heading(
            "Call Routing",
            [
                page("Content/Druid Voice/Outbound Calling.md"),
                page("Content/Druid Voice/Transfer Calls.md"),
            ],
        ),
    ]

    live_chat = [
        page("Content/Live Chat/Live Chat.md", "Overview"),
        page("Content/Live Chat/Setting up the Live Chat Starter.md", "Set up Live Chat"),
        page("Content/Live Chat/Live Chat Multiple Queues.md", "Multichat"),
        page("Content/Live Chat/Agent Assist.md"),
        page("Content/Live Chat/Real-time Machine Translation in Live Chat.md", "Real-time Machine Translation"),
        page("Content/Live Chat/Live Dashboard.md"),
        page("Content/Live Chat/Measuring Helpdesk KPIs.md"),
    ]
    contact_overview = Node("Overview", "overview.md", "page", synthetic=True)
    contact_centers = [
        contact_overview,
        page("Content/Live Chat/Amazon Live Chat.md", "Amazon Connect"),
        page("Content/Live Chat/Cisco Live Chat.md", "Cisco CC Express"),
        page("Content/Live Chat/ClarBridge Integration.md", "Clarabridge"),
        page("Content/Live Chat/Druid External Live Chat.md", "Druid External"),
        page("Content/Live Chat/Freshchat Integration.md", "Freshchat"),
        page("Content/Live Chat/Genesys Live Chat.md", "Genesys"),
        page("Content/Live Chat/Oracle B2C Live Agent Integration.md", "Oracle Service Center"),
        page("Content/Live Chat/RingCentral CX.md", "RingCentral CX"),
        page("Content/Live Chat/Salesforce MIAW Live Chat.md", "Salesforce MIAW"),
        page("Content/Live Chat/Salesforce Live Chat.md", "Salesforce Service Cloud"),
        page("Content/Live Chat/Talkdesk Live Chat.md", "Talkdesk"),
        page("Content/Live Chat/Zendesk Contact Center.md", "Zendesk"),
    ]

    channels = [
        page("Content/Channels/Channels.md", "Overview"),
        heading(
            "Engagement & Support",
            [
                page("Content/Channels/Cuedesk/Cuedesk Integration.md"),
                page("Content/Channels/Druid_Generic_Chat.md"),
                page("Content/Channels/Infobip.md"),
                page("Content/Channels/Sprinklr/Sprinklr Integration.md"),
                page("Content/Channels/Sunshine/Sunshine_Channel.md", "Sunshine Platform"),
                page("Content/Channels/Sunshine/Sunshine_Channel_Old.md"),
                page("Content/Channels/MetaWorkplace/MetaWorkplace Integration.md"),
            ],
        ),
        heading(
            "Voice & Telephony",
            [
                page("Content/Channels/Voice Audio Codes/Voice Audio Codes Channel.md", "AudioCodes"),
                page("Content/Channels/Voice Text/Voice_Text_Integration.md", "Druid VoiceText"),
                page("Content/Channels/Vonage RCS.md"),
                page("Content/Channels/Vonage_SMS.md"),
                page("Content/Channels/Vonage_Voice.md"),
                page("Content/Channels/RingCentral/RingCentral_channel.md", "Ring Central"),
                page("Content/Channels/Sakari_SMS.md"),
                page("Content/Channels/Twillio/TwilioSMS_Channel.md"),
            ],
        ),
        heading(
            "Social Media & Chat",
            [
                page("Content/Channels/Facebook Integration/Facebook Integration.md"),
                page("Content/Channels/Google Chat/Google_Chat_Integration.md"),
                page("Content/Channels/Instagram/Instagram Integration.md"),
                page("Content/Channels/Line/Line Integration.md", "Line"),
                page("Content/Channels/Slack Integration/Slack Integration.md"),
                page("Content/Channels/MS Teams/MS Teams Integration.md"),
                page("Content/Channels/MS_Copilot.md"),
                page("Content/Channels/Telegram/Telegram_Integration.md"),
                page("Content/Channels/Viber/Viber Integration.md"),
                page("Content/Channels/Webex/Webex_Integration.md"),
                page("Content/Channels/WeChat/WeChat Integration.md"),
                page("Content/Channels/WhatsApp Integration/WhatsAppMeta Integration.md"),
                page("Content/Channels/WhatsApp Integration/WhatsApp Integration.md", "WhatsApp Vonage"),
            ],
        ),
        heading(
            "Web & Email",
            [
                page("Content/Channels/WebChat/WebChat.md"),
                page("Content/Channels/Outlook.md"),
                page("Content/Channels/Email/Email Integration.md"),
                page("Content/Channels/Mobile App Channel.md"),
            ],
        ),
    ]

    full_cloud = [
        page("Content/Druid Deployment/Druid Deployment.md", "Overview"),
        page("Content/Druid Deployment/Druid-hosted.md"),
    ]
    hybrid = [
        page("Content/Druid Deployment/Hybrid Deployment.md"),
        page("Content/Druid Deployment/DRUID AI Platform Network Matrix.md"),
        page("Content/Druid Deployment/DRUID Platform Services and IPs.md"),
        page("Content/Druid Deployment/Deployment Requirements.md"),
        page("Content/Druid Deployment/Druid Connector Host.md"),
        page("Content/Druid Deployment/Druid Data Service Installation.md"),
        page("Content/Druid Deployment/KB Installation.md"),
    ]
    on_prem = [page("Content/Druid Deployment/High Availability On Premises.md", "HA On-premises Deployment")]
    edge = [page("Content/Druid Deployment/Edge Deployment.md")]

    platform_releases_page = page("Content/13_Release Notes/Druid AI Releases.md", "Overview")
    platform_future = child_by_title(platform_releases_page, "Future Releases")
    platform_latest = child_by_title(platform_releases_page, "Druid 10.1 - Latest")
    platform_previous = child_by_title(platform_releases_page, "Previous Releases")
    for child in (platform_future, platform_latest, platform_previous):
        detach_child(child)
    platform_releases = [platform_releases_page, platform_latest, platform_future, platform_previous]

    home = [page("Content/Home.md", "Home")]

    spaces: dict[str, list[Node]] = {
        "home": home,
        "get-started": get_started,
        "ai-agent-orchestration": orchestration,
        "build-ai-agents": build_agents,
        "ai-governance-security": governance,
        "data-analytics-insights": analytics,
        "integrations": integrations,
        "conversational-ai-apps": conversational,
        "release-lifecycle": lifecycle,
        "how-to": how_to,
        "knowledge-base": knowledge,
        "data-service": data_service,
        "solution-library": solution_library,
        "druid-voice": druid_voice,
        "live-chat": live_chat,
        "contact-centers": contact_centers,
        "channels": channels,
        "full-cloud": full_cloud,
        "hybrid": hybrid,
        "ha-on-premises": on_prem,
        "edge": edge,
        "platform-releases": platform_releases,
        "business-apps-releases": business_releases,
    }

    original = {path for path, node in pages.items()}
    assigned: list[str] = []
    for nodes in spaces.values():
        assigned.extend(collect_paths(nodes))
    missing = sorted(original - set(assigned))
    extra = sorted(set(assigned) - original)
    duplicates = sorted({path for path in assigned if assigned.count(path) > 1})
    if missing or extra or duplicates:
        raise SystemExit(
            "TOC assignment mismatch\n"
            f"missing ({len(missing)}): {missing[:20]}\n"
            f"extra ({len(extra)}): {extra[:20]}\n"
            f"duplicates: {duplicates[:20]}"
        )

    meta = {
        "home": {"dir": "home", "title": "Home", "group": None, "section": "Home"},
        "get-started": {"dir": "ai-platform/get-started", "title": "Get Started", "group": "ai-platform", "section": "Get Started"},
        "ai-agent-orchestration": {"dir": "ai-platform/ai-agent-orchestration", "title": "AI Agent Orchestration", "group": "ai-platform", "section": "AI Agent Orchestration"},
        "build-ai-agents": {"dir": "ai-platform/build-ai-agents", "title": "Build AI Agents", "group": "ai-platform", "section": "Build AI Agents"},
        "ai-governance-security": {"dir": "ai-platform/ai-governance-security", "title": "AI Governance & Security", "group": "ai-platform", "section": "AI Governance & Security"},
        "data-analytics-insights": {"dir": "ai-platform/data-analytics-insights", "title": "Data Analytics & Insights", "group": "ai-platform", "section": "Data Analytics & Insights"},
        "integrations": {"dir": "ai-platform/integrations", "title": "Integrations", "group": "ai-platform", "section": "Integrations"},
        "conversational-ai-apps": {"dir": "ai-platform/conversational-ai-apps", "title": "Conversational AI Apps", "group": "ai-platform", "section": "Conversational AI Apps"},
        "release-lifecycle": {"dir": "ai-platform/release-lifecycle", "title": "Release Lifecycle & Versioning", "group": "ai-platform", "section": "Release Lifecycle & Versioning"},
        "how-to": {"dir": "ai-platform/how-to", "title": "How to", "group": "ai-platform", "section": "How to"},
        "knowledge-base": {"dir": "knowledge-and-data/knowledge-base", "title": "Knowledge Base", "group": "knowledge-and-data", "section": "Knowledge Base"},
        "data-service": {"dir": "knowledge-and-data/data-service", "title": "Data Service", "group": "knowledge-and-data", "section": "Data Service"},
        "solution-library": {"dir": "solution-library", "title": "Solution Library", "group": None, "section": "Solution Library"},
        "druid-voice": {"dir": "druid-voice", "title": "Druid Voice", "group": None, "section": "Druid Voice"},
        "live-chat": {"dir": "human-handoff/live-chat", "title": "Live Chat", "group": "human-handoff", "section": "Live Chat"},
        "contact-centers": {"dir": "human-handoff/contact-centers", "title": "Contact Centers", "group": "human-handoff", "section": "Contact Centers"},
        "channels": {"dir": "channels", "title": "Channels", "group": None, "section": "Channels"},
        "full-cloud": {"dir": "druid-deployment/full-cloud", "title": "Full Cloud", "group": "druid-deployment", "section": "Full Cloud"},
        "hybrid": {"dir": "druid-deployment/hybrid", "title": "Hybrid", "group": "druid-deployment", "section": "Hybrid"},
        "ha-on-premises": {"dir": "druid-deployment/ha-on-premises", "title": "HA On-premises", "group": "druid-deployment", "section": "HA On-premises"},
        "edge": {"dir": "druid-deployment/edge", "title": "Edge", "group": "druid-deployment", "section": "Edge"},
        "platform-releases": {"dir": "releases/platform-releases", "title": "Platform Releases", "group": "releases", "section": "Platform Releases"},
        "business-apps-releases": {"dir": "releases/business-apps-releases", "title": "Business Apps Releases", "group": "releases", "section": "Business Apps Releases"},
    }
    return spaces, renames, meta


GROUPS = [
    ("ai-platform", "AI Platform", [
        "get-started",
        "ai-agent-orchestration",
        "build-ai-agents",
        "ai-governance-security",
        "data-analytics-insights",
        "integrations",
        "conversational-ai-apps",
        "release-lifecycle",
        "how-to",
    ]),
    ("knowledge-and-data", "Knowledge & Data", ["knowledge-base", "data-service"]),
    ("human-handoff", "Human Handoff", ["live-chat", "contact-centers"]),
    ("druid-deployment", "Druid Deployment", ["full-cloud", "hybrid", "ha-on-premises", "edge"]),
    ("releases", "Releases & Roadmap", ["platform-releases", "business-apps-releases"]),
]


def normalize_headings(text: str) -> str:
    """Drop the extra H1 GitBook exports, and restore the heading levels under it."""
    prefix = ""
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            prefix = text[: end + 4]
            body = text[end + 4 :]
    lines = body.splitlines(keepends=True)
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines):
        return text
    if not re.match(r"^#\s+\S", lines[index]) or lines[index].startswith("##"):
        return text
    del lines[index]
    output: list[str] = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append(line)
            continue
        if not in_fence:
            match = re.match(r"^(#{2,6})(\s+.*)$", line)
            if match:
                newline = "\n" if line.endswith("\n") else ""
                line = match.group(1)[1:] + match.group(2).rstrip("\n") + newline
        output.append(line)
    return prefix + "".join(output)


# Existing GitBook keys stay stable. New areas continue the numeric sequence.
# Tuple is (section key, space key, public section path, space path).
SITE_IDS = {
    "home": ("section-1", "space-2", "home", "home"),
    "get-started": ("section-2", "space-29", "docs-platform-get-started", "get-started"),
    "ai-agent-orchestration": ("section-4", "space-30", "ai-agent-orchestration", "ai-agent-orchestration"),
    "build-ai-agents": ("section-3", "space-31", "build-ai-agents", "build-ai-agents"),
    "ai-governance-security": ("section-5", "space-32", "ai-governance-and-security", "ai-governance-and-security"),
    "data-analytics-insights": ("section-6", "space-33", "data-analytics-and-insights", "data-analytics-and-insights"),
    "integrations": ("section-8", "space-34", "integrations", "integrations"),
    "conversational-ai-apps": ("section-15", "space-15", "conversational-ai-apps", "conversational-ai-apps"),
    "release-lifecycle": ("section-7", "space-35", "release-lifecycle-and-versioning", "release-lifecycle-and-versioning"),
    "how-to": ("section-16", "space-16", "how-to", "how-to"),
    "knowledge-base": ("section-17", "space-17", "knowledge-base", "knowledge-base"),
    "data-service": ("section-18", "space-18", "data-service", "data-service"),
    "solution-library": ("section-19", "space-19", "solution-library", "solution-library"),
    "druid-voice": ("section-20", "space-20", "druid-voice", "druid-voice"),
    "live-chat": ("section-9", "space-36", "live-chat", "live-chat"),
    "contact-centers": ("section-21", "space-21", "contact-centers", "contact-centers"),
    "channels": ("section-22", "space-22", "channels", "channels"),
    "full-cloud": ("section-23", "space-23", "full-cloud", "full-cloud"),
    "hybrid": ("section-24", "space-24", "hybrid", "hybrid"),
    "ha-on-premises": ("section-25", "space-25", "ha-on-premises", "ha-on-premises"),
    "edge": ("section-26", "space-26", "edge", "edge"),
    "platform-releases": ("section-27", "space-27", "platform-releases", "platform-releases"),
    "business-apps-releases": ("section-28", "space-28", "business-apps-releases", "business-apps-releases"),
}
GROUP_IDS = {
    "ai-platform": ("section-group-1", "layer-plus"),
    "knowledge-and-data": ("section-group-3", None),
    "human-handoff": ("section-group-2", None),
    "druid-deployment": ("section-group-4", None),
    "releases": ("section-group-5", None),
}


def public_url(space_key: str, slugs: list[str]) -> str:
    section_path = SITE_IDS[space_key][2]
    # The default Home section is published at the site root. /home redirects there.
    if space_key == "home":
        base = SITE_BASE
    else:
        base = f"{SITE_BASE}/{section_path}"
    return base + "/" + "/".join(slugs)


def write_site_yaml(meta: dict[str, dict]) -> None:
    order = [
        "home",
        "ai-platform",
        "knowledge-and-data",
        "solution-library",
        "druid-voice",
        "human-handoff",
        "channels",
        "druid-deployment",
        "releases",
    ]
    group_ids = {key for key, _, _ in GROUPS}
    lines = [
        "$schema: https://api.gitbook.com/gitbook-docs.yaml",
        "site:",
        "  title: Druid AI Docs",
        "  structure:",
    ]

    def write_space(key: str, indent: int) -> None:
        info = meta[key]
        _, space_key, _, space_path = SITE_IDS[key]
        pad = " " * indent
        lines.append(f"{pad}- type: space")
        lines.append(f"{pad}  key: {space_key}")
        lines.append(f"{pad}  title: {yaml_quote(info['title'])}")
        lines.append(f"{pad}  path: {space_path}")
        lines.append(f"{pad}  default: true")
        lines.append(f"{pad}  content:")
        lines.append(f"{pad}    directory: ./{info['dir']}")

    def write_section(key: str, indent: int, default: bool = False) -> None:
        info = meta[key]
        section_key, _, section_path, _ = SITE_IDS[key]
        pad = " " * indent
        lines.append(f"{pad}- type: section")
        lines.append(f"{pad}  key: {section_key}")
        lines.append(f"{pad}  title: {yaml_quote(info['section'])}")
        lines.append(f"{pad}  path: {section_path}")
        if default:
            lines.append(f"{pad}  default: true")
        lines.append(f"{pad}  children:")
        write_space(key, indent + 4)

    for key in order:
        if key in group_ids:
            title = next(title for group_key, title, _ in GROUPS if group_key == key)
            children = next(children for group_key, _, children in GROUPS if group_key == key)
            group_key, icon = GROUP_IDS[key]
            lines.append("    - type: section-group")
            lines.append(f"      key: {group_key}")
            lines.append(f"      title: {yaml_quote(title)}")
            if icon:
                lines.append(f"      icon: {icon}")
            lines.append("      children:")
            for child in children:
                write_section(child, 8)
            continue
        write_section(key, 4, default=key == "home")
    (ROOT / "gitbook-docs.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def set_front_matter_title(text: str, title: str) -> str:
    quoted = f"title: {yaml_quote(title)}"
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            matter = text[4:end]
            if re.search(r"(?m)^title:", matter):
                matter = re.sub(r"(?m)^title:.*$", quoted, matter, count=1)
            else:
                matter = quoted + "\n" + matter
            return "---\n" + matter + text[end:]
    return f"---\n{quoted}\n---\n\n" + text


def rewrite_links(text: str, content_path: str, owner: dict[str, str], urls: dict[str, str]) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    in_fence = False
    source_dir = str(Path("imported-content") / content_path).rsplit("/", 1)[0]
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append(line)
            continue
        if not in_fence:
            line = replace_line_links(line, source_dir, content_path, owner, urls)
        output.append(line)
    return "".join(output)


def replace_line_links(
    line: str,
    source_dir: str,
    content_path: str,
    owner: dict[str, str],
    urls: dict[str, str],
) -> str:
    def replace(match: re.Match[str]) -> str:
        title = match.group(1)
        raw_dest = match.group(2)
        dest = raw_dest[1:-1] if raw_dest.startswith("<") else raw_dest
        if re.match(r"^[a-z][a-z0-9+.-]*:", dest) or dest.startswith("#") or dest.startswith("//"):
            return match.group(0)
        fragment = ""
        path_part = dest
        if "#" in dest:
            path_part, fragment = dest.split("#", 1)
            fragment = "#" + fragment
        if not path_part or path_part.endswith("/"):
            return match.group(0)
        unquoted = urllib.parse.unquote(path_part)
        if not unquoted.lower().endswith(".md"):
            return match.group(0)
        target = lexical_join(source_dir, unquoted)
        prefix = "imported-content/"
        if not target.startswith(prefix):
            return match.group(0)
        relative = target[len(prefix) :]
        if relative not in owner or owner[relative] == owner.get(content_path):
            return match.group(0)
        url = urls.get(relative)
        if not url:
            return match.group(0)
        return f"[{title}]({url}{fragment})"

    return LINK_RE.sub(replace, line)


def relative_resources(space_dir: Path) -> str:
    depth = len(space_dir.relative_to(ROOT).parts) + 1
    return "/".join([".."] * depth) + "/imported-content/Content/Resources"


def link_shared_assets(space_dir: Path) -> None:
    gitbook = space_dir / ".gitbook"
    gitbook.mkdir(parents=True, exist_ok=True)
    assets = gitbook / "assets"
    if assets.is_symlink():
        return
    if assets.exists():
        shutil.rmtree(assets)
    depth = len(space_dir.relative_to(ROOT).parts) + 1
    target = "/".join([".."] * depth) + "/imported-content/.gitbook/assets"
    os.symlink(target, assets)


def apply() -> None:
    spaces, renames, meta = build()
    missing_ids = [key for key in spaces if key not in SITE_IDS]
    if missing_ids:
        raise SystemExit(f"Spaces missing site ids: {missing_ids}")
    owner: dict[str, str] = {}
    urls: dict[str, str] = {}
    for key, nodes in spaces.items():
        for path, slugs in page_slugs(nodes).items():
            owner[path] = key
            urls[path] = public_url(key, slugs)

    for key, nodes in spaces.items():
        space_dir = ROOT / meta[key]["dir"]
        content_dir = space_dir / "Content"
        content_dir.mkdir(parents=True, exist_ok=True)
        for path in collect_paths(nodes):
            source = IMPORTED / path
            target = space_dir / path
            target.parent.mkdir(parents=True, exist_ok=True)
            if not source.exists():
                raise SystemExit(f"Missing source file: {source}")
            shutil.move(str(source), str(target))
        link = content_dir / "Resources"
        if not link.exists():
            os.symlink(relative_resources(space_dir), link)
        link_shared_assets(space_dir)
        readme = first_page(nodes)
        (space_dir / ".gitbook.yaml").write_text(
            "root: .\n\nstructure:\n"
            f"  readme: {yaml_quote(readme)}\n"
            "  summary: SUMMARY.md\n",
            encoding="utf-8",
        )
        (space_dir / SUMMARY_NAME).write_text(render_summary(nodes), encoding="utf-8")

    template_readme = ROOT / "home" / "README.md"
    if template_readme.exists():
        template_readme.unlink()

    overview = ROOT / "human-handoff/contact-centers/overview.md"
    overview.write_text('---\ntitle: "Overview"\n---\n', encoding="utf-8")

    rewritten = 0
    normalized = 0
    for path, space_key in owner.items():
        file_path = ROOT / meta[space_key]["dir"] / path
        original = file_path.read_text(encoding="utf-8")
        updated = original
        if path in renames:
            updated = set_front_matter_title(updated, renames[path])
        updated = rewrite_links(updated, path, owner, urls)
        leveled = normalize_headings(updated)
        if leveled != updated:
            normalized += 1
            updated = leveled
        if updated != original:
            file_path.write_text(updated, encoding="utf-8")
            rewritten += 1

    old_summary = IMPORTED / SUMMARY_NAME
    old_config = IMPORTED / ".gitbook.yaml"
    if old_summary.exists():
        old_summary.unlink()
    if old_config.exists():
        old_config.unlink()
    write_site_yaml(meta)
    print(
        f"spaces {len(spaces)} pages {len(owner)} retitled {len(renames)} "
        f"files rewritten {rewritten} headings normalized {normalized}"
    )


if __name__ == "__main__":
    apply()
