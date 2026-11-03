# Lean source and verification bundles

This directory is one Lake project, configured by [lakefile.toml](lakefile.toml),
[lean-toolchain](lean-toolchain) and [lake-manifest.json](lake-manifest.json).
Its two libraries have different jobs: `QuarticQuery` contains the development;
`QuarticCorpus` contains the Comparator challenges and solutions.

## Where to start reading

1. [Statement.lean](QuarticQuery/Statement.lean) defines the shared vocabulary.
2. [Results/Unconditional.lean](QuarticQuery/Results/Unconditional.lean) contains
   the unconditional headline and the combined Theorem 1.1 declaration.
3. [Results/Conditional.lean](QuarticQuery/Results/Conditional.lean) shows the
   assembly before the Forrelation lower-bound hypothesis is discharged.
4. [QuarticQuery.lean](QuarticQuery.lean) is the library's import entry point.
   Some component modules enter through its imports rather than appearing there
   directly.

## Component map

| Directory | Responsibility |
| --- | --- |
| [Model/](QuarticQuery/Model/) | Classical and quantum query models. |
| [Construction/](QuarticQuery/Construction/) | The total-function construction, transcripts and local tests. |
| [Tournament/](QuarticQuery/Tournament/) | Drift and the ideal tournament process. |
| [Forrelation/](QuarticQuery/Forrelation/) | Promise, circuit construction and repetition. |
| [ForrelationLower/](QuarticQuery/ForrelationLower/) | The Forrelation lower-bound development. |
| [Amplification/](QuarticQuery/Amplification/) | Amplification geometry, averages and procedures. |
| [LowerBound/](QuarticQuery/LowerBound/) | Direct product, minimax and the planted-input construction. |
| [Upper/](QuarticQuery/Upper/) | The quantum upper-bound implementation and its component procedures. |
| [Bridge/](QuarticQuery/Bridge/) and [Appendix/](QuarticQuery/Appendix/) | Interfaces to the imported query-complexity development and Theorem A.1. |
| [Results/](QuarticQuery/Results/) | Exponents, headline statements and the final assembly. |
| [Paper/](QuarticQuery/Paper/) | Statement-alignment companions and returned proof candidates; consult their build evidence before relying on a declaration. |

## Checking and recorded evidence

Each positive bundle in [QuarticCorpus/](QuarticCorpus/) contains an authored
`Solution.lean`, a `comparator.json` configuration and a generated
`Challenge.lean`. Regenerate challenges through
[build_challenges.py](../tools/build_challenges.py). The
[Negative/](QuarticCorpus/Negative/) cases deliberately supply wrong solutions;
they are expected to be rejected for their specified reasons.

[scripts/Reach.lean](scripts/Reach.lean) reads the compiled environment for the
dependency record. Build and Comparator commands are documented in the
[maintenance guide](../tools/README.md#generate-and-check-the-lean-evidence).
The [corpus guide](../corpus/README.md) explains their recorded outputs.

Module paths and declaration names are referenced by statement ties, challenge
configurations and receipts. Preserve those interfaces when organising files.

Some `Paper/` module headers retain the submitted reviewers' descriptions of
their drafts as unelaborated or written without a compiler. Those comments
record the submission environment. Use the current source-bound receipts and
reviewed statement ties in [the corpus](../corpus/README.md) for acceptance of
the integrated source; the original returns remain unchanged.

## Round-four additions

[RealizedCaps.lean](QuarticQuery/LowerBound/RealizedCaps.lean) bounds the joint
success-and-compliance event for initially uncapped trees;
[RealizedCapsExternal.lean](QuarticQuery/LowerBound/RealizedCapsExternal.lean)
averages it over a finite external seed. [UniformEndpoint.lean](QuarticQuery/Upper/UniformEndpoint.lean)
and [ConstructionForrelationSharp.lean](QuarticQuery/Paper/ConstructionForrelationSharp.lean)
hold the coherent amplifier and sharp decoder; the `RealLeaf*` modules extend the
Forrelation lower bound to bounded real leaves. Their bundles live under
[Independent/](QuarticCorpus/Independent/) (`RealizedCaps`, `UniformAmplifier`,
`DecoderSharp`, `Degree`, `ModelZero`, `RealLeaves`), are authored rather than
generated, and run through the [round-four runner](../tools/return_checks/round4_formal.py).
Outcomes, repairs and remaining gaps are in the
[adjudication](../research/adjudication/round4_formal.md).

## Independent round-three checks

[Eq19Whole.lean](QuarticQuery/Paper/Eq19Whole.lean) states both the equality and
probability bound in equation (19). [Eq19Complete.lean](QuarticQuery/Paper/Eq19Complete.lean)
states the same display with the bound on the expected-count quotient.
[Independent/Eq19/](QuarticCorpus/Independent/Eq19/) gives a separately authored
product-law specification, bridges to the maintained definitions and direct and
independent Comparator targets. These authored challenges are outside the
one-level generated-bundle route and must not be regenerated from the solutions.
Audit modules should import each inspected target module directly: a private
intermediary import does not make its names available to the audit in Lean's
module system.

[Independent/Semantics.lean](QuarticCorpus/Independent/Semantics.lean) proves
finite expectations against the actual query and promise definitions;
[SemanticMutations.lean](QuarticCorpus/Independent/SemanticMutations.lean)
shows which answers change under deliberately incorrect alternatives.
[SharedAudit.lean](QuarticCorpus/Independent/Controls/SharedAudit.lean) distinguishes
a concrete comparison witness from an impossible shared premise that Comparator
can accept vacuously. Use the [native runner](../tools/return_checks/round3_formal.py)
and [adjudication](../research/adjudication/round3_formal.md) for current outcomes.

[ConstructionFull.lean](QuarticQuery/Paper/ConstructionFull.lean) conjoins the
finite-count/coherent-query construction theorem with full physical-coordinate
essentiality witnesses. The older `construction_lemma_2_2_complete` declaration
keeps its existing interface and does not itself assert that support clause.
