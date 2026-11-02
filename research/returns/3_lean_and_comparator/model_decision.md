# Model decision

**Recommendation:** keep the public statement layer Mathlib-only and give it the paper's literal bit-query semantics. Use **complexitylib at `62ca5c21461b2482e8bd12b7cb9b4937d887a33a`** as the main proof engine, through explicit model-transport theorems. Port the bounded amplification development from **troyjlee/quantum-query-complexity at `517ba85eb211232771429804d8583e3f52b9d541`** as a separately licensed implementation. Use QudeLeap's Walsh and amplification mathematics selectively. The inspected OpenAI factoring framework is a design reference, not the definition of query complexity.

This is a source-based architectural recommendation, **not a completed formal verification**. The inspected declarations and full pins are recorded in `reuse_checked.json` and `new_prior_art.json`. No Lean executable was available in this review environment. The companion `core_definitions.lean` is explicitly **UNBUILT**. None of the bridges below has been checked here.

## 1. Why this model is the right public contract

The paper counts worst-case individual input-bit queries; all other finite computation is free. Its upper-bound routines use measurements, classical randomness, repeated attempts, and a hard query cap, including when a subroutine receives an input outside its promise. Its total function includes stored binary pointer fields and circuit transcripts. Those features should appear directly in the public specification, rather than be reconstructed from a gate-cost or expected-cost model. See the packet's `paper/extracted.md`, Sections 2–4 and the definitions of the standard query model, capped search, and `F_{k,m}`.

The proposed public model has these properties:

- A total Boolean function is `(ι → Bool) → Bool`. A partial Boolean function is `(ι → Bool) → Option Bool`; `none` means outside the promise.
- A deterministic program is an ordinary binary decision tree. Its cost is maximum syntactic depth, with repeated probes counted.
- A randomized program is a finitely supported probability distribution over those trees. Its cost is the largest tree depth in its support. This is a worst-case cap, not an expected number of queries.
- A quantum program has an arbitrary but finite workspace, input-independent isometries, literal XOR input queries, finite projective measurements, and classical branches. Its cap is a syntactic maximum over every branch.
- Success is required only on promised inputs. The cost remains bounded on every input.
- The minimum definitions of `D`, `R`, and `Q` require explicit read-all existence and attainment theorems before being used. Natural-number `sInf` assigns zero to the empty set; a formula containing `sInf` alone is not a valid complexity lower-bound API.
- The query register is unnecessary for constant functions. The `ConstantOnPromise` alternative handles an empty coordinate type without pretending that a zero-dimensional Hilbert space has a unit vector.

These choices are implemented as draft signatures in `core_definitions.lean`; their equivalence to the paper's informal computational model remains a mathematical proof obligation. In particular, finite general measurements and dynamic allocation need finite-ancilla realization. Arbitrarily large finite workspace is allowed, while an infinite-dimensional workspace or an unbounded runtime is not introduced silently.

## 2. What the four inspected libraries actually offer

| Source | Actual model | Best use here | Main gap |
|---|---|---|---|
| complexitylib `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` | Arbitrary finite workspace; controlled phase oracle; fixed-length unitary evolution; final basis event. Classical distributions use `StdSimplex`. | Existing deterministic/randomized infrastructure, minimax, Fourier algebra, spectral sensitivity, and quartic simulation. | No scalar `Q` minimization definition in the inspected quantum files; no proved bridge here from the adaptive public model. |
| Troy Lee `517ba85eb211232771429804d8583e3f52b9d541` | Finite query algorithms over a promise reader `read : X → ι → σ`; native oracle swaps a blank answer with the read symbol; optional-index/optional-answer basis. | Bounded amplification, exact conditional output law, query-budget arithmetic, and native/XOR simulation. | Older toolchain; oracle and basis differ; full-state successful-output wrapper still needed. |
| QudeLeap `971dc8be8a153a116b6d7cd748f984d545861b00` | A detailed execution framework with environment, output-state and restoration contracts, native event counts, space, and time. | Walsh-Hadamard algebra, independently inspectable state-level amplification endpoint, explicit count formulas. | Much more infrastructure than this query-complexity theorem needs; version port and all environment assumptions must remain visible. |
| OpenAI math `4eaee87548250b2682affda7d05d947c05554bae` | Concrete finite-gate circuits on input wires, exact matrix semantics, uniformity and polynomial resource conditions. | Circuit bookkeeping and proof-organization examples. | This is a factoring/circuit model, not a black-box bit-query model; its physical amplification theorem is a special quarter-success case. |

