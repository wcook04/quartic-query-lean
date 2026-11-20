# Reconstruction phrase links: review and reading guide

## Outcome

This return provides a new phrase layer for the complete reconstruction, paper lines 1–4670, at the packet's frozen source commit `f192def14f95a3aff7da5866f35be7b565595e1d`. It contains **419 phrase ties, 415 titled declaration cards, and eight topics**. The ties name 484 declaration contributions because some complete displays need more than one supporting statement. All ties are `new`; there is no phrase seed to preserve or remove.

The work reached the end of every section and appendix. The linked statements were read with their hypotheses and relevant definitions. An independent pass revisited the construction and Appendix G mappings; it corrected missing conjuncts, a definition mistaken for an implementation guarantee, the forward/inverse distinction, and a numerical complexity bound that was less direct than the available program witness. This is an AI-authored source review, not a human expert review, Lean compilation, Comparator run, or live-site validation.

The five files in this folder are the complete return: `ties.json`, `topics.json`, `titles.json`, `notes.json`, and this review. The paper and all 195 Lean files remain byte-for-byte identical to the attached ZIP. No new mathematical proofs or source changes were attempted.

## Start here if the construction is unfamiliar

The cost being compared is the number of times an algorithm asks for an unknown input bit. Computation between those requests is free in this model. A quantum request can act on a superposition of addresses, but it still counts as an oracle call. Both algorithms must return the correct Boolean answer with probability at least two thirds on every relevant input, and their budget is a maximum over inputs and branches.

The large input is a board with columns and many addressed certificate cells. A winning column must contain only ones and have a correctly addressed cell whose pointers find zeros in every other column. Its auxiliary partial-function inputs determine that cell's address. A partial function can answer one, answer zero, or be undefined. The board function is nevertheless total: an undefined auxiliary value prevents that column from winning. Every complete board still has a Boolean answer.

The stored circuit transcript has two jobs. Its domain output says whether an auxiliary input is promised, and its value output gives the answer when it is promised. The local gate equations show that the transcript is an actual computation. The domain test is essential because a perfectly consistent computation can correctly report that the input is unpromised. The probabilistic quantum decoder proposes an address; it does not replace those exact certificate tests.

The quantum algorithm uses comparisons to produce a short list that is likely to contain the genuine winner, then searches for failed local tests on those candidates. It need not certify every candidate during list construction. The classical argument couples a board with a zero in every column to one with a randomly selected zero erased and a valid cell planted. An algorithm can distinguish them only by reading a changed location. Reaching the planted cell requires naming the entire correct address before receiving its first changed bit.

The address answers come from independent hard partial-function inputs. A separate cap on each input gives a product bound for guessing their entire answer tuple. That separate-cap requirement is stronger than merely bounding the sum of the queries. The proof uses the joint event that a guess is correct and the relevant cap holds; conditioning on that cap can alter the hard input law and is not the same argument.

For each fixed order $k$, the same explicit family has quantum cost at most $C_k\sqrt m(\log_2m)^6$ and randomized cost at least $m^{2-1/k}/(400(\log_2m)^2)$, after a $k$-dependent threshold. The ratio of the polynomial exponents is $4-2/k$. Choosing an arbitrarily large fixed $k$ rules out every universal power below four; the universal quartic upper bound supplies the other direction. Letting $k$ grow with $m$ needs estimates uniform in $k$ and is a separate additional argument.

These points are the entry route through the cards: query model → promise → winning certificate → local tests → short list and verification → planting and separate caps → exponent. The analytic Forrelation proof can then be read as the supplier of the hard address bit.

## How to interpret a link

| Field | What it says |
| --- | --- |
| `defines` | The declaration defines the object or condition named. A definition alone does not prove an implementation satisfies it. |
| `states` | The selected claim is the declaration's mathematical statement, with the surrounding parameters understood. |
| `contains` | The declaration states the selected claim among additional conclusions. |
| `part` | The declaration supplies an identified component of the selected phrase or full display. |
| `proof` | The selected claim is supported by an identified passage inside the declaration's proof; the complete type is still quoted in the comparison register. |
| `same` / `stronger` | An authored judgment that the source states the selected claim, or a stronger version, in its actual context. These labels are not build evidence. |
| `weaker` / `different` | The particular destination omits part of the selected claim, narrows its scope, or states a different related proposition. The precise difference is recorded per contribution. |

Complete formulas are kept intact even when they contain several assertions. This creates many `part/weaker` contributions: three separate census theorems, for example, each supply only one count in a three-count display. Their collective coverage can be complete even though no single declaration states the entire display. A weaker contribution is not a verdict that the displayed mathematics is false.

The source signature, proof route, build status and headline dependency reach remain separate questions, as required by the packet's statement-evidence contract. No receipt was refreshed, and no declaration was promoted to current build evidence. In particular, the one-query compiler explicitly describes itself as an unverified candidate; a matching signature does not remove that qualification.

## Findings that most affect a reader

| Issue | Source finding | Consequence for these annotations |
| --- | --- | --- |
| Historical missing claims | Current files contain the full planted-event endpoints, finite list sampler, retained-register results, real-leaf analytic endpoints and additional Appendix A steps. | Earlier absence judgments were not copied forward. |
| Same family, both bounds | `construction_family_named` supplies the named circuit, coefficient 1/400 and logarithmic power six. | The two complexities are attached to the same function; fixed-k quantifiers are explicit. |
| Quantum law versus state | A probability law, a retained isometry and a physical continuation are distinct interfaces. | Cards explain what the current type actually preserves and what it measures. |
| Sharp qk cap | `ReadSpecOneQuery` calls itself a candidate not checked by native elaboration. | Sharp destinations disclose that status. The conservative 2qk source route remains the route to the required asymptotic bound. |
| Clean oracle E.2 | The source supplies retained-workspace E.1; the paper calls the reset-workspace form an ordinary corollary. | Retention is not relabelled as cleanup. |
| Integer circuit | Arithmetic maintains residues; final signed bounds recover the comparison signs. | Notes never claim every intermediate word is its intended signed integer. |
| Separate caps and external randomness | Endpoints use finite independent seeds and structural or recursive compliance predicates. | Unrestricted measurable seeds and terminal-count equivalences are not silently added. |
| Explicit floor threshold | The named theorem uses 3,499,200 k²; the paper specializes the sharper bound to 13,669 k². | The threshold mismatch is recorded without declaring the smaller arithmetic deduction false. |
| Worked finite board | The 104/48/104 census has declarations; the 180-gate board witness was not located. | The 371-test and 5,936-bit board is not credited to an unrelated asymptotic constructor. |

No mathematical contradiction with the paper was established by this source review. The material issues are missing exact destinations, narrower hypotheses or interfaces, ordinary corollaries, alternative proof routes and unestablished build status.

## Topic organization

| Topic | Purpose | Ties |
| --- | --- | ---: |
| Query models and promises | What an input query reveals, which inputs require correctness, and how the maximum query budget is counted. | 57 |
| The Forrelation address bit | The Walsh correlation, its one-sided promise, the quantum decoder and the exact certificate circuit. | 41 |
| Columns and addressed certificates | The board layout, the unique winning pair and the local checks that certify it. | 29 |
| Quantum comparisons and verification | How complementary comparisons yield a short candidate list and how each candidate is verified. | 76 |
| The classical planting argument | Couple a zero input with a planted one and bound how a classical algorithm can discover the change. | 47 |
| Prediction with a separate cap | Why predicting independent answers has a product bound when every input has its own query cap. | 37 |
| The optimal exponent | Combine the bounds for one fixed-parameter family with the universal upper bound and distinguish the growing-parameter consequence. | 61 |
| The Forrelation lower bound | The Gaussian interpolation, derivative estimates and decision-tree bounds that make an address bit classically hard. | 71 |

## Scope and coverage

| Paper range | Subject | Review scope |
| --- | --- | --- |
| 1–199 | Result, model and address bit | Definitions, quantifiers, universal bound and three Forrelation ingredients. |
| 200–474 | Certificate construction | Layout, transcripts, winner uniqueness, local verification and comparison mechanism. |
| 475–809 | Quantum upper bound | Weighted list, retained preparation, decoder, verifier and physical cost. |
| 810–1341 | Classical lower bound and exponent | Coupling, search, capped prediction, product proof, floors and fixed/growing-parameter distinction. |
| 1342–2048 | Alternative Forrelation proof and conclusion | Gaussian interpolation, real-leaf bounds, amplification and sharp uniform endpoint. |
| 2049–2324 | Appendix A | Universal quartic route and its actual constants. |
| 2325–2829 | Appendix B | Conditional product proof, search estimates, realized caps, minimax and examples. |
| 2830–3134 | Appendix C | Thresholds, growing parameters and quantitative inequalities. |
| 3135–3347 | Appendix D | Read in full; literature comparisons remain written mathematics where the paper says so. |
| 3348–3808 | Appendix E | Amplification, retained registers, coherent local tests and physical compilation. |
| 3809–4065 | Appendix F | Finite models, off-promise conventions, simulation and exact examples. |
| 4066–4451 | Appendix G | Integer normalization, promise decoder, modular circuit and finite census. |
| 4452–4670 | Correspondence, formal note, attribution and references | Read in full; provenance and bibliographic prose are not assigned fictitious Lean statements. |

The review did not stop at a partial line range. It also does not claim that every untied sentence is unformalizable or absent from every possible combination of lemmas. Definitions and load-bearing results have priority, meaningful proof steps have destinations, and ordinary derivations, repeated explanations, missing concrete instantiations and external comparisons are accounted for below. No source link was invented solely to eliminate an uncoloured sentence.

## Findings by section

### Opening, construction, quantum bound and Appendix G

#### Scope and outcome

Read paper lines 1–810 and 4066–4670, including the final correspondence, formal-proof note and references. Inspected the linked declarations and the relevant definitions and hypotheses. The paper and Lean files are unchanged. The result is a source-level correspondence review; no Lean build, kernel audit or live-site test was run.

The phrase layer is new because this packet has no seed. Existing paragraph selections and the historical fidelity review were useful for navigation but not accepted as evidence that a proposed phrase matches its declaration. The returned titles name mathematical objects or claims. Each note supplies the assumptions and the meaning of the notation a reader needs at the point of entry.

#### What a reader needs to keep separate

The board is a total Boolean input. Undefined auxiliary answers do not make the board undefined; they prevent the affected column from winning. A consistent transcript can exist on an unpromised input. The domain-output test is what rejects it. The quantum decoder may still return any Boolean label there, within its all-input cap.

A pointer word names a row; its stored target bit is not read for free. Similarly, naming a cell address selects an ordinary bit coordinate. It does not certify that the address is correct. The lower-bound argument counts a correct address guess when the algorithm first queries a planted cell, while the upper-bound verifier checks that the proposed address is certified.

The theorem's quantifiers fix k before the threshold and the constants. The family wrapper supplies both bounds for the same named circuit, including logarithmic exponent six and classical coefficient 1/400. The universal-exponent declaration concerns an infimum of powers with one common constant over all input lengths; it does not identify an equality R=Q^4 at one finite input size.

Probability, retained state and physical query count have distinct source statements. Equality of measured answer laws does not identify the full workspace state. The complete retained decoder quantifies over every embedded logical state and every continuation. Its established source route uses the two-query compiler. The exact qk candidate discussed below has a separate evidence status.

The arithmetic invariant is a congruence modulo 2^w. Ideal integer-walk estimates do not imply that every intermediate register is its intended signed integer. The final bound |N|≤M and the three final comparison bounds justify sign recovery at the chosen width. The notes state this invariant before discussing gate costs.

#### Material findings

1. Current source wrappers now state many claims that the historical review described as missing: the full integer promise comparisons; output rules on every consistent transcript; the retained physical decoder; independent tensor preparation; the list algorithm; and the concrete error and query-cost statements. The return follows those current declarations.
2. `Paper/ReadSpecOneQuery.lean` explicitly says: “This is a candidate, not a native-checked theorem.” `Paper/ConstructionForrelationSharp.lean` makes its sharp physical witnesses conditional on that elaboration. The signatures of `forr_walsh_physical` and `construction_decoder_sharp` match the intended one-query-per-read route, but a source signature is not a build receipt. Both linked notes and their link notes disclose this status. The first candidate's explicit final state is Hψ; obtaining ψ uses a further free H. The conservative complete decoder keeps the physical cap 2qk and already supplies the asymptotic ingredient.
3. The complete flag-by-flag state written in G.2 is not identified by the generic `Samples` statement. The source gives a retained preparation and its exact binomial output law; that does not by itself assert the exact displayed flag, address and count-register tensor decomposition. The decomposition and the specific flag-unitary proof remain untied here.
4. The type of the large-success tail theorem states the endpoint exp(−qc/16), not the stronger intermediate exp(−qc/10). Likewise, the exact circuit size theorem exposes `coreSize+3`; the closed expanded polynomial in G.3 requires unfolding constructor recurrences and arithmetic. These are documented as partial statement correspondences, not mathematical counterexamples.
5. All three counts in G.4 have individual source declarations: 104 one-inputs, 48 zero-inputs and 104 undefined inputs. Each is marked as a component of the complete selected display. The five-entry numerator histogram and the full three-example table do not have a matching assembled declaration in the supplied source.
6. No instantiated 180-gate circuit with output indices 178 and 179 was located. Consequently the exact 371-test and 5,936-bit worked board, its precise pattern of failed tests, and the second off-promise board are not credited to the general asymptotic circuit theorem. This is the main missing concrete-example correspondence in these sections. The negative witness with Φ=−1 is a different input from the board's Φ=−1/2 example; the paper itself distinguishes them, and the return does not merge them.

No mathematical contradiction with the paper was established in these sections. Missing type clauses, alternative implementations and absent concrete instantiations are reported at their actual level. The presence of a proof body in the packet is not described as successful elaboration.

#### Coverage and intentional omissions

The theorem statement, the R/Q conventions, the promise definition and three ingredients, the certificate layout, winning conditions, uniqueness, local tests, comparison facts, weighted tournament, decoding and verification bounds all have phrase links. Appendix G links the integer normalization and comparisons, binomial analysis, coherent output law, arithmetic invariants, final sign recovery, circuit costs and promise census.

The introduction's motivation and repeated roadmap, figure descriptions, attribution and bibliography remain untied. The named figure asset and the 180-gate worked-board constructor are not supplied in this packet as matching formal objects. Scalar bookkeeping inside already represented derivations is not treated as if every intermediate line had its own theorem. The explicit flagged state, literal phase-kickback calculation, five-value histogram, fixed small-board examples and expanded constructor-count algebra are recorded above at their actual source coverage. The reading reached line 4670; there was no unreviewed tail.

The global review supplies every weaker or different pair with the exact selected paper phrase and actual Lean signature. This fragment's annotations passed the packet's mechanical checker before merging.

### Classical proof and exponent review

#### Scope and outcome

Read the entire assigned text, paper lines 811–1341 and 2325–2829, and inspected the relevant Lean declarations and their local proof context. This fragment adds exact mathematical phrases, with complete display formulas preserved. Titles explain the mathematical result; notes explain the meaning, assumptions, and limitations for someone opening the source without prior familiarity. These are source correspondences, not a claim that a Lean build was run.

The current source is substantially more complete than the historical fidelity review. It contains the absolute two-event discrepancy bound, the full independent-selection equality, exact fixed-time joint-event and true-cell bounds, complete absolute three-term discrepancies, the conditional uniform-zero law, and a wrapper for all clauses of the erased-zero display. The historical claim that these endpoints are absent must not be repeated. The unconditional cubic failure and exponent-four theorem also exist.

#### Reading decisions that matter mathematically

The classical lower bound is independent of the size of the realizing circuit. Circuit size matters to the quantum upper bound, which must be supplied by the same eventual family. The planted proof keeps the selected column independent of the whole dummy run, counts each discovered column once, and counts repeated queries as cost. Its nonheavy event is used jointly with a proposed true-cell query. It never conditions the hard input law on nonheaviness.

Separate caps are materially stronger than a total budget of rL. The predictor used here actually has a total target budget L, which implies the needed separate caps. It stops before reading an excess target query or the chosen cell bit. The source’s generic replay theorem guarantees the returned address under matching-answer and prefix-count premises; the actual fixed-time endpoint is the preferable link for the nonheavy joint event.

The weighted direct-product proof and the conditional-value proof are both present. The latter explicitly handles compatible adaptive schedules, positive transcript mass, separate local posteriors, unchanged factors, zero-weight branches, and finite terminal iteration. Compound displays are not called exact matches when an individual declaration supplies only one of their clauses. Their component links are marked weaker and the missing clauses are identified below.

#### Concrete formalization boundaries

1. The finite average theorem uses a finite seed type. It permits correlated advice and coins encoded in one seed, independent of the complete target tuple. It does not prove transfer from an arbitrary measurable external seed. The ExternalRandomness and MeasurablePolicies source descriptions explicitly keep that extension as further work.
2. OutTree.capped is a cap on all syntactic branches. The paper often phrases a cap in terms of actual executions. Clipping is structurally capped even on inconsistent repeated-answer branches. The realized-cap theorem uses recursive actualComplies, while the paper’s corollary uses terminal numerical counts; the packet defines actualCount but contains no count-compliance equivalence theorem.
3. The sharper successor search inequality with denominator m+1 exists for one column’s finite set of worlds. A theorem packaging both averaged m+1 claims in §6.3 was not found. The weaker denominator-m endpoints do exist. None of these claims asserts an optimal distinguishing probability at a fixed budget.
4. The early/late decomposition is not encoded. The total expected-discovery bound and full equation (B.7) have declarations using the alternative finite-world argument. These declarations state their conclusions via an alternative route; they do not identify the printed route as formalized.
5. The ratio argument and the exponent-four conclusion are available for a fixed k chosen before t. No source theorem with the numeric growing-k threshold 13669 k² or the stated k(m) family was found. That part of §7.3 is explicitly an ordinary deduction in the paper, and is left unlinked here.
6. The minimax theorem provides one promised-input probability law with every shallow tree’s success at most 2/3. It does not state a strict common positive margin and does not implement the appendix’s nearest-point separation proof. The stronger finite-dimensional statement in B.4 is mathematically consistent with the endpoint; its source correspondence is incomplete.
7. The concrete XOR/AND examples, dependent selected-column experiment, simulator table, and numeric conditioning counterexample (B.9) have no matching instantiated declarations. They are left untied instead of being mapped to general results that do not prove their calculations.

No mathematical error in the assigned paper text was established by this review. The issues above are differences in what the available declarations state or prove. In particular, finite seed coverage and an omitted equivalence wrapper should not be reported as counterexamples to the paper’s mathematical claims.


### Forrelation and quantitative appendices: source review

#### Scope and result

I read every assigned line: Section 8 and the conclusion (1342–2048), then Appendices C and D (2830–3347). The phrase ties were created from the frozen paper and the actual source statements and proof slices. The historical statement-fidelity review was treated as a warning about possible issues, not as a verdict on the current source. The full source remains unchanged.

The fragment supplies 79 new ties. Each named declaration has a title of 2–12 words and a reading note of 40–120 words. Quotes stay within one paragraph or one complete display. Compound displays remain intact; a declaration missing a selected conjunct receives `weaker`, even when its `part` relation identifies the particular component. Such rows are partial coverage, not claims that the complete display is false.

#### Findings that change what a reader should infer

1. **The main analytic endpoint statements have direct, useful destinations.** `sum_abs_ext_Dl_le_real_leaves_explicit` covers arbitrary leaf values in [-1,1], all biases of magnitude at most one half, and the exact 2^{-r} residual in (8.28). `advantage_le_sharp_real_leaves_explicit` gives the corresponding sharp bound (8.29), and even permits a general row-orthogonal matrix with an entry bound. These are preferable to the earlier Boolean-tree helpers.
2. **A narrower intermediate is not a missing final theorem.** `walk_chaos` and `abs_ext_tree_chaos_le` use a Boolean tree followed by one real map on its two outputs. Their scope is narrower than independent real labels at every leaf. The later finite convex-decomposition argument supplies the full real-leaf endpoint. The notes preserve both facts.
3. **The sharp uniform bound is stated exactly.** `QuarticQuery.forrelation_lower_uniform_sharp` has constant 2/18225, denominator k² ln(4km), and hypothesis 15k+2≤2t. The fixed-k theorem `bansalSinhaLower` is a locally derived proposition in this source, rather than an unproved literature premise. This report says what the source declares, not that the snapshot compiled.
4. **The named explicit floor threshold is coarser than the paper’s specialization.** `lvalue_lt_R_explicit` assumes t≥3499200k². The paper states 13669k² and optionally ceil(54675k²/4). The smaller thresholds are ordinary arithmetic consequences of the sharp theorem and the logarithmic estimate, but are not the hypotheses of that named theorem. No countercalculation was found or asserted.
5. **The generic martingale statement is broader than its local implementation.** The source has a two-point exponential-moment lemma and a finite query-tree crossing estimate with a bad-coefficient term. They are not literally a theorem about every bounded centered law or every zero-start martingale. Their links make that boundary explicit.
6. **Differentiating an integrand and differentiating its expectation are different claims.** `hasDerivAt_ext_s` is pointwise in the Gaussian realization. The needed averaged derivative is a local claim in `exists_identity`, justified by a uniform dominating bound for interior interpolation parameters. The paper’s polynomial shortcut is an alternative written route; the source does not export the polynomial statement or its endpoint version.
7. **The full growing-family schedule is a written combination.** The expanded quantum constant and its exponential envelope have exact theorems. No named theorem was located for the particular floor schedule, the explicit epsilon expression, or its final exponent comparison. Appendix D explicitly labels its literature comparisons as written mathematics only; those passages have not been relabelled as formal statements.

#### Choices made for a cold reader

The cards follow the mathematical dependency: normalized correlation and promise; product-weighted extension; Gaussian integration; the interpolated sign law; one common mean-value point; the positive Forrelation mean; the full real-leaf derivative bound; amplification and off-promise acceptance; the sharp uniform conclusion. The constants are explained where they enter, rather than treated as opaque names.

Each note distinguishes the relevant object from nearby ones. The independent Gaussian samples U, the correlated pair (U,HU), the conditionally independent signs at a fixed bias, the unconditional comparison law ν₁, and the promise-supported minimax law used on the board are different objects. The analytic notes never assume the correlated pair is independent or that ν₁ is supported on promised inputs. They also identify the indexing conversion k=l+1, so a reader does not mistake the number of Gaussian links for the number of sign blocks.

The proof-route distinctions are local and concrete: dominated differentiation versus a polynomial shortcut; a two-point/tree exponential argument versus the printed general martingale proof; a finite convex extension for real leaves; exponential control of the padded depth versus the printed binomial sum; and the older coarse threshold versus the sharp arithmetic specialization. Agreement of an endpoint is not a claim that these proof routes coincide.

#### Statements or components not found in the printed form

The detailed ledger is in the omission register below. In particular, no separate matching declaration was located for commutation of the distinct ordinary partials in (8.5), the named law ν_s in (8.13), the polynomial-in-s shortcut, each full two- and three-block worked derivative display, the single-path derivative and expected-product estimate (8.25), the uniform-Fourier expansion (8.27), the generic probability-space maximal inequality, the arbitrary-acceptance quantifiers of (8.37)–(8.38), the exact intermediate C.4 algebra, the growing-family schedule and epsilon calculation, the exact 119/144 intermediate gap, or the smaller named threshold specialization. This is a report of source destinations not located, not a proof that the mathematical claims are false or that their final consequences lack formal suppliers.

No sentence was shown to be mathematically false by this source inspection. Several sentences are broader than a tempting declaration; those comparisons are quoted below. The full arbitrary-real-leaf endpoint and the sharp uniform statement should not be described as missing.

#### Verification limits

Only frozen source bytes were inspected. This work does not claim Lean elaboration, kernel checking, current Comparator status, a native build of ReadSpecOneQuery, or compiled dependency reach. The packet’s mechanical checker validates locations and shapes of links; it cannot establish their mathematical fidelity.


### Review of Appendices A, E and F

#### Scope and evidence status

I read the full assigned ranges, paper lines 2049–2324 and 3348–4065, together with the request, return contract, writing method, statement-evidence contract, prior fidelity review, and the Physlib exemplar. This fragment contains **142 new phrase ties and 139 declaration cards**. Every card has a title of 2–12 words and a reading note of 40–120 words. No source file or paper text was changed.

The links are based on **source inspection**, not a Lean build. The supplied return checker verifies quotation positions, nonoverlap, formula boundaries, declared names, line ranges, and required fields. It cannot establish mathematical fidelity or successful elaboration. I also checked namespace scopes independently, because the supplied checker accepts suffix matches and would otherwise tolerate an incorrect namespace prefix. That check caught and corrected `failProb_attempts`: it is in `QuarticQuery.Amplification`, outside the nested `Preparation` namespace.

All ties are new because this is a fresh phrase map, not a revision of a seed. The earlier annotation files and source-link labels were used for navigation, never as evidence that a statement matched. Several important destinations have changed since the earlier review.

#### What changed and why

##### Appendix A: make the actual proof route visible

The new roadmap tie at (A.2) sends each of the four inequalities to its own current source endpoint. The later occurrences receive shorter destinations at the point where their proofs are explained. The route now includes the nonnegative Perron witness, coordinate-mask norm, progress quantity, per-query estimate, final overlap, sensitive-block star, sensitivity graph, degree-dimensional restriction, recursive Huang matrix, majority-supported eigenvector, and the sensitive-block counting ingredients of the deterministic bound.

The explicit constants must be kept separate:

| Route or component | Actual source content | Reading consequence |
| --- | --- | --- |
| Printed Appendix A route | `appendixA_D_le_Q_pow_four`: $D\leq1500625Q^4$, using $35^4$ | This is the direct destination for the printed raw-$Q$ bound. |
| Headline imported endpoint | `QuarticQuery.D_le_Q_pow_four` in `Appendix/TheoremA1.lean`: $D\leq20736Q^4$ | It is a different route and coefficient, not the statement of the printed star proof. |
| Alternative sensitivity estimate | `appendixA_lemmaA3`: block sensitivity at most $16Q^2$ and spectral sensitivity at most $36Q$ | This does not state the printed $1225Q^2$ and $35Q$ pair. The $36^2=1296$ degree-scale coefficient alone is not a complete quartic coefficient; multiplying by the block-sensitivity factor gives $20736$. |
| Optional hybrid | `appendixA_D_le_Q_pow_four_hybrid`: coefficient $19600$ | It combines a different block-sensitivity argument with the newer spectral estimate and is not substituted into the printed route. |
| Named combined endpoint | `appendixA_theoremA1` uses $(1+Q)^4$ | Its reassuring name does not make it the exact raw-$Q^4$ display. The map uses the tighter statement plus the separate $R\leq D$ theorem. |

The norm convention is also explicit. Spectral sensitivity is the Euclidean operator norm of the real sensitivity adjacency matrix. The degree bridge changes the bit-valued output to a sign-valued output without changing degree. These definitions are not interchangeable with an entrywise matrix norm or an unexplained scaling of the adjacency matrix.

The literal bit-query equation (A.4) ends with equality because the whole query-register mass is one. The source progress lemmas used here work with the **controlled phase** oracle and sum only active-control mass, which is at most one. The following paragraph of the paper states exactly that version, and those clauses are tied. I did not represent its inequality as the bit-query decomposition’s equality.

##### Appendix E: separate laws, retained states, and query units

The sequential-verification cards explain what `vall` and `tval` mean before their induction bounds. In the lower-bound card, the hypotheses are visible by name: bounded probability data, dominance, fresh verifier success, forced stopping at zero total weight, the finite-horizon condition, and a failure bound only on histories that still miss the dominant candidate. The perfect-indicator variant explicitly replaces `v(s)≥1−ε` by `v(s)=1`; that is why the list bound has no extra verifier error.

The current source has a **finite list-valued sampler**, `quantumTournament_list`, with a law chosen before both the input and the dominant candidate. An old claim that only the Boolean continuation had been formalized would now be wrong. The new cards distinguish the list output from the Boolean verification endpoint while explaining their relationship.

Amplification has three materially different interfaces:

