# ADR-0028: SourceSnapshot content identity for hashing

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-072
- **Resolves:** OQ-E17 (identity inputs and serialisation requirements; exact serialisation remains open)
- **Related:** ADR-0004, ADR-0005, ADR-0016 (DR-053), ADR-0018 (DR-055), ADR-0021, ADR-0022 (DR-064), ADR-0023 (DR-067), ADR-0024 (DR-068), ADR-0027 (DR-071)

## Context
ADR-0004 and ADR-0018 require each SourceSnapshot to have a deterministic content hash; ADR-0018 left its canonical serialisation open (OQ-E17). Since then, DR-064 fixed a single flat Passage segmentation per snapshot, DR-068 an immutable logical Passage order, and DR-071 how a single text value becomes bytes for its hash. ADR-0005 allows Passages to hold only their hash (`HASH_ONLY` / `WITHHELD`), and ADR-0004 keeps hashes after licence-driven purges. What remained was which snapshot components form its content identity and what its serialisation must guarantee.

## Decision
The SourceSnapshot content hash is derived from the ordered sequence of the snapshot's Passage `contentHash` values, in the snapshot's DR-068 logical Passage order, and nothing else.

## Detailed rules
1. **Identity inputs.** The snapshot's Passage `contentHash` values, each computed under DR-071 / ADR-0027.
2. **Order.** The inputs are taken in the snapshot's DR-068 logical Passage order only — never from entity IDs, locus numbering, storage/insertion order or physical acquisition order.
3. **Exclusions.** The following are not part of SourceSnapshot content identity: PassageLocus and any locus information; entity IDs (Work, Edition, Source, SourceSnapshot, Passage); acquisition, provenance, decoding, licence, verification and parser metadata; storage state, including `contentState`; derived/search data (e.g. normalisations, accent profiles, search keys).
4. **Algorithm.** SHA-256 as established by ADR-0004; not redefined.
5. **Serialisation requirements.** The eventual serialisation of the identity inputs must: be deterministic; preserve Passage order; preserve Passage boundaries; distinguish an empty Passage from an absent Passage; use a snapshot-hash domain distinct from other hash types; and have an identifiable format/version.
6. **Not yet chosen.** The exact serialisation — framing, count or length encoding, domain tag value, representation of the format/version, any structured serialisation format, and storage representation — is **not** chosen by this ADR and remains open.

## Resulting hash chain
- `Passage.original` → DR-071 canonical text hashing → `Passage.contentHash`.
- `Passage.contentHash` values → DR-068 logical Passage order → SourceSnapshot content identity (this ADR) → exact serialisation (still open) → `SourceSnapshot.contentHash`.
- PassageLocus remains a separate addressing layer, governed as metadata with provenance.

## Alternatives considered

| Alternative | Why not chosen |
|---|---|
| Raw Passage text instead of Passage `contentHash` | Snapshots containing `HASH_ONLY` or tombstoned Passages could not have their hash recomputed (ADR-0004, ADR-0005) |
| Concatenating Passage texts | Loses Passage boundaries (`["ab","c"]` vs `["a","bc"]`), which DR-064 makes part of snapshot identity |
| Including PassageLocus | Locus is addressing, separate from Passage identity (ADR-0022, DR-053); including it would make metadata corrections create new snapshots, contrary to DR-055 |
| Including entity IDs | Identical content would hash differently; content identity is distinct from entity identity (DR-054) |
| Hashing the acquired bytes | Already covered by the Manifest (ADR-0021); does not reflect segmentation or order |

## Consequences
- Identical segmentation, order and Passage text give identical snapshot hashes across re-imports and conforming implementations of the eventual serialisation.
- Metadata revisions, including locus corrections, do not change the snapshot hash and do not create a new snapshot (DR-055).
- A snapshot hash can be recomputed from retained Passage hashes, the eventual serialisation rule and the hash algorithm, without the text.
- Passage hash scheme identification, already required by DR-071, is needed for snapshot verification.

## Non-goals
- Exact framing, field tags, count or length encoding, domain tag value, version representation, structured serialisation format, storage fields.
- Empty-Passage validity (OQ-E14).
- The composite EvidenceAnchor hash (OQ-E18).
- The text-to-bytes rule (DR-071) and the hash algorithm (ADR-0004).

## Relationship to existing decisions

| Decision | Relationship |
|---|---|
| ADR-0004 | Algorithm inherited; tombstoned content remains verifiable through retained hashes |
| ADR-0018 / DR-055 | Fills, at the level of identity inputs and requirements, the serialisation gap ADR-0018 left open; consistent with metadata-only changes not creating a new snapshot |
| ADR-0021 | Acquired-byte hashes in the Manifest are separate and unaffected |
| ADR-0022 / DR-064 | Passage boundaries are part of identity (one segmentation per snapshot); structure via Locus is excluded |
| DR-053 | A Locus is an address, not evidence; addressing is excluded |
| DR-054 | Content hashes remain distinct from entity IDs |
| DR-067 | EvidenceAnchors bind to snapshot, Passage, `contentHash` and span, not to loci; unaffected |
| DR-068 | The only source of order |
| DR-071 / ADR-0027 | Defines each Passage `contentHash`; not redefined |

## Boundary with E16 and E18
- **E16** (DR-071): one text value → canonical bytes.
- **E17** (this ADR): ordered sequence of Passage content hashes → snapshot content identity, with serialisation requirements; exact serialisation open.
- **E18**: EvidenceAnchor → composite hash — **still open**. E17's snapshot-hash domain must remain distinct from other hash types, including the eventual EvidenceAnchor hash domain; E18 remains responsible for deciding its own domain and serialisation.
