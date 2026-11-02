# Sections 1 and 2: mathematical statements and Lean proof drafts

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

The principal results below are explicit conjunctions for Lemmas 2.1 and 2.2. They retain the fixed parameter k, the family m=4^t, exact promise recognition, worst-case query bounds and coherent evaluation. The total-function statement uses one specified Forrelation circuit family.

**Evidence status.** Every new Lean file and every Lean signature below is **unelaborated**. No Lean or Lake executable and no packaged compiled dependency cache were available. This report provides proof text and a statement comparison by source inspection. It provides no new kernel, Comparator or dependency-closure receipt. `compiled` is false throughout.

The preprint and its construction are OpenAI’s. All source locations below are relative to the attached input ZIP. Public references and exact literature locators appear in `REFERENCES.md`. The original records remain unchanged; supplemental quantitative or intermediate statements appear in `NEW_STATEMENTS.json`.

The blueprint follows the requested order of value. The code uses `namespace QuarticQuery.Paper`; the imports and `open` declarations in each referenced module supply the context of the displayed signatures. Full source files contain the proof terms. A declaration name below denotes proposed evidence until elaboration succeeds.

## Lemmas, corollaries, displays and definitions

### `lem-2.1`

<!-- passage:row-lem-2-1 -->

**Class:** Short assembly of existing declarations.

**Mathematics (`lem-2.1`).** For every fixed k≥2 and m=4^t: (i) for all sufficiently large t, R(P_{k,m})>L_{k,m}; (ii) for every 0<η<1/2 the coherent, total-output algorithm of Lemma 2.1(ii) uses O_k(1+log(1/η)) physical bit queries with promised error at most η; (iii) for every t≥1 an exact two-output circuit recognizes the promise and gives its value using at most S_k m(log_2 m)^2 gates, with S_k depending only on k.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean`](lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean), declaration `QuarticQuery.Paper.construction_lemma_2_1_complete`.

```lean
theorem construction_lemma_2_1_complete (k : ℕ) (hk : 2 ≤ k) :
    (∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t → Lvalue k t < R (P k t)) ∧
    (∃ A : ℝ, 0 < A ∧ ∀ (t : ℕ) (η : ℝ), 0 < η → η < 1 / 2 →
      ∃ (n : ℕ) (L : BitInput (ForrelationCoord k t) → Bool → ℝ)
        (Z : Type) (instZ : Fintype Z),
        let _ := instZ
        ∃ (o : Z) (out : Z → Bool)
          (F : BitInput (ForrelationCoord k t) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          ((2 * (n * k) : ℕ) : ℝ) ≤ A * (1 + Real.log (1 / η)) ∧
          IsCirc (n * k) F ∧
          (∀ z b, L z b = lawOf (F z (rket o)) out b) ∧
          (∀ z, 0 ≤ L z false ∧ 0 ≤ L z true ∧ L z false + L z true = 1) ∧
          (∀ z b, P k t z = some b → 1 - η ≤ L z b) ∧
          ∃ instI : Inhabited (ForrelationCoord k t),
            let _ := instI
            ∃ (w : ℕ) (emb : Z ↪ Fin (w + 1))
              (K : AdaptiveProgram (ForrelationCoord k t) w →
                AdaptiveProgram (ForrelationCoord k t) w),
              ∀ next, (K next).queryCap ≤ 2 * (n * k) + next.queryCap ∧
                ∀ z ψ b, (K next).outputMass z (clEmb emb ψ) b =
                  next.outputMass z (clEmb emb (F z ψ)) b) ∧
    (∃ S : ℕ, 0 < S ∧ ∀ t : ℕ, 1 ≤ t → ∃ C : Circuit (ForrelationCoord k t),
      CircuitRealises C (P k t) ∧
      (C.size : ℝ) ≤ (S : ℝ) * (mValue t : ℝ) *
        (Real.logb 2 (mValue t : ℝ)) ^ 2)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_lemma_2_1_i`
- `QuarticQuery.Paper.construction_lemma_2_1_ii`
- `QuarticQuery.Paper.construction_lemma_2_1_iii`
- `QuarticQuery.Paper.construction_lemma_2_1`
- `QuarticQuery.Paper.construction_lemma_2_1_ii_complete`

**Proof.**

Combine the fixed-k lower bound, the complete same-witness coherent physical implementation, and the exact circuit conclusion. The literal second conjunct includes the finite logical isometry F and output map out, their common accurate law, the physical workspace and embedding, and the compile_circ continuation equation for that same F on every embedded state. Its cap is bounded by a constant depending only on k times 1+ln(1/eta). Part (i) remains the explicitly different repository proof route. No published quantitative bound is imported as an axiom.

**Named dependencies.** `QuarticQuery.ForrelationLower.bansalSinhaLower`; `QuarticQuery.Paper.construction_lemma_2_1_i`; `QuarticQuery.Paper.construction_lemma_2_1_ii_complete`; `QuarticQuery.Paper.construction_lemma_2_1_iii`.

**Proof route.** different for part i same for parts ii and iii.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:151 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=unassessed`, `formal_origin=ours`, `build=not_run`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=outside`. These labels do not describe the new source proofs.

**Scope.** All three conclusions are literal in construction_lemma_2_1_complete, including the physical retained-workspace statement. The older construction_lemma_2_1 remains an explicitly partial helper because its sampler and Runs witnesses share only the output law. New source is unelaborated; no compiled or comparator status is asserted.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-lem-2-1 -->

### `lem-2.1.ii`

<!-- passage:row-lem-2-1-ii -->

**Class:** Short assembly of existing declarations.

**Mathematics (`lem-2.1.ii`).** For each fixed k≥2 there is A_k>0, independent of t and η, such that for every m=4^t and 0<η<1/2 a coherent algorithm rηins its workspace, outputs a Boolean value on every input, uses at most A_k(1+ln(1/η)) physical bit queries on every branch, and outputs P_{k,m}(z) with probability at least 1-η on every promised input.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean`](lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean), declaration `QuarticQuery.Paper.construction_lemma_2_1_ii_complete`.

```lean
theorem construction_lemma_2_1_ii_complete (k : ℕ) (hk : 1 ≤ k) :
    ∃ A : ℝ, 0 < A ∧ ∀ (t : ℕ) (η : ℝ), 0 < η → η < 1 / 2 →
      ∃ (n : ℕ) (L : BitInput (ForrelationCoord k t) → Bool → ℝ)
        (Z : Type) (instZ : Fintype Z),
        let _ := instZ
        ∃ (o : Z) (out : Z → Bool)
          (F : BitInput (ForrelationCoord k t) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          ((2 * (n * k) : ℕ) : ℝ) ≤ A * (1 + Real.log (1 / η)) ∧
          IsCirc (n * k) F ∧
          (∀ z b, L z b = lawOf (F z (rket o)) out b) ∧
          (∀ z, 0 ≤ L z false ∧ 0 ≤ L z true ∧ L z false + L z true = 1) ∧
          (∀ z b, P k t z = some b → 1 - η ≤ L z b) ∧
          ∃ instI : Inhabited (ForrelationCoord k t),
            let _ := instI
            ∃ (w : ℕ) (emb : Z ↪ Fin (w + 1))
              (K : AdaptiveProgram (ForrelationCoord k t) w →
                AdaptiveProgram (ForrelationCoord k t) w),
              ∀ next, (K next).queryCap ≤ 2 * (n * k) + next.queryCap ∧
                ∀ z ψ b, (K next).outputMass z (clEmb emb ψ) b =
                  next.outputMass z (clEmb emb (F z ψ)) b
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_lemma_2_1_ii`

**Proof.**

Use the earlier partial helper only for its query-cap arithmetic, accurate Boolean law, and coherent Samples witness. Open that witness as Z, instZ, o, out, F, IsCirc(n*k) F and the exact law equation. Choose a parked physical address from the nonempty Forrelation coordinate set, take finite workspace w=card Z, and embed Z into Fin(w+1). Apply compile_circ directly to that same F before any measurement or reset. Its continuation equation holds for every logical state and every physical continuation, and its physical cap is 2nk. The resulting statement contains this shared witness, total output law, promised error, and A_k independent of t and eta together.

**Named dependencies.** `QuarticQuery.Paper.construction_lemma_2_1_ii`; `QuarticQuery.Upper.compile_circ`; `QuarticQuery.Upper.clEmb`; `Function.Embedding.nonempty_of_card_le`; `QuarticQuery.Upper.decode_samples`; `QuarticQuery.Upper.decodeProb_correct`; `QuarticQuery.Forrelation.repetitions_le`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:158 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** The older construction_lemma_2_1_ii is a partial helper: Samples(n*k)L and Runs(2nk)L alone do not identify the retained physical workspace because Samples.runs measures the full basis and resets it. The complete theorem uses compile_circ before that stage and explicitly ties the same F to all output-law and physical-continuation clauses. The theorem covers k>=1, hence the paper k>=2 domain. All source remains unelaborated.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-lem-2-1-ii -->

### `lem-2.2`

<!-- passage:row-lem-2-2 -->

**Class:** New proof.

**Mathematics (`lem-2.2`).** For m=4^t≥4 and any exact circuit realizing P_k,m with size S≤A m(log₂m)^2, one common family of K=m+(m−1)+r(S+2)≤(42+20A)m(log₂m)^3 tests characterizes every addressed winner on every total input. Each test is exactly computed by an adaptive tree of depth log₂m+1. For each (i,s), the same witnesses admit arbitrary-index coherent evaluation and a physical implementation using at most 2(log₂m+1) bit queries, with all continuation output probabilities preserved.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionComplete.lean`](lean/QuarticQuery/Paper/ConstructionComplete.lean), declaration `QuarticQuery.Paper.construction_lemma_2_2_complete`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_lemma_2_2_complete {k t : ℕ}
    (C : Circuit (ForrelationCoord k t)) (A : ℕ) (ht : 1 ≤ t)
    (hC : CircuitRealises C (P k t))
    (hS : C.size ≤ A * mValue t * (2 * t) ^ 2) :
    Fintype.card (TestIndex (2 * t) (40 * t) C.size) =
      mValue t + (mValue t - 1) + 40 * t * (C.size + 2) ∧
    Fintype.card (TestIndex (2 * t) (40 * t) C.size) ≤
      (42 + 20 * A) * mValue t * (2 * t) ^ 3 ∧
    (∀ (x : BitInput (Loc k t C)) (i : Column (2 * t)) (s : Address (40 * t)),
      PaperWinsAt (P k t) C (2 * t) (40 * t) x i s ↔
        ∀ e : TestIndex (2 * t) (40 * t) C.size,
          localTest C (2 * t) (40 * t) x i s e = true) ∧
    (∀ (i : Column (2 * t)) (s : Address (40 * t))
        (e : TestIndex (2 * t) (40 * t) C.size),
      (∀ x, (localTestTree C (2 * t) (40 * t) i s e).eval x =
        localTest C (2 * t) (40 * t) x i s e) ∧
      (localTestTree C (2 * t) (40 * t) i s e).depth ≤ 2 * t + 1) ∧
    (∀ (i : Column (2 * t)) (s : Address (40 * t)),
      ∃ (Z : TestIndex (2 * t) (40 * t) C.size → Type)
        (instZ : ∀ e, Fintype (Z e)),
        let _ := instZ
        ∃ (o : ∀ e, Z e) (out : ∀ e, Z e → Bool)
          (F : ∀ e, BitInput (Loc k t C) → Reg (Z e) ≃ₗᵢ[ℂ] Reg (Z e)),
          (∀ e, IsCirc (max 3 (2 * t + 1)) (F e)) ∧
          IsCirc (max 3 (2 * t + 1)) (fun x => sigmaOp fun e => F e x) ∧
          (∀ (x : BitInput (Loc k t C))
              (a : TestIndex (2 * t) (40 * t) C.size → ℂ)
              (e : TestIndex (2 * t) (40 * t) C.size),
            slice e (sigmaOp (fun e => F e x) (constructionIndexStart o a)) =
              a e • F e x (rket (o e))) ∧
          (∀ (x : BitInput (Loc k t C))
              (e : TestIndex (2 * t) (40 * t) C.size) (z : Z e),
            out e z ≠ localTest C (2 * t) (40 * t) x i s e →
              (F e x (rket (o e))).ofLp z = 0) ∧
          ∃ (w : ℕ) (emb : (Σ e, Z e) ↪ Fin (w + 1))
            (P : AdaptiveProgram (Loc k t C) w → AdaptiveProgram (Loc k t C) w),
            ∀ next, (P next).queryCap ≤ 2 * (2 * t + 1) + next.queryCap ∧
              ∀ x ψ b, (P next).outputMass x (clEmb emb ψ) b =
                next.outputMass x
                  (clEmb emb (sigmaOp (fun e => F e x) ψ)) b)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_lemma_2_2`

