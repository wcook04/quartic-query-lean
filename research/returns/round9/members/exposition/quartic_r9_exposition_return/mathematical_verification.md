# Mathematical verification and limits

The calculations below check the exposition's worked examples and several delicate interfaces. They do not certify the entire preprint, its analytic Forrelation lower bound, or the Lean development. No Lean compilation, Comparator run, or manuscript build was performed. Existing receipts in the supplied packet are historical evidence.

All line references below refer to the supplied repository/docs/exposition.md, whose SHA-256 is recorded in coverage.json. The executable standard-library check is checks/verify_mathematical_examples.py; its output is evidence/mathematical_example_checks.json.

## 1. The small interference experiment

Exact rational arithmetic over all 256 eight-bit inputs gives values of Φ in multiples of 1/8 and within [−1,1]. The four inputs actually used in the exposition give:

| Bit string | Φ | Projection success Φ² | Promise status |
|---|---:|---:|---|
| 0111 1000 | 1 | 1 | P=1 |
| 0100 1000 | 0 | 0 | P=0 |
| 1000 1000 | −1 | 1 | Outside the promise |
| 1111 1000 | 1/2 | 1/4 | P=1 |

The last row matters editorially: a criticism claiming that *every* worked decoder case is deterministic would be false. The sign-blind projection is the chosen experiment; this is not a claim that all quantum access is sign-blind. The source itself distinguishes projection success from decoding correctness (lines 92–96).

For the toy cell, the four test families give 4+3+2(180+2)=371 tests, and the stated board layout has 5,936 input bits. The toy uses r=2 rather than the theorem family's r=20 log₂m. Its L₂,₄ is zero. Its role is to expose operations, not instantiate the positive-budget hardness theorem.

## 2. Question 1: certificate failures

At column 2 of the domain-bit board, the first domain output is zero and the value outputs are 00. String, pointer and gate-consistency tests pass. The exact remaining failures are:

| Chosen cell label | Failed output tests |
|---|---|
| 00 | First domain test |
| 01 | First domain test; second value test |
| 10 | First domain test; first value test |
| 11 | First domain test; both value tests |

Thus the source counts 1,2,2,3 are correct (lines 151, 410). An indexed answer table would diagnose swapped bit positions that equal counts conceal.

## 3. Question 2: product weights and overshoot

On the cycled board, successive pivots 2 and 4 give weights (1,0,0,1) and then (1,0,0,0). The second preparation has success probability 1/4, and conditional success selects column 1. With θ=π/6, one Grover iteration succeeds with probability one; two iterations total succeed with probability 1/4.

For the separately declared fractional comparison matrix, the two weight vectors are (1,0,2/3,1/4) and (1,0,4/15,0). After the second pivot:

- Joint success-and-label masses are (1/4,0,1/15,0).
- Total success is 19/60.
- The successful label law is (15/19,0,4/19,0).

These quantities are different and all agree with the answer (lines 241–245, 274, 412). The matrix is not claimed to be realized by the physical four-column board. Verification resumes the physical board; the answer should mark that return.

The exact script also checks the half-drift identity for all 64 orientations of a four-vertex tournament and three unequal/equal weight choices: 192 finite instances. For the general identity, pair the ordered off-diagonal terms using aᵢₚ+aₚᵢ=1 and aᵢᵢ=0. A separate total-expectation step propagates the conditional inequality. Finite enumeration supports the examples; it does not replace that argument.

## 4. Conditional amplification and the capped routine

The successful component includes the entire retained workspace. Amplification changes its scalar coefficient and preserves its normalized direction. Every successful trial therefore has the same conditional label law. Mixing iteration counts and stopping at the first successful fresh trial preserves that law as well. The local exposition establishes the fixed-iterate part and should expose the last mixture step.

