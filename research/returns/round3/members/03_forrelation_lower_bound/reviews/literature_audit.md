# Focused primary-source audit for round-three section 03

Audit date: 2 November 2026. This report uses the supplied source bytes and specified public primary versions. It does not certify Lean compilation, claim author confirmation, or claim an exhaustive novelty/erratum search.

## 1. Source-by-source use table

| Source and exact version | Assessed locator | Proper role in the replacement section | What it does not establish for the local argument |
| --- | --- | --- | --- |
| OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, dated 5 October 2026; supplied PDF SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e` | §2.1, printed pp. 3–4, equations (3)–(5), Lemma 2.1(i) | Defines the target normalized Walsh promise with yes threshold `delta=2^(-5k)` and no threshold `delta/2`; asks for `R(P)>floor(m^(1-1/k)/(log_2 m)^2)` for each fixed `k` and sufficiently large powers of four `m`. | Does not supply an independent proof of the Forrelation lower bound; its proof cites Bansal–Sinha. |
| Bansal–Sinha, arXiv:2008.07003v3, 17 November 2020 | Theorem 1.3 and Corollary 1.4, printed p. 4; `main.tex:261–278` | Credit for the published randomized lower-bound theorem for exactly this promise. State its published quantitative order, and distinguish that literature route from the locally reconstructed proof. | Its printed `k^-29` quantitative theorem is not the type of the local fixed-`k` proposition `BansalSinhaLower`. A proof of the endpoint `R>L` is not a formal proof of the published numerical comparison. |
| Same Bansal–Sinha version | §3, Figure 1 and Theorem 3.1, printed p. 16; Theorems 3.2–3.4, p. 17; Corollary 3.5, p. 18; Lemma 4.3, p. 19; §5.4, p. 38 | Antecedent for independent Gaussian-pair chains, conditional sign rounding, transformed Gaussian integration by parts, biased Fourier estimates and promise-mass/amplification assembly. Its multilevel comparison is audited separately. | Their truncation is the Gaussian cdf minus `1/2`; the local algebraic truncation produces a different measure. Their promise-mass theorem cannot be silently applied to the local measure. Their Theorem 3.2 involves levels `k,...,k(k-1)`, not only the local order-`k` derivatives. |
| Girish–Tal–Kewen Wu, arXiv:2103.11604v2, 13 May 2021 | §1.3, ordinary-decision-tree discussion, printed pp. 6–8; Lemma 1.9, p. 8; supplied `PDT.tex:365–421`; CCC 2021 edition: Lemma 9, printed p. 39:8 | Methodological ancestry for contracted coefficient arrays, the martingale along an adaptive root-to-leaf path, reverse induction and a union bound. The replacement proves the bounded-bias specialization explicitly. | Does not state the exact local numerical biased raw-derivative bound. It cannot be cited as if those constants or that measure were already its theorem. The future-good-event issue must be handled by stopping, just as its footnote 2 emphasizes. |
| Sherstov–Storozhenko–Pei Wu, arXiv:2008.10223v4, 29 January 2023 | Supplied PDF p. 35: Corollaries 4.14 and 4.15; latter proof continues p. 36. Corresponding public v4 HTML labels: 4.12 and 4.13. Supplied `quantum-classical-query.tex:2252–2308` | Sharper external Fourier comparison only: an absolute `C>=1` gives level-`j` weight at most `C^j sqrt(binomial(d,j)(1+ln n)^(j-1))`, including trees with leaves in `[-1,1]`. The constant remains an explicit external parameter. | This Fourier theorem is not an existing local Lean proof. Their random-orthogonal rorrelation lower bound is not a direct replacement for the explicit Walsh promise/circuit. No numerical value of `C` is supplied by the cited corollary. |
| Avishay Tal, arXiv:1912.12561v1, 29 December 2019 (FOCS 2020 work) | Supplied text §5.1, Theorem 5.1 and Corollary 5.3; §5.2, Definition 5.5 and Lemma 5.7, printed pp. 13–14 | Historical Fourier-growth and rorrelation context; compare the preceding depth-power estimate when explaining why the SSW binomial factor improves dependence on `k`. | Tal's “good orthogonal matrix” assumption is not satisfied by Walsh matrices in the relevant asymptotic regime; its distribution/moment theorem is not automatically transferable. This source is not needed as a premise of the self-contained elementary route. |

The source versions, theorem numbers, author names and citation roles should be stated once, then kept stable. Kewen Wu (GTW) and Pei Wu (SSW) are distinct authors.

## 2. Exact Bansal–Sinha assembly audit

The supplied Bansal–Sinha archive has SHA-256
`f48a3225662484d12e19bf03412478cf87a388f7c2e33c69a4d7f2078202e015`.
Its physical `main.tex` has SHA-256
`800119f9f12877392a92e34ac380c61a50b2a297cee0a70511058580061f835b`.
The two displays are physically at lines **1180 and 1181**. Line **1184 is the subsequent depth threshold**, not the defective comparison. The supplied v3 PDF, printed p. 38, and public v3 HTML agree on the mathematical expressions. I visually checked a rendering of the supplied PDF p. 38, so this finding does not rely solely on OCR.

Write `alpha=1-1/k`, `L=log(kN)`, and `h=k(k-1)`, and absorb universal constants into `A>0`. The preceding level-`ell` upper-bound term is

\[
T_\ell=(A k^{28}d_1)^{\ell/2}N^{-\alpha\ell/2}L^{(\ell-1)/2},
\qquad k\le\ell\le h.
\]

The next displayed expression replaces the logarithmic exponent by `alpha ell/2`. The missing factor is

\[
L^{(\ell-1)/2-\alpha\ell/2}=L^{(\ell/k-1)/2}.
\]

It is one at `ell=k` and grows without bound at every `ell>k` for fixed `k` as `N` grows. For `k>=3`, choose integer depths asymptotic to `c_0 k^-28 N^alpha/L^alpha`, with fixed `c_0>0`. These depths eventually exceed `h`. Then `T_h` is asymptotic to a positive constant times `L^((k-2)/2)`, while the proposed following finite sum has a bounded limit. Thus the inequality between the two displayed upper-bound sums fails, whatever universal constant is chosen. This does **not** calculate a decision tree's actual distinguishing advantage and does **not** refute the lower-bound theorem.

From those multilevel estimates alone, a sufficient replacement is

\[
d_1\le c_1 k^{-28}\frac{N^{1-1/k}}{L^{1-1/[k(k-1)]}}.
\]

Indeed, substitution bounds each term by
`(Ac_1)^(ell/2) L^((ell/h-1)/2) <= (Ac_1)^(ell/2)` for `L>=1`.
Choosing `Ac_1<=128^-2` makes the sum at most
`128^(1-k)/127 < 32^-k/4`. Error reduction costs order `k/eta^2`, yielding the corresponding weaker logarithmic denominator and `k^-29 eta^2` prefactor, under the promise-mass dimension condition. The even coarser denominator `L` also suffices. Either weaker fixed-`k` estimate still dominates the target `N^alpha/(log_2 N)^2` eventually, because the corrected logarithmic exponent is less than two. This repair is a deduction about the displayed estimates, not an editorial replacement for the stated theorem.

There is a **separate reciprocal typo** in equation (5.31), physical `main.tex:1173`: it subtracts `delta^2/(4N)`. Theorem 3.1 supplies the exceptional uniform mass `4/(N delta^2)`. A safe repaired lower gap is

\[
\mathbb E_{p_1}f-\mathbb E_{p_0}f
\ge 6\delta-2\delta-\frac4{N\delta^2},
\]

using the amplified algorithm's error at most `delta` on promised inputs and `[0,1]` acceptance on other inputs. For example `N>=4/delta^3` makes the last term at most `delta` and gives gap at least `3delta`. This does not introduce an assumption that either hard measure is entirely promise supported.

Recommended editorial wording: “The displayed final comparison in v3 §5.4 loses a positive logarithmic factor at levels above `k`. We retain Bansal and Sinha's theorem and credit, identify this assembly defect precisely, and prove the fixed-parameter endpoint directly below.”

## 3. Local-route distinctions that must survive editing

1. Gaussian-chain structure is inherited, but the measure changes with the truncation. The local proof must establish its own mean, promise mass and uniform endpoint for that same local measure throughout.
2. One-block differentiation and repeated Stein elimination produce raw derivatives of order `k` at biased points. They do **not** imply that only degree-`k` uniform Fourier coefficients of the original tree matter: `partial_S gtilde(mu)=sum_{T superset S} ghat(T) mu_(T\S)`.
3. GTW's ordinary-tree method is the proper martingale credit. Its stopping construction, rather than conditioning on a future event, protects the conditional mean-zero property. The biased coordinates should be explicitly centered and bounded before applying the exponential estimate.
4. The exact sharp local edge product is `Psi(x) phi'(y)<=3/16`. Its improved elementary endpoint, the fixed-parameter `BansalSinhaLower`, and the SSW-dependent endpoint have different signatures. Do not describe their formal status from the older route note alone; source-current receipts determine status of the exact powers-of-four theorem.
5. If comparing the SSW route, a restriction that leaves endpoint coordinates free with probability `1/2` and interior coordinates with probability `3/4` has the same free-probability product `(1/4)(3/4)^(k-2)` on every path. Multiplying its reciprocal by `(3/16)^(k-1)` gives `3/4^(k-1)`. This is a local finite identity; the Fourier theorem with constant `C` remains the external input. No factor `k!` occurs because a path chooses one coordinate in each labelled block.
6. Minor metadata caution: a lower bound for parity decision trees also applies to ordinary bit-query trees, since the latter are a subclass. A note saying the parity result “does not itself give” an ordinary randomized lower bound should instead specify any actual promise/quantitative mismatch. The present proof does not need this reduction.

