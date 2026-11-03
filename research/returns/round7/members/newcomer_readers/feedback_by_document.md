# Critique of the three documents

## Overall judgment and scope

The exposition has several excellent teaching passages, but it still does not meet the packet's specified entry level. Its most successful repairs give the reader something to do: distinguish alignment from opposite alignment, follow a pointer, reject a false domain certificate, continue a pivot calculation, or identify an invalid conditioning argument. Its least successful passages state a correct interface and immediately use several operations that the intended reader has never learned. More detail is not the general remedy. The next revision should move detail toward those missing operations and away from numerical refinements that interrupt them.

The expert companion is a useful compact proof route for a prepared reader. Its strongest material explains why the new construction can tolerate arbitrary loser comparisons and why the classical reduction bounds a joint event. Some of that material receives less space than the explicit constants. The long record contains many of the explanations the shorter documents need, but its examples and return directions have not all stayed synchronized with them. The most urgent changes are therefore precise: fix the exercise's logical target, repair example and section references, preserve probability scope in summaries, and make the exposition's quantum and reduction steps usable by its stated audience.

These are three **emulated backgrounds**, not observations of recruited readers. The separate logs record modeled reading experiences and distinguish first-pass comprehension from understanding recovered with the record or literature. All three passes cover the complete current exposition. The companion was read in full across the review; the record was read substantially along its guide, linked proofs, examples and selected appendices, not audited word for word. The source register in `feedback.json` records the individual scopes. The current Markdown is authoritative; the long record's supplied PDF is an older edition. No formal receipts were rerun.

## 1. Exposition

### 1.1 The first page changes the reader instead of preparing the reader

The sentence beginning “This account is written for a graduate student” is candid about the draft's prerequisites. It does not solve the audience problem posed by this packet. The analysis/combinatorics mathematician has substantial proof experience but no quantum measurement model. The undergraduate has the linear algebra needed to learn that model, but not its notation or operations. The circuit-trained physicist can read an oracle circuit but has not learned decision-tree complexity or minimax. A single course list cannot stand in for three different bridges.

The first stopping points are consequently different. The undergraduate stops at the first oracle equation: the basis labels, answer register, XOR and linear action have not been connected. The mathematician can continue through the Walsh inner product, then cannot justify replacing its value by the probability of a measurement. The physicist gets further through the quantum language but initially imports gate count, physical memory and input preparation into a resource that counts only queries. All three can manipulate the opening exponent display while remaining unsure what its quantities mean operationally. See findings associated with the introduction and §1, especially the three separate prerequisite diagnoses.

The supplied survey and the newly consulted Ben-David notes give a useful alternative sequence: a known task on an unknown bit string, one charged observation, an adaptive decision, then the model. An OR example need not become a miniature textbook. Its job is to identify what is fixed, what is hidden, what one call reveals, what the algorithm's randomness means, and which costs are ignored. The quantum bridge then needs the basis-state interpretation, the squared-norm rule and the bit-to-phase query relation at the first places where they are used. The physicist should be able to skip those few explanations without losing the construction. Sources and exact reading scopes are in `literature_comparison.md`, §§1 and 4.

The opening currently carries a theorem with explicit constants, the infimum of all universal exponents, a mechanism sketch, historical exponents, the older AND–OR construction, prerequisites and reading routes. Each has a plausible reason to be present. Their accumulation is the problem. The one-line exponent arithmetic is a successful orientation device and should remain. The detailed predecessor calculation should be encountered when the reader can compare it with the new construction. The coefficient $1/400$ and logarithmic exponent six should not appear to be the principal discovery simply because they dominate the first display.

### 1.2 The small inputs work; the total object needs one more operational bridge

The three eight-bit inputs are unusually effective. The positive input aligns with the transformed sign vector; the zero case is orthogonal; the negative case is oppositely aligned. Squaring the amplitude erases the distinction between the positive and negative extremes. That observation gives totality a real mathematical job: a fast partial decoder can behave confidently on an input for which no partial value is defined. Keep the explicit warning that the small instance demonstrates conventions, not the asymptotic classical lower bound.

Several small changes would make this passage more self-contained. Define the sign diagonal when it first appears. Identify the measurement that tests overlap with the uniform vector. Avoid describing the experiment as deciding all three examples, since the negative input has no required partial-function answer. The nonextreme input with amplitude $1/2$ is a natural short check of whether the reader can convert bits to signs and probability; its point is more valuable than the complete 256-input census.

