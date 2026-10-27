# ADR-0022: Passage granularity and cross-passage evidence spans

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-064
- **Related:** ADR-0002, ADR-0015 (DR-052), ADR-0016 (DR-053), ADR-0018 (DR-055), ADR-0019 (DR-056), ADR-0020 (DR-057)

## Context
DR-052 fixed the coordinate system for evidence spans but left open how text is divided into Passages, how evidence that crosses a Passage boundary is represented, and whether a span may end inside a grapheme cluster (OQ-E08). Scholarly and document structure is layered (e.g. sūkta ⊃ ṛc ⊃ pāda; chapter ⊃ section ⊃ paragraph), and researchers sometimes need to quote text that crosses a structural boundary. Modelling that structure, or such quotations, by nesting Passages or creating containing Passages would give the same characters more than one textual identity, and adding Passages after acquisition would change an immutable SourceSnapshot (DR-055).

## Decision

**1. Passage model.** Passages are flat, non-overlapping, immutable, text-bearing units within exactly one SourceSnapshot, created as part of that snapshot's declared segmentation. A SourceSnapshot has **one** declared Passage segmentation. Passages **must not** be nested or overlapping. No synthetic or containing Passage is created to represent larger scholarly structures or cross-passage evidence.

**2. Structure is separate from Passage identity.** Scholarly and document structure (e.g. sections, pādas, sūktas, chapters, paragraphs, pages) is represented with the existing **Locus**, **PassageLocus**, explicit locus mappings (ADR-0016), and **optional span mappings within a Passage**. A Locus is an address defined by its CitationScheme; it is not textual evidence.

**3. Evidence spans.** DR-052 is unchanged: Unicode code-point offsets, zero-based, half-open `[start,end)`, over the exact stored `original` Passage text; normalised or search text is never the coordinate system.

**4. Cross-passage evidence.** An EvidenceAnchor **may** contain multiple ordered, passage-local segments. All segments of one EvidenceAnchor **must** belong to the same SourceSnapshot, each reference its own Passage, use DR-052 span coordinates, and preserve their explicit ordering. A cross-passage EvidenceAnchor does not create a new Passage, and no EvidenceAnchor crosses a SourceSnapshot boundary.

**5. Unicode grapheme safety.** An evidence span **must not** split a Unicode extended grapheme cluster. Validation uses a pinned, explicitly recorded Unicode segmentation version so that the rule is deterministic and reproducible. This is an additional boundary constraint; the coordinate system remains Unicode code-point offsets (DR-052).

## Consequences
- Every character of a SourceSnapshot belongs to exactly one Passage, so each quotation has one textual identity and snapshot hashing stays unambiguous.
- Larger or finer structures (e.g. a pāda within a ṛc, a sūkta across several ṛcs, a section across paragraphs) are expressed as Loci mapped to whole Passages or to spans within Passages, never as Passages.
- PassageLocus gains an optional span in DR-052 coordinates.
- ADR-0019's existing annotation-target terminology is not otherwise changed by this ADR. Any further definition of "structural unit" remains outside DR-064 and must be resolved separately if required.
- The current single-passage EvidenceAnchor shape `{passageId, contentHash, span, quotedTextHash}` becomes one **segment**; an anchor is an ordered list of such segments within one snapshot.
- ADR-0015's open pointer on grapheme-cluster boundaries is resolved by decision 5.
- Because segmentation is fixed when the snapshot is created, a different segmentation of the same content requires a new SourceSnapshot (consistent with DR-055).
- ROOT_TEXT designations (DR-057) and annotation binding (DR-056) are unaffected: both remain bound to specific snapshots and passages.

## Explicit non-decisions / follow-up questions
Not decided by this ADR (tracked in OPEN_QUESTIONS.md OQ-E11 … OQ-E14 where a question is needed):
- Exact schema representation of a multi-segment EvidenceAnchor (OQ-E11).
- Composite hash and join encoding for multi-segment evidence (OQ-E11).
- Whether multi-segment evidence permits omitted text, gaps or ellipsis (OQ-E12).
- Exact Unicode segmentation library and version (OQ-E13).
- Domain-specific Passage segmentation rules, i.e. which granularity each extension or source uses (OQ-E14).
- UI rendering of multi-segment evidence; database and index implementation; API representation (implementation design, no decision entry).
