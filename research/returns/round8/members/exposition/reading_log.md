# Reading log: four simulated perspectives

The four accounts remain separate and follow the current exposition in reading order. They describe modelled audience difficulties and the reviewer's mathematical attempts, not recruited human readers. MATH, UG and PHYS attempted the five questions before consulting the supplied answers; TEACH's recomputation was answer-exposed and is labelled throughout. The coordinating pass inspected every current exposition PDF page. Individual accounts state their own narrower visual and source-reading scopes.

These logs were consolidated from the workstreams' sequential notes and recorded attempts. Later source checks and prior-round comparisons informed the recommendations. They do not turn a reread into a fresh blinded experiment. All file paths in this return are relative to the supplied packet unless identified as online URLs.

## MATH reading log: a mathematician outside quantum computation

### Perspective and scope

This is a simulated reading perspective, not a report of a recruited human reader. The imagined reader is comfortable with finite-dimensional linear algebra, probability on finite sets, conditioning, asymptotics and proof by induction. They have not taken a quantum computing or complexity-theory course. I read the supplied current `repository/docs/exposition.md` in order, including all five questions, their answers, figure captions, disclosure and the bibliography file. I also read the expert companion’s opening through its main theorem and purpose paragraph, and followed selected record passages where this reading genuinely needed more context. This log concerns conceptual and textual navigation. I did not inspect the exposition PDF visually or execute Lean, Comparator or packet scripts.

The reading below was first formed from the current exposition. Previous-round notes were consulted afterward to distinguish a missing explanation from a deliberate, already-corrected teaching choice. In particular, the field inventory, gate calculation, unequal-weight sampler, three-budget paragraph and XOR trace are present and should not be reported as absent. Previous table removal is respected: recommendations below do not ask for prose to be squeezed back into narrow table cells.

### Introduction: I can identify the theorem, but I decode the opening retrospectively

The first sentence announces the optimal exponent before I know the two complexity measures or why totality is a dividing line. It is not incomprehensible to a mathematician; an optimal exponent is a familiar kind of result. Nevertheless, I am initially reading a theorem in a new formal vocabulary rather than being shown a problem. The next paragraph immediately improves matters. The hidden string 0010, its inspected coordinates, and the contrast with 0000 give a concrete charged operation. That is the first point at which I can explain the model to somebody else.

The explanation of the worst-case cap is very good. Fixing the input before putting probability over coins or measurement is exactly the convention I need. The early phrase about answering correctly on every input briefly sounds exact rather than bounded-error, but the definition repairs it. I would make that repair local rather than expect the reader to carry two possible interpretations for a paragraph.

The query model’s limits are well stated. I would still like a positive reason to study the idealization. The source introductions help here. Buhrman–de Wolf frames decision trees as a simpler model whose lower bounds can be understood more fully; the online IBM introduction similarly explains why this deliberately restricted setting is useful for quantum algorithmic ideas. One purpose sentence would suffice. The exposition should not add an essay on physical implementation.

The infimum defining alpha_tot is welcome. It turns “fourth power” into a uniform comparison of two measures rather than a numerical speedup on one input. The theorem then gives the quantitative family. Its explicit constants are honest but visually prominent relative to their significance. I initially ask why six logarithms and 1/400 matter, then the next sentence tells me they are loose choices. The later m-power calculation supplies the right intuition: one quantum square root and a classical factor m times almost m.

The roadmap is unusually good because it states what I should be able to do: trace a certificate, sample a pivot, and explain the hidden plant. This is a better promise than “we make the theorem accessible.” I would keep it. The prerequisite paragraph needs a slightly more accurate account of what will be imported: concentration and the capped amplification routine are not immediate consequences of elementary probability and finite-dimensional linear algebra, even though their use is reasonable.

### Section 1: the sign geometry makes the small problem real

I converted the three eight-bit strings to signs, checked Wg=(2,-2,-2,-2), and recovered the amplitudes 1,0,-1. The geometry then makes those numbers memorable: the first pattern matches the transformed second pattern, is orthogonal to it, or reverses it. This is the strongest part of the introductory example. The large negative amplitude is not simply another positive example, because the promise is one-sided. The exposition is right to make that distinction conspicuous.

I can now explain what the partial function asks on its promise. I do not yet know why a quantum machine can reveal that correlation with few queries. The unit-vector and projection discussion begins that bridge. For this reader, a basis label such as |j> is harmless notation once explained as an ordinary vector basis. The triple |j,b,w> is a slightly larger step: the workspace is introduced as a label but its later role in reversible calculation is not yet visible. A small example of something stored there would help.

The two sign diagonals and Walsh matrix are easy to multiply. Their query cost is less obvious because the phase operation has been postponed to Section 3. I accepted it provisionally, but this is the first place where one can follow the algebra while losing the computational interpretation. The later phase-kickback identity is short enough that its present separation should be an intentional teaching decision, not an accident.

The distinction between a projection event and a correct decoded answer is demonstrated well by the intermediate-amplitude example. There is a terminological burden: “success” means the selected projection outcome, not correctness. This will change again for tournament sampling and violation search. It would help to give these events operational names as they first occur.

The negative example’s certainty of acceptance is the real payoff. It explains why the total function cannot trust a decoder to certify its own promise. The final L=0 warning appropriately says that this tiny example does not itself establish a separation; its wording could be plainer than “positive-budget separation.”

### Section 2: I can trace a certificate and see why local checks work

The general field inventory is manageable after the small sign example, provided I treat P_{k,m} temporarily as a partial-function box whose general definition comes next. It introduces many indices at once, but their jobs are now explicitly different: the address selects a cell; a stored pointer selects a row in another column. The sentence allowing every assignment of input bits is vital. It makes totality independent of whether the supplied transcript is honest.

The winning conditions are compact and useful. I can prove uniqueness immediately: two all-one winning columns cannot point to zeros in each other. I can also see why an arbitrary string of stored certificate bits does not accidentally narrow the input domain. The long credit-and-parameters paragraph delays the promised concrete board. I do not want credit removed; I want the reasons for r, the history of pointer functions and the bit-cost convention to stop competing in one paragraph before the reader has seen a cell do anything.

The four-column board is an effective recurring object. The r=2 reset is explicitly limited to definitions and algorithms, which prevents confusing the toy with the asymptotic hard family. Column 2 has no true address because one address instance is off promise, although its decoder can still return a label later. That distinction is important and is maintained.

The transcript explanation uses induction in exactly the right way: every predecessor is already forced, so correct local equations force the true global evaluation. The word “circuit” should locally include acyclicity for this audience, because fan-in two alone does not imply an order suitable for induction. Once that is supplied, the proof is elementary and convincing.

The link into the record helps identify the actual circuit and tests, but it introduces a numerical mismatch: the linked preserved board has amplitudes ±1/2 rather than this exposition’s ±1. The limitation is honestly disclosed. A reader seeking a reproduction of the present example nevertheless has to identify which facts transfer and which do not. The shared circuit, gate checks and certificate geometry should be the explicit purpose of that route.

The domain-bit counterexample is excellent. All gate equations can hold while the domain output is false; circuit correctness and validity of the partial-function answer are not the same assertion. The explicit gate-2 calculation likewise shows how three queried bits can test a local equation without recomputing the whole circuit. The separate induction prevents the incorrect inference that a false stored predecessor could fool all tests simultaneously.

**Question 1 attempt.** On the domain-counterexample board, the stored value bits are 00 and the domain bits are 01. The first domain test fails at every address. At 00 no value test fails; at 01 only the second value test fails; at 10 only the first; at 11 both. Thus the total failed-test counts are 1,2,2,3. The answer agrees. This exercise checks the right distinction; an exercise that only recomputed K=371 would have taught less.

The historical AND-OR discussion gives context for the extra power, but it asks the reader to infer the exact inner Boolean function from its certificate shapes. A direct statement of “one in each row” as the one-output condition would remove that inference. The heading about the earlier construction giving a cube also compresses the chronology: the prose itself correctly starts at 5/2 and explains later improvements toward three.

### Section 3: I understand the interface; the exact circuit deserves one more conceptual step

The three-property organization works. The construction needs a cheap bounded-error decoder, an exact modest-size circuit for checking promise and value, and a classical lower bound. These are different roles, and the text now separates them.

Phase kickback supplies the missing query-cost explanation from Section 1. Its elementary eigenvector calculation is a good fit for this reader. Repetition then gives reliable decoding, although Chernoff is an imported estimate rather than something I would derive instantly from the advertised prerequisites. The constant 2^{10k} is usefully visible. “Cheap” here is asymptotic in m with k fixed, not a numerical claim about practical small instances. The toy examples have deterministic decoder outcomes and should not be allowed to obscure that distinction.

The exact circuit’s near-linear size is essential to the later cost. “Fast Walsh transform” remains more of a name than an explanation in the exposition. Following the record reveals a simple half-size recurrence with sums and differences. A brief description of that recursion would do more than another exact constant. I am not asking for the record’s word arithmetic or gate budget to be inserted wholesale.

The Forrelation classical lower bound is correctly declared as an input. I can use it without pretending I have proved it. The global-correlation intuition helps explain the quantum half more than the classical half. Aaronson–Ambainis’s introduction similarly treats the property as global and immediately separates that intuition from the substantial lower-bound theorem. The exposition should retain its explicit boundary and perhaps say a little more about the indistinguishability statement imported from the source, not replace it with a new toy argument.

