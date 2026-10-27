# ADR-0020: ROOT_TEXT is a reviewed designation, not a layer or an authority tier

- **Status:** Accepted (2026-10-27)
- **Decision Register:** DR-057
- **Related:** ADR-0003, ADR-0005, ADR-0011, ADR-0013

## Context
The original question (OQ-E07) asked whether a generic `ROOT_TEXT` layer type was needed for works like the Aṣṭādhyāyī. The documentation was using "root text" in three different senses:

1. as a **layer / artifact type** (Example 03: `layer: ROOT_TEXT`);
2. as the **authoritative textual layer** for a work (what DR-057 now defines);
3. as an **authority tier** (`ROOT_TEXT_EDITION` in the `vedic-sanskrit` rubric, source-model.md §11g).

## Decision
- **`ROOT_TEXT` is an explicit, reviewed designation (role).** It applies only to a reviewed textual artifact representing the authoritative textual layer for a specified Work or Edition context.
- It is **never inferred** from language, origin, OCR, website labelling, agreement with another source, or LLM generation.
- A Work may have multiple legitimate textual representations across editions/recensions; these remain explicitly distinguished.
- Translation, commentary, transliteration, normalised text, OCR derivatives, reconstruction and other derived representations never silently replace ROOT_TEXT.
- For Vedic sources, required accent information is part of the source text itself and is preserved as textual content (consistent with ADR-0005).

**Three separate concepts:**

| Concept | What it says | Where it lives |
|---|---|---|
| Layer / artifact type | What kind of representation a Source is (e.g. `SAMHITA_PATHA`, `PADAPATHA`, `TRANSLATION`, `COMMENTARY`) | `Source.layer` (extension-defined) |
| ROOT_TEXT designation | That a reviewed artifact is the authoritative textual layer for a stated Work/Edition context | A constrained **Relation** `DESIGNATED_ROOT_TEXT_FOR` (Source snapshot → Work or Edition context) with reviewer, date, rationale and review status in its provenance |
| Authority assessment | How much weight a source carries for a purpose | AuthorityAssessment (ADR-0008) |

**Consequences for existing terms:**
- `ROOT_TEXT` is **not a layer type**. Example 03's `layer: ROOT_TEXT` is withdrawn. Which layer type non-Vedic base texts (e.g. sūtra texts) should use remains open (DR-066).
- `ROOT_TEXT_EDITION` in the authority rubric **overlaps** with this designation: it names a text role, not a degree of authority. It is **retained for now, not renamed**, and must not be read as a ROOT_TEXT designation. Its rename or removal is handled with the open Vedic authority rubric (DR-049).
- No current source in the examples has a ROOT_TEXT designation. Designation requires review; no expert review has taken place (DR-048).
