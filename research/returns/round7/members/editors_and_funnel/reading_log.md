# Reading log

These notes preserve the section-by-section reading sequence of the three document reviews. The four perspectives are emulated analytical roles, not independent human reports and not opinions attributed to the literature's authors. Each document had a complete current-Markdown reading; subsequent literature and visual checks are identified in the component logs and source inventory. Reactions such as “I slowed down” describe the recorded analytical reading, not an empirical reader study.

The input packet identifies the record PDF as older than its Markdown. Record findings use the current Markdown. The two shorter supplied PDFs were visually sampled; no new manuscript PDF was generated. Selected claims were then followed into the available formal sources, as reported separately in `claim_journeys.md`.

## The expert companion

This log records the order of the specialist-paper reading and the points at which the text created or discharged an expectation. I read every paragraph of the current Markdown. I then inspected the supplied PDF text and viewed pages 1, 3, 9, 11, 12 and 14, and checked the two figure source files. I used the earlier dispositions after the first reading to distinguish persistent issues from issues already repaired. No Lean build, Comparator run or new manuscript rendering was performed.

### Title, subtitle and abstract

The title tells me the result immediately. The subtitle makes the companion relationship clear, which I need because the author line and headline theorem otherwise invite an authorship assumption. The abstract also gives unambiguous credit. I would preserve that.

My first pause is scope: total Boolean functions appears in the abstract but is absent from the title. My next is k. I see the final exponent 4−2/k without being told in the abstract what k represents or how it is chosen. I can infer the role after reading the paper, but the abstract is asking me to use information I do not yet have.

The mechanism is present. I can identify a certificate address that is classically expensive, and a search over columns that is quantumly cheap. I want the next paragraph to tell me what is special about the total construction. Instead I retain two unresolved questions: whether the classical “cannot locate” sentence means a hard-distribution guarantee or a universal execution claim, and how much of the argument “complete” promises this document will print.

### §1: definitions, theorem and contribution

The opening gives the conventional complexity parameters and a fixed query cap. The oracle makes the quantum access precise. The sentence about reading one bit at a time is less satisfactory as a description common to both models; coherent access is the whole difference the next sentence formalises.

The infimum defining alpha_tot is clear once parsed. I have not yet been given the historical range of possible exponents, so it feels like a formal definition ahead of the question rather than a natural summary of it. The added-one convention is harmless and the uniform C_alpha is important. I would keep the latter visible.

The theorem tells me what family and estimates to look for. I notice that b_k has no declared range, although a later explicit value resolves that. The paragraph after the theorem explains the quartic universal upper bound and the cubic conjecture well enough. In particular, fixing k=3 to rule out the cube is immediate.

The following contribution paragraph slows me down sharply. It contains four exact constants or thresholds, same-circuit consistency, a promise of a full argument, two observations about antecedents, a uniform Forrelation statement, a growing-k family, and Lean. I cannot rank those contributions from the presentation. I expect the column mechanism next; I am instead being asked to catalogue the companion's outputs.

### §1.1: earlier separations

This subsection is useful because it derives the old exponents rather than simply naming them. The arithmetic 2+c makes the cubic bottleneck of the particular AND–OR recipe intelligible. I note the careful restriction to that recipe; it should survive editing.

The order of one assumption is awkward. The displayed quantum cost has already dropped Q(g) before the text assumes Q(g) is polylogarithmic. Reading the passage generously repairs the scope, but a specialist checking the formula should not have to do that.

The chronological table is compact and useful. Its heading uses R=Q^a for bounds that are lower separations, then includes a universal upper bound as the final entry. I would use it as a map of historical progress only after mentally correcting the direction of the statements. That is avoidable.

The Ben-David credit is present and the earlier dispositions confirm that this was deliberately repaired. I would not raise the old omission again.

### §1.2: overview of the construction

I now get the construction I expected: m columns, a data string, hard address blocks and a separate cell for each answer vector. The first address sentence writes P(A_i,h) for every column without immediately mentioning undefined values. Since this is a total function, I expect the promise failure case to be stated near that definition. It does appear correctly later.

Figure 1 gives the useful dependence: hard address blocks select one cell, and that cell's pointers disqualify every rival. This is a good object to picture. On visual inspection I notice that the figure labels the blocks independent. I have not yet been given any distribution; this must mean disjoint input coordinates, while later independence will mean something stronger.

The coupled-input overview identifies the two differences. I first read “two places” as two changed bits, then remember that filling a cell changes a block. The subsequent probability events use the right interpretation.

The hardness-scale paragraph describes the right counting argument, including the idea that a cell query names an address by its position. That is much better than simply asserting that a classical algorithm must compute the address. I have to treat the approximate equalities as exponent heuristics rather than established tight characterisations of R(P).

The quantum paragraph is the most compelling part of the overview. It tells me why nested verification would cost too much, what a pairwise comparison actually reads, why the genuine winner is protected against unpromised opponents, and why arbitrary loser comparisons must be allowed. I now know what theorem the next quantum section needs to deliver.

### §1.3: predecessors and roadmap

The cheat-sheet lineage is clear. The next paragraph distinguishes back pointers from the present direct pointers, but the move from one old function to its no-back-pointer variant needs clearer nouns. “Their functions” is too broad at the exact sentence that is supposed to identify the earlier tradeoff.

The explicit Walsh form is connected to the circuit requirement. That connection is useful, because a partial query separation alone does not explain how to verify promise membership cheaply.

The comparison-search paragraph introduces many near neighbours. I can follow it, but I want the closest mathematical relation sooner: an indicator of survival becomes a product of probabilities. That finally arrives in §3.2. It would be a better organising centre for this paragraph.

The closing roadmap is crowded. I learn which arguments are cited and which are proved here, which answers my abstract-scope question, but this answer arrives after almost four pages of introduction. The same paragraph also tells me what other record links mean and where the exposition is. I would prefer a simple route into §2 and local explanations at the citations.

### §2: Forrelation and the total function

The definition of Phi and its one-sided promise is precise. The explicit warning about large negative values matters. I can see why m is a power of four when the integer numerator is introduced, but a brief purpose at the initial parameter declaration would have prevented that small wait.

The three properties provide the right interface. Property (ii) is carrying a contract and several implementation remarks together. The projection statistic, the coherent decoder and the alternative interference test are all compatible, and the text correctly says the exact circuit checks the domain separately. I would retain that distinction while giving the contract its own clean sentence group.

The cell definition makes totality clear. I have a minor question about the convention for S: the exact input-size and test-count formulas use S as the number of stored gate bits, so that convention should be stated. The uniqueness argument is correct but expresses its contradiction indirectly.

