# Reading log: expert companion

This is a section-by-section account of the reading that produced QS001–QS071. It records comprehension and friction rather than impersonating a real referee. The current Markdown was read from the abstract through Appendix A, including the link definitions. The supplied 14-page PDF was used to inspect pages 1, 3, 5, 6, 7, 9, 11, 12 and 14; layout observations below apply only to pages actually inspected. The mathematical source is the packet's current Markdown, not a later public checkout. The record's older PDF was not used to locate current record claims.

## Abstract

The first useful information is the total-function result and the separation of two measures with the same error convention. I understand immediately that the theorem concerns the optimal universal exponent, not a claim that randomized complexity always equals a fourth power of quantum complexity. The attribution to OpenAI is also immediate. The last part of the abstract does substantially more work than the opening apparatus: separate certificate arrays, hard addresses, cheap quantum decoding, and comparisons reliable only for the winner give an actual mechanism.

I slow at “complete argument with explicit constants.” This sounds like a self-contained proof in the present paper. By the end of §1.3 I discover a longer list of cited ingredients and record-only refinements. The issue is the promise made by the abstract, not a demand to reproduce all of those proofs. The abstract could state the role of the companion more economically and accurately.

The classical statement about paying for the address in a constant fraction of columns is a useful heuristic but initially sounds like a literal property of every successful execution. I expect to see a hard distribution and a heavy/light argument, and eventually do. The abstract need not contain that machinery; it should avoid phrasing the distributional argument as a per-column deterministic obligation.

The winner-only comparison guarantee is the phrase I would retain through a severe length cut. It tells a quantum-algorithms reader why this is not just another invocation of minimum finding.

## §1: definitions, theorem and contributions

The formal oracle and worst-case cap clarify the model. The first sentence about reading one bit at a time is less satisfactory: it evokes a classical observation process immediately before a superposition query is introduced. The intended distinction is cheap inter-query computation versus charged oracle access. The conventional bit oracle already says what is needed.

The definition of α_tot is explicit about the order of quantifiers and the constant uniform in the input length and function. The added one is explained. I do not want this precision removed. The family theorem then gives me a concrete parameter to follow, and the k=3 consequence gives an immediate check that the result really refutes a cubic relation rather than merely approaching it from below.

The next paragraph overwhelms that clean opening. It introduces b_k, c_k, a very large C_k, a t threshold, the fixed circuit, counterexamples, two observations, a long record, a uniform Forrelation lower bound and Lean. It spans the page break. I can identify what each item means, but I cannot tell which one is meant to make the companion worth reading. The quantitative Forrelation refinement is particularly easy to miss because it is syntactically attached to the existence of a long record.

My expectation after the theorem is a short answer to “what prevents the usual construction and what is changed?” The paper does answer this, but only after the catalogue. I would relocate constants to the point at which they are used, preserving a short declaration of the companion's explanatory and quantitative contributions.

## §1.1: earlier separations

This is much better than a chronology of exponent records. The displayed AND–OR construction provides a common calculation, and c=1/2, 2/3 and nearly 1 explain the three earlier separation exponents. The restriction of the barrier to this recipe is important. Nothing in this calculation proves a barrier for every possible cheat-sheet construction, and the current wording does not claim one.

There is a small but real premise-order problem. The paper first introduces a general partial g, writes a cost in which the evaluation term is m′, and only afterwards supposes that Q(g) is polylogarithmic. Reading the original cheat-sheet discussion confirms that the small-quantum-cost premise belongs before that simplification. This is an easily repaired scope ambiguity, not a false historical exponent.

The word Rorrelation also arrives before its distinction from explicit Walsh Forrelation. A reader may initially think it is a spelling variation. A short first-use explanation would prevent that. The table is convenient, but its heading uses an equality while combining achieved separation lower bounds with a universal upper bound. The logical direction should be explicit even in an overview table.

## §1.2: first encounter with the construction

The three objects in a column are intelligible: an X string, the address blocks, and an array indexed by the answers to those blocks. The outward pointers make uniqueness of a winner plausible before the formal definition. Figure 1 is useful for this geometry. I can distinguish the selected cell from the rest of the array, and the arrows point to the actual disqualifying zeros.

Two small semantic problems arise at this first encounter. The overview gives every column a true address even though the address function is partial. Later sections fix this, but the off-promise case should be present at the first definition because it drives the comparison problem. Separately, the figure calls the blocks independent. The coordinates are disjoint; independence belongs to the probability law in the lower bound, not to the total function itself.

The classical heuristic anticipates the eventual coupling well: erase one zero and fill one cell. However, the m² claim should be tied to a uniformly hidden column and the expected number of discovered zeros, rather than read as an ordinary search problem on unrelated bits. That connection is easy to make without importing the full lower-bound proof into the introduction.

The next paragraph finally poses the quantum design problem. A naive outer search with an inner verification costs roughly m. The comparison routine is cheap because it reads only the pointer field aimed at the rival. The all-one winner can never be disqualified, even by an unpromised rival. This is the conceptual high point of the introduction. I would put it before the detailed classical heuristic for the present audience.

The power arithmetic is helpful as an overview. I read the approximation signs as exponent-level intuition, not as matching Θ bounds on the exact function complexities. The theorem and §6 must remain the places where the inequality directions are explicit.

## §1.3: lineage and scope

The cheat-sheet and outward-pointer ancestry are now properly connected to concrete roles. The explanation of the back-pointer shortcut is more useful than merely saying that an older function separated D from Q rather than R from Q. The paper also explains why a comparison reads one field instead of a whole exponential-alphabet symbol. This is the right level of historical detail.

