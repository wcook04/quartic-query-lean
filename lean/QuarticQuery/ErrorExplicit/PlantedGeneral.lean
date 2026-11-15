module

public import QuarticQuery.ErrorExplicit.Defs
public import QuarticQuery.LowerBound.Planted.Main

/-!
# The planted lower bound at every error

`addressedF_not_RLe` (LowerBound/Planted/Main.lean) proves the classical lower bound
for the addressed function at error `1/3`. Its engine is the per-tree gap bound
`tree_gap_le`: for one deterministic tree of depth at most `G`, the acceptance
probabilities on the coupled planted and dummy inputs differ by at most
`G (2/m² + 1/(mL) + (2/3)^r)`, where `L` is any cap below `R f`.

Averaging that bound over the trees of an error-`e` program, and using that error
`e` forces acceptance at least `1 - e` on every planted input and at most `e` on
every dummy input, gives `1 - 2e ≤ G (2/m² + 1/(mL) + (2/3)^r)`. The hard
distribution and the direct-product bound are those of the `1/3` proof
(`exists_address_guess_bound`, which uses only `¬ RLe f L`); the error of the
inner problem stays `1/3`, and only the outer error changes.
-/

@[expose] public section

open Finset

namespace QuarticQuery.ErrorExplicit

open QuarticQuery

variable {κ : Type} [Fintype κ] [DecidableEq κ]

/-- The per-query discrepancy of the planted coupling with `m = 2^ℓ` columns, cap `L`
for each inner instance and address length `r`. -/
noncomputable def plantedRate (ℓ r L : ℕ) : ℝ :=
  2 / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 + 1 / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) + ((2 : ℝ) / 3) ^ r

theorem plantedRate_pos (ℓ r L : ℕ) : 0 < plantedRate ℓ r L := by
  unfold plantedRate
  have h1 : 0 < 2 / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 := by positivity
  have h2 : 0 ≤ 1 / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) := by positivity
  have h3 : 0 ≤ ((2 : ℝ) / 3) ^ r := by positivity
  linarith

