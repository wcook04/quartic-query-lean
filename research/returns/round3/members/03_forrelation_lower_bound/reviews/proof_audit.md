# Independent mathematical audit: the fixed-parameter Forrelation lower bound

This is an ordinary mathematical reading of the supplied packet. I found no mathematical gap in the first-block interpolation, repeated Stein elimination, biased decision-tree derivative estimate, promise-mass argument, or fixed-parameter threshold. I did not run Lean. Source-current build and Comparator findings belong to the separate evidence audit. Older draft statements about what had not been formalized must be updated against the current snapshot: in particular, the current source contains both the sharp edge helpers and `QuarticQuery.forrelation_lower_uniform_sharp`.

## 1. The exact statement and conventions

Fix an integer k≥2 and write ℓ=k−1, m=4^t. The input is k blocks of m signs; its length is km, not m. Let H be the normalized symmetric Walsh matrix. Its entries have absolute value m^(−1/2), and HHᵀ=I. With all indices in [m],

\[
\Phi(z)=\frac1m\sum_{p_0,\ldots,p_\ell}
   \prod_{j=0}^{\ell}z_j(p_j)
   \prod_{j=0}^{\ell-1}H_{p_{j+1},p_j}.
\]

The promise is 1 when Φ≥δ and 0 when |Φ|≤δ/2, where δ=32^(−k). In particular, large negative Φ is unpromised. Reading all km signs computes the partial function on its domain, so randomized complexity is a minimum over a nonempty set of natural budgets. The target is strictly R(P)>floor(m^(1−1/k)/(log₂m)²), for every t past a k-dependent threshold.

## 2. A useful simplification: the interpolation average is a polynomial

Let F be the multilinear extension of an arbitrary real function g on the finite sign cube:

\[
F(\mu)=\sum_z g(z)\prod_i\frac{1+\mu_i z_i}{2}.
\]

Every partial derivative of F is bounded on a fixed bounded box. Also ∂ᵢ²F=0. Put

\[
q(x)=\sqrt{2+x^2},\quad
\Psi(x)=\frac1{2q(x)},\quad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3},\quad
\varphi'(x)=\frac3{q(x)^5}.
\]

The identities φ=xΨ−Ψ′ and |φ|≤1/2 follow directly. For the latter, (2+x²)³−x²(3+x²)²=8+3x²≥0. The coarse bounds Ψ≤1 and φ′≤3 suffice; the sharp product bound is Ψ(x)φ′(y)≤3/16, attained at x=y=0.

Draw independent standard Gaussian vectors U₀,…,U_{ℓ−1}; set Vⱼ=HUⱼ, Xⱼ=φ(Uⱼ), Yⱼ=φ(Vⱼ). The bias wₛ is sX₀ in block zero, Yⱼ₋₁Xⱼ in intermediate block j, and Y_{ℓ−1} in the last block. Its coordinates are bounded by 1/2, and intermediate coordinates by 1/4.

**Finite-linearity alternative to dominated differentiation.** For fixed U, F(wₛ(U)) is a polynomial in s of degree at most m. Expanding the finite product writes it as ∑_{r=0}^m bᵣ(U)sʳ. Each bᵣ(U) is a finite sum of products of bounded functions, hence integrable. Thus

\[
h_g(s)=\mathbb E_U F(w_s(U))
       =\sum_{r=0}^m (\mathbb E b_r(U))s^r
\]

is an ordinary polynomial. Its derivative is obtained by finite linearity. This proves the needed exchange without a limit-under-integral theorem. It also supplies continuity on [0,1], differentiability in (0,1), and the ordinary mean-value or integral forms. The supplied Lean proof uses a dominated derivative theorem, which is also valid; this is a simplification of the exposition, not the claim that its route has a gap.

## 3. The zero endpoint, with the dependence accounted for

