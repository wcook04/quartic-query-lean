# Round 10 further manuscript revision

Authoring baseline: `f1b1231cfe3dc444ca6961a78c0400fbe505cd9e`. This note accompanies the 48 individual decisions in [round10_further_dispositions.json](round10_further_dispositions.json). The three feedback transcripts are preserved under `research/returns/round10/further_*_feedback.md`. They contain sequential reassessments, including corrections to earlier criticism. They are advisory evidence, not commands, proofs or measured reader outcomes.

## Selected contribution and readers

The mathematical result remains OpenAI's nearly quartic separation. The expert companion reconstructs its weighted tournament and capped prediction reduction for a query-complexity reader. The exposition teaches those mechanisms using the existing small board, quantum experiments, changed cases and exercises, assuming finite-dimensional linear algebra, elementary probability and asymptotic notation. The reasoning record preserves the complete ordinary proof, analytic input, quantitative estimates and exact formal correspondence for a reader recovering or checking an argument.

The shared mechanism is unchanged: comparisons generate a short quantum candidate list before certificate verification; a classical visit to the planted certificate predicts its hard address. The same circuit defines the total input function on both sides. This pass improves the order in which the reader sees the required contracts, constructions and stronger proofs. It does not assert a new separation, formal theorem, independent verification or novelty clearance.

## Concrete architecture decisions

- **Expert:** moved the existing §1.1 mechanism and existing figure ahead of the model and quantitative theorem, keeping subsection numbers. Replaced the overloaded contribution paragraph with contribution/credit and the actual fixed-parameter dependence. Added one compact explanation of local proofs versus imported inputs and record derivations. Displayed the preparation success and successful-label laws separately; explained why the classical predictor fixes a query time. Defined the evidence terms in §6. Appendix E now names the uniform analytic input separately from its deduction.
- **Exposition:** stated the two-answer-to-cell operation before the first Walsh calculation. Explained the roles of logarithmic address length, fixed hardness parameter and small circuit. Named local certification, successful-label law, tournament guarantee and direct-product lemma at their existing derivations. Split §4 into four mathematical stages. Put the joint-event inclusion before simulator instructions, marked the XOR trace optional and returned to the board at the end of §6. Moved only the gate-number census to A.4, preserving its exact external check and example boundary. Added accurately delimited AIK v3 and BDK v1 comparisons.
- **Record:** §5.1 now gives the finite measured-output law and all-branch cap needed by the evaluator, then the original stronger Lemma 3.1. The full geometry, finite schedule, averaging, cap and retained-register proof moved to §5.6, after the evaluator. No mathematical proof block was deleted. The tournament now invokes the weaker contract it actually uses. Added the two changed locations before the long direct-product proof, the power balance before the analytic details, and the design constraints before the algebraic Gaussian pair. Explained finite admissibility versus asymptotic usefulness in §7.3. G.4 now spells out every clause of the compound compared theorem.

No new diagram, page quota, generic roadmap, theorem renumbering scheme or second audit table was introduced. The record's existing §3 ingredient contract, §8 full proof and Appendices F/G history/current-audit division remain. The later reviews explicitly supported those decisions.

## Paragraph decisions at the inspected scope

This is an author review of changed and adjacent passages, not a new blind-reader study or a claim to have reverified every line of the 140-page record. Unchanged proofs retain their prior source-bound review; the present checks concentrate on the statements, transitions and evidence touched here.

