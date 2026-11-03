# Integrated critique by document

The detailed findings, exact current quotations, severities and advice are in `feedback.json` and the readable `findings.md`. This account explains priorities and tradeoffs. A claim that a proof was recoverable in the inspected scope is not a new Lean, Comparator or independent human verification.

## Expert companion: overall critique from the lower-bound panel

The companion is now a credible specialist account of the separation, and a reader interested in randomized lower bounds would read its classical proof to the end. The principal planted-distribution argument is recoverable without following every link. The reader can identify the common hard law, the independently hidden column, the two first-difference events, the capped address predictor, and the final budget charge. The main remaining work is to make those mechanisms more prominent than the numerical refinements and to repair several small statements whose compression is misleading.

I found one definite mathematical-description error in the historical discussion, rather than in the core mL lower bound: §1.3 says that each zero of a nonmarked column in the ABBLSS construction points back to the marked column. The requirement applies to the selected highlighted zero/leaf, not every zero. The cited source's algorithm explicitly permits other zero cells to give irrelevant destinations. This is a local correction with no effect on the present construction, but it matters because the paragraph is meant to explain why the predecessor did not already supply the desired randomized separation.

Figure 2 has a separate concrete inconsistency. It claims m=4 but draws eight bits in each X_i. The source uses four rows and a loop of eight bit positions. The two-panel idea is sound; the scale needs repair. Figure 1 is visually useful but should more strongly communicate that every column owns an array. Showing only the winning column's array risks reviving the shared-cheat-sheet mental model that the new lower bound escapes.

### The most consequential mathematical presentation issue

The largest remaining gap for this panel is in §5's proof outline. The text correctly distinguishes the rounded-Gaussian planted law from the minimax law on the promise, but does not show the bridge from off-promise indistinguishability to promise hardness. “Because the promise is one-sided” is too compressed. The record's §3.14 gives a pointwise acceptance comparison whose expectation combines planted positive signal, uniform leakage and amplified error. Those quantities explain why the error must become exponentially small in k and why the amplified depth has a k factor. The companion gives more space to the explicit threshold arithmetic than to this logic. Reversing that emphasis would improve the mathematical explanation without adding a new theorem or reproducing the analytic proof.

The direct-product proof has a smaller version of the same weighting problem. Its unnormalized form is elegant, but “the recursion absorbs its two branches” skips the algebra at the exact point where adaptive interleaving must be controlled. One common-factor calculation would make the proof immediately auditable. Elsewhere the paper keeps several lines of elementary floor estimates and padded logarithmic accounting. Those are the natural places to recover the space.

### The classical proof's useful next layer

The generic reduction should be visible as a theorem-shaped goal before the proof: an arbitrary partial P, a realizing circuit C, a hard cap L<R(P), and R(F_{P,C,m})>⌊mL/100⌋. The present section already proves that statement. Naming it clearly would help a specialist see what comes from the construction and what comes from the Forrelation supplier. It would also avoid using F_{k,m} while P is temporarily arbitrary.

The erased-zero estimate needs a qualifier, not a new argument. Its conditional uniformity holds before the first discovery, and repeated queries do not create additional discoveries. The compressed companion statement can sound false after a zero is already known. The source and record state the intended event precisely. Restoring that precision is cheap.

The planted-cell paragraph has the right reduction but too many operations in one block. It should define the simulator, then separately prove that the original joint event is contained in simulator success. The paper already makes the central distinction correctly: it does not condition the hard input law on nonheaviness. The final union and average deserve one more visible line, because the cancellation of the factor m is a decisive part of preserving the exponent.

These changes would let the intended reader take away a compact three-term argument. At present the reader can reconstruct that argument, but its most memorable ending is liable to be a collection of constants. The desired memory is: independent choice of the selected column makes discovered zeros rare; low total budget makes heavy columns rare; the direct product makes a successful guess of an unlearned address rare even after all query times are counted.

### Earlier work and the role of the companion

The historical arithmetic is a genuine improvement. It shows how the partial-function exponent enters the old AND–OR cheat-sheet recipe, instead of merely listing 5/2, 8/3 and 3. Move the polylogarithmic Q(g) condition before the displayed bound, and explicitly connect certification of the inner outputs to certification of the outer promise. The equality heading in the history table should also become one-sided separation language.

