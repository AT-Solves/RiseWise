# ADR-0004: Immutable, content-addressed snapshots and passages

- **Status:** Accepted (2026-10-26) · **Refined by** ADR-0018 (2026-10-27)
- **Design reference:** source-model.md §6, §9

## Context
A reasoning result produced today must be able to identify exactly which source text it used, even after providers release updates, RiseWise corrects errors, or licences change.

## Decision
- SourceSnapshots, Passages and Annotations are **immutable**. Changes create new versions.
- Every manifest file, snapshot and passage carries a **SHA-256 content hash**.
- Reasoning cites `passageId + contentHash`, and a reasoning run records a **CorpusState** id (the immutable set of active snapshot ids).
- Corrections are new derived snapshots (`CORRECTS`), never in-place edits.
- Content purged for licence reasons is **tombstoned**: hashes and metadata are kept.

## Consequences
- Reproducibility and stale-evidence detection reduce to hash comparisons.
- Storage grows with versions; unchanged passages share hashes, which limits duplication.
- Metadata, provenance and licence changes are append-only revisions rather than overwrites.
