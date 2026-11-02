# Statement fidelity review

Reviewer: `ai:truth-auditor`, 2 November 2026, two passes. The first pass read `lean/QuarticQuery/Statement.lean` and the ties for everything except `LowerBound/Planted/` and `Upper/`. The second pass read `LowerBound/Planted/*.lean`, `Upper/*.lean` and `Results/Conditional.lean` in full against Sections 3 and 4 of the preprint, at commit `efc70f3`. Lean was not run in either pass, so nothing here says that a file compiles. Relations are in `corpus/ties.json`.

## Result

`alphaTot_eq_four_of_bansalSinha (h : BansalSinhaLower) : alphaTot = 4` says what it appears to say. Its only hypothesis is the Bansal-Sinha randomized lower bound for this `P` in this query model, which is the one input the preprint imports (`lean/QuarticQuery/Results/Conditional.lean:47`). `Q_Fkm_le` is a real bound on an `AdaptiveProgram` on the bit oracle, with a syntactic cap, for the exact function `totalise (Fkm …)`, on all inputs (`Upper/Bound.lean:251`). `Gvalue_lt_R_addressedF` is the non-asymptotic Proposition 4.2 (`LowerBound/Planted/Main.lean:190`). I found no vacuity: `BansalSinhaLower` is not false for a degenerate reason, the promise has both values, and the bounds do not collide with `D ≤ 20736 Q⁴`.

Nothing in the new files changes what a theorem means in a way that affects the headline. Three readings need care: `family_bounds` is unconditional only in its circuit and `Q` halves (finding 2); Proposition 3.2 has no list in its statement (finding 3); and Lemma 3.1's exact tie is off the headline's path (finding 4).

The sharper constant `2G/m²` in equation (19) is correct and is a real improvement. It is not double counting, and `2` cannot be lowered (finding 5).

Steps proved by a route other than the preprint's: equation (19), Theorem A.1, and the composition of quantum stages (finding 6).

Tie counts, computed from `corpus/ties.json`: 308 ties on 68 rows. Relations: 22 exact, 10 stronger, 274 partial, 2 weaker. Routes: 144 same, 17 alternative, 147 none. Exact or stronger ties exist on 24 rows. 50 ties carry hypotheses. The second pass added 87 ties and edited 8. Of 314 tagged pairs in the Lean sources, 308 are reviewed; the other 6 name ids with no row (finding 11). 53 of the 121 rows have no tie.

## Findings, most severe first

### 1. The headline is conditional on Bansal-Sinha alone (resolved)

- Where: `Results/Conditional.lean:38`, `:47`; `Statement.lean:319`.
- Paper: Theorem 1.1, with Lemma 2.1(i) as the only external input.
- First pass: `alphaTot_eq_four` took all of equation (2) as a hypothesis. That theorem is unchanged, and `familyBounds_of_bansalSinha` now discharges the hypothesis, so `FamilyBounds` is no longer an assumption of the headline.
- What remains: the result is conditional, and the hypothesis is a binder, so an axiom report cannot show it. Read the type. `lean/QuarticCorpus/Separation/Solution.lean` says this too.
- `thm-1.1` stays `partial` under the strict rule, because the row also asserts `R = O((1+Q)^4)` and equation (2), which are separate declarations. A conjunction theorem would lift it (finding 10).
- `cubic_bound_fails_of_bansalSinha` is `exact`. Its proof uses the hypothesis at `k = 3` only, though the binder quantifies over all `k ≥ 2`.

### 2. `family_bounds` is equation (2) in two halves of different status

- Where: `Results/Conditional.lean:25`.
- What it says: `S`, `A`, `b` are chosen before `t`. At each `t ≥ 1` one circuit realises `P`, has size at most `S m (2t)²`, and has `Q ≤ A 2^t (2t)^b`, unconditionally, with `b = 6` for every `k`. The lower half is `8 ≤ t → L < R(P) → G < R(F)`, conditional at that `t`, in the floor form.
- It is not vacuous. The circuit and `Q` halves hold without the hypothesis, and the lower half is an implication whose premise is plausibly true (see "Vacuity" below).
- Reading it as an unconditional equation (2) would be wrong. So would reading `familyBounds_of_bansalSinha` as a statement about the size-bounded circuit: `FamilyBoundsAt` still hides the circuit behind an existential (`Results/Exponent.lean:170`), though the witness is `forrCircuit`. Neither matters for `alphaTot`, whose statement mentions no circuit.
- Both ties on `eq-2` are `partial`. First-pass finding 4 is closed by `family_bounds` for the size, and left open only as this gap between two statements.