The total input length is finally explicit. This is useful because m is a construction scale, not the number of input bits. I can match the three bracketed summands back to strings, address inputs and cells, but a few words naming those summands would reduce the backward lookup.

### Section 4: the ideal tournament is clear; reversibility is the main newcomer bottleneck

The failed baseline is exactly right: a direct outer search with an expensive certificate test inside would multiply two square roots and lose the intended advantage. I now know why comparisons and a short list are needed.

The pointer comparison is concrete. A zero in a rival’s string disqualifies that rival. A winner cannot be disqualified by any incoming pointer because its own string is all ones. Therefore only the winner’s own correct decoding is needed. This is the central robustness property for totality, and it is well taught. The deterministic example verifies one comparison without pretending that all real instances behave deterministically.

The first substantial slowdown for this reader comes at coherent reversible implementation. The paragraph is much better than a slogan: it says the intermediate labels remain in separate registers and gives the reason probabilities add without unwanted interference. Still, a reader without circuit training benefits from seeing one reversible computation into a fresh zero register. Recording enough inputs is the bridge between an ordinary classical rule and a reversible operation. The description should not assume that bridge is familiar merely because the reader knows unitary matrices.

The dominating-nonwinner example is a major strength. It shows that the tournament is for generating candidates, not certifying F=1. The loser cycle is independently useful: it explains why sorting or minimum finding is not a substitute. These examples should both stay, but their board modifications should have stable names to avoid tracking several incompatible meanings of “the changed board.”

The weighted ideal process is natural to a probability-trained mathematician. The operational definition of weight as the chance of beating earlier pivots is what makes the later sampler believable. The four zero-one weight outcomes let me check the first drift numerically. The general unordered-pair cancellation is elegant and uses exactly complementarity, not transitivity. I would expose the ordered-to-unordered grouping just a little more explicitly because it is the proof’s algebraic hinge.

The Markov argument is satisfying: if the winner has not yet been listed, its own weight keeps the total bounded away from zero, while the total has exponentially decreasing expectation. The process is allowed to die immediately after listing the winner. Keeping the earlier list is what makes that harmless.

The preparation’s conditional law follows from independent fresh comparison registers for a fixed column and orthogonality between different column labels. I can reconstruct the probability calculation. One schematic full state would nevertheless connect that argument to the linear-algebra language more transparently than prose alone. The unequal-weight abstract matrix is worth retaining; the concrete board would not reveal the mistake of sampling uniformly among positive weights.

Amplification is explained through the two-dimensional good/bad plane. The preserved successful-state direction is the relevant invariant, and the text correctly includes the whole retained workspace. I would not demand a full derivation of the randomized unknown-p routine. I would improve its record link: the anchor named as giving trial counts lands after M, N and the trial scheme have been introduced, so the newcomer has to search backward to reconstruct the contract’s implementation.

**Question 2 attempt.** Starting from weights (1,0,0,1) after pivot 2, choosing pivot 4 leaves (1,0,0,0). The next preparation succeeds with probability 1/4 and its successful label is always 1. Here theta=pi/6, so one Grover iteration makes the success coefficient sin(3theta)=1. The answer agrees and additionally reminds the reader that rejection of the other listed candidates remains bounded-error. This is a good use of the p=1/4 example, especially after p=1/2 was correctly shown not to improve with a single ordinary Grover iterate.

Verification changes the meaning of success: now it means finding a violation. The explicit sentence saying so must remain. I can explain why a correctly decoded true winner is accepted with certainty at this stage, whereas every false candidate is rejected with high probability because every address has some failing test. The global error bound then has a clear place for list failure, fresh winner decoding and false acceptance.

The cost paragraphs are appropriate as an end-of-section calculation. I would finish on the mechanism—cheap comparisons and a short expensive-verification list—rather than leave the loose sixth logarithmic power as the dominant memory.

### Section 5: the planted-pair reduction is teachable and the cap trace earns its length

The finite minimax explanation is good for this reader. One law defeats all shallow deterministic trees; it is not selected afresh against each particular tree. Following the record gives a finite convex-separation argument with a success-vector polytope and an orthant, a familiar mathematical structure. The exposition need not carry that proof in full.

The dummy and planted inputs differ at only two types of locations. This support-of-the-change observation gives the proof a clear task: bound an erased-zero hit and a true-cell visit on the dummy path. The latter event deliberately overcounts bits which did not actually change. That overcount is harmless and explained.

The picture’s prose needs more care about instances. It calls the planted cell column 1’s Figure 2 cell while also resampling address inputs from mu. The geometry may be the same, but the correct address and transcripts depend on those new samples. I read the picture as a schematic selected realization with address 10. That intended reading should be explicit. This is an exposition/instance-description issue, not evidence that the general coupling proof is false.

The erased-zero estimate combines two different arguments: early discoveries have small conditional probability, while late-discovered columns must each consume many distinct string reads. The text gives both, but one explicit charging sentence would show how the global G bounds the number of late columns. The independent-I example is excellent. It proves that a uniform marginal cannot replace independence from the transcript.

**Question 3 attempt.** With two positions queried in each column, each zero is found with probability 1/2. Hence E[Z]=2 and an independent planted index is hit with probability 1/2. Choosing I among discovered columns gives a hit whenever at least one is found, with probability 1-(1/2)^4=15/16. The answer agrees.

The true-cell step is the deepest classical idea, and the current wording does teach it: the query position already proposes the entire address. Deliberate learning is not required. The two direct-product counterexamples then isolate genuine assumptions. “Both hypotheses” should name its intended pair, because the displayed lemma contains several hypotheses. The joint-side-information example is especially sharp: independence from each coordinate separately is insufficient.

In the optional proof box, the key point for this reader is why adaptivity does not destroy a product conditional law once the full deterministic transcript is fixed. The explanation is correct: consistency with the transcript imposes coordinatewise constraints, and a tuple satisfying those constraints follows exactly that sequence of choices. This step deserves its own paragraph before the continuation values. The supermartingale-style product argument is then natural. A coordinate’s value may rise on a particular answer but not in conditional expectation. The small AND calculation makes that distinction explicit.

The warning against conditioning on lightness is also important. It shows why “the algorithm is cheap on this event” is not itself permission to apply a capped theorem conditionally. The simulator repairs this by enforcing a cap on every run, with a total output even on aborting branches. The three-budget paragraph should not be compressed away. It is how I check the actual hypothesis transfer.

The XOR trace changes partial function and index convention, both announced. The zero-based target column 1 is still easy to confuse visually with the earlier first column, so a local reminder about independent labels would help. The branch calculation itself is clear: the original light true-cell event has probability 1/8, while the simulator may also guess correctly on its abort branch, making total success 1/4.

**Question 4 attempt.** Moving the a=0 cell query ahead of the second target query permits that branch to be light if the run stops there. It contributes when a=0,b=0,c=d, probability 1/8. Adding the unchanged a=1 branch gives 1/4. The question could specify whether it wants the new contribution or the total; the answer correctly provides both. Its warning that a later query to c would make the whole run heavy is essential and should remain.

Finally, summing over times before averaging over I explains the missing factor m. This is not cosmetic algebra: it is the distinction between a hidden random target and an adversarially chosen target protected simultaneously in all columns. The final <1/3 gap then contradicts correctness on the planted and dummy distributions. I can reconstruct that proof without treating the all-zero cells as a promise on the total function.

### Section 6: the limit claim is precise and the endpoint exercise is useful

The floor estimates are intentionally loose. I did not interpret them as claims of optimal constants, and I do not recommend stronger bounds. The important step is replacing Q by an upper bound in the denominator, then using a positive m-power against a logarithm. The monotonicity explanation prevents a reversed inequality.

The order alpha first, then fixed k, then m growing is explicit. The nonuniform-threshold example explains why plugging in k=k(m) is a different argument. This is especially valuable for mathematicians, who may be tempted to optimize parameters immediately.

For Question 5, k=4 excludes all powers strictly below 3.5 and so yields alpha_tot >= 3.5; to exclude a uniform power-3.5 inequality itself with these estimates, k=5 suffices. The answer agrees. The matching universal quartic theorem is then a cited input with a record route. I sampled the beginning of that record appendix, which clearly identifies its general result and reconstructive role; I did not re-prove the entire sensitivity chain.

The final teach-back prompts are well chosen. They ask for the exact causal steps rather than a formula recitation. This is the right pedagogical ending before the optional formal-navigation section.

### Section 7, answers and references: the evidence distinction is clear, the code entrance needs a cue

The formal statement is approached through the same domain-bit counterexample, which is better than ending with a generic proof-assistant endorsement. The distinction between the formal family theorem’s unspecified logarithmic power and the explicit paper count is valuable and should survive revision.

For this reader, “find the clause” in Lean needs a small syntactic cue: the name of the relevant predicate or phrase and what it expresses. Importing only Mathlib is meaningful to a formalization reader but does little to help this newcomer navigate the definition. A short cue is enough; no Lean tutorial is required.

