module

public import QuarticQuery.ErrorExplicit.Family
public import QuarticQuery.Appendix.TheoremA1

/-!
# The optimal exponent at explicit errors

`UniversalPowerError e d α` is equation (1) of the preprint with `R` replaced by `R_e`
and `Q` by `Q_d`; at `e = d = 1/3` it is `UniversalPower α`
(`universalPowerError_one_third`).

* Lower side: for every `0 ≤ e < 1/2` and every `d ≥ 1/250`, no `α < 4` is admissible.
  This uses one fixed `k` with `2 - 1/k > α/2`, the explicit family bounds of
  `Family.lean`, and the abstract threshold lemma `exists_threshold_gap`.
* Upper side: for every `0 ≤ e` and `0 ≤ d ≤ 1/3`, `R_e(f) ≤ D(f) ≤ 20736 Q_d(f)^4`
  (Theorem A.1 of the project, after `Q ≤ Q_d`).

Together: for `0 ≤ e < 1/2` and `1/250 ≤ d ≤ 1/3`, the admissible exponents are exactly
`[4, ∞)` and `alphaTotError e d = 4`. The range `d ∈ (1/3, 1/2)` needs a general-error
form of Theorem A.1 (or quantum amplification), and `d < 1/250` needs amplification of
the family algorithm; neither is formalised here.
-/

@[expose] public section

namespace QuarticQuery.ErrorExplicit

open QuarticQuery QuarticQuery.Upper QuarticQuery.Forrelation Filter

/-- Equation (1) at explicit errors: a constant `C > 0` with
`R_e(f) ≤ C (1 + Q_d(f))^α` for every total `f` on `Fin n`, `n ≥ 1`. -/
def UniversalPowerError (e d α : ℝ) : Prop :=
  0 ≤ α ∧ ∃ C : ℝ, 0 < C ∧
    ∀ n : ℕ, 1 ≤ n → ∀ f : TotalBool (Fin n),
      (RError (totalise f) e : ℝ) ≤ C * Real.rpow (1 + (QError (totalise f) d : ℝ)) α

/-- `α_tot` at explicit errors. -/
noncomputable def alphaTotError (e d : ℝ) : ℝ :=
  sInf {α : ℝ | UniversalPowerError e d α}

theorem universalPowerError_one_third (α : ℝ) :
    UniversalPowerError (1 / 3) (1 / 3) α ↔ UniversalPower α := by
  simp only [UniversalPowerError, UniversalPower, RError_one_third, QError_one_third]

theorem alphaTotError_one_third : alphaTotError (1 / 3) (1 / 3) = alphaTot := by
  unfold alphaTotError alphaTot
  congr 1
  ext α
  exact universalPowerError_one_third α

/-! ## Renaming coordinates -/

section Reindex

variable {ι κ : Type}

theorem RLeError.comap {f : PartialBool κ} {g : PartialBool ι} {e : ℝ} {t : ℕ} (u : ι → κ)
    (hfg : ∀ x b, f x = some b → g (fun i => x (u i)) = some b) (h : RLeError g e t) :
    RLeError f e t := by
  obtain ⟨A, hA, hc⟩ := h
  refine ⟨A.map u, by simpa using hA, fun x b hx => ?_⟩
  rw [RandomizedProgram.success_map]
  exact hc _ b (hfg x b hx)

theorem RLeError_reindex_iff (u : ι ≃ κ) {f : PartialBool ι} {e : ℝ} {t : ℕ} :
    RLeError (reindex u f) e t ↔ RLeError f e t := by
  constructor
  · intro h
    have := h.comap (f := reindex u.symm (reindex u f)) u.symm fun _ _ hx => hx
    rwa [reindex_symm_reindex] at this
  · exact RLeError.comap u fun _ _ hx => hx

theorem RError_reindex [Fintype ι] [Fintype κ] (u : ι ≃ κ) (f : PartialBool ι) (e : ℝ) :
    RError (reindex u f) e = RError f e := by
  simp only [RError, RLeError_reindex_iff]

