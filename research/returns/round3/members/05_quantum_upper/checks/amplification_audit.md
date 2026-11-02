# Amplification audit and proposed replacement passages

Scope: the quantum-upper packet extracted at `packet/`, 2 November 2026. This is an intermediate contribution to the root editor, not a final integrated section. The attached source is primary for the target argument. I independently rederived the amplification calculation and inspected the exact type boundary. I did not run Lean or Comparator. Current build evidence should be taken from the separate evidence audit, not from old `Status: unelaborated` source comments or the original round-two return.

## Principal findings

1. OpenAI Lemma 3.1 is mathematically sound under the unitary-preparation and designated success-subspace hypotheses. The finite random-length/fresh-trial construction preserves the entire successful state in the designated **original preparation register**. Random seeds, first-success indices, and failed trial registers may be retained as additional junk; the enlarged joint register is not asserted to equal the original good vector.
2. Its proof has a worst-case cap on every input and branch. The promise `p ≥ γ` is used only for the failure guarantee, never for the cost. The exact padded product used downstream is `N(2M+1)`, not the possibly smaller abstract `Proc.callCap`; `Paper.amplification_budget_le` supplies the relevant product inequality.
3. The existing abstract `Proc` theorem does express a full state law up to phase. Both `Upper.Samples.amplify` (measured `Runs`) and `Paper.quantum_amplify_samples` (coherent `Samples`) conclude an exact classical label law. The latter retains registers but does not identify their successful quantum state with the original good state. The current adjudication explicitly preserves this gap.
4. This gap is substantive at the interface level. `Samples.bind` explicitly copies the preceding outcome label into a fresh direct-sum tag. Even if the original successful register is `|+>`, the basic bind-to-same-label witness can make `( |00> + |11> )/√2`. The original register then has mixed reduced state, despite exactly the same computational-basis label distribution. A query-free uncopy can repair this simple example. What is missing is a proved general register-routing/uncomputation correspondence, not a mathematical impossibility.
5. The exact successful label law suffices for the tournament. No physical full-state claim needs to be smuggled through `Samples` to prove Proposition 3.3.

## Proposed ordinary proof of bounded amplification

Let `H` be the finite preparation register, `|0>` its fixed unit basis vector, `A_x` its unitary preparation on a fixed oracle input `x`, and `Π` the fixed success projector. All its gates and the success subspace are specified before `x`; only oracle calls depend on `x`. Put

\[
\psi_x=A_x|0\rangle,\qquad p_x=\|\Pi\psi_x\|^2\in[0,1].
\]

For `p_x>0`, write `g_x=Πψ_x/√p_x`. First fix `0<p_x<1`, suppress `x`, and put `b=(I−Π)ψ/√(1−p)`. These are orthonormal, and there is a unique `θ∈(0,π/2)` with `sin θ=√p`, `cos θ=√(1−p)`. Thus `ψ=sin θ g+cos θ b`.

Set

\[
S_0=I-2|0\rangle\langle0|,\quad S_\chi=I-2\Pi,
\quad G=-AS_0A^{-1}S_\chi.
\]

Because `AS₀A⁻¹=I−2|ψ><ψ|`, the matrix of `G` in the ordered orthonormal basis `(g,b)` is

\[
\begin{pmatrix}\cos2\theta&\sin2\theta\\-\sin2\theta&\cos2\theta\end{pmatrix}.
\]

The addition formulas therefore give, by induction on `ℓ≥0`,

\[
G^\ell\psi=\sin((2\ell+1)\theta)g+
\cos((2\ell+1)\theta)b.
\]

The projected successful part is a scalar multiple of the same `g`. On every successful branch, after normalization it is `g` up to a phase of modulus one. The statement is applied only when the projected vector is nonzero. For `p=0`, every iterate stays in the failure subspace. For `p=1`, every iterate is a phase multiple of the entire original state and succeeds with certainty. No normalized zero vector is treated as a conditional state.

Fix `0<γ≤1/2` and `0<η<1/2`, before seeing `p`, and define

\[
M=\left\lceil10/\sqrt\gamma\right\rceil,
\qquad
N=\left\lceil\frac{\ln(1/\eta)}{\ln(40/31)}\right\rceil.
\]

