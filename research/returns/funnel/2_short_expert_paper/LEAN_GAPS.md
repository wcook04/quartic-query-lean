# Statement-to-Lean boundaries

This file accompanies `paper.md` and follows its reading order. It distinguishes an absent statement-level match from a different proof, a short assembly of proved facts, and an error in the supplied metadata. These distinctions do not introduce an unproved hypothesis into the headline theorem. The supplied source declares `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.alphaTot_eq_four_unconditional` without a Forrelation assumption.

The assessment is a source audit. Lean and Lake were unavailable in this authoring environment. Neither these mappings nor the proposed signatures in `NEW_STATEMENTS.json` have been freshly compiled here. Recorded builds, Comparator runs and reachability are described in `SOURCE_AUDIT.md`; they are different kinds of evidence. A new corpus ID does not necessarily mean that a new mathematical proof is required.

All source paths below are relative to the supplied `repository/lean/` directory. Declaration names in `correspondence.json` have been checked against the supplied declaration inventory and the relevant source modules. Several corpus entries with empty ties have direct definitions or theorems in the actual source. Such cases are identified below as metadata omissions, not proof gaps.

## 1. Query model and headline

### Unnumbered oracle and exponent definitions

**Passage:** `query-model`. **IDs:** `def-query-oracle`, `eq-1`.

The displayed bit oracle and definition of the optimal exponent have direct counterparts in `QuarticQuery.bitOracle`, `QuarticQuery.UniversalPower` and `QuarticQuery.alphaTot` in `QuarticQuery/Statement.lean:102,323,329`. The universal constant is quantified before the input length and function, and `UniversalPower` includes both nonnegative exponent and positive constant. The absence of a tie on corpus row `eq-1` is not an absent definition. The model's minima are supported by the read-all and attainment results `QuarticQuery.RLe_R` and `QuarticQuery.QLe_Q`; the paper is not relying on the infimum of an empty feasible set.

### Display (1): the full separation theorem

**Passage:** `headline`. **IDs:** `thm-1.1`, `eq-2`. **Boundary:** short asymptotic assembly and alternative proof inputs.

The literal type of `QuarticQuery.theorem_1_1_unconditional` in `QuarticQuery/Results/Unconditional.lean:23` gives `alphaTot = 4`, `UniversalPower 4`, and a family indexed by `t`, with `m = 4^t`. It supplies an existential exact circuit, an explicit polylogarithmic quantum budget, and the strict floor bound `Gvalue (mValue t) (Lvalue k t) < R (...)`. Its lower-bound conjunct is not written in the display's Omega form.

The conversion is supported by `QuarticQuery.Gvalue_ge`, `QuarticQuery.rpow_le_of_Gvalue_lt` and `QuarticQuery.familyBoundsAt_of_parts` in `QuarticQuery/Results/Exponent.lean`; the floor estimate gives the constant `1/400` for `k >= 2`, `t >= 8`. `QuarticQuery.Upper.Q_Fkm_le` supplies a sufficient logarithmic exponent six. Thus the displayed asymptotic theorem follows by assembling proved components. The existing corpus marks the combined headline exact but the separate family row `eq-2` partial; this return preserves the distinction between the literal formal type and its asymptotic presentation.

The Forrelation input is proved by the alternative route in Section 5. The universal quartic bound is obtained through complexitylib and model bridges, as described under Section 6 below. No single fixed value of `k` is asserted to achieve exponent four.

## 2. Construction

### Forrelation matrix formula and promise

**Passage:** `forrelation-definition`. **IDs:** `eq-3`, `eq-4`. **Boundary:** notation and definition bridge, not a missing proof.

The frozen `QuarticQuery.Phi` and `QuarticQuery.P` use an integer numerator and exact integer threshold tests. `QuarticQuery.Forrelation.Phi_eq_matrix_product` identifies the matrix expression, and `QuarticQuery.Forrelation.P_eq_cases` identifies the displayed partial-function cases. Their hypotheses apply in the manuscript's range `k >= 2`. The normalization and the asymmetric treatment of large negative values are retained. These source theorems supply the display even though the corpus marks the individual ties partial because each handles only part of its compound row.

### Display (2): the fixed-parameter lower bound