| Declaration | What its statement provides | Scope to preserve |
| --- | --- | --- |
| `Amplification.bounded_amplification` | One abstract procedure, a uniform call cap, failure bounds, and phase-invariant observations of successful states for every preparation | This is an abstract procedure theorem; it is not by itself a physical `AdaptiveProgram` witness. |
| `Upper.uniformOpaqueAmplifier` | One fixed choice unitary before every preparation, a retained original-register factor, success bounds, and logical-circuit accounting | The success condition is a Boolean predicate on basis labels, with a basis origin. The statement does not directly quantify over an arbitrary free projector. |
| `Paper.quantum_amplified_label_law` | A physical bounded sampler with the exact amplified classical-label law | Its conclusion does not identify that measured label with a designated retained subsystem from the general-projector statement. |

Thus the retained-state source work is substantial and should not be dismissed as “only label probabilities.” Equally, its particular projector interface should not be expanded silently. The mixed nature of this comparison is marked on the affected links, and the complete source headers appear below.

The cap display links both the syntactic cap theorem and `amplification_budget_le`. The latter bounds the **padded product itself**, $N(2M+1)$, which is what the implementation charges. Bounding a smaller procedure’s actual cap would not suffice to bound that product in the subsequent arithmetic.

The cost cards maintain three units: calls to a preparation or its inverse, logical reads within that preparation, and physical bit-oracle queries. E.5’s two-query compiler is a valid conservative upper bound. I do not call it necessary or optimal. The newer `Paper/ReadSpecOneQuery.lean` says explicitly that it is a **candidate, not a native-checked theorem**; the sharp Forrelation wrappers inherit that qualification. This fragment does not use those candidates to upgrade the evidence status of the physical bounds.

Equation (E.1) has a current arbitrary-index coherent destination, not merely a uniform-sampling theorem. Its card explains arbitrary coefficients, retained index-dependent workspace, and zero amplitude on incorrect output labels. Equation **(E.2) remains deliberately untied**: the `ConstructionCoherent` module explicitly disclaims a further clean-XOR theorem, and the paper itself says the reset-workspace form is derived there as an ordinary corollary. It would be a serious interface error to label E.1’s retained workspace as already reset.

##### Appendix F: teach the conventions before the examples

The map now exposes the actual definitions of partial functions, totalization, tree evaluation and syntactic depth, positive finite random mixtures, their success law, and the three admissibility predicates and minima. The cards repeatedly make the quantifier order concrete: one tree, mixture, or state-and-program is chosen before the universal input quantifier. Off-promise inputs lack a correctness obligation but remain subject to the same cap.

The empty-coordinate alternative in `QLe` is explained as a representational necessity. The query basis is empty when there are no coordinates, so it has no unit vector; the constant-answer clause nevertheless gives the expected zero-query behavior. It also handles empty promises naturally. This is not evidence of a model loophole.

The measurement cards explain why branch vectors remain unnormalized. Their squared norms carry the branch probabilities, and the source proves nonnegativity and exact total-mass conservation for every vector, including zero. The controlled-phase/bit identity is an equality of states at one oracle call. By contrast, deferred measurement’s final endpoint is an equality of accepting masses, with no assertion that the two final states coincide. The strengthened `FixedSim` invariant retains both an entry map and an oracle-compatible embedding; that distinction is essential when a query is prepended.

The exact examples are linked only to their actual statements. There is a direct quantum one-bit identity theorem and a direct randomized OR theorem. These do not independently state the other complexities printed in the same displays. The four OR success probabilities have an exact theorem; the table’s individual component outputs come from the definitions and are marked as additional content. The one-sided promise has direct randomized and quantum zero theorems. I did not invent direct deterministic OR, quantum OR, or two-bit XOR complexity declarations to make the examples appear fully covered.

#### Cold-reader changes that would most improve the paper

1. **Put the two proof routes beside the first universal-bound display.** A short sentence naming $35^4$ as the printed route and $20736$ as the imported endpoint prevents a reader from treating different constants as a contradiction or as identical evidence. Keep raw $Q^4$ distinct from the relaxed $(1+Q)^4$ form.
2. **Define the unit of every cost symbol where it first appears.** The E.5 table now has direct cards for address, comparison, and local-test logical costs. Its caption should continue to say that the final budget already includes physical conversion factors.
3. **State the retained subsystem before presenting the amplified label formula.** The original register includes the preparation’s workspace; trial histories belong to separate auxiliary factors. A probability law for labels does not identify that subsystem.
4. **Keep the clean-oracle corollary visibly separate.** E.2’s reset workspace is stronger than E.1’s retained workspace. The paper already says it is an ordinary corollary; preserve that sentence rather than using a source link that suggests a direct formal theorem exists.
5. **Explain the `none` case before giving any complexity minimum.** Undefined is not false. The one-sided identity example is an effective demonstration and should remain close to the promise definition.
6. **Describe deferred measurement by its output guarantee.** “Same acceptance mass for every input and vector” is precise. “Same state” would overstate the theorem, especially after padding finished branches with oracle calls.
7. **Mark the exact-example coverage honestly.** The source proves some displayed components directly and supplies generic tools for others. Keeping the ordinary OR and parity calculations is useful; forcing a nearby theorem to pretend to be the full example is not.

#### Expected declarations not identified and deliberate omissions

The absence claims here concern identifiable statements in the supplied local source, not mathematical impossibility and not a claim that the printed arguments are false. the omission register below records every omission with its paper range. The most consequential are the full general-error $Q_\epsilon$ adversary theorem, literal bit-query (A.4) decomposition, clean-XOR equation (E.2), the concrete cyclic probability tables, repeated-query pruning, exact $D(\mathrm{OR}_2)=2$ and $Q(\mathrm{OR}_2)=1$, the full nondyadic-selector necessity argument, and the exact three two-bit parity complexities. I also leave the literature comparisons and ordinary purification/dilation discussion untied.

No new mathematical error in the paper’s assigned statements was established by this review. The most important findings are **evidence-scope differences** and stale annotation assumptions. In particular, a `weaker` label below often means that a declaration proves one conjunct of a whole display or its endpoint without the displayed intermediate steps. It is not a verdict that the display is false.


## Omission register

The following ranges identify untied material or untied components within a partly linked passage. A range in this register does not mean that every sentence within it lacks a link. The precise linked spans are in `ties.json`.

- **Paper lines 811–831.** Context and motivation at the start of the assigned section; no standalone additional formal claim beyond the theorem/hard-law ties.

- **Paper lines 905–911.** First-difference narrative; the actual necessary-event statement is tied at line 912 and its averaged endpoint at (6.2).

- **Paper lines 1148–1148.** Literature attribution and comparison of external results; no internal declaration verifies the bibliographic claims.

- **Paper lines 1260–1277.** Parameter choices and elementary setup for the ratio; the complete ratio (7.3), fixed-k choice, and divergence are tied.

- **Paper lines 1320–1341.** Growing-k family is described by the paper as an ordinary deduction. No theorem with the 13669 k^2 threshold or the resulting k(m) family was found; fixed-k declarations are not used as replacements.

- **Paper lines 2368–2376.** Concrete incompatible-schedule example is not instantiated in Lean. The surrounding general schedule condition is covered by classical_prefix_iff.

- **Paper lines 2392–2396.** Maximum attainment is tied. The additional interval 1/2≤V≤1 is not packaged as the displayed claim in the located declaration.

- **Paper lines 2493–2497.** Explanation relating the two proof routes; the normalization display is tied only to its available first-identity definition.

- **Paper lines 2519–2521.** Early/late counts and their two separate estimates are not defined or proved in the packet; only the total endpoint and exact uniform-zero posterior are tied.

- **Paper lines 2550–2563.** Detailed finite-world induction prose is not individually annotated; the complete combinatorial inequality is tied to the theorem proving this induction.

- **Paper lines 2583–2595.** Alternative use of Drucker’s external global-budget theorem and numerical substitution has no matching internal theorem.

- **Paper lines 2650–2768.** The four-column XOR planting/simulation, dependent selection, promised AND conditioning, and adaptive cap example including (B.9) have no matching concrete declarations. General clipping and selection results do not prove their numerical tables.

- **Paper lines 2777–2790.** Finiteness is tied. The nearest-point separation construction and strict common margin are not formalized by the non-strict hard-law theorem, whose proof uses minimax.

- **Paper lines 2803–2817.** The exact elementary estimate, final allowance range and full double-floor endpoint are tied; remaining intermediate floor algebra is not split into more navigation fragments.

- **Paper lines 1344–1346.** Authorship, historical review status, and the narrative transition are not mathematical theorem statements.

- **Paper lines 1362–1362.** The phase-query implementation is covered by the quantum construction elsewhere; this fragment does not duplicate that source audit.

- **Paper lines 1386–1400.** External attribution and literature provenance are not certified by a local theorem; only the precise mathematical bounds are linked.

- **Paper lines 1433–1437.** No named declaration for commuting distinct mixed partials was located; the monomial worked example remains explanatory. Same-coordinate vanishing and the chain rule are separately linked.

- **Paper lines 1472–1476.** The parameterized transform search and derivative formula are written motivation; the selected concrete functions and their derivatives are linked instead.

- **Paper lines 1497–1499.** The nonnegative polynomial identity occurs inside the bound proof; the theorem for |φ|≤1/2 is already linked. No additional equality theorem is invented.

- **Paper lines 1534–1534.** The attribution and comparison with another truncation choice are literature statements.

- **Paper lines 1541–1545.** Underlying Gaussian notation is explained in the interpolation and moment cards; no separate law-definition destination is needed.

- **Paper lines 1562–1567.** The code represents ν_s by Gaussian integrals of product-weighted extensions. No exported declaration constructs the named unconditional probability law ν_s itself.

- **Paper lines 1569–1569.** The promise-supported minimax board law and the off-promise analytic comparison law are conceptually distinguished, not equated by a theorem here.

- **Paper lines 1592–1592.** The polynomial-in-s shortcut is not the source proof route; the source uses dominated differentiation. This is a route difference, not a refutation of the written argument.

- **Paper lines 1602–1664.** The full k=2 and k=3 worked displays are specializations of a generic chain argument, not individually exported statements. One generic reduction and the same-coordinate cancellation are linked without claiming all worked formulas.

- **Paper lines 1671–1673.** The one-edge multiplier is part of the recursive integrand and path expansion; no redundant definition card is added.

- **Paper lines 1721–1735.** No separate full-path derivative and squared-path coefficient theorem matching these printed displays was located. The formal mean argument uses nested sums Rs, Yy, and TT.

- **Paper lines 1747–1764.** The fixed-path expected product estimate (8.25), including T_p, is not an exported named theorem found in the source. The marginal moment suppliers and aggregate mass_ge conclusion are linked.

- **Paper lines 1775–1777.** The illustrative promised-mass and Markov bounds are used through specialized pointwise acceptance comparisons; no standalone measure statement is substituted.

- **Paper lines 1790–1802.** No named uniform-Fourier expansion matching (8.27) or its degree-(k+1) monomial example was located.

- **Paper lines 1835–1835.** Convex-mixture closure follows by ordinary averaging. The full real-leaf theorem is for a single tree; no mixture quantifier is silently added to its type.

- **Paper lines 1875–1879.** The degree-two example merely illustrates chaos_insert; the generic identity is the selected destination.

- **Paper lines 1885–1898.** The explanatory path-cylinder and zero-probability discussion is supported by finite merge/walk identities, not a separate conditional-distribution theorem.

- **Paper lines 1921–1940.** The exact intermediate union-bound route differs: the code controls the two signs and bad coefficients in its recursion. The final crossing bound agrees, but intermediate printed constants are not attached to it as statements.

- **Paper lines 1953–1957.** These parameter substitutions are algebraic choices already explained in the explicit real-leaf theorem and residual card.

- **Paper lines 1966–1966.** The +1 remainder is an immediate weakening of the linked exact +2^{-r} bound.

- **Paper lines 2028–2037.** The narrative count of k factors and the repeated threshold explanation add no separate source theorem; the sharp quantitative bound and threshold mismatch are already explicit.

- **Paper lines 2041–2045.** The broader quantum, planting, and quartic conclusions belong to other assigned fragments. This fragment links only its analytic summary, avoiding unreviewed cross-topic claims.

- **Paper lines 2884–2899.** The exact C.4 squared main-term expression is not exported in that form. In particular core_bound deliberately drops the factor four; exists_threshold supplies the required final smallness conclusion. The C.3 depth and logarithm estimates are linked to their actual local proof claims.

- **Paper lines 2904–2921.** The historical closure is within the bansalSinhaLower proof; no arbitrary-acceptance theorem is invented for its local inequalities.

- **Paper lines 2945–2989.** No named theorem for (C.6), the floor schedule k=floor(sqrt(t/20)), its explicit epsilon, or the final growing-family exponent bound was located. These are written combinations of the uniform promise bound, generic planting theorem, and explicit quantum cost.

- **Paper lines 3005–3013.** No generic conditional-Hoeffding/supermartingale declaration matching the printed arbitrary-law proof was found; the narrower two-point and finite-tree estimates are transparently linked.

- **Paper lines 3047–3063.** The exact 119/144 numerical gap and the intermediate (C.10) inequality are not exported statements in the source. The uniform contradiction uses compatible inequalities without naming these displayed endpoints.

- **Paper lines 3067–3086.** The binomial/geometric-series intermediates of C.11 and the full chain in C.12 are not the formal route; only their actual exported numerical endpoints are linked.

- **Paper lines 3126–3132.** The arithmetic specialization to 13669k² and optional ceil(54675k²/4) has no matching named floor theorem. This absence does not show either ordinary specialization false.

- **Paper lines 3135–3347.** Appendix D is a literature-and-scope comparison. D.3 and D.4 expressly describe their comparisons as written mathematics only, with no Lean theorem stating them. No local theorem is made to certify those external-source comparisons.

- **Paper lines 2072–2077.** **Explicit polynomial interpolation formula and uniqueness argument.** Degree and its Fourier/sign conventions are tied. The complete interpolation construction is explanatory background rather than a separately identified local theorem.

- **Paper lines 2125–2135.** **Absolute-value Rayleigh comparison and the ordinary bit-query deferred-measurement route.** The eigenvector result and the separate fixed-sequence bridge are linked. The prose proof combines several matrix facts and bit/phase conventions; it is not represented by one exact statement here.

- **Paper lines 2143–2154.** **Equation (A.4), literal bit-query decomposition with sum of block masses equal to one.** Available local progress statements use a controlled phase oracle. Its active control mass is at most one, not necessarily equal to one. The following controlled-phase clauses at 2156–2160 receive exact destinations; the bit-query equality is not silently substituted.

- **Paper lines 2181–2192.** **Exact coefficient comparison and the general-error Q_epsilon adversary formula.** The 1/35 endpoint and sharper cap inequality are linked. No local full theorem defining Q_epsilon and proving the displayed general-error ratio was identified. The error-1/3 statement is not represented as that more general assertion.

- **Paper lines 2275–2282.** **Intermediate equalities in the Rayleigh chain and explicit extension-by-zero argument.** The outer Rayleigh inequality and the paper-route degree endpoint are linked; the selected full Rayleigh display is explicitly marked partial. Routine intermediate matrix equalities are not given invented standalone names.

- **Paper lines 2297–2305.** **An explicit tree constructor for the repeated maximum-monomial algorithm.** Sensitive-block extraction, lifting, disjointness, round count, and the Midrijanis endpoint have destinations. The actual endpoint invokes the complexitylib decision-tree bound; no separate local recursive tree constructor for all the prose instructions was identified.

- **Paper lines 3358–3361.** **Closed product for sequential verification and permutation invariance.** The recursion and its member/union bounds are tied. No dedicated local equality V(L)=1−product(1−v) or permutation theorem was identified in the inspected tournament modules.

- **Paper lines 3429–3435.** **The literal two-by-two Grover rotation matrix.** The full vector decomposition and phase-equivalence theorem are tied. The displayed matrix presentation is explanatory linear algebra, not a separately identified matrix-valued local declaration.

- **Paper lines 3541–3547.** **Product-state versus Bell-state counterexample.** No local declaration for these two vectors and the stated alternate-basis probabilities was identified. It remains an ordinary mathematical example, not an application of the successful-label theorem.

- **Paper lines 3571–3623.** **The exact cyclic four-candidate and fractional-comparison examples.** Generic finite-law, conditional-label, and tournament statements are tied. No declaration for these particular 11999/12000 tables and their exact probabilities was identified; the general theorem is not labeled as that numerical example.

- **Paper lines 3667–3670.** **Comparisons with earlier search algorithms.** These are literature and scope comparisons, not claims that a local declaration formalizes those external algorithms.

- **Paper lines 3710–3719.** **Equation (E.2), clean XOR oracle with workspace reset and cap 4q_*.** The inspected ConstructionCoherent module explicitly disclaims an extra clean-XOR theorem, and paper line 3719 calls this an ordinary corollary of retained-workspace equation (E.1). No exact clean interface declaration was identified. Equation (E.1), arbitrary-index coherence, and physical continuation compilation are tied instead.

- **Paper lines 3733–3739.** **Literal tensor decoder and sharp physical Forrelation route.** The paper’s conservative compiler and aggregate budgets are tied here. The root reviewer owns Appendix G.2’s concrete Forrelation witnesses. ReadSpecOneQuery explicitly labels itself a candidate awaiting native checking, so it is not silently used as a verified replacement for this budget.

- **Paper lines 3800–3804.** **Every separate enlarged ceiling and logarithmic estimate.** The exact budget, size-hypothesis budget bound, fixed-family Q bound, and constant definition are tied. No arbitrary links were added for each arithmetic sentence merely because it occurs inside a long proof.

- **Paper lines 3835–3835.** **Removing repeated queries without increasing depth.** No local standalone pruning theorem with evaluation preservation and depth monotonicity was identified. The syntactic depth definition is tied and must not be confused with this ordinary equivalence argument.

- **Paper lines 3858–3858.** **Converting arbitrary random histories or biased coins to finite tree mixtures.** Finiteness of bounded-depth trees is tied. The whole randomized-model convention comparison, including arbitrary real biases, is broader than that finiteness statement and was not assigned a fictitious single theorem.

- **Paper lines 3884–3892.** **Bare phase-oracle limitation, arbitrary projector change of basis, purification and dilation.** The one-call controlled-phase/bit identity and coordinate-projector norm identity are tied. The imported controlled-phase definition and general model comparisons are not given invented local declaration names. The paper itself disclaims a new formal purification/dilation theorem.

- **Paper lines 3974–3978.** **The entire prepended-query operator chain.** The isometry-extension lemma, oracle-compatible FixedSim invariant, and final mass identity are tied. The operator chain is implemented within FixedSim.query, but no standalone exact theorem of that displayed chain was identified.

- **Paper lines 4007–4009.** **The full one-bit D=R=Q=1 display.** The direct Q=1 declaration is linked as a partial component. The D and R values can be assembled from generic cardinality and zero-query results; no direct local combined display was identified.

- **Paper lines 4027–4033.** **D(OR_2)=2, Q(OR_2)=1, strict-threshold optimum, and nondyadic necessity.** The explicit random mixture, full success table, and R(OR_2)=1 theorem are tied. No direct local declarations for the remaining exact complexities or the full fair-coin obstruction were identified. A test of one mutated mixture would not prove the general optimum.

- **Paper lines 4038–4038.** **The direct D(trueOnly)=0 specialization.** R and Q zero have direct declarations and partial ties. D zero follows from the generic zero-query characterization and the constant-label fact, but no direct theorem for this specialization was identified.

- **Paper lines 4043–4063.** **The two-bit parity circuit, amplitudes, and exact cap complexities.** No direct local declarations for D(XOR_2)=R(XOR_2)=2 and Q(XOR_2)=1 were identified. Polynomial-degree facts about XOR do not by themselves state these three complexities. The expected-cost versus maximum-cap literature comparison is also left as an ordinary model discussion.

The opening and Appendix G omissions are specified in their section review above, including the flagged-state decomposition, literal phase-kickback calculation, expanded constructor algebra, five-value histogram and the concrete 180-gate board. The correspondence tables and bibliography at the end are provenance material.

## Exact weaker and different comparisons

This register includes **all 176 weaker or different declaration contributions** in the final ties. Each table shows the full selected paper quotation and the actual source signature or defining equation, with active section-variable excerpts where needed. Only variables used in a declaration are generalized by Lean; the excerpts are context, not additional assumed hypotheses invented for the statement. A separately highlighted proof passage is included when the tie points inside a proof. HTML escaping in the tables is only for display; the selected paper bytes are unchanged in `ties.json`.

### 1. qr-test-count-bound — weaker

Paper lines 399–402; `QuarticQuery.Paper.construction_K_count` in `QuarticQuery/Paper/ConstructionTests.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
K=2m-1+20\ell(S+2)\le(42+20A)m\ell^3.
\tag{4.10}
\]</pre></td><td><pre>theorem construction_K_count (t S : ℕ) :
    Fintype.card (TestIndex (2 * t) (40 * t) S) =
      mValue t + (mValue t - 1) + 40 * t * (S + 2)</pre></td></tr></tbody>
</table>

This declaration gives the exact count, which simplifies to the equality shown after r=20ℓ. It does not give the displayed cubic upper bound.

### 2. qr-test-count-bound — weaker

Paper lines 399–402; `QuarticQuery.Paper.construction_K_bound` in `QuarticQuery/Paper/ConstructionTests.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
K=2m-1+20\ell(S+2)\le(42+20A)m\ell^3.
\tag{4.10}
\]</pre></td><td><pre>theorem construction_K_bound (t S A : ℕ) (ht : 1 ≤ t)
    (hS : S ≤ A * mValue t * (2 * t) ^ 2) :
    Fintype.card (TestIndex (2 * t) (40 * t) S) ≤
      (42 + 20 * A) * mValue t * (2 * t) ^ 3</pre></td></tr></tbody>
</table>

This declaration gives the cubic upper bound under ht and hS. The displayed exact equality is supplied by construction_K_count.

### 3. qr-comparison-before-list — weaker

Paper lines 463–468; `QuarticQuery.Paper.quantumWinner_dominates` in `QuarticQuery/Paper/QuantumComparison.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\Pr[i^\star\text{ wins against }j]
\ \geq\ \Pr[\widehat s_{i^\star}=s_{i^\star}]
\ \geq\ 1-\varepsilon.
\tag{4.15}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

theorem quantumWinner_dominates (hk : 1 ≤ k) (ht : 1 ≤ t)
    {n : ℕ} {ε : ℝ} (hε : 0 &lt; ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n)
    {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t}
    (hw : WinsAt (P k t) C (2 * t) (40 * t) x i s)
    (j : Col t) (hji : j ≠ i) :
    1 - ε ≤ cmpProb n x i j</pre></td></tr></tbody>
</table>

The type gives the final comparison success bound 1−ε under the decoding-repetition hypothesis. It does not state the intermediate inequality against the probability of correct address decoding.

### 4. qr-comparison-table — weaker

Paper lines 501–506; `QuarticQuery.Tournament.IsComparison` in `QuarticQuery/Statement.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
0\leq a_{ij}\leq1,
\qquad a_{ij}+a_{ji}=1\quad(i\ne j),
\qquad a_{ii}=0.
\tag{5.1}
$$</pre></td><td><pre>structure Tournament.IsComparison {ι : Type} (a : ι → ι → ℝ) : Prop where
  complementary : ∀ i j, i ≠ j → a i j + a j i = 1
  self_zero : ∀ i, a i i = 0</pre></td></tr></tbody>
</table>

This structure states complementarity and the zero diagonal, but omits 0≤a_ij≤1; UnitValued supplies that clause.

### 5. qr-comparison-table — weaker

Paper lines 501–506; `QuarticQuery.Tournament.UnitValued` in `QuarticQuery/Tournament/Ideal.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
0\leq a_{ij}\leq1,
\qquad a_{ij}+a_{ji}=1\quad(i\ne j),
\qquad a_{ii}=0.
\tag{5.1}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι]

@[expose] def UnitValued (a : ι → ι → ℝ) : Prop := ∀ i j, 0 ≤ a i j ∧ a i j ≤ 1</pre></td></tr></tbody>
</table>

This predicate states only 0≤a_ij≤1; IsComparison supplies complementarity and the zero diagonal.

### 6. qr-dominant-weight-chain — weaker

Paper lines 588–593; `QuarticQuery.Paper.quantumWeight_lower` in `QuarticQuery/Paper/QuantumTournamentFacts.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
w_s(h)\geq(1-\varepsilon)^h
\geq1-h\varepsilon
\geq1-T\varepsilon
=\frac{999}{1000}&gt;\frac12.
$$</pre></td><td><pre>theorem quantumWeight_lower {Col : Type} [Fintype Col]
    {a : Col → Col → ℝ} {ε : ℝ} {s : Col} (ha : UnitValued a)
    (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) (hd : Dominant a ε s)
    {T : ℕ} (hT : (T : ℝ) * ε &lt; 1 / 2) (L : List Col)
    (hL : L.length ≤ T) (hs : s ∉ L) :
    (1 - ε) ^ L.length ≤ weight a L s ∧
    1 - (T : ℝ) * ε ≤ (1 - ε) ^ L.length ∧
    1 / 2 &lt; weight a L s ∧ 0 &lt; total (weight a L)</pre></td></tr></tbody>
</table>

The type gives (1−ε)^h≤w_s, 1−Tε≤(1−ε)^h and w_s>1/2. It does not state the intermediate 1−hε or the substitution 1−Tε=999/1000 shown here.

### 7. qr-ideal-miss — weaker

Paper lines 600–606; `QuarticQuery.Tournament.ideal_miss_le` in `QuarticQuery/Tournament/Ideal.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\Pr[s\notin L_T]
\leq\Pr[W_T\geq1/2]
\leq2\,\mathbb EW_T
\leq\frac{2m}{2^T}.
\tag{5.5}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι]
variable [DecidableEq ι]

theorem ideal_miss_le {a : ι → ι → ℝ} {ε : ℝ} {s : ι}
    (hc : IsComparison a) (ha : UnitValued a) (hε0 : 0 ≤ ε) (hε : ε ≤ 1)
    (hd : Dominant a ε s) {T : ℕ} (hT : (T : ℝ) * ε &lt; 1 / 2) :
    prob a T (fun _ l =&gt; s ∉ l) ≤ prob a T (fun w _ =&gt; 1 / 2 ≤ total w) ∧
      prob a T (fun w _ =&gt; 1 / 2 ≤ total w) ≤ 2 * (Fintype.card ι : ℝ) / 2 ^ T</pre></td></tr></tbody>
</table>

The theorem states absence≤Pr[W_T≥1/2]≤2m/2^T. The intermediate Pr[W_T≥1/2]≤2 E W_T is used in its proof, not exposed in its type.

### 8. qr-decode-cost-and-accuracy — weaker

Paper lines 700–706; `QuarticQuery.Paper.quantumDecode_query_bound_real` in `QuarticQuery/Paper/QuantumComparison.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\text{address-decoding queries}
=O_k\!\left(r\ln(r/\varepsilon)\right),
\qquad
\Pr[\text{correct address}]\geq1-\varepsilon
\quad\text{if all }r\text{ promises hold}.
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

theorem quantumDecode_query_bound_real (ht : 1 ≤ t) {ε : ℝ}
    (hε : 0 &lt; ε) (hε1 : ε ≤ 1) :
    ((2 * addrCost k t (repetitions k (ε / (40 * t : ℕ))) : ℕ) : ℝ) ≤
      80 * (t : ℝ) * (k : ℝ) *
        (1 + 16 * (2 : ℝ) ^ (10 * k) * Real.log ((40 * t : ℕ) / ε))</pre></td></tr></tbody>
</table>

This theorem bounds the physical decoder budget but does not assert promised accuracy; quantumDecode_correct supplies that separate clause.

### 9. qr-decode-cost-and-accuracy — weaker

Paper lines 700–706; `QuarticQuery.Paper.quantumDecode_correct` in `QuarticQuery/Paper/QuantumComparison.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\text{address-decoding queries}
=O_k\!\left(r\ln(r/\varepsilon)\right),
\qquad
\Pr[\text{correct address}]\geq1-\varepsilon
\quad\text{if all }r\text{ promises hold}.
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

theorem quantumDecode_correct (hk : 1 ≤ k) (ht : 1 ≤ t)
    {n : ℕ} {ε : ℝ} (hε : 0 &lt; ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n)
    {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t}
    (hs : ∀ h, P k t (readA x i h) = some (s h)) :
    1 - ε ≤ addrLaw n x i s</pre></td></tr></tbody>
</table>

This theorem gives the correct-address probability under hs and hn, but not the displayed logarithmic query bound.

### 10. qr-verifier-count — weaker

Paper lines 744–746; `QuarticQuery.Paper.construction_K_count` in `QuarticQuery/Paper/ConstructionTests.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3).
$$</pre></td><td><pre>theorem construction_K_count (t S : ℕ) :
    Fintype.card (TestIndex (2 * t) (40 * t) S) =
      mValue t + (mValue t - 1) + 40 * t * (S + 2)</pre></td></tr></tbody>
