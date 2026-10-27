# RiseWise
A provenance-first knowledge, research and reasoning platform.

RiseWise is a provenance-first knowledge, research and reasoning platform. Every important conclusion should be traceable to the exact source passages behind it, and RiseWise says honestly when it does not have a source.

**Tarka** is the structured reasoning capability within RiseWise. It is not a chatbot: it examines a question through claims, evidence, arguments, counterarguments, assumptions, contradictions and uncertainty, and supports "Why?" and "Challenge this conclusion". An LLM-generated statement is never automatically treated as a fact.

The first two domains are **GENERAL** and **VEDIC_SANSKRIT** (Pāṇini, Siddhānta Kaumudī, Ṛgveda, Taittirīya Saṃhitā and related scholarship).

RiseWise is built first for the individual **evidence-driven researcher**. Vedic/Sanskrit research is the first deeply supported specialization; researchers can also work privately with their own legitimately obtained sources ([DR-060](docs/DECISION_REGISTER.md)).

## Current state

- **Design phase.** The Knowledge Source Model v0.1 is approved; the product requirements and decisions are documented. No schema, database or reasoning engine has been implemented yet for the current architecture.
- **Earlier Python backend retired.** The previous Python backend was an earlier prototype and is retired as the core implementation path ([ADR-0014](docs/architecture/decisions/0014-retire-python-prototype-as-core-implementation.md)). See [Historical Python Prototype](#historical-python-prototype) below.
- **Schema technology approved.** TypeScript is the language and Zod the runtime validation library for RiseWise domain models and validation schemas ([ADR-0013](docs/architecture/decisions/0013-typescript-and-zod-for-domain-models.md)).
- **Everything else is still provisional or open,** including the web framework, API server, database, local or cloud LLM providers, embeddings, search, authentication, deployment and billing. See the Decision Register.

## Development status

Implementation setup for the current RiseWise/Tarka architecture is being established. There are currently no supported instructions for running it locally.

## Project documents

| Document | Purpose |
|---|---|
| [Product requirements](docs/PRODUCT_REQUIREMENTS.md) | What RiseWise must do (approved / provisional / open) |
| [Decision Register](docs/DECISION_REGISTER.md) | Central index of decisions, open items and review points |
| [Source model](docs/architecture/source-model.md) | The approved Knowledge Source Model |
| [Architecture decisions](docs/architecture/decisions/) | ADRs |
| [Open questions](docs/OPEN_QUESTIONS.md) | Unresolved questions |
| [Conflicts](docs/CONFLICTS.md) | Recorded conflicts and how they are handled |

## Historical Python Prototype

An earlier Python prototype of RiseWise is still in this repository (`backend/`, `tests/`, `requirements.txt`, `pytest.ini`, `.env.example`). It contained:

- **Module 1, Context Structurer** (`POST /context/structure`): turned a raw decision or question into a structured decision context.
- **Module 2, RITA Engine** (`POST /rita/scan`): scanned a decision context and produced findings.
- **Pipeline orchestrator** (`POST /decisions/analyze`): ran Module 1 then Module 2 in one call.
- **Ollama integration**: a self-hosted model served by Ollama as the default LLM backend, with the Anthropic API as an opt-in alternative.

The prototype is **retired as the core implementation path** ([ADR-0014](docs/architecture/decisions/0014-retire-python-prototype-as-core-implementation.md)). It is not the current architecture, and it remains recoverable in Git history (commits `7d3199a`, `41713d5`, `fa1c324`, `cb43582`). Its own design notes are in `docs/adr-0001` … `docs/adr-0004`; they use a separate, historical numbering from the current ADR series. Python is not prohibited for future, explicitly approved supporting tooling.

### Running the retired prototype (historical reference only)

> These instructions apply **only to the retired Python prototype**. They are not setup instructions for the current RiseWise/Tarka architecture.

**LLM backend (choose one):**

- Self-hosted (prototype default): install [Ollama](https://ollama.com), run `ollama serve`, then `ollama pull llama3.1` (or your chosen model).
- Anthropic API: set `RISEWISE_LLM_PROVIDER=anthropic` and `ANTHROPIC_API_KEY` in `.env`.

```bash
pip install -r requirements.txt
cp .env.example .env   # configure your chosen LLM backend
uvicorn backend.app.main:app --reload
```

```bash
POST http://localhost:8000/decisions/analyze
{"raw_input": "Should we do X?"}
```

`/context/structure` and `/rita/scan` were also independently callable.

### Testing the retired prototype (historical reference only)

```bash
pip install -r requirements.txt
pytest
```

The prototype's tests run offline against fake/mocked LLM clients; no running Ollama server or Anthropic API key is required.