**Proof.**

1. Package the exact count, explicit size estimate, test equivalence and depth specialization.
2. Obtain the coherent witnesses once for each column/address.
3. Choose a finite physical embedding for their direct-sum register, and compile their already-proved controlled operator.
4. Simplify the common read cap for t≥1 to obtain the physical 2(2t+1) bound.

**Named dependencies.** `QuarticQuery.Paper.construction_K_count`; `QuarticQuery.Paper.construction_K_bound`; `QuarticQuery.Paper.construction_lemma_2_2_i`; `QuarticQuery.Paper.construction_test_depth`; `QuarticQuery.Paper.construction_lemma_2_2_ii`; `QuarticQuery.Upper.compile_circ`; `Function.Embedding.nonempty_of_card_le`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:266 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** construction_lemma_2_2_complete is the primary full-scope endpoint. The shorter generic construction_lemma_2_2 is retained as a useful assembly but alone omits the size asymptotic and physical compiler. CircuitRealises and the circuit-size bound are the exact supplied circuit properties of Lemma 2.1(iii), not unproved hardness hypotheses. A depends-on tie to the Forrelation supplier is required when selecting the concrete family. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-lem-2-2 -->

### `lem-2.2.i`

<!-- passage:row-lem-2-2-i -->

**Class:** Short assembly of existing declarations.

**Mathematics (`lem-2.2.i`).** Assume C realizes the partial function f exactly. For every physical input and fixed (i,s), winning at that address is equivalent to every test in the common finite index type passing. Each localTestTree computes its test exactly, with adaptive depth at most max(3,ℓ+1), hence at most ℓ+1=2t+1 for m≥4. The four test classes check the all-ones column, the selected zero in each competitor, every gate equation, and the two output conditions per instance. Every one of a pointer test’s ℓ+2^ℓ pointer and possible-target locations is essential: two full inputs differing only there can have different local-test outputs.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionTests.lean`](lean/QuarticQuery/Paper/ConstructionTests.lean), declaration `QuarticQuery.Paper.construction_lemma_2_2_i`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_lemma_2_2_i {κ : Type} {f : PartialBool κ} (C : Circuit κ)
    (ℓ r : ℕ) (hC : CircuitRealises C f) :
    (∀ (x : BitInput (BitLoc ℓ r C.size κ)) (i : Column ℓ) (s : Address r),
      PaperWinsAt f C ℓ r x i s ↔
        ∀ e : TestIndex ℓ r C.size, localTest C ℓ r x i s e = true) ∧
    (∀ (i : Column ℓ) (s : Address r) (e : TestIndex ℓ r C.size),
      (∀ x, (localTestTree C ℓ r i s e).eval x = localTest C ℓ r x i s e) ∧
      (localTestTree C ℓ r i s e).depth ≤ max 3 (ℓ + 1))
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_test_depth`
- `QuarticQuery.Paper.constructionPointerLookup`
- `QuarticQuery.Paper.construction_pointer_test_eq_lookup`
- `QuarticQuery.Paper.construction_pointer_every_coordinate`
- `QuarticQuery.Paper.constructionPointerLoc`
- `QuarticQuery.Paper.construction_pointerLoc_injective`
- `QuarticQuery.Paper.construction_essential_coordinate_lift`
- `QuarticQuery.Paper.construction_pointer_every_physical_coordinate`

**Proof.**

1. Compose the paper/public winner equivalence with winsAt_iff_localTests.
2. Reuse the exact decision-tree evaluation and depth bounds for every index.
3. For t≥1 simplify max(3,2t+1) by elementary arithmetic.
4. Identify the pointer-test formula with a separate pointer/target lookup; to witness each pointer bit’s relevance use two pointer words differing in that bit and a distinguishing target array. For each target coordinate use its unique pointer encoding and flip only that target.
5. Map pointer coordinates and target-column coordinates into their disjoint BitLoc constructor branches and prove injectivity by a partial coordinate decoder.
6. Extend each schema input to the full physical space using a chosen preimage on this injection’s range and false elsewhere; injection gives exact restriction back to the schema and preserves agreement away from the selected location.
7. Transport the unequal schema outputs and use injectivity of Boolean negation to obtain unequal actual pointer-test outputs.

**Named dependencies.** `QuarticQuery.winsAt_iff_paperWinsAt`; `QuarticQuery.winsAt_iff_localTests`; `QuarticQuery.localTestTree_eval`; `QuarticQuery.localTestTree_depth_le`; `QuarticQuery.pointerEquiv`; `QuarticQuery.Paper.construction_pointer_every_coordinate`; `QuarticQuery.Paper.construction_pointerLoc_injective`; `QuarticQuery.Paper.construction_essential_coordinate_lift`; `Classical.choose_spec`; `Option.some.inj`.

**Proof route.** same.

**Correction.** Retain the accepted corrected ledger wording: adaptive depth is at most max(3,ℓ+1), while fixed support can contain all ℓ+m coordinates. No correction of the current attached preprint is warranted.

**Source and earlier review.**

- paper/extracted.md:266 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The current preprint already states an adaptive query bound correctly. The fixed-support mistake was in an older ledger. The lookup-schema witnesses are now transported to full BitLoc inputs by construction_pointer_every_physical_coordinate. It quantifies X,Y agreeing at every physical coordinate except the selected pointer or target location, with unequal actual localTest values. construction_pointerLoc_injective proves that all ℓ+m listed locations are distinct. All tree correctness and equivalences range over arbitrary invalid/unpromised inputs as well. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-lem-2-2-i -->

### `lem-2.2.ii`

<!-- passage:row-lem-2-2-ii -->

**Class:** New proof.

**Mathematics (`lem-2.2.ii`).** Every local test admits an exact unitary evaluation with at most n=max(3,ℓ+1) abstract reads. The block-diagonal controlled operator acts on an arbitrary complex superposition Σ_e a_e|e,o_e⟩ by applying the correct local operator in each index block, leaving its coefficient and index unchanged, and has zero amplitude at every wrong Boolean output. The finite physical compiler implements this same controlled operator with at most 2n ordinary bit-oracle queries while preserving every continuation output probability for every embedded logical state. For m=4^t≥4 this is at most 2(2t+1) queries. The test index type and count are independent of i,s.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionCoherent.lean`](lean/QuarticQuery/Paper/ConstructionCoherent.lean), declaration `QuarticQuery.Paper.construction_lemma_2_2_ii`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_lemma_2_2_ii {κ : Type} (C : Circuit κ) (ℓ r : ℕ)
    (i : Column ℓ) (s : Address r) :
    ∃ (Z : TestIndex ℓ r C.size → Type) (instZ : ∀ e, Fintype (Z e)),
      let _ := instZ
      ∃ (o : ∀ e, Z e) (out : ∀ e, Z e → Bool)
        (F : ∀ e, BitInput (BitLoc ℓ r C.size κ) → Reg (Z e) ≃ₗᵢ[ℂ] Reg (Z e)),
        (∀ e, IsCirc (max 3 (ℓ + 1)) (F e)) ∧
        IsCirc (max 3 (ℓ + 1)) (fun x => sigmaOp fun e => F e x) ∧
        (∀ (x : BitInput (BitLoc ℓ r C.size κ))
            (a : TestIndex ℓ r C.size → ℂ) (e : TestIndex ℓ r C.size),
          slice e (sigmaOp (fun e => F e x) (constructionIndexStart o a)) =
            a e • F e x (rket (o e))) ∧
        (∀ (x : BitInput (BitLoc ℓ r C.size κ))
            (e : TestIndex ℓ r C.size) (z : Z e),
          out e z ≠ localTest C ℓ r x i s e →
            (F e x (rket (o e))).ofLp z = 0)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_controlled_exact_samples`
- `QuarticQuery.Paper.construction_support_of_exact_law`
- `QuarticQuery.Paper.construction_slice_indexStart`
- `QuarticQuery.Paper.construction_controlled_compile`
- `QuarticQuery.Paper.construction_lemma_2_2_complete`

**Proof.**

1. Apply Samples.tree to each exact local decision tree and pad all read budgets to n.
2. Choose the finite unitary witnesses for each index and combine them with IsCirc.sigma.
3. Use linearity to show the action for arbitrary coefficients, not only the uniform initial index distribution.
4. Convert the exact point-mass output law into coordinatewise zero amplitudes at all incorrectly labelled basis vectors.
5. Embed the finite direct-sum workspace into Fin(w+1) and apply compile_circ to the same operator; its continuation equality proves physical correctness on arbitrary states.

**Named dependencies.** `QuarticQuery.Upper.Samples.tree`; `QuarticQuery.Upper.Samples.mono`; `QuarticQuery.Upper.Samples.congr`; `QuarticQuery.Upper.IsCirc.sigma`; `QuarticQuery.Upper.slice_sigmaOp`; `QuarticQuery.Upper.lawOf`; `QuarticQuery.Upper.pt`; `QuarticQuery.Upper.compile_circ`; `Function.Embedding.nonempty_of_card_le`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:271 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** This repairs a real scope omission in the uncompiled Section2 candidate, whose Samples statement only supplied a particular uniform-index law. The generic theorem gives abstract-read coherence; construction_controlled_compile and the single complete family theorem give physical bit-query accounting. Workspace is retained. No clean XOR oracle with reset ancillas is asserted. No state normalization premise is needed for the displayed linear identities; normalized superpositions are included. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-lem-2-2-ii -->

### `cor-unique-winner`

<!-- passage:row-cor-unique-winner -->

**Class:** Short assembly of existing declarations.

**Mathematics (`cor-unique-winner`).** On every total input there is at most one winning column, even if other columns’ partial inputs are outside the promise or their transcripts are false.

**Proposed relation after elaboration:** stronger

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.construction_unique_winner`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_unique_winner (x : BitInput (BitLoc ℓ r C.size κ))
    (i j : Column ℓ) (hi : constructionWinner f C ℓ r x i)
    (hj : constructionWinner f C ℓ r x j) : i = j
```

**Proof.**

1. Choose a winning address for each alleged winning column.
2. Apply winsAt_column_unique: if i≠j, the pointer from i forces a zero in the all-ones X string of j.

**Named dependencies.** `QuarticQuery.winsAt_column_unique`; `QuarticQuery.Paper.construction_winner_iff_exists_winsAt`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:235 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** This is stated for arbitrary partial f and arbitrary C, so it specializes to the Forrelation family without new hypotheses. The existing source theorem already proves the mathematics; the contribution is an exact tie to the literal paper winner predicate. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-cor-unique-winner -->

### `cor-local-dichotomy`

<!-- passage:row-cor-local-dichotomy -->

**Class:** Short assembly of existing declarations.

**Mathematics (`cor-local-dichotomy`).** Assume C realizes the partial function f exactly. For every input and column, a winner has an address at which every local test passes, and a nonwinner has a failing test at every address. No promise is imposed on the complete input.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionTests.lean`](lean/QuarticQuery/Paper/ConstructionTests.lean), declaration `QuarticQuery.Paper.construction_local_dichotomy`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_local_dichotomy {κ : Type} {f : PartialBool κ}
    {C : Circuit κ} {ℓ r : ℕ} (hC : CircuitRealises C f)
    (x : BitInput (BitLoc ℓ r C.size κ)) (i : Column ℓ) :
    (constructionWinner f C ℓ r x i →
      ∃ s : Address r, ∀ e : TestIndex ℓ r C.size,
        localTest C ℓ r x i s e = true) ∧
    (¬ constructionWinner f C ℓ r x i →
      ∀ s : Address r, ∃ e : TestIndex ℓ r C.size,
        localTest C ℓ r x i s e = false)
```

