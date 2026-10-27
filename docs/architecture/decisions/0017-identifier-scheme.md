# ADR-0017: Identifier scheme

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-054

## Context
Identifiers are referenced everywhere and are expensive to change (OQ-E01). Earlier examples used readable keys such as `work:rv` and passage keys that embed citation loci.

## Decision
- Every persisted entity has an **immutable, opaque primary identifier**. MVP format: **ULID**.
- **Human-readable keys** may exist as separate, scoped **aliases**. They are never entity identity.
- **Content hashes** identify immutable content and are distinct from entity IDs.
- Citation/locus identifiers are governed by their CitationScheme and are **never embedded in primary entity IDs**.
- IDs are **never reused**.

## Consequences
- In documentation examples, readable keys are labelled as aliases; passages show an opaque ID placeholder separately from any alias.
- An alias may contain readable text (including a citation), because it is not identity; changing an alias never changes the entity.
- Alias scoping and uniqueness rules are a schema-design detail.
