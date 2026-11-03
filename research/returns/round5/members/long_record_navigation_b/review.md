# Located review findings

This is a readable rendering of `findings.json`, which is authoritative. Source paths refer to the supplied packet unless explicitly identified as files in this return. See `sources_read.md` for reading coverage and limits.

## High priority

### LR-001 — 1.1. Certificates that disqualify every other candidate — Dependencies and proof recovery

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `high`

**PDF page:** 3

**Exact current-source quotation:**

> **Dependencies and proof recovery.**

**Finding:** The supplied 116-page record PDF does not preserve the Markdown's internal proof navigation. Its 137 link annotations consist of 130 URI actions and seven external-PDF actions, with no internal GoTo or direct destination link actions. None of the 339 explicit Markdown IDs is present as a named PDF destination. The dependency table on page 3 and the catalogue's Argument references, including pages 91 and 108, therefore display destinations without clickable internal routes. The PDF has 79 outline entries, so it is readable, but the outline does not replace the promised passage-level links. This is independent of the disclosed one-paragraph Markdown/PDF revision difference.

**Reader impact:** A researcher who downloads the record to follow a companion proof cannot jump from its dependency map or catalogue to the relevant argument. The failure affects the main purpose of this long reference document even though the Markdown anchors all exist.

**Suggested direction:** Preserve the existing explicit passage IDs and internal links in the PDF conversion, then check the dependency table and representative catalogue Argument links in the actual output. Retain the working outline as an additional navigation route.

**Evidence:**

- repository/docs/reasoning_record.md, #record-dependencies, and Appendix B Argument references.
- repository/docs/reasoning_record.pdf: complete annotation/destination inventory; pages 3, 91 and 108 sampled directly. Diagnostic details are in evidence/pdf_navigation.json in this return.
- For comparison only, the supplied SK long-record PDF has 42 internal GoTo actions, all with existing named destinations. This establishes a useful rendering pattern, not any mathematical connection between the results.

### LR-002 — 2.7. What the formal models establish

**Paper:** `reasoning_record` · **Category:** `lean_link` · **Severity:** `high`

**Exact current-source quotation:**

> The complete declaration `theorem_1_1_unconditional` packages the common-circuit eventual family in the integer form

**Finding:** The record names the implementation theorem but supplies no direct link to the exact compared statement, solution wrapper or configuration. The actual configured name is QuarticQuery.Checked.theorem_one_one. No QuarticQuery.Checked name, Challenge.lean link, Solution.lean link or comparator_map link appears anywhere in the current record. The same distinction is obscured when §3.16 says that a receipt explicitly lists the implementation name bansalSinhaLower: the receipt contains both configured and scanned implementation names. A reader arriving here cannot determine exact comparison membership from the record alone without reconstructing joins across JSON files.

**Reader impact:** A quantum-query expert following Theorem 1 into the formal evidence needs to inspect the asserted type and its definitions. Having to discover wrapper names in machine records defeats the promised short statement audit and risks treating receipt membership as configured-target membership.

**Suggested direction:** At the formal entry point, show a compact mapping from each central prose claim to its exact compared target, statement source, Solution wrapper and configuration. Link the existing 343-line statement file. Keep implementation names as a secondary route. Use the successful expert Appendix A as the model; no new proof is needed.

**Evidence:**

- repository/docs/reasoning_record.md, §2.7, paragraph beginning For fixed k; §3.16, #forr_validation_scope; §7.3.
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:328–334; Solution.lean:21–31; comparator.json/theorem_names.
- repository/corpus/comparator_map.json/declarations/QuarticQuery.Checked.theorem_one_one; note on solution_proof_reference explicitly says that the join is textual.
- repository/corpus/receipts/comparator-Unconditional-2026-11-02T212245429608+0000.json/declarations contains four Checked targets and four implementation names; actual configuration selects only the four Checked targets.
- repository/docs/expert_companion.md, Appendix A, The four compared theorems and Five things to check.

### LR-003 — 5.5 The contradiction and the constants

**Paper:** `expert_companion` · **Category:** `structure` · **Severity:** `high`

**Exact current-source quotation:**

> Full proof: [record §6]

**Finding:** The link labelled as the full lower-bound proof lands at #CL-discrepancy, section 6.6, where the record combines three already-established inequalities. It passes over the direct product, coupling, erased-zero identity, and capped simulator. It also starts with the coarser zero-search bounds; the m+1 refinement used in the companion is earlier at #CL-zero-optional.

**Reader impact:** Drucker/Shaltiel and cheat-sheet readers following the link to inspect adaptivity or the hidden address arrive after the very mechanisms they need to check and must reconstruct the route backwards.

**Suggested direction:** Distinguish the full section entry from the final discrepancy assembly and add direct routes to the erased-zero and simulator arguments already present in the record.

**Evidence:**

- expert_companion.md, section 5.5, line 239; LINK_MAP.json entry 2 (zero-based).
- reasoning_record.md, #CL-discrepancy, lines 3644–3661; #CL-direct-product-statement, line 2851; #CL-zero-optional, lines 3536–3553; #CL-simulator, line 3569.

### LR-004 — Overview

**Paper:** `exposition` · **Category:** `structure` · **Severity:** `high`

**Exact current-source quotation:**

> Full proofs of every step are in the [long reasoning record]

**Finding:** The exposition provides only one direct record link, to the top of a 5,945-line Markdown file. Its eight substantive later proof locators are plain text, including the circuit, Forrelation, amplification state, query count, direct product, zero search and Appendix A. The crucial capped-simulator paragraph has no direct proof locator of its own.

**Reader impact:** Strong students and researchers checking a single step cannot use the exposition as an index into the longer argument; they must leave their place and search a large second document.

**Suggested direction:** Turn the existing proof locators into exact section or passage links, using the record’s stable IDs. Give the capped simulator its own link; retain the global overview link.

**Evidence:**

- exposition.md, lines 48, 125, 131, 188, 191, 218, 227, 229, 234, 264.
- LINK_MAP.json entry 51 is the only direct exposition-to-record link; independently enumerating the current Markdown found no omitted record link.
- Existing targets include #forr_circuit, #forr_target, #upper-explicit-log6, #upper-returned-register, #CL-erased-zero-identity, #CL-direct-product-statement, #CL-simulator and #R3-A-RESULT.

### LR-005 — Appendix A. Checking the statement — What Comparator establishes

**Paper:** `expert_companion` · **Category:** `lean_link` · **Severity:** `high`

**Exact current-source quotation:**

> [its parts][cmp-lemma22]

**Finding:** This link does not lead to separately compared versions of Lemma 2.2(i) and (ii). It leads to Construction/Challenge.lean, whose four target theorems state winner uniqueness, unique gate-consistent transcripts, no incoming zero to a winner, and the winner finding a rival zero. None states the complete local-test equivalence together with the adaptive or coherent query bounds. The full ConstructionFull target does contain those clauses. Calling the four helper theorems “its parts” gives them the wrong mathematical role.