theorem QLeError.reindex [Fintype ι] [Fintype κ] (u : ι ≃ κ) {f : PartialBool ι} {e : ℝ}
    {t : ℕ} (h : QLeError f e t) : QLeError (QuarticQuery.reindex u f) e t := by
  rcases h with ⟨b, hb⟩ | ⟨w, ψ, A, hψ, hA, hc⟩
  · exact .inl ⟨b, fun x c hx => hb _ c hx⟩
  · refine .inr ⟨w, stateEquiv u ψ, A.relabel u, ?_, by simpa using hA, fun x b hx => ?_⟩
    · rw [(stateEquiv u).norm_map, hψ]
    · rw [AdaptiveProgram.outputMass_relabel]
      exact hc _ b hx

theorem QLeError_reindex_iff [Fintype ι] [Fintype κ] (u : ι ≃ κ) {f : PartialBool ι} {e : ℝ}
    {t : ℕ} : QLeError (QuarticQuery.reindex u f) e t ↔ QLeError f e t := by
  constructor
  · intro h
    have := h.reindex u.symm
    rwa [reindex_symm_reindex] at this
  · exact QLeError.reindex u

theorem QError_reindex [Fintype ι] [Fintype κ] (u : ι ≃ κ) (f : PartialBool ι) (e : ℝ) :
    QError (QuarticQuery.reindex u f) e = QError f e := by
  simp only [QError, QLeError_reindex_iff]

/-- A universal bound over `Fin n` holds on any nonempty finite coordinate type. -/
theorem transport_bound_error {e d D α : ℝ}
    (h : ∀ n : ℕ, 1 ≤ n → ∀ f : TotalBool (Fin n),
      (RError (totalise f) e : ℝ) ≤ D * Real.rpow (1 + (QError (totalise f) d : ℝ)) α)
    [Fintype ι] [Nonempty ι] (f : TotalBool ι) :
    (RError (totalise f) e : ℝ) ≤ D * Real.rpow (1 + (QError (totalise f) d : ℝ)) α := by
  let u := Fintype.equivFin ι
  let g : TotalBool (Fin (Fintype.card ι)) := fun x => f fun i => x (u i)
  have hg : totalise g = reindex u (totalise f) := rfl
  have := h _ Fintype.card_pos g
  rwa [hg, RError_reindex, QError_reindex] at this

end Reindex

/-! ## No exponent below four -/

