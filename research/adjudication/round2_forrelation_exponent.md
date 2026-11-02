# Round-two uniform Forrelation and single-family adjudication

The sharp scalar coefficient `3/16` yields a uniform Forrelation lower bound with
constant `2/18225`, a factor `256` above `1/2332800`, under the existing dimension
condition `k ≥ 2`, `m = 4^t`, `15k + 2 ≤ 2t`. The live source now contains the
scalar, path, advantage and parameter assembly for that endpoint, preserving the
older theorem interfaces. **Compilation is pending at this draft checkpoint.**
The existing repetition decoder also admits the exact budget expansion and the
envelope `B10(k) ≤ 2^53 k 2^(10k)` for `k ≥ 1`; source for both is added.

This file adjudicates returns `6_sharp_uniform_forrelation` (54 statement
records, eight change records) and `7_single_family_exponent` (32 statement
records, no changes to existing statement IDs). Original return bytes are
preserved. These are substantive advisory research returns, classified
`parent_advance_incomplete`: they contain useful ordinary proofs, but neither
claims new Lean execution. Neither the new SSW endpoint nor the BHMT-based total
function theorem is treated as compiled. The existing unconditional fixed-order
quartic-exponent theorem is unchanged.

## Exact live proof delta

- `ForrelationLower/Stein.lean`: `psi_dphi_le_sharp` and equality at zero. If
  `qx² ≥ 2`, `qy² ≥ 2`, then `qx qy ≥ 2` and `qy⁴ ≥ 4`, whence
  `2 qx qy⁵ ≥ 16`. This checks the product, rather than multiplying the previous
  loose individual bounds `1` and `3`.
- `ForrelationLower/Walk.lean`: `abs_cf_le_sharp` groups those two scalar factors
  at each path edge. It requires only a bound on the matrix entries, not
  orthogonality.
- `ForrelationLower/Cascade.lean`: `advantage_le_sharp` uses the existing
  mean-value interpolation identity, path injectivity and decision-tree growth
  estimate. The old `advantage_le` is retained as a weaker corollary.
- `ForrelationLower/Main.lean`: `not_RLe_of_gap_sharp` retains the old promise
  comparison and error `1/3` amplification. The old `not_RLe_of_gap` remains a
  corollary with its original type.
- `ForrelationLower/Uniform.lean`: `main_term_le_sharp` reuses the old arithmetic
  at `lg/256` and `K/16`. Multiplication by `16` converts its `a/48` bound to
  `a/3`, where `a = 18^(-(k-1))`. `not_RLe_uniform_sharp` combines that with
  the old residual bound `a/4`. The available promise gap is at least
  `119a/144 > 7a/12`. `forrelation_lower_uniform_sharp` applies this contradiction
  at the actual minimum budget `R(P k t)`, avoiding a second floor argument. `uniform_budget_floor_bounds` adds the
  auxiliary cutoff bounds `X ≥ 2`, `1 ≤ floor X ≤ m`, and `floor X ≥ X/2`
  for `k ≥ 2`, `k ≤ t`, `t ≥ 41`. The exact induction base is
  `2^41 = 2199023255552 ≥ 27993600*41^3 = 1929346905600`; its predecessor
  fails that conservative estimate. This improves the sufficient `64` in the
  return and feeds the generic planted lower theorem.
- `Upper/Bound.lean`: `budgetConst_eq_expanded`,
  `budgetConst_le_exponential`, and `Q_Fkm_le_exponential` expose the existing
  repetition algorithm's dependence on `k`. They do not change its decoder.

The uniform endpoint in this delta is

```
∀ k t : ℕ, 2 ≤ k → 15*k + 2 ≤ 2*t →
  (2/18225) * m^(1 - 1/(k:ℝ)) / ((k:ℝ)^2 * log(4*k*m)) < R(P k t),
where m = mValue t = 4^t.
```

