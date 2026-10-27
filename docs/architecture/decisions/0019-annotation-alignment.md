# ADR-0019: Annotation alignment

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-056
- **Related:** ADR-0009, ADR-0015, ADR-0018

## Context
Linguistic analyses, metrical data and cross-text alignments must attach to source text without altering it, and must stay correct when sources are updated (OQ-E06).

## Decision
- Annotations are **separate, versioned objects**. They never modify authoritative SourceSnapshot or Passage content.
- They may target **passages, exact spans, structural units, or other annotations**. Span targets use the ADR-0015 coordinate system.
- Every annotation reference is **bound to its specific SourceSnapshot and Passage**.
- Cross-text alignments (e.g. Sanskrit ↔ translation or commentary) are **explicit, typed and provenance-bearing**, never inferred from positional similarity.
- Source content changes **never silently migrate** annotations to a new snapshot.
- **LLM-generated annotations remain proposals** unless independently verified.

## Consequences
- Moving an annotation to a new snapshot is an explicit, recorded act that creates a new annotation version.
- Still open: whether human-curated annotation datasets (e.g. the Zurich Ṛgveda morphology) are evidence-eligible immediately or only after review (DR-065, OQ-E10).
