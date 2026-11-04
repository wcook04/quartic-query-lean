# Reader-focused manuscript revision

This revision makes the three PDFs mathematical reading documents and keeps their verification history in a linked reference. It follows twelve sequential assessments, preserved as `research/returns/reader_{expert,exposition,record}_{01..04}.md`, and the user's explicit request to remove hashes, internal names, source paths and review machinery from the printed presentation. The [44 individual decisions](reader_focused_revision.json) distinguish adopted changes, already adequate passages, later withdrawals and suggestions rejected for this audience. Baseline: `071ce02`.

## What changed

The specialist companion retains its mechanism-first introduction and exact two reductions. Its abstract now describes reconstructed proofs without implying a new separation or leading with a formal-state qualification. Section 2 derives the circuit bound locally from word width, butterfly cost and the complete gate ledger. Appendix C gives the averaged Grover identity and the numerical success estimate. Appendix E derives the floor coefficient directly from integer-valued randomized complexity. Section 6 now explains mathematical proof routes and links the readable theorem index instead of printing status tables, internal identifiers and execution history.

The teaching exposition explains the optimal exponent before using its symbol, connects the eight-bit example to the exact five possible Forrelation values, and walks through the two Walsh butterfly layers that lead to Boolean arithmetic and transcripts. The local-test count now explicitly explains why the number of certificate cells does not enter verification cost. Section 5.1 carries the classical reduction continuously through the final contradiction. Section 5.2 then tests its hypotheses with the existing independent-selection example, AND conditioning example, two-clock XOR trace and cap/independence counterexamples. Every question and answer anchor remains. The certificate-complexity literature paragraph moves to the earlier-construction appendix, and the circuit appendix gives the full 5936-bit toy count. Section 7 offers readable formal theorem links and the mathematically relevant scope, without teaching source syntax or narrating checks.

The long paper is titled **OpenAI’s nearly quartic query separation: a complete proof reconstruction**, with a natural author/date line and abstract. It retains all substantive proofs: the total construction, exact circuit, bounded quantum procedures, capped classical reduction, independent Forrelation argument and universal quartic upper bound. The introduction ranks the reconstruction and uniform analytic control above convenient constants. Section 3.2 distinguishes the whole-cube Gaussian laws used to prove hardness from the promise-supported minimax law used to plant addresses. Section 6 states the budget hierarchy together. Section 7.3 distinguishes an explicit schedule and rate from the simpler diagonal existence consequence. Section 8.5 states the uniform analytic target before the details, and identifies the four decisive steps; §§8.8–8.9 name their existing zeroing and derivative-path invariants.

The construction figure is the actual existing `expert_column.svg`, reused before record §4.3 with a caption explaining outward pointers and malformed rivals. No new Gaussian-chain figure was fabricated. The existing three-block calculation supplies that explanation.

## Evidence relocation and navigation

The parent first preserved original record Appendices B, F and G in `docs/verification_details.md`. Their catalogue, dated checks, exact theorem types, qualifications and anchors remain available there. Original reference notes were also preserved, with historical prefixes on duplicate reference anchors. The printed record now has coherent appendices: A remains the universal upper bound; old C becomes B (references), old D becomes C (alternative threshold), and old E becomes D (technical comparisons). The external specialist companion still has its own Appendix E; a receiving check caught and corrected that one overbroad remapping before the renewed freeze.

Eleven further historical items preserve the finite-check narration and pointers removed from the mathematical body: circuit/board checks, comparison choices, separate-cap enumeration, planted toy, independent-selection control, simulator enumeration, Forrelation census, adversary-normalization checks, status of the gate-cost identity, Bansal–Sinha source coordinates, and the old authorship/review disclosure. Those extracts retain their original status and do not report new execution. They intentionally repeat no passage or claim identifiers.

`docs/proof_index_intro.md` contains fourteen natural-language entries. Main results pair specifications with substantial implementation links; supporting entries identify exact circuit certification, label sampling, tournament output, capped prediction and quartic-bound routes. The index explicitly distinguishes a specification's intentional placeholder from the separate checked proof. It also keeps the existential family theorem separate from the named family's explicit constants, and the measured-label route separate from full physical retained-state correspondence. The parent owns the generated complete source directory and machine-readable checking evidence.

The record's printed references now use natural author names and retain scholarly editions and mathematical locators, while removing hashes, extraction-line histories and operational notes. The same compact notes are in its BibTeX file. Short-paper bibliography notes no longer print source fingerprints. Source destinations and final binding remain the parent's responsibility.

## Paragraph-level author decisions

This is a bounded decision log for the changed passages, not a claim of blind reader testing or a new line-by-line validation of every unchanged proof.

