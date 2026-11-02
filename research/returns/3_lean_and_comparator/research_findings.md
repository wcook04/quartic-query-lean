# Mathematical and implementation findings

This document explains the decisions behind the return. The input paper is
`paper/quartic-query-separation.pdf`; line references use `paper/extracted.md`.
Statements about external code are supported by the full commits and exact
declarations in `new_prior_art.json`, `model_decision.md`, and the per-row plan.
All source checks are distinct from compilation.

## 1. What a successful project would establish

There are three mathematical branches. The construction and quantum algorithm
give `Q(F_{k,m}) <= C_k sqrt(m) (log m)^b_k`; the planted-input argument gives
`R(F_{k,m}) >= c_k m^(2-1/k)/(log m)^2`; the known universal bound gives
`R(f) <= D(f) <= C(1+Q(f))^4`. A separate asymptotic argument joins them.
This is the actual dependency structure of Sections 2–5 and Appendix A.

For a proposed exponent `0 <= alpha < 4`, choose one integer `k >= 2` with
`2-1/k > alpha/2`, then hold k fixed as m tends to infinity through powers of
four. The ratio of the classical lower bound to the proposed quantum power has
a positive power of m divided by a fixed power of log m. That ratio diverges.
Only after separately proving that exponent four belongs to the universal
bound set may one conclude that its infimum is four. This avoids both an
empty-infimum error and a silent change from fixed-k bounds to a uniform-in-k
statement. [Paper pp. 1, 14, Theorem 1.1 and Section 5.]

The original ledger has 118 entries of several kinds. A complete main theorem
and complete coverage of those 118 entries are different milestones. An
alternative formal proof of Theorem A.1 can be mathematically sufficient for
the main result while leaving the author's intermediate Lemma A.2 unproved.
The plan records that distinction per row.

## 2. A substantive ledger error: adaptive access versus fixed support

The input ledger says that each certificate test is a function of at most
`ell+1` input bits, including the pointer test. The paper instead says it can
be **evaluated** in `ell+1` queries. Those statements have different meanings.

The pointer test is `X_j[decode(p)] = 0`. The algorithm reads the ell bits of p
and then one target bit. But for every possible target position a, there is an
input with p=a on which flipping X_j[a] changes the answer. Thus every one of
the m target bits can be relevant to the Boolean function. With m=4 and ell=2,
the test has a depth-three decision tree while all four target bits can affect
its output on suitable inputs.

The correct formal target is a decision tree computing this test with depth
at most `ell+1`. A separate coherent implementation must prove the bit-oracle
cost of loading the pointer, computing the target location, reading that bit,
and uncomputing. It must not obtain the entire pointer or cell in a single
query. The new `BitLoc` type makes every such access a physical bit access.
[Paper p. 6, Lemma 2.2, lines 266–294; original ledger `lem-2.2.i`.]

## 3. The drift file is a useful algebraic seed

The supplied `Drift.lean` states the finite identity

\[
\sum_p \frac{w_p}{W}\sum_i w_i a_{ip}
=\frac{W^2-\sum_i w_i^2}{2W}\le \frac W2,
\qquad W=\sum_iw_i>0.
\]

Its `IsComparison` structure includes complementarity off the diagonal and
zero diagonal, but no probability bounds. Its theorems allow arbitrary real
weights, including negative ones. This does not invalidate the finite algebra:
the sum-of-squares argument still works with positive W. It does mean that
calling the expression an expectation requires extra hypotheses.

Add a probability wrapper with `0 <= w_i`, `0 <= a_ij <= 1`, normalization of
the pivot law, and preservation of those invariants. Define the W=0 state as
absorbing. Then prove the finite-horizon expectation bound, the winner-weight
bound, Markov's inequality, and the implementation coupling. Algebra alone
does not establish any of those process-level claims. The exact finite check
in `checks/finite_checks.py` confirms the identity and process bounds for a
small example; it is not a general proof. [Paper pp. 8–9, Eqs. 10–15; supplied
`lean/current/Drift.lean`, inspected in full.]

The attachment records no successful terminal build receipt. It is therefore
an existing **unverified source draft**, not a checked theorem available for
the new corpus. Its module/public/exposure port and actual compilation should
be an early, small milestone.

