# Round-eight reading log

## Scope and navigation

These are three separately recorded, AI-emulated perspectives. They do not represent any named researcher, editor or institution. The sections follow the lead paper in reading order; follow-up source checks are identified rather than presented as unaided first reactions. The supporting record and literature were read at the scopes listed in `feedback.json`, not indiscriminately in full. The coordinator additionally read the complete attached historical conversation and current assignment.

The panel did not compile Lean, run Comparator or rerun formal receipts. A separate coordinating pass rendered the current 16-page expert PDF and performed the finite arithmetic checks reported at the end. The source manuscripts were not edited.

- Part I: quantum-algorithms referee.
- Part II: randomized lower-bound referee.
- Part III: handling editor.
- Part IV: coordinating visual, source-navigation and exact finite checks.

# Part I — Quantum-algorithms referee: sequential reading notes

This is a synthetic specialist perspective anchored in amplitude amplification, bounded-error search, minimum finding and Forrelation. It does not represent any named author's opinion. I read the current expert Markdown from title through the appendix and link definitions, then checked its bibliography and the relevant linked arguments. These notes describe that reading and the targeted checks it prompted. They are not a claim that every reaction was transcribed before consulting another source. My accompanying source inventory distinguishes full sections from samples. I did not render the PDF, compile Lean, execute Comparator, or recheck formal receipts; the panel's separate visual inspection must carry any claims about page appearance.

## Title, abstract and the first page

The title tells me the result immediately; the subtitle tells me this is a companion to OpenAI's separation. The abstract then identifies the construction and attributes the original result. I know within a paragraph that I am being asked to understand a reconstruction, not an independently claimed separation. The sentence about a true certificate defeating every rival is the first point where I become interested in the mechanism. It is a stronger opening than a general promise to give a transparent or accessible account.

I nevertheless read the abstract's “about square root of m” quantum cost as a leading-power description, not the literal bound. That interpretation relies on knowing the field's conventions. The paper later makes the dependence on k important, so the first summary should mark fixed k and suppressed logarithms. Likewise, “exact certificate tests” is accurate for the individual tests, while finding a failed test is bounded error. The short abstract could leave a reader thinking that successful list construction is followed by certain verification. These are repairs to the summary, not objections to the proof.

The query-oracle definition and all-branch cap are useful. In particular, the cap on off-promise inputs is not gratuitous formality: almost every losing column is allowed to have an off-promise address, and its comparison still has to terminate within budget. I would resist a register edit that automatically removed this qualification as defensive prose. The definition of the universal exponent also has a job. It makes clear that this is a statement over all Boolean functions with a uniform multiplicative constant, not merely an asymptotic relation within the displayed family.

Theorem 1 is readable at this point even though the construction is deferred. Its two scales, roughly square root of m and m to the power 2 minus 1/k, are enough to see where four will come from. The following paragraph credits the universal upper bound, makes the cubic conjecture and its refutation precise, and assigns the displayed constants to this reconstruction. The contribution paragraph then says that the original theorem, construction and analyses are OpenAI's. This is unusually clear provenance and should survive shortening. The sentence about one circuit serving both bounds is also worth keeping: a transcript-defined total function really depends on the circuit witness.

## Section 1.1: history and the cubic barrier

The AND–OR calculation is the most informative part of the historical material. It gives a reason that a familiar totalization recipe stalls at the cube instead of just listing milestones. I can reconstruct how the outer partial hardness and the inner certificate cost compete. That prepares me to ask how the present construction avoids spending m queries quantumly.

The next paragraph restarts the chronology from Grover and traverses the same exponents again. The reader has just seen the 5/2, 8/3 and near-cubic progression with an explanation. A second progression without the explanation slows the approach to the construction. I would retain one chronology and the calculation. The issue is not that history is unimportant; it is that the reader gets it twice before meeting the mechanism the introduction promised.

## Section 1.2: construction overview and figures

I can describe the construction after the first paragraph: columns have ordinary bit strings, hard partial instances determining an address, and an array of alleged certificates. A winner is all ones and has a selected certificate pointing to zeros everywhere else. This is enough conceptual structure before the exact circuit appears. The numerical address length 20 log m is early. The constant will pay for a union bound later; here it acts as an unmotivated item to remember.

The first figure caption describes the correct asymmetry: pointers from a winner hit zeros and no pointer into its all-one string can hit a zero. I checked that meaning in the Markdown caption and accompanying construction. I did not inspect the image at printed scale, so I make no claim about its label sizes or visual hierarchy. The panel's render review owns that question.

The failed nested Grover strategy is excellent motivation. A quantum researcher naturally tries search over candidates with an inner certificate verifier. Giving the resulting square-root-of-m times square-root-of-K cost immediately explains why the paper needs a new candidate-generation step. This paragraph earns more space than another list of related search algorithms would. Its last sentence should describe the weights as products accumulated across pivot history. Individual comparison probabilities alone are not the weights used by the tournament.

The classical overview is also useful from this side of the panel. It tells me why the many columns are necessary: the planted column is independently hidden, and a cell address reveals a vector of hard answers. I can already distinguish the cost of finding some zero from finding the zero selected for erasure. The formula for the exponent then closes the overview instead of leaving the purpose of the construction implicit.

## Section 1.3: antecedents and the search menu

The pointer discussion helps separate this construction from back-pointer variants. I understand that the relevant pointers are stored in the hidden selected cell, with one field for each rival, and that a comparison reads only its own rival-directed field. This is a real access-model distinction, not just a change in diagram.

The Forrelation paragraph also answers a construction question: the explicit Walsh form is chosen because an exact reasonably small circuit is needed, not because every optimal partial separation is interchangeable. I would keep that reason close to the source choice.

The comparison-search paragraph is where I slow down. It asks me to compare a surviving set, fixed graph directions, minimum finding, king finding, fixed candidate claims and bounded-error validity search before I have seen the circuit that this construction offers. I recognize all the categories, but I cannot yet check the interfaces. The surviving-set antecedent belongs here in brief; the detailed distinctions would be more useful after §3.1. The AIK comparison itself is sensible: a fixed direction is approximated there, whereas here the exact outcome probabilities enter the analysis. The phrase “approximate a fixed graph” can be made more precise without expanding it substantially.

## Section 2: the partial promise and the total Boolean input

The sign convention, normalization and one-sided promise are clean. Stating that large negative Phi is off-promise prevents the common but consequential replacement of the promise by an absolute-value test. This qualification is needed later by the domain-bit discussion and Appendix A.1. It is not a stylistic blemish.

Property (ii) is an actual algorithm description: prepare the uniform state, apply the matrices from right to left, and project back. That is more useful than simply citing a constant-query Forrelation algorithm. I can see both why the success probability is Phi squared and why the decoder may behave arbitrarily off-promise. The repetition claim is enough for fixed k. When the paper later quotes an exponential dependence on k, though, I need to know that this is a rare-event multiplicative-tail estimate, using order delta to the minus two repetitions, rather than an additive-gap estimate with another squaring. The record supplies this. The short paper should indicate the source of the dependence where it begins to matter.

The local attribution is slightly uneven. The alternative interference test is explicitly credited to Aaronson–Ambainis, while their earlier projection circuit is also the route just described. The surrounding general credit is not false. A more local source locator would avoid implying that this version of the experiment first appeared in the later preprint.

For property (iii), I understand the integer numerator and the need to preserve its sign. The nearly linear circuit size is crucial because the final verification pays its square root. The compressed justification could say where its logarithmic factors come from: fast-transform arithmetic and bit width. I do not need a gate-level construction in this companion. The supplied record's detailed circuit construction is the right destination for that.

The column definition makes the alleged transcripts free input coordinates. This establishes totality honestly; the certificates are neither trusted nor supplied by an oracle. The exact row encoding of an ell-bit pointer is a tiny omission. A fixed bijection to rows in [m] would settle it once. The same-circuit paragraph and input-length estimate are useful because they close two possible gaps in the interpretation of the family.