The input-length exponent feels like a detour. I want to understand the local tests and how they become quantum verification. The all-address failure statement then gives me exactly the needed guarantee. I mark it to preserve.

### §3: amplification before the tournament

The section announces the new tournament immediately, which helps. It then spends a long proof sketch on bounded amplification. I understand why the procedure has a fixed cap and why the unknown-success-probability expected-time theorem is insufficient. The numerical trial constants and the rotation formula are more than I need for this paper's central proof.

The returned-state clause also catches my attention because the next sentence says only the measured label law is used. The formal section later distinguishes the two formal procedures accurately. My response is to simplify the main contract's presentation, not to claim the stronger state fact is false or unproved.

### §3.1: comparison circuit

The decoder is bounded even outside the promise; good. Sorting the unordered pair makes the probability complement identity meaningful. The tie rule and self-comparison convention are explicit. The orthogonal label registers explain why the coherent implementation has the same output probabilities.

The winner guarantee is exactly the invariant promised in §1.2. A bad opponent cannot put a zero into the winner's all-one string. A correct decoding of the winner makes its own pointer useful. I would preserve this short, concrete argument.

I notice a vocabulary burden: winning the total predicate, winning a comparison, defeating, being the victor and being dominant all occur nearby. The mathematical distinction is correct, but consistent verbs would reduce the later need to remind readers that dominance is insufficient.

### §3.2: the weighted tournament

Proposition 3 states the circuit-access assumptions and the probabilistic guarantee together. It is a long sentence. I would separate the interface from the probability conditions, because they answer different questions.

The explanatory paragraph is strong. The source's surviving set becomes w_i, and the algorithm samples with the desired bias. “Halves in expectation” should say at most half, but the intended mechanism is apparent.

The ideal process computes the expected weight by pairing terms. I check that W=0 is absorbing after early stopping so that “after T steps” is defined; this convention is implicit rather than stated. The winner's weight and Markov's inequality then finish the argument cleanly.

The exact sampling paragraph answers my main implementation concern. The algorithm does not compute weights. Independent fresh comparison workspaces give a product, and conditioning on the success flag normalises the masses exactly. This is the kind of displayed calculation the short companion should spend its space on.

The coupling paragraph handles history-dependent failure properly. I mark the dependence on the entire past and the harmlessness of failure after the winner has already appeared as non-negotiable details.

### §3.3: verification and cost

The need for verification is explicit, with a concrete counterexample destination. This is good: a dominant comparison candidate is a useful search output, not automatically a certificate of the function's value.

The wording about finding a failing test and accepting when the search fails is easy to reverse. I reconstruct the intended one-sided logic without difficulty, but the vocabulary could do more of the work.

The error budget is correct in structure. On zero-inputs any one of T candidate verifications might falsely accept. On a one-input it is enough for the included winner's fresh decoding to succeed, which explains why the final term is a single epsilon. I would add that short interpretation.

The loose logarithmic count is a slowdown. It expands details the section itself declares irrelevant to the final exponent. I would keep the resulting bound and a clean route to the exact calculation.

### §4: choosing the hard law

The lower-bound route is immediately visible. I know I will bound the chance of the erased bit and the chance of the filled cell.

The first paragraph also changes L from the specific floor in (5) to a generic threshold, explains compactness and invokes minimax. That is a useful general formulation, but it merits a paragraph of its own so the object mu is not lost inside the roadmap.

### §4.1: direct product

The unnormalised-measure proof is concise and well motivated. Restricting one factor while reducing its own budget makes adaptivity understandable. Joint independence of free information is explicitly required. I would keep these statements.

The source paragraph has a good correction: a global-budget theorem can also supply the required exponential tail. The alternatives and parameter substitution should be easier to separate from the core proof. The earlier dispositions confirm the old suggestion of incompatibility has been repaired, so that is a resolved issue.

### §4.2: planting and the hybrid inequality

The dummy distribution is a natural starting point. Its definition compresses several random choices and deterministic assignments into one sentence, so I read it twice to check the independence scope.

The picture is supposed to make the construction concrete. On inspection it is labelled m=4 but each row strip has eight bits. Positions five and seven cannot occur in [4]. I checked the source loop to establish that this is a real mismatch in the supplied picture rather than an extraction artifact.

The caption correctly says the address inputs are the same in the two panels. A graphic connection would help because repeated distribution labels visually suggest independent samples.

The first-difference inequality is the right reduction. Its qualifier specifying the dummy run is separated from the display by the floating figure in the PDF. That qualifier should remain attached to the bound.

### §4.3: erased-zero probability

The equality E[Z]/m is clear and its independence explanation is useful. The early/late argument is also short. I pause only at the conditional uniformity statement, which should explicitly concern a zero not yet found. Repeated queries to an already discovered zero do not contribute to Z.

The optional sharper estimate does not name whether it bounds E[Z] or the hit probability. Its scale tells me which is intended. Since it is unused, I would either remove it from this paper or put it in an explicitly optional sentence with its quantity named.

### §4.4: planted-cell probability

The operation at the beginning is excellent: a query position already commits to an address. The capped predictor then makes the intuition into a direct-product application.

The paragraph is dense because it contains the simulator, stopping convention, output convention, cap implication and useful event. I would divide it at the point where the algorithm has been fully defined. The aborted branch should explicitly output the fixed vector.

The joint-event sentence is essential. I would not compress it into a conditional-success statement. I also want one line showing that the average over the m possible planted columns cancels the m in the sum of fixed-column bounds. The final expression is right, but showing the cancellation helps the reader see the lower bound's factor structure.

### §4.5: contradiction and floor removal

The three terms in the discrepancy bound correspond to the two ways to see a changed input location, with the cell event split into heavy and light cases. The explanation of r and the slack constants is useful.

The move from pointwise correctness to the distributional gap should explicitly say that the success guarantee is averaged over each support. The current singular “zero-input Y^(0)” is slightly loose for a random variable.

The main proof ends satisfactorily at R(F)>floor(mL/100). The remaining floor-removal arithmetic is valid, but it changes the final emphasis from the mechanism to routine constants.

### §5: Forrelation supplier

The cited fixed-k estimate has already been stated in §2. The new role of this section is to distinguish it from a uniform estimate with explicit dependence on k.

The source comparison helps: I can see the different k and logarithmic dependence. The claim that the constants are “the record's” is less helpful than a direct description of the derivation and its credit.

The proof outline names many techniques and constants quickly. I understand that it compares two acceptance-gap estimates, but I would like that central conflict stated before the stopped-martingale terminology and the amplification depth. The distinction between the planted law and mu is explicit and should stay.

### §6: optimal exponent

