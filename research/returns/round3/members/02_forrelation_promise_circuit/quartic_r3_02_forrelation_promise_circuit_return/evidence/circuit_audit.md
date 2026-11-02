# Circuit, arithmetic and finite-example audit

## Verdict and scope

The inspected ordinary integer-threshold and modular-circuit arguments are sound. The exact circuit recognizes the asymmetric promise on every input; it also sets its value output to the positive-threshold comparison even outside the promise. The endpoint does not depend on a signed interpretation of every intermediate word.

This audit read the complete current `Forrelation/Arithmetic.lean`, `Builder.lean`, `Circuit.lean`, `Sanity.lean`, `Promise.lean`, and `Paper/ConstructionArithmetic.lean`, `ConstructionForrelationDefinitions.lean`, `ConstructionForrelationCircuit.lean`, `ConstructionForrelationComplete.lean`; the assigned baseline §§3.1–3.5, roadmap §1.1 and interfaces §§2.2/3.17; source preprint §2.1; and the scoped round-two blueprint, review, gaps and maintained construction tie review. The current native compilation receipts are a separate evidence task. No Lean compilation or Comparator run was performed by this auditor.

The current integrated sources still contain historical `UNELABORATED` header comments. The maintained `round2_construction_quantum.md` reports later native passes for the integrated helper modules. A status statement must use the current source-bound receipts, not the old headers alone. Historical round-two returned copies are distinct from the integrated `repository/lean` copies.

## 1. Integer representation and exact comparisons

Fix integers (k\ge2), (t\ge1), and (m=4^t). Coordinates are indexed by the (2t)-bit representations of (0,\ldots,m-1), with

\[
W_{ab}=(-1)^{a\cdot b},\qquad H=m^{-1/2}W,
\qquad u=m^{-1/2}\mathbf1.
\]

For sign blocks (z_0,\ldots,z_{k-1}), expanding the matrix product gives

\[
N(z)=\sum_{a_0,\ldots,a_{k-1}}
\left(\prod_{r=0}^{k-1}z_r(a_r)\right)
\left(\prod_{r=0}^{k-2}W_{a_r,a_{r+1}}\right)\in\mathbb Z,
\quad
\Phi(z)=\frac{N(z)}{M},
\quad M=m(\sqrt m)^{k-1}=2^{t(k+1)}.
\]

There are (k-1) normalized Walsh factors and two normalized boundary vectors, so the denominator contains (k+1) factors of (\sqrt m), not (k). The identity (M=2^{t(k+1)}) uses (k\ge1); the underlying natural-number definition has a truncated (k-1), so do not silently state that exponent identity for (k=0).

Since (M>0), multiplying the positive real denominators yields, with (s=5k),

\[
\Phi\ge2^{-s}\iff 2^sN\ge M,
\qquad |\Phi|\le2^{-s-1}\iff2^{s+1}|N|\le M.
\]

These inequalities include equality at both thresholds. Their conjunction is impossible. Define (p_1=[2^sN\ge M]), (p_0=[2^{s+1}|N|\le M]), (d=p_1\lor p_0), (b=p_1). Then (d=1) exactly on the promise and the value bit is correct whenever (d=1). In fact (b=0) at every unpromised input, since the positive comparison would itself make the input promised.

Relevant current-source declarations are `QuarticQuery.Paper.construction_N_phi`, `construction_integer_tests` and `construction_forr_output_bits`, plus `QuarticQuery.Forrelation.delta_le_Phi_iff`, `abs_Phi_le_iff`, `P_tests`. The two integer equivalences and the actual circuit-output clauses are distributed across separate declarations. The maintained tie review correctly records each individual tie for `claim-integer-tests` as partial; the conjunction follows from using both, but is not the exported type of either theorem alone.

## 2. The exact arithmetic circuit

### Butterfly recurrence

Write (m=2^h), where here (h=2t). Splitting a vector into its first and second halves and splitting the highest index bit in the Walsh character gives

\[
W_{2^{h+1}}(a_0,a_1)
=\bigl(W_{2^h}a_0+W_{2^h}a_1,
        W_{2^h}a_0-W_{2^h}a_1\bigr).
\]

Each level uses (m) scalar additions or subtractions, over (h) levels. One transform therefore uses (mh) arithmetic operations. Starting from (z_{k-1}), perform one transform and multiply coordinatewise by (z_{k-2}), then repeat backwards through the blocks, finally summing the coordinates. This produces (N).

### Ideal integers and modular words are different assertions

For the ideal integer recurrence, after (j) transforms every coordinate has magnitude at most (m^j), by induction using the triangle inequality. A butterfly partial block with (2^q\le m) terms is bounded by (2^q) times the maximum magnitude of that transform's inputs. Hence all such partial blocks are bounded by the next full-step bound. Every prefix of the final sum is bounded by (m^k). Thus (k\log_2m+2) signed bits suffice before threshold shifts, and an additional (O(k)) bits suffice for those shifts. This proves the source preprint's (m^{O(k)}) bound for the ideal arithmetic recurrence.