The local-test paragraph contains the key all-address assertion: a nonwinner has a failed test at every address. This is the fact the later verifier needs even when the decoded label is arbitrary. Its proof by topological induction is standard and adequate. I would insert the actual gate-test operation before that induction: read the claimed gate output and at most two predecessor values, using genuine input bits for input predecessors and alleged outputs for internal predecessors. That one operation explains the three-query claim more directly than a longer abstract explanation would. The extra output tests are correctly distinguished from consistency of the output gates; that previous-round repair should not be removed.

## Section 3 and Lemma 2: a correct tool in an awkward position

The section promises candidate generation and verification, then immediately presents an amplifier before defining the comparator. Its contract is important, but most of its technique is standard for this reader. I would first show what random comparison is available, then state the exact amplifier interface at the point where its law-preservation property is needed. The previous revision already removed numerical trial arithmetic; I am not asking it to remove arithmetic that is no longer present. The remaining issue is reader order.

The designated accessible flag is correct and necessary. A fixed query-free reflection means a test of the flag the preparation has written, not a success predicate that is independent of the oracle input before preparation. That distinction could be stated more plainly. The central contract should also say which original law is preserved: the original law conditional on the preparation succeeding. “Its original law” can grammatically mean the unconditional output distribution. The proof and section introduction make the intended reading clear, so I regard this as a reusable lemma's ambiguity, not a mathematical counterexample.

The direct-measurement branch handles high initial success probability. This is not a peripheral endpoint because the first tournament stage has success probability one. The random-length branch handles smaller success probability. A constant mixing probability should be named; the argument is not true for every mixture that happens to include both branches with arbitrarily tiny weights. Similarly, the normalized good/bad decomposition should exclude p equal to one and handle that endpoint separately in a few words. The record does so. These small repairs make the abbreviated proof genuinely self-contained without restoring the long arithmetic.

I checked the historical distinction with QSearch. The adjective “untruncated” is essential: the cited expected-cost routine is not being used as the all-branch procedure, and the paper does not claim that bounded timeouts are a new invention. BBHT already discusses the unknown-number and zero-solution settings. The exact lemma locator should identify the arXiv version inspected, because the bibliography currently identifies only the journal edition. Publisher and arXiv metadata disagree by one final page; that is a metadata discrepancy to resolve, not evidence that the authors invented their range.

## Section 3.1: executing the comparison

Once the comparator is defined, its economy becomes apparent. It decodes two addresses and reads two rival-directed pointer fields. It does not inspect either complete transcript. I would name that saving because it is precisely what the nested-search obstruction demanded.

I paused at the ordered bit pair. The bit found by the pointer from i lies in X_j, and conversely. Writing the candidate pair as (i,j) and then the observed bits in source-pointer order can initially reverse which column is disqualified. Naming the target strings fixes this without new notation.

Sorting the pair and running one fixed circuit is a mathematical safeguard worth its words. Complementarity is then an exact equality between the two outcomes of one experiment; it is not a claim that independently designed noisy procedures happen to add to one. Retaining the decoded labels as controls also matters: it explains why different decoded addresses contribute orthogonal probability blocks even though the full state is coherent. Calling this state a classical mixture would be wrong, and the current text does not do that.

The winner argument is especially clear. A rival at any address cannot point to a zero in an all-one column. Only the winner's address must decode correctly to disqualify its rival. Thus the comparison guarantee does not need both decoders to succeed, and loser–loser probabilities can remain arbitrary. This is the interface the whole paper should foreground.

## Section 3.2: weights, sampling and stopping

Proposition 3 has the right query and probability contract. In isolation, it would benefit from explicitly saying that the inverse comparison has the same query cap; reversibility in this model supplies that fact, but amplification spends it repeatedly. The product weights should have their finite pivot-history range bound immediately, rather than an ellipsis and an unindexed product.

The ideal process is persuasive. Pairwise complementarity pairs the cross terms, while self-loss removes diagonal terms. The resulting exact drift is stronger than the inequality needed. The diagonal also means a chosen pivot cannot be selected again, an inexpensive useful invariant omitted from the short explanation. The proof's central comparison is between rapidly falling expected total mass and the at-least-half mass still carried by an unselected dominant candidate. I would make those two invariants more visible among the subsequent Markov and stopping details.

The algorithm does not compute the weights, and the paper says so at exactly the right place. The tensor product gives products for a fixed label; orthogonal candidate labels give a sum across labels. The displayed preparation and the two short explanatory sentences make the exact law believable without assuming input independence. This is one of the companion's strongest passages.

The fractional example is correct. After pivot 2 the total weight is 23/12, so the preparation succeeds with probability 23/48 and normalizes to the displayed 12/23, 8/23 and 3/23 masses. One more pivot would reveal the operation that one pivot does not: multiplication into existing weights. If pivot 4 follows, the weights become (1,0,4/15,0), with conditional law (15/19,0,4/19,0). This is an optional extension of the existing illustration, not a proposal for a new result. The explicit boundary between this abstract matrix and a realized four-column Boolean input is important and should remain.

The coupling is sound when read conditionally on the entire history. At each relevant history the real transition has a history-dependent failure mass and, on success, exactly the ideal label law. No conditioning on all stages succeeding is needed. Once the winner is in the list, subsequent failure cannot remove it. I found no residual version of the previous-round global-conditioning problem. A brief transition factorization would explain the valid coupling more directly than another general warning about dependence.

Only the measured pivot history should persist between stages; fresh comparison workspaces are built against that history again. The text gives fresh workspaces within the stage, but could identify this persistent/fresh split explicitly. It also explains the T-squared cost: later stages redo more comparisons. I would name this operational source of the sum rather than leave it in “summing over n”.

The full-proof link is a concrete navigation defect. Its anchor starts at the real amplified tournament, after the ideal process, drift and exact sampling argument. A reader checking the whole proposition lands halfway through the promised proof. The record has suitable earlier anchors, so this needs a target repair, not additional mathematics.

## Section 3.3: total verification and cost

The dominance counterexample motivates verification before the verifier is described. Decoding afresh and measuring the address is also useful: it makes the later local-test search an experiment at a classical address, and the nonwinner guarantee holds at every such address. The search wording “no defect found” correctly avoids saying that absence of a reported defect proves validity.

The zero-input union bound works for an adaptive, input-dependent list because every nonwinner's verification error is bounded after any previous selection history. I supplied that conditional reasoning; the text should make it as explicit for false candidates as it already does for the true winner. On a one-input, accepting an earlier false candidate still produces the right Boolean answer. The printed observation says this clearly and prevents confusing decision correctness with guaranteed winner identification.

The ordinary bit-oracle implementation is enough, but arrives after several coherent pointer uses. Moving its short explanation to the first such use would remove a temporary question about query cost. The common log-to-the-sixth bound is deliberately loose and the paper labels it that way; I have no objection to that choice for an exponent theorem.

The link claiming the exponential envelope for C_k has a distinct destination problem. Record §5.4 gives its explicit sum of constants; the comparison of that sum with a constant below 2^53 times k times 2^(10k) is in §7.3. Both statements are present, so this is a broken explanation route, not an unsupported constant.

## Sections 4–4.5: reading the lower bound as a quantum specialist

I read the entire lower-bound section to understand what the quantum construction must preserve. I can follow the proof's division into an independent hidden erased zero and a hidden selected cell. The finite-minimax input, separate caps, dummy/planted coupling and capped simulator make distinct contributions. The direct-product proof exposes why the product law permits the unchanged factors to leave the branch sum; that is good local explanation.

I do not claim an independent specialist audit of the full linked classical record. The randomized referee owns that deeper check. From the quantum side, the critical compatibility is clear: cheap comparison may use any off-promise rival label, while the lower-bound distribution uses genuinely promised independent address inputs. These are different uses of the same total construction, not contradictory assumptions. The fixed circuit serves both. The selected-cell event is counted even if a particular bit does not change under planting, which safely enlarges the first-difference event.

