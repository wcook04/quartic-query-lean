# Bansal–Sinha arXiv:2008.07003v3, §5.4: independent check of the log exponent

Source: `annexes/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.tar.gz`, extracted to
`/private/tmp/claude-501/bs_src_6860/` (files `main.tex`, 1202 lines; `generalk.tex`, 377 lines).
Comparison: SSW arXiv:2008.10223, extracted to `/private/tmp/claude-501/ssw_src_*/quantum-classical-query.tex`.
The annex has only v3. It contains no erratum or later version.

## 1. Ingredients (as stated in the paper)

**Theorem 1.3 (`thm:lower`, main.tex:261–265).** For k ≥ 2, δ = 2^{-5k}, depth ≥
Ω( k^{-28} (N / log(kN))^{1-1/k} · η² / log(1/δ) ).

**Theorem 4.2 (`thm:level`, main.tex:767–772).** For f: {±1}^{kN} → [0,1],
|E_{p1} f − E_{p0} f| ≤ sup_μ Σ_{ℓ=k}^{k(k-1)} (1/√N)^{ℓ(1−1/k)} (8k)^{14ℓ} wt^μ_ℓ(f).

**Tal's bound (`thm:tal`, main.tex:778–784)** and **Cor. 4.5 (`cor:wt`, main.tex:796–799).** For a depth-d randomized tree on m = kN bits, ℓ ≤ d:
wt^μ_ℓ(f) ≤ ((cd)^ℓ log^{ℓ−1} m)^{1/2}.

The parameter choice and level range: ℓ runs over k, …, k(k−1) (from Lemma `lemma:monomial`, main.tex:995–999, and generalk.tex:236–243, 306–318).

## 2. The display in §5.4 (main.tex:1179–1186)

```
|E_{p1}[f(Z)] - f(0)| <= sup_mu sum_{l=k}^{k(k-1)} (1/sqrt N)^{l(1-1/k)} (8k)^{14l} wt^mu_l(f)          (line 1180)
   <= sum_{l=k}^{k(k-1)} (1/sqrt N)^{l(1-1/k)} (8k)^{14l} sqrt(d_1^l log^{l-1}(kN))                   (line 1182)
   <= sum_{l=k}^{k(k-1)} ( c d_1 k^{28} (log(kN)/N)^{1-1/k} )^{l/2}                                    (line 1184)
```

The proof then concludes (main.tex:1187–1189) that d_1 < C k^{-28} (N/log(kN))^{1-1/k} makes the advantage ≤ δ/4.

The first inequality (1180) is Thm 4.2 and is fine. The second (1182) is Cor. 4.5 and is fine. It drops the c^{ℓ/2} factor, which is absorbed later. The third inequality (1184) is where the problem lies.

## 3. Exponent bookkeeping for the third inequality

Write L = log(kN). The level-ℓ term on line 1182 is

T_ℓ = N^{−ℓ(k−1)/(2k)} · (8k)^{14ℓ} · c^{ℓ/2} · d^{ℓ/2} · L^{(ℓ−1)/2}.

The claimed level-ℓ term on line 1184 is

R_ℓ = c'^{ℓ/2} · k^{14ℓ} · d^{ℓ/2} · L^{ℓ(k−1)/(2k)} · N^{−ℓ(k−1)/(2k)}.

The powers of N and d agree. The constants agree once c' ≥ 8^{28} c. The only discrepancy is the power of L:

- actual exponent: (ℓ − 1)/2
- claimed exponent: ℓ(k − 1)/(2k) = (ℓ − ℓ/k)/2

Actual ≤ claimed ⇔ ℓ − 1 ≤ ℓ − ℓ/k ⇔ ℓ ≤ k.

- ℓ = k: the exponents are equal, (k−1)/2 on both sides. The inequality holds.
- ℓ > k: T_ℓ / R_ℓ = L^{(ℓ/k − 1)/2}, which tends to ∞ with N. **The inequality on line 1184 is false for every level ℓ > k** (for L ≥ 1 large, i.e. all large N). The worst level is ℓ = k(k−1). There the ratio is L^{(k−2)/2}.
- The range ℓ ∈ [k, k(k−1)] contains a level ℓ > k exactly when k(k−1) > k, i.e. **k ≥ 3**. For **k = 2** the sum has the single term ℓ = 2 = k, so the display is valid and Theorem 1.3 follows as stated.

This is a false inequality, not a typo. No re-reading of line 1184 with the same ingredients yields the stated threshold. The next section shows that the conclusion drawn from it also fails at the stated threshold.

## 4. What the argument as written actually gives

Rewrite T_ℓ = L^{−1/2} · x^{ℓ/2} with x := c'' k^{28} d L / N^{1−1/k} (c'' absolute).

**At the paper's threshold** d = C k^{−28} (N/L)^{1−1/k}, we get x = C c'' L^{1/k}. The top level is then
T_{k(k−1)} = L^{−1/2} (C c'')^{k(k−1)/2} L^{(k−1)/2} = Θ_k(L^{(k−2)/2}).
For k ≥ 3 and large N this is unbounded, so the bound is not even below 1. For k = 3, for instance, it is Θ(L^{1/2}). So the conclusion "advantage ≤ δ/4" does not follow from Thm 4.2 + Tal for k ≥ 3.

**Best threshold from Thm 4.2 + Tal as stated.** We need L^{−1/2} x^{ℓ/2} ≤ ε for all ℓ ∈ [k, k(k−1)], with ε ≈ δ/(4k²). If x ≥ 1, the binding level is ℓ = k(k−1), which gives x ≤ (ε² L)^{1/(k(k−1))}. Then

