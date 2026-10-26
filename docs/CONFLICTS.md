# Conflicts log

Contradictions between requirements, design decisions, or sources. **Product behaviour is never changed silently**: every contradiction is recorded here with its current handling. Open items block nothing in Step 1 (documentation) but must be resolved, or explicitly deferred, before the affected area is implemented.

| ID | Area | Status |
|---|---|---|
| C-001 | Availability states: requirement vs design | Resolved (approved with Source Model v0.1) |
| C-002 | "EVIDENCE" as both an epistemic kind and an entity | Open |
| C-003 | Terminology: "Source", "Manifest", "Version" | Resolved (mapping recorded) |
| C-004 | VedaWeb translation licences vs underlying rights | Open |
| C-005 | DCS licence version: 3.0 vs 4.0 | Open |
| C-006 | Taittirīya Saṃhitā: TITUS terms vs Sanskrit Library CC licence | Open |
| C-007 | Ambuda: permissive intent vs missing licence metadata | Open |
| C-008 | ashtadhyayi.com: informal permission vs undocumented upstream editions | Open |
| C-009 | How a silent upstream term combines with the most-restrictive rule | Open — **resolve before schema design** |

---

## C-001 — Availability states: requirement vs design

- **Requirement:** availability states `AVAILABLE`, `PARTIAL`, `LICENCE_PENDING`, `SCAN_ONLY`, `USER_SUPPLIED`, `NOT_AVAILABLE`.
- **Design:** these mix three dimensions (holding, rights, origin). The design stores Holding / Origin / Coverage / reason codes, computes the access class, and **derives** display labels; it adds `REFERENCE_ONLY` and `IMPORT_REQUIRED`; `USER_SUPPLIED` becomes an origin badge.
- **Resolution:** accepted by the product owner with Source Model v0.1 (ADR-0007). All six original labels remain available in the UI vocabulary.

## C-002 — "EVIDENCE" as both an epistemic kind and an entity

- **Requirement:** epistemic kinds include `EVIDENCE` alongside `FACT`, `INFERENCE`, etc.; the reasoning chain also has an "Evidence" step.
- **Design:** evidence is modelled as a *link* (EvidenceAnchor → passage span) used by claims. The architecture proposal (rev. 1) suggested `EVIDENCE` as a kind label for statements that directly report what a source says.
- **Status:** open. Belongs to Tarka design; does not affect the source model, which only provides EvidenceAnchor. Needs a definition before Tarka schema work.

## C-003 — Terminology: "Source", "Manifest", "Version"

- **Requirement wording:** "Source", "Version", "Manifest" listed as concepts; "Source vs Claim" as a distinction.
- **Design mapping:** *Source* = a concrete representation of an Edition (digital text, scan, print reference). *Version* = SourceSnapshot (content) plus append-only revisions (metadata, licence, provenance). *Manifest* = embedded in Acquisition. Claims are not part of the source model.
- **Resolution:** mapping recorded here and in source-model.md §3. UI copy may use "source" loosely, but APIs and schemas use the defined meanings.

## C-004 — VedaWeb translation licences vs underlying rights

- **Observation [V]:** VedaWeb's TEI header labels all its translation layers CC BY-NC-SA 4.0, including translations based on old editions (e.g. Griffith 1890 [V]) and on a modern reprint (Geldner, Harvard Oriental Series 63, 2003 [V]).
- **Conflict:** for old editions, the underlying work may be public domain [K] while the digital representation is NC-SA. For the Geldner layer, the rights of the 2003 publisher edition relative to VedaWeb's CC label are unclear.
- **Current handling:** record both licence layers; effective rights take the most restrictive. The Geldner layer is treated as `LICENCE_PENDING` until upstream rights are confirmed. The public-domain underlying work enables a future first-party transcription route (source-model.md §18).

## C-005 — DCS licence version: 3.0 vs 4.0

- **Observation [S]:** the DCS website states CC BY 3.0; the data repository states CC BY 4.0.
- **Current handling:** both are permissive, attribution-only licences; record both statements as licence evidence and mark `verificationStatus: DISPUTED` until confirmed with the maintainer or by reading the repository licence file directly.

## C-006 — Taittirīya Saṃhitā: TITUS terms vs Sanskrit Library CC licence

- **Observation [S]:** the Sanskrit Library's TS (derived from TITUS data) is offered under CC BY-NC-SA 3.0, which permits non-commercial redistribution. TITUS's own terms allow free scholarly use with citation, prohibit commercial use, and do not state a redistribution licence. GRETIL lists the TITUS TS as a restricted download.
- **Conflict:** the downstream grant (redistribution allowed) may exceed what the upstream terms grant.
- **Current handling:** `LICENCE_PENDING` in all contexts (example 02). Resolution requires written confirmation from the Sanskrit Library and/or TITUS (OQ-L10).

## C-007 — Ambuda: permissive intent vs missing licence metadata

- **Observation [S]:** Ambuda states a permissive / public-domain intent, but its metadata export lacks per-text licence fields.
- **Current handling:** any Ambuda text is `LICENCE_PENDING` until per-text licence evidence exists. Vedic and grammar coverage is also unconfirmed (OQ-V14).

## C-008 — ashtadhyayi.com: informal permission vs undocumented upstream editions

- **Observation [V]:** the data README says "free to use … provided that appropriate credits are mentioned"; there is no formal licence, and the editions from which commentaries were typed are not documented.
- **Current handling:** `LICENCE_PENDING` (example 03). Needs written permission and edition provenance (OQ-L11).

## C-009 — How a silent upstream term combines with the most-restrictive rule

- **Design rules in tension:** (a) effective rights take the most restrictive value per term across all licence records and upstream constraints; (b) any `UNKNOWN` term ⇒ `LICENCE_PENDING`.
- **Problem found in the paper test:** an upstream notice often states only some terms (e.g. van Nooten–Holland: "research, not commercial" [S]; TITUS: "scholarly use, no commercial" [S]) and is silent on redistribution or derivatives. If a silent upstream term counts as `UNKNOWN`, almost every derived source (including all VedaWeb Ṛgveda text layers) becomes `LICENCE_PENDING`. If it counts as "no additional restriction", RiseWise relies on the downstream provider having had the right to grant what it grants.
- **Current handling:** examples 01 and 02 show both outcomes. Nothing is evidence-eligible until this is decided.
- **Needs:** a product/legal decision (OQ-L12) and then a precise rule in the rights policy, before schema design.
