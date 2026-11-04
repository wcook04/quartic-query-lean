# Review of the round-ten exposition

**Lead:** `repository/docs/exposition.md`, SHA-256 `e034aae7c7a74529656a84289b41767bcc4f06cbe1a3d2926fc8a01f918918b8`. All line numbers refer to this supplied edition. The PDF inspected has 24 pages. This report gives revision advice; it does not replace or edit the manuscript.

## Editorial decision

The most useful next revision is a reorganization of the teaching route, followed by a small number of local clarifications. Another round that only appends explanations to individual objections would increase the reader's workload. The current text supplies the central mathematical mechanisms, including the conditional sampler law, the permanent list, the whole-run light event and the stopped predictor. The mathematical audit found no error in those mechanisms within its declared scope. The next task is to make their relationship easier to reconstruct, while retaining the exact contracts on which they depend. See [the mathematical verification](checks/mathematical_verification.md) for the checks and their limits.

Three revisions would produce the greatest improvement. First, let the reader execute the construction before managing its full scale hierarchy. Second, make the quantum section progress from a comparison property to an ideal process, then to the implementation of that process. Third, make the classical proof culminate in a task that assembles its three charges into the product scale $mL$. These are EX10-001, EX10-005 and EX10-008. The other findings support those changes or remove smaller avoidable costs. The complete, source-ordered findings are in [feedback.json](feedback.json); impact order is separate from encounter order.

This is an editorial assessment using simulated backgrounds. The first-pass files preserve both actual observations and the departures from the requested strict chronology. In particular, source chunks were visible before their individual rows were written, line 223 was retrieved after a skipped range, and the combined rubric was partly exposed in a tool batch. The later perspectives share context and know the answers. These limits prevent any claim of independent blind readers or measured learning, but do not prevent checking a mathematical implication, a quotation, an exercise calculation or a proposed dependency order.

## 1. Let the example carry the scale hierarchy

The first OR example establishes what is charged. The next reader task should be understanding what sort of total problem could permit a greater advantage. Instead, the introduction asks the reader to manage a uniform infimum, the order of choosing $\alpha$ and $k$, the parameters $m,C_k$, powers of logarithms, a conservative coefficient, a reconstruction-versus-source distinction, construction history and two optional routes. Section 2 then supplies another general parameter block and a stopped-simulator preview before the four-column board. The first completely specified winning board appears on PDF page 6. This ordering is the evidence for EX10-001; it is not a claim that the definitions or scope notices are absent. [Exposition, lines 22–51 and 106–145, PDF pp.1–6.]

A more economical architecture can preserve the same theorem and give the exact notation a purpose when it arrives:

| Current material | Proposed job and position | Dependency that must survive |
| --- | --- | --- |
| Query model, OR benchmark, total versus promised functions | Opening frame | Per-input error, all-branch query cap, and no runtime claim |
| Exact infimum and explicit family inequalities | One named theorem at the end of Section 3, before Section 4 uses the bounds, with a short opening pointer | Uniformity over all functions; fixed $k$; the same $F_{k,m}$ in both bounds |
| Three eight-bit inputs | First operational example | Signed amplitude, squared probability, and the off-promise negative case |
| General column before the base board | Introduce the concrete fields and four winning tests on the base board; then state their general form | Stored data may be false; domain and value outputs are different obligations |
| The line-129 stopped-simulator estimate | Explain the choice of $r$ when the classical true-cell event has been defined | The bound is on a joint event and applies to adaptive proposals |
| Final fixed $k$ quotient | Main concluding argument | Choose $\alpha$, then $k$, then grow $m$; do not insert growing $k$ into fixed $k$ constants |

This is a redistribution of existing material, not a request for another overview. The informal opening should still say what the result asserts and who proved it. It should not leave a reader unsure whether four is a lower threshold or a universal upper limit. The exact theorem must remain easy to locate and must still state the same conclusion. The source preprint's Theorem 1.1 and the companion's introduction provide the statement boundary; they do not prescribe the novice's instructional order. [Supplied preprint, pp.1–2; companion, lines 12–34.]

The title's promise can then be fulfilled twice: an early explanation identifies the two relevant scales, and the final section proves how their quotient excludes every smaller uniform power. It is unnecessary for the learner to carry the exact $1/400$ coefficient through the whole first encounter. Conversely, the final order of quantifiers cannot be made optional: it is what turns the family estimates into the claimed optimal exponent. The recommended relocation preserves that distinction.