**Proof.**

1. A winner supplies a WinsAt address, then the local-test equivalence makes all tests true.
2. For a nonwinner, existence of a winning address would contradict the winner equivalence; exists_failing_localTest therefore supplies a failed Boolean test at each address.

**Named dependencies.** `QuarticQuery.Paper.construction_winner_iff_exists_winsAt`; `QuarticQuery.winsAt_iff_localTests`; `QuarticQuery.exists_failing_localTest`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:290 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The all-input quantifiers include out-of-promise A strings and inconsistent transcripts. CircuitRealises is required to connect exact circuit checks with partial-function answers; the supplied Forrelation circuit satisfies it. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-cor-local-dichotomy -->

### `claim-proj-prob`

<!-- passage:row-claim-proj-prob -->

**Class:** Short assembly of existing declarations.

**Mathematics (`claim-proj-prob`).** Prepare u, apply D_{z_1} H ... H D_{z_k} from right to left, and project onto u. Its success probability is Φ(z)^2, at least δ^2 on P(z)=1 and at most δ^2/4 on P(z)=0. Each D is implemented by one physical bit-oracle call through phase kickback; H and the final projection are input independent.

**Proposed relation after elaboration:** Partial for the full bundled row: exact projection law and local one-query phase identity; complete physical witness has cap 2k.

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationQuantum.lean`](lean/QuarticQuery/Paper/ConstructionForrelationQuantum.lean), declaration `QuarticQuery.Paper.construction_projection_test`.

```lean
theorem construction_projection_test (k t : ℕ) (hk : 1 ≤ k) :
    (∀ z : BitInput (ForrelationCoord k t),
      successProb z = Phi k t z ^ 2 ∧
      (P k t z = some true → delta k ^ 2 ≤ successProb z) ∧
      (P k t z = some false → successProb z ≤ delta k ^ 2 / 4)) ∧
    Samples k (fun (z : BitInput (ForrelationCoord k t)) b => bern (Phi k t z ^ 2) b) ∧
    (∀ [Inhabited (ForrelationCoord k t)],
      Runs (2 * k) (fun (z : BitInput (ForrelationCoord k t)) b => bern (Phi k t z ^ 2) b))
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_bitOracle_phase_kickback`
- `QuarticQuery.Paper.construction_bitOracle_phase_preserves`

**Proof.**

Bundle the exact projection law and gap with the existing coherent k-read sampler. Its generic compiler gives 2k physical bit queries. The root-owned supplemental phase theorem proves that a single bitOracle call on the minus-answer subspace implements the desired signs and preserves that subspace and norm. The input-independent Walsh gate is existing hGate. A tight end-to-end k-call Runs compilation is not supplied.

**Named dependencies.** `QuarticQuery.Forrelation.successProb_eq`; `QuarticQuery.Forrelation.successProb_of_true`; `QuarticQuery.Forrelation.successProb_of_false`; `QuarticQuery.Upper.forr_samples`; `QuarticQuery.Upper.Samples.runs`; `QuarticQuery.Paper.construction_bitOracle_phase_kickback`; `QuarticQuery.Paper.construction_bitOracle_phase_preserves`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:176 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** The constant factor is irrelevant for Lemma 2.1(ii), whose full O_k(log(1/eta)) conclusion is supplied below. AA §3.2 gives the Phi^2 circuit immediately before Proposition 6; Proposition 6 itself is a different ceil(k/2)-query test with law (1+Phi)/2.

**Remaining obligation.** A complete physical `Runs k` witness for the entire projection routine remains to be supplied. The new `construction_bitOracle_phase_kickback` theorem proves the one-call local phase step, including entangled workspace. The existing generic compiler proves `Runs (2*k)`. This leaves Lemma 2.1(ii)’s O_k bound intact.

<!-- /passage:row-claim-proj-prob -->

### `claim-N-phi`

<!-- passage:row-claim-N-phi -->

**Class:** New proof.

**Mathematics (`claim-N-phi`).** Let W=sqrt(m)H, whose entries are +/-1. Then N=z_1^T W D_{z_2} W ... W D_{z_k}(1,...,1)^T is an integer, M=m(sqrt m)^{k-1} is a positive integer, and Φ=N/M. Here m=4^t, so sqrt m=2^t.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean), declaration `QuarticQuery.Paper.construction_N_phi`.

```lean
theorem construction_N_phi (k t : ℕ) (hk : 1 ≤ k)
    (z : BitInput (ForrelationCoord k t)) :
    (forrelationNumerator k t z : ℝ) =
      (fun _ : Fin (mValue t) => (1 : ℝ)) ⬝ᵥ
        (alternate (W t) (List.ofFn fun h : Fin k => signDiag z h) *ᵥ
          fun _ => (1 : ℝ)) ∧
    Phi k t z = (forrelationNumerator k t z : ℝ) / (forrelationDenominator k t : ℝ) ∧
    0 < forrelationDenominator k t ∧
    (forrelationDenominator k t : ℝ) =
      (mValue t : ℝ) * (Real.sqrt (mValue t : ℝ)) ^ (k - 1) ∧
    W t = Real.sqrt (mValue t : ℝ) • H t ∧
    (∀ i j : Fin (mValue t), W t i j = 1 ∨ W t i j = -1)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_tailProd_smul`
- `QuarticQuery.Paper.construction_alternate_smul`
- `QuarticQuery.Paper.construction_denominator`
- `QuarticQuery.Paper.construction_numerator_matrix`

**Proof.**

Prove the scaling law for tailProd by list induction, then for alternate on its nonempty diagonal list. Rewrite W=(2^t)H and the all-ones vector=(2^t)u. The k-1 matrix factors and two vector factors reproduce exactly M. Unfold Phi=N/M and cancel the positive denominator. Bundle integrality by the existing integer types, positivity, normalization, and the +/-1 entry alternatives.

**Named dependencies.** `QuarticQuery.forrelationNumerator`; `QuarticQuery.forrelationDenominator`; `QuarticQuery.Forrelation.forrelationDenominator_pos`; `QuarticQuery.Forrelation.Phi_eq_matrix_product`; `QuarticQuery.Forrelation.walshSign_eq_one_or`; `QuarticQuery.Forrelation.H`; `QuarticQuery.Forrelation.W`; `QuarticQuery.Forrelation.u`; `QuarticQuery.Forrelation.alternate`; `QuarticQuery.Forrelation.tailProd`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:183 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** The formal product is ones^T D_1 W ... D_k ones. Absorbing the first diagonal gives the paper z_1^T expression. The type supplies k>=1, hence covers every paper k>=2.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-claim-N-phi -->

### `claim-integer-tests`

<!-- passage:row-claim-integer-tests -->

**Class:** Short assembly of existing declarations.

**Mathematics (`claim-integer-tests`).** Φ≥δ iff 2^{5k}N≥M, and |Φ|≤δ/2 iff 2^{5k+1}|N|≤M. For the actual two-output circuit, b is the first comparison and d is the disjunction of the two comparisons, on every input.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean), declaration `QuarticQuery.Paper.construction_integer_tests`.

```lean
theorem construction_integer_tests (k t : ℕ)
    (z : BitInput (ForrelationCoord k t)) :
    (delta k ≤ Phi k t z ↔
      (2 : ℤ) ^ (5 * k) * forrelationNumerator k t z ≥ forrelationDenominator k t) ∧
    (|Phi k t z| ≤ delta k / 2 ↔
      (2 : ℤ) ^ (5 * k + 1) * |forrelationNumerator k t z| ≤ forrelationDenominator k t) ∧
    (promised (P k t) z ↔
      ((2 : ℤ) ^ (5 * k) * forrelationNumerator k t z ≥ forrelationDenominator k t ∨
       (2 : ℤ) ^ (5 * k + 1) * |forrelationNumerator k t z| ≤ forrelationDenominator k t)) ∧
    (P k t z = some true ↔
      (2 : ℤ) ^ (5 * k) * forrelationNumerator k t z ≥ forrelationDenominator k t)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_forr_value_output`
- `QuarticQuery.Paper.construction_forr_output_bits`

**Proof.**

First bundle the real/integer equivalences and the promise disjunction. Then export the actual value output of forrProg by tracking its final three gates after forrCore_spec. The result holds even off the promise. Use uniqueness of gate-consistent transcripts and the existing CircuitRealises domain clause to state both actual output bits together.

**Named dependencies.** `QuarticQuery.Forrelation.delta_le_Phi_iff`; `QuarticQuery.Forrelation.abs_Phi_le_iff`; `QuarticQuery.Forrelation.promised_P_iff`; `QuarticQuery.Forrelation.P_eq_some_true_iff`; `QuarticQuery.Forrelation.forrCore_spec`; `QuarticQuery.Forrelation.forrCircuit_realises`; `QuarticQuery.Forrelation.consistent_unique`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:195 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** The additional output theorem uses l=k-1, so its circuit is forrCircuit l t on k=l+1 blocks. A theorem about P alone would leave the actual b,d circuit outputs implicit; this export closes that omission.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-claim-integer-tests -->

### `claim-circuit-size`

<!-- passage:row-claim-circuit-size -->

**Class:** New proof.

**Mathematics (`claim-circuit-size`).** N is obtained by k-1 unnormalized Walsh transforms, coordinate sign changes and a final signed sum. A transform of length m uses O(m log m) additions/subtractions. The ideal integer recurrence and its butterfly partial sums have magnitude m^{O(k)}, so O_k(log m) bits suffice. An exact two-output Boolean circuit has O_k(m(log m)^2) gates.

**Proposed relation after elaboration:** Exact size and output endpoint by the existing modular route; partial for a register-by-register formalization of the preprint’s integer derivation.

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean`](lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean), declaration `QuarticQuery.Paper.construction_circuit_costs`.

```lean
theorem construction_circuit_costs (l t : ℕ) (ht : 1 ≤ t) :
    widthTop l t + 1 ≤ (3 * l + 5) * (2 * t) ∧
    (∀ w : ℕ, whtCost w (2 * t) ≤ (2 * t) * mValue t * (6 * w + 1)) ∧
    (∀ n w : ℕ, layerCost n w l ≤
      1 + (l + 1) * (whtCost w n + 2 ^ n * (6 * w))) ∧
    (∀ x : BitInput (ForrelationCoord (l + 1) t),
      |forrelationNumerator (l + 1) t x| ≤ forrelationDenominator (l + 1) t) ∧
    CircuitRealises (forrCircuit l t) (P (l + 1) t) ∧
    (forrCircuit l t).size ≤
      forrConstant (l + 1) * mValue t * (2 * t) ^ 2
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_circuit_width`
- `QuarticQuery.Paper.construction_lemma_2_1_iii`
- `QuarticQuery.Paper.construction_abs_sum_range_le`
- `QuarticQuery.Paper.construction_abs_walshN`
- `QuarticQuery.Paper.construction_walkN_bound`
- `QuarticQuery.Paper.construction_walkN_prefix_bound`
- `QuarticQuery.Paper.construction_butterfly_block_bound`

**Proof.**

Export the concrete width, transform-cost, layer-cost, final numerator bound, circuit correctness, and size endpoint. The existing circuit uses modular Enc invariants, with exact signed interpretation needed at the final comparisons. Root-owned arithmetic lemmas bound ideal walk values, signed prefixes, and butterfly blocks by triangle inequalities, supplying the broad polynomial-magnitude argument. These bounds are separate from a register-by-register identification of the actual modular implementation with unbounded signed arithmetic.

**Named dependencies.** `QuarticQuery.Forrelation.walkN`; `QuarticQuery.Forrelation.numerator_eq_walk`; `QuarticQuery.Forrelation.wht_spec`; `QuarticQuery.Forrelation.whtCost_le`; `QuarticQuery.Forrelation.layerCost`; `QuarticQuery.Forrelation.abs_numerator_le`; `QuarticQuery.Forrelation.forrCircuit_realises`; `QuarticQuery.Forrelation.forrCircuit_size_le`; `QuarticQuery.Paper.construction_abs_walshN`; `QuarticQuery.Paper.construction_walkN_bound`; `QuarticQuery.Paper.construction_walkN_prefix_bound`; `QuarticQuery.Paper.construction_butterfly_block_bound`.