**Reader impact:** A reader checking the key adaptive/coherent local-test lemma will find four true but different claims. The wording makes exact comparison coverage look broader than the displayed target types show.

**Suggested direction:** Name the four construction helpers as helpers, and reserve part-(i)/part-(ii) labels for declarations that actually state those parts. Keep the link to the existing full conjunction.

**Evidence:**

- repository/docs/expert_companion.md, Appendix A: sentence beginning Besides the four theorems.
- repository/docs/lean_links.json/links/cmp-lemma22 targets lean/QuarticCorpus/Construction/Challenge.lean without a line fragment.
- repository/lean/QuarticCorpus/Construction/Challenge.lean:326–342 lists winsAt_unique, existsUnique_gateConsistent, winner_no_incoming_zero and winner_finds_zero.
- repository/lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean:25–60 contains the count, test equivalence, adaptive depth, coherent implementation and physical cap.

### LR-006 — Expert companion 5.2 Planting a winner; exposition 2 One column, then four and 5 The classical lower bound

**Paper:** `both` · **Category:** `figure` · **Severity:** `high`

**Exact current-source quotation:**

> The two coupled inputs. They differ only at the erased zero

**Finding:** Three image targets in the current Markdown are absent from the archive and absent from LINK_MAP.json: expert_planted.svg, exposition/fig2_board.svg, and exposition/fig4_planted.svg. The supplied map reports zero problems but omits these references. The supplied PDFs do contain these figures; this is a missing-source-asset problem for Markdown readers and reproducibility. All three captions contain nested square brackets, so an enumeration that cannot parse nested label brackets is insufficient.

**Reader impact:** Pointer-function and lower-bound readers using the Markdown lose precisely the board and coupled-input illustrations that explain which bits change. A reader trusting the link map would not discover that the supplied Markdown cannot reproduce those figures.

**Suggested direction:** Restore the already-requested figure assets and regenerate the link inventory from all actual Markdown references, including labels containing bracketed coordinates. Validate the resulting Markdown/PDF navigation separately.

**Evidence:**

- expert_companion.md, line 187, figures/expert_planted.svg.
- exposition.md, line 97, figures/exposition/fig2_board.svg; line 205, figures/exposition/fig4_planted.svg.
- Independent enumeration gives 77 inline/reference-definition destinations; LINK_MAP.json lists 74. The three extra targets do not exist among the extracted 162 members. This is an asset-completeness defect, not a ZIP CRC failure.

### LR-007 — 3.17. The complete Forrelation ingredient

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `high`

**Exact current-source quotation:**

> The same partial function
> $P_{k,m}$ defined in §3.1 has the following three properties.

**Finding:** The construction’s complete input interface appears only after the long independent hardness reconstruction and two literature comparisons. Section 1.1 already tells construction readers to combine §§3.1–3.5 with §3.17, so the intended route requires a substantial forward jump and then an immediate continuation to §4. The three properties, their common witnesses, and the permitted thresholds should be available before a reader is asked to decide which proof recovery to undertake.

**Reader impact:** Cheat-sheet and pointer-function experts chiefly need the exact partial-function contract before inspecting the new total construction; burying its conjunction makes them assemble the interface from separated pages.

**Suggested direction:** Make the existing three-part ingredient the entry statement for §3, with separate routes to promise/circuit details and optional hardness recovery. Preserve the existing stable destinations as aliases if material is moved.

**Evidence:**

- record §1.1, Dependencies and proof recovery; §3.17, numbered properties 1–3; §4 introduction explicitly consumes §3.17.
- The current §3 spans 1,335 Markdown lines and 9,501 whitespace-delimited words; this is a navigation-size observation, not a suggested deletion of its proofs.

## Medium priority

### LR-008 — 3. Where a natural shortcut fails, Table 1, row 2

**Paper:** `expert_companion` · **Category:** `error` · **Severity:** `medium`

**Exact current-source quotation:**

> each with probability $1$, or any pair at exactly $1/2$

**Finding:** The deterministic three-cycle is offered as an alternative counterexample to treating comparisons as bounded-error queries to a fixed tournament. A three-cycle is itself a legitimate fixed tournament, and its edge directions are computed exactly in this example. It refutes imposing a total order, not using a fixed tournament. The separate probability-1/2 example does refute bounded-error evaluation of a fixed edge. This is a local counterexample-label error; it does not invalidate the fractional-weight proof.

**Reader impact:** King-finding and tournament authors will immediately distinguish an arbitrary fixed tournament from a transitive ordering. Conflating them weakens the table intended to show why those results do not apply directly.

**Suggested direction:** Separate the no-total-order point from the no-fixed-bounded-error-edge point, and attach each existing example to the property it actually violates. Retain both examples.

**Evidence:**

- expert companion §3 Table 1 row 2.
- record §5.2, upper-comparison-model explicitly allows cycles; upper-bounded-error-comparison distinguishes the fixed-predicate guarantee; upper-cyclic-example illustrates absence of a total ordering.
- paper/source.pdf, §3 opening and §3.2, PDF pages 7–9: arbitrary comparison probabilities and complementary edges are separate from a total order.
- evidence/local_counterexample_checks.json: the three-cycle has zero diagonal and complementary off-diagonal entries, and is a valid fixed tournament.

### LR-009 — 4 The quantum algorithm: a tournament — Remark: a returned state versus a measured label

**Paper:** `exposition` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> The rotation argument in the box above shows

**Finding:** The paragraph cites record §5.5 for the assertion that successful amplification returns the full normalized good state. That section is formal correspondence and state-specification discussion. The ordinary state-return proof is in §5.1, including #upper-returned-register. The present locator sends a reader seeking the mathematical proof to evidence history instead.

**Reader impact:** Amplitude-amplification readers trying to distinguish a preserved quantum state from a correct classical label must find the designated-register argument themselves; the incorrect destination obscures an otherwise carefully explained distinction.

**Suggested direction:** Point the mathematical state-return assertion to the existing §5.1 proof and returned-register passage. Use a separate formal-correspondence link only for the evidence question.

**Evidence:**

- exposition.md, line 191, ends the state-return assertion with “(record §5.5)”.
- reasoning_record.md, §5.1, #upper-amplification-statement (line 2189) and #upper-returned-register (line 2294); §5.5 begins “Formal correspondence and the remaining state specification” at line 2800.

### LR-010 — 2.8. Execution evidence and checks of meaning

**Paper:** `reasoning_record` · **Category:** `notation` · **Severity:** `medium`

**Exact current-source quotation:**

