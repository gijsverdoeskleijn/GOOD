---
owner: GOOD operations owner
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 60
sources:
  - good-docs
---

# Build, deployment, and operations

## Documentation build

Install `docs/requirements.txt` in an isolated Python environment and run
`make docs-check`. The command regenerates the source inventory, validates page
metadata and citations, builds the HTML portal with warnings treated as errors,
and writes a reproducibility manifest under `build/`.

`make docs-pdf` creates the controlled PDF snapshot when a compatible LaTeX
toolchain is available. PDF output is a versioned snapshot; the authenticated
HTML portal remains authoritative.

## Publication

Pull requests build an HTML artifact for reviewer inspection. Publishing to an
internal deployment environment must require approval and an authenticated
target. GitHub Pages is not enabled because the portal is internal at launch.

## Incidents and support

Report build failures, broken integrations, access problems, stale content, and
suspected disclosure through the issue tracker. Do not include credentials,
restricted source text, personal data, or sensitive logs in issues.

