# RiseWise Knowledge Source Model — v0.1

| | |
|---|---|
| **Status** | Approved design (product owner, 2026-10-26). Documentation only — nothing here is implemented. |
| **Scope** | The domain-neutral source/knowledge layer that Tarka will later reason over. |
| **Frozen decisions** | ADR-0001 … ADR-0011 in [`decisions/`](decisions/README.md). |
| **Worked examples** | Metadata-only YAML in [`source-model-examples/`](source-model-examples/README.md). |
| **Unresolved items** | [`../OPEN_QUESTIONS.md`](../OPEN_QUESTIONS.md) and [`../CONFLICTS.md`](../CONFLICTS.md). |

## Verification tags

Facts about real sources, editions and conventions carry a tag. The tags describe how well *this document* knows the fact; they are not a judgement of the source.

| Tag | Meaning |
|---|---|
| **[V]** | Verified on the primary page during research (e.g. a README or TEI header was read directly). |
| **[S]** | Taken from a search summary of the official page. Must be re-checked against the primary source. |
| **[K]** | Background knowledge, not verified. Treat as a hypothesis. |

**No [S] or [K] item is architectural truth.** Each one is tracked in `OPEN_QUESTIONS.md` (or `CONFLICTS.md` if sources disagree). The architecture depends only on the *shape* of the model, never on these values. No corpus text is reproduced anywhere in this document; examples use `<placeholders>`.

---

## 1. Executive Summary

The Source Model is the foundation Tarka will reason over. It must answer **"Where did this come from?"** and **"What exact passage supports this?"** for any piece of knowledge — and must say honestly when RiseWise does not have a source.

The model rests on five separations:

1. **What a text is vs. which printing vs. which digital file.** A **Work** (the Ṛgveda) is realised in an **Edition** (e.g. van Nooten & Holland 1994 [S]). The edition is held as one or more **Sources** — digital representations, scans, or print references — each with immutable, versioned **SourceSnapshots** containing **Passages**.
2. **A canonical address vs. the text found at that address in one edition.** A **Locus** is a citation address (RV 1.1.1). A **Passage** is the concrete text at that address in one snapshot of one Source. Editions and translations line up through shared loci; their disagreements are recorded, never merged away.
3. **Original text, translations, commentaries and interpretations are separate.** Translations and commentaries are separate Works linked by typed relations (`TRANSLATION_OF`, `COMMENTARY_ON`). The model cannot represent a translation as the original.
4. **Provenance, Licence, Authority, Verification and Availability are five separate record types**, each with its own history. None stands in for another.
5. **Everything that feeds reasoning is immutable and content-addressed.** A reasoning result records the exact passage versions and hashes it used, plus a corpus-state id, so it can be reproduced.

Domain specifics (śākhā, maṇḍala/sūkta/ṛc, kāṇḍa/prapāṭhaka/anuvāka, padapāṭha, accents, sūtra relations) live in **domain extensions** that supply citation schemes, layer types, annotation schemas and verification rules. The core stays domain-neutral.

## 2. Design Principles

| # | Principle | Consequence |
|---|---|---|
| P1 | **Provenance is first-class** | Every content entity has a provenance chain from day one. There are no anonymous passages. |
| P2 | **The original is preserved** | Text is stored exactly as received, where the licence allows. Normalised forms are additional derived fields, never replacements. |
| P3 | **Immutability for anything reasoning cites** | Snapshots, passages and annotations are never edited in place. A change creates a new version. |
| P4 | **Unknown is never treated as permitted** | A licence that hasn't been confirmed means the content is held for review and cannot be used as evidence. |
| P5 | **No silent merging** | Conflicting editions and readings are kept side by side. Any "preferred edition" choice is a recorded, attributed assessment. |
| P6 | **Orthogonal concerns stay orthogonal** | Provenance, authority, verification, licence and availability are separate records with separate histories. |
| P7 | **LLM output is never a source** | LLM output cannot become source content. LLM-produced annotations or interpretations are stored with `origin: LLM` and are excluded as evidence. |
| P8 | **Rights are evaluated in context** | Whether something may be stored, displayed, redistributed, sent to an external processor or used commercially is computed per use context, not stored as one flag. |
| P9 | **The core is domain-neutral** | Core entities know nothing about maṇḍalas or sūtras. Extensions declare those structures. |
| P10 | **Honest absence** | Availability is a modelled state with reason codes, including "not extant" and "not published". |
| P11 | **Simple first** | The fewest entities that keep the required distinctions. Generic `Relation` and `Annotation` entities replace many special-purpose tables. |

## 3. Core Source Concepts