## 2. Separate the mathematical example from its implementation record

The transcript example teaches a precise operation. A gate check reads a proposed output and its predecessors; it does not recursively recompute those predecessors. If every local equation passes in an acyclic circuit, induction forces the entire proposed computation to be correct. The domain and value outputs then certify the additional facts a winning cell needs. The changed pair $t_1=t_2=0$ makes the distinction executable: the later OR equation can pass while an earlier NOT equation fails. [Exposition, lines 145–157.]

The exact 180-gate realization and $K=371$ are a different kind of information. They establish what a particular small circuit and its test list contain. Their source gate numbering is useful when checking the artifact, but it is not needed to understand why a false transcript cannot make every test pass. EX10-003 proposes gathering those artifact-specific details in the already optional circuit-check note, leaving the connected-gate example and the symbolic count

$$
K=m+(m-1)+rS+2r.
$$

on the main route. The general near-linear circuit-size estimate still matters and must remain available before its use in the verifier's query cost. No recommendation here replaces the circuit defining $F$ with an unrelated toy circuit.

The same distinction applies later to the XOR simulator. The statement at line 402 translates the record's zero-based column 1 to the exposition's column 2. That warning is accurate, but it makes the learner perform a conversion at the moment when two different clocks are being distinguished. The local example can use its existing target symbol $i$; the exact record label belongs in the evidence note. The table, Question 4 and its answer must be relabelled together if this change is made. This is EX10-009, and it is a narrower action than changing every index convention in the paper.

The first phase-query trajectory needs one smaller clarification. Its framing sentence lists a final $H$, but the arrows stop at $u$ just before that operation. Line 98 explains how final $H$ and outcome $00$ implement the projection test. EX10-002 asks only for a visible stage label or a final labelled arrow. The signed overlap, its square and the two-query count have been checked and should not be treated as erroneous.

## 3. Rebuild the quantum section around the distribution it must implement

The construction-specific problem is not simply to apply quantum search. Checking a column already costs about $\sqrt m$, up to logarithms; placing that check inside another search over columns loses the intended exponent. The cheap operation is instead a comparison that reliably favors a real winner but may be arbitrary between losers. The section needs to make the reader understand what follows from that unusual contract before explaining how to run it coherently. [Exposition, lines 208–235.]

At present, reversible flag computation appears at lines 217–223, before the paragraph proving the winner guarantee. The text then returns to the physical board, false dominance, cycles and ideal weights, before resuming quantum registers at line 259. EX10-005 proposes one continuous progression:

1. Give the comparison rule and prove its one-sided guarantee against a true winner.
2. Use the false-pointer and cycle examples to show why neither final verification nor the arbitrary-probability model can be discarded.
3. Define the ideal weights, derive expected halving and explain why a missing winner retains mass.
4. State the sampling contract: the exact conditional law, an all-input cap, and failure control above a specified success threshold.
5. Realize that contract with fresh comparison registers, the joint mass $w_i/m$, and the amplification invariant.
6. Transfer the ideal argument to the capped process, then verify its retained list.

This order moves existing material; it does not replace a proof by an analogy. In particular, a recommendation to shorten the quantum prerequisites must not erase the full workspace. The good vector in the amplification proof includes the column and all retained trial data. The inverse must undo the whole preparation. A clean column-only state is neither established nor needed. Childs's retained-information explanation and BHMT's good/bad decomposition are useful comparisons for these local operations, while BHMT's expected-cost unknown-success algorithm is not the capped guarantee used here. The passage-specific comparisons and editions are recorded in [literature_comparison.md](literature_comparison.md).

The fractional example already provides the missing distinction that a zero-one cycle alone could not teach. After pivot 2 it gives weights $(1,0,2/3,1/4)$, joint masses $(1/4,0,1/6,1/16)$ and conditional law $(12,0,8,3)/23$. The first-pass concern about absent fractional weights was therefore withdrawn. There is no current finding asking for another such example. The next revision should use the existing example as the concrete target of the sampler contract. [Exposition, lines 271–279; later annotation of U0347.]

