# Round five: statement fidelity of the cited Lean results

Reviewer: Claude (Opus 5.5), 3 November 2026. This pass compared each Lean result that the two papers cite against the claim it is cited for. It read every cited declaration and the definitions it uses, the preprint's statements as extracted in `research/intake/statement_ledger.json`, and their use in `docs/expert_companion.md` and `docs/exposition.md`. Lean was not run, and no proof was judged here. The machine-readable record is `round5_statement_fidelity.json`.

## The four compared theorems

The statement file defines R and Q as the standard bounded-error worst-case query complexities. R is the least depth of a finite mixture of decision trees that is right with probability at least 2/3 on every promised input. Q is the least syntactic query cap, taken over every measurement branch and every input, of a program whose initial state, unitaries and measurements are all fixed before the input. The program reaches the input only through the bit oracle. The Forrelation promise P, the function F, and the parameters L, G, l = 2t and r = 40t all match the preprint's equations (1) to (8) and (17). No compared theorem carries a hypothesis.

| Paper claim | Lean statement | Relation | How it differs |
|:--|:--|:--|:--|
| alpha_tot = 4 | `alpha_tot_eq_four` | same | The infimum of the empty set would be 0, so the equation alone already shows the set is nonempty. |
| Theorem 1.1 with (2) | `theorem_one_one` | same | Order: k, then constants S, A, b and threshold, then all t, then one circuit serving both bounds. The power b of the logarithm is existential. The lower bound is Proposition 4.2's floor(mL/100) < R, which implies the 1/400 form for t >= 8. The circuit is existential, as in Lemma 2.1(iii). |
| Cubic conjecture fails | `cubic_bound_fails` | same | Uses Q^3 rather than (1+Q)^3. Functions with Q = 0 have R = 0, so the two forms are equivalent. |
| (5), Lemma 2.1(i) | `forrelation_lower_bound` | same | States L < R(P) for each fixed k beyond some threshold. This is strictly weaker than Bansal and Sinha's Corollary 1.4, despite the name `BansalSinhaLower`. |

## Other cited results

| Paper claim | Lean statement | Relation | How it differs |
|:--|:--|:--|:--|
| Lemma 2.2 ("four facts") | `winsAt_unique` and three others | different | None of the four is part of Lemma 2.2. They are the unique-winner corollary, unique transcripts, and the Boolean halves of "the winner dominates" from Section 3.3. |
| Lemma 2.2 | `construction_lemma_2_2_with_support` | stronger | Gives the test equivalence on every input and test trees of depth 2t+1. It gives the exact count K, essential pointer coordinates, and a physical cap of 2(2t+1). The coherent clause does not promise that the workspace is restored. |
| (11), preprint (19) | `checked_eq19` | stronger | The identity and the 4G/m^2 bound hold for any m = 2^l and any input law. |
| Lemma 3.1, coherent | `uniformOpaqueAmplifier` | stronger | It is uniform in A and returns a product of A's good state with an auxiliary vector, with exact success mass. Its success test is a predicate on basis labels; the reduction from a general projector is routine but is not in Lean. |
| Lemma 3.1, measured | `Samples.amplify` | weaker | It fixes the law of the measured label and not the state. This is the form the upper bound uses. |
| Lemma 4.1 | `direct_product_external_finite_realized_caps` | stronger | It covers uncapped algorithms, through the joint event of success and compliance. Randomness ranges over a finite seed space. Compliance is not proved equal to the count condition. |
| (12), preprint (21) | `eq_21` | same | A joint event under the original law, with beta = 2/3 and the minimax hypothesis on mu as a premise. |
| 6 and 1/400 | `construction_family_named` | stronger | Uses a named circuit and explicit constants. Its threshold is existential: no Lean theorem states t >= 13669 k^2. |
| (16) | `forrelation_lower_uniform_sharp` | same | Uniform in k. It is incomparable with Bansal and Sinha: a better power of k and a worse power of the logarithm. |
| Remark, explicit Q | `Q_Fkm_le_exponential` | same | Q(F) <= 2^53 k 2^(10k) sqrt(m) (2t)^6 for every t >= 1. |
| 2G/(m(m+1)) | `zero_search_sum_successor` | weaker | It is the deterministic charging inequality only; no probability bound is derived. |
| 2G/m^2 | `erasedZero_le_two` | stronger | Half the paper's 4G/m^2. Neither paper cites it at present. |
| explicit budget | `budget_le` | different | Bounds an internal counting function, not Q. Cite `Q_Fkm_le` for Q. |
| model checks | zero-cost, degree | different, same | Calibrations: D, R and Q vanish exactly on functions constant on their promise. The imported degree is the paper's degree. |

## Where a paper currently says more than the Lean statement

1. **Lemma 2.2 "four facts".** Table 2 of the companion lists `cmp-lemma22` as a partial form of Lemma 2.2, and the link registry calls it "the four parts of Lemma 2.2". Neither is right: the four theorems state other facts from Sections 1.3, 2.2 and 3.3. The repository's own ties file them under those rows. Lemma 2.2 itself is `cmp-lemma22-full`.
2. **"Built" against the sources' own status lines.** Three files still say they are uncompiled: `ConstructionFamily.lean` ("Status: unelaborated"), `ZeroSearchSuccessor.lean` and `RealizedCaps.lean`. Oleans exist for all three, but `ConstructionFamily.lean` was modified after its olean was written. A fresh build receipt would settle this, and the status lines should be corrected.
3. **The wrong solutions.** "Rejected in the same setup" is true of the tool, but the five controls target the Tournament challenge and not the four theorems.
4. **"Explicitly specified" F.** In the compared theorem, F is built from some circuit that realises P. The named circuit appears only in the constants theorem, which is built but not compared. The two are equally strong mathematically.

One place understates the Lean statement. The exposition calls the floor form of the lower bound a weakening, but for t >= 8 it implies the 1/400 form.

## Disagreements with earlier reviews

This pass disagrees with the companion's Table 2 on `cmp-lemma22`, as described above. Otherwise it agrees with `corpus/ties.json`, `docs/statement_fidelity_review.md` and `round4_formal.md` on every statement they cover. Their conditional-headline concern is closed: no compared theorem takes `BansalSinhaLower` as a hypothesis.

## Open questions

- Should "evaluated coherently" in Lemma 2.2(ii) include clean uncomputation? If so, the Lean clause is weaker on that point, though the proof does not need it.
- The companion uses link labels `def-output-mass`, `def-gate` and `def-pointer`. These are absent from the current `CITATIONS`.