The choice of explicit Walsh Forrelation has a role beyond quantum hardness: a compact exact circuit is needed to certify promise membership and the value. That makes the literature discussion part of the construction.

The paragraph about comparisons needs a clearer comparison of contracts. A minimum, a king, a source and a verified accepting column are not interchangeable output notions. Fixed graph edges computed with noise are also different from arbitrary pairwise output probabilities. The paper identifies this distinction, but several named results and two kinds of certificate-complexity separation are compressed into one paragraph. The strongest comparison would name each primitive's input promise, output guarantee and invariant.

The final paragraph is overburdened. It is simultaneously a roadmap, a list of external inputs, a list of record-only results, a rule about every remaining record link and an advertisement for the exposition. I have no mathematical objection to those boundaries. I want them arranged around what the reader needs now, rather than making the reader memorise an inventory of document roles.

## §2: the Forrelation supplier

The displayed Φ and the one-sided promise are clear. Explicitly excluding large negative values is necessary, because the projection statistic only sees the square. The distinction between a promise solver and a domain recogniser survives the current revision, and the alternative interference test connects this presentation to the familiar Forrelation literature.

The quantum cost needs one extra explanatory bridge: each diagonal sign layer takes one phase query to the standard bit oracle; the Walsh transforms, uniform-state preparation and projection are independent of the input. The original preprint supplies that bridge. Without it the reader sees a matrix formula followed by a query claim, and must reconstruct their relation.

The integer numerator and exact circuit are appropriately stated as a supplier. I do not need the short paper to reproduce the butterfly and Boolean-adder construction. I do need a precise convention for S, because the next paragraph stores one bit per non-input gate and uses rS in the input length.

At the total-function definition, “independent input bits” is not the right phrase for unconstrained coordinates. A transcript is supplied by the input and may lie; it is not a deterministic output of the address block. Saying that directly is both simpler and more accurate.

The common-circuit paragraph is worth retaining. It ensures the upper and lower estimates concern the same total Boolean function. The exact input-length conversion is less central and interrupts the path to local tests. It would fit better as a remark after the mechanism.

The local-test paragraph is effective. It lists the tests, explains why gate consistency forces the true evaluation, and states the all-input dichotomy needed later. Its final sentence—circuit size enters through √K—is one of the best explanatory sentences in the paper. It gives a purpose to the circuit-size estimate instead of merely reporting it.

## §3 and Lemma 2: entering the quantum proof

The opening names the tournament as the new step, but the paper then spends a substantial proof sketch on standard amplification constants. Round six already intended to shorten this. The remaining M, 9/20 and 9/40 calculation is not wrong; it is weighted too heavily for this audience.

The contract itself is excellent: a deterministic cap on every branch, a failure bound only above a threshold, and an exact conditional successful state. The following sentence correctly says that the upper bound consumes the measured-label distribution. That should remain. The proof sketch could be shorter while keeping the two important ideas: randomising the Grover count handles unknown success probability, and every successful branch has the same successful-state direction.

The claim that unknown-success search “only” has an expected cost is too broad. The specific untruncated BHMT procedure has that guarantee. Timeouts are already part of standard search and minimum finding. The paper should identify the theorem being contrasted and the role of the known threshold, without making capping itself sound like an invention.

In the PDF the statement of Lemma 2 is split between pages 5 and 6. This is a small production issue but worth fixing: the budget and output law form one interface that readers will repeatedly consult.

## §3.1: comparing two columns

Sorting the indices and running the same circuit is a concrete explanation of complementarity. I do not have to assume that two separately programmed directional tests happen to add to one. The self-loss convention is also explicit, so the diagonal term in the drift calculation will vanish.

The pointer rule is correct but would be easier to check as two named observations followed by four cases. In prose, “disqualifies” and “victor” make the direction of the pointer slightly harder to track than necessary.

Retaining the decoded labels in orthogonal registers is essential. This is where the measured decoder and the coherent comparison acquire the same probabilities. It should not be removed in the name of simplifying formal details.

The dominant-candidate argument is satisfying: the winner's own address needs to decode correctly, but the rival's address can be arbitrary because no pointer can find a zero in an all-one column. The cost is then polylogarithmic. I would explicitly point out why ε need only be of order 1/T: the proof uses the actual comparison probabilities, rather than demanding that every coherent call simulate a perfect fixed-edge oracle.

## §3.2: ideal process

The statement of Proposition 3 has the right division between unconditional cap/list length and conditional containment of a dominant candidate. The paragraph connecting a surviving set to product weights is a successful previous repair. I do not regard that relationship as missing.

The algorithm itself is scattered across the proof, however. I find myself assembling a short procedure: keep measured pivots, construct a coherent trial from that history, amplify, measure a new label, append or stop, then return the current list. A short algorithm display would reduce that reconstruction work.

The drift identity is the best compact proof in the quantum section. Pairing i and ρ gives the half-weight estimate, and the immediate observation about cycles tells me exactly which hypotheses are absent. No rank argument and no transitivity are hidden.

The winner-survival argument then uses only its product weight and Markov's inequality. When the process stops at W=0, one small convention would make the argument completely literal: extend it by the absorbing zero state when speaking of W after T stages.

## §3.2: exact sampling

The sentence that the algorithm never computes the weights deserves more attention than it currently receives. It rules out a completely different, expensive implementation based on estimating every probability.

The coherent state and the calculation Pr(success and label i)=w_i/m make the implementation convincing. Fresh workspaces are the reason the factors multiply. This is conditional on the fixed input and already measured history; it is not an independence assertion about adaptive histories.