**Passage:** `forrelation-properties`. **IDs:** `eq-5`, `lem-2.1.i`; external implication `claim-bs-to-L`. **Boundary:** alternative proof and a metadata correction.

`QuarticQuery.Lvalue` is the displayed floor definition. `QuarticQuery.ForrelationLower.bansalSinhaLower`, in `QuarticQuery/ForrelationLower/Main.lean:506`, proves exactly the eventual fixed-`k` lower-bound proposition `QuarticQuery.BansalSinhaLower`. The source proves this proposition directly. It does not formalise the entire published Bansal–Sinha Theorem 1.3, its uniform parameter dependence, or the numerical comparison of their lower-bound expression with `L`.

The supplied tie for `claim-bs-to-L` falsely calls this theorem an exact proof of that numerical comparison. The manuscript's separate sentence attributing implication (2) to the published corollary is a literature claim plus an elementary asymptotic comparison. Its correspondence entry has an empty Lean list. The direct lower-bound proof is mapped separately. Both affected rows also misidentify the theorem as a definition in `Statement.lean`; `STATEMENT_CHANGES.json` records these as metadata-only corrections. No mathematical change is made to `lem-2.1.i`.

### Display (3): numerator and integer threshold tests

**Passage:** `exact-circuit`. **IDs:** `claim-N-phi`, `claim-integer-tests`. **Boundary:** assembly of identities.

The displayed package combines `QuarticQuery.forrelationNumerator`, `QuarticQuery.forrelationDenominator`, `QuarticQuery.Forrelation.numerator_eq_walk`, `QuarticQuery.Forrelation.Phi_eq_matrix_product`, `QuarticQuery.Forrelation.delta_le_Phi_iff` and `QuarticQuery.Forrelation.abs_Phi_le_iff`. No one named theorem states this entire package in the manuscript's `N,M,W` notation. The exact tests and the circuit realization are supported by `QuarticQuery.Forrelation.forrCore_spec`, `QuarticQuery.Forrelation.forrCircuit_realises` and `QuarticQuery.Forrelation.forrCircuit_size_le`. The O-notation explanation is the arithmetic interpretation of the proved size bound, not an additional asymptotic circuit theorem silently inferred from the numerator bound alone.

### True address, display (4), and the winner predicate

**Passages:** `layout`, `winner-definition`. **IDs:** `eq-7`, `eq-8`, `def-F`, `claim-winner-fidelity`. **Boundary:** direct definitions and already-proved equivalence.

The true address agrees with `QuarticQuery.trueAddress` on the promised instances, using `QuarticQuery.apply_eq_trueAddress`. The outward-pointer condition is a clause of `QuarticQuery.WinsAt`. The total function is `QuarticQuery.addressedF`, specialized by `QuarticQuery.Fkm`. `QuarticQuery.winsAt_iff_paperWinsAt` supplies the informal/formal winner equivalence, and `QuarticQuery.winsAt_column_unique` proves uniqueness. Empty ties on the pointer and uniqueness rows are metadata omissions; these are not missing proofs. The four-column example is an illustrative evaluation of the pointer predicate, not a new general theorem.

### Display (5): number and depth of tests

**Passage:** `local-tests`. **IDs:** `def-K`, `lem-2.2.i`. **Boundary:** compound statement and inherited specification correction.

`QuarticQuery.card_testIndex` in `QuarticQuery/Construction/LocalTests.lean:132` gives the exact count. The asymptotic equality uses `r = 20 log_2 m` and the circuit-size theorem. `QuarticQuery.localTestTree_eval`, `QuarticQuery.localTestTree_depth_le` and `QuarticQuery.winsAt_iff_localTests` give, separately, exact evaluation, the bound `max(3, ell+1)`, and the conjunction's meaning. No one source declaration states the whole corpus row, but its mathematical components are present.

The earlier ledger's fixed-coordinate-support wording was corrected in the supplied adjudication. The current attached preprint already says O(log m) queries and describes the adaptive pointer lookup explicitly. This return therefore treats the adaptive-depth formulation as a precise specification and an inherited ledger correction, not as a newly found false assertion in the attached preprint. Coherent access is supplied separately by the compiler and `QuarticQuery.Upper.test_samples`.

