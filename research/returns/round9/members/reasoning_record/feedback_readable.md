# Source-order findings

237 accepted findings. Source lines refer to the supplied reasoning-record Markdown; the exact edition is bound in feedback.json. Priority is separate in verdict.md. Optional low-severity formatting advice is not a mathematical error.

## RR9-001 — §1, opening mechanism

**medium · first_encounter · lines 5–5 · U00013**

> at most $L$ address-input queries

The overview introduces L through the cap event before identifying its size or saying that it is a one-instance hardness allowance.

**Reader cost.** The reader cannot yet see why multiplying by m gives the displayed exponent rather than merely a symbolic budget.

**Repair.** Identify L as the chosen subthreshold Forrelation query allowance before the cap event; give its scale there and leave its floor definition to the theorem.

**Later resolution / qualification:** {"line_start": 1633, "line_end": 1642, "explanation": "The bundle specifies L and its hardness property."}

## RR9-002 — §1, contributions

**medium · first_encounter · lines 7–7 · U00017**

> the threshold $t\ge13669k^2$

The threshold t≥13669k² appears before the opening has related t to the board dimension m.

**Reader cost.** A headline numerical improvement has no visible meaning in input-size terms at first encounter.

**Repair.** Supply m=4^t at this first threshold and say that this is the Forrelation hardness threshold; distinguish it from the total-function floor conditions.

## RR9-003 — §1, contributions

**low · structure · lines 7–7 · U00017**

> Beyond the preprint, we determine the constants it leaves unspecified

One paragraph puts constants, an analytic proof, model examples, a varying parameter and formal coverage on the same level.

**Reader cost.** The mathematical advance and the verification aids compete for attention before their dependence is known.

**Repair.** Group the quantitative mathematical consequences together, then identify examples and formal correspondence as separate reading aids.

## RR9-004 — Front matter

**medium · credit · lines 7–7 · U00017**

> give an independent proof of the Forrelation lower bound

Independent proof can mean an independently checked derivation or a proof independent of earlier analytic methods. Later source comparisons qualify the relationship.

**Reader cost.** The introduction can suggest stronger methodological independence than the detailed attribution intends.

**Repair.** Specify the sense of independence at the claim and attach the exact source-comparison destination.

**Later resolution / qualification:** {"line_start": 1612, "line_end": 1643, "note": "Source comparison and bundled ingredient distinguish the routes."}

## RR9-005 — A nearly quartic separation between randomized and quantum queries: a complete reasoning record

**medium · first_encounter · lines 7–7 · U00017**

> the logarithmic exponent six and the coefficient $1/400$

The opening lists two improved constants without attaching either to its inequality.

**Reader cost.** A reader has to retain an unexplained six and 1/400 until the later theorem commentary.

**Repair.** Name the quantum logarithmic loss and the randomized lower-bound coefficient in this list; keep the full formulas in §1.

**Later resolution / qualification:** {"line_start": 79, "description": "The paragraph after (2) identifies b_k=6 and c_k=1/400.", "line_end": 79, "source_path": "repository/docs/reasoning_record.md"}

## RR9-006 — Reading guide

**medium · navigation · lines 10–10 · U00020**

> Reading guide

The guide offers several routes before the reader has a concise dependency map of the construction.

**Reader cost.** Choosing among routes requires recognizing technical topics whose roles are only explained later.

**Repair.** Put a short construction-to-upper/lower-to-exponent dependency map before the route choices.

## RR9-007 — §1, reading routes

**medium · evidence_presentation · lines 14–14 · U00025**

> This route takes the Forrelation lower bound of Bansal and Sinha

The construction route tells the reader to take the Bansal–Sinha theorem as an input, while the source-display qualification is only encountered later.

**Reader cost.** A route is a dependency promise; readers choosing it should know at that decision point that the record also supplies a direct proof and a scoped source check.

**Repair.** Add a short dependency-status pointer to §3.6 and Appendix E at this route, without treating the displayed-step problem as a disproof.

**Later resolution / qualification:** {"line_start": 911, "line_end": 911, "explanation": "The source mismatch and independent route are distinguished later."}

## RR9-008 — Reading guide

**medium · prerequisite · lines 16–16 · U00028**

> No results are taken from the literature on this route.

The absolute statement leaves the background level unstated. A complete reconstruction still relies on standard linear algebra and analytic facts.

**Reader cost.** An outsider cannot tell what they must already know to follow the route.

**Repair.** State the background boundary and distinguish imported query-complexity ingredients from foundational tools used without proof.

## RR9-009 — Reading guide

**low · structure · lines 20–20 · U00034**

> No results are taken from the literature on this route.

A statement-inspection route is described using the proof-dependency language of the other routes.

**Reader cost.** Readers can mistake checking a formal type for reconstructing a proof without external libraries.

**Repair.** Describe the concrete stopping test for this route: identify the type, the intended model, the ordinary transport and the evidence boundary.

## RR9-010 — Reading guide

**medium · structure · lines 22–22 · U00038**

> Appendix B indexes the 121 original claims

The guide lists a large catalogue and several later appendices but gives no page-scale or visible contents for navigating the 132-page PDF.

**Reader cost.** A print or PDF reader cannot estimate the detour or locate the return point as readily as a Markdown reader.

**Repair.** Add a compact contents or page-indexed route map for the long record, without multiplying the existing prose guides.

## RR9-011 — 1. The theorem and the construction

**low · prose · lines 60–60 · U00063**

> The preprint permits any finite real constant

The witness-normalization aside interrupts the first interpretation of the universal exponent.

**Reader cost.** The reader has only just encountered the quantifier order and must distinguish a harmless formulation change before seeing its use.

**Repair.** Move the equivalence-of-constants note to the formal statement comparison or a footnote next to (1), leaving the common-constant meaning contiguous.

## RR9-012 — 1. The theorem and the construction

**medium · chronology · lines 63–63 · U00066**

> Theorem 1.1

The initial theorem introduces a family indexed by k and m before showing what m measures in the final Boolean input.

**Reader cost.** Readers may equate m with input length and misread the strength of the displayed bounds.

**Repair.** Add a local statement that m is the number of columns and link to the physical input-length formula.

**Later resolution / qualification:** {"source_path": "repository/docs/reasoning_record.md", "line_start": 1720, "line_end": 1776}

## RR9-013 — 1.1. Certificates that disqualify every other candidate

**medium · navigation · lines 108–108 · U00097**

> 1.1.

The overview duplicates the guide with a second inventory and a shorter-account route.

**Reader cost.** The repeated maps use different organizational groupings, so the reader spends effort reconciling navigation schemes.

**Repair.** Choose one main dependency map and make alternate entry routes references to that map.

## RR9-014 — §1, relation to earlier separations

**medium · prerequisite · lines 146–146 · U00150**

> the cheat-sheet arithmetic that stops at three.

The reason the earlier cheat-sheet arithmetic reaches three is outsourced to the specialist companion exactly where it is used to motivate the new construction.

**Reader cost.** A complete-record reader must change documents to judge what the extra factor m accomplishes.

**Repair.** Include the short comparison of the old classical and quantum scales here, then offer the companion for the historical sequence of exponents.

## RR9-015 — 2. Models, promises and query budgets

**low · first_encounter · lines 155–155 · U00162**

> The source definitions at $t=0$

The source-totalization warning precedes a concrete example of an out-of-range expression.

**Reader cost.** The reader must retain an abstract implementation caveat with no nearby use.

**Repair.** Move it beside the first floor or logarithmic formula whose totalized value matters, or illustrate that formula here.

## RR9-016 — 2. Models, promises and query budgets

**low · structure · lines 159–159 · U00167**

> Theorem, lemma and proposition numbers are the preprint's.

The display prefixes already have a table, but preprint theorem/proposition labels and record section numbers still need to be distinguished when the same number is used in both systems.

**Reader cost.** A reader can still search for Lemma 4.1 in §4 even though its proof is in §6.1.

**Repair.** Extend the existing key only with the theorem/proposition-versus-section distinction, and identify both labels in substantial local theorem headings. Do not create another display-prefix inventory.

## RR9-017 — 2.2. Deterministic trees and finite random mixtures

**medium · structure · lines 184–184 · U00199**

> The source charges the syntactic depth

The classical-model subsection begins to switch between a mathematical definition and source implementation terminology before setting a clear division between them.

**Reader cost.** The reader must repeatedly decide whether a sentence changes the model or only explains its encoding.

**Repair.** Give the model convention directly, then group the infimum and complexitylib correspondence in a labeled implementation note at the end of the subsection.

## RR9-018 — 2.3. The oracle and finite workspaces

**low · structure · lines 233–233 · U00239**

> The source uses $z\in\operatorname{Fin}(w+1)$

The source-specific workspace type interrupts the ordinary Hilbert-space model before the bit oracle has been displayed.

**Reader cost.** The type syntax adds a second representation to track at the first quantum definition.

**Repair.** Keep the nonempty finite-workspace condition in the model paragraph and move its Fin encoding to the nearby formal correspondence note.

## RR9-019 — 2.3. The oracle and finite workspaces

**medium · structure · lines 248–248 · U00252**

> Thus the bit oracle and this **controlled phase oracle** are interchangeable at one call.

The three oracle variants and their idle behavior are explained in one dense paragraph, although the one-call distinction drives the later cap proof.

**Reader cost.** A reader can remember phase equivalence but accidentally discard the control bit needed for its converse.

**Repair.** Add a compact table listing bit, controlled phase and bare phase oracles, whether an idle state is supplied, and which one-call translation has been proved.

## RR9-020 — 2.3. The oracle and finite workspaces

**low · prerequisite · lines 250–250 · U00258**

> General binary orthogonal projectors can be put into this form

The model explains general binary projective measurements, but its agreement with the standard model is stated without mentioning mixed initial states or finite generalized measurements.

**Reader cost.** Readers using the broader textbook convention cannot see which reductions are included in the agreement claim.

**Repair.** Add a brief scope sentence explaining the free finite-ancilla purification/dilation convention, or explicitly limit the claimed comparison to pure states and projective measurements. No new formal theorem is needed.

## RR9-021 — 2.5. Renaming coordinates and deferring measurements

**medium · prerequisite · lines 326–326 · U00325**

> The source induction retains, besides the entry map, an embedding that commutes with the oracle.

The strengthened induction invariant is revealed only after the weaker mass identity has been stated.

**Reader cost.** A reader trying to reconstruct the induction initially works with a hypothesis too weak for the query constructor.

**Repair.** State the typed entry map, compatible embedding, oracle-intertwining equation and mass identity together before the constructor cases, with the reason for strengthening the invariant.

## RR9-022 — 2.5. Renaming coordinates and deferring measurements

**low · prerequisite · lines 332–332 · U00333**

> For a query followed by a continuation with entry $L$ and compatible embedding $J$

The proof switches the continuation entry-map name from E to L and immediately writes an extension on range(J) without restating the common source and target spaces.

**Reader cost.** The reader must reconstruct the types of J, L, H_b and Z to verify that the extension is well-defined.

**Repair.** Give a short source/target annotation for the two isometries and say that L is the continuation entry map previously denoted by E.

## RR9-023 — 2.5. Renaming coordinates and deferring measurements

**medium · evidence_presentation · lines 340–340 · U00343**

> used by the imported universal upper bound

Imported is ambiguous between a Lean dependency and an external theorem assumed by the reader.

**Reader cost.** The complete-proof route reconstructs Appendix A, so this wording can make that route appear to rely on a literature result after all.

**Repair.** Specify that this is the Lean source dependency, and link the independent printed derivation in Appendix A and the three-route comparison in G.9.

## RR9-024 — 2.6. Exact small examples

**low · prerequisite · lines 399–399 · U00392**

> all supported response functions must be among $1,x_0,x_1$

The endpoint argument moves from an average-success bound to a classification of all optimal one-query response functions without displaying that finite classification.

**Reader cost.** The reader has to enumerate the constant and one-bit Boolean response maps to verify why the weights must be exactly thirds.

**Repair.** Add the short observation that among the six possible response functions only 1, x_0 and x_1 attain two successes on 00,01,10; then give the three pointwise inequalities.

## RR9-025 — 2.6. Exact small examples

**low · structure · lines 431–431 · U00422**

> The supplied 1998 version of Beals et al.

The parity example ends with a version-history paragraph after its direct proof has already settled the needed cap.

**Reader cost.** This interrupts the transition from the model examples to Forrelation with bibliography maintenance rather than another mathematical step.

**Repair.** Move the edition comparison to the inspected-editions appendix and leave a short warning that expected-query parity figures use another convention.

## RR9-026 — 3.3. The quantum promise algorithm, including amplification and coherence

**low · first_encounter · lines 550–550 · U00514**

> ### 3.3. The quantum promise algorithm, including amplification and coherence

The heading calls the Bernoulli repetition argument amplification, while §5.1 later uses the same word for Grover amplitude amplification.

**Reader cost.** The two procedures have different dependence on the initial success probability, and readers may transfer the wrong cost.

**Repair.** Name error reduction by repetition in this heading or at the first sentence, reserving amplitude amplification for §5.1.

## RR9-027 — 3.3. The quantum promise algorithm, including amplification and coherence

**low · prerequisite · lines 568–568 · U00525**

> Let $\Pi=|u\rangle\langle u|$.

The projector is written on the address space after the implementation has introduced the answer qubit and block-selection workspace.

**Reader cost.** The subsequent flag unitary is read as a full-register operation, so its tensor factors are implicit.

**Repair.** State once that Π acts on the address register and is tensored with identity on untouched registers.

## RR9-028 — 3.3. The quantum promise algorithm, including amplification and coherence

**low · prerequisite · lines 585–585 · U00539**

> We repeat the trial $q$ times on fresh registers

The repeated construction uses many fresh address registers without saying how they are accessed through the single physical query register of §2.

**Reader cost.** A literal tensor interpretation can look like an unannounced collection of independent oracle ports.

**Repair.** Add a register-routing sentence: swap the active trial address and answer into the oracle interface and retain previous trial registers as workspace.

## RR9-029 — 3.3. The quantum promise algorithm, including amplification and coherence

**medium · evidence_presentation · lines 675–675 · U00588**

> The formal implementation proves the same asymptotic bound with at most $2qk$ physical queries

The factor-two implementation statement arrives in the conclusion of the ordinary kq-query construction.

**Reader cost.** Readers can lose track of whether the retained-workspace proof has just doubled its own cap or whether another implementation is being compared.

**Repair.** Place the kq ordinary construction and 2qk compiled construction in a small two-row cost/evidence note, preserving the explicit distinction already made.

## RR9-030 — 3.4. The exact Boolean circuit

**low · structure · lines 700–700 · U00615**