| Concept | Definition | Is NOT |
|---|---|---|
| **Work** | An abstract intellectual creation: a saṃhitā, a sūtra text, a commentary, a translation, a monograph, a dataset. Has a `workKind`. | A book, a file or an edition |
| **Edition** | A specific scholarly or published realisation of a Work by identified editors or publishers. Revised editions are separate Editions linked by `REVISION_OF`. | A digital file |
| **Source** | A concrete representation of an Edition that RiseWise holds or references: a digital text, a scan, or a print reference (metadata only). Born-digital works may have a Source without a print edition. | The Work, or a claim |
| **Agent** | A person, organisation, tool, model or user: authors, editors, commentators, data-entry contributors, providers, software, LLMs. | — |
| **Acquisition** | One act of obtaining material from a provider: method, time, provider version (release or commit), raw licence statements captured, file hashes. Its file list is the **Manifest**. | The content itself |
| **Manifest** | The immutable description of what an Acquisition obtained: files, sizes, SHA-256 hashes, formats, encodings, provider version, captured licence text, and which Sources it contains. | A licence decision |
| **SourceSnapshot** | One immutable version of a Source's content, produced by an Acquisition or by a RiseWise derivation such as a correction. The unit reasoning cites. | A mutable record |
| **CitationScheme** | A named, versioned addressing scheme declared by an extension (e.g. `rv.msr`). May be work-level or edition-specific. | Hard-coded structure |
| **Locus** | One address under a CitationScheme (e.g. `rv.msr:1.1.1`). Contains no text. | A passage |
| **Passage** | The concrete text unit at one or more loci inside one SourceSnapshot: original text (or only a hash if the licence forbids storage), normalised forms, script/encoding info, content hash. | A Locus, or a claim |
| **Text (content)** | The textual payload of a Passage: `original` (exact), `script`, `encoding` / `transliterationScheme`, `normalisations[]`, `contentState` (`STORED` / `HASH_ONLY` / `WITHHELD`). | Metadata |
| **Translation** | A Work with kind `TRANSLATION`, linked `TRANSLATION_OF` its target. Its passages align to the target's loci. | The original |
| **Commentary** | A Work with kind `COMMENTARY`, linked `COMMENTARY_ON` its target; sub-commentaries are `COMMENTARY_ON` another commentary. It is a text with its own loci. | Interpretation, or the root text |
| **Interpretation** | An attributed reading of a locus ("commentator X reads Y as Z"), anchored to the passage where that author says it. Origin: `SOURCE_EXTRACTED`, `HUMAN_CURATED` or `LLM_PROPOSED`. Only anchored, non-LLM interpretations may serve as evidence. | Commentary text; a fact |
| **Annotation** | Structured data about a passage span or token: linguistic (lemma, morphology, sandhi split, derivation), metrical, alignment notes. Has a producer (dataset, tool, human, LLM), an `origin`, and an extension-defined body schema. | Original text |
| **Relation** | A typed link between entities, carrying its own provenance. | — |
| **EvidenceAnchor** | A pointer from future reasoning objects to exact text: `{passageId, contentHash, span(start,end), quotedTextHash}`. Claims and conclusions belong to Tarka; the source model only guarantees the anchor can be resolved and checked. | A conclusion |
| **Citation** | A human- and machine-readable reference derived from Work + Edition + Source + Snapshot + Locus + span, formatted by the extension. | Stored free text |
| **ProvenanceRecord** | Who or what produced an entity, by which activity, from which inputs (W3C PROV style: entity, activity, agent). | Authority |
| **LicenceRecord** | Licence and rights information, each term backed by evidence of where it was stated, with a verification status. | Usage permission — that is computed from licence plus context |
| **AuthorityAssessment** | A curator's recorded judgement of how much weight a source carries **for a given purpose in a given domain**, with a rationale. | Verification, or popularity |
| **VerificationRecord** | The result of a specific check on a specific target (fidelity, integrity, metadata, licence, alignment), with method, verifier and rule version. | A claim status |
| **AvailabilityRecord** | What RiseWise actually holds for a Work, Edition or layer: holding state, origin, coverage, reason codes. The access class is computed per context. | Reliability |
| **CorpusState** | A named, immutable set of the SourceSnapshot ids active at a point in time. Reasoning runs record it. | — |

**Two status vocabularies are kept apart.** Claim statuses (`SUPPORTED`, `PARTIALLY_SUPPORTED`, `CONTRADICTED`, `CONTESTED`, `UNVERIFIED`, `INSUFFICIENT_EVIDENCE`, `INFERRED`) and epistemic kinds (`FACT`, `EVIDENCE`, `INFERENCE`, `ASSUMPTION`, `INTERPRETATION`, `UNCERTAINTY`) belong to Tarka's reasoning layer. Source *verification states* (section 8) describe source fidelity and integrity. A verified source does not make a claim `SUPPORTED`; Tarka's rules decide that from evidence anchors.

## 4. Entity Relationship Model

```
                        ┌──────────┐  Relation (typed, with provenance)
                        │  Agent   │◄───── authors / editors / commentators /
                        └────┬─────┘       providers / tools / LLMs / users
                             │
┌────────┐ realised in ┌─────▼────┐ represented by ┌──────────┐ versioned as ┌────────────────┐
│  Work  │────────────►│ Edition  │───────────────►│  Source  │─────────────►│ SourceSnapshot │
└───┬────┘   0..*      └──────────┘     0..*       └────┬─────┘    0..*      └───────┬────────┘
    │ Relation: TRANSLATION_OF / COMMENTARY_ON /         │ (born-digital:          │ produced by
    │ PART_OF / RECENSION_OF / REARRANGEMENT_OF          │  Work→Source direct)    ▼
    │                                                    │                ┌─────────────┐
    │ addressed by                                       │                │ Acquisition │──► Manifest
    ▼                                                    │                └─────────────┘   (files + hashes)
┌──────────────┐ defines ┌───────┐                       │                       │ contains
│CitationScheme│────────►│ Locus │◄──── aligned to ──────┼───────────────┐       ▼
└──────────────┘ (ext.)  └───────┘     (PassageLocus)    │               │  ┌─────────┐
                                                         │               └──│ Passage │──► Text (original,
                                                         │                  └────┬────┘     normalisations, hash)
                                                         │                       │ targeted by
                                                         │                       ▼
                                                         │                 ┌────────────┐   ┌────────────────┐
                                                         │                 │ Annotation │   │ Interpretation │
                                                         │                 └────────────┘   └────────────────┘
          attached to Work / Edition / Source / Snapshot / Passage / Annotation:
   ┌──────────────┐ ┌────────────────┐ ┌──────────────────┐ ┌───────────────────┐ ┌────────────────────┐
   │ LicenceRecord│ │ProvenanceRecord│ │VerificationRecord│ │AuthorityAssessment│ │ AvailabilityRecord │
   └──────────────┘ └────────────────┘ └──────────────────┘ └───────────────────┘ └────────────────────┘
                                                         CorpusState ──► {SourceSnapshot ids}
                                                         EvidenceAnchor ──► Passage + span + hash (used by Tarka)
```

**Cardinalities and rules**

