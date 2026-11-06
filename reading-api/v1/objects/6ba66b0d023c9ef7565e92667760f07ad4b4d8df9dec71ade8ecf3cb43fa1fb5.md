# Verification details and statement concordance

This reference preserves the full statement catalogue, checking history and formal correspondence accompanying the mathematical papers. Start with the [proof index](proof_index.md) for readable theorem names and links, or return to the [complete mathematical account](reasoning_record.md). Historical dates, appendix letters and statuses below refer to their recorded source editions. Mathematical backlinks from these historical records retain that edition.

## Appendix B. Mathematical statement catalogue

This appendix indexes every original claim by its identifier, with a link to its proof.

<a id="ROOT-CATALOGUE-INTRO"></a>
<!-- passage:ROOT-CATALOGUE-INTRO -->
This is a reference catalogue for the argument in §§2–7 and Appendix A. It preserves all 121 original claim IDs, the exact maintained statement of each claim, and a direct link to its proof or explanation. The groups follow the mathematical dependencies. Their introductory paragraphs identify formal boundaries which would otherwise be obscured by listing many component declarations.

The configured Comparator targets, their status, and the refinements that have no catalogue ID (the threshold $13669k^2$, the logarithmic exponent six and the named-circuit constants) are listed with their proofs in [Appendix G.4](#checked-statements). The [correspondence record](reasoning_record_correspondence.json) and [dated review receipt](reasoning_record_review.json) retain the declaration inventory and evidence. [Appendix G.3](#evidence-checks) explains their authority and historical scope.

The quotations below are the maintained ledger's literal claim text, including its plain-text notation, preserved so that each row can be matched byte for byte against the ledger; the linked argument gives the typeset statement and complete reasoning. Corrections to a historical quotation, including the Bansal–Sinha-to-$L$ and Huang rows, are identified by their original and maintained hashes in the correspondence. This compact catalogue does not replace either the proofs or that full evidence record.
<!-- /passage:ROOT-CATALOGUE-INTRO -->

### B.1. Functions, budgets and separation

The first group fixes the objects quantified over in the theorem. Read §§2.1–2.6 and Appendices G.2–G.3 for the promise, the common algorithm and the all-input cap. The exact function-model and separation wrappers now have source-bound mathematical-fidelity reviews. The global logarithm convention is prose: the available logarithm lemmas establish its separate numerical uses rather than one theorem asserting the entire convention. The real-power family and the floor-form headline remain distinct conjunctions, joined by the floor argument in §7.

#### def-log-convention

<a id="CAT-def-log-convention"></a>
<!-- passage:CAT-def-log-convention -->
<!-- claim:def-log-convention -->

> log means log_2, except where changing the base only changes an absolute constant. Ledger pinning: log in T (prop-3.2), r and l (eq-6) and L (eq-5) is exactly log_2.

**Argument:** [§2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-LOGS).

<!-- /passage:CAT-def-log-convention -->

#### def-partial-query

<a id="CAT-def-partial-query"></a>
<!-- passage:CAT-def-partial-query -->
<!-- claim:def-partial-query -->

> A partial Boolean function is a pair (D,P) with D a subset of {0,1}^N and P:D->{0,1}. An algorithm computes it if it is correct, with the stated error, on every x in D; behaviour off D is unconstrained.

**Argument:** [§2.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-PARTIAL).

<!-- /passage:CAT-def-partial-query -->

#### def-R

<a id="CAT-def-R"></a>
<!-- passage:CAT-def-R -->
<!-- claim:def-R -->

> For a (partial) Boolean function f, R(f) is the least q such that some probability distribution on deterministic decision trees of depth at most q satisfies Pr[T(x)=f(x)] >= 2/3 for every x in dom f. The query cap holds on every branch and every coin outcome.

**Argument:** [§2.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-PARTIAL), [§2.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-CLASSICAL).

<!-- /passage:CAT-def-R -->

#### def-query-oracle

<a id="CAT-def-query-oracle"></a>
<!-- passage:CAT-def-query-oracle -->
<!-- claim:def-query-oracle -->

> For x in {0,1}^n the bit oracle is the unitary O_x|i,b,z> = |i, b xor x_i, z>, with i in [n], b a bit, z a workspace label. It is self-inverse.

**Argument:** [§2.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ORACLE).

<!-- /passage:CAT-def-query-oracle -->

#### def-Q

<a id="CAT-def-Q"></a>
<!-- passage:CAT-def-Q -->
<!-- claim:def-Q -->

> Q(f) is the least q such that some quantum algorithm, with unrestricted query-free computation between uses of O_x and with at most q queries on every branch including all measurement outcomes, outputs f(x) with probability >= 2/3 for every x in dom f.

**Argument:** [§2.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ORACLE), [§2.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-ADAPTIVE).

<!-- /passage:CAT-def-Q -->

#### eq-1

<a id="CAT-eq-1"></a>
<!-- passage:CAT-eq-1 -->
<!-- claim:eq-1 -->

> alpha_tot = inf{alpha >= 0 : exists C_alpha < infinity such that for every n >= 1 and every total f:{0,1}^n->{0,1}, R(f) <= C_alpha (1+Q(f))^alpha}.

**Argument:** [§1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-RESULT).

<!-- /passage:CAT-eq-1 -->

#### eq-2

<a id="CAT-eq-2"></a>
<!-- passage:CAT-eq-2 -->
<!-- claim:eq-2 -->

> For fixed integer k>=2 and all sufficiently large powers of four m: Q(F_{k,m}) <= C_k sqrt(m) (log m)^{b_k} and R(F_{k,m}) >= c_k m^{2-1/k}/(log m)^2, with c_k,C_k,b_k>0 depending only on k.

**Argument:** [§1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-RESULT), [§1.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ARCHITECTURE), [§7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-FAMILY-ASSEMBLY).

<!-- /passage:CAT-eq-2 -->

#### thm-1.1

<a id="CAT-thm-1.1"></a>
<!-- passage:CAT-thm-1.1 -->
<!-- claim:thm-1.1 -->

> alpha_tot = 4. More precisely, R(f) = O((1+Q(f))^4) for every total Boolean f, and eq-2 holds for each fixed integer k>=2.

**Argument:** [§1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-RESULT), [§1.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ARCHITECTURE), [Appendix G.2](#ROOT-EVIDENCE-CONVENTION), [§7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-FAMILY-ASSEMBLY), [§7.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-NO-SMALLER).

<!-- /passage:CAT-thm-1.1 -->

#### cor-cubic-refuted

<a id="CAT-cor-cubic-refuted"></a>
<!-- passage:CAT-cor-cubic-refuted -->
<!-- claim:cor-cubic-refuted -->

> It is false that R(f) = O(Q(f)^3) for all total Boolean f ([3, Conjecture 2]): no C satisfies R(f) <= C Q(f)^3 for all total f.

**Argument:** [§1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-RESULT), [§7.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-NO-SMALLER), [§1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-QUANTIFIERS).

<!-- /passage:CAT-cor-cubic-refuted -->

### B.2. The Forrelation supplier

The literal ledger quotations below number the sign blocks $z_1,\ldots,z_k$; §3 numbers them $z_0,\ldots,z_{k-1}$. The $j$-th quoted block is therefore block $j-1$ in the derivation. This changes no coordinate inside a block.

Section 3 defines the promise and states its contract; §§8.1–8.4 construct the decoder and exact circuit; §§8.5–8.15 prove the randomized lower bound. The complete Lemma 2.1 wrapper and its component wrappers are available. Component facts about projection probability, threshold arithmetic and circuit size still require their surrounding definitions and translations: a partial tie to one of these rows is not automatically an exact proof of the whole prose row. The corrected Bansal–Sinha-to-$L$ statement is preserved below; its historical wording and the source-version discrepancy remain visible in the correspondence and §3.3. The ordinary sharp phase implementation costs $qk$, whereas the generic compiled route has the separately proved $2qk$ cap.

#### def-walsh-sign

<a id="CAT-def-walsh-sign"></a>
<!-- passage:CAT-def-walsh-sign -->
<!-- claim:def-walsh-sign -->

> m=4^t. H is the m x m normalized Walsh-Hadamard matrix, H_{a,b}=m^{-1/2}(-1)^{<a,b>} for a,b in {0,1}^{log_2 m}. u=m^{-1/2}(1,...,1)^T. A bit a is identified with the sign (-1)^a. For z in {+-1}^m, D_z=diag(z).

**Argument:** [§3.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_definition).

<!-- /passage:CAT-def-walsh-sign -->

#### eq-3

<a id="CAT-eq-3"></a>
<!-- passage:CAT-eq-3 -->
<!-- claim:eq-3 -->

> For z_1,...,z_k in {+-1}^m: Phi(z_1,...,z_k) = u^T D_{z_1} H D_{z_2} H ... H D_{z_k} u (k diagonals, k-1 copies of H), and delta = 2^{-5k}.

**Argument:** [§3.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_definition), [§3.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_references).

<!-- /passage:CAT-eq-3 -->

#### eq-4

<a id="CAT-eq-4"></a>
<!-- passage:CAT-eq-4 -->
<!-- claim:eq-4 -->

> P=P_{k,m} is the partial function on km bits with P=1 if Phi>=delta, P=0 if |Phi|<=delta/2, undefined otherwise. The two cases are disjoint.

**Argument:** [§3.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_definition), [§3.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_references).

<!-- /passage:CAT-eq-4 -->

#### eq-5

<a id="CAT-eq-5"></a>
<!-- passage:CAT-eq-5 -->
<!-- claim:eq-5 -->

> L = L_{k,m} = floor(m^{1-1/k}/(log_2 m)^2).

**Argument:** [§3.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_definition).

<!-- /passage:CAT-eq-5 -->

#### claim-bs-to-L

<a id="CAT-claim-bs-to-L"></a>
<!-- passage:CAT-claim-bs-to-L -->
<!-- claim:claim-bs-to-L -->

> For fixed k>=2 and the positive constant c of the Bansal-Sinha bound: for all sufficiently large powers of four m, c k^{-29} (m/log(km))^{1-1/k} > floor(m^{1-1/k}/(log_2 m)^2).

**Argument:** [§8.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_bs_translation), [§3.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_references).

<!-- /passage:CAT-claim-bs-to-L -->

#### lem-2.1.i

<a id="CAT-lem-2.1.i"></a>
<!-- passage:CAT-lem-2.1.i -->
<!-- claim:lem-2.1.i -->

> For fixed k>=2 and all sufficiently large powers of four m, R(P_{k,m})>L with L as in eq-5.

**Argument:** [§8.14](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_threshold), [§8.15](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_attribution), [§3.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_bundle), [§3.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_references).

<!-- /passage:CAT-lem-2.1.i -->

#### claim-proj-prob

<a id="CAT-claim-proj-prob"></a>
<!-- passage:CAT-claim-proj-prob -->
<!-- claim:claim-proj-prob -->

> Prepare u, apply D_{z_1} H ... H D_{z_k} right to left, measure the projection onto u. Each D uses one bit query (phase kickback), H and the projection use none. Success probability is exactly Phi^2: >=delta^2 on 1-inputs, <=delta^2/4 on 0-inputs.

**Argument:** [§8.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_quantum).

<!-- /passage:CAT-claim-proj-prob -->

#### lem-2.1.ii

<a id="CAT-lem-2.1.ii"></a>
<!-- passage:CAT-lem-2.1.ii -->
<!-- claim:lem-2.1.ii -->

> For every 0<eta<1/2 there is a quantum algorithm using O_k(1+log(1/eta)) bit queries that outputs P_{k,m}(z) with error <=eta for every z in dom P. It has a coherent implementation retaining all workspace. On every input, promised or not, measuring its output register yields a bit.

**Argument:** [§8.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_quantum), [§3.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_bundle), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-decode), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-decode-cost), [§8.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_coherent).

<!-- /passage:CAT-lem-2.1.ii -->

#### claim-N-phi

<a id="CAT-claim-N-phi"></a>
<!-- passage:CAT-claim-N-phi -->
<!-- claim:claim-N-phi -->

> With W=sqrt(m) H (entries +-1), N = z_1^T W D_{z_2} W ... W D_{z_k} (1,...,1)^T is an integer, Phi=N/M_{k,m}, and M_{k,m}=m (sqrt m)^{k-1} is a positive integer because m is a power of four.

**Argument:** [§8.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_integer).

<!-- /passage:CAT-claim-N-phi -->

#### claim-integer-tests

<a id="CAT-claim-integer-tests"></a>
<!-- passage:CAT-claim-integer-tests -->
<!-- claim:claim-integer-tests -->

> Phi>=delta iff 2^{5k} N >= M_{k,m}; and |Phi|<=delta/2 iff 2^{5k+1}|N| <= M_{k,m}. d is the disjunction, b the first comparison.

**Argument:** [§8.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_integer).

<!-- /passage:CAT-claim-integer-tests -->

#### claim-circuit-size

<a id="CAT-claim-circuit-size"></a>
<!-- passage:CAT-claim-circuit-size -->
<!-- claim:claim-circuit-size -->

> N is computed by k-1 unnormalized Walsh-Hadamard transforms, coordinate sign changes and a final signed sum. Each transform uses O(m log m) additions and subtractions; all intermediate integers have absolute value at most m^{O(k)}, so O_k(log m) bits suffice; hence Boolean size O_k(m (log m)^2).

**Argument:** [§8.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_circuit).

<!-- /passage:CAT-claim-circuit-size -->

#### lem-2.1.iii

<a id="CAT-lem-2.1.iii"></a>
<!-- passage:CAT-lem-2.1.iii -->
<!-- claim:lem-2.1.iii -->

> There is a Boolean circuit C=C_{k,m} of fan-in at most two and size S=S_{k,m}=O_k(m (log m)^2), counting non-input gates, with output bits d,b such that for every input z: d=1 iff P_{k,m} is defined at z, and d=1 implies b=P_{k,m}(z). The circuit computes these outputs exactly on every input.

**Argument:** [§8.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_circuit), [§3.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_bundle), [§8.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_circuit_size).

<!-- /passage:CAT-lem-2.1.iii -->

#### lem-2.1

<a id="CAT-lem-2.1"></a>
<!-- passage:CAT-lem-2.1 -->
<!-- claim:lem-2.1 -->

> Conjunction of lem-2.1.i, lem-2.1.ii and lem-2.1.iii for each fixed k>=2.

**Argument:** [§3.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_bundle), [§3.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_references).

<!-- /passage:CAT-lem-2.1 -->

### B.3. The addressed total function

Section 4 constructs one total function from a circuit and explains every local test. The [complete support wrapper][src-construction-full] conjoins physical-coordinate essentiality with the test count, exact evaluation, decision-tree bound and arbitrary-index coherent access. The printed Lemma 2.2 states the count and adaptive/coherent query clauses. Essentiality is an additional diagnostic in the expanded maintained ledger, so the new conjunction strengthens the printed lemma. The older [complete evaluator theorem][src-construction-complete] is partial relative to that expanded row, rather than deficient for omitting a support clause demanded by the original printed lemma. Layout, the addressed predicate and the test-count definition also have component ties; their complete mathematical interpretation is given by the common construction, not by a name alone. The winner-fidelity claim uses the same circuit and its correct transcript.

#### def-transcript

<a id="CAT-def-transcript"></a>
<!-- passage:CAT-def-transcript -->
<!-- claim:def-transcript -->

> For a fixed circuit, a transcript assigns a proposed bit to each non-input gate, including output gates. Input-wire values are not copied; they are read from the actual input.

**Argument:** [§4.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-transcripts).

<!-- /passage:CAT-def-transcript -->

#### eq-6

<a id="CAT-eq-6"></a>
<!-- passage:CAT-eq-6 -->
<!-- claim:eq-6 -->

> r = ceil(20 log_2 m), l = log_2 m.

**Argument:** [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-layout).

<!-- /passage:CAT-eq-6 -->

#### def-column-layout

<a id="CAT-def-column-layout"></a>
<!-- passage:CAT-def-column-layout -->
<!-- claim:def-column-layout -->

> The input has m columns. Column i contains: X_i in {0,1}^m; strings A_{i,1},...,A_{i,r} in {0,1}^{km} with no promise; and for each s in {0,1}^r a cell B_{i,s} holding, for each j != i, a pointer p_{i,s,j} in [m] encoded in l bits by a fixed bijection, and for each h in [r] an alleged evaluation transcript of C_{k,m} on A_{i,h}.

**Argument:** [§4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-construction-context), [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-layout).

<!-- /passage:CAT-def-column-layout -->

#### def-eval-transcript

<a id="CAT-def-eval-transcript"></a>
<!-- passage:CAT-def-eval-transcript -->
<!-- claim:def-eval-transcript -->

> An evaluation transcript of C_{k,m} on A_{i,h} has one bit per non-input gate including output gates, and these gates are the count S. It is correct iff every bit equals the true value of that gate on input A_{i,h}.

**Argument:** [§4.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-transcripts).

<!-- /passage:CAT-def-eval-transcript -->

#### eq-7

<a id="CAT-eq-7"></a>
<!-- passage:CAT-eq-7 -->
<!-- claim:eq-7 -->

> If every P(A_{i,h}) is defined, the true address of column i is s_i=(P(A_{i,1}),...,P(A_{i,r})) in {0,1}^r.

**Argument:** [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-address-winner).

<!-- /passage:CAT-eq-7 -->

#### eq-8

<a id="CAT-eq-8"></a>
<!-- passage:CAT-eq-8 -->
<!-- claim:eq-8 -->

> Outward pointer condition at address s: X_j[p_{i,s,j}] = 0 for every j != i. Eq. 8 of the paper is the case s=s_i.

**Argument:** [§4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-construction-context), [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-address-winner).

<!-- /passage:CAT-eq-8 -->

#### def-winner

<a id="CAT-def-winner"></a>
<!-- passage:CAT-def-winner -->
<!-- claim:def-winner -->

> Column i is a winner iff X_i=1^m, every P(A_{i,h}) is defined, and the cell B_{i,s_i} contains correct evaluation transcripts on all A_{i,h} and pointers satisfying eq-8.

**Argument:** [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-address-winner).

<!-- /passage:CAT-def-winner -->

#### def-F

<a id="CAT-def-F"></a>
<!-- passage:CAT-def-F -->
<!-- claim:def-F -->

> F_{k,m}(y)=1 if some column of y is a winner, else 0. It is a total Boolean function on all input bit strings.

**Argument:** [§4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-construction-context), [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-address-winner).

<!-- /passage:CAT-def-F -->

#### cor-unique-winner

<a id="CAT-cor-unique-winner"></a>
<!-- passage:CAT-cor-unique-winner -->
<!-- claim:cor-unique-winner -->

> For every input, at most one column is a winner.

**Argument:** [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-unique).

<!-- /passage:CAT-cor-unique-winner -->

#### def-win-at-address

<a id="CAT-def-win-at-address"></a>
<!-- passage:CAT-def-win-at-address -->
<!-- claim:def-win-at-address -->

> WinsAt(y,i,s) holds iff X_i=1^m, for every h the transcript in B_{i,s} on A_{i,h} is correct with outputs d=1 and b=s_h, and eq-8 holds at s. The paper's wording, i is a winner and s=s_i, is equivalent by claim-winner-fidelity.

**Argument:** [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-fidelity).

<!-- /passage:CAT-def-win-at-address -->

#### def-K

<a id="CAT-def-K"></a>
<!-- passage:CAT-def-K -->
<!-- claim:def-K -->

> K_{k,m} = m + (m-1) + r(S_{k,m}+2) = O_k(m (log m)^3).

**Argument:** [§4.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-local-tests), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-verifier).

<!-- /passage:CAT-def-K -->

#### lem-2.2.i

<a id="CAT-lem-2.2.i"></a>
<!-- passage:CAT-lem-2.2.i -->
<!-- claim:lem-2.2.i -->

> For every input y and (i,s) in [m] x {0,1}^r: i wins at s iff all K_{k,m} tests pass, namely (a) X_i[b]=1 for each b; (b) for each j != i, X_j[p_{i,s,j}]=0; (c) for each h and each non-input gate, the claimed value equals the gate function of its predecessors, read from the transcript or from A_{i,h}; (d) for each h, claimed d=1 and claimed b=s_h. Each test is computed by a deterministic adaptive bit-query decision tree of depth at most max(3,l+1), which is l+1 for m>=4: a pointer test reads l pointer bits, then the one target bit they select, while gate tests read at most three fixed bits. A pointer test is not a function of a small fixed set of bits: it can depend on all l+m pointer and target coordinates.

