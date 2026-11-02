# Remaining Lean correspondence obligation for the quantum upper bound

This record accompanies replacement §5. It separates a remaining **physical returned-state correspondence** from the label-law and query-complexity results already supported by the current packet. It does not propose an additional assumption for Proposition 3.3, retract the current list theorem, or report a new Lean or Comparator run.

Source locators below are relative to the supplied packet. Exact extracted declarations, source hashes, available elaborated types and evidence flags are recorded in `checks/lean_evidence_audit.json`. The ordinary proof and the distinction between a returned subsystem and the enlarged workspace are in §5.1 and §5.5 of `section.md`.

## 1. What remains, and what is already resolved

| Question | Current status |
|---|---|
| Does fixed-budget amplification preserve the complete normalized good state in the abstract procedure semantics? | Yes. `QuarticQuery.Amplification.bounded_amplification` includes phase-invariant observables, a conditional-state clause, zero wrong-state mass, zero-success failure and a uniform call cap. |
| Is the required amplified classical label law physically realizable with an all-branch bit-query cap? | Yes. `QuarticQuery.Upper.Samples.amplify` supplies a measured `Runs` witness. |
| Is there a coherent realization retaining registers and giving that same amplified label law? | Yes. `QuarticQuery.Paper.quantum_amplify_samples` supplies `Samples`; its conclusion remains a law about designated classical labels. |
| Does either physical amplification type identify a fixed original output subsystem with the complete original normalized good state? | No such theorem is supplied. This is the remaining bridge specified in §3 below. |
| Is the literal tensor state in equation (15) available? | Yes, through `Paper.equation_15`. The short-circuit `Upper.stage_samples` is a separate construction with the required successful index masses. Equality of their complete states is not asserted. |
| Is Proposition 3.2 represented by an actual bounded-list output, rather than only a Boolean endpoint? | Yes. `Paper.quantumTournament` gives a finite bounded-list `Samples` law, a physical `Runs` implementation, the dominant-membership bound and the 6072 cap. Historical claims to the contrary are obsolete for these source bytes. |
| Is the explicit upper bound for the chosen total function present in the current proof closure? | Yes. `Upper.Fkm_forrCircuit_QLe` and `Upper.Q_Fkm_le` are reached from the supplied headline roots. |

The final upper-bound proof uses measured labels, so it does not need the missing output-subsystem theorem. The stronger physical interpretation of the successful-state sentence in Lemma 3.1 does need that theorem. The ordinary fresh-trial/routing proof supplies the mathematical construction; its full formal correspondence has not yet been supplied.

## 2. Existing amplification interfaces: their actual scope

### 2.1. The abstract state theorem

`repository/lean/QuarticQuery/Amplification/Bounded.lean`, lines 242–257, declares `QuarticQuery.Amplification.bounded_amplification`. For `0 < γ`, `γ ≤ 1/2`, `0 < η`, `η < 1/2`, it proves the call-cap estimates and, for every inner-product-space preparation `A : Preparation H`, includes the following actual clauses:

```lean
(∀ h : Option H → ℝ, PhaseInvariant h →
  (amplify γ η).expect A h A.zero =
    (amplify γ η).successProb A * h (some A.goodState) +
    (amplify γ η).failProb A * h none) ∧
(∀ k : H → ℝ, (∀ c : ℂ, ‖c‖ = 1 → ∀ v, k (c • v) = k v) →
  (amplify γ η).successProb A ≠ 0 →
  (amplify γ η).conditional A k = k A.goodState) ∧
(amplify γ η).wrongStateMass A = 0 ∧
(γ ≤ A.prob → (amplify γ η).failProb A ≤ η) ∧
(A.prob = 0 → (amplify γ η).failProb A = 1)
```

These are statements about the abstract `Proc` semantics. A finite physical register, a specified output subsystem and a compiler witness connecting that subsystem to `A.goodState` do not occur in this type. The current source-bound root receipt declares the theorem, but the exported closure of the two headline roots does not reach it. No separate printed elaborated type for this exact declaration was supplied in the reviewed type/axiom log; the quotation is from the source signature with its ambient parameters accounted for.