- A Work has 0..* Editions (0 is allowed: we may know a work exists without having an edition recorded).
- An Edition has 0..* Sources (0 = reference only).
- A Source has 1..* Snapshots once acquired; a print-reference Source has none.
- An Acquisition produces 1..* Snapshots (one fetch from a multi-layer provider yields many Sources, each with its own licence).
- A Passage belongs to exactly one Snapshot and maps to 1..* Loci with a mapping type: `EXACT` / `PARTIAL` / `SPLIT` / `MERGED`.
- Licence records attach at **Work** (underlying rights, e.g. public domain), **Edition** (editorial rights), **Source** (digital representation licence) and optionally **annotation dataset** level. Effective rights combine them using the most restrictive term (section 7).

**Relation predicates (core set; extensions may add)**

| Predicate | From → To | Example (illustrative; see tags) |
|---|---|---|
| `PART_OF` | Work → Work | TS → a Kṛṣṇa Yajurveda grouping record (structure to be expert-confirmed) |
| `RECENSION_OF` | Work → Work | a śākhā-specific saṃhitā → an abstract Veda record, only where an expert-confirmed structure exists |
| `TRANSLATION_OF` | Work → Work | Griffith's RV translation → RV |
| `COMMENTARY_ON` | Work → Work | Kāśikā → Aṣṭādhyāyī; Nyāsa → Kāśikā |
| `REARRANGEMENT_OF` | Work → Work | Siddhānta Kaumudī → Aṣṭādhyāyī [K] (see OQ-V05) |
| `REVISION_OF` | Edition → Edition | 2nd edition → 1st |
| `DERIVED_FROM` | Source/Snapshot → Source/Snapshot/Edition | Sanskrit Library TEI → TITUS file → Fushimi data entry → Weber edition [S] |
| `CORRECTS` | Snapshot → Snapshot | RiseWise-corrected snapshot → imported snapshot |
| `ATTRIBUTED_TO` | Work/Interpretation → Agent | commentary → commentator (traditional attribution flagged as such) |
| `ALIGNS_WITH` | Passage → Passage | padapāṭha passage ↔ saṃhitā passage (via loci) |

## 5. Source Lifecycle

```
REGISTERED ──► RIGHTS_REVIEW ──► APPROVED_FOR_ACQUISITION ──► ACQUIRED ──► PARSED ──► VERIFIED(levels) ──► ACTIVE
    │               │                                            │            │                           │
    │               └─► REFERENCE_ONLY (cannot hold content)     │            └─► PARSE_FAILED            ├─► SUPERSEDED (newer snapshot)
    │                                                            └─► QUARANTINED (integrity/safety issue) ├─► WITHDRAWN (licence change)
    └─► NOT_AVAILABLE (with reason)                                                                       └─► TOMBSTONED (content purged,
                                                                                                               hashes + metadata kept)
```

1. **Registered** — Work/Edition/Source exist as metadata. Possible without any content, so absences can be recorded.
2. **Rights review** — licence evidence captured and checked; access class decided (section 7). Pending ⇒ content cannot be used.
3. **Acquisition** — only for approved access classes. The Manifest records method, time, provider version and hashes.
4. **Parse** — files become Passages under the extension's citation scheme. Original text kept; normalisations added; passage hashes computed.
5. **Verify** — automated integrity checks, then optional human/expert checks (section 8).
6. **Active** — the snapshot is included in the current CorpusState.
7. **Change** — re-import, correction or licence change creates new versions or state transitions. Nothing already used in reasoning is deleted without a tombstone.

This lifecycle is a design target. No importer exists in this phase.

## 6. Provenance Model

**Two kinds of provenance, kept separate**

- **Upstream provenance** — what a source *says* about its own origin (e.g. "data entry by M. Fushimi, based on Weber" [S]). Stored as **claims with their own source** (where we read it) and a verification status. Not accepted as true by default.
- **RiseWise provenance** — what RiseWise itself did: acquired, parsed, normalised, aligned, corrected, verified. Recorded by RiseWise and checkable by hash.

**ProvenanceRecord fields:** `id` · `entityRef` (type + id + contentHash) · `activity` (`acquire`, `parse`, `normalise`, `align`, `annotate`, `correct`, `verify`, `upstream-claim`) · `agentRef` (human / organisation / tool@version / model@version + prompt version) · `used[]` (input entity refs + hashes) · `startedAt` / `endedAt` · `parameters` (e.g. normalisation profile id@version) · `recordedBy` · `evidenceRef` (for upstream claims: URL or file + captured hash + date).

**Example chain** — answers "Where did this information come from?":

```
Conclusion (Tarka, later)
 └─ Inference (Tarka, later)
     └─ EvidenceAnchor {passage P#, span 12–48, quotedTextHash}
         └─ Passage P#  (locus rv.msr:1.1.1, contentHash h1)
             └─ SourceSnapshot S#v3  (manifest hash m3)
                 └─ Source "VedaWeb — vnh version"
                     └─ Edition "van Nooten & Holland, HOS 1994" [S]
                         └─ Work "Ṛgveda Saṃhitā"
             └─ Acquisition A# (git clone VedaWebProject/vedaweb-data @<commit>, <date>, by curator U)
                 └─ upstream provenance claims (TEI header [V]): UT Austin LRC revision ← van Nooten & Holland diskette [S]
```

"What exact passage supports this?" is answered by resolving the EvidenceAnchor, re-hashing the passage text and confirming it matches.

## 7. Licence & Rights Model

**LicenceRecord** (append-only revisions; attachable at Work, Edition, Source or annotation-dataset level):

