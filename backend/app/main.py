"""RiseWise backend — MVP entrypoint.

Implements Module 1 (Context Structurer) only, by design: see
docs/adr-0001-backend-first-module1.md for why the backend was built before
any frontend or database. See the RiseWise project constitution for the
full RITA Framework and reasoning pipeline this module is step 1 of.
"""

from __future__ import annotations

from fastapi import Depends, FastAPI, HTTPException

from .llm_client import AnthropicLLMClient, LLMClient
from .schemas import StructureRequest, StructureResponse

app = FastAPI(
    title="RiseWise API",
    description="A provenance-first AI reasoning engine for defensible decisions.",
    version="0.1.0",
)


def get_llm_client() -> LLMClient:
    """FastAPI dependency. Overridden in tests with a fake so they run
    without network access or a real API key."""
    return AnthropicLLMClient()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/context/structure", response_model=StructureResponse)
def structure_context(
    request: StructureRequest, llm: LLMClient = Depends(get_llm_client)
) -> StructureResponse:
    """Structure ANY raw decision or question into a Decision Context.

    This endpoint makes no assumption about domain, topic, or scenario —
    generalization is the LLM's job (see llm_client.SYSTEM_PROMPT), not
    hardcoded logic here.
    """
    try:
        context = llm.structure(request.raw_input)
    except RuntimeError as exc:
        # Config/availability failure (e.g. no API key). Fail loudly rather
        # than silently fabricating a structure — constitution section 16.
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return StructureResponse(context=context, raw_input=request.raw_input)
