# Forrelation findings and source boundaries

## Supplied work

The five `ConstructionForrelation*.lean` files contain 26 declarations, all marked unelaborated. They supply literal definition bundles, the complete promise including its undefined branch, the numerical comparison with `L`, an integer matrix normalization theorem, actual circuit output-bit rules, and a conjunction of all three parts of Lemma 2.1. The signatures and row-by-row reasoning are in `row_records.json`; every requested row has an entry. No imported file is `Paper.Section2` or `ForrelationLower.Uniform`.

The paper fixes `m` to powers of four at the beginning of Section 2. This agrees with `mValue t = 2^(2*t)`. The dyadic extension in a previous Forrelation research note is a separate proposed generalization and is not silently imported into these statements. See `paper/extracted.md`, Section 2 opening and Section 2.1, and `Statement.lean:153–190`.

## Probability, coherent implementation, and query count

The probability law and both promise inequalities have exact existing components: `successProb_eq`, `successProb_of_true`, and `successProb_of_false`. `Upper.forr_samples` supplies `k` abstract reads. The generic compilation theorem `Samples.runs` charges `2k` physical bit queries. The primary `construction_lemma_2_1_ii_complete` exposes one finite witness `Z,o,out,F`, its accurate Boolean law, and the physical `compile_circ` equation for the same `F` on every embedded logical state and every continuation. The cap constant is quantified before dimension and error. The older Samples/Runs conjunction remains an explicitly partial helper because `Samples.runs` measures and resets.

The root-owned `ConstructionPhase.lean` additionally proves the exact one-call phase action on the minus-answer subspace and preservation of that subspace and normalization. This supports the local phase-kickback sentence. It does not supply an end-to-end `Runs k` declaration. The `claim-proj-prob` metadata preserves this residual instead of relabeling the generic `2k` implementation as a `k`-query program.

Aaronson and Ambainis, *Forrelation: A Problem that Optimally Separates Quantum from Classical Computing*, Section 3.2, describe the direct `Phi^2` test before Proposition 6. Proposition 6 is a different, sharper algorithm with `ceil(k/2)` queries and acceptance law `(1+Phi)/2`; its thresholds also differ. Cite the relevant paragraph, not Proposition 6 as though it were the same test. The held extracted source was read at lines 585–760, covering Sections 3.1–3.2 and Figure 1. Primary source: <https://arxiv.org/abs/1411.5729>.

## Arithmetic construction

The existing circuit implements fixed-width residues, as the `Enc` definition in `Forrelation/Arithmetic.lean` states. Exactness of the final Boolean tests follows from the final range estimates. This is sufficient for `CircuitRealises`; it does not itself state a signed, unbounded-integer interpretation of every stored register.

Our exported circuit-cost statement includes the actual width, butterfly gate-cost estimate, layer cost, final numerator bound, correctness and total size. The root-owned `ConstructionArithmetic.lean` supplies separate ideal integer bounds for the walk, prefixes and butterfly blocks. These make the elementary polynomial-magnitude argument precise. Full correspondence of each stored modular register to an unbounded signed integer at the selected width remains a distinct formal obligation. No overflow counterexample has been established, and the missing binding must not be reported as a false width bound.

The actual value output is fixed on unpromised inputs as well: it is the first integer comparison. This required exporting the last-gate computation, since the generic `CircuitRealises` interface constrains the value output only when the domain bit is true. `construction_forr_output_bits` supplies both actual output-bit rules for every gate-consistent transcript.

## The published lower-bound comparison

`construction_claim_bs_to_L` proves the isolated numerical comparison for every positive constant `c` and fixed `k>=2`. Its stronger helper states the full floor/unfloored/published-expression chain. The previously supplied candidate `claim_bs_to_L_log2` described the unfloored middle comparison in its comment without including that middle inequality in its exported type. The new helper makes it literal.

The independently proved repository theorem `ForrelationLower.bansalSinhaLower` establishes the eventual complexity inequality `L<R(P)`. It does not state the precise published Bansal–Sinha rate and is not an exact witness for the isolated numerical comparison. The new Lemma 2.1 conjunction uses this repository proof as an explicitly different route for part (i).

Bansal and Sinha, *k-Forrelation Optimally Separates Quantum and Classical Query Complexity*, Theorem 1.3 and Corollary 1.4, supply the cited published rate. Their original `main.tex` from arXiv v3 was inspected directly: lines 150–330 for the definitions and main theorem, 760–805 for the Fourier-growth context, and 1140–1202 including the whole Section 5.4 argument. The step at line 1184 does not dominate the preceding logarithmic factor uniformly for levels above `k`: the exponent difference is positive there. The held adjudication already documents this for `k>=3`. This diagnoses that displayed deduction; it does not disprove the theorem. Neither our numerical comparison proof nor the repository fixed-`k` lower-bound proof depends on that step. Primary source: <https://arxiv.org/abs/2008.07003>.

## Historical transcript slice

The assigned pasted attachment was read completely at lines 901–1759. It confirms the independent treatment of statement identity, compilation, comparison, proof route and dependency reach. The first-round returns had already distinguished the `k` versus `2k` phase implementation and the numerical-comparison mismatch. The later stronger uniform and dyadic research claims in that transcript are proposed statements at that historical point, not fresh execution evidence for the five modules supplied here.

The transcript contains historical recipient and publication planning. Those details do not belong in these deliverables. Historical shell commands and quoted skill instructions were treated as source material only.

## Verification

No Lean compiler, Lake build, Comparator run or external-kernel replay was performed for this contribution. The source was reviewed against the supplied declarations and successful proof patterns. `reading_receipt.json` lists exact full-file and partial-file coverage; it does not claim a full read of unrelated lower-bound internals or all literature files. The existing packet build flags and adjudication receipts remain historical evidence and are not transferred to the new declarations.
