<a id="R3-BS-LOG-DEFICIT"></a>
<!-- passage:R3-BS-LOG-DEFICIT -->
# Bansal–Sinha v3 source audit for the frozen long-record review

This is a bounded audit of the named source passages and their use in the supplied baseline. It is not an independent review of every proof in Bansal–Sinha and it does not refute Theorem 1.3.

## Exact source and hypotheses

Mathematical source: Nikhil Bansal and Makrand Sinha, *k-Forrelation Optimally Separates Quantum and Classical Query Complexity*, arXiv:2008.07003v3, 17 November 2020. The packet's 40-page PDF has Theorem 1.3 and Corollary 1.4 on printed/PDF p. 4; Theorem 3.2, Theorem 3.3 and Theorem 3.4 on p. 17; Corollary 3.5 on p. 18; the disputed §5.4 display on p. 38. The corresponding TeX source was extracted without changing packet bytes to:

`main.tex, extracted from the packet’s version-pinned Bansal–Sinha source archive (see the source receipt)`.

Its SHA-256 is `800119f9f12877392a92e34ac380c61a50b2a297cee0a70511058580061f835b`. Theorem 1.3 is lines 261–265, the competing inequalities are lines 1180–1181, and the ensuing depth threshold is line 1184. The older second-reading memorandum sometimes calls the subtheorems 4.2/4.5; the actual supplied PDF prints 3.2/3.5.

Their parameter `N` is one block's length, equal to the baseline's `m`; total input length is `kN`. The dimension is a power of two; using powers of four is an allowed restriction. The normalized path expression is `N^{-1}` times the sum over `k` indices with `k−1` normalized Walsh entries. It equals the baseline's alternating matrix product. Inputs are signs in `{−1,1}^{kN}`; the partial Boolean output is in `{0,1}`. Its promise is value one when `Φ≥δ`, value zero when `|Φ|≤δ/2`, undefined otherwise; `δ=2^{-5k}`. In particular this is not a two-sided sign promise.

Theorem 1.3 states that error at most `1/2−η/2` requires

\[
\Omega\!\left(k^{-28}\left(\frac{m}{\log(km)}\right)^{1-1/k}
             \frac{\eta^2}{\log(1/\delta)}\right)
=\Omega\!\left(k^{-29}\left(\frac{m}{\log(km)}\right)^{1-1/k}\eta^2\right).
\]

Here the advantage above success probability one half is `η/2`, not `η`; error `1/3` corresponds to `η=1/3`. The proof first amplifies the original depth `d` by `τ=Θ(η^{-2}log(1/δ))` to amplified depth `d₁=Θ(dτ)`. Its function `f:{−1,1}^{km}→[0,1]` is that amplified algorithm's acceptance probability, not a sign-valued output. In the source's polynomial-extension notation `f(0)=E_unif f`, since the argument zero refers to the vector of biases, not an input in the sign cube.

The source's `wt^μ_ℓ(f)` is the sum of absolute coefficients for the orthonormal biased basis with factors `(z_i−μ_i)/sqrt(1−μ_i²)`, for `|μ_i|≤1/2`. It is not literally the raw derivative normalization used in the local reconstruction. The latter satisfies

\[
\mathcal E_\mu\partial_S f
=\widehat f^{\,\mu}(S)\prod_{i\in S}(1-\mu_i^2)^{-1/2}.
\]

The source subtheorems are used in their own normalization; no missing conversion is needed to audit their §5.4 algebra.

## The actual display

Writing `Λ=log(km)` and retaining an absolute constant `c₀` from the Fourier estimate, Theorem 3.2 and Corollary 3.5 give the level terms. The literal line 1180 writes `sqrt(d₁^ell log(km)^(ell−1))` without the constant from Corollary 3.5; the display below restores that harmless constant before analyzing the logarithmic exponents.

\[
\left|\mathbb E_{p_1}f-f(0)\right|
\le \sup_{|\mu|\le1/2}\sum_{\ell=k}^{k(k-1)}
 m^{-\ell(1-1/k)/2}(8k)^{14\ell}\operatorname{wt}^{\mu}_{\ell}(f)
\le \sum_{\ell=k}^{k(k-1)}
 m^{-\ell(1-1/k)/2}(8k)^{14\ell}
 (c_0d_1)^{\ell/2}\Lambda^{(\ell-1)/2}.
\]

Levels greater than the tree depth have zero coefficients, so the source's condition `ℓ≤d₁` in Corollary 3.5 does not require retaining any nonzero higher-level terms. The problematic next displayed inequality is