I read the five answers and the bibliography. The answers generally provide the missing scope distinctions without doing the whole exercise again. The bibliography has ordinary scholarly entries and useful source locators. Its raw BibTeX contains an extra standalone closing brace after the BHMT2002 entry; this is a source-portability observation for the parent review, not a claim that the supplied PDF failed to build.

The moving-main overview links and commit-pinned detailed links should have a deliberate edition policy. I found no current text disagreement from that alone, but a future newcomer could follow two different versions of the record without knowing why their examples differ.

### What this reader can now say to a friend

A query measures how many input bits an algorithm needs to consult, allowing all other calculation for free. For total Boolean tasks, quantum algorithms can be almost a fourth power cheaper than randomized ones, but no universal power larger than four is needed to simulate their query advantage. The constructed task has many columns. A true winner is all ones and has an honestly certified cell, hidden at an address made from hard partial-function answers, pointing to zeros in all other columns. Quantum algorithms can obtain those answer labels cheaply enough to compare columns. The comparisons need not sort the losers: a weighted process halves its total weight on average while an unlisted true winner keeps substantial weight. Quantum preparation and amplification sample that weight law without calculating the weights; the algorithm retains a short list and checks its certificates.

Classically, a random winner can be planted by changing just a string zero and one hidden cell. Finding the changed zero is unlikely with few queries. Visiting the correct cell, even by a lucky guess, already proposes all the hard address answers. A capped simulation converts such a visit into a simultaneous predictor; an independent-input direct product bounds its chance. Heavy columns are few, and averaging over the hidden target yields a lower bound of order m times the address-hardness scale. Comparing that with quantum square-root m cost gives thresholds 4-2/k, and the fixed-k limit excludes every exponent below four.

This is close to what the reader should say. The remaining honesty clauses are that Forrelation hardness and the universal upper bound are substantial imported results, the tiny board does not establish asymptotic hardness, “four” concerns a family and an infimum rather than a practical fourth-root running-time promise, and the explicit logarithmic count is not exactly the formal family theorem’s statement.

### Overall MATH verdict

I would read this to the end. Its current mathematical spine is coherent and much stronger than a merely polished summary. The signed examples, exact domain counterexample, dominating nonwinner, unequal-weight sampler and capped predictor are genuine teaching devices. I found no demonstrated error affecting the separation theorem in this pass. The residual work is mostly interface work: first-use computational meaning, consistency between a pictured realization and a distributional description, the precise entry point of linked proofs, and the amount of independent context packed into single paragraphs. Those are worth fixing because they determine whether an outsider understands the method rather than merely trusts its formulas.


---

## UG reading log: a strong final-year undergraduate

### Perspective, procedure and limits

This is a simulated mathematics/CS undergraduate perspective, not evidence from a human participant. The assumed background is finite-dimensional linear algebra, elementary probability, asymptotic notation, algorithms and the names P and NP. Quantum measurement, query trees, distributional lower bounds and direct products are new material. The introductory model passages in Buhrman–de Wolf and de Wolf provide the comparison baseline; their advanced proofs are not assumed prerequisites.

This account consolidates notes from a sequential reading of the complete current exposition. The five attempts were saved separately before consulting the answer section; their results are reproduced below. The expert companion's introduction and relevant record targets were read afterward to distinguish a deliberate import from an unexplained local step. All 20 pages of the current exposition PDF were also rendered and visually inspected. Those page observations are a separate layout pass, not claims about what the Markdown alone reveals. No supplied executable, Lean build or Comparator was run.

### Introduction: an attractive comparison arrives before its vocabulary

The opening announces an optimal fourth power. I recognize what an exponent is, but not yet what the two quantities measure or why total Boolean functions matter. The four-bit OR task supplies the necessary handle: I can now count individual observations and understand why an unseen coordinate can prevent a certain answer. The distinction between input length and number of queries is more useful to me at this point than the exact theorem constants.

The model definition succeeds when it fixes an input first and locates randomness in the algorithm. I can explain the all-branch cap after that paragraph. The physical-oracle sentence also prevents me from mistaking query savings for an equal saving in runtime. Those are clear boundaries with an actual purpose.

There is one avoidable task change. Searching for the position of a unique 1 is meaningful, but deciding OR under the promise that exactly one 1 exists is constant. The text uses the former to illustrate partial Boolean functions without stating its output. I can infer the intention; a beginner should not need that inference while learning the distinction itself. This is a local ambiguity, not a counterexample to the theorem.

The infimum definition gives a precise target but is demanding for my first page. I need its universal quantifier in words more urgently than I need every symbol. The statement with fixed k, powers-of-four m, six logarithms and 1/400 is honest, and the subsequent power-only comparison helps. I would introduce that comparison's purpose before asking the reader to attend to its lower-order factors. The caveat that these are directional bounds is essential: I must not retell the result as a proof that each query complexity equals its displayed estimate.

The promised outcomes are unusually useful. Tracing a certificate, sampling a pivot and explaining the hidden plant are things I can try. The prerequisite list should, however, distinguish probability I am expected to know from concentration, minimax and amplification facts the article imports. “The deeper inputs” sounds exhaustive when the reading later needs additional named tools.

### Section 1: I can do the arithmetic before I know its job

My first substantial loss occurs at the displayed W matrix. I can multiply it, and can translate 0/1 into signs, but I do not yet know what question the matrix will let a quantum procedure answer. The later geometric paragraph resolves much of that uncertainty. Introducing the correlation being measured before the full matrix would make the calculation an answer to a question rather than an exercise in waiting.

Once the three inputs are available, the computation is satisfying. Their common second block transforms to the stated sign pattern; the first blocks align, are orthogonal, or point in the opposite direction. The amplitudes 1, 0 and −1 then have a visible meaning. The one-sided promise matters: the negative case is excluded, although its squared amplitude is 1. I would retain that example through any shortening.

The unit-vector explanation gives me a plausible mathematical description of a quantum state. The oracle triple introduces a new difficulty: a workspace label is named before I have seen a reason to store intermediate data. Later it will be crucial that these labels remain in the state. One small example of a register holding a computed bit would make this first mention prepare its eventual role.

I understand that one query acts linearly on a superposition and that measurement does not reveal the entire input. The phase-query construction is deferred to Section 3, so I provisionally accept the two-query cost of the displayed experiment. This is an explicit deferral, not a missing argument; its cost is that the first example's computational interpretation arrives after the next major construction.

The intermediate example with amplitude 1/2 is important. It prevents the three extreme examples from teaching the false rule that every promised input is decided after one trial. A little more emphasis on the difference between a projection outcome and a correct decoded bit would help, because “success” will later name several different events. The final warning about the toy's zero hardness budget is also necessary. I can use this example to learn the mechanism without claiming it witnesses the asymptotic lower bound.

### Section 2: the certificate is convincing once its pieces have jobs

The initial general column inventory asks me to hold m, k, r, ell, S, an address array, transcripts and pointers simultaneously. It is precise, but I still want one cell to perform a task before I memorize its storage format. The distinction between an r-bit cell address and an ell-bit pointer to a row is especially good; it prevents two unrelated indexing operations from merging in my head.

The four winning conditions and the explicit statement that every assignment of input bits is allowed make totality concrete. A dishonest transcript is an ordinary input whose claimed certificate must fail. It is not a reason to exclude that input from the function's domain. The short uniqueness proof is then reconstructible from the all-one string and the outgoing zero pointers.

The paragraph combining cheat-sheet credit, the choice of r, a later tail bound, cell size and alphabet encoding is heavy at this exact position. Each fact is useful somewhere. Here I am waiting for the promised board. Keeping brief credit and placing the numerical design reasons near their uses would improve the sequence without suppressing predecessors.

The four-column board lets me identify the winning column and the zero reached by each pointer. Column 2's off-promise input means it has no true semantic address, even though all of its physical cells exist. That is a difficult distinction worth teaching explicitly, and the article does teach it. The reset to r=2 is also clearly marked as a teaching miniature.

The local-circuit argument is persuasive. If every gate agrees with its predecessors, induction forces the true computation; demanding the appropriate outputs is a separate test. The changed board shows why the domain bit is indispensable. I can now explain why a correctly evaluated circuit may still certify that an address input is outside the promise. This is better instruction than another unmotivated gate count.

The actual gate-2 example is helpful, although switching from one-based board positions to zero-based circuit inputs makes me recount the string. The K=371 calculation has a clear checking role. Its exact value should remain subordinate to the four test families and their constant query costs.

The checker link introduces another example with different positive and negative strings. The mismatch is disclosed accurately, so it is not an inconsistency to accuse the authors of hiding. It is still a learning cost. A reader following a reproduction link expects the current board; the landing explanation should say immediately which checks transfer and which decoder probabilities change.

#### Question 1: attempt made before reading the answer

On the changed board, column 2 has domain outputs (0,1) and value outputs (0,0). The first domain test fails at every address. At 00 there is no value mismatch; at 01 and 10 there is one; at 11 there are two. The resulting counts are 1, 2, 2 and 3, with the string, pointer and gate-consistency tests passing. This matches the supplied answer. The question tests why domain checking is logically separate, not merely whether I can reproduce a formula.

