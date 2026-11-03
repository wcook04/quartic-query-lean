# Reading log

The expert companion is the lead document. These section-ordered notes preserve what each reading pass understood, where it slowed down and what later consultation resolved. They are analytical reading notes, not a timed user study. Exact read and skim scopes are in `feedback.json` and `review_scope.md`.

## Specialist companion: section-by-section reading log

These notes concern the current Markdown in the round-seven packet. I read the expert companion in full, checked its classical argument against all of record §6 and source-preprint §4, inspected the two figures and the shortcut table in the supplied PDF, and used the previous-round dispositions to distinguish a remaining problem from a fixed one. The order below foregrounds the classical argument, then returns through the rest of the companion. “I” describes an emulated specialist reading position, not the opinion of any named researcher.

### §4: the randomized lower bound — entry

I can see the right proof architecture in the opening: make a zero-input and a nearby one-input, identify the two possible places at which the executions first disagree, and bound each place separately. The genericity of the argument is particularly useful. Forrelation will provide a hard partial function, but the planting argument itself needs only a suitable hard distribution and a correct circuit. I would like to see the generic numerical goal immediately, because it is stronger as an organizing statement than “we now prove the lower bound in (2).” Equation (2) already has the specialized power m^{2−1/k}; the proof I am about to read naturally has the simpler output mL.

The minimax paragraph is careful. The compactness sentence earns its place: it explains why “L is below randomized complexity” supplies a strict gap for the attained optimal mixture, rather than merely a collection of inputs defeating different deterministic trees. The resulting μ is one common law for all trees. I do not need a proof of finite minimax here. I do need to remember that μ is supported on the promise, and the text now tells me that plainly.

The notation is less modular than the argument. The section is temporarily about an arbitrary P, while the eventual conclusion retains the Forrelation-specific name F_{k,m}. The record's F_{P,C,m} makes the reusable statement easier to hold in mind. This is a presentation problem, not a defect in the construction.

### §4.1: separate caps

The lemma states the relevant output task: recover the entire vector, not its parity and not a substantial fraction of its entries. Its independent side information is jointly independent of the whole target tuple. Its cap holds on each branch. Those restrictions are exactly the ones I would look for before believing a perfect β^r product bound under adaptive interleaving.

The unnormalized proof is a good choice for a short companion. It avoids a detour through zero-probability histories and gives an ordinary finite induction. The definition of V_d is understandable: it is the best weight of correctly answered inputs under a given remaining allowance. I slow down at “the recursion absorbs its two branches.” I can supply the algebra, but this is the only nontrivial factorization in the proof. The branch sums change one factor; all other factors are common and nonnegative. Writing that fact explicitly would be more valuable than another sentence explaining where a loose constant later comes from.

The source paragraph is substantially improved. Shaltiel's historical contribution is described as a fair-tree XOR-advantage result in the uniform setting, not silently relabelled as the exact vector-output theorem used here. Drucker's global-budget theorem is now explicitly acknowledged as sufficient for the actual simulator. I checked the specialization: his total allowance becomes L and the loss is only a factor two in β^r. That is comfortably absorbed later. This should remain a positive observation. There is no reason to manufacture a claim that the separate-cap version is uniquely necessary.

The two counterexample pointers are appropriate. A reader who knows direct-product theorems will understand why expectations and marginal independence are different assumptions. The table makes those differences concrete without interrupting the lemma.

### §4.2: the coupled inputs

The sampling procedure is now easy to recover. First choose the zero positions and the independent address inputs; leave every cell blank; only then choose the hidden column I independently of the complete dummy input. The planted input shares all address data. It erases one zero and fills one selected cell. This is enough to see why the two function values differ.

I pause briefly at the all-zero cell convention. In familiar cheat-sheet lower bounds one often first ensures that the blank pattern is not a valid certificate. Here the dummy value is zero already because every X_i contains a zero. A short explanation would stop an experienced reader from checking a convention that is not required for this particular support claim.

The coupling inequality has the right direction. A query to any bit in the selected cell is counted, even when that particular planted bit equals its old blank value. That deliberate overcount is useful and should be said explicitly, as it is in the source preprint. The proof needs to upper-bound the first difference; it need not identify every query that actually causes a difference.

Figure 2 is a useful two-panel picture. The erased zero and selected cell are highlighted, and the caption says that the address inputs are shared. However, its claimed concrete dimension is wrong: it says m=4 while drawing eight bits in each X_i. I verified that this is in the figure source, not merely PDF text extraction. The visual should either show a genuine four-by-four X matrix or announce that it is schematic. The current mixed scale is particularly unfortunate because m is doing two jobs in the proof: number of columns and number of positions per X string.

### §4.3: the erased zero

Equation (11) is the cleanest line in the lower-bound section. Fix the dummy run, count its discovered columns, and then average the independent selected column. It isolates the extra factor 1/m without making a dubious argument about the algorithm's adaptive choice of which columns to inspect.

The next paragraph needs a small qualifier with a large logical function. J_i is uniform among unqueried rows only before its zero has been found. A repeated query to an observed zero returns zero with certainty; it just makes no new discovery. The record and the preprint keep those concepts separate. In the companion they are compressed into “finds the zero” and “rows ... have been queried.” I would restore “new discovery,” “before the first discovery,” and “distinct positions.” The resulting early/late estimate is then completely standard.

I do not need the improved m(m+1) denominator at this point. The proof has reached the bound required for the first channel, and I want to proceed to the second. A footnote would preserve the useful optional fact without asking me to assess a second search inequality before the planted-cell reduction.

### §4.4: the planted cell

The definition of heaviness is correct: λ_i counts the total calls to all r address inputs of a column, including repetitions. It is not a separate count bounded by L on each instance. The global G budget therefore limits the number of heavy columns, and independent I makes heaviness unlikely in the selected column.

The sentence that a query's location already names an address is the conceptual center. It explains why cell contents do not need to be decoded by the simulator. The reduction supplies all other data for free, enforces its own cap while running, and at the proposed query time outputs the named address. This is a predictor of r hard answers. It is not an algorithm that certifies its own guessed cell.

The long paragraph is correct but carries too many transitions without a break. I would put the simulator's definition in one paragraph and the original-event-to-success inclusion in a second. The distinction matters because “nonheavy” refers to the complete original run and cannot be used as an observable condition deciding which hard inputs the simulator receives.

The sentence after equation (12) is excellent: the event remains under the original law. The lower-bound proof does not ask whether a cheaply investigated column is conditionally hard; it maps every cheap successful visit into a success of a globally capped predictor. I would protect this sentence during any shortening.

