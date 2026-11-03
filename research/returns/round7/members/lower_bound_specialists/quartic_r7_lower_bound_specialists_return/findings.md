# All findings

A readable version of `feedback.json`, in document order. “Keep” is an explicit preservation recommendation. Severity measures the effect on this document’s reader, not a claim that the theorem is false. Source lines refer to the supplied current Markdown.
## LS001

**expert_companion · medium · unclear · direct_product**

**Location:** Abstract (source line 9)

**Exact current phrase:**

> A classical algorithm cannot locate the winning column's certificate

The next clause says that an algorithm must spend the address cost in each of a constant fraction of the columns. Taken literally, this sounds like a necessary property of every successful execution. The proof establishes a distributional obstruction to bounded-error algorithms: a particular run can guess the correct cell cheaply.

**Why it matters:** The abstract is often the only version of the classical mechanism a reader retains; it should not turn a probability estimate into a pathwise impossibility.

**Advice:** Qualify the claim by bounded-error success on the planted experiment, or describe low-budget discovery as unlikely. Keep the per-column cost intuition.

**Prior-round relation:** The body fixed the old CX010 overstatement by explaining prediction from query position; this residual is in the abstract, not the corrected body.

## LS002

**expert_companion · low · consistency · separations**

**Location:** Abstract and §1.2 (source line 9)

**Exact current phrase:**

> Together these give $R\approx Q^{4-2/k}$.

The approximation sign suggests a two-sided estimate for the complexities of the constructed function. What has actually been proved is a quantum upper bound and a randomized lower bound, enough to force a separation exponent. The same shorthand reappears in the overview displays.

**Why it matters:** A separations specialist distinguishes a lower-bound witness from a tight characterization of that witness. The latter is stronger and is not needed here.

**Advice:** Use one-sided separation language at the first occurrence and explicitly say that logarithms are suppressed in the overview.

## LS003

**expert_companion · low · prose · separations**

**Location:** §1 Introduction, first paragraph (source line 14)

**Exact current phrase:**

> reads its input one bit at a time

As a common opening for both models, this phrase gives a classical description immediately before introducing a quantum oracle that may query indices in superposition. The displayed oracle corrects the picture, but the opening sentence momentarily conflicts with it.

**Why it matters:** A reader entering from classical lower bounds should not have to mentally repair the first description of the comparison model.

**Advice:** Describe the unit of cost as an oracle access to a bit-indexed input, then distinguish classical access and superposed quantum access without expanding the model discussion.

## LS004

**expert_companion · keep · keep · separations**

**Location:** §1 Introduction, paragraph after Theorem 1 (source line 29)

**Exact current phrase:**

> Taking $k=3$ in (2) gives exponent $10/3>3$

This is the right immediate consequence to give after the headline. It identifies an actual fixed parameter that beats the conjectured cube before moving to the limiting exponent.

**Why it matters:** It prevents the reader from thinking that refuting the cubic conjecture already requires the technical growing-parameter remark.

**Advice:** Keep this short calculation beside the conjecture and retain the later order of quantifiers.

## LS005

**expert_companion · medium · overweighted · separations**

**Location:** §1 Introduction, contribution paragraph (source line 31)

**Exact current phrase:**

> This paper adds the following to the preprint.

The four-part contribution paragraph mixes the theorem, four exact constants, a proof-scope claim, two observations, the long record, and the formalisation. It reads like a project inventory just before the mathematical overview should establish momentum. The constants receive more opening space than their role warrants.

**Why it matters:** The specialist needs to know which mechanism is new and which mathematical work this companion performs. Several competing selling points obscure that decision.

**Advice:** Separate provenance and mathematical contribution from the quantitative-reference information. Keep the complete constant list at the theorem or in the sections where each constant is used.

**Prior-round relation:** Round-six QX-017 asked for a shorter constants paragraph. The current detailed First/Second/Third/Fourth paragraph shows that the compression did not fully land.

## LS006

**expert_companion · low · underweighted · certificates**

**Location:** §1.1 Earlier separations (source line 35)

**Exact current phrase:**

> A quantum algorithm computes $g\circ h$ and Grover-checks a certificate

The certificate calculation appears abruptly. The important feature of AND–OR is that certifying all n inner outputs also certifies that the outer input lies in the domain of g. The supplied ABK intuition makes this domain-certification role explicit before performing the cost calculation.

**Why it matters:** Without this connection, the paragraph looks like a fortuitous list of complexity measures rather than an explanation of why this particular inner function was chosen.

**Advice:** Add the single causal link from n small certificates to certification of the outer promise. The resulting contrast with the present exact-circuit transcripts will then be immediate.

**Source:** https://arxiv.org/abs/1511.01937v2

## LS007

**expert_companion · medium · unclear · separations**

**Location:** §1.1 Earlier separations (source line 39)

**Exact current phrase:**

> If $Q(g)$ is polylogarithmic

This assumption arrives after the displayed quantum bound that already uses it. For an arbitrary partial g, computing g composed with AND–OR contributes a factor Q(g) to the inner quantum cost; the preceding sentence initially introduces g without that restriction.

**Why it matters:** The arithmetic is the explanation of why the earlier recipe reaches the cube. Its hypotheses should be attached before the formula is read, rather than supplied retroactively.

**Advice:** State the polylogarithmic quantum-cost assumption when g is introduced, as ABK do by taking g to be Forrelation with Q(g)=1. This is a scope clarification, not a request for a new composition theorem.

**Source:** https://arxiv.org/abs/1511.01937v2

**Prior-round relation:** The round-six C05 conversion has been added. This concerns the placement of the new conversion's hypothesis, not its absence.

## LS008

**expert_companion · low · consistency · separations**

**Location:** §1.1 Earlier separations, table (source line 41)

**Exact current phrase:**

> Exponent $a$ with $R=Q^{a}$ (total $f$)

The heading presents equality, but the entries record achieved separations up to logarithms and one universal upper bound. Those are different types of statement. The row labels partially repair this, but the heading is the part a reader is likely to quote.

**Why it matters:** A compact history table should preserve the direction of each bound instead of relying on prose elsewhere to explain its shorthand.

**Advice:** Name the first column as an achieved separation exponent and distinguish the universal upper-bound row visually or in a short note.

## LS009

**expert_companion · medium · figure · certificates**

**Location:** §1.2 Figure 1 (source line 52); supplied PDF page 3

**Exact current phrase:**

> a separate cell $B_{i,s}$

The main construction figure draws one certificate array, that of the winner, while the lower bound depends on every column having a separate array. The text does say this, but the picture can still be remembered as one shared cheat sheet attached to the whole matrix.

**Why it matters:** A shared array is precisely the mental model the new construction must displace; a misleading memory of the picture loses the source of the per-column charge.

**Advice:** Add a compact indication that the omitted columns also carry their own A-blocks and cell arrays, or state this explicitly in the figure caption. Keep the winner's array enlarged.

## LS010

**expert_companion · medium · unclear · direct_product**

**Location:** §1.2 Overview, erased-zero paragraph (source line 56)

**Exact current phrase:**

> Finding the erased zero means finding one marked zero

There are m easily encountered zeros in the dummy matrix, but only the zero in the independently chosen hidden column matters. Finding any zero costs about m queries; the m² scale comes from discovering enough distinct columns that the selected column is likely to be among them.

**Why it matters:** The current sentence risks importing the wrong search problem at the very point where the extra factor m must become visible.

**Advice:** Identify the marked zero as the zero in a hidden independently selected column, or use the discovery-count explanation from equation (11). Do not suggest that all zeros are interchangeable targets.

## LS011

**expert_companion · keep · keep · direct_product**

**Location:** §1.2 Overview, classical prediction paragraph (source line 58)

**Exact current phrase:**

> A query to $B_{i,s}$ reveals $s$ by its position

This now identifies the actual reduction. A simulator outputs the address named by a proposed query; it is not forced to read a certificate or decide whether it is valid. The sentence is substantially better than the informal assertion that a reader must first compute the address.

**Why it matters:** The query-position observation is what turns a cell visit into an all-answers prediction event under a hard product law.

**Advice:** Keep this sentence and its fuller implementation in §4.4. Do not compress it back to an absolute claim that guessing cannot work.

**Prior-round relation:** Round-six CX010 fix confirmed in the current overview and §4.4.

## LS012

**expert_companion · medium · error · certificates**

**Location:** §1.3 Relation to earlier constructions, pointer paragraph (source line 73)

**Exact current phrase:**

> each zero of a non-marked column carries a back pointer to the marked column

This overstates the condition in the cited pointer function. ABBLSS require the designated highlighted zero (the leaf ℓ_j) in each nonmarked column to point back to the marked column; arbitrary other zero cells need not do so. Their algorithm explicitly allows the set of back-pointer destinations from all observed zeros to contain nonmarked columns. Thus replacing “highlighted zero” by “each zero” describes a different function.

**Why it matters:** The entire comparison is meant to explain why earlier pointer constructions are easy for randomized algorithms. An inaccurate description of their positive inputs undermines that explanation and the credit to the predecessor.

**Advice:** Restrict the claim to the highlighted leaf in each nonmarked column. Preserve the subsequent explanation of why finding arbitrary zeros yields candidate destinations rather than immediately identifying the marked column.

**Source:** https://arxiv.org/abs/1506.04719v3

**Prior-round relation:** Residual in the wording introduced to answer CX002. The old missing-tradeoff criticism is fixed; this is a new inaccuracy in the added description.

## LS013

**expert_companion · keep · keep · certificates**

**Location:** §1.3 Relation to earlier constructions, comparison paragraph (source line 77)

**Exact current phrase:**

> a comparison between two losing columns can have any probability, including $1/2$

The contrast with a fixed graph and a bounded-error edge oracle is precise. It states a concrete interface difference instead of merely saying that the tournament is novel.

**Why it matters:** This lets a classical separations reader understand why an existing fixed-tournament search theorem cannot simply be quoted unchanged.

**Advice:** Retain the explicit 1/2 case and the distinction between certificate complexity and randomized complexity in the preceding sentences.

## LS014

**expert_companion · keep · keep · separations**

**Location:** §1.3 final paragraph, proof scope (source line 79)

**Exact current phrase:**

> We cite, and do not reprove,

The explicit scope list is valuable. It now distinguishes the argument proved here from the Forrelation supplier, circuit and local-test ingredients, standard amplification facts, and the uniform refinement cited from the record.

**Why it matters:** A referee can decide where independent source checking is needed; the list also prevents the phrase “complete argument” from being read as a promise to reprove the literature.

**Advice:** Keep the scope statement, but make the abstract and contribution paragraph use the same convention. Do not expand it into a receipt or review-status ledger.

## LS015

**expert_companion · low · missing · fourier**

**Location:** §2 Forrelation, property (iii) (source line 105)

**Exact current phrase:**

> $\Phi=N/m^{(k+1)/2}$ for an integer $N$

The choice m=4^t has been fixed several times, but its useful role is never stated at the point of exact arithmetic: m^{(k+1)/2}=2^{t(k+1)} is integral for every k. That makes the displayed threshold tests comparisons of integers without parity cases.

**Why it matters:** The apparently arbitrary restriction to powers of four otherwise looks like inherited notation rather than a simplifying design choice.

**Advice:** Give the arithmetic reason for powers of four in a short clause here or at the initial parameter choice. The record already contains the needed explanation.

## LS016

**expert_companion · low · unclear · direct_product**

**Location:** §2 Total function, input specification (source line 107)

**Exact current phrase:**

> All of these are independent input bits.

In the definition of a total function there is no probability law yet. Here “independent” means freely assignable, disjoint input coordinates, whereas in §4 it means probabilistic independence under a carefully chosen law. Figure 1 similarly labels the instances independent.

**Why it matters:** The lower bound relies on a precise distributional independence statement. Using the same word loosely in the construction makes that distinction harder to retain.

**Advice:** Describe these as unconstrained or separate input coordinates. Reserve distributional independence for the hard experiment.

## LS017

**expert_companion · keep · keep · separations**

**Location:** §2 Total function, circuit parameter (source line 114)

**Exact current phrase:**

> both bounds in (2) are proved for the function built from it

This is an essential short sentence. The function really depends on the circuit because the transcript bits are part of the input, and the paper now fixes one circuit for both analyses.

**Why it matters:** Without it, a reader could mistake separate existential upper- and lower-bound constructions for bounds on the same total function.

**Advice:** Keep the sentence, and keep the adjacent distinction that the classical lower bound uses circuit correctness whereas the quantum cost also uses circuit size.

## LS018

**expert_companion · low · structure · separations**

**Location:** §2 Total function, input-length count (source line 114)

**Exact current phrase:**

> $Q(F_{k,m})\le n^{1/44+o(1)}$

This is a true input-length corollary for the fixed-k setting, but it is not used again and arrives between the definition and the local tests. It invites the reader to wonder whether a bound in terms of n is another advertised result.

**Why it matters:** The construction already introduces several scales; the conversion to total input length interrupts the explanation of why certificates are locally checkable.

**Advice:** Retain the polynomial input-size reassurance, but move the 1/44 consequence to a brief remark or omit it from the main flow. If kept, explicitly maintain the fixed-k qualification.

## LS019

**expert_companion · keep · keep · certificates**

**Location:** §2 Local tests (source line 120)

**Exact current phrase:**

> when $i$ does not win some test fails at $(i,s)$ for every address $s$

The universal quantifier over addresses is exactly the soundness statement the upper bound needs on arbitrary total inputs, including unpromised loser inputs. This is stronger and more useful than describing only the tests at the true address.

**Why it matters:** It closes the otherwise tempting gap between a promise decoder and an algorithm for a total function.

**Advice:** Keep this sentence adjacent to the proof by topological gate consistency, and keep its use in §3.3.

## LS020

**expert_companion · medium · prose · separations**

**Location:** §3 Lemma 2 proof sketch (source line 128)

**Exact current phrase:**

> Search with an unknown success probability bounds its cost only in expectation

This sounds like a general limitation of unknown-success search, whereas the sentence is referring to the particular cited expected-cost algorithm. The lemma being proved is itself an unknown-success procedure with a fixed cap and a threshold guarantee.

**Why it matters:** The broad wording momentarily makes the current construction look inconsistent with the preceding assertion.

**Advice:** Attach the expectation claim to the cited BHMT procedure rather than to search with unknown probability in general; the reason for the fixed number of trials then remains clear.

**Source:** https://arxiv.org/abs/quant-ph/0005055

## LS021

**expert_companion · low · unclear · separations**

**Location:** §3.1 Comparing two columns (source line 134)

**Exact current phrase:**

> Let $a_{ij}$ be the probability that $i$ defeats $j$.

The input is implicitly fixed here, but that fact is not stated until Proposition 3. A reader about to encounter the hard distribution in §4 may initially treat a_ij as also averaging over random inputs.

**Why it matters:** The sampler needs exact probabilities for each fixed input and history, not probabilities averaged over a distribution of boards.

**Advice:** Say “for this fixed input” when a_ij is defined. The later statement can then remain concise.

## LS022

**expert_companion · keep · keep · separations**

**Location:** §3.1 Comparing two columns, symmetry (source line 134)

**Exact current phrase:**

> For an unordered pair $\{i,j\}$, we sort the indices and run one fixed circuit

The convention explains why the two ordered probabilities sum to one even though the decoder is probabilistic. This is a small implementation detail with a real role in the weight-halving identity.

**Why it matters:** Running independently chosen comparison routines in the two directions would not automatically justify equation (7).

**Advice:** Keep the convention and the explanation that retained label registers preserve the measured probabilities.

## LS023

**expert_companion · low · prose · separations**

**Location:** §3.2 Tournament, intuitive paragraph (source line 145)

**Exact current phrase:**

> The total weight halves in expectation at every step

The displayed calculation gives an upper bound by half, generally strictly smaller because of the diagonal correction. “Halves” can suggest equality when the mechanism actually gives at least that much expected decrease.

**Why it matters:** The proof uses an inequality, and a precise verbal statement would match equation (8) without any extra machinery.

**Advice:** Describe the expected new total weight as at most half the old total.

## LS024

**expert_companion · keep · keep · separations**

**Location:** §3.2 Exact sampling (source line 154)

**Exact current phrase:**

> The algorithm never computes the weights.

This is the right sentence to bridge a classical-looking ideal process and its quantum realization. The following tensor-product state then explains how the weights arise as probabilities without querying their numerical values.

**Why it matters:** A lower-bound specialist could otherwise read the ideal process as granting the algorithm information it has not obtained from the input.

**Advice:** Keep this sentence and the exact distinction between success-and-label mass w_i/m and conditional label law w_i/W.

## LS025

**expert_companion · keep · keep · direct_product**

**Location:** §3.2 Coupling (source line 161)

**Exact current phrase:**

> conditional on the entire past

The stopped coupling is stated at the right level. It handles history-dependent failure probabilities and does not infer a global joint law from marginal stage guarantees.

**Why it matters:** This is the quantum-side counterpart of the classical proof's insistence on the original joint event; both are places where careless conditioning would change the theorem.

**Advice:** Preserve this local explanation even if the surrounding standard amplification material is shortened.

