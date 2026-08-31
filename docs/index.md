---
owner: GOOD documentation owner
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-docs
  - good-proposal
---

# GOOD Developer Portal

```{admonition} Internal GOOD team documentation
:class: internal
This portal is intended only for authorized GOOD team members at launch. Do not
redistribute restricted source material or generated snapshots.
```

The GOOD Developer Portal is the authoritative, living Development Plan and
Developer User Manual for the General Open Orbital Dynamics platform. It links
technical statements to versioned code repositories and approved project
documents so that contributors can discover both the current guidance and its
evidence.

Use **Onboarding** when joining the project, **Development Plan** when planning
or reviewing work, and **Developer User Manual** when developing or operating
the platform. The remaining sections provide the underlying architecture,
interfaces, provenance, reference, and governance material.

```{toctree}
:maxdepth: 2
:caption: Start here

onboarding/index
development-plan/index
developer-manual/index
```

```{toctree}
:maxdepth: 2
:caption: System documentation

architecture/index
repositories/index
components/index
interfaces/index
data-and-provenance/index
operations/index
decisions/index
reference/index
```

```{toctree}
:maxdepth: 2
:caption: Documentation governance

governance/index
profiles/index
```

## Document status

Pages marked **draft** are useful working material but require their named
owner's review. Every page records its owner, access class, review date, and
registered sources in machine-readable metadata. Every build records the
portal revision and source baselines in a manifest.

