"""Pydantic schemas for the RiseWise Context Structurer (RITA Framework, Module 1).

These types define the Decision Context produced by Step 1 of the RiseWise
reasoning pipeline. The structure is deliberately domain-agnostic: it must
hold for any decision or question a user brings to RiseWise, not a single
demo scenario. Nothing in this file may encode assumptions specific to one
topic or industry.
"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class EvidenceStatus(str, Enum):
    """Evidence Integrity Layer classification (constitution section 5).

    Every claim RiseWise handles must be classified as one of these six —
    never presented as fact when it is really an interpretation or
    assumption.
    """

    VERIFIED_EVIDENCE = "verified_evidence"
    SOURCE_RECORD = "source_record"
    INTERPRETATION = "interpretation"
    ASSUMPTION = "assumption"
    HYPOTHESIS = "hypothesis"
    UNKNOWN = "unknown"


class KnownEvidenceItem(BaseModel):
    statement: str = Field(
        ..., description="A single fact, data point, or claim already present in the user's input."
    )
    status: EvidenceStatus = Field(
        ..., description="Evidence Integrity classification for this statement."
    )


class Stakeholder(BaseModel):
    name: str = Field(..., description="Who or what group is affected by or involved in the decision.")
    role: Optional[str] = Field(
        None,
        description="Their relationship to the decision, e.g. beneficiary, affected party, decision-maker, excluded party.",
    )


class StructureRequest(BaseModel):
    raw_input: str = Field(
        ...,
        min_length=1,
        description="The user's decision or question, in their own words. Any topic or domain.",
    )


class DecisionContext(BaseModel):
    """Structured Decision Context — output of RiseWise pipeline Step 1 (constitution section 6)."""

    decision_or_problem: str
    objective: str
    constraints: List[str] = Field(default_factory=list)
    stakeholders: List[Stakeholder] = Field(default_factory=list)
    time_horizon: Optional[str] = None
    system_boundary: Optional[str] = None
    known_evidence: List[KnownEvidenceItem] = Field(default_factory=list)
    unknown_information: List[str] = Field(default_factory=list)


class StructureResponse(BaseModel):
    context: DecisionContext
    raw_input: str
