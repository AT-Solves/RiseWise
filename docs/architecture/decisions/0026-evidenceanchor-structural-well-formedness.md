# ADR-0026: EvidenceAnchor structural well-formedness

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-070
- **Resolves:** OQ-E20
- **Related:** ADR-0015 (DR-052), ADR-0022 (DR-064), ADR-0023 (DR-067), ADR-0024 (DR-068), ADR-0025 (DR-069)

## Context
DR-067 defines an EvidenceAnchor as one cited textual selection of one or more ordered, passage-local segments within one SourceSnapshot. DR-068 gives each SourceSnapshot a declared logical reading order over its Passages. DR-069 defines the join relations `CONTINUOUS` and `DISCONTINUOUS` between consecutive segments, declared and mechanically verified, and defines no relation for configurations in which neither holds. What remained open (OQ-E20) was which segment configurations form a structurally well-formed EvidenceAnchor: reverse order, overlap, repeated Passages, repeated spans, and adjacent segments within one Passage.

## Decision
1. **One or more segments.** That an EvidenceAnchor contains one or more segments is a restatement of DR-067, not a new rule.
2. **Non-empty segments.** Every segment has a non-empty span (`start < end`). This restricts EvidenceAnchor well-formedness only; it does not alter DR-052's general half-open span model.
3. **Forward progression.** For every pair of consecutive segments, the relation mechanically derived under DR-069 must be `CONTINUOUS` or `DISCONTINUOUS`. Therefore reverse ordering, overlapping segments, and identical/repeated spans are not well-formed. No new ordering formula and no new join relation is introduced.
4. **Repeated Passages.** A Passage identity may repeat only in consecutive segments. A repeated Passage with separated spans is well-formed and is joined by `DISCONTINUOUS`. Example: `A[0,10) → A[20,30)` is well-formed; `A[0,10) → B[0,10) → A[20,30)` is not, because returning to A after B violates rule 3.
5. **One structural representation for same-Passage continuity.** A well-formed EvidenceAnchor contains no pair of consecutive segments within the same Passage joined `CONTINUOUS`; such a selection must be expressed as a single segment. Example: `A[0,10) → A[10,20)` is not well-formed; `A[0,20)` is the well-formed representation.
6. **`DISCONTINUOUS` segments are never merged.**
7. **Structural only.** These rules define structural well-formedness only. They do not determine whether an EvidenceAnchor provides sufficient evidence for a claim.
8. **Presupposed rules.** E20 presupposes, and does not restate or redefine, the requirements of DR-064 and DR-067: every segment resolves to a Passage in the anchor's single SourceSnapshot; spans are valid; spans are grapheme-safe; the EvidenceAnchor remains within one SourceSnapshot.
9. **Boundaries.** A well-formed EvidenceAnchor is structurally valid only if every consecutive boundary has exactly one mechanically valid DR-069 relation.

## Rationale
- **Reverse order** has no DR-069 relation: the next segment would begin before the previous one ends in the SourceSnapshot's citable textual content. Allowing it would require a new join relation, and a rearranged selection can change a source's meaning. A researcher who needs to cite later text first can use separate EvidenceAnchors at the Tarka layer (DR-067).
- **Overlap** has no DR-069 relation and would cite the same characters twice within one selection, inflating the evidence.
- **Identical repeated spans** are the limiting case of overlap and fail rule 3 for the same reason.
- **Repeated Passages with separated spans** are a legitimate elided quotation within one Passage; DR-069 already gives them the relation `DISCONTINUOUS`. Forbidding repeated Passage identity as such would wrongly exclude them.
- **One structural representation for same-Passage continuity:** without rule 5, the same selection could be written with any number of arbitrary split points, so structurally identical selections would have different representations.
- **No loss of source information:** the single segment covers exactly the same characters, and its quoted text verifies the same text. Only the creator's split point disappears.
- **The creator's split point is not part of EvidenceAnchor semantics:** a `CONTINUOUS` boundary inside one Passage carries no meaning under DR-067 or DR-069; segments are passage-local units of a selection, not a record of how the selection was made.
- **Determinism:** one structural representation per selection makes value-object equality, deduplication and any future deterministic composite hash (OQ-E18) straightforward, without a separate normalisation step.
- **Normalisation behaviour is left open:** this ADR states what a well-formed anchor is, not how tools reach it. Whether tools normalise at creation time, and how violations are reported, are implementation and presentation questions; deciding them here would also risk silently rewriting existing anchors.
- **Structural, not evidential:** well-formedness says only that a selection is coherently represented. Whether it supports a claim is decided by Tarka's evidence and status rules.

## Consequences
- Every well-formed multi-segment EvidenceAnchor reads forward through the SourceSnapshot's citable textual content, and each of its boundaries carries exactly one verifiable DR-069 relation.
- A Passage can appear in more than one segment only consecutively, and then only across `DISCONTINUOUS` joins.
- ADR-0025's non-decision listing "repeated Passages" among configurations in which neither relation holds is read with this ADR: a repeated Passage with separated spans is joined by `DISCONTINUOUS`; only backward, overlapping or identical repeats have no relation.

## Explicit non-decisions
Not decided by this ADR:
- Hashing and canonical serialisation (OQ-E16, OQ-E17, OQ-E18).
- Unicode segmentation version policy (OQ-E13).
- Complex material and segmentation rules (OQ-E14).
- Carrying anchors across snapshots (OQ-E19).
- Normalisation implementation and violation reporting.
- Tarka/UI representation (OQ-E21).
- Evidential sufficiency.