The move to a column introduces two distinct addresses. The $r$ hard answers choose a certificate cell; an $\ell$-bit pointer in that cell chooses a row of another column. The toy makes both lengths two, which accidentally conceals the distinction. Figure 1 should support an actual trace from address inputs to a cell and from a stored pointer to an input bit. It should also distinguish a static dependency from information already known to the algorithm. The giant array is polynomial in the construction parameter $m$, but $m$ is not the total input length. That matters to every subsequent cost claim.

The sentence allowing every assignment to every input bit is indispensable. It prevents stored transcripts from becoming trusted advice. The domain-bit mutation is equally important: correct value outputs and matching addresses do not certify membership in the promise. Preserve it. What remains missing is a small gate check that reads an actual input wire where appropriate and a stored transcript wire otherwise. The current pointer trace is already present and helpful; this review is asking for the parallel circuit operation, not claiming that no local test has been explained. The record's §4.4 supplies the distinction. A large gate count and the name Shannon expansion do not teach it.

The cheap quantum decoder, exact certification circuit and classical hardness statement are three different interfaces. Section 3 now distinguishes them clearly. Keep that structure. Explain that the quantum verifier searches local checks of a supplied transcript; it does not evaluate the entire certification circuit afresh for every candidate. Otherwise its almost-linear circuit size appears to contradict the later square-root query count. The classical interface can remain an accepted theorem, but should retain the geometric question: why do a few ordinary bit observations fail to reveal the global relationship that the quantum experiment probes? This is a request for intuition about an imported theorem, not a demand for its analytic proof in the exposition.

### 1.3 The linked board is a different probability experiment

The exposition and the record use different raw strings in their four-column boards:

| Role | Exposition input and $\Phi$ | Record/checker input and $\Phi$ |
|---|---|---|
| Positive | `01111000`, $1$ | `00000000`, $1/2$ |
| Zero | `01001000`, $0$ | `00010010`, $0$ |
| Negative | `10001000`, $-1$ | `11110000`, $-1/2$ |

Thus the nonzero projection probabilities are $1$ in one example and $1/4$ in the other. The addresses, winning geometry, circuit size and local-test counts can agree while the decoder laws differ. This does not invalidate either board. It does make the link promising a script for every count on the exposition's board too broad. The checker’s all-256-input loop includes the new strings and is designed to validate their circuit outputs. Its named board and projection check still use the older strings; that coverage does not instantiate the exposition’s changed board or deterministic tournament. State exactly what the linked artifact checks and how the two examples are related. The deterministic exposition example should not be discarded merely to make the pictures look identical.

### 1.4 Teach the weighted sampler before its amplification recipe

Section 4 begins well. Verifying one candidate is expensive, and putting that verification inside an outer Grover search loses the desired exponent. Cheap comparisons are therefore motivated before being defined. The counterexamples also earn their space: a column can win comparisons without satisfying the total predicate, and losing columns can cycle. Those two facts explain why the algorithm needs final verification and why it cannot rely on an underlying total order.

The weighted process is the central new operation. The weights are products of comparison probabilities, not posterior probabilities that a candidate is a true winner. They are not estimated by the algorithm. The complementary pair identity gives an expected mass decrease; it does not promise that every realized update halves the mass. The current deterministic table can accidentally teach both an active-set interpretation and pathwise halving. Keep the table as a first example, then connect it to the record's existing fractional row. With weights $(11999/12000,0,0,1)$, the successful mass is $23999/48000$ and the two positive conditional label probabilities are $11999/23999$ and $12000/23999$. That small contrast exposes the distinction the binary row hides.

The newly completed sampler stage is a real round-six success: it computes joint masses, conditions on success, measures a pivot and continues the same board. Question 2 is also a meaningful continuation. The remaining ordering problem is that this execution comes after the ideal proof, preparation, amplification and coupling. A reader needs a concrete success flag and measured label earlier to know what all those layers implement.

The exact-successful-law assertion deserves more explanation than the trial constants. For a fixed input, history and label, fresh comparison workspaces give the product of the appropriate probabilities. Orthogonal label blocks make their masses add. The normalized successful vector includes **all retained registers**, not just a pure state of the column register. Amplitude amplification rotates the total good and bad components while preserving the relative successful label law. A small two-reflection picture or vector calculation would connect this to the circuit-trained reader's existing Grover intuition and give the other two readers an explicit usable contract. The record already supplies the argument; no new result is needed.