The subsequent AND–OR history is harder to reconstruct. I need the phrase about composition to specify that an inner problem supplies each outer input bit. Until that is said, I cannot confidently reproduce which n controls which board. The historical comparison earns its place when it explains the extra quantum cost that this construction removes.

### Section 3: three interfaces, three different kinds of knowledge

The separation into cheap quantum decoding, an exact circuit and classical hardness is effective. These are distinct promises needed by different parts of the construction. I should not infer that an efficient decoder proves exact domain membership, or that an exact circuit has to be evaluated from scratch by the verifier.

Phase kickback finally closes the operational gap from Section 1. I can follow the minus eigenstate and see why the answer register is restored. Repetition introduces a probability estimate I would probably take as a lemma: the rule is separating rare-event rates, not simply voting on a bit whose success is already greater than one half. The visible dependence on k is useful because it explains what the fixed-parameter convention buys.

The fast Walsh circuit is named more than explained. I would understand the near-linear arithmetic count better after one description of recursively reusing sums and differences. That explanatory bridge is already in the record; it need not bring all finite gate constants into the exposition.

The classical hardness statement is correctly identified as an imported theorem. The global-correlation explanation motivates it but does not pretend to prove it. The total input-length calculation then establishes an important scale check: m is a structural parameter, and the quantum and classical costs concern the same total function and the same circuit choice.

### Section 4: the central idea is strong; its probability layers need more space

The failed nested search is an excellent opening. I can explain why paying a square-root verification cost inside a square-root search loses the desired saving. The tournament's purpose is to propose a short list cheaply and reserve costly verification for that list.

The comparison convention deserves careful reading. Sorting the pair before using the same experiment gives complementary probabilities; the index tie rule handles both pointers succeeding or neither. The dominating nonwinner is an essential counterexample: comparisons alone cannot decide the function. The cyclic losers explain why I cannot replace the construction with ordinary minimum finding.

The ideal weights have a good interpretation as chances of defeating previously selected pivots. The algorithm never estimates those weights. I can check the halving calculation, but I would benefit from seeing one unordered pair's contribution before the general sum. The winner survives until selected while total surviving mass contracts; that is the mechanism I should be able to teach back.

The abstract fractional matrix is valuable because it removes the accidental determinism of the toy board. I recompute the post-pivot weights and can distinguish the joint success probability w_i/m from the label law conditional on success. The article is right to label this matrix abstract rather than suggest that it has been implemented by another board.

The largest quantum gap for me is the passage from fresh comparisons to a product of probabilities. A mathematical register display showing fresh workspace for each comparison would make its independence visible. Retaining labels prevents the inappropriate interference between distinct histories; it does not turn the whole state into a classical mixture. I can accept the paragraph as written but would struggle to reconstruct that distinction without a diagram or a second worked register example.

Amplitude amplification adds another layer. The successful direction includes all workspace, not just the column label, and preserving that direction preserves the conditional label law. The formula is understandable; the reflections themselves are less so for a first quantum encounter. A two-dimensional picture with the prepared state and successful direction would address the actual obstacle. The first numerical illustration preserves probability 1/2 without increasing it; the later 1/4 case is a clearer demonstration of improvement.

#### Question 2: attempt made before reading the answer

After pivots 2 and 4 on the cyclic board I obtain weights (1,0,0,0). The preparation succeeds with probability 1/4 and, on success, returns column 1. With theta=pi/6, one Grover iterate gives sin-squared(3 theta)=1. The answer agrees. This establishes the special example, not exact verification or monotonic improvement on arbitrary inputs.

The all-input cap, the stopped coupling and retention of every earlier pivot are safeguards I would preserve. A later failure cannot erase an already listed winner. Verification must also keep its event convention straight: finding a violation rejects a candidate, and absence of a found violation after a bounded search is not an exact certificate of correctness. The final cost discussion successfully attributes the square root to short-list sampling and verification; the sixth logarithm is secondary accounting.

### Section 5: a convincing plant once the conditioning is unpacked

The hard distribution is a mathematical tool, not a hidden rule the algorithm is forbidden to know. I understand why the algorithm may know its law but not its sampled address inputs. The dummy and planted inputs differ only at an erased zero and the newly filled cell. The common-transcript argument should be read as an induction up to the first differing answer, which is more precise than a general intuition that the inputs are close.

The erased-zero calculation gives a particularly good warning about independence. I can compute both the independent planted-column case and the dependent selection rule, even though the latter has the same uniform marginal. The early/late charging argument is correct, but its two charges should be visually separated so I do not mistake the bound for a claim that every fresh query has small success probability.

#### Question 3: attempt made before reading the answer

With two fixed positions queried in each of four columns, an independently selected column's zero is found with probability 1/2. Under the dependent selection rule, a found zero is selected whenever at least one column was hit, giving 1-(1/2)^4=15/16. This agrees with the answer and directly tests the hypothesis used by the coupling.

The true-cell explanation is the lower bound's most memorable idea: an address is already encoded in the position of a query. A visit can therefore reveal a correct proposed answer vector even when the algorithm never explicitly computed those answers. This addresses blind guesses and repeated cell visits.

The direct-product box is optional but difficult. My main pause is why conditioning on an adaptive transcript preserves independence. The deterministic-tree rectangle argument supplies the reason, but it shares a paragraph with the continuation-value construction. Those are two conceptual steps. I would give them separate entrances. The later example showing that lightness is not a legitimate conditioning event is strong and should remain nearby.

The three-budget paragraph resolves a real possible misunderstanding. Total budget G, a simulator's total allowance L in one column, and the direct product's allowance L per instance are different objects. The simulator satisfies the last requirement because the second is stronger. This is clear once said, and should survive any shortening.

The XOR trace then makes the stopped simulation concrete. I obtain 1/8 for the original light true-cell event and 1/4 for total predictor success, including a lucky default. The inclusion need not be equality. The example's switch to XOR and zero-based columns is explicitly announced; a brief reminder would make the transfer back to the board easier.

#### Question 4: attempt made before reading the answer

If the modified a=0 branch stops after its early cell query, it contributes on a=0, b=0, c=d, an event of probability 1/8. The unchanged a=1 branch contributes another 1/8, so the full light true-cell event has probability 1/4. If the modified branch subsequently reads c, it becomes heavy and its earlier cell visit is excluded from the whole-run light event. The supplied answer makes both scopes clear. The question itself should ask separately for the new branch and the full event, because “the event” can refer to either.

The final averaging over I explains why there is no extra factor of m. It deserves its displayed calculation. The three-term gap bound is then a summary of mechanisms I have encountered, not an unexplained inequality.

### Section 6: I can now state what approaches four

The exponent calculation is clearer than the first-page slogan. Keeping k fixed while letting m grow controls its hidden constants; choosing k only after choosing a proposed exponent below four gives the universal conclusion. The monotonicity step uses a quantum upper bound in the correct direction. No matching quantum lower bound is claimed.

#### Question 5: attempt made before reading the answer

At k=4 the power threshold is 3.5, so this family excludes every alpha below 3.5 and implies the infimum is at least 3.5. It does not by this calculation exclude the endpoint inequality itself. Choosing k=5 gives d=1/20 for alpha=3.5. This matches the answer. It is the most important question for preventing an inaccurate final summary.

The brief uniform-parameter extension is correctly bracketed as unnecessary here. I would keep the optional route clearly separated from the argument just completed.

### Section 7, answers and rendered pages

The formal-evidence section distinguishes a theorem statement from proof and comparison evidence. Natural-language link labels are a clear improvement. A first-time Lean reader could still use one syntax orientation before being asked to locate a clause. The unspecified logarithmic exponent in the general formal statement is disclosed; I should not claim that this exact statement literally contains the exposition's power six.

The answer section confirms all five attempts. A small diagnostic sentence after each answer could explain what a particular wrong response would misunderstand. The references establish credit, but their rendered presentation still has a long URL split on page 19 and a page 20 containing only two entries.

The PDF inspection found useful figures but uneven pacing. Figure 1 on page 4 has small labels relative to the body. Figure 2 is the necessary board anchor. Figure 3 occupies page 9 alone, leaving substantial white space around a large legend. Figure 4 on page 14 interrupts the early/late sentence begun on page 13. These are observed layout issues; the previously removed prose tables, raw Lean identifiers and orphan question label should not be reported as current defects.

### Final teach-back and what still needs support

My defensible teach-back is that the article constructs total Boolean functions with a cheap quantum route to a short list of possible winners and a classical obstacle to finding the planted winner. Exact stored circuits certify that the partial-function addresses really belong to their promises. Quantum comparisons support a weighted tournament, but final verification is still necessary. Classically, the planted change can be exposed only by finding the erased zero or visiting the correct addressed cell; the hard law and capped predictor bound the latter. Fixed k gives thresholds below four, and selecting k after a proposed exponent rules out every smaller universal exponent.

That is close to the intended conceptual endpoint. I can independently reproduce the five small calculations and explain why the negative-amplitude, dominating-nonwinner and dependent-column examples are needed. I would still want support reconstructing the retained-workspace product state, the amplification reflection picture and the conditional-product proof. Those are the narrow places to spend explanatory effort. Adding more exact constants or more evidence bookkeeping would not repair them.


---

## PHYS reading log: a circuit-trained physicist or engineer

### Scope and status

