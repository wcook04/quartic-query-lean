# Review notes

## Conclusion and the strength of this reading

The supplied endpoint is unconditional: `QuarticQuery.alphaTot_eq_four_unconditional : alphaTot = 4`, and `QuarticQuery.theorem_1_1_unconditional` includes the universal upper bound and the fixed-parameter family. The formerly assumed proposition `BansalSinhaLower` is proved by `QuarticQuery.ForrelationLower.bansalSinhaLower`. The earlier conditional files remain in the dependency chain as reusable implications. Their existence does not make the final theorem conditional.

The mathematical reconstruction did not reveal a fatal error in the separation argument. The issues below concern the exact meaning of individual statements, mismatched evidence labels, proof routes, source locators, and the limits of the available verification. This conclusion is a source reading and mathematical reconstruction. It is not a new kernel certification or a human review.

## What was independently checked for this return

The source archive was extracted locally and its 157 manifest-listed members were checked against their SHA-256 hashes, with no mismatch. The manifest pins repository revision `c7e0c9161f0ad898889bd9166e7b354acd42188d` and the OpenAI paper source `openai/math 4eaee875`. The supplied paper is 19 pages and has SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.

The current definitions, proof modules, unconditional assembly, comparator solutions, comparator configurations, negative-control sources, and dependency extractor were inspected. The shared definition block in each of the five challenge files was independently compared with `Statement.lean` after removing comments and normalizing whitespace; every block matched. This is a source-text equality check. It does not rerun Comparator or establish compiled definitional equality by itself.

A comment-stripped search of the production directory `lean/QuarticQuery/` found no `sorry`, `admit`, `axiom`, or `native_decide` token. The challenge files deliberately contain placeholder proofs, and the negative-control directory deliberately contains a foreign axiom and a sorry proof. These files are distinct from the production proof directory, so their expected contents must not be treated as defects in the proved result. Equally, a source-text search cannot replace a kernel axiom report.

The supplied dependency extraction names `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional` as its roots. It reports 2,021 project declarations and a reached set of 1,319 project declarations. The extraction script follows compiled declaration types and bodies, including internal auxiliary dependencies. These numbers describe the supplied extraction, not a newly generated environment. Full declaration names in the returned correspondence are checked against that declared-name inventory.

The proof reconstructions include the complete fixed-k Gaussian argument, the weighted direct-product induction, finite minimax, the dummy/planted coupling, both zero-search estimates, uniform bounded amplification, probabilistic tournament and its Boolean continuation, bit-oracle compilation, all floor arithmetic, the exponent comparison, and every Appendix A lemma. The root reading checked the completed mathematical sections after delegation, including the conditioning restrictions and the optional new zero-search refinement. A separate reviewer then read the root model, exponent and Appendix A proofs, finding no substantive proof error. The wording was tightened to distinguish separate inputs from probabilistic independence, to retain the nonnegative exponent restriction, and to say that a query budget is an upper cap. Every original corpus row is reproduced in the final statement catalogue and mapped to its proof or definition passages.

The final artifact checks include exact preservation of all original corpus quotations, literal passage locators, claim registration, declared-name checks, valid statement dependencies, and parsed bibliography entries. A separate syntax pass extracted every mathematical expression with Pandoc and processed it with XeLaTeX without an error. That checks notation syntax only. It neither proves the displayed mathematics nor elaborates any Lean proposal. The detailed results are in `validation.json`.

An independent static review also checked all proposed Lean signatures against the source vocabulary and section contexts. It found that the advertised Forrelation import context omitted the arithmetic-circuit and sanity modules; the proposals now explicitly include `QuarticQuery.Forrelation.Circuit` and `QuarticQuery.Forrelation.Sanity`. No further clear missing binder, unavailable name or namespace mismatch was found. This is still a source comparison, and every new signature remains uncompiled.

## Verification not rerun

Neither `lean` nor `lake` is installed in the available local environment. The packet does not include its `.olean` build tree, dependency checkouts, `corpus/receipts/` directory, the comparator runner, or the repository's Python generation and test tools. No fresh `lake build`, `#print axioms`, Comparator run, external-kernel run, or negative-control execution was performed for this return.

The pinned toolchain is `leanprover/lean4:v4.36.0-rc2`. The Lake manifest pins complexitylib to `62ca5c21461b2482e8bd12b7cb9b4937d887a33a`, cslib to `254e30e6d4299c51323aaeaf5f51a4763b375d4a`, and Mathlib to `69552756cd8a2d2d48763cf7279fd814d6a1224d`. The complexitylib adversary source could not be retrieved through the available public fetch route. The imported quartic theorem is therefore identified from its explicit use in `Appendix/TheoremA1.lean` and the supplied source record, with an independent ordinary proof of the mathematical endpoint included in this return.

