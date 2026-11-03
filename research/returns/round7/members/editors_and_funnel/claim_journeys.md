# Fifteen claim journeys through the funnel

These are claim-level reading trips through the current supplied Markdown and the available Lean source. Each trip explicitly matches the exposition to the expert companion, enters the record and reads a formal endpoint. Where the papers offer only a whole-document link, the section matching below was manual. A journey can be mathematically adequate while its navigation is weak. We did not run Lean, Comparator or receipt checks, and we did not assert that live GitHub pages or the older record PDF match these bytes.

All paths, line numbers and anchors below refer to the supplied working files. The JSON companion retains exact source phrases and record anchor names so each trip can be reproduced in the packet.

The packet’s `LINK_MAP.json` reports zero problems for 75 links from the shorter papers. That does not test all of the record’s return links, the explanatory adequacy of a destination, or every omitted imported Lean file. The table and trips below therefore distinguish source existence from a successful reading route.

| Journey | Claim | Main outcome |
| --- | --- | --- |
| J01 | The optimal universal exponent is four | The mathematical endpoint agrees. |
| J02 | Both bounds use one circuit, with exponent six and coefficient 1/400 | Consistent after the two endpoints are distinguished. |
| J03 | Failure of the universal cubic bound | The main route agrees. |
| J04 | Forrelation hardness for each fixed k | The eventual fixed-k target matches. |
| J05 | A coherent promise decoder has an all-input cap | The coherent implementation and promise restriction are preserved. |
| J06 | The exact circuit checks domain and value | The common mathematical interface matches; the examples need not use the same gate list as the asymptotic family. |
| J07 | Winning defines a total function with at most one winning pair | This is a strong, readily inspectable journey. |
| J08 | The local tests characterize winning and can be queried coherently | The complete implementation type supports the advertised interface. |
| J09 | A winner defeats an off-promise opponent | The necessary ordinary bridge is that the winner’s decoder is correct with probability at least 1−ε, while no correctness condition is imposed on the rival’s label. |
| J10 | The probabilistic tournament returns a short list containing a dominant candidate | Substantively successful, with a stale visible return label. |
| J11 | Amplification preserves the measured pivot law under a fixed cap | The current cross-document calibration is materially better. |
| J12 | The direct product bounds a joint success-and-cap event | The bridge is explicit and necessary. |
| J13 | Erased-zero discovery is bounded by 4G/m² | The endpoint matches. |
| J14 | A cell query predicts an address: the capped simulator | The mathematical bridge survives: the simulator aborts before excess forwarded queries and may guess. |
| J15 | The universal quartic upper bound closes the infimum argument | The constants differ because the routes differ; both close the universal-exponent argument. |

## J01. The optimal universal exponent is four

- **Exposition:** Introduction, `repository/docs/exposition.md` line 19.
- **Expert companion:** §1, Theorem 1, `repository/docs/expert_companion.md` line 21.
- **Record:** §7.2, `repository/docs/reasoning_record.md` line 3683.

**Lean destination and relation.**

`alpha_tot_eq_four` in `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, line 326. Same equality. The body in the Challenge is a deliberate specification placeholder; the paired Solution forwards to alphaTot_eq_four_unconditional.

**Reading trip.** The exposition has a general link to the expert paper in its introduction and direct statement links in §7. The claim-to-expert step is a manual section match, not a dedicated per-claim link. Expert §6 gives the quotient argument. Record §7.2 supplies coordinate renaming and excludes all smaller powers; G.4 identifies the equality target.

**Assessment.** The mathematical endpoint agrees. The exponent is a universal infimum, not an assertion that one fixed k attains an exact fourth-power separation.

**Advice.** Retain the quotient and the order of choices. Give the relevant expert section when offering the expert-paper route.

## J02. Both bounds use one circuit, with exponent six and coefficient 1/400

- **Exposition:** Introduction and §3, `repository/docs/exposition.md` line 132.
- **Expert companion:** §2 and §7, `repository/docs/expert_companion.md` line 114.
- **Record:** §1 and §7, `repository/docs/reasoning_record.md` line 64.

**Lean destination and relation.**

`theorem_one_one` in `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, line 328. Compared headline uses one existential circuit per size and an existential logarithmic exponent; lower bound is in floor form.

