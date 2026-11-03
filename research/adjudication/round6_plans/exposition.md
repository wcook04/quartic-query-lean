# Round six: revision plan for the exposition

Manuscript `docs/exposition.md` at `9bdd443` (313 lines, 14 PDF pages). Dispositions: `../round6_dispositions/exposition.json` (72 findings, all quotes verified at their stated lines; 45 fix, 19 keep, 5 move to record, 2 decline, 1 already resolved; three findings of my own, AJ-01 to AJ-03).

## Operator direction that governs this plan

Will, 3 November: the papers should look like ordinary papers in the field, following the exemplars. No hashes, commands, receipts, configurations or review-status statements appear in the exposition. Metadata lives in the repository and the record, not in the PDF. "There's always something to improve in every single sentence"; the panels' meta findings are the wrong focus.

So the order of priority is:

1. **The line edit (Part D)**, which is the main deliverable.
2. The panels' teaching findings: the sampler worked row, the three budgets, prerequisites, questions for the reader, the projection experiment versus the decoder, and the example resets.
3. Evidence-presentation findings. These are fixed by removing material from the paper, never by adding status prose.

Reference register: the Buhrman–de Wolf survey (definitions stated once and plainly, credit by name and year, results stated before their proofs) and the SK exemplar `r6packet/exemplars/expository.md`. From the exemplar we take numbered **Question n** paragraphs placed in the text, with answers collected at the end, a one-line AI-assistance note, and plain link text.

## A. Clusters and decisions

| Cluster | Findings | Decision |
|---|---|---|
| C1 Classical cost in the Overview | SX-004, QX-022, CX007 | Fix. The Overview names the two ways to tell the pair apart, says that a cell's position names r hard answers, and says that guessing them succeeds with probability at most (2/3)^r. The cost is "about L queries in a constant fraction of the columns". The phrase "almost every column" (line 26) is wrong and must go. |
| C2 Reader, prerequisites, routes | SX-001, QX-023, SX-002, QX-024, SX-007, SX-008 | Fix. State the operations assumed and point to de Wolf's lecture notes (new bib entry). Swap the "constants" learning outcome for the mechanism. Give one sentence each for the quantum route, the classical route and the companion. Compress the Overview to about 1.45 pages. |
| C3 Experiment versus decoder | SX-009, SX-010 | Fix. Call §1's procedure the *projection experiment*. Add 1111 1000 (Φ=1/2, one-shot success 1/4). In §3, name the decoder as repetitions of that experiment. Optionally add a scope clause for the sign-sensitive test. |
| C4 Parameters and resets | SX-011, SX-012, SX-024, CX009 | Fix. Give r's purpose where r is introduced. Add a one-sentence map from the board to the theorem. Make the Figure 4 reset explicit: the layout and the planted cell are reused, address inputs are drawn from μ, and other cells are blank. |
| C5 Local tests | SX-014, QX-025, CX028, FX016 | Fix. Trace one pointer test and one gate test, and say the circuit is public while its proposed gate values are input bits. Move 5936 to §3 as an instance of the formula for n. Describe the checker as a short script. |
| C6 Sampler worked row | SX-019, QX-011, QX-010, SX-016, SX-020; QX-012 already resolved | Fix, and this is the largest addition. Run one exact stage on the cycled board. Make the measurement explicit, give the self-comparison convention, and write a one-sentence failure ledger. |
| C7 Amplifier numerics | SX-022, QX-020, CX024 | Fix. Keep the contract and send 9/40, 40/31 and the trial recipe to record §5.1. |
| C8 Minimax detour | SX-023, CX022 | Fix. Keep Yao's principle and the property of μ, and replace the parenthesis with a link. |
| C9 Conditioning cues | SX-025–SX-028 | Fix with one clause each. Add one positive history inside the box. |
| C10 Simulator budgets | SX-030, SX-031 | Fix. Set out the three budgets G, the column total L and the per-instance L in one sentence. Announce the XOR toy and zero-based indexing at the link. |
| C11 Exponent step | FX025, AJ-01 | Fix: "Fix 0≤α<4", and state t≥8 for the floor step. |
| C12 Questions | SX-003 (with SX-032) | Fix with four questions and an answers section. |
| C13 Formal section | QX-001, CX004, FX001, SX-033, QX-026, FX014, FX004 fix; QX-007, CX020, FX008, SX-035, FX006 move to record; FX013, FX048 decline; SX-034 keep | §7 becomes one short paragraph (below). The no-review sentence was verified **false**: `round5_statement_fidelity.md` (an AI review dated 3 November, with no Lean run) covers all four theorems and both auxiliary statements. It is deleted, and nothing replaces it. |
| C14 History | SX-005 | Fix with one clause on why AND-OR was there: its small certificates make domain membership cheap to certify. |
| Keeps | 19 rows | The keep list must survive the line edit. It covers the exponent arithmetic, the three inputs with L=0, the domain-bit board, the moved pointer, the cycle, the table and drift identity, the stopping rule, the joint-event AND example, the planted pair, the same-circuit sentence, the quantifier order with t≥2^k, and the definition-meaning sentence. |

