# Contributing

Thanks for helping maintain Awesome Agentic Computer Vision.

## Add a curated paper

1. Add the paper to the most relevant table in `README.md`.
2. Prefer official arXiv, project, conference, and code links.
3. Keep the existing table format and use the official paper title.
4. Run `python3 scripts/validate_catalog.py` before opening a pull request.

## Automated discovery queue

Every Monday, the `Weekly paper discovery` workflow searches arXiv using the queries in `automation/searches.json`. New, non-duplicate results are added to `automation/candidates.json`, rendered into the README review queue, and proposed in a pull request.

The queue is intentionally review-first. To accept a paper:

1. Verify that it is genuinely agentic computer vision work.
2. Move it into the correct curated table in `README.md` and add authoritative links.
3. Remove its object from `automation/candidates.json`.
4. Run `python3 scripts/update_catalog.py --render-only`.
5. Run `python3 scripts/validate_catalog.py`.

To reject a paper, remove it from `automation/candidates.json`, add its bare arXiv ID (for example, `2608.01234`) to `automation/exclusions.json`, and render the README again. The exclusion prevents the same paper from being rediscovered.

## Run discovery manually

Use the `Weekly paper discovery` workflow's **Run workflow** button on GitHub. For local testing without network access, pass an Atom fixture with `python3 scripts/update_catalog.py --feed-file path/to/feed.xml`.