**Argument:** [§4.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-local-tests), [§4.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-local-equivalence), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-verifier).

<!-- /passage:CAT-lem-2.2.i -->

#### lem-2.2.ii

<a id="CAT-lem-2.2.ii"></a>
<!-- passage:CAT-lem-2.2.ii -->
<!-- claim:lem-2.2.ii -->

> Each test is evaluated exactly with O(log m) bit queries, also coherently with the same bound with test indices in superposition. The number of tests and the indexing convention are the same for every (i,s).

**Argument:** [§4.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-local-tests), [§4.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-coherent-tests), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-verification-proof).

<!-- /passage:CAT-lem-2.2.ii -->

#### lem-2.2

<a id="CAT-lem-2.2"></a>
<!-- passage:CAT-lem-2.2 -->
<!-- claim:lem-2.2 -->

> Conjunction of lem-2.2.i and lem-2.2.ii.

**Argument:** [§4.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-coherent-tests).

<!-- /passage:CAT-lem-2.2 -->

#### cor-local-dichotomy

<a id="CAT-cor-local-dichotomy"></a>
<!-- passage:CAT-cor-local-dichotomy -->
<!-- claim:cor-local-dichotomy -->

> A winner has an address at which every test passes; a nonwinner has a failing test at every address.

**Argument:** [§4.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-dichotomy).

<!-- /passage:CAT-cor-local-dichotomy -->

#### claim-winner-fidelity

<a id="CAT-claim-winner-fidelity"></a>
<!-- passage:CAT-claim-winner-fidelity -->
<!-- claim:claim-winner-fidelity -->

> Given the correctness half of lem-2.1.iii: WinsAt(y,i,s) iff X_i=1^m, every P(A_{i,h}) is defined, s=s_i, the transcripts in B_{i,s} are correct, and eq-8 holds. Hence exists s, WinsAt(y,i,s) is the paper's winner condition.

**Argument:** [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-fidelity).

<!-- /passage:CAT-claim-winner-fidelity -->

### B.4. Amplification and the returned state

Section 5.6 gives the state calculation and bounded fresh-trial procedure. The [amplification theorem for abstract procedures][src-amplification] matches the abstract amplification assertion, including its successful state and cap. The implemented upper bound uses a physical label-law theorem. Those two statements do not supply the missing identification of a designated physical output subsystem; Appendix G.7 states that stronger target completely. Thus an exact abstract tie for Lemma 3.1 must not be read as closing the physical-state bridge. Trial parameters, mixture and recursion have separate formal suppliers.

#### def-grover-trial

<a id="CAT-def-grover-trial"></a>
<!-- passage:CAT-def-grover-trial -->
<!-- claim:def-grover-trial -->

> M = ceil(10/sqrt(gamma)). A trial picks with probability 1/2 l=0, and with probability 1/2 a uniform l in {0,...,M-1}, applies l Grover iterations to A|0>, and measures the success bit. The procedure runs ceil(log(1/eta)/log(40/31)) trials with fresh registers, stopping at the first success.

**Argument:** [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-grover-trial).

<!-- /passage:CAT-def-grover-trial -->

#### claim-grover-state

<a id="CAT-claim-grover-state"></a>
<!-- passage:CAT-claim-grover-state -->
<!-- claim:claim-grover-state -->

> For 0<p<1 write A|0>=sin(theta)|g>+cos(theta)|b>, 0<theta<pi/2, with g,b normalized in the successful and unsuccessful subspaces. After l Grover iterations the state is sin((2l+1)theta)|g>+cos((2l+1)theta)|b>. Hence measuring success yields |g> up to global phase, independently of l.

**Argument:** [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-grover-geometry).

<!-- /passage:CAT-claim-grover-state -->

#### claim-sin2theta

<a id="CAT-claim-sin2theta"></a>
<!-- passage:CAT-claim-sin2theta -->
<!-- claim:claim-sin2theta -->

> If gamma<=p<=1/2 then sin(2theta)=2 sqrt(p(1-p)) >= sqrt(gamma).

**Argument:** [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-small-probability).

<!-- /passage:CAT-claim-sin2theta -->

#### eq-9

<a id="CAT-eq-9"></a>
<!-- passage:CAT-eq-9 -->
<!-- claim:eq-9 -->

> If gamma<=p<=1/2 and M=ceil(10/sqrt(gamma)), then (1/M) sum_{l=0}^{M-1} sin^2((2l+1)theta) >= 1/2 - 1/(2M|sin 2theta|) >= 9/20.

**Argument:** [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-average-exact), [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-small-probability).

<!-- /passage:CAT-eq-9 -->

#### lem-3.1

<a id="CAT-lem-3.1"></a>
<!-- passage:CAT-lem-3.1 -->
<!-- claim:lem-3.1 -->

> For 0<gamma<=1/2 and 0<eta<1/2 there is a single procedure, black-box in A and A^{-1} and with call counts depending only on gamma and eta, using O(gamma^{-1/2} log(1/eta)) calls for every p and on every branch, such that for every state preparation A with a success bit, success probability p and, if p>0, normalized successful state |g>: it reports failure or produces a successful outcome; conditional on success the output is |g> up to global phase; if p>=gamma, failure probability <=eta; if p=0 it always reports failure.

**Argument:** [§5.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-amplification-statement), [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-amplification-proof).

<!-- /passage:CAT-lem-3.1 -->

### B.5. Tournament sampling

The matrix inequalities lead to the ideal process and its shrinking expected weight in §5.2. The implemented sampler must then be related to that process. The literal tensor equation and the finite bounded-list theorem are now explicit declarations. Some component rows about the sampler, coupling and cost retain partial ties because each row combines a construction or interpretation with an estimate. The list theorem supplies one common witness and the complete list-law conclusion; it does not assert equality of every retained tensor state in the alternative measured route.

#### def-aij

<a id="CAT-def-aij"></a>
<!-- passage:CAT-def-aij -->
<!-- claim:def-aij -->

> For a fixed oracle input and a coherent comparison circuit, a_{ij} is the probability that i is reported as defeating j when the result is measured, using one circuit per unordered pair; a_{ii}=0.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparison-model).

<!-- /passage:CAT-def-aij -->

#### eq-10

<a id="CAT-eq-10"></a>
<!-- passage:CAT-eq-10 -->
<!-- claim:eq-10 -->

> a_{ij}+a_{ji}=1 for i != j, and a_{ii}=0.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparison-model), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparison-law).

<!-- /passage:CAT-eq-10 -->

#### def-T-eps

<a id="CAT-def-T-eps"></a>
<!-- passage:CAT-def-T-eps -->
<!-- claim:def-T-eps -->

> For m>=2: T=ceil(log_2(1000m)), epsilon=1/(1000T).

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-parameters).

<!-- /passage:CAT-def-T-eps -->

#### eq-11

<a id="CAT-eq-11"></a>
<!-- passage:CAT-eq-11 -->
<!-- claim:eq-11 -->

> i_* is dominant if a_{i_* j} >= 1-epsilon for every j != i_*.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-parameters).

<!-- /passage:CAT-eq-11 -->

#### def-ideal-process

<a id="CAT-def-ideal-process"></a>
<!-- passage:CAT-def-ideal-process -->
<!-- claim:def-ideal-process -->

> Ideal process: w_i=1 for all i, W=sum_i w_i. While W>0 sample p with probability w_p/W, append p to the list, update by eq-12. If W=0, leave list and weights unchanged. Run T steps.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-ideal-process).

<!-- /passage:CAT-def-ideal-process -->

#### eq-12

<a id="CAT-eq-12"></a>
<!-- passage:CAT-eq-12 -->
<!-- claim:eq-12 -->

> Update w_i <- w_i a_{ip} for all i in [m].

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-ideal-process).

<!-- /passage:CAT-eq-12 -->

#### eq-13

<a id="CAT-eq-13"></a>
<!-- passage:CAT-eq-13 -->
<!-- claim:eq-13 -->

> For W>0: E[W_new | w] = (1/W) sum_{p,i} w_p w_i a_{ip} = (W^2 - sum_i w_i^2)/(2W) <= W/2.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-weight-drift).

<!-- /passage:CAT-eq-13 -->

#### claim-expected-WT

<a id="CAT-claim-expected-WT"></a>
<!-- passage:CAT-claim-expected-WT -->
<!-- claim:claim-expected-WT -->

> The bound of eq-13 also holds when W=0, hence E[W_T] <= m/2^T.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-weight-drift).

<!-- /passage:CAT-claim-expected-WT -->

#### claim-weight-lb

<a id="CAT-claim-weight-lb"></a>
<!-- passage:CAT-claim-weight-lb -->
<!-- claim:claim-weight-lb -->

> If i_* satisfies eq-11 and has not been selected in t<=T steps, then w_{i_*} >= (1-epsilon)^t >= 1-T epsilon > 1/2. Hence W>0 until it is selected.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-dominant-weight).

<!-- /passage:CAT-claim-weight-lb -->

#### eq-14

<a id="CAT-eq-14"></a>
<!-- passage:CAT-eq-14 -->
<!-- claim:eq-14 -->

> Pr[i_* absent from the ideal list] <= Pr[W_T >= 1/2] <= 2m/2^T.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-dominant-weight).

<!-- /passage:CAT-eq-14 -->

#### construct-sampler

<a id="CAT-construct-sampler"></a>
<!-- passage:CAT-construct-sampler -->
<!-- claim:construct-sampler -->

> Given pivots p_1,...,p_t with t<T: prepare uniform |i> over [m], compare i with each pivot in a fresh workspace, set the success bit iff every comparison says i defeats its pivot, keeping all garbage. Apply lem-3.1 with gamma=1/(2m), eta=epsilon. On failure stop and return the accumulated list; otherwise measure the index, append, and continue for at most T stages.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-stage-state), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-quantum-tournament).

<!-- /passage:CAT-construct-sampler -->

#### eq-15

<a id="CAT-eq-15"></a>
<!-- passage:CAT-eq-15 -->
<!-- claim:eq-15 -->

> Pre-success state: m^{-1/2} sum_{i=1}^m |i> tensor_{b=1}^t |phi(i,p_b)>.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-stage-state), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-evidence).

<!-- /passage:CAT-eq-15 -->

#### claim-success-prob

<a id="CAT-claim-success-prob"></a>
<!-- passage:CAT-claim-success-prob -->
<!-- claim:claim-success-prob -->

> Conditional on index i the success probability is prod_{b=1}^t a_{i p_b} = w_i (empty product 1). Total success probability is W/m, and conditional on success the index has law w_i/W exactly.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-stage-law), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-evidence).

<!-- /passage:CAT-claim-success-prob -->

#### claim-coupling

<a id="CAT-claim-coupling"></a>
<!-- passage:CAT-claim-coupling -->
<!-- claim:claim-coupling -->

> Until i_* is first selected, W/m >= 1/(2m), so at each such history the sampler fails with probability <=epsilon and otherwise follows the exact ideal pivot law. The real list contains i_* except with probability <= 2m/2^T + T epsilon.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-coupling), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-evidence), [§5.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-continuation-induction).

<!-- /passage:CAT-claim-coupling -->

#### claim-tournament-cost

<a id="CAT-claim-tournament-cost"></a>
<!-- passage:CAT-claim-tournament-cost -->
<!-- claim:claim-tournament-cost -->

> Stage t uses O(c(t+1)) queries per call; lem-3.1 uses O(sqrt(m) log(1/epsilon)) calls; the sum over t<T is O(c sqrt(m) T^2 log T), a fixed cap on every branch.

**Argument:** [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-cost), [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-finite-budget).

<!-- /passage:CAT-claim-tournament-cost -->

#### prop-3.2

<a id="CAT-prop-3.2"></a>
<!-- passage:CAT-prop-3.2 -->
<!-- claim:prop-3.2 -->

> Let m>=2, T=ceil(log_2(1000m)), epsilon=1/(1000T). For a coherent comparison circuit controlled by two candidate indices, reversible with all workspace retained, using at most c>=1 bit queries, with probabilities a_{ij} satisfying eq-10, there is a quantum algorithm making O(c sqrt(m) T^2 log T) queries on every branch and returning a list of at most T candidates such that, for every fixed oracle input and every i_* satisfying eq-11, the list contains i_* with probability >= 1-2m/2^T-T epsilon.

**Argument:** [§5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-purpose), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparison-model), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-cost), [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-evidence).

<!-- /passage:CAT-prop-3.2 -->

### B.6. Decoding and verification

Sections 5.3–5.4 put decoding, tournament comparison and verification into one algorithm and bound its actual cap. Several source rows describe complete procedures or their state interpretation, while their named ties expose only particular laws or numerical bounds. These partial component correspondences are compatible with the complete final quantum upper endpoint. Promise correctness and all-input budget control have different domains and are retained separately in the ordinary argument and the formal witnesses.

#### def-decode

<a id="CAT-def-decode"></a>
<!-- passage:CAT-def-decode -->
<!-- claim:def-decode -->

> decode(i): run the algorithm of lem-2.1.ii on each A_{i,h}, h in [r], with error <= epsilon/r, retaining workspace. Output a string in {0,1}^r on every input.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-decode).

<!-- /passage:CAT-def-decode -->

#### claim-decode-cost

<a id="CAT-claim-decode-cost"></a>
<!-- passage:CAT-claim-decode-cost -->
<!-- claim:claim-decode-cost -->

> decode uses O_k(r log(r/epsilon)) = (log m)^{O_k(1)} queries. If all r instances are defined, the address is correct with probability >=1-epsilon. Otherwise it still returns some address.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-decode-cost).

<!-- /passage:CAT-claim-decode-cost -->

#### def-comparison

<a id="CAT-def-comparison"></a>
<!-- passage:CAT-def-comparison -->
<!-- claim:def-comparison -->

> Comparison of distinct columns, in sorted order: decode each in separate workspaces; read each column's pointer towards the other at its decoded address and inspect the pointed bit of the other's X string. A column disqualifies its opponent if that bit is 0. If exactly one disqualifies the other it is victorious, otherwise the smaller index. A self-comparison returns false without reading a pointer.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparator).

<!-- /passage:CAT-def-comparison -->

#### claim-comparison-state

<a id="CAT-claim-comparison-state"></a>
<!-- passage:CAT-claim-comparison-state -->
<!-- claim:claim-comparison-state -->

> The comparison uses c=(log m)^{O_k(1)} queries; its reversal costs the same. Measurement probabilities agree with the classical description, since later operations are controlled on the decoded registers in the computational basis. The resulting a_{ij} satisfy eq-10.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparator), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-comparison-law).

<!-- /passage:CAT-claim-comparison-state -->

#### claim-winner-dominates

<a id="CAT-claim-winner-dominates"></a>
<!-- passage:CAT-claim-winner-dominates -->
<!-- claim:claim-winner-dominates -->

> If i_* is a winner then for every j != i_*, a_{i_* j} >= 1-epsilon, on every input, whether or not the opponent's instances are defined.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-winner-dominates).

<!-- /passage:CAT-claim-winner-dominates -->

#### def-verify

<a id="CAT-def-verify"></a>
<!-- passage:CAT-def-verify -->
<!-- claim:def-verify -->

> verify(i): decode and measure an address s afresh. Let A prepare a uniform test index and an exact failing-test flag at (i,s), with K tests. Apply lem-3.1 with gamma=1/K and eta=epsilon. Reject if a failed test is found, otherwise accept. Output 1 iff some listed candidate is accepted.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-verifier).

<!-- /passage:CAT-def-verify -->

#### claim-verify

<a id="CAT-claim-verify"></a>
<!-- passage:CAT-claim-verify -->
<!-- claim:claim-verify -->

> A non-winner is accepted with probability <=epsilon, at every address. A true winner is rejected with probability <=epsilon, only by decoding error. Verification costs O(sqrt(K) log(1/epsilon) log m) = sqrt(m)(log m)^{O_k(1)} queries for the search, plus decoding.

**Argument:** [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-verification-proof).

<!-- /passage:CAT-claim-verify -->

#### claim-error

<a id="CAT-claim-error"></a>
<!-- passage:CAT-claim-error -->
<!-- claim:claim-error -->

> On a 0-input the error is at most T epsilon. On a 1-input it is at most 2m/2^T + T epsilon + epsilon < 1/3.

**Argument:** [§5.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-continuation-induction), [§5.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-total-error).

<!-- /passage:CAT-claim-error -->

#### claim-coherent-access

<a id="CAT-claim-coherent-access"></a>
<!-- passage:CAT-claim-coherent-access -->
<!-- claim:claim-coherent-access -->

> All superposed array accesses are ordinary bit queries. The global bit index is computed reversibly; a pointer is read in O(log m) queries; a controlled query uses load, use, unload, two queries.

**Argument:** [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-oracle-access), [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-read-compiler).

<!-- /passage:CAT-claim-coherent-access -->

#### prop-3.3

<a id="CAT-prop-3.3"></a>
<!-- passage:CAT-prop-3.3 -->
<!-- claim:prop-3.3 -->

> For every fixed k>=2, Q(F_{k,m}) <= sqrt(m) (log m)^{O_k(1)}.

**Argument:** [§5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-purpose), [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-finite-budget), [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-asymptotic-bound), [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-explicit-log6).

<!-- /passage:CAT-prop-3.3 -->

### B.7. Direct product and independent information

Section 6.1 gives both the conditional-transcript argument and the unnormalized-mass induction. The product law and terminal estimates have exact suppliers, while the value function, one-step calculation and supermartingale rows require several components. In particular, equation (16) includes both the queried factor and the unchanged factors. The available direct-product and address-guess declarations quantify finite seed spaces. The rows below allow arbitrary independent information: their ordinary reduction to a finite distribution on bounded-depth behaviours is supplied in §6.1, but no formal pushforward theorem identifying those two interfaces is asserted.

#### claim-product-law

<a id="CAT-claim-product-law"></a>
<!-- passage:CAT-claim-product-law -->
<!-- claim:claim-product-law -->

> For a deterministic algorithm, at every transcript tau of positive probability, the conditional law of (U_1,...,U_r) given tau is a product of separate conditional laws, because the event of obtaining tau is a Cartesian product of constraints on each input.

**Argument:** [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-product-law).

<!-- /passage:CAT-claim-product-law -->

#### def-value-V

<a id="CAT-def-value-V"></a>
<!-- passage:CAT-def-value-V -->
<!-- claim:def-value-V -->

> With q_h queries already made to U_h, V_h(tau) is the largest success probability for computing P(U_h) under its conditional law given tau using at most L-q_h further queries.

**Argument:** [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-conditional-values).

<!-- /passage:CAT-def-value-V -->

#### eq-16

<a id="CAT-eq-16"></a>
<!-- passage:CAT-eq-16 -->
<!-- claim:eq-16 -->