`construction_family_named` in `repository/lean/QuarticQuery/Paper/ConstructionFamily.lean`, line 30. The explicit named circuit has exponent 6 and coefficient 1/400, with an existential threshold. This is the endpoint for those constants.

**Reading trip.** Expert §7 explicitly separates the two targets and links the named-circuit result. Record G.4 and G.9 explain the same distinction. The exposition’s four-theorem link alone does not expose the named constants.

**Assessment.** Consistent after the two endpoints are distinguished. The explicit threshold 13669k² is an ordinary specialization in the record, not part of either headline type.

**Advice.** Keep the existing distinction. Offer one readable route from the displayed explicit family to the named-circuit endpoint through the companion; do not add a new formalization obligation.

## J03. Failure of the universal cubic bound

- **Exposition:** Introduction and §6, `repository/docs/exposition.md` line 265.
- **Expert companion:** §1 and §6, `repository/docs/expert_companion.md` line 29.
- **Record:** §1 and §7.2, `repository/docs/reasoning_record.md` line 88.

**Lean destination and relation.**

`cubic_bound_fails` in `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, line 336. Same unshifted universal assertion: no real C works for every n≥1 and total function.

**Reading trip.** The exposition names the cubic conclusion again in §7. Expert §1 explains the choice k=3. Record §1 connects an unshifted cubic bound to the shifted definition and §7.2 supplies the general contradiction.

**Assessment.** The main route agrees. The exposition’s separate phrase about k=2 and its exercise answer need precision; those do not invalidate this k=3 route.

**Advice.** Keep the k=3 example and distinguish the endpoint equality of an exponent calculation from a proved Ω(Q³) bound.

## J04. Forrelation hardness for each fixed k

- **Exposition:** §3, Classical hardness, `repository/docs/exposition.md` line 130.
- **Expert companion:** §2(i) and §5, `repository/docs/expert_companion.md` line 250.
- **Record:** §3.6, §3.15 and §3.17, `repository/docs/reasoning_record.md` line 1611.

**Lean destination and relation.**

`forrelation_lower_bound` in `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, line 340. The target is BansalSinhaLower, whose definition is ∀k≥2 ∃t₀ ∀t≥t₀, Lvalue k t < R(P k t).

`forrelation_lower_uniform_sharp` in `repository/lean/QuarticQuery/ForrelationLower/Uniform.lean`, line 527. Separate uniform numerical estimate with 15k+2≤2t; it is stronger in a different parameter direction, not a quoted instance of the Bansal–Sinha formula.

**Reading trip.** The exposition cites the external source; the expert §5 distinguishes that input from the record’s alternative route. The record bundles the three needed properties in §3.17 and directs the formal reader to G.4–G.5.

**Assessment.** The eventual fixed-k target matches. Do not identify its proof with the printed Bansal–Sinha argument, or turn the record’s explicit threshold into part of the compared type.

**Advice.** Retain the external-result/alternative-proof distinction. Put the elementary threshold calculation after the uniform statement for readers who need the constant.

## J05. A coherent promise decoder has an all-input cap

- **Exposition:** §3, A cheap quantum decoder, `repository/docs/exposition.md` line 122.
- **Expert companion:** §2(ii), `repository/docs/expert_companion.md` line 103.
- **Record:** §3.3, `repository/docs/reasoning_record.md` line 571.

**Lean destination and relation.**

`construction_lemma_2_1_ii_complete` in `repository/lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean`, line 25. One coherent preparation and label law are chosen before the input; correctness is only on the promise, while the physical continuation cap is uniform.

**Reading trip.** The expert links repetition directly; the coherent continuation endpoint is reached via the record’s formal discussion. Its signature includes the workspace and every continuation, rather than only a scalar success probability.

**Assessment.** The coherent implementation and promise restriction are preserved. The supplied wrapper imports ConstructionForrelationQuantum, which is not included in the packet; this journey reads the complete wrapper type and its proof text, not its entire imported dependency closure.

**Advice.** For teaching, explain phase kickback and retained workspace at their first operational use or give an explicit accepted interface. Preserve the all-input cap.