</table>

The type gives the exact cardinality. It does not give the O_k(mℓ³) bound in this display; construction_K_bound supplies that bound under the circuit-size hypothesis.

### 11. qr-verifier-count — weaker

Paper lines 744–746; `QuarticQuery.Paper.construction_K_bound` in `QuarticQuery/Paper/ConstructionTests.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3).
$$</pre></td><td><pre>theorem construction_K_bound (t S A : ℕ) (ht : 1 ≤ t)
    (hS : S ≤ A * mValue t * (2 * t) ^ 2) :
    Fintype.card (TestIndex (2 * t) (40 * t) S) ≤
      (42 + 20 * A) * mValue t * (2 * t) ^ 3</pre></td></tr></tbody>
</table>

The type gives the cubic logarithmic upper bound under hS, but does not state the exact test-count equality in this display.

### 12. qr-full-algorithm-errors — weaker

Paper lines 776–782; `QuarticQuery.Paper.quantumError_bound` in `QuarticQuery/Paper/QuantumComparison.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{aligned}
\Pr_x[\text{error}]&amp;\leq T\varepsilon &amp;&amp;\text{for every }x\text{ with }F_{k,m}(x)=0,\\
\Pr_x[\text{error}]&amp;\leq\frac{2m}{2^T}+T\varepsilon+\varepsilon&lt;\frac13
&amp;&amp;\text{for every }x\text{ with }F_{k,m}(x)=1.
\end{aligned}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

theorem quantumError_bound (hk : 1 ≤ k) (ht : 1 ≤ t)
    (hC : CircuitRealises C (P k t)) {n : ℕ}
    (hn : repetitions k (epsval (mValue t) / (40 * t : ℕ)) ≤ n) :
    ∃ val : BitInput (Loc k t C) → ℝ,
      Runs (budget k t n (Fintype.card (Tests t C)))
        (fun x b =&gt; bern (val x) b) ∧
      (∀ x, Fkm k t C x = false →
        val x ≤ (Tval (mValue t) : ℝ) * epsval (mValue t)) ∧
      (∀ x, Fkm k t C x = true →
        1 - val x ≤ 2 * (mValue t : ℝ) / 2 ^ Tval (mValue t) +
          (Tval (mValue t) : ℝ) * epsval (mValue t) + epsval (mValue t))</pre></td></tr></tbody>
</table>

The declaration gives both zero-input and one-input probability bounds, but omits the final strict comparison with 1/3; quantumError_numeric supplies it.

### 13. qr-full-algorithm-errors — weaker

Paper lines 776–782; `QuarticQuery.Paper.quantumError_numeric` in `QuarticQuery/Paper/QuantumComparison.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{aligned}
\Pr_x[\text{error}]&amp;\leq T\varepsilon &amp;&amp;\text{for every }x\text{ with }F_{k,m}(x)=0,\\
\Pr_x[\text{error}]&amp;\leq\frac{2m}{2^T}+T\varepsilon+\varepsilon&lt;\frac13
&amp;&amp;\text{for every }x\text{ with }F_{k,m}(x)=1.
\end{aligned}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

theorem quantumError_numeric {m : ℕ} (hm : 2 ≤ m) :
    (Tval m : ℝ) * epsval m = 1 / 1000 ∧
    2 * (m : ℝ) / 2 ^ Tval m + (Tval m : ℝ) * epsval m + epsval m &lt; 1 / 3</pre></td></tr></tbody>
</table>

The declaration gives only Tε=1/1000 and the numeric bound below 1/3; the input-dependent probability inequalities are in quantumError_bound.

### 14. rec-cl-mplusone-ingredient — weaker

Paper lines 961–966; `QuarticQuery.zero_search_sum_successor` in `QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb EZ\le\frac{2}{m+1}\mathbb E Q_X,
\qquad
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
\le\frac{2G}{m(m+1)}.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι α : Type} [DecidableEq α]

theorem zero_search_sum_successor (e : α → ι) (he : Function.Injective e) (c : ι → Bool)
    (hc1 : ∀ p, c (e p) = true) (hc2 : ∀ q, c q = true → ∃ p, e p = q)
    (x : α → BitInput ι) (hout : ∀ j j' q, c q = false → x j q = x j' q)
    (hin : ∀ j p, x j (e p) = decide (p ≠ j)) (T : QueryTree ι) (U : Finset α) :
    ((U.card : ℝ) + 1) * ∑ j ∈ U, ind (e j ∈ T.path (x j)) ≤
      2 * ∑ j ∈ U, ((T.path (x j)).countP c : ℝ)</pre></td></tr></tbody>
</table>

This theorem proves the one-column inequality (|U|+1)D_U ≤ 2Q_U. It does not state either averaged bound on EZ or selected-column hit probability; those require averaging and the independent-selection identity.

### 15. rec-cl-per-input-cap — different

Paper lines 991–992; `QuarticQuery.OutTree.capped` in `QuarticQuery/LowerBound/DirectProduct.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>If it makes at most $L$ queries to each input on every
run, counting repeated queries</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]

def OutTree.capped {r : ℕ} {β : Type} :
    OutTree (Fin r × κ) β → (Fin r → ℕ) → Prop
  | .leaf _, _ =&gt; True
  | .query p l u, c =&gt; 0 &lt; c p.1 ∧
      l.capped (Function.update c p.1 (c p.1 - 1)) ∧
      u.capped (Function.update c p.1 (c p.1 - 1))</pre></td></tr></tbody>
</table>

OutTree.capped requires the allowance on every syntactic branch, including inconsistent repeated-answer branches. The quoted prose constrains executions; the source does not prove these two formulations equivalent for an arbitrary tree.

### 16. rec-cl-separate-cap-product — weaker

Paper lines 995–999; `QuarticQuery.Paper.classical_direct_product_average` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Pr\!\left[\mathcal A(U_1,\ldots,U_r)
       =\bigl(P(U_1),\ldots,P(U_r)\bigr)\right]\leq\beta^r.
\tag{6.3}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem classical_direct_product_average {S : Type} [Fintype S]
    {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ} {β : ℝ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : classicalMass μ = 1)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ β)
    {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) (hp1 : ∑ s, p s = 1)
    (T : S → OutTree (Fin r × κ) (Fin r → Bool))
    (hT : ∀ s, (T s).capped fun _ =&gt; L) :
    ∑ s, p s * guessSuccess f (fun _ =&gt; μ) (T s) ≤ β ^ r</pre></td></tr></tbody>
</table>

The theorem assumes a finite seed type S ([Fintype S]) and a structural cap on every syntactic branch. The paper permits unrestricted independent advice and coins and states the cap for executions; transfer to these broader formulations is not in this theorem type.

### 17. rec-cl-whole-address-guess — weaker

Paper lines 1009–1011; `QuarticQuery.address_guess_average` in `QuarticQuery/LowerBound/Minimax.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Pr[\widehat s=(P(U_1),\ldots,P(U_r))]\le(2/3)^r.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type}
variable [Fintype κ] [DecidableEq κ]

theorem address_guess_average {S : Type} [Fintype S] {f : PartialBool κ} {μ : BitInput κ → ℝ}
    {L r : ℕ} (hμ : ∀ x, 0 ≤ μ x)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ 2 / 3)
    {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) (hp1 : ∑ s, p s = 1)
    (T : S → OutTree (Fin r × κ) (Fin r → Bool)) (hT : ∀ s, (T s).capped fun _ =&gt; L) :
    ∑ s, p s * guessSuccess f (fun _ =&gt; μ) (T s) ≤ (2 / 3) ^ r</pre></td></tr></tbody>
</table>

The Lean endpoint quantifies over finite mixtures of capped predictors; the surrounding application of Lemma 6.1 permits an unrestricted independent seed.

### 18. rec-cl-simulator-replay — weaker

Paper lines 1049–1049; `QuarticQuery.eval_simTree` in `QuarticQuery/LowerBound/Planted/Simulator.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The replay therefore agrees up to time $q$ and outputs $s_i$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι ρ β : Type}
variable {tgt : ι → Option ρ} {guess : ι → Option β} {dflt : β} {base : BitInput ι}

theorem eval_simTree (x : BitInput ι) (V : BitInput ρ)
    (hbase : ∀ q, tgt q = none → x q = base q) (hV : ∀ q p, tgt q = some p → x q = V p)
    (T : QueryTree ι) (t c : ℕ) {q : ι} {s : β} (hq : (T.path x)[t]? = some q)
    (hs : guess q = some s)
    (hc : ((T.path x).take t).countP (fun q =&gt; (tgt q).isSome) ≤ c) :
    (simTree tgt guess dflt base T t c).eval V = s</pre></td></tr></tbody>
</table>

The theorem concludes equality of the output with the proposed address under matching-answer and prefix-count premises. It does not itself assert equality of the complete replay history.

### 19. rec-cl-weighted-optimum — weaker

Paper lines 1099–1100; `QuarticQuery.exists_tree_budgetValue_le` in `QuarticQuery/LowerBound/DirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Induction on depth shows that $W_c(\nu)$ is the maximum weighted success
of a tree of depth at most $c$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]

theorem exists_tree_budgetValue_le (f : PartialBool κ) (c : ℕ) (ν : BitInput κ → ℝ) :
    ∃ T : QueryTree κ, T.depth ≤ c ∧ budgetValue f c ν ≤ treeSuccess f ν T</pre></td></tr></tbody>
</table>

This declaration constructs a depth-c tree with success at least W_c. The upper bound for all trees is the separate treeSuccess_le_budgetValue declaration.

### 20. rec-cl-weighted-optimum — weaker

Paper lines 1099–1100; `QuarticQuery.treeSuccess_le_budgetValue` in `QuarticQuery/LowerBound/DirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Induction on depth shows that $W_c(\nu)$ is the maximum weighted success
of a tree of depth at most $c$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]

theorem treeSuccess_le_budgetValue (f : PartialBool κ) {c : ℕ} (ν : BitInput κ → ℝ)
    {T : QueryTree κ} (hT : T.depth ≤ c) : treeSuccess f ν T ≤ budgetValue f c ν</pre></td></tr></tbody>
</table>

This declaration bounds every depth-c tree by W_c. Attainment, the other half of being a maximum, is supplied by exists_tree_budgetValue_le.

### 21. rec-cl-independent-seed-average — weaker

Paper lines 1142–1142; `QuarticQuery.Paper.classical_direct_product_average` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Finally average the bound over the coins and outside information.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem classical_direct_product_average {S : Type} [Fintype S]
    {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ} {β : ℝ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : classicalMass μ = 1)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ β)
    {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) (hp1 : ∑ s, p s = 1)
    (T : S → OutTree (Fin r × κ) (Fin r → Bool))
    (hT : ∀ s, (T s).capped fun _ =&gt; L) :
    ∑ s, p s * guessSuccess f (fun _ =&gt; μ) (T s) ≤ β ^ r</pre></td></tr></tbody>
</table>

The theorem averages over a finite seed type S. The paper’s unqualified independent outside information and coins allow more general random sources.

### 22. rec-cl-tail-display — weaker

Paper lines 1180–1183; `QuarticQuery.Paper.classical_tail_le` in `QuarticQuery/Paper/ClassicalAsymptotics.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
G(2/3)^r\le\tfrac1{100}m^{2-20\log_2(3/2)}
\le\tfrac1{100}m^{-8}.
\]</pre></td><td><pre>theorem classical_tail_le (t : ℕ) {G : ℝ}
    (hG : G ≤ (mValue t : ℝ) ^ 2 / 100) :
    G * ((2 : ℝ) / 3) ^ (40 * t) ≤
      (1 / 100 : ℝ) *
        (mValue t : ℝ) ^ (2 - 20 * Real.logb 2 ((3 : ℝ) / 2))</pre></td></tr></tbody>
</table>

The Lean theorem gives G(2/3)^(40t) ≤ m^(2−20 log₂(3/2))/100. It does not include the displayed further inequality ≤ m^(−8)/100.

### 23. rec-cl-contradiction — weaker

Paper lines 1193–1193; `QuarticQuery.addressedF_not_RLe` in `QuarticQuery/LowerBound/Planted/Main.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Since no algorithm of budget \(G\) exists, \(R(F_{P,C,m})&gt;G\), which proves the generic theorem.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ] {ℓ r S : ℕ}

theorem addressedF_not_RLe (f : PartialBool κ) (C : Circuit κ) (hC : CircuitRealises C f)
    {ℓ r L G : ℕ} (hL : ¬ RLe f L) (hL1 : 1 ≤ L)
    (hdisc : 4 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 + (G : ℝ) / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) +
      (G : ℝ) * ((2 : ℝ) / 3) ^ r &lt; 1 / 3) :
    ¬ RLe (totalise (addressedF f C ℓ r)) G</pre></td></tr></tbody>
</table>

The theorem concludes ¬ RLe F G under a discrepancy premise. The conversion to the numeric minimum R(F)>G is supplied by Gvalue_lt_R_addressedF and the finite-minimum lemmas, not by this declaration alone.

### 24. rec-cl-power-beats-log — weaker

Paper lines 1288–1288; `QuarticQuery.Paper.classical_power_log_tendsto` in `QuarticQuery/Paper/ClassicalAsymptotics.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The numerator is a positive power of $m$ and the denominator a fixed power of $\log_2m$, so the quotient tends to infinity.</pre></td><td><pre>theorem classical_power_log_tendsto {d δ e : ℝ} (hd : 0 &lt; d) (hδ : 0 &lt; δ) :
    Tendsto (fun t : ℕ =&gt; d * (mValue t : ℝ) ^ δ /
      Real.logb 2 (mValue t : ℝ) ^ e) atTop atTop</pre></td></tr></tbody>
</table>

This theorem proves divergence of the scalar lower bound d m^δ/(log₂m)^e. It does not itself state divergence of the query-complexity quotient; classical_Fkm_ratio supplies that conclusion.

### 25. fr-walsh-objects — weaker

Paper lines 1352–1352; `QuarticQuery.Forrelation.W` in `QuarticQuery/Forrelation/Walsh.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$, and $D_z=\operatorname{diag}(z)$.</pre></td><td><pre>noncomputable def W (t : ℕ) : Matrix (Fin (mValue t)) (Fin (mValue t)) ℝ :=
  (walshZ t).map (Int.castRingHom ℝ)</pre></td></tr></tbody>
</table>

This definition supplies the unnormalized matrix W; the selected sentence defines four objects. The other three objects have separate definition links.

### 26. fr-walsh-objects — weaker

Paper lines 1352–1352; `QuarticQuery.Forrelation.H` in `QuarticQuery/Forrelation/Walsh.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$, and $D_z=\operatorname{diag}(z)$.</pre></td><td><pre>noncomputable def H (t : ℕ) : Matrix (Fin (mValue t)) (Fin (mValue t)) ℝ :=
  ((2 : ℝ) ^ t)⁻¹ • W t</pre></td></tr></tbody>
</table>

This definition supplies the normalized matrix H; the selected sentence defines four objects. The other three objects have separate definition links.

### 27. fr-walsh-objects — weaker

Paper lines 1352–1352; `QuarticQuery.Forrelation.u` in `QuarticQuery/Forrelation/Product.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$, and $D_z=\operatorname{diag}(z)$.</pre></td><td><pre>noncomputable def u (t : ℕ) : Fin (mValue t) → ℝ := fun _ =&gt; ((2 : ℝ) ^ t)⁻¹</pre></td></tr></tbody>
</table>

This definition supplies the uniform vector u; the selected sentence defines four objects. The other three objects have separate definition links.

### 28. fr-walsh-objects — weaker

Paper lines 1352–1352; `QuarticQuery.Forrelation.signDiag` in `QuarticQuery/Forrelation/Product.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$, and $D_z=\operatorname{diag}(z)$.</pre></td><td><pre>noncomputable def signDiag {k t : ℕ} (z : BitInput (ForrelationCoord k t)) (h : Fin k) :
    Matrix (Fin (mValue t)) (Fin (mValue t)) ℝ :=
  Matrix.diagonal fun i =&gt; (bitSign (z (h, i)) : ℝ)</pre></td></tr></tbody>
</table>

This definition supplies the sign diagonal D_z; the selected sentence defines four objects. The other three objects have separate definition links.

### 29. fr-normalization-identities — weaker

Paper lines 1357–1360; `QuarticQuery.Forrelation.W_mul_transpose` in `QuarticQuery/Forrelation/Walsh.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
$$</pre></td><td><pre>theorem W_mul_transpose (t : ℕ) :
    W t * (W t)ᵀ = (mValue t : ℝ) • (1 : Matrix _ _ ℝ)</pre></td></tr></tbody>
</table>

This declaration supplies only WWᵀ=mI. The complete selected display also asserts the other matrix and vector normalization identities, which are separate declarations.

### 30. fr-normalization-identities — weaker

Paper lines 1357–1360; `QuarticQuery.Forrelation.H_transpose` in `QuarticQuery/Forrelation/Walsh.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
$$</pre></td><td><pre>theorem H_transpose (t : ℕ) : (H t)ᵀ = H t</pre></td></tr></tbody>
</table>

This declaration supplies only Hᵀ=H. The complete selected display also asserts the other matrix and vector normalization identities, which are separate declarations.

### 31. fr-normalization-identities — weaker

Paper lines 1357–1360; `QuarticQuery.Forrelation.H_mul_H` in `QuarticQuery/Forrelation/Walsh.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
$$</pre></td><td><pre>theorem H_mul_H (t : ℕ) : H t * H t = 1</pre></td></tr></tbody>
</table>

This declaration supplies only H²=I. The complete selected display also asserts the other matrix and vector normalization identities, which are separate declarations.

### 32. fr-normalization-identities — weaker

Paper lines 1357–1360; `QuarticQuery.Forrelation.u_dot_self` in `QuarticQuery/Forrelation/Product.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n]

theorem u_dot_self (t : ℕ) : u t ⬝ᵥ u t = 1</pre></td></tr></tbody>
</table>

This declaration supplies only ‖u‖₂=1, expressed as u·u=1. The complete selected display also asserts the other matrix and vector normalization identities, which are separate declarations.

### 33. fr-normalization-identities — weaker

Paper lines 1357–1360; `QuarticQuery.Forrelation.isOrth_signDiag` in `QuarticQuery/Forrelation/Product.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n]

theorem isOrth_signDiag {k t : ℕ} (z : BitInput (ForrelationCoord k t)) (h : Fin k) :
    IsOrth (signDiag z h)</pre></td></tr></tbody>
</table>

This declaration supplies only D_zᵀD_z=I. The complete selected display also asserts the other matrix and vector normalization identities, which are separate declarations.

### 34. fr-forrelation-overlap — weaker

Paper lines 1365–1368; `QuarticQuery.Forrelation.Phi_eq_matrix_product` in `QuarticQuery/Forrelation/Product.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Phi(z)=u^{\mathsf T}D_{z_0}H\cdots H D_{z_{k-1}}u,\qquad \delta=32^{-k}.
\tag{8.1}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n]

theorem Phi_eq_matrix_product (k t : ℕ) (hk : 1 ≤ k) (z : BitInput (ForrelationCoord k t)) :
    Phi k t z = u t ⬝ᵥ
      (alternate (H t) (List.ofFn fun h : Fin k =&gt; signDiag z h) *ᵥ u t)</pre></td></tr></tbody>
</table>

The theorem states the matrix-overlap identity for Φ under k≥1. The selected display also defines δ=32^{-k}; that threshold is supplied by the separate delta definition.

### 35. fr-forrelation-overlap — weaker

Paper lines 1365–1368; `QuarticQuery.Forrelation.delta` in `QuarticQuery/Forrelation/Promise.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Phi(z)=u^{\mathsf T}D_{z_0}H\cdots H D_{z_{k-1}}u,\qquad \delta=32^{-k}.
\tag{8.1}
\]</pre></td><td><pre>noncomputable def delta (k : ℕ) : ℝ := (2 : ℝ) ^ (-(5 * (k : ℤ)))</pre></td></tr></tbody>
</table>

This definition gives δ=2^{-5k}=32^{-k}. It does not state the matrix identity for Φ that occupies the other half of the selected display.

### 36. fr-explicit-threshold-scope — weaker

Paper lines 1386–1386; `QuarticQuery.lvalue_lt_R_explicit` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The proof gives the sufficient choice $t_0(k)=13669k^2$.</pre></td><td><pre>theorem lvalue_lt_R_explicit (k t : ℕ) (hk : 2 ≤ k) (ht : 3499200 * k ^ 2 ≤ t) :
    Lvalue k t &lt; R (P k t)</pre></td></tr></tbody>
</table>

The paper gives t₀(k)=13669k². The named theorem instead assumes ht : 3499200 * k ^ 2 ≤ t. It proves the desired floor conclusion only above that larger sufficient threshold; the sharp uniform supplier is linked separately.

### 37. fr-probability-weights — weaker

Paper lines 1419–1419; `QuarticQuery.ForrelationLower.bw_nonneg` in `QuarticQuery/ForrelationLower/Cube.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For $|\mu_i|\le1$ the weights are nonnegative and sum to one</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]

theorem bw_nonneg {μ : ι → ℝ} (h : ∀ a, |μ a| ≤ 1) (z : ι → Bool) : 0 ≤ bw μ z</pre></td></tr></tbody>
</table>

The theorem gives nonnegative weights when every |μᵢ|≤1. The selected phrase also says that their sum is one; that separate claim is supplied by sum_bw.

### 38. fr-probability-weights — weaker

Paper lines 1419–1419; `QuarticQuery.ForrelationLower.sum_bw` in `QuarticQuery/ForrelationLower/Cube.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For $|\mu_i|\le1$ the weights are nonnegative and sum to one</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]

theorem sum_bw (μ : ι → ℝ) : ∑ z, bw μ z = 1</pre></td></tr></tbody>
</table>

The theorem states that the weights sum to one, even for arbitrary real biases. It does not establish the nonnegativity also asserted by the selected phrase.

### 39. fr-coordinate-affinity — weaker

Paper lines 1419–1419; `QuarticQuery.ForrelationLower.ext_affine` in `QuarticQuery/ForrelationLower/Cube.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For arbitrary real $\mu$, the same finite sum defines a polynomial that is affine in each coordinate.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]

theorem ext_affine (a : ι) (g : (ι → Bool) → ℝ) (μ : ι → ℝ) :
    ext g μ = ext g (Function.update μ a 0) + μ a * ext (D a g) μ</pre></td></tr></tbody>
</table>

The source statement gives the exact one-coordinate affine decomposition for arbitrary real μ. It does not separately assert that the full multivariate function is a polynomial, as the selected sentence also does.

### 40. fr-extension-derivative-identities — weaker

Paper lines 1430–1435; `QuarticQuery.ForrelationLower.hasDerivAt_ext` in `QuarticQuery/ForrelationLower/Cube.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\partial_i F_g(\mu)=F_{\partial_i g}(\mu),\qquad
\partial_i^2F_g=0,\qquad
\partial_i\partial_jF_g=\partial_j\partial_iF_g.
\tag{8.5}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]

theorem hasDerivAt_ext (g : (ι → Bool) → ℝ) {c : ℝ → ι → ℝ} {c' : ι → ℝ} {t : ℝ}
    (hc : ∀ a, HasDerivAt (fun s =&gt; c s a) (c' a) t) :
    HasDerivAt (fun s =&gt; ext g (c s)) (∑ a, c' a * ext (D a g) (c t)) t</pre></td></tr></tbody>
</table>

The theorem gives the chain rule for differentiable bias paths, yielding the first partial-derivative identity by a one-coordinate path. It does not state the repeated-derivative zero identity or commutation of distinct partials in the same selected display.

### 41. fr-extension-derivative-identities — weaker

Paper lines 1430–1435; `QuarticQuery.ForrelationLower.D_D` in `QuarticQuery/ForrelationLower/Cube.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\partial_i F_g(\mu)=F_{\partial_i g}(\mu),\qquad
\partial_i^2F_g=0,\qquad
\partial_i\partial_jF_g=\partial_j\partial_iF_g.
\tag{8.5}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]

theorem D_D (a : ι) (g : (ι → Bool) → ℝ) : D a (D a g) = fun _ =&gt; 0</pre></td></tr></tbody>
</table>

The theorem states that the repeated same-coordinate discrete derivative is zero. Combined with the extension derivative identity this supplies the second clause, but it does not state the first clause or the commutation clause.

### 42. fr-derivative-moment — weaker

Paper lines 1453–1461; `QuarticQuery.ForrelationLower.ext_Dl` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\partial_JF_g(\mu)
=\mathcal E_\mu\!\left[g(z)\prod_{i\in J}\xi_i(z_i)\right],
\qquad
\mathcal E_\mu\xi_i=0,
\qquad
|\mu_i|\le\tfrac12\ \Longrightarrow\ |\xi_i|\le2.
\tag{8.6}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem ext_Dl (L : List ι) (hL : L.Nodup) (g : (ι → Bool) → ℝ) (μ : ι → ℝ)
    (hμ : ∀ a, |μ a| &lt; 1) :
    ext (Dl L g) μ = ext (fun z =&gt; g z * (L.map fun a =&gt; xi μ a (z a)).prod) μ</pre></td></tr></tbody>
</table>

Under distinct derivative coordinates and |μᵢ|<1, the theorem gives the mixed-derivative expectation identity. It does not state the separate centering or magnitude-two assertions in the selected display.

### 43. fr-derivative-moment — weaker

Paper lines 1453–1461; `QuarticQuery.ForrelationLower.xi_mean` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\partial_JF_g(\mu)
=\mathcal E_\mu\!\left[g(z)\prod_{i\in J}\xi_i(z_i)\right],
\qquad
\mathcal E_\mu\xi_i=0,
\qquad
|\mu_i|\le\tfrac12\ \Longrightarrow\ |\xi_i|\le2.
\tag{8.6}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem xi_mean {μ : ι → ℝ} (hμ : ∀ a, |μ a| ≤ 1 / 2) (a : ι) :
    piB (μ a) false * xi μ a false + piB (μ a) true * xi μ a true = 0</pre></td></tr></tbody>
</table>

The paper introduces centering under |μᵢ|<1. The named centering lemma assumes hμ : ∀ a, |μ a| ≤ 1/2, the narrower bias range used later.

### 44. fr-derivative-moment — weaker

Paper lines 1453–1461; `QuarticQuery.ForrelationLower.abs_xi_le` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\partial_JF_g(\mu)
=\mathcal E_\mu\!\left[g(z)\prod_{i\in J}\xi_i(z_i)\right],
\qquad
\mathcal E_\mu\xi_i=0,
\qquad
|\mu_i|\le\tfrac12\ \Longrightarrow\ |\xi_i|\le2.
\tag{8.6}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem abs_xi_le {μ : ι → ℝ} (hμ : ∀ a, |μ a| ≤ 1 / 2) (a : ι) (b : Bool) : |xi μ a b| ≤ 2</pre></td></tr></tbody>
</table>

The theorem proves only |ξᵢ|≤2 under |μᵢ|≤1/2. It does not give either the mixed-derivative identity or the centering identity in the selected display.

### 45. fr-gaussian-functions — weaker

Paper lines 1479–1484; `QuarticQuery.ForrelationLower.qf` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
q(x)=\sqrt{2+x^2},\qquad
\Psi(x)=\frac1{2q(x)},\qquad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3}.
\tag{8.7}
\]</pre></td><td><pre>noncomputable def qf (x : ℝ) : ℝ := Real.sqrt (2 + x ^ 2)</pre></td></tr></tbody>
</table>

This definition supplies q(x)=√(2+x²). The selected display introduces three functions; the other definitions are separate links.

### 46. fr-gaussian-functions — weaker

Paper lines 1479–1484; `QuarticQuery.ForrelationLower.psiS` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
q(x)=\sqrt{2+x^2},\qquad
\Psi(x)=\frac1{2q(x)},\qquad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3}.
\tag{8.7}
\]</pre></td><td><pre>noncomputable def psiS (x : ℝ) : ℝ := 1 / (2 * qf x)</pre></td></tr></tbody>
</table>