The abstract Fourier-input endpoint
`η²/(162 e C²) [m/(1+ln(km))]^(1-1/k)` and the smaller sufficient dimension
`m ≥ 24 k 32^(2k)` remain ordinary mathematical deductions. They require an
explicit SSW hypothesis and a new null-tail argument; the live theorem above
uses neither as an unproved import.

## Executed probes and evidence boundary

Both return scripts were inspected before execution. Their imports are from the
Python standard library; neither launches processes, uses the network, nor
writes files. Return 6 reads its own metadata to check anchors and dependency
IDs. The following commands completed with exit zero on 2 November 2026:

```
python3 research/returns/round2/6_sharp_uniform_forrelation/checks.py
python3 research/returns/round2/7_single_family_exponent/checks.py
```

A second execution redirected each output to `/tmp` and `cmp` confirmed
byte-for-byte agreement with its submitted `checks_output.txt`. Return 6 checks
exact rational/integer identities, all levels for `2 ≤ k ≤ 64`, the omission of
free probabilities as a negative control, and finite endpoint-norm examples.
Return 7 checks exact budget expansions, circuit recurrences, floor transfer,
schedule discontinuities and rational amplitude-estimation margins. Its exponent
tables and nearby-`k` scans use floating point and are illustrative finite
numerical evidence, not enclosures, actual complexities, global optima or
asymptotic certificates. No analytic lemma follows merely from those tests.

Return-6 `checks.py` SHA-256:
`4c2a224447af3433992b9dc23d4edb452923218e35d8e7cf35a29c89be50ed49`.
Return-7 `checks.py` SHA-256:
`71a311c33b9a09182d9ed82b37f2540f326affe22f0bdc182cd0f47023bcb446`.

Focused build checkpoint: the original governed request for
`QuarticQuery.ForrelationLower.Stein` was deferred with exit `75`, job
`cf_a603fc09c674403bbb2e`, then cancelled through the owner API before a Lean
child started. Its terminal receipt is `cancelled`, exit `130`; stdout is empty
and stderr contains only capacity waits. The separate Section4 diagnostic
subsequently exhausted its 1500-second seat budget with exit `117`, without
proof diagnostics. These are execution/admission outcomes, not theorem verdicts.
After its process group ended, the scalar attainment rewrite, explicit path
multiplication/positivity, and B10 multiplication bound were repaired.

Exactly one native targeted build is now queued as
`cf_bf3d0271e57c43479b86`: ordinary guarded
`lake build QuarticQuery.ForrelationLower.Uniform QuarticQuery.Upper.Bound`,
through `command_future --lean-host-admission`, with 41 local source/configuration
paths and a 7200-second admitted seat budget reflecting the observed cold-cache
cost. The source closure is frozen. Candidate hashes were refreshed after the
repairs. The initial state is `waiting_host_admission` behind the disjoint
construction/quantum batch. The terminal result and parent-controlled root
build are required before recording kernel acceptance. No new Comparator
receipt is claimed here. No commit is made in this lane.

## Primary-source adjudication

