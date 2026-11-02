# Section 3: exact statements and proposed Lean proofs

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

This is an advisory proof blueprint and source package for the supplied Section 3, not a replacement for the final paper.

<!-- passage:principal-result -->
The proposed `QuarticQuery.Paper.quantumTournament` gives an actual bounded list as the
measured output of one coherent circuit. Let the candidate set have size \(m\ge2\),
let each coherent comparison use at most \(c\) reads, and suppose its probabilities
satisfy \(a_{ii}=0\), \(a_{ij}+a_{ji}=1\) for distinct candidates. Set
\(T=\lceil\log_2(1000m)\rceil\) and \(\varepsilon=1/(1000T)\).
One circuit, chosen before the input and any dominant candidate, outputs a list
of length at most \(T\). Whenever \(a_{sj}\ge1-\varepsilon\) for every \(j\ne s\),
its output law satisfies

\[
\Pr[s\text{ occurs in the list}]
\ge 1-\frac{2m}{2^T}-T\varepsilon.
\]

Its compiled physical bit-query cap has the explicit uniform bound

\[
C\le6072\,c\sqrt m\,T^2\ln T.
\]

Here `Samples` counts logical reads, while `Runs` counts ordinary bit queries.
`quantumBitOracle_isCirc` represents an ordinary bit query by one read, so a
comparison with the paper's physical cap also supplies a comparison with that
read cap. The final compilation's factor two is included in the constant.
The first inequality is Proposition 3.2. The numerical constant and the explicit
coherent output witness are recorded as auxiliary statements. Every new source
file is **UNELABORATED**: no Lean compiler, Comparator run or independent kernel
check was available. The mathematical arguments below and the executable finite
checks do not change that status.
<!-- endpassage:principal-result -->

## Why the tournament works

<!-- passage:proof-mechanism -->
Write \(w_i(L)=\prod_{p\in L}a_{ip}\) and \(W(L)=\sum_iw_i(L)\), with products
counting the entries of the pivot history. The ideal process samples a new pivot
with probabilities \(w_p/W\). Complementarity pairs the two terms for every
unordered pair, giving the exact drift calculation (13):

