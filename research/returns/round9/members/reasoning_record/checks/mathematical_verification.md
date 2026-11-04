# Mathematical verification: actual checks and limits

This is a record of scoped reasoning and source inspection, not a correctness certificate. It follows the frozen encounters. Exact primary-source editions and passages are in `checks/sources.json`; lead section labels refer to the current source bound by `coverage.json`. No historical computational checker, Lean build or Comparator run was repeated.

## Classical checks

The following checks concern lead §§3.7–3.15, 6 and 7.3. Source comparisons are to the exact BS-v3, Drucker-v2, Shaltiel-TR01-009, GTW-v2 and SSW-v4 records in the ledger, not to unspecified later editions.


### Gaussian comparison and tree growth

I checked the algebraic identities for φ and Ψ, the product bound Ψ(x)φ′(y)≤3/16, and the bounded integration-by-parts argument. The uniform ν0 endpoint uses ordered reflection/clearing inside the multilinear extension; it does not assume that U and HU are independent. The k=3 expansion supports the general derivative-propagation invariant. Its stated range should exclude the terminal block, where no remaining X factor exists.

The path map is injective as a map to sets of **block-coordinate pairs**, so applying the derivative-growth bound introduces no k! factor. Higher uniform Fourier degrees remain inside raw biased derivatives, as F24 records. The polynomial mean value theorem is applied to one averaged scalar function hg, yielding a common interpolation point for its entire derivative expression.

For the tree martingale, I checked the fresh-coordinate cylinder law, treatment of charged repetitions, contracted coefficient arrays, bounded increments, finite stopped exponential process and recovery of the absolute derivative sum from a fixed sign array. The key safeguard is predictable stopping before a coefficient bound fails. Conditioning on the later good event would not preserve the martingale law. This is the relevant comparison with Girish–Tal–Wu’s ordinary-tree discussion, arXiv: 2103.11604v2 §1.3 and Lemma 1.9; I did not read their complete parity-tree proof.

The hard mean lower bound uses ETp=0 and exp(−Tp)≥1−Tp after a pointwise kernel estimate. It needs only marginal second moments of selected U and V coordinates, so no independence inside a Gaussian pair is smuggled in. The amplification estimate is pointwise in a fixed promised input and uses independent algorithmic coins. F41 bounds an acceptance probability on **every** input; no law is conditioned onto the promise.

The numerical F43 assembly is consistent: τ=25k gives ε≤ak/18, the dimension condition gives uniform-law leakage at most δ, δ≤ak/32 yields the gap 119ak/144, and the upper comparison is at most 7ak/12. Excluding D=0 is needed before absorbing the added one in the depth parameter. In F49 the short omitted chain is b/√m≤1/18 and 2^−k≤1/4. The threshold 13669k² is sufficient and deliberately nonminimal.

### Minimax, direct product and planting

The finite closest-pair argument gives a distribution on the promised domain after P and L are fixed. It is independent of the analytic Gaussian comparison distribution. The strict positive separating margin is common to the finite set of depth-L trees; it does not claim a single law hard for every cap or error parameter.

The direct-product theorem uses per-input caps on every execution and joint independence of side information from the whole target tuple. At one fixed compatible history, the remaining input law factors. The terminal product bounds a **conditional probability**, not a realized success indicator. Truncating an arbitrary algorithm gives a bound on success intersected with cap compliance; conditioning on compliance is a different assertion and is false in the supplied AND example. The example’s conditional successes 1, 1/2, 1/2, 1/4 give joint mass 5/16 and conditional success 5/8, exceeding (3/4)². A global allowance rL is also not equivalent to separate L allowances.

I checked the first-difference coupling, the use of a full-cell visit as an overcount of a changed-bit query, and the identity Pr(hit the selected zero)=EZ/m. A uniform marginal for I is insufficient: independence from the full dummy run is essential. The four-column counterexample gives 175/256 for the dependent selector.

The early/late zero-search proof gives EZ≤4G/m. The optional worlds induction and all-one reference path supply the stronger expectation-cost inequalities stated in the record. Their query set needs clearer notation: varying only X means that A and B, including the selected column’s fields, are fixed side data. The reference-path scan demonstrates sharpness of an expectation-cost inequality; it does not establish a full success curve for every worst-case budget.

The target-column simulator enforces one shared L-call allowance, stronger than the r separate allowances required by the theorem. It outputs an address from the proposed coordinate label before reading the cell. The cheap true-cell event is contained in simulator success, since the default may also be correct. Unioning over original query times **inside** the average over independent I yields G(2/3)^r with no additional m factor. The XOR trace’s joint mass 1/8 and unconditional simulator success 1/4 agree with this containment.

