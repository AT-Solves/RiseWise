# RiseWise Product Requirements

| | |
|---|---|
| **Status** | v0.1 — records requirements established so far. Documentation only. |
| **Created** | 2026-10-26 |
| **Counts** | 101 items: 68 APPROVED · 18 PROVISIONAL · 15 OPEN (§23 consolidates the OPEN items and related open decisions). |
| **Why it exists** | Several fundamental requirements existed only in Claude session history (Decision Register DR-006). |
| **Related** | [`DECISION_REGISTER.md`](DECISION_REGISTER.md) · [`architecture/source-model.md`](architecture/source-model.md) · [`architecture/decisions/`](architecture/decisions/README.md) · [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) · [`CONFLICTS.md`](CONFLICTS.md) |

## How to read this document

Every item has one classification:

| Label | Meaning |
|---|---|
| **APPROVED** | Approved requirement. Stated or explicitly approved by the product owner. |
| **PROVISIONAL** | Provisional / proposed. Suggested in design work (often by Claude) but **not** explicitly approved. Must not be treated as a requirement. |
| **OPEN** | Open decision. A question the product owner has not yet decided. |

**Distinctions this document keeps:**

- **Requirement ≠ architectural decision ≠ implementation choice.** This document states *what* RiseWise must do. *How* is recorded in ADRs (architecture) and, later, implementation documents. Where a requirement is implemented by an ADR, the ADR is referenced, not restated.
- **Open question ≠ approved requirement.** OPEN items may not be relied on.
- **Legal policy ≠ legal advice.** Licensing items describe RiseWise's conservative product policy. None is a legal conclusion.
- **Scholarly requirement ≠ verified scholarly fact.** Requiring support for, e.g., *kāṇḍa / prapāṭhaka / anuvāka* does not assert any citation convention; those remain unverified (DR-045, DR-046).

**Source notes.** "PO" = product owner. Most requirements were established in a single Claude Code session on 2026-10-26. Source notes name the session message they came from:

| Note | Session message |
|---|---|
| `PO-brief` | Product owner's greenfield brief introducing Tarka (reasoning chain, epistemic kinds, statuses, domains, architectural principle, "Challenge this conclusion") |
| `PO-approval-1` | Product owner's approval of the core product direction (MVP domains, "Why?", the seven user-understanding questions) |
| `PO-corpus` | Product owner's corpus-research brief (planned Vedic knowledge model; NOT_AVAILABLE instead of unverified substitutes) |
| `PO-source` | Product owner's Knowledge Source Model brief (source-first principle, concepts, licence fields, rights classes, tiers, versioning, constraints) |
| `PO-C009` | Product owner's conservative licensing rule resolving CONFLICT C-009 |
| `PO-steps` | Product owner's repeated phase constraints ("do not implement …") |
| `Claude-rev1` / `Claude-rev2` | Claude's architecture proposal revisions 1 and 2 — **proposals only** unless later approved |
| `SM-v0.1` | Knowledge Source Model v0.1, approved by the product owner |

---

## 1. Product Definition

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-001 | RiseWise is a provenance-first knowledge, research and reasoning platform. | APPROVED | PO-approval-1 | DR-001 |
| PR-002 | The product name is RISEWISE; its core reasoning capability is called TARKA. | APPROVED | PO-brief | DR-001 |
| PR-003 | RiseWise evolves from its original Vedic/Sanskrit knowledge-discovery focus into a general-purpose reasoning platform, keeping Vedic/Sanskrit as the first specialised domain. | APPROVED | PO-brief | DR-001, DR-004 |
| PR-004 | The implementation is greenfield. RiseWise v0.1 (TypeScript demo, no database, AI-generated summaries), v0.2 (evaluation, 14/14 checks) and v0.3 (verification rules, source-record fields, 31/31 checks) are product history, not code to preserve. The v0.3 check list and field list are not available. | APPROVED | PO-brief (history); session audit | DR-005 |

