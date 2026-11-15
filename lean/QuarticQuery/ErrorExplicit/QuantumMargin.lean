module

public import QuarticQuery.ErrorExplicit.Defs
public import QuarticQuery.Upper.Bound

/-!
# The quantum family algorithm already has error at most `1/250`

`Upper.Fkm_QLe` (Upper/Verify.lean) assembles the tournament and the verifier into a
program for `F_{k,m}` and concludes `QLe`, i.e. error `1/3`. Before that weakening its
proof has, with `T = ⌈log₂(1000 m)⌉` and `ε = 1/(1000 T)`:

* on a true input, acceptance at least `1 - 2m/2^T - Tε - ε`;
* on a false input, acceptance at most `Tε = 1/1000`.

By `miss_bound_le`, `Tval_mul_epsval` and `epsval_le` the first is at least
`1 - 1/500 - 1/1000 - 1/1000 = 1 - 1/250`. This module re-runs the same proof with
the same algorithm and the same query budget and keeps that margin.

The only new ingredient is `Runs.toQLeErrorPartial`, the compiler `Runs.toQLePartial`
with the success threshold `2/3` replaced by `1 - e`; its output-law proof is unchanged.
-/

@[expose] public section

namespace QuarticQuery.ErrorExplicit

open QuarticQuery QuarticQuery.Upper QuarticQuery.Forrelation QuarticQuery.Tournament
  QuarticQuery.Amplification

section Compile

variable {ι : Type} [Fintype ι] [Inhabited ι]

/-- `Runs.toQLePartial` at an arbitrary success threshold `1 - e`. -/
theorem Runs.toQLeErrorPartial {c : ℕ} {L : BitInput ι → Bool → ℝ} (h : Runs c L)
    (f : PartialBool ι) {e : ℝ} (hL : ∀ x b, f x = some b → 1 - e ≤ L x b) :
    QLeError f e c := by
  obtain ⟨w₀, h⟩ := h
  obtain ⟨P, hP⟩ := h w₀ le_rfl
  obtain ⟨hcap, hmass⟩ := hP (fun a => .output a) 0 (by simp [AdaptiveProgram.queryCap])
  refine .inr ⟨w₀, startState, P fun a => .output a, norm_startState, by simpa using hcap,
    fun x b hb => ?_⟩
  rw [hmass]
  have hn : ‖(startState : State ι w₀)‖ ^ 2 = 1 := by rw [norm_startState]; norm_num
  have h2 := hL x b hb
  cases b <;> simpa [AdaptiveProgram.outputMass, hn] using h2

/-- `Runs.toQLe` at an arbitrary success threshold `1 - e`. -/
theorem Runs.toQLeError {c : ℕ} {L : BitInput ι → Bool → ℝ} (h : Runs c L) (f : TotalBool ι)
    {e : ℝ} (hL : ∀ x, 1 - e ≤ L x (f x)) : QLeError (totalise f) e c :=
  Runs.toQLeErrorPartial h _ fun x b hb => by
    obtain rfl : f x = b := Option.some.inj hb
    exact hL x

end Compile

/-- The numerical margin of the existing schedule: `2m/2^T + Tε + ε ≤ 1/250`. -/
theorem total_error_le_250 {m : ℕ} (hm : 2 ≤ m) :
    2 * (m : ℝ) / 2 ^ Tval m + (Tval m : ℝ) * epsval m + epsval m ≤ 1 / 250 := by
  have h1 := miss_bound_le m
  have h2 := Tval_mul_epsval hm
  have h3 := epsval_le hm
  linarith

variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