Primary source locations: complexitylib [Search.lean][cs-search], [Randomized.lean][cs-randomized], and [Adversary.lean][cs-adversary]; Troy [Algorithm.lean][troy-algorithm], [Oracle.lean][troy-oracle], [Complexity.lean][troy-complexity], and [Simulation.lean][troy-simulation]; QudeLeap [Solves.lean][qude-solves] and [amplification Results.lean][qude-amplitude]; OpenAI [Basic.lean][oai-basic] and [PhysicalAmplification.lean][oai-amplitude].

### Correcting an important intake error

complexitylib does **not** restrict the workspace to a trivial type. Its actual declarations include:

```lean
abbrev Cslib.Quantum.State (N : ℕ) (W : Type*) :=
  EuclideanSpace ℂ (Fin N × Bool × W)

noncomputable def Cslib.Quantum.phaseOracle (x : Fin N → Bool) :
  State N W →ₗ[ℂ] State N W

noncomputable def Cslib.Quantum.run
    (U : ℕ → State N W →ₗᵢ[ℂ] State N W)
    (ψ₀ : State N W) (x : Fin N → Bool) : ℕ → State N W
```

The phase on basis coordinate `(i,b,w)` is `(-1)^(b && x i)`. The answer-control bit is essential: this is a controlled phase oracle, not the phase-only oracle that can identify complementary inputs up to global phase. The source assumes a finite workspace and includes norm-preservation lemmas. See [Search.lean][cs-search].

Its existing theorem is a statement about **every specified algorithm**, rather than an already defined `Q(f)` minimum:

```lean
Cslib.Quantum.complexity_le_mul_pow_four
  (U : ℕ → State N W →ₗᵢ[ℂ] State N W)
  (hψ₀ : ‖ψ₀‖ = 1) (T : ℕ)
  (S : Finset (Fin N × Bool × W))
  (h : ∀ x,
    |measureProb (run U ψ₀ x T) S - bitVal ℝ (f x)| ≤ 1 / 3) :
  Cslib.DecisionTree.complexity f ≤ 20736 * T ^ 4
```

Implicit parameters are omitted in this display; the exact source signature is in `reuse_checked.json`. The source obtains this through its spectral-sensitivity, polynomial, block-sensitivity, and Midrijanis developments. Thus it is close to the paper's universal quartic upper bound, but using it for our `Q` still requires the model bridge and minimum attainment. [Adversary.lean][cs-adversary], [Polynomial.lean][cs-polynomial], [Midrijanis.lean][cs-midrijanis].

## 3. Required model bridges, in the order to prove them

### A. Public classical trees and complexitylib

Construct an evaluation- and depth-preserving equivalence between the public `QueryTree ι` and `Cslib.DecisionTree ι Bool`. Push finitely supported distributions along it, prove normalization and support-depth preservation, and identify success with one minus error. Then prove equality of the total-function `D` and `R` definitions. Use a subtype of the actual promise domain when invoking APIs parameterized by abstract input types.

The concrete reuse is `Cslib.RandomizedDecisionTree`, `.depth`, `.errorProb`, `.Computes`, `Cslib.QueryComplexity.randomizedComplexity`, and `exists_computes_depth_eq_randomizedComplexity`. The latter explicitly supplies the attainment needed for the library's own minimum. A partial-function API is additional work; it should not be assumed from a total-function theorem. [DecisionTree/Basic.lean][cs-tree], [Randomized.lean][cs-randomized].

### B. Literal XOR and controlled phase