This definition supplies Ψ(x)=1/(2q(x)). The selected display introduces three functions; the other definitions are separate links.

### 47. fr-gaussian-functions — weaker

Paper lines 1479–1484; `QuarticQuery.ForrelationLower.phiS` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
q(x)=\sqrt{2+x^2},\qquad
\Psi(x)=\frac1{2q(x)},\qquad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3}.
\tag{8.7}
\]</pre></td><td><pre>noncomputable def phiS (x : ℝ) : ℝ := x * (3 + x ^ 2) / (2 * qf x ^ 3)</pre></td></tr></tbody>
</table>

This definition supplies φ(x)=x(3+x²)/(2q(x)³). The selected display introduces three functions; the other definitions are separate links.

### 48. fr-gaussian-derivatives — weaker

Paper lines 1488–1493; `QuarticQuery.ForrelationLower.hasDerivAt_phiS` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\varphi'(x)=\frac3{q(x)^5},\qquad
\Psi'(x)=-\frac{x}{2q(x)^3},\qquad
\varphi=x\Psi-\Psi'.
\tag{8.8}
\]</pre></td><td><pre>theorem hasDerivAt_phiS (x : ℝ) : HasDerivAt phiS (dphi x) x</pre></td></tr></tbody>
</table>

The theorem states only φ′(x)=3/q(x)^5. The selected display also states the derivative of Ψ and the identity φ=xΨ−Ψ′.

### 49. fr-gaussian-derivatives — weaker

Paper lines 1488–1493; `QuarticQuery.ForrelationLower.hasDerivAt_psiS` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\varphi'(x)=\frac3{q(x)^5},\qquad
\Psi'(x)=-\frac{x}{2q(x)^3},\qquad
\varphi=x\Psi-\Psi'.
\tag{8.8}
\]</pre></td><td><pre>theorem hasDerivAt_psiS (x : ℝ) : HasDerivAt psiS (-x / (2 * qf x ^ 3)) x</pre></td></tr></tbody>
</table>

The theorem states only Ψ′(x)=−x/(2q(x)^3). The selected display also states the derivative of φ and the identity φ=xΨ−Ψ′.

### 50. fr-rounding-odd-bounded — weaker

Paper lines 1495–1495; `QuarticQuery.ForrelationLower.phiS_neg` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The function $\varphi$ is odd and $|\varphi|\le1/2$</pre></td><td><pre>theorem phiS_neg (x : ℝ) : phiS (-x) = - phiS x</pre></td></tr></tbody>
</table>

This theorem gives oddness, φ(−x)=−φ(x). The selected phrase also asserts the bound |φ|≤1/2, supplied by abs_phiS_le.

### 51. fr-rounding-odd-bounded — weaker

Paper lines 1495–1495; `QuarticQuery.ForrelationLower.abs_phiS_le` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The function $\varphi$ is odd and $|\varphi|\le1/2$</pre></td><td><pre>theorem abs_phiS_le (x : ℝ) : |phiS x| ≤ 1 / 2</pre></td></tr></tbody>
</table>

This theorem gives |φ(x)|≤1/2. The selected phrase also asserts oddness, supplied by phiS_neg.

### 52. fr-sharp-edge-bound — weaker

Paper lines 1504–1509; `QuarticQuery.ForrelationLower.psi_dphi_le_sharp` in `QuarticQuery/ForrelationLower/Stein.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
0&lt;\Psi(x)\varphi'(y)
=\frac{3}{2\sqrt{2+x^2}(2+y^2)^{5/2}}
\le\frac3{16}.
\tag{8.9}
\]</pre></td><td><pre>theorem psi_dphi_le_sharp (x y : ℝ) : psiS x * dphi y ≤ 3 / 16</pre></td></tr></tbody>
</table>

The theorem states the upper inequality Ψ(x)φ′(y)≤3/16. The selected display additionally asserts strict positivity and an explicit product formula; those are not conjuncts of this theorem’s type.

### 53. fr-bias-range — weaker

Paper lines 1569–1569; `QuarticQuery.ForrelationLower.abs_wv_le_half` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The endpoint coordinates have bias of magnitude at most $1/2$ and the middle coordinates at most $1/4$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)

theorem abs_wv_le_half (hl : 1 ≤ l) {s : ℝ} (hs : |s| ≤ 1) (u : PC l n → ℝ) (c : BC l n) :
    |wv H s u c| ≤ 1 / 2</pre></td></tr></tbody>
</table>

The selected sentence distinguishes endpoint |w|≤1/2 and interior |w|≤1/4. The theorem proves |w|≤1/2 for every coordinate under l≥1 and |s|≤1; it does not state the sharper interior bound.

### 54. fr-interpolation-derivative — weaker

Paper lines 1595–1599; `QuarticQuery.ForrelationLower.hasDerivAt_ext_s` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
h_g'(s)=\sum_a\mathbb E_U
\left[X_0(a)\,\partial_{(0,a)}F_g(w_s(U))\right].
\tag{8.15}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)

theorem hasDerivAt_ext_s (g : (BC l n → Bool) → ℝ) (u : PC l n → ℝ) (s : ℝ) (hl : 0 &lt; l) :
    HasDerivAt (fun s =&gt; ext g (wv H s u))
      (∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s u)) s</pre></td></tr></tbody>
</table>

This theorem differentiates F_g(w_s(U)) for fixed U. Equation (8.15) differentiates its Gaussian average. The latter interchange is proved separately inside exists_identity for 0<s<1.

### 55. fr-interpolation-derivative — weaker

Paper lines 1595–1599; `QuarticQuery.ForrelationLower.exists_identity` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
h_g'(s)=\sum_a\mathbb E_U
\left[X_0(a)\,\partial_{(0,a)}F_g(w_s(U))\right].
\tag{8.15}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)

theorem exists_identity (hl : 0 &lt; l) (g : (BC l n → Bool) → ℝ) :
    ∃ s ∈ Set.Ioo (0 : ℝ) 1,
      ∫ u, ext g (wv H 1 u) ∂(gP (PC l n)) - ∫ u, ext g (wv H 0 u) ∂(gP (PC l n)) =
        ∑ a, ∫ u, Int H s l 0 a (D (cn 0 a) g) u ∂(gP (PC l n))

Selected proof passage:
  have hderiv : ∀ s ∈ Set.Ioo (0 : ℝ) 1, HasDerivAt h
      (∑ a, ∫ u, Int H s l 0 a (D (cn 0 a) g) u ∂(gP (PC l n))) s := by
    intro s hs
    have hs1 : |s| ≤ 1 := abs_le.mpr ⟨by linarith [hs.1], hs.2.le⟩
    have hBd : ∀ s' ∈ Set.Ioo (0 : ℝ) 1, ∀ u : PC l n → ℝ,
        ‖∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s' u)‖ ≤ Fintype.card n * B := by
      intro s' hs' u
      have hs1' : |s'| ≤ 1 := abs_le.mpr ⟨by linarith [hs'.1], hs'.2.le⟩
      calc _ ≤ ∑ _a : n, B := by
            refine (norm_sum_le _ _).trans (sum_le_sum fun a _ =&gt; ?_)
            rw [Real.norm_eq_abs, abs_mul]
            have h1 := abs_Xf_le u 0 a
            have h2 : |ext (D (cn 0 a) g) (wv H s' u)| ≤ B :=
              abs_ext_le (abs_D_le hB _) fun c =&gt; abs_wv_le H hs1' u c
            nlinarith [abs_nonneg (Xf u 0 a), abs_nonneg (ext (D (cn 0 a) g) (wv H s' u))]
        _ = _ := by simp
    have := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := gP (PC l n))
      (F := fun s u =&gt; ext g (wv H s u))
      (F' := fun s u =&gt; ∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s u))
      (bound := fun _ =&gt; Fintype.card n * B) (x₀ := s) (s := Set.Ioo 0 1)
      (Ioo_mem_nhds hs.1 hs.2)
      (.of_forall fun s' =&gt; ((continuous_ext g).comp
        (continuous_pi fun c =&gt; continuous_wv H s' c)).aestronglyMeasurable)
      (bcf_ext H g hs1).integrable
      (BCf.sum _ fun a _ =&gt; (bcf_Xf 0 a).mul (bcf_ext H _ hs1)).1.aestronglyMeasurable
      (.of_forall fun u s' hs' =&gt; hBd s' hs' u) (integrable_const _)
      (.of_forall fun u s' _ =&gt; hasDerivAt_ext_s H g u s' hl)
    have e : ∫ u, (∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s u)) ∂(gP (PC l n)) =
        ∑ a, ∫ u, Int H s l 0 a (D (cn 0 a) g) u ∂(gP (PC l n)) := by
      rw [integral_finsetSum _ fun a _ =&gt; ((bcf_Xf 0 a).mul (bcf_ext H _ hs1)).integrable]
      refine sum_congr rfl fun a _ =&gt; ?_
      have := integral_walk H hs1 l 0 (by omega) a g (fun _ =&gt; 1) (BCf.const 1) (fun _ _ _ _ =&gt; rfl)
      simpa using this
    rw [← e]
    exact this.2</pre></td></tr></tbody>
</table>

The selected proof slice establishes the averaged derivative for 0<s<1 using a dominated derivative bound. It does not export the polynomial-in-s claim or the endpoint derivative formula.

### 56. fr-three-block-chain-rule — weaker

Paper lines 1626–1631; `QuarticQuery.ForrelationLower.sum_dw_eq` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\frac{\partial}{\partial U_a}F_{0a}(w_s)
=s\varphi'(U_a)\underbrace{F_{0a,0a}(w_s)}_{0}
 +\sum_bH_{b,a}\varphi'(V_b)\varphi(U'_b)F_{0a,1b}(w_s).
\tag{8.16}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)
include hj in

theorem sum_dw_eq (s : ℝ) (u : PC l n → ℝ) (E : BC l n → ℝ) (hE : E (cn j a) = 0) :
    ∑ c : BC l n, (Sf s c * (dY H j a u c.1 c.2 * Xf u c.1 c.2 +
        Yf H u c.1 c.2 * dX j a u c.1 c.2)) * E c =
      ∑ b, H b a * dphi (Vc H u j b) * Xf u (j + 1) b * E (cn (j + 1) b)</pre></td></tr></tbody>
</table>

The theorem is the algebraic bias-chain sum after assuming hE : E (cn j a)=0; it does not itself assert that E is this mixed derivative or state the full k=3 derivative formula. hasDerivAt_ext and D_D supply those additional steps.

### 57. fr-earlier-layer-coefficient — weaker

Paper lines 1653–1653; `QuarticQuery.ForrelationLower.EarlyOnly` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The weights accumulated at the first crossing depend only on the first Gaussian layer.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)

def EarlyOnly (j : ℕ) (θ : (PC l n → ℝ) → ℝ) : Prop :=
  ∀ (u : PC l n → ℝ) (p : PC l n) (t : ℝ), j ≤ p.1.val → θ (Function.update u p t) = θ u</pre></td></tr></tbody>
</table>

EarlyOnly defines the condition that a coefficient ignores the current and later Gaussian layers. It does not prove that the particular accumulated coefficient in this sentence satisfies that condition; the iteration proof supplies that verification.

### 58. fr-iterated-gaussian-identity — weaker

Paper lines 1678–1685; `QuarticQuery.ForrelationLower.integral_walk` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
h_g'(s)=\sum_{p\in[m]^k}
\left(\prod_{j&lt;k-1}H_{p_{j+1},p_j}\right)
\mathbb E_U\left[
\left(\prod_{j&lt;k-1}\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))\right)
\partial_{S_p}F_g(w_s(U))\right].
\tag{8.20}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)

theorem integral_walk {s : ℝ} (hs : |s| ≤ 1) (e : ℕ) : ∀ (j : ℕ), j + e = l → ∀ (a : n)
    (g₀ : (BC l n → Bool) → ℝ) (θ : (PC l n → ℝ) → ℝ), BCf θ → EarlyOnly j θ →
    ∫ u, θ u * (Xf u j a * ext (D (cn j a) g₀) (wv H s u)) ∂(gP (PC l n)) =
      ∫ u, θ u * Int H s e j a (D (cn j a) g₀) u ∂(gP (PC l n))</pre></td></tr></tbody>
</table>

The theorem replaces a remaining rounded factor under the integral by Int, assuming a continuous bounded coefficient that satisfies EarlyOnly. It is one induction ingredient, not the full derivative-of-h_g path formula.

### 59. fr-iterated-gaussian-identity — weaker

Paper lines 1678–1685; `QuarticQuery.ForrelationLower.Int_eq_paths` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
h_g'(s)=\sum_{p\in[m]^k}
\left(\prod_{j&lt;k-1}H_{p_{j+1},p_j}\right)
\mathbb E_U\left[
\left(\prod_{j&lt;k-1}\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))\right)
\partial_{S_p}F_g(w_s(U))\right].
\tag{8.20}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)

theorem Int_eq_paths (s : ℝ) (e : ℕ) : ∀ (j : ℕ) (a : n) (g : (BC l n → Bool) → ℝ)
    (u : PC l n → ℝ), Int H s e j a g u =
      ∑ q : Fin e → n, cf H s e j a q u * ext (Dl (plist e j q) g) (wv H s u)</pre></td></tr></tbody>
</table>

The theorem expands Int as a finite path sum for arbitrary s. It has no derivative or Gaussian-average conclusion; those come from the separate analytic identity.

### 60. fr-iterated-gaussian-identity — weaker

Paper lines 1678–1685; `QuarticQuery.ForrelationLower.exists_identity` in `QuarticQuery/ForrelationLower/Walk.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
h_g'(s)=\sum_{p\in[m]^k}
\left(\prod_{j&lt;k-1}H_{p_{j+1},p_j}\right)
\mathbb E_U\left[
\left(\prod_{j&lt;k-1}\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))\right)
\partial_{S_p}F_g(w_s(U))\right].
\tag{8.20}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : Type} [Fintype n] [DecidableEq n] {l : ℕ} (H : Matrix n n ℝ)
variable {j : ℕ} (hj : j &lt; l) (a : n)

theorem exists_identity (hl : 0 &lt; l) (g : (BC l n → Bool) → ℝ) :
    ∃ s ∈ Set.Ioo (0 : ℝ) 1,
      ∫ u, ext g (wv H 1 u) ∂(gP (PC l n)) - ∫ u, ext g (wv H 0 u) ∂(gP (PC l n)) =
        ∑ a, ∫ u, Int H s l 0 a (D (cn 0 a) g) u ∂(gP (PC l n))