This is the cleanest conclusion in the paper. Choose alpha, choose k, fix it, and let m grow. The displayed positive power of m beats the fixed logarithmic loss. I can audit the quantifiers directly.

The following growing-k remark is a separate optional result and now has a proper derivation in the record. Its long epsilon expression makes the paragraph heavy. The fact that the exponent tends to four is enough for the specialist companion's narrative. The endpoint caveat is repeated twice and could be stated once after both regimes.

### §7: formal statement

The current section is much more conventional than the evidence apparatus described in the previous review. There are readable links rather than hashes and commands.

It is still a long section. The useful mathematical facts are the relation between the standard and formal models, the common-circuit quantifiers, the existential logarithmic exponent in the main endpoint, and the separate explicit-constant result. The two unused constants in the universal upper bound and the full auxiliary-lemma correspondence dilute that message.

The measured and retained-state amplifier procedures are now separated accurately, and success together with compliance is distinguished from conditional success. I would preserve those distinctions in the long record. I would not turn them into additional warnings in the short paper.

The sentence saying the statements have no hypotheses “so” their proofs are complete could be phrased more carefully. The actual verification facts in the preceding sentence support the claim; absence of hypotheses by itself does not.

### End matter and Appendix A

The AI disclosure is brief but generic about the actual division of work. It should be factual without asserting review that did not happen.

The main OpenAI preprint reference lands at a repository root. A direct manuscript link would improve the first step of an audit.

Appendix A is worth keeping. Its examples explain why the delicate hypotheses appear in the main argument. The rows need labels because the body refers to them by number. Beta should remain an upper-bound parameter rather than becoming “the best” probability. The zero-cap example makes a good general point but should be labelled as a toy outside the L>=1 setting used in §4.

My final impression is of a paper with a convincing explanatory centre and too little restraint around it. The next revision should make that centre easier to reach, not append another layer of qualifications.


## The exposition

These are the reviewer's section-by-section notes from reading the current Markdown, then inspecting the corresponding supplied PDF pages and following selected destinations. They emulate a lecturer and copy editor; they are not observations from an independent student study. The first pass below records the difficulty before the later comparison material was used to diagnose it.

### Introduction, first paragraph: establishing what is counted

The classical description is understandable at once: choose a position, read a bit, use the answers to choose another position. The quantum oracle then introduces three registers and a superposition in the same paragraph. I can parse it as a quantum-algorithms reader, but I cannot infer that a mathematically strong newcomer can. The common unit of cost needs to be an oracle application. The opening phrase about charging for bits read risks sounding like a charge for information extracted.

I expected a tiny ordinary example before a new hard partial function appeared. OR or AND would suffice to establish a transcript, an early stop and a worst-case count. Without that example, the word run in the later lower-bound proof will carry more background than this paragraph has supplied.

### Introduction, partial versus total and the theorem

The partial/total contrast is the right question to put near the beginning. The infimum definition is precise, but it arrives before the prose explains that the same constant must work for every total Boolean function and every input length. I noted this because the later proof needs a distinction between disproving one exponent and bounding the infimum of all admissible exponents.

The theorem display contains all the needed parameter dependence. I slowed down over what I was meant to remember: the logarithm's power six and the factor 1/400 are visually prominent, although the conceptual story concerns the powers one half and 2−1/k. The subsequent provenance sentence is correct but makes those refinements feel like a second headline.

The exponent arithmetic is helpful. I would keep it. I also recorded that the approximate equalities are stronger visually than the one-sided estimates they summarize. A reader learning how complexity inequalities are combined should be told that these are exponents of a proved upper bound and a proved lower bound.

### Introduction, mechanism, history and reading instructions

The mechanism paragraph tells me what the paper is about: a certificate at an address, a cheap quantum comparison and a classical price for finding the address. The word certificate is still doing two jobs. A stored cell contains witness data, while its validation reads other input fields. Later, certificate size is used in its usual complexity-theoretic sense. I wanted that distinction before the history paragraph.

The historical sequence is informative but long for this position. I understood the fractions as an expert reader, yet had no concrete object to attach cheat sheets or outward pointers to. The AND-OR paragraph is a better bridge because it explains why a familiar composition costs a factor of n quantumly. Its claim about n-bit certificates needs the two cases spelled out; that would turn a quoted property into something a newcomer could verify.

The prerequisites are now specific, and the two course routes are useful. This is a successful round-six repair. It also reveals an unresolved audience mismatch: the exposition now admits that it assumes most of the techniques a newcomer needs to learn. I would preserve that honesty while closing the small first-use gaps, rather than further narrowing the readership.

After inspecting pages 1–2, I found that the opening takes almost two complete pages before the first example. The accumulation of theorem, constants, mechanism, history, comparison, prerequisite list, outcomes and routes is the main structural obstacle to the examples-first experience.

### §1: first concrete inputs

This section became substantially easier to follow. I could check the bit/sign conversion, multiply the common second block by W, and verify the positive, zero and negative cases. The chosen examples are useful because the negative one will return when totality matters.

The geometric interpretation explains why the normalized inner product is bounded and why ±1 have a natural meaning. I briefly had to restore which object was a bit string, a sign vector or a normalized vector. Naming the normalized vector at the comparison would remove that small stumble.

At the projection experiment I encountered two first-use gaps. D_z was not yet defined, and projection onto u was not explained as an actual measurable outcome. Those are easy local repairs. The phrase that a single run decides the three examples is less careful: one example is unpromised. The next paragraph says the right thing, so the earlier phrase should not blur it.

The additional input with Phi=1/2 pays off. It shows why the decoder repeats the experiment, which the three extremal examples alone could not show. I would keep this sentence through any compression. The census of all 256 inputs, by contrast, is not used later; I could not tell whether I was expected to derive or merely trust it. The L=0 caveat is useful and should remain.

The closing phrase that §2 repairs acceptance of the unpromised input momentarily suggested that the cheap decoder itself would be fixed. The actual repair is different: exact certificate checks prevent a winning column. That distinction should stay visible.

### §2: one column and the four-column board

The inventory is explicit, and the sentence allowing every assignment establishes totality well. I was then asked to track seven kinds of symbols before the concrete board. A lecturer could make the material easier by interleaving the numerical layout with the general inventory rather than postponing the board until after the attribution paragraph.

The winning condition is understandable, but the four clauses deserve a stable layout. I knew I would have to look them up again during verification. The pointer argument for at most one winner is short and convincing. It should remain beside the definition.

Figure 1 shows the important two-scale relation: one column's cell points into the strings of all other columns. Its internal prose is small at the PDF's actual scale. I would keep the drawing and move some words to the caption, rather than make the drawing more elaborate.

