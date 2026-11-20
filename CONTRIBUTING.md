# Contributing

## Scope and sources

Include agents for image restoration, enhancement, or super-resolution that use planning, tool calls, or feedback. Standalone restoration models belong under supporting tools. General visual tool use and creative editing are outside the active catalog.

1. Search the catalog by title, arXiv ID, and DOI before adding a paper. Update existing entries when a final version appears.
2. Verify the title, authors, version, and venue against a publisher, proceedings, arXiv, or a confirmed OpenReview decision.
3. Label unconfirmed manuscripts as preprints or submissions. An OpenReview submission or a code repository alone does not establish acceptance.
4. Use public primary sources only. Explain why a paper fits the catalog; do not share private submissions or reviews.
5. Use the four-column format: **Paper | Venue | Link | Code**. List the lead author, keep paper and project links separate from code, and use a dash if no code link is available. Put optional summaries and figure links in the companion notes.

## Before opening a pull request

- Branch from the latest `main` without disturbing uncommitted work. Keep changes focused.
- Check table columns, duplicate identifiers, section anchors, and relative paths. Preview rendering and open all new or changed external links. Record access errors as unverified.
- Verify figure paths and versions. External images and other resources retain their original terms.
- If reporting energy, record hardware, time steps, and how energy was measured or estimated. Do not rank results from incompatible protocols.
- Include sources, verification date, rationale, checks actually run, and any open issues. Do not report CI as passed if it did not run.

This is a manual catalog. The owner reviews each pull request; adding papers, enabling automation, and publishing changes are separate decisions.