This is a simulated reader perspective, not a report of a study with a human physicist. The modelled reader knows finite-dimensional quantum states, computational-basis measurement, unitary circuits, Hadamard gates and the usual Grover story from a first course. They do not know decision-tree complexity, cheat sheets, pointer functions, minimax lower bounds or direct-product arguments. The supplied de Wolf notes, particularly their query-model discussion and Grover/amplitude-amplification sections, anchor what this reader can reasonably bring. Buhrman–de Wolf §3 anchors the unfamiliar query-complexity vocabulary.

I read the current exposition in order, including all five exercises before consulting their answers, the final Lean/AI statements and the bibliography. The log below preserves the order of that first pass. The literature and previous-round comparison was performed afterward; it changes the advice, not the account of where the first pass became difficult. I subsequently read the expert companion's introduction and selected construction passages, the linked quantum/circuit/simulator passages of the record, and the primary sources identified in `physics_sources.json`. I did not compile Lean, run Comparator, execute supplied example scripts or visually inspect the rendered PDF. Figure comments in this workstream concern the caption and its mathematical role, not measured print readability.

### Introduction

The first paragraph gives a result I can understand at the level of powers, although “answer correctly on every possible input” initially sounds like exact computation. The next definition resolves that: the same error bound holds for each fixed input, and the query cap applies to every outcome branch. I appreciate the physical-oracle boundary. It says what resource the result measures before I have a chance to import hardware gate counts or memory-loading costs.

The four-bit OR example is well chosen. I can understand one query without knowing a decision tree. The comparison with Grover immediately gives a reference point for “fourth power.” The total/partial distinction then produces the first small hesitation: “search promised exactly one 1” is a search task, whereas the surrounding functions return one bit. If the output is merely OR, that promised task is constant. I can repair the sentence mentally, but it is an avoidable change of task during the introduction of a new definition.

The infimum defining the universal exponent is mathematically readable. The quantifier over all functions and all lengths is more important than the notation, and the text says so. The exact theorem nevertheless gives several numbers before I know their roles: a power of four for m, a constant depending on k, logarithmic exponent six, coefficient 1/400. I initially inspect those as if they were part of the physical mechanism. The text later says they are loose counts; that comment should control the emphasis from the start.

The paragraph about one hidden winning certificate is a useful map. I understand that there will be a cheap way to propose addresses and a more expensive way to validate them. I do not yet understand why a classical procedure must pay for many columns rather than getting lucky; the introduction properly promises to bound that possibility. The power-only calculation gives a target I can keep in mind. It also expressly says these are directional bounds, which matters: the quantum complexity is not being proved equal to a square root.

The article states its prerequisites and provides two routes through the hard proofs. I would choose the quantum route first, accepting the lower-bound statement provisionally. The list of things I should be able to do at the end is concrete: trace a certificate, sample a pivot, explain the plant. This is a real improvement over a document that only announces that its proof is intuitive.

### Section 1: three eight-bit inputs

The sign encoding and 4-by-4 matrix are manageable. I multiply W by the common second block and recover the stated vector. The three first blocks then give amplitudes 1, 0 and −1. The geometry is a good use of my existing linear algebra. I would recognize H much faster if it were identified immediately as two ordinary Hadamard gates in the displayed binary ordering.

The tiny threshold initially looks like a measurement-resolution issue. The sentence about multiples of 1/8 resolves the toy promise, and I see that only the signs and zero matter in these three examples. I would like the text to mark the threshold as inherited from the general construction, so that I do not start treating it as a numerical choice this toy explains.

The state/measurement primer is short enough not to obstruct a reader who already knows it. The oracle formula is the right new object for me: one application is an access to the Boolean input, and everything input-independent is free in this model. The phase query is deferred to Section 3, but the promise of that explanation is explicit.

The projection experiment is almost a circuit I can draw. The final “input-independent change of basis” feels unnecessarily abstract: H itself takes the uniform vector to the all-zero basis state. One named final gate would finish the operational picture. The three measured probabilities 1, 0, 1 show very clearly why a measurement of the squared amplitude loses the sign.

The extra 1111 1000 example stops me from believing that one trial solves the whole promise. I calculate its amplitude as 1/2 and hence its projection probability as 1/4. That is the first example that actually motivates repetition; a short displayed calculation would earn its place as much as the three extreme examples do.

The final paragraph is the payoff: a partial-function decoder may accept the negative-amplitude input, but a total-function certificate cannot rely on that response to establish a domain claim. I now understand why the construction needs two logically different tests. I also understand that the tiny instance does not demonstrate the asymptotic separation.

### Section 2: one column and the board

This is my first substantial stall. The column contains a bit string, several hard instances, and an array of cells. The address and pointer lengths are carefully distinguished. But the cell suddenly contains circuit transcripts before the domain/value task of the classical circuit is explained. Knowing quantum circuits does not supply the missing reason to store this particular computation. I keep reading with an incomplete picture of what the cell certifies.

The winning conditions resolve the logical shape: an all-one string, valid address inputs, consistent stored computation and outward pointers to zeros. The uniqueness argument is immediate once these conditions are visible. I would still benefit from knowing at the first transcript mention that the stored circuit computes both promise membership and the promised value.

The long genealogy paragraph arrives before I have manipulated a full board. It contains important attribution, but too many different explanatory jobs: address length, a future direct product, a union bound, polynomial array size, predecessor pointers and alphabet encoding. I expect the four-column example here and instead have to defer it for one more dense paragraph. Short credit plus one design reason would be enough before the board; the specialist distinctions could follow later.

The four-column example becomes concrete quickly. I can find the zero in each losing string and check column 1's outgoing pointers. I also see why column 2 has no semantic address although every cell still exists. The announcement that r=2 is only a teaching choice matters. It would be wrong to infer the general lower bound from this miniature board.

The transcript explanation repairs my earlier uncertainty. The induction over gate order is the right proof: local equations force the true evaluation even on an off-promise input. The domain bit then does a different job from merely checking those equations. The source/checker paragraph is honest about the distinct boards, but its location makes me translate between two examples just as this one has stabilized. I would prefer the record landing passage to carry the detailed version correspondence.

The changed board is excellent. I reconstruct why column 2 satisfies string, pointer and gate-equation checks at address 00 and still fails its first domain-output test. This is a complete explanation of a necessary hypothesis. The gate-2 check is also useful, though I have to recount the input string because this inherited gate list uses zero-based input labels while the board uses one-based row positions. Marking the two bits would let the reader concentrate on the query logic.

The count K=371 is understandable once the four test types are distinguished. One small question remains: if outputs are already gates, why test them again? The intended answer is clear from the changed board: checking that an output is correctly computed does not demand the domain/value output required by this candidate. Saying that explicitly would prevent a false double-counting objection.

#### Question 1: attempted before the answer

I obtain domain outputs (0,1), value outputs (0,0), and passing string, pointer and gate tests at every address. The first domain test always fails. Relative to address 00 there are no value mismatches; at 01 and 10 there is one; at 11 there are two. Thus the failure counts are 1, 2, 2 and 3. The answer agrees.

The historical AND–OR discussion then moves to a new input length n. I can understand its row certificates, but the composition needs one explicit sentence: each input bit of the outer partial function is supplied by an inner AND–OR problem. Without that sentence I briefly imagine one inner problem supplying the whole outer string. Once repaired, the comparison explains why reducing the quantum search scale is the key design change.

### Section 3: the general partial function

The general formula is a natural extension of the toy. The binary indexing could be made more circuit-friendly by saying that the position register has 2t qubits and k counts queried sign layers. The data being queried contain km Boolean entries; they are not a km-qubit input state. This distinction has been implicit since the beginning and becomes valuable again at scale.

Phase kickback is correctly derived. I can see exactly how the answer qubit returns to the minus state while the position register acquires a sign. The repetition rule is also precise, but it is not ordinary majority voting: it separates two rare-event rates c/4 and c. Naming that feature would make the c inverse factor less surprising. The explicit 2^(10k) is useful rather than discouraging. It explains why “cheap” means fixed-k cheap as m grows.

The exact circuit is the important bridge to verification. Its output specification is clear and its use of integer arithmetic explains why domain membership can be certified exactly. The near-linear size is mostly a supplied fact in this exposition. A signal-processing reader could understand the mechanism with one Walsh butterfly identity, while leaving all finite gate constants in the record. I do not need the full arithmetic construction here, but I need a reason that it is small enough to search.

The hardness statement is clearly identified as an input theorem, not something proved by the quantum interference picture. That restraint is good. “Shallow classical decision tree” is the first distinctly TCS object that I have to infer. A short definition as an adaptive bit-query tree would prepare the whole lower-bound half.

The total-input-length calculation is useful as a scale check. It confirms that m is not n, and that the result compares two query costs for the same function and fixed circuit. I do not interpret it as a practical implementation estimate.

### Section 4: tournament, sampler and verifier

The first paragraph tells me exactly why naive Grover fails: the expensive local verification sits inside another search. This is the conceptual entry I need. Cheap comparisons generate a short list, and expensive verification is paid only for that list. The high-level loop is now present, but I would draw it with a clear classical/quantum boundary: each stage is coherent until its label is measured; subsequent stages use a classical pivot list.