| Field | Notes |
|---|---|
| `licenceId` | SPDX-style identifier where one exists (`CC-BY-4.0`, `CC-BY-NC-SA-3.0`, `LGPLLR`); otherwise `CUSTOM`, `PUBLIC_DOMAIN`, `ALL_RIGHTS_RESERVED`, `UNKNOWN` |
| `licenceUrl` / `licenceText` | URL plus a captured copy (hash + capture date) of the exact wording |
| `rightsHolder` | If known; `UNKNOWN` allowed |
| `scope` | What it covers: underlying work / edition apparatus / digital representation / annotation layer |
| `permittedUse` | `commercial` (ALLOWED / PROHIBITED / UNKNOWN), `derivatives` (ALLOWED / SHARE_ALIKE / PROHIBITED / UNKNOWN), `redistribution` (ALLOWED / CONDITIONAL / PROHIBITED / UNKNOWN), `attribution` (required? + text template), `scholarlyOnly`, `membersOnly` |
| `upstreamConstraints[]` | Inherited terms, e.g. the van Nooten–Holland "research but not commercial" notice carried into VedaWeb's version [S] |
| `acquisitionMethod` | `PUBLIC_DOWNLOAD` / `API` / `GIT_REPOSITORY` / `WRITTEN_PERMISSION` / `PURCHASED_LICENCE` / `USER_UPLOAD` / `FIRST_PARTY_TRANSCRIPTION` / `PRINT_REFERENCE` |
| `evidence[]` | Where each term was stated (URL, file, TEI header element, email) plus captured hash |
| `verificationStatus` | `UNVERIFIED` · `PROVIDER_STATED` · `CURATOR_VERIFIED` · `LEGAL_REVIEWED` · `DISPUTED` |
| `effectiveFrom` / `supersedes` | For licence changes |
| `checksumRef` | Hash of the content the licence applies to |

**Effective rights** are computed, not stored. They combine all applicable licence records (Work ∧ Edition ∧ Source ∧ upstream), taking the most restrictive value for each term. **Any `UNKNOWN` term puts the item under review (`LICENCE_PENDING`).** They are then evaluated against a **use context** by a configurable rights policy:

| Use context (configurable) | Example question |
|---|---|
| `LOCAL_PERSONAL` | A user's own machine, own research |
| `HOSTED_FREE_NONCOMMERCIAL` | Public free tier |
| `HOSTED_PAID_PROFESSIONAL` | Paid tier |
| `ENTERPRISE_PRIVATE` | Customer-hosted |
| `EXTERNAL_PROCESSOR` | May this text be sent to a cloud LLM or embedding API? |

The output is a **RightsDecision**: `canStore` · `canDisplayFull` · `canDisplayExcerpt(maxLength)` · `canRedistribute` · `canExport` · `canDeriveAnnotations` · `canSendToExternalProcessor` · `attributionText` · `shareAlikeObligation`.

**The five access classes** (derived per Source and per use context):

| Class | Meaning | Typical case |
|---|---|---|
| `REDISTRIBUTABLE` | RiseWise may store, display and redistribute, subject to attribution / share-alike | CC BY 4.0 material (DCS [S]; VedaWeb Zurich morphology [V]); public-domain first-party transcriptions |
| `INTERNAL_USE_ONLY` | RiseWise may store and use for reasoning and limited display, but not redistribute or export | written permission that excludes redistribution; NC material in a context that does not allow redistribution |
| `USER_IMPORT_ONLY` | RiseWise ships an importer, manifest and checksums only; each user obtains and stores their own copy under its terms | NC or scholarly-only sources in commercial tiers; copyrighted works the user has licensed |
| `UNAVAILABLE` | Cannot be held: restricted, not extant, or not digitised | modern copyrighted scholarship with no import route; unpublished volumes |
| `LICENCE_PENDING` | Not yet decided. Content may not be used as evidence. | ashtadhyayi.com data before written permission |

**Open rule (CONFLICT C-009, OQ-L12):** whether an upstream constraint that is *silent* on a term counts as `UNKNOWN` (⇒ pending) or as "no additional restriction" is not yet decided. Until it is, affected sources are treated as `LICENCE_PENDING`.

The class depends on context: a CC BY-NC-SA source may be `REDISTRIBUTABLE` in a free non-commercial tier but `USER_IMPORT_ONLY` in a paid tier. That mapping needs legal review (OQ-L01). **Conservative default until then:** NC and scholarly-only material is `USER_IMPORT_ONLY` in every hosted or paid context.

## 8. Verification Model

Verification concerns **source fidelity and integrity**, not truth.

**VerificationRecord:** `target` (Snapshot / Passage / Annotation / LicenceRecord / Alignment / metadata field) · `checkType` · `method` (`AUTOMATED_RULE` / `HUMAN_COLLATION` / `EXPERT_REVIEW`) · `ruleId@version` · `result` (`PASS` / `FAIL` / `PARTIAL` / `NOT_APPLICABLE`) · `details` · `verifierAgent` · `timestamp` · `evidenceRef` (e.g. the scan page compared against).

**Check types (starter set)**

| Check | Target | Method |
|---|---|---|
| `INTEGRITY_HASH` | Snapshot, Passage | Automated: stored text re-hashes to the recorded hash |
| `MANIFEST_MATCH` | Acquisition | Automated: files match the manifest |
| `STRUCTURE_VALID` | Passage loci | Automated: locators valid under the scheme; no unexpected gaps or duplicates for the declared coverage |
| `ENCODING_ROUNDTRIP` | Passage | Automated: transliteration to display script and back is lossless |
| `ACCENT_PRESERVED` | Passage (Vedic) | Automated: accent marks present where the edition is accented; no loss after normalisation |
| `EDITION_COLLATION` | Passage sample | Human/expert: digital text matches the printed edition (scan page referenced) |
| `METADATA_CONFIRMED` | Work / Edition fields | Human: e.g. editor, year, series confirmed against the title page |
| `LICENCE_CONFIRMED` | LicenceRecord | Curator or legal |
| `ALIGNMENT_CONFIRMED` | PassageLocus | Human: a translation or commentary passage really corresponds to its target locus |
| `ANNOTATION_SPOT_CHECK` | Annotation dataset | Expert sample review |

