# Sections 4–5: conditional values, planting, and the exponent

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

This advisory development supplies a proposed Lean proof of the preprint's conditional-value direct-product argument, the absolute planted/dummy probability estimates, the exact logarithmic tail, and the quotient argument for every fixed exponent below four. Every assigned statement has an entry below with its mathematical meaning, proposed declaration, dependencies, and correspondence qualifications.

**Evidence boundary.** All new Lean is **unelaborated**. No Lean executable was available, and no new kernel, build, Comparator, or dependency-closure result is claimed. The complete proofs are source proposals. The expected-zero endpoint uses the permitted alternative route through the stronger existing search bound; the compound `claim-EZ` row remains partial because its early/late subclaims are absent. See [LEAN_GAPS.md](LEAN_GAPS.md) for the complete boundary and [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) for the required compilation.

## Mathematical scope and notation

The preprint is OpenAI's *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026, Sections 4–5 [P1]. Its family uses $m=4^t$, $r=40t$, the address-query budget $L$, and $G=\lfloor mL/100\rfloor$. Each use of a probability law assumes nonnegative normalized input weights supported on the partial function's promise. The generic Lean algebra sometimes needs fewer hypotheses; it acquires its probabilistic interpretation only under these assumptions. All algorithms here have worst-case query caps. The same realizing circuit is used whenever the two complexities of one function are compared.

The extra conditional-value proof reuses the existing one-instance optimum and its attainment theorem. It adds the conditional law of an actual adaptive transcript, the remaining query budget, the two-answer expectation, finite iteration, and a bound on the actual algorithm's success. This is substantially more work than invoking the existing direct-product endpoint. It provides a declaration for each displayed step of the written argument; it does not improve the bound. The existing shorter proof can remain the headline dependency.

Drucker's conditional values and transcript-independence lemmas are the closest proof reference [DP1, Lemmas 3.1–3.2, the following product argument, and the final paragraph of Section 3]. Shaltiel introduced the separately capped fairness condition; his displayed fair-tree theorem is an XOR-advantage statement [DP2, Section 5, Definition 4, Theorem 5, Lemma 7]. These are attribution and proof references. They do not certify any new Lean file.

Finite mixtures represent the project's independent coins and side information. No measure-theoretic pushforward from arbitrary external probability spaces is formalized, and no Mathlib `Supermartingale` instance is constructed. The finite conditional inequalities, finite horizon, and actual-algorithm consequence are stated directly. Repeated queries count against the cap, and zero-probability transcript branches are handled before cancellation.

The classes below use the assignment's four alternatives: `already_stated_under_another_name`, `few_lines_from_existing_declarations`, `genuine_new_proof`, and `prose_not_a_theorem`. Each assigned item has mathematical content, so none is discarded as prose. For definitions, agreement with the source implementation is the relevant proof obligation. All Lean snippets below are **unelaborated**; surrounding namespace, variables, instances, and helper definitions are in the linked module.

<!-- passage:classical-claim-product-law -->
## `claim-product-law`

**Class:** `genuine_new_proof`. **Compilation:** unelaborated. **Difficulty:** medium.

For a positive-probability transcript $\tau$, define $E_h(\tau)$ by the observed bit constraints on input $h$. The actual execution event is a rectangle, and
\[
\Pr[U=u\mid\tau]=\prod_h\Pr[U_h=u_h\mid E_h(\tau)].
\]
This is `claim-product-law`; the prefix proof accounts for the adaptive schedule.

**Lean statement (unelaborated).** The namespace is `QuarticQuery.Paper`; the file supplies the finite-type variables and definitions.

```lean
theorem classical_transcript_product_law {β : Type}
    (T : OutTree (Fin r × κ) β) (τ : ClassicalTranscript r κ)
    (μ : Fin r → BitInput κ → ℝ)
    (hm : 0 < ∑ V : Fin r → BitInput κ,
      if classicalPrefix T τ V then ∏ h, μ h (V h) else 0)
    (U : Fin r → BitInput κ) :
    (if classicalPrefix T τ U then ∏ h, μ h (U h) else 0) /
        (∑ V : Fin r → BitInput κ,
          if classicalPrefix T τ V then ∏ h, μ h (V h) else 0) =
      ∏ h, classicalLaw (classicalTranscriptWeight μ τ h) (U h)
```

**Proof and correspondence.** The finite identity is pointwise and uses an actual deterministic `OutTree` execution-prefix event. The proof first derives schedule consistency from positive transcript mass; transcript rectangularity is proved, not assumed. The algebraic identity itself needs no sign hypothesis; its probabilistic interpretation uses the nonnegative independent priors already assumed in Lemma 4.1. Repeated coordinates are retained in the transcript. The separate positivity helper proves that every local restricted mass is positive from nonnegative priors and positive actual transcript mass.

**Declarations used:** `QuarticQuery.Paper.classical_prefix_iff`, `QuarticQuery.Paper.classical_rectangle_weight`, `QuarticQuery.Paper.classical_mass_product`, `QuarticQuery.Paper.classical_product_law`, `QuarticQuery.Paper.classical_product_marginal`, `QuarticQuery.Paper.classical_transcript_mass_pos`.

**Source:** preprint [P1], Section 4.1, pp. 11–12; Drucker [DP1], Lemmas 3.1–3.2 and the following product argument. The source declarations are in `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`.
<!-- /passage:classical-claim-product-law -->

<!-- passage:classical-def-value-V -->
## `def-value-V`

**Class:** `genuine_new_proof`. **Compilation:** unelaborated. **Difficulty:** medium.

With $q_h(\tau)$ counting queries to instance $h$, including repetitions,
\[
V_h(\tau)=\max_{T:\operatorname{depth}(T)\le L-q_h(\tau)}
 \Pr[T(U_h)=P(U_h)\mid\tau].
\]
This is `def-value-V`. The implementation divides the existing weighted Bellman value by the transcript mass and proves the maximum characterization in both directions.

**Lean statement (unelaborated).** The namespace is `QuarticQuery.Paper`; the file supplies the finite-type variables and definitions.

```lean
noncomputable def classicalTranscriptValue (f : PartialBool κ)
    (μ : Fin r → BitInput κ → ℝ) (τ : ClassicalTranscript r κ)
    (L : ℕ) (h : Fin r) : ℝ :=
  classicalValue f (L - classicalQueriesTo τ h) (classicalTranscriptWeight μ τ h)
```

**Proof and correspondence.** The definition uses the actual transcript-restricted prior and `L - classicalQueriesTo τ h`; the counter counts repeated queries. Bounds for all allowed trees and an attaining tree prove that this is the maximum stated in the paper. Positive-mass conditioning is the intended probabilistic use. At zero mass the supplied zero convention is totalized and never claimed to be a conditional probability.

