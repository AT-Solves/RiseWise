# ADR-0031: INFERRED as a derivation status

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-075
- **Product owner decision:** refined Candidate 3 of the P3 product-semantics study explicitly selected (2026-11-03)
- **Related:** DR-002, DR-003, DR-014, DR-017 (ADR-0009), DR-073 (ADR-0029), DR-074 (ADR-0030), ADR-0008, PR-022, PR-040, PR-041, PR-044, PR-050, PR-090 … PR-093, PR-160 … PR-163

## Context
DR-003 and PR-090 approve seven claim/conclusion statuses, one of which is `INFERRED`, and six epistemic kinds, one of which is `INFERENCE`. Neither term has been defined. "Inference" also appears as a Tarka Core function (PR-022), a step in the reasoning chain (PR-040), a step in the trace "Conclusion → inference → evidence → exact passage → …" (PR-050) and a node in the source model's illustrative provenance chain (source-model.md §6). PR-041 and DR-002 use the lower-case product language "known versus inferred" without defining either term.

DR-073 / ADR-0029 established that `FACT` is an asserted epistemic kind, not a status or verdict. DR-074 / ADR-0030 established that `EVIDENCE` is an asserted epistemic kind for propositions reporting what a source says, and that the relationship between evidential material and a claim is a separate concept.

## Problem
Without a definition, `INFERRED` could be read as a confidence level, as "no evidence", as an LLM-origin marker, or as an automatic consequence of the `INFERENCE` kind — readings that would conflict with DR-003 (status from evidence and rules; no model or person sets status directly), PR-050 (conclusions trace through inference to evidence) and ADR-0008 (provenance is a separate record). A further risk is that every evidence-to-claim relationship ("Source S states P" → "P", DR-074) is treated as an inference, which would make almost every source-backed claim `INFERRED`.

The product owner selected a minimal definition that fixes the meaning of `INFERRED` and blocks these readings without deciding the inference architecture or the status model.

## Decision
`INFERRED` is a claim/conclusion status indicating that the proposition is derived through reasoning from premises. `INFERRED` does not mean that the proposition is weakly supported, unsupported, uncertain, evidence-free, or produced by an LLM. `INFERRED` is not computed merely from the `INFERENCE` epistemic kind. An evidence relationship by itself does not make a claim `INFERRED`. Whether `INFERRED` can coexist with another claim status, and how inference affects status computation, remain open.

## Exact semantic definition
1. **Meaning.** `INFERRED` is a claim/conclusion status indicating that the proposition is derived through reasoning from premises.
2. **Premises — minimum only.** An `INFERRED` proposition is derived through reasoning from premises. The premise entity type, premise cardinality, whether premises are claims or evidence propositions, graph structure, warrants, inference rules and inference categories (deductive, abductive, defeasible) are not decided.
3. **Status computation unchanged.** Status remains determined by evidence and verification rules (DR-003, PR-032). This ADR does not define when `INFERRED` is computed.

## Non-equivalences
`INFERRED` does **not** mean, and is not automatically:
- weakly supported;
- unsupported;
- uncertain;
- evidence-free — an inference may be derived from premises that themselves have evidence;
- LLM-generated — LLM origin is provenance, separate from status (ADR-0008); a human, a deterministic rule or another approved reasoning mechanism could participate in an inference;
- the `INFERENCE` epistemic kind;
- `UNVERIFIED`;
- `INSUFFICIENT_EVIDENCE`;
- `PARTIALLY_SUPPORTED`;
- `SUPPORTED`.

**Not a confidence or strength level.** `INFERRED` must not be read as a point on an ordering such as `SUPPORTED > INFERRED > PARTIALLY_SUPPORTED`. No confidence semantics are introduced; PR-163 remains provisional.

## Relationship to the INFERENCE kind
- `INFERRED` is not computed merely from the `INFERENCE` epistemic kind. The existence or assignment of the `INFERENCE` kind must not itself directly set the `INFERRED` status. This preserves DR-003: no model or person sets a status directly.
- The semantic definition of the `INFERENCE` kind remains open.

## Relationship to evidence relationships (DR-074)
- An evidence relationship between a claim and evidential material does not, by itself, constitute an inference and does not by itself cause the claim to receive `INFERRED` status.
- This does not say that reasoning can never use evidence. The step from "Source S states P" to "P" is not, by this ADR, a mandatory inference; whether a particular reasoning step from evidence to a proposition constitutes an inference in a specific reasoning record remains open, as does the exact relationship between evidence, premises, inference and conclusion.

