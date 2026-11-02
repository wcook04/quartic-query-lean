# Independent formal-scope audit: quantum upper bound

## Main finding

The packet supplies current source-bound build evidence for the quantum helper declarations, including the list-valued tournament and the literal tensor preparation. It does not supply a theorem identifying the coherent retained-workspace amplification implementation with the original normalized successful output state. The missing item is a semantic bridge, not merely an outstanding compilation run.

The packet was not changed and no Lean or Comparator run was performed in this review. No Lean, Lake or pinned compiled dependency cache was available in this workspace. All compilation claims below are about the supplied native receipts, checked against the exact enclosed source bytes.

## 1. What the source-bound evidence supports

The current root receipt is `repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json`, recorded at 18:25:39 UTC on 2 November 2026, source pin `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`, toolchain `leanprover/lean4:v4.36.0-rc2`. It reports a successful Lake target followed by declarations read from its compiled environment: 2,652 declarations. The packet manifest's repository commit is `1dd469dd0042b937b739da3bc211eeb60bdf7462`; a changed commit label does not invalidate a source-current record when the exact bound sources match.

This subaudit independently hashed all 124 local Lean/config inputs listed in the snapshot, current build receipt, dependency export and final axiom verdict. Every file was present and matched, and all four source-hash maps were identical. The current build receipt's bytes match its snapshot hash. The native type/axiom log and audit-source bytes also match the final verdict's recorded SHA-256 hashes. These are checks of supplied evidence integrity, not a reproduction of the build.

The dependency export names `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional` as its roots and reports 1,354 reached public declarations. None has the `QuarticQuery.Paper.` prefix. Its full 2,652-name declared list is identical to the root receipt's declaration list.

| Exact declaration | In current root environment | In current headline closures | Exact name in current Comparator | Printed full type in supplied axiom log |
| --- | --- | --- | --- | --- |
| `QuarticQuery.Amplification.bounded_amplification` | yes | no | no | source + ambient variables |
| `QuarticQuery.Amplification.IndexRegister.index_law_of_amplified` | yes | no | no | source + ambient variables |
| `QuarticQuery.Upper.Samples.amplify` | yes | yes | no | source + ambient variables |
| `QuarticQuery.Paper.quantum_amplify_samples` | yes | no | no | yes |
| `QuarticQuery.Paper.equation_15` | yes | no | no | yes |
| `QuarticQuery.Paper.quantumTournament` | yes | no | no | yes |
| `QuarticQuery.Paper.quantumTournament_cost` | yes | no | no | yes |
| `QuarticQuery.Paper.quantumError_bound` | yes | no | no | yes |
| `QuarticQuery.Upper.Fkm_QLe` | yes | yes | no | source + ambient variables |
| `QuarticQuery.Upper.budget_le` | yes | yes | no | source + ambient variables |
| `QuarticQuery.Upper.Q_Fkm_le` | yes | yes | no | source + ambient variables |

The current Tournament Comparator checks `QuarticQuery.Checked.expected_weight_eq` and `QuarticQuery.Checked.expected_weight_le_half`. The Separation and Unconditional bundles compare their own family/headline wrappers. Such receipts do not separately compare `Paper.quantumTournament`, `Paper.equation_15`, `bounded_amplification`, or `Q_Fkm_le` by exact name. The final axiom audit checks 258 reviewed declarations against the allowed `propext`, `Classical.choice`, and `Quot.sound` set. A clean axiom report is not a check that theorem premises agree with the preprint.

Historical return-3 comments saying “UNELABORATED” are preserved provenance. The subsequent integrating sources and source-current root receipt supersede them as compilation evidence. Repeating those comments as the current build state would be incorrect.

## 2. The three amplification interfaces

`Amplification.bounded_amplification` quantifies over every preparation on every complex inner-product space after fixing `amplify γ η`. Its syntax contains only classical mixtures, restarts, Grover circuits and success measurements. It establishes the all-branch call cap, the complete law for phase-invariant state payoffs, the conditional state payoff, zero wrong-state mass, the promised failure bound, and certain failure at zero initial success. This is a state-level theorem in the abstract `Proc` semantics.

`Upper.Samples.amplify` instead produces `Runs` with the exact law `ampLaw`. The physical compiler measures every basis label, resets to its fixed start state, and continues with a classical label. Its theorem supplies the algorithm used by the existing headline proof, but cannot return the unmeasured full successful state.

`Paper.quantum_amplify_samples` supplies a coherent `Samples` witness with all auxiliary registers retained, and has the same exact successful-label distribution. This is a useful stronger implementation interface than the measured program, but its conclusion is still only a label law. `Samples` existentially hides the workspace and certifies `L x b = lawOf (F x (rket o)) out b`; it does not identify any designated output subsystem.

The distinction is substantive. `Samples.bind` keeps the first basis register and routes a new continuation into a direct-sum block indexed by the full output label. Successful labels can therefore be copied coherently into ancillary records. Retaining those records ensures reversibility, but by itself does not prove that tracing them out leaves a pure original good state. For example, the states `( |0⟩+|1⟩ )/√2` and `( |0⟩−|1⟩ )/√2` have the same computational-basis label law and are orthogonal; equality of a fixed label law cannot establish phase-equivalence of states.

The last justified bridge is: each Grover trial has successful component proportional to the original good vector; the measured implementation and the coherent `Samples` transport both preserve its chosen measured-label distribution. A theorem connecting the entire physical trial composition to the original output register is absent.

## 3. Exact missing state specification

A useful missing declaration would fix finite input and original-workspace alphabets, an input-independent initial basis state `o`, success predicate `S`, and a concrete family `F` with `IsCirc n F`. Let `A_x = prepOf (F x) o S`, `p_x = A_x.prob`, `M = iterationBound γ`, `N = trialCount η`, with `0 < γ ≤ 1/2` and `0 < η < 1/2`.

