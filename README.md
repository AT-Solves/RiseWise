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

No frontend, no database yet. See `docs/adr-0001-backend-first-module1.md`,
`docs/adr-0002-rita-engine.md`, and `docs/adr-0003-pipeline-orchestrator.md`
for why, and the RiseWise project's `constitution.md` doc (in the attached
Claude project) for the full RITA Framework and reasoning pipeline.

## Running locally

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in ANTHROPIC_API_KEY
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

Tests run offline against a fake LLM client — no API key required.