By contrast, the half-mixture, $19/40$, $9/40$, case split and exact logarithmic trial count still occupy the teaching path, despite the earlier plan to move them. Preserve the bounded cap on every input, the zero-success case and the precise conditional law. Move the numerical derivation to its existing destination. The current assertion that every number of trials and iterations is fixed should refer to the predetermined **caps**: the algorithm randomizes an iteration count and may stop early.

Verification needs one last bridge. The reader has seen local tests described as classical adaptive procedures. Explain how a coherent test-label register selects a reversible implementation with a common query cap. Then the search for a failed test has a visible meaning. Keep the distinction between finding a listed candidate and certifying a winner, and keep the explanation that later stopping cannot remove an already listed winner.

### 1.5 The lower bound needs a visible reduction, not more cautions

The planted-pair explanation is substantially better than a slogan that a classical algorithm must learn many addresses. It allows the algorithm to guess a cell and bounds that possibility. The first-difference formulation specifies one dummy run and the two kinds of changed coordinates. The independence counterexamples, the three budgets and the warning against conditioning on lightness already do useful work. They should not be deleted during a density reduction, nor reported as missing.

The first remaining obstacle is minimax. A separate difficult input for each algorithm is different from a single distribution that defeats all shallow deterministic algorithms. The latter supplies independent hard address instances. The undergraduate needs that quantifier exchange explained, and the physicist needs to know why a deterministic run suffices in a randomized lower bound. A brief interpretation before the theorem and a return to the averaging argument would make the route continuous. The hard law is an existence witness; the exposition need not give an efficient sampler for it.

The erased-zero calculation must condition on the transcript **prefix before the next query**. The phrase “whole transcript” suggests a completed run, which may contain future discoveries. The record has the correct prefix argument. This is a local repair to the presentation of an adaptive probability estimate, not evidence of a failed lower bound.

The direct-product box correctly distinguishes increasing success on one branch from nonincreasing conditional expectation. The tiny AND example and parity side-information example are strong. Their connection to the simulator should be made executable. The record's XOR trace shows which query is answered from outside data, which is forwarded to a hidden instance, when a shared counter causes an abort, and when the simulator outputs a cell label without reading the cell. The exposition's link should land at that trace, with the change of primitive and indexing identified before the reader enters it. A short trace on the main route would be even more useful than another verbal assurance about the cap.

Finally, the reduction gives an event inclusion. A cheap hit implies a successful address prediction; the predictor may also succeed elsewhere, including on a default guess. The events need not be equal. The factor $G$ comes from possible query times, and averaging over an independent uniform column avoids an additional factor $m$. These are the two inferences the reader should be able to repeat. Retargeting one question to this operation would assess the promised lower-bound understanding better than adding more arithmetic exercises.

### 1.6 Correct Question 4 while preserving the successful exponent explanation

The fixed-parameter order is now clear and should remain: fix a proposed universal power, choose $k$, then let $m$ grow. The threshold counterexample explains why fixed-$k$ bounds cannot be used with an arbitrary growing schedule. The remaining error is narrow and definite.

Question 4 asks which $k$ proves $\alpha_{\rm tot}\ge3.5$. Its answer says $k=4$ does not suffice. But the displayed estimates with $k=4$ give, for each fixed $0\le\alpha<7/2$,

$$
\frac{R(F_{4,m})}{(1+Q(F_{4,m}))^\alpha}
\gtrsim_\alpha
\frac{m^{7/4-\alpha/2}}{(\log m)^{2+6\alpha}}
\longrightarrow\infty.
$$

That excludes every universal power below $7/2$, which is enough for the stated lower bound on the infimum. At $\alpha=7/2$, these estimates alone do not give divergence. Choosing $k=5$ excludes that endpoint by creating a positive gap. The question should name endpoint exclusion if that is the intended answer. The main proof of $\alpha_{\rm tot}=4$ is unaffected. Similarly, “exactly the cube” should not suggest that logarithmic losses have disappeared at $k=2$.

The final Lean paragraph is appropriately short and gives a concrete inspection task through the domain-bit example. Preserve that invitation. The mathematical ending also needs a final reconstruction task: explain how cheap comparisons, expensive certification and a hard hidden address produce the two powers of $m$. This can replace an existing less central task.

### 1.7 What the three readers can currently take away