/-- **Proposition 3.3 with its error margin.** The algorithm of `Upper.Fkm_QLe`, with the
same schedule and the same budget, computes `F_{k,m}` with error at most `1/250`
(for `k ≥ 1`, `t ≥ 1` and any circuit realising `P k t`). -/
theorem Fkm_QLeError_250 (hk : 1 ≤ k) (ht : 1 ≤ t) (hC : CircuitRealises C (P k t)) {n : ℕ}
    (hn : repetitions k (epsval (mValue t) / (40 * t : ℕ)) ≤ n) :
    QLeError (totalise (Fkm k t C)) (1 / 250 : ℝ) (budget k t n (Fintype.card (Tests t C))) := by
  classical
  have hm : 2 ≤ Fintype.card (Col t) := by
    rw [card_col]
    calc 2 ≤ 2 ^ 1 := by norm_num
      _ ≤ 2 ^ (2 * t) := Nat.pow_le_pow_right (by norm_num) (by omega)
  have hm' : 2 ≤ mValue t := card_col t ▸ hm
  obtain ⟨ε, hεd⟩ : ∃ ε, ε = epsval (mValue t) := ⟨_, rfl⟩
  have hTε : (Tval (mValue t) : ℝ) * ε = 1 / 1000 := by rw [hεd]; exact Tval_mul_epsval hm'
  have hε0 : 0 ≤ ε := by rw [hεd]; exact epsval_nonneg _
  have hε1 : ε ≤ 1 / 1000 := by rw [hεd]; exact epsval_le hm'
  have hε : 0 < ε := by
    rcases hε0.eq_or_lt with h | h
    · rw [← h] at hTε; norm_num at hTε
    · exact h
  choose f hf01 hfε hf1 hrun using fun p : Col t × Addr t =>
    search_runs (C := C) p.1 p.2 hε
  let g : Col t → Addr t → BitInput (Loc k t C) → ℝ := fun c s => f (c, s)
  have hA0 := fun x c s => addrLaw_nonneg (C := C) hk n x c s
  have hA1 := fun x c => sum_addrLaw (C := C) hk n x c
  have hv : ∀ c, Runs (2 * addrCost k t n + searchCost t (Fintype.card (Tests t C)) ε)
      fun x b => bern (verifyProb n g x c) b := fun c => by
    have hb := (addr_samples (C := C) hk n c).runs.bind (K := fun s x b => bern (g c s x) b)
      fun s => hrun (c, s)
    refine hb.congr fun x b => ?_
    cases b with
    | true => simp [bern, verifyProb]
    | false =>
      simp only [bern, Bool.false_eq_true, ite_false, verifyProb, mul_sub, mul_one]
      rw [Finset.sum_sub_distrib, hA1]
  have hv01 : ∀ x c, 0 ≤ verifyProb n g x c ∧ verifyProb n g x c ≤ 1 := fun x c => by
    constructor
    · exact Finset.sum_nonneg fun s _ => mul_nonneg (hA0 x c s) (hf01 _ x).1
    · calc verifyProb n g x c ≤ ∑ s, addrLaw n x c s :=
            Finset.sum_le_sum fun s _ =>
              mul_le_of_le_one_right (hA0 x c s) (hf01 _ x).2
        _ = 1 := hA1 x c
  have htour := tournament_runs (ι := Loc k t C) (Col := Col t)
    (a := fun x => cmpProb (C := C) n x) (v := fun x c => verifyProb n g x c)
    hm (fun x => cmpProb_isComparison x n) (fun x => cmpProb_unit hk x n)
    (fun i p => cmp_samples hk n i p) hv hv01
  dsimp only at htour
  rw [card_col, ← hεd] at htour
  obtain ⟨val, hrunT, hlow, hhigh⟩ := htour
  have hgood : ∀ {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t},
      WinsAt (P k t) C (2 * t) (40 * t) x i s → 1 - ε ≤ addrLaw n x i s := fun {x i s} hw =>
    addrLaw_good hk ht hε (by linarith) (by rw [hεd]; exact hn) hw.2.1
  refine (Runs.toQLeError hrunT (Fkm k t C) fun x => ?_).mono (by rw [budget, ← hεd])
  cases hF : Fkm k t C x with
  | true =>
    obtain ⟨i, s, hw⟩ := addressedF_eq_true_iff.1 hF
    have hd : Dominant (cmpProb n x) ε i := fun j hj =>
      (hgood hw).trans (cmpProb_winner hk hw hj)
    have hvi : 1 - ε ≤ verifyProb n g x i := by
      have h1 : g i s x = 1 := hf1 (i, s) x fun e => (winsAt_iff_localTests hC).1 hw e
      calc 1 - ε ≤ addrLaw n x i s := hgood hw
        _ = addrLaw n x i s * g i s x := by rw [h1, mul_one]
        _ ≤ verifyProb n g x i :=
          Finset.single_le_sum (f := fun s => addrLaw n x i s * g i s x)
            (fun s _ => mul_nonneg (hA0 x i s) (hf01 _ x).1) (Finset.mem_univ s)
    have h := hhigh x i hd hvi
    have herr := total_error_le_250 hm'
    rw [← hεd] at herr
    simp only [bern, ite_true]
    linarith
  | false =>
    have hno : ∀ c, ¬ ∃ s, WinsAt (P k t) C (2 * t) (40 * t) x c s := fun c ⟨s, hw⟩ => by
      have := addressedF_eq_true_iff.2 ⟨c, s, hw⟩
      rw [show addressedF (P k t) C (2 * t) (40 * t) x = Fkm k t C x from rfl, hF] at this
      exact Bool.noConfusion this
    have hle : ∀ c, verifyProb n g x c ≤ ε := fun c => by
      calc verifyProb n g x c ≤ ∑ s, addrLaw n x c s * ε :=
            Finset.sum_le_sum fun s _ => by
              obtain ⟨e, he⟩ := exists_failing_localTest hC (hno c) s
              exact mul_le_mul_of_nonneg_left (hfε (c, s) x e he) (hA0 x c s)
        _ = ε := by rw [← Finset.sum_mul, hA1, one_mul]
    have h := hlow x hle
    simp only [bern, Bool.false_eq_true, ite_false]
    linarith