What I still want is one genuinely fractional finite example. The cross-document route currently leads to an example whose comparisons are deterministic. That illustrates the tensor-product flags but not why a weight replaces set membership. A small admissible probability matrix, clearly identified as an example of the abstract tournament proposition, would close that teaching gap without requiring a new theorem or a physical board realisation.

The stop-on-failure rule is visible and correct. The case p=0 must be allowed because the function is total and because, after the winner is listed, the remaining mass may be zero.

## §3.2: coupling and cost

The text correctly conditions on the whole past. That is a substantive improvement over a slogan about conditioning on no failures, which would bias histories if success probabilities differ between them. Once the winner is listed, later failures are harmless.

The stage cost and its sum are transparent, apart from reusing n for a history length after it denoted total input length. That symbol can be changed cheaply. The +1 should be identified as harmless initialization/padding rather than leave a reader to reconcile it with n workspaces.

At this point I believe the mathematical quantum mechanism as presented. I do not need a new formal audit to find the remaining explanatory issues.

## §3.3: verification and errors

Verification is the decisive all-input step, and the paper says why comparison dominance is insufficient. The short false-dominant example belongs here as well as in the appendix, because it explains why the tournament's output is a list and why finding a plausible winner is not already deciding F.

The search is for a failing local test. Its own reported failure means no violation detected, which leads to acceptance of the candidate. The mathematics is correct, but success/failure vocabulary reverses meaning across nested routines. Naming the violation result would make the paragraph easier to read.

The two final error cases are also correct in structure. On a zero-input, any accepted candidate is a false positive, so a union bound over the list is needed. On a one-input, accepting a nonwinner still returns the right Boolean answer. The only harmful events are omitting the true winner or failing its fresh decoding if verification reaches it. A short explanation of that asymmetry would pre-empt a common question about the missing T factor.

The final loose query count is harder to follow than the proposition-level accounting. I can derive the stated log^6 bound, but the paragraph switches from the sharper comparison cost to deliberately inflated logarithmic bounds. A small cost ledger and a link to the explicit count would be clearer. No attempt to improve the bound is needed.

## §4.1: the classical ingredient

The construction of μ from finite minimax is legitimate. It could be introduced after stating the useful depth-L hardness property, so that a reader first knows what object is needed.

The unnormalised-measure proof is compact and well motivated. A leaf factorises; a query changes one factor; the budget recurrence absorbs the two branches. The independent side information and coins are jointly independent of the inputs, not merely individually independent. The proof is a good example of completeness without unnecessary length.

The Drucker observation is now properly qualified: the global-budget result would suffice with a constant factor absorbed later. The parameter substitution can live in the record, but the acknowledgement should remain. I do not re-raise the old complaint that the proof wrongly rules out the global theorem.

## §§4.2–4.5: planting, discoveries and the predictor

The planted-pair picture is clear, and I can follow the two possible discrepancy locations. Blank cells are actual all-zero bit strings; querying a planted-cell bit is an event covering possible discrepancies, not necessarily an observation that the cell is occupied. A one-clause clarification would avoid inventing an occupancy bit.

The identity E[Z]/m is the correct way to expose the uniform independent column. The early-discovery estimate should explicitly concern a first discovery before the zero is known. Repeated queries cannot be counted as new discoveries. The proof's intention is clear, but the current conditional-uniformity sentence is slightly too broad.

The sentence that a query position already names an address explains the predictor construction exceptionally well. The subsequent simulator paragraph contains too many operations in one block. Splitting its definition from the event inclusion would make (12) easier to audit.

The distinction between a joint cap-and-success event and a conditional probability is essential and should remain. So should the fact that the free data are jointly independent of the entire address vector. The final discrepancy inequality then gives the classical bound cleanly.

The exact floor constants and sharper discovery count are useful record material. In the expert paper they dilute the end of the main mechanism. I would move them together with the threshold calculation rather than interleave refinements into the proof.

## §5: two different jobs for Forrelation

The first sentence says the main theorem only needs (5). That is the right starting point. The cited fixed-k lower bound and the additional uniform estimate then play different roles, but the section presents them as a continuous calculation.

The uniform estimate matters for explicit thresholds and the single growing-k family. The main fixed-exponent proof does not require that stronger uniform packaging. Label those roles so readers can choose the right depth.

The Gaussian-chain proof outline is caught between a citation and an explanation. It names a rounded Gaussian chain, multilinear derivatives, a stopped martingale and amplification without showing the inequality that connects them. Either a shorter route description or a clear statement of the existing distinguishing-gap comparison would serve the reader better.

The statement that the planted Gaussian law is not the promised minimax μ is excellent. This distinguishes two uses of distributions that could otherwise be conflated.

## §6: the exponent

The main argument is clean: choose α, then a fixed k with positive exponent gap, then take m large. The quantifier explanation earns its place. It excludes every smaller universal exponent without claiming an exact R=Ω(Q^4) family.

The growing-k remark is optional and depends on different uniform estimates. Its explicit ε formula is cumbersome relative to its purpose. The asymptotic conclusion and the choice of k(t) are useful; the constants can stay at the linked derivation. This is not a request to make the theorem stronger or to pretend the small permitted t values have a useful finite-size separation exponent.

The exposition's exercise about α_tot≥3.5 should be repaired to match this infimum argument. k=4 suffices to exclude every exponent strictly below 3.5, even though the same fixed-k estimates do not refute an inequality with exponent exactly 3.5.

## §7, disclosure and Appendix A