The exact schedule constants at line 301 serve an assurance task. They specify an implementable routine and prove that its cap is valid even when success is very small. The main learning path, however, uses the contract and the fact that each successful trial has the same normalized good state. Put the detailed choice of $M,N$ and the $9/40$ averaged estimate in a marked derivation whose location is explicit. Keep the zero/one endpoints, below-threshold cap and first-success mixing argument accessible. Removing those guarantees would damage the proof; moving their numerical derivation would not.

### Make the error and query units easy to compare

EX10-007 proposes replacing part of the dense accounting prose with a compact event ledger. The existing common-unit cost sum already resolves the previous conversion concern; any accompanying cost table should replace the relevant prose, not duplicate that repair. The event ledger distinguishes events that currently share the symbol $\varepsilon$:

| Event | Situation in which it matters | Charge |
| --- | --- | --- |
| Ideal list still lacks the winner | $F=1$ | $2m/2^T$ |
| Real sampler stops before the winner is listed | $F=1$, conditional on a common pre-winner history | $T\varepsilon$ |
| Fresh decoding of the listed winner is wrong | $F=1$ | $\varepsilon$ |
| Some listed nonwinner's violation is missed | $F=0$ | $T\varepsilon$ |

Comparison decoding is already included in the actual $a_{ij}$; it is not another row to add to the final error. The two Boolean cases are alternatives. These are the manuscript's existing claims, not new estimates. [Exposition, lines 323–325; mathematical verification §3.]

An optional cost table can distinguish a bit query, one comparison, one preparation, one stage and the complete tournament. Letting $C_{\rm cmp}$ denote the displayed bit-query cost of a comparison only within this proposed ledger, a stage with $j$ previous pivots uses at most $j$ comparisons per preparation. The entire tournament therefore has the $T^2$ factor in the manuscript. Verification then adds a separate short-list cost; it is not nested inside every search operation. This table should replace repeated verbal counting, not be appended beside all of it. The final exact bound and its deliberately loose logarithmic simplification remain available.

## 4. Make the classical proof teach the product scale

The lower bound has two changed regions, but three charges. That distinction should organize the proof's presentation. The first-difference argument identifies the erased zero and the filled true cell. The cell event then splits according to the target column's whole-run address budget. The resulting map is:

| Event charged on the dummy run | Why it is bounded | Bound |
| --- | --- | --- |
| The zero erased in the independently selected column is found | The run finds $Z$ zeros; the selected column is independent, so its chance is $Z/m$; early/late counting controls $\mathbb E Z$ | $4G/m^2$ |
| The selected column is heavy | More than $L$ address queries can be spent in at most $G/L$ columns | $G/(mL)$ |
| A light selected column's true cell is visited | A fixed-time proposed coordinate supplies a capped prediction of the whole address; union over times and average over the selected column | $G(2/3)^r$ |

The table is a proposed map of the existing proof, with all three arguments still supplied in the text. These are overlapping upper bounds, not a partition: an erased-zero hit may coexist with a cell visit, and the heavy-column bound also charges some runs with no cell visit. It should appear after the paired inputs and first-difference event are understood, rather than importing unknown terms into the introduction. It should also be the map used at the final calculation. [Exposition, lines 352–426 and 455–464.]

The quantitative payoff is now visible without claiming matching classical complexity. For a budget $G\le c\,mL$, the three terms are at most

$$
4c\,L/m,\qquad c,\qquad c\,mL\,m^{-10}.
$$

Using $L\le m$, these sum to at most $4c+c+c/m^8$. The paper chooses $c=1/100$, leaving a comfortable gap below $1/3$. The address-input hardness contributes $L$; hiding the selected column contributes $m$. The erased-zero term remains controlled because its search scale is no smaller than the chosen budget. This is the operation EX10-008 asks a learner to reconstruct.

There is no current mathematical criticism of the joint-event argument. The first pass recorded concern as soon as whole-run lightness appeared. Lines 385–400 then supplied both a counterexample to conditional success and a simulator that stops before an over-budget hidden query. The relevant containment is one-way: a light true-cell visit makes the simulator correct, while a lucky default can make it correct without any visit. Giving the simulator all outside data is valid because those data are jointly independent of its hidden tuple. The mathematical check confirmed these claims and the absence of an extra factor $m$ after averaging over the planted index. [Mathematical verification §4; exposition lines 383–434.]