The attached historical execution trace reports a successful full build, five accepted comparison bundles, external-kernel acceptance for the unconditional bundle, and five rejected negative controls. The final progress entries are N064, N068 and N069, with N069 timestamp `2026-11-02T07:29:09.635Z`. These are historical reported runs. The trace also records older partial states, deferred builds and a watcher-shell failure; its latest state must be read against the current source. The raw receipt files named by those reports are absent from this packet. The final record consistently distinguishes these reports from checks executed during this reconstruction.

## Findings requiring an evidence or wording correction

### 1. The numerical Bansal–Sinha comparison is not the theorem cited as its formal witness

For `claim-bs-to-L`, the corpus ties `QuarticQuery.ForrelationLower.bansalSinhaLower` as an exact alternative-route witness. That theorem concludes `Lvalue k t < R (P k t)` eventually. It does not state that a particular expression involving the published constant and `k^-29` exceeds `Lvalue`. The latter numerical comparison has a complete proof in the record, using positivity of the published constant and the growing power of the logarithm. Its current exact formal tie should be removed or replaced by a theorem stating that comparison. The same endpoint theorem is an appropriate alternative-route witness for `lem-2.1.i`.

The tie's file and kind also need correction: `bansalSinhaLower` is a theorem in `ForrelationLower/Main.lean`, not a definition in `Statement.lean`. The latter contains the proposition `BansalSinhaLower`.

### 2. Older reviews describe a superseded conditional state

`docs/statement_fidelity_review.md` records its second pass at `efc70f3`. Its claims that the headline remains conditional, its tie counts, and its comments that comparison evidence has not reached the generated rows do not describe the final pin. The earlier intake and adjudication documents also say the Forrelation lower bound was not reproved. Those remarks were accurate for their historical stage. The current unconditional source, its internal lower-bound modules, and current corpus supersede them. The final record retains their useful mathematical observations without importing their stale completion status.

### 3. Proposition 3.2's list output remains only partially matched

The ordinary theorem returns a candidate list. `QuarticQuery.Upper.tournament_runs` produces a Boolean continuation that consumes candidates through a verifier and includes that verifier's error in its acceptance guarantee. This is sufficient for the final upper bound. It is not literally the list-valued statement with its original error term. The corpus's partial classification should remain. The record proves both the list coupling and the actual continuation induction, explaining the relationship explicitly.

### 4. A checked one-sided discrepancy does not certify an absolute value

`QuarticQuery.tree_gap_le` bounds planted acceptance minus dummy acceptance, with the improved term `2G/m^2`. The corpus equation (23) is an absolute-value estimate, and equation (18) also uses an absolute value. The first-difference argument proves the absolute-value form in prose, but the exported one-sided theorem should not be relabeled an exact witness for it. The one-sided form already suffices for the randomized contradiction.

### 5. The sharper zero-search constant has an expected-cost sharpness statement

The checked induction proves the erased-zero estimate `2G/m^2`. The record supplies an additional prose proof of `2G/[m(m+1)]`, via the common all-one reference path for each column. This is registered separately in `NEW_STATEMENTS.json` and is unnecessary for the separation theorem.

Scanning a single column until its zero appears has expected cost `(m+1)/2` and one discovery. It attains the underlying expected-cost inequality and shows that the coefficient two in its coarser `m`-denominator version is asymptotically sharp. Its worst-case cost is `m`. It therefore does not establish sharpness for every fixed worst-case total query budget. The scan example in finding 5 of the earlier fidelity review should be qualified this way.

### 6. The universal upper bound has an alternative formal proof

`Appendix/TheoremA1.lean` explicitly imports the complexitylib theorem `Cslib.Quantum.complexity_le_mul_pow_four`, after bridging the adaptive model to a fixed query sequence and deterministic trees. It proves the endpoint with constant `20736`. It does not prove the preprint's Lemmas A.2–A.5 in their displayed forms. In particular, `FixedSim.build` and `exists_fixedSequence` prove deferral, which is only one step of Lemma A.2. The record proves the spectral adversary argument, the star and matching bounds, the signed-cube argument and the maximum-monomial algorithm fully in prose and marks their evidence accordingly. The numerical constant in that reconstructed proof is not identified with `20736`.

### 7. Definitional and helper omissions in the corpus are not missing mathematics by themselves

Several original rows have no reviewed tie even though relevant definitions or theorems occur in the source. Examples include `alphaTot` and `UniversalPower`, `Lvalue`, `Gvalue`, the exact tournament drift, winner uniqueness, and the local-test dichotomy. The record adds source correspondences while preserving their original evidence fields. A new source correspondence does not amount to a new build or comparison receipt.

The current coverage file also lists `claim-butterfly` and `def-P` as source ledger tags without matching rows. The new intermediate-claim registry supplies the butterfly recurrence with its own identifier and points to the exact promise definitions; it does not silently add invented rows to the original corpus.

