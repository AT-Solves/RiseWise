# ADR-0008: Provenance, authority, verification, licence and availability are separate records

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §2 (P6), §6, §7, §8, §10

## Context
These five concepts are easily conflated: "we know where it came from" (provenance) is not "it deserves weight" (authority), which is not "its digital copy was checked" (verification), which is not "we may use it" (licence), which is not "we hold it" (availability).

## Decision
Each concept is a separate record type with its own history:

| Concept | Record | Answers |
|---|---|---|
| Provenance | ProvenanceRecord (upstream claims + RiseWise activities) | Where did it come from, and what was done to it? |
| Authority | AuthorityAssessment (per domain and purpose, with rationale) | How much weight does it carry for this purpose? |
| Verification | VerificationRecord (check, method, result, verifier) | Has its fidelity/integrity been checked? |
| Licence | LicenceRecord (evidence-backed) → computed RightsDecision | What may we do with it, in this context? |
| Availability | AvailabilityRecord (holding, origin, coverage, reasons) | What do we actually hold? |

Upstream provenance is stored as **claims** with their own source and verification status, not accepted as fact. Source verification states are distinct from Tarka's claim statuses.

## Consequences
- UI and API can show all five independently; none can be inferred from another.
- Authority is never derived from popularity or usage.
