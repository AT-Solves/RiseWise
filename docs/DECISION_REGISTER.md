# RiseWise Decision Register

## About this register

**Why it exists.** This is the long-term memory of RiseWise. It records important architectural, product, business, legal/licensing, scholarly, security, privacy, data, research and operational decisions, plus unresolved concerns, temporary assumptions, deviations, risks and review points, so that none are lost across conversations, ADRs, commits, conflicts or open-question documents.

**How it relates to other documents.** The register is the central **index and history**. It does not replace the detailed documents, which remain the source of truth:

| Document | Holds |
|---|---|
| [`architecture/decisions/`](architecture/decisions/README.md) (ADRs) | Detailed architectural decisions |
| [`CONFLICTS.md`](CONFLICTS.md) | Discovered conflicts between requirements, designs or sources |
| [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) | Unresolved questions |
| [`PRODUCT_REQUIREMENTS.md`](PRODUCT_REQUIREMENTS.md) | Product requirements (approved / provisional / open) |
| [`architecture/source-model.md`](architecture/source-model.md) | The approved Knowledge Source Model |
| **This register** | One entry per decision/finding: its status, significance, limits and review trigger, linking to the above |

**Create a new entry when work discovers:** a legal or licensing uncertainty · a scholarly uncertainty · a security or privacy concern · a deviation from approved architecture · a temporary assumption · a product decision with long-term consequences · a conflict between sources · an intentionally deferred decision · a decision that needs expert review · a decision that could invalidate previous work · a situation where "we don't know" is itself an important finding.

**Update an existing entry when:** its status changes; a reviewer responds; a related ADR, conflict or open question is added, resolved or superseded; its revisit trigger occurs; or new evidence changes its significance. Never delete an entry — mark it `SUPERSEDED`, `REJECTED` or `RESOLVED` and add a dated note.

**Rules**

- **This is a project governance record, not legal advice.** `APPROVED` means approved by the product owner as RiseWise policy or design. It does **not** mean legally, scholarly or security verified.
- **Unresolved items must never be silently treated as approved.** `OPEN`, `PROPOSED`, `REVIEW_REQUIRED`, `BLOCKED` and `TEMPORARY` entries may not be relied on as settled.
- `REVIEW_REQUIRED` is used whenever expert, legal, scholarly, security or other specialist review is still needed.
- Keep entries short; put detail in the linked document.

**Classifications:** `ARCHITECTURE` `TECHNICAL` `PRODUCT` `BUSINESS` `LEGAL` `LICENSING` `SCHOLARLY` `SECURITY` `PRIVACY` `DATA` `RESEARCH` `OPERATIONAL` `OTHER`

**Statuses:** `PROPOSED` `APPROVED` `OPEN` `BLOCKED` `REVIEW_REQUIRED` `TEMPORARY` `SUPERSEDED` `REJECTED` `RESOLVED`

**Entry format:** each entry lists ID, date, classification and status in its header line, then: Decision / finding · Why it matters · Sources · Related · Allowed · Not allowed · Risk if ignored · Revisit if · Reviewer · Review trigger.

**"Session"** in *Sources* means the decision originated in a Claude Code session; such product decisions are now recorded in [`PRODUCT_REQUIREMENTS.md`](PRODUCT_REQUIREMENTS.md) (DR-006).

---

## Status summary

Verified against the entries below (66 entries; every entry appears exactly once in the index).

| Status | Count | Entries |
|---|---|---|
| APPROVED | 34 | DR-001, DR-002, DR-003, DR-004, DR-005, DR-007, DR-011, DR-012, DR-013, DR-014, DR-015, DR-016, DR-017, DR-018, DR-019, DR-020, DR-021, DR-022, DR-023, DR-024, DR-025, DR-026, DR-027, DR-028, DR-052, DR-053, DR-054, DR-055, DR-056, DR-057, DR-060, DR-061, DR-062, DR-063 |
| OPEN | 13 | DR-009, DR-010, DR-032, DR-041, DR-042, DR-043, DR-047, DR-048, DR-049, DR-058, DR-064, DR-065, DR-066 |
| REVIEW_REQUIRED | 14 | DR-030, DR-031, DR-034, DR-035, DR-036, DR-037, DR-038, DR-039, DR-040, DR-044, DR-045, DR-046, DR-050, DR-051 |
| BLOCKED | 1 | DR-033 |
| TEMPORARY | 1 | DR-029 |
| PROPOSED | 1 | DR-008 |
| RESOLVED | 2 | DR-006, DR-059 |
| SUPERSEDED | 0 | — |
| REJECTED | 0 | — |
| **Total** | **66** | |

## Index

| ID | Topic | Classification | Status |
|---|---|---|---|
| DR-001 | RiseWise platform definition | PRODUCT, ARCHITECTURE | APPROVED |
| DR-002 | Tarka is structured reasoning, not a chatbot | PRODUCT | APPROVED |
| DR-003 | LLM statements never automatically facts; status from evidence and rules | PRODUCT, ARCHITECTURE | APPROVED |
| DR-004 | MVP domains: GENERAL and VEDIC_SANSKRIT | PRODUCT | APPROVED |
| DR-005 | Greenfield implementation; v0.1–v0.3 are product history only | PRODUCT, RESEARCH | APPROVED |
| DR-006 | Product requirements not yet recorded in the repository | PRODUCT, OPERATIONAL | RESOLVED |
| DR-007 | Documentation-first, approval-gated delivery | OPERATIONAL | APPROVED |
| DR-008 | Proposed technical defaults (stack, excluding schema technology) | TECHNICAL | PROPOSED |
| DR-009 | Deployment target and cloud LLM provider | PRODUCT, PRIVACY, TECHNICAL | OPEN |
| DR-010 | Commercial intent and tiers | BUSINESS, LICENSING | OPEN |
| DR-011 | Work → Edition → Source → SourceSnapshot → Passage | ARCHITECTURE, DATA | APPROVED |
| DR-012 | Locus separate from Passage | ARCHITECTURE, DATA | APPROVED |
| DR-013 | Translations and commentaries are separate works | ARCHITECTURE, SCHOLARLY | APPROVED |
| DR-014 | Immutable, content-addressed snapshots | ARCHITECTURE, DATA | APPROVED |
| DR-015 | Original text preserved where legally permitted | ARCHITECTURE, DATA, LICENSING | APPROVED |
| DR-016 | Provenance, licence, verification, authority, availability kept separate | ARCHITECTURE | APPROVED |
| DR-017 | LLM output is never a source | ARCHITECTURE, PRODUCT | APPROVED |
| DR-018 | No silent merging of editions | ARCHITECTURE, SCHOLARLY | APPROVED |
| DR-019 | No substitution for requested source material | ARCHITECTURE, SCHOLARLY | APPROVED |
| DR-020 | Domain specifics via extensions; extension content provisional | ARCHITECTURE | APPROVED |
| DR-021 | Availability dimensions with derived labels | ARCHITECTURE, DATA | APPROVED |
| DR-022 | Evidence-eligibility gate (G1–G5) | ARCHITECTURE | APPROVED |
| DR-023 | Source-layer security controls | SECURITY | APPROVED |
| DR-024 | Workspace isolation of private and internal content | PRIVACY, SECURITY | APPROVED |
| DR-025 | Rights evaluated per use context | LICENSING, ARCHITECTURE | APPROVED |
| DR-026 | Silence in a licence is not permission | LICENSING | APPROVED |
| DR-027 | Unknown rights block shared/public evidence | LICENSING | APPROVED |
| DR-028 | Private USER_SUPPLIED pathway | LICENSING, PRIVACY, PRODUCT | APPROVED |
| DR-029 | Conservative default for NC / scholarly-only material | LICENSING | TEMPORARY |
| DR-030 | Rights policy per tier, required uses, excerpt limits | LEGAL, LICENSING, BUSINESS | REVIEW_REQUIRED |
| DR-031 | Sending non-open text to external processors | LEGAL, LICENSING, PRIVACY | REVIEW_REQUIRED |
| DR-032 | Who may verify licences | LICENSING, OPERATIONAL | OPEN |
| DR-033 | Current third-party Vedic examples are LICENCE_PENDING | LICENSING, DATA | BLOCKED |
| DR-034 | VedaWeb licensing chain | LICENSING | REVIEW_REQUIRED |
| DR-035 | Sanskrit Library / TITUS licensing relationship | LICENSING | REVIEW_REQUIRED |
| DR-036 | DCS licence discrepancy and upstream editions | LICENSING | REVIEW_REQUIRED |
| DR-037 | ashtadhyayi.com permission and provenance | LICENSING, SCHOLARLY | REVIEW_REQUIRED |
| DR-038 | GRETIL per-file licences | LICENSING | REVIEW_REQUIRED |
| DR-039 | Ambuda licence metadata and coverage | LICENSING, DATA | REVIEW_REQUIRED |
| DR-040 | Tool and dictionary licences (Vidyut, Heritage, Cologne) | LICENSING | REVIEW_REQUIRED |
| DR-041 | Owner of permission correspondence | OPERATIONAL, LICENSING | OPEN |
| DR-042 | Code licence | LICENSING, BUSINESS | OPEN |
| DR-043 | First-party corpus strategy and licence | PRODUCT, DATA, LICENSING | OPEN |
| DR-044 | Edition rights for public-domain transcription | LEGAL | REVIEW_REQUIRED |
| DR-045 | Vedic citation conventions not frozen | SCHOLARLY | REVIEW_REQUIRED |
| DR-046 | Unverified Vedic bibliographic and encoding facts | SCHOLARLY, RESEARCH | REVIEW_REQUIRED |
| DR-047 | Traditional commentaries largely unavailable as verified text | DATA, SCHOLARLY | OPEN |
| DR-048 | Expert reviewer availability | SCHOLARLY, OPERATIONAL | OPEN |
| DR-049 | Vedic authority rubric | SCHOLARLY | OPEN |
| DR-050 | Corpus research was partly indirect | RESEARCH | REVIEW_REQUIRED |
| DR-051 | Vedic Unicode and accent handling | TECHNICAL, SCHOLARLY | REVIEW_REQUIRED |
| DR-052 | Evidence span offsets | TECHNICAL, DATA | APPROVED |
| DR-053 | Citation-scheme scope and locus mappings | TECHNICAL, DATA | APPROVED |
| DR-054 | Identifier scheme | TECHNICAL | APPROVED |
| DR-055 | SourceSnapshot granularity | TECHNICAL, DATA | APPROVED |
| DR-056 | Annotation alignment | TECHNICAL, DATA | APPROVED |
| DR-057 | ROOT_TEXT designation | TECHNICAL, DATA, SCHOLARLY | APPROVED |
| DR-058 | "EVIDENCE" as epistemic kind and as entity | PRODUCT, ARCHITECTURE | OPEN |
| DR-059 | Terminology: Source, Manifest, Version | ARCHITECTURE | RESOLVED |
| DR-060 | Target user, primary job and MVP specialization | PRODUCT | APPROVED |
| DR-061 | GENERAL domain | PRODUCT, ARCHITECTURE | APPROVED |
| DR-062 | Schema technology: TypeScript + Zod (only) | TECHNICAL, ARCHITECTURE | APPROVED |
| DR-063 | Python prototype retired as the core implementation path | TECHNICAL, ARCHITECTURE | APPROVED |
| DR-064 | Passage granularity and cross-passage spans | TECHNICAL, DATA | OPEN |
| DR-065 | Evidence eligibility of human-curated annotation datasets | TECHNICAL, DATA, SCHOLARLY | OPEN |
| DR-066 | Layer type for non-Vedic base texts | TECHNICAL, DATA | OPEN |