\[
\mathbb E[W'\mid w]
=\frac{W^2-\sum_i w_i^2}{2W}\le\frac W2
\qquad(W>0).
\]

No total order or transitivity is needed. If a dominant candidate has not yet
been listed, its surviving weight is at least
\((1-\varepsilon)^{|L|}\ge1-T\varepsilon>1/2\).
Thus a missed dominant candidate implies remaining total weight above one half.
The ideal miss probability is at most \(2m/2^T\), using the existing
`Tournament.ideal_tournament` argument.

The real stage has exactly the ideal conditional pivot law whenever it succeeds.
Its probability of failure, conditional on any reachable history before the
dominant candidate is listed, is at most \(\varepsilon\). Coupling at each such
history therefore adds at most \(T\varepsilon\). Independence between failures
is unnecessary. The auxiliary perfect indicator \(v(s)=1\) appears only in the
proof of list membership; it is absent from the list circuit. This removes the
extra verifier error attached to the supplied Boolean-continuation theorem.
The recursive law explicitly terminates when \(W=0\); it does not interpret a
totalized division by zero as a probability distribution.
<!-- endpassage:proof-mechanism -->

## The full state and its sampling law

<!-- passage:state-and-law -->
Equation (15) retains the complete result of every fresh comparison. For a fixed
history \(p_0,\ldots,p_{t-1}\), it prepares

\[
\frac1{\sqrt m}\sum_i |i\rangle
  \bigotimes_{b<t} A_{i,p_b}|0\rangle.
\]

The new `equation_15` constructs that state as a coordinate identity on finite
registers and proves its read cap. Its tensor basis is nested in reverse pivot
order, a fixed register convention related to the displayed order by a
query-free permutation. `quantumWorkspace_uniformize` first converts a finite
family of pairwise existential `Samples` witnesses into one common workspace,
origin and output map. `quantumTensorStage_of_samples` composes that construction
with the tensor preparation. The successful masses are

\[
\Pr[\mathrm{success},i]=\frac{w_i}{m},\qquad
\Pr[\mathrm{success}]=\frac Wm,\qquad
\Pr[i\mid\mathrm{success}]=\frac{w_i}{W}\quad(W>0).
\]

The supplied `Upper.stage_samples` skips later comparisons after an earlier
failure. It has these successful masses, but its full retained state differs
from (15). The list theorem uses this existing implementation through its exact
law; the separate tensor construction supplies the literal displayed state.
That difference is the accepted finding F-STAGE-LAW. The generic tensor helper
identities also hold for unnormalized vectors as identities of masses. They
become probabilities for the unitary preparation of a normalized basis state.
The conditional statements explicitly require positive successful mass.
<!-- endpassage:state-and-law -->

## How bounded amplification is used

<!-- passage:amplification-use -->
Brassard, Høyer, Mosca and Tapp give the two-dimensional amplitude-amplification
calculation in [BHMT, §2, Lemma 1 and equation (8)]. It preserves the normalized
good component up to a global phase whenever the projected good amplitude is
nonzero. The random
iteration identity used here is [BBHT, arXiv v1, §4, Lemma 2, printed p. 3].
The supplied preprint specializes these ingredients to a fixed finite trial cap.
For \(0<\gamma\le1/2\), \(0<\eta<1/2\) and
\(M=\lceil10/\sqrt\gamma\rceil\), one trial chooses zero iterations with
probability one half and a uniformly random iteration count below \(M\) with the
remaining half. At most \(N=\lceil\ln(1/\eta)/\ln(40/31)\rceil\) trials run.
The padded product actually charged by the implementation obeys

\[
N(2M+1)\le138\,\gamma^{-1/2}\ln(1/\eta)
\quad(0<\gamma\le1/2,\;0<\eta<1/2).
\]

This explicit bound is needed because a bound on a potentially smaller
`Proc.callCap` alone cannot upper-bound `stageCost` or `searchCost`.
`quantum_amplify_samples` retains the random-choice and trial workspaces and
returns a genuine `Samples` witness with the exact successful-label law.
This enables the bounded list to be the measured label. Retaining trial records
does not assert equality of the whole output register with the original good
state. BHMT's expected-time unknown-success result, Theorem 3, is not the source
of the pointwise finite cap. The supplied proof files credit adaptations of
Troy Lee's amplitude geometry and trigonometric-sum files; that code provenance
is preserved separately from the mathematical attribution.
<!-- endpassage:amplification-use -->

## Comparison, verification and the final error

<!-- passage:comparison-verification -->
The comparison wrappers refer to the actual `cmpProb` and `cmp_samples`
implementation. Sorting a pair selects one common unordered comparison circuit;
reversing its interpretation complements the output bit. This proves the
off-diagonal relation in (10). The diagonal probability is zero, and a separate
zero-read implementation handles self-comparisons. When a candidate is a true
winner, only its own decoded address needs a success guarantee. Its probability
of defeating each distinct opponent is at least \(1-\varepsilon\), without an
extra promise on the opponent.

For verification, the fixed-address search is one-sided: if all local tests
pass, it accepts with certainty; if any test fails, acceptance is at most
\(\varepsilon\). A true winner can therefore be rejected only through an
incorrect decoded address. The explicit local-test count, decoder repetition
count, pointer-test cap and search cap are exported in `QuantumComparison`.
The final Boolean decision procedure has the supplied continuation route,
which the new wrappers retain. It satisfies

\[
\Pr[\text{accept a zero-input}]\le T\varepsilon,\qquad
\Pr[\text{reject a one-input}]
\le\frac{2m}{2^T}+T\varepsilon+\varepsilon<\frac13.
\]

The list output theorem and the final Boolean decision theorem are separate
declarations with their actual output types. No new reach claim is made for the
headline upper bound merely because these wrappers import its dependencies.
<!-- endpassage:comparison-verification -->

## Entry for every assigned statement

Each signature below is **unelaborated** and is read in the namespace, imports and variable context of its named source file. `genuine_new_proof` describes new proof work in this package; it makes no claim of mathematical novelty. Definitional rows receive agreement lemmas rather than new mathematical assertions.

### `prop-3.2`

<!-- passage:row-prop-3.2 -->
**Classification:** A new construction or proof is required.

**Mathematical statement.** For m≥2, T=ceil(log₂(1000m)), ε=1/(1000T), and a coherent comparison family of c logical reads with complementary probabilities, there is one normalized list law and one coherent circuit with that list as its measured label. Every label has length at most T. Its physical bit-query cap C satisfies C≤6072 c sqrt(m) T² ln(T), and, for every fixed oracle input x and every ε-dominant s, Pr[s is listed]≥1−2m/2^T−Tε.

**Source.** `paper/extracted.md, Section 3.2, source line 363`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumTournament {ι Col : Type} [Fintype ι] [Inhabited ι]
    [Fintype Col] [DecidableEq Col] {cc : ℕ} {a : BitInput ι → Col → Col → ℝ}
    (hm : 2 ≤ Fintype.card Col) (hc : ∀ x, IsComparison (a x))
    (hcmp : ∀ i p, Samples cc fun x b => bern (a x i p) b) :
    let m := Fintype.card Col
    let T := Tval m
    let ε := epsval m
    ∃ C : ℕ, ∃ law : BitInput ι → QuantumCandidateList Col T → ℝ,
      (C : ℝ) ≤ 6072 * (cc : ℝ) * Real.sqrt (m : ℝ) *
        (T : ℝ) ^ 2 * Real.log (T : ℝ) ∧
      Samples (T * quantumStageReads m T cc ε) law ∧
      Runs C law ∧
      (∀ x o, 0 ≤ law x o) ∧
      (∀ x, ∑ o, law x o = 1) ∧
      ∀ x s, Dominant (a x) ε s →
        1 - 2 * (m : ℝ) / 2 ^ T - T * ε ≤
          ∑ o : QuantumCandidateList Col T, if s ∈ o.1 then law x o else 0
```

**Proof plan.** First construct the bounded output alphabet QuantumCandidateList. Lift finite amplification from Runs to Samples by retaining trial registers. Induct over the remaining number of stages with Samples.bind, returning the existing list on failure. This gives one Samples witness independently of x and s. Prove list-law nonnegativity and total mass one, including the zero-weight branch. Apply the perfect-indicator coupling to its exact expectation and the existing ideal_tournament miss bound. Compile once with Samples.runs and identify its cost by quantumStageReads_compile. Apply the explicit numerical cost inequality.

**Declarations used.** `QuarticQuery.Upper.stage_samples`; `QuarticQuery.Paper.quantum_amplify_samples`; `QuarticQuery.Upper.Samples.bind`; `QuarticQuery.Upper.Samples.runs`; `QuarticQuery.Tournament.ideal_tournament`; `QuarticQuery.Paper.quantumList_coupling`; `QuarticQuery.Paper.quantumListLaw_vall`; `QuarticQuery.Paper.quantumTournament_cost`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumTournament`; `QuarticQuery.Paper.quantumTournament_list`; `QuarticQuery.Paper.quantumListLaw_total`; `QuarticQuery.Paper.quantumListLaw_nonneg`; `QuarticQuery.Paper.quantumBitOracle_isCirc`; `QuarticQuery.Paper.quantumCandidateList_probability`.

**Correspondence and scope.** The supplied Upper.tournament_runs is a Boolean verifier continuation and loses a further verifier ε. The old uncompiled Paper.Section3 candidate addressed list law only through Runs; this return supplies an actual coherent list-label witness as well. The retained-register implementation is an alternative implementation route with the same required law. c ordinary bit queries can be represented by c logical reads using quantumBitOracle_isCirc plus IsCirc composition. The final compiler charges two bit queries per read, already included in 6072. This is proposed source, not a compiled theorem.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-prop-3.2 -->

### `claim-coupling`

<!-- passage:row-claim-coupling -->
**Classification:** A new construction or proof is required.

**Mathematical statement.** Let a be unit-valued, v and f be in [0,1], v(s)=1, and f(L)=1 whenever W(L)=0. Suppose s is ε-dominant, 0≤ε≤1, T₀ε<1/2, and f(L)≤ε for every history of length at most T₀ omitting s. For |L|+n≤T₀, tval(a,v,f,n,L)≥1−missFrom(a,s,n,L)−nε. With v=1_{s}, tval is exactly the probability that the returned list contains s.

**Source.** `paper/extracted.md, Section 3.2, source line 432`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournament.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumList_coupling (ha : UnitValued a) (hv : ∀ c, 0 ≤ v c ∧ v c ≤ 1)
    (hf : ∀ L, 0 ≤ f L ∧ f L ≤ 1) (hz : ∀ L, total (weight a L) = 0 → f L = 1) {s : Col}
    {ε : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) (hd : Dominant a ε s) (hvs : v s = 1) {T₀ : ℕ}
    (hT : (T₀ : ℝ) * ε < 1 / 2) (hfail : ∀ L : List Col, L.length ≤ T₀ → s ∉ L → f L ≤ ε)
    (T : ℕ) (L : List Col) (hL : L.length + T ≤ T₀) :
    1 - missFrom a s T L - T * ε ≤ tval a v f T L
```

**Proof plan.** Adapt tval_lower with a perfect verifier. If s is already listed, le_tval_of_mem gives acceptance at least one. Otherwise half_lt_total permits normalizing the next-pivot law. Apply induction separately at each history. Writing X=1−miss−nε, use X≤1 and f(L)≤ε to prove X−ε≤(1−f(L))X; split on X≥0, since a negative lower-bound bracket is allowed. quantumListLaw_vall and quantumVall_indicator identify the expectation with membership. No independence of stage failures is assumed.

**Declarations used.** `QuarticQuery.Upper.tval_lower`; `QuarticQuery.Upper.le_tval_of_mem`; `QuarticQuery.Tournament.half_lt_total`; `QuarticQuery.Upper.sum_ratio`; `QuarticQuery.Upper.missFrom_nonneg`; `QuarticQuery.Paper.quantumListLaw_vall`; `QuarticQuery.Paper.quantumVall_indicator`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumList_coupling`; `QuarticQuery.Paper.quantumTournament_list`.

**Correspondence and scope.** The new perfect-verifier hypothesis v(s)=1 removes the factor (1−ε) from the analytic lower bound. This verifier is used only in the correctness proof; the constructed list sampler does not receive s. The existing Boolean-program theorem remains valid and distinct.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-coupling -->

### `claim-tournament-cost`

<!-- passage:row-claim-tournament-cost -->
**Classification:** A new construction or proof is required.

**Mathematical statement.** For m≥2, T=ceil(log₂(1000m)), ε=1/(1000T), N=trialCount(ε), M=iterationBound(1/(2m)), the exact compiled cap 2N(2M+1)cT² is at most 6072 c sqrt(m) T² ln(T). The comparison cap c counts logical reads; the factor two converting reads into physical bit queries is already included.

**Source.** `paper/extracted.md, Section 3.2, source line 440`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumTournament_cost {m : ℕ} (hm : 2 ≤ m) (cc : ℕ) :
    ((Tval m * stageCost m (Tval m) cc (epsval m) : ℕ) : ℝ) ≤
      6072 * (cc : ℝ) * Real.sqrt (m : ℝ) *
        (Tval m : ℝ) ^ 2 * Real.log (Tval m : ℝ)
```

**Proof plan.** The new amplification_budget_le gives N(2M+1)≤138 γ^(−1/2)ln(1/ε). Multiply by 2cT², exactly matching the compiled budget. Then sqrt(2m)≤2sqrt(m), T≥2, and ln(1000T)≤11ln(T), because 1000≤2^10≤T^10. This yields 276×2×11=6072. The T-fold coherent stage construction pads each history to the same cT logical reads and compiles only once.

**Declarations used.** `QuarticQuery.Paper.amplification_budget_le`; `QuarticQuery.Upper.stageCost`; `QuarticQuery.Amplification.iterationBound`; `QuarticQuery.Amplification.trialCount`; `QuarticQuery.Paper.quantumStageReads_compile`; `QuarticQuery.Paper.quantumTval_two_le`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumTournament_cost`; `QuarticQuery.Paper.quantumTournament_cost_log`; `QuarticQuery.Paper.quantumStageReads`; `QuarticQuery.Paper.quantumStageReads_compile`.

**Correspondence and scope.** A bound on Proc.callCap alone would not justify the product used by stageCost; the extracted amplification_budget_le bounds that product itself. The paper uses a big-O assertion, so this explicit numerical constant is a valid stronger quantitative form after compilation. The literal integer cap is retained, including ceilings and the compiler factor two.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-tournament-cost -->

### `def-grover-trial`

<!-- passage:row-def-grover-trial -->
**Classification:** Already stated under another name; agreement supplied.

**Mathematical statement.** For γ>0 and 0<η≤1, M=ceil(10/sqrt(gamma)); N=ceil(log(1/eta)/log(40/31)); a trial chooses ell=0 with half the probability and ell uniform in {0,...,M-1} with the other half, uses G^ell A, measures success, and restarts on failure, stopping after at most N trials.

**Source.** `paper/extracted.md:332-352`. Proposed source: `lean/QuarticQuery/Paper/QuantumAmplification.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantum_grover_parameters (γ η : ℝ) :
    iterationBound γ = ⌈10 / Real.sqrt γ⌉₊ ∧
    trialCount η = ⌈Real.log (1 / η) / Real.log (40 / 31)⌉₊ ∧
    amplify γ η = attempts (iterationBound γ) (trialCount η)
```

**Proof plan.** Use definitional equality for parameters/recursion, trialWeight_nonneg and sum_trialWeight for the mixture, callCap_attempts for every branch. The new Samples transport uses Samples.gate, Samples.bind, Samples.pure and IsCirc.mono to retain independent workspaces.

**Declarations used.** `QuarticQuery.Amplification.iterationBound`; `QuarticQuery.Amplification.trialCount`; `QuarticQuery.Amplification.amplify`; `QuarticQuery.Amplification.attempts`; `QuarticQuery.Amplification.trialWeight`; `QuarticQuery.Amplification.sum_trialWeight`; `QuarticQuery.Amplification.callCap_attempts`.

**Related proposed declarations.** `QuarticQuery.Paper.quantum_grover_parameters`; `QuarticQuery.Paper.quantum_grover_trial_distribution`; `QuarticQuery.Paper.quantum_grover_trial_recursion`; `QuarticQuery.Paper.quantum_grover_call_cap`.

**Correspondence and scope.** The construction already exists in Proc. Agreement is by unfolding the parameter definitions and one recursion equation; normalization requires M != 0, supplied by gamma > 0. Proc.restart represents a fresh start. The separate coherent transport quantum_amplify_samples retains every trial workspace and proves the successful label law. Full-state semantics remain in Amplification.bounded_amplification. Adjudication M-1 requires one procedure fixed from gamma, eta before A; this is preserved. Prior proposal new-upper-call-cap is relevant; no strengthening of the source statement is asserted merely by a doc tag.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-def-grover-trial -->

### `claim-grover-state`

<!-- passage:row-claim-grover-state -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For 0<p<1, choose theta in (0,pi/2) and normalized orthogonal good and bad vectors with A|0>=sin(theta)|g>+cos(theta)|b>. Every Grover iterate equals sin((2ell+1)theta)|g>+cos((2ell+1)theta)|b>, and whenever its good component is nonzero its normalized good component is |g> up to phase.

**Source.** `paper/extracted.md:321-330`. Proposed source: `lean/QuarticQuery/Paper/QuantumAmplification.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantum_grover_state (A : Preparation H) (h0 : 0 < A.prob) (h1 : A.prob < 1) :
    (0 < A.angle ∧ A.angle < Real.pi / 2) ∧
    ‖A.goodState‖ = 1 ∧ ‖A.badState‖ = 1 ∧
    A.good A.goodState = A.goodState ∧ A.good A.badState = 0 ∧
    inner ℂ A.goodState A.badState = 0 ∧
    A.state = ((Real.sin A.angle : ℝ) : ℂ) • A.goodState +
      ((Real.cos A.angle : ℝ) : ℂ) • A.badState ∧
    ∀ ℓ : ℕ,
      A.iterate ℓ =
        ((Real.sin ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.goodState +
        ((Real.cos ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.badState ∧
      (A.good (A.iterate ℓ) ≠ 0 →
        PhaseEq (normalised (A.good (A.iterate ℓ))) A.goodState)
```

**Proof plan.** Use the existing state and iterate formulas. From norm_badPart_sq and p<1 deduce badPart != 0 and normalize it. Orthogonality follows from the self-adjoint projector and good_goodState/good_badState. Nonzero projected mass forces nonzero sine, enabling phaseEq_normalised_good_iterate.

**Declarations used.** `QuarticQuery.Amplification.Preparation.angle_mem`; `QuarticQuery.Amplification.Preparation.norm_goodState`; `QuarticQuery.Amplification.Preparation.norm_badPart_sq`; `QuarticQuery.Amplification.norm_normalised`; `QuarticQuery.Amplification.Preparation.good_goodState`; `QuarticQuery.Amplification.Preparation.good_badState`; `QuarticQuery.Amplification.Preparation.state_eq`; `QuarticQuery.Amplification.Preparation.iterate_eq`; `QuarticQuery.Amplification.Preparation.good_iterate`; `QuarticQuery.Amplification.Preparation.phaseEq_normalised_good_iterate`; `QuarticQuery.Amplification.Preparation.good_iterate_of_prob_zero`.

**Related proposed declarations.** `QuarticQuery.Paper.quantum_grover_state`; `QuarticQuery.Paper.quantum_grover_zero`.

**Correspondence and scope.** The single wrapper includes both normalized vectors, their projector behavior and orthogonality, the angle range, initial decomposition, all iterates and conditional phase preservation. A positive initial p does not guarantee positive success mass at every chosen iteration. The final implication requires the actual good component to be nonzero; when it is zero no conditional state is claimed. This makes the implicit event condition in the original text explicit. Prior numerical examples new-amplification-arithmetic and new-amplification-concrete-state are out of this Section 3 closure and remain proposed examples.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-grover-state -->

### `claim-sin2theta`

<!-- passage:row-claim-sin2theta -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For the Grover angle with sin²θ=p and 0<γ≤p≤1/2, sin(2θ)=2 sqrt(p(1−p))≥sqrt(γ).

**Source.** `paper/extracted.md:335-338`. Proposed source: `lean/QuarticQuery/Paper/QuantumAmplification.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantum_sin_two_angle (A : Preparation H) {γ : ℝ}
    (hp : γ ≤ A.prob) (hhalf : A.prob ≤ 1 / 2) :
    Real.sin (2 * A.angle) = 2 * Real.sqrt (A.prob * (1 - A.prob)) ∧
    Real.sqrt γ ≤ Real.sin (2 * A.angle)
```

**Proof plan.** Rewrite sin(2theta) with Preparation.sin_two_angle. Both sides are nonnegative. After squaring, 4p(1-p)>=gamma follows from p>=gamma and p<=1/2. The proof is copied from the local hs argument in Bounded.lean.

**Declarations used.** `QuarticQuery.Amplification.Preparation.sin_two_angle`; `QuarticQuery.Amplification.Preparation.prob_nonneg`; `Real.sqrt_le_iff`; `Real.sq_sqrt`.

**Related proposed declarations.** `QuarticQuery.Paper.quantum_sin_two_angle`.

**Correspondence and scope.** The equality is already named; the inequality existed only as a local have inside Preparation.nine_fortieths_le. The wrapper extracts that same calculation. Its signature permits gamma <= 0 because Real.sqrt then gives zero; the paper uses only gamma>0. The paper statement is unchanged.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-sin2theta -->

### `eq-9`

<!-- passage:row-eq-9 -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For gamma>0, gamma<=p<=1/2 and M=ceil(10/sqrt(gamma)), (1/M)sum_{ell<M}sin^2((2ell+1)theta)>=1/2-1/(2M|sin(2theta)|)>=9/20.

**Source.** `paper/extracted.md:339-343`. Proposed source: `lean/QuarticQuery/Paper/QuantumAmplification.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantum_eq_9 (A : Preparation H) {γ : ℝ} (hγ : 0 < γ)
    (hp : γ ≤ A.prob) (hhalf : A.prob ≤ 1 / 2) :
    let M := iterationBound γ
    (1 / 2 - 1 / (2 * (M : ℝ) * |Real.sin (2 * A.angle)|) ≤
      (1 / (M : ℝ)) * ∑ ℓ ∈ Finset.range M,
        Real.sin ((2 * ℓ + 1) * A.angle) ^ 2) ∧
    (9 / 20 : ℝ) ≤ 1 / 2 - 1 / (2 * (M : ℝ) * |Real.sin (2 * A.angle)|)
```

**Proof plan.** Obtain sqrt(gamma)<=sin(2theta) from quantum_sin_two_angle and M>=10/sqrt(gamma) from Nat.le_ceil. Then M sin(2theta)>=10; the reciprocal term is at most 1/20. Apply average_sin_sq_ge for the first inequality and linarith for the second.

**Declarations used.** `QuarticQuery.Paper.quantum_sin_two_angle`; `QuarticQuery.Amplification.average_sin_sq_ge`; `QuarticQuery.Amplification.iterationBound_ne_zero`; `Nat.le_ceil`; `Real.sqrt_pos`; `one_div_le_one_div_of_le`.

**Related proposed declarations.** `QuarticQuery.Paper.quantum_eq_9`.

**Correspondence and scope.** Both links of the literal displayed chain are included. Existing average_sin_sq_ge_nine_twentieths proves the final endpoint under an angle premise, which by itself does not name the middle lower bound. gamma>0 forces M>=1 and sin(2theta)>0, so all denominators are valid. Prior new-upper-average-exact is already the type of Amplification.average_sin_sq; the new wrapper proves the paper chain instead of silently replacing it by that stronger identity.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-eq-9 -->

### `claim-coherent-access`

<!-- passage:row-claim-coherent-access -->
**Classification:** Already stated under another name; agreement supplied.

**Mathematical statement.** Computing a fixed global bit address is query free. An addressed controlled read costs two bit-oracle calls by load/use/unload, reversal preserves the number of coherent reads, and a pointer with ell bits followed by its target costs at most 2(ell+1) bit queries through the generic compiler.

**Source.** `paper/extracted.md:507-512; see also 282-287`. Proposed source: `lean/QuarticQuery/Paper/QuantumAmplification.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantum_controlled_bit_query {ι Z : Type} [Fintype ι] [Inhabited ι]
    [Fintype Z] {w : ℕ} (e : Z ↪ Fin (w + 1)) (R : ReadSpec ι Z) :
    ∃ P : AdaptiveProgram ι w → AdaptiveProgram ι w, ∀ next,
      (P next).queryCap = 2 + next.queryCap ∧
      ∀ x ψ b, (P next).outputMass x (clEmb e ψ) b =
        next.outputMass x (clEmb e (R.op x ψ)) b
```

**Proof plan.** Re-export exact compile_read and compile_circ interfaces, plus IsCirc.sigma and IsCirc.symm. Apply Samples.tree to an adaptive pointer tree; disqTree_depth and disqTree_eval identify its depth and semantics. Compile via Samples.runs. No assumption that a pointer depends on a fixed small coordinate set is used.

**Declarations used.** `QuarticQuery.Upper.IsCirc.symm`; `QuarticQuery.Upper.IsCirc.sigma`; `QuarticQuery.Upper.compile_read`; `QuarticQuery.Upper.compile_circ`; `QuarticQuery.Upper.Samples.tree`; `QuarticQuery.Upper.Samples.disq`; `QuarticQuery.Upper.Samples.runs`; `QuarticQuery.Upper.disqTree_depth`; `QuarticQuery.Upper.disqTree_eval`; `QuarticQuery.Q_reindex`.

**Related proposed declarations.** `QuarticQuery.Paper.quantum_controlled_bit_query`; `QuarticQuery.Paper.quantum_inverse_reads`; `QuarticQuery.Paper.quantum_controlled_reads`; `QuarticQuery.Paper.quantum_compile_circuit`; `QuarticQuery.Paper.quantum_coherent_tree`; `QuarticQuery.Paper.quantumComparison_pointer_queries`; `QuarticQuery.Paper.quantumBitRead`; `QuarticQuery.Paper.quantumBitRead_eq`; `QuarticQuery.Paper.quantumBitOracle_isCirc`.

**Correspondence and scope.** The row is an implementation claim with several clauses, so it maps to several exact interfaces. A ReadSpec has an input-independent address function on retained basis labels. compile_read loads/uses/unloads and preserves an arbitrary continuation with two physical bit queries. IsCirc.sigma supplies superposed control; IsCirc.symm preserves read counts. The pointer-specific Runs cap 2*(2t+1) is provided in QuantumComparison.lean. Typed BitLoc coordinates are harmless: any fixed enumeration preserves Q by Q_reindex. Prior NEW-FOR-28 proposes a sharper phase-only single-query implementation; it is not implied by this generic two-query compiler.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-coherent-access -->

### `def-aij`

<!-- passage:row-def-aij -->
**Classification:** Already stated under another name; agreement supplied.

**Mathematical statement.** For the actual constructed comparison, a_ij is cmpProb n x i j, the probability that the measured output says i defeats j; a_ii=0. One fixed sorted-pair circuit is reused in the reverse ordering.

**Source.** `paper/extracted.md, Section 3.2, source line 356`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumComparison_unordered_state (hk : 1 ≤ k) (n : ℕ)
    (i j : Col t) (hij : i ≠ j) :
    ∃ (Z : Type) (_ : Fintype Z) (o : Z) (out : Z → Bool)
      (F : BitInput (Loc k t C) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
      IsCirc (cmpCost k t n) F ∧
      ∀ x b,
        lawOf (F x (rket o)) out b = bern (cmpProb n x i j) b ∧
        lawOf (F x (rket o)) (fun z => !(out z)) b = bern (cmpProb n x j i) b
```

**Proof plan.** The source cmpProb definition fixes the table. quantumComparison_unordered_state supplies one fixed preparation with its two output interpretations for i versus j and j versus i. quantumComparison_self records the diagonal convention.

**Declarations used.** `QuarticQuery.Upper.cmpProb`; `QuarticQuery.Upper.cmp_samples`; `QuarticQuery.Paper.quantumComparison_unordered_state`; `QuarticQuery.Paper.quantumComparison_self`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumComparison_unordered_state`; `QuarticQuery.Paper.quantumComparison_self`.

**Correspondence and scope.** A definition is paired with a proof that the implemented circuit has its stated law. Algebraic IsComparison alone would not identify those numbers with an actual circuit.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-def-aij -->

### `eq-10`

<!-- passage:row-eq-10 -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For the actual comparison procedure, cmpProb(n,x,i,j)+cmpProb(n,x,j,i)=1 whenever i≠j, and cmpProb(n,x,i,i)=0.

**Source.** `paper/extracted.md, Section 3.2, source line 359`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumComparison_complementary (n : ℕ)
    (x : BitInput (Loc k t C)) (i j : Col t) (hij : i ≠ j) :
    cmpProb n x i j + cmpProb n x j i = 1
```

**Proof plan.** Project complementary and self_zero from the existing cmpProb_isComparison theorem. The core uses one sorted-pair circuit and flips the output interpretation for the reverse orientation.

**Declarations used.** `QuarticQuery.Upper.cmpProb_isComparison`; `QuarticQuery.Upper.cmpProb`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumComparison_complementary`; `QuarticQuery.Paper.quantumComparison_self`.

**Correspondence and scope.** No fixed orientation or probability gap from 1/2 is introduced for nonwinners. The probabilities may be fractional and cyclic.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-eq-10 -->

### `def-decode`

<!-- passage:row-def-decode -->
**Classification:** Already stated under another name; agreement supplied.

**Mathematical statement.** For k≥1 and any natural repetition count n, for every oracle input, the retained-workspace decoder has the product law D_i(s)=∏_h Bernoulli(decodeProb(A_{i,h}))(s_h) on all r=40t-bit addresses; its law is nonnegative and sums to one.

**Source.** `paper/extracted.md, Section 3.3, source line 452`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumDecode (hk : 1 ≤ k) (n : ℕ) (i : Col t) :
    Samples (addrCost k t n) fun (x : BitInput (Loc k t C)) s =>
      addrLaw n x i s
```

**Proof plan.** Use addr_samples directly. Its proof uses decode_samples independently at each h and Samples.pi. Use sum_addrLaw and addrLaw_nonneg for totality, including off-promise inputs.

**Declarations used.** `QuarticQuery.Upper.addr_samples`; `QuarticQuery.Upper.addrLaw`; `QuarticQuery.Upper.Samples.pi`; `QuarticQuery.Upper.sum_addrLaw`; `QuarticQuery.Upper.addrLaw_nonneg`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumDecode`; `QuarticQuery.Paper.quantumDecode_total`.

**Correspondence and scope.** This construction needs a definition and a realizability theorem. A tautological restatement of the address type alone would not establish an algorithm. The chosen circuit is fixed before the input.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-def-decode -->

### `claim-decode-cost`

<!-- passage:row-claim-decode-cost -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** Assume k≥1, t≥1, r=40t and 0<ε≤1. If all r partial instances define the string s and n≥repetitions(k,ε/r), the actual decoder returns s with probability at least 1−ε and at most 2rnk physical bit queries on every branch. At the least prescribed n, its cost is at most 2rk[1+16·2^(10k) ln(r/ε)]. The supplied finite polynomial estimate is extracted at ε=epsval(m).

**Source.** `paper/extracted.md, Section 3.3, source line 456`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumDecode_correct (hk : 1 ≤ k) (ht : 1 ≤ t)
    {n : ℕ} {ε : ℝ} (hε : 0 < ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n)
    {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t}
    (hs : ∀ h, P k t (readA x i h) = some (s h)) :
    1 - ε ≤ addrLaw n x i s
```

**Proof plan.** Correctness is addrLaw_good. Samples.runs turns each logical read into two bit queries. Apply repetitions_le to η=ε/(40t), establish η∈(0,1], and multiply its real bound by 80tk. The polynomial specialization copies the local repetition-count proof in Upper.budget_le.

**Declarations used.** `QuarticQuery.Upper.addrLaw_good`; `QuarticQuery.Forrelation.repetitions_le`; `QuarticQuery.Upper.Samples.runs`; `QuarticQuery.Upper.Tval_mValue_le`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumDecode_correct`; `QuarticQuery.Paper.quantumDecode_runs`; `QuarticQuery.Paper.quantumDecode_query_bound_real`; `QuarticQuery.Paper.quantumDecode_repetitions_polylog`; `QuarticQuery.Paper.quantumDecode_polylog`.

**Correspondence and scope.** Cost claims for the least prescribed repetition count must not be generalized to every arbitrarily oversized n. The source charges 2rnk physical queries, not rnk. The additive 1 in the count is explicit; with r≥40 and ε≤1 it is absorbed by the positive logarithm in the paper’s O_k statement.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-decode-cost -->

### `def-comparison`

<!-- passage:row-def-comparison -->
**Classification:** Already stated under another name; agreement supplied.

**Mathematical statement.** For i<j, compare independently decoded addresses s₁ and s₂. Let d₁ mean that i disqualifies j, and d₂ that j disqualifies i. The first index wins if d₁=d₂, and otherwise iff d₁=true. Its probability is the double mixture over the two address laws. A self-comparison has a zero-read implementation returning false.

**Source.** `paper/extracted.md, Section 3.3, source line 466`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumComparison_sorted (n : ℕ) (x : BitInput (Loc k t C))
    (i j : Col t) (hij : i < j) :
    cmpProb n x i j =
      ∑ s₁, addrLaw n x i s₁ * ∑ s₂, addrLaw n x j s₂ *
        (if firstWins (disq x i s₁ j hij.ne')
          (disq x j s₂ i hij.ne) then (1 : ℝ) else 0)
```

**Proof plan.** Unfold cmpProb at i<j and coreProb to obtain the mixture. Check the four Boolean pairs for firstWins. The pointer computation uses the existing adaptive tree of depth 2t+1; apply Samples.runs. Obtain the self law from Samples.pure false.

**Declarations used.** `QuarticQuery.Upper.firstWins`; `QuarticQuery.Upper.coreProb`; `QuarticQuery.Upper.cmpProb`; `QuarticQuery.Upper.Samples.disq`; `QuarticQuery.Upper.disqTree_eval`; `QuarticQuery.Upper.disqTree_depth`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumComparison_sorted`; `QuarticQuery.Paper.quantumComparison_rule`; `QuarticQuery.Paper.quantumComparison_disqualification`; `QuarticQuery.Paper.quantumComparison_pointer_queries`; `QuarticQuery.Paper.quantumComparison_self_zero_reads`.

**Correspondence and scope.** The pointer’s target coordinate depends on the bits just read. No fixed small coordinate support is asserted. The uniform common-length comparison may pad the self branch with identity reads; the zero-read self specialization is supplied explicitly.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-def-comparison -->

### `claim-comparison-state`

<!-- passage:row-claim-comparison-state -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For k≥1 and any natural repetition count n, there is an input-independent circuit family whose measured Boolean law is Bernoulli(cmpProb), with cmpCost logical reads, and its inverse has the same count. Its physical bit-query cap is 2·cmpCost. For every input, a_ij+a_ji=1 for distinct indices and a_ii=0. The displayed finite polynomial comparison cap proves the claimed fixed-k polylogarithmic bound.

**Source.** `paper/extracted.md, Section 3.3, source line 472`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumComparison_state (hk : 1 ≤ k) (n : ℕ) (i j : Col t) :
    ∃ (Z : Type) (_ : Fintype Z) (o : Z) (out : Z → Bool)
      (F : BitInput (Loc k t C) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
      IsCirc (cmpCost k t n) F ∧
      IsCirc (cmpCost k t n) (fun x => (F x).symm) ∧
      ∀ x b, lawOf (F x (rket o)) out b = bern (cmpProb n x i j) b
```

**Proof plan.** Destructure cmp_samples to recover a register, a basis start, an output labelling and IsCirc witness. Apply IsCirc.symm to that same circuit. The logical-to-physical compiler gives a factor of two both ways. Project complementary and self_zero from cmpProb_isComparison. Expand cmpCost, use the decoder bound, and extract the polynomial specialization from its repetition estimate.

**Declarations used.** `QuarticQuery.Upper.cmp_samples`; `QuarticQuery.Upper.core_samples`; `QuarticQuery.Upper.Samples.bind`; `QuarticQuery.Upper.IsCirc.symm`; `QuarticQuery.Upper.cmpProb_isComparison`; `QuarticQuery.Upper.Samples.runs`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumComparison_state`; `QuarticQuery.Paper.quantumComparison_unordered_state`; `QuarticQuery.Paper.quantumComparison_runs`; `QuarticQuery.Paper.quantumComparison_cost_exact`; `QuarticQuery.Paper.quantumComparison_query_bound`; `QuarticQuery.Paper.quantumComparison_polylog`; `QuarticQuery.Paper.quantumComparison_complementary`; `QuarticQuery.Paper.quantumComparison_self`.

**Correspondence and scope.** The semantic claim is equality of measured probabilities to the retained-register mixture. No state equation for the separate stage sampler is inferred here. Costs distinguish logical reads from physical calls. The original source already proves complementarity; the missing item was a reviewed tie to that theorem.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-comparison-state -->

### `claim-winner-dominates`

<!-- passage:row-claim-winner-dominates -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** Assume k≥1, t≥1 and 0<ε≤1. For any input x, if i wins at its true address s and n≥repetitions(k,ε/(40t)), then a_ij≥1−ε for every j≠i. No promise is imposed on any instance in column j.

**Source.** `paper/extracted.md, Section 3.3, source line 477`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumWinner_dominates (hk : 1 ≤ k) (ht : 1 ≤ t)
    {n : ℕ} {ε : ℝ} (hε : 0 < ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n)
    {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t}
    (hw : WinsAt (P k t) C (2 * t) (40 * t) x i s)
    (j : Col t) (hji : j ≠ i) :
    1 - ε ≤ cmpProb n x i j
```

**Proof plan.** The winning-address clause of WinsAt supplies every promised answer. Apply addrLaw_good, then transitivity with cmpProb_winner. Package the result into Dominant for direct use by the tournament.

**Declarations used.** `QuarticQuery.Upper.addrLaw_good`; `QuarticQuery.Upper.cmpProb_winner`; `QuarticQuery.Tournament.Dominant`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumWinner_dominates`; `QuarticQuery.Paper.quantumWinner_isDominant`.

**Correspondence and scope.** The winner’s own decoder can err. The required probability is obtained only after combining the decoder bound with cmpProb_winner; the deterministic pointer facts alone are insufficient.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-winner-dominates -->

### `def-verify`

<!-- passage:row-def-verify -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For ε>0, at a fixed address, search uniformly among the exact local tests, accepting if the bounded search reports no failed test. All-passing addresses are accepted with probability one; any failed test gives acceptance at most ε. Fresh decoding followed by that search has acceptance v_i=Σ_s D_i(s) f_{i,s}. The list is accepted at its first accepted candidate.

**Source.** `paper/extracted.md, Section 3.3, source line 483`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumVerify_fixedAddress (i : Col t) (s : Addr t)
    {ε : ℝ} (hε : 0 < ε) :
    ∃ f : BitInput (Loc k t C) → ℝ,
      (∀ x, 0 ≤ f x ∧ f x ≤ 1) ∧
      (∀ x e, localTest C (2 * t) (40 * t) x i s e = false → f x ≤ ε) ∧
      (∀ x, (∀ e, localTest C (2 * t) (40 * t) x i s e = true) → f x = 1) ∧
      Runs (searchCost t (Fintype.card (Tests t C)) ε) fun x b => bern (f x) b
```

**Proof plan.** Reuse search_runs for each column-address pair, retaining its four conjuncts. Use addr_samples.runs.bind to compose a measured fresh address with the selected search; verify the Bernoulli law in both Boolean cases. Use vall_runs for the final OR, and card_testIndex for the size and positivity of the test family.

**Declarations used.** `QuarticQuery.Upper.search_runs`; `QuarticQuery.Upper.verifyProb`; `QuarticQuery.Upper.addr_samples`; `QuarticQuery.Upper.Runs.bind`; `QuarticQuery.Upper.vall_runs`; `QuarticQuery.card_testIndex`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumVerify_fixedAddress`; `QuarticQuery.Paper.quantumVerify_runs`; `QuarticQuery.Paper.quantumVerify_probability`; `QuarticQuery.Paper.quantumVerify_list`; `QuarticQuery.Paper.quantumTests_card`; `QuarticQuery.Paper.quantumTests_card_ge_m`; `QuarticQuery.Paper.quantumTests_card_ge_four`.

**Correspondence and scope.** The result is a family of programs chosen before x. No oracle-dependent value is inserted into a free gate. The exact search cost excludes fresh decoding, which is then added explicitly.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-def-verify -->

### `claim-verify`

<!-- passage:row-claim-verify -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** Assume k≥1, t≥1, 0<ε≤1, C realizes P(k,t), and n≥repetitions(k,ε/(40t)). A fixed verification procedure has acceptance at most ε for every nonwinner, and at least 1−ε for every winner. At the winner’s true address the search accepts surely; only address decoding can cause its rejection. Its cap is 2·addrCost+searchCost. For K≥2 and 0<ε<1/2, searchCost≤276√K ln(1/ε) max(3,2t+1). At the paper parameters and least prescribed repetition count, if C.size≤forrConstant(k)·m·(2t)^2, the whole single-candidate cap is at most budgetConst(k)·2^t·(2t)^6. The selected forrCircuit satisfies this size premise. Since m=4^t, this is an explicit sqrt(m)·(log₂ m)^6 bound.

**Source.** `paper/extracted.md, Section 3.3, source line 490`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumVerify (hk : 1 ≤ k) (ht : 1 ≤ t)
    (hC : CircuitRealises C (P k t)) {n : ℕ} {ε : ℝ}
    (hε : 0 < ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n) :
    ∃ v : BitInput (Loc k t C) → Col t → ℝ,
      (∀ c, Runs (2 * addrCost k t n + searchCost t (Fintype.card (Tests t C)) ε)
        fun x b => bern (v x c) b) ∧
      (∀ x c, 0 ≤ v x c ∧ v x c ≤ 1) ∧
      (∀ x c, (¬ ∃ s, WinsAt (P k t) C (2 * t) (40 * t) x c s) → v x c ≤ ε) ∧
      (∀ x c s, WinsAt (P k t) C (2 * t) (40 * t) x c s → 1 - ε ≤ v x c)
```

**Proof plan.** For a nonwinner, exists_failing_localTest supplies a failed test at each address. Multiply its acceptance bound by the nonnegative address law and sum to ε. For a winner, winsAt_iff_localTests makes the fixed-address acceptance one; retain its nonnegative summand and lower-bound its address mass. Choose all searches once and combine the results into quantumVerify. The search bound uses amplification_budget_le on γ=1/K, not the abstract Proc cap, because searchCost charges the padded product. To specialize from K to m, use Tval_pos to put one verification below T copies, then below the complete budget; apply Upper.budget_le with the explicit circuit-size premise. Instantiate that premise with forrCircuit_size_le for the selected circuit.

**Declarations used.** `QuarticQuery.Upper.search_runs`; `QuarticQuery.exists_failing_localTest`; `QuarticQuery.winsAt_iff_localTests`; `QuarticQuery.Upper.addrLaw_good`; `QuarticQuery.Upper.addrLaw_nonneg`; `QuarticQuery.Upper.sum_addrLaw`; `QuarticQuery.Paper.amplification_budget_le`; `QuarticQuery.Upper.budget_le`; `QuarticQuery.Upper.budgetConst`; `QuarticQuery.Forrelation.forrCircuit_size_le`; `QuarticQuery.Tournament.Tval_pos`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumVerify`; `QuarticQuery.Paper.quantumVerify_unit`; `QuarticQuery.Paper.quantumVerify_nonwinner`; `QuarticQuery.Paper.quantumVerify_winner`; `QuarticQuery.Paper.quantumVerify_testCost`; `QuarticQuery.Paper.quantumVerify_search_query_bound`; `QuarticQuery.Paper.quantumVerify_polylog`; `QuarticQuery.Paper.quantumVerify_forrCircuit_polylog`.

**Correspondence and scope.** This preserves exact one-sided behavior of the local test. A generic two-sided noisy verifier would require a different error budget. The explicit 276 bound is new numerical packaging of existing ingredients, and is unelaborated. The sqrt(m) specialization requires the stated circuit-size bound; CircuitRealises alone does not control K. The exported bound includes fresh decoding and uses the deliberately loose existing budgetConst with exponent six.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-verify -->

### `claim-error`

<!-- passage:row-claim-error -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** Assume k≥1, t≥1, C realizes P(k,t), and n is at least the prescribed repetition count. One algorithm, fixed before the input, has the supplied budget cap and acceptance probability v(x). If F(x)=0 then v(x)≤Tε. If F(x)=1 then 1−v(x)≤2m/2^T+Tε+ε<1/3, with T=ceil(log₂(1000m)), ε=1/(1000T).

**Source.** `paper/extracted.md, Section 3.3, source line 497`. Proposed source: `lean/QuarticQuery/Paper/QuantumComparison.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumError_bound (hk : 1 ≤ k) (ht : 1 ≤ t)
    (hC : CircuitRealises C (P k t)) {n : ℕ}
    (hn : repetitions k (epsval (mValue t) / (40 * t : ℕ)) ≤ n) :
    ∃ val : BitInput (Loc k t C) → ℝ,
      Runs (budget k t n (Fintype.card (Tests t C)))
        (fun x b => bern (val x) b) ∧
      (∀ x, Fkm k t C x = false →
        val x ≤ (Tval (mValue t) : ℝ) * epsval (mValue t)) ∧
      (∀ x, Fkm k t C x = true →
        1 - val x ≤ 2 * (mValue t : ℝ) / 2 ^ Tval (mValue t) +
          (Tval (mValue t) : ℝ) * epsval (mValue t) + epsval (mValue t))
```

**Proof plan.** Build the single-candidate verifier by quantumVerify, and invoke tournament_runs with the actual cmp_samples law. On zero inputs every column lacks a winning address. On one inputs extract a winning column and address, apply quantumWinner_isDominant and the winning verifier bound. Rearrange the existing acceptance inequality. Keep the full Runs witness in the conclusion; use total_error_lt only for its final strict numerical consequence.

**Declarations used.** `QuarticQuery.Upper.tournament_runs`; `QuarticQuery.Upper.Fkm_QLe`; `QuarticQuery.addressedF_eq_true_iff`; `QuarticQuery.Tournament.Tval_mul_epsval`; `QuarticQuery.Tournament.total_error_lt`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumError_bound`; `QuarticQuery.Paper.quantumError_numeric`.

**Correspondence and scope.** This theorem exposes the two probability estimates already used inside Fkm_QLe. It is not merely a restatement of QLe or a numeric bound <1/3. The proof uses the reached Boolean continuation route; it does not itself construct the list-valued Proposition 3.2, which is handled by QuantumTournament.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-error -->

### `construct-sampler`

<!-- passage:row-construct-sampler -->
**Classification:** A new construction or proof is required.

**Mathematical statement.** For a finite nonempty candidate set of size m, a coherent comparison family of c logical reads yields, for each fixed history of t pivots, a coherent stage of tc reads with successful index mass m^(-1)∏_{b<t}aᵢ,p_b. QuantumTensor supplies the full fresh-register implementation. quantumStage_samples separately exports the existing short-circuit implementation at the same cap and successful masses.

**Source.** `paper/extracted.md, Section 3.2, source line 409`. Proposed source: `lean/QuarticQuery/Paper/QuantumTensor.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumTensorStage_of_samples {ι Col : Type} [Fintype Col] [Nonempty Col]
    {c : ℕ} {a : BitInput ι → Col → Col → ℝ}
    (hcmp : ∀ i j, Samples c fun x b => bern (a x i j) b)
    (p : ℕ → Col) (t : ℕ) :
    ∃ L : BitInput ι → Option Col → ℝ,
      Samples (t * c) L ∧
      ∀ x i, L x (some i) =
        (∏ b ∈ Finset.range t, a x i (p b)) / Fintype.card Col
```

**Proof plan.** Use stage_samples for the stage, quantum_amplify_samples for each history, and the quantumTournament_list induction using Samples.bind. Histories are classical labels retained coherently, which are orthogonal. On failure the branch labels its accumulated list; later gates on that branch are padded identities. The additional direct construction first applies quantumWorkspace_uniformize to Col×Col, then quantumTensorStage and equation_15_index_law. The result quantumTensorStage_of_samples needs exactly the same comparison-law interface.

**Declarations used.** `QuarticQuery.Upper.stage_samples`; `QuarticQuery.Paper.quantum_amplify_samples`; `QuarticQuery.Upper.Samples.bind`; `QuarticQuery.Paper.quantumTournament_list`; `QuarticQuery.Paper.quantumWorkspace_uniformize`; `QuarticQuery.Paper.quantumTensorStage`; `QuarticQuery.Paper.equation_15_index_law`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumTensorStage_of_samples`; `QuarticQuery.Paper.quantumTensorStage`; `QuarticQuery.Paper.quantumStage_samples`; `QuarticQuery.Paper.quantumWorkspace_uniformize`; `QuarticQuery.Paper.quantumTournament_list`.

**Correspondence and scope.** F-STAGE-LAW is accepted in the adjudication: stage_samples may skip later comparisons after an earlier failure, so its complete workspace state is not literally (15). Successful index masses are exact. The separate QuantumTensor construction runs every comparison and supplies the literal displayed state. Keep these routes distinguished. The primary proposed declaration now supplies the literal fresh-tensor route from pairwise Samples witnesses. Successful masses agree; equality of the two full retained states is neither needed nor asserted.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-construct-sampler -->

### `eq-15`

<!-- passage:row-eq-15 -->
**Classification:** A new construction or proof is required.

**Mathematical statement.** For a finite nonempty candidate set of size m, any fixed pivot sequence p₀,…,pₜ₋₁ and a common-workspace comparison family Fᵢⱼ of c reads, there is an input-independent choice of initial basis state and a circuit Aₓ of tc reads whose i-slice is m^(-1/2) times the tensor product of the complete states Fᵢ,p_b(x)|o⟩. Thus every fresh comparison is run on the full branch. The finite-workspace uniformization lemma derives the common workspace from pairwise Samples witnesses without adding reads.

**Source.** `paper/extracted.md, Section 3.2, source line 416`. Proposed source: `lean/QuarticQuery/Paper/QuantumTensor.lean`.

**Lean statement (unelaborated).**

```lean
theorem equation_15 {ι Col Z : Type} [Fintype Col] [Nonempty Col] [Fintype Z]
    {c : ℕ} (o : Z)
    (F : Col → Col → BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z)
    (hF : ∀ i j, IsCirc c (F i j)) (p : ℕ → Col) (t : ℕ) :
    ∃ (i₀ : Col)
      (A : BitInput ι → Reg (Σ _ : Col, TensorBasis Z t) ≃ₗᵢ[ℂ]
        Reg (Σ _ : Col, TensorBasis Z t)),
      IsCirc (t * c) A ∧
      ∀ x i, slice i (A x (rket (⟨i₀, tensorOrigin o t⟩ :
          Σ _ : Col, TensorBasis Z t))) =
        (((Real.sqrt ((Fintype.card Col : ℝ)⁻¹) : ℝ) : ℂ) •
          tensorVector (fun b => F i (p b) x (rket o)) t)
```

**Proof plan.** Use quantumWorkspace_uniformize for the finite pair family when needed. Construct TensorBasis recursively as a dependent sum. Prove tensorPreparation_state by slice_sigmaOp, slice_leftOp_rket and map_smul. Count reads with IsCirc.left, IsCirc.sigma and IsCirc.comp. Prepare the uniform candidate state using exists_unit_gate, then apply the controlled tensor preparation. The common workspace and every gate family are chosen before the oracle input. quantumTensorStage_of_samples composes this construction with the actual Samples comparison interface.

**Declarations used.** `QuarticQuery.Upper.exists_unit_gate`; `QuarticQuery.Upper.leftOp`; `QuarticQuery.Upper.sigmaOp`; `QuarticQuery.Upper.IsCirc.left`; `QuarticQuery.Upper.IsCirc.sigma`; `QuarticQuery.Upper.IsCirc.comp`; `QuarticQuery.Upper.slice_sigmaOp`; `QuarticQuery.Upper.slice_leftOp_rket`; `QuarticQuery.Upper.lawOf_sigma`; `QuarticQuery.Upper.regCongr_rket`.

**Related proposed declarations.** `QuarticQuery.Paper.equation_15`; `QuarticQuery.Paper.quantumWorkspace_uniformize`; `QuarticQuery.Paper.tensorPreparation_state`; `QuarticQuery.Paper.tensorPreparation_isCirc`; `QuarticQuery.Paper.quantumTensorStage_of_samples`.

**Correspondence and scope.** The coordinate equation is the full tensor state, with a fixed reversed nesting of fresh registers. This differs by a query-free basis permutation from increasing pivot order. sqrt(m^-1)=1/sqrt(m) because m>0. Upper.stage_samples short-circuits, so it is not identified with this whole state. The new list theorem continues to use that existing stage through its exact successful-label law; this is explicitly an alternative implementation route. The new common-workspace bridge removes the need to assume uniform workspace as an unexplained extra property of comparisons.

**Correction.** Replace the proposed full-state tie to Upper.stage_samples with the new full-state construction. This corrects evidence correspondence, not equation (15).
<!-- endpassage:row-eq-15 -->

### `claim-success-prob`

<!-- passage:row-claim-success-prob -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** For m>0, unit-valued comparison probabilities 0≤a_ij≤1, and W(L)>0, stageLaw is nonnegative with total mass one and positive successful mass. Its joint successful-index mass is Pr[index i and success]=w_i/m, total success probability is W/m, and the conditional index law on success is exactly w_i/W. The weight is the empty-product-compatible product ∏_{p∈L}a_{ip}.

**Source.** `paper/extracted.md, Section 3.2, source line 420`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumStage_success {Col : Type} [Fintype Col] [Nonempty Col]
    (a : Col → Col → ℝ) (ha : UnitValued a)
    (L : List Col) (hW : 0 < total (weight a L)) :
    (∀ o, 0 ≤ stageLaw a L o) ∧
    (∑ o, stageLaw a L o) = 1 ∧
    (0 < ∑ i, stageLaw a L (some i)) ∧
    (∀ i, stageLaw a L (some i) = weight a L i / Fintype.card Col) ∧
    (∑ i, stageLaw a L (some i)) = total (weight a L) / Fintype.card Col ∧
    (∀ i, stageLaw a L (some i) / (∑ j, stageLaw a L (some j)) =
      weight a L i / total (weight a L))
```

**Proof plan.** Induct on the history to prove every stage-law mass nonnegative, using 0≤a_ij≤1 for the failure and success factors. A separate finite-sum induction proves total mass one. Use sum_stageLaw_some and W>0 to prove positive successful mass. Then apply stageLaw_some and cancel the common nonzero cardinality with div_div_div_cancel_right₀. Prove weight equals List.prod by induction. The literal tensor-state version is provided separately by QuantumTensor; the successful-label identities here use the implemented stage law.

**Declarations used.** `QuarticQuery.Tournament.UnitValued`; `QuarticQuery.Upper.stageLaw_some`; `QuarticQuery.Upper.sum_stageLaw_some`; `div_div_div_cancel_right₀`; `QuarticQuery.Paper.quantumWeight_product`; `QuarticQuery.Paper.quantumStageLaw_nonneg`; `QuarticQuery.Paper.quantumStageLaw_total`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumStage_success`; `QuarticQuery.Paper.quantumWeight_product`; `QuarticQuery.Paper.quantumStageLaw_nonneg`; `QuarticQuery.Paper.quantumStageLaw_total`; `QuarticQuery.Paper.tensor_success_mass`; `QuarticQuery.Paper.equation_15_index_law`; `QuarticQuery.Paper.equation_15_success_probability`; `QuarticQuery.Paper.equation_15_conditional_index`.

**Correspondence and scope.** UnitValued is explicit because positive total weight alone does not make the summands nonnegative for an arbitrary real table. The theorem now states normalization, nonnegativity and positive successful mass before giving conditional probabilities. The positive W hypothesis is kept for meaningful conditioning. Lean totalized division also makes the ratio identity true at W=0, but that algebraic identity alone is not a conditional probability. This strengthens the proposed wrapper interface; it does not correct or alter the paper statement. The generic tensor identities are identities of masses for arbitrary vectors; their probability interpretation uses the normalized isometry witness supplied by equation_15. Conditioning requires W>0. The primary stage statement explicitly assumes UnitValued and proves normalization.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-success-prob -->

### `eq-13`

<!-- passage:row-eq-13 -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** Suppose aᵢᵢ=0 and aᵢⱼ+aⱼᵢ=1 for i≠j, and let W=∑ᵢwᵢ>0. Then ∑ₚ(wₚ/W)∑ᵢwᵢaᵢₚ=(1/W)∑ₚ∑ᵢwₚwᵢaᵢₚ=(W²−∑ᵢwᵢ²)/(2W)≤W/2. For the tournament, wᵢ≥0 and aᵢⱼ∈[0,1], so the first sum is the expected next total weight. The formal algebraic identity itself holds for arbitrary real weights.

**Source.** `paper/extracted.md, Section 3.2, source line 390`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumDrift {Col : Type} [Fintype Col] [DecidableEq Col]
    (w : Col → ℝ) {a : Col → Col → ℝ} (ha : IsComparison a)
    {W : ℝ} (hW : W = ∑ i, w i) (hpos : 0 < W) :
    (∑ p, (w p / W) * ∑ i, w i * a i p) =
        (1 / W) * ∑ p, ∑ i, w p * w i * a i p ∧
    (1 / W) * (∑ p, ∑ i, w p * w i * a i p) =
        (W ^ 2 - ∑ i, w i ^ 2) / (2 * W) ∧
    (W ^ 2 - ∑ i, w i ^ 2) / (2 * W) ≤ W / 2
```

**Proof plan.** Distribute finite sums to identify the pivot-law expectation with the double sum. Invoke expected_weight_eq for the paired-complementary identity and expected_weight_le_half for the inequality. The underlying pairing lemma is two_mul_weighted_sum.

**Declarations used.** `QuarticQuery.Tournament.two_mul_weighted_sum`; `QuarticQuery.Tournament.expected_weight_eq`; `QuarticQuery.Tournament.expected_weight_le_half`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumDrift`.

**Correspondence and scope.** The source already proves the exact drift algebra. This is a missing correspondence and a conjunction wrapper, not a new drift argument. Nonnegative weights are needed for the probabilistic interpretation; the algebraic equalities and square-based upper bound themselves hold for arbitrary real weights with positive total.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-eq-13 -->

### `claim-weight-lb`

<!-- passage:row-claim-weight-lb -->
**Classification:** A short consequence of existing declarations.

**Mathematical statement.** If s has not been selected in history L with t=|L|≤T, a is unit-valued, s is ε-dominant, 0≤ε≤1, and Tε<1/2, then w_s≥(1−ε)^t≥1−Tε>1/2 and W>0.

**Source.** `paper/extracted.md, Section 3.2, source line 398`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumWeight_lower {Col : Type} [Fintype Col]
    {a : Col → Col → ℝ} {ε : ℝ} {s : Col} (ha : UnitValued a)
    (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) (hd : Dominant a ε s)
    {T : ℕ} (hT : (T : ℝ) * ε < 1 / 2) (L : List Col)
    (hL : L.length ≤ T) (hs : s ∉ L) :
    (1 - ε) ^ L.length ≤ weight a L s ∧
    1 - (T : ℝ) * ε ≤ (1 - ε) ^ L.length ∧
    1 / 2 < weight a L s ∧ 0 < total (weight a L)
```

**Proof plan.** Use pow_le_weight at the actual history length. Bernoulli inequality gives (1−ε)^t≥1−tε, and tε≤Tε. Existing dominant_weight_lb and half_lt_total provide the strict lower bounds.

**Declarations used.** `QuarticQuery.Tournament.pow_le_weight`; `QuarticQuery.Tournament.dominant_weight_lb`; `QuarticQuery.Tournament.half_lt_total`; `one_add_mul_le_pow`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumWeight_lower`.

**Correspondence and scope.** The source dominant_weight_lb displays exponent T; the row displays t. This wrapper preserves t explicitly and gives the positivity consequence. At the paper parameters Tε=1/1000, all strict half-threshold requirements hold.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-claim-weight-lb -->

### `def-T-eps`

<!-- passage:row-def-T-eps -->
**Classification:** Definition or prose; only an agreement lemma is needed.

**Mathematical statement.** For m≥2, T=Nat.clog 2 (1000m) is the least natural exponent with 1000m≤2^T, equivalently ceil(log₂(1000m)); ε=1/(1000T) is positive. The agreement lemma also records the source definitions for arbitrary m using Lean’s totalized arithmetic.

**Source.** `paper/extracted.md, Section 3.2, source line 365`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumTournament_parameters (m : ℕ) :
    Tval m = Nat.clog 2 (1000 * m) ∧
      epsval m = 1 / (1000 * (Tval m : ℝ))
```

**Proof plan.** Use definitional equality for the parameters. Existing Tval_pos, epsval_nonneg, epsval_le and Tval_mul_epsval give positivity/ranges and Tε=1/1000. No new parameter object is needed.

**Declarations used.** `QuarticQuery.Tournament.Tval`; `QuarticQuery.Tournament.epsval`; `QuarticQuery.Tournament.Tval_pos`; `QuarticQuery.Tournament.Tval_mul_epsval`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumTournament_parameters`.

**Correspondence and scope.** The rfl wrapper proves agreement with the chosen source notation; it is not a new mathematical result. The code uses the integer ceiling-log representation, whose least-power semantics is certified by Nat.le_pow_clog and Nat.clog_le_of_le_pow.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-def-T-eps -->

### `eq-11`

<!-- passage:row-eq-11 -->
**Classification:** Definition or prose; only an agreement lemma is needed.

**Mathematical statement.** s is ε-dominant precisely when a_sj≥1−ε for every j≠s.

**Source.** `paper/extracted.md, Section 3.2, source line 377`. Proposed source: `lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`.

**Lean statement (unelaborated).**

```lean
theorem quantumDominant_iff {Col : Type} (a : Col → Col → ℝ) (ε : ℝ) (s : Col) :
    Dominant a ε s ↔ ∀ j, j ≠ s → 1 - ε ≤ a s j
```

**Proof plan.** Unfold Tournament.Dominant; the equivalence is Iff.rfl.

**Declarations used.** `QuarticQuery.Tournament.Dominant`.

**Related proposed declarations.** `QuarticQuery.Paper.quantumDominant_iff`.

**Correspondence and scope.** This is a missing definition tie. It does not assert that every comparison table has a dominant candidate, and no tournament guarantee assumes one exists on a zero-input.

**Correction.** No change to the preprint statement.
<!-- endpassage:row-eq-11 -->

## Auxiliary statements

The following records give the additional interfaces and explicit constants. Their `proposed_lean` signatures and import contexts are in `NEW_STATEMENTS.json`; their proof bodies are in the named source files. The proposed signatures use the supplied vocabulary, with the two list-interface abbreviations expanded where necessary. Every record is unelaborated.

### `r2-q-amplification-budget`

<!-- passage:aux-r2-q-amplification-budget -->
For 0<gamma<=1/2 and 0<eta<1/2, N=trialCount(eta), M=iterationBound(gamma) satisfy N(2M+1)<=138 (sqrt gamma)^(-1) log(1/eta). This bounds the entire charged product, uniformly in the actual success probability.

**Purpose.** stageCost and searchCost charge the product N(2M+1). The previous theorem bounds Proc.callCap, which can be smaller, so its endpoint alone cannot bound those definitions.

**Proof relation.** Extracts the numerical inequalities already proved locally in Amplification.callCap_amplify_le; unelaborated. No stronger algorithmic statement is inferred from an upper bound on a smaller cap.
<!-- endpassage:aux-r2-q-amplification-budget -->

### `r2-q-coherent-amplification`

<!-- passage:aux-r2-q-coherent-amplification -->
For γ>0 and η>0, a coherent sampler of n reads on Option beta can be amplified to another coherent sampler with cap trialCount(eta)*(2 iterationBound(gamma)+1)*n abstract reads. Its failure probability f_x is in [0,1], is at most eta when initial success mass is at least gamma, and is one at zero initial success mass. When the initial successful mass is positive, the joint mass of the successful output label some b is exactly (1-f_x)*L_x(some b)/sum_c L_x(some c), with all random-choice and trial workspaces retained. At zero initial successful mass, every successful-label mass is zero.

**Purpose.** Provides a circuit with an actual classical label in its final basis, allowing the list-valued tournament to be obtained before compilation to an AdaptiveProgram continuation. Retaining the trial records also matches the fresh-workspace implementation description.

**Proof relation.** New proof transport: the entire induction in Upper.Samples.attempts is run with Samples.bind and Samples.pure, followed by a final optional Samples.runs compilation. It certifies a coherent successful-label law, not a theorem that the whole final register equals the original good state. All source unelaborated.
<!-- endpassage:aux-r2-q-coherent-amplification -->

### `r2-q-conditional-label-law`

<!-- passage:aux-r2-q-conditional-label-law -->
If q_b>=0, sum_b q_b>0, and 0<=f<1, ampLaw(f,q) is a nonnegative probability distribution on Option beta, its successful event has positive mass, and its law conditional on success is q_b/sum_c q_c.

**Purpose.** Makes the probability interpretation and nonzero-event condition explicit. A cancellation identity for arbitrary q and f!=1 would not by itself establish a conditional distribution.

**Proof relation.** Finite normalization calculation using ampLaw. It divides by the actual sum of successful masses. New wrapper unelaborated.
<!-- endpassage:aux-r2-q-conditional-label-law -->

### `new-upper-sampler-law`

<!-- passage:aux-new-upper-sampler-law -->
For γ>0 and η>0, a coherent sampler of n reads has the Samples.amplify physical bit-query cap trialCount(η)*2*((2 iterationBound(γ)+1)*n). Its failure is at most η when initial success mass is at least γ, and is certain when the initial success mass is zero. The unconditional successful label masses have the exact ampLaw formula; division into a conditional law requires positive actual successful mass.

**Purpose.** Keeps the exact interface on the existing headline proof path separate from the abstract full-state theorem and from the new coherent transport.

**Proof relation.** Preserves the prior proposal ID from previous_round/1_long_reasoning_record/NEW_STATEMENTS.json. It is an exact re-export of Upper.Samples.amplify, whose input implementation uses full measurement and a known reset. The new alias is unelaborated; no status inheritance.
<!-- endpassage:aux-new-upper-sampler-law -->

### `r2-quantum-list-law-normalized`

<!-- passage:aux-r2-quantum-list-law-normalized -->
Any Samples witness whose measured label is a list of length at most T gives nonnegative masses summing to one for every oracle input. The constructed tournament supplies such a witness.

**Purpose.** Makes the probability interpretation of the literal list output explicit. The internal recursive list-law proof additionally handles zero total weight by certain termination.

**Proof relation.** Re-export of Samples.nonneg and Samples.sum_eq_one on the explicit bounded-list subtype. quantumListLaw_total remains an internal normalization proof for the chosen recursive law. No probabilistic assertion is based on totalized division alone.
<!-- endpassage:aux-r2-quantum-list-law-normalized -->

### `r2-quantum-perfect-indicator-coupling`

<!-- passage:aux-r2-quantum-perfect-indicator-coupling -->
Let a be unit-valued, v and f be in [0,1], v(s)=1, and f(L)=1 whenever W(L)=0. Suppose s is ε-dominant, 0≤ε≤1, T₀ε<1/2, and f(L)≤ε for every history of length at most T₀ omitting s. For |L|+n≤T₀, tval(a,v,f,n,L)≥1−missFrom(a,s,n,L)−nε. With v=1_{s}, tval is exactly the probability that the returned list contains s.

**Purpose.** Removes the verifier epsilon when proving list membership.

**Proof relation.** An explicit perfect-indicator version of the existing continuation induction. This perfect verifier is a proof device and does not choose the algorithm. UNELABORATED in this environment.
<!-- endpassage:aux-r2-quantum-perfect-indicator-coupling -->

### `r2-quantum-tournament-budget-6072`

<!-- passage:aux-r2-quantum-tournament-budget-6072 -->
For m≥2, T=ceil(log₂(1000m)), ε=1/(1000T), N=trialCount(ε), M=iterationBound(1/(2m)), the exact compiled cap 2N(2M+1)cT² is at most 6072 c sqrt(m) T² ln(T). The comparison cap c counts logical reads; the factor two converting reads into physical bit queries is already included.

**Purpose.** Turns the paper big-O into a uniform finite numerical inequality.

**Proof relation.** The arithmetic copies the actual ceiling bounds and includes the physical bit-query compilation factor; no optimization or novelty is claimed. UNELABORATED in this environment.
<!-- endpassage:aux-r2-quantum-tournament-budget-6072 -->

### `r2-quantum-coherent-list-witness`

<!-- passage:aux-r2-quantum-coherent-list-witness -->
For m≥2, T=ceil(log₂(1000m)), ε=1/(1000T), and a coherent comparison family of c logical reads with complementary probabilities, there is one normalized list law and one coherent circuit with that list as its measured label. Every label has length at most T. Its physical bit-query cap C satisfies C≤6072 c sqrt(m) T² ln(T), and, for every fixed oracle input x and every ε-dominant s, Pr[s is listed]≥1−2m/2^T−Tε.

**Purpose.** Exhibits an actual coherent finite list label before converting to the Boolean continuation interface.

**Proof relation.** Retain trial and history registers; compose Samples; compile to Runs at the end. Finite bounded-list alias is defined in the supplied Lean module; it is not an extra axiom. UNELABORATED in this environment.
<!-- endpassage:aux-r2-quantum-coherent-list-witness -->

### `r2-quantum-ordinary-oracle-read`

<!-- passage:aux-r2-quantum-ordinary-oracle-read -->
The ordinary oracle bitOracleL is a single IsCirc logical read on the same basis type.

**Purpose.** Identifies the paper comparison input convention with the generic theorem hypothesis.

**Proof relation.** Concrete ReadSpec flips only the answer bit, keeps address/workspace, and has no phase sign. UNELABORATED in this environment.
<!-- endpassage:aux-r2-quantum-ordinary-oracle-read -->

### `r2-quantum-decode-bit-budget`

<!-- passage:aux-r2-quantum-decode-bit-budget -->
For k≥1,t≥1,r=40t and 0<ε≤1, choosing n=ceil(16·2^(10k) ln(r/ε)) gives at most 2rk[1+16·2^(10k) ln(r/ε)] physical bit queries for the full address decoder.

**Purpose.** Pins the hidden constant and the physical-query factor of two in claim-decode-cost.

**Proof relation.** Source-proof extraction and elementary inequalities. All supplied proof bodies are unelaborated; no novelty claim. The numeric amplification helper is supplied in QuantumAmplification.lean.
<!-- endpassage:aux-r2-quantum-decode-bit-budget -->

### `r2-quantum-decode-polylog`

<!-- passage:aux-r2-quantum-decode-polylog -->
Let R_k=1+1920000·2^(10k). At ε=1/(1000 ceil(log₂(1000m))), m=4^t,t≥1, n=repetitions(k,ε/(40t))≤R_k(2t)^2 and 2 addrCost(k,t,n)≤40R_k k(2t)^3.

**Purpose.** Exports the actual finite polynomial estimate previously local to Upper.budget_le.

**Proof relation.** Source-proof extraction and elementary inequalities. All supplied proof bodies are unelaborated; no novelty claim. The numeric amplification helper is supplied in QuantumAmplification.lean.
<!-- endpassage:aux-r2-quantum-decode-polylog -->

### `r2-quantum-comparison-bit-budget`

<!-- passage:aux-r2-quantum-comparison-bit-budget -->
For natural k,t,n the exact cap identity holds. The real logarithmic bound assumes t≥1 and 0<ε≤1; the paper-parameter specialization assumes t≥1. The comparison physical-query cap is 2 cmpCost=4 addrCost+8t+4. With the least repetition count it is at most 160tk[1+16·2^(10k) ln(40t/ε)]+8t+4. At the paper parameters it is at most 2(40R_k k+4)(2t)^3, where R_k=1+1920000·2^(10k).

**Purpose.** Makes the comparison cost claim exact for the implemented decoder and two adaptive pointer tests.

**Proof relation.** Source-proof extraction and elementary inequalities. All supplied proof bodies are unelaborated; no novelty claim. The numeric amplification helper is supplied in QuantumAmplification.lean.
<!-- endpassage:aux-r2-quantum-comparison-bit-budget -->

### `r2-quantum-verification-search-budget`

<!-- passage:aux-r2-quantum-verification-search-budget -->
For K≥2 and 0<ε<1/2, the implemented fixed-address search has physical cap searchCost(t,K,ε)≤276√K ln(1/ε) max(3,2t+1). For t≥1 the final factor equals 2t+1.

**Purpose.** Bounds the exact padded product charged by searchCost; the abstract Proc callCap bound alone cannot upper-bound this larger charged quantity.

**Proof relation.** Source-proof extraction and elementary inequalities. All supplied proof bodies are unelaborated; no novelty claim. The numeric amplification helper is supplied in QuantumAmplification.lean.
<!-- endpassage:aux-r2-quantum-verification-search-budget -->

### `r2-quantum-verification-polylog`

<!-- passage:aux-r2-quantum-verification-polylog -->
For t≥1, m=4^t, ε=1/(1000 ceil(log₂(1000m))), n=repetitions(k,ε/(40t)), and C.size≤forrConstant(k)·m·(2t)^2, the full physical single-candidate verification cap 2 addrCost(k,t,n)+searchCost(t,card(Tests(t,C)),ε) is at most budgetConst(k)·2^t·(2t)^6. For k=l+1 the selected forrCircuit(l,t) satisfies the size hypothesis. This is a finite sqrt(m)·(log₂m)^6 upper bound.

**Purpose.** Closes the finite-K to finite-m specialization of claim-verify with the circuit-size premise exposed and includes the fresh-decoding cap.

**Proof relation.** Elementary domination of the single-candidate cap by the existing complete budget, followed by Upper.budget_le. The selected-circuit corollary invokes forrCircuit_size_le. No smaller constant or exponent is claimed; both wrappers are unelaborated.
<!-- endpassage:aux-r2-quantum-verification-polylog -->

### `r2-q-common-workspace`

<!-- passage:aux-r2-q-common-workspace -->
A finite nonempty family of coherent samplers with one read cap can use a common finite workspace, origin and output map, with the same read cap and the same individual output laws.

**Purpose.** Connects pairwise existential Samples comparison witnesses to the common-workspace hypothesis of the literal tensor-state equation.

**Proof relation.** Finite direct sum of the existing workspaces, preceded by a query-free basis swap. This is the block construction already used in Samples.bind, extracted as a reusable statement. No added oracle assumptions, no claim of mathematical novelty.
<!-- endpassage:aux-r2-q-common-workspace -->

### `r2-q-full-tensor-sampler`

<!-- passage:aux-r2-q-full-tensor-sampler -->
For a finite nonempty candidate set of size m, any coherent comparison family of c reads and fixed sequence of t pivots, a coherent sampler of tc reads has successful index mass (1/m)∏_{b<t}aᵢ,p_b. Its proof constructs the full fresh tensor state after putting the family in a common workspace.

**Purpose.** Supplies a direct full-tensor construction from the same comparison interface used by the tournament, respecting F-STAGE-LAW.

**Proof relation.** Uses quantumWorkspace_uniformize, equation_15 and its successful-index mass calculation. The signature uses the existing Samples/bern vocabulary. The list theorem keeps its existing short-circuit sampler and agrees on the law needed for the proof.
<!-- endpassage:aux-r2-q-full-tensor-sampler -->