Selected proof passage:
  have hderiv : ∀ s ∈ Set.Ioo (0 : ℝ) 1, HasDerivAt h
      (∑ a, ∫ u, Int H s l 0 a (D (cn 0 a) g) u ∂(gP (PC l n))) s := by
    intro s hs
    have hs1 : |s| ≤ 1 := abs_le.mpr ⟨by linarith [hs.1], hs.2.le⟩
    have hBd : ∀ s' ∈ Set.Ioo (0 : ℝ) 1, ∀ u : PC l n → ℝ,
        ‖∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s' u)‖ ≤ Fintype.card n * B := by
      intro s' hs' u
      have hs1' : |s'| ≤ 1 := abs_le.mpr ⟨by linarith [hs'.1], hs'.2.le⟩
      calc _ ≤ ∑ _a : n, B := by
            refine (norm_sum_le _ _).trans (sum_le_sum fun a _ =&gt; ?_)
            rw [Real.norm_eq_abs, abs_mul]
            have h1 := abs_Xf_le u 0 a
            have h2 : |ext (D (cn 0 a) g) (wv H s' u)| ≤ B :=
              abs_ext_le (abs_D_le hB _) fun c =&gt; abs_wv_le H hs1' u c
            nlinarith [abs_nonneg (Xf u 0 a), abs_nonneg (ext (D (cn 0 a) g) (wv H s' u))]
        _ = _ := by simp
    have := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := gP (PC l n))
      (F := fun s u =&gt; ext g (wv H s u))
      (F' := fun s u =&gt; ∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s u))
      (bound := fun _ =&gt; Fintype.card n * B) (x₀ := s) (s := Set.Ioo 0 1)
      (Ioo_mem_nhds hs.1 hs.2)
      (.of_forall fun s' =&gt; ((continuous_ext g).comp
        (continuous_pi fun c =&gt; continuous_wv H s' c)).aestronglyMeasurable)
      (bcf_ext H g hs1).integrable
      (BCf.sum _ fun a _ =&gt; (bcf_Xf 0 a).mul (bcf_ext H _ hs1)).1.aestronglyMeasurable
      (.of_forall fun u s' hs' =&gt; hBd s' hs' u) (integrable_const _)
      (.of_forall fun u s' _ =&gt; hasDerivAt_ext_s H g u s' hl)
    have e : ∫ u, (∑ a, Xf u 0 a * ext (D (cn 0 a) g) (wv H s u)) ∂(gP (PC l n)) =
        ∑ a, ∫ u, Int H s l 0 a (D (cn 0 a) g) u ∂(gP (PC l n)) := by
      rw [integral_finsetSum _ fun a _ =&gt; ((bcf_Xf 0 a).mul (bcf_ext H _ hs1)).integrable]
      refine sum_congr rfl fun a _ =&gt; ?_
      have := integral_walk H hs1 l 0 (by omega) a g (fun _ =&gt; 1) (BCf.const 1) (fun _ _ _ _ =&gt; rfl)
      simpa using this
    rw [← e]
    exact this.2</pre></td></tr></tbody>
</table>

This proof slice identifies the averaged derivative with the iterated Gaussian sum only for s in (0,1). The paper’s display is asserted for every s in [0,1], including both endpoints.

### 61. fr-forrelation-path-expansion — weaker

Paper lines 1705–1710; `QuarticQuery.forrelationNumerator` in `QuarticQuery/Statement.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Phi(z)=\frac1m\sum_{p\in[m]^k}
\left(\prod_{j&lt;k}z_j(p_j)\right)
\left(\prod_{j&lt;k-1}H_{p_{j+1},p_j}\right).
\tag{8.22}
\]</pre></td><td><pre>def forrelationNumerator (k t : ℕ) (z : BitInput (ForrelationCoord k t)) : ℤ :=
  ∑ path : Fin k → Fin (mValue t),
    (∏ h : Fin k, bitSign (z (h, path h))) *
    (∏ h : Fin (k - 1),
      walshSign t (path ⟨h.val, Nat.lt_of_lt_of_le h.isLt (Nat.sub_le k 1)⟩)
        (path ⟨h.val + 1, Nat.add_lt_of_lt_sub h.isLt⟩))</pre></td></tr></tbody>
</table>

This definition gives the integer path sum with unnormalized Walsh signs. The selected display is the normalized real Φ expansion; it additionally needs the denominator and the definition of H.

### 62. fr-forrelation-path-expansion — weaker

Paper lines 1705–1710; `QuarticQuery.forrelationDenominator` in `QuarticQuery/Statement.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Phi(z)=\frac1m\sum_{p\in[m]^k}
\left(\prod_{j&lt;k}z_j(p_j)\right)
\left(\prod_{j&lt;k-1}H_{p_{j+1},p_j}\right).
\tag{8.22}
\]</pre></td><td><pre>def forrelationDenominator (k t : ℕ) : ℤ :=
  (2 : ℤ) ^ (2 * t) * ((2 : ℤ) ^ t) ^ (k - 1)</pre></td></tr></tbody>
</table>

This definition gives only the normalization m(√m)^{k−1}. The selected display also contains the path numerator and its real correlation, which are separate definitions.

### 63. fr-uniform-forrelation-moments — weaker

Paper lines 1715–1719; `QuarticQuery.ForrelationLower.ext_PhiF_zero` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E_{\mathcal U}\Phi=0,\qquad
\mathbb E_{\mathcal U}\Phi^2=\frac1m.
\tag{8.23}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem ext_PhiF_zero : ext (PhiF t : (BC l (Nm t) → Bool) → ℝ) 0 = 0</pre></td></tr></tbody>
</table>

This theorem gives the uniform first moment zero. The selected display also gives the second moment 1/m, which is a separate theorem.

### 64. fr-uniform-forrelation-moments — weaker

Paper lines 1715–1719; `QuarticQuery.ForrelationLower.ext_PhiF_sq` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E_{\mathcal U}\Phi=0,\qquad
\mathbb E_{\mathcal U}\Phi^2=\frac1m.
\tag{8.23}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem ext_PhiF_sq (l t : ℕ) :
    ext (fun z : BC l (Nm t) → Bool =&gt; PhiF t z ^ 2) 0 = ((2 : ℝ) ^ (2 * t))⁻¹</pre></td></tr></tbody>
</table>

This theorem gives the uniform second moment 1/m. The selected display also gives the first moment zero, which is a separate theorem.

### 65. fr-gaussian-edge-lower-estimates — weaker

Paper lines 1740–1745; `QuarticQuery.ForrelationLower.qf_le_exp` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
q(x)\le\sqrt3\,e^{(x^2-1)/6},\qquad
\Psi(x)\varphi'(y)\ge
\frac1{18}\exp\!\left[-\frac{x^2-1}{6}-\frac{5(y^2-1)}6\right].
\tag{8.24}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem qf_le_exp (x : ℝ) : qf x ≤ Real.sqrt 3 * Real.exp ((x ^ 2 - 1) / 6)</pre></td></tr></tbody>
</table>

This theorem gives the upper bound for q(x). The selected display also gives the lower bound for Ψ(x)φ′(y), supplied by a separate theorem.

### 66. fr-gaussian-edge-lower-estimates — weaker

Paper lines 1740–1745; `QuarticQuery.ForrelationLower.psi_dphi_ge` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
q(x)\le\sqrt3\,e^{(x^2-1)/6},\qquad
\Psi(x)\varphi'(y)\ge
\frac1{18}\exp\!\left[-\frac{x^2-1}{6}-\frac{5(y^2-1)}6\right].
\tag{8.24}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem psi_dphi_ge (x y : ℝ) :
    (1 / 18) * Real.exp (-((x ^ 2 - 1) / 6 + 5 / 6 * (y ^ 2 - 1))) ≤ psiS x * dphi y</pre></td></tr></tbody>
</table>

This theorem gives the lower bound for Ψ(x)φ′(y). It uses, but does not itself state, the separate q(x) bound also printed in the selected display.

### 67. fr-selected-gaussian-moments — weaker

Paper lines 1755–1755; `QuarticQuery.ForrelationLower.integral_Uc_sq` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Every selected $U$ coordinate has second moment one, and so, by (8.11) for the corresponding unit Walsh row, does every selected $V$ coordinate</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem integral_Uc_sq {j : ℕ} (hj : j &lt; l) (a : Nm t) :
    ∫ u : PC l (Nm t) → ℝ, Uc u j a ^ 2 ∂(gP (PC l (Nm t))) = 1</pre></td></tr></tbody>
</table>

This theorem gives the selected U-coordinate second moment. The phrase also asserts the V-coordinate second moment; that requires the separate transformed-coordinate theorem.

### 68. fr-selected-gaussian-moments — weaker

Paper lines 1755–1755; `QuarticQuery.ForrelationLower.integral_Vc_sq` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Every selected $U$ coordinate has second moment one, and so, by (8.11) for the corresponding unit Walsh row, does every selected $V$ coordinate</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem integral_Vc_sq {j : ℕ} (hj : j &lt; l) (a : Nm t) :
    ∫ u : PC l (Nm t) → ℝ, Vc (H t) u j a ^ 2 ∂(gP (PC l (Nm t))) = 1</pre></td></tr></tbody>
</table>

This theorem gives the selected V-coordinate second moment. The phrase also asserts the U-coordinate second moment, which has its own declaration.

### 69. fr-positive-forrelation-mean — weaker

Paper lines 1769–1773; `QuarticQuery.ForrelationLower.mass_ge` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E_{\nu_1}\Phi\ge a_k:=18^{-(k-1)}
\ge32^{-(k-1)}=32\delta.
\tag{8.26}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem mass_ge (hl : 0 &lt; l) :
    (1 / 18 : ℝ) ^ l ≤
      ∫ u, ext (PhiF t : (BC l (Nm t) → Bool) → ℝ) (wv (H t) 1 u) ∂(gP (PC l (Nm t))) -
        ext (PhiF t : (BC l (Nm t) → Bool) → ℝ) 0</pre></td></tr></tbody>
</table>

The theorem gives correlated mean minus uniform mean ≥18^{-(k−1)}. The selected display additionally identifies the uniform mean as zero and compares 18^{-(k−1)} with 32δ; those are supplied by the other two links.

### 70. fr-positive-forrelation-mean — weaker

Paper lines 1769–1773; `QuarticQuery.ForrelationLower.ext_PhiF_zero` in `QuarticQuery/ForrelationLower/Promise.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E_{\nu_1}\Phi\ge a_k:=18^{-(k-1)}
\ge32^{-(k-1)}=32\delta.
\tag{8.26}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem ext_PhiF_zero : ext (PhiF t : (BC l (Nm t) → Bool) → ℝ) 0 = 0</pre></td></tr></tbody>
</table>

This theorem supplies only the zero uniform mean needed to turn mass_ge into an absolute correlated-mean bound. It does not state either inequality in the selected lower-mean chain.

### 71. fr-positive-forrelation-mean — weaker

Paper lines 1769–1773; `QuarticQuery.ForrelationLower.dl_le` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E_{\nu_1}\Phi\ge a_k:=18^{-(k-1)}
\ge32^{-(k-1)}=32\delta.
\tag{8.26}
\]</pre></td><td><pre>theorem dl_le (l : ℕ) : 32 * dl (l + 1) ≤ (1 / 18 : ℝ) ^ l</pre></td></tr></tbody>
</table>

The theorem gives the numerical inequality 32δ≤18^{-(k−1)}. It does not state the correlated-distribution mean inequality in the selected display.

### 72. fr-leaf-pairing-identity — weaker

Paper lines 1890–1894; `QuarticQuery.ForrelationLower.walk_chaos` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathcal E_\mu[g(z)Y_r^c(I,z)]
=\mathbb E_\mu[g(z)Y_r^c(Q_d,z)].
\tag{8.32}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]

theorem walk_chaos {μ : ι → ℝ} {ξ : ι → Bool → ℝ}
    (hm : ∀ a, piB (μ a) false * ξ a false + piB (μ a) true * ξ a true = 0)
    (v : Bool → ℝ) (c : Finset ι → ℝ) (ℓ : ℕ) (T : QueryTree ι) :
    ext (fun z =&gt; v (T.eval z) * chaos ξ c ℓ univ z) μ =
      walk μ (fun Q x b =&gt; v b * chaos ξ c ℓ Q x) T ∅ (fun _ =&gt; false)</pre></td></tr></tbody>
</table>

The paper allows an independent real value in [-1,1] at every leaf. walk_chaos uses T : QueryTree ι with Boolean leaves and one postprocessing map v : Bool → ℝ. The full real-leaf endpoint growth theorem is separately linked at (8.28).

### 73. fr-maximal-inequality-scope — different

Paper lines 1905–1909; `QuarticQuery.ForrelationLower.hit_azuma` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Pr\!\left(\max_{j\le d}|Z_j|&gt;R\right)
\le2\exp\!\left(-\frac{R^2}{2B^2d}\right).
\tag{8.33}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem hit_azuma (hμ : ∀ a, |μ a| ≤ 1)
    (hm : ∀ a, piB (μ a) false * ξ a false + piB (μ a) true * ξ a true = 0)
    (hB₀ : 0 &lt; B₀) (hξ : ∀ a b, |ξ a b| ≤ B₀)
    (Y : Finset ι → (ι → Bool) → ℝ) (Y' : ι → Finset ι → (ι → Bool) → ℝ)
    (hY : ∀ q Q x b, q ∉ Q →
      Y (insert q Q) (Function.update x q b) = Y Q x + ξ q b * Y' q Q x)
    {R β lam : ℝ} (hlam : 0 ≤ lam) (hβ : 0 ≤ β) (T : QueryTree ι) (d : ℕ) (hT : T.depth ≤ d)
    (Q : Finset ι) (x : ι → Bool) :
    hit μ (fun Q x =&gt; R &lt; Y Q x ∨ ∃ q, β &lt; |Y' q Q x|) T Q x ≤
      Real.exp (lam * (Y Q x - R) + lam ^ 2 * β ^ 2 * B₀ ^ 2 * d / 2) +
        hit μ (fun Q x =&gt; ∃ q, β &lt; |Y' q Q x|) T Q x</pre></td></tr></tbody>
</table>

The paper quantifies over arbitrary zero-start martingales and gives a two-sided maximum bound with deterministic increment bound B. hit_azuma quantifies over a finite QueryTree, fixed product biases and the specific fresh-query increment identity hY; its conclusion is one-sided and adds the probability of a bad coefficient event.

### 74. fr-terminal-polynomial-moment — weaker

Paper lines 1947–1951; `QuarticQuery.ForrelationLower.abs_ext_tree_chaos_le` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\left|\mathcal E_\mu[gY_r^c(I,\cdot)]\right|
\le K^r+(2n)^r(4n)^r e^{-\Lambda}.
\tag{8.35}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem abs_ext_tree_chaos_le (hμ : ∀ a, |μ a| ≤ 1)
    (hm : ∀ a, piB (μ a) false * ξ a false + piB (μ a) true * ξ a true = 0)
    (hB₀ : 0 &lt; B₀) (hξ : ∀ a b, |ξ a b| ≤ B₀) {Λ K : ℝ} {d : ℕ} (hd : 0 &lt; d) (hK : 0 &lt; K)
    (hKsq : K ^ 2 = 2 * d * B₀ ^ 2 * Λ) (hn : 1 ≤ Fintype.card ι) (T : QueryTree ι)
    (hT : T.depth ≤ d) (k : ℕ) (c : Finset ι → ℝ) (hc : ∀ J, |c J| ≤ 1)
    (v : Bool → ℝ) (hv : ∀ b, |v b| ≤ 1) :
    |ext (fun z =&gt; v (T.eval z) * chaos ξ c k univ z) μ| ≤
      K ^ k + (Fintype.card ι * B₀) ^ k * ((4 * Fintype.card ι : ℝ) ^ k * Real.exp (-Λ))</pre></td></tr></tbody>
</table>

The paper’s g may have arbitrary real leaf labels. This intermediate theorem uses a Boolean QueryTree and a single bounded map v : Bool → ℝ. It also permits a general factor bound B₀, specialized to 2 here; the lost real-leaf generality is the reason for the weaker classification.

### 75. fr-off-promise-pointwise-comparison — weaker

Paper lines 1992–1997; `QuarticQuery.ForrelationLower.not_RLe_of_gap_sharp` in `QuarticQuery/ForrelationLower/Main.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
(1-\varepsilon)(\Phi(z)-\delta)
\le A(z)
\le\varepsilon+\frac{4\Phi(z)^2}{\delta^2}.
\tag{8.37}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem not_RLe_of_gap_sharp (hl : 0 &lt; l) {L τ : ℕ} {Λ K A : ℝ} (hK : 0 &lt; K)
    (hKsq : K ^ 2 = 2 * (2 * τ * L + 1 : ℕ) * 2 ^ 2 * Λ)
    (hA : ((3 / 16 : ℝ) * ((2 : ℝ) ^ t)⁻¹) ^ l * (K ^ (l + 1) +
        (Fintype.card (BC l (Nm t)) * 2) ^ (l + 1) *
        ((4 * Fintype.card (BC l (Nm t)) : ℝ) ^ (l + 1) * Real.exp (-Λ))) ≤ A)
    (hε1 : (8 / 9 : ℝ) ^ τ ≤ 1)
    (hgap : (8 / 9 : ℝ) ^ τ + 4 / dl (l + 1) ^ 2 * ((2 : ℝ) ^ (2 * t))⁻¹ + A &lt;
      (1 - (8 / 9 : ℝ) ^ τ) * ((1 / 18 : ℝ) ^ l - dl (l + 1))) :
    ¬ RLe (P (l + 1) t) L

Selected proof passage:
  -- the two pointwise comparisons
  have hup : ∀ z, a z ≤ ε + 4 / δ ^ 2 * PhiF t z ^ 2 := by
    intro z
    by_cases hz : |PhiF t z| ≤ δ / 2
    · have := hno z (P_no hz)
      have : 0 ≤ 4 / δ ^ 2 * PhiF t z ^ 2 := by positivity
      linarith
    · have h2 : (δ / 2) ^ 2 &lt; PhiF t z ^ 2 := by
        have := sq_lt_sq' (by linarith [abs_nonneg (PhiF t z), not_le.mp hz]) (not_le.mp hz)
        rwa [sq_abs] at this
      have h3 : 1 ≤ 4 / δ ^ 2 * PhiF t z ^ 2 := by
        rw [div_mul_eq_mul_div, le_div_iff₀ (by positivity)]
        nlinarith
      linarith [ha1 z]
  have hlow : ∀ z, (1 - ε) * (PhiF t z - δ) ≤ a z := by
    intro z
    have hle1 : PhiF t z - δ ≤ 1 := by linarith [(abs_le.mp (hPhi1 z)).2]
    have h1e : 0 ≤ 1 - ε := by linarith
    by_cases hz : δ ≤ PhiF t z
    · have := hyes z (P_yes hz)
      nlinarith
    · have : PhiF t z - δ ≤ 0 := by linarith [not_le.mp hz]
      nlinarith [ha0 z]</pre></td></tr></tbody>
</table>

The paper quantifies over every acceptance function A in [0,1] with any promise error ε in [0,1]. The proof slice establishes these comparisons only for its constructed amplified acceptance a, with ε=(8/9)^τ, fixed δ=dl(l+1), and Φ=PhiF t.

### 76. fr-acceptance-expectation-gap — weaker

Paper lines 2003–2008; `QuarticQuery.ForrelationLower.not_RLe_of_gap_sharp` in `QuarticQuery/ForrelationLower/Main.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E_{\nu_1}A-\mathbb E_{\mathcal U}A
\ge (1-\varepsilon)(a_k-\delta)
       -\varepsilon-\frac4{m\delta^2}.
\tag{8.38}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem not_RLe_of_gap_sharp (hl : 0 &lt; l) {L τ : ℕ} {Λ K A : ℝ} (hK : 0 &lt; K)
    (hKsq : K ^ 2 = 2 * (2 * τ * L + 1 : ℕ) * 2 ^ 2 * Λ)
    (hA : ((3 / 16 : ℝ) * ((2 : ℝ) ^ t)⁻¹) ^ l * (K ^ (l + 1) +
        (Fintype.card (BC l (Nm t)) * 2) ^ (l + 1) *
        ((4 * Fintype.card (BC l (Nm t)) : ℝ) ^ (l + 1) * Real.exp (-Λ))) ≤ A)
    (hε1 : (8 / 9 : ℝ) ^ τ ≤ 1)
    (hgap : (8 / 9 : ℝ) ^ τ + 4 / dl (l + 1) ^ 2 * ((2 : ℝ) ^ (2 * t))⁻¹ + A &lt;
      (1 - (8 / 9 : ℝ) ^ τ) * ((1 / 18 : ℝ) ^ l - dl (l + 1))) :
    ¬ RLe (P (l + 1) t) L

Selected proof passage:
  have hE1 : (1 - ε) * (∫ u, ext (PhiF t) (wv (H t) 1 u) ∂(gP (PC l (Nm t))) - δ) ≤
      ∑ j, q j * ∫ u, ext (G j) (wv (H t) 1 u) ∂(gP (PC l (Nm t))) := by
    have hint : ∫ u : PC l (Nm t) → ℝ, (1 - ε) * (ext (PhiF t) (wv (H t) 1 u) - δ)
        ∂(gP (PC l (Nm t))) ≤ ∫ u, ∑ j, q j * ext (G j) (wv (H t) 1 u) ∂(gP (PC l (Nm t))) := by
      refine integral_mono ((hbcP.integrable.sub (integrable_const δ)).const_mul _)
        (integrable_finsetSum _ fun j _ =&gt; (hbcG j).integrable.const_mul _) fun u =&gt; ?_
      have h1 := ext_mono hlow (hμ1 u)
      have h2 : ext (fun z =&gt; (1 - ε) * (PhiF t z - δ)) (wv (H t) 1 u) =
          (1 - ε) * (ext (PhiF t) (wv (H t) 1 u) - δ) := by
        rw [ext_smul]
        congr 1
        have : (fun z : BC l (Nm t) → Bool =&gt; PhiF t z - δ) =
            fun z =&gt; PhiF t z + (fun _ =&gt; -δ) z := by
          funext z; ring
        rw [this, ext_add, ext_const]
        ring
      rw [h2, hexta] at h1
      exact h1
    rw [integral_const_mul, integral_sub hbcP.integrable (integrable_const δ),
      integral_finsetSum _ fun j _ =&gt; (hbcG j).integrable.const_mul _] at hint
    simp only [integral_const_mul] at hint
    simpa using hint
  -- upper bound on the uniform measure
  have hE0 : ∑ j, q j * ext (G j) 0 ≤ ε + 4 / δ ^ 2 * ((2 : ℝ) ^ (2 * t))⁻¹ := by
    rw [← hexta]
    have h1 := ext_mono hup hμ0
    have h2 : ext (fun z =&gt; ε + 4 / δ ^ 2 * PhiF t z ^ 2) (0 : BC l (Nm t) → ℝ) =
        ε + 4 / δ ^ 2 * ((2 : ℝ) ^ (2 * t))⁻¹ := by
      have e := ext_add (fun _ =&gt; ε) (fun z =&gt; 4 / δ ^ 2 * PhiF t z ^ 2) (0 : BC l (Nm t) → ℝ)
      rw [e, ext_const, ext_smul, ext_PhiF_sq]
    rwa [h2] at h1
  -- the advantage of each tree
  have hadv : ∀ j, ∫ u, ext (G j) (wv (H t) 1 u) ∂(gP (PC l (Nm t))) ≤ ext (G j) 0 + A := by
    intro j
    have hcard : 1 ≤ Fintype.card (BC l (Nm t)) := by
      have hne : Nonempty (BC l (Nm t)) := ⟨(0, ⟨0, by simp [mValue]⟩)⟩
      exact Fintype.card_pos
    have := advantage_le_sharp (H t) hl (rowsOrth_H t) (ε := ((2 : ℝ) ^ t)⁻¹) (by positivity) abs_H_le
      (d := 2 * τ * L + 1) (Nat.succ_pos _) hK hKsq hcard (T j) ((hdepth j).trans (Nat.le_succ _))
      v hv
    have h2 := (abs_le.mp (this.trans hA)).2
    simp only [G]
    linarith
  have hmass := mass_ge (t := t) hl
  rw [ext_PhiF_zero, sub_zero] at hmass
  have hfin : ∑ j, q j * ∫ u, ext (G j) (wv (H t) 1 u) ∂(gP (PC l (Nm t))) ≤
      ∑ j, q j * ext (G j) 0 + A := by
    calc _ ≤ ∑ j, q j * (ext (G j) 0 + A) :=
          sum_le_sum fun j _ =&gt; mul_le_mul_of_nonneg_left (hadv j) (hq0 j)
      _ = _ := by rw [sum_congr rfl fun j _ =&gt; mul_add _ _ _, sum_add_distrib, ← sum_mul, hq1,
            one_mul]
  have h1e : 0 ≤ 1 - ε := by linarith
  have hE2 := mul_le_mul_of_nonneg_left (sub_le_sub_right hmass δ) h1e
  linarith</pre></td></tr></tbody>
</table>

The displayed inequality applies to arbitrary A and ε satisfying the preceding promise assumptions. The local proof uses its finite amplified tree mixture a and the fixed error ε=(8/9)^τ; hE1, hE0, and mass_ge yield this specialized gap.

### 77. fr-conclusion-forrelation-adaptivity — weaker

Paper lines 2043–2043; `QuarticQuery.ForrelationLower.hit_chaos_le` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For a single Forrelation input, an adaptively chosen fresh sign has a centered increment under a fixed product bias. The resulting bound on the sum of mixed derivatives gives (8.29), with its factor $m^{-(k-1)/2}$ from the Walsh entries.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem hit_chaos_le (hμ : ∀ a, |μ a| ≤ 1)
    (hm : ∀ a, piB (μ a) false * ξ a false + piB (μ a) true * ξ a true = 0)
    (hB₀ : 0 &lt; B₀) (hξ : ∀ a b, |ξ a b| ≤ B₀) {Λ K : ℝ} {d : ℕ} (hd : 0 &lt; d) (hK : 0 &lt; K)
    (hKsq : K ^ 2 = 2 * d * B₀ ^ 2 * Λ) (hn : 1 ≤ Fintype.card ι) (T : QueryTree ι)
    (hT : T.depth ≤ d) (ℓ : ℕ) (c : Finset ι → ℝ) (hc : ∀ J, |c J| ≤ 1) (x : ι → Bool) :
    hit μ (fun Q x =&gt; K ^ ℓ &lt; |chaos ξ c ℓ Q x|) T ∅ x ≤
      (4 * Fintype.card ι : ℝ) ^ ℓ * Real.exp (-Λ)</pre></td></tr></tbody>
</table>

The theorem bounds revealed-polynomial crossings under centered-factor hypotheses. The selected summary also asserts the final mixed-derivative expectation-gap estimate and its Walsh scaling, which this theorem does not state.

### 78. fr-conclusion-forrelation-adaptivity — weaker

Paper lines 2043–2043; `QuarticQuery.ForrelationLower.advantage_le_sharp_real_leaves_explicit` in `QuarticQuery/ForrelationLower/RealLeafExplicit.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For a single Forrelation input, an adaptively chosen fresh sign has a centered increment under a fixed product bias. The resulting bound on the sum of mixed derivatives gives (8.29), with its factor $m^{-(k-1)/2}$ from the Walsh entries.</pre></td><td><pre>theorem advantage_le_sharp_real_leaves_explicit
    {n : Type} [Fintype n] [DecidableEq n] {l d : ℕ}
    (H : Matrix n n ℝ) (hl : 0 &lt; l) (hH : RowsOrth H)
    {ε : ℝ} (hε : 0 ≤ ε) (hHb : ∀ a b, |H a b| ≤ ε)
    (hd : 1 ≤ d) (hn : 1 ≤ Fintype.card (BC l n))
    (T : RealQueryTree (BC l n)) (hT : T.depth ≤ d) (hbounded : T.Bounded) :
    |∫ u, ext T.eval (wv H 1 u) ∂(gP (PC l n)) - ext T.eval 0| ≤
      ((3 / 16 : ℝ) * ε) ^ l *
        ((Real.sqrt (16 * ((l + 1 : ℕ) : ℝ) * d *
            Real.log (4 * Fintype.card (BC l n)))) ^ (l + 1) +
          (1 / 2 : ℝ) ^ (l + 1))</pre></td></tr></tbody>
</table>

The theorem supplies the final real-leaf advantage bound and its matrix-entry factor. The selected summary also describes the fresh-sign centered-increment mechanism, which is part of its supporting argument rather than this theorem’s type.

### 79. qm-a1 — weaker

Paper lines 2057–2061; `QuarticQuery.Paper.appendixA_D_le_Q_pow_four` in `QuarticQuery/Paper/AppendixA.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 R(f)\le D(f)\le 35^4 Q(f)^4
       =1{,}500{,}625\,Q(f)^4.
\tag{A.1}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_D_le_Q_pow_four (f : TotalBool (Fin n)) :
    D (totalise f) ≤ 1500625 * Q (totalise f) ^ 4</pre></td></tr></tbody>
</table>

This declaration states the D ≤ 1,500,625 Q^4 component. The R ≤ D component is the separate linked theorem; neither declaration alone states the whole displayed chain.

### 80. qm-a1 — weaker

Paper lines 2057–2061; `QuarticQuery.R_le_D` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 R(f)\le D(f)\le 35^4 Q(f)^4
       =1{,}500{,}625\,Q(f)^4.
\tag{A.1}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}
variable [Fintype ι]

theorem R_le_D (f : PartialBool ι) : R f ≤ D f</pre></td></tr></tbody>
</table>

This declaration states R ≤ D for every partial function, but does not supply the displayed quartic bound on D. The companion link supplies that component.

### 81. qm-a2-roadmap — weaker

Paper lines 2093–2099; `QuarticQuery.Paper.appendixA_blockSensitivity_star_le_Q_sq` in `QuarticQuery/Paper/AppendixAStar.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 \operatorname{bs}(f)\le 35^2Q(f)^2,
 \qquad \lambda(f)\le35Q(f),
 \qquad \deg(f)\le\lambda(f)^2,
 \qquad D(f)\le\operatorname{bs}(f)\deg(f).
\tag{A.2}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_blockSensitivity_star_le_Q_sq (f : TotalBool (Fin n)) :
    blockSensitivity f ≤ 1225 * Q (totalise f) ^ 2</pre></td></tr></tbody>
</table>

This theorem gives bs(f)≤1225 Q(f)² only; the other three roadmap inequalities are the separate linked results.

### 82. qm-a2-roadmap — weaker

Paper lines 2093–2099; `QuarticQuery.Paper.appendixA_spectralSensitivity_adversary_le_Q` in `QuarticQuery/Paper/AppendixAStar.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 \operatorname{bs}(f)\le 35^2Q(f)^2,
 \qquad \lambda(f)\le35Q(f),
 \qquad \deg(f)\le\lambda(f)^2,
 \qquad D(f)\le\operatorname{bs}(f)\deg(f).
\tag{A.2}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_spectralSensitivity_adversary_le_Q (f : TotalBool (Fin n)) :
    spectralSensitivity f ≤ 35 * Q (totalise f)</pre></td></tr></tbody>
</table>

This theorem gives λ(f)≤35 Q(f) only; it does not also state the block-sensitivity, degree, or deterministic bounds.

### 83. qm-a2-roadmap — weaker

Paper lines 2093–2099; `QuarticQuery.Paper.appendixA4_paper_route` in `QuarticQuery/Paper/AppendixAHuangRoute.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 \operatorname{bs}(f)\le 35^2Q(f)^2,
 \qquad \lambda(f)\le35Q(f),
 \qquad \deg(f)\le\lambda(f)^2,
 \qquad D(f)\le\operatorname{bs}(f)\deg(f).
\tag{A.2}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA4_paper_route (f : TotalBool (Fin n)) :
    (degree f : ℝ) ≤ spectralSensitivity f ^ 2</pre></td></tr></tbody>
</table>

This theorem gives deg(f)≤λ(f)² only; it does not state either query bound or the deterministic product bound.

### 84. qm-a2-roadmap — weaker

Paper lines 2093–2099; `QuarticQuery.Paper.appendixA_lemmaA5` in `QuarticQuery/Paper/AppendixASensitivity.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 \operatorname{bs}(f)\le 35^2Q(f)^2,
 \qquad \lambda(f)\le35Q(f),
 \qquad \deg(f)\le\lambda(f)^2,
 \qquad D(f)\le\operatorname{bs}(f)\deg(f).
\tag{A.2}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_lemmaA5 (f : TotalBool (Fin n)) :
    D (totalise f) ≤ blockSensitivity f * degree f</pre></td></tr></tbody>
</table>

This theorem gives D(f)≤bs(f)deg(f) only; the spectral and query inequalities in the display require the other declarations.

### 85. qm-adversary — weaker

Paper lines 2116–2121; `QuarticQuery.Paper.appendixA_lemmaA2` in `QuarticQuery/Paper/AppendixASpectralAdversary.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 Q(f)\ge
 \frac{1-2\sqrt2/3}{2}\frac{\|\Gamma\|}{M}
 \ge\frac1{35}\frac{\|\Gamma\|}{M}.
\tag{A.3}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_lemmaA2
    (f : TotalBool (Fin n)) (Γ : AppendixAMatrix n)
    (hsym : ∀ x y, Γ x y = Γ y x) (hΓ : ∀ x y, 0 ≤ Γ x y)
    (hzero : ∀ x y, f x = f y → Γ x y = 0) (hne : Γ ≠ 0) :
    (1 / 35 : ℝ) * (appendixAMatrixNorm Γ / appendixACoordinateMax Γ) ≤
      (Q (totalise f) : ℝ)</pre></td></tr></tbody>
</table>

The declaration states Q(f) ≥ (1/35)‖Γ‖/M, the weaker end of (A.3). It does not state the displayed sharper coefficient (1−2√2/3)/2. That coefficient appears before division in appendixA_adversary_of_perron.

### 86. qm-mask-positive — weaker

Paper lines 2122–2122; `QuarticQuery.Paper.appendixACoordinateMax_pos` in `QuarticQuery/Paper/AppendixASpectralAdversary.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The denominator is positive: a nonzero entry joins distinct opposite-output inputs, and some coordinate distinguishes those inputs. Its mask is therefore nonzero.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixACoordinateMax_pos
    (f : TotalBool (Fin n)) (Γ : AppendixAMatrix n)
    (hsym : ∀ x y, Γ x y = Γ y x) (hΓ : ∀ x y, 0 ≤ Γ x y)
    (hzero : ∀ x y, f x = f y → Γ x y = 0) (hne : Γ ≠ 0) :
    0 &lt; appendixACoordinateMax Γ</pre></td></tr></tbody>
</table>

The theorem states positivity of the maximum masked norm. It does not state the sentence’s selected-entry and distinguishing-coordinate explanation as separate conclusions.

### 87. qm-final-overlap — weaker

Paper lines 2163–2167; `QuarticQuery.Paper.appendixA_unit_states_final_overlap` in `QuarticQuery/Paper/AppendixAAdversary.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 |\langle\psi_x,\psi_y\rangle|
 \le\sqrt{ab}+\sqrt{(1-a)(1-b)}
 \le\frac{2\sqrt2}{3}.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ} {W : Type*} [Fintype W]

theorem appendixA_unit_states_final_overlap
    {ι : Type*} [Fintype ι] (ψ φ : EuclideanSpace ℂ ι)
    (hψ : ‖ψ‖ = 1) (hφ : ‖φ‖ = 1) (S : Finset ι)
    (hp : Cslib.Quantum.measureProb ψ S ≤ 1 / 3)
    (hq : 2 / 3 ≤ Cslib.Quantum.measureProb φ S) :
    ‖inner ℂ ψ φ‖ ≤ 2 * Real.sqrt 2 / 3</pre></td></tr></tbody>
</table>

The declaration gives the final bound |⟨ψ,φ⟩| ≤ 2√2/3. It does not include the displayed intermediate expression √(ab)+√((1−a)(1−b)).

### 88. qm-telescope-adversary — weaker

Paper lines 2176–2179; `QuarticQuery.Paper.appendixA_adversary_of_perron` in `QuarticQuery/Paper/AppendixAAdversary.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 (1-2\sqrt2/3)\|\Gamma\|
 \le |W_0-W_q|\le2qM.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ} {W : Type*} [Fintype W]

theorem appendixA_adversary_of_perron
    (f : TotalBool (Fin n)) (Γ : AppendixAMatrix n)
    (v : BitInput (Fin n) → ℝ)
    (U : ℕ → Cslib.Quantum.State n W →ₗᵢ[ℂ] Cslib.Quantum.State n W)
    {ψ₀ : Cslib.Quantum.State n W} (hψ₀ : ‖ψ₀‖ = 1) (T : ℕ)
    (S : Finset (Fin n × Bool × W))
    (h : ∀ x, |Cslib.Quantum.measureProb (Cslib.Quantum.run U ψ₀ x T) S -
      Cslib.BitString.bitVal ℝ (f x)| ≤ 1 / 3)
    (hΓ : ∀ x y, 0 ≤ Γ x y)
    (hzero : ∀ x y, f x = f y → Γ x y = 0)
    (hv : AppendixAPerronWitness Γ v)
    {M : ℝ} (hM : 0 ≤ M)
    (hcoord : ∀ i, appendixAMatrixNorm (appendixAGammaCoord Γ i) ≤ M) :
    (1 - 2 * Real.sqrt ((1 / 3 : ℝ) * (1 - 1 / 3))) * appendixAMatrixNorm Γ ≤
      2 * (T : ℝ) * M</pre></td></tr></tbody>
</table>

The declaration states the outer inequality (1−2√2/3)‖Γ‖ ≤ 2TM under the displayed algorithm/Perron hypotheses, but omits the intermediate |W₀−Wq| term. Its parameter T is the cap before the paper substitutes q=Q(f).

### 89. qm-star-mask — weaker

Paper lines 2209–2209; `QuarticQuery.Paper.appendixA_mask_star_norm_le_one` in `QuarticQuery/Paper/AppendixAStar.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>A coordinate belongs to at most one of the disjoint blocks, so its mask keeps at most one undirected star edge and has norm at most one.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_mask_star_norm_le_one (x : BitInput (Fin n))
    (L : Finset (BitInput (Fin n))) (hx : x ∉ L) (i : Fin n)
    (hcount : (L.filter (fun y =&gt; x i ≠ y i)).card ≤ 1) :
    appendixAMatrixNorm (appendixAGammaCoord (appendixA_starMatrix x L) i) ≤ 1</pre></td></tr></tbody>
</table>

The declaration assumes hcount, that at most one leaf survives the mask. It proves the norm conclusion but not the sentence’s derivation of hcount from block disjointness; that is provided by appendixA_sensitiveFamily_star_properties.

### 90. qm-sensitivity-mask — weaker

Paper lines 2219–2219; `QuarticQuery.Paper.appendixA_sensitivity_mask_norm_le_one` in `QuarticQuery/Paper/AppendixAStar.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The masked matrix is a direct sum of matrices \(\left(\begin{smallmatrix}0&amp;1\\1&amp;0\end{smallmatrix}\right)\) and zeros, so its norm is at most one.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_sensitivity_mask_norm_le_one (f : TotalBool (Fin n)) (i : Fin n) :
    appendixAMatrixNorm (appendixAGammaCoord (appendixA_sensitivityMatrix f) i) ≤ 1</pre></td></tr></tbody>
</table>

The declaration proves the norm bound. It does not state the sentence’s explicit direct-sum decomposition, although its proof uses the matching structure.

### 91. qm-huang-supported — weaker

Paper lines 2274–2274; `QuarticQuery.Paper.huang_supported_positive_eigenvector` in `QuarticQuery/Paper/AppendixAHuangMatrix.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Their dimensions sum to more than \(2^d\), so their intersection contains a nonzero real vector \(v\).</pre></td><td><pre>theorem huang_supported_positive_eigenvector (d : ℕ) (hd : 0 &lt; d)
    (U : Finset (HuangVertex d)) (hU : 2 ^ (d - 1) &lt; #U) :
    ∃ v : HuangVertex d → ℝ,
      huangEnd d v = √(d : ℝ) • v ∧ v ≠ 0 ∧ ∀ x ∉ U, v x = 0</pre></td></tr></tbody>
</table>

The theorem produces the nonzero eigenvector supported on U. It does not state the sentence’s preceding inequality for the sum of the two subspace dimensions.

### 92. qm-huang-rayleigh — weaker

Paper lines 2275–2281; `QuarticQuery.Paper.huang_absolute_rayleigh_supported` in `QuarticQuery/Paper/AppendixAHuangMatrix.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 u^{\mathsf T}A_Uu
 \ge v^{\mathsf T}H'_dv
 =\sqrt d\,\|v\|^2
 =\sqrt d\,\|u\|^2.
\tag{A.10}
\]</pre></td><td><pre>theorem huang_absolute_rayleigh_supported (d : ℕ) (U : Finset (HuangVertex d))
    (v : HuangVertex d → ℝ) (hv : huangEnd d v = √(d : ℝ) • v)
    (hsupp : ∀ x ∉ U, v x = 0) :
    √(d : ℝ) * (∑ x, |v x| ^ 2) ≤
      ∑ x ∈ U, ∑ y ∈ U, |v x| * huangCubeMatrix d x y * |v y|</pre></td></tr></tbody>
</table>

The theorem states the outer Rayleigh inequality √d‖|v|‖² ≤ |v|ᵀA_U|v| under the eigenvector/support hypotheses. It omits the displayed intermediate equalities through vᵀH′dv.

### 93. qm-maximal-support-block — weaker

Paper lines 2299–2299; `QuarticQuery.Paper.appendixA_sensitiveBlock_of_maximal_support` in `QuarticQuery/Paper/AppendixASensitivity.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The resulting function of \(S\) is nonconstant and therefore takes a value opposite to its value at \(x|_S\). The coordinates where such an assignment differs from \(x|_S\) form a nonempty block \(B\subseteq S\).</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_sensitiveBlock_of_maximal_support {f : TotalBool (Fin n)}
    {S : Finset (Fin n)} (hS : S.Nonempty)
    (hcoeff : fourierCoeff (fun x =&gt; bitVal ℝ (f x)) S ≠ 0)
    (hmax : ∀ T, S ⊂ T → fourierCoeff (fun x =&gt; bitVal ℝ (f x)) T = 0)
    (x : BitInput (Fin n)) :
    ∃ B : Finset (Fin n), B ⊆ S ∧ B.Nonempty ∧ IsSensitiveBlock f x B</pre></td></tr></tbody>
</table>

The theorem concludes existence of a nonempty sensitive B⊆S under maximal-support hypotheses. It does not state the sentence’s intermediate restricted-function nonconstancy or identify B as the difference set of a particular witness assignment.

### 94. qm-a-assembled — weaker

Paper lines 2316–2319; `QuarticQuery.Paper.appendixA_D_le_Q_pow_four` in `QuarticQuery/Paper/AppendixA.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 D(f)\le(1225Q(f)^2)(1225Q(f)^2)
       =1{,}500{,}625Q(f)^4.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {n : ℕ}

theorem appendixA_D_le_Q_pow_four (f : TotalBool (Fin n)) :
    D (totalise f) ≤ 1500625 * Q (totalise f) ^ 4</pre></td></tr></tbody>
</table>

The theorem gives D ≤ 1,500,625 Q^4 directly. The display additionally shows the factorization into two 1225 Q² terms; this intermediate product is in appendixA_D_le_of_QLe’s proof, not in this theorem’s statement.

### 95. rec-cl-local-history-constraints — different

Paper lines 2342–2343; `QuarticQuery.Paper.classicalLocalConsistent` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For each $h$, let $E_h(\tau)\subseteq D$ consist of the
inputs agreeing with every answer recorded from input $h$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

def classicalLocalConsistent (τ : ClassicalTranscript r κ) (h : Fin r)
    (x : BitInput κ) : Prop := ∀ e ∈ τ, e.1.1 = h → x e.1.2 = e.2</pre></td></tr></tbody>
</table>

classicalLocalConsistent tests the recorded answer equalities on the full Boolean cube; it does not itself require x∈D. Promise support is supplied by the prior μ.

### 96. rec-cl-conditional-product-law — weaker

Paper lines 2354–2360; `QuarticQuery.Paper.classical_prefix_iff` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 H_\tau=\bigcap_{h=1}^{r}\{U_h\in E_h(\tau)\},\qquad
 \Pr(H_\tau)=\prod_{h=1}^{r}\mu(E_h(\tau)),\qquad
 \mathcal L(U_1,\ldots,U_r\mid H_\tau)
   =\bigotimes_{h=1}^{r}\mu(\,\cdot\mid E_h(\tau)).
\tag{B.1}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem classical_prefix_iff {β : Type}
    (T : OutTree (Fin r × κ) β) (τ : ClassicalTranscript r κ)
    (U : Fin r → BitInput κ) :
    classicalPrefix T τ U ↔
      classicalSchedule T τ ∧ ∀ h, classicalLocalConsistent τ h (U h)</pre></td></tr></tbody>
</table>

The theorem gives the prefix-event equivalence with compatible schedule and local constraints. It does not give either probability identity in the rest of display (B.1).

### 97. rec-cl-conditional-product-law — weaker

Paper lines 2354–2360; `QuarticQuery.Paper.classical_mass_product` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 H_\tau=\bigcap_{h=1}^{r}\{U_h\in E_h(\tau)\},\qquad
 \Pr(H_\tau)=\prod_{h=1}^{r}\mu(E_h(\tau)),\qquad
 \mathcal L(U_1,\ldots,U_r\mid H_\tau)
   =\bigotimes_{h=1}^{r}\mu(\,\cdot\mid E_h(\tau)).
\tag{B.1}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem classical_mass_product (ν : Fin r → BitInput κ → ℝ) :
    (∑ U : Fin r → BitInput κ, ∏ h, ν h (U h)) =
      ∏ h, classicalMass (ν h)</pre></td></tr></tbody>
</table>

This is the finite product-mass identity after the transcript weight is factored. It does not itself identify the adaptive prefix event or state its normalized conditional law.

### 98. rec-cl-conditional-product-law — weaker

Paper lines 2354–2360; `QuarticQuery.Paper.classical_transcript_product_law` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 H_\tau=\bigcap_{h=1}^{r}\{U_h\in E_h(\tau)\},\qquad
 \Pr(H_\tau)=\prod_{h=1}^{r}\mu(E_h(\tau)),\qquad
 \mathcal L(U_1,\ldots,U_r\mid H_\tau)
   =\bigotimes_{h=1}^{r}\mu(\,\cdot\mid E_h(\tau)).
\tag{B.1}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem classical_transcript_product_law {β : Type}
    (T : OutTree (Fin r × κ) β) (τ : ClassicalTranscript r κ)
    (μ : Fin r → BitInput κ → ℝ)
    (hm : 0 &lt; ∑ V : Fin r → BitInput κ,
      if classicalPrefix T τ V then ∏ h, μ h (V h) else 0)
    (U : Fin r → BitInput κ) :
    (if classicalPrefix T τ U then ∏ h, μ h (U h) else 0) /
        (∑ V : Fin r → BitInput κ,
          if classicalPrefix T τ V then ∏ h, μ h (V h) else 0) =
      ∏ h, classicalLaw (classicalTranscriptWeight μ τ h) (U h)</pre></td></tr></tbody>
</table>

The theorem states the final conditional-law factorization in (B.1), deriving schedule compatibility from positive prefix mass. It does not package the preceding event equality and mass identity in its conclusion.

### 99. rec-cl-terminal-conditional-success — weaker

Paper lines 2458–2467; `QuarticQuery.guessSuccess_leaf` in `QuarticQuery/LowerBound/DirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\begin{aligned}
 \Pr[\mathcal A(U)=P^r(U)\mid H_\tau]
 &amp;=\prod_{h=1}^{r}\Pr[P(U_h)=s_h\mid H_\tau]\\
 &amp;\leq\prod_{h=1}^{r}\max_{b\in\{0,1\}}
               \Pr[P(U_h)=b\mid H_\tau]\\
 &amp;\leq\prod_{h=1}^{r}V_h(\tau)=Z(\tau),
\end{aligned}
\tag{B.5}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem guessSuccess_leaf (f : PartialBool κ) (ν : Fin r → BitInput κ → ℝ) (s : Fin r → Bool) :
    guessSuccess f ν (.leaf s) = ∏ h, constSuccess f (ν h) (s h)</pre></td></tr></tbody>
</table>

The declaration gives the fixed-output product equality for independent weights. The conditional transcript law is supplied by (B.1), and the two upper bounds are separate.

### 100. rec-cl-terminal-conditional-success — weaker

Paper lines 2458–2467; `QuarticQuery.Paper.classical_final_bound` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\begin{aligned}
 \Pr[\mathcal A(U)=P^r(U)\mid H_\tau]
 &amp;=\prod_{h=1}^{r}\Pr[P(U_h)=s_h\mid H_\tau]\\
 &amp;\leq\prod_{h=1}^{r}\max_{b\in\{0,1\}}
               \Pr[P(U_h)=b\mid H_\tau]\\
 &amp;\leq\prod_{h=1}^{r}V_h(\tau)=Z(\tau),
\end{aligned}
\tag{B.5}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]
variable {r : ℕ}

theorem classical_final_bound (f : PartialBool κ)
    (ν : Fin r → BitInput κ → ℝ) (c : Fin r → ℕ)
    (hν : ∀ h x, 0 ≤ ν h x) (s : Fin r → Bool) :
    guessSuccess f (fun h =&gt; classicalLaw (ν h)) (.leaf s) ≤
        ∏ h, max (constSuccess f (classicalLaw (ν h)) false)
          (constSuccess f (classicalLaw (ν h)) true) ∧
      (∏ h, max (constSuccess f (classicalLaw (ν h)) false)
          (constSuccess f (classicalLaw (ν h)) true)) ≤
        classicalProductValue f ν c</pre></td></tr></tbody>
</table>

The theorem states the two inequalities for the separately normalized local laws. It does not include the first equality or the explicit conditional-prefix notation in display (B.5).

### 101. rec-cl-normalized-weight-identity — weaker

Paper lines 2485–2491; `QuarticQuery.Paper.classicalValue` in `QuarticQuery/Paper/ClassicalDirectProduct.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 V_h(\tau)=\frac{W_{L-q_h(\tau)}(\nu_h^\tau)}{\mu(E_h(\tau))},
 \qquad
 \Pr(H_\tau)\,Z(\tau)
   =\prod_{h=1}^{r}W_{L-q_h(\tau)}(\nu_h^\tau).
\tag{B.6}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ]

noncomputable def classicalValue (f : PartialBool κ) (c : ℕ)
    (ν : BitInput κ → ℝ) : ℝ := budgetValue f c ν / classicalMass ν</pre></td></tr></tbody>
</table>

classicalValue defines the first ratio in (B.6). The second identity also needs the prefix mass product from (B.1) and cancellation of positive masses; it is not a conjunct of this declaration.

### 102. rec-cl-early-late-total-endpoint — weaker

Paper lines 2523–2529; `QuarticQuery.Paper.expectedZeros_le_four` in `QuarticQuery/Paper/ClassicalPlanted.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb EZ_{\mathrm{early}}\le\frac{2G}{m},
\qquad
Z_{\mathrm{late}}\le\frac{2G}{m},
\qquad
\mathbb EZ\le\frac{4G}{m}.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ] {ℓ r S : ℕ}

theorem expectedZeros_le_four {μ : BitInput κ → ℝ} (hμ : ∀ x, 0 ≤ μ x)
    (hμ1 : ∑ x, μ x = 1) {G : ℕ}
    (T : QueryTree (BitLoc ℓ r S κ)) (hT : T.depth ≤ G) :
    expectedZeros μ T ≤ 4 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ)</pre></td></tr></tbody>
</table>

Lean proves only the final total bound EZ≤4G/m. It does not define Z_early or Z_late and does not prove the two separately displayed early/late bounds.

### 103. rec-cl-total-discovery-factor-two — weaker

Paper lines 2569–2571; `QuarticQuery.Paper.expectedZeros_le_two` in `QuarticQuery/Paper/ClassicalPlanted.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb EZ\le\frac{2}{m}\mathbb E Q_X\le\frac{2G}{m}.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ] {ℓ r S : ℕ}

theorem expectedZeros_le_two {μ : BitInput κ → ℝ} (hμ : ∀ x, 0 ≤ μ x)
    (hμ1 : ∑ x, μ x = 1) {G : ℕ}
    (T : QueryTree (BitLoc ℓ r S κ)) (hT : T.depth ≤ G) :
    expectedZeros μ T ≤ 2 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ)</pre></td></tr></tbody>
</table>

The theorem states EZ≤2G/m. The displayed intermediate bound EZ≤(2/m)E Q_X is used through the per-column estimate and summed query-count proof, but is not a conjunct of this endpoint.

### 104. rec-cl-joint-success-and-cap — weaker

Paper lines 2609–2612; `QuarticQuery.direct_product_realized_caps_average` in `QuarticQuery/LowerBound/RealizedCaps.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
 \Pr\!\left[\mathcal A(U)=P^r(U)\ \text{and}\ E\right]\leq\beta^r.
\tag{B.8}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ] {r : ℕ}

theorem direct_product_realized_caps_average
    {S : Type} [Fintype S]
    {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ} {β : ℝ}
    (hμ : ∀ x, 0 ≤ μ x)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ β)
    {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) (hp1 : ∑ s, p s = 1)
    (T : S → OutTree (Fin r × κ) (Fin r → Bool)) :
    ∑ s, p s * compliantSuccess f μ (T s) (fun _ =&gt; L) ≤ β ^ r</pre></td></tr></tbody>
</table>

The theorem covers finite independent seeds and uses recursive actualComplies. Display (B.8) uses terminal count inequalities and permits unrestricted independent advice; neither the count-equivalence wrapper nor arbitrary measurable-seed transfer is stated here.

### 105. rec-cl-clipped-original-output — weaker

Paper lines 2618–2620; `QuarticQuery.OutTree.clip_eval_eq_of_actualComplies` in `QuarticQuery/LowerBound/RealizedCaps.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>On $E$, every prefix count is at most the terminal
count, so truncation never occurs and the two algorithms produce the same
output.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {κ : Type} [Fintype κ] [DecidableEq κ] {r : ℕ}

theorem clip_eval_eq_of_actualComplies {β : Type}
    (fallback : β) (T : OutTree (Fin r × κ) β)
    (c : Fin r → ℕ) (x : BitInput (Fin r × κ))
    (hc : actualComplies T c x) :
    (clip fallback T c).eval x = T.eval x</pre></td></tr></tbody>
</table>

Lean proves output preservation from recursive actualComplies. The paper derives that premise from the terminal-count event E; no count-compliance equivalence theorem is supplied in the packet.

### 106. rec-cl-appendix-fixed-time-inclusion — weaker

Paper lines 2641–2644; `QuarticQuery.eval_simTree` in `QuarticQuery/LowerBound/Planted/Simulator.lean`. Relation: `proof`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>If the original dummy run is nonheavy and its proposed query at a fixed
time is to a bit in the true-address cell, the simulator reaches that query without
truncation and outputs its address, so the joint event is contained in
simulator success.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι ρ β : Type}
variable {tgt : ι → Option ρ} {guess : ι → Option β} {dflt : β} {base : BitInput ι}

theorem eval_simTree (x : BitInput ι) (V : BitInput ρ)
    (hbase : ∀ q, tgt q = none → x q = base q) (hV : ∀ q p, tgt q = some p → x q = V p)
    (T : QueryTree ι) (t c : ℕ) {q : ι} {s : β} (hq : (T.path x)[t]? = some q)
    (hs : guess q = some s)
    (hc : ((T.path x).take t).countP (fun q =&gt; (tgt q).isSome) ≤ c) :
    (simTree tgt guess dflt base T t c).eval V = s</pre></td></tr></tbody>
</table>

The theorem proves correct simulator output assuming compatible answers and a prefix target-count bound. The specific nonheavy true-cell event implies those premises in the proof of eq_21; that event inclusion is not the general simulator theorem’s statement.

### 107. rec-cl-allowance-range — weaker

Paper lines 2811–2811; `QuarticQuery.one_le_Lvalue` in `QuarticQuery/Results/Exponent.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\(1\le L\le m\)</pre></td><td><pre>theorem one_le_Lvalue {k t : ℕ} (hk : 2 ≤ k) (ht : 8 ≤ t) : 1 ≤ Lvalue k t</pre></td></tr></tbody>
</table>

This declaration gives 1≤L under k≥2 and t≥8; the upper bound L≤m is the separate Lvalue_le_mValue theorem.

### 108. rec-cl-allowance-range — weaker

Paper lines 2811–2811; `QuarticQuery.Lvalue_le_mValue` in `QuarticQuery/Results/Exponent.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\(1\le L\le m\)</pre></td><td><pre>theorem Lvalue_le_mValue {k t : ℕ} (hk : 1 ≤ k) (ht : 1 ≤ t) : Lvalue k t ≤ mValue t</pre></td></tr></tbody>
</table>

This declaration gives L≤m (already under k≥1,t≥1), not the lower bound 1≤L. The two declarations together establish the displayed interval.

### 109. fr-coarse-advantage — different

Paper lines 2842–2848; `QuarticQuery.ForrelationLower.advantage_le_sharp_real_leaves_explicit` in `QuarticQuery/ForrelationLower/RealLeafExplicit.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\left|\mathbb E_{\nu_1}g-\mathbb E_{\mathcal U}g\right|
\le
\left(\frac{3}{\sqrt m}\right)^{k-1}
\left[\bigl(16kd\ln(4km)\bigr)^{k/2}+1\right]
\tag{C.1}
\]</pre></td><td><pre>theorem advantage_le_sharp_real_leaves_explicit
    {n : Type} [Fintype n] [DecidableEq n] {l d : ℕ}
    (H : Matrix n n ℝ) (hl : 0 &lt; l) (hH : RowsOrth H)
    {ε : ℝ} (hε : 0 ≤ ε) (hHb : ∀ a b, |H a b| ≤ ε)
    (hd : 1 ≤ d) (hn : 1 ≤ Fintype.card (BC l n))
    (T : RealQueryTree (BC l n)) (hT : T.depth ≤ d) (hbounded : T.Bounded) :
    |∫ u, ext T.eval (wv H 1 u) ∂(gP (PC l n)) - ext T.eval 0| ≤
      ((3 / 16 : ℝ) * ε) ^ l *
        ((Real.sqrt (16 * ((l + 1 : ℕ) : ℝ) * d *
            Real.log (4 * Fintype.card (BC l n)))) ^ (l + 1) +
          (1 / 2 : ℝ) ^ (l + 1))</pre></td></tr></tbody>
