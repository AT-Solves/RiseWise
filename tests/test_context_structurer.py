"""Tests for Module 1 (Context Structurer).

Uses a fake LLM client so these tests run without network access or an API
key. Deliberately exercises the endpoint with decisions from two unrelated
domains (a software decision and a civic-policy decision) to demonstrate
the module has no hardcoded scenario logic — it must work for any user
question or input.
"""

from fastapi.testclient import TestClient

from backend.app.main import app, get_llm_client
from backend.app.schemas import (
    DecisionContext,
    EvidenceStatus,
    KnownEvidenceItem,
    Stakeholder,
)


class FakeLLMClient:
    """Returns a fixed context regardless of input, so tests can assert the
    endpoint wires the LLM's response through untouched."""

    def __init__(self, context: DecisionContext) -> None:
        self._context = context

    def structure(self, raw_input: str) -> DecisionContext:
        return self._context


def _use_fake(context: DecisionContext) -> None:
    app.dependency_overrides[get_llm_client] = lambda: FakeLLMClient(context)


def teardown_function() -> None:
    app.dependency_overrides.clear()


def test_health() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_structure_context_software_decision() -> None:
    context = DecisionContext(
        decision_or_problem="Should the team migrate from REST to GraphQL?",
        objective="Reduce over-fetching for the mobile client",
        constraints=["2-sprint budget", "no breaking changes for existing partners"],
        stakeholders=[
            Stakeholder(name="Mobile team", role="beneficiary"),
            Stakeholder(name="Partner integrations", role="affected party"),
        ],
        time_horizon="Next quarter",
        system_boundary="API layer only; no client rewrite",
        known_evidence=[
            KnownEvidenceItem(
                statement="Mobile payload sizes are 3x larger than needed",
                status=EvidenceStatus.SOURCE_RECORD,
            )
        ],
        unknown_information=["Partner willingness to adopt a new schema"],
    )
    _use_fake(context)
    client = TestClient(app)
    response = client.post(
        "/context/structure", json={"raw_input": "Should we migrate from REST to GraphQL?"}
    )
    assert response.status_code == 200
    body = response.json()
    assert body["raw_input"] == "Should we migrate from REST to GraphQL?"
    assert body["context"]["decision_or_problem"] == context.decision_or_problem
    assert body["context"]["stakeholders"][0]["name"] == "Mobile team"


def test_structure_context_civic_decision() -> None:
    """A second, unrelated domain — proves the endpoint isn't tied to one scenario."""
    context = DecisionContext(
        decision_or_problem="Should the city introduce downtown congestion pricing?",
        objective="Reduce peak-hour traffic",
        constraints=["Political approval required", "Low-income commuter impact must be assessed"],
        stakeholders=[
            Stakeholder(name="Downtown commuters", role="affected party"),
            Stakeholder(name="City council", role="decision-maker"),
        ],
        time_horizon=None,
        system_boundary=None,
        known_evidence=[],
        unknown_information=["Effect on low-income commuters"],
    )
    _use_fake(context)
    client = TestClient(app)
    response = client.post(
        "/context/structure", json={"raw_input": "Should the city introduce congestion pricing?"}
    )
    assert response.status_code == 200
    assert response.json()["context"]["decision_or_problem"] == context.decision_or_problem


def test_structure_context_requires_llm_config_when_none_available() -> None:
    """Without a configured LLM client, the endpoint fails loudly (503) rather
    than silently fabricating a structure — constitution section 16: never
    compensate for missing evidence/config with confident output."""
    app.dependency_overrides.pop(get_llm_client, None)
    client = TestClient(app)
    response = client.post("/context/structure", json={"raw_input": "Anything at all"})
    assert response.status_code == 503


def test_structure_request_rejects_empty_input() -> None:
    client = TestClient(app)
    response = client.post("/context/structure", json={"raw_input": ""})
    assert response.status_code == 422
