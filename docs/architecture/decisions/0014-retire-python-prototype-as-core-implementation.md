# ADR-0014: Retire the Python prototype as the core implementation path

- **Status:** Accepted (2026-10-26)
- **Decision Register:** DR-063 (see also DR-005 correction, DR-062)
- **Related:** ADR-0013

## Context
The `main` branch contains an earlier, legitimate RiseWise prototype written in Python (all commits dated 2026-09-09):

| Commit | Content |
|---|---|
| [`7d3199a`](https://github.com/AT-Solves/RiseWise/commit/7d3199a43a47ea9c5071be5e01224c28264672fd) | Module 1, Context Structurer (backend-first, domain-agnostic MVP) |
| [`41713d5`](https://github.com/AT-Solves/RiseWise/commit/41713d5614c20dbab156e52c2d940f9e902aab0f) | Module 2, RITA Engine (scans a decision context on any topic) |
| [`fa1c324`](https://github.com/AT-Solves/RiseWise/commit/fa1c324b6b2dadbe084910a1c71c565cc6f80dd6) | Pipeline orchestrator (`POST /decisions/analyze`) |
| [`cb43582`](https://github.com/AT-Solves/RiseWise/commit/cb43582520107201119395629a551b61a8d0dd10) | Default LLM backend changed to self-hosted Ollama |

Since then, the product direction has become the provenance-first RiseWise/Tarka architecture (Knowledge Source Model v0.1, ADR-0001 … ADR-0012). ADR-0013 separately approved TypeScript + Zod for domain models and validation schemas; ADR-0013 itself did not retire Python.

## Decision
- The Python prototype is **retired as the core implementation path** for RiseWise/Tarka.
- The core direction is the provenance-first RiseWise/Tarka architecture.
- The prototype remains **historical and recoverable** from Git history (the commits above).

**What this decision is not:**
- It is not a judgement that the prototype was wrong or useless; it was a narrower prototype that informed the current design.
- It does not prohibit future, explicitly approved use of Python for supporting purposes, such as research tools, corpus processing, evaluation tooling or scripts.
- It does not decide whether or when prototype files are removed from `main`, or how the Claude design branch and `main` are integrated.
- It does not resolve the numbering collision between the prototype's ADRs (`docs/adr-0001` … `adr-0004` on `main`) and this ADR series.

## Consequences
- New core implementation work follows the RiseWise/Tarka architecture, using TypeScript + Zod for domain models and validation schemas (ADR-0013); other stack choices remain provisional or open (DR-008).
- The prototype's history stays available for reference; nothing in it is treated as nonexistent (DR-005 correction).
- Any future Python tooling needs its own explicit approval.
- The ADR numbering collision remains an open housekeeping item.