### 8. The literal circuit-size and quantum-cost claims need component-level care

`abs_numerator_le` bounds the final integer numerator. It does not by itself prove the preprint's whole claim about the size of every intermediate integer and the final circuit. The record proves the butterfly arithmetic and gate accounting, and distinguishes the source's residue implementation from the direct signed-integer explanation.

The simple phase-kickback Forrelation trial uses one bit query per sign layer. The supplied general compiler charges two ordinary bit queries per abstract read. These implementations establish the same asymptotic promise-query estimate but different literal finite caps. Stronger explicit displays are registered separately; they are not presented as the literal output of a theorem with a larger certified cap.

### 9. Theorem numbering in text extractions is unreliable

The local flattened extraction of Aaronson–Ben-David–Kothari–Rao–Tal renumbers results and drops mathematical identifiers. The official arXiv PDF has Theorem 1 for `deg(f) <= lambda(f)^2`, Theorem 2 for the quartic universal upper bound, Definition 7 for spectral sensitivity, and Lemma 9 for its quantum lower bound. Conjecture 2 is in Section 7 on printed page 20. These locators were checked against the PDF.

Likewise, the Bansal–Sinha PDF's relevant results are Theorem 1.3 and Corollary 1.4, even when a flattened local extraction changes their labels. Midrijānis's product bound is inside the proof of Theorem 4, supported by Lemma 3; Theorem 4 itself states a cubic degree bound. Citations in the record use these precise locations.

### 10. Prior-art and quantifier boundaries

The internal lower-bound route uses correlated Gaussians, truncation, biased product measures, integration by parts and decision-tree Fourier growth. The biased tree-growth argument has a clear precedent in Girish–Tal–Wu's martingale and contraction method. Bansal–Sinha prove a stronger quantitative lower bound by a different interpolation route. The fact that the packet's search did not locate the exact first-block reflection-and-elimination identity establishes only a search result. This record makes no historical novelty claim and no unproved improved dependence on `k`.

The family parameter `k` is fixed before the input dimension grows. Constants and thresholds may depend on it. Each family supplies exponent `4-2/k`, and the full collection excludes every universal exponent below four. No argument here claims a single fixed family with an exact fourth-power lower bound. The same circuit witness is used for each member's quantum upper and randomized lower estimates.

## Reading coverage and unavailable material

The detailed per-section reading lists from the three mathematical reviews are included below, and the machine-readable source receipt gives their exact paths. All current production proof modules relevant to the theorem were assigned and read; the root additionally read the model definitions, final assembly and exponent arithmetic, Appendix endpoint, original statement rows for these parts, current comparator wrappers/configurations and dependency extractor. The paper's mathematical content was read across Sections 1–5 and Appendix A, using the supplied extraction and checking ambiguous formulas against the PDF. The four supplied writing guides were read. They are form guidance, not mathematical authority for this theorem.

The attached 125,744-line execution trace was used as a historical source: its complete root visible-progress section and the latest task state were read, with targeted searches in the surrounding prompt/build record. Its twenty embedded child traces were not independently read line by line. All text of the three unrelated SK/QAOA exemplars was read for structure and writing conventions: the long record, lines 1–5659; the short paper, lines 1–1149; and the expository paper, lines 1–1514. This includes their Markdown and figure-source code. Their figures were not rendered and their mathematics was not independently audited. The resulting form checks led to an explicit numbering convention and a unified clickable citation system. Unused literature papers in the packet were inventoried; no assertion of complete reading of every background bibliography item is made. Proof-bearing sources actually used are identified in the section receipts and bibliography.

Original full texts that were unavailable or not independently opened are identified explicitly in their bibliographic notes, including Barnum–Saks–Szegedy and the original Yao paper where applicable. The general minimax and adversary results needed here have complete ordinary proofs in the manuscript. The missing private repository tooling, raw verification receipts, external dependency checkout and old temporary scripts cannot be reconstructed from the supplied packet. This return neither substitutes invented files for them nor treats their absence as evidence of a mathematical failure.

## Handoff

The source repository and original corpus were left unchanged. `STATEMENT_CHANGES.json` records changed mathematical formulations; evidence-label repairs are recorded here and in `LEAN_GAPS.md`. `NEW_STATEMENTS.json` contains explicit proposed signatures for additional displayed claims. These are proposals using the supplied vocabulary and inspected helper declarations, not newly compiled theorems. A later formal pass should prioritize the literal claim-to-theorem mismatches and the new erased-zero refinement before presenting those particular statements as kernel checked.


## Supplement: Forrelation source review

# Forrelation review notes

## Scope and verification

