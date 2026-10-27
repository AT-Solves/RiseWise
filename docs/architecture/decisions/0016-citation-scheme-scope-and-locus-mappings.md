# ADR-0016: Citation-scheme scope and explicit locus mappings

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-053
- **Amends:** ADR-0002 (its statement that edition-specific schemes "are aligned to work-level ones by mappings")

## Context
ADR-0002 separated Locus (address) from Passage (text) and said edition-specific schemes are aligned to work-level ones by mappings. That wording implies every edition-specific scheme must be mapped, and does not say what a mapping must contain. Edition-specific numberings (e.g. Siddhānta Kaumudī serial numbers, OQ-V04) differ between editions, and numbering that looks sequential or identical is not evidence of correspondence.

## Decision
- Every **CitationScheme declares its scope: `WORK` or `EDITION`.** A Locus belongs to the scope of its scheme.
- Work-scoped loci may support cross-edition addressing **only where that is genuinely valid**. Edition-scoped loci preserve edition-specific numbering.
- **Mappings between loci are not automatically required.** A mapping exists only where it is genuinely established.
- Every mapping is **explicit, typed and provenance-bearing**. It is never inferred from matching or sequential numbers.
- A Locus is an address; a Passage is the textual evidence. (Unchanged from ADR-0002.)

**Minimum model change.** A locus mapping is represented as a constrained **Relation** between two Loci (predicate `LOCUS_MAPS_TO`), not a new top-level entity. Required fields:

| Field | Meaning |
|---|---|
| `fromLocus`, `toLocus` | The two loci (each with its scheme and scope) |
| `mappingType` | e.g. `EQUIVALENT`, `CONTAINS`, `CONTAINED_IN`, `OVERLAPS` (vocabulary finalised in schema design) |
| `basis` | What establishes the mapping: a cited concordance, an edition's own cross-reference, or reviewed passage comparison, as evidence anchors or source references |
| `provenance` | ProvenanceRecord: who or what asserted it, when, from which inputs |
| `verificationStatus` | As for other records (§8 of source-model.md) |

A mapping with no basis is not created. Where a correspondence is suspected but not established, it is recorded at most as an unresolved note, never as a mapping.

## Consequences
- ADR-0002's "aligned … by mappings" is read as "may be aligned, through explicit mappings where established".
- PassageLocus (passage → locus, `EXACT` / `PARTIAL` / `SPLIT` / `MERGED`) is unchanged and distinct from locus-to-locus mappings.
- The scope of each provisional Vedic scheme (`rv.msr`, `rv.aas`, `ts.kpa`, `asht.aps`, `sk.num`) still needs expert confirmation (DR-045).
