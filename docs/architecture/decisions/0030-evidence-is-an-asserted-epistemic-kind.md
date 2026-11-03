# ADR-0030: EVIDENCE is an asserted epistemic kind

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-074
- **Product owner decision:** option P2-A1 explicitly selected (P2 product-semantics study, 2026-11-03)
- **Resolves:** DR-058 and C-002 at the semantic level (PR-082); the exact evidence-relationship representation remains open
- **Related:** DR-003, DR-017 (ADR-0009), DR-022, DR-067 (ADR-0023), DR-069 (ADR-0025), DR-070 (ADR-0026), DR-071, DR-072, DR-073 (ADR-0029), ADR-0003, ADR-0008, ADR-0019, PR-040, PR-041, PR-050, PR-051, PR-053, PR-054, PR-080, PR-082, PR-090 … PR-093

## Context
DR-003 and PR-080 approve `EVIDENCE` as one of Tarka's six epistemic kinds. The source model separately provides the EvidenceAnchor: a value object identifying one exact cited textual selection in one SourceSnapshot (DR-067), whose structural validity is not evidential sufficiency (DR-070). Approved requirements also need Tarka to show which evidence supports and which contradicts a claim (PR-041, PR-071), down to the exact passage (PR-051), and place "evidence" between inference and passage in the trace (PR-050).

How the kind `EVIDENCE` relates to EvidenceAnchors and evidence links was open (DR-058, PR-082, C-002). C-002 recorded that the architecture proposal (rev. 1) had suggested `EVIDENCE` as a kind label for statements that directly report what a source says; that suggestion was never approved. DR-073 / ADR-0029 has since established that `FACT` is an asserted epistemic kind, not a status or verdict.

The product owner was asked to choose between four interpretations (P2-A kind, P2-B relationship, P2-C kind and relationship as parallel representations, P2-D argument role) and, within A, between an asserted kind (A1) and a kind that requires an eligible anchor (A2). The product owner selected **A1**.

## Decision
`EVIDENCE` is an **asserted epistemic kind** describing a proposition that reports or represents what a source says or contains. `EVIDENCE` does not by itself establish that the reported proposition is true, authoritative, relevant, sufficient, or supportive of any claim. Its grounding in source material and its relationship to a claim are represented separately.

## Semantic definition
1. **A kind, not a verdict.** `EVIDENCE` classifies a proposition as a report or representation of what a source says or contains (for example, "Source S states that P"). It is not an evidence-strength verdict.
2. **Asserted, not gated.** Assigning the kind does not require that the proposition has an eligible EvidenceAnchor or has passed evidence eligibility (DR-022). Grounding, structural validity, eligibility, sufficiency and status are separate dimensions, each evaluated on its own terms.
3. **Not status.** `EVIDENCE` does not determine claim status. Evidence and verification rules determine status (DR-003, PR-032).
4. **Report ≠ reported content.** An `EVIDENCE` proposition "Source S states that P" is not the proposition P. Whether, and how, it bears on a claim about P is represented by the evidence-to-claim relationship and assessed by Tarka's rules.

## Relationship to EvidenceAnchor
- The EvidenceAnchor remains exactly as governed by DR-067 / ADR-0023, DR-069 / ADR-0025 and DR-070 / ADR-0026: the exact textual selection, a value object. This ADR does not change it.
- The grounding of an `EVIDENCE` proposition in source material is represented separately, through the source and provenance structures and the EvidenceAnchor. The `EVIDENCE` kind is not the anchor, the passage or the source.
- Structural validity of an EvidenceAnchor remains distinct from evidential sufficiency (DR-070).

## Relationship to evidence-to-claim polarity
- The relationship between evidential material and a claim is represented separately from the `EVIDENCE` kind.
- Supporting / contradicting polarity belongs to that evidence-to-claim relationship, **not** to the EvidenceAnchor. (An anchor is a value object without identity, DR-067; the same selection may bear on different claims differently.)
- There is one evidence-to-claim relationship concept. This ADR does not create a second, parallel evidential representation. Its exact representation — what it connects, its entity form, its cardinality and any polarity values beyond supporting and contradicting — is a Tarka architecture (GAP-1) decision.

## Semantic chain
Semantic and provenance relationships only; this is **not** a database schema:

```text
Source
  ↓
SourceSnapshot
  ↓
Passage
  ↓
EvidenceAnchor
  ↓
EVIDENCE proposition
  ↓
Evidence relationship to Claim
  ↓
Status computation
```