At s=0 the first block is identically zero. Clear subsequent blocks one coordinate at a time inside the average. Suppose all earlier blocks and some coordinates in the current block r have already been set to zero. Reflect U_{r−1} in the unit row H_{a,*}. This negates V_{r−1}(a), fixes V_{r−1}(b) for b≠a, and preserves the standard Gaussian measure. It may change X_{r−1}, but that occurs only in the already-cleared preceding block. Oddness of φ therefore negates just the uncleared current bias (r,a). The extension is affine in that coordinate, so averaging its values at opposite biases replaces that bias by zero without changing the expectation. After finitely many steps all biases are zero:

\[
h_g(0)=F(0)=\mathbb E_{\mathcal U}g.
\]

No independence of U and HU has been used. An equivalent proof integrates the independent standard-normal coordinates of V_{r−1} after the preceding block is removed. The reflection proof follows the local Lean construction more closely.

## 4. Stein identity and the explicit three-block calculation

If γ is the standard Gaussian density, then (Ψγ)′=−φγ. For a continuously differentiable G with G and G′ bounded, integrate (ΨGγ)′ on [−R,R] and let R tend to infinity. The boundary term vanishes and all integrands are bounded multiples of γ. Consequently

\[
\mathbb E[\varphi(U)G(U)]=\mathbb E[\Psi(U)G'(U)].
\]

Coordinatewise use is legitimate on the underlying product Gaussian space. There is no use of a nonsingular density for the singular pair (U,HU), nor any conditioning on HU while pretending that U remains independent.

For k=3 write U,U′ for the two independent layers, V=HU and V′=HU′. Let F_{0a,1b} denote the indicated mixed derivative of F. The bias is

\[
w_s=(s\varphi(U),\;\varphi(V)\varphi(U'),\;\varphi(V')).
\]

First,

\[
h_g'(s)=\sum_a\mathbb E\,[\varphi(U_a)F_{0a}(w_s)].
\]

Before applying Stein, the complete relevant chain rule is

\[
\frac{\partial}{\partial U_a}F_{0a}(w_s)
=s\varphi'(U_a)\underbrace{F_{0a,0a}(w_s)}_{0}
 +\sum_bH_{b,a}\varphi'(V_b)\varphi(U'_b)F_{0a,1b}(w_s).
\]

Hence

\[
h_g'(s)=\sum_{a,b}H_{b,a}\mathbb E\,
 [\Psi(U_a)\varphi'(V_b)\varphi(U'_b)F_{0a,1b}(w_s)].
\]

The earlier factor Ψ(Uₐ)φ′(V_b) is independent of the entire layer U′. The second chain rule is

\[
\frac{\partial}{\partial U'_b}F_{0a,1b}(w_s)
=\varphi(V_b)\varphi'(U'_b)
    \underbrace{F_{0a,1b,1b}(w_s)}_{0}
 +\sum_cH_{c,b}\varphi'(V'_c)F_{0a,1b,2c}(w_s).
\]

Another application of Stein yields the exact result

\[
h_g'(s)=\sum_{a,b,c}H_{b,a}H_{c,b}\mathbb E\,[
 \Psi(U_a)\varphi'(V_b)\Psi(U'_b)\varphi'(V'_c)
 F_{0a,1b,2c}(w_s)].
\]

Both zero terms need to be shown: merely saying that the method propagates along a path obscures why the derivative does not return to the block just entered. Also, the factor φ(U′_b) is the one removed by Stein; it is not differentiated as part of G.

For general k, the same invariant proves the path identity by induction. Upon entering block j, its selected derivative is already present, the still-unremoved factor is Xⱼ(pⱼ), and every accumulated weight depends only on earlier Gaussian layers. Differentiation in Uⱼ(pⱼ) kills the same-block term by the repeated derivative and produces only next-block terms. After ℓ steps,

\[
h_g'(s)=\sum_{p\in[m]^k}\left(\prod_{j<\ell}H_{p_{j+1},p_j}\right)
\mathbb E\left[\left(\prod_{j<\ell}\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))\right)
 \partial_{S_p}F(w_s)\right],
\qquad S_p=\{(j,p_j):0\le j<k\}.
\]

Boundedness of F and its derivatives on the bias box, and boundedness of φ, φ′, Ψ, justify every integration. Integrating over s gives the integral identity. The mean value theorem supplies one common s*∈(0,1) with h_g(1)−h_g(0)=h_g′(s*), which is the exact exported form.

