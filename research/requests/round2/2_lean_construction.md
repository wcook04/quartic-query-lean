## Your job: Lean for Sections 1 and 2 (query models, Forrelation, the construction)

We want every statement of the preprint to have a Lean declaration that says exactly what it says. Your rows are Sections 1 and 2: the query models, the Forrelation promise and its quantum test, the exact circuit, the column layout, transcripts, winners and local tests. Their current status is in `corpus/statements.json`; `skeleton/record_skeleton.md` shows which declarations already carry them.

Work list (status in brackets: n none, p partial, u unassessed): def-log-convention (n), def-partial-query (p), def-query-oracle (p), eq-1 (n), eq-2 (p), def-transcript (p), def-walsh-sign (p), eq-3 (p), eq-4 (p), eq-5 (n), claim-bs-to-L (u), claim-proj-prob (p), lem-2.1.ii (p), claim-N-phi (p), claim-integer-tests (p), claim-circuit-size (p), lem-2.1 (u), eq-6 (p), def-column-layout (p), eq-7 (p), eq-8 (n), def-winner (n), cor-unique-winner (u), def-win-at-address (n), def-K (p), lem-2.2.i (p), lem-2.2.ii (p), lem-2.2 (u), cor-local-dichotomy (u). Rows marked u already have candidate declarations in `lean/QuarticQuery/Paper/Section2.lean`; check whether they state the row exactly, and repair them if not.

1. For each row, read the paper's text, every tie and note in `corpus/ties.json`, the adjudication verdicts, and the first round's proposals for it in `previous_round/*/NEW_STATEMENTS.json` and `LEAN_GAPS.md`. Classify it: a definition already present under another name (prove the two agree, or show they are the same constant); a statement a few lines from existing declarations; one needing a genuine new proof; or prose that should not be a theorem (say why in one sentence).
2. For every row that should be a theorem, write the exact Lean statement in the vocabulary of `lean/QuarticQuery/Statement.lean` and the existing development, and its proof. Use only declarations that exist in `repository/lean/` or in Mathlib at the pinned revision (`lean/lake-manifest.json`), and name them exactly. Where the paper's statement is false or imprecise as written (as Lemma 2.2(i) was), state the corrected version and the reason.
3. Write the proofs as Lean files, `lean/QuarticQuery/Paper/Construction*.lean` in namespace `QuarticQuery.Paper`, each declaration with a doc comment beginning `Ledger: <row id>` and one sentence on whether it is verbatim or corrected. Prefer short proofs from existing lemmas. Write proofs a compiler will accept: explicit `have` steps, `simp only [...]` with named lemmas, no reliance on automation you have not seen work in this codebase. Label every file "unelaborated" at the top unless you compiled it.
4. Order the work by value to a reader checking the paper: Lemma 2.1 and its parts, Lemma 2.2 and its parts, the corollaries, then the displays, then definitions.

## Return one ZIP containing

- `lean/`: your Lean files at their module paths.
- `blueprint.md`: one entry per row in the work list: class, the statement in mathematics, the Lean statement, the proof plan naming the declarations used, and any correction.
- `coverage_plan.json`: one object per row with `id`, `class`, `declaration`, `uses`, `difficulty` (`trivial`, `short`, `substantial`), `compiled` (true or false), `notes`.
- `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