The text now handles several credit distinctions well. It credits Ben-David's earlier super-Grover construction, qualifies the Shaltiel result, recognizes that Drucker's global-budget theorem already suffices, separates Walsh Forrelation from random-orthogonal Rorrelation, and distinguishes certificate-complexity comparisons from randomized complexity. Those fixes should survive the next round. A new related-work citation to Ben-David–Blais can be brief and optional; its cost measure is not the same premise as the elementary lemma here.

The opening contribution paragraph remains too close to a project inventory. The construction's mechanism, the companion's proof scope, the explicit constants, two observations, the long record and Lean are all packed into one enumeration. A shorter mathematical statement of what this companion adds would serve the reader better. The exact constant list belongs with the quantitative results, not ahead of the mechanism.

### What should be retained intact

The strongest parts of the present companion are the distinctions it states locally. The same circuit serves both bounds. A loser fails some local test at every address. A winner defeats an opponent even if the opponent's address inputs are unpromised. The comparison symmetry comes from a fixed sorted-pair circuit. The physical sampler realizes w_i/W without computing the weights. The coupling is performed one stage at a time conditional on the entire past. The capped predictor enforces its budget before an excess call. Its success estimate is a joint event under the original law. The exponent argument fixes α and k in the correct order.

The formal section is also much better focused. It explains meaningful mathematical interfaces instead of presenting commands and receipts. Its joint-success-and-compliance description should remain. The one inference from “no hypotheses” to “proofs complete” should be repaired: unconditional scope and evidence of proof completion are different facts already supplied by adjacent sentences.

The growing-k remark is an optional refinement of the main proof. It should stay visibly optional. Its displayed finite lower exponent is negative at the first allowed parameter, so validity of the formula must not be confused with a useful finite separation example. No sharper bound is requested; the issue is explanation and proportion.

With these changes, the companion would give a lower-bound specialist the right result, the right ancestry, and a proof whose expensive steps are visibly the ones that need attention. The needed revision is concentrated: sharpen the few misleading compressions and shorten the arithmetic that does not drive the theorem.


## Exposition: overall critique

### Verdict

The current exposition contains a real randomized lower-bound argument. It should not be dismissed as a dressed-up claim that the address is hidden. Section 5 gives the hard distribution, the coupled planted pair, the independence of the planted column, the two possible distinguishing events, the separate-cap direct product, the capped predictor, the joint light-and-hit event, and the budget accounting. In several places it is better at teaching a delicate probability distinction than the short expert account. The domain-bit board, the marginal-uniformity counterexample, and the AND example separating joint from conditional success are all worth retaining.

The remaining gap is between containing that argument and making it reconstructible by the audience fixed in the packet. The draft declares a graduate audience already familiar with several substantial quantum and lower-bound tools. Its first concrete object arrives after a dense two-page opening. It spends considerable main-path space on a numerical amplitude-amplification recipe and circuit implementation vocabulary, while the one decisive predictor simulation is only executed in the record. A reader could master every current exercise and still not be able to explain why an arbitrary cheap sequence of cell guesses is covered by the lower bound.

### Changes that matter most

First, repair the exact local mathematical and probabilistic wording. In the erased-zero proof, condition on the entire preceding transcript prefix before each query. Conditioning on the completed transcript does not establish the claimed next-query probability. The intended argument is supported and the expert companion already has the correct temporal wording; this is not a claim that the lower-bound theorem fails.

The sentence denying any hard distribution at m=4 is false under the section’s own definition. The uniform law on a-plus and a-zero is hard for zero-query deterministic algorithms. The toy fails the useful positive-budget application, not existence of a hard law. This is a small but instructive distinction between a bound becoming vacuous and a mathematical object ceasing to exist.

Question 4 must distinguish a lower bound on an infimum from failure of an endpoint inequality. The displayed strict recipe validly chooses k=5 for exponent 3.5. But the statement that k=4 does not suffice for α_tot≥3.5 is wrong: that one fixed family rules out every exponent below 3.5. It does not have to rule out the endpoint to prove the lower bound on the infimum. The nearby phrase that k=2 gives exactly the cube should be sharpened for the same reason; logarithmic losses are still present.

The quantum walkthrough also needs its probability modality preserved. The realised trial and iteration counts are random and may stop early; it is their maximum cap that is fixed. In the answer to Question 2, a one-quarter pivot success probability really does become one after a suitable Grover iteration. That does not make final verification exact. Columns 2 and 4 certainly fail local string tests, but the stated bounded-error search may miss a failed test. The answer should not promise their rejection on every branch.