## 2. Problem RiseWise Solves

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-010 | Help users examine a question through structured, traceable reasoning rather than receiving an unexplained answer. | APPROVED | PO-brief | DR-002 |
| PR-011 | Reason over structured, traceable knowledge instead of treating LLM output as fact. | APPROVED | PO-source | DR-003 |
| PR-012 | Support research-oriented knowledge discovery with provenance-first scholarship (original RiseWise scope). | APPROVED | PO-brief (history) | DR-001 |
| PR-013 | Target users, personas and the primary use cases have **not** been defined. | OPEN | — (gap identified while writing this document) | DR-060 |

## 3. RiseWise vs Tarka

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-020 | RiseWise = knowledge + research + reasoning platform. Tarka = the structured reasoning capability inside RiseWise. | APPROVED | PO-brief, PO-approval-1 | DR-001, DR-002 |
| PR-021 | RiseWise comprises: Tarka Core · Knowledge Layer · Evidence & Provenance · Domain Adapters · Evaluation Framework · Research Workspace · Administration / Governance. (Product structure stated by the PO; technical architecture is separate.) | APPROVED | PO-brief | DR-001 |
| PR-022 | Tarka Core includes: question decomposition, claim extraction, evidence evaluation, argument analysis, counterargument analysis, contradiction detection, assumption detection, inference, uncertainty assessment, conclusion generation, provenance generation. | APPROVED | PO-brief | DR-002 |

## 4. Core Product Principles

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-030 | Tarka is **not** a normal chatbot. | APPROVED | PO-brief, PO-approval-1 | DR-002 |
| PR-031 | An LLM-generated statement is never automatically considered a fact. | APPROVED | PO-brief, PO-approval-1 | DR-003 |
| PR-032 | Evidence and verification rules determine the status of a claim. | APPROVED | PO-approval-1 | DR-003 |
| PR-033 | Every important conclusion must be explainable. | APPROVED | PO-brief | DR-002 |
| PR-034 | The core engine is domain-neutral; domain adapters provide specialised knowledge and validation. | APPROVED | PO-brief, PO-approval-1 | DR-020 |
| PR-035 | Do not implement fake scholarly knowledge. If a corpus is not available, represent that limitation explicitly. | APPROVED | PO-brief | DR-019, DR-047 |
| PR-036 | Provenance is first-class, not an afterthought. | APPROVED | PO-source | DR-016 |
| PR-037 | Local-first / open-source preference; loosely coupled architecture. | APPROVED | PO-brief (history) | — |
| PR-038 | Prefer simple, implementable architecture over unnecessary complexity. | APPROVED | PO-source | — |

## 5. Tarka Reasoning Model

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-040 | Tarka examines a question through: Question → Claims → Definitions → Evidence → Sources → Arguments → Counterarguments → Assumptions → Inferences → Contradictions → Uncertainty → Conclusion → Provenance. | APPROVED | PO-brief, PO-approval-1 | DR-002 |
| PR-041 | The user must be able to understand: what Tarka thinks; why it thinks that; what evidence supports it; what evidence contradicts it; what assumptions are involved; what is known versus inferred; what remains uncertain. | APPROVED | PO-approval-1 | DR-002 |
| PR-042 | A 14-stage pipeline with typed stage contracts, a deterministic status-rule function, and a rules-only (no-LLM) mode for testing. | PROVISIONAL | Claude-rev1 | DR-008 |
| PR-043 | Statuses computed by deterministic rules over the reasoning graph, with the LLM drafting wording only. | PROVISIONAL | Claude-rev1, Claude-rev2 (refines PR-032; mechanism not approved) | DR-003 |
| PR-044 | Status thresholds (e.g. what counts as SUPPORTED vs CONTESTED). | OPEN | Claude-rev1 draft rules only | DR-003 |

