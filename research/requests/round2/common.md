# {title}

## Context

Will Cook, an economics undergraduate, directs a project that turns AI-produced mathematics into checked, readable explanation. This packet concerns "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity" (OpenAI, 5 October 2026), included as `paper/quartic-query-separation.pdf` with line-numbered text in `paper/extracted.md`.

The whole of Theorem 1.1 is checked in Lean with no hypothesis: `QuarticQuery.alphaTot_eq_four_unconditional : alphaTot = 4` and `QuarticQuery.theorem_1_1_unconditional`. This includes our own proof of the Forrelation randomized lower bound in the weaker fixed-k form the separation needs (`QuarticQuery.ForrelationLower.bansalSinhaLower`). Comparator accepts five statement bundles against independently compiled challenges that import Mathlib only, and five deliberately wrong solutions are rejected for the intended reason. These runs are unsandboxed local rehearsals. No person has reviewed any of it; all review so far is by AI agents.

This is the second round. A first round of five returns produced a long reasoning record, a short expert paper, an examples-first exposition, a Forrelation route note and a reader plan. They are in `previous_round/`, and every finding in them has a verdict in `repository/research/adjudication/funnel_adjudication.json` (readable summary: `funnel_adjudication_notes.md`). Use the verdicts, not the returns' own conclusions. Since then:

- The statement record was corrected: `claim-bs-to-L` lost a wrong `exact` tie, the `lem-2.1.i` locator was fixed, the older conditional `theorem_1_1` now records its hypothesis.
- New Lean files state the preprint's named results directly (`repository/lean/QuarticQuery/Paper/Section2.lean`, `Section3.lean`, `Section4.lean`) and prove an explicit Forrelation lower bound uniform in k with a k^2 loss (`repository/lean/QuarticQuery/ForrelationLower/Uniform.lean`). `BUILD_STATUS.md` in this packet says which of these are compiled; treat any declaration it does not list as built as source text only.
- Two independent readings found that one inequality in Section 5.4 of Bansal and Sinha, arXiv:2008.07003v3 (main.tex line 1181), fails for every k >= 3: `repository/research/adjudication/bansal_sinha_section54_second_reading.md`. As written, their argument supports a slightly weaker logarithmic denominator. The preprint and our Lean proof do not depend on that display.

Read in this order: `READ_ME_FIRST.md`; `BUILD_STATUS.md`; `repository/README.md`; `repository/docs/statement_evidence_contract.md`; `repository/corpus/README.md`; then your job's sources. `repository/corpus/statements.json` has one record per statement of the preprint, with separate evidence fields (`formal_statement`, `build`, `comparator`, `route`, `reach`) and the Lean declarations tied to it. `repository/corpus/lean_dependencies.json` is the dependency closure read from the compiled environment of the headline theorem. `repository/lean/` is the full Lean source. `literature/` holds the cited and related papers from our annex: `extracted.md` is text extracted from the authors' TeX where we hold it, and `source.tar.gz`, where present, is the original arXiv source. Prefer the TeX for exact statements and locators.

This round builds the foundation for the final papers: Lean coverage of every statement of the preprint, an adversarial check of the formal definitions, and two research questions that could change what the papers say. The papers themselves come next round, written over the record this round completes. Seven packets run in parallel; yours is one of them, and the others cover the remaining sections, so stay inside your job.

Anything you write in Lean will be compiled by us with the pinned toolchain and Mathlib revision. A proof that compiles is worth far more than several that do not: prefer small lemmas with explicit intermediate statements, exact declaration names copied from the source, and tactics this codebase already uses successfully. When you are unsure of a Mathlib name, say so in a comment and give the statement you need.

The audience for any paper is a working theoretical computer scientist or mathematician who knows query complexity at the level of a graduate course. Write for that reader. Do not address or name any particular person.

{job}

## The evidence contract (applies to every return)

Lean is bound to statements, not to prose. Your writing may improve on the preprint's derivations, and we want that. Every claim a reader is asked to believe must stay traceable:

1. Each displayed statement in your text either matches a record in `corpus/statements.json` (cite its `id`) or is new. Put every new displayed claim in `NEW_STATEMENTS.json` with keys `id`, `statement`, `why_needed`, `depends_on`, `proposed_lean` (a Lean signature using only the vocabulary of `lean/QuarticQuery/Statement.lean` and already-proved declarations), and `route_note`. We will prove these in Lean.
2. If you change what a statement says, record it in `STATEMENT_CHANGES.json` with `id`, `old`, `new`, `relation` (`stronger`, `weaker`, `equivalent`, `corrected`) and `reason`.
3. `correspondence.json` maps passages of your text to evidence: a list of objects with `passage` (an anchor you place in the text as `<!-- passage:NAME -->`), `from` and `to` (the exact first and last few words of the passage), `role` (`states`, `defines`, `proves`, `explains`, `uses`, `mentions`), `statement_ids`, and `lean` (full declaration names from `statements.json` or the Lean source; empty when none).
4. `LEAN_GAPS.md` lists, in reading order, every displayed claim of yours whose Lean evidence is missing, partial, or by a different route, with the reason.
5. When the Lean proof of a step takes a different route from the preprint's (see each tie's `route`), say so once where the step is used. Never describe a proof as checked when only a nearby statement is.

You have no Lean compiler unless your environment provides one. If you write Lean, label every block "unelaborated" unless you compiled it, and then give the toolchain and command.

{boundary}
## Writing and claims

- Lead with the strongest result, at full strength, then its scope. State the open boundary once, after the result. Attribution is one plain clause where the earlier result is used.
- The preprint and its mathematics are OpenAI's. Credit every earlier result to its authors with an exact locator. Say "AI-assisted" honestly: begin each paper with the statement "**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them."
- "Nearly quartic" means exponent 4 - 2/k for each fixed k. Never write that a single family achieves a fourth power unless you have proved it, and then state exactly what was proved.
- Write ordinary mathematics in the problem's own notation. No em dashes. No contrast constructions of the form "not X, but Y" or "X rather than Y" as rhetoric. No taglines, no workflow nouns on the reading path (no "packet", "return", "trace", "corpus row" in a paper's prose), no inventory of counts in the prose. A symbol used once is inlined. Every named object is defined before use.
- Follow the four guides in `writing/`: `the-deliverable.md` first, then `mathematical-writing-mechanics.md`, `full-exposition-guide.md` and `register-from-literature.md`. `exemplars/` holds the three papers of an earlier project in the same series as models of form; they are about a different theorem.
- The intended reader cares about: the path up the mountain more than the summit; which steps an expert finds obvious and which need spelling out; one worked example over many charts; whether each formal statement says what the informal theorem says; and an author who stands behind every sentence.
- Separate what you verified from what you infer, and give a file and location or URL for every factual claim. "Not found" in a search is a search result, never a novelty claim. A finding about a published paper is stated as exactly what fails, where, and what still follows.
