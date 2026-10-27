# Conflicts log

Cross-project index: [`DECISION_REGISTER.md`](DECISION_REGISTER.md) — new conflicts and questions must also be considered for the register.

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
| C-009 | How a silent upstream term combines with the most-restrictive rule | Resolved (ADR-0012, 2026-10-26) |
| C-010 | "Stored exactly as received" vs Unicode scalar offsets | Resolved (ADR-0021, 2026-10-27) |
| C-011 | `ROOT_TEXT` used as layer, designation and authority tier | Resolved (ADR-0020, 2026-10-27); tier rename deferred to DR-049 |
| C-012 | ADR-0002 implied mandatory locus mappings | Resolved (ADR-0016, 2026-10-27) |

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
- **Current handling (ADR-0012 R3/R4):** record both licence layers; the more restrictive interpretation applies. All VedaWeb translation layers, including Griffith and Geldner, are `LICENCE_PENDING` for shared/public use until upstream rights are confirmed. The public-domain underlying work enables a future first-party transcription route (source-model.md §18).

## C-005 — DCS licence version: 3.0 vs 4.0

- **Observation [S]:** the DCS website states CC BY 3.0; the data repository states CC BY 4.0.
- **Current handling (ADR-0012 R4):** record both statements as licence evidence, mark `verificationStatus: DISPUTED`, and apply the more restrictive reading term by term until confirmed with the maintainer. Separately, DCS base texts come from various upstream editions whose terms are undocumented, so DCS text remains `LICENCE_PENDING` for shared use under R3.

## C-006 — Taittirīya Saṃhitā: TITUS terms vs Sanskrit Library CC licence

- **Observation [S]:** the Sanskrit Library's TS (derived from TITUS data) is offered under CC BY-NC-SA 3.0, which permits non-commercial redistribution. TITUS's own terms allow free scholarly use with citation, prohibit commercial use, and do not state a redistribution licence. GRETIL lists the TITUS TS as a restricted download.
- **Conflict:** the downstream grant (redistribution allowed) may exceed what the upstream terms grant.
- **Current handling (ADR-0012 R3/R4):** the more restrictive (upstream) reading applies and redistribution is `UNKNOWN` ⇒ `LICENCE_PENDING` for shared/public use (example 02). Resolution requires written confirmation from the Sanskrit Library and/or TITUS (OQ-L10).

## C-007 — Ambuda: permissive intent vs missing licence metadata

- **Observation [S]:** Ambuda states a permissive / public-domain intent, but its metadata export lacks per-text licence fields.
- **Current handling:** any Ambuda text is `LICENCE_PENDING` until per-text licence evidence exists. Vedic and grammar coverage is also unconfirmed (OQ-V14).

## C-008 — ashtadhyayi.com: informal permission vs undocumented upstream editions

- **Observation [V]:** the data README says "free to use … provided that appropriate credits are mentioned"; there is no formal licence, and the editions from which commentaries were typed are not documented.
- **Current handling:** `LICENCE_PENDING` (example 03). Needs written permission and edition provenance (OQ-L11).

## C-009 — How a silent upstream term combines with the most-restrictive rule

- **Design rules in tension:** (a) effective rights take the most restrictive value per term across all licence records and upstream constraints; (b) any `UNKNOWN` term ⇒ `LICENCE_PENDING`.
- **Problem found in the paper test:** an upstream notice often states only some terms (e.g. van Nooten–Holland: "research, not commercial" [S]; TITUS: "scholarly use, no commercial" [S]) and is silent on redistribution or derivatives. If a silent upstream term counts as `UNKNOWN`, almost every derived source (including all VedaWeb Ṛgveda text layers) becomes `LICENCE_PENDING`. If it counts as "no additional restriction", RiseWise relies on the downstream provider having had the right to grant what it grants.
- **Resolution (2026-10-26):** product owner adopted a conservative rule — *silence is not permission*. A silent or unknown term is `UNKNOWN` and pending review; conflicting statements take the more restrictive interpretation; unresolved rights never become shared/public evidence; users may use their own copies via the private `USER_SUPPLIED` pathway. Recorded in ADR-0012 and source-model.md §7.1. **This is RiseWise's conservative product policy, not legal advice.**
- **Effect:** all real VedaWeb Ṛgveda layers and the Sanskrit Library TS remain `LICENCE_PENDING` for shared/public use (source-model.md §22.6; examples 01, 02).

## C-010 — "Stored exactly as received" vs Unicode scalar offsets

- **Conflict:** ADR-0005 stores passage text "exactly as received"; DR-052 counts evidence offsets in Unicode scalar values over the stored `original`. Acquired material that is not valid Unicode cannot satisfy both.
- **Resolution (2026-10-27):** [ADR-0021](architecture/decisions/0021-acquired-bytes-and-decoded-passage-text.md) amends ADR-0005. Acquired bytes are preserved and hashed as the original artifact; Passage `original` is the faithful decoded Unicode text with the decoding recorded as provenance; undecodable material is quarantined, never replaced with U+FFFD. Unicode offsets are not byte offsets.

## C-011 — `ROOT_TEXT` used as layer, designation and authority tier

- **Conflict:** "Root text" appeared as a layer type (example 03 `layer: ROOT_TEXT`), as an authority tier (`ROOT_TEXT_EDITION`, source-model.md §11g), and — after DR-057 — as a reviewed designation.
- **Resolution (2026-10-27):** [ADR-0020](architecture/decisions/0020-root-text-designation.md) separates the three. `ROOT_TEXT` is only the reviewed designation (Relation `DESIGNATED_ROOT_TEXT_FOR`). Example 03's layer is withdrawn (layer type open: DR-066). `ROOT_TEXT_EDITION` overlaps with the designation; it is retained for now and must not be read as a designation; rename or removal is decided under DR-049.

## C-012 — ADR-0002 implied mandatory locus mappings

- **Conflict:** ADR-0002 said edition-specific schemes "are aligned to work-level ones by mappings"; DR-053 allows mappings only where genuinely established, explicit, typed and provenance-bearing. Example 03 contained an unexplained `EXACT` `sk.num` → `asht.aps` mapping.
- **Resolution (2026-10-27):** [ADR-0016](architecture/decisions/0016-citation-scheme-scope-and-locus-mappings.md) amends ADR-0002; mappings are constrained Relations `LOCUS_MAPS_TO` with type, basis and provenance. Example 03's mapping is marked unresolved.