/-- **Theorem (T2).** For the explicit circuit `forrCircuit l t` (so `k = l + 1 ≥ 1`) and
every `t ≥ 1`, `F_{k,m}` has a quantum algorithm with error at most `1/250` using at most
`budgetConst k · 2^t · (2t)^6` queries: the same algorithm and budget as the public
`Upper.Fkm_forrCircuit_QLe`, which states only error `1/3`. -/
theorem Fkm_forrCircuit_QLeError_250 (l t : ℕ) (ht : 1 ≤ t) :
    QLeError (totalise (Fkm (l + 1) t (forrCircuit l t))) (1 / 250 : ℝ)
      (budgetConst (l + 1) * 2 ^ t * (2 * t) ^ 6) :=
  (Fkm_QLeError_250 (by omega) ht (forrCircuit_realises l t) le_rfl).mono
    (budget_le ht (forrCircuit_size_le l t ht))

/-- The `1/250` statement implies the public one: same witness, weaker threshold. -/
theorem Fkm_forrCircuit_QLe_of_250 (l t : ℕ) (ht : 1 ≤ t) :
    QLe (totalise (Fkm (l + 1) t (forrCircuit l t)))
      (budgetConst (l + 1) * 2 ^ t * (2 * t) ^ 6) :=
  (QLeError_one_third _ _).1 ((Fkm_forrCircuit_QLeError_250 l t ht).mono_error (by norm_num))

/-- **T2, complexity form.** For every error `d ≥ 1/250` (no repetition needed),
`Q_d(F_{k,m}) ≤ budgetConst k · 2^t · (2t)^6` with `k = l + 1`, `t ≥ 1`. -/
theorem QError_Fkm_le (l t : ℕ) (ht : 1 ≤ t) {d : ℝ} (hd : 1 / 250 ≤ d) :
    (QError (totalise (Fkm (l + 1) t (forrCircuit l t))) d : ℝ) ≤
      (budgetConst (l + 1) : ℝ) * 2 ^ t * (2 * (t : ℝ)) ^ 6 := by
  have h := QError_le_of_QLeError ((Fkm_forrCircuit_QLeError_250 l t ht).mono_error hd)
  have hc : ((QError (totalise (Fkm (l + 1) t (forrCircuit l t))) d : ℕ) : ℝ) ≤
      ((budgetConst (l + 1) * 2 ^ t * (2 * t) ^ 6 : ℕ) : ℝ) := by exact_mod_cast h
  simpa using hc

end QuarticQuery.ErrorExplicit