I slow down once more when the union over query times and the average over I are combined. The final Gβ^r is right. The reader should see that the average of m identical per-column bounds cancels the m, while the union over G times remains. This is exactly where an extra factor could spoil the exponent, so one line of accounting belongs in the companion even if a specialist could reconstruct it.

### §4.5: contradiction and constants

The three-term estimate is the right endpoint: erased-zero discovery, heavy selected column, and an exceptional successful address guess. The explanatory sentence gives each parameter a role. That is more helpful than optimizing 1/100 or the address multiplier 20. The final transition to randomized algorithms is also correct: a common input law and a common deterministic bound can be averaged over coins, while bounded error on every supported zero- and one-input forces a gap of at least 1/3.

The floor paragraph is correct. It is also more detailed than the companion needs. I want the generic mL lower bound to be the remembered ending. The elementary comparison at t≥8 and the coefficient 1/400 can remain as an explicitly cited conversion without taking a full paragraph away from the harder parts.

### §5: what Forrelation supplies

The first two paragraphs clearly separate the published fixed-k supplier from the record's uniform-in-k estimate. They no longer imply that the explicit threshold is in Bansal–Sinha, and the comparison of k-powers and logarithmic powers is balanced. I do not read (16) as a global improvement over the literature bound. I understand why uniformity becomes relevant only for the later schedule k=k(t).

The last paragraph is too compressed for the panel most interested in this section. It identifies the rounded Gaussian law and the derivative method, but “because the promise is one-sided” is not yet the missing argument. Why should a solver allowed arbitrary behavior off promise distinguish laws that both have off-promise mass? The record supplies the answer in §3.14: pointwise acceptance inequalities produce an expectation gap, and amplification reduces the error below a positive signal exponentially small in k. The uniform law's leakage also has to be small. I need that relationship, even in one line, before the depth 50kD+1 and the signal scale 18^{−(k−1)} feel motivated.

The distinction between this planted analytic law and μ is now explicit. That correction should be preserved. A future edit should not replace both by one generic phrase “the hard distribution.”

### Abstract, §1 and §1.1: opening and history

Returning to the opening after the proof, I find the main theorem and the cubic consequence persuasive. The order “choose α, then k, then let m grow” is already foreshadowed, and k=3 gives a concrete refutation. The abstract's claim that a classical algorithm cannot locate the certificate without spending L in many columns remains too pathwise. The proof says that low-cost discovery is unlikely under the hard experiment. This distinction is now well handled in the body; the abstract should catch up.

The long First/Second/Third/Fourth paragraph is the part that most resembles a project report. Its information is mostly useful, but its sequence is not the reader's sequence of questions. Provenance, the construction's mechanism, proof scope, numerical constants, the long record and Lean all compete before the overview has settled. The theorem should carry the result; a short contribution statement should say what the companion does; the quantitative inventory can live where the estimates are used.

The cheat-sheet arithmetic is a valuable improvement over an unexplained list of historical exponents. I can see why the AND–OR recipe stops at three. The polylogarithmic assumption on Q(g) should precede the quantum-cost formula. I would also preserve ABK's causal explanation of why certificates of all inner AND–OR values certify the outer promise. That is what connects the old framework to the transcript certificates in the new function.

The historical table is serviceable, but its equality heading is imprecise. Its rows describe separations and a universal upper bound, not equations R=Q^a. This is an inexpensive repair.

### §1.2 and §1.3: mechanism and antecedents

The overview gets the new structure across: a separate array per column, an independently hidden winner, cheap quantum comparisons, expensive randomized addressing. The sentence “a query ... reveals s by its position” is worth keeping verbatim. The phrase “one marked zero,” by contrast, needs to identify which zero is marked. An algorithm can find an arbitrary dummy zero much more cheaply than the m² scale; it is the zero belonging to an independently selected hidden column that matters.

Figure 1 enlarged the winner's certificate array successfully, but it draws no trace of the other arrays. The text corrects this, yet the figure is likely to dominate memory. A small indication of a separate array attached to every column would reinforce the source of the extra classical cost.

The pointer comparison contains one actual factual error. The cited ABBLSS function does not require every zero in a nonmarked column to point back to the marked column. It requires the distinguished highlighted zero/leaf to do so. Other zero cells can have other destinations, which is why their randomized algorithm handles a set of candidate columns. The current wording is a residual of a useful previous-round addition, not a reason to remove that addition. Correct the restricted set of zeros and keep the explanatory comparison.

The distinction between Walsh Forrelation and random-orthogonal Rorrelation is handled appropriately. The reason for choosing an explicit nearly linear exact circuit is also stated where it belongs. Likewise, the comparison with certificate-complexity separations names the actual interface difference, including the possibility of probability 1/2 for a comparison between losers.

### §2: construction and local tests

The three supplier properties are a good interface. I know what the classical proof consumes, what the quantum decoder consumes, and what makes an arbitrary-input certificate check possible. The one-sided promise and the projection statistic are kept distinct. The restriction m=4^t would be more memorable if the integer denominator m^{(k+1)/2} were explicitly tied to it.

“Independent input bits” is unfortunate at definition time. These are free coordinates, not yet random variables. The later law imposes independence, and that later probabilistic fact should have its own vocabulary. This is a small wording issue with particular importance for a lower-bound audience.

The fixed circuit is correctly kept common to both bounds. The local-test dichotomy is also exactly right: a loser fails at every address, not merely at a correctly decoded one. Those statements are more important than the optional n^{1/44+o(1)} input-length conversion. I would not let a shortening pass remove them.

### §3–§3.3: the upper bound read from the classical side

I can follow the upper bound without needing to audit every constant in amplitude amplification. The sorted unordered-pair convention gives the symmetry identity, the retained label registers give the intended probabilities, and the winner's all-one column protects it from arbitrary unpromised opponents. These are the interface facts relevant to the separation.

The weighted tournament explanation is effective. Its total weight is at most halved in expectation, and its successful sampler does not compute those weights. The distinction between w_i/m and w_i/W is explicit. The stagewise coupling uses the full history, so a success guarantee is not silently conditioned into a new process. The output is a short list, and local verification converts it into the total Boolean answer. I would keep these links intact.

The sentence about unknown-success search having only expected cost should refer to the cited algorithm, rather than sound like a universal limitation. The current lemma is itself a capped procedure with a threshold guarantee. Finally, the padded ℓ^6 count is a sensible safe estimate but has too much narrative space. This is a particularly clear place to shorten the companion while retaining all its substantive mathematical content.

### §6: what “four” means

The fixed-k proof is clear and should remain the main ending. The positive exponent gap beats any fixed logarithmic loss, and the universal upper bound closes the infimum. The paragraph explicitly says what it does not prove, in mathematical terms rather than project-status terms.