## LS026

**expert_companion · medium · overweighted · separations**

**Location:** §3.3 Verification and query count, final paragraph (source line 169)

**Exact current phrase:**

> The exponent six in (2) comes from a deliberately loose count

The paragraph spends a full sequence of trial, iteration, padding and rounding calculations on an exponent immediately declared irrelevant below. It is longer than the explanation of how the off-promise Forrelation law is turned into hardness in §5.

**Why it matters:** This gives routine slack accounting disproportionate emphasis relative to the delicate new reductions.

**Advice:** Keep the final cap and the reason the count is valid on every input, with the detailed loose arithmetic in the cited record. Preserve more room for the simulator or the promise-gap argument.

**Prior-round relation:** Round-six QX-021 planned a two-sentence compression. The current paragraph still contains the full padding/trial/iteration narrative; this is a residual, not an assertion that no compression occurred.

## LS027

**expert_companion · medium · structure · direct_product**

**Location:** §4 opening and §4.5 generic conclusion (source line 173)

**Exact current phrase:**

> The argument applies to any partial function $P$

The useful generic reduction is introduced in prose, but its quantitative conclusion is delayed until equation (15), and that conclusion is still written as R(F_{k,m}) although P has temporarily been arbitrary. The record's F_{P,C,m} notation makes this modularity much clearer.

**Why it matters:** A lower-bound specialist should be able to identify the reusable statement and its exact assumptions before reading the proof. The current notation partly hides the fact that the analytic supplier is used only through L<R(P).

**Advice:** Display the generic lower-bound goal near the beginning and use an unambiguous name for the addressed function during the generic argument. Specialize back to F_{k,m} at the end.

## LS028

**expert_companion · keep · keep · direct_product**

**Location:** §4 opening, minimax paragraph (source line 173)

**Exact current phrase:**

> by compactness the best worst-case success is attained and is below $2/3$

This is a careful and economical explanation of the strict minimax premise. The text does not merely say that each tree fails somewhere and then exchange quantifiers without justification.

**Why it matters:** The same hard law must work for every deterministic L-query tree, including all predictors generated by later choices of column and query time.

**Advice:** Keep the attainment clause and the fact that μ is supported on the promise. No separate minimax proof is needed in this companion.

## LS029

**expert_companion · medium · unclear · direct_product**

**Location:** §4.1 Lemma 4 proof, induction step (source line 183)

**Exact current phrase:**

> the recursion absorbs its two branches

This compresses the only tensorization step into a metaphor. The reason is that every factor other than the queried one is identical in the two answer branches and can be factored out; the remaining sum is bounded by V at the old budget.

**Why it matters:** For a reader checking adaptive interleaving, this is the exact step that must survive compression. Independence alone does not imply that a product of changing values decreases in expectation.

**Advice:** Add the common-factor calculation in one line or spell out that only one measure and one remaining budget change. The record's weighted proof already supplies it.

**Source:** https://arxiv.org/abs/1005.0644v2

## LS030

**expert_companion · keep · keep · direct_product**

**Location:** §4.1 source paragraph, fair-tree attribution (source line 185)

**Exact current phrase:**

> for XOR advantage under uniform inputs

This qualification correctly distinguishes the target and input convention of Shaltiel's fair-tree theorem from the vector-output statement for an arbitrary hard law used here.

**Why it matters:** A loose citation to “the direct product theorem” would blur genuinely different results. The current sentence credits the antecedent without claiming that its literal statement is identical.

**Advice:** Keep the qualification and the separate reference to Drucker's fair specialization.

**Source:** https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html

## LS031

**expert_companion · keep · keep · direct_product**

**Location:** §4.1 source paragraph, global-budget theorem (source line 185)

**Exact current phrase:**

> Drucker's Theorem 1.1, with one global budget, would also serve.

The correction is mathematically useful and correctly specialized. With T=L, error 1/3, number of copies r, and α=3/r, the budget is L and the success bound is 2(2/3)^r. Since r≥40, the parameter range is admissible, and equation (14) has enough slack.

**Why it matters:** It prevents the reader from mistaking the choice of a short separate-cap proof for a claim that existing global-budget theorems are inapplicable.

**Advice:** Keep this observation without expanding it into a second proof of the lower bound.

**Source:** https://arxiv.org/abs/1005.0644v2

**Prior-round relation:** Round-six CX001 fix confirmed; do not reopen the old objection.

## LS032

**expert_companion · low · credit · direct_product**

**Location:** §4.1 source paragraph and References (source line 185)

**Exact current phrase:**

> Drucker's Lemmas 3.1–3.2

For a current related-work map, Ben-David–Blais, FOCS 2025, arXiv:2512.08268, is a relevant later direct-product source. Its maximum-distributional expected-cost measure differs from this fixed-law hard-cap premise, so it is context rather than a replacement needed by the proof.

**Why it matters:** The packet explicitly asks for current community context. A short note can place the elementary specialization without expanding the companion's technical scope.

**Advice:** Consider one related-work citation; retain the present Drucker proof and exact cap assumptions.

**Source:** https://arxiv.org/html/2512.08268v1

## LS033

**expert_companion · low · teaching · certificates**

**Location:** §4.2 Planting a winner, blank input (source line 189)

**Exact current phrase:**

> It has no winner.

Here the zero value follows immediately from the single zero in every X_i, independently of whether the blank cell pattern happens to satisfy some transcript tests. This differs from cheat-sheet proofs that add a sentinel bit to ensure that a blank certificate is invalid.

**Why it matters:** A reader familiar with the ABK blank-array argument may spend time looking for an omitted “all-zero certificates are invalid” convention that this construction does not need for its dummy-input value.

**Advice:** Attach the short reason “every X_i has a zero” to this sentence. This makes the coupling's support condition immediate.

**Source:** https://arxiv.org/abs/1511.01937v2

## LS034

**expert_companion · medium · figure · certificates**

**Location:** §4.2 Figure 2 caption (source line 191); supplied PDF page 9

**Exact current phrase:**

> here with $m=4$ and $I=3$

The supplied PDF figure draws eight bit boxes in every X_i strip while its caption says m=4. The definition requires each X_i to have exactly m bits. The figure source confirms a four-row panel and a loop over bit positions 1 through 8, so this is not an extraction artefact.

**Why it matters:** The figure is advertised as a concrete small instance. A reader trying to reconcile the dimensions cannot decide whether m counts columns, row positions, or something else.

**Advice:** Draw four bits per X_i for this caption, or explicitly label the panel schematic and remove the literal m=4 claim. Keep the two red changes and the shared address data.

## LS035

**expert_companion · low · unclear · direct_product**

**Location:** §4.2 coupling inequality (10) (source line 193)

**Exact current phrase:**

> or a bit of $B_{I,s_I}$

The right-hand event counts every query into the selected cell, even if the queried bit agrees with its blank value. The inequality is correct because this is an upper bound on seeing a changed bit, but the preceding “differ only in those two places” language can make it sound as if every visit forces divergence.

**Why it matters:** The proof is a first-difference argument, so the direction of this containment matters. It also explains why no properties of the contents of a queried cell are needed.

**Advice:** Add the source preprint's short observation that counting any visit is conservative even when a planted bit remains zero.

## LS036

**expert_companion · medium · unclear · direct_product**

**Location:** §4.3 erased-zero discovery estimate (source line 210)

**Exact current phrase:**

> since $J_i$ is uniform on the unqueried rows

This conditional statement needs the qualifier that the zero has not yet been discovered. After a zero was observed, J_i is known, and querying it again has probability one of returning zero. The proof counts new discoveries, not all observations of zero; the record and source preprint make that distinction explicit.

**Why it matters:** The stated conditional probability is the only probabilistic input to the early/late estimate. Its exact event should not be left to the reader to infer.

**Advice:** Say “before its first discovery” and count distinct previously queried rows; repeated queries contribute no new discovery. The bound itself does not need changing.

## LS037

**expert_companion · low · overweighted · direct_product**

**Location:** §4.3 final optional refinement (source line 215)

**Exact current phrase:**

> the constants below do not need it

The sharper 2G/[m(m+1)] estimate is presented immediately after the completed search bound, even though no following conclusion uses it. It interrupts the transition to the planted-cell estimate, which is the more delicate half of the proof.

**Why it matters:** The reader has to decide whether the new coefficient signals a hidden necessity or a different theorem, then discard it.

**Advice:** Move the optional refinement to a footnote or a compact pointer after the lower bound is assembled. Keep the record's full refinement available.

## LS038

**expert_companion · keep · keep · direct_product**

**Location:** §4.4 heavy-column definition (source line 219)

**Exact current phrase:**

> counting repetitions

The budget counts actual query calls, including repeated coordinates. That convention aligns the heavy-column charge with the simulator's cap and with the cap-event counterexample in Table 1.

**Why it matters:** Counting only distinct coordinates in one place and all calls in another would silently alter the event being bounded.

**Advice:** Keep the convention here and mirror the first-discovery convention explicitly in §4.3, where repeats do not count as additional discoveries.

## LS039

**expert_companion · medium · structure · direct_product**

**Location:** §4.4 simulator definition (source line 221)

**Exact current phrase:**

> Fix a column $i$ and a time $\tau\in\{1,\dots,G\}$.

The paragraph following this sentence packs the fixed target, free input, run simulation, abort rule, output rule, cap implication, event inclusion and conclusion into one block. Each step is correct, but the object the reader is trying to verify changes several times within the paragraph.

**Why it matters:** This is the reduction that earns the mL lower bound. It should be easier to audit than the optional logarithmic accounting.

**Advice:** Split the paragraph after the simulator's output rule. Keep one compact block defining the predictor and one proving the joint-event containment; no replacement section or new lemma is needed.

## LS040

**expert_companion · keep · keep · direct_product**

**Location:** §4.4 simulator, stopping rule (source line 221)

**Exact current phrase:**

> it aborts before an $(L+1)$-st query to them in total

The cap is imposed during execution for every possible target tuple, and it is a total cap on all r address instances. The proof then correctly uses that total cap to imply the separate caps.

**Why it matters:** This is what makes the direct-product premise true without conditioning the hard inputs on the original run's eventual cost.

**Advice:** Keep both “before” and “in total”; they do real mathematical work.

## LS041

**expert_companion · keep · keep · direct_product**

**Location:** §4.4 after equation (12) (source line 226)

**Exact current phrase:**

> This bounds a joint event under the original law.

This is the most important guard in the classical section. The cap event can be correlated with the hidden answers; the theorem bounds success and compliance jointly, not success after selecting compliant runs.

**Why it matters:** Removing this distinction would invalidate the reduction even though every displayed one-input hardness estimate remained true.

**Advice:** Preserve this sentence, its counterexample link, and the forward containment from the original run to a genuinely capped simulator.

## LS042

**expert_companion · medium · underweighted · direct_product**

**Location:** §4.4 union and average after equation (12) (source line 226)

**Exact current phrase:**

> Summing (12) over the $G$ times, averaging over the independent $I$

The correct operation is compressed enough that a reader may insert an extra factor m, or incorrectly divide the Gβ^r term by m. For each fixed i the union bound is Gβ^r; averaging m identical upper bounds contributes (1/m)∑_i Gβ^r=Gβ^r.

**Why it matters:** This is where the reduction preserves the exponent. The accounting of m deserves to be visible rather than merely recoverable.

**Advice:** Give the one-line sum over i and query time, or reproduce the record's sentence explaining that the factor m cancels. No independence between different query times is required.

## LS043

**expert_companion · low · structure · direct_product**

**Location:** Appendix A Table 1 references (source line 226); supplied PDF page 14

**Exact current phrase:**

> row 7 of Table 1

The prose repeatedly refers to numbered rows, but the supplied table has no visible row numbers. The longest example spans several lines, so counting rows is surprisingly inconvenient when moving between §4.4 and the appendix.

**Why it matters:** The table is a navigation aid; its cross-references should identify entries directly rather than asking the reader to count.

**Advice:** Add unobtrusive row numbers or name the simplification in the reference. Keep the table at the end, where it no longer interrupts the construction.

## LS044

**expert_companion · keep · keep · direct_product**

**Location:** §4.5 constants and contradiction (source line 240)

**Exact current phrase:**

> The random column $I$ divides the first two terms by $m$

The sentence now assigns roles to the unknown column, the address length, and the slack constants. This is much more useful than reporting only that the final numerical estimate is small.

**Why it matters:** The reader can tell which factors create the separation and which choices merely simplify the contradiction.

**Advice:** Keep this role-based summary after equation (14); its three terms are the natural memory aid for the classical proof.

**Prior-round relation:** Round-six CX030 change confirmed.

## LS045

**expert_companion · low · overweighted · direct_product**

**Location:** §4.5 floor conversion (source line 246)

**Exact current phrase:**

> For the constant in (2), take $k\ge2$, $t\ge8$

The floor conversion is correct, but the companion gives almost every elementary inequality in the conversion immediately after the substantive contradiction. The explicit threshold in the next sentence already greatly exceeds eight.

**Why it matters:** The end of the classical argument loses its emphasis on the mL mechanism and lands on routine rounding.

**Advice:** Keep the resulting coefficient and the sufficient t≥8 condition, with one direct reference to the complete floor calculation. Avoid spending equal space on rounding and the event bound.

## LS046

**expert_companion · keep · keep · fourier**

**Location:** §5 Forrelation supplier, first two paragraphs (source line 255)

**Exact current phrase:**

> Compared with Bansal and Sinha's bound

The current comparison correctly says that the record's bound improves the power of k while worsening the logarithmic power. It also distinguishes what is needed for the fixed-k theorem from what the growing-k remark needs.

**Why it matters:** A reader should not infer that one bound uniformly dominates the other or that the explicit threshold is supplied by the published theorem.

**Advice:** Keep this distinction and the explicit attribution of the constants in (16) to the record.

**Prior-round relation:** Round-six CX012 comparison fix confirmed.

## LS047

**expert_companion · high · underweighted · fourier**

**Location:** §5 Forrelation supplier, proof outline (source line 257)

**Exact current phrase:**

> Because the promise is one-sided

This causal phrase does not yet explain why an algorithm correct only on the promise distinguishes the two non-promise-supported laws. The record's decisive bridge is the pointwise acceptance comparison and its expectation gap; it also explains why constant error is too large relative to the exponentially small positive-promise mass.

**Why it matters:** For a lower-bound specialist this is the delicate interface between Fourier indistinguishability and promise-query hardness. The exact threshold constants get a full paragraph while this interface is asserted in one sentence.

**Advice:** Expose the existing proof's three quantities: positive signal under the planted law, leakage under the uniform law, and amplified error. A single inequality or a short verbal comparison from record §3.14 would justify the stated cause without reproducing the full analytic proof.

## LS048

**expert_companion · keep · keep · fourier**

**Location:** §5 Forrelation supplier, two laws (source line 257)

**Exact current phrase:**

> it is not the minimax law $\mu$ of §4

This distinction is now explicit and correct. The analytic planted law may put mass outside the promise; minimax later supplies a possibly unrelated law entirely supported on the domain.

**Why it matters:** Confusing these distributions would break the direct-product hypothesis and the claim that every planted certificate has a defined address.

**Advice:** Keep the sentence and avoid calling both distributions simply “the hard distribution” without a local qualifier.

**Prior-round relation:** Round-six CX021/CX048 issue is fixed.

## LS049

**expert_companion · medium · credit · fourier**

**Location:** §5 Forrelation supplier, proof outline (source line 257)

**Exact current phrase:**

> in the style of Girish, Tal and Wu

The phrase identifies a source family but not the precise ingredient borrowed: a derivative-growth or stopped-martingale method for trees, distinct from the rounded-Gaussian construction attributed to Bansal–Sinha. The following link supplies the detail only after the whole compressed argument.

**Why it matters:** Readers in the Fourier-growth community need to know which step is an application of a published method and which constants or specializations belong to the record.

**Advice:** Attach a precise section or theorem locator to the method attribution and identify the derivative-growth step it informs. Preserve the separate credit for the chain and for the record's constant calculation.

**Source:** https://doi.org/10.4230/LIPIcs.CCC.2021.39

## LS050

**expert_companion · keep · keep · separations**

**Location:** §6 Optimal exponent, fixed-parameter proof (source line 265)

**Exact current phrase:**

> The quantifiers come in the order:

The explicit order α, fixed k, its constants and threshold, then m→∞ is exactly the needed logical structure. The following sentence also refuses to identify a fixed-k result with an exact fourth-power lower bound.

**Why it matters:** This prevents both an illicit exchange of quantifiers and an overstatement of what “optimal exponent” establishes.

**Advice:** Keep this paragraph essentially intact; it is a better conclusion to the main argument than the numerical growing-k refinement.

## LS051

**expert_companion · medium · teaching · separations**

**Location:** §6 Growing-k remark (source line 267)

**Exact current phrase:**

> With $k=\lfloor\sqrt{t/20}\rfloor$ and $t\ge80$

The stated validity range is not the range in which the displayed exponent is informative. At the first allowed value t=80, ℓ=160 gives ε(ℓ)=7.7376748332, so 4−ε is negative. The inequality can still be true because the function is nonconstant and Q,R≥1; it simply does not demonstrate a near-quartic separation there.

