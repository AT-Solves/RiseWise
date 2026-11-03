# ADR-0025: Join relations between EvidenceAnchor segments

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-069
- **Resolves:** OQ-E12
- **Related:** ADR-0015 (DR-052), ADR-0022 (DR-064), ADR-0023 (DR-067), ADR-0024 (DR-068)

## Context
DR-067 made an EvidenceAnchor one cited textual selection of ordered, passage-local segments within one SourceSnapshot, and required its representation to stay extensible for join/omission semantics. DR-068 gave every SourceSnapshot a declared logical reading order over its Passages, so the SourceSnapshot's citable textual content is an ordered sequence in which every character belongs to exactly one Passage. It is therefore now mechanically decidable whether one segment begins exactly where the previous one ends. What remained open (OQ-E12) was whether a selection may exclude intervening text, how that is expressed, how it is verified, and what it does — and does not — mean.

## Decision

**1. Join relations.** Consecutive segments of one EvidenceAnchor are joined by a declared relation:
- **`CONTINUOUS`** — the next segment begins exactly where the previous segment ends in the SourceSnapshot's citable textual content, in DR-068 order.
- **`DISCONTINUOUS`** — citable source text exists between the two segments, in DR-068 order, and is not part of the anchor.

**2. Declared and mechanically verified.** The relation is declared in the anchor and verified against the relationship mechanically derived from the segments' coordinates and the SourceSnapshot's DR-068 Passage order. A declared relation that does not match the mechanically derived relationship fails verification.

**3. Structural fact only.** A join relation is a structural fact about the cited selection. It does not state or imply why intervening text is excluded, and does not state or imply any intent of an author, editor or citer. Any such interpretation requires a separate, evidenced claim.

**4. Presentation ellipsis is not source text.** An ellipsis is the presentation of `DISCONTINUOUS` and is never stored as source text or as quoted text. Ellipsis characters, lacuna marks or similar marks that are part of the source text remain source text and may be quoted like any other source text.

**5. Absent material creates no gap.** Material that is not part of the SourceSnapshot's citable textual content — because it is missing, damaged, or excluded by ingestion/segmentation rules — lies outside the sequence over which join relations are derived and does not by itself make a selection `DISCONTINUOUS`. Such absence is recorded through availability/coverage and segmentation rules, not through join relations.

**6. Quoted text.** Each segment's quoted text and `quotedTextHash` remain exact and are unaffected by join relations. No representation may present text joined by `DISCONTINUOUS` as continuous source text.

## Consequences
- An elided quotation can be one EvidenceAnchor; independent pieces of evidence remain separate anchors (DR-067).
- The excluded text of a `DISCONTINUOUS` join is always recoverable from the SourceSnapshot by coordinates, so it can be inspected (e.g. by "Challenge this conclusion").
- Tarka may state the structural fact that a selection excludes intervening text; it may not attribute the exclusion to anyone without a separate, evidenced claim.
- A tampered join declaration is detected by the mechanical check in decision 2.

## Explicit non-decisions / follow-up questions
Not decided by this ADR:
- Configurations in which neither relation holds — reverse order, repeated Passages, overlapping segments — and whether adjacent segments within one Passage must be merged: their validity and any representation remain **OQ-E20**. This ADR defines no relation for them.
- Composite hash construction and canonical serialisation (OQ-E18, OQ-E16, OQ-E17).
- Placement of complex material such as footnotes, marginalia and tables, and therefore what is citable content (OQ-E14).
- How Tarka or a UI presents excluded text or unverifiable evidence (OQ-E21).
- Additional join relations (e.g. editorial insertions); none is defined.
- Domain citation conventions, such as referring to a text by its opening words; these are not join relations and are not addressed here.
- Field names, storage, API and UI representation.
