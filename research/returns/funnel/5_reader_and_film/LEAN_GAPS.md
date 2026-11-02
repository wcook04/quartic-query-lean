# Lean evidence gaps and different proof routes

The supplied snapshot reports the full unconditional Theorem 1.1. The entries below identify limitations of particular correspondences and differences in proof route; they do not turn that theorem back into a conditional result. Reading order follows the argument map, followed by additional film details. The exact raw fields remain in `argument_map.json` and the input corpus.

<!-- passage:gaps-main -->
## The distinctions that affect the explanation

The winner definition should be read before any evidence badge: the true address must be defined, its transcripts must be correct, and its outward pointers must find zeros. Source definitions such as `WinsAt` can be present even when the corpus row has no reviewed tie. The finite example adds proposed specialization statements; all remain uncompiled.

For quantum amplification, the standalone full-state theorem and the reached label-sampling theorem are separate declarations. For the tournament, the formal program consumes its list inside verification. For the direct product, the exact full statement is available by an alternative subdistribution proof, while the headline uses a deterministic specialization. The erased-zero estimate is stronger in Lean, but the paper's intervening expectation identity is not part of that route.

The Forrelation lower bound is discharged by a separate fixed-k proof. It bypasses `claim-bs-to-L`, whose supplied exact tie is incorrect. The universal quartic endpoint is imported through the complexitylib bridge rather than the chain of Appendix A lemmas. These differences should be stated once where the reader uses the relevant step.

`eq-2` remains a partial corpus row. The full unconditional theorem retains one circuit in both bounds, and `rpow_le_of_Gvalue_lt` converts its floor lower bound to the asymptotic form after enlarging the threshold. The alternative route does not weaken the headline claim.

Sources: packet `repository/corpus/statements.json`; `repository/docs/statement_fidelity_review.md`, findings 3–7; `Results/Unconditional.lean`; `Results/Exponent.lean`; `AUDIT_FINDINGS.json`.
<!-- /passage:gaps-main -->

## Every affected displayed corpus row

<!-- passage:gaps-table -->
The table preserves the supplied statement and route classifications. “None” means that this row has no reviewed supplier; it does not assert that the development lacks relevant code. The different declarations attached to one row retain their individual relations in the corpus.