| Passage | Mathematical job and decision |
| --- | --- |
| Expert abstract, final two sentences | State the measured-label headline route before the stronger physical correspondence boundary. Kept the boundary; did not let it imply a hypothesis of the headline proof. |
| Expert contribution | Attribute the theorem and reductions; identify reconstruction and explicit accounting. Removed mixed evidence inventory from this early paragraph; C_k remains parameter-dependent. |
| Expert §1.1 four mechanism paragraphs | Motivate both algorithms and the exponent quotient. Retained wording and existing illustration; moved together before model detail. |
| Expert quantitative theorem/model | State all-input caps, error law, fixed k, same circuit and exact inequalities. Retained full statement; the mechanism move does not weaken it. |
| Expert paragraph after theorem | Explain which proof is here and which is an input. Kept record destinations and optional uniform scope explicit. |
| Expert §2 circuit/decoder sketches | Explain their different purposes. Retained complete domain/value contract and exact gate-count destination instead of duplicating record §8.3. |
| Expert §3.2 tensor paragraph | Derive product masses and two normalizations. Replaced one dense sentence with two displayed laws and one purpose sentence; all workspace and inverse conditions remain. |
| Expert §4.4 fixed-time paragraph | Turn a chosen cell coordinate into one prediction. Added why the query time is fixed; did not change the order of truncation, prediction or time union. |
| Expert §6 opening and endpoint paragraph | Define evidence operations and expose exact endpoint identities. Receiving PDF showed an overlong identifier, so namespace and basenames are now separate. |
| Exposition §1 first paragraph | Give a purpose for the three input roles before matrix notation. Added the concrete cell-selection operation; retained all subsequent calculations. |
| Exposition §2 parameter paragraph | Explain why r is logarithmic and k is fixed. Expanded only the design rationale; formula r=20log₂m and polynomial array remain exact. |
| Exposition §2 local certification | State the all-input equivalence after deriving its tests. Named it, retaining the nonwinner and malformed-address consequences. |
| Exposition circuit census | Reproducible optional detail. Moved intact to A.4; retained S=180, K=371, zero-based gate labels and the distinction between the checker board and this board. |
| Exposition §4 milestones | Guide the reader through comparison, ideal law, implementation and verification. Added headings; retained calculations and examples in sequence. |
| Exposition §4 successful-label paragraph | Explain why amplification changes success mass but not the label law. Named existing conclusion, preserving fresh trials and state up to global phase. |
| Exposition §5 event inclusion | Explain the reduction before code-like steps. Moved the mathematical purpose earlier and removed one redundant inline inclusion later. |
| Exposition §5 simulator/trace | Prove all-input cap and show two clocks. Retained every instruction, default and branch; made trace optional without moving its exercise or answer. |
| Exposition §6 final synthesis | Recover the opening board and why the two costs differ. Added after exact fixed-k argument and imported upper bound, before synthesis exercise. |
| Record §5.1 and §5.6 | Separate a sufficient measured contract from its stronger state proof. Relocated complete proof and changed local proof references only. |
| Record §6 opening | Identify first disagreement and address prediction before direct-product machinery. Added construction preview; full coupling and independence stay in §6.3. |
| Record §8 proof spine | Identify Walsh-edge and derivative powers before numerical constants. Added early scale explanation, retaining F33 and exact assembly. |
| Record §8.7 | Motivate phi/Psi by bounded biases, integration identity and edge-factor control. The following existing computations verify each requirement. |
| Record §8.10 | Explain why biased derivatives require their own estimate. Existing F24 already gives a counterexample; rejected a duplicate new expansion and kept a short bridge. |
| Record §7.3 | Distinguish finite admissibility from informative asymptotic exponent. Kept both allowances and square-root schedule unchanged. |
| Record G.4 | Specify compared compound theorem and current named-theorem evidence. Exact source type supports three clauses; historical source comment is reconciled with the later receipt. |

Retained deliberately: all off-promise explanations; expected-versus-worst-case cap distinction; conditional-law calculation; source/winner/comparison distinctions; final verifier; heavy/light event under the original law; all counterexamples; separate fixed/growing-k arguments; all disclosure text. No artificial sentence-length target or word-list score selected these decisions.

## Source comparisons and mathematical readback

The portable mathematical-reasoning and formal-math-exposition methods were applied in that order. The full exposition mechanics and worked guide were read in bounded chunks; their advice is subordinate to actual source truth, attribution and this repository's genre. Current transition owners are in the isolated `lean-exposition-quartic-r10` checkout. The parent checked concrete passages from the retained primary literature; no new numerical register comparison or stylistic score is claimed in this pass.

The two supplied source archives are byte-identical to existing annex copies, as recorded by the parent in [round10_further_annex_integrity.json](round10_further_annex_integrity.json). The read comparison used AIK v3, especially the source invariant before search and the difference between actual caps and analysis-only stopping, and BDK v1, especially the reason for cumulative certificate encoding and totality despite irrelevant malformed cards. The adopted writing moves were purpose before encoding and invariant/contract before machinery. No sporting metaphor, graph theorem or certificate-complexity result was transported into the R–Q proof.

The exposition's existing AIK v2 entry remains distinct from the new cited v3 entry. BDK is explicitly v1. A first draft of the BDK comparison described finding versus reading certificates too loosely; author readback narrowed it to randomized evaluation versus certificate complexity before the final render. Primary identities, additional antecedent comparisons and archive integrity are recorded in the parent's [literature audit](round10_further_literature.json).

Read the exact `QuarticQuery.Checked.theorem_one_one` type in `lean/QuarticCorpus/Unconditional/Challenge.lean`: it asserts alphaTot=4, UniversalPower4 and the same-circuit fixed-k family. Read the named-family declaration and historical header in `lean/QuarticQuery/Paper/ConstructionFamily.lean`. The maintained correspondence records that declaration's complete type, exact source hash, source-bound build, axiom-audit inclusion and absence of exact-name Comparator coverage. File inclusion alone was not used as a comparison claim. The explicit13669k² threshold remains an ordinary argument; the family theorem does not acquire it from nearby formal results.

