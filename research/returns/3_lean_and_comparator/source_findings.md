# Source findings and limits

Research date: **2026-11-01**. This file distinguishes source inspection, mathematical inference, and unperformed verification.

## Deliverables and scope

`new_prior_art.json` has the same fourteen keys as the packet's quantum-prior-art records. It contains eight records: four substantially rechecked model candidates, Mathlib at the actual target pin, and three additional public repositories. `reuse_checked.json` records 49 declarations with full commit SHA, source path, line, copied signature, and a source URL. The additional catalogue is useful evidence for the statement plan; it is not itself a proof dependency.

The workstream reviewed `READ_ME_FIRST.md`, both named classical/quantum prior-art JSON files, `literature/references_resolved.json`, and the relevant model, construction, amplification, tournament, and direct-product sections of `paper/extracted.md`. The team separately owns the full statement-ledger and Comparator audit. The earlier AI-written catalogues were treated as leads; the descriptions below come from opened source files, not their claims of proof completeness.

Inspection means that source was fetched at the full SHA and its declarations, assumptions, toolchain, dependency manifest, and applicable licence were read. It **does not mean** that the source compiled, that every imported theorem was recursively audited, or that any theorem was replayed with Comparator. No Lean/lake/elan executable was available. All formalization and compatibility conclusions remain conditional on those checks.

## New or materially improved findings