The source preprint explicitly supplies this bridge in Lemma 3.1 (paper/extracted.md, lines 305–355). The packaged expert companion's Lemma 2 also supplies the half-direct/half-randomized trial, the p=1 endpoint and finite retry cap. BHMT's untruncated QSearch has an expected-cost guarantee and runs indefinitely at zero success; it must not be substituted for the local bounded contract. See amplification sources S15–S16, the local accounts S02/S04, and the precise record landing in evidence/cross_document_checks.json.

On a one-input, the winner's weight remains above 1/2 until selected, so the prepared success probability is at least 1/(2m) on the histories where the sampling guarantee is used. Coupling is valid stage by stage at a common history. Conditioning the whole ideal process globally on every real stage succeeding would be an invalid replacement.

At line 282, both error budgets are valid. On F=1, Tε covers premature sampler failures and the final ε covers the winner's fresh decoding. On F=0, Tε covers missed violations across the list. Comparison decoding errors already enter the comparison probabilities and winner-weight calculation; there is no additional missing zero-input decoder-error term.

## 5. Question 3: an independently selected column

Enumerating the 256 zero-location tuples for four columns confirms:

| Fixed distinct positions queried per column | Independent I: erased zero hit | I chosen from found zeros, with the stated default |
|---:|---:|---:|
| 1 | 1/4 | 175/256 |
| 2 | 1/2 | 15/16 |

For arbitrary adaptive query rules, the identity remains E[Z]/4 when I is independent of the entire dummy run. The fixed-pattern numerical values do not automatically remain unchanged. At an adaptive prefix, the next zero location is uniform on unread rows because every candidate unread location gives exactly the same observed answers and deterministic choices up to that prefix. This is the missing explanatory bridge at line 317; it is not an invalid bound.

## 6. Question 4: a stopped predictor and whole-run lightness

Exact enumeration of the 16 XOR inputs confirms the event distinctions:

| Event in the specified trace | Probability |
|---|---:|
| Original light true-cell visit | 1/8 |
| Original stopped predictor correct, including lucky default output | 1/4 |
| Modified a=0 branch visits the true cell and stops | 1/8 |
| Total light visit after that modification, including the unchanged branch | 1/4 |
| Total light visit if the modified branch later reads c | 1/8 |

A later target query makes the whole modified branch heavy. The earlier visit still occurred; it no longer belongs to the joint light-and-visit event. The simulator does not condition its input law on lightness. The fixed-time lemma and the exercise's union of branch-specific visit times should be distinguished explicitly (lines 344–360).

There is no missing factor m in the nonheavy bound. The proof unions over query times for each fixed column and then averages the independently uniform planted column. The earlier concern about this factor was resolved and is not recycled as a mathematical objection.

The exact script checks the one-query AND optima 3/4 on four uniform inputs and 2/3 on the three-point promised law. The pooled-budget strategy succeeds with probability 3/4, exceeding the separate-cap product benchmark (3/4)²=9/16. The conditional-value example has average product 9/16 as well. These experiments and quantities must remain separately labelled.

## 7. Question 5 and parameter domains

For fixed k=4, the estimates exclude powers strictly below 7/2. They do not exclude the endpoint inequality. At α=7/2 and k=5, the power in the ratio is d=1/20>0, so the logarithmic denominator cannot prevent divergence. The order is α first, then a fixed k, then m through sufficiently large powers of four. Constants depending on k cannot be treated as uniform while k grows.

The omission of t≥1 at line 102 is a genuine local scope defect: t=0 gives m=1, a zero upper bound for S at line 173 and a zero logarithmic denominator at line 181. The record explicitly fixes positive integer t at line 441; the expert companion does so in Section 2. This does not contradict the headline theorem, whose range is sufficiently large powers of four.

The script's final numerical gap check concerns only the algebraic envelope for m≥4 under the separate hypotheses of the proof. It does not claim hardness for m=4.

## Remaining mathematical limits

The analytic lower bound for Forrelation is imported, not rederived here. The fixed-k weakening to L was compared with Bansal–Sinha's statement and with the packaged reconstruction. The full exact-circuit construction, formal semantic correspondence and optional growing-k refinement were not audited end to end. These limitations are recorded separately from the complete reading of the lead manuscript.