/-- The classical family bound in the shape `c (4^t)^s / (2t)^2` used by the threshold
lemma, with `c = (1 - 2e) / (109350 k²)`. -/
theorem RError_Fkm_lower_shape (l t : ℕ) (hk : 2 ≤ l + 1) (ht : 41 ≤ t)
    (hkt2 : 15 * (l + 1) + 2 ≤ 2 * t) {e : ℝ} (he : 0 ≤ e) (he2 : e < 1 / 2) :
    (1 - 2 * e) / (109350 * ((l + 1 : ℕ) : ℝ) ^ 2) *
        ((4 : ℝ) ^ t) ^ (2 - 1 / ((l + 1 : ℕ) : ℝ)) / (2 * (t : ℝ)) ^ 2 ≤
      (RError (totalise (Fkm (l + 1) t (forrCircuit l t))) e : ℝ) := by
  set k : ℕ := l + 1 with hkdef
  have h := RError_Fkm_lower k t hk ht hkt2 (forrCircuit l t) (forrCircuit_realises l t) he
  refine le_trans ?_ h
  have hk2 : (2 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have ht1 : (41 : ℝ) ≤ (t : ℝ) := by exact_mod_cast ht
  have hm1 : (1 : ℝ) ≤ (mValue t : ℝ) := by
    have : 1 ≤ mValue t := Nat.one_le_two_pow
    exact_mod_cast this
  have hlg0 : 0 < Real.log (4 * (k : ℝ) * (mValue t : ℝ)) := Real.log_pos (by nlinarith)
  have hlg := log_four_k_m_le (k := k) (t := t) (by omega) (by omega)
  have hlg' : Real.log (4 * (k : ℝ) * (mValue t : ℝ)) ≤ 3 / 2 * (2 * (t : ℝ)) ^ 2 := by
    nlinarith
  have hpow : ((4 : ℝ) ^ t) ^ (2 - 1 / (k : ℝ)) =
      Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) := by
    rw [mValue_cast]; exact (Real.rpow_eq_pow _ _).symm
  rw [hpow]
  have hY0 : 0 ≤ Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) :=
    Real.rpow_nonneg (by positivity) _
  have hg : 0 ≤ 1 - 2 * e := by linarith
  set Y := Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ))
  set lg := Real.log (4 * (k : ℝ) * (mValue t : ℝ))
  have hk0 : (0 : ℝ) < (k : ℝ) ^ 2 := by
    have : (0 : ℝ) < (k : ℝ) := by linarith
    positivity
  have ht0 : (0 : ℝ) < (2 * (t : ℝ)) ^ 2 := by
    have : (0 : ℝ) < (t : ℝ) := by linarith
    positivity
  have heq : (1 - 2 * e) / (109350 * (k : ℝ) ^ 2) * Y / (2 * (t : ℝ)) ^ 2 =
      (1 - 2 * e) * Y / (109350 * (k : ℝ) ^ 2 * (2 * (t : ℝ)) ^ 2) := by
    rw [div_mul_eq_mul_div, div_div]
  rw [heq]
  have hnum : 0 ≤ (1 - 2 * e) * Y := mul_nonneg hg hY0
  have hcmp : 72900 * (k : ℝ) ^ 2 * lg ≤ 109350 * (k : ℝ) ^ 2 * (2 * (t : ℝ)) ^ 2 := by
    nlinarith
  exact div_le_div_of_nonneg_left hnum (mul_pos (mul_pos (by norm_num) hk0) hlg0) hcmp

/-- **Theorem (T4, lower side).** For every classical error `0 ≤ e < 1/2`, every quantum
error `d ≥ 1/250` and every `α < 4`, `UniversalPowerError e d α` fails. -/
theorem not_universalPowerError_of_lt_four {e d α : ℝ} (he : 0 ≤ e) (he2 : e < 1 / 2)
    (hd : 1 / 250 ≤ d) (hα : α < 4) : ¬ UniversalPowerError e d α := by
  rintro ⟨hα0, D, hD, hbound⟩
  obtain ⟨k, hk, hs⟩ := exists_nat_exponent hα
  obtain ⟨l, rfl⟩ : ∃ l, k = l + 1 := ⟨k - 1, by omega⟩
  have hc : 0 < (1 - 2 * e) / (109350 * ((l + 1 : ℕ) : ℝ) ^ 2) := by
    have h1 : (0 : ℝ) < ((l + 1 : ℕ) : ℝ) := by positivity
    have h2 : 0 < 1 - 2 * e := by linarith
    exact div_pos h2 (by positivity)
  have hC : (0 : ℝ) < (budgetConst (l + 1) : ℝ) := by exact_mod_cast budgetConst_pos _
  obtain ⟨T, hT⟩ := exists_threshold_gap 6 hc hC hD hα0 hs
  set t := max T (max 41 (8 * (l + 1) + 1)) with htdef
  have hTt : T ≤ t := le_max_left _ _
  have h41 : 41 ≤ t := le_trans (le_max_left _ _) (le_max_right _ _)
  have hkt : 8 * (l + 1) + 1 ≤ t := le_trans (le_max_right _ _) (le_max_right _ _)
  have hkt2 : 15 * (l + 1) + 2 ≤ 2 * t := by omega
  have hR := RError_Fkm_lower_shape l t hk h41 hkt2 he he2
  have hQ := QError_Fkm_le l t (by omega) hd
  have hgap := hT t hTt _ _ (Nat.cast_nonneg _) hQ hR
  exact absurd (transport_bound_error hbound (Fkm (l + 1) t (forrCircuit l t)))
    (not_le.2 hgap)