The common bias is essential. The order-k derivative still contains all higher uniform degrees:

\[
\partial_{S}F(\mu)=\sum_{T\supseteq S}\widehat g(T)\mu^{T\setminus S}.
\]

Thus “only degree k” is potentially misleading; the exact claim is order-k derivatives evaluated at bounded, generally nonzero biases.

## 5. A rigorous biased decision-tree estimate

Fix n≥1 independent signs of means |μᵢ|≤1/2 and put ξᵢ=(Zᵢ−μᵢ)/(1−μᵢ²). These variables are centered, independent, and bounded by 2. Direct one-coordinate summation gives

\[
\partial_SF(\mu)=\mathbb E_\mu[g(Z)\prod_{i\in S}\xi_i(Z_i)]
\]

for distinct-coordinate S. Let T be a deterministic tree of depth at most d≥1 with real leaves of absolute value ≤1. Repeated queries and short leaves are allowed. Denote the set of coordinates revealed after i queries by Qᵢ and hold it fixed after termination. For any coefficient array |c(S)|≤1, set

\[
Y_r^c(Q_i)=\sum_{S\subseteq Q_i,\ |S|=r}c(S)\prod_{u\in S}\xi_u.
\]

At a fresh query q its increment is ξ_q Y_{r−1}^{c^q}(Q_i), with c^q(S)=c(S∪{q}); at repeated queries the increment is zero. Conditional on each transcript, the fresh coordinate retains its original centered product law. This follows because the event of following any fixed reachable path is precisely the cylinder specified by its distinct queried coordinates. No null-event conditioning is needed if the expectations are written as finite branch-weight sums.

For Λ>0 put K²=8dΛ. The maximal inequality needed is

\[
\Pr\{\max_{i\le d}|Y_r^c(Q_i)|>K^r\}\le(4n)^r e^{-\Lambda}.
\]

At r=0 the event is empty because |c(∅)|≤1. For the induction, stop the order-r process **before** any step when one of the n contracted order-(r−1) chaoses exceeds K^(r−1). By the induction hypothesis and a union bound, the probability that stopping occurs is at most n(4n)^(r−1)e^(−Λ). The stopped process has centered increments bounded by D=2K^(r−1).

For a centered random variable W∈[−D,D], the secant bound on exp gives E exp(λW)≤cosh(λD)≤exp(λ²D²/2). The latter inequality follows coefficientwise from (2j)!≥2ʲj!. Hence exp(λZᵢ−λ²D²i/2) is a nonnegative supermartingale for the stopped process Z. Stopping additionally at its first crossing of R, capped at d, is a finite-horizon operation: iterated conditional expectation shows its expectation is at most 1. On crossing it is at least exp(λR−λ²D²d/2). Taking λ=R/(D²d), and repeating for −Z, proves

\[
\Pr\{\max_{i\le d}|Z_i|>R\}\le2e^{-R^2/(2D^2d)}.
\]

For R=Kʳ this is 2e^(−Λ). The original process agrees with the stopped one until a coefficient failure. Thus its crossing probability is at most [2+n(4n)^(r−1)]e^(−Λ)≤(4n)ʳe^(−Λ). A simultaneous crossing and coefficient failure is included in the latter failure event; there is no missing case. The supplied Lean proof uses a looser double count of the failure event, which also satisfies its (4n)ʳ bound.

**The important logical point:** never condition the martingale on the event that all increment bounds hold. Such conditioning need not preserve the martingale law. Stopping before a failure is what proves the estimate.

At a leaf the conditional expectation of the full chaos equals the chaos on the coordinates queried there, since every monomial with an unqueried coordinate has mean zero. Therefore

\[
\mathbb E_\mu[T(Z)Y_r^c([n])]=\mathbb E_\mu[T(Z)Y_r^c(Q_d)].
\]

On the good event the terminal chaos is at most Kʳ; on every outcome it is at most (2n)ʳ. Choosing c(S) to be the sign of the desired derivative (and zero for other r-sets), then Λ=2r ln(4n), yields

