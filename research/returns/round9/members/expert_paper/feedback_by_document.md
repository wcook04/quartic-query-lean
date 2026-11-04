# Round-nine critique of the expert companion

## Editorial decision and mathematical scope

Revise before treating this as a self-contained specialist companion. The required changes are concentrated in what a reader may infer at each step, how the reconstruction's contribution is distinguished from the original result, and how the optional uniform refinement connects to its promised application. The supplied main quantum and classical reductions did not yield a counterexample or a failed inequality in this review. That is a limited review result, not a certification of the full development. The complete Gaussian and martingale reconstruction and every Lean dependency were not independently re-proved.

The detailed findings distinguish local mathematical qualifications, omitted proof transitions, first-encounter costs, source and evidence presentation, and optional editorial refinements. They are ordered by encounter. Several findings can be repaired by the same structural edit; they should not be interpreted as separate demands to lengthen the manuscript. The revision should make the decisive arguments easier to assess while removing material that does not serve the intended specialist at its present location.

## 1. The first page needs a more decisive allocation of attention

The title states the headline mathematical result, the subtitle identifies a companion, and the abstract eventually names the two reconstructed reductions. The principal reader decision is nevertheless delayed: what does this manuscript add to OpenAI's preprint, and what is its independent technical purpose? Section 1 states a detailed theorem with the reconstructed numerical choices before the contribution paragraph. In the supplied PDF, the sentence naming the two locally checkable steps breaks after its colon at the page 1–2 transition.

Bring the attribution and reconstruction task forward enough that a specialist can classify the paper before investing in the construction parameters. This does not require weakening the theorem or multiplying disclaimers. It requires attaching the original result, the reconstructed reductions, the optional additional quantitative estimate, and the formal correspondence to their respective owners. The original preprint already contains the tournament and capped-predictor analyses; making those arguments locally auditable is a reconstruction contribution, not a claim to have originated them. The abstract's description of the single family also depends on the optional uniform argument, whereas the main fixed-parameter proof establishes the optimal infimum by choosing a different fixed k for each excluded exponent. Those are compatible mathematical claims, but their different proof routes should be visible.

The abstract introduces k without a role explanation and compresses the addressed-certificate construction, hard distribution, comparison guarantee, tournament and final verification into a small space. Select the minimum mechanism that explains the quartic power and use a short indication of the two reductions as the contribution. Avoid making the abstract function as a miniature notation dictionary. Treat the theorem's citation and the reconstruction's numerical constants separately so that its visual citation does not suggest that the explicit sixth logarithmic power and coefficient1/400 were stated verbatim in the cited theorem.

The statement with a universal constant over all total functions is the right object to assess, but the prose saying k=3 gives power10/3 needs the same precision as the displayed argument: logarithmic losses mean that every smaller fixed exponent is excluded. A reader should not have to infer whether a bare power is exact, suppressed-logarithmic, or a limiting exponent.

## 2. Construction and ancestry need clearer division of tasks

The reader is asked to understand the column layout, partial-function promises, gate transcripts, addresses and outward pointers almost simultaneously in the overview. The formal definition later supplies the necessary detail. Make the overview's limited role explicit and introduce each payload by the task it performs. Hard answers select a cell; transcripts enforce that those answers are defined and correct; outward pointers rule out competing all-one columns. These are different obligations, even though they reside in one selected certificate.

Preserve the distinction between a coordinate query naming an address and a content query revealing information. The classical argument turns the position of a cell query into a predicted vector before any content is read. A brief operational description at the first address discussion will reduce the later burden of the simulator proof. Likewise, distinguish a comparison's pointer-following cost from the address-decoding cost; the ell+1 bit-query count only covers the former operation.

The historical cost calculation is useful only if its variables, assumed partial-function properties and quantifier regime are stable. Its conclusion is a limitation of the particular AND–OR/cheat-sheet recipe under the displayed estimates. It is not a general impossibility theorem for all totalizations. Check the broad claim that the later exponents came from that framework against the cited editions and narrow the wording to the specific sequence being discussed. When using little-o terms for partial separations, name the parameter limit rather than leaving a reader to reconcile them with a fixed-k convention unaided.

The pointer discussion should emphasize the relevant resource change: large certificates are split into separately addressable bit fields. It is not enough to say that exponential alphabets were avoided. The reader must understand which part of a certificate can be inspected cheaply and which is still expensive enough to require verification. Figure1 should name the owner of its enlarged array directly. Figure2 should visually indicate that the two panels share the same sampled address inputs, not merely the same distribution.

A source updated after the previous packet is relevant here. Arora and Kumar's *Quantum Query Complexity of Tournament Solutions*, arXiv:2610.39702v1 (29 October2026), §6.1, obtains a fixed-edge Condorcet winner by king finding and verification. This supplies a current comparator for the paragraph discussing king finding. Its oracle model remains different from arbitrary fractional loser comparisons; it does not replace Proposition3. See `literature_comparison.md` for the precise scope of this addition.

## 3. The quantum proof should expose its contracts without repeating its machinery

