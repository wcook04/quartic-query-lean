# Round-nine exposition revision

The maintained [exposition](../../docs/exposition.md) now teaches the two operations that carry the separation: generating the exact successful pivot law with a capped quantum routine, and turning a whole-run light cell visit into a capped classical predictor. Its theorem remains the fixed-parameter result: choose an exponent below four, fix a suitable integer `k`, then grow `m` through powers of four. No Lean theorem was changed.

## Review coverage and decisions

The [disposition file](round9_dispositions/exposition.json) binds all 135 new `EX9001`–`EX9135` findings to the exact baseline at `7772e4f2b98149a38ed69b88397982620f94bdac` and to current quotations and line spans. The baseline SHA-256 is `ce1887b35542c06e98132ac843f12eb78e9c4c224e7fb49f8da96255c21b240e`. It also records all 164 EX rows in the exposition return's previous-round audit and all 18 exposition observations in the reasoning-record return's supporting audit, including `XP196`. Those historical assessments are not counted as new findings.

The main finding dispositions comprise 126 applied repairs or local alternatives and nine suggestions not adopted. The latter are `EX9030`, `EX9047`, `EX9056`, `EX9058`, `EX9069`, `EX9071`, `EX9088`, `EX9098` and `EX9103`. Each has an individual reason. In particular, an additional table is not automatically better than an exhaustive two-case rule, and another exercise need not improve a route that already tests the relevant causal implication. These are editorial judgments, not assertions that the suggested alternatives are mathematically invalid.

The returns remain evidence of simulated reader encounters, with their disclosed familiarity, retrospective recording and source-coverage limits. This revision does not establish improved human comprehension or a blind reader result. The supplied cross-document audit's historical request-author label and incomplete image-link inventory remain historical input facts; they are not silently repaired inside the preserved return. All four maintained exposition figures render. The unmatched closing brace after the BHMT bibliography entry was removed without changing that entry's content.

## What changed

The opening counts oracle calls, defines the varying Boolean arity and deterministic budget, separates quoted theorem strength from reconstructed constants, and states which constants may depend on `k`. The source of the integer condition `t ≥ 1` is explicit in the general finite setup. The phase-query eigenstate calculation now precedes its first use, with a block-to-full-input coordinate map. The nontrivial half-amplitude example is an attempt with a separately located answer.

The board section distinguishes derived addresses from input fields, retains explicit base/domain-bit/cycle names, shows why a true transcript at a wrong address still fails an output test, and keeps the gate check beside its concrete wire values. It displays all four summands in the local-test count. Historical AND–OR cost arithmetic follows the new quantum cost argument, and its claimed quantum regime and domain-certificate step are explicit.

The quantum route now includes:

- a visible initialize, sample/measure/append, stop, and verify loop;
- a two-label retained-workspace state whose measured flag has the classical mixture law;
- the coordinate rule for tensor products, before the two-pivot product calculation;
- the two reflection matrices and their multiplication in the ordered good/bad basis;
- the finite half-direct, half-bounded-uniform iteration schedule with fresh trials and an all-input cap;
- the argument that mixing iteration counts and selecting the first success preserve the same conditional label law;
- the two-ordinary-query implementation of a controlled read;
- separate one-input and zero-input error budgets, and one sum in bit-query units before enlarging logarithmic powers.

The classical route now gives the fixed-prefix reason for posterior uniformity, separates probabilistic early discoveries from deterministic late charging, and parses a cell-bit coordinate into its proposed address without reading input. The stopped simulator has named global and forwarded-query clocks, a stop-before-read rule and a total default output. A table executes both branches of the existing XOR example. The optional direct-product proof comes after its application, with a rejoin marker. The final mixture step displays the signed-gap expectation inequality.

Question 4 and its answer distinguish fixed-time events from their two-time union. If the changed branch later reads the second target bit, that whole branch is heavy and contributes zero; the remaining light-visit probability is `1/8`. No query is removed from the count. The exponent calculation uses integrality in place of an unnecessary second floor estimate and identifies the exact dependence of its ratio constant. The combined explanation prompt is separated from its rubric.