## 4. The central model choice is an interface and proved bridges

Use a literal adaptive bit-query definition for the public Q. The draft has
finite unitary/measurement/query programs, a syntactic worst-case query cap,
and unnormalised branch states. Measurement probabilities are carried by
squared norm; a branch of probability zero does not require dividing by zero.
The query cap holds on all inputs, while correctness is restricted to promised
inputs. The algorithm's state, gates and output rule are chosen independently
of x; the bit oracle is the only operation that receives x.

The existing complexitylib controlled-phase model has arbitrary finite
workspace. The phase oracle `(-1)^(b*x_i)` is conjugate to the bit-flip oracle
by a Hadamard on its answer bit. This must be implemented as a proof, with a
separate deferred-measurement/padding argument for adaptive algorithms. For an
upper bound, construct an algorithm and transport it into the public model.
For a lower bound, transport **every** public-model algorithm into the model
to which the imported lower bound applies. The two proof directions cannot be
interchanged. Constant factors are acceptable for the exponents, but they must
be explicit in the finite bounds.

The draft also handles a subtle edge case: with an empty coordinate type,
the register space `Fin 0 × Bool × W` is zero-dimensional and has no unit
vector. A constant-answer alternative gives the correct zero-query behavior
without pretending such a vector exists.

For R and Q defined by a natural-number infimum, prove that their feasible
cost sets are nonempty and attain their minimum before using lower-bound
characterizations. `sInf (empty : Set Nat)` is zero. Read-all algorithms supply
the required witnesses on finite inputs. Empty promise domains, constant
functions, and N=0 deserve explicit sanity lemmas. A misleading complexity
definition can otherwise make a perfectly type-correct theorem meaningless.
[Pinned Randomized.lean, Search.lean, Complexity.lean and Simulation.lean in
`new_prior_art.json`; draft `core_definitions.lean`.]

## 5. Reuse amplification at the strength actually established

The inspected Troy Lee source contains `AmpSetup.amplified_cond_law`, zero-
success behavior, constant success amplification, and an explicit worst-case
budget bound. This is unusually well matched to the paper: after amplification,
the tournament needs the same conditional candidate distribution `w_i/W`.
Ordinary success amplification without that distribution theorem is
insufficient.

There are still three separate obligations. First, transport its oracle and
workspace semantics into the public model. Second, repeat a fixed number of
trials to make failure at most eta, preserving the conditional law and charging
all forward and inverse queries. Third, the paper's Lemma 3.1 asserts the full
successful state up to global phase. A theorem about classical output
probabilities alone does not establish that stronger statement; use the
inspected Grover-plane state theorem or prove the needed state wrapper.

For the tournament, create independent workspaces for comparisons with each
previous pivot and retain their garbage. Conditioned on candidate i, their
joint success probability must be the product of the individual a-values.
Reusing an entangled workspace without that product proof is not licensed by
the drift identity. [Paper pp. 7–9, Lemma 3.1 and Eq. 15; source declarations
in `QuantumQueryComplexity/Quantum/Amplitude/Amplification.lean` and
`Geometry.lean` at the recorded full pin.]

## 6. The classical lower bound has a clean first conditional milestone

Prove the per-instance-capped direct-product lemma directly by finite
continuation values. At a positive-probability transcript, the independent
input blocks remain independent under their separate observed constraints.
The best remaining success value for the queried block decreases in
conditional expectation. Other blocks' values remain unchanged, so their
product is a supermartingale. Finite recursion avoids requiring a large
measure-theoretic martingale development.

Drucker's Lemmas 3.1–3.2 support these two ingredients, but his main
total-budget direct-product theorem is a different statement. The paper needs
at most L queries to **each** independent instance, adaptive interleaving,
and arbitrary independent side information. Cite the precise lemmas and
prove the chosen capped formulation. [Paper pp. 11–12, Lemma 4.1;
[Drucker, arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2), pp. 11–12.]

