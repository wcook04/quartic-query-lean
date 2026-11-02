# Statement fidelity review

Reviewer: `ai:truth-auditor`, 2 November 2026. Independent reading of `lean/QuarticQuery/Statement.lean` and the proposed ties against the preprint. Lean was not run, so nothing here says that a file compiles. Relations are in `corpus/ties.json`.

## Result

I found no definitional error in `Statement.lean`. Every definition matches the preprint, and the attacks listed below did not break any of them.

The one finding that changes what a theorem means is that `alphaTot_eq_four` is conditional on all of equation (2), not on the Bansal-Sinha lower bound alone. The other serious findings are in the corpus builder, which drops the ties for the main theorems and misnames declarations.

Tie counts, computed from `corpus/ties.json`: 221 ties on 50 rows. Relations: 21 exact, 4 stronger, 194 partial, 2 weaker. Routes: 86 same, 11 alternative, 124 none. Exact or stronger ties exist on 19 rows.

## Findings, most severe first

### 1. The headline is conditional on all of equation (2)

- Where: `lean/QuarticQuery/Results/Headline.lean:21`, `lean/QuarticQuery/Results/Exponent.lean:170` and `:178`, `lean/QuarticQuery/Statement.lean:319`.
- Paper: Theorem 1.1, with Lemma 2.1(i) as the only external input (Section 1.2, end).
- What is wrong: `alphaTot_eq_four (hfam : FamilyBounds)` takes both bounds of (2) for every `k` as a hypothesis. `FamilyBounds` contains Propositions 3.3 and 4.2. `BansalSinhaLower` occurs only in `Statement.lean` and in its copy in `lean/QuarticCorpus/Tournament/Challenge.lean`; grep finds it in no other file, including `LowerBound/Planted/` and `Upper/`. The `thm-1.1` proof note in `research/returns/adjudication.json` says the evidence class is conditional on Bansal-Sinha for all `k >= 2`. That does not describe this theorem.
- Consequence: `alphaTot_eq_four` says that the exponent arithmetic and the quartic bound reduce Theorem 1.1 to (2). It does not say that the preprint's own mathematics has been checked. Its tie is `partial`, with `FamilyBounds` listed.
- Fix: prove `BansalSinhaLower → FamilyBounds` once `Upper/` and `Planted/` are finished, with one circuit, `forrCircuit (k-1) t`, for both bounds. Then state `alphaTot_eq_four (h : BansalSinhaLower)`. Until then, label the result as conditional on (2).

### 2. The builder truncates every statement id that contains a dot

- Where: `tools/build_corpus.py:44`, `DOC_TIE = re.compile(r"Ledger:\s*([^\n.]+)")`.
- Paper: `thm-1.1`, `thm-A.1`, `lem-2.1.ii`, `lem-2.1.iii`, `lem-2.2.i`, `lem-3.1`, `lem-4.1`, `lem-A.2`, `prop-3.2`, `prop-4.2`.
- What is wrong: the pattern stops at the first dot, so `Ledger: thm-1.1.` yields the id `thm-1`, which matches no row and is discarded without a message. I replayed `declared_ties` in memory with a corrected pattern. 69 tagged declarations are lost: 54 in the reviewed tree and 15 in `Upper/` and `Planted/`. `corpus/statements.json` therefore reports `thm-1.1`, `lem-4.1` and `thm-A.1` as having no Lean evidence, and `corpus/coverage.json` undercounts.
- Fix: match ids with `[A-Za-z0-9-]+(?:\.[A-Za-z0-9]+)*`, separated by commas. `corpus/ties.json` already holds reviewed entries for these 54 declarations, in the spelling the corrected builder produces. They have no effect until this is fixed.

### 3. The builder misnames declarations after any `end` of a section

- Where: `tools/build_corpus.py:91` to `:97`.
- What is wrong: the scan treats `end Tests` and `end Attainment` as closing a namespace, so it pops `QuarticQuery` although no `namespace` was opened for them. Later declarations in the file lose the prefix. In the reviewed ties 16 names are affected, for example `R_reindex`, `RLe_reindex_iff`, `winsAt_iff_paperWinsAt` and `addressedF_eq_true_iff`. The real names start with `QuarticQuery.`.
- Consequence: `statement_records` matches names against receipts by exact string, so a receipt with the real name can never mark these ties built or compared.
- Fix: track `section` as well, or take names from the compiled environment. `corpus/ties.json` uses the current spelling, as the brief required. Once the builder is fixed, prefix these 16: `DLe_reindex_iff`, `D_reindex`, `RLe_reindex_iff`, `R_reindex`, `TestIndex`, `addressedF_eq_true_iff`, `addressedF_eq_true_iff_localTests`, `card_testIndex`, `exists_failing_localTest`, `localTest`, `localTestTree`, `localTestTree_depth_le`, `localTestTree_eval`, `winsAt_iff_localTests`, `winsAt_iff_outputs`, `winsAt_iff_paperWinsAt`. The namespace prefix is the review's inference from the Lean files; it was not read from a compiled environment.

