# Round seven: expert companion revision

The corrective pass at the end supersedes this audit's earlier acceptance of the expert paper's prose tables. The user's final criterion permits genuinely readable tables and rejects cramped prose or status tables; full-width prose was chosen for these two passages.

## Scope and plan

This revision owns `docs/expert_companion.md`; it changes no Lean definition,
proof, corpus statement or recorded execution evidence. The four preserved
returns are advice, checked against the maintained record and formal sources.
The paper remains a reconstruction of OpenAI's construction and analyses.

The plan followed was to reorganise the opening around the total-function
question and winner-only comparison guarantee, replace the standard-amplifier
and constant bookkeeping with bounded proof destinations, and spend that space
on the actual reductions: exact weighted sampling, a capped address predictor,
and the promise-to-distribution gap in the Forrelation proof. Section numbers,
equation tags (1)–(16), bibliography keys and the generated Lean link block were
preserved. Theorem 1 now states the already proved explicit choices six and
1/400; §7 identifies the separate named-circuit theorem supporting them.

Mathematical reasoning preceded authoring. The manuscript pass used the
route-human-authoring, formal-math-exposition and long-to-short instructions;
the current register skill and rule owner were resolved in the verified
lean-exposition worktree based on main at 5a9a3ab, because the older sibling
checkout lacked that skill. No advisory attachment script was executed.

## Literature and writing decisions

Primary texts were read at these task-relevant locations; no claim of a new
literature priority result is made. Local text extractions were used alongside
primary web editions for wording and source-location checks.