---

## Product and project foundation

### DR-001 — RiseWise platform definition
`PRODUCT` `ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** RiseWise is a provenance-first knowledge, research and reasoning platform. Pillars: Tarka Core, Knowledge Layer, Evidence & Provenance, Domain Adapters, Evaluation, Research Workspace, Administration/Governance.
- **Why:** Defines scope; every later design must serve provenance-first knowledge work.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) (session origin); [source-model.md](architecture/source-model.md) §1 · **Related:** DR-002, DR-006
- **Allowed:** knowledge, research and reasoning features that preserve provenance · **Not allowed:** features that present untraceable output as knowledge
- **Risk if ignored:** drift into a generic chatbot product
- **Revisit if:** product owner changes the positioning
- **Reviewer:** — · **Review trigger:** —

### DR-002 — Tarka is structured reasoning, not a chatbot
`PRODUCT` · **APPROVED** · 2026-10-26
- **Decision:** Tarka examines questions through Question → Claims → Definitions → Evidence → Sources → Arguments → Counterarguments → Assumptions → Inferences → Contradictions → Uncertainty → Conclusion → Provenance. Users must see what Tarka thinks, why, supporting and contradicting evidence, assumptions, known vs inferred, and uncertainty. "Why?" and "Challenge this conclusion" are required; challenge must not manufacture artificial balance.
- **Why:** Core product identity; drives the reasoning model and UI.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) (session origin) · **Related:** DR-003, DR-058
- **Allowed:** structured, explainable reasoning outputs · **Not allowed:** free-form chat answers presented as conclusions; invented counterarguments
- **Risk if ignored:** unexplainable conclusions
- **Revisit if:** Tarka design begins (requirements must be recorded first, DR-006)
- **Reviewer:** — · **Review trigger:** start of Tarka design

### DR-003 — LLM statements are never automatically facts; status comes from evidence and rules
`PRODUCT` `ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** Epistemic kinds FACT, EVIDENCE, INFERENCE, ASSUMPTION, INTERPRETATION, UNCERTAINTY and statuses SUPPORTED, PARTIALLY_SUPPORTED, CONTRADICTED, CONTESTED, UNVERIFIED, INSUFFICIENT_EVIDENCE, INFERRED. Evidence and verification rules determine a claim's status; the LLM does not.
- **Why:** The central trust principle of RiseWise.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) (session origin); [source-model.md](architecture/source-model.md) §3 · **Related:** DR-017, DR-058, [C-002](CONFLICTS.md)
- **Allowed:** LLMs proposing candidate claims, labelled UNVERIFIED · **Not allowed:** any model or person setting a status directly
- **Risk if ignored:** hallucinations presented as established facts
- **Revisit if:** never relaxed without product-owner decision
- **Reviewer:** — · **Review trigger:** —

### DR-004 — MVP domains: GENERAL and VEDIC_SANSKRIT
`PRODUCT` · **APPROVED** · 2026-10-26
- **Decision:** The first two domains are GENERAL and VEDIC_SANSKRIT (Pāṇini, Aṣṭādhyāyī, Siddhānta Kaumudī, Vedic Sanskrit, Ṛgveda, Kṛṣṇa Yajurveda / Taittirīya Saṃhitā, linguistic analysis, commentary, translation, scholarly interpretation). Product/Business, History, Science and Law come later.
- **Why:** Bounds MVP scope while keeping the core domain-neutral.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) (session origin); [source-model.md](architecture/source-model.md) §11–12 · **Related:** DR-020
- **Allowed:** core work that serves both domains · **Not allowed:** building other domain adapters in the MVP
- **Risk if ignored:** scope explosion
- **Revisit if:** MVP is complete or product priorities change
- **Reviewer:** — · **Review trigger:** end of MVP

### DR-005 — Greenfield implementation; v0.1–v0.3 are product history only
`PRODUCT` `RESEARCH` · **APPROVED** · 2026-10-26
- **Decision / finding:** The repository contained no earlier implementation (only a README). RiseWise v0.1 (TypeScript demo, no database), v0.2 (14/14 eval checks) and v0.3 (verification rules, source-record fields, 31/31 checks) are treated as requirements history, not code to preserve. The v0.3 check list and field list are **not available**.
- **Why:** Prevents claims of compatibility with code that does not exist; v0.3 artefacts were re-proposed, not recovered.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) PR-004 (session audit) · **Related:** DR-006
- **Allowed:** fresh design informed by the history · **Not allowed:** claiming to reproduce v0.3 behaviour or checks
- **Risk if ignored:** false continuity claims
- **Revisit if:** the v0.3 code, 31 checks or field list are found — then map to them
- **Reviewer:** product owner · **Review trigger:** if v0.3 artefacts surface
- **Correction (2026-10-26):** The statement that the repository contained no earlier implementation was based on the repository state visible to the governance work at the time (`main` at the initial commit `22ffae5`). It is incorrect: the `main` history contains an earlier Python prototype (commits `7d3199a`, `41713d5`, `fa1c324`, `cb43582`). That prototype is now formally recorded as historical and retired as the core path by [ADR-0014](architecture/decisions/0014-retire-python-prototype-as-core-implementation.md) / DR-063. No historical implementation work should be treated as nonexistent.

### DR-006 — Product requirements are not yet recorded in the repository
`PRODUCT` `OPERATIONAL` · **RESOLVED** · 2026-10-26
- **Resolution (2026-10-26):** recorded in [`PRODUCT_REQUIREMENTS.md`](PRODUCT_REQUIREMENTS.md) v0.1, each item classified APPROVED / PROVISIONAL / OPEN with its session source.
- **Finding:** DR-001–DR-005, DR-008 and DR-009 existed only in Claude session history. The repository has no `docs/product/` requirements document; `source-model.md` covers the source layer only.
- **Why:** Sessions are not durable project memory; later work could lose or misremember requirements.
- **Sources:** this register · **Related:** DR-001–DR-005, DR-008, DR-009
- **Allowed:** relying on this register's summaries meanwhile · **Not allowed:** treating unrecorded session statements as detailed specifications
- **Risk if ignored:** requirements drift; schema built on unrecorded assumptions
- **Revisit if:** product requirements documents are created
- **Reviewer:** product owner · **Review trigger:** before Tarka design; ideally before schema design

### DR-007 — Documentation-first, approval-gated delivery
`OPERATIONAL` · **APPROVED** · 2026-10-26
- **Decision:** Work proceeds step by step; each step stops for product-owner review. No schema, database, importers, corpus downloads, Tarka, LLM integration, embeddings, UI, auth/tiers or billing until explicitly approved.
- **Why:** Gets the foundation right before code depends on it.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) (session origin); [source-model.md](architecture/source-model.md) §21 · **Related:** DR-008
- **Allowed:** documentation and design · **Not allowed:** starting the next step without approval
- **Risk if ignored:** rework on unapproved foundations
- **Revisit if:** product owner changes the delivery mode
- **Reviewer:** product owner · **Review trigger:** each step

