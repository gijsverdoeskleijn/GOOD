---
owner: GOOD documentation owner
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-docs
---

# Contributing documentation

## Change process

1. Create or select an issue describing the documentation need and evidence.
2. Confirm the page owner and access classification before copying source
   material.
3. Make the smallest coherent change and update page metadata and source
   baselines where appropriate.
4. Run `make docs-check` and inspect the generated portal.
5. Open a pull request using the repository template and request the named
   content owner plus any affected code or security owners.
6. Resolve review comments and let an authorized human merge the change.

## Writing and linking

- Prefer plain Markdown and short, descriptive headings.
- Explain tasks in the Developer User Manual, concepts in Architecture, and
  exact generated details in Reference.
- Link to authoritative code, schema, API, decision, or PDF sources instead of
  creating copies that will drift.
- State units, coordinate systems, time standards, versions, and uncertainty
  conventions wherever ambiguity would affect scientific results.
- Use text-based diagrams where practical and provide meaningful labels.

## Adding a source

Update the appropriate file under `docs/_data/`, obtain the source owner's and
access owner's approval, then run `make registry`. A repository must include a
stable URL, ref and baseline revision before monitoring is enabled. A PDF must
include a stable Drive identifier or controlled-record identifier and revision
before ingestion.

