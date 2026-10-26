# ADR-0012: Conservative rights policy — silence is not permission

- **Status:** Accepted (2026-10-26)
- **Refines:** ADR-0006 (does not supersede it)
- **Resolves:** CONFLICTS.md C-009
- **Design reference:** source-model.md §7.1, §22.6

> **RiseWise conservative product policy — not legal advice.** This ADR defines RiseWise's behaviour. It does not state what any licence legally permits.

## Context
ADR-0006 combined licence records by "most restrictive term" and treated `UNKNOWN` as pending, but did not say how an upstream notice that is *silent* on a term combines with a downstream licence that grants it (CONFLICT C-009). The paper test showed the outcome for real sources depends entirely on this choice.

## Decision
If RiseWise cannot establish that a particular use is permitted, it does not assume permission.

1. Explicitly permitted → `PERMITTED`, subject to all attached conditions and other applicable restrictions.
2. Explicitly prohibited → `PROHIBITED`.
3. Silent or unknown → `UNKNOWN` → pending review.
4. Conflicting statements (including a downstream grant broader than an upstream term) → the more restrictive interpretation until clarified.
5. A source with unresolved rights for a use must not become shared or public evidence.
6. A user may use their own legitimately obtained copy through the private `USER_SUPPLIED` pathway, subject to their own rights and workspace restrictions.
7. RiseWise never claims that silence in a licence means permission.

Terms are evaluated **per use** (`STORE`, `DISPLAY_FULL`, `DISPLAY_EXCERPT`, `REDISTRIBUTE`, `DERIVE`, `COMMERCIAL_USE`, `EXTERNAL_PROCESSING`) across the **whole rights chain**: Work, Edition, Source and every disclosed upstream link. A disclosed upstream link with no documented terms contributes `UNKNOWN`. Order of restrictiveness: `PROHIBITED` > `UNKNOWN` > `PERMITTED`; conditions are unioned.

Access classes remain the five of ADR-0007 and remain **context-dependent**: a context is affected only by the uses it requires. Rights are resolved only when every link has evidence for the term and the licence record has been reviewed. Clarifications are stored as **licence evidence**, separate from provenance and verification (ADR-0008). LLM output remains excluded as source evidence (ADR-0009).

## Consequences
- Every real VedaWeb Ṛgveda layer and the Sanskrit Library Taittirīya Saṃhitā are `LICENCE_PENDING` for shared/public use until their rights chains are clarified (source-model.md §22.6).
- RiseWise needs a clarification workflow (requests to providers/rights holders) before any third-party Vedic text can be shared evidence; private `USER_SUPPLIED` use remains possible meanwhile.
- The schema must represent tri-state per-use terms, conditions, rights-chain links, and conflicting statements; it never defaults a term to `PERMITTED`.
