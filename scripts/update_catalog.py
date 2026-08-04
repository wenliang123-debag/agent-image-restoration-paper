#!/usr/bin/env python3
"""Discover recent arXiv papers and update the review queue in README.md."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
CONFIG_PATH = ROOT / "automation" / "searches.json"
CANDIDATES_PATH = ROOT / "automation" / "candidates.json"
EXCLUSIONS_PATH = ROOT / "automation" / "exclusions.json"
START_MARKER = "<!-- AUTO-CANDIDATES:START -->"
END_MARKER = "<!-- AUTO-CANDIDATES:END -->"
ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?", re.I)
ATOM = {"atom": "http://www.w3.org/2005/Atom"}
USER_AGENT = "awesome-agentic-cv-catalog/1.0 (https://github.com/wenliang123-debag/agent-image-restoration-paper)"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def arxiv_id_from_url(value: str) -> str | None:
    match = ARXIV_ID_RE.search(value)
    return match.group(1) if match else None


def parse_feed(payload: bytes, section: str, discovered_on: str) -> list[dict[str, Any]]:
    root = ET.fromstring(payload)
    papers: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ATOM):
        identifier = arxiv_id_from_url(entry.findtext("atom:id", default="", namespaces=ATOM))
        if not identifier:
            continue
        title = normalize_space(entry.findtext("atom:title", default="", namespaces=ATOM))
        summary = normalize_space(entry.findtext("atom:summary", default="", namespaces=ATOM))
        published = entry.findtext("atom:published", default="", namespaces=ATOM)
        authors = [
            normalize_space(author.findtext("atom:name", default="", namespaces=ATOM))
            for author in entry.findall("atom:author", ATOM)
        ]
        papers.append(
            {
                "arxiv_id": identifier,
                "title": title,
                "authors": [author for author in authors if author],
                "published": published[:10],
                "section": section,
                "summary": summary,
                "discovered_on": discovered_on,
                "arxiv_url": f"https://arxiv.org/abs/{identifier}",
            }
        )
    return papers


def fetch_feed(query: str, max_results: int) -> bytes:
    parameters = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    request = urllib.request.Request(
        f"https://export.arxiv.org/api/query?{parameters}",
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def existing_arxiv_ids(
    readme: str,
    candidates: list[dict[str, Any]],
    exclusions: list[str] | None = None,
) -> set[str]:
    identifiers = set(ARXIV_ID_RE.findall(readme))
    identifiers.update(item["arxiv_id"] for item in candidates)
    identifiers.update(exclusions or [])
    return identifiers


def is_recent(published: str, cutoff: datetime) -> bool:
    try:
        value = datetime.strptime(published, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return False
    return value >= cutoff


def matches_search_filters(paper: dict[str, Any], search: dict[str, Any]) -> bool:
    searchable = f"{paper['title']} {paper['summary']}".casefold()
    groups = search.get("include_all_groups", [])
    title = paper["title"].casefold()
    title_terms = search.get("title_include_any", [])
    title_matches = not title_terms or any(term.casefold() in title for term in title_terms)
    return title_matches and all(any(term.casefold() in searchable for term in group) for group in groups)


def escape_cell(value: str) -> str:
    return html.escape(normalize_space(value)).replace("|", "&#124;")


def format_authors(authors: list[str]) -> str:
    if not authors:
        return "Unknown authors"
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{', '.join(authors[:3])}, *et al.*"


def render_candidates(candidates: list[dict[str, Any]]) -> str:
    if not candidates:
        return "_No papers are waiting for review._"

    lines = [
        "| Candidate | Suggested section | Published |",
        "|---|---|---|",
    ]
    for item in sorted(candidates, key=lambda candidate: (candidate["published"], candidate["arxiv_id"]), reverse=True):
        title = escape_cell(item["title"])
        authors = escape_cell(format_authors(item.get("authors", [])))
        section = escape_cell(item["section"])
        lines.append(
            f"| [{title}]({item['arxiv_url']})<br>{authors} | {section} | {item['published']} |"
        )
    return "\n".join(lines)


def replace_generated_block(readme: str, generated: str) -> str:
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one automated-candidate marker pair")
    before, remainder = readme.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    return f"{before}{START_MARKER}\n{generated}\n{END_MARKER}{after}"


def discover(
    config: dict[str, Any],
    readme: str,
    candidates: list[dict[str, Any]],
    exclusions: list[str],
    feed_file: Path | None,
) -> list[dict[str, Any]]:
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=int(config["lookback_days"]))
    discovered_on = now.date().isoformat()
    seen = existing_arxiv_ids(readme, candidates, exclusions)
    found: list[dict[str, Any]] = []

    for index, search in enumerate(config["queries"]):
        if feed_file:
            if index > 0:
                break
            payload = feed_file.read_bytes()
        else:
            if index > 0:
                time.sleep(float(config.get("request_delay_seconds", 3)))
            payload = fetch_feed(search["query"], int(config["max_results_per_query"]))
        added_for_query = 0
        for paper in parse_feed(payload, search["section"], discovered_on):
            if added_for_query >= int(config["max_new_per_query"]):
                break
            if (
                paper["arxiv_id"] in seen
                or not is_recent(paper["published"], cutoff)
                or not matches_search_filters(paper, search)
            ):
                continue
            seen.add(paper["arxiv_id"])
            found.append(paper)
            added_for_query += 1

    found.sort(key=lambda paper: (paper["published"], paper["arxiv_id"]), reverse=True)
    return found[: int(config["max_new_candidates"])]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feed-file", type=Path, help="Use a local Atom feed instead of the arXiv API")
    parser.add_argument("--render-only", action="store_true", help="Render the current candidate file without network access")
    arguments = parser.parse_args()

    config = load_json(CONFIG_PATH)
    candidates = load_json(CANDIDATES_PATH)
    exclusions = load_json(EXCLUSIONS_PATH)
    if not isinstance(candidates, list):
        raise ValueError("automation/candidates.json must contain a JSON array")
    if not isinstance(exclusions, list) or not all(isinstance(item, str) for item in exclusions):
        raise ValueError("automation/exclusions.json must contain an array of arXiv ID strings")
    readme = README_PATH.read_text(encoding="utf-8")
    new_candidates: list[dict[str, Any]] = []

    if not arguments.render_only:
        new_candidates = discover(config, readme, candidates, exclusions, arguments.feed_file)
        candidates.extend(new_candidates)
        CANDIDATES_PATH.write_text(
            json.dumps(candidates, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    updated_readme = replace_generated_block(readme, render_candidates(candidates))
    README_PATH.write_text(updated_readme, encoding="utf-8")
    print(f"Discovered {len(new_candidates)} new candidate(s); {len(candidates)} total awaiting review.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, ET.ParseError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