### 3. Proposition 3.2 has no list in its statement

- Where: `Upper/Tournament.lean:367`.
- Paper: Proposition 3.2 returns a list of at most `T` candidates containing `i*` with probability at least `1 - 2m/2^T - Tε`.
- What Lean does: `tournament_runs` consumes the list inside the program through a verifier `v`, and bounds acceptance by `1 - 2m/2^T - Tε - ε` when `v s ≥ 1 - ε`. Taking `v` to be the indicator of `s` recovers list membership with one extra `ε` against the row.
- Consequence: the tie is `partial`, and the statement is what Section 3.3 needs. The error budget of `claim-error` is the same, `total_error_lt` at `Tournament/Ideal.lean:327`.
- `tval_lower` (`Upper/Tournament.lean:239`) is the paper's coupling by induction over histories, with failure charged at the history where it occurs, so history-dependent failure is handled as the paper requires.

### 4. Lemma 3.1's exact tie is not on the headline's path

- Where: `Amplification/Bounded.lean`, `Upper/Amplify.lean:247`, `:346`.
- `bounded_amplification` remains the `exact` tie for `lem-3.1`. No file outside `Amplification/` uses it, or `Proc`, or `IndexRegister`.
- `Q_Fkm_le` uses `Samples.amplify`, which states Lemma 3.1 on the bit oracle for samplers. It gives a label law, exact on success, with the state `|g⟩` absent. It is for circuits, so "black-box in `A`" is not stated either, though `IsCirc` enforces input-independence. The tie is `partial`.
- This is sufficient: the tournament measures the index at once and verification measures the failing test, so nothing uses `|g⟩`.
- First-pass finding 6 is closed in a way that pass did not expect. `Proc` is never compiled, so the concern about `restart` and discarded registers no longer arises.

### 5. The constant `2G/m²` in equation (19) is correct

- Where: `LowerBound/Planted/ZeroSearch.lean:37`, `:167`, `:192`, `:210`, `:226`.
- Paper: `E Z ≤ 4G/m`, split into early discoveries and columns with at least `m/2` queries.
- The proof: `zero_search_sum` says `|U| · #{j ∈ U : found} ≤ 2 Σ_{j∈U} (queries to the column)`, for any set `U` of worlds, by induction on the tree. I checked the only substantive case by hand. At a query to `p ∈ U`, put `n = |U \ {p}|`, let `N` be the finds in the subtree on `U \ {p}`, and let `S` be its column queries. The worlds other than `p` continue to one subtree, so the total charge is at least `1 + S + n`, and the induction gives `nN ≤ 2S`. Then `(n+1)(1+N) = nN + n + N + 1 ≤ 2S + 2n + 1 ≤ 2(1 + S + n)`, using `N ≤ n`. Nothing is charged twice. A query not in the column sends every world to one subtree (`hout`), and a query in the column at `p ∉ U` only adds cost.
- Averaging is sound. `avg_resample` redraws one coordinate of `J`, and `sum_xQueries_le` adds columns inside one run, where each query belongs to one column.
- Check run: 198,361 random adaptive trees with worlds and extra coordinates, 0 violations, largest ratio 0.8 (`M ≤ 7`). Script `/private/tmp/claude-501/-Users-willcook-src-ai-workflow/23667333-0d0a-458f-8117-1ccaac600bb5/scratchpad/checks.py`, exit 0; not part of this repository.
- The constant is tight. Scanning a column until the zero appears finds it in every world at mean cost `(M+1)/2`, a ratio of `M/(M+1)` in `zero_search_sum`. So `E Z = 2G/(m+1)` is attained, up to rounding `G` to whole columns.
- The improvement does not reach any conclusion. `addressedF_not_RLe` keeps `4G/m²` in its hypothesis (`Main.lean:113`) and weakens to it at `:154`, `G` is unchanged, and `G/(mL)` dominates (23): at `k = 2`, `t = 8` the value is 0.0099951 with `4` and 0.0099948 with `2`.

