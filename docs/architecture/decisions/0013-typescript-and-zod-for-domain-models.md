# ADR-0013: TypeScript and Zod for domain models and validation schemas

- **Status:** Accepted (2026-10-26)
- **Decision Register:** DR-062 (splits the schema-technology part out of the DR-008 proposal)
- **Design reference:** source-model.md §21 (MVP source model)

## Context
The next step defines the Knowledge Source Model's entities as schemas validated by tests. That needs a definition language and a runtime validation library. A full technology stack was proposed in architecture proposal rev. 2 (DR-008) but never approved.

## Decision
- **TypeScript** is the language for RiseWise domain-model and schema definitions.
- **Zod** is the runtime validation library for those schemas.

**Scope — this ADR approves only the above.** It applies to RiseWise domain models and validation schemas. It does **not** approve any other technology. In particular, the following remain provisional or open unless separately approved: React/Vite, Fastify, SQLite, PostgreSQL, Ollama, cloud LLM providers, embeddings, search technology, authentication, deployment platform, billing/tier implementation, monorepo tooling (e.g. pnpm), ORM/migration tooling, and test framework.

## Consequences
- Schema work (Step 2) may be written in TypeScript with Zod, once the product owner authorises that step.
- No persistence, API, UI or LLM technology follows from this decision.
- Zod schemas are the source of truth for runtime validation of domain records; any derived artefacts (e.g. JSON Schema) are a separate, future decision.