The author source check preserved every existing explicit anchor, claim marker, passage delimiter and display tag. The only new explicit anchor/passage is `upper-label-contract`. All mathematical parameter formulas and theorem inequalities remain unchanged. The amplification proof move required local §5.1→§5.6 labels in the record, expert Appendix C and exposition Appendix A.3; external source section numbers were left alone. The receipt identifies this as a semantic-reference change, not a blanket replacement.

## Corrections to the critiques

The later reviews withdraw missing-overview and indiscriminate example-removal criticisms, retract the exposition theorem-too-late complaint, and soften the record's opening/navigation/history diagnoses. Their adversarial passes do not identify a decisive error in the principal separation; that is a bounded reading report, not verification evidence.

The alleged growing-parameter contradiction disappears because uniform F43 supplies a different allowance from the fixed-k threshold. The extracted radical ambiguity also disappears on reading the actual source/typeset schedule, k=floor(sqrt(t/20)); no formula was corrected. The early range where epsilon is at least four is mathematically valid but not an informative near-quartic estimate, now explained at the start of that argument. The G.4 concern was a prose ambiguity about clauses, resolved by reading the full type, not a formal theorem mismatch.

Potential objections involving unbiased address answers, arbitrary losing comparisons, expected caps, conditioning on lightness or uniform-but-dependent planting were already excluded by explicit hypotheses and counterexamples. Their explanations were retained. The failed broader simplification attempt was to replace biased derivatives by degree-k Fourier coefficients at zero; existing F24 shows why that would lose higher-degree terms. No such mathematical simplification was adopted.

## Authoring receipt and receiving boundary

- **Object, genre and promise:** three coordinated but audience-specific accounts of one separation; reconstruct the mechanisms, recover full proofs, and inspect formal meanings respectively.
- **Contribution type:** explanatory reconstruction, explicit estimates and examples, with separately recorded formal proofs. No new theorem authority conferred by prose.
- **Headline and compressed claims:** fixed k, all-input caps, same circuit, logarithmic slack and alpha=4 preserved across abstracts, openings and theorem statements. Optional growing-k result remains a distinct uniform deduction.
- **Internal dependency map:** contract before evaluator; full amplification proof later in §5.6; plant/first-disagreement before product machinery; analytic power balance before constants.
- **External map and citation roles:** original OpenAI result and predecessor credit retained; AIK/BDK additions are related constructions; uniform analytic proof and exact gate count retain precise record destinations.
- **Concrete anchors and limits:** existing small boards, fractional table and XOR trace retained with their changed laws/parameters; none is treated as a hardness instance for large m.
- **Simplification attempted:** replace repeated explanations with a local contract or named conclusion; rejected deleting necessary cap/state/conditioning detail and rejected duplicate Fourier explanation. Net length is not a success measure.
- **Conditional hypotheses and notation:** no new conditional mathematical premise; p_b, p and f are defined locally in the measured-law contract. Full state g remains defined in the relocated proof. No one-use house notation introduced.
- **Difficulty and fertility:** exact successful sampling, capped prediction and analytic derivative growth remain the hard steps. No speculative programme added merely to fill a review template.
- **Formal alignment:** exact headline type and named-family evidence read; no Lean code or receipt changed by the author. Whole physical output-state correspondence remains open in G.7.
- **Reader evidence:** author sequential/transition reread at the changed scope plus parent receiving inspection. No new independent or blind reader participated, and no learning improvement is measured. Existing returned reassessments remain their own dated evidence.
- **Review coverage:** all three feedback transcripts considered, changed source and adjacent proof passages assessed, unchanged long-record mathematics sampled through its affected dependencies. This is not a fresh full mathematical audit of the entire record.
- **Render and bibliography:** parent rendered the source freezes and inspected affected pages; final binding/render/whole-page acceptance remains parent-owned. Author applied the reported expert identifier-overflow repair. Parent found the record §5.2 heading/statement split and applied an existing Needspace guard. No final-render acceptance is claimed in this author receipt.
- **Source hashes:** disposition hashes identify the authored freeze before final generated-link rebinding. Parent must record final hashes after binding. No author commit.

## Receiving acceptance

The final PDFs contain 19 expert, 27 exposition and 141 record pages. All pages were inspected at contact-sheet size, with the affected pages listed in [validation](round10_further_validation.json) also inspected at readable size. Final source hashes, native render bindings, navigation checks, 48 dispositions and seven bounded literature comparisons are recorded there. `make check` ran 264 tests with two skips and no failures. All old record anchors, claim occurrences, passage markers and equation tags were preserved. No Lean source changed and no new Lean or Comparator execution is claimed. The printed source editions and Markdown crosslinks identify the committed revisions.
