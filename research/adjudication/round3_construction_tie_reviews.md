# Round-three construction and classical tie reviews

51 declaration-level judgments across 43 statement IDs are recorded in [the review data](round3_construction_tie_reviews.json). Each retains the ledger text, lexical Lean signature and implicit section context, source location and hash, source comparison, route, premises and open assumptions. These are source reviews, not elaborated `#check` results, builds, Comparator executions or fresh bindings. Freeze and recheck the full local Lean/configuration snapshot before binding.

| Statement | Individually reviewed declaration | Relation | Route |
| --- | --- | --- | --- |
| `def-winner` | `QuarticQuery.Paper.constructionWinner` | exact | none |
| `def-winner` | `QuarticQuery.Paper.construction_winner_iff_exists_winsAt` | stronger | none |
| `def-win-at-address` | `QuarticQuery.Paper.construction_winsAt_iff_winner_and_address` | partial | none |
| `def-win-at-address` | `QuarticQuery.Paper.construction_win_at_address_outputs` | partial | same |
| `cor-local-dichotomy` | `QuarticQuery.Paper.construction_local_dichotomy` | stronger | same |
| `lem-2.2` | `QuarticQuery.Paper.construction_lemma_2_2_complete` | partial | same |
| `claim-winner-dominates` | `QuarticQuery.Paper.quantumWinner_dominates` | exact | same |
| `claim-product-law` | `QuarticQuery.Paper.classical_transcript_product_law` | exact | same |
| `eq-16` | `QuarticQuery.Paper.classical_eq_16_transcript` | partial | same |
| `eq-16` | `QuarticQuery.Paper.classicalTranscriptValue_unchanged` | partial | same |
| `claim-final-bound` | `QuarticQuery.Paper.classical_final_bound` | exact | same |
| `claim-uniform-zero` | `QuarticQuery.Paper.uniform_zero_given_transcript` | exact | same |
| `eq-21` | `QuarticQuery.Paper.eq_21` | exact | same |
| `eq-22` | `QuarticQuery.Paper.eq_22` | exact | same |
| `claim-tail` | `QuarticQuery.Paper.classical_tail_parameters` | partial | same |
| `lem-2.2.i` | `QuarticQuery.Paper.construction_lemma_2_2_i` | partial | same |
| `lem-2.2.i` | `QuarticQuery.Paper.construction_pointer_every_physical_coordinate` | partial | same |
| `lem-2.2.ii` | `QuarticQuery.Paper.construction_lemma_2_2_ii` | partial | same |
| `lem-2.2.ii` | `QuarticQuery.Paper.construction_lemma_2_2_complete` | stronger | same |
| `def-aij` | `QuarticQuery.Paper.quantumComparison_unordered_state` | partial | same |
| `eq-10` | `QuarticQuery.Paper.quantumComparison_complementary` | partial | same |
| `def-T-eps` | `QuarticQuery.Paper.quantumTournament_parameters` | exact | none |
| `eq-11` | `QuarticQuery.Paper.quantumDominant_iff` | exact | none |
| `def-ideal-process` | `QuarticQuery.Tournament.expectFrom` | exact | none |
| `eq-12` | `QuarticQuery.Tournament.weight` | exact | none |
| `claim-expected-WT` | `QuarticQuery.Tournament.expected_final_weight` | exact | same |
| `claim-weight-lb` | `QuarticQuery.Paper.quantumWeight_lower` | exact | same |
| `eq-14` | `QuarticQuery.Tournament.ideal_miss_le` | exact | same |
| `construct-sampler` | `QuarticQuery.Paper.quantumTensorStage_of_samples` | partial | same |
| `eq-15` | `QuarticQuery.Paper.equation_15` | exact | same |
| `claim-success-prob` | `QuarticQuery.Paper.quantumStage_success` | exact | same |
| `claim-coupling` | `QuarticQuery.Paper.quantumList_coupling` | partial | same |
| `claim-tournament-cost` | `QuarticQuery.Paper.quantumTournament_cost` | partial | same |
| `prop-3.2` | `QuarticQuery.Paper.quantumTournament` | stronger | same |
| `def-decode` | `QuarticQuery.Paper.quantumDecode` | partial | same |
| `claim-decode-cost` | `QuarticQuery.Paper.quantumDecode_correct` | partial | same |
| `def-comparison` | `QuarticQuery.Paper.quantumComparison_sorted` | partial | same |
| `claim-comparison-state` | `QuarticQuery.Paper.quantumComparison_state` | partial | same |
| `def-verify` | `QuarticQuery.Paper.quantumVerify_fixedAddress` | partial | same |
| `claim-verify` | `QuarticQuery.Paper.quantumVerify` | partial | same |
| `claim-error` | `QuarticQuery.Paper.quantumError_bound` | partial | same |
| `claim-coherent-access` | `QuarticQuery.Paper.quantum_coherent_tree` | partial | same |
| `def-value-V` | `QuarticQuery.Paper.classicalTranscriptValue` | partial | same |
| `claim-supermartingale` | `QuarticQuery.Paper.classical_transcript_conditional_expectation` | partial | same |
| `lem-4.1` | `QuarticQuery.Paper.classical_direct_product_average` | partial | same |
| `claim-address-guess` | `QuarticQuery.address_guess_average` | partial | same |
| `prop-3.3` | `QuarticQuery.Upper.Q_Fkm_le` | stronger | same |
| `claim-minimax-mu` | `QuarticQuery.exists_hard_distribution` | exact | same |
| `lem-2.2.i` | `QuarticQuery.Paper.construction_lemma_2_2_with_support` | stronger | same |
| `lem-2.2.ii` | `QuarticQuery.Paper.construction_lemma_2_2_with_support` | stronger | same |
| `lem-2.2` | `QuarticQuery.Paper.construction_lemma_2_2_with_support` | stronger | same |

## Material judgments

- The corrected `lem-2.2.i` includes essential support on physical pointer and target coordinates. The existing `construction_lemma_2_2_complete` is partial for the corrected combined `lem-2.2` row, although it is stronger for `.ii` alone. The new `construction_lemma_2_2_with_support` conjoins the full physical witness with that complete statement; its type is stronger for `.i`, `.ii` and the conjunction. `Loc` is definitionally the relevant `BitLoc`, and the coordinate map is injective. The new wrapper requires its own validation and binding.
- `def-win-at-address` combines output-test and winner/true-address equivalences. Each reviewed theorem proves one component; neither should be credited as the whole combined statement on its own. The output-test component needs the supplied circuit-realization premise.
- `eq-16` combines the queried-factor inequality with the unaffected factors. The source contains separate declarations. Likewise `claim-tail` includes convergence of the displayed envelope, which is not the same conclusion as convergence of the bounded left-hand tail; the reviewed combined declaration remains partial for the literal row.
- `lem-4.1` and `claim-address-guess` refer to arbitrary independent information, while the reviewed averaging declarations quantify over finite seed types. They are partial for the literal rows until an independently validated finite-behavior pushforward is supplied.
- `eq-21` retains nonheaviness inside the original-law joint event. `eq-22` uses an independent uniform planted index and the given one-instance hardness; no conditional-hardness premise is inferred. `claim-uniform-zero` conditions only on a positive-probability full adaptive transcript.
- Quantum statements distinguish a retained-state witness from a measured label law. Several definitions and proofs comprise more than one theorem, and the corresponding partial judgments do not imply a whole-row result. The list-valued tournament declaration packages its explicit physical cap and membership probability.

Normal mathematical premises are recorded separately from additional open assumptions. A reviewed relation does not prove its declaration was built or compared, and later source edits require reinspection before binding.