**Why it matters:** Exact thresholds invite readers to interpret the first admissible parameter as a meaningful finite separation example. Here that would be a misreading.

**Advice:** Separate validity of the formula from its asymptotic use. State that its quantitative lower exponent becomes useful later, without seeking a sharper theorem or adding another table of thresholds.

## LS052

**expert_companion · medium · overweighted · separations**

**Location:** §6 Growing-k remark, parameter overload (source line 267)

**Exact current phrase:**

> $\varepsilon(\ell)=8\sqrt{10/\ell}+(56\log_2\ell+508)/\ell$

The derivation is now in the record, but the companion still carries the full error formula, a schedule, two threshold conditions, an exponential quantum constant and a new floor choice in one paragraph. The exact 508 has no subsequent use.

**Why it matters:** The main conclusion already has a clean fixed-k proof. This paragraph feels like a second technical theorem squeezed into a remark, obscuring whether it is required for α_tot=4.

**Advice:** Keep the existence and role of the uniform family in the remark, and move the exact numerical schedule data to the linked record unless the abstract's R≥Q^{4−o(1)} formulation specifically needs a local quantified version.

**Prior-round relation:** The round-six C10 derivation move landed. This concerns the residual information density of the shortened remark, not a missing derivation or the previously corrected 508/514 mismatch.

## LS053

**expert_companion · medium · evidence_presentation · separations**

**Location:** §7 Formal statement, first paragraph (source line 271)

**Exact current phrase:**

> The four statements carry no hypotheses, so their proofs are complete

The absence of hypotheses describes the statements' unconditional scope; it is not by itself what makes proofs complete. The preceding successful proof checking and axiom restriction are the evidence for completeness. The sentence joins two different facts with an unjustified “so”.

**Why it matters:** The formal section should help a reader interpret exactly what the checks establish without inviting the inference that a hypothesis-free statement is automatically proved.

**Advice:** Describe the checked headline statements as unconditional, keeping the proof-checking fact in the preceding sentence. No new caveat or review-status paragraph is needed.

## LS054

**expert_companion · low · overweighted · separations**

**Location:** §7 Formal statement, universal upper-bound constants (source line 275)

**Exact current phrase:**

> gives the constant $35^4$

The two different universal constants, 20736 and 35^4, arrive in a section whose purpose is to relate the formal theorem to the printed statement. Neither affects the exponent or any lower-bound argument in the companion.

**Why it matters:** The reader has to infer whether the two constants represent competing versions, different hypotheses, or merely different proofs of the same universal fact.

**Advice:** Give the mathematical fact that the universal upper bound is included, and leave the proof-route constants in the record unless comparing those proofs is an explicit aim.

## LS055

**expert_companion · keep · keep · direct_product**

**Location:** §7 Formal statement, direct-product scope (source line 279)

**Exact current phrase:**

> success together with compliance

The text accurately presents a joint-event formal statement that can apply to trees exceeding the caps, while separately explaining the finite-seed restriction and the ordinary arguments connecting it to the printed lemma.

**Why it matters:** This is a mixed relation of scope, not simply a “stronger” or “weaker” formal theorem. The paragraph gives a mathematically useful account of that relation.

**Advice:** Keep the joint-event wording and the two named bridge arguments; avoid reducing the relationship to a one-word status label.

## LS056

**expert_companion · low · consistency · direct_product**

**Location:** Appendix A introduction (source line 294)

**Exact current phrase:**

> Here $\beta$ is the best success on one instance within its cap

In §4, β=2/3 is a common upper bound supplied by minimax, not necessarily the exact best success. In the toy examples the displayed β values are exact optima. Calling these the same quantity “as in §4” is imprecise.

**Why it matters:** The direct-product lemma needs an upper bound; the counterexamples use exact values to demonstrate failure. Those roles are compatible but should not be conflated.

**Advice:** Call β a one-instance success bound in the common description, and state that the displayed toy examples use their exact optima.

## LS057

**expert_companion · keep · keep · direct_product**

**Location:** Appendix A, cap-conditioning counterexample (source line 306)

**Exact current phrase:**

> success with the caps respected is $5/16\le\beta^2$

This row gives both the valid joint estimate and the invalid conditional estimate for the same small adaptive experiment. It does more than warn abstractly against conditioning and earns its space despite being the longest row.

**Why it matters:** It provides a concrete check of the subtle logical distinction on which the planted-cell proof depends.

**Advice:** Keep the two probabilities and the repeated-query mechanism. The full enumeration belongs in the record, as it already does.

## LS058

**exposition · keep · keep · learner**

**Location:** Introduction (source line 12)

**Exact current phrase:**

> the count is the worst case over inputs and over every coin flip or measurement outcome.

This sentence fixes both the success quantifier and the cost convention before any examples. That is particularly valuable because the later sampler may fail or stop early, and the classical proof first fixes its random coins.

**Why it matters:** It prevents expected query cost from silently replacing the stated worst-case measure.

**Advice:** Keep this convention visible when describing caps in Section 4.

## LS059

**exposition · medium · structure · learner**

**Location:** Introduction (source line 29)

**Exact current phrase:**

> The exponent comes from one line of arithmetic.

The opening delivers the theorem, formal critical-exponent definition, logarithmic provenance, proof overview, history, AND-OR comparison, prerequisites and route map before the first worked input. In the supplied PDF the introduction occupies roughly two pages and the audience paragraph arrives on the second. The subtitle promises examples first, but this entrance still asks the newcomer to retain the whole construction before seeing a bit string.

**Why it matters:** The reader meets certificates, direct products, addresses and two composed cost comparisons before having an object on which these terms act.

**Advice:** Keep the exact theorem and one-line cost mechanism near the beginning; let the detailed AND-OR comparison and quantitative provenance follow the first board. Check the actual first-page break.

## LS060

**exposition · medium · unclear · separations**

**Location:** Introduction (source line 31)

**Exact current phrase:**

> Q\approx\sqrt m,\qquad R\approx m\cdot L

The displayed approximation signs suggest two-sided complexity estimates. The theorem immediately above supplies an upper bound on Q and a lower bound on R. Those are enough for the separation, but are not the same claim as R and Q being asymptotic to the displayed quantities.

**Why it matters:** The key inferential move is precisely that opposite one-sided bounds prove a separation; an apparent equality hides that lesson.

**Advice:** Mark these as the budgets the construction achieves and the lower bound the adversary forces, retaining the heuristic arithmetic without implying matching bounds.

## LS061

**exposition · high · teaching · separations**

**Location:** Introduction (source line 33)

**Exact current phrase:**

> Since the planted column is unknown, a classical algorithm has to spend about $L$ queries in a constant fraction

The closing sentence turns the later probabilistic heavy/light argument into a per-run learning story. The proof does not say an algorithm must first learn addresses, or literally invest L queries in a fixed fraction of columns on every run. It bounds expensive columns and successful cheap guesses separately. Section 5 now says this correctly, but the opening still plants the misconception the later argument must undo.

**Why it matters:** A learner may come away believing address blindness alone proves the randomized lower bound, missing the simulator and the union over guesses.

**Advice:** Make the opening describe the expensive-column versus lucky-address dichotomy. Keep the later explicit treatment of guessing.

**Prior-round relation:** SX004/CX007 repaired the earlier stronger column claim. This is a remaining distinction between a heuristic learning story and the now-correct lower-bound mechanism.

## LS062

**exposition · keep · keep · certificates**

**Location:** Introduction (source line 39)

**Exact current phrase:**

> AND-OR is used because its small certificates make the promise of the composed function cheap to certify.

The comparison with cheat sheets explains why AND-OR was present, rather than listing earlier exponents without a mechanism. It connects the old totalisation problem to the current certificate construction and identifies where the old cubic accounting comes from.

**Why it matters:** This gives the new exponent a meaningful baseline and credits the predecessor for solving a real certification problem.

**Advice:** Keep the explanation, but place it after the newcomer has seen what this paper means by a certificate.

**Source:** Aaronson–Ben-David–Kothari, arXiv:1511.01937v2, §3.1, https://arxiv.org/abs/1511.01937

## LS063

**exposition · high · teaching · learner**

**Location:** Introduction (source line 41)

**Exact current phrase:**

> This account is written for a graduate student who knows the query models above

The current audience declaration changes the assignment. The packet asks for a mathematically literate newcomer, including an undergraduate or a mathematician from another field. This paragraph instead presupposes the query models, Grover search, amplification with unknown success probability, uncomputation, Yao and adaptive decision-tree conditioning. Naming the prerequisites is useful, but does not supply the requested entrance.

**Why it matters:** A newcomer can read the first definitions and still be unable to perform the first consequential quantum operation or understand what the hard distribution proves.

**Advice:** Keep the fixed audience. Teach the few operations that the examples need and state the deeper results as precise accepted inputs. Report any remaining audience mismatch rather than treating the added prerequisite list as its resolution.

**Prior-round relation:** SX001 added the prerequisite statement; this finding concerns where that repair landed, not the previous absence of an audience statement.

## LS064

**exposition · keep · keep · learner**

**Location:** §1 Three eight-bit inputs (source line 58)

**Exact current phrase:**

> a large **negative** value of $\Phi$ is outside the promise.

The negative example is not decorative: it exposes why a squared-amplitude experiment cannot establish the domain predicate of the eventual total function. The subsequent changed board cashes out exactly this distinction.

**Why it matters:** This is an example that teaches a necessary construction feature, not merely a small calculation.

**Advice:** Preserve the signed convention and its explicit return in the domain-bit example.

## LS065

**exposition · low · teaching · learner**

**Location:** §1 Three eight-bit inputs (source line 66)

**Exact current phrase:**

> the Walsh transform scaled to preserve length.

For the displayed 4-by-4 matrix, the claim that H preserves length is accessible from the row dot products, but the text imports it as a name. A newcomer who has not seen the Walsh transform has no local reason why the geometric picture is legitimate.

**Why it matters:** This is the first point where the displayed matrix can teach the operation instead of requiring prior vocabulary.

**Advice:** Indicate the orthogonality calculation for this matrix, or explicitly invite the reader to check H-transpose H equals the identity; no general Fourier theory is needed.

## LS066

**exposition · low · unclear · learner**

**Location:** §1 Three eight-bit inputs (source line 68)

**Exact current phrase:**

> so a single run happens to decide them.

One of the three inputs has no value of P. The experiment produces a definite outcome on all three, but it does not decide P on the unpromised a-minus. The next paragraph corrects the conceptual picture, yet this sentence briefly uses decision language outside the function domain.

**Why it matters:** The exposition is teaching exactly the distinction between accepting an off-promise string and deciding a partial function.

**Advice:** Keep the calculation but describe the three experimental outcomes rather than calling all three decisions.

## LS067

**exposition · low · overweighted · learner**

**Location:** §1 Three eight-bit inputs (source line 72)

**Exact current phrase:**

> Of all $256$ inputs, $104$ are one-inputs, $48$ are zero-inputs and $104$ lie outside the promise

The census is unexplained and does not feed the later board, decoder or lower bound. The symmetry between positive and negative values is useful; the exact totals feel like validation output inserted into the lesson.

**Why it matters:** The reader has just learned the promise distinction and is diverted into counts they are neither shown how to obtain nor asked to use.

**Advice:** Keep the symmetry if useful. Route the complete census to the existing checked-example destination unless a later teaching task uses it.

## LS068

**exposition · keep · keep · certificates**

**Location:** §2 One column, then four (source line 84)

**Exact current phrase:**

> Every bit is an input bit, and every assignment is allowed.

This is the right short statement of totality. In particular it prevents the reader from assuming that stored transcripts or pointer fields are truthful by definition.

**Why it matters:** The later verifier and adversarial dummy input only make sense when malformed certificates are allowed inputs.

**Advice:** Keep it adjacent to the input layout, rather than deferring totality to the proof.

## LS069

**exposition · medium · prose · learner**

**Location:** §2 One column, then four (source line 88)

**Exact current phrase:**

> Column $i$ **wins** at address $s$ when four conditions hold

The four defining conditions are packed into one semicolon chain. These conditions are independently referenced by the transcript argument, domain-bit counterexample, pointer comparison and final tests. Their stable identities are harder to remember than they need to be.

**Why it matters:** The reader repeatedly reconstructs which clause is being used, especially when Section 7 calls back to the second clause.

**Advice:** Give the four clauses a stable visually parallel presentation and use those same roles in the local-test explanation. This is a functional list, not prose that needs to be homogenised to a register statistic.

## LS070

**exposition · medium · credit · certificates**

**Location:** §2 One column, then four (source line 90)

**Exact current phrase:**

> direct pointers to a zero in every other column appear in the work of Ambainis and coauthors

The source does discuss this direct-pointer alternative, but immediately explains why it rejects it: storing all direct pointers in a queried cell makes the alphabet exponentially large and is unsuitable for its Boolean separation. The current sentence is literally defensible yet omits the very issue that makes the present use interesting. The source construction proceeds with a balanced pointer tree.

**Why it matters:** The reader cannot tell whether the new paper reused an implemented gadget or revived a previously rejected representation, nor why the old obstruction no longer blocks the current bit-query comparison.

**Advice:** Keep the credit and carry over the source objection. Explain at the local-cost level how this construction accesses one indexed pointer and pays for its bits without treating the entire certificate as a unit-cost alphabet symbol.

**Source:** Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs, arXiv:1506.04719v3, construction overview, paragraph beginning “In principle”, https://arxiv.org/abs/1506.04719

## LS071

**exposition · medium · teaching · learner**

**Location:** §2 One column, then four (source line 90)

**Exact current phrase:**

> the array has $2^r=m^{20}$ cells, polynomially many.

Polynomially many can sound reassuring without explaining what it is reassuring about. A twenty-power input expansion is enormous, and the reader has not yet been told why the separation is being compared through R versus Q rather than through an efficient implementation in the final input length.

**Why it matters:** The scale choice can look like a hidden resource violation or like a practical algorithmic claim, depending on the reader.

**Advice:** Explain what the polynomial expansion preserves and what the query model charges. Connect this sentence to the later explicit n formula, instead of treating polynomiality as self-explanatory.

## LS072

**exposition · low · overweighted · learner**

**Location:** §2 One column, then four (source line 96)

**Exact current phrase:**

> Every transcript, in the sense defined below, is the true evaluation of a fixed $180$-gate circuit.

The exact 180-gate size arrives before transcript has been explained and later produces the exact total 371. Neither integer is needed to understand why local checking works. Their precision has more visual weight than the one gate equation the learner has not yet seen.

**Why it matters:** The example feels verified but not fully taught at the point where the proof-carrying input is new.

**Advice:** Let a single concrete local equation carry the first teaching burden. Keep exact totals in the linked check unless the exposition uses them for an actual cost exercise.

## LS073

**exposition · keep · keep · learner**

**Location:** §2, Figure 2 (source line 98)

**Exact current phrase:**

> The four-column board. Column 1 wins at address 10

The exposition figure correctly draws four positions in each X string and a certificate at address 10; the blue true-cell outlines distinguish losing columns from an absent address. I inspected the supplied SVG and its rendered image. The expert companion figure problem reported elsewhere does not occur in this exposition figure.

**Why it matters:** This is a usable concrete board and should not receive a copied finding based on another document’s graphic.

**Advice:** Preserve the four-position board and its distinction between true cells and winning cells.

## LS074

**exposition · keep · keep · certificates**

**Location:** §2 The domain bit is needed (source line 104)

**Exact current phrase:**

> A function that checked only value bits would accept this board.

The changed board is an unusually effective counterexample. String, pointer, value and gate conditions all survive; precisely the domain test fails. The example therefore isolates the missing hypothesis rather than merely producing another zero-input.

**Why it matters:** The learner can see why totality needs a domain certificate even though the quantum projection experiment is cheap.

**Advice:** Keep the exact changed-board data and the question that counts failures at its four addresses.

## LS075

**exposition · medium · missing_example · certificates**

**Location:** §2 Local tests (source line 106)

**Exact current phrase:**

> each reading one proposed gate value and the two values feeding it

The text works one pointer test all the way down to three queried bits, but never works a gate-consistency test at that same resolution. A newcomer can follow the pointer while still imagining that checking a transcript means evaluating the whole circuit.

**Why it matters:** The cheap certificate verification is one of the reasons the totalisation succeeds; this is the local operation that needs to become tangible.

**Advice:** Use a gate already in the supplied small circuit, show its three queried values and the pass/fail decision, and state why no earlier gates need to be recomputed during that test. Do not add a new circuit construction.

## LS076

**exposition · medium · teaching · learner**

**Location:** §2 Local tests (source line 106)

**Exact current phrase:**

> each reading the $\ell$ bits of a pointer $p_{i,s,j}$ and then the bit of $X_j$ they name

This charges for learning a stored pointer, whereas choosing a query position in an indexed cell array is free once the algorithm chooses that position. The contrast becomes decisive in Section 5, where a guessed cell address is already a proposed answer vector before any cell content is read. The newcomer would benefit from that distinction here.