The pairwise comparison is understandable. I need to notice that the tie rule covers both pointers finding zeros and neither doing so. Sorting the unordered pair before running the one experiment is a careful convention. It gives complementary probabilities for the two requested orientations without inventing an underlying deterministic order.

The reversible implementation paragraph is mathematically plausible to me, but very dense. It simultaneously defers measurements, computes counts, retains labels, performs controlled pointer reads, writes an outcome flag and explains why different labels do not interfere in the final probability. I would like one annotated register state. The complete state remains coherent; only the measured output law is calculated as a sum over orthogonal label branches. The exposition says this correctly, but makes the reader supply the drawing.

The winner-only guarantee is the first major breakthrough. No rival pointer can find a zero in the winner’s all-one string, regardless of what an off-promise decoder says. The winner’s correctly decoded cell then disqualifies the rival. I can now explain why totality does not destroy the cheap comparison.

The dominating nonwinner prevents a seductive mistake: search success is not yet decision success. The changed pointer leaves column 1 dominant while invalidating its certificate. I would keep this even in a shorter paper. The cycle among losers then shows that the comparison process cannot sort the candidates. The subsequent specialist comparison to HMW search is accurate but less useful for this reader than proceeding directly to the replacement process.

The ideal weight process is a good abstraction because the text expressly says the algorithm never knows or estimates its weights. The deterministic cycle gives a useful first update. I reproduce the four possible totals, 0, 2, 2, 2, and their mean 3/2. The general half-drift identity is short enough to check; I would separate the off-diagonal pairing from the vanished diagonal to make the exact role of complementarity unforgettable.

The survival argument is also recoverable: until chosen, the winner retains almost all its weight while the expected total decays. Markov then bounds the chance that it remains missing. One point deserves an extra sentence for a circuit reader: the T factors in the winner’s survival product are not the many physical comparison calls used inside amplification. The actual probabilities already include decoder errors.

The sampler paragraph contains the most important new operational argument. With input, history and candidate fixed, the separate fresh comparison workspaces give a product of probabilities. Orthogonal candidate labels then allow those products to add. This is right, and it is more informative than a black-box sampling claim. Still, the source preprint’s short tensor-product preparation would make the explanation easier to reconstruct than prose alone. It would also make clear that w_i/m is a squared norm, not an amplitude.

The deterministic preparation after pivot 2 works by hand. The abstract fractional matrix is a worthwhile supplement; it is explicitly not claimed to be a new realization by the board. I check the sum 23/12, success probability 23/48, joint masses and normalized law. That computation teaches the distinction between uniform support and weighted sampling. I would retain it.

The good/bad decomposition properly includes all workspace. This is a major strength. The label marginal need not be pure; the vector being rotated is the full successful component. The reflection about the prepared state can be implemented using the preparation and its inverse. A small conjugation formula or circuit would let me connect that geometric statement to gates immediately.

The unknown-success-probability contract has exactly the clauses needed later: a cap on every branch, a success guarantee only above gamma, and certain reported failure at zero success probability. The p=1/2 example intentionally shows no probability improvement, only preservation. It is a valid cautionary case, but I would prefer to see the existing p=1/4 improvement before or alongside it rather than only in an exercise.

The real/ideal coupling is sound after a careful second read. The failure probability is charged along each common history only before the winner has appeared. Afterward the retained list makes termination harmless. Dividing this into before/after cases would make the reasoning easier to reproduce without adding any new theorem.

#### Question 2: attempted before the answer

Starting from (1,0,0,1), pivot 4 leaves (1,0,0,0). One preparation succeeds with probability 1/4 and the conditional next pivot is 1. Since theta is pi/6, one Grover iteration takes the success probability to one. The answer agrees, and correctly warns that this exact amplification fact does not make subsequent bounded-error rejection of losing candidates certain.

Verification now uses success to mean finding a violated test. The bold warning is helpful and should stay. I understand why every address of a nonwinner has at least one violation, including a meaningless off-promise decoded address. I have one small implementation question about the concrete 371-test example: a uniform state on 371 labels is not obtained by an unqualified bank of Hadamards. The model allows a free input-independent preparation, so one sentence resolves it without padding details.

The final error bounds are consistent with the stated parameters. The cost section also distinguishes actual branch-dependent counts from fixed caps. Its most important closing message should be the architecture: two separately bounded square-root jobs are added, whereas the failed direct approach nested one inside the other. The explicit logarithm counts are secondary to that contrast.

### Section 5: the planted pair

I enter this section knowing the advertised lower bound but not yet its proof. Minimax is sensibly explained as producing one distribution hard for every capped deterministic tree. I would connect it still more directly to worst-case correctness: an algorithm correct on every promised input must also be correct on average under this hard law. There is no physical sampling or state-preparation assumption here.

The dummy/plant construction is concrete. Every dummy column has a zero and every cell is blank; planting erases one zero and fills one addressed cell. I understand why this creates a true winner. Figure 4’s fixed address 10 should be labelled as one realization of the new random address inputs, since this is a different use of the board from the off-promise quantum example.

Fixing the algorithm’s coins produces a deterministic adaptive query rule. The equal-transcript observation is the real reason for the coupling bound: until an altered coordinate is read, identical earlier answers force identical later queries and output. I can derive the probability inequality once that induction is stated in my own words.

The erased-zero count is a clean argument, but it requires careful probability scope. The uniform-but-dependent selected column is an excellent counterexample: it shows why marginal symmetry alone is insufficient. I would not cut it as mere cautionary prose.

#### Question 3: attempted before the answer

Two fixed distinct positions per column find each zero with probability 1/2. The independent selected column is hit with probability 1/2. The dependent selection misses only when all four columns’ zeros are missed, probability 1/16, so it is hit with probability 15/16. The answer agrees.

The true-cell argument explains a subtle point clearly: selecting the position of a cell already proposes all the address bits, even before reading its contents. The heavy/light split bounds the chance that the planted column is one of the few heavily queried columns. The separately capped direct product then controls what a light-column predictor can do.

The two counterexamples before the direct-product proof are useful but introduce further small functions. I can keep them separate because their purposes are stated: pooled budgets and merely individual independence are insufficient. The optional proof is where this reader slows most in the classical half. I need first to understand why conditioning on an adaptive deterministic transcript leaves a product set of possible inputs, and then to understand the best residual-budget success value. Those two steps deserve separate paragraphs. Once I view V_h as a value function with queries remaining, the nonincreasing expectation argument is intelligible.

The warning about conditioning on cheap runs is necessary. The simulator resolves it constructively by aborting before exceeding its actual cap and still producing a defined output. The three-budget paragraph is particularly helpful: a total target budget of L meets the L-per-instance requirements automatically. This is not the forbidden pooled-budget inference, because it is a restriction to a smaller allowed class.

The XOR trace is another reset of the small example, but this reset has a clear purpose and is explicitly announced. I calculate 1/8 for the light true-cell event and 1/4 for total simulator correctness. That comparison makes the direction of event inclusion tangible.

#### Question 4: attempted before the answer

On the changed a=0 branch, the cell is queried after only one target query. If the run stops there, it is light and the queried address is correct exactly when a=0, b=0 and c=d, with probability 1/8. The unchanged a=1 branch contributes another 1/8, so the probability of a light true-cell visit somewhere on the whole run is 1/4. I was initially unsure whether the question wanted the branch probability or the two-branch total; the answer gives both. The answer’s warning about a later query to c is useful, because lightness is defined for the entire dummy run.

The averaging over the planted column removes the extra factor m; the text spells this out. The final constants establish a gap below 1/3, while correctness on the two kinds of input would require a gap at least 1/3. I understand the proof architecture. I would still need a deliberate reread to reproduce the optional direct-product proof unaided.

### Section 6: exponent and quantifiers

The floor calculation is routine. The more valuable step is the monotonicity used to substitute a quantum upper bound into the denominator. I can now explain why the argument does not require a matching estimate for Q.

The order alpha, then k, then m is clear. The counterexample to casual growing-k substitution is effective and connects to the explicit exponential-in-k decoder cost. I do not leave thinking that a fixed small k gives an exact fourth-power equality.

#### Question 5: attempted before the answer

For k=4 the threshold is 3.5, and all strictly smaller powers are excluded. Thus alpha_tot is at least 3.5; the endpoint inequality itself is not excluded. Taking k=5 gives threshold 3.6 and excludes exponent 3.5. The answer agrees.

The final return to the two mechanisms is useful. It asks me to state the conceptual arguments rather than merely repeat the exponent division. The universal quartic upper bound remains a cited input, which is a reasonable boundary for this exposition.

### Section 7, answers and references

The formal-statement section is short and tied to the changed board. It gives me an actual clause to inspect rather than only announcing that Lean succeeded. The difference between the displayed logarithmic power and the formal family theorem’s unspecified power is also explicit. “Separately compiled challenge statements” is still specialist vocabulary; I need a plain description of the tool’s statement-matching role. The next sentence correctly says that reading definitions remains necessary.

All five supplied answers agree with my calculations, with the scope ambiguity noted for Question 4. The AI attribution is direct and preserves OpenAI’s authorship of the theorem and construction. I read the bibliography entries but did not independently verify every entry’s metadata. The `.bib` source contains an extra standalone closing brace after the BHMT entry; this workstream has not established any rendered consequence, so it is an integration note rather than a mathematical finding.