The growing-k remark is correct in its intended asymptotic role, but its finite constants invite the wrong reading. At t=80, the stated lower exponent is negative. This is a valid but uninformative endpoint of the quantitative estimate, not an error. The remark should distinguish its validity threshold from the range in which the displayed exponent is useful. The full 508 formula is optional information in a companion whose main proof never needs it.

### §7, references and Appendix A

The formal section now reads much more like a mathematical scope statement. It distinguishes the headline theorem, the named-circuit quantitative theorem, the measured-label amplifier actually used, and the retained-state result. The description of success together with recursive compliance is particularly good. It avoids the false simplification that every formal statement is merely stronger or weaker than its printed counterpart.

One sentence has the wrong logical connective: the statements' having no hypotheses explains unconditional scope, while their checked proofs establish completeness. Those are distinct facts. The two unrelated universal quartic constants can also leave the main flow; the record already explains the two routes.

The short AI-tools note is adequate for this mathematical companion. I would not turn it into a workflow diary. For current literature context, a brief Ben-David–Blais 2025 direct-product citation could be useful, but it is not a reason to replace the elementary proof.

The shortcut table earns its place at the end. Its joint-versus-conditional row is unusually good because it exhibits both numbers in one example. Its cross-references need actual row labels: the paper repeatedly says “row 7,” but the printed table asks the reader to count. The description of β should also distinguish a success upper bound from an exact optimum. These are small editorial repairs to a useful appendix, not grounds to discard it.


## Reading log: long record, construction and classical lower bound

### Scope and reading conditions

These notes cover the current Markdown, not the stale PDF. I read §§1–2, §4, all of §6, all of §7, Appendix B.7–B.9, and Appendices C–F in full. I also read G.1–G.4 and G.8–G.9 to understand evidence terminology; the findings here concern G.8 and the points where that appendix affects the owned mathematical sections. The matched classical sections of the companion (§§4–6) and exposition (§§5–6) were read for consistency. Other reviewers cover the intervening analytic and quantum arguments. This is a bounded prose and mathematics review, not a new Lean, Comparator, or PDF-rendering run.

The previous record dispositions and classical-expert verdict were read before the findings were finalized. Several improvements are now real: the independent-information hypothesis is explicit; the direct-product comparison distinguishes separate caps from a global budget; the finite examples explain their purpose; and the formal evidence has a dedicated appendix. The comments below concern what remains after those repairs, including places where revised statements did not propagate.

### Opening, reading guide, and §1

The opening now gives an intelligible construction-level story: use hard partial functions to hide addresses, place certifying material at those addresses, and let a genuine winner rule out rivals. I can see why the classical argument should need approximately the number of columns times the effort required to locate one address. The same-function sentence at the theorem is essential. Without it, the independent generic classical theorem and particular efficient quantum circuit could be mistakenly combined for different total functions.

I stop at the claim that a lightly queried column reveals its planted cell with probability at most \((2/3)^r\). Read literally as an eventual discovery probability, that is stronger than the proof. The precise result is a fixed-query-time joint event bound, with nonheaviness intersected rather than conditioned on. A union over prospective query times introduces \(G\). Section 6.5 gets this right. The opening therefore needs synchronization with its own proof, not a new lower-bound argument.

The guide improves the first route by permitting the reader to use the direct-product statement without reading both proofs. It does not identify exactly where to resume after the statement. The cap-event corollary and the paragraph explaining its planted use are more relevant to this route than the optional second proof. An exact destination would remove this ambiguity.

The companion route in §1.1 no longer points to the current section numbering. This is particularly damaging in a document intended as a destination for readers of the shorter account. A link that reaches the correct file but directs the reader to the wrong section is not a successful navigation check.

### §2: query models and exact examples

The model distinctions are careful. Finite mixtures with arbitrary real weights make the exact \(2/3\) threshold meaningful, and the OR example explains why finitely many fair bits are a different convention. The separation between a partial function's promise and its Boolean values is also established before certificates use it.

I slow down when mathematical definitions immediately acquire source-type names. The types are useful for an audit route, but they repeatedly change the register of the main explanation. Similarly, the correction about which textbook section is “Quantum parallelism” answers an earlier editorial problem instead of the current reader's model question. Edition-specific detail belongs with the inspected-edition list unless it changes the mathematics being explained.

The small-example table works well because each example targets a plausible wrong inference. It is not a random collection of easy cases. The off-promise example prepares the domain-output check; the exact OR threshold prepares minimax; parity distinguishes classical from quantum queries.

The zero-query receipt note is harder to interpret after the evidence update. The body says the packet supplies no successful receipt for certain exact example declarations, while G.4 lists a compared general ModelZero statement. These may refer to different declarations and snapshots, but a reader should not have to reconstruct the project's history to know whether a mathematical example has formal support.

### §4.1–4.2: transcripts and the semantic total function

The local-to-global transcript argument is elementary and correct. It is also the place where a miniature gate illustration would do the most work: one proposed gate value, its predecessor values, and whether each comes from the input or from the cell. The later 180-gate finite circuit is too large to supply that first picture.

The semantic definition earns its separation from the verifying implementation. Uniqueness and totality follow from the winner predicate itself; an off-promise decoder is never asked to establish them. This organization should survive any shortening.

The formula \(r=40t=20\ell\) arrives before its exact lower-bound purpose is local. I know it must make address prediction very unlikely, but the decisive reason is the later union over \(G\) prospective cell queries. A short pointer to that job would make the constant look selected rather than arbitrary.

The added input-length calculation is useful. It confirms that the enormous table is still polynomial in \(m\), with a large fixed exponent. The operational consequence deserves equal emphasis: query complexity charges access to chosen coordinates, so the algorithm does not pay for initializing or reading the whole explicitly addressed table.

### §4.3–4.8: examples, local tests, and antecedents

The four-column Forrelation example is now properly limited: its circuit is synthesized from a finite truth table rather than obtained from the asymptotic construction. The later XOR toy changes the partial function as well. Both are legitimate, but the record asks the reader to learn two boards and two indexing conventions. I wanted a short purpose map before the second board: the first isolates semantic checks, the second makes the planted coupling and capped simulator transparent.

The second finite board, where the domain test is the only failed condition, is a strong improvement. It proves why that check is present. The first board alone would not isolate it because other conditions already disqualify the relevant column.

The detailed arithmetic for the loose local-test coefficient temporarily pushes the main equivalence out of view. For the classical route, circuit size does not matter. For the quantum route, the growth rate and the provenance of the explicit later constant matter more than this local expansion. The calculation should remain available, but its position can better reflect that hierarchy.