### DR-008 — Proposed technical defaults
`TECHNICAL` · **PROPOSED** · 2026-10-26
- **Proposal:** TypeScript monorepo (pnpm); React + Vite SPA; Fastify API; Zod schemas; SQLite by default with Postgres for teams (both tested in CI); Ollama as default LLM provider plus a Fake provider for tests; qualitative confidence bands; no open-web retrieval in MVP; Python NLP tools only as a later sidecar.
- **Why:** These were offered as "defaults unless you object" in architecture proposal rev. 2 and have **not** been explicitly approved.
- **Update (2026-10-26):** TypeScript + Zod for domain models and validation schemas was approved separately (DR-062, ADR-0013). Everything else in this entry remains PROPOSED.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) PR-172 (session origin: architecture proposal rev. 2) · **Related:** DR-009, DR-054
- **Allowed:** discussing them as proposals · **Not allowed:** treating them as approved
- **Risk if ignored:** schema written in an unapproved stack
- **Revisit if:** product owner approves or changes them
- **Reviewer:** product owner · **Review trigger:** before schema design

### DR-009 — Deployment target and cloud LLM provider
`PRODUCT` `PRIVACY` `TECHNICAL` · **OPEN** · 2026-10-26
- **Question:** MVP local-only vs. hosted demo; whether any cloud LLM provider is allowed and which (architecture proposal rev. 2, decisions D2/D3). Recommendation was local-only, Ollama by default, one opt-in cloud provider.
- **Why:** Affects auth scope, data egress and external-processing rights.
- **Sources:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) (session origin) · **Related:** DR-031, DR-010
- **Allowed:** — · **Not allowed:** sending any content to a cloud provider before decision
- **Risk if ignored:** unplanned data egress
- **Revisit if:** decided
- **Reviewer:** product owner · **Review trigger:** before LLM integration

### DR-010 — Commercial intent and tiers
`BUSINESS` `LICENSING` · **OPEN** · 2026-10-26
- **Question:** Whether and when RiseWise offers free, paid professional and enterprise tiers. The model is designed to support them; no commitment has been made.
- **Why:** Determines how NC / scholarly-only material can be used (DR-030).
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-P02 · **Related:** DR-029, DR-030
- **Allowed:** designing for multiple contexts · **Not allowed:** assuming commercial use of NC material
- **Risk if ignored:** licence breaches in a paid tier
- **Revisit if:** business plan is set
- **Reviewer:** product owner · **Review trigger:** before any hosted or paid offering

## Source model architecture

### DR-011 — Work → Edition → Source → SourceSnapshot → Passage
`ARCHITECTURE` `DATA` · **APPROVED** · 2026-10-26
- **Decision:** Five distinct levels; Acquisition/Manifest records how snapshots were obtained.
- **Why:** Exact provenance requires never collapsing work, printing, digital file, version and text.
- **Sources:** [ADR-0001](architecture/decisions/0001-work-edition-source-snapshot-passage.md) · **Related:** DR-012, DR-014
- **Allowed:** 0..* cardinalities (known work without edition/source) · **Not allowed:** a flat "document" model
- **Risk if ignored:** ambiguous citations
- **Revisit if:** schema design proves a level redundant (requires new ADR)
- **Reviewer:** — · **Review trigger:** schema design

### DR-012 — Locus is separate from Passage
`ARCHITECTURE` `DATA` · **APPROVED** · 2026-10-26
- **Decision:** A Locus is an address and holds no text; passages map to loci (EXACT / PARTIAL / SPLIT / MERGED).
- **Why:** Editions, translations and commentaries align without being merged.
- **Sources:** [ADR-0002](architecture/decisions/0002-locus-distinct-from-passage.md) · **Related:** DR-053
- **Allowed:** edition-specific schemes · **Not allowed:** storing text on a Locus
- **Risk if ignored:** lost variants
- **Revisit if:** DR-053 decisions require amendment
- **Reviewer:** — · **Review trigger:** schema design

### DR-013 — Translations and commentaries are separate works; commentary ≠ interpretation
`ARCHITECTURE` `SCHOLARLY` · **APPROVED** · 2026-10-26
- **Decision:** `TRANSLATION_OF` / `COMMENTARY_ON` relations between Works; Interpretation is an attributed, anchored reading (deferred to Tarka phase).
- **Why:** The model cannot cite a translation or commentary as the original.
- **Sources:** [ADR-0003](architecture/decisions/0003-translations-commentaries-are-separate-works.md) · **Related:** DR-019
- **Allowed:** sub-commentary chains · **Not allowed:** labelling translation/commentary passages as root text
- **Risk if ignored:** misattributed scholarship
- **Revisit if:** never without new ADR
- **Reviewer:** — · **Review trigger:** —

### DR-014 — Immutable, content-addressed snapshots
`ARCHITECTURE` `DATA` · **APPROVED** · 2026-10-26
- **Decision:** Snapshots, passages and annotations are immutable and SHA-256 hashed; reasoning cites passage id + hash + CorpusState; corrections are new snapshots; purges leave tombstones.
- **Why:** Reproducibility of reasoning results.
- **Sources:** [ADR-0004](architecture/decisions/0004-immutable-content-addressed-snapshots.md) · **Related:** DR-052
- **Allowed:** append-only revisions · **Not allowed:** in-place edits of cited content
- **Risk if ignored:** irreproducible results
- **Revisit if:** storage cost becomes prohibitive
- **Reviewer:** — · **Review trigger:** —

### DR-015 — Original text preserved where legally permitted
`ARCHITECTURE` `DATA` `LICENSING` · **APPROVED** · 2026-10-26
- **Decision:** Text stored exactly as received where the licence allows; normalisations are additive; accents are text; hash-only passages where storage is not allowed.
- **Why:** No silent loss of script, encoding or accent information.
- **Sources:** [ADR-0005](architecture/decisions/0005-preserve-original-text.md) · **Related:** DR-051
- **Allowed:** derived search/display forms · **Not allowed:** replacing the original; storing text without storage rights
- **Risk if ignored:** corrupted Vedic texts
- **Revisit if:** DR-051 is decided
- **Reviewer:** — · **Review trigger:** —
- **Amendment (2026-10-27):** "Exactly as received" applies to the acquired bytes (preserved and hashed); Passage `original` is the faithful decoded Unicode text, decoding recorded, undecodable material quarantined ([ADR-0021](architecture/decisions/0021-acquired-bytes-and-decoded-passage-text.md)).

### DR-016 — Provenance, licence, verification, authority and availability are separate
`ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** Five separate record types with separate histories; upstream provenance stored as claims; authority never inferred from popularity; licence evidence separate from provenance and verification.
- **Why:** Each answers a different question; conflation hides risk.
- **Sources:** [ADR-0008](architecture/decisions/0008-separate-provenance-authority-verification-licence-availability.md) · **Related:** DR-021, DR-025
- **Allowed:** showing all five independently · **Not allowed:** deriving one from another
- **Risk if ignored:** "we know where it came from" mistaken for "we may use it" or "it is reliable"
- **Revisit if:** never without new ADR
- **Reviewer:** — · **Review trigger:** —

### DR-017 — LLM output is never a source
`ARCHITECTURE` `PRODUCT` · **APPROVED** · 2026-10-26
- **Decision:** LLM output never becomes source content; LLM annotations/interpretations carry `origin: LLM` and are excluded as evidence; tool output is not evidence until verified.
- **Why:** Enforces DR-003 at the data layer.
- **Sources:** [ADR-0009](architecture/decisions/0009-llm-output-is-never-a-source.md) · **Related:** DR-003, DR-022
- **Allowed:** LLM-proposed items, labelled and excluded · **Not allowed:** LLM recollection as a substitute source
- **Risk if ignored:** fabricated evidence
- **Revisit if:** never
- **Reviewer:** — · **Review trigger:** —

### DR-018 — No silent merging of editions
`ARCHITECTURE` `SCHOLARLY` · **APPROVED** · 2026-10-26
- **Decision:** Disagreeing passages at a locus are kept side by side; preferences are attributed AuthorityAssessments.
- **Why:** Edition differences are scholarly information.
- **Sources:** [ADR-0010](architecture/decisions/0010-no-silent-merging-no-substitution.md); [source-model.md](architecture/source-model.md) §22 case 5 · **Related:** DR-019
- **Allowed:** recorded preferences · **Not allowed:** canonical-text overwrite
- **Risk if ignored:** hidden variants
- **Revisit if:** never without new ADR
- **Reviewer:** — · **Review trigger:** —

### DR-019 — No substitution for requested source material
`ARCHITECTURE` `SCHOLARLY` · **APPROVED** · 2026-10-26
- **Decision:** When a requested work/edition/layer/recension is unavailable, the label and reason are passed on; no translation, commentary, other recension, unaccented text, unverified OCR, unclear-licence copy or LLM recollection may substitute.
- **Why:** Honest absence over confident substitution.
- **Sources:** [ADR-0010](architecture/decisions/0010-no-silent-merging-no-substitution.md) · **Related:** DR-013, DR-017
- **Allowed:** INSUFFICIENT_EVIDENCE outcomes · **Not allowed:** any substitution listed above
- **Risk if ignored:** misleading answers
- **Revisit if:** never without new ADR
- **Reviewer:** — · **Review trigger:** —

### DR-020 — Domain specifics via extensions; extension content is provisional
`ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** Core entities are domain-neutral; extensions declare schemes, layers, annotation schemas, rubrics, rules. Vedic schemes and layer names are provisional data, not architecture.
- **Why:** Multi-domain future; prevents uncertain scholarship from becoming architecture.
- **Sources:** [ADR-0011](architecture/decisions/0011-domain-specifics-via-extensions.md) · **Related:** DR-045, DR-057
- **Allowed:** versioned extension changes · **Not allowed:** Vedic structures in core entities
- **Risk if ignored:** core locked to one domain
- **Revisit if:** a domain cannot be expressed as an extension
- **Reviewer:** — · **Review trigger:** —