The quantum proof needs three different outputs: a label sampled from an exact conditional law, a list that includes a genuine winner with high probability, and a Boolean decision whose resource cap holds even when no winner exists. Keep those contracts distinct at every transition. In particular, “exact” belongs to the conditional label law. It does not imply certain success, a known preparation probability, a zero-error final algorithm, or a theorem returning an arbitrary successful quantum subsystem.

The bounded amplification lemma separates p=0, p=1, intermediate probabilities and subthreshold probabilities. The remaining presentation task is to make the fixed trial schedule and resource accounting auditable without forcing the reader into the long record for the definition of the randomized trial itself. Any further abbreviation should preserve the direct-measurement branch, the finite cutoff and the reason all successful trials have the same label law. The conditional law must survive both randomizing the iteration count and stopping at the first success.

For comparisons, the sorted-pair convention, deterministic tie rule and self-comparison rule are not cosmetic. They create the complementary probabilities used in the drift identity. Keep their connection to the identity local. The winner needs only its own decoding to be correct: every pointer from an opponent into its all-one string reads one, regardless of the opponent's promise status. That is the mechanism behind the total-function construction and deserves priority over generic explanations of quantum search.

The weighted process is an analysis device; the circuit reconstructs a product experiment from the measured history. Fresh workspaces multiply success probabilities for a fixed label, and orthogonal label registers add their masses. Do not describe this as an assumption that input bits are independent. Make the empty-history case explicit, and distinguish the exact joint mass w_i/m from the normalized label law w_i/W. The four-candidate numerical example is internally consistent: the first selected pivot gives success 23/48 and the second gives 19/60. Its teaching value would increase if the multiplication of the old third weight by a fresh comparison probability were more visually immediate.

The coupling argument is conditional on the entire past. A history-dependent failure probability must not be folded into a globally conditioned law. The present proof recognizes this, but several suggested abbreviations would erase the distinction. Compress repeated declarations that weights are not computed, rather than the conditional coupling. Similarly, make it explicit that retaining a winner once selected is enough; a subsequent stage's failure cannot remove it.

Verification is a separate Boolean task. A false candidate can be dominant, and a failed defect search is not an exact certificate. On a zero-input, the accepted-candidate events are union-bounded under the selected history. On a one-input, accepting an incorrect candidate already produces the correct Boolean answer. These cases should remain separately stated. The final query accounting should show enough substitutions that the loose sixth logarithmic power is transparent, without turning the expert paper into a derivation of every numerical envelope.

AppendixA.3 should make its robustness to decoding errors explicit. Every rival pointer reads one in the all-one first column. The first column’s own pointer can read either zero or one: the outcomes are therefore(0,1) or(1,1), and both select column1 because it wins ties. Thus the asserted sure dominance does hold even at a wrongly decoded address. An initial reviewer concern about this claim was rejected after checking the actual comparator; it is not counted as a mathematical error.

## 4. The classical reduction needs complete operational conventions

The hard distribution must be introduced with three separate facts: every target block is drawn from a promised-input hard law; different address instances are independent; and the selected column is independent of the complete dummy input and run. Uniform answer bits are not required. A uniform marginal selected column is insufficient. These distinctions are substantive premises of different steps and should not be merged into a generic assertion of randomness.

The separate-cap direct-product lemma can be assessed through its unnormalised value recurrence. Its application to the simulator uses a total target cap L, which implies cap L for every target instance. State that implication where it is used. The optional Drucker global-budget calculation is an alternative supplier, not another lemma the main proof needs. If retained, its parameters should be instantiated explicitly enough that the extra factor2 can be checked against the discrepancy slack. The source comparison below confirms that this route is consistent with the displayed constants.

In the coupling, a visit to the selected cell is an event covering a possible first changed answer. The queried bit need not actually change. Keep that overcount visible so a reader does not infer that a cell hit is a distinguishing event with certainty. For the erased zero, the probability is E Z/m because the selected index is independent of the whole dummy run; it is not the probability of any single fresh query succeeding. The early/late argument counts discoveries and distinct rows before discovery, while its resource charge can count all queries. These uses of “query” need stable descriptions.

The simulator paragraph is close to an executable definition but omits the case in which the original decision tree terminates before the specified time tau. The long record supplies the missing convention: return the fixed fallback vector. Include that convention locally. Also define the proposed time's query before reading its answer, separate the original-tree clock from the target-query cap, and state that a repeated target query consumes the cap. The supplied PDF happens to split the two-clock sentence across pages 10–11; that sentence should remain physically whole in the next render.

The central event is lightness and a true-cell query at a fixed time under the original law. It is a subset of an unconditional predictor-success event. No conditional hard distribution on light columns is introduced. The factor m disappears only after averaging over the independent selected column. Keep the order “fixed column and fixed time; bound; union over time; average over column” explicit. This is the specific inference the paper says it makes locally checkable.

At the end, the floor constants and the power calculation can be short, but the reader should know which inequality absorbs each floor and why t>=8 suffices. The sharper optional erased-zero estimate is not needed to close the argument and can be moved to the record unless it serves an explicit comparison. AppendixA.5 must state that the parity inputs are uniform; independence of the two instances alone does not force the claimed one-instance optimum.