\[
\sum_{S\in\mathcal F}|\partial_S\widetilde T(\mu)|
\le(16rd\ln(4n))^{r/2}+2^{-r}.
\]

The weaker residual +1 suffices for the fixed-parameter proof and matches the baseline's simplification. This proof covers any selected family of distinct r-element subsets, not just the complete level. Paths choose one coordinate in each labeled block, so they give distinct k-subsets with no factor k!.

Combining with the path identity and coarse edge bound gives, for every tree and hence every mixture,

\[
|\mathbb E_{\nu_1}T-\mathbb E_{\mathcal U}T|
\le\left(\frac3{\sqrt m}\right)^{k-1}
 [(16kd\ln(4km))^{k/2}+1].
\]

## 6. Moments and the promise

Distinct Forrelation paths are distinct sign monomials, hence orthogonal under the uniform product law. There are mᵏ paths, and the square of each Walsh coefficient is m^(−k−1). Therefore E_U Φ=0 and E_U Φ²=1/m.

For the hard mean, eᵃ≥1+a with a=(x²−1)/3 gives

\[
q(x)\le\sqrt3e^{(x^2-1)/6},\qquad
\Psi(x)\varphi'(y)\ge\frac1{18}
 e^{-(x^2-1)/6-(5/6)(y^2-1)}.
\]

For any fixed path let A_p be the sum of these quadratic exponents over its ℓ edges. Every U coordinate has second moment 1; each selected V coordinate is a unit-row linear form and also has second moment 1. Thus E A_p=0, even though U and V in one layer may be correlated. Also A_p≥−ℓ, so exp(−A_p) is bounded, and A_p is integrable. Pointwise exp(−A_p)≥1−A_p gives its expectation at least 1. Each path weight has expectation at least 18^(−ℓ).

Apply the path identity to Φ. Its selected k-th derivative is the constant m^(−1)∏H. Multiplication by the path coefficient gives m^(−1)∏H²=m^(−k), all positive. Summing mᵏ terms gives

\[
\mathbb E_{\nu_1}\Phi\ge18^{-(k-1)}\ge32\delta.
\]

**Optional shorter route for the mean only.** Conditional rounding of one sign path gives the product of φ(Uⱼ(pⱼ))φ(Vⱼ(pⱼ₊₁)) over independent layers. One coordinate Stein identity replaces each pair expectation by H_{pⱼ₊₁,pⱼ}E[Ψ(Uⱼ(pⱼ))φ′(Vⱼ(pⱼ₊₁))]. The same squares and bound result. This is valid but the main section can use the full identity already proved, which keeps its proof spine simpler.

If an acceptance probability a∈[0,1] has promise error ε, then the following are valid at every input, including unpromised inputs:

\[
(1-\varepsilon)(\Phi-\delta)\le a\le\varepsilon+4\Phi^2/\delta^2.
\]

The first uses correctness only on Φ≥δ and nonnegativity elsewhere; the second uses correctness only on |Φ|≤δ/2 and a≤1 elsewhere. Consequently

\[
\mathbb E_{\nu_1}a\ge(1-\varepsilon)(18^{-(k-1)}-\delta),\qquad
\mathbb E_{\mathcal U}a\le\varepsilon+4/(m\delta^2).
\]

## 7. Amplification and a checked sufficient threshold

Repeat a depth-L error-1/3 algorithm independently 2τ times; any wrong majority implies at least τ errors, even with arbitrary fixed tie breaking. Markov's inequality for 2^{number of errors} gives error at most 2^(−τ)(4/3)^(2τ)=(8/9)ᵗᵃᵘ and depth at most 2τL. Every random seed gives a deterministic tree, and finite input/history spaces allow collection into a finite mixture. This does not change the worst-case query convention.

Choose τ so ε=(8/9)ᵗᵃᵘ<δ. An explicit possible choice is τ=30k: the exact integer inequality 32·8³⁰<9³⁰ implies it. The baseline's existential choice is equally valid.

Put X=m^(1−1/k)/(2t)² and L=floor X. For t≥8, 4t²≤2ᵗ≤m^(1−1/k), so X≥1 and d=2τL+1≤(2τ+1)X. Let

