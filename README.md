# RiseWise

A provenance-first AI reasoning engine for defensible decisions.

## Current state (MVP, Phase 1-2 in progress)

Two reasoning modules and a thin orchestrator connecting them, all backend-only:

- **Module 1 — Context Structurer** (`POST /context/structure`): turns a
  raw decision or question, on any topic, into a structured Decision
  Context (decision, objective, constraints, stakeholders, time horizon,
  system boundary, known evidence, unknown information).
- **Module 2 — RITA Engine** (`POST /rita/scan`): takes a Decision Context
  and scans it through the four RITA dimensions (Relational Integrity,
  Integrity of Systems, Temporal Alignment, Adaptive Regeneration),
  producing findings with observation, risk/opportunity, key questions,
  evidence status, and confidence.
- **Pipeline orchestrator** (`POST /decisions/analyze`): runs Module 1 then
  Module 2 over the same raw input in one call.

Reasoning is LLM-backed, not rule-based, so it generalizes across any
domain rather than being scoped to one demo scenario. By default the LLM
is a **self-hosted open model served by Ollama** — no third-party API
dependency. The Anthropic API is available as an opt-in alternative. See
`docs/adr-0004-self-hosted-ollama-default.md` for why, and
`docs/adr-0001`–`0003` for the modules and pipeline. The RiseWise project's
`constitution.md` doc (in the attached Claude project) has the full RITA
Framework and reasoning pipeline.

No frontend, no database yet.

## Running locally

**LLM backend (choose one):**

- Self-hosted (default): install [Ollama](https://ollama.com), run
  `ollama serve`, then `ollama pull llama3.1` (or your chosen model).
- Anthropic API: set `RISEWISE_LLM_PROVIDER=anthropic` and
  `ANTHROPIC_API_KEY` in `.env`.

```bash
pip install -r requirements.txt
cp .env.example .env   # configure your chosen LLM backend
uvicorn backend.app.main:app --reload
```

```bash
POST http://localhost:8000/decisions/analyze
{"raw_input": "Should we do X?"}
```

`/context/structure` and `/rita/scan` remain independently callable if you
only want one step, or want to re-run the RITA scan on a hand-edited context.

## Testing

```bash
pip install -r requirements.txt
pytest
```

Tests run offline against fake/mocked LLM clients — no running Ollama
server or Anthropic API key required.