**Derived verification state** per target: `UNVERIFIED` → `INTEGRITY_CHECKED` → `HUMAN_VERIFIED` → `EXPERT_VERIFIED`; side states `DISPUTED` and `FAILED`. A failed integrity check moves a snapshot to `QUARANTINED`.

**Keeping the concepts apart**

- **Authority ≠ verification.** A highly authoritative edition can have an unverified digital copy full of typing errors; a perfectly verified copy can be of a low-authority edition. Both are shown.
- **Provenance ≠ authority.** Knowing exactly where something came from says nothing about how much weight it deserves.
- **AuthorityAssessment** fields: `subject` (Source / Edition / Work) · `domain` · `purpose` (e.g. "wording of the root text", "traditional interpretation", "historical-linguistic analysis") · `tier` from the extension rubric · `rationale` · `assessor` · `date`. Authority is never inferred from usage or popularity.

## 9. Versioning Model

| Change | Mechanism | Effect on reasoning |
|---|---|---|
| **Provider releases new data** | New Acquisition → new Manifest → new SourceSnapshot (vN+1). The old snapshot stays, marked `SUPERSEDED`. | Old results still resolve to vN. New runs use vN+1. A diff report flags changed passages. |
| **Re-import of identical files** | Same hashes → recorded as a no-op Acquisition; no new snapshot | None |
| **Edition revision** | New Edition with `REVISION_OF`, its own Sources and snapshots | A different edition; never merged |
| **Correction by RiseWise** | New **derived** snapshot (`CORRECTS` the imported one) with a correction list: locus, old hash, new text, justification, evidence (scan page), agent. Only where the licence permits derivatives; share-alike / no-derivatives terms enforced. | The corrected snapshot may be preferred; the original remains citable |
| **Changed metadata** | Append-only metadata revision with provenance; content snapshots untouched | Results record the metadata revision they displayed |
| **Changed provenance** | New upstream-provenance claim superseding the old one | Shown in "Why?" history |
| **Changed licence** | New LicenceRecord revision with `effectiveFrom`; access class recomputed. If it becomes restricted: class changes and content may be tombstoned (purged; hashes and metadata kept). | Past results remain *identifiable* (ids, hashes) even if their text can no longer be shown |
| **Corpus update across many sources** | New **CorpusState** (immutable set of active snapshot ids) | Every reasoning run stores its CorpusState id |

**Passage identity across versions.** *Lineage key* = `(sourceId, primaryLocus)`. *Version identity* = `passageId` (unique per snapshot) + `contentHash`. Unchanged passages share a `contentHash` between snapshots, so stale-evidence detection is a hash comparison.

**What a reasoning run records:** `corpusStateId`; for each evidence anchor `passageId`, `contentHash`, `snapshotId`, `manifestHash`, `licenceRevisionId`, `extensionVersion` (citation scheme + normalisation profile versions).

## 10. Availability Model

The originally proposed states (`AVAILABLE`, `PARTIAL`, `LICENCE_PENDING`, `SCAN_ONLY`, `USER_SUPPLIED`, `NOT_AVAILABLE`) work well as **user-facing labels**, but mix three independent dimensions — what content exists, what the rights are, and who provided it. A source can be partial *and* licence-pending; user-supplied material can be partial. (Logged as CONFLICT C-001, resolved by approval of this design.)

**Stored dimensions**

| Dimension | Values |
|---|---|
| **Holding** — what content RiseWise has | `FULL_TEXT` · `PARTIAL_TEXT` · `IMAGE_ONLY` (scans, unverified OCR) · `METADATA_ONLY` · `NONE` |
| **Access class** — section 7, computed per context | `REDISTRIBUTABLE` · `INTERNAL_USE_ONLY` · `USER_IMPORT_ONLY` · `LICENCE_PENDING` · `UNAVAILABLE` |
| **Origin** | `CURATED_IMPORT` · `FIRST_PARTY` (RiseWise-made, e.g. verified transcription of a public-domain edition) · `USER_SUPPLIED` |

Plus **Coverage** (explicit covered and missing locus ranges) and **reason codes** for anything not held:

| Reason code | Meaning |
|---|---|
| `NOT_ACQUIRED` | Not obtained yet |
| `LICENCE_RESTRICTED` | Restricted by licence |
| `NO_DIGITAL_TEXT` | Only print or scans exist |
| `NOT_EXTANT` | The work or part is lost |
| `NOT_PUBLISHED` | E.g. edition volumes never published |
| `UNKNOWN` | Not yet established |

**Derived display label** (first match wins):

| Label | Rule |
|---|---|
| `LICENCE_PENDING` | access = `LICENCE_PENDING` |
| `NOT_AVAILABLE` (+ reason) | holding = `NONE`, or access = `UNAVAILABLE` |
| `REFERENCE_ONLY` | holding = `METADATA_ONLY` — known and citable bibliographically, but no text held |
| `IMPORT_REQUIRED` | access = `USER_IMPORT_ONLY` and the user has not imported it |
| `SCAN_ONLY` | holding = `IMAGE_ONLY` |
| `PARTIAL` | holding = `PARTIAL_TEXT` |
| `AVAILABLE` | holding = `FULL_TEXT` |

`USER_SUPPLIED` is an **origin badge** shown next to any label, not a competing state.

**Availability ≠ reliability.** An `AVAILABLE` source can be low-authority or unverified. Labels never imply quality; authority and verification are shown separately.

**No-substitution rule (core verification rule).** When the requested Work, Edition, layer or recension isn't available, Tarka receives the availability label with its reason. It may not substitute: a translation for the original; a commentary for the root text; another recension; an unaccented text for an accented one; an unverified OCR text; a copy whose licence is unclear; or LLM recollection.

## 11. Vedic/Sanskrit Extension Model

The `vedic-sanskrit` extension **declares** structures. Values always come from sources and experts, never from this design. **Every scheme below is provisional** until confirmed by an expert (OQ-V01 … OQ-V06); scheme definitions are versioned so a correction is a new scheme version, not an architectural change.