## 3. Quantum upper bound

### Display (6): parameters

**Passage:** `comparison`. **ID:** `def-T-eps`. **Boundary:** direct definitions.

`QuarticQuery.Tournament.Tval` and `QuarticQuery.Tournament.epsval` implement the displayed parameters. The ceiling is expressed through the natural ceiling logarithm. The identities and numerical consequences are proved by `QuarticQuery.Tournament.Tval_mul_epsval`, `QuarticQuery.Tournament.miss_bound_le` and `QuarticQuery.Tournament.total_error_lt`. A definition does not require a separately tied theorem simply because the corpus only lists its consequences.

### Display (7): comparison laws

**Passage:** `comparison`. **IDs:** `eq-10`, `eq-11`, `claim-winner-dominates`. **Boundary:** combined predicates and theorems.

`QuarticQuery.Upper.cmpProb_isComparison` provides complementarity and self-comparison zero through `QuarticQuery.Tournament.IsComparison`. `QuarticQuery.Upper.cmpProb_winner`, together with correct-address decoding, provides the dominant-row inequality. `QuarticQuery.winner_no_incoming_zero` and `QuarticQuery.winner_finds_zero` express the off-promise mechanism. The empty tie on `eq-11` is not a missing dominance theorem. These conclusions are split across declarations rather than packaged as one three-part display.

### Abstract amplification, decomposition, display (8), and display (9)

**Passages:** `amplification-statement`, `amplification-proof`. **IDs:** `lem-3.1`, `claim-grover-state`, `eq-9`. **Boundary:** exact abstract theorem; distinct application implementation.

`QuarticQuery.Amplification.Preparation.state_eq`, `.iterate_eq`, `.grover_rotation` and `.phaseEq_normalised_good_iterate` give the decomposition, rotation and successful-state claim. `QuarticQuery.Amplification.average_sin_sq_ge` and `.average_sin_sq_ge_nine_twentieths` supply display (9). The full uniform black-box proposition is `QuarticQuery.Amplification.bounded_amplification` in `QuarticQuery/Amplification/Bounded.lean:242`; the record marks it built but outside the reported final-root reachability closure. That reachability fact does not make it unproved.

The final bit-query upper bound uses `QuarticQuery.Upper.Samples.amplify`, not a compilation of the abstract `Proc`. It proves an exact law of the measured successful label, a failure bound, and a worst-branch cap. Its retries measure the complete computational basis and reset the known state. The manuscript acknowledges this distinction in `tournament-formal-route`. The abstract full-state theorem should not be cited as though its entire procedure were the compiled final algorithm.

### Displays (10) and (11): drift and ideal absence

**Passage:** `tournament-drift`. **IDs:** `eq-13`, `eq-14`. **Boundary:** exact source statements, despite incomplete metadata.

`QuarticQuery.Tournament.expected_weight_eq` and `.expected_weight_le_half` in `QuarticQuery/Tournament/Drift.lean:55,71` supply the drift calculation for positive total weight. The absorbing zero state is covered by the process semantics. `QuarticQuery.Tournament.expected_final_weight`, `.dominant_weight_lb` and `.ideal_miss_le` supply the iteration and absence bound. The empty tie list for `eq-13` must not be reported as an absent formal drift proof. No ranking or transitivity assumption is present in `IsComparison`.

### Display (12): tensor-product sampler, and the list-output interface

**Passages:** `tournament-sampler`, `tournament-formal-route`. **IDs:** `eq-15`, `construct-sampler`, `claim-success-prob`, `claim-coupling`, `prop-3.2`. **Boundary:** a missing exact state-format statement and a different program interface.

The precise bra-ket tensor-state expression has no tied theorem in that notation. `QuarticQuery.Upper.stage_samples` constructs the circuit through the sampler combinators; `.stageLaw_some` and `.sum_stageLaw_some` give the relevant unnormalized label mass and total success probability. Combined with `.Samples.amplify`, these establish the conditional candidate law used by the algorithm. The displayed state is a faithful mathematical explanation of the product construction, but it is not itself the type of one named checked theorem.

