# Source model examples (metadata only)

These YAML files walk real and hypothetical cases through the RiseWise Knowledge Source Model v0.1 ([`../source-model.md`](../source-model.md)). They are a **paper test of the model**, not a schema, not seed data, and not an import specification.

## Conventions

- **No corpus text.** Every textual payload is a `<placeholder>`. Nothing was downloaded or ingested to write these files.
- **Verification tags.** Any fact about a real source carries `tag: V | S | K` (see the legend in `source-model.md`). `S` and `K` facts are unverified and are tracked in [`../../OPEN_QUESTIONS.md`](../../OPEN_QUESTIONS.md); they must not be copied into implementation as truth.
- **Hypothetical examples** are marked `hypothetical: true` and use placeholder names.
- **Identifiers** such as `work:rv` are illustrative human-readable keys; the identifier scheme is still open (OQ-E01).
- Field names follow the design document but are **not frozen**; schema design (Step 2) may rename them.
- Computed values (effective rights, access class, display label, evidence eligibility) are shown under `computed:` to make the paper test explicit. They are not stored fields.

## Files

| File | Design § | Paper-test case |
|---|---|---|
| `01-rigveda-passage.yaml` | §13 | — (multi-layer alignment) |
| `02-taittiriya-samhita-passage.yaml` | §14 | — (derivation chain, partial coverage) |
| `03-panini-rule.yaml` | §15 | Case 3: uncertain licence |
| `04-external-restricted-source.yaml` | §16 | Case 2: copyrighted, not redistributable |
| `05-user-supplied-source.yaml` | §17 | Case 4: user-uploaded private source |
| `06-paper-test-public-domain.yaml` | §22 | Case 1: fully available public-domain source (hypothetical) |
| `07-paper-test-edition-disagreement.yaml` | §22 | Case 5: two editions disagree at one locus (hypothetical) |
