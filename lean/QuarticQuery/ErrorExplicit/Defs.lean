module

public import QuarticQuery.Model.Classical
public import QuarticQuery.Model.Quantum

/-!
# Error-explicit query complexity

The public vocabulary in `QuarticQuery.Statement` fixes the error at `1/3`
(success at least `2/3` on every promised input). This module adds the same
definitions with an arbitrary real error `e`: success at least `1 - e` on every
promised input. Nothing else changes: the program classes, the worst-case depth
and the syntactic quantum query cap are exactly those of `RLe` and `QLe`.

Each definition sits next to a lemma showing that at `e = 1/3` it is the existing
definition (`RLeError_one_third`, `RError_one_third`, `QLeError_one_third`,
`QError_one_third`). For `0 ≤ e` the read-all tree makes every feasible set
nonempty, so the natural-number infimum is attained (`RLeError_RError`,
`QLeError_QError`).
-/

@[expose] public section

namespace QuarticQuery.ErrorExplicit

open QuarticQuery

variable {ι : Type}

/-- Error at most `e` on every promised input within `budget` classical queries:
a finite mixture of decision trees of depth at most `budget` that outputs the
correct value with probability at least `1 - e`. At `e = 1/3` this is `RLe`. -/
def RLeError (f : PartialBool ι) (e : ℝ) (budget : ℕ) : Prop :=
  ∃ A : RandomizedProgram ι,
    A.depth ≤ budget ∧ ∀ x b, f x = some b → 1 - e ≤ A.success x b

/-- Randomized query complexity with error `e`. At `e = 1/3` this is `R`. -/
noncomputable def RError [Fintype ι] (f : PartialBool ι) (e : ℝ) : ℕ :=
  sInf {t : ℕ | RLeError f e t}

/-- Error at most `e` on every promised input within `budget` quantum queries,
in exactly the model of `QLe` (a constant-on-promise function, or a unit initial
state and an adaptive program whose syntactic query cap is at most `budget`).
At `e = 1/3` this is `QLe`. -/
def QLeError [Fintype ι] (f : PartialBool ι) (e : ℝ) (budget : ℕ) : Prop :=
  ConstantOnPromise f ∨
  ∃ (w : ℕ) (ψ₀ : State ι w) (A : AdaptiveProgram ι w),
    ‖ψ₀‖ = 1 ∧ A.queryCap ≤ budget ∧
    ∀ x b, f x = some b → 1 - e ≤ A.outputMass x ψ₀ b

/-- Quantum query complexity with error `e`. At `e = 1/3` this is `Q`. -/
noncomputable def QError [Fintype ι] (f : PartialBool ι) (e : ℝ) : ℕ :=
  sInf {t : ℕ | QLeError f e t}

/-! ## Agreement with the public `1/3` definitions -/

theorem RLeError_one_third (f : PartialBool ι) (t : ℕ) :
    RLeError f (1 / 3 : ℝ) t ↔ RLe f t := by
  have h : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  simp only [RLeError, RLe, h]

theorem RError_one_third [Fintype ι] (f : PartialBool ι) :
    RError f (1 / 3 : ℝ) = R f := by
  unfold RError R
  congr 1
  ext t
  exact RLeError_one_third f t

theorem QLeError_one_third [Fintype ι] (f : PartialBool ι) (t : ℕ) :
    QLeError f (1 / 3 : ℝ) t ↔ QLe f t := by
  have h : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  simp only [QLeError, QLe, h]

theorem QError_one_third [Fintype ι] (f : PartialBool ι) :
    QError f (1 / 3 : ℝ) = Q f := by
  unfold QError Q
  congr 1
  ext t
  exact QLeError_one_third f t

/-! ## Monotonicity -/

theorem RLeError.mono_error {f : PartialBool ι} {a b : ℝ} {t : ℕ} (hab : a ≤ b)
    (h : RLeError f a t) : RLeError f b t := by
  obtain ⟨A, hA, hc⟩ := h
  exact ⟨A, hA, fun x c hx => le_trans (by linarith) (hc x c hx)⟩

theorem RLeError.mono {f : PartialBool ι} {e : ℝ} {s t : ℕ} (h : RLeError f e s)
    (hst : s ≤ t) : RLeError f e t := by
  obtain ⟨A, hA, hc⟩ := h
  exact ⟨A, hA.trans hst, hc⟩

theorem QLeError.mono_error [Fintype ι] {f : PartialBool ι} {a b : ℝ} {t : ℕ} (hab : a ≤ b)
    (h : QLeError f a t) : QLeError f b t := by
  rcases h with h | ⟨w, ψ, A, hn, hT, hA⟩
  · exact Or.inl h
  · exact Or.inr ⟨w, ψ, A, hn, hT, fun x c hx => le_trans (by linarith) (hA x c hx)⟩

