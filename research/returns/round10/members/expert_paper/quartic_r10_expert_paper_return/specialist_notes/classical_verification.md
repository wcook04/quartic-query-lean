# Randomized lower-bound specialist verification

## Status and scope

This was the second simulated reader perspective, an informed specialist reread after the root reviewer's first-pass notes were frozen. It was not a blind read. The sequential reread covered the expert companion's §§2, 4, 5, 6 and then Appendices A.4–A.8, in that order. The root reviewer was notified when this sequence finished, before the editor perspective began. Subsequent work inspected the actual mathematical jobs delegated to the supplied reasoning record, selected primary literature, and a small number of supplied Lean statements.

No mathematical failure was established in the classical capped-simulator argument, its separate-cap product lemma, the erased-zero estimate, or the optional uniform Forrelation derivation in the passages inspected. This is a scoped verification result, not certification of the whole manuscript or formal development. No manuscript or Lean file was changed; no Lean build, Comparator run, submitted checker, or previous-return script was executed. The only executed checks were the new finite-example and arithmetic sanity checks in this directory.

**Edition boundary.** Every record-body locator below refers to the supplied repository/docs/reasoning_record.md. The companion's web links name commit 8357f268732746d1575e05e7de8c888e20ad3793. The packet's LINK_MAP.json reports that the pinned record differs from the packaged record. I did not independently obtain that commit's record. Consequently, “supports the claim” below means support in the supplied edition, not verified support in the immutable linked edition. The root reviewer is handling this traceability issue. Advice to add a record anchor presupposes a link to the edition that actually contains it.

## Classical mechanism

### Separate caps and adaptive interleaving

The companion's Lemma 5 uses a cap of \(L\) on **each** input on every branch, with auxiliary information and coins jointly independent of the whole input tuple. Its unnormalised recurrence is sufficient. For a subprobability measure \(\nu\), \(V_d(\nu)\) is the best correct-output mass at depth at most \(d\). A first query replaces one factor by the sum of its two restricted continuation values, which is at most that factor's previous value. Induction on the sum of remaining caps bounds the joint correct-output mass by the product of individual values. Zero-mass branches need no conditional probability. This addresses arbitrary adaptive interleaving.

The current record's #CL-weighted-values passage, lines 3152–3237, supplies this argument. The passage #CL-independent-information, lines 3012–3035, reduces arbitrary independent auxiliary randomness to a finite mixture of capped deterministic behaviours. Its parity example correctly shows why independence from each input separately is insufficient. Balanced answer bits are unnecessary, and the companion does not assume them.

Drucker's general-budget theorem is also a valid optional route. With \(T=L\), error \(1/3\), and \(\alpha=3/r\), its allowed budget is \(L\), and its success bound becomes \(2(2/3)^r\). Since \(r=20\ell\ge40\), the parameter is admissible. The companion does not mistake a general total-budget theorem for the exact separate-cap contract. The supplied arXiv-v2 text's theorem statement, §3 proof and fair-tree remark were inspected; its partial-function extension is explicit in its introduction.

### Truncation and the event actually bounded

For each fixed column and time, the simulator can sample all outside data independently of the target address tuple. It answers target queries until the next one would exceed the aggregate allowance \(L\), then aborts before that query. This stronger aggregate cap implies the separate cap needed by Lemma 5. At the designated cell query it outputs the queried address before reading the cell bit. Remaining branches receive a fixed default address. Under a light original run that visits the true address at that time, the simulator succeeds. This gives an **inclusion**, not equality; accidental success of a default output is harmless.

The current record, lines 3567–3662, establishes this mechanism and shows the default-output asymmetry in an explicit toy. The subsequent union over times and averaging over the independently selected column are valid. A proof that first conditions on terminal lightness would change the target law and is not the proof given.

The associated example link needs adjustment. Companion line 298 points to Appendix A.7 as support for a warning about terminal lightness. A.7 explicitly studies a different per-block compliance event. Its numbers are correct: among 16 equally likely inputs, 8 are compliant and 5 are both correct and compliant, giving conditional success \(5/8>9/16\). The exact terminal-lightness example already exists in the supplied record at #CL-conditioning-counterexample, lines 3639–3644. Link directly to that passage and either retarget A.7 or describe it as a related warning. This is a navigation/example mismatch, not a failed lower bound.