\[
\sum_{\ell=k}^{k(k-1)}
 m^{-\ell(1-1/k)/2}(8k)^{14\ell}
 (c_0d_1)^{\ell/2}\Lambda^{(\ell-1)/2}
\ \stackrel{\text{printed}}\le\ 
\sum_{\ell=k}^{k(k-1)}
 \left(Cd_1k^{28}\left(\frac{\Lambda}{m}\right)^{1-1/k}\right)^{\ell/2}.
\]

Take `C=8^{28}c₀` to align constants. The ratio of the left summand to the right summand is exactly

\[
\Lambda^{(\ell-1)/2-\ell(1-1/k)/2}
=\Lambda^{(\ell/k-1)/2}.
\]

For fixed `k` and fixed `ℓ>k`, this ratio tends to infinity with `m`. Changing an absolute constant to a larger constant cannot absorb that growth. Even permitting a different constant depending on this fixed `k` would not absorb it. This issue is therefore separate from quantitative bookkeeping in a growing-`k` limit.

For `k=2`, the level range contains only `ℓ=k=2`, where the powers agree. For `k≥3`, a level exceeding `k` is present. This tests the displayed bound between sums, not the true magnitude of a decision tree's advantage.

### Explicit smallest obstruction: k=3, ℓ=6

The actual level-six expression is, up to a fixed positive constant,

\[
m^{-2}d_1^3\Lambda^{5/2}.
\]

The printed replacement has `m^{-2}d₁³Λ²`. Their ratio is `sqrt(Λ)`. At the advertised amplified-depth scale `d₁=a(m/Λ)^{2/3}` for any fixed `a>0`, the actual expression becomes `a³sqrt(Λ)` while the printed expression is `a³`. The `k^{-28}` and other numerical factors are constants when `k=3`; reinstating them does not remove the divergence. Integer rounding of the depth does not affect this conclusion for sufficiently large `m`. The left sum contains this nonnegative term and the printed right sum stays bounded at that threshold, so the inequality between the sums fails, not just a convenient termwise proof of it.

There is a separate exceptional-mass transcription in equation (5.31): the PDF prints `δ²/(4m)`, whereas the preceding uniform second-moment/Markov argument gives `4/(mδ²)`. For fixed `k` both vanish with `m`, so replacing this term changes a sufficient size threshold and does not remedy or create the logarithmic issue.

## What follows and what does not

1. The exact logarithmic comparison in the inspected display is unsupported for `k≥3`. No author-confirmed erratum was supplied, and this audit did not locate or assume a repair proving the sharp stated logarithmic exponent.
2. This is not a counterexample to the theorem's claimed query lower bound. The divergence concerns an upper estimate used in one proof, not an achieved algorithmic advantage or an efficient decision tree.
3. The fixed-`k` endpoint needed in the separation is much weaker. Even the scale `m^(1−1/k)/log(km)` exceeds `m^(1−1/k)/(log₂m)²` eventually for every fixed `k`. Indeed, if `m≥k`, then `log₂(km)≤2log₂m`, and the ratio of those scales is at least `(log₂m)/2` after a fixed change-of-base constant.
4. The weaker denominator of one logarithm can be recovered from the displayed multilevel ingredients: write each level term as `Λ^{-1/2} x^{ℓ/2}`, where `x=Ck^{28}d₁Λ/m^(1−1/k)`. If `x≤1/4`, the sum is at most `2^{1−k}/sqrt(Λ)`, which is below `δ/4` for all sufficiently large `m` with `k` fixed. This is a deduction from those cited ingredients, not an independently audited proof of them, and it is not a repair of the sharper Theorem 1.3 statement. Reversing the preliminary constant-error amplification gives a fixed-`k` lower bound of order `m^(1−1/k)/log(km)`.
5. The supplied local proof independently discharges `QuarticQuery.BansalSinhaLower` by `QuarticQuery.ForrelationLower.bansalSinhaLower`. Expanded, this is

```lean
∀ k : ℕ, 2 ≤ k → ∃ t₀ : ℕ, ∀ t : ℕ,
  t₀ ≤ t → Lvalue k t < R (P k t)
```

It does not assert the stronger exact BS logarithmic expression. Its validity and source-bound compilation receipts are a separate evidence question, handled by the parent audit.

## Ready-to-apply replacement for baseline §3.6