The reached `QuarticQuery.Upper.tournament_runs` returns a program that sends candidates to a verifier and bounds acceptance. It does not expose the preprint's stand-alone list-output specification. `QuarticQuery.Upper.tval_lower` gives the history-dependent success calculation used in this continuation. The prose list argument is provided in the manuscript; claiming a separate compiled general list theorem would need an additional interface theorem. This distinction does not weaken the final bound on the total function.

### Display (13): total-function error

**Passage:** `candidate-verification`. **ID:** `claim-error`. **Boundary:** specialization of a theorem and local proof facts.

Although `claim-error` has an empty tie list, `QuarticQuery.Upper.tournament_runs` states the two acceptance estimates with its verifier hypotheses. `QuarticQuery.Upper.search_runs` gives the verifier's pass/fail guarantees. The proof of `QuarticQuery.Upper.Fkm_QLe` instantiates these with the true-winner and every-address-fails facts. `QuarticQuery.Tournament.total_error_lt` supplies the final strict numerical bound. There is no separate named theorem whose conclusion is exactly the two probabilities in display (13), but the specialization is present in the final upper-bound proof. This is packaging, not an open proof of correctness on zero inputs or off-promise inputs.

## 4. Randomized lower bound

### Capped direct product and displays (14)–(15)

**Passages:** `direct-product`, `weighted-recursion`, `weighted-product`. **IDs:** `lem-4.1`, `new-dp-recursion`, `new-dp-weighted`. **Boundary:** different proof route; new corpus records for existing formal statements.

The recursion in display (14) is `QuarticQuery.budgetValue` in `QuarticQuery/LowerBound/DirectProduct.lean:40`, with `QuarticQuery.constSuccess` and `QuarticQuery.restrictWeight`. Its optimal-value interpretation follows from `QuarticQuery.exists_tree_budgetValue_le` and `QuarticQuery.treeSuccess_le_budgetValue`. These are proved components; the combined maximum-value formulation requires only a wrapper or the accompanying notation translation.

Display (15) is the direct mathematical reading of `QuarticQuery.guessSuccess_le_prod` at line 258, with nonnegative weights and the per-instance budget predicate `QuarticQuery.OutTree.capped`. Its arbitrary remaining budgets and weights are already in the theorem. No new mathematical proof is needed for this invariant. The new ID records its first displayed appearance in this return.

`QuarticQuery.direct_product_average` and `QuarticQuery.direct_product_randomized` add finite independent side information and coins. The full exact statements are recorded as built but outside the final-root reachability closure; the deterministic form is used inside the final planted proof, with its independent averaging carried out there. The preprint's conditional-optimal-success supermartingale is not the source derivation. This paper intentionally uses the source's induction on unnormalized weights. It does not claim that the untied conditional-value intermediate rows were formalised.

### Planting and the first-difference argument

**Passage:** `planting`. **IDs:** `def-dummy`, `def-planted`, `claim-Y-values`, `eq-18`. **Boundary:** one-sided source theorem.

The dummy and planted input definitions and their Boolean values have named counterparts. `QuarticQuery.QueryTree.exists_mem_path_ne` and `QuarticQuery.eq_of_dummy_ne_planted` prove the first-difference mechanism. The source theorem `QuarticQuery.output_gap_le` in `QuarticQuery/LowerBound/Planted/Main.lean:33` bounds planted-minus-dummy and already separates the planted-cell contribution into heavy and nonheavy parts. It is not a theorem about an absolute difference of averaged output probabilities. The manuscript uses the signed direction explicitly in `classical-gap`; `STATEMENT_CHANGES.json` records the narrower scope relative to `eq-18`.

### Display (16): the coefficient two

**Passage:** `zero-search-induction`. **ID:** `new-zero-search-two`, strengthening the inequality in `eq-19`. **Boundary:** stronger conclusion by an alternative proof; final averaging is an assembly.

`QuarticQuery.zero_search_sum` proves the finite-world induction. `QuarticQuery.column_zero_bound`, `QuarticQuery.avg_foundZero_le` and `QuarticQuery.sum_xQueries_le` assemble it into `QuarticQuery.avg_foundZero_I_le` in `QuarticQuery/LowerBound/Planted/ZeroSearch.lean:226`. The latter fixes the address data and averages the independent zero positions and planted column; its bound is exactly `2G/m^2`. Averaging over the independent address data gives the manuscript's full dummy probability and is explicitly done in the proof of `QuarticQuery.tree_gap_le`.