### DR-021 — Availability dimensions with derived labels
`ARCHITECTURE` `DATA` · **APPROVED** · 2026-10-26
- **Decision:** Store holding, origin, coverage and reason codes; compute access class per context; derive labels (LICENCE_PENDING, NOT_AVAILABLE, REFERENCE_ONLY, IMPORT_REQUIRED, SCAN_ONLY, PARTIAL, AVAILABLE); USER_SUPPLIED is an origin badge. Availability ≠ reliability.
- **Why:** "We don't have this source" represented honestly, with reasons.
- **Sources:** [ADR-0007](architecture/decisions/0007-access-classes-and-availability-dimensions.md); [C-001](CONFLICTS.md) (resolved) · **Related:** DR-016
- **Allowed:** new derived labels without migration · **Not allowed:** implying quality from availability
- **Risk if ignored:** false "available" signals
- **Revisit if:** UI research shows labels confuse users
- **Reviewer:** — · **Review trigger:** UI design

### DR-022 — Evidence-eligibility gate (G1–G5)
`ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** A passage may back evidence only if text held and hash verified (G1), rights permit the use in context (G2), workspace may see it (G3), layer matches the claim (G4), origin is not LLM (G5).
- **Why:** The single check that keeps unavailable, restricted or unverified material out of evidence.
- **Sources:** [source-model.md](architecture/source-model.md) §22 · **Related:** DR-017, DR-027, DR-028
- **Allowed:** usable ≠ authoritative (authority and verification still shown) · **Not allowed:** bypassing any gate
- **Risk if ignored:** restricted or fabricated material used as evidence
- **Revisit if:** Tarka design adds gates
- **Reviewer:** — · **Review trigger:** Tarka design

### DR-023 — Source-layer security controls
`SECURITY` · **APPROVED** · 2026-10-26
- **Decision:** Source text is untrusted data for LLMs (prompt injection); safe parsing (no XXE, size/archive limits, quarantine); Unicode safety flags; RightsDecision checked at every exit (API, export, display, snippets, embeddings, caches, external calls); append-only audit; tombstones.
- **Why:** Integrity and licence enforcement depend on these.
- **Sources:** [source-model.md](architecture/source-model.md) §19 · **Related:** DR-024, DR-031
- **Allowed:** — · **Not allowed:** any exit path that skips the rights check
- **Risk if ignored:** injection, leakage, tampering
- **Revisit if:** implementation begins (security review of design)
- **Reviewer:** security reviewer · **Review trigger:** before first importer or API is built

### DR-024 — Workspace isolation of private and internal content
`PRIVACY` `SECURITY` · **APPROVED** · 2026-10-26
- **Decision:** User-supplied and internal-only content is scoped to its workspace, never enters shared indexes, and is not sent to external processors without explicit user consent.
- **Why:** Protects users' private material and third-party rights.
- **Sources:** [source-model.md](architecture/source-model.md) §19, §7.1 (R6) · **Related:** DR-028
- **Allowed:** private use by the owner · **Not allowed:** cross-workspace visibility
- **Risk if ignored:** privacy and licence breaches
- **Revisit if:** team/shared workspaces are designed
- **Reviewer:** privacy/security reviewer · **Review trigger:** auth/workspace design

## Licensing

### DR-025 — Rights evaluated per use context
`LICENSING` `ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** Evidence-backed, append-only licence records; effective rights computed across the rights chain and evaluated per use context into a RightsDecision; five access classes.
- **Why:** Same material can be usable in one context and not another.
- **Sources:** [ADR-0006](architecture/decisions/0006-evidence-backed-licences-contextual-rights.md), [ADR-0012](architecture/decisions/0012-conservative-rights-policy-silence-is-not-permission.md) · **Related:** DR-026, DR-030
- **Allowed:** context-specific outcomes · **Not allowed:** a single global "usable" flag
- **Risk if ignored:** over- or under-use of licensed material
- **Revisit if:** never without new ADR
- **Reviewer:** — · **Review trigger:** —

### DR-026 — Silence in a licence is not permission
`LICENSING` · **APPROVED** · 2026-10-26
- **Decision:** Explicitly permitted → permitted (with conditions); explicitly prohibited → prohibited; silent/unknown → UNKNOWN, pending review; conflicts → more restrictive reading; undocumented upstream links → UNKNOWN. RiseWise never claims silence means permission. **RiseWise conservative product policy, not legal advice.**
- **Why:** Resolved C-009; decides whether any third-party text can be used.
- **Sources:** [ADR-0012](architecture/decisions/0012-conservative-rights-policy-silence-is-not-permission.md); [source-model.md](architecture/source-model.md) §7.1; [C-009](CONFLICTS.md) (resolved) · **Related:** DR-027, DR-033
- **Allowed:** using explicitly permitted uses · **Not allowed:** inferring permission from silence or free accessibility
- **Risk if ignored:** licence breaches
- **Revisit if:** legal review recommends a different policy
- **Reviewer:** legal (optional, policy is conservative) · **Review trigger:** before any hosted or paid offering

### DR-027 — Unknown rights block shared/public evidence
`LICENSING` · **APPROVED** · 2026-10-26
- **Decision:** A source with unresolved rights for a use must not become shared or public evidence. Rights are resolved only when every chain link has evidence and the licence record is reviewed.
- **Why:** Implements DR-026 at the evidence gate (G2).
- **Sources:** [ADR-0012](architecture/decisions/0012-conservative-rights-policy-silence-is-not-permission.md) (R5) · **Related:** DR-022, DR-032
- **Allowed:** private USER_SUPPLIED use (DR-028) · **Not allowed:** shared evidence from LICENCE_PENDING sources
- **Risk if ignored:** restricted material published via answers
- **Revisit if:** never relaxed without product-owner decision
- **Reviewer:** — · **Review trigger:** —

### DR-028 — Private USER_SUPPLIED pathway
`LICENSING` `PRIVACY` `PRODUCT` · **APPROVED** · 2026-10-26
- **Decision:** A user may import their own legitimately obtained source privately: INTERNAL_USE_ONLY in their workspace, licence UNVERIFIED (user attestation), always labelled, never shared/redistributed/externally processed without consent; promotion to shared corpus only via curator review.
- **Why:** Keeps restricted material usable for its lawful holder without RiseWise redistributing it.
- **Sources:** [ADR-0012](architecture/decisions/0012-conservative-rights-policy-silence-is-not-permission.md) (R6); [source-model.md](architecture/source-model.md) §17, §22 case 4 · **Related:** DR-024
- **Allowed:** private evidence in the owner's workspace · **Not allowed:** treating user attestation as verified licence
- **Risk if ignored:** RiseWise redistributing users' licensed material
- **Revisit if:** terms of service are drafted (user warranties)
- **Reviewer:** legal · **Review trigger:** before public launch

### DR-029 — Conservative default for NC / scholarly-only material
`LICENSING` · **TEMPORARY** · 2026-10-26
- **Decision:** Until the tier policy is decided, NC and scholarly-only material is USER_IMPORT_ONLY in every hosted or paid context.
- **Why:** Safe placeholder while DR-030 is open.
- **Sources:** [ADR-0006](architecture/decisions/0006-evidence-backed-licences-contextual-rights.md); [source-model.md](architecture/source-model.md) §7 · **Related:** DR-030, DR-010
- **Allowed:** local/private use via import · **Not allowed:** hosted or paid redistribution of NC material
- **Risk if ignored:** commercial use of NC material
- **Revisit if:** DR-030 is decided
- **Reviewer:** legal · **Review trigger:** DR-030 decision

### DR-030 — Rights policy per tier, required uses per context, excerpt limits
`LEGAL` `LICENSING` `BUSINESS` · **REVIEW_REQUIRED** · 2026-10-26
- **Question:** How NC, share-alike and scholarly-only licences map to each use context; which uses each context requires; maximum excerpt length for non-redistributable text.
- **Why:** Configures the rights policy; affects every tier.
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-L01, OQ-L03, OQ-L15 · **Related:** DR-029, DR-010
- **Allowed:** conservative default (DR-029) · **Not allowed:** choosing a mapping without legal review
- **Risk if ignored:** licence breaches at scale
- **Revisit if:** legal advice received
- **Reviewer:** legal + product owner · **Review trigger:** before any hosted or paid offering

### DR-031 — Sending non-open text to external processors
`LEGAL` `LICENSING` `PRIVACY` · **REVIEW_REQUIRED** · 2026-10-26
- **Question:** Whether text from non-open sources may be sent to cloud LLM or embedding services. Proposed default: only REDISTRIBUTABLE content, unless the licence explicitly allows it.
- **Why:** An external call may itself be a redistribution.
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-L02; [source-model.md](architecture/source-model.md) §19 · **Related:** DR-009, DR-023
- **Allowed:** local processing · **Not allowed:** external processing of non-REDISTRIBUTABLE text before decision
- **Risk if ignored:** licence breach and data egress
- **Revisit if:** legal advice received or DR-009 decided
- **Reviewer:** legal · **Review trigger:** before LLM integration

### DR-032 — Who may verify licences
`LICENSING` `OPERATIONAL` · **OPEN** · 2026-10-26
- **Question:** Who may set CURATOR_VERIFIED / LEGAL_REVIEWED and what evidence is required.
- **Why:** Rights resolution (DR-027) depends on it.
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-L04 · **Related:** DR-027
- **Allowed:** — · **Not allowed:** marking licences verified without a defined reviewer role
- **Risk if ignored:** unaccountable licence approvals
- **Revisit if:** governance roles are defined
- **Reviewer:** product owner · **Review trigger:** before any licence is marked resolved