### 2.2. Why `Samples` is a label interface

The definition at `repository/lean/QuarticQuery/Upper/Sampler.lean`, lines 115–117, is:

```lean
def Samples {ι β : Type} (n : ℕ) (L : BitInput ι → β → ℝ) : Prop :=
  ∃ (Z : Type) (_ : Fintype Z) (o : Z) (out : Z → β)
    (F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z),
    IsCirc n F ∧ ∀ x b, L x b = lawOf (F x (rket o)) out b
```

This gives a concrete coherent witness, but identifies only its classical output law. The existential register `Z` is not identified with the original preparation's register, and the conclusion contains no reduced-density or factorization equation for an original subsystem. A coherent implementation and a correct label law therefore do not automatically supply the successful-state correspondence.

With ambient `{ι β : Type} [Fintype ι] [Inhabited ι] [Fintype β]`, `QuarticQuery.Paper.quantum_amplify_samples` has this source signature at `repository/lean/QuarticQuery/Paper/QuantumAmplification.lean`, lines 355–361:

```lean
theorem quantum_amplify_samples {n : ℕ}
    {L : BitInput ι → Option β → ℝ} (h : Samples n L) {γ η : ℝ}
    (hγ : 0 < γ) (hη : 0 < η) : ∃ f : BitInput ι → ℝ,
      (∀ x, 0 ≤ f x ∧ f x ≤ 1) ∧
      (∀ x, γ ≤ ∑ b, L x (some b) → f x ≤ η) ∧
      (∀ x, ∑ b, L x (some b) = 0 → f x = 1) ∧
      Samples (trialCount η * ((2 * iterationBound γ + 1) * n))
        fun x => ampLaw (f x) fun b => L x (some b)
```

Its elaborated type is printed in `native_logs/final-evidence/reviewed-type-axiom-audit.log`, lines 1134–1144; the following axiom record lists `propext`, `Classical.choice`, and `Quot.sound`. It is in the current root's declared set, but not in the two headline roots' reached set. The signature's positivity assumptions are broader than the parameter range used for the 138 estimate; the quantitative estimate below additionally uses `γ ≤ 1/2` and `η < 1/2`.

`QuarticQuery.Upper.Samples.amplify`, in `repository/lean/QuarticQuery/Upper/Amplify.lean`, lines 346–352, has the same failure-law clauses and concludes instead:

```lean
Runs (trialCount η * (2 * ((2 * iterationBound γ + 1) * n)))
  fun x => ampLaw (f x) fun b => L x (some b)
```

This declaration is reached by the current headline proof closure. The factor two is the physical compiler's charge. `Runs` reports measured classical output mass, so it also does not assert that the original quantum register is returned unmeasured.

### 2.3. A concrete reason the distinction matters

Let $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$. The product state $|+\rangle|0\rangle$ and the Bell state $(|00\rangle+|11\rangle)/\sqrt2$ give the same first-register computational-basis law, $(1/2,1/2)$. Their first-register density operators are, respectively,

$$
\rho_+=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},
\qquad
\rho_{\rm Bell,H}=\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix}.
$$

The probability of the $+$ outcome is $1$ for the first and $1/2$ for the second. Thus equality of these label laws does not establish equality of the returned quantum state. `Samples.bind` can retain a copied output label in its auxiliary direct-sum tag; retaining such information is compatible with its exact classical mixture law. Its type at `Upper/Sampler.lean`, lines 241–243, makes no stronger state claim.

`checks/state_example.py` computes both complete density matrices, their partial traces, and these measurement probabilities using only exact `fractions.Fraction` arithmetic. It also verifies that applying a CNOT to the Bell state returns the product state. The example therefore shows a missing inference and the need for specified routing/uncomputation; it is not an impossibility result about recovering the state. The generated JSON is an ordinary finite calculation, not a Lean theorem or a verification of the implementation of `Samples.bind`.

## 3. Exact remaining physical-state bridge

This is the target associated with claim `r3-q-physical-state-bridge`. The following is a specification, **not a newly compiled theorem**.

### 3.1. Fixed interface and quantifier order