No finding was rejected on mathematical grounds. FX025 is the one mathematical correction. I checked it: for α<0 the substitution reverses, for example R=100, Q=4, Q_up=9 and α=−1 give 500<1000. The theorem is unaffected.

## B. Mathematics checked for this plan (scratch `expo/checks.py`, exact arithmetic)

- **Census.** 104/48/104 is correct, and Φ takes only the values 0, ±1/2 and ±1. On 1111 1000, Φ=1/2 and one projection succeeds with probability 1/4.
- **Board counts.** 5936 = 4[4+16+4(6+360)] is the §3 formula for n with m=4, r=2, k=2, S=180, and K=371 is correct.
- **Cycled board, one sampler stage.** After pivot 2 the weights are (1,0,0,1). The joint masses of success and each column are (1/4,0,0,1/4), so success has probability 1/2, which is at least γ=1/8, and the conditional law is (1/2,0,0,1/2). At p=1/2, θ=π/4 and sin²((2j+1)π/4)=1/2 for every j, so amplification changes nothing on this stage.
- **Next stage.** After pivots 2 and 4 the weights are (1,0,0,0) and success has probability 1/4. Then θ=π/6, and one Grover iteration gives success with certainty and returns column 1. After column 1 is listed the total weight is 0, the sampler fails with certainty and stops, and the list is {2,4,1} or {2,1}.
- **Exact decoders on this board.** Every input on the board has projection probability 0 or 1, so the decoders are exact and the comparisons deterministic. Column 2 decodes deterministically as 10 even though it is unpromised.
- **Fractional variant.** 23999/48000, 11999/23999 and 12000/23999 match (1−ε)/(2−ε) with ε=1/12000.
- **Amplifier constant.** The worst per-trial success over p≥γ is about 0.246, which is at least 9/40. The constant is correct; it moves to the record only to save space.
- **Erased-zero changed case.** With two fixed queries per column, the independent hit probability is 1/2, the dependent one is 15/16, and no zero is found with probability 1/16. With one query: 1/4, 175/256 and 81/256.
- **Direct-product positive history.** Under separate caps on uniform AND, after U₁'s first bit the value V₁ is 1 (bit 0) or 1/2 (bit 1) and V₂=3/4. The average 3/8+3/16 = 9/16 equals the starting product.
- **Budgets.** A column total of at most L gives at most L on each instance. Heavy columns number at most G/L. A constant fraction of columns must be heavy because the gap term is G/(mL).
- **Exponent and parameters.** For α=3.5, k=5 and the exponent is 3.6. (2/3)^{40t} ≤ m^{−10}. ⌊x⌋≥x/2 needs L≥1, which first holds at t=8.

## C. Page budget (14 pages; current figures from the students' measurements)