The exact toy's premise must be stated carefully. For AND on the uniform domain \(\{01,10,11\}\), every one-query deterministic tree succeeds with probability at most \(2/3\). A tree that continues only after seeing 1 selects an easy input when conditioned on being light. However, \(R(P)=1=L\): a randomized one-query algorithm achieves worst-case success \(2/3\) by choosing a coordinate uniformly, answering 0 after a 0, and answering 1 with probability \(2/3\) after a 1. Thus the toy meets the separate-cap lemma's hard-law premise; it does not meet strict \(L<R(P)\) or represent the final large-\(m\) construction. No new theorem or replacement construction is needed to make the warning useful.

### Erasure and the final discrepancy

Conditioning on a transcript prefix preserves a uniform location among the unqueried positions of an undiscovered zero. Early discoveries consequently have conditional probability at most \(2/m\) per query. Late discoveries occur in columns charged at least \(m/2\) queries each, of which there are at most \(2G/m\). Hence \(\mathbb EZ\le4G/m\). The independent uniform choice of \(I\) gives the separate identity \(\Pr[\text{selected zero hit}]=\mathbb EZ/m\). Current-record lines 3438–3502 supply both steps and the correct independence hypothesis.

The optional stronger estimate also checks out. On a fixed outside configuration, let the all-one reference path first visit \(d\) distinct positions of the selected column. Summing query cost over all \(m\) possible zero locations gives at least

\[
\sum_{s=1}^{d}s+(m-d)d=\frac{d(2m-d+1)}2\ge\frac{d(m+1)}2.
\]

Exactly \(d\) worlds discover the zero. Averaging yields the current record's expectation-cost refinement. This is not a proof of an optimal success curve for every worst-case cap, and the record correctly refrains from claiming one.

The main discrepancy estimate uses \(4G/m^2+G/(mL)+G\beta^r\). With \(G=\lfloor mL/100\rfloor\), \(1\le L\le m\), and \(\beta^r\le m^{-10}\), the displayed \(6/100<1/3\) bound is sound. The fixed-parameter floor step at \(t\ge8\) is also sufficient. No missing multiplicative factor in these steps was found.

## Optional uniform Forrelation estimate

### Distribution, interpolation and derivative growth

Current-record §§3.6–3.15, lines 854–1624, were read through the proof, not merely searched for anchors. The correlated law uses an algebraic bounded bias function, so it differs from both the published Gaussian-CDF construction and the later promised minimax law. The companion correctly says that it may put mass off the promise.