> Theorem and equation numbers refer to the OpenAI preprint; section numbers refer to this record unless another source is named.

**Finding:** The blanket equation-number convention is inaccurate for the visible record. The Forrelation proof has local tags (F1)–(F60), the construction has (4.1)–(4.19), the direct-product proof has (6.1)–(6.11), and Appendix A has (A.1)–(A.11). Section 6.1 explicitly identifies local (6.4) with preprint (16), while Section 5 refers to preprint equation numbers without putting those numbers on its displays. The convention is also buried in execution evidence rather than mathematical navigation.

**Reader impact:** Authors checking their cited lemma, and readers returning from a short-paper reference to an equation, can search the wrong numbering system or mistake a reconstruction display for an original one.

**Suggested direction:** State the actual local-versus-preprint convention before the proofs and provide a compact crosswalk for the displays cited by the companion. Use one visible convention consistently.

**Evidence:**

- record §3.6, tags F1–F5; §4.1, tags 4.1–4.2; §6.1, equation 6.4 and the sentence identifying it as preprint (16); §5.2, the display called equation (13).

### LR-011 — 1.1. Certificates that disqualify every other candidate — links to earlier drafts

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `medium`

**PDF page:** 3

**Exact current-source quotation:**

> The earlier [short expert draft]

**Finding:** Seven PDF links have been converted from source-directory destinations into nonexistent files ending in /.pdf. The two historical draft links on page 3 target 2_short_expert_paper/.pdf and 3_examples_first_exposition/.pdf; the other five occur on pages 21, 44 and 87. All seven paths are absent. Their represented source directories do exist, so the Markdown reading-closure check does not detect this PDF-specific failure.

**Reader impact:** A reader opening an example checker, finite calculation or earlier draft from the PDF receives an unusable file destination, despite the packet's successful source-link checks. This interrupts evidence inspection as well as reading navigation.

**Suggested direction:** Give each directory link an actual document or index-file destination and preserve that destination correctly in the PDF. Test rendered link actions separately from source target existence.

**Evidence:**

- repository/docs/reasoning_record.pdf, external GoToR annotations on pages 3 (two), 21 (one), 44 (two) and 87 (two).
- evidence/pdf_navigation.json lists all seven exact targets and their failed relative-file existence checks.
- READING_LINK_CLOSURE.json represents the original directories, not these generated /.pdf paths.

### LR-012 — 5.4 The planted cell; also 5.2 Planting a winner

**Paper:** `expert_companion` · **Category:** `structure` · **Severity:** `medium`

**PDF page:** 8

**Exact current-source quotation:**

> ### 5.4 The planted cell

**Finding:** The headings for sections 5.2 and 5.4 are printed as literal ### text attached to the preceding paragraph in the supplied PDF, and both are absent from its outline. In the current Markdown these are the two subsection headings without a preceding blank line. They mark the planting construction and capped-simulator argument, so the lost hierarchy obscures two important proof destinations.

**Reader impact:** A reader moving from the erased-zero proof to the true-cell proof can miss the change of mechanism; a PDF reader using bookmarks cannot reach these two subsections directly.

**Suggested direction:** Make these headings parse as headings under the actual publication renderer and check both their visual hierarchy and their PDF outline entries after rendering.

**Evidence:**

- repository/docs/expert_companion.md, lines 183 and 212: 5.2 and 5.4 immediately follow prose without a blank line.
- repository/docs/expert_companion.pdf, pages 7 and 8: extracted literal ### markers, with page 8 visually confirmed; outline omits both headings.
- evidence/pdf_navigation.json records the literal text and missing outline entries.

### LR-013 — 4. The quantum upper bound — amplification proof sketch

**Paper:** `expert_companion` · **Category:** `lean_link` · **Severity:** `medium`

**Exact current-source quotation:**

> the amplified procedure returns the original register in the normalised successful state

**Finding:** The attached Lean-statement link highlights only UniformAmplifier/Challenge.lean:17–20, ending at let M := iterationBound γ. It excludes the query cap, the retained-state factorization and every success/failure clause that the sentence asks the reader to check. The full-construction link has the same problem: its selected range 14–41 stops at let _ := instZ, before the coherent-evaluation and physical-cap clauses ending at line 60. Both targets exist; the chosen excerpts are incomplete.

**Reader impact:** A specialist is following these links precisely to inspect the delicate returned-state and coherent-oracle assertions. The highlighted ranges contain the names and binders but not the claims, forcing an unguided search down the file.

**Suggested direction:** Extend the two link ranges through the complete theorem types, or link to clearly labelled subclauses in addition to the full type. The necessary source already exists.

**Evidence:**

- repository/docs/lean_links.json/links/cmp-amplifier: lines [17,20]; UniformAmplifier/Challenge.lean:27–29 (cap), 37–48 (factorization and success law), 52 (end of type).
- repository/docs/lean_links.json/links/cmp-lemma22-full: lines [14,41]; ConstructionFull/Challenge.lean:42–60 completes the physical conclusion.
- The same cmp-amplifier reference is used in repository/docs/exposition.md, §7.

### LR-014 — 7. The exponent — Remark (one explicit sequence)

**Paper:** `expert_companion` · **Category:** `lean_link` · **Severity:** `medium`

**Exact current-source quotation:**

> the [quantum budget][src-budget] it uses is built in Lean but has not been compared

**Finding:** The growing-k remark needs the explicit envelope 2^53 k 2^(10k), but its quantum-budget link highlights budget_le:86–90, whose right side contains only the opaque budgetConst k. The highlighted statement does not expose the essential dependence on k. The supplied file already has budgetConst_le_exponential and Q_Fkm_le_exponential, which are the relevant existing declarations.

**Reader impact:** An expert inspecting the one-sequence claim must verify uniform control of constants, not merely a fixed-k asymptotic. The present landing exposes exactly the quantity whose growth still needs checking.

**Suggested direction:** Point the remark to the existing exponential-constant theorem and the corresponding Q_Fkm inequality, while retaining the separate label that the sequence deduction is ordinary mathematics.

**Evidence:**

- repository/docs/lean_links.json/links/src-budget: Upper/Bound.lean:86–90.
- repository/lean/QuarticQuery/Upper/Bound.lean:67–68, budgetConst_le_exponential; 287–290, Q_Fkm_le_exponential.
- The supplied root-build receipt lists both declarations. No fresh Lean run was performed for this review.

### LR-015 — Appendix B. Mathematical statement catalogue — introductory paragraphs

**Paper:** `reasoning_record` · **Category:** `lean_link` · **Severity:** `medium`

**Exact current-source quotation:**

> The exhaustive declaration inventory belongs to the [correspondence record](reasoning_record_correspondence.json)

