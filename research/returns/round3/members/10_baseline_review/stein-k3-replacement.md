<a id="R3-STEIN-K3"></a>
<!-- passage:R3-STEIN-K3 -->
# Concrete difficult-passage improvement: the three-block Stein calculation

## Disposition

This is an explanatory expansion of the already stated identity `NEW-FOR-13`, not a new mathematical claim or a new proof route. The baseline's general argument is correct on inspection, but its hardest transition compresses two distinct facts: a repeated cube derivative kills the derivative through the current block, and every weight created earlier is independent of the next Gaussian vector. The three-block case makes both facts visible before the induction. It also makes clear that the mean-value parameter is chosen for the complete scalar expectation, not separately for each path.

Use this as a replacement inside the existing `forr_identity` passage, §3.10. Preserve its opening paragraph justifying differentiation under the Gaussian expectation. Replace the following two paragraphs, from “Apply the coordinate Stein identity in \(U_0(a)\)” through “the iteration stops”, with the text below. Preserve the subsequent boundedness paragraph, the exact `NEW-FOR-13` display and all following prose. The only minor follow-on edit is to replace “The parameter may depend on \(g\)” after the display by “The mean value theorem was applied to the whole scalar function \(h_g\), so one parameter \(s_*\) serves every path; it may depend on \(g\).”

The packet anchor and exact old boundary excerpt, rather than a mutable line number, govern application. In the frozen baseline the replacement starts at line 542 and ends at line 544.

## Ready-to-apply text

```markdown
First take \(k=3\), so there are two Gaussian vectors \(U_0,U_1\) and the three blocks of biases are
\[
w_s=(sX_0,\;Y_0X_1,\;Y_1).
\]
Products within a block are coordinatewise. For this calculation write \(D_{r,a}=\partial_{(r,a)}\), and keep the same bias \(w_s(U)\) in every extension below. The derivative formula just proved is
\[
h'_g(s)=\sum_a\mathbb E\!\left[X_0(a)\mathcal E_{w_s}D_{0,a}g\right].
\]
Apply the coordinate Stein identity to \(X_0(a)=\varphi(U_0(a))\). Differentiating the extension with respect to \(U_0(a)\) can affect its first or second block. The first-block contribution is
\(s\varphi'(U_0(a))\mathcal E_{w_s}D_{0,a}^{2}g=0\), because a multilinear extension has zero second derivative in the same coordinate. The second-block contribution through coordinate \(b\) is
\(H_{b,a}\varphi'(V_0(b))X_1(b)\mathcal E_{w_s}D_{0,a}D_{1,b}g\). Consequently
\[
h'_g(s)=\sum_{a,b}H_{b,a}\,
\mathbb E\!\left[
\Psi(U_0(a))\varphi'(V_0(b))X_1(b)
\mathcal E_{w_s}D_{0,a}D_{1,b}g
\right].
\]
Now eliminate \(X_1(b)=\varphi(U_1(b))\) in the same way. The factor \(\Psi(U_0(a))\varphi'(V_0(b))\) depends only on \(U_0\), so differentiation in \(U_1(b)\) leaves it unchanged. The contribution through the middle-block bias is
\(Y_0(b)\varphi'(U_1(b))\mathcal E_{w_s}D_{0,a}D_{1,b}^{2}g=0\). Differentiation through the last-block coordinate \(c\) remains and gives
\[
\begin{aligned}
h'_g(s)=\sum_{a,b,c}H_{b,a}H_{c,b}\,
\mathbb E\!\bigl[&\Psi(U_0(a))\varphi'(V_0(b))
\Psi(U_1(b))\varphi'(V_1(c))\\
&\mathcal E_{w_s}D_{0,a}D_{1,b}D_{2,c}g\bigr].
\end{aligned}
\]
There is now one cube derivative in each block and no remaining \(X\) factor to eliminate.

The general induction repeats these two steps. After choosing \(a_0,\ldots,a_j\), the term still to be eliminated has the factor
\(X_j(a_j)\mathcal E_{w_s}\partial_{(0,a_0)}\cdots\partial_{(j,a_j)}g\), multiplied by weights depending only on \(U_0,\ldots,U_{j-1}\). Stein in \(U_j(a_j)\) leaves those weights unchanged. Its effect on the current-block bias vanishes by the repeated derivative at \((j,a_j)\); its effect on bias \((j+1,b)\) contributes
\(H_{b,a_j}\varphi'(V_j(b))X_{j+1}(b)\) and a new cube derivative at \((j+1,b)\). At the last block the convention is \(X_\ell=1\), so the iteration stops after \(\ell=k-1\) eliminations. This convention also covers \(k=2\) directly.
```

## Why this attempt succeeds, and its limits

The worked case is an exact two-step derivation, with all terms caused by the chain rule accounted for. It explains why differentiating analytic weights does not create additional terms at the next step: those weights depend on earlier Gaussian vectors. Its conclusion retains the common nonzero bias. Thus it does not suggest that only the degree-three uniform Fourier coefficients contribute. In the baseline's following expansion of \(\mathcal E_\mu\partial_Jg\), every uniform Fourier coefficient indexed by a superset of \(J\) still contributes when the bias is nonzero.

The computation is a specialization of the local proof in `QuarticQuery/ForrelationLower/Walk.lean`: `sum_dw_eq`, `integral_walk`, `exists_identity`, and `Int_eq_paths`. It is not represented as a separately compiled new Lean theorem. It does not repair or bypass any unproved premise in the local argument, and it makes no historical novelty claim. It is distinct from Bansal–Sinha's Gaussian-CDF truncation and multilevel Fourier expansion.

The replacement deliberately leaves the finite-dimensional differentiation and dominated-convergence justification in place. It also leaves the later uniform-in-bias derivative estimate in place; the three-block computation alone is not a decision-tree lower bound.
<!-- /passage:R3-STEIN-K3 -->
