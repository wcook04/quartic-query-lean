# Round-ten critique: the complete reasoning record

## Judgment and scope

The most valuable revision is to make the complete proof easier to hold in view while preserving its reconstructibility. The current record supplies the major mathematical bridges that earlier rounds requested. The remaining work is concentrated: put the total construction ahead of the long analytic supplier proof; show the complete bounded quantum evaluator before its subroutines; keep the successful-sampler law adjacent to the coupling that uses it; and finish the planted reduction before presenting unused alternatives. Two smaller repairs concern an exact gate-count ledger and the identity of a running board. One residual source-status sentence needs a narrower claim. A final, optional change would put current formal statements before their execution history.

These are eight consolidated recommendations, in source order in `feedback.json`. The impact ranking is separate. None is a verified mathematical-error finding. That conclusion is bounded by the actual source, mathematical and formal inspections documented in `supporting_reviews/`; it is not a certification of the full development.

The primary reader covered all 6,781 lines of the lead, including every appendix, the catalogue, references and terminal link definitions. Its evidence is a frozen, prospective **batch** encounter record. It does not meet the stronger ideal of independently recording a cognitive state before exposure to every next sentence. The 4,262 rows include mechanically segmented sentence candidates and shared block annotations. All later corrections and judgments remain separate. In particular, an early suspicion that §3.18 was missing was disproved, and an early claim that the supplier interface appeared only at §3.17 was withdrawn. These corrections materially reduced the final finding set. See `reading_log.md`, `coverage.json` and `supporting_reviews/primary_adjudicated_candidates.json`.

All manuscript locators below refer to the submitted, hash-bound source, not to a proposed revision. Source IDs such as P0, QS04 and CLS-S01 resolve to editions, URLs and inspected passages in `sources/` and `literature_comparison.md`.

## 1. Make the object explain the need for the supplier

**RR10-001 — opening and §§3–4; lines 3–42, 114–154, 441–1669 and 1670–3971.**

The record asks an outsider to understand three distinct resources: a partial function that is hard for classical queries, a capped quantum proposal that is reliable on its promise, and an exact Boolean circuit that recognizes both the domain and the value. Their difference matters because the eventual total input supplies a purported transcript. Checking local consistency of that supplied transcript is a different task from computing the hard partial function. The total construction is where these roles become concrete.

The existing three-property preview at lines 454–460 already states a usable contract. It is therefore incorrect to diagnose a missing early interface. The stronger editorial question is whether the full publication-order route makes good use of that interface. At present the reader proceeds through the entire analytic Forrelation lower bound before seeing the complete addressed board and its local tests. The skip route helps a targeted visitor, but a complete reader still carries an uninstantiated construction through the supplier proof.

The proposed redesign uses the existing contract as an explicit pending lemma. It introduces the board, address selection, supplied transcripts and winner predicate while those obligations are still small enough to remember. The quantum and planted reductions then demonstrate why each clause is needed. A later proof part discharges the exact circuit, quantum and analytic obligations in full. This is a change of explanatory order; it imports no unchecked source theorem and deletes no derivation.

One feasible architecture is:

| Part | Reader task | Material and obligations |
| --- | --- | --- |
| Question, theorem and models | Understand what a total-function separation says and which query caps are meant | Current §§1–2; short mechanism synopsis; one task-oriented map |
| Supplier contract and total input | Know the three guarantees and operate on a complete board | Existing preview, precise promise conventions, §4 construction and tests |
| Quantum evaluation | Follow one bounded decision procedure on every input | Current §5, reorganized by RR10-004 and RR10-005 |
| Classical obstruction | Follow one pair of coupled inputs to the discrepancy contradiction | Current §6, with optional alternatives after the conclusion |
| Complete supplier proofs and parameter closure | Discharge the pending contract, then justify fixed and growing parameters | All of current §3; §7; explicit uniform estimate before its growing-parameter use |
| Verification and reference material | Inspect statement dependencies, formal routes and history | Catalogue, current status, detailed transports, source comparisons and archive |

There is a less disruptive option: keep the elementary definition, quantum decoder and exact circuit in §§3.1–3.5, but move §§3.6–3.15 after the construction and reductions. That preserves more existing exposition and leaves only the analytic lower bound pending. The choice should be tested on the complete route, not decided by how many section numbers must change.

The opening should be adjusted with the architecture. Its planted-zero/planted-cell mechanism and the comparison between an $mL$-scale classical obstruction and a square-root-$m$ quantum search belong in the synopsis. The fixed-column/fixed-time joint event, numerical repetition choice and union over query times are better placed at the lower-bound proof map, where the simulator and its counters have names. This is a recommendation about the amount of state demanded at first encounter, not a criticism of that calculation.

