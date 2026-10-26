# ADR-0006: Evidence-backed licences, most-restrictive rights, unknown = pending, rights per context

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §7

## Context
Freely accessible material is not necessarily openly licensed. Rights can attach at different levels (underlying work, edition apparatus, digital representation, annotation layer) and upstream terms can carry through derivations. RiseWise intends to support free and potentially paid tiers, so the same material may be usable in one context and not another.

## Decision
- **LicenceRecords** are append-only, attach at Work / Edition / Source / annotation-dataset level, and every term is backed by **evidence** (where it was stated, captured with a hash and date) and a **verification status**.
- **Effective rights** are computed by combining all applicable records and upstream constraints, taking the **most restrictive** value per term.
- **Any `UNKNOWN` term ⇒ `LICENCE_PENDING`** ⇒ content cannot be used as evidence.
- Rights are evaluated per **use context** (e.g. local personal, hosted free, hosted paid, enterprise, external processor) by a configurable policy producing a **RightsDecision**. Rights are never stored as a single flag.
- Conservative default until legal review: NC and scholarly-only material is `USER_IMPORT_ONLY` in every hosted or paid context.

## Consequences
- Licence status is auditable and reversible without losing history.
- The rights policy mapping is configuration, not architecture, and requires legal review (OQ-L01).
- Every exit point (API, export, display, search, embeddings, caches, external LLM calls) must consult the RightsDecision.