Drucker's conditional-value proof is a useful source comparison here because it gives the quantity a computational interpretation before multiplying it. The exposition's separate-cap statement is not identical to that paper's global-budget headline theorem. A redesign must preserve the exact cap and independence contract, even if the proof of that contract remains optional. The theorem needed after the optional box must never be hidden inside the box.

## 5. Give the recurring examples stable identities

The paper uses several intentionally different examples. Their differences are mathematically useful; they should not be collapsed into one allegedly universal small instance. A compact reference table can make return navigation cheaper:

| Object | What changes or is fixed | What the reader can test |
| --- | --- | --- |
| Base board | The strings, true transcripts and addressed pointers of Figure 2 | All four winning conditions; exactly one winner |
| Domain-bit board | The all-one candidate moves to off-promise column 2, with matching pointer changes | Why checking value outputs alone is insufficient |
| False-pointer board | One pointer in column 1's true cell is changed | Comparison dominance does not certify a winner |
| Cycled board | Three loser-to-loser pointers are changed from the base board | Cycles, weight updates and a retained winning list |
| Fractional matrix | An abstract complementary probability matrix, not another board realization | Unequal weights, joint masses and conditional probabilities |
| Planted pair | Independent sampled address inputs, random zeros, one erased zero and one filled cell | First-difference coupling and the hidden selected column |
| XOR trace | A separate total two-bit XOR function and a hidden-tuple query cap of one | Two clocks, stop-before-read and whole-run lightness |

EX10-006 asks for the name “cycled board” at the later sampler and Question 2 uses. This is not a request to insert a new disclaimer at every line. The present figure captions and resets have been inspected, and their mathematics was checked independently. The useful change is to make a returning reader retrieve the intended state without reconstructing the entire history of mutations.

## 6. Make exercises test the promised reconstruction

The projection check and Questions 1–5 were attempted before their answers. Their saved results agree with the supplied answers. That fact supports the arithmetic and statement checks; it does not establish that the declared audience will learn the mechanisms unaided.

| Task | Operation actually tested | Remaining teaching use |
| --- | --- | --- |
| Projection check | Signed amplitude versus its squared probability | Keep the measurement stage visibly aligned with the operation |
| Question 1 | Domain/value failures across four addresses | Pair with a brief explanation of why a gate-consistent transcript can still fail output tests |
| Question 2 | Sequential weight updates, normalization and overshoot | Make the active physical and abstract examples explicit |
| Question 3 | Independence of planting versus a uniform marginal | Keep its adaptive identity distinct from the fixed-pattern product |
| Question 4 | Two clocks and whole-run rather than visit-time lightness | Preserve the altered future query that changes the joint event |
| Question 5 | A limiting threshold versus exclusion of its endpoint | Keep the fixed $k$ choice and the positive exponent calculation |
| Combined task | Reconstructing the two mechanisms and their logical role | Add or retarget a short quantitative assembly task for the three classical charges |

The supplied answer page places the combined rubric before the numbered solutions. EX10-011 recommends putting final synthesis feedback last. This is a low-cost sequencing decision, not evidence that the answers are wrong. All solutions occupy PDF page 22, so reordering alone cannot guarantee blindness. The partial rubric exposure in this review came from a tool retrieval that included too much text; it must not be blamed on the manuscript or used as a simulated human result. The lecturer's proposed modules and perspective-specific explanations are in [the informed perspective checks](perspectives.md).

## 7. Cross-document dependencies and formal meaning

The expert companion's opening is a useful source for the construction's two decisive reductions. It explicitly identifies the conditional sampler and capped address predictor, and it separates the fixed $k$ result from a uniform refinement. The exposition should not inherit the companion's full prerequisite load or add the growing $k$ family to its main teaching target. Its own fixed-exponent argument already reaches the stated equality. [Companion, lines 12–91; exposition, lines 468–480.]

The current packaged reasoning record supplies the detailed destinations examined in the mathematical audit: exact circuit arithmetic, coherent local tests, bounded amplification, the explicit logarithmic count, finite minimax, early/late zero discovery, the XOR simulator and the growing-parameter interface. The complete analytic Forrelation argument and the complete imported universal-bound proof were not independently re-proved in this review. Their availability in the packet is distinct from having audited them. [Mathematical verification §§6–7.]

