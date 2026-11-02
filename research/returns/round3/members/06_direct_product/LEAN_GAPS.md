# Formal correspondence and remaining boundaries

This file follows `section.md` in reading order. No unresolved mathematical
step was found in the assigned direct-product lemma. The ordinary proofs in
this return do not acquire Lean or Comparator status from nearby theorems.

## Evidence applying throughout

The supplied native retry for `QuarticQuery.Paper.ClassicalDirectProduct`
records `passed`, exit code 0, and unchanged inputs. All six local input
hashes match the packet. The root-build receipt, final type/axiom audit,
and dependency export each record 124 local Lean/configuration hashes;
all 124 match. The audit log and generated audit-source hashes also match.
These are supplied execution records with newly recomputed byte bindings,
not newly performed Lean executions. The root `.olean` bytes are absent;
its recorded digest could not be recomputed. External dependency source
closure was not independently rebuilt in this review.

The packet commit is `1dd469dd0042b937b739da3bc211eeb60bdf7462`; the root
receipt records `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`. The labels
differ, but the recorded local build inputs have identical bytes. Source
currency is established by those bytes, not by treating the labels as equal.

The Paper module's `UNELABORATED` header and the original round-two return
describe the earlier submission. They are superseded, for the live integrated
source bytes, by the later successful receipts. Preserve historical returns;
the source owner should update the misleading live comment separately.

Seventeen relevant Paper declarations have supplied elaborated `#check`
types and axiom observations. Their recorded axioms are confined to
`propext`, `Classical.choice`, and `Quot.sound`. Other declarations in
`lean_types.json` have exact source signatures plus complete namespace and
section-variable context, and current source-build evidence, but no
declaration-specific elaborated type printout. These representations are
explicitly distinguished. None of the direct-product helpers has its own
supplied exact-declaration Comparator pass.

## 1. `CL-direct-product-statement`: equation (6.1)

`QuarticQuery.direct_product` proves the deterministic all-paths capped
endpoint for nonnegative weights. It does not need normalization or promise
support for its weighted algebra; the paper's probabilistic interpretation
does need a normalized law supported on the promise.

`QuarticQuery.Paper.classical_direct_product` proves the normalized
deterministic endpoint by the conditional-value route. Its hardness binder
is precisely the one-instance depth-$L$ hypothesis. Its `hT` binder is the
paper's separate cap, in structural form. Neither binder is an extra
unproved conjecture.

Both averaging routes quantify a **finite** seed type. They prove the full
finite-mixture version, but they do not literally quantify an arbitrary
external probability space. The ordinary finite-behavior reduction is
proved in `CL-independent-information` and already has the baseline ID
`NCL-finite-capped`. Relative to the entire canonical Lemma 4.1 wording,
the direct formal relation remains partial on that clause. Some old core
ties call the finite averaging theorem exact, while the newer Paper tie
calls it partial; the same scope distinction applies consistently to both.

## 2. `CL-product-law`: equation (6.2)

`classical_prefix_iff` proves actual-prefix equivalence with schedule
compatibility and local constraints. `classical_transcript_product_law`
normalizes that actual prefix event. `classical_transcript_mass_pos`
derives every local positive denominator from a positive global history
and nonnegative priors. The normalized identity is algebraic and has fewer
hypotheses than its probability interpretation. This is not a missing
probability assumption in the ordinary theorem: the section states the
normalized independent input law before using it.

Impossible schedules or contradictory repeated answers have no conditional
law. Lean totalizes division by zero algebraically; the section does not
mistake that convention for a probability measure. No substantive clause
of this product-law passage was found missing from the supplied components.

## 3. `CL-conditional-values`: equations (6.3) and (6.4)

The definition `classicalTranscriptValue` alone does not prove optimality.
Its exact meaning uses both `classicalTranscriptValue_attained` and
`classicalTranscriptValue_bounds_tree`. `classicalQueriesTo` counts repeated
calls; it is not the number of distinct observed coordinates.

`classical_eq_16_transcript` proves the queried-factor inequality.
`classicalTranscriptValue_unchanged` separately proves the other-factor
clause. The canonical `eq-16` row contains both, so its primary theorem
alone is partial even though the supplied components cover both clauses.
The zero-mass cancellation is established by
`classical_budgetValue_zero_mass` and `classical_branchValue`.