## 6. Evidence and Provenance Requirements

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-050 | Every piece of knowledge/evidence must eventually be traceable to its origin: Conclusion → inference → evidence → exact passage → edition → work → source → acquisition/provenance. | APPROVED | PO-source | DR-011, DR-016 |
| PR-051 | RiseWise must answer "Where did this information come from?" and "What exact source passage supports this?" | APPROVED | PO-source | DR-022 |
| PR-052 | Reproducibility: a reasoning result generated today must identify exactly which source and version it used. | APPROVED | PO-source | DR-014 |
| PR-053 | Do not treat an LLM-generated interpretation as source evidence. | APPROVED | PO-source | DR-017 |
| PR-054 | Do not collapse: Work vs Edition · Edition vs Digital Representation · Original text vs Translation · Text vs Commentary · Commentary vs Interpretation · Evidence vs Conclusion · Source vs Claim · Provenance vs Authority · Authority vs Verification · Availability vs Reliability. (Implemented by ADR-0001…0011.) | APPROVED | PO-source | DR-011–DR-021 |
| PR-055 | Quoted evidence must be checked against the stored passage text, so fabricated quotes are rejected. | PROVISIONAL | Claude-rev1 (EvidenceAnchor hash is approved in SM-v0.1; the Tarka-stage quote check is not yet a requirement) | DR-022 |

## 7. "Why?" Requirement

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-060 | Tarka must support "Why?". | APPROVED | PO-approval-1 | DR-002 |
| PR-061 | "Why?" walks the provenance graph from the conclusion back to passages and source records, showing which agent/model/prompt version or rule produced each step and which rules set the status; available on claims, evidence and status. | PROVISIONAL | Claude-rev2 (explanation contract) | DR-022 |

## 8. "Challenge this conclusion" Requirement

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-070 | Tarka must support "Challenge this conclusion". | APPROVED | PO-brief, PO-approval-1 | DR-002 |
| PR-071 | A challenge deliberately attempts to weaken or falsify a conclusion by: identifying hidden assumptions; finding contradictory evidence; finding alternative interpretations; testing source quality; checking reasoning consistency. | APPROVED | PO-brief | DR-002 |
| PR-072 | The final result reassesses the original conclusion. | APPROVED | PO-brief | DR-002 |
| PR-073 | Do not manufacture counterarguments merely to create artificial balance. | APPROVED | PO-brief | DR-002 |
| PR-074 | Mechanism: findings must cite evidence or a specific logical flaw and pass a materiality test; outcomes UPHELD / STRENGTHENED / WEAKENED / OVERTURNED; a new immutable conclusion version with before/after diff; "no material challenge found" is valid. | PROVISIONAL | Claude-rev1, Claude-rev2 | DR-002 |

## 9. Epistemic Kinds

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-080 | Tarka distinguishes FACT · EVIDENCE · INFERENCE · ASSUMPTION · INTERPRETATION · UNCERTAINTY. | APPROVED | PO-brief, PO-source | DR-003 |
| PR-081 | No agent (LLM or person) can directly assign FACT; FACT is reachable only through evidence and verification rules. | PROVISIONAL | Claude-rev1, Claude-rev2 (derived from PR-031/PR-032; exact definition not approved) | DR-003 |
| PR-082 | How the kind EVIDENCE relates to evidence links/entities. | OPEN | CONFLICT C-002 | DR-058 |
| PR-083 | Whether human review is required before a statement may be labelled FACT. | OPEN | Claude-rev1 decision list (Claude-rev2 proposed "rules decide; reviewers confirm inputs" — not approved) | DR-003 |

## 10. Claim/Conclusion Statuses

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-090 | Statuses: SUPPORTED · PARTIALLY_SUPPORTED · CONTRADICTED · CONTESTED · UNVERIFIED · INSUFFICIENT_EVIDENCE · INFERRED. | APPROVED | PO-brief, PO-source | DR-003 |
| PR-091 | Statuses apply to claims (PR-032) and to conclusions. | APPROVED | PO-brief ("possible conclusion statuses"), PO-approval-1 ("status of a claim") | DR-003 |
| PR-092 | Source verification states (fidelity/integrity) are separate from claim statuses. | APPROVED | SM-v0.1 (architecture, ADR-0008) | DR-016 |
| PR-093 | Status definitions and thresholds. | OPEN | see PR-044 | DR-003 |