## J06. The exact circuit checks domain and value

- **Exposition:** §2, Transcripts; §3, An exact circuit, `repository/docs/exposition.md` line 102.
- **Expert companion:** §2(iii), `repository/docs/expert_companion.md` line 105.
- **Record:** §3.4, `repository/docs/reasoning_record.md` line 670.

**Lean destination and relation.**

`forrCircuit_realises` in `repository/lean/QuarticQuery/Forrelation/Circuit.lean`, line 343. Exact CircuitRealises conclusion for the named circuit, with k=l+1.

`forrCircuit_size_le` in `repository/lean/QuarticQuery/Forrelation/Circuit.lean`, line 466. Size bound for t≥1, with a circuit constant dependent on k.

**Reading trip.** The expert’s §2 link lands at the construction of the circuit; the exposition’s small 180-gate example instead links to record §4.4. Both concern domain and value, but the toy Shannon circuit and the general Walsh circuit are distinct witnesses.

**Assessment.** The common mathematical interface matches; the examples need not use the same gate list as the asymptotic family. Their roles should remain explicit.

**Advice.** Retain the domain-bit counterexample. Do not make a reader think the large-size fast-transform circuit is the 180-gate toy circuit.

## J07. Winning defines a total function with at most one winning pair

- **Exposition:** §2, `repository/docs/exposition.md` line 88.
- **Expert companion:** §2, `repository/docs/expert_companion.md` line 112.
- **Record:** §4.2, `repository/docs/reasoning_record.md` line 1747.

**Lean destination and relation.**

`WinsAt` in `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, line 266. A predicate on raw input bits with defined partial values required only of the proposed winner.

`addressedF` in `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, line 276. Total Boolean function obtained by deciding existence of a winning pair.

`winsAt_unique` in `repository/lean/QuarticQuery/Construction/Winner.lean`, line 55. Uniqueness of both column and address.

**Reading trip.** The exposition’s §7 links directly to WinsAt and F. The matching expert proof and record §4.2 give the contradiction through a pointer into an all-one string. The packaged Construction Challenge is absent, but Winner.lean contains the concrete implementation statement and short proof.

**Assessment.** This is a strong, readily inspectable journey. It does not confuse totalization with answering an unpromised partial input arbitrarily.

**Advice.** Keep this as the first formal-definition inspection task. The explicit ordinary proof is short enough to stay beside the definition.

## J08. The local tests characterize winning and can be queried coherently

- **Exposition:** §2, Local tests, `repository/docs/exposition.md` line 106.
- **Expert companion:** §2, Local tests, `repository/docs/expert_companion.md` line 116.
- **Record:** §4.4–§4.6, `repository/docs/reasoning_record.md` line 1812.

**Lean destination and relation.**

`construction_lemma_2_2_with_support` in `repository/lean/QuarticQuery/Paper/ConstructionFull.lean`, line 23. Contains the exact K count, equivalence to all tests passing, adaptive depth and one coherent physical continuation. Also includes essential-coordinate witnesses.

**Reading trip.** Expert §2 links §§4.4–4.6, which supply separate ordinary and coherent arguments. G.4 identifies this implementation theorem. The packet omits Independent/ConstructionFull/Challenge.lean; that absence is a packaging boundary, not evidence that the statement was never compared.

**Assessment.** The complete implementation type supports the advertised interface. A depth cap ℓ+1 is not the number of input coordinates on which a pointer test can depend, and the type does not promise restored workspace.

**Advice.** Keep the concrete pointer query and gate-consistency induction. Preserve the distinction between adaptive depth and support when linking the formal result.

## J09. A winner defeats an off-promise opponent

- **Exposition:** §4, Comparing two columns, `repository/docs/exposition.md` line 142.
- **Expert companion:** §3.1, `repository/docs/expert_companion.md` line 139.
- **Record:** §4.7 and §5.3, `repository/docs/reasoning_record.md` line 1952.

**Lean destination and relation.**

`winner_no_incoming_zero` in `repository/lean/QuarticQuery/Construction/Winner.lean`, line 62. Boolean half: every rival label points to a one in the winner.

