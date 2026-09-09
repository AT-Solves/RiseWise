# ADR-0003: Thin pipeline orchestrator over Modules 1-2

## Status
Accepted (2026-09-09)

## Context
ADR-0002 deferred connecting Module 1 (Context Structurer) and Module 2
(RITA Engine) into one flow, leaving callers to pass Module 1's `context`
into Module 2's request body manually. That's a real usability gap: the
constitution's pipeline (section 6) treats Context Structuring and RITA
Scan as consecutive steps of one flow, not two unrelated capabilities.

## Decision
Add `POST /decisions/analyze`: takes the same `raw_input` as
`/context/structure`, internally calls `llm.structure()` then
`llm.rita_scan()` on the result, and returns both outputs together.

This is deliberately a thin orchestration layer, not a new reasoning
module:
- It contains no prompts, no domain logic, and no new schema fields beyond
  bundling the two existing outputs (`AnalyzeResponse` = `raw_input` +
  `DecisionContext` + `RitaScan`).
- `/context/structure` and `/rita/scan` are unchanged and still
  independently callable — `/decisions/analyze` is additive, not a
  replacement. A caller who only wants Step 1, or who wants to re-run Step
  2 on a hand-edited context, still can.
- A single LLM-config failure fails the whole call with 503 (same
  contract as the individual endpoints) rather than partially succeeding,
  since Module 2 cannot run meaningfully on the absence of Module 1's
  output.

## Consequences
- As more modules are added (Evidence Integrity, Perspective Engine,
  Tension Mapper, ...), this orchestrator will need to grow or be
  restructured — a single flat function chaining N calls does not scale
  indefinitely. Revisit this ADR when adding Module 3.
- No retry, partial-result, or streaming behavior yet; each call is
  synchronous and all-or-nothing.
