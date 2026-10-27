# Architecture Decision Records

Format: Context → Decision → Consequences. ADRs are immutable once accepted; a change is a new ADR that supersedes the old one. The only permitted edit to an accepted ADR is adding a dated cross-reference to its status line (e.g. "Amended by ADR-0021").

ADR-0001 … 0011 were accepted with the RiseWise Knowledge Source Model v0.1 ([`../source-model.md`](../source-model.md)), approved by the product owner on 2026-10-26. They freeze the **shape** of the model only. No Vedic scholarly fact, citation convention or licence value is frozen by any ADR; those live in [`../../OPEN_QUESTIONS.md`](../../OPEN_QUESTIONS.md).

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
| [0012](0012-conservative-rights-policy-silence-is-not-permission.md) | Conservative rights policy — silence is not permission (refines 0006; resolves C-009) | Accepted |
| [0013](0013-typescript-and-zod-for-domain-models.md) | TypeScript and Zod for domain models and validation schemas (only) | Accepted |
| [0014](0014-retire-python-prototype-as-core-implementation.md) | Retire the Python prototype as the core implementation path | Accepted |
| [0015](0015-evidence-span-offsets.md) | Evidence span offsets | Accepted |
| [0016](0016-citation-scheme-scope-and-locus-mappings.md) | Citation-scheme scope and explicit locus mappings (amends 0002) | Accepted |
| [0017](0017-identifier-scheme.md) | Identifier scheme | Accepted |
| [0018](0018-sourcesnapshot-granularity.md) | SourceSnapshot granularity (refines 0004) | Accepted |
| [0019](0019-annotation-alignment.md) | Annotation alignment | Accepted |
| [0020](0020-root-text-designation.md) | ROOT_TEXT is a reviewed designation, not a layer or an authority tier | Accepted |
| [0021](0021-acquired-bytes-and-decoded-passage-text.md) | Acquired bytes and decoded passage text (amends 0005) | Accepted |
| [0022](0022-passage-granularity-and-cross-passage-evidence-spans.md) | Passage granularity and cross-passage evidence spans | Accepted |