### 4. `FamilyBoundsAt` is not literally equation (2) for the paper's function

- Where: `lean/QuarticQuery/Results/Exponent.lean:170`.
- Paper: equation (2), with `F_{k,m}` built from `C_{k,m}` of size `O_k(m (log m)^2)`.
- What is fine: the package uses one circuit for both bounds, as the adjudication requires. As a hypothesis it is enough, and asking only for some realising circuit makes the theorem stronger, since the conclusion does not mention the circuit.
- What differs: `Cir` is any circuit realising `P`, with no size bound, so the package speaks of a family of total functions that may differ from the paper's. `b` is a natural number, possibly zero. That is harmless, since a real `b_k` rounds up for `t >= 1`.
- Fix: if the package is to be read as (2), add `(Cir.size : ℝ) ≤ c * mValue t * (2 * t) ^ 2` or fix `Cir = forrCircuit (k-1) t`. Neither changes `alphaTot_eq_four`.

### 5. Lemma 2.1(ii) has no quantum statement in the reviewed tree

- Where: `lean/QuarticQuery/Forrelation/Repetition.lean:28`, `:218`, `:234`.
- Paper: Lemma 2.1(ii) and the first half of its proof.
- What is wrong: `successProb` is the squared length of a real vector, and `threshold_correct` is a binomial tail bound. No `AdaptiveProgram` occurs, so query cost, the coherent implementation and behaviour off the promise are not stated. "Each using `k` queries" in the doc comment at `:234` is not part of the theorem. This is honest as scaffolding, and the rows are `partial`. It should not be read as a check of the lemma.
- Fix: state the lemma with `QLe`, which is presumably `Upper/` work. I did not check that directory.

### 6. Lemma 3.1 is about `Proc`, not about the bit oracle

- Where: `lean/QuarticQuery/Amplification/Procedure.lean:33` and `:54`.
- Paper: Lemma 3.1, "with fresh registers".
- What is fine: `bounded_amplification` is an exact match for the corrected row. One `Proc` depends on `γ` and `η` only and works for every `A`, with `138 √γ⁻¹ log(1/η)` calls on every branch.
- What remains: `restart` resets a vector and keeps its mass, which has no direct `AdaptiveProgram` step. Whoever compiles `Proc` into `AdaptiveProgram` must allocate fresh workspace for each trial and account for the discarded registers. `mix` also accepts arbitrary real weights. `attempts` uses `trialWeight`, which sums to 1 by `sum_trialWeight`, so the only reviewed use is fine.
- Fix: none needed here. Check this at the compilation step.

### 7. Two tagged ids match no row

- Where: `Ledger: def-P` at `lean/QuarticQuery/Forrelation/Promise.lean:63`, `:70`, `:87`, and `Ledger: claim-butterfly` at `lean/QuarticQuery/Forrelation/Walsh.lean:71`, `lean/QuarticQuery/Forrelation/Circuit.lean:25`, `:40`.
- What is wrong: the builder drops unknown ids silently, which is also what hid finding 2.
- Fix: make unknown ids a hard error. Replace `def-P` with `eq-4`, and add a `claim-butterfly` row or retag these under `claim-circuit-size`.

### 8. Tags missing or in the wrong place

`Statement.lean` has no `Ledger:` tag at all, so several definition rows are tied only to supporting lemmas although a faithful definition exists. Statement.lean is frozen for this review; `research/` was not edited either. These tags would give an `exact` tie:

| Row | Declaration | Location |
| --- | --- | --- |
| `eq-1` | `alphaTot`, with `UniversalPower` | `Statement.lean:323`, `:329` |
| `eq-5` | `Lvalue` | `Statement.lean:309` |
| `eq-17` | `Gvalue` | `Statement.lean:314` |
| `eq-8` | fourth conjunct of `WinsAt` | `Statement.lean:282` |
| `eq-10` | `Tournament.IsComparison` | `Statement.lean:302` |
| `eq-11` | `Tournament.Dominant` | `Tournament/Ideal.lean:220` |
| `lem-2.1.i` | `BansalSinhaLower`, as the external hypothesis | `Statement.lean:319` |
| `def-column-layout` | `BitLoc`, `readX`, `readA`, `readPointerBit`, `readTranscript` | `Statement.lean:245` to `:265` |
| `def-win-at-address` | `winsAt_iff_outputs` | `Construction/LocalTests.lean:287` |
| `def-winner` | `WinsAt` with `winsAt_iff_paperWinsAt` | `Statement.lean:277` |
| `def-grover-trial` | `amplify` | `Amplification/Procedure.lean:82` |
| `def-T-eps` | `Tval`, `epsval` | `Tournament/Ideal.lean:296`, `:299` |
| `eq-7` | `trueAddress` | `Construction/LocalTests.lean:307` |
| `eq-13` | `expected_weight_eq`, `expected_weight_le_half` | `Tournament/Drift.lean:55`, `:71` |
| `cor-unique-winner` | `winsAt_column_unique` (now under `def-F`) | `Construction/Winner.lean:42` |
| `cor-local-dichotomy` | `localTests_iff_eq_of_winsAt`, `exists_failing_localTest` | `Construction/LocalTests.lean:262`, `:268` |
| `claim-circuit-size` | `forrCircuit_size_le` (now under `lem-2.1.iii`) | `Forrelation/Circuit.lean:466` |
| `claim-weight-lb` | `half_lt_total` | `Tournament/Ideal.lean:254` |

