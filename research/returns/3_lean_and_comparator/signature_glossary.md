# Signature glossary and limits

The 118 rows in `formalisation_plan.json` are **unbuilt theorem and definition drafts**. They are detailed statements of the intended obligations, not a compilable Lean package. Names such as `FiniteDistribution`, `Config`, `CoherentQueryAlgorithm`, `AdaptiveListAlgorithm`, `HardDistribution`, and `ExactPivotOrStop` name interfaces still to implement. They are not imported results or hidden assumptions. A `theorem` line without a proof body is a specification, not a theorem that Lean has accepted.

The canonical definition draft is `core_definitions.lean`. It uses coordinate types directly, so there are no free cell queries. For readability the JSON uses the following shorter notation. These conventions must be applied before elaborating the drafts.

| Row shorthand | Canonical interpretation / required bridge |
|---|---|
| `Bits n` | `BitInput (Fin n)` |
| `PartialBool n`, `P.value x` | `PartialBool (Fin n)`, `P x`; the canonical type is an `Option Bool` valued function, not a record with a `value` field |
| `TotalBool.toPartial f` | `totalise f` |
| `PromiseInput P`, `P.onPromise x` | The finite subtype `{x // ∃ b, P x = some b}`, with its uniquely determined Boolean output |
| `m`, `r`, `ell` for the paper family | `mValue t = 4^t`, `addressBits t = 40*t`, `pointerBits t = 2*t`; require `t ≥ 1` whenever dividing by a logarithm or r |
| `Lval k t`, `Gval m L` | Canonical `Lvalue k t`, `Gvalue m L` |
| `P k t` | Exact integer-threshold Forrelation on `ForrelationCoord k t = Fin k × Fin (4^t)`; a flat `Fin (k*4^t)` presentation requires reindexing |
| `forrelationScalar`, `numerator`, `denominator` | Canonical `Phi`, `forrelationNumerator`, `forrelationDenominator`, after proving the matrix-product identity |
| `BansalSinha k` | The fixed-k proposition `∀ᶠ t in atTop, Lvalue k t < R (P k t)`; `∀ k ≥ 2, BansalSinha k` is equivalent to canonical `BansalSinhaLower` |
| `F k t` | A shorthand for `totalise (Fkm k t (chosenCircuit k t))`. Introduce this only after selecting a circuit family whose exact realization and size bound are proved. The canonical core deliberately keeps `C` explicit. |
| Generic `Config`, `cfg.P`, `cfg.circuit`, `addressedFunction cfg` | A generalization of the core construction to any finite partial Boolean function and exact recognizing circuit. `cfg.m=2^cfg.ell` and the pointer bijection are structure data; realization and size are proved specifications, not automatic properties. The Forrelation instance specializes to `Fkm`. |
| `CircuitRecognizes P C` | Core `CircuitRealises C P`, plus gate-evaluation existence/uniqueness when the statement refers to true transcripts |
| JSON `WinsAt cfg y i s` | The paper's semantic true-address condition. The core uses local gate tests and output bits. Prove their equivalence under `CircuitRealises`; never assume that arbitrary circuits recognize P. |
| `D f` for a total f | `D (totalise f)` in the core. Transport exactly to `Cslib.DecisionTree.complexity f`. |
| `R`, `Q` | Canonical randomized and adaptive quantum worst-case bit-query minima at error 1/3. In particular Q in this packet is **not** a silently substituted fixed-length or phase-only measure. |
| `FixedQueryAlgorithm n` | A `FixedProgram (Fin n) w`, existentially packaged over finite workspace w, together with convenient fields for final Born probabilities |
| `AdaptiveQueryAlgorithm n` | An `AdaptiveProgram (Fin n) w` plus normalized input-independent initial state, workspace packaging, and derived output law / query cap |
| `QuantumComputesOn A P ε` | The promise-restricted Born correctness property, with the appropriate adaptive or fixed denotation made explicit. Any use with a fixed A requires a fixed witness; importing an adaptive Q minimum first requires purification. |
| `CoherentQueryAlgorithm`, `CoherentIndexedAlgorithm`, `ReversiblePreparation`, `CoherentComparison` | Fixed reversible bit-oracle programs with a retained workspace, input-independent gates, declared clean input sectors, output labels and proved query counts. “Coherent” is a concrete denotation property, not a free semantic assumption. |
| `FiniteDistribution α`, `Prob μ E`, `Expect μ f` | Finitely supported probability mass functions / real simplices, probability as the sum of masses satisfying E, and expectation as the finite weighted sum. Conditioning is used only on positive-mass events, or with a specified zero-event convention that is multiplied by zero. |
| `State`, `ket`, `tensor`, `OrthogonalProjection` | Finite-dimensional complex Euclidean state spaces, basis vectors and explicit product-index tensor constructions; norm and inner-product conventions must match the chosen model. |
| `euclideanOperatorNorm` | The induced ℓ2 operator norm, not an arbitrary/default entrywise or row-sum matrix norm |
| `FamilyBounds`, `HasCoherentDecoder`, `HasExactSmallCircuit` | Abbreviations for the complete earlier signatures in eq-2 and Lemma 2.1(ii),(iii). They must be reducible public definitions with those exact quantifiers. |
| `HardDistribution P μ L β` | μ is supported on promised inputs and every deterministic decision tree of worst-case depth at most L has μ-average correctness at most β. |
| `NonnegativeAdversary f Γ` | Γ is real symmetric, nonzero and entrywise nonnegative, with Γ[x,y]=0 whenever f(x)=f(y). The coordinate dimension is finite. |
| `NonnegativeUnitTopVector Γ v` | Every coordinate of v is nonnegative, its Euclidean norm is one, and Γv=‖Γ‖₂v. The corresponding Rayleigh identity follows; it is not silently assumed for arbitrary v. |
| `MaximalMonomialSupport g S` | S supports a nonzero coefficient of maximum degree in the unique multilinear polynomial for g. Round lemmas explicitly require g nonconstant. |
| `ExactPivotOrStop K a i ε` | At every positive-probability history avoiding i, K stops with some history-dependent probability f≤ε, and otherwise draws the next pivot from the exact current normalized weight law of a. Previously accumulated candidates are never removed. |