### DR-033 — Current third-party Vedic examples are LICENCE_PENDING
`LICENSING` `DATA` · **BLOCKED** · 2026-10-26
- **Finding:** Under DR-026, every VedaWeb Ṛgveda layer (incl. the CC BY 4.0 Zurich morphology) and the Sanskrit Library Taittirīya Saṃhitā are LICENCE_PENDING for shared/public use. No third-party Vedic text is shared evidence today.
- **Why:** Vedic MVP depth depends on clearing these chains.
- **Sources:** [source-model.md](architecture/source-model.md) §22.6; examples [01](architecture/source-model-examples/01-rigveda-passage.yaml), [02](architecture/source-model-examples/02-taittiriya-samhita-passage.yaml) · **Related:** DR-034, DR-035
- **Allowed:** private USER_SUPPLIED copies · **Not allowed:** shared/public evidence from these sources
- **Risk if ignored:** licence breach; or, if forgotten, an MVP with no usable Vedic text
- **Revisit if:** any rights chain is resolved
- **Reviewer:** product owner (correspondence), legal · **Review trigger:** responses to DR-034/DR-035

### DR-034 — VedaWeb licensing chain
`LICENSING` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** VedaWeb states CC licences per layer [V], but upstream links (van Nooten–Holland/UT Austin notice "research, not commercial" [S]; GRETIL/Sansknet input; Lubotsky; Zurich annotation) have undocumented or narrower terms; translation layers (Griffith 1890, Geldner HOS 2003) have unverified underlying rights.
- **Why:** Blocks all VedaWeb layers (DR-033).
- **Sources:** [C-004](CONFLICTS.md); [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-L09, OQ-L14 · **Related:** DR-033
- **Allowed:** recording statements as licence evidence · **Not allowed:** assuming VedaWeb's licence covers upstream rights
- **Risk if ignored:** relying on a grant the provider may not have been able to give
- **Revisit if:** VedaWeb or upstream holders clarify in writing
- **Reviewer:** legal; curator · **Review trigger:** clarification received

### DR-035 — Sanskrit Library / TITUS licensing relationship
`LICENSING` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** Sanskrit Library offers its TITUS-derived TS under CC BY-NC-SA 3.0 [S]; TITUS terms allow scholarly use, prohibit commercial use and are silent on redistribution [S]; GRETIL lists the TITUS TS as restricted [S].
- **Why:** The only licence-clear-looking structured TS found is blocked.
- **Sources:** [C-006](CONFLICTS.md); OQ-L10 · **Related:** DR-033
- **Allowed:** — · **Not allowed:** shared use until clarified
- **Risk if ignored:** redistribution beyond upstream terms
- **Revisit if:** written confirmation from Sanskrit Library and/or TITUS
- **Reviewer:** legal; curator · **Review trigger:** clarification received

### DR-036 — DCS licence discrepancy and upstream editions
`LICENSING` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** Website states CC BY 3.0, repository CC BY 4.0 [S]; base texts come from various upstream editions with undocumented terms.
- **Why:** DCS was a candidate openly licensed linguistic layer; currently LICENCE_PENDING.
- **Sources:** [C-005](CONFLICTS.md); OQ-L13 · **Related:** DR-033
- **Allowed:** recording both statements (DISPUTED) · **Not allowed:** treating DCS as REDISTRIBUTABLE
- **Risk if ignored:** relying on an unconfirmed licence version and upstream rights
- **Revisit if:** maintainer confirms
- **Reviewer:** curator; legal · **Review trigger:** confirmation received

### DR-037 — ashtadhyayi.com permission and provenance
`LICENSING` `SCHOLARLY` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** README: "free to use … provided that appropriate credits are mentioned" [V]; no formal licence; source editions of commentaries undocumented.
- **Why:** Richest grammar/commentary source (Pāṇini, Siddhānta Kaumudī) is LICENCE_PENDING and lacks edition provenance.
- **Sources:** [C-008](CONFLICTS.md); OQ-L11; example [03](architecture/source-model-examples/03-panini-rule.yaml) · **Related:** DR-041
- **Allowed:** — · **Not allowed:** ingestion or evidence use before written permission and edition provenance
- **Risk if ignored:** licence breach; unverifiable edition basis
- **Revisit if:** written permission and edition list obtained
- **Reviewer:** legal; Sanskrit expert (editions) · **Review trigger:** response received

### DR-038 — GRETIL per-file licences
`LICENSING` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** Collection licence reported CC BY-NC-SA 4.0 [S]; individual file headers decide; GRETIL is also an upstream link for VedaWeb layers.
- **Why:** Affects GRETIL directly and VedaWeb indirectly.
- **Sources:** OQ-L07 · **Related:** DR-034
- **Allowed:** — · **Not allowed:** assuming collection-level terms per file
- **Risk if ignored:** per-file restrictions missed
- **Revisit if:** files of interest are checked
- **Reviewer:** curator · **Review trigger:** before any GRETIL-derived source is used

### DR-039 — Ambuda licence metadata and coverage
`LICENSING` `DATA` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** Permissive/public-domain intent stated, but per-text licence fields missing [S]; Vedic and grammar coverage unconfirmed.
- **Why:** Potential future licence-clear source; currently LICENCE_PENDING.
- **Sources:** [C-007](CONFLICTS.md); OQ-V14 · **Related:** DR-043
- **Allowed:** — · **Not allowed:** treating Ambuda texts as public domain without per-text evidence
- **Risk if ignored:** relying on intent, not licence
- **Revisit if:** per-text licences published or confirmed
- **Reviewer:** curator · **Review trigger:** before any Ambuda text is used

### DR-040 — Tool and dictionary licences (Vidyut, Sanskrit Heritage, Cologne)
`LICENSING` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** Vidyut code MIT [V], data-bundle licence unstated; Sanskrit Heritage data LGPLLR [S]; Cologne dictionaries CC BY-SA 4.0 at repository level [V], per-dictionary terms unconfirmed.
- **Why:** Linguistic layers and definitions depend on them; share-alike obligations.
- **Sources:** OQ-L13 · **Related:** DR-043
- **Allowed:** — · **Not allowed:** bundling their data before confirmation
- **Risk if ignored:** unmet share-alike or attribution obligations
- **Revisit if:** confirmed
- **Reviewer:** curator; legal · **Review trigger:** before integration

### DR-041 — Owner of permission correspondence
`OPERATIONAL` `LICENSING` · **OPEN** · 2026-10-26
- **Question:** Who sends permission/clarification requests to VedaWeb, Sanskrit Library/TITUS, ashtadhyayi.com, DCS (drafts can be prepared on request).
- **Why:** DR-033–DR-037 cannot progress without it.
- **Sources:** OQ-P03 · **Related:** DR-033–DR-037
- **Allowed:** preparing drafts · **Not allowed:** contacting third parties without product-owner approval
- **Risk if ignored:** Vedic sources stay blocked indefinitely
- **Revisit if:** owner assigned
- **Reviewer:** product owner · **Review trigger:** now (long lead time)

### DR-042 — Code licence
`LICENSING` `BUSINESS` · **OPEN** · 2026-10-26
- **Question:** Licence for RiseWise code (Apache-2.0 recommended; AGPL-3.0 alternative).
- **Why:** Needed before code is committed to a public repository.
- **Sources:** OQ-L06 · **Related:** DR-043
- **Allowed:** — · **Not allowed:** publishing code under an assumed licence
- **Risk if ignored:** unclear reuse terms for contributors and users
- **Revisit if:** decided
- **Reviewer:** product owner · **Review trigger:** before first code commit

### DR-043 — First-party corpus strategy and licence
`PRODUCT` `DATA` `LICENSING` · **OPEN** · 2026-10-26
- **Question:** Whether and how RiseWise builds its own redistributable corpus (e.g. verified transcriptions of public-domain editions), and under which licence (OQ-L05); whether to transcribe SCAN_ONLY commentaries.
- **Why:** Long-term path out of third-party licence dependence (DR-033).
- **Sources:** [source-model.md](architecture/source-model.md) §18; OQ-L05 · **Related:** DR-044, DR-047, DR-048
- **Allowed:** design support (FIRST_PARTY origin) · **Not allowed:** starting transcription before DR-044 review
- **Risk if ignored:** permanent dependence on blocked sources
- **Revisit if:** product owner decides
- **Reviewer:** product owner · **Review trigger:** after MVP source model is implemented

### DR-044 — Edition rights for public-domain transcription
`LEGAL` · **REVIEW_REQUIRED** · 2026-10-26
- **Question:** Which public-domain printed editions are legally free to transcribe, given possible protection of scholarly/critical editions in some jurisdictions (e.g. German law [K]).
- **Why:** Precondition for DR-043.
- **Sources:** OQ-L08 · **Related:** DR-043
- **Allowed:** — · **Not allowed:** treating an old print as free to transcribe without review
- **Risk if ignored:** infringing edition rights
- **Revisit if:** legal advice received
- **Reviewer:** legal · **Review trigger:** before any first-party transcription

## Scholarly and research

### DR-045 — Vedic citation conventions are not frozen
`SCHOLARLY` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** `rv.aas` [K], `ts.kpa` lowest unit [K], `sk.num` edition-specific numbering [K], SK `REARRANGEMENT_OF` relation [K], Kṛṣṇa Yajurveda grouping are provisional.
- **Why:** Wrong schemes would mis-address passages.
- **Sources:** [ADR-0011](architecture/decisions/0011-domain-specifics-via-extensions.md); OQ-V02–V05, OQ-V09 · **Related:** DR-020, DR-053
- **Allowed:** provisional, versioned scheme definitions · **Not allowed:** freezing them as architecture or presenting them as established
- **Risk if ignored:** systematic citation errors
- **Revisit if:** expert confirms
- **Reviewer:** Sanskrit/Vedic expert · **Review trigger:** before Vedic extension implementation

### DR-046 — Unverified Vedic bibliographic and encoding facts
`SCHOLARLY` `RESEARCH` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** Śākala recension [S]; accent presence/encoding in VedaWeb and Sanskrit Library files [K]; edition dates and derivation chains [S]; Keith and Böhtlingk editions [K]; padapāṭha in SL TS (unknown); DCS/Ambuda coverage [K]; Cologne dictionary list [K].
- **Why:** These appear in examples; none may be used as truth.
- **Sources:** OQ-V01, OQ-V07, OQ-V08, OQ-V10–V15 · **Related:** DR-050
- **Allowed:** use with tags as hypotheses · **Not allowed:** copying into fixtures, UI or code as facts
- **Risk if ignored:** invented scholarship
- **Revisit if:** verified against primary sources/expert
- **Reviewer:** Sanskrit expert; curator · **Review trigger:** before any fixture or UI uses them

### DR-047 — Traditional commentaries largely unavailable as verified text
`DATA` `SCHOLARLY` · **OPEN** · 2026-10-26
- **Finding:** No licence-clear verified digital text found for Sāyaṇa (RV, TS) or Bhaṭṭa Bhāskara (TS); the Mysore Bhaṭṭa Bhāskara edition is incomplete (kāṇḍa 4 commentary missing; vols 6–7 not published [S]). They are SCAN_ONLY / NOT_AVAILABLE.
- **Why:** "We don't have this" is a key finding for the commentary layer of the Vedic model.
- **Sources:** corpus research (session); example [02](architecture/source-model-examples/02-taittiriya-samhita-passage.yaml) · **Related:** DR-043, DR-019
- **Allowed:** linking scans; NOT_AVAILABLE labels · **Not allowed:** OCR or LLM text as commentary evidence
- **Risk if ignored:** commentary claims without source text
- **Revisit if:** a licensed transcription is found or created
- **Reviewer:** Sanskrit expert · **Review trigger:** DR-043 decision

### DR-048 — Expert reviewer availability
`SCHOLARLY` `OPERATIONAL` · **OPEN** · 2026-10-26
- **Question:** Is a Sanskritist available for collation, scheme confirmation and Vedic golden cases?
- **Why:** DR-045, DR-046, DR-051 and Vedic evaluation depend on it; RiseWise will not write expected answers from model memory.
- **Sources:** OQ-P01 · **Related:** DR-045, DR-046, DR-051
- **Allowed:** structural (non-scholarly) Vedic checks · **Not allowed:** scholarly-accuracy tests without expert input
- **Risk if ignored:** unverified scholarship ships
- **Revisit if:** expert engaged
- **Reviewer:** product owner · **Review trigger:** before Vedic extension implementation

### DR-049 — Vedic authority rubric
`SCHOLARLY` · **OPEN** · 2026-10-26
- **Question:** Tiers and purposes for authority assessments in the Vedic domain (provisional list in source-model.md §11g).
- **Why:** Authority must be justified per purpose.
- **Sources:** OQ-V06 · **Related:** DR-016, DR-048
- **Allowed:** UNASSESSED default · **Not allowed:** authority inferred from popularity
- **Risk if ignored:** arbitrary weighting of sources
- **Revisit if:** expert input
- **Reviewer:** Sanskrit expert · **Review trigger:** before authority assessments are recorded
- **Note (2026-10-27):** The provisional tier `ROOT_TEXT_EDITION` overlaps with the DR-057 ROOT_TEXT designation (it names a text role, not a degree of authority). Retained, not renamed; its rename or removal is decided here ([ADR-0020](architecture/decisions/0020-root-text-designation.md)).

### DR-050 — Corpus research was partly indirect
`RESEARCH` · **REVIEW_REQUIRED** · 2026-10-26
- **Finding:** GRETIL, TITUS, Ambuda, Sanskrit Library and Zenodo could not be opened directly during research (session network restrictions); findings from them are [S] search summaries. Nothing was downloaded.
- **Why:** Licence and coverage conclusions rest partly on secondary summaries.
- **Sources:** corpus research (session); tag legend in [source-model.md](architecture/source-model.md) · **Related:** DR-034–DR-040, DR-046
- **Allowed:** using [S] findings as leads · **Not allowed:** acting on [S] findings as verified
- **Risk if ignored:** decisions based on misread summaries
- **Revisit if:** a verification pass reads primary pages and sample files
- **Reviewer:** curator · **Review trigger:** before any source is approved for acquisition

## Technical and data (pre-schema)

### DR-051 — Vedic Unicode and accent handling
`TECHNICAL` `SCHOLARLY` · **REVIEW_REQUIRED** · 2026-10-26
- **Question:** Working-copy normalisation (NFC or none) given canonical reordering of combining accent marks; raw original stays the reference.
- **Why:** Accents are scholarly content.
- **Sources:** OQ-E03; [ADR-0005](architecture/decisions/0005-preserve-original-text.md) · **Related:** DR-015, DR-052
- **Allowed:** raw-original storage · **Not allowed:** destructive normalisation
- **Risk if ignored:** silent accent corruption; offset mismatches
- **Revisit if:** expert + engineering decision
- **Reviewer:** Sanskrit expert + engineering · **Review trigger:** schema design (affects DR-052)
- **Note (2026-10-27):** Offsets no longer depend on this policy (DR-052 uses the stored `original`), but the working-copy normalisation policy remains open.

### DR-052 — Evidence span offsets
`TECHNICAL` `DATA` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** Evidence spans use Unicode scalar-value (code-point) offsets, zero-based and half-open `[start,end)`, over the exact stored `original` Passage text. Normalised/search text is never the coordinate system. `quotedTextHash` verifies the span; `contentHash` verifies the passage. Spans never split invalid Unicode sequences. Reconciled with ADR-0005 by ADR-0021: acquired bytes are preserved and hashed; `original` is decoded Unicode with the decoding recorded; undecodable material is quarantined, never replaced. Unicode offsets are not byte offsets.
- **Why:** Anchors must be re-verifiable and are costly to migrate.
- **Sources:** [ADR-0015](architecture/decisions/0015-evidence-span-offsets.md); [ADR-0021](architecture/decisions/0021-acquired-bytes-and-decoded-passage-text.md) · **Related:** DR-014, DR-015, DR-051, DR-064
- **Allowed:** evidence anchors in the approved coordinate system · **Not allowed:** byte offsets, grapheme offsets or normalised-text offsets; U+FFFD substitution in citable text
- **Risk if ignored:** anchors that cannot be re-verified
- **Revisit if:** a script or source requires a different unit (new decision required)
- **Reviewer:** — · **Review trigger:** —
- **History:** opened 2026-10-26 as "Evidence span offsets and passage granularity" (OQ-E02, OQ-E08). Passage granularity and cross-passage spans were not part of the approval and moved to DR-064 (OPEN).

### DR-053 — Citation-scheme scope and locus mappings
`TECHNICAL` `DATA` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** Every CitationScheme declares scope `WORK` or `EDITION`; a Locus belongs to its scheme's scope. Work-scoped loci support cross-edition addressing only where genuinely valid; edition-scoped loci preserve edition numbering. Locus mappings are not automatically required; they exist only where established and are explicit, typed and provenance-bearing (a constrained Relation `LOCUS_MAPS_TO` with type, basis and provenance). Never inferred from matching or sequential numbers. A Locus is an address; a Passage is evidence.
- **Why:** Edition numberings differ; inferred correspondences would mis-cite.
- **Sources:** [ADR-0016](architecture/decisions/0016-citation-scheme-scope-and-locus-mappings.md) (amends [ADR-0002](architecture/decisions/0002-locus-distinct-from-passage.md)); [C-012](CONFLICTS.md) · **Related:** DR-012, DR-045
- **Allowed:** recording unresolved suspected correspondences as notes · **Not allowed:** mappings without basis or provenance; mappings from numbering alone
- **Risk if ignored:** systematic mis-citation across editions
- **Revisit if:** schema design needs a different mapping representation
- **Reviewer:** — (scheme scopes still need expert confirmation, DR-045) · **Review trigger:** —
- **History:** opened 2026-10-26 as "Citation-scheme mapping and locus scope" (OQ-E04, OQ-E05).

### DR-054 — Identifier scheme
`TECHNICAL` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** Every persisted entity has an immutable opaque primary ID (MVP: ULID). Human-readable keys may exist as separate scoped aliases and are never identity. Content hashes identify immutable content and are distinct from entity IDs. Citation/locus identifiers are governed by their CitationScheme and never embedded in primary IDs. IDs are never reused.
- **Why:** Identifiers are referenced everywhere.
- **Sources:** [ADR-0017](architecture/decisions/0017-identifier-scheme.md) · **Related:** DR-008, DR-062
- **Allowed:** readable aliases, clearly labelled · **Not allowed:** aliases or locus strings as identity; ID reuse
- **Risk if ignored:** unstable or overloaded identifiers
- **Revisit if:** ULID proves unsuitable (format change needs a new decision)
- **Reviewer:** — · **Review trigger:** —
- **History:** opened 2026-10-26 as an OPEN question (OQ-E01); the "both" proposal is what was approved, with ULID chosen.

### DR-055 — SourceSnapshot granularity
`TECHNICAL` `DATA` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** A SourceSnapshot is the immutable version boundary for citable source content. A Source may have multiple snapshots; every Passage belongs to exactly one. Snapshots have a deterministic content hash. Changed citable content creates a new snapshot; metadata-only changes do not. Reasoning runs are traceable to the exact snapshot/content used.
- **Why:** Reproducibility and per-layer licensing.
- **Sources:** [ADR-0018](architecture/decisions/0018-sourcesnapshot-granularity.md) (refines [ADR-0004](architecture/decisions/0004-immutable-content-addressed-snapshots.md)) · **Related:** DR-011, DR-014
- **Allowed:** one Acquisition producing snapshots for several Sources · **Not allowed:** modifying a snapshot; new textual snapshots for metadata-only changes
- **Risk if ignored:** irreproducible reasoning
- **Revisit if:** schema design defines the canonical serialisation for hashing
- **Reviewer:** — · **Review trigger:** —
- **History:** recorded 2026-10-26 as PROPOSED ("one SourceSnapshot per Source under a shared Acquisition", OQ-E09).

### DR-056 — Annotation alignment
`TECHNICAL` `DATA` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** Annotations are separate, versioned objects that never modify SourceSnapshot or Passage content. They may target passages, exact spans (DR-052 coordinates), structural units or other annotations, and every reference is bound to a specific SourceSnapshot and Passage. Cross-text alignments (e.g. Sanskrit ↔ translation/commentary) are explicit, typed and provenance-bearing, never inferred from position. Content changes never silently migrate annotations. LLM-generated annotations remain proposals unless independently verified.
- **Why:** Analysis must stay attached to the exact text it describes.
- **Sources:** [ADR-0019](architecture/decisions/0019-annotation-alignment.md) · **Related:** DR-017, DR-022, DR-065
- **Allowed:** explicit, recorded re-targeting as a new annotation version · **Not allowed:** silent migration; positional alignment; LLM annotations as evidence without verification
- **Risk if ignored:** misaligned or unvetted linguistic evidence
- **Revisit if:** —
- **Reviewer:** — · **Review trigger:** —
- **History:** opened 2026-10-26 as "Annotation alignment and dataset evidence eligibility" (OQ-E06, OQ-E10). Human-curated dataset evidence eligibility was not part of the approval and moved to DR-065 (OPEN).

### DR-057 — ROOT_TEXT designation
`TECHNICAL` `DATA` `SCHOLARLY` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** `ROOT_TEXT` is an explicit, reviewed source-role designation for the authoritative textual layer of a specified Work or Edition context. Never inferred from language, origin, OCR, website labels, agreement with another source or LLM generation. Multiple legitimate representations across editions/recensions stay distinct. Derived representations (translation, commentary, transliteration, normalised text, OCR, reconstruction) never silently replace it. Vedic accents are textual content. Represented as a constrained Relation `DESIGNATED_ROOT_TEXT_FOR` with reviewer provenance — distinct from layer type and from authority assessment.
- **Why:** Prevents unreviewed text being treated as authoritative.
- **Sources:** [ADR-0020](architecture/decisions/0020-root-text-designation.md); [C-011](CONFLICTS.md) · **Related:** DR-020, DR-048, DR-049, DR-066
- **Allowed:** designations made through review · **Not allowed:** `ROOT_TEXT` as a layer type; inferred designations; reading the `ROOT_TEXT_EDITION` authority tier as a designation
- **Risk if ignored:** unreviewed or derived text cited as the authoritative text
- **Revisit if:** —
- **Reviewer:** Sanskrit expert for each Vedic designation · **Review trigger:** each designation
- **History:** opened 2026-10-26 as "Root-text layer for non-Vedic śāstra works" (OQ-E07). The remaining question — which layer type non-Vedic base texts use — moved to DR-066 (OPEN). `ROOT_TEXT_EDITION` tier naming moved to DR-049.

### DR-058 — "EVIDENCE" as epistemic kind and as entity
`PRODUCT` `ARCHITECTURE` · **OPEN** · 2026-10-26
- **Question:** How the epistemic kind EVIDENCE relates to the EvidenceAnchor/evidence link.
- **Why:** Affects how users read "known vs inferred".
- **Sources:** [C-002](CONFLICTS.md) · **Related:** DR-003
- **Allowed:** source model provides EvidenceAnchor only · **Not allowed:** defining Tarka evidence semantics ad hoc
- **Risk if ignored:** inconsistent labelling in Tarka
- **Revisit if:** Tarka design
- **Reviewer:** product owner · **Review trigger:** before Tarka schema work

### DR-059 — Terminology: Source, Manifest, Version
`ARCHITECTURE` · **RESOLVED** · 2026-10-26
- **Decision:** Source = concrete representation of an Edition; Version = SourceSnapshot plus append-only revisions; Manifest embedded in Acquisition.
- **Why:** Shared vocabulary.
- **Sources:** [C-003](CONFLICTS.md) (resolved); [source-model.md](architecture/source-model.md) §3 · **Related:** DR-011
- **Allowed:** loose "source" in UI copy · **Not allowed:** other meanings in APIs/schemas
- **Risk if ignored:** ambiguous APIs
- **Revisit if:** schema naming review
- **Reviewer:** — · **Review trigger:** —

### DR-060 — Target user, primary job and MVP specialization
`PRODUCT` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):**
  - **Primary user/persona — Evidence-driven Researcher:** a researcher who needs to investigate a question using traceable evidence and produce a defensible, challengeable conclusion.
  - **Primary job:** investigate a question using traceable evidence and produce a defensible, challengeable conclusion with explicit provenance, assumptions, contradictions and uncertainty — mapping to the Tarka reasoning chain (Question → Claims → Evidence → Sources → Arguments → Counterarguments → Assumptions → Inferences → Contradictions → Uncertainty → Conclusion → Provenance).
  - **Primary MVP specialization:** Vedic/Sanskrit Researcher/Scholar — the first deeply supported research context, not a restriction on the Tarka engine and not the universal primary user.
  - **Secondary MVP pathway:** a researcher working with their own legitimately obtained sources (the approved `USER_SUPPLIED` route, DR-028).
  - **Model:** RiseWise → Evidence-driven Researcher → research context (Vedic/Sanskrit — primary MVP specialization; own sources — secondary MVP pathway). Tarka remains the structured reasoning capability inside RiseWise.
  - **Positioning (product definition, not marketing copy):** RiseWise — a provenance-first research and reasoning platform; Tarka — the structured reasoning capability inside RiseWise. The prototype-era line "A provenance-first AI reasoning engine for defensible decisions" is retired as the product definition. Final marketing copy is not decided.
  - **Scope:** individual researcher first; institutional/team use is later, not MVP. Private `USER_SUPPLIED` sources are acceptable as an MVP pathway. Students/learners are not an MVP persona (future support is not prohibited). Decision-makers are not a separate primary persona; the retired prototype framing does not determine product identity.
