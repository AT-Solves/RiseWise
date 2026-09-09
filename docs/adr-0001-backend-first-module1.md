# ADR-0001: Backend-first, Module 1 only, domain-agnostic by construction

## Status
Accepted (2026-09-09)

## Context
The RiseWise repository contained only a README and no code. The project
constitution's MVP architecture (section 11) specifies a Next.js frontend,
FastAPI backend, and PostgreSQL database, with eight reasoning modules
(section 12). Building all three layers before any reasoning logic exists
would front-load infrastructure with nothing yet to validate against, which
conflicts with section 13's instruction to build the smallest meaningful
working version first.

Separately: an early draft of this step defaulted to demonstrating the
module against the constitution's named initial use case (community waste
segregation, section 17). That was corrected on explicit direction — the
Context Structurer must generalize to any user's decision or question, not
be designed around, or implicitly scoped to, one demo scenario.

## Decision
1. Build backend-only for this step. No `frontend/`, no `agents/`, no
   Postgres. A FastAPI service with a single endpoint, `POST
   /context/structure`, implementing Module 1 (Context Structurer) from
   the reasoning pipeline (constitution section 6, Step 1).
2. Structuring is performed by an LLM (Anthropic, via `AnthropicLLMClient`
   in `backend/app/llm_client.py`), not hand-written rules. A schema
   (`backend/app/schemas.py`) constrains the output shape; the LLM
   supplies the generalization across arbitrary domains. No scenario-
   specific logic exists anywhere in `backend/app/`.
3. No database yet — the endpoint is stateless. Persistence is deferred
   until a second module (e.g. the RITA Engine) actually needs to read
   back a prior Decision Context.
4. Tests use a fake `LLMClient` (dependency-injected via FastAPI's
   `Depends`) so the suite runs offline, and deliberately cover two
   unrelated domains (a software decision, a civic-policy decision) to
   demonstrate the endpoint carries no hidden scenario assumptions.

## Consequences
- Nothing is visually demoable yet (no UI). The next meaningful step that
  would change this is either a bare frontend page or Module 2 (RITA
  Engine) built on top of this endpoint.
- Running the endpoint for real requires `ANTHROPIC_API_KEY` (see
  `.env.example`); without it, the endpoint returns 503 rather than
  fabricating output, per constitution section 16.
- Evidence Integrity classification (constitution section 5) is only
  partially exercised here — the LLM classifies evidence items found in
  the *user's own input*. It is not yet doing the fuller evidence
  research/validation described in section 16 and Phase 8; that is out of
  scope for Module 1.