The manuscript does not use the preprint's auxiliary random variable `Z` or claim that its expectation identity has the same formal representation. The assertion is an upper bound; a finite worst-case cap need not attain the coefficient two.

### Display (17): the per-time joint event

**Passage:** `heavy-simulator`. **ID:** `eq-21`. **Boundary:** no stand-alone theorem in the displayed event syntax.

`QuarticQuery.simTree`, `QuarticQuery.depth_simTree_le` and `QuarticQuery.eval_simTree` in `QuarticQuery/LowerBound/Planted/Simulator.lean` establish the capped simulation. `QuarticQuery.reachedCell` represents the nonheavy-and-cell event. The implementation bounds the union of such events directly in `QuarticQuery.avg_reachedCell_le`; it does not separately export display (17), for each time, in the manuscript's probability notation. The simulator implication and direct-product bound justify the displayed intermediate inequality, and that implication is used inside the proof of the aggregate theorem. A stand-alone per-time wrapper would be a packaging addition.

The joint event is retained. Conditioning the hard input distribution on nonheaviness would require an unsupported step and is not part of either proof.

### Display (18): total planted-cell encounter

**Passage:** `heavy-simulator`. **ID:** `eq-22`. **Boundary:** sum of two formal bounds.

The source `QuarticQuery.avg_reachedCell_le` bounds the nonheavy joint union by `G*rho`, with the required capped-guess hypothesis. `QuarticQuery.avg_heavy_le` supplies `G/(mL)`. Their sum gives the displayed complete cell-encounter bound after `rho = (2/3)^r`. The source's `tree_gap_le` combines these contributions directly rather than first naming a theorem with exactly display (18) as its conclusion. This is a short assembly, not a missing probability estimate.

### Display (19): signed planted gap

**Passage:** `classical-gap`. **ID:** `new-planted-gap-two`, correcting the scope and strengthening a coefficient in `eq-23`. **Boundary:** exact generic theorem with specialization; different numerical packaging later.

`QuarticQuery.tree_gap_le` in `QuarticQuery/LowerBound/Planted/Main.lean:59` proves the signed inequality with coefficient two and a general capped-guess parameter `rho`. It assumes a nonnegative normalized measure supported on the promise, `L >= 1`, and a depth-`G` tree. Substituting `rho=(2/3)^r` from the direct product gives (19). The extension to randomized mixtures is finite linear averaging, performed inside `QuarticQuery.addressedF_not_RLe`.

The later generic exclusion theorem still exposes the more generous coefficient-four numerical hypothesis, despite using the sharper coefficient-two bound internally. Its `QuarticQuery.twoThirds_pow_le` estimate uses `m^(-10)`, weaker than the preprint's exact real exponent `m^(-20 log_2(3/2))`; either suffices. The manuscript's asymptotic tail argument is the elementary consequence of this parameter choice. `QuarticQuery.discrepancy_lt_third` and `QuarticQuery.Gvalue_lt_R_Fkm` prove the numerical exclusion required for the final theorem. No improved separation exponent is inferred from the sharper coefficient.

## 5. Fixed-parameter Forrelation proof

The supplied corpus has no individual rows for the new route's analytic intermediate lemmas. The seven `new-fl-*` IDs register the manuscript's displays. Existing source theorems remain the evidence; the proposed display-level signatures are not claimed to have been compiled in this return.

### Display (20): truncation and derivative

**Passage:** `forrelation-truncation`. **ID:** `new-fl-truncation`. **Boundary:** definitions plus a derivative theorem, not an absent proof.

`QuarticQuery.ForrelationLower.qf`, `.psiS`, `.phiS` and `.dphi` in `QuarticQuery/ForrelationLower/Stein.lean:22–28` are the displayed definitions. `.hasDerivAt_phiS` at line 76 proves the derivative. `.abs_phiS_le`, `.phiS_neg`, `.psiS_pos`, `.psiS_le`, `.dphi_pos` and `.dphi_le` support the subsequent bounds. A bundled conjunction in the display's notation would be a wrapper, not a new analytic argument.

