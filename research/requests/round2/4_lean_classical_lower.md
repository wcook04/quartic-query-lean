## Your job: Lean for Sections 4 and 5 (the randomized lower bound and the exponent)

We want every statement of the preprint to have a Lean declaration that says exactly what it says. Your rows are Section 4 (the capped direct product, the dummy and planted inputs, the erased zero, the heavy columns and the address simulator, the final numerics) and the exponent argument of Section 5. The Lean development proves Lemma 4.1 by induction on sub-distributions (`lean/QuarticQuery/LowerBound/DirectProduct.lean`) where the paper uses a product of conditional values and a supermartingale, and proves the erased-zero bound with constant 2 where the paper has 4 (`lean/QuarticQuery/LowerBound/Planted/`).

Work list (status in brackets: n none, p partial, w weaker): claim-product-law (n), def-value-V (n), eq-16 (n), claim-supermartingale (n), claim-final-bound (n), eq-17 (n), def-dummy (p), def-planted (p), claim-Y-values (p), eq-18 (p), def-Z (n), claim-uniform-zero (n), claim-EZ (n), def-heavy (n), def-simulator (n), eq-21 (p), eq-22 (p), eq-23 (p), claim-tail (w), claim-numeric (p), cor-R-omega (p), claim-exponent-ratio (p). `lean/QuarticQuery/Paper/Section4.lean` holds candidate declarations from an earlier pass; check them first.

1. For each row, read the paper's text, its ties and notes in `corpus/ties.json`, the adjudication verdicts, the first round's proposals (`previous_round/*/NEW_STATEMENTS.json`, `LEAN_GAPS.md`), and the Lean modules that implement the step. Classify it: already stated under another name (prove the agreement); a few lines from existing declarations; a genuine new proof; or prose that should not be a theorem (say why).
2. The paper's own route to Lemma 4.1 (the value V of eq-16 and the supermartingale) is a different proof of a statement Lean already checks. State its displayed claims exactly and prove them, so a reader can check the paper's argument as written, and say in `blueprint.md` how much work this is relative to its value. Do the same for eq-17 and the paper's 4G/m² estimate (which follows from the Lean 2G/m² bound).
3. For the planted argument, state the paper's displays (eq-18, eq-21 to eq-23, claim-tail, claim-numeric) exactly, including absolute values where the paper has them; the Lean bound `tree_gap_le` is one-sided. Prove the exact forms or explain why the one-sided form is all the argument uses.
4. Write the Lean as files `lean/QuarticQuery/Paper/Classical*.lean` in namespace `QuarticQuery.Paper`, each declaration with a doc comment beginning `Ledger: <row id>`. Use only declarations present in `repository/lean/` or Mathlib at the pinned revision, named exactly. Write proofs a compiler will accept. Label every file "unelaborated" unless you compiled it.

## Return one ZIP containing

- `lean/`: your Lean files at their module paths.
- `blueprint.md`: one entry per row: class, the statement in mathematics, the Lean statement, the proof plan naming the declarations used, and any correction.
- `coverage_plan.json`: one object per row with `id`, `class`, `declaration`, `uses`, `difficulty`, `compiled`, `notes`.
- `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