These are modeled outcomes, not observed quotations. The mathematician can likely explain the normalized correlation, uniqueness of a winning column, weighted-mass identity and probability traps. Their account of the quantum implementation remains dependent on imported operations. The undergraduate can describe the board and perform the displayed calculations, but is most likely to reduce the algorithm to repeatedly deleting candidates and the lower bound to “it has to solve every address.” Both formulations lose a central qualification. The physicist can describe the coherent comparison and interference advantage, but may confuse an exact certification circuit with a subroutine evaluated in full, or assume that unreliable comparisons are noisy measurements of a fixed true ordering.

All three should instead be able to explain the same causal chain: a total predicate checks untrusted transcript and pointer data; cheap comparisons preserve a genuine winner without certifying other columns; coherent sampling realizes an uncomputed weighted law; final verification removes false candidates; and a capped simulator turns a cheap visit to the planted cell into an unlikely correct address guess. They should then derive the critical powers from the displayed bounds and keep the endpoint qualification. The current exposition contains nearly all of that material, but its order and prerequisite bridges do not yet make the chain reliably reconstructible.

## 2. Expert companion

### 2.1 Keep its specialist role and make its scope easier to use

The companion should remain a research-paper account. A newcomer needing a full introduction to phase queries is not a reason to expand this document. The useful diagnostic is whether it compresses a standard tool or the construction's own distinctive inference. Standard amplification can be a lemma with a citation. Exact sampling from products of unreliable comparisons is central and needs enough explanation to audit here.

The abstract's promise of a complete argument and the later list of accepted inputs are compatible only after the reader reconstructs the scope. State that scope at the route-selection point. The last introduction paragraph currently combines roadmap, accepted inputs, optional refinements, link conventions and a return to the exposition. It would be easier to use if those functions were separated. A returning newcomer should be able to choose the compact quantum proof or the compact classical proof without interpreting the entire production architecture.

The first line's $4-o(1)$ form also looks stronger than the exposition's fixed-$k$ statements. The growing-$k$ remark supplies the additional argument. Make that destination easy to locate; do not leave the reader to infer that the quantifiers changed harmlessly. Conversely, the theorem introduces an unspecified logarithmic exponent even though the next paragraph and later proof provide six. Explain the choice or simplify the bookkeeping.

### 2.2 Give the mechanism more introductory weight than its constants

The construction overview has two particularly good sentences: a zero carries no pointer, and the winner's guarantee is independent of the rival's address inputs. These explain the design decisions that create the separation. They deserve priority over a crowded contribution list containing a leading constant, a large explicit threshold, several section references and a growing-parameter refinement.

The history is now meaningfully attributed. Keep the separate roles of pointer constructions, addressed certificates, partial-function hardness and comparison search. The old AND–OR calculation is explicitly tied to that recipe, which is the right scope. Do not turn it into a claimed impossibility for the entire cheat-sheet framework. Also identify Rorrelation when the name first appears; postponing its random-orthogonal interpretation makes it look like a typo in Forrelation. The dated papers describe the landscape at their dates, not what remained open after the supplied 2026 preprint.

The separation table needs a more accurate heading. Equality-shaped notation mixes attained lower-bound separations, suppressed losses and a universal upper bound. The surrounding text distinguishes these statements, but the table should preserve the distinction. The overview's approximation between $L$ and $R(P)$ has a similar problem: the proof needs a chosen hardness threshold below $R(P)$, not a matching characterization of the full randomized complexity.

### 2.3 Preserve the local mathematical distinctions

“Independent input bits” is ambiguous in a definition of a total function. It should mean distinct unconstrained coordinates, not stochastic independence under the later planted law. The latter law deliberately makes selected transcripts and pointers depend on the address and string data. The exposition's unrestricted-assignment sentence is clearer. Likewise, one marked zero among columns can suggest the wrong dummy distribution; each dummy column has its own hidden zero, and the planted operation erases one.

The comparison definition handles a genuinely important detail well: sorting an unordered pair and running a single fixed experiment gives complementary outcome probabilities. Preserve it. In the exact-sampling paragraph, explain why fixing the input, history and candidate gives a tensor product of fresh workspaces, and why different candidates occupy orthogonal blocks. That is the bridge from the comparison circuit to the classical weights. The subsequent coupling correctly allows stage failures to depend on the history. Its conditional guarantee is stronger editorial evidence than a generic claim that a union bound applies.