The formal section is substantially cleaner than the old receipt-heavy appendix. The result statements, model convention and common-circuit requirement are useful. The measured/reset implementation is now correctly distinguished from the separate retained-state result. That distinction should survive any further compression.

The section still contains several different levels of detail: axiom names, infimum nonemptiness, alternative upper-bound constants, exact quantified witnesses and lemma-interface comparisons. I would prioritise the mathematical statement and the genuinely different interfaces, leaving implementation inventories and alternative routes at the linked record. This is a presentation recommendation, not an allegation that the reported formal results are false.

The AI disclosure is short and proportionate.

Appendix A is a useful set of hypothesis counterexamples. The table fits on its page and contains no observed overflow. It needs row labels because the body refers to numbered rows. The false-dominant example should specify the zeros in the other columns so it is fully checkable on its own. The cap-zero examples are examples of general lemma hypotheses; readers should not mistake their tiny parameters for the final construction's regime.

## End-of-reading judgment

I would read the expert companion to the end. Its mathematical centre is now recoverable: inexpensive outward-pointer comparisons, fractional surviving weights, exact conditional sampling, a stopped coupling and final all-input verification. The next revision should spend its attention on hierarchy and specificity. Shorten familiar amplification constants, give the fractional mechanism a real example, repair local scope and reference errors, and protect the sentences that explain why an ingredient is needed.


---

# Supplement: sequential quantum reading of the record


## What was read and how these notes should be used

These are section-by-section notes for the record contribution to the quantum panel. They complement the lead reviewer’s full expert-companion reading log; they do not replace it. The current Markdown was the authority for quotations and locators. I read the record’s complete quantum §5, the complete quantum Forrelation subsection §3.3, all of §4’s construction/local-test material, and the model/exponent/formal-interface dependencies described below. I did not compile Lean, run Comparator, visually inspect the PDFs or reread the full classical lower-bound proof. No manuscript was changed.

The RR-S entries in feedback.json → sources_read record exact literature scope. “Read” there means the stated sections were read deliberately; it does not imply the entire paper when the scope says otherwise. “Skimmed” marks selected online passages or metadata checks. The latest AIK version check is deliberately narrower than the supplied-v2 reading.

## Opening, reading guide and §1

The opening gives the exponent arithmetic quickly, which is the right instinct for this panel. I understood the intended division of labor: the quantum cost is about a square root in the construction parameter, while the planted classical obstruction approaches a square. I slowed at the approximate equality between actual complexity measures. It is defensible as power counting, but the reader needs to know that the estimates being combined are one-sided bounds. The later quantified theorem and fixed-parameter argument resolve the issue correctly; the opening should not invite a stronger interpretation than those statements.

The guide now supplies a viable route around the long Gaussian proof. That previous-round repair should be acknowledged as successful. I still had to cross-check the companion’s headings because the record’s visible section numbers describe an older arrangement. This is not an absent-anchor problem: the link can open the correct file while the prose names the wrong section. In the record’s current ideal-process passage, the reverse companion pointer has the same defect.

The construction summary successfully explains why certificates point outwards and how one true column can disqualify every other column. My expectation at the end of §1 was a small set of algorithmic contracts: decode an address with a promise, compare two columns safely against a true winner, search among candidates, then check. Later sections do supply them, but source-model prose sometimes obscures their interfaces.

## §2.1–§2.6: models and small examples

Read all six subsections. The explicit input, promise and worst-case query conventions matter to this argument. In particular, an algorithm is a procedure on every input even when its correctness theorem only concerns promised inputs. This convention prevents an unpromised address block from creating an undefined subroutine later.

The distinction among a bit oracle, a controlled phase oracle and a bare phase oracle was worth reading closely. A global phase cannot reveal a complemented bit string to a circuit that has only the bare phase operation; adding control or an idle sector changes that comparison. The record’s concrete explanation is better than a blanket assertion that the models are interchangeable.

Deferred measurement was also treated with the right restraint. Matching final acceptance probabilities does not mean matching final states. I expected this point to be used again in the amplification/compiler discussion, and it is, though that later discussion should point back more cleanly. The exact small examples give a useful scale check. In Appendix A, the parity algorithm is repeated more fully than necessary; the new matrix/progress calculation there is the part worth repeating around a backlink.

I slowed when mathematical definitions were followed immediately by source-type names. The source lookup is useful, but the ordinary-reader contract should be readable before its representation is described. This concern recurs more strongly in §§3.3 and 5.4.

## §§3.1–§3.3: the quantum Forrelation ingredient

Read the complete promise, integer-numerator and quantum subsections. The normalized product has an immediately usable norm bound. The one-sided promise is easy to misremember from standard Forrelation discussions, so the statement that squaring removes the sign is important: large negative values are not false instances under this promise. The record correctly distinguishes the projection experiment with probability Phi squared from the interference experiment with probability (1+Phi)/2.

The supplied Bansal–Sinha introduction was then read through its bounded-error and total-function corollaries. It supplies the alternate interference circuit and makes the exponential dependence on k visible in its bounded-error query count. This is the right comparison for the record’s choice. I did not read the full Bansal–Sinha lower-bound proof as part of this subreview, and no new opinion about its detailed Gaussian argument is being inferred from the introduction.

The integer numerator makes the domain test exact, which later prevents an incorrect decoded address from being treated as a valid certificate. The quantum amplification uses a fixed number of repeated trials; the retained registers provide a unitary preparation and inverse. The main thing I wanted stated earlier was why those histories must remain. A bounded-error address bit is not a clean exact Boolean oracle. This becomes easier to understand once the exact local-test uncomputation in §4.6 is read.