> If the next query at tau addresses U_h then E[V_h(tau') | tau] <= V_h(tau). The conditional laws and budgets of the other inputs do not change.

**Argument:** [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-conditional-values).

<!-- /passage:CAT-eq-16 -->

#### claim-supermartingale

<a id="CAT-claim-supermartingale"></a>
<!-- passage:CAT-claim-supermartingale -->
<!-- claim:claim-supermartingale -->

> E[prod_j V_j(tau') | tau] <= prod_j V_j(tau). The product is a supermartingale over at most rL queries.

**Argument:** [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-supermartingale).

<!-- /passage:CAT-claim-supermartingale -->

#### claim-final-bound

<a id="CAT-claim-final-bound"></a>
<!-- passage:CAT-claim-final-bound -->
<!-- claim:claim-final-bound -->

> At the final transcript tau, Pr[chosen vector correct | tau] <= prod_h max_b Pr(P(U_h)=b | tau) <= prod_h V_h(tau).

**Argument:** [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-supermartingale).

<!-- /passage:CAT-claim-final-bound -->

#### lem-4.1

<a id="CAT-lem-4.1"></a>
<!-- passage:CAT-lem-4.1 -->
<!-- claim:lem-4.1 -->

> Let P:D->{0,1}, D subset {0,1}^n, mu a distribution on D, L a nonnegative integer. Suppose every deterministic algorithm making at most L queries computes P under mu with success probability <=beta. If U_1,...,U_r are iid mu, every classical algorithm making at most L queries to each U_h, possibly randomized, adaptive among the r inputs, and given arbitrary additional information independent of (U_1,...,U_r), outputs (P(U_1),...,P(U_r)) with probability <=beta^r.

**Argument:** [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-direct-product-statement), [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-supermartingale), [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-weighted-values), [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-weighted-product), [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-independent-information).

<!-- /passage:CAT-lem-4.1 -->

#### claim-minimax-mu

<a id="CAT-claim-minimax-mu"></a>
<!-- passage:CAT-claim-minimax-mu -->
<!-- claim:claim-minimax-mu -->

> If L<R(P), there is a distribution mu on dom P, which is in particular nonempty, such that every deterministic tree of depth <=L has success probability <=2/3 under mu.

**Argument:** [§6.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-minimax).

<!-- /passage:CAT-claim-minimax-mu -->

#### claim-address-guess

<a id="CAT-claim-address-guess"></a>
<!-- passage:CAT-claim-address-guess -->
<!-- claim:claim-address-guess -->

> Under mu from claim-minimax-mu, for U_1,...,U_r iid mu, every classical algorithm making at most L queries to each U_h, given information independent of (U_1,...,U_r), outputs (P(U_1),...,P(U_r)) with probability <=(2/3)^r.

**Argument:** [§6.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-address-guess).

<!-- /passage:CAT-claim-address-guess -->

### B.8. Planting, discoveries and truncation

Sections 6.2–6.6 prove the planted lower bound. The complete equality-and-bound row (19) needs a conjunction theorem; a stronger probability inequality alone does not cover its equality clause. The independently uniform column is essential to that equality, as the finite selection example shows. The early/late proof of $\mathbb E Z$ and the stronger alternative search proof remain different arguments; formal support for the alternative estimate does not formalize the early/late decomposition. Likewise, the planted-average definition accepts a transcript chooser, so correctness of that transcript is an additional separately proved property. The arbitrary independent information in the address guess has the finite-seed boundary described in B.7. Signed and absolute-gap versions are distinguished in the entries and their correspondence.

#### eq-17

<a id="CAT-eq-17"></a>
<!-- passage:CAT-eq-17 -->
<!-- claim:eq-17 -->

> G = floor(mL/100).

**Argument:** [§6.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-generic-statement).

<!-- /passage:CAT-eq-17 -->

#### def-dummy

<a id="CAT-def-dummy"></a>
<!-- passage:CAT-def-dummy -->
<!-- claim:def-dummy -->

> Dummy input Y^(0): independently for each i, J_i uniform in [m], X_i has a single 0 at position J_i. All A_{i,h} are iid mu independent of the J_i. All cells B_{i,s} are one fixed blank pattern.

**Argument:** [§6.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-dummy).

<!-- /passage:CAT-def-dummy -->

#### def-planted

<a id="CAT-def-planted"></a>
<!-- passage:CAT-def-planted -->
<!-- claim:def-planted -->

> I is uniform in [m] and independent of Y^(0). Y^(1) is Y^(0) with X_I:=1^m and B_{I,s_I} filled with the correct transcripts and pointers p_{I,s_I,j}=J_j for j != I.

**Argument:** [§6.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-planted).

<!-- /passage:CAT-def-planted -->

#### claim-Y-values

<a id="CAT-claim-Y-values"></a>
<!-- passage:CAT-claim-Y-values -->
<!-- claim:claim-Y-values -->

> F_{k,m}(Y^(0))=0 and F_{k,m}(Y^(1))=1 for all sample points.

**Argument:** [§6.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-planted).

<!-- /passage:CAT-claim-Y-values -->

#### eq-18

<a id="CAT-eq-18"></a>
<!-- passage:CAT-eq-18 -->
<!-- claim:eq-18 -->

> For a deterministic algorithm with at most G queries, |Pr[outputs 1 on Y^(1)]-Pr[outputs 1 on Y^(0)]| <= Pr(the dummy run queries X_I[J_I]) + Pr(the dummy run queries any bit of B_{I,s_I}).

**Argument:** [§6.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-first-difference).

<!-- /passage:CAT-eq-18 -->

#### def-Z

<a id="CAT-def-Z"></a>
<!-- passage:CAT-def-Z -->
<!-- claim:def-Z -->

> Z is the number of columns whose zero is discovered in the dummy run.

**Argument:** [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-early-late), [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-erased-zero-identity).

<!-- /passage:CAT-def-Z -->

#### claim-uniform-zero

<a id="CAT-claim-uniform-zero"></a>
<!-- passage:CAT-claim-uniform-zero -->
<!-- claim:claim-uniform-zero -->

> Before the zero in a column is found, its location is uniform among positions of that column not yet queried, conditional on the full adaptive transcript.

**Argument:** [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-early-late).

<!-- /passage:CAT-claim-uniform-zero -->

#### claim-EZ

<a id="CAT-claim-EZ"></a>
<!-- passage:CAT-claim-EZ -->
<!-- claim:claim-EZ -->

> E Z <= 4G/m: an early discovery (fewer than m/2 distinct positions queried in that column before it) has probability <=2/m per query, giving <=2G/m in expectation; any other discovery lies in one of at most 2G/m columns receiving >=m/2 queries.

**Argument:** [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-early-late).

<!-- /passage:CAT-claim-EZ -->

#### eq-19

<a id="CAT-eq-19"></a>
<!-- passage:CAT-eq-19 -->
<!-- claim:eq-19 -->

> Pr(the dummy run queries X_I[J_I]) = E Z/m <= 4G/m^2.

**Argument:** [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-early-late), [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-zero-worlds), [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-zero-average).

<!-- /passage:CAT-eq-19 -->

#### def-heavy

<a id="CAT-def-heavy"></a>
<!-- passage:CAT-def-heavy -->
<!-- claim:def-heavy -->

> Column i is heavy if, over the entire dummy run, the algorithm makes more than L queries in total to A_{i,1},...,A_{i,r}. Repeats count.

**Argument:** [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-heavy).

<!-- /passage:CAT-def-heavy -->

#### eq-20

<a id="CAT-eq-20"></a>
<!-- passage:CAT-eq-20 -->
<!-- claim:eq-20 -->

> Pr(I is heavy) <= G/(mL).

**Argument:** [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-heavy).

<!-- /passage:CAT-eq-20 -->

#### def-simulator

<a id="CAT-def-simulator"></a>
<!-- passage:CAT-def-simulator -->
<!-- claim:def-simulator -->

> Fix i and t in {1,...,G}. A simulator receives all of the dummy input outside A_{i,1},...,A_{i,r}, runs the deterministic algorithm up to its proposed t-th query, and aborts before an (L+1)st query to those r strings in total. If it reaches time t and the proposed query is to a cell B_{i,s}, it outputs s; otherwise it outputs a fixed vector.

**Argument:** [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-simulator).

<!-- /passage:CAT-def-simulator -->

#### eq-21

<a id="CAT-eq-21"></a>
<!-- passage:CAT-eq-21 -->
<!-- claim:eq-21 -->

> For each i and t: Pr(i is nonheavy and the t-th query is in B_{i,s_i}) <= (2/3)^r.

**Argument:** [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-simulator), [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-joint-event).

<!-- /passage:CAT-eq-21 -->

#### eq-22

<a id="CAT-eq-22"></a>
<!-- passage:CAT-eq-22 -->
<!-- claim:eq-22 -->

> Pr(the dummy run queries B_{I,s_I}) <= G/(mL) + G(2/3)^r.

**Argument:** [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-cell-union).

<!-- /passage:CAT-eq-22 -->

#### eq-23

<a id="CAT-eq-23"></a>
<!-- passage:CAT-eq-23 -->
<!-- claim:eq-23 -->

> The output-probability difference is at most 4G/m^2 + G/(mL) + G(2/3)^r.

**Argument:** [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-discrepancy).

<!-- /passage:CAT-eq-23 -->

#### claim-tail

<a id="CAT-claim-tail"></a>
<!-- passage:CAT-claim-tail -->
<!-- claim:claim-tail -->

> G(2/3)^r <= (1/100) m^{2-20 log_2(3/2)} = o(1).

**Argument:** [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-tail-numeric).

<!-- /passage:CAT-claim-tail -->

#### claim-numeric

<a id="CAT-claim-numeric"></a>
<!-- passage:CAT-claim-numeric -->
<!-- claim:claim-numeric -->

> For m=4^t, r=40t, 1<=L<=m and G<=mL/100: 4G/m^2<=4/100, G/(mL)<=1/100, G(2/3)^r<=1/100, so eq-23 is at most 6/100<1/3.

**Argument:** [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-tail-numeric).

<!-- /passage:CAT-claim-numeric -->

#### prop-4.2

<a id="CAT-prop-4.2"></a>
<!-- passage:CAT-prop-4.2 -->
<!-- claim:prop-4.2 -->

> For each fixed integer k>=2 and every sufficiently large power of four m, R(F_{k,m}) > G=floor(mL/100), with L=floor(m^{1-1/k}/(log_2 m)^2).

**Argument:** [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-concrete-lower).

<!-- /passage:CAT-prop-4.2 -->

#### cor-R-omega

<a id="CAT-cor-R-omega"></a>
<!-- passage:CAT-cor-R-omega -->
<!-- claim:cor-R-omega -->

> For fixed k, R(F_{k,m}) = Omega_k(m^{2-1/k}/(log m)^2).

**Argument:** [§7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-FAMILY-ASSEMBLY), [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-concrete-lower).

<!-- /passage:CAT-cor-R-omega -->

#### prop-4.2-generic

<a id="CAT-prop-4.2-generic"></a>
<!-- passage:CAT-prop-4.2-generic -->
<!-- claim:prop-4.2-generic -->

> Let m=4^t with t>=1 and r=40t. Let P be a partial function on km bits with an exact circuit C (d=1 iff defined, and d=1 implies b=P), and F the total function built from (P,C). If 1<=L<=m and L<R(P), then R(F)>floor(mL/100).

**Argument:** [§6.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-generic-statement), [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-randomized-contradiction).


This original catalogue row specializes the coordinate count to $km$ for the Forrelation application. The [body theorem](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-generic-statement) allows any finite coordinate set and every realizing circuit.
<!-- /passage:CAT-prop-4.2-generic -->

### B.9. Passing to the exponent

Section 7 removes the floor and compares exponents for each fixed $k$. The same-family upper and lower estimates are used together. The threshold may depend on $k$; the fixed-$k$ argument of §§7.1–7.2 alone gives no joint growing-$k$ schedule. The separate uniform argument in [§7.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-GROWING-K) gives such a schedule. The no-smaller-exponent declaration and the stronger numerical suppliers have their full quantifier order recorded in the correspondence.

#### claim-floor

<a id="CAT-claim-floor"></a>
<!-- passage:CAT-claim-floor -->
<!-- claim:claim-floor -->

> For sufficiently large m, floor((m/100) floor(m^{1-1/k}/(log m)^2)) >= c_k m^{2-1/k}/(log m)^2 after decreasing c_k>0.

**Argument:** [§7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-FAMILY-ASSEMBLY), [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-floors).

<!-- /passage:CAT-claim-floor -->

#### claim-exponent-ratio

<a id="CAT-claim-exponent-ratio"></a>
<!-- passage:CAT-claim-exponent-ratio -->
<!-- claim:claim-exponent-ratio -->

> For fixed 0<=alpha<4 and integer k>=2 with 2-1/k>alpha/2: R(F_{k,m})/(1+Q(F_{k,m}))^alpha >= c_{k,alpha} m^{2-1/k-alpha/2}/(log m)^{2+alpha b_k}, which tends to infinity.

**Argument:** [§7.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-RATIO), [§1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-QUANTIFIERS).

<!-- /passage:CAT-claim-exponent-ratio -->

#### claim-no-smaller-exponent

<a id="CAT-claim-no-smaller-exponent"></a>
<!-- passage:CAT-claim-no-smaller-exponent -->
<!-- claim:claim-no-smaller-exponent -->

> For every 0<=alpha<4, alpha does not belong to the set in eq-1, because a suitable k exists with k > 1/(2-alpha/2).

**Argument:** [§7.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-NO-SMALLER).

<!-- /passage:CAT-claim-no-smaller-exponent -->

### B.10. The universal upper bound

Appendix A gives the complete ordinary derivation with coefficient $35^4$; [Appendix G.9](#R3-A-ROUTES) compares it with the complexity-library and hybrid formal routes. Its formal ties include exact or stronger endpoints and partial correspondence for several definitions, progress estimates and rounding steps. The corrected Huang statement requires $d\ge1$ for two distinct eigenvalues with equal multiplicities; at $d=0$ the matrix is the singleton zero matrix. The printed adversary prefactor is discussed with an explicit parity witness in §A.2. No statement about a corrected convention is silently substituted for what the cited edition prints.

#### def-D

<a id="CAT-def-D"></a>
<!-- passage:CAT-def-D -->
<!-- claim:def-D -->

> D(f) is the least depth of a deterministic decision tree computing f exactly on every input.

**Argument:** [§2.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-PARTIAL), [§2.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-CLASSICAL).

<!-- /passage:CAT-def-D -->

#### def-deg

<a id="CAT-def-deg"></a>
<!-- passage:CAT-def-deg -->
<!-- claim:def-deg -->

> deg(f) is the degree of the unique real multilinear polynomial agreeing with f on the cube, with degree 0 for every constant function, including the zero function. With this convention it is unchanged by replacing input or output bits by signs.

**Argument:** [§A.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-DEGREE-BLOCK).

<!-- /passage:CAT-def-deg -->

#### def-bs

<a id="CAT-def-bs"></a>
<!-- passage:CAT-def-bs -->
<!-- claim:def-bs -->

> A nonempty B subset [n] is a sensitive block at x if flipping all bits of B changes f(x). bs(f) is the maximum over x of the number of pairwise disjoint sensitive blocks at x.

**Argument:** [§A.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-DEGREE-BLOCK).

<!-- /passage:CAT-def-bs -->

#### def-Gamma-i

<a id="CAT-def-Gamma-i"></a>
<!-- passage:CAT-def-Gamma-i -->
<!-- claim:def-Gamma-i -->

> For an input-indexed matrix Gamma, (Gamma_i)_{xy}=Gamma_{xy} 1{x_i != y_i}. Matrix norms are operator norms for the Euclidean norm.

**Argument:** [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-PERRON).

<!-- /passage:CAT-def-Gamma-i -->

#### claim-perron

<a id="CAT-claim-perron"></a>
<!-- passage:CAT-claim-perron -->
<!-- claim:claim-perron -->

> A nonzero real symmetric entrywise nonnegative Gamma has a nonnegative unit eigenvector v of eigenvalue ||Gamma||.

**Argument:** [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-PERRON).

<!-- /passage:CAT-claim-perron -->

#### def-adv-progress

<a id="CAT-def-adv-progress"></a>
<!-- passage:CAT-def-adv-progress -->
<!-- claim:def-adv-progress -->

> W_t = sum_{x,y} v_x v_y Gamma_{xy} <psi_x^t | psi_y^t>, where psi_x^t is the purified state after t queries on input x.

**Argument:** [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-PROGRESS).

<!-- /passage:CAT-def-adv-progress -->

#### claim-per-query

<a id="CAT-claim-per-query"></a>
<!-- passage:CAT-claim-per-query -->
<!-- claim:claim-per-query -->

> Each query changes W by at most: |W_{t+1}-W_t| <= 2 sum_i u_i^T Gamma_i u_i <= 2 max_i ||Gamma_i||, where u_i(x)=v_x ||phi_{x,i}||.

**Argument:** [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-PROGRESS).

<!-- /passage:CAT-claim-per-query -->

#### claim-final-overlap

<a id="CAT-claim-final-overlap"></a>
<!-- passage:CAT-claim-final-overlap -->
<!-- claim:claim-final-overlap -->

> If Pr[output 1] is <=1/3 on one state and >=2/3 on another, their overlap has absolute value <=2 sqrt(2)/3. Hence |W_final| <= (2 sqrt(2)/3)||Gamma||.

**Argument:** [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-FINAL).

<!-- /passage:CAT-claim-final-overlap -->

#### lem-A.2

<a id="CAT-lem-A.2"></a>
<!-- passage:CAT-lem-A.2 -->
<!-- claim:lem-A.2 -->

> Let f be a nonconstant total Boolean function, Gamma a nonzero real symmetric entrywise nonnegative input-indexed matrix with Gamma_{xy}=0 whenever f(x)=f(y). Then Q(f) >= c ||Gamma|| / max_i ||Gamma_i|| for an absolute constant c>0.

**Argument:** [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-PROGRESS), [§A.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-ADVERSARY-FINAL).

<!-- /passage:CAT-lem-A.2 -->

#### def-Sf

<a id="CAT-def-Sf"></a>
<!-- passage:CAT-def-Sf -->
<!-- claim:def-Sf -->

> S_f is the adjacency matrix on {0,1}^n of the graph joining inputs that differ in exactly one bit and have different f-values. lambda(f)=||S_f||.

**Argument:** [§A.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-A-DEFINITIONS) (definition), [§A.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-BS-LAMBDA) (use).

<!-- /passage:CAT-def-Sf -->

#### lem-A.3.bs

<a id="CAT-lem-A.3.bs"></a>
<!-- passage:CAT-lem-A.3.bs -->
<!-- claim:lem-A.3.bs -->

> For nonconstant total f, bs(f)=O(Q(f)^2).

**Argument:** [§A.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-BS-LAMBDA).

<!-- /passage:CAT-lem-A.3.bs -->

#### lem-A.3.lambda

<a id="CAT-lem-A.3.lambda"></a>
<!-- passage:CAT-lem-A.3.lambda -->
<!-- claim:lem-A.3.lambda -->

> For nonconstant total f, lambda(f)=O(Q(f)).

**Argument:** [§A.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-BS-LAMBDA).

<!-- /passage:CAT-lem-A.3.lambda -->

#### lem-A.3

<a id="CAT-lem-A.3"></a>
<!-- passage:CAT-lem-A.3 -->
<!-- claim:lem-A.3 -->

> Conjunction of lem-A.3.bs and lem-A.3.lambda.

**Argument:** [§A.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-BS-LAMBDA).

<!-- /passage:CAT-lem-A.3 -->

#### claim-restrict-parity

<a id="CAT-claim-restrict-parity"></a>
<!-- passage:CAT-claim-restrict-parity -->
<!-- claim:claim-restrict-parity -->

> With f in sign form and d=deg f>=1, restricting variables outside a degree-d monomial's support gives g on the d-cube with nonzero parity correlation. So for some sigma in {-1,1}, U={x:g(x)=sigma x_1...x_d} has |U|>2^{d-1}, and every cube edge inside U changes g.

**Argument:** [§A.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-HUANG-RESTRICTION).

<!-- /passage:CAT-claim-restrict-parity -->

#### def-huang

<a id="CAT-def-huang"></a>
<!-- passage:CAT-def-huang -->
<!-- claim:def-huang -->

> H'_1=[[0,1],[1,0]], H'_{j+1}=[[H'_j,I],[I,-H'_j]]. Its entrywise absolute value is the cube adjacency matrix.

**Argument:** [§A.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-def-huang -->

#### claim-huang-spectrum

<a id="CAT-claim-huang-spectrum"></a>
<!-- passage:CAT-claim-huang-spectrum -->
<!-- claim:claim-huang-spectrum -->

> For d>=1, (H'_d)^2=dI and trace H'_d=0; H'_d has eigenvalues +-sqrt(d), each of multiplicity 2^{d-1}.

**Argument:** [§A.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-claim-huang-spectrum -->

#### claim-interlace

<a id="CAT-claim-interlace"></a>
<!-- passage:CAT-claim-interlace -->
<!-- claim:claim-interlace -->

> There is a nonzero v in the sqrt(d)-eigenspace supported on U; with u=|v|, u^T A_U u >= v^T H'_d v = sqrt(d)||u||^2.

**Argument:** [§A.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-claim-interlace -->

#### lem-A.4

<a id="CAT-lem-A.4"></a>
<!-- passage:CAT-lem-A.4 -->
<!-- claim:lem-A.4 -->

> Every nonconstant total Boolean f satisfies deg(f) <= lambda(f)^2.

**Argument:** [§A.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-lem-A.4 -->

#### claim-round-block

<a id="CAT-claim-round-block"></a>
<!-- passage:CAT-claim-round-block -->
<!-- claim:claim-round-block -->

> In each round of the algorithm on input x, with S the selected maximum-degree monomial's support in the current restriction, the restriction to S with all other unqueried variables set as in x is nonconstant. So some nonempty subset of S is a sensitive block at x. Blocks of different rounds are disjoint.

**Argument:** [§A.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-MONOMIAL-TREE).

<!-- /passage:CAT-claim-round-block -->

#### lem-A.5

<a id="CAT-lem-A.5"></a>
<!-- passage:CAT-lem-A.5 -->
<!-- claim:lem-A.5 -->

> Every total Boolean f satisfies D(f) <= bs(f) deg(f).

**Argument:** [§A.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-MONOMIAL-TREE).

<!-- /passage:CAT-lem-A.5 -->

#### thm-A.1

<a id="CAT-thm-A.1"></a>
<!-- passage:CAT-thm-A.1 -->
<!-- claim:thm-A.1 -->

> Every total Boolean function satisfies R(f) <= D(f) = O((1+Q(f))^4), with an absolute constant.

**Argument:** [Appendix A](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-APPENDIX-INTRO), [§A.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-QUARTIC-UPPER).

<!-- /passage:CAT-thm-A.1 -->

## Appendix F. Execution history

<a id="execution-history"></a>
This appendix records how the formal evidence accumulated. The current compared statements and their status are in [Appendix G.4](#checked-statements), and instructions for reproducing the checks are in the repository's [README](../README.md#reproducing-the-formal-checks). The passages below are an archive of earlier observations, not the current statement inventory. Use the following snapshot index before comparing their counts.

| Observation | Scope of the recorded observation | Where to read it |
| --- | --- | --- |
| Earlier supplied packet | 124 local Lean/configuration files; byte agreement across packet, receipt and dependency records, despite differing commit labels | [F.4](#history-upper-evidence) |
| 2 November targeted integration | 18 inspected declarations; named construction and Equation (19) comparisons | [F.1](#history-evidence-convention) and its individual receipts |
| 2 November global integration | Root build, five named bundles and a separate Unconditional paranoid run; 121 catalogue relations partitioned as 51 exact, 31 stronger, 39 partial | [F.1](#history-evidence-convention) |
| 3 November round-four integration | New source fingerprint; root build and dedicated comparisons listed individually | [Round-four adjudication](../research/adjudication/round4_formal.md) |
| Current reading inventory | Statement-by-statement distinctions between comparison, build, ordinary argument and review | [G.4](#checked-statements) |

Exact hashes, target lists and execution modes remain in the linked receipts. The counts above have different denominators and must not be added together.

For the current mathematical statements and their evidence, start with [Appendix G.1](#record-statement-check) and [G.4](#checked-statements). The material below records earlier executions and is not a substitute for that statement audit.

### F.1. The 2 November receipts and the earlier frozen packet

The earlier fidelity return proposed zero-query example declarations without successful receipts for those exact names. That was a statement about the frozen return, not the maintained model controls now indexed in Appendix G.4.

<a id="history-evidence-convention"></a>
<!-- passage:history-evidence-convention -->
The frozen receipts record a successful root build and comparisons in the Foundations, Separation and Unconditional bundles; Unconditional also records a paranoid pass. In Foundations the named comparisons include the [three equivalences between complexity bounds and budget tests][cmp-le-iff], each of the three read-all inequalities, and the $R$ and $Q$ renaming equalities. The $D$ renaming equality is built but has no named comparison in that packet. The partial-domain/correctness wrappers, oracle wrapper, output-mass identities, deferred-measurement theorem, and equivalent universal-exponent formulations likewise have build support there, without a named comparison. The real-power family has a build and a supplied selected axiom audit, without a named comparison. Unconditional compares the complete floor-form theorem, exponent endpoint and cubic refutation; Separation compares the universal upper endpoint. Comparison membership belongs to those exact declarations, not automatically to every declaration used by their proofs. An absent named comparison is recorded as unknown, rather than inferred from a nearby passing wrapper.

**Targeted verification of 2 November.** The integration's [native receipt of 2 November 2026](../corpus/receipts/lean-build-round3-targeted-2026-11-02T204814950389+0000.json) records successful builds and type/axiom inspection for the two equation (19) conjunctions, the independently specified product experiment, the construction strengthened by the support diagnostic, and the named finite semantic checks. All 18 inspected declarations use only Lean's three standard axioms (propositional extensionality, the axiom of choice and quotient soundness) as transitive axioms. On the same source snapshot, the dedicated Comparators accepted the [construction conjunction](../corpus/receipts/comparator-round3-construction-support-2026-11-02T204814950389+0000.json), the [independent product-law target](../corpus/receipts/comparator-round3-eq19-independent-2026-11-02T204814950389+0000.json), and the [direct conjunction of identity and hit-probability bound](../corpus/receipts/comparator-round3-eq19-direct-2026-11-02T204814950389+0000.json) for equation (19), which is the [whole erased-zero theorem][src-equation-19]. The other whole-display wrapper, the [identity with the bound on the divided expectation][src-equation-19-expectation], has build and axiom evidence but no separate Comparator receipt; acceptance is not transferred between the two forms.

The three deliberate controls have different intended outcomes:

| Control | Recorded outcome | Meaning |
| --- | --- | --- |
| [Missing equality](../corpus/receipts/comparator-round3-eq19-missing-equality-2026-11-02T204814950389+0000.json) | Rejected | A bound alone does not match the conjunction. |
| [Changed threshold](../corpus/receipts/comparator-round3-threshold-mutation-2026-11-02T204814950389+0000.json) | Rejected | The altered specification differs. |
| [Shared impossible premise](../corpus/receipts/comparator-round3-shared-bad-spec-blindness-2026-11-02T204814950389+0000.json) | Accepted | Both modules share the same bad specification. |

The last receipt credits no paper declaration: acceptance demonstrates agreement, not semantic correctness. These are targeted source-bound observations; the dated integration review records the global build, comparisons and dependency export separately.

**Global verification of 2 November.** The same source snapshot also has a successful [root build and dependency export](../corpus/receipts/lean-build-root-2026-11-02T205500674428+0000.json). The refreshed [Foundations](../corpus/receipts/comparator-Foundations-2026-11-02T205755119082+0000.json), [Construction](../corpus/receipts/comparator-Construction-2026-11-02T205620278544+0000.json), [Tournament](../corpus/receipts/comparator-Tournament-2026-11-02T210431678518+0000.json), [Separation](../corpus/receipts/comparator-Separation-2026-11-02T210108868598+0000.json) and [Unconditional](../corpus/receipts/comparator-Unconditional-2026-11-02T211003816536+0000.json) bundles all passed their named comparisons; Unconditional also passed a separate [paranoid check](../corpus/receipts/comparator-Unconditional-2026-11-02T212245429608+0000.json). The existing controls for a changed definition, foreign axiom, missing declaration, admitted proof and weakened conclusion were rejected for their intended reasons. The full receipt inventory is retained in the integrated correspondence.

On 2 November every catalogue row had a mathematical-fidelity review current for those sources and at least one qualifying built declaration. This does not make every complete row a Lean theorem or a compared theorem: the reviewed relations were 51 exact, 31 stronger and 39 partial. Only 4 rows (Lemma 2.2, its parts (i) and (ii), and equation (19)) have direct comparison evidence: Comparator was configured with their own declarations. Eight more, including Theorem 1.1 and the definitions of $R$, $Q$ and $D$, were credited by earlier receipts only because a compared wrapper theorem restates them; that credit is recorded as wrapper-mediated, not as a comparison of the declaration itself. The other rows' comparison state is `not_run` under the evidence policy, not an inference that no historical comparison ever occurred. Dependency reach is a further question about particular proof roots, recorded independently of build and comparison. For example, the bounded-list tournament wrapper is built, but the headline root uses the measured-label amplifier rather than that wrapper; [G.7](#upper-current-formal-scope) identifies both routes. The [correspondence record](reasoning_record_correspondence.json) retains their separate dependency observations. The remaining formal boundaries, including arbitrary-information transport and the physical successful-state bridge, are still stated explicitly.

**Inspecting the selected formal dependencies.** The [recorded native views](../corpus/native_extractions/round3/README.md) expose the complete selected local closures for the direct equation (19) conjunction, the independently specified product-law conjunction, and the finite semantic goals. They retain the actual adapter reports, graphs, selected views, build receipts and successful validate/select/inspect commands. Their local reports have complete scope, but each exported graph remains explicitly partial at external Mathlib, Init and Batteries declarations. These views make the stated formal objects and their dependencies inspectable; they are not an additional proof, a mathematical-fidelity judgment or a fresh-clone reproducibility result.
<!-- /passage:history-evidence-convention -->

The round-four integration of 3 November 2026 reran the root build, the dependency export, the five baseline bundles and the five baseline negative controls on the integrated sources, and added dedicated comparisons for the finite-seed direct product, the degree and zero-cost model checks, the real-leaf estimates, the uniform amplifier and the sharp decoder; [the round-four formal adjudication](../research/adjudication/round4_formal.md) lists every receipt. Adding sources changes the global source fingerprint, so the 2 November receipts above describe the earlier sources.

### F.2. Forrelation promise and circuit

<a id="forr_current_evidence"></a>
<!-- passage:forr_current_evidence -->
The source assessed here is the packet snapshot labeled `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Its timestamped root-build receipt matches all 124 supplied local Lean/configuration files; the relevant integrated helper modules also have source-matched native passes. The supplied audit prints the principal helper theorem types and reports only the permitted Lean axioms. These are inspected records of previous runs. The returned section review did not run Lean or Comparator anew, and no Comparator receipt supplied with that return names these Forrelation helper declarations. The round-three integration’s root build of 2 November and exact comparison scope are recorded separately in [F.1](#history-evidence-convention).

The reviewed wrappers jointly state the normalization, promise, and integer numerator: the [Walsh definitions][src-walsh], the [alternating product and its threshold][src-forr-product], the [complete promise][src-forr-promise] and the [integer form of the numerator][src-forr-integer]. The two threshold equivalences and the actual all-input output rules are split between the [integer comparisons][src-forr-tests] and the [output rules of the constructed circuit][src-forr-output-bits]. The coherent physical conclusion is the [physical implementation of part (ii)][src-lemma21-ii]. The circuit endpoint and bound are the [existence of the circuit][src-forr-circuit-exists] and the [circuit bound of part (iii)][src-lemma21-iii]. The finite census is recorded in the [checks of small instances][src-forr-census].

Two exact correspondences remain narrower than the surrounding ordinary proof: the supplied implementation has a $2qk$, rather than a formally packaged $qk$, bit-query cap; and the arithmetic contracts establish modular representation with correct final signs, rather than a signed interpretation of every intermediate register. Neither qualification weakens Lemma 2.1(ii)–(iii). The packet also contains [Lemma 2.1 as one statement][src-lemma21], a conjunction including the separately proved randomized lower bound; its presence updates the old evidence sentence in §3.2, without supplying a new proof of that lower bound in this section. Exact types, premises, routes, and receipt references are in [correspondence.json](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/correspondence.json) and [LEAN_GAPS.md](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/LEAN_GAPS.md).
<!-- /passage:forr_current_evidence -->

<a id="history-construction"></a>
### F.3. Addressed construction

<a id="history-construction-evidence"></a>
<!-- passage:history-construction-evidence -->
The frozen packet includes a source-bound successful root-build receipt for the cited declarations. A later selected type/axiom audit includes the newer Paper construction wrappers. Audit membership is recorded name by name in the [construction correspondence](../research/returns/round3/members/04_addressed_construction/correspondence.json); it is not asserted for all older core declarations. Their 124 recorded local Lean/configuration hashes match the supplied packet bytes; the returned section review did not rerun Lean. The round-three integration of 2 November separately performed the root build and targeted construction comparison recorded in [F.1](#history-evidence-convention). The Construction Comparator configuration names the [four checked winner wrappers][cmp-winners]: uniqueness of the winning pair, uniqueness of the gate-consistent transcript, and the two halves of winner dominance. The source theorems they forward to have wrapper-mediated credit only. It does not compare the newer complete local-test theorem. Old source comments and earlier returns calling those files unelaborated describe an earlier stage; the exact receipts and their scope are retained in the evidence sidecar. No human review is claimed.
<!-- /passage:history-construction-evidence -->

### F.4. Quantum upper bound

<a id="history-upper-evidence"></a>
<!-- passage:history-upper-evidence -->
The reviewed packet contains a successful source-bound root build receipt and later exact-type/axiom auditing, in addition to focused module passes. The former record labels its commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`, while the packet manifest labels its repository commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`. For that frozen local Lean/configuration closure, all 124 supplied source hashes agree across the packet files, evidence snapshot, root receipt, dependency export and axiom verdict. This makes the recorded evidence applicable to those exact bytes despite the differing commit labels. Those are retained earlier executions; the round-three integration’s new native runs are recorded separately in [F.1](#history-evidence-convention). The recorded toolchain is `leanprover/lean4:v4.36.0-rc2`; the dependency pins are preserved in the source receipt.
<!-- /passage:history-upper-evidence -->

### F.5. Direct product

<a id="history-direct-product-evidence"></a>
<!-- passage:history-direct-product-evidence -->
The supplied receipts record successful native compilation of the packet’s exact
source bytes; the returned section review made no fresh Lean run. The round-three
integration’s 2 November root build and comparison scope are recorded in [F.1](#history-evidence-convention). The headline dependency
closure still uses the unnormalized route, and no exact-declaration
Comparator pass is supplied in that snapshot for the direct-product helpers described in its correspondence file. The conditional-value file's
old “UNELABORATED” header predates the successful receipts. Exact types,
byte checks, declaration membership, and the limits
of the recorded evidence are in [correspondence.json](../research/returns/round3/members/06_direct_product/correspondence.json), [lean_types.json](../research/returns/round3/members/06_direct_product/lean_types.json),
and [LEAN_GAPS.md](../research/returns/round3/members/06_direct_product/LEAN_GAPS.md). The arbitrary-information finite-behavior reduction,
the generic joint-event truncation corollary, and the combined identity
(6.11) are ordinary deductions supplied here; they are not new Lean builds
or new Comparator passes.
<!-- /passage:history-direct-product-evidence -->

### F.6. Exponent and Appendix A

The current exponent endpoint and the three quartic proof routes are indexed in [G.9](#ROOT-EXPONENT-CORRESPONDENCE). This section records the earlier checks supporting those declarations.

An earlier annex transcription put an extra square root around the full adversary denominator. Correcting that transcription did not resolve the separate factor-two discrepancy in the inspected Špalek–Szegedy display, tested by the parity witness in Appendix A.2.

<a id="history-exponent-evidence"></a>
<!-- passage:history-exponent-evidence -->
The timestamped root-build receipt covers the exponent declarations now listed in [Appendix G.9](#ROOT-EXPONENT-CORRESPONDENCE) and binds the supplied source bytes. The reviewed type-and-axiom audit separately covers the newer named-family and quotient declarations. The timestamped Unconditional Comparator receipt covers the final compared declarations, not every explanatory helper. The challenges share the maintained definitions and theorem specifications; independent compilation does not make them independently authored mathematical tests. These descriptions identify the earlier supplied receipts. The round-three integration of 2 November also performed the new root build, named comparisons and paranoid check recorded in [F.1](#history-evidence-convention); that execution does not create additional helper theorems or extend the earlier selected type-and-axiom audit.
<!-- /passage:history-exponent-evidence -->

<a id="history-appendix-a-evidence"></a>
<!-- passage:history-appendix-a-evidence -->
The source-bound native receipts record successful compilation of the ten `Paper/AppendixA*.lean` modules. After the root build, the recorded type and allowed-axiom audit passed for the reviewed declarations. This supersedes the historical “unelaborated” comments retained in the source and the baseline's statements that these intermediate theorems have no formal ties. The Appendix-specific type-and-axiom audit is retained evidence from the earlier review. The round-three integration of 2 November also performed a new root build and the named comparisons recorded in [F.1](#history-evidence-convention); it does not claim a new Appendix-specific type-and-axiom audit. The complete types, exact source hashes and receipt locations are in the [Appendix A correspondence](../research/returns/round3/members/08_reviewed/quartic_r3_08_return/correspondence.json).
<!-- /passage:history-appendix-a-evidence -->

### F.7. Earlier drafts

The earlier [short expert draft](../research/returns/funnel/2_short_expert_paper/) and [examples-first draft](../research/returns/funnel/3_examples_first_exposition/) are preserved advisory returns from an earlier round. The maintained [expert companion](expert_companion.md) and [exposition](exposition.md) are the current reading copies. The archived drafts have not been refreshed against this integration. Their main theorem belongs to §§1 and 7 here; their construction, tournament and planted proof belong to §§4, 5 and 6.

## Appendix G. Formal statements and evidence

<a id="formal-appendix"></a>
A Lean 4 formalization accompanies this record. Its four headline targets are the separation family, the optimal exponent, failure of a cubic bound and eventual fixed-$k$ Forrelation hardness. They are written in the separate [statement file][statement-file] against definitions of the query models, and Comparator checks that separately compiled proofs establish those types using only the three standard axioms. This appendix describes what the formalization checks and where its statements differ from the claims of the record. No person has reviewed the definitions, the proofs or this record.

### G.1. Checking one statement

<a id="record-statement-check"></a>
One configured statement, checked against Theorem 1.1, shows what the formalization establishes.

1. Read the [compared headline theorem][thm-headline] beside Theorem 1.1 in §1. Its quantifiers run $\forall k\ \exists S,A,b,t_0\ \forall t\ \exists\mathcal C$, with one circuit for both bounds. Here $S$ is a coefficient in $\mathcal C.\mathrm{size}\le S\,m(2t)^2$, not the earlier actual gate count; $A$ is the quantum-query coefficient, $b$ its logarithmic exponent and $t_0$ the dyadic-size threshold. Its lower bound is the integer form $\lfloor mL/100\rfloor<R(F_{k,m})$, which implies (2) by the floor calculation of §6.6.
2. Read the [definition of $R$][def-R] and the [definition of $Q$][def-Q] in the same file against §§2.1–2.4: one algorithm for every promised input, success probability at least $2/3$, and a cap that holds on every input and every branch. The classical read-all witnesses of [§2.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-CLASSICAL) and quantum witness of [§2.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-ADAPTIVE) make each complexity the minimum of a nonempty set of caps.
3. Check that the [solution file][statement-solution] proves the statement by forwarding to an implementation theorem, and that the [configuration][statement-config] names it.
4. Read the two-bit OR calculation in [§2.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-OR) against these definitions, whose randomized complexity is one because the threshold $2/3$ is inclusive; the semantic controls of Appendix G.3 state such values against the same definitions.
5. Read [the separation-family paragraph in G.4](#formal-separation-family): confirm its exact configured comparison and distinguish its existential logarithmic exponent from the built explicit-constants theorem.

This route exposes the proposed correspondence between the compared type, Theorem 1.1 and the query models of §2 for mathematical inspection. Comparator establishes that the submitted proofs inhabit the configured types under the shared definitions. Deciding that those definitions express the intended theorem is a separate semantic judgment; no human review is claimed.

<a id="formal-models-map"></a>
### G.2. What the formal models establish

The formal model uses the domain-and-value convention of §2.1. The detailed comparison below distinguishes a partial promise from the embedding of an already total function; the [construction domain wrappers][src-construction-models] prove the relevant translation and correctness conditions.

The [physical compiler][src-runs] converts an abstract coordinate read into ordinary bit queries. An abstract read consists of a coordinate function on basis labels, an involutive permutation of those labels, and an optional sign, where the permutation preserves both its coordinate and its sign. Given a basis label, the compiler embeds the abstract register into the physical coordinate, answer-bit, and workspace registers, loads the queried bit, applies the indicated signed permutation if that bit is one, queries the unchanged coordinate again, and returns to the chosen embedding. On bit zero it is the identity and on bit one it is exactly the prescribed signed involution, so both actions preserve inner products. The finite isometries used to place the active register extend to unitaries on a sufficiently large finite workspace by completing an orthonormal basis, so the bit queries are the only input-dependent gates.


The bridges between the formal models and conventional formulations are of three kinds.

**Definitions.** Partial functions with a domain; one algorithm with a global cap; finite mixtures of decision trees for $R$; programs with fixed gates and the bit oracle for $Q$ (§§2.1–2.4).

**Proved translations.** Minima of nonempty sets of caps through read-all witnesses; renaming coordinates; deferred measurement as a fixed sequence of controlled phase queries with the same acceptance mass for every input and every starting vector (§2.2, §2.5).

**Ordinary identifications.** Finite seed spaces in place of arbitrary randomness and recursive cap compliance as observable query counts interpret the classical reduction. The basis change from a general projector to a basis-label predicate belongs to the stronger successful-state specification in G.7, which is not a premise of the headline measured-label upper bound (Appendices G.7–G.8).

<a id="ROOT-EVIDENCE-CONVENTION"></a>
<!-- passage:ROOT-EVIDENCE-CONVENTION -->
The formal interpretation starts with the order of the mathematical choices: choose one algorithm, then require its correctness and its query cap for every relevant input. A theorem about a differently quantified algorithm, a different promise, or only one part of a displayed conjunction would not establish the same statement. The definitions in §§2.1–2.5 make these choices explicit. Here we describe their formal counterparts and the particular translations used later. Complete source signatures, including the circuit and workspace quantifiers, are accessible in the retained [model contract](../research/returns/round3/members/01_models_evidence/model_contract.json) and [declaration correspondence](../research/returns/round3/members/01_models_evidence/correspondence.json); [Appendix B](#ROOT-CATALOGUE-INTRO) follows every numbered source claim.

**The partial function and its domain.** For a finite coordinate type $I$, a formal [partial Boolean function][def-partial] on $I$ is a function from [bit inputs][def-bit-input] on $I$ to optional Boolean values. A defined value records both membership in the promise and the required answer. An undefined value imposes no correctness requirement. This is the domain-and-value description of §2.1, with no assumption of totality. [Totalisation][def-totalise] embeds a total Boolean function into this type by defining its value everywhere. It is that embedding, rather than an arbitrary completion of a partial function, which appears in the total-function separation statements.

**One algorithm and a global cap.** The [deterministic][def-DLe], [randomized][def-RLe] and [quantum][def-QLe] budget tests take a partial Boolean function and a natural-number budget; the complexities [$D$][def-D], [$R$][def-R] and [$Q$][def-Q] are natural numbers. In the classical cases, the witness is one decision tree or one mixture of trees, with a global depth cap and correctness on all defined inputs. In the quantum case, the witness is either the explicitly constant-on-promise alternative or one normalized initial state and one capped program, chosen before the input. This includes the constant and empty-promise cases without selecting an algorithm separately for each input. None of these definitions assumes a lower-bound theorem or any property of Forrelation.

For every finite Boolean promise the read-all construction gives
\[
 R(f)\le D(f),\qquad Q(f)\le D(f),\qquad D(f)\le |I|.
\]
An equivalence $e:I\simeq J$ simply renames the coordinates. After [renaming the coordinates][def-reindex] of $f$ by $e$, each of the three complexities is unchanged. These statements concern arbitrary finite promises: their only ordinary premises are the specified finite coordinate types and, for renaming, the equivalence. The [classical][src-le-iff-classical] and [quantum][src-le-iff-quantum] equivalences between complexity bounds and budget tests connect the numerical complexities to the budget predicates. The uniform choice and global cap remain inside those predicates; they cannot be discarded when applying the numerical inequalities.

**The physical query and its output law.** With $x$ a bit input, $i\in I$, a response bit $b$, and workspace label $z\in\operatorname{Fin}(w+1)$, the oracle acts by
\[
 \operatorname{bitOracle}_x|i,b,z\rangle
   =|i,b\mathbin{\oplus}x_i,z\rangle.
\]
It is an involutive complex linear isometry equivalence, for every input and every basis label. The construction states these [bit-oracle identities][src-query-oracle] in one wrapper. For an adaptive program $A$ and an arbitrary state vector $\psi$, the two output masses obey
\[
 \operatorname{outputMass}_A(x,\psi,b)\ge0,
 \qquad
 \operatorname{outputMass}_A(x,\psi,\mathsf{true})
 +\operatorname{outputMass}_A(x,\psi,\mathsf{false})=\|\psi\|^2.
\]
Normalization makes these masses a probability distribution. The identities themselves do not require a unit vector; this distinction matters when an intermediate branch carries unnormalized mass.

**Deferring measurements with the same witnesses.** For an adaptive program on $\operatorname{Fin}(n)$ with workspace parameter $w$ and query cap at most $T$, the [fixed-sequence normal form][src-fixed-sequence] supplies an enlarged workspace, an entry map, a fixed sequence $U$ and an output event $S$. All these witnesses are chosen before the input and initial vector. For every $x$ and $\psi$, the mass of $S$ after the length-$T$ sequence on the entered vector equals the original program's true-output mass. For a normalized vector these masses are probabilities. In symbols, the quantifier order is
\[
 \exists W',\operatorname{entry},U,S\quad\forall x,\psi:\qquad
 \operatorname{measureProb}\bigl(\operatorname{run}
 U(\operatorname{entry}\psi)\,x\,T,S\bigr)
 =\operatorname{outputMass}_A(x,\psi,\mathsf{true}).
\]
The full witness types are those of the linked source contract. The stated cap is the only additional premise of this translation. In particular, this output-law theorem should not be read as identifying a designated retained subsystem with an arbitrary normalized successful state; the stronger amplification issue is isolated in Appendix G.7.

**The family and the universal exponent.** The [universal power bound][def-universal] is a predicate on real exponents, and the [formal optimal exponent][def-alpha] is the infimum of the exponents satisfying it. Its quantifiers range over total Boolean functions on $\operatorname{Fin}(n)$, with $n\ge1$ and exponent $\alpha\ge0$, as in (1). The finite-constant and infimum formulations are explicitly related by the source wrappers. No Forrelation hypothesis belongs to this definition.

For fixed $k\ge2$, the [existential family theorem][src-equation-two] gives the real-power family bound (2), and the [named-family theorem][src-constants] names its circuit and constants. The constants and threshold are chosen after $k$ and before the size, and one circuit at each size satisfies both the quantum upper bound and the randomized lower bound. The fixed-parameter Forrelation estimate is supplied inside the unconditional proof. The [complete unconditional Theorem 1.1][src-theorem] packages the common-circuit eventual family in the integer form
\[
 R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor,
 \qquad
 L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor,
\]
together with $\alpha_{\mathrm{tot}}=4$ and the universal power bound at exponent four. Its range and threshold occur inside the conclusion. The floor-removal argument and full types are recorded in the correspondence; the integer statement and the real-power statement should not be conflated merely because they describe the same family.

The parameter-free [unconditional exponent theorem][src-alpha] gives the exponent alone. The cubic refutation states that there is no common real constant $C$ for which
\[
 \bigl(R(\operatorname{totalise}f)\bigr)_{\mathbb R}
 \le C\bigl(Q(\operatorname{totalise}f)\bigr)_{\mathbb R}^{3}
\]
for every $n\ge1$ and total $f$ on $\operatorname{Fin}(n)$. The universal upper endpoint, the [universal quartic power bound][src-universal-power], proves the universal power bound at exponent four; the headline proof uses the imported complexity-library route described in Appendix A. These are unconditional declarations. By contrast, the [conditional family bounds][src-family-conditional] retain the premise $L<R(P_{k,4^t})$, with $L$ the [lower-bound value][def-L] at $m=4^t$, in their lower-bound clause, and the [conditional form of Theorem 1.1][src-theorem-conditional] takes the [Forrelation hardness statement][def-bansal-sinha] as an explicit hypothesis. Citing either of those conditional suppliers alone does not remove its hypothesis. A restriction such as $k\ge2$ and an unproved lower-bound assumption play different mathematical roles, and their actual types preserve that difference.

<a id="evidence-checks"></a>

### G.3. Execution evidence and checks of meaning

The [correspondence record](reasoning_record_correspondence.json) separates the current catalogue observation from the frozen historical audit. It retains full available source types, ordinary premises, assumptions, mathematical-fidelity judgments, source hashes, and separate build, Comparator and dependency-reach evidence. The [dated review receipt](reasoning_record_review.json) identifies the exact observation used here. A source-fidelity judgment is not an execution receipt, and a pass for one declaration does not certify its neighbours. The immutable [baseline catalogue](../research/returns/funnel/1_long_reasoning_record/reasoning-record.md#ROOT-CATALOGUE-INTRO) and [121-row historical audit](../research/adjudication/round3_appendix_audit.json) remain earlier evidence; their absence claims are not current facts.

**Machine-readable access.** Current observations are in `current_catalogue_snapshot.rows`. The `current_in_memory_evidence` fields under `catalogue_rows` belong to the frozen audit, as `catalogue_rows_scope` explains.

Four kinds of evidence are kept apart throughout this record: an ordinary proof, a successful Lean build with its axiom audit, a Comparator comparison of a configured statement, and review of whether a formal definition models the intended mathematics. The current checked statements and their status are listed in [Appendix G.4](#checked-statements); [Appendix F](#execution-history) records how the evidence accumulated, run by run. [Appendix B](#ROOT-CATALOGUE-INTRO) and [the dated integration review](reasoning_record_review.json) give the maintained record's evidence boundary for every catalogued claim.


The challenges compile separately but mechanically share the maintained definitions and theorem specifications. Their agreement therefore establishes conformity to that specification; source review and independently specified examples address its mathematical meaning. The dependency export separately records which declarations are used by particular headline proof roots. It is not another compilation or comparison result. The retained return rechecked source-byte bindings and exact finite examples without rerunning Lean or Comparator. Its dependency pins are bound, but it does not enclose the external checkout bytes and native compiled artifacts needed for a full replay. It reports no human review.

The examples in §2.6 establish their stated costs by ordinary proofs and exact finite arithmetic. The section's exact-arithmetic checker verifies the truth tables, the one-query classical OR obstruction and the two-bit quantum interference calculation; that frozen record has no exact-example Lean or Comparator receipts. Its separate finite semantic controls distinguish per-input algorithm selection, a weakened success threshold, false completion of an undefined value, minimum rather than maximum branch cost, a strict rather than inclusive success threshold, and two deliberately wrong promise/comparison specifications. These are different failure modes of the intended model, so matching the controls is useful evidence about the definitions. It does not prove general model equivalence or constitute a Lean or Comparator execution. Conversely, a comparison of a shared specification does not, merely by passing, establish that specification's intended meaning. Ordinary proofs, full declaration types, Lean execution, Comparator execution and review of mathematical fidelity remain separate throughout this record.


The maintained [semantic controls](../lean/QuarticCorpus/Independent/Semantics.lean) give independently specified finite expectations directly against the project definitions: one-bit identity cannot have randomized cap zero; the three-way OR mixture has success $(2/3,2/3,2/3,1)$ and randomized complexity one; the true-only promise has randomized and quantum complexity zero; and the pair of sign blocks $(-1,1,1,1)$ has Forrelation value $-1$ and lies outside the one-sided promise. The two-vertex matrix $\left(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\right)$ witnesses that the actual tournament predicate is nonempty: its diagonal vanishes and its two opposite off-diagonal entries sum to one. These checks import the actual definitions but do not obtain their expected answers from generated Challenge statements. The [mutation checks](../lean/QuarticCorpus/Independent/SemanticMutations.lean) show how changing the algorithm/input quantifier order, making the threshold strict, taking an absolute value in the high Forrelation branch, or completing the undefined input by false changes the selected answers. Their scope is these precise examples, not a proof that every semantic mismatch has been excluded.

A separate [shared-specification control](../lean/QuarticCorpus/Independent/Controls/SharedAudit.lean) makes the limitation of comparison concrete. Its deliberately bad tournament predicate adds an impossible field. Two modules can agree on the resulting vacuous assertion, whereas the independent expected matrix cannot satisfy that predicate. The changed-threshold and inequality-only controls instead ask comparison to distinguish different types or definitions. The dated review records their actual native outcomes separately from the mathematical detection statements; a positive comparison of the deliberately shared bad specification is evidence of agreement, not of a correct model.


<!-- /passage:ROOT-EVIDENCE-CONVENTION -->

<a id="checked-statements"></a>
### G.4. Central statements and their evidence

The first four entries are the configured Unconditional targets. Later entries distinguish separately compared statements, built declarations, ordinary arguments and their use by the headline proof; status does not transfer from one entry to another.

The headline statements are the four configured targets of the Unconditional Comparator bundle, all in the [statement file][statement-file] whose definitions follow the models of §§2.1–2.5. Each target is proved in the paired [solution file][statement-solution] by forwarding to an implementation theorem, and the [configuration][statement-config] names exactly these four targets. The statement file ends each target with an intentional `sorry`: it is the specification, and Comparator checks that the separately compiled solution proves the same type from the same definitions using only the three standard axioms. The [receipt of 3 November 2026](../corpus/receipts/comparator-Unconditional-2026-11-03T033042571917+0000.json) records acceptance of the four configured targets on the integrated round-four sources, and a [later paranoid run the same day](../corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json), which also runs every external checker bundled with Lean and was executed as an unsandboxed local rehearsal, accepted them again; their credit extends to those configured names only. The dedicated comparisons of Lemma 2.2 and Equation (19) were rerun on the same sources and passed (receipts stamped `2026-11-03T120058951138`).

The *corpus judgments* below come from [the statement corpus](../corpus/statements.json) and [its ties](../corpus/ties.json): *exact* means that the Lean type states the claim, *stronger* that it implies the claim with more information, and *partial* that it proves only some clauses or keeps a hypothesis. Those judgments are bound to the sources of 2 November and were not refreshed after the round-four additions, so a declaration added later has no corpus row. The *textual review* is the separate comparison of 3 November in [round5_statement_fidelity.md](../research/adjudication/round5_statement_fidelity.md), made by an AI model that read the declarations and the preprint without running Lean; it does not refresh a corpus binding. Neither source is a human review.

#### The optimal exponent

The [compared exponent theorem][thm-alpha] states exactly $\alpha_{\mathrm{tot}}=4$. The corpus calls its relation to catalogue claim thm-1.1 partial because that claim also contains the universal bound and the family. The ordinary proof is in [§7.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-NO-SMALLER).

<a id="formal-separation-family"></a>
#### The separation family

The [compared separation theorem][thm-headline] is exact for catalogue claim thm-1.1. Its type is a conjunction: $\alpha_{\rm tot}=4$, the universal power-four bound, and a fixed-parameter separating family. In its family clause it gives $\lfloor mL/100\rfloor<R(F_{k,m})$ and $Q\le A\,2^t(2t)^b$, with $b$ existential and one circuit per size. This implies (2) by the floor calculation of §6.6; it does not state $b=6$ or the coefficient $1/400$. The ordinary assembly is in [§7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-FAMILY-ASSEMBLY).

#### Failure of a cubic bound

The [compared failure of the cubic bound][thm-cubic] states exactly that no real $C$ satisfies $R(f)\le C\,Q(f)^3$ for every $n\ge1$ and every total $f$. See [§7.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-NO-SMALLER) for the ordinary proof.

#### Fixed-parameter Forrelation hardness

The [compared Forrelation lower bound][thm-forrelation] is exact for Lemma 2.1(i) with an eventual threshold. It is weaker than the ordinary result in [§8.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_target), which also gives the explicit threshold $13669k^2$.

The quantifier order in the compared family statement is $\forall k\ \exists S,A,b,t_0\ \forall t\ \exists\mathcal C$, with one circuit $\mathcal C$ for both bounds, as in §1. The other central statements of this record have their own formal status, recorded by the dated receipts and [the round-four formal adjudication](../research/adjudication/round4_formal.md). The Lean links in this edition use `8357f268732746d1575e05e7de8c888e20ad3793`. Its `lean/` tree is byte-identical to the paranoid receipt revision `9a0a5cdace28594058f6df59b9b2e45a9e7c1a4f`; the editorial revision supplies no fresh Lean or Comparator execution.

| Bundle statement file | Imported vocabulary |
| --- | --- |
| Unconditional, Construction | Mathlib only |
| UniformAmplifier, RealizedCaps, ConstructionFull | Modules of the maintained development |
| Eq19 | Maintained interfaces through its independent specification |

Separate compilation has these different source boundaries; it is not a uniform claim of independently authored definitions.

<a id="formal-named-family"></a>
#### Explicit constants for the named family

The [named-family theorem][src-constants] proves Equation (2) with $b_k=6$, coefficient $1/400$ and a circuit-size bound. It is built and axiom-audited, but not configured for comparison. The 2 November corpus and the 3 November textual review both judge it stronger than (2), because it fixes explicit constants for the named circuit. Its threshold remains existential: no Lean theorem states $t\ge13669k^2$. The file header’s “Status: unelaborated” describes its original authoring environment, before the recorded build and axiom audit; it is not the current checking status. The [2 November source-bound build receipt](../corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json) includes this exact declaration; its separate axiom-audit and comparison status are recorded in the [round-four formal adjudication](../research/adjudication/round4_formal.md). See [§6.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-floors), [Appendix G.9](#ROOT-EXPONENT-CORRESPONDENCE).

#### The existential form of Equation (2)

The [existential family theorem][src-equation-two] packages Equation (2) existentially. It is built, not compared, and the corpus judges it stronger because it adds a circuit-size witness for the same circuit. The textual review did not cover it. See [§7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-FAMILY-ASSEMBLY).

#### The explicit Forrelation threshold

The threshold $t\ge13669k^2$ in (F51) is the ordinary specialization of (F43) proved in [§8.14](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_threshold). It has no Lean statement and was not covered by the textual review.

#### The uniform Forrelation estimate

The [uniform Forrelation estimate][src-forrelation-uniform] formalizes (F43). It is built but not compared, and has no corpus row. The textual review judges it the same statement: uniform in $k$, with a better power of $k$ and a worse power of the logarithm than Bansal and Sinha. The ordinary proof is in [§8.14](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_uniform_assembly).

#### The quantum bound with logarithmic exponent six

The [quantum upper bound with logarithmic exponent six][src-q-bound] is built but not compared. The corpus judges it stronger than Proposition 3.3 because it gives $C_k2^t(2t)^6$ for the same circuit family. The textual review did not cover it. See [§5.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-explicit-log6).

#### The quantum bound uniform in the parameter

The [quantum upper bound uniform in $k$][src-budget-exponential] is built but not compared and has no corpus row. The textual review judges it the same as (7.5): $Q\le2^{53}k\,2^{10k}\sqrt m\,(2t)^6$ for every $t\ge1$. Its ordinary proof is in [§7.3](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#ROOT-GROWING-K).

#### The bounded tournament theorem

The [bounded tournament theorem][src-quantum-tournament] is built but not compared. The corpus judges it stronger than Proposition 3.2 because it supplies a bounded-list law with explicit cap $6072\,c_{\mathrm{rd}}\sqrt m\,T^2\ln T$. The textual review did not cover it. See [§5.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-tournament-statement).

#### Local certificate tests

The [local certificate theorem][src-construction-full] was compared in its own bundle and passed again on the 3 November sources. Both reviews judge it stronger than Lemma 2.2: it includes both parts, the test equivalence on every input, the exact count $K$, a size bound, adaptive depth $2t+1$, physical cap $2(2t+1)$ and the essential-coordinate diagnostic for pointers. The coherent clause does not promise to restore the workspace. See [§§4.4–4.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-local-tests).

#### Abstract bounded amplification

The [abstract amplification theorem][src-amplification] is built and the corpus judges it exact for Lemma 3.1 in its abstract procedure semantics. That semantics neither compiles to the bit-query model nor identifies a returned subsystem. The textual review did not cover it. See [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-amplification-proof).

#### Amplification returning the successful state

The [retained-state amplification theorem][src-opaque-amplifier] was compared on 3 November and has no corpus row. The textual review judges it stronger than Lemma 3.1 in its uniformity and exact success mass: one selector gate is fixed before every opaque preparation unitary, and the successful state returns tensored with an auxiliary vector. Its success event is narrower, being a predicate on basis labels. The routine reduction from a general projector has not been formalized. See [Appendix G.7](#upper-missing-physical-state).

#### Amplification of measured labels

The [measured-label amplification theorem][src-amplify-measured] is built. The corpus judges it partial for Lemma 3.1, and the textual review judges it weaker: it gives the cap, failure bounds and measured-label law without the state. This is the form used by the proof of Theorem 1.1. See [§5.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-amplification-proof).

#### Direct products with finite averaging

The [finite-average direct-product theorem][src-direct-product-average] is built and the corpus judges it partial for Lemma 4.1: it averages over finite seeds without arbitrary external information. The textual review did not cover it. See [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-direct-product-statement).

#### Direct products on the cap event

The [direct product on the cap event][src-direct-product-caps] was compared on 3 November and has no corpus row. The textual review judges it stronger in allowing initially uncapped trees through the joint event of success and compliance, and narrower in allowing only finitely many weighted seeds. Compliance is a recursive predicate; its agreement with per-input query counts is an ordinary identification in [Appendix G.8](#CL-direct-product-formal). The ordinary cap-event proof is in [§6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-joint-cap).

#### The erased-zero identity and bound

The [complete erased-zero theorem][src-equation-19] was compared and passed again on the 3 November sources. Both reviews judge it stronger than Equation (19): it conjoins identity and bound for every $m=2^\ell$, and the textual review also records that the input law is arbitrary. The alternative complete-expectation wrapper is built only. See [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-erased-zero-identity).

#### The stronger charging estimate

The [deterministic charging inequality][src-zero-successor] behind $2G/(m(m+1))$ is built and has no corpus row. The textual review judges it weaker than the probability bound: averaging the deterministic estimate remains ordinary mathematics. See [§6.4](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-zero-optional).

#### The fixed-time planted-cell event

The [fixed-time joint-event theorem][src-per-time] is built, exact in the corpus and judged the same by the textual review. It states Equation (21) at one time as a joint event under the original law, with $\beta=2/3$ and the minimax hypothesis on $\mu$ as a premise. Prose query time $q$ corresponds to the source's zero-based index $q-1$; [the joint-event definition](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-joint-event) fixes the event before that change of indices. See [§6.5](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-simulator).

#### Winner uniqueness and dominance

The [four winner theorems][cmp-winners] were compared in the Construction bundle. The corpus judges them stronger relative to the unique-winner corollary; the textual review records different statements used beside Lemma 2.2: unique winners, unique gate-consistent transcripts and the two halves of winner dominance. See [§4.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#AC-total-unique), [§4.7](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#AC-comparison).

#### Controls for the query models

The compared [zero costs][cmp-zero-cost], [degree][cmp-degree] controls have no corpus row. The textual review judges them the same as their ordinary counterparts: $D$, $R$ and $Q$ vanish exactly on functions constant on the promise, and degree means the degree of the unique multilinear representation. See [§2.6](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-01-ZERO), [Appendix A.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-A-DEFINITIONS).

#### The universal quartic bound

The [formal universal quartic bound][src-universal-power] is compared through the Separation bundle’s configured universal-bound wrapper. The corpus judges it partial for Theorem A.1: it proves that four belongs to the set in (1), but omits $D$. The textual review did not cover it. See [Appendix A](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#R3-A-RESULT).



A comparison establishes that two statements agree under shared definitions. Whether those definitions model the paper is a separate question, addressed by Appendices G.2–G.3 and the finite controls.


### G.5. Forrelation

<a id="forr_validation_scope"></a>
<!-- passage:forr_validation_scope -->
**Formal implementation of the asymptotic conclusion.** Instantiating the supplied coherent sampler at $q$ repetitions gives $qk$ abstract reads, which its generic compiler implements with at most $2qk$ physical bit queries. The complete Lemma 2.1(ii) wrapper packages this construction with the repetition count $n$ and the law existentially quantified, and its proof chooses $n=q$. The wrapper binds one isometry $F_z$, one initial basis state, one output labeling and the measured law of that isometry, and the physical implementation applies the same $F_z$ before every subsequent continuation, adding at most $2nk$ to the continuation's cap. Coherence, the measured law and the physical cost therefore sit in one witness, which proves the required $O_k(1+\log(1/\eta))$ conclusion. The explicit ceiling choice comes from the repetition and decoder theorems; the wrapper's existential statement alone does not assert it.

The local phase-kickback identity has also been compiled, but it does not yet supply a complete formal program with the sharper $qk$ physical cap, so the sharper displayed inequality rests on the ordinary construction above. Likewise, [the tensor state in §8.2](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#forr_quantum) explains our construction, and the source's retained-isometry theorem asserts no equality with that concrete-register display. The correspondence files record the full theorem types and these distinctions.


The fixed-$k$ statement (F3) with an eventual threshold is the [compared Forrelation lower bound][thm-forrelation], a configured Unconditional target whose type is the [Forrelation hardness statement][def-bansal-sinha] ([Appendix G.4](#checked-statements)). Its solution forwards to the [implementation theorem][src-forr-implementation], which supplies the proof; Comparator compares the configured target, and the implementation receives no separate comparison credit. The uniform estimate (F43) is the [uniform Forrelation estimate][src-forrelation-uniform], which has a recorded build and an axiom audit and is not configured for comparison.

The threshold (F51), the finite-polynomial explanation of differentiation and the comparison (F57)–(F60) are ordinary mathematics with no Lean counterpart. The ordinary proof of (F25) allows arbitrary bounded real leaf labels, whereas the formal interface uses a Boolean-output tree followed by one fixed map from its two output values into $[-1,1]$, which suffices for acceptance probabilities. The estimate (F60) rests on an external Fourier theorem, allows variable error and every power-of-two dimension, and is the type of neither formal endpoint.

The three parts of Lemma 2.1 are packaged together in [one formal statement][src-lemma21], including the retained-isometry physical implementation of part (ii). Its threshold is eventual, and the explicit specialization $13669k^2$ is ordinary. Its generic physical compiler charges $2qk$ queries for $q$ repetitions, whereas the phase construction of §8.2 has the cap $qk$; both give the stated asymptotic bound, and neither the sharper cap nor the explicit threshold appears in the compiled type.
<!-- /passage:forr_validation_scope -->

### G.6. The addressed construction

<a id="AC-evidence"></a>
<!-- passage:AC-evidence -->
The exact source declarations and complete types are recorded in [correspondence.json](../research/returns/round3/members/04_addressed_construction/correspondence.json) and [evidence/lean_audit.json](../research/returns/round3/members/04_addressed_construction/evidence/lean_audit.json). In particular, the [identification of consistent transcripts with true evaluations][src-transcript] gives (4.2), the [uniqueness of the winning pair][src-winner-unique] gives pair uniqueness, and the [description of winning by the local tests][src-winner-tests] gives (4.12) under the premise that $C$ [computes $P$ exactly][def-realises]. The [semantic bridge to the paper's winning condition][src-winner-paper] has no such premise because both sides already refer to the partial function.

The [complete evaluator theorem][src-construction-complete] packages the count, finite size bound, local-test equivalence, adaptive depth, arbitrary-index retained-workspace implementation, and physical query cap for the same circuit witnesses. Its premises $t\geq1$, [exact computation][def-realises] of $P_{k,4^t}$ by $C$, and the circuit-size bound are exactly the supplied circuit properties. The [essential-coordinate theorem for pointers][src-pointer-support] supplies the essential-coordinate witnesses for the support argument. The maintained [full support wrapper][src-construction-full] conjoins those witnesses with every clause of the complete evaluator theorem. For each pointer test, every bit of the pointer word and every possible target coordinate has two full physical inputs differing only at that coordinate on which the test values differ. The witnesses and the evaluator use the same circuit. The printed Lemma 2.2 asserts the test count and adaptive/coherent query bounds; it does not separately assert this essential-coordinate diagnostic. The diagnostic strengthens the printed lemma and is included in the expanded maintained ledger to exclude the erroneous fixed-support interpretation discussed in §4.5. The older complete evaluator is partial relative to that expanded ledger row, not because the printed lemma requires an additional support clause. Its current source-bound execution evidence is recorded separately in the integration receipt. The clean oracle (4.16) and the explicit finite example have the separate ordinary-proof and computational status stated above.

The status of the construction statements is summarized in [Appendix G.4](#checked-statements); the history of their receipts is in [Appendix F](#history-construction).
<!-- /passage:AC-evidence -->

### G.7. The quantum upper bound

The proof of Proposition 3.3 in Theorem 1.1 uses only the law of the measured labels. The stronger statement about the returned state at the end of this subsection is not a premise of it. The [bounded-list tournament theorem][src-quantum-tournament] has the order of quantifiers of Proposition 3.2 in §5.2: its sampler is fixed before the input and before the dominant vertex.

<a id="upper-current-formal-scope"></a>
<!-- passage:upper-current-formal-scope -->

Two formal routes accompany the ordinary proof of §§5.1–5.6, and they have different roles.

**Measured labels and Boolean continuation.** The measured-label amplifier, the tournament continuation and the numerical quantum bound prove the acceptance law of §5.5 and its final budget. This is the route used by the headline proof roots.

**Retained states and bounded lists.** The bounded-list tournament theorem and its tensor-stage wrappers prove Proposition 3.2 as a list law, as written in §5.2. They are built separately and are not used by the headline proof roots.

The measured-label route suffices for Proposition 3.3; the list theorem is a separately built formal counterpart of the list statement in §5.2. The fully qualified names and exact types are indexed in the correspondence; the shorter declaration names below identify their mathematical roles. The formal upper bound follows the same progression as the ordinary proof: amplify a successful outcome, combine trials into a bounded list, decode and verify a candidate, and then bound the integer budget. The state information carried at each step is part of the claim.

**From a successful state to its measured label.** The [abstract amplification theorem][src-amplification] proves the complete assertion of Lemma 3.1 for [abstract procedures][src-proc], including phase-invariant observables, zero wrong-state mass, failure when the success probability is zero, and a uniform call cap. At the physical-program level, the [amplifier of measured labels][src-amplify-measured] supplies the law of the measured label of a [compiled bit-query program][src-runs], which the final bound uses. The [coherent trial loop][src-coherent-amplify] realizes that same label law by a [coherent sampler][src-samples] with retained workspace. Neither of the latter two types identifies a designated physical output subsystem with the original normalized successful state. The abstract theorem and the physical label law therefore support different conclusions; the missing identification is stated precisely below.

**Fresh registers and a bounded list.** The literal tensor construction in equation (15) is supplied by the [formal tensor preparation][src-equation-15]. The [common workspace for finitely many samplers][src-common-workspace] and the [tensor stage built from samplers][src-tensor-stage] realize its stages in a common workspace. The alternative [stage sampler of the tournament][src-stage-sampler] may omit later work after failure: it gives the same successful index law, without equality of the full retained states. Proposition 3.2 only needs the specified list law. The [bounded-list tournament theorem][src-quantum-tournament] supplies an actual finite coherent sampler for the bounded list, its compiled bit-query implementation, a normalized nonnegative law, the dominant-membership estimate and the explicit 6072 query bound. The current theorem therefore supplies the list law as well as its physical query cap.

**Decoding, verification and the final budget.** The formal statements of [decoder correctness][src-decoder], the [comparison state][src-comparison-state], [winner dominance][src-winner-dominates], the [verifier][src-verifier] and the [error of the complete algorithm][src-error-bound] expose the corresponding laws and all-input budgets. Correctness premises for promised Forrelation instances remain explicit; the budget does not disappear on unpromised inputs. For $k=l+1$, $m=4^t$ and $t\ge1$, the [algorithmic form of Proposition 3.3][src-prop33] gives its upper bound for the canonical circuit, the [quantum query bound][src-q-bound] gives its numerical complexity form, and the [explicit quantum budget][src-budget] bounds the actual integer budget by the expression with logarithmic exponent six. These steps use the measured laws already available, so the remaining full-state specification is not an extra assumption of the final upper bound.

The supplied dependency export for the [unconditional Theorem 1.1][src-theorem] and the [unconditional failure of the cubic bound][src-cubic] reaches the older measured/Boolean upper-bound route, including the [amplifier of measured labels][src-amplify-measured] and the [quantum query bound][src-q-bound]. It does not reach the new list and tensor wrappers. This is a fact about those specified proof roots; it does not negate the wrappers' compilation or their mathematical statements. Exact-name Comparator coverage is narrower again: in particular, the Tournament bundle compares two drift wrappers, not the new list theorem. The companion files record declaration membership, complete available types and these evidence dimensions separately. Historical “UNELABORATED” comments in integrated source files do not override newer source-bound passing receipts.
<!-- /passage:upper-current-formal-scope -->

**Correspondence note.** The compiled version rests on a finite-label statement. Let $q_x(b)$ be the unamplified probability of a successful label $b$, and put $q_x=\sum_bq_x(b)$. Then there is a failure probability $f_x\in[0,1]$ such that the output law has the following form:

$$
\begin{aligned}
\Pr[\bot]&=f_x,\\
\Pr[b]&=(1-f_x)\frac{q_x(b)}{q_x} &&(q_x>0),\\
q_x\geq\gamma&\Longrightarrow f_x\leq\eta,\\
q_x=0&\Longrightarrow f_x=1.
\end{aligned}
$$

For the ordinary procedure just proved, this law follows by measuring the successful state. The formal headline proof obtains the required law from its separate measured/reset implementation, the [amplifier of measured labels][src-amplify-measured]; this is a correspondence of output laws, not an identification of returned states or a claim about formal dependency ([Appendix G.7](#upper-current-formal-scope)). For $q_x>0$ and $f_x<1$, which are the hypotheses under which the ratio is a conditional probability, the successful mass is $1-f_x>0$, and dividing by it gives the conditional law $q_x(b)/q_x$. For the bounded procedure above, $p>0$ implies $f_x<1$, and in the tournament the stronger bound $f_x\leq\varepsilon<1$ holds at every history before the dominant vertex has been selected. At $q_x=0$ the only output is failure, and that event receives no conditional law. Substituting $q_x(i)=w_i/m$ gives the ideal pivot law wherever it is used.

<a id="upper-missing-physical-state"></a>
<!-- passage:upper-missing-physical-state -->
The remaining formal target for the complete physical reading of Lemma 3.1 can be stated without ambiguity. Fix a finite original Hilbert space $H$ with its computational basis, a basis state $h_0$, a fixed success projector $\Pi$ on $H$, and a concrete oracle-dependent unitary circuit $A_x$ with at most $q$ logical reads. Put $p_x=\|\Pi A_x|h_0\rangle\|^2$ and, only when $p_x>0$, put $g_x=\Pi A_x|h_0\rangle/\sqrt{p_x}$.

<!-- claim:r3-q-physical-state-bridge -->
For fixed $0<\gamma\leq1/2$ and $0<\eta<1/2$, the desired theorem must construct a finite-dimensional auxiliary Hilbert space $J$, with a specified finite computational basis and fixed initial state $j_0$, a final success predicate on $J$, and a coherent unitary $B_x$ on $H\otimes J$. The construction includes a specified input-independent routing that places the complete first successful original register in the designated $H$ slot. Write $\Pi_{\rm out}=I_H\otimes\Pi_J$ for the final auxiliary-flag success projection and
$$
 \Psi_x=B_x(|h_0\rangle\otimes|j_0\rangle),
 \qquad s_x=\|\Pi_{\rm out}\Psi_x\|^2.
$$
The required statement is
$$
 \begin{aligned}
 &0\leq s_x\leq1,\qquad
   p_x\geq\gamma\Longrightarrow s_x\geq1-\eta,\qquad
   p_x=0\Longrightarrow\Pi_{\rm out}\Psi_x=0,\\
 &p_x>0\Longrightarrow s_x\geq p_x/2>0,\\
 &p_x>0\Longrightarrow
   \exists\,\xi_x\in J:\quad
       \Pi_{\rm out}\Psi_x=g_x\otimes\xi_x
       \quad\hbox{and}\quad\|\xi_x\|^2=s_x.
 \end{aligned}
$$
Here $M=\lceil10/\sqrt\gamma\rceil$ and $N=\lceil\ln(1/\eta)/\ln(40/31)\rceil$ are the input-independent counts in [the bounded trial schedule](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#upper-grover-trial). It must give a logical-read circuit cap $qN(2M+1)$ and transport this same circuit through the physical compiler with cap at most $2qN(2M+1)$ ordinary bit queries, on arbitrary embedded input states and continuations. This arbitrary-state clause concerns correctness of the compiler; the amplification guarantee concerns the specified initial state. All these bounds hold on every input, whether or not $p_x\geq\gamma$.

To express the preprint's black-box uniformity, the underlying program with slots for $A$ and $A^{-1}$ must be fixed by $\gamma,\eta$ and the register/query interface before the preparation oracle is supplied. Its branches, $M,N$ and cap cannot depend on $p_x$. The auxiliary space, routing and all non-oracle gates are input-independent. An equivalent adaptive formulation gives the same normalized original-register state, up to phase, on every positive-mass successful history. The finite-coordinate version and an explicitly uncompiled proposed interface are in the [quantum gap record](../research/returns/round3/members/05_quantum_upper/LEAN_GAPS.md).

The ordinary fresh-trial/routing argument in §5.6 supplies the mathematical construction. The round-four integration added the [amplifier for opaque preparations][cmp-amplifier], accepted by Comparator: for one selector gate chosen before every opaque unitary, it states the retained-factor identity and the exact success mass, with the zero-mass, $p/2$ and $1-\eta$ clauses and a logical cap. The basis change from a general fixed projector to a coordinate predicate and the literal flag/Hadamard identification remain unproved, so no source-bound Lean theorem of the full physical type displayed above is claimed. In particular, the coherent composition can retain a copy of a successful output label in auxiliary registers, and the measured compilation route reads a complete basis label. What remains is the physical transport and uncomputation statement: after the chosen compiler and any copied labels, the designated physical output subsystem must still have the abstract successful factor $g_x$. The accepted opaque identity alone does not identify that subsystem. This bridge is needed before promoting the physical wrapper to the full state claim. This missing formal bridge is not an extra assumption in the proof of Proposition 3.3: that proof uses only measured labels, whose law is already supplied by the compiled route.
<!-- /passage:upper-missing-physical-state -->

### G.8. The classical lower bound

<a id="CL-direct-product-formal"></a>
<!-- passage:CL-direct-product-formal -->
The [weighted direct-product development][src-direct-product-module] proves (6.10) by
unnormalized induction and exports the [weighted direct product][src-direct-product] and its
finite-mixture versions. The additional
[conditional-value development][src-conditional-value-module] proves the transcript product
law, the conditional-value inequality, finite product iteration, and the
bound on actual terminal success, ending in the
[capped direct product by conditional values][src-direct-product-capped] and its
[average over finite seeds][src-direct-product-average]. It expresses finite
conditional expectations directly, without Mathlib's supermartingales. It reuses the one-input optimization lemmas, and does not invoke
the older multi-input direct-product theorem to prove its endpoint.

The round-four integration added the
[direct product on the cap event][cmp-direct-product] as an endpoint, accepted by
Comparator. It covers a finite seed space with arbitrary nonnegative weights
summing to one, each seed selecting an initially uncapped tree, and bounds the
weighted joint event that every instance is answered correctly and no
instance exceeds its cap of $L$ queries by $\beta^r$. [Compliance with the caps][src-complies] is
a recursive predicate, which follows the path taken on the
given input and decrements the cap of each queried instance. The observable
[query count][src-count], the number of queries that path makes to each instance,
is defined separately, and the equivalence of the two descriptions is not a
Lean theorem.

**Ordinary cap-count identification.** At a leaf, every observable count is zero and recursive compliance holds. At a query to instance $h$, compliance requires $c_h>0$ and applies the same condition to the chosen subtree with $c_h$ lowered by one. The path count for $h$ is one plus its subtree count; other counts are unchanged. Induction therefore identifies recursive compliance with the condition that each instance is queried at most its cap. This is an ordinary proof, not a new formal declaration.

Arbitrary measurable
external randomness is handled by the ordinary [finite-behavior reduction in §6.1](https://github.com/wcook04/quartic-query-lean/blob/071ce02338cd0e4f43185ef41c8c4a555dc460f7/docs/reasoning_record.md#CL-independent-information),
not by a Lean theorem. The arbitrary-information reduction, the generic
joint-event truncation corollary and the combined identity (6.11) are ordinary
deductions supplied here. The worked example is a separate exact finite
calculation.
<!-- /passage:CL-direct-product-formal -->

<a id="CL-formal-scope"></a>
<!-- passage:CL-formal-scope -->

In the Lean development an older core theorem proves the one-sided planted discrepancy inequality, and the supplied Paper wrapper states the stronger absolute-value endpoint, which follows from the coupling argument and the stronger search estimate. These formal endpoints do not identify the alternative proof with the paper's early/late derivation.

The retained [planted correspondence](../research/returns/round3/members/07_planted_lower_bound/correspondence.json) records the packet's complete source signatures, compiler-reported types, hypotheses and historical receipts. The [integrated correspondence](reasoning_record_correspondence.json) adds the maintained conjunction wrappers and keeps each evidence observation bound to its own source.

**The whole equation (19).** There are two complete conjunctions, ordinarily equivalent by substituting their common equality:
\[
 \begin{aligned}
 &\left(\Pr[\mathrm{hit}]=\frac{\mathbb E Z}{m}\right)
 \ \wedge\
 \left(\Pr[\mathrm{hit}]\le\frac{4G}{m^2}\right),\\
 &\left(\Pr[\mathrm{hit}]=\frac{\mathbb E Z}{m}\right)
 \ \wedge\
 \left(\frac{\mathbb E Z}{m}\le\frac{4G}{m^2}\right).
 \end{aligned}
\]
Both use one nonnegative normalized law $\mu$, one deterministic query tree $T$ and $\operatorname{depth}(T)\le G$. Their formal column size is $2^\ell$, with $\ell=2t$ giving $m=4^t$; no promise-support or hardness premise is required.

The [whole erased-zero theorem][src-equation-19] gives the first conjunction; the [identity with the bound on the divided expectation][src-equation-19-expectation] gives the second. The [identity alone][src-erased-zero-identity] is algebraically valid for arbitrary finite real weights, while interpreting it as a probability needs normalization and nonnegativity. The older [erased-zero bound][src-erased-zero-bound] supplies only the hit-probability upper bound. Exact execution evidence belongs to each named declaration and is reported in the dated integration receipt. The unchanged returned proposal remains historical provenance; its earlier uncompiled status does not describe a later maintained declaration.

**An independently written product experiment.** The [independent specification](../lean/QuarticCorpus/Independent/Eq19/Spec.lean) shares the project's coordinate, query-tree, path and depth interfaces. Within that boundary it independently defines the reference input coordinate by coordinate, the event that a column's zero lies on the query path, and the number of distinct discovered columns. It writes the law as explicit products: all address strings have independent mass $\mu$, every zero position is independently uniform, and the selected column has a further independent factor $1/m$. Its expectations do not use the maintained definitions of the [dummy input][src-dummy], the [event that the dummy run finds a zero][src-found-zero], the [joint average over addresses, zeros and planted column][src-coupled-average], the [number of discovered zeros][src-discovered-zeros] or its [expectation][src-expected-zeros]. The [bridge](../lean/QuarticCorpus/Independent/Eq19/Bridge.lean) identifies each of those objects before transporting the complete conjunction. Separate finite path controls test that declared shared-interface boundary. The direct actual-vocabulary comparison and this explicit-product comparison therefore check different things. Neither identifies the alternative search proof with the paper's early/late argument.

**The expectation estimate and its route.** The [theorem on the position of an unseen zero][src-uniform-zero] states its posterior given a transcript of positive probability. The [bound on the expected number of discovered zeros][src-expected-zeros-bound] obtains the endpoint through the stronger zero-search induction. Thus even a complete conjunction theorem for (19) does not formalize the early/late proof of $\mathbb E Z$ in §6.4. The distinction concerns the proof route and the compound expectation row, not the truth of the displayed endpoint.

**The simulator and the eventual lower bound.** The Paper wrappers state the absolute form of (18), the individual-time joint event (21), the cell bound (22), and the absolute discrepancy (23). The core one-sided discrepancy theorem remains a separate sufficient endpoint. Prose query time $q$ corresponds to the source's zero-based index $q-1$. The exact logarithmic tail bound, its envelope limit and the elementary finite power estimate have separate statements. Finally, the [two formal forms of Proposition 4.2][src-prop42], for every circuit computing $P$ and for the canonical circuit, supply the eventual fixed-$k$ hardness premise using the Forrelation theorem. The [core planted lower bound][src-planted-core] keeps that premise in its own type. A proof of an unconditional wrapper does not erase the binder of a conditional supplier.

The $m+1$ refinement, elementary convex-separation proof, arbitrary-coin finite-behaviour reduction and finite examples are ordinary arguments or computations at their stated scope. They do not acquire formal status from a nearby endpoint theorem. A matching build, an axiom audit, a Comparator result, review of the intended statement and human review are different kinds of evidence.

<!-- /passage:CL-formal-scope -->

### G.9. The exponent and Appendix A

The bound (7.5) of §7.3 is the [quantum upper bound uniform in $k$][src-budget-exponential], which is built and not configured for comparison; the rest of §7.3 is ordinary mathematics.

<a id="ROOT-EXPONENT-CORRESPONDENCE"></a>
<!-- passage:ROOT-EXPONENT-CORRESPONDENCE -->
The source preprint supplies the attribution for this exponent argument; the supplied Lean sources and frozen execution records support the formal claims separately. The [named-family theorem][src-constants] proves (7.1) for the [canonical Forrelation circuit][src-forr-circuit] with \(k\) strings at size \(m=4^t\), with constant \(1/400\), logarithmic exponent six, the [quantum constant][src-budget-constant] \(C_k\), and the circuit-size bound in the same conclusion. The [existential family theorem][src-equation-two] packages these facts existentially. Neither statement has an unproved Forrelation binder.

The [finite quotient calculation][src-ratio-arithmetic] proves the finite quotient inequality. The [exponent ratio for abstract sequences][src-ratio-abstract] adds divergence of the explicit lower envelope and the quotient for abstract sequences satisfying the fixed-parameter bounds. The [exponent ratio for the named family][src-ratio-family] specializes all three conclusions to the named total-function family with \(b_k=6\). Thus the literal quotient and limit now have formal support; the older [comparison of powers][src-eventual-comparison] supplies only the sufficient eventual strict comparison. The elementary integral argument above explains the same limit by a different proof.

Three declarations implement the [choice of \(k\)][src-exponent-choice], the [exclusion of smaller exponents][src-no-smaller-exponent] and the [infimum argument][src-alpha-infimum]. Their intermediate binders for family bounds and reindexing are discharged by the model and construction theorems. The final [exponent theorem][src-alpha], [Theorem 1.1][src-theorem] and [failure of the cubic bound][src-cubic] have no mathematical assumption left open.

The compared forms of these final statements, and the status of the named-family constants theorem, are listed in [Appendix G.4](#checked-statements).
<!-- /passage:ROOT-EXPONENT-CORRESPONDENCE -->

<a id="R3-A-ROUTES"></a>
<!-- passage:R3-A-ROUTES -->
Three separate formal bounds are present in the supplied source. Their constants come from the indicated ingredients:

| Formal route | Block sensitivity | Spectral sensitivity | Quartic coefficient |
| --- | --- | --- | ---: |
| Existing complexitylib route | \(\operatorname{bs}\le16Q^2\), polynomial method | \(\lambda\le36Q\), specialized progress | \(16\cdot36^2=20736\) |
| Literal Appendix A assembly | \(\operatorname{bs}\le35^2Q^2\), star adversary | \(\lambda\le35Q\), general adversary | \(35^4=1500625\) |
| Separate hybrid | \(\operatorname{bs}\le16Q^2\), polynomial method | \(\lambda\le35Q\), general adversary | \(16\cdot35^2=19600\) |

The second route proves the intermediate general-matrix, star, actual-face and recursive-matrix statements used in this appendix. Its larger numerical constant reflects the star estimate for block sensitivity. The hybrid keeps the stronger polynomial-method estimate and is exported separately. The first route is the one used by the recorded headline proof; the other two are separately compiled alternatives. The constants distinguish implementations of known inequalities; none establishes a sharp universal constant. The coefficients in the first and third rows are read from the pinned complexitylib proof and its project wrappers; the reconstruction of (A.1) uses the fully explained second row.
<!-- /passage:R3-A-ROUTES -->

<a id="R3-A-FORMAL"></a>
<!-- passage:R3-A-FORMAL -->

The formal multiplicity proof uses a local variation: multiplying coordinates by their parity signs anticommutes with \(H'_d\), so it sends each positive-root eigenvector to a negative-root eigenvector and conversely. The square and trace identities are separately checked. The resulting eigenvector and extension argument agree with (A.8)–(A.10).

The general bound is the [formal spectral-adversary lemma][src-lemma-a2]; its Perron and progress assumptions are proved by its dependencies and are not extra open hypotheses. The [star and sensitivity estimates][src-lemma-a3], the [spectral degree theorem on an actual face][src-lemma-a4] and the [bridge to Midrijānis's bound][src-lemma-a5] are separate formal statements. The quartic statements at a [quantum query cap][src-quartic-cap] and at the [attained quantum minimum][src-quartic-minimum] are stated separately, and [Theorem A.1 in its displayed form][src-theorem-a1] also includes \(R\le D\). The [older quartic bound][src-quartic-older] proves coefficient 20736, while the [hybrid quartic bound][src-quartic-hybrid] proves 19600.

Some corpus rows deliberately combine several assertions. For example, the matrix spectrum row includes square, trace, symmetry, eigenvalue classification and multiplicities; these are supplied by several declarations, rather than by the multiplicity theorem alone. Likewise the per-query row and the final-overlap row each have separate supporting estimates. Their correspondence remains partial at a single primary declaration even though the named additional declarations have compilation evidence for the reviewed snapshot. The polynomial-definition prose includes an ordinary uniqueness proof beyond the one Fourier-degree bridge. The exact parity witness above is an ordinary mathematical and finite-computational check, with no supplied Lean theorem for its exact one-query algorithm. Comparator acceptance of the existing separation wrapper does not constitute a separate comparison of each new Appendix declaration.
<!-- /passage:R3-A-FORMAL -->


## Appendix C. References and inspected editions

This appendix gives the exact edition and locator of every cited source.

<a id="historical-ROOT-REFERENCES"></a>
<!-- passage:historical-ROOT-REFERENCES -->
The editions and theorem locators below are those assessed in the retained section returns. In-text citations distinguish a theorem used as a premise, an antecedent, a comparison and a disputed displayed step. The notes retain the scope of those readings; a listed source is not thereby claimed to have been read in full for this revision. Machine-readable records are in [reasoning_record.bib](reasoning_record.bib).

<a id="historical-ref-OpenAI2026"></a>

- **OpenAI2026.** OpenAI. *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. 2026. [Full-text edition](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). Preprint dated 5 October 2026. Mathematical target throughout this record. The retained reviewed PDF has SHA-256 a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e.

<a id="historical-ref-BDW02"></a>

- **BDW02.** Harry Buhrman and Ronald de Wolf. *Complexity Measures and Decision Tree Complexity: A Survey*. 2002. Theoretical Computer Science. 21–43. [Full-text edition](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf). Author PDF dated 10 October 2002; supplied PDF SHA-256 7002019660c498b652611acf5cdbe264ea9c4a139f8f4da6e82e12822e5d9122. Sections 3.1–3.3, printed pages 5–8, supply the model conventions. Section 3.2 explicitly allows biased coins, takes maximum supported depth, and uses inclusive success at least 2/3. Section 3.3 uses a fixed sequence of input-independent gates and bit queries. Standard exposition, not a proof of the new separation.

<a id="historical-ref-DW26"></a>

- **DW26.** Ronald de Wolf. *Quantum Computing: Lecture Notes*. 2026. [Version record](https://arxiv.org/abs/1907.09415v6). Version 6, 27 August 2026. Supplied source archive SHA-256 2ffd080924542b6de1409a1dbd73efcb85e99bc0d3cc2daac5e3eeba84ef2535. Measurement: Section 1.2.2, printed pages 4–6, and Section 2.1.2, pages 14–15. Oracle and phase query: Section 2.4, printed pages 17–18, especially printed footnote 7; Chapter 2, Exercise 10 distinguishes controlled and uncontrolled phase queries. Section 2.3 is Quantum parallelism; the earlier Section 2.3/footnote 17 locator is corrected. Official author PDF independently consulted at https://homepages.cwi.nl/~rdewolf/qcnotes.pdf.

<a id="historical-ref-BBCMW98"></a>

- **BBCMW98.** Robert Beals and Harry Buhrman and Richard Cleve and Michele Mosca and Ronald de Wolf. *Quantum Lower Bounds by Polynomials*. 1998. [Version record](https://arxiv.org/abs/quant-ph/9802049v3). Conference/arXiv-era version, separately identified from the journal manuscript. The supplied PDF has SHA-256 afec116657493976b70df7dcb8b174c8c0be55a9337d9e035afd5f1fc4d9cd4c. Section 3.2, PDF page 4, defines classical randomized cost using expected queries on a worst-case input; the paragraph following Proposition 6.4, PDF page 9, uses that convention for parity. The arXiv v3 metadata dates it 30 September 1998; no byte identity with a newly downloaded arXiv PDF is asserted. Author-hosted conference PDF also consulted: https://homepages.cwi.nl/~rdewolf/publ/qc/focs98.pdf.

<a id="historical-ref-BBCMW01"></a>

- **BBCMW01.** Robert Beals and Harry Buhrman and Richard Cleve and Michele Mosca and Ronald de Wolf. *Quantum Lower Bounds by Polynomials*. 2001. Journal of the ACM. 778–797. [Full-text edition](https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf). Added external comparison, accessed 2 November 2026. Author-hosted journal manuscript, Section 3.2 printed page 7, uses worst-case randomized query cost; Proposition 6.4 and adjoining paragraph, printed page 17, give quantum parity cost ceil(N/2) and classical bounded-error cost N. The assessment is confined to these passages and version identity. This journal edition uses worst-case query cost, whereas the older conference version uses expected cost.

<a id="historical-ref-ABKRT2020"></a>

- **ABKRT2020.** Aaronson, Scott and Ben-David, Shalev and Kothari, Robin and Rao, Shravas and Tal, Avishay. *Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem*. 2020. [Version record](https://arxiv.org/abs/2010.12629v1). Version 1, 23 October 2020. Theorem 1: pp. 1 and 6–7; Theorem 2 and its deduction: p. 2; Definition 7: p. 6; Lemma 9: p. 8; Conjecture 2: p. 20. Locators refer to the original PDF, not flattened extraction numbering.

<a id="historical-ref-AA18"></a>

- **AA18.** Scott Aaronson and Andris Ambainis. *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing*. 2018. SIAM Journal on Computing. 982–1038. [Version record](https://arxiv.org/abs/1411.5729v1). Mathematical locators refer to the inspected arXiv v1, 21 November 2014, not journal pagination: Section 1.1.3, p. 4; Section 3.2, Figure 1 and Proposition 6, pp. 13–14. Projection probability Phi squared and the separate interference probability (1+Phi)/2 must be distinguished. Journal metadata is supplied for attribution.

<a id="historical-ref-BansalSinha2021"></a>

- **BansalSinha2021.** Nikhil Bansal and Makrand Sinha. *$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity*. 2021. Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing. 1303–1316. [Version record](https://arxiv.org/abs/2008.07003v3). Full-version mathematical locators refer to arXiv v3, 17 November 2020: Theorem 1.3 and Corollary 1.4, p. 4; Theorems 3.1–3.4, pp. 16–17; Corollary 3.5, p. 18; Lemma 4.3, p. 19; Section 5.4, p. 38. In supplied v3 main.tex, the disputed comparison is physical line 1181; line 1184 is the later threshold.

<a id="historical-ref-GirishTalWu2021"></a>

- **GirishTalWu2021.** Uma Girish and Avishay Tal and Kewen Wu. *Fourier Growth of Parity Decision Trees*. 2021. 36th Computational Complexity Conference (CCC 2021). 39:1–39:36. [Version record](https://arxiv.org/abs/2103.11604v2). Mathematical locators use arXiv v2, 13 May 2021: Section 1.3, pp. 6–8, and Lemma 1.9, p. 8. In the CCC 2021 version the corresponding result is Lemma 9, p. 39:8.

<a id="historical-ref-SherstovStorozhenkoWu2023"></a>

- **SherstovStorozhenkoWu2023.** Alexander A. Sherstov and Andrey A. Storozhenko and Pei Wu. *An Optimal Separation of Randomized and Quantum Query Complexity*. 2023. SIAM Journal on Computing. 525–567. [Version record](https://arxiv.org/abs/2008.10223v4). Locators refer to arXiv v4, 29 January 2023: PDF Corollaries 4.14–4.15, p. 35; the real-valued proof continues p. 36. The HTML conversion calls these Corollaries 4.12–4.13. The absolute Fourier constant is unspecified.

<a id="historical-ref-Tal2019v1"></a>

- **Tal2019v1.** Avishay Tal. *Towards Optimal Separations between Quantum and Randomized Query Complexities*. 2019. [Version record](https://arxiv.org/abs/1912.12561v1). Version 1, 29 December 2019; published at FOCS 2020. Context only: Theorem 5.1 and Corollary 5.3, p. 13; Definition 5.5 and Lemma 5.7, p. 14.

<a id="historical-ref-ABK2019"></a>

- **ABK2019.** Aaronson, Scott and Ben-David, Shalev and Kothari, Robin. *Separations in Query Complexity Using Cheat Sheets*. 2016. Proceedings of the 48th Annual ACM Symposium on Theory of Computing. 863–876. [Full-text edition](https://arxiv.org/pdf/1511.01937v2). Edition inspected: arXiv v2, 9 July 2019. Printed Section 6.1, Definitions 14–15, pp. 20–21; Section 6.2, Lemma 17, p. 22. These appear as Definitions 10–11 and Lemma 13 in the supplied environment-numbered Markdown extraction. Historical antecedent and algorithmic comparison; no theorem transfer to this multi-column construction.

<a id="historical-ref-ABBLSS2015"></a>

- **ABBLSS2015.** Ambainis, Andris and Balodis, Kaspars and Belovs, Aleksandrs and Lee, Troy and Santha, Miklos and Smotrovs, Juris. *Separations in Query Complexity Based on Pointer Functions*. 2015. [Full-text edition](https://arxiv.org/pdf/1506.04719v3). Edition inspected: arXiv v3, 26 October 2015. Section 1.3, pp. 5–6; final paragraph of Use of a balanced tree, p. 6, discusses direct pointers and immediately gives the exponential-alphabet qualification. Historical comparison, not an imported bit-query theorem.

<a id="historical-ref-BHMT2000"></a>

- **BHMT2000.** Brassard, Gilles and Høyer, Peter and Mosca, Michele and Tapp, Alain. *Quantum Amplitude Amplification and Estimation*. 2000. [Version record](https://arxiv.org/abs/quant-ph/0005055v1). Inspected arXiv v1. Section 2, Lemma 1, printed pages 5–6, and equation (8), page 7: amplification geometry and successful component. Theorem 3, pages 8–9: expected-time unknown-success search, not the all-branch cap. Theorem 12, page 19, is amplitude estimation. Published version: Contemporary Mathematics 305 (2002), pages 53–74; locators in this record refer to v1.

<a id="historical-ref-BBHT1996"></a>

- **BBHT1996.** Boyer, Michel and Brassard, Gilles and Høyer, Peter and Tapp, Alain. *Tight Bounds on Quantum Searching*. 1996. [Version record](https://arxiv.org/abs/quant-ph/9605034v1). Inspected arXiv v1. Section 4, Lemma 2, printed page 3: exact average for a random number of Grover iterations. Theorem 3 and subsequent timeout discussion, page 4: unknown-number expected-time search. The fixed capped construction is proved separately in §5.6. Journal version: Fortschritte der Physik 46 (1998); its pagination is not used for these locators.

<a id="historical-ref-DH1999"></a>

- **DH1999.** Dürr, Christoph and Høyer, Peter. *A Quantum Algorithm for Finding the Minimum*. 1999. [Version record](https://arxiv.org/abs/quant-ph/9607014v2). Inspected revised arXiv v2; original preprint July 1996. Theorem 1 and Lemmas 1–2, pages 1–2. Historical comparison only: ordered values and rank improvement do not supply a proof for arbitrary probabilistic comparisons.

<a id="historical-ref-HMW2003"></a>

- **HMW2003.** Høyer, Peter and Mosca, Michele and de Wolf, Ronald. *Quantum Search on Bounded-Error Inputs*. 2003. [Version record](https://arxiv.org/abs/quant-ph/0304052v2). Inspected arXiv v2. Section 1, pages 1–3: uniform bounded-error access to fixed Boolean predicates. Section 3, pages 4–7: search construction. Section 4: AND–OR applications. Section 5, pages 8–9: imperfect-verifier generalization. Hypothesis comparison only; arbitrary loser comparisons need not satisfy the fixed-predicate correctness guarantee. Published in ICALP 2003, LNCS 2719, pages 291–299; locators here use v2.

<a id="historical-ref-AIK2026"></a>

- **AIK2026.** Ambainis, Andris and Iraids, Jānis and Kokainis, Mārtiņš. *Near-Optimal Separations of Certificate Complexity from Randomized and Quantum Query Complexity*. 2026. [Version record](https://arxiv.org/abs/2609.11664v2). arXiv v2. Recent comparison-based separation of certificate complexity identified by the preprint's §1.1; cited as an antecedent for comparison and certificate checking, with no theorem imported as a premise.

<a id="historical-ref-BDK2026"></a>

- **BDK2026.** Ben-David, Shalev and Kothari, Robin. *Randomized Query Complexity Can Beat Certificate Complexity*. 2026. [Version record](https://arxiv.org/abs/2609.15063v1). Inspected arXiv v1, Section 3, Lemma 5, pages 3–5. Antecedent for candidate generation, tournament comparison and certificate checking; no theorem from this source is imported as a premise of the fractional-weight proof.

<a id="historical-ref-MPS2023"></a>

- **MPS2023.** Mande, Nikhil S. and Paraashar, Manaswi and Saurabh, Nitin. *Randomized and Quantum Query Complexities of Finding a King in a Tournament*. 2023. 43rd IARCS Annual Conference on Foundations of Software Technology and Theoretical Computer Science (FSTTCS 2023). 30:1–30:19. [Published edition](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30). Inspected published edition. Theorem 19, Section 4, pages 30:11–30:13, including the nearby proof and Algorithm 4. Exact direction queries to a fixed tournament; contextual comparison only. The baseline's Theorem 4.4 locator does not match this edition.

<a id="historical-ref-Drucker2012"></a>

- **Drucker2012.** Drucker, Andrew. *Improved Direct Product Theorems for Randomized Query Complexity*. 2012. Computational Complexity. 197–244. [Version record](https://arxiv.org/abs/1005.0644v2). Assessed arXiv version 2, 9 May 2014, and supplied pinned TeX. All locators use arXiv printed pagination: Section 1.3, pp. 6–7; Lemmas 3.1–3.2, pp. 11–12; fair specialization at the end of Section 3, p. 13. Relevant passages of the earlier supplied PDF agree; complete edition identity was not established

<a id="historical-ref-Shaltiel2001"></a>

- **Shaltiel2001.** Shaltiel, Ronen. *Towards Proving Strong Direct Product Theorems*. 2001. [Report page](https://eccc.weizmann.ac.il/report/2001/009/). Assessed ECCC report: Section 1.1, p. 1, definitions of success/advantage and footnotes 1–2; Section 5, Definition 4 and Theorem 5, printed p. 11, and Lemma 7, p. 12. These are PDF pages 12–13. Later journal publication: Computational Complexity 12(1–2):1–22 (2003); journal-edition theorem numbering not assessed

<a id="historical-ref-Huang2019"></a>

- **Huang2019.** Huang, Hao. *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*. 2019. Annals of Mathematics. 949–955. [Full-text edition](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf). Published edition inspected at Lemma 2.2, p. 952, and the proof and spectral remark for Theorem 1.1, p. 953. The supplied six-page source is instead arXiv:1907.00847v2; its corresponding locators are pp. 4–5.

<a id="historical-ref-Midrijanis2004"></a>

- **Midrijanis2004.** Midrijānis, Gatis. *Exact quantum query complexity for total Boolean functions*. 2004. [Version record](https://arxiv.org/abs/quant-ph/0403168v2). Version 2, 27 March 2004. Lemma 3, p. 3; proof of Theorem 4, pp. 3–4, especially its final paragraph for D(f) <= deg(f) bs(f). Theorem 5 concerns exact, not bounded-error, quantum query complexity.

<a id="historical-ref-HLS2007"></a>

- **HLS2007.** Høyer, Peter and Lee, Troy and Špalek, Robert. *Negative weights make adversaries stronger*. 2007. [Full-text edition](https://www.ucw.cz/~robert/papers/madv.pdf). The inspected 29-page author PDF: Definition 1 and Theorem 1, printed p. 3. Version-2 metadata is dated 24 April 2007; byte identity of the author PDF and arXiv PDF was not established. Theorem 1 attributes the nonnegative spectral bound, including denominator two, to Barnum–Saks–Szegedy. Related conference publication: STOC 2007, pp. 526–535, DOI 10.1145/1250790.1250867.

<a id="historical-ref-SS2006"></a>

- **SS2006.** Špalek, Robert and Szegedy, Mario. *All Quantum Adversary Methods are Equivalent*. 2006. Theory of Computing. 1–18. [Full-text edition](https://theoryofcomputing.org/articles/v002a001/v002a001.pdf). Publisher edition. Oracle convention: Section 2.1, p. 4; operator norm: Section 2.4, p. 5; Theorem 3.1 and equation (3.1): p. 6; closing proof: p. 14. The printed error prefactor lacks a factor 1/2 under those conventions; the exact two-bit parity witness checks this local discrepancy without disputing the nonnegative-adversary equivalences.

<a id="historical-ref-BSS2003"></a>

- **BSS2003.** Barnum, Howard and Saks, Michael and Szegedy, Mario. *Quantum query complexity and semi-definite programming*. 2003. Proceedings of the 18th IEEE Annual Conference on Computational Complexity. 179–193. [Publication metadata](https://doi.org/10.1109/CCC.2003.1214419). The proceedings title and DOI are confirmed by the [Rutgers institutional record](https://www.researchwithrutgers.org/en/publications/quantum-query-complexity-and-semi-definite-programming/). The attribution of the adversary theorem follows Høyer–Lee–Špalek Theorem 1 and Špalek–Szegedy reference 7. Original full text was not supplied or independently inspected in this review.

<a id="historical-ref-ComplexitylibPinned"></a>

- **ComplexitylibPinned.** complexitylib contributors. *complexitylib: pinned Lean source dependency*. [Full-text edition](https://github.com/cslib-community/complexitylib/tree/62ca5c21461b2482e8bd12b7cb9b4937d887a33a). Revision read from the supplied lake-manifest.json and DEPENDENCY_SOURCES.json. Exact proof-source and run evidence are recorded separately in correspondence.json; a source citation alone does not assert successful compilation. No repository commit date or individual author list is inferred.

<a id="historical-ref-GPW2018"></a>

- **GPW2018.** Mika Göös, Toniann Pitassi and Thomas Watson. *Deterministic communication vs. Partition number*. SIAM Journal on Computing (2018), DOI [10.1137/16M1059369](https://doi.org/10.1137/16M1059369). The retained baseline assessment uses [ECCC TR15-050](https://eccc.weizmann.ac.il/report/2015/050/), revision text dated 5 September 2017, Theorem 5 and §2.1, pp. 3–5. Historical construction antecedent; this integration does not claim a fresh full reading.

<!-- /passage:historical-ROOT-REFERENCES -->

[OpenAI2026]: https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf
[BDW02]: https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf
[DW26]: https://arxiv.org/abs/1907.09415v6
[BBCMW98]: https://arxiv.org/abs/quant-ph/9802049v3
[BBCMW01]: https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf
[ABKRT2020]: https://arxiv.org/abs/2010.12629v1
[AA18]: https://arxiv.org/abs/1411.5729v1
[BansalSinha2021]: https://arxiv.org/abs/2008.07003v3
[GirishTalWu2021]: https://arxiv.org/abs/2103.11604v2
[SherstovStorozhenkoWu2023]: https://arxiv.org/abs/2008.10223v4
[Tal2019v1]: https://arxiv.org/abs/1912.12561v1
[ABK2019]: https://arxiv.org/pdf/1511.01937v2
[ABBLSS2015]: https://arxiv.org/pdf/1506.04719v3
[BHMT2000]: https://arxiv.org/abs/quant-ph/0005055v1
[BBHT1996]: https://arxiv.org/abs/quant-ph/9605034v1
[DH1999]: https://arxiv.org/abs/quant-ph/9607014v2
[HMW2003]: https://arxiv.org/abs/quant-ph/0304052v2
[AIK2026]: https://arxiv.org/abs/2609.11664v2
[BDK2026]: https://arxiv.org/abs/2609.15063v1
[MPS2023]: https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30
[Drucker2012]: https://arxiv.org/abs/1005.0644v2
[Shaltiel2001]: https://eccc.weizmann.ac.il/report/2001/009/
[Huang2019]: https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf
[Midrijanis2004]: https://arxiv.org/abs/quant-ph/0403168v2
[HLS2007]: https://www.ucw.cz/~robert/papers/madv.pdf
[SS2006]: https://theoryofcomputing.org/articles/v002a001/v002a001.pdf
[BSS2003]: https://doi.org/10.1109/CCC.2003.1214419
[ComplexitylibPinned]: https://github.com/cslib-community/complexitylib/tree/62ca5c21461b2482e8bd12b7cb9b4937d887a33a



## Historical finite-check notes retained from the mathematical account

The passages below preserve the computational evidence pointers and checking qualifications removed from the reader edition. They are copied from the record at commit `071ce02`; their section references, dated status and descriptions belong to that source edition, and do not assert a fresh execution. The mathematical examples and proofs remain in the current paper. Passage and claim identifiers are intentionally not repeated here.

### The four-column certificate checks

**Which board was checked?** The archived checker uses the §4.3 inputs with $\Phi=+1/2$ and $-1/2$. The examples-first exposition uses different inputs with $\Phi=+1$ and $-1$. The 256-input circuit truth table, gate identities and local-test rules transfer unchanged; the board-specific projection probabilities and decoder laws do not. Readers from that exposition can return to its [optional circuit check](exposition.md#circuit-check).

**Finite-check evidence.** The checker evaluates the partial function from the integer expression (4.7) and the Boolean circuit separately, and compares them on all 256 eight-bit inputs. It also checks all 16 candidate pairs on the board against (4.5), each of the 360 single-bit changes to the selected transcripts, and six witnesses showing that every coordinate of a two-bit-pointer/four-bit-target lookup is essential; the preserved round-three output records these checks as passing.

A second board in the output isolates the domain test. Its off-promise column is all ones, stores the true transcripts and has pointers reaching zeros in all other columns, so at the address named by its value-output bits every test except one domain-output test passes. Without the domain tests this column would be accepted incorrectly; with the full test list the board has no winner and the function is zero.

The full gate list, complete base board, selected transcripts, test counts and construction of the second board are in [examples/circuit.json](../research/returns/round3/members/04_addressed_construction/examples/circuit.json), [examples/board.json](../research/returns/round3/members/04_addressed_construction/examples/board.json), and [examples/output.json](../research/returns/round3/members/04_addressed_construction/examples/output.json). From the directory of [the preserved construction return](../research/returns/round3/members/04_addressed_construction/), run [`python3 examples/check_example.py`](../research/returns/round3/members/04_addressed_construction/examples/check_example.py) to reproduce the output with the Python standard library and exact integer or rational arithmetic. These finite computational checks are separate from the general proofs above and from the supplied Lean evidence.

### The comparison example

In the example, column 2 can propose $00$, $01$, $10$, or $11$, and can direct its incoming pointer to any of the four rows of column 1, where it always reads a one, while the true cell $B_{1,10}$ always points to the zero at row 1 of column 2. The checker confirms this for all 16 rival-label/target choices, and for all 48 choices once the other two rivals are included. The tournament in §5 uses this property; comparisons between two nonwinners remain unrestricted.

### The separate-cap finite example

**Finite-check evidence.** The exact calculation and enumeration in [worked_example.md](../research/returns/round3/members/06_direct_product/worked_example.md)
check all 16 input pairs, all 10 one-input trees of depth at most one and
all 5,188 vector-output trees satisfying the separate caps; this finite
check illustrates the proof and its limits, and the preceding argument proves the general theorem.

### The physical planted toy

**Finite-check evidence.** The files [checks/planted_example.py](../research/returns/round3/members/07_planted_lower_bound/checks/planted_example.py) and [checks/planted_example.json](../research/returns/round3/members/07_planted_lower_bound/checks/planted_example.json) implement all 192 physical bit coordinates of this toy and evaluate its winning predicate directly.

### Independent selection control

Thus the identity in (19) needs more than a uniform marginal law for $I$: it needs independence from the whole dummy run. The [retained independence checker](../research/returns/round3/members/09_evidence_backend/checks/eq19_independence_control.py) enumerates this finite experiment, whose counterexample concerns only the altered selection rule; in the preprint's experiment $I$ is independent of the whole run.

### The capped simulator enumeration

**Finite-check evidence.** The exhaustive enumeration in the [planted example](../research/returns/round3/members/07_planted_lower_bound/checks/planted_example.py) fixes the other columns' \(A\)-strings, ranges over all \(4^4\) zero-position vectors and all \(16\) target tuples, and ranges independently over the four choices of \(I\). It obtains
\[
\mathbb EZ=\frac38,\qquad
\Pr[\text{erased-zero hit}]=\frac3{32}
=\frac{\mathbb EZ}{4},
\]
and
\[
\Pr[\text{target 1 nonheavy and time 4 visits its true cell}]
=\frac18
\le
\Pr[\text{capped simulator correct}]
=\frac14.
\]
These finite computations are exact for this toy and this conditional outside configuration; they illustrate the reduction, and the general inequalities rest on the proofs above.

### The Forrelation circuit census

The [exact checker](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/checks/) independently compares direct path summation, dense Walsh multiplication, butterfly multiplication, both integer tests and an append-only Boolean-gate reconstruction on every input at $k=2,t=1$; it also checks all 4,096 inputs at $k=3,t=1$. All arithmetic is integral or rational. These are finite semantic checks, and the ordinary proofs above establish the parameterized conclusions.

### Adversary-normalization finite checks

The [exact-arithmetic checks](../research/returns/round3/members/08_reviewed/quartic_r3_08_return/checks/) check the four input states, oracle permutation, masks, eigenbasis, output probabilities and progress drop.
<!-- /passage:R3-A-PARITY-PREFACTOR -->

### Status of the closed circuit-cost identity

This accounting is a hand derivation from the same constructors and bounds the actual gate list, including its repeated doublings; the closed-form cost identity was not newly compiled as a Lean theorem.

### Bansal–Sinha source coordinates

**Source coordinates.** The supplied source archive has SHA-256 `f48a3225662484d12e19bf03412478cf87a388f7c2e33c69a4d7f2078202e015`. Physical `main.tex` lines 1180–1181 contain those bounds; line 1184 states the subsequent depth threshold.

### Historical authorship and review disclosure

<a id="ai-disclosure"></a>
Will Cook directed this reconstruction. AI agents wrote the Lean formalization, the explanatory additions and the text of this record, working from OpenAI's preprint, which contains the theorem, the construction and both analyses; the earlier ingredients keep their authors' credit as cited. No person has reviewed the mathematics, and the record has not been submitted for publication.

<!-- lean-links -->
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52
[cmp-degree]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/Degree/Challenge.lean#L14-L20
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[cmp-le-iff]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Foundations/Challenge.lean#L326-L330
[cmp-winners]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Construction/Challenge.lean#L326-L341
[cmp-zero-cost]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Independent/ModelZero/Challenge.lean#L11-L14
[def-D]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L76-L77
[def-DLe]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L67-L69
[def-L]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L297-L300
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-QLe]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L133-L137
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-RLe]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L62-L65
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-bansal-sinha]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L305-L309
[def-bit-input]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L15
[def-partial]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L18-L19
[def-realises]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L215-L221
[def-reindex]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L27-L29
[def-totalise]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L21-L22
[def-universal]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L311-L315
[src-alpha]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L17-L18
[src-alpha-infimum]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L240-L248
[src-amplification]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Amplification/Bounded.lean#L238-L293
[src-amplify-measured]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Amplify.lean#L345-L352
[src-budget]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L86-L90
[src-budget-constant]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L52-L57
[src-budget-exponential]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L286-L290
[src-coherent-amplify]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumAmplification.lean#L352-L361
[src-common-workspace]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumWorkspace.lean#L23-L34
[src-comparison-state]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L216-L223
[src-complies]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L50-L61
[src-conditional-value-module]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[src-construction-complete]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionComplete.lean#L23-L67
[src-construction-full]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFull.lean#L21-L69
[src-construction-models]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionModels.lean
[src-count]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L101-L107
[src-coupled-average]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/Main.lean#L26-L29
[src-cubic]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L40-L44
[src-decoder]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L52-L59
[src-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/DirectProduct.lean#L302-L308
[src-direct-product-average]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean#L900-L909
[src-direct-product-capped]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalDirectProduct.lean#L877-L884
[src-direct-product-caps]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/RealizedCapsExternal.lean#L24-L34
[src-direct-product-module]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/DirectProduct.lean
[src-discovered-zeros]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L180-L185
[src-dummy]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/Inputs.lean#L48-L54
[src-equation-15]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTensor.lean#L114-L131
[src-equation-19]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Eq19Whole.lean#L26-L33
[src-equation-19-expectation]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Eq19Complete.lean#L23-L31
[src-equation-two]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFamily.lean#L56-L67
[src-erased-zero-bound]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L249-L254
[src-erased-zero-identity]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L204-L209
[src-error-bound]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L536-L549
[src-eventual-comparison]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L115-L123
[src-expected-zeros]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L197-L202
[src-expected-zeros-bound]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L238-L243
[src-exponent-choice]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L159-L161
[src-family-conditional]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Conditional.lean#L22-L31
[src-fixed-sequence]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Bridge/Deferred.lean#L282-L290
[src-forr-census]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Sanity.lean
[src-forr-circuit]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Circuit.lean#L336-L339
[src-forr-circuit-exists]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Forrelation/Circuit.lean#L477-L482
[src-forr-implementation]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/ForrelationLower/Main.lean#L524-L525
[src-forr-integer]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L139-L152
[src-forr-output-bits]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean#L55-L69
[src-forr-product]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L48-L54
[src-forr-promise]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L57-L65
[src-forr-tests]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L166-L178
[src-forrelation-uniform]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532
[src-found-zero]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean#L156-L159
[src-le-iff-classical]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Model/Classical.lean#L277-L282
[src-le-iff-quantum]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Model/Quantum.lean#L413-L414
[src-lemma-a2]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixASpectralAdversary.lean#L105-L113
[src-lemma-a3]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixAStar.lean#L480-L484
[src-lemma-a4]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixAHuangRoute.lean#L112-L117
[src-lemma-a5]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixASensitivity.lean#L288-L291
[src-lemma21]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean#L63-L90
[src-lemma21-ii]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean#L21-L44
[src-lemma21-iii]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean#L109-L115
[src-no-smaller-exponent]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Exponent.lean#L230-L236
[src-opaque-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/UniformEndpoint.lean#L15-L53
[src-per-time]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L340-L348
[src-planted-core]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/Main.lean#L201-L206
[src-pointer-support]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionPointerSupport.lean#L77-L85
[src-proc]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Amplification/Procedure.lean#L31-L39
[src-prop33]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L270-L273
[src-prop42]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/Section4.lean#L16-L32
[src-q-bound]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Bound.lean#L277-L280
[src-quantum-tournament]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTournamentFacts.lean#L283-L303
[src-quartic-cap]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L46-L51
[src-quartic-hybrid]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L104-L106
[src-quartic-minimum]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L59-L62
[src-quartic-older]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Appendix/TheoremA1.lean#L51-L53
[src-query-oracle]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionModels.lean#L178-L185
[src-ratio-abstract]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalAsymptotics.lean#L332-L348
[src-ratio-arithmetic]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalAsymptotics.lean#L232-L240
[src-ratio-family]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalAsymptotics.lean#L369-L386
[src-runs]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Compile.lean#L329-L332
[src-samples]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Sampler.lean#L113-L117
[src-stage-sampler]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Upper/Tournament.lean#L62-L65
[src-tensor-stage]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumTensor.lean#L322-L335
[src-theorem]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Unconditional.lean#L21-L29
[src-theorem-a1]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/AppendixA.lean#L65-L70
[src-theorem-conditional]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Results/Conditional.lean#L50-L60
[src-transcript]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/Transcript.lean#L62-L65
[src-uniform-zero]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ClassicalUniformZero.lean#L248-L257
[src-universal-power]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Appendix/TheoremA1.lean#L68-L70
[src-verifier]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L496-L507
[src-walsh]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean#L26-L37
[src-winner-dominates]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/QuantumComparison.lean#L294-L302
[src-winner-paper]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/LocalTests.lean#L326-L330
[src-winner-tests]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/LocalTests.lean#L235-L238
[src-winner-unique]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Construction/Winner.lean#L54-L56
[src-zero-successor]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean#L17-L22
[statement-config]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/comparator.json
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
