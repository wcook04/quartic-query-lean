# Independent source/mathematics peer review of proposed §4

Review date: 2026-11-02. Advisory AI review, not human review. The initial draft was read in full from `return/section.md`; it was not edited by this reviewer. This review evaluates ordinary mathematics, attribution, coherent query accounting and the finite example. Native Lean evidence remains the separate Lean auditor's responsibility.

## Verdict

The mathematical proof spine is correct at the supplied circuit interface. The retained-workspace `2 q_*` physical query bound, the clean `4 q_*` corollary, uniqueness, totality, local-test equivalence, off-promise winner dominance, and the finite `K` bound are justified. The example's actual promise values and circuit size are correct. The initial draft has concrete presentation defects and a mismatch with its example files that must be repaired before delivery.

## Required fixes found in the initial draft

1. **Math delimiters throughout.** Most inline formulas appear in ordinary parentheses, e.g. `(P:D\to\{0,1\})`, rather than `$...$` or `\(...\)`. The few surviving `\(...\)` suggest accidental delimiter stripping. Repair globally and inspect the result; a blind replacement of all parentheses would corrupt ordinary parentheses and nested formulas.
2. **Malformed display (4.12).** `W(y;i,s)quad\Longleftrightarrow` must be `W(y;i,s)\quad\Longleftrightarrow`.
3. **Example definition and failure counts disagree with the current checker.** In `work/example/check_example.py`, `make_board` puts every pointer into each nonwinner at that target column's zero, at every cell. Rivals' pointers into column 1 range over all four rows as their address varies. The initial draft instead says all pointers default to row 1 except three in `B_{1,10}`. Adopt the checker rule or revise and rerun it consistently. With the current checker, the wrong addresses `00,01,11` for column 1 have respectively **1,2,1 failures**, not 3,4,3; all their pointer tests pass and the failures are value-output tests.
4. **Example label list punctuation.** Replace `(00,01,10,) or (11)` by a properly formatted list `00, 01, 10, or 11`.

## Two precision edits

- **Retained phases.** The displayed direct-sum identity (4.15) is correct. The sentence “preserves all coefficients and relative phases” can be read as preservation of the reduced index state, which is not guaranteed when the index becomes entangled with workspace. Prefer: “The controlled unitary acts linearly on the supplied coefficients; the workspace may become entangled with the label and depends on the input.” No change to the formula or theorem is needed.
- **Complete boards in JSON.** `board.json` currently contains the complete base board. The counterexample is generated completely by `domain_omission_check`, but its JSON output contains only its X strings, tested pair and result summaries. Say “complete base board and counterexample construction” or additionally export the full second board before calling the JSON files “complete boards”.

## Checked mathematical points

### Transcript and semantic construction

The induction for (4.2) is valid on every raw input. Applying (4.1) to the evaluated domain/value gates then establishes the exact certificate interface. The semantic definition (4.5), including equality to the true transcript, is total without needing to define the partial function off-domain. Its circuit-correctness premise is needed exactly at (4.12), not for totality or uniqueness. Column uniqueness uses the direct contradiction between an outgoing zero and the other column's all-one string; address uniqueness then follows bitwise. No gap found.

### Size bound

`r=20 ell` and `S≤A m ell²` imply

`K=2m−1+20ell S+40ell ≤ (42+20A)m ell³`

for `m≥4, ell≥2`, as the draft proves. The constant is loose but valid and matches `construction_lemma_2_2_complete`. No need to sharpen it.

### Coherent query accounting

The ordinary proof supports the stated constants:

1. Fix the candidate `(i,s)` and use an exact depth-at-most-`q_*` decision tree for each label.
2. Retain each level's answers and reversibly compute its next location from the label and history. At an inactive leaf use any fixed valid location, with the active control false. The input bit is loaded into a clean temporary register, conditionally XORed into the retained answer, and unloaded with the same location. This costs two ordinary bit queries and leaves the temporary clean.
3. Use `q_*` such levels, with no intermediate measurement. The entire controlled evaluator costs at most `2q_*` queries, retains its history, and is invertible.
4. Its output label is deterministic inside each index block. A query-free controlled XOR into a separate target therefore leaves that block's workspace unchanged. Applying the inverse restores it, at another `2q_*` queries. The clean oracle costs at most `4q_*` queries and acts on arbitrary superpositions by linearity.

The existence of an arbitrary test-index superposition is faithfully separated from the particular uniform test sampler. Fixed `(i,s)` is the scope of the printed formal theorem; no superposition over candidate pairs is claimed in this draft. The clean corollary is properly classified as an ordinary proof, separate from the formal retained-workspace statement.

### Example arithmetic and exact replay

I independently ran `python3 work/example/check_example.py`; exit code was 0, all checks passed, and the parsed stdout matched `work/example/output.json` exactly. The output SHA-256 was `f3d99698661e40b838f6ebdcfe7e839b5d0076af30c92da8e56a4be68c8d942f`; checked script SHA-256 was `86ebd2d14aabae3a473bbdb7ecab80bd22a1dfdf48a321f4fc36d725e7022103`.

Verified values and scope:

- `S=180`, output gates 178 and 179, `K=371`, total base-board input bits 5936.
- `00000000`: `N=4`, `Phi=1/2`, `P=1`.
- `00010010`: `N=0`, `Phi=0`, `P=0`.
- `11110000`: `N=−4`, `Phi=−1/2`, outside the one-sided promise.
- Matrix product for the zero instance is correct: `W(1,1,−1,1)^T=(2,−2,2,2)^T`, with zero inner product against `(1,1,1,−1)`.
- Circuit outputs checked against integer and independent rational evaluations on all 256 inputs.
- All 16 pairs on the specified base board checked against the direct semantic predicate.
- All 360 single-bit selected-transcript changes tested; these are not exhaustive arbitrary transcript corruption tests, and the draft does not claim otherwise.
- Six essential-coordinate witnesses for the two-bit pointer/four-bit target lookup are correct.
- Domain-omission counterexample has exactly one failed domain test while every remaining test passes; its full semantic function value is zero.

The board intentionally has `r=2` instead of the family's `r=40`, and uses a truth-table circuit instead of the asymptotic circuit. Both qualifications are clearly disclosed. It illustrates the genuine `P_{2,4}` promise and generic construction, and does not assert a finite-case separation.

### Off-promise comparison

The event inclusion in (4.19) is correct without a promise or correctness guarantee on the rival. Independence of the rival's decoded label is unnecessary for this implication. Orthogonal retained labels justify the mixture interpretation of the coherent circuit. The true winner's address correctness follows by a union bound over its promised instances. Comparisons of two nonwinners remain unconstrained.

### Attribution

The distinctions among OpenAI's construction, ABK's historical certifying/addressing framework and Lemma 17's evaluate-then-check strategy, and Ambainis et al.'s direct-pointer discussion are all accurate. The latter's exponential-alphabet qualification is now properly included. Exact arXiv editions and printed locators are correct. The OpenAI short commit pin is not independently checked in this second pass; the root author should retain its own verification receipt for that URL if describing it as a supplied pin.

## Disposition

No substantive mathematical repair is needed. Fix the formatting, align the example description and counts with the delivered data, and make the two precision edits before final packaging. The proof and citation content otherwise passes this focused independent review.
