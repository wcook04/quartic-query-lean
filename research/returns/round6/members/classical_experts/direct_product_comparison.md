# Adversarial check of CX001: Drucker's global-budget theorem

## Verdict and scope

**CX001 is valid as a proof-choice question for the actual construction.** I found no gap in applying Drucker's supplied Theorem 1.1 to the capped simulator with the parameters below. Its weaker bound, \(2(2/3)^r\), still gives the manuscript's stated \(6/100<1/3\) discrepancy ceiling for every admitted construction parameter.

This is an applicability audit and substitution into an existing theorem. It is not a new theorem, a request to replace the current proof, or a claim that the global-budget theorem gives the sharp \((2/3)^r\) intermediate statement. The fair-tree proof remains correct and has an intelligible benefit: an exact product bound and a visible per-instance cap invariant.

## Sources actually checked

The source checked is Andrew Drucker, *Improved Direct Product Theorems for Randomized Query Complexity*, arXiv:1005.0644v2. The supplied directory is literature/quartic-ref-13-improved-direct-product-theorems-for-rando/. Locators below refer to its source.tex and printed PDF page numbers; the public primary record is [arXiv:1005.0644v2](https://arxiv.org/abs/1005.0644v2).

| Source location | What was checked |
|---|---|
| §1.2, Theorem 1.1; source.tex lines 313–314; printed p. 4 | Exact hypothesis, global query allowance, \(0<\alpha\le1\), weak first success inequality, independent product input law |
| End of §1.2; source.tex line 363; printed p. 6 | Explicit statement that the results also apply to partial functions |
| §2.1; source.tex lines 430–449, especially line 436 | Query cost as worst-case tree height; a randomized algorithm as a distribution of capped trees; vector-valued outputs |
| Entire §3; source.tex lines 504–606; printed pp. 10–13 | Restated theorem and its proof, including convexity, posterior factorization, the product potential, and the final fair-tree specialization |
| §3; source.tex line 516; printed p. 10 | \(T\) is permitted to be noninteger |
| §3; source.tex line 524 | Full support is only a simplifying assumption within the proof, discharged by a limiting argument |
| §3; source.tex line 556; printed p. 11 | Actual integer cost is \(M=\lfloor\alpha\varepsilon T k\rfloor\) |
| §3, Lemma 3.2; source.tex line 558 and following proof; printed pp. 11–12 | Adaptive interleaving is covered; conditioning on a complete reachable transcript leaves a product of restricted laws |
| End of §3; source.tex line 606; printed p. 13 | The source itself identifies the exact fair-tree specialization |

For this check I re-read the source theorem, query-model definitions and entire §3 proof, rather than relying only on the abstract or an extracted theorem label. PDF page locators were checked through text extraction; I did not render pages, compile Lean, or run Comparator. Yao's original paper was not read and is not needed as a newly inspected source for this check.

Current manuscript evidence:

- expert_companion.md §5 opening, §§5.1–5.5, and Appendix A's parameter definitions;
- reasoning_record.md §6.2, anchors CL-minimax and the hardness-law interface;
- reasoning_record.md §6.3, anchors CL-dummy and CL-planted;
- reasoning_record.md §6.5, anchors CL-heavy, CL-simulator, CL-joint-event and CL-cell-union;
- reasoning_record.md §6.6, anchors CL-discrepancy, CL-tail-numeric, CL-randomized-contradiction and CL-floors.

## 1. Exact theorem contract and strictness

In mathematical paraphrase, Theorem 1.1 assumes that every randomized \(T\)-query algorithm computes one Boolean function under law \(\mu\) with success at most \(1-\varepsilon\). For each \(0<\alpha\le1\), an algorithm with total cap \(\lfloor\alpha\varepsilon T k\rfloor\), on \(k\) independent inputs from \(\mu\), has all-answer success at most

\[
\left(2^{\alpha\varepsilon}(1-\varepsilon)\right)^k.
\]

Both the hypothesis and this first conclusion are non-strict. The theorem also supplies a further strict numerical simplification involving \(0.84\); that simplification is unnecessary here.

The manuscript has an integer \(L\) with \(1\le L\le m\) and \(L<R(P)\). Its finite minimax argument provides a promise-supported \(\mu\) for which each deterministic depth-\(L\) tree has success at most \(2/3\). Averaging deterministic trees gives the same bound for every randomized depth-\(L\) tree. Thus the source's one-input hypothesis holds with \(\varepsilon=1/3\).

The finite minimax separation actually supplies a strict margin below \(2/3\), but CX001 does not require or consume that extra margin. There is no mismatch between a weak source hypothesis and a strict manuscript complexity prerequisite.

The source's finite theorem allows \(\alpha\) to be selected for the particular multiplicity. It does not require \(\alpha\) to remain constant as \(k\) varies. The present selection is therefore allowed.

## 2. Parameter and floor check

To avoid confusing the source multiplicity with the manuscript's Forrelation parameter, write the former as \(k_D\). Select

\[
T_D=L,\qquad
k_D=r,\qquad
\varepsilon_D=\frac13,\qquad
\alpha_D=\frac3r.
\]

The actual construction has

\[
m=4^t,\quad t\ge1,\quad
\ell=2t,\quad r=20\ell=40t.
\]

Consequently \(r\ge40\) and

\[
0<\alpha_D=\frac3r\le\frac3{40}<1.
\]

The global cap, including the floor used in the source proof, is exactly

\[
\left\lfloor\alpha_D\varepsilon_D T_D k_D\right\rfloor
=\left\lfloor\frac3r\cdot\frac13\cdot Lr\right\rfloor
=\lfloor L\rfloor=L.
\]

The source success bound becomes

\[
\left(2^{1/r}\frac23\right)^r
=2\left(\frac23\right)^r.
\]

There is no loss from flooring, no need to reduce the simulator's allowance to \(L-1\), and no distinction between a real and an integer query threshold in this application.

The illustrative two-address toy has \(r=2\), so the displayed choice would give \(\alpha_D=3/2\), outside Theorem 1.1's stated \(0<\alpha\le1\) range. CX001 concerns the actual \(r=40t\) construction, not all toy instances or the general fair lemma. The source remarks on a larger range for its first bound, but no such extension is needed or invoked here.

## 3. Partial functions and the input law

Drucker explicitly states that the results also apply to partial functions. Here \(\mu\) is supported on the domain \(D\) of \(P\), precisely the law produced in the manuscript's minimax step.

The compatibility can also be seen without using a promise-specific interpretation of the theorem: extend \(P\) arbitrarily outside \(D\) to a total Boolean function, and give all those outside inputs probability zero under \(\mu\). Every tree's one-instance success under \(\mu\), and every vector algorithm's success under \(\mu^{\otimes r}\), remain unchanged. This is an explanation of how the supplied theorem applies, not a proposed change to the paper's constructed total function.

The source theorem quantifies over arbitrary \(\mu\). Its proof's temporary full-support assumption is expressly justified by a limiting argument. A promise-supported law therefore causes no support gap.

The requirement is independence of the \(r\) entire target strings, each with law \(\mu\). It does not require individual bits within a string to be independent, and it does not require the labels \(P(U_h)\) to be balanced. The current dummy distribution draws all address strings independently from \(\mu\), satisfying the actual requirement.

## 4. The actual simulator is a global-cap algorithm

For fixed column \(i\) and time \(q\le G\), reasoning_record.md at CL-simulator supplies as outside data all zero positions \(J_j\), the address strings in other columns, and the fixed blank cells. It explicitly supplies no target string, target address, or target transcript.

These outside data are jointly independent of the \(r\) target strings under the dummy law. Fixing any outside-data outcome of positive probability leaves the target law exactly \(\mu^{\otimes r}\). With that outcome fixed, the simulator is an ordinary deterministic vector-output query algorithm:

1. It computes all answers to outside queries for free.
2. It forwards target queries to the appropriate target string.
3. One shared counter charges every such query, including repetitions.
4. It aborts before query \(L+1\) to the target tuple in total.
5. At the proposed \(q\)-th query, a cell coordinate \(B_{i,s}\) already determines an answer vector \(s\); no cell-content query is needed to output it.
6. On termination, abortion, or a different proposed coordinate, it outputs a fixed vector.

Deleting the free internal simulation steps gives a decision tree of depth at most \(L\). Its cap holds for every target input tuple and every branch. Adaptive selection of which target to query next is fully permitted by the source theorem.

Apply the source bound after fixing the independent outside data, then average over those data. Equivalently, they can be viewed as the simulator's independent random tape. The result is the unconditional success bound \(2(2/3)^r\). There is no conditioning on nonheaviness; the actual manuscript uses an event inclusion from the light-and-true-cell event into simulator success.

The final randomized original algorithm also poses no additional issue: the manuscript first works with a deterministic capped tree and finally averages over its independent random tape. The global theorem itself already permits randomized capped algorithms.

## 5. Does the factor two fit every admitted parameter?

Yes. The actual parameter relation gives the finite bound

\[
\left(\frac23\right)^r
=\left(\frac49\right)^{20t}
\le 2^{-20t}
=m^{-10}.
\]

Since \(G=\lfloor mL/100\rfloor\), \(1\le L\le m\), and \(m\ge4\),

\[
G\le\frac{mL}{100}\le\frac{m^2}{100}.
\]

Using the global theorem at the existing joint-event step changes only the guessing term in the manuscript's discrepancy estimate:

\[
\frac{4G}{m^2}+\frac{G}{mL}+2G\left(\frac23\right)^r
\le
\frac4{100}+\frac1{100}+\frac{2}{100m^8}
\le
\frac6{100}<\frac13.
\]

The last weak inequality already follows from \(m^8\ge2\); every admitted \(m=4^t\), \(t\ge1\), satisfies it. Thus the same \(6/100\) ceiling survives, not merely some unspecified constant below \(1/3\).

A more precise uniform envelope at the smallest admitted \(m=4\) is

\[
\frac4{100}+\frac1{100}+\frac{2}{100\cdot4^8}
=\frac{163841}{3276800}
=0.05000030517578125.
\]

This envelope decreases with \(m\). Exact rational arithmetic was used only to check the displayed fraction and decimal; the universal conclusion follows from the inequalities above, not from sampling finitely many parameters.

If \(G=0\), the query-time union is empty, and the actual discrepancy is zero. Nothing divides by \(G\). If a small-\(t\) concrete Forrelation choice yields \(L=0\), it does not satisfy the generic theorem's admitted assumption \(1\le L\); no extension to that excluded case is being claimed. The concrete family is used past the manuscript's stated positivity and hardness thresholds.

## Consequence for CX001

Retain CX001 as a narrowly phrased question about the chosen exposition route. An expert may reasonably ask why the exact fair-tree lemma receives the primary attention when the cited global-budget theorem already supplies enough decay for the actual total-cap simulator.

The answer may simply be that the exact fair proof is short, transparent, and gives the cleaner \(\beta^r\) contract used in the printed intermediate statements. The review should preserve that benefit. It should not call the fair lemma erroneous, claim the headline global theorem yields the exact printed intermediate bound, or request a new formalization.

**No applicability gap was found in the actual construction.**