The planted figure's caption carefully identifies a small structural illustration rather than a finite instance satisfying the eventual hardness threshold. Again, I checked its semantic description, not printed rendering. The quantum reader learns why the m factor survives without needing a second visual algorithm for the classical proof.

## Section 5: an optional analytic argument before the main conclusion

I understand immediately that the cited fixed-k Forrelation theorem suffices for the main exponent result. The additional uniform estimate then has two separate uses: an explicit sufficient threshold and a growing-k family. This scoping is good. Its proof outline introduces a different collection of tools—Gaussian correlation, algebraic truncation, stopped martingales and a promise-to-distribution bridge—before the fixed-k conclusion has been closed.

For this reader, the analytic subsection is overweight in that position. I would finish the short fixed-k deduction first or make the optional route unmistakable. This is a structural preference, not a request to suppress the reconstructed estimate or its credit. The passage comparing polynomial k dependence and logarithmic losses is correctly qualified. The O(k) classical error reduction here should not be confused with the exponentially small quantum decoder success gap; they are different experiments with different roles.

The final distinction between the analytic law with off-promise mass and the minimax law supported on the promise is useful. It prevents importing a distributional property from the analytic proof into the planting argument where it has not been asserted.

## Section 6: fixed and growing parameters

The fixed-k quantifier order is explicit and sound: select the forbidden exponent, choose one sufficiently large fixed k, then let m grow beyond that k's threshold. The factor involving C_k is constant in that limit. This closes the stated exponent theorem cleanly, and the 1+Q convention agrees with the original definition.

The single growing family is correctly distinguished from this argument. Its schedule k equal to the floor of the square root of t/20 is precise but looks guessed in the short paper. The record explains the balance between the 40k decoder loss in a fourth power and the ell/k classical loss. A sentence giving that reason would make the schedule memorable without importing its arithmetic. The warning that the result is asymptotic and does not establish an Omega(Q^4) family is also worth retaining.

## Section 7, AI disclosure and references

The formal section tells me what claims have corresponding statements, what the compared family theorem supplies and where the explicit constants are supplied separately. I have not rerun those checks. I assess the presentation only. It is useful that an existential logarithmic exponent in one formal statement is not silently identified with the displayed exponent six.

The measured-label law is the formal interface relevant to the quantum proof printed here. That relationship should lead the last paragraph. The retained-state variant and the finite-seed direct-product bridge are accurate distinctions as presented, but receive nearly equal weight although they serve different reader questions. A tighter main paragraph plus clearly labelled record destinations would better finish a specialist paper. It is not necessary to turn the closing section into a taxonomy of every neighboring interface.

The AI disclosure repeats the correct separation of original theorem ownership from reconstruction. I read the bibliography source and selectively checked the quantum references. I did not inspect every cited paper. The BBHT locator needs version precision; the page-range discrepancy has an identifiable publisher/arXiv origin. No larger attribution reversal emerged from the quantum sources I read.

## Appendix A

A.1 is a genuinely useful small example: squaring the amplitude loses sign, so the decoder cannot act as the exact domain circuit. A.2 distinguishes lack of a total order from lack of a bounded-error fixed orientation; these are two different reasons familiar search interfaces cannot be substituted wholesale. A.3 shows why winning comparisons do not certify a column. Those three examples test specific tempting quantum shortcuts and should be kept.

The remaining examples protect independence, branchwise caps, joint side information, joint compliance and parameter uniformity. I read them in full. They are concrete rather than ceremonial warnings, but eight ungrouped cautions feel like the history of several review rounds accumulated in one appendix. Grouping by the inference each protects would make it easier to find the one needed while reading a proof. The solution is not to delete necessary hypotheses from the main text or to replace examples with general cautionary prose.

## Overall reading outcome

I would read this companion to the end. Its winner-only comparison, exact fractional sampler and separate total verifier are understandable and, at the level inspected, mathematically convincing. The previous quantum repairs are present. I found no new blocker to the headline quantum argument. The next improvement is to spend the reader's attention on the interface that is unusual: exact probabilities between arbitrary losers, the product law they induce, and the stopped history-conditioned implementation. The standard amplifier can support that story more economically, and the proof links must land at the arguments their labels promise. Those changes would improve the paper more than further defensive prose or another formal audit.


---

# Part II — Randomized lower-bound referee: sequential reading record

## Scope of this reading

This is a separate, hypothetical lower-bound researcher’s perspective, anchored in cheat-sheet constructions, pointer functions, Forrelation lower bounds and direct products. It is an AI review, not a report of any named researcher’s reaction. I read the current expert Markdown in order, including the title, abstract, captions, appendices, bibliography source and links. I then followed the classical route into the reasoning record and compared the indicated primary-source passages. The follow-up checks below are distinguished from the initial reading. I did not render the PDFs, run Lean, run Comparator or rerun the packet’s verification receipts. Those are separate activities from this reading.

The main mathematical conclusion of this reading is positive: I found no counterexample or invalid inference in the current planted lower-bound proof. The most consequential remaining problems concern the shape of the article: the generic reduction is less explicit than its proof deserves; the optional analytic estimate delays the main conclusion; and the provenance of that quantitative refinement needs the same care already given to the separation theorem. Many of the round-seven warnings are now correctly handled. I preserve them as strengths rather than re-reporting them as missing.

## Title and abstract

The title tells me the endpoint immediately, and the subtitle establishes that this is a companion. The abstract’s second sentence attributes the separation to OpenAI. I therefore do not begin with the mistaken expectation that the author is claiming priority for the fourth-power separation.

The classical mechanism is compressed successfully: hidden certificate, cost equal to columns times address hardness, cheap quantum address decoding. The phrase saying a classical algorithm is unlikely to find the planted certificate is especially good. It permits a lucky address guess and does not confuse successful location with prior computation of the address. This is the right statement to retain from the previous review.

I slow down at the informal square-root-m cost. I have not yet seen the fixed Forrelation parameter or the suppressed logarithms. I understand the intended scale after reading the theorem, so this is a small local qualification rather than a mathematical problem. More substantially, the abstract describes the theorem and its mechanism but gives only the broad word reconstruction for the companion’s added value. For a specialist who has already seen the preprint, I would like to know which difficult verification this account makes easier.

## Section 1: theorem, models and contribution

The query model is stated early enough to prevent runtime interpretations. The all-branch cap includes off-promise inputs, which will matter for comparison and amplification. The definition of the optimal exponent is precise: the constant is uniform over functions and dimensions, and the added one accommodates constants. I can read Theorem 1 before knowing the entire construction because it points to §2 and treats the family as an object to be defined.

The distinction between the universal upper bound and the exhibited family is sound. Taking k equal to three beats the cubic exponent, while larger fixed choices approach four. I also see that the coefficient and logarithmic power belong to this reconstruction rather than being copied verbatim from the source theorem.

The contribution paragraph is candid about ownership of the theorem, construction and analyses. Its list of two difficult reductions is a useful selection principle. What it still lacks is a sharper statement of the explanatory service: exact law preservation on the quantum side, and an unconditional, fixed-time predictor event on the classical side. Those are things a referee can actually try to recover from the paper. A declaration that the reductions fit together is less operational.

## Section 1.1: earlier separations

The historical attribution to Ben-David before the general cheat-sheet framework is now present. The quantitative AND–OR comparison is more informative than a chronology of exponents by itself. It shows why a partial-function gap does not simply become a total-function gap at no cost: certifying the outer promise creates a verification expense.

That makes the phrase about turning any partial separation into a total one unfortunate. The preceding and following mathematics are more careful than that sentence. A generic totalizing construction and a theorem preserving a useful separation are different claims. The latter depends on the available certificates and their verification cost. This is a scope qualification, not a request for another historical survey.