**Proof route.** The exact endpoint uses the repository modular-arithmetic proof. The ideal intermediate bounds follow the preprint’s arithmetic argument; their full register correspondence is recorded separately..

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:190 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** Explicit existing size constant forrConstant k=200(k+1)^2 is recorded in the submitted theorem. For l=k-1 and t>=1 the submitted width inequality is widthTop(l,t)+1 <= (3l+5)(2t). The route does not need every intermediate residue interpreted as an exact signed integer to establish CircuitRealises.

**Remaining obligation.** The ideal walk, prefixes and butterfly blocks have explicit polynomial magnitude bounds in ConstructionArithmetic.lean. No supplied theorem identifies every register of the particular modular implementation with an unbounded signed intermediate value. This is a formal correspondence gap; no overflow counterexample is established.

<!-- /passage:row-claim-circuit-size -->

### `claim-bs-to-L`

<!-- passage:row-claim-bs-to-L -->

**Class:** New proof.

**Mathematics (`claim-bs-to-L`).** For each fixed integer k≥2 and each c>0, for all sufficiently large m=4^t, floor(m^{1-1/k}/(log_2 m)^2) ≤ m^{1-1/k}/(log_2 m)^2 < c k^{-29}(m/log_2(km))^{1-1/k}.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationComparison.lean`](lean/QuarticQuery/Paper/ConstructionForrelationComparison.lean), declaration `QuarticQuery.Paper.construction_claim_bs_to_L`.

```lean
theorem construction_claim_bs_to_L (k : ℕ) (hk : 2 ≤ k)
    (c : ℝ) (hc : 0 < c) :
    ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
      (Lvalue k t : ℝ) < c * (k : ℝ) ^ (-29 : ℤ) *
        ((mValue t : ℝ) / Real.logb 2 ((k : ℝ) * (mValue t : ℝ))) ^
          (1 - 1 / (k : ℝ))
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_affine_comparison`
- `QuarticQuery.Paper.construction_L_le_unfloored`
- `QuarticQuery.Paper.construction_bs_comparison_chain`

**Proof.**

Put a=1-1/k in (0,1]. For any 1<=Lambda<=A+Bt, Lambda^a<=Lambda. Once t>=ceil((A+B)/(4c))+1, the affine denominator is below c(2t)^2. Apply this with Lambda=log_2(km), A=log_2 k, B=2, and c replaced by c k^{-29}; then use the natural-floor bound. The proof establishes the entire unfloored middle comparison as a separate theorem.

**Named dependencies.** `QuarticQuery.Lvalue`; `QuarticQuery.Forrelation.logb_mValue`; `Real.logb_mul`; `Real.div_rpow`; `Real.rpow_le_rpow_of_exponent_le`; `Nat.le_ceil`; `Nat.floor_le`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:173 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=unassessed`, `formal_origin=ours`, `build=not_run`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=outside`. These labels do not describe the new source proofs.

**Scope.** This is an elementary comparison, independent of whether the published precise Bansal–Sinha rate is established. Positive c and k>=2 are essential and appear explicitly. Logarithms follow the paper base-2 convention; changing a fixed base only rescales c. The source bansalSinhaLower proves a different statement, L<R(P), and is not used here.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-claim-bs-to-L -->

### `eq-1`

<!-- passage:row-eq-1 -->

**Class:** Equivalent formulations of an existing definition.

**Mathematics (`eq-1`).** alpha_tot is the infimum of nonnegative alpha for which one finite real C bounds R(f) by C(1+Q(f))^alpha uniformly over every n≥1 and every total Boolean f on n bits. The same set is obtained by requiring C>0.

**Proposed relation after elaboration:** equivalent

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionModels.lean`](lean/QuarticQuery/Paper/ConstructionModels.lean), declaration `QuarticQuery.Paper.construction_alphaTot_eq_inf`.

```lean
theorem construction_alphaTot_eq_inf :
    alphaTot = sInf {α : ℝ | 0 ≤ α ∧ ∃ C : ℝ,
      ∀ n : ℕ, 1 ≤ n → ∀ f : TotalBool (Fin n),
        (R (totalise f) : ℝ) ≤ C * Real.rpow (1 + (Q (totalise f) : ℝ)) α}
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_universalPower_iff`
- `QuarticQuery.Paper.construction_exponent_set_wellDefined`

**Proof.**

1. Unpack UniversalPower; discard positivity for one implication.
2. For the converse choose max C 1 and multiply C≤max C 1 by the nonnegative real power.
3. Use set extensionality and the membership equivalence under sInf.
4. Use universalPower_four for nonemptiness and the first conjunct of UniversalPower for the zero lower bound.

**Named dependencies.** `QuarticQuery.UniversalPower`; `QuarticQuery.alphaTot`; `QuarticQuery.universalPower_four`; `Real.rpow_nonneg`; `mul_le_mul_of_nonneg_right`.

**Proof route.** same definition; supplementary nonemptiness uses alternative universal-bound route.

**Correction.** None proposed.

**Source and earlier review.**

- paper/extracted.md:28-34 (equation 1)
- repository/lean/QuarticQuery/Statement.lean:322-329 (UniversalPower and alphaTot)
- repository/research/adjudication/funnel_adjudication.json:F-EQ1-EQUIV
- repository/research/adjudication/funnel_adjudication.json:pending_ties eq-1
- repository/lean/QuarticQuery/Appendix/TheoremA1.lean (universalPower_four)

F-EQ1-EQUIV accepted the equivalence of finite and positive constants. F-UNTIED identified the missing reviewed definition tie. The new theorem proves the exact equivalence instead of treating it as a notation assumption.

**Scope.** The paper asks for a finite constant. Lean uses a real constant, so finiteness is built into the type. Requiring positivity is equivalent: replace C by max(C,1), since the real power is nonnegative. The proof preserves the quantifier order C before input size n and the function f. A supplementary theorem verifies nonemptiness and a lower bound for the infimum set, so the definition does not silently rely on sInf of an empty/unbounded set.

**Remaining obligation.** Fresh elaboration and review of the new tie. No mathematical change to equation (1) is proposed.

<!-- /passage:row-eq-1 -->

### `eq-2`

<!-- passage:row-eq-2 -->

**Class:** Short assembly of existing declarations.

**Mathematics (`eq-2`).** For each fixed integer k≥2, choose the supplied exact circuit family. For all sufficiently large m=4^t, Q(F_{k,m})≤budgetConst(k) sqrt(m)(log_2 m)^6 and R(F_{k,m})≥(1/400)m^(2−1/k)/(log_2 m)^2. The circuit has at most forrConstant(k)m(log_2 m)^2 gates. Therefore the paper’s positive-c,C,b existential statement holds.

**Proposed relation after elaboration:** exact existential statement, with a stronger named-family companion

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionFamily.lean`](lean/QuarticQuery/Paper/ConstructionFamily.lean), declaration `QuarticQuery.Paper.construction_equation_two`.

```lean
theorem construction_equation_two (k : ℕ) (hk : 2 ≤ k) :
    ∃ (S : ℕ) (c C : ℝ), 0 < c ∧ 0 < C ∧
      ∃ (b : ℕ), 0 < b ∧ ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
        ∃ Cir : Circuit (ForrelationCoord k t), CircuitRealises Cir (P k t) ∧
          Cir.size ≤ S * mValue t * (2 * t) ^ 2 ∧
          (Q (totalise (Fkm k t Cir)) : ℝ) ≤
            C * Real.sqrt (mValue t : ℝ) * (Real.logb 2 (mValue t : ℝ)) ^ b ∧
          c * Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) /
              (Real.logb 2 (mValue t : ℝ)) ^ 2 ≤
            (R (totalise (Fkm k t Cir)) : ℝ)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_family_named`
- `QuarticQuery.Paper.construction_sqrt_mValue`

**Proof.**

1. Write k=l+1. Obtain an eventual threshold for Lvalue(k,t)<R(P(k,t)) from ForrelationLower.bansalSinhaLower.
2. Set the new threshold to max(t0,8). Apply Gvalue_lt_R_Fkm to exactly forrCircuit l t.
3. Apply rpow_le_of_Gvalue_lt to obtain c=1/400; use Q_Fkm_le to obtain b=6 and Upper.budgetConst(k).
4. Rewrite log_2(mValue t)=2t and sqrt(mValue t)=2^t. Retain forrCircuit_realises and forrCircuit_size_le in the same theorem.
5. Package c=1/400, C=budgetConst(k), b=6 and S=forrConstant(k) to prove the paper-shaped existential statement.

**Named dependencies.** `QuarticQuery.ForrelationLower.bansalSinhaLower`; `QuarticQuery.Gvalue_lt_R_Fkm`; `QuarticQuery.rpow_le_of_Gvalue_lt`; `QuarticQuery.Forrelation.forrCircuit`; `QuarticQuery.Forrelation.forrCircuit_realises`; `QuarticQuery.Forrelation.forrCircuit_size_le`; `QuarticQuery.Forrelation.forrConstant`; `QuarticQuery.Upper.Q_Fkm_le`; `QuarticQuery.Upper.budgetConst_pos`; `QuarticQuery.logb_mValue`; `QuarticQuery.mValue_cast`; `QuarticQuery.Forrelation.mValue_cast`.

**Proof route.** same assembly, with existing alternative Forrelation lower-bound proof.

**Correction.** None proposed.

**Source and earlier review.**

- paper/extracted.md:35-44 (Theorem 1.1 equation 2)
- repository/lean/QuarticQuery/ForrelationLower/Main.lean:505-506 (bansalSinhaLower)
- repository/lean/QuarticQuery/LowerBound/Planted/Main.lean:203-208 (Gvalue_lt_R_Fkm)
- repository/lean/QuarticQuery/Results/Exponent.lean:365-413 (Gvalue_ge and rpow_le_of_Gvalue_lt)
- repository/lean/QuarticQuery/Upper/Bound.lean:249-261 (Q_Fkm_le and budgetConst_pos)
- repository/lean/QuarticQuery/Forrelation/Circuit.lean:389,462-469 (constant and size)
- repository/lean/QuarticQuery/Forrelation/Walsh.lean:196-198 (square-root normalization identity)
- repository/corpus/ties.json:eq-2

The existing family_bounds tie splits unconditional Q and conditional floor-R. FamilyBoundsAt hides the size bound behind its existential circuit. The new named-family companion removes both presentation deficiencies and translates to the exact real-power lower bound.

**Scope.** The named companion simultaneously certifies circuit correctness, size, Q and R for the fixed explicit forrCircuit l t. It fixes c=1/400 and b=6 and uses Upper.budgetConst(l+1)>0. The original existential statement follows for every k≥2 by writing k=l+1. Threshold t0 is enlarged to at least 8. The lower-bound proof is unconditional because ForrelationLower.bansalSinhaLower is applied, not assumed. Only its fixed-k theorem is used; the uncompiled uniform-k module is not imported.

**Remaining obligation.** Fresh elaboration of two short wrappers and their parameter identity; no new Forrelation or planted lower-bound mathematics is needed. The wrapper still inherits the disclosed alternative lower-bound proof route.

<!-- /passage:row-eq-2 -->

### `eq-3`

<!-- passage:row-eq-3 -->

**Class:** Short assembly of existing declarations.

**Mathematics (`eq-3`).** For k≥2, m=4^t, and z=(z_1,...,z_k), Φ(z)=u^T D_{z_1} H D_{z_2} H ... H D_{z_k}u, with exactly k diagonals and k-1 Walsh factors, and δ=2^{-5k}.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean), declaration `QuarticQuery.Paper.construction_equation_3`.

```lean
theorem construction_equation_3 (k t : ℕ) (hk : 1 ≤ k)
    (z : BitInput (ForrelationCoord k t)) :
    Phi k t z = u t ⬝ᵥ
      (alternate (H t) (List.ofFn fun h : Fin k => signDiag z h) *ᵥ u t) ∧
    delta k = (2 : ℝ) ^ (-(5 * (k : ℤ)))