**Why it matters:** Without it, the later phrase “position alone” can look as though the lower bound gives the predictor information for free that the algorithm had to read elsewhere.

**Advice:** Distinguish a stored pointer value from the algorithm’s chosen query index using the existing pointer test and a guessed cell position. Keep both within the bit-query model defined at the start.

## LS077

**exposition · medium · teaching · learner**

**Location:** §3 The general partial function (source line 122)

**Exact current phrase:**

> phase kickback

This is a consequential quantum operation, not a harmless name: it explains why multiplying all amplitudes by input-dependent signs costs one bit-oracle call. The opening oracle formula does not by itself teach that conversion to the stipulated newcomer.

**Why it matters:** The claimed two-query experiment can otherwise seem to access four signs at no cost by assumption.

**Advice:** Give the short bit-oracle-to-phase calculation using the answer register, or identify it as the exact accepted operation supplied by the quantum reading route. Avoid assuming a broad quantum algorithms course.

## LS078

**exposition · medium · overweighted · learner**

**Location:** §3 The general partial function (source line 124)

**Exact current phrase:**

> A fast Walsh transform and ripple-carry arithmetic give a circuit of fan-in two

The main route develops the integer thresholds and implementation vocabulary far enough to require arithmetic-circuit background, but not far enough to teach or verify the size constant. The subsequent argument only consumes an exact domain/value circuit of near-linear size.

**Why it matters:** The newcomer spends attention on an implementation sketch while the role of exactness versus fast decoding is the concept they need to retain.

**Advice:** Keep the circuit contract, its size and why that size is sufficient visible; route the fast-transform and ripple-carry implementation to the existing record destination.

## LS079

**exposition · medium · underweighted · learner**

**Location:** §3 The general partial function (source line 130)

**Exact current phrase:**

> This is the randomized lower bound of Bansal and Sinha for this one-sided promise

The hard Forrelation estimate is responsibly identified as an imported theorem, but it receives only its formula and citation while the routine exact-circuit implementation receives a detailed arithmetic description. For a newcomer, the main unexplained source of difficulty is why a few classical observations cannot reliably distinguish the promised cases, not how the integer comparison is wired.

**Why it matters:** The exposition explains the amplification of hardness much better than the source of the hardness. That is acceptable only if its lesson boundary is explicit.

**Advice:** State clearly that the lesson imports this analytic lower bound, give a short explanation of the indistinguishability task it solves, and point to the expert or record account for the proof idea. Do not attempt a new Fourier proof in the exposition.

## LS080

**exposition · keep · keep · certificates**

**Location:** §3 The general partial function (source line 132)

**Exact current phrase:**

> Both bounds concern this one function, with the same circuit.

This closes an important possible loophole: the quantum upper bound cannot choose a cheap verifier while the classical lower bound talks about a different total function. The exact circuit is public and fixed throughout.

**Why it matters:** The same-family requirement is central to a separation and is easy to lose in a modular presentation.

**Advice:** Keep this sentence and its return after the classical proof.

## LS081

**exposition · keep · keep · learner**

**Location:** §4 The quantum algorithm: a tournament (source line 136)

**Exact current phrase:**

> a Grover search over $m$ columns with that check inside costs about $\sqrt m\cdot\sqrt m=m$

This is the right immediate motivation for the tournament. It makes the obvious nested search fail quantitatively before introducing a more elaborate algorithm.

**Why it matters:** The learner understands why cheap comparisons and a short candidate list are necessary for the desired exponent.

**Advice:** Keep the cost comparison; it is more informative than simply announcing a tournament lemma.

## LS082

**exposition · keep · keep · learner**

**Location:** §4 A cycle among losers (source line 146)

**Exact current phrase:**

> the search cannot sort them.

The cycle and the dominating nonwinner are different failures of tempting shortcuts. The first rules out treating pairwise outcomes as an order, while the second rules out accepting the best-looking candidate. The current concrete pointers make both claims inspectable.

**Why it matters:** This avoids presenting the comparison oracle as an ordinary bounded-error order test and explains the need for final verification.

**Advice:** Preserve both examples and the statement that loser probabilities need not be bounded away from one half.

## LS083

**exposition · keep · keep · learner**

**Location:** §4 An ideal process (source line 152)

**Exact current phrase:**

> The weights are defined from the unknown probabilities $a_{ij}$; the algorithm never computes or estimates them.

The paragraph cleanly distinguishes an analytical process from an implementable procedure before defining the weights. The absorbing zero-weight state is also specified, so the drift argument does not silently divide by zero.

**Why it matters:** This removes a common false impression that the algorithm learns all pairwise probabilities or numerically maintains the weights.

**Advice:** Keep these two scope statements when shortening the algorithm section.

## LS084

**exposition · medium · overweighted · learner**

**Location:** §4 Amplification with a fixed cap (source line 179)

**Exact current phrase:**

> Either way a trial succeeds with probability at least $9/40$.

The full 3/8, 19/40, 9/40 and logarithmic trial-count derivation remains on the main path. The next construction-specific step needs a capped amplification contract and preservation of the conditional pivot law, not these numerical choices. This is one of the longest uninterrupted prose paragraphs in the exposition.

**Why it matters:** The learner’s live question—how to sample the ideal pivot law with a worst-case budget—is interrupted by a textbook subroutine proof.

**Advice:** Keep the contract and the state-direction reason visible; make the constant calculation optional or use the existing record proof.

**Prior-round relation:** SX022/QX020/CX024 planned to move recipe-level constants out of the main exposition. The current Markdown still contains them.

## LS085

**exposition · keep · keep · learner**

**Location:** §4 Amplification with a fixed cap (source line 179)

**Exact current phrase:**

> amplification changes how often we succeed but not the distribution of the column given success.

This is the indispensable bridge from quantum amplification to the classical ideal process. Explaining it through the preserved direction of the good state is more useful than an unexplained assertion that the sampler is correct.

**Why it matters:** The drift proof uses a specific conditional pivot distribution, not merely a successful search for any surviving column.

**Advice:** Keep this argument even if the numerical amplification recipe is removed from the main route.

## LS086

**exposition · keep · keep · learner**

**Location:** §4 A stage of the search (source line 181)

**Exact current phrase:**

> After the winner is listed, $|w|$ may be tiny or zero and the sampler may fail with certainty

The failure state is explained at the point where it matters. Stopping after the winner is listed is harmless, and the cap still applies when no winner exists. This addresses the all-input query bound rather than analysing only successful positive inputs.

**Why it matters:** The main theorem is about a total function and every measurement branch; the pathological-looking branches are part of the stated algorithm.

**Advice:** Preserve this explanation and the empty-list output in verification.

## LS087

**exposition · low · missing_example · learner**

**Location:** §4 A stage of the search (source line 183)

**Exact current phrase:**

> so the decoders are exact and the comparisons deterministic.

The four-column calculation teaches the pivot law, but its weights only become zero or one. The general argument’s use of fractional comparison probabilities remains unexperienced. This is not a defect in the board; it is a limit of what the board demonstrates.

**Why it matters:** A reader can master the worked tournament while still treating weights as a surviving subset of columns, which is stronger than the theorem allows.

**Advice:** At this point give an exact route to the record’s existing fractional-weight example, or briefly state the missing distinction. Do not replace the useful deterministic board with a large new example.

## LS088

**exposition · medium · error · learner**

**Location:** §4 Amplification with a fixed cap; The count (source line 189)

**Exact current phrase:**

> Every number of trials, iterations, stages and comparisons is fixed in advance

The realised numbers are not fixed in advance in the algorithm just described: a trial randomises its iteration count, trials stop at success, and stages stop on reported failure. What is fixed in advance is a branchwise upper cap. The mathematical worst-case argument is sound with that distinction, but the current sentence states the wrong operational fact.

**Why it matters:** The exposition should teach how an adaptive or random algorithm can have a deterministic query bound, rather than suggest it has a deterministic execution length.

**Advice:** Replace the claim about realised counts with the actual cap property. Make the same adjustment to “The number of preparations is fixed in advance” in the amplifier paragraph.

## LS089

**exposition · medium · teaching · learner**

**Location:** §5 The classical lower bound: a planted pair (source line 197)

**Exact current phrase:**

> By Yao's minimax principle

The statement following the citation is precise, but a newcomer needs the change of quantifiers made explicit: one distribution defeats every capped deterministic tree, rather than a different difficult input selected for each tree. The later independent sampling relies on committing to that one law first.

**Why it matters:** The lower bound is not just “random inputs are hard”; it needs a shared hard law that can be sampled repeatedly and supplied to the predictor reduction.

**Advice:** Explain this single role of minimax in the main text, keeping the complete finite proof in its existing destination.

## LS090

**exposition · low · unclear · learner**

**Location:** §5 The pair (source line 199)

**Exact current phrase:**

> leave every cell blank.

Blank sounds like an extra symbol or an absent record, although the function was defined on Boolean assignments only. The expert companion explicitly says every cell bit is zero; the exposition does not.

**Why it matters:** The dummy input must be a concrete member of the total Boolean domain, and the coupling later compares actual bit values.

**Advice:** Specify the fixed bit pattern meant by blank at its first use. Retain the explanation that a filled bit can equal its blank value.

## LS091

**exposition · medium · error · direct_product**

**Location:** §5 Figure 4 introduction (source line 201)

**Exact current phrase:**

> At $m=4$ there is no hard distribution

This is false literally. Section 1 supplies promised inputs a-plus and a-zero with different values. For L_{2,4}=0, their uniform distribution makes every zero-query deterministic algorithm succeed with probability 1/2, hence at most 2/3. What fails at this size is the useful positive-budget lower-bound application, not existence of a hard distribution in the stated sense.

**Why it matters:** The lesson conflates a degenerate numerical bound with nonexistence of the object used to prove it.

**Advice:** Say exactly which large-m or positive-L hypothesis the picture does not meet. Keep the distinction between a diagram of the coupling and a nontrivial quantitative lower bound.

## LS092

**exposition · keep · keep · direct_product**

**Location:** §5 The pair (source line 210)

**Exact current phrase:**

> where both events refer to the run on the dummy input.

This is the decisive coupling convention. It permits the chosen column to remain independent of the run being counted and makes the first differing query the correct witness, even when later planted answers would change the algorithm’s behaviour.

**Why it matters:** Counting arbitrary visits in the planted execution would destroy the simple independence argument.

**Advice:** Keep this explicit convention and the observation that counting all true-cell visits only overestimates the chance of a distinguishing query.

## LS093

**exposition · high · unclear · direct_product**

**Location:** §5 The erased zero (source line 216)

**Exact current phrase:**

> condition on the whole transcript of the dummy run.

To justify the next-query discovery probability, the conditioning must be on the history before that query. If “whole transcript” means the completed run, whether an earlier query found the zero is already known and its conditional probability is generally zero or one. The expert companion correctly says “given the past”; the exposition’s wording obscures the filtration needed by this adaptive argument.

**Why it matters:** The early/late estimate is a genuine lower-bound step, and the current temporal wording invites an invalid conditioning calculation.

**Advice:** Name the current transcript prefix, including prior queries to other fields. Explain residual uniformity on unread positions relative to that prefix; do not weaken the conditioning to only the current column.

**Prior-round relation:** SX026 requested full adaptive conditioning. The current repair risks reading “full transcript” as the final transcript instead of the entire past.

## LS094

**exposition · keep · keep · direct_product**

**Location:** §5 The erased zero (source line 218)

**Exact current phrase:**

> A uniform marginal is a weaker condition than independence from the run

The four-column calculation makes the independence condition do visible work: both choices of I are marginally uniform, but their hit probabilities differ. It also specifies the no-discovery branch, so the alternative law is actually defined.

**Why it matters:** This teaches the exact information pattern the coupling needs and is more useful than a generic warning about independence.

**Advice:** Preserve the calculation and its changed-case question.

## LS095

**exposition · keep · keep · separations**

**Location:** §5 The true cell (source line 222)

**Exact current phrase:**

> The algorithm need not compute $s_I$ to reach $B_{I,s_I}$: it may guess an address or visit many cells.

This is a substantive improvement over the address-hiding slogan. It recognises that naming a correct cell can be lucky and sets up the direct-product bound on predictors at individual query slots.

**Why it matters:** The proof must cover algorithms that enumerate addresses or spread guesses without explicitly computing any Forrelation output.

**Advice:** Keep it and align the introduction’s learning language with it.

**Prior-round relation:** The current text resolves the previous complaint that guessing was omitted; do not report that old omission again.

## LS096

**exposition · low · missing · direct_product**

**Location:** §5 The true cell (source line 222)

**Exact current phrase:**

> At most $G/L$ columns are heavy

The division uses L>0. The opening says m is large, so the intended Forrelation application has this property, but the exposition then uses a zero-budget toy and makes the erroneous hard-distribution comment. An explicit positive-L premise would keep those roles separated.

**Why it matters:** The generic counting argument has a hypothesis the smallest displayed example does not satisfy.

**Advice:** State 1≤L≤m when entering the generic lower-bound calculation, as the expert companion does, and keep toy geometry separate from that premise.

## LS097

**exposition · keep · keep · direct_product**

**Location:** §5 Direct product with separate caps (source line 233)

**Exact current phrase:**

> One answer may raise $V_h$; only the average cannot.

The AND calculation correctly teaches the supermartingale step rather than falsely asserting that every branch’s conditional success decreases. It also shows why adaptivity is compatible with the product argument.

**Why it matters:** This is exactly where an intuitive multiplication of independent success probabilities would otherwise be inadequate.

**Advice:** Keep the small calculation inside the optional proof; the lemma statement and its hypotheses should remain outside the box.

## LS098

**exposition · keep · keep · direct_product**

**Location:** §5 Why the event must be joint (source line 236)

**Exact current phrase:**

> its success given that it stays light is $1$.

The three-input AND example isolates the selection-bias error with very little machinery. It distinguishes a valid joint-event bound from an invalid conditional bound and is directly consumed by the simulator paragraph.

**Why it matters:** The reader can see why lightness must remain inside the event instead of being treated as a promise under a new law.

**Advice:** Preserve this example near the simulator rather than moving it to a generic list of counterexamples.

## LS099

**exposition · high · missing_example · learner**

**Location:** §5 The simulator (source line 238)

**Exact current phrase:**

> it stops before the $(L+1)$-st forwarded query.

The exposition names the simulator’s operations clearly but leaves its only actual query-by-query trace in the record. This is the novel lower-bound reduction: a real transcript that attempts a cell query must become a valid separately capped predictor, including on runs that would exceed the cap. The main worked board does not execute that operation.

**Why it matters:** A newcomer can follow the distributions and direct-product lemma yet fail to connect them. The proof then risks being remembered as address blindness despite containing the correct reduction.

**Advice:** Bring a compact part of the already supplied XOR simulator trace into the exposition, including one run that stops and one that reaches the selected query slot. Use the existing example and state its changed law and indexing.

## LS100

**exposition · medium · teaching · learner**

**Location:** §5 The simulator (source line 238)

**Exact current phrase:**

> otherwise it outputs a fixed address.

The fallback output looks like arbitrary housekeeping unless the text explains that the direct-product theorem needs a total predictor on every execution. The lower-bound event only implies predictor success in one direction; it does not require all predictor successes to correspond to the event.

**Why it matters:** The learner may object that a default guess can be right, or mistakenly try to condition away aborted runs.

**Advice:** Explain why default successes are harmless overcounting and why a defined output on aborted or irrelevant runs allows the theorem to be applied without conditioning.

## LS101

**exposition · keep · keep · direct_product**

**Location:** §5 The simulator (source line 240)

**Exact current phrase:**

> Three budgets are in play.

The distinction between the global G budget, the simulator’s total L allowance for one column, and the separate L cap per instance is now explicit and correct. The observation that the second implies the third addresses the actual reduction rather than merely restating the lemma.

**Why it matters:** This prevents a false pooled-budget interpretation and explains why a stronger-cap simulator can use the separate-cap theorem.

**Advice:** Keep this paragraph; it is not disposable numerical bookkeeping.

**Prior-round relation:** SX030 requested this separation. The current text implements it, so it should be retained rather than raised again as missing.

## LS102

**exposition · medium · teaching · learner**

**Location:** §5 The simulator (source line 244)

**Exact current phrase:**

> so no factor $m$ appears

The sentence explains the cancellation verbally, but this is the exact place a first-time reader is likely to union over all mG candidate slots and lose the lower-bound exponent. One displayed average over I would make the accounting checkable.

**Why it matters:** The factor m in the final lower bound depends on distinguishing a union over query times from averaging over the independent planted column.

**Advice:** Show the existing calculation as an average of m per-column bounds before simplifying. No new lemma or tighter estimate is needed.

## LS103

**exposition · medium · teaching · learner**

**Location:** §5 Finishing (source line 249)

**Exact current phrase:**

> A randomized algorithm computing $F$ with $G$ queries would have gap at least $1/3$

The closing contradiction skips the elementary bridge from worst-case correctness on every Boolean input to the average gap under the planted pair. The reader needs to see that positive inputs are accepted with probability at least 2/3 and negative inputs with probability at most 1/3, then average those inequalities.