For each input and finite workspace prove the exact operator identity

```text
H_answer ∘ controlledPhaseOracle(x) ∘ H_answer = literalBitOracle(x).
```

The one-qubit Hadamard is input-independent, so this translation preserves the number of queries exactly. First establish the equality on basis vectors, then on arbitrary states; derive probability preservation and the translation of a fixed-length program. Also prove the reverse conjugation identity. This specific equivalence is an algebraic fact about the two displayed oracle definitions; it is not a blanket statement that every oracle convention costs the same.

Any additional idle-index or blank-answer sectors used by Troy require a separate embedding or controlled simulation. The existing factor-two theorems in Troy apply to **its native oracle and its optional XOR oracle**, not automatically to the entire route into our model. Record the final proven constant rather than inventing one. [Search.lean][cs-search], [XorOracle.lean][troy-xor], [Simulation.lean][troy-simulation].

### C. Adaptive programs and fixed-length coherent programs

Both directions are necessary:

1. Translate fixed phase programs and the imported amplification algorithms into the public adaptive literal-bit model. This establishes the new algorithmic upper bound for the intended `Q`.
2. Translate **every** public bounded adaptive quantum program into a fixed-length program, with preserved output probabilities and at most `c_model * T` oracle calls for an explicitly proved absolute constant. This is the direction needed to turn complexitylib's per-algorithm quartic theorem into the universal upper bound for the public `Q`.

The second direction needs coherent records of measurement outcomes, controlled branch operations, sufficient finite ancillas, and padding of halted branches. Prove that all these operations are input-independent. Controlled oracle simulation and padding must be included in the query accounting. Classical randomization can be purified into an ancilla. Binary projectors can represent finite projective measurements through iteration; arbitrary finite instruments require a finite dilation result.

An absolute multiplicative overhead preserves the paper's exponents and changes the quartic coefficient to at most `20736 * c_model^4`. Exact equality of the two minima should only be stated if the stronger exact-cost bridge is proved. Do not replace the public adaptive definition with a narrower fixed model and then infer the universal theorem without this direction.

### D. Native/optional XOR simulation and finite minima

Troy already contains `qQueryOn_le_two_mul_xorQQueryOn` and `xorQQueryOn_le_two_mul_qQueryOn`. Their hypotheses matter: feasible minima must exist, and the answer must be determined by the observed oracle. `xorQueryCounts_nonempty` requires observational determinacy `read x = read y → f x = f y` and nonnegative error. [Simulation.lean][troy-simulation].

For the public `PartialBool` interface, observation determines the promised answer by construction; read-all algorithms give the missing existence proof. Prove these once, alongside `RLe`/`QLe` monotonicity, to keep all later lower-bound arguments from accidentally exploiting `sInf ∅ = 0`.

## 4. Amplification: reuse the strong part without weakening the paper

Troy's opened source provides:

- `QuantumQueryComplexity.AmpSetup.amplified_cond_law`: conditional output probabilities equal the original good-output weights divided by original success probability.
- `two_thirds_le_returnProb`: a fixed-budget success guarantee under the source hypotheses.
- `amplified_prob_none_of_succProb_eq_zero`: the zero-success case.
- `AmpSetup.amplifiedBudget_le_real`: a bound by `16 * (prep.len + mark.len) / sqrt p₀`.
- `QuantumQueryComplexity.GroverSplit.grover_pow_mulVec`: the exact state decomposition in the good/bad invariant plane.

See [Amplification.lean][troy-amplitude] and [Geometry.lean][troy-geometry].

This is particularly useful for the tournament, which needs the conditional law of the sampled candidate. However, **equality of measured output distributions does not prove equality of the entire successful quantum state**. The paper's Lemma 3.1 requests the latter. Complete a state-level wrapper using `grover_pow_mulVec`; explicitly account for ancillary registers, conditioning, global phase, fresh attempts, and discarded failure information. The successful reduced state must match the required good state, or the theorem must retain the stronger appropriate state contract. A distribution-only theorem is insufficient for that row.