```

**Proof.**

Pair Phi_eq_matrix_product with the defining equality for delta. alternate starts with the first diagonal, and each tail matrix contributes one H. The submitted theorem works already for k>=1; the paper only uses k>=2.

**Named dependencies.** `QuarticQuery.Forrelation.Phi_eq_matrix_product`; `QuarticQuery.Forrelation.delta`; `QuarticQuery.Forrelation.alternate`; `QuarticQuery.Forrelation.tailProd`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:140 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** Every new declaration is source text only; no Lean or comparator run was available.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-eq-3 -->

### `eq-4`

<!-- passage:row-eq-4 -->

**Class:** Short assembly of existing declarations.

**Mathematics (`eq-4`).** P_{k,m}:{0,1}^{km}-> {0,1,*} satisfies P(z)=1 iff Φ(z)≥δ, P(z)=0 iff |Φ(z)|≤δ/2, and P(z)=* iff both inequalities fail. The two defined cases are disjoint.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean), declaration `QuarticQuery.Paper.construction_equation_4`.

```lean
theorem construction_equation_4 (k t : ℕ)
    (z : BitInput (ForrelationCoord k t)) :
    Fintype.card (ForrelationCoord k t) = k * mValue t ∧
    (P k t z = some true ↔ delta k ≤ Phi k t z) ∧
    (P k t z = some false ↔ |Phi k t z| ≤ delta k / 2) ∧
    (P k t z = none ↔ ¬ delta k ≤ Phi k t z ∧ ¬ |Phi k t z| ≤ delta k / 2) ∧
    ¬ (delta k ≤ Phi k t z ∧ |Phi k t z| ≤ delta k / 2)
```

**Proof.**

Bundle all three branches, their disjointness, and the input-coordinate count. The undefined branch explicitly includes large negative Phi.

**Named dependencies.** `QuarticQuery.Forrelation.P_eq_some_true_iff`; `QuarticQuery.Forrelation.P_eq_some_false_iff`; `QuarticQuery.Forrelation.P_eq_none_iff`; `QuarticQuery.Forrelation.cases_disjoint`; `Fintype.card_prod`; `Fintype.card_fin`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:145 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** Every new declaration is source text only; no Lean or comparator run was available.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-eq-4 -->

### `eq-5`

<!-- passage:row-eq-5 -->

**Class:** Existing definition, exposed explicitly.

**Mathematics (`eq-5`).** For fixed k≥2 and m=4^t, L_{k,m}=floor(m^{1-1/k}/(log_2 m)^2).

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean), declaration `QuarticQuery.Paper.construction_equation_5`.

```lean
theorem construction_equation_5 (k t : ℕ) :
    Lvalue k t =
      ⌊Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
        (Real.logb 2 (mValue t : ℝ)) ^ 2⌋₊
```

**Proof.**

The existing Lvalue is definitionally equal to the displayed natural floor. Keep the complexity inequality separate as Lemma 2.1(i), as adjudication requires.

**Named dependencies.** `QuarticQuery.Lvalue`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:155 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=none`, `formal_origin=none`, `build=not_run`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=none`. These labels do not describe the new source proofs.

**Scope.** Uses the corrected ledger row: the former appended lower-bound assertion was removed by adjudication. At t=0 Lean totalizes division by zero; the paper asymptotics use t>=1.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-eq-5 -->

### `eq-6`

<!-- passage:row-eq-6 -->

**Class:** Short assembly of existing declarations.

**Mathematics (`eq-6`).** At m=4^t=2^(2t), the base-two logarithm is ℓ=2t and the natural ceiling r=⌈20 log₂m⌉ is 40t.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.construction_eq6`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_eq6 (t : ℕ) :
    Real.logb 2 (mValue t : ℝ) = (2 * t : ℕ) ∧
      ⌈20 * Real.logb 2 (mValue t : ℝ)⌉₊ = 40 * t
```

**Proof.**

1. Apply logb_mValue to identify the real logarithm.
2. Rewrite 20·(2t) as the natural cast of 40t and use the natural-ceiling-of-a-natural-cast identity.

**Named dependencies.** `QuarticQuery.logb_mValue`; `QuarticQuery.mValue`; `Nat.ceil_natCast`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:207 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The attached paper expressly fixes powers of four (paper/extracted.md:130–132). This is the actual family, not a restriction introduced by the formalization. The identity also holds for t=0 although the query-depth specialization uses t≥1. Nat.ceil_natCast was name-checked against the official public Mathlib Floor.Semiring documentation; the pinned revision was not elaborated. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-eq-6 -->

### `eq-7`

<!-- passage:row-eq-7 -->

**Class:** Short assembly of existing declarations.

**Mathematics (`eq-7`).** If each of this column’s r partial-function instances has a defined answer, s is the true address exactly when f(A_i,h)=some(s_h) for every h. No other column is required to satisfy any promise.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.construction_trueAddress_iff`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_trueAddress_iff
    (x : BitInput (BitLoc ℓ r C.size κ)) (i : Column ℓ)
    (hdef : ∀ h, promised f (readA x i h)) (s : Address r) :
    (∀ h, f (readA x i h) = some (s h)) ↔ s = trueAddress f x i hdef
