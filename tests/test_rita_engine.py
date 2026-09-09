"""Tests for Module 2 (RITA Engine).

Uses a fake LLM client so these tests run without network access or an API
key. Feeds Decision Contexts from two unrelated domains through the same
endpoint to demonstrate the module carries no scenario-specific logic.
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
    """Returns a fixed scan regardless of input context, so tests can assert
    the endpoint wires the LLM's response through untouched."""

    def __init__(self, scan: RitaScan) -> None:
        self._scan = scan

    def structure(self, raw_input: str):  # pragma: no cover - not exercised here
        raise NotImplementedError

    def rita_scan(self, context: DecisionContext) -> RitaScan:
        return self._scan


def _use_fake(scan: RitaScan) -> None:
    app.dependency_overrides[get_llm_client] = lambda: FakeLLMClient(scan)


def teardown_function() -> None:
    app.dependency_overrides.clear()


SOFTWARE_CONTEXT = DecisionContext(
    decision_or_problem="Should the team migrate from REST to GraphQL?",
    objective="Reduce over-fetching for the mobile client",
    constraints=["2-sprint budget"],
    stakeholders=[Stakeholder(name="Mobile team", role="beneficiary")],
    time_horizon="Next quarter",
    system_boundary="API layer only",
    known_evidence=[],
    unknown_information=["Partner willingness to adopt a new schema"],
)

CIVIC_CONTEXT = DecisionContext(
    decision_or_problem="Should the city introduce downtown congestion pricing?",
    objective="Reduce peak-hour traffic",
    constraints=["Political approval required"],
    stakeholders=[Stakeholder(name="Downtown commuters", role="affected party")],
    time_horizon=None,
    system_boundary=None,
    known_evidence=[],
    unknown_information=["Effect on low-income commuters"],
)


def _sample_scan(observation: str) -> RitaScan:
    return RitaScan(
        findings=[
            RitaFinding(
                dimension=RitaDimension.RELATIONAL_INTEGRITY,
                observation=observation,
                risk_or_opportunity="Some stakeholders may bear disproportionate cost.",
                key_questions=["Who is excluded from this decision?"],
                evidence_status=EvidenceStatus.INTERPRETATION,
                confidence=ConfidenceLevel.MEDIUM,
            ),
            RitaFinding(
                dimension=RitaDimension.ADAPTIVE_REGENERATION,
                observation="No information given about recovery capacity.",
                risk_or_opportunity="Unknown resilience if the intervention fails.",
                key_questions=[],
                evidence_status=EvidenceStatus.UNKNOWN,
                confidence=ConfidenceLevel.LOW,
            ),
        ]
    )


def test_rita_scan_software_context() -> None:
    scan = _sample_scan("Mobile team benefits; partner integrations bear migration cost.")
    _use_fake(scan)
    client = TestClient(app)
    response = client.post("/rita/scan", json={"context": SOFTWARE_CONTEXT.model_dump()})
    assert response.status_code == 200
    body = response.json()
    assert len(body["scan"]["findings"]) == 2
    assert body["scan"]["findings"][0]["dimension"] == "relational_integrity"
    assert body["context"]["decision_or_problem"] == SOFTWARE_CONTEXT.decision_or_problem


def test_rita_scan_civic_context() -> None:
    """A second, unrelated domain — proves the endpoint isn't tied to one scenario."""
    scan = _sample_scan("Commuters who can't afford the fee bear the cost; council benefits from reduced congestion.")
    _use_fake(scan)
    client = TestClient(app)
    response = client.post("/rita/scan", json={"context": CIVIC_CONTEXT.model_dump()})
    assert response.status_code == 200
    body = response.json()
    assert body["context"]["decision_or_problem"] == CIVIC_CONTEXT.decision_or_problem
    assert body["scan"]["findings"][1]["evidence_status"] == "unknown"


def test_rita_scan_requires_llm_config_when_none_available() -> None:
    app.dependency_overrides.pop(get_llm_client, None)
    client = TestClient(app)
    response = client.post("/rita/scan", json={"context": SOFTWARE_CONTEXT.model_dump()})
    assert response.status_code == 503


def test_rita_scan_rejects_missing_context() -> None:
    client = TestClient(app)
    response = client.post("/rita/scan", json={})
    assert response.status_code == 422


def test_rita_finding_rejects_invalid_dimension() -> None:
    import pytest
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        RitaFinding(
            dimension="not_a_real_dimension",
            observation="x",
            risk_or_opportunity="y",
            evidence_status=EvidenceStatus.UNKNOWN,
            confidence=ConfidenceLevel.LOW,
        )
