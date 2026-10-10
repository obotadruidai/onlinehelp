#!/usr/bin/env python3
"""Link-preservation tests for the Flare HTML5 to GitBook converter."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from flare_html_to_gitbook import (  # noqa: E402
    Corpus,
    apply_links,
    compose_page,
    prepare_topic,
    render_markdown,
    rewrite_url,
)


SOURCE = "Content/4_Flows/Internal Actions.htm"


def corpus_with_topics(*topics: str) -> Corpus:
    corpus = Corpus("https://docs.druidai.com/docs")
    for topic in topics:
        corpus.add_topic(topic)
        corpus.anchors[topic] = set()
    corpus.anchors[SOURCE] = {"GetIntentMatchingParams", "GetConversationTranscript"}
    corpus.anchors["Content/5_Entities/System Entities.htm"] = {
        "[[MatchingFlow]]",
        "[[KBQnA]]",
    }
    return corpus


class RewriteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.corpus = corpus_with_topics(
            SOURCE,
            "Content/4_Flows/Post Actions.htm",
            "Content/4_Flows/Pre Actions.htm",
            "Content/Governance & Security/User Management/Authoring User Management.htm",
            "Content/5_Entities/System Entities.htm",
        )

    def test_external_link_is_unchanged(self) -> None:
        href = "https://example.com/docs/guide.htm?a=1&b=2#section"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "external")
        self.assertEqual(rewritten, href)

    def test_mailto_is_unchanged(self) -> None:
        href = "mailto:support@druidai.com"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "email")
        self.assertEqual(rewritten, href)

    def test_cross_reference_with_spaces_and_ampersand(self) -> None:
        href = "../Governance & Security/User Management/Authoring User Management.htm"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus, "Authoring User Management")
        self.assertEqual(kind, "crossref")
        self.assertEqual(
            rewritten,
            "../Governance%20%26%20Security/User%20Management/Authoring%20User%20Management.md",
        )

    def test_same_folder_cross_reference_keeps_fragment(self) -> None:
        rewritten, kind = rewrite_url("Post Actions.htm#Overview", SOURCE, self.corpus)
        self.assertEqual(kind, "crossref")
        self.assertEqual(rewritten, "Post%20Actions.md#Overview")

    def test_published_help_url_becomes_relative_markdown(self) -> None:
        href = "https://docs.druidai.com/docs/Content/4_Flows/Pre%20Actions.htm"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "crossref")
        self.assertEqual(rewritten, "Pre%20Actions.md")

    def test_other_druid_site_stays_external(self) -> None:
        href = "https://druidai.com/pricing"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "external")
        self.assertEqual(rewritten, href)

    def test_javascript_and_bare_hash_are_dropped(self) -> None:
        self.assertEqual(rewrite_url("javascript:void(0);", SOURCE, self.corpus)[0], None)
        self.assertEqual(rewrite_url("#", SOURCE, self.corpus)[0], None)

    def test_truncated_fragment_is_repaired_when_unique(self) -> None:
        href = "../5_Entities/System Entities.htm#[[Matchi"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus, "[[MatchingFlow]]")
        self.assertEqual(kind, "crossref")
        self.assertEqual(
            rewritten,
            "../5_Entities/System%20Entities.md#%5B%5BMatchingFlow%5D%5D",
        )

    def test_in_page_anchor_stays_on_the_page(self) -> None:
        rewritten, kind = rewrite_url("#GetIntentMatchingParams", SOURCE, self.corpus)
        self.assertEqual(kind, "fragment")
        self.assertEqual(rewritten, "#GetIntentMatchingParams")

    def test_missing_topic_stays_on_the_published_site(self) -> None:
        href = "Does Not Exist.htm"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "unresolved")
        self.assertTrue(rewritten.startswith("https://docs.druidai.com/docs/"))
        self.assertIn("Does%20Not%20Exist.htm", rewritten)

    def test_versioned_help_image_stays_on_that_site_when_missing_locally(self) -> None:
        href = "https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/key audiocodes.png"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "external")
        self.assertEqual(rewritten, f"<{href}>")

    def test_spaced_bookmark_matches_flare_id(self) -> None:
        self.corpus.anchors["Content/Governance & Security/Explainability and Utterances Annotation.htm"] = {
            "ExplainabilityatDruidConductorLevel"
        }
        self.corpus.add_topic("Content/Governance & Security/Explainability and Utterances Annotation.htm")
        href = "../Governance & Security/Explainability and Utterances Annotation.htm#Explainability at Druid Conductor Level"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "crossref")
        self.assertTrue(rewritten.endswith("#ExplainabilityatDruidConductorLevel"))

    def test_image_reference_keeps_the_asset_path(self) -> None:
        href = "../Resources/Images/Flows/internal actions.png"
        rewritten, kind = rewrite_url(href, SOURCE, self.corpus)
        self.assertEqual(kind, "asset")
        self.assertEqual(rewritten, "../Resources/Images/Flows/internal%20actions.png")


SAMPLE = """
<html><head><title>Internal Actions</title>
<meta name="description" content="Flow engine actions." />
</head><body>
<div id="mc-main-content">
  <h1 id="InternalActions">Internal Actions</h1>
  <p>See <a href="../Governance &amp; Security/User Management/Authoring User Management.htm">Authoring User Management</a>
  and <a href="https://example.com/docs/guide.htm?a=1&amp;b=2#section">the external guide</a>.</p>
  <p>see<a href="Post Actions.htm"> Post Actions</a>.</p>
  <p>Entity <a href="../5_Entities/System Entities.htm#[[Matchi" class="MCXref xref">[[MatchingFlow]]</a>.</p>
  <div class="note">Ensure roles exist. See <a href="Post Actions.htm">Post Actions</a>.</div>
  <div class="MCDropDown MCDropDown_Closed dropDown">
    <span class="MCDropDownHead dropDownHead">
      <a href="#" class="MCDropDownHotSpot"><img class="MCDropDown_Image_Icon" src="../../Skins/Default/Stylesheets/Images/transparent.gif" alt="Closed" /></a>
      <a name="GetConve"></a>
      <a href="#">GetConversationTranscript</a>
    </span>
    <div class="MCDropDownBody dropDownBody"><p>Transcript body.</p></div>
  </div>
  <p><img alt="Roles" src="../Resources/Images/Flows/internal actions.png" /></p>
  <div class="codeSnippet"><a class="codeSnippetCopyButton" href="javascript:void(0);">Copy</a>
    <pre><code>[[Intent]].Match</code></pre>
  </div>
