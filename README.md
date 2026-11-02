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
Sinha. Comparator accepts these statements against an independent challenge that
imports Mathlib only.

The Forrelation lower bound is proved along a shorter route than the published
one, in the weaker form the separation needs: fixed `k`, error `1/3`, and an
unspecified threshold in `m`. [The blueprint](docs/forrelation_lower_bound_blueprint.md)
describes the route, [an independent reading](docs/forrelation_lower_bound_review.md)
checks it, and [a prior-art search](docs/forrelation_route_prior_art.md) records
what is already known. No person has reviewed it yet.

## What is checked, and what that means

| Layer | State |
| --- | --- |
| Proofs | The `QuarticQuery` target builds at the recorded commit with no `sorry`, no custom axioms and no `native_decide`. |
| Statements | [Statement.lean](lean/QuarticQuery/Statement.lean) fixes every definition a theorem means. It imports Mathlib only. |
| Comparison | Comparator accepts each bundle in [lean/QuarticCorpus/](lean/QuarticCorpus/) against an independently compiled challenge, and rejects five deliberately wrong solutions for the intended reason. The unconditional bundle also passes every external kernel bundled with Lean (`--paranoid`). Runs on this machine are unsandboxed local rehearsals, and [corpus/receipts/](corpus/receipts/) records them as such. |
| Fidelity | [The review](docs/statement_fidelity_review.md) compares Lean statements with the preprint. It was done by an AI agent that did not write the proofs. No human has reviewed it. |
| Literature | Claims about cited sources were checked against those sources by AI agents; see [the adjudication](research/returns/adjudication_notes.md). |

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

## Repository map

| Path | Purpose |
| --- | --- |
| [lean/](lean/) | The Lake project: `QuarticQuery` holds the proofs, `QuarticCorpus` the Comparator bundles. |
| [corpus/](corpus/README.md) | Statement records, reviewed ties, receipts and the evidence graph. |
| [docs/](docs/) | The evidence contract, the fidelity review, and the lower-bound blueprint, review and prior-art search. |
| [research/](research/README.md) | The statement ledger, research records and review requests. |
| [tools/](tools/README.md) | Generators and checks. |
| [tests/](tests/) | Tests for the tools. |

## Check it

```sh
make check
```

This checks layout, generated files and the Python tests. Lean needs a Mathlib
checkout at the pinned revision; the toolchain and dependencies are fixed by
[lean-toolchain](lean/lean-toolchain) and [lake-manifest.json](lean/lake-manifest.json).

```sh
cd lean && lake build QuarticQuery
```

```sh
python3 tools/run_comparator.py
```

Licensed under [Apache-2.0](LICENSE).
