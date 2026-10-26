# RiseWise
A provenance-first AI reasoning engine for defensible decisions.

RiseWise is a provenance-first knowledge, research and reasoning platform. Every important conclusion should be traceable to the exact source passages behind it, and RiseWise says honestly when it does not have a source.

**Tarka** is the structured reasoning capability within RiseWise. It is not a chatbot: it examines a question through claims, evidence, arguments, counterarguments, assumptions, contradictions and uncertainty, and supports "Why?" and "Challenge this conclusion". An LLM-generated statement is never automatically treated as a fact.

The first two domains are **GENERAL** and **VEDIC_SANSKRIT** (Pāṇini, Siddhānta Kaumudī, Ṛgveda, Taittirīya Saṃhitā and related scholarship).

## Current state

- **Design phase.** The Knowledge Source Model v0.1 is approved; the product requirements and decisions are documented. No schema, database or reasoning engine has been implemented yet.
- **Earlier Python backend retired.** The previous Python backend was an earlier prototype and is retired as the core implementation path ([ADR-0014](docs/architecture/decisions/0014-retire-python-prototype-as-core-implementation.md)).
- **Schema technology approved.** TypeScript is the language and Zod the runtime validation library for RiseWise domain models and validation schemas ([ADR-0013](docs/architecture/decisions/0013-typescript-and-zod-for-domain-models.md)).
- **Everything else is still provisional or open,** including the web framework, API server, database, local or cloud LLM providers, embeddings, search, authentication, deployment and billing. See the Decision Register.

## Development status

Implementation setup is being established. There are currently no supported instructions for running RiseWise locally.

## Project documents

| Document | Purpose |
|---|---|
| [Product requirements](docs/PRODUCT_REQUIREMENTS.md) | What RiseWise must do (approved / provisional / open) |
| [Decision Register](docs/DECISION_REGISTER.md) | Central index of decisions, open items and review points |
| [Source model](docs/architecture/source-model.md) | The approved Knowledge Source Model |
| [Architecture decisions](docs/architecture/decisions/) | ADRs |
| [Open questions](docs/OPEN_QUESTIONS.md) | Unresolved questions |
| [Conflicts](docs/CONFLICTS.md) | Recorded conflicts and how they are handled |
