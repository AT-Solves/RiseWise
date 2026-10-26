# ADR-0007: Five access classes; availability as stored dimensions with derived labels

- **Status:** Accepted (2026-10-26)
- **Design reference:** source-model.md §7, §10; CONFLICTS.md C-001

## Context
RiseWise must distinguish material it can redistribute, use internally only, require users to import, cannot hold, or has not yet cleared. The initially proposed availability states mixed three independent dimensions (content held, rights, origin), which forces false choices (a source can be both partial and licence-pending).

## Decision
- **Access classes** (computed per use context): `REDISTRIBUTABLE`, `INTERNAL_USE_ONLY`, `USER_IMPORT_ONLY`, `UNAVAILABLE`, `LICENCE_PENDING`.
- **Stored availability dimensions:** Holding (`FULL_TEXT`, `PARTIAL_TEXT`, `IMAGE_ONLY`, `METADATA_ONLY`, `NONE`), Origin (`CURATED_IMPORT`, `FIRST_PARTY`, `USER_SUPPLIED`), Coverage (covered/missing loci), and reason codes (`NOT_ACQUIRED`, `LICENCE_RESTRICTED`, `NO_DIGITAL_TEXT`, `NOT_EXTANT`, `NOT_PUBLISHED`, `UNKNOWN`).
- **Display labels are derived** (first match wins): `LICENCE_PENDING`, `NOT_AVAILABLE` (+reason), `REFERENCE_ONLY`, `IMPORT_REQUIRED`, `SCAN_ONLY`, `PARTIAL`, `AVAILABLE`. `USER_SUPPLIED` is an origin badge, not a state.
- Availability never implies reliability.

## Consequences
- "We don't have this source" is represented honestly, with a reason.
- Labels can evolve without data migration because they are derived.