A trial chooses zero iterations with probability `1/2`, and otherwise chooses `ℓ` uniformly from `{0,…,M−1}`; equivalently, `Pr[ℓ]=1/(2M)+(1/2)1_{ℓ=0}`. It prepares `ψ`, applies `G^ℓ`, and measures only success versus failure. At most `N` independent fresh trials are run, stopping at the first success. The entire successful trial register is the output register. A successful trial may be swapped into a fixed output location by a query-free operation controlled on the recorded first-success index.

The trigonometric identity is

\[
\frac1M\sum_{\ell=0}^{M-1}\sin^2((2\ell+1)\theta)
=\frac12-\frac{\sin(4M\theta)}{4M\sin(2\theta)}
\quad(M\ge1,\ \sin2\theta\ne0).
\]

To see it, subtract `sin(4ℓθ)` from `sin(4(ℓ+1)θ)` and use the sine-difference formula to get `2 sin(2θ) cos((4ℓ+2)θ)`. Sum over `ℓ`, telescope, and then use `sin²u=(1−cos2u)/2`.

If `γ≤p≤1/2`, then `sin2θ=2√(p(1−p))≥√γ`, so `M sin2θ≥10`. Consequently the average is at least `1/2−1/(2M|sin2θ|)≥9/20`; the factor `2` in this weaker bound is the target paper's deliberately loose version of the exact factor `4`. The uniform half of the trial succeeds with probability at least `9/40`. If `p≥1/2`, the zero-iteration half alone succeeds with probability at least `p/2≥1/4≥9/40`. This covers `p=1` as well.

For fixed `x`, let `f₀(x)` be a trial's failure probability. Fresh choices and fresh registers give `Pr[all N fail]=f₀(x)^N≤(31/40)^N≤η` whenever `p_x≥γ`. At `p_x=0`, every trial fails, so the final failure probability is one. At every `p_x>0`, even below `γ`, the zero-iteration branch gives trial success at least `p_x/2>0`; because `N≥1`, the eventual success event is positive. The latter positivity is an elementary refinement useful when explicitly writing conditional distributions, though the application can instead make every conditional claim only on a positive success event.

Every successful trial has the same pure output density operator `|g_x><g_x|`. Mixing over iteration counts and over the first successful trial leaves that density operator unchanged. If all classical randomness is purified, and if first-success routing is made explicit, the success-projected global state has the form

\[
g_x\otimes\xi_x,
\]

where `ξ_x` contains seeds, stopping information, failed-trial workspaces and absorbed phases. Its squared norm is the overall success probability. This is the correct meaning of retaining all registers while returning the original successful state. No claim is made that all auxiliary registers return to zero.

Finally each trial uses `2ℓ+1≤2M−1` calls to `A` or `A⁻¹`; the source safely charges `2M+1`. Therefore on every branch, including `p<γ` and `p=0`, the call cap is at most `N(2M+1)`. Put `L=ln(1/η)`. Since `ln(40/31)≥1/4` and `L≥ln2≥1/2`, we have `N≤4L+1≤6L`. Also `M≤10/√γ+1`, and `√γ≤1`, so `2M+1≤23/√γ`. Hence

\[
N(2M+1)\le138\,\gamma^{-1/2}\ln(1/\eta).
\]

For the logarithm bound, `ln x≥2(x−1)/(x+1)` for `x≥1`, as follows by differentiating the difference; at `x=40/31` the right side is `18/71>1/4`. These are ordinary proofs, not results of a finite numerical experiment.

### Citation roles

The target construction and its finite stopping rule are OpenAI, supplied preprint §3.1, Lemma 3.1, printed pp.7–8. The invariant two-dimensional geometry is BHMT, `quant-ph/0005055v1`, §2, Lemma 1, printed pp.5–6, and equation (8), printed p.7. The random-iteration average is BBHT, `quant-ph/9605034v1`, §4, Lemma 2, printed p.3. BBHT Theorem 3, printed p.4, is expected-time; it is methodological ancestry, not the direct proof of a syntactic pointwise cap. BHMT Theorem 3, printed pp.8–9, likewise concerns expected calls and explicitly runs forever when the initial success probability is zero. BHMT Theorem 12, printed p.19, is amplitude estimation and should not be cited as bounded amplification. Adapted Lean geometry/averaging files preserve their separate Troy Lee code-provenance credit; that is not priority for the underlying mathematics.

