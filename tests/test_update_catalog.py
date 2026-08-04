from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from update_catalog import (
    END_MARKER,
    START_MARKER,
    matches_search_filters,
    parse_feed,
    render_candidates,
    replace_generated_block,
)


class CatalogAutomationTests(unittest.TestCase):
    def test_parse_arxiv_feed(self) -> None:
        payload = (ROOT / "tests" / "fixtures" / "arxiv_feed.xml").read_bytes()
        papers = parse_feed(payload, "Agentic Low-Level Vision", "2026-08-04")

        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["arxiv_id"], "2608.01234")
        self.assertEqual(papers[0]["title"], "A Test Agent for Image Restoration")
        self.assertEqual(papers[0]["authors"], ["Alice Example", "Bob Example"])

    def test_replace_generated_block(self) -> None:
        original = f"before\n{START_MARKER}\nold\n{END_MARKER}\nafter\n"
        updated = replace_generated_block(original, "new")
        self.assertEqual(updated, f"before\n{START_MARKER}\nnew\n{END_MARKER}\nafter\n")

    def test_render_empty_queue(self) -> None:
        self.assertEqual(render_candidates([]), "_No papers are waiting for review._")

    def test_section_keyword_groups(self) -> None:
        paper = {
            "title": "An Agent for Image Restoration",
            "summary": "A planning system for low-level vision.",
        }
        search = {
            "title_include_any": ["restoration"],
            "include_all_groups": [["image restoration"], ["agent", "agentic"]],
        }
        self.assertTrue(matches_search_filters(paper, search))

        unrelated = {"title": "Generic Agent Infrastructure", "summary": "Tool use for databases."}
        self.assertFalse(matches_search_filters(unrelated, search))


if __name__ == "__main__":
    unittest.main()