**Finding:** This sends a human reader to a 7,350,008-byte JSON file without naming the authoritative branch. Its catalogue_rows entries contain fields called current_in_memory_evidence that say legacy_unbound/not_run/stale, while current_catalogue_snapshot.rows contains the separately dated maintained evidence. For thm-1.1 these two locations give unassessed/not_run versus exact/built_at_pin/compared. The file explains this distinction in catalogue_rows_scope, but the manuscript gives no route to that explanation or to the correct row. These are intentionally preserved historical observations, not a contradiction in the mathematics or a finding about the parallel rebuild.

**Reader impact:** A referee searching a theorem ID can encounter an obsolete field called current before the maintained observation and draw the wrong conclusion about its support. The record makes the reader learn an internal JSON schema to answer a straightforward evidence question.

**Suggested direction:** Give a small human-readable claim-to-declaration index, and link each entry to the dated maintained observation plus its receipt. Identify the authoritative JSON branch beside any raw-JSON link; keep historical overlays available as a separate route.

**Evidence:**

- repository/docs/reasoning_record_correspondence.json/catalogue_rows[id=thm-1.1]/current_in_memory_evidence.
- repository/docs/reasoning_record_correspondence.json/current_catalogue_snapshot/rows[id=thm-1.1]/evidence.
- repository/docs/reasoning_record_correspondence.json/catalogue_rows_scope explicitly says current_in_memory_evidence belongs to the frozen historical audit and directs consumers to current_catalogue_snapshot.

### LR-016 — 1.1 Certificates that disqualify every other candidate — Dependencies and proof recovery

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> They have not been refreshed against this integration.

**Finding:** The record’s two links back toward a short or expository treatment lead to historical funnel-return directories. There is no link to the supplied expert_companion.md or exposition.md, and none of the three expert proof arrival points has a route back to the section that cited it.

**Reader impact:** A reader entering from a current companion can return only through browser history; following the record’s own short-paper links instead opens expressly unreconciled predecessor material and creates avoidable version confusion.

**Suggested direction:** Separate the historical-provenance links from reader navigation and provide return links to the current companion/exposition and relevant source sections.

**Evidence:**

- reasoning_record.md, line 115, links ../research/returns/funnel/2_short_expert_paper/ and ../research/returns/funnel/3_examples_first_exposition/.
- No occurrence of expert_companion.md or exposition.md exists anywhere in current reasoning_record.md.

### LR-017 — Expert companion 4.2 A tournament with probabilistic comparisons; all proof links to the record

**Paper:** `both` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> Full proof: [record §5.2]

**Finding:** All four direct proof links into the record use /blob/main rather than an immutable record version. The packet binds exact current draft and record bytes, while a later reader of those links may see different hypotheses, numbering or evidence. A present anchor match does not preserve the cited proof version.

**Reader impact:** A referee checking the result against a pinned Lean statement can unknowingly combine it with an evolved ordinary proof; this weakens the intended reproducible relationship between the companion and its destination.

**Suggested direction:** Publish version-matched proof links or another immutable record permalink that actually contains the cited bytes, with a separately labelled route to the latest record.

**Evidence:**

- LINK_MAP.json entries 1, 2, 3 and 51 all have ref=main.
- SOURCE_STATUS.json fixes the current record SHA-256 to 1b677c780734209fd36fc206a17e4262f9124e290f84736e9573db8f1f88a986.
- expert_companion.bib, Record2026 entry, line 216, also links to /blob/main/docs/reasoning_record.md.

### LR-018 — 4.2 A tournament with probabilistic comparisons

**Paper:** `expert_companion` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> Full proof: [record §5.2]

**Finding:** The full-proof link starts at the ideal weight process, after the comparison interface and the definitions of T, epsilon and a dominant candidate. The landing is useful for the weight calculation but does not itself state the complete proposition whose proof is promised.

**Reader impact:** Minimum-finding and king-finding readers must scroll above the arrival to learn which comparison assumptions and coherent query cap govern the subsequent sampling and coupling argument.

**Suggested direction:** Use the existing comparison-model entry for the full proposition, or label the present link as the ideal-process subargument and supply a nearby prerequisite route. Preserve the more precise subargument anchor.

**Evidence:**

- reasoning_record.md, #upper-ideal-process at line 2356; #upper-comparison-model at 2314; #upper-tournament-parameters at 2335.
- At the target the text begins “Begin with weights”; the query-cap conclusion appears only later at #upper-tournament-cost.

### LR-019 — 3 Where a natural shortcut fails

**Paper:** `expert_companion` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> Each instance is checked in the companion record or in its review material;

**Finding:** The shortcut table names only the place in the short paper where each issue is used. It gives no exact supporting record or review-material link, despite relying on explicit checked examples. Several relevant record anchors already exist, including the dependent-selection and cap-conditioning counterexamples.

**Reader impact:** Researchers familiar with product bounds or bounded-error search will naturally inspect the counterexample before accepting the claimed obstruction; “review material” makes that inspection a repository search.

**Suggested direction:** Attach exact existing proof/example destinations to the rows that need them, and distinguish a mathematical counterexample from its optional enumerated check. Do not expand the table with new examples.

**Evidence:**

- expert_companion.md, section 3, lines 108–123.
- reasoning_record.md, #CL-selection-independence-example (line 3448), #CL-adaptive-example (line 3084), #CL-conditioning-counterexample (line 3623), and #CL-independent-information (line 3025).

### LR-020 — 4.3 Verification and the query count

**Paper:** `expert_companion` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> explicit budget [@Record2026, §5.4]

**Finding:** The derivation of the displayed logarithmic exponent is cited only through a bibliography entry and the broad section number. The record has an exact #upper-explicit-log6 passage, but the companion never links to it; the nearest quantum full-proof link leads to the tournament weight process instead.

**Reader impact:** A referee checking the deliberately explicit exponent six must find a different, long section after following the quantum proof link. This is an unusually important numerical support point to leave as a broad reference.

**Suggested direction:** Give the existing finite-budget and exponent-six passages direct locators at this claim, alongside the bibliographic citation.

**Evidence:**

- expert_companion.md, line 166.
- reasoning_record.md, #upper-finite-budget (line 2746) and #upper-explicit-log6 (line 2777).

### LR-021 — 2.8. Execution evidence and checks of meaning

**Paper:** `reasoning_record` · **Category:** `register` · **Severity:** `medium`

**Exact current-source quotation:**

> The section-specific build and comparison descriptions report the frozen snapshots inspected in the retained returns

**Finding:** The first main reading route encounters a chronology of frozen checkpoints, targeted runs, global runs, negative controls, declaration counts, and native dependency views before reaching the Forrelation definition. Similar historical explanations recur at the ends of §§3–7 and Appendix A. The mathematical distinction between proof, build, comparison, and fidelity is necessary; repeatedly narrating how the evidence accumulated is not the same task. This is an organizational finding, not a claim that any parallel rebuild statement is wrong.