The address-length paragraph explains why logarithmic r is chosen, a useful repair from round six. Its wording still makes a long address sound intrinsically hard to guess. The later direct product needs a particular distribution and caps; address length alone does not provide the prediction bound.

The four-column reset is explicit: r is reduced to two, and the toy represents definitions and the algorithm rather than the asymptotic lower bound. I did not record the old complaint that the reset is absent, because it is now present. The pointer encoding is also explicit and consistent in this section.

The board says all transcripts are true evaluations before transcripts have been introduced. The later explanation of gate consistency is good, but I wanted one literal gate equation. The concrete pointer trace is now there; the concrete gate trace planned in SX-014 is not. The exact 180-gate figure and 371-test total can remain as checks, but they do not substitute for teaching that operation.

The changed board is excellent. It demonstrates that correct stored gate values and correct value bits still do not establish the promise. The first domain bit blocks the false winner. Question 1 uses the same distinction across all four addresses. The sentence that a nonwinner fails at least one test at every address is the key invariant, and I marked it for retention.

On PDF inspection, Figure 2 appears between “fixed and public” and “part of the definition” across pages 4–5. That float placement interrupts the important distinction between a fixed public circuit and untrusted gate-value input data.

### §3: three supplier guarantees

The three-part interface is well chosen. I know what is supplied by Forrelation and what will be new in the total construction. The cheap decoder paragraph is compact, though phase kickback is named before it is taught. A one-line bit-oracle calculation would bridge the model to the sign oracle without adding much length.

The exact-circuit paragraph is denser than the other two. It combines normalization, integer arithmetic, word length, threshold comparisons and a numerical gate constant. I wanted its purpose first: a near-linear circuit yields a near-linear collection of local checks, even though evaluating every gate directly is too expensive. The current text gives the implementation count more space than that reason.

The classical hardness theorem is a sensible imported input. I did not ask for its full analytic proof here. I wanted a short intuition for why the matrix product is globally informative to the quantum experiment while a shallow classical tree sees little difference. The later literature comparison confirmed that the supplied Bansal–Sinha introduction presents the promise and the separating task before the technical machinery.

The total input-length formula is useful, but it also makes the scale startling: polynomially many cells means a very high polynomial. The reader should be reminded why this is not a theorem about practical storage or wall-clock speedup. The closing same-circuit sentence is exactly the right logical reassurance and should remain.

### §4, comparisons and counterexamples

The failure of nested search is a strong motivation for the tournament. The description should say search for a violation rather than read all m bits when assigning a square-root query cost.

The comparison rule is understandable. The paragraph about retained labels and orthogonality gives the right reason to identify its output law with the classical sampling description. Its final phrase about making a_ij well defined is weaker than what has actually been shown. The mathematical point is the law and the reversible implementation.

The outward-pointer argument handles an unpromised rival clearly. The dominating nonwinner and cycle are valuable changed cases. At this point I was still treating the decoders as noisy, so the categorical toy victories and 0/1 table briefly seemed too strong. The explanation that every toy experiment is exact appears later; it should precede these examples.

Figure 3 shows the topology immediately. The angled pointer calculations are harder to read. They could be moved to a small horizontal table without losing the graph's purpose.

### §4, ideal process and coherent sampling

The warning that the algorithm never knows the weights is well placed. The absorbed zero-weight state is also defined, so I did not re-raise either issue from older rounds. The pairing identity makes the expected mass decrease transparent once a_ii=0 and complementarity are recalled.

The sampling preparation explains fresh registers and derives both joint and conditional probabilities. That is the new mechanism. Here I expected the board trace next. Instead, the exposition continues through the full amplifier recipe and the coupling argument before running one stage.

The toy trace, when it arrives, is effective: two branches carry success mass one quarter each, the success probability is one half, and the measured pivot is uniform on those branches. Question 2 provides the one-quarter case where a Grover iteration really changes the probability. These should remain. However, all the toy comparisons are deterministic, so they do not demonstrate the preservation of a nonuniform fractional-weight law. I followed the record's existing `#upper-cyclic-example`, which does show that distinction and explicitly limits its scope to an abstract comparison example.

The bounded-amplification paragraph is over-weighted. The reader needs its cap and conditional-law contract; the 19/40 and 9/40 estimates interrupt the new algorithm. The round-six disposition already identified this and planned to move the recipe. I recorded it as a fix that did not land.

I also noticed that the actual number of preparations cannot be fixed in advance if trials stop at first success and the Grover iteration count is randomized. The intended statement is a fixed upper cap. The count paragraph repeats the same wording, so this is one repair needed in two places.

The coupling sentence needs a short explanation for the target audience: use the same pivot draw while the real stage succeeds, and count the first failed stage before the winner is listed. The exact-law calculation has already done the hard work; the prose should use it explicitly.

### §4, verification and cost

Verification correctly uses the fact that every nonwinner fails at every address. The winner's fresh-decoding error should be assigned explicitly, rather than introduced only in the final error sum. The text also needs a short bridge from an adaptive classical local test to a reversible test evaluator controlled by a superposed index. The long record supplies that argument; the exposition should not make its existence implicit.

The two error regimes are now clearly separated, which is an improvement. The cost paragraph still packs two nested products into one dense block. I wanted named factors for stages, preparations, comparisons and test evaluations before the final loose logarithmic powers.

I later checked Answer 2. Its claim that the verifier rejects both losing candidates is stronger than the stated bounded-error test search. The zeros are definite failing witnesses; detecting them still has the verifier's one-sided failure probability. The exact toy decoders do not remove that search error.

### §5: planting and the two ways to notice

The hard-distribution consequence of minimax is stated cleanly, with the proof routed to the record. The pair is also clear: all columns have one zero and blank cells; one column's zero is erased and its true cell filled. Figure 4 is the best diagram for the lower-bound mechanism because it shows both changed regions.

The sentence saying no hard distribution exists at m=4 stopped me. With L=0, a balanced distribution on the two promised outputs is already hard enough. I checked this directly from the two inputs established in §1. The intended caveat concerns the quantitative asymptotic regime, not existence of a distribution.

The first-difference inequality is readable, and the parenthesis about overcounting a cell visit is useful. The erased-zero argument then says to condition on the whole transcript. For the hazard calculation I needed the transcript prefix before the current query. The surrounding residual-uniformity reasoning is correct in that interpretation, so I recorded a time-index ambiguity rather than rejecting the bound.

The dependent-I example is strong. It gives a complete rule even when no zero is found, calculates the changed hit probability and names the difference between a uniform marginal and independence. The changed-case question tests the actual condition.

### §5: direct product and simulator