Repeat a bounded base routine a predetermined number of times to reach arbitrary failure tolerance `η`. Prove the geometric failure bound, exact conditional law, state condition, zero-success behavior, and a cap on every branch. Do not infer an off-promise hard cap from a success-probability theorem. QudeLeap's endpoint offers an independent comparison: `algorithm_solves` and all-path formulas `preparationCount = k+1`, `inversePreparationCount = k`, `goodReflectionCount = k`. Its general `Solves` contract additionally carries validity, initialization, and supported-path assumptions; preserve them when comparing. [Solves.lean][qude-solves], [Results.lean][qude-amplitude].

The inspected OpenAI `physical_quarter_amplification` theorem handles one exact round from success mass one quarter. It cannot substitute for a uniform unknown-success bounded amplifier. [PhysicalAmplification.lean][oai-amplitude].

## 5. Forrelation and the total construction

The core draft makes these specification choices explicit:

- Restrict to `m = 4^t` so the normalized Walsh coefficient can be specified through an exact integer numerator and integer denominator. Then `log₂ m = 2t` and the paper's `r = 20 log₂ m` becomes `40t`.
- Define the `1` region by **positive** Forrelation at least `2^(-5k)`, the `0` region by absolute value at most `2^(-5k-1)`, and leave the other region unpromised. Large negative Forrelation is not automatically accepting.
- Treat the integer path sum as a specification. A separate theorem constructs the efficient fan-in-two circuit deciding the promise and value; the path-sum definition itself does not establish the circuit-size claim.
- Parameterize `Fkm` by that concrete circuit and prove `CircuitRealises`. A transcript stores gate values, not a duplicate input at unit access cost.
- Encode every pointer as its actual `2t` bits and every cell field as a physical input coordinate. Prove pointer decoding is a bijection and coordinate counts agree with the paper. A single query that reveals a `Fin m` pointer would change the model.
- Prove transcript uniqueness from acyclic evaluation, uniqueness of a winning column, and the stated local verifier cost before using the quantum verification algorithm.

The exact paper-to-core agreement, parameter restriction, and asymptotic reindexing are release gates, not facts already established by a plausible definition. The separation remains **exponent `4 - 2/k` for each fixed `k ≥ 2`**. The universal exponent infimum is a separate consequence, not a fourth-power family.

No source-verified Lean theorem for the Bansal–Sinha Forrelation lower bound or this paper's capped direct-product theorem was located in the bounded search. The lower bound should enter first as an explicit argument about the exact public `P` and `R`; it must not enter Comparator's permitted-axiom list. The construction's own upper bound, drift, transcript factorization, and direct-product proof remain distinct tasks.

## 6. Version closure and licences

Use one build closure:

```text
Lean      leanprover/lean4:v4.36.0-rc2
complexitylib 62ca5c21461b2482e8bd12b7cb9b4937d887a33a
mathlib       69552756cd8a2d2d48763cf7279fd814d6a1224d
cslib         254e30e6d4299c51323aaeaf5f51a4763b375d4a
```

The Mathlib and cslib pins above come from complexitylib's actual [lake-manifest.json][cs-manifest]. The intake's independently sampled cslib pin is not this dependency. Do not mix `.olean` files from the four libraries' different Lean/Mathlib versions.

Troy targets Lean `v4.35.0-rc2`, QudeLeap `v4.33.1`, and the inspected OpenAI Lean subtree `v4.34.1`. Port the smallest source dependency closure into a licensed vendor namespace or a separately pinned compatible package; then compile and replay its declarations on the target. Source similarity is not compatibility evidence. Exact toolchain and manifest links are attached to each prior-art row.

The complete inspected code licences are Apache-2.0: [complexitylib][cs-license], [Troy][troy-license], [QudeLeap][qude-license], [OpenAI Lean subtree][oai-license], and [Mathlib][mathlib-license]. Preserve existing copyright/licence notices, supply the licence and any applicable notices when distributing adapted source, and document changed files. The optional new code sources in `new_prior_art.json` also have inspected Apache-2.0 licences. This source-code finding does not determine rights in paper prose or figures.