The factor 2^(10k) is not a problem for fixed k, but it is the hidden cost that later competes with the improving classical exponent. The reader should be reminded of that distinction here, with a forward pointer to §7.3. The long implementation paragraph after the ordinary proof creates a second apparent conclusion and distracts from the compact contract the tournament will use.

## §4.1–§4.4: addressed transcripts and the finite board

Read these subsections in full. The transcript is a locally checkable witness for a deterministic circuit, and the selected cell supplies the domain and answer checks together. The addressed function becomes total because its value is defined on arbitrary bit strings, while correctness of a decoder remains a separate promise statement.

The four-column board is detailed enough to audit the local test definition. Its exact counts are useful: there is a true address with no failed tests, and incorrect addresses with one or two failed tests among 371. I wanted this data reused later when the verifier prepares a uniform test index. It gives concrete success probabilities for the failed-test search without inventing a second example. As written, the board pays a fairly large setup cost and then does not fully repay that cost on the quantum side.

The distinction between semantic winning and dominance by comparisons only became fully salient after reading the shorter accounts’ counterexample. The record should make that implication direction visible before the abstract tournament. Otherwise a reader can believe the list routine has already settled the total Boolean function.

## §§4.5–§4.8: access, unpromised rivals and antecedents

Read these subsections in full. The pointer test has small decision depth even though its possible queried positions have large total support; this is an essential model distinction and is already explicit. I did not re-raise the prior-round concern about confusing the two.

The exact-test oracle argument is strong. Conditioned on an index block, the output bit is certain. Copying that bit does not disturb the workspace, so the inverse uncomputes it. This is the clean counterpart to the noisy retained decoder and should be cross-referenced as such.

The winner-versus-rival argument is one of the best explanations in the record. An incoming pointer from an arbitrary rival label reads a one in the actual winner. The winner’s own correctly decoded cell then finds a zero in the rival. I checked that only the winner’s decoder enters the probability lower bound and that no independence assumption for the two decoded labels is smuggled in. The text gets this right. This mechanism is more informative than a generic phrase about tolerating noisy comparisons.

The antecedent discussion identifies relevant construction and certificate-search literature. The algorithmic comparison in §5 should say more precisely which predecessor uses ordered values, which uses a genuine orientation, and which uses candidate sets with approximate membership.

## §5 opening and §5.1: amplification

Read the entire section, including all endpoint, cap and retained-register paragraphs. The purpose paragraph explains the algorithm well and names the drift identity as central. The full proof of standard amplification then delays that identity. I wanted a route that first treats amplification as a contract and allows a specialist to come back for its proof.

The two-dimensional analysis is correct in the stated setting. At the quantifiers, however, I needed the success subspace to be specified as fixed and accessible. The proof freely uses its reflection. This is automatic for the source’s success flag and the concrete applications, but the generalized phrase every designated success subspace leaves the black-box access assumption implicit.

The zero-iteration half of each trial is an intelligible design choice once the large-success regime is reached: it protects against overshooting a state that already has substantial good mass. The text introduces it before giving that purpose. The exact averaging identity is a good recovery aid. I checked the relevant primary BBHT passage, including its timeout discussion, so I would avoid crediting the mere existence of a cap to the present work.

The cap is syntactic and holds even at zero success probability. This is the needed property, not merely an expectation bound. The arithmetic proving 138 is recoverable but over-prominent relative to the state argument. It would work better as separately labeled scalar accounting.

The whole-workspace good direction, routing to a designated subsystem, and history phases are handled carefully. The paragraph showing how to control only fixed reflections while applying the preparation and inverse unconditionally answers a substantive oracle question. The plus-state versus entangled-state example is excellent. It makes the weaker measured-law guarantee observably different from the stronger retained-state guarantee.

## §5.2: probabilistic tournament

Read all of §5.2, including the finite budgets and final restated law. This is the quantum contribution I would direct a specialist to first after the input construction. The abstract theorem states an all-input running cap separately from a conditional guarantee for a dominant row. I wanted one immediate sentence distinguishing that row property from semantic winning and explaining the role of the list.

The ideal process is explicitly an analysis device. That sentence avoids an illegal-algorithm interpretation in which the weights are somehow available to the quantum computer. The ordered-pair pairing in the drift proof is concise and exposes exactly the hypotheses used. The selected vertex gets zero weight, and the absorbing zero state is properly specified. The survival estimate for a dominant vertex then makes the Markov argument immediate.

The stage preparation is the critical implementation step. Fresh comparison registers for a fixed input and fixed history produce the product weight, and orthogonal index blocks produce the sum. I checked that the text is not assuming random input coordinates or independent unknown edge values. It is not. The complete retained workspace permits the inverse required by amplification.

The example is useful for drift and conditioning, but its loser cycle is deterministic. It therefore demonstrates the failure of sorting more directly than the absence of a bounded-error comparison predicate. I wanted one half-probability loser pair and one real-sampler continuation. That would illustrate the two genuinely delicate parts without making the example larger.

At the compiled finite-label law, the narrative became ambiguous. The ordinary state theorem implies the measured law, but the formal upper bound uses its own measure/reset procedure. The text introduces the compiled version and then says the law follows by measuring the state. I had to consult the current companion and Appendix G.7 to distinguish a specification implication from an implementation dependency.

The coupling paragraph then resolves the probabilistic concerns very well. Its auxiliary independent failure bit is a construction on a common probability space. The physical sampler is not being assumed to have a history-independent failure event. The argument stops paying for failures once the wanted candidate has been listed, as it must. Later failure can be certain and the list-inclusion guarantee can still hold. This is exactly the sort of detail a long record should supply.

