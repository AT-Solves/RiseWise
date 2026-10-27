# ADR-0023: EvidenceAnchor semantics

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-067
- **Resolves:** OQ-E11 (semantics only; representation details remain implementation-level)
- **Related:** ADR-0015 (DR-052), ADR-0017 (DR-054), ADR-0018 (DR-055), ADR-0019 (DR-056), ADR-0022 (DR-064)

## Context
DR-064 allowed an EvidenceAnchor to contain multiple ordered, passage-local segments within one SourceSnapshot, but left the anchor's semantics and verification requirements open (OQ-E11). The Source Model already lists EvidenceAnchor as a value object (§21), and DR-054's ULID rule applies to persisted entities. The source hashing rules (text-to-bytes encoding, snapshot serialisation) and the order of Passages within a SourceSnapshot are not yet defined.

## Decision
An **EvidenceAnchor** is a **value object** representing **one cited textual selection**, consisting of **one or more ordered, passage-local segments** belonging to **exactly one SourceSnapshot**.

1. EvidenceAnchor remains a value object. It is not a persisted entity and carries no ULID; DR-054 is unaffected.
2. One EvidenceAnchor represents one cited textual selection, potentially crossing Passage boundaries. Multiple independent pieces of evidence are represented by multiple EvidenceAnchors at the Tarka claim/evidence layer.
3. Each segment is local to one Passage.
4. All segments belong to exactly one SourceSnapshot, and the anchor identifies that SourceSnapshot.
5. Each segment is independently verifiable using the approved Passage identity, Passage content hash, DR-052 span, exact stored `original` text and quoted-text verification rules.
6. The complete anchor must be deterministically verifiable as an ordered whole. Verification must be capable of detecting changes to SourceSnapshot identity, segment membership/count, segment ordering, Passage identity, Passage content hash, span or quoted text.
7. The representation must remain extensible for future join/omission semantics. This ADR defines no join or omission vocabulary or semantics.
8. Verification uses whatever canonical hashing and serialisation rules are eventually approved, applied deterministically.

## Consequences
- A single-segment anchor is the special case of a one-segment selection; the existing single-segment examples remain valid.
- Tarka represents several pieces of evidence for a claim as several anchors, not as one anchor.
- The reasoning-run record in the Source Model (§9) records the SourceSnapshot once per EvidenceAnchor and Passage-specific references and content hashes per segment. This is a documentation consequence, not a new reasoning-run decision.
- No schema, storage, API or UI representation follows from this ADR.

## Explicit non-decisions / follow-up questions
This ADR approves **no** particular composite hash construction, canonical byte encoding, canonical serialisation, passage-order rule, segment well-formedness rule, verification-state vocabulary, storage representation, API or UI. Tracked in OPEN_QUESTIONS.md:
- OQ-E12 — gaps and ellipsis; join/omission semantics between segments.
- OQ-E13 — Unicode segmentation library and version.
- OQ-E14 — domain-specific Passage segmentation.
- OQ-E15 — Passage order within a SourceSnapshot.
- OQ-E16 — canonical byte encoding for source text hashes.
- OQ-E17 — canonical serialisation of the SourceSnapshot content hash.
- OQ-E18 — exact composite EvidenceAnchor hash construction.
- OQ-E19 — carrying EvidenceAnchors to a new SourceSnapshot.
- OQ-E20 — segment well-formedness.
- OQ-E21 — source-layer verification state vs Tarka's treatment/display of unavailable or unverifiable evidence.