## 11. MVP Domains

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-100 | The first two MVP domains are GENERAL and VEDIC_SANSKRIT. | APPROVED | PO-approval-1 | DR-004 |
| PR-101 | Product/Business, History, Science and Law are added later. | APPROVED | PO-approval-1 | DR-004 |

## 12. Vedic/Sanskrit Scope

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-110 | Scope: Pāṇini · Aṣṭādhyāyī · Sanskrit grammar · Siddhānta Kaumudī · Vedic Sanskrit · Ṛgveda · Kṛṣṇa Yajurveda · Taittirīya Saṃhitā · linguistic analysis · provenance · source verification · traditional commentary · translations · scholarly interpretation. | APPROVED | PO-brief, PO-approval-1, PO-source | DR-004 |
| PR-111 | Planned Vedic knowledge model: Text → Structure → Passage → Linguistic information → Context → Commentary → Translation → Scholarly interpretation → Provenance. | APPROVED | PO-corpus | DR-011 |
| PR-112 | The model must eventually support: śākhā/recension · maṇḍala · sūkta · ṛc · kāṇḍa · prapāṭhaka · anuvāka · mantra · pada/padapāṭha · saṃhitā text · accent information · grammatical analysis · traditional commentary · translation · scholarly interpretation. *(Capability requirement only — no citation convention is asserted.)* | APPROVED | PO-source | DR-020, DR-045 |
| PR-113 | Vedic-specific structures are domain extensions, not hard-coded core. | APPROVED | PO-source | DR-020 |
| PR-114 | Which corpora/editions to use. The PO asked not to make this decision on their behalf. | OPEN | PO-corpus | DR-033 |
| PR-115 | Vedic golden test cases are written or reviewed by a Sanskrit expert, never from model memory. | PROVISIONAL | Claude-rev1/rev2 (follows from PR-035; mechanism not approved) | DR-048 |

## 13. General-Domain Scope

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-120 | GENERAL is an MVP domain, and the core source model must work beyond Vedic Sanskrit (later History, Science, Law, Product/Business, general research). | APPROVED | PO-approval-1, PO-source | DR-004, DR-020 |
| PR-121 | In the MVP, GENERAL operates over user-supplied sources (documents the user adds). | PROVISIONAL | Claude-rev1 | DR-061 |
| PR-122 | What GENERAL covers (question types, source types, whether any curated general corpus exists). | OPEN | — (gap) | DR-061 |

## 14. Source/Knowledge Requirements

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-130 | RiseWise eventually has its own structured source/knowledge layer. | APPROVED | PO-source | DR-011 |
| PR-131 | External sources may be used where their licences permit. Restricted/copyrighted sources use licence-aware import/reference, never blind redistribution. | APPROVED | PO-source | DR-025, DR-027 |
| PR-132 | RiseWise should be capable of building and maintaining its own first-party corpus from legitimately usable material. (Capability goal; strategy is OPEN — PR-133.) | APPROVED | PO-source | DR-043 |
| PR-133 | First-party corpus strategy, licence and transcription programme. | OPEN | — | DR-043, DR-044 |
| PR-134 | Every source records: licence · licence URL/reference · rights holder if known · permitted use · redistribution status · commercial-use status · attribution requirement · acquisition method · provenance · checksum/hash where appropriate. | APPROVED | PO-source | DR-025 |
| PR-135 | Distinguish material that RiseWise can redistribute · can use internally but not redistribute · users must provide themselves · is unavailable · has licence pending verification. | APPROVED | PO-source | DR-021, DR-025 |
| PR-136 | Support versioning of sources, editions, corpus updates, corrections, re-imports, and changed metadata, provenance and licence information. | APPROVED | PO-source | DR-014 |
| PR-137 | Preserve original Unicode and source text where legally permitted. | APPROVED | PO-source | DR-015 |
| PR-138 | Do not assume a source is trustworthy merely because it is widely used; do not assume a licence without evidence; freely accessible is not open. | APPROVED | PO-corpus, PO-source | DR-026 |
| PR-139 | Do not silently resolve conflicting editions. | APPROVED | PO-source | DR-018 |
| PR-140 | Licensing policy: explicitly permitted → permitted (with conditions); explicitly prohibited → prohibited; silent/unknown → UNKNOWN, pending review; conflicting → more restrictive; unresolved rights never become shared/public evidence; RiseWise never claims silence means permission. **RiseWise conservative product policy, not legal advice.** | APPROVED | PO-C009 | DR-026, DR-027 |
| PR-141 | Verification rules and source updates (original RiseWise scope, carried forward). | APPROVED | PO-brief (history) | DR-016 |