## Successful label law and the zero-weight branch

Suppose the successful labels are `b∈β`, with unamplified masses `q_x(b)≥0` and `q_x=Σ_b q_x(b)`. In a normalized preparation, `q_x∈[0,1]`. On any successful amplified branch, measurement of the original output yields its conditional original law. Thus, for final failure probability `f_x`,

\[
\Pr[\bot]=f_x,\qquad
\Pr[b]=(1-f_x)\frac{q_x(b)}{q_x}\quad(q_x>0).
\]

When `0≤f_x<1`, the successful mass is `1−f_x>0`, and dividing by it gives exactly `q_x(b)/q_x`. The range and positivity hypotheses matter: the displayed algebra is not a conditional probability assertion on a null event. At `q_x=0`, every `q_x(b)=0` by nonnegativity and `f_x=1`, so the correct law is the point mass at failure. Lean's totalized division `0/0=0` is merely how its single algebraic definition is extended at zero; the separate `f_x=1` clause establishes the probability interpretation.

For tournament history `L`, set `w_i(L)=∏_{p∈L}a_{ip}` and `W=Σ_i w_i`. Assuming `0≤a_{ij}≤1`, all weights are nonnegative. Fresh independent comparison registers give

\[
q_x(i)=w_i/m,\qquad q_x=W/m.
\]

Thus the successful index law is `w_i/W` whenever the success event is positive. At `W=0` the stage stops with certainty. Before a dominant vertex `s` is listed, `w_s≥(1−ε)^{|L|}≥1−Tε=999/1000>1/2`, so `W/m≥1/(2m)` and the amplification promise holds with `γ=1/(2m)`. It need not hold after `s` is listed, nor on histories with no dominant vertex. The query cap continues to hold in both cases.

## Exact physical type gap

An exact additional theorem could be specified as follows. This is a mathematical specification, not elaborated Lean code or an assertion that the named helper exists.

Given finite `ι,Z`, a family `F : BitInput ι → (Reg Z ≃ₗᵢ[ℂ] Reg Z)` with `IsCirc n F`, a fixed origin `o:Z`, and a fixed coordinate success projector `Π`, let `p_x=‖Π(F_x|o>)‖²` and `g_x=Π(F_x|o>)/√p_x` for positive `p_x`. For `0<γ≤1/2`, `0<η<1/2`, there should exist a finite auxiliary register `J`, fixed start `j₀`, fixed heralding projector `Π_ok=I_Z⊗Π_J`, and a single input-uniform circuit family `V_x` on `Reg(Z×J)`, chosen independently of `x`, such that:

* `IsCirc [N(2M+1)n] V` (or an explicitly bounded larger padded read count);
* for every input, with `v_x=V_x|o,j₀>` and `s_x=‖Π_ok v_x‖²`, one has `0≤s_x≤1`;
* `p_x≥γ ⇒ s_x≥1−η`, and `p_x=0 ⇒ s_x=0`;
* whenever `p_x>0`, there is `ξ_x∈Reg J` with `Π_J ξ_x=ξ_x`, `‖ξ_x‖²=s_x`, and the **vector equality** `Π_ok v_x=g_x⊗ξ_x` (a unit phase may equivalently be included and absorbed into `ξ_x`);
* applying `compile_circ` to this same `V` gives a physical implementation with cap `2N(2M+1)n` on every branch and its continuation equation for every embedded input vector.

This output factorization or the equivalent conditional reduced-density equality is absent from the inspected `Samples` conclusions. A proof can use the finite tree of success/failure measurements, fresh trial registers, controlled routing, and reversal of copied bookkeeping tags. It should not use a premise that simply assumes the desired retained-state realization.

Suggested proposed declaration name: `QuarticQuery.Paper.quantum_amplification_retained_state`. Any actual Lean statement must define the tensor/flag interface and preserve the existential-before-input quantifier order above. The evidence state is **missing physical state-correspondence bridge**, not a paper assumption or a counterexample to Lemma 3.1.

### Exact two-dimensional counterexample to inference from a label law

Let `g=|+>=(|0>+|1>)/√2`, `Π=I`, and let the label be the computational-basis bit. Its successful label law is `(1/2,1/2)`. The orthogonal state `|->=(|0>−|1>)/√2` has exactly the same law, so even on the same register that law cannot establish state equality up to global phase.

