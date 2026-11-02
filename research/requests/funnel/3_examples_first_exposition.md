## Your job: the examples-first exposition (exposition with exact small computations)

Write an expository paper, about 7,000 to 10,000 words, that a mathematically literate reader outside query complexity can follow, built on worked examples before general statements. The exemplar `exemplars/expository.md` shows the form; make this one better.

1. Open with a board small enough to compute by hand: a few columns, one winner, outward pointers to zeros, and an opponent whose address is garbage. Compute everything exactly. `research/returns/1_understand_the_paper/worked_examples.md` and its checker are a starting point; verify their numbers.
2. Build each idea from an example: a cyclic comparison table where no ordering exists and the weighted tournament still finds the winner (compute the expected weight drop exactly); why amplification keeps the conditional distribution of the sampled candidate; why conditioning on staying under a query cap can make a problem easier (the AND example); the planted input; and the exponent 4 - 2/k as k grows, with a table.
3. Then the theorem and the proof outline, stated exactly, each step pointing back to its example.
4. Every number and example you compute must be reproducible: include a standard-library Python script that recomputes all of them, and say which Lean declarations state the general facts each example instances.
5. Say what is checked and what is not in one short section, in plain words.

## Return one ZIP containing

- `exposition.md` with `<!-- passage:NAME -->` anchors; `references.bib`.
- `examples.py` (standard library only) and `examples_output.txt`.
- `figures.md`: a specification of each figure (what is drawn, exact data, caption), to be drawn by us.
- `correspondence.json`, `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
