## Your job: Lean for Section 3 (the quantum upper bound)

We want every statement of the preprint to have a Lean declaration that says exactly what it says. Your rows are Section 3: amplification, the comparison probabilities, the ideal tournament, the coherent sampler, decoding, comparison, verification and the error bound. The Lean development proves the final upper bound `QuarticQuery.Upper.Q_Fkm_le` through its own modules (`lean/QuarticQuery/Amplification/`, `Tournament/`, `Upper/`), sometimes with different interfaces from the paper's: the tournament there runs the verifier inside a Boolean continuation, while the paper's Proposition 3.2 returns a list.

Work list (status in brackets: n none, p partial): def-grover-trial (p), claim-grover-state (p), claim-sin2theta (p), eq-9 (p), def-aij (n), eq-10 (p), def-T-eps (p), eq-11 (n), eq-13 (n), claim-weight-lb (p), construct-sampler (p), eq-15 (n), claim-success-prob (n), claim-coupling (p), claim-tournament-cost (p), prop-3.2 (p), def-decode (n), claim-decode-cost (n), def-comparison (n), claim-comparison-state (n), claim-winner-dominates (p), def-verify (n), claim-verify (n), claim-error (n), claim-coherent-access (p). `lean/QuarticQuery/Paper/Section3.lean` holds candidate declarations from an earlier pass; check them first.

1. For each row, read the paper's text, its ties and notes in `corpus/ties.json`, the adjudication verdicts, the first round's proposals for it (`previous_round/*/NEW_STATEMENTS.json`, `LEAN_GAPS.md`), and the Lean modules that implement the step. Classify it: already stated under another name (prove the agreement); a few lines from existing declarations; a genuine new proof; or prose that should not be a theorem (say why).
2. Give the list-valued Proposition 3.2 exactly as the paper states it, proved from the existing ideal-process and sampler lemmas (`Tournament/Drift.lean`, `Tournament/Ideal.lean`, `Upper/Tournament.lean`). Give the comparison facts (complementarity, a_ii = 0, winner dominance with probability at least 1 - epsilon) as statements about the actual Lean comparison procedure.
3. For every row that should be a theorem, write the exact Lean statement in the vocabulary of `Statement.lean` and the existing modules, and its proof, as Lean files `lean/QuarticQuery/Paper/Quantum*.lean` in namespace `QuarticQuery.Paper`, each declaration with a doc comment beginning `Ledger: <row id>`. Use only declarations present in `repository/lean/` or Mathlib at the pinned revision, named exactly. Write proofs a compiler will accept: explicit `have` steps and named lemmas. Label every file "unelaborated" unless you compiled it.
4. Order the work by value to a reader: Proposition 3.2, Lemma 3.1's use, the comparison and verification facts, the error bound, then displays and definitions.

## Return one ZIP containing

- `lean/`: your Lean files at their module paths.
- `blueprint.md`: one entry per row: class, the statement in mathematics, the Lean statement, the proof plan naming the declarations used, and any correction.
- `coverage_plan.json`: one object per row with `id`, `class`, `declaration`, `uses`, `difficulty`, `compiled`, `notes`.
- `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
