# ADR-0021: Acquired bytes and decoded passage text

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-052 (reconciliation), DR-015
- **Amends:** ADR-0005 (its wording "Passage text is stored exactly as received")
- **Resolves:** CONFLICTS.md C-010

## Context
ADR-0005 says passage text is stored "exactly as received". ADR-0015 counts evidence offsets in Unicode scalar values over the stored `original` text. If acquired material is not valid Unicode (e.g. malformed UTF-8 or a legacy font encoding), the passage text cannot be both byte-for-byte as received and a valid sequence of Unicode scalar values.

## Decision
- **Acquired source bytes are preserved** as the original acquired artifact (the files in the Acquisition's Manifest) and are **hashed**. This is the byte-exact record of what was received.
- A Passage's **`original` is a decoded Unicode representation** of the acquired material. It is otherwise unaltered: no normalisation, no accent stripping, no character substitution.
- The **decoding method** (source encoding, decoder and version, and any transcoding from a legacy encoding) is **recorded as provenance** of the `parse` activity.
- Invalid or undecodable material is **never silently replaced** with U+FFFD or any other substitute. It is quarantined, or otherwise prevented from becoming citable evidence, until resolved.
- ADR-0015 offsets operate on the exact stored Unicode `original`. **Unicode offsets are not byte offsets.**

**How ADR-0005 now reads:** "stored exactly as received" applies to the acquired bytes; the Passage `original` is the faithful decoded text of those bytes, with the decoding recorded. All other ADR-0005 rules (additive normalisation, accents are text, hash-only passages where storage is not permitted) are unchanged.

## Consequences
- Byte-level fidelity is checkable from the Manifest; text-level fidelity from passage `contentHash`.
- A transcoding from a legacy encoding is itself a recorded transformation and should be verifiable (e.g. by round-trip or collation).
- The working-copy normalisation policy remains open (OQ-E03, DR-051).
