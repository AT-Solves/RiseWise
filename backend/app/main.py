"""RiseWise backend — MVP entrypoint.

Implements Module 1 (Context Structurer), Module 2 (RITA Engine), and a
thin pipeline orchestrator that chains them. See docs/adr-0001,
docs/adr-0002, and docs/adr-0003 for the reasoning behind each, and the
RiseWise project constitution for the full RITA Framework and reasoning
pipeline these are steps 1-2 of.
"""

from __future__ import annotations

import os

from fastapi import Depends, FastAPI, HTTPException

from .llm_client import AnthropicLLMClient, LLMClient, OllamaLLMClient
from .schemas import (
    AnalyzeResponse,
    ScanRequest,
    ScanResponse,
    StructureRequest,
    StructureResponse,
)

app = FastAPI(
    title="RiseWise API",
    description="A provenance-first AI reasoning engine for defensible decisions.",
    version="0.3.0",
)


def get_llm_client() -> LLMClient:
    """FastAPI dependency, shared by every reasoning endpoint. Defaults to a
    self-hosted Ollama model (docs/adr-0004-self-hosted-ollama-default.md);
    set RISEWISE_LLM_PROVIDER=anthropic to use the Anthropic API instead.
    Overridden in tests with a fake so they run without network access or a
    running LLM of either kind."""
    provider = os.environ.get("RISEWISE_LLM_PROVIDER", "ollama").lower()
    if provider == "anthropic":
        return AnthropicLLMClient()
    return OllamaLLMClient()


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


@app.post("/decisions/analyze", response_model=AnalyzeResponse)
def analyze_decision(
    request: StructureRequest, llm: LLMClient = Depends(get_llm_client)
) -> AnalyzeResponse:
    """Pipeline orchestrator: run Module 1 then Module 2 over the same raw
    input, in one call. A convenience layer only — /context/structure and
    /rita/scan remain independently callable and independently correct;
    this endpoint does not add any reasoning of its own (see adr-0003).
    """
    try:
        context = llm.structure(request.raw_input)
        scan = llm.rita_scan(context)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return AnalyzeResponse(raw_input=request.raw_input, context=context, scan=scan)