The redesign has costs. Deferring proofs introduces explicit debt; a reader must see which guarantees remain to be proved. Renumbering can damage the two shorter accounts' proof destinations. Accordingly, preserve old anchors or redirects, keep the three guarantees visible as a checklist of mathematical dependencies, and mark their later discharge. The same chosen circuit must serve both bounds. The decoder must remain capped even off promise. Eventual fixed-parameter hardness, the direct threshold and the uniform estimate must remain distinct. P0's construction/reduction organization and QS13's fixed pointer representation support this dependency-oriented comparison; neither source justifies replacing this record's detailed proofs with an asymptotic sketch.

## 2. Make exact accounting and the running example independently usable

**RR10-002 — §3.4, lines 773–779; PDF page 19.**

The circuit discussion explains the primitive arithmetic costs and then asserts an exact composite size $S$. The later algebra proves the advertised coarse estimate once that expression is accepted. What is missing is a short assignment of each non-transform summand, including the final constant, to the constructors that contribute it. This is the surviving part of RR9-033. It does not establish that either the identity or coefficient 200 is false.

A four-column ledger—operation, number of calls, cost per call, contribution—would make the advertised exactness reproducible. It should account for sign handling, final addition, repeated doubling, comparisons, constant gates and outputs, rather than merely repeat the resulting polynomial. If exact equality is not useful, an explicitly justified upper-bound ledger can support the needed coefficient without asserting an unshown identity. This is a local explanation, not a request for a new formal theorem.

**RR10-003 — §4.4, lines 1926–1945; PDF page 41.**

The record's four-column board and the exposition's four-column board share a circuit and gate numbering but use different input values. The former uses nonzero Forrelation values of magnitude $1/2$, while the latter includes magnitude 1. The manuscript correctly discloses the difference. The problem is that the alternate board is introduced between the definition of the current example and its worked local-test count, immediately before another reference to the four-column board.

Name the object explicitly as the §4.3 board throughout the local calculation. Complete that calculation, then place the companion-navigation note. The note should identify the transferable circuit/test specification and the nontransferable input and projection probabilities. The exposition's incoming checker link needs a landing paragraph that says which board the archived checker actually checked. No new experiment is being requested or claimed; no change to 371 tests or the displayed bit count follows from this recommendation.

This matters more than surface consistency. The purpose of the example is to let a reader carry one concrete input from representation through certification and search. If the input silently changes in the reader's working model, correct probabilities become difficult to attach to the right experiment. The remedy is stable reference, not forcing both documents to use the same example.

## 3. Give the quantum proof one program and one transition law

### A complete control-flow preview

**RR10-004 — §5 opening, lines 2063–2069, with the later tournament setup at 2227–2282.**

The opening already gives the two-stage idea: produce a short candidate list, then check it. The missing orientation is the whole finite procedure, including its stop and output rules, before the detailed amplifier and weight arguments. The rules eventually appear and are mathematically explained; the concern is their late assembly.


The preview should use named subroutines whose proofs follow. It needs the fixed stage horizon, the classical pivot list retained between stages, the rule that a failed stage sampler returns the current list, fresh decoding of each listed candidate, a fixed measured address for its tests, search for a failed exact local test, and the acceptance rule. The two amplifier thresholds should be identified as $1/(2m)$ for pivot sampling and $1/K$ for searching the local tests, with the prescribed error tolerance. The weights used in the analysis must not appear as values the implementation is assumed to know.

The crucial conceptual feature is that amplifier failure has two different meanings. During list generation it stops list extension. During search for a violated local predicate it is the event on which a candidate is accepted. This does not make the evaluator incorrect: an invalid candidate has an actual violated exact predicate and a bounded probability of failing to find it; a valid certificate has no violation. Showing this control flow first gives the subsequent success and error estimates an identifiable purpose. The Mande–Paraashar–Saurabh published Algorithm 4 is a comparison for the relation between stored history, loop and sampler, not a substitute theorem for this fractional-weight setting (QS09).

The new preview should replace repeated setup later. RR9-094 remains partly unresolved because renaming a passage as interpretation did not remove the repeated model, parameters and dominance assumption before the weight proof. Preserve the additional explanation of complementary comparisons and their error accounting; consolidate definitions that have already done their job.

### The current-history kernel is the bridge to the coupling

**RR10-005 — §5.2, lines 2445–2506; PDF pages 53–55.**