### Display (21): Stein identity

**Passage:** `forrelation-truncation`. **ID:** `new-fl-stein`. **Boundary:** direct source theorem with its regularity hypotheses.

`QuarticQuery.ForrelationLower.stein_one` in `QuarticQuery/ForrelationLower/Stein.lean:137` states the identity under continuity, pointwise differentiability, and uniform bounds on the test function and its derivative. These are the manuscript's continuously differentiable bounded-test assumptions. The multidimensional coordinate form is `.stein_pi`. This display does not require a missing proof; its new ID reflects missing corpus coverage for the route.

### Display (22): mean-value path identity

**Passage:** `forrelation-path`. **ID:** `new-fl-path`. **Boundary:** assembly of named identities.

`QuarticQuery.ForrelationLower.exists_identity` in `QuarticQuery/ForrelationLower/Walk.lean:461` provides some `s` strictly between zero and one and an identity in terms of the recursively defined derivative expression. `.Int_eq_paths` at line 541 expands that expression into paths, and `.integral_ext_wv_zero` in `Cascade.lean:256` identifies the zero endpoint with uniform signs. Combining them yields (22). There is no one source theorem already written as this complete path-sum formula with the manuscript's distribution symbol `D`.

The existence of one `s`, potentially depending on the test function, is essential. This return does not replace it by a claimed checked integral identity or say that higher uniform Fourier levels vanish. The derivatives are at a nonzero bias and have one distinct coordinate in each block.

### Coefficient formula following (22)

**Passage:** `forrelation-path`. **ID:** `new-fl-path-weight`. **Boundary:** unfolded recursive definition and specialization.

The path coefficient is the recursive `QuarticQuery.ForrelationLower.cf`; `.abs_cf_le` in `QuarticQuery/ForrelationLower/Walk.lean:556` bounds it by `(3*epsilon)^(k-1)` when the matrix entries have magnitude at most `epsilon`. Substituting the Walsh bound `epsilon=1/sqrt(m)` gives the stated estimate. The source uses `psiS <= 1` and `dphi <= 3`; it does not justify replacing this by a sharper advertised constant from an earlier blueprint without another argument.

### Display (23): decision-tree advantage

**Passage:** `forrelation-growth`. **ID:** `new-fl-advantage`. **Boundary:** exact specialization; subsequent logarithmic simplification is a short deduction.

`QuarticQuery.ForrelationLower.advantage_le` in `QuarticQuery/ForrelationLower/Cascade.lean:384` gives this bound for a more general orthogonal matrix with bounded entries. It uses `.sum_abs_ext_Dl_le` in `TreeGrowth.lean:738`. The assumptions `d>0`, positive deviation parameter, `k>=2`, bounded tree output, and `kappa^2=8d Lambda` must be retained. The coordinate count is `km`.

The later choice `Lambda=2k ln(4km)`, the resulting tail at most one, and the displayed-in-prose O(log^(-k/2) m) decay follow by algebra with fixed `k` and fixed amplification count. No separately named source theorem states that exact simplified O-notation. `.exists_threshold` in `Main.lean` proves the quantitative eventual smallness needed by the endpoint. The martingale-growth route is attributed to Girish, Tal and Wu; no novelty conclusion follows from the absence of a corpus row.

### Display (24): moments

**Passage:** `forrelation-moments`. **ID:** `new-fl-moments`. **Boundary:** conjunction and notation bridge.

`QuarticQuery.ForrelationLower.ext_PhiF_zero`, `.ext_PhiF_sq` and `.mass_ge` in `QuarticQuery/ForrelationLower/Promise.lean:559,564,499` give the three facts. `.Phi_eq_PhiF` identifies the fixed Forrelation expression. A wrapper combines the three clauses and changes notation from expectations of multilinear extensions to the rounded distribution `D`. The source has the mathematical components; no moment estimate is being inferred merely from an informal blueprint.

### Display (25) and its pointwise inequalities

**Passage:** `forrelation-gap`. **ID:** `new-fl-gap`. **Boundary:** local proof facts, finite averaging, and a proposed display-level wrapper.