The direct-product proof likewise has the right framework: unnormalized measures avoid conditioning on zero-mass branches. But saying the recursion absorbs its two branches conceals the crucial factorization. The record gives the common product over all unqueried coordinates. A short display there would be more valuable than another paragraph explaining a deliberately loose logarithmic exponent in the quantum count.

The local verification cost should be read as an implementation bound. Saying a controlled query costs two ordinary queries can sound like an unavoidable exact lower bound; the record supplies a sufficient two-query implementation. The different amplification case splits in the exposition and companion are compatible, but their common contract should be easy to recognize without redoing both constant calculations.

### 2.4 Place optional refinements after the argument they refine

The sharpened erased-zero coefficient interrupts the transition to the planted-cell estimate, although the coarser estimate already closes the proof. Section 5's Gaussian-chain outline introduces substantial analytic machinery between the completed construction argument and the exponent payoff. This may be a useful specialist optional route, but its position should not force a construction reader to infer that every new stochastic object is needed before the elementary exponent deduction.

The growing-parameter bound has a large range where its exponent is vacuous. At the stated starting schedule $t=80$, the displayed loss exceeds four. This is not a contradiction; it is an asymptotic certificate with conservative constants. Name that practical meaning so the explicit threshold is not mistaken for a useful finite-size separation. Appendix A's failed-simplification examples should remain, but the longest adaptive example needs enough space to be executed; a dense table cell can become compressed proof prose.

### 2.5 Present and desired takeaways

The prepared mathematician can use the companion to reconstruct both main bounds, accepting the stated suppliers. The undergraduate can use its introduction and selected lemmas after the exposition, but will not independently bridge every circuit or minimax step. The physicist can follow the quantum route and much of the classical reduction, with assistance at the complexity conventions. Those are appropriate differences for this document.

The current risk is that readers remember explicit constants and the label “tournament” more readily than the exact invariant. They should leave with the three-part argument: complementary comparisons drive a weighted drift, coherent preparation samples the corresponding conditional law, and exact total-predicate verification checks the shortlist. The lower-bound takeaway should be an event inclusion for a capped predictor, not an assertion that the original algorithm necessarily computes the address. Preserve the clearly separated measured-label and retained-state statements, the true-winner robustness, and the joint-event simulator argument.

## 3. Long reasoning record

### 3.1 Repair the entry points before shortening the proofs

The record has a different legitimate job: full derivations, alternate proofs, explicit constants, source comparisons and a formal-statement inspection route. Its length alone is not a defect. The four-route guide is a useful improvement, and the most valuable next edit is to make those routes accurate and easy to leave and re-enter.

Several return directions retain the companion's old numbering. The current quantum argument is §3, the randomized argument §4 and the Forrelation supplier §5. The record directs readers to other ranges, including a nonexistent §5.5. Treat these as one renumbering repair. A link that opens a file does not validate the prose describing where to go inside it. The construction route also needs a more exact continuation after the direct-product statement: §6.1 contains corollaries, counterexamples and alternate proofs as well as the lemma whose proof the reader was told to skip.

The opening planted-cell summary omits the scope of the exponentially small probability. The proof controls a fixed proposed cell query together with lightness, then unions over up to $G$ query times. A summary that sounds like a bound on eventual discovery is misleading. The tournament synopsis similarly emphasizes winner reliability but should preserve complementarity for all pairs, since that remains necessary for the paired-sum identity. Both repairs align a summary with an existing correct argument; they do not request new proofs.

### 3.2 The model and circuit sections contain useful explanations to export

The record clearly states that a partial decoder may behave arbitrarily off promise while its query cap still applies. It also states that gate count, synthesis and workspace are outside the optimized resource. These are precisely the conventions the exposition needs before its huge input array and unpromised comparisons. The small randomized OR example gives a distribution over actual strategies, which is much easier to understand than a minimum over unspecified mixtures.

The unnormalized branch convention would benefit from one numerical measurement example before the recursion. The exact circuit discussion needs a short bridge from ideal bounded integers to residues modulo a power of two: the congruences preserve algebra, and signed bounds are needed when interpreting the final comparisons. The preceding magnitude estimates have not become irrelevant. These are local teaching transitions within an otherwise appropriate full proof.

The Forrelation preview also compresses two provenance claims. The eventual fixed-$k$ hardness input can be taken from Bansal and Sinha; the particular explicit numerical threshold belongs to the record's refinement. Later sections distinguish them. Keep that distinction in the preview. The monomial derivative example and the worked three-block calculation are particularly good: they expose repeated-coordinate cancellation before a general argument. Preserve them, including the sentence explaining that the same middle index enters and leaves.