**Reader impact:** Specialists arriving to check a construction or estimate must decode the project’s evidence history before seeing its mathematical interface, while formal reviewers must reconcile overlapping versions scattered through several sections.

**Suggested direction:** Keep a short evidence-reading key and exact current declaration destinations in the mathematical route. Consolidate chronological receipts, old comments, checkpoint reconciliation, and negative-control execution history in one separate evidence section or sidecar. The SK exemplar’s §§12–13 illustrate this separation.

**Evidence:**

- record §§2.7–2.8, Formal support and source scope after §3.5, §§5.5, 6.7, 7.3, A.6.
- exemplars/long-reasoning-record.md overview and §§12–13: formal interfaces and dated execution history are assigned separate late sections.

### LR-022 — 1. The result and its scope

**Paper:** `reasoning_record` · **Category:** `misplaced` · **Severity:** `medium`

**Exact current-source quotation:**

> Section 7 retains the complete parameter argument.

**Finding:** The opening has already derived the quotient inequality, justified exponentiation, proved divergence, interpreted the infimum, and refuted the cubic bound before §1.1 explains the actual certificate mechanism. Section 7 then supplies the same argument in its intended proof location. The opening gives more space to the standard exponent assembly than to the new reason the construction reaches four.

**Reader impact:** Query-complexity experts can perform the exponent arithmetic once the two scales are visible; they need the outward-pointer/comparison mechanism and the mL versus sqrt(m) arithmetic first.

**Suggested direction:** Retain the fixed-k quantifier warning and a brief scale calculation in the opening, and route the full quotient/infimum derivation to §7. Bring the existing §1.1 mechanism forward.

**Evidence:**

- record §1, passage R3-01-QUANTIFIERS; §1.1, ROOT-ARCHITECTURE; §§7.1–7.2.
- The current expert companion §1.2 and exposition Overview already expose the scale calculation early.

### LR-023 — 5.2. A tournament with probabilistic comparisons

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> This proves Proposition 3.2:

**Finding:** The complete list-output statement appears as a sentence after the drift proof, sampling construction, example, coupling, and cost analysis. At the section’s entry the reader gets pieces of the comparison model and parameters but no single statement collecting all-input cap, list length, dominant-vertex guarantee, and quantifier order. The exact theorem is present, but it is too late to serve as the destination contract.

**Reader impact:** Minimum-finding and tournament experts must know in advance whether they are checking a returned vertex, a list, a Boolean continuation, or a promise algorithm. Those are materially different claims.

**Suggested direction:** Promote the existing Proposition 3.2 statement to the start of §5.2 and divide its proof into visible drift, exact sampling, coupling, and cost stages. Keep its all-input and coherent-access hypotheses together.

**Evidence:**

- record §5.2, anchors upper-comparison-model, upper-tournament-parameters, upper-tournament-cost and upper-tournament-evidence.
- Appendix B.5, prop-3.2, already collects the statement in one place.

### LR-024 — 5.2. A tournament with probabilistic comparisons

**Paper:** `reasoning_record` · **Category:** `misplaced` · **Severity:** `medium`

**Exact current-source quotation:**

> We give the induction used by that Boolean continuation

**Finding:** After proving the list theorem and its padded cost, the section inserts a second acceptance-probability induction for an older Boolean continuation before returning to the actual column decoder in §5.3. The relation is worth preserving, but the detour changes the output object and introduces v(i), V(L), R_n(L), I_n(L), and T_0 at the point where the main algorithm should continue. The final dependency route explains why this proof matters to formal correspondence, not why every mathematical reader must read it here.

**Reader impact:** An expert following the short paper’s list algorithm has to determine whether the Boolean recursion repairs a missing part of that proof or is an alternative implementation; this interrupts the all-input quantum argument.

**Suggested direction:** Keep the list theorem’s proof continuous through decoding and verification. Place the Boolean continuation induction in a clearly marked alternative-proof or formal-route subsection and link it from the declaration that uses it.

**Evidence:**

- record §5.2, upper-tournament-evidence and upper-continuation-induction; §5.3, upper-decode; §5.5 explains that headline roots reach the measured/Boolean route.

### LR-025 — 6.1. A direct product with a separate query cap on each input

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `medium`

**Exact current-source quotation:**

> **The proof with unnormalized weights.**

**Finding:** One numbered subsection contains the conditional-transcript proof, independent-information reduction, a truncation corollary, a detailed adaptive counterexample, a second weighted proof, the equivalence of the two proofs, a planted-proof application, and formal correspondence. The two proofs are not redundant in purpose, but their hierarchy is visible only through bold phrases within a 437-line subsection. A reader cannot use the table of contents to select the proof route or the application.

**Reader impact:** Direct-product specialists need to find the capped theorem and its precise application quickly; formal readers additionally need the unnormalized implementation. Giving both audiences the same undivided route makes each reread material for the other.

**Suggested direction:** Give the existing proof variants, cap-event corollary, counterexamples, and application stable descriptive subheadings. Retain equation (6.11) as the explicit bridge between the two proofs.

**Evidence:**

- record §6.1, anchors CL-product-law, CL-joint-cap, CL-adaptive-example, CL-weighted-values, CL-normalization and CL-planted-interface.

### LR-026 — 6.5. A capped simulator for the planted cell

**Paper:** `reasoning_record` · **Category:** `misplaced` · **Severity:** `medium`

**Exact current-source quotation:**

> Return to the four-column XOR example and use \(L=1\)

**Finding:** The simulator is defined and its unconditional success bound is established, but the crucial inclusion of the nonheavy true-cell event in simulator success is postponed until after the complete XOR simulation table and enumeration. The general reduction is therefore interrupted just before equation (21), the exact statement a short-paper reader is trying to recover.

**Reader impact:** Lower-bound readers need to check that the event stays joint and that no conditioning on nonheaviness occurs. The intervening toy changes P, r, L and the query budget before that logical step has been closed.

**Suggested direction:** Place the existing general event inclusion and equation (21) immediately after the simulator definition; follow with the XOR example and conditioning counterexample as checks of that completed reduction.

**Evidence:**

- record §6.5, CL-simulator, CL-simulator-example, CL-joint-event and CL-conditioning-counterexample.

### LR-027 — 7. The optimal exponent

**Paper:** `reasoning_record` · **Category:** `wasted` · **Severity:** `medium`

**Exact current-source quotation:**

> For completeness, the lower estimate follows from the two nested floors without an asymptotic convention.

**Finding:** The t>=8 induction, the lower bound floor(a)>=a/2, the m floor(a)>=200 check, and the coefficient 1/400 are proved again almost immediately after the complete calculation in §6.6. This is a duplicate proof, rather than a restatement of the endpoint needed for a stand-alone landing passage.

