# A finite check of the spectral-adversary coefficient

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

<!-- passage:coefficient-finding -->
**Finding.** The error-dependent coefficient printed in Špalek–Szegedy's 2006 Theorem 3.1 is incompatible with its stated oracle and spectral-norm conventions. Two-bit parity supplies a complete finite witness. The standard coefficient with an additional factor \(1/2\) is consistent with the witness and is stated explicitly by Høyer, Lee and Špalek. This check concerns that coefficient; it gives no reason to reject the equivalences among adversary formulations, or the asymptotic Appendix A bound. No novelty or author-confirmed erratum is claimed.

## Source and convention checks

<!-- passage:coefficient-source-conventions -->
The [publisher PDF of Špalek–Szegedy](https://theoryofcomputing.org/articles/v002a001/v002a001.pdf), DOI [10.4086/toc.2006.v002a001](https://doi.org/10.4086/toc.2006.v002a001), was checked at these locations:

| Locator | Relevant convention |
| --- | --- |
| §2.1, printed p. 4 | A query sends \(\lvert i,b,z\rangle\) to \(\lvert i,b+x_i\bmod \lvert G\rvert,z\rangle\). An algorithm has \(T\) ordinary oracle calls and arbitrary input-independent unitaries. |
| §2.4, printed p. 5 | \(\lambda(A)\) is the Euclidean operator norm. |
| Theorem 3.1 and equation (3.1), printed p. 6 | The display is \(Q_\epsilon(f)/(1-2\sqrt{\epsilon(1-\epsilon)})\ge SA(f)\), with \(SA(f)=\max_\Gamma\lVert\Gamma\rVert/\max_i\lVert\Gamma\circ D_i\rVert\). The theorem supplies no explicit error-range restriction. |
| Footnote 1, printed p. 6 | This concerns the weighted formulation, not the spectral normalization or query cost. |
| Proof of Theorem 3.1, printed p. 14 | The same coefficient appears again. |

The rendered theorem was inspected, so the missing factor is not an extraction inference. The supplied annex note's additional outer square root is a **separate transcription error**. Neither an altered norm nor a doubled query cost occurs in the checked conventions.

## One ordinary bit-oracle call computes two-bit parity exactly

<!-- passage:coefficient-one-query-witness -->
Let \(f(x_0,x_1)=x_0\mathbin{\oplus}x_1\). Use a two-dimensional query-index register and an answer qubit, with a one-dimensional unused workspace. Prepare the input-independent unit vector

\[
 \lvert\psi\rangle
 =\frac{\lvert0\rangle+\lvert1\rangle}{\sqrt2}
   \otimes\frac{\lvert0\rangle-\lvert1\rangle}{\sqrt2}.
\]

The ordinary bit oracle flips the answer qubit when \(x_i=1\). Since the answer factor is the minus eigenvector of that flip, one call gives

\[
 O_x\lvert\psi\rangle
 =\frac{(-1)^{x_0}\lvert0\rangle+(-1)^{x_1}\lvert1\rangle}{\sqrt2}
     \otimes\lvert-\rangle.
\]

Apply the Hadamard gate to the index register. Its resulting index is \(x_0\oplus x_1\) with probability one, up to the global phase \((-1)^{x_0}\). Measuring that register is therefore an exact one-query algorithm in §2.1's model. The initial preparation is absorbed into \(U_0\), and the final Hadamard into \(U_1\). Thus \(Q_\epsilon(f)\le1\) for every nonnegative allowed error. Only this upper bound is needed for the discrepancy.

## A feasible matrix with spectral ratio two

<!-- passage:coefficient-matrix-witness -->
Order the inputs as \(00,01,10,11\) and choose the square's adjacency matrix:

\[
 \Gamma=\begin{pmatrix}
 0&1&1&0\\1&0&0&1\\1&0&0&1\\0&1&1&0
 \end{pmatrix}.
\]

It is symmetric, nonnegative, and every nonzero entry joins opposite parity outputs. Its orthonormal character vectors are one half of

\[
 (1,1,1,1),\quad(1,1,-1,-1),\quad
 (1,-1,1,-1),\quad(1,-1,-1,1),
\]

with eigenvalues \(2,0,0,-2\). Hence \(\|\Gamma\|=2\). The coordinate masks are

\[
 \Gamma_0=\begin{pmatrix}
 0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0
 \end{pmatrix},\qquad
 \Gamma_1=\begin{pmatrix}
 0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0
 \end{pmatrix}.
\]

Both are permutation matrices and have Euclidean norm one. This feasible matrix gives \(SA(f)\ge2\).

<!-- passage:coefficient-positive-error-contradiction -->
At error zero, the printed coefficient would imply \(Q_0(f)\ge2\), contrary to the explicit algorithm. To avoid relying on inclusion of the endpoint, take \(\epsilon=1/100\). The same algorithm has error at most \(1/100\), whereas the printed coefficient would require

\[
 Q_{1/100}(f)\ge2\left(1-2\sqrt{\frac{99}{10000}}\right)
 =2-\frac{\sqrt{99}}{25}>1.
\]

The final strict inequality follows from \(99<625\), so no decimal approximation is involved. This positive error lies in the usual range \(0<\epsilon<1/2\).

## The coefficient supported by the progress argument

<!-- passage:coefficient-supported-bound -->
With the ordinary bit oracle, the standard argument gives

\[
 Q_\epsilon(f)\ge
 \frac{1-2\sqrt{\epsilon(1-\epsilon)}}{2}
 \frac{\|\Gamma\|}{\max_i\|\Gamma_i\|}
 \qquad(0\le\epsilon<1/2).
\]

The factor two arises from the maximum change in an overlap in one oracle call. It is attained by the present example: with Perron vector \(v=(1,1,1,1)/2\), the complex progress sum begins at \(W_0=2\) and ends at \(W_1=0\), while the maximum coordinate-mask norm is one. A claim \(|W_1-W_0|\le\max_i\|\Gamma_i\|\) would fail here.

<!-- passage:coefficient-primary-corroboration -->
For primary corroboration, [Høyer, Lee and Špalek, *Negative weights make adversaries stronger*, author PDF](https://www.ucw.cz/~robert/papers/madv.pdf), printed p. 3, Definition 1 and Theorem 1, states exactly the coefficient with denominator two for the same nonnegative symmetric spectral ratio, attributing it to Barnum–Saks–Szegedy. The displayed theorem was inspected visually. This corroborates the coefficient without claiming that the BSS original full text was independently checked.

The [primary arXiv record](https://arxiv.org/abs/quant-ph/0611054) identifies the authors as Peter Høyer, Troy Lee and Robert Špalek; first submission 5 November 2006; version 2 dated 24 April 2007; and conference publication in STOC 2007, pp. 526–535. It records [arXiv:quant-ph/0611054v2](https://arxiv.org/abs/quant-ph/0611054v2) and the related conference DOI [10.1145/1250790.1250867](https://doi.org/10.1145/1250790.1250867). The theorem locator here is to the 29-page author PDF actually inspected, not to conference pagination or an independently fetched arXiv PDF; byte identity of those files was not established.

At \(\epsilon=1/3\), the factor-two coefficient is \((1-2\sqrt2/3)/2\), whose reciprocal is \(18+12\sqrt2<35\). The returned Lean scripts assemble this fixed-error specialization and the rational constant 35. They do not export a new adaptive arbitrary-error complexity definition. The mathematical arbitrary-error formula above and the exact finite counterexample must not be mistaken for compiled Lean theorems.

## Exact checks and a possible Lean statement

<!-- passage:coefficient-exact-checks -->
Run `python checks/source_coefficient_check.py > checks/source_coefficient_check.json` from the return directory. The script checks all four inputs, the oracle permutation, the output probabilities, the orthonormal eigenbasis, both masks, the progress change and the strict rational comparison at error \(1/100\). Arithmetic uses integers and `fractions.Fraction` only. The final Hadamard is represented as \(B/\sqrt2\), checking \(B^TB=2I\) and dividing squared output masses by two. There is no random seed, numerical eigensolver or floating-point tolerance.

<!-- passage:coefficient-proposed-lean-statement -->
For a future formalization in `namespace QuarticQuery.Paper`, define `appendixAParityTwo : TotalBool (Fin 2)` by `fun x => x 0 ^^ x 1`. The following **proposed signature is not implemented or elaborated**:

```lean
theorem appendixA_parityTwo_exact_one_query :
    ∃ (ψ : QuarticQuery.State (Fin 2) 0)
      (A : QuarticQuery.AdaptiveProgram (Fin 2) 0),
      ‖ψ‖ = 1 ∧ A.queryCap = 1 ∧
      ∀ x, A.outputMass x ψ (appendixAParityTwo x) = 1
```

The witnesses are the state above and one `.query`, followed by the index Hadamard as `.unitary`, then a coordinate-basis `.measure` with the two output leaves. Here workspace parameter zero still gives `Fin (0 + 1)`, so the state space has dimension four. The proposition uses the actual supplied `State`, `AdaptiveProgram`, `queryCap` and `outputMass` vocabulary. It implies `QLe (totalise appendixAParityTwo) 1`; that fixed-error corollary alone would not express exact success or the \(1/100\)-error witness. No new theorem, axiom or proof placeholder for this check has been added to the Lean modules.
