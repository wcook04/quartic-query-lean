# quartic-query-lean

A Lean formalisation of the nearly quartic separation between randomized and
quantum query complexity in
[OpenAI's preprint](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).
The preprint and its mathematics are OpenAI's.

Lean checks Theorem 1.1 of the preprint with no hypothesis:

```lean
theorem alphaTot_eq_four_unconditional : alphaTot = 4
```

`alphaTot` is the optimal exponent in equation (1). The checked development
includes the construction of the total functions, the randomized lower bound,
the quantum upper bound in an adaptive bit-query model, the exact Forrelation
circuit with its size bound, the universal quartic upper bound, and the
Forrelation randomized lower bound that the preprint imports from Bansal and
Sinha. Recorded Comparator runs accept these statements against separately
compiled challenges that import Mathlib only. The challenges share the maintained
statement vocabulary and theorem specifications; agreement does not replace
review of their mathematical meaning.

The Forrelation lower bound is proved along a shorter route than the published
one, in the weaker form the separation needs: fixed `k`, error `1/3`, and an
unspecified threshold in `m`. [The blueprint](docs/forrelation_lower_bound_blueprint.md)
describes the route, [an independent reading](docs/forrelation_lower_bound_review.md)
checks it, and [a prior-art search](docs/forrelation_route_prior_art.md) records
what is already known. No person has reviewed it yet.

## Start reading

- Follow the [Lean source map](lean/README.md) from the shared definitions to
  [the unconditional result](lean/QuarticQuery/Results/Unconditional.lean).
- Use the [statement corpus](corpus/README.md) to distinguish statement alignment,
  compilation and comparison evidence.
- Read the [document guide](docs/README.md) for the contract, reviews and their
  revision scope, or the [research guide](research/README.md) for source research,
  review decisions and writing requests.
- Read the maintained [long reasoning record](docs/reasoning_record.md) for the
  complete argument and its source correspondence. Its review sidecar identifies
  the assessed edition; the original returned drafts remain immutable evidence.

The [round-nine revision](research/adjudication/round9_revision.md) incorporates
the three [advisory returns](research/returns/round9/README.md) with individual
dispositions. It revises the mathematical explanations and reading routes;
these editorial checks are separate from the recorded formal proof checks.

## What is checked, and what that means

| Layer | State |
| --- | --- |
| Proofs | The `QuarticQuery` target builds at the recorded commit with no `sorry`, no custom axioms and no `native_decide`. |
| Statements | [Statement.lean](lean/QuarticQuery/Statement.lean) fixes every definition a theorem means. It imports Mathlib only. |
| Comparison | Comparator accepts each bundle in [lean/QuarticCorpus/](lean/QuarticCorpus/) against an independently compiled challenge, and rejects five deliberately wrong solutions for the intended reason. The unconditional bundle also passes every external kernel bundled with Lean (`--paranoid`). Runs on this machine are unsandboxed local rehearsals, and [corpus/receipts/](corpus/receipts/) records them as such. |
| Fidelity | [The review](docs/statement_fidelity_review.md) compares Lean statements with the preprint. It was done by an AI agent that did not write the proofs. No human has reviewed it. |
| Literature | Claims about cited sources were checked against those sources by AI agents; see [the adjudication](research/adjudication/adjudication_notes.md). |

The [round-three integration record](research/adjudication/round3_integration.md)
tracks the ten latest returns and their validation, following the
[round-two checkpoint](research/adjudication/round2_integration.md). New proof candidates do not
inherit the earlier build results. Current corpus evidence distinguishes
source-bound passes from stale or historically unbound receipts, and tracks
statement-review freshness independently of build and comparison freshness.

A compiled proof shows that a statement follows. Whether it says what the preprint
says is a separate question, which is why [corpus/](corpus/README.md) keeps these
facts apart for every statement and computes no overall score.

Some steps are proved along a different route from the preprint's, and each such
tie records this. The search for the erased zero gives `2G/m²` in place of
`4G/m²`. Theorem A.1 goes through
[complexitylib](https://github.com/cslib-community/complexitylib) instead of
Appendix A. Lemma 4.1 uses an induction on sub-distributions in place of the
supermartingale. [The contract](docs/statement_evidence_contract.md) explains how
statements and proofs stay aligned as derivations improve.

For website work, run `make reading-web` to export the four-paper reader with source-linked manuscript HTML, then start with the [frontend design brief](docs/frontend_brief.md). It connects the two reference readers to Quartic’s data and gives browser acceptance checks.

The [statement comparison reader](docs/reading_api.md#compare-a-paper-result-with-lean) opens a result in the original paper beside the exact Lean source, Lean’s printed type and axioms, and the reviewer’s reasons for its match. For the headline result it distinguishes the theorem proving the whole family from the shorter theorem proving the exponent alone.

The [selection resolver](docs/reading_api.md#resolve-a-paper-selection) opens a paper passage beside its Lean dependencies and readers can follow those declarations back to the papers. The [theorem application reader](docs/reading_api.md#inspect-a-theorem-application) follows the actual arguments used to assemble both bounds for one total function. The [website reading API](docs/reading_api.md) connects our three papers and OpenAI’s original PDF to Lean statements, source code and evidence about how each statement matches.

The [proof index](docs/proof_index.md) gives readable mathematical descriptions and links to the formal statements and their proofs. The [verification reference](docs/verification_details.md) keeps the detailed checking history outside the papers.

## Repository map

| Path | Purpose |
| --- | --- |
| [lean/](lean/README.md) | The Lake project: `QuarticQuery` holds the proofs, `QuarticCorpus` the Comparator bundles. |
| [corpus/](corpus/README.md) | Statement records, reviewed ties, receipts and the evidence graph. |
| [docs/](docs/README.md) | The evidence contract, the fidelity review, and the lower-bound blueprint, review and prior-art search. |
| [research/](research/README.md) | The statement ledger, research records and review requests. |
| [tools/](tools/README.md) | Generators and checks. |
| [tests/](tests/README.md) | Tests for the tools. |

## Check it

```sh
make check
```

Use Python 3.10 or newer, Git and Make for this command. It checks layout,
generated files and the Python tests. Lean needs a Mathlib
checkout at the pinned revision; the toolchain and dependencies are fixed by
[lean-toolchain](lean/lean-toolchain) and [lake-manifest.json](lean/lake-manifest.json).

```sh
cd lean && lake build QuarticQuery
```

```sh
python3 tools/run_comparator.py
```

## Reproducing the formal checks

The two papers and the record link to Lean sources and record passages pinned
at the round-nine source edition `8357f268732746d1575e05e7de8c888e20ad3793`.
The recorded Comparator run of the headline bundle
([its receipt](corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json))
was made at commit `9a0a5cdace28594058f6df59b9b2e45a9e7c1a4f`, in Comparator's
`--paranoid` mode and without a sandboxing tool (`--inadvisably-no-sandbox`).
The `lean/` directory is byte-identical between that checked revision and the
linked source edition; the round-nine changes are editorial. No fresh Lean or
Comparator run is claimed for them.
The toolchain is `leanprover/lean4:v4.36.0-rc2` and Mathlib is pinned at
`69552756cd8a2d2d48763cf7279fd814d6a1224d`.

From `lean/`:

```sh
lake build QuarticQuery
lake comparator --config QuarticCorpus/Unconditional/comparator.json --paranoid
lake env lean --run scripts/Reach.lean QuarticQuery.Checked.theorem_one_one
```

Add `--inadvisably-no-sandbox` to the Comparator command to reproduce the
recorded unsandboxed run. The last command prints the `QuarticQuery`
declarations in the dependency closure of the headline theorem: it traverses the
types and bodies of all constants the theorem reaches, in every namespace, and
displays the project projection, keeping one witness path for each edge that
passes through hidden constants.

Licensed under [Apache-2.0](LICENSE).

The [round-ten expert revision](research/adjudication/round10_revision.md) acts on
the first R10 return. Its evidence and dispositions are separate from the two
supporting-paper reviews recorded in the [complete R10 assimilation](research/adjudication/round10_remaining_revision.md).
