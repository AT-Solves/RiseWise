# ADR-0032: UNVERIFIED and INSUFFICIENT_EVIDENCE claim statuses

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-076
- **Product owner decision:** P4 decision explicitly approved (P4 product-semantics study, 2026-11-03)
- **Related:** DR-003, DR-014, DR-017 (ADR-0009), DR-019 (ADR-0010), DR-021, DR-022, DR-028, DR-073 (ADR-0029), DR-074 (ADR-0030), DR-075 (ADR-0031), ADR-0008, PR-031, PR-032, PR-090 … PR-093, PR-160 … PR-163, OQ-E21

## Context
DR-003 and PR-090 approve seven claim/conclusion statuses, including `UNVERIFIED` and `INSUFFICIENT_EVIDENCE`. The only governing text for `UNVERIFIED` is DR-003's application rule: LLMs may propose "candidate claims, labelled UNVERIFIED". `INSUFFICIENT_EVIDENCE` is established as an honest outcome: "a valid outcome …, including when a corpus is unavailable" (PR-162); "Allowed: INSUFFICIENT_EVIDENCE outcomes" (DR-019); "Some questions will honestly end with insufficient evidence" (ADR-0010); "the honest outcome is insufficient evidence for claims that depend on it" (source-model.md §22).

The token `UNVERIFIED` is also used in the Source Model for other concepts: the derived source-verification state (§8: `UNVERIFIED` → `INTEGRITY_CHECKED` → `HUMAN_VERIFIED` → `EXPERT_VERIFIED`), `LicenceRecord.verificationStatus` (§7), and the licence of a `USER_SUPPLIED` source (DR-028, §7 R6). The concepts are already kept apart (source-model.md §3; §8 "Verification concerns source fidelity and integrity, not truth"; ADR-0008; PR-092), but the shared token is not addressed. DR-075 records that `INFERRED` does not mean `UNVERIFIED` and leaves P4 open.

DR-003 and PR-032 also say that "evidence and verification rules" determine a claim's status, while "verification" elsewhere names source fidelity and integrity checks.

## Problem
Without a definition, claim-status `UNVERIFIED` could be read as "not yet evaluated", "insufficient evidence", "LLM-generated", "source-unverified", "untrusted provenance" or "truth unknown". Several of these readings would derive status from origin (contrary to DR-003 and ADR-0008), duplicate `INSUFFICIENT_EVIDENCE`, or confuse source verification with claim status (contrary to PR-092). The boundary between `UNVERIFIED` and `INSUFFICIENT_EVIDENCE` needs to be explicit.

## Decision
- **`UNVERIFIED`** is a claim/conclusion status indicating that status evaluation has not yet been completed.
- **`INSUFFICIENT_EVIDENCE`** is an evaluation outcome indicating that the evidence available to the evaluation is insufficient to establish the claim's evidential standing.
- `UNVERIFIED` and `INSUFFICIENT_EVIDENCE` are distinct.

## UNVERIFIED
1. **Meaning.** Status evaluation of the claim or conclusion has not yet been completed.
2. **Origin-neutral.** The status applies independently of who or what proposed the claim (an LLM, a person, a rule or another mechanism).
3. **The LLM rule is an application.** DR-003's rule that LLM candidate claims are labelled `UNVERIFIED` remains in force and is an application of this status, not its definition. An LLM-proposed claim is initially `UNVERIFIED` because it has not yet been evaluated, not because it came from an LLM.
4. **Not:** an origin marker; an LLM-origin marker; a provenance judgment; a source-verification state; a licence-verification state; a truth judgment; a confidence level; a synonym for `INSUFFICIENT_EVIDENCE`. It does not mean untrusted, false, uncertain or unsupported.

## INSUFFICIENT_EVIDENCE
1. **Meaning.** An evaluation outcome: the evidence available to the evaluation is insufficient to establish the claim's evidential standing.
2. **Not defined as:** "truth is unknown"; "the claim is false"; "the claim is weak"; "the claim has no evidence"; "the source is unavailable"; "the claim is less supported than another status".
3. **Existing cases preserved.** PR-162, DR-019, ADR-0010 and source-model.md §22 remain in force: `INSUFFICIENT_EVIDENCE` is a valid outcome, including when a corpus is unavailable. Unavailability is one situation in which the evidence available to an evaluation can be insufficient; it is not the definition.
4. **No ordering.** No ordering of statuses is introduced (consistent with DR-075).

## Conceptual distinction (not a lifecycle)
- Before status evaluation is completed, a claim is `UNVERIFIED`.
- After status evaluation, a claim has an applicable evaluation outcome, which may be `INSUFFICIENT_EVIDENCE`.

This is semantic governance only. It does **not** decide whether every evaluation replaces `UNVERIFIED` with exactly one other status, when evaluation begins or ends operationally, or any transition lifecycle; status coexistence and lifecycle remain ungoverned.

## Semantic layers of the token UNVERIFIED
The following are different concepts in different layers. No field is renamed and no schema change is made; the contextual phrases are prose distinctions only.

| Prose term | Meaning | Layer | Governed by |
|---|---|---|---|
| claim-status `UNVERIFIED` | Status evaluation not yet completed | Tarka reasoning | DR-003, PR-090, this ADR |
| source-verification `UNVERIFIED` | No source fidelity/integrity check has passed for the target | Source Model | source-model.md §8, ADR-0008 |
| licence-verification `UNVERIFIED` | A licence statement (or user attestation) has not been confirmed | Source Model (licensing) | source-model.md §7 (`LicenceRecord.verificationStatus`), DR-028, ADR-0012 R6 |