The heavy-column argument must bound a joint event. Conditioning the input
distribution on a column being nonheavy can bias it. A simple warning example
is AND of two uniform bits with L=1: an adaptive algorithm queries the first
bit, stops if it is zero, and queries the second otherwise. Among nonheavy
runs its answer is certain, although the best unconditional one-query success
is only 3/4. This is why the paper's aborting simulator proves
`Pr(nonheavy AND guessed-address-correct) <= beta^r`.

There is also a simpler finite tail estimate than the asymptotic one in the
intake. With m=4^t and r=40t,

\[
(2/3)^{40t}\le(1/2)^{20t}=m^{-10}.
\]

If `1 <= L <= m` and `G <= mL/100`, then

\[
\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r
\le\frac4{100}+\frac1{100}+\frac1{100m^8}
\le\frac6{100}<\frac13.
\]

This removes logarithmic-limit machinery from that step. The eventual-in-t
reasoning is still needed to derive the Forrelation lower bound and to obtain
`1 <= L <= m`. This is our elementary simplification of Eq. 23, not a claim
that the paper contains an error. [Paper p. 13, Eqs. 19–23.]

## 7. Forrelation: exact statement first, deep lower bound later

For the public problem P, retain exactly the thresholds `Phi >= delta` and
`abs(Phi) <= delta/2`, with `delta=2^(-5k)`. Large negative Phi is outside the
promise. For m=4^t, the denominator `M=m*(sqrt m)^(k-1)` is an integer, so the
two comparisons can be expressed as `2^(5k) N >= M` and
`2^(5k+1) abs(N) <= M`. This produces an exact, decidable definition. The
normalised matrix formula must be proved equal to it.

An exact sum definition of N does not establish the circuit size bound.
That needs the butterfly recursion, integer magnitude bounds, bit widths,
fan-in-two arithmetic circuits and transcript verification. The circuit
argument remains explicit in Fkm until a concrete correct circuit family is
constructed; the paper itself specifies a construction scheme rather than a
unique gate numbering. [Paper pp. 3–6, Eqs. 3–8 and Lemmas 2.1–2.2.]

Bansal and Sinha's Theorem 1.3/Corollary 1.4 match the promise normalization
and the fixed-k randomized lower bound consumed here. Their proof is a
substantial Gaussian/Fourier argument. Source matching is not a Lean proof.
The intended persistent hypothesis is the exact weaker consequence
`forall fixed k >= 2, eventually t, Lvalue k t < R(P k t)`, with a separately
recorded bridge from the literal published bound. It must never be added to
Comparator's allowed-axiom list. [Bansal–Sinha,
[arXiv:2008.07003v3](https://arxiv.org/html/2008.07003v3), Eq. 1.3,
Theorem 1.3, Corollary 1.4.]

## 8. What is reusable, and what remains open

The checked sources materially help with decision trees, finite minimax,
Boolean Fourier analysis, sensitivity/degree arguments, the universal quartic
upper bound, exact conditional-law amplification, Hadamard matrices and
finite conditional-probability infrastructure. The model comparison gives
reasons for selecting or declining each import. General multiplicative-weights
regret and Dürr–Høyer minimum finding are related prior art; neither is a
necessary prerequisite for this proof.

No complete matching Lean Forrelation lower bound or capped adaptive
direct-product theorem was verified in the inspected sources. This is a
bounded search result, not a universal absence claim. Search queries and
inspection gaps are retained. If a matching built theorem is later found,
replace the corresponding proof/hypothesis work with an exact transport and
rerun the statement-fidelity checks.

## 9. Practical definition of success

The first useful result is the new construction's randomized lower bound
under a concrete hardness premise, with the capped direct product and all
probability bookkeeping actually proved. In parallel, settle the quantum
model bridge and port the strongest amplification theorem. After both family
bounds and the universal upper bound are proved, publish a distinct conditional
exponent theorem. The unconditional result follows only when its remaining
Forrelation premise has a formal proof in the same semantics.

Comparator is then one layer of evidence: it checks the chosen theorem and
its frozen definitions against a separately compiled Challenge. Human/source
review of the mathematical statement, a hypothesis inventory, build receipts,
and kernel replay serve different purposes and should remain separate in the
future website's data. The exact preparation rules and negative controls are
specified in `comparator_design.md`.
