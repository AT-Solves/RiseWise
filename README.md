# RiseWise

A provenance-first AI reasoning engine for defensible decisions.

## Current state (MVP, Phase 1-2 in progress)

Two modules exist so far, both backend-only:

- **Module 1 — Context Structurer** (`POST /context/structure`): turns a
  raw decision or question, on any topic, into a structured Decision
  Context (decision, objective, constraints, stakeholders, time horizon,
  system boundary, known evidence, unknown information).
- **Module 2 — RITA Engine** (`POST /rita/scan`): takes a Decision Context
  and scans it through the four RITA dimensions (Relational Integrity,
  Integrity of Systems, Temporal Alignment, Adaptive Regeneration),
  producing findings with observation, risk/opportunity, key questions,
  evidence status, and confidence.

No frontend, no database, no pipeline orchestrator yet — chaining the two
endpoints (pass Module 1's `context` into Module 2's request body) is done
by the caller for now. See `docs/adr-0001-backend-first-module1.md` and
`docs/adr-0002-rita-engine.md` for why, and the RiseWise project's
`constitution.md` doc (in the attached Claude project) for the full RITA
Framework and reasoning pipeline.

## Running locally

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in ANTHROPIC_API_KEY
uvicorn backend.app.main:app --reload
```

```bash
POST http://localhost:8000/context/structure
{"raw_input": "Should we do X?"}

POST http://localhost:8000/rita/scan
{"context": { ...the "context" object from the response above... }}
```

## Testing

```bash
pip install -r requirements.txt
pytest
```

Tests run offline against a fake LLM client — no API key required.