## Explicit non-equivalences
`EVIDENCE` is **not**:
- true, proven or established;
- authoritative (authority is separate: ADR-0008, DR-049);
- relevant to a claim;
- sufficient;
- `SUPPORTED` or any other status;
- source verification (source verification states are separate from Tarka kinds and statuses: ADR-0008, PR-092, source-model.md §3);
- the EvidenceAnchor, the passage or the source.

A verified source does not make a claim `SUPPORTED` (source-model.md §3). An `EVIDENCE` proposition can exist without being sufficient to establish the claim it concerns.

## Rejected alternatives

| Alternative | Why not chosen |
|---|---|
| P2-A2 — `EVIDENCE` only for propositions grounded in an eligible EvidenceAnchor | Would make the kind an earned or gated standing and merge it with eligibility; inconsistent with the asserted-kind pattern of DR-073 |
| P2-B — `EVIDENCE` is only the claim ↔ EvidenceAnchor relationship | `EVIDENCE` is an approved epistemic kind (DR-003, PR-080); redefining it as only a relationship would conflict with approved governance |
| P2-C — `EVIDENCE` both as an independent kind and as a second, equivalent evidential representation duplicating the claim ↔ anchor relationship | Would create two parallel meanings and routes for the same evidence, which could diverge in the Why trace |
| P2-D — `EVIDENCE` as an argument or evidential role | Would blur the distinction between epistemic kind, evidential relationship, sufficiency and claim status |

## Consequences
- `EVIDENCE` remains one of the six approved epistemic kinds, with a defined meaning.
- DR-058, PR-082 and C-002 are resolved at the semantic level; the evidence-relationship representation remains open for Tarka architecture.
- A future "Why?" trace must be able to distinguish: the `EVIDENCE` proposition; the exact EvidenceAnchor / source passage grounding it; the relationship between that evidence and a claim; and the independently computed claim status. The trace UI and schema are not defined here.
- DR-073 is unchanged: `FACT` remains an asserted epistemic kind, not `SUPPORTED`, established truth, proof or evidential sufficiency.
- No LLM authority is added. LLM output is not a source (DR-017); LLM-generated content does not automatically become evidence; an LLM does not set status (DR-003); an LLM interpretation is not source evidence (PR-053).

## Explicitly deferred questions
This ADR does **not** decide:
- whether `FACT` and `EVIDENCE` (or any kinds) may coexist on one reasoning object; kind exclusivity;
- the evidence-relationship representation: what it connects, entity form, cardinality, polarity values beyond supporting and contradicting, and how grounding is represented;
- the meaning of `INFERRED` (P3);
- initial `UNVERIFIED` and its distinction from `INSUFFICIENT_EVIDENCE` (P4);
- whether and how an LLM may locate source passages, propose EvidenceAnchors, propose `EVIDENCE` propositions, propose evidence relationships or their polarity, or receive human confirmation (P5);
- the treatment of unsourced GENERAL model knowledge (P6); existing governance remains authoritative: model knowledge is not evidence (DR-017, DR-061);
- the relationship between the Source Model `Interpretation` entity, the Tarka `INTERPRETATION` kind, source commentary, Tarka-generated interpretations and the evidential status of interpretations (P7);
- status meanings, thresholds and propagation; evidence sufficiency; authority and contradiction weighting; human review; the FACT path; LLM-origin evidence eligibility; inference semantics; circularity rules; the reasoning-record schema (GAP-1b and GAP-1);
- unavailable or unverifiable evidence (OQ-E21);
- any schema, type, storage, API, UI or runtime behaviour.

## Cross-references

| Decision | Relationship |
|---|---|
| DR-003, PR-080 | `EVIDENCE` remains an approved kind; its meaning is now defined |
| DR-058, PR-082, C-002 | Resolved at the semantic level; relationship representation open |
| DR-073 / ADR-0029 | Same asserted-kind pattern; `FACT` unchanged; coexistence not decided |
| DR-067 / ADR-0023 | EvidenceAnchor unchanged; polarity is not a property of the anchor |
| DR-069 / ADR-0025, DR-070 / ADR-0026 | Unchanged; structural facts and structural validity are not evidential sufficiency |
| DR-071, DR-072 | Unchanged |
| DR-022, source-model.md §22 | Eligibility gate unchanged and separate from the kind |
| ADR-0008, PR-092, source-model.md §3 | Source verification remains separate from Tarka kinds and statuses |
| DR-017 / ADR-0009, PR-053, ADR-0019 | LLM boundary unchanged |
| ADR-0003, source-model.md §3 Interpretation | Unchanged; the mapping to Tarka is deferred (P7) |
| PR-040, PR-041, PR-050, PR-051 | Served by keeping evidence, relationship (with polarity) and status distinct |
| PR-090 … PR-093 | No status defined or changed |