The pointer support remark is correctly marked as a remark and kept off the first route. The distinction between adaptive query depth and the set of all coordinates on which a test depends is exact. The winner-versus-rival comparison is another strong point: the event inclusion needs correctness only from the winner's decoder. It does not assume that an unpromised rival behaves coherently with a nonexistent promise value.

The historical discussion of direct pointers is accurate but compressed. Earlier pointer constructions worry about the cost of an entire pointer collection as one alphabet symbol. Here the algorithm accesses a selected field, paying for its Boolean bits. Explicitly connecting those two statements would explain the design choice better than the fact of Boolean encoding alone.

### §6 opening and §6.1: direct product

The generic lower-bound theorem is the right entry point. It makes clear that this chapter needs a hard partial function, a realizing circuit, and a suitable budget; it does not need the analytic Forrelation proof or the circuit-size estimate.

The direct-product prelude is nevertheless long enough that the particular hard distribution disappears from view before it has been introduced. There are two proofs, the cap-event corollary, a worked adaptive example, the normalization identity, and a literature comparison. These materials belong in a complete record. The first route needs a more precise interface through them so the construction-specific argument remains the main path.

The conditional-value proof survives close inspection. The conditioning event for a fixed positive-probability execution factors into one consistency condition for each input. Adaptivity does not spoil that factorization once the history and independent external information are fixed. Bits inside a single input may be arbitrarily dependent, which the record explicitly says. The single-input hardness assumption is used at the root; later posteriors may be easier, and the continuation value accounts for that. The product has nonincreasing expectation because exactly one factor can change at a query, not because arbitrary products of supermartingales have that property.

The joint-independence warning for side information is excellent. The parity example shows why independence from each input separately is insufficient. The finite-behavior reduction also keeps arbitrary independent information from silently expanding the deterministic model.

The cap-event corollary has the correct logical form. It constructs an actual truncated algorithm and bounds success intersected with the cap event. The AND example then demonstrates that conditioning on the cap event can increase success and destroy the useful independence. Its deliberately redundant query is a teaching device; saying so before the calculation would help. The rectangle language suggests a small diagram or table of the selected rectangles, because that is the conceptual payoff beyond the numerical example.

The optional second proof now has a stated purpose: unnormalized weights handle zero-mass histories differently, and the identity shows that both versions calculate the same quantity. This resolves the earlier unexplained duplication. The remaining friction in the source comparison is notation: Drucker's \(k\), the number of instances, is set to \(r\), while this manuscript's \(k\) is the Forrelation order. The substitution is correct but should be labeled as source notation.

### §6.2–6.3: hard law, dummy input, and planting

The minimax argument is complete at the level needed here: finitely many bounded-depth behaviors give a compact convex set of success vectors, and separation supplies a distribution supported on the promise. The distinction from the analytic Forrelation hard measure is indispensable. Nothing in the planting experiment should inherit an unsupported coordinate-product assumption from the analytic argument.

The dummy experiment is the real center of the classical proof. All \(J_i\) are independent hidden zero locations; the address inputs are independent samples from \(\mu\); the cells are fixed blanks; and the selected column \(I\) is independent of the run. The prose contains all of this, but I wanted one compact dependency table to hold it while reading the simulator. In particular, addresses are functions of the \(A\) inputs, not another independent family of random variables.

The XOR toy is correctly advertised as generic and nonasymptotic. Its zero-based indexing differs from the earlier board for no mathematical benefit. The first-difference coupling is sound: it is enough to overcount every query to the selected cell, even though some planted bits may equal their previous blank values.

### §6.4: erased zero

The identity involving the number of discovered columns uses the independence of \(I\), not merely a uniform marginal. The selection example makes that distinction concrete. I would preserve it even if optional search refinements are shortened.

The early/late argument is adequate for the advertised discrepancy constant. The alternative search estimates are correctly labeled as refinements; none is needed for the exponent. Reusing \(Z\) after it denoted the product potential is a small but unnecessary memory cost. Referring to “the baseline” is also project vocabulary rather than mathematical explanation.

The formal endpoint's independence from promise support and hardness is a good boundary. Equation (19) is about the independent zero-location experiment. Hardness enters when predicting an address, not when counting discovered zeroes.

### §6.5: the simulator and query accounting

This is the strongest part of the detailed lower-bound exposition. Heavy means more than \(L\) queries to all address-input strings of one column in total. The capped simulator therefore has a total \(L\) budget, which automatically implies the separate cap on every one of its \(r\) instances. The proof does not confuse a total \(rL\) budget with these caps.

The simulator's side information includes all zero locations, even \(J_i\), but excludes the target \(A\) tuple and its address. That is allowed because the zero locations are jointly independent of that tuple. The surprising inclusion of \(J_i\) deserves one explanatory sentence; otherwise a reader may think the reduction has handed itself the very hidden object it is trying to find.

The output address is extracted from the coordinate of a prospective query, before the cell contents are read. This is the decisive observation. It establishes a predictor without granting access to the planted certificate.

The proof then bounds the fixed-time joint event and takes a union over times. Averaging over the independently selected column cancels the apparent factor \(m\). These are the exact facts missing from the opening shorthand. The second cap-conditioning counterexample is correct, but it should explain its different role from the earlier AND example: this one mirrors the simulator directly.

### §6.6: discrepancy and floors

The discrepancy assembly is correct. Heavy columns, erased-zero discovery, and cell prediction are charged separately; the chosen constants leave a gap below \(1/3\). The random-mixture argument then contradicts bounded error. The finite \(m^{-10}\) tail estimate is the most direct justification of the generic theorem over its advertised range, so it should precede the asymptotic \(o(1)\) discussion.

The floor accounting is worth retaining. Positivity and the range \(t\ge8\) are checked before floors are absorbed. The final lower bound uses the same realizing circuit as the upper bound. What is still missing pedagogically is a compact account of where losses occur: the planting step preserves \(mL\); the address length defeats the time union; floors cost constants; the chosen Forrelation budget introduces the displayed logarithmic loss.

The paragraph about old Lean core theorems interrupts the final mathematical calculation. The information belongs in G.8, where signed and absolute discrepancy endpoints can be compared without breaking the proof.

### §7 and the statement catalogue

The fixed-\(k\) exponent argument is precise about strictness. It rules out exponents below \(4-2/k\), not the endpoint, because the logarithmic denominator remains. The opening and this section duplicate much of the same ratio argument; the opening can retain the conclusion and purpose while the full calculation stays here.