### 3.3 Make the existing examples a coherent set of destinations

The transcript-uniqueness induction, local gate checks and pointer-support example are strong. They distinguish a circuit's correct evaluation from the desired output condition, and dependence on many coordinates from the number of bits read along one adaptive path. A newcomer reaching these passages from the exposition has a specific question; make the answer local and recognizable.

The addressed board, fractional tournament and XOR simulator each serve a sensible different purpose. Their transitions change raw strings, probabilities, candidate names, primitive functions and indexing conventions. Some changes are explained only after the new calculation. Put the purpose and reset before the example. In particular, the fractional tournament is the appropriate next step after the exposition's deterministic row, while the XOR trace teaches a shared counter and a predictor output. Neither illustrates the quantitative Forrelation lower bound at toy size.

The cap-event corollary is indispensable to the lower-bound route. It explains why an always-capped theorem can be used to bound a joint event in a larger computation without conditioning the law on that event. The minimax proof is also a good optional destination for an analyst, provided the need for one common hard distribution is stated before the convex geometry. For the undergraduate, a tiny success matrix would help identify which coordinates are inputs and which vectors represent algorithms. The transcript-prefix factorization and the simulator's abort branch then give a complete operational argument.

After the simulator table, the exact probabilities from enumeration are less illuminating than the execution itself. A brief explanation of the hidden parity cases behind the gap would help the reader distinguish the target event from the larger predictor-success event. This is a presentation request about an existing finite example; no new exhaustive project is needed.

### 3.4 Keep proof, source comparison and execution history distinct

The fixed-$k$ endpoint discussion is more precise than the exposition's shorthand and should remain the reference. The universal-upper-bound appendix has a useful dependency outline; keep the actual four inequalities close enough to the opening that a reader can see why two quadratic contributions give the quartic power. Historical threshold calculations can remain recoverable without appearing necessary for the current theorem. The source-comparison appendix correctly states that neither of its compared arguments is a dependency of the current proof. Preserve its edition boundaries and its distinction between a local mismatch and a refutation of a published theorem.

The statement catalogue and execution history have legitimate audit uses. They should not be treated as continuous reading for a newcomer. Stable claim identifiers can remain anchors without becoming the grammatical subject of proof sentences. Terms such as “the integration” and explanations that a constant was chosen to match another document sound like production history inside mathematics. Move that information to the existing maintenance apparatus or describe the mathematical slack directly. The formal inspection route should say whether an instruction asks for reading a definition, following an existing check, or executing code; those are different actions.

The current record's PDF lags its Markdown. This review therefore uses current Markdown quotations and no page locators for current-record findings. A future distribution should make the authoritative version obvious at every entry. That is a version-coherence issue, not a request to rerun formal receipts in this pass.

### 3.5 Present and desired takeaways

None of the three newcomers should be expected to read the record linearly as the next step after the exposition. The mathematician can use substantial construction, minimax and analytic routes; the physicist can use the model, decoder, sampler and verification routes; the undergraduate can profit from exact small examples and the simulator trace with guidance. These are successful uses of a long record when the entry and return links work.

The desired outcome is local auditability: a reader arrives with a specific omitted inference, sees its hypotheses and complete argument, identifies the next use, and returns to the shorter account without a notation or example surprise. Much of the record already supports that outcome. Repair the summaries, source-scope sentences and destinations first. Preserve the genuinely explanatory mathematics rather than optimizing the entire record toward the paragraph profile of a short research paper.

## 4. What the next pass should change in the method

The method already contains most of the necessary principles. The recurring failure is satisfying them individually while missing their combined effect: the frame becomes an overloaded introduction, the example becomes data that no longer match its link, and a planned move of constants is treated as a finished repair. `method_feedback.json` gives 24 specific findings tied to the supplied rules, including rules worth preserving.

The next pass should judge completion by reader operations. Can the newcomer interpret one query, perform one local check, normalize unequal successful masses, and explain the capped predictor's event inclusion? Can the reader distinguish a critical exponent from its endpoint? Can the link they follow answer the question it promises? These checks are more informative than repeatedly lowering a style score. The broad reference profile, damaged extractions and missing packaged rule IDs deserve maintenance, but that maintenance should stay in the writing method rather than becoming more process prose in the papers.
