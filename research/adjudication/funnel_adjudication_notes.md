# Adjudication of the five funnel returns

Date: 2 November 2026. Companion to `funnel_adjudication.json`. The five returns in `research/returns/funnel/` were written without a Lean compiler. I checked each finding against the Lean source, the corpus, the preprint and the annexed papers. Nothing here is a new build or Comparator run.

## Result

The returns found no error in the separation argument, and I found none. Their useful content is a handful of evidence-metadata repairs, two qualifications, and one real gap in a cited paper's displayed proof that does not touch this result.

Counts over 45 distinct findings: 34 accepted, 6 accepted with changes, 1 rejected, 4 unverified. One of the 45 is my own, and I extended one other. Eight led to edits in this change; most of the rest were already recorded in the tie notes, which the returns could not see in full.

## Corrections applied

- `claim-bs-to-L`: the exact tie to `bansalSinhaLower` is removed. That theorem proves `L < R(P)` for each fixed `k`, not the comparison of `c k^-29 (m/log km)^(1-1/k)` with `L`. The row also now says `k >= 2` and `c > 0`; with `c = 0` it is false.
- `lem-2.1.i`: the tie now records `bansalSinhaLower` as a theorem at `ForrelationLower/Main.lean:506`. `Statement.lean` holds only the proposition. A sweep of every tie in the corpus found no other wrong locator.
- `thm-1.1`: the older `theorem_1_1` now has a reviewed tie, partial, with its `BansalSinhaLower` hypothesis. The empty list the returns saw came from an unreviewed doc-comment tag, not from a reviewed tie that dropped it.
- `eq-19`: the tie note no longer calls the coefficient 2 tight without qualification. Scanning a column attains it for expected cost, but scanning costs `m` in the worst case, so under a depth cap `G` it finds the zero with probability only `G/m^2`.
- `lem-A.5`: the Midrijanis locator adds that the inequality uses his Lemma 3. The corpus already placed it inside the proof of Theorem 4.

`build_corpus.py` regenerated the corpus. The exact count fell from 19 to 18, because `claim-bs-to-L` is no longer exact.

## The Bansal-Sinha logarithm (return 2)

Return 2 is right, and it is a gap, not a typo. In the final display of Section 5.4 of arXiv v3, the term at level `l` carries `log(kN)^((l-1)/2)` from Tal's bound. The next line replaces it by `log(kN)^(l(1-1/k)/2)`. Their ratio is `log(kN)^((l/k-1)/2)`, which grows with `N` whenever `l > k`. The sum runs from `l = k` to `k(k-1)`, so the step fails for every `k >= 3` and holds for `k = 2`.

Taken as displayed, the argument still gives a lower bound with denominator `log(kN)^(1-1/(k(k-1)))` in place of `log(kN)^(1-1/k)`. I did not try to decide whether Theorem 1.3 as stated follows by some other route. The preprint is unaffected: for fixed `k` either form exceeds `L`, which divides by `(log m)^2`, and the Lean development proves `lem-2.1.i` directly. The note is in the `lem-2.1.i` proof notes. The reciprocal misprint `delta^2/(4N)` in the same section was already recorded.

A second reading was then made from the TeX source alone, without this verdict: [bansal_sinha_section54_second_reading.md](bansal_sinha_section54_second_reading.md). It reaches the same conclusion independently: the third inequality of the display (`main.tex:1184`) fails for `k >= 3`; at the paper's depth the top level `l = k(k-1)` contributes about `log(kN)^((k-2)/2)`; changing the depth cannot repair it, because Tal's bound and the Sherstov-Storozhenko-Wu bound both carry `log^(l-1)`; and Sherstov, Storozhenko and Wu handle their own analogous step correctly. The argument as written proves the stated theorem with an extra factor `log(kN)^((k-2)/(k(k-1)))` in the denominator. The stated theorem is unsupported by this display, not shown false. Both readings are by AI agents.

## The route note (return 4)

- Its elementary Theorem 2, `R > (2/18225) m^(1-1/k) / (k^2 ln(4km))` for `m >= 2^(15k+2)`, checks on reading. Every constant in Section 7 and the maximal inequality of Lemma 9 work out. It is a paper deduction; a concurrent Lean file proves a version with the coarser edge constant 3 and constant `1/2332800`.
- The edge bound 3/16 is correct: the Lean kernels are the note's, with coarser proved bounds 1 and 3.
- The Sherstov-Storozhenko-Wu locator is right. Corollary 4.14 uses natural logarithms, Theorem 1.9 base two, and the constant is unspecified.
- The orientation `H(p_(r+1), p_r)` matches `Walk.lean`. The blueprint reverses it, which is harmless for the symmetric Walsh matrix.
- The hard mean `18^-(k-1)` is `mass_ge` for Walsh `H`. The general orthogonal case is paper-only.
- Its sharper Theorem 1 through Sherstov-Storozhenko-Wu I did not check.
- The prior-art document wrongly calls the Girish-Servedio bound non-adaptive.

## Partly right

- The planted-gap displays (18) and (23) print "the difference", with no absolute value. The absolute value is the ledger's wording of (18). The Lean theorems are one-sided and already tied as partial, which is all the contradiction needs.
- The replay pin `d42fb67` and the packet pin `c7e0c91` differ only in the README, the evidence graph and one receipt. No Lean source differs.
- Return 1 credits Ambainis et al. with direct pointers to each zero. Their passage gives random access through a balanced tree of pointers, which is close but not the same.

## Rejected

Return 3's replacement of the `claim-tail` exponent by `m^-8`. The bound is true and fine for exposition, but the row records the paper's correct exponent.

## A finding the returns missed

`corpus/receipts/lean-build-root.json` names commit `16adedc`, but it lists `bansalSinhaLower` and `theorem_1_1_unconditional`, whose files do not exist at that commit. They arrive in `06f3eb8`, committed half an hour after the receipt was written. The build ran on an uncommitted tree. Every `built_at_pin` flag for the Forrelation lower-bound declarations rests on this receipt. The headline's Comparator receipt is at `d42fb67`, which contains the source, so the comparison evidence stands. The build receipt should be recorded again at a clean pin. I did not edit receipts.

## Left for others

- `tools/build_corpus.py` should show negative controls as "altered solution rejected as expected". The receipts already say `rejected_as_expected`; the graph drops it. It should also replace the stale "fidelity review not run" string and show unknown hypotheses on unassessed ties.
- The `hypotheses` field mixes open assumptions with ordinary premises. That makes `eq-19` show as conditional on `T.depth <= G`, which is the row's own premise. This needs one schema change for all rows, not a piecemeal edit.
- Untied rows with existing declarations (`eq-1`, `eq-5`, `eq-17`, the winner corollaries) and the concurrent `Paper/Section2.lean` declarations are in `pending_ties`. None is tied here: the new files are not in any build receipt yet.
- Small fixes in files I do not own: the `cycleThree` comment says `i` loses to `i+1` when it wins, the blueprint's matrix orientation, and the prior-art note on Girish-Servedio.

## Not checked

- Return 4's Theorem 1 and the returns' remaining bibliographic locators (cheat-sheet definition numbers, BBHT pages, Shaltiel).
- The new statements proposed in each return's `NEW_STATEMENTS.json`, apart from those named above. None is added to the corpus.
- The returns' scripts were not run.
- `make check` fails only because `check_repository.py` rejects six preserved files in `research/returns/funnel/` (four Python scripts, a PNG and an SVG). The earlier returns moved their scripts to `tools/return_checks/`; this change does not touch the returns, so the move is left open.
