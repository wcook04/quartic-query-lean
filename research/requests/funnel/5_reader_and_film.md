## Your job: the reader's map and the film (exposition design; no new mathematics required)

Design the explanation layer that sits over the checked corpus: how a reader moves from one sentence to the Lean declaration and back, and a film that a presenter delivers.

1. Levels. Write the explanation at five levels: one sentence; one paragraph; one page; an argument map whose nodes are statement ids from `corpus/statements.json`; and a reading route through the paper's sections. Each level must lead with one concrete example and must say what is novel and why it matters. Choose what an expert finds obvious and what must be spelled out, and say why for each choice.
2. Argument map. Give the map as data: nodes (statement ids, a plain label, the evidence fields from `statements.json`), edges (`supports`, with a one-line reason), and the reading order. Mark the hardest steps and the places where the Lean route differs.
3. Statement fidelity, made visible. Design how the reader sees, for any statement, the exact Lean statement beside the paper's sentence, the Comparator verdict, and the remaining risk that a definition says something else. Use `docs/statement_fidelity_review.md`.
4. Film. A twelve-minute film script for a presenter, Will Cook, speaking to camera with visuals, built on one worked example from start to finish, ending with what is checked and what is not. Then a four-minute script on how the checking works: statement bundles, wrong solutions rejected, and what a Lean proof cannot tell you. For every shot give the spoken words, the picture with exact data, and the statement ids it relies on.
5. Data contract. Map each level to the files in `corpus/` and state any field the reader needs that the corpus lacks.

## Return one ZIP containing

- `levels.md` and `levels.json` (the five levels as data); `argument_map.json`.
- `fidelity_view.md`: the design for showing statement fidelity.
- `film_12min.md` and `film_4min.md`: scripts with shot lists.
- `data_contract.md`; `correspondence.json`, `NEW_STATEMENTS.json`, `LEAN_GAPS.md` as specified above.