Second, bring the capped-predictor operation onto the main teaching path. The important question is not whether the reader remembers that addresses contain r answers. It is whether the reader can take a chosen query slot of a dummy execution, supply independent side information, stop before exceeding L forwarded queries, and output a candidate address without reading cell contents. The record already contains a small trace. A compact portion of that trace, with a stopped run and a successful selected-slot run, would teach the missing operation without adding new mathematics. Explain why the default output is legitimate overcounting and why lightness remains inside a joint event.

Third, align the opening intuition with that proof. The current statement that a classical algorithm must pay to learn addresses encourages a stronger per-run interpretation than the proof supplies. The actual argument controls both expensive columns and lucky cheap guesses. Section 5 now says so explicitly. A newcomer should encounter that distinction first in the overview and then see how the simulator proves it.

Fourth, rebalance the quantum side. Preserve the failure of nested Grover search, the dominating nonwinner, the cycle among losers, the ideal-versus-implemented process distinction, and preservation of the conditional pivot law. These are construction-specific reasons that explain why the algorithm works. The 9/40 amplification recipe and the exact logarithmic trial count are supplier-proof detail. Prior dispositions planned to make them optional, but they remain in the current main text. State the capped contract and route its constant calculation to the record. Similarly, the exact circuit’s size and role matter more to the lesson than an incomplete sketch of ripple-carry implementation.

Fifth, explain the representation issue in the pointer credit. Ambainis and coauthors discuss direct pointers to every other column but reject that representation because its alphabet cost obstructs their Boolean construction. The current attribution is literally defensible and should be kept; its significance is incomplete without that objection. Explain why indexed access to pointer bits and local comparisons change the relevant cost here. This is both a credit improvement and an answer to a natural “why was this not already the old gadget?” question.

### What the reader should leave able to do

The intended newcomer should be able to build the four-column Boolean input, identify exactly which winning condition fails in a changed board, and distinguish a cheap off-promise decoder output from a valid domain certificate. They should understand why testing every candidate inside Grover search loses the desired exponent, why pairwise comparisons need not define a total order, and why the algorithm verifies its short list.

For the classical side, they should be able to state why the two coupled runs agree until a changed coordinate is queried, why the independent planted column averages over the dummy execution, and why a lucky true-cell query can be converted into a capped predictor. They should distinguish a joint event from a conditioned hard distribution, and identify the global, column and per-instance budgets. Finally, they should know why a hard-law argument plus all-input bounded-error correctness forces a contradiction, and why k is fixed before m grows.

The draft already contains most of the ingredients needed for those outcomes. Its current exercises assess only part of them. Add or retarget a changed-case task at the simulator, rather than expanding the number of routine arithmetic exercises.

### What must be kept

Keep the precise query-cost convention; the signed eight-bit examples and their off-promise outcome; the statement that every bit assignment is allowed; the changed board isolating the domain bit; the correct four-position exposition figure; the public-circuit-versus-stored-values distinction; and the statement that both bounds concern the same circuit.

Keep the two different comparison counterexamples, the declaration that weights are analytical and never estimated, the absorbing state, the conditional-law argument, and the no-winner and early-stopping discussion. Keep the dummy-run coupling convention, the explicitly allowed address guesses, the independence example, the direct-product conditional-value example, the lightness selection-bias example, and the three-budget paragraph. These are substantive repairs already present; a new round should not erase them by mechanically shortening every paragraph.

The formal-evidence section should keep its statement that the logarithmic power is unspecified in the formal family theorem and its concrete invitation to inspect a winning-condition clause. The report of verification can be shorter without weakening that scope distinction. The original theorem and construction attribution should also remain explicit.


## Overall critique: the long record's construction and classical side

The detailed classical proof is substantially stronger than its opening summary. In the inspected sections, the hard distribution, independent-information reduction, cap-event logic, erased-zero identity, simulator, and final budget accounting fit together correctly. The most important mathematical correction is local: the introduction states an eventual planted-cell discovery probability without the time-union factor and without preserving the joint-event qualification. Section 6.5 already supplies the right statement. The next revision should make the overview faithful to that proof.