| Passage | Reader's need and author decision |
| --- | --- |
| Expert abstract and contribution | Identify whose theorem is reconstructed and what this account supplies. Remove early evidence mechanics; keep original credit and quantitative scope. |
| Expert circuit construction | Recover the displayed size constant without opening another paper. Replace the sketch with the actual cost derivation. |
| Expert minimax paragraph | Know whether the hard law defines the function. State that it is a proof witness only. |
| Expert bounded amplifier | See why a fixed schedule succeeds. Add the finite average and its elementary bound, retaining all cases and the exact conditional law. |
| Expert uniform appendix | Recover the denominator. Add integer/floor arithmetic; leave the correct radical untouched. |
| Exposition opening and small experiment | Understand what the exponent means and why perfect tiny examples do not give the general decoder. Add these two local explanations, not another roadmap. |
| Exposition Walsh/transcript bridge | See how numerical transforms become locally testable Boolean values. Add two concrete butterfly layers and fixed-width arithmetic. |
| Exposition local-test count | Understand the apparent cost of an enormous array. Explain that only the selected cell is tested. |
| Exposition classical proof | Follow one complete reduction before inspecting failure modes. Move the existing examples intact after the contradiction. |
| Record ingredient contract | Distinguish analytic laws from planted promised inputs. Insert the minimax bridge where the contract is first consumed. |
| Record classical opening | Keep three different budgets straight. State their hierarchy in prose, with the aggregate simulator cap implying each separate cap. |
| Record growing parameter | Identify the extra content beyond fixed-k quantifiers. State explicit schedule/rate versus diagonal existence. |
| Record analytic opening | See the strongest destination and four indispensable steps before constants. Add the uniform target and proof spine; preserve the complete derivations. |
| Formalization sections and references | Follow mathematics first and inspect exact evidence on demand. Replace printed identifiers/history by natural theorem links and scope. |

## Mathematical and source readback

The mathematical-reasoning method preceded prose revision. The portable exposition deep guides had been read in the preceding pass; their principles were applied with the current graph-to-long owner refreshed. Source truth and the user's requested separation of mathematical prose from evidence govern the result. No new word-list score or comprehension metric selected the edits.

Author readback covered the changed mathematical passages and their dependencies: the exact headline type, the named-circuit family, the uniform Forrelation theorem, actual Walsh/circuit cost definitions, the finite census, the bounded-amplification geometry, original-law capped prediction, the analytic endpoint/path invariants and the fixed/growing-parameter arithmetic. This does not claim a fresh complete reading of the entire Lean tree, literature annex or every unchanged ordinary proof. The parent independently enumerated the small Walsh instance and checked the schedule values described in feedback.

The headline specification retains all three clauses: optimal exponent, universal quartic bound and same-circuit fixed-parameter family. Explicit six and $1/400$ remain a separate named-family result. Source-file inclusion does not imply a separate statement comparison. The physical successful-state correspondence remains narrower than the ordinary retained-state argument; the Boolean theorem needs the exact measured-label law instead. No Lean source, theorem assumption, algorithmic cap or error convention changed in this pass.

The alleged square-root error was withdrawn by the later review: the actual schedule is `floor(sqrt(t/20))`. The uniform growing-parameter calculation uses a different allowance from the fixed-k threshold. At the initial admissible parameters its exponent estimate can be trivial; that limitation was already explicit and remains so. Scores and reports that no fatal error was found are not mathematical acceptance evidence.

## Author validation and receiving work

At author freeze, `git diff --check` passed for the owned manuscript and bibliography paths. Both shorter papers retain every baseline explicit anchor. The record plus supplement retains every old explicit anchor, passage identifier and claim identifier, with no duplicate passage identifiers. Existing repeated claim markers between the catalogue and proofs are intentional. The proof-index reference labels were checked against the existing source registry; the winning-condition label is supplied by the exposition registry.

A source scan excluding URLs, HTML markers and generated link definitions found no visible source hash, receipt/Comparator/packet/checker terminology, dotted Lean identifier or obsolete Appendix F/G reference in the manuscripts. This is a narrow text check, not a substitute for reading the rendered PDFs. Mathematical uses of “recorded” for query transcripts and “round” for an algorithm are legitimate and were not removed indiscriminately.

The papers, bibliographies, authored index introduction and supplement were frozen for the parent to bind, render and inspect. Final PDF acceptance, metadata, link targets, figure/table adjacency, source-map adaptation, register comparison and regression checks are receiving tasks. This author note does not claim them complete, a fresh Lean build, external referee validation or measured reader comprehension. No commit was made by the manuscript author.

Receiving rendering also caught a missing TeX command separator after the replacement of literal quantum-budget code by prose. The expression now reads `\iff q`; a scan of command names in changed prose found no similar concatenation. The correction was made before final binding.