I can reconstruct the displayed predecessor costs. The text specializes m prime to n and obtains the expected exponent. At the statement that this recipe stops at the cube, I pause: the chosen balance has not yet been identified as the exponent-optimal balance for these estimates. The two cases on either side are easy, but this is the exact inference the comparison is meant to teach. A sentence explaining the balance would earn more than a second list of achieved powers.

The next paragraph supplies the OR benchmark and then repeats the 5/2, 8/3, 3 and 4 progression. I would merge the repeated chronology while retaining the predecessor cost comparison. The distinction between Rorrelation and explicit Walsh–Hadamard Forrelation is good and later becomes essential to the exact circuit.

### Literature check after the first pass

I read ABK’s §3.1 motivation and §3.2 construction/lower bound closely. Its exposition first makes the promise-certification obstacle explicit, then introduces composition and the addressed array. That causal ordering is useful here. I also read the relevant introductory technique discussion in the pointer-functions paper: the highlighted-zero back pointers and the exponential-alphabet objection to putting all direct pointers into one symbol support the companion’s revised account. I did not treat either paper as a source of the new separation.

## Section 1.2: construction overview

The overview gives me the objects I will need: a column string, several partial-function inputs, a selected address and a cell that disqualifies rivals. I can see why there is at most one real winner before meeting all the circuit details.

The two classical hiding mechanisms are now distinguished correctly. Finding some zero is easy compared with finding the zero in an independently selected column. The Z/m explanation is excellent because it displays where one factor of m enters rather than appealing to an unspecified search principle.

The certificate-location sentence is the classical core: a query position names a whole vector of proposed answers before any cell content is read. This is much better than saying the algorithm must learn the address. I expect §4 to make that sentence into an actual predictor, and it does.

I would qualify the hardness-scale interface here. The later generic reduction needs L between one and m, not merely below R(P). The intended Forrelation choice satisfies the condition. Including that range here would keep the overview from advertising a broader reduction than the stated proof supports. Likewise, the role of logarithmically many independent address instances could be said in one sentence: their success bound must survive a union over query slots.

## Section 1.3: antecedents of the new construction

This section does real explanatory work when it identifies one cell array per column and the direction of the pointers. The direct-pointer comparison is particularly good. It avoids claiming that outward pointers are a new invention and instead explains why indexed bit-field access does not pay for one gigantic alphabet symbol at every comparison.

The recent candidate-comparison literature occupies more space than I personally need as a classical referee, but it is relevant to the quantum reader. I would not delete the distinctions merely because I skip over them. The costs and input guarantees, not the number of references, determine whether this comparison is useful.

The final organization paragraph is accurate, though it forecasts the analytic Forrelation section as if that section were equally necessary to the main theorem. This foreshadows the main allocation problem later: the fixed-k separation needs a cited hardness input, while the uniform estimate supports optional additional conclusions.

## Section 2: promise, circuit, total input and tests

The one-sided promise is unambiguous, including the exclusion of large negative Forrelation values. The three required properties separate randomized hardness, quantum evaluation and exact domain/value recognition. This is the correct interface for the totalization.

I read the integer-circuit explanation as a cited supplier with a reconstruction route, not as a complete proof in the companion. That is acceptable because the paper has already named its proof scope. The important fact for my later argument is correctness of the circuit, not its size.

The total-function definition makes a valuable clarification: transcripts are separate, freely assignable input bits and may be false. There is no probabilistic independence assertion about arbitrary inputs. Independence will be imposed only in the hard law. This prevents a misleading idea that the stored transcript is automatically tied to the address inputs.

The same-circuit paragraph is necessary. It identifies one family on which both estimates hold, and it says why the lower bound does not depend on choosing the efficient circuit. I would make the latter fact prominent again at the beginning of the generic reduction, where it becomes a reusable contract.

The total input-length calculation is correct at the explanatory level needed here, but the exact exponent 22 is less important than the fact that m is a construction parameter rather than the full bit length. I would put the detailed arithmetic in a subordinate place if space is needed for a central simulator example.

The local tests are intelligible. Gate consistency and output constraints do different jobs, and the induction in topological order explains why a falsified transcript cannot defeat all tests. The pointer encoding has a minor presentational gap: an ell-bit word must name one of m rows, and the later blank word is a legitimate row encoding rather than a null pointer. A fixed encoding convention would remove that hesitation.

## Section 3: quantum proof, read from the classical side

I did not treat my reading of this section as an independent quantum circuit audit. I followed its proof logic because the lower-bound comparison must concern the same total function. The requirement is clear: a real winner is nearly dominant, while comparisons among losers may be arbitrary probabilities.

Lemma 2 says more than a search-cost bound: successful output labels retain their original conditional law, and the query cap is branchwise even below the success threshold. That is exactly the property the product-weight sampler later consumes. The near-unit success case is handled explicitly, so I do not re-raise the earlier amplification objection.

The half-drift calculation pairs the complementary comparison probabilities and leaves the sum of squared weights on the diagonal. I can follow why a still-unselected winner retains positive weight and why a small expected total weight bounds the miss event. The fresh-workspace construction then samples the stated weights without computing them. The fractional example makes the difference from uniform sampling over surviving labels concrete.

Final verification is logically separate from dominance. The paper gives an actual false-dominance example rather than suggesting dominance itself decides the total function. From my perspective, this section supplies the needed all-input upper bound and preserves the construction’s totality. I leave detailed quantum implementation and source-comparison judgments to the quantum referee.

## Section 4 opening: the generic reduction and hard law

This is where I want a clean theorem to reuse. The opening says the argument works for abstract P and C and displays the mL lower bound. The record has a fully articulated generic statement. The companion should expose that same statement with its finite-domain and circuit-realization hypotheses, together with the inherited m and r conventions. At present it is easy to read the phrase with these choices as still restricting P to its previous km-bit Forrelation presentation.

The minimax paragraph is correct. A law is chosen to defeat every depth-L tree, rather than one law per tree, and strictness comes from attainment in a finite game. I do not need the whole convex-separation proof in the short paper.

One detail worth making explicit is that the resulting address need not be uniform. Independent copies of a hard distribution do not make their answers unbiased. The proof needs a bound on prediction by every shallow tree, not a statement about uniform addresses in a large array.

## Section 4.1: direct product

The unnormalised proof is a good choice. Its recursion has a clear budget interpretation, and at a query only one measure and one allowance change. The common factors can be pulled outside the sum; that is the mathematical reason adaptive interleaving does not defeat tensorization.

Compared with the preprint’s conditional-posterior route, this proof avoids null-history conventions and is short enough to be worth retaining. Its audience needs no general tutorial on direct products. What would help is a sentence previewing the actual vector-output predictor before this lemma: the output will be the address encoded in a proposed query coordinate. That tells me why this is the relevant direct-product target.

The attribution to Shaltiel is appropriately qualified by target and input-law conventions, while Drucker supplies the directly relevant product formulation. The alternative use of Drucker’s global-budget theorem is correct: the simulator has total cap L, and the extra factor two fits the slack. Source parameters T and alpha should be identified as source notation, since both letters have other meanings in this companion.

### Record check

I read the complete record §6.1, including the conditional-value proof, the joint-event corollary and the unnormalised proof. The two proof routes agree through the normalization identity. A reader following the short proof should be directed to the weighted proof, because the record’s initial V notation denotes a normalized continuation probability whereas the short proof’s V is an unnormalised value. This is a navigation issue, not a mathematical disagreement.

## Sections 4.2–4.3: planting and the erased zero

The paired inputs are literal coupled inputs: all A strings are unchanged, I is independent of the entire dummy data, and only one X bit and one cell may differ. The dummy run controls the right side of the first-difference inequality. Counting every visit to the cell is a safe overcount even when the particular bit read stays zero.

The zero argument is correct. I fixes a target independently after the dummy data have been chosen, so the selection identity is exactly E Z divided by m. The early/late decomposition then bounds E Z. Repeated queries do not create new discoveries, and using the total budget to count late columns is safe.

