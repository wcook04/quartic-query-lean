module

public import QuarticQuery.ErrorExplicit.PlantedGeneral
public import QuarticQuery.ErrorExplicit.QuantumMargin
public import QuarticQuery.ForrelationLower.Uniform

/-!
# The family `F_{k,m}` with explicit error and one logarithm

Classical side. The auxiliary cap in the planted argument is not part of the
function. Taking it to be `L = ⌊H⌋` with
`H = 2 m^(1-1/k) / (18225 k² ln(4km))`, the uniform Forrelation bound
`forrelation_lower_uniform_sharp` gives `L < R(P k t)`, and
`uniform_budget_floor_bounds` (with `H = 256 X`) gives `H ≥ 512`, hence `L ≥ H/2`.
With `ℓ = 2t`, `r = 40t` the planted rate is at most `4/(mL)`, and the general-error
planted bound gives

  `R_e(F_{k,m}[C]) ≥ (1 - 2e) m L / 4 ≥ (1 - 2e) m^(2-1/k) / (72900 k² ln(4km))`

for every circuit `C` realising `P k t`, `k ≥ 2`, `t ≥ 41`, `15k + 2 ≤ 2t`, `0 ≤ e`.

Quantum side: `QuantumMargin.QError_Fkm_le` for the circuit `forrCircuit (k-1) t`.
-/

@[expose] public section

namespace QuarticQuery.ErrorExplicit

open QuarticQuery QuarticQuery.Upper QuarticQuery.Forrelation

/-- The auxiliary cap `H_{k,t} = 2 m^(1-1/k) / (18225 k² ln(4km))`, `m = 4^t`. -/
noncomputable def sharpBudget (k t : ℕ) : ℝ :=
  (2 / 18225 : ℝ) * Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
    ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ)))

/-- The properties of the cap `⌊H_{k,t}⌋` used by the family bound. -/
theorem sharpCap_bounds (k t : ℕ) (hk : 2 ≤ k) (ht : 41 ≤ t) (hkt2 : 15 * k + 2 ≤ 2 * t) :
    1 ≤ ⌊sharpBudget k t⌋₊ ∧ ⌊sharpBudget k t⌋₊ ≤ mValue t ∧
      sharpBudget k t / 2 ≤ (⌊sharpBudget k t⌋₊ : ℝ) ∧
      ⌊sharpBudget k t⌋₊ < R (P k t) := by
  have hkt : k ≤ t := by omega
  have hk2 : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hm1 : (1 : ℝ) ≤ (mValue t : ℝ) := by
    have : 1 ≤ mValue t := Nat.one_le_two_pow
    exact_mod_cast this
  have hX2 : (2 : ℝ) ≤ (1 / 2332800 : ℝ) *
      Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
      ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) :=
    (uniform_budget_floor_bounds k t hk hkt ht).1
  have hH : sharpBudget k t = 256 * ((1 / 2332800 : ℝ) *
      Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
      ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ)))) := by
    unfold sharpBudget
    ring
  have hH2 : 2 ≤ sharpBudget k t := by rw [hH]; linarith
  have hR := forrelation_lower_uniform_sharp k t hk hkt2
  -- `H ≤ m`, from `m^(1-1/k) ≤ m` and `k² ln(4km) ≥ 1`.
  have hYhi : Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) ≤ (mValue t : ℝ) := by
    calc _ ≤ (mValue t : ℝ) ^ (1 : ℝ) :=
        Real.rpow_le_rpow_of_exponent_le hm1 (by
          have : (0 : ℝ) ≤ 1 / (k : ℝ) := by positivity
          linarith)
      _ = _ := Real.rpow_one _
  have hY0 : 0 ≤ Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) :=
    Real.rpow_nonneg (by positivity) _
  have hdenlo : 1 ≤ (k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ)) := by
    have hlog2 := Real.log_le_log (by norm_num : (0 : ℝ) < 2)
      (by nlinarith : (2 : ℝ) ≤ 4 * (k : ℝ) * (mValue t : ℝ))
    have hloghalf : (1 / 2 : ℝ) ≤ Real.log (4 * (k : ℝ) * (mValue t : ℝ)) := by
      have := Real.log_two_gt_d9
      linarith
    have hmul := mul_le_mul (show (4 : ℝ) ≤ (k : ℝ) ^ 2 by nlinarith)
      hloghalf (by norm_num : (0 : ℝ) ≤ 1 / 2) (sq_nonneg (k : ℝ))
    linarith
  have hHm : sharpBudget k t ≤ (mValue t : ℝ) := by
    unfold sharpBudget
    rw [div_le_iff₀ (by linarith)]
    have hmul := le_mul_of_one_le_right (show (0 : ℝ) ≤ (mValue t : ℝ) by positivity) hdenlo
    nlinarith
  refine ⟨?_, ?_, ?_, ?_⟩
  · apply Nat.le_floor
    rw [Nat.cast_one]
    linarith
  · exact_mod_cast (Nat.floor_le (by linarith : 0 ≤ sharpBudget k t)).trans hHm
  · have := Nat.lt_floor_add_one (sharpBudget k t)
    linarith
  · have hfl : (⌊sharpBudget k t⌋₊ : ℝ) ≤ sharpBudget k t := Nat.floor_le (by linarith)
    have hR' : sharpBudget k t < (R (P k t) : ℝ) := hR
    have : (⌊sharpBudget k t⌋₊ : ℝ) < (R (P k t) : ℝ) := lt_of_le_of_lt hfl hR'
    exact_mod_cast this