## Relationship to SUPPORTED and other statuses
- This ADR defines `INFERRED` only. It does not define `SUPPORTED`, `PARTIALLY_SUPPORTED`, `CONTRADICTED`, `CONTESTED`, `UNVERIFIED` or `INSUFFICIENT_EVIDENCE`, their thresholds, precedence or propagation (PR-044, PR-093).
- `INFERRED` does not mean `UNVERIFIED`. An LLM-generated inference may be unverified, but LLM origin and inference status are separate concepts. The rule that LLM candidate claims are labelled `UNVERIFIED` (DR-003) is unchanged; the distinction between initial `UNVERIFIED` and `INSUFFICIENT_EVIDENCE` (P4) and the name collision between claim-status `UNVERIFIED` and source-verification `UNVERIFIED` are not addressed.
- `INFERRED` does not mean that evidence is absent or insufficient. Whether insufficient or unavailable premise evidence changes a resulting status is a future status-propagation decision; OQ-E21 is not resolved.
- A proposition represented as a conclusion is not thereby `INFERRED`; whether every conclusion is inferred is not decided.

## Explicitly deferred: status coexistence
- Whether `INFERRED` can coexist with another claim status, including `SUPPORTED`, remains **open**. This ADR neither permits nor forbids `INFERRED` + `SUPPORTED`, and creates no status precedence or propagation.
- Whether the seven status tokens form one mutually exclusive status dimension or more than one dimension remains **unresolved**. No multi-status model is introduced.

## Explicitly deferred: inference architecture
Not decided: the reasoning record; Claim vs Statement; the Conclusion object; `INFERENCE` kind semantics; the premise model; the inference graph; inference provenance; warrants and inference rules; circularity (cycle detection, self-support, graph constraints); inference reproducibility and rule/warrant versioning in relation to CorpusState (CorpusState governance is unchanged: source-model.md §3, DR-014); the compatibility matrix between epistemic kinds and statuses (e.g. `FACT` + `INFERRED`, `FACT` + `EVIDENCE`, `INFERENCE` + `INFERRED`, `INFERENCE` + `SUPPORTED`, `EVIDENCE` + `INFERRED`) and kind exclusivity.

## Explicitly deferred: LLM policy
Existing governance is unchanged: the LLM does not directly assign status (DR-003); LLM output is not a source (DR-017); LLM output is not automatically evidence; an LLM-origin inference is not `INFERRED` merely because of its origin. Not decided (P5): whether an LLM may propose an inference, premises, inference relationships or warrants; human confirmation; acceptance workflow; provenance requirements.

## Product language
The technical status `INFERRED` should not automatically be assumed to define every occurrence of lower-case product language "inferred" or "known" (e.g. "known versus inferred" in PR-041 and DR-002) unless explicitly stated. This is analogous to DR-073's treatment of ordinary-language "fact". "Known" is not defined by this ADR.

## Alternatives considered

| Alternative (P3 study) | Why not chosen |
|---|---|
| Weak-confidence status | Would turn a status into a strength scale overlapping `PARTIALLY_SUPPORTED`, `INSUFFICIENT_EVIDENCE`, the `UNCERTAINTY` kind and PR-163 |
| Evidence-free reasoning | Conflicts with PR-050 (conclusions trace through inference to evidence) |
| Mirror of the `INFERENCE` kind | Would let whoever assigns the kind set a status, contrary to DR-003, and duplicates vocabulary |
| LLM-generated marker | Would derive status from origin, contrary to DR-003 and ADR-0008 |
| Derivation marker deciding coexistence either way (Candidates 1 and 2) | Would decide status dimensionality, which the product owner has kept open |

## Consequences
- `INFERRED` has a defined meaning that does not overlap confidence, verification, insufficiency, origin or the `INFERENCE` kind.
- DR-074's evidence relationship is not swallowed by `INFERRED`.
- DR-073 and DR-074 are unchanged.
- Status coexistence and dimensionality must be decided before status rules are defined (PR-044, PR-093).
- A future "Why?" trace must not present `INFERRED` as a strength verdict.

## Cross-references

| Decision | Relationship |
|---|---|
| DR-003, PR-090 | `INFERRED` remains an approved status; its meaning is now defined; no other status defined |
| PR-032 | Unchanged: rules determine status |
| PR-044, PR-093 | Remain open (definitions, thresholds, precedence, propagation) |
| DR-073 / ADR-0029 | Unchanged; kind/status compatibility still open |
| DR-074 / ADR-0030 | Unchanged; an evidence relationship is not by itself an inference |
| DR-002, PR-041 | "Known versus inferred" is product language, not defined by this ADR |
| PR-022, PR-040, PR-050, source-model.md §6 | Inference as function, chain step, trace step and provenance node — representation not decided |
| DR-014, source-model.md §3 (CorpusState) | Unchanged |
| DR-017 / ADR-0009, ADR-0008 | Unchanged; origin is provenance, not status |
| PR-160 … PR-162 | Unchanged; `INFERRED` ≠ uncertain or insufficient |
| PR-163 | Remains provisional; `INFERRED` is not confidence |