I did pause over the sentence asserting residual uniformity conditional on the entire past. The record gives its reason: a positive-probability transcript prefix constrains the independent zero positions separately, the address strings are independent of them, and the blank cells add no information. A short clause or a direct link to that argument would make the assertion easier to verify in the companion.

The phrase as the preprint does contributes little to this calculation. Local mathematical attribution can be carried by a citation without narrating the reconstruction process.

## Section 4.4: the planted cell

This is the strongest part of the current classical account. The original algorithm has a total budget G. A target column is heavy according to its complete original run. The simulator has a different, stronger restriction: at most L queries in total to the target tuple. That implies the separate allowance L per instance required by the direct-product lemma. The text now keeps these relationships correct.

I track two clocks while reading: the original query slot tau and the target-query counter. Free replies to outside queries still advance the original simulation. Naming that convention would remove a small possible ambiguity.

Giving the simulator all outside dummy data is safe. This includes J_i, which may initially feel surprising because zero positions were just being hidden. The task has changed: the simulator predicts address answers, and zero positions are independent of the target address tuple. The original tree is not suddenly given that free data; it receives ordinary replies from the simulation. The record’s more explicit enumeration makes this clear.

The predictor’s fixed default vector is not an irrelevant implementation detail. It supplies an output on every branch and can accidentally be right. Thus the light true-cell event is contained in predictor success, not equal to it. This is a good place for a compact execution of the already available toy. The companion has many counterexamples to invalid shortcuts but sends the positive execution of its advertised classical reduction to the record.

The joint event is correctly left inside the probability. The time union and column average are explicit, and the cancellation of m is visible. None of these should be sacrificed during a style pass. I found no conditional-on-lightness error in the current text.

The worked-example link has a concrete mismatch: its text promises a trace, but CL-simulator lands at the general definition. CL-simulator-example is the existing anchor for the trace. The link works mechanically but could land more precisely.

### Record and exposition check

I read record §6.5 and the exposition’s classical section. The XOR toy supplies both a reached-query branch and an abort/default branch. Its conceptual value is the one-way event inclusion: the light hit has probability 1/8 while predictor success is 1/4. I read the calculation in the supplied text; I did not execute its retained enumeration program. The exposition also explicitly distinguishes the three budgets and warns that a cheap prefix is not necessarily a light complete run. Those explanations can serve the expert paper without copying the whole teaching section.

## Section 4.5: contradiction, floors and losses

The discrepancy bound is assembled correctly, and the contradiction uses support-wise correctness averaged over each input law. Fixing and averaging coins does not require one deterministic tree to be good on every input. The generic statement is therefore proved in the ordinary argument at the inspected scope.

The explanation of the exponent loss is excellent: the selected Forrelation scale contributes the loss 1/k and the logarithms; the time union is paid by address length; the floors only change constants. That is what I want to remember at the end of the reduction.

The optional sharper erased-zero estimate is mathematically harmless, but it is a weak closing note for this section. It changes none of the stated exponent argument. I would subordinate it so the completed mL reduction carries the reader directly to the main conclusion.

## Section 5: analytic hardness and the uniform refinement

The opening paragraph supplies all the fixed-k hardness needed for the main theorem. The rest of the section develops a stronger uniform interface for a different task: an explicit threshold and a growing-k family. After the two principal reductions, this is a substantial detour before the exponent is concluded.

The detour is not intrinsically unwelcome. The improved k dependence and changed truncation may be of interest to a lower-bound researcher. That makes the attribution issue more significant: the paper should say precisely what mathematical work belongs to the reconstruction and what novelty has or has not been assessed. I do not infer priority from the displayed bound.

The comparison of k dependence and logarithmic dependence should be read as a tradeoff, not a uniform dominance statement. The source theorem and the reconstruction have different parameter behavior. The useful feature for this paper is explicit uniform control.

The two acceptance-gap displays are genuinely explanatory. The pointwise bridge explains why an off-promise analytic law can still prove a lower bound. Signal, solver error and uniform leakage are visible in a single inequality. However, nu_1 is only described by ancestry, despite the changed truncation. Either the section should make the defining object more concrete or openly identify itself as an outline with a precise destination.

The dimension condition would become less arbitrary if its role were exposed through the short leakage inequality already present in the record. The final distinction between nu_1 and the promise-supported minimax law mu is essential and correct.

I read record §§3.15–3.18 to check the threshold and attribution description. I did not audit the full analytic argument in §§3.7–3.14, so this reading does not certify the uniform estimate independently of its supplied proofs.

## Section 6: optimal exponent and optional family

The fixed-k ratio argument is straightforward and correctly quantified. One first chooses alpha, then a single k, then holds its constants fixed while m grows. It excludes every exponent below four and does not need a growing parameter. This should be the main payoff immediately following the two complexity bounds.

The explicit threshold 13669 k squared is unnecessary for that logical step. Using it there makes the main route appear dependent on the optional uniform reconstruction. It should remain available without obscuring the simpler sufficient route.

The growing-k remark appropriately says fixed-k eventual statements alone are insufficient. I followed its link to record §7.3 and found the uniform schedule and range t at least 80. The companion’s family definition would be tidier with that eventual range stated. I do not ask for a new theorem or an optimized finite exponent. The asymptotic statement and the explicit denial of an exact fourth-power lower bound are the right scope.

## Section 7 and the AI disclosure

The discussion separates the compared family theorem from the explicit fixed-circuit constants and therefore avoids claiming literal statement identity where there is only an additional theorem. That is useful to a mathematical referee.

The two ordinary classical correspondence arguments are still real mathematical steps: arbitrary independent randomness is represented by finitely many induced behaviors, and recursive compliance is identified with pathwise query counts. The record’s Appendix G.8 explains this. The phrase ordinary bridges could be replaced by the concrete operations so that the reader knows what has and has not been checked by the reported formal comparison.

I did not re-verify the receipts or compile the Lean sources. The disclosure is read as authorship and tool-use information. It does not convert this review into a fresh formal check.

## Appendix A and references

The appendix is useful when an example protects a likely false inference. The expectation-versus-cap example and the separate-versus-joint independence example are particularly economical. Their hypotheses are explicit and their scope is local to the lemma.

The adaptive AND example in A.7 would benefit from naming its compliance event directly. The redundant query deliberately selects which branches violate the cap; saying this would help readers focus on the conditioning error rather than the apparently inefficient algorithm. The count of eight compliant inputs then becomes transparent.

The dependent-selection example in A.4 should expose the probability of at least one discovery, rather than present 175/256 as an isolated number. The fixed-parameter warning in A.8 is correct but repeats a distinction §6 has already resolved. If the appendix is shortened, preserve the examples that explain otherwise tempting substitutions at their actual uses.

I read the bibliography source in full and checked the principal classical attributions against the supplied or retrieved passages named in the source inventory. This is not a claim to have read every cited paper. The current expert paper has a coherent proof spine; I would finish it. I would ask for the interface, contribution and allocation revisions before considering it an exemplary specialist companion.


---

# Part III — Handling-editor reading log

This is a simulated editorial perspective, not an attributed reaction of any real editor or cited author. I read the current expert Markdown from the title through Appendix A and its reference links before consulting the previous-round revision note. I then checked the exposition, selected record entries, the stated portions of the supplied literature, and the online sources listed in `feedback.json` (handling-editor source entries). This log follows the lead paper’s reading order and distinguishes first-pass reactions from those follow-up checks. The rendered-PDF review belongs to the coordinating reviewer, not to this perspective.

## Title, subtitle and abstract

The title states an unambiguous mathematical result. The subtitle immediately tells me whose separation is being explained and what kind of document I am reading. That combination matters: a title announcing the optimal exponent could otherwise look like a claim of a new separation by this author. The subtitle prevents that misreading without making the title timid. I would keep it.