### 6. Routes a reader should be told about

- **Equation (19)**: the argument above replaces the paper's conditional early/late bookkeeping. `def-Z`, `claim-uniform-zero` and `claim-EZ` have no tie, and cannot, since `Z` and the conditional uniformity never appear. The tie to `eq-19` is `stronger`, route `alternative`.
- **Theorem A.1**: proved through complexitylib, with constant `20736`, as recorded in `Appendix/TheoremA1.lean`. Lemmas A.2 to A.5 and their supporting rows have no tie in the paper's form.
- **Composition**: `Samples.bind` replaces reversible bookkeeping by one lemma, that a second stage under control of a label is block diagonal. That is the paper's sentence on orthogonal address outcomes. `Samples.runs` measures every label and swaps back to the start state, in place of fresh registers. Only `Samples.runs` is marked `alternative`.
- **Independence**: `avg_resample` replaces conditional probability throughout Section 4. The simulator argument is otherwise the paper's.
- Smaller differences: each read costs two bit queries, so a phase query costs two against the paper's one (`compile_read`, `Upper/Compile.lean:151`). Threshold on the retained count replaces repetition and majority. Every stage is charged for `T` pivots. `(2/3)^(40t) ≤ m^-10` replaces the paper's exponent. All are constants or slack.

The `route` field records the declaration's own proof step, so `thm-1.1` and `prop-4.2` show `same`, and their notes name the steps below them.

### 7. The simulator bounds a joint event

- Where: `LowerBound/Planted/Simulator.lean:131`, `:172`.
- Confirmed: `reachedCell` is the indicator of "nonheavy and reached the true cell". `avg_reachedCell_le` proves pointwise in `U` that this indicator is at most the sum over `t < G` of the indicator that the capped simulator `sims t` guessed correctly. `sims` is built from `J`, `A` and `T`, and is independent of `U`, because `dummy_update_of_aTarget_none` shows the base answers do not read the redrawn strings. The distribution of `U` is `prodW μ`, and nothing conditions it on nonheavy.
- The equation (21) bound per time `t` is not stated. The union is bounded directly. The heavy term joins in `tree_gap_le`. So `eq-21` and `eq-22` have only `partial` ties, with no gap in the argument.
- `tree_gap_le` is one-sided, planted minus dummy. That is all the proof uses, and `eq-23`'s absolute value is not stated.

### 8. The builder faults of the first pass (fixed)

First-pass findings 2 and 3 are fixed in `tools/build_corpus.py`: ids keep their dots and `end` of a section no longer pops a namespace. All 221 first-pass ties match a declaration the builder finds, so no renaming was needed. `tests/test_build_corpus.py` has regression cases and passes: 6 tests, exit 0.

### 9. Comparator receipts do not reach the evidence fields

- Where: `corpus/receipts/`, `tools/build_corpus.py` in `statement_records`.
- What is wrong: two receipts appeared while I worked, `comparator-Construction.json` and `comparator-Foundations.json`, neither mine, and both passed and unsandboxed. Their declarations are `QuarticQuery.Checked.*`, while ties name `QuarticQuery.*`. `compared` matches by exact string, and `best` also requires `built`, which needs a `lean_build` receipt. So `corpus/coverage.json` reports `comparator: not_run` for all 121 rows.
- Fix: map the `Checked` names to the ties, and add a build receipt. No `Separation` receipt existed when I last looked.

### 10. Strict relations that one small theorem would lift

Under the strict rule, these rows have no single `exact` tie although two declarations together cover them:

