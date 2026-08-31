---
owner: GOOD documentation owner
status: in-review
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-docs
  - good-proposal
---

# Documentation-system requirements

## Requirements

1. **Purpose, audience, and authority**

   - The system shall support GOOD research-software developers, especially
     onboarding and day-to-day platform development.
   - The authoritative output shall be an authenticated, navigable online
     portal. Generated PDF files are identifiable, versioned snapshots.
   - Code repositories are the primary source of truth for technical behavior;
     approved PDFs provide project and contextual sources.

2. **Content and generation**

   - The portal shall contain a living Development Plan and Developer User
     Manual, including project requirements, architecture, work packages,
     schedule, interfaces, data/provenance, operations, and contributor guidance.
   - It shall generate or link Python and C++ API reference from approved inline
     documentation and support text-based, version-controlled diagrams.
   - Reusable content units may support purpose-specific views without creating
     competing authoritative copies.

3. **Traceability, FAIR, and Open Science**

   - Every page shall identify its owner, status, access class, review date, and
     registered sources.
   - Builds shall record the documentation revision and the revisions or stable
     identifiers of inputs used.
   - Published material shall provide appropriate identifiers, metadata,
     licensing, attribution, provenance, and accessible formats.

4. **Review, discovery, and lifecycle**

   - Changes shall use pull requests, assigned owners, review rules, and an
     auditable history. Issues shall track gaps, drift, and maintenance work.
   - The portal shall provide structured navigation, full-text search, stable
     links, and access to appropriate versioned or released snapshots.

5. **Access and integrations**

   - At launch, content shall be limited to authorized GOOD team members, with
     public, internal, and restricted classifications supported.
   - GitHub, Astro-WISE GitLab, Google Drive, API specifications, deployment,
     issue tracking, and team-chat integrations shall use minimum privileges and
     approved secret storage. Credentials shall never enter documentation.

6. **AI-assisted maintenance**

   - The AI agent shall be the primary documentation maintainer and monitor
     approved code and PDF sources for changes, contradictions, and stale pages.
   - It may report, edit documentation, create issues, and draft pull requests,
     always stating evidence, confidence, and required reviewers.
   - It shall not merge, approve, publish externally, change access controls, or
     disclose restricted material without explicit human authorization.

## Proposed implementation

Use Sphinx with MyST Markdown to build a DPDD-style, searchable internal portal.
The canonical developer view is assembled from contributor-owned pages under
version control and exported to HTML plus a versioned PDF snapshot. Each page
has validated metadata, while registries describe GitHub, GitLab, and controlled
PDF sources. CI validates metadata, links, diagrams, and generated Python/C++
reference and records a reproducibility manifest.

The content model incorporates the useful CalTQ idea of reusable documentation
units. The developer portal is the only output at launch; `release` or `public`
profiles may be added later with explicit ownership, inclusion rules, access
controls, and tests. The legacy CalTQ generator is not reused.

GitHub Issues and pull requests provide maintenance and change control. The
portal is distributed initially as an authenticated build artifact until an
approved internal hosting target is selected. Google Drive and private GitLab
connections remain read-only. Scheduled freshness checks compare registered
repository refs with the revisions cited by the documentation and provide a
structured input for the AI maintenance process.

## Initial acceptance criteria

1. One authenticated entry point contains onboarding, Development Plan,
   Developer User Manual, architecture, repository/component/interface,
   provenance, operations, reference, and governance material.
2. A clean checkout can reproduce HTML and PDF outputs using documented
   commands, with warnings and validation failures blocking acceptance.
3. At least two GitHub and one Astro-WISE GitLab repository contribute
   revision-traceable content.
4. At least one Python and one C++ API source is generated from inline
   documentation and linked to its source revision.
5. At least three approved PDF documents are registered with stable identifiers,
   revisions, owners, access classes, and citations.
6. Search, navigation, stable links, page ownership, review status, access class,
   and last-reviewed information are available.
7. Each build produces a manifest identifying its portal revision, profile,
   source baselines, timestamp, and content digests.
8. Pull-request review and owner approval are enforced for protected content.
9. The deployed portal requires GOOD team authentication and does not expose
   credentials or restricted material in builds or logs.
10. A scheduled source check produces a reviewable drift report.
11. A deliberate source/documentation mismatch produces a source-linked issue
    or draft pull request for human review.
12. A documented recovery exercise shows that a released portal snapshot can be
    rebuilt from its recorded source and build information.