</div>
</body></html>
"""


class ConvertTests(unittest.TestCase):
    def test_sample_topic_preserves_both_link_kinds(self) -> None:
        corpus = corpus_with_topics(
            SOURCE,
            "Content/4_Flows/Post Actions.htm",
            "Content/Governance & Security/User Management/Authoring User Management.htm",
            "Content/5_Entities/System Entities.htm",
        )
        soup, main, anchors = prepare_topic(SAMPLE)
        self.assertIn("GetConversationTranscript", anchors)
        self.assertIn("GetConve", anchors)
        self.assertIn("InternalActions", anchors)
        apply_links(main, SOURCE, corpus)
        page = compose_page(
            render_markdown(soup, main),
            "Internal Actions",
            "Flow engine actions.",
        )
        self.assertIn(
            "[Authoring User Management](../Governance%20%26%20Security/User%20Management/Authoring%20User%20Management.md)",
            page,
        )
        self.assertIn("[the external guide](https://example.com/docs/guide.htm?a=1&b=2#section)", page)
        self.assertIn("../5_Entities/System%20Entities.md#%5B%5BMatchingFlow%5D%5D", page)
        self.assertIn("[Post Actions](Post%20Actions.md)", page)
        self.assertIn("see [Post Actions](Post%20Actions.md)", page)
        self.assertNotIn("javascript:", page)
        self.assertNotIn(".htm)", page)
        self.assertIn("![Roles](../Resources/Images/Flows/internal%20actions.png)", page)
        self.assertIn("## GetConversationTranscript", page)
        self.assertIn('<a id="GetConve"></a>', page)
        self.assertIn('<a id="GetConversationTranscript"></a>', page)
        self.assertIn("```", page)
        self.assertIn("[[Intent]].Match", page)
        self.assertIn('description: "Flow engine actions."', page)


if __name__ == "__main__":
    unittest.main()
