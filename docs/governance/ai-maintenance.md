---
owner: GOOD documentation owner
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 60
sources:
  - good-docs
---

# AI documentation maintenance

The AI documentation agent is the primary maintainer. Human domain owners remain
accountable for technical correctness and publication decisions.

## Maintenance cycle

1. Read the source registries and the previous build manifest.
2. Detect changed refs, releases, schemas, API surfaces, PDF revisions, and
   deployment behavior.
3. Map each change to pages citing the affected source identifier.
4. Classify the effect as no documentation impact, clear update, or uncertain/
   conflicting evidence.
5. For a clear update, run validation and prepare a draft pull request. For an
   uncertainty or conflict, create a documentation issue.
6. Report sources, old and new revisions, affected pages, reasoning, confidence,
   validation results, and requested reviewers.

## Agent decision record

Each issue or draft pull request should contain:

- **Evidence:** stable source links, revisions, and relevant locations;
- **Impact:** affected components, interfaces, requirements, and pages;
- **Action:** changes made or questions requiring a human decision;
- **Confidence:** high, medium, or low, with a reason;
- **Validation:** commands and results;
- **Reviewers:** content, code, security, or access owners as applicable.

The scheduled freshness workflow is deterministic monitoring, not itself an AI
review. Its report is the input from which the agent investigates and proposes
an appropriate response.