The growing-\(k\) subsection uses uniform estimates, so it is not the invalid substitution of a varying parameter into a fixed-parameter asymptotic statement. The competing terms \(40k+\ell/k\) explain the square-root scale and should motivate the schedule before it is chosen. The range \(t\ge80\) is a validity threshold; where the displayed epsilon is at least four, the inequality is trivial. The explicit warning that this does not give \(\Omega(Q^4)\) should remain.

The catalogue has not caught up. It still says that no growing-\(k\) schedule is inferred, although §7.3 now derives one. It also refers to nonexistent §6.7. The generic theorem entry specializes to \(km\) input bits without a local \(k\) hypothesis, unlike the body. These are repairable indexing problems, but they obstruct the record's role as an audit destination.

### Appendices C–G

The edition-aware reference list is useful. The BSS entry should align its title with its CCC 2003 metadata rather than blend it with the earlier manuscript title. Appendix D explicitly redefines \(\ell\), but using it for \(k-1\) after the main text uses it for \(\log_2m\) makes comparison harder.

Appendix E is careful about the limits of source criticism. Its comparison of two upper bounds is not presented as a counterexample to Bansal–Sinha's theorem. Its SSW transfer isolates the Fourier-growth input rather than claiming a distribution theorem transfers unchanged. These are important strengths.

The execution history and formal-evidence appendix are now separate, which is the right architecture. Residual snapshot language still creates friction: “current integration,” an absent helper receipt, later compared endpoints, and “names listed above” need explicit dates or referents. G.8's “finite-behavior reduction above” also needs a section link for a reader entering the appendix directly. None of these comments claims that a supplied receipt failed or that a new formal run was performed.


## Supplemental reading log: the Forrelation supplier, quantum proof and universal upper bound

These notes supplement the lead expert-companion log and the classical-record log. They describe the current Markdown. The supplied record PDF is an older reading edition, as SOURCE_STATUS.json already discloses. No statement below treats that known condition as a new finding. The notes distinguish a first reading difficulty from a difficulty resolved by consulting another section.

### Record §3, entry and §§3.1–3.2

The entry now tells me what the construction consumes: a hard partial function, a coherent decoder with an all-input cap, and an exact domain-and-value circuit. That is the right abstraction for a lower-bound specialist. I do not need to read the circuit census to understand the planting reduction. The current skip instruction says so explicitly; the previous complaint about an unavoidable circuit detour has been repaired.

The one-sided promise is stated unusually carefully. A large negative Forrelation value is outside the promise, even though the projection experiment sees its square. I checked that the circuit and the quantum routine are being asked to do different things on such an input. They are: the circuit rejects domain membership, while the decoder may produce either bit. The distinction is consistent with the later total function. This should remain visible in every shortened account.

The numerator explanation also earns its length. The path expansion identifies an integer, and the backward Walsh recurrence computes that same integer without enumerating m^k terms. The denominator is integral because m is a power of four. The sign convention, number of Walsh factors and positive denominator are all placed where the exact comparisons need them. This gives a reader a recoverable route from the analytic promise to Boolean predicates.

### Record §§3.3–3.5

The quantum proof makes the phase-query implementation explicit and applies the matrix word in the correct order. The fixed cap on unpromised inputs is an algorithmic property, not an assertion of correctness there. That is exactly the contract later comparisons need. I would add only a short three-block index trace if this section is meant to be entered independently; no additional quantum machinery is missing.

The gate construction is a reference destination. Its numerical census is too detailed for the lead companion, but appropriate here provided the shorter route stops at the contract and size bound. I checked that the later count uses the transcript length as a number of local tests, rather than charging the whole circuit as quantum computation. Query complexity makes that distinction possible.

The small instance separates several plausible confusions: true bits represent negative signs, the yes promise is one-sided, and projection probabilities square the signed quantity. The enumeration is useful as a calibration of these choices. It should not be sold as empirical evidence for the asymptotic randomized lower bound. The section itself explains that the negative example passes the projection while failing the domain circuit. This supplies the diagnostic purpose, so no separate missing-purpose finding is retained.

### Record §3.6

There are two legitimate routes: import the published fixed-k supplier for the construction, or read the record's independent quantitative derivation. The distinction is now available early. I checked that the import is Bansal–Sinha's explicit Walsh promise, with the relevant thresholds, rather than the random-orthogonal rorrelation theorem. The source allocation is correct in the present draft.

The full proof outline motivates the modified algebraic truncation before deploying it. That is a successful repair. The reader should not be sent back to an earlier review's complaint that the truncation has no stated purpose. The remaining issue is allocation: a specialist should learn the power balance and the off-promise acceptance bridge as clearly as the precise constants.

### Record §§3.7–3.8

The multilinear extension is defined as an expectation under independent biased signs, then extended algebraically to real biases. This order clarifies the two meanings without conflating them. The centered character divides by 1−μ_i²; the later bound |μ_i|≤1/2 keeps it bounded. The raw derivative convention is essential. It is not an orthonormal biased Fourier coefficient, and a derivative at a nonzero bias is not merely the kth uniform Fourier level.

The bounded Gaussian identity supplies both the centering relation and usable numerical bounds. I followed the purpose of the two auxiliary functions: their identity permits an integration step that removes a bias factor, while their uniform product bound makes the eventual path sum small. The introductory purpose sentence now prevents the formula from appearing to be an arbitrary trick.

### Record §§3.9–3.10

The chain is constructed from independent underlying Gaussian vectors. Correlated pairs are obtained by applying the Walsh transform; the proof does not need a density for a singular pair. The zero endpoint is obtained by the stated reflection argument, and only the first block is interpolated. These are precise choices, not interchangeable variants of a generic Gaussian interpolation.

I slowed down at the general derivative transfer, then found the three-block calculation genuinely useful. The same middle coordinate is selected twice in the path notation, but the polynomial differentiations select one coordinate in each labeled block. The dangerous same-block second derivative vanishes by multilinearity. Earlier weights depend only on earlier Gaussian vectors, so differentiating the next independent vector does not create extra derivative terms in those weights. The record states this invariant explicitly. It is the sentence I would preserve if the general proof were tightened.

A notation problem remains: ℓ is reset to k−1 although elsewhere it is log₂m. This is harmless inside the local derivation, but inconvenient precisely when comparing the k-dependent estimate with the later schedule. A reader should not have to translate the same letter twice when reading a quantitative lower bound.

### Record §3.11

This is the hardest interface for a new specialist reader. The derivative sum is rewritten as a leaf expectation of a polynomial in revealed centered variables. Querying a fresh coordinate changes this polynomial by a centered factor times a contracted coefficient array of one lower degree. The coefficient class remains bounded, allowing induction. Repeated queries do nothing, and terminated paths are padded without changing the process.