> The implemented circuit instead maintains congruences modulo one fixed power of two

The ideal-value, stored-residue and final-sign invariants are already present, but are spread across two dense paragraphs.

**Reader cost.** The reader must remember which intermediate quantities are integers and which are residues when the smaller implemented width is chosen.

**Repair.** Consider a compact representation table collecting those three existing invariants before the operation costs; do not add a missing-proof claim.

## RR9-031 — 3.4. The exact Boolean circuit

**medium · prerequisite · lines 713–713 · U00631**

> A+B\pmod{2^w}&6w

The operation table charges six gates per bit for addition immediately after deriving a five-gate full adder.

**Reader cost.** The reader cannot reconcile the exact constructor count with the elementary arithmetic count without opening the implementation.

**Repair.** Explain whether the extra xor comes from using the conditional adder at control zero, or whether 6w is simply the deliberately charged upper bound; cite the actual constructor if asserting an identity.

## RR9-032 — 3.4. The exact Boolean circuit

**low · prerequisite · lines 751–751 · U00653**

> one forms the conjunction of the other two negated signs

The three-output-gate count relies on treating the conjunction of two negated signs as one binary truth function.

**Reader cost.** Readers counting AND and NOT gates separately will obtain five gates and suspect the size arithmetic.

**Repair.** Name that gate as NOR on the two sign wires and remind the reader that arbitrary binary truth functions are allowed.

## RR9-033 — 3.4. The exact Boolean circuit

**medium · prerequisite · lines 767–767 · U00668**

> Adding the final sum, the repeated doublings, three comparisons and three output gates gives

The exact S formula aggregates several constructors but does not map its bracket terms and final +7 to those constructors.

**Reader cost.** The explicit coefficient cannot be audited from the prose without reverse-engineering the circuit.

**Repair.** Add a term ledger showing the gate contribution of sign layers, final sum, doublings, comparisons and constants; retain the existing coarse inequality.

## RR9-034 — 3.5. A complete check of the smallest nontrivial instance

**low · chronology · lines 798–798 · U00689**

> smallest

The complete smallest-instance calculation follows the arithmetic compiler, so an outside reader reaches the long implementation before seeing a worked value of Phi.

**Reader cost.** The first numerical interpretation of the promise is delayed until after substantial notation and gate accounting.

**Repair.** Consider moving one existing small Phi calculation immediately after the promise definition, leaving the full census here. The sign and gap warnings are already present.

## RR9-035 — 3.5. A complete check of the smallest nontrivial instance

**low · example · lines 833–833 · U00709**

> Every positive value is at least $\Phi=1/2>\delta$

The smallest-instance census has no values in the positive promise gap, although it follows the exact endpoint-test derivation.

**Reader cost.** A reader may overestimate what the finite illustration tests about the threshold and gap.

**Repair.** Explicitly say that this census illustrates sign, promise membership and normalization, while the equality and gap handling are established by the general integer inequalities.

## RR9-036 — 3.5. A complete check of the smallest nontrivial instance

**low · evidence_presentation · lines 842–842 · U00713**

> The [exact checker](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/checks/)

The small-instance subsection ends with a dense execution inventory, mixing two parameter settings and five independent implementations.

**Reader cost.** The reader has just completed a hand census and must parse a tooling summary before reaching the construction.

**Repair.** Move the detailed inventory to an evidence note or Appendix F, leaving the checker link and the fact that the general conclusions rest on the printed proofs.

## RR9-037 — 3.6. The statement and the proof

**medium · first_encounter · lines 895–895 · U00746**

> Bansal

The published hardness result is stated before the reader is told that a displayed step in that source needs qualification.

**Reader cost.** A first-time reader cannot tell whether the theorem is an input, an independently proved target or a disputed premise.

**Repair.** At the citation, state the precise role: comparison theorem; direct proof follows; the disputed display is separately audited.

**Later resolution / qualification:** {"line_start": 911, "line_end": 911, "explanation": "The source-display qualification is supplied before the direct proof; the finding concerns its first cited use."}

## RR9-038 — §3.6, proof spine

**medium · structure · lines 916–916 · U00761**

> To prove this indistinguishability, we scale only the first block of Gaussian biases.

The proof spine compresses four technical transformations into one paragraph without showing which numerical output each must supply.

**Reader cost.** Readers reconstructing the proof have to infer why the next several lemmas are needed and which bounds survive into the final contradiction.

**Repair.** Give a small dependency list linking F22/F25 to F33, F36/F39 to F42, and those two inequalities to F43.

## RR9-039 — §3.6, terminology and credit

**low · prose · lines 920–920 · U00770**

> the truncation (F9) replaces their shifted Gaussian distribution function

Calling the algebraic map a truncation can suggest literal clipping, although it is a smooth bounded transform.

**Reader cost.** The next identities depend on differentiability, so an inaccurate mental picture makes the method harder to anticipate.

**Repair.** At first use, identify truncation as the paper’s term for a smooth bounded bias transform and give its range.

## RR9-040 — 3.6. The statement and the proof

**medium · first_encounter · lines 920–920 · U00770**

> Owen

The discussion of avoiding Owen’s T names a specialized analytic object before explaining the elementary replacement needed in this proof.

**Reader cost.** This adds a historical comparison at a point where the reader is trying to learn the proof mechanism.

**Repair.** Lead with the elementary truncation and its two required identities; defer the specialized comparison to the attribution subsection.

## RR9-041 — §3.9, rounded Gaussian law

**medium · first_encounter · lines 1059–1059 · U00840**

> we give each coordinate of the $k$-block sign cube the bias

The bias vector introduces endpoint and middle-block rules simultaneously, so the reader must reconstruct how adjacent Gaussian layers overlap.

**Reader cost.** The clearing proof and derivative propagation both depend on precisely that overlap.

**Repair.** Add a compact k=2 specialization or a block-to-layer dependency table beside F14, identifying the absent middle-block case.

## RR9-042 — §3.9, hard-law terminology

**high · first_encounter · lines 1079–1079 · U00846**

> The hard distribution is $\nu_1$.

Calling ν1 “the hard distribution” without a forward distinction invites identification with the promised-domain minimax law µ later used for planting.

**Reader cost.** ν1 lives on the entire cube and may put most mass off the promise; µ has a different support and a different quantifier role.

**Repair.** Label ν1 as the analytic comparison law and announce that planting will use a separate promised-input law obtained after the complexity lower bound.

**Later resolution / qualification:** {"line_start": 3211, "line_end": 3211, "explanation": "The minimax proof finally states that the analytic hard measure plays no role."}

## RR9-043 — 3.10. Moving the derivative through the blocks

**medium · notation · lines 1094–1094 · U00862**

> 3.10.

The worked k=3 derivative introduces its own block notation before the general block induction.

**Reader cost.** The reader has to translate between two indexing systems while learning the induction invariant.

**Repair.** Use the general block labels in the k=3 example and identify the two active derivatives at each step.

## RR9-044 — §3.10, derivative propagation

**medium · prerequisite · lines 1160–1160 · U00895**

> after the derivative enters block $j$

The invariant is phrased for block j without stating its range, although Xj is absent in the last block.

**Reader cost.** At j=k−1 the literal invariant no longer names an existing unremoved factor.

**Repair.** State the invariant for 0≤j≤k−2, give its base case explicitly, and separate the final arrival in block k−1.

**Later resolution / qualification:** {"line_start": 1166, "line_end": 1166, "explanation": "The following paragraph says the last block carries no X factor."}

## RR9-045 — §3.10, higher Fourier levels

**low · example · lines 1189–1189 · U00907**

> A derivative of order $k$ at a biased point can carry uniform Fourier degrees above $k$

F24 explains why higher uniform degrees survive, but the point is only visible through a general summation formula.

**Reader cost.** This distinction is central to comparing the one-block method with the multilevel source argument.

**Repair.** Use a single monomial of degree k+1 to illustrate the retained bias factor after differentiating k coordinates.

## RR9-046 — 3.11. Derivative growth along a decision tree

**medium · first_encounter · lines 1204–1204 · U00912**

> 3.11.

The Fourier-growth proof introduces several coefficient arrays and revealed-coordinate sets together.

**Reader cost.** The probabilistic object being stopped is difficult to separate from the deterministic tree and its coefficient bookkeeping.

**Repair.** Give a short object table with each array, its index set and its role before the martingale calculation.

## RR9-047 — §3.11, contracted arrays

**low · example · lines 1242–1242 · U00937**

> the new terms are exactly

The degree-two calculation shows the new terms but does not state the general combinatorial correspondence in words.

**Reader cost.** The later union bound over contracted arrays is easier to follow if each new r-set is seen to arise exactly once by adjoining the fresh coordinate.

**Repair.** After the example, explicitly identify the bijection between new r-subsets and old (r−1)-subsets contracted at q.

## RR9-048 — §3.11, maximal inequality

**medium · prerequisite · lines 1285–1285 · U00971**

> Iterated conditional expectation over these at most $d$ steps

The finite stopped-supermartingale step is summarized in one sentence between the exponential process and crossing bound.

**Reader cost.** This is the place where the proof avoids an optional-stopping theorem and should make that avoidance reconstructible.

**Repair.** Display the stopped process at j∧σ and the one-step conditional expectation inequality, then iterate over d deterministic steps.

## RR9-049 — §3.11, induction in degree

**medium · prerequisite · lines 1305–1305 · U00981**

> Suppose the claim holds at degree $r-1$.

The induction refers to failure of any contracted expression without immediately restating that the same Λ is used at every degree.

**Reader cost.** The exponent (4n)^(r−1)e^−Λ and the following union bound cannot be reconstructed safely if Λ is thought to be degree-optimized separately.

**Repair.** Fix Λ before the degree induction and state explicitly that the induction hypothesis is applied to every contracted array with that same value.

## RR9-050 — §3.11, predictable stopping

**medium · prerequisite · lines 1311–1311 · U00984**

> Before the stop, the increment (F27) is centered

The stopped increment bound is correct, but the predictability of the decision to stop is implicit.

**Reader cost.** The martingale step requires the coefficient bound to be checked from the past before observing the fresh queried sign.

**Repair.** State that all contracted expressions are measurable at the pre-query history and that stopping is decided before the new answer.

## RR9-051 — §3.11, source locator

**low · credit · lines 1324–1324 · U00990**

> Girish, Tal and Wu make this distinction in their footnote 2.

The footnote citation gives only a number even though the section has already distinguished arXiv and conference numbering.

**Reader cost.** Footnote numbers can change between those editions, making the most important caution hard to locate.

**Repair.** Attach the edition and page to the stopping-versus-conditioning footnote reference, or quote its topic in the locator without copying a passage.

## RR9-052 — §3.11, choice of signs

**low · prerequisite · lines 1337–1337 · U00997**

> We choose $c(J)$ to be the sign of $\partial_JF_g(\mu)$

“Choosing the coefficients at the end” can sound as though the signs depend on the random transcript.

**Reader cost.** The martingale proof only allows a coefficient array fixed before the random tree execution.

**Repair.** Say explicitly that c is chosen from the deterministic numbers ∂JFg(µ), for fixed g and µ, and therefore is nonrandom during the process.

## RR9-053 — §3.12, scale and extension

**low · structure · lines 1370–1370 · U01018**

> The scale of (F33) can already be read off here.

One paragraph handles convex mixtures, arbitrary random coins, the depth exponent and an obsolete coarse threshold.

**Reader cost.** The central explanation of m^(1−1/k) is buried among model and archival details.

**Repair.** Give the scale explanation its own paragraph directly after F33, and move the finite-mixture and historical-threshold remarks into separate short notes.

## RR9-054 — §3.13, uniform moment

**low · prerequisite · lines 1386–1386 · U01030**

> contains a coordinate appearing once

The cancellation of distinct paths is described using a coordinate appearing once without making the block label explicit.

**Reader cost.** A numeric coordinate can reappear in different blocks; those are still different independent sign variables.

**Repair.** State that the singleton is a block-coordinate pair, so equal numeric indices in different blocks do not affect the cancellation.

## RR9-055 — §3.13, hard mean

**medium · prerequisite · lines 1395–1395 · U01034**

> we use the elementary inequality $e^v\ge1+v$

The exponential lower bound appears before the strategy behind this unusual algebraic choice is made explicit.

**Reader cost.** A reader may try to factor the expectation across correlated U,V coordinates, which is not the intended route.

**Repair.** Preview that the product will become exp(−Tp) and that only ETp=0 is needed, then perform the scalar inequality.

**Later resolution / qualification:** {"line_start": 1413, "line_end": 1422, "explanation": "The expectation calculation and dependence caveat supply the strategy later."}

## RR9-056 — §3.13, path derivative

**low · prerequisite · lines 1424–1424 · U01045**

> Since $\Phi$ has one variable in each block

The claim that the path derivative is constant elides why no other path monomial contributes.

**Reader cost.** The cancellation is stronger than merely observing that Φ is multilinear.

**Repair.** State that differentiating the chosen coordinate in every block kills every path with a different coordinate in any block, leaving one coefficient.

## RR9-057 — §3.13, promise-mass scale

**medium · structure · lines 1446–1446 · U01052**

> For example, the inequality $\Phi\le\delta+\mathbf1_{\{\Phi\ge\delta\}}$ gives

The 31δ illustration introduces a weaker scale just before the proof switches back to ak for amplification.

**Reader cost.** Readers must track two lower bounds for the same mass without knowing that the weaker one serves the historical appendix.

**Repair.** Mark this as the bound used in Appendix D or move it there; end the main moment section with the ak scale used next.

## RR9-058 — §3.14, amplification

**low · prerequisite · lines 1458–1458 · U01063**

> We run it independently $2\tau$ times

The amplification argument is pointwise in a promised input, but that quantifier is easy to lose once error indicators are introduced.

**Reader cost.** The independent runs are conditional on one fixed input; the input law need not be a product law.

**Repair.** Say that z is fixed throughout F40 and independence is only over fresh algorithmic coins, then take input expectations afterward.

## RR9-059 — §3.14, padded depth

**low · prose · lines 1467–1467 · U01069**

> we may use the larger integer $d=2\tau D+1$

The extra query in d=2τD+1 is introduced as a convenience and later described as a formal-interface match, leaving two motivations separated.

**Reader cost.** An exact-constant reader needs to know whether the algorithm actually performs the extra query or the analytic bound is merely being evaluated at a larger cap.

**Repair.** State at this first occurrence that d is an upper-bound parameter only, not an added oracle operation, and mention the later interface reason here.

## RR9-060 — §3.14, pointwise comparison

**medium · example · lines 1472–1472 · U01074**

> Then at every input

The two-sided comparison combines three input regions and two different inequalities into one display.