The record also has a serious maintenance problem at its navigation layer. Current companion section numbers, the removal of §6.7, and the addition of the growing-\(k\) derivation have not propagated to all referring passages. These are not cosmetic errors in a document whose declared purpose includes letting a reader move from a short account to a complete argument. The opening map points to the wrong companion range; the classical chapter sends readers to §5 and even nonexistent §5.5; the catalogue still denies a schedule that §7.3 now proves. A reader who follows the advertised route can reasonably think a proof is missing or that two parts of the record disagree.

### What a specialist currently takes away

A persistent reader finds a sound and unusually explicit planting argument. A generic partial function \(P\) supplies a promised hard law \(\mu\). Each column contains several independent samples, whose values select a certificate cell. The dummy input has one independent hidden zero per column and fixed blank cells. An independently selected column becomes a winner after its zero is erased and its true cell is filled. A classical tree can distinguish the coupled inputs only by discovering the erased zero or by asking a coordinate in that selected cell. Heavy columns consume the total address-query budget. For a nonheavy target at a fixed prospective query time, the query coordinate itself predicts all address bits under a genuine capped algorithm. That yields the direct-product bound and then the time union.

This is the right understanding. The present ordering makes the reader work too hard to maintain it. Section 6 begins with a long standard-ingredient development before displaying the construction-specific random experiment. The direct-product discussion is valuable, especially its careful posterior law and side-information hypotheses, but it occupies the position where the reader most wants to see what has been sampled and what changes under planting.

The desired takeaway should be available on the first pass: three discrepancy terms, three different reasons they are small, and one exact predictor reduction. The complete details should remain close enough to inspect. This is a routing problem rather than a request to delete the record's proof obligations.

### Priorities for revision

First, repair the opening probability claim. The fixed-time statement is a joint bound on nonheaviness and a correct cell query. Eventual cell discovery costs the union over at most \(G\) query times. Conditioning on nonheaviness is not licensed; the record's own example explains why. The correction should be propagated as a single invariant through every summary, rather than treating the early passage as harmless intuition. This is incomplete propagation of a previous fix, not a newly discovered flaw in the main theorem.

Second, reconcile the reading routes and catalogue against the current headings. Links must be checked semantically: reaching a file is insufficient if the referenced section concerns another topic. The growing-parameter claim needs the same treatment. Fixed-parameter estimates alone do not justify a varying schedule, but §7.3 uses a uniform estimate and obtains one. The catalogue should state the narrower caveat or point to the existing derivation, rather than contradict it.

Third, improve the first lower-bound route. Keep the generic theorem at the front. Identify exactly which direct-product statement and cap-event paragraph the reader needs, then move them into the dummy/planting experiment without requiring both proofs and both illustrative counterexamples first. One table of the sampled objects and their dependencies would pay for itself repeatedly. It must show that the address is a function of the target input tuple, while \(I\), the zero locations, other columns, and blank cells are independent of that tuple in the required groupings.

Fourth, make the loss accounting visible. The proof preserves the factor \(mL\). The logarithmic address length is selected to survive the union over potential query times. The floors lose constants. The displayed Forrelation budget supplies the denominator used in the final family. A short inventory of those roles would answer the specialist's immediate question about where the near-quartic exponent is lost, without adding a theorem.

Fifth, give the examples distinct jobs and consistent labels. The finite Forrelation board demonstrates the actual semantic predicate and isolates the domain check. The XOR board illustrates the coupling and the simulator. These are useful different tasks. Changing both the partial function and the indexing convention unnecessarily makes them feel like unrelated constructions. One small gate-level example before either large board would also explain how transcript bits certify circuit evaluation.

Sixth, finish separating mathematical explanation from execution history. Source types inside basic model definitions, an old textbook-section correction, the “baseline” referent, and the old-core-versus-wrapper discussion interrupt otherwise clear mathematics. The new Appendix G is the right home for this material. Historical receipt statements should identify their snapshot and declaration set so that a later compared endpoint does not appear to contradict them.

### What should be protected

The conditional-value direct-product proof is worth preserving in full somewhere accessible. Its proof of the posterior product law, its allowance for dependence within each instance, its exact one-factor update, and its joint-independence warning are not redundant formalities. They prevent the common wrong proof of this type of lower bound.

The truncation argument should also remain explicit. A cap event is not an independent condition under which hardness can simply be reapplied. The record proves a joint-event bound by constructing a new capped algorithm. The distinction between a total \(rL\) budget and the simulator's total \(L\) budget is handled correctly. The simulator then extracts the address before querying the cell contents. Those are the core pieces of the reduction, and none should be compressed into a phrase like “by direct product.”

