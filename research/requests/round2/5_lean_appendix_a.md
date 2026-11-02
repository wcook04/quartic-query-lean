## Your job: Lean for Appendix A (the universal quartic upper bound)

The preprint's Appendix A proves the universal bound D(f) = O(Q(f)^4) through Lemmas A.2 (the nonnegative spectral adversary), A.3 (block sensitivity against spectral sensitivity), A.4 (Huang's signed hypercube) and A.5 (the maximal-monomial algorithm, Midrijānis's D <= bs · deg). Our Lean development imports the consequence from complexitylib (`lean/QuarticQuery/Appendix/TheoremA1.lean`, constant 20736 = 12^4) and states none of the lemmas. `complexitylib/Complexity/Computability/QueryComplexity/` in this packet holds the library's source, including `Huang.lean`, `Midrijanis.lean`, `SpectralSensitivity.lean`, `SensitivityBounds.lean`, `Degree.lean`, `NisanSzegedy.lean` and `Quantum/`.

Work list (all none unless marked p): def-deg, def-bs, def-Gamma-i, claim-perron, def-adv-progress, claim-per-query, claim-final-overlap, lem-A.2 (p), def-Sf, lem-A.3.bs, lem-A.3.lambda, lem-A.3, claim-restrict-parity, def-huang, claim-huang-spectrum, claim-interlace, lem-A.4, claim-round-block, lem-A.5.

1. Map each row onto complexitylib: give the exact library declaration that states it (file and name), or the closest one, and the precise difference (model, normalisation, constant, hypothesis). Read the library's definitions of degree, block sensitivity, sensitivity, spectral sensitivity and its quantum model, and compare each with the paper's, with locators.
2. For each row that the library states in another form, write a bridge theorem in our vocabulary (`Statement.lean`, the bridges in `lean/QuarticQuery/Bridge/`), with its proof. For each row the library lacks, write the statement and a proof, preferring the paper's route; say where the library proves the same consequence differently.
3. Assemble the paper's Theorem A.1 from Lemmas A.2 to A.5 in Lean as a second route alongside the imported one, so a reader can check the appendix as written. Track the constant your route gives.
4. Write the Lean as files `lean/QuarticQuery/Paper/AppendixA*.lean` in namespace `QuarticQuery.Paper`, each declaration with a doc comment beginning `Ledger: <row id>`. Use only declarations present in `repository/lean/`, `complexitylib/` or Mathlib at the pinned revision, named exactly. Label every file "unelaborated" unless you compiled it.

## Return one ZIP containing

- `lean/`: your Lean files at their module paths.
- `blueprint.md`: the library map, then one entry per row: class, the statement in mathematics, the Lean statement, the proof plan, and any correction or locator fix.
- `coverage_plan.json`: one object per row with `id`, `class`, `declaration`, `library_declaration`, `uses`, `difficulty`, `compiled`, `notes`.
- `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above; `references.bib`.