**Reader impact:** The same-family and fixed-k quantifier checks are the delicate work at this destination. Repeating elementary floor arithmetic makes the reader search for a distinction that is not there.

**Suggested direction:** Keep one canonical floor-removal proof in §6.6 and link to it from the assembled estimates in §7. Restate its hypotheses and conclusion as needed for arrival, without repeating the induction.

**Evidence:**

- record §6.6, CL-floors, and §7, ROOT-FAMILY-ASSEMBLY contain the same t>=8 and two-floor derivation.

### LR-028 — 3.16. Literature comparison and the scope of the conclusion

**Paper:** `reasoning_record` · **Category:** `misplaced` · **Severity:** `medium`

**Exact current-source quotation:**

> Fix the version before making the comparison.

**Finding:** The version-specific Bansal–Sinha audit and the separate Sherstov–Storozhenko–Wu comparison occupy the route between the proved Forrelation endpoint and its three-part interface. They include a source-archive hash, TeX line numbers, an alternative sufficient logarithmic comparison, a reciprocal correction to the exceptional uniform-probability term, and a variable-error deduction that the main proof explicitly does not use. The exact attribution is valuable, but this material changes the task from recovering the ingredient to auditing alternative literature routes.

**Reader impact:** Bansal–Sinha and Fourier-growth readers need precise, neutral source comparisons; construction readers should be able to finish the required ingredient without being diverted into conclusions declared unnecessary to it.

**Suggested direction:** Keep a concise attribution and scope note at the point of use, and move the full version-specific checks and external comparison proof to a named source-comparison appendix or evidence note. Preserve exact edition and theorem locators there.

**Evidence:**

- record §3.16, forr_bs_mismatch and forr_ssw_comparison; §3.17 consumes only the existing fixed-k bound, coherent decoder and exact circuit.
- The section explicitly states that (F56) is used only for the comparison and is not assumed by (F43).

### LR-029 — Appendix B. Mathematical statement catalogue

**Paper:** `reasoning_record` · **Category:** `register` · **Severity:** `medium`

**PDF page:** 90

**Exact current-source quotation:**

> The quotations below are the maintained ledger's literal claim text, including its plain-text notation

**Finding:** The reader-facing catalogue intentionally prints raw ledger notation and machine identifiers for all 121 rows. Formulas such as alpha_tot, >=, tensor_{b=1}^t and long brace expressions are harder to scan than the typeset arguments they index. Preserving exact source text is a provenance requirement, but it need not determine the presentation of the mathematical navigation layer.

**Reader impact:** A mathematician looking up a named theorem is made to parse an internal serialization; students arriving from the exposition encounter a second notation system. This is especially costly in a catalogue of 6,406 whitespace-delimited words.

**Suggested direction:** Retain literal texts and IDs in the existing machine-readable correspondence, while giving the displayed catalogue human-readable claim names and typeset statements or concise labels. Preserve every ID as a stable navigation key.

**Evidence:**

- record Appendix B introduction and rows eq-1, eq-15, lem-3.1 and def-adv-progress; the literal source strings are already retained in reasoning_record_correspondence.json.
- repository/docs/reasoning_record.pdf, page 108, visually inspected: raw brace/underscore notation is printed in claim-floor and claim-exponent-ratio.

### LR-030 — Appendix B. Mathematical statement catalogue

**Paper:** `reasoning_record` · **Category:** `missing` · **Severity:** `medium`

**Exact current-source quotation:**

> It preserves all 121 original claim IDs

**Finding:** The catalogue preserves the original ledger but does not provide a parallel entry list for the existing additional results on which the current companion’s sharpened theorem depends. The explicit threshold 13669 k^2, the log-six budget derivation, and the named-circuit refinement are present in the body, yet cannot be found by their own statement names in the original-only catalogue. This is a navigation gap, not a demand for new formalization or a claim that the original catalogue misstates its scope.

**Reader impact:** A reader checking why the short theorem has stronger explicit constants than the preprint needs the exact ordinary specializations and their evidence boundaries, not just the original theorem row.

**Suggested direction:** Add a compact index of these already-existing refinements and their proof destinations, with explicit ordinary-proof versus formal-declaration status. Keep it distinct from the 121 preserved historical IDs.

**Evidence:**

- record §3.15, r3-forr-explicit-fixed-threshold; §5.4, upper-explicit-log6; §7.3, construction_family_named.
- expert companion Theorem 1 and the paragraph immediately following it display the explicit threshold, coefficient and logarithmic power.

### LR-031 — 4.3. A four-column instance

**Paper:** `reasoning_record` · **Category:** `figure` · **Severity:** `medium`

**Exact current-source quotation:**

> Use these instances in the board below.

**Finding:** The record has a detailed four-column table but no figure of the addressed cell and outward pointers. Its X, A, B, transcript and zero-witness roles must be assembled from the table, equations and linked example data. The short papers use drawings to establish this spatial picture, but it disappears at the long-record destination. The concrete address inputs also differ: the record's examples have Forrelation values 1/2, 0 and -1/2, while the exposition uses 1, 0 and -1. Both triples are valid; an illustration should not silently identify them.

**Reader impact:** Pointer-function experts can decode the layout, but the exposition’s reader has to remap the visual into new notation; both benefit from seeing which arrow certifies which condition.

**Suggested direction:** Use the existing generic column illustration beside the layout, with the record's exact labels. For a concrete four-column drawing, keep the record's own input strings or give an explicit crosswalk to the exposition's different valid examples. Preserve the warning that r=2 is a miniature construction example rather than the asymptotic schedule.

**Evidence:**

- record §§4.2–4.3, AC-layout and AC-example-board; no Markdown image occurs anywhere in the current record.
- Existing assets repository/docs/figures/expert_column.svg and repository/docs/figures/exposition/fig1_column.svg; expert §1.2 already uses the first.
- repository/docs/reasoning_record.md §4.3: strings 00000000, 00010010, 11110000; exposition §1: a+, a0, a- with values 1, 0, -1.

## Low priority

### LR-032 — Appendix A. Checking the statement — What Comparator establishes

**Paper:** `expert_companion` · **Category:** `lean_link` · **Severity:** `low`

**Exact current-source quotation:**

> The challenge file and the solution are compiled separately.

**Finding:** The linked statement file ends every one of the four targets with sorry, but the appendix neither explains these intentional specification holes nor links the matching Solution.lean directly. The description of rejecting an unfinished proof makes that visual first impression especially confusing. The supplied solution has genuine proof terms delegating to the implementation theorems, and the configuration selects those four names; this is an explanation/link omission, not an admitted proof in the solution.

**Reader impact:** A mathematician opening the recommended statement file for the first time may mistake the specification placeholders for unfinished theorem proofs, despite the passing Comparator explanation.