The two query-cost presentations and multiple proof endings make it harder to tell when the ordinary proposition ends and the source-interface supplement begins. Logical reads, physical queries and the concrete comparison count should be mapped once. The reason for T squared should be attached to the state preparation: every stage rebuilds all prior comparisons, and the amplifier repeats that full preparation.

## §5.3: concrete comparison and verification

Read all of §5.3. The same unordered-pair circuit is used in both directions, which gives complementarity; self-comparison has the designated zero outcome. A four-case table could make the direction of the two pointer tests immediately inspectable. The sentence calling the result a classical mixture should name the output probability law instead. Retained coherent label blocks are not globally replaced by a mixture until measurement or discarding occurs.

The concrete comparison cost is more transparent when reduced to the already available O_k(ell log ell) expression, as in the companion, than when it immediately becomes an unspecified polylogarithm. The later enlarged count is valid but should be recognized as deliberately loose.

I checked the verifier’s quantifier over every address. It is exactly what is needed for arbitrary decoder output on a nonwinner. A search success means a failed local test was found and the candidate is rejected; a reported search failure means acceptance. This polarity changes the meaning of failure from the tournament’s failure symbol and deserves a small operational table.

The final two-case decision analysis is sound. On zero-inputs, every candidate is a nonwinner and the union bound applies. On one-inputs, an earlier acceptance is already the correct Boolean decision, even if it is not a valid witness. The proof needs the winner’s inclusion and fresh decoding when reached; it does not need to charge every possible earlier false acceptance. This should stay explicit.

## §5.4: input access and exact cap

Read the full compiler explanation and scalar accounting. The ordinary load–use–unload implementation explains why a logical input-dependent coordinate read can be charged to the standard bit oracle. The input-dependent indices are computed inside the circuit; nothing assumes random-access data is free. The two-query cost is a valid conservative accounting choice. No suggestion to optimize it is part of this review.

The abstract-read signature and continuation representation then interrupt the mathematical cost calculation. These are useful to a reader checking the formal model, but their natural destination is Appendix G with a nearby link. The main flow needs the input-query conversion, the total finite budget, and the statement that all maxima are fixed even when a run stops early.

The power six comes from enlarged scalar bounds, including replacing a logarithm by a reciprocal error. It should be introduced as a convenient uniform exponent rather than left for the reader to infer after the calculation. The explicit statement that gate count and workspace are not bounded is worth keeping: it tells an algorithms reader exactly what resource theorem has been proved.

## §5.5: continuation proof

Read the entire subsection. This is a useful alternate proof interface, not obviously a different mathematical evaluation algorithm. The earlier text already runs the tournament and then checks its list. What changes here is that the formal result directly establishes an accepting-bit continuation rather than separately returning the strongest list witness.

The cons notation reverses the apparent storage order from the earlier append description. The products and eventual acceptance event are insensitive to this convention, but a sentence should say so. Reusing Q as a temporary scalar lower bound is needlessly hard when Q already denotes quantum query complexity. The signed-bound case itself is carefully handled and should remain: the lower estimate can be negative, and the proof does not silently multiply inequalities as though it were a probability.

## §7 and Appendix A

Read the opening of §7 and all §§7.1–7.3. The fixed-parameter argument makes the one-sided inequalities rigorous and then excludes every smaller universal exponent. The growing-k estimate is now present; the old missing-recovery complaint is fixed. The parameter choice becomes understandable when the competing k and log(m)/k contributions appear. I would preview that balance before the long explicit constant calculation. The reference to choosing 508 because the companion uses it is revision history, not part of the mathematical reason for the inequality.

Read Appendix A.1–A.6 in full as part of checking the universal upper-bound side of the exponent discussion. The two-bit adversary witness is useful, particularly the matrix and per-query progress comparison. The exact parity algorithm repeats §2.6. The separate older-annex-transcription history should be kept away from the local mathematical witness. This subreview did not independently read every outside primary source cited in Appendix A and makes no claim to have reverified their editions or formal receipts.

## Appendix B.4–B.6 and G.7

Read the complete amplification/tournament/verification catalogue entries and all of G.7. The catalogue provides useful stable anchors, but plain-text tensor formulas and raw identifier headings are much less readable than the ordinary proof. This is avoidable even if the machine IDs remain unchanged. Some visible §5.2 labels now land in §5.5, which is another semantic navigation mismatch.

G.7 makes a distinction that should be clearer in the main text: the formal decision upper bound uses measured finite-label continuation machinery, while the ordinary stronger successful-state proof is not itself the same compiler result. This is why the main-text compiled-version paragraph needs careful phrasing. I did not recheck source receipts or infer a new formal guarantee from the appendix.

## Previous-round check and remaining limits

Read the previous quantum-panel verdict completely and the quantum-related record dispositions, with relevant statement-fidelity passages. I did not repeat the old mandatory-Forrelation-detour complaint, the old missing growing-k proof complaint, the removed BHMT theorem-number issue, or a claim that all evidence chronology still occupies the main proof. I instead identified places where the repairs remain locally uneven: semantic section labels, interface narration and source-code vocabulary.

The complete record’s classical §6 and the full §§3.6–3.16 Forrelation hardness proof were outside this subreview. Corresponding work belongs to the other panel reviewers. The companion quantum §§3.0–3.3 and relevant formal paragraph in §7 were read for consistency; the exposition quantum §4 was read in full, with its preceding Forrelation summary and adjacent context. No claim is made here that the entire exposition or companion was read by this one reviewer; the lead reviewer handles the required full expert-companion pass.

