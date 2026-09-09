# RiseWise

A provenance-first AI reasoning engine for defensible decisions.

## Current state (MVP, Phase 1 in progress)

Only **Module 1 — Context Structurer** exists so far: a FastAPI backend with
one endpoint that turns a raw decision or question, on any topic, into a
structured Decision Context (decision, objective, constraints, stakeholders,
time horizon, system boundary, known evidence, unknown information).

No frontend, no database yet. See `docs/adr-0001-backend-first-module1.md`
for why, and the RiseWise project's `constitution.md` doc (in the attached
Claude project) for the full RITA Framework and reasoning pipeline.

## Running locally

```bash
cd backend
pip install -r ../requirements.txt   # or: pip install -r requirements.txt from repo root
cp ../.env.example ../.env           # fill in ANTHROPIC_API_KEY
uvicorn app.main:app --reload --app-dir .
```

From the repo root:

```bash
POST http://localhost:8000/context/structure
{"raw_input": "Should we do X?"}
```

## Testing

```bash
pip install -r requirements.txt
pytest
```

Tests run offline against a fake LLM client — no API key required.