The actual local circuit maintains residues modulo (2^w). Its central invariant is exactly

```lean
def Enc (w : ℕ) (p : Prog ι) (v : List (Wire ι))
    (F : BitInput ι → ℤ) : Prop :=
  v.length = w ∧ AllValid p v ∧
    ∀ x, (bv (vals x p v) : ℤ) ≡ F x [ZMOD (2 : ℤ) ^ w]
```

Congruence is sufficient for additions, subtractions and sign multiplication. It does not, by itself, say that decoding each stored word as a signed integer gives the ideal integer value. `construction_walkN_bound`, `construction_walkN_prefix_bound`, and `construction_butterfly_block_bound` concern the ideal integers. A register-by-register signed refinement remains a separate formal obligation. This does not obstruct exact final Boolean outputs or demonstrate an overflow counterexample.

### Boolean arithmetic and sign recovery

A full adder uses five binary gates. Set (r=a\oplus b), (s=r\oplus c), (c'=(a\land b)\lor(r\land c)). Checking the eight Boolean triples proves (s+2c'=a+b+c). Multiplying those identities by successive powers of two and cancelling carries gives ripple addition modulo (2^w) in (5w) gates.

The source's shared addition/subtraction combinator first xors each second-operand bit with its sign-control bit and uses that sign as the initial carry. It costs (w+5w=6w) gates. If the sign bit is one, the complement plus one is the additive inverse modulo (2^w). The source therefore charges addition (6w), subtraction (6w+1) (one newly generated true gate), and coordinate sign multiplication (6w). These are counts in the supplied arbitrary-binary-truth-table gate model; constant-false wires cost no gate.

For (s=5k), (e=t(k+1)), choose

\[
w=s+3+e.
\]

Only the signs of

\[
A=2^sN-M,\quad B=M-2^{s+1}N,\quad C=M+2^{s+1}N
\]

must be read. Walsh orthogonality and Cauchy–Schwarz give (|\Phi|\le1), hence (|N|\le M). Consequently

\[
|A|\le(2^s+1)M,
\qquad |B|,|C|\le(2^{s+1}+1)M
<4\,2^sM=2^{w-1}.
\]

For any integer (T\in[-2^{w-1},2^{w-1})), the high bit of (T\bmod2^w) equals ([T<0]). If (T\ge0), its residue is (T<2^{w-1}); if (T<0), its residue is (2^w+T\in[2^{w-1},2^w)). Thus the three computed high bits determine exactly

\[
p_1=\neg[A<0],\qquad p_0=\neg[B<0]\land\neg[C<0].
\]

The last three gates produce (b=p_1), (p_0) and (d=b\lor p_0). The conjunction for (p_0) is precisely (-M\le2^{s+1}N\le M).

### Size, including a simpler ordinary accounting

The source recurrence is

\[
T_w(0)=0,\qquad T_w(h+1)=2T_w(h)+2^h(12w+1),
\]

so (T_w(h)=h2^{h-1}(12w+1)) for (h\ge1), and in the present family

\[
T_w(2t)=tm(12w+1).
\]

Its layer count is (1+6wkm+(k-1)T_w(2t)). Adding the final sum, two shifts, final comparisons and three output gates gives the exact constructor count

\[
S=6w\bigl((k+1)m+5k+t(k+1)+4\bigr)
 +(k-1)tm(12w+1)+7. \tag{*}
\]

This identity is derived here from the source constructor recurrences; no Lean theorem for this closed-form simplification was compiled or claimed. It is useful as a shorter ordinary proof of the existing upper bound. Put (a=k+1\ge2). For (t\ge1), (w=5a-2+at\le6at), and

\[
(k+1)m+5k+t(k+1)+4
=a(m+t+5)-1\le7amt.
\]

The last inequality uses (m,t\ge1). Also (12w+1\le13w), (k-1\le a), and (7\le7a^2mt^2). Formula (*) yields

\[
S\le(252+78+7)a^2mt^2
=337a^2mt^2
\le200(k+1)^2m(2t)^2.
\]

Thus the source's deliberately loose constant (200(k+1)^2) follows without the baseline's additional (X,Y,Z) abbreviations. The exact source theorem remains `forrCircuit_size_le`/`exists_circuit`. The sharper intermediate coefficient 337 is merely an ordinary accounting estimate and is unnecessary as a new canonical statement.

For the concrete smallest case (k=2,t=1), (w=16) and the reconstructed gate count is (3563), below the formal bound (28800). For (k=3,t=1), (w=22) and the count is (7275).

### Transcript guarantee

Each appended gate depends only on the fixed input bits, a constant, or prior gate values. Evaluating in order produces a gate-consistent transcript. Induction on the gate index shows any gate-consistent transcript equals that evaluation. Consequently exact output recognition can be consumed by the later total construction: a consistent transcript whose domain bit is one certifies both that the partial-function input is promised and that the value bit is its answer. No claim about the later classical lower bound is needed here.