**a) Work and tradition metadata (extension fields on Work):** `shakha` (recension), `vedaAffiliation`, `textGenre` (saṃhitā / brāhmaṇa / āraṇyaka / sūtra / vyākaraṇa / commentary …), `traditionalAttribution` vs `historicalAttribution` (kept separate).

**b) Citation schemes (provisional):**

| Scheme id | Levels | Notes |
|---|---|---|
| `rv.msr` | maṇḍala.sūkta.ṛc[.pāda] | |
| `rv.aas` | aṣṭaka.adhyāya.varga.ṛc | Alternative traditional division [K]; mapped to `rv.msr` (OQ-V02) |
| `ts.kpa` | kāṇḍa.prapāṭhaka.anuvāka[.further unit] | Lowest unit and its name follow the chosen edition [K] (OQ-V03) |
| `asht.aps` | adhyāya.pāda.sūtra | Aṣṭādhyāyī |
| `sk.num` | sūtra serial number | **Edition-specific**; numbering may differ between editions [K] (OQ-V04). Mapped to `asht.aps` by alignment |
| `commentary.local` | the commentary's own structure | plus `COMMENTARY_ON` locus links |

**c) Layer types** (each layer is its own Source with its own licence): `SAMHITA_PATHA` · `PADAPATHA` · (other recitation forms only if sources exist) · `TRANSLATION` · `COMMENTARY` · `SUB_COMMENTARY` · `ANNOTATION_MORPHOLOGY` · `ANNOTATION_METRE` · `ANNOTATION_DERIVATION`.

**d) Text representation rules.** Original script and encoding stored exactly (Devanāgarī, IAST, SLP1 …). Display forms derived through a **verified round-trip** transliteration (`ENCODING_ROUNDTRIP`). **Accents are part of the text, never an annotation.** An `accentProfile` on the passage records `accented: true | false | unknown`, `accentSystem` (as encoded by the source), and whether accents were verified. Normalisation profiles are versioned and may strip accents *for search keys only*.

**e) Annotation schemas.** `morph` (lemma, grammatical categories, token span) · `sandhi` (split points) · `derivation` (sequence of sūtra loci applied; usually tool-produced → origin `TOOL`, inference until verified) · `metre` (metre name, pāda structure) · `accentAnalysis` (optional analytical layer, separate from the accent marks in the text).

**f) Grammar-specific relations** (each sourced, never asserted by RiseWise): `ANUVRTTI_FROM` (sūtra → sūtra) · `ADHIKARA_SCOPE` (heading sūtra → range) · `SUTRA_TYPE` assignment (stored as an Interpretation attributed to a commentary or scholar, since classifications can be contested) · `CITES_SUTRA` (commentary passage → sūtra locus).

**g) Source roles / authority rubric** (configurable tiers, applied per purpose): `ROOT_TEXT_EDITION` · `TRADITIONAL_COMMENTARY` · `CRITICAL_SCHOLARSHIP` · `SECONDARY_SCHOLARSHIP` · `REFERENCE` · `TOOL_OUTPUT` · `USER_SUPPLIED` · `UNASSESSED`.

**h) Domain verification rules.** VR-101 a translation may not be cited as the root text · VR-102 a commentary statement is attributed to the commentator, not the root text · VR-103 accent preservation · VR-104 a padapāṭha may not be cited as the saṃhitā text · VR-105 recension must match the requested śākhā.

## 12. General-Domain Extension Model

| Element | Declaration |
|---|---|
| Work kinds | `DOCUMENT`, `ARTICLE`, `BOOK`, `REPORT`, `WEB_PAGE`, `DATASET`, `NOTE` |
| Citation schemes | `page.para`, `section.path`, `char.range` (fallback), `url.fragment` |
| Layers | `ORIGINAL`, `TRANSLATION`, `SUMMARY` — a summary is *derived*, never evidence; only the original can be quoted as evidence |
| Authority rubric | `PRIMARY_DOCUMENT`, `OFFICIAL`, `PEER_REVIEWED`, `REPUTABLE_SECONDARY`, `TERTIARY`, `USER_SUPPLIED`, `UNASSESSED` |
| Identifiers | DOI, ISBN, URL + capture hash |
| Rules | Web captures store URL, retrieval time and content hash; a changed page is a new snapshot |

Later domains reuse the core unchanged — **History** (primary/secondary roles; dating as attributed interpretation), **Law** (jurisdiction; effective dates as validity intervals; authority hierarchy), **Science** (study type; retraction status as a VerificationRecord), **Product/Business** (internal documents; recency weighting). Validity intervals and authority are therefore generic fields, not Vedic ones.

## 13–17. Worked examples

The five worked examples are maintained as metadata-only YAML (no corpus text):

| § | Example | File |
|---|---|---|
| 13 | Ṛgveda passage | [`01-rigveda-passage.yaml`](source-model-examples/01-rigveda-passage.yaml) |
| 14 | Taittirīya Saṃhitā passage | [`02-taittiriya-samhita-passage.yaml`](source-model-examples/02-taittiriya-samhita-passage.yaml) |
| 15 | Pāṇini rule | [`03-panini-rule.yaml`](source-model-examples/03-panini-rule.yaml) |
| 16 | External restricted source | [`04-external-restricted-source.yaml`](source-model-examples/04-external-restricted-source.yaml) |
| 17 | User-supplied source | [`05-user-supplied-source.yaml`](source-model-examples/05-user-supplied-source.yaml) |

Summary of what each demonstrates:

