# Forrelation quantum semantics audit

Scope: delegated source-level audit of the supplied round-three job 02, against packet commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`. This note is a working contribution to the parent author's return. It is not an integrated paper, a new Lean run, or a Comparator run. No input file was modified.

## Conclusions for the replacement section

The normalized product, asymmetric promise, projection law, binomial amplification, and ordinary coherent quantum construction in baseline §§3.1–3.3 are mathematically sound on the stated domain `k >= 2`, `m = 4^t`, `t >= 1`. Three distinctions must remain explicit:

1. The source's direct projection experiment has acceptance probability `Phi^2` and has an ordinary implementation using `k` physical bit queries. Aaronson–Ambainis, arXiv:1411.5729v1, §3.2, Figure 1 and the paragraph immediately before Proposition 6 describe this experiment. Proposition 6 instead constructs a `ceil(k/2)`-query interference experiment with probability `(1+Phi)/2`.
2. The supplied logical implementation gives `Samples k`; its generic compiler gives `Runs (2*k)`. The local theorem `construction_bitOracle_phase_kickback` is not a whole-circuit `Runs k` theorem. A direct ordinary proof of a `k`-query implementation is legitimate, but its full formal correspondence remains partial.
3. `Samples nk L` and `Runs (2nk) L` alone pair a coherent witness with a measured/reset witness having the same law. The current complete wrapper additionally links the **same** isometry `F`, initial label `o`, output map `out`, law `L`, and retained physical continuation. It supplies exactly the missing conjunction, with the allowed factor-two overhead.

The baseline's old claims that the packet contains no receipt directory and that Lemma 2.1(ii)/the complete Lemma 2.1 have no joint declaration are superseded by this packet. Current evidence must be cited narrowly and source-bound.

## 1. Normalization and the promise

Let `W[a,b]=(-1)^(a dot b)` on binary strings of length `2t`, `H=W/2^t`, `u=(1,...,1)/2^t`, and `D_r=diag(z_r)` for signs `z_r(a)=(-1)^(x_(r,a))`. All factors are real orthogonal: the nontrivial row inner products vanish by pairing an index with its translate along a coordinate on which the two rows differ. Consequently

`psi_z = D_0 H D_1 H ... H D_(k-1) u`,

`Phi(z) = <u,psi_z>`, `||u||=||psi_z||=1`, and `|Phi(z)|<=1`.

The product is evaluated from right to left. There are exactly `k-1` internal `H` factors. An additional `H` prepares `u` from the zero basis vector; an additional final `H` converts the projection onto `u` into the zero-address event. Neither extra transform consumes an input query.

The exact promise is `P(z)=1` if `Phi(z)>=delta`, `P(z)=0` if `|Phi(z)|<=delta/2`, and undefined otherwise, with `delta=2^(-5k)`. A negative large correlation must remain unpromised. Replacing the yes condition by `|Phi|>=delta` is a different partial function.

The integral numerator is the sum over paths `p in [m]^k` of the product of the `k` input signs and the `k-1` Walsh signs. Its denominator is

`M = m (sqrt(m))^(k-1) = 2^(t(k+1)) > 0`.

The final equality uses `k>=1`; it should not be asserted for the formal extension at `k=0`, where natural subtraction saturates and the supplied denominator is `m`. On the intended domain there is no issue. Positivity of `M` gives the exact tests `2^(5k) N >= M` and `2^(5k+1)|N| <= M` without approximation.

Principal source declarations: `QuarticQuery.Forrelation.Phi_eq_matrix_product`, `abs_Phi_le_one`, `delta_le_Phi_iff`, `abs_Phi_le_iff`, `P_eq_cases`; full conjunctions are `QuarticQuery.Paper.construction_equation_3`, `construction_equation_4`, `construction_N_phi`, `construction_integer_tests`. The definition itself is `QuarticQuery.P` in `Statement.lean`.

## 2. The same coherent preparation and measured law

Write

`F_z = H D_0 H D_1 ... H D_(k-1) H`.

For `|0>` the zero address basis state, let `v_z=F_z|0>`. Its zero coordinate is `Phi(z)`. The zero-address predicate is recorded coherently by the permutation

`|a,f> -> |a, f xor [a=0]>`.

The resulting one-trial vector, starting with flag zero, is

`|tau_z> = sum_a v_z(a) |a,[a=0]>`.

This is normalized on **every** input. Its flag law is Bernoulli with parameter `p(z)=Phi(z)^2`. On the promise, `p>=c` for a yes-input and `p<=c/4` for a no-input, where `c=delta^2=2^(-10k)`.

For `q` repetitions, use `q` fresh address/flag registers and the tensor product `|tau_z>^(tensor q)`. Then reversibly compute the flag count and `B=[count >= q*c/2]` into fresh registers while retaining the original addresses and flags. Thus one particular coherent preparation has output law

`L_z(1) = sum_{s=0}^q [s>=q*c/2] binom(q,s) p(z)^s (1-p(z))^(q-s)`,

`L_z(0)=1-L_z(1)`.

This is an all-input identity, not merely a promise implication. For any fixed pattern of flags with `s` successes, summing squared amplitudes over the corresponding Cartesian product of address sets factorizes into `p^s(1-p)^(q-s)`. The `binom(q,s)` disjoint flag patterns give the displayed law. This supplies the hard coherence/probability step directly and avoids identifying two unrelated witnesses that happen to have the same acceptance probability.

The source implementation uses a finite label map `out:Z -> Bool` rather than a separately named tensor-factor output qubit. These are ordinarily equivalent: `|z,b> -> |z,b xor out(z)>` is an input-independent permutation, so appending the output qubit costs no queries and preserves the entire register `z`.

Source locators:

- `Forrelation/Repetition.lean`: `successProb_eq`, `failureProb_eq`, `successProb_of_true`, `successProb_of_false`.
- `Upper/Decode.lean`: `forr_samples` constructs the normalized `F_z` witness; `Samples.count` proves the count law; `Samples.threshold` proves the threshold law; `decode_samples` and `decodeProb_correct` combine them.
- `Upper/Sampler.lean`: `Samples` explicitly existentially quantifies `Z`, its finite instance, `o`, `out`, `F`, `IsCirc n F`, and the all-input equality with `lawOf (F x (rket o)) out`.

The source's coherent count construction uses retained direct-sum/workspace labels and `Samples.bind`; the simple tensor-product proof is an ordinary realization of the same probability calculation, not a claim that the implementation uses literally the same tensor-factor layout.

## 3. Repetition count and query cost

The elementary moment identity is `E[a^S]=(1-p+pa)^q`. With `c>0` and `p in [0,1]`, the upper error tail is

`Pr[S>=qc/2] <= exp(-qc/2) (1+p(e-1))^q <= exp(-qc/16)` when `p<=c/4`,

using `e-1<7/4`, `1+y<=exp(y)`. The exponent is at most `-qc/2 + 7qp/4 <= -qc/16`.

The lower error tail is

`Pr[S<qc/2] <= exp(qc/2) (1-p+p/e)^q <= exp(-qc/10) <= exp(-qc/16)` when `p>=c`,

using `1-e^(-1)>3/5`. The strict lower-tail event presents no rounding problem; Markov's inequality still gives the weak bound. Since `S` is integral, output one exactly when `S>=ceil(qc/2)`.

Therefore

`q = ceil(16 * 2^(10k) * ln(1/eta))`

suffices for error at most `eta`, for `0<eta<1/2`. It is positive and input independent. The ceiling estimate is

`q <= 1+16*2^(10k)*ln(1/eta)`.

### Ordinary `qk` physical-query construction

For each fixed block `r`, position the query address at `(r,a)` coherently in `a` and put the response qubit in `|->`. Then

`O_x(|r,a> |-> |w>) = z_r(a) |r,a> |-> |w>`.

The response qubit remains in `|->`; arbitrary workspace amplitudes and entanglement are allowed. Input-independent block relabelings and Walsh transforms supply the remaining gates. This yields the entire trial in `k` calls. Repeating on fresh registers, with input-independent swaps to bring the active address register into the physical query register, yields `qk` calls with all other registers retained. Counting and thresholding use no input queries. Every execution uses the same number of calls; no stopping rule depends on outcomes or on the promise.

This justifies the ordinary statement `Q_eta(P)<=qk` and the all-input fixed cap. The corresponding full formal `Runs (q*k)` or retained physical `q*k` compilation theorem is **not supplied**. The only current tight local formal theorem is `construction_bitOracle_phase_kickback` plus `construction_bitOracle_phase_preserves`.

### Source-certified generic `2qk` compilation

`ReadSpec` permits a signed involutive permutation conditioned on one queried bit. `Upper.compile_read` loads the bit, applies the controlled signed permutation, then unloads it: two physical queries. `Upper.compile_circ` extends this to every `IsCirc n F`, preserving the complete logical register in a finite physical embedding, with cap `2n`.

`Upper.P_runs` chooses the same all-input threshold law and gives `Runs (2*(n*k)) L` with error at most `eta` when `n>=repetitions k eta`. The current complete wrapper strengthens the packaging to retained physical workspace, still with this factor two.

It is safe to display the `2qk` bound as the current full compiled guarantee and separately explain the ordinary phase-kickback `qk` proof. Either gives `O_k(1+log(1/eta))`; neither establishes a new theorem uniform in growing `k`.

## 4. Why the complete wrapper really uses one witness

In `Paper/ConstructionForrelationComplete.lean`, `construction_lemma_2_1_ii_complete`:

1. Calls `construction_lemma_2_1_ii k hk` to obtain `n,L`, the cap, `hs:Samples(n*k)L`, law normalization, and correctness.
2. Opens `hs` **once**, obtaining `Z,instZ,o,out,F,hF,hL`.
3. Chooses an embedding `emb:Z -> Fin(w+1)` and applies `compile_circ emb hF` to **this same** `F`.
4. Returns the cap, `IsCirc(n*k)F`, equality `L z b=lawOf(F z(rket o))out b`, all-input normalization, correctness, and a physical continuation `K` with

   `(K next).queryCap <= 2*(n*k)+next.queryCap`,

   `(K next).outputMass z (clEmb emb psi) b = next.outputMass z (clEmb emb (F z psi)) b`

   for every `next`, input `z`, logical state `psi` and output bit `b`.

The continuation equation concerns arbitrary embedded logical states, not just the original basis state. It therefore preserves the coherent resource for later use. The proof of `compile_circ` constructs only unitary/query prefixes before `next`; unlike `Samples.runs`, it does not measure all basis labels and reset them before continuation.

The `[Inhabited (ForrelationCoord k t)]` instance is not an unproved mathematical premise. The complete wrapper constructs it as `(0,0)`, using `k>=1` and `mValue t>0`. It only chooses the fixed physical address at which the compiler parks its query register between reads. The logical basis type `Z` is nonempty because the initial label `o:Z` is part of the same witness.

To recover the Boolean law from the retained physical continuation, take the coordinate projector onto the finite set of embedded basis labels satisfying `out(z)=true`, then return the measured bit. `clEmb_apply_cl` copies every logical coordinate exactly and `clEmb_apply_of_ne` vanishes off the embedding. The projector mass is therefore precisely `lawOf(F_z|o>)out true=L_z(true)`; the complementary mass is `L_z(false)`. No additional oracle calls or reset are required. A literal output qubit can equivalently be appended by the query-free permutation described above.

Two exact boundaries:

- The complete theorem existentially quantifies `n`; its statement does **not** say `n=repetitions k eta`, though the proof chooses this value. Cite `decode_samples`, `P_runs`, `repetitions_le` or the ordinary construction for the explicit displayed ceiling count.
- The theorem does not assert behavior on arbitrary physical states outside `clEmb`'s range. That is not needed for a computation initialized in the chosen embedding.

## 5. Concrete examples clarifying the promise

For `k=2,t=1`, order addresses as `0,1,2,3`. Then

`W = [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]`,

`M=8`, `delta=1/1024`. Set the second block to `v=(-1,1,1,1)`, so `Wv=(2,-2,-2,-2)`.

| First block | Second block | N | Phi | P | Projection p |
| --- | --- | --- | --- | --- | --- |
| `(1,-1,-1,-1)` | `v` | 8 | 1 | 1 | 1 |
| `(1,1,1,-1)` | `v` | 0 | 0 | 0 | 0 |
| `v` | `v` | -8 | -1 | undefined | 1 |

Thus the negative example produces the same deterministic projection flag as the positive example while the exact promise recognizer rejects it. This is fully compatible with the algorithm's specification: it must output a bit on every input but need be accurate only on the promise. It also shows why the exact promise detector cannot simply threshold `Phi^2`.

The expected complete numerator histogram is `{-8:8,-4:96,0:48,4:96,8:8}`; equivalently the promise census is 104 yes, 48 no, 104 undefined. This follows from the baseline's even/odd parity argument and the declarations `census_true`, `census_false`, `census_none`. This delegated audit has not rerun a census script; the parent checker is independent evidence.

## 6. Literature roles and edition boundaries

- **OpenAI, 5 October 2026 supplied preprint**, §2.1, equations (3)–(4), Lemma 2.1(ii)–(iii), printed pp.3–4: exact claim being explained. The supplied PDF hash is governed by the packet manifest. This audit read the attached extraction at the exact passages. It does not claim a public publication record beyond the supplied source.
- **Aaronson–Ambainis**, arXiv:1411.5729v1 (2014), §3.1 and §3.2, printed pp.12–14, Figure 1, paragraph before Proposition 6: problem/circuit ancestry and the squared-amplitude quantum perspective. Proposition 6 is separately the half-query interference test. The attached arXiv promise uses yes threshold `3/5` and no threshold `1/100`; do not credit this version with the literal `delta,delta/2` thresholds. The journal publication is SICOMP 47(3), 982–1038 (2018), but numerical locators above are to the actually inspected arXiv v1.
- **Bansal–Sinha**, arXiv:2008.07003v3, equations (1.1)–(1.3): exact normalized form and asymmetric promise for general powers `N=2^n`; specialize `N=m=4^t`. Its Proposition 1.2 records the `(1+Phi)/2` interference law. The source's exact lower bound and any §5.4 proof issue are outside this focused quantum audit.
- Web cross-check on 2 November 2026: https://arxiv.org/abs/2008.07003v3 reports v3 dated 17 November 2020, and https://arxiv.org/abs/1411.5729 reports the 21 November 2014 v1. The tool references were `turn2view0`, `turn2view1`; the parent must independently open them before citing tool references in its final answer. No web statement beyond these primary-source bibliographic checks is needed from this delegated audit.

## 7. Evidence state and files returned to parent

`quantum_declarations.json` contains 34 exact source declaration signatures, source lines/hashes, necessary surrounding implicit contexts, and, where available, the supplied native full-type-and-axiom excerpt. It separates verbatim source signatures from native elaborated output.

`quantum_evidence_hash_checks.json` records freshly performed SHA-256 comparisons for every local input in the supplied native acceptance records of four modules:

| Module | Reported state | Local input hashes matched |
| --- | --- | --- |
| `Paper.ConstructionForrelationDefinitions` | `current_native_pass` | 11/11 |
| `Paper.ConstructionForrelationQuantum` | `current_native_pass` | 28/28 |
| `Paper.ConstructionForrelationComplete` | `current_native_pass` | 29/29 |
| `Paper.ConstructionPhase` | `current_native_pass` | 7/7 |

There were no mismatched or unavailable declared local inputs in those focused checks. This validates the supplied records' attachment to the extracted sources; it does not replay Lake or independently reproduce the native binary artifacts.

The supplied `reviewed-type-axiom-audit.log` includes the full types and allowed-axiom lists of `construction_projection_test` (lines 229–243), `construction_bitOracle_phase_kickback` (244–251), its preservation theorem (252–262), and `construction_lemma_2_1_ii_complete` (263–307). Their printed axiom lists are `propext`, `Classical.choice`, `Quot.sound`. The separate supplied audit verdict reports success. The parent evidence audit should bind those log/verdict hashes before making a broader current-evidence claim.

Current `corpus/ties.json` marks `construction_lemma_2_1_ii_complete` exact, same route, with ordinary premises fixed `k>=1`, `m=4^t`, `0<eta<1/2`, and no open assumptions. It correctly retains `construction_projection_test` and both phase-kickback declarations as partial ties to the bundled tight projection claim.

No fresh Lean or Comparator execution was performed in this delegated audit. The historical return-2 blueprint and comments labeled `UNELABORATED` describe their submission-time state; they must not override the later source-bound native evidence in this packet.