**Declarations used:** `QuarticQuery.Paper.classicalQueriesTo`, `QuarticQuery.Paper.classicalTranscriptValue_attained`, `QuarticQuery.Paper.classicalTranscriptValue_bounds_tree`, `QuarticQuery.exists_tree_budgetValue_le`, `QuarticQuery.treeSuccess_le_budgetValue`.

**Source:** preprint [P1], Section 4.1, pp. 11–12; Drucker [DP1], Lemmas 3.1–3.2 and the following product argument. The source declarations are in `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`.
<!-- /passage:classical-def-value-V -->

<!-- passage:classical-eq-16 -->
## `eq-16`

**Class:** `genuine_new_proof`. **Compilation:** unelaborated. **Difficulty:** medium.

If the next query is to instance $h$ and a query remains, then
\[
\mathbb E[V_h(\tau')\mid\tau]\le V_h(\tau).
\]
This is `eq-16`. For $j\ne h$, the transcript restriction and remaining budget of instance $j$ are unchanged. The exact finite two-branch form uses the mass of the restricted prior divided by the old mass.

**Lean statement (unelaborated).** The namespace is `QuarticQuery.Paper`; the file supplies the finite-type variables and definitions.

```lean
theorem classical_eq_16_transcript (f : PartialBool κ)
    {μ : Fin r → BitInput κ → ℝ} (hμ : ∀ j x, 0 ≤ μ j x)
    (τ : ClassicalTranscript r κ) (L : ℕ) (h : Fin r) (q : κ)
    (hc : classicalQueriesTo τ h < L) :
    classicalBranchProbability (classicalTranscriptWeight μ τ h) q false *
        classicalTranscriptValue f μ (τ ++ [((h, q), false)]) L h +
      classicalBranchProbability (classicalTranscriptWeight μ τ h) q true *
        classicalTranscriptValue f μ (τ ++ [((h, q), true)]) L h ≤
      classicalTranscriptValue f μ τ L h
```

**Proof and correspondence.** The exact two-answer conditional inequality is proved from the already compiled one-instance Bellman inequality. Zero branch mass is treated before any cancellation; the proof does not require the false assertion that every query outcome has positive mass. Transcript append and budget-count lemmas connect the local formula to the paper's τ and τ′. The unqueried-instance clause is a separate theorem.

**Declarations used:** `QuarticQuery.Paper.classical_branchValue`, `QuarticQuery.Paper.classical_eq_16`, `QuarticQuery.Paper.classical_transcriptWeight_append`, `QuarticQuery.Paper.classical_budget_append`, `QuarticQuery.Paper.classicalTranscriptValue_unchanged`, `QuarticQuery.Paper.classical_two_branch_expectation`, `QuarticQuery.budgetValue_add_le`.

**Source:** preprint [P1], Section 4.1, pp. 11–12; Drucker [DP1], Lemmas 3.1–3.2 and the following product argument. The source declarations are in `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`.
<!-- /passage:classical-eq-16 -->

<!-- passage:classical-claim-supermartingale -->
## `claim-supermartingale`

**Class:** `genuine_new_proof`. **Compilation:** unelaborated. **Difficulty:** high.

The product of conditional values satisfies
\[
\mathbb E\!\left[\prod_jV_j(\tau')\mid\tau\right]\le\prod_jV_j(\tau).
\]
This is `claim-supermartingale`. The separate caps imply at most $rL$ queries. Finite iteration and the terminal success bridge recover the deterministic endpoint of `lem-4.1`, then finite averaging handles independent side information and coins.

**Lean statement (unelaborated).** The namespace is `QuarticQuery.Paper`; the file supplies the finite-type variables and definitions.

```lean
theorem classical_transcript_conditional_expectation {β : Type}
    (T : OutTree (Fin r × κ) β) (f : PartialBool κ)
    {μ : Fin r → BitInput κ → ℝ} (hμ : ∀ j x, 0 ≤ μ j x)
    (τ : ClassicalTranscript r κ) (L : ℕ) (h : Fin r) (q : κ)
    (hm : 0 < ∑ V : Fin r → BitInput κ,
      if classicalPrefix T τ V then ∏ j, μ j (V j) else 0)
    (hc : classicalQueriesTo τ h < L) :
    (∑ U : Fin r → BitInput κ,
      ((if classicalPrefix T τ U then ∏ j, μ j (U j) else 0) /
        (∑ V : Fin r → BitInput κ,
          if classicalPrefix T τ V then ∏ j, μ j (V j) else 0)) *
        (∏ j, classicalTranscriptValue f μ (τ ++ [((h, q), U h q)]) L j)) ≤
      ∏ j, classicalTranscriptValue f μ τ L j
```

**Proof and correspondence.** The primary statement uses the normalized actual execution-prefix law explicitly and the product of classicalTranscriptValue at the extended transcript. Positive local masses are derived from nonnegative priors and positive actual transcript mass. The theorem holds for any query with remaining budget, so specializes to the actual next query. Finite iteration then bounds actual algorithm success using a separate normalized-success split. The code never calls guessSuccess_le_prod or the existing direct_product endpoint. No identification with Mathlib's measure-theoretic Supermartingale structure is asserted or needed for bounded finite trees.

**Declarations used:** `QuarticQuery.Paper.classical_product_conditional_expectation`, `QuarticQuery.Paper.classical_transcript_product_law`, `QuarticQuery.Paper.classical_transcript_mass_pos`, `QuarticQuery.Paper.classical_transcriptWeight_append`, `QuarticQuery.Paper.classical_budget_append`, `QuarticQuery.Paper.classical_product_step`, `QuarticQuery.Paper.classical_product_marginal`, `QuarticQuery.Paper.classical_terminalValue_le`, `QuarticQuery.Paper.classical_capped_depth_uniform`, `QuarticQuery.Paper.classical_guessSuccess_query`, `QuarticQuery.Paper.classical_success_le_terminal`, `QuarticQuery.Paper.classical_direct_product`.

**Source:** preprint [P1], Section 4.1, pp. 11–12; Drucker [DP1], Lemmas 3.1–3.2 and the following product argument. The source declarations are in `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`.
<!-- /passage:classical-claim-supermartingale -->

<!-- passage:classical-claim-final-bound -->
## `claim-final-bound`

**Class:** `genuine_new_proof`. **Compilation:** unelaborated. **Difficulty:** low.

At a terminal transcript, the chosen answer vector is fixed and
\[
\Pr[\text{chosen vector correct}\mid\tau]
\le\prod_h\max_{b\in\{0,1\}}\Pr[P(U_h)=b\mid\tau]
\le\prod_hV_h(\tau).
\]
This is `claim-final-bound`. The first inequality follows from the conditional product law and choosing the better constant output separately. The second follows because a constant-output tree is permitted under every remaining budget.

**Lean statement (unelaborated).** The namespace is `QuarticQuery.Paper`; the file supplies the finite-type variables and definitions.

```lean
theorem classical_final_bound (f : PartialBool κ)
    (ν : Fin r → BitInput κ → ℝ) (c : Fin r → ℕ)
    (hν : ∀ h x, 0 ≤ ν h x) (s : Fin r → Bool) :
    guessSuccess f (fun h => classicalLaw (ν h)) (.leaf s) ≤
        ∏ h, max (constSuccess f (classicalLaw (ν h)) false)
          (constSuccess f (classicalLaw (ν h)) true) ∧
      (∏ h, max (constSuccess f (classicalLaw (ν h)) false)
          (constSuccess f (classicalLaw (ν h)) true)) ≤
        classicalProductValue f ν c
```

**Proof and correspondence.** Both inequalities in the paper's terminal display are stated as a conjunction. A terminal transcript fixes the chosen vector; normalized transcript weights are substituted into the leaf theorem. The actual-execution bridge integrates this terminal bound through the true conditional split.

**Declarations used:** `QuarticQuery.guessSuccess_leaf`, `QuarticQuery.constSuccess_nonneg`, `QuarticQuery.Paper.classicalValue_bounds_tree`, `QuarticQuery.Paper.classical_success_le_terminal`.

**Source:** preprint [P1], Section 4.1, pp. 11–12; Drucker [DP1], Lemmas 3.1–3.2 and the following product argument. The source declarations are in `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`.
<!-- /passage:classical-claim-final-bound -->

<!-- passage:classical-eq-17 -->
## `eq-17`

**Class:** `already_stated_under_another_name`. **Compilation:** unelaborated. **Difficulty:** low.

For natural $m,L$,
\[
G=\left\lfloor\frac{mL}{100}\right\rfloor.
\]
This is the corrected canonical `eq-17`. Proposition 4.2 carries the independent assertion $R(F_{k,m})>G$. The adjudication accepted separating these two roles to avoid a circular dependency at the statement-record level.

**Lean statement (unelaborated).** The namespace is `QuarticQuery.Paper`; the file supplies the finite-type variables and definitions.

```lean
theorem classical_eq_17_floor (m L : ℕ) :
    Gvalue m L = ⌊(m : ℝ) * (L : ℝ) / 100⌋₊
```

**Proof and correspondence.** Canonical eq-17 was already corrected to the definition G = floor(mL/100), separate from the lower-bound assertion in Proposition 4.2. The supplied wrapper proves the real-floor presentation exactly; its Nat division version is rfl. No canonical statement change is proposed, and no prop-4.2 lower bound is smuggled into the definition.

**Declarations used:** `QuarticQuery.Gvalue`, `QuarticQuery.Paper.classical_eq_17`, `Nat.floor_div_eq_div`.

**Source:** preprint [P1], Section 4.2, p. 12, display (17); `repository/research/adjudication/adjudication.json`, finding `R1-AF-18`; `funnel_adjudication.json`, `pending_ties`. The corrected canonical row is preserved.
<!-- /passage:classical-eq-17 -->

<!-- passage:PL-def-dummy -->
## `def-dummy`

**Class:** `already_stated_under_another_name`. **Proposed route:** `same`. **Compiled:** no.

Let $m=2^\ell$. Draw all $A_{i,h}$ independently from a nonnegative normalized weight $\mu$, and draw all zero positions $J_i$ independently and uniformly from the $m$ rows. Apply `dummy J A`. This is the exact choice of the all-false blank pattern allowed in the preprint.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.dummyAvg`:

```lean
noncomputable def dummyAvg (μ : BitInput κ → ℝ)
    (g : BitInput (BitLoc ℓ r S κ) → ℝ) : ℝ
```

**Proof plan and agreement.** `dummyAvg` exposes both sampling stages that were absent from the old partial tie. `dummyAvg_const` and `dummyAvg_nonneg` establish normalization and positivity of this finite expectation functional. `dummyAvg_eq_coupledAvg` proves agreement with the expectation used by the supplied lower-bound proof, adding only its independent unused index $I$.

**Qualification or correction.** The source represents row and column labels by `Fin m`. The paper’s row $j\in\{1,\ldots,m\}$ corresponds to Lean’s `j-1`. There is no change to which physical bit is zero. `pointerEquiv` is the shared encoding bijection.

**Existing declarations used:** `QuarticQuery.dummy`, `QuarticQuery.avg`, `QuarticQuery.prodW`, `QuarticQuery.unif`, `QuarticQuery.sum_prodW`, `QuarticQuery.avg_resample`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-def-dummy -->

<!-- passage:PL-def-planted -->
## `def-planted`

**Class:** `already_stated_under_another_name`. **Proposed route:** `same`. **Compiled:** no.

Independently choose a uniform column $I$. In the dummy input set $X_I$ to all ones, and fill the cell at `trueAddr f (A I)` with the chosen consistent circuit transcripts and pointers to $J_j$ for every $j\ne I$.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.plantedAvg`:

```lean
noncomputable def plantedAvg (μ : BitInput κ → ℝ) (f : PartialBool κ)
    (tr : BitInput κ → Fin S → Bool) (g : BitInput (BitLoc ℓ r S κ) → ℝ) : ℝ
```

**Proof plan and agreement.** `plantedAvg` is exactly `coupledAvg` applied to the pre-existing planting map. `paperCoupledAvg_const`, `plantedAvg_const` and `plantedAvg_nonneg` establish the sampling-law properties. The ordinary assumptions that the address strings lie in the promise and the transcript chooser is consistent are used only for the winning-value theorem.

**Qualification or correction.** The address default `false` outside the promise carries no semantic assertion: the sampling law assigns such strings zero weight. The fixed blank pattern is all false.

**Existing declarations used:** `QuarticQuery.planted`, `QuarticQuery.trueAddr`, `QuarticQuery.coupledAvg`, `QuarticQuery.sum_unif`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-def-planted -->

<!-- passage:PL-claim-Y-values -->
## `claim-Y-values`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `same`. **Compiled:** no.

On every sample point in the support of the independent address distribution, $F(Y^{(0)})=0$ and $F(Y^{(1)})=1$.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.dummy_planted_values_on_support`:

```lean
theorem dummy_planted_values_on_support {f : PartialBool κ} {C : Circuit κ}
    {tr : BitInput κ → Fin C.size → Bool} (htr : ∀ x, GateConsistent C x (tr x))
    {μ : BitInput κ → ℝ} (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (J : Column ℓ → Column ℓ) (A : Column ℓ → Fin r → BitInput κ) (I : Column ℓ)
    (hA : prodW (prodW μ) A ≠ 0) :
    addressedF f C ℓ r (dummy J A) = false ∧
      addressedF f C ℓ r (planted f tr J A I) = true
```

**Proof plan and agreement.** Combine `addressedF_dummy` and `addressedF_planted`. For the latter, `ne_zero_of_prodW_ne_zero` first selects column $I$ and then instance $h$, giving $\mu(A_{I,h})\ne0$ and therefore the promised input required by the existing theorem. Specialize $f=P(k,t)$, $\ell=2t$, $r=40t$, and the same circuit $C$ used in `Fkm`.

**Qualification or correction.** The source type of $A$ includes all bit strings. Consequently the exact Lean statement must say “on the support”, or instead use a subtype of promised strings. A claim for every arbitrary ambient $A$ is false. This is the precise reading of the preprint’s sample points, whose $A$ strings are sampled from $\mu$ on the promise.

**Existing declarations used:** `QuarticQuery.addressedF_dummy`, `QuarticQuery.addressedF_planted`, `QuarticQuery.ne_zero_of_prodW_ne_zero`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-claim-Y-values -->

<!-- passage:PL-eq-18 -->
## `eq-18`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `same`. **Compiled:** no.

Write $V_I$ for the event that the dummy run queries any bit of its true-address cell, and $E_I$ for querying the removed zero. The ledger’s symmetric form is $|\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]|\le\Pr[E_I]+\Pr[V_I]$.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.eq_18`:

```lean
theorem eq_18 {μ : BitInput κ → ℝ} (hμ : ∀ x, 0 ≤ μ x)
    (f : PartialBool κ) (tr : BitInput κ → Fin S → Bool)
    (T : QueryTree (BitLoc ℓ r S κ)) :
    |plantedAvg μ f tr (fun x => ind (T.eval x = true)) -
        dummyAvg μ (fun x => ind (T.eval x = true))| ≤
      coupledAvg μ (fun A J I => foundZero T A J I) +
        coupledAvg μ (fun A J I => cellVisit f T J A I)
```

**Proof plan and agreement.** `output_gap_abs_le_unsplit` proves the bound pointwise. If the outputs differ, `QueryTree.exists_mem_path_ne` supplies a queried bit where the coupled inputs differ. `eq_of_dummy_ne_planted` places that bit in $E_I$ or $V_I$. An indicator difference has absolute value at most one. `paperCoupledAvg_abs_le` then averages both inequalities defining an absolute bound. This avoids any assumption about the direction of the output gap.

**Qualification or correction.** Adjudication `F-TREE-GAP` is decisive: the printed paper says ‘difference’ and does not print absolute-value bars in (18) or (23); `eq-18` in the ledger supplies the symmetric reading. This wrapper proves that symmetric form. The one-sided version was already sufficient for the lower-bound contradiction.

**Existing declarations used:** `QuarticQuery.QueryTree.exists_mem_path_ne`, `QuarticQuery.eq_of_dummy_ne_planted`, `QuarticQuery.ind_nonneg`, `QuarticQuery.ind_le_one`, `QuarticQuery.avg_mono`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-eq-18 -->

<!-- passage:PL-def-Z -->
## `def-Z`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `same`. **Compiled:** no.

$Z$ is the number of columns for which the complete dummy run queries that column’s hidden zero. A column discovered more than once still contributes one.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.discoveredZeros`:

```lean
noncomputable def discoveredZeros (T : QueryTree (BitLoc ℓ r S κ))
    (A : Column ℓ → Fin r → BitInput κ) (J : Column ℓ → Column ℓ) : ℕ
```

**Proof plan and agreement.** `discoveredZeros` is a `Finset.card`, and `discoveredZeros_cast` proves agreement with the sum of the source’s `foundZero` indicators. `erasedZero_eq_expectedZeros_div` then proves the exact identity $\Pr[E_I]=\mathbb E Z/m$ by the independent uniform choice of $I$.

**Qualification or correction.** This is a natural-number count, converted to a real only for expectations. `QueryTree.path` includes repeated queries; the cardinality definition counts distinct discovered columns correctly.

**Existing declarations used:** `QuarticQuery.QueryTree.path`, `QuarticQuery.foundZero`, `Finset.card_filter`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-def-Z -->

<!-- passage:PL-claim-uniform-zero -->
## `claim-uniform-zero`

**Class:** `genuine_new_proof`. **Proposed route:** `same`. **Compiled:** no.

For a transcript $\tau$, let $U_i(\tau)$ be the positions in column $i$ absent from its query list. If $\tau$ has positive probability and no zero in column $i$ has appeared, then $\Pr[J_i=p\mid\tau]=1/|U_i(\tau)|$ for $p\in U_i(\tau)$, and it is zero otherwise.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalUniformZero.lean`, declaration `QuarticQuery.Paper.uniform_zero_given_transcript`:

```lean
theorem uniform_zero_given_transcript (μ : BitInput κ → ℝ)
    (_hμ : ∀ x, 0 ≤ μ x) (_hμ1 : ∑ x, μ x = 1)
    (T : QueryTree (BitLoc ℓ r S κ)) (τ : List (BitLoc ℓ r S κ × Bool))
    (i p : Column ℓ) (hτ : NoZeroSeen i τ) (hpos : 0 < dummyTraceMass μ T τ) :
    dummyTraceZeroMass μ T τ i p / dummyTraceMass μ T τ =
      if p ∈ unqueriedRows i τ then 1 / ((unqueriedRows i τ).card : ℝ) else 0
```

**Proof plan and agreement.** The new file `ClassicalUniformZero.lean` defines the concrete prefix event from the actual decision tree’s query/answer schedule. `observedPrefix_query_cons` exposes its adaptive next-step semantics. `observedPrefix_dummy_fiber` proves that, for any fixed outside variables, a possible zero position produces the recorded prefix exactly when it lies in the unqueried set and the all-one reference produces that prefix. Resample $J_i$ using `avg_resample`; `dummyTraceMass_factor` and `dummyTraceZeroMass_factor` compute the two finite likelihoods. Divide them only after assuming the transcript probability is positive.

**Qualification or correction.** The theorem includes all $A$ strings and all other zero positions in the averaged sample space. It does not assume posterior independence or uniformity. `NoZeroSeen` asks that every recorded answer from $X_i$ is true. Illegal schedules and inconsistent answer lists have zero probability, so the positive-probability premise excludes them. This is the main new proof in this subsection.

**Existing declarations used:** `QuarticQuery.dummy`, `QuarticQuery.avg_resample`, `QuarticQuery.avg_unif`, `QuarticQuery.avg_mul_left`, `QuarticQuery.QueryTree`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-claim-uniform-zero -->

<!-- passage:PL-claim-EZ -->
## `claim-EZ`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `alternative`. **Compiled:** no. **Whole-row relation:** partial.

The requested endpoint is $\mathbb E Z\le4G/m$. The new source first derives the stronger inequality $\mathbb E Z\le2G/m$ and then weakens its coefficient.

**The paper's early/late calculation.** Call a discovery early if fewer than $m/2$ distinct positions in that column were queried before its zero was found. At a positive-probability prefix with no zero seen in that column, the preceding uniformity claim gives probability $1/(m-d)$ for a new queried position, where $d$ positions have already been ruled out. During an early discovery $d<m/2$, so this probability is at most $2/m$. A repeated query or a query outside a column contributes no new discovery. Sum these conditional probabilities over at most $G$ query times, padding a stopped run by zero contributions.

Every remaining discovered column has received at least $m/2$ queries. Since the total query count is at most $G$, there are at most $2G/m$ such columns on each run. Writing $Z_{\rm early}$ and $Z_{\rm late}$ for the two parts of the count gives the clauses of `claim-EZ`:

\[
\mathbb E Z_{\rm early}\leq 2G/m,\qquad
Z_{\rm late}\leq 2G/m,\qquad
\mathbb E Z=\mathbb E Z_{\rm early}+\mathbb E Z_{\rm late}\leq4G/m.
\]

This reconstructs the mathematical argument. The submitted Lean endpoint below uses the alternative search induction; it does not formalize these early/late variables or their expectation partition.


**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.expectedZeros_le_four`:

```lean
theorem expectedZeros_le_four {μ : BitInput κ → ℝ} (hμ : ∀ x, 0 ≤ μ x)
    (hμ1 : ∑ x, μ x = 1) {G : ℕ}
    (T : QueryTree (BitLoc ℓ r S κ)) (hT : T.depth ≤ G) :
    expectedZeros μ T ≤ 4 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ)
```

**Proof plan and agreement.** `erasedZero_le_two` averages `avg_foundZero_I_le` over $A$. Combine it with the new identity `erasedZero_eq_expectedZeros_div` and $m>0$, then multiply by $m$. `expectedZeros_le_four` gives the printed constant, and `eq_19` also states the full removed-zero probability $\Pr[E_I]\le4G/m^2$.

**Qualification or correction.** The compound ledger row also describes the paper’s early/late decomposition, including the early-discovery expectation and the late-column count. Those intermediate random variables and their expectation partition are not supplied here. Thus the endpoint is exact by an alternative route, while the whole compound row retains partial coverage. The stronger endpoint is separately registered as `new-r2-EZ-two`. Adjudication removes the unqualified claim that coefficient two is tight under a worst-case depth cap; no such optimality assertion is made.

**Existing declarations used:** `QuarticQuery.avg_foundZero_I_le`, `QuarticQuery.avg_le_const`, `QuarticQuery.avg_unif`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-claim-EZ -->

<!-- passage:PL-def-heavy -->
## `def-heavy`

**Class:** `already_stated_under_another_name`. **Proposed route:** `same`. **Compiled:** no.

Column $i$ is heavy exactly when the complete dummy run makes more than $L$ queries in total to its strings $A_{i,1},\ldots,A_{i,r}$, with repeated queries counted.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.HeavyColumn`:

```lean
def HeavyColumn (L : ℕ) (T : QueryTree (BitLoc ℓ r S κ))
    (A : Column ℓ → Fin r → BitInput κ) (J : Column ℓ → Column ℓ) (i : Column ℓ) : Prop
```

**Proof plan and agreement.** `HeavyColumn` names the existing predicate `L < aQueries i (T.path (dummy J A))`. `heavyColumn_iff` proves definitional agreement. The threshold is strict: a run with exactly $L$ target queries is nonheavy.

**Qualification or correction.** This is a definition, not a new probabilistic theorem. Heaviness depends on the whole run, which is why it must remain inside the joint event in (21).

**Existing declarations used:** `QuarticQuery.aQueries`, `QuarticQuery.aTarget`, `QuarticQuery.QueryTree.path`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-def-heavy -->

<!-- passage:PL-def-simulator -->
## `def-simulator`

**Class:** `already_stated_under_another_name`. **Proposed route:** `same`. **Compiled:** no.

Fix column $i$ and a proposed query time. The simulator supplies the non-target dummy bits from independent side information, queries the target strings only when the original algorithm does, and aborts before spending more than $L$ total target queries. At the proposed query it outputs a cell address if available, otherwise a fixed vector.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.addressSimulator`:

```lean
def addressSimulator (L t : ℕ) (T : QueryTree (BitLoc ℓ r S κ))
    (J : Column ℓ → Column ℓ) (A : Column ℓ → Fin r → BitInput κ) (i : Column ℓ) :
    OutTree (Fin r × κ) (Address r)
```

**Proof plan and agreement.** `addressSimulator` specializes `simTree` with `aTarget i`, `cellGuess i`, the all-false default vector and `dummy J A`. `addressSimulator_depth_le` follows directly from `depth_simTree_le`. The simulator’s bound is a total cap on the target strings, so `OutTree.capped_of_depth_le` supplies the per-instance cap required by the direct product.

**Qualification or correction.** Lean time `t` is the paper’s proposed query `t+1`. At `t=0` the simulator inspects the proposed first location without answering that query; this is correct because it only guesses the address of the cell that would be queried.

**Existing declarations used:** `QuarticQuery.simTree`, `QuarticQuery.aTarget`, `QuarticQuery.cellGuess`, `QuarticQuery.depth_simTree_le`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-def-simulator -->

<!-- passage:PL-eq-21 -->
## `eq-21`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `same`. **Compiled:** no.

For every fixed column and every proposed query time, the joint probability of nonheaviness and querying that column’s true-address cell is at most $(2/3)^r$.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.eq_21`:

```lean
theorem eq_21 {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : ∑ x, μ x = 1)
    (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (hard : ∀ U : QueryTree κ, U.depth ≤ L → treeSuccess f μ U ≤ 2 / 3)
    (T : QueryTree (BitLoc ℓ r S κ)) (i : Column ℓ) (t : ℕ) :
    avg (prodW (prodW μ)) (fun A => avg (prodW (unif ℓ)) fun J =>
      reachedCellAt f L T J A i t) ≤ ((2 : ℝ) / 3) ^ r
```

**Proof plan and agreement.** `reachedCellAt` defines the event with `List.getElem?`; a stopped run cannot satisfy it. `avg_reachedCellAt_le` extracts the per-time implication already used internally by the existing union-bound proof: on a positive-weight sample satisfying the event, `eval_simTree` returns the true address and the simulator is capped. `eq_21` uses `address_guess_le` and then `avg_resample` to average the original target law with its independent outside variables. There is no factor of $m$ or $G$ in this per-time estimate. The imported `address_guess_le` still uses the packet’s alternative direct-product proof; this wrapper checks the paper’s simulator step without claiming that imported proof follows the paper’s value-process derivation.

**Qualification or correction.** The theorem bounds a joint event under the original product law. Dividing by the probability of nonheaviness would change the assertion and is unsupported. The exported statement is even available for all natural times; restricting to the paper’s first $G$ proposed queries is immediate.

**Existing declarations used:** `QuarticQuery.eval_simTree`, `QuarticQuery.OutTree.capped_of_depth_le`, `QuarticQuery.address_guess_le`, `QuarticQuery.avg_resample`, `QuarticQuery.dummy_update_of_aTarget_none`, `QuarticQuery.dummy_update_of_aTarget_some`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-eq-21 -->

<!-- passage:PL-eq-22 -->
## `eq-22`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `same`. **Compiled:** no.

The full true-address cell event satisfies $\Pr[V_I]\le G/(mL)+G(2/3)^r$, with $L\ge1$ and a worst-case depth cap $G$.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.eq_22`:

```lean
theorem eq_22 {f : PartialBool κ} {μ : BitInput κ → ℝ} {L G : ℕ}
    (hL : 1 ≤ L) (hμ : ∀ x, 0 ≤ μ x) (hμ1 : ∑ x, μ x = 1)
    (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (hard : ∀ U : QueryTree κ, U.depth ≤ L → treeSuccess f μ U ≤ 2 / 3)
    (T : QueryTree (BitLoc ℓ r S κ)) (hT : T.depth ≤ G) :
    coupledAvg μ (fun A J I => cellVisit f T J A I) ≤
      (G : ℝ) / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) + (G : ℝ) * ((2 : ℝ) / 3) ^ r
```

**Proof plan and agreement.** `cellVisit_le_heavy_add_reached` is the pointwise union bound. `avg_heavy_le` handles the heavy term. The compiled-source theorem `avg_reachedCell_le` bounds the nonheavy union over times by $G\rho$. Resampling and averaging restore the full original law; `address_guess_le` sets $\rho=(2/3)^r$. The intermediate generic wrapper is `cellVisit_le`.

**Qualification or correction.** Uniformly averaging the chosen column introduces no factor of $m$. All support, normalization, query-cap, and hardness hypotheses are explicit. The source’s existing `avg_reachedCell_le` alone was only the nonheavy part, which is why the earlier tie was partial.

**Existing declarations used:** `QuarticQuery.avg_reachedCell_le`, `QuarticQuery.avg_heavy_le`, `QuarticQuery.avg_resample`, `QuarticQuery.address_guess_le`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-eq-22 -->

<!-- passage:PL-eq-23 -->
## `eq-23`

**Class:** `few_lines_from_existing_declarations`. **Proposed route:** `alternative`. **Compiled:** no.

The absolute output-one gap is at most $4G/m^2+G/(mL)+G(2/3)^r$. The new file also states the stronger first coefficient two and the same coefficient-four bound for randomized programs.

**Lean statement (unelaborated).** In `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, declaration `QuarticQuery.Paper.eq_23`:

```lean
theorem eq_23 {f : PartialBool κ} {μ : BitInput κ → ℝ} {L G : ℕ}
    (tr : BitInput κ → Fin S → Bool) (hL : 1 ≤ L)
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : ∑ x, μ x = 1)
    (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (hard : ∀ U : QueryTree κ, U.depth ≤ L → treeSuccess f μ U ≤ 2 / 3)
    (T : QueryTree (BitLoc ℓ r S κ)) (hT : T.depth ≤ G) :
    |plantedAvg μ f tr (fun x => ind (T.eval x = true)) -
        dummyAvg μ (fun x => ind (T.eval x = true))| ≤
      4 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 +
        (G : ℝ) / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) + (G : ℝ) * ((2 : ℝ) / 3) ^ r
```

**Proof plan and agreement.** `eq_23_two` combines exact `eq_18`, `erasedZero_le_two` and `eq_22`. `eq_23` weakens only the first coefficient. `eq_23_randomized` applies the deterministic bound to every tree in the positive finite mixture, uses its worst-case depth bound, commutes finite averages, and identifies the mixture of indicator outputs with `RandomizedProgram.success`. Its statement is about the actual program output probabilities.

**Qualification or correction.** This closes the symmetric-packaging gap without weakening a statement to match a one-sided source theorem. The two-sided conclusion is stronger than the direction used by `addressedF_not_RLe`. Its zero-search route remains alternative to the paper’s early/late argument. No new lower-bound exponent is inferred from the improved coefficient.

**Existing declarations used:** `QuarticQuery.avg_foundZero_I_le`, `QuarticQuery.avg_reachedCell_le`, `QuarticQuery.avg_heavy_le`, `QuarticQuery.address_guess_le`, `QuarticQuery.RandomizedProgram.success`. The relevant paper locator is the row’s `source_line` in `corpus/statements.json`; full reviewed tie metadata was consulted, including rows with no old tie.
<!-- /passage:PL-eq-23 -->

<!-- passage:r2-classical-tail -->
## `claim-tail`: the exact logarithmic exponent

**Class:** genuine new proof of the missing exact form. The existing `QuarticQuery.twoThirds_pow_le` remains useful for the finite numerical estimate. Its exponent is weaker than the preprint's exponent, and it does not state the factor $G$ or the zero limit. The adjudication `F-CLAIM-TAIL` explicitly rejects replacing the original row with the weaker exponent. No correction of the preprint is needed.

The preprint states, for its choices $m=4^t$, $r=40t$, $1\leq L\leq m$, and $G\leq mL/100$,

\[
G(2/3)^r\leq \frac1{100}m^{2-20\log_2(3/2)}=o(1).
\]

The first step is an identity:

\[
(2/3)^{40t}=m^{-20\log_2(3/2)}.
\]

Multiplication by $G\leq m^2/100$ gives the displayed upper bound. The exponent is negative because $(3/2)^2>2$, so $2\log_2(3/2)>1$. The submitted source also gives the exact geometric expression

\[
m^{2-20\log_2(3/2)}=\bigl(16(2/3)^{40}\bigr)^t,
\]

whose base is strictly between zero and one. This proves the limit without weakening the exponent. Numerically, the exponent is approximately $-9.6992500144$; this numerical value is only explanatory.

**Lean statements, unelaborated:** `classical_twoThirds_exact` states the identity, `classical_tail_le` states the exact finite inequality, and `classical_tail_envelope_tendsto` states the zero limit of the displayed upper envelope. The principal actual-parameter wrapper is:

```lean
theorem QuarticQuery.Paper.classical_tail_parameters (k : ℕ) (hk : 1 ≤ k) :
    (∀ t : ℕ,
      (Gvalue (mValue t) (Lvalue k t) : ℝ) * ((2 : ℝ) / 3) ^ (40 * t) ≤
        (1 / 100 : ℝ) *
          (mValue t : ℝ) ^ (2 - 20 * Real.logb 2 ((3 : ℝ) / 2))) ∧
    Tendsto (fun t : ℕ =>
      (Gvalue (mValue t) (Lvalue k t) : ℝ) * ((2 : ℝ) / 3) ^ (40 * t))
      atTop (nhds 0)
```

The displayed signature is unelaborated; the module supplies `open Filter` and the surrounding namespace for unqualified vocabulary.

**Proof dependencies:** `mValue_cast`; the definitions `mValue`, `Lvalue`, and `Gvalue`; `Lvalue_le_mValue`; `Nat.cast_div_le`; `Real.rpow_def_of_pos`; `Real.log_inv`; `Real.log_pow`; `Real.logb`; `Real.rpow_add`; `Real.rpow_two`; `Real.logb_lt_logb`; `Real.logb_pow`; `tendsto_pow_atTop_nhds_zero_of_lt_one`; and `squeeze_zero`. The actual-budget wrapper treats $t=0$ separately, where Lean's total division gives $L=G=0$. For $t\geq1$, the existing bound $L\leq m$ proves $G\leq m^2/100$.

**Source locations:** `paper/extracted.md:670–674`; `repository/corpus/statements.json`, row `claim-tail`; `repository/corpus/ties.json`, same row; `repository/lean/QuarticQuery/Results/Exponent.lean:429–440`; `repository/research/adjudication/funnel_adjudication.json`, finding `F-CLAIM-TAIL`; and `previous_round/1_long_reasoning_record/LEAN_GAPS.md`, “Discrepancy, arithmetic, and quantifiers.” The new exact statements preserve the original row unchanged.
<!-- /passage:r2-classical-tail -->

<!-- passage:r2-classical-numeric -->
## `claim-numeric`: expose the three component inequalities

**Class:** a short extraction from an existing proof. `QuarticQuery.discrepancy_le` already proves the three component estimates in its local declarations `h1`, `h2`, and `h3`; its exported conclusion only states their sum. The submitted theorem exports all three estimates together with the sum and the strict comparison of constants.

For every $t\geq0$, put $m=4^t$, and suppose $1\leq L\leq m$ and $G\leq mL/100$. Then

\[
\frac{4G}{m^2}\leq\frac4{100},\qquad
\frac{G}{mL}\leq\frac1{100},\qquad
G(2/3)^{40t}\leq\frac1{100},
\]

and their sum is at most $6/100<1/3$. These are the corrected statement record's exact clauses. The first two inequalities follow by division by positive quantities. For the last, the existing `twoThirds_pow_le` gives $(2/3)^{40t}\leq m^{-10}$, while $G\leq m^2/100$ and $m^2\leq m^{10}$. The exact logarithmic tail is unnecessary for this finite estimate.

**Lean statement, unelaborated:**

```lean
theorem QuarticQuery.Paper.classical_numeric_components {t : ℕ} {L G : ℝ}
    (hL1 : 1 ≤ L) (hLm : L ≤ (mValue t : ℝ))
    (hG : G ≤ (mValue t : ℝ) * L / 100) :
    4 * G / (mValue t : ℝ) ^ 2 ≤ 4 / 100 ∧
    G / ((mValue t : ℝ) * L) ≤ 1 / 100 ∧
    G * ((2 : ℝ) / 3) ^ (40 * t) ≤ 1 / 100 ∧
    4 * G / (mValue t : ℝ) ^ 2 + G / ((mValue t : ℝ) * L) +
      G * ((2 : ℝ) / 3) ^ (40 * t) ≤ 6 / 100 ∧
    (6 / 100 : ℝ) < 1 / 3
```

**Proof dependencies:** the proof is the component calculation in `QuarticQuery.discrepancy_le`, with `QuarticQuery.twoThirds_pow_le`, `pow_le_pow_right₀`, order-preserving multiplication, and field arithmetic. No new probabilistic assumption is added. The statement does not need $G\geq0$; nonnegativity holds automatically at the actual natural-number budget.

**Source locations:** `paper/extracted.md:666–676`; `repository/lean/QuarticQuery/Results/Exponent.lean:443–488`; the `claim-numeric` entries in `statements.json`, `ties.json`, and the first adjudication. The source proof already proves the numerical content, so this task changes its exported statement, with no change to the original row.
<!-- /passage:r2-classical-numeric -->

<!-- passage:r2-classical-omega -->
## `cor-R-omega`: close the eventual quantifiers

**Class:** already stated by the uncompiled candidate `QuarticQuery.Paper.cor_R_omega_log2`, with a short proof from existing declarations. The proposed replacement has the same mathematical statement and uses only the imported lower-bound modules. It does not import the uncompiled `Paper.Section4`.

For each fixed integer $k\geq2$, there is a threshold $t_0(k)$ such that every $t\geq t_0(k)$ and every circuit $C$ realizing $P_{k,4^t}$ satisfy

\[
R(F_{k,4^t,C})\geq
\frac1{400}\frac{(4^t)^{2-1/k}}{(\log_2(4^t))^2}.
\]

This is the preprint's Omega claim with an explicit constant. The threshold still depends on $k$. Its independence from the choice of realizing circuit is preserved. Natural logarithms replace $1/400$ by $(\log 2)^2/400$.

**Lean statement, unelaborated:**

```lean
theorem QuarticQuery.Paper.classical_cor_R_omega_log2 (k : ℕ) (hk : 2 ≤ k) :
    ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t → ∀ C : Circuit (ForrelationCoord k t),
      CircuitRealises C (P k t) →
        (1 / 400 : ℝ) * (mValue t : ℝ) ^ (2 - 1 / (k : ℝ)) /
          Real.logb 2 (mValue t : ℝ) ^ 2 ≤
            (R (totalise (Fkm k t C)) : ℝ)
```

**Proof plan and agreement:** `ForrelationLower.bansalSinhaLower k hk` supplies a threshold for $L<R(P)$. Enlarge it to at least eight and apply `Gvalue_lt_R_Fkm` to the same realizing circuit. `rpow_le_of_Gvalue_lt` removes the floors with constant $1/400$. Finally `logb_mValue` and `mValue_cast` put the result in the paper's notation. This is precisely the type of the candidate `cor_R_omega_log2`, with an equivalent threshold construction. The natural-log variant `classical_cor_R_omega_log` is an algebraic conversion from this theorem.

**Source locations:** `paper/extracted.md:682–686`; `repository/lean/QuarticQuery/Paper/Section4.lean:35–80`; `repository/lean/QuarticQuery/LowerBound/Planted/Main.lean:203–210`; `repository/lean/QuarticQuery/Results/Exponent.lean:365–413`; and `repository/lean/QuarticQuery/ForrelationLower/Main.lean`, declaration `bansalSinhaLower`. The actual-parameter and constant strengthening is registered separately, and the original row remains unchanged.
<!-- /passage:r2-classical-omega -->

<!-- passage:r2-classical-ratio -->
## `claim-exponent-ratio`: state the quotient and its lower envelope

**Class:** genuine new proof of an omitted finite inequality, followed by a short consequence of the existing asymptotic proof. `eventually_gt_rpow` already gives every eventual comparison $R>D(1+Q)^\alpha$; the record correctly marks that as partial because it does not state the displayed lower envelope.

Here is the finite calculation. Suppose $m\geq1$, $W\geq1$, $c,C\geq0$, $\alpha\geq0$, $b\in\mathbb N$, $q\geq0$, and

\[
q\leq C m^{1/2}W^b,\qquad r\geq c m^s/W^2.
\]

Since $m^{1/2}W^b\geq1$, the local `hbase` step in `classical_ratio_arithmetic` gives $1+q\leq(1+C)m^{1/2}W^b$.

Raising this inequality to $\alpha$ and using positivity of the denominators gives

\[
\frac{r}{(1+q)^\alpha}\geq
\frac{c}{(1+C)^\alpha}
\frac{m^{s-\alpha/2}}{W^{2+\alpha b}}.
\]

`classical_ratio_arithmetic` states this complete finite implication. It permits every real $s$; the inequality itself does not need the positive exponent needed for divergence. `classical_power_log_tendsto` states that for every fixed $d>0$, $\delta>0$, and real $e$,

\[
\frac{d(4^t)^\delta}{(\log_2(4^t))^e}\longrightarrow+\infty.
\]

Its proof uses the existing `eventually_poly_lt_exp`, with $2\delta>0$. It does not assume a theorem that the intended lower envelope diverges.

For the actual canonical family set $k=l+1\geq2$, $C_k=\texttt{Upper.budgetConst}(k)$, $c=1/400$, $b_k=6$, and

\[
d_{k,\alpha}=\frac1{400(1+C_k)^\alpha}>0.
\]

For each fixed $\alpha\geq0$ with $2-1/k>\alpha/2$, the submitted `classical_Fkm_ratio` states that eventually

\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\geq d_{k,\alpha}
\frac{m^{2-1/k-\alpha/2}}{(\log_2 m)^{2+6\alpha}},
\]

and states both divergence of the right-hand side and divergence of the ratio. Its $F_{k,m}$ uses `Forrelation.forrCircuit l t` in both complexities. The parameterization $k=l+1\geq2$ covers precisely the required integers, while avoiding a dependent-type cast of the circuit. The exact Lean statement is below. It is unelaborated; `classical_exponent_ratio` supplies its abstract-sequence form.

```lean
namespace QuarticQuery.Paper
open Filter
theorem classical_Fkm_ratio (l : ℕ) (hk : 2 ≤ l + 1) {α : ℝ}
    (hα : 0 ≤ α) (hs : α / 2 < 2 - 1 / ((l + 1 : ℕ) : ℝ)) :
    ∃ d : ℝ, 0 < d ∧
      (∀ᶠ t : ℕ in atTop,
        d * (mValue t : ℝ) ^ (2 - 1 / ((l + 1 : ℕ) : ℝ) - α / 2) /
          Real.logb 2 (mValue t : ℝ) ^ (2 + α * 6) ≤
            (R (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ) /
              (1 + (Q (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ)) ^ α) ∧
      Tendsto (fun t : ℕ =>
        d * (mValue t : ℝ) ^ (2 - 1 / ((l + 1 : ℕ) : ℝ) - α / 2) /
          Real.logb 2 (mValue t : ℝ) ^ (2 + α * 6)) atTop atTop ∧
      Tendsto (fun t : ℕ =>
        (R (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ) /
          (1 + (Q (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ)) ^ α)
        atTop atTop
end QuarticQuery.Paper
```

**Proof dependencies:** `Upper.Q_Fkm_le`, `Upper.budgetConst_pos`, `Forrelation.forrCircuit_realises`, `classical_cor_R_omega_log2`, `Real.rpow_le_rpow`, `Real.mul_rpow`, `Real.rpow_mul`, `Real.rpow_sub`, `Real.rpow_add`, `eventually_poly_lt_exp`, `eventually_gt_rpow`, and `Filter.tendsto_atTop_atTop`. The last function only converts a family of eventual numerical lower bounds into the formal limit statement. Choosing $k$ for a given $\alpha<4$ is still the existing `exists_nat_exponent`; $k$ remains fixed during the limit.

**Source locations:** `paper/extracted.md:695–713`; `repository/lean/QuarticQuery/Results/Exponent.lean:23–169`; `repository/lean/QuarticQuery/Upper/Bound.lean:244–271`; the `claim-exponent-ratio` entries of `statements.json` and `ties.json`; and the first round's `LEAN_GAPS.md` discussion of the literal ratio. There is no change to the original row's exponent or quantifier order.
<!-- /passage:r2-classical-ratio -->

## Sources and verification

[sources.md](sources.md) gives the immutable source location, exact literature locators, citation roles, and the receipt limitation. [NEW_STATEMENTS.json](NEW_STATEMENTS.json) registers the auxiliary statements. [STATEMENT_CHANGES.json](STATEMENT_CHANGES.json) is empty: no change to a canonical statement is proposed. [correspondence.json](correspondence.json) binds each anchored passage to its statement identifiers and source declarations. [validation.json](validation.json) records only the checks actually performed.