## Five implementation gates

1. **Nonempty feasible sets and attainment.** Prove finite-query witnesses for R, D and Q before any lower bound uses their `Nat` infimum definitions. In Lean, `sInf ∅ : ℕ` is zero. The empty-coordinate quantum case is handled explicitly in the canonical draft.
2. **Both model directions.** Prove bit/controlled-phase conjugacy, canonical/adapted coordinate transports, and fixed/adaptive compilation with its actual overhead. Exact equality of costs and a constant-factor equivalence are different results. Lower-bound constants must absorb whichever overhead the proof establishes.
3. **Physical bits.** Flatten `BitLoc` by a bijection of coordinates. Do not flatten a multi-bit pointer or whole cell into a unit-cost oracle answer. All lengths must remain fixed independently of the input.
4. **Probability semantics.** Prove output masses normalize, weights are nonnegative, and algorithm correctness is quantified only over promised inputs while runtime remains bounded for every input and branch.
5. **Circuit identity.** Construct the exact Forrelation recognizing circuit and size proof before instantiating the claimed family. The existence of some exact truth-table circuit alone does not establish the quantum upper bound.

## Reading `route` and line estimates

`prove` includes new definitions as well as new theorems. `import` means that an inspected source already proves the relevant mathematical inequality; the definition/model bridge remains new proof work. `hypothesis` is used only for the long-lived Bansal–Sinha lower bound. It denotes a visible theorem argument, never an added global axiom or Comparator allowlist entry.

Line ranges are judgment estimates for **incremental local code after dependencies**, not calendar estimates and not measurements of an implementation. They exclude copied third-party files and a new full proof of Bansal–Sinha. Small wrapper rows can share code; library porting can consume effort without proportionally increasing line counts. Conversely a missing semantic lemma can make a nominally short wrapper difficult. The total range therefore gives scale, not a reliable forecast.

The dependency list describes statement/proof prerequisites at ledger-row granularity. Some rows contain both a primitive definition and its derived family statement (notably eq-5, eq-17 and def-F). The primitive must be defined before its theorem, even when the row's final declaration is scheduled later. The `depends_on` graph is acyclic and includes only the 118 original IDs; interfaces beyond the ledger are listed separately under `blocking_interfaces`.

## Main theorem coverage versus every-row coverage

The imported quartic upper bound permits the main theorem route to bypass parts of the appendix proof. It does not prove every appendix intermediate statement. If “every statement of the paper” remains the goal, the generic nonnegative spectral adversary theorem, Perron-style eigenvector lemma and full signed-cube multiplicity claims still have their own rows and pass criteria. Existing declarations proving a weaker conclusion or using a different proof do not automatically cover those rows.
