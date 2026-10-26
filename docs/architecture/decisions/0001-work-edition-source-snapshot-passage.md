# ADR-0001: Separate Work, Edition, Source, SourceSnapshot and Passage

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §3, §4

## Context
RiseWise must answer "where did this come from?" down to an exact passage, across texts that exist as abstract works, multiple printed editions, multiple digital representations of each edition, and multiple versions of each representation. Collapsing any two of these levels makes provenance ambiguous (e.g. citing "the Ṛgveda" when the wording came from one digital file of one edition).

## Decision
The core model has five distinct levels:

1. **Work** — the abstract intellectual creation.
2. **Edition** — a specific published/scholarly realisation of a Work. Revised editions are separate Editions linked by `REVISION_OF`.
3. **Source** — a concrete representation of an Edition that RiseWise holds or references (digital text, scan, or print reference). Born-digital works may have a Source without a print Edition.
4. **SourceSnapshot** — one immutable version of a Source's content.
5. **Passage** — the concrete text unit inside one SourceSnapshot.

An **Acquisition** (with its **Manifest**) records how a snapshot was obtained; it is not a sixth content level.

## Consequences
- Every citation and evidence anchor resolves to a Passage in a specific Snapshot of a specific Source of a specific Edition of a Work.
- Edition-level rights and digital-representation rights can differ and are recorded separately (see ADR-0006).
- "We know this work but hold no edition/representation" is representable (0..* cardinalities).
- More entities than a flat "document" model; accepted as the minimum needed for honest provenance.