More closely reflecting `Samples.bind`, copying the label into a fresh tag transforms `|+>|0>` into

\[
|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2.
\]

The original register's reduced density is `diag(1/2,1/2)`, whereas `|+><+|` is the matrix with all four entries `1/2`. A measurement in the `(|+>,|->)` basis distinguishes them: the original `g` gives `+` with probability one; the copied-label marginal gives `+` with probability `1/2`. Both have computational label law `(1/2,1/2)`. Since the full Bell state is pure, retaining all registers does not itself solve the mismatch. Erasing the copied tag by another controlled-NOT restores `g|0>` at zero query cost in this example; the full amplifier requires the corresponding general correspondence theorem.

The copied tag is visible in `Upper/Sampler.lean`: in `Samples.bind`, `W := Σ b, Zb b`, and `P z` swaps the fresh origin with `⟨out₁ z, ob (out₁ z)⟩`; the displayed `hslice` formula makes the resulting tag explicit. `Paper.quantum_attempts_samples` invokes this generic bind both for trial continuations and for the random length. The theorem is correct for the law it states; a theorem about the original quantum output register needs extra information.

## Physical query accounting

`IsCirc n` counts abstract signed, controlled reads. `compile_read` loads the addressed input bit, applies its controlled operation, and unloads with a second ordinary bit query. The read specification preserves the address under the controlled permutation, which is necessary to erase the loaded bit with the same second query. Thus `Samples.runs` gives `Runs (2*n)`, and `quantum_compile_circuit` exposes the same factor for arbitrary continuations. Inverting a circuit keeps the same read count. A controlled family can be padded to a common count and assembled by direct sums; its gates are selected from finite input-independent data.

Consequently the amplified logical read cap `N(2M+1)n` becomes physical cap `2N(2M+1)n ≤ 276 n γ^{-1/2}ln(1/η)`. If a comparison is first supplied in physical query units `c`, represent each ordinary bit query by one abstract read, then apply the generic compiler once. Do not silently identify the read and query counts; also do not multiply by two again at every nested macro after a final global compilation has already charged it.

## Context references that do not replace the tournament proof

Dürr–Høyer `quant-ph/9607014v2`, Theorem 1 and Lemmas 1–2, printed pp.1–2, searches in an ordered set and analyzes ranks; it supplies a conceptual predecessor for repeatedly sampling better candidates. The probabilistic comparison matrix in the target paper need not define an order, so the rank proof cannot be imported without its hypothesis.

Høyer–Mosca–de Wolf `quant-ph/0304052v2`, §1, PDF pp.1–2, and §3, PDF pp.4–7, assumes that **each** algorithm computes a definite underlying bit with uniformly bounded error (the presentation takes success at least `9/10`). It interleaves amplification and error reduction to search in `O(√n)` calls. False-candidate pair comparisons in the target tournament can have probabilities near one half with no chosen underlying orientation; the hypothesis match fails for a direct substitution. The relevant claim here is exact sampling proportional to the actual comparison probabilities, not suppression of every comparison to a fixed true bit.

## Scope of reading and validation

Assessed: target preprint §3.1; baseline §1.1, §2.2, §5.1 and amplification-related §5.2/§5.4 passages; BHMT §2's preparation/rotation and equation (8), plus exact theorem-role checks for Theorems 3 and 12; BBHT §4 Lemma 2/Theorem 3; Dürr–Høyer Theorem 1/Lemmas 1–2; HMW setup and §3 algorithm hypotheses. Assessed source interfaces: `Preparation`, `Proc`, `bounded_amplification`, `ampLaw`, `Samples`, `Samples.bind`, `Samples.amplify`, `quantum_attempts_samples`, `quantum_amplify_samples`, `quantum_amplified_conditional`, `amplification_budget_le`, physical compilation statements. Other source proofs were sampled at indicated declarations. The round-two construction/quantum adjudication was assessed at its quantum disposition and compilation table; no independent recreation of its source-current receipts was attempted by this subtask.

Primary online versions were opened and checked against their theorem locators through arXiv. No private access was used. No numerical search substitutes for the proofs above. No new Lean source was authored or compiled.