## 5. The optional uniform refinement has the largest remaining dependency gap

Section 5 completes the fixed-k proof. Section 6 changes the quantitative supplier and then promises a single family with growing k. A sufficient condition t>=13669k² is presented for the old budget L=floor(m^(1−1/k)/ell²). Shortly afterwards the manuscript chooses k=floor(sqrt(t/20)). That schedule does not satisfy the preceding sufficient condition. Reading these paragraphs as one unchanged budget leads to a false objection.

The record resolves the issue explicitly. In §7.3, lines3788–3797 of the supplied current text, it defines

\[
X=\frac{2}{18225}\frac{m^{1-1/k}}{k^2\ln(4km)},\qquad L=\lfloor X\rfloor,
\]

uses the generic lower bound with this new L, and obtains

\[
R(F_{k,m})>\frac{m^{2-1/k}}{1822500\,k^2\ln(4km)}.
\]

The companion should show this change of budget before stating the growing schedule. This is a missing local inference, not a contradiction in the supplied record and not a request for a new bound. The explicit quantum envelope is then combined with the same circuit family. The finite parameter conditions and floor handling can remain in the record if the local statement identifies them accurately.

A second transition concerns the acceptance function. The shallow-tree estimate is introduced for a deterministic depth-d decision tree, whereas pointwise low-error correctness is a property of a randomized solver. Extend the expectation estimate to finite mixtures by linearity before invoking the pointwise envelope; do not fix a random seed and assume pointwise correctness survives. After error reduction, make clear which depth belongs to the repeated solver and how the O(k) repetition cost is charged. These are existing argument steps to expose, not stronger theorems to add.

At the first use of ν1, identify the finite random object and link its exact construction. Attach the displayed shallow-tree inequality directly to record equation(F33), and identify the property supplied by the changed truncation. This gives a specialist a defined imported object and an exact proof destination before the averaged-acceptance and amplified-depth argument. The pointwise sandwich then explains why possible off-promise mass is permitted. These are local definition and dependency repairs within the already-attributed reconstruction.

## 6. Formal claims and navigation need evidence that is easy to interpret

The four configured headline targets, the existential family, the named-circuit constants, the uniform estimate and the auxiliary direct-product and amplification results have different statements and checking routes. The paper partly distinguishes them, but its links need to preserve those distinctions. A reader following a statement file should understand why that specification contains intentional `sorry` placeholders and where its separately compiled proving solution is. A built declaration should not acquire comparison credit merely by being adjacent to a compared endpoint.

The current packet includes a 3 November 2026 paranoid Comparator receipt for the four configured Unconditional targets. All 70 source-hash entries from that receipt that were present in the packet matched their supplied files. This checks byte agreement with a historical record; the present review did not rerun Lean, Comparator or the external checkers. The named-circuit source also retains an undated “Status: unelaborated” authoring comment. Reconcile that comment with the current recorded build status at the link destination, rather than asking readers to infer which text is historical.

The link map reports zero navigation problems, but25 expert-paper links point to pinned record bytes that differ from the packaged current text. This is not proof that the links are broken or that their arguments differ materially. It does mean that anchor existence alone does not establish that a reader sees the revised passage. Exact pinned GitHub targets could not be fetched through the available web service in this review. Validate the content of the actual delivered edition, especially at the parameter switch, the detailed constants and the statement-evidence discussion. Keep immutable links, but make them point to the intended complete argument.

The bibliography should bind edition-sensitive theorem numbers consistently. Reference checking is a separate task from reading a search snippet, and a citation in the manuscript is not evidence that this review read the entire cited paper. The source register records the actual scope of each reading.

## Cross-document consequences

### Reasoning record

The record already contains the missing early-stop simulator case and the growing-parameter budget substitution. Bring the needed sentence or mathematical transition into the short paper, then verify that the short paper's link lands on that exact argument. The record's AppendixG should remain the detailed destination for comparison scope, ordinary transport and historical receipts. Its presence does not make every abbreviated claim locally self-contained. The full record was not the lead paper in this review; only relevant destinations were read, so no400-finding or full-record coverage claim is made.

### Exposition

The exposition was supporting material, not a second independently reviewed lead. The requested full 250-finding pedagogical review is outside this packet's scope. Cross-document revisions should nevertheless propagate the explanation of tie-breaking robustness in the dominance example, the explicit input law for parity examples, the treatment of a halted original tree, and the difference between the fixed-k and growing-k budgets wherever the same operations are taught. Do not mechanically insert specialist proof detail into its examples-first route. Preserve the distinction between an abstract fractional comparator example and a realized four-column Boolean input.

## How to apply the detailed feedback

Repair mathematical hypotheses and transitions first; then decide the scope and location of the optional refinement; then revise opening allocation, construction explanations and proof navigation; finally reflow the PDF and check the actual links. Retain separate dispositions for old findings that are resolved. The same conceptual issue may have more than one propagation point, but it should not be counted as multiple independent errors merely because it appears in several reader perspectives. The verdict supplies a ranked revision sequence; `feedback.json` supplies source-order repair locations.