Fix a finite nonempty original basis `Z`, with $H=\mathbb C^Z$ (the source's `Reg Z`), an initial basis label $h_0\in Z$, a fixed orthogonal success projector $\Pi$ on $H$, a finite input-coordinate type $\iota$, and a logical-read budget $q$. The entire workspace of the original preparation is part of $H$. The success projector is input-independent; it can be a coordinate projector or another fixed projector implemented using free input-independent gates.

For fixed $0<\gamma\leq1/2$ and $0<\eta<1/2$, choose **one finite amplification template before the preparation $A$ and the input $x$ are supplied**. Define

$$
M=\left\lceil10/\sqrt\gamma\right\rceil,
\qquad N=\left\lceil\ln(1/\eta)/\ln(40/31)\right\rceil,
\qquad K_{\rm log}=qN(2M+1).
$$

The template's trial schedule, fresh-register layout, control flow, stopping bound and routing are fixed by these parameters and the register/query interface. It accepts a concrete family

```lean
A : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z
hA : IsCirc q A
```

and instantiates its preparation/inverse slots with `A` and its inverse. No schedule or cap depends on the unknown success probability, and input dependence enters only through these allowed calls and, after compilation, ordinary bit-oracle reads. The `IsCirc q A` witness is needed to translate those calls into the stated logical-read and physical bit-query costs. It is not needed to obtain controlled access to an opaque preparation: the construction below uses only unconditional calls to `A` and its inverse.

For a control bit $c$, write $C_c(U)=|0\rangle\langle0|_c\otimes I+|1\rangle\langle1|_c\otimes U$, and let $Z_c$ apply phase $-1$ only when $c=1$. Set $S_0=I-2|h_0\rangle\langle h_0|$ and $S_\chi=I-2\Pi$. Both reflections are fixed, input-independent unitaries. For $G_x=-A_xS_0A_x^{-1}S_\chi$, the exact operator identity is

$$
C_c(G_x)
=(Z_c\otimes I)(I_c\otimes A_x)\,C_c(S_0)\,
 (I_c\otimes A_x^{-1})\,C_c(S_\chi).
$$

On the false-control block the right-hand side is $A_xA_x^{-1}=I$; on the true-control block it is $-A_xS_0A_x^{-1}S_\chi=G_x$. This calculation holds on every vector, including a superposition of control values, and charges exactly two unconditional preparation/inverse calls even on the false block. Thus controlled Grover iterations require control only of the fixed reflections and the control phase, not controlled `A` or controlled `A⁻¹`.

Run all $N$ fresh trials coherently, then route the first successful one. In each trial, make one unconditional preparation call, store its iteration-count seed, and use $M-1$ of the displayed controlled iterates, with the $j$th control asserting that the chosen count is at least $j$. The call count is $1+2(M-1)=2M-1$ in every trial, hence at most the padded $2M+1$. Record only the success predicate in each trial's herald register. Finally compute the first-success record and route its entire original register. Both actions are fixed reversible operations. Later trials do not alter whether an earlier success occurred, so the returned-register law and the overall failure probability agree with the measured procedure that stops at its first success. The coherent circuit pays for all $N$ trials but still obeys $N(2M+1)$ preparation/inverse calls. This gives the required black-box uniformity using `A` and `A⁻¹` alone.

### 3.2. State, herald and designated subsystem

The template chooses a finite auxiliary basis `W`, an initial basis label $j_0\in W$, and a fixed success predicate on `W`. Write $J=\mathbb C^W$, let $\Pi_J$ be the predicate's coordinate projector, and use the basis identification $\operatorname{Reg}(Z\times W)\cong H\otimes J$. Thus $|h_0,j_0\rangle=|h_0\rangle\otimes|j_0\rangle$ is a fixed normalized starting vector. Extra trial registers, iteration-count seeds, outcome records and routing controls belong to $J$.

Instantiation yields a coherent unitary family $B_x$ on $H\otimes J$, including a specified, input-independent routing controlled by the first-success record. That routing places the **entire** successful original register, with all of its original preparation workspace, in the designated $H$ slot. Keeping all records is permitted, but a copied basis label may not remain entangled with $H$ if the theorem claims that $H$ is pure.

For every input $x$, define

$$
\begin{aligned}
\psi_x&=A_x|h_0\rangle,&p_x&=\|\Pi\psi_x\|^2,\\
\Psi_x&=B_x|h_0,j_0\rangle,&\Pi_{\rm out}&=I_H\otimes\Pi_J,\\
s_x&=\|\Pi_{\rm out}\Psi_x\|^2.
\end{aligned}
$$

The output-success projector must be $I_H\otimes\Pi_J$: heralding succeeds by reading auxiliary data, without measuring the returned original register. For all $x$, the required conclusions are

$$
0\leq p_x\leq1,\qquad 0\leq s_x\leq1,\qquad
p_x\geq\gamma\Longrightarrow s_x\geq1-\eta,
\qquad p_x=0\Longrightarrow\Pi_{\rm out}\Psi_x=0.
$$

Only when $p_x>0$, define $g_x=\Pi\psi_x/\sqrt{p_x}$. Require the explicit positive-success bound and the factorization

$$
p_x>0\Longrightarrow
\left[
s_x\geq p_x/2>0\ \text{ and }\ 
\exists\xi_x\in J:\quad
\Pi_J\xi_x=\xi_x,\quad
\Pi_{\rm out}\Psi_x=g_x\otimes\xi_x,\quad
\|\xi_x\|^2=s_x
\right].
$$

The displayed positivity bound follows because the first trial selects zero iterations with probability at least $1/2$, and $N\geq1$. Its success event is contained in the event that at least one of the $N$ trials succeeds, so $s_x\geq p_x/2$. This is the positive-success clause of the proposed theorem, not an assumption on its input. In particular, the conditional state is defined for every positive original success probability, even when it is smaller than $\gamma$. At $p_x=0$ there is no normalized good vector and no conditional-state claim on a null event. At $p_x=1$ the same factorization applies, with certain success.

Since $\|g_x\|=1$ and $s_x>0$, the factorization is equivalent to saying that the successful conditional reduced density operator on the designated original subsystem is $|g_x\rangle\langle g_x|$. For the converse, a pure successful global vector with this reduced density has zero component in $g_x^\perp\otimes J$, and therefore is $g_x\otimes\xi_x$; its norm and the auxiliary herald condition give the other two displayed equations. This equivalence concerns the designated subsystem and does not identify the enlarged workspace with $g_x$ alone. Each successful measured history gives $g_x$ up to a phase; when histories are kept coherently, the phase and all additional records are absorbed into $\xi_x$. An equivalent adaptive specification may state this same original-register property separately on every positive-mass successful history, together with the same success bounds and uniform cap.

### 3.3. Logical cap and the same physical implementation

The instantiated circuit must have a witness

```lean
IsCirc (q * trialCount η * (2 * iterationBound γ + 1)) B
```

up to harmless associativity of natural-number multiplication and the chosen product-basis encoding. This is an input-uniform syntactic cap. It is not an expected number of calls and does not require $p_x\geq\gamma$.

The existing compiler is already strong enough to express the required transport once this **same** retained-state circuit has been constructed. `QuarticQuery.Upper.compile_circ`, `repository/lean/QuarticQuery/Upper/Compile.lean`, lines 217–221, says, with the ambient finite physical embedding `e : Z ↪ Fin (w + 1)`:

```lean
theorem compile_circ {n : ℕ}
    {F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z} (hF : IsCirc n F) :
    ∃ P : AdaptiveProgram ι w → AdaptiveProgram ι w, ∀ next,
      (P next).queryCap ≤ 2 * n + next.queryCap ∧
      ∀ x ψ b, (P next).outputMass x (clEmb e ψ) b =
        next.outputMass x (clEmb e (F x ψ)) b
```

Apply it with the product basis `Z × W`, a sufficiently large fixed physical embedding, and $n=K_{\rm log}$. The required bit-query cap is therefore $2K_{\rm log}$ plus the continuation's cap. The continuation equation is required for arbitrary embedded vectors and continuations. This arbitrary-vector clause is compiler correctness for $B$, not a claim that amplification produces $g_x$ from an arbitrary initial vector. The amplification claim uses exactly $|h_0,j_0\rangle$.

By contrast, `Samples.runs` at `Upper/Compile.lean`, lines 396–397, states `Samples n L → Runs (2 * n) L`. Its proof measures a complete basis label to obtain a classical law. Applying that theorem alone loses the returned-state interface, even though it is sufficient for the final upper bound.

### 3.4. Proposed interface, explicitly uncompiled

The following contract is schematic notation, **not Lean source**. `RetainedAmplifierTemplate`, `instantiate`, and `SuccessfulOriginalSubsystem` are proposed interface concepts, not declarations found in the packet. Its purpose is to make the quantifier order and required output identity reviewable before any future formalization.

```text
for every fixed finite interface (ι, Z, h0, Π, q)
and every γ, η with 0 < γ ≤ 1/2 and 0 < η < 1/2:

  there exists P : RetainedAmplifierTemplate(interface, γ, η)
    with fixed finite W, initial j0, auxiliary success predicate,
    preparation/inverse slots, and original-register routing,

  such that for every circuit family A and witness hA : IsCirc q A:
    B := instantiate(P, A, hA)
    IsCirc K_log B
    for every x:
      SuccessfulOriginalSubsystem(B, A, h0, j0, Π, Π_J, x)
      [the zero case, probability bounds, p_x > 0 => s_x >= p_x/2 > 0,
       and p_x > 0 factorization are exactly those of §3.2]

    compile this B, on every sufficiently large fixed embedding,
    with the all-vector/all-continuation equation of compile_circ
    and additional physical queryCap at most 2 * K_log.
```

The order is `∃ P, ∀ A, ∀ x`, not a separate input-dependent algorithm for each $x$ or an unknown-probability-dependent stopping rule. A proposition-valued `IsCirc` witness is the existing formal representation of the preparation; a future formalization may choose another explicit circuit syntax for the template while proving its instantiations satisfy `IsCirc`.

## 4. Quantitative and conditional-law obligations already handled

`Paper.amplification_budget_le`, `Paper/QuantumAmplification.lean`, lines 156–159, bounds the actual padded product:

```lean
(trialCount η : ℝ) * (2 * (iterationBound γ : ℝ) + 1) ≤
  138 * (Real.sqrt γ)⁻¹ * Real.log (1 / η)
```

It assumes `0 < γ`, `γ ≤ 1/2`, `0 < η`, `η < 1/2`. Its elaborated type is printed in the reviewed audit, lines 741–746. Bounding only the potentially smaller abstract `Proc.callCap` would not establish this padded implementation cost. Multiplying by the preparation's $q$ logical reads and by the compiler's factor two gives the physical charge $2qN(2M+1)$, or at most $276q\gamma^{-1/2}\ln(1/\eta)$.

For a tournament history, the successful masses are $q_i=w_i/m$ and $q=\sum_iq_i=W/m$. When $W>0$, conditioning gives exactly $w_i/W$; when $W=0$, the algorithm fails with certainty. A totalized Lean quotient at zero is not a conditional probability on that event. Before a dominant vertex has appeared, its weight is at least $1-T\varepsilon=999/1000>1/2$, so the required success lower bound $q\geq1/(2m)$ holds. After it appears, or when no dominant vertex exists, the success promise is unnecessary: the same fixed cap remains valid.

The padded physical tournament cap is $2T^2c_{\rm rd}N(2M_0+1)$. The 138 bound gives $276c_{\rm rd}\sqrt{2m}T^2\ln(1000T)$; $\sqrt{2m}\leq2\sqrt m$ and $\ln(1000T)\leq11\ln T$ for the specified $T$ yield $6072c_{\rm rd}\sqrt mT^2\ln T$. The two-bit-query compilation charge is included once. `Paper.quantumTournament_cost`, `Paper/QuantumTournamentFacts.lean`, lines 238–241, is the current finite-budget inequality; its printed type is at audit lines 734–739.

## 5. The resolved list theorem and final upper-bound route

`QuantumCandidateList Col T` is the actual bounded-list subtype `{l : List Col // l.length ≤ T}` (`Paper/QuantumTournament.lean`, line 30). `QuarticQuery.Paper.quantumTournament`, `Paper/QuantumTournamentFacts.lean`, lines 287–303, assumes finite column and input-coordinate types, $m\geq2$, complementary comparison probabilities on every input, and `Samples cc` realizations of the comparisons. Its actual conclusion is:

```lean
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

Its elaborated type is printed at audit lines 685–704, followed by the standard three-axiom list at line 705. This is direct list-membership support, not a Boolean-verifier substitute. Its ideal membership indicator is an analytic device; it is not an additional physical verifier with another error term in the list theorem.

`Paper.equation_15` at `Paper/QuantumTensor.lean`, lines 120–131, supplies an `IsCirc (t * c)` family and the literal tensor slice equation. Its elaborated type is at audit lines 1146–1159. `Upper.stage_samples` at `Upper/Tournament.lean`, lines 63–65, instead supplies `Samples (L.length * cc)` for the short-circuit `stageLaw`. They can be used for the same successful index law without equating their full failure workspace or full retained states.

For the final Boolean function, decoder promise correctness is needed only for the true winner. Nonwinner verification uses exact local tests at every decoded address, and the caps hold on all bit strings. The eventual extra $\varepsilon$ in the one-input error bound belongs to fresh verification of the winner, not to the list-membership theorem. `CircuitRealises`, the stated circuit-size bound and the repetition bound are ordinary construction premises discharged for the chosen circuit; they are not new unresolved assumptions on the family.

The current final algorithmic theorem is `QuarticQuery.Upper.Fkm_forrCircuit_QLe`, `Upper/Bound.lean`, lines 272–273:

```lean
theorem Fkm_forrCircuit_QLe (l t : ℕ) (ht : 1 ≤ t) :
  QLe (totalise (Fkm (l + 1) t (forrCircuit l t)))
    (budgetConst (l + 1) * 2 ^ t * (2 * t) ^ 6)
```

Its numerical companion `Upper.Q_Fkm_le` is at lines 278–280. Both are reached from the supplied headline roots. The formal parameter is $k=l+1$, and the paper application fixes $k\geq2$, $m=4^t$, $t\geq1$. The explicit logarithmic exponent six and ordinary-bit-query accounting are present in the current source-bound evidence. No missing physical successful-state theorem is silently assumed by this measured-label route.

## 6. Evidence boundary and what would close the remaining bridge

The supplied root build receipt is `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`, status `passed`, with recorded toolchain `leanprover/lean4:v4.36.0-rc2`. The receipt labels commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`; the packet manifest labels `1dd469dd0042b937b739da3bc211eeb60bdf7462`. All 124 reviewed local source/configuration hashes agree across the packet bytes, evidence snapshot, root receipt, dependency export and axiom verdict. The source-byte binding, rather than an assumption that these commit labels coincide, supports applying that evidence to the supplied files.

The dependency export has two specified roots: `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional`. It reaches the older measured/Boolean upper-bound route, including `Upper.Samples.amplify` and `Upper.Q_Fkm_le`, and reaches no declaration in the `Paper` namespace. Nonmembership in those two closures does not mean a wrapper failed to compile. Conversely, declaration membership or successful compilation does not by itself prove that a human-intended state interface is expressed by its type.

The current Tournament Comparator receipt covers the two drift wrappers, not the new list theorem. None of the exact new quantum `Paper` helper names quoted here has a current exact-name Comparator receipt. Type/axiom auditing, Comparator matching, build success, source-byte currentness and dependency reach are distinct evidence dimensions. Historical `UNELABORATED` source comments are not newer build evidence.

To close the specific remaining bridge, construct a uniform retained-state amplifier with the original subsystem and initialization of §3, prove its successful factorization and all-input logical cap, and instantiate the existing compiler on that same circuit. Any label copies that would leave the original register entangled must be absent or explicitly uncomputed before the designated return. A future source-bound build and exact-type audit should then record that complete theorem. This return makes no such new formalization or execution claim. The density-matrix example is an ordinary exact calculation; the other finite and structural checks are separately recorded under checks/.