The finite discrepancy calculation, both floor losses and the 1/400 coefficient check out. For the optional Drucker substitution, the exact replacement tail is 2/(100m^8); using m≥4 before coarsening keeps it below 1/100, so the 6/100 claim is valid. The record should show that one-line bridge. The fixed-k exponent argument requires α<4−2/k. The endpoint is not proved by the displayed quotient, as the record acknowledges.

The growing-k assembly uses a different cap L=floor X obtained directly from F43. I checked the integer improvement R>floor(y)⇒R>y for integer R, the floor penalty 40(x−k)²/k<20, and the aggregation giving 28 log₂ℓ+237. The extra relaxation from 474 to 508 is sufficient but its purpose is not explained. Existing estimates also imply Q(Ft)→∞ through the quartic upper bound; stating this would make the asymptotic family interpretation explicit.


## Quantum checks

The following concern lead §§2–5 and Appendix A, with selected original source statements listed under Q-S02 through Q-S11.


The checked geometry gives the same good vector on every successful Grover branch, and the later routing argument correctly describes a subsystem of the enlarged workspace. The finite-label law is deliberately weaker than a full-state assertion. The record already distinguishes this from the measured/reset implementation; it must not be reported again as an unacknowledged formal equivalence.

The exact Grover average has denominator 4M sin(2θ), while the later proof deliberately uses a weaker denominator-two inequality. The constant 138 and padded 6072 factor were followed as upper bounds. The ordinary kq decoder and the compiled 2qk construction likewise need evidence separation, not a claim that one is an arithmetic error. The ordinary theorem does not require fair-coin-only sampling. The OR endpoint example correctly exposes the exact 2/3 issue.

The tournament drift uses a fixed oracle and fresh comparison registers. Its complementarity need not encode any transitive ordering or noisy fixed edge bit. The dominant weight remains above one half before selection, so only preselection sampler failures enter the Tε coupling charge. No independence of those stage failures is required. A selected vertex obtains weight zero, and the process cannot repeat it on positive-weight steps. The cyclic and fractional examples were checked without treating them as realized Boolean boards.

The local verification construction is exact at every address. A false address or off-promise instance does not invalidate its test list. The four-column generic example uses r=2 and its own finite circuit, already explicitly distinguished from the separation family. The test count 371 and total bit count 5936 are consistent with that variant. The support/depth distinction is correct; its issue is placement.

Appendix A’s prefactor discussion was checked against the original publisher theorem and the Høyer–Lee–Špalek author PDF. The factor-two discrepancy is genuinely present in the inspected printed formula; the record’s own coefficient and parity witness agree with its progress proof. No author-confirmed erratum is claimed. The lead’s ABKRT Lemma 9 locator is correct in the original v1 PDF; the flattened extraction’s different numbering must not be used to “correct” it. The signed-cube argument and sensitive-block decision-tree calculation were followed without establishing a new defect.

## Formal sources: evidence boundary

Read selected model/target ranges in `Challenge.lean` and selected amplification, compiler and tournament declarations listed in `sources.json`. The `Paper/QuantumAmplification.lean` and `Paper/QuantumTournamentFacts.lean` wrappers carry explicit unelaborated notices. Their declarations were inspected as source statements. The existing `Upper/Samples.amplify` interface describes a measured output law. No Lean process, Comparator process or historical receipt was rerun. The generated challenge’s `sorry` placeholders are not interpreted as an absence of implementation proofs.


## Formal statement and receipt inspection

`checks/formal_statement_checks.json` records the textual target comparison, forwarding sources and configuration inspected. Four Challenge/Solution types matched after whitespace normalization. That does not perform elaboration or establish equality of all dependencies. The configuration permits the three recorded standard axioms; actual process results are historical receipt data.

The historical paranoid Unconditional receipt reports passed, four declarations, toolchain 4.36.0-rc2, and an unsandboxed command. Seventy present source files match its recorded hashes; 154 referenced source paths are absent from the selective packet. Their absence is a scope limit, not evidence that the ZIP is corrupt. The narrative pin inconsistency is separately checked against the 126 current Lean reference definitions.

## Excluded conclusions

No counterexample to the main separation theorem was found. This is weaker than proving all arguments correct. The two BS source-display defects and the adversary-prefactor edition discrepancy concern inspected displays; they do not justify an unqualified claim that their entire source theorems are false. The source paper’s original theorem-numbering was checked where extraction macros could produce a false locator complaint. Stronger external algorithms and minimax theorems were contextual comparisons only.
