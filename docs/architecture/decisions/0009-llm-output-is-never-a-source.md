# ADR-0009: LLM output is never a source

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §2 (P7), §3, §19

## Context
RiseWise's core principle is that an LLM-generated statement is never automatically a fact. The source layer is where facts are anchored; if LLM output could enter it, the principle would be bypassed.

## Decision
- LLM output can **never** become source content (Passage, Text, Snapshot) or licence/provenance truth.
- LLM-produced annotations or interpretations may be stored only with `origin: LLM` (and model/prompt version in provenance) and are **excluded as evidence**.
- Tool output (e.g. a morphological analyser) is stored with `origin: TOOL` and is not evidence-eligible until verified.
- All source text shown to an LLM is treated as untrusted data; LLM output cannot change source records.

## Consequences
- Evidence anchors always resolve to text that came from an identified source, never from a model.
- When a source is unavailable, LLM recollection is not an acceptable substitute (ADR-0010).