`winner_finds_zero` in `repository/lean/QuarticQuery/Construction/Winner.lean`, line 69. Boolean half: the winner’s correct cell points to a zero in each rival.

**Reading trip.** The exposition and expert give the same two-case reason. Record §4.7 states the arbitrary-label guarantee before §5.3 puts it into a probabilistic comparison. The supplied Winner.lean ends at the two Boolean facts, not at the complete decoded comparison law.

**Assessment.** The necessary ordinary bridge is that the winner’s decoder is correct with probability at least 1−ε, while no correctness condition is imposed on the rival’s label. The Boolean declarations alone should not be described as a formal proof of the full sampling routine.

**Advice.** Keep the two concrete pointer facts prominent. Name the probabilistic step when moving from them to a_ij≥1−ε.

## J10. The probabilistic tournament returns a short list containing a dominant candidate

- **Exposition:** §4, An ideal process and A stage of the search, `repository/docs/exposition.md` line 152.
- **Expert companion:** §3.2, Proposition 3, `repository/docs/expert_companion.md` line 143.
- **Record:** §5.2, `repository/docs/reasoning_record.md` line 2150.

**Lean destination and relation.**

`quantumTournament` in `repository/lean/QuarticQuery/Paper/QuantumTournamentFacts.lean`, line 287. One input-indexed list law and finite cap are chosen before the dominant candidate; includes success ≥1−2m/2^T−Tε and an explicit 6072 cost bound.

**Reading trip.** The expert links §5.2. The entry statement is useful and the endpoint is identifiable in G.4. A later return pointer at #upper-ideal-process still sends the reader to companion §4.2, although this argument is now §3.2.

**Assessment.** Substantively successful, with a stale visible return label. The deterministic toy board makes the mechanism visible but does not exercise arbitrary fractional loser comparisons; the record’s separate fractional example remains valuable.

**Advice.** Repair the return label and add a small fractional-probability check only where it teaches the feature absent from the deterministic board; preserve the weighted sampling law.

## J11. Amplification preserves the measured pivot law under a fixed cap

- **Exposition:** §4, Amplification with a fixed cap, `repository/docs/exposition.md` line 179.
- **Expert companion:** Lemma 2 and §7, `repository/docs/expert_companion.md` line 279.
- **Record:** §5.1 and G.7, `repository/docs/reasoning_record.md` line 2114.

**Lean destination and relation.**

`Samples.amplify` in `repository/lean/QuarticQuery/Upper/Amplify.lean`, line 346. Measured-label Runs endpoint with failure bounds and ampLaw; this is the form used by the upper bound.

`uniformOpaqueAmplifier` in `repository/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean`, line 17. Separate retained-state endpoint, uniform in the opaque preparation, for success predicates on basis labels.

**Reading trip.** The expert’s current §7 correctly separates measured and retained-state forms. The older round-six complaint that its pronoun identifies them is fixed. The ordinary Lemma 2 and the prose proof may still be used to explain the ideal law; they do not establish identity of the two formal implementations.

**Assessment.** The current cross-document calibration is materially better. The exposition’s wording about the realized number of preparations being fixed needs correction to an advance upper cap.

**Advice.** Preserve the two endpoint descriptions. Put the preparation count and the random stopping rule in different clauses, without adding an implementation-identification theorem.

## J12. The direct product bounds a joint success-and-cap event

- **Exposition:** §5, Direct product and simulator, `repository/docs/exposition.md` line 224.
- **Expert companion:** §4.1, Lemma 4, `repository/docs/expert_companion.md` line 177.
- **Record:** §6.1 and G.8, `repository/docs/reasoning_record.md` line 2682.

**Lean destination and relation.**

`direct_product_external_finite_realized_caps` in `repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean`, line 18. Finite weighted external seeds; conclusion bounds compliantSuccess, not success conditional on compliance.

**Reading trip.** The three prose statements allow arbitrary independent coins and outside information. The record’s #CL-independent-information groups these into finitely many behaviors. G.8 explains the recursive cap predicate and its ordinary relation to query counts. Expert §7 now links success together with compliance, fixing the old ambiguous link text.

**Assessment.** The bridge is explicit and necessary. The normalized conditional-value proof in the exposition and unnormalized proof in the expert are two presentations of the same bound; a verbatim-proof correspondence is unnecessary.