Source and licence verification do not set claim status (source-model.md §3, PR-092, ADR-0008). They affect evidence eligibility through the gate (DR-022: G1 requires an `INTEGRITY_HASH` pass; G2 applies rights; G3 workspace), and eligibility is distinct from status. Lower-case "unverified" in ordinary product prose (e.g. "unverified OCR", "unverified substitute", "unverified upstream claims") is not reinterpreted by this ADR.

## "Verification rules" in claim-status statements
When DR-003 and PR-032 say that "evidence and verification rules" determine a claim's status, "verification rules" refers to the rules used to evaluate claim status and evidential standing. It does not make a Source Model source-verification state (§8) a claim status, and it does not equate source verification with claim status computation. Source verification — including §8 checks and the domain verification rules of extensions (e.g. VR-101 … VR-105, used by gate G4) — remains a Source Model concern whose effect on reasoning is through evidence eligibility. The historical wording of DR-003 and PR-032 is retained unchanged.

## Alternatives considered (P4 study)

| Alternative | Why not chosen |
|---|---|
| `UNVERIFIED` = not yet sufficient evidence | Duplicates `INSUFFICIENT_EVIDENCE` |
| `UNVERIFIED` = truth or standing not established | Duplicates `INSUFFICIENT_EVIDENCE`, `PARTIALLY_SUPPORTED` and `CONTESTED`; appeals to truth, contrary to §8 and the pattern of DR-073 |
| `UNVERIFIED` = untrusted provenance or origin | Derives status from provenance, contrary to DR-003 and ADR-0008 |
| `UNVERIFIED` = LLM-generated | Derives status from origin, contrary to DR-003, ADR-0008 and DR-075; leaves human claims undefined |
| `UNVERIFIED` = workflow label outside status computation | Would reinterpret an approved status as a non-status |
| `INSUFFICIENT_EVIDENCE` defined as "cannot support a stronger status" | Implies a status ordering |

## Consequences
**Positive**
- Separates the evaluation state (`UNVERIFIED`) from an evaluation outcome (`INSUFFICIENT_EVIDENCE`).
- Removes the LLM-origin reading of `UNVERIFIED`; human-authored claims are covered by the same status.
- Prevents source- or licence-verification `UNVERIFIED` from being read as claim status.
- Preserves "we don't have this source" / insufficient-evidence behaviour (PR-161, PR-162, DR-019, ADR-0010).
- Leaves status-engine mechanics open.

**Constraints**
- Implementation must later define evaluation rules and any transitions.
- UI and traces must eventually distinguish claim-status `UNVERIFIED` from source- and licence-verification `UNVERIFIED`, and `UNVERIFIED` from `INSUFFICIENT_EVIDENCE`.
- Source and licence verification must remain separate from claim status.
- DR-073, DR-074 and DR-075 are unchanged.

## Non-decisions
This ADR does **not** decide: the status transition lifecycle; when evaluation begins or ends operationally; whether status is run-relative or globally persisted; the status persistence model; whether statuses are mutually exclusive; whether `INFERRED` can coexist with another status, including its interaction with `UNVERIFIED` and `INSUFFICIENT_EVIDENCE`; evidence, support and contradiction thresholds (PR-044, PR-093); unavailable-corpus transition rules and the treatment of unavailable or unverifiable evidence (OQ-E21); partial-evaluation rules; status propagation; confidence semantics (PR-163 remains provisional); uncertainty semantics; a status reason-code schema; storage, API and UI representation; the status-engine implementation; Claim vs Statement; the evidence-relationship representation; LLM evidence-link proposal rights (P5); unsourced GENERAL knowledge (P6); Source Interpretation vs Tarka `INTERPRETATION` (P7); E18 composite EvidenceAnchor serialisation; E17 exact SourceSnapshot hash framing; ingestion and segmentation architecture; any renaming of `UNVERIFIED` tokens.

## Cross-references

| Decision | Relationship |
|---|---|
| DR-003 | Wording unchanged; LLM candidates labelled `UNVERIFIED` is an application; "verification rules" clarified for claim status |
| PR-032 | Wording unchanged; "verification rules" clarified |
| PR-090, PR-091 | `UNVERIFIED` and `INSUFFICIENT_EVIDENCE` meanings now defined; other statuses not defined |
| PR-093, PR-044 | Remain open |
| PR-162, DR-019, ADR-0010, source-model.md §22 | Preserved: `INSUFFICIENT_EVIDENCE` is valid, including when a corpus is unavailable |
| PR-161, DR-021 | Preserved |
| DR-075 / ADR-0031 | Unchanged; `INFERRED` ≠ `UNVERIFIED`; coexistence open |
| DR-073, DR-074 | Unchanged |
| source-model.md §3, §7, §8; ADR-0008; PR-092; DR-028 | Source- and licence-verification `UNVERIFIED` unchanged and separate |
| DR-022 | Unchanged; verification affects eligibility, not status |
| DR-014, source-model.md §3 (CorpusState) | Unchanged; run-relativity of status not decided |
| DR-017 / ADR-0009 | Unchanged |
