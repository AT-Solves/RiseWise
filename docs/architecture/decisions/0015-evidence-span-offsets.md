# ADR-0015: Evidence span offsets

- **Status:** Accepted (2026-10-27) · **Refined by** ADR-0022 (2026-10-27): multi-segment anchors within one snapshot; spans must not split an extended grapheme cluster
- **Decision Register:** DR-052
- **Related:** ADR-0004, ADR-0005, ADR-0021

## Context
Evidence anchors point into passage text. The offset unit had to be fixed before any anchor exists, because changing it later would require migrating every anchor (OQ-E02). Vedic text contains combining accent marks, so the unit must be unambiguous.

## Decision
- Evidence span offsets count **Unicode scalar values (code points)**. They are **not byte offsets** and not grapheme-cluster offsets.
- Offsets are **zero-based and half-open**: `[start, end)`.
- The coordinate system is the **exact stored `original` Passage text** (the decoded Unicode text defined in ADR-0021). Normalised or search text is **never** the coordinate system.
- `quotedTextHash` verifies the extracted span; `contentHash` verifies the complete passage.
- A span must not split an invalid Unicode sequence. (Under ADR-0021, citable `original` text contains only valid Unicode scalar values, so every offset falls on a scalar-value boundary.)

## Consequences
- Anchors are stable as long as the stored `original` is unchanged; any content change produces a new SourceSnapshot (ADR-0018) and old anchors keep pointing at the old snapshot.
- A span boundary may fall inside a grapheme cluster (e.g. between a base letter and its accent mark). Whether such spans should be allowed, warned or rejected is part of the open passage-granularity question (DR-064, OQ-E08).
- The Unicode working-copy normalisation policy (OQ-E03, DR-051) no longer affects offsets, but remains open.
- Out of scope here and still open: passage granularity and spans crossing passage boundaries (DR-064).
