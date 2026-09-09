"""Direct unit tests for OllamaLLMClient (constitution: keep reasoning
modules independent, test each one).

Uses httpx.MockTransport to simulate the Ollama server's REST API, so
these run offline without a real Ollama installation. This is the first
direct test of either LLM client's request/response handling — previous
tests only exercised clients indirectly through the FastAPI dependency
override.
"""

import httpx
import pytest

from backend.app.llm_client import OllamaLLMClient
from backend.app.schemas import DecisionContext


def _client_with_response(json_body: dict, status_code: int = 200) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code, json=json_body)

    return httpx.Client(transport=httpx.MockTransport(handler))


def _client_that_refuses_connection() -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("Connection refused", request=request)

    return httpx.Client(transport=httpx.MockTransport(handler))


STRUCTURE_PAYLOAD = {
    "decision_or_problem": "Should we adopt a four-day work week?",
    "objective": "Improve retention without hurting output",
    "constraints": ["Client SLAs require 5-day coverage"],
    "stakeholders": [{"name": "Employees", "role": "beneficiary"}],
    "time_horizon": "This fiscal year",
    "system_boundary": "Internal teams only",
    "known_evidence": [
        {"statement": "Attrition is up 12% year over year", "status": "source_record"}
    ],
    "unknown_information": ["Client tolerance for reduced coverage"],
}


def test_ollama_structure_parses_response() -> None:
    fake_http = _client_with_response(
        {"message": {"content": __import__("json").dumps(STRUCTURE_PAYLOAD)}}
    )
    llm = OllamaLLMClient(host="http://fake-ollama:11434", model="llama3.1", client=fake_http)
    context = llm.structure("Should we adopt a four-day work week?")
    assert isinstance(context, DecisionContext)
    assert context.decision_or_problem == STRUCTURE_PAYLOAD["decision_or_problem"]
    assert context.stakeholders[0].name == "Employees"


def test_ollama_raises_runtime_error_when_unreachable() -> None:
    llm = OllamaLLMClient(host="http://fake-ollama:11434", client=_client_that_refuses_connection())
    with pytest.raises(RuntimeError, match="Could not reach Ollama"):
        llm.structure("Anything")


def test_ollama_raises_runtime_error_on_http_error_status() -> None:
    fake_http = _client_with_response({"error": "model not found"}, status_code=404)
    llm = OllamaLLMClient(host="http://fake-ollama:11434", model="does-not-exist", client=fake_http)
    with pytest.raises(RuntimeError, match="pulled"):
        llm.structure("Anything")


def test_ollama_raises_runtime_error_on_non_json_content() -> None:
    fake_http = _client_with_response({"message": {"content": "Sure, here's my answer: ..."}})
    llm = OllamaLLMClient(host="http://fake-ollama:11434", client=fake_http)
    with pytest.raises(RuntimeError, match="did not return valid JSON"):
        llm.structure("Anything")


def test_ollama_defaults_come_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RISEWISE_OLLAMA_HOST", "http://custom-host:9999")
    monkeypatch.setenv("RISEWISE_OLLAMA_MODEL", "custom-model")
    llm = OllamaLLMClient()
    assert llm.host == "http://custom-host:9999"
    assert llm.model == "custom-model"