The actual public v3 [Bansal–Sinha full text](https://arxiv.org/html/2008.07003v3),
§5.4, confirms both reported issues. The preceding Fourier expression has
logarithmic exponent `(ell-1)/2`; the next displayed upper expression uses
`ell(1-1/k)/2`. Their difference is `(ell/k-1)/2`. At
`ell = k(k-1)` it is `(k-2)/2`, positive for `k ≥ 3`. With amplified depth
proportional to `N^(1-1/k) / log(kN)^(1-1/k)`, the last term of the former bound
grows as `log(kN)^((k-2)/2)`, while the proposed finite sum stays bounded.
This rejects that displayed implication; it does not refute the lower-bound
theorem or compute a decision tree's actual advantage. Retaining the displayed
multilevel estimates gives logarithmic denominator exponent
`1 - 1/[k(k-1)]` as a sufficient replacement. Equation (5.31) separately prints
`delta²/(4N)` where the preceding exceptional-mass estimate supplies
`4/(N delta²)`. Both defects must stay separate.

The [SSW v4 primary text](https://arxiv.org/html/2008.10223v4) gives the required
Fourier-weight bound for `[-1,1]`-valued depth-`d` trees and one absolute `C ≥ 1`.
The HTML calls these Corollaries 4.12–4.13; the return's PDF locators 4.14–4.15
must not be interchanged without noting the representation. This is an external
mathematical input, not a local Lean declaration or a numerical value of `C`.

[BHMT, Theorem 12](https://arxiv.org/pdf/quant-ph/0005055), printed p. 19, supplies
the probability and estimation-error theorem used in return 7. The proposed
retained-workspace circuit and controlled-query accounting are a new local
composition. A bounded-error `QLe` statement alone does not supply the coherent
`Samples` interface used by the addressed verifier. The Grover iterate's minus
sign, inverse sampler, retained estimate register and all-input query cap must
be represented. The return correctly keeps these obligations explicit.

No author correspondence, human review, independent theorem acceptance or
exhaustive erratum search is asserted. Source names and method credit remain
Bansal–Sinha for the chain antecedent, Girish–Tal–Kewen Wu for the elementary
martingale route, SSW for the Fourier input, BHMT for amplitude estimation, and
OpenAI for the total function construction and nearly quartic separation.

## Disposition vocabulary

`existing` means the cited live source already supplies the restricted local
claim. `landed-source` means a proof was added by this lane; the build checkpoint
above determines whether it is kernel evidence. `ordinary` means the argument
survives source and mathematical inspection but has uncompiled formal
obligations. `partial` identifies a strictly narrower live statement. `external`
means an identified primary theorem that remains a hypothesis for local
formalization. `audit` means an exact source/algebra finding, not a theorem about
optimal query complexity. The original `NEW_STATEMENTS.json` and change records
retain the complete proposed types; this table is a disposition crosswalk, not
a new statement corpus.


## Every returned statement

### Return 6

| Statement ID | Disposition | Exact scope |
| --- | --- | --- |
| `r2-sharp-ssw-input` | external | SSW Fourier estimate; no local proof of existence of its absolute constant. |
| `r2-sharp-sharp-result` | ordinary | Full variable-error and improved-dimension theorem; requires restriction transfer, SSW and tail assembly. |
| `r2-sharp-elementary-result` | partial | landed-source endpoint at m=4^t and old threshold; smaller tail threshold and arbitrary powers of two remain ordinary. |
| `r2-sharp-scope` | ordinary | Exact n=km substitution; no removal of the k factor when measuring total length. |
| `r2-sharp-extension` | partial | Cube ext/D/Dl algebra exists; the packaged Fourier expansion wrapper remains uncompiled. |
| `r2-sharp-kernel` | landed-source | Sharp product and equality added to Stein; existing derivative/oddness/bias bounds reused. |
| `r2-sharp-stein` | existing | stein_one has the required bounded/continuous derivative hypotheses. |
| `r2-sharp-chain` | partial | wv and endpoint half bound exist; quarter bound for interior coordinates remains a small formal obligation. |
| `r2-sharp-zero-endpoint` | existing | integral_ext_wv_zero under RowsOrth; chain length and orthogonality remain hypotheses. |
| `r2-sharp-path-identity` | partial | Existing exists_identity is a mean-value identity; literal integration in s needs its own regularity proof. |
| `r2-sharp-worked-chain` | ordinary | k=3 expansion and Fourier differentiation are finite identities, not new compiled wrappers. |
| `r2-sharp-advantage` | landed-source | advantage_le_sharp uses the mean-value form sufficient for the endpoint. |
| `r2-sharp-moments` | partial | Walsh mass_ge and uniform moments exist; broader arbitrary-orthogonal statement is uncompiled. |
| `r2-sharp-subgaussian` | ordinary | Endpoint conditioning gives coefficient norm 1/m pointwise; MGF and two-sided exponential tail remain to formalize. |
| `r2-sharp-gap` | ordinary | Exact denominator 1-delta, min-tail and improved Gamma* are sound; live finite proof deliberately retains the weaker old gap. |
| `r2-sharp-restriction` | ordinary | Identity without division includes v_i=0; probability interpretation also needs v_i>=0 and |mu_i|<=1-v_i. |
| `r2-sharp-path-restriction` | ordinary | Common product is (1/4)(3/4)^(k-2); no path-multiplicity factor; SSW remains explicit. |
| `r2-sharp-growth` | partial | Parameterized tree growth is local; the compact specialized display is not separately formalized. |
| `r2-sharp-growth-proof` | existing | sum_abs_ext_Dl_le supplies the parameterized stopped-process route; no conditioning on a future good event. |
| `r2-sharp-amplification` | partial | exists_amplified covers source error 1/3; variable eta and eta=1 endpoint are ordinary. |
| `r2-sharp-finite-elementary` | partial | not_RLe_of_gap_sharp covers error 1/3 with padded depth and conservative Markov gap; full Gamma*/eta interface remains ordinary. |
| `r2-sharp-finite-sharp` | ordinary | Binomial Fourier inequality and inversion depend on unformalized SSW/restriction interface. |
| `r2-sharp-threshold` | ordinary | Smaller exponential-tail threshold sound; no new tail theorem in the live Lean delta. |
| `r2-sharp-sharp-proof` | ordinary | Variable-error ceiling/cancellation gives 1/(162 e C^2); no local kernel theorem. |
| `r2-sharp-elementary-proof` | partial | main_term_le_sharp and old-threshold assembly landed; improved-tail version remains ordinary. |
| `r2-sharp-original-constant` | landed-source | forrelation_lower_uniform_sharp preserves old dimension condition and gains exactly factor 256. |
| `r2-sharp-finite-range` | ordinary | Equivalent Markov-gap positivity criterion with positive denominators; not a necessity theorem for all methods. |
| `r2-sharp-small-dimension` | ordinary | Empty no-promise at m=1 and m=2,k=2; second example is outside current powers-of-four family. |
| `r2-sharp-comparison` | ordinary | Distinct elementary/Tal/SSW consequences; no optimality claim for residual log loss. |
| `r2-sharp-bs-failure` | audit | Public v3 display has the asserted exponent mismatch; repaired exponent concerns its bound expressions. |
| `r2-audit-bs-sum-counterexample` | audit | Exact exponent algebra and asymptotic comparison of two upper-bound sums; not an actual decision-tree counterexample. |
| `r2-audit-bs-gap-geometric` | audit | Reciprocal correction and geometric tail bound are sound ordinary deductions; source theorem imports are separate. |
| `r2-impl-kernel` | landed-source | psi_dphi_le_sharp and psi_dphi_eq_sharp_at_zero. |
| `r2-impl-bias` | ordinary | Interior quarter bound not added; existing half bound suffices for landed endpoint. |
| `r2-impl-coefficient` | landed-source | abs_cf_le_sharp. |
| `r2-impl-growth` | partial | Parameterized growth reused, specialization is not a new local declaration. |
| `r2-impl-advantage` | landed-source | advantage_le_sharp. |
| `r2-impl-restriction` | ordinary | Coordinate-dependent exact finite identity remains a formalization task. |
| `r2-impl-weights` | ordinary | Weights are nonnegative and sum to one under stated inequalities; no compiled interface. |
| `r2-impl-tree-restriction` | ordinary | Depth cannot increase after fixing variables; no compiled restricted-tree wrapper added. |
| `r2-impl-profile` | ordinary | Quarter interior bias and common path product remain uncompiled. |
| `r2-impl-endpoint-norm` | ordinary | Norm-preserving diagonal/orthogonal product; exact finite script is supporting evidence only. |
| `r2-impl-linear-mgf` | ordinary | cosh(v)<=exp(v^2/2) and independence argument not compiled here. |
| `r2-impl-forrelation-tail` | ordinary | Requires endpoint norm, MGF and exponential Markov; not implied by second moment alone. |
| `r2-impl-amplification` | partial | Existing fixed-error construction only; arbitrary advantage is uncompiled. |
| `r2-impl-gap` | ordinary | Exact mass/gap abstraction not added; old weaker comparison remains sufficient. |
| `r2-impl-finite-elementary` | partial | Sharp padded fixed-error contradiction landed, broader return signature uncompiled. |
| `r2-impl-arithmetic` | partial | Scaled main bound landed; old tail bound reused rather than smaller local t>=2 wrapper. |
| `r2-impl-elementary-endpoints` | partial | Old-threshold sharp endpoint landed; subgaussian threshold remains ordinary. |
| `r2-impl-ssw-input` | external | No axiom or opaque import added; retain explicit Fourier hypothesis. |
| `r2-impl-path-profile` | ordinary | Requires bias/restriction wrappers and explicit external Fourier hypothesis. |
| `r2-impl-finite-sharp` | ordinary | No compiled binomial inversion or full variable-error wrapper. |
| `r2-impl-sharp-arithmetic` | ordinary | Ceiling and k-cancellation arithmetic independently checked; no local Lean result. |
| `r2-impl-sharp-endpoint` | ordinary | Full SSW endpoint is a live residual, not implied by the elementary theorem. |

### Return 7

| Statement ID | Disposition | Exact scope |
| --- | --- | --- |
| `sf-uniform-forrelation` | existing | The coarse theorem is in Uniform; this lane also adds a stronger sharp endpoint under the same hypotheses. |
| `sf-uniform-parameters` | existing | Coarse Uniform parameter proof reused; sharpened coefficient assembly is separate. |
| `sf-floor-budget` | partial | uniform_budget_floor_bounds now supplies X>=2 and all floor bounds for k>=2,k<=t,t>=41; its displayed intermediate fraction is not separately packaged. |
| `sf-floor-transfer` | ordinary | Integer R>floor(x) implies R>x. First floor loses factor at most two; no second factor is permitted. |
| `sf-planted-numerical` | existing | Results/Exponent.twoThirds_pow_le and discrepancy_le already supply this for generic L. |
| `sf-total-lower` | ordinary | Use generic Gvalue_lt_R_addressedF with L=floor X; stronger fixed-L corollary is unnecessary. |
| `sf-schedule` | ordinary | Both floor-sqrt schedules satisfy conditions for t>=80; no schedule theorem added here. |
| `sf-T-and-repetitions` | ordinary | Exact Tval identity/refined substitution differs from existing upper bound Tval_mValue_le. |
| `sf-B10` | landed-source | budgetConst_eq_expanded and budgetConst_le_exponential, with Q_Fkm_le_exponential consumer. |
| `sf-circuit-arithmetic` | ordinary | Existing size bound suffices; exact recurrence/closed formula remains uncompiled. |
| `sf-amplitude-estimation-interface` | ordinary | BHMT theorem checked in primary source; retained coherent local implementation and compiler cap remain unproved. |
| `sf-AE-margins` | ordinary | 25/64 and 47/64 margins checked rationally; this is not a proof of BHMT. |
| `sf-majority-quarter` | ordinary | Chernoff comparison gives (3/4)^h for 2h runs with ties counted as errors; no formal wrapper added. |
| `sf-AE-decoder` | ordinary | 128 abstract reads versus 256 physical cap correctly separated; local Samples proof missing. |
| `sf-AE-decoder-runs` | ordinary | Requires executable retained law, not just bounded-error QLe existence. |
| `sf-generic-decoder-composition` | ordinary | Current decode_samples and addrLaw are hardwired; rebuild address/comparison/verification laws parametrically. |
| `sf-AE-budget` | ordinary | B5 arithmetic is conditional on the new decoder and composition; no compiled Q upper bound with 2^(5k). |
| `sf-AE-count-arithmetic` | ordinary | Finite exact ceiling-envelope checks pass; universal formal arithmetic remains. |
| `sf-input-cardinality` | ordinary | Sum/product/subtype cardinality derivation matches actual BitLoc roles; no new cardinality proof added. |
| `sf-input-envelope` | ordinary | Uses existing circuit-size bound; cannot claim exact arbitrary-length padding. |
| `sf-generic-quartic` | partial | Appendix proves source finite-coordinate result; transport to actual BitLoc must remain explicit. |
| `sf-exact-exponent-5` | ordinary | Positive A and denominator require total lower and new B5 route; not actual complexity evaluations. |
| `sf-finite-rate-5` | ordinary | Depends on missing BHMT decoder/composition and common schedule, not merely fixed-k bounds. |
| `sf-exact-exponent-10` | ordinary | Can use existing repetition decoder; remaining lower/floor/schedule/log composition is explicit. |
| `sf-finite-rate-10` | ordinary | Strongest no-BHMT next baseline: coefficient 8 sqrt(10), remainder (56 log2 s+524)/s. |
| `sf-balancing` | ordinary | Exact rounding correction 2(k-x)^2/(k x^2) cancels first-order floor error; finite script supports arithmetic. |
| `sf-log-bounds` | ordinary | Lower A>=s/2-30>0 for s>=160 is sound; no elaborated wrapper. |
| `sf-log-upper-and-deficit` | ordinary | Denominator lower bound s/2 and positive numerator are necessary for division directions. |
| `sf-input-log-envelope` | ordinary | 22s<=log2 n<=22s+4log2 s+14 under circuit/schedule bounds; not a count of columns. |
| `sf-limit-and-input-size` | ordinary | Q diverges from growing R plus universal quartic bound; limit and input-size squeeze remain uncompiled. |
| `sf-diagonal-from-fixed-k` | ordinary | Already follows by choosing common increasing thresholds; no explicit rate claimed from fixed-k theorem. |
| `sf-square-root-barrier-for-estimates` | ordinary | AM-GM gives lower bound 8 sqrt(a)/sqrt(s) for these estimates only; not an algorithmic impossibility theorem. |

## Change records and historical corrections

All eight return-6 change records are accepted with these boundaries:

| Change ID | Verdict |
| --- | --- |
| `r2-sharp-gap` | Stronger certified gap `Gamma*` is correct; live endpoint needs only the older smaller gap. |
| `r2-sharp-finite-sharp` | Same upper bound also bounds `Gamma*`; inversion requires positive gap, positive constants and the explicit SSW input. |
| `r2-sharp-finite-elementary` | Arbitrary-advantage/gap extension is mathematically sound but broader than the landed fixed-error theorem. |
| `r2-sharp-restriction` | Equivalent identity without division includes zero free probabilities. Probability nonnegativity is an additional interpretation condition. |
| `r2-sharp-bs-failure` | Accepted correction to the displayed implication, without declaring Theorem 1.3 false. |
| `r2-audit-bs-gap-geometric` | Accepted reciprocal correction; retain the preceding mass theorem's hypotheses. |
| `r2-sharp-sharp-result` | Smaller sufficient dimension from the subgaussian null tail is accepted as ordinary mathematics; full error and SSW hypotheses remain explicit. |
| `r2-sharp-elementary-result` | Same sharp constant under the smaller sufficient dimension is ordinary; only the old-threshold powers-of-four specialization is implemented here. |

All eight change IDs were checked against the original JSON. Return 7 has an intentionally empty
`STATEMENT_CHANGES.json`: its uniform-in-order, coherent-decoder and single-family
claims are proposed additions, not rewrites of the preprint's fixed-order
statement. Its historical build caveats are correct about the received packet;
a new local build supersedes those status observations only for the exact
modules and bytes actually compiled. No stale recorded commit is promoted to
current evidence.

## Next proof consumers, in dependency order

1. Compile the sharp elementary endpoint and exact existing-decoder budget.
   Both improve named live consumers while preserving statement meaning.
2. For the single-family baseline, consume `uniform_budget_floor_bounds`
   (which supplies the needed bounds from `t ≥ 41`), then instantiate the generic
   planted theorem at `L = floor X`. Here
   `X = m^(1-1/k)/(2332800 k² ln(4km))` already suffices. This gives total lower
   constant `1/466560000`, with one floor loss. The new sharp endpoint permits a
   stronger constant after the same proof. Do not use the unnecessarily strong
   fixed-`Lvalue` threshold `t ≥ 3499200 k²` for a growing square-root schedule.
3. Combine the repeated decoder's explicit `2^53 k 2^(10k)` bound with
   `k = floor sqrt(t/20)`, `t ≥ 80`, the generic lower bound and the logarithmic
   squeeze. This can establish the explicit rate with leading
   `8 sqrt(10)/sqrt(2t)` independently of BHMT. A fixed-order diagonal sequence
   proves bare existence with no explicit rate and remains a distinct deduction.
4. For the sharper SSW Forrelation theorem, first formalize finite
   coordinate-dependent restrictions, depth preservation and the path profile;
   retain the external Fourier theorem as `hFourier` until it is proved. The
   improved dimension needs conditional endpoint norm plus the MGF/tail proof.
5. For the `8 sqrt(5)` rate, the precise missing quantum edge is a reindexable
   retained `Samples` decoder on every coordinate map, error at most `eta` on the
   promise, and an all-input physical query cap
   `256*k*2^(5*k)*ceil(log(1/eta)/log(4/3))`, together with a generic addressed
   composition theorem consuming it. Its abstract cap can be `128` before the
   factor-two physical compiler. No numerical substitution into the hardwired
   existing `Fkm_QLe` supplies that theorem.

These residuals are source-current candidates for the next campaign. No new
packet is prepared before the entire current batch is assimilated and validated.

## Mathematical consequence handoff

- Canonical mathematics: the sharp coefficient/endpoint and B10 arithmetic live
  in Lean source; this note records the complete return dispositions and exact
  still-ordinary claims.
- Prior art and credit: primary source loci checked above; all numerical
  constants and the power-of-four domain remain explicit. The SSW constant is
  not assigned a numerical value. No novelty or optimality verdict is inferred.
- Lean obligations: exact declarations and pending builds are named above;
  imports alone are not proof evidence.
- Paper: return manuscripts are preserved as research. Updating public prose
  requires the final build boundary and a separate manuscript review; the
  smaller-dimension and BHMT statements cannot be labeled kernel-checked.
- Comparator: no new endpoint challenge or acceptance receipt in this lane.
  Parent integration owns statement ties, generation and comparison decisions.
  Candidate relations, seven narrowly exact new rows, explicit source hashes and
  separate pending compilation status are in
  `round2_forrelation_exponent_ties.json`; broad returned rows remain partial.
- Reviewer/public route: no human review or author confirmation. This work is a
  local AI-agent proof implementation and source audit.
- Publication destinations: no submission requested or made here. Existing
  publication metadata must distinguish local build from external acceptance.
- Continuation: the five dependency-ordered consumers above replace any prompt
  that would ask for the coarse coefficient already strengthened here. The
  reusable lesson is to group the sharp scalar product before bounding the
  path, and to choose the auxiliary planted cutoff from the available uniform
  estimate without changing the total function.

Execution receipt: `research_actor_mode = mixed` (advisory returns plus direct
source/Lean work); selected probe = sharp coefficient through existing finite
contradiction; falsifier = a failed scalar bound or a gap no larger than
`7a/12`; alternative attacks considered = external SSW/restriction upgrade,
endpoint-conditioning tail upgrade, and no-BHMT existing-decoder diagonal.
The elementary sharp endpoint was selected because it reuses the complete
existing proof chain and isolates the genuinely new coefficient. The other
mechanisms are retained as exact consumers, not repackaged as completed proofs.
