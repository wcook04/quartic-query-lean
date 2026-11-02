<a id="R3-BS-WEAK-LOG"></a>
<!-- passage:R3-BS-WEAK-LOG -->
# A sufficient fixed-parameter corollary of the inspected Bansal–Sinha ingredients

This is an optional ordinary mathematical derivation for the source audit. It establishes a weaker logarithmic denominator than the statement of Bansal–Sinha Theorem 1.3. It is **conditional on the cited source ingredients below**, whose complete proofs have not all been independently audited in this review. It is not a claim to repair the sharper logarithmic exponent, nor is it needed by the baseline's independent local proof of \(R(P)>L\).

## Imported statements and conventions

Fix an integer \(k\ge2\), put \(\delta=2^{-5k}\) and \(\alpha=1-1/k\), and let \(m\) run through powers of two. The input consists of \(k\) sign blocks of length \(m\). The partial Boolean function equals one when the normalized Forrelation value is at least \(\delta\), and zero when its absolute value is at most \(\delta/2\). The intermediate region is unpromised. Algorithms have a worst-case bound on the depth of their decision trees; acceptance probabilities lie in \([0,1]\) on every input, including unpromised inputs.

Use the **Bansal–Sinha** distributions \(p_0,p_1\), with their Gaussian-CDF truncation. These are not the distribution \(\nu_1\) formed using the algebraic truncation in the baseline's §3.9. We use the following exact imported statements from arXiv:2008.07003v3:

1. **Theorem 3.1**, the input-distribution theorem, gives
   \[
   p_0(\text{promised zero})\ge1-\frac4{m\delta^2},
   \qquad p_1(\text{promised one})\ge6\delta.
   \]
2. **Theorem 3.2** bounds \(|\mathbb E_{p_1}f-\mathbb E_{p_0}f|\) by the sum of biased level weights at \(k\le\ell\le k(k-1)\), with coefficient \(m^{-\alpha\ell/2}(8k)^{14\ell}\).
3. **Corollary 3.5** bounds those weights for an acceptance function of a depth-\(d_1\) randomized tree by \((c_0d_1)^{\ell/2}\log(km)^{(\ell-1)/2}\), uniformly over the biases in \([-1/2,1/2]^{km}\), for an absolute constant \(c_0>0\). Its statement covers \(\ell\le d_1\). Higher levels vanish because every such acceptance function has multilinear degree at most \(d_1\); no additional bound is needed there.

Theorem 3.1 is on printed/PDF p. 16, Theorem 3.2 on p. 17, and Corollary 3.5 on p. 18. The combination of the latter two is the justified expression at `main.tex:1180`; the following line is the separate disputed comparison. Set \(C=8^{28}c_0\) and \(\Lambda=\ln(km)\), absorbing any fixed logarithm-base convention into \(c_0\). The three imported statements are all that is used from the source after this point.

## Corollary

For each fixed \(k\ge2\), there are constants \(c_k>0\) and \(m_k\) such that every bounded-error randomized decision tree computing this partial function, with error at most \(1/3\) on every promised input, has depth
\[
d>c_k\frac{m^{1-1/k}}{\ln(km)}
\qquad(m\ge m_k).
\]
Consequently, on the powers of four used in the baseline, this depth eventually exceeds
\(L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor\).

## Complete deduction from the imported statements

Choose an odd positive integer \(r_k\ge72\ln(1/\delta)\). Repeat the given depth-\(d\) algorithm independently \(r_k\) times and take a majority vote. This produces an acceptance function \(f\) of depth \(d_1\le r_kd\), with error at most \(\delta\) on each promised input. Here is an elementary bound for that amplification. For an error indicator \(B_i\), \(\mathbb EB_i\le1/3\); the centered variable \(B_i-\mathbb EB_i\) lies in \([-1,1]\). The convexity and hyperbolic-cosine argument in baseline §3.11 gives
\(\mathbb E e^{\lambda(B_i-\mathbb EB_i)}\le e^{\lambda^2/2}\). Independence and exponential Markov therefore bound the probability of at least half of the repetitions failing by
\[
\exp(-\lambda r_k/6+r_k\lambda^2/2).
\]
Taking \(\lambda=1/6\) gives \(e^{-r_k/72}\le\delta\). The number of repetitions depends on \(k\), not on \(m\) or the particular input.

Write \(\beta=4/(m\delta^2)\). Since \(0\le f\le1\) everywhere and only the promised parts require an error guarantee,
\[
\mathbb E_{p_1}f\ge p_1(\text{promised one})-\delta\ge5\delta,
\qquad
\mathbb E_{p_0}f\le\delta+p_0(\text{not promised zero})\le\delta+\beta.
\]
Thus
\[
\mathbb E_{p_1}f-\mathbb E_{p_0}f\ge4\delta-\beta.
\]
For \(m\ge4/\delta^3\), the right-hand side is at least \(3\delta\). No assertion that either measure is supported entirely inside the promise has been used. This also avoids relying on the reciprocal-\(\delta\) transcription in the source's equation (5.31).

Theorems 3.2 and Corollary 3.5, in their own biased normalization, give
\[
\begin{aligned}
\left|\mathbb E_{p_1}f-\mathbb E_{p_0}f\right|
&\le\sum_{\ell=k}^{k(k-1)}m^{-\alpha\ell/2}(8k)^{14\ell}
 (c_0d_1)^{\ell/2}\Lambda^{(\ell-1)/2}\\
&=\Lambda^{-1/2}\sum_{\ell=k}^{k(k-1)}
 \left(\frac{Ck^{28}d_1\Lambda}{m^\alpha}\right)^{\ell/2}.
\end{aligned}
\]
This equality retains the actual exponent \((\ell-1)/2\). Set
\[
c_k=\frac1{4Ck^{28}r_k}.
\]
If \(d\le c_km^\alpha/\Lambda\), then
\(Ck^{28}d_1\Lambda/m^\alpha\le1/4\). Summing a geometric series yields
\[
\left|\mathbb E_{p_1}f-\mathbb E_{p_0}f\right|
\le\frac1{\sqrt\Lambda}\sum_{\ell=k}^{\infty}2^{-\ell}
=\frac{2^{1-k}}{\sqrt\Lambda}.
\]
For fixed \(k\), this tends to zero. In particular it is at most \(\delta/4\) once
\(\Lambda\ge(2^{3-k}/\delta)^2\). This contradicts the lower bound \(3\delta\) just obtained. Combining the two explicit size conditions proves the corollary.

Finally, for \(m\ge k\), \(\ln(km)\le2\ln m\), and
\[
\frac{c_km^\alpha/\ln(km)}{m^\alpha/(\log_2m)^2}
\ge\frac{c_k\ln m}{2(\ln2)^2}\longrightarrow\infty.
\]
Hence the lower bound eventually exceeds the unfloored expression defining \(L\), and therefore exceeds \(L\) itself.

The proof gives exactly the fixed-parameter consequence needed here. The explicit threshold may be extremely large as a function of \(k\); this derivation does not authorize substituting an arbitrary growing \(k=k(m)\) or claiming the sharper logarithmic expression from Theorem 1.3. Its literature credit belongs to the cited Bansal–Sinha ingredients; the summation and eventual comparison are supplied explicitly here.
<!-- /passage:R3-BS-WEAK-LOG -->
