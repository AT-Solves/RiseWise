# ADR-0002: Locus (address) is distinct from Passage (text)

- **Status:** Accepted (2026-10-26) · **Amended by** ADR-0016 (2026-10-27): mappings only where established, explicit and provenance-bearing · **Refined by** ADR-0022 (2026-10-27): PassageLocus may carry an optional span; structure is never modelled as nested Passages
- **Design reference:** source-model.md §3, §4, §11

## Context
The same citation address (e.g. a verse or a sūtra) appears in several editions, translations and commentaries, sometimes with different segmentation or numbering. If text were stored "at" an address, editions would compete for one slot and disagreements would be lost.

## Decision
- A **CitationScheme** (declared by a domain extension, versioned) defines addresses.
- A **Locus** is one address under a scheme. **A Locus holds no text.**
- A **Passage** holds text and maps to one or more Loci through a PassageLocus mapping typed `EXACT`, `PARTIAL`, `SPLIT` or `MERGED`.
- Schemes may be work-level or edition-specific; edition-specific schemes are aligned to work-level ones by mappings, not by rewriting.

## Consequences
- Editions, translations and commentaries line up through shared loci without being merged.
- Edition-specific numbering (e.g. a numbering that differs between printings) is supported without changing the core.
- Open design points before schema work: locus scoping for edition-specific schemes and locus-to-locus mapping between schemes (see OPEN_QUESTIONS OQ-E04, OQ-E05).