This review covers paper Section 2.1, all eight Forrelation modules, all eight ForrelationLower modules, the lower-bound blueprint, independent reading and prior-art memorandum, the assigned corpus rows, and the relevant portions of the cited primary literature. The supplied commit is c7e0c9161f0ad898889bd9166e7b354acd42188d. Source reading and mathematical reconstruction were performed. No Lean or comparator run was performed; no included file supplies the build receipts named by the README. Parent integration also reports that Lean/lake are absent locally.

The reconstruction now proves the full fixed-k argument in ordinary mathematics, including finite product weights, centered derivative characters, bounded truncation, Gaussian integration by parts, reflection clearing, the exact block walk, finite leaf weights, stopped degree growth, the hard and uniform moments, 2tau-run amplification, and an explicit threshold. It also reconstructs the coherent quantum test and exact Boolean arithmetic circuit.

## Material finding: endpoint evidence was attached to an intermediate inequality

Location: corpus/statements.json, claim-bs-to-L.

The row asserts an asymptotic numerical inequality comparing the published Bansal–Sinha scale with L. Its sole listed declaration is QuarticQuery.ForrelationLower.bansalSinhaLower, marked exact/alternative. That theorem states BansalSinhaLower, namely for each k>=2, eventually Lvalue k t < R(P k t). It has no numerical expression involving c or k^-29 and does not use the published theorem. An alternative proof of the endpoint does not establish that separate inequality. The corpus tie should be removed from the comparison row and retained on lem-2.1.i. The comparison is correct for c>0 and fixed k>=2, and the draft supplies its full elementary proof.

The comparison row should explicitly require c>0. Without positivity, it is false, for example at c=0 and eventually positive L. This is a statement clarification justified by the constant's original lower-bound role, not a change to the intended imported theorem.

## Metadata correction

Both claim-bs-to-L and lem-2.1.i list the declaration kind as definition and its file as Statement.lean. The actual declaration is a theorem in lean/QuarticQuery/ForrelationLower/Main.lean, line 506 in this packet. Statement.lean defines the proposition BansalSinhaLower; it does not contain its proof.

## Circuit evidence boundary

The sole tie on claim-circuit-size, abs_numerator_le, bounds the final numerator only. It does not establish the claimed magnitude bound for all arithmetic intermediates. The prose reconstruction supplies an elementary m^k bound for direct arithmetic and separately describes the source's residue implementation. The latter uses width 5k+3+t(k+1) and only the final |N|<=M bound to interpret the three sign tests. This is mathematically sound and avoids signed-range invariants at every intermediate stage.

The claim-butterfly identifier appears in Circuit.lean comments but is absent from the corpus. NEW-FOR-03 registers the actual identity. The explicit circuit constant and wider k>=1,t>=1 range are now NEW-FOR-29; the original asymptotic row remains unchanged.

## Quantum evidence boundary

The projection probability and binomial tail calculations have exact component proofs. The source's abstract sampler has k reads; its general compiler yields 2k bit queries. One-query phase kickback is mathematically valid and proves a sharper implementation, but Upper.P_runs is not an exact witness for that count. NEW-FOR-28 records the sharper explicit cap as a prose proof and an uncompiled proposed signature. A second signature packages a coherent Samples law with correctness at qk abstract reads, while preserving the distinction between an abstract read and its general bit-oracle compilation. The corpus lemma's O_k count is supported by either cap.

## Lower-bound document corrections

1. The blueprint's last status section says the root does not yet import the development and that an independent reading is outstanding. The later README, actual imports and supplied independent review supersede that working status. Preserve its date/status context rather than treating it as a present blockage.
2. The blueprint mentions stronger analytic bounds on Psi and phi'. They are mathematically true, but the actual imported advantage proof uses the coarse source bounds Psi<=1 and phi'<=3. The reconstruction consistently retains the factor 3^(k-1).
3. Amplification is 2tau independent runs, with depth 2tau L and error (8/9)^tau, as exists_amplified states. Writing merely tau runs with the same numerical exponent loses a factor.
4. exists_identity is a mean-value statement with one s in (0,1). The independent review writes a time-integrated identity, which is also derivable but is not the exact statement of that declaration. The reconstruction follows the actual mean-value route.
5. Int_eq_paths is in Walk.lean, not Cascade.lean. The advantage bound, reflection clearing, and path-set injectivity are in Cascade.lean.
6. The independent review suggests stronger quantitative k-dependence and possible sharper use of the SSW Fourier bound. Those hand derivations are not frozen endpoints in this packet and are not promoted in this record.

## Primary-source checks and attribution

The original Bansal–Sinha arXiv PDF uses Theorem 1.3 and Corollary 1.4 for the main lower bound and bounded-error corollary. These locators match the preprint. The local Markdown extraction flattens restatable environments and calls the bounded-error result Corollary 3; that extracted number should not be copied as an original locator. The checked bound has the k^-29 factor, threshold 2^-5k, and matrix block dimension N corresponding to this record's m.

