"""LLM client abstraction shared by RiseWise's reasoning modules.

RiseWise's reasoning modules must generalize across arbitrary user input,
never hardcode logic for one scenario or one topic. This module isolates
the only place that calls an LLM, so the provider can be swapped without
touching main.py, and so it can be replaced with a fake in tests
(constitution section 13: keep reasoning modules independent; avoid hidden
hardcoded assumptions).

Currently backs:
- Module 1, Context Structurer (structure)
- Module 2, RITA Engine (rita_scan)
"""

from __future__ import annotations

import json
import os
from typing import Optional, Protocol

from .schemas import DecisionContext, RitaScan

STRUCTURE_SYSTEM_PROMPT = """You are the Context Structurer for RiseWise, a provenance-first \
AI reasoning engine. Convert the user's raw decision or question — which may be \
about ANY topic or domain — into a structured Decision Context.

Do not solve the decision. Do not recommend an option. Only structure it.

Extract:
- decision_or_problem: the core decision or question, restated precisely
- objective: what the user is trying to achieve
- constraints: known limits (budget, time, policy, technical, resource, etc.)
- stakeholders: who benefits, bears cost, is affected, or is absent from the decision, each with a short role
- time_horizon: the relevant time frame, if stated or reasonably inferable
- system_boundary: what is explicitly in scope vs out of scope for this decision
- known_evidence: facts or claims already present in the input, each classified as one of:
  verified_evidence, source_record, interpretation, assumption, hypothesis, unknown
- unknown_information: what would need to be known but is not yet stated

If the input is too thin to populate a field, leave it empty rather than inventing content.
Never fabricate evidence, sources, or stakeholders not implied by the input.

Respond with ONLY a JSON object matching this shape (no prose, no markdown fences):
{
  "decision_or_problem": "...",
  "objective": "...",
  "constraints": ["..."],
  "stakeholders": [{"name": "...", "role": "..."}],
  "time_horizon": "..." or null,
  "system_boundary": "..." or null,
  "known_evidence": [{"statement": "...", "status": "..."}],
  "unknown_information": ["..."]
}
"""

RITA_SCAN_SYSTEM_PROMPT = """You are the RITA Engine for RiseWise, a provenance-first \
AI reasoning engine. You receive a structured Decision Context — about ANY topic or \
domain — and scan it through the four RITA Framework dimensions.

Do not recommend an option. Only scan and surface findings.

For each dimension, ask the framework's own questions and produce zero, one, or several
findings — do not force exactly one finding per dimension, and do not invent a finding
where the context gives no basis for one:

RELATIONAL_INTEGRITY: Who benefits? Who bears the cost? Who is negatively affected? Who
is absent from the decision? Is harm being externalized? Are benefits/burdens
disproportionately distributed? Does the decision damage trust or cooperation?

INTEGRITY_OF_SYSTEMS: What systems are connected? What dependencies or feedback loops
exist? Does solving one problem create another? Is the problem being displaced outside
the stated system boundary? What downstream consequences may occur?

TEMPORAL_ALIGNMENT: What happens immediately, medium-term, long-term? Are future costs
being created? Is short-term efficiency undermining long-term stability? Are consequences
reversible? What assumptions must remain true over time?

ADAPTIVE_REGENERATION: Can the affected system(s) recover from failure? Does the
intervention consume resources faster than they can be restored? Is the solution
resilient and adaptable to changing conditions? Does it increase dependency or build
capability?

Each finding must have all five fields:
- dimension: one of relational_integrity, integrity_of_systems, temporal_alignment, adaptive_regeneration
- observation: what you observed, grounded in the given Decision Context
- risk_or_opportunity: the risk or opportunity this observation implies
- key_questions: open questions this finding raises (list, may be empty)
- evidence_status: one of verified_evidence, source_record, interpretation, assumption, hypothesis, unknown
  — classify the OBSERVATION itself, not the underlying decision
- confidence: one of low, medium, high

Ground every finding in the given Decision Context. Where the context lacks the
information a question needs, that is itself worth a finding with evidence_status
"unknown" rather than a fabricated answer.

Respond with ONLY a JSON object matching this shape (no prose, no markdown fences):
{
  "findings": [
    {
      "dimension": "...",
      "observation": "...",
      "risk_or_opportunity": "...",
      "key_questions": ["..."],
      "evidence_status": "...",
      "confidence": "..."
    }
  ]
}
"""


class LLMClient(Protocol):
    def structure(self, raw_input: str) -> DecisionContext:
        ...

    def rita_scan(self, context: DecisionContext) -> RitaScan:
        ...


class AnthropicLLMClient:
    """Default RiseWise LLM client, backed by the Anthropic API.

    Reads ANTHROPIC_API_KEY and RISEWISE_LLM_MODEL from the environment —
    never hardcode credentials or a model name (constitution section 13).
    """

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None) -> None:
        # Intentionally does not validate api_key here: this object is built
        # by a FastAPI dependency, which runs before route-handler try/except
        # blocks. Deferring the check to each call keeps the "missing key"
        # failure inside the code path that can turn it into a clean 503
        # instead of an uncaught 500 (see main.py).
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or os.environ.get("RISEWISE_LLM_MODEL", "claude-sonnet-4-5")

    def _require_key(self) -> None:
        if not self.api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. RiseWise's reasoning modules require an "
                "LLM to generalize across arbitrary input; see .env.example."
            )

    def _call(self, system_prompt: str, user_content: str) -> dict:
        self._require_key()

        import anthropic  # imported lazily so tests don't need the package unless this path runs

        client = anthropic.Anthropic(api_key=self.api_key)
        message = client.messages.create(
            model=self.model,
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_content}],
        )
        text = "".join(
            block.text for block in message.content if getattr(block, "type", None) == "text"
        )
        return json.loads(text)

    def structure(self, raw_input: str) -> DecisionContext:
        payload = self._call(STRUCTURE_SYSTEM_PROMPT, raw_input)
        return DecisionContext.model_validate(payload)

    def rita_scan(self, context: DecisionContext) -> RitaScan:
        payload = self._call(RITA_SCAN_SYSTEM_PROMPT, context.model_dump_json())
        return RitaScan.model_validate(payload)
