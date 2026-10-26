# Open questions

Cross-project index: [`DECISION_REGISTER.md`](DECISION_REGISTER.md) — new conflicts and questions must also be considered for the register.

Unresolved items from the RiseWise Knowledge Source Model v0.1. **Nothing here is architectural truth.** Facts tagged [S] (search summary of an official page) or [K] (background knowledge) must be confirmed against primary sources or by an expert before they are used in implementation, fixtures or UI copy.

Categories: **L** licensing/legal · **V** Vedic/Sanskrit facts and conventions · **E** engineering/model · **P** product/people.

**Before schema design (Step 2)** at minimum: OQ-E01, OQ-E02, OQ-E04, OQ-E05, OQ-E08 should be resolved or given an explicit provisional answer.

---

## L — Licensing and legal

| ID | Question | Owner | Source |
|---|---|---|---|
| OQ-L01 | How do NC, share-alike and scholarly-only licences map to each use context (local personal, hosted free, hosted paid, enterprise)? Conservative default until decided: NC/scholarly-only ⇒ `USER_IMPORT_ONLY` in hosted or paid contexts. | Product owner + legal | §7, §20.1 |
| OQ-L02 | May text from non-open sources be sent to cloud LLM / embedding services? Proposed default: only `REDISTRIBUTABLE` content unless the licence explicitly allows it. | Product owner + legal | §19, §20.2 |
| OQ-L03 | Maximum excerpt length for displaying non-redistributable text. | Product owner + legal | §20.3 |
| OQ-L04 | Who may set `CURATOR_VERIFIED` / `LEGAL_REVIEWED` on a licence, and what evidence is required? | Product owner | §20.4 |
| OQ-L05 | Licence for RiseWise's first-party corpus and annotations (e.g. CC BY 4.0 or CC BY-SA 4.0). | Product owner | §18, §20.7 |
| OQ-L06 | Licence for RiseWise code (pending since the architecture proposal: Apache-2.0 recommended). | Product owner | §20.7a |
| OQ-L07 | GRETIL: confirm collection licence (reported CC BY-NC-SA 4.0 [S]) and per-file headers for each file of interest. | Curator | research |
| OQ-L08 | Which public-domain printed editions are legally free to transcribe, given possible protection of scholarly/critical editions in some jurisdictions (e.g. German law [K])? | Legal | §18 |
| OQ-L09 | Confirm public-domain status of the underlying works behind VedaWeb translations (e.g. Griffith 1890 [K]) and the rights status of the Geldner HOS 2003 layer (C-004). | Curator + legal | ex. 01 |
| OQ-L10 | Sanskrit Library / TITUS: written confirmation of TS redistribution terms (C-006); TITUS terms for any other Vedic text [S]. | Product owner (correspondence) | ex. 02, 04 |
| OQ-L11 | ashtadhyayi.com: written permission (commercial use, redistribution) and the source edition for each commentary file (C-008). | Product owner (correspondence) | ex. 03 |
| ~~OQ-L12~~ | **Resolved 2026-10-26** — silent upstream terms are `UNKNOWN` and pending review (ADR-0012; RiseWise conservative product policy, not legal advice). | — | C-009 |
| OQ-L14 | Clarification requests to VedaWeb (per layer: vnh, aufrecht, padapāṭha, Lubotsky, Zurich, translations) on upstream rights, needed before any VedaWeb layer can be shared evidence (ADR-0012). | Product owner (correspondence) | §22.6 |
| OQ-L15 | Required uses per use context (which of STORE / DISPLAY / REDISTRIBUTE / DERIVE / COMMERCIAL_USE / EXTERNAL_PROCESSING each context needs) — policy configuration, part of OQ-L01. | Product owner + legal | §7.1 |
| OQ-L13 | DCS: confirm licence version (3.0 vs 4.0, C-005). Vidyut: confirm the data-bundle licence (code is MIT [V]). Sanskrit Heritage: confirm LGPLLR terms [S]. Cologne dictionaries: confirm per-dictionary terms under the repository's CC BY-SA 4.0 [V]. | Curator | research |

## V — Vedic/Sanskrit facts and conventions (provisional in the `vedic-sanskrit` extension)