- **Why:** Evaluation cases, UI and MVP priorities depend on who RiseWise serves.
- **Sources:** product-owner approval (session, 2026-10-27); [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) PR-013 · **Related:** DR-001, DR-002, DR-004, DR-028, DR-033, DR-061, DR-063
- **Allowed:** designing MVP work around the evidence-driven researcher with the two research contexts above · **Not allowed:** treating Vedic scholars as the only user; adding decision-makers or students as MVP personas; inventing a marketing tagline as an approved decision; reading this as a decision on DR-061 (GENERAL scope), DR-009 (deployment) or DR-010 (commercial intent)
- **Risk if ignored:** features built for an imagined user; the retired prototype framing redefining the product
- **Revisit if:** institutional/team use or learners are brought into scope; the Vedic corpus remains unusable for shared evidence (DR-033)
- **Reviewer:** product owner · **Review trigger:** before Tarka or UI design
- **History:** opened 2026-10-26 as "Target users, personas and use cases undefined" (OPEN) — "No target users, personas or primary use cases have been defined. Identified while writing PRODUCT_REQUIREMENTS.md."

### DR-061 — GENERAL domain
`PRODUCT` `ARCHITECTURE` · **APPROVED** · 2026-10-27
- **Decision (approved 2026-10-27):** GENERAL is a structural, domain-neutral baseline extension of RiseWise/Tarka. It applies generic source, citation, provenance and reasoning behaviour to material that does not require specialised domain rules. For the MVP, GENERAL operates over legitimately supplied user sources. GENERAL is not a topical catch-all, a general-knowledge model, or the historical decision-analysis system. Live open-web retrieval and a curated GENERAL corpus are outside the MVP unless separately approved. `USER_SUPPLIED` is a domain-neutral source/rights route and may be used by both GENERAL and specialised domains such as VEDIC_SANSKRIT.
- **Scope interpretation:**
  - GENERAL is structural, not topical; it is not "everything that is not Vedic".
  - MVP source scope: legitimately supplied user sources. `USER_SUPPLIED` is a source/rights route, not a domain, and may serve both GENERAL and VEDIC_SANSKRIT.
  - Tarka's domain-neutral core rules apply; LLM/model knowledge cannot become supported evidence merely because a question is in GENERAL.
  - Live open-web retrieval is outside the MVP; captured web pages are also outside the MVP unless separately approved.
  - A curated GENERAL corpus is outside the MVP; its strategy remains with DR-043.
  - The historical RITA decision-analysis prototype is not part of GENERAL.
  - MVP includes baseline GENERAL evaluation focused on generic reasoning, provenance and evidence behaviour, without a separate subject-matter expert role.