I checked the distinction between conditioning on a node history and conditioning on a future event. A node history fixes queried coordinates and leaves fresh coordinates at their original product law. A future event that a process never crosses a threshold need not preserve that law. The text uses stopping for the latter task. That is the right distinction, and it parallels the cap-event issue in the classical planting proof.

The proof would be substantially easier to retain after one worked r=2 update. A reader could then see what the contracted array is before reading its general definition and the stopping estimate. This is an example request at an existing inference, not a request for another theorem. The comparison with Girish–Tal–Wu supports that pedagogical choice: their ordinary-tree discussion begins with low-degree behavior before explaining the more general process. The source's theorem should not be described as already containing the record's exact bounded-bias raw-derivative statement.

### Record §§3.12–3.13

The path-to-set map is injective because each coordinate remembers its block. Consequently there is no k! loss. The absolute Walsh factors contribute m^−(k−1)/2, and the degree-k derivative bound contributes a leading d^(k/2). At this point I expected the text to say explicitly that their balance yields d on the m^(1−1/k) scale. Instead it points directly to the later numerical assembly. The formula is correct, but its explanatory payoff is delayed.

The moment calculation then does the right separate job. The uniform law has a small second moment, while the rounded law has positive first moment. Neither observation alone says that the rounded law is supported on the promise. The text preserves this limitation and supplies a different bridge in the next subsection. The one-sided yes threshold is used there; it is not merely a naming convention.

### Record §§3.14–3.15

The pointwise acceptance inequalities are the heart of the promise-hardness deduction. On the promise they use correctness; off the promise their bounds remain valid because acceptance lies between zero and one. Taking expectations then produces a signed acceptance gap from the two moments. This gives a complete answer to the question left compressed in expert §5.

The exponentially small useful mass explains why error 1/3 is inadequate. Amplification to error exponentially small in k costs O(k) repetitions, and the padded depth handles the zero-query boundary. I would introduce the small-gap motivation before the majority calculation, so the repetition count is a response to a known need.

The final finite estimate is useful, especially because its k-dependence supports the growing-parameter discussion. I followed the source of the two powers of k: one enters the derivative estimate, and one enters through the amplified depth. The exact denominator and threshold are less informative than that decomposition. A short explanation of these losses would help the reader see what the optional refinement buys without changing any bound.

### Record §§3.16–3.18 and Appendix E

The current credit is specific. Bansal–Sinha supply the explicit promise, Gaussian-chain antecedent and transformed integration-by-parts antecedent. Girish–Tal–Wu supply the ordinary-tree martingale strategy. SSW's Fourier-growth theorem is used in the separate Appendix E comparison. The record proves its own altered distribution's identities rather than importing a promise-mass result for a different law.

The version-specific logarithmic comparison in Appendix E is bounded correctly. A mismatch in a displayed substitution is not a counterexample to the cited theorem. The record explicitly says so. That distinction must survive any further compression or discussion of priority. I did not treat a localized source concern as evidence that the separation theorem fails.

There is now some repetition among the theorem preview, the detailed credit section and the final source subsection. The detailed account should remain; one of the surrounding summaries can become a compact location index. The common-witness conjunction in §3.17 is useful and should not be cut with the repetition.

### Record §5.1

The successful state is preserved through the Grover rotation, and the fixed number of fresh randomized trials gives a branchwise cap even when the success probability is tiny or zero. Keeping the workspace is necessary for inversion. The ordinary proof explains these requirements rather than relying on the phrase amplitude amplification.

The reading prose still names internal claim keys. Those keys belong in source markers and the correspondence apparatus. A mathematical reader needs the formula and its role; they do not benefit from learning a maintenance identifier. This is a residual issue after the broader relocation of formal apparatus, not a request to remove that apparatus from the record.

### Record §5.2

The complementarity identity handles cycles and fractional comparisons. The successful preparation samples the ideal weights without computing them. I checked that the coupling charges possible disagreement only until the winner is selected; later failures cannot remove it from the list. The failure law can depend on the full history. The coupling's independent Bernoulli variable is constructed from the output law and does not add an implementation assumption.

Two reading problems remain. The return instruction names companion §4.2, which now concerns planting; the tournament is §3.2. Also, the sentence saying that the compiled law follows from the successful-state assertion should distinguish ordinary implication from actual formal dependency. Appendix G.7 has the needed distinction, but an entrant here can read the sentence too strongly before reaching it.

### Record §§5.3–5.5

Fresh decoding followed by exact local tests is the correct way to verify a candidate. Every address of a loser has a failing test, so arbitrary off-promise decoder outputs cannot create sound accepting certificates. On a true winner, correct decoding leaves no failed test. The one-input and zero-input error accounts use different events and are kept separate.

The explicit query budget belongs in the long record. It resolves controlled accesses, reversibility, pointer-bit charges and all-input caps. The companion can cite this destination while spending more of its limited space on the classical simulator and the promise-gap bridge.

The alternate formal route initially sounds like the same sequential verification procedure. The following text resolves the question by naming the Boolean continuation and the difference in the statement being tracked. That explanation is already present; no separate missing-interface finding is retained.

### Appendix A

The universal bound is a separate established result, correctly separated from the new construction. The adversary progress argument, star example, sensitivity graph, maximum-degree face and maximal-monomial tree form a coherent proof. The dimension argument on the signed cube is the part that deserves the most explanatory attention. The final multiplication of constants is routine by comparison.

The Midrijānis step makes a subtle point explicit: all disjoint sensitive blocks are sensitive at the same original full input. Each restriction preserves the relevant maximum-degree coefficient. Without the common input, the block-sensitivity bound would not follow. This is a successful example of expanding the right inference.

The adversary-prefactor discrepancy is carefully localized to a printed coefficient and its cited edition. The older annex transcription story is maintenance history and can move to Appendix F without weakening the mathematical comparison. No author-confirmed erratum or optimality claim should be inferred from the record's finite witness.

### Appendices B and G, sampled correspondence route

The catalogue was sampled as a navigation and scope aid, not independently re-proved declaration by declaration. G.1–G.7 and G.9 were read for the model/proof boundary, with the classical G.8 reviewed separately. The three universal-bound routes have different coefficients and different dependency roles; the table states that distinction well.

The missing general physical-state bridge is explicitly not an assumption of the measured-label upper-bound proof. That distinction is important to retain. Likewise, G.9 identifies the compiled uniform quantum estimate while labeling the remaining growing-k optimization ordinary mathematics. Neither point should trigger an unsolicited request for more formalization. The review's task is to make the existing claims readable and accurate.


