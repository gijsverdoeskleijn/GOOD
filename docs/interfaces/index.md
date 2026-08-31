---
owner: GOOD system architect
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-proposal
---

# Interfaces and configuration

This catalogue will hold versioned contracts between Tudat, GOOD-WISE,
application workflows, data services, and deployment infrastructure.

## Minimum interface description

- stable identifier, version, owner, producer, and consumers;
- transport or calling convention and authentication boundary;
- input, output, configuration, and error schemas;
- units, reference systems, temporal conventions, and uncertainty semantics;
- compatibility and deprecation rules;
- provenance fields and correlation identifiers;
- contract tests and example payloads or calls.

API specifications and configuration schemas shall be generated from, or linked
directly to, the owning repository. Narrative pages explain intent and usage;
they must not become competing copies of the contract.