**Reader cost.** The central off-promise safeguard requires the reader to reconstruct a case split before understanding why neither law is conditioned.

**Repair.** Present a compact case table for yes, no, and outside-promise inputs showing the bound used on A in each region.

## RR9-061 — §3.15, two k losses

**low · prerequisite · lines 1512–1512 · U01095**

> The two powers of $k$ have different sources

The explanation names the two k factors but does not point to their separate appearances in the assembled expression.

**Reader cost.** Readers comparing F43 with Appendix E need to distinguish the growth-lemma loss from amplification cost.

**Repair.** Annotate the k in F25 and the k in τ=25k at this sentence, then point to Appendix E for the cancellation available with its external theorem.

## RR9-062 — §3.15, depth padding absorption

**medium · prerequisite · lines 1535–1535 · U01107**

> The assumption on $D$ and the equality $800(2/18225)=(8/27)^2$ imply

The transition to F46 uses D≥1 to absorb the additive one, but the sentence cites only the upper bound on D and a numerical identity.

**Reader cost.** Omitting the lower-bound use makes the padded-depth estimate appear to follow from an upper bound alone.

**Repair.** Show d≤50kD(1+1/(50k)) and cite the preceding D≥1 step before substituting the assumed bound.

## RR9-063 — §3.15, residual estimate

**medium · prerequisite · lines 1567–1567 · U01115**

> the residual satisfies

The residual estimate F49 is correct but the stated coarse bounds b≤3 and √m≥54 leave its comparison with ak unstated.

**Reader cost.** The reader has to discover the intended b/√m≤1/18 and 2^−k≤1/4 chain.

**Repair.** Write those two inequalities explicitly, making the residual no larger than ak/4 in one visible step.

## RR9-064 — §3.15, threshold variants

**low · structure · lines 1607–1607 · U01132**

> the smaller threshold $\lceil54675k^2/4\rceil$ also follows

The sharper ceiling threshold is inserted between the chosen threshold and the nonempty-promise consequence.

**Reader cost.** This creates another numerical target before the proof has finished stating what the selected one guarantees.

**Repair.** Finish the consequences of the declared threshold first; put the slightly smaller sufficient threshold into a short optional note.

## RR9-065 — §3.16, attribution

**medium · structure · lines 1617–1617 · U01142**

> The proof above combines a known Gaussian-chain architecture with a known decision-tree growth strategy.

The opening attribution paragraph interleaves three sources, distribution differences, theorem ownership, and the proof’s local obligations.

**Reader cost.** Readers trying to identify which input is borrowed must parse a long narrative rather than a small set of exact dependencies.

**Repair.** Organize this material by object: promise/theorem, Gaussian architecture, tree growth, and optional external comparison, each with its precise locator.

## RR9-066 — §3.16, review-history vocabulary

**low · evidence_presentation · lines 1621–1621 · U01152**

> The bounded searches and source comparisons in the retained reviews

The phrase “retained reviews” makes a mathematical attribution limitation depend on an internal review process.

**Reader cost.** A reader cannot tell which search was conducted or why this process fact belongs in the proof narrative.

**Repair.** State the priority limitation directly and move the historical search scope to the source audit or bibliography note.

## RR9-067 — §3.16, source-error scope

**high · evidence_presentation · lines 1624–1624 · U01154**

> leaves their theorem intact

“Leaves their theorem intact” is stronger than the appendix’s demonstrated conclusion: the checked display error does not itself disprove the theorem.

**Reader cost.** The local source audit cannot certify the original theorem’s remaining proof obligations merely by locating a bad comparison.

**Repair.** At both occurrences, state only that the checked display issue does not by itself refute the source theorem, and identify §3 as the independently supplied prerequisite. Do not imply an external theorem certification.

**Later resolution / qualification:** {"line_start": 5881, "line_end": 5903, "explanation": "Appendix E states the narrower, justified source-check scope."}

## RR9-068 — 4.1. What a transcript certifies

**low · first_encounter · lines 1664–1664 · U01191**

> 4.1.

The mixed input/gate-predecessor example appears later in the local tests, after the transcript has been defined abstractly.

**Reader cost.** The later local-test count depends on exactly which bits are copied and which are queried from the actual input.

**Repair.** Move or briefly preview the existing AND(x_a,tau_u) example at the transcript definition; a new example or theorem is unnecessary.

## RR9-069 — 4.2. Columns and their selected cells

**low · first_encounter · lines 1700–1700 · U01225**

> 4.2.

The complete column definition is a nested array of address strings, cells, pointers and transcripts that is demanding to hold in memory.

**Reader cost.** The reader must hold a nested data structure before knowing which pieces the two algorithms inspect.

**Repair.** Consider a one-column schematic keyed to the existing field definitions and later uses; this is an optional visual aid, not a missing-definition claim.

## RR9-070 — 4.3. A four-column instance

**medium · error · lines 1794–1794 · U01295**

> N=z_1^{\mathsf T}W_4z_2

The finite construction example silently returns to one-based sign-block labels z_1,z_2 after §3.1 explicitly fixed record blocks z_0,…,z_{k−1}.

**Reader cost.** This is a genuine notation inconsistency at the point where the example is supposed to instantiate the earlier definition.

**Repair.** Use z_0,z_1 in (4.7) and its worked multiplication, or explicitly mark and justify a local convention before the display.

## RR9-071 — 4.3. A four-column instance

**medium · example · lines 1834–1834 · U01316**

> at every cell the pointers into columns 2, 3, and 4 go to their respective zero rows

The filling rule quantifies over pointers that do not exist in a column’s own cells: there is no self-pointer.

**Reader cost.** A reader filling the board literally is asked to assign fields absent from the layout.

**Repair.** Qualify the rule by j≠i, or say each existing pointer into columns 2–4 goes to the corresponding zero.

## RR9-072 — 4.4. The local tests

**low · first_encounter · lines 1837–1837 · U01320**

> 4.4.

The test counts, locations and adaptive depths are supplied across several adjacent labeled paragraphs, making a quick cross-check laborious.

**Reader cost.** It is easy to double-count output gates or assume that d and b are not already transcript bits.

**Repair.** Collect the existing test family, count, queried locations and maximum depth in one compact table; do not add new accounting claims.

## RR9-073 — 4.4. The local tests

**medium · prose · lines 1910–1910 · U01380**

> Its board uses amplitudes $+1$ and $-1$

The unqualified word amplitudes can refer either to input sign entries or to the Forrelation projection amplitude.

**Reader cost.** The comparison between the exposition and checker boards is otherwise nonsensical for input signs, which remain ±1 in both.

**Repair.** Say Forrelation values Φ or projection amplitudes Φ when distinguishing the two boards.

## RR9-074 — 4.4. The local tests

**low · transition · lines 1910–1910 · U01382**

