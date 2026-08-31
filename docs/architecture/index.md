---
owner: GOOD system architect
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-proposal
  - astrowise-development-manual
  - tudat-reference-paper
---

# Conceptual architecture

GOOD links acquisition data to traceable analysis and scientific applications.
Tudat provides orbital-dynamics modelling and estimation capabilities;
GOOD-WISE provides data discovery, persistence, workflow, and provenance
capabilities. Their contracts must be explicit enough to reproduce a result
from referenced data, configuration, and software revisions.

````{only} html
```{mermaid}
flowchart LR
    A[Acquisition sources] --> D[Registered data and metadata]
    D --> W[GOOD-WISE data, workflow and provenance]
    W <--> T[Tudat analysis and estimation]
    T --> R[Parameters, uncertainties and results]
    W --> R
    R --> U[Scientific applications]
    C[Versioned configuration and software] --> W
    C --> T
```
````

````{only} latex
```{admonition} Architecture flow
Acquisition sources feed registered data and metadata into GOOD-WISE. GOOD-WISE
exchanges data and provenance with Tudat analysis and estimation. Together they
produce parameters, uncertainties, and results for scientific applications.
Both components use versioned configuration and software.
```
````

## Architectural documentation rules

- Each component page names its owner, repositories, responsibilities,
  dependencies, interfaces, deployment context, and verification evidence.
- Each interface page describes both producer and consumer, versioning,
  compatibility, error behavior, and provenance fields.
- Diagrams are stored as text and reviewed with the documentation that explains
  them.
- Implementation details are generated or linked from the code repository that
  owns them.

The proposal architecture figure and its caption may be added after its access
classification and approved source location have been confirmed for this
internal portal.
