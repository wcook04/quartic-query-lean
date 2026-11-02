# {title}

## Context

Will Cook, an economics undergraduate, directs a project that turns AI-produced mathematics into checked, readable explanation. This packet concerns "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity" (OpenAI, 5 October 2026), included as `paper/quartic-query-separation.pdf` with line-numbered text in `paper/extracted.md`.

The whole of Theorem 1.1 is now checked in Lean with no hypothesis: `QuarticQuery.alphaTot_eq_four_unconditional : alphaTot = 4` and `QuarticQuery.theorem_1_1_unconditional`. This includes our own proof of the Forrelation randomized lower bound, which the preprint imports from Bansal and Sinha, in the weaker fixed-k form the separation needs. Comparator accepts five statement bundles against independently compiled challenges that import Mathlib only, and five deliberately wrong solutions are rejected for the intended reason. These runs are unsandboxed local rehearsals. Statement fidelity and the new lower-bound route have been read by AI reviewers only; no person has reviewed any of it.

Read in this order: `READ_ME_FIRST.md`; `repository/README.md`; `repository/docs/statement_evidence_contract.md`; `repository/corpus/README.md`; then your job's sources. `repository/corpus/statements.json` has one record per statement of the preprint, with separate evidence fields (`formal_statement`, `build`, `comparator`, `route`, `reach`) and the Lean declarations tied to it. `repository/lean/` is the full Lean source. `repository/docs/` holds the fidelity review, the lower-bound blueprint, its independent reading and the prior-art search.

The audience for any paper is a working theoretical computer scientist or mathematician who knows query complexity at the level of a graduate course. Write for that reader. Do not address or name any particular person.

{job}

## The evidence contract (applies to every return)

Lean is bound to statements, not to prose. Your writing may improve on the preprint's derivations, and we want that. Every claim a reader is asked to believe must stay traceable:

1. Each displayed statement in your text either matches a record in `corpus/statements.json` (cite its `id`) or is new. Put every new displayed claim in `NEW_STATEMENTS.json` with keys `id`, `statement`, `why_needed`, `depends_on`, `proposed_lean` (a Lean signature using only the vocabulary of `lean/QuarticQuery/Statement.lean` and already-proved declarations), and `route_note`. We will prove these in Lean.
2. If you change what a statement says, record it in `STATEMENT_CHANGES.json` with `id`, `old`, `new`, `relation` (`stronger`, `weaker`, `equivalent`, `corrected`) and `reason`.
3. `correspondence.json` maps passages of your text to evidence: a list of objects with `passage` (an anchor you place in the text as `<!-- passage:NAME -->`), `from` and `to` (the exact first and last few words of the passage), `role` (`states`, `defines`, `proves`, `explains`, `uses`, `mentions`), `statement_ids`, and `lean` (full declaration names from `statements.json` or the Lean source; empty when none).
4. `LEAN_GAPS.md` lists, in reading order, every displayed claim of yours whose Lean evidence is missing, partial, or by a different route, with the reason.
5. When the Lean proof of a step takes a different route from the preprint's (see each tie's `route` and the README), say so once where the step is used. Never describe a proof as checked when only a nearby statement is.

{boundary}
