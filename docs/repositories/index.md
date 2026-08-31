---
owner: GOOD technical coordinator
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 60
sources:
  - good-docs
  - good-project-website
  - astrowise-good
---

# Repository catalogue

The machine-readable {doc}`../reference/source-registry` is the inventory for
documentation inputs. A repository becomes an active source only after its
owner, access class, default ref, relevant paths, and baseline revision are
recorded.

## Required repository record

Each contributing repository must state:

- purpose, work package, component, and responsible owner;
- clone and access instructions that do not expose credentials;
- supported development and deployment environments;
- build, test, lint, API-documentation, and release commands;
- relevant Python, C++, schema, and API-specification paths;
- branching, review, versioning, release, and deprecation policy;
- dependencies on other GOOD repositories and external services.

## Current registration status

- **GOOD documentation:** registered; documentation checks are implemented here.
- **Preliminary GOOD project website:** registered and monitored as a public
  source of project terminology.
- **GOOD-WISE/Astro-WISE:** awaiting the approved GitLab repository URL and
  baseline revision.
- **Tudat implementation repositories:** awaiting selection of the specific
  repositories and documentation paths used by GOOD.