## Validation performed on this contribution

The 54 findings QS101–QS154 use the requested schema. Every quotation was checked programmatically for exact containment in the current reasoning_record.md and for a maximum of 25 whitespace-delimited words. This validates the quotation fields, not the mathematical claims. The mathematical assessment came from reading and the explicit reasoning described above. No Lean build, Comparator execution or PDF rendering was performed, and no manuscript file was modified.


---

# Supplement: exposition reading notes


These notes record the section-by-section reading issues from the current Markdown. They are a review of the supplied text, not a report of a human learner experiment. The complete exposition body and questions were read. PDF pages 1, 2, 4, 5, 6, 7, 8 and 10 were visually inspected after rasterizing the supplied PDF; the PDF text was also extracted to locate page breaks. No Lean compilation, Comparator run or manuscript rendering was performed.

## Introduction

The Boolean query model immediately establishes what is being compared. The worst-case cap over outcomes is a useful precision to keep. At the quantum oracle formula, however, the intended reader needs the roles of its registers and the distinction between an oracle invocation and a list of readable answers. The opening gives no small operation with which to interpret the formula.

The total-versus-partial distinction is clear in words. The universal exponent formula then arrives before the reader has a numerical separation in mind. The statement has the right quantifier order, but the contrast between one universal multiplicative constant and a family’s k-dependent constant deserves a sentence. At the theorem, the constants six and one four-hundredth look more central than they turn out to be.

The one-line m-times-L arithmetic gives the desired map. Its approximate-equality notation should be identified as a comparison of proved scales; the article is using inequalities, not establishing exact values for the two complexities. The certificate-in-a-column explanation is motivating but introduces certificate, cell, address, planting and direct product almost at once. A short definition of a certificate would reduce the load.

The historical paragraph is informative for a specialist. For a newcomer it is a sequence of names and fractions until the AND-OR paragraph explains an actual obstruction. The composition direction is not explicit enough for that calculation to be reconstructed. At the audience paragraph, the reader is now expected to know a sizeable list of specialist operations. This is a better disclosure than pretending the text is elementary, but it changes the task’s promised audience.

The map of two course routes is useful, as are the links to the companion and record. Visually, the introduction nearly fills two pages. The first matrix starts on page 3. A tighter entrance could let the concrete example supply some of the vocabulary now carried abstractly.

## §1. Three eight-bit inputs

The sign convention, explicit Walsh matrix, and three binary strings are enough to check the stated inner products. The geometric account correctly distinguishes agreement, opposite sign and orthogonality. The amplitude interpretation is where a learner first needs two missing bridges: phase kickback from the stated bit oracle, and the meaning of projection as a measurement.

The extra one-input with acceptance probability one quarter is a good repair. It prevents the displayed three special inputs from making the general decoder look deterministic. The phrase that a single run decides them should nevertheless be scoped to the promised inputs, since the third has no P-value.

The next paragraph correctly explains that an unpromised input can be accepted by this projection test. That is a property of this test, not a general impossibility of distinguishing the two signs quantumly. The current text mostly keeps that scope; do not reopen the old rejected request for a long alternative Forrelation-decoder discussion.

The census of all 256 inputs is exact but not used later. The L=0 limitation is the fact that matters for the board’s role. Keep that limitation and avoid using the census as a visual substitute for a hard distribution.

## §2. One column, then four

The general schema is complete, but it precedes the first usable column example. A reader has to remember an all-one string, r partial-function instances, 2^r cells, r transcripts and m−1 pointers before seeing one winning configuration. The four winning conditions are genuinely parallel and would be easier to reuse if numbered.

Figure 1 is legible at the supplied PDF size. It displays the one-way asymmetry of the winner well. Its short cell label should include certification of the domain as well as of the address values, because the domain bit is the next lesson.

The four-column setup successfully declares the r=2 simplification and says that it cannot illustrate the asymptotic hardness. Figure 2 makes the true cells and the impossible pointer into the all-one string clear. The prose immediately after it should separate why F=1 from why the other columns cannot win.

The transcript paragraph explains the fixed-circuit-versus-input-data distinction correctly. Shannon expansion and the count 180 are introduced too abruptly for the audience, while no actual gate consistency test is carried out. The worked pointer test is good and should be matched by one small gate test, as the prior plan already proposed.

The changed board with an unpromised first address input is excellent. It exhibits true gate transcripts and correct value bits with a failing domain bit. Question 1 lets the reader use the distinction independently. The single failing test at address 00 should return later at verification: it gives the concrete probability 1/K that motivates the verifier’s amplification.

## §3. The general partial function

The three-fact organization makes the supplier’s role clear. It should be preserved. The normalized Walsh tensor and the roles of the decoder, exact circuit and lower bound deserve more emphasis than the detailed constants.

The phase operation is now named, but it has already been used in Section 1. The requested error eta should be identified before the repetition formula. Correctness is only on the promise; the bounded query cap holds on all inputs. The last clause of the decoder paragraph currently carries both scopes and is easy to misread.

The exact-circuit paragraph compresses several standard constructions. The phrase boundary factors can be mistaken for promise-boundary cases instead of the two normalization vectors. The main reader needs to know that S is nearly linear because K then remains nearly linear. The integer comparisons and constant 200 can be an optional calculation or a record destination.

The classical hardness statement is appropriately imported. The input-length formula is an opportunity to say that m is not the input bit length and that the result compares query measures for one common family. Its large polynomial size should not turn into an unsolicited implementation discussion; a precise sentence about the parameter suffices.

## §4. The quantum algorithm

