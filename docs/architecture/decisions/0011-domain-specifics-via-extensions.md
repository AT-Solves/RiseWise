# ADR-0011: Domain specifics only through extensions

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §2 (P9), §11, §12

## Context
The source model must serve General, Vedic/Sanskrit, and later History, Science, Law and Product/Business. Hard-coding Vedic structures (maṇḍala, sūkta, kāṇḍa, padapāṭha, sūtra relations) into the core would block other domains.

## Decision
- Core entities are domain-neutral.
- Domain extensions declare: citation schemes, layer types, Work extension fields, annotation body schemas, extra relation predicates, authority rubrics, and domain verification rules. Extensions are versioned.
- The first extensions are `general` and `vedic-sanskrit`.
- **Extension content is provisional data, not architecture.** In particular, the `vedic-sanskrit` citation schemes, layer names and attributions in source-model.md §11 are provisional until confirmed by an expert (OPEN_QUESTIONS OQ-V*). Correcting them produces a new extension/scheme version, not a new ADR.

## Consequences
- Adding a domain does not change core entities.
- Uncertain scholarly facts cannot become architectural truth by accident.