## Exposition: sequential reading notes

This log records an agent review from the perspectives of a mathematically literate newcomer and of researchers concerned with totalisation, certificates and randomized lower bounds. It is not a report of a human learning experiment. I read the current exposition in full, compared its classical argument with the expert companion’s Section 4, consulted the relevant earlier dispositions, and inspected the four supplied exposition SVG figures and selected pages of the supplied PDF. The notes below collect the first-use difficulties and the later passages that resolve them. They do not claim that any manuscript, Lean proof or receipt was changed or rerun.

### Introduction: the question is clear before the object is

The opening does useful work immediately. It defines a query, distinguishes the randomized and quantum access rules, and fixes a worst-case cost convention over every input and every random or measurement branch. The partial-versus-total distinction then gives the result a real question: how much of a large partial-function speedup can survive when the algorithm owes an answer on every bit string? I can read the theorem as saying that no universal exponent below four works, while four does work. The dependence of the constants on a fixed k is visible rather than concealed in the headline.

The first difficulty is the density of the entrance. Before seeing one input, I have a formal infimum, exact logarithmic powers, a circuit-bearing certificate, an address obtained from several partial-function values, a planted pair, a direct product, an earlier AND-OR composition and a substantial prerequisite list. The supplied PDF makes the cost visible: the introduction occupies roughly two pages, and the explicit audience arrives on the second. The theorem and the simple exponent arithmetic deserve the early position. The numerical provenance and the detailed old-versus-new construction comparison could wait until the board gives these words something to refer to.

The heuristic line also needs more careful direction. An upper bound on Q and a lower bound on R suffice; the approximation signs make it easy to remember matching estimates instead. More consequentially, the closing account of a classical algorithm paying to learn addresses sounds like a compulsory sequence of actions. I noted that a classical algorithm could instead guess an address, or visit many cells. Section 5 does answer that objection correctly. The introduction should plant that expensive-versus-lucky distinction, so the eventual proof sharpens the first picture rather than replacing it.

The historical paragraph is useful because it distinguishes deterministic-versus-quantum pointer separations from the bounded-error randomized problem. The AND-OR paragraph is better than a list of records: it says why small certificates were useful and where the cubic accounting arose. That is worth keeping. The audience paragraph, however, declares a graduate student already familiar with the quantum and classical tools. The packet fixed a broader newcomer audience. This is not repaired merely by accurately listing what the present draft assumes.

### Section 1: the small input earns its place

The bit-to-sign convention is explicit. The common second block lets me check three inner products without repeatedly multiplying unrelated matrices. The negative case is the important one: the partial function owes no value there, but the squared-amplitude experiment accepts it just as confidently as the positive case. This gives the future domain bit a concrete job.

I slowed at the statement that H preserves length. For someone who knows elementary linear algebra but has never met Walsh transforms, the displayed four-by-four matrix is enough to verify that claim. A short row-orthogonality observation would be more useful than importing the transform’s name as background. The quantum phase-oracle operation also remains an assumed operation; the geometric calculation itself is accessible, but converting one bit-oracle query into all the input-dependent signs has not yet been taught.

The projection experiment is carefully qualified by the additional input with Phi equal to one half. That is a valuable repair: the first three cases do not establish an exact decoder on the whole promise. The phrase that one run “decides” all three is nevertheless loose because one of the three has no value of P. The mathematical data are fine; the decision language crosses the very domain boundary the example is intended to teach.

The census of 104 positive, 48 zero and 104 unpromised inputs feels less useful. I understand the positive/negative symmetry, but the exact counts do not advance a subsequent calculation. The explicit statement L_{2,4}=0 is important and correct: it tells me that the small board is not a nontrivial instance of the quantitative lower bound. This distinction later makes the claim that there is no hard distribution at m=4 stand out as too strong.

### Section 2: the total function becomes tangible

The sentence allowing every assignment of every input bit is essential. It prevents me from assuming that transcript fields are honest certificates supplied by the definition. There may be false gate values, meaningless labels and unhelpful pointers; the function must still have a definite output.

The four winning conditions are conceptually manageable, but their semicolon presentation makes their individual identities harder to retain. They recur as four families of tests and as separate failure mechanisms. Stable visual clauses would help both the newcomer and the later formal-definition callback.

Figure 2 is a successful concrete object. Its X strings have four positions, in agreement with m=4. This exposition figure must not inherit the separate dimensional complaint about the expert companion’s graphic. The blue outlines distinguish true cells in losing columns from a winning cell. Figure 1 is a schematic illustration, not another numerical four-position board; its different drawn width is not itself a contradiction.

The circuit transcript paragraph explains the right invariant: the circuit is public, proposed values are input bits, and satisfying all local equations forces the actual evaluation in gate order. The domain-bit counterexample is the strongest part of the construction lesson. It keeps the pointer and value checks successful while making only the promise certificate fail. A reader can identify the necessity of the domain condition rather than merely observe another negative input.

I wanted one gate test worked at the same resolution as the pointer test. The latter names its two pointer bits, its selected string bit and its three-query cost. The former is described abstractly, even though it is the part likely to be unfamiliar. The exact 180-gate and 371-test totals do less to explain this local access than one actual gate equation would.

The source comparison raised a different issue. The pointer-functions paper does discuss direct pointers to all other columns, but rejects that option in its representation because the alphabet becomes exponentially large. Its actual construction uses a balanced tree. The current attribution is not invented; it omits the old objection. Explaining what is different about indexed, bit-level access here would help both credit and mechanism.

The large addressed array also needs a resource explanation. Polynomial size is relevant, but m to the twentieth power is not obviously benign to a newcomer. The paper should connect it to the final input-length expression and to what a query complexity separation does and does not charge for. In particular, choosing a query position is different from reading a stored pointer value.

### Section 3: a good interface with uneven teaching weight

The three supplied properties are the right modular interface: cheap quantum decoding on the promise, an exact domain-and-value circuit on every input, and a classical lower bound. The final sentence that both bounds use this same function and this same circuit is important. It prevents a modular proof from quietly changing the object between its two halves.

The weighting is less successful for the stipulated audience. The arithmetic-circuit sketch introduces integer thresholds, a fast Walsh transform and ripple-carry arithmetic, while the source of classical hardness receives essentially one theorem statement and a citation. I would not ask this exposition to reproduce the analytic Forrelation proof. I would ask it to state its lesson boundary and give the reader a clear description of the indistinguishability problem supplied by that theorem. A precise accepted input is better than either pretending the bound is obvious or opening a second research-level proof.