`QuarticQuery.ForrelationLower.exists_amplified` in `QuarticQuery/ForrelationLower/Amplify.lean:80` uses `2*tau` repetitions, depth at most `2*tau*L`, and error `(8/9)^tau`. The all-input lower and upper acceptance inequalities in the manuscript are reconstructed from the proof of `.not_RLe_of_gap` in `Main.lean:81`. They are local facts there, not separately named exported theorems with the manuscript's function `a` and distribution `D`. Applying the three moments and integrating gives the displayed gap lower bound. Its complete conjunction is a proposed wrapper, not a new execution-certified declaration.

The two comparison laws need not be promise-supported. Correctness is used only where the two promise cases apply; elsewhere the pointwise inequalities follow from `0 <= a <= 1` and the threshold relations. The planted hard measure is obtained later from finite minimax after the worst-case lower bound has been proved. Identifying it with the Gaussian law would be an unsupported substitution.

The eventual contradiction is established by `.exists_threshold`, `.not_RLe_of_gap` and finally `.bansalSinhaLower`. The endpoint is unconditional even though the displayed explanatory package lacks a single named counterpart.

## 6. Optimal exponent

### Display (26): ratio and limit

**Passage:** `exponent`. **ID:** `claim-exponent-ratio`. **Boundary:** explicit ratio formula is a short deduction; the exclusion theorem is formal.

This ID exists in the supplied corpus. `QuarticQuery.eventually_gt_rpow` in `QuarticQuery/Results/Exponent.lean:118` states that, from eventual family bounds, `R_t > D*(1+Q_t)^alpha` eventually for every constant `D`. It does not state the display's literal lower bound on the quotient or its convergence in that notation. `QuarticQuery.exists_nat_exponent` chooses the fixed integer `k`, and `.not_universalPower_of_family` proves exclusion of every exponent below four. The manuscript supplies the elementary ratio calculation. A separately packaged quotient-limit statement would require a wrapper; it is not a remaining gap in the optimal-power theorem.

The universal upper bound invoked in the same passage is `QuarticQuery.D_le_Q_pow_four` and `QuarticQuery.R_le_D_le_one_add_Q_pow_four` in `QuarticQuery/Appendix/TheoremA1.lean:52,57`. These local-model statements use `Cslib.Quantum.complexity_le_mul_pow_four` through the bit/phase, deferred-measurement and decision-tree bridges. The preprint's individual Appendix A lemmas are not all formalised in their stated form. The passage correctly treats this as a different route to the quartic bound; the local theorem derives from the imported library rather than being itself a declaration inside that external library.

## 7. Evidence claims and remaining review obligations

Sections 7.1–7.2 add no new displayed mathematical theorem. They distinguish mathematical definitions, source proofs, archived execution evidence, and this fresh source inspection. In particular:

- The challenge vocabulary is byte-identical to the common frozen vocabulary, but the challenge and candidate specifications were not independently authored mathematical models. Comparator statement identity does not itself settle informal fidelity.
- The negative tests are expected to be rejected. Their successful test outcomes are not accepted proofs. An initially mismatched expected diagnostic for `WeakenedConclusion` was corrected in the trace; the solution was rejected throughout.
- The reported paranoid receipt identifies the `d42fb67a` prefix, with full preceding commit `d42fb67a7e060fb5386867dadf20a5903df39141`. The supplied source manifest identifies `c7e0c9161f0ad898889bd9166e7b354acd42188d`. No complete supplied diff proves the two source states identical.
- The root dependency inventory and positive Comparator evidence support the unconditional endpoint. Successful descendant `#print axioms` output was found for the Forrelation theorem and a scratch theorem proving `alphaTot = 4` via that theorem. No successful named-root `#print axioms` output was located in the assessed trace regions. This does not turn an observed failed or deferred diagnostic attempt into a successful audit receipt.
- Direct build and Comparator commands are reproducible instructions, not claims of execution in this authoring environment. Several repository automation scripts, archived individual receipts and complete external-kernel logs are absent from the packet. Public availability of the private repository is not assumed.

These are evidence and review limitations. They should not be conflated with an unproved mathematical assumption in the declared headline theorem.