**Suggested direction:** Explain briefly that Challenge contains specifications with intentional holes and that Comparator checks the separate proof-bearing solution. Link that existing solution beside the statement and configuration.

**Evidence:**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:326–341 contains the four intentional sorry bodies.
- repository/lean/QuarticCorpus/Unconditional/Solution.lean:16–41 supplies all four exact implementation proof terms.
- repository/docs/expert_companion.md, Appendix A, five deliberately wrong solutions and What Comparator establishes.

### LR-033 — 3.3. The quantum promise algorithm, including amplification and coherence

**Paper:** `reasoning_record` · **Category:** `wasted` · **Severity:** `low`

**Exact current-source quotation:**

> Markov's inequality itself follows by integrating

**Finding:** The promise-algorithm proof pauses to derive Markov’s inequality and elementary numerical bounds on e. The needed new information is the precise fixed repetition count, its all-input cap, and retention of the complete workspace; those features are buried among background estimates familiar to the stipulated specialist audience.

**Reader impact:** Forrelation and amplification experts spend attention on generic concentration arithmetic before reaching the exact coherent output law that can fail if handled casually.

**Suggested direction:** Keep the explicit tail inequality and repetition count in the main proof. Put elementary derivations of standard probability inequalities and loose numerical constants in an optional calculation note, retaining their recoverability.

**Evidence:**

- record §3.3, forr_repetition and forr_coherent; README explicitly lists Markov, union bounds and amplification as known background for the intended expert readers.

### LR-034 — 3.12. Indistinguishability of shallow trees

**Paper:** `reasoning_record` · **Category:** `wasted` · **Severity:** `low`

**Exact current-source quotation:**

> For comparison with the previous draft

**Finding:** The main derivation prints the weaker bound (F34) immediately after the stronger bound (F33), introducing it as a comparison with the previous draft, then later refers to the old sufficient threshold in Appendix D. The old argument is already preserved separately; its weaker estimate does not advance the current proof of (F43).

**Reader impact:** A reader checking the current numerical assembly must determine which estimate is operative and whether a loss of constants is intentional. Editorial history distracts from that choice.

**Suggested direction:** Keep the stronger estimate in the main proof and retain the weaker estimate with its complete historical-threshold derivation in the existing Appendix D or an archival note. Link to it once for readers auditing the change.

**Evidence:**

- record §3.12, F33–F34; §3.15, F43 and F51; Appendix D explicitly says it uses the coarse F34 route.

### LR-035 — B.10. The universal upper bound, thm-A.1

**Paper:** `reasoning_record` · **Category:** `structure` · **Severity:** `low`

**Exact current-source quotation:**