d ≲ k^{−28} · ε^{2/(k(k−1))} · N^{1−1/k} / L^{1 − 1/(k(k−1))},

and ε^{2/(k(k−1))} = 2^{−10/(k−1)}·(4k²)^{−2/(k(k−1))} is bounded below by an absolute constant. So the proof as written supports

**depth ≥ Ω( k^{−28} · N^{1−1/k} / log(kN)^{1 − 1/(k(k−1))} · η²/log(1/δ) )** (the k^{−28} may need a slightly worse absolute constant).

This is weaker than the stated (N/log kN)^{1−1/k} by a factor log(kN)^{(k−2)/(k(k−1))}. That is 1 for k = 2, L^{1/6} for k = 3 and L^{1/6} for k = 4, and it tends to 1/k asymptotically.

The simpler sufficient choice x ≤ 1/4, i.e. d ≲ k^{−28} N^{1−1/k}/L (denominator L¹), also works and makes all levels a geometric series. That is the shape SSW use (see §6).

Qualitative consequences are unaffected. These are Ω̃(N^{1−1/k}), the "matches up to polylog" remark (main.tex:267), the O(1) vs N^{1−ε} and α(N) vs N^{1−o(1)} separations, the cubic total-function corollary and the communication corollaries. Only the explicit log exponent in Theorem 1.3 and Corollary 1.4 (main.tex:275–278, "analogous", main.tex:1189) is unsupported for k ≥ 3.

## 5. Can the finer structure of Lemma 5.1 rescue it?

Lemma `lemma:monomial` gives the decay N^{−ℓ(1−1/k)/2} as a *lower bound* on the exponent T+(k−1) (generalk.tex:318, 332, 340). Some intermediate levels decay faster. In the explicit k = 3 proof (main.tex:1103–1118), levels 4 and 5 carry N^{−2} rather than N^{−4/3} and N^{−5/3}. With Tal and d = (N/L)^{2/3}, those levels give N^{−2/3}L^{1/6} and N^{−1/3}L^{1/3}, both → 0. But the top level ℓ = 6 = k(k−1) carries exactly (1/√N)^4 = N^{−2} = N^{−ℓ(1−1/k)/2} (eq. `eq:term6`, main.tex:1103–1112, with |J| = 6 when all six indices are distinct; θ_J ≤ 8). Its contribution is N^{−2}·d³·L^{5/2} = L^{1/2} at the stated threshold. So for k = 3 the extra decay of the explicit computation does not rescue the stated exponent. The obstruction is the top level, not a loose count at intermediate levels. For general k I did not verify whether every top-level configuration has T+(k−1) = (k−1)², but generalk.tex:306–318 forces ℓ_m = 0 at |J| = k(k−1) and gives T+(k−1) ≥ (k−1)². Nothing in the paper claims more.

## 6. Repair by the other growth bounds named

- **Tal's bound** (the one already used) has log^{ℓ−1}. The deficit is exactly this log power at ℓ > k, so it gives no repair.
- **Sherstov–Storozhenko–Wu** (Tal's conjecture, proved; SSW tex:520–531, 2256): wt_ℓ ≤ C^ℓ √(binom(d,ℓ)(1+ln n)^{ℓ−1}). The log power is again ℓ−1. The √(ℓ!) saving only improves k-dependence, since ℓ ≤ k² is fixed as N → ∞, so it gives no repair of the log exponent.
- **Trivial bound** wt_ℓ ≤ binom(d,ℓ) has no log but costs d^{ℓ/2} more. At d ≈ N^{1−1/k} the level-ℓ term becomes ≈ N^{ℓ(1−1/k)/2}, which is useless. No mix of these fixes the top level.
- **Parameter choice.** The only free parameter in §5.4 is d. §4 shows that the optimal d with these ingredients gives L^{1−1/(k(k−1))}. No other choice gives better.

So **no simple local repair restores the stated log(kN)^{1−1/k}** for k ≥ 3. Restoring it would need a level-ℓ bound with log exponent ≤ ℓ(1−1/k) for ℓ > k (for example a log-free bound at high levels, which is open as far as the paper's citations go), or a sharper Thm 4.2 decay at the top level.

**SSW's own analogous step is done correctly.** At SSW tex:2529–2535 they bound (1+ln nk)^{(ℓ−1)/ℓ} ≤ (1+ln nk), take one full log per unit of d, and conclude with denominator log^{2−1/k}. Their extra log^{1−1/k} comes from their Gaussian coefficient bound (ℓ log n / n)^{…}. Applied to Bansal–Sinha, whose coefficient bound has no log, the same handling gives denominator L¹, consistent with §4. SSW tex:796 restate the Bansal–Sinha bound without comment, so they offer no independent confirmation of it.

## 7. Verdict, conservatively labelled

- Lines 1180 and 1182: valid.
- Line 1184, third inequality: **false as displayed for every ℓ > k, hence for every k ≥ 3** (true for k = 2). It is not a typo with a correct intended version, because the conclusion fails at the stated threshold (top-level term Θ_k(L^{(k−2)/2})).
- The argument as written proves Ω(k^{−28} N^{1−1/k} log(kN)^{−(1−1/(k(k−1)))} η²/log(1/δ)), and the cruder but clean Ω(k^{−28} N^{1−1/k}/log(kN) · …).
- Theorem 1.3's exact log exponent is **unsupported, not refuted**, for k ≥ 3. I found no argument showing the stated bound is false.
- Not verified: whether a sharper accounting in generalk.tex could improve the top-level decay for k ≥ 4. For k = 3 it cannot (explicit level-6 term).