- **Not resolved or changed by this decision (each keeps its current status):** DR-009 (deployment), DR-010 (commercial intent), DR-030 (tier/source rights), DR-031 (external processing), DR-023 (safe import controls), DR-024 (workspace isolation), DR-043 (first-party corpus), DR-064 (passage granularity), document ingestion and supported formats, detailed web-capture policy beyond the MVP exclusion, detailed GENERAL evaluation design.
- **Why:** Determines what the GENERAL extension must support and prevents an unbounded domain.
- **Sources:** product-owner approval (session, 2026-10-27); [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) PR-120, PR-121, PR-122, PR-213, PR-214; [source-model.md](architecture/source-model.md) §12; [ADR-0011](architecture/decisions/0011-domain-specifics-via-extensions.md) · **Related:** DR-004, DR-020, DR-028, DR-043, DR-060, DR-063
- **Allowed:** GENERAL reasoning over legitimately supplied user sources under core rules · **Not allowed:** treating GENERAL as a topical catch-all or general-knowledge model; live web retrieval, captured web pages or a curated GENERAL corpus in the MVP without separate approval; equating `USER_SUPPLIED` with GENERAL
- **Risk if ignored:** GENERAL becomes an empty or unbounded domain
- **Revisit if:** web retrieval/capture or a curated corpus is proposed; DR-043 is decided
- **Reviewer:** product owner · **Review trigger:** before GENERAL extension design
- **History:** opened 2026-10-26 as "GENERAL domain scope undefined" (OPEN) — "GENERAL is an approved MVP domain, but its scope (question types, source types, any curated corpus) is undefined; 'user-supplied sources only' is a Claude proposal, not approved."