The formal-reading extension is explicitly optional. It explains statement-only challenge placeholders, maps the Option-valued winning clause to board fields, retains the distinction between existential family and explicit-circuit theorems, and explains the constant-factor equivalence between the cubic formulations. The old preparation-time source comment is described as historical, alongside later recorded evidence. No fresh proof run is inferred.

## Writing sources actually used

These sources informed concrete choices; they were not used as a numerical style target.

1. **Ronald de Wolf, _Quantum Computing: Lecture Notes_, supplied extracted edition**, Chapter 1, the tensor-product and measurement passages (extraction lines 63–95). Its order fixes the state space before interpreting probabilities. The revision follows that operation order: the two-label state retains orthogonal branches, and the tensor-product coordinate rule appears before multiplying win probabilities. The distinction between amplitudes and their squared norms is exercised using the existing half-amplitude input.
2. **The same notes, Chapter 7**, geometric and algebraic Grover analyses and amplitude amplification (extraction lines 956–1032). The inspected source moves from good/bad coordinates to two reflections, then to the angle recurrence, and states why the full preparation must be unitary. The exposition now performs the missing two-by-two multiplication, names the complete inverse workspace, and preserves the overshoot example. The source's unknown-success discussion is not misrepresented as the exact capped schedule: that schedule was read in the maintained record at `upper-grover-trial`.
3. **The supplied _Why the SK order parameter has no gaps_ expository exemplar**, opening and finite-model passage (`exemplars/expository.md`, lines 17–91 in the round-nine packet). The inspected opening identifies a concrete reconstruction task and distinguishes accepted deep inputs from local calculations; its first finite example defines the object before using it. This supports the separated route obligations, a local operation before tensor notation, and the explicit accepted trigonometric guarantee beside the bounded schedule. Its mathematical content and its examples were not imported into the quartic proof.
4. **The maintained lean-exposition `record-to-expository` skill and `docs/writing_method.md`**. The prescribed frame-before-examples and operation-level prerequisite ladder support retaining the exact target near the start while moving the detailed predecessor construction after the new mechanism. Their warning against substituting a prerequisite list for a performed operation is applied in the retained-state, reflection and simulator calculations.

Mathematical source readback included the record's `forr_circuit`, `forr_bs_translation`, `AC-coherent`, `upper-grover-geometry`, `upper-grover-trial`, `upper-explicit-log6`, `CL-early-late`, `CL-simulator-example`, `ROOT-GROWING-K`, and `R3-A-RESULT` passages; the unconditional challenge declarations and `construction_family_named` were inspected directly. These are claim and implementation checks, distinct from the writing comparisons above.

## Render and local validation

The existing `tools/render_papers.py` and TikZ figure family were reused. Figure 1 has larger, shorter payload labels; its long all-one annotation was moved into the existing caption to avoid crossing pointer lanes. Figure 3's pointer legend is closer to the cycle and calls them zero-reaching pointers. The board address labels were enlarged in the shared style, and Figure 4 uses more of the page width. The geometry, arrow meanings and stored mathematical data were preserved.

The local command was:

```sh
python3 tools/render_papers.py --paper exposition --output-dir /tmp/quartic-r9-exposition-render
```

The result is a 24-page PDF. All pages were inspected in contact sheets, with the changed figures, reflection matrices, simulator table and answers inspected at page size. The first-page AI disclosure footnote is visible. The winning-condition introduction stays with its list, the concrete gate setup stays with its first equation, and the complete Question 2 answer is together. No overfull boxes or undefined references were reported; the remaining renderer messages concern absolute temporary figure paths and an unused table-caption setup.

`git diff --check` passes on the owned manuscript, bibliography and figure paths. All 135 main, 164 prior-audit and 18 supporting-audit current quotations and line starts were checked against the final local source. The rendered receipt records exact source and PDF hashes. Final commit-pinned link rebinding and the release-directory render belong to integration; the receiving agent must inspect that final artifact. `make check`, staged layout validation, commit and push are also integration responsibilities. This editorial validation is not fresh Lean, Comparator or human-review evidence.