```

**Proof.**

1. Compare each supplied answer with apply_eq_trueAddress.
2. Use injectivity of some and function extensionality to obtain address equality; the reverse direction substitutes the true address.

**Named dependencies.** `QuarticQuery.trueAddress`; `QuarticQuery.apply_eq_trueAddress`; `Option.some.inj`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:223 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The promise premise is local to the addressed column. Equality is independent of the proof object used to establish that the answers are defined. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-eq-7 -->

### `eq-8`

<!-- passage:row-eq-8 -->

**Class:** Existing definition, exposed explicitly.

**Mathematics (`eq-8`).** At any proposed cell address s, every competing column j≠i has X_j[p_i,s,j]=0. The paper’s display is this predicate at the true address s_i.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.constructionOutwardPointers`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
def constructionOutwardPointers {S : ℕ} (x : BitInput (BitLoc ℓ r S κ))
    (i : Column ℓ) (s : Address r) : Prop :=
  ∀ j : {j : Column ℓ // j ≠ i},
    readX x j.val (pointerEquiv ℓ (readPointerBit x i s j)) = false
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_eq8_of_winsAt`

**Proof.**

1. Name the universally quantified physical-bit predicate without changing its definition.
2. Project the fourth clause of WinsAt to show that every winning addressed cell satisfies it.

**Named dependencies.** `QuarticQuery.readX`; `QuarticQuery.readPointerBit`; `QuarticQuery.pointerEquiv`; `QuarticQuery.WinsAt`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:227 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The definition is generic in transcript-size S; the projection theorem is a consequence, while the definition itself is the exact row. It quantifies over all j≠i, rather than merely asserting existence of one outgoing witness. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-eq-8 -->

### `def-transcript`

<!-- passage:row-def-transcript -->

**Class:** Existing definition, exposed explicitly.

**Mathematics (`def-transcript`).** For every circuit C and input x, a transcript is a Boolean value at each of its S non-input gates, including its domain and value outputs. It is consistent precisely when every proposed gate value equals that gate’s truth table applied to actual input bits or earlier transcript bits. This holds precisely for the topological evaluation, which is the unique consistent transcript.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.construction_transcript_definition`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_transcript_definition {κ : Type} (C : Circuit κ)
    (x : BitInput κ) (tr : Fin C.size → Bool) :
    GateConsistent C x tr ↔ ∀ g : Fin C.size,
      tr g = (C.gate g).table
        (predecessorValue C x tr g (C.gate g).left)
        (predecessorValue C x tr g (C.gate g).right)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_transcript_input_wire`
- `QuarticQuery.Paper.construction_transcript_gate_wire`
- `QuarticQuery.Paper.construction_transcript_correct`

**Proof.**

1. Expose the defining gate equations by reflexivity.
2. Expose both input-wire and earlier-gate predecessor evaluations by reflexivity.
3. Package the existing characterization and unique-existence theorems; their inductive proof follows the topological gate ordering.

**Named dependencies.** `QuarticQuery.GateConsistent`; `QuarticQuery.predecessorValue`; `QuarticQuery.gateConsistent_iff_eq_circuitEval`; `QuarticQuery.existsUnique_gateConsistent`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:122 (Section 1.3)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The type Fin C.size includes both C.domainOut and C.valueOut. Input values are fetched from x and are never copied into transcript coordinates. Statements quantify over every x and every proposed transcript. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-def-transcript -->

### `def-column-layout`

<!-- passage:row-def-column-layout -->

**Class:** Existing definition, exposed explicitly.

**Mathematics (`def-column-layout`).** The physical input coordinates are the disjoint union of X-bits (column,row), A-bits (column,h,Forrelation coordinate), pointer bits (column,address,other column,bit), and transcript bits (column,address,h,gate). At m=4^t they give m columns, km-bit A strings, and 2^r cells per column. A fixed bijection sends each ℓ-bit pointer word to exactly one of the m rows.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.construction_column_layout`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_column_layout (ℓ r S : ℕ) (κ : Type) :
    BitLoc ℓ r S κ =
      ((Column ℓ × Column ℓ) ⊕
        (Column ℓ × Fin r × κ) ⊕
        (Σ i : Column ℓ, Address r × {j : Column ℓ // j ≠ i} × Fin ℓ) ⊕
        (Column ℓ × Address r × Fin r × Fin S))
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_pointer_encoding`
- `QuarticQuery.Paper.construction_layout_cardinalities`

**Proof.**

1. Unfold BitLoc by type equality to expose all four disjoint coordinate kinds.
2. Reuse bijectivity and unique-encoding theorems for pointerEquiv.
3. Simplify Fintype cardinalities of Fin, products and Boolean function types.

**Named dependencies.** `QuarticQuery.BitLoc`; `QuarticQuery.Column`; `QuarticQuery.Address`; `QuarticQuery.ForrelationCoord`; `QuarticQuery.pointerEquiv_bijective`; `QuarticQuery.existsUnique_pointer`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:208 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** Every Boolean function on BitLoc is an allowed total input. The A strings carry no global promise and arbitrary transcript contents are permitted. Every ℓ-bit pointer is valid because the pointer decoder is a bijection; there is no hidden invalid-pointer exclusion. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-def-column-layout -->

### `def-winner`

<!-- passage:row-def-winner -->

**Class:** Existing definition, exposed explicitly.

**Mathematics (`def-winner`).** A column is a winner if its X string is all ones, all its partial answers are defined, the cell indexed by those answers contains the unique true circuit transcript for every instance, and its pointers select a zero in every other column. This is equivalent to the existence of an address satisfying public WinsAt.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.constructionWinner`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
def constructionWinner (f : PartialBool κ) (C : Circuit κ) (ℓ r : ℕ)
    (x : BitInput (BitLoc ℓ r C.size κ)) (i : Column ℓ) : Prop :=
  (∀ j, readX x i j = true) ∧
  ∃ hdef : ∀ h, promised f (readA x i h),
    (∀ h, readTranscript x i (trueAddress f x i hdef) h =
      circuitEval C (readA x i h)) ∧
    constructionOutwardPointers x i (trueAddress f x i hdef)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_winner_iff_exists_winsAt`

**Proof.**

1. Define the four literal paper conditions together.
2. In the forward direction choose trueAddress and use winsAt_iff_paperWinsAt.
3. In the reverse direction use the same equivalence and substitute the true address.

**Named dependencies.** `QuarticQuery.trueAddress`; `QuarticQuery.circuitEval`; `QuarticQuery.PaperWinsAt`; `QuarticQuery.winsAt_iff_paperWinsAt`; `QuarticQuery.WinsAt`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:221 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The all-ones condition and the unique true transcript are explicit; neither is weakened to a local output constraint. No CircuitRealises premise is needed for this semantic definition or its equivalence to public WinsAt. Circuit correctness is needed only when replacing partial answers with output tests. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-def-winner -->

### `def-win-at-address`

<!-- passage:row-def-win-at-address -->

**Class:** Short assembly of existing declarations.

**Mathematics (`def-win-at-address`).** WinsAt(x,i,s) is equivalent to “i is a winner and s=s_i”. If C realizes f on every input, it is also equivalent to all X_i bits being one, all transcripts being the true evaluations with domain output one and answer output s_h, and all outward zero-pointer checks.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionDefinitions.lean), declaration `QuarticQuery.Paper.construction_winsAt_iff_winner_and_address`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_winsAt_iff_winner_and_address
    (x : BitInput (BitLoc ℓ r C.size κ)) (i : Column ℓ) (s : Address r) :
    WinsAt f C ℓ r x i s ↔
      constructionWinner f C ℓ r x i ∧
        ∃ hdef : ∀ h, promised f (readA x i h), s = trueAddress f x i hdef
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_win_at_address_outputs`

**Proof.**

1. Convert through the literal winner definition and the true-address characterization.
2. Reuse winsAt_iff_outputs for the output-test formulation under CircuitRealises.

**Named dependencies.** `QuarticQuery.winsAt_iff_paperWinsAt`; `QuarticQuery.winsAt_iff_outputs`; `QuarticQuery.Paper.construction_trueAddress_iff`; `QuarticQuery.Paper.construction_winner_iff_exists_winsAt`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:264 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** There are two exact formulations with different hypotheses. The paper-wording equivalence needs no realization premise. The current ledger’s output-test equivalence explicitly requires CircuitRealises C f, supplied for C_k,m by Lemma 2.1(iii); dropping it would make the equivalence false. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-def-win-at-address -->

### `def-K`

<!-- passage:row-def-K -->

**Class:** Short assembly of existing declarations.

**Mathematics (`def-K`).** There are K=m+(m−1)+r(S+2) tests, independently of i and s. If m=4^t, t≥1 and S≤A·m·(2t)^2, then K≤(42+20A)·m·(2t)^3. For each fixed k≥1 the supplied exact Forrelation circuits give a constant B(k), chosen before t, with K≤B(k)m(log₂m)^3 for every t≥1.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionTests.lean`](lean/QuarticQuery/Paper/ConstructionTests.lean), declaration `QuarticQuery.Paper.construction_K_count`.

The full contextual binders and imports are recorded in `row_details.json` and the source module.

```lean
theorem construction_K_count (t S : ℕ) :
    Fintype.card (TestIndex (2 * t) (40 * t) S) =
      mValue t + (mValue t - 1) + 40 * t * (S + 2)
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_K_bound`
- `QuarticQuery.Paper.construction_K_family`

**Proof.**

1. Specialize card_testIndex to ℓ=2t and r=40t.
2. Rewrite r=20ℓ; bound each lower-order term by a multiple of mℓ³ and distribute the size bound.
3. For positive k use forrCircuit(k−1,t) and A=forrConstant(k), with B=42+20A.

**Named dependencies.** `QuarticQuery.card_testIndex`; `QuarticQuery.Forrelation.forrCircuit`; `QuarticQuery.Forrelation.forrCircuit_realises`; `QuarticQuery.Forrelation.forrCircuit_size_le`; `QuarticQuery.Forrelation.forrConstant`.

**Proof route.** same.

**Correction.** No change to the attached preprint or current adjudicated row.

**Source and earlier review.**

- paper/extracted.md:269 (Section 2.2)

The original statement, ties and evidence fields are preserved in source_records/target_statements.json.

**Scope.** The main count theorem alone does not assert the asymptotic estimate. The evidence set includes the explicit estimate and the family quantifier ordering. The inequality proof exports arithmetic already used inside Upper/Bound.lean:137–163; it is not a novelty claim. All submitted proof bodies are unelaborated: no lean/lake executable or pinned Mathlib artifacts were available. No new build, dependency closure, axiom check, or Comparator result is claimed. Original built-at-pin evidence applies only to the original declarations. The proposed statement relation below is a mathematical/source-level assessment pending elaboration and review.

**Remaining obligation.** Elaboration, compilation at the pinned toolchain, axiom/dependency checks, and semantic review remain; no completed-check claim is made.

<!-- /passage:row-def-K -->

### `def-partial-query`

<!-- passage:row-def-partial-query -->

**Class:** Equivalent formulations of an existing definition.

**Mathematics (`def-partial-query`).** Define the Option-valued extension of f:D→{0,1} by f on D and none outside D. It is promised exactly on D. For every success predicate C(x,b), correctness whenever the Option value is some b is equivalent to C(x,f(x)) for each x in D. Instantiating C gives the original deterministic, randomized and quantum notions. Every Option-valued partial function is recovered from its own domain and values.

**Proposed relation after elaboration:** equivalent

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionModels.lean`](lean/QuarticQuery/Paper/ConstructionModels.lean), declaration `QuarticQuery.Paper.construction_correct_on_domain_iff`.

```lean
theorem construction_correct_on_domain_iff {ι : Type}
    (D : Set (BitInput ι)) (f : D → Bool)
    (Correct : BitInput ι → Bool → Prop) :
    (∀ x b, constructionPartial D f x = some b → Correct x b) ↔
      ∀ x (hx : x ∈ D), Correct x (f ⟨x, hx⟩)
```

**Supporting declarations.**

- `QuarticQuery.Paper.constructionPartial`
- `QuarticQuery.Paper.constructionPartial_eq_some_iff`
- `QuarticQuery.Paper.construction_promised_iff`
- `QuarticQuery.Paper.construction_RLe_domain_iff`
- `QuarticQuery.Paper.construction_DLe_domain_iff`
- `QuarticQuery.Paper.construction_QLe_domain_iff`
- `QuarticQuery.Paper.constructionPartial_reconstruct`

**Proof.**

1. Split on membership in D to characterize extension(x)=some b.
2. Use that characterization to prove the generic correctness equivalence in both directions.
3. Unfold RLe, DLe, QLe and ConstantOnPromise and rewrite with the generic equivalence. The budgets are preserved literally.
4. For the reverse conversion, split on promised f x; use Classical.choose_spec on the promised branch and f x=none on the other.

**Named dependencies.** `QuarticQuery.PartialBool`; `QuarticQuery.promised`; `QuarticQuery.RLe`; `QuarticQuery.DLe`; `QuarticQuery.QLe`; `QuarticQuery.ConstantOnPromise`; `QuarticQuery.RandomizedProgram.depth`; `QuarticQuery.AdaptiveProgram.queryCap`.

**Proof route.** same.

**Correction.** None proposed.

**Source and earlier review.**

- paper/extracted.md:117-123 (Section 1.3)
- repository/lean/QuarticQuery/Statement.lean:23-36 (PartialBool, totalise, promised)
- repository/lean/QuarticQuery/Statement.lean:73-89 (RLe and DLe)
- repository/lean/QuarticQuery/Statement.lean:120-151 (caps, ConstantOnPromise, QLe)
- repository/corpus/ties.json:def-partial-query
- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md:1582-1592 (Section 11.1, printed page 89)

The existing ties concern reindexing and are partial. The definitions themselves supply the semantics; this bridge supplies the missing pair-to-Option equivalence.

**Scope.** The new bridge explicitly relates a pair (D,f:D→Bool) to the existing Option Bool function. A generic Correct predicate handles every specified error requirement; the three model specializations retain their exact depth and probability conditions. The reverse reconstruction theorem covers every existing partial function, including empty promises. No off-domain correctness hypothesis is added.

**Remaining obligation.** Fresh elaboration and intended-meaning review of the new translation lemmas. General simulation equivalence to every textbook machine model is outside this definition row.

<!-- /passage:row-def-partial-query -->

### `def-query-oracle`

<!-- passage:row-def-query-oracle -->

**Class:** Short assembly of existing declarations.

**Mathematics (`def-query-oracle`).** For every input x and workspace, O_x sends |i,b,z> to |i,b xor x_i,z>, is its own inverse, and is a complex linear isometry equivalence.

**Proposed relation after elaboration:** exact

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionModels.lean`](lean/QuarticQuery/Paper/ConstructionModels.lean), declaration `QuarticQuery.Paper.construction_query_oracle`.

```lean
theorem construction_query_oracle {ι : Type} [Fintype ι] {w : ℕ}
    (x : BitInput ι) :
    (∀ (i : ι) (b : Bool) (z : Fin (w + 1)),
      bitOracle x (ket (i, b, z)) = ket (i, xor b (x i), z)) ∧
    (∀ ψ : State ι w, bitOracle x (bitOracle x ψ) = ψ) ∧
    ∃ U : State ι w ≃ₗᵢ[ℂ] State ι w, ∀ ψ, U ψ = bitOracle x ψ
```

**Proof.**

1. Apply bitOracle_ket and check the four Boolean cases to rewrite the existing if/negation as xor.
2. Apply bitOracle_bitOracle for inversion.
3. Take U=bitOracleL x and use bitOracleL_apply for the linear-isometry-equivalence witness.

**Named dependencies.** `QuarticQuery.bitOracle`; `QuarticQuery.ket`; `QuarticQuery.bitOracle_ket`; `QuarticQuery.flipPoint`; `QuarticQuery.bitOracle_bitOracle`; `QuarticQuery.bitOracleL`; `QuarticQuery.bitOracleL_apply`.

**Proof route.** same.

**Correction.** None proposed.

**Source and earlier review.**

- paper/extracted.md:18-25 (oracle and query convention)
- repository/lean/QuarticQuery/Statement.lean:95-106 (Basis, State, bitOracle)
- repository/lean/QuarticQuery/Model/Quantum.lean:27-85 (flipPoint, bitOracleL, inversion)
- repository/lean/QuarticQuery/Model/Quantum.lean:282-302 (ket and bitOracle_ket)
- literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md:345-353 (Section 2.4, printed pp.17-18)

Existing ties are separate partial properties. This is the missing conjunction, with no change to oracle semantics.

**Scope.** One theorem combines all clauses of the row. The action is on actual basis kets, not merely an unexplained amplitude formula. Complex linear isometry equivalence supplies surjectivity and norm/inner-product preservation, which is unitarity in this finite-dimensional setting. The workspace label is unchanged. No bit/phase model bridge is substituted for the requested oracle statement.

**Remaining obligation.** Fresh elaboration of the conjunction. Its component declarations are in the supplied compiled Model/Quantum module, according to BUILD_STATUS.md.

<!-- /passage:row-def-query-oracle -->

### `def-walsh-sign`

<!-- passage:row-def-walsh-sign -->

**Class:** Existing definition, exposed explicitly.

**Mathematics (`def-walsh-sign`).** For m=4^t and a,b in {0,1}^{2t}, bitSign(e)=(-1)^e, H_{a,b}=m^{-1/2}(-1)^{<a,b>}, u=m^{-1/2}(1,...,1)^T, and D_z=diag(z). The positive square root is 2^t.

**Proposed relation after elaboration:** exact on paper domain

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`](lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean), declaration `QuarticQuery.Paper.construction_walsh_definitions`.

```lean
theorem construction_walsh_definitions (k t : ℕ)
    (z : BitInput (ForrelationCoord k t)) :
    (∀ b : Bool, bitSign b = (-1 : ℤ) ^ (if b then (1 : ℕ) else 0)) ∧
    (∀ i j : Fin (mValue t), walshSign t i j =
      (-1 : ℤ) ^ (∑ b ∈ range (2 * t),
        if i.val.testBit b && j.val.testBit b then (1 : ℕ) else 0)) ∧
    (∀ i j : Fin (mValue t), H t i j =
      (Real.sqrt (mValue t : ℝ))⁻¹ * (walshSign t i j : ℝ)) ∧
    (∀ i : Fin (mValue t), u t i = (Real.sqrt (mValue t : ℝ))⁻¹) ∧
    (∀ h : Fin k, signDiag z h = Matrix.diagonal fun i => (bitSign (z (h, i)) : ℝ))
```

**Supporting declarations.**

- `QuarticQuery.Paper.construction_forr_sqrt_mValue`

**Proof.**

Unfold the existing bit and matrix definitions. Identify sqrt(4^t)=2^t using mValue_cast and positivity. Bundle every component of the original definition, including the bit/sign convention and diagonal.

**Named dependencies.** `QuarticQuery.bitSign`; `QuarticQuery.walshSign`; `QuarticQuery.Forrelation.H`; `QuarticQuery.Forrelation.W`; `QuarticQuery.Forrelation.u`; `QuarticQuery.Forrelation.signDiag`; `QuarticQuery.Forrelation.mValue_cast`; `Real.sqrt_sq`.

**Proof route.** same.

**Correction.** No new change to the corrected ledger statement.

**Source and earlier review.**

- paper/extracted.md:136 (Section 2.1)
- repository/corpus/statements.json
- repository/corpus/ties.json

The input record gives the previous declarations the following labels: `formal_statement=partial`, `formal_origin=ours`, `build=built_at_pin`, `comparator=not_run`, `conditional=False`, `route=none`, `reach=reached`. These labels do not describe the new source proofs.

**Scope.** Every new declaration is source text only; no Lean or comparator run was available.

**Remaining obligation.** Fresh elaboration, axiom audit and review of the exact statement remain. No further statement-level gap was identified in this scoped source review.

<!-- /passage:row-def-walsh-sign -->

### `def-log-convention`

<!-- passage:row-def-log-convention -->

**Class:** Prose convention.

**Mathematics (`def-log-convention`).** Throughout the construction log means log_2. For m=4^t, log_2 m=2t. The displayed identity is a direct check of the convention on this family.

**Proposed relation after elaboration:** definition/convention; supplementary exact identity

**Lean statement, unelaborated.** Source: [`lean/QuarticQuery/Paper/ConstructionModels.lean`](lean/QuarticQuery/Paper/ConstructionModels.lean), declaration `QuarticQuery.Paper.construction_log2_mValue`.

```lean
theorem construction_log2_mValue (t : ℕ) :
    Real.logb 2 (mValue t : ℝ) = 2 * (t : ℝ)
```

**Proof.**

1. Apply QuarticQuery.logb_mValue exactly.
2. Keep the convention itself as prose; do not create a global theorem asserting that all unspecified logarithms have base two.
3. The ceiling identity for r belongs to eq-6, and the exact T ceiling theorem belongs to the Section 3 task.

**Named dependencies.** `QuarticQuery.logb_mValue`; `QuarticQuery.Lvalue`; `QuarticQuery.Fkm`; `QuarticQuery.Tournament.Tval`.

**Proof route.** same.

**Correction.** None proposed.

**Source and earlier review.**

- paper/extracted.md:117-123 (Section 1.3)
- repository/lean/QuarticQuery/Statement.lean:293-310 (Fkm and Lvalue)
- repository/lean/QuarticQuery/Results/Exponent.lean:300-305 (logb_mValue)
- repository/lean/QuarticQuery/Tournament/Ideal.lean:295-299 (Tval and epsval)

No mathematical correction requested for this row. Existing corpus evidence is none because this prose convention has no direct reviewed tie.

**Scope.** Choosing the base of log is a notation convention rather than a theorem. Its operational meaning is already explicit: Lvalue uses Real.logb 2, Fkm uses ell=2*t and r=40*t, and Tournament.Tval uses Nat.clog 2. The supplied theorem pins log_2(mValue t)=2*t; it does not claim a separate theorem about every permitted asymptotic change of base.

**Remaining obligation.** Fresh elaboration of the wrapper. The general prose convention needs no proof.

<!-- /passage:row-def-log-convention -->

## Supplemental statements

The following entries retain new quantitative forms and intermediate claims separately from the preprint’s records. Their complete signatures and supplied proof files are in `NEW_STATEMENTS.json`. All remain unelaborated.

<!-- passage:new-construction-explicit-family-constants -->

**Statement (`construction-explicit-family-constants`).** For k=l+1≥2, the fixed circuit forrCircuit(l,t) eventually realises P, has size≤forrConstant(k)m(log_2 m)^2, and its addressed total function satisfies Q≤budgetConst(k)sqrt(m)(log_2 m)^6 and R≥m^(2−1/k)/(400(log_2 m)^2), where m=4^t.

**Purpose.** Records the stronger explicit constants and named common circuit used to prove the original eq-2 without silently changing its existential formulation.

**Lean statement, unelaborated.**

```lean
theorem construction_family_named (l : ℕ) (hk : 2 ≤ l + 1) :
    ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
      CircuitRealises (Forrelation.forrCircuit l t) (P (l + 1) t) ∧
      (Forrelation.forrCircuit l t).size ≤
        Forrelation.forrConstant (l + 1) * mValue t * (2 * t) ^ 2 ∧
      (Q (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ) ≤
        (Upper.budgetConst (l + 1) : ℝ) * Real.sqrt (mValue t : ℝ) *
          (Real.logb 2 (mValue t : ℝ)) ^ 6 ∧
      (1 / 400 : ℝ) * Real.rpow (mValue t : ℝ) (2 - 1 / ((l + 1 : ℕ) : ℝ)) /
          (Real.logb 2 (mValue t : ℝ)) ^ 2 ≤
        (R (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ)
```

**Proof route and status.** Short assembly of existing declarations; Forrelation input uses the existing alternative fixed-k proof. Full proof text is supplied in ConstructionFamily.lean, unelaborated.

<!-- /passage:new-construction-explicit-family-constants -->

<!-- passage:new-construction-exponent-infimum-well-defined -->

**Statement (`construction-exponent-infimum-well-defined`).** The set of exponents satisfying UniversalPower is nonempty and bounded below by zero.

**Purpose.** Makes the nonvacuity of the real infimum in equation (1) explicit.

**Lean statement, unelaborated.**

```lean
theorem construction_exponent_set_wellDefined :
    ({α : ℝ | UniversalPower α}).Nonempty ∧
      BddBelow {α : ℝ | UniversalPower α}
```

**Proof route and status.** Use universalPower_four for a witness and the nonnegative-exponent clause for the lower bound. Existing universal bound uses the complexitylib route. Supplied proof text is unelaborated.

<!-- /passage:new-construction-exponent-infimum-well-defined -->

<!-- passage:new-r2-forrelation-affine-comparison -->

**Statement (`r2-forrelation-affine-comparison`).** For fixed k>=2,c>0,A>=0,B>=0, every eventually positive denominator Lambda bounded above by A+Bt satisfies m^(1-1/k)/(2t)^2 < c(m/Lambda)^(1-1/k), for all sufficiently large t.

**Purpose.** Retains the actual auxiliary comparison used to derive claim-bs-to-L.

**Lean statement, unelaborated.**

```lean
theorem construction_affine_comparison {k : ℕ} (hk : 2 ≤ k)
    {c A B : ℝ} (hc : 0 < c) (hA : 0 ≤ A) (hB : 0 ≤ B) :
    ∃ t₀ : ℕ, 1 ≤ t₀ ∧ ∀ t : ℕ, t₀ ≤ t →
      ∀ Λ : ℝ, 1 ≤ Λ → Λ ≤ A + B * t →
        (mValue t : ℝ) ^ (1 - 1 / (k : ℝ)) / (2 * (t : ℝ)) ^ 2 <
          c * ((mValue t : ℝ) / Λ) ^ (1 - 1 / (k : ℝ))
```

**Proof route and status.** Proof body supplied in lean/QuarticQuery/Paper/ConstructionForrelationComparison.lean. Source only: unelaborated, no compilation or comparator run.

<!-- /passage:new-r2-forrelation-affine-comparison -->

<!-- passage:new-r2-forrelation-unfloored-comparison -->

**Statement (`r2-forrelation-unfloored-comparison`).** For fixed k>=2 and c>0, eventually L <= m^(1-1/k)/(2t)^2 < c k^(-29)(m/log_2(km))^(1-1/k), where m=4^t.

**Purpose.** Records the stronger unfloored middle inequality, omitted from the candidate Section2 declaration type.

**Lean statement, unelaborated.**

```lean
theorem construction_bs_comparison_chain (k : ℕ) (hk : 2 ≤ k)
    (c : ℝ) (hc : 0 < c) :
    ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
      (Lvalue k t : ℝ) ≤ (mValue t : ℝ) ^ (1 - 1 / (k : ℝ)) /
        (Real.logb 2 (mValue t : ℝ)) ^ 2 ∧
      (mValue t : ℝ) ^ (1 - 1 / (k : ℝ)) /
          (Real.logb 2 (mValue t : ℝ)) ^ 2 <
        c * (k : ℝ) ^ (-29 : ℤ) *
          ((mValue t : ℝ) / Real.logb 2 ((k : ℝ) * (mValue t : ℝ))) ^
            (1 - 1 / (k : ℝ))
```

**Proof route and status.** Proof body supplied in lean/QuarticQuery/Paper/ConstructionForrelationComparison.lean. Source only: unelaborated, no compilation or comparator run.

<!-- /passage:new-r2-forrelation-unfloored-comparison -->

<!-- passage:new-r2-forrelation-generic-query-count -->

**Statement (`r2-forrelation-generic-query-count`).** For k>=1 the projection test has coherent sampler cost k reads and generic physical bit-query cost 2k, with success probability Phi^2 and the exact promise gap.

**Purpose.** Separates the available compiler count from the paper tight local phase count.

**Lean statement, unelaborated.**

```lean
theorem construction_projection_test (k t : ℕ) (hk : 1 ≤ k) :
    (∀ z : BitInput (ForrelationCoord k t),
      successProb z = Phi k t z ^ 2 ∧
      (P k t z = some true → delta k ^ 2 ≤ successProb z) ∧
      (P k t z = some false → successProb z ≤ delta k ^ 2 / 4)) ∧
    Samples k (fun (z : BitInput (ForrelationCoord k t)) b => bern (Phi k t z ^ 2) b) ∧
    (∀ [Inhabited (ForrelationCoord k t)],
      Runs (2 * k) (fun (z : BitInput (ForrelationCoord k t)) b => bern (Phi k t z ^ 2) b))
```

**Proof route and status.** Proof body supplied in lean/QuarticQuery/Paper/ConstructionForrelationQuantum.lean. Source only: unelaborated, no compilation or comparator run.

<!-- /passage:new-r2-forrelation-generic-query-count -->

<!-- passage:new-r2-forrelation-explicit-circuit-costs -->

**Statement (`r2-forrelation-explicit-circuit-costs`).** For k=l+1 and t>=1 the explicit circuit has widthTop+1 <= (3l+5)(2t), Walsh gate cost <= (2t)m(6w+1), the recorded layer bound and final numerator bound, realizes P, and has at most forrConstant(k)m(2t)^2 gates.

**Purpose.** Records quantitative strengthening and the actual modular endpoint.

**Lean statement, unelaborated.**

```lean
theorem construction_circuit_costs (l t : ℕ) (ht : 1 ≤ t) :
    widthTop l t + 1 ≤ (3 * l + 5) * (2 * t) ∧
    (∀ w : ℕ, whtCost w (2 * t) ≤ (2 * t) * mValue t * (6 * w + 1)) ∧
    (∀ n w : ℕ, layerCost n w l ≤
      1 + (l + 1) * (whtCost w n + 2 ^ n * (6 * w))) ∧
    (∀ x : BitInput (ForrelationCoord (l + 1) t),
      |forrelationNumerator (l + 1) t x| ≤ forrelationDenominator (l + 1) t) ∧
    CircuitRealises (forrCircuit l t) (P (l + 1) t) ∧
    (forrCircuit l t).size ≤
      forrConstant (l + 1) * mValue t * (2 * t) ^ 2
```

**Proof route and status.** Proof body supplied in lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean. Source only: unelaborated, no compilation or comparator run.

<!-- /passage:new-r2-forrelation-explicit-circuit-costs -->

<!-- passage:new-r2-forrelation-product-scaling -->

**Statement (`r2-forrelation-product-scaling`).** For a list of k>=1 diagonals, replacing each intervening A by cA multiplies the alternating matrix word by c^(k-1).

**Purpose.** Makes the normalization proof recoverable from an explicit existing-vocabulary matrix identity.

**Lean statement, unelaborated.**

```lean
theorem construction_alternate_smul {n : Type} [Fintype n] [DecidableEq n]
    (c : ℝ) (A : Matrix n n ℝ) (k : ℕ) (hk : 1 ≤ k)
    (D : Fin k → Matrix n n ℝ) :
    alternate (c • A) (List.ofFn D) = c ^ (k - 1) • alternate A (List.ofFn D)
```

**Proof route and status.** Proof body supplied in lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean. Source only: unelaborated, no compilation or comparator run.

<!-- /passage:new-r2-forrelation-product-scaling -->

<!-- passage:new-new-r2-K-explicit -->

**Statement (`new-r2-K-explicit`).** If t≥1 and S≤A·mValue(t)·(2t)^2, then the local-test count is at most (42+20A)·mValue(t)·(2t)^3.

**Purpose.** Exports a reusable finite constant behind the existing O_k(m log³m) row.

**Lean statement, unelaborated.**

```lean
theorem construction_K_bound (t S A : ℕ) (ht : 1 ≤ t)
    (hS : S ≤ A * mValue t * (2 * t) ^ 2) :
    Fintype.card (TestIndex (2 * t) (40 * t) S) ≤
      (42 + 20 * A) * mValue t * (2 * t) ^ 3
```

**Proof route and status.** The arithmetic is already present locally in Upper/Bound.lean:137–163; this is an explicit reusable interface, with no novelty claim.

<!-- /passage:new-new-r2-K-explicit -->

<!-- passage:new-new-r2-exact-law-support -->

**Statement (`new-r2-exact-law-support`).** If measuring a finite state through a Boolean output label has the point-mass law at b, then every basis amplitude whose output label is different from b is zero.

**Purpose.** Turns an exact sampler distribution into the support statement needed to evaluate local tests coherently.

**Lean statement, unelaborated.**

```lean
theorem construction_support_of_exact_law {Z : Type} [Fintype Z]
    (ψ : Reg Z) (out : Z → Bool) (b : Bool)
    (h : ∀ c, pt b c = lawOf ψ out c) (z : Z) (hz : out z ≠ b) :
    ψ.ofLp z = 0
```

**Proof route and status.** Elementary nonnegative finite-sum argument: each wrong squared amplitude is bounded by the zero probability of its output label.

<!-- /passage:new-new-r2-exact-law-support -->

<!-- passage:new-new-r2-arbitrary-index-coherence -->

**Statement (`new-r2-arbitrary-index-coherence`).** A finite family of exact Boolean samplers with a common n-read bound has a single direct-sum n-read unitary implementation that evaluates every index coherently for arbitrary complex index coefficients and has zero amplitude at every wrong output label.

**Purpose.** The existing uniform-index Samples endpoint does not by itself state the arbitrary-superposition clause of Lemma 2.2(ii).

**Lean statement, unelaborated.**

```lean
theorem construction_controlled_exact_samples {ι Γ : Type} [Fintype Γ]
    (n : ℕ) (g : BitInput ι → Γ → Bool)
    (h : ∀ e : Γ, Samples n fun x b => pt (g x e) b) :
    ∃ (Z : Γ → Type) (instZ : ∀ e, Fintype (Z e)),
      let _ := instZ
      ∃ (o : ∀ e, Z e) (out : ∀ e, Z e → Bool)
        (F : ∀ e, BitInput ι → Reg (Z e) ≃ₗᵢ[ℂ] Reg (Z e)),
        (∀ e, IsCirc n (F e)) ∧
        IsCirc n (fun x => sigmaOp fun e => F e x) ∧
        (∀ (x : BitInput ι) (a : Γ → ℂ) (e : Γ),
          slice e (sigmaOp (fun e => F e x) ((WithLp.toLp 2 (fun p => a p.1 * (rket (o p.1)).ofLp p.2)))) =
            a e • F e x (rket (o e))) ∧
        (∀ (x : BitInput ι) (e : Γ) (z : Z e),
          out e z ≠ g x e → (F e x (rket (o e))).ofLp z = 0)
```

**Proof route and status.** Uses the existing IsCirc.sigma direct-sum closure and linearity. Its read count becomes at most 2n physical bit queries under compile_circ; no clean-XOR claim is made.

<!-- /passage:new-new-r2-arbitrary-index-coherence -->

<!-- passage:new-new-r2-pointer-essential-coordinates -->

**Statement (`new-r2-pointer-essential-coordinates`).** For the Boolean lookup function that decodes an ℓ-bit pointer and reads the selected bit of a 2^ℓ-bit target array, every pointer or target coordinate is essential.

**Purpose.** Provides a direct witness proof for the corrected ledger’s distinction between adaptive query depth and fixed coordinate dependence.

**Lean statement, unelaborated.**

```lean
theorem construction_pointer_every_coordinate (ℓ : ℕ)
    (q : Fin ℓ ⊕ Column ℓ) :
    ∃ x y : BitInput (Fin ℓ ⊕ Column ℓ),
      (∀ p, p ≠ q → x p = y p) ∧
        x (.inr (pointerEquiv ℓ (fun b => x (.inl b)))) ≠ y (.inr (pointerEquiv ℓ (fun b => y (.inl b))))
```

**Proof route and status.** A stronger quantified schema for the ledger’s already-adjudicated support qualification. The actual local pointer test is its negation after the explicit physical-coordinate substitution.

<!-- /passage:new-new-r2-pointer-essential-coordinates -->

<!-- passage:new-new-r2-pointer-physical-support -->

**Statement (`new-r2-pointer-physical-support`).** For a fixed pointer-test index at a fixed column and address, each of its ℓ pointer-word coordinates and m possible target-column coordinates is essential on full physical inputs: two inputs agree at every other physical location and yield different local-test outputs. These ℓ+m locations are pairwise distinct.

**Purpose.** Closes the earlier qualification that only the separate lookup schema, plus its definitional substitution, had formal support witnesses.

**Lean statement, unelaborated.**

```lean
theorem construction_pointer_every_physical_coordinate {κ : Type} (C : Circuit κ)
    (ℓ r : ℕ) (i : Column ℓ) (s : Address r) (e : Fin (2 ^ ℓ - 1))
    (q : Fin ℓ ⊕ Column ℓ) :
    ∃ X Y : BitInput (BitLoc ℓ r C.size κ),
      (∀ p, p ≠ (match q with
        | .inl b => .inr (.inr (.inl ⟨i, (s, otherColumn i e, b)⟩))
        | .inr j => .inl ((otherColumn i e).val, j)) → X p = Y p) ∧
        localTest C ℓ r X i s (.inr (.inl e)) ≠
          localTest C ℓ r Y i s (.inr (.inl e))
```

**Proof route and status.** The physical-coordinate map is injective because pointer and target locations occupy separate BitLoc branches. Extend the existing schema witnesses using a chosen inverse on the injection range, set all other coordinates false, and use Boolean-negation injectivity.

<!-- /passage:new-new-r2-pointer-physical-support -->

<!-- passage:new-r2-phase-kickback-state -->

**Statement (`r2-phase-kickback-state`).** On the answer-qubit minus subspace, one application of the actual bit oracle multiplies each index amplitude by the sign of the queried input bit, with arbitrary entangled workspace.

**Purpose.** Makes the local physical implementation in claim-proj-prob explicit without attributing a one-query cost to the generic two-query compiler.

**Lean statement, unelaborated.**

```lean
theorem construction_bitOracle_phase_kickback
    (x : BitInput ι) (ψ : State ι w)
    (hminus : ∀ (i : ι) (z : Fin (w + 1)),
      ψ.ofLp (i, true, z) = -ψ.ofLp (i, false, z))
    (p : Basis ι w) :
    (bitOracle x ψ).ofLp p =
      (if x p.1 then (-1 : ℂ) else 1) * ψ.ofLp p
```

**Proof route and status.** Proof text supplied in lean/QuarticQuery/Paper/ConstructionPhase.lean. Unelaborated. Local one-call identity; no complete Runs k witness is asserted.

<!-- /passage:new-r2-phase-kickback-state -->

<!-- passage:new-r2-phase-kickback-preservation -->

**Statement (`r2-phase-kickback-preservation`).** The bit oracle preserves the normalized minus-answer subspace used for phase kickback.

**Purpose.** Records that the phase-query answer ancilla can be retained for later phase queries.

**Lean statement, unelaborated.**

```lean
theorem construction_bitOracle_phase_preserves
    (x : BitInput ι) (ψ : State ι w)
    (hminus : ∀ (i : ι) (z : Fin (w + 1)),
      ψ.ofLp (i, true, z) = -ψ.ofLp (i, false, z))
    (hunit : ‖ψ‖ = 1) :
    ‖bitOracle x ψ‖ = 1 ∧
      ∀ (i : ι) (z : Fin (w + 1)),
        (bitOracle x ψ).ofLp (i, true, z) =
          -(bitOracle x ψ).ofLp (i, false, z)
```

**Proof route and status.** Proof text supplied in lean/QuarticQuery/Paper/ConstructionPhase.lean. Unelaborated. Local one-call identity; no complete Runs k witness is asserted.

<!-- /passage:new-r2-phase-kickback-preservation -->

<!-- passage:new-r2-integer-sum-bound -->

**Statement (`r2-integer-sum-bound`).** If every term of a finite integer sum of length a has absolute value at most B, the sum has absolute value at most a B.

**Purpose.** Provides the induction step for the ideal integer walk and its partial sums.

**Lean statement, unelaborated.**

```lean
theorem construction_abs_sum_range_le (a : ℕ) (v : ℕ → ℤ) (B : ℤ)
    (hv : ∀ j, j < a → |v j| ≤ B) :
    |∑ j ∈ range a, v j| ≤ (a : ℤ) * B
```

**Proof route and status.** Proof text supplied in lean/QuarticQuery/Paper/ConstructionArithmetic.lean. Unelaborated. The ideal arithmetic statements do not identify every actual modular register with an unbounded signed integer.

<!-- /passage:new-r2-integer-sum-bound -->

<!-- passage:new-r2-integer-walk-bound -->

**Statement (`r2-integer-walk-bound`).** For sign inputs bounded in absolute value by one, the ideal unnormalized Walsh walk after l transforms on m=2^n coordinates has each coordinate bounded by m^l.

**Purpose.** Supplies an explicit polynomial magnitude bound for the ideal arithmetic in the preprint.

**Lean statement, unelaborated.**

```lean
theorem construction_walkN_bound (n l : ℕ) (σ : ℕ → ℕ → ℤ)
    (hσ : ∀ h i, |σ h i| ≤ 1) (i : ℕ) :
    |walkN n l σ i| ≤ ((2 ^ n : ℕ) : ℤ) ^ l
```

**Proof route and status.** Proof text supplied in lean/QuarticQuery/Paper/ConstructionArithmetic.lean. Unelaborated. The ideal arithmetic statements do not identify every actual modular register with an unbounded signed integer.

<!-- /passage:new-r2-integer-walk-bound -->

<!-- passage:new-r2-integer-prefix-bound -->

**Statement (`r2-integer-prefix-bound`).** A prefix of length a in the final ideal signed sum has absolute value at most a m^l.

**Purpose.** Includes partial accumulators in the magnitude argument.

**Lean statement, unelaborated.**

```lean
theorem construction_walkN_prefix_bound (n l a : ℕ) (σ : ℕ → ℕ → ℤ)
    (hσ : ∀ h i, |σ h i| ≤ 1) :
    |∑ j ∈ range a, walkN n l σ j| ≤ (a : ℤ) * ((2 ^ n : ℕ) : ℤ) ^ l
```

**Proof route and status.** Proof text supplied in lean/QuarticQuery/Paper/ConstructionArithmetic.lean. Unelaborated. The ideal arithmetic statements do not identify every actual modular register with an unbounded signed integer.

<!-- /passage:new-r2-integer-prefix-bound -->

<!-- passage:new-r2-butterfly-block-bound -->

**Statement (`r2-butterfly-block-bound`).** An offset Walsh butterfly block of 2^q inputs, each bounded by B in absolute value, has absolute value at most 2^q B.

**Purpose.** Includes recursive transform blocks in the ideal arithmetic bound.

**Lean statement, unelaborated.**

```lean
theorem construction_butterfly_block_bound (q i offset : ℕ)
    (v : ℕ → ℤ) (B : ℤ)
    (hv : ∀ j, j < 2 ^ q → |v (offset + j)| ≤ B) :
    |∑ j ∈ range (2 ^ q), walshN q i j * v (offset + j)| ≤
      ((2 ^ q : ℕ) : ℤ) * B
```

**Proof route and status.** Proof text supplied in lean/QuarticQuery/Paper/ConstructionArithmetic.lean. Unelaborated. The ideal arithmetic statements do not identify every actual modular register with an unbounded signed integer.

<!-- /passage:new-r2-butterfly-block-bound -->