## 4. `CL-supermartingale`: equations (6.5) and (6.6)

`classical_transcript_conditional_expectation` states the one-step product
bound using the normalized **actual** prefix law. The finite-horizon and
iteration statements are `classical_capped_depth_uniform` and
`classical_terminalValue_le`. The terminal bound
`classical_final_bound` states both inequalities as a conjunction.
`classical_guessSuccess_query` and `classical_success_le_terminal` connect
the recursive terminal potential with actual algorithmic success.

The complete proof needs these separate components; a one-step inequality
alone is not the whole canonical supermartingale/final-bound row. The
development represents finite conditional expectations and their iteration;
it does not construct a Mathlib measure-theoretic `Supermartingale` object.
No such object or unbounded optional-stopping theorem is needed here.

## 5. `CL-independent-information`

The ordinary finite-behavior reduction for arbitrary independent information
is complete in prose. The supplied source proves the depth bound, but no
matching full probability-space pushforward theorem is supplied. The
separate-independence parity example is an ordinary four-outcome calculation,
not a Lean theorem. The joint independence of side information and coins
from the tuple is a paper premise. Neither separate marginal independence
nor an arbitrary dependence on a hidden answer meets that premise.

## 6. `CL-joint-cap`: equation (6.7)

The new ID `NCL-joint-cap` explicitly separates the generic event theorem
from the canonical all-paths theorem. No supplied generic declaration accepts
an arbitrary possibly-uncapped `OutTree` and bounds the indicator of both
correctness and its realized count event. A formal version would need path
counts, a truncation operation, its cap theorem, and agreement on cap-respecting
runs. The ordinary truncation proof is complete. No candidate Lean proof
is returned and no compilation status is assigned to this new corollary.

## 7. `CL-adaptive-example`: equation (6.8)

`checks/check_adaptive_example.py` is independently authored finite semantic
evidence. It uses exact rational arithmetic, checks 16 input tuples and four
posterior laws, and enumerates all 10 one-input and 5,188 capped two-input
trees for this tiny example. Its successful run is neither a general proof,
a Lean build, nor a Comparator receipt. The global-budget counterexample
uses total budget $rL=2$; a total budget $L$ would imply the theorem's caps.

## 8. `CL-weighted-values` and `CL-weighted-product`: (6.9)–(6.10)

These retain baseline IDs `NCL-weighted-value` and `NCL-weighted-product`.
The weighted optimum is the existing `budgetValue`, characterized in both
directions by `exists_tree_budgetValue_le` and
`treeSuccess_le_budgetValue`. The product endpoint is
`guessSuccess_le_prod`, with `guessSuccess_leaf` and `guessSuccess_query`
providing its two exact decompositions. These sources have current supplied
build evidence. Their proof route is unnormalized structural induction.

The source-current headline dependency closure reaches this core route.
It does not reach any theorem in `Paper.ClassicalDirectProduct`, although
those Paper theorems are imported and compiled. Compiled membership and
headline dependency reach are different observations.

## 9. `CL-normalization`: equation (6.11)

The individual ratio is the source definition `classicalValue` together
with its attained-maximum interpretation. The combined statement equating
history mass times normalized product with the unnormalized product is a
direct algebraic deduction from the rectangle mass factorization. It has
the new ID `NCL-product-normalization`; no single supplied declaration or
fresh Lean proof is claimed for the combined display.

## 10. `CL-planted-interface`

This paragraph restates the interface consumed by baseline §6.5. The
concrete source supplies `simTree`, `depth_simTree_le`, `eval_simTree`,
and the address-guessing theorems. Its cap is on **all target queries in
total**, hence implies each separate cap. The ordinary fixed-time event
containment is justified by the simulator's agreement before truncation.
This return does not claim a new review or build of the entire planted
lower-bound development. The unconditional hard-distribution supplier is
`exists_hard_distribution`; no additional minimax premise is introduced.

## 11. Literature and scope

The citation audit establishes exact source versions and theorem roles.
It does not certify Lean code. Drucker's global-budget theorem and
Shaltiel's uniform fair-XOR theorem are not silently substituted for
Lemma 4.1. The stronger joint-event form here is an ordinary corollary,
with no claim of novelty. No conclusion about the quantum upper bound,
Forrelation lower bound, Appendix A, or the full nearly-quartic theorem
is independently audited by this focused return.