> **Argument:** [§7.3](#ROOT-APPENDIX-INTRO)

**Finding:** The visible label says §7.3, but ROOT-APPENDIX-INTRO is the start of Appendix A. The same catalogue also sends def-Sf to §A.3/ROOT-BS-LAMBDA, where the star application begins, while S_f and lambda(f) are defined in §A.1. Existence of the anchor alone is therefore not enough to validate these argument locators.

**Reader impact:** Readers using a printed section label and readers clicking the link arrive at different mathematical locations. A declaration audit that begins by locating the underlying object loses its direct route.

**Suggested direction:** Correct the displayed section label for thm-A.1 and route definition entries to the actual definitions. Audit catalogue link labels and semantic destinations as a separate check from anchor existence.

**Evidence:**

- record B.10 thm-A.1; ROOT-APPENDIX-INTRO occurs immediately after Appendix A heading.
- record B.10 def-Sf; its definition is in A.1, R3-A-DEFINITIONS; ROOT-BS-LAMBDA begins A.3.

### LR-036 — 4 The quantum algorithm: a tournament — Comparing two columns

**Paper:** `exposition` · **Category:** `notation` · **Severity:** `low`

**Exact current-source quotation:**

> $a_{i^\star j}\ge1-\varepsilon$ for every $j$

**Finding:** The inequality says “for every j” immediately after setting a_ii=0. Taken literally with j=i*, it would require 0≥1−epsilon. The surrounding words “rival” and “opponent” make the intended exclusion clear, and the record states it correctly. This is a local omitted index restriction, not a failure of the algorithm or its proof.

**Reader impact:** A student checking the notation against the preceding diagonal convention encounters an apparent contradiction at the point where the winner guarantee is introduced.

**Suggested direction:** State the rival restriction j≠i* explicitly where the inequality is quantified, consistently with the record.

**Evidence:**

- exposition.md, lines 139 and 141: a_ii=0 followed by the quoted universal claim.
- reasoning_record.md, #upper-winner-dominates, lines 2660–2665, states the inequality with j≠i*.
- paper/extracted.md, section 3.2, equations (10) and (11), separates the zero diagonal from the distinct-opponent guarantee.

## Keep

### LR-037 — 1.1 Certificates that disqualify every other candidate — Dependencies and proof recovery

**Paper:** `reasoning_record` · **Category:** `keep` · **Severity:** `keep`

**Exact current-source quotation:**

> **Dependencies and proof recovery.**

**Finding:** The dependency table pairs mathematical objects with their uses and exact argument destinations. Its Forrelation shortcut explicitly lets a construction reader consume the ingredient statement while deferring the long classical-hardness proof. The target anchors checked here are present and unique.

**Reader impact:** Readers of the source literature can follow the separation mechanism without first reading every foundational or analytic reconstruction. This is the right kind of roadmap for a proof reference.

**Suggested direction:** Keep the table and its stable links, and expose it as a clear arrival/return hub. Preserve the distinction between the ingredient’s statement and its independent proof.

**Evidence:**

- reasoning_record.md, lines 101–113.
- Independent mechanical check: 339 unique explicit anchor IDs, and all 199 current direct internal fragment links resolve to those IDs. All 78 entries of READING_LINK_CLOSURE.json resolve locally as enumerated; this does not assert PDF link behavior.

### LR-038 — 3.6 The statement and the proof

**Paper:** `reasoning_record` · **Category:** `keep` · **Severity:** `keep`

**Exact current-source quotation:**

> The positive yes condition matters: a large negative value is outside the promise.

**Finding:** The Forrelation proof arrival resets the normalization, the one-sided promise, the error and query-cap conventions, and the exact statement to be proved. It then supplies a short proof-spine overview before the analytic details. This is an effective standalone destination.

**Reader impact:** Aaronson–Ambainis and Bansal–Sinha readers can establish immediately which promise problem is under discussion and what quantitative consequence the reconstruction needs.

**Suggested direction:** Preserve this self-contained entry and proof overview. For a citation of the uniform numerical estimate alone, supplement it with the narrower existing section-3.15 anchor.

**Evidence:**

- expert_companion.md, line 260, links #forr_target.
- reasoning_record.md, lines 869–940, #forr_target and #forr_proof_spine; #forr_uniform_assembly begins at line 1520.

### LR-039 — 5.2. A tournament with probabilistic comparisons

**Paper:** `reasoning_record` · **Category:** `keep` · **Severity:** `keep`

**Exact current-source quotation:**

> Conditioned on success, the amplified state is the normalized success component of the unamplified preparation.

**Finding:** The record identifies the exact successful pivot law, rather than merely claiming a high probability of finding some pivot, and uses that law to build a coupling only until the dominant candidate is selected. The four-candidate cycle gives an explicit check of both drift and the conditional law.

**Reader impact:** Quantum search experts can see exactly why arbitrary loser comparisons are permitted and which distributional property the amplification step must preserve.

**Suggested direction:** Preserve the exact conditional-law calculation, the coupling’s stopping boundary, and the cyclic example when shortening background amplification or implementation history.

**Evidence:**

- record §5.2, upper-stage-law, upper-cyclic-example, upper-quantum-tournament and upper-coupling.

### LR-040 — 6.4. Discoveries and the erased zero

**Paper:** `reasoning_record` · **Category:** `keep` · **Severity:** `keep`

**Exact current-source quotation:**

> Thus a uniform marginal law for $I$ does not suffice

**Finding:** The equality between hit probability and expected discoveries divided by m is stated before its search bound, and the dependent-selection example shows numerically why marginal uniformity does not suffice. This isolates the exact independence requirement instead of leaving it implicit in the coupling.

**Reader impact:** Randomized lower-bound readers can test the probability space and the selection rule without reconstructing the whole planted proof.

**Suggested direction:** Retain the identity, its separate assumptions, and the 175/256 counterexample. Keep them adjacent and link directly to this passage from the companion’s erased-zero step.

**Evidence:**

- record §6.4, CL-erased-zero-identity and CL-selection-independence-example; the independent law is fixed in CL-planted.

### LR-041 — 7. The optimal exponent

**Paper:** `reasoning_record` · **Category:** `keep` · **Severity:** `keep`

**Exact current-source quotation:**

> Both inequalities in (7.1) use this circuit

**Finding:** The assembly explicitly insists on a common circuit/function witness for the upper and lower bounds, fixes k before size tends to infinity, and states the strict exponent gap. These are the genuine logical checks in passing from the two algorithms to the universal infimum.

**Reader impact:** Experts can verify that separately existential bounds have not been combined illicitly and that a fixed-k estimate has not been silently used with k growing.

**Suggested direction:** Preserve these witness and quantifier checks when removing duplicate floor arithmetic and shortening the opening.

**Evidence:**

- record §7, ROOT-FAMILY-ASSEMBLY; §§7.1–7.2; §6.6, CL-concrete-lower.

### LR-042 — A.6. The quartic estimate and its formal routes

**Paper:** `reasoning_record` · **Category:** `keep` · **Severity:** `keep`

**Exact current-source quotation:**

> The first route is the one used by the recorded headline proof

**Finding:** The three-route table distinguishes the complexitylib endpoint, literal Appendix A reconstruction and hybrid estimate by ingredients and constants. It then says which route the headline actually uses. This makes a proof-route difference visible without pretending it is a disagreement about the theorem.

**Reader impact:** Sensitivity and adversary-method readers can check the proof they care about while formal reviewers can identify the route selected by the actual endpoint.

**Suggested direction:** Keep the route table and the explicit headline-route sentence, with declaration-specific links supplied by the formal-evidence layer. Use this organizational pattern for other alternative implementations.

**Evidence:**

- record Appendix A.6, R3-A-ASSEMBLY and R3-A-FORMAL.

### LR-043 — 2.8. Execution evidence and checks of meaning

**Paper:** `reasoning_record` · **Category:** `lean_link` · **Severity:** `keep`

**Exact current-source quotation:**

> Comparison membership belongs to those exact declarations, not automatically to every declaration used by their proofs.

**Finding:** This is the right evidence boundary: a successful wrapper does not make every helper a configured Comparator target. The accompanying separation of source presence, compilation, comparison, dependency reach and mathematical meaning is substantively useful.

**Reader impact:** Both formal-methods readers and query-complexity authors need to know whether a claim was checked as a complete type or merely occurs somewhere below a checked endpoint.

**Suggested direction:** Keep this distinction, but pair it with the short exact-name index requested above so the principle is usable at an arrival point.

**Evidence:**

- repository/docs/reasoning_record.md, §2.8.
- repository/lean/QuarticCorpus/Unconditional/comparator.json lists four target names; the map separately labels statement dependencies.

### LR-044 — Appendix A. Checking the statement — The four compared theorems

**Paper:** `expert_companion` · **Category:** `lean_link` · **Severity:** `keep`

**Exact current-source quotation:**

> The exponent $b$ is existential here.

**Finding:** The appendix now distinguishes the existential-exponent, floor-form compared family from the stronger named-family theorem with b=6 and coefficient 1/400. The supplied Challenge and ConstructionFamily types support that distinction, and the shared-circuit quantifier is preserved.

**Reader impact:** An expert can see precisely what the checker established without assuming that explicit display constants were part of the compared statement. This resolves a central earlier editorial concern well.

**Suggested direction:** Keep the complete shared-circuit quantifier explanation and the separate status of the stronger constants theorem when simplifying the appendix or record.

**Evidence:**

- repository/lean/QuarticCorpus/Unconditional/Challenge.lean:328–334.
- repository/lean/QuarticQuery/Paper/ConstructionFamily.lean:30–40.
- repository/docs/expert_companion.md, Appendix A, Quantifier order.

### LR-045 — 6.7. Formal correspondence — The expectation estimate and its route

**Paper:** `reasoning_record` · **Category:** `lean_link` · **Severity:** `keep`

**Exact current-source quotation:**

> even a complete conjunction theorem for (19) does not formalize the early/late proof

**Finding:** The record correctly separates the full equality-plus-bound statement of equation (19) from the particular derivation used to establish its bound. Eq19Whole really includes both clauses, while the source proof of the bound goes through finite-world zero search. The independent product experiment is also explicitly limited to the interfaces it actually shares.

**Reader impact:** A reader of the preprint can verify the endpoint without mistaking a different formal proof route for a formalization of each printed intermediate step.

**Suggested direction:** Retain the whole-display/route distinction and link the complete conjunction directly from equation (19), alongside the ordinary early/late and alternative arguments.

**Evidence:**

- repository/lean/QuarticQuery/Paper/Eq19Whole.lean:26–34.
- repository/lean/QuarticQuery/Paper/ClassicalPlanted.lean:215–257.
- repository/lean/QuarticCorpus/Independent/Eq19/Challenge.lean:19–24.