The independent selection of \(I\) and the example showing that uniform marginal selection is insufficient are particularly useful. The erased-zero estimate belongs to a simpler probability experiment than the address-hardness argument; the formal evidence discussion correctly identifies that boundary. The first-difference argument also correctly overcounts cell visits even if a planted bit happens to remain equal to its blank value.

The semantic totality argument, the isolated domain-check board, and the winner-only comparison invariant should remain. They establish what happens on arbitrary total inputs without pretending that a promise algorithm has a meaningful answer everywhere.

Finally, the exponent discussion preserves three distinctions that matter: the two bounds concern the same total function; fixed \(k\) gives a strict threshold below \(4-2/k\); and the explicit growing-\(k\) estimate does not establish an exact \(\Omega(Q^4)\) separation. The conservative explicit constants are acceptable once their purpose is clear. They do not all need to compete with the main mechanism for attention.

### Relation to the earlier review

This pass does not reopen the resolved complaint that Drucker's global-budget theorem was misidentified with the separate-cap result. The current comparison and attribution are much better. Nor does it repeat a demand for unexplained duplicate proofs: the second proof now states how its normalization differs and why both calculate the same object. The new finite-example checks and the evidence appendix are also genuine improvements.

The remaining pattern is incomplete propagation. Local fixes have improved individual passages while leaving summaries, catalogue entries, routes, and historical notes on different versions of the story. A future revision should test these layers as claims about the same current manuscript. The success criterion is that a reader can enter from any of the three documents, find the current proof, and recover its actual hypotheses and scope without reconstructing the editing history.


### The Forrelation and quantum destinations in the long record

The expanded record does real explanatory work. It does not merely attach proof names to an asserted separation. The Gaussian-chain argument states which random variables are independent, the derivative transfer records the dependence of accumulated weights, and the tree estimate works with the raw derivatives actually needed under biased signs. The promise-gap argument then turns moment information into an acceptance gap without pretending that the rounded law is promise-supported. These are the passages that make the record worth consulting.

The main remaining weakness is that the mathematical importance of a calculation and the space allocated to it still diverge. The reader sees detailed constants before being told what fixes the power m^(1−1/k). After (F33), explain the balance between d^(k/2) and m^−(k−1)/2. Around (F43), identify the separate k losses from derivative growth and amplification. These are explanatory changes to an existing derivation. They require no stronger theorem. Likewise, the promise gap should motivate error reduction before the count of repetitions is derived.

The hardest section is the contracted-array and stopping argument in §3.11. Its statement is precise, and its proof protects the conditional-law issue correctly. A two-coordinate example would reduce more reader effort than another paragraph restating the source lineage. The existing three-block calculation in §3.10 shows why this kind of example works: it exposes a disappearing derivative and the fixed earlier weights, both of which are easy to miss in the general formula.

The quantum chapter is strongest where it explains the exact output law and weakest where it slips into implementation vocabulary. It correctly samples the ideal weights without computing them and couples the implemented process to the ideal one history by history. The candidate-verification soundness is also clear. Internal claim names should become readable references, and the sentence relating a physical label theorem to a successful-state assertion should say whether it describes ordinary mathematical implication or formal dependency. G.7 already supplies the distinction. A new proof project is unnecessary.

The record's navigation has a concrete regression. A link may open the intended file while its visible section number names a different argument. The tournament return points to companion §4.2 instead of §3.2; analogous classical returns are also stale. This is not a demand for more routing prose. It is a request that the existing route become accurate and bounded.

Appendix A gives a recoverable proof of the known universal quartic bound. Preserve the maximum-degree face, the signed-cube eigenspace argument and the common-original-input explanation in the maximal-monomial tree. The numerical variants and source-prefactor discussion should remain subordinate to those ideas. Existing formal alternatives are useful in G.9, where their different coefficients and dependency roles can be compared directly.

The source discussion now distinguishes explicit Forrelation from rorrelation, and distinguishes the altered rounded law from its antecedent. That is a success. The same allocation is repeated in several nearby summaries, however. A compact source-location index would serve the final subsection better than another narrative explanation. The principle is to preserve local credit and complete derivations while spending repeated prose on the next inference the reader needs.