The exact circuit-size contract is enough for the later test count. Implementation vocabulary that neither teaches the construction nor permits its verification can go to the record. The quantum route similarly needs the small phase-kickback operation at the point of use, or a precise statement that this particular oracle conversion is an accepted primitive.

### Section 4: the construction-specific ideas are strongest when the subroutines recede

The nested-Grover obstruction is an excellent opening. It makes the obvious algorithm cost m rather than square root m, so the tournament has a concrete purpose. The two failure examples then answer different natural objections: a dominating column need not win, and losing columns need not admit any total order. They justify both the unusual search analysis and final verification.

The ideal-process paragraph explicitly says the algorithm does not know or estimate its weights. This is exactly the distinction I needed before the weight update. The table, the pairwise cancellation in the drift identity and the absorbing zero-weight state make the analytical process understandable. The four-column run remains deterministic, though. It teaches a surviving subset very well; it does not itself teach genuinely fractional weights. A pointer to the already available fractional example at this point would make that limitation explicit.

The sampler explanation contains the key bridge: fresh work registers give a product of comparison probabilities, and amplification preserves the direction of the successful state, hence the conditional column law. That is worth real proof space. By contrast, the long numerical amplification recipe interrupts the construction with 19/40, 9/40 and the exact logarithmic trial count. Earlier dispositions said these constants would leave the main exposition, but they are still here. The reader needs the capped contract and its applicability on zero-success inputs; the standard constant calculation can be optional.

The failure and stopping explanations are good. Before the winner is listed there is sufficient mass; after it is listed, sampling may fail without removing it from the list. No-winner inputs and an empty list are addressed. The sentence that every number of trials and iterations is fixed in advance is nonetheless wrong literally. Iteration counts are random and executions stop early. Their upper caps are fixed. That distinction is how a random, adaptive procedure meets the worst-case convention established at the beginning.

The answer to Question 2 introduces a separate small error. A particular pivot preparation with success probability one quarter becomes certain after one Grover iteration. The final verifier is still a bounded-error search over local tests. The fact that columns 2 and 4 have failed string tests does not mean the stated verifier rejects them on every branch. The exercise has silently transferred exactness from one part of the toy to another.

### Section 5: a real lower-bound proof, with two important local repairs still needed

This section does substantially more than assert that an address is hidden. It constructs a common hard law, draws the dummy input, chooses an independent planted column, couples two executions, and separates the erased-zero and true-cell events. The convention that both events refer to the dummy run is explicit and essential. The observation that a queried filled bit might equal its blank value correctly treats the visit event as an overestimate.

For a newcomer, Yao’s role needs one more sentence: a single distribution defeats every capped deterministic tree. A separate difficult input for each tree would not supply independent instances for the later reduction. Likewise, “blank” should mean a particular Boolean pattern, as it does explicitly in the expert companion.

The m=4 warning overshoots. There is a zero-query hard law on the two opposite-valued promised examples. What is missing is a positive budget that makes the generic lower-bound application useful. The drawing can still illustrate the locations changed by planting; it should not deny existence of the distribution itself.

The erased-zero argument has the most serious local wording issue. To say that the next unread position finds the hidden zero with probability at most 2/m, condition on the entire preceding history, not on the completed transcript. The expert companion’s “given the past” expresses the correct temporal object. The intended estimate is standard and supported; the concern is that the exposition currently instructs the reader to condition on future information.

The independence example is strong. It shows that a marginally uniform I can be heavily biased toward discoveries by its dependence on the run, and defines the no-discovery case too. This is a genuine teaching gain, not a warning appended without evidence.

The true-cell paragraph explicitly allows guessing and visiting many cells. The separate-cap direct product, its adaptive history factorisation, and the AND example where one conditional value rises are all helpful. The joint-event counterexample then shows exactly why conditioning on staying light is invalid. These repairs should be retained and not reissued as unresolved complaints from an earlier round.

The simulator is the remaining weak teaching transition. The prose states the correct construction, including free independent side information, the total L cap, and an output read from the chosen query position. But the only executed trace is in the record. This is the operation that turns a cell visit into a valid predictor, and it is the hard inference the learner should be able to reconstruct. The existing short XOR trace could supply a stopped run and a run that reaches its selected slot. The fallback output deserves a sentence too: it makes the predictor total, and its accidental successes can only enlarge the probability bounding the event.

The three-budget paragraph is now especially good. It separates G globally, L in one column, and L per instance, then states why the stronger total cap implies the theorem’s separate caps. The final average over I would benefit from one displayed sum so the learner sees why no extra m appears. The closing contradiction also needs the elementary all-input bridge: acceptance at least two thirds on every planted positive input and at most one third on every dummy negative input forces an average gap of at least one third. These small lines would complete the transition from a distributional experiment to the claimed worst-case lower bound.

### Section 6: the endpoint lesson needs internally consistent exercises

The order of choices is clear: choose a target exponent, fix k, then let m grow. The artificial threshold t≥2^k is a useful logical example of why a growing k cannot simply be substituted. The monotonicity reason for replacing Q by its upper bound is also explicit.

The phrase that k=2 gives exactly the cube is too loose beside this careful argument. It identifies the polynomial threshold, not an attained endpoint bound after logarithmic losses. Question 4 repeats the endpoint confusion more sharply. Choosing k=5 is valid under the displayed strict recipe. But the assertion that k=4 does not suffice for the stated goal α_tot≥3.5 is false: that family excludes every smaller exponent and therefore proves that lower bound on the infimum. It need not exclude the endpoint inequality itself. The question and answer should choose which of these two tasks they are testing.

The floor calculation can provide its second elementary check if its constants remain in the lesson. The unrelated explicit constant 35^4 in the matching upper bound has no subsequent teaching role and can stay in the record.

### Section 7, answers and attribution

The formal statement paragraph correctly says that its family theorem leaves the logarithmic power unspecified. This is an important scope distinction from the quantitative headline. The best newcomer invitation is the next paragraph’s concrete check of the domain clause against the changed board. That is an action with a reason. The many separate definition links in the preceding paragraph are less helpful without a comparable local question.

The exercises are useful but do not test the central capped-predictor reduction. Success at all four could coexist with misunderstanding the true-cell lower bound. Retargeting one task to the existing simulator example would assess the intended classical payoff. This is a recommendation for a teaching task, not a claim that a real reader has already passed or failed it.

The closing attribution separates OpenAI’s theorem and construction from this exposition and its formal development. It should remain. The overall verdict is that Section 5 contains a genuine lower-bound argument and several excellent examples; the priority is to make its one essential simulator operation executable for the stipulated newcomer, while repairing the literal conditioning and endpoint errors and trimming unrelated subroutine detail.
