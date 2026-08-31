---
owner: GOOD WP4 owner
status: draft
access: public
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-docs
---

# GOOD Documentation System — Draft Requirements and Implementation

## 1. Draft requirements

1. **Purpose and audience**

   - The main purpose is a living Development Plan and Developer User Manual for GOOD research software engineering developers.
   - It shall support onboarding, development, integration, testing, release, operation, reuse, and reproducibility of the GOOD platform.
   - It shall be an internal, navigable documentation website. Versioned PDF exports shall support milestones, grant reporting, preservation, and offline use, but are snapshots rather than the current source of truth.

2. **Off-loading developers: AI documentation assistant**

   - An AI documentation agent shall be the primary operational agent responsible for keeping documentation current.
   - It may monitor approved sources, identify stale or conflicting content, update documentation, create GitHub issues, and draft pull requests.
   - If needed it can make requests for merge/pull.
   - It cannot, alter access controls, expose restricted information, or make unreviewed scientific, architectural, security, or governance decisions.

3. **Content and structure**

   - The site shall cover onboarding; architecture; repositories and components; APIs; configurations; data models; provenance; build, test, deployment and release procedures; runbooks; troubleshooting; Architectural Decision Records; contribution guidance; and governance.
   - It shall include diagrams of system boundaries, component and repository dependencies, data/configuration/software-version/result flows, and the relationships between Tudat, GOOD-WISE/Astro-WISE, external data sources, and workflows.
   - The core Development Plan and Developer User Manual shall be organised as task- and component-oriented pages, rather than as one static linear document.

4. **Sources of truth and provenance**

   - Code repositories shall be the primary technical source of truth; GitHub is primary and GitLab Astro-WISE is secondary.
   - The system shall use suitable inline Python and C++ documentation, API specifications, configuration schemas, repository metadata, releases, and selected approved PDF references.
   - It shall be able to take as input half a dozen external PDFs.
   - The system shall distinguish generated reference material from human-authored explanation and shall not overwrite maintained editorial content without review.

5. **Authoring, review, and maintenance**

   - Each substantial documentation area shall have named GOOD team owners.

6. **Discovery, access, and Open Science**

   - The site shall provide navigation, full-text search, stable URLs, deep links, cross-links to code/issues/releases/decisions, and versions corresponding to active development and released software.
   - Credentials, private keys, tokens, and secrets shall never appear in documentation source, generated output, issues, or logs.
   - The system shall support FAIR and Open Science practice through clear licensing and attribution, portable/interoperable formats, provenance, persistent identifiers where appropriate, and preservation of released documentation with its source inputs.

## 2. Draft implementation

The draft implementation as a prototype is this **Sphinx documentation-as-code portal** with MyST Markdown that you are now viewing. It has a searchable catalogue structure of the Development Plan and Developer user manual from a version-controlled source. It is navigable as HTML and can generate PDF snapshots. When a real need arises, the design allows to later add functionality to aggregate views which are generated from selected contents. It remains possible for non-code savvy persons to provide feedback on the documentation through PDF comments and the like.

## 3. Implementation qualification criteria

1. A single internal entry point provides onboarding, the Development Plan and Developer User Manual, architecture, repository/component overviews, interfaces/configuration, data/provenance, contribution guidance, and operations material.
2. The portal builds reproducibly from version-controlled sources and produces a machine-readable build manifest with build time and all source commits, tags, and PDF versions.
3. At least two GitHub repositories and one GitLab Astro-WISE repository are registered and contribute version-traceable content.
4. The generated developer reference includes at least one Python and one C++ inline-documentation source, each linked to its repository location and source revision.
5. At least one approved PDF reference is indexed or searchable, cited, access-classified, and linked to source/version metadata.
6. The Development Plan and Developer User Manual is maintained as navigable portal content and exports to a dated, versioned PDF snapshot.
7. Navigation, full-text search, stable URLs, deep links, and cross-links to relevant repositories, issues, releases, and decisions work in the internal site.
8. Pull requests require named documentation-owner approval; protected areas automatically request appropriate technical reviewers; unapproved changes cannot reach the internal published site.
9. The documentation issue workflow supports ownership, source/domain labels, freshness tracking, and links from documentation issues to relevant implementation work.
10. Access is restricted to authenticated GOOD team members, and automated checks confirm that the published build contains no credentials, tokens, private keys, or restricted documents.
11. A deliberate mismatch between source material and documentation is detected by the AI agent, producing a source-linked report and either a GitHub issue or draft pull request.
12. An AI-authored pull request records assessed sources, proposed changes, confidence, and required reviewers, and remains unmerged until a designated GOOD owner approves it.