\[
C=16k(2\tau+1)(\ln(4k)+2),\quad
\eta_0=\min\{1,\delta^2/(4\cdot9^{k-1})\},
\]

\[
t_0=\max\left\{8,\left\lceil C/\eta_0\right\rceil,
 \left\lceil2\cdot3^{k-1}/\delta\right\rceil,
 \left\lceil4/\delta^3\right\rceil\right\}.
\]

For every t≥t₀, ln(4km)≤(ln(4k)+2)t. Since Xᵏ=m^{k−1}/(2t)^{2k}, the square of the leading advantage term is at most 9^{k−1}(C/(4t))ᵏ≤δ²/4. The residual is at most 3^{k−1}2^(−t)≤3^{k−1}/t≤δ/2. Thus the full advantage is ≤δ. Also m=4ᵗ≥t≥4/δ³ gives 4/(mδ²)≤δ. The uniform acceptance expectation is at most 2δ, the hard one is at most 3δ by the advantage bound, but the moment lower bound gives at least 31δ/2. This contradiction applies at every t≥t₀, not merely along a subsequence.

Therefore no depth-L algorithm exists, and the least successful integer query budget is >L. Both promise values must occur in these dimensions, because otherwise a constant zero-query algorithm would succeed.

## 8. Evidence and editorial dispositions

1. **No extra analytic hypothesis needed.** All objects are finite-dimensional, all cube extensions are finite polynomials, all Stein integrations are of bounded functions with bounded coordinate derivatives, and all martingales have finite deterministic horizons.
2. **No independence error found.** Independence is used for different underlying Gaussian coordinates/layers and for signs conditional on their biases. U and HU in one layer remain correlated.
3. **No factorial lost.** Paths index distinct coordinate sets because blocks are labeled. Do not sum over arbitrary orderings of one set.
4. **No promise-support assumption.** The two pointwise acceptance inequalities are necessary and sufficient; high negative values remain unpromised.
5. **No hidden uniform theorem inferred from fixed k.** The fixed theorem alone does not supply a numerical threshold or coefficient in k. Its intermediate estimates can support separate uniform theorems.
6. **Current evidence supersedes historical status.** `forrelation_lower_uniform_sharp` is present at Uniform.lean527. The evidence auditor reports exact membership in source-current root-build and reviewed-axiom receipts, but not Comparator. This report independently inspected the source statement and the corresponding parameter argument; it did not verify those receipts itself.
7. **SSW remains a distinct input.** The sharper Fourier theorem is not needed for any proof above. Neither a current sharp elementary theorem nor fixed-parameter Comparator evidence implies the SSW-dependent theorem.
8. **The most useful exposition change** is the explicit k=3 double cancellation and the finite-polynomial justification for the interpolation derivative. Both clarify why the shorter route is mathematically legitimate without changing its conclusion.

## 9. Reading and checks performed

Read READ_ME_FIRST.md; baseline §1.1 and §3.1, all §§3.6–3.17; earlier route note §§1–7 and formal-boundary passage; quantitative note all displayed proof sections, including finite elementary/sharp inequalities and the full stopped-martingale proof; blueprint and review in full. Inspected current Lean Walk.lean272–524, TreeGrowth.lean414–440 and514–600, and relevant declaration locators across Stein/Promise/Main. Inspected Uniform.lean1–145 and420–565 and Main.lean81–118,366–395. The baseline has 11 assigned sections and the neighboring interface; this reading does not claim to have assessed the rest of its full manuscript.

Only finite exact arithmetic was run: 32·8³⁰<9³⁰, 18·8²⁵<9²⁵, and 800·(2/18225)=(8/27)². These checks corroborate explicit constants and are not proof evidence for the analytic statements. No numerical quadrature, probabilistic sampling, Lean execution, or Comparator run was performed.

## 10. Addendum: a substantially simpler explicit fixed-k threshold

The root proposes replacing the cumbersome four-term threshold by a consequence of the **current** sharp elementary uniform theorem. This is mathematically valid and is a useful simplification, provided the replacement section actually proves the numerical uniform estimate before using it.