Mathlib's [HadamardMatrix.lean][mathlib-hadamard] is already present at the chosen target pin. `Matrix.IsHadamard`, `IsHadamard.kronecker`, and `IsHadamard.of_mul_conjTranspose` can support a Walsh construction without an upgrade to master. The associated [PR 38582][mathlib-pr] is a useful discovery record; availability of the exact file at the pinned commit is the operative evidence. It supplies matrix algebra, not the Fourier-growth lower bound.

## 7. What would change this recommendation

This recommendation should change if either of two short prototypes exposes a substantive obstacle:

1. **Semantic bridge prototype:** compile the public definitions; prove read-all attainment; identify the classical trees; prove the bit/controlled-phase basis identity; translate a one-bit identity algorithm and a finite measured branch with the exact distribution and declared cap. Then extend to the general adaptive-to-fixed theorem. If the chosen public syntax cannot express the paper's finite algorithms, revise the syntax before freezing challenge statements.
2. **Amplification port prototype:** compile the smallest Troy dependency closure on the target and instantiate a two-outcome example with nontrivial success probability. Check the conditional distribution, full-state condition, zero-success case, and hard cap. If porting the closure costs more than reproving the invariant-plane lemma in complexitylib, retain Troy as a design reference and reprove that small mathematical core.

Neither prototype was executed here. A successful source-level inspection does not settle the cost of porting or the adequacy of a Comparator challenge.

After those prototypes, freeze public definitions and the challenge module graph. Keep model bridges in the solution dependency graph and include them in axiom audits. A conditional theorem may have a named lower-bound argument; a theorem advertised as unconditional may not acquire the same claim through an ambient axiom or an opaque imported assumption.

[cs-search]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Search.lean
[cs-randomized]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Randomized.lean
[cs-tree]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/DecisionTree/Basic.lean
[cs-adversary]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Adversary.lean
[cs-polynomial]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Quantum/Polynomial.lean
[cs-midrijanis]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/Complexity/Computability/QueryComplexity/Midrijanis.lean
[cs-manifest]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/lake-manifest.json
[cs-license]: https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/LICENSE
[troy-algorithm]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Algorithm.lean
[troy-oracle]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Oracle.lean
[troy-complexity]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Complexity.lean
[troy-simulation]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Simulation.lean
[troy-xor]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/XorOracle.lean
[troy-amplitude]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Amplitude/Amplification.lean
[troy-geometry]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/QuantumQueryComplexity/Quantum/Amplitude/Geometry.lean
[troy-license]: https://github.com/troyjlee/quantum-query-complexity/blob/517ba85eb211232771429804d8583e3f52b9d541/LICENSE
[qude-solves]: https://github.com/QudeLeap/Lean-QuantumAlg/blob/971dc8be8a153a116b6d7cd748f984d545861b00/QuantumAlg/Core/Algorithm/Solves.lean
[qude-amplitude]: https://github.com/QudeLeap/Lean-QuantumAlg/blob/971dc8be8a153a116b6d7cd748f984d545861b00/QuantumAlg/Primitives/AmplitudeAmplification/Endpoint/Results.lean
[qude-license]: https://github.com/QudeLeap/Lean-QuantumAlg/blob/971dc8be8a153a116b6d7cd748f984d545861b00/LICENSE
[oai-basic]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/QuantumFactoring/Basic.lean
[oai-amplitude]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/QuantumFactoring/PhysicalAmplification.lean
[oai-license]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/LICENSE
[mathlib-hadamard]: https://github.com/leanprover-community/mathlib4/blob/69552756cd8a2d2d48763cf7279fd814d6a1224d/Mathlib/LinearAlgebra/Matrix/HadamardMatrix.lean
[mathlib-pr]: https://github.com/leanprover-community/mathlib4/pull/38582
[mathlib-license]: https://github.com/leanprover-community/mathlib4/blob/69552756cd8a2d2d48763cf7279fd814d6a1224d/LICENSE