**Advice.** Keep the joint-event counterexample and the three-budget explanation. Route a formal reader through both the finite-mixture reduction and the cap-count identification.

## J13. Erased-zero discovery is bounded by 4G/m²

- **Exposition:** §5, The erased zero, `repository/docs/exposition.md` line 212.
- **Expert companion:** §4.3, `repository/docs/expert_companion.md` line 201.
- **Record:** §6.4, `repository/docs/reasoning_record.md` line 3280.

**Lean destination and relation.**

`eq_19_complete` in `repository/lean/QuarticQuery/Paper/Eq19Complete.lean`, line 23. Conjunction of the exact random-column identity and the 4G/m² bound under the complete dummy law. Uses an alternative finite-world proof, not the early/late decomposition.

**Reading trip.** The exposition links the early/late proof and the expert links its sharper optional continuation. The record identifies which route is formal. The missing Independent/Eq19/Challenge file prevents inspecting that configured challenge locally; Eq19Complete and the independent Spec/Bridge are present.

**Assessment.** The endpoint matches. A checked inequality is not evidence that this particular explanatory decomposition was formalized, and the record already makes that distinction.

**Advice.** Keep the independent-column counterexample and the readable early/late proof. Preserve the endpoint/route distinction in the audit appendix.

## J14. A cell query predicts an address: the capped simulator

- **Exposition:** §5, The simulator, `repository/docs/exposition.md` line 238.
- **Expert companion:** §4.4, `repository/docs/expert_companion.md` line 221.
- **Record:** §6.5, `repository/docs/reasoning_record.md` line 3393.

**Lean destination and relation.**

`eq_21` in `repository/lean/QuarticQuery/Paper/ClassicalPlanted.lean`, line 342. Per-column, per-time joint-event inequality under the original dummy sampling law; μ is normalized, supported on the promise and hard at cap L.

**Reading trip.** The expert’s equation (12), the exposition’s light-and-hit event and record equation (21) are the same step under different numbering. The exposition promises a worked trace but links #CL-simulator; the actual example starts at #CL-simulator-example. Record §6.6 then sends the expert reader back to nonexistent companion §5.5 instead of current §4.5.

**Assessment.** The mathematical bridge survives: the simulator aborts before excess forwarded queries and may guess. The weakest part of the journey is finding the promised example and returning to the right section.

**Advice.** Point the example link at its own anchor, repair the return label, and retain lightness inside the probability. Do not recast the argument as computing the address before any cell visit.

## J15. The universal quartic upper bound closes the infimum argument

- **Exposition:** §6, `repository/docs/exposition.md` line 271.
- **Expert companion:** §1 and §7, `repository/docs/expert_companion.md` line 275.
- **Record:** Appendix A, `repository/docs/reasoning_record.md` line 3763.

**Lean destination and relation.**

`D_le_Q_pow_four` in `repository/lean/QuarticQuery/Appendix/TheoremA1.lean`, line 52. D≤20736 Q⁴ through the imported complexity-library route.

`universalPower_four` in `repository/lean/QuarticQuery/Appendix/TheoremA1.lean`, line 70. Membership of exponent four in the defining set, derived from R≤D.

**Reading trip.** The exposition links the record’s ordinary reconstruction with constant 35⁴. Expert §7 also names the imported route with constant 20736. The theorem file explicitly says its imported proof is not a line-by-line formalization of Appendix A.

**Assessment.** The constants differ because the routes differ; both close the universal-exponent argument. This is a successful calibrated comparison, not an inconsistency to “fix” by making the constants equal.

**Advice.** Keep both routes identifiable in the record, while giving the exposition only the upper-bound consequence it needs.

## What these trips establish

The shared headlines, fixed-k quantifiers, floor-to-real conversion, named circuit, promise restriction and principal probability events are recoverable across the current documents. Several paths require an unnecessary manual search, and the record has stale visible return numbers despite valid anchors. The current measured-label/retained-state distinction and the 508 growing-k correction should be preserved. A local absence from this review packet is reported as an access boundary; it is not a verdict on the repository’s full proof or a request for new formalization.
