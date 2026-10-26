# ADR-0010: No silent merging of editions; no substitution of unavailable sources

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §2 (P5), §10, §22 case 5

## Context
Editions disagree. Desired sources are sometimes unavailable. Silently resolving disagreements or quietly substituting a different source would produce confident-looking but untraceable results.

## Decision
- Passages from different editions at the same locus are **kept side by side**; there is no canonical-text field on Locus.
- Any preference between editions is an attributed **AuthorityAssessment**, never an overwrite or merge.
- **No-substitution rule:** when a requested Work, Edition, layer or recension is unavailable, the availability label and reason are passed on. It is forbidden to substitute: a translation for the original; a commentary for the root text; another recension; an unaccented text for an accented one; unverified OCR; a copy with unclear licence; or LLM recollection.

## Consequences
- Disagreements surface to the reasoning layer, which must report them (e.g. as contested) rather than hide them.
- Some questions will honestly end with insufficient evidence.