| Part | Now | Target | Grows / shrinks |
|---|---:|---:|---|
| Title + Overview | 1.76 | 1.45 | Shrinks: payoff paragraph −⅓, example map 9→6 rows. Grows: prerequisite sentence and route sentence. |
| §1 | 0.73 | 0.76 | +1/2 example; census sentence shortened |
| §2 | 2.01 | 2.05 | + r purpose, toy map, traced tests, Question 1; − 5936 sentence |
| §3 | 0.75 | 0.77 | + decoder naming, 5936 instance |
| §4 | 3.02 | 3.05 | + worked stage (~9 lines), measurement, self-comparison, failure ledger, Question 2; − amplifier numerics (~5 lines), − ℓ-power bookkeeping in "The count" (keep totals and result, link #upper-explicit-log6, ~3 lines), − 1–2 lines of the related-work paragraph |
| §5 | 2.83 | 2.95 | + budgets, reset, cues, positive history, Question 3; − minimax parenthesis |
| §6 | 0.40 | 0.48 | + α≥0, t≥8, Question 4 |
| §7 | 0.89 | 0.40 | one paragraph |
| Answers to the questions | — | 0.22 | new, unnumbered, before the note |
| Note on preparation | 0.09 | 0.06 | shorter |
| References | 1.53 | 1.57 | + de Wolf notes |
| **Total** | 14.00 | **13.76** | 0.24 page of slack for floats |

If the render exceeds 14 pages or produces a float-only page, cut in this order: the SX-010 clause, the fractional-variant sentence at line 171 (the worked stage supersedes it), one row of the example map, then the related-work paragraph in §4 down to minimum finding, king finding and HMW only.

## D. Line edit, paragraph by paragraph (the main deliverable)

For each paragraph, this section gives its job, then what is weak, then the intended change. "Tics" means the recognisable machine register: the paper announcing its own structure, "not X but Y" contrasts, stacked short declaratives, and intensifiers. Throughout, prefer "we" for steps of the argument, as the survey does. Keep present tense for mathematics. Name an object before its symbol. Put one job in each sentence.

**Title/subtitle.** Fine.

**Overview ¶1 (line 12, the models).**
- Job: define the query models.
- Weak: the oracle formula arrives before the reader knows why a superposition matters. "The query count is a worst case over inputs and over every random choice or measurement outcome" is a sentence appended to fix an omission.
- Change: order the sentences as classical query, randomized and quantum query, then R and Q, and put "worst case over inputs and over every random choice or measurement" inside the definition sentence.

**¶2 (line 14, α_tot).**
- Job: pose the question.
- Weak: "the question is the best power" is clipped. The definition of α_tot is one long sentence with three quantifiers.
- Change: first say "Beals et al. and later work show R ≤ poly(Q) for total functions; how large must the power be?" (cite only what is already in the bibliography; otherwise drop the attribution). Then give α_tot in a display: α_tot = inf{α ≥ 0 : ∃C ∀ total f, R(f) ≤ C(1+Q(f))^α}.

**¶3 (theorem + constants sentence, lines 16–22).**
- Job: state the theorem.
- Weak: "The preprint leaves the constants ... unspecified; the explicit 6 and 1/400 come from the counts in Sections 4 and 6" is a provenance remark sitting on the theorem.
- Change: keep the theorem. Make the remark a short sentence after the display, "The constants 6 and 1/400 are ours; the preprint does not fix them", or fold it into "with explicit constants derived in Sections 4 and 6".

**¶4 (line 24, prior bounds).**
- Job: give credit.
- Fine. Optionally join it to ¶3 with "Together with the upper bound R = O(Q⁴) of ABKRT…".

**¶5 ("Who this is for", line 26).**
- Job: the reader, the outcomes and the route.
- Weak: one 160-word paragraph does four jobs. "The result settles how much…" repeats ¶4. The outcomes are a list of tasks without their purpose. The three payoffs are a long sentence with semicolons. "almost every column" is wrong. The constants are a stated outcome.
- Change: split it into two short paragraphs.
  - (a) Reader and prerequisites (C2): who the reader is, and the operations assumed, with the de Wolf pointer.
  - (b) What they will be able to do, as three verbs: build the function on a four-column board; run the quantum tournament on it; explain why a classical algorithm must pay for an address in a constant fraction of columns. Then give the section route in one sentence.
  - Drop the sentence restating that the result settles the question.

**¶6 ("The reason for four", lines 28–32).**
- Job: give the heuristic.
- Weak: the classical sentence is wrong in tone (C1). "Here L is the classical cost of the partial function k-fold Forrelation" names Forrelation before §1 has introduced it. "The polylogarithmic factors have been dropped from this display" trails at the end.
- Change: put the factor-dropping caveat before the display ("Up to logarithmic factors,"). Rewrite the classical half as the C1 sentence. Introduce Forrelation as "a partial function, k-fold Forrelation, introduced in Section 1, whose classical cost is nearly linear in its about m input bits".

**¶7 (quantifier order, line 34).**
- Job: preview the quantifiers.
- Weak: "so the quantifiers come in a fixed order" is a tic, and the last sentence repeats the first.
- Change: one sentence: "Since 4−2/k < 4 for every k, we prove α_tot ≥ 4 by fixing α < 4, choosing one k > 2/(4−α), and letting m grow; every constant depends on k (Section 6)."

**¶8 ("Where this sits", line 36).**
- Job: history.
- Weak: it reads as a chronological list. "They observed that their method gives…" is a good sentence buried in the middle.
- Change: keep the credit and the order. Make the ABK observation the paragraph's spine: "Aaronson, Ben-David and Kothari … reached 5/2 and observed that any partial function with nearly linear randomized and polylogarithmic quantum cost would give a cube; Tal …; Bansal–Sinha and SSW supplied one."

**¶9 ("The same arithmetic", line 38).**
- Job: explain why the old route stops at three.
- Weak: "as R(g) ≲ n ≈ Q" is compressed. The new-route sentence is long. The reason for AND-OR is missing (SX-005).
- Change: add the clause that AND-OR is there so that domain membership has small certificates, at the price of a quadratic outer cost. Split the new-route sentence into one sentence per factor of Q².

**Example map (lines 40–49).**
- Job: navigation.
- Weak: the "What it shows" cells repeat the payoff sentence.
- Change: six rows: three inputs; four-column board with the changed domain bit; moved pointer; cycled pointers; planted pair; the lower-bound counterexamples (dependent choice, pooled budget, side information, AND). Use terse noun phrases.

**¶10 (record pointer, line 51).**
- Job: reading routes.
- Change: add the two routes and the companion (C2). Keep "The boxed proof in Section 5 can be skipped". Say that the questions have answers at the end.

**§1 ¶1 (line 55).**
- Job: set the size.
- Weak: "This section fixes the partial function at the smallest size" is a tic opening.
- Change: "We first look at the partial function at its smallest size, k=2 and m=4, where every value can be checked by hand."

**§1 ¶2 (line 66, the promise).**
- Job: the promise.
- Fine. Make "undefined otherwise" an explicit "outside the promise", and keep the negative-value remark.

**§1 ¶3 (three inputs, line 72).**
- Job: the calculation.
- Fine. The numerator sentence is dense: list the three products in a short display row.

**§1 ¶4 (line 74, the projection experiment).**
- Job: what Φ measures and the quantum test.
- Weak: four jobs in one paragraph (geometric reading, the circuit, the success probability, the lesson). The lesson sentence "This is the first distinction that must survive the whole argument" is a tic.
- Change: split it.
  - (a) Φ as an alignment.
  - (b) The **projection experiment**, with the 1111 1000 sentence (C3).
  - (c) The lesson in plain words: "The experiment accepts a⁻ with certainty, which is harmless for P but not once P sits inside a total function, where every input needs an answer: an exact certificate must reject a⁻."

**§1 ¶5 (line 76).**
- Job: census and scope.
- Change: the AJ-02 census sentence. Keep the L=0 caveat. Replace the last sentence with "The domain bit of Section 2 repairs this."

**§2 ¶0 (line 80).**
- Delete "This section builds…", or make it the heading's single lead sentence that says why: "A total function must answer on every input; we store, for each column, a certificate addressed by the answers to r instances of P."

**"One column" (lines 82–88).**
- Job: the layout.
- Weak: the sentence "A cell holds r circuit transcripts, explained below" defers. "Every bit is an ordinary input bit, and every assignment of bits is allowed" is a good sentence placed last.
- Change: move "every assignment is allowed (the function is total)" up to sit next to the list.

**Winning definition (line 92).**
- Job: define winning.
- Weak: "At most one pair wins" is followed by two justifications in the wrong order.
- Change: state the definition, then uniqueness as "At most one column can win, since a pointer from one winner would find a zero in the other's all-one string; within a column the promised values fix the address."

**Attribution (line 94).**
- Job: credit.
- Change: add r's purpose (SX-011) as a sentence after "here r = 20 log₂ m". Keep the novelty sentence, but write it as a claim of the combination without the word "new" twice.

**"Four columns" (lines 96–100).**
- Job: the board.
- Weak: the parameters, the decoding convention and the pointer rule are packed together. The toy map is missing (SX-012).
- Change: open with the toy-map sentence. Give the pointer rule as a short list or a sentence with a colon. Keep "a fixed 180-gate circuit described below".

**Line 104.**
- Job: who wins.
- Change: remove the 5936 sentence (it moves to §3). Otherwise fine.

**Transcripts (line 106).**
- Job: certificates of evaluation.
- Weak: four jobs: what C is, the toy circuit, the checker, and the forcing lemma. "everything else below can be checked by hand" interrupts.
- Change: order it as what C outputs, then the forcing lemma (the key fact, with its one-line induction), then the toy circuit with "a short script checks every count on this board (record §4.4)". End with the domain/value consequence.

**"The domain bit is needed" (line 108).**
- Job: the counterexample.
- Change: place Question 1 directly after this paragraph. Otherwise keep it verbatim in content and tighten "Change the board:" into "Change the board as follows."

**Local tests (lines 110–114).**
- Job: the test family and its cost.
- Weak: the counts come before any test is shown. The last sentence "So a winner is unique and certified … and the domain tests are essential" restates.
- Change: list the four kinds of test, then trace one pointer test and one gate test on Figure 2 (C5), then give K and the board value 371, then the outcomes at (1,10), at column 1's other addresses and at (2,00). Drop the restating sentence.

**§3 ¶1 (line 118).**
- "This section states the three facts…" is a tic. Change to "Three facts about k-fold Forrelation are used below."
- Merge the parameter setup and the definition so that H, u and D_z are defined in one sentence before the display.

**Decoder (line 124).**
- Change: begin "Repeating the projection experiment of Section 1, …". Keep ρ and the Chernoff bound. "the cap holds on every input" becomes "the number of queries is the same on every input".

**Circuit (line 126).**
- Job: an exact circuit.
- Fine. The p₁/p₀ comparison sentence can lose its brackets with "p₁ is the bit [·]".

**Hardness (line 132).**
- Job: imported theorem and credit.
- Fine. Make "The record gives a separate derivation…" a parenthesis.

**Line 134 (input size).**
- Change: add the board instance: "for the board of Section 2 (r=2) this is 5936". Delete "The parameter m counts columns", since it is stated in §2.

**§4 ¶1 (line 138).**
- Job: why direct search fails.
- Good. Slightly reorder so that the obstacle comes first and the plan last. Keep the R ≈ Q^{2−1/k} remark.

**Comparing two columns (line 140).**
- Fine. Add the self-comparison convention here ("a column compared with itself loses, without a query; a_ii = 0").

**Reversible comparison (line 142).**
- Job: unitarity.
- Weak: one long sentence with "and since".
- Change: two sentences. The first says the comparison is a unitary whose inverse costs the same. The second says each outcome has probability equal to the classical rule averaged over decoded labels, because distinct labels sit in orthogonal registers.

**Outward pointers (line 144).**
- Keep. "Nothing is claimed about comparisons between two losers" is good.

**Moved pointer (line 146).**
- Keep. The final sentence "A column that dominates … logically necessary" can drop "logically".

**Cycle (line 148).**
- Keep. Its middle sentence about label independence is long; split it at "this matters for column 2".

**Related work (line 152).**
- Job: place the search.
- Weak: a list of four citations with relative clauses.
- Change: lead with the obstacle: "Standard quantum search assumes either a total order (minimum finding [DH]) or a fixed predicate computed with bounded error [HMW]; here a loser pair may compare with probability exactly 1/2." Then mention king finding and the comparison-based separations in one clause.

**Ideal process (line 154) and table.**
- Keep. "Once |w|=0 the process is absorbed" is fine. Put "On the cycled board, pivot 1…" before the table as an explicit lead-in sentence.

**Drift (lines 163–171).**
- Job: the halving argument.
- Weak: line 171 is a 120-word paragraph doing parameters, the Markov step, the cycled-board remark and the fractional variant.
- Change: split it.
  - (a) Choice of T and ε, and why the winner keeps weight above 1/2.
  - (b) The Markov conclusion.
  - (c) The fractional variant with both numbers (QX-011), or drop it in favour of the worked stage.

**Sampling a pivot quantumly (lines 173–177).**
- Job: the realised law.
- Weak: "The algorithm realises the ideal pivot law without knowing the weights" is good. The next three sentences narrate the procedure in an unclear order.
- Change: preparation, then success flag, then why the masses multiply (fresh registers, fixed i), then why they add (orthogonal i), then the display. Then insert the **worked stage** (C6) as its own paragraph headed "One stage on the cycled board". Then Question 2.

**Stopping (line 179).**
- Job: the stage rule and its failure.
- Weak: three ideas in one paragraph (amplify, stop rule, coupling).
- Change: put the measurement sentence (QX-010) first after amplification. The stop rule follows. "After the winner is listed nothing is claimed" stays, with its reason. The coupling sentence ends the paragraph.

**Amplification (line 181).**
- Change: reduce it to the contract (C7) in about 4 sentences. Keep "conditioning on success keeps the law of the marked label" and the zero-success clause. The final sentence "The cap does not depend on knowing p, which matters…" stays.

**Verification (line 183).**
- Change: the failure ledger (SX-020) replaces "Adding up". Keep the recall of the changed domain-bit board.

**The count (lines 185–189).**
- Job: the query total.
- Weak: the ℓ-power accounting reads like a ledger. "The exponent six is an artefact of this deliberately loose count" is fine.
- Change: keep the two totals and √m(log m)^{O_k(1)}. Compress the ℓ-power justification to one sentence plus the record link. Keep the controlled-query and pointer remark only if space allows. End with "This is the √m half of the Overview's heuristic."

**§5 ¶1 (line 193).**
- Change: "This section proves…" becomes "We now show R(F_{k,m}) > ⌊mL/100⌋." State Yao's principle and the property of μ, and give the link in place of the parenthesis (C8).

**The pair (line 195).**
- Job: the two inputs.
- Change: add the reset sentence (C4) after the Figure 4 reference. Revise the caption to match it.

**First difference (lines 199–204).**
- Change: add the overcount half-sentence. The sentence "The run on Y⁰ does not depend on I, which is chosen independently" should move before the display, because the display relies on it.

**Erased zero (lines 206–210).**
- Change: add the transcript-conditioning clause (SX-026). "For the inequality," becomes "To bound E Z,".

**Independence example (line 212).**
- Keep. Its last sentence, "A uniform marginal is a weaker condition than independence…", is good. Put Question 3 after this paragraph.

**True cell (line 214).**
- Weak: "and that is what must be unlikely" is a tic.
- Change: "a query in the true cell reveals, by its position, the r hard answers s_I." Keep heavy and light. The sentence "The tool is a direct-product theorem with a separate cap on each instance" leads into the next paragraph; keep it.

**Direct product statement (line 216).**
- Keep. Italic statement.

**Hypotheses needed (line 218).**
- Change: name the input law in each example (SX-027). Keep the credit sentences.

**Box (lines 220–228).**
- Change: insert the positive-history sentence (SX-028) after the product-posterior sentence. Keep everything else. The final "Every distribution in this argument is finite…" may lose "Section 7 says what Lean proves".

**Why the event must be joint (line 230).**
- Keep. Name the law ("uniform on the three promised inputs 01, 10, 11"), which is already done. Cut "With two instances the cap event can also make initially independent samples dependent" to the link only, if space is needed.

**Simulator (lines 232–239).**
- Job: the reduction.
- Weak: one long paragraph, with the budget implication missing.
- Change: split it.
  - (a) What the simulator is given and does.
  - (b) The three budgets: "The run as a whole makes at most G queries; the simulator stops after L queries to column i's address inputs in total, hence at most L to each instance, which is what the direct product requires (it would even allow rL)."
  - (c) The joint event and its display.
  - (d) Summing over j and averaging over I.
  - Add the XOR announcement at the record link (SX-031).

**Finishing (lines 241–245).**
- Fine. Shorten "Fixing its coins gives deterministic algorithms whose gaps average to at least 1/3, while each gap is below 1/3, a contradiction" to one clause.

**§6 ¶1 (line 249).**
- Change: "This section combines…" becomes "Combining the two bounds:". Add t≥8 (AJ-01).

**α step (line 253).**
- Change: "Fix 0 ≤ α < 4". Keep the rest.

**k=3 remark (line 257).**
- Keep.

**Order matters (line 259).**
- Keep, and remove "The order matters." as an opener ("All constants … depend on k, so one cannot substitute…"). Put Question 4 here.

**Upper bound (line 261).**
- Keep. Drop "with the explicit constant 35⁴" unless the record link needs it (it is fine as link text).

**§7 (new single paragraph, about 10 lines).** "The theorem has also been proved in the Lean proof assistant. One [statement file] in the [public repository] contains, using only Mathlib, every definition the statement uses: [R], as the least depth of a finite random mixture of [decision trees] right with probability 2/3 on every promised input; [Q], as the least [query cap] of a [quantum program] reaching the input only through the [bit oracle]; [the function F_{k,m}] with its [winning condition]; and [α_tot]. It states [four theorems]: α_tot = 4, the family bounds (with the power of the logarithm left as an unspecified exponent), the failure of every bound R ≤ CQ³, and the Forrelation lower bound of Section 3. The proofs are in [a separate file]; an independent checker confirms that they establish exactly these statements. What a reader can usefully check is whether the definitions say what is intended, and the [winning condition] is a good place to start: its second clause requires every address input to be promised, which is the clause the changed board of Section 2 fails. The record explains [why these definitions agree with the usual query models]."

The bracketed items are the existing link labels.
- Drop `def-RLe`, `def-QLe`, `def-randomized`, `def-universal`, `thm-alpha`, `thm-headline`, `thm-cubic`, `thm-forrelation`, `statement-config`, `statement-receipt`, `src-constants`, `cmp-*`, `amplifier-*`, `direct-product-config`, `src-amplify-measured` and `def-compliant` unless one is used.
- Keep `statement-file`, `statement-solution`, `def-R`, `def-Q`, `def-tree`, `def-querycap`, `def-adaptive`, `def-oracle`, `def-F`, `def-wins`, `def-alpha` and `thm-all`, plus a record link to §2.2.
- Remove the 343-line count, "deliberate placeholders", "built but not compared", "Each link opens the exact lines", the trust conclusion sentence, the Forrelation-proof-not-reviewed sentence, the auxiliary-results paragraph and the no-review sentence.
- Never claim any review.

**Answers to the questions (new, unnumbered, before the note).** Four short paragraphs, each linking back to its question.

**Note on preparation.** "The separation theorem and the construction are OpenAI's [@OpenAI2026]; Section 2 credits their ingredients. This exposition was prepared with the assistance of AI systems, under the author's direction." No review-status clause.

## E. Questions to insert (answers verified in Part B)

1. **(§2, after the domain-bit board.)** "On the changed board, which of column 2's tests fail at each of its four addresses?"
   - Answer: the own-string and pointer tests pass at every address, and so do the gate tests. The tests that fail are:
     - at 00: the first domain test;
     - at 01: the first domain test and the second value test;
     - at 10: the first domain test and the first value test;
     - at 11: the first domain test and both value tests.
   - Executor: reconfirm against the record §4.4 second-board output before printing.
2. **(§4, after the worked stage.)** "Suppose the measured pivot is column 4. What are the new weights, the success probability of one preparation, and the next pivot? What does one Grover iteration do here?"
   - Answer: (1,0,0,0); 1/4; column 1 with conditional probability 1. With θ=π/6, one iteration succeeds with certainty. The next stage then has total weight 0, so the sampler fails with certainty and stops. Verification accepts column 1 and rejects columns 2 and 4 by their own-string tests.
3. **(§5, after the independence example.)** "Query two fixed positions in each of the four columns. How often is an independent I hit, and how often an I chosen among columns where a zero was found (uniformly among all four if none)?"
   - Answer: 1/2 and 15/16; no zero is found with probability 1/16.
4. **(§6.)** "To show α_tot ≥ 3.5, which k does the argument use, and what exponent does it give?"
   - Answer: k > 2/(4−3.5) = 4, so k=5, giving 4−2/5 = 3.6 > 3.5.

## F. Ordered edit list

1. Overview: ¶1–¶10 per Part D. Line 26 is split into two paragraphs. Edit line 32 (C1), line 38 (SX-005) and the map table at lines 40–49 (six rows). Line 51 gets the routes.
2. §1: lines 55, 74 (split, plus the experiment naming and the 1/2 example) and 76 (census, scope).
3. §2: lines 80, 88, 92, 94 (r purpose), 96 (toy map), 104 (remove 5936), 106 (reorder; script), and 108, followed by Question 1. Lines 110–114 get the traced tests.
4. §3: lines 118, 124 (decoder naming) and 134 (5936 instance).
5. §4: lines 140 (self-comparison), 142, 152, 154 and 171 (split; QX-011). After 177, insert the worked stage and Question 2. Then lines 179 (measurement), 181 (contract only), 183 (ledger) and 185–189 (compress).
6. §5: lines 193 (minimax link), 195, 197 (reset; caption), 199–204, 210, 212 followed by Question 3, 214, 218 (laws) and 221 (positive history). Lines 232–239 are split (budgets, XOR note).
7. §6: lines 249 (t≥8), 253 (0≤α) and 259, followed by Question 4.
8. §7: replace lines 265–269 with the single paragraph. Prune the `<!-- lean-links -->` block **through `tools/build_lean_links.py`**, never by hand, if that tool owns the block. Otherwise leave unused definitions, since pandoc ignores them, but check that the renderer does not warn.
9. Add "Answers to the questions".
10. Rewrite the Note on preparation.
11. exposition.bib: add de Wolf, *Quantum Computing: Lecture Notes*, arXiv:1907.09415 (cite chapter 7 "Grover's search algorithm" and the probability appendix).
12. Figure 4 caption (fig4 itself unchanged: it already labels A_{i,h}∼μ). No other figure changes.
13. Render with `tools/render_papers.py --paper exposition`. Inspect every page at reading size, check that it is 14 pages or fewer with no float-only page, and apply the Part C cut order if needed.

## G. Coordination

- **Expert companion owner.**
  - Use one consistent classical heuristic, "about L queries in a constant fraction of the columns, or a lucky r-bit guess"; companion §1.2 already says this.
  - Use the same AND-OR scope clause (their CX015).
  - Confirm that the section names I cite in the route sentence (§1.1 history, §3 shortcut table) are stable.
  - Under the same operator direction, their Appendix A review-status and commit sentences (SX-040/041, FX002, QX-006, CX014) presumably also leave the PDF. Both papers should drop review-status prose together, so that neither cites the other's.
- **Record owner.**
  - §2.9 rows still describe outdated review status (CX004, QX-008, FX027). This is metadata in their scope.
  - The §6.5 XOR trace could add a one-line crosswalk to the exposition's one-based board (SX-031).
  - The "required" hardness route (SX-042) is theirs.
  - Link targets I rely on are #upper-cyclic-example, #upper-amplification-proof, #upper-explicit-log6, #CL-minimax, #CL-simulator, #AC-example-tests, #forr_small_instance and a §2.2 bridge anchor (#R3-01-BRIDGES or the §2.2 heading; the executor picks it).
- **Link tool.** Record links are pinned by `tools/build_lean_links.py`; any new record anchor must exist at the pinned commit, or the tool will fail.

## H. Lean wording that needs a fidelity recheck after the edit

Only the new §7 paragraph:

- the descriptions of R, Q, F and α_tot (matching `RLe`/`R`, `QLe`/`Q`, which also has the constant-on-promise branch, `Fkm`/`WinsAt` and `alphaTot`/`UniversalPower`, which includes 0 ≤ α);
- "the power of the logarithm left as an unspecified exponent" (`theorem_one_one`, existential b; it also carries an existential circuit and the floor-form lower bound, so state "for some exact circuit realising P" if the sentence names the circuit);
- "the Forrelation lower bound of Section 3" (`BansalSinhaLower`: L < R(P) for each fixed k ≥ 2 beyond some t₀, which matches §3's "for fixed k and all large m");
- "its second clause requires every address input to be promised", which is the second conjunct of `WinsAt` at Challenge.lean L262–272: `f (readA x i h) = some (s h)`;
- "an independent checker confirms that they establish exactly these statements", which must not overstate. It is the Comparator acceptance of the statement file. Keep or drop it, but do not add axioms or trust taxonomy.

§6's "0 ≤ α" now matches `UniversalPower`.

## I. Execution notes (3 November, after go-ahead)

The plan was executed in `docs/exposition.md` and `docs/exposition.bib`; the figure sources are unchanged. These are the departures from the plan:

- **Example map table removed** rather than shrunk. Register rule 20 and Will's direction to read like the literature both point this way. A roadmap paragraph now carries the examples.
- **Answers section** follows the exemplar: Questions 1–4 sit in the text and link to "Answers to the questions" at the end. "Use of AI tools" replaces the "Note on preparation". It makes no review claim.
- **Sign-sensitive test sentence (SX-010) dropped** to fit the page budget. The scoped §1 sentence stays.
- **Fractional cycled-board variant (QX-011) dropped.** The exact stage on the actual board supersedes it, and the numbers live at record #upper-cyclic-example.
- **SSW rorrelation sentence in §3 dropped.** SSW keeps its credit in the introduction. The §3 pointer to the record's separate hardness derivation was also dropped.
- **Record cross-references** fell from 21 to 10, under rule 21.
- **Figure widths.** fig1 is now 82% (was 94%), fig2 82% (was 92%), fig3 36% (was 42%) and fig4 62% (was 76%), to hold 14 pages. Each was checked legible at 100 dpi.
- **Page count:** 14. References run from page 13 to page 14, with no float-only page.

No mathematical statement changed, apart from adding the hypothesis α ≥ 0 at the §6 step (FX025) and the explicit t ≥ 8 for the floor step (AJ-01). In §7 the Lean statement is described more briefly. It still records the existential circuit, the floor form of the lower bound and the unspecified power of the logarithm.

**Register comparison** (IQR units, expository profile, before → after):

| Feature | Before | After |
|---|---:|---:|
| status vocabulary | +12.6 | +5.5 |
| meta-narration | +1.8 | −0.7 |
| negation | +1.1 | +0.4 |
| Let/Suppose openers | −1.2 | −0.1 |
| "we" | −2.0 | −1.5 |
| triads | +1.5 | +2.2 |

Against profile_v2, status fell from +11.8 to +5.0 and negation from +2.5 to +1.3. Residual status hits come from mathematical uses of "verification" (the algorithm's final stage) and from §7's "Lean". The triad increase comes from lists of named authors and of prerequisites, which are intended.

**Checks.**

- `make check` passes: 226 tests OK, 2 skipped.
- `python3 tools/build_lean_links.py --check` passes. The exposition's link block now holds exactly the 13 labels it uses. The block was edited by hand from the generator's own definitions, and no tool or registry changed.
- `tools/render_papers.py --paper exposition` renders 14 pages.

**Follow-up pass (coordinator, 3 Nov).**

- **Figures** are back at their original widths: 94/92/42/76%. All four were checked at 110 dpi. The document is now 15 pages, which the coordinator accepted.
- **de Wolf citation** was checked against arXiv, where 1907.09415 runs v1 (19 Jul 2019) to v6 (27 Aug 2026). The bib entry now cites v6, 27 August 2026. The packet copy has the August 2026 changelog, and its chapter 7 covers Grover, amplitude amplification and the case where only a lower bound on the success probability is known. §7.4 of that chapter runs a reversible circuit backwards to clean up workspace. Appendix B gives the union bound, Markov and Chernoff, but neither Yao's principle nor decision trees.
- **Prerequisite sentence** now cites:
  - §3 of the Buhrman–de Wolf survey for the query models (new bib entry, TCS 288(1):21–43, 2002);
  - de Wolf's lecture notes, chapter 7, for amplitude amplification and uncomputation, and Appendix B for Markov and Chernoff;
  - Yao 1977 for minimax.
  Conditioning along decision-tree branches is left uncited, as elementary.
- **Introduction** now defines $r$ before it is used.
- **Citations** where the author is named in the sentence now use the year-only form. The theorem heading no longer prints "OpenAI" twice.
- **Cold-read fixes:**
  - §2 local tests now open with a lecture-style lead-in.
  - §3 now opens with "The construction uses k-fold Forrelation through three facts, which we now state."
  - The person is consistent in "Comparing two columns".
  - The end of §1 links again to the domain bit.
  - §5 states the Figure 4 reset in full.
  - §7 is split into two paragraphs: what the file states, and what to check.
  - "The count" opens with "Let us total the queries."
- **Checks:**
  - `check_repository`, `build_challenges`, `build_corpus` and `build_comparator_map` all pass.
  - The exposition's own link block passes `updated_paper` (the function behind `build_lean_links --check`).
  - `make check` and `build_lean_links --check` currently fail. The cause is `docs/expert_companion.md`, which uses record anchors `CL-direct-product-formal` and `ROOT-GROWING-K` that are absent at the pinned commit `e9dfefb`. That file belongs to the companion agent.
  - The unit tests show the same single error, in `test_papers_carry_current_link_blocks`; the other tests pass.