The formal statement comparison also has real content. The family challenge leaves the quantum logarithmic exponent existential and states the classical lower bound with a floor. A separate theorem for the named explicit circuit supports six and $1/400$. The supplied sources substantiate that distinction. Allowing input length zero in the exposition, while the formal universal-power definition starts at one, does not change the exponent set because the extra functions are constant. These are statement-strength and equivalence observations, not new error findings. No Lean, Lake or Comparator process was run.

EX10-010 concerns only the placement of evidence chronology. The clause using `some` teaches why the domain-bit board fails. The old preparation-time comment and its later dependency evidence belong at a linked audit destination. The reader should not need to reconcile historical build states to understand the mathematical clause, and the exposition should not imply that a new execution occurred.

There is a separate link-verification limit. `LINK_MAP.json` reports that the 13 linked record occurrences and the linked companion at the pinned revision differ from the current packaged prose. This review read the packaged counterparts. Attempts to fetch the exact GitHub prose and the pinned source-preprint URL returned `DisabledError`; the live pinned prose was not independently inspected. Consequently, this return does not certify that every online destination contains every current repair. Supplying the pinned prose snapshots, or checking a deliberately updated pin, would close that evidence boundary without asking for new mathematics.

## Revision order and acceptance

First decide the main teaching route and move material according to EX10-001, EX10-005 and EX10-008. Then normalize the recurring example references and exact-artifact notes. Replace rather than duplicate the error and cost accounting. Finish with the projection stage label, the duplicated connective, the formal-status placement and solution order.

After reordering, perform three concrete checks on the corresponding construction, quantum and classical reading routes; a reader using only one route may accept the other bound as the article permits. Starting from the declared prerequisites, reconstruct one winning candidate and explain why an off-promise rival cannot defeat it. Starting from a fixed pivot history, derive the joint success mass, its conditional law and the reason later failure cannot erase a listed winner. Starting from the planted pair, derive the three classical charges and then the fixed $k$ ratio. Each check must preserve the exact event, cap, circuit and quantifier conventions listed in the corresponding structured finding.

A merely serviceable revision would make those passages locally correct and navigable. An excellent revision would let the reader reconstruct why the operations were chosen and retrieve their roles without carrying the exact schedule constants or implementation indices through every page. The proposed acceptance tasks assess that difference. No claim of actual reader improvement is made until someone performs them on the revised edition with exposure recorded.


## How the prior review changes this advice

The historical audit inspected every EX9001–EX9135 finding and its individual decision, plus 49 relevant RR9 originals and XP9-122. Its 185 entries resolve 175 old concerns, identify nine different consequences of applied repairs, and leave one narrow request partially unresolved. Those are historical assessments, not 185 fresh findings. The other 353 R9 IDs are explicitly listed as uninspected. See [history_summary.md](history_summary.md) and [previous_round_audit.json](previous_round_audit.json).

The principal preservation constraints follow directly from that audit:

- EX9005–EX9007, EX9011 and EX9031–EX9033 supplied accurate opening qualifications. EX10-001 moves them to where they become useful.
- EX9060–EX9061 supplied the retained-workspace calculation; EX9075 and EX9077–EX9079 supplied the reflection, finite schedule and endpoints. EX10-005 relocates this material intact.
- EX9084–EX9086 supplied the distinct error cases, common query unit and logarithmic enlargement. EX10-007 offers a comparative replacement presentation, not a still-missing calculation.
- EX9104–EX9105 and EX9121 supplied the capped-predictor rubric; EX9122 separated prompt and feedback. EX10-008 and EX10-011 address a different task and a different answer-navigation consequence.
- EX9014, EX9034, XP9-122 and retained RR9-152 explain why the XOR model warning must precede execution. EX10-009 moves only the coordinate translation.

The narrow substantive challenge is EX9034: variant introductions and independent-toy resets are present, but later “the board” references still leave the persistent cycled-board identity implicit. The other disposition challenge concerns EX9130's evidence pointer: its repair is at line 494, while the decision incorrectly cites line 98. Correcting that pointer does not reopen a proof-status complaint. Live packet metadata also repeats an incorrect author label and omits two figure links from its inventory; [method_feedback.json](method_feedback.json) separates those packaging issues from manuscript mathematics.