| Statement ID | Formal statement | Route | Reason to expose a limit or distinction |
| --- | --- | --- | --- |
| `def-column-layout` | `partial` | `none` | The reviewed ties prove the pointer bijection. The complete layout is the source type BitLoc, which has no direct reviewed tie in this row. |
| `def-winner` | `none` | `none` | No reviewed tie on the row. The exact definition WinsAt and the proof winsAt_iff_paperWinsAt can be inspected separately. |
| `cor-unique-winner` | `none` | `none` | No reviewed row tie; Construction/Winner.lean contains winsAt_column_unique and winsAt_unique. |
| `eq-1` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `thm-1.1` | `exact` | `alternative` | The full unconditional source theorem supplies the headline. Its Forrelation and universal-upper-bound ingredients use alternative routes. The short alphaTot equality supplies only one clause. The older theorem_1_1 still has a BansalSinhaLower hypothesis despite its empty metadata array. |
| `eq-3` | `partial` | `none` | The statistic, delta and normalized matrix representation have separate declarations. No single tied declaration states every clause of this ledger row. |
| `eq-4` | `partial` | `none` | P_eq_cases pins all promise branches; cases_disjoint supplies disjointness. Individual ties remain partial. Large negative correlation is outside the promise. |
| `lem-2.1.ii` | `partial` | `none` | QLe (P k t) (2 (2^(10k+5) k)) for every t: the constant-query quantum bound at error 1/3, on the real oracle. |
| `lem-2.2.i` | `partial` | `none` | Test indexing, exact evaluation, depth, and winner equivalence are proved in separate declarations. Keep the per-test adaptive query bound distinct from the size of its possible support. |
| `cor-local-dichotomy` | `none` | `none` | No reviewed row tie; exists_failing_localTest and winner/test equivalence are candidate source suppliers. |
| `claim-winner-dominates` | `partial` | `none` | The deterministic pointer invariants and cmpProb_winner are partial suppliers. The quantitative bound also uses the winner address-decoding probability, combined in Upper/Verify.lean. |
| `eq-10` | `partial` | `none` | cmpProb is tied, but the equation theorem cmpProb_isComparison is not tied to this row. The full source type is available for inspection. |
| `eq-13` | `none` | `none` | The row has no reviewed tie although Tournament.expected_weight_eq and expected_weight_le_half are present and the latter is used in the comparison controls. This is an evidence-mapping gap, not source-proof absence. |
| `lem-3.1` | `exact` | `same` | An exact full-state theorem is available but outside headline reach. The reached sampler theorem is partial relative to that state-level row and proves the needed exact label law and cap. Do not combine reach and exactness across these ties. |
| `prop-3.2` | `partial` | `none` | The formal quantum program consumes a list through its verifier instead of returning it. Its guarantee includes the verifier error; the paper row asserts list membership. The ideal-process theorem and cost statements cover other parts. |
| `claim-verify` | `none` | `none` | No tie on this row. Upper.search_runs and the verification lemmas supply relevant source evidence, currently tied elsewhere. Do not silently promote this row. |
| `lem-2.1.i` | `exact` | `alternative` | Discharged unconditionally by ForrelationLower.bansalSinhaLower. This is a separate fixed-k proof of the weaker bound needed here, not a formal reproduction of the cited Bansal–Sinha proof. The source locator in the supplied tie is wrong. |
| `def-dummy` | `partial` | `none` | The sample-point definition and a product-weight identity are tied, while the full distribution appears in the coupling context. |
| `def-planted` | `partial` | `none` | The sample-point definition and individual consequences supply parts of the distributional row; retain independent uniform planting and support hypotheses. |
| `claim-Y-values` | `partial` | `none` | Two separate declarations establish rejection of the dummy input and acceptance of the planted input on the hard distribution support. |
| `eq-18` | `partial` | `none` | Run by run, one-sided: planted minus dummy output is at most found zero + heavy + reachedCell. No absolute value, which the proof never needs, and the cell term is already split. |
| `eq-19` | `stronger` | `alternative` | The source proves a stronger 2G/m² erased-zero bound by another argument. It does not define the paper random variable Z or prove the displayed EZ/m identity. Keep the inequality and missing identity separate. |
| `lem-4.1` | `exact` | `alternative` | The full randomized/auxiliary-information statement has exact alternative-route ties. The headline uses a deterministic specialization. The formal proof inducts over subdistributions rather than using the paper supermartingale. |
| `eq-21` | `partial` | `none` | The joint event over the whole run. The per-time probability of the row is not stated; avg_reachedCell_le bounds the union directly. |
| `eq-22` | `partial` | `none` | Joint event only, G rho, pointwise over U and with no conditioning on nonheavy. The heavy term G/(mL) joins in tree_gap_le, so the row as stated is not one declaration. |
| `eq-23` | `partial` | `none` | The tied tree theorem is one-sided, uses 2G/m² and an abstract rho, and does not alone state the paper absolute gap with rho=(2/3)^r. Its application supplies the needed impossibility argument. |
| `cor-R-omega` | `partial` | `none` | The recorded arithmetic theorem converts G<r into the power bound; it does not itself mention R or F. The family construction supplies the substitution. |
| `eq-2` | `partial` | `none` | The tied declarations split same-circuit size, query bounds, floor form and asymptotic form. The current row stays partial even though the full unconditional headline assembles the family. rpow_le_of_Gvalue_lt supplies the floor-to-Omega conversion at an enlarged threshold. |
| `claim-exponent-ratio` | `partial` | `none` | The choice of k only. |
| `thm-A.1` | `exact` | `alternative` | The exact endpoint is reached through complexitylib, not by reproducing the paper Appendix A proof. Reading Appendix A does not make its intermediate lemmas checked. |
| `def-query-oracle` | `partial` | `none` | The listed bridge lemmas and bitOracleL cover different properties. The action is in the public bitOracle definition and must be displayed with the model. |
| `lem-2.2.ii` | `partial` | `none` | The coherent test sampler and failing-test search are partial suppliers. Some tied declarations concern later verification rather than the entire coherent-access sentence. |
| `claim-bs-to-L` | `exact` | `alternative` | Disputed exact tie: bansalSinhaLower proves the endpoint L<R(P), not this numerical comparison. The active Lean route bypasses this step; withhold an automatic checked badge. See AUDIT-01 and AUDIT-02. |
| `eq-7` | `partial` | `none` | The recorded theorem proves address uniqueness; the true-address definition itself has no complete reviewed tie here. |
| `claim-success-prob` | `none` | `none` | No row tie is recorded. Upper.stageLaw_some and stageLaw_none are source candidates for the successful-label and failure masses; W>0 is required for the conditional law. |
| `def-simulator` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `eq-8` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `def-comparison` | `none` | `none` | No reviewed tie is recorded on this row. Inspect QuarticQuery.Upper.cmpProb and its surrounding hypotheses as a candidate correspondence; the raw evidence remains unchanged. |
| `claim-comparison-state` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `eq-15` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `claim-error` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `def-walsh-sign` | `partial` | `none` | W W^T = m I over the reals. |
| `claim-N-phi` | `partial` | `none` | Gives Phi = N/M as the matrix product; integrality is by type, but W's +-1 entries and M>0 are stated elsewhere. |
| `claim-integer-tests` | `partial` | `none` | Second iff of the row. |
| `claim-proj-prob` | `partial` | `none` | The real projection identity and an executable sampler have separate ties; the source compiler uses a constant-factor bit-query overhead. The film states the probability and fixed-k cheapness without an exact physical query count. |
| `eq-6` | `partial` | `none` | logb_mValue establishes log₂m=2t; Fkm uses r=40t directly. The ceiling formula is not separately tied to this row. |
| `def-transcript` | `partial` | `none` | Uniqueness and existence are tied, while the transcript representation and gate rules are public definitions. They are distinct correspondence obligations. |
| `def-K` | `partial` | `none` | card_testIndex proves the exact count. The big-O estimate in the ledger row is not in that declaration. |
| `def-decode` | `none` | `none` | No reviewed tie is recorded on this row. Inspect QuarticQuery.Upper.decode_samples and its surrounding hypotheses as a candidate correspondence; the raw evidence remains unchanged. |
| `claim-decode-cost` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `eq-11` | `none` | `none` | No reviewed Lean tie is recorded for this row. It remains a paper statement in this explanation; source absence is not inferred from missing metadata. |
| `def-T-eps` | `partial` | `none` | Numeric consequence used in Section 3.3. |
| `claim-weight-lb` | `partial` | `none` | Weight bounds at exponent T, where the row has t. W>0 until selected is half_lt_total, which carries no tag. |
| `construct-sampler` | `partial` | `none` | The successful-label law and coherent construction are tied separately. Amplification and the stopping rule enter in tournament_runs. |
| `claim-coupling` | `partial` | `none` | The reached statement bounds acceptance through a verifier and includes its factor, rather than directly asserting list membership. |
| `claim-tournament-cost` | `partial` | `none` | The tied statements supply a concrete cap and a coarse polylogarithmic estimate, not every symbolic cost clause of the paper row. |
| `def-verify` | `none` | `none` | No reviewed tie is recorded on this row. Inspect QuarticQuery.Upper.verifyProb and its surrounding hypotheses as a candidate correspondence; the raw evidence remains unchanged. |
| `eq-5` | `none` | `none` | No reviewed tie is recorded on this row. Inspect QuarticQuery.Lvalue and its surrounding hypotheses as a candidate correspondence; the raw evidence remains unchanged. |
| `def-heavy` | `none` | `none` | No reviewed tie is recorded on this row. Inspect QuarticQuery.aQueries and the inequality L < aQueries I l in LowerBound/Planted/Heavy.lean and its surrounding hypotheses as a candidate correspondence; the raw evidence remains unchanged. |
| `eq-17` | `none` | `none` | No reviewed tie is recorded on this row. Inspect QuarticQuery.Gvalue and its surrounding hypotheses as a candidate correspondence; the raw evidence remains unchanged. |
<!-- /passage:gaps-table -->