The abstract gets to the theorem immediately. It also gives a real mechanism, not only a list of techniques: addressed certificates are hard to locate classically, and winner-only comparisons permit a quantum tournament. I understand what is being reconstructed before I reach the introduction. The abstract’s weakness is its description of this paper’s contribution. Reconstructing the ingredients and describing Lean formalisation are activities. The reader benefit that becomes apparent later is more exact: the short text exposes the weighted sampling identity and the capped predictor in inspectable form. That would help an expert already holding the preprint decide why to read this companion.

I would not turn the abstract into an evidence inventory. It does not need the names of formal modules, numerical trial counts, the fixed threshold, or a catalogue of independently reviewed components. Its current mathematical object and causal narrative are a stronger opening than those additions would be.

## Section 1: the theorem and the promise to the reader

The first paragraph is good. It states the total-function question and the cubic-to-quartic gap, credits OpenAI, and identifies the feature I should watch for: a true certificate defeats every rival even if a rival violates its promise. That is a meaningful starting point for a specialist.

The next paragraph gives both standard query-model syntax and the nonstandard convention the argument repeatedly needs. I would distinguish their editorial value. The full action of the bit oracle is familiar to the stipulated reader. The requirement that the cap hold on all branches, including off-promise branches, is essential. It will constrain the amplification subroutine and the decoder. I would retain that convention even if the standard oracle formula moved to a later definitions paragraph.

Equation (1) is exact, and its explanatory sentence works. The reader sees why the constant must be uniform and why one is added to Q. I do not need more foundational commentary at this point. The theorem follows soon enough and gives a concrete family, with logarithmic and numerical losses fixed. There is a minor attribution issue in the theorem’s packaging: its heading cites the source theorem, while the next paragraph explains that the displayed constants were reconstructed here. That explanation is correct, but it should remain attached when the theorem is quoted in isolation.

The credit paragraph is admirably direct. It says that the theorem, construction and two analyses are OpenAI’s. I would not add more novelty disclaimers after every later result. The paragraph then identifies the two reductions this paper proves, which is exactly what I need to know. Its final supplier inventory is less successful. The collection of hardness, decoding, exact circuits, amplification, minimax and the universal upper bound makes me parse dependencies before I have seen the construction. Most of those qualifications can be carried beside their actual uses.

## Section 1.1: the previous recipe arrives before the present object

Here I slow down for the first sustained period. I have just been promised an explanation of a winner-only comparison mechanism; instead I begin an AND–OR composition calculation for the older cheat-sheet construction. I need to hold n, m-prime, g, h and f in mind before I have formed a picture of the current columns. The calculation itself is valuable. It supplies the correct reason this selected recipe reaches the cubic scale and it carries the low-quantum-cost hypothesis that earlier rounds had evidently made explicit. My objection is placement, not mathematical content.

The next paragraph gives the exponent chronology again, now as continuous prose. The previous-round note explains why a table became prose: the user rejected cramped prose-heavy tables, and the final criterion permitted readable tables while rejecting that particular layout. The revision solved a real presentation problem. It did not settle whether the final historical paragraph duplicates the preceding explanation. On this read it does. I would keep one compact chronology and one actual bottleneck argument, giving them different locations or roles.

The text wisely says the AND–OR recipe stops at the cube rather than asserting that cheat sheets can never support more. I would preserve that narrow claim. The phrase that the framework turns any partial separation into a total one should also make its loss or regime clear; the supplied cheat-sheet paper explicitly emphasizes that the total separation can be weaker.

## Section 1.2: the paper becomes easy to follow again

The column description gives me the object I wanted earlier. It has a visible winning condition: an all-one string, a selected cell, and pointers to zeros in all other strings. I would give one short hint of what “certifies these answers” means—stored gate values checked locally—because simply storing answer bits would not enforce a promise. The detailed circuit can wait.

The nested-search obstruction is useful. It explains why finding a candidate and fully checking it cannot be done together by the most direct Grover construction. I can now see the role of comparisons. The phrasing that the tournament uses probabilities as weights briefly makes me wonder how those numerical probabilities become available. Section 3.2 later answers this beautifully: they are analytical weights and are sampled without being estimated. That distinction should already be visible in the overview, perhaps by moving rather than duplicating the later sentence.

The classical overview is substantially better than the usual “hide a cheat sheet” slogan. The independent chosen column, the dummy run, and the Z/m calculation explain why finding any zero does not suffice. The query position itself names the address, so the reader is told that accidental guesses must be bounded too. The last exponent calculation gives the promised connection between the mechanisms and four. This is the natural end of an overview and could have appeared before the older recipe’s algebra.

## Section 1.3: accurate related work, too many simultaneous questions

The first two paragraphs identify genuine design choices. The distinction that a zero carries no pointer is memorable and relevant to the lower bound. The direct pointers are stored as separate bit fields, so a comparison only pays for the one rival field it needs. This explains how the construction uses an idea whose alphabet cost looked unattractive in a different setting.

The paragraph is factually careful about highlighted leaves and back-pointer variants. I checked the supplied pointer-function discussion and the previous-round correction rather than reviving an older misattribution. Still, a reader at this stage must absorb a balanced tree, a no-back-pointer variant, an exponential alphabet, a large pointer field and its bit-level encoding. Much of this would be clearer after the new local-test interface has been stated.

The explicit-Forrelation versus random-matrix-Rorrelation distinction is worth keeping: the small exact circuit is a mathematical reason for the chosen supplier. It tells me why lower-bound exponents alone do not make the partial problems interchangeable.

The comparison-search paragraph has a clear closest antecedent, then expands into minimum finding, king finding, candidate-claim comparisons and bounded-error search. The current wording is accurate about the different input guarantees. My editorial concern is that every earlier referee question has been made an opening obligation. I would keep the closest antecedent and the concrete nested-search obstruction central, and relocate the remaining alternatives. Online reads of AIK v3 and BDK v1 confirmed that the specific comparison contracts are the appropriate ones; I did not find a reason to add another credit correction.

## Section 2: the supplied properties are the right abstraction

The powers-of-four restriction and the factor twenty are explained by their actual uses. That is good mathematical writing. I do not have to guess whether either parameter reflects a genuine endpoint obstruction.

The Walsh formula and one-sided promise are precise. A large negative value is explicitly unpromised. I then get the three supplier properties. This is the right abstraction for the construction, but the roles of those properties could be named before the formula-heavy material: a classically hard answer, a cheap quantum decoder, and a small exact circuit whose evaluation can be certified. That would tell me what to retain from the Forrelation definition.

Property (ii) makes the off-promise cap explicit and does not pretend that the squared statistic tests the promise. The alternative interference algorithm is correctly cited, but it interrupts the supplier interface with another implementation not used in the stated count. I would preserve the reference in the record or as a small source note rather than ask the reader to choose between decoders here.

The total-function definition is strong. In particular, saying that transcript bits are freely assignable input coordinates is better than calling them independent. It distinguishes totality from the later hard distribution. The uniqueness proof is short and illuminating: a second all-one column obstructs the first column’s pointer condition. The sentence about fixing the same circuit for both bounds also matters. It prevents a family-level proof from quietly using incompatible witnesses.

The local-tests paragraph contains the right content but too many jobs. It counts the tests, explains the two extra output conditions, gives the topological induction, handles all addresses of nonwinners, counts queries and asserts coherent access. I do not want any of these steps deleted. I want a visible boundary between correctness and cost. The statement about additional output tests is especially useful because it resolves apparent double counting at the output gates.

## Section 3: the exact sampler is the paper’s explanatory centre

The two-part algorithm is clear: construct a short list and verify it. T and epsilon should be named as a list cap and an error allowance when they appear. The general amplification lemma then begins before the comparison experiment. I understand the lemma, but not yet why exact preservation of the conditional label law is the property this application needs. The placement could be improved either by moving the lemma to its first sampling use or by previewing the event to be amplified.

The bounded-amplification proof is now carefully scoped. It handles zero probability, near-unit probability, the conditional output law and the fixed cutoff. The previous-round notes show those were deliberate repairs; I am not treating them as missing. The contrast with untruncated expected-cost QSearch is useful and should survive compression.