The retained-register sampler supplies exactly the conditional distribution the ideal process needs. Once the current pivot history is $L$, its successful label law is proportional to $w_i(L)$. The next mathematical step is the real/ideal coupling. At present a formal correspondence note inserts generic input-indexed masses, totals and failure notation before the proof returns to the history variables. Its content is relevant to the formal account, but its position adds a translation at the decisive probabilistic bridge.

For an active stage with $|L|<T$, the local mathematical display should instead state the real transition law directly:

\[
\Pr(\mathrm{stop}\mid L)=f(L),\qquad
\Pr(\mathrm{next}=i\mid L)=(1-f(L))\frac{w_i(L)}{W(L)}
\quad(W(L)>0).
\]

For $W(L)=0$, the stopping mass is one. At $|L|=T$, the algorithm returns the list deterministically; that is the horizon rule, not an application of the sampler kernel. The small-failure guarantee belongs only to histories meeting the amplifier's success threshold. The rest of the coupling then has a single vocabulary. This display is a proposed explanatory bridge, not an additional theorem: it restates the current sampler guarantee in the variables of its immediate use (current lines 2443–2467; P0, Proposition 3.2 and equation (15)).

The coupling must remain history conditioned. Before the dominant vertex has entered the common list, its weight gives the success threshold. An exact successful sample allows both processes to take the same next label; failure can stop the real process. After the dominant vertex has entered the list, subsequent failure cannot erase it. This supports the stopped, stagewise failure charge. It would be incorrect to replace the argument by conditioning globally on no failure or by assuming independent stage failures.

Move the generic measured-label implementation discussion to its existing Appendix G.7 destination, leaving a precise link. Keep §5.1's stronger successful-state calculation where it belongs: it explains the ordinary retained-vector argument. Do not infer physical-state equality from a formal measured-label endpoint. The formal and ordinary routes can support the same bounded algorithm through different intermediate assertions. The specialist inspections of `Samples.amplify`, the abstract factor statement and the finite-list theorem support this scoped distinction; omitted compilation modules were not treated as read (`supporting_reviews/quantum_review.md` and `formal_review.md`).

## 4. Preserve the classical reduction's pending question

**RR10-006 — detailed source alternative at 3242–3268; optional search estimates at 3504–3565; continuation at 3567–3802.**

The classical argument changes probability spaces and query counters. Its main question is precise: how can a decision tree notice the difference between a zero input and the coupled planted one input? The two possible discoveries—the erased zero and the planted cell—must both be bounded. A useful complete route should retain that question until the discrepancy contradiction closes it.

The conditional-value direct product supplies the separate-cap address bound. The hard law and coupling then identify the two exceptional locations. The erased-zero identity and coefficient-four bound are already sufficient for their part of the contradiction. Two full alternatives follow before the planted-cell simulator, so the reader leaves a completed estimate, proves variants, and then reconstructs the unfinished second event. RR9-145 identified this placement; its current optional label and continuation link make skipping possible but leave the full publication-order cost.

Move those alternatives after the generic discrepancy result. At the sufficient estimate, continue directly to the capped predictor. Keep the alternatives fully available, including the search-induction route used by the formal wrapper and the sharper refinement. Each relocated proof needs its own entry assumptions: $m$, dummy input, selected-column identity and the meaning of its query count. Moving a proof without those definitions would trade one burden for another.

The quantitative substitution into Drucker's global-budget theorem is a related, lower-priority relocation. Its present source subsection is legitimate provenance, and the primary reread did not establish it as an independent defect. It can nevertheless move with the alternatives if the author adopts a continuous main-proof route. Credit and the distinction between global budget and separate per-input caps must remain at the direct-product use. The actual conditional-value product, not the title of a source theorem, is what supplies the exact cap-event contract here (CLS-S01 and CLS-S03).

The mathematical reconstruction supports preserving several delicate features. The predictor halts before an offending query, so its cap holds on every branch. It bounds success jointly with compliance under the original law; it does not condition on lightness and then assume a product distribution. Averaging the selected column is distinct from union bounding query time. Those distinctions explain why an extra factor $m$ must not appear in the planted-cell bound. The selected lower-bound route closes with the actual stated constants and floors. Full derivations and their scopes are in `supporting_reviews/classical_review.md` and `independent_mathematical_checks.md`.

**RR10-007 — §6.6, line 3743; PDF page 80.**

The phrase “the stated theorem stands” remains even though the earlier occurrence was narrowed after RR9-067. The source inspection diagnoses a particular displayed inference in Bansal–Sinha v3; that does not by itself refute the theorem. It also does not certify the rest of the original argument. The record has independently proved the prerequisite it actually needs, so it can state that limited conclusion without weakening its own proof.