theorem QLeError.mono [Fintype ι] {f : PartialBool ι} {e : ℝ} {s t : ℕ} (h : QLeError f e s)
    (hst : s ≤ t) : QLeError f e t := by
  rcases h with h | ⟨w, ψ, A, hn, hT, hA⟩
  · exact Or.inl h
  · exact Or.inr ⟨w, ψ, A, hn, hT.trans hst, hA⟩

/-! ## Exact witnesses and attainment -/

theorem DLe.toRLeError {f : PartialBool ι} {e : ℝ} {t : ℕ} (he : 0 ≤ e) (h : DLe f t) :
    RLeError f e t := by
  obtain ⟨T, hT, hc⟩ := h
  refine ⟨.ofTree T, by simpa using hT, fun x b hx => ?_⟩
  rw [RandomizedProgram.success_ofTree, if_pos (hc x b hx)]
  linarith

theorem DLe.toQLeError [Fintype ι] {f : PartialBool ι} {e : ℝ} {t : ℕ} (he : 0 ≤ e)
    (h : DLe f t) : QLeError f e t := by
  cases isEmpty_or_nonempty ι with
  | inl _ => exact .inl (constantOnPromise_of_isEmpty f)
  | inr hι =>
    obtain ⟨i₀⟩ := hι
    obtain ⟨T, hT, hc⟩ := h
    refine .inr ⟨0, ket (readyPoint i₀), .ofTree (readyPoint i₀) T, norm_ket _,
      by simpa using hT, fun x b hx => ?_⟩
    rw [AdaptiveProgram.outputMass_ofTree, if_pos (hc x b hx)]
    linarith

section Attainment

variable [Fintype ι]

theorem RLeError_set_nonempty (f : PartialBool ι) {e : ℝ} (he : 0 ≤ e) :
    {t : ℕ | RLeError f e t}.Nonempty :=
  ⟨_, DLe.toRLeError he (DLe_card f)⟩

theorem QLeError_set_nonempty (f : PartialBool ι) {e : ℝ} (he : 0 ≤ e) :
    {t : ℕ | QLeError f e t}.Nonempty :=
  ⟨_, DLe.toQLeError he (DLe_card f)⟩

/-- For `0 ≤ e` the infimum defining `RError` is attained. -/
theorem RLeError_RError (f : PartialBool ι) {e : ℝ} (he : 0 ≤ e) :
    RLeError f e (RError f e) :=
  Nat.sInf_mem (RLeError_set_nonempty f he)

/-- For `0 ≤ e` the infimum defining `QError` is attained. -/
theorem QLeError_QError (f : PartialBool ι) {e : ℝ} (he : 0 ≤ e) :
    QLeError f e (QError f e) :=
  Nat.sInf_mem (QLeError_set_nonempty f he)

theorem RError_le_of_RLeError {f : PartialBool ι} {e : ℝ} {t : ℕ} (h : RLeError f e t) :
    RError f e ≤ t :=
  Nat.sInf_le h

theorem QError_le_of_QLeError {f : PartialBool ι} {e : ℝ} {t : ℕ} (h : QLeError f e t) :
    QError f e ≤ t :=
  Nat.sInf_le h

/-- A lower bound on `RError`: if every budget that achieves error `e` is at least
`B`, then so is `RError f e` (for `0 ≤ e`). -/
theorem le_RError_of_forall {f : PartialBool ι} {e B : ℝ} (he : 0 ≤ e)
    (h : ∀ t : ℕ, RLeError f e t → B ≤ (t : ℝ)) : B ≤ (RError f e : ℝ) :=
  h _ (RLeError_RError f he)

/-- Lower error costs more: `RError f b ≤ RError f a` when `0 ≤ a ≤ b`. -/
theorem RError_anti {f : PartialBool ι} {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b) :
    RError f b ≤ RError f a :=
  RError_le_of_RLeError ((RLeError_RError f ha).mono_error hab)

/-- Lower error costs more: `QError f b ≤ QError f a` when `0 ≤ a ≤ b`. -/
theorem QError_anti {f : PartialBool ι} {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b) :
    QError f b ≤ QError f a :=
  QError_le_of_QLeError ((QLeError_QError f ha).mono_error hab)

/-- Exact deterministic computation has every nonnegative error: `RError f e ≤ D f`. -/
theorem RError_le_D (f : PartialBool ι) {e : ℝ} (he : 0 ≤ e) : RError f e ≤ D f :=
  RError_le_of_RLeError (DLe.toRLeError he (DLe_D f))

end Attainment

end QuarticQuery.ErrorExplicit