/-- **General-error acceptance gap.** If the addressed function has an error-`e`
randomized program of depth at most `G`, the realising circuit is `C`, `1 ≤ L` and
`L` is not a `1/3`-error budget for the inner function `f`, then
`1 - 2e ≤ G · (2/m² + 1/(mL) + (2/3)^r)` with `m = 2^ℓ`. No assumption on `e`. -/
theorem one_sub_two_mul_le_of_RLeError (f : PartialBool κ) (C : Circuit κ)
    (hC : CircuitRealises C f) {ℓ r L G : ℕ} (hL : ¬ RLe f L) (hL1 : 1 ≤ L) {e : ℝ}
    (hG : RLeError (totalise (addressedF f C ℓ r)) e G) :
    1 - 2 * e ≤ (G : ℝ) * plantedRate ℓ r L := by
  obtain ⟨P, hP, hs⟩ := hG
  obtain ⟨μ, hμ0, hμ1, hdom, hguess⟩ := exists_address_guess_bound hL
  let tr : BitInput κ → Fin C.size → Bool := fun x => Classical.choose (hC.exists_transcript x)
  have htr : ∀ x, GateConsistent C x (tr x) := fun x =>
    Classical.choose_spec (hC.exists_transcript x)
  have hadd : ∀ x, P.success x true + P.success x false = 1 := fun x => by
    unfold RandomizedProgram.success
    rw [← sum_add_distrib, ← P.weight_sum]
    refine sum_congr rfl fun j _ => ?_
    cases (P.tree j).eval x <;> simp
  have hsucc : ∀ x, avg P.weight (fun k => ind ((P.tree k).eval x = true)) =
      P.success x true := fun x => by
    refine sum_congr rfl fun k _ => ?_
    beta_reduce
    by_cases h : (P.tree k).eval x = true
    · rw [ind_true h, if_pos h, mul_one]
    · rw [ind_false h, if_neg h, mul_zero]
  have h0 : ∀ (J : Column ℓ → Column ℓ) (A : Column ℓ → Fin r → BitInput κ),
      P.success (dummy J A) true ≤ e := fun J A => by
    have := hs (dummy J A) false (by rw [totalise, addressedF_dummy])
    linarith [hadd (dummy (S := C.size) J A)]
  have h1 : ∀ (J : Column ℓ → Column ℓ) (A : Column ℓ → Fin r → BitInput κ) (I : Column ℓ),
      prodW (prodW μ) A ≠ 0 → 1 - e ≤ P.success (planted f tr J A I) true := fun J A I hA =>
    hs _ true (by
      rw [totalise, addressedF_planted htr J A I fun h =>
        hdom _ (ne_zero_of_prodW_ne_zero (ne_zero_of_prodW_ne_zero hA I) h)])
  have hPU0 := prodW_nonneg (ι := Fin r) hμ0
  have hPU1 : ∑ U : Fin r → BitInput κ, prodW μ U = 1 := sum_prodW hμ1
  have hPA0 : ∀ A : Column ℓ → Fin r → BitInput κ, 0 ≤ prodW (prodW μ) A :=
    prodW_nonneg hPU0
  have hPA1 : ∑ A : Column ℓ → Fin r → BitInput κ, prodW (prodW μ) A = 1 := sum_prodW hPU1
  have hPJ0 : ∀ J : Column ℓ → Column ℓ, 0 ≤ prodW (unif ℓ) J := prodW_nonneg (unif_nonneg ℓ)
  have hPJ1 : ∑ J : Column ℓ → Column ℓ, prodW (unif ℓ) J = 1 := sum_prodW (sum_unif ℓ)
  set δ : ℝ := 2 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 + (G : ℝ) / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) +
    (G : ℝ) * ((2 : ℝ) / 3) ^ r with hδ
  have hδG : δ = (G : ℝ) * plantedRate ℓ r L := by
    rw [hδ, plantedRate]
    ring
  have hgap : ∀ k, coupledAvg (ℓ := ℓ) (r := r) μ (fun A J I =>
      ind ((P.tree k).eval (planted f tr J A I) = true) -
        ind ((P.tree k).eval (dummy J A) = true)) ≤ δ := fun k =>
    tree_gap_le tr hL1 hμ0 hμ1 hdom (fun U hU => hguess r U hU) (P.tree k)
      ((Finset.le_sup (f := fun j => (P.tree j).depth) (mem_univ k)).trans hP)
  have hmix := avg_le_const (fun k => (P.weight_pos k).le) P.weight_sum hgap
  have hlow : 1 - 2 * e ≤ avg P.weight fun k => coupledAvg (ℓ := ℓ) (r := r) μ (fun A J I =>
      ind ((P.tree k).eval (planted f tr J A I) = true) -
        ind ((P.tree k).eval (dummy J A) = true)) := by
    unfold coupledAvg
    rw [avg_comm]
    refine const_le_avg_of_ne hPA0 hPA1 fun A hA => ?_
    rw [avg_comm]
    refine const_le_avg_of_ne hPJ0 hPJ1 fun J _ => ?_
    rw [avg_comm]
    refine const_le_avg_of_ne (unif_nonneg ℓ) (sum_unif ℓ) fun I _ => ?_
    rw [avg_sub, hsucc, hsucc]
    linarith [h0 J A, h1 J A I hA]
  rw [← hδG]
  linarith

/-- **Theorem (T1): the planted lower bound at every nonnegative error.**
Let `f` be a partial Boolean function on a finite type, `C` any circuit realising
`f` (its size plays no part), `m = 2^ℓ` columns, address length `r`, and `L` an
integer with `1 ≤ L < R f` (the public `1/3`-error complexity of `f`). Then for
every error `0 ≤ e`,

  `(1 - 2e) / (2/m² + 1/(mL) + (2/3)^r) ≤ R_e(addressedF f C ℓ r)`.

For `e ≥ 1/2` the left side is `≤ 0` and the statement is trivial; the content is
`0 ≤ e < 1/2`. -/
theorem planted_lower_general (f : PartialBool κ) (C : Circuit κ) (hC : CircuitRealises C f)
    (ℓ r : ℕ) {L : ℕ} (hL1 : 1 ≤ L) (hLR : L < R f) {e : ℝ} (he : 0 ≤ e) :
    (1 - 2 * e) /
        (2 / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 + 1 / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) +
          ((2 : ℝ) / 3) ^ r) ≤
      (RError (totalise (addressedF f C ℓ r)) e : ℝ) := by
  have hnot : ¬ RLe f L := lt_R_iff.mp hLR L le_rfl
  have hpos := plantedRate_pos ℓ r L
  refine le_RError_of_forall he fun G hG => ?_
  have h := one_sub_two_mul_le_of_RLeError f C hC hnot hL1 hG
  exact (div_le_iff₀ (show (0 : ℝ) < 2 / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 +
    1 / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) + ((2 : ℝ) / 3) ^ r from hpos)).2 h

end QuarticQuery.ErrorExplicit