> Return to the [exposition, Section 2](exposition.md#2-one-column-then-four) after inspecting these tests.

This instruction addresses a reader arriving from the exposition but occurs in the main forward proof of the reasoning record.

**Reader cost.** A cover-to-cover reader is directed out of the lead at a point where no external detour is needed.

**Repair.** Mark it explicitly as a return link for exposition readers, and keep it typographically separate from the main proof.

## RR9-075 — 4.4. The local tests

**low · structure · lines 1921–1921 · U01390**

> The checker evaluates the partial function from the integer expression (4.7)

The general local-equivalence proof is followed by a long cluster of checker operations before coherent access resumes.

**Reader cost.** The quantum dependency chain is paused to enumerate finite tests whose evidential status is already stated.

**Repair.** Group the finite board counts and domain-isolating second board in an example box; move reproduction commands and mutation counts to its evidence note.

## RR9-076 — 4.5. Remark: depth and support of a pointer test

**medium · structure · lines 1928–1928 · U01399**

> ### 4.5. Remark: depth and support of a pointer test

The support discussion occupies a full subsection between the local-test contract and the coherent evaluator, although its final sentence says the count matters only to formal-statement comparison.

**Reader cost.** The ordinary quantum proof temporarily follows a different issue before using the depth bound it has just established.

**Repair.** Keep a short depth-versus-support warning beside (4.13) and place the essential-coordinate proof with Appendix G.6.

## RR9-077 — 4.6. Coherent evaluation of an arbitrary test index

**medium · first_encounter · lines 1964–1964 · U01437**

> When a later routine needs the work registers reset

The stronger clean oracle is introduced as a later routine’s need, while the following paragraph says the actual search uses retained workspace.

**Reader cost.** The reader may think the 4q_* clean cost is required in the final verifier and carry an extra factor into its budget.

**Repair.** Name and distinguish the retained-workspace evaluator and clean oracle, then identify the latter as an optional stronger interface; the implemented verifier uses (4.15).

**Later resolution / qualification:** {"line_start": 1978, "description": "The uniform-index paragraph states that the later search uses retained work registers.", "line_end": 1978, "source_path": "repository/docs/reasoning_record.md"}

## RR9-078 — 4.6. Coherent evaluation of an arbitrary test index

**medium · prose · lines 1973–1973 · U01445**

> By linearity it also holds on arbitrary superpositions of the label and target.

The pronoun it follows a sentence about the noisy decoder even though the intended claim is the exact clean transformation (4.16).

**Reader cost.** This placement can attach a reset-workspace claim to the noisy decoder, the very implication the paragraph denies.

**Repair.** Name (4.16) explicitly, or move the linearity sentence immediately after that display and before contrasting the noisy decoder.

## RR9-079 — 4.7. Why a winner defeats an unpromised opponent

**medium · structure · lines 1981–1981 · U01456**

> 4.7.

The winner argument is used again in §5.3 with nearly the same proof but a different notation for the comparison probabilities.

**Reader cost.** Repetition helps recall only if the later use is explicitly an instantiation of the earlier lemma.

**Repair.** Give this implication a compact named statement and cite it from the later comparator proof.

## RR9-080 — 4.7. Why a winner defeats an unpromised opponent

**low · prose · lines 2010–2010 · U01472**

> every joint distribution of the two outputs

The universal wording applies to the event inclusion, while the numerical 1−ε conclusion still depends on the correct winner marginal.

**Reader cost.** A reader can overread the final displayed bound as uniform over arbitrary replacements of both output marginals.

**Repair.** Split the assertion into an event inclusion valid for all joint laws and its numerical consequence for laws with the decoder’s promised winner marginal.

## RR9-081 — 4.8. Antecedents of the construction

**low · first_encounter · lines 2015–2015 · U01478**

> 4.8.

The historical pointer and cheat-sheet discussion comes immediately before the algorithmic upper bound.

**Reader cost.** Its source-by-source qualifications postpone the transition from local certificates to candidate search.

**Repair.** Keep a short lineage paragraph here and move the detailed hypothesis comparisons into the source appendix.

## RR9-082 — 5.1. Amplification with a fixed stopping time

**low · prose · lines 2053–2053 · U01521**

> ### 5.1. Amplification with a fixed stopping time

The procedure stops at its first success, so its actual stopping time is random even though its upper bound is fixed.

**Reader cost.** The heading blurs a predetermined branch cap with a deterministic number of executed trials.

**Repair.** Use bounded stopping time or predetermined query cap in the heading, and reserve exactly fixed schedule for the later coherent implementation.

## RR9-083 — 5.1. Amplification with a fixed stopping time

**medium · first_encounter · lines 2059–2059 · U01527**

> using $A,A^{-1}$ as black boxes

The contract is strong enough to suggest a need for controlled black-box access when the coherent trial construction is reached; the fact that only uncontrolled A calls are required is postponed.

**Reader cost.** This is a material interface question, because a controlled unknown unitary is an extra capability.

**Repair.** Add a short forward assurance at the contract that only uncontrolled calls to A and its inverse are used, with control implemented on fixed reflections as shown later.

**Later resolution / qualification:** {"line_start": 2173, "description": "The coherent construction explicitly uses uncontrolled A calls and controlled fixed reflections.", "line_end": 2173, "source_path": "repository/docs/reasoning_record.md"}

## RR9-084 — 5.1. Amplification with a fixed stopping time

**medium · first_encounter · lines 2061–2061 · U01530**

> the designated output register contains the normalized success component

The lemma’s output-register contract does not yet say that this register is the entire original A interface viewed as one subsystem of a larger workspace.

**Reader cost.** The reader can identify the returned state with the whole enlarged trial/history workspace, an interpretation the later discussion excludes.

**Repair.** Describe the designated subsystem in the statement and retain the later routing proof as its justification.

**Later resolution / qualification:** {"line_start": 2171, "description": "The retained-register discussion distinguishes the original output subsystem from the enlarged workspace.", "line_end": 2171, "source_path": "repository/docs/reasoning_record.md"}

## RR9-085 — 5.1. Amplification with a fixed stopping time

**low · credit · lines 2067–2067 · U01538**

> The expected-cost searches in those sources do not by themselves give the all-branch cap needed here

The comparison emphasizes expected cost but does not acknowledge that the inspected BBHT discussion also mentions timeout for the no-solution case.

**Reader cost.** The reader may infer that fixed-budget search itself is the new ingredient rather than the particular uniform cap and returned-state contract proved here.

**Repair.** Narrow the comparison to the exact contract required here and briefly acknowledge the prior timeout discussion; preserve the attribution of the reconstructed lemma to OpenAI.

## RR9-086 — 5.1. Amplification with a fixed stopping time

**low · figure · lines 2075–2075 · U01550**

> gives the matrix with rows

The central two-dimensional Grover operator is specified as two parenthesized row vectors embedded in prose.

**Reader cost.** The reader must reconstruct the matrix before checking its signs against the next angle-addition calculation.

**Repair.** Display the 2×2 matrix with the ordered basis (g,b) and the coordinate column (sin α,cos α).

## RR9-087 — 5.1. Amplification with a fixed stopping time

**low · figure · lines 2075–2075 · U01547**

> $G=-AS_0A^{-1}S_\chi$

In the supplied PDF the Grover-iterate definition breaks across pages 44–45, leaving G= at the foot of one page and the product on the next.

**Reader cost.** The most important operator definition is split before the reader can see what is being defined.

**Repair.** Set the defining product as a nonbreaking display or keep its short introductory sentence with the formula during pagination.

## RR9-088 — 5.1. Amplification with a fixed stopping time

**low · first_encounter · lines 2097–2097 · U01564**

> For one amplification trial, choose the following two integers

The introduction gives both M and N as choices for one trial, although M controls the within-trial iteration range and N counts the outer trials.

**Reader cost.** The two nested loops are harder to identify at the first display of their parameters.

**Repair.** Introduce these as the procedure’s two parameters and label M as the iteration-range size and N as the trial cap.

## RR9-089 — 5.1. Amplification with a fixed stopping time

**low · prose · lines 2129–2129 · U01590**

> give `claim-sin2theta`:

The visible prose exposes an internal claim identifier here, and the same leak occurs with claim-verify in §5.3.

**Reader cost.** These code-like tokens supply no mathematical meaning and look like unresolved editorial placeholders in the PDF.

**Repair.** Remove the raw identifiers from visible prose while keeping their invisible anchors or catalogue links.

## RR9-090 — 5.1. Amplification with a fixed stopping time

**low · structure · lines 2155–2155 · U01611**

> **Constant accounting.** The padded product charged by the implementation

The constant-138 derivation interrupts the progression from successful measured histories to the coherent returned-register interpretation.

**Reader cost.** The reader checks numerical inequalities before the full state/interface issue raised by the lemma has been closed.

**Repair.** Finish the returned-register and controlled-iterate argument before the constant accounting, or mark the arithmetic as a separately skippable budget block.

## RR9-091 — 5.1. Amplification with a fixed stopping time

**medium · prerequisite · lines 2173–2173 · U01630**

> To control a Grover iterate, we apply $A$ and $A^{-1}$ unconditionally

The crucial no-controlled-A construction is expressed only in prose, including a control-dependent minus sign.

**Reader cost.** A reader cannot quickly check operator order or distinguish an irrelevant global sign from the relative phase required by a control.

**Repair.** Display the controlled product and its false/true control blocks I and G, retaining the explanation that only fixed reflections and the phase are controlled.

## RR9-092 — 5.1. Amplification with a fixed stopping time

**low · structure · lines 2176–2176 · U01635**

> The successful-state assertion needs more than equality of label distributions.

The pure-versus-entangled example is an evidence-interface comparison after the ordinary amplification proof, but before the tournament begins.

**Reader cost.** It lengthens the critical dependency route with a formal-strength distinction already signposted by the retained-register statement.

**Repair.** Move the full counterexample to the formal correspondence discussion and leave a concise link identifying the distinction in this proof.

## RR9-093 — 5.2. A tournament with probabilistic comparisons

**medium · structure · lines 2189–2189 · U01645**

> **Proposition 3.2 (statement).**

The proposition is one long paragraph containing oracle access, inverse cost, arbitrary probabilities, diagonal convention, parameters, dominance, all-input cap and success guarantee.

**Reader cost.** The reader must parse all hypotheses and conclusions simultaneously before knowing which ones the proof uses at each stage.

**Repair.** Split the statement into comparison-interface assumptions, parameter definitions, and algorithm/output guarantees; keep the quantifier order explicit.

## RR9-094 — 5.2. A tournament with probabilistic comparisons

**low · structure · lines 2193–2193 · U01655**

> We first fix the comparison model and the parameters.

The comparison model and parameter definitions are immediately repeated in full after the proposition already contains them.

**Reader cost.** The proof’s first substantive weight step is delayed by duplicate setup rather than a new inference.

**Repair.** Keep the complete setup in either the statement or the proof opening, and use a short reminder of fixed input and complementarity in the other location.

## RR9-095 — 5.2. A tournament with probabilistic comparisons

**low · first_encounter · lines 2225–2225 · U01680**

> \varepsilon=\frac{1}{1000T}.

The same ε later controls winner-address accuracy, stage-sampler failure and fresh verification error, but the roles are not collected when the error budget is chosen.

**Reader cost.** The final Tε and ε terms appear to be unrelated tolerances until the reader reconstructs all three uses.

**Repair.** Add a small error-budget summary naming the three uses and their aggregate contributions; keep the existing numerical choice.

## RR9-096 — 5.2. A tournament with probabilistic comparisons

**low · prerequisite · lines 2250–2250 · U01700**

> after a history $p_1,\ldots,p_h$, the weight of $i$ is the product

The central history-to-weight formula is stated only in words and must be recovered when the tensor-product preparation is introduced.

**Reader cost.** The reader has to translate between the update rule, history L and the later success mass w_i/m without a stable displayed definition.

**Repair.** Display w_i(L)=∏_{b≤h}a_{i p_b} next to the update and reuse that notation at the sampler.

## RR9-097 — 5.2. A tournament with probabilistic comparisons

**medium · prose · lines 2307–2307 · U01740**

> A self-comparison sets its outcome bit to false and makes no query.

This branchwise statement sounds like a physical no-query claim inside a coherently controlled comparison schedule; the later compiler executes cancelling queries even on disabled branches.

**Reader cost.** The reader can confuse the abstract self-comparison operation with the number of ordinary oracle calls in the shared physical circuit.

**Repair.** Say the self-comparison is a query-free abstract operation and that the common controlled implementation may retain padded cancelling calls.

**Later resolution / qualification:** {"line_start": 2616, "description": "The controlled-read implementation explains that false-control branches still execute both ordinary queries.", "line_end": 2616, "source_path": "repository/docs/reasoning_record.md"}

## RR9-098 — 5.2. A tournament with probabilistic comparisons

**low · transition · lines 2307–2307 · U01735**

> We now implement one step quantumly.

The state preparation is developed and illustrated before the actual measured stage transition is stated several paragraphs later.

**Reader cost.** The reader knows how a weighted state is formed but not yet when its index is measured or how failure changes the list.

**Repair.** Give a short stage outline here—prepare, amplify, measure/append on success, return list on failure—then prove the exact law.

**Later resolution / qualification:** {"line_start": 2395, "description": "The real-sampler paragraph supplies the full measure/append/stop rule.", "line_end": 2395, "source_path": "repository/docs/reasoning_record.md"}

## RR9-099 — 5.2. A tournament with probabilistic comparisons

**low · example · lines 2373–2374 · U01774**

> the ideal process selects
$s$ within three pivots with probability one

The calculation explicitly treats the first pivot a and one continuation, then states an unconditional within-three-pivots conclusion.

**Reader cost.** The remaining initial pivots are easy by cyclic symmetry, but the reader must supply that argument to verify the certainty claim.

**Repair.** Add that first pivot s succeeds immediately and first pivots b or c follow by cyclic relabeling of the displayed calculation.

## RR9-100 — 5.2. A tournament with probabilistic comparisons

**low · example · lines 2378–2378 · U01776**

> To see genuinely fractional losing weights on the same four candidates

The deterministic-cycle example and fractional variation use long runs of rational calculations without a common stage summary.

**Reader cost.** Comparing which weights vanish and which remain fractional requires scanning between separated displays.

**Repair.** Add a compact stage table for each variant with pivot history, weight vector, W/m and conditional next-pivot law; preserve the existing distinction between ideal certainty and real failure.

## RR9-101 — 5.2. A tournament with probabilistic comparisons

**medium · structure · lines 2399–2399 · U01795**

> The compiled version rests on a finite-label statement.

The formal measured-label correspondence intervenes between the real algorithm and the coupling that proves its success guarantee.

**Reader cost.** The reader must leave the probability proof to parse which source implementation exports which state or output law.

**Repair.** Move the implementation comparison after the coupling or to Appendix G.7; retain here the joint-success law needed for the coupling.

## RR9-102 — 5.2. A tournament with probabilistic comparisons

**low · figure · lines 2403–2403 · U01799**

> \Pr[\bot]=f_x,

The supplied PDF sets all four clauses of the finite-label law on one very long horizontal display on page 51.

**Reader cost.** The equation nearly reaches the right page edge and forces the success law and zero-probability case to be read as one visual strip.

**Repair.** Use aligned rows separating failure mass, successful-label mass, promised failure bound and the zero-success case.

## RR9-103 — 5.2. A tournament with probabilistic comparisons

**low · prerequisite · lines 2418–2418 · U01811**

> If $W>0$, we independently choose a possible ideal next pivot

The explicit coupling recipe gives only its W>0 branch, even though the paragraph initially defines a coupling for all agreed lists.

**Reader cost.** The reader has to import the absorbing-zero and certain-failure rules to complete the marginal construction.

**Repair.** Add the W=0 branch directly: append nothing in the ideal process and stop the real process with certainty.

## RR9-104 — 5.2. A tournament with probabilistic comparisons

**medium · first_encounter · lines 2450–2450 · U01839**

> let $c_{\mathrm{rd}}$ be the number of logical reads in a comparison

The cost argument moves from physical comparison cap c to logical-read cap c_rd and later c_c, with the conversion summarized only in §5.4.

**Reader cost.** The reader can multiply by the two-query compiler twice or mistake a padded implementation bound for the ordinary construction’s exact cost.

**Repair.** Introduce one compact unit legend here for logical reads, physical bit queries and preparation calls, then point back to it in the finite budget.

**Later resolution / qualification:** {"line_start": 2636, "description": "§5.4 explicitly states that a, c_c and c_0 count logical reads and the final budget already includes factors of two.", "line_end": 2636, "source_path": "repository/docs/reasoning_record.md"}

## RR9-105 — 5.2. A tournament with probabilistic comparisons

**low · evidence_presentation · lines 2474–2474 · U01855**

> There is one input-independent bounded sampler, with output law $\lambda_x$

The finite-list formulation restates the just-proved list theorem in a new probability-law notation before the concrete comparator is introduced.

**Reader cost.** The main proof acquires another witness notation whose role is formal correspondence rather than a new algorithmic step.

**Repair.** Place this formulation in a labeled correspondence note or alongside §5.5, leaving a short link from the completed proposition.

## RR9-106 — 5.2. A tournament with probabilistic comparisons

**low · credit · lines 2484–2484 · U01861**

> **Comparison with earlier search procedures.**

The paragraph combines four literature comparisons, two complexity measures and two distinct search tasks after the proof and its formal list-law restatement.

**Reader cost.** The concrete reason each prior algorithm does not substitute for the fractional-weight process is buried in a long prose block.

**Repair.** Use a compact comparison table with task, oracle contract and relevant limitation; keep the attribution of the present fractional-weight argument adjacent to its theorem.

## RR9-107 — 5.3. Decoding, comparison, and verification

**medium · first_encounter · lines 2519–2519 · U01898**

> To compare two columns, we fix a numerical ordering of the columns.

The comparator recipe lists address decoding and pointers but never locally states that it omits the gate-transcript checks.

**Reader cost.** The reader coming directly from the local-test construction may charge the much more expensive verification work to every comparison.

**Repair.** State at the end of the recipe that comparison reads selected pointer fields only, while transcripts are checked later by the verifier.

## RR9-108 — 5.3. Decoding, comparison, and verification

**medium · transition · lines 2550–2550 · U01936**

> To verify a candidate, we decode the candidate column's address afresh, measure it, and fix the resulting address $a$.

The deliberate switch from coherent retained addresses in comparison to a measured fixed address in verification is easy to miss inside the prose.

**Reader cost.** The reader can wrongly include address decoding inside every amplified local-test call or uncompute the measured address.

**Repair.** Add a two-row interface summary: comparison retains both labels coherently; verification samples one label once before searching exact tests.

## RR9-109 — 5.3. Decoding, comparison, and verification

**low · first_encounter · lines 2586–2586 · U01977**

> Here $K\geq m\geq4$, so $0<1/K\leq1/2$

The amplification-parameter admissibility check appears after the verification proof and query estimate.

**Reader cost.** The reader applying Lemma 3.1 must temporarily supply the γ range before the text checks it.

**Repair.** Put the K≥m and ε<1/2 check alongside the first choice γ=1/K, leaving the general range reminder only once.

## RR9-110 — 5.3. Decoding, comparison, and verification

**medium · prose · lines 2598–2598 · U01990**

> \Pr[\text{error}\mid F_{k,m}(x)=0]

The displayed error bounds use conditional-probability notation even though the proof fixes x and assumes its function value.

**Reader cost.** This can suggest an input distribution or conditioning event where the query-complexity guarantee is pointwise.

**Repair.** Write the bounds as Pr_x[error] for each x with F(x)=0 or F(x)=1, or explicitly label the displayed conditioning as shorthand for these pointwise cases.

## RR9-111 — 5.4. Coherent access and the query cap

**medium · structure · lines 2616–2616 · U02002**

> A controlled read can always be implemented with two ordinary bit queries.

The load–use–unload proof partly repeats the controlled-read construction already used to prove (4.15), but in the later section it adds the crucial unchanged-coordinate explanation.

**Reader cost.** The reader has to merge two separated versions of the same implementation argument to justify the earlier cap.

**Repair.** Put the full two-query read construction at its first use in §4.6 and use §5.4 for its application to the budget, with a precise back-reference.

## RR9-112 — 5.4. Coherent access and the query cap

**medium · structure · lines 2638–2638 · U02029**

> Let $q$ be the Forrelation repetition count for error $\varepsilon/r$

The finite-budget paragraph introduces q, a, c_c, c_0, N, M_0 and M_1 in one sentence chain.

**Reader cost.** The reader must search backward through that chain to interpret every factor in the next display.

**Repair.** Put the quantities, definitions and operational meanings in a small parameter table immediately before B_{k,t}.

## RR9-113 — 5.4. Coherent access and the query cap

**low · prose · lines 2677–2677 · U02058**

> Put $\tau=2t$ and $u=2^t$

The explicit logarithm-six calculation renames the established logarithmic parameter ℓ as τ without making the equality ℓ=τ visible.

**Reader cost.** The reader must translate between the earlier circuit/comparison bounds and a fresh pair of symbols before checking the substitutions.

**Repair.** Retain ℓ throughout this calculation, or introduce τ=ℓ=2t if the source notation is important to the correspondence.

## RR9-114 — 5.4. Coherent access and the query cap

**medium · prerequisite · lines 2683–2683 · U02068**

> We insert these bounds into the two brackets of $B_{k,t}$.

The logarithm-six conclusion is carried by a long paragraph of products and enlargements, with each power contribution embedded in prose.

**Reader cost.** The reader cannot readily verify which component contributes each factor of τ or reproduce the final C_k.

**Repair.** Use a budget ledger with one row for tournament stage, all stages, fresh decoding and local-test search, showing the bound and resulting τ exponent; leave the deliberate slack explicit.

## RR9-115 — 5.5. Sequential verification of the listed candidates

**medium · first_encounter · lines 2698–2698 · U02083**

> Fix verifier acceptance probabilities $v(i)\in[0,1]$

The continuation proof does not locally say that v(i) already averages the fresh address decoder as well as the local-test search.

**Reader cost.** The reader may identify v(i) with the earlier fixed-address verification probability and omit decoder error from the Boolean continuation.

**Repair.** Define v(i) as the full fresh verifier acceptance probability at the fixed input, including address sampling.

## RR9-116 — 5.5. Sequential verification of the listed candidates

**low · prerequisite · lines 2698–2698 · U02086**

> Both the weight product and the probability that at least one fresh verification accepts are invariant under permutation

The storage-order equivalence is asserted between two recursive descriptions without displaying its simple closed form for verification.

**Reader cost.** The reader must separately reason about reversal of the list to be sure early stopping has not changed the event.

**Repair.** Add V(L)=1−∏_{i∈L}(1−v(i)) with multiplicities, which immediately explains the permutation claim and the fresh-outcome requirement.

## RR9-117 — 5.5. Sequential verification of the listed candidates

**medium · prerequisite · lines 2700–2700 · U02089**

> Let $R_n(L)$ be the acceptance probability with $n$ tournament stages still available

The main continuation recurrence, including its W=0 convention, is given only as a long prose sentence.

**Reader cost.** The subsequent induction asks the reader to repeatedly reconstruct the recurrence rather than refer to a stable formula.

**Repair.** Display R_0(L) and the positive-stage recurrence, with the W=0 case shown explicitly or attached as a clear convention.

## RR9-118 — 5.5. Sequential verification of the listed candidates

**low · prerequisite · lines 2712–2712 · U02105**

> If $B\geq0$, then $f(L)B\leq\varepsilon(1-\varepsilon)$

The sign-sensitive estimate is compressed into a paragraph that also introduces B, averages successors and subtracts the loss.

**Reader cost.** This is the step where multiplying a lower bound by 1−f could be misread when B is negative.

**Repair.** Separate the two sign cases in a short aligned bound and then state the common inequality f(L)B≤ε(1−ε).

## RR9-119 — §6, four-step plan

**low · figure · lines 2728–2728 · U02120**

> argue in four steps.

The PDF places the first item of the four-step plan at the bottom of page 60 and the other three on page 61.

**Reader cost.** The intended overview cannot be scanned as one unit before the lengthy direct-product proof.

**Repair.** Keep the plan together on one page, or shorten the introduction enough to start it wholly on the next page.

## RR9-120 — §6.1, conditional independence

**medium · first_encounter · lines 2743–2747 · U02132**

> Independent instances remain hard to solve together when each has its own
query allowance, even when the algorithm chooses adaptively

The informal claim that inputs remain independent at a history precedes the crucial fixing of independent side information and coins.

**Reader cost.** If the history omits a latent shared random seed, conditioning can create dependence; the exact transcript convention matters.

**Repair.** Add the fixing qualification to the opening intuition, then let the proof supply the rectangle calculation.

**Later resolution / qualification:** {"line_start": 2779, "line_end": 2806, "explanation": "The proof fixes independent information and proves the product posterior."}

## RR9-121 — §6.1, transcript compatibility

**low · example · lines 2813–2813 · U02164**

> An arbitrary string of proposed

The caveat about an arbitrary proposed history would be easier to verify with one impossible adaptive transcript.

**Reader cost.** The rectangle equality needs both recorded answers and compatibility with the deterministic choice of next query.

**Repair.** Add a two-query example where the proposed second coordinate conflicts with the first answer, distinguishing an impossible schedule from a zero-mass answer event.

## RR9-122 — §6.1, restoring randomization

**low · structure · lines 2920–2920 · U02211**

> To restore arbitrary independent side information and coins

The finite grouping argument is repeated here, in §3.12 and again at the generic lower-bound contradiction.

**Reader cost.** The same representation fact interrupts three different proofs and makes the conventions seem local rather than shared.

**Repair.** State the finite-mixture convention once in the model section and use short references at later applications, retaining only application-specific independence details.

## RR9-123 — §6.1, cap-event corollary

**medium · structure · lines 2947–2947 · U02224**

> **Corollary (success together with respecting the caps).**

The capped-success corollary is the interface later used, but it is not named as such until after the full conditional-value proof.

**Reader cost.** A reader may spend the proof expecting a theorem about the conditional law on cheap runs, precisely the misreading the examples later correct.

**Repair.** Preview the joint-event formulation immediately after the lemma and say that truncation converts the every-branch cap into that interface.

## RR9-124 — §6.1, budget counterexample

**low · structure · lines 3024–3024 · U02259**

> The exact calculation and enumeration in

The pooled-budget counterexample is immediately followed by an exhaustive tree-enumeration report.

**Reader cost.** The simple 3/4 versus 9/16 calculation is sufficient to establish the distinction; enumeration metadata competes with the lesson.

**Repair.** End the example with the budget distinction and move enumeration counts to an evidence note or linked artifact description.

## RR9-125 — §6.1, second proof placement

**medium · structure · lines 3052–3052 · U02273**

> A second proof, by induction on unnormalized weights

The planting interface is followed by a second full direct-product proof before the planting construction begins.

**Reader cost.** The reader must hold the simulator handoff in memory across another recurrence and induction.

**Repair.** Place the optional weighted proof after the generic lower bound or in an appendix, while retaining the normalization identity at the main proof’s end.

## RR9-126 — §6.1, normalized versus weighted values

**low · structure · lines 3120–3120 · U02306**

> The two proofs rest on the same one-factor calculation.

The exact normalization identity appears only after the second proof has introduced a separate vocabulary and completed its induction.

**Reader cost.** Readers cannot use the connection to orient themselves while learning W.

**Repair.** Preview Wc(ν)=mass(ν) times the normalized continuation value before the weighted proof, treating zero mass separately, and retain the final derivation.

## RR9-127 — Sources

**medium · first_encounter · lines 3148–3148 · U02317**

> Drucker

The source comparison supplies a global-budget alternative that is sufficient for the application, but its quantitative specialization is buried in prose.

**Reader cost.** The reader cannot readily see which resource advantage the custom direct-product lemma adds.

**Repair.** Show a small table comparing per-instance cap, total budget and resulting success bound for the two routes.

## RR9-128 — §6.1, global-budget alternative

**low · transition · lines 3153–3153 · U02321**

> $\mu$ be the minimax law of §6.2

The Drucker substitution uses the minimax law µ of §6.2 before that law has been constructed.

**Reader cost.** This is a backward dependence in a paragraph whose only purpose is optional source comparison.

**Repair.** Move the numerical alternative after the minimax step, or begin it conditionally with the exact one-instance hypothesis it will later receive.

## RR9-129 — §6.1, alternative numerical tail

**medium · prerequisite · lines 3162–3162 · U02324**

> there would remain at most $6/100$.

The assertion that the factor-two tail still leaves the total at most 6/100 omits the small numerical inequality that makes it true.

**Reader cost.** Doubling the later coarse 1/100 bound would appear to give 7/100, so the reader needs the retained m-dependence.

**Repair.** Show 2/(100m^8)≤1/100 for m≥4 before adding 4/100 and 1/100.

## RR9-130 — §6.2, local construction recap

**low · structure · lines 3179–3179 · U02337**

> Each of the \(m\) columns contains

The recap repeats the entire layout in one dense paragraph immediately before another statement of the generic theorem.

**Reader cost.** It is hard to identify the three pieces that the classical proof actually uses: zeros, hard inputs and addressed cells.

**Repair.** Give a compact three-row layout keyed to X, A and B, with one line each for independence and the simulator’s access.

## RR9-131 — §6.2, minimax law dependence

**medium · prerequisite · lines 3192–3192 · U02349**

> Assume that \(L\) is a nonnegative integer

The law µ is introduced without recording in its notation or accompanying sentence that it may depend on P and the chosen cap L.

**Reader cost.** The later family varies parameters, and there is no claim of one law hard for all caps or dimensions.

**Repair.** State the dependencies of µ at the conclusion of the minimax lemma and that the proof chooses it after fixing P and L.

## RR9-132 — §6.2, finite separation proof

**medium · prerequisite · lines 3204–3204 · U02364**

> differentiating this quadratic from the right at zero gives

The nearest-point argument condenses positivity, a directional derivative and the sign of the separating vector into one paragraph.

**Reader cost.** This is a nonstandard-looking proof of a familiar minimax step, and readers cannot readily check the strict common margin.

**Repair.** Split the argument into the closest-pair construction and the derivative inequality, displaying v·(b−a)≤0 before using the coordinates where vx>0.

## RR9-133 — §6.2, address law

**medium · prerequisite · lines 3216–3216 · U02373**

> We apply Lemma 4.1 of §6.1 to independent

The vector-prediction bound is stated without explicitly saying that the output bits P(Uh) can be biased.

**Reader cost.** Independence of input instances does not mean the hidden address is uniform, and address-uniformity would be a stronger unjustified assumption.

**Repair.** State that the answer bits need not be uniform and that their unpredictability is furnished by the one-input success bound under µ.

## RR9-134 — §6.2, repeated source comparison

**low · structure · lines 3223–3223 · U02378**

> his headline theorem, stated for one global budget, would also serve

The source paragraph repeats the fair/global-budget comparison immediately after §6.1 already explained and parameterized it.

**Reader cost.** The reader encounters another literature detour just as the promised law has made planting possible.

**Repair.** Keep one consolidated comparison and reduce this occurrence to the exact theorem interface being used.

## RR9-135 — 6.3. Coupled zero and one inputs

**medium · first_encounter · lines 3226–3226 · U02381**

> 6.3.

The coupling is described through textual modifications of a large board without a compact before/after view.

**Reader cost.** The first-difference proof depends on exactly two classes of changed bits.

**Repair.** Add a before/after table listing unchanged fields, erased zero and planted cell.

## RR9-136 — §6.3, sampling space

**medium · structure · lines 3249–3249 · U02399**

> The zero positions $J_1,\ldots,J_m$ are independent uniform rows.

The sampling explanation anticipates simulator access and then repeats the actual sampling definition below.

**Reader cost.** Independence, construction and access permissions are intertwined, making it harder to verify the probability space once.

**Repair.** Use one sampling-order list that makes the selected column independent of the entire dummy experiment, followed by a separate simulator-access table; avoid stating the sampling twice.

## RR9-137 — §6.3, finite resampling remark

**low · structure · lines 3268–3268 · U02416**

> Resampling a coordinate from its original law preserves the expectation

The paragraph teaches an abstract resampling identity that is not named when the imminent planting estimates use conditioning and averaging.

**Reader cost.** It creates a new operation for the reader to track without a visible payoff.

**Repair.** Attach the finite-sum identity to its first actual use or state which later averaging step it justifies.

## RR9-138 — §6.3, toy parameter scope

**low · first_encounter · lines 3287–3287 · U02433**

> we temporarily take \(m=4\), \(r=2\)

The toy parameter tuple and zero-based convention are given before the board, but the precise exclusion from the generic lower-bound parameter regime appears only after it.

**Reader cost.** Readers can initially try to reconcile incompatible parameters while reconstructing the example.

**Repair.** Move the existing statement that this toy does not satisfy r=40t and G=floor(mL/100) to its introduction; do not add a second warning or claim the tuple is undefined.

**Later resolution / qualification:** {"line_start": 3300, "line_end": 3300, "explanation": "The later artifact paragraph explicitly excludes the theorem’s parameter choice."}

## RR9-139 — §6.3, toy evidence

**low · evidence_presentation · lines 3300–3300 · U02442**

> implement all 192 physical bit coordinates of this toy

The implementation and coordinate-count report interrupts the mathematical transition from the planted board to the coupling.

**Reader cost.** The reader needs the changed-bit set next, rather than details of the archival checker.

**Repair.** Move the checker paths and 192-coordinate census to the example caption or an evidence note, leaving the parameter-scope caveat with the example’s introduction.

## RR9-140 — §6.3, first difference

**low · prerequisite · lines 3307–3307 · U02450**

> the absolute difference of the expected output indicators

The Boolean-output inequality is described verbally, although it is the precise step converting coupling into a distributional gap.

**Reader cost.** Writing it explicitly would distinguish this statement from a total-variation claim about the whole transcript.

**Repair.** Include |E T(Y1)−E T(Y0)|≤E|T(Y1)−T(Y0)|=Pr[T(Y1)≠T(Y0)] before the event union.

## RR9-141 — §6.4, overloaded Z

**low · prose · lines 3332–3332 · U02464**

> the product potential called $Z$ in §6.1 is no longer in use.

The new discovery count reuses Z from the product potential and needs an explicit retirement sentence to repair the collision.

**Reader cost.** The proof repeatedly sends readers back to §6.1, so the retired notation remains live during cross-reading.

**Repair.** Give the discovery count a distinct symbol or subscript and eliminate the retirement explanation.

## RR9-142 — §6.4, independence example placement

**medium · structure · lines 3342–3342 · U02472**

> **Independence of the selected column.**

A full counterexample to dependent column selection interrupts the identity-to-search-bound chain.

**Reader cost.** The proof has already specified independent I, and the pending task is to bound EZ; the long interruption increases the chance of losing that goal.

**Repair.** Retain a one-sentence warning at the identity and move the full four-column example after the early/late estimate or into a clearly inset example.

## RR9-143 — §6.4, adaptive zero posterior

**low · prerequisite · lines 3354–3354 · U02485**

> To handle adaptivity, we fix a positive-probability transcript prefix.

The proof repeats the transcript-rectangle reasoning from §6.1 but the analogy is not pointed out.

**Reader cost.** Readers may treat this as a new independence theorem instead of the same fixed-history mechanism with different coordinates.

**Repair.** Refer explicitly to the earlier cylinder argument and then state the extra fact specific here: blank B cells constrain no J or A values.

## RR9-144 — §6.4, early discovery accounting

**low · prerequisite · lines 3366–3366 · U02494**

> Assigning contribution zero after a branch stops

The fixed-horizon summation does not name the indicator being summed.

**Reader cost.** Readers checking repeated queries and early stopping must reconstruct how a single discovery contributes exactly once.

**Repair.** Define the indicator that query q is the first zero discovery in its column while fewer than m/2 rows were previously tested, then sum its conditional expectation.

## RR9-145 — §6.4, optional search variants

**medium · structure · lines 3388–3388 · U02507**

> The rest of §6.4 gives two optional estimates for the same term

After declaring the main proof ready to continue, the section presents two stronger alternatives before allowing that continuation.

**Reader cost.** A complete sequential reader cannot use the route shortcut and must carry the unresolved planted-cell event through both alternatives.

**Repair.** Put the optional search refinements after the generic theorem, with a forward link here, or group them in an appendix.

## RR9-146 — §6.4, alternative search worlds

**medium · question · lines 3394–3394 · U02514**

> the total number of queries to this column

“Queries to this column” is ambiguous in a construction where a column includes X, A and B; the conclusion later counts only X queries.

**Reader cost.** The induction’s answer-one branch is valid for X positions, whereas A/B queries need to be fixed side-data queries.

**Repair.** Define the worlds by varying only the selected X column, fixing every other bit including that column’s A/B fields, and define QU to count X queries only.

**Later resolution / qualification:** {"line_start": 3419, "line_end": 3419, "explanation": "The final averaging step specifies QX as the number of X-bit queries."}

## RR9-147 — §6.4, reference all-one path

**low · prerequisite · lines 3434–3434 · U02546**

> in order of first appearance.

The reference path proof lists distinct positions but the lower cost bound includes repeated and post-discovery calls only implicitly.

**Reader cost.** The inequality is deliberately one-sided and does not assume that the algorithm stops at discovery.

**Repair.** State before the sum that extra calls only increase the counted cost and that matching the all-one path is used only until the first differing answer.

## RR9-148 — §6.5, heavy-column notation

**low · prose · lines 3455–3455 · U02561**

> Let \(q_i\) be the number of queries

The terminal count qi and the following fixed time q use nearly identical notation for unrelated quantities.

**Reader cost.** The simulator proof already requires two clocks, so this overload adds avoidable reading friction.

**Repair.** Use a distinct name for the complete-run target-call count and reserve q for the original query time.

## RR9-149 — §6.5, simulator clocks

**medium · prerequisite · lines 3469–3469 · U02576**

> charged against one shared counter

The simulator paragraph implements two clocks but never labels them together: original query time and charged target-query count.

**Reader cost.** An outside query advances q without using the direct-product allowance, and that distinction is essential to the union bound.

**Repair.** State the two counters explicitly or show a two-column trace convention before the algorithm description.

## RR9-150 — §6.5, fixed default

**low · prerequisite · lines 3469–3469 · U02578**

> it outputs a fixed vector.

The fixed-vector default is part of the construction but its role in the success-event inclusion is postponed until the example.

**Reader cost.** A reader may incorrectly infer equality between visiting the true cell cheaply and simulator success.

**Repair.** Say immediately that defaults may also be correct, so only containment of the joint event is required.

**Later resolution / qualification:** {"line_start": 3511, "line_end": 3511, "explanation": "The XOR example computes the extra successful default mass."}

## RR9-151 — §6.5, complete-run nonheaviness

**medium · prerequisite · lines 3477–3477 · U02586**

> suppose the complete dummy run makes column \(i\) nonheavy

The event uses complete-run nonheaviness even though the simulator only needs the prefix before q to obey the cap.

**Reader cost.** The stronger event is valid, but without explaining the choice it can look as though future run information is supplied to the simulator.

**Repair.** Say that the simulator never tests complete-run nonheaviness; this stronger event is chosen solely to match the heavy-column counting bound.

## RR9-152 — §6.5, simulator example narrative

**medium · structure · lines 3489–3489 · U02597**

> Readers coming from the examples-first exposition should note two differences

The example introduction spends a long sentence comparing another document’s board before stating the four-query tree.

**Reader cost.** The local example’s operation is obscured by cross-document differences and indexing history.

**Repair.** State the local P, labels and tree first; put the companion comparison in a short parenthetical note after the trace.

## RR9-153 — §6.5, simulator trace layout

**low · figure · lines 3493–3493 · U02602**

> At time 1 the proposed query is $X_0[0]$

The four times and charged counts are written as one long prose paragraph on page 73.

**Reader cost.** The very distinction the example teaches requires visual comparison across four separate steps.

**Repair.** Use a trace table with original time, proposed query, answer source, target count and action.

## RR9-154 — §6.5, toy probability provenance

**low · structure · lines 3497–3497 · U02609**

> The exhaustive enumeration in the

The probability displays are introduced as results of exhaustive enumeration before the short analytic calculation is shown.

**Reader cost.** The event inclusion should be understood from the target bits without requiring trust in a historical checker.

**Repair.** Present the 1/8+1/8 derivation first and place the enumeration scope afterward as supplementary evidence.

**Later resolution / qualification:** {"line_start": 3511, "line_end": 3511, "explanation": "The following paragraph derives the probabilities directly."}

## RR9-155 — §6.5, second conditioning example

**low · structure · lines 3517–3517 · U02624**

> The following smaller example isolates the nonheavy event

A third local example of conditioning follows the full cap-event example and the simulator’s default-mass example.

**Reader cost.** The examples teach related but distinct failures, and their cumulative length can hide the exact purpose of this final one.

**Repair.** Introduce a one-line contrast of purposes—dependence of a cap event, extra default success, and selection of easy inputs—or consolidate the repeated conditioning lesson.

## RR9-156 — §6.5, union and average

**medium · prerequisite · lines 3524–3524 · U02636**

> We average over the independent uniform \(I\)

The key no-extra-m calculation is expressed in prose and a final bound, leaving its two operations easy to swap.

**Reader cost.** Unioning over all columns before averaging would falsely introduce an m factor into the critical tail.

**Repair.** Display m^−1 Σ_i Σ_q Pr(Eiq)≤G(2/3)^r with Eiq defined as the fixed-column joint event.

## RR9-157 — §6.6, completion handoff

**low · transition · lines 3537–3537 · U02646**

> may return to its §4.5.

The sentence inviting companion readers to return occurs before the finite numerical contradiction has actually been completed here.

**Reader cost.** The destination may rely on the very estimate the reader is about to leave before seeing established.

**Repair.** Move the return instruction after the generic theorem’s contradiction, or specify that the remaining finite arithmetic is supplied at the destination.

## RR9-158 — §6.6, alternative coefficient

**low · structure · lines 3547–3547 · U02651**

> The alternative search estimate likewise gives

The coefficient-two variant is displayed again before the coefficient-four proof is numerically closed.

**Reader cost.** The active bound and optional strengthening become parallel proof targets even though one suffices.

**Repair.** Finish the finite contradiction using coefficient four, then note the coefficient-two replacement in a separate optional sentence.

## RR9-159 — §6.6, PDF arithmetic transition

**low · figure · lines 3572–3572 · U02667**

> and

Page 75 begins with the orphan connective “and” and the sum bound, separated from the individual estimates at the bottom of page 74.

**Reader cost.** The reader cannot check the numerical assembly without turning back across the page boundary.

**Repair.** Keep the individual terms and their total together as one aligned display or prevent the break before the total.

## RR9-160 — §6.6, asymptotic tail comparison

**low · structure · lines 3579–3579 · U02670**

> For comparison with the preprint, the exact logarithmic form is

After a finite bound valid for all permitted dimensions, the text pauses for a separate asymptotic logarithmic comparison before the contradiction.

**Reader cost.** The proof is ready to finish and the asymptotic check no longer supplies a needed premise.

**Repair.** Move the preprint comparison after the contradiction or into the source-comparison note.

## RR9-161 — §6.6, Forrelation specialization

**medium · structure · lines 3605–3605 · U02689**

> all sufficiently large powers of four \(m\).

The specialization reopens the published Forrelation comparison before applying the explicit prerequisite already proved in §3.

**Reader cost.** Readers completing the direct-proof route are made to reassess a literature theorem whose proof display is separately qualified.

**Repair.** Apply the §3.15 prerequisite directly and place the published comparison in one consolidated source note.

## RR9-162 — §6.6, floor threshold interface

**low · prerequisite · lines 3619–3619 · U02701**

> with a threshold uniform in \(k\)

The floor arithmetic begins a new t≥8 calculation without first stating the combined threshold that will be used.

**Reader cost.** The reader must carry the Forrelation threshold and the elementary floor threshold separately until the last paragraph.

**Repair.** State t≥max{8,t0(k)} at the start of the specialization and note that the explicit §3.15 choice already dominates eight.

## RR9-163 — §6.6, circuit index consistency

**medium · prose · lines 3652–3652 · U02720**

> the circuit \(C_{k,m}\)

The circuit is called C_(k,m) here but C_(k,t) in §7, with no local statement identifying the two indexings.

**Reader cost.** The separation requires the same circuit and total function on both sides, so a notation change at that handoff is unusually costly.

**Repair.** Choose one circuit indexing throughout the handoff or explicitly identify C_(k,m)=C_(k,t) when m=4^t.

**Later resolution / qualification:** {"line_start": 3692, "line_end": 3701, "explanation": "§7 introduces C_(k,t) and emphasizes that the same circuit is used."}

## RR9-164 — §6.6, quantified threshold

**low · prerequisite · lines 3668–3668 · U02729**

> the threshold supplied by Forrelation hardness may depend on the fixed \(k\).

The final proposition says the threshold may depend on k even though the record has already supplied an explicit sufficient choice.

**Reader cost.** The advertised numerical threshold is difficult to recover at the exact classical endpoint where a user might apply it.

**Repair.** State the available combined sufficient threshold here, while retaining the fixed-k formulation as the conceptual theorem.

## RR9-165 — 7. The optimal exponent

**medium · first_encounter · lines 3674–3674 · U02735**

> 7. The optimal exponent

The exponent section restates the definition of alpha_tot and the theorem before collecting the actual bounds.

**Reader cost.** The repeated headline delays the one new task: comparing growth rates with the correct quantifier order.

**Repair.** Open with the two same-family estimates and refer back to the definition, retaining only the quantifier reminder needed here.

## RR9-166 — §7.1, logarithmic exponent

**low · prose · lines 3701–3701 · U02750**

> The quantum estimate allows \(b_k=6\) for every \(k\)

The section introduces a variable bk and immediately says it can always be six.

**Reader cost.** The extra symbol increases the parameter bookkeeping in an argument whose only varying parameter is already k.

**Repair.** Use six in the displayed family estimates unless the generalized log-exponent proof is itself an intended reusable lemma.

## RR9-167 — §7.1, asymptotic quotient

**low · prerequisite · lines 3733–3733 · U02770**

> put \(e=2+\alpha b_k\)

The logarithmic domination proof changes variables and notation immediately after the finite quotient without first isolating its positive exponent.

**Reader cost.** The decisive fact is εα>0; the remaining logarithm estimate is routine but can obscure that dependence on the earlier choice of k.

**Repair.** State that k and εα are now fixed with εα>0 before introducing e and the t parameter.

## RR9-168 — 7.2. Excluding all smaller universal powers

**medium · chronology · lines 3758–3758 · U02786**

> bijection

The final reindexing step is short but arrives after all asymptotics, although the function has been structurally indexed throughout.

**Reader cost.** A reader may have wondered since §4 whether the family belongs to the theorem’s standard cube domain.

**Repair.** Link the coordinate-renaming lemma at the first definition of the structured total function and retain this step as its application.

## RR9-169 — §7.3, growing-parameter result

**medium · structure · lines 3777–3777 · U02802**

> we assemble such a family from estimates already proved

The reader is promised a single family approaching exponent four, but the explicit result is postponed until after a full page of constants.

**Reader cost.** There is no compact target against which to assess the purpose of each ensuing estimate.

**Repair.** State the schedule k=floor√(t/20), the valid range t≥80 and the final exponent function at the section’s start, then derive them.

## RR9-170 — §7.3, quantum constant expansion

**medium · structure · lines 3779–3779 · U02803**

> expanding the constant $C_k$ of §5.4 gives

The exact decimal expansion of Ck comes before the only scale used in balancing, namely k·2^(10k).

**Reader cost.** Readers must process large integers before seeing the tradeoff that selects k.

**Repair.** Lead with Ck≤2^53 k2^(10k), explain its role in 40k, and put the digit-by-digit verification in an aligned note.

## RR9-171 — §7.3, logarithm bound

**medium · prerequisite · lines 3793–3793 · U02813**

> also $\ln(4k)\le(1-\ln2)\,2t$

The implication from k≤2t/15 to ln(4k)≤(1−ln2)2t is asserted without the scalar inequality that justifies it.

**Reader cost.** This inequality supplies the denominator bound behind X≥2 and is not a direct rearrangement of k≤2t/15.

**Repair.** Show the scalar chain justifying the logarithmic bound, for example ln(4k)≤4k−1≤8t/15−1≤2t(1−ln2), using an explicit bound on ln 2. The easy X<m statement is not treated as a separate gap.

## RR9-172 — §7.3, uniform lower-bound assembly

**medium · structure · lines 3793–3793 · U02817**

> Since $R(F_{k,m})$ is an integer

One paragraph establishes X<m, X≥2, two admissibility conditions, an integer strictness improvement and the final total lower bound.

**Reader cost.** The rounding argument is difficult to audit because each conclusion becomes a premise before the paragraph has a visual break.

**Repair.** Separate admissibility of L from the transfer to R(F), and display the integer step R>floor(y)⇒R>y explicitly between them.

## RR9-173 — 7.3. Letting $k$ grow with $t$

**medium · first_encounter · lines 3793–3793 · U02814**

> t=32

The base case 2^t≥648t^3 is asserted numerically inside the schedule derivation.

**Reader cost.** A mistaken base value would affect the claimed all-t range of the final family.

**Repair.** Print the exact integer comparison at t=32 or link a small check with its explicit output.

## RR9-174 — §7.3, parameter regimes

**medium · prerequisite · lines 3800–3800 · U02821**

> We now choose $k=\lfloor\sqrt{t/20}\rfloor$ with $t\ge80$.

The growing schedule has t of order k² with a coefficient far below the earlier 13669 threshold, but the reason this is legitimate is only implicit in the new L choice.

**Reader cost.** A reader can incorrectly think the schedule violates the fixed-k prerequisite used for the original L.

**Repair.** State that §7.3 uses L=floor X from the uniform theorem, replacing the earlier m^(1−1/k)/(log m)² allowance, so it needs only 15k+2≤2t.

## RR9-175 — §7.3, logarithms of complexities

**low · prerequisite · lines 3805–3805 · U02828**

> Then $\log_2R(F_t)>A$, $\log_2Q(F_t)\le B$

The proof takes log Q(Ft) before stating that Ft is nonconstant and hence Q(Ft)≥1.

**Reader cost.** The later sign-sensitive exponent comparison makes positivity a logical premise rather than a cosmetic convention.

**Repair.** Move the nonconstancy and Q,R≥1 observation before the first logarithms, and give a precise pointer to the available zero/one inputs and their parameter range.

**Later resolution / qualification:** {"line_start": 3819, "line_end": 3819, "explanation": "Positivity is stated near the final exponent comparison."}

## RR9-176 — §7.3, final slack

**low · prose · lines 3818–3818 · U02837**

> the convenient bound $508$.

The larger constant 508 is called convenient without explaining what convenience it buys over 474.

**Reader cost.** The record emphasizes explicit constants, so an unexplained numerical relaxation looks arbitrary.

**Repair.** Name the interface or simplification requiring 508, or state simply that this is a chosen harmless slack value.

## RR9-177 — §7.3, nonvacuous asymptotic family

**medium · prerequisite · lines 3823–3823 · U02845**

> The exponents therefore tend to four

The concluding exponent statement does not explicitly say that Q(Ft) tends to infinity along the family.

**Reader cost.** Exponents approaching four are more informative when the complexity variable itself is seen to grow.

**Repair.** Derive this in one sentence from the growing R lower bound and the total-function quartic upper bound already proved in Appendix A.

## RR9-178 — A.1. Degree, sensitive blocks and the sensitivity graph

**low · first_encounter · lines 3844–3844 · U02865**

> A.1.

The upper-bound appendix introduces four complexity/sensitivity quantities before showing a single example relating them.

**Reader cost.** The chain is elementary to specialists but abstract for the document’s broader learning route.

**Repair.** Consider one tiny Boolean-function illustration relating the newly defined measures. Treat this as optional support for the outside reader, not an unstated prerequisite or a missing proof.

## RR9-179 — A.1. Degree, sensitive blocks and the sensitivity graph

**low · first_encounter · lines 3854–3854 · U02872**

> At a cube point

The short uniqueness induction leaves the roles of p, p0 and p1 implicit for a reader who has not recently used multilinear interpolation.

**Reader cost.** The subsequent maximum-degree argument relies on this representation rather than a general polynomial surrogate.

**Repair.** Say that p is the difference of two multilinear representations, and that p0,p1 are polynomials on n−1 variables. The omitted trivial base case is not a mathematical defect.

## RR9-180 — A.1. Degree, sensitive blocks and the sensitivity graph

**low · first_encounter · lines 3870–3870 · U02887**

> two adversary estimates

The text explicitly identifies the two adversary matrices, but the associated norm and mask-norm calculations must be collected from their separate later applications.

**Reader cost.** A reader may try to derive both inequalities from the sensitivity graph and miss the block-flip star.

**Repair.** Consider a compact dependency summary pairing each matrix with its norm ratio and resulting measure bound, without repeating the proofs.

## RR9-181 — A.2. The nonnegative adversary bound

**low · prerequisite · lines 3901–3901 · U02912**

> Randomness can be purified.

The normal-form proof compresses finite classical randomness to one unexplained sentence before giving the measurement isometry in full.

**Reader cost.** A reader reconstructing the promised self-contained reduction cannot see how the arbitrary real mixture weights enter a pure finite state.

**Repair.** Add the standard finite selector construction with amplitudes √p_j and keep the selector as an orthogonal history register; no extended purification theorem is needed.

## RR9-182 — A.2. The nonnegative adversary bound

**medium · prerequisite · lines 3905–3905 · U02922**

> Thus this conversion preserves the query cap; it introduces no extra factor two into (A.3).

Appendix A gives a second normal-form construction in the bit-oracle model without explicitly connecting its cap preservation to the controlled-phase bridge in §2.5.

**Reader cost.** The reader may think the two reductions disagree about padding or need to compose them and pay another conversion.

**Repair.** Say that this is a direct bit-oracle version of the same deferred-measurement principle, chosen here to expose the exact adversary coefficient, with no need to apply both reductions.

## RR9-183 — A.2. The nonnegative adversary bound

**low · prose · lines 3907–3907 · U02924**

> Track the complex-valued progress

The summands are complex, but the symmetric sum W_t is real because the (x,y) and (y,x) terms are conjugates.

**Reader cost.** The phrase suggests a genuinely complex progress quantity and leaves an avoidable layer of reasoning around the later real initial value and absolute-value estimates.

**Repair.** Call it a real progress quantity written using complex overlaps, or add the conjugate-pair observation once.

## RR9-184 — A.2. The nonnegative adversary bound

**low · prerequisite · lines 3932–3932 · U02939**

> the constraints force its maximum to occur at

The final-overlap proof names the extremal endpoint probabilities without spelling out the monotonic angle interval argument.

**Reader cost.** This is the one step converting the two success inequalities into the numerical coefficient 2√2/3.

**Repair.** Add that u≤arcsin√(1/3), v≥arcsin√(2/3), and cos(v−u) decreases for their nonnegative angle gap, so the smallest gap gives the stated endpoint.

## RR9-185 — A.2. The nonnegative adversary bound

**medium · structure · lines 3957–3957 · U02959**

> **The prefactor can be checked on two bits.**

The detailed edition-specific prefactor challenge interrupts the path from the adversary lemma to its two applications.

**Reader cost.** The reader has to complete a separate source-discrepancy argument before recovering how the quartic estimate is assembled.

**Repair.** Move the parity prefactor audit to the source-comparison appendix or a clearly optional note; leave the correct coefficient and exact citation at (A.3).

## RR9-186 — A.4. A maximum-degree face and Huang's signed cube

**low · structure · lines 4043–4043 · U03044**

> with the convenient extension \(H'_0=(0)\)

The zero-dimensional signed-matrix extension is introduced after the proof has already restricted to d≥1 and does not use this extension.

**Reader cost.** The main eigenspace argument is interrupted by a boundary convention that cannot arise in this branch of the proof.

**Repair.** Put the unused boundary convention in a footnote or the formal correspondence discussion, while retaining j≥1 in the multiplicity statement.

## RR9-187 — A.5. Midrijānis's decision tree

**medium · prerequisite · lines 4068–4068 · U03068**

> Otherwise it selects a maximum-degree monomial

The decision-tree algorithm implicitly treats the truth table or polynomial of the fixed function and every restricted polynomial as available without query cost.

**Reader cost.** A reader can confuse expensive classical preprocessing with input-bit queries and wonder how the algorithm identifies this monomial.

**Repair.** State that f is fixed when the decision tree is designed and all polynomial manipulation is free input-independent computation.

## RR9-188 — eq-3

**low · notation · lines 4239–4239 · U03206**

> z_1,...,z_k

The literal catalogue uses one-based Forrelation block indices while the main definition uses zero-based indices; the translation is left to the reader.

**Reader cost.** A verifier comparing the catalogue row to its proof must translate indices before checking matrix order and boundary factors.

**Repair.** Add one notation crosswalk adjacent to B.2, preserving all literal ledger quotations.

## RR9-189 — B.5. Tournament sampling

**medium · first_encounter · lines 4639–4639 · U03472**

> Some component rows about the sampler, coupling and cost retain partial ties

The catalogue describes exact and partial correspondence at group level, but individual entries expose only argument links. A row read or quoted on its own loses the group’s scope qualification.

**Reader cost.** Several rows conjoin construction, interpretation and a bound. One linked declaration may support only part of that row.

**Repair.** Add a source-bound crosswalk beside the catalogue rows, separating literal claim clauses, supporting declarations, single-primary-declaration relation and aggregate clause coverage. Include the exponent/family and full-Appendix-A examples without rewriting the archival quotations.

## RR9-190 — Appendix C. References and inspected editions

**low · first_encounter · lines 5609–5609 · U04112**

> Inspected edition or source

The bibliography uses the same “Inspected edition or source” label for full-text editions and for metadata records. The prose gives the limits, but a link scan does not show them.

**Reader cost.** A reader should be able to tell what evidence a link exposes before using it to check a theorem or edition.

**Repair.** Use link labels that identify full-text edition, version metadata or publication metadata, keeping the existing inspection-scope notes.

## RR9-191 — Appendix D, general threshold parameters

**low · prerequisite · lines 5776–5776 · U04416**

> and a real $0<\delta\le1$.

The appendix temporarily frees δ and τ after the main proof has fixed both in terms of k.

**Reader cost.** Readers can accidentally carry the old specializations into the new general threshold formula.

**Repair.** Announce this temporary generalization explicitly before H1 and state where the Forrelation specialization resumes.

## RR9-192 — Appendix D, repeated floor lemma

**low · structure · lines 5798–5798 · U04423**

> First, $4t^2\le2^t$ for every integer $t\ge8$.

The proof of 4t²≤2^t is repeated verbatim in substance from §6.6.

**Reader cost.** The duplicate elementary induction adds length without changing its hypothesis or use.

**Repair.** Give the inequality with a precise cross-reference to the earlier proof, retaining only the new application to X.

## RR9-193 — Appendix D, claim identifier

**low · evidence_presentation · lines 5823–5823 · U04438**

> These estimates prove the precise ordinary statement NEW-FOR-25.

The bare internal identifier NEW-FOR-25 is used as the conclusion of a mathematical derivation.

**Reader cost.** A reader who does not know the catalogue cannot tell which quantified statement has just been established.

**Repair.** State the content of the conclusion in mathematical terms and put the identifier in a linked parenthetical catalogue reference.

## RR9-194 — Appendix D, three threshold versions

**medium · evidence_presentation · lines 5849–5849 · U04453**

> a separately named explicit, coarser threshold $t\ge3499200k^2$

The paragraph introduces a third threshold 3499200k² without identifying the exact separately named source statement that owns it.

**Reader cost.** The old maximum, current 13669k² and coarser named threshold are difficult to distinguish as mathematical and formal interfaces.

**Repair.** Use a three-row threshold table with purpose, hypotheses and exact destination for each, or remove the unnamed third figure from this paragraph.

## RR9-195 — Appendix E, source audit presentation

**medium · evidence_presentation · lines 5861–5861 · U04466**

> the supplied source archive has SHA-256

The comparison opens with a long source hash and physical source-file lines before identifying the mathematical discrepancy.

**Reader cost.** Provenance displaces the equation comparison that lets readers judge the claim.

**Repair.** Lead with edition, page and equation; move the archive hash and physical line coordinates to a compact provenance note or table.

## RR9-196 — Appendix E, source notation translation

**low · prose · lines 5865–5865 · U04468**

> $h=k(k-1)$

The source comparison introduces N, α, Λ and h at once while the main text already used k,m,δ,L and h for related quantities.

**Reader cost.** Readers must mentally translate before checking the exponent loss.

**Repair.** Give a source-to-record notation table, especially N↔m, and avoid reusing h for k(k−1) without flagging the change from k−1.

## RR9-197 — Appendix E, reciprocal error structure

**medium · structure · lines 5896–5896 · U04488**

> There is also a separate reciprocal error

A separate exceptional-probability error is appended to the logarithmic comparison without a distinct subheading.

**Reader cost.** Two independent source defects, with different consequences and repairs, are liable to be conflated.

**Repair.** Give the reciprocal-error calculation its own short labeled subsection, with Theorem 3.1 and equation (5.31) as separate source locators.

## RR9-198 — Appendix E, SSW transfer heading

**low · figure · lines 5910–5910 · U04499**

> Sherstov, Storozhenko, and Pei Wu prove a stronger Fourier-growth theorem.

The SSW comparison begins with a long run-in heading and immediate edition-numbering details rather than the mathematical purpose.

**Reader cost.** On page 113, the entry into a new optional proof is visually and conceptually hard to locate.

**Repair.** Use a normal subsection heading stating the transfer task, followed by the theorem and then a concise edition note.

## RR9-199 — Appendix E, random-restriction law

**medium · prerequisite · lines 5920–5920 · U04507**

> Independently leave coordinate $i$ free with probability $p_i$

The restriction probabilities and the Fourier coefficient convention are packed into the same paragraph as the forecast cancellation of k.

**Reader cost.** The reader needs to verify a probability law before following its analytic payoff.

**Repair.** Separate the restriction experiment into free/fix-plus/fix-minus outcomes, verify they sum to one, then state F57 and its purpose.

## RR9-200 — Appendix E, restriction identity

**medium · example · lines 5923–5923 · U04511**

> \mathbb E_\rho\widehat {g_\rho}(S)

The phrase “a monomial expansion gives” omits the small coefficient calculation that carries the whole transfer.

**Reader cost.** Readers cannot tell immediately why fixed coordinates contribute µi rather than normalized conditional means.

**Repair.** Check F57 on a single monomial: coordinates in S must be free and each remaining selected coordinate contributes its unconditional fixed-sign mean µi; then invoke linearity.

## RR9-201 — Appendix E, blockwise free probabilities

**low · prerequisite · lines 5928–5928 · U04512**

> take $p_i=1/2$ on the first and last blocks

The choices one half and three quarters are stated without recalling the endpoint and interior bias bounds that make them admissible.

**Reader cost.** The random restriction law requires |µi|≤1−pi, so these values are not arbitrary.

**Repair.** Recall |µi|≤1/2 at endpoints and ≤1/4 inside, then show that the chosen pi saturate those constraints.

## RR9-202 — Appendix E, expanded dimension domain

**medium · prerequisite · lines 5941–5941 · U04522**

> Assume $m$ is a power of two

The calculation switches from powers of four to powers of two before explaining why the original construction restriction can be dropped here.

**Reader cost.** A reader may read the result as silently extending the frozen family definition or its formal coverage.

**Repair.** Move the Walsh-matrix explanation and the limitation to this ordinary comparison before the changed assumption.

**Later resolution / qualification:** {"line_start": 5967, "line_end": 5967, "explanation": "The final paragraph explains the ordinary Walsh extension and formal limit."}

## RR9-203 — Appendix E, amplification ceiling

**low · prerequisite · lines 5942–5942 · U04522**

> $\tau=\lceil5k\ln2/\eta^2\rceil<4k/\eta^2$.

The strict upper bound on the ceiling is given without the k≥2 estimate that absorbs its additive one.

**Reader cost.** The cancellation of k in the final constant depends on this bound and the endpoint η=1 is included.

**Repair.** Show ceil(5k ln2/η²)≤5k ln2/η²+1<4k/η² for k≥2 and 0<η≤1.

## RR9-204 — Appendix E, comparison theorem interface

**medium · prerequisite · lines 5958–5958 · U04528**

> Consequently the comparison route proves, assuming (F56),

The final variable-error display inherits several assumptions from preceding paragraphs rather than restating them as a usable proposition.

**Reader cost.** A reader returning to F60 cannot immediately recover k’s range, the power-of-two condition, the dimension threshold and the external constant’s status.

**Repair.** State all hypotheses and the unspecified absolute C with F60, and identify it as the optional consequence of F56.

## RR9-205 — Appendix F. Execution history

**low · navigation · lines 5973–5973 · U04542**

> The passages below keep every earlier receipt, packet label and run traceable.

The execution history retains many exact receipts, aliases and file counts in prose. Comparing two observations requires repeatedly recovering their snapshot, closure and checking mode.

**Reader cost.** A count or accepted target from one snapshot must not be silently combined with the dependency route of another.

**Repair.** Add one snapshot index with date, source/closure identity, target list, counts with their denominators, and the current destination. Use the same readable labels in F and G, preserving full hashes and byte-equivalence limits in the receipts.

## RR9-206 — Appendix F. Execution history

**medium · structure · lines 5973–5973 · U04542**

> The passages below keep every earlier receipt, packet label and run traceable.

The publication-order reader reaches the full execution history before the current statement inventory, even though line 5973 does provide a direct current-status link.

**Reader cost.** A reader seeking the present theorem must cross four pages of historical qualifications to reach the current check.

**Repair.** Put the current status inventory before the historical narrative, or make the history an explicitly separate archival part. The current link exists; this is an ordering proposal.

## RR9-207 — F.1. The 2 November receipts and the earlier frozen packet

**medium · evidence_presentation · lines 5985–5985 · U04561**

> The deliberate [missing-equality]

Three controls with different desired outcomes are narrated in one paragraph, including an intentionally accepted bad shared specification.

**Reader cost.** Accepted and rejected can look like a single pass/fail axis even though success means different things for these controls.

**Repair.** Present a compact control/outcome/meaning comparison, separating syntactic mismatch detection from shared-specification blindness.

## RR9-208 — F.1. The 2 November receipts and the earlier frozen packet

**low · prerequisite · lines 5989–5989 · U04576**

> Dependency reach is a further question about particular proof roots

Dependency reach is introduced after several status counts without a concrete example.

**Reader cost.** A reader unfamiliar with formal developments may interpret reach as another form of validation.

**Repair.** Use one already named target to show built-but-not-used versus used-by-this-root, and link the exhaustive graph.

## RR9-209 — F.3. Addressed construction

**low · evidence_presentation · lines 6012–6012 · U04611**

> Audit membership is recorded name by name

The sentence states a policy but supplies no direct target-list destination at that point.

**Reader cost.** A reader following one local-test declaration must search a long sidecar to apply the policy.

**Repair.** Link the subject-specific membership subsection or JSON pointer alongside the statement.

## RR9-210 — F.6. Exponent and Appendix A

**low · structure · lines 6042–6042 · U04641**

> An earlier annex transcription put an extra square root

A transcription-history note opens the exponent/Appendix A section before the section gives its evidence task.

**Reader cost.** The reader must process an old typo and a separate source discrepancy before learning what is now checked.

**Repair.** Lead with the current endpoint and move this episode beside the exact source-discrepancy comparison.

## RR9-211 — F.7. Earlier drafts

**low · funnel · lines 6056–6056 · U04662**

> The earlier [short expert draft]

The paragraph correctly labels its links as earlier advisory drafts, but it does not provide direct adjacent links to the current companions.

**Reader cost.** A reader can accidentally enter an obsolete account during a present verification task.

**Repair.** Add current-companion destinations beside the archive links or in the common edition index; preserve the existing archived-edition labels.

## RR9-212 — Appendix G. Formal statements and evidence

**medium · first_encounter · lines 6061–6061 · U04668**

> Its four headline statements are written in a separate statement file

The appendix opening introduces four statements and a comparison without offering the statement-file link until later.

**Reader cost.** The declared concrete object is not immediately inspectable at the point where the reader is invited to assess it.

**Repair.** Link the statement file and name the four compared mathematical targets at the appendix entry; follow with their common specification/solution architecture and dated receipt details. The architecture is present later; this is an ordering repair.

## RR9-213 — G.1. Checking one statement

**medium · prerequisite · lines 6068–6068 · U04675**

> Its quantifiers run $\forall k\ \exists S,A,b,t_0\ \forall t\ \exists\mathcal C$

The audit compresses the circuit-size constant, query constant, exponent and threshold into unglossed letters.

**Reader cost.** A non-Lean mathematician cannot compare the exact type with c_k,C_k,b_k,m_0(k) in Theorem 1.1.

**Repair.** Give a short mathematical dictionary: formal S is the circuit-size coefficient in C.size≤S·m·(2t)^2, A is the query coefficient, b the logarithmic exponent, and t_0 the dyadic size threshold. Distinguish this coefficient S from earlier actual gate-count notation.

## RR9-214 — G.1. Checking one statement

**medium · error · lines 6069–6069 · U04677**

> The read-all witnesses of §2.2

This local locator omits the quantum read-all witness, which is constructed in §2.4, not §2.2.

**Reader cost.** The proposed verification route sends readers to a passage that does not justify Q being the minimum of a nonempty set.

**Repair.** Point to §2.2 for D and R and §2.4 for Q, preferably directly to their read-all arguments.

**Later resolution / qualification:** {"line_start": 293, "line_end": 301, "note": "The Q read-all simulation and nonempty minimum appear here."}

## RR9-215 — G.1. Checking one statement

**low · funnel · lines 6072–6072 · U04680**

> Read the statement's paragraph in Appendix G.4.

The fifth step names a long section rather than the specific separation-family paragraph.

**Reader cost.** The bounded audit task ends with another scan instead of a definite check.

**Repair.** Link directly to the separation-family status paragraph and state the two facts the reader should confirm there.

## RR9-216 — G.2. What the formal models establish

**medium · transition · lines 6081–6081 · U04689**

> The source provides a concrete compilation argument behind this accounting.

This accounting has no clear immediate antecedent after the paragraph on totalisation.

**Reader cost.** The reader enters a two-query compiler without knowing which cost or representation is being transported.

**Repair.** Identify the abstract-read to physical-bit-query problem before describing the compiler and link its source contract at the first sentence.

## RR9-217 — G.2. What the formal models establish

**medium · evidence_presentation · lines 6090–6090 · U04699**

> **Ordinary identifications.**

The list places seed reduction, cap-count identification and a general-projector reduction in one category although their relation to the headline proof differs.

**Reader cost.** Readers may infer that every unformalized identification is an unproved assumption of the final theorem.

**Repair.** Add a second axis saying used for headline interpretation, alternative proof comparison or stronger unused state specification.

## RR9-218 — G.2. What the formal models establish

**low · structure · lines 6094–6094 · U04707**

> Complete source signatures, including the circuit and workspace quantifiers

After the explicit three-part model map, this paragraph returns to general audit instructions and sidecars before continuing the object comparison.

**Reader cost.** The reader repeatedly restarts the same verification task.

**Repair.** Keep the model comparison contiguous and collect the sidecar-access instruction once at the end of G.1 or G.2.

## RR9-219 — G.2. What the formal models establish

**low · structure · lines 6096–6096 · U04708**

> **The partial function and its domain.**

The partial-function encoding and totalisation are explained again only a few paragraphs after line 6079.

**Reader cost.** The audit grows without adding a new semantic comparison.

**Repair.** Consolidate the two treatments and retain the extra distinctions about the total-function endpoint in the single version.

## RR9-220 — G.3. Execution evidence and checks of meaning

**medium · prose · lines 6150–6150 · U04770**

> `current_catalogue_snapshot.rows`

Implementation keys dominate the first paragraph of the evidence-reading section.

**Reader cost.** A mathematical reader has to parse a JSON schema before understanding the distinction between maintained observations and frozen review.

**Repair.** Explain that distinction in ordinary terms and move the exact JSON pointers into one compact access note.

## RR9-221 — G.3. Execution evidence and checks of meaning

**low · example · lines 6160–6160 · U04794**

> A concrete fair comparison matrix also witnesses

The semantic test is described without its tiny matrix.

**Reader cost.** The reader cannot perform the stated nonemptiness check without a code detour, although the entire example is small.

**Repair.** Display or precisely link the actual finite matrix and the predicate it satisfies; retain the limited semantic conclusion.

## RR9-222 — G.4. The compared statements

**medium · evidence_presentation · lines 6168–6168 · U04805**

> ### G.4. The compared statements

The heading describes the section as compared statements although its later entries include built-only and ordinary-only endpoints. Those individual statuses are already qualified in the prose.

**Reader cost.** A scanning reader can overstate formal coverage even though individual paragraphs contain qualifications.

**Repair.** Rename the section around central statements and their status, and use a compact inventory separating configured comparison, build, headline use and ordinary proof. Keep explanation for exceptional scope differences.

## RR9-223 — G.4. The compared statements

**low · evidence_presentation · lines 6170–6170 · U04809**

> a [later paranoid run the same day]

The prose reports paranoid external checking but leaves the recorded unsandboxed execution mode to the linked receipt. It does not falsely claim isolation.

**Reader cost.** A reader auditing the recorded procedure must open the receipt to distinguish checker selection from execution mode.

**Repair.** If the run is summarized in prose, include its actual unsandboxed local mode beside the dated result, with the exact command retained in the receipt. This is provenance detail, not a reason to reject the theorem or rerun the check.

## RR9-224 — G.4. The compared statements

**high · error · lines 6188–6188 · U04828**

> Lean links are pinned to commit `d234866`

The current file's Lean reference definitions use b8db5326715e5a4ce6996cde0768b92b5fcd5177, not d234866.

**Reader cost.** The human-facing edition statement disagrees with the actual destinations, undermining a reader's attempt to bind prose and evidence.

**Repair.** Update the stated pin to the actual link edition and separately document any verified source-byte equivalence to the receipt edition; do not infer equivalence from the labels.

**Later resolution / qualification:** {"line_start": 6461, "line_end": 6586, "note": "The actual pinned Lean links are all in the b8db532... revision."}

## RR9-225 — G.4. The compared statements

**medium · evidence_presentation · lines 6188–6188 · U04829**

> The statement files of the Unconditional and Construction bundles import only Mathlib.

Different trust boundaries of the statement bundles are compressed into the same paragraph as family quantifiers and source pins.

**Reader cost.** Readers cannot compare which specifications are independently written and which import the implementation vocabulary.

**Repair.** Move the bundle/import comparison to a compact separate table, retaining the exact named imports and avoiding an undifferentiated independence label.

## RR9-226 — G.4. The compared statements

**medium · evidence_presentation · lines 6192–6192 · U04834**

> The 2 November corpus and the 3 November textual review

Dates and review labels are repeated for many entries before their definitions appear at the end of G.4.

**Reader cost.** Readers have to treat the classifications as unexplained authorities for several pages.

**Repair.** Define the two review sources, dates and scopes before the first entry that uses them.

**Later resolution / qualification:** {"line_start": 6266, "line_end": 6266, "note": "The two provenance categories are defined here."}

## RR9-227 — G.5. Forrelation

**low · evidence_presentation · lines 6277–6277 · U04936**

> the source's retained-isometry theorem asserts no equality with that display

The phrase that display refers back to a tensor-state equality in a distant section without giving its exact display label or link.

**Reader cost.** The reader must search the decoder section to recover the precise represented state; the current paragraph already identifies the kind of equality at issue.

**Repair.** Link the exact tensor-state display at this reference, preserving the stated distinction between ordinary state equality and the formal instantiated interface.

## RR9-228 — G.7. The quantum upper bound

**low · prose · lines 6315–6315 · U04996**

> Thus the older Boolean-only description does not describe this packet's available list theorem.

A correction of an older description interrupts the current account of the tensor-stage and list contracts.

**Reader cost.** Readers without the older return must process an editorial dispute unrelated to reconstructing the present theorem.

**Repair.** Move the old-description correction to F and leave the current list contract here.

## RR9-229 — G.7. The quantum upper bound

**low · prerequisite · lines 6327–6327 · U05015**

> a finite auxiliary register $J$

J is introduced as a register but later contains a vector xi_x and enters a tensor product of Hilbert spaces.

**Reader cost.** The same symbol can mean a finite index set or its Hilbert space, affecting the type of the displayed factorization.

**Repair.** Distinguish the finite basis-label set from its Hilbert space, or explicitly declare J to denote the auxiliary Hilbert space.

## RR9-230 — G.7. The quantum upper bound

**medium · first_encounter · lines 6345–6345 · U05021**

> a logical-read circuit cap $qN(2M+1)$

The quantities M and N are used in the local specification without being recalled there.

**Reader cost.** A reader arriving at this direct evidence destination cannot check the uniform cap without leaving the appendix.

**Repair.** Recall the definitions and parameter dependence of M and N or provide a direct exact link beside the cap.

## RR9-231 — G.8. The classical lower bound

**low · prerequisite · lines 6375–6379 · U05048**

> the number of queries that path makes to each instance

The ordinary induction identifying recursive compliance with path counts is present, but embedded inside a dense evidence-status paragraph.

**Reader cost.** The reader checking whether the formal cap event is the printed event cannot isolate the actual transport.

**Repair.** Separate the existing short ordinary induction into clearly marked base and query cases, identify its endpoint as recursive compliance versus observable counts, and keep the no-Lean-status statement separate. Do not propose a new formal theorem.

## RR9-232 — G.8. The classical lower bound

**low · prose · lines 6390–6390 · U05056**

> NCL-checked-gap in the baseline

An unexplained historical ledger label occurs in the first sentence of the planted-lower-bound status subsection.

**Reader cost.** Readers must locate an old baseline to identify the current one-sided theorem being compared.

**Repair.** Use the mathematical name in prose and move the historical identifier behind a link or into F.

## RR9-233 — G.8. The classical lower bound

**medium · structure · lines 6394–6394 · U05063**

> The older [erased-zero bound]

Several identities, two complete conjunctions, an old bound and their evidence statuses are introduced in one long paragraph.

**Reader cost.** The reader must reconstruct the difference between algebraic equivalence and separately checked declarations before seeing the displays.

**Repair.** Lead with the two displayed conjunctions, identify their ordinary equivalence, then give each declaration and evidence status alongside it.

## RR9-234 — G.8. The classical lower bound

**medium · evidence_presentation · lines 6407–6407 · U05077**

> It still shares the project's coordinate, query-tree, path and depth interfaces

The independence boundary arrives near the end of a long positive description of the independently written experiment.

**Reader cost.** An early scan can overstate what was independently specified.

**Repair.** State the shared interfaces immediately after naming the independent specification, then explain the separately written law and observables.

## RR9-235 — G.8. The classical lower bound

**low · prerequisite · lines 6411–6411 · U05088**

> Prose query time $q$ corresponds to the source's zero-based index $q-1$.

The time-index conversion is buried among endpoint and tail-bound status statements.

**Reader cost.** This is the exact off-by-one identification needed to compare a particular fixed-time event.

**Repair.** Place the conversion beside the fixed-time joint-event entry in G.4 and link the event definitions.

## RR9-236 — G.9. The exponent and Appendix A

**medium · structure · lines 6434–6434 · U05117**

> Three separate formal bounds are present in the supplied source.

The most useful comparison of the three quartic routes appears very late in the audit.

**Reader cost.** Readers of Appendix A or the early model bridge must retain uncertainty about which proof and constant the headline uses for dozens of pages.

**Repair.** Add a short forward-linked route declaration at Appendix A and the model bridge, preserving the full comparison here.

## RR9-237 — Use of AI tools

**medium · chronology · lines 6458–6458 · U05147**

> AI agents wrote the Lean formalization, the explanatory additions and the text of this record

The complete disclosure that AI agents wrote the formalization, additions and record appears at the end. Earlier no-human-review statements do not fully identify who authored and assessed the material.

**Reader cost.** Readers should encounter the provenance before interpreting the manuscript’s formal and review claims.

**Repair.** Provide a brief early authorship and review-status disclosure linked to the full final account; consolidate repeated wording while preserving distinctions of scope.