This is the clearest small factual-scope repair. Apply the same qualification at both occurrences and in Appendix E. If the stronger affirmative statement is intended, it needs an identified alternative argument with matching hypotheses and range. The optional SSW transfer is a distinct source argument, not evidence of an author-approved repair to Bansal–Sinha. See CLS-S02 and CLS-S09; the relevant passages were inspected, not inferred from citation titles.

## 5. Make formal evidence answer the current question first

**RR10-008 — Appendices F–G, lines 6125–6648; optional editorial proposal.**

The current archive explicitly says it is historical, includes a snapshot index and points to the current inventory. That resolves the earlier disclosure complaint. The remaining opportunity is architectural: a complete reader traverses the dated archive beginning on PDF page 119 before the worked current check on page 124 and the central statement inventory on page 129.

One worked check followed by the current inventory would establish the referents for later history. Model and transport explanations can then answer why a particular formal statement has its recorded scope, followed by the execution chronology. Keep receipt-specific bindings and the archive recoverable. This is an optional reorder, not a finding that the current text mislabels historical runs or requires new formalization.

The formal reread inspected actual signatures and selected bodies, not just declaration names. The four configured headline targets, the different explicit-constants theorem, the ordinary threshold and the older formal supplier threshold remain distinct. Accepting-mass transport, measured labels, an abstract retained factor and a physical compiled continuation are different assertions. The printed universal-bound route and imported Lean route also have different constants and dependencies. These distinctions must survive any move; a shorter status table is useful only if it retains them (`supporting_reviews/formal_review.md`).

The historical receipt comparison verified all 69 receipt-listed files present in this packet against their recorded hashes; 155 of the 224 listed files were absent from the selected local subset. That establishes byte agreement for the overlap only. No build or Comparator run was performed. The failed attempt to read the remote pinned record is an access limit, not evidence of a broken public destination.

## 6. Cross-document consequences

### Expert companion

The complete current Markdown and all 166 original XP9 findings and dispositions were inspected. The expert account has a different task: a compact argument with reliable expansion destinations. Do not automatically export the lead's proposed architecture or the removal of its optional proofs into that genre. For example, the compact amplification lemma in the companion has a local role; the long record's placement concern does not revive XP9-058.

The main dependency consequence is that every companion expansion link must still land at a complete entry after the lead is reorganized. A source contract can be deferred within the long record, but a visitor following a specific lemma link needs its hypotheses and proof destination immediately. XP9-155 remains only partially verified: the current pin and anchors are present, but the remote pinned bytes could not be independently read. This is recorded as unresolved verification scope, not a new manuscript defect. The audit classifies 165 concerns resolved and this one bounded issue unresolved.

### Examples-first exposition

The complete current exposition and all 135 original EX9 findings/dispositions were inspected in a later historical audit. The board/checker landing contributes to RR10-003. The exposition-side relocation requested by EX9039 was implemented at line 159; the remaining problem is a new consequence at the receiving lead passage. Two additional results belong in that audit rather than as duplicate lead findings.

First, EX9022 has a small new consequence: the operation recipe now explicitly includes a final Hadamard layer, while the adjacent displayed trajectory stops before it. The author can label the displayed state as the pre-final-layer state, or extend the trajectory through that last operation before the zero-coordinate measurement. This is a stage-labeling mismatch, not evidence that the stated projection probability is false. The existing two-dimensional calculation supplies the check; a fresh unexposed exercise attempt is not claimed.

Second, six old disposition records point at stale or semantically wrong current ranges even though the repairs exist: EX9104, EX9105, EX9118, EX9121, EX9122 and EX9130. The exercise rubrics occur at lines 486 and 500; EX9130's relevant formal-status explanation is at line 494. Repair the evidence locators as evidence locators. Do not manufacture six new manuscript complaints from this bookkeeping error. All EX9 IDs retain their original spelling, without an inserted hyphen.

## 7. Test the proposed edition by the reader's actual task

The next review should attempt a few demanding but finite tasks. Starting at the main entry, reconstruct the total board and its winner without opening the analytic lower-bound proof. Starting at the quantum opening, write the finite control flow and explain both failure outcomes before reading the subroutine derivation. At the sampler/coupling boundary, identify the real transition kernel and both coupled marginals using one set of variables. At the planted reduction, trace the two exceptional events to the final discrepancy without entering an unused quantitative alternative. At the formal entry, identify the current claim, selected proof route and historical evidence before consulting the archive.

These are acceptance checks for the proposed writing, not reported human outcomes. An excellent next edition would make those tasks straightforward while leaving every current derivation available and correctly scoped. More route links alone would not demonstrate that improvement; neither would a smaller page count. The relevant evidence would be a coherent complete route, working independent proof entries, and a new honestly bounded reader pass.
