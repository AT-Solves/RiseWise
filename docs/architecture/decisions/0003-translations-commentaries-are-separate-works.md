# ADR-0003: Translations and commentaries are separate Works; commentary ≠ interpretation

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §3, §4, §11

## Context
A translation is not the original text, and a commentary is not the text it comments on. A commentary (a text) is also different from an interpretation (an attributed reading extracted from some text). If these share a representation, the system can cite a translation as the original or present a commentator's view as what the root text says.

## Decision
- A translation is a **Work** with `workKind: TRANSLATION`, linked `TRANSLATION_OF` its target Work.
- A commentary is a **Work** with `workKind: COMMENTARY`, linked `COMMENTARY_ON` its target; a sub-commentary is `COMMENTARY_ON` another commentary.
- Each has its own Editions, Sources, Snapshots, Passages and loci; passages align to the target's loci via mappings.
- An **Interpretation** is a separate concept: an attributed reading of a locus, anchored to the passage where its author states it, with an origin (`SOURCE_EXTRACTED`, `HUMAN_CURATED`, `LLM_PROPOSED`).

## Consequences
- The model has no way to label a translation or commentary passage as the original text.
- Domain rules (e.g. VR-101, VR-102) can be enforced structurally.
- Interpretation entity is designed now but deferred to the Tarka phase (source-model.md §21).