The decision-tree martingale/contraction argument is identifiable prior art in Girish–Tal–Wu, Section 1.3 and Lemma 1.9. Bansal–Sinha Section 5.3 transfers Fourier growth to biased measures by random restrictions. SSW prove a sharper uniform Fourier theorem. The record attributes those mechanisms and does not claim a new general Fourier theorem.

The exact first-block reflection-and-elimination proof differs from the displayed proofs inspected in these sources. Neither the packet's unsuccessful novelty search nor this limited check establishes that the route is historically new. The bibliography includes only real primary works with checked identifiers. No public URL is invented for the private source snapshot.

## Mathematical checks

The reconstructed proof explicitly checks the following potential failure points:

- No independence between U and HU is assumed.
- Reflection changes earlier X factors only in blocks already cleared.
- Each Stein differentiation hits only its current and next block; the current contribution vanishes by the repeated discrete derivative.
- Earlier analytic weights are independent of the currently differentiated Gaussian layer.
- The path family is injective as subsets because it selects exactly one coordinate per block.
- The derivative-growth estimate is uniform in biased means, so higher uniform Fourier levels remain accounted for.
- Repeated queries reuse their known answers and contribute no fresh product probability.
- The tree stopping argument uses bounded finite depth, with bad-coefficient events included.
- The hard distribution need not satisfy the promise; correctness is applied through all-input envelopes.
- The exact floor is bounded in the needed direction, and the threshold applies to all sufficiently large powers of four.
- m=1 is outside the displayed asymptotic formulas; the circuit size statement requires t>=1.
- A full hand count at k=2,m=4 matches the source census and its negative witness.

The mathematical source argument appears coherent on this reading. This is an AI source review, not an independent human review or a replayed kernel verification.


## Supplement: Construction and classical source review

# Construction and classical lower bound: review

## Outcome

The reconstruction covers all 45 assigned corpus rows in 36 anchored passages and includes 10 separately registered intermediate statements. All original corpus statements are retained; stronger displayed forms have distinct NCL identifiers. STATEMENT_CHANGES is empty. The main text is approximately 7,800 words before integration.

No source edit, Lean build, kernel replay, or comparator run was performed. The record reconstructs proofs from the supplied source. The parent owns the final evidence summary and artifact persistence.

## Mathematical review

1. The same circuit determines the function used by both bounds. Its correctness is needed for the output-test bridge; its size is irrelevant to the generic classical lower bound. The semantic WinsAt primitive and the raw local output-test description are equivalent under CircuitRealises. This bridge is distinguished from winsAt_iff_paperWinsAt.

2. Gate consistency implies actual evaluation by topological induction, on and off the promise. Both output gates are non-input gates and have transcript entries. Input bits are read from the actual input.

3. The test index set is fixed independently of the candidate and address. Pointer tests have small adaptive depth and potentially large support. The coherent procedure retains and uncomputes history. Support size is never used as a substitute for query depth.

4. The original direct-product proof supplies every conditional-probability row. The source's stronger weighted induction changes one nonnegative weight and one cap and factors out the unchanged optimal values. It needs no normalization. Arbitrary independent side information is reduced to a finite mixture of induced trees; the finite-tree helper is registered as prose-only.

5. The finite minimax proof is complete: the compact convex hull of success vectors is disjoint from an upper orthant; a closest pair gives a nonnegative separating normal and a distribution on the promised inputs. Differentiating squared distance along each segment gives the payoff inequality. A positive uniform margin is obtained and registered separately. The source theorem itself is only attributed the weak ≤2/3 endpoint.

6. The coupling changes only the erased zero and selected cell. A first differing answer must occur on the dummy path before outputs can differ. Absolute indicator difference is bounded by this event. The exact source discrepancy theorem is one-sided and is described accordingly.

7. The coefficient-two zero-search induction allows arbitrary subsets of possible positions. At a candidate position p, world p discovers its zero and pays at least one query; all other worlds pay a query before the same answer-one subtree. Repeated and post-discovery queries are retained in the costs.

8. The optional m(m+1) denominator compares every zero-world with the all-one reference path. If this path visits d distinct positions, exactly d worlds discover the zero and their total cost is at least 1+...+d+(m-d)d. Repetitions and later queries add cost; before the first zero the complete histories coincide even with adaptive outside queries. Conditioning on fixed outside data preserves the independent uniform zero. This refinement is prose-only, unnecessary for the main result, and carries no novelty claim.

9. Scanning to the zero has expected cost (m+1)/2 and worst-case cost m. It witnesses asymptotic sharpness of coefficient two in an expected-cost inequality. It does not establish a universally optimal fixed-depth distinguishing bound. This qualifies finding 5 of repository/docs/statement_fidelity_review.md and the corresponding historical trace remarks.

