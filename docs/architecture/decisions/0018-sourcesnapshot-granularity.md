# ADR-0018: SourceSnapshot granularity

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-055
- **Refines:** ADR-0004

## Context
ADR-0004 made snapshots immutable and content-addressed. The version boundary for citable content, and how metadata-only changes are treated, needed to be explicit (OQ-E09).

## Decision
- A **SourceSnapshot is the immutable version boundary for citable source content.** A Source may have multiple snapshots.
- **Every Passage belongs to exactly one SourceSnapshot.**
- A snapshot has a **deterministic content hash**. Original source content is immutable.
- If citable source content changes, a **new snapshot** is created; the old one is never modified.
- **Metadata-only changes** that do not change acquired source content do not create a new textual snapshot (they are append-only metadata revisions).
- Reasoning runs must be traceable to the exact snapshot and content used.

## Consequences
- One Acquisition may still produce snapshots for several Sources (e.g. a multi-layer provider), each Source versioned independently.
- Deterministic hashing requires a defined canonical serialisation of snapshot content; that is a schema-design detail.