| Source and locator | Writing or mathematical move actually used |
| --- | --- |
| [OpenAI, 5 October 2026 preprint](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf), introduction and §§3–4 | Lead with the separation and its mechanism; keep all-branch resource guarantees beside the algorithms. Attribute construction and analyses directly. |
| [Aaronson–Ben-David–Kothari, v2](https://arxiv.org/html/1511.01937v2), §3.1, opening through certificate construction; §3.2 | Put the small-Q(g) assumption before the composition cost. Explain what certificates establish before counting their size. Use an intuition-to-implementation transition rather than a contribution inventory. |
| [Aaronson–Ben-David–Kothari–Rao–Tal, v1](https://arxiv.org/html/2010.12629v1), introduction, “Deterministic vs. quantum query complexity” | State what the existing inequality supplies for the main question, then give its short consequence; avoid equal space for alternate numerical implementations. |
| [Ambainis–Iraids–Kokainis, v3](https://arxiv.org/html/2609.11664v3), §6.1, Algorithm 4 and candidate sets | Compare the actual surviving-set operation to fractional weights. Keep an executable stage description beside the proposition; distinguish exact probabilities from approximate fixed-edge predicates. |
| [Drucker](https://doi.org/10.1007/s00037-012-0043-7), “Our methods”, §3 Lemmas 3.1–3.2 and fair specialisation | Show which factor changes under one query. Preserve the global-budget alternative as a sufficient route, rather than claiming the separate-cap version indispensable. |
| [Bansal–Sinha v3](https://arxiv.org/html/2008.07003v3), introduction and §3; maintained record §§3.12–3.16 | Distinguish the analytic correlated law from a promise-supported minimax law. Explain the lower-bound exponent by the competing depth/dimension powers, then expose the promise-gap inequality. |
| [Girish–Tal–Wu, CCC 2021](https://doi.org/10.4230/LIPIcs.CCC.2021.39), §1.3, Lemma 9, printed p.39:8 and footnote 2 | Attribute the ordinary-tree derivative-growth/stopping method precisely. The changed bounded-bias constants and raw-derivative statement remain the reconstruction's calculation. |

The quantum and classical audit agents independently checked the revised
amplifier interfaces, the fractional example, F41/F42, the uniform bound and
its ancestry against current sources. Their separate audit files contain the
source-level evidence. This prose pass introduces no new mathematical result.

## Consequential cuts and retained destinations

| Passage | Decision and destination |
| --- | --- |
| Abstract and opening | Replace claims of a complete proof with reconstruction from named ingredients. Keep OpenAI attribution, totality and the principal theorem immediate. |
| Introduction constants | State six and 1/400 in the theorem; put C_k and the explicit threshold with their uses. |
| Amplification numerical trials | Keep cap, zero-success and exact conditional label law; record §5.1 keeps the constants and retained-state strengthening. |
| Quantum padded products | Keep three cost scales; record §5.4 keeps the loose logarithmic and exponential constant accounting. |
| Early/late optional refinement | Keep the baseline proof continuous; link the stronger count after the assembled lower bound. |
| Floor arithmetic | Keep resulting coefficient and required regime; record §6.6 preserves every inequality. |
| Growing-k finite epsilon | Keep schedule, uniformity requirement and asymptotic result; record §7.3 keeps the finite formula. |
| Formal proof variants | Keep model/content distinctions that affect interpretation; record Appendix G keeps alternate universal constants, axiom taxonomy and execution evidence. |
| Forrelation proof outline | Expand rather than compress: the actual two competing acceptance-gap estimates now explain the claim that amplification yields a contradiction. |

The main separation argument and the record are unchanged in mathematical
reach. Optional corrections were selected by the inference they clarify,
not by the number or severity of repeated reviewer requests.

## Dispositions by concrete revision

`accepted` means the requested substantive repair is in the manuscript.
`adapted` means the diagnosed difficulty was repaired with a different form.
`previously-addressed/protected` identifies a keep finding whose required
invariant survives the rewrite. Rendering and bibliography actions outside
this writer's scope are explicitly routed to the parent instead of silently
counted as complete.


### Title, abstract, §1

**Accepted/adapted findings:** EF001, EF002, EF003, EF004, EF005, EF006, EF007, EF008, QS001, QS003, QS004, QS006, QS007, NR113, NR114, NR115, NR116, NR118, NR119, LS001, LS002, LS003, LS005.

Question-first opening; explicit exponent six and coefficient 1/400 in Theorem 1; contribution framed as reconstruction of OpenAI, with actual cited inputs stated immediately. Abstract discovery claim is distributional and m is introduced.

### §1.1

**Accepted/adapted findings:** EF010, EF011, QS008, QS009, QS010, NR120, NR122, NR123, LS006, LS007, LS008.

Small quantum cost is a premise before the AND–OR formula; its total cheat-sheet function is named; inner certificates certify the outer input; Rorrelation is identified. Historical rows give achieved lower-bound exponents and the universal bound is separate.

### §1.2

**Accepted/adapted findings:** EF013, EF014, EF015, EF016, QS012, QS013, QS014, QS015, NR124, NR125, LS009, LS010.

Promise-qualified semantic addresses; quantum nested-search obstacle precedes the classical hiding argument. Independently chosen column I and conditioning on the dummy run explain Z/m; one changed bit and one changed block are distinguished. L is a lower-bound scale.

### §1.3

**Accepted/adapted findings:** EF018, EF019, EF020, QS017, QS018, QS019, QS020, NR128, NR129, NR130, LS012.

Highlighted leaves, not all zeros, carry predecessor back pointers; back-pointer and no-back-pointer variants are distinct. Comparison antecedents are compared by input/output guarantees. King is defined; fixed predicate search remains available but costs sqrt(K).

### §2

**Accepted/adapted findings:** EF021, EF022, EF023, EF024, EF025, QS021, QS023, QS024, QS026, NR131, NR132, NR133, LS015, LS016, LS018.

Powers of four explained; matrix application order and one phase query per sign layer stated. S counts non-input gates including outputs. Coordinates are freely assignable, not probabilistically independent. Output consistency and semantic tests are distinct. Optional Q-versus-input-length claim removed.

### Lemma 2 and §3 opening

**Accepted/adapted findings:** EF027, EF028, QS028, QS029, NR135, LS020.

Fixed input-independent success bit, all-branch cap, zero-success case and exact conditional label law are foregrounded. State argument is up to global phase. Numerical trials remain in record §5.1; expected-cost comparison is specifically untruncated QSearch.

### §3.1

**Accepted/adapted findings:** QS032, QS034, LS021.

Sorted indices enforce one circuit; explicit target-bit cases determine each comparison. a_ij are exact probabilities for a fixed input, and only the winner needs reliability. Retained workspaces preserve those probabilities.

### §3.2

**Accepted/adapted findings:** EF029, EF030, EF031, EF032, QS035, QS037, QS038, QS040, QS041, QS044, NR137, LS023.

Proposition interface split into clauses; explicit algorithm summary; product interpretation conditional on fixed input/history and fresh workspaces; half-drift bound and absorbing W=0; exact success-label law; abstract fractional example; stopped stagewise coupling and all-input cap.

### §3.3

**Accepted/adapted findings:** EF036, EF037, EF038, QS045, QS046, QS047, QS048, NR139, NR140, LS026.

Dominance counterexample placed before verification. Search reports a defect or no defect found; candidate acceptance remains separate. One-input and zero-input errors interpreted; controlled read is at most two queries. Retained only comparison/list/verification costs, with padded constant arithmetic in record §5.4.

### §4 opening and §4.1

**Accepted/adapted findings:** EF039, EF041, QS049, QS051, NR142, LS027, LS029.

Generic F_{P,C,m} lower-bound target precedes Forrelation substitution. Promise-supported minimax law and strict/attained threshold retained. Separate-cap proof exposes the unchanged common product factor. Drucker global-budget substitution remains valid and optional.

### §4.2 and Figure 2 caption

**Accepted/adapted findings:** EF042, EF043, EF044, QS052, NR143, LS033, LS034, LS035.

Sampling, dummy assignment and independent I are separate steps. Dummy support is zero because every column has a zero. A cell visit conservatively covers a possible first differing bit. Caption identifies m=4 as geometry, not a hardness threshold; figure owner corrects four-bit strings and tuple labels.

### §4.3 and end §4.5

**Accepted/adapted findings:** EF045, EF046, QS054, QS055, NR144, LS036, LS037.

Residual uniformity is conditional on the entire past before first discovery. Distinct prior rows and repeated query calls are distinguished. Optional sharper probability relocated after lower-bound assembly.

### §4.4

**Accepted/adapted findings:** EF047, EF048, EF050, QS057, LS039, LS042.

Predictor definition ends before its cap/event proof; abort returns fixed vector; output address precedes reading the cell. Total cap L implies separate caps. Joint event is never conditioned on nonheaviness. Explicit sum over i and time shows the column factor cancels.

### §4.5

**Accepted/adapted findings:** EF051, EF052, QS059, LS045.

Correctness on both full supports is averaged. Preserved roles of three discrepancy terms, address length and slack constants. Floor details moved to record §6.6; the separation retains mL and loses powers only through the chosen Forrelation threshold.

### §5

**Accepted/adapted findings:** EF053, EF054, EF055, QS060, QS061, NR146, NR147, LS047, LS049.

Fixed-k cited theorem distinguished from uniform refinement. Added shallow-tree gap bound and its m/d power balance. F41 pointwise promise inequalities and F42 expectation gap expose positive signal, amplified error and uniform leakage. Changed truncation and exact GTW antecedent identified; analytic law distinguished from minimax law.

### §6

**Accepted/adapted findings:** EF058, EF059, QS064, NR148, LS051, LS052.

Fixed alpha, then fixed k, constants/threshold, then m grows. One growing-k family kept with its uniform inputs and exact schedule; finite epsilon formula moved to record §7.3. No exact Omega(Q^4) claim.

### §7 and AI disclosure

**Accepted/adapted findings:** EF060, EF061, EF062, EF063, EF065, QS065, LS053, LS054.

Four mathematical paragraphs replace lengthy source inventory: unconditional endpoints, model bridges/nonempty minima, existential headline versus explicit circuit constants, measured/reset versus retained-state amplifier, finite-seed compliance and ordinary bridges. Detailed axioms, alternate quartic coefficients and execution history remain in record. AI responsibilities stated.

### Appendix A

**Accepted/adapted findings:** EF067, EF068, EF069, QS068, QS069, LS043, LS056.

Cross-references use descriptive row names. Beta is a success bound, exact in finite examples. Zero-budget examples test general lemma hypotheses. False dominant example now states other columns have zeros. Joint and conditional cap probabilities retained.

### Specific adaptations, rejected expansion and external owners

- **LS032 — rejected for this companion:** the optional later direct-product citation is not needed to explain the selected fixed-law, hard-cap proof. No claim is made that the later source is irrelevant in general; adding another result with a different resource measure would enlarge the short related-work catalogue without changing an inference here.
- **NR150 — adapted:** shorten the row's label and use the direct record link, but preserve its exact 5/16 and 5/8 probabilities and repeated-query mechanism. The example earns its space by displaying the distinction the proof needs; replacing it by a warning would lose the checkable witness.
- **QS019 — adapted:** use a compact progression through comparison contracts in §1.3 rather than another table.
- **QS035, QS057 — adapted:** give the actual algorithm in connected prose, separating its definition from its proof, rather than adding numbered lists.
- **EF027, QS028, NR134–NR135 — adapted:** state the measured-label theorem used by the tournament; prove its law through the retained successful-state direction up to phase. Retained-state numerical details remain in the record. This removes the need to reconcile two unnecessary numerical splits in the short proof.
- **EF025, QS026, LS018, NR132 — adapted:** retain the polynomial input-size count; remove the unused 1/44 input-length consequence rather than move a second bound into the main argument.
- **EF066 — parent-owned bibliography repair:** the OpenAI bibliography entry should link directly to the October 5 manuscript. This writer does not own the bibliography.
- **EF042–EF043, QS013, QS053, QS071, LS009, LS034, NR143 — figure coordination:** the figure owner corrected the m=4 strings, shared address blocks and tuple law, and replaced “independent” by “disjoint”. The expert caption explicitly explains the schematic regime and arrays belonging to every column.
- **EF070, QS070 — rendering acceptance:** the first render was inspected. Figure 2 and (10)'s probability qualifier now remain together. Figure 1 still interrupted a following paragraph at the page boundary, so a supported PDF-only page break was added at its source paragraph boundary and the figure owner was asked to rerender. The second render was inspected at reading size: Figure 1 now precedes the whole paragraph and its enlarged certificate label is readable. Final bibliography/repin rendering remains parent-owned.

### Protected findings

The following requests identify material already repaired in earlier rounds or
already correct. It was retained for the stated mathematical role; these are
not counted as new discoveries or newly proved claims.


- **Title, abstract, §1:** EF009, QS002, QS005, NR117, LS004. Protected content: Question-first opening; explicit exponent six and coefficient 1/400 in Theorem 1; contribution framed as reconstruction of OpenAI, with actual cited inputs stated immediately. Abstract discovery claim is distributional and m is introduced.

- **§1.1:** EF012, QS011, NR121. Protected content: Small quantum cost is a premise before the AND–OR formula; its total cheat-sheet function is named; inner certificates certify the outer input; Rorrelation is identified. Historical rows give achieved lower-bound exponents and the universal bound is separate.

- **§1.2:** EF017, QS016, NR126, LS011. Protected content: Promise-qualified semantic addresses; quantum nested-search obstacle precedes the classical hiding argument. Independently chosen column I and conditioning on the dummy run explain Z/m; one changed bit and one changed block are distinguished. L is a lower-bound scale.

- **§1.3:** NR127, LS013, LS014. Protected content: Highlighted leaves, not all zeros, carry predecessor back pointers; back-pointer and no-back-pointer variants are distinct. Comparison antecedents are compared by input/output guarantees. King is defined; fixed predicate search remains available but costs sqrt(K).

- **§2:** EF026, QS022, QS025, QS027, LS017, LS019. Protected content: Powers of four explained; matrix application order and one phase query per sign layer stated. S counts non-input gates including outputs. Coordinates are freely assignable, not probabilistically independent. Output consistency and semantic tests are distinct. Optional Q-versus-input-length claim removed.

- **Lemma 2 and §3 opening:** QS030, NR134. Protected content: Fixed input-independent success bit, all-branch cap, zero-success case and exact conditional label law are foregrounded. State argument is up to global phase. Numerical trials remain in record §5.1; expected-cost comparison is specifically untruncated QSearch.

- **§3.1:** QS031, QS033, NR136, LS022. Protected content: Sorted indices enforce one circuit; explicit target-bit cases determine each comparison. a_ij are exact probabilities for a fixed input, and only the winner needs reliability. Retained workspaces preserve those probabilities.

- **§3.2:** EF033, EF034, EF035, QS036, QS039, QS042, QS043, NR138, LS024, LS025. Protected content: Proposition interface split into clauses; explicit algorithm summary; product interpretation conditional on fixed input/history and fresh workspaces; half-drift bound and absorbing W=0; exact success-label law; abstract fractional example; stopped stagewise coupling and all-input cap.

- **§4 opening and §4.1:** EF040, QS050, NR141, LS028, LS030, LS031. Protected content: Generic F_{P,C,m} lower-bound target precedes Forrelation substitution. Promise-supported minimax law and strict/attained threshold retained. Separate-cap proof exposes the unchanged common product factor. Drucker global-budget substitution remains valid and optional.

- **§4.2 and Figure 2 caption:** QS053. Protected content: Sampling, dummy assignment and independent I are separate steps. Dummy support is zero because every column has a zero. A cell visit conservatively covers a possible first differing bit. Caption identifies m=4 as geometry, not a hardness threshold; figure owner corrects four-bit strings and tuple labels.

- **§4.4:** EF049, QS056, QS058, NR145, LS038, LS040, LS041. Protected content: Predictor definition ends before its cap/event proof; abort returns fixed vector; output address precedes reading the cell. Total cap L implies separate caps. Joint event is never conditioned on nonheaviness. Explicit sum over i and time shows the column factor cancels.

- **§4.5:** LS044. Protected content: Correctness on both full supports is averaged. Preserved roles of three discrepancy terms, address length and slack constants. Floor details moved to record §6.6; the separation retains mL and loses powers only through the chosen Forrelation threshold.

- **§5:** EF056, QS062, LS046, LS048. Protected content: Fixed-k cited theorem distinguished from uniform refinement. Added shallow-tree gap bound and its m/d power balance. F41 pointwise promise inequalities and F42 expectation gap expose positive signal, amplified error and uniform leakage. Changed truncation and exact GTW antecedent identified; analytic law distinguished from minimax law.

- **§6:** EF057, QS063, LS050. Protected content: Fixed alpha, then fixed k, constants/threshold, then m grows. One growing-k family kept with its uniform inputs and exact schedule; finite epsilon formula moved to record §7.3. No exact Omega(Q^4) claim.

- **§7 and AI disclosure:** EF064, QS066, QS067, NR149, LS055. Protected content: Four mathematical paragraphs replace lengthy source inventory: unconditional endpoints, model bridges/nonempty minima, existential headline versus explicit circuit constants, measured/reset versus retained-state amplifier, finite-seed compliance and ordinary bridges. Detailed axioms, alternate quartic coefficients and execution history remain in record. AI responsibilities stated.

- **Appendix A:** LS057. Protected content: Cross-references use descriptive row names. Beta is a success bound, exact in finite examples. Zero-budget examples test general lemma hypotheses. False dominant example now states other columns have zeros. Joint and conditional cap probabilities retained.

## Paragraph pass and validation

Every prose paragraph was read sequentially in the revised source. The opening,
overview, theorem interface, amplification proof, tournament explanation,
classical setup, simulator, Forrelation account and formal discussion were
rewritten. Exact definitions, displays (3)–(16), the half-drift calculation,
stopped coupling, direct-product recurrence, discrepancy assembly and fixed-k
ratio argument were retained where their existing form already carried the
proof efficiently; edits around them expose assumptions and the next inference.
The introduction's historical paragraphs and all captions were checked for
quantifier direction, model and notation before sentence polish. The final
counterexample table retains its numerical witnesses with shorter reference
names.

Register measurement used the current standard-library module directly, with
five cited primary texts: OpenAI, ABK, ABKRT, Bansal–Sinha and Drucker. The first
measurement gave 5,129 extracted prose words and 279 sentences; after the final
source pass it gave 5,185 and 332. Mean absolute corpus distance changed from 1.817
to 1.809, while feature outliers changed from 12 to 14. These are descriptive,
not a quality verdict. Paragraph mean fell from 97.3 to 81.1 words and abstract
prose from 160 to 142 words in that measurement; the added explanation is
concentrated in the previously underexplained Forrelation and simulator steps.
The final measurement includes the phase qualification and source page-break correction.

Source checks confirm that section/equation numbering and generated link
region are preserved, and no dotted Lean identifiers or execution hashes were
added to the paper prose. A sequential read caught and removed mechanical
duplicate boundary prefixes introduced by the replacement script. Quantum
and classical auditors checked the settled mathematical interfaces; the
parent owns final link regeneration, full rendered inspection and `make check`.
No commit was made by this writer.


Writer handoff source SHA-256 (before parent link regeneration): `1fc60226cd4b7dd786026fba5797550b5f44c9e6b87213c2f305fa20526f41ce`.

Writer validation: equation-tag sequence unchanged; generated Lean-link block byte-identical; every citation key resolves in the bibliography; every linked record anchor exists in the current record; duplicate-heading checks and scoped `git diff --check` pass. These checks do not replace the parent's full generated-source and rendered-output checks.


## Corrective pass: remove prose tables

The user rejected cramped prose-heavy tables after inspecting the long record,
then clarified that readable tables are acceptable. This pass applies that
readability criterion without reopening the mathematics. Full-width prose is
the chosen presentation for both expert-paper tables: the historical sequence
fits in a paragraph and the counterexamples need room for their hypotheses
and calculations. The expert paper now contains no tables or boxed cards,
but that is a local editorial choice, not a universal table ban. Earlier
dispositions retaining those two tables are superseded as presentation
decisions; their mathematical content is preserved.

The historical table's five rows are now the final paragraph of §1.1. The OR
quadratic benchmark, the 5/2, 8/3, 3 and 4 separating exponents, every source
citation and the different quantifier direction of the universal quartic
bound remain explicit.

The eight former Appendix A rows now have full-width prose destinations:

- Promise inference from the projection statistic: §A.1 retains the exact k=2,
  m=4, negative-Phi witness and its record link.
- Total-order or fixed-orientation comparisons: §A.2 retains both the
  deterministic loser cycle and the unbiased-pair example, with the record link.
- Accepting a dominant column: §A.3 retains the all-one first column, zeros
  elsewhere, one false pointer, smaller-index tie-break and lack of a winner.
- Uniform marginal planting: §A.4 retains the adaptive selection experiment,
  175/256 versus 1/4 comparison, independence requirement and record link.
- Expected query caps: §A.5 retains two parity instances, cap one per instance,
  the fair mixture and 5/8 versus beta-squared comparison.
- Separate versus joint independence: §A.6 retains the zero-query XOR
  side-information example, 1/2 versus 1/4 probabilities and record link.
- Conditioning on compliance: §A.7 retains the adaptive repeated-query
  experiment, all sixteen cases through their exact counts, both 5/16 and 5/8
  probabilities and the trace destination. The probabilities are displayed at
  ordinary text width.
- Growing a fixed parameter: §A.8 retains the threshold counterexample and its
  connection to the uniform estimates used in §6.

All main-text references to Table 1 now name the appropriate Appendix A
subsection. The general beta convention and the distinction between finite
examples and the asymptotic construction remain at the appendix opening.
This corrects the presentation choices associated with EF011, EF068,
QS009, QS068, NR123, NR150, LS008, LS043 and LS057 while preserving their
substantive scope. Earlier advice to keep these tables is superseded by the user's later
readability criterion. This choice does not prohibit a useful readable table
in another passage or paper.

Validation: no Markdown pipe table or Table 1 reference remains; the sequence
of equation tags (1)–(16) and the complete generated Lean-link region are
unchanged. All prior appendix record-link targets remain present. The parent
and cold reader receive a stable-source signal for fresh rendering and
inspection. No commit was made.

Corrective-pass source SHA-256 before parent regeneration: `ec54af20ef6989cfaa40cb054e2cd9cf0b5d9aa8acd24863df975e046eda5187`.

The corrective pass also checked link labels: they remain natural mathematical phrases (for example, “exact conditional label law” and “uniform estimate (16)”), not exposed declaration names or raw URLs. The generated link destinations remain separate from the prose.