10. The simulator receives outside-target data only, aborts before the (L+1)-st total target query, and identifies the proposed cell address without reading its bit. The cap holds on every branch. Nonheaviness of the entire original run implies faithfulness up to the proposed query. The probability bound is on a joint event, not a conditional input law.

11. The discrepancy estimate uses exactly 1≤L≤m and G≤mL/100. The finite inequality 4/9≤1/2 gives the tail used in the source. The preprint's real-logarithm exponent is also proved. Averaging deterministic-tree gaps conflicts with the pointwise bounded-error requirements on the coupled zero and one inputs.

12. The nested floors cost at most a factor four when t≥8, yielding constant 1/400 uniformly in k≥2. The threshold for L<R(P) alone may depend on k. The concrete theorem still uses the same circuit as the upper bound.

## Attribution decisions

Drucker is cited at §1.3, Lemmas 3.1–3.2, and the final paragraph of §3, verified in arXiv:1005.0644v2. The global-budget Theorem 1.1 is not substituted for the capped statement. Shaltiel §5 Theorem 5 is identified as an XOR-advantage theorem, consistently with Drucker's own attribution of the fair direct-product result.

The addressed certificate-array mechanism is attributed to Aaronson, Ben-David, and Kothari, Definitions 14–15 and Lemma 17 in the PDF numbering of arXiv:1511.01937v2. The supplied TeX extraction shifts those numbers.

The unique all-one column and outward zero-witness chain are attributed to Göös, Pitassi, and Watson, Theorem 5 and §2.1. Direct pointers to one zero in every other column are explicitly discussed by Ambainis et al., §1, “Use of a balanced tree.” No novelty claim is made for direct outward pointers themselves. This refines adjudication R2-C-GPW's wording, which should not be read as claiming novelty of direct pointers alone.

The nearest-point minimax proof is self-contained, with Yao 1977 cited for the distributional principle. The original Yao full text was not read; publisher metadata was verified.

## Remaining limits

The finite-capped helper, strict hard-distribution strengthening, and m(m+1) zero-search improvement have proposed signatures and complete prose arguments but no supplied matching proof. The conditional-law and martingale rows have complete prose proofs and alternative formal endpoints. LEAN_GAPS.md lists the distinctions.

Source files are private packet contents at the supplied pin. No public repository link was invented. Passage correspondence names declarations and packet paths, and the read receipt records exact literature portions. Root's cold review found the mathematical routes correct on reading; the reported display typo was fixed. This is not a fresh proof-assistant validation.


## Supplement: Quantum source review

# Review of the quantum reconstruction

## Result and scope

The reconstructed quantum argument covers all 31 assigned corpus rows and six separately registered displayed intermediates. It gives complete ordinary-mathematical proofs of bounded amplification, exact conditional sampling, arbitrary probabilistic tournament selection, off-promise decoding and verification, ordinary bit-query compilation, and the explicit sixth-power logarithmic budget. No mathematical error affecting the upper bound was found in the inspected sources. This is a source and mathematical review, not a Lean build or independent human review.

The main manuscript is `reasoning-record.md`, Section 5. Its subsection labels distinguish bounded amplification, the probabilistic tournament, decoding/comparison/verification, and coherent access with query accounting. It preserves the preprint's Lemma 3.1 and Propositions 3.2–3.3 as named source results.

## Located findings and dispositions

