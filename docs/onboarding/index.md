---
owner: GOOD project coordinator
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-proposal
  - good-project-website
---

# Onboarding

GOOD develops an open platform for orbital-dynamics research by connecting the
Tudat analysis capabilities with the GOOD-WISE/Astro-WISE data and workflow
environment. The platform is intended to make analyses reproducible, reusable,
and traceable from input data and software versions to scientific results.

## First-day route

1. Ask the project coordinator for GOOD team and repository access.
2. Read the {doc}`../development-plan/index` and
   {doc}`../architecture/index`.
3. Locate your work package and its owners in the Development Plan.
4. Follow the repository-specific setup linked from
   {doc}`../repositories/index`.
5. Read {doc}`../governance/contributing` before proposing code or
   documentation changes.
6. Record missing, contradictory, or stale material as a documentation issue.

## Access checklist

- GOOD GitHub organization or repositories
- Astro-WISE GitLab repositories required for the assigned work
- Internal developer portal and deployment environment
- Approved Google Drive project-document folder
- Issue tracker and team-chat channels
- Required development and test infrastructure

Credentials must never be placed in documentation, source files, build logs, or
AI prompts. Use the approved secret-management mechanisms for each service.

## Project vocabulary

**GOOD**
: General Open Orbital Dynamics platform.

**Tudat**
: Orbital-dynamics analysis software developed and extended in WP1.

**GOOD-WISE**
: GOOD's data, provenance, and workflow capabilities built on Astro-WISE and
  developed in WP2.

**Living document**
: Documentation whose source is version controlled and rebuilt as its approved
  technical sources change.