### Teach-back and assignment verdict

**What this simulated reader can say after a first pass:** a carefully constructed total bit problem hides an exact certificate at an address made from partial-function answers. Quantum computation can decode those answers cheaply and use comparisons to find a short candidate list. Classical computation has to find a plant hidden both among columns and among addresses. The different query scales approach a fourth power.

**What a satisfactory teach-back must add:** comparisons only need a one-sided reliability property against a genuine winner; losers can form cycles or have fractional comparison probabilities. The weights are analytic probabilities, not data estimated by the algorithm. Fresh coherent comparisons and full-workspace amplification sample the correct conditional law; every sampled pivot is retained, and exact local predicates are checked by bounded-error search. In the lower bound, equal answers couple dummy and planted runs, reaching a true cell is already a proposed address, and the capped simulator bounds a joint event rather than success conditioned on staying cheap. Fixed k and growing m are taken in the specified order.

I would read this to the end, but as a study text with written working rather than as an effortless introduction. The quantum argument is now substantially reconstructible and its delicate points are stated correctly. The remaining barrier is the amount of state, control flow and probability scope encoded in long prose paragraphs. A small circuit/register picture at the sampler, an earlier purpose for transcripts, cleaner example-to-record transitions and a visibly separated classical value-function argument would improve understanding more than additional caveats or longer numerical counts.


---

## TEACH reading log: lecturer considering an advanced undergraduate / first graduate assignment

### Scope and provenance

This is a simulated lecturer perspective, anchored in the query-model passages of Buhrman–de Wolf's survey and de Wolf's lecture notes, with de Wolf's actual Grover exercise sheet as an additional comparison. It is agent review, not a report of a real class, a student study or the opinion of any named author. I know basic probability, linear algebra and algorithms, and can supply a first course's circuit-model background. I ask what a student with the exposition's stated prerequisites could reconstruct unaided, and which passages I would have to teach separately.

I read the entire current `repository/docs/exposition.md` in order, including captions, the five questions, answers, disclosure, references and link definitions. The reactions below preserve that reading order. Diagnoses obtained from companion passages, earlier-round notes, methods and online comparisons are identified as later checks rather than original understanding. A preliminary structural search exposed some answer text before my exercise calculations. Consequently my five calculations are **answer-exposed recomputations, not blind attempts**. I did not treat their correctness as evidence that the exercises teach an unassisted reader. The parent reviewer independently performed a blind attempt; that is a distinct observation and must not be attributed to this perspective.

After the text pass I compared the expert companion's introduction and selected linked record passages. I then read the method files, prior-round revision account and literature. I visually inspected current exposition PDF pages 1, 2, 4, 5, 9, 14, 15 and 16, rendered at 90 dpi. The parent reviewer inspected all 20 pages separately. My visual claims are limited to these eight pages. I rendered those pages with Poppler; I did not run any supplied script, Lean build or Comparator check. No manuscript was changed. The exact local and online reading scopes are listed in `teacher_sources.json`.

### Introduction: the first classroom decision

The four-bit OR entrance is productive. It gives a query a physical meaning and separates reading an unknown input bit from the computation performed between reads. The all-branch cap is an unusually useful early sentence: a worst-case resource promise includes branches on which the eventual answer is wrong. I would keep that even if a style detector flags its negative wording. The introduction also marks that the eventual estimates are upper and lower bounds, not matching evaluations of the two complexities.

My first substantive stop is the promise example. The surrounding object is a partial Boolean function, but “search promised exactly one 1” usually requires returning an index. OR on that same promise is constant one. The example can be repaired without changing any theorem, but in class I would have to ask, “What is the required output?” before using it. The issue is a switch of task type, not a claim that promised search is invalid.

The first two pages then accumulate the universal infimum, the family theorem, parameters k and m, constants depending on k, logarithmic factors, an informal exponent elimination, a historical comparison and the route. Each component is defensible individually. The cumulative experience still asks a newcomer to park too many symbols before manipulating the advertised small construction. The prerequisite sentence on page 2 arrives after much of this work. The small infimum display on page 1 makes its quantifiers harder to read than the ordinary prose precisely when those quantifiers matter most.

For a course assignment, I would currently provide an external instruction: read the query-cost example, note the informal destination, and return to the precise theorem after the construction. That instruction is evidence of a sequencing issue in a text claiming to stand alone. This does not require removing the exact theorem or postponing immediate credit. The method itself already allows an informal result before a long construction.

The two suggested routes are sensible: one can study the quantum mechanism while accepting the classical lower bound, or the reverse. Later, however, the final teach-back asks about both mechanisms together. A reader who follows an authorized skip route needs a success criterion appropriate to that route. Otherwise an optional section has silently become compulsory at the assessment point.

### Section 1: a real operation, then an early register burden

The three eight-bit inputs supply a good common object. The normalized Walsh transform makes the inner product executable using elementary linear algebra, and the sign-reversed input is the right warning: identical acceptance probability does not force the partial predicate to be defined on both inputs. The experiment on the negative case is one of the most effective passages because it exposes a tempting false inference by calculation.

I can follow the phase kickback and the projection calculation, but the position register, answer bit and workspace label arrive close together. Students with the stated prerequisites have not necessarily used registers at all. A single explicit basis-state transformation, showing which component changes and which merely records information, would make the existing explanation easier to teach. This is a request to expose an operation already used, not to add a separate quantum-computing chapter.

The entire first calculation is worked by the author. The first numbered question does not arrive until after the much larger construction. I would insert or orally ask a tiny independent calculation here, such as changing one supplied sign block and deciding whether the resulting vector aligns, reverses or is orthogonal. That would tell me whether the learner can perform the operation before the argument uses it as a supplier.

The explicit warning that this toy has L=0 is correct and should survive revision. The small board illustrates signs, promises and locations; it is not itself a positive-budget separation. Earlier-round concerns about presenting the toy as a witness are fixed. The remaining pedagogical burden is carrying several such scope resets, not absence of the warnings.

### Section 2: the construction becomes assignable

The column-string / address-input / addressed-cell architecture earns the first figure. It makes clear that the transcripts and pointers are themselves input data and may lie. The winning predicate is an exact local-check condition, and the one-line uniqueness proof is memorable: two all-one winning columns cannot both provide a pointer to a zero in the other. I would ask students to reproduce that proof without looking.

The distinction between an r-bit cell address and an ell-bit pointer position is especially valuable because their lengths happen to agree in the four-column example. Without that sentence the toy would teach an accidental identification. Figure 1 is useful at normal size, though its smaller labels need enlargement for a projected classroom page. Figure 2's highlighted winning cell and pointer paths give the local tests a visible target.

The attribution paragraph is overloaded for this point in a lesson. It credits cheat sheets, explains the address length, justifies union bounds and distinguishes alphabets. The credit should remain at first use, but some parameter engineering could wait until its cost or probability role is visible. Students do not yet know why twenty logarithmic copies or an exponentially small decoder error is the right tradeoff.

The actual gate-2 check is now concrete and useful. A transcript entry is compared with the actual input bit, so a forged self-consistent story cannot simply invent its leaves. The finite checker uses the same small circuit, but its named board uses different positive and negative strings, with amplitudes ±1/2 instead of ±1; the caution about that relationship is honest but interrupts the local-test lesson. I would keep the scope statement near the linked evidence rather than have the main reading route rehearse the checker distinction at length.

The four test families are now readable full-width prose. I do **not** recommend restoring the rejected long prose tables. The present 2r output-test sentence could say more directly that each of r transcripts contributes one domain bit and one value bit. That is a small teaching gloss, not a different inventory.

Question 1 is correctly posed and its answer is correct. In my answer-exposed recomputation, the changed board's string, pointer and gate checks pass, but the first domain output fails at every address. The stored value bits are 00, so the additional value-test failures equal the address's Hamming distance from 00: total failures 1, 2, 2 and 3 at 00, 01, 10 and 11. The exercise tests promise rejection well. It does not yet test the induction that makes a false transcript fail somewhere, even though that induction is the core reason the total function is well defined on arbitrary data. A second task could change one stored gate value and follow the consistency consequence, using the existing circuit.

The historical AND-OR comparison introduces a different parameter n. The text should say explicitly that there are n separate inner AND-OR inputs, each of n² bits. Otherwise “g on n bits composed with AND-OR on n² bits” is easy to picture as one shared n²-bit object. The lower-bound product is an imported composition fact, not a general principle that two quoted costs can always be multiplied. These are explanatory ambiguities, not objections to the cited historical result.

### Section 3: a useful interface whose prerequisites should be named

The three facts about the partial supplier are a good way to keep the exposition finite. I understand the required quantum decoder, randomized hardness threshold and exact near-linear transcript circuit. The sentence explaining that circuit size controls the verifier's rS gate tests is particularly good: an apparently technical circuit fact has an immediate role.

The reference to a Chernoff bound assumes slightly more than “elementary conditional probability.” A lecturer can state the concentration fact as an accepted input, or give a short repeated-trial calculation; the reader should know which treatment is intended. There is no need to prove all of concentration theory.