</table>

The theorem gives a sharper bound for one arbitrary bounded real-leaf tree and permits any row-orthogonal matrix H. The selected display, with its following quantifier, covers every tree or convex mixture for the Walsh matrix. Mixture closure is a further averaging argument, not a quantifier of this theorem.

### 110. fr-historical-hardness-closure — weaker

Paper lines 2923–2923; `QuarticQuery.ForrelationLower.bansalSinhaLower` in `QuarticQuery/ForrelationLower/Main.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Thus $L&lt;R(P_{k,4^t})$ for every $t\ge t_0$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {l t : ℕ}

theorem bansalSinhaLower : BansalSinhaLower</pre></td></tr></tbody>
</table>

The selected sentence uses the explicit t₀ from (C.2) with the paper’s choice τ=30k. bansalSinhaLower exports only existence of a sufficient t₀ and its proof chooses τ existentially. The general threshold witness is separately linked, but this theorem does not specify that repetition count or threshold.

### 111. fr-centered-exponential-moment — weaker

Paper lines 2998–3003; `QuarticQuery.ForrelationLower.two_point_exp_le` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\mathbb E e^{\lambda W}
\le \cosh(\lambda B)
\le e^{\lambda^2B^2/2}.
\tag{C.7}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}

theorem two_point_exp_le {p0 p1 a0 a1 B t : ℝ} (hp0 : 0 ≤ p0) (hp1 : 0 ≤ p1) (hp : p0 + p1 = 1)
    (hm : p0 * a0 + p1 * a1 = 0) (hB : 0 &lt; B) (h0 : |a0| ≤ B) (h1 : |a1| ≤ B) :
    p0 * Real.exp (t * a0) + p1 * Real.exp (t * a1) ≤ Real.exp (t ^ 2 * B ^ 2 / 2)</pre></td></tr></tbody>
</table>

The paper allows every centered W in [-B,B]. The theorem allows only a two-point law with probabilities p0,p1, values a0,a1, and B>0. It states the final exponential bound; the cosh comparison appears inside its proof.

### 112. fr-appendix-maximal-inequality — different

Paper lines 3016–3019; `QuarticQuery.ForrelationLower.hit_azuma` in `QuarticQuery/ForrelationLower/TreeGrowth.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\Pr\!\left(\max_{j\le d}|Z_j|&gt;R\right)
\le2\exp\!\left(-\frac{R^2}{2B^2d}\right).
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} [Fintype ι] [DecidableEq ι]
variable {μ : ι → ℝ}
variable {B₀ : ℝ} {ξ : ι → Bool → ℝ}

theorem hit_azuma (hμ : ∀ a, |μ a| ≤ 1)
    (hm : ∀ a, piB (μ a) false * ξ a false + piB (μ a) true * ξ a true = 0)
    (hB₀ : 0 &lt; B₀) (hξ : ∀ a b, |ξ a b| ≤ B₀)
    (Y : Finset ι → (ι → Bool) → ℝ) (Y' : ι → Finset ι → (ι → Bool) → ℝ)
    (hY : ∀ q Q x b, q ∉ Q →
      Y (insert q Q) (Function.update x q b) = Y Q x + ξ q b * Y' q Q x)
    {R β lam : ℝ} (hlam : 0 ≤ lam) (hβ : 0 ≤ β) (T : QueryTree ι) (d : ℕ) (hT : T.depth ≤ d)
    (Q : Finset ι) (x : ι → Bool) :
    hit μ (fun Q x =&gt; R &lt; Y Q x ∨ ∃ q, β &lt; |Y' q Q x|) T Q x ≤
      Real.exp (lam * (Y Q x - R) + lam ^ 2 * β ^ 2 * B₀ ^ 2 * d / 2) +
        hit μ (fun Q x =&gt; ∃ q, β &lt; |Y' q Q x|) T Q x</pre></td></tr></tbody>
</table>

This is the general two-sided martingale maximum bound. The named declaration instead gives a one-sided crossing estimate for a finite query tree with product-biased fresh signs and an explicit additive bad-coefficient probability; it is an implementation ingredient, not this generic theorem.

### 113. fr-uniform-small-errors — weaker

Paper lines 3038–3043; `QuarticQuery.ForrelationLower.eps_le` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\varepsilon\le18^{-k}=\frac{a_k}{18},
\qquad \delta\le\frac{a_k}{32},
\qquad \frac4{m\delta^2}\le\delta.
\tag{C.8}
\]</pre></td><td><pre>theorem eps_le (k : ℕ) : (8 / 9 : ℝ) ^ (25 * k) ≤ (1 / 18 : ℝ) ^ k</pre></td></tr></tbody>
</table>

This theorem supplies only ε≤18^{-k}; the selected display states three separate numerical estimates. The other two are linked independently with their own hypotheses.

### 114. fr-uniform-small-errors — weaker

Paper lines 3038–3043; `QuarticQuery.ForrelationLower.dl_le` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\varepsilon\le18^{-k}=\frac{a_k}{18},
\qquad \delta\le\frac{a_k}{32},
\qquad \frac4{m\delta^2}\le\delta.
\tag{C.8}
\]</pre></td><td><pre>theorem dl_le (l : ℕ) : 32 * dl (l + 1) ≤ (1 / 18 : ℝ) ^ l</pre></td></tr></tbody>
</table>

This theorem supplies only δ≤a_k/32; the selected display states three separate numerical estimates. The other two are linked independently with their own hypotheses.

### 115. fr-uniform-small-errors — weaker

Paper lines 3038–3043; `QuarticQuery.ForrelationLower.q_le` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\varepsilon\le18^{-k}=\frac{a_k}{18},
\qquad \delta\le\frac{a_k}{32},
\qquad \frac4{m\delta^2}\le\delta.
\tag{C.8}
\]</pre></td><td><pre>theorem q_le {l t : ℕ} (ht : 15 * (l + 1) + 2 ≤ 2 * t) :
    4 / dl (l + 1) ^ 2 * ((2 : ℝ) ^ (2 * t))⁻¹ ≤ dl (l + 1)</pre></td></tr></tbody>
</table>

This theorem supplies only 4/(mδ²)≤δ; the selected display states three separate numerical estimates. The other two are linked independently with their own hypotheses.

### 116. fr-fixed-threshold-comparison — weaker

Paper lines 3114–3124; `QuarticQuery.forrelation_lower_uniform_sharp` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\begin{aligned}
R(P_{k,4^t})
&amp;&gt;\frac2{18225}\,
   \frac{m^{1-1/k}}{k^2\ln(4km)}\\
&amp;\ge\frac{m^{1-1/k}}{54675k^2t}\\
&amp;&gt;\frac{m^{1-1/k}}{4t^2}
 \ge\left\lfloor\frac{m^{1-1/k}}{(2t)^2}\right\rfloor.
\end{aligned}
\tag{C.15}
\]</pre></td><td><pre>theorem forrelation_lower_uniform_sharp
    (k t : ℕ) (hk : 2 ≤ k) (ht : 15 * k + 2 ≤ 2 * t) :
    (2 / 18225 : ℝ) *
        Real.rpow (mValue t : ℝ) (1 - 1 / (k : ℝ)) /
        ((k : ℝ) ^ 2 * Real.log (4 * (k : ℝ) * (mValue t : ℝ))) &lt;
      (R (P k t) : ℝ)</pre></td></tr></tbody>
</table>

The theorem gives the first sharp lower bound under 15k+2≤2t. The selected chain additionally bounds its denominator, compares 54675k²t with 4t², and passes to the floor under t≥13669k²; those later comparisons are not its conclusion.

### 117. fr-fixed-threshold-comparison — weaker

Paper lines 3114–3124; `QuarticQuery.log_four_k_m_le` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\begin{aligned}
R(P_{k,4^t})
&amp;&gt;\frac2{18225}\,
   \frac{m^{1-1/k}}{k^2\ln(4km)}\\
&amp;\ge\frac{m^{1-1/k}}{54675k^2t}\\
&amp;&gt;\frac{m^{1-1/k}}{4t^2}
 \ge\left\lfloor\frac{m^{1-1/k}}{(2t)^2}\right\rfloor.
\end{aligned}
\tag{C.15}
\]</pre></td><td><pre>theorem log_four_k_m_le {k t : ℕ} (hk : 1 ≤ k) (hkt : k ≤ t) :
    Real.log (4 * (k : ℝ) * (mValue t : ℝ)) ≤ 6 * t</pre></td></tr></tbody>
</table>

The theorem states only ln(4km)≤6t for 1≤k≤t. It helps the second line of the selected chain, but does not assert a query lower bound or either final floor comparison.

### 118. fr-fixed-threshold-comparison — weaker

Paper lines 3114–3124; `QuarticQuery.lvalue_lt_R_explicit` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\begin{aligned}
R(P_{k,4^t})
&amp;&gt;\frac2{18225}\,
   \frac{m^{1-1/k}}{k^2\ln(4km)}\\
&amp;\ge\frac{m^{1-1/k}}{54675k^2t}\\
&amp;&gt;\frac{m^{1-1/k}}{4t^2}
 \ge\left\lfloor\frac{m^{1-1/k}}{(2t)^2}\right\rfloor.
\end{aligned}
\tag{C.15}
\]</pre></td><td><pre>theorem lvalue_lt_R_explicit (k t : ℕ) (hk : 2 ≤ k) (ht : 3499200 * k ^ 2 ≤ t) :
    Lvalue k t &lt; R (P k t)</pre></td></tr></tbody>
</table>

The displayed chain assumes k≥2 and t≥13669k² and ends at the floor allowance. The named floor theorem assumes the larger threshold t≥3499200k². Neither 13669 nor the optional ceiling threshold is exported in that theorem; the sharp suppliers are separate links.

### 119. fr-promise-values-exist — weaker

Paper lines 3130–3130; `QuarticQuery.ForrelationLower.exists_P_yes` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The lower bound also shows that both promise values occur in these dimensions</pre></td><td><pre>theorem exists_P_yes {l t : ℕ} (hl : 0 &lt; l) :
    ∃ z : BC l (Nm t) → Bool, P (l + 1) t z = some true</pre></td></tr></tbody>
</table>

This theorem gives a one-input for every t when k≥2. The selected phrase asserts that both promise values occur; the zero-input existence is a separate theorem with a dimension hypothesis.

### 120. fr-promise-values-exist — weaker

Paper lines 3130–3130; `QuarticQuery.ForrelationLower.exists_P_no` in `QuarticQuery/ForrelationLower/Uniform.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The lower bound also shows that both promise values occur in these dimensions</pre></td><td><pre>theorem exists_P_no {l t : ℕ} (ht : 10 * (l + 1) + 3 ≤ 2 * t) :
    ∃ z : BC l (Nm t) → Bool, P (l + 1) t z = some false</pre></td></tr></tbody>
</table>

This theorem gives a zero-input when 10k+3≤2t. The selected phrase asserts that both promise values occur; the one-input existence is supplied separately.

### 121. qm-acceptance-recursion — weaker

Paper lines 3364–3371; `QuarticQuery.Upper.tval` in `QuarticQuery/Upper/Tournament.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
\begin{aligned}
R_0(L)&amp;=V(L),\\
R_n(L)&amp;=f(L)V(L)+(1-f(L))\sum_i\frac{w_i}{W}R_{n-1}(i::L)
&amp;&amp; (n&gt;0,\ W&gt;0),\\
R_n(L)&amp;=V(L) &amp;&amp;(n&gt;0,\ W=0).
\end{aligned}
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {Col : Type} [Fintype Col]

