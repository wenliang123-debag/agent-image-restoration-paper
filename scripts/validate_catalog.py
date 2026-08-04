#!/usr/bin/env python3
"""Run deterministic checks for the curated catalog and automation files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from update_catalog import (
    CANDIDATES_PATH,
    END_MARKER,
    EXCLUSIONS_PATH,
    README_PATH,
    ROOT,
    START_MARKER,
    render_candidates,
)


ROW_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?", re.I)
RELATIVE_IMAGE_RE = re.compile(r'<img[^>]+src=["\'](\./[^"\']+)["\']', re.I)


def validate() -> list[str]:
    errors: list[str] = []
    readme = README_PATH.read_text(encoding="utf-8")

    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        errors.append("README must contain exactly one automated-candidate marker pair")
    elif readme.index(START_MARKER) > readme.index(END_MARKER):
        errors.append("README automated-candidate markers are reversed")

    rows_by_id: dict[str, list[int]] = {}
    for line_number, line in enumerate(readme.splitlines(), start=1):
        # Curated paper and generated-candidate rows start with a linked title.
        # Resource tables may intentionally cite a paper again and are excluded.
        if not line.startswith("| ["):
            continue
        for identifier in set(ROW_ARXIV_RE.findall(line)):
            rows_by_id.setdefault(identifier, []).append(line_number)
    for identifier, lines in rows_by_id.items():
        if len(lines) > 1:
            errors.append(f"arXiv {identifier} appears in multiple table rows: {lines}")

    for relative_path in RELATIVE_IMAGE_RE.findall(readme):
        asset = (ROOT / relative_path).resolve()
        if not asset.is_file():
            errors.append(f"missing local image referenced by README: {relative_path}")

    try:
        candidates = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"cannot read automation/candidates.json: {error}")
        return errors

    if not isinstance(candidates, list):
        errors.append("automation/candidates.json must contain a JSON array")
        return errors

    candidate_ids: set[str] = set()
    required = {"arxiv_id", "title", "authors", "published", "section", "summary", "discovered_on", "arxiv_url"}
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            errors.append(f"candidate {index} must be an object")
            continue
        missing = required - set(candidate)
        if missing:
            errors.append(f"candidate {index} is missing: {', '.join(sorted(missing))}")
        identifier = candidate.get("arxiv_id")
        if identifier in candidate_ids:
            errors.append(f"candidate arXiv ID is duplicated: {identifier}")
        candidate_ids.add(identifier)

    try:
        exclusions = json.loads(EXCLUSIONS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"cannot read automation/exclusions.json: {error}")
        exclusions = []
    if not isinstance(exclusions, list) or not all(isinstance(item, str) for item in exclusions):
        errors.append("automation/exclusions.json must contain an array of arXiv ID strings")
    else:
        if len(exclusions) != len(set(exclusions)):
            errors.append("automation/exclusions.json contains duplicate IDs")
        overlap = candidate_ids.intersection(exclusions)
        if overlap:
            errors.append(f"candidate IDs are also excluded: {', '.join(sorted(overlap))}")

    if readme.count(START_MARKER) == 1 and readme.count(END_MARKER) == 1:
        actual = readme.split(START_MARKER, 1)[1].split(END_MARKER, 1)[0].strip()
        expected = render_candidates(candidates).strip()
        if actual != expected:
            errors.append("README candidate queue is stale; run: python3 scripts/update_catalog.py --render-only")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
