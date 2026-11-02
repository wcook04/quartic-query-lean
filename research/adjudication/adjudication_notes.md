# Adjudication of the three research returns

Date: 2 November 2026. Companion to `adjudication.json`. Nothing here is a formal proof, and the intake ledger itself was not edited. Proposed row text is in `ledger_row_changes`.

## Result

The paper's proof held up under a second, independent line-by-line reading, including Sections 2 to 5 and Appendix A. I found no mathematical error. The returns are mostly right. Their real value is a small set of statement and dependency repairs.

Counts over 84 entries: 60 accepted, 14 accepted with changes, 3 rejected, 7 unverified. Of these, 72 respond to the returns, 6 are calculations the brief named, and 6 are points the returns missed. All 84 are in the JSON by return. 31 existing rows change text or dependencies, and 3 rows are added. The revised dependency graph has no cycle (121 rows checked by script).

## Corrections adopted

- `lem-2.2.i`: a pointer test is a decision tree of depth at most max(3, l+1), not a function of a small fixed bit set. At m=4 it depends on all six variables, checked exhaustively.
- `def-deg`: degree 0 for every constant, including the zero function.
- `eq-5` and `eq-17`: now definitions only. Their inequalities live in `lem-2.1.i` and `prop-4.2`. Return 3 preferred to keep `eq-17` as an assertion depending on `prop-4.2`; that is rejected.
- `claim-minimax-mu`: split into generic minimax and a new `claim-address-guess`. Lemma 2.1(i) enters at `prop-4.2`. The hypothesis 1<=L was not needed here.
- New `prop-4.2-generic` carries the non-asymptotic form. The concrete row is its instance, and it must use the same circuit as the quantum bound.
- New `claim-winner-fidelity` ties a primitive `WinsAt` back to the paper's winner, using circuit correctness.

## Rejected

Three of return 3's dependency edits. Dropping `lem-2.1.iii` from `lem-2.2.i` loses the meaning of the output tests. Making `eq-17` depend on `prop-4.2` is replaced by the split. Removing the Appendix edges describes an import route through library theorems, not the paper's structure.

## Calculations redone

- r=40t, l=2t and 2^r=m^20 hold exactly for m=4^t. T needs base 2: natural log gives 2m/2^T=64 at m=4^20.
- (2/3)^(40t) is m^(-11.699). The bounds m^-10 (return 3) and m^-11 (return 1), and the ledger's G-tail target m^-9, are all true, with no real discrepancy. Exact check for t=1 to 39.
- Total quantum error stays below 0.00304 for m=4 to 4^199.
- The AND example is correct. Returns 1 and 3 quote different true quantities: conditional success 1, joint probability 1/2, one-query optimum 3/4.
- n=O_k(m^22 log^3 m) is correct, but it is derived and is not stated in the paper.
- k=3 refutes the cubic bound with ratio m^(1/6) over polylogs. k=2 does not.

Both return scripts ran from copies in a separate directory with `python3 -I`, exit 0, and their output matched the saved results. `verify_examples.py` took its output path as an argument. `finite_checks.py` takes no paths, so its copy wrote `finite_checks.json` beside itself in the scratch directory. My own checks are in `scratchpad/scripts_iso/own_checks.py`, exit 0.

## Citations checked in the primary text

Bansal-Sinha v3 equations 1.1 to 1.3, Theorem 1.3, Corollary 1.4 and Section 5.4. Drucker Section 1.3, Theorem 1.1 and Lemmas 3.1 and 3.2. Midrijanis, inside the proof of Theorem 4. ABKRT Theorems 1 to 3, Lemma 9, Conjecture 2 and its footnote on the earlier preprint. Huang's remark. BHMT Lemma 1 and Eq. 8. Goos-Pitassi-Watson Section 2.1. All match what return 2 says, and ledger doubt D9 is closed.

## Points the returns missed

- Lemma 3.1 must read "there is one procedure, black-box in A, for all A". As written, the procedure could depend on p, which depends on the oracle input. The proof is uniform. Return 3 raised this order for Proposition 3.2 but not here.
- Bansal-Sinha's proof needs N large depending on k, so a single threshold for all k overstates it. Their proof display also prints delta^2/(4N) where their Theorem 3.1 gives 4/(delta^2 N). That is harmless for fixed k.
- `cor-cubic-refuted` does not need Q>=1, since Q^3 <= (1+Q)^3.
- The ledger's Lean target for r misdescribes it. Use 40t.
- A generic circuit must have d and b among its non-input gates.

## Not checked

- The truth of the Bansal-Sinha lower bound. It is the one external input, and neither I nor any return re-proved it. Any Lean main theorem is conditional on it.
- Ben-David 2015 priority: the source is not held.
- The contents of arXiv:2004.13231. Its existence and four authors are confirmed from ABKRT, nothing more.
- Barnum-Saks-Szegedy, Nisan, Nisan-Szegedy and Yao originals, and the online correction notes.
- Every claim about external Lean libraries, including complexitylib, Troy Lee's library, arlib and the 11 intake corrections in return 3. No clone was found and no network was used.
- Nothing was compiled. The local project has no `.olean` for `Drift`, and the live `Drift.lean` differs from the copy return 3 audited.
- I read all 118 ledger rows, but I did not audit `comparator_design.md`, `model_decision.md`, `core_definitions.lean` or each row of `formalisation_plan.json` beyond dependency differences and selected audit notes.
