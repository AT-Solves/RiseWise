# ADR-0005: Preserve the original text; normalisation is additive; accents are text

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §2 (P2), §11d, §19

## Context
Sanskrit sources use several scripts and transliteration schemes, and Vedic texts carry accent marks. Normalising text for search or display can silently lose information (e.g. stripping or reordering combining accent marks).

## Decision
- Passage text is stored **exactly as received** where the licence permits storage.
- Normalised forms (search keys, display transliterations) are **additional, versioned, derived fields**; they never replace the original.
- Display transliterations must pass a verified round-trip check.
- **Accent marks are part of the text, never an annotation.** Separate accent *analysis* may exist as an annotation layer.
- Where a licence forbids storage, a passage may hold only its hash (`contentState: HASH_ONLY` / `WITHHELD`).

## Consequences
- No silent loss of script, encoding or accent information.
- The exact Unicode normalisation policy for the working copy is still open (OQ-E03); the raw original remains the reference either way.