The separate-cap lemma has the right contract. Both counterexamples are relevant, and their different input laws are now explicit. The phrase “both hypotheses” is too vague because the lemma has more than two assumptions; naming the two varied assumptions would fix it.

The optional proof's product structure and value function are understandable. The numerical AND update gives a concrete instance of a value rising on one branch while its expectation does not rise. The proof box spans pages 11–12, but this is a minor layout matter, not a reason to lengthen the main route.

The joint-event counterexample is also useful. The three-budget paragraph is a successful repair and should stay. My main remaining stall was operational: how does a proposed addressed-cell query become an answer guess before any cell contents are read? I followed the record to find the short simulator trace. The exposition's link lands at the general simulator anchor, while the actual table has `#CL-simulator-example`. That table, including the abort branch, is what the intended reader needs most.

The final averaging step should show the 1/m factor rather than only say no factor m appears. The contradiction should show the two acceptance probabilities that force a gap of one third. Both additions are short explanations of existing reasoning.

### §6: exponent and quantifiers

The ratio calculation has the correct nonnegative-alpha hypothesis and uses the upper bound on Q in the correct direction. The t>=8 calculation concerns floor conversion, and should be labeled as such so it is not confused with the k-dependent Forrelation threshold.

The fixed-k warning is excellent. The t>=2^k example demonstrates why the order of quantifiers matters. I then worked Question 4 and found that it asked a weaker statement than its answer tested. At k=4 the ratio diverges for every alpha<3.5, already proving the infimum lower bound. At k=5 it also diverges at alpha=3.5, excluding that endpoint bound. The exercise needs one clearly chosen target.

The matching universal upper bound closes the main mathematical question. The extra constant 35^4 is less important to this reader than the resulting equality of the optimal exponent; it should not become a new proof detour here.

### §7, answers and closing matter

The formalization paragraph is long but contains one material statement difference worth keeping: the family's formal quantum bound leaves the logarithmic power unspecified. The best sentence is the suggested inspection of the winning condition against the changed board. That action should organize the section; a reader does not need every model definition linked in the same paragraph.

The ordinary AI-credit paragraph is appropriate, as is a normal bibliography. Local novelty language earlier in the exposition should agree with that attribution. I did not ask for receipts, status caveats or review taxonomy in the paper.

### Comparison pass after the sequential read

I then read the supplied de Wolf chapter on Grover and amplitude amplification closely. Its sequence makes the search problem and good/bad subspace visible before variants and cost refinements. I sampled the supplied SK exposition's opening and first finite example; it introduces unfamiliar probability operations through calculations rather than using a list of prerequisites as the entire bridge. I sampled the Bansal–Sinha opening and theorem interface, and followed the existing long-record sampler and simulator examples.

Online, I read MIT's historical lecture notes 10–11 for their instructional structure and IBM's Grover introduction for its framing. The MIT notes are old and contain historical bounds; they are not used as authority for the current optimal exponent. Their useful pattern is to attach a general method immediately to a small OR or AND-OR example. No external source is being treated as evidence that a real reader of this draft succeeded or failed.


## The full reasoning record

This log follows the current `repository/docs/reasoning_record.md`, not its older PDF. It records an editorial and proof-navigation reading; it is not a claim that Lean or Comparator was run. The mathematical body was read consecutively. Catalogue and formal appendices are described below at the granularity actually inspected.

### Front matter and §1

The opening gives me the correct question immediately and the construction paragraph does considerably more work than the title. I can now tell why a winner has outgoing certificates, why the opponent's promise status should not matter to the quantum algorithm, and why the lower bound has two discovery events. That mechanism should survive any shortening. I slow down at the last sentence of the opening mechanism: the probability `(2/3)^r` belongs to a carefully capped success event, whereas the opening makes it sound like a property of an arbitrary lightly queried column. The full explanation comes much later. A short indication that the estimate is a joint cap event would avoid asking the opening to carry a theorem it has not stated.

The first reading-guide table is useful, but its construction route is a long itinerary of section numbers; several are not links. The next paragraph adds exceptions and optional detours, then §1.1 gives a dependency table and another routes paragraph. I need one usable route that I can follow as a reader, not three partly overlapping navigation devices. The stated theorem and quantified ratio calculation are precise. I understand why fixed k excludes smaller powers, including the cubic power. However, the introduction has now proved the exponent argument almost completely before I have seen the function, and §7 will do it again. The ratio display deserves to stay somewhere; its two placements have different jobs and should be visibly distinguished.

The outward-pointer paragraph is the most effective part of this opening. The uniqueness proof is two sentences and uses exactly the data just introduced. The final comparison with earlier cheat sheets answers why the construction changes the exponent; I wanted that historical paragraph earlier, before the long quantifier calculation. I checked the companion's headings after the record said its §§4–6 summarize the quantum tournament, planted bound and Forrelation supplier. They are actually §§3–5. That navigation sentence is stale even though the surrounding mathematics is coherent.

### §2: models and small examples

I read the partial-function and query-cap conventions in full. They are unusually careful about a promise being an obligation on an algorithm, rather than an input-completion rule. The distinction is relevant later and earns its space. The finite-mixture discussion identifies an exact-error issue that ordinary accounts often suppress; the OR example eventually pays it off. The prose alternates between ordinary mathematics and Lean's representation choices, however. A reader trying to understand the mathematical model must repeatedly decide whether `source`, `constructor`, or `wrapper` introduces another mathematical condition. The model definitions are needed; implementation terminology should be concentrated where it resolves a real ambiguity.

The controlled-phase caveat is mathematically helpful, especially its explanation using global sign. The final sentence correcting de Wolf's section number reads like a reply to a previous reviewer, rather than part of the argument. In §2.4 the mass recursion and its induction are easy to follow. The large disjunction defining QLe arrives before the empty-coordinate reason for the first branch. I understand the reason after reading the next paragraph; bringing the reason to the display would remove the initial impression that there are two competing models.

The deferred-measurement construction is substantial, not just an appeal to folklore. Its entry isometry, auxiliary J and unitary extension require an explicit invariant to orient a referee. I can reconstruct the purpose of each map, but I would have understood the proof faster from one sentence saying what the induction must retain. The distinction between an acceptance law and a retained final state is valuable and should remain.

The examples in §2.6 are well selected. In particular OR on two bits makes the inclusive 2/3 endpoint and arbitrary biases concrete, and the negative lesson about replacing `none` with false changes the problem. The examples should not be diluted into a checklist. The zero-query example ends with an obsolete-sounding sentence about earlier fidelity returns and missing receipts; that interrupts an otherwise complete mathematical proof and belongs in the formal appendix. The final parity paragraph distinguishes two editions of Beals et al. accurately in intent, but its bibliographic audit is longer than needed at this point; a compact note could protect the convention without displacing the example's payoff.

