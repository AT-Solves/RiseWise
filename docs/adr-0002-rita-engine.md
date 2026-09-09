# ADR-0002: RITA Engine takes structured context, not raw text

## Status
Accepted (2026-09-09)

## Context
Module 2 (RITA Engine, constitution section 12) analyses a decision through
the four RITA dimensions (section 4) and produces findings per section 6
Step 2. It is the second stage of the pipeline, sitting after Module 1
(Context Structurer, ADR-0001).

## Decision
1. `POST /rita/scan` accepts an already-structured `DecisionContext` (the
   output type of `/context/structure`), not raw user text. This keeps the
   two modules independently testable and independently callable —
   constitution section 13's "keep reasoning modules independent" — rather
   than having the RITA Engine silently re-derive structure from text, or
   Module 1 and Module 2 becoming coupled through a single combined
   endpoint. Chaining them (raw text → context → scan) is left to the
   caller for now; a pipeline orchestrator is deferred until more modules
   exist and the chaining shape is clearer.
2. `RitaScan.findings` is a flat, dimension-tagged list rather than a fixed
   struct with one slot per R/I/T/A. The constitution does not cap findings
   per dimension, and a decision may legitimately surface zero findings
   under one dimension and several under another; a fixed-slot struct would
   either force fabrication or silently drop findings.
3. Every `RitaFinding` carries `evidence_status` and `confidence` as
   required fields, not optional ones — per section 5, an observation
   without an evidence classification is not a defensible finding, and the
   schema enforces that rather than relying on prompt discipline alone.
4. The `AnthropicLLMClient` is extended (a shared `_call` helper, a second
   system prompt) rather than duplicated per module. It is judged safe to
   share because the LLM call itself is provider glue with no
   scenario-specific logic in it; the reasoning behavior lives entirely in
   each module's own system prompt and schema.

## Consequences
- A caller wanting the full Step 1 → Step 2 flow must currently make two
  HTTP calls and pass Module 1's `context` field into Module 2's request
  body themselves. This is acceptable for the MVP; revisit if a third
  module makes manual chaining unwieldy.
- Like Module 1, this module fails loudly (503) rather than fabricating a
  scan when no LLM is configured (section 16).
- RITA findings are only as good as the given `DecisionContext` — the
  Engine does not go back to raw text or external sources for more
  information. If the context is thin, the expected outcome is findings
  with `evidence_status: unknown`, not invented specifics.