Replace the full anchored passage `forr_bs_translation`, including its evidence paragraph, with the following. This preserves `claim-bs-to-L`; no change to that mathematical statement is proposed.

```markdown
<a id="forr_bs_translation"></a>
<!-- passage:forr_bs_translation -->

### 3.6. The published statement and the lower-bound scale needed here

Bansal and Sinha state a randomized lower bound of
\(c k^{-29}(m/\log(km))^{1-1/k}\), for an absolute \(c>0\), for error at most \(1/3\) on the same \((2^{-5k},k)\)-Forrelation promise [BS21, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, p. 4]. Their \(N\) is our block length \(m\), not the total input length \(km\). The normalized product and both promise thresholds agree. Theorem 1.3 parameterizes error as \(1/2-\eta/2\); here \(\eta=1/3\). A fixed change of logarithm base is absorbed into \(c\).

The numerical implication used by the OpenAI preprint is straightforward. Fix \(k\ge2\), put \(\alpha=1-1/k\), and use base-two logarithms. For \(m\ge k\), \(\log_2(km)\le2\log_2m\). Dividing the stated lower-bound scale by the unfloored definition of \(L\) gives at least
\(c k^{-29}2^{-\alpha}(\log_2m)^{2-\alpha}\), which tends to infinity because \(2-\alpha=1+1/k>0\). Thus, for every \(c>0\) and fixed \(k\), all sufficiently large powers of four satisfy

<!-- claim:claim-bs-to-L -->
\[
c k^{-29}\left(\frac{m}{\log_2(km)}\right)^{1-1/k}
>\frac{m^{1-1/k}}{(\log_2m)^2}
\ge\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor=L.
\]

The stated theorem and the inspected derivation need separate records. In v3 §5.4, p. 38, the step between `main.tex` lines 1180–1181 replaces the logarithmic exponent \((\ell-1)/2\) by \(\ell(1-1/k)/2\) at levels \(k\le\ell\le k(k-1)\). The ratio is \(\log(km)^{(\ell/k-1)/2}\). It grows with \(m\) for every fixed \(\ell>k\); already \(k=3,\ell=6\) leaves a factor \(\sqrt{\log(3m)}\). The supplied source audit therefore does not establish that displayed implication. This finding concerns that proof step and does not refute Theorem 1.3. The ensuing depth threshold is on line 1184. Equation (5.31) also prints \(\delta^2/(4m)\) where the preceding second-moment estimate gives \(4/(m\delta^2)\); that separate correction affects the sufficient size threshold.

The separation needs only the weaker fixed-\(k\) statement \(R(P)>L\). Sections 3.7–3.15 prove it independently by the local interpolation and decision-tree argument. Even a lower-bound scale \(m^{1-1/k}/\log(km)\) would exceed \(L\) eventually, since its ratio to the unfloored \(L\) grows as \(\log m\). No claim about the exact logarithmic exponent of the published theorem is needed for that internal proof.

**Source correspondence.** The current snapshot contains the numerical comparison itself in `QuarticQuery.Paper.construction_claim_bs_to_L`; `QuarticQuery.Paper.construction_bs_comparison_chain` also states the unfloored middle inequality. Their premises are \(k\ge2\) and \(c>0\), and neither asserts a randomized lower bound. By contrast, `QuarticQuery.ForrelationLower.bansalSinhaLower` proves the eventual endpoint \(L<R(P)\) by the separate local route. A receipt for the latter endpoint cannot certify the sharp published expression; a receipt for the former arithmetic statement cannot certify the source theorem either. Current source-bound validation is recorded in the evidence appendix.
<!-- /passage:forr_bs_translation -->
```

## Ready addition to §3.16

At the start of `forr_attribution`, replace the sentence beginning “Bansal and Sinha prove a stronger randomized lower bound” with:

> Bansal and Sinha state a quantitatively stronger randomized lower bound, with explicit dependence on the error advantage and on \(k\), for the same small threshold [BS21, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, p. 4]. Section 3.6 records both its numerical implication for our target scale and the unresolved logarithmic comparison in the inspected v3 proof. The independent fixed-\(k\) proof given here establishes the weaker endpoint required by the total-function construction; it does not resolve that sharper source statement.

Retain the subsequent ancestry paragraph: the Gaussian tools are established source material, the GTW ordinary-tree martingale argument is an antecedent rather than a drop-in biased-measure theorem, and the local one-block elimination does not establish historical novelty.
<!-- /passage:R3-BS-LOG-DEFICIT -->
