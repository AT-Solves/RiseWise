# ADR-0004: Self-hosted open model (Ollama) as the default LLM backend

## Status
Accepted (2026-09-09)

## Context
Modules 1 and 2 were originally built against the Anthropic API only
(ADR-0001, ADR-0002). On explicit direction, RiseWise should not depend on
a third-party API by default — the reasoning should run on a model the
project self-hosts.

A genuinely separate question came up alongside this: could RiseWise train
its own LLM from scratch? Recorded here for the project history, not as an
open option: training a model competitive enough to do RiseWise's
structuring/RITA reasoning requires web-scale training data and
distributed GPU infrastructure running for weeks to months, at a cost
normally in the tens of millions of dollars — categorically different from
an MVP task, and not something any development session can produce. This
ADR is about which existing model RiseWise calls, not about training one.

## Decision
1. Add `OllamaLLMClient`, a second implementation of the existing
   `LLMClient` Protocol, calling a self-hosted model served by
   [Ollama](https://ollama.com) over its local REST API
   (`POST {host}/api/chat`, `format: "json"`). Ollama runs an existing
   open-weight model (e.g. Llama, Qwen, Mistral) that the operator pulls
   and runs themselves — RiseWise trains nothing.
2. `OllamaLLMClient` becomes the **default** provider. `AnthropicLLMClient`
   (ADR-0001) is kept, not deleted, and selected via
   `RISEWISE_LLM_PROVIDER=anthropic` — useful as a fallback if a
   self-hosted model's output quality proves insufficient for a given
   task, without having to re-add the integration later.
3. Both clients share the same system prompts
   (`STRUCTURE_SYSTEM_PROMPT`, `RITA_SCAN_SYSTEM_PROMPT`) — the reasoning
   instructions are provider-agnostic; only the HTTP/SDK glue differs
   between the two classes.
4. Ollama-specific config (`RISEWISE_OLLAMA_HOST`, `RISEWISE_OLLAMA_MODEL`)
   and Anthropic's model variable (renamed `RISEWISE_ANTHROPIC_MODEL` for
   clarity now that two providers exist) are separate environment
   variables, per constitution section 13 ("use environment variables for
   secrets").

## Consequences — including tradeoffs worth being explicit about
- **Quality risk, stated plainly**: open-weight models run locally are, in
  general, meaningfully weaker than frontier hosted models at complex
  structured-extraction and multi-step reasoning tasks like the RITA scan.
  This has not yet been evaluated against real RiseWise inputs — do that
  before trusting Ollama's output for anything real. If quality is
  inadequate, `RISEWISE_LLM_PROVIDER=anthropic` is a one-line escape hatch,
  not a rebuild.
- **Operational burden shifts to the operator**: Ollama must be installed
  and running (`ollama serve`), and the chosen model must be pulled
  (`ollama pull <model>`) before the backend can serve real requests. The
  backend does not install or manage Ollama itself.
- `OllamaLLMClient.structure()`/`.rita_scan()` raise `RuntimeError` (→ 503
  at the API layer, consistent with Module 1/2's existing contract) when
  Ollama is unreachable, returns a non-2xx status, or returns text that
  isn't valid JSON — the last of these is a real risk with smaller local
  models that don't reliably follow "JSON only" instructions.
- No new pip dependency: Ollama's REST API is called with `httpx`, already
  a project dependency (used by FastAPI's TestClient).
