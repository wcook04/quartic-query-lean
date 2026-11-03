# Classical-mechanism findings

Round 5 · 3 November 2026 · packet `classical_mechanism`

34 findings: 3 high, 14 medium, 6 low, 11 keep.

This is a readable mirror of `findings.json`. Severity orders revision priority; `keep` records successful changes. The core classical lower-bound proof was not found to fail. No new theorem, manuscript rewrite, Lean build, or Comparator run is claimed. Exact editions and reading limits are in `source_coverage.md`.

## CM-001 · high · credit

**Paper and location:** expert_companion · 6. The Forrelation lower bound; related passage in 1.1 Where this sits

> Sherstov, Storozhenko and Wu prove a sharper bound

The surrounding subject is the lower bound for the explicit Walsh-Hadamard promise P_{k,m}, but SSW's separation theorem concerns rorrelation for a uniformly random orthogonal matrix. SSW themselves call their result and Bansal–Sinha's incomparable. The record instead uses SSW's stronger Fourier-growth theorem in a separately derived comparison (F56)–(F60). Section 1.1 also says that both teams proved the Aaronson–Ambainis k-fold Forrelation conjecture, conflating the exact explicit problem with the general optimal partial separation.

**Reader impact.** Bansal–Sinha and SSW readers will see their different mathematical statements merged, and may infer that SSW is a stronger replacement for the precise ingredient used here.