## 15. No-Substitution Principle

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-150 | When a desired corpus is unavailable, show NOT_AVAILABLE rather than using an unverified substitute. | APPROVED | PO-corpus | DR-019 |
| PR-151 | Do not treat a translation as the original text, or commentary as the original text. | APPROVED | PO-source | DR-013, DR-019 |
| PR-152 | Full substitution list (no translation, commentary, other recension, unaccented text, unverified OCR, unclear-licence copy, or LLM recollection) as ADR-0010. | APPROVED | SM-v0.1 (approved) | DR-019 |

## 16. Uncertainty / Insufficient Evidence Behaviour

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-160 | The user must see what remains uncertain (PR-041). | APPROVED | PO-approval-1 | DR-002 |
| PR-161 | The model must support "we don't have this source" honestly. | APPROVED | PO-source | DR-021 |
| PR-162 | INSUFFICIENT_EVIDENCE is a valid outcome (PR-090), including when a corpus is unavailable. | APPROVED | PO-brief | DR-003, DR-019 |
| PR-163 | Confidence is shown as qualitative bands (LOW / MEDIUM / HIGH), never numeric scores. | PROVISIONAL | Claude-rev1, Claude-rev2 | DR-008 |
| PR-164 | Corpus unavailability is reported at the start of an inquiry. | PROVISIONAL | Claude-rev1 | — |

## 17. Local-First / Open-Source Direction

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-170 | Local-first / open-source preference. | APPROVED | PO-brief (history) | — |
| PR-171 | Fully offline operation with a local LLM (Ollama) by default; cloud providers opt-in. | PROVISIONAL | Claude-rev1, Claude-rev2 | DR-008, DR-009 |
| PR-172 | Technology choices (TypeScript, React/Vite, Fastify, Zod, SQLite/Postgres). *(Implementation choices, not requirements.)* | PROVISIONAL | Claude-rev2 | DR-008 |
| PR-173 | Code licence. | OPEN | — | DR-042 |
| PR-174 | Whether any cloud LLM provider is allowed, and which. | OPEN | Claude-rev2 decision D2 | DR-009 |

## 18. Public/Tiered Product Direction

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-180 | The architecture must allow public/free tiers and potentially paid professional/enterprise tiers. (A design constraint, not a commitment to launch tiers.) | APPROVED | PO-source | DR-010, DR-025 |
| PR-181 | Whether and when tiers are offered; commercial intent. | OPEN | — | DR-010 |
| PR-182 | Rights mapping per tier, required uses per context, excerpt limits. | OPEN | — (requires legal review) | DR-030 |
| PR-183 | Until PR-182 is decided, NC and scholarly-only material is USER_IMPORT_ONLY in hosted or paid contexts. | PROVISIONAL | SM-v0.1 (temporary default) | DR-029 |

