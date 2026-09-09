"""LLM client abstraction for the Context Structurer.

RiseWise's reasoning modules must generalize across arbitrary user input,
never hardcode logic for one scenario. This module isolates the one place
that calls an LLM, so the provider can be swapped without touching main.py,
and so it can be replaced with a fake in tests (constitution section 13:
keep reasoning modules independent; avoid hidden hardcoded assumptions).
"""

from __future__ import annotations

import json
import os
from typing import Optional, Protocol

from .schemas import DecisionContext

SYSTEM_PROMPT = """You are the Context Structurer for RiseWise, a provenance-first \
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


class LLMClient(Protocol):
    def structure(self, raw_input: str) -> DecisionContext:
        ...


class AnthropicLLMClient:
    """Default RiseWise LLM client, backed by the Anthropic API.

    Reads ANTHROPIC_API_KEY and RISEWISE_LLM_MODEL from the environment —
    never hardcode credentials or a model name (constitution section 13).
    """

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None) -> None:
        # Intentionally does not validate api_key here: this object is built
        # by a FastAPI dependency, which runs before route-handler try/except
        # blocks. Deferring the check to structure() keeps the "missing key"
        # failure inside the code path that can turn it into a clean 503
        # instead of an uncaught 500 (see main.py).
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or os.environ.get("RISEWISE_LLM_MODEL", "claude-sonnet-4-5")

    def structure(self, raw_input: str) -> DecisionContext:
        if not self.api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. RiseWise's Context Structurer requires an "
                "LLM to generalize across arbitrary input; see .env.example."
            )

        import anthropic  # imported lazily so tests don't need the package unless this path runs

        client = anthropic.Anthropic(api_key=self.api_key)
        message = client.messages.create(
            model=self.model,
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": raw_input}],
        )
        text = "".join(
            block.text for block in message.content if getattr(block, "type", None) == "text"
        )
        payload = json.loads(text)
        return DecisionContext.model_validate(payload)
