# ADR-0024: Passage order within a SourceSnapshot

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-068
- **Resolves:** OQ-E15
- **Related:** ADR-0016 (DR-053), ADR-0018 (DR-055), ADR-0022 (DR-064), ADR-0023 (DR-067)

## Context
DR-064 established one flat, non-overlapping Passage segmentation per SourceSnapshot, and DR-067 established that an EvidenceAnchor's segments are ordered. Neither defined the order of Passages within a SourceSnapshot, so there was no source-level relation against which the order or contiguity of an anchor's segments could later be judged (OQ-E15). Several different kinds of order exist and can legitimately differ: the order in which material was physically acquired, the order a reader traverses the text, the order implied by a citation scheme, structural containment, and the order a user interface displays.

## Decision
A **SourceSnapshot has a declared, deterministic logical reading order over its Passages.** Conceptually this is a snapshot-level ordered Passage sequence.

This order is:
- the logical textual/reading order of the SourceSnapshot's declared Passage segmentation;
- immutable, as part of the SourceSnapshot's declared segmentation;
- provenance-bearing (the segmentation, including its order, is attributable to the agent or process that declared it);
- independent of physical acquisition order;
- independent of scholarly/citation order;
- independent of UI display order;
- **never inferred** from citation numbers, Locus numbering, page numbering, Passage IDs, sequential database IDs, or matching numeric labels (consistent with DR-053).

**The kinds of order remain separate:**

| Order | Belongs to |
|---|---|
| Logical reading order | The SourceSnapshot's declared Passage segmentation (this ADR) |
| Physical/acquisition order | Acquisition / Manifest / provenance |
| Scholarly/citation order | CitationScheme / Locus |
| Structural order | Locus / PassageLocus |
| Display order | UI |

No storage representation is required by this ADR. An ordinal or an equivalent representation may be chosen later as an implementation detail, provided it represents the same immutable, snapshot-level ordering semantics.

## Consequences
- **Snapshots:** because the logical Passage order is part of the declared segmentation, a materially different Passage order is a different segmentation state and requires a new SourceSnapshot (consistent with DR-055 and DR-064).
- **DR-064 reading:** DR-064's statement that every character of a SourceSnapshot belongs to exactly one Passage is read together with this ADR: the Passage segmentation is an ordered segmentation of the SourceSnapshot's citable textual content. Ingestion and segmentation rules determine what source material enters that textual content. This ADR does not state that any source is physically "one linear text".
- **EvidenceAnchor:** EvidenceAnchor segment order remains the anchor's explicit segment order as defined by DR-067. Passage order provides the source-level order against which future rules (OQ-E12, OQ-E20) can reason. This ADR does not decide whether anchors must follow source order, whether reverse-order segments are invalid, whether skipped Passages represent gaps or ellipsis, whether a Passage may appear more than once, or any adjacency/merging rule.
- **Complex material:** footnotes, marginalia, tables, multi-column layouts, headers/footers, appendices and damaged or missing material are ingestion/segmentation questions and are not resolved here.

## Explicit non-decisions / follow-up questions
Not decided by this ADR:
- Field names, database representation, ordinal format, linked-list (`NEXT`) representation, API representation and UI ordering (implementation).
- OQ-E12 — gaps, ellipsis and join semantics.
- OQ-E13 — Unicode segmentation library and version.
- OQ-E14 — domain/source segmentation rules, including placement of complex material.
- OQ-E16 — canonical text-to-byte encoding for hashes.
- OQ-E17 — canonical serialisation of the SourceSnapshot content hash.
- OQ-E18 — EvidenceAnchor composite hash construction.
- OQ-E19 — carrying anchors across snapshots.
- OQ-E20 — segment well-formedness.
- OQ-E21 — source-layer verification state vs Tarka treatment.