| ID | Item | Tag | Where used |
|---|---|---|---|
| OQ-V01 | Recension of the extant Ṛgveda text recorded as Śākala. | [S] | ex. 01 |
| OQ-V02 | Alternative RV division aṣṭaka.adhyāya.varga.ṛc (`rv.aas`) and its mapping to `rv.msr`. | [K] | §11b |
| OQ-V03 | TS citation convention (`ts.kpa`): levels below anuvāka, their names, and which edition's segmentation to follow. | [K] | §11b, ex. 02 |
| OQ-V04 | Siddhānta Kaumudī sūtra numbering differs between editions (`sk.num` edition-specific); which editions/numberings to support. | [K] | §11b, ex. 03 |
| OQ-V05 | Is `REARRANGEMENT_OF` the right relation between Siddhānta Kaumudī and Aṣṭādhyāyī (rearranged sūtras plus explanation)? | [K] | §4, ex. 03 |
| OQ-V06 | Authority rubric tiers for the Vedic domain, and which purposes they apply to. | design | §11g |
| OQ-V07 | Which VedaWeb RV versions carry accents, and how they are encoded. | [K] | ex. 01 |
| OQ-V08 | Sanskrit Library TS: encoding (SLP1?) and whether accents are encoded (Weber's edition is accented). | [K] | ex. 02 |
| OQ-V09 | How to model Kṛṣṇa Yajurveda grouping and śākhā relations (`PART_OF` / `RECENSION_OF`). | design | ex. 02 |
| OQ-V10 | Bibliographic details: Müller RV with Sāyaṇa (1849–74 [S]); Weber TS (1871–72 [S]); van Nooten & Holland (HOS, 1994 [S]); Fushimi → TITUS → Sanskrit Library chain [S]; Mysore TS with Bhaṭṭa Bhāskara (1894–98 [S]) and its gaps (kāṇḍa 4 commentary; vols 6–7 not published [S]); Ānandāśrama TS with Sāyaṇa (1900–08 [S]). | [S] | ex. 01, 02 |
| OQ-V11 | Keith's TS translation (HOS, 1914): edition details, public-domain status, scan availability. | [K] | ex. 02 |
| OQ-V12 | Does the Sanskrit Library TS file include a padapāṭha? | unknown | ex. 02 |
| OQ-V13 | Böhtlingk's Aṣṭādhyāyī (1887) as a public-domain collation print. | [K] | ex. 03 |
| OQ-V14 | Vedic coverage and accent handling in DCS (believed unaccented [K]); Vedic and grammar coverage in Ambuda. | [K] | research |
| OQ-V15 | List of dictionaries in the Cologne collection (Monier-Williams, Böhtlingk–Roth, Grassmann, Apte). | [K] | research |

## E — Engineering and model

| ID | Question | Notes |
|---|---|---|
| OQ-E01 | Identifier scheme: opaque ids (e.g. ULID) plus human-readable keys (`work:rv`)? Proposed: both. | §20.9 |
| OQ-E02 | **Span offsets** for EvidenceAnchor: measured in which unit (Unicode code points of the raw original? NFC working copy? grapheme clusters?). Must be fixed before anchors exist. | pre-schema |
| OQ-E03 | Unicode policy for the working copy of Vedic text (NFC vs none) given canonical reordering of combining accent marks; raw original remains the reference. | §11d, §19 |
| OQ-E04 | **Locus scope:** a Locus is defined as an address in a Work, but edition-specific schemes (`sk.num`) address an Edition. Should Locus/CitationScheme carry an optional edition scope? | ADR-0002 |
| OQ-E05 | **Locus-to-locus mapping** between schemes (`rv.aas` ↔ `rv.msr`, `sk.num` ↔ `asht.aps`): a separate mapping record, or Relations between Loci? | ADR-0002 |
| OQ-E06 | Annotation targets across versions: which text version's tokenisation does a dataset (e.g. Zurich morphology) align to, and how is that alignment recorded? | ex. 01 |
| OQ-E07 | Root-text layer type for non-Vedic śāstra works (e.g. sūtra texts): add a generic `ROOT_TEXT` layer to the core or the extension? | ex. 03 |
| OQ-E08 | **Passage granularity:** one level (e.g. ṛc) or hierarchical (sūkta ⊃ ṛc ⊃ pāda)? How do evidence spans cross passage boundaries? | pre-schema |
| OQ-E09 | Snapshot granularity for multi-layer providers: one snapshot per Source (proposed) under a shared Acquisition — confirm. | §4 |
| OQ-E10 | Evidence eligibility of human-curated annotation datasets (e.g. Zurich morphology): eligible after `ANNOTATION_SPOT_CHECK`, or immediately with origin `DATASET`? | ex. 01 |

## P — Product and people

| ID | Question |
|---|---|
| OQ-P01 | Is a Sanskritist available for collation, scheme confirmation (OQ-V*) and Vedic verification? |
| OQ-P02 | Commercial intent and tier timeline (drives OQ-L01). |
| OQ-P03 | Who sends permission requests to providers (OQ-L10, OQ-L11)? Drafts can be prepared on request. |