## 19. Privacy and User-Supplied Sources

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-190 | A user may provide their own legitimately obtained source through a private USER_SUPPLIED pathway, subject to the user's own rights and workspace restrictions. | APPROVED | PO-C009 | DR-028 |
| PR-191 | User-supplied and internal-only content stays in its workspace and is not shared, redistributed or externally processed without explicit user consent. | APPROVED | SM-v0.1 (approved) | DR-024 |
| PR-192 | MVP deployment: local-only single user vs hosted demo; authentication scope. | OPEN | Claude-rev2 decision D3 | DR-009 |
| PR-193 | Whether non-open text may be sent to external processors. | OPEN | — (requires legal review) | DR-031 |

## 20. Evaluation Requirements

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-200 | An Evaluation Framework is part of RiseWise (continuing the v0.2/v0.3 evaluation-check approach). | APPROVED | PO-brief | DR-001, DR-005 |
| PR-201 | Evaluation layers (invariant checks, golden cases, adversarial cases, LLM-mode metrics such as unsupported-fact rate = 0) and a release gate. | PROVISIONAL | Claude-rev1 | — |
| PR-202 | Evaluation must check that "Challenge this conclusion" does not manufacture counterarguments. | PROVISIONAL | Claude-rev1 (follows from PR-073) | DR-002 |
| PR-203 | Recover or replace the v0.3 31-check list. | OPEN | — | DR-005 |

## 21. Security / Integrity Principles

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-210 | LLM output is never a source. | APPROVED | PO-source, SM-v0.1 | DR-017 |
| PR-211 | Source-layer integrity and security controls: content hashes, safe import, source text treated as untrusted data for LLMs, rights checks at every exit, append-only audit. | APPROVED | SM-v0.1 (approved; architecture §19) | DR-023 |
| PR-212 | Never request, display, commit or hard-code secrets. | PROVISIONAL | Claude-rev1 (standard practice; not stated by PO for RiseWise) | — |
| PR-213 | No open-web retrieval and no LLM tool use in the MVP. | PROVISIONAL | Claude-rev1 | DR-008 |

## 22. Explicit Non-Goals for the Current Phase

| ID | Requirement | Status | Source | DR |
|---|---|---|---|---|
| PR-220 | Current phase is documentation only. Not yet: database schemas, TypeScript types, Zod schemas, migrations, source ingestion, corpus downloads, scraping, Tarka, LLM integration, embeddings, UI, authentication/tiers, billing, additional technology choices; no resolving scholarly questions without evidence; no resolving legal questions. | APPROVED | PO-steps | DR-007 |
| PR-221 | Other domain adapters are out of MVP scope (PR-101). | APPROVED | PO-approval-1 | DR-004 |
| PR-222 | MVP excludes team auth, open-web retrieval, embeddings and Sanskrit morphological analysis. | PROVISIONAL | Claude-rev1 | DR-008 |

## 23. Requirements Still Requiring Product Decisions

Consolidated list of OPEN items above, plus related open decisions:

| ID | Decision needed | DR |
|---|---|---|
| PR-013 | Target users, personas, primary use cases | DR-060 |
| PR-044 / PR-093 | Status definitions and thresholds | DR-003 |
| PR-082 | Meaning of EVIDENCE as an epistemic kind | DR-058 |
| PR-083 | Human review before FACT? | DR-003 |
| PR-114 | Vedic corpora and editions (blocked by licensing) | DR-033–DR-037 |
| PR-122 | GENERAL domain scope | DR-061 |
| PR-133 | First-party corpus strategy | DR-043, DR-044 |
| PR-173 | Code licence | DR-042 |
| PR-174, PR-192 | Cloud LLM provider; deployment target | DR-009 |
| PR-181, PR-182 | Commercial intent; tier rights mapping (legal review) | DR-010, DR-030 |
| PR-193 | External processing of non-open text (legal review) | DR-031 |
| PR-203 | v0.3 evaluation checks | DR-005 |
| — | Expert reviewer availability | DR-048 |
| — | Technical stack (proposal awaiting approval) | DR-008 |