`Builder.narrow` is total even for malformed raw forward references: it replaces such a reference with constant false, matching execution of the raw list. The specific arithmetic builder proves validity invariants and appends valid references. Do not infer that every arbitrary raw `Prog` list is syntactically valid merely because it packages to a total `Circuit`.

## 3. Smallest example and complete analytical census

For (k=2,t=1), (m=4), (M=8), (\delta=2^{-10}), and natural binary index order,

\[
W=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]

Fix (z_1=(-1,1,1,1)). Then (Wz_1=(2,-2,-2,-2)). The three first blocks below supply all three logical cases.

| (z_0) | (N=z_0^TWz_1) | (\Phi=N/8) | (P) | Exact circuit ((d,b)) | Projection probability |
|---|---:|---:|---|---|---:|
| ((1,-1,-1,-1)) | (8) | (1) | (1) | ((1,1)) | (1) |
| ((1,-1,1,1)) | (0) | (0) | (0) | ((1,0)) | (0) |
| ((-1,1,1,1)) | (-8) | (-1) | undefined | ((0,0)) | (1) |

The third row shows why the quantum proposal procedure and the exact certificate circuit have distinct jobs. The projection test may output one deterministically on a negative, unpromised input; this violates no promise-algorithm guarantee. The exact circuit must identify the promise failure.

For the count, the four rows of (W) and their negatives are eight distinct even-parity sign vectors. They exhaust the eight even-parity choices of (z_1). For each such (z_1), (Wz_1=\pm4e_j), so varying (z_0) gives (N=4) eight times and (N=-4) eight times. This contributes (64) occurrences of each sign.

The other eight (z_1)'s have odd parity. Multiplying coordinatewise by any Walsh row preserves odd parity, so each Walsh coordinate is (2) or (-2). Varying (z_0) therefore gives twice a sum of four independent signs: the numerator multiplicities at ((-8,-4,0,4,8)) are ((1,4,6,4,1)) for each such (z_1). The complete histogram is

\[
N=-8,-4,0,4,8
\quad\text{with counts}\quad8,96,48,96,8.
\]

Every positive numerator is at least four, so it meets the positive threshold. Every negative numerator is at most minus four, so it is unpromised. Only zero meets the small-absolute-value threshold. Therefore there are (104) one-inputs, (48) zero-inputs, and (104) unpromised inputs.

The analytical argument does not depend on trusting an enumeration. The supplied source's `census_true`, `census_false`, `census_none` and `Phi_negativeWitness` match it.

## 4. Executed independent checker

Command executed successfully:

```sh
python agent_circuit/exact_example_checker.py --json agent_circuit/exact_example_results.json
```

The checker uses arbitrary-precision integers and exact rational comparisons. It compares direct path expansion, dense Walsh multiplication, butterfly arithmetic, and a separately written Boolean reconstruction of the source constructors. Every gate has fan-in at most two, append-only wire indices are checked, and the word residues and final three sign bits are compared with the ideal integers.

Complete families checked:

| Parameters | Inputs checked | One | Zero | Undefined | Reconstructed gates |
|---|---:|---:|---:|---:|---:|
| (k=2,t=1) | (256) | (104) | (48) | (104) | (3563) |
| (k=3,t=1) | (4096) | (1472) | (1152) | (1472) | (7275) |

In addition, the checker checks all (8193) integers (N\in[-4096,4096]) at (k=2,t=4) against the exact threshold and sign-recovery rules. This deliberately reaches equality boundaries absent in the smallest input: (N=4) is a yes-threshold equality, (N=\pm2) are no-threshold equalities, (N=3) lies in the positive gap and (N=-4) is unpromised. These are synthetic numerators; the checker does not claim they are attained by actual sign inputs at that dimension.

Finite checks do not certify the infinite family, a Lean build, a Comparator pass, the current statement ties, or a lower-bound theorem. The reconstruction is not compiled/extracted Lean execution.

## 5. Ranked changes recommended to the parent section

1. Retain the modular-word versus signed-integer distinction. The exact endpoint is complete through congruence plus three final range bounds; do not convert the remaining register-refinement gap into a circuit-correctness gap.
2. Add all three concrete rows above, so the positive, zero and negative cases share one displayed matrix-vector calculation. Preserve the (104/48/104) census and give its parity proof.
3. Keep the value output fixed on every input. `CircuitRealises` alone is weaker than the actual output rule; cite `construction_forr_output_bits` in addition to `construction_integer_tests` for that rule.
4. Keep (m=4^t), (M=2^{t(k+1)}), (\delta=2^{-5k}), and both nonstrict integer thresholds unchanged.
5. Simplify the explicit size proof through (*) if desired, or give only the general (O_k(m\log^2m)) proof and separately cite the source's constant. Any closed-form gate-count display added to the manuscript is an ordinary derivation unless tied to a new checked declaration.
6. Refresh evidence wording from the supplied current receipts. Historical `UNELABORATED` comments and the old baseline statement that no build directory was supplied are obsolete as descriptions of this round-three packet.

No mathematical refutation of Lemma 2.1(iii) was found. No source inputs were edited.