- `thm-1.1`: `alphaTot_eq_four_of_bansalSinha`, `universalPower_four`, `familyBounds_of_bansalSinha`.
- `eq-2`: `family_bounds` with `rpow_le_of_Gvalue_lt`, keeping the circuit and its size in the conclusion.
- `lem-2.1.ii`: `P_runs` with `decode_samples` and `repetitions_le`.
- `claim-Y-values`: `addressedF_dummy` with `addressedF_planted`.
- `eq-22`: `avg_heavy_le` with `avg_reachedCell_le`, for a statement about reaching the cell at all.
- From the first pass, still open: `eq-3`, `eq-4`, `claim-integer-tests`, `claim-grover-state`, `eq-9`, `claim-numeric`, `def-query-oracle`.

### 11. Tags: open items

Open from the first pass: `Ledger: def-P` and `Ledger: claim-butterfly` still match no row (6 declarations). The builder now lists them in `ledger_ids_without_a_row` but does not fail. The candidate tags of the first pass are still unused, though the builder now accepts a reviewed tie with no doc comment:

| Row | Declaration | Location |
| --- | --- | --- |
| `eq-1` | `alphaTot`, with `UniversalPower` | `Statement.lean:323`, `:329` |
| `eq-5` | `Lvalue` | `Statement.lean:309` |
| `eq-17` | `Gvalue` | `Statement.lean:314` |
| `eq-8` | fourth conjunct of `WinsAt` | `Statement.lean:282` |
| `eq-11` | `Tournament.Dominant` | `Tournament/Ideal.lean:220` |
| `lem-2.1.i` | `BansalSinhaLower`, as the external hypothesis | `Statement.lean:319` |
| `def-win-at-address` | `winsAt_iff_outputs` | `Construction/LocalTests.lean:287` |
| `def-winner` | `WinsAt` with `winsAt_iff_paperWinsAt` | `Statement.lean:277` |
| `eq-13` | `expected_weight_eq`, `expected_weight_le_half` | `Tournament/Drift.lean:55`, `:71` |
| `cor-unique-winner` | `winsAt_column_unique` | `Construction/Winner.lean:42` |
| `cor-local-dichotomy` | `localTests_iff_eq_of_winsAt`, `exists_failing_localTest` | `Construction/LocalTests.lean:262`, `:268` |

New candidates from the second pass, untagged at present:

| Row | Declaration | Location |
| --- | --- | --- |
| `eq-10` | `cmpProb_isComparison` | `Upper/Columns.lean:195` |
| `claim-success-prob` | `stageLaw_some`, `sum_stageLaw_some` | `Upper/Tournament.lean:43`, `:51` |
| `claim-error` | `total_error_lt` | `Tournament/Ideal.lean:327` |
| `claim-verify` | `search_runs` with the two cases in `Fkm_QLe` | `Upper/Verify.lean:108`, `:138` |
| `claim-decode-cost` | `addrLaw_good`, `addrCost` | `Upper/Columns.lean:65`, `:50` |
| `claim-comparison-state` | `core_samples`, `firstWins` | `Upper/Columns.lean:143`, `:118` |
| `def-comparison` | `coreProb`, `firstWins` | `Upper/Columns.lean:121`, `:118` |
| `def-verify` | `verifyProb` | `Upper/Verify.lean:127` |
| `def-heavy` | `aQueries` | `LowerBound/Planted/Heavy.lean:22` |
| `def-simulator` | `simTree` | `LowerBound/Planted/Simulator.lean:32` |

Tags in the wrong place, from the first pass: `lem-A.2` on `FixedSim.build` and `exists_fixedSequence`, and most `def-query-oracle` tags on the Hadamard gadget in `Bridge/Oracle.lean`. In the second pass: `search_runs` and `verifyProb` sit under `lem-2.2.ii` but belong to `claim-verify`, and `Samples.pi` sits under `lem-2.1.ii` but belongs to `claim-decode-cost`.

### 12. One tie is weaker by design

`twoThirds_pow_le` (`Results/Exponent.lean:429`) gives `m^-10`, while the paper's exponent is `20 log_2(3/2) = 11.70`. `m^-10` suffices for `discrepancy_le`, so this needs no fix. The tie is `weaker`.

## Vacuity and model checks