For \(q(x)=\sqrt{2+x^2}\), the record uses \(\Psi(x)=1/(2q(x))\) and \(\varphi(x)=x(3+x^2)/(2q(x)^3)\). The identities \(\varphi'=3/q^5\) and \(\varphi=x\Psi-\Psi'\) give the stated integration-by-parts formula. The kernel bound \(\Psi(x)\varphi'(y)\le3/16\) follows directly. These were checked algebraically.

The first-block interpolation passes a derivative along the Gaussian chain, one coordinate per labelled block. Multilinearity removes repeated differentiation in a coordinate, and independence of a fresh Gaussian link makes successive integration-by-parts steps legitimate. The resulting raw derivatives are evaluated at biased points; they retain higher uniform Fourier levels. The argument does not silently discard those levels or insert a missing \(k!\).

The derivative-growth proof centres coordinates as \(\xi_i=(z_i-\mu_i)/(1-\mu_i^2)\), so \(|\xi_i|\le2\) on the prescribed bias range. Its degree-\(r\) signed sum has increment \(\xi_qY_{r-1}^{c^q}\). The contraction is predictable, and the process is stopped before an excessive coefficient is used. This is different from conditioning on a future good event. The union over fixed contractions, maximal martingale estimate and chosen tail parameter supply the asserted \((16rd\ln(4n))^{r/2}+2^{-r}\) bound. Girish–Tal–Wu's ordinary-tree overview and stopping warning support the stated methodological antecedent; their cited lemma is not presented as already proving this exact bounded-bias raw-derivative estimate.

### Promise bridge and the numerical contradiction

The pointwise inequalities in companion line 365 are valid even off the promise. On the one-promise, correctness gives the lower inequality; elsewhere its left side is nonpositive. On the zero-promise, correctness gives the upper inequality; elsewhere the square term exceeds one. Thus no unjustified conditioning on promise membership is needed.

For the moment lower bound, the record controls the pathwise product of positive kernels by an exponential whose exponent has mean zero. Jensen's inequality then applies. This does not require independence between correlated Gaussian coordinates of a link. It gives \(a_k=18^{-(k-1)}\); the uniform second moment is \(1/m\).

The assembly at current-record #forr_uniform_assembly was checked in detail:

- \(18\cdot8^{25}<9^{25}\) yields amplification error at most \(a_k/18\) after \(50k\) runs.
- \(\delta\le a_k/32\), and \(m\ge2^{15k+2}\) gives \(4/(m\delta^2)\le\delta\).
- The lower acceptance gap is at least \((1-1/16-1/9)a_k=119a_k/144\).
- A zero-query solver is ruled out before absorbing the padding in \(d=50kD+1\).
- \(800(2/18225)=(8/27)^2\) and \((1+1/(50k))^k\le50/49<(9/8)^2\) bound the main upper term by \(a_k/3\).
- The residual is at most \(a_k/4\). Hence the upper bound \(7a_k/12\) is strictly smaller than the lower bound, with margin \(35a_k/144\).

The resulting strict bound (16), including its coefficient \(2/18225\), is supported by the inspected derivation. The explicit sufficient threshold \(t\ge13669k^2\) follows from the same statement. The supplied Lean file has a matching sharp theorem statement, but no compilation or dependency revalidation was attempted.

## Floors, growing \(k\), and delegated costs

The growing family correctly changes its allowance to \(L=\lfloor X\rfloor\), where \(X\) is the right side of (16). It does not substitute a growing \(k\) into a fixed-\(k\) asymptotic assertion. Under the stated conditions, the current record proves \(2\le X<m\), so \(L\ge X/2\) and \(L<R(P)\). Since randomized query complexity is integer-valued, \(R(F)>\lfloor mL/100\rfloor\) implies \(R(F)>mL/100\). There is no additional floor loss at this step; the denominator \(1822500\) is correct.

The current record's §7.3 explicitly expands \(C_k\) and checks \(C_k\le2^{53}k2^{10k}\). I verified that arithmetic and its connection to the displayed constants; I did not independently reprove the quantum algorithm. For readability, the companion could identify \(2^{10k}=\delta^{-2}\) as the cost of its specified projection decoder when importing this envelope. Section 2 already supplies that dependence, so this is a short bridge, not missing mathematics. Polynomial circuit dependence is absorbed in the envelope.

The choice \(k=\lfloor\sqrt{t/20}\rfloor\), \(t\ge80\), meets the new classical conditions. The finite exponent loss in current-record §7.3 tends to zero, and the classical lower bound diverges. The universal quartic upper bound then forces \(Q(F_t)\to\infty\). The manuscript correctly stops short of claiming \(R=\Omega(Q^4)\).

Two small navigation/precision recommendations remain. At (16), a theorem link should land directly on #forr_uniform_assembly; the current #forr_target starts with the fixed-\(k\) target before the lengthy derivation. The circuit sketch's “\(O(\ell)\) transform layers” is defensible when \(k\) is fixed, but clearer as “each of the \(k-1\) Walsh transforms has \(\ell\) layers,” especially before a section that exposes the \(k\)-dependence. Neither point changes the theorem.

## Evidence files

The final advice appears in [feedback.json](../feedback.json), particularly XP10-007, XP10-011 and XP10-012. [classical_proof_destinations.json](../evidence/classical_proof_destinations.json) records the advertised proof jobs and supplied-edition passages inspected. [sources_read.json](../sources_read.json) records exact reading scopes and edition limits. [literature_comparison.md](../literature_comparison.md) contains the primary-source comparisons. [finite_math_results.json](../checks/finite_math_results.json) records eleven passed finite-example/arithmetic checks, with their limited scope. The portable recomputation script changes only output handling from the reviewer’s original check script; the mathematical checks are unchanged.