noncomputable def tval (a : Col → Col → ℝ) (v : Col → ℝ) (f : List Col → ℝ) :
    ℕ → List Col → ℝ
  | 0, L =&gt; vall v L
  | T + 1, L =&gt; f L * vall v L +
      (1 - f L) * ∑ p, weight a L p / total (weight a L) * tval a v f T (p :: L)</pre></td></tr></tbody>
</table>

The definition gives the first two lines algebraically. The W=0 line additionally uses the paper’s premise f(L)=1; that premise is not part of the definition.

### 122. qm-acceptance-final — weaker

Paper lines 3394–3394; `QuarticQuery.Upper.tournament_runs` in `QuarticQuery/Upper/Tournament.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>At the empty history with $n=T_0=T$, the ideal estimate gives $I_T([])\leq2m/2^T$, and expanding the product in the lower bound and discarding its nonnegative cross term gives $R_T([])\geq1-2m/2^T-T\varepsilon-\varepsilon$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι Col : Type} [Fintype ι] [Inhabited ι] [Fintype Col] [DecidableEq Col]

theorem tournament_runs {cc cV : ℕ} {a : BitInput ι → Col → Col → ℝ} {v : BitInput ι → Col → ℝ}
    (hm : 2 ≤ Fintype.card Col) (hc : ∀ x, IsComparison (a x)) (hu : ∀ x, UnitValued (a x))
    (hcmp : ∀ i p, Samples cc fun x b =&gt; bern (a x i p) b)
    (hv : ∀ c, Runs cV fun x b =&gt; bern (v x c) b) (hv01 : ∀ x c, 0 ≤ v x c ∧ v x c ≤ 1) :
    let m := Fintype.card Col
    let T := Tval m
    let ε := epsval m
    ∃ val : BitInput ι → ℝ,
      Runs (T * stageCost m T cc ε + T * cV) (fun x b =&gt; bern (val x) b) ∧
      (∀ x, (∀ c, v x c ≤ ε) → val x ≤ T * ε) ∧
      (∀ x s, Dominant (a x) ε s → 1 - ε ≤ v x s →
        1 - 2 * (m : ℝ) / 2 ^ T - T * ε - ε ≤ val x)</pre></td></tr></tbody>
</table>

The theorem contains the final acceptance inequality and a realizing bounded program. It does not state the sentence’s intermediate ideal-miss estimate or the product-expansion step.

### 123. qm-amplifier-uniform — weaker

Paper lines 3404–3404; `QuarticQuery.Amplification.bounded_amplification` in `QuarticQuery/Amplification/Bounded.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>There is one procedure, depending only on these choices and using $A,A^{-1}$ as black boxes, with the following guarantees for every unitary preparation $A$ and every fixed input oracle.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {H : Type u} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

theorem bounded_amplification {γ η : ℝ} (hγ : 0 &lt; γ) (hγ1 : γ ≤ 1 / 2) (hη : 0 &lt; η)
    (hη1 : η &lt; 1 / 2) :
    (amplify γ η).callCap ≤ trialCount η * (2 * iterationBound γ + 1) ∧
    ((amplify γ η).callCap : ℝ) ≤ 138 * (Real.sqrt γ)⁻¹ * Real.log (1 / η) ∧
    ∀ {H : Type u} [NormedAddCommGroup H] [InnerProductSpace ℂ H] (A : Preparation H),
      (amplify γ η).successProb A + (amplify γ η).failProb A = 1 ∧
      (∀ h : Option H → ℝ, PhaseInvariant h →
        (amplify γ η).expect A h A.zero =
          (amplify γ η).successProb A * h (some A.goodState) +
          (amplify γ η).failProb A * h none) ∧
      (∀ k : H → ℝ, (∀ c : ℂ, ‖c‖ = 1 → ∀ v, k (c • v) = k v) →
        (amplify γ η).successProb A ≠ 0 →
        (amplify γ η).conditional A k = k A.goodState) ∧
      (amplify γ η).wrongStateMass A = 0 ∧
      (γ ≤ A.prob → (amplify γ η).failProb A ≤ η) ∧
      (A.prob = 0 → (amplify γ η).failProb A = 1)</pre></td></tr></tbody>
</table>

The theorem quantifies one abstract Proc before every Preparation and proves its state-observation laws and call cap. It does not itself give a physical AdaptiveProgram implementation on the stated finite interface.

### 124. qm-retained-subsystem — weaker

Paper lines 3406–3406; `QuarticQuery.Upper.uniformOpaqueAmplifier` in `QuarticQuery/Upper/UniformEndpoint.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The procedure returns failure or a state. On every successful return, one designated subsystem, with the same full register interface as $A$, contains the normalized success component of $A|0\rangle$, up to global phase.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {Z : Type} [Fintype Z]

theorem uniformOpaqueAmplifier
    (o : Z) (S : Z → Bool) {γ η : ℝ}
    (hγ : 0 &lt; γ) (hη : 0 &lt; η) (hηhalf : η &lt; 1 / 2) :
    let M := iterationBound γ
    let N := trialCount η
    let a₀ : Fin M := ⟨0, Nat.pos_of_ne_zero (iterationBound_ne_zero hγ)⟩
    ∃ V : Reg (Fin M) ≃ₗᵢ[ℂ] Reg (Fin M),
      V (rket a₀) = choiceState M ∧
      (∀ (ι : Type) [Nonempty ι] (n : ℕ)
          (F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          IsCirc n F →
          IsCirc (N * ((2 * (M - 1) + 1) * n))
            (fun x =&gt; finalB (N := N) V (F x) o S)) ∧
      ∀ U : Reg Z ≃ₗᵢ[ℂ] Reg Z,
        let A := prepOf U o (fun z =&gt; S z = true)
        let ψ := finalB (N := N) V U o S
          (rket (finalOrigin (N := N) a₀ o))
        let ξ := assembledOriginalAux (N := N) (⟨a₀, o⟩ : AmpTrial M Z) S
          (fun _ =&gt; opaqueTrialVector U o (fun z =&gt; S z = true) V a₀)
          (fun _ =&gt; trialSelectorGood A V a₀)
        coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ =
            retainedProduct ξ A.goodState ∧
        ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2 =
            1 - A.trialFail M ^ N ∧
        (A.prob = 0 →
          coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ = 0) ∧
        (0 &lt; A.prob → A.prob / 2 ≤
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (0 &lt; A.prob → ‖ξ‖ ^ 2 =
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (γ ≤ A.prob → 1 - η ≤
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (∀ (b : Fin N → Bool) (a : Fin M) (y : Fin N → AmpTrial M Z),
          firstSuccess b = none → ξ.ofLp (b, (a, y)) = 0) ∧
        coordProj (fun p : FinalAux N M Z =&gt;
          (firstSuccess p.1).isSome = true) ξ = ξ</pre></td></tr></tbody>
</table>

The concrete factorization theorem assumes a Boolean basis-label success predicate S and a basis origin o. The lemma’s surrounding statement allows any fixed free success projector; conversion of that interface is not in this declaration.

### 125. qm-amplified-label — different

Paper lines 3410–3410; `QuarticQuery.Paper.quantum_amplified_label_law` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>In particular, if success with classical label $b$ has unamplified probability $p_b$, measuring the retained label returns $b$ with probability $(1-f)p_b/p$ for $p&gt;0$, where $f$ is the amplifier’s failure probability.</pre></td><td><pre>theorem quantum_amplified_label_law {ι β : Type} [Fintype ι] [Inhabited ι] [Fintype β]
    {n : ℕ} {L : BitInput ι → Option β → ℝ} (h : Samples n L)
    {γ η : ℝ} (hγ : 0 &lt; γ) (hη : 0 &lt; η) :
    ∃ f : BitInput ι → ℝ,
      (∀ x, 0 ≤ f x ∧ f x ≤ 1) ∧
      (∀ x, γ ≤ ∑ b, L x (some b) → f x ≤ η) ∧
      (∀ x, ∑ b, L x (some b) = 0 → f x = 1) ∧
      Runs (trialCount η * (2 * ((2 * iterationBound γ + 1) * n)))
        (fun x =&gt; ampLaw (f x) (fun b =&gt; L x (some b)))</pre></td></tr></tbody>
</table>

The theorem constructs a bounded physical sampler with this classical label law from a Samples witness. It does not identify its measured register as the retained subsystem of the general-projector procedure in Lemma E.1.

### 126. qm-grover-state — weaker

Paper lines 3440–3445; `QuarticQuery.Paper.quantum_grover_state` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
G^j\psi
 =\sin((2j+1)\theta)g+\cos((2j+1)\theta)b,
\qquad
\Pr[\text{success after }j]=\sin^2((2j+1)\theta).
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

theorem quantum_grover_state (A : Preparation H) (h0 : 0 &lt; A.prob) (h1 : A.prob &lt; 1) :
    (0 &lt; A.angle ∧ A.angle &lt; Real.pi / 2) ∧
    ‖A.goodState‖ = 1 ∧ ‖A.badState‖ = 1 ∧
    A.good A.goodState = A.goodState ∧ A.good A.badState = 0 ∧
    inner ℂ A.goodState A.badState = 0 ∧
    A.state = ((Real.sin A.angle : ℝ) : ℂ) • A.goodState +
      ((Real.cos A.angle : ℝ) : ℂ) • A.badState ∧
    ∀ ℓ : ℕ,
      A.iterate ℓ =
        ((Real.sin ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.goodState +
        ((Real.cos ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.badState ∧
      (A.good (A.iterate ℓ) ≠ 0 →
        PhaseEq (normalised (A.good (A.iterate ℓ))) A.goodState)</pre></td></tr></tbody>
</table>

The theorem contains the displayed state expansion for 0<p<1, but does not state the displayed squared-norm probability formula; the companion declaration supplies it.

### 127. qm-grover-state — weaker

Paper lines 3440–3445; `QuarticQuery.Amplification.Preparation.norm_good_iterate_sq` in `QuarticQuery/Amplification/Geometry.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
G^j\psi
 =\sin((2j+1)\theta)g+\cos((2j+1)\theta)b,
\qquad
\Pr[\text{success after }j]=\sin^2((2j+1)\theta).
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
variable (A : Preparation H)

theorem norm_good_iterate_sq (ℓ : ℕ) :
    ‖A.good (A.iterate ℓ)‖ ^ 2 = Real.sin ((2 * ℓ + 1) * A.angle) ^ 2</pre></td></tr></tbody>
</table>

The theorem gives the probability equality, including endpoint probabilities, but does not give the display’s full state expansion.

### 128. qm-grover-success-state — weaker

Paper lines 3447–3447; `QuarticQuery.Paper.quantum_grover_state` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Projection onto success removes the $b$ term, so whenever success has nonzero probability the normalized result is $g$ or $-g$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

