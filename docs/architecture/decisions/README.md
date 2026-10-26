# Architecture Decision Records

Format: Context → Decision → Consequences. ADRs are immutable once accepted; a change is a new ADR that supersedes the old one.

All ADRs below were accepted with the RiseWise Knowledge Source Model v0.1 ([`../source-model.md`](../source-model.md)), approved by the product owner on 2026-10-26. They freeze the **shape** of the model only. No Vedic scholarly fact, citation convention or licence value is frozen by any ADR; those live in [`../../OPEN_QUESTIONS.md`](../../OPEN_QUESTIONS.md).

| ADR | Title | Status |
|---|---|---|
| [0001](0001-work-edition-source-snapshot-passage.md) | Separate Work, Edition, Source, SourceSnapshot and Passage | Accepted |
| [0002](0002-locus-distinct-from-passage.md) | Locus (address) is distinct from Passage (text) | Accepted |
| [0003](0003-translations-commentaries-are-separate-works.md) | Translations and commentaries are separate Works; commentary ≠ interpretation | Accepted |
| [0004](0004-immutable-content-addressed-snapshots.md) | Immutable, content-addressed snapshots and passages | Accepted |
| [0005](0005-preserve-original-text.md) | Preserve the original text; normalisation is additive; accents are text | Accepted |
| [0006](0006-evidence-backed-licences-contextual-rights.md) | Evidence-backed licences, most-restrictive rights, unknown = pending, rights per context | Accepted |
| [0007](0007-access-classes-and-availability-dimensions.md) | Five access classes; availability as stored dimensions with derived labels | Accepted |
| [0008](0008-separate-provenance-authority-verification-licence-availability.md) | Provenance, authority, verification, licence and availability are separate records | Accepted |
| [0009](0009-llm-output-is-never-a-source.md) | LLM output is never a source | Accepted |
| [0010](0010-no-silent-merging-no-substitution.md) | No silent merging of editions; no substitution of unavailable sources | Accepted |
| [0011](0011-domain-specifics-via-extensions.md) | Domain specifics only through extensions | Accepted |