The sorted-pair rule in §3.1 is excellent. It makes complementarity exact. Retaining decoder labels explains why the coherent circuit has the same probabilities as the measured experiment. The winner’s guarantee is also correctly asymmetric: it needs its own address decoded correctly and places no correctness requirement on the rival’s address. These details are all part of the argument, not implementation trivia.

In §3.2 the actual algorithm is finally stated explicitly. That is essential: an analysis of an ideal process alone would not tell me what a quantum algorithm does. The weight definition and half-drift identity are compact enough for a specialist. Their interpretation is particularly good: fresh workspaces multiply probabilities, orthogonal labels add masses. Equation (9) then feels explained rather than merely asserted.

The fractional four-candidate example earns its space. It demonstrates nonuniform sampling, which the deterministic-cycle example cannot do. The warning that it is not a realization of the four-column Boolean board is necessary and is already fixed. I would not force the examples into one object just to remove that sentence.

The coupling paragraph preserves the exact conditional law at each common history and stops at the right event. It then abruptly becomes a query-count paragraph. A paragraph break and a less overloaded stage-count symbol would be enough. The explanation should remain connected prose unless pseudocode genuinely makes the output rule easier to inspect; a blanket ban on algorithms or lists would be as unhelpful as making every proof into one.

Section 3.3 makes the defect-search convention explicit. A successful search means rejection of the candidate; no defect found means acceptance. It also explains why accepting an earlier false candidate on a one-input cannot hurt the decision problem. This is a good example of an apparently odd event being interpreted by the output task rather than by an overstrong certificate-finding specification.

The loose logarithmic exponent is appropriate. The exact huge C_k constant belongs with the later growing-k use, since that is where its dependence matters. The fixed-k proof needs only a fixed constant.

## Section 4: the planted reduction is genuinely reconstructible

The opening generic statement tells me that the lower bound depends on classical hardness and the circuit’s correctness, not its size. That is useful modularity. I would name the inherited address length and circuit contract locally, so that the displayed generic inequality is not mistaken for a theorem about arbitrary r.

The minimax setup chooses one hard law before taking independent samples. The direct-product lemma puts joint independence and all-branch separate caps in its statement. The proof’s unnormalised measures have a clear purpose: there is no null-history conditioning. The single-factor recursion is compact and suits the expert paper better than importing the exposition’s longer conditional-law example. The statement that Drucker’s global-budget theorem would also suffice is worth keeping. It avoids an inflated claim that a specialized lemma is indispensable.

The dummy/planted construction is precise about the two changed locations. The coupling inequality deliberately overcounts a visit to the selected cell even when the queried bit has not changed. That is a necessary one-sided event inclusion and is stated plainly. The erased-zero count distinguishes fresh positions from repeated calls, and independence of the selected index is attached to the completed dummy run.

The first sentence of §4.4 is the classical counterpart of the successful-mass sentence in §3.2: a query position already names an address. It covers guesses without pretending that every hit first computes the answer vector. The simulator has a total output, enforces its cap on every run, and bounds a joint event under the original law. I can recover the mechanism. This is where shortening must be most conservative.

The simulator paragraph is still visually dense. It would help to separate the fixed-column/fixed-time setup and free information from the output rule, then keep the event inclusion in its existing later paragraph. That is a prose organization change, not a missing theorem.

The explicit average over columns is useful. I can see why the m terms disappear. The closing interpretation of the three discrepancy terms then tells me where the exponent is preserved. The optional stronger erased-zero constant interrupts the end of the proof; I would leave its destination in the record and let the power-loss explanation close the section.

## Section 5: a valuable secondary argument blocks the main route

The first paragraph says the fixed-k estimate follows from the cited theorem and suffices for the separation. At this point I expect the two completed reductions to be combined. Instead the text starts a uniform analytic refinement with a different dependence on k, an alternative truncation, Gaussian laws, a shallow-tree bound, moment inequalities and error amplification.

These are serious mathematics, not padding. The pointwise promise bridge is particularly useful: it explains why a solver’s performance on the promise can be used against laws with off-promise mass. The problem is that the paper has not decided how central this independent proof is to its contribution. The introduction mentions an additional estimate but asks the reader primarily to care about two reductions. The uniform proof deserves either a clear secondary role or enough foregrounding that a specialist expects to assess it.

The phrase about a different algebraic truncation is too compressed to explain the improved k-dependence. The selected record entry explains two departures from Bansal–Sinha, including first-block interpolation. A brief statement of what the change buys would make the short outline more informative without importing the entire proof.

The distinction between the analytic law nu_1 and the promise-supported minimax law mu is correct, but it appears at the end. I wanted that distinction when nu_1 was introduced. Moving the existing sentence earlier would make the off-promise gap calculation easier to follow without adding words.

## Section 6: the mathematical conclusion is cleaner than its route here

The quotient argument is exact and easy to follow. It fixes alpha, then k, then constants and threshold, then lets m grow. The sentence about what a fixed k excludes is useful and prevents confusing an infimum with an attained fourth-power finite-parameter separation.

However, the opening uses the explicit threshold 13669k², which makes the main conclusion seem to require the optional uniform proof. The fixed-k theorem only needs a sufficiently large threshold. I would complete that simpler route before, or independently of, the uniform refinement. The growing-k family then becomes a legitimate optional extension with its uniform classical and quantum suppliers together.

The final warning that this does not prove R=Omega(Q^4) is the right one. It is a mathematical boundary, not defensive prose to be removed by a style detector.

## Section 7 and the disclosure

The formal section correctly identifies its main endpoints and the difference between the compared existential family theorem and the explicit-circuit theorem. That distinction is useful to an ordinary specialist and should be kept. The model bridges also state meaningful preservation properties.

The nonemptiness of the minima and the standard-axiom phrase have lower value here. They are better suited to the record’s model and checking discussion. The final auxiliary-interface paragraph is harder still: measured labels, reset workspace, retained successful states, basis tests, finite seeds and recursive compliance appear in quick succession. The paragraph is accurate enough to signal that distinctions exist, but not short enough to feel like an ordinary theorem report and not long enough to let me assess the interfaces without leaving the paper.

“Ordinary bridges” is the weakest phrase in that paragraph. It does not classify which mathematical implication is proved on paper, which is checked formally, and which is a reading of the formal definition. A short explicit description would help more than the adjective. No new formalisation is requested; this is an explanation of the evidence already supplied.

The AI disclosure names what the systems did. It should also identify the accountable author, if the author is willing to accept that responsibility, without claiming independent human verification that has not happened. I would not import a boilerplate declaration from another paper.

## Appendix A and the supporting funnel

The appendix is now readable full-width prose. I would not revive the old table criticism as if the table were still present. The revised format does make the appendix’s selection more visible: construction-specific failures sit beside generic lessons about independent marginals, expected caps and varying parameters. For this expert audience, A.1, A.3 and A.7 are the strongest. They explain actual tempting shortcuts in this proof. The others could remain in the record with precise links at their uses.

The exposition agrees on the main bounds, winner definition, decoder limitations and capped predictor. Its longer examples are useful destinations rather than material the expert paper should repeat. Two details need harmonisation: its formal-family paragraph mentions the power six as counted in prose without pointing to the explicit-circuit theorem now named by the expert paper; and the answer to Question 4 begins with “Yes” before explaining that a later target query makes the whole path heavy. That answer should state the case distinction first, because the exercise is testing exactly that distinction.

The record’s opening and reading guide distinguish the fixed-k construction route from the uniform refinement. The expert paper should preserve that dependency choice more visibly. My conclusion from the editorial read is not that the mathematics must be rebuilt. It is that the paper should make a firmer selection: let the two reductions carry the main argument, finish the fixed-k conclusion promptly, and give secondary analytic refinements and evidence interfaces deliberate, recoverable destinations.


# Part IV — Coordinating inspection and adjudication