**`BansalSinhaLower` as encoded.** It says that for each `k ≥ 2`, from some `t₀(k)`, no randomized tree mixture of depth `L = ⌊m^(1-1/k)/(log₂ m)²⌋` computes `P k t` with error `1/3`.

- The promise is not empty and has both values, so `R(P)` is not `0` for a degenerate reason. 0-inputs: over uniform `z`, distinct paths give orthogonal characters, so `E[N²] = m^k` and `E[Φ²] = 1/m`, and Chebyshev gives `|Φ| ≤ δ/2` for some `z` once `m > 2^(10k+2)`, and for almost all `z` as `m` grows. 1-inputs: `Φ = 1` occurs for all `t`. For odd `k` take all zeros. For even `k` take the bent function `x·y` on the first two layers and zeros on the rest. I computed `Φ = 1` for `k = 2` to `6` at `t = 1, 2, 3`, and the adjudication records a census of 104 true and 48 false inputs at `k = 2`, `t = 1`.
- `L` is well below `km`, the trivial upper bound on `R(P)`. The imported bound in `corpus/statements.json` is `Ω(k^-29 (N/log(kN))^(1-1/k))`, whose ratio to `L` grows like `t^(1+1/k)`, so a `t₀(k)` exists for each `k`, and the quantifier order matches. As I recall, classical simulation of `⌈k/2⌉` quantum queries gives `Õ(m^(1-1/k))`, so `L` sits a logarithmic factor below the expected value; I did not check that source.
- `P_QLe` gives `Q(P) ≤ 2^(10k+6) k`, independent of `t`, for this `P`. That does not contradict the hypothesis: `D ≤ 20736 Q⁴` is proved only for total functions.

**`family_bounds` and the program.** The chain compiles to a real `AdaptiveProgram`:

- `IsCirc` has a gate constructor with no access to `x`, and `x` enters only through `ReadSpec.op` (`Upper/Circuit.lean:342`).
- `compile_read` proves that a read is two `.query` steps around fixed isometries, with `P` chosen before `x` (`Upper/Compile.lean:151`).
- `Samples.runs` compiles a sampler, and `Runs` has `∃ P` before `∀ x b` (`:322`).
- `Runs.toQLePartial` produces QLe's second disjunct, never `ConstantOnPromise`, with `A.queryCap ≤ c`, a syntactic cap over all branches (`:373`).
- `Fkm_QLe` proves `2/3 ≤ L x (Fkm k t C x)` for every `x`, by `hrunT.toQLe` (`Upper/Verify.lean:187`).
- `F` is not constant: `addressedF_dummy` and `addressedF_planted` give both values.
- `budget` counts the `2` per read in `stageCost` and `searchCost`, and `Tests` has the card of `card_testIndex`.

**The `D ≤ 20736 Q⁴` check.** `G < R ≤ D ≤ 20736 Q⁴` with `Q ≤ C 2^t (2t)^6` would fail for a degenerate model. It requires `m^(2-1/k) / (100 (2t)²) ≲ 20736 C⁴ m² (2t)^24`, which holds since `2 - 1/k < 2`. Computed with exact integers for `k` in `{2, 3, 4, 10}` and `t` in `{8, 16, 32, 64, 128}` with the real `budgetConst`: all consistent. For example, at `k = 2`, `t = 128`, `G = 10^108.8` and the forced lower bound `Q ≥ 10^26.1` sits below the cap `10^75.1`. Stress run with `C = 1`, `k < 40`, `8 ≤ t < 200`: 0 contradictions.

The check has teeth because it holds for every `k`. The window between the forced lower bound and the cap is `C_k (2t)^6.5 m^(1/(4k))` up to absolute constants, so a model that undercharged `Q` by `m^ε` would contradict `D ≤ 20736 Q⁴` at large `k`, given Bansal-Sinha. `2 - 1/k → 2 = 4 · (1/2)` is the theorem itself.

**Thresholds.** `L ≥ 1` first holds at `t = 8` for `k = 2`: computed `L = 0` at `t = 7` and `L = 1` at `t = 8`, matching `four_mul_sq_le_two_pow`. `discrepancy_le` needs no lower bound on `t`.