## 4. Primary web locators and coverage limits

- Bansal–Sinha full v3: <https://arxiv.org/html/2008.07003v3>, §§1.1, 3, 4, 5.4; PDF <https://arxiv.org/pdf/2008.07003v3>. Metadata: <https://ir.cwi.nl/pub/30886> (STOC 2021 pp. 1303–1316, DOI `10.1145/3406325.3451040`).
- GTW v2: <https://arxiv.org/html/2103.11604v2>, §1.3 and Lemma 1.9; <https://arxiv.org/pdf/2103.11604v2>, printed p. 8. Conference version: <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.39>, Lemma 9, printed p. 39:8.
- SSW v4: <https://arxiv.org/html/2008.10223v4>, Corollaries 4.12–4.13 in that conversion; <https://arxiv.org/pdf/2008.10223v4>, Corollaries 4.14–4.15, printed pp. 35–36. Journal metadata verified at <https://epubs.siam.org/doi/full/10.1137/22M1468943>.
- Tal v1: <https://arxiv.org/abs/1912.12561v1>; local supplied extracted text was used for §§5.1–5.2.
- OpenAI original folder: <https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026>. Search located the primary folder and original overview, but direct opening of the folder was restricted; the supplied preprint bytes are the mathematical source actually read.

Targeted searches for the exact Bansal–Sinha title with “erratum” and “correction” found no correction of the §5.4 display. The search also surfaced the separate Aaronson–Ambainis simulation correction; that is not a correction of Bansal–Sinha's lower bound. No exhaustive forward-citation or author-site search was performed. No author was contacted.

The attached Bansal–Sinha full version and SSW PDF were read at the specified mathematical locators, not cover to cover. GTW's standard-tree overview and concentration statements were assessed; parity-tree cleanup proofs were not audited. Tal's good-matrix discussion was assessed only to delimit comparison scope. The local source receipt records this subdivision.