It must construct, uniformly before the oracle input is known, a finite record workspace `W`, an origin, a success flag on `W`, and a retained-workspace unitary `V_x` with at most `N(2M+1)n` logical reads. After a specified input-independent query-free routing/uncomputation map has placed the successful trial's original register in one designated output slot, write `Ψ_x` for the prepared state and `Π_succ` for the success projection. The required clauses are:

1. `s_x := ‖Π_succ Ψ_x‖²` lies in `[0,1]`; `p_x ≥ γ` implies `s_x ≥ 1−η`; and `p_x=0` implies `s_x=0`.
2. Whenever `s_x>0`, there is a unit vector `ξ_x` on the record workspace such that `normalised (Π_succ Ψ_x)` is phase-equivalent to `ξ_x ⊗ A_x.goodState`. Equivalently, the successful output register has reduced density matrix `|g_x⟩⟨g_x|`. The tensor factor is the complete original successful state, not just a measured index.
3. The physical compiler transports this same unitary and output subsystem on arbitrary embedded states/continuations with at most `2N(2M+1)n` ordinary bit queries. A literal equality between the enlarged global state and `A_x.goodState` is ill-typed and is not the target.
4. To recover the preprint's black-box wording, the construction/compilation must be a single parameter-only procedure using `F` and its inverse through their black-box interface. Merely choosing an arbitrary `IsCirc` witness separately for each preparation does not state this uniformity.

This is a proposed proof obligation, not a new compiled declaration. It can be expressed either through a retained pure-state factorization or through an instrument semantics preserving every phase-invariant payoff of the original output register. No existing `Samples`/`Runs` theorem can be promoted to this statement by equal successful masses alone. The quantum upper bound itself does not require closing this stronger interface gap because the successful index law suffices.

## 4. What changed since the baseline's tournament paragraph

The current `Paper.quantumTournament` now has the exact list-valued output type. Its law and query cap are chosen before `∀ x s`; every output label is a list of length at most `T`; the law is nonnegative and sums to one; and every ε-dominant `s` appears with probability at least `1−2m/2^T−Tε`. It supplies both a coherent `Samples` witness and an ordinary physical `Runs` witness with an explicit cap no greater than `6072 cc √m T² ln T`.

The proof extracts `[0,1]` comparison values from the actual comparison samplers, so this is not an extra unproved range assumption in the final theorem. The perfect indicator of the distinguished candidate is used only in the mathematical coupling proof. It does not give the algorithm access to the unknown winner. The older `Upper.tournament_runs` retains its verifier continuation, including the additional verifier ε. That earlier theorem still lies on the headline dependency path.

`Paper.equation_15` separately constructs the literal uniform-index/fresh-comparison tensor state, retaining every comparison register. `Upper.stage_samples` may stop doing later comparisons once a loss has occurred. These constructions share the successful index masses and the necessary cost order. Their complete states are not identified. The current source docstring calling `stage_samples` “the stage state of equation (15)” should be read narrowly as a sampler-law description or corrected in a later source edit.

## 5. Probability and budget boundaries

The original `IsComparison` structure gives only complementarity and a zero diagonal. It does not assert `[0,1]` range. Drift equalities are valid finite algebra under their stated premises, but their probability interpretation additionally needs nonnegative weights, positive total weight and unit-valued comparisons. `quantumStage_success` states these probability prerequisites explicitly. At zero total weight, `ampLaw` is a normalized failure law only because the amplification theorem supplies failure probability one. A formal cancellation with Lean's zero division must never be described as conditioning on a null event.

The correct charged amplification quantity is `N(2M+1)`, bounded directly by `Paper.amplification_budget_le`. A bound on `Proc.callCap`, which can be smaller than the padded charged product, would not by itself bound `stageCost` or `searchCost`.

`Samples` and `IsCirc` count logical reads; `Runs` counts ordinary bit-oracle queries. `compile_read` loads, uses and unloads the addressed bit using two physical queries, and `Samples.runs` returns `Runs (2*n)`. The exact tournament identity is `2*(T*quantumStageReads m T cc ε) = T*stageCost m T cc ε`. The factor two is included in 6072 and must not be dropped or charged twice. The natural logarithm in 6072 only changes the constant relative to the preprint's logarithm convention.

The final explicit family bound is `Q(F_{k,4^t}) ≤ budgetConst(k)·2^t·(2t)^6`, for the supplied `forrCircuit`, `k≥1`, and `t≥1`. `Fkm_QLe` has the all-input worst-case physical query cap. `budget_le` bounds that exact cap; `Fkm_forrCircuit_QLe` discharges its realizing-circuit and size premises with the explicit construction; and `Q_Fkm_le` passes to the numerical query complexity. These ordinary interfaces are not an additional open mathematical hypothesis. The fixed-parameter condition must still be retained when this bound is used for the nearly-quartic separation.

## 6. Machine-readable correspondence support

`lean_audit.json` records 530 extracted source declarations from the focused amplification, tournament, upper and Paper-quantum modules. Each record has source path, exact source signature, ambient source variables/namespace, file SHA-256, and separate current-root, exact-name Comparator and headline-reach fields. For 57 quantum declarations it also stores the complete printed elaborated type and axiom observation from the supplied native log. For other names, the JSON explicitly says that only the source signature plus ambient context was available; no elaborated type is invented. This extraction does not claim every proof was read.

Its source-read receipt distinguishes full reads from selected source passages and programmatic metadata checks. No full lower-bound, Appendix A, external-library or whole-corpus intended-statement audit was attempted by this subagent.