1. **Proposition 3.2 has a genuine endpoint difference.** At `upper-tournament-evidence`, the list theorem is distinguished from `QuarticQuery.Upper.tournament_runs`, which consumes the list through a Boolean verifier and includes one extra verifier error. The complete list proof is reconstructed by coupling. `upper-continuation-induction` separately derives the exact source invariant and its verifier factor. Nothing is relabeled exact merely because it is sufficient for Proposition 3.3.
2. **The exact abstract amplification theorem is outside the supplied headline dependency closure.** `QuarticQuery.Amplification.bounded_amplification` has the exact Lemma 3.1 type, but the upper bound reaches `QuarticQuery.Upper.Samples.amplify`. The latter supplies the exact successful-label law needed after immediate measurement. `upper-amplification-proof` and `upper-quantum-tournament` state both facts. Aggregate corpus reach for the row does not imply reach for every declaration tied to it.
3. **Several “none” rows have direct source ingredients.** Examples include `eq-13`, `claim-success-prob`, `claim-decode-cost`, `claim-comparison-state`, `claim-verify`, and `claim-error`. They are cataloged in reading order in `LEAN_GAPS.md`. The original classifications were retained; the sidecar correspondences are proposed source relations, not fresh formal evidence.
4. **Literal state equality and successful-label equality are different.** `upper-stage-state` proves the paper's tensor preparation. The actual `QuarticQuery.Upper.stage_samples` can stop comparing after failure; it has the required exact law but not that literal workspace. This is stated locally.
5. **Retained workspace is load bearing.** `upper-comparison-law` proves orthogonality of decoded-label sectors and the classical-mixture law. This prevents interference between inconsistent off-promise decoder outcomes. The actual compiler's complete basis measurement and known reset are explained, without treating an unknown quantum state as freely erasable.
6. **Off-promise correctness is explicit at all interfaces.** Amplification has an unconditional cap; decoders always return a string; no opponent decoding guarantee enters winner dominance; a nonwinner has a failed local test at every possible address; the zero-input error is conditional on the full tournament history. These points appear in `upper-amplification-proof`, `upper-decode`, `upper-winner-dominates`, `upper-verification-proof`, and `upper-total-error`.
7. **Logarithm bases were normalized during the cold review.** The tournament horizon and input sizes use base two; explicit amplification repetitions and inequalities use `\ln`, matching `Real.log` in Lean. Big-O polylogarithms retain the document's base-two `\log` convention where the base does not affect the conclusion. The constant 138 is justified with natural logarithms.
8. **All mathematical delimiters were checked after writing.** A first draft lost some inline TeX delimiters during string construction. They were repaired before final correspondence extraction. The final source has balanced inline math delimiters, and each displayed block has an adjacent corpus or new-statement tag.
9. **All named Lean declarations were checked against the supplied declaration inventory.** The final manuscript names 61 fully qualified declarations, all present in `corpus/lean_dependencies.json`. Correspondence names and the existing vocabulary in new proposed signatures were checked as well. This is a name check only; it does not prove the proposed new signatures compile.
10. **Minor source comment.** `Tournament/Ideal.lean:364` describes `cycleThree` by saying i “loses” to i+1, while its definition gives a(i,i+1)=1 under the paper's winning-probability convention. The cycle theorem and all uses are mathematically consistent; the comment's verbal direction is reversed. The example is not needed by the proof, and the source was not edited.
11. **Bibliography metadata was checked against primary pages.** The publisher gives BBHT pages 493–505, while arXiv metadata gives 493–506; the bibliography follows the publisher and records the differing metadata in its note. Dagstuhl gives the Mande–Paraashar–Saurabh article pages 30:1–30:19. Proof locators use the supplied arXiv texts, which are identified explicitly.

## Primary sources and inspected locators

- Brassard–Høyer–Mosca–Tapp: supplied first four pages/Section 2, Lemma 1, equation (8), and Theorems 2–3. Primary metadata: <https://arxiv.org/abs/quant-ph/0005055>, DOI `10.1090/conm/305/05215`.
- Boyer–Brassard–Høyer–Tapp: supplied first four pages, Section 4, Lemma 2 and Theorem 3 including its proof. Primary metadata: <https://arxiv.org/abs/quant-ph/9605034>, publisher DOI `10.1002/(SICI)1521-3978(199806)46:4/5<493::AID-PROP493>3.0.CO;2-P`.
- Dürr–Høyer: the complete supplied text, Theorem 1 and its hitting-probability and expected-cost lemmas. Primary metadata: <https://arxiv.org/abs/quant-ph/9607014>, version 2 dated 7 January 1999.
- Mande–Paraashar–Saurabh: supplied introduction and Section 4, including the quantum algorithm and its proof; primary publication page <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30>.
- Ben-David–Kothari: supplied Theorem 1, randomized candidate comparison proof, and Lemma 5 with the quantum construction. Primary metadata: <https://arxiv.org/abs/2609.15063> and the authors' research publication page. This is cited as an organizational antecedent; its function and separation are different.
- Sun–Yao–Zhang: inspected the supplied SINK remark around Theorem 10 to understand the lineage in Ben-David–Kothari. No unverified theorem number or bibliographic detail from it is used in the reconstructed manuscript, and it is not included as a manuscript reference.

The bibliographic citations identify prior methods. Every inequality needed for the present amplification and tournament argument is proved in the reconstruction, including the sum identity, geometric failure bound, drift, Bernoulli bound, Markov step, coupling, verifier errors, compiler count, and final size arithmetic.

## Mathematical paper review receipt

