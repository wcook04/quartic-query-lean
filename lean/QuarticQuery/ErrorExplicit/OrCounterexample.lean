module

public import QuarticQuery.ErrorExplicit.QuantumMargin
public import QuarticQuery.LowerBound.Planted.Coupling
public import QuarticQuery.LowerBound.Planted.Average

/-!
# No error-uniform constant as the quantum error approaches `1/2`

For `N ≥ 2` let `OR_N` be the OR of `N` bits and `d_N = (N-1)/(2N-1) < 1/2`.
Query a uniform coordinate; if it is one output one, otherwise output one with
probability `d_N`. Error on the zero input is exactly `d_N`; on a nonzero input the
success probability is at least `1/N + (1 - 1/N) d_N = 1 - d_N`. Run coherently by the
project's sampler compiler (`Samples.runs`, two bit queries per read) this gives
`Q_{d_N}(OR_N) ≤ 2`. (The return's `≤ 1` assumes a one-query implementation; the
factor two is the compiler's and is immaterial here.)

Classically, `R(OR_N) ≥ N/3`: on a tree of depth `T`, the inputs `0` and `e_i` give the
same output unless `i` lies on the zero-input path, so averaging over `i` gives
`2/3 ≤ 1/3 + T/N`.

Hence no constant `C` satisfies `R(f) ≤ C (1 + Q_d(f))^4` for all `d < 1/2`.
-/

@[expose] public section

open Finset

namespace QuarticQuery.ErrorExplicit

open QuarticQuery QuarticQuery.Upper

/-- The OR of `N` bits. -/
def orF (N : ℕ) : TotalBool (Fin N) := fun x => decide (∃ i, x i = true)

/-- The error at which one read suffices: `d_N = (N-1)/(2N-1)`. -/
noncomputable def orError (N : ℕ) : ℝ := ((N : ℝ) - 1) / (2 * (N : ℝ) - 1)

theorem orError_nonneg {N : ℕ} (hN : 1 ≤ N) : 0 ≤ orError N := by
  have : (1 : ℝ) ≤ N := by exact_mod_cast hN
  unfold orError
  apply div_nonneg <;> linarith

theorem orError_lt_half {N : ℕ} (hN : 1 ≤ N) : orError N < 1 / 2 := by
  have : (1 : ℝ) ≤ N := by exact_mod_cast hN
  unfold orError
  rw [div_lt_iff₀ (by linarith)]
  linarith

theorem orError_mul {N : ℕ} (hN : 1 ≤ N) :
    orError N * (2 * (N : ℝ) - 1) = (N : ℝ) - 1 := by
  have : (1 : ℝ) ≤ N := by exact_mod_cast hN
  unfold orError
  exact div_mul_cancel₀ _ (ne_of_gt (by linarith))

/-! ## The one-read sampler -/

/-- The sampler for `OR_N` has error at most `d` whenever `N - 1 ≤ d (2N - 1)`. -/
theorem orF_QLeError_of (N : ℕ) [Inhabited (Fin N)] (hN : 1 ≤ N) {d : ℝ} (hd0 : 0 ≤ d)
    (hd1 : d ≤ 1) (hdN : (N : ℝ) - 1 ≤ d * (2 * (N : ℝ) - 1)) :
    QLeError (totalise (orF N)) d 2 := by
  classical
  have hN0 : (0 : ℝ) < (N : ℝ) := by
    have : (1 : ℝ) ≤ N := by exact_mod_cast hN
    linarith
  let prob : Fin N × Bool → ℝ := fun p => (N : ℝ)⁻¹ * bern d p.2
  have hp0 : ∀ p, 0 ≤ prob p := by
    rintro ⟨i, c⟩
    have : 0 ≤ bern d c := by cases c <;> simp [bern] <;> linarith
    exact mul_nonneg (by positivity) this
  have hrow : ∀ i : Fin N, ∑ c : Bool, prob (i, c) = (N : ℝ)⁻¹ := fun i => by
    rw [Fintype.sum_bool]
    simp only [prob, bern, eq_self_iff_true, if_true, Bool.false_eq_true, if_false]
    ring
  have hp1 : ∑ p, prob p = 1 := by
    rw [Fintype.sum_prod_type]
    simp only [hrow]
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul,
      mul_inv_cancel₀ hN0.ne']
  have hg : Samples (ι := Fin N) 0 fun _ p => prob p := Samples.gate hp0 hp1
  have hK : ∀ p : Fin N × Bool, Samples 1
      fun (x : BitInput (Fin N)) b => ∑ c, pt (x p.1) c * pt (c || p.2) b :=
    fun p => (Samples.query p.1).map fun c => c || p.2
  have hS := (hg.bind hK).runs
  have hL : ∀ (x : BitInput (Fin N)) (b : Bool),
      (∑ p, prob p * ∑ c, pt (x p.1) c * pt (c || p.2) b) =
        ∑ i, (N : ℝ)⁻¹ * ((1 - d) * pt (x i) b + d * pt true b) := by
    intro x b
    rw [Fintype.sum_prod_type]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [sum_pt_mul]
    rw [Fintype.sum_bool]
    simp only [prob, bern, eq_self_iff_true, if_true, Bool.false_eq_true, if_false, Bool.or_false,
      Bool.or_true]
    ring
  refine (Runs.toQLeError hS (orF N) fun x => ?_).mono (by norm_num)
  beta_reduce
  rw [hL]
  cases hx : orF N x with
  | false =>
    have hall : ∀ i, x i = false := by
      intro i
      by_contra h
      have : orF N x = true := by
        simp only [orF, decide_eq_true_eq]
        exact ⟨i, by simpa using h⟩
      rw [hx] at this
      exact Bool.noConfusion this
    simp only [hall, pt_self, pt_of_ne (show true ≠ false by decide), mul_one, mul_zero,
      add_zero]
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, ← mul_assoc,
      mul_inv_cancel₀ hN0.ne', one_mul]
  | true =>
    obtain ⟨j, hj⟩ : ∃ j, x j = true := by simpa [orF] using hx
    simp only [pt_self, mul_one]
    have hsplit : ∑ i, (N : ℝ)⁻¹ * ((1 - d) * pt (x i) true + d) =
        d + (N : ℝ)⁻¹ * (1 - d) * ∑ i, pt (x i) true := by
      rw [Finset.mul_sum]
      have : ∑ i, (N : ℝ)⁻¹ * ((1 - d) * pt (x i) true + d) =
          ∑ i, ((N : ℝ)⁻¹ * d + (N : ℝ)⁻¹ * (1 - d) * pt (x i) true) :=
        Finset.sum_congr rfl fun i _ => by ring
      rw [this, Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
        nsmul_eq_mul, ← mul_assoc, mul_inv_cancel₀ hN0.ne', one_mul]
    rw [hsplit]
    have hone : 1 ≤ ∑ i, pt (x i) true := by
      have := Finset.single_le_sum (f := fun i => pt (x i) true) (fun i _ => pt_nonneg _ _)
        (Finset.mem_univ j)
      simpa [hj, pt_self] using this
    have hc : 0 ≤ (N : ℝ)⁻¹ * (1 - d) := mul_nonneg (by positivity) (by linarith)
    have hlow : d + (N : ℝ)⁻¹ * (1 - d) ≤ d + (N : ℝ)⁻¹ * (1 - d) * ∑ i, pt (x i) true := by
      nlinarith
    refine le_trans ?_ hlow
    -- `1 - d ≤ d + (1 - d)/N` is `N - 1 ≤ d (2N - 1)`.
    have key : (N : ℝ) * (1 - d) ≤ (N : ℝ) * (d + (N : ℝ)⁻¹ * (1 - d)) := by
      rw [mul_add, ← mul_assoc, mul_inv_cancel₀ hN0.ne', one_mul]
      nlinarith
    exact le_of_mul_le_mul_left key hN0

/-- **`Q_{d_N}(OR_N) ≤ 2`** for `N = n + 2`. -/
theorem orF_QLeError (n : ℕ) : QLeError (totalise (orF (n + 2))) (orError (n + 2)) 2 := by
  have h1 : 1 ≤ n + 2 := by omega
  exact orF_QLeError_of (n + 2) h1 (orError_nonneg h1)
    ((orError_lt_half h1).le.trans (by norm_num)) (orError_mul h1).ge

theorem orF_QError_le (n : ℕ) : QError (totalise (orF (n + 2))) (orError (n + 2)) ≤ 2 :=
  QError_le_of_QLeError (orF_QLeError n)

/-! ## The classical lower bound -/

/-- One tree: `∑_i [T(e_i) = 1] ≤ N [T(0) = 1] + depth T`. -/
theorem sum_ind_unit_le {N : ℕ} (T : QueryTree (Fin N)) :
    ∑ i : Fin N, ind (T.eval (fun j => decide (j = i)) = true) ≤
      (N : ℝ) * ind (T.eval (fun _ => false) = true) + T.depth := by
  classical
  have hpt : ∀ i : Fin N, ind (T.eval (fun j => decide (j = i)) = true) ≤
      ind (T.eval (fun _ => false) = true) + (if i ∈ T.path (fun _ => false) then 1 else 0) := by
    intro i
    have h1 := ind_le_one (T.eval (fun j => decide (j = i)) = true)
    have h2 := ind_nonneg (T.eval (fun _ => false) = true)
    by_cases he : T.eval (fun _ => false) = T.eval (fun j => decide (j = i))
    · rw [← he]
      have : (0 : ℝ) ≤ (if i ∈ T.path (fun _ => false) then 1 else 0) := by
        split_ifs <;> norm_num
      linarith
    · have hi : i ∈ T.path (fun _ => false) := by
        obtain ⟨q, hq, hne⟩ := T.exists_mem_path_ne he
        have hqi : q = i := by
          by_contra h
          exact hne (by simp [h])
        exact hqi ▸ hq
      rw [if_pos hi]
      linarith
  refine (Finset.sum_le_sum fun i _ => hpt i).trans ?_
  rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul,
    Finset.sum_boole]
  have hcard : ((univ.filter fun i => i ∈ T.path (fun _ => false)).card : ℝ) ≤ T.depth := by
    have h1 : (univ.filter fun i => i ∈ T.path (fun _ => false)) ⊆
        (T.path (fun _ => false)).toFinset := fun i hi => by simpa using hi
    have h2 := (Finset.card_le_card h1).trans ((T.path _).toFinset_card_le.trans
      (T.length_path_le _))
    exact_mod_cast h2
  linarith

/-- **`R(OR_N) ≥ N/3`**: every `1/3`-error budget for `OR_N` is at least `N/3`. -/
theorem le_three_mul_of_RLe_orF {N T : ℕ} (h : RLe (totalise (orF N)) T) :
    (N : ℝ) ≤ 3 * T := by
  classical
  obtain ⟨P, hP, hs⟩ := h
  have hadd : ∀ x, P.success x true + P.success x false = 1 := fun x => by
    unfold RandomizedProgram.success
    rw [← sum_add_distrib, ← P.weight_sum]
    refine sum_congr rfl fun j _ => ?_
    cases (P.tree j).eval x <;> simp
  have hsucc : ∀ x, P.success x true = ∑ k, P.weight k * ind ((P.tree k).eval x = true) :=
    fun x => by
      refine sum_congr rfl fun k _ => ?_
      by_cases h : (P.tree k).eval x = true
      · rw [ind_true h, if_pos h, mul_one]
      · rw [ind_false h, if_neg h, mul_zero]
  have h0 : P.success (fun _ => false) true ≤ 1 / 3 := by
    have := hs (fun _ => false) false (by simp [totalise, orF])
    linarith [hadd (fun _ => false)]
  have h1 : ∀ i : Fin N, 2 / 3 ≤ P.success (fun j => decide (j = i)) true := fun i =>
    hs (fun j => decide (j = i)) true (by simp [totalise, orF])
  have hsum : (N : ℝ) * (2 / 3) ≤ ∑ i : Fin N, P.success (fun j => decide (j = i)) true := by
    have := Finset.sum_le_sum fun i (_ : i ∈ (univ : Finset (Fin N))) => h1 i
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul] at this
    exact this
  have hupper : ∑ i : Fin N, P.success (fun j => decide (j = i)) true ≤
      (N : ℝ) * P.success (fun _ => false) true + T := by
    simp only [hsucc]
    rw [Finset.sum_comm]
    have hw : ∀ k, ∑ i : Fin N, P.weight k * ind ((P.tree k).eval (fun j => decide (j = i)) = true)
        ≤ P.weight k * ((N : ℝ) * ind ((P.tree k).eval (fun _ => false) = true) + T) :=
      fun k => by
        rw [← Finset.mul_sum]
        refine mul_le_mul_of_nonneg_left ?_ (P.weight_pos k).le
        have hd : ((P.tree k).depth : ℝ) ≤ T := by
          exact_mod_cast (Finset.le_sup (f := fun j => (P.tree j).depth) (mem_univ k)).trans hP
        have := sum_ind_unit_le (P.tree k)
        linarith
    refine (Finset.sum_le_sum fun k _ => hw k).trans (le_of_eq ?_)
    calc ∑ k, P.weight k * ((N : ℝ) * ind ((P.tree k).eval (fun _ => false) = true) + T)
        = ∑ k, ((N : ℝ) * (P.weight k * ind ((P.tree k).eval (fun _ => false) = true)) +
            P.weight k * T) := Finset.sum_congr rfl fun k _ => by ring
      _ = (N : ℝ) * ∑ k, P.weight k * ind ((P.tree k).eval (fun _ => false) = true) +
            (∑ k, P.weight k) * T := by
          rw [Finset.sum_add_distrib, Finset.mul_sum, Finset.sum_mul]
      _ = _ := by rw [P.weight_sum, one_mul]
  have hN : (0 : ℝ) ≤ N := Nat.cast_nonneg N
  nlinarith [mul_le_mul_of_nonneg_left h0 hN]

/-- **Theorem (T4, counterexample).** No constant `C` makes `R(f) ≤ C (1 + Q_d(f))^4`
hold for all total `f` and all quantum errors `0 ≤ d < 1/2` (here `R` is the public
`1/3`-error randomized complexity). The witnesses are `OR_N` at `d_N = (N-1)/(2N-1)`. -/
theorem no_error_uniform_constant :
    ¬ ∃ C : ℝ, ∀ d : ℝ, 0 ≤ d → d < 1 / 2 → ∀ n : ℕ, 1 ≤ n → ∀ f : TotalBool (Fin n),
      (R (totalise f) : ℝ) ≤ C * (1 + (QError (totalise f) d : ℝ)) ^ 4 := by
  rintro ⟨C, hC⟩
  obtain ⟨n, hn⟩ := exists_nat_gt (243 * |C|)
  have hb := hC (orError (n + 2)) (orError_nonneg (by omega)) (orError_lt_half (by omega))
    (n + 2) (by omega) (orF (n + 2))
  have hR : ((n + 2 : ℕ) : ℝ) ≤ 3 * R (totalise (orF (n + 2))) :=
    le_three_mul_of_RLe_orF (RLe_R _)
  have hQ : (QError (totalise (orF (n + 2))) (orError (n + 2)) : ℝ) ≤ 2 := by
    exact_mod_cast orF_QError_le n
  have hQ0 : (0 : ℝ) ≤ QError (totalise (orF (n + 2))) (orError (n + 2)) := Nat.cast_nonneg _
  have hpow : (1 + (QError (totalise (orF (n + 2))) (orError (n + 2)) : ℝ)) ^ 4 ≤ 81 := by
    have h3 : (1 + (QError (totalise (orF (n + 2))) (orError (n + 2)) : ℝ)) ≤ 3 := by linarith
    calc _ ≤ (3 : ℝ) ^ 4 := pow_le_pow_left₀ (by linarith) h3 4
      _ = 81 := by norm_num
  have hCb : C * (1 + (QError (totalise (orF (n + 2))) (orError (n + 2)) : ℝ)) ^ 4 ≤
      |C| * 81 := by
    have h0 : 0 ≤ (1 + (QError (totalise (orF (n + 2))) (orError (n + 2)) : ℝ)) ^ 4 := by
      positivity
    calc _ ≤ |C| * (1 + (QError (totalise (orF (n + 2))) (orError (n + 2)) : ℝ)) ^ 4 :=
          mul_le_mul_of_nonneg_right (le_abs_self C) h0
      _ ≤ |C| * 81 := mul_le_mul_of_nonneg_left hpow (abs_nonneg C)
  push_cast at hR
  linarith

end QuarticQuery.ErrorExplicit