**Why it matters:** This is where the hard distribution proves a lower bound for all bounded-error algorithms, rather than just poor average performance of one deterministic strategy.

**Advice:** Spell out the two acceptance inequalities and their difference before averaging over coins. Keep the fixed-cap convention from the introduction.

## LS104

**exposition · low · unclear · learner**

**Location:** §6 Exponent four, and the order of quantifiers (source line 257)

**Exact current phrase:**

> Both are at least $1$ once $t\ge8$

The displayed reason establishes the lower bound for the unfloored expression defining L, but the second floor also needs mL/100≥1. This follows easily here, yet it is not what the displayed inequality itself proves.

**Why it matters:** A passage introduced to make the constant transparent should account for both floor applications it explicitly invokes.

**Advice:** Give the short second check or route the numerical constant calculation to the record and keep only its consequence on the main path.

## LS105

**exposition · medium · unclear · separations**

**Location:** §6 Exponent four, and the order of quantifiers (source line 265)

**Exact current phrase:**

> $k=2$ gives exactly the cube.

For k=2 the polynomial threshold is three, but the displayed bounds retain logarithmic losses. At α=3 the lower bound on the ratio is proportional to a negative power of log m, not a divergent quantity. “Exactly the cube” can be read as an attained cubic relation or a refutation of the cubic upper bound, neither of which follows from this k.

**Why it matters:** The section is explicitly teaching strict exponents and endpoints; loose language here defeats that purpose.

**Advice:** Distinguish the polynomial threshold from an endpoint inequality. Keep the k=3 choice for refuting the cubic conjecture.

**Prior-round relation:** The previous statement-fidelity review marked the endpoint wording as an optional clarification; it remains unresolved in the current exposition.

## LS106

**exposition · keep · keep · separations**

**Location:** §6 Exponent four, and the order of quantifiers (source line 267)

**Exact current phrase:**

> substituting $k=t$ asks for $t\ge2^t$, which never holds.

The artificial threshold example isolates the quantifier error cleanly without claiming it is the true Forrelation threshold. It shows why “for each fixed k, eventually” cannot justify an arbitrary growing k.

**Why it matters:** The final passage needs this distinction to support taking an infimum of exponents while allowing constants to depend on k.

**Advice:** Keep this simple logical example and the order α, then k, then m.

## LS107

**exposition · low · overweighted · learner**

**Location:** §6 Exponent four, and the order of quantifiers (source line 271)

**Exact current phrase:**

> the record reconstructs it with the constant $35^4$

The explicit deterministic-upper-bound constant does not affect the critical exponent or any calculation in this exposition. It arrives after the reader has completed the main separation argument and creates another apparently important quantity with no teaching use.

**Why it matters:** It dilutes the conclusion with provenance-level precision, while the proof of the matching upper bound is intentionally elsewhere.

**Advice:** Keep the theorem, its dependence on Huang and the proof destination; leave the numerical reconstruction constant in the record.

## LS108

**exposition · medium · evidence_presentation · learner**

**Location:** §7 The statement in Lean (source line 275)

**Exact current phrase:**

> There [$R$][def-R] is defined through [finite random mixtures][def-randomized] of [decision trees][def-tree]

The paragraph turns nearly every technical noun into a separate link. The useful invitation in the next paragraph—check one concrete winning-condition clause on the changed board—is much more actionable for this audience than a forest of definition links.

**Why it matters:** A newcomer can click many endpoints without knowing which question a click answers or which definitions deserve attention first.

**Advice:** Lead with the concrete definition check and group the general model links behind the statement-file destination. Preserve exact formal scope in ordinary prose.

## LS109

**exposition · keep · keep · separations**

**Location:** §7 The statement in Lean (source line 275)

**Exact current phrase:**

> the power of the logarithm in the quantum bound left unspecified.

This correctly states a material difference between the formal family theorem and the numeric headline. The formal statement is not being presented as though it alone certifies the power six printed in the exposition.

**Why it matters:** It keeps the distinction between checked theorem scope and a more explicit paper-level estimate legible.

**Advice:** Keep this sentence and the path to the record’s explicit count; avoid adding receipt identifiers to the teaching document.

## LS110

**exposition · medium · error · learner**

**Location:** Answers to the questions, Question 2 (source line 283)

**Exact current phrase:**

> and rejects $2$ and $4$ by the zeros in their own strings.

The verification algorithm searches for a failed local test with bounded error. Exact toy decoders and deterministic comparisons do not make this search exact: a nonwinner can still be accepted when the capped search misses a failing test. The answer’s unconditional rejection claim is stronger than the verification contract stated in Section 4.

**Why it matters:** The worked example silently changes a bounded-error algorithm into an exact one at the final step.

**Advice:** Distinguish the deterministic fact that these columns fail string tests from the verifier’s probability of discovering those failures. Keep the certain one-iteration amplification claim for the separate pivot preparation, where p=1/4 justifies it.

## LS111

**exposition · medium · teaching · learner**

**Location:** Answers to the questions (source line 285)

**Exact current phrase:**