### §§3.1–3.5: the partial function, decoder and circuit

The three-property preview makes the purpose of the long Forrelation section clear. The phrase that conclusions are “consumed by §3.17” momentarily turns an ordinary mathematical ingredient into software jargon. The promise is then defined cleanly, with the positive-threshold issue explained before it can cause a mistake. I particularly value the negative-Forrelation example: the quantum test can output one on an unpromised input, so a separate circuit domain bit is necessary. This is a genuine explanatory bridge into the total construction.

The integer numerator and two exact tests are transparent. In the decoder, the fixed repetition count and retained-workspace construction are also transparent, but §3.3 changes register abruptly after its ordinary bound. It spends two paragraphs on a wrapper, an existential n, a generic compiler, abstract reads and physical queries, then returns to antecedent quantum algorithms. Appendix G was supposed to be the destination for that level of correspondence. The distinction between qk in the ordinary construction and 2qk in the formal implementation matters; it should be stated once at the place where a reader asks about it.

The circuit proof lets me reconstruct the size bound. The split between ideal integer bounds and modular storage is useful. The five-gate full-adder calculation is followed by a six-w-per-operation table without a sufficiently immediate explanation of why a deliberately nonminimal implementation is being counted. I stopped to reconcile them. The loose constant 200 is harmless, but the route 337 to 800 should state that the extra slack is for a simple uniform expression, otherwise the reader wonders whether a contribution was dropped. The endpoint tests deserve to stay exact; “No floating-point approximation enters” adds no mathematical content after the residue argument.

I read the complete 256-input census. It is valid as a compact hand calculation and useful for someone auditing conventions. As part of a first construction reading, it is much less important than the three-example table immediately before it. The reading guide permits skipping it; the local section itself could make that purpose clearer. The closing checker paragraph should be shortened to a source note, since the hand argument is already the mathematical warrant.

### §§3.6–3.10: entry to the independent lower-bound proof

I read the statement and its comparison with the published bound, then the complete setup through the path-derivative identity. The proof-spine paragraph is a real improvement from round six: it identifies the two laws, the interpolation, the derivative transport and the tree estimate before introducing the functions. The entry sentence itself is grammatically damaged: “Let …, let …, and we index …, read …, and write …” mixes an imperative construction with a first-person assertion. More seriously for readability, the passage fully reintroduces the promise, Walsh normalization and query convention that the immediately preceding pages have already established. That is useful for a link landing, but a linear reader needs an indication that this is a restart for a self-contained proof, not another change of definitions.

The discrete/polynomial derivative distinction is explained well. The algebraic truncation is motivated by the identity it satisfies, but a reader still needs to know why the bound 1/2 is the useful range: it will control the derivative characters and stopping argument. The zero endpoint proof is a good use of sequential clearing; I can follow why the reflection changes no uncleared earlier block. The three-block worked derivative is especially valuable: the disappearing repeated derivative is visible, and the next induction names its invariant. I would keep that calculation even if the section were shortened. The sentences saying that no singular Gaussian density is used or no covariance is differentiated should become a concise explanatory note, because those absent alternatives are not the reader's main question at that point.

### §§3.11–3.18: derivative growth, promise gap and constants

The derivative-growth lemma has a clear statement, but its proof introduces the degree-r process before telling me its eventual coefficients will be chosen as derivative signs. I can infer that purpose only on reaching (F32). I checked Girish–Tal–Wu's original §1.3 online: their overview sets up the signed Fourier sum first, then introduces the martingale because it represents that sum. That order would help here without importing their theorem or changing this proof. The record improves on a compressed overview by giving the stopping construction rather than merely conditioning on a future good event. Its explanation of the distinction is precise and worth keeping.

The application (F33) is quick once the three inputs to the bound are separated: path uniqueness, the Walsh coefficient, and the bounded kernel. The moment calculation and pointwise promise inequalities do necessary work. The explanation that the hard law has only a small promised mass is the missing conceptual reason for amplification, and I wanted it just before, rather than just after, the majority calculation. The numerical assembly is reconstructible. It would be easier to audit if the error-gap budget were introduced as a small plan, because 119/144, 1/3 and 1/4 otherwise appear as unexplained numbers. The final threshold's strict inequalities are carefully directed; I do not raise the older threshold or 514/508 discrepancy as unresolved.

The end of §3 has three overlapping attribution summaries: the proof-spine entry, §3.16, and §3.18. Credit is correct in purpose and specific enough to preserve, but the repeated warnings about not claiming priority have become more prominent than the mathematical distinction they defend. The full ingredient bundle is an effective exit: it gives the same promise and witnesses needed downstream, with the accuracy parameter chosen in the right order.

### §4: addressed certificates and local tests

I read all of §4. The transcript lemma is elementary but essential because it explains why a claimed output is tied to the actual input. The layout table and winning predicate are precise; the input-length paragraph successfully answers the scale question introduced by 2^r cells. I slowed at the phrase “This identification is semantic”: it describes the review process rather than saying the elementary fact that the address is forced by the values. That distinction can be made in the proof's own vocabulary.

The four-column example is concrete and correctly declares its reduced r and substitute circuit. It nevertheless resets both the Forrelation example and the block numbering, from z_0,z_1 in §3 to z_1,z_2 here. A reader who has kept the earlier eight-bit example in mind has to rebuild it. The full-board completion is described through the accompanying checker; enough of it is written in the paragraph to be mathematical, so the checker need not be the grammatical subject. The four classes of local tests explain their separate roles well. The phrase “all of them pass” follows a new count of 5936 input bits and briefly seems to refer to bits rather than 371 tests.

I read the support remark and coherent-evaluation construction rather than skipping them. The remark now clearly separates adaptive depth from fixed support; this was a successful round-six repair and should remain. The compute–copy–uncompute corollary is useful, but the section's figure-free stream of register descriptions makes the relationship among retained evaluation, reset evaluation and uniform sampling harder to see than it needs to be. The winner's immunity to arbitrary incoming pointers is excellent; the proof does not smuggle in a promise for the opponent. Historical antecedents are credited by what each one contributes, which is the right approach, though the final sentence repeats attribution already made at the section entry.

### §5.1: fixed-cap amplification

I read the full geometry, trial definition, exact averaging identity, cap calculation and returned-register argument. The content deserves inclusion in a complete proof record; the problem is its presentation density. The lemma statement is one paragraph carrying algorithm uniformity, state output, endpoints and cost. Separating its mathematical clauses would make it considerably easier to audit. The proof could also explicitly fix the success projection as an input-independent operation before charging only A and its inverse; the use of a generic success subspace otherwise requires the reader to supply that convention.