- **object:** Section 5 of the long reasoning record for the supplied quartic query-complexity paper and Lean snapshot.
- **genre_and_target_reader:** Complete research proof reconstruction for a graduate reader in theoretical computer science or mathematics familiar with finite probability and the query model.
- **venue_calibration:** First four pages and a proof from BHMT, BBHT, and Dürr–Høyer were read; their direct definitions, explicit probability calculations, and concise theorem organization were used for calibration.
- **contribution_type:** Exposition and correspondence review. The six new rows expose intermediates or stronger quantitative statements already in the supplied source; no new research priority is claimed.
- **headline_claim_and_evidence_class:** The all-input quantum upper bound, unconditionally on the randomized lower bound, with source endpoints `QuarticQuery.Upper.Fkm_forrCircuit_QLe` and `QuarticQuery.Upper.Q_Fkm_le`. Source inspection is distinguished from supplied build fields.
- **scanability_check_title_abstract_intro_theorems_conclusion:** Scope and purpose are given before the amplification proof. Each subsequent section has a mathematical task. The final explicit bound is connected to the chosen circuit.
- **external_field_map:** Amplification, random-iteration search, total-order minimum finding, fixed tournament king finding, and candidate/certificate verification are cited with their differing hypotheses.
- **internal_dependency_map:** Exact successful-state law gives exact pivot law; complementary probabilities give ideal drift; dominant survival gives a success threshold; coupling gives a short candidate list; exact tests and fresh decoding give verification; the compiler and explicit counts give the total bound.
- **concrete_anchor_and_example_boundary:** Zero-success amplification, certain-success amplification, a comparison with probability one half, and cyclic comparisons are explicitly allowed. No toy example is used to claim sharpness.
- **hard_step_and_proof_forward_decisions:** The conditional output law, arbitrary history-dependent failures, retained-label orthogonality, off-promise verifier soundness, and ordinary-oracle compilation receive full proofs.
- **mathematical_taste_rubric_evidence_and_dispositions:** Proofs are organized around the needed statements; routine arithmetic stays inline; the six genuinely useful additional displays are separately registered. Evidence paragraphs follow completed proof groups.
- **concrete_simplification_attempt_and_outcome:** The trigonometric sum is derived by one telescoping identity. The ideal miss bound is the pointwise indicator inequality followed by expectation. Both preserve the paper's constants. The exact source continuation induction is also retained to expose the fidelity difference.
- **difficulty_landscape_and_fertile_questions:** The missing list-valued compiled theorem is identified precisely. It is an evidence/endpoint task; it is not needed to close the quantum upper bound.
- **short_long_transfer_locators:** Every owned row has one or more anchored passages in `correspondence.json`; the stronger finite and logarithmic bounds have new records.
- **notation_definition_and_equation_grammar:** Every new symbol is introduced locally. Natural logs and base-two logs are distinguished. T is the tournament horizon; a separate T0 denotes the general continuation horizon. No undefined probability is conditioned on a zero-mass success event.
- **first_time_reader_house_jargon_scan:** No new house terminology. Existing formal identifiers occur only in explicit evidence paragraphs.
- **one_use_symbol_scan:** None requiring removal; introduced constants, labels, and costs are reused in their derivation.
- **conditional_hypothesis_restrictiveness:** The comparison theorem requires only complementary unit-interval probabilities, and the dominant-vertex property is used only for inclusion. The final quantum result uses the realizing circuit but no randomized lower-bound assumption.
- **citation_role_checks:** Every external citation has a concrete method or antecedent role and an exact supplied locator. The present full proofs do not depend on an unquoted unknown theorem.
- **lean_statement_correspondence_and_validation_refs:** All names checked against the supplied declaration inventory. Mathematical evidence relations and composition alternatives are listed in `LEAN_GAPS.md`. No new formal check was claimed.
- **compressed_claim_occurrences_and_post_edit_scope_check:** List membership is not substituted for Boolean acceptance in evidence notes. The broader source k>=1 is explicitly restricted to the paper's k>=2 for the family statement. The selected circuit is retained in the explicit endpoint.
- **bibliography_render_check:** Entries inspected as text, authors and persistent identifiers verified from primary pages. Final rendered bibliography inspection is deferred to the parent integration step.
- **figure_and_reproducibility_check:** No figure or computational experiment is necessary for these exact proofs. Source paths and SHA-256 hashes are in the read receipt.
- **cold_reader_confusion_and_disposition:** Parent cold review identified missing inline math delimiters and ambiguous log notation; both were fixed before final sidecars. No mathematics was altered by those formatting repairs.
- **version_bound_review_coverage_and_omissions:** All assigned Lean files read in full. Exact additional portions and literature ranges appear in `source_read_receipt.json`. No remote repository or third-party Lean library was fetched or built.
- **material_transition_warrants_and_source_conflicts:** The only substantive endpoint discrepancy is the list versus verifier continuation. The abstract versus compiled amplification and literal-state versus output-law distinctions are explicitly resolved. BBHT page metadata was resolved in favor of the publisher.
- **exact_open_boundary:** No source theorem returning the candidate list with precisely the original Proposition 3.2 bound was found. No fresh compilation or independent comparison of any newly registered statement was performed.
- **rendered_release_checks:** Parent handles integration and rendered document QA. This child supplies Markdown, JSON, and BibTeX; no final PDF rendering is claimed here.
- **deliberate_non_changes:** Original corpus statements, hashes, and source code left unchanged; partial or absent evidence not upgraded; source query overheads and padding kept visible; no elementary gate bound asserted.