> **[Question 3](#question-3).** An independent $I$ is hit with probability

The four questions assess local-test counts, a deterministic tournament step, independence of I, and an exponent choice. None asks the learner to use the capped predictor and the joint event, although reconstructing that reduction is central to the promised classical explanation. The existing Question 3 only exercises the easier erased-zero side.

**Why it matters:** Success on every current exercise would not establish that the reader understands why guessed cell visits are rare.

**Advice:** Add or retarget one changed-case task using the record’s existing simulator trace. Ask what happens when a selected cell query occurs before versus after the cap, keeping the solution separate.

## LS112

**exposition · medium · error · separations**

**Location:** §6 Question 4 and answer (source line 287)

**Exact current phrase:**

> as $k=2$ for the cube, $k=4$ gives exactly $3.5$ and does not suffice.

For the question as written—showing α_tot≥3.5—k=4 does suffice. That fixed family rules out every α<3.5 because d=1.75−α/2>0 for each such α; therefore the infimum of universal exponents is at least 3.5. Choosing k=5 is a valid answer under the displayed strict recipe and also rules out the endpoint inequality with exponent 3.5 itself. The error is the unqualified claim that k=4 does not suffice for the stated infimum goal, not the choice of k=5.

**Why it matters:** The exercise teaches the wrong boundary logic for the infimum that defines the theorem.

**Advice:** Match the task and answer: decide whether it tests a lower bound on the critical exponent or failure of the endpoint universal inequality. Preserve that distinction in the cubic comparison too.

## LS113

**exposition · keep · keep · certificates**

**Location:** Use of AI tools (source line 291)

**Exact current phrase:**

> The theorem and the construction are OpenAI's

The attribution separates the original mathematics from the exposition and its formal development. This is especially useful because the prose earlier describes a combination as new.

**Why it matters:** It avoids crediting the explanatory artifact with discovering the theorem.

**Advice:** Preserve the attribution while making borrowed gadget roles precise at their local use.

## LS114

**reasoning_record · high · error · direct_product**

**Location:** Opening mechanism paragraph (source line 5)

**Exact current phrase:**

> reveals its planted cell with probability at most $(2/3)^r$

Read literally, this probability assertion is too strong. The proved statement is the fixed-time joint bound Pr[i nonheavy AND query q lies in B_{i,s_i}] ≤ (2/3)^r. Visiting the cell at any time requires the union over at most G times, giving G(2/3)^r. The preceding description of a column receiving few queries also invites conditioning on nonheaviness, which §6.5 correctly shows is invalid. This is an error in the printed summary assertion; the detailed proof in §6.5 is correct.

**Why it matters:** The opening is where a lower-bound specialist forms the model of the reduction. Dropping the time index conceals the entire reason for the long address.

**Advice:** State the joint fixed-time meaning at the overview level, or give the all-time G-factor explicitly. Preserve the two distinguishing channels and the correct detailed simulator proof.

**Prior-round relation:** Round-six CX008 was addressed, but the new summary still loses a quantifier and a union factor; this is a defect of the landed fix.

## LS115

**reasoning_record · medium · funnel · direct_product**

**Location:** Reading guide: construction route (source line 16)

**Exact current phrase:**

> with the statement of Lemma 4.1 in place of its proofs

The revised route is much better, but this phrase does not tell me whether to read the cap-event corollary, the adaptive example, or the planted-use paragraph. Those are not interchangeable with the two proofs. The simulator uses a total cap and a joint event, so the jump from the lemma statement directly to §6.2 needs an explicit destination.

**Why it matters:** A reader following the promised short route may skip the explanation that prevents the most tempting misuse of the direct product.

**Advice:** Give precise links to the lemma statement, the joint-event interface if desired, and “Use in the planted argument”; state where the specialist resumes. Keep both proofs available.

**Prior-round relation:** Follow-up to the implemented round-six route repair, not a claim that the old “required” labels remain.

## LS116

**reasoning_record · keep · keep · separations**

**Location:** §1: theorem and exponent argument (source line 64)

**Exact current phrase:**

> The two inequalities concern the same function at each pair $(k,m)$.

This sentence is worth keeping exactly at the theorem. The later generic classical theorem works for every realizing circuit, whereas the quantum estimate uses a particular efficient circuit; the common-function requirement is therefore substantive.

**Why it matters:** It prevents separate existence claims for an easy quantum function and a hard randomized function from being mistaken for a separation.

**Advice:** Preserve the sentence and its connection to the circuit-independence observation in §6.6.

## LS117

**reasoning_record · medium · evidence_presentation · separations**

**Location:** §1.1 dependency map and Appendix B scope (source line 126)

**Exact current phrase:**

> Statements of all claims

The catalogue tracks the maintained source claims, but it does not give a separate entry for the new growing-k derivation. “All claims” therefore overstates what a reader can find there.

**Why it matters:** A referee following a claim from the companion may search the catalogue and infer a missing proof even though the proof exists in §7.3.

**Advice:** State the catalogue’s actual scope and provide navigation to existing additions outside it. An index update or scope label is enough; do not create new formal targets.

## LS118

**reasoning_record · high · consistency · separations**

**Location:** §1.1: routes into the record (source line 130)

**Exact current phrase:**

> whose §§4–6 summarize the quantum tournament, the planted lower bound and the Forrelation supplier

The companion has been renumbered. Its quantum tournament is §3, randomized lower bound §4, Forrelation supplier §5, and exponent conclusion §6. This sentence now describes the wrong section range.

**Why it matters:** The record promises dependable return routes but sends a reader one section too late before they have even begun the proof.

**Advice:** Update the section names and numbers together, and check all prose return instructions as well as hyperlink targets. The current range for the three named topics is §§3–5.

**Prior-round relation:** Navigation regression after the round-six restructuring.

## LS119

**reasoning_record · low · prose · separations**

**Location:** §2.1: inputs and partial functions (source line 161)

**Exact current phrase:**

> This is the source type `PartialBool I`.

The mathematical description is clear, but the immediate switch to an implementation type interrupts it. Similar source-first phrasing recurs throughout §2 even after the formal apparatus was moved to Appendix G.

**Why it matters:** A classical specialist reading only the model conventions has to distinguish mathematical hypotheses from implementation identifiers before either bound appears.

**Advice:** Retain the domain-and-value convention in the body; concentrate implementation spelling in G.2 or a compact margin/reference note. No definition or proof needs to change.

**Prior-round relation:** Residual prose after evidence concentration, rather than a request to restore or re-audit moved material.

## LS120

**reasoning_record · keep · keep · direct_product**

**Location:** §2.2: finite random mixtures (source line 204)

**Exact current phrase:**

> They use the allowed arbitrary real biases;

The finite-mixture argument properly states the convention needed at an exact success threshold. The later OR example makes the distinction from a fixed finite number of fair bits concrete.

**Why it matters:** This is a real model boundary for the compactness/minimax argument, not merely notation.

**Advice:** Keep the convention and the example. A specialist route can skip the detailed example once this sentence has fixed the model.

## LS121

**reasoning_record · low · prose · separations**

**Location:** §2.3: oracle conventions (source line 236)

**Exact current phrase:**

> In this edition §2.3 is “Quantum parallelism.”

This sentence answers an earlier citation mistake rather than a question about the oracle model. The correct edition and locator are already recorded in Appendix C.

**Why it matters:** Version forensics interrupt an otherwise clean explanation of the controlled-phase distinction.

**Advice:** Keep the accurate citation and move this correction history to the inspected-edition note. Preserve the actual controlled-versus-bare phase-oracle warning.

## LS122

**reasoning_record · keep · keep · certificates**

**Location:** §2.6: example ordering (source line 335)

**Exact current phrase:**

> Each example below tests one convention against a plausible misreading.

The new risk-to-example table earns its place. The off-promise example explains why a domain bit is part of a certificate; the OR example fixes an exact endpoint; parity distinguishes the two query models.

**Why it matters:** A reader can now select an example for a genuine doubt rather than reading a collection of unrelated small facts.

**Advice:** Preserve the map, and keep its links to the later construction and cap examples current.

**Prior-round relation:** Successful round-six repair of the missing example-purpose map.

## LS123

**reasoning_record · medium · evidence_presentation · separations**

**Location:** §2.6: zero-query example (source line 356)

**Exact current phrase:**

> the packet supplies no successful receipt for those exact example declarations

The referent of “the packet” is no longer clear. G.4 now lists a compared ModelZero statement saying that D, R and Q vanish exactly on functions constant on the promise. The quoted sentence may concern older proposed example declarations rather than that general theorem, but the current reader cannot recover that distinction here.

**Why it matters:** A reader can leave the body believing there is no recorded formal support for precisely the characterization that the current appendix says was compared.

**Advice:** Date the frozen return explicitly, or replace this historical status aside by a pointer to the current G.4 row. This asks for clearer presentation of existing evidence, not a new Lean run.

## LS124

**reasoning_record · keep · keep · fourier**

**Location:** §3 opening: the three-property interface (source line 429)

**Exact current phrase:**

> The construction uses the same partial function in two ways.

The opening makes a useful distinction between proposing a value quantumly and certifying domain membership by an exact circuit. It gives the reader a reason for the circuit before its arithmetic begins.

**Why it matters:** The eventual total function depends on both interfaces; a cheap promise algorithm alone does not validate a certificate.

**Advice:** Retain this explanation when shortening the introductory contract.

## LS125

**reasoning_record · keep · keep · fourier**

**Location:** §3.4: circuit route and §3 opening (source line 440)

**Exact current phrase:**

> From §3.4 it needs only the opening contract and the size bound

The current draft explicitly allows construction readers to bypass the gate census after recovering the interface. This resolves the earlier complaint that the arithmetic implementation was an unavoidable prerequisite.

**Why it matters:** The long record can preserve complete arithmetic while still serving the lower-bound reader.

**Advice:** Keep this permission and the direct destination; do not reimpose a compulsory line-by-line circuit read.

## LS126

**reasoning_record · keep · keep · fourier**

**Location:** §3.1: one-sided promise (source line 483)

**Exact current phrase:**

> so a value $\Phi=-1$ is unpromised.

This explicit negative-value case prevents the reader from silently replacing the positive-threshold yes promise by an absolute-value promise. The following small instance makes the distinction testable.

**Why it matters:** The quantum projection observes Φ², while the exact domain circuit must distinguish a large negative value from a promised yes input.

**Advice:** Keep this boundary case beside the definition.

**Source:** https://arxiv.org/html/2008.07003v3#S1

## LS127

**reasoning_record · keep · keep · fourier**

**Location:** §3.2: numerator recurrence (source line 514)

**Exact current phrase:**

> evaluating its $m^k$ summands one at a time would be wasteful

The record first identifies the exact integer by a path sum and then supplies a recurrence computing that same integer. This is a good explanation of why a formal finite expression is not yet an efficient circuit.

**Why it matters:** The claimed near-linear circuit size would be implausible if the reader thought the implementation enumerated paths.

**Advice:** Preserve the equivalence between the recurrence and the displayed numerator.

## LS128

**reasoning_record · low · teaching · fourier**

**Location:** §3.3: projection measurement (source line 545)

**Exact current phrase:**

> The word is applied from right to left.

The operation order is correctly stated, but the first use of the alternating word would benefit from a very short index trace for k=3, identifying which input block is queried first and which is last.

**Why it matters:** The record shifts block indices relative to the preprint, and matrix multiplication order is a common source of wrong mental pictures.

**Advice:** Specialize the already-defined operator word to k=3 as a short index trace, without adding another general construction. Keep this distinct from the later Gaussian three-block calculation.

## LS129

**reasoning_record · keep · keep · fourier**

**Location:** §3.7: derivative normalization (source line 968)

**Exact current phrase:**

> These raw derivatives let us work under the biased product measure itself

This sentence accurately identifies the quantity controlled later. The proof does not simply insert a uniform Fourier-level estimate at a nonzero bias.

**Why it matters:** At a biased point, a kth derivative contains contributions from higher uniform Fourier levels; this matters to both credit and the correctness of the transfer.

**Advice:** Keep the raw-derivative convention adjacent to (F8) and preserve the later (F24) explanation.

**Source:** https://arxiv.org/html/2103.11604v2

## LS130

**reasoning_record · keep · keep · fourier**

**Location:** §3.8: bounded Stein identity (source line 975)

**Exact current phrase:**

> We need bounded biases and an integration-by-parts identity that removes them one at a time.

The purpose of the algebraic truncation is now stated before the formula. It ties bounded biases to the tree estimate and the integration identity to the block-by-block derivative transfer.

**Why it matters:** A reader otherwise sees a complicated smooth function before knowing which two properties were selected.

**Advice:** Preserve this repaired motivation; the earlier complaint that the function arrives wholly unexplained no longer applies.

## LS131

**reasoning_record · low · consistency · fourier**

**Location:** §3.9: Gaussian-chain notation (source line 1040)

**Exact current phrase:**

> Write $\ell=k-1$.

This reuses ℓ, which denotes log₂m in the construction and growing-parameter argument, for the number of Gaussian links. The local definition is explicit, so there is no logical error, but a reader comparing the estimates must repeatedly undo the alias.

**Why it matters:** The review asks readers to compare k-dependent constants with logarithmic factors; this collision obscures that comparison.

**Advice:** Reserve a different local symbol for the number of links, or keep k−1 directly. Reconcile the same alias in Appendix D.

## LS132

**reasoning_record · keep · keep · fourier**

**Location:** §3.10: the three-block calculation (source line 1142)

**Exact current phrase:**

> The same index $b$ enters and leaves the middle block.

The worked calculation reveals the cancellation that the general induction needs: a same-coordinate repeated derivative vanishes, and the unremoved factor stays outside the function differentiated at the next step.

**Why it matters:** This is an example that teaches an actual proof transition, rather than merely substituting values into the final bound.

**Advice:** Keep the three-block calculation even if surrounding implementation commentary is shortened.

## LS133

**reasoning_record · keep · keep · fourier**

**Location:** §3.10: general path invariant (source line 1147)

**Exact current phrase:**

> all accumulated weights depend only on $U_0,\ldots,U_{j-1}$

The dependence invariant is the right justification for leaving earlier edge weights untouched in the next Gaussian integration step.

**Why it matters:** Without it, a skeptical reader could reasonably expect additional product-rule terms.

**Advice:** Retain this explicit dependency statement beside the induction rather than replacing it by a generic appeal to repetition.

## LS134

**reasoning_record · medium · missing_example · fourier**

**Location:** §3.11: contracted coefficient arrays (source line 1225)

**Exact current phrase:**

> where $c^q(J)=c(J\cup\{q\})$

The proof introduces a family of coefficient arrays, contracts it at an adaptively selected coordinate, and then performs induction on degree. This is the densest new interface in the Fourier argument and has no small worked example.

**Why it matters:** The reader has to understand why the lower-degree quantity remains in the same uniformly bounded class before the stopping argument is credible.

**Advice:** Work out the r=2 increment for a queried pair of coordinates, showing the old revealed set, the fresh centered factor and the contracted coefficients. This is an explanatory example, not a request for a new lemma.

**Source:** https://arxiv.org/html/2103.11604v2#S1.SS3

## LS135

**reasoning_record · keep · keep · fourier**

**Location:** §3.11: stopped process versus conditioning (source line 1230)

**Exact current phrase:**

> A fresh coordinate keeps its original conditional distribution under adaptive querying.

The proof justifies fresh-coordinate centering by an actual root-to-node cylinder event, then uses a stopped process. This avoids conditioning on a future good event, which can destroy the martingale property.

**Why it matters:** The same distinction between permissible transcript conditioning and impermissible event selection recurs in the planted lower bound; it is a useful conceptual connection.

**Advice:** Preserve the cylinder argument and the stopping construction. An optional cross-reference to §6.1 would help readers recognize the shared issue.

**Source:** https://arxiv.org/html/2103.11604v2#S1.SS3

## LS136

**reasoning_record · medium · underweighted · fourier**

**Location:** §3.12: reading the advantage estimate (source line 1349)

**Exact current phrase:**

> The numerical assembly in §3.15 uses (F33)

Immediately after (F33), the record routes the reader to constants without first extracting the reason for the exponent: the main term has d^(k/2) multiplied by m^−(k−1)/2. Balancing these powers is what produces m^(1−1/k).

**Why it matters:** The lower-bound specialist wants to see which part of the argument fixes the exponent before tracking small numerical factors.

**Advice:** Explain that power balance in one short paragraph before the finite arithmetic; keep the exact bound unchanged.

## LS137

**reasoning_record · keep · keep · fourier**

**Location:** §3.13–3.14: the off-promise bridge (source line 1428)

**Exact current phrase:**

> These estimates concern the two distributions fixed throughout the proof.

The record does not claim that the rounded law is supported on promised one-inputs. It combines its positive first moment and the uniform second moment with the pointwise acceptance inequalities in (F41).

**Why it matters:** This is the essential bridge from a distributional analytic comparison to a promise-problem lower bound.

**Advice:** Keep (F41), the case-by-case explanation, and the explanation of why constant error is too large. These deserve priority over optional constant refinements.

## LS138

**reasoning_record · low · teaching · fourier**

**Location:** §3.14: amplitude of the useful gap (source line 1470)

**Exact current phrase:**

> its positive-promise mass is bounded below only by a quantity exponentially small in $k$.

The subsection begins with a general majority bound before explaining locally why constant promise error is inadequate for this comparison. The preceding moment subsection already displays the small signal, and the actual repetition count is chosen later, after the motivation. A brief reminder at this entry would help readers arriving directly at the amplification subsection.

**Why it matters:** The role of amplification is to make the error small relative to the useful acceptance gap; that purpose can be recalled before the generic calculation without changing its order of mathematical choices.

**Advice:** Preview the required error scale relative to a_k before the generic majority calculation. Keep the actual choice of repetitions and the existing finite arithmetic in §3.15.

## LS139

**reasoning_record · medium · underweighted · fourier**

**Location:** §3.15: where the two powers of k arise (source line 1512)

**Exact current phrase:**

> We use the padded depth $d=50kD+1$

The explicit lower bound has a k² denominator, but the numerical assembly does not pause to identify its two sources: the degree-k derivative estimate already charges k, and the error reduction makes the tested depth proportional to kD.

**Why it matters:** This decomposition is more informative for the later growing-k schedule than the decimal-sized absolute denominator.

**Advice:** Collect these two losses in a short explanatory sentence near (F43), while retaining the precise arithmetic in the record.

## LS140

**reasoning_record · low · structure · fourier**

**Location:** §3.16 and §3.18: repeated source account (source line 1594)

**Exact current phrase:**

> The proof above combines a known Gaussian-chain architecture with a known decision-tree growth strategy.

The source allocation is now careful, but §§3.6, 3.16 and 3.18 repeat substantial parts of the same explanation of Bansal–Sinha, Girish–Tal–Wu and the optional SSW comparison.

**Why it matters:** The long record needs provenance at first use and a stable detailed comparison; repeated summaries make the proof feel as if it repeatedly restarts.

**Advice:** Keep the local theorem attribution and the detailed comparison in §3.16; make §3.18 a compact source-location index rather than a third narrative account.

## LS141

**reasoning_record · keep · keep · fourier**

**Location:** §3.17: the joined ingredient (source line 1619)

**Exact current phrase:**

> These three properties form the conjunction required in OpenAI's Lemma 2.1.

This closure checks that the quantum decoder, the exact circuit and the hardness estimate refer to the same promise, normalization and parameters. It also states when the accuracy parameter is chosen.

**Why it matters:** Separately correct ingredients would not suffice if they concerned different partial functions or incompatible thresholds.

**Advice:** Keep the common-witness and quantifier checks as the exit from the Forrelation chapter.

## LS142

**reasoning_record · medium · missing_example · certificates**

**Location:** §4.1: transcript lemma (source line 1660)

**Exact current phrase:**

> A transcript $\tau\in\{0,1\}^{S}$ proposes a value for every non-input gate.

The definition and induction are correct, but the first concrete circuit later has 180 gates. There is no intermediate view of one gate check showing which proposed bits are in the cell and which predecessor bit comes from the address input.

**Why it matters:** A reader can understand the abstract lemma yet still picture a transcript as a trusted computation rather than a set of untrusted input bits tested locally.

**Advice:** Use one already available gate from the finite example, or point to the two-gate XOR toy, to illustrate a single local check. The aim is to expose the coordinate roles, not add another full circuit.

## LS143

**reasoning_record · medium · underweighted · direct_product**

**Location:** §4.2: parameter r (source line 1687)

**Exact current phrase:**

> r=\lceil20\log_2m\rceil=40t=20\ell.

The numerical choice is introduced before its classical job is made local: enough independent answers must suppress all G prospective cell queries. The introduction gives an approximate hardness story, but the reader needs the specific reason that an address has logarithmically many bits rather than a fixed length.

**Why it matters:** Without that reason, 20 looks like a construction detail and the m^20 cell array looks arbitrary.

**Advice:** Add a short forward pointer to the G(2/3)^r term in §6.5–§6.6. Explain that the constant is slack; do not optimize it or change the family.

## LS144

**reasoning_record · low · teaching · separations**

**Location:** §4.2: input length (source line 1704)

**Exact current phrase:**

> so the input length is $O_k(m^{22}\ell^3)$, polynomial in $m$.

The new input-length calculation is valuable. Its punchline should also remind the reader why an enormous explicitly addressed input does not itself charge the quantum algorithm that many queries: it accesses selected coordinates and never initializes or reads the whole table.

**Why it matters:** A neighboring-area reader can otherwise confuse the size of the function with the cost of evaluating it in the query model.

**Advice:** Connect the length count to the already stated rule that computation and coordinate arithmetic are free. Keep the full count and the fixed-k qualifier.

**Prior-round relation:** The previously missing length calculation is fixed; this concerns its explanatory payoff.

## LS145

**reasoning_record · keep · keep · certificates**

**Location:** §4.2: semantic definition (source line 1751)

**Exact current phrase:**

> Totality and uniqueness follow from the semantic definition (4.5) alone;

This separation between the semantic function and the circuit-based verification is exact and useful. Totality is not being inferred from the behavior of an off-promise decoder.

**Why it matters:** It resolves the most common conceptual confusion in turning a partial-function ingredient into a total problem.

**Advice:** Keep this sentence beside the uniqueness proof and retain the domain guards in (4.5).

## LS146

**reasoning_record · medium · funnel · certificates**

**Location:** §4.3: four-column example (source line 1758)

**Exact current phrase:**

> we use a circuit synthesized from this finite truth table

The board is a genuine instance of the generic definition, but it changes both r and the circuit implementation. Later §6 changes P as well. The record now warns about each change, yet the purpose of using two different boards is still left to the reader.

**Why it matters:** Repeated local caveats do not by themselves tell a reader which mechanism each example isolates or which quantities can be compared across them.

**Advice:** Add a compact example crosswalk: Forrelation board for promise/domain certification and winner dominance; XOR board for planting and truncation. Reuse this map when shorter papers link into either example.

**Prior-round relation:** The round-six crosswalk note is present; the remaining issue is its placement and the absence of a single map of the two examples.

## LS147

**reasoning_record · low · unclear · certificates**

**Location:** §4.3: stored transcripts (source line 1809)

**Exact current phrase:**

> every cell of each column stores the column's two true transcripts

Here “true” means the true evaluation of the total Boolean circuit, including on an unpromised input. Earlier “true address” exists only on the promise. Using the same adjective for the two notions makes the unpromised column briefly look contradictory.

**Why it matters:** The example is supposed to teach exactly why a correct circuit transcript is not enough to certify membership in the promise.

**Advice:** Call these evaluated circuit transcripts at this point, and preserve the explanation that one has domain output zero.

## LS148

**reasoning_record · low · overweighted · separations**

**Location:** §4.4: local-test count (source line 1846)

**Exact current phrase:**

> \leq(42+20A)m\ell^3.

The explicit loose coefficient receives an inequality and a paragraph of arithmetic just before the essential equivalence lemma. For the lower-bound route, circuit size and K do not enter at all; for the upper-bound route, the growth rate and provenance of the eventual explicit constant are the useful facts.

**Why it matters:** The construction-specific semantic equivalence is visually delayed by a routine estimate.

**Advice:** Move the loose constant accounting after the equivalence or mark it as the explicit-budget calculation. Keep it available to the complete-proof route.

## LS149

**reasoning_record · low · evidence_presentation · certificates**

**Location:** §4.4: finite checker report (source line 1894)

**Exact current phrase:**

> all these checks pass.

The sentence sounds like a current execution result, but this paragraph reports a preserved round-three checker output. The later prose does distinguish finite checks from general proofs; it should also make the time and source of the execution clear at the point of the claim.

**Why it matters:** The reader should not have to infer whether the present draft re-ran the board and mutation checks.

**Advice:** Use the recorded output as a dated example receipt and link it once; keep the mathematical examples in the body and execution details in the appropriate appendix. No re-verification is requested.

## LS150

**reasoning_record · keep · keep · certificates**

**Location:** §4.4: example isolating the domain test (source line 1896)

**Exact current phrase:**

> A second board in the output isolates the domain test.

This second board is more diagnostic than merely observing that column 2 loses on the first board, where its zero and incoming pointers already disqualify it. Here the domain-output test is the only failed requirement.

**Why it matters:** It shows necessity of the domain test instead of merely compatibility with it.

**Advice:** Keep this isolated counterexample and its exact relationship to the generic local-test lemma.

## LS151

**reasoning_record · keep · keep · certificates**

**Location:** §4.5: pointer support (source line 1907)

**Exact current phrase:**

> the support is exactly $m+\ell$

The distinction between adaptive depth and total relevant coordinates is correct. The remark is now correctly marked and excluded from the first construction route.

**Why it matters:** It blocks a false interpretation of a logarithmic-depth pointer test as depending on only logarithmically many fixed physical bits.

**Advice:** Keep the diagnostic as a remark with its formal-statement destination; do not promote it back into the main argument.

**Prior-round relation:** The round-six relocation and labeling are effective.

## LS152

**reasoning_record · keep · keep · certificates**

**Location:** §4.7: arbitrary rival behavior (source line 1981)

**Exact current phrase:**

> The event inclusion uses only the winner's decoder,

This is the exact comparison invariant that makes outward pointers useful. It is stronger and cleaner than assuming the rival decoder is correct or independent.

**Why it matters:** It explains how the total function can contain arbitrary off-promise losing columns without invalidating the quantum tournament.

**Advice:** Preserve the event inclusion and the explicit freedom of the joint decoder law.

## LS153

**reasoning_record · medium · underweighted · separations**

**Location:** §4.8: direct pointers and earlier alphabets (source line 1992)

**Exact current phrase:**

> Here every pointer bit is a Boolean input coordinate,

The historical comparison is accurate but its resolution is compressed. The earlier objection was to treating the entire outgoing collection as one alphabet symbol; the present routine accesses one selected pointer field, paying for its bits. Merely saying that the bits are Boolean coordinates does not quite articulate why that avoids the earlier algorithmic cost.

**Why it matters:** A pointer-functions reader recognizes the old obstacle and wants to see the changed access pattern, not just a change of encoding.

**Advice:** Tie this sentence directly to the selective pointer lookup of §4.4 and the total input-length count of §4.2. No new comparison theorem is needed.

**Source:** https://arxiv.org/pdf/1506.04719v3#page=6

## LS154

**reasoning_record · medium · prose · fourier**

**Location:** §5.1: internal claim labels in reading prose (source line 2040)

**Exact current phrase:**

> the state and success formula in `claim-grover-state`

Machine identifiers still appear in ordinary proof sentences throughout the quantum chapter, despite the relocation of most formal apparatus to Appendix G. This example names a claim by an internal key instead of a readable equation or assertion.

**Why it matters:** A reader following the mathematical derivation gains nothing from remembering the export key and is pulled back into maintenance vocabulary.

**Advice:** Use readable local references in rendered prose; retain the identifiers in source markers and correspondence files. Treat the repeated instances as one editorial repair.

## LS155

**reasoning_record · high · funnel · fourier**

**Location:** §5.2: return instruction (source line 2198)

**Exact current phrase:**

> Return to the [specialist companion](expert_companion.md), §4.2.

The current companion’s tournament is §3.2. Its §4.2 is the planted input construction. The link opens the right document, but the visible destination tells the reader to return to a different argument.

**Why it matters:** This breaks the specific short-to-long-to-short reading route the record promises.

**Advice:** Correct the return label to the current tournament section and inspect every analogous numeric return label after the restructuring.

## LS156

**reasoning_record · medium · evidence_presentation · fourier**

**Location:** §5.2: what the compiled label theorem follows from (source line 2359)

**Exact current phrase:**

> It follows from the phase-independent successful-state assertion by measuring the label.

As an ordinary mathematical implication this is correct. Because the preceding paragraph calls it the compiled version, however, the sentence can also be read as claiming that the physical label-law theorem is derived from the complete physical-state theorem. Appendix G.7 explicitly distinguishes those formal routes and the remaining general-projector bridge.

**Why it matters:** The reader should not confuse a mathematical implication with the dependency route actually supporting the implemented algorithm.

**Advice:** State which sense of “follows” is intended and route formal dependency details to G.7; no further formalization is requested.

## LS157

**reasoning_record · keep · keep · fourier**

**Location:** §5.2: exact coupling (source line 2365)

**Exact current phrase:**

> The independence belongs to the construction of the coupling from that law

This explains why the coupling may use an independent Bernoulli failure variable even when the physical sampler’s behavior depends on the full history. The output law is sufficient to construct the coupling.

**Why it matters:** Without this sentence, the proof could appear to assume history-independent sampling failures.

**Advice:** Retain the law-based coupling and the point at which charging stops after the winner is listed.

## LS158

**reasoning_record · keep · keep · fourier**

**Location:** §5.3: fresh verification (source line 2431)

**Exact current phrase:**

> Decoding, comparison, and verification

The section verifies candidates after decoding afresh and uses the fact that every address of a nonwinner has a failed local test. Correctness therefore survives arbitrary outputs of an off-promise decoder.

**Why it matters:** A lower-bound reader might otherwise assume the upper algorithm depends on all decoded addresses being meaningful.

**Advice:** Keep the per-address soundness explanation and separate zero-input and one-input error accounting.

## LS159

**reasoning_record · keep · keep · fourier**

**Location:** §5.4: detailed query accounting (source line 2545)

**Exact current phrase:**

> Coherent access and the query cap

This is the appropriate long destination for the detailed coherent-access and integer-budget accounting. It explains why reading a pointer field, reversing work and padding branches remain ordinary bit queries.

**Why it matters:** These implementation costs justify the model of the separation, while their complete arithmetic is disproportionate in the short companion.

**Advice:** Retain this destination when compressing the companion’s count, with a precise return link.

## LS160

**reasoning_record · keep · keep · direct_product**

**Location:** §6: generic lower bound (source line 2655)

**Exact current phrase:**

> The argument gives a generic bound.

Opening with the generic P,C,L statement makes the classical mechanism legible without carrying the Forrelation analysis. In particular, the independence of the bound from circuit size belongs here.

**Why it matters:** The reader can see that the exponent loss enters through the chosen hard partial function, not through the planting reduction.

**Advice:** Keep this opening. Give the no-circuit-size restriction the same prominence as the L<R(P) hypothesis.

## LS161

**reasoning_record · high · funnel · direct_product**

**Location:** §6: entry and §6.6 return instructions (source line 2668)

**Exact current phrase:**

> return to its §5.

The current companion’s classical proof is §4, not §5. The later instruction at the beginning of record §6.6 likewise says to return to companion §5.5, which does not exist; the intended destination is §4.5.

**Why it matters:** These are broken reading instructions even though the links to the companion file resolve.

**Advice:** Correct both prose destinations, ideally using stable named anchors and visible topic names. Include prose cross-references in the revision check.

**Prior-round relation:** New stale references left after companion renumbering.

## LS162

**reasoning_record · medium · structure · direct_product**

**Location:** §6: order of the proof (source line 2668)

**Exact current phrase:**

> We begin in §6.1 with the direct product that the simulator uses.

The first route is now signposted, but a continuous reader still traverses a lemma, two proofs, a cap corollary, an adaptive example, a normalization identity and a literature comparison before seeing the hard distribution. This is a particularly large prelude for the standard ingredient rather than the construction-specific reduction.

**Why it matters:** The reader’s mental model of the dummy input and the simulator has to survive hundreds of lines before either is defined.

**Advice:** Make the skip destination explicit in this sentence, and give the two-line simulator interface immediately beside the lemma statement. Keep the full proofs in the record; this is a reading-order request.

**Prior-round relation:** The purpose sentence for the second proof is fixed; this is the residual first-pass ordering cost.

## LS163

**reasoning_record · keep · keep · direct_product**

**Location:** §6.1: statement of Lemma 4.1 (source line 2702)

**Exact current phrase:**

> the posteriors met during the algorithm may be easier;

The one-input hardness assumption is correctly attached to the original law, while the proof uses an optimal continuation value under each posterior. This sentence prevents the false argument that each conditional answer is still at most β predictable.

**Why it matters:** Without it, a familiar-looking product bound is easy to justify for the wrong reason.

**Advice:** Keep it directly after the statement and preserve the remaining-query allowance in V_h.

## LS164

**reasoning_record · keep · keep · direct_product**

**Location:** §6.1: product-law proof (source line 2743)

**Exact current phrase:**

> The bits within one input may be arbitrarily
> dependent.

This small sentence correctly states the scope of the independence used. The product is across complete instances, not across their bits, and μ from minimax need not have any coordinate product structure.

**Why it matters:** It prevents an incorrect transfer from simple fair-bit examples to the hard Forrelation law.

**Advice:** Keep this explicit distinction when shortening the proof.

## LS165

**reasoning_record · keep · keep · direct_product**

**Location:** §6.1: supermartingale step (source line 2818)

**Exact current phrase:**

> at each step only the queried factor can change,

The proof identifies the actual reason that the product has nonincreasing expectation. Separate supermartingale inequalities for the factors would not be enough.

**Why it matters:** This is the central adaptivity argument and should survive any register-based compression.

**Advice:** Preserve the sentence and the connection to the transcript rectangle law.

## LS166

**reasoning_record · keep · keep · direct_product**

**Location:** §6.1: independent side information (source line 2868)

**Exact current phrase:**

> independence from each input separately is too weak.

The parity-side-information example is short, exact and directly exposes the needed joint independence. It is more informative than a general warning about correlated side data.

**Why it matters:** It makes the simulator’s allowed free information testable rather than verbal.

**Advice:** Keep the example and link back to it when declaring the simulator’s side information.

## LS167

**reasoning_record · low · teaching · direct_product**

**Location:** §6.1: adaptive example (source line 2922)

**Exact current phrase:**

> and, if $a\neq t$, queries $A_0$

The third query is deliberately useless; its only job is to select the cap event. That purpose is understandable after the calculation but not before the algorithm is described.

**Why it matters:** A reader initially looks for an algorithmic advantage from the adaptivity and can mistake the toy for a poor example of efficient computation.

**Advice:** Say up front that this is an artificial counterexample to conditioning, using a redundant query to mark which runs violate the cap. Preserve the exact calculation.

## LS168

**reasoning_record · medium · figure · direct_product**

**Location:** §6.1: adaptive example (source line 2950)

**Exact current phrase:**

> The cap event selects a union of rectangles,

This is the conceptual payoff of the example, but the table only lists histories. A reader must mentally reconstruct how the union creates dependence even though each history separately preserves the product law.

**Why it matters:** The most delicate distinction is geometric: one transcript rectangle versus a union selected by the eventual query count.

**Advice:** A small 4-by-4 grid of the already listed A,B inputs, marking the cap event and successful outputs, would make that distinction visible. Use the same existing example, without adding another construction.

## LS169

**reasoning_record · keep · keep · direct_product**

**Location:** §6.1: budgets in the adaptive example (source line 2957)

**Exact current phrase:**

> a total budget $L=1$ implies the separate caps

This qualification is important. The counterexample rules out replacing separate L-caps by total rL, while the actual simulator has the stricter total L-cap.

**Why it matters:** It avoids turning a useful warning about pooled budgets into an incorrect objection to the simulator or to Drucker’s alternative theorem.

**Advice:** Keep both total-budget comparisons together, as the current text does.

## LS170

**reasoning_record · keep · keep · direct_product**

**Location:** §6.1: second proof (source line 2963)

**Exact current phrase:**

> the identity (6.11) at its end shows that the two proofs compute the same quantity.

The added purpose sentence repairs the previous unexplained duplication. The normalized and unnormalized presentations are now visibly related, with zero-mass histories handled differently.

**Why it matters:** It gives a reader a reason to choose or compare the two proofs.

**Advice:** Keep this sentence and the normalization identity; retain the second proof off the default construction route.

**Prior-round relation:** Successful round-six repair of CX005.

## LS171

**reasoning_record · low · unclear · direct_product**

**Location:** §6.1: Drucker substitution (source line 3086)

**Exact current phrase:**

> $k=r$ and $\alpha=3/r\le3/40$

The symbol k has denoted the Forrelation order throughout the record, but here it is Drucker’s number of instances and is set equal to r. The substitution is correct, yet the source notation collides at exactly the point where the reader compares dependence on k.

**Why it matters:** It can make a specialist momentarily think the proof is imposing an equation between the two construction parameters.

**Advice:** Label this as Drucker’s k, or use a source-symbol column in a tiny substitution table. Keep the global-budget alternative and the factor-two calculation.

**Source:** https://arxiv.org/abs/1005.0644v2

## LS172

**reasoning_record · low · structure · certificates**

**Location:** §6.2: return to the construction (source line 3108)

**Exact current phrase:**

> Recall the setting.

The long reset is justified after the direct-product prelude, but it repeats almost the entire layout of §4.2. A standalone entrant needs the random variables and the roles of the three fields, not another prose definition of every block.

**Why it matters:** The repeated setup makes the lower-bound chapter feel longer without sharpening which fields are random, fixed or supplied free to the simulator.

**Advice:** Make the reset a compact construction/data-role recap and point back for the full winning predicate. Preserve its usefulness as an independent entry point.

## LS173

**reasoning_record · keep · keep · fourier**

**Location:** §6.2: minimax law (source line 3142)

**Exact current phrase:**

> the hard measure used in the analytic proof of Forrelation hardness plays no role in it.

This distinction is indispensable. The simulator needs a product of promised-input samples from a minimax hard law, while the analytic Forrelation comparison uses distributions that can place mass outside the promise.

**Why it matters:** Conflating those two laws would break the planting construction, even though both are reasonably called hard distributions.

**Advice:** Keep the sentence, and use visibly distinct names in any figure or compressed summary.

## LS174

**reasoning_record · medium · figure · direct_product**

**Location:** §6.3: sampling the dummy input (source line 3192)

**Exact current phrase:**

> Independently, we draw every \(A_{i,h}\) from \(\mu\)

All the independence is present in prose, but the record lacks one compact sampling diagram or table showing the J variables, all A inputs, fixed blank cells and the independently chosen I. The later simulator discussion depends on grouping exactly these variables.

**Why it matters:** The reader has to reconstruct the probability space repeatedly when checking the erased-zero and address-guess arguments.

**Advice:** Add a data-dependency table for the existing experiment, including which variables are known to a target-column simulator. Do not depict true addresses or planted transcripts as independent random samples.

## LS175

**reasoning_record · keep · keep · certificates**

**Location:** §6.3: blank certificate cells (source line 3192)

**Exact current phrase:**

> so the blank cells reveal neither a zero location nor any value of \(P\).

The blank cells are not just a convenient zero-input. Their independence is what makes outside queries free in the address predictor without leaking the target answers.

**Why it matters:** It distinguishes this distribution from one filled with valid certificates or pointers, which could reveal the hidden structure.

**Advice:** Keep this explanatory clause and preserve the fact that the simulator runs the dummy input, never the planted one.

## LS176

**reasoning_record · medium · funnel · certificates**

**Location:** §6.3: XOR toy indexing (source line 3213)

**Exact current phrase:**

> Rows and columns carry zero-based labels in this example.

The switch from the one-based Forrelation board in §4 to zero-based labels in this toy is an avoidable extra change on top of changing P and r. The crosswalk later tells the reader about it, but the same symbol for column 1 now names a different displayed position.

**Why it matters:** A reader following the exposition into the record spends effort translating labels instead of tracing the capped simulation.

**Advice:** Use one display convention across the mathematical examples, or print an explicit label map with the toy. Source-code indexing can remain separately documented.

**Prior-round relation:** The round-six warning is present; this concerns the remaining translation cost, not an absent disclaimer.

## LS177

**reasoning_record · keep · keep · certificates**

**Location:** §6.3: XOR toy scope (source line 3226)

**Exact current phrase:**

> it is neither a Forrelation instance nor a choice satisfying

The toy’s scope is explicit: it demonstrates the generic construction and later truncation, not an asymptotic hard family. This prevents an apparently tiny example from being treated as evidence of the separation exponent.

**Why it matters:** The actual parameter choices make G very small at small m, so an unqualified toy would be misleading.

**Advice:** Keep this boundary while improving the cross-example map.

## LS178

**reasoning_record · keep · keep · direct_product**

**Location:** §6.3: first difference (source line 3245)

**Exact current phrase:**

> some planted bits can equal their blank values

Counting every visit to the selected cell is a safe overcount. The proof does not assume that every bit of a planted certificate differs from the blank pattern.

**Why it matters:** It prevents a silent equality between reaching the cell and observing a distinguishing bit.

**Advice:** Keep this parenthesis beside (18), including in shorter summaries.

## LS179

**reasoning_record · low · unclear · direct_product**

**Location:** §6.4: discovery count (source line 3252)

**Exact current phrase:**

> Let \(Z\) count the columns whose unique zero is queried

Z was the product of continuation values in §6.1 and is now a count of discovered columns. The scopes are mathematically clear, but both objects are averaged inside the same chapter and both feed the final probability estimate.

**Why it matters:** A reader jumping between the direct product and erased-zero arguments can misread which expectation is meant.

**Advice:** Use a distinguishing subscript in explanatory summaries, or flag the local reuse of notation once. There is no need to rename preprint-numbered claims.

## LS180

**reasoning_record · keep · keep · direct_product**

**Location:** §6.4: independence control (source line 3270)

**Exact current phrase:**

> Symmetry under column permutations still gives

The selection example isolates uniform marginal probability from independence of the selected column and the run. Its 175/256 versus 1/4 comparison is a concrete, memorable failure mode.

**Why it matters:** It explains why the equality in (19) needs the full sampling construction, not just a uniform I.

**Advice:** Preserve the example and its statement that only the altered selection rule is a counterexample.

## LS181

**reasoning_record · low · prose · direct_product**

**Location:** §6.4: optional refinement (source line 3360)

**Exact current phrase:**

> The baseline contains one further refinement,

“The baseline” is an internal project referent. It does not tell a mathematical reader whose argument this is or why it belongs in the record.

**Why it matters:** The sentence abruptly moves from proof exposition into workflow history.

**Advice:** Identify the refinement by its mathematical purpose and leave its archival provenance to Appendix F or the source notes.

## LS182

**reasoning_record · keep · keep · direct_product**

**Location:** §6.5: heavy columns (source line 3388)

**Exact current phrase:**

> The threshold bounds the total number of queries to all \(r\) strings of a column,

This is the right budget to charge. Heavy columns consume more than L address-input queries in total; the direct-product lemma then applies because the capped simulator’s total L budget implies every per-instance cap.

**Why it matters:** Confusing the threshold with rL would lose the classical mL lower bound.

**Advice:** Keep the sentence next to (20), and preserve all three budget levels in compressed versions.

## LS183

**reasoning_record · medium · teaching · direct_product**

**Location:** §6.5: simulator side information (source line 3393)

**Exact current phrase:**

> every \(J_j\), all the \(A\)-strings of the other columns, and the fixed blank cells

The list is correct, but the surprising member is J_i itself: the simulator is allowed to know the target column’s zero even though the original algorithm is trying to discover hidden structure. This does not help it compute s_i because J_i is independent of the target A tuple.

**Why it matters:** A specialist checking the reduction may pause over whether free information has accidentally solved part of the target task.

**Advice:** Add the reason this apparently generous information is harmless: the predictor’s target is the vector of P-values, not the erased zero. Keep the target strings, address and transcripts excluded.

## LS184

**reasoning_record · keep · keep · direct_product**

**Location:** §6.5: extracting the guessed address (source line 3395)

**Exact current phrase:**

> without a query to the cell's contents.

This is the decisive reduction step. The coordinate of a prospective cell query already encodes the whole address, so the simulator stops before observing any planted content.

**Why it matters:** It turns a search event into a vector-answer predictor without assuming the algorithm explicitly computes that vector.

**Advice:** Keep this sentence and the time-four row of the toy simulator; give them visual priority over routine constant arithmetic.

## LS185

**reasoning_record · low · structure · direct_product**

**Location:** §6.5: two conditioning examples (source line 3448)

**Exact current phrase:**

> The distinction in (21) between the joint event and success conditional on nonheaviness

This is the second explicit counterexample to conditioning on a cap event in the same chapter. The first uses two AND instances and a redundant query; this one uses one promised AND instance and mirrors the simulator more directly. Their different teaching jobs are not announced.

**Why it matters:** A continuous reader can feel that the same warning is being proved twice without knowing which example to retain mentally.

**Advice:** State the distinction in purpose: the first exhibits loss of a product law under a union of transcript rectangles; this one isolates the actual nonheavy event. Link them rather than treating the second as a fresh surprise.

## LS186

**reasoning_record · keep · keep · direct_product**

**Location:** §6.5: union bound and random target (source line 3462)

**Exact current phrase:**

> The factor \(m\) cancels,

The average over the independent selected column, rather than a union over all columns, is exactly where an unnecessary factor m is avoided. This is correctly made explicit.

**Why it matters:** The exponent bookkeeping depends on preserving this averaging step.

**Advice:** Keep the explanation, including the distinction between the time union and the column average.

## LS187

**reasoning_record · medium · prose · direct_product**

**Location:** §6.6: evidence aside in discrepancy assembly (source line 3484)

**Exact current phrase:**

> In the Lean development an older core theorem proves

The main discrepancy calculation is interrupted by the history of core and Paper wrappers. G.8 already explains signed versus absolute endpoints and their proof routes.

**Why it matters:** The reader is trying to check a three-term bound, but is sent into declaration genealogy before the numerical contradiction.

**Advice:** Keep the absolute-value inequality in the body and move or reduce this implementation-history paragraph to its G.8 destination.

**Prior-round relation:** Residual evidence prose after the round-six move to Appendix G; the move itself is acknowledged as successful.

## LS188

**reasoning_record · low · structure · direct_product**

**Location:** §6.6: tail and finite contradiction (source line 3490)

**Exact current phrase:**

> the paper's exact logarithmic tail:

The asymptotic o(1) calculation comes before the simpler finite m^-10 estimate that actually proves the stated generic theorem for every allowed m. Both are correct, but their order briefly suggests an extra large-m hypothesis is being introduced.

**Why it matters:** The reader has to wait to learn that the construction reduction itself needs no new threshold once 1≤L≤m.

**Advice:** Lead with the finite estimate used for the contradiction and present the preprint’s exact tail as a comparison or recovery note. Preserve the numbered source claim.

## LS189

**reasoning_record · medium · underweighted · fourier**

**Location:** §6.6: where the exponent is lost (source line 3544)

**Exact current phrase:**

> This comparison identifies the literature input and the strength we use.

The lower-bound chapter gives every ingredient but never collects the losses in one place: the planting reduction preserves mL; the address length is chosen to defeat the time union; the two floors lose only constants; the deliberately weaker Forrelation L supplies the displayed logarithmic denominator.

**Why it matters:** This is the exact accounting a separations reader wants when judging where exponent four is won or lost.

**Advice:** Add a compact loss ledger referring to the existing inequalities. Do not derive a stronger bound; simply classify each existing loss as constant, logarithmic or a power of m.

## LS190

**reasoning_record · keep · keep · direct_product**

**Location:** §6.6: floor arithmetic (source line 3577)

**Exact current phrase:**

> Both floors are bounded in the direction a lower bound needs.

The record gives an actual range t≥8, checks positivity before applying the floor estimate, and uses the same circuit as the upper bound. This is more useful than a vague “absorb the floors into constants”.

**Why it matters:** It keeps the numerical endpoint and the same-family quantifiers auditable.

**Advice:** Preserve the proof, while keeping it visually subordinate to the simulator and budget accounting.

## LS191

**reasoning_record · low · overweighted · separations**

**Location:** §7: repetition of the parameter argument (source line 3606)

**Exact current phrase:**

> We now combine the two bounds for the same functions and compute the infimum.

Section 1 already gives the full ratio inequality and its limiting argument. Section 7 then restates the definition, the theorem, the same-function requirement, the floor conversion and the ratio. The complete proof belongs here, but the opening currently duplicates much of it.

**Why it matters:** The reader encounters the easy endpoint at greater length than the difficult reduction that earns it.

**Advice:** Choose one location for the full parameter argument; let the other state the idea and point to it. Preserve the explicit order of quantifiers in at least one visible display.

## LS192

**reasoning_record · keep · keep · separations**

**Location:** §7.1: strict exponent threshold (source line 3676)

**Exact current phrase:**

> At \(\alpha=4-2/k\) the power gap

The strictness is correctly explained. For fixed k the ratio method excludes powers below 4−2/k; the endpoint does not follow because of the logarithmic denominator.

**Why it matters:** This is the precision the exposition needs when describing k=2 and the cubic threshold.

**Advice:** Keep this sentence as the canonical wording for the derived accounts.

## LS193

**reasoning_record · medium · underweighted · separations**

**Location:** §7.3: choosing the growing parameter (source line 3730)

**Exact current phrase:**

> We now choose $k=\lfloor\sqrt{t/20}\rfloor$

The schedule appears as a choice before the reader sees why that scale is natural. The later expression 40k+ℓ/k contains the competing losses: increasing k reduces the 1/k classical loss but increases the exponential-in-k quantum prefactor.

**Why it matters:** The long numerical derivation can look like an arbitrary successful substitution instead of a readable balance of the existing estimates.

**Advice:** Motivate the schedule using those two terms before substituting it. Keep the current proved schedule and constants; no optimization or stronger theorem is requested.

## LS194

**reasoning_record · low · prose · separations**

**Location:** §7.3: choice of displayed epsilon constant (source line 3748)

**Exact current phrase:**

> The chain gives the constant $474$; we state $508$,

This explains an editorial synchronization choice with the companion, rather than a mathematical necessity. The record is supposed to be the source from which the shorter account is derived; citing the shorter account as the reason for the constant reverses that direction.

**Why it matters:** The reader sees revision history inside an otherwise self-contained inequality chain.

**Advice:** Describe 508 simply as a convenient conservative bound in the mathematical text, and record the cross-document synchronization outside it. Keep the agreed value if that is the chosen presentation.

## LS195

**reasoning_record · low · teaching · separations**

**Location:** §7.3: initial range of the growing-k estimate (source line 3749)

**Exact current phrase:**

> when $\varepsilon(\ell)\ge4$ the inequality below holds trivially.

This is correct, and it reveals that t≥80 is a validity threshold, not the point at which the displayed exponent gives a useful positive separation. The distinction is easy to miss because the final theorem-like display emphasizes “for every t≥80”.

**Why it matters:** An explicit constant-heavy estimate can appear quantitatively stronger than its first admissible values warrant.

**Advice:** Say that the interest of this schedule is the asymptotic approach of the exponent to four. Do not add another numerical threshold unless it serves a reader need.

## LS196

**reasoning_record · keep · keep · separations**

**Location:** §7.3: endpoint limitation (source line 3753)

**Exact current phrase:**

> although the argument gives no bound $R=\Omega(Q^4)$ for this family.

The new uniform schedule is distinguished from an exact fourth-power lower bound. That distinction must survive even though all three formulations have “quartic” in their informal description.

**Why it matters:** It prevents an asymptotic exponent statement from being promoted to a constant-factor relation.

**Advice:** Keep this limitation attached to the growing-k conclusion and mirror it in any summary.

## LS197

**reasoning_record · low · overweighted · fourier**

**Location:** Appendix A.2: correction history inside the proof (source line 3920)

**Exact current phrase:**

> A separate older annex transcription inserted an extra square root around the entire denominator.

The local adversary-prefactor comparison earns its place because it checks a specific mathematical statement. The older annex transcription story is a separate maintenance event and interrupts that comparison.

**Why it matters:** A reader needs the correct coefficient, the counterexample’s scope and the cited edition, not the history of an unrelated transcription.

**Advice:** Move the transcription history to Appendix F and leave the mathematical discrepancy and its precise limits here.

## LS198

**reasoning_record · keep · keep · fourier**

**Location:** Appendix A.4: signed-cube argument (source line 3952)

**Exact current phrase:**

> A maximum-degree face and Huang's signed cube

The proof uses an actual restriction on a maximum-degree support, preserves its coefficient, and identifies a parity-agreement set of more than half the face. The eigenspace intersection then gives the required sensitivity witness.

**Why it matters:** This is the conceptual center of the universal quartic bound; replacing it by a chain of named inequalities would remove the explanation.

**Advice:** Keep the face restriction and dimension argument together, with the surrounding constant discussion secondary.

## LS199

**reasoning_record · keep · keep · fourier**

**Location:** Appendix A.5: common sensitive-block input (source line 4013)

**Exact current phrase:**

> at that original \(x\)

The proof explicitly puts every sensitive block at the same original input, even though the algorithm proceeds through successive restrictions.

**Why it matters:** Block sensitivity is defined at one input; merely producing a block sensitive somewhere at each round would not prove the product bound.

**Advice:** Preserve this sentence and the disjoint-support argument when tightening the proof.

## LS200

**reasoning_record · low · prose · direct_product**

**Location:** Appendix B.7: displayed catalogue prose (source line 4944)

**Exact current phrase:**

> E[prod_j V_j(tau') | tau] <= prod_j V_j(tau).

The catalogue’s machine-style expressions are harder to read than the mathematical displays they index. This particular entry compresses a product, a conditional expectation and a transcript update into plain text.

**Why it matters:** The reference destination makes the reader reconstruct notation at precisely the moment they want a quick statement check.

**Advice:** Offer readable mathematical rendering next to the stable claim identifier, while retaining the exact ledger payload in its machine-readable file. Do not silently change a hashed statement.

## LS201

**reasoning_record · medium · consistency · direct_product**

**Location:** Appendix B.8: introductory cross-reference (source line 5000)

**Exact current phrase:**

> Sections 6.2–6.7 prove the planted lower bound.

There is no §6.7 in the current record. The former formal-scope section was moved to G.8; the proof now ends in §6.6.

**Why it matters:** A catalogue that is meant to be the stable navigation destination should not refer to a vanished section.

**Advice:** Change the range to the current proof sections and link formal scope separately to G.8.

**Prior-round relation:** Stale catalogue prose after the evidence-appendix move.

## LS202

**reasoning_record · medium · consistency · direct_product**

**Location:** Appendix B.8: generic theorem row (source line 5236)

**Exact current phrase:**

> Let P be a partial function on km bits

The body’s generic theorem permits a partial function on any finite coordinate set; this catalogue row specializes to km bits without specifying k in its local assumptions. It is narrower and less self-contained than the statement it is indexing.

**Why it matters:** A reader looking up the generic reduction cannot tell whether the dependence on the Forrelation block size is essential.

**Advice:** Align the catalogue’s quantified input dimension with the existing body statement, or explicitly label this as a specialized historical corpus row. This is a presentation correction, not a request for another theorem.

## LS203

**reasoning_record · high · consistency · separations**

**Location:** Appendix B.9: introduction (source line 5244)

**Exact current phrase:**

> no joint growing-$k$ schedule is inferred.

As a statement about all of Section 7 this is stale: §7.3 now derives a growing-k schedule from uniform estimates. The fixed-k bounds alone still do not justify substitution, but the catalogue paragraph does not make that restricted scope explicit.

**Why it matters:** The catalogue contradicts the new result a reader may have arrived to locate.

**Advice:** Restrict the warning to the fixed-k argument of §§7.1–7.2, and point to the separate existing uniform-estimate derivation in §7.3.

**Prior-round relation:** Incomplete propagation of the accepted round-six growing-k addition.

## LS204

**reasoning_record · low · credit · separations**

**Location:** Appendix C: BSS2003 (source line 5652)

**Exact current phrase:**

> Quantum decision trees and semidefinite programming

The entry combines the 2003 CCC metadata and DOI with the title of the May 2002 manuscript. The institutional record for the 2003 proceedings article gives “Quantum query complexity and semi-definite programming”. The difference is an edition/title issue, not a mathematical correction.

**Why it matters:** This appendix promises exact inspected editions; mixing the manuscript title with proceedings metadata weakens that promise.

**Advice:** Use the proceedings title for the 2003 DOI, or identify the 2002 manuscript separately. The original full text was not a proof source for this review.

**Source:** https://www.researchwithrutgers.org/en/publications/quantum-query-complexity-and-semi-definite-programming/

## LS205

**reasoning_record · low · unclear · fourier**

**Location:** Appendix D: earlier threshold notation (source line 5715)

**Exact current phrase:**

> Fix integers $k=\ell+1\ge2$

Throughout the main construction ℓ means log₂m=2t; here it is reset to k−1. The definition is explicit, so there is no logical problem, but it makes comparison with the current threshold and growing-k estimate needlessly hazardous.

**Why it matters:** A reader may carry the dominant notation into a historical appendix whose purpose is comparison.

**Advice:** Use a visibly local auxiliary letter or warn at the opening that this appendix’s ℓ is unrelated to the construction’s bit length.

## LS206

**reasoning_record · keep · keep · fourier**

**Location:** Appendix E: Bansal–Sinha comparison (source line 5820)

**Exact current phrase:**

> it neither constructs an algorithm nor disproves Bansal and Sinha's theorem.

The scope of the version-specific calculation is carefully bounded. A failed comparison of two upper-bound expressions is not a counterexample to the source theorem, and the record says so.

**Why it matters:** It lets a reader assess a local source criticism without implying a research-level refutation.

**Advice:** Preserve the version, displayed-step locator and explicit non-refutation boundary.

## LS207

**reasoning_record · low · prose · fourier**

**Location:** Appendix E: SSW author attribution (source line 5849)

**Exact current phrase:**

> **Pei Wu**

The boldface author name reads as a correction to a previous draft. Correct attribution matters, but the current mathematical reader has no reason to infer that there was a competing identity.

**Why it matters:** Editorial emphasis interrupts a source comparison and makes an ordinary author credit look adversarial.

**Advice:** Use normal author typography; keep the full correct name and the version-specific theorem locators.

## LS208

**reasoning_record · keep · keep · fourier**

**Location:** Appendix E: SSW transfer (source line 5906)

**Exact current phrase:**

> The only external mathematical input to (F60), beyond the proof above, is (F56).

This states precisely what is transferred: a decision-tree Fourier-growth theorem, not the random-orthogonal or rorrelation distribution theorem. It also leaves the absolute constant unspecified.

**Why it matters:** It avoids conflating a stronger analytic tool with an automatically stronger theorem for a different promise.

**Advice:** Keep the source/transfer boundary and the fact that the main explicit proof does not require this comparison route.

## LS209

**reasoning_record · medium · evidence_presentation · direct_product**

**Location:** Appendix F.5: historical status (source line 5966)

**Exact current phrase:**

> no exact-declaration
> Comparator pass is supplied for these helpers.

Inside a history appendix this can be true of the frozen return, but the nearby “current integration” wording obscures the date and the set of helpers. G.8 now names a later realized-caps endpoint accepted by Comparator. The reader should not have to infer which sentence belongs to which snapshot.

**Why it matters:** The status trail risks appearing contradictory even when every historical observation is accurate.

**Advice:** Attach a date/snapshot to each historical status paragraph and name the helper set being described. Keep current status in G.4 and do not promote one declaration’s result to another.

**Prior-round relation:** The broad round-six tense repair was made in F.1; this local present-tense ambiguity remains in F.5.

## LS210

**reasoning_record · low · unclear · separations**

**Location:** Appendix F.6: displaced referent (source line 5981)

**Exact current phrase:**

> contains the names listed above

After moving the formal declaration discussion to Appendix G, “the names listed above” has no obvious local referent in the exponent-history subsection.

**Why it matters:** A reader cannot tell which declarations the historical audit sentence covers without searching several different sections.

**Advice:** Name the relevant list or link to its exact current location, keeping the historical scope of the receipt unchanged.

## LS211

**reasoning_record · keep · keep · fourier**

**Location:** Appendix G.7: present evidence boundary (source line 6210)

**Exact current phrase:**

> This missing formal bridge is not an extra assumption in the proof of Proposition 3.3

The record correctly separates the stronger full-state specification from the measured-label statement used by the final upper bound. It also distinguishes a built wrapper from a wrapper reached by a particular proof root.

**Why it matters:** This prevents an optional formal strengthening from being mistaken for a mathematical gap in the separation theorem.

**Advice:** Keep the boundary concise and source-specific. Do not turn the review into a request to complete the stronger formal target.

## LS212

**reasoning_record · medium · funnel · direct_product**

**Location:** Appendix G.8: finite-behavior reduction (source line 6242)

**Exact current phrase:**

> the ordinary finite-behavior reduction above,

The formal-statement route can enter directly at Appendix G, but the relevant reduction is far away in §6.1. “Above” does not identify it, and there are several finite-mixture discussions in the record.

**Why it matters:** A reader checking the arbitrary-randomness boundary must search rather than follow a bounded proof route.

**Advice:** Link this phrase specifically to CL-independent-information, and distinguish the per-input cap condition from the finite seed-space statement.

## LS213

**reasoning_record · keep · keep · direct_product**

**Location:** Appendix G.8: equality and bound (source line 6253)

**Exact current phrase:**

> No promise-support or hardness premise is needed for this row.

This is a helpful boundary around equation (19). Its identity and search estimate belong to the independent zero-location experiment; the promised hard law is needed later for predicting the selected cell.

**Why it matters:** It shows which pieces of the lower bound remain valid independently of the Forrelation supplier.

**Advice:** Keep this separation of assumptions, especially when displaying the whole lower-bound chain.

## LS214

**reasoning_record · keep · keep · fourier**

**Location:** Appendix G.9: the status of the growing-k derivation (source line 6278)

**Exact current phrase:**

> the rest of §7.3 is ordinary mathematics.

The current record states exactly which displayed uniform estimate has a compiled supplier and which subsequent optimization is an ordinary derivation.

**Why it matters:** This is a more useful scope statement than a blanket claim that every displayed refinement has the same formal status.

**Advice:** Carry this distinction into any future summary that advertises the explicit growing-k family.