The polynomial total-input-length observation is correct, but an end-of-section check distinguishing m columns from n or the total number of input bits would be helpful. It is exactly the sort of notation confusion that survives a correct local reading. The family theorem is parameterized by construction scale, while query complexity is still measured on actual bit strings.

### Section 4: the main quantum lesson, with a dense interface

The failed nested-search idea is a strong opening. Students see why simply checking every candidate with a square-root search inside another square-root search is too expensive. The pairwise comparison must therefore eliminate candidates cheaply. The guaranteed behavior against the true winner and the arbitrary behavior among nonwinners are kept distinct. Figure 3's cycle makes that arbitrary behavior concrete.

The ideal weights are introduced honestly as quantities for analysis. The algorithm does not estimate them. This must remain explicit. The fractional example is a real improvement over a board whose weights are all zero or one, because it shows sampling in proportion to weights rather than uniformly from their support. But Question 2 returns to the zero-or-one board, so an instructor still lacks evidence that the learner understood the fractional operation.

My slowest quantum paragraph is the reversible implementation. Deferred measurements, retained decoder labels, branch orthogonality, a controlled comparison, fresh independent workspaces and reversibility are now all present. The problem is no longer an omitted ingredient. It is that the paragraph compresses several operations into prose. A student who can repeat “keep the labels orthogonal” may still be unable to sketch the preparation and its inverse. A small state/register transformation using the actual column and comparison flags would be worth more than another disclaimer. The source preprint's corresponding preparation formula and de Wolf's explicit full-space amplification derivation are helpful comparisons, but neither establishes that this particular compressed sequence teaches successfully.

The direct explanation of the successful unit vector g is mathematically well chosen. It includes all retained workspace, and amplification changes its coefficient while preserving its internal relative label law. This is the crucial bridge from an ideal distribution to an implementable sampler. The p=1/2 example usefully refuses to pretend that every iteration improves success.

Question 2 recomputes to weights (1,0,0,0), preparation success 1/4, next pivot 1, and one iteration raising the success probability to one. This answer is correct. A second iteration on the same state would return success probability to 1/4, directly testing the overshoot warning. De Wolf's 2011 exercise sheet asks learners to execute one iteration and then two; this is a particularly close teaching comparison because it changes an operation, not merely a numerical input.

The stage paragraph is now careful about the success threshold before the winner is listed, arbitrary behavior afterward and retention of the candidate list. The continuation {2,1} is a useful stopping example. I would preserve it. The reversal of the word “success” when verification searches for a violation is also explicitly flagged and should remain so.

The error estimate is correct but crowded. Students need to distinguish stochastic errors already absorbed in the actual a_ij from failures added in the final union bound. A small oral classification task would test that distinction. I do not advocate a new error ledger table or another loose bound. The logarithmic exponent six is explicitly described as a loose artefact; that arithmetic can be second-pass material while the square-root mechanism stays prominent.

A later funnel check found that the link described as giving amplification trial counts lands at `upper-amplification-proof`, after the M and N definitions at `upper-grover-trial`. The link exists and the proof is present. The defect is that the promised entry point assumes the very definitions the reader clicked to find.

### Section 5: the strongest reduction, with too many rapid model changes

The fixed hard law is introduced with the correct quantifier: one distribution defeats every capped deterministic tree. That sentence is worth keeping even if it increases the rate of contrasts or negations. The dummy/planted pair is then concrete. I can name the only two changed locations and explain why both runs coincide until a changed location is read.

Figure 4 shows the right pair and labels what is revealed to the reader. Its use of a realized address 10 could be described as one realization of the new random draw, to prevent a student from carrying over the deterministic inputs of Figure 2. The text already discloses the reset to samples from μ and the L=0 limitation; this is a residual example-continuity issue, not an unannounced change of law.

The early/late erased-zero argument is understandable once the complete transcript prefix is conditioned on. On the delivered PDF, however, Figure 4 interrupts that conditional-uniformity paragraph between pages 13 and 14. A lecturer would move the figure to its pair definition so the proof can be read without reconstructing a broken sentence. Question 3 recomputes to 1/2 for an independent planted column and 15/16 for the dependent choice. Its answer is correct, and it tests independence rather than a uniform marginal. Because it uses fixed positions, it does not test the harder adaptive-prefix argument that precedes it.

The true-cell step gives a compelling reason that guessing is still bounded: naming a query position proposes an entire address. That is free choice of a query label, unlike learning pointer bits from the input. The use of whole-run lightness should be reinforced at its definition, since later becoming heavy matters even if the true-cell query occurred early.

The direct-product statement is exact and strong enough for the application. The separate-cap and jointly-independent-side-information counterexamples are both valuable. The optional proof is also mathematically coherent, but its product conditioning, value function, one-step inequality, AND calculation and leaf estimate are packed into two large paragraphs. I would teach the existing AND value calculation before introducing every V_h, then split the proof by those operations. It should remain optional, with the full contract outside the box.

This section cycles through uniform AND inputs, fair identity bits with XOR side information, a differently promised AND problem and finally fair XOR inputs. Every reset is disclosed. The cumulative cost is still high. Students need a stable local question—why a cheap visit yields a capped predictor—while these supporting examples are supplied. Some supplier detail can be optional without weakening the inference.

The simulator is the best construction-specific teaching moment. Its external information is independent of the target tuple; it forwards at most L target queries; it reads an address from a query position before reading the cell; and a default guess can only enlarge the success event. The three-budget paragraph now states exactly why the global cap, target-column cap and separate per-instance caps fit together. I would keep it intact.

The XOR trace makes the one-way implication tangible. Question 4, with the stopping condition, recomputes correctly: on the modified a=0 branch, the moved cell query is reached with one target query and names 00. Its true-cell event requires a=0, b=0 and c=d, with probability 1/8. The unchanged a=1 branch contributes another 1/8, giving total 1/4. The answer's later-query-to-c variant is more revealing than the stopped-run case and should become an explicit second part before the answer. That would test complete-run lightness rather than merely replaying the trace.

The final average over I correctly prevents an extra m factor. I would ask a class to distinguish “the independently selected planted column's true cell is hit” from “some column's true cell is hit.” The existing display supplies the proof; this would test whether they know which event it proves.

### Sections 6 and 7, answers and closure

The eventual floor estimates and fixed-k quantifier order are correct. The repeated “so” in the opening arithmetic paragraph is an editing matter, not a mathematical defect. Question 5 is now particularly good: k=4 gives α_tot ≥3.5 but does not itself refute the endpoint 3.5 inequality, while k=5 provides a strict exponent gap against it. I would retain that changed-case task exactly in spirit.

The final unnumbered teach-back asks the right questions but provides no separate criteria for success. A student could say “quantum interference finds the hidden cheat sheet” and feel finished without reconstructing either cost mechanism. For assignment use, I would supply a short checklist: the two changed locations; the joint capped-prediction event; weight sampling without estimating weights; retained-list verification; and fixed k before m in the exponent argument. Routes that skip one half need a correspondingly narrower checklist.

The formal-inspection task is much better than asking students to trust a list of Lean names. I read the targeted winning clause in `Challenge.lean`; its `some (s h)` encoding simultaneously asserts definedness and value. A newcomer needs a tiny cue about that option-valued function to understand why finding the clause checks the domain requirement. No new formalization work is needed. The explicit statement that the compared family theorem leaves the logarithmic exponent unspecified is appropriately local and should remain.

The numbered answers are correct on my recomputation. They should not be used as evidence of independent learning in this review because of my answer exposure. The disclosure and ordinary bibliography belong at the end. I did not treat reference metadata, a proof receipt or a successful tool run as evidence that a human reader understood the exposition.

### Assignment verdict and teach-back

I would assign this as a guided unit in an advanced undergraduate or first graduate course, with separate preparation for coherent reversible operations and with a short assessment sheet testing the changed cases above. I would not yet assign the entire text as a wholly self-contained first encounter for every reader named in its prerequisite sentence. That is a scope/pacing judgment, not a request to narrow the user's intended audience.

The likely current teach-back is: a partial problem has a large quantum/classical gap; exact certificates make a total function; a quantum tournament narrows the search; a classical algorithm must find hidden information. Those are useful headings but omit the proof-bearing distinctions. A successful teach-back should say that exact gate/domain/value checks reject arbitrary false cells; pairwise comparisons are reliable against the winner even if losers behave cyclically; the algorithm coherently prepares a weight-proportional law without evaluating the weights, preserves it conditionally during amplification, keeps candidates and verifies them; and the classical proof bounds two changed locations through an independent plant and a joint light-and-correct event. It should finish by explaining why fixed k gives a power below four and why varying the fixed k rules out every smaller universal exponent.

These are proposed teaching tests. Their value has not been established by a real class. The next revision should preserve the now-correct examples and make the learner's reconstruction observable, rather than accumulating more qualifications around already-correct sentences.

### Sources not read in this workstream

Yao (1977), Nisan (1991) and Barnum–Saks–Szegedy (2003) remained cited-only references; I did not read those originals. I did not read the full supplied Grover (1996) or Aaronson–Ambainis–Bogdanov–Yeung (2021) texts. Search hits for Childs's notes and Watrous's course index were not treated as inspected teaching passages. The root and other perspectives may have distinct documented reading scopes; they should not be attributed to this lecturer pass.

