**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Bansal–Sinha §5.4: verification and a replacement proof

<!-- passage:bs-verdict -->
The final Fourier-weight inequality in §5.4 of Bansal and Sinha, arXiv:2008.07003v3, has an incorrect logarithmic exponent when $k\ge3$. The single-block interpolation described in the accompanying note supplies a replacement argument: combined with the Fourier theorem of Sherstov, Storozhenko and Wu, it proves the stated logarithmic exponent, with stronger dependence on $k$, in an explicit range of block sizes. Thus the failed displayed inequality does not give a counterexample to the theorem. The replacement argument below proves a large-dimension theorem and does not establish a literal all-$(k,N)$ version outside its stated range.

All computations in this document are mathematical derivations from the attached sources. No new Lean compilation, Comparator check, human review or author confirmation is claimed.
<!-- /passage:bs-verdict -->

## 1. Exact source and locators

<!-- passage:bs-source -->
The principal source is the attached archive
`literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.tar.gz`.
The archive contains `main.tex` and `generalk.tex`. The decisive displayed inequality is at `main.tex:1184`, inside §5.4, on numbered PDF page 38. The public [v3 PDF](https://arxiv.org/pdf/2008.07003v3) and [v3 HTML](https://arxiv.org/html/2008.07003v3) reproduce it.

The supplied second-reading document gets the section numbers of several ingredients wrong. In v3 the correct references are:

| Ingredient | Correct reference | TeX locator |
|---|---|---|
| Randomized lower bound to be proved | Theorem 1.3 | `main.tex:261–265`, label `thm:lower` |
| Constant-error corollary | Corollary 1.4 | `main.tex:275–278`, label `cor:smallerr` |
| Promise mass of the two distributions | Theorem 3.1 | `main.tex:725–729`, label `thm:input` |
| Comparison using biased Fourier levels | Theorem 3.2 | `main.tex:767–772`, label `thm:level` |
| Tal's uniform Fourier estimate | Theorem 3.3 | `main.tex:778–784`, label `thm:tal` |
| Transfer to biased Fourier weight | Theorem 3.4 | `main.tex:790–795`, label `thm:fwt` |
| Biased Fourier estimate for trees | Corollary 3.5 | `main.tex:796–799`, label `cor:wt` |
| Final assembly | §5.4 | `main.tex:1166–1189` |

The version history on [arXiv](https://arxiv.org/abs/2008.07003) lists v3, dated 17 November 2020, as its latest revision at the time of this check. The [ECCC record TR20-127](https://eccc.weizmann.ac.il/report/2020/127/) likewise lists a final revision from 17 November 2020. Targeted searches for the title with “erratum” or “correction” did not locate an author correction to the §5.4 display. That is a bounded search result. It does not establish that no correction exists.

The [published STOC 2021 version](https://ir.cwi.nl/pub/30886/30886.pdf), pages 1303–1316, was also checked. Its Theorem 1.3 on page 1304 states the same $k^{-29}[N/\log(kN)]^{1-1/k}\eta^2$ lower-bound order. Its proof section ends with the explicit $k=3$ calculation on page 1316 and refers omitted arguments to the full version. It has no §5.4 and does not reproduce the defective final display or provide a replacement for that step. This report identifies a defect in the full v3 proof, with the same theorem statement present in the conference version.
<!-- /passage:bs-source -->

## 2. What goes wrong in the logarithm

<!-- passage:bs-levels -->
Use $N$ for the size of each input block, so the total input has $kN$ bits. Set

\[
 \alpha=1-\frac1k,\qquad L=\log(kN),\qquad h=k(k-1).
 \tag{B1}
\]

The logarithm base changes only absolute constants. Below take $L\ge1$. Theorems 3.2 and 3.3 and Corollary 3.5 imply an upper bound on the acceptance-probability difference whose level-$\ell$ term is

\[
 T_\ell=
 (A k^{28}d_1)^{\ell/2}
 N^{-\alpha\ell/2} L^{(\ell-1)/2},
 \qquad k\le\ell\le h,
 \tag{B2}
\]

where $A>0$ is an absolute constant and $d_1$ is the amplified query depth. The factor $A$ absorbs the factor $8^{28}$ and the absolute constant in the Fourier estimate. Fourier levels above the tree depth vanish; extending their upper bounds to the whole displayed range is harmless.

Line 1184 replaces the logarithmic factor by $L^{\alpha\ell/2}$. Their quotient, after matching the other factors, is

\[
 L^{(\ell-1)/2-\alpha\ell/2}
   =L^{(\ell/k-1)/2}.
 \tag{B3}
\]

It equals one at $\ell=k$. For every $\ell>k$, it tends to infinity with $N$, with $k$ fixed. No absolute constant absorbs it. The interval from $k$ to $h$ includes such a level exactly when $k\ge3$.
<!-- /passage:bs-levels -->

<!-- passage:bs-sum-counterexample -->
The defect also invalidates the inequality between the displayed sums; it is not merely a failed termwise justification. Fix $k\ge3$ and a positive constant $c_0$, and take integer depths asymptotic to

\[
 d_1=c_0 k^{-28}N^{\alpha}L^{-\alpha}.
 \tag{B4}
\]

Such depths eventually exceed $h$. The last term of the actual upper-bound sum satisfies

\[
 T_h\sim (Ac_0)^{h/2}L^{(k-2)/2}.
 \tag{B5}
\]

For every fixed positive $c_0$, this diverges. Each term in the proposed right-hand sum has a finite limit depending on $k$, $c_0$, and its absolute constant. That sum is bounded as $N\to\infty$. Therefore the displayed comparison fails along these depths, whatever universal constant is chosen.

This counterexample concerns two upper-bound expressions. It says nothing by itself about the actual distinguishing advantage, which is at most one, and nothing by itself about the truth of Theorem 1.3.
<!-- /passage:bs-sum-counterexample -->

## 3. What follows from the original multi-level estimates

<!-- passage:bs-corrected-threshold -->
Keeping the original estimates, a valid sufficient depth restriction is

\[
 d_1\le c_1 k^{-28}
  \frac{N^{1-1/k}}{L^{1-1/[k(k-1)]}},
 \tag{B6}
\]

for a suitably small absolute $c_1>0$. To prove this, substitute (B6) into (B2):

\[
 T_\ell\le (Ac_1)^{\ell/2}
     L^{(\ell/h-1)/2}
  \le (Ac_1)^{\ell/2}
  \qquad(k\le\ell\le h).
 \tag{B7}
\]

Choose $Ac_1\le128^{-2}$. The sum is bounded by

\[
 \sum_{\ell=k}^{h}T_\ell
 \le\sum_{\ell=k}^{\infty}128^{-\ell}
 =\frac{128^{1-k}}{127}
 <\frac{32^{-k}}4.
 \tag{B8}
\]

The final strict inequality holds for every $k\ge2$. Thus, once the promise gap has been established, the original error-reduction cost $O(\eta^{-2}\log(1/\delta))$, with $\delta=32^{-k}$, gives

\[
 R_{(1-\eta)/2}(P_{k,N})
 =\Omega\!\left(
  \frac{\eta^2}{k^{29}}
  \frac{N^{1-1/k}}{
   [\log(kN)]^{1-1/[k(k-1)]}}
  \right).
 \tag{B9}
\]

This deduction uses absolute constants uniformly in $k\ge2$, subject to the dimension condition needed for the promise gap. The denominator can also be weakened to one full power of $\log(kN)$, giving an immediate geometric-series proof.

Within the information in (B2), the power $1-1/h$ is the strongest possible uniform logarithmic exponent: if $d_1$ is proportional to $N^{\alpha}/L^\beta$, the highest term contains $L^{[h(1-\beta)-1]/2}$, which diverges whenever $\beta<1-1/h$. This is an obstruction to this collection of upper bounds. It is not a lower-bound optimality theorem for Forrelation itself.
<!-- /passage:bs-corrected-threshold -->

<!-- passage:bs-local-repairs -->
Replacing Tal's bound by the sharper Sherstov–Storozhenko–Wu bound while keeping Theorem 3.2 does not remove this obstruction. The improved estimate has a factor $\sqrt{\binom{d_1}{\ell}}$, giving savings of order $1/\sqrt{\ell!}$ in its dependence on the Fourier level. For fixed $k$ and $\ell\le k(k-1)$, that is a constant as $N\to\infty$. Its logarithmic exponent is still $(\ell-1)/2$.

In the original proof's explicit $k=3$ calculation, equation `eq:term6`, `main.tex:1103–1118`, includes a level-six term with coefficient $N^{-2}$. At the proposed depth $d_1\asymp N^{2/3}L^{-2/3}$, its quoted Fourier upper bound is of order $L^{1/2}$. The improved decay of some intermediate levels therefore cannot fix the highest level in that calculation.

To recover the claimed exponent through the same multi-level inequality would require additional information that specifically improves the high-level terms, such as stronger coefficient cancellation or a specialized derivative-weight estimate. The generic bounds stated in that paper and in SSW do not supply that information.
<!-- /passage:bs-local-repairs -->

## 4. A separate reciprocal error in the promise gap

<!-- passage:bs-promise-typo -->
Equation (5.31), `main.tex:1173`, subtracts $\delta^2/(4N)$ for the exceptional probability under the uniform distribution. Theorem 3.1 proves the different bound $4/(N\delta^2)$. The correctly justified comparison, using error at most $\delta$, is

\[
 \mathbb E_{p_1}f-\mathbb E_{p_0}f
 \ge6\delta-\frac4{N\delta^2}-2\delta.
 \tag{B10}
\]

For example, $N\ge4\delta^{-3}$ makes the right side at least $3\delta$. This repairs the promise-gap step in a stated dimension range. The reciprocal correction leaves the logarithmic failure in §2 unchanged. The second-reading document should distinguish these two issues and replace its Theorem 4.1 reference by Theorem 3.1.
<!-- /passage:bs-promise-typo -->

## 5. Replacement proof using the single-block interpolation

<!-- passage:bs-replacement-ingredients -->
For clarity this section restates the precise ingredients needed from the accompanying note. Set $m=N$, $n=km$, and $\delta=32^{-k}$. The Walsh Forrelation promise is positive when $\Phi\ge\delta$, zero when $|\Phi|\le\delta/2$, and undefined elsewhere.

The single-block interpolation uses

\[
 \Psi(x)=\frac1{2\sqrt{2+x^2}},\qquad
 \varphi(x)=\frac{x(3+x^2)}{2(2+x^2)^{3/2}},\qquad
 \varphi'(x)=\frac3{(2+x^2)^{5/2}}.
 \tag{B11}
\]

The equality $\varphi=x\Psi-\Psi'$ yields Gaussian integration by parts. Its edge coefficient satisfies $0\le\Psi(x)\varphi'(y)\le3/16$. Biases in the first and last blocks have magnitude at most $1/2$, and those in intermediate blocks have magnitude at most $1/4$.

Only the first bias block is scaled by $s\in[0,1]$. On differentiating in $s$, successive integration by parts moves one derivative through each of the $k$ blocks. The term that differentiates the same cube coordinate twice vanishes by multiaffinity. Earlier kernel weights depend only on earlier Gaussian layers. Consequently the advantage involves raw derivatives on path sets $S_p$, each containing one coordinate from each block, and obeys

\[
 |\mathbb E_{\mathcal D}T-\mathbb E_{\mathcal U}T|
 \le\left(\frac3{16\sqrt m}\right)^{k-1}
   \sup_{s,U}\sum_p|\partial_{S_p}\widetilde T(w_s)|.
 \tag{B12}
\]

The orthogonality of the Walsh matrix makes the zero interpolation endpoint uniform. Applying the same identity to $\Phi$, followed by Jensen's inequality, gives

\[
 \mathbb E_{\mathcal D}\Phi\ge a:=18^{-(k-1)},
 \qquad \mathbb E_{\mathcal U}\Phi^2=\frac1m.
 \tag{B13}
\]

These ingredients use a different smooth truncation and interpolation from Bansal–Sinha. Their construction of correlated Gaussian layers and products in intermediate blocks remains an antecedent; the replacement proof does not invoke their invalid displayed inequality.
<!-- /passage:bs-replacement-ingredients -->

<!-- passage:bs-replacement-sharp-growth -->
Let $C\ge1$ be an absolute constant from SSW, Corollary 4.14, in its natural-log form:

\[
 \sum_{|S|=j}|\widehat T(S)|
 \le C^j\sqrt{\binom d j}\,(1+\ln n)^{(j-1)/2}.
 \tag{B14}
\]

A coordinatewise restriction leaves endpoint coordinates free with probability $1/2$, and intermediate coordinates free with probability $3/4$. The expected Fourier coefficient of a restricted function at $S$ is the raw derivative at the bias, multiplied by the product of the free probabilities in $S$. For a path set the product is $(1/4)(3/4)^{k-2}$. Restrictions preserve decision-tree depth. Combining this identity, the triangle inequality, (B12), and (B14) gives, for a depth-$d$ tree,

\[
 |\mathbb E_{\mathcal D}T-\mathbb E_{\mathcal U}T|
 \le\frac{3C^k}{4^{k-1}}\sqrt{\binom d k}
    \left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
 \tag{B15}
\]

The coefficient calculation is exact:

\[
 (3/16)^{k-1}\,4(4/3)^{k-2}=3/4^{k-1}.
 \tag{B16}
\]

The bound extends to a randomized tree by averaging over its random coins. This is where using only level $k$ changes the logarithmic bookkeeping: the factor $(1+\ln(km))^{(k-1)/2}$ is exactly the factor whose $2/k$-power becomes a denominator of exponent $1-1/k$.
<!-- /passage:bs-replacement-sharp-growth -->

<!-- passage:bs-replacement-finite -->
Suppose the original algorithm has depth $D$ and success at least $(1+\eta)/2$, for $0<\eta\le1$. Repeat it independently $2\tau$ times. Counting a tie as an error gives an amplified error bound

\[
 \varepsilon\le(1-\eta^2)^\tau\le e^{-\tau\eta^2}.
 \tag{B17}
\]

Define

\[
 p=\frac{a-\delta}{1-\delta},\qquad
 q=\min\{1,4/(m\delta^2)\},\qquad
 \Gamma=(1-\varepsilon)p-\varepsilon-q.
 \tag{B18}
\]

Here $p$ is a lower bound for the positive-promise mass under $\mathcal D$, and $q$ is an upper bound for the complement of the zero promise under $\mathcal U$. Thus the amplified acceptance difference is at least $\Gamma$. Substituting $d=2\tau D$ into (B15) yields the finite implication

\[
 \Gamma\le\frac{3C^k}{4^{k-1}}
   \sqrt{\binom{2\tau D}{k}}
   \left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
 \tag{B19}
\]

When $\Gamma>0$, the binomial coefficient is nonzero. Using
$\binom{2\tau D}k\le(2e\tau D/k)^k$ gives

\[
 D\ge\frac{k}{2e\tau C^2}
   \left(\frac{\Gamma4^{k-1}}3\right)^{2/k}
   \left(\frac m{1+\ln(km)}\right)^{1-1/k}.
 \tag{B20}
\]

The upper bound $q$ in (B18) can be replaced by any valid upper bound for the same exceptional mass. This finite inequality records exactly what the proof needs at smaller $m$.
<!-- /passage:bs-replacement-finite -->

<!-- passage:bs-replacement-endpoint -->
Take

\[
 \tau=\left\lceil\frac{5k\ln2}{\eta^2}\right\rceil,
 \qquad m\ge 2^{15k+2}.
 \tag{B21}
\]

Then $\varepsilon\le\delta$, $q\le\delta$, and
$\tau<(4k)/\eta^2$. Since
$\delta/a=18^{k-1}/32^k\le1/32$,

\[
 \Gamma\ge a-3\delta\ge\frac{29a}{32},\qquad
 \left(\frac{\Gamma4^{k-1}}3\right)^{2/k}
 \ge\frac4{81}\left(\frac{87}{64}\right)^{2/k}
 \ge\frac4{81}.
 \tag{B22}
\]

Substitution into (B20) proves

\[
 \boxed{\displaystyle
 R_{(1-\eta)/2}(P_{k,m})\ge
 \frac{\eta^2}{162eC^2}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.}
 \tag{B23}
\]

This restores the logarithmic exponent of Bansal–Sinha Theorem 1.3 for every fixed $k\ge2$ and all sufficiently large powers-of-two block sizes. It is also uniform over the explicitly stated joint range. As $k^{-29}\le1$, it implies their asserted lower-bound order in that range, with stronger $k$-dependence. The supplied Lean model currently restricts $m$ to powers of four, and the sharp SSW estimate and the new quantitative assembly remain formalization obligations.
<!-- /passage:bs-replacement-endpoint -->

## 6. A smaller sufficient dimension threshold

<!-- passage:bs-null-tail -->
The condition $m\ge2^{15k+2}$ is an artifact of using only the second moment to make $q\le\delta$. Under the uniform law there is a direct subgaussian estimate. Fix the intermediate sign blocks and the final sign block $y$. The Forrelation polynomial has the form

\[
 \Phi=m^{-1}x^{\mathsf T}Ay,
 \qquad A\text{ orthogonal},\qquad \|Ay\|_2^2=m,
 \tag{B24}
\]

where the coordinates of $x$ are still independent uniform signs. Writing $v=Ay$, independence and $\cosh u\le e^{u^2/2}$ give

\[
 \mathbb E_x e^{\lambda\Phi}
  =\prod_i\cosh(\lambda v_i/m)
  \le\exp\!\left(\frac{\lambda^2}{2m}\right).
 \tag{B25}
\]

The bound is uniform in the conditioned variables. For $u>0$, exponential Markov and the choice $\lambda=mu$, applied to each sign, imply

\[
 \Pr_{\mathcal U}(|\Phi|>u)
 \le2e^{-mu^2/2};\qquad
 \Pr_{\mathcal U}(|\Phi|>\delta/2)
 \le2e^{-m\delta^2/8}.
 \tag{B26}
\]

This proof is valid for every real orthogonal matrix in the Forrelation expression; it uses no random-matrix theorem. It is a new paper lemma in the present return and has no claimed compiled counterpart.
<!-- /passage:bs-null-tail -->

<!-- passage:bs-smaller-range -->
Consequently the original proof of (B23) works under $m\ge8\delta^{-2}\ln(2/\delta)$. Using the stronger hard mean $a$ allows an even smaller sufficient threshold, while retaining the same final constant:

\[
 m\ge8\delta^{-2}\ln(8/a).
 \tag{B27}
\]

A convenient sufficient condition avoiding a logarithm in the size hypothesis is

\[
 \boxed{m\ge24k\,2^{10k}.}
 \tag{B28}
\]

Indeed, $\ln(8/a)=\ln8+(k-1)\ln18<3k$, so (B28) implies (B27). The inequality $e^3>18$ follows already from the Taylor sum through degree five, which equals $92/5$. Thus $q\le a/4$. With the same amplification as in (B21),

\[
 \Gamma\ge a-2\delta-q\ge\frac{11a}{16},\qquad
 \left(\frac{\Gamma4^{k-1}}3\right)^{2/k}
 \ge\frac4{81}\left(\frac{33}{32}\right)^{2/k}
 \ge\frac4{81}.
 \tag{B30}
\]

Substituting in (B20) gives exactly the constant in (B23). The elementary $2/18225$ conclusion also survives this size reduction: with its error bound $\varepsilon\le a/18$, the gap is at least $(31/32-1/9-1/4)a=175a/288$. With the source-compatible padded depth $d=50kL+1$ retained in the main note, its upper bound is $7a/12=168a/288$, leaving slack $7a/288>0$. Without the extra padding the stronger upper bound $59a/108$ is also valid, but it is not needed for the stated constant.

The sharp endpoint is therefore proved here in a larger joint parameter range. A positive lower bound cannot hold literally for every power-of-two $m$: at $m=2$, $k=2$, the Walsh transform sends each sign vector to a vector with one coordinate $\pm\sqrt2$ and the other zero. Hence $\Phi$ always equals $\pm1/\sqrt2$. At threshold $\delta=32^{-2}$, the zero promise is empty; the partial function is constant one on its domain, and zero queries suffice. The case $m=1$ is similarly degenerate. These examples do not refute an asymptotic theorem for fixed $k$ and sufficiently large $m$.

Extending the proof beyond (B28) for nondegenerate promises remains a separate question. When the displayed upper bound for the uniform exceptional mass is comparable to one, (B18) gives no positive gap, even after reducing $\varepsilon$ to zero. Neither amplification nor the SSW Fourier estimate repairs that particular loss of information.
<!-- /passage:bs-smaller-range -->

## 7. Comparison with the published results

<!-- passage:bs-comparison -->
All appearances of $m$ in this table denote block size. Constants in $\Omega(\cdot)$ are absolute where stated by the source.

| Argument | Matrix and promise | Result or comparison |
|---|---|---|
| Bansal–Sinha, Theorem 1.3 as stated | Walsh; positive threshold $32^{-k}$, zero threshold half that | $\Omega(\eta^2 k^{-29}[m/\log(km)]^{1-1/k})$. Its §5.4 derivation has the defect shown above. |
| Original Bansal–Sinha multi-level estimates, with corrected logarithms | Same promise | Formula (B9), with denominator exponent $1-1/[k(k-1)]$, and the promise-gap dimension condition. |
| Single-block identity with Tal's Fourier bound | Walsh; same threshold $32^{-k}$ | $\Omega(\eta^2 k^{-1}[m/(1+\ln(km))]^{1-1/k})$ in the same large-dimension range. Its Fourier bound lacks the factorial saving that cancels amplification cost. |
| Single-block identity with SSW, Corollary 4.14 | Walsh; same threshold $32^{-k}$ | Formula (B23), uniformly for $m\ge24k2^{10k}$ after (B26). There is no explicit inverse power of $k$ when expressed using block size. |
| SSW's own query lower bound, Theorem 1.1 | Random orthogonal matrix, with high probability; positive threshold $2^{-k}$, zero threshold $2^{-k-1}$ | $\Omega(\eta^2 m^{1-1/k}/[k(\log m)^{2-1/k}])$, using their advantage parameter $\gamma=\eta/2$, for $k\le\frac13\log_2m-1$. |
| Tal's original Rorrelation lower bound | Random orthogonal matrix; threshold $2^{-k}$ | Constant-error lower bound $\Omega(m^{2(k-1)/(3k-1)}/[k\log m])$; see the main result and §5.4. |

The last two rows concern a different threshold and a random orthogonal matrix. The general Fourier theorem of SSW applies to decision trees independently of their Rorrelation application, which is why it can be used for Walsh Forrelation in (B15). The table does not identify their promise problems for growing $k$.

Writing total input length as $n=km$, the new endpoint is

\[
 \frac{\eta^2}{162eC^2}
 \left(\frac{n}{k(1+\ln n)}\right)^{1-1/k}.
 \tag{B29}
\]

Thus “no inverse polynomial in $k$” must always specify the block-size normalization. This argument gives logarithmic denominator exponent $1-1/k$ using the published sharp Fourier estimate. It does not prove that this logarithmic loss is necessary for this specific promise problem.
<!-- /passage:bs-comparison -->

## 8. Source-read receipt and remaining boundary

<!-- passage:bs-receipt -->
Read completely for this sub-review: the job instructions and build-status table; the repository README and evidence contract; corpus README; the supplied second-reading report; and the first-round Forrelation `note.md`. Inspected the complete relevant source sections of Bansal–Sinha (`main.tex` §1.1, §3, §5.2's explicit three-block calculation, §5.3, §5.4), and the SSW theorem statements and proof sections supplying the Fourier bound and the Rorrelation comparison. Inspected the relevant sections of Tal's supplied PDF extraction and the declared single-block walk, cascade, and promise interfaces in the attached Lean source. The sub-review did not re-prove the entire branching-process analysis in `generalk.tex`, and no claim here requires a new correctness verdict on that proof.

Public sources checked on 2 November 2026: Bansal–Sinha arXiv abstract, v3 HTML and PDF, ECCC version record, and the 14-page final STOC PDF held by CWI; SSW arXiv/publisher records and author-hosted PDF; Tal arXiv record. The attached Tal literature directory has no TeX archive, so its readable extraction was used for this comparison. The original Bansal–Sinha and SSW TeX archives were available. No mathematical source needed for the decisive exponent calculation or the replacement argument was unavailable.

The strongest claimed endpoint in this report is a complete paper proof conditional only on the explicitly cited SSW Fourier theorem. Its Lean realization, including the coordinate-dependent restriction identity, the variable-error interface, the sharper coefficient bound, and the optional subgaussian null tail, remains to be checked by the pinned compiler. The previous fixed-$k$ Lean theorem does not by itself certify these stronger statements.
<!-- /passage:bs-receipt -->

## References

- N. Bansal and M. Sinha, *$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity*, arXiv:2008.07003v3, 2020; STOC 2021. [Versioned paper](https://arxiv.org/abs/2008.07003v3). Exact mathematical locators appear in §1 above.
- A. A. Sherstov, A. A. Storozhenko and P. Wu, *An Optimal Separation of Randomized and Quantum Query Complexity*, SIAM Journal on Computing 52(2), 525–567, 2023. [DOI](https://doi.org/10.1137/22M1468943), [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4). Corollary 4.14 is the natural-log Fourier bound; Theorem 1.1 and §5 give the Rorrelation comparison. In the supplied TeX use `quantum-classical-query.tex:2250–2273` and `:2480–2653`.
- A. Tal, *Towards Optimal Separations between Quantum and Randomized Query Complexities*, arXiv:1912.12561, 2019; FOCS 2020. [Paper](https://arxiv.org/abs/1912.12561). Theorem 5.1 supplies the earlier Fourier estimate; the main result and §5.4 give the Rorrelation lower bound.
- X. Wu, *Analyzing XOR-Forrelation through Stochastic Calculus*, arXiv:2109.02732, 2021. [Paper](https://arxiv.org/abs/2109.02732). Lemma 2.2 is the constant-free-probability restriction identity generalized in the accompanying note.