The elementary averaging derivation is sound in structure. Several sentences interrupt it with internal claim IDs. Those should be invisible anchors or a lookup table, not part of the sentence. The returned-state discussion correctly distinguishes the designated subsystem from the enlarged workspace, and the product-state/Bell-state comparison makes that distinction real. It should stay. The recurrence proof and the physical correspondence discussion repeat each other's conclusions, so the section could state the ordinary result cleanly and send the formal comparison to G.7.

### §5.2: the probabilistic tournament

The proposition is the central quantum theorem and is appropriately stated at the entry. I understood its hypotheses but had to hold too many quantifiers and constants in one paragraph. The four-stage proof map helps. The same comparison model and parameter definitions are then repeated in the statement, the two short subsections and the proof opening. That is a clear source of length with little explanatory benefit.

The drift calculation is the key idea. It is short and exact, and the cyclic four-candidate example pays it off numerically. I would keep both. The ideal weights are explicitly analytical quantities, which avoids an important false inference that the algorithm estimates every a_ij. The next pivot's exact conditional law is then derived from orthogonal labels and fresh comparison registers. The coupling proof is unusually explicit about why failure probabilities are charged only until the desired vertex is selected. This is an effective proof-navigation destination.

The passage sends a companion reader back to §4.2, but the companion's tournament is §3.2. After the proposition has been proved, it is completed again as a finite-list law, with a separate padded constant 6072 in between. These clauses have legitimate formal roles, yet the literary structure makes a reader wonder how many variants of the theorem remain to be proved. One close of the ordinary proposition, followed by a clearly scoped implementation note, would help.

### §§5.3–5.5: decoding, verification and the final cap

The comparison rule is complete even for two losing columns. The distinction between a decoder's arbitrary off-promise output and a verifier's exact promise check is consistently maintained. In the verifier, however, “success” alternates between finding a failed test, accepting a candidate, and obtaining the correct final answer. The probabilities are correct but the vocabulary creates avoidable reversals. Defining “find a violation” as the search event and reserving “accept” for the candidate would lighten the prose.

The final error proof explains why an earlier false acceptance on a one-input does not hurt the Boolean output. That is a good detail, not padding. The all-input cap is then explained through coherent access, an abstract-read compiler, an exact padded budget, an asymptotic bound and a deliberately loose log-six calculation. The individual steps are useful to different audiences, but their sequence leaves the algorithmic reader in a long constant-accounting appendix before the classical argument begins. The exact finite budget should remain available; the six powers of the logarithm need a compact factor-by-factor reading aid.

At §5.5 I stopped at the description of a “slightly different route.” The ordinary §5.3 algorithm already verifies the listed candidates sequentially and returns one bit. The genuine distinction concerns the formal theorem interface and induction route, not that elementary behavior. That distinction should be stated precisely. The induction itself is thorough, including the negative-Q case, but its final paragraph belongs to a reader who has chosen the formal route.

### §6.1: the capped direct product

I read both proofs, the cap-event corollary and the adaptive example. The conditional proof explains the real issue: after a positive-probability transcript, inputs remain a product, and one query changes only one continuation value. This is far better than merely saying that independent tasks multiply. The jointly-independent-information counterexample is particularly efficient and should stay. The cap-event corollary also states the right joint event; I do not re-raise the former conditional-on-nonheavy mistake as though it remained.

The record gives the conditional-value and unnormalized-weight proofs with an identity showing they agree. That identity earns the second proof's presence. The second proof is properly optional, so I would not demand that it be deleted. What could improve is the choice of local examples: later §6.5 gives another cap-conditioning example, with different promise and parameters. A shared counterexample cross-reference would reduce the number of tiny distributions a reader must remember. The Drucker comparison has been corrected in round six: it now explicitly says that a global-budget theorem can serve here with a factor two. I checked that this is not still being presented as an unavailable route.

### §§6.2–6.4: hard law, planting and the erased zero

I read the finite minimax proof in full. It tells the reader why one distribution works for every tree, rather than introducing μ by assertion. I wanted a short sentence before the convex geometry explaining the objective of the separating vector, because the proof's variables K,H,a,c,v arrive quickly. The introduction to §6.2 repeats almost the whole construction after §6.1's long detour; that is a useful local restart, but it would be easier to navigate if it were identified as a compact recall and linked to the winning predicate.

The coupled inputs and first-difference inequality are clear. The XOR toy correctly states that it is neither the Forrelation board nor an asymptotic parameter choice. It nevertheless requires a second numbering convention and a second circuit, which is a large cost for readers arriving from the exposition. The practical payoff is the simulator trace, so those two pieces should be presented as one worked route rather than separated by several further estimates.

For the erased zero I read the selection identity, independence counterexample, early/late proof and both optional refinements. The independence example is good: a marginally uniform column is not enough. The main early/late proof is straightforward, while the optional refinements make the ordinary versus formal route distinction explicit. Their current optional labels are adequate; my remaining objection is repetitive prose about what each endpoint does not prove, rather than a missing warning. The main argument has already earned its return to §6.5.

### §§6.5–6.6: the simulator and contradiction

The simulator is the best classical proof-navigation destination in the record. Its independent side information, shared target-query cap, stopping point and output address are all explicit. The time-four trace says that the simulator outputs an address before reading the changed cell bit, which is exactly the detail a reader could otherwise miss. The joint event is contained in simulator success under the original law; no illicit conditioning is used. The cancellation of the factor m when averaging over I is also stated, so I do not flag that older concern as missing.

The second conditioning counterexample is accurate in purpose, but it competes with the earlier adaptive cap example. The contradiction then repeats the strong versus weak endpoint distinction and the Bansal–Sinha-to-L comparison, although neither is needed to understand why a gap below 1/3 contradicts bounded error. The proof's mathematical climax should be the common finite gap bound and its averaging over coins. The floors are handled carefully, with t≥8 explicit. Return references to companion §5 and §5.5 are stale; the lower bound is now §4 and §4.5.

### §7: the exponent and a growing parameter

I read all three subsections. The fixed-parameter order is exact, and the ratio proves the intended infimum assertion without claiming an exact Ω(Q^4) family. The proof is considerably longer than the idea, partly because the same calculation appears in §1 and again because the shifted/unshifted distinction is repeated. The integral estimate is legitimate in a complete record; it should be visually subordinate to the choice of k.

