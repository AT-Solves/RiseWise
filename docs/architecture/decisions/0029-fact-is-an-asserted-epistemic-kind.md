# ADR-0029: FACT is an asserted epistemic kind distinct from evidential status

- **Status:** Accepted (2026-11-03)
- **Decision Register:** DR-073
- **Product owner decision:** option P1-E explicitly selected (P1 product-semantics study, 2026-11-03)
- **Related:** DR-003, DR-017 (ADR-0009), DR-022, DR-058, ADR-0008, PR-011, PR-031, PR-032, PR-041, PR-080, PR-081, PR-083, PR-090 … PR-093

## Context
DR-003 approved two Tarka vocabularies: the epistemic kinds `FACT`, `EVIDENCE`, `INFERENCE`, `ASSUMPTION`, `INTERPRETATION`, `UNCERTAINTY`, and the claim statuses `SUPPORTED`, `PARTIALLY_SUPPORTED`, `CONTRADICTED`, `CONTESTED`, `UNVERIFIED`, `INSUFFICIENT_EVIDENCE`, `INFERRED`. Evidence and verification rules determine a claim's status (DR-003, PR-032).

The repository also uses the lower-case word "fact" in product prose: the DR-003 title ("LLM statements are never automatically facts") and risk line ("hallucinations presented as established facts"), PR-011 ("instead of treating LLM output as fact") and PR-031 ("never automatically considered a fact"). Elsewhere, approved documents use "fact" in other ordinary senses (e.g. a "structural fact" in DR-069 / ADR-0025; research facts about sources in source-model.md).

Governance did not say whether the prose "fact" and the kind `FACT` are the same thing. Read as the same thing, `FACT` would become an earned standing ("established as true") and would duplicate the status vocabulary, in particular `SUPPORTED`. The provisional PR-081 ("FACT is reachable only through evidence and verification rules") leaned towards that reading. The product owner was asked to choose between five interpretations and selected P1-E.

## Decision
`FACT` is an **asserted epistemic kind**: it describes what kind of proposition a claim is. `FACT` does not mean that the proposition has been proven true, sufficiently supported, or otherwise established as true.

The lower-case word "fact" in existing product prose (DR-003, PR-011, PR-031 and similar) is ordinary product language referring to an established, trustworthy fact. It is not a technical synonym for the Tarka `FACT` epistemic kind.

The evidential standing of a claim is determined separately, through Tarka's status, evidence and rule machinery, whose detailed definitions remain to be decided.

## Detailed rules
1. **What `FACT` answers.** "What kind of proposition is this?" — not "Is this proposition sufficiently supported?"
2. **Not a status.** `FACT` ≠ `SUPPORTED`, and `FACT` is not synonymous with any other status.
3. **Not a verdict.** `FACT` ≠ established truth. A `FACT` kind alone must not be presented, in "Why?" traces or elsewhere, as proof, truth or an evidential verdict.
4. **Status boundary unchanged.** Evidence and verification rules determine a claim's status; no model or person sets a status directly (DR-003). This ADR defines none of the seven statuses.
5. **Approved wording retained.** The wording of DR-003, PR-011 and PR-031 is not changed; it is read as ordinary product language under this ADR.

## Alternatives considered

| Alternative | Why not chosen |
|---|---|
| P1-A — asserted kind, leaving the DR-003 / PR-031 prose unaddressed | Same meaning as the chosen option, but would leave an unresolved conflict between the kind and the approved prose |
| P1-B — `FACT` as earned epistemic standing | Duplicates `SUPPORTED`; turns a kind into a second status; leaves no kind for factual claims not yet established; risks erasing "known versus inferred" (PR-041) when an inference earns `FACT` |
| P1-C — `FACT` as a mechanically verified textual/attributional fact | Ties a reasoning kind to source verification (PR-092, ADR-0008); overlaps the open meaning of `EVIDENCE` (DR-058); paraphrased attributions are not mechanically verifiable |
| P1-D — `FACT` as a gated kind | An assignment policy rather than a meaning; would still have required choosing A, B or C |

## Consequences
- `FACT` remains one of the six approved epistemic kinds.
- `FACT` is not itself an evidential verdict; a `FACT`-kind claim's standing is shown by its status.
- `SUPPORTED` remains a separate item of the status vocabulary.
- Detailed status semantics, thresholds and propagation remain open (PR-044, PR-093; GAP-1b).
- "Why?" traces and other presentation must not present `FACT` alone as proof or truth.
- Later governance must define the relationship between kinds and statuses.
- PR-081 (provisional) no longer reflects an available reading of `FACT` as evidential standing; it remains provisional, and whether and by whom the `FACT` kind may be assigned is undecided.

## Explicit non-decisions
This ADR does **not** decide:
- whether kinds are mutually exclusive, or whether a claim may have more than one kind;
- which `FACT` + status combinations are valid;
- who assigns kinds; whether an LLM may assign a kind; whether an LLM-origin claim may later receive `FACT`;
- whether human review is required (PR-083), or whether human review may confer any status;
- how `FACT` interacts with `INFERENCE` or with `EVIDENCE`;
- the meaning of the `EVIDENCE` kind (DR-058, PR-082, C-002);
- status definitions, thresholds and propagation (PR-044, PR-093);
- contradiction semantics, including `CONTESTED` vs `CONTRADICTED`;
- `UNVERIFIED` vs `INSUFFICIENT_EVIDENCE`;
- evidence sufficiency; source authority (DR-049);
- interpretation semantics, including the Source Model Interpretation entity vs the `INTERPRETATION` kind;
- unavailable or unverifiable evidence (OQ-E21);
- the remaining Tarka product-semantics questions (meaning of `EVIDENCE`, meaning of `INFERRED`, how initial `UNVERIFIED` is established, the LLM evidence-proposal boundary, unsourced GENERAL knowledge, Source Interpretation vs `INTERPRETATION`);
- any schema, type, storage, UI or assignment logic.

## Relationship to existing decisions

| Decision | Relationship |
|---|---|
| DR-003 | Wording unchanged. Its kind list includes `FACT`; its lower-case "facts" (title, risk) is ordinary product language under this ADR |
| PR-011, PR-031 | Wording unchanged; "fact" read as ordinary product language |
| PR-032 | Unchanged: rules determine status |
| PR-080 | `FACT` remains one of the six kinds; its meaning is now defined |
| PR-081 (provisional) | Its "reachable only through evidence" reading of `FACT` as standing is not adopted; it remains provisional |
| PR-083 (open) | Remains open; `FACT` is a kind, not a verdict |
| PR-090 … PR-093 | No status defined or changed |
| DR-058 / PR-082 / C-002 | Remain open |
| ADR-0008, PR-092, source-model.md §3 | Unaffected: source verification states remain separate from Tarka kinds and statuses; this is not a source-layer definition |
| DR-017 / ADR-0009 | Unaffected: LLM output is never a source |
