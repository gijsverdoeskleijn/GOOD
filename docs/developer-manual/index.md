---
owner: GOOD technical coordinator
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 60
sources:
  - good-docs
  - astrowise-development-manual
---

# Developer User Manual

This manual is the operational part of the Development Plan. It gives a GOOD
developer one route from obtaining access through making, verifying, reviewing,
and deploying a change. Repository-specific commands remain in the repositories
that own them and are linked from {doc}`../repositories/index`.

## Standard development flow

1. Select an approved issue and identify the owning work package, component,
   repositories, interfaces, and documentation pages.
2. Create a focused branch in the source repository.
3. Implement code, tests, inline API documentation, and affected portal pages
   together.
4. Record configuration, input-data, dependency, and software revisions needed
   to reproduce the result.
5. Run the repository's tests and documentation checks.
6. Open a pull request that links the issue, evidence, and affected requirements
   or decisions.
7. Obtain review from the configured code and documentation owners.
8. Merge and deploy only through the approved repository process.

## Definition of done

A change is complete when its behavior is tested; public Python and C++ APIs are
documented; interfaces and schemas remain consistent; provenance is captured;
user-facing and developer documentation is updated; and required human reviews
and deployment checks pass.

## Repository-specific setup

The source registry currently contains the documentation repository and the
preliminary project website. The GOOD-WISE/Astro-WISE repository URL, Tudat
implementation repositories, API paths, and build entry points must be supplied
by their owners before this manual can provide reproducible setup procedures.