The failed nested-Grover approach gives the right local problem. Its wording should say quantum search for a failing test rather than literally reading all m bits in sqrt(m) queries. A procedural list of the actual algorithm would help distinguish it from the ideal weight process that follows.

The comparison rule is understandable after reconstructing two pointer reads. A full trace of one existing pair would help, especially where one column has no true address but its quantum decoder still returns a label. The retained-workspace paragraph supplies the right coherence idea, but needs the deferred-measurement bridge from the measured projection experiment.

The winner argument is clean: no rival pointer can find a zero in its string, and a correctly decoded winner points to a rival zero. The dominant nonwinner then establishes why comparison success cannot replace verification. The cycle establishes why minimum-finding order arguments do not apply. These examples do distinct jobs and should both stay.

Figure 3 is readable and has a clear arrow convention. Checking one cycle edge requires consulting both a changed pointer and an unchanged one; a small pair-outcome table could reduce the cross-reference work. The following HMW comparison correctly mentions arbitrary probability one half. The closer 2026 comparison-based routes deserve a short place here, since their set-to-weight relationship is the immediate novelty comparison.

The ideal process explicitly says the unknown probabilities and weights are never computed. That is essential. The initial table supplies a helpful expectation check. The pairwise cancellation in the general identity deserves one explicit pair calculation. The winner’s lower bound is pathwise until selection, while the total-weight bound is in expectation; naming that distinction makes the Markov step easier to reconstruct.

The coherent preparation correctly fixes the input, history and label before multiplying probabilities from fresh workspaces. The exact success-and-label formula is the construction’s central law. The empty-history base case should be stated so the first pivot does not seem to need a prior pivot.

The amplification paragraph is the main pacing failure. It supplies the standard trial recipe and constants in an unboxed block, despite the previous accepted move to the record. It also needs the p>0 normalization qualifier and the companion’s harmless global-phase qualification. Its contract belongs on the main route; the detailed recipe need not interrupt it.

The stage paragraph correctly distinguishes sampler success, measurement of the next pivot, and stopping on failure. The coupling can be explained with a shared pivot until failure, rather than left as a technique name. The statement that stopping cannot remove a listed winner is one of the most valuable lines in the section.

The worked stage is exact and useful but too special. It demonstrates only 0/1 weights, a uniform conditional output law, and the p=1/2 Grover plateau. Question 2 gives the p=1/4 single-survivor case. Neither demonstrates the fractional law. The record has a nearby unequal-weight example and carefully marks it as an abstract comparison example rather than a full board construction. Its loser comparisons are still deterministic; changing one loser pair to probabilities one half in both directions would expose the arbitrary-loser feature directly.

Verification has the right one-sided structure on a fixed decoded address. Recall the board’s single bad test here, and explain the coherent bit-query implementation of the local test. The error budget itself is clear after those objects are understood. The sentence saying decoder errors are already inside a_ij deserves promotion because it prevents the mistaken idea that every coherent comparison must be close to an exact orientation.

The count paragraph makes one false operational statement: the actual trial, iteration and stage counts are variable, while fixed caps govern them. This should be corrected locally. The symbol c is also reused from the Section 3 success probability. The final return to the square-root contribution is good closure.

## §5. The classical lower bound

The minimax distribution is stated as an accepted input, which suits a quantum-focused reading route. Define blank cells as all-zero bits. The updated caption correctly resets address inputs and cell contents instead of silently carrying the unpromised column from Figure 2 into the planted distribution.

The sentence saying no hard distribution exists at m=4 should be replaced by the precise L=0 limitation. A balanced distribution on the two promised examples meets the displayed zero-query hardness condition. It simply does not support the later positive-budget argument.

The first-difference coupling is clear, including the harmless overcount when a filled bit equals a blank bit. The erased-zero explanation should condition on the observed past, not an ambiguous completed transcript. The example separating marginal uniformity from independence is useful and now defines the empty branch.

The direct-product statement, its optional proof, and the examples distinguishing separate caps and joint independence are coherent. The different AND distributions are now named, resolving the previous issue. The simulator paragraph is the best explanation of the hidden address: the position of a queried bit itself names the guessed vector. The three budget sentence is worth keeping. The concluding one-third gap would benefit from the explicit 2/3 minus 1/3 acceptance calculation.

## §6. Exponent four

The ratio argument correctly fixes a target exponent, then one k, then lets m grow. The logarithms are handled in the correct direction because alpha is nonnegative. The small floor calculation can remain, but it should not distract from the positive power gap.

The phrase exactly the cube needs a leading-power qualification. The t≥2^k example is an effective illustration of why fixed-parameter asymptotics cannot automatically be diagonalized. A short link can distinguish the companion’s additional uniform estimates without moving that argument into the exposition.

Question 4’s stated goal and answer do not match: k=4 suffices for alpha_tot≥3.5, while k=5 rules out a universal endpoint bound of exponent 3.5. Clarify the task. The final mention of the constant 35^4 in an imported upper bound does not help this audience’s payoff.

## §7, questions, and close

The shortened formal section is much improved. Its most useful entry is the suggested check of the winning condition against the changed board. Put that before the run of links to query-model definitions. Keep the plain note that the formal family theorem leaves the logarithmic exponent unspecified; that is an actual mathematical difference the reader can understand.

The four answers are separate and clearly located. Their assessment coverage is weaker than their presence suggests: none makes the reader use a genuinely fractional pivot law. Retargeting the second task would test the central mechanism instead of a convenient special case. The short AI-origin statement is properly separated from the mathematics and does not need another round of procedural caveats.