**Revision direction.** Distinguish the common optimal partial-separation milestone from the explicit-Hadamard theorem. If the intended reference is the sharper Fourier comparison, identify that theorem and the record's deduction explicitly; do not attribute the latter deduction directly to SSW.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 243; exact quote independently matched
- literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/source.pdf; arXiv:2008.10223v4, 29 January 2023; Theorem 1.1, p. 3; §1.8, p. 10; Fourier Corollaries 4.14–4.15, statements p. 35, proof continues p. 36; [Primary source](https://arxiv.org/pdf/2008.10223v4)
- repository/docs/reasoning_record.md; §3.16, forr_ssw_comparison, equations (F56)–(F60); §3.18 forr_references
- repository/docs/expert_companion.md; §1.1, phrase ending "which Bansal and Sinha and Sherstov, Storozhenko and Wu proved"

## CM-002 · high · unclear

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — The true cell

> For a light column, we show that the run reaches its true cell with probability at most about $(2/3)^r$ per query.

This preview reads as a success bound conditioned on being light. The valid assertion bounds the joint event that the column is light and a fixed query visits its true cell. The distinction is handled correctly later, but the first description states the tempting invalid reading just before teaching why it fails.

**Reader impact.** Direct-product specialists will see a mismatch between the preview and the formal event. A student can retain the intuitive preview while treating the later warning as unrelated technical bookkeeping.

**Revision direction.** Name the joint event at this first appearance, and reserve “conditional on lightness” exclusively for the counterexample. Keep the exact simulator inclusion that follows.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 222; exact quote independently matched
- repository/docs/exposition.md, lines 222, 233, 235–241
- repository/docs/expert_companion.md, §5.4, equation (12)
- repository/docs/reasoning_record.md, §6.1, CL-joint-cap and §6.5, CL-joint-event

## CM-003 · high · unclear

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — The true cell

> Reaching the true cell $B_{I,s_I}$ requires knowing $s_I$

This categorical claim excludes the possibility that the algorithm guesses the address and happens to query the true cell. That possibility is exactly what the capped direct-product bound controls. The subsequent simulator proof is sound, but the sentence gives the student an incorrect reason for its conclusion.

**Reader impact.** Readers of cheat sheets and direct products will distinguish computing an address from guessing it. Students may infer that every successful cell visit forces an address-computation lower bound, bypassing the essential probabilistic reduction.

**Revision direction.** Make the first description include both costly address learning and lucky address guessing, using the already present argument; do not suggest a new information-theoretic theorem.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 222; exact quote independently matched
- repository/docs/exposition.md, line 222 versus simulator and joint event, lines 235–241
- repository/docs/expert_companion.md, §1.2, line 54 explicitly includes guessing
- paper/extracted.md, §4 opening, lines 516–520
- repository/docs/reasoning_record.md, §6.5, CL-simulator and CL-joint-event

## CM-004 · medium · unclear

**Paper and location:** expert_companion · 1.2 The idea

> it must invest about $L$ queries in a constant fraction of the $m$ columns

The overview turns the address route into a necessary behaviour of every distinguisher. The planted pair can also be distinguished by exhaustively scanning the X strings, without any address query, at cost m². The actual proof rules out both routes within G=⌊mL/100⌋: the erased-zero estimate uses L≤m, while heavy columns and unlikely guesses control the cell route. Omitting the zero route makes the claimed necessity stronger than the argument.

**Reader impact.** Cheat-sheet and randomized-query readers will immediately test whether a certificate can be bypassed by inspecting the X data. The answer is the two-event accounting, not a universal obligation to learn many addresses.

**Revision direction.** Include the erased-zero alternative when previewing the mL cost and state the conclusion as a lower bound at the chosen budget. Use the two routes already proved in §5.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 54; exact quote independently matched
- paper/extracted.md; §4 opening, lines 516–520; §4.2, equations (18)–(23)
- repository/docs/expert_companion.md; §5.2–§5.5, especially (10), (11), (13) and L≤m
- repository/docs/reasoning_record.md; CL-entry-interface; CL-first-difference; CL-tail-numeric

## CM-005 · medium · missing

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — The pair

> In each column $i$ choose one position $J_i$ uniformly

The paragraph specifies uniform zero locations but does not explicitly give their joint independence from one another and from the address inputs. Uniform marginals alone do not justify the conditional-uniform search estimate or the simulator’s independent outside information. The intended product law is unambiguous in the preprint and record and should survive this compression.

**Reader impact.** The intended audience includes researchers who study adaptive conditioning. They will notice that the later argument needs a product distribution while the displayed sampling instructions only explicitly call the address inputs independent.

**Revision direction.** Specify that the zero positions and all address inputs are drawn mutually independently; retain the separate statement that I is independent of the entire dummy experiment.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 203; exact quote independently matched
- repository/docs/exposition.md, lines 203, 218, 235
- paper/extracted.md, §4.2, lines 600–602 explicitly separates and joins these independence requirements
- repository/docs/reasoning_record.md, §6.3, CL-dummy, lines 3365–3376

## CM-006 · medium · missing

**Paper and location:** both · Exposition 5, The erased zero; expert 3, Table 1 row 4

> Suppose instead that $I$ is chosen uniformly among the discovered columns whenever there are any.

The counterexample leaves I undefined when no zero is discovered, an event of probability 81/256. The following claim that I has a uniform marginal requires a symmetric rule on that event. Choosing a fixed column there would not preserve uniformity. The record supplies the missing rule: choose uniformly among all four columns.

**Reader impact.** Probability readers cannot assess the claimed joint law until every branch of the sampling rule is specified. This is precisely an example meant to teach the difference between a marginal and a joint distribution.

**Revision direction.** Restore the no-discovery fallback from the record in both this paragraph and the companion’s Table 1 row 4. Keep the numerical contrast 175/256 versus 1/4.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 220; exact quote independently matched
- repository/docs/exposition.md, line 220
- repository/docs/expert_companion.md, Table 1 row 4, line 117 has the same omission
- repository/docs/reasoning_record.md, CL-selection-independence-example, lines 3450–3456 explicitly gives uniform fallback
- checks/finite_checks.json: exact enumeration over 256 zero-position tuples

## CM-007 · medium · credit

**Paper and location:** both · Expert 5.1 A direct product with separate caps; exposition 5, Direct product with separate caps

> This is the separately capped mechanism of Shaltiel and Drucker

The attribution is directionally correct, but the short papers omit the precise distinction already present in the record. Drucker Lemmas 3.1–3.2 supply the value inequality and posterior product law; the fair specialization is explicitly stated at the end of §3. His headline Theorem 1.1 instead has a global budget and a weaker success bound. The supplied Shaltiel report states an XOR-advantage theorem in the uniform-input setting. The exposition cites only Drucker's two ingredient lemmas and omits Shaltiel entirely.

**Reader impact.** Direct-product readers need to know whether this is the familiar fair-tree argument, a use of Drucker's global-budget theorem, or a claimed new extension. The present compression also sends a reader to component lemmas rather than the exact fair specialization.

**Revision direction.** Add one compact source note giving Drucker §1.3 and the final paragraph of §3, and the original Shaltiel fair-tree locator with its formulation differences. Distinguish the global-budget theorem without adding its proof. The detailed distinctions are already in record §6.1.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 182; exact quote independently matched
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/source.pdf; arXiv:1005.0644v2, 9 May 2014; §1.1 footnote 3, p. 3; §1.3, pp. 6–7; Lemmas 3.1–3.2, pp. 11–12; final paragraph of §3, p. 13; Theorem 1.1, p. 4; [Primary source](https://arxiv.org/pdf/1005.0644v2)
- literature/quartic-ref-22-towards-proving-strong-direct-product-theo/source.pdf; ECCC TR01-009, 2001, not journal-numbered edition; §1.1 footnotes 1–2, printed p. 1; §5 Definition 4 and Theorem 5, printed p. 11; Lemma 7, printed p. 12 (PDF pp. 2, 12–13); [Primary source](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/Paper.pdf)
- repository/docs/reasoning_record.md; §6.1, CL-literature-and-verification; §6.2, CL-address-guess

## CM-008 · medium · credit

**Paper and location:** exposition · 2. One column, then four

> The new features are a separate cell array in every column, pointers that point outward, and the tournament of Section 4.

Calling outward pointers a new feature without qualifying the combination overstates their novelty. Ambainis et al. explicitly considered direct pointers from the special element to a zero in every other column. They rejected that form for their Boolean construction because it creates an exponential alphabet. The expert companion already acknowledges this antecedent, so the two drafts give different impressions.

**Reader impact.** Pointer-function authors will notice that an explicitly discussed earlier design is presented as new; the actual role of addressing and bitwise access becomes less clear.

**Revision direction.** Qualify novelty as the use and combination of these ingredients in this construction, and attach the exact pointer-function locator already supported by the packet. Keep the separate-cell-array and tournament explanation.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 89; exact quote independently matched
- literature/quartic-ref-04-separations-in-query-complexity-based-on-p/source.pdf; arXiv:1506.04719v3, 26 October 2015; §1.3, "Use of a balanced tree", p. 6, final paragraph; [Primary source](https://arxiv.org/pdf/1506.04719v3)
- repository/docs/expert_companion.md; §1.1, "the direct outward pointers used here are discussed by Ambainis et al."

## CM-009 · medium · lean_link

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — Direct product with separate caps

> Lean also proves the version for coins and side information on arbitrary independent probability spaces

The linked compared declaration quantifies over a finite seed type Ω with [Fintype Ω] and real weights. The companion distinguishes that formal theorem from the ordinary finite-behaviour reduction covering arbitrary independent randomness. The exposition instead describes the latter as a Lean theorem over arbitrary probability spaces. The supplied target does not display that quantification; this is a statement-to-link mismatch, independent of the rebuild status.

**Reader impact.** A reader checking the advertised formal scope can mistake an ordinary reduction to the Lean model for a separately mechanised arbitrary-space theorem.

**Revision direction.** Match the companion’s distinction between the finite formal theorem and the ordinary finite-behaviour reduction, or identify an already-existing formal arbitrary-space target if one is intended. Do not require new formalisation.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 230; exact quote independently matched
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean; lines 18–25; [Fintype Ω] and finite sum.
- repository/docs/expert_companion.md; lines 182–182; Explicitly says arbitrary finite probability space, then adds the finite-behaviour argument.
- repository/docs/reasoning_record.md; lines 3695–3702; Ordinary finite-behaviour reduction is distinguished from a formal pushforward theorem.

## CM-010 · medium · lean_link

**Paper and location:** expert_companion · 5.1 A direct product with separate caps

> Lean proves Lemma 4 with coins and side information drawn from an arbitrary finite probability space jointly independent of the inputs

The linked declaration is a stronger joint-event statement, not the all-branches-capped success statement displayed as Lemma 4. Its type has no T.capped premise: it bounds a weighted sum of compliantSuccess for arbitrary finite trees. The cap event and product-input law are hidden in that imported definition. This distinction is mathematically useful, but neither the link text nor a nearby gloss tells the reader how the theorem specialises to Lemma 4 or how it matches the later success-and-cheap-run discussion.

**Reader impact.** Drucker/Shaltiel readers auditing the subtle conditional-versus-joint distinction should be able to see exactly which event Lean bounds; an opaque success name defeats the main reason to offer a formal link.

**Revision direction.** Identify the linked theorem as the original-run joint success/compliance bound, explain that the compliance event is certain for Lemma 4’s capped algorithms, and link its existing event/cap definitions. No new formalisation is needed.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 182; exact quote independently matched
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean; lines 18–25; Finite Ω; arbitrary T; conclusion ∑ω wω * compliantSuccess f μ (Tω) (fun _ => L) ≤ β^r; no all-branches cap premise.
- repository/docs/expert_companion.md; lines 174–182; Displayed lemma instead assumes a cap on every branch and bounds success.
- repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean; lines 3–8; Imports cap/tree/success definitions from LowerBound.RealizedCaps; that source module is not packaged.
- Pasted text(20261103-030534).txt (separate supplied attachment); lines 61644–61652; Historical trace excerpt explicitly defines compliantSuccess as success AND actualComplies under product input weights. Historical excerpt, not a claim of current native build.

## CM-011 · medium · lean_link

**Paper and location:** expert_companion · 5.3 The erased zero

> Lean proves (11) with the bound $4G/m^2$ as a [directly compared statement][cmp-eq11]

The link correctly reaches a conjunction containing both equality and inequality, but the terms hitProbability and expectedCount are imported from a separate specification and are not defined in the linked file. The crucial independent product experiment therefore cannot be audited by reading that declaration alone. The record provides exactly the explanation and specification path needed, but the companion does not direct the reader to them, and Spec.lean is not supplied in this packet.

**Reader impact.** For a reader concerned about the planted-index independence assumption, checking the shape “hit = expectation/m” is insufficient: they must inspect the law that defines hit and expectation.

**Revision direction.** Pair this theorem link with the existing independent experiment specification and its record explanation, including the independent 1/m factor for I. Include that already-existing specification when presenting the packet as locally inspectable.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 211; exact quote independently matched
- repository/lean/QuarticCorpus/Independent/Eq19/Challenge.lean; lines 3–24; Imports Eq19.Spec and states the conjunction in imported hitProbability/expectedCount vocabulary.
- repository/docs/reasoning_record.md; lines 3797–3797; “An independently written product experiment” explains each independent factor and links Spec.lean/Bridge.lean.
- repository/corpus/comparator_map.json; Eq19 checked_eq19 is a configured direct target; this is a semantic navigation request, not a dispute of its target status.

## CM-012 · medium · lean_link

**Paper and location:** expert_companion · 5.5 The contradiction and the constants

> Full proof: [record §6]

The “Full proof” link lands at #CL-discrepancy, which is the start of record §6.6. It skips the direct product (§6.1), minimax (§6.2), coupled inputs (§6.3), erased zero (§6.4), and capped simulator (§6.5). All are in the record, but the destination gives the reader only the closing combination while advertising the full proof.

**Reader impact.** An expert following the link to check the dependence or cap subtleties lands after the relevant arguments and has to search backwards through a long record.

**Revision direction.** Use the section-entry destination for the whole proof and add specific existing anchors where the zero identity and simulator are invoked.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 239; exact quote independently matched
- repository/docs/expert_companion.md; lines 239–239; URL ends #CL-discrepancy.
- repository/docs/reasoning_record.md; lines 2847–2851; Classical section and direct-product entry.
- repository/docs/reasoning_record.md; lines 3642–3648; Actual destination is §6.6, combining prior results.

## CM-013 · medium · structure

**Paper and location:** expert_companion · 5.4 The planted cell (also 5.2 Planting a winner) · supplied PDF p. 8

> ### 5.4 The planted cell

Two of the five classical-proof subsection headings are rendered as literal Markdown inside the previous paragraph. In the supplied PDF p. 7 prints “### 5.2 Planting a winner” after the direct-product formal-status sentence; p. 8 similarly prints “### 5.4 The planted cell”. The current Markdown omits a blank line before both headings. This visibly hides the two structural transitions the proof most needs.

**Reader impact.** Direct-product and query-complexity readers scanning for the hard input and the capped simulator lose the proof outline; the otherwise careful rendering looks unfinished.

**Revision direction.** Restore the section breaks in the maintained source and inspect these two rendered pages after regeneration.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 212; exact quote independently matched
- repository/docs/expert_companion.md; lines 182–185; No blank line before the 5.2 heading.
- repository/docs/expert_companion.md; lines 211–214; No blank line before the 5.4 heading.
- repository/docs/expert_companion.pdf; PDF pages 7, 8; Visually rendered and inspected: both ### strings appear inline.

## CM-014 · medium · figure

**Paper and location:** both · Expert 5.2 Planting a winner; exposition 2 and 5

> The two coupled inputs. They differ only at the erased zero

The source figure for this planted-pair caption is not included in the packet. The same is true of the exposition’s four-column board and planted pair: figures/expert_planted.svg, figures/exposition/fig2_board.svg and figures/exposition/fig4_planted.svg are absent. The corresponding pictures are present in the PDFs, so this is missing reproducible source and broken relative Markdown rendering, not missing PDF artwork or ZIP corruption. LINK_MAP.json reports zero problems but omits all three references.

**Reader impact.** Authors and referees comparing the argument with its central figures cannot inspect or rebuild the current Markdown faithfully from the supplied packet; the claimed link audit does not expose the omissions.

**Revision direction.** Include the existing three figure sources and make the link audit enumerate every current image reference as well as ordinary hyperlinks.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 187; exact quote independently matched
- repository/docs/expert_companion.md; lines 187–187; References the absent expert_planted.svg.
- repository/docs/exposition.md; lines 97–97; References the absent fig2_board.svg.
- repository/docs/exposition.md; lines 205–205; References the absent fig4_planted.svg.
- LINK_MAP.json; 74 link rows, problem_count=0; none of those three image paths is listed.
- repository/docs/expert_companion.pdf; PDF pages 8; Planted figure visibly present.
- repository/docs/exposition.pdf; PDF pages 4, 9; PDF text confirms board on p.4; planted figure visually inspected on p.9.

## CM-015 · medium · structure

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — Why the event must be joint

> The same failure appears with two instances.

The two-instance example immediately repeats a one-instance counterexample without explaining what it adds. Its genuine additional lesson is that conditioning on the cap can create dependence between initially independent blocks even though every fixed transcript is a rectangle. That distinction is explicit in the record but absent here, so the second, more artificial algorithm looks like redundant arithmetic. The repeated query deliberately spends budget without learning a bit; its role in defining the cap event is also left unexplained.

**Reader impact.** Students must retain two distributions, two one-query success parameters, two cap events and a repeated-query rule in one paragraph. Direct-product readers expect the second example to demonstrate inter-block dependence rather than merely another numerical violation.

**Revision direction.** Give the two-instance example a distinct job: explain that the cap event can create dependence between blocks, and that the repeated query deliberately spends budget. Alternatively, retain the simpler three-input example here and link the two-instance calculation in the record. Both arguments already exist.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 233; exact quote independently matched
- repository/docs/exposition.md, line 233
- repository/docs/reasoning_record.md, §6.1, CL-adaptive-example, especially lines 3119–3124
- repository/docs/reasoning_record.md, §6.5, CL-conditioning-counterexample, lines 3625–3627

## CM-016 · medium · misplaced

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — Standard proof: minimax

> Take closest points $a\in K$ and $c\in O$ and put $v=c-a\ne0$.

The full convex-separation proof appears before the planted pair, delaying the construction that explains why a hard distribution is needed. It introduces an orthant, Euclidean projections and a squared-norm gap without a worked example. This is a much larger prerequisite burden than the specific finite-minimax consequence used below.

**Reader impact.** The cited-literature readership already knows Yao’s principle, while a strong student who does not know convex separation is unlikely to learn it from this compressed box. Both audiences lose momentum before the new mechanism.

**Revision direction.** Keep the precise one-law-for-all-depth-L-trees statement at the entry point; relocate the standard proof to the record or after the mechanism, with a precise link. Preserve the separate end-of-proof averaging argument.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 200; exact quote independently matched
- repository/docs/exposition.md, lines 197–203
- repository/docs/expert_companion.md, §5, line 170 invokes finite minimax in one sentence
- paper/extracted.md, §4.1, lines 575–589
- repository/docs/reasoning_record.md, §6.2, CL-minimax contains the complete argument

## CM-017 · medium · unclear

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — Direct product with separate caps

> with a total budget of $rL$, an algorithm could spend everything on a few blocks.

The sentence identifies a different budget hypothesis but leaves the numerical failure of the exact β^r conclusion to the reader. The next AND example is used only for conditioning, although the record uses the same distribution to show the pooled-budget distinction: with two total queries, compute the first AND exactly and guess zero on the second, succeeding with probability 3/4 rather than 9/16. Fixed uneven allocation already suffices for this example; adaptive allocation is a further mechanism in the general Shaltiel/Drucker obstruction.

**Reader impact.** A student can ask why spending the queries on a few blocks helps when every answer must be correct. Connecting the already-used AND distribution to the pooled budget answers that question without introducing another model or example.

**Revision direction.** Reuse the record’s existing 3/4-versus-9/16 comparison as the short bridge, and give a precise pointer to Drucker §4 for the general Shaltiel obstruction. Keep the pooled, expected, and separate worst-case budgets distinct.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 229; exact quote independently matched
- repository/docs/reasoning_record.md; §6.1, CL-adaptive-example, paragraph beginning “The same distribution distinguishes the two budget conditions.”
- repository/docs/reasoning_record.md; §6.1, CL-adaptive-example, final two paragraphs
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/source.pdf; arXiv:1005.0644v2; §4, pp. 13–14, separate general easy/hard selector-and-parity obstruction; [Primary source](https://arxiv.org/pdf/1005.0644v2)
- literature/quartic-ref-22-towards-proving-strong-direct-product-theo/source.pdf; ECCC TR01-009; §3.1–3.3, printed pp. 5–7

## CM-018 · low · misplaced

**Paper and location:** expert_companion · 5.3 The erased zero

> The preprint's early-and-late count gives $4G/m^2$, which also suffices.

The reference-input count is correct and concise, but its optional status appears only after the full calculation. The m+1 refinement improves a harmless discrepancy constant; the original coefficient-four bound already proves the separation and the displayed 1/400 coefficient. A reader should not mistake the refinement for a repair required by the preprint.

**Reader impact.** Experts auditing OpenAI’s construction want to identify the proof obligations that are essential to the theorem. The distinction between an alternative sharpening and an indispensable step should be visible before they invest in the calculation.

**Revision direction.** Label the reference-input count as an optional alternative at its introduction and identify the original sufficient bound first. Keep the clean exact identity and preserve the alternative proof in the companion or an accessible linked note.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 211; exact quote independently matched
- repository/docs/expert_companion.md, §5.3, lines 206–211 and §5.5, lines 229–239
- paper/extracted.md, §4.2, lines 618–637 and 665–675
- repository/docs/reasoning_record.md, CL-zero-optional, lines 3538–3552 and CL-tail-numeric, lines 3665–3692

## CM-019 · low · structure

**Paper and location:** expert_companion · 5. The randomized lower bound

> The lower bound applies to any partial function $P$ with an exact circuit as in §2 (iii)

The local lower-bound section starts with the generic hypotheses and direct-product proof, postponing the planted pair until §5.2. The high-level purpose is available back in §1.2, but a reader entering §5 to check this mechanism first meets its auxiliary lemma rather than the two changes whose detection must be controlled.

**Reader impact.** The preprint itself opens §4 with the erased-zero/filled-cell dichotomy. Readers of lower-bound papers use this small overview to understand why a direct product rather than a direct sum or certificate bound is needed.

**Revision direction.** Add a brief local reminder of the two indistinguishability events before the generic hypotheses, or introduce the pair before the auxiliary lemma. Do not repeat the full overview or rewrite the proof.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 170; exact quote independently matched
- repository/docs/expert_companion.md, §5 opening and §§5.1–5.2
- paper/extracted.md, §4, lines 516–520
- repository/docs/reasoning_record.md, §6.2, CL-entry-interface, lines 3296–3298

## CM-020 · low · missing

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — The simulator

> Summing over $j\le G$, averaging over the independent uniform $I$, and adding the heavy case,

The key absence of an extra factor m is left implicit. The bound is first obtained for each fixed column, then averaged with a factor 1/m rather than union-bounded over all columns. A student can reasonably expect mG(2/3)^r after tracking both column and time indices.

**Reader impact.** The exposition aims to teach why the randomized budget is mL. Explaining which operation sums over time and which averages over columns prevents a spurious extra factor from obscuring that scaling.

**Revision direction.** Explicitly identify the cancellation of the m identical per-column bounds under the uniform-column average, using the already supplied record explanation.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 239; exact quote independently matched
- repository/docs/exposition.md, lines 235–241
- repository/docs/reasoning_record.md, CL-cell-union, lines 3632–3639 explicitly says why no extra factor m appears
- paper/extracted.md, equation (22)

## CM-021 · low · lean_link

**Paper and location:** expert_companion · 5.3 The erased zero · supplied PDF p. 8

> The bound $2G/(m(m+1))$ is also proved in Lean

The attached link displays the finite charging invariant ((|U|+1)∑hit ≤ 2∑queries), not the normalised planted-experiment probability bound in the sentence. The reader must instantiate the possible zero worlds, divide, average outside information and use the global budget to recognise the displayed endpoint. Those steps are already present in the mathematical discussion, but the link is described as if it displays the endpoint directly.

**Reader impact.** Readers checking exact formal correspondence need to distinguish the named finite invariant from its probability interpretation; this is especially valuable next to an explicitly direct Eq19 target.

**Revision direction.** Describe the linked object as the charging invariant supplying the sharper bound and point to the existing averaging argument. Keep its proof-route and comparison scope distinct from the direct Eq19 endpoint; do not request a new theorem.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 211; exact quote independently matched
- repository/lean/QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean; lines 17–22; Statement is a sum over U, with c counting queries to the selected coordinate set.
- repository/docs/expert_companion.md; lines 206–211; Prose already supplies the per-column and outer averaging reasoning.

## CM-022 · low · credit

**Paper and location:** expert_companion · 5.2 Planting a winner

> and leaves every cell blank.

The introductory history credits the addressing device, but the lower-bound section does not connect its blank-array/filled-true-cell coupling to the earlier cheat-sheet lower-bound proof. ABK Lemma 6 already uses a blank array and then changes only the true cell to force the algorithm to query that cell. Here the independently erased zero adds a second channel and the column averaging produces the extra factor.

**Reader impact.** Cheat-sheet readers would benefit from seeing precisely which part of the lower-bound mechanism is inherited and which new two-location accounting they should inspect.

**Revision direction.** Add a short mechanism-level pointer to ABK Lemma 6 when introducing the coupled pair, and distinguish the additional erased-zero channel and column cost. No proof detour is needed.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 185; exact quote independently matched
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/source.pdf; arXiv:1511.01937v2, 9 July 2019; §3.2, Lemma 6, pp. 12–13; opening claim in its proof on p. 13; [Primary source](https://arxiv.org/pdf/1511.01937v2)
- paper/extracted.md; §4 opening and §4.2 coupled pair

## CM-023 · low · credit

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — opening

> By the minimax theorem there is a distribution

The exposition invokes the exact distributional-to-randomized principle central to this section but does not name Yao or cite the source, even though the expert companion does and the preprint supplies reference [27]. Its optional proof box is longer than the missing attribution would be.

**Reader impact.** Readers trying to connect the argument to query-complexity literature are given a generic theorem name rather than the standard identifiable principle.

**Revision direction.** Name and cite Yao's principle at this first use, retaining the compact finite formulation. Keep any elementary proof optional rather than enlarging it.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 197; exact quote independently matched
- paper/extracted.md; §4.1, immediately after Lemma 4.1, minimax display and reference [27]
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/source.pdf; arXiv:1005.0644v2; §5, Lemma 5.1, p. 14; [Primary source](https://arxiv.org/pdf/1005.0644v2)
- Yao1977; FOCS 1977, pp. 222–227; cited only, original not read

## CM-024 · keep · keep

**Paper and location:** expert_companion · 5.4 The planted cell

> Its total cap on the $A_{i,h}$ is $L$, so Lemma 4 applies.

This is the decisive reduction: an L-total-query simulator has the L-separate-cap property, and its success contains the original correct-and-nonheavy event. The proof never conditions the hard law on nonheaviness. The lower bound therefore pays only L per potentially useful column, not rL.

**Reader impact.** Direct-product specialists will check this interface before accepting the mL scaling. It is short, explicit, and avoids the exact conditioning shortcut the counterexamples warn against.

**Revision direction.** Keep the total-cap-to-separate-caps sentence, the event inclusion and the explicit joint-event display together. Do not compress them into a conditional-success slogan.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 216; exact quote independently matched
- repository/docs/expert_companion.md, §5.4, lines 214–223
- repository/docs/exposition.md, simulator, lines 235–241
- paper/extracted.md, §4.2, lines 647–663
- repository/docs/reasoning_record.md, CL-simulator and CL-joint-event

## CM-025 · keep · keep

**Paper and location:** expert_companion · 5.3 The erased zero

> This identity uses that $I$ is independent of the whole dummy run; a uniform marginal law is not enough

The exact identity Pr(hit)=E Z/m is now separated from the search-cost estimate, and the independence hypothesis is stated at precisely the point where it is used. This is a successful repair of the earlier editorial finding.

**Reader impact.** Probability and direct-product readers can check the identity without reading the zero-search proof or importing any Forrelation hardness assumption.

**Revision direction.** Preserve the identity-first order and the whole-run independence statement. Repair the finite counterexample’s missing fallback rather than removing the counterexample.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 204; exact quote independently matched
- repository/docs/expert_companion.md, equations (11) and following paragraph
- repository/docs/exposition.md, lines 214–220
- repository/docs/reasoning_record.md, CL-erased-zero-identity, lines 3434–3445

## CM-026 · keep · keep

**Paper and location:** expert_companion · 5.5 The contradiction and the constants

> A randomized algorithm of worst-case cost $G$ is an average of such trees

The passage correctly separates obtaining μ by minimax from averaging the final deterministic discrepancy bound over coins. There is no unsupported assertion that one fixed seed is good on every input, and no unnecessary second minimax theorem.

**Reader impact.** Readers of randomized query lower bounds can identify the quantifiers and see why a worst-case-success algorithm would contradict the distributional gap bound.

**Revision direction.** Keep this concise averaging step and the pointwise zero-input/one-input correctness premise. The exposition’s corresponding paragraph is also sound.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 234; exact quote independently matched
- repository/docs/expert_companion.md, lines 170 and 229–239
- repository/docs/exposition.md, line 244
- paper/extracted.md, lines 676–679
- repository/docs/reasoning_record.md, CL-randomized-contradiction, lines 3697–3701

## CM-027 · keep · keep

**Paper and location:** exposition · 5. The classical lower bound: a planted pair — Finishing

> Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm.

The final sentence correctly identifies the interface needed to combine the two complexities: the randomized argument is generic in the exact realizing circuit, so it applies to the same circuit used for the quantum upper bound. It prevents an existential-witness mismatch.

**Reader impact.** Experts assessing a separation require the two inequalities to hold for one function. Students can see why proving bounds for unrelated constructions would not suffice.

**Revision direction.** Keep this explicit same-circuit conclusion alongside the lower-bound result.

**Evidence.**

- repository/docs/exposition.md; Current Markdown line 248; exact quote independently matched
- repository/docs/exposition.md, line 248
- repository/docs/expert_companion.md, §5 opening, §7 line 270
- repository/docs/reasoning_record.md, CL-concrete-lower, lines 3755–3775

## CM-028 · keep · keep

**Paper and location:** expert_companion · 7. The exponent

> The order of quantifiers is: the exponent $\alpha$, then one fixed $k$, then its constants and threshold, then $m\to\infty$

The fixed-k proof now states its quantifier order and its limitation explicitly. The later growing-k schedule is separately labeled and discloses its reliance on uniform estimates and its ordinary, non-Lean status. The classical constants used earlier are arithmetically consistent with the supplied record.

**Reader impact.** Forrelation specialists will distinguish a fixed-k asymptotic lower bound from a parameter-uniform family. This wording prevents an unjustified substitution k=k(m).

**Revision direction.** Keep this separation and the statement that no exact Ω(Q^4) bound follows. Any shortening of the growing-k remark should retain its assumptions.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 270; exact quote independently matched
- repository/docs/expert_companion.md, §5.5 lines 229–239; §6 lines 243–248; §7 lines 266–277
- repository/docs/exposition.md, §6 lines 252–264
- repository/docs/reasoning_record.md, CL-floors and §7.1–§7.2

## CM-029 · keep · lean_link

**Paper and location:** expert_companion · Appendix A. Checking the statement

> The exponent $b$ is existential here.

The companion now keeps the compared existential logarithmic exponent separate from the explicit b=6 and 1/400 theorem. It also identifies the fixed-k quantifier order and the single circuit shared by both bounds. This resolves the earlier risk of silently giving a stronger numerical statement the status of the headline comparison.

**Reader impact.** Query-complexity experts can quickly see the exact object and quantifiers they are asked to trust.

**Revision direction.** Preserve this precise scope distinction and same-circuit wording during shortening.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 309; exact quote independently matched
- repository/docs/expert_companion.md; lines 302–317; Four compared statements, explicit-constant distinction, quantifier order.
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean; lines 328–334; ∀k ∃S,A,b,t0 ∀t ∃C, with both bounds for the same C.
- repository/lean/QuarticCorpus/Unconditional/comparator.json; Exactly the four quoted headline theorem names are configured.

## CM-030 · keep · lean_link

**Paper and location:** expert_companion · Appendix A. Checking the statement

> What remains is whether the formal statement says what Theorem 1 says.

The new single-file reading guide, definition-by-definition links, explicit worst-case caps, same-circuit quantifiers and modelling caveat are a substantial improvement. The four headline names agree with the supplied configuration, and inspected line ranges land on the intended current definitions and target types. These facts should not be confused with a fresh execution of Comparator during this review.

**Reader impact.** Researchers can separate semantic review from proof checking and inspect the theorem without traversing implementation proofs.

**Revision direction.** Keep the compact audit guide and the explicit shared-modelling-error caveat; extend its navigation discipline to the classical mechanism’s auxiliary targets.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 283; exact quote independently matched
- repository/docs/expert_companion.md; lines 283–322; Guide and modelling caveat.
- repository/lean/QuarticCorpus/Unconditional/Challenge.lean; lines 1–343; 343-line file, imports Mathlib, target vocabulary visibly local.
- repository/lean/QuarticCorpus/Unconditional/Solution.lean; Four wrapper proof references match the named targets; no execution was performed.
- checks/link_checks.json; Independent local line-range checks; no live GitHub or Lean execution claim.

## CM-031 · keep · lean_link

**Paper and location:** expert_companion · 5.3 The erased zero

> as a [directly compared statement][cmp-eq11]

The target selected for (11) now includes the exact erased-zero equality together with the coefficient-four inequality as one conjunction. It is not merely the older implementation theorem that bounds the hit probability. That is the right formal object to show beside the independence discussion.

**Reader impact.** Referees can distinguish preservation of the full displayed identity from a proof of only its weaker endpoint.

**Revision direction.** Keep this direct conjunction target; add its definition path as requested separately.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 211; exact quote independently matched
- repository/lean/QuarticCorpus/Independent/Eq19/Challenge.lean; lines 19–24; Equality AND bound.
- repository/corpus/comparator_map.json; QuarticQuery.Independent.Eq19.checked_eq19 is recorded with direct configured target credit and the eq-19 tie.

## CM-032 · keep · keep

**Paper and location:** expert_companion · 2. The construction — property (i)

> This follows from Bansal and Sinha's bound

The quoted quantitative lower bound is correctly specialized to the exact one-sided promise delta=2^{-5k}. Bansal–Sinha Theorem 1.3 and Corollary 1.4 give the displayed k^{-29} factor and logarithmic loss. For fixed k, dividing m^{1-1/k} by (log_2 m)^2 leaves strictly more logarithmic slack, so the eventual inequality L<R(P) is justified.

**Reader impact.** Forrelation readers can verify the one literature ingredient without trusting the alternative Lean proof or an inappropriate rorrelation transfer.

**Revision direction.** Preserve this concise interface, its fixed-k scope, and the exact source locator when shortening the separate Forrelation section.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 85; exact quote independently matched
- literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.pdf; arXiv:2008.07003v3, 17 November 2020; definition (1.3), p. 3; Theorem 1.3 and Corollary 1.4, p. 4; [Primary source](https://arxiv.org/pdf/2008.07003v3)

## CM-033 · keep · keep

**Paper and location:** expert_companion · 5.1 A direct product with separate caps

> zero-weight branches need no division.

The nonnegative-measure value recursion gives a short, complete proof of the required fair-tree bound and avoids undefined conditional probabilities on zero-mass branches. It is a useful concise presentation of the same mechanism explained by the conditional-value proof in the preprint and Drucker.

**Reader impact.** Direct-product readers can audit adaptivity and the zero-mass edge case without a long standard amplification or minimax excursion.

**Revision direction.** Preserve the unnormalized formulation and the final fix-and-average step, with clearer proof provenance rather than a longer proof.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 180; exact quote independently matched
- repository/docs/reasoning_record.md; §6.1, CL-weighted-values, CL-weighted-product, CL-normalization
- paper/extracted.md; §4.1, proof of Lemma 4.1
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/source.pdf; §3, Lemmas 3.1–3.2 and fair specialization

## CM-034 · keep · keep

**Paper and location:** expert_companion · 1.1 Where this sits

> The cheat-sheet arithmetic shows why the earlier route stopped at the cube.

The new history table and calculation now explain the 5/2, 8/3-o(1), and 3-o(1) milestones and connect the cubic route to AND-OR composition and certificate verification. The numerical comparison is supported by ABK §3.1 and the Bansal–Sinha/SSW total-function corollaries. This resolves an important predecessor criticism.

**Reader impact.** The cited-literature audience can see what changed structurally instead of being given an isolated exponent claim.

**Revision direction.** Keep the arithmetic and accurate independent credit; correct only the separate explicit-Forrelation versus rorrelation attribution noted above.

**Evidence.**

- repository/docs/expert_companion.md; Current Markdown line 44; exact quote independently matched
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/source.pdf; arXiv:1511.01937v2; §1 introduction, p. 2; §3.1, pp. 9–10; §3.2, Theorem 5 and Lemma 6, pp. 11–13
- literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/source.pdf; Corollary 1.5, p. 4
- literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/source.pdf; §1.3, Theorem 1.5, p. 4