The growing-k subsection is new and self-contained. The constant 508 is now reconciled with the companion and is supported by a displayed bound with slack; I do not resurrect the earlier 514 discrepancy. The explanation of the floor choice k=floor(sqrt(t/20)) arrives after expanding a very large C_k. I would first explain that this choice balances the 40k and ell/k terms in 4B−A, then put the exact arithmetic after the target. The reason to retain 508 is compatibility with the companion, but that publication-coordination sentence distracts from the simple fact that the bound has slack. No stronger asymptotic conclusion is needed.

### Appendix A

I read the entire upper-bound reconstruction. The four-inequality chain (A.2) is an excellent map: the two adversary matrices have distinct jobs, followed by the spectral degree bound and the monomial decision tree. The proof of the spectral consequence of Huang is particularly economical once the majority set is identified. The parity witness for the adversary factor is a concrete and mathematically relevant source check. Its computation should stay available, but its closing history of an earlier annex transcription is too much editorial archaeology in the middle of the upper-bound route. The copy should distinguish the local coefficient issue from the asymptotic theorem once, rather than layering several disclaimers.

The Midrijānis discussion is correct to identify the product estimate inside the proof rather than mislabel its theorem. The final assembly is concise and does not need more explanation. Some elementary facts are proved in unusually fine detail while other concepts, such as the Rayleigh quotient, are assumed. That uneven audience calibration is a matter of presentation, not a mathematical defect.

### Appendix B

I read all 121 catalogue statements and their argument links; repeated HTML anchors and markers were omitted from the display used for this pass. The catalogue is useful as a lookup destination, but its long introduction and group introductions partly recreate Appendix G's status discussion. “Literal maintained ledger” is an understandable repository constraint, yet raw inequalities and IDs should not be the only reader-facing statement view. The proof links are the useful part.

Several labels are stale after sections moved: B.8 refers to §§6.2–6.7 though there is no §6.7, B.9's broad no-growing-k sentence does not distinguish its fixed-k rows from the now-present §7.3, and B.10 says Appendix A keeps three formal routes separate although the table is in G.9. These are not broken anchors; they are wrong descriptions of what the reader will find. Byte-valid links alone will not catch them.

### Appendices C–E

I read the bibliographic notes, the full historical-threshold proof and both source comparisons. The edition-specific locators are valuable, especially where source, PDF and HTML theorem numbering differ. The bibliography is currently a source-assessment log: instructions like “Do not attach…” and repeated explanations of what was or was not inspected sound like internal adjudication. Keep precise editions and locators in the bibliography; place review history elsewhere.

Appendix D clearly says it is historical and no longer needed for the main proof. That is a successful distinction. Its elementary floor/threshold inequalities duplicate calculations already given in the body, and the final paragraph switches from mathematics to declaration status. A reader should be able to decide from the heading whether to read a historical alternative; no additional caution labels are needed.

Appendix E's Bansal–Sinha comparison is appropriately version-specific and limits the conclusion to displayed inequalities. I inspected the supplied source text around the theorem and proof ending; the review should not convert this local calculation into a claim that the original theorem is false. The SSW transfer names the actual imported Fourier theorem and keeps the random-orthogonal separation separate from the Walsh application. Those distinctions are correct and should survive editing. The opening sentence of the transfer says that k-dependence disappears, but k remains in the exponent and dimension condition: it is the explicit multiplicative polynomial loss in k that disappears. That wording should be narrowed.

### Appendices F–G and AI disclosure

I read the complete current appendix text as prose and navigation, without rerunning its receipts. Appendix F is historical, but its paragraphs still contain unqualified “current integration,” “current root build” and “the source assessed here.” Those deictic phrases defeat the purpose of isolating history and make it harder to understand which source snapshot a paragraph describes. The dates at the start of F.1 help; use dates or named snapshots consistently throughout.

G.1 offers a useful bounded check of one statement. It nevertheless asks the reader to test a finite example after saying this is a statement check, and its concluding sentence treats the checklist as establishing semantic agreement without identifying which of its steps is the judgment rather than a mechanical test. A clear scope sentence and direct links to the relevant definitions would make the route more usable.

G.4 gives the necessary exceptions and should not be replaced by an indiscriminate “fully verified” label. Its wide second table, however, mixes current execution, older corpus relations and later textual review in dense prose cells. A claim-directed reader needs a shorter current statement summary first, with the historical comparison columns retained for readers who choose them. G.5–G.9 then repeat much of the table. The quantum section is especially vulnerable to temporal wording: it both states a remaining physical bridge and records an accepted opaque-unitary retained-factor theorem. The remaining obligation should be named in terms of its precise physical transport, so the reader does not mistake an already proved factor identity for the missing part.

The final AI disclosure identifies authorship roles. The last sentence about no person reviewing or submission status is an internal status note, already repeated in G and F; it is not needed to explain the contribution or the mathematics. Removing it from the paper would not authorize any claim that a human review occurred.

### Source-comparison and previous-round pass

After the continuous record read I read all 60 previous-round disposition rows, in addition to the full plan. This confirmed that several tempting complaints would simply re-raise repaired issues: the route guide exists, the proof-spine credit is at the Forrelation entry, the unnormalized proof is explicitly optional with a purpose sentence, and the Drucker alternative is acknowledged. The remaining catalogue references did not all update with those repairs.

For source comparison I sampled Bansal–Sinha's opening/results, their approach discussion and final lower-bound proof; SSW's independent-work discussion and decision-tree Fourier corollaries; and GTW's ordinary-tree overview, Lemma 1.9 and stopping footnote online. I checked the long-record exemplar's full heading inventory and opening through the beginning of its argument map. These were targeted readings rather than complete source-paper reviews. The source list records the actual boundaries. The useful comparison is motivational order and precise allocation of source roles, not a license to replace this record's mathematics or import a stronger theorem.


## Integration pass: what changed after following the claims

Following fifteen claims clarified several distinctions that should be retained: the main existential family versus its named-circuit constants; measured pivot labels versus a separately retained register; a cap event joined to success versus conditioning on compliance; and different constants from two universal-upper-bound routes. These are meaningful mathematical differences, not reasons to infer that the headline theorem has failed.

The packet's successful link inventory did not settle navigation. Several record return labels still point by name to former companion section numbers, and the exposition's simulator link promises a worked trace but lands before it. The journey file reports local source destinations and their limitations rather than treating every existing anchor as a successful teaching route.

The register audit also changed how the numerical flags should be read. Several “outside” flags describe distance from the corpus median even though the observed value is within the corpus's min–max range. This defect affects the interpretation of the measurement, while the source manuscript errors remain independently grounded in their actual sentences. All 403 input payload hashes matched the supplied manifest; incompleteness of the exported rule inventory is a content issue, not evidence that the input ZIP is damaged.