/-! ## Four is admissible -/

/-- **Theorem (T4, upper side).** For every `0 ≤ e` and `0 ≤ d ≤ 1/3` and every total
`f`, `R_e(f) ≤ D(f) ≤ 20736 Q_d(f)^4`. -/
theorem RError_le_D_le_QError_pow_four {n : ℕ} (f : TotalBool (Fin n)) {e d : ℝ}
    (he : 0 ≤ e) (hd0 : 0 ≤ d) (hd : d ≤ 1 / 3) :
    RError (totalise f) e ≤ D (totalise f) ∧
      D (totalise f) ≤ 20736 * QError (totalise f) d ^ 4 := by
  refine ⟨RError_le_D _ he, (D_le_Q_pow_four f).trans ?_⟩
  have hQ : Q (totalise f) ≤ QError (totalise f) d := by
    rw [← QError_one_third]
    exact QError_anti hd0 hd
  gcongr

theorem universalPowerError_of_four_le {e d α : ℝ} (he : 0 ≤ e) (hd0 : 0 ≤ d)
    (hd : d ≤ 1 / 3) (hα : 4 ≤ α) : UniversalPowerError e d α := by
  refine ⟨by linarith, 20736, by norm_num, fun n _ f => ?_⟩
  obtain ⟨h₁, h₂⟩ := RError_le_D_le_QError_pow_four f he hd0 hd
  have hq : (0 : ℝ) ≤ QError (totalise f) d := Nat.cast_nonneg _
  have h3 : (RError (totalise f) e : ℝ) ≤ 20736 * (1 + (QError (totalise f) d : ℝ)) ^ 4 := by
    have : (RError (totalise f) e : ℝ) ≤ 20736 * (QError (totalise f) d : ℝ) ^ 4 := by
      exact_mod_cast h₁.trans h₂
    refine this.trans ?_
    gcongr
    linarith
  have h4 : (1 + (QError (totalise f) d : ℝ)) ^ 4 ≤
      Real.rpow (1 + (QError (totalise f) d : ℝ)) α := by
    have : (1 + (QError (totalise f) d : ℝ)) ^ 4 =
        Real.rpow (1 + (QError (totalise f) d : ℝ)) (4 : ℝ) := by
      rw [Real.rpow_eq_pow]
      exact_mod_cast (Real.rpow_natCast (1 + (QError (totalise f) d : ℝ)) 4).symm
    rw [this]
    exact Real.rpow_le_rpow_of_exponent_le (by linarith) hα
  linarith

/-- **Theorem (T4).** For every classical error `0 ≤ e < 1/2` and every quantum error
`1/250 ≤ d ≤ 1/3`, the admissible exponents in equation (1) with `R_e`, `Q_d` are
exactly `[4, ∞)`, so `alphaTotError e d = 4`. At `e = d = 1/3` this is the project's
`alphaTot_eq_four_unconditional` (via `alphaTotError_one_third`). -/
theorem alphaTotError_eq_four {e d : ℝ} (he : 0 ≤ e) (he2 : e < 1 / 2)
    (hd : 1 / 250 ≤ d) (hd3 : d ≤ 1 / 3) :
    (∀ α : ℝ, UniversalPowerError e d α ↔ 4 ≤ α) ∧ alphaTotError e d = 4 := by
  have hd0 : 0 ≤ d := le_trans (by norm_num) hd
  have hiff : ∀ α : ℝ, UniversalPowerError e d α ↔ 4 ≤ α := fun α =>
    ⟨fun h => by
      by_contra hlt
      exact not_universalPowerError_of_lt_four he he2 hd (not_le.1 hlt) h,
     fun h => universalPowerError_of_four_le he hd0 hd3 h⟩
  refine ⟨hiff, ?_⟩
  have hleast : IsLeast {α : ℝ | UniversalPowerError e d α} 4 :=
    ⟨(hiff 4).2 le_rfl, fun α hα => (hiff α).1 hα⟩
  exact hleast.csInf_eq

end QuarticQuery.ErrorExplicit