theorem quantum_grover_state (A : Preparation H) (h0 : 0 &lt; A.prob) (h1 : A.prob &lt; 1) :
    (0 &lt; A.angle ∧ A.angle &lt; Real.pi / 2) ∧
    ‖A.goodState‖ = 1 ∧ ‖A.badState‖ = 1 ∧
    A.good A.goodState = A.goodState ∧ A.good A.badState = 0 ∧
    inner ℂ A.goodState A.badState = 0 ∧
    A.state = ((Real.sin A.angle : ℝ) : ℂ) • A.goodState +
      ((Real.cos A.angle : ℝ) : ℂ) • A.badState ∧
    ∀ ℓ : ℕ,
      A.iterate ℓ =
        ((Real.sin ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.goodState +
        ((Real.cos ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.badState ∧
      (A.good (A.iterate ℓ) ≠ 0 →
        PhaseEq (normalised (A.good (A.iterate ℓ))) A.goodState)</pre></td></tr></tbody>
</table>

The declaration concludes PhaseEq, allowing any unit complex phase. The sentence identifies the phase more specifically as the real sign +1 or −1; that specificity is not in this theorem’s conclusion.

### 129. qm-grover-zero — weaker

Paper lines 3449–3449; `QuarticQuery.Paper.quantum_grover_zero` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>At $p=0$ the state lies in the failure subspace, where the success reflection fixes it; since the reflection about $\psi$ also fixes $\psi$, every iterate has zero success probability.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

theorem quantum_grover_zero (A : Preparation H) (h : A.prob = 0) (ℓ : ℕ) :
    A.good (A.iterate ℓ) = 0</pre></td></tr></tbody>
</table>

The declaration proves the zero successful projection for every iterate. It does not state the sentence’s separate fixed-vector explanations for the two reflections.

### 130. qm-repeated-failure — weaker

Paper lines 3511–3511; `QuarticQuery.Amplification.failProb_attempts` in `QuarticQuery/Amplification/Bounded.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Hence the probability of $N$ failures is $f^N\leq(31/40)^N\leq\eta$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {H : Type u} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

theorem failProb_attempts (A : Preparation H) {M : ℕ} (hM : M ≠ 0) (n : ℕ) :
    (attempts M n).failProb A = A.trialFail M ^ n</pre></td></tr></tbody>
</table>

The theorem proves the exact f^N identity under M≠0. The inequalities additionally use trialFail_le and the chosen N; neither numerical inequality is in this declaration.

### 131. qm-amplification-cap — weaker

Paper lines 3518–3522; `QuarticQuery.Paper.quantum_grover_call_cap` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\operatorname{calls}(\gamma,\eta)
\leq N(2M+1)
\leq138\,\gamma^{-1/2}\ln(1/\eta).
$$</pre></td><td><pre>theorem quantum_grover_call_cap (γ η : ℝ) :
    (amplify γ η).callCap ≤ trialCount η * (2 * iterationBound γ + 1)</pre></td></tr></tbody>
</table>

This theorem proves calls≤N(2M+1), without the logarithmic estimate. The companion declaration proves the second inequality.

### 132. qm-amplification-cap — weaker

Paper lines 3518–3522; `QuarticQuery.Paper.amplification_budget_le` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\operatorname{calls}(\gamma,\eta)
\leq N(2M+1)
\leq138\,\gamma^{-1/2}\ln(1/\eta).
$$</pre></td><td><pre>theorem amplification_budget_le {γ η : ℝ} (hγ : 0 &lt; γ) (hγ1 : γ ≤ 1 / 2)
    (hη : 0 &lt; η) (hη1 : η &lt; 1 / 2) :
    (trialCount η : ℝ) * (2 * (iterationBound γ : ℝ) + 1) ≤
      138 * (Real.sqrt γ)⁻¹ * Real.log (1 / η)</pre></td></tr></tbody>
</table>

This theorem proves N(2M+1)≤138 γ^(-1/2) log(1/η). It does not itself relate the product to the procedure’s callCap.

### 133. qm-positive-amplified-success — weaker

Paper lines 3526–3526; `QuarticQuery.Upper.uniformOpaqueAmplifier` in `QuarticQuery/Upper/UniformEndpoint.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>the total success probability is positive whenever $p&gt;0$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {Z : Type} [Fintype Z]

theorem uniformOpaqueAmplifier
    (o : Z) (S : Z → Bool) {γ η : ℝ}
    (hγ : 0 &lt; γ) (hη : 0 &lt; η) (hηhalf : η &lt; 1 / 2) :
    let M := iterationBound γ
    let N := trialCount η
    let a₀ : Fin M := ⟨0, Nat.pos_of_ne_zero (iterationBound_ne_zero hγ)⟩
    ∃ V : Reg (Fin M) ≃ₗᵢ[ℂ] Reg (Fin M),
      V (rket a₀) = choiceState M ∧
      (∀ (ι : Type) [Nonempty ι] (n : ℕ)
          (F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          IsCirc n F →
          IsCirc (N * ((2 * (M - 1) + 1) * n))
            (fun x =&gt; finalB (N := N) V (F x) o S)) ∧
      ∀ U : Reg Z ≃ₗᵢ[ℂ] Reg Z,
        let A := prepOf U o (fun z =&gt; S z = true)
        let ψ := finalB (N := N) V U o S
          (rket (finalOrigin (N := N) a₀ o))
        let ξ := assembledOriginalAux (N := N) (⟨a₀, o⟩ : AmpTrial M Z) S
          (fun _ =&gt; opaqueTrialVector U o (fun z =&gt; S z = true) V a₀)
          (fun _ =&gt; trialSelectorGood A V a₀)
        coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ =
            retainedProduct ξ A.goodState ∧
        ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2 =
            1 - A.trialFail M ^ N ∧
        (A.prob = 0 →
          coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ = 0) ∧
        (0 &lt; A.prob → A.prob / 2 ≤
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (0 &lt; A.prob → ‖ξ‖ ^ 2 =
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (γ ≤ A.prob → 1 - η ≤
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (∀ (b : Fin N → Bool) (a : Fin M) (y : Fin N → AmpTrial M Z),
          firstSuccess b = none → ξ.ofLp (b, (a, y)) = 0) ∧
        coordProj (fun p : FinalAux N M Z =&gt;
          (firstSuccess p.1).isSome = true) ξ = ξ</pre></td></tr></tbody>
</table>

The concrete theorem gives the stronger numerical bound success≥p/2, but only for a basis-label success predicate S; the surrounding paper statement allows an arbitrary fixed success projector.

### 134. qm-retained-factor — weaker

Paper lines 3531–3531; `QuarticQuery.Upper.uniformOpaqueAmplifier` in `QuarticQuery/Upper/UniformEndpoint.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>If the history is retained coherently, the phase of each history can be absorbed into its auxiliary amplitude: after the fixed routing, the unnormalized successful component factors as $g\otimes\xi$, with $\|\xi\|^2$ equal to the success probability.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {Z : Type} [Fintype Z]

theorem uniformOpaqueAmplifier
    (o : Z) (S : Z → Bool) {γ η : ℝ}
    (hγ : 0 &lt; γ) (hη : 0 &lt; η) (hηhalf : η &lt; 1 / 2) :
    let M := iterationBound γ
    let N := trialCount η
    let a₀ : Fin M := ⟨0, Nat.pos_of_ne_zero (iterationBound_ne_zero hγ)⟩
    ∃ V : Reg (Fin M) ≃ₗᵢ[ℂ] Reg (Fin M),
      V (rket a₀) = choiceState M ∧
      (∀ (ι : Type) [Nonempty ι] (n : ℕ)
          (F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          IsCirc n F →
          IsCirc (N * ((2 * (M - 1) + 1) * n))
            (fun x =&gt; finalB (N := N) V (F x) o S)) ∧
      ∀ U : Reg Z ≃ₗᵢ[ℂ] Reg Z,
        let A := prepOf U o (fun z =&gt; S z = true)
        let ψ := finalB (N := N) V U o S
          (rket (finalOrigin (N := N) a₀ o))
        let ξ := assembledOriginalAux (N := N) (⟨a₀, o⟩ : AmpTrial M Z) S
          (fun _ =&gt; opaqueTrialVector U o (fun z =&gt; S z = true) V a₀)
          (fun _ =&gt; trialSelectorGood A V a₀)
        coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ =
            retainedProduct ξ A.goodState ∧
        ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2 =
            1 - A.trialFail M ^ N ∧
        (A.prob = 0 →
          coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ = 0) ∧
        (0 &lt; A.prob → A.prob / 2 ≤
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (0 &lt; A.prob → ‖ξ‖ ^ 2 =
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (γ ≤ A.prob → 1 - η ≤
          ‖coordProj (finalSuccess (M := M) (N := N) (Z := Z)) ψ‖ ^ 2) ∧
        (∀ (b : Fin N → Bool) (a : Fin M) (y : Fin N → AmpTrial M Z),
          firstSuccess b = none → ξ.ofLp (b, (a, y)) = 0) ∧
        coordProj (fun p : FinalAux N M Z =&gt;
          (firstSuccess p.1).isSome = true) ξ = ξ</pre></td></tr></tbody>
</table>

The theorem proves the factorization for a Boolean basis-label success predicate S, with auxiliary and original factors ordered ξ⊗g. The general-projector interface in the paper is not established by this declaration; equality of auxiliary norm and success is asserted when p>0.

### 135. qm-controlled-grover — weaker

Paper lines 3534–3537; `QuarticQuery.Upper.slice_opaqueSlot` in `QuarticQuery/Upper/OpaqueSlot.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
(Z_c\otimes I)(I\otimes A)C(S_0)(I\otimes A^{-1})C(S_\chi)
=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes G.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι Λ Z : Type} [Fintype Λ] [Fintype Z]

theorem slice_opaqueSlot (U : Reg Z ≃ₗᵢ[ℂ] Reg Z)
    (o : Z) (S : Z → Prop) (P : Λ → Prop) [DecidablePred P]
    (a : Λ) (ψ : Reg (Σ _ : Λ, Z)) :
    slice a (opaqueSlot U o S P ψ) =
      if P a then circU U o S Amplification.groverStep (slice a ψ)
      else slice a ψ</pre></td></tr></tbody>
</table>

The slice identity proves this controlled product for coordinate-subspace reflection signU S and a basis origin o. The paper’s display is stated under the broader fixed-projector interface.

### 136. qm-list-budget — weaker

Paper lines 3634–3638; `QuarticQuery.Paper.quantumTournament_cost` in `QuarticQuery/Paper/QuantumTournamentFacts.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
 B_{\mathrm{list}}
 =2T^2c_{\mathrm{rd}}N(2M_0+1)
 \leq6072\,c_{\mathrm{rd}}\sqrt m\,T^2\ln T.
$$</pre></td><td><pre>theorem quantumTournament_cost {m : ℕ} (hm : 2 ≤ m) (cc : ℕ) :
    ((Tval m * stageCost m (Tval m) cc (epsval m) : ℕ) : ℝ) ≤
      6072 * (cc : ℝ) * Real.sqrt (m : ℝ) *
        (Tval m : ℝ) ^ 2 * Real.log (Tval m : ℝ)</pre></td></tr></tbody>
</table>

The theorem proves the displayed upper bound for T·stageCost. The displayed equality to 2T² c_rd N(2M₀+1) requires unfolding stageCost and the parameter definitions; it is not an explicit equality in the theorem statement.

### 137. qm-pointer-essential — weaker

Paper lines 3678–3678; `QuarticQuery.Paper.construction_pointer_every_physical_coordinate` in `QuarticQuery/Paper/ConstructionPointerSupport.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>For one pointer test, the complete relevant coordinate set consists of the $\ell$ pointer bits and all $m$ bits of the target column, and each of them is essential when $\ell\geq1$.</pre></td><td><pre>theorem construction_pointer_every_physical_coordinate {κ : Type} (C : Circuit κ)
    (ℓ r : ℕ) (i : Column ℓ) (s : Address r) (e : Fin (2 ^ ℓ - 1))
    (q : Fin ℓ ⊕ Column ℓ) :
    ∃ X Y : BitInput (BitLoc ℓ r C.size κ),
      (∀ p, p ≠ constructionPointerLoc C ℓ r i s e q → X p = Y p) ∧
        localTest C ℓ r X i s (.inr (.inl e)) ≠
          localTest C ℓ r Y i s (.inr (.inl e))</pre></td></tr></tbody>
</table>

The theorem proves that every listed physical coordinate is essential. It does not also state that no other coordinate is relevant; that upper-support conclusion comes from the pointer-test definition.

### 138. qm-coherent-local-physical — different

Paper lines 3705–3705; `QuarticQuery.Paper.construction_controlled_compile` in `QuarticQuery/Paper/ConstructionCoherent.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>This proves the arbitrary-index coherent part of OpenAI’s Lemma 2.2, with retained workspace and at most $2(\ell+1)$ ordinary bit queries for $m\geq4$.</pre></td><td><pre>theorem construction_controlled_compile {ι Γ : Type} [Fintype ι] [Inhabited ι]
    [Fintype Γ] {Z : Γ → Type} [∀ e, Fintype (Z e)] {n w : ℕ}
    (F : ∀ e, BitInput ι → Reg (Z e) ≃ₗᵢ[ℂ] Reg (Z e))
    (hF : ∀ e, IsCirc n (F e)) (emb : (Σ e, Z e) ↪ Fin (w + 1)) :
    ∃ P : AdaptiveProgram ι w → AdaptiveProgram ι w, ∀ next,
      (P next).queryCap ≤ 2 * n + next.queryCap ∧
      ∀ x ψ b, (P next).outputMass x (clEmb emb ψ) b =
        next.outputMass x (clEmb emb (sigmaOp (fun e =&gt; F e x) ψ)) b</pre></td></tr></tbody>
</table>

The theorem compiles any given indexed IsCirc n family with cap 2n. It does not itself supply local-test circuits or simplify max{3,ℓ+1}=ℓ+1; construction_lemma_2_2_ii and ℓ≥2 provide those steps.

### 139. qm-uniform-test-law — weaker

Paper lines 3724–3724; `QuarticQuery.Upper.testLaw` in `QuarticQuery/Upper/Verify.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>If $h$ tests fail, a failed test is observed with probability $h/K$, because the index blocks are orthogonal and each test is exact.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {k t : ℕ} {C : Circuit (ForrelationCoord k t)}

noncomputable def testLaw (x : BitInput (Loc k t C)) (i : Col t) (s : Addr t)
    (o : Option (Tests t C)) : ℝ :=
  ∑ e, (Fintype.card (Tests t C) : ℝ)⁻¹ * pt (testRes x i s e) o</pre></td></tr></tbody>
</table>

The definition explicitly sums the uniform exact-test law. The h/K count and its coherent orthogonality explanation are consequences, not separate conclusions of this definition.

### 140. qm-two-query-circuit — weaker

Paper lines 3747–3747; `QuarticQuery.Paper.quantum_compile_circuit` in `QuarticQuery/Paper/QuantumAmplification.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Composing these read implementations adds their caps, and reversing their logical circuit uses the same number of reads, so a circuit of $q$ logical reads is implemented with at most $2q$ ordinary bit queries, also when its indices are superposed.</pre></td><td><pre>theorem quantum_compile_circuit {ι Z : Type} [Fintype ι] [Inhabited ι]
    [Fintype Z] {w n : ℕ} (e : Z ↪ Fin (w + 1))
    {F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z} (hF : IsCirc n F) :
    ∃ P : AdaptiveProgram ι w → AdaptiveProgram ι w, ∀ next,
      (P next).queryCap ≤ 2 * n + next.queryCap ∧
      ∀ x ψ b, (P next).outputMass x (clEmb e ψ) b =
        next.outputMass x (clEmb e (F x ψ)) b</pre></td></tr></tbody>
</table>

The theorem states the physical 2q compilation bound and continuation-mass equality. The sentence’s separate equal-cost claim for logical inversion is supplied by quantum_inverse_reads.

### 141. qm-classical-minima — weaker

Paper lines 3862–3866; `QuarticQuery.R_le_iff` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f)\leq q\iff R_{\leq}(f,q),\qquad
D(f)\leq q\iff D_{\leq}(f,q),\qquad
R(f)\leq D(f)\leq |I|.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}
variable [Fintype ι]

theorem R_le_iff {f : PartialBool ι} {t : ℕ} : R f ≤ t ↔ RLe f t</pre></td></tr></tbody>
</table>

This declaration proves only R(f)≤q iff RLe f q; the display also contains the deterministic equivalence and R≤D≤|I|.

### 142. qm-classical-minima — weaker

Paper lines 3862–3866; `QuarticQuery.D_le_iff` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f)\leq q\iff R_{\leq}(f,q),\qquad
D(f)\leq q\iff D_{\leq}(f,q),\qquad
R(f)\leq D(f)\leq |I|.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}
variable [Fintype ι]

theorem D_le_iff {f : PartialBool ι} {t : ℕ} : D f ≤ t ↔ DLe f t</pre></td></tr></tbody>
</table>

This declaration proves only D(f)≤q iff DLe f q; the display also contains the randomized equivalence and R≤D≤|I|.

### 143. qm-classical-minima — weaker

Paper lines 3862–3866; `QuarticQuery.R_le_D` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f)\leq q\iff R_{\leq}(f,q),\qquad
D(f)\leq q\iff D_{\leq}(f,q),\qquad
R(f)\leq D(f)\leq |I|.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}
variable [Fintype ι]

theorem R_le_D (f : PartialBool ι) : R f ≤ D f</pre></td></tr></tbody>
</table>

This declaration proves only R(f)≤D(f); the two budget equivalences and the cardinality upper bound are supplied by the other links.

### 144. qm-classical-minima — weaker

Paper lines 3862–3866; `QuarticQuery.D_le_card` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f)\leq q\iff R_{\leq}(f,q),\qquad
D(f)\leq q\iff D_{\leq}(f,q),\qquad
R(f)\leq D(f)\leq |I|.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}
variable [Fintype ι]

theorem D_le_card (f : PartialBool ι) : D f ≤ Fintype.card ι</pre></td></tr></tbody>
</table>

This declaration proves only D(f)≤|I|; it does not state R≤D or either budget equivalence.

### 145. qm-projection-mass — weaker

Paper lines 3892–3892; `QuarticQuery.norm_sq_eq_project_add` in `QuarticQuery/Model/Quantum.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>A two-outcome measurement uses the branches $\Pi_S\psi$ and $(I-\Pi_S)\psi$. These span orthogonal subspaces and have squared norms summing to $\|\psi\|^2$.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem norm_sq_eq_project_add (S : Finset (Basis ι w)) (ψ : State ι w) :
    ‖ψ‖ ^ 2 = ‖project S ψ‖ ^ 2 + ‖ψ - project S ψ‖ ^ 2</pre></td></tr></tbody>
</table>

The declaration states the squared-norm sum identity for the displayed two components. It does not separately assert their orthogonality or define the measurement branches.

### 146. qm-quantum-mass-laws — weaker

Paper lines 3912–3916; `QuarticQuery.AdaptiveProgram.outputMass_nonneg` in `QuarticQuery/Model/Quantum.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
M_A(x,\psi,b)\geq0,
\qquad
M_A(x,\psi,1)+M_A(x,\psi,0)=\|\psi\|^2.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem outputMass_nonneg (A : AdaptiveProgram ι w) (x : BitInput ι) (ψ : State ι w) (b : Bool) :
    0 ≤ A.outputMass x ψ b</pre></td></tr></tbody>
</table>

The theorem proves nonnegativity of each output mass, but not the display’s total-mass equality.

### 147. qm-quantum-mass-laws — weaker

Paper lines 3912–3916; `QuarticQuery.AdaptiveProgram.outputMass_true_add_false` in `QuarticQuery/Model/Quantum.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
M_A(x,\psi,b)\geq0,
\qquad
M_A(x,\psi,1)+M_A(x,\psi,0)=\|\psi\|^2.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem outputMass_true_add_false (A : AdaptiveProgram ι w) (x : BitInput ι) (ψ : State ι w) :
    A.outputMass x ψ true + A.outputMass x ψ false = ‖ψ‖ ^ 2</pre></td></tr></tbody>
</table>

The theorem proves the total-mass equality, but does not separately state nonnegativity of each output mass.

### 148. qm-tree-quantum-simulation — weaker

Paper lines 3935–3935; `QuarticQuery.AdaptiveProgram.outputMass_ofTree` in `QuarticQuery/Model/Quantum.lean`. Relation: `states`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Induction on the tree gives the same output and no larger cap.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem AdaptiveProgram.outputMass_ofTree (p : Basis ι w) (t : QueryTree ι) (x : BitInput ι)
    (b : Bool) : (ofTree p t).outputMass x (ket p) b = if t.eval x = b then 1 else 0</pre></td></tr></tbody>
</table>

The theorem gives the exact output law of the tree simulation. Its cap equality is a separate theorem queryCap_ofTree and is not stated here.

### 149. qm-quantum-minima — weaker

Paper lines 3937–3941; `QuarticQuery.Q_le_D` in `QuarticQuery/Model/Quantum.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
Q(f)\leq D(f)\leq |I|,
\qquad
Q(f)\leq q\iff q\text{ is admissible for }f.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem Q_le_D (f : PartialBool ι) : Q f ≤ D f</pre></td></tr></tbody>
</table>

The theorem supplies Q(f)≤D(f), but not D(f)≤|I| or the admissible-budget equivalence.

### 150. qm-quantum-minima — weaker

Paper lines 3937–3941; `QuarticQuery.D_le_card` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
Q(f)\leq D(f)\leq |I|,
\qquad
Q(f)\leq q\iff q\text{ is admissible for }f.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}
variable [Fintype ι]

theorem D_le_card (f : PartialBool ι) : D f ≤ Fintype.card ι</pre></td></tr></tbody>
</table>

The theorem supplies D(f)≤|I|, but not Q(f)≤D(f) or the quantum-budget equivalence.

### 151. qm-quantum-minima — weaker

Paper lines 3937–3941; `QuarticQuery.Q_le_iff` in `QuarticQuery/Model/Quantum.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
Q(f)\leq D(f)\leq |I|,
\qquad
Q(f)\leq q\iff q\text{ is admissible for }f.
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem Q_le_iff {f : PartialBool ι} {t : ℕ} : Q f ≤ t ↔ QLe f t</pre></td></tr></tbody>
</table>

The theorem supplies Q(f)≤q iff QLe f q, but not the comparison with D or the coordinate count.

### 152. qm-reindex-complexities — weaker

Paper lines 3954–3956; `QuarticQuery.R_reindex` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f^e)=R(f),\qquad D(f^e)=D(f),\qquad Q(f^e)=Q(f).
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}

theorem R_reindex [Fintype ι] [Fintype κ] (e : ι ≃ κ) (f : PartialBool ι) :
    R (reindex e f) = R f</pre></td></tr></tbody>
</table>

This theorem states only randomized invariance; the other two displayed equalities require the companion declarations.

### 153. qm-reindex-complexities — weaker

Paper lines 3954–3956; `QuarticQuery.D_reindex` in `QuarticQuery/Model/Classical.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f^e)=R(f),\qquad D(f^e)=D(f),\qquad Q(f^e)=Q(f).
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ α : Type}

theorem D_reindex [Fintype ι] [Fintype κ] (e : ι ≃ κ) (f : PartialBool ι) :
    D (reindex e f) = D f</pre></td></tr></tbody>
</table>

This theorem states only deterministic invariance; the other two displayed equalities require the companion declarations.

### 154. qm-reindex-complexities — weaker

Paper lines 3954–3956; `QuarticQuery.Q_reindex` in `QuarticQuery/Model/Quantum.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(f^e)=R(f),\qquad D(f^e)=D(f),\qquad Q(f^e)=Q(f).
\]</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι κ : Type} {w : ℕ}
variable [Fintype ι] [Fintype κ]

theorem Q_reindex (e : ι ≃ κ) (f : PartialBool ι) : Q (QuarticQuery.reindex e f) = Q f</pre></td></tr></tbody>
</table>

This theorem states only quantum invariance; the other two displayed equalities require the companion declarations.

### 155. qm-deferred-padding — weaker

Paper lines 3980–3980; `QuarticQuery.exists_fixedSequence` in `QuarticQuery/Bridge/Deferred.lean`. Relation: `contains`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The output case allows both measurement continuations to be padded to the same $T$, so structural induction gives the displayed mass identity with exactly $T$ queries.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {N w : ℕ} {W W₁ W₂ : Type}
variable [Fintype W₁] [Fintype W₂]

theorem exists_fixedSequence (A : AdaptiveProgram (Fin N) w) {T : ℕ} (hT : A.queryCap ≤ T) :
    ∃ (W' : Type) (_ : Fintype W') (entry : State (Fin N) w →ₗᵢ[ℂ] QState N W')
      (U : ℕ → QState N W' →ₗᵢ[ℂ] QState N W') (S : Finset (Fin N × Bool × W')),
      ∀ (x : BitInput (Fin N)) (ψ : State (Fin N) w),
        measureProb (run U (entry ψ) x T) S = A.outputMass x ψ true</pre></td></tr></tbody>
</table>

The theorem concludes the exactly-T mass identity. Its statement does not include the sentence’s structural-induction explanation or the padding construction for individual branches.

### 156. qm-identity-values — weaker

Paper lines 4007–4009; `QuarticQuery.Independent.ModelZero.identity_Q_eq_one` in `QuarticCorpus/Independent/ModelZero/Proof.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
D(\mathrm{id}_1)=R(\mathrm{id}_1)=Q(\mathrm{id}_1)=1.
\]</pre></td><td><pre>theorem identity_Q_eq_one : Q SemanticReview.oneBitIdentity = 1</pre></td></tr></tbody>
</table>

The declaration states only Q(id₁)=1. It does not state the displayed deterministic or randomized equalities.

### 157. qm-or-success-table — weaker

Paper lines 4020–4023; `QuarticQuery.SemanticReview.orMixture_success` in `QuarticCorpus/Independent/Semantics.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>| $00$ | 0 | 1 | 0 | 0 | $2/3$ |
| $01$ | 1 | 1 | 0 | 1 | $2/3$ |
| $10$ | 1 | 1 | 1 | 0 | $2/3$ |
| $11$ | 1 | 1 | 1 | 1 | $1$ |</pre></td><td><pre>theorem orMixture_success (x : BitInput (Fin 2)) :
    orMixture.success x (x 0 || x 1) =
      if x 0 &amp;&amp; x 1 then (1 : ℝ) else 2 / 3</pre></td></tr></tbody>
</table>

The theorem states exactly the four success-probability values. The selected table also lists the OR value and each component tree’s output, which follow from their definitions rather than this theorem’s conclusion.

### 158. qm-or-complexities — weaker

Paper lines 4027–4029; `QuarticQuery.SemanticReview.orTwo_R_eq_one` in `QuarticCorpus/Independent/Semantics.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>\[
R(\mathrm{OR}_2)=1,\qquad D(\mathrm{OR}_2)=2.
\]</pre></td><td><pre>theorem orTwo_R_eq_one : R orTwo = 1</pre></td></tr></tbody>
</table>

The declaration proves R(OR₂)=1 only. It does not prove the display’s D(OR₂)=2 component.

### 159. qm-one-sided-values — weaker

Paper lines 4038–4038; `QuarticQuery.SemanticReview.trueOnly_R_eq_zero` in `QuarticCorpus/Independent/Semantics.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Consequently $D(f)=R(f)=Q(f)=0$.</pre></td><td><pre>theorem trueOnly_R_eq_zero : R trueOnly = 0</pre></td></tr></tbody>
</table>

This theorem states only R(trueOnly)=0. The displayed D and Q values are separate; Q has the companion direct declaration, while D follows from the general zero-query characterization.

### 160. qm-one-sided-values — weaker

Paper lines 4038–4038; `QuarticQuery.SemanticReview.trueOnly_Q_eq_zero` in `QuarticCorpus/Independent/Semantics.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>Consequently $D(f)=R(f)=Q(f)=0$.</pre></td><td><pre>theorem trueOnly_Q_eq_zero : Q trueOnly = 0</pre></td></tr></tbody>
</table>

This theorem states only Q(trueOnly)=0. The displayed D and R values are separate; R has the companion direct declaration, while D follows from the general zero-query characterization.

### 161. qr-integer-normalization — weaker

Paper lines 4077–4085; `QuarticQuery.Paper.construction_N_phi` in `QuarticQuery/Paper/ConstructionForrelationDefinitions.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{aligned}
N(z)&amp;=\sum_{(a_0,\ldots,a_{k-1})\in\mathcal X^k}
  \left(\prod_{r=0}^{k-1}z_r(a_r)\right)
  \left(\prod_{r=0}^{k-2}W_{a_r,a_{r+1}}\right)\in\mathbb Z,\\
M&amp;=m(\sqrt m)^{k-1}=2^{t(k+1)}&gt;0,
\qquad \Phi(z)=\frac{N(z)}{M}.
\end{aligned}
$$</pre></td><td><pre>theorem construction_N_phi (k t : ℕ) (hk : 1 ≤ k)
    (z : BitInput (ForrelationCoord k t)) :
    (forrelationNumerator k t z : ℝ) =
      (fun _ : Fin (mValue t) =&gt; (1 : ℝ)) ⬝ᵥ
        (alternate (W t) (List.ofFn fun h : Fin k =&gt; signDiag z h) *ᵥ
          fun _ =&gt; (1 : ℝ)) ∧
    Phi k t z = (forrelationNumerator k t z : ℝ) / (forrelationDenominator k t : ℝ) ∧
    0 &lt; forrelationDenominator k t ∧
    (forrelationDenominator k t : ℝ) =
      (mValue t : ℝ) * (Real.sqrt (mValue t : ℝ)) ^ (k - 1) ∧
    W t = Real.sqrt (mValue t : ℝ) • H t ∧
    (∀ i j : Fin (mValue t), W t i j = 1 ∨ W t i j = -1)</pre></td></tr></tbody>
</table>

The type gives N as the unnormalized matrix product, Φ=N/M, positivity and M=m(√m)^(k−1). The path sum is the definition of N; the additional equality M=2^{t(k+1)} is in denominator_eq.

### 162. qr-integer-normalization — weaker

Paper lines 4077–4085; `QuarticQuery.Forrelation.denominator_eq` in `QuarticQuery/Forrelation/Circuit.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{aligned}
N(z)&amp;=\sum_{(a_0,\ldots,a_{k-1})\in\mathcal X^k}
  \left(\prod_{r=0}^{k-1}z_r(a_r)\right)
  \left(\prod_{r=0}^{k-2}W_{a_r,a_{r+1}}\right)\in\mathbb Z,\\
M&amp;=m(\sqrt m)^{k-1}=2^{t(k+1)}&gt;0,
\qquad \Phi(z)=\frac{N(z)}{M}.
\end{aligned}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

theorem denominator_eq (l t : ℕ) :
    forrelationDenominator (l + 1) t = 2 ^ (t * (l + 2))</pre></td></tr></tbody>
</table>

This type gives only M=2^{t(k+1)} after k=l+1; it omits the numerator, positivity and real normalization clauses.

### 163. qr-small-binomial-tail — weaker

Paper lines 4151–4158; `QuarticQuery.Forrelation.binomTail_small` in `QuarticQuery/Forrelation/Repetition.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{aligned}
\Pr[S\ge qc/2]
&amp;\le e^{-qc/2}\mathbb E e^S\\
&amp;\le\exp\bigl(-qc/2+qp(e-1)\bigr)
\le e^{-qc/16}.
\end{aligned}
$$</pre></td><td><pre>theorem binomTail_small (n : ℕ) {p c : ℝ} (h0 : 0 ≤ p) (h1 : p ≤ 1)
    (hp : p ≤ c / 4) : binomTail n p (n * (c / 2)) ≤ Real.exp (-(n * c / 16))</pre></td></tr></tbody>
</table>

The type states the final error bound exp(−qc/16); the intermediate exponential-moment inequalities in the selected display occur in supporting lemmas and proof steps.

### 164. qr-large-binomial-tail — weaker

Paper lines 4162–4169; `QuarticQuery.Forrelation.binomTail_large` in `QuarticQuery/Forrelation/Repetition.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{aligned}
\Pr[S&lt;qc/2]
&amp;\le e^{qc/2}\mathbb E e^{-S}\\
&amp;\le\exp\bigl(qc/2-qp(1-e^{-1})\bigr)
\le e^{-qc/10}\le e^{-qc/16},
\end{aligned}
$$</pre></td><td><pre>theorem binomTail_large (n : ℕ) {p c : ℝ} (h1 : p ≤ 1) (hc : 0 &lt; c) (hp : c ≤ p) :
    1 - binomTail n p (n * (c / 2)) ≤ Real.exp (-(n * c / 16))</pre></td></tr></tbody>
</table>

The type states exp(−qc/16); it does not state the stronger intermediate exp(−qc/10) bound or the displayed moment chain.

### 165. qr-sharp-physical-decoder-cap — weaker

Paper lines 4225–4228; `QuarticQuery.Paper.construction_decoder_sharp` in `QuarticQuery/Paper/ConstructionForrelationSharp.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
Q_\eta(P_{k,m})\le k\left\lceil16\,2^{10k}\ln(1/\eta)\right\rceil
 =O_k(1+\log(1/\eta)).
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type} {k t : ℕ}

theorem construction_decoder_sharp (k t : ℕ) (hk : 1 ≤ k)
    (η : ℝ) (hη : 0 &lt; η) :
    ∃ (n : ℕ), n = repetitions k η ∧
      ∃ (Z : Type) (instZ : Fintype Z),
        let _ := instZ
        ∃ (o : Z) (out : Z → Bool)
          (F : BitInput (ForrelationCoord k t) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          IsCirc (n * k) F ∧
          (∀ z b, bern (decodeProb k t n z) b = lawOf (F z (rket o)) out b) ∧
          (∀ z b, P k t z = some b →
            1 - η ≤ lawOf (F z (rket o)) out b) ∧
          ∃ instI : Inhabited (ForrelationCoord k t),
            let _ := instI
            ∃ (w : ℕ) (e : Z ↪ Fin (w + 1))
              (K : AdaptiveProgram (ForrelationCoord k t) w →
                AdaptiveProgram (ForrelationCoord k t) w),
              ∀ next, (K next).queryCap ≤ n * k + next.queryCap ∧
                ∀ z ψ b, (K next).outputMass z (clEmb e ψ) b =
                  next.outputMass z (clEmb e (F z ψ)) b</pre></td></tr></tbody>
</table>

The candidate type supplies the explicit nk cap with n=repetitions k η and promised accuracy, but not the displayed asymptotic O_k reformulation. Its compiler is explicitly not native-checked.

### 166. qr-retained-decoder-and-inverse — weaker

Paper lines 4233–4233; `QuarticQuery.Paper.construction_lemma_2_1_ii_complete` in `QuarticQuery/Paper/ConstructionForrelationComplete.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The coherent decoder therefore supplies a bounded-error address bit, a fixed all-input cap and the complete inverse preparation.</pre></td><td><pre>theorem construction_lemma_2_1_ii_complete (k : ℕ) (hk : 1 ≤ k) :
    ∃ A : ℝ, 0 &lt; A ∧ ∀ (t : ℕ) (η : ℝ), 0 &lt; η → η &lt; 1 / 2 →
      ∃ (n : ℕ) (L : BitInput (ForrelationCoord k t) → Bool → ℝ)
        (Z : Type) (instZ : Fintype Z),
        let _ := instZ
        ∃ (o : Z) (out : Z → Bool)
          (F : BitInput (ForrelationCoord k t) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
          ((2 * (n * k) : ℕ) : ℝ) ≤ A * (1 + Real.log (1 / η)) ∧
          IsCirc (n * k) F ∧
          (∀ z b, L z b = lawOf (F z (rket o)) out b) ∧
          (∀ z, 0 ≤ L z false ∧ 0 ≤ L z true ∧ L z false + L z true = 1) ∧
          (∀ z b, P k t z = some b → 1 - η ≤ L z b) ∧
          ∃ instI : Inhabited (ForrelationCoord k t),
            let _ := instI
            ∃ (w : ℕ) (emb : Z ↪ Fin (w + 1))
              (K : AdaptiveProgram (ForrelationCoord k t) w →
                AdaptiveProgram (ForrelationCoord k t) w),
              ∀ next, (K next).queryCap ≤ 2 * (n * k) + next.queryCap ∧
                ∀ z ψ b, (K next).outputMass z (clEmb emb ψ) b =
                  next.outputMass z (clEmb emb (F z ψ)) b</pre></td></tr></tbody>
</table>

The theorem supplies the accurate forward isometry and retained physical continuation, but does not state an inverse implementation in its conclusion.

### 167. qr-retained-decoder-and-inverse — weaker

Paper lines 4233–4233; `QuarticQuery.Upper.IsCirc.symm` in `QuarticQuery/Upper/Circuit.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>The coherent decoder therefore supplies a bounded-error address bit, a fixed all-input cap and the complete inverse preparation.</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι Z Y : Type} [Fintype Z] [Fintype Y]

theorem symm {n : ℕ} {F : BitInput ι → Reg Z ≃ₗᵢ[ℂ] Reg Z} (hF : IsCirc n F) :
    IsCirc n fun x =&gt; (F x).symm</pre></td></tr></tbody>
</table>

This theorem supplies the inverse logical preparation with the same read count; it assumes the forward IsCirc witness and does not assert its accuracy or physical cap.

### 168. qr-residue-invariant — weaker

Paper lines 4258–4258; `QuarticQuery.Forrelation.Enc` in `QuarticQuery/Forrelation/Arithmetic.lean`. Relation: `defines`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>each $w$-bit word represents the intended integer modulo $2^w$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

def Enc (w : ℕ) (p : Prog ι) (v : List (Wire ι)) (F : BitInput ι → ℤ) : Prop :=
  v.length = w ∧ AllValid p v ∧ ∀ x, (bv (vals x p v) : ℤ) ≡ F x [ZMOD (2 : ℤ) ^ w]</pre></td></tr></tbody>
</table>

Enc defines the modular representation condition. The selected clause says the implemented circuit maintains it; that preservation is established by the separate arithmetic constructor specifications.

### 169. qr-word-arithmetic-costs — weaker

Paper lines 4268–4275; `QuarticQuery.Forrelation.addV_spec` in `QuarticQuery/Forrelation/Arithmetic.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{array}{c|c}
\text{operation on }w\text{-bit words}&amp;\text{non-input gates}\\\hline
A+B\pmod{2^w}&amp;6w\\
A-B\pmod{2^w}&amp;6w+1\\
(-1)^bB\pmod{2^w}&amp;6w
\end{array}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

theorem addV_spec {w : ℕ} {p : Prog ι} {a b : List (Wire ι)} {A B : BitInput ι → ℤ}
    (ha : Enc w p a A) (hb : Enc w p b B) :
    ∃ out p', addV a b p = (out, p') ∧ Ext p p' (6 * w) ∧
      Enc w p' out fun x =&gt; A x + B x</pre></td></tr></tbody>
</table>

This constructor supplies only the addition row, with modular correctness and exactly 6w added gates.

### 170. qr-word-arithmetic-costs — weaker

Paper lines 4268–4275; `QuarticQuery.Forrelation.subV_spec` in `QuarticQuery/Forrelation/Arithmetic.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{array}{c|c}
\text{operation on }w\text{-bit words}&amp;\text{non-input gates}\\\hline
A+B\pmod{2^w}&amp;6w\\
A-B\pmod{2^w}&amp;6w+1\\
(-1)^bB\pmod{2^w}&amp;6w
\end{array}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

theorem subV_spec {w : ℕ} {p : Prog ι} {a b : List (Wire ι)} {A B : BitInput ι → ℤ}
    (ha : Enc w p a A) (hb : Enc w p b B) :
    ∃ out p', subV a b p = (out, p') ∧ Ext p p' (6 * w + 1) ∧
      Enc w p' out fun x =&gt; A x - B x</pre></td></tr></tbody>
</table>

This constructor supplies only the subtraction row, with modular correctness and exactly 6w+1 added gates.

### 171. qr-word-arithmetic-costs — weaker

Paper lines 4268–4275; `QuarticQuery.Forrelation.signMul_spec` in `QuarticQuery/Forrelation/Arithmetic.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\begin{array}{c|c}
\text{operation on }w\text{-bit words}&amp;\text{non-input gates}\\\hline
A+B\pmod{2^w}&amp;6w\\
A-B\pmod{2^w}&amp;6w+1\\
(-1)^bB\pmod{2^w}&amp;6w
\end{array}
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

theorem signMul_spec {w : ℕ} {p : Prog ι} {s : Wire ι} {b : List (Wire ι)}
    {B : BitInput ι → ℤ} (hs : s.Valid p.length) (hb : Enc w p b B) :
    ∃ out p', signMul s w b p = (out, p') ∧ Ext p p' (6 * w) ∧
      Enc w p' out fun x =&gt; bitSign (val x p s) * B x</pre></td></tr></tbody>
</table>

This constructor supplies only the sign-multiplication row, with modular correctness and exactly 6w added gates.

### 172. qr-final-signed-range — weaker

Paper lines 4301–4301; `QuarticQuery.Forrelation.test_bounds` in `QuarticQuery/Forrelation/Circuit.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>all three absolute values are at most $(2^{s+1}+1)M$, which is strictly less than $2^{s+2}M=2^{w-1}$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

theorem test_bounds (s e : ℕ) (N M : ℤ) (hM : M = 2 ^ e) (hN : |N| ≤ M) :
    (-2 ^ (s + 2 + e) ≤ 2 ^ s * N - M ∧ 2 ^ s * N - M &lt; 2 ^ (s + 2 + e)) ∧
    (-2 ^ (s + 2 + e) ≤ M - 2 * (2 ^ s * N) ∧ M - 2 * (2 ^ s * N) &lt; 2 ^ (s + 2 + e)) ∧
    (-2 ^ (s + 2 + e) ≤ M + 2 * (2 ^ s * N) ∧ M + 2 * (2 ^ s * N) &lt; 2 ^ (s + 2 + e))</pre></td></tr></tbody>
</table>

The type gives membership in the required signed interval, not the preceding absolute-value estimate with coefficient 2^{s+1}+1.

### 173. qr-expanded-circuit-count — weaker

Paper lines 4342–4345; `QuarticQuery.Forrelation.forrCircuit_size_eq` in `QuarticQuery/Forrelation/Circuit.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
S=6w\bigl((k+1)m+5k+t(k+1)+4\bigr)
 +(k-1)tm(12w+1)+7.
$$</pre></td><td><pre>Source section variables (only those used are generalized):
variable {ι : Type}

theorem forrCircuit_size_eq (l t : ℕ) : (forrCircuit l t).size = coreSize l t + 3</pre></td></tr></tbody>
</table>

The type states S=coreSize+3. The displayed closed expression additionally unfolds coreSize, layerCost and whtCost and solves their arithmetic recurrences.

### 174. qr-small-promise-census — weaker

Paper lines 4410–4414; `QuarticQuery.Forrelation.census_true` in `QuarticQuery/Forrelation/Sanity.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\#P_{2,4}^{-1}(1)=104,\qquad
\#P_{2,4}^{-1}(0)=48,\qquad
\#\{z:P_{2,4}(z)\text{ undefined}\}=104.
$$</pre></td><td><pre>theorem census_true :
    (univ.filter fun z : BitInput (ForrelationCoord 2 1) =&gt; P 2 1 z = some true).card = 104</pre></td></tr></tbody>
</table>

Only the 104 one-inputs are counted; the other two selected counts have separate declarations.

### 175. qr-small-promise-census — weaker

Paper lines 4410–4414; `QuarticQuery.Forrelation.census_false` in `QuarticQuery/Forrelation/Sanity.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\#P_{2,4}^{-1}(1)=104,\qquad
\#P_{2,4}^{-1}(0)=48,\qquad
\#\{z:P_{2,4}(z)\text{ undefined}\}=104.
$$</pre></td><td><pre>theorem census_false :
    (univ.filter fun z : BitInput (ForrelationCoord 2 1) =&gt; P 2 1 z = some false).card = 48</pre></td></tr></tbody>
</table>

Only the 48 zero-inputs are counted; the other two selected counts have separate declarations.

### 176. qr-small-promise-census — weaker

Paper lines 4410–4414; `QuarticQuery.Forrelation.census_none` in `QuarticQuery/Forrelation/Sanity.lean`. Relation: `part`.

<table>
<thead><tr><th>Exact paper phrase</th><th>Actual Lean statement and source context</th></tr></thead>
<tbody><tr><td><pre>$$
\#P_{2,4}^{-1}(1)=104,\qquad
\#P_{2,4}^{-1}(0)=48,\qquad
\#\{z:P_{2,4}(z)\text{ undefined}\}=104.
$$</pre></td><td><pre>theorem census_none :
    (univ.filter fun z : BitInput (ForrelationCoord 2 1) =&gt; P 2 1 z = none).card = 104</pre></td></tr></tbody>
</table>

Only the 104 undefined inputs are counted; the other two selected counts have separate declarations.

## Source integrity and validation

The extracted paper and all 195 Lean files were compared byte for byte with the attached archive: **196 files compared, zero changes**. The paper SHA-256 is `0b05687d43c79e455f57ac1df464bd8528e31f7f81adf669bd816c40146903fb`. The source commit identifies the packet provenance; these comparisons do not authenticate a build or compiled dependency closure.

The supplied checker was run on the combined return. Additional static checks cover `\[...\]` and `\(...\)` boundaries, full namespace spellings rather than suffixes alone, title and note lengths, all required annotations, link-note length, and accidental source markup inside selected phrases. Definition highlights were extended to include their defining right-hand sides. Shared declaration cards were reconciled so one declaration has one title and note throughout the paper.

All 419 phrases are nonoverlapping exact source selections. All 415 named declarations have a title and a 40–120-word note. The mechanical pass establishes the integrity of the link data; the mathematical judgments remain the source review recorded above. No Lean execution, fresh kernel result, current Comparator status, live-site rendering, or human cold-reader test is claimed.

Final packet checker output:

```text
419 ties (419 with Lean), 415 declarations, 8 topics, 0 removed
PASS
```
