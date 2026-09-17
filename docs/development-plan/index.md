---
owner: GOOD project lead
status: draft
access: internal
last_reviewed: '2026-08-31'
review_interval_days: 90
sources:
  - good-proposal
---

# Development Plan

The Development Plan is the core GOOD project document. It connects goals,
requirements, architecture, work packages, deliverables, schedule, risks, and
developer guidance. Detailed technical instructions live in the linked portal
sections so they can evolve with the code without duplicating content here.

## Project goals

- Provide a general, open platform to support orbital-dynamics sicentific research (e.g. cometary dynamics) and to support socio-economic use cases (e.g., light pollution by satellites which is detrimental to optical astronomy).
- Which scientific research to support is specified in the GOOD use cases (see below).
- Link data acquisition, traceable analysis, and scientific applications.
- Advance and integrate Tudat and GOOD-WISE/Astro-WISE capabilities.
- Make software, data use, configuration, provenance, and results reproducible
  in accordance with Open Science and FAIR principles.


## Development approach

The proposed development approach is to first build a prototype of the GOOD platform. And secondly the final GOOD platform. Two options are considered as architecture of the prototype GOOD platform. 
1. taking the FOTOS OPS API and adapt it so that it interfaces between Tudat orbit pipelines and the AstroWISE database.
2. taking the FOTOS API and FOTOS OPS database and adapt the FOTOS OPS database to support also the AstroWISE image processing pipelines.

One of the two architectures is selected as the architecture of the prototype platform. This is then implemented and qualified.

After building the prototype GOOD platform the architectural design of the GOOD platform is made. It takes in the lessons learned from the GOOD prototype platform. Then implemented then qualified.

There will be a working platform at all times. The prototype platform is operational until the final platform is operational. 

### Support from AI

GOOD team will develop a method to let AI be the main custodian of documentation. Keeping it up to date as decision are made. 

GOOD team will develop guidelines how AI can assist in  design, implementation, qualification (software testing, system testing), operations, helpdesk.

## GOOD use cases

The proposed GOOD science cases that drive the prototype GOOD platform are: 

- [Redo extraction of precision astrometry from comets by Margherita inside GOOD (prototype)](https://docs.google.com/spreadsheets/d/1TkMxX6Q1LeDtnWEv6geDCf8t2iW9ECfo8B1xF8voY4o/edit?gid=1049909592#gid=1049909592)
- [Redo Comet dynamical orbit modelling of Margherita inside GOOD prototype](https://docs.google.com/spreadsheets/d/1TkMxX6Q1LeDtnWEv6geDCf8t2iW9ECfo8B1xF8voY4o/edit?gid=1049909592#gid=1049909592)
- [Apophis orbital modelling benchmark using existing astrometry](https://docs.google.com/spreadsheets/d/1TkMxX6Q1LeDtnWEv6geDCf8t2iW9ECfo8B1xF8voY4o/edit?gid=1049909592#gid=1049909592)
- usecase adding a new catalog dataset to be handled by the GOOD platform
- usecase geocentric satellite

## Work packages

| Work package | Scope | Documentation owner |
|---|---|---|
| WP1 | Tudat core development | WP1 owner |
| WP2 | GOOD-WISE core development | WP2 owner |
| WP3-1 | Near-Earth space situational awareness | WP3-1 owner |
| WP3-2 | Solar System dynamics | WP3-2 owner |
| WP3-3 | Spacecraft radio tracking | WP3-3 owner |
| WP4 | Dissemination, outreach, and project management | WP4 owner |

Named owners, contributors, effort, milestones, and dependencies must be
verified against the approved work-package plan before this page is promoted
from draft.

## Mapping tasks to persons

## Mapping persons to tasks

## Schedule: mapping tasks onto time

## Planning views

- {doc}`../architecture/index` defines boundaries and technical dependencies.
- {doc}`../components/index` records component responsibilities and owners.
- {doc}`../interfaces/index` records cross-component contracts.
- {doc}`../operations/index` covers integration, deployment, and support.
- {doc}`../decisions/index` records consequential technical decisions.
- {doc}`../governance/system-requirements` defines requirements and acceptance
  criteria for this documentation system.

## Schedule and status

The approved proposal describes a 36-month project starting in Q2 2026, with a
beta platform expected after approximately two years and the complete platform
after approximately three years. Replace this summary with the approved,
milestone-level schedule when its controlled source and owner are registered.

```{warning}
Dates on this draft page are orientation only. The approved project schedule
remains controlling until a versioned schedule source is registered here.
```

