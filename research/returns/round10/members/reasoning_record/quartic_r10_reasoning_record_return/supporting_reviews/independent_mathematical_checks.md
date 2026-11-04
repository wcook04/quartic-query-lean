# Mathematical reconstruction before comparison with the current record

This is source-only preparatory work by the integrating reviewer. It was not supplied to the primary first-pass reader. It is not a new Lean execution, an independent human referee report, or a proof that every current-record derivation is correct. Source: the supplied OpenAI preprint, 5 October 2026, `paper/extracted.md` and `paper/source.pdf`, P0.

## Quantum interfaces to verify against the record

1. **Promise and squared amplitude.** The circuit measures a probability equal to the square of the real Forrelation amplitude. On the promised sets the two cases are separated by a fixed positive gap for fixed k. A large negative amplitude can also have a large square, but lies outside the promise; the exact transcript circuit separately checks the signed threshold. One must not extend the quantum output guarantee to that input.

2. **Fresh registers and conditional law.** For a fixed pivot history, the index register is uniform and each comparison has its own complete workspace. Conditional on index i, the all-success probability is the product of the relevant comparison probabilities. Orthogonality between different indices then yields total success W/m and index probabilities w_i/W. Independence is required within a fixed index; there is no assertion that the index and work registers are independent.

3. **Amplification and successful-state preservation.** Every Grover iterate stays in the span of the normalized successful and unsuccessful components of the same preparation. Projecting onto success therefore yields the same successful state up to global phase. Randomizing the iteration count and taking the first successful fresh trial preserve the conditional state. The number of attempts is capped even when p=0 or p is below the promised amplification threshold.

4. **Local coupling rather than global postselection.** The sampler's failure probability may depend on the full pivot history. At each common history, its conditional successful index law equals the ideal pivot law. Couple one stage at a time and charge the conditional failure probability before the true winner enters the list. Conditioning the entire actual run on avoiding abort need not reproduce the unconditional ideal history law.

5. **Fractional weights.** Complementarity for distinct candidates and a zero diagonal imply that the weighted double sum is half the off-diagonal product sum. Thus the expected new total weight is `(W^2 - sum_i w_i^2)/(2W)` when W is positive. A high-reliability winner retains weight greater than one half until selected. No transitive order on all candidates, rounding of probabilities, or deterministic tournament oracle is used.

6. **Verification direction.** The search marks failures of exact local tests. A valid certificate never yields a marked failure. An invalid certificate can be accepted only if the capped failure search misses a marked test. The winner can still be lost through fresh address decoding; that error must remain separate from the exactness of the checks.

## Classical interfaces to verify against the record

1. **Minimax quantifiers.** A finite family of depth-L trees gives a compact simplex of randomized strategies. If L is below randomized complexity, the attained maximum worst-case success is strictly less than two thirds. A hard distribution with deterministic success at most two thirds follows. It need not have exactly balanced output labels.

2. **Adaptive product law.** At a fixed complete deterministic transcript, the event that produces it is a product of the observed-coordinate constraints on the separate target inputs. The query schedule is already determined by those observed answers. This is why adaptive interleaving preserves the product of the conditional input laws. Conditioning on being a light column is a different event and is not licensed by this argument.

3. **Remaining-budget value.** The potential for one coordinate is the optimal prediction success with the remaining permitted queries. Its conditional expected value cannot increase after a particular legal query and optimal continuation. Multiplying potentials works because a query changes only one factor and the other conditional laws are unchanged. A fixed finite horizon allows early stopping to be padded; no unproved optional-stopping hypothesis is needed.

4. **The address guess is made before reading the cell.** For fixed column i and query ordinal t, the capped simulator stops before exceeding the total target-column budget and outputs the address of the proposed t-th cell query. On the joint event of a correct-address visit and a nonheavy column it guesses the complete true address. This event inclusion is sufficient; the simulator need not know that it is on the joint event.

5. **Average over the planted column.** Union bound over query ordinals first, then average over an independent uniformly chosen planted column. This leaves a G times beta-to-the-r term; a further factor of m is not required. The heavy-column and erased-zero terms are charged separately.

## Global interfaces

The universal exponent statement fixes each exponent below four, then chooses a sufficiently large fixed k, then lets m tend to infinity. A logarithmic factor is beaten by the resulting positive power of m. Allowing k to grow with m requires additional uniform information; it is not a consequence of merely having a constant and threshold for each fixed k.

The universal quartic upper bound uses three logically distinct inputs: the spectral adversary lower bound, the signed-cube degree estimate, and deterministic complexity bounded by degree times block sensitivity. For the last step, each iteration queries a maximum-degree monomial of the current restriction; a sensitive block at the same original input is charged to each iteration. The blocks are disjoint because the queried variable sets are disjoint.

The returned specialist checks will decide whether any of these interfaces are actually missing, incorrect or unnecessarily hard to reconstruct in the current record. Their presence here is not a finding.