- **§13 Ṛgveda** — parallel layers (two saṃhitā versions, padapāṭha, morphology, translation, commentary) aligned to one locus, each a separate Source with its own licence; a translation whose underlying work and digital representation carry different licences; a commentary that is `SCAN_ONLY`; variant readings shown, never merged.
- **§14 Taittirīya Saṃhitā** — a multi-step derivation chain recorded as *unverified upstream claims*; upstream terms (TITUS) carried into effective rights; partial and never-published commentary coverage.
- **§15 Pāṇini rule** — a source with an informal licence and undocumented edition → `LICENCE_PENDING`, so no passage is evidence; commentary and sub-commentary chains; an edition-specific scheme (`sk.num`) aligned to `asht.aps`; grammar relations held as attributed interpretations; tool derivations not evidence-eligible.
- **§16 External restricted source** — `REFERENCE_ONLY` in the shared corpus; private user import only.
- **§17 User-supplied source** — user-attested licence (unverified), workspace-private, origin badge, promotion only through curator review.

## 18. What RiseWise Owns vs What It References

| RiseWise owns (first-party, licensable by RiseWise) | RiseWise references (third-party, governed by its licence) |
|---|---|
| The schema, identifiers, citation-scheme encodings, extension definitions | Third-party digital texts (VedaWeb, Sanskrit Library, DCS …) |
| Registry metadata it writes | Upstream provenance statements (stored as claims) |
| Provenance, verification and authority records | Licence texts (captured copies kept as evidence) |
| Alignments and locus mappings it creates | Translations and scholarship under copyright (reference only) |
| Corrections, as derivatives where the licence allows (share-alike respected) | Scans hosted elsewhere (linked, host terms recorded) |
| First-party annotations by its curators | Tool outputs (tool licence terms recorded) |
| **First-party digital editions**: verified transcriptions of public-domain printed editions | |

A first-party corpus is the long-term path to a redistributable source layer. **Caveat:** some jurisdictions protect scholarly/critical editions for a period (e.g. a special right for scientific editions in German law [K]); which editions are free to transcribe needs legal review per edition (OQ-L08).

## 19. Security & Integrity Considerations

- **Integrity** — SHA-256 for every file (manifest), passage and snapshot; hashes checked on read for evidence anchors. Provenance, licence and verification logs are append-only.
- **Safe import** — untrusted files are parsed without executing anything: XML external entities disabled, size/depth/archive-bomb limits, MIME checks. Unparseable files go to quarantine.
- **Unicode safety** — original preserved; invisible characters, bidi controls and confusables detected and flagged; normalisation never destructive. The raw original is the reference, so canonical reordering of combining marks (relevant to accents) cannot corrupt it (policy to be confirmed: OQ-E03).
- **Prompt injection** — all source text is untrusted data when shown to any LLM. It cannot change records. LLM output never writes to Passage, Text or LicenceRecord.
- **Rights enforcement** — the RightsDecision is checked at every exit point: API responses, exports, UI display, search snippets, embeddings, caches and **calls to external LLM or embedding services**. Derived artefacts (embeddings, indexes) inherit the restrictions of their source.
- **Tenant isolation** — user-supplied and internal-only content is scoped to its workspace and never enters shared indexes.
- **Tombstones** — purging content for licence reasons keeps hashes and metadata, so past results stay identifiable without showing restricted text.
- **Audit** — who acquired, approved, corrected, verified or changed a licence, and when.

## 20. Open Questions / Decisions Needed

Tracked with ids in [`../OPEN_QUESTIONS.md`](../OPEN_QUESTIONS.md):

1. Rights policy per tier (OQ-L01) · 2. External processors (OQ-L02) · 3. Excerpt limits (OQ-L03) · 4. Who may verify licences (OQ-L04) · 5. Citation conventions for `ts.kpa` and `sk.num` (OQ-V03, OQ-V04) · 6. Unicode policy for accents (OQ-E03) · 7. Licence for first-party corpus and annotations (OQ-L05) · 7a. Code licence (OQ-L06) · 8. Expert reviewer availability (OQ-P01) · 9. Identifier scheme (OQ-E01).

## 21. Recommended MVP Source Model

**In the MVP (12 entities + 2 value objects)**

| Entity | Purpose |
|---|---|
| Agent | People, organisations, tools, LLMs, users |
| Work | With `workKind` + extension fields |
| Edition | — |
| Source | Digital text / scan / print reference; layer type |
| Acquisition (+ embedded Manifest) | — |
| SourceSnapshot | Immutable, hashed |
| Passage | Text content + hash + accent profile + loci via PassageLocus |
| Locus + CitationScheme | Scheme defined by the extension |
| Relation | Typed, with provenance |
| Annotation | Generic; body schema per extension; origin + producer |
| LicenceRecord | Append-only revisions, evidence-backed |
| ProvenanceRecord | Upstream claims + RiseWise activities |
| VerificationRecord | — |
| AvailabilityRecord | Holding / origin / coverage / reason; access class computed |

- **Value objects:** `EvidenceAnchor`, `Citation`.
- **Computed, not stored:** effective rights, RightsDecision, access class per context, display label.
- **Deferred:** `AuthorityAssessment` (a simple tier field on Source at first), `Interpretation` (arrives with Tarka), `CorpusState` (needed at the first reasoning run; design kept), correction workflows, variant-set computation, metadata revision UI.

---

## 22. Paper Test

**Purpose:** show that the model cannot accidentally treat unavailable, unverified or restricted material as trustworthy evidence. Each case traces the records the model would hold and the gate that decides evidence eligibility.

**Evidence-eligibility gate (as defined above).** A passage may back an `EvidenceAnchor` only if **all** hold:

| # | Condition | Defined in |
|---|---|---|
| G1 | The passage text is held (`contentState: STORED`) and its hash re-verifies (`INTEGRITY_HASH` pass) | §3, §8 |
| G2 | The effective access class in the current use context is not `LICENCE_PENDING` or `UNAVAILABLE`, and the RightsDecision allows the intended use | §7 |
| G3 | The workspace is allowed to see it (tenant isolation for user-supplied / internal content) | §19 |
| G4 | The passage comes from a Source whose layer matches what is being claimed (no-substitution rule; VR-101/102/104/105) | §10, §11 |
| G5 | The passage/annotation `origin` is not `LLM` | P7 |