## What this pass adds to the three readings

I read the complete attached conversation, the current assignment, the source-status object, the lead Markdown and bibliography, and the passages identified in the coordinating source records. The historical conversation establishes prior preferences and work; it does not authorize an unrelated repository operation in this return. The assignment is feedback on the expert companion, with the exposition and reasoning record serving that review. No manuscripts, skills or repositories were changed.

The lead paper now has a coherent main argument. The current text contains the difficult repairs identified in the previous round: the accessible success flag; an every-branch amplification cap; the high-success branch; exact complementary probabilities from one sorted-pair experiment; fresh workspaces; a history-conditioned stopped coupling; verification valid at every decoded address; an independently selected hidden column; and an unconditional joint-event bound for the capped simulator. This review does not report those as absent. The next question is how much work the reader must do to recover their purpose.

The main agreement across perspectives is about route and allocation. The quantum reader wants the actual comparison interface before the detailed comparison with neighboring algorithms. The lower-bound reader wants the already proved generic reduction stated completely. The editor wants the sufficient fixed-k argument finished before the optional analytic reconstruction. These are compatible revisions. They do not demand a new theorem, a stronger separation or further formalization.

## The current PDF, pages 1–16

I rendered all 16 expert-companion pages locally, inspected every page in contact sheets, and viewed the figure pages individually at higher scale. I also extracted font sizes and link annotations for targeted corroboration. The supplied PDF is the object assessed; no new PDF was authored.

The title no longer leaves the final word stranded. The two figures do not exhibit the earlier crossed-label problem, and the former prose-heavy tables have been replaced by full-width prose. I saw no current page overlap, text clipping or obvious markup leak in the inspected pages. Those observations are visual inspection, not a claim of exhaustive typesetting correctness.

The remaining issue in Figure 1 on PDF page 3 is scale and selection. Several explanatory labels are approximately 6.4–7.3 points against body text around 10.9 points. The mathematical meaning is available in the caption, but reading the detail at normal page size asks for more effort than the surrounding prose. The eight drawn bit positions are schematic, while the formal parameter convention is m=4^t. The caption should identify a schematic row count so the drawing does not look like a literal admissible instance. The useful reader operation is to follow a winner's outward pointer to a zero and then observe why the reverse direction cannot find a zero in the winner.

Figure 2 on PDF page 9 successfully aligns the dummy and planted columns. Its chief explanatory obligation is literal reuse: the same address inputs and all other untouched data occur on both sides, not freshly sampled copies. The caption says this; the repeated sampling notation in the image could say it more plainly. Small blue labels around 7.4 points and the red annotation carry information better repeated briefly in the caption. The picture's structural purpose is sound, and the small illustrated board is already distinguished from an instance satisfying an eventual hardness theorem.

The long bibliography URLs and commit hash still create awkward lines and white space. The project name complexitylib is also split across a line in §7 on PDF page 12. These were already acknowledged in the prior review, so they are recorded as remaining finishing work, not newly discovered defects. Their priority is below the proof-route and mathematical-contract issues.

## Mechanical link existence and mathematical entry points

The packet's link map resolves the expert paper's local targets. The following observations ask whether the destination begins the mathematical task promised by the link. They were checked against the current packaged record. The remote pinned record and packaged record have different recorded revision identifiers; their exact remote bytes were not independently compared. No finding here asserts that a URL is absent, that its HTTP request fails, or that its published historical contents were freshly audited.

| Promise in the expert paper | Current anchor in the packaged record | More useful existing destination |
| --- | --- | --- |
| §2: proof of the quantum decoder, property (ii) | `forr_repetition`, at the tail estimate | `forr_quantum`, where the preparation and projection probability begin; alternatively narrow the label to repetition |
| §3.2: a longer version of the tournament proof | `upper-quantum-tournament`, at the real sampler | `upper-tournament-statement` for the complete proposition and proof, or `upper-ideal-process` for the ideal argument |
| §3.3: the envelope C_k ≤ 2^53 k 2^(10k) | `upper-explicit-log6`, containing an explicit sum | `ROOT-GROWING-K`, where the sum is dominated by the stated exponential envelope; the two stages can have separate links |
| §4.4: a trace of the capped simulator on a small example | `CL-simulator`, the general simulator | `CL-simulator-example`, the existing positive execution |

These are low-cost, high-value corrections. A functioning anchor can still ask a reader to search backward for half a proof. The supplied writing skill already requires full-proof destinations; the method failure is enforcement rather than lack of another general rule.

## Fresh finite checks

The following checks used exact integer or rational arithmetic. The stated probabilities were independently reconstructed from their finite experiments where applicable. No packet-supplied program was executed to obtain them. The results are recorded in `checks/exact_checks.json`; they are finite checks, not proofs of the asymptotic theorems.

| Passage | Checked value | What the check establishes |
| --- | --- | --- |
| Appendix A.1, k=2 and m=4 | Φ=−1; projection probability 1 | The sign-loss example has the stated extreme value |
| §3.2 fractional weights after pivot 2 | W=23/12; preparation success 23/48; label law (12/23,0,8/23,3/23) | The displayed normalization is correct |
| Appendix A.4 | Dependent hit 175/256; independent selection 1/4; each marginal probability for I is 1/4 | Uniformity of I does not substitute for independence |
| Appendix A.5 | Joint success 5/8 versus separate-cap comparison 1/4 | The expected-cost counterexample has the stated gap |
| Appendix A.6 | Joint success 1/2 versus independent comparison 1/4 | Individually independent-looking side information need not be jointly independent of the target tuple |
| Appendix A.7 | 8 of 16 inputs compliant, 5 compliant successes; joint 5/16, conditional 5/8, β²=9/16 | The joint/conditional distinction is numerically real |
| Record §7.3 | 5,707,107,503,019,240 < 2^53 | The displayed uniform envelope has the reported integer slack |
| Fixed-k threshold calculation | 4·13669=54676 > 54675 | The quoted threshold coefficient clears the specified comparison |

The quantum referee also checked the suggested second pivot in the existing fractional illustration: following pivot 2 with pivot 4 leaves weights (1,0,4/15,0) and normalized law (15/19,0,4/19,0). This is optional advice about making an existing example exercise multiplication into history. It is not a proposed new theorem.

## Sources and quantitative scope

The source inventory distinguishes the supplied texts, exact online editions, targeted reads, sampled passages and abstract-only discoveries. The coordinator reopened the primary sources used for the important online comparisons. The BBHT page range is a genuine disagreement between publisher and arXiv metadata. The located arXiv lemma numbering is usable, but the uninspected journal numbering is not being declared wrong.

The two newest abstract-only discoveries were not converted into demands for citations or claims that an existing method has been superseded. The October 29 tournament paper is a follow-up lead whose full applicability has not been assessed. The fixed-edge comparison context alone does not establish applicability to arbitrary fractional loser comparisons.

I sampled Tal's introductory fixed/growing-parameter explanation and SSW's introduction and analytic overview from the supplied literature. They reinforce two presentation decisions: different parameter routes should remain visibly separate, and an analytic improvement should explain the operation that improves it. Their general orthogonal-matrix setting does not by itself supply the small exact Walsh circuit required here.

The register's 42-document comparison shelf mixes research papers with slides, notes and a survey. Its metrics are descriptive detectors. They do identify dense multi-job paragraphs; they also flag harmless author lists as triads and count necessary formal-status language. No uniform rewrite or numerical target follows from those rates. The method recommendations preserve the current rules that already protect mathematical scope and successful explanations.

## What remains unestablished by this return

The principal reductions were inspected deeply enough to give detailed, source-bound advice, and no new fatal inference was found there. The full analytic Forrelation reconstruction was not independently reproved. No new formal execution, exhaustive novelty search, venue acceptance, or independent human validation is implied. The useful deliverable is an accountable review: every granular comment attaches to current text, every literature comparison has an identified scope, and the important repaired arguments are protected while the remaining revision choices are made concrete.