## New calculations in the worked example

<!-- passage:gaps-new -->
Every entry below is `proposed_uncompiled`. Its public-vocabulary signature and dependency list are in `NEW_STATEMENTS.json`.

| New ID | Displayed content | Remaining Lean work |
| --- | --- | --- |
| `reader-forrelation-yes` | An explicit address-answer 1 in the running example. | Elaborate the signature and prove its finite specialization. |
| `reader-forrelation-zero` | An explicit address-answer 0 in the running example. | Elaborate the signature and prove its finite specialization. |
| `reader-example-parameters` | Prevent the small illustration from being presented as an asymptotic speedup experiment. | Elaborate the signature and prove its finite specialization. |
| `reader-example-instance` | Certify the running construction and the two locations changed in the film using the actual supplied family. | Elaborate the signature and prove its finite specialization. |
| `reader-walsh-example` | Every entry and matrix-vector product displayed in the exact Forrelation scene is tied to the supplied public definition. | Elaborate the signature and prove its finite specialization. |
| `reader-tournament-first-pivot` | The film displays one symbolic update without inventing the actual comparison probabilities of the construction. | Elaborate the signature and prove its finite specialization. |
The supplied circuit is fixed, but its full gate transcript is specified symbolically by `circuitEval`; no fabricated gate list is displayed. The small instance has `L=0` and carries no asymptotic lower-bound claim. The symbolic tournament update introduces no numerical comparison matrix.
<!-- /passage:gaps-new -->

## Reported checking and unavailable original receipts

<!-- passage:gaps-records -->
The graph and trace record successful local comparisons and expected rejection of the five altered solutions. Original receipts, logs and compiled exports are not in the supplied packet. The recorded paranoid receipt names source commit `d42fb67a7e060fb5386867dadf20a5903df39141`; the final packet is pinned to `c7e0c9161f0ad898889bd9166e7b354acd42188d`. This return has not replayed either run or verified a source diff between them.

The old fidelity review's conditional headline describes its earlier snapshot. The legacy `QuarticQuery.theorem_1_1` has an explicit `BansalSinhaLower` hypothesis even though its supplied metadata omits it. Default to the full unconditional declaration and display the actual type. A negative-control harness `passed` means it observed the expected rejection. These are evidence-record corrections, not mathematical statement changes.

Sources: `AUDIT_FINDINGS.json`, AUDIT-03 through AUDIT-08; `READ_SCOPE.md`; packet `repository/README.md`; attached trace O191–O193 and final closeout.
<!-- /passage:gaps-records -->
