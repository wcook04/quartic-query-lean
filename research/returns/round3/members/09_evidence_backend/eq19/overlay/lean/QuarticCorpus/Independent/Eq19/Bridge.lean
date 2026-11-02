module

public import QuarticCorpus.Independent.Eq19.Spec
public import QuarticQuery.Paper.Eq19Whole

/-! Proposed bridges to the actual project definitions; not elaborated here. -/

@[expose] public section

open scoped BigOperators

namespace QuarticQuery.Independent.Eq19

variable {κ : Type} {ℓ r S : ℕ}

theorem referenceInput_eq_dummy (J : Column ℓ → Column ℓ)
    (A : Column ℓ → Fin r → BitInput κ) :
    referenceInput (S := S) J A = dummy J A := by
  funext q
  rcases q with ⟨i, j⟩ | ⟨i, h, q⟩ | q
  · by_cases hz : j = J i <;> simp [referenceInput, dummy, hz]
  · rfl
  · rfl

theorem hit_eq_foundZero (T : QueryTree (BitLoc ℓ r S κ))
    (A : Column ℓ → Fin r → BitInput κ)
    (J : Column ℓ → Column ℓ) (i : Column ℓ) :
    hit T A J i = foundZero T A J i := by
  simp only [hit, zeroWasQueried, foundZero, ind, referenceInput_eq_dummy]

theorem zerosSeen_eq_discoveredZeros (T : QueryTree (BitLoc ℓ r S κ))
    (A : Column ℓ → Fin r → BitInput κ) (J : Column ℓ → Column ℓ) :
    zerosSeen T A J = Paper.discoveredZeros T A J := by
  simp only [zerosSeen, zeroWasQueried, Paper.discoveredZeros, referenceInput_eq_dummy]

variable [Fintype κ] [DecidableEq κ]

theorem hitProbability_eq_coupledAvg (μ : BitInput κ → ℝ)
    (T : QueryTree (BitLoc ℓ r S κ)) :
    hitProbability μ T = coupledAvg μ (fun A J I => foundZero T A J I) := by
  simp only [hitProbability, dataWeight, zeroWeight, coupledAvg, avg, prodW,
    unif, hit_eq_foundZero]

theorem expectedCount_eq_expectedZeros (μ : BitInput κ → ℝ)
    (T : QueryTree (BitLoc ℓ r S κ)) :
    expectedCount μ T = Paper.expectedZeros μ T := by
  simp only [expectedCount, dataWeight, zeroWeight, Paper.expectedZeros, avg,
    prodW, unif, zerosSeen_eq_discoveredZeros]

theorem specification_eq19 {μ : BitInput κ → ℝ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : ∑ x, μ x = 1) {G : ℕ}
    (T : QueryTree (BitLoc ℓ r S κ)) (hT : T.depth ≤ G) :
    (hitProbability μ T = expectedCount μ T / ((2 ^ ℓ : ℕ) : ℝ)) ∧
    (hitProbability μ T ≤ 4 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ) ^ 2) := by
  simpa only [hitProbability_eq_coupledAvg, expectedCount_eq_expectedZeros] using
    (Paper.eq19_whole hμ hμ1 T hT)

end QuarticQuery.Independent.Eq19
