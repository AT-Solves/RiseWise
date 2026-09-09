"""Tests for the pipeline orchestrator (/decisions/analyze).

Uses a fake LLM client implementing both structure() and rita_scan(), so
these run offline. Covers two unrelated domains to demonstrate the
orchestrator adds no scenario-specific logic of its own — it only chains
Module 1 and Module 2.
"""

from fastapi.testclient import TestClient

from backend.app.main import app, get_llm_client
from backend.app.schemas import (
    ConfidenceLevel,
    DecisionContext,
    EvidenceStatus,
    RitaDimension,
    RitaFinding,
    RitaScan,
    Stakeholder,
)


class FakeLLMClient:
    """Returns fixed, distinguishable outputs from each method, so tests can
    assert the orchestrator actually calls both and wires their outputs
    together correctly — not just one of them."""

    def __init__(self, context: DecisionContext, scan: RitaScan) -> None:
        self._context = context
        self._scan = scan
        self.structure_calls = 0
        self.rita_scan_calls = 0

    def structure(self, raw_input: str) -> DecisionContext:
        self.structure_calls += 1
        return self._context

    def rita_scan(self, context: DecisionContext) -> RitaScan:
        self.rita_scan_calls += 1
        # Assert the orchestrator passes Module 1's actual output into
        # Module 2, not the raw input or something else.
        assert context == self._context
        return self._scan


def _use_fake(context: DecisionContext, scan: RitaScan) -> FakeLLMClient:
    fake = FakeLLMClient(context, scan)
    app.dependency_overrides[get_llm_client] = lambda: fake
    return fake


def teardown_function() -> None:
    app.dependency_overrides.clear()


def _sample_context(decision: str) -> DecisionContext:
    return DecisionContext(
        decision_or_problem=decision,
        objective="Some objective",
        constraints=[],
        stakeholders=[Stakeholder(name="Someone", role="affected party")],
        time_horizon=None,
        system_boundary=None,
        known_evidence=[],
        unknown_information=[],
    )


def _sample_scan() -> RitaScan:
    return RitaScan(
        findings=[
            RitaFinding(
                dimension=RitaDimension.TEMPORAL_ALIGNMENT,
                observation="Some observation.",
                risk_or_opportunity="Some risk.",
                key_questions=[],
                evidence_status=EvidenceStatus.HYPOTHESIS,
                confidence=ConfidenceLevel.MEDIUM,
            )
        ]
    )


def test_analyze_chains_structure_and_scan_software_domain() -> None:
    context = _sample_context("Should the team migrate from REST to GraphQL?")
    scan = _sample_scan()
    fake = _use_fake(context, scan)
    client = TestClient(app)
    response = client.post(
        "/decisions/analyze", json={"raw_input": "Should we migrate from REST to GraphQL?"}
    )
    assert response.status_code == 200
    body = response.json()
    assert body["raw_input"] == "Should we migrate from REST to GraphQL?"
    assert body["context"]["decision_or_problem"] == context.decision_or_problem
    assert body["scan"]["findings"][0]["dimension"] == "temporal_alignment"
    assert fake.structure_calls == 1
    assert fake.rita_scan_calls == 1


def test_analyze_chains_structure_and_scan_civic_domain() -> None:
    """A second, unrelated domain — proves the orchestrator isn't tied to
    one scenario; it just chains whatever the two modules produce."""
    context = _sample_context("Should the city introduce downtown congestion pricing?")
    scan = _sample_scan()
    _use_fake(context, scan)
    client = TestClient(app)
    response = client.post(
        "/decisions/analyze", json={"raw_input": "Should the city introduce congestion pricing?"}
    )
    assert response.status_code == 200
    assert response.json()["context"]["decision_or_problem"] == context.decision_or_problem


def test_analyze_requires_llm_config_when_none_available() -> None:
    app.dependency_overrides.pop(get_llm_client, None)
    client = TestClient(app)
    response = client.post("/decisions/analyze", json={"raw_input": "Anything"})
    assert response.status_code == 503


def test_analyze_rejects_empty_input() -> None:
    client = TestClient(app)
    response = client.post("/decisions/analyze", json={"raw_input": ""})
    assert response.status_code == 422