/-- **Theorem (T3, classical side).** For `k ≥ 2`, `t ≥ 41`, `15k + 2 ≤ 2t`, every
circuit `C` realising `P k t`, and every error `0 ≤ e`, with `m = 4^t`:

  `(1 - 2e) m^(2-1/k) / (72900 k² ln(4km)) ≤ R_e(F_{k,m}[C])`.

(`ln` is the natural logarithm; the bound is trivial for `e ≥ 1/2`.) -/
theorem RError_Fkm_lower (k t : ℕ) (hk : 2 ≤ k) (ht : 41 ≤ t) (hkt2 : 15 * k + 2 ≤ 2 * t)
    (C : Circuit (ForrelationCoord k t)) (hC : CircuitRealises C (P k t))
    {e : ℝ} (he : 0 ≤ e) :
    (1 - 2 * e) * Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) /
        (72900 * (k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) ≤
      (RError (totalise (Fkm k t C)) e : ℝ) := by
  obtain ⟨hL1, hLm, hLH, hLR⟩ := sharpCap_bounds k t hk ht hkt2
  set L := ⌊sharpBudget k t⌋₊ with hLdef
  set H := sharpBudget k t with hHdef
  have hk2 : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hm1 : (1 : ℝ) ≤ (mValue t : ℝ) := by
    have : 1 ≤ mValue t := Nat.one_le_two_pow
    exact_mod_cast this
  have hm0 : (0 : ℝ) < (mValue t : ℝ) := by linarith
  have hL1' : (1 : ℝ) ≤ (L : ℝ) := by exact_mod_cast hL1
  have hLm' : (L : ℝ) ≤ (mValue t : ℝ) := by exact_mod_cast hLm
  have hlg : 0 < Real.log (4 * (k : ℝ) * (mValue t : ℝ)) := Real.log_pos (by nlinarith)
  have hden : 0 < (k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ)) := by positivity
  -- The general planted bound at `ℓ = 2t`, `r = 40t`.
  have hP := planted_lower_general (P k t) C hC (2 * t) (40 * t) hL1 hLR he
  have hcol : ((2 ^ (2 * t) : ℕ) : ℝ) = (mValue t : ℝ) := rfl
  rw [hcol] at hP
  change _ ≤ (RError (totalise (Fkm k t C)) e : ℝ) at hP
  set rate : ℝ := 2 / (mValue t : ℝ) ^ 2 + 1 / ((mValue t : ℝ) * (L : ℝ)) +
    ((2 : ℝ) / 3) ^ (40 * t) with hrate
  have hrate0 : 0 < rate := by
    have h1 : 0 < 2 / (mValue t : ℝ) ^ 2 := by positivity
    have h2 : 0 ≤ 1 / ((mValue t : ℝ) * (L : ℝ)) := by positivity
    have h3 : 0 ≤ ((2 : ℝ) / 3) ^ (40 * t) := by positivity
    linarith
  -- `rate ≤ 4 / (m L)`.
  have hmL0 : 0 < (mValue t : ℝ) * (L : ℝ) := by positivity
  have hr1 : 2 / (mValue t : ℝ) ^ 2 ≤ 2 / ((mValue t : ℝ) * (L : ℝ)) := by
    apply div_le_div_of_nonneg_left (by norm_num) hmL0
    rw [sq]
    exact mul_le_mul_of_nonneg_left hLm' hm0.le
  have hr3 : ((2 : ℝ) / 3) ^ (40 * t) ≤ 1 / ((mValue t : ℝ) * (L : ℝ)) := by
    refine (twoThirds_pow_le t).trans ?_
    rw [← one_div]
    apply div_le_div_of_nonneg_left (by norm_num) hmL0
    have h1 : (mValue t : ℝ) * (L : ℝ) ≤ (mValue t : ℝ) ^ 2 := by
      rw [sq]; exact mul_le_mul_of_nonneg_left hLm' hm0.le
    have h2 : (mValue t : ℝ) ^ 2 ≤ (mValue t : ℝ) ^ 10 :=
      pow_le_pow_right₀ hm1 (by norm_num)
    linarith
  have hrate4 : rate ≤ 4 / ((mValue t : ℝ) * (L : ℝ)) := by
    have : 4 / ((mValue t : ℝ) * (L : ℝ)) =
        2 / ((mValue t : ℝ) * (L : ℝ)) + 1 / ((mValue t : ℝ) * (L : ℝ)) +
          1 / ((mValue t : ℝ) * (L : ℝ)) := by ring
    rw [this, hrate]
    linarith
  -- `m · m^(1-1/k) = m^(2-1/k)`.
  have hpow : Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) =
      (mValue t : ℝ) * Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) := by
    have : (2 : ℝ) - 1 / (k : ℝ) = 1 + (1 - 1 / (k : ℝ)) := by ring
    show (mValue t : ℝ) ^ (2 - 1 / (k : ℝ)) =
      (mValue t : ℝ) * (mValue t : ℝ) ^ (1 - 1 / (k : ℝ))
    rw [this, Real.rpow_add hm0, Real.rpow_one]
  have hlgne : Real.log (4 * (k : ℝ) * (mValue t : ℝ)) ≠ 0 := hlg.ne'
  have hkne : (k : ℝ) ≠ 0 := by positivity
  have hmne : (mValue t : ℝ) ≠ 0 := hm0.ne'
  have hLne : (L : ℝ) ≠ 0 := by positivity
  by_cases hg : 0 ≤ 1 - 2 * e
  · -- target = (1-2e) m H / 8 ≤ (1-2e) m L / 4 ≤ (1-2e) / rate ≤ R_e.
    have htarget : (1 - 2 * e) * Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) /
        (72900 * (k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) =
        (1 - 2 * e) * (mValue t : ℝ) * H / 8 := by
      rw [hpow, hHdef, sharpBudget]
      field_simp
      ring
    have hstep1 : (1 - 2 * e) * (mValue t : ℝ) * H / 8 ≤
        (1 - 2 * e) * (mValue t : ℝ) * (L : ℝ) / 4 := by
      have := mul_le_mul_of_nonneg_left hLH (mul_nonneg hg hm0.le)
      nlinarith
    have hstep2 : (1 - 2 * e) * (mValue t : ℝ) * (L : ℝ) / 4 ≤ (1 - 2 * e) / rate := by
      have h := div_le_div_of_nonneg_left hg hrate0 hrate4
      have : (1 - 2 * e) / (4 / ((mValue t : ℝ) * (L : ℝ))) =
          (1 - 2 * e) * (mValue t : ℝ) * (L : ℝ) / 4 := by
        field_simp
      linarith
    rw [htarget]
    exact hstep1.trans (hstep2.trans hP)
  · replace hg : 1 - 2 * e < 0 := lt_of_not_ge hg
    have hden72 : 0 < 72900 * (k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ)) :=
      mul_pos (by positivity) hlg
    have hY : 0 ≤ Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) :=
      Real.rpow_nonneg hm0.le _
    have hneg : (1 - 2 * e) * Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) /
        (72900 * (k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) ≤ 0 := by
      rw [div_le_iff₀ hden72, zero_mul]
      nlinarith
    exact hneg.trans (Nat.cast_nonneg _)

/-- **Theorem (T3, family statement).** One explicit function, `F_{k,m}` built from the
explicit circuit `forrCircuit l t` realising `P k t`, with `k = l + 1` and `m = 4^t`.
For `k ≥ 2`, `t ≥ 41`, `15k + 2 ≤ 2t`, every classical error `0 ≤ e` and every quantum
error `d ≥ 1/250`:

* `(1 - 2e) m^(2-1/k) / (72900 k² ln(4km)) ≤ R_e(F_{k,m})`;
* `Q_d(F_{k,m}) ≤ A_k √m (log₂ m)^6` with `A_k = budgetConst k`, `√m = 2^t`,
  `log₂ m = 2t`.

The function does not depend on `e` or `d`. -/
theorem family_bounds_error_explicit (l t : ℕ) (hk : 2 ≤ l + 1) (ht : 41 ≤ t)
    (hkt2 : 15 * (l + 1) + 2 ≤ 2 * t) {e d : ℝ} (he : 0 ≤ e) (hd : 1 / 250 ≤ d) :
    CircuitRealises (forrCircuit l t) (P (l + 1) t) ∧
    (1 - 2 * e) * Real.rpow (mValue t : ℝ) (2 - 1 / ((l + 1 : ℕ) : ℝ)) /
        (72900 * ((l + 1 : ℕ) : ℝ) ^ 2 *
          Real.log (4 * ((l + 1 : ℕ) : ℝ) * (mValue t : ℝ))) ≤
      (RError (totalise (Fkm (l + 1) t (forrCircuit l t))) e : ℝ) ∧
    (QError (totalise (Fkm (l + 1) t (forrCircuit l t))) d : ℝ) ≤
      (budgetConst (l + 1) : ℝ) * 2 ^ t * (2 * (t : ℝ)) ^ 6 :=
  ⟨forrCircuit_realises l t,
    RError_Fkm_lower (l + 1) t hk ht hkt2 _ (forrCircuit_realises l t) he,
    QError_Fkm_le l t (by omega) hd⟩

/-- The explicit constant: `budgetConst k ≤ 2^53 k 2^(10k)` (reused from `Upper.Bound`). -/
theorem budgetConst_le_explicit {k : ℕ} (hk : 1 ≤ k) :
    budgetConst k ≤ 2 ^ 53 * k * 2 ^ (10 * k) :=
  budgetConst_le_exponential hk

end QuarticQuery.ErrorExplicit