### DR-062 — Schema technology: TypeScript + Zod (only)
`TECHNICAL` `ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** TypeScript is the definition language and Zod the runtime validation library for RiseWise domain models and validation schemas.
- **Why:** Step 2 (schema definitions validated by tests) needs both; removes the blocker identified in DR-008.
- **Sources:** [ADR-0013](architecture/decisions/0013-typescript-and-zod-for-domain-models.md); product-owner approval (session) · **Related:** DR-008, DR-007
- **Allowed:** writing domain-model types and Zod schemas once Step 2 is authorised · **Not allowed:** treating any other stack item as approved — React/Vite, Fastify, SQLite, PostgreSQL, Ollama, cloud LLM providers, embeddings, search, authentication, deployment platform, billing/tiers, monorepo/ORM/test tooling all stay PROPOSED or OPEN
- **Risk if ignored:** scope creep from "schema technology approved" to "stack approved"
- **Revisit if:** Zod cannot express a required model constraint, or a cross-language need arises
- **Reviewer:** — · **Review trigger:** —

### DR-063 — Python prototype retired as the core implementation path
`TECHNICAL` `ARCHITECTURE` · **APPROVED** · 2026-10-26
- **Decision:** The earlier Python implementation on `main` (Context Structurer, RITA Engine, pipeline orchestration, Ollama integration) was a narrower prototype that informed the evolution of the current RiseWise/Tarka design. It is retired as the core implementation path and remains recoverable through Git history: [`7d3199a`](https://github.com/AT-Solves/RiseWise/commit/7d3199a43a47ea9c5071be5e01224c28264672fd), [`41713d5`](https://github.com/AT-Solves/RiseWise/commit/41713d5614c20dbab156e52c2d940f9e902aab0f), [`fa1c324`](https://github.com/AT-Solves/RiseWise/commit/fa1c324b6b2dadbe084910a1c71c565cc6f80dd6), [`cb43582`](https://github.com/AT-Solves/RiseWise/commit/cb43582520107201119395629a551b61a8d0dd10).
- **Why:** Records the prototype's existence and status explicitly, so it is neither lost nor mistaken for the current core path; corrects DR-005.
- **Sources:** [ADR-0014](architecture/decisions/0014-retire-python-prototype-as-core-implementation.md); [ADR-0013](architecture/decisions/0013-typescript-and-zod-for-domain-models.md) · **Related:** DR-062, DR-005, DR-008
- **Allowed:** referring to and recovering the prototype from history; future explicitly approved Python for supporting tooling (research tools, corpus processing, evaluation, scripts) · **Not allowed:** continuing the prototype as the core implementation path; treating this as a judgement that the prototype was wrong; treating ADR-0013 as the decision that retired Python
- **Risk if ignored:** two competing core implementations; or prototype work forgotten
- **Revisit if:** a supporting Python tool is proposed; or `main` and the design branch are integrated (removal of prototype files and the old `docs/adr-0001` … `0004` numbering collision are separate, undecided items)
- **Reviewer:** — · **Review trigger:** branch integration

### DR-064 — Passage granularity and cross-passage spans
`TECHNICAL` `DATA` · **OPEN** · 2026-10-27
- **Question:** Flat vs hierarchical passages (e.g. sūkta ⊃ ṛc ⊃ pāda); how evidence spans crossing passage boundaries are represented; whether span boundaries inside grapheme clusters are allowed.
- **Why:** Split from DR-052, whose approval covered offsets only.
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-E08; [ADR-0015](architecture/decisions/0015-evidence-span-offsets.md) · **Related:** DR-052
- **Allowed:** — · **Not allowed:** fixing passage granularity in schema without a decision
- **Risk if ignored:** evidence that cannot span verses or sentences
- **Revisit if:** decided
- **Reviewer:** engineering (+ Sanskrit expert) · **Review trigger:** before schema design

### DR-065 — Evidence eligibility of human-curated annotation datasets
`TECHNICAL` `DATA` `SCHOLARLY` · **OPEN** · 2026-10-27
- **Question:** Whether human-curated annotation datasets (e.g. the Zurich Ṛgveda morphology) are evidence-eligible immediately (origin `DATASET`) or only after review such as `ANNOTATION_SPOT_CHECK`.
- **Why:** Split from DR-056, whose approval covered alignment and LLM annotations only.
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-E10; [ADR-0019](architecture/decisions/0019-annotation-alignment.md) · **Related:** DR-056, DR-022
- **Allowed:** — · **Not allowed:** treating dataset annotations as evidence before decided
- **Risk if ignored:** unvetted linguistic evidence
- **Revisit if:** decided
- **Reviewer:** engineering + Sanskrit expert · **Review trigger:** before annotation import

### DR-066 — Layer type for non-Vedic base texts
`TECHNICAL` `DATA` · **OPEN** · 2026-10-27
- **Question:** Which layer/artifact type a Source uses when it represents the text of a non-Vedic work itself (e.g. the Aṣṭādhyāyī sūtrapāṭha), now that `ROOT_TEXT` is a designation and not a layer.
- **Why:** Remainder of the original DR-057 question.
- **Sources:** [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) OQ-E07; [ADR-0020](architecture/decisions/0020-root-text-designation.md); example [03](architecture/source-model-examples/03-panini-rule.yaml) · **Related:** DR-057, DR-020
- **Allowed:** placeholder in examples · **Not allowed:** `ROOT_TEXT` or `SAMHITA_PATHA` as the layer for sūtra texts
- **Risk if ignored:** mislabelled layers
- **Revisit if:** decided
- **Reviewer:** engineering (+ Sanskrit expert) · **Review trigger:** schema design

---

## Change log

| Date | Change |
|---|---|
| 2026-10-27 | DR-061 approved: GENERAL is a structural, domain-neutral baseline extension; MVP sources are legitimately supplied user sources; live web retrieval, captured web pages and a curated GENERAL corpus outside the MVP; USER_SUPPLIED is a domain-neutral route. PR-120/121/122/213/222 reconciled; PR-214 split from PR-213. |
| 2026-10-27 | DR-060 approved: Evidence-driven Researcher; primary job; Vedic/Sanskrit as primary MVP specialization; own sources (USER_SUPPLIED) as secondary pathway; individual first; prototype-era positioning retired. |
| 2026-10-27 | DR-052 … DR-057 approved (ADR-0015 … ADR-0020); ADR-0021 reconciles ADR-0005 with DR-052. Unapproved remainders split out as DR-064 (passage granularity), DR-065 (dataset evidence eligibility), DR-066 (layer type for non-Vedic base texts). Notes added to DR-015, DR-049, DR-051. |
| 2026-10-26 | Added DR-063 (Python prototype retired as core path; ADR-0014). Added dated correction to DR-005 (earlier prototype exists on `main`). |
| 2026-10-26 | Added DR-062 (TypeScript + Zod approved for domain models/schemas only; ADR-0013). DR-008 updated: remainder of stack still PROPOSED. |
| 2026-10-26 | Status counts audited (index and entries consistent; earlier chat report had miscounted APPROVED, OPEN and REVIEW_REQUIRED). DR-006 → RESOLVED via PRODUCT_REQUIREMENTS.md. Added DR-060, DR-061 (gaps found while writing requirements). Added status summary. |
| 2026-10-26 | Register created and seeded with DR-001 … DR-059 from the source model, ADR-0001 … ADR-0012, CONFLICTS.md, OPEN_QUESTIONS.md and recorded session decisions. No existing open question was closed. |