Tags in the wrong place:

- `lem-A.2` sits on `FixedSim.build` and `exists_fixedSequence` (`Bridge/Deferred.lean:268`, `:286`). They prove deferred measurement, which is one step of that proof. The adversary bound itself has no declaration in this repository, because it lives inside complexitylib.
- Most `def-query-oracle` tags are on the Hadamard gadget in `Bridge/Oracle.lean`. They support the bridge and do not pin `O_x`.

### 9. Strict relations that one small theorem would lift

Under the strict rule, these rows have no single `exact` tie although two declarations together cover them. A conjunction theorem or a split row would raise them:

- `eq-3`: `Phi_eq_matrix_product` with `Forrelation.delta`.
- `eq-4`: `P_eq_cases` with `cases_disjoint`.
- `claim-integer-tests`: `delta_le_Phi_iff`, `abs_Phi_le_iff` and the `d`, `b` assembly.
- `claim-grover-state`: `iterate_eq`, `state_eq`, `angle_mem`, `phaseEq_normalised_good_iterate`.
- `eq-9`: `average_sin_sq_ge` with an extracted middle inequality.
- `claim-numeric`: the three sub-bounds in `discrepancy_le` are inside its proof and could be exported.

`def-query-oracle` is the same kind of case: `Statement.bitOracle` with `bitOracleL` and `bitOracle_bitOracle`.

### 10. One tie is weaker by design

`twoThirds_pow_le` (`Results/Exponent.lean:429`) gives `m^-10`, while the paper's exponent is `20 log_2(3/2) = 11.70`. `claim-tail` also carries the `G` factor and `o(1)`. `m^-10` suffices for `discrepancy_le`, so this needs no fix. The tie is `weaker`.

## Definitions: what was tried and held

All of `Statement.lean` was read against Sections 1, 1.3, 2.1, 2.2, 3.2, 4.2 and equations (1) to (8), (10), (17). Formulae were read in `source.pdf` pages 1 to 6, since the text extraction garbles some displays.

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
- **Challenge copy.** After removing comments, `lean/QuarticCorpus/Tournament/Challenge.lean` differs from `Statement.lean` only by its two added theorem statements and the wrapper lines.

## Effect on generated files

`corpus/ties.json` is new, and `corpus/statements.json`, `corpus/evidence-graph.json` and `corpus/coverage.json` were not regenerated. They are now stale against it. Ties on rows affected by finding 2 are not picked up until the pattern is fixed.

## What I did not check

- No Lean was run, so no statement here is a build result. No `#print axioms` was run. The complexitylib closure was checked only by a grep for `sorry` and `axiom` in `Complexity/Computability/QueryComplexity`, which found none. I did not read that library's proofs.
- `LowerBound/Planted/` and `Upper/` were excluded. That removes 27 proposed ties from `corpus/statements.json` and 15 lost ones, and ten rows have no entry in `corpus/ties.json`: `claim-coherent-access`, `def-dummy`, `def-planted`, `claim-Y-values`, `eq-18`, `eq-19`, `eq-20`, `eq-21`, `eq-22`, `eq-23`. Both directories changed while I worked.
- The truth of Bansal-Sinha, and whether its thresholds match. I relied on the adjudication's reading of the source.
- Proof bodies were read in `Construction/`, `LowerBound/DirectProduct.lean`, `LowerBound/Minimax.lean`, `Bridge/`, `Model/` and `Results/`. In `Forrelation/`, `Tournament/` and `Amplification/` I read statements and doc comments, with proofs only where they bore on a route. Routes there rest on that reading.
- Rows with no proposed tie were not classified. I report candidate tags for some in finding 8, but that list is not complete.
- `source.pdf` was viewed for pages 1 to 6 only. Later sections were read in `extracted.md`.