Passing the gate makes a passage *usable*, not *authoritative*: authority (§8) and verification level (§8) are still reported alongside it, and claim status remains Tarka's decision.

### Case 1 — A fully available public-domain source

*Hypothetical* (no such source has been created yet): RiseWise produces a first-party transcription of a public-domain printed edition and collates it against the scan. See [`06-paper-test-public-domain.yaml`](source-model-examples/06-paper-test-public-domain.yaml).

- Records: Work, Edition (public domain), Source (`origin: FIRST_PARTY`), Snapshot, Passages; LicenceRecords: Work `PUBLIC_DOMAIN` (`LEGAL_REVIEWED` per OQ-L08), Source `<RiseWise first-party licence>` (OQ-L05).
- Availability: holding `FULL_TEXT`, access `REDISTRIBUTABLE` in all contexts → label `AVAILABLE`.
- Gate: G1–G5 pass → **usable as evidence.**
- Guard: verification state is reported separately (e.g. `HUMAN_VERIFIED` for collated sections, `INTEGRITY_CHECKED` for the rest). "Available + public domain" does not imply "accurate" or "authoritative".

### Case 2 — A copyrighted source RiseWise cannot redistribute

See [`04-external-restricted-source.yaml`](source-model-examples/04-external-restricted-source.yaml).

- Records: Work (`TRANSLATION_OF` target), Edition (bibliographic), Source `kind: PRINT_REFERENCE`, LicenceRecord `ALL_RIGHTS_RESERVED`.
- Availability: holding `METADATA_ONLY`, access `UNAVAILABLE` (shared corpus) → label `REFERENCE_ONLY`. No snapshot, no passages.
- Gate: **G1 fails** (no text) → **cannot be evidence** in the shared corpus. It can appear only as a bibliographic pointer.
- If a user imports their own licensed copy: a separate private Source (`origin: USER_SUPPLIED`) in that workspace, `INTERNAL_USE_ONLY` there; G3 confines it to that workspace; it is never redistributed or sent to external processors without rights. The shared reference record stays `REFERENCE_ONLY`.

### Case 3 — A source with uncertain licence

See [`03-panini-rule.yaml`](source-model-examples/03-panini-rule.yaml) (ashtadhyayi.com data).

- LicenceRecord: `CUSTOM`, terms "free to use … with appropriate credits" [V]; `commercial: UNKNOWN`, `redistribution: UNKNOWN` (upstream edition rights undocumented).
- Effective rights: any `UNKNOWN` ⇒ access `LICENCE_PENDING` in **every** use context → label `LICENCE_PENDING`.
- Lifecycle: stops at `RIGHTS_REVIEW`; no acquisition is approved, so no passages exist. Even if content had been obtained earlier, **G2 fails** → **cannot be evidence.**
- Tarka would receive `LICENCE_PENDING` and, by the no-substitution rule, may not fall back to an unverified copy elsewhere or to LLM recollection of the sūtra; the honest outcome is insufficient evidence for claims that depend on it.

### Case 4 — A user-uploaded private source

See [`05-user-supplied-source.yaml`](source-model-examples/05-user-supplied-source.yaml).

- Records: Source `origin: USER_SUPPLIED`, scoped to the uploader's workspace; Acquisition `USER_UPLOAD`; LicenceRecord as declared by the user, `verificationStatus: UNVERIFIED`, evidence = user attestation.
- Availability: label per holding (e.g. `AVAILABLE`) **plus** a mandatory `User-supplied` origin badge; access `INTERNAL_USE_ONLY` in that workspace.
- Gate: G1, G2 (for the user's own workspace and local use), G4, G5 can pass; **G3 restricts it to that workspace** → usable as evidence *only there*, always labelled user-supplied, authority `UNASSESSED`, verification `INTEGRITY_CHECKED` at most.
- Guard: it is never visible to other workspaces, never redistributed, not sent to external processors without explicit user consent, and enters the shared corpus only through curator licence review as a new `CURATED_IMPORT` acquisition.

### Case 5 — Two editions that disagree at the same locus

*Hypothetical* disagreement (no claim is made that any real editions differ at any particular locus). See [`07-paper-test-edition-disagreement.yaml`](source-model-examples/07-paper-test-edition-disagreement.yaml).

- Records: one Work, two Editions, two Sources, two Snapshots; Passage A and Passage B both map to locus `<L>` with different `contentHash` values (after the same normalisation profile).
- The model keeps **both** passages. Nothing merges them; there is no "canonical text" field on Locus (Locus holds no text).
- A citation must name the specific edition/snapshot; an EvidenceAnchor binds to *one* passage and its hash.
- Any preference between the editions is an `AuthorityAssessment` (attributed, with rationale, per purpose) — not an overwrite.
- Tarka (later) sees both readings; when the claim depends on the differing wording, the reasoning layer must surface the disagreement (e.g. `CONTESTED`), not silently pick one.
- Gate: both passages may individually pass G1–G5; the disagreement is preserved as information, not hidden.

### Paper-test result

| Case | Label | Evidence-eligible? | Blocking gate |
|---|---|---|---|
| 1 Public domain, first-party | `AVAILABLE` | Yes (verification level shown separately) | — |
| 2 Copyrighted, non-redistributable | `REFERENCE_ONLY` | No (shared); private import only in its workspace | G1 (shared), G3 (private) |
| 3 Uncertain licence | `LICENCE_PENDING` | No | G2 |
| 4 User-uploaded private | e.g. `AVAILABLE` + `User-supplied` badge | Only in owner's workspace, labelled | G3 |
| 5 Editions disagree | `AVAILABLE` (each) | Yes, each separately; disagreement preserved | — (P5 no-merge) |

In none of the five cases does unavailable, unverified-licence or restricted material become usable shared evidence, and in no case is LLM output admitted (G5).