Write c=2/18225 and α=1−1/k. The current source theorem states

\[
R(P_{k,4^t})>c\frac{m^\alpha}{k^2\ln(4km)}
\quad\text{when }k\ge2,\quad15k+2\le2t.
\]

Set t₀(k)=13669k². For every integer t≥t₀(k), the following implications are exact:

- k≤k²≤13669k²≤t, so the existing `log_four_k_m_le` applies.
- 15k+2≤16k≤16k²≤27338k²≤2t, so the uniform theorem's dimension hypothesis holds. The first inequality uses k≥2.
- k>0, t>0, m=4ᵗ>0, and 4km>1, so every denominator being compared is positive.
- ln(4km)≤6t, and c/6=1/54675.
- 4t≥4·13669k²=54676k²>54675k².

It follows that

\[
R(P_{k,4^t})>
 c\frac{m^\alpha}{k^2\ln(4km)}
\ge\frac{m^\alpha}{54675k^2t}
>\frac{m^\alpha}{4t^2}
\ge\left\lfloor\frac{m^\alpha}{(2t)^2}\right\rfloor.
\]

This is strict for every t≥t₀(k), including t=t₀(k). It requires no additional asymptotic argument. The identity log₂(4ᵗ)=2t supplies the exact original target.

### Ordinary proof of the sharp uniform estimate needed here

Let a=18^(−k+1), b=3/16 and suppose an error-1/3 algorithm has integer depth

\[
L\le\frac2{18225}\frac{m^{1-1/k}}{k^2\ln(4km)}.
\]

Take τ=25k. Then ε=(8/9)^(25k)≤18^(−k)=a/18, because 18·8²⁵<9²⁵. Also δ≤a/32 and the dimension hypothesis implies q=4/(mδ²)≤δ. The weaker all-input acceptance inequalities already proved give a hard-minus-uniform acceptance gap at least

\[
(1-\varepsilon)(a-\delta)-\varepsilon-q
\ge a-2\delta-2\varepsilon
\ge\frac{119}{144}a.
\]

If L=0, the amplified acceptance is constant and has gap zero, a contradiction. Thus L≥1, and one may use the unpadded positive depth d=50kL in the ordinary derivative estimate. Its K² parameter satisfies

\[
16kd\ln(4km)=800k^2L\ln(4km)
\le\frac{64}{729}m^{1-1/k}
=\left(\frac8{27}\right)^2m^{1-1/k}.
\]

Since b·(8/27)=1/18, the leading term of the sharp advantage estimate is at most (8/27)a. The residual is at most a/4: the dimension hypothesis implies m≥16, hence b/√m≤1/18, while 2^(−k)≤1/4. Thus the full advantage is at most

\[
\left(\frac8{27}+\frac14\right)a=\frac{59}{108}a
<\frac{119}{144}a.
\]

The exact difference is 121a/432>0. This proves the numerical uniform estimate without the stronger promise probability denominator 1−δ and without SSW. The current Lean proof pads d to 50kL+1 and correspondingly uses a/3 instead of 8a/27 for its leading term. The ordinary unpadded proof is a valid simplification, with the same final theorem, but not a literal step-for-step reconstruction of the current tactic proof.

### Can the threshold be improved while using the same logarithmic lemma?

Using only ln(4km)≤6t and c=2/18225, the exact sufficient integer threshold from this comparison is

\[
t\ge\left\lceil\frac{54675}{4}k^2\right\rceil.
\]

The sharp query bound is already strict, so equality in the denominator comparison is harmless. The simpler 13669k² is within k²/4 of this threshold and avoids a new ceiling expression. No improvement of substance follows from the same 6t estimate alone. A stronger elementary logarithmic bound would lower the constant, but would add arithmetic that is unnecessary for the fixed-k conclusion. Recommendation: use 13669k² and expressly label its transport as an ordinary proved corollary, unless it is subsequently compiled as its own declaration.

The arithmetic constants in this addendum were checked with exact rational/integer computation. A sample of premise inequalities at k=2,…,24 was also checked, but the general proof is the displayed algebra, not that finite sample.