| Finding | Opened primary source | What it supplies | What it does not establish |
|---|---|---|---|
| Target-pin Hadamard matrices | [Mathlib HadamardMatrix.lean][hadamard] and [PR 38582][pr] | `Matrix.IsHadamard`, Kronecker construction, and a matrix-product criterion already present in the target Mathlib. | Fourier growth, Forrelation's classical lower bound, or the paper's exact Walsh circuit. |
| Finite adaptive probability kernels | [arlib SequentialKernel.lean][arlib-kernel] and [SequentialDominate.lean][arlib-dominate] | `Arlib.Probability.seqWeight`, normalization, sequential-law domination. | The capped direct-product theorem, a Bellman-product supermartingale, or adaptive transcript factorization. |
| Product-fiber conditioning | [arlib ProductFiber.lean][arlib-fiber] | `Arlib.Probability.CoinSpace.condPr_eq_blockPr`, `condPr_fiber_eq`, and independence for specified blocks. | Conditioning on an adaptively revealed transcript without first proving the appropriate rectangular structure. |
| An actual formalized multiplicative-weights precedent | [girving/debate Learn/Indistinguishable.lean][debate] and [author's Zulip thread][zulip] | Exponential reweighting, a KL potential, convergence, and a small indistinguishable circuit existence result. | The paper's quadratic-complementarity drift or its tournament proposition. The author explicitly separates circuit existence from sample complexity. |
| Further Hadamard/register implementation | [VerifiedQC/ForShor Hadamard.lean][forshor] and [VQC Lab projects page][vqc] | `Shor.eval_Hreg_zero_uniform` and register-preservation lemmas. | A discharged concrete quantum semantics: the inspected theorems retain typeclass hypotheses. It is not a query-complexity lower bound. |
| Stronger Troy amplification audit | [Amplification.lean][amp] and [Geometry.lean][geometry] | Exact conditional output law, zero-success case, a hard budget expression, and invariant-plane state algebra. | The paper's complete state-preservation wrapper, arbitrary failure tolerance, or the public-model bridge without further work. |
| Actual QudeLeap endpoint audit | [Results.lean][qude] | `algorithm_solves` and explicit preparation/inverse/mark counts. | Automatic off-promise resource guarantees after discarding validity and supported-path assumptions. |
| Existing quartic upper-bound route | [complexitylib Adversary.lean][adversary], [Polynomial.lean][polynomial], [Midrijanis.lean][midrijanis] | `complexity_le_mul_pow_four`, `blockSensitivity_le_sixteen_mul_sq`, `complexity_le_degree_mul_blockSensitivity`. | Equality of the paper's `Q` and this fixed controlled-phase model. |

The new arlib, debate, and ForShor repositories all have opened Apache-2.0 licences. Their specific toolchains and Mathlib pins are in the JSON. Importing them all would add incompatible version closures and redundant probability/execution representations. The recommendation is narrow adaptation where the benefit survives a port prototype; an available name is not a reason to add a dependency.

## Corrections to the intake

1. **complexitylib has arbitrary finite workspace.** Its `State N W` is indexed by `Fin N × Bool × W`. The earlier description of a trivial workspace is false. [Search.lean][search]
2. **Its oracle is controlled phase.** The second basis coordinate controls the phase. A phase-only model lacking that control would be a materially different oracle convention. [Search.lean][search]
3. **Its quantum theorem is per algorithm.** The inspected quantum modules do not define a scalar `Q(f)` minimum. A bridge and attainment theorem are needed to obtain the theorem in the new scalar API. [Adversary.lean][adversary]
4. **The cslib dependency must follow the manifest.** complexitylib's pinned manifest selects `254e30e6d4299c51323aaeaf5f51a4763b375d4a`, not the separately sampled cslib commit from the intake. [lake-manifest.json][manifest]
5. **QudeLeap's inspected manifest does not depend on cslib.** It does have its own older Mathlib pin and extensive execution framework. [manifest][qude-manifest]
6. **`AdaptiveWeights.lean` is not Hedge.** It develops weighted adaptive branch/transcript calculations. It does not provide the paper's tournament drift merely because of its filename. [AdaptiveWeights.lean][weights]
7. **Troy's oracle is not the literal paper oracle.** The native answer register has a blank symbol, and a query swaps that blank with the observed symbol. Existing factor-two native/XOR results do not automatically supply the complete complexitylib or public-model translation. [Oracle.lean][oracle], [Simulation.lean][simulation]
8. **A conditional output law is weaker than a full successful-state law.** The former is exactly useful for sampling candidates; it must not replace the stronger statement in Lemma 3.1. Troy's geometry is a promising route to the latter. [Amplification.lean][amp], [Geometry.lean][geometry]
9. **A natural `sInf` is not automatically a well-behaved minimum.** Troy explicitly discusses feasible query-count sets and observational determinacy. The public model must discharge the corresponding gate. [Complexity.lean][complexity], [Simulation.lean][simulation]
10. **The OpenAI factoring framework counts different resources.** Its finite gate set, input-wire model, and uniformity conditions should not be imposed on a query-complexity theorem. Its quarter-success amplification theorem is a special endpoint. [Basic.lean][oai], [PhysicalAmplification.lean][oai-amp]
11. **Hadamard support does not require Mathlib master.** The opened module exists at `69552756cd8a2d2d48763cf7279fd814d6a1224d`. PR metadata has a Bors-merge title but a null `merged_at`; the pinned source, not that field, establishes availability. [HadamardMatrix.lean][hadamard], [PR 38582][pr]

## Search coverage and honest negative results

The search combined public web queries, repository metadata, commit-pinned source retrieval, repository file lists, and indexed GitHub code queries. It covered the requested themes: Forrelation, Bansal–Sinha, Fourier growth, direct-product theorems, multiplicative weights, Dürr–Høyer/minimum finding, Grover search, and amplitude amplification.

No directly reusable Lean proof of the exact Forrelation lower bound, the paper's capped direct-product theorem, or its complete separation was located in this bounded search. This statement is deliberately narrower than “no such formalization exists.”

The retained `search_receipts.json` documents several queries and limitations:

- `Forrelation language:Lean`, `"Bansal" "Sinha" language:Lean`, and `"Shaltiel" language:Lean` returned zero indexed results at query time.
- `"Fourier growth" language:Lean` returned two unrelated matches in the inspected results.
- `"direct product" language:Lean` returned a large number of mostly algebraic matches; a raw result count provides little evidence about complexity-theoretic direct products.
- Some Høyer/Drucker-related queries hit HTTP 429. Those are **failed searches**, not negative findings.
- A `HadamardMatrix` code search returned zero even though the exact target file was successfully fetched. This is direct evidence that the code index is incomplete.
- A promising Tanner Duve quantum-algorithms blog URL returned 404 when opened. It was not used as verified formalization evidence.
- The Hayata–Yamasaki lean-quantum repository was encountered, but this workstream did not inspect relevant query-complexity declarations from it. It is not a recommended dependency on the strength of its name.

There is a public [OpenMaths course on this exact separation][openmaths] with a [provider record][openmaths-providers]. The opened record labels the exposition AI-authored, self-checked, and without completed independent review. It retains the Forrelation lower bound as a named assumption. It can help locate expanded explanations, but it is neither a Lean proof nor independent validation of the paper. No immutable source commit was established for that site, so it is not entered as a pinned repository in `new_prior_art.json`.

The literature papers remain mathematical sources even when their results are not formalized. Their statements must be matched to the exact promise, error, and cost convention before entering named hypotheses. A search result or exposition cannot discharge that transport.

## Remaining proof and validation gaps

The most consequential open items are:

- Elaborating the proposed core definitions on the selected toolchain.
- Read-all feasibility and minimum attainment for the public `R` and `Q`.
- Exact classical-tree transport; bit/phase conjugation; finite deferred measurement; all-branch cap preservation; optional-oracle conversion.
- A state-level, hard-budget amplification theorem at arbitrary tolerance.
- The exact small circuit for the promise and output predicate, with transcript and physical-bit accounting.
- The tournament's conditional sampling and potential argument, rather than an unrelated generic multiplicative-weights theorem.
- Adaptive transcript factorization, conditional product structure, Bellman-product decay, and the capped direct-product theorem.
- A formal Forrelation/Fourier-growth lower-bound development; this is the expected long-lived explicit hypothesis.
- Rebuilding all adapted code, recursive axiom audits, Comparator replay, and negative-control rejection.

None of these gaps is hidden in the “reusable” label. That label identifies a concrete source theorem or substrate; the statement ledger separately records the remaining proof obligations.

[hadamard]: https://github.com/leanprover-community/mathlib4/blob/69552756cd8a2d2d48763cf7279fd814d6a1224d/Mathlib/LinearAlgebra/Matrix/HadamardMatrix.lean
[pr]: https://github.com/leanprover-community/mathlib4/pull/38582
[arlib-kernel]: https://github.com/meelgroup/arlib/blob/8d08f89a6d05c5e8368e91659bd6e117fbb74c4e/Arlib/Probability/SequentialKernel.lean
[arlib-dominate]: https://github.com/meelgroup/arlib/blob/8d08f89a6d05c5e8368e91659bd6e117fbb74c4e/Arlib/Probability/SequentialDominate.lean
[arlib-fiber]: https://github.com/meelgroup/arlib/blob/8d08f89a6d05c5e8368e91659bd6e117fbb74c4e/Arlib/Probability/ProductFiber.lean
[debate]: https://github.com/girving/debate/blob/0dab8ad4b58b7a0e82f1738e86135d444462b953/Learn/Indistinguishable.lean
[zulip]: https://leanprover-community.github.io/archive/stream/236449-Program-verification/topic/Outcome.20indistinguishability.html
[forshor]: https://github.com/VerifiedQC/ForShor/blob/a3178a47e1275476c172dd7acd95ec2d43c105c8/FastMultiplication/ShorVerification/Implementation/Shared/Hadamard.lean
[vqc]: https://www.vqc.cs.umd.edu/projects.html
[amp]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Amplitude/Amplification.lean
[geometry]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Amplitude/Geometry.lean
[qude]: https://github.com/QudeLeap/Lean-QuantumAlg/blob/971dc8be8a153a116b6d7cd748f984d545861b00/QuantumAlg/Primitives/AmplitudeAmplification/Endpoint/Results.lean
[qude-manifest]: https://github.com/QudeLeap/Lean-QuantumAlg/blob/971dc8be8a153a116b6d7cd748f984d545861b00/lake-manifest.json
[search]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Search.lean
[adversary]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Adversary.lean
[polynomial]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Polynomial.lean
[midrijanis]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Midrijanis.lean
[manifest]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/lake-manifest.json
[weights]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Probability/AdaptiveWeights.lean
[oracle]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Oracle.lean
[simulation]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Simulation.lean
[complexity]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Complexity.lean
[oai]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/QuantumFactoring/Basic.lean
[oai-amp]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/QuantumFactoring/PhysicalAmplification.lean
[openmaths]: https://openmaths.org/courses/randomized-versus-quantum-query-complexity/
[openmaths-providers]: https://openmaths.org/courses/randomized-versus-quantum-query-complexity/providers.html

