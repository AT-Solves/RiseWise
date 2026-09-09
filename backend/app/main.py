"""RiseWise backend — MVP entrypoint.

Implements Module 1 (Context Structurer) and Module 2 (RITA Engine). See
docs/adr-0001-backend-first-module1.md and docs/adr-0002-rita-engine.md for
the reasoning behind each, and the RiseWise project constitution for the
full RITA Framework and reasoning pipeline these modules are steps 1-2 of.
"""

from __future__ import annotations

from fastapi import Depends, FastAPI, HTTPException

from .llm_client import AnthropicLLMClient, LLMClient
from .schemas import ScanRequest, ScanResponse, StructureRequest, StructureResponse

app = FastAPI(
    title="RiseWise API",
    description="A provenance-first AI reasoning engine for defensible decisions.",
    version="0.2.0",
)


def get_llm_client() -> LLMClient:
    """FastAPI dependency, shared by every reasoning endpoint. Overridden in
    tests with a fake so they run without network access or a real API key."""
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
    generalization is the LLM's job (see llm_client.STRUCTURE_SYSTEM_PROMPT),
    not hardcoded logic here.
    """
    try:
        context = llm.structure(request.raw_input)
    except RuntimeError as exc:
        # Config/availability failure (e.g. no API key). Fail loudly rather
        # than silently fabricating a structure — constitution section 16.
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return StructureResponse(context=context, raw_input=request.raw_input)


@app.post("/rita/scan", response_model=ScanResponse)
def rita_scan(
    request: ScanRequest, llm: LLMClient = Depends(get_llm_client)
) -> ScanResponse:
    """Scan a Decision Context through the four RITA dimensions.

    Takes an already-structured Decision Context (the output of
    /context/structure) rather than raw input — this module reasons over
    structure, not text, keeping it independent of how that structure was
    produced (constitution section 13: keep reasoning modules independent).
    """
    try:
        scan = llm.rita_scan(request.context)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return ScanResponse(scan=scan, context=request.context)