**Lower bound.** `planted` differs from `dummy` only where `eq_of_dummy_ne_planted` says. `addressedF_not_RLe` fixes trees by averaging over `P.weight`, uses `h1` only on `A` in the support of `prodW (prodW μ)` (`Main.lean:164` to `:175`), and uses only `exists_transcript` from the circuit.

**Escape hatches.** Text search of `lean/QuarticQuery` for `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `opaque`, `extern` and `csimp` finds only the word "axiom" in two comments. This is a text search, not an axiom report.

## Definitions: what was tried and held

`Statement.lean` was last changed in commit `7047335`, before the first pass, so the following still stands. All of it was read against Sections 1, 1.3, 2.1, 2.2, 3.2, 4.2 and equations (1) to (8), (10), (17). Formulae were read in `source.pdf` pages 1 to 6, since the text extraction garbles some displays.

- **Input-independence of the quantum model.** `∃ w ψ₀ A` precedes `∀ x`, and `AdaptiveProgram` has no constructor that mentions `x`. `bitOracle` is the only place `x` enters `outputMass`. Isometries and measurement sets are therefore fixed before the input, and `S` is a fixed `Finset`.
- **Could the model be too strong?** `→ₗᵢ` on a finite-dimensional space is unitary. Measurement branches are charged by the `max` in `queryCap`. `exists_fixedSequence` compiles any program into `T` phase queries with input-independent gates in complexitylib's independent model, and `D_le_Q_pow_four` then gives `D ≤ 20736 Q⁴`, so a program with a hidden leak would contradict a proved bound. This holds assuming the proofs check.
- **Could the model be too weak?** Standard fixed-sequence algorithms are `unitary` and `query` chains by construction. Any initial state is allowed, and a preparation adds no query. `w` is any finite number. Controlled queries cost two bit queries, as in the paper (Section 3.3, end). Any binary projector is a coordinate projector conjugated by a unitary. So `Q` is the standard quantity, with no constant-factor change.
- **The syntactic cap.** `queryCap` also counts branches unreachable on promised inputs. Truncating at depth `t` and answering arbitrarily changes nothing on the promise, so this does not change `Q`, and the same holds for `RLe`.
- **`ConstantOnPromise`.** For a function that is not constant on its promise, the disjunct is false, so `Q` is unchanged. For a constant function on nonempty `ι`, the second disjunct already gives budget 0. The disjunct only matters when `ι` is empty, where `State` has no unit vector and every function is constant. `constantOnPromise_of_isEmpty` confirms this.
- **`RandomizedProgram`.** `success` is the weighted sum over trees, and `depth` is the supremum over a support of positive weights. A randomized algorithm of worst-case cost `t` on finite `ι` fixes its coins to a tree of depth at most `t`. There are finitely many such trees (`finite_depth_le`), so it is a finite mixture, and `exists_program_of_mixture` removes zero weights. Depth charges every query on the longest path, as the paper does.
- **`sInf ∅ = 0`.** `R`, `D` and `Q` are all genuine minima by `RLe_R`, `DLe_D` and `QLe_Q`. `alphaTot` is safe: `alphaTot_eq_four_of` uses `IsLeast`, so emptiness of the set cannot produce the value.
- **Equation (1).** `0 ≤ α`, `n ≥ 1`, `1 + Q` and the quantifier order match. `0 < C` is harmless, since `C` can be enlarged.
- **Forrelation.** Numerator paths, the `k - 1` factors, the denominator `2^(2t) (2^t)^(k-1)`, `true ↦ -1`, both thresholds, and undefinedness on large negative `Φ` all match. `Phi_eq_matrix_product` confirms the matrix form, and the `k = 2`, `t = 1` census and the witness `Φ = -1` show the promise is neither empty nor total.
- **Circuit.** Gates read strictly earlier gates, so the circuit is acyclic. `none` is a free constant-false wire, and `table` is any two-input function, which is fan-in two. `domainOut` and `valueOut` are stored gates. Transcripts hold one bit per stored gate and inputs are read directly.
- **`BitLoc`.** Four disjoint summands: `X` strings, `A` strings, pointer bits for each `(i, s, j ≠ i, b)`, transcript bits for each `(i, s, h, g)`. Each column has its own `2^r` cells, pointers have `ℓ` bits through a bijection, and there is one transcript per `h`.
- **`WinsAt` and `addressedF`.** The four conjuncts are the conditions around (7) and (8). `winsAt_iff_paperWinsAt` and `winsAt_iff_localTests` agree with this reading.
- **Parameters.** `ℓ = 2t` and `r = 40t` are exact for `m = 4^t`. `Lvalue` and `Gvalue` match (5) and (17).
- **`BansalSinhaLower`.** It transcribes Lemma 2.1(i), with `t₀` depending on `k`, which the adjudication requires. It is a hypothesis about this `R` and this `P`.

The `Separation` challenge states the five theorems of `Separation/Solution.lean` over a copy of the vocabulary, and `tools/build_challenges.py --check` reports 4 bundles current, exit 0. That checks the bundles against their generator; I did not repeat the comment-stripped comparison of the first pass.

## Effect on generated files

`corpus/ties.json`, `corpus/statements.json`, `corpus/evidence-graph.json` and `corpus/coverage.json` were regenerated with `python3 -I tools/build_corpus.py`, and `--check` exits 0. No row or tie is `unassessed` now. `corpus/coverage.json`: 16 exact, 8 stronger, 43 partial, 1 weaker, 53 none, by best relation per row. `build` and `comparator` remain `not_run` for all 121 rows (finding 9). `corpus/evidence-graph.json` still describes its `fidelity_review` evidence as not yet run, since a generator string owns that text.

## What I did not check

- No Lean was run, so no statement here is a build result. No `#print axioms` was run. `lean/.lake/build` holds `.olean` files newer than their sources for `Results/Conditional`, `Upper/Bound` and `LowerBound/Planted/Main`, which suggests a build, but no `lean_build` receipt exists, and I give that no weight as evidence.
- Complexitylib was checked in the first pass only by a grep for `sorry` and `axiom` in `Complexity/Computability/QueryComplexity`. Its proofs were not read. `universalPower_four` rests on it.
- The truth of Bansal-Sinha, and whether its thresholds match. I relied on the adjudication's reading of the source (R1-AF-06, and R1-AF-06a records it as unverified).
- Second pass, read in full: all of `Upper/`, `LowerBound/Planted/`, `Results/Conditional.lean`, `Results/Exponent.lean`, `Results/Headline.lean`. Tactic steps were read for the logic, not replayed, except `zero_search_sum`'s main case. `budget_le` was not rederived term by term.
- Files the second pass relied on through statements only: `Forrelation/Circuit.lean` (`forrCore_spec`, `coreSize_le`), `Amplification/Geometry.lean` and `Bounded.lean` (`trialFail_le`, `phaseEq_normalised_good_iterate`), `Forrelation/Repetition.lean` (`threshold_correct`, `threshold_correct_third`), `Tournament/Ideal.lean` (`half_lt_total`, `ideal_tournament`). The first pass also read those three families for statements and doc comments, with proofs only where they bore on a route.
- Proof bodies in `Construction/`, `LowerBound/DirectProduct.lean`, `LowerBound/Minimax.lean`, `Bridge/` and `Model/` were read in the first pass. `Results/Conditional.lean` and the `Upper/` and `Planted/` files use them through statements.
- Rows with no tie were not classified. Finding 11 lists candidates, and that list is not complete. The 6 tagged pairs on `def-P` and `claim-butterfly` have no row to attach to, so they are unreviewed.
- The relations are one reviewer's reading under the strict rule. `stronger` on `prop-3.3` assumes `forrCircuit` counts as the paper's construction scheme, as the note in `Statement.lean:291` says.
- `source.pdf` was viewed for pages 1 to 6 only. Sections 3 and 4 were read in `extracted.md`.
- `corpus/receipts/` changed during this pass by another process. Those receipts were read, not reproduced.
