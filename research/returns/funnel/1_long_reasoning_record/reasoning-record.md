**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# A nearly quartic separation between randomized and quantum queries: a complete reasoning record

## 1. The result and its scope

<a id="ROOT-RESULT"></a>
<!-- passage:ROOT-RESULT -->
The optimal universal power relating bounded-error randomized and quantum query complexity of total Boolean functions is four. This record reconstructs OpenAI's theorem in *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity* (5 October 2026), including the finite-cube proof of the fixed-parameter Forrelation lower bound in the accompanying Lean source. The upper bound for all total functions is due to Aaronson, Ben-David, Kothari, Rao and Tal [ABKRT2021, Theorem 2](https://arxiv.org/abs/2010.12629). The separation construction and its combination of ingredients are attributed to OpenAI [OpenAI2026, Theorem 1.1](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).

Here and throughout, a query reveals one input bit, computation between queries is free, and a query budget is a cap on every possible execution. Let $R(f)$ and $Q(f)$ be the minimum such budgets for randomized and quantum algorithms, respectively, with success probability at least $2/3$ on every input in the domain of $f$. The definitions, including measurements and promises, are given below. Write $\log=\log_2$. The universal exponent is defined by

<!-- claim:eq-1 -->
\[
\alpha_{\mathrm{tot}}=\inf\left\{\alpha\geq0:\ \exists C_\alpha>0\ \forall n\geq1\ \forall f:\{0,1\}^n\to\{0,1\},\quad R(f)\leq C_\alpha(1+Q(f))^\alpha\right\}.
\]

Requiring $C_\alpha>0$ gives the same admissible exponents as requiring a finite real constant: replace any finite witness by its maximum with $1$. The additive $1$ avoids a separate convention for zero-query constant functions.

**Theorem 1.1 (OpenAI).** The universal exponent satisfies

<!-- claim:thm-1.1 -->
\[
\alpha_{\mathrm{tot}}=4.
\]

More precisely, the universal estimate $R(f)=O((1+Q(f))^4)$ holds with an absolute constant. For each fixed integer $k\geq2$, there are positive constants $c_k,C_k,b_k$, a threshold $m_0(k)$, and explicitly defined total Boolean functions $F_{k,m}$, one for each power of four $m\geq m_0(k)$, such that

<!-- claim:eq-2 -->
\[
Q(F_{k,m})\leq C_k\sqrt m\,(\log m)^{b_k},\qquad
R(F_{k,m})\geq c_k\frac{m^{2-1/k}}{(\log m)^2}.
\]

The supplied implementation takes $b_k=6$. The constants and the starting point may depend on the fixed $k$. For each such $k$, these bounds give separation exponent $4-2/k$, up to powers of the logarithm. They rule out every universal exponent below four. They do not assert an exact fourth-power separation for one fixed family. Establishing such a sharper family is outside the result proved here.

The special choice $k=3$ already has exponent $10/3>3$. Consequently the following conjectured universal estimate is false:

<!-- claim:cor-cubic-refuted -->
\[
\neg\exists C\in\mathbb R\ \forall n\geq1\ \forall f:\{0,1\}^n\to\{0,1\},\qquad R(f)\leq C Q(f)^3.
\]

The conjecture is Conjecture 2 in Section 7, printed page 20, of Aaronson, Ben-David, Kothari, Rao and Tal [ABKRT2021](https://arxiv.org/abs/2010.12629). Its formulation concerns all total Boolean functions with one universal constant.

**Evidence.** The supplied source states `QuarticQuery.alphaTot_eq_four_unconditional`, `QuarticQuery.theorem_1_1_unconditional` and `QuarticQuery.cubic_bound_fails_unconditional` in `lean/QuarticQuery/Results/Unconditional.lean`. The second theorem gives the family with an explicit floor lower bound; the floor estimates later in this record give the displayed asymptotic form. These are unconditional declarations. The reported compilation and comparison results belong to the supplied source record. No new Lean kernel execution was available during this reconstruction. The universal upper endpoint is checked by an imported alternative route; the ordinary proof in Appendix A is separately reconstructed in full.
<!-- /passage:ROOT-RESULT -->

<a id="ROOT-ARCHITECTURE"></a>
<!-- passage:ROOT-ARCHITECTURE -->
### 1.1. Why these exponents arise

The construction starts with a partial Boolean function $P_{k,m}$ on $km$ bits. For fixed $k$, a quantum algorithm computes $P_{k,m}$ with a constant number of queries, whereas a classical algorithm needs more than $L=\lfloor m^{1-1/k}/(\log m)^2\rfloor$ queries for sufficiently large $m$. A Boolean circuit of size $O_k(m(\log m)^2)$ decides both the promise and its value. The circuit supplies locally testable certificates.

The total function arranges $m$ columns. A positive input has one all-one column. That column contains several separate instances of $P_{k,m}$; their values specify a hidden address. At that address, a transcript certifies their values and pointers identify a zero in each other column. Every bit pattern has a definite output because inconsistent transcripts, failed promises and unsuccessful pointers simply fail the certificate test.

A quantum algorithm locates the distinguished column through noisy comparisons. Each comparison uses the easy quantum computation of the address and a search for a zero indicated by a pointer. A final search checks the local constraints. This takes $O_k(\sqrt m(\log m)^6)$ queries with a cap on every measurement branch. The randomized lower bound compares a distribution with one zero in every column to a coupled distribution in which one zero is erased and a valid certificate is planted. The algorithm must discover the erased zero or query the hidden address to distinguish them. The former event costs order $m^2$; the latter is suppressed by the hardness of many independent copies of $P_{k,m}$. The resulting lower budget is order $mL$, hence $m^{2-1/k}/(\log m)^2$.

The proof below follows that dependence. It first fixes the models, then proves the partial-function ingredients, defines the total function, proves the quantum upper bound and randomized lower bound, and finally compares powers. Appendix A supplies the independent universal quartic upper bound. Exact statements from the supplied corpus, including its added rows, are reproduced in the statement catalogue, with pointers to the passages that prove them. An entry with no formal tie is still accompanied by a mathematical proof; its absence of a formal tie remains visible.
<!-- /passage:ROOT-ARCHITECTURE -->


## 2. Models, promises and query budgets


<a id="ROOT-LOGS"></a>
<!-- passage:ROOT-LOGS -->
All unqualified logarithms in the parameters $L,r,\ell,T$ are base two. Natural logarithms are written $\ln$; they occur in analytic estimates. Changing the base in an asymptotic estimate multiplies a logarithm by a fixed positive constant, which is absorbed into the stated constant. The exact powers and floors defining a function always use the displayed base. The family is indexed by an integer $t$, with $m=4^t=2^{2t}$, so $\log m=2t$ exactly. This fixes the convention in `def-log-convention`.
<!-- /passage:ROOT-LOGS -->

<a id="ROOT-PARTIAL"></a>
<!-- passage:ROOT-PARTIAL -->
### 2.1. Classical queries

A finite coordinate set is denoted by $I$. An input is a map $x:I\to\{0,1\}$. A partial Boolean function consists of a domain $D\subseteq\{0,1\}^I$ and a map $f:D\to\{0,1\}$. In the Lean vocabulary it is a function `PartialBool I`, which returns `some b` on a promised input of value $b$ and `none` off the promise. A total function is converted to this form by `totalise`. Correctness is required on $D$. An algorithm's behavior on other inputs is unrestricted, although its query cap still holds there.

A deterministic decision tree has a Boolean label at each leaf and a coordinate at each internal node. At a node labeled $i$, the next branch is selected by $x_i$. The depth is the greatest number of internal nodes on any root-to-leaf path. Repeated queries are counted each time. The tree computes $f$ if its output equals $f(x)$ for every $x\in D$. For total functions, the deterministic complexity is

<!-- claim:def-D -->
\[
D(f)=\min\{q\in\mathbb N:\text{a deterministic decision tree of depth at most }q\text{ computes }f\}.
\]

The same definition on a promise is useful in intermediate steps. A randomized algorithm is a probability distribution on deterministic trees. A fixed query cap $q$ means that every tree in its support has depth at most $q$. We allow arbitrary real probabilities. For fixed finite $I$ and $q$, there are finitely many labeled trees of depth at most $q$: at depth zero there are two, and at each next depth a tree is either a leaf or a choice of one of finitely many coordinates and two smaller trees. Thus any distribution over internal random tapes can be grouped by its resulting tree into a finite mixture. Discarding trees of zero probability gives the positive weights used by `RandomizedProgram`.

<!-- claim:def-R -->
\[
R(f)=\min\left\{q\in\mathbb N:\ \exists\text{ a distribution on trees of depth at most }q\ \forall x\in D,\quad\Pr[T(x)=f(x)]\geq\frac23\right\}.
\]

There is always a witness to either minimum. Order the coordinates, query each once, then output $f(x)$ when promised and an arbitrary bit otherwise. Its depth is $|I|$. The nonempty set of admissible natural budgets therefore has a least member. Enlarging a budget never invalidates an algorithm. It follows that $R(f)\leq q$ is equivalent to the existence of an admissible $q$-query randomized algorithm, and $q<R(f)$ is equivalent to its nonexistence. A deterministic tree gives a one-point randomized distribution, so $R(f)\leq D(f)\leq |I|$. These observations justify the natural-number infima in the source; an empty infimum is never used to obtain a lower bound.

Renaming coordinates by a bijection changes no complexity. Relabel every query node by the bijection and identify the corresponding inputs; evaluation and every path length are unchanged. Applying the inverse bijection gives the reverse inequality. This will let us present the construction with structured coordinates while applying a universal statement about $\{0,1\}^n$.

**Evidence.** The definitions are `QuarticQuery.QueryTree`, `QueryTree.depth`, `RLe`, `DLe`, `R`, and `D` in `Statement.lean`. `Model/Classical.lean` proves `DLe_card`, `RLe_R`, `DLe_D`, `R_le_iff`, `D_le_iff`, `lt_R_iff`, `R_le_D`, and the reindexing theorems. The corpus has exact ties for the least-budget characterizations; some definitional rows have only neighboring partial ties. Reading a definition directly is identified here as source inspection and does not create a new comparison receipt.
<!-- /passage:ROOT-PARTIAL -->

<a id="ROOT-ORACLE"></a>
<!-- passage:ROOT-ORACLE -->
### 2.2. Quantum queries and adaptive measurements

For a nonempty coordinate set, take a finite-dimensional complex Hilbert space with computational basis $|i,b,z\rangle$, where $i\in I$, $b\in\{0,1\}$, and $z$ is a workspace label. The input oracle is

<!-- claim:def-query-oracle -->
\[
O_x|i,b,z\rangle=|i,b\mathbin\oplus x_i,z\rangle.
\]

For each $x$, this map permutes an orthonormal basis, hence preserves all inner products and norms. Applying it twice toggles the same bit twice, so $O_x^2=I$. Gates between queries are arbitrary input-independent unitaries. A phase query is obtained by placing the answer bit in $(|0\rangle-|1\rangle)/\sqrt2$, because a toggle then multiplies that state by $(-1)^{x_i}$. Conversely, conjugating the answer bit by its Hadamard transform exchanges the bit-query and controlled-phase descriptions. This costs no extra oracle call.

The source allows a finite adaptive program with four kinds of operation: return a bit; apply a unitary; make a query; or measure a coordinate projector and continue with one of two programs. A measurement by an orthogonal projector $\Pi$ has unnormalized branches $\Pi\psi$ and $(I-\Pi)\psi$. Their squared norms are the probabilities when $\|\psi\|=1$. Keeping these vectors unnormalized automatically retains the probability of reaching a branch. The budget is defined recursively by maximum at a measurement, no increment at a unitary, and an increment of one at a query. This charges every possible outcome, including outcomes whose probability happens to vanish on a particular input.

Let $M_A(x,\psi,b)$ be the mass assigned to output $b$ by program $A$, on input $x$ and initial vector $\psi$. For a return command this mass is $\|\psi\|^2$ for its returned bit and zero for the other. A gate or query transforms the state before continuing. A measurement sums the two continuation masses on the two projected states. These rules imply

<!-- claim:ROOT-MASS -->
\[
M_A(x,\psi,b)\geq0,\qquad M_A(x,\psi,0)+M_A(x,\psi,1)=\|\psi\|^2.
\]

For completeness, induction on the program proves both assertions. They hold for a return command. At a unitary or query, apply the induction hypothesis to the transformed state, whose norm is unchanged. At a measurement, each output mass is a sum of nonnegative terms. The sum over both outputs is $\|\Pi\psi\|^2+\|(I-\Pi)\psi\|^2$, which is $\|\psi\|^2$ because the two projected vectors are orthogonal and add to $\psi$. In particular a normalized initial vector gives a probability distribution on the output bit.

The initial state, all gates, every query coordinate register and every branch rule are chosen before the input. The definition is

<!-- claim:def-Q -->
\[
Q(f)=\min\left\{q\in\mathbb N:\ \exists\text{ an input-independent quantum program of query cap at most }q\ \forall x\in D,\quad\Pr[A(x)=f(x)]\geq\frac23\right\}.
\]

A function constant on its promise is permitted a zero-query constant output. This includes an empty promise and the empty coordinate type, for which the source's explicit indexed Hilbert space would have dimension zero. For every other partial function a deterministic read-all tree can be simulated exactly: prepare $|i,0,z\rangle$, query the chosen coordinate, measure its answer, and follow the corresponding child. A query-free change of basis prepares the next coordinate. Induction on the tree gives the same answer and cap. Thus the set of admissible quantum budgets is nonempty, and its minimum is attained. In particular $Q(f)\leq D(f)\leq |I|$. Coordinate bijections act by a unitary relabeling of the query register and preserve output probabilities and caps.

**Evidence.** `QuarticQuery.bitOracle`, `AdaptiveProgram`, `AdaptiveProgram.queryCap`, `AdaptiveProgram.outputMass`, `ConstantOnPromise`, `QLe` and `Q` are in `Statement.lean`. The norm and involution statements and the two mass identities are proved in `Model/Quantum.lean`, as are `DLe.toQLe`, `QLe_card`, `QLe_Q`, `Q_le_iff` and `Q_reindex`. The new displayed mass row only exposes existing theorems. It introduces no new mathematical assertion beyond those declarations.
<!-- /passage:ROOT-ORACLE -->

<a id="ROOT-EVIDENCE-CONVENTION"></a>
<!-- passage:ROOT-EVIDENCE-CONVENTION -->
### 2.3. How the evidence is stated

Theorem, lemma, proposition and equation numbers retain the source preprint's numbering; section numbers refer to this record unless another work is named. Claim identifiers refer to the supplied statement corpus or the accompanying registry of new statements.

A mathematical proof and a formal theorem answer different reading questions. Each proof here is ordinary mathematics with its assumptions stated where needed. Its evidence note identifies the corresponding declarations and says whether they prove the same statement, a stronger statement, part of the statement, or a statement by another route. A theorem's appearance in the dependency closure of the main result does not extend its scope to nearby claims. Conversely, an elementary definition can be visibly present in the source even when the corpus lacks a formal tie to its row.

All packet-relative source paths below refer to repository commit `c7e0c9161f0ad898889bd9166e7b354acd42188d`. The companion files preserve the corpus's original statements and evidence while recording corrections and new expository claims separately. Compilation and comparator statuses are reported evidence from that packet, not a fresh execution during this reading. The full methods, source inventory and limits of the available verification are in `review_notes.md`; `LEAN_GAPS.md` lists every displayed step whose formal support is partial, absent or by another route.
<!-- /passage:ROOT-EVIDENCE-CONVENTION -->


## 3. Forrelation: the promise problem and its complete lower bound


<a id="forr_scope"></a>
<!-- passage:forr_scope -->

This section supplies the complete Forrelation ingredient used in the total-function construction. Fix an integer \(k\ge2\). The dimension is \(m=4^t\), and statements about sufficiently large dimensions mean every integer \(t\) above a threshold depending on \(k\). The input has \(km\) bits. Constants depending on \(k\) are permitted throughout this ingredient; no claim here supplies a uniform nearly quartic separation by allowing \(k\) to vary with \(m\).

For $0<\varepsilon<1/2$, write $R_\varepsilon(P)$ and $Q_\varepsilon(P)$ for the minimum worst-case numbers of classical randomized and quantum bit queries that give error at most $\varepsilon$ on every promised input. A query cap applies on every execution and input. Write $R(P)=R_{1/3}(P)$; the notation $Q_\eta$ below uses the requested error $\eta$. These are the same conventions as the query models in the rest of the record.

The three conclusions are a randomized lower bound, a quantum promise algorithm, and an exact Boolean circuit recognizing the promise and its value. The preprint obtains the first conclusion from Bansal and Sinha. The supplied Lean source proves that conclusion by its own Gaussian and decision-tree argument. We give both the short published implication and the entire internal argument. The mathematical comparisons below concern the statements and source proofs inspected in this packet. The corpus reports builds at the supplied pin; this reading did not run Lean or its statement comparator, and the packet contains no build-receipt directory. A reported build therefore remains a supplied claim about a previous run.
<!-- /passage:forr_scope -->

<a id="forr_definition"></a>
<!-- passage:forr_definition -->

### 3.1. The normalized Walsh product and the promise

Index the \(m\) coordinates by binary strings of length \(2t\). Arithmetic in their inner product is over the two-element field. A bit \(x\) denotes the sign \((-1)^x\), so a true bit is the negative sign. For an input block \(z_r\in\{-1,1\}^m\), let \(D_{z_r}\) be its diagonal matrix. We number the blocks from \(0\) to \(k-1\); this only shifts the preprint's subscripts.

<!-- claim:def-walsh-sign -->
\[
W_{ab}=(-1)^{a\cdot b},\qquad H=m^{-1/2}W,\qquad
u=m^{-1/2}(1,\ldots,1)^{\mathsf T},\qquad D_z=\operatorname{diag}(z).
\]

For rows \(a,c\), the product of their entries at \(b\) is \((-1)^{(a+c)\cdot b}\). If \(a=c\), every summand is one. Otherwise choose a coordinate where \(a+c\) is one. Pair each \(b\) with the string obtained by flipping that coordinate. The paired terms have opposite signs. This proves the following identities and norm bound.

<!-- claim:NEW-FOR-01 -->
\[
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
\]

Each factor in the alternating product preserves Euclidean norm. Cauchy–Schwarz therefore bounds the absolute value of its inner product with \(u\) by one. In particular, the following real quantity is defined on every input and lies in \([-1,1]\).

<!-- claim:eq-3 -->
\[
\Phi(z)=u^{\mathsf T}D_{z_0}H D_{z_1}H\cdots H D_{z_{k-1}}u,
\qquad \delta=2^{-5k}.
\]

The promise uses a positive, one-sided yes case. A large negative value is outside the promise. Since \(\delta>0\), the two specified cases cannot overlap: \(\Phi\ge\delta\) implies \(|\Phi|\ge\delta>\delta/2\).

<!-- claim:eq-4 -->
\[
P_{k,m}(z)=
\begin{cases}
1,&\Phi(z)\ge\delta,\\
0,&|\Phi(z)|\le\delta/2,\\
\text{undefined},&\text{otherwise}.
\end{cases}
\]

The lower-bound scale, with the preprint's base-two logarithm, is

<!-- claim:eq-5 -->
\[
L=L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
\]

We use this formula only when \(t\ge1\), and the lower-bound proof will take \(t\ge8\). The formal definitions also assign values at \(t=0\); their totalized division by zero is irrelevant to these claims.

**Source and evidence.** The definitions and orthogonality calculations are in `Forrelation/Walsh.lean` and `Forrelation/Product.lean`: `walshN`, `walshZ`, `W`, `H`, `sum_walshN_mul`, `W_mul_transpose`, `H_mul_H`, `u`, `signDiag`, `Phi_eq_matrix_product`, and `abs_Phi_le_one`. The three branches and their disjointness are proved in `Forrelation/Promise.lean` by `P_eq_cases` and `cases_disjoint`. These declarations support different parts of the corpus rows; the corpus correctly describes them as partial matches individually. The row for \(L\) has no formal tie, although `QuarticQuery.Lvalue` in `Statement.lean` is the corresponding frozen definition. This missing tie should be recorded without claiming an additional build.
<!-- /passage:forr_definition -->

<a id="forr_integer"></a>
<!-- passage:forr_integer -->

### 3.2. An integer numerator and exact promise tests

There are two boundary factors \(m^{-1/2}\), and \(k-1\) occurrences of \(H=m^{-1/2}W\). Expanding matrix multiplication gives a sum over one coordinate in each block. Every summand before normalization is an integer of absolute value one. Thus

<!-- claim:claim-N-phi -->
\[
\begin{aligned}
N(z)&=\sum_{p\in[m]^k}
 \left(\prod_{r=0}^{k-1}z_r(p_r)\right)
 \left(\prod_{r=0}^{k-2}W_{p_r,p_{r+1}}\right)\in\mathbb Z,\\
M&=m(\sqrt m)^{k-1}=2^{t(k+1)}>0,\qquad
\Phi(z)=\frac{N(z)}{M}.
\end{aligned}
\]

Equivalently, start with the last sign vector, multiply alternately by \(W\) and by the preceding sign diagonal, and sum the resulting coordinates. This right-to-left recurrence is the matrix formula for \(N\). The denominator is integral because \(\sqrt m=2^t\). The norm bound already proved implies \(|N|\le M\).

Multiplying inequalities by the positive integers \(M\) and \(2^{5k}\) gives exact integer comparisons, with no numerical approximation.

<!-- claim:claim-integer-tests -->
\[
\Phi\ge\delta\ \Longleftrightarrow\ 2^{5k}N\ge M,
\qquad
|\Phi|\le\delta/2\ \Longleftrightarrow\ 2^{5k+1}|N|\le M.
\]

Let \(p_1\) be the first comparison and \(p_0\) the second. Then the desired circuit outputs are \(d=p_1\lor p_0\) and \(b=p_1\). The already proved disjointness means that \(d=1\) identifies the domain exactly and \(b\) gives the promised value there.

**Source and evidence.** `numerator_eq_walk` and `Phi_eq_matrix_product` in `Forrelation/Product.lean` identify the path numerator with the alternating product. The equivalences are `delta_le_Phi_iff` and `abs_Phi_le_iff` in `Forrelation/Promise.lean`. Integrality is present in the integer type of `forrelationNumerator`; positivity is `forrelationDenominator_pos`. The later `P_tests` expresses the same comparisons in the sign-test form used by the circuit. These facts jointly support `claim-N-phi` and `claim-integer-tests`; no single cited declaration contains every sentence of either row.
<!-- /passage:forr_integer -->

<a id="forr_quantum"></a>
<!-- passage:forr_quantum -->

### 3.3. The quantum promise algorithm, including amplification and coherence

Prepare the state \(|u\rangle\) in an address register. Apply the alternating product in the definition of \(\Phi\), reading the displayed product from right to left. Each \(D_{z_r}\) costs one bit query: with the response qubit in \(|-\rangle=(|0\rangle-|1\rangle)/\sqrt2\), the oracle's response flip acts as multiplication by \((-1)^{x_{r,a}}\) on address \(a\). The response qubit returns to \(|-\rangle\), so it carries no input-dependent entanglement. Each \(H\) is input independent and costs no queries.

Project onto \(|u\rangle\). This can be implemented by applying the inverse of its query-free preparation and testing whether the address register is zero. If \(|\psi_z\rangle\) is the state before this projection, its amplitude along \(u\) is \(\langle u|\psi_z\rangle=\Phi(z)\). Consequently one trial uses \(k\) bit queries and has success probability

<!-- claim:claim-proj-prob -->
\[
p(z)=|\langle u|\psi_z\rangle|^2=\Phi(z)^2,
\qquad P(z)=1\Rightarrow p(z)\ge\delta^2,
\qquad P(z)=0\Rightarrow p(z)\le\delta^2/4.
\]

Here squaring does not lose the promise distinction: a large negative value, which would also have large squared amplitude, was never assigned a required answer. Put \(c=\delta^2\). Run the trial independently \(q\) times and output one when its number \(S\) of successes is at least \(qc/2\). To account for the complete error estimate, use the binomial moment identity \(\mathbb E a^S=(1-p+pa)^q\), which follows by multiplying the \(q\) independent one-trial moments.

For \(p\le c/4\), Markov's inequality applied to \(e^S\) gives \(\Pr[S\ge qc/2]\le e^{-qc/2}(1+p(e-1))^q\). The elementary inequality \(1+y\le e^y\), together with \(e-1\le7/4\), bounds this by \(e^{-qc/16}\). For the other tail, \(p\ge c\), apply Markov to \(e^{-S}\). Since \(1-e^{-1}\ge3/5\), the resulting bound is \(e^{qc/2-3qp/5}\le e^{-qc/10}\le e^{-qc/16}\). These numerical inequalities can be checked without a tail-bound theorem: the exponential series gives \(e>1+1+1/2+1/6>5/2\), and its tail from the \(1/4!\) term is at most \((1/24)\sum_{j\ge0}5^{-j}=5/96\), giving \(e<11/4\). Markov itself is the pointwise inequality \(Y\ge a\mathbf1_{Y\ge a}\), integrated for a nonnegative random variable.

<!-- claim:NEW-FOR-02 -->
\[
\begin{aligned}
p\le c/4&\ \Longrightarrow\ \Pr[S\ge qc/2]\le e^{-qc/16},\\
p\ge c>0&\ \Longrightarrow\ \Pr[S<qc/2]\le e^{-qc/16},\\
q&=\left\lceil16\,2^{10k}\ln(1/\eta)\right\rceil
 \ \Longrightarrow\ \Pr[\text{error}]\le\eta.
\end{aligned}
\]

The threshold is a real number compared with the integer \(S\); it means \(S\ge\lceil qc/2\rceil\), so no rounding assumption has been inserted. The ceiling bound gives \(q\le1+16\,2^{10k}\ln(1/\eta)\). For fixed \(k\), multiplying by \(k\) gives the required query cost.

To retain coherence, use a fresh address register for each trial and do not measure it. After the query-free inverse preparation, compute the predicate “address equals zero” reversibly into a fresh flag. The two flag values label orthogonal subspaces. The \(q\)-trial state is the tensor product of the one-trial states, so summing squared amplitudes over flag strings of weight \(s\) gives the same binomial probability. Reversibly compute their Hamming weight and then the threshold predicate into an output bit, retaining the flags, count, and every address register. A classical map \(f\) can be implemented reversibly by \(|x,b\rangle\mapsto|x,b\oplus f(x)\rangle\); it is a permutation and hence unitary. This explains the count and threshold operations without discarding their inputs. All operations are defined on every input, and the final output register always measures to a bit. Correctness is asserted only where \(P\) is defined.

<!-- claim:NEW-FOR-28 -->
\[
\forall\,0<\eta<\tfrac12,\qquad
Q_\eta(P_{k,m})\le
k\left\lceil16\,2^{10k}\ln(1/\eta)\right\rceil
=O_k(1+\log(1/\eta)),
\]

<!-- claim:lem-2.1.ii -->
The bound is $O_k(1+\log(1/\eta))$, with a coherent implementation retaining all workspace and a bit output on all inputs.

**Source and evidence.** `successProb_eq`, `successProb_of_true`, `successProb_of_false`, `binomTail_small`, `binomTail_large`, `repetitions_le`, and `threshold_correct` are in `Forrelation/Repetition.lean`. They formalize the real probability calculations. The inspected declarations `Upper.forr_samples`, `Upper.decode_samples`, `Upper.decodeProb_correct`, and `Upper.P_runs` connect these probabilities to coherent samplers and bit-oracle programs. Their compiler charges two bit queries per abstract read, yielding \(2qk\) queries. Thus their compiled bound proves the stated \(O_k(1+\log(1/\eta))\) conclusion, while the sharper \(qk\) count in the display has the phase-kickback proof just given and is not the literal count certified by `P_runs`. The manuscript's `claim-proj-prob` is therefore correctly tagged partial by the corpus. Aaronson and Ambainis supply the underlying Forrelation quantum construction [AA18, discussion of \(k\)-fold Forrelation](https://arxiv.org/abs/1411.5729); Bansal–Sinha also describe a different interference test with probability \((1+\Phi)/2\) [BS21, Proposition 1.2](https://arxiv.org/abs/2008.07003). We need only the squared-projection test above.
<!-- /passage:forr_quantum -->

<a id="forr_circuit"></a>
<!-- passage:forr_circuit -->

### 3.4. The exact Boolean circuit

The circuit must determine both promise membership and value on every input, so a numerical approximation to \(\Phi\) would be insufficient. We compute the integer comparisons instead. First we describe the arithmetic recurrence; then we explain how bounded-fan-in Boolean gates implement it with the claimed size.

For an array \(a\) of length \(2^{h+1}\), split it into its two length-\(2^h\) halves. If \(T_0,T_1\) are their unnormalized Walsh transforms, the transform of \(a\) consists of \(T_0+T_1\) followed by \(T_0-T_1\). To verify this, split a binary output index into its highest bit and remaining bits. The highest input bit contributes sign \(+1\) in the first half and \((-1)^{\text{highest output bit}}\) in the second. This gives both branches coordinate by coordinate.

<!-- claim:NEW-FOR-03 -->
\[
W_{2^{h+1}}(a_0,a_1)
=\bigl(W_{2^h}a_0+W_{2^h}a_1,
        W_{2^h}a_0-W_{2^h}a_1\bigr).
\]

<!-- claim:claim-circuit-size -->
At each level there are \(2^{h+1}\) additions or subtractions, over \(h+1\) levels. Thus a transform on \(m\) entries uses \(m\log_2m\) integer additions and subtractions. The numerator requires \(k-1\) transforms, \(k\) layers of coordinate sign multiplication, and a final sum. For a direct integer computation, a transform multiplies the maximum absolute coordinate by at most \(m\); an intermediate butterfly value is a signed sum of a subset of the current inputs and obeys the same bound. Starting from signs, all transform and final-sum values have magnitude at most \(m^k\). For \(m\ge4\), they need at most \(k\log_2m+2\) signed bits. The constant-factor shifts in the comparisons add \(O(k)\) bits. This proves the intermediate-size assertion in `claim-circuit-size` directly.

The supplied circuit uses a convenient variant: it maintains residues modulo one fixed power of two. Addition, subtraction, and sign multiplication commute with taking residues, so large intermediate integers require no separate sign interpretation. Only the final three comparisons require recovering a sign. This implementation also explains exactly which magnitude bound the formal circuit uses.

For a word of \(w\) bits, a full adder has five gates. On bits \(a,b,c\), compute \(r=a\mathbin{\mathrm{xor}}b\), the sum bit \(s=r\mathbin{\mathrm{xor}}c\), and the carry \((a\land b)\lor(r\land c)\). If zero or one of \(a,b,c\) is one, the carry is zero and \(s\) equals the number of ones. If two or three are one, the carry is one and \(s\) is respectively zero or one. Hence \(s+2\,\mathrm{carry}=a+b+c\) in all cases. Chaining these identities with powers-of-two weights cancels successive carries and proves the usual ripple identity. Discarding the last carry computes addition modulo \(2^w\), at cost \(5w\).

To choose addition or subtraction according to a sign bit \(b\), xor every bit of the second word with \(b\), then add with initial carry \(b\). At \(b=0\) this adds the word unchanged. At \(b=1\), bitwise complement represents \(2^w-1-B\), and the initial carry makes the residue \(-B\pmod{2^w}\). The extra xors cost \(w\) gates. We obtain the costs

<!-- claim:NEW-FOR-04 -->
\[
\begin{array}{c|c}
\text{operation modulo }2^w&\text{non-input gates}\\ \hline
A+B&6w\\
A-B&6w+1\\
(-1)^b B&6w
\end{array}
\qquad
\operatorname{whtCost}(w,h)\le h2^h(6w+1).
\]

The subtraction count includes one constant-true gate. The last inequality follows by induction from the butterfly recurrence: two transforms of length \(2^h\), followed by \(2^h\) additions and \(2^h\) subtractions, cost at most \(2h2^h(6w+1)+2^h(12w+1)\le(h+1)2^{h+1}(6w+1)\). All these gates have fan-in at most two. Negation, constants, and arbitrary two-input Boolean gates fit the circuit model in the packet.

Set \(s=5k\), \(e=t(k+1)\), and use \(w=s+3+e\) bits. The three signed integers whose signs are needed are \(A=2^sN-M\), \(B=M-2^{s+1}N\), and \(C=M+2^{s+1}N\). Since \(M=2^e\) and \(|N|\le M\), their magnitudes are at most \((2^{s+1}+1)M<4\,2^sM=2^{w-1}\). Thus each lies in the signed interval where the high bit of its residue is exactly its sign bit.

<!-- claim:NEW-FOR-05 -->
\[
-2^{w-1}\le A,B,C<2^{w-1},\qquad
p_1=\neg\operatorname{neg}(A),\qquad
p_0=\neg\operatorname{neg}(B)\land\neg\operatorname{neg}(C).
\]

For completeness, a nonnegative integer below \(2^{w-1}\) has high bit zero. For a negative integer at least \(-2^{w-1}\), its least nonnegative residue is \(2^w+T\in[2^{w-1},2^w)\), which has high bit one. This proves the sign test. The conjunction for \(p_0\) states \(-M\le2^{s+1}N\le M\), exactly the absolute-value comparison. Assemble \(b=p_1\), \(d=p_1\lor p_0\), using three final gates when negated inputs are absorbed into their two-input truth tables.

The complete size estimate in the source is explicit. Write \(a=k+1\), \(X=mt^2\), \(Z=aX\), and \(Y=a^2X\). For \(t\ge1\), the width obeys \(w\le6at\), whence \(tmw\le6Z\) and \(mw\le6Z\). The transform bound gives \(\operatorname{whtCost}(w,2t)\le84Z\). All \(k\) sign layers and \(k-1\) transforms cost at most \(1+120Y\). The final sum costs at most \(36Z\); forming \(2^{5k}N\) by repeated doubling costs at most \(180Y\); forming \(M\) from one costs at most \(36Y\). The remaining additions, subtractions, and output gates cost at most \(144Z+6\). The sum is at most \(336Y+180Z+7\le523Y\le800Y\). This deliberately loose accounting proves the source constant.

<!-- claim:NEW-FOR-29 -->
\[
\begin{gathered}
\forall k\ge1\ \forall t\ge1\ \exists C_{k,m},\qquad
S\le200(k+1)^2m(\log_2m)^2,\\
d(z)=1\ \Longleftrightarrow\ z\in\operatorname{dom}P_{k,m},
\qquad d(z)=1\ \Longrightarrow\ b(z)=P_{k,m}(z).
\end{gathered}
\]

<!-- claim:lem-2.1.iii -->
In particular, for each fixed $k\ge2$ this is an exact circuit of size $O_k(m(\log_2m)^2)$ with the required domain and value outputs.

The gate list is acyclic because each new gate reads input wires or earlier gates. Its execution assigns each gate the truth function of its already determined predecessors, yielding a transcript. Any transcript satisfying the same local gate equations agrees with this one by induction on the gate index. Therefore the circuit's exact arithmetic also supplies the canonical gate values needed later in the transcript construction.

**Source and evidence.** `fullAdd_spec`, `ripple_spec`, `addsub_spec`, `signMul_spec`, and `sign_wire` are in `Forrelation/Arithmetic.lean`; `wht_spec`, `whtCost_le`, `layers_spec`, `test_bounds`, `forrCore_spec`, `forrCircuit_realises`, `coreSize_le`, and `exists_circuit` are in `Forrelation/Circuit.lean`. `Forrelation/Builder.lean` supplies extension and execution invariants culminating in `realises_of_run`. The formal circuit is a same-purpose residue implementation of the preprint's integer computation. The standalone preprint sentence about every intermediate integer is proved above; `abs_numerator_le`, the sole declaration tied to `claim-circuit-size`, only bounds the final numerator and must not be described as proving that whole sentence. `exists_circuit` gives a stronger parameter range than the lemma requires.
<!-- /passage:forr_circuit -->

<a id="forr_small_instance"></a>
<!-- passage:forr_small_instance -->

### 3.5. A complete check of the smallest nontrivial instance

The source includes a finite census at $k=2$, $t=1$, so $m=4$. It can be verified directly without trusting an enumeration. Here $M=8$ and $\delta=2^{-10}$. The four rows of $W$ are sign vectors with even parity, meaning an even number of negative entries. Their negatives also have even parity, and the eight signed rows are distinct: orthogonal rows cannot agree up to sign. They account for all eight even-parity sign vectors.

If the second block is a signed row, orthogonality makes $Wz_1$ a vector with one nonzero coordinate, equal to $4$ or $-4$. As the first block ranges over its sixteen possible sign vectors, the numerator is $4$ on eight inputs and $-4$ on eight. The eight choices for the second block in this class therefore contribute sixty-four positive and sixty-four negative numerators.

The other eight possible second blocks have odd parity. Every row has even parity, so its coordinatewise product with such a block has odd parity. The sum of four signs with odd parity is $2$ or $-2$; it can be neither zero nor $4$ nor $-4$. Thus all four coordinates of $Wz_1$ are signs times two. Multiplying by the freely chosen first-block signs makes the numerator twice a sum of four independent signs. The multiplicities for the possible numerators $-8,-4,0,4,8$ are therefore $1,4,6,4,1$, by choosing which of the four summands are positive. The eight second blocks of this class contribute forty positive numerators, forty negative numerators, and forty-eight zeros.

Every positive numerator in this instance is at least four, and thus has $\Phi\ge1/2>\delta$. Every negative numerator has $\Phi\le-1/2$, placing it outside both promise cases. The zero numerators are exactly the zero-inputs. The census is consequently

<!-- claim:NEW-FOR-26 -->
\[
|\{z:P_{2,4}(z)=1\}|=104,\qquad
|\{z:P_{2,4}(z)=0\}|=48,\qquad
|\{z:P_{2,4}(z)\text{ undefined}\}|=104.
\]

In particular the promise contains both values and has a nonempty complement already at this small dimension. For a concrete negative example, take both blocks to be $(-1,1,1,1)$. Direct multiplication gives $W(-1,1,1,1)^{\mathsf T}=(2,-2,-2,-2)^{\mathsf T}$, so $N=-8$ and $\Phi=-1$. This example also checks the direction of the yes inequality and the bit-to-sign convention.

Forrelation/Sanity.lean records these facts as **census_true**, **census_false**, **census_none**, **promise_nonempty_two_one**, **Phi_negativeWitness**, and **P_negativeWitness**. The census declarations use a kernel computation in the supplied source. The argument above supplies an independent mathematical count; this session did not replay the kernel computation. The example is a finite consistency check, not a substitute for the lower bound at growing dimensions.
<!-- /passage:forr_small_instance -->

<a id="forr_bs_translation"></a>
<!-- passage:forr_bs_translation -->

### 3.6. The published lower bound implies the required scale

Bansal and Sinha prove that bounded-error randomized decision trees for the same \((2^{-5k},k)\)-Forrelation promise need at least a universal positive constant times \(k^{-29}(m/\log(km))^{1-1/k}\) queries [BS21, Theorem 1.3 and Corollary 1.4](https://arxiv.org/abs/2008.07003). Their \(N\) is our \(m\), the size of one block; the total input length is \(km\). Both normalized products and both promise thresholds agree. Logarithm bases only modify the positive constant.

Fix \(k\ge2\), write \(\alpha=1-1/k\), and use base-two logarithms in the comparison. For \(m\ge k\), \(\log_2(km)\le2\log_2m\). Dividing the published lower bound by the unfloored expression for \(L\) gives a ratio at least \(c k^{-29}2^{-\alpha}(\log_2m)^{2-\alpha}\). The exponent is \(2-\alpha=1+1/k>0\). Choose \(m\) large enough that this last quantity exceeds one. Positivity of the common numerator then gives

<!-- claim:claim-bs-to-L -->
\[
c k^{-29}\left(\frac{m}{\log_2(km)}\right)^{1-1/k}
>\frac{m^{1-1/k}}{(\log_2m)^2}
\ge\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor=L.
\]

This proves the required strict lower bound by the preprint's literature route. The constant \(c\) must be positive; that condition is implicit in its lower-bound origin and should be explicit when the comparison is isolated.

**Evidence correction.** The corpus labels `claim-bs-to-L` an exact alternative-route consequence of `QuarticQuery.ForrelationLower.bansalSinhaLower`. That declaration proves the final assertion \(R(P)>L\); it never states the numerical comparison displayed here. Proving an endpoint by another argument does not prove every intermediate claim of the original argument. The comparison therefore has a complete mathematical proof here and a primary-source premise, but no exact formal witness in the supplied tie. Its evidence field should be corrected. The same declaration is an exact alternative-route witness for `lem-2.1.i`, where its conclusion belongs. Its actual location is `ForrelationLower/Main.lean`, and it is a theorem, not a definition in `Statement.lean`.
<!-- /passage:forr_bs_translation -->

<a id="forr_cube"></a>
<!-- passage:forr_cube -->

### 3.7. The internal lower-bound proof: finite-cube calculus

We now prove the required randomized lower bound without invoking the published lower bound as a hypothesis. The probabilistic objects used below are explicit finite-cube distributions obtained by averaging product measures over Gaussian parameters. The main analytic identity measures the effect of changing just the first block of biases.

Let $I$ be a finite coordinate set. Identify a bit assignment with its sign vector $z\in\{-1,1\}^I$. For real biases $\mu=(\mu_a)_{a\in I}$, define the polynomial extension of a real function $g$ by

<!-- claim:NEW-FOR-06 -->
\[
p_\mu(z)=\prod_{a\in I}\frac{1+\mu_a z_a}{2},
\qquad
\mathcal E_\mu g=\sum_{z\in\{-1,1\}^I}g(z)p_\mu(z),
\qquad
\partial_a g(z)=\frac{g(z_{a\leftarrow1})-g(z_{a\leftarrow-1})}{2}.
\]

When every $|\mu_a|\le1$, each factor of $p_\mu$ is nonnegative. Summing independently over each sign gives $\sum_zp_\mu(z)=\prod_a1=1$. Hence $\mathcal E_\mu$ is an expectation: it preserves inequalities, sends constants to themselves, and satisfies $|\mathcal E_\mu g|\le B$ when $|g|\le B$. At other real biases it remains a polynomial, which permits differentiation without a domain convention.

Separate the two terms with signs $+1$ and $-1$ in coordinate $a$. This shows that $\mathcal E_\mu g$ is affine in $\mu_a$, with derivative $\mathcal E_\mu\partial_a g$. The discrete derivative is independent of $z_a$, so differentiating twice at the same coordinate gives zero. Derivatives at different coordinates commute because the four updated values and their signs are identical in both orders. Also $|\partial_a g|\le B$ if $|g|\le B$, by the triangle inequality and division by two. These facts iterate to any list of distinct coordinates.

For a differentiable bias path $c(s)$, differentiate the finite polynomial term by term and group terms according to the differentiated coordinate. For a fixed bias with $|\mu_a|<1$, set $\xi_a(z_a)=(z_a-\mu_a)/(1-\mu_a^2)$. The two one-coordinate products satisfy $((1+\mu_a z_a)/2)\xi_a(z_a)=z_a/2$. Substitution into the finite sum proves the derivative–character identity. The resulting calculus is

<!-- claim:NEW-FOR-07 -->
\[
\begin{aligned}
\frac{d}{ds}\mathcal E_{c(s)}g
 &=\sum_{a\in I}c_a'(s)\mathcal E_{c(s)}\partial_a g,\\
\partial_a^2g&=0,\qquad
\mathcal E_\mu\partial_Jg
 =\mathcal E_\mu\!\left[g\prod_{a\in J}\xi_a\right],\\
\mathcal E_\mu g
 &=\mathcal E_{\mu[a\leftarrow0]}g+\mu_a\mathcal E_\mu\partial_ag,
\qquad
|\mu_a|\le\tfrac12\ \Longrightarrow\
\mathcal E_\mu\xi_a=0,\quad|\xi_a|\le2.
\end{aligned}
\]

The identity for $J$ assumes distinct coordinates. Its proof applies the one-coordinate identity repeatedly; factors involving other coordinates are unchanged. For the last bound, the numerator of $\xi_a$ has magnitude at most $3/2$ and its denominator is at least $3/4$. Its mean is zero because the sign has mean $\mu_a$.

The source calls the polynomial extension **ext**, the one-coordinate derivative **D**, and iterated derivatives **Dl**. We use $\partial$ to avoid confusing this derivative with deterministic query complexity. The relevant proofs are **sum_bw**, **abs_ext_le**, **hasDerivAt_ext**, **D_D**, **abs_D_le**, **ext_D_eq_mul_xi**, and **ext_affine** in ForrelationLower/Cube.lean, together with **ext_Dl**, **xi_mean**, and **abs_xi_le** in TreeGrowth.lean. These are additional explanatory statements absent from the original corpus; their sidecar entries identify existing source evidence rather than claim new mathematics.
<!-- /passage:forr_cube -->

<a id="forr_stein"></a>
<!-- passage:forr_stein -->

### 3.8. A bounded truncation and its Gaussian integration identity

The unbounded Gaussian coordinates will become small biases through an odd smooth function. The particular functions used in the source admit direct algebraic estimates:

<!-- claim:NEW-FOR-08 -->
\[
\begin{gathered}
q(x)=\sqrt{2+x^2},\qquad
\Psi(x)=\frac1{2q(x)},\qquad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3},\\
\varphi'(x)=\frac3{q(x)^5},\qquad
\Psi'(x)=-\frac{x}{2q(x)^3},\qquad
\varphi(x)=x\Psi(x)-\Psi'(x),\\
\varphi(-x)=-\varphi(x),\qquad
|\varphi(x)|\le\tfrac12,\qquad 0<\Psi(x)\le1,\qquad
0<\varphi'(x)\le3.
\end{gathered}
\]

The derivative formulas follow from differentiating $q^2=2+x^2$ and the product and quotient rules; $q>0$ everywhere. To verify the less immediate half bound, square the proposed inequality. Both sides are nonnegative, and the difference between $q(x)^6=(2+x^2)^3$ and $x^2(3+x^2)^2$ is $8+3x^2\ge0$. Oddness follows from the evenness of $q$. The coarser bounds on $\Psi$ and $\varphi'$ use $q\ge1$; these are the constants actually used in the formal advantage estimate.

Let $\gamma(x)=(2\pi)^{-1/2}e^{-x^2/2}$. Since $\gamma'=-x\gamma$, the preceding relation gives $(\Psi\gamma)'=-\varphi\gamma$. For a continuously differentiable $G$ with both $G$ and $G'$ bounded, integrate the derivative of $\Psi G\gamma$ over $[-R,R]$. The boundary values tend to zero: $\Psi G$ is bounded and $\gamma(\pm R)\to0$. All terms in the derivative are absolutely integrable, since the bounded factors multiply the probability density. Letting $R\to\infty$ proves

<!-- claim:NEW-FOR-09 -->
\[
\mathbb E[\varphi(U)G(U)]
=\mathbb E[\Psi(U)G'(U)],
\qquad U\sim N(0,1).
\]

For several independent Gaussian coordinates, hold all but one fixed and apply this identity to the remaining coordinate. A uniform bound on the function and coordinate derivative permits integrating over the other coordinates: the absolute integrals are finite, so iterated integration agrees with the joint integral. This is precisely the form used in each walk step.

We also need two elementary Gaussian facts. If $e$ is a unit vector, the map $R_e(u)=u-2\langle e,u\rangle e$ is an orthogonal reflection. Direct expansion gives $\|R_eu\|^2=\|u\|^2$ and $R_e^2=I$. Its Jacobian has absolute determinant one. The product Gaussian density depends only on $\|u\|^2$, so change of variables preserves the Gaussian integral. Further, independence and symmetry give $\mathbb E U_iU_j=0$ for $i\ne j$ and $\mathbb E U_i^2=1$, whence $\mathbb E\langle e,U\rangle^2=\sum_i e_i^2=1$. The variance identity follows equally from one-variable integration by parts: $\int x^2\gamma(x)\,dx=-\int x\gamma'(x)\,dx=\int\gamma(x)\,dx=1$, with $x\gamma(x)\to0$ at both ends.

<!-- claim:NEW-FOR-10 -->
\[
\mathbb E F(R_eU)=\mathbb E F(U)\quad(\|e\|_2=1),
\qquad
\mathbb E\langle e,U\rangle^2=1.
\]

The first equality applies whenever its integrals are defined, in particular to the bounded continuous functions used here. ForrelationLower/Stein.lean proves the displayed formulas as **hasDerivAt_phiS**, **abs_phiS_le**, **stein_one**, **stein_pi**, **integral_reflect**, and **integral_dot_sq**, using the source names **qf**, **psiS**, **phiS**, and **dphi**. The Gaussian integration identity is an instance of the integration-by-parts method used in the Forrelation literature [BS21, Section 4](https://arxiv.org/abs/2008.07003). The particular algebraic truncation and the first-block interpolation below belong to the supplied argument; this attribution does not assert that no earlier equivalent construction exists.
<!-- /passage:forr_stein -->

<a id="forr_distribution"></a>
<!-- passage:forr_distribution -->

### 3.9. The hard measure and why its initial endpoint is uniform

Write $\ell=k-1$. Draw independent standard Gaussian vectors $U_0,\ldots,U_{\ell-1}\in\mathbb R^m$, and put $V_j=HU_j$, $X_j(a)=\varphi(U_j(a))$, $Y_j(a)=\varphi(V_j(a))$. For $0\le s\le1$, form a bias for every input coordinate by

<!-- claim:NEW-FOR-11 -->
\[
w_s(r,a)=
\begin{cases}
sX_0(a),&r=0,\\
Y_{r-1}(a)X_r(a),&1\le r<\ell,\\
Y_{\ell-1}(a),&r=\ell.
\end{cases}
\qquad
h_g(s)=\mathbb E_U\mathcal E_{w_s(U)}g.
\]

Here $|w_s(r,a)|\le1/2$, including the endpoint blocks; middle blocks even have magnitude at most $1/4$. Conditional on the Gaussians, sample the signs independently with these means. Averaging this conditional law gives a probability measure on the finite cube. Call its endpoint at $s=1$ the hard distribution $\nu_1$. Positivity and total mass one follow from the finite product-weight calculation and expectation. The same construction at $s=0$ gives $\nu_0$.

We prove that $\nu_0$ is exactly uniform. Its block zero is already unbiased. Suppose that blocks below $r$ have been set to zero and that some coordinates of block $r$ have also been cleared. For an uncleared coordinate $a$ of that block, reflect $U_{r-1}$ across the row vector $H_{a,*}$. This vector has length one. Its inner product with $U_{r-1}$ is $V_{r-1}(a)$, and row orthogonality implies that the reflection changes $V_{r-1}(a)$ to its negative while leaving every $V_{r-1}(b)$, $b\ne a$, unchanged. The reflection may change every coordinate of $X_{r-1}$, but these appear only in block $r-1$, whose biases were already cleared. No other block is affected.

Oddness of $\varphi$ therefore negates exactly the current bias $w(r,a)$ among uncleared coordinates. Gaussian invariance says the average of the extension is unchanged. For each fixed collection of its other biases, the extension is affine in this bias. Averaging its values at opposite biases gives its value at zero. We have cleared coordinate $(r,a)$ without changing the Gaussian expectation. Iterate over the finite set of coordinates in block $r$, then over $r=1,\ldots,\ell$. At the end every bias is zero, so

<!-- claim:NEW-FOR-12 -->
\[
h_g(0)=\mathcal E_0g=\mathbb E_{\mathrm{unif}}g.
\]

This argument uses reflection and affine cancellation; it does not assume that $U_j$ and $HU_j$ are independent. Their dependence is the feature producing Forrelation. ForrelationLower/Cascade.lean encodes partial clearing with **mw**, the reflections with **Rf**, the one-coordinate step with **integral_mw_insert**, and the endpoint equality with **integral_ext_wv_zero**. The biases and their bounds are **wv** and **abs_wv_le_half** in Walk.lean.
<!-- /passage:forr_distribution -->

<a id="forr_identity"></a>
<!-- passage:forr_identity -->

### 3.10. The Stein elimination identity, one block at a time

Differentiate $h_g(s)$. Only block zero changes with $s$, so the cube chain rule gives $h_g'(s)=\sum_a\mathbb E[X_0(a)\mathcal E_{w_s}\partial_{(0,a)}g]$. This differentiation under the Gaussian expectation requires justification. The finite-cube extension and all its discrete derivatives are uniformly bounded on the unit bias cube by the maximum of $|g|$. The coordinates $X,Y,\Psi,\varphi'$ are bounded. On a fixed neighborhood of $[0,1]$, the extension is a finite polynomial in bounded biases, and its derivative is bounded by a constant depending only on $g,k,m$. The difference quotients converge pointwise and are dominated by that constant through the one-variable mean value theorem. Dominated convergence therefore gives the derivative formula.

Apply the coordinate Stein identity in $U_0(a)$ to the $a$th summand. That Gaussian coordinate affects bias $(0,a)$ through $X_0(a)$ and each bias $(1,b)$ through $Y_0(b)$. Differentiating through $(0,a)$ creates $\partial_{(0,a)}^2g=0$, so it contributes nothing. Differentiating through $(1,b)$ produces $H_{b,a}\varphi'(V_0(b))X_1(b)$ and a new cube derivative at $(1,b)$. Stein supplies the factor $\Psi(U_0(a))$. When $\ell=1$, the convention is $X_1=1$ because block one is the last block.

For the general step, suppose indices $a_0,\ldots,a_j$ have been selected and the current term contains $X_j(a_j)\mathcal E_{w_s}\partial_{(0,a_0)}\cdots\partial_{(j,a_j)}g$. Every previously produced weight depends only on $U_0,\ldots,U_{j-1}$. Consequently differentiating with respect to $U_j(a_j)$ leaves that weight unchanged. Its effect on bias $(j,a_j)$ is again killed by the repeated discrete derivative. Its effect on each $(j+1,b)$ gives $H_{b,a_j}\varphi'(V_j(b))X_{j+1}(b)$. This produces exactly one additional block index. At $j=\ell-1$ there is no further $X$ factor to eliminate, and the iteration stops.

All applications of Stein satisfy its boundedness hypotheses: the current function is a product of finitely many bounded smooth weights and a finite polynomial extension; its relevant coordinate derivative is a finite sum of products of the same kind. For a path $p=(p_0,\ldots,p_\ell)$ define $\partial_pg=\partial_{(0,p_0)}\cdots\partial_{(\ell,p_\ell)}g$. The usual real mean value theorem applied to $h_g$ now supplies a common parameter $s_*\in(0,1)$ such that

<!-- claim:NEW-FOR-13 -->
\[
\begin{aligned}
\mathbb E_{\nu_1}g-\mathbb E_{\mathrm{unif}}g
={}&\sum_{p\in[m]^k}
\left(\prod_{j=0}^{\ell-1}H_{p_{j+1},p_j}\right)\\
&\quad\cdot\mathbb E_U\left[
\left(\prod_{j=0}^{\ell-1}
\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))\right)
\mathcal E_{w_{s_*}(U)}\partial_pg
\right].
\end{aligned}
\]

The parameter may depend on $g$. The identity is exact, not an approximation. Its common biased derivative evaluation is essential: the path weights may have different signs, but every derivative is evaluated at the same bias before applying a bound uniform in that bias.

ForrelationLower/Walk.lean proves the local derivative calculation in **sum_dw_eq**, its repeated integration in **integral_walk**, and the common-parameter statement in **exists_identity**. The recursively nested expression **Int** is expanded into the paths by **Int_eq_paths** in Walk.lean. The source uses the mean-value form written here. The review document also writes an integral over $s$; that follows from additional integration of the derivative formula, but is unnecessary for the formal route reconstructed here.

Only a derivative of order $k$ appears in this identity. This does not restrict $g$ to its degree-$k$ Fourier part. If $g(z)=\sum_S\widehat g(S)\prod_{a\in S}z_a$, then $\mathcal E_\mu\partial_Jg=\sum_{S\supseteq J}\widehat g(S)\prod_{a\in S\setminus J}\mu_a$. Thus arbitrary higher uniform degrees occur in the same derivative evaluated at a nonzero bias. The next argument must, and will, be uniform over all these biases.
<!-- /passage:forr_identity -->

<a id="forr_tree_growth"></a>
<!-- passage:forr_tree_growth -->

### 3.11. Biased derivative growth for finite decision trees

Let $n=|I|\ge1$, let $T$ be a deterministic decision tree of depth at most $d\ge1$, and let $g(z)=v(T(z))$ with $|v(0)|,|v(1)|\le1$. Fix biases $|\mu_a|\le1/2$. We prove a bound on the sum of its absolute order-$r$ biased derivatives. The proof tracks the set of already queried coordinates, so it applies even if the tree queries the same coordinate repeatedly.

Temporarily allow any independent centered variables $\xi_a$ bounded by a common $B>0$; eventually these will be the derivative characters above with $B=2$. For coefficients $|c(J)|\le1$ and queried-coordinate set $Q$, write

<!-- claim:NEW-FOR-14 -->
\[
A_{r,c}(Q,z)=\sum_{\substack{J\subseteq Q\\|J|=r}}
c(J)\prod_{a\in J}\xi_a(z_a).
\]

If a fresh coordinate $q\notin Q$ is queried, split the new subsets according to whether they contain $q$. The change in $A_{r+1,c}$ is $\xi_q A_{r,c^q}(Q,z)$, where $c^q(J)=c(J\cup\{q\})$. A repeated query makes no change. Conditional on the answers so far, a fresh coordinate retains its original law and hence its centeredness and bound.

Here is why adaptivity does not invalidate that assertion or the later leaf calculation. For any fixed root-to-leaf path, reaching the leaf imposes exactly the listed values of its queried coordinates. Every full assignment satisfying those values follows that path, by induction through the tree. Thus its event is a cylinder on those coordinates; under a product law all other coordinates retain their independent distributions. Given the leaf, a monomial involving an unqueried centered coordinate averages to zero. The conditional expectation of the full-coordinate expression $A_{r,c}(I,z)$ is therefore its restriction to the leaf's queried set $Q$. Since $g$ is constant at that leaf,
$\mathbb E_\mu[g A_{r,c}(I,z)]$ equals the average of $v(T(z))A_{r,c}(Q,z)$ at the leaves. This is the leaf-weight identity used to convert a stopping estimate into a Fourier bound.


One can express the preceding conditional-expectation argument entirely as a finite recursion. A state consists of a set $Q$ of known coordinates and an assignment $x$ containing their answers; values of $x$ outside $Q$ are immaterial. Let $\operatorname{merge}(Q,x,z)$ use $x$ on $Q$ and $z$ on its complement. For a terminal function $F$ of a tree's output, known set, and assignment, define its walk average recursively. At a leaf with value $b$, use $F(b,Q,x)$. At a query $a\in Q$, follow the child indexed by the already known answer $x_a$. At a fresh query, average the two children with weights $(1+\mu_a)/2$ and $(1-\mu_a)/2$, inserting $a$ into $Q$ and writing its new answer into $x$. A depth induction proves that this recursion is the product expectation of the terminal quantity obtained by running the tree on $\operatorname{merge}(Q,x,z)$.

For the fresh-query induction step, split the product sum over the two values of $z_a$. The remaining factors of its weight do not involve $z_a$, so the split gives exactly the two child weights. For a known query the merged assignment has fixed answer $x_a$, giving the single-child rule. At a leaf the terminal function sees no additional queries, giving the base case. This argument also proves that the recursion's weights are nonnegative and sum to one whenever $|\mu_a|\le1$.

Equivalently, the weight of a reachable leaf is the product of its one-coordinate answer probabilities over its distinct queried coordinates. Repeated queries contribute no extra probability factor because their answers are fixed by the earlier query. A zero-probability leaf contributes nothing, and the finite recursion remains valid without division by its probability. Thus the proof does not require conditioning on null events.

<!-- claim:NEW-FOR-27 -->
\[
\mathcal E_\mu[gA_{r,c}(I,z)]
=\sum_{\lambda\ {\rm leaf}}
w_\mu(\lambda)\,v(b_\lambda)
A_{r,c}(Q_\lambda,x_\lambda),
\qquad
\sum_\lambda w_\mu(\lambda)=1.
\]

To check the displayed equality directly, fix a leaf $\lambda$. Its cylinder event supplies its product weight $w_\mu(\lambda)$. Expand the full chaos and average each monomial over the unqueried coordinates. If its subset is contained in $Q_\lambda$, its product is already fixed and equals the corresponding term on the right. Otherwise choose one unqueried coordinate in it; its centered factor has mean zero, and independence factors it from the rest, killing that term. Sum over subsets and then leaves. This proves the exact identity used before applying any absolute values or probability estimates. In the source, **merge**, **ext_prod_merge**, **walk_eq_ext**, and **walk_chaos** provide these finite equalities. The stopping function **hit** uses the same recursion with value one when its target event has already occurred and with continued averaging otherwise.

We next prove the elementary exponential estimate underlying the stopping argument. If a centered two-valued random variable $\xi$ lies in $[-B,B]$, convexity gives
$e^{a\xi}\le\frac{B-\xi}{2B}e^{-aB}+\frac{B+\xi}{2B}e^{aB}$.
Taking its expectation gives $\cosh(aB)$. Comparing power series, $(2j)!\ge2^j j!$, so $\cosh x\le e^{x^2/2}$. Thus

<!-- claim:NEW-FOR-15 -->
\[
\mathbb E e^{a\xi}\le e^{a^2B^2/2}
\quad\text{whenever }\mathbb E\xi=0,\ |\xi|\le B.
\]

Consider now a process $Y$ along the tree that starts at zero and changes at a fresh query by $\xi_q C_q$, where $C_q$ is determined by the past. Stop immediately before taking a step whose coefficient has magnitude greater than $\beta$, and also stop when $Y$ exceeds a positive level $R$. Before either stopping event, the preceding estimate gives
$\mathbb E[e^{\lambda(Y_{j+1}-Y_j)}\mid\text{past}]\le
e^{\lambda^2\beta^2B^2/2}$ for $\lambda\ge0$.
Repeated queries have zero increment and satisfy this bound as well. Pad shorter paths with zero increments to length $d$.

For an explicit finite proof, multiply at step $j$ by the factor $e^{-\lambda^2\beta^2B^2/2}$ when a step is taken and by one after stopping. Conditional expectation never increases the product. Induction over at most $d$ steps bounds its final expectation by one. On paths that first cross $R$ before a bad coefficient, the product is at least $e^{\lambda R-\lambda^2\beta^2B^2d/2}$. Its expectation is therefore at least that quantity times the crossing probability. This proves the required hitting estimate, without invoking an optional-stopping theorem at an unbounded time:

<!-- claim:NEW-FOR-16 -->
\[
\Pr[\text{$Y$ ever exceeds $R$}]
\le e^{-\lambda R+\lambda^2\beta^2B^2d/2}
+\Pr[\text{some queried coefficient has magnitude $>\beta$}].
\]

A coefficient can be declared bad whenever any possible fresh-query coefficient at the current state exceeds $\beta$. That larger bad event is what the induction below bounds. Crossing and coefficient failure at the same state is included in the bad event, so the displayed inequality covers that case too.

Choose positive $K,\Lambda$ with $K^2=2dB^2\Lambda$. We prove by induction on $r$ that the probability of ever seeing $|A_{r,c}|>K^r$ is at most $(4n)^r e^{-\Lambda}$. At $r=0$, $A_{0,c}=c(\varnothing)$ has absolute value at most one, so the event is empty. For $r+1$, the fresh-query coefficient is an order-$r$ expression for one of the $n$ coefficient arrays $c^q$, each still bounded by one. The induction hypothesis and a union bound give failure probability at most $n(4n)^r e^{-\Lambda}$. Apply the hitting estimate to $A_{r+1,c}$ and its negative with $\beta=K^r$, $R=K^{r+1}$, and $\lambda=K/(\beta B^2d)$. The exponent is $-K^2/(2B^2d)=-\Lambda$. The two estimates together are at most $2e^{-\Lambda}+2n(4n)^r e^{-\Lambda}\le(4n)^{r+1}e^{-\Lambda}$, using $n\ge1$.

At every leaf a crude deterministic bound is $|A_{r,c}|\le(nB)^r$: there are at most $n^r$ subsets and each term has magnitude at most $B^r$. On the event without a threshold crossing use $K^r$; on its complement use the crude bound. The leaf-weight identity and $|v|\le1$ now give

<!-- claim:NEW-FOR-17 -->
\[
\begin{aligned}
\Pr[\exists\text{ visited state}:|A_{r,c}|>K^r]
&\le(4n)^r e^{-\Lambda},\\
\left|\mathbb E_\mu[gA_{r,c}(I,z)]\right|
&\le K^r+(nB)^r(4n)^r e^{-\Lambda}.
\end{aligned}
\]

To extract the derivative sum, take $c(J)$ to be the sign of $\mathcal E_\mu\partial_Jg$ for the desired distinct size-$r$ subsets, and zero for all others. The derivative–character identity converts the left side into the sum of absolute derivatives. The arrays need not include all size-$r$ subsets. A family of lists is also permitted provided that every list has length $r$, contains no repeated coordinate, and different lists represent different subsets.

Now set $B=2$ and $\Lambda=2r\ln(4n)$ for $r\ge1$. Then $K^2=16rd\ln(4n)$ and the residual term is
$(2n)^r(4n)^r/(4n)^{2r}=2^{-r}\le1$. We obtain

<!-- claim:NEW-FOR-18 -->
\[
\sum_{J\in\mathcal J}|\mathcal E_\mu\partial_Jg|
\le \bigl(16rd\ln(4n)\bigr)^{r/2}+1
\]
for every family $\mathcal J$ of distinct size-$r$ subsets.

The source implements the same finite branching calculation as **walk**, **walk_eq_ext**, **walk_chaos**, **hit**, **hit_azuma**, **hit_chaos_le**, **abs_ext_tree_chaos_le**, and **sum_abs_ext_Dl_le** in ForrelationLower/TreeGrowth.lean. Its final theorem retains the parameters $K,\Lambda$ and the residual term. The simplified display is a proved mathematical specialization; no separately named source theorem has exactly this compact statement.

The proof mechanism has identifiable prior art. Girish, Tal, and Wu use martingales along decision-tree paths, smaller-degree contractions to bound increments, stopping, and union bounds [GTW21, Section 1.3, Lemma 1.9](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.39). The present reconstruction writes that mechanism directly for the bounded centered variables supplied by a biased product measure. Bansal and Sinha instead transfer uniform Fourier bounds to biased measures using random restrictions [BS21, Theorem 3.4 and Section 5.3](https://arxiv.org/abs/2008.07003). Their derivative normalization and the orthonormal biased Fourier normalization differ by products of $\sqrt{1-\mu_a^2}$, which are uniformly controlled for $|\mu_a|\le1/2$. Sharper decision-tree Fourier bounds appear in Sherstov, Storozhenko, and Wu [SSW23](https://arxiv.org/abs/2008.10223); no sharp Fourier estimate is required in the argument above.
<!-- /passage:forr_tree_growth -->

<a id="forr_advantage"></a>
<!-- passage:forr_advantage -->

### 3.12. A depth bound makes the two measures indistinguishable

Return to the path identity. Each path chooses exactly one coordinate from each of the $k$ blocks. Its list has no repeated coordinate; two paths define the same set only if their entries agree block by block. We may therefore apply the derivative bound with $r=k$, $n=km$, and this path family.

The product of the absolute matrix entries is $m^{-(k-1)/2}$. The remaining analytic weights have absolute value at most $3^{k-1}$, because $\Psi\le1$ and $\varphi'\le3$. After the triangle inequality, put the finite path sum inside the Gaussian expectation. Every bias there has coordinates of magnitude at most $1/2$, so the uniform derivative estimate applies pointwise. The Gaussian average of its constant bound is itself. Thus every depth-$d$ tree with output magnitude at most one satisfies

<!-- claim:NEW-FOR-19 -->
\[
\left|\mathbb E_{\nu_1}g-\mathbb E_{\mathrm{unif}}g\right|
\le
\left(\frac3{\sqrt m}\right)^{k-1}
\left[\bigl(16kd\ln(4km)\bigr)^{k/2}+1\right]
=:A_{k,m}(d).
\]

The same estimate holds for any mixture of such trees. Indeed, its expectation difference is the weighted sum of the differences of the individual trees; nonnegative weights summing to one and the triangle inequality preserve the bound. In particular it applies to randomized acceptance probabilities.

ForrelationLower/Cascade.lean proves the distinctness conditions in **Lpath_nodup** and **Lpath_inj**, then proves **advantage_le**. That theorem permits any row-orthogonal matrix whose entries have magnitude at most a parameter $\varepsilon$ and replaces $3/\sqrt m$ by $3\varepsilon$. As with the growth bound, the source keeps $K,\Lambda$ explicit. The displayed Walsh specialization follows by substitution and the residual calculation already shown. The blueprint's stronger analytic constants would change the numerical factor; we retain the actual coarse constants used by the source theorem.
<!-- /passage:forr_advantage -->

<a id="forr_moments"></a>
<!-- passage:forr_moments -->

### 3.13. The two moments needed to make the promise useful

The uniform second moment follows directly from the path expansion of $\Phi$. Under uniform independent signs, a nonempty sign monomial has mean zero: averaging any coordinate appearing once cancels it. Every Forrelation path uses one coordinate from each block, so its mean is zero. Two different paths disagree in some block. In their product, at least one coordinate then appears exactly once, and the mixed expectation is zero. A path multiplied by itself contributes one. There are $m^k$ paths and each squared coefficient is $m^{-(k+1)}$. Hence

<!-- claim:NEW-FOR-20 -->
\[
\mathbb E_{\mathrm{unif}}\Phi=0,\qquad
\mathbb E_{\mathrm{unif}}\Phi^2=\frac1m.
\]

To lower-bound the hard mean, first derive a quantitative positive bound on the analytic weights. The elementary inequality $e^a\ge1+a$, applied to $a=(x^2-1)/3$, gives $2+x^2\le3e^{(x^2-1)/3}$. Taking positive square roots and using the explicit formulas for $\Psi,\varphi'$ gives

<!-- claim:NEW-FOR-21 -->
\[
\begin{aligned}
q(x)&\le\sqrt3\,e^{(x^2-1)/6},\\
\Psi(x)\varphi'(y)
&\ge\frac1{18}
\exp\!\left[-\frac{x^2-1}{6}-\frac56(y^2-1)\right].
\end{aligned}
\]

For each path $p$, set $T_p=\sum_{j<\ell}[(U_j(p_j)^2-1)/6+(5/6)(V_j(p_{j+1})^2-1)]$. Each selected $U$ coordinate has variance one, and each selected $V$ coordinate is a unit row's linear form in a Gaussian vector, so it also has variance one. Therefore $\mathbb E T_p=0$. Multiplying the preceding positive inequalities gives a lower bound $18^{-\ell}e^{-T_p}$ for the path weight. The pointwise inequality $e^{-T_p}\ge1-T_p$ gives its expectation at least one. Integrability is harmless: every summand of $T_p$ is bounded below by $-1$, so $e^{-T_p}\le e^\ell$, while $T_p$ itself has finite absolute expectation.

Apply the exact Stein path identity to $g=\Phi$. A path derivative removes all $k$ sign factors in precisely that path; every other monomial misses at least one of those coordinates and is killed. Thus $\partial_p\Phi=m^{-1}\prod_{j<\ell}H_{p_j,p_{j+1}}$, a constant. Symmetry of $H$ makes its product with the matrix coefficient in the walk equal to $m^{-1}\prod H_{p_j,p_{j+1}}^2=m^{-k}$. All contributions are nonnegative. Their analytic expectations are at least $18^{-\ell}$, and there are $m^k$ paths. The uniform mean vanishes, giving

<!-- claim:NEW-FOR-22 -->
\[
\mathbb E_{\nu_1}\Phi\ge18^{-(k-1)}
\ge32^{-(k-1)}=32\delta.
\]

The formal source organizes this calculation as nested sums. To make that organization explicit, for an edge from $a$ to $b$ at Gaussian layer $j$, let
$\tau_{j,a,b}=(U_j(a)^2-1)/6+(5/6)(V_j(b)^2-1)$.
Let $T_{0,j,a}=0$ and recursively set
$T_{e+1,j,a}=m^{-1}\sum_b(\tau_{j,a,b}+T_{e,j+1,b})$.
The nonnegative nested weight starts at $Y_{0,j,a}=1$ and recurs as
$Y_{e+1,j,a}=\sqrt m^{-1}\sum_b\Psi(U_j(a))\varphi'(V_j(b))Y_{e,j+1,b}$.
Inductively it is at least $(\sqrt m/18)^e e^{-T_{e,j,a}}$. At the induction step, apply the edge inequality and the finite exponential inequality
$m^{-1}\sum_b e^{-v_b}\ge e^{-\overline v}$, where $\overline v=m^{-1}\sum_bv_b$.
To prove the latter, apply $e^x\ge1+x$ to each $x=-(v_b-\overline v)$ and average. The mean of every $T_{e,j,a}$ is zero, by the variance identities and induction. Therefore its exponential average is at least one. The final sum over $a$ divided by $M=m(\sqrt m)^\ell$ gives the same hard mean. This is the source's **Yy_ge**, **integral_TT**, and **mass_ge** argument, with the outer paths expanded in the preceding paragraph.

The uniform moment is proved in the source by recursively peeling a sign layer in **ext_lin_zero**, **ext_lin_sq_zero**, and **ext_Rs_sq**, culminating in **ext_PhiF_zero** and **ext_PhiF_sq**. The path proof is the expanded version of that orthogonality calculation. The identity **Phi_eq_PhiF** identifies its nested numerator with the frozen Forrelation function. The tangent bound is **qf_le_exp** and **psi_dphi_ge**. All these declarations are in ForrelationLower/Promise.lean.
<!-- /passage:forr_moments -->

<a id="forr_amplification"></a>
<!-- passage:forr_amplification -->

### 3.14. Amplification is needed because the distributions include unpromised inputs

Suppose a randomized algorithm of depth at most $L$ computes $P$ with error at most $1/3$ on its domain. Repeat it independently $2\tau$ times and take majority, breaking ties in any fixed way. On a promised input, an incorrect majority implies at least $\tau$ incorrect trials. If $E_i$ is the error indicator of trial $i$, then $\mathbb E2^{E_i}=1+\Pr[E_i=1]\le4/3$. Independence and Markov's inequality yield
$\Pr[\sum E_i\ge\tau]\le2^{-\tau}(4/3)^{2\tau}=(8/9)^\tau$.
The depth of each resulting tree is at most $2\tau L$. This proof uses precisely $2\tau$ runs, matching the Lean source.

<!-- claim:NEW-FOR-23 -->
\[
R_{1/3}(P)\le L
\ \Longrightarrow\
\text{there is an acceptance function }a
\text{ of depth }\le2\tau L
\text{ with promise error }\varepsilon=(8/9)^\tau.
\]

A randomized algorithm is a finite mixture of trees after its finite query histories and deterministic responses are collected. Equivalently, one can start with the finite-mixture model in the packet. Independent repetition takes the product of its mixing weights, which still sum to one. The combined tree runs its component trees sequentially, retaining their outcomes. This gives the depth and error statements without changing the worst-case query convention.

The hard measure need not be supported on yes inputs, and uniform measure need not be supported on no inputs. We therefore use inequalities valid at every point of the whole cube. If $\Phi\ge\delta$, correctness gives $a\ge1-\varepsilon$, and $\Phi-\delta\le1$; if $\Phi<\delta$, the expression $(1-\varepsilon)(\Phi-\delta)$ is nonpositive. Similarly, if $|\Phi|\le\delta/2$, correctness gives $a\le\varepsilon$; otherwise $4\Phi^2/\delta^2>1\ge a$. Consequently

<!-- claim:NEW-FOR-24 -->
\[
(1-\varepsilon)(\Phi-\delta)\le a
\le\varepsilon+\frac{4\Phi^2}{\delta^2},
\quad
\begin{cases}
\mathbb E_{\nu_1}a\ge(1-\varepsilon)(18^{-(k-1)}-\delta),\\
\mathbb E_{\mathrm{unif}}a\le\varepsilon+\dfrac4{\delta^2m}.
\end{cases}
\]

Choose $\tau$ so that $\varepsilon<\delta$. Such an integer exists because $(8/9)^\tau$ decreases to zero; explicitly any integer greater than $\ln(1/\delta)/\ln(9/8)$ suffices. Then $\varepsilon<1/2$ and the hard expectation is greater than or equal to $(1/2)\cdot31\delta$. If $m$ is large enough that $4/(\delta^2m)\le\delta$ and the tree advantage is at most $\delta$, the uniform expectation is at most $2\delta$ and the hard expectation at most $3\delta$. This contradicts the lower bound $31\delta/2$.

For a completely exact test of the needed constants, the contradiction applies whenever
$\varepsilon+4/(\delta^2m)+A_{k,m}(2\tau L+1)
<(1-\varepsilon)(18^{-(k-1)}-\delta)$.
The extra one in the depth parameter ensures positivity for the growth lemma even if $L=0$. ForrelationLower/Amplify.lean proves **exists_amplified** using the explicit sequential tree **runAll** and the majority-error implication **maj_wrong**. ForrelationLower/Main.lean packages the all-input inequalities and the expectation gap in **not_RLe_of_gap**. This is the point where treating $P$ as a total function or silently assuming promise support would invalidate a proof; the two pointwise inequalities avoid both errors.
<!-- /passage:forr_amplification -->

<a id="forr_threshold"></a>
<!-- passage:forr_threshold -->

### 3.15. Closing the bound for every sufficiently large power of four

We finish by proving the required estimates with an explicit sufficient threshold. Fix $k\ge2$, let $\ell=k-1$, keep the chosen $\tau$, and put $m=4^t$. Write $X=m^{1-1/k}/(2t)^2$, so $L=\lfloor X\rfloor$. For $t\ge8$, $X\ge1$. Indeed $1-1/k\ge1/2$, so the numerator is at least $2^t$, while $4t^2\le2^t$. The latter holds with equality at $t=8$ and persists by induction because $(t+1)^2\le2t^2$ for $t\ge3$. It follows that $d=2\tau L+1\le(2\tau+1)X$.

All logarithms in the analytic estimates in this proof are natural. Since
$\ln(4km)=\ln(4k)+2t\ln2\le(\ln(4k)+2)t$ for $t\ge1$, define
$C=16k(2\tau+1)(\ln(4k)+2)$.
Set $\Lambda=2k\ln(4km)$ and take the positive $K$ satisfying $K^2=16kd\ln(4km)$. Then $K^2\le CXt$. Raising $X$ to the integer power $k$ gives $X^k=m^{k-1}/(2t)^{2k}$; this exact cancellation is why the exponent of $m$ in $L$ has its particular value.

The square of the leading advantage term is at most
$9^\ell m^{-\ell}(CXt)^k=9^\ell(C/(4t))^k$.
The residual term is at most $3^\ell2^{-t}$, since $\ell\ge1$. To make both small, set $\eta_0=\min\{1,\delta^2/(4\cdot9^\ell)\}$ and choose

<!-- claim:NEW-FOR-25 -->
\[
t_0=\max\!\left\{
8,\
\left\lceil\frac{C}{\eta_0}\right\rceil,\
\left\lceil\frac{2\cdot3^\ell}{\delta}\right\rceil,\
\left\lceil\frac4{\delta^3}\right\rceil
\right\}.
\]

For every $t\ge t_0$, $C/t\le\eta_0\le1$, so the squared leading term is at most $9^\ell\eta_0^k\le9^\ell\eta_0\le\delta^2/4$. Its unsquared value is therefore at most $\delta/2$. The elementary inequality $2^t\ge t$ gives residual at most $3^\ell/t\le\delta/2$. Also $m=4^t\ge t\ge4/\delta^3$, so $4/(\delta^2m)\le\delta$. We have now checked every hypothesis of the preceding contradiction for every $t\ge t_0$, rather than for a selected subsequence.

<!-- claim:lem-2.1.i -->
\[
\forall k\ge2\ \exists t_0\ \forall t\ge t_0,\qquad
R(P_{k,4^t})>
\left\lfloor\frac{(4^t)^{1-1/k}}{(2t)^2}\right\rfloor.
\]

To pass from “no algorithm of depth at most $L$” to the displayed strict inequality, the randomized complexity is a minimum over an inhabited set of integer budgets. Reading all $km$ bits computes any partial Boolean function on its domain, so such a budget exists. A nonempty set of natural numbers has a least element. If that element were at most $L$, its realizing algorithm would contradict what we proved. The same lower bound also ensures both promise values occur for these dimensions: if at most one value occurred, a zero-query constant output would be correct throughout the promise.

ForrelationLower/Main.lean makes the estimates in **four_sq_le_two_pow**, **Xk_facts**, **core_bound**, and **exists_threshold**, and closes them in **bansalSinhaLower : BansalSinhaLower**. The source's constants $c_1,c_2,c_3$ satisfy $c_3=C$ above. Its internal threshold has precisely these four kinds of terms. The formal endpoint has no analytic lower-bound assumption: the argument just reconstructed supplies it. The corpus reports this endpoint compared against the frozen statement and built at the pin. Neither report was rerun during the present examination.
<!-- /passage:forr_threshold -->

<a id="forr_attribution"></a>
<!-- passage:forr_attribution -->

### 3.16. What this proof uses from earlier work, and what the source establishes

The problem, its alternating Walsh expression, and its small-query quantum algorithm are established Forrelation constructions [AA18](https://arxiv.org/abs/1411.5729). Bansal and Sinha prove a stronger randomized lower bound, including quantitative dependence on advantage and on $k$, for the same small constant threshold [BS21, Theorem 1.3, Corollary 1.4](https://arxiv.org/abs/2008.07003). The strict fixed-$k$ lower bound used here is weaker by a polylogarithmic factor. It follows from that theorem by the explicit comparison above.

The internal proof shares substantial ingredients with that literature: correlated Gaussian vectors, coordinatewise truncation, randomized rounding to biased signs, polynomial extensions, Gaussian integration by parts, and a decision-tree Fourier-growth estimate. The supplied source chooses a first-block interpolation and eliminates one Gaussian coordinate at each successive block. Its uniform endpoint is proved by successive reflections. Its decision-tree estimate is a direct biased version of the martingale and contraction method explained by Girish, Tal, and Wu [GTW21, Section 1.3](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.39). Bansal–Sinha's published interpolation uses multiple Gaussian-variance parameters and bounds biased levels from $k$ through $k(k-1)$ [BS21, Theorem 3.2 and Section 5.1](https://arxiv.org/abs/2008.07003). These are concrete differences between the inspected arguments.

Sherstov, Storozhenko, and Wu prove sharp Fourier bounds and an optimal-up-to-logarithms quantum–randomized separation through orthogonal-matrix variants [SSW23](https://arxiv.org/abs/2008.10223). Tal's earlier work develops the random-orthogonal Rorrelation variant and supplies the decision-tree Fourier bound used by Bansal–Sinha [Tal20, Theorem 1.3 and Section 5.1](https://arxiv.org/abs/1912.12561). Their results explain why neither a general Fourier-growth estimate nor the nearly maximal partial-function separation should be presented here as a new theorem. The supplied argument proves exactly the fixed-$k$ proposition needed in this construction; this record does not certify stronger quantitative claims suggested in the informal review.

The packet's prior-art memorandum says it did not locate this exact first-block reflection-and-elimination route in the references it inspected. A finite literature check cannot establish historical novelty. The defensible statement is that the route differs from the displayed proofs in the primary sources checked here. The algebraic truncation, the identity, and the resulting quantitative possibilities merit an independent mathematical review before any stronger attribution claim.
<!-- /passage:forr_attribution -->

<a id="forr_bundle"></a>
<!-- passage:forr_bundle -->

### 3.17. The complete Forrelation ingredient

Combining the established bounds yields the preprint's three-part lemma.

<!-- claim:lem-2.1 -->
\[
\begin{gathered}
\text{For each fixed }k\ge2\text{ and every sufficiently large }m=4^t,\\
R(P_{k,m})>L_{k,m},\qquad
Q_\eta(P_{k,m})=O_k(1+\log(1/\eta)),\\
\text{and an exact fan-in-two circuit for domain and value has size }
O_k\!\left(m(\log_2m)^2\right).
\end{gathered}
\]

The quantum assertion includes retained workspace, arbitrary requested error $0<\eta<1/2$, and a bit output on every input. The circuit assertion includes exact domain recognition on every input. Those qualifications are used later: promise errors can be handled probabilistically, whereas a certificate that an input belongs to the promise must be checked exactly. The randomized lower bound uses the same bit-query convention and the same one-sided promise.

There is no single exact conjunction declaration attached to the row **lem-2.1** in the corpus. Its three mathematical parts have been reconstructed separately, with the evidence limitations stated at each part. Their combination in this paragraph is a mathematical conjunction of those results. It should not be relabeled as a newly replayed kernel theorem.
<!-- /passage:forr_bundle -->

<a id="forr_references"></a>
<!-- passage:forr_references -->

### 3.18. Primary references for this section

- **[AA18](https://arxiv.org/abs/1411.5729)** Scott Aaronson and Andris Ambainis, “Forrelation: A Problem that Optimally Separates Quantum from Classical Computing,” *SIAM Journal on Computing* 47(3), 982–1038, 2018. Primary preprint: https://arxiv.org/abs/1411.5729. The inspected material includes its definition and discussion of $k$-fold Forrelation; the construction predates this project.
- **[BS21](https://arxiv.org/abs/2008.07003)** Nikhil Bansal and Makrand Sinha, “$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity,” *STOC 2021*, 1303–1316, DOI 10.1145/3406325.3451040. Primary preprint: https://arxiv.org/abs/2008.07003. The original PDF's Theorem 1.3 and Corollary 1.4 are on page 4. Its Theorems 3.2 and 3.4 and Section 5.3 identify the advantage and biased-restriction machinery. The packet's Markdown extraction flattens some numbered theorem environments, so its local numbering must not replace the PDF's numbering.
- **[GTW21](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.39)** Uma Girish, Avishay Tal, and Kewen Wu, “Fourier Growth of Parity Decision Trees,” *36th Computational Complexity Conference*, LIPIcs 200, 39:1–39:36, 2021. DOI 10.4230/LIPIcs.CCC.2021.39. Official publication: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.39. Primary preprint: https://arxiv.org/abs/2103.11604. Section 1.3 and Lemma 1.9 give the ordinary decision-tree martingale argument relevant here; the paper's additional parity-query analysis is not needed.
- **[SSW23](https://arxiv.org/abs/2008.10223)** Alexander A. Sherstov, Andrey A. Storozhenko, and Pei Wu, “An Optimal Separation of Randomized and Quantum Query Complexity,” *SIAM Journal on Computing* 52(2), 525–567, 2023. DOI 10.1137/22M1468943. Primary preprint: https://arxiv.org/abs/2008.10223. The introduction and Fourier-growth results situate the prior partial-function separations and sharper bounds.
- **[Tal20](https://arxiv.org/abs/1912.12561)** Avishay Tal, “Towards Optimal Separations between Quantum and Randomized Query Complexities,” *FOCS 2020*, 228–239. Primary preprint: https://arxiv.org/abs/1912.12561. The introduction, Theorem 1.3, and Section 5.1 describe the Rorrelation construction and decision-tree Fourier growth.

The source-specific locators in this section refer to the private repository snapshot supplied in the packet, at its stated pin, not to an asserted public repository. Full declaration names and exact passages are recorded in the correspondence sidecar.
<!-- /passage:forr_references -->


## 4. Transcripts, addressed certificates, and the total function


<a id="CL-construction-context"></a>
<!-- passage:CL-construction-context -->
The total function couples two kinds of certificates. A column can certify that it contains only ones, and its selected cell can point to a zero in every other column. The selected cell is itself hidden at an address formed by values of separate inputs to the partial function. This arrangement explains both sides of the construction: a correct address gives short tests for a complete witness, while a classical algorithm that has invested little in a column has little chance of identifying its address.

There are several antecedents for these ingredients. Göös, Pitassi, and Watson use a unique all-one column and a pointer chain through one zero in each other column [GPW2018, Theorem 5 and §2.1, pp. 3–5 of the ECCC revision](https://eccc.weizmann.ac.il/report/2015/050/). Ambainis, Balodis, Belovs, Lee, Santha, and Smotrovs discuss direct pointers from a distinguished element to a zero in each other column, as well as balanced pointer trees [ABBLSS2015, §1, “Use of a balanced tree”](https://arxiv.org/abs/1506.04719v3). Aaronson, Ben-David, and Kothari define certificate arrays addressed by the answers to several partial-function instances [ABK2016, §6.1, Definitions 14–15; §6.2, Lemma 17](https://arxiv.org/abs/1511.01937v2). The function below combines these ingredients with explicit Boolean circuit transcripts. These references establish the ancestry of the ingredients; the proof below establishes the properties of this particular combination.
<!-- /passage:CL-construction-context -->

<a id="CL-transcripts"></a>
<!-- passage:CL-transcripts -->
Fix a partial Boolean function $P:D\to\{0,1\}$, where $D\subseteq\{0,1\}^{n}$, and a fan-in-two Boolean circuit $C$. We require two distinguished non-input gates, with outputs denoted by $d$ and $b$, such that on every $x\in\{0,1\}^{n}$, the output $d$ equals one exactly when $x\in D$, and whenever $d=1$, the output $b$ equals $P(x)$. In the eventual application, $n=km$ and $C=C_{k,m}$ is the exact circuit constructed earlier. Until the final instantiation, the argument uses only the stated correctness property.

Number the non-input gates in a topological order, and write $S$ for their number. A transcript is a proposed value for every one of these $S$ gates, including the two output gates. Input wires have no transcript entries. Their values are read from the actual input. A predecessor of a gate can therefore be an actual input bit, an earlier transcript bit, or a fixed constant. The Lean representation uses a constant-false predecessor and an arbitrary two-input Boolean table, which also represents constants and unary gates.

For a fixed input $x$, evaluate the gates in their topological order. This defines a transcript $\operatorname{ev}_{C}(x)$. At a gate $g$, its value is the gate's Boolean function applied to the two predecessor values, so this transcript passes every gate-consistency check. Conversely, suppose a transcript passes every such check. At the first gate, its predecessor values are actual input bits or constants, so its claimed value is correct. Inductively, if all earlier gate entries are correct, both predecessors of the next gate have their actual values, and its consistency check forces its entry to be correct too. Thus a consistent transcript is uniquely determined, on every input, including inputs outside $D$.

<!-- claim:NCL-transcript-characterization -->
\[
\operatorname{GateConsistent}(C,x,\mathrm{tr})
\quad\Longleftrightarrow\quad
\mathrm{tr}=\operatorname{ev}_{C}(x).
\]

This proves the asserted meaning of a correct evaluation transcript, as well as its existence and uniqueness. The correspondence is exact for `QuarticQuery.gateConsistent_iff_eq_circuitEval`; `QuarticQuery.circuitEval_gateConsistent`, `QuarticQuery.GateConsistent.unique`, and `QuarticQuery.existsUnique_gateConsistent` supply the two directions and uniqueness separately. The transcript convention is the one in `Statement.lean`, `Gate`, `Circuit`, `predecessorValue`, and `GateConsistent`.
<!-- /passage:CL-transcripts -->

<a id="CL-layout"></a>
<!-- passage:CL-layout -->
Now let $m=4^{t}$, with $t\geq1$, and use base-two logarithms. The two address lengths are fixed by the following equalities.

<!-- claim:eq-6 -->
\[
\ell=\log_2m=2t,
\qquad
r=\lceil20\log_2m\rceil=40t.
\]

The input has $m$ columns. Column $i$ contains a string $X_i\in\{0,1\}^{m}$, strings $A_{i,1},\ldots,A_{i,r}\in\{0,1\}^{n}$, and one cell $B_{i,s}$ for each $s\in\{0,1\}^{r}$. Each cell contains one pointer into every other column and one length-$S$ transcript for every $A_{i,h}$. A pointer into column $j\ne i$ is an $\ell$-bit word encoding an element of $[m]$ by a fixed bijection. Since $m=2^{\ell}$, every pointer word has a meaning. There is no invalid pointer encoding and no promise on any part of the complete input.

The formal coordinate type `QuarticQuery.BitLoc` is the disjoint union of the $X$-coordinates, the $A$-coordinates, the pointer coordinates, and the transcript coordinates. This makes the physical bit cost explicit. In particular, consulting a pointer means querying its bits. `QuarticQuery.pointerEquiv_bijective` and `QuarticQuery.existsUnique_pointer` establish the bijection used by the layout. `QuarticQuery.logb_mValue` gives the logarithm identity; the choices $\ell=2t$ and $r=40t$ are built into `QuarticQuery.Fkm`.
<!-- /passage:CL-layout -->

<a id="CL-address-winner"></a>
<!-- passage:CL-address-winner -->
If all $A_{i,h}$ belong to $D$, define the true address of column $i$ by the following vector.

<!-- claim:eq-7 -->
\[
s_i=\bigl(P(A_{i,1}),\ldots,P(A_{i,r})\bigr)\in\{0,1\}^{r}.
\]

At an arbitrary address $s$, the outward pointer condition requires that every pointer reaches a zero in its designated other column.

<!-- claim:eq-8 -->
\[
X_j[p_{i,s,j}]=0\qquad\text{for every }j\ne i.
\]

Column $i$ is a winner if $X_i=1^m$, all $A_{i,h}$ belong to $D$, and the cell $B_{i,s_i}$ contains the correct transcripts on these strings and satisfies the outward pointer condition. We set the value of the complete input $y$ to one exactly when a winner exists.

<!-- claim:def-F -->
\[
F(y)=
\begin{cases}
1,&\text{if some column of }y\text{ is a winner},\\
0,&\text{otherwise}.
\end{cases}
\]

This is a total Boolean function. A string outside $D$ can prevent its own column from winning; it does not leave $F$ undefined. Arbitrary incorrect transcripts and arbitrary pointer words are treated in the same way, by the truth or falsity of the winner predicate. For $P=P_{k,m}$ and the chosen circuit $C_{k,m}$, this is $F_{k,m}$. `QuarticQuery.addressedF_eq_true_iff` is the exact existential characterization of the source definition. The types of `addressedF` and `Fkm` give totality. The displayed pointer condition is an explicit conjunct of `QuarticQuery.WinsAt`; the corpus assigns that row no separate theorem.
<!-- /passage:CL-address-winner -->

<a id="CL-fidelity"></a>
<!-- passage:CL-fidelity -->
There are two useful descriptions of winning at an address $s$. The semantic description requires $X_i=1^m$, $P(A_{i,h})=s_h$ for every $h$, correct transcripts in $B_{i,s}$, and the outward pointer condition. The local description replaces $P(A_{i,h})=s_h$ by the two output tests $d=1$ and $b=s_h$ in each transcript, while retaining gate consistency and the other conditions. Under the correctness property of $C$, these descriptions agree.

Indeed, a gate-consistent transcript is the true evaluation transcript. Its domain output is one exactly when $A_{i,h}\in D$; if that output is one, its value output is $P(A_{i,h})$. Thus passing both output tests gives $P(A_{i,h})=s_h$. Conversely, if $P(A_{i,h})=s_h$, the correct transcript has domain output one and value output $s_h$. Applying this argument for every $h$ proves both implications. Whenever the semantic description holds, all partial-function values are defined and their vector equals $s$, so $s=s_i$. Consequently, existence of an address satisfying the local description is precisely the paper's winner condition.

This is `claim-winner-fidelity` together with `def-win-at-address`. The source's primitive `QuarticQuery.WinsAt` is the semantic description. Therefore `QuarticQuery.winsAt_iff_paperWinsAt` needs no circuit correctness assumption: both sides already mention the values of $P$. The bridge to output tests is `QuarticQuery.winsAt_iff_outputs`, which does require `CircuitRealises C P`. Keeping these two bridges distinct prevents an incorrect circuit from being silently substituted for the intended partial function.
<!-- /passage:CL-fidelity -->

<a id="CL-unique"></a>
<!-- passage:CL-unique -->
For every complete input, at most one column is a winner. Suppose distinct columns $i$ and $j$ both won. The pointer from the selected cell of $i$ into column $j$ would exhibit a zero in $X_j$, while the winning condition for $j$ would require every bit of $X_j$ to be one. This contradiction proves `cor-unique-winner`. For a fixed column, a winning address is also unique: its $h$-th bit must equal the single value $P(A_{i,h})$ for every $h$. Hence at most one pair $(i,s)$ satisfies the winning predicate.

The source contains the exact uniqueness conclusions in `QuarticQuery.winsAt_column_unique`, `QuarticQuery.winsAt_address_unique`, and `QuarticQuery.winsAt_unique`. The corpus's empty tie for `cor-unique-winner` is a metadata omission; it does not mean that the source lacks the theorem.
<!-- /passage:CL-unique -->

<a id="CL-local-tests"></a>
<!-- passage:CL-local-tests -->
We next construct all tests in Lemma 2.2, including their indexing convention. For a fixed candidate pair $(i,s)$, use the following four families.

| Test family | Number | Passing condition | Maximum bit queries |
|---|---:|---|---:|
| Column bits | $m$ | The selected bit of $X_i$ is one. | $1$ |
| Outward pointers | $m-1$ | The selected pointer in $B_{i,s}$ reaches a zero. | $\ell+1$ |
| Gate consistency | $rS$ | A claimed gate value equals its gate function on the two predecessor values. | $3$ |
| Transcript outputs | $2r$ | The domain output is one, or the value output equals the corresponding bit of $s$. | $1$ |

The first family is indexed by $[m]$. For the second, list the columns other than $i$ in their ordinary order, skipping $i$, and index this list by $[m-1]$. For the last two families, use a pair consisting of $h\in[r]$ and either a gate index or one of the two output labels. Thus the common index set is $[m]\sqcup[m-1]\sqcup([r]\times([S]\sqcup\{d,b\}))$; its type and cardinality are independent of $(i,s)$.

<!-- claim:def-K -->
\[
K_{k,m}=m+(m-1)+r(S_{k,m}+2)=O_k\bigl(m(\log m)^3\bigr).
\]

The exact count follows by addition and multiplication of the four finite cardinalities. For the growth bound, the earlier circuit estimate gives $S_{k,m}\leq c_k m(\log_2m)^2$ for sufficiently large $m$, and $r=20\log_2m$. Substituting these bounds gives a constant multiple, depending only on $k$, of $m(\log_2m)^3$; the remaining terms are bounded by the same expression once $m\geq4$. `QuarticQuery.TestIndex`, `QuarticQuery.otherColumn_bijective`, and `QuarticQuery.card_testIndex` give the common index set and its exact cardinality. The asymptotic substitution is a prose deduction from the circuit size bound.
<!-- /passage:CL-local-tests -->

<a id="CL-local-equivalence"></a>
<!-- passage:CL-local-equivalence -->
All these tests pass exactly when column $i$ wins at address $s$. If they all pass, the first and second families give the all-one and outward pointer conditions. For each transcript, all gate tests pass, so the topological induction already proved identifies it with the true evaluation of $C$. The output tests, together with circuit correctness, then show that $A_{i,h}\in D$ and $P(A_{i,h})=s_h$. These are all the winning conditions. Conversely, a winner at $s$ has each asserted bit, each outward zero, and each true transcript. Every test therefore passes. This proves the equivalence in `lem-2.2.i`.

The query costs also hold on every input. A pointer test first reads all $\ell$ pointer bits, computes the indicated target for free, and then reads that single target bit. A gate test reads its claimed output and the at most two nonconstant predecessors. Input predecessors are read from $A_{i,h}$, and gate predecessors are read from the same stored transcript. Constants require no query. The remaining tests read one bit. Each test is therefore computed by an exact deterministic adaptive decision tree of depth at most $\max(3,\ell+1)$, which equals $\ell+1$ for $m\geq4$.

A pointer test can depend on every one of its $m$ target bits: fix its pointer to any chosen target and flipping that target flips the answer. It can also depend on each of its $\ell$ pointer bits: changing that bit changes the decoded address, and the two target bits can be assigned different values. Its support can therefore contain all $m+\ell$ coordinates. The shallow decision tree bound concerns the number read on one path. `QuarticQuery.localTestTree_eval` and `QuarticQuery.localTestTree_depth_le` verify the tree's exact output and depth, while `QuarticQuery.winsAt_iff_localTests` verifies the equivalence. These declarations collectively support Lemma 2.2(i); none alone states its entire prose conjunction.
<!-- /passage:CL-local-equivalence -->

<a id="CL-coherent-tests"></a>
<!-- passage:CL-coherent-tests -->
The same tests can be evaluated coherently with $O(\log m)$ queries, uniformly when the test index is in superposition. Here is the reversible implementation. Retain the candidate pair, test index, and query history in registers. At each level of the deterministic tree, compute the next queried location from these registers by an input-independent reversible operation. Use the bit oracle to place that input bit in a fresh answer register, and retain it while computing the next location. After at most $d=\max(3,\ell+1)$ levels, compute the test's Boolean answer into an output register. Reverse the computation to clear the history and ancillary registers. This uses at most a constant multiple of $d$ oracle calls. Branches that have already terminated can be padded by an inactive controlled query operation; such an operation can itself be implemented by loading the queried bit, conditionally using it, and unloading it, at constant query cost. All computations of locations are uniform functions of the retained registers, so the procedure acts linearly on superpositions of test indices and candidate pairs.

This proves `lem-2.2.ii`. The common index set was established before any input was queried, so its size does not depend on the candidate. The later quantum verification section supplies the formal coherent implementation represented in the corpus by `QuarticQuery.Upper.test_samples` and `QuarticQuery.Upper.search_runs`. `Construction/LocalTests.lean` itself formalizes only the classical trees; its depth theorem alone does not certify this reversible implementation. Lemma 2.2 is the conjunction of the two parts just proved.
<!-- /passage:CL-coherent-tests -->

<a id="CL-dichotomy"></a>
<!-- passage:CL-dichotomy -->
The local dichotomy follows for every input. If column $i$ wins, its true address has every test passing. If it does not win, then for each address $s$ at least one test fails: otherwise the equivalence just proved would make it a winner at $s$. A winning column has every test passing at only its true address, by address uniqueness. These conclusions are `cor-local-dichotomy`; the source contains the exact relevant statements as `QuarticQuery.exists_failing_localTest` and `QuarticQuery.localTests_iff_eq_of_winsAt`. This formulation remains valid when some $A_{i,h}$ violates the partial-function promise.
<!-- /passage:CL-dichotomy -->


## 5. Quantum evaluation on every input


<a id="upper-purpose"></a>
<!-- passage:upper-purpose -->

The quantum algorithm has two tasks. It first produces a short list of columns that is likely to contain the winning column, if there is one. It then checks the columns in that list. Both tasks must have a fixed query bound on every input, including inputs on which some of the Forrelation promises fail. This requirement determines the amplification procedure and the comparison rule below.

There are useful precedents for the three steps of generating candidates, comparing them, and checking a certificate. Ben-David and Kothari use this organization in their quantum certificate separation [BenDavidKothari2026, Lemma 5](https://arxiv.org/abs/2609.15063). Quantum minimum finding provides another example of repeatedly searching among candidates [DurrHoyer1996, Theorem 1](https://arxiv.org/abs/quant-ph/9607014). Its comparisons come from a total order. Finding a king in a fixed tournament also has a quantum algorithm using a square root number of vertices, up to logarithmic factors [MandeParaasharSaurabh2023, Theorem 4.4](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30). Here a comparison is a quantum experiment whose winning probability can be any real number in the unit interval. In particular, an input outside the Forrelation promises need not determine a reliable orientation of each edge. We therefore prove the probabilistic tournament statement needed for this setting.

The only complexity measure in this section is the number of queries to the ordinary input bit oracle. Input independent unitary gates, finite work registers, reversible arithmetic on indices, and measurements are free in this measure. Whenever a cost is first stated in calls to a subroutine, we subsequently account for its implementation with bit queries.
<!-- /passage:upper-purpose -->


### 5.1. Amplification with a fixed stopping time


<a id="upper-amplification-statement"></a>
<!-- passage:upper-amplification-statement -->

**Lemma 3.1, with the quantifiers made explicit.** For every pair of real numbers \(0<\gamma\leq 1/2\) and \(0<\eta<1/2\), there is one procedure, depending on \(\gamma,\eta\) and using a preparation \(A\) as a black box, with the following property for every unitary \(A\), every fixed input oracle, and every designated success subspace. Write \(p\) for the probability that measuring \(A|0\rangle\) in that subspace succeeds. The procedure returns either failure or a state. Every returned state is the normalized success component of \(A|0\rangle\), up to global phase. If \(p\geq\gamma\), its failure probability is at most \(\eta\). If \(p=0\), it fails with certainty. On every branch, for every \(p\in[0,1]\), it uses \(O(\gamma^{-1/2}\ln(1/\eta))\) calls to \(A\) and \(A^{-1}\). In particular, neither the procedure nor its stopping rule depends on knowing \(p\). This is corpus statement `lem-3.1`.

The distinction between a fixed bound and an expected bound matters here. Boyer, Brassard, Høyer, and Tapp analyze a random number of Grover iterations when the number of solutions is unknown [BBHT1998, Section 4, Lemma 2 and Theorem 3](https://arxiv.org/abs/quant-ph/9605034). Brassard, Høyer, Mosca, and Tapp extend the underlying two dimensional analysis to arbitrary preparation algorithms [BHMT2002, Section 2, Lemma 1 and equation (8)](https://arxiv.org/abs/quant-ph/0005055). We give the particular bounded construction in full.
<!-- /passage:upper-amplification-statement -->

<a id="upper-grover-geometry"></a>
<!-- passage:upper-grover-geometry -->

Let \(\Pi\) be the orthogonal projection onto the success subspace, let \(\psi=A|0\rangle\), and let \(p=\|\Pi\psi\|^2\). First suppose \(0<p<1\). Define \(g=\Pi\psi/\sqrt p\) and \(b=(I-\Pi)\psi/\sqrt{1-p}\). Orthogonality of the two projection ranges gives orthonormal vectors \(g,b\), and normalization of \(\psi\) gives \(\psi=\sqrt p\,g+\sqrt{1-p}\,b\). There is a unique \(\theta\in(0,\pi/2)\) such that \(\sin\theta=\sqrt p\). Its cosine is \(\sqrt{1-p}\).

The success reflection is \(S_\chi=I-2\Pi\). The reflection about the reference state is \(S_0=I-2|0\rangle\langle0|\). Choose the Grover iterate \(G=-AS_0A^{-1}S_\chi\). The minus sign is a global phase, so it has no query cost. Conjugating \(S_0\) by \(A\) gives \(I-2|\psi\rangle\langle\psi|\). Consequently \(G=(2|\psi\rangle\langle\psi|-I)S_\chi\). Both factors preserve the span of \(g,b\). On coordinates in the ordered basis \(g,b\), \(S_\chi\) changes the sign of the first coordinate. Multiplying it by the reflection about \(\psi\) gives the matrix with rows \((\cos(2\theta),\sin(2\theta))\) and \((-\sin(2\theta),\cos(2\theta))\).

Applying this matrix to a vector with coordinates \((\sin\alpha,\cos\alpha)\) gives \((\sin(\alpha+2\theta),\cos(\alpha+2\theta))\), by the addition formulas. Induction on the nonnegative integer \(\ell\), beginning at \(\alpha=\theta\), therefore proves the state and success formula in `claim-grover-state`:

<!-- claim:claim-grover-state -->
\[
G^\ell\psi
 =\sin((2\ell+1)\theta)g+\cos((2\ell+1)\theta)b,
\qquad
\Pr[\text{success after }\ell]=\sin^2((2\ell+1)\theta).
\]

Projection onto success removes the \(b\) term. Whenever success has nonzero probability, the normalized result is \(g\) or \(-g\). This conclusion concerns the whole workspace, including registers that \(A\) has used to record intermediate data. It is stronger than a statement about the probability of a success flag alone.

At \(p=0\), the state lies in the failure subspace. The success reflection leaves it unchanged, and the reflection about \(\psi\) leaves \(\psi\) unchanged. Thus every iterate has zero success probability. At \(p=1\), the success reflection sends \(\psi\) to \(-\psi\), and every iterate remains a scalar multiple of \(\psi\) in the success subspace. These cases require no definition of a normalized zero component.
<!-- /passage:upper-grover-geometry -->

<a id="upper-grover-trial"></a>
<!-- passage:upper-grover-trial -->

For `def-grover-trial`, choose the following two integers, using natural logarithms in the second expression:

<!-- claim:def-grover-trial -->
\[
M=\left\lceil\frac{10}{\sqrt\gamma}\right\rceil,
\qquad
N=\left\lceil\frac{\ln(1/\eta)}{\ln(40/31)}\right\rceil.
\]

In one trial, set \(\ell=0\) with probability \(1/2\); with the remaining probability \(1/2\), choose \(\ell\) uniformly from \(0,\ldots,M-1\). Prepare \(\psi\), apply \(G^\ell\), and measure success. Run at most \(N\) such trials on fresh initialized registers, stopping at the first success. Return failure if none succeeds. Equivalently, the probability assigned to an iteration count \(\ell<M\) is \(1/(2M)\), with an additional \(1/2\) assigned to zero. This is a finite distribution selected before any access to the input.

One preparation followed by \(\ell\) iterates uses \(2\ell+1\) calls to \(A\) or \(A^{-1}\). The reflections use no such calls. Since \(\ell<M\), the actual count in a trial is at most \(2M-1\); the formal construction uses the convenient upper bound \(2M+1\). Stopping after \(N\) trials therefore gives a syntactic cap independently of the input and of the outcomes. We have not used a success assumption to establish this cap.
<!-- /passage:upper-grover-trial -->

<a id="upper-average-exact"></a>
<!-- passage:upper-average-exact -->

The following exact identity supplies the estimate for a randomized iteration count. It is the explicit identity proved in `QuarticQuery.Amplification.average_sin_sq`; it strengthens the inequality recorded as equation (9), so we record it as `new-upper-average-exact`.

<!-- claim:new-upper-average-exact -->
\[
\frac1M\sum_{\ell=0}^{M-1}\sin^2((2\ell+1)\theta)
 =\frac12-\frac{\sin(4M\theta)}{4M\sin(2\theta)}
 \quad(M\geq1,\ \sin(2\theta)\ne0).
\]

To prove it, use \(\sin^2 u=(1-\cos(2u))/2\). The difference between \(\sin(4(\ell+1)\theta)\) and \(\sin(4\ell\theta)\) is \(2\sin(2\theta)\cos((4\ell+2)\theta)\). Summing this equality over \(\ell=0,\ldots,M-1\) cancels every interior sine term and leaves \(\sin(4M\theta)\). Dividing by the nonzero \(2\sin(2\theta)\) gives the sum of the cosine terms. Substituting into the sum of the squared sines and dividing by \(M\) proves the identity. The source also proves the identity after multiplication by \(\sin(2\theta)\), which avoids division and remains valid when that sine vanishes.
<!-- /passage:upper-average-exact -->

<a id="upper-small-probability"></a>
<!-- passage:upper-small-probability -->

Suppose now that \(\gamma\leq p\leq1/2\). The sine addition formula and the definitions of \(\theta,g,b\) give `claim-sin2theta`:

<!-- claim:claim-sin2theta -->
\[
\sin(2\theta)=2\sqrt{p(1-p)}\geq\sqrt\gamma.
\]

Indeed, \(1-p\geq1/2\), so the square of the left side is \(4p(1-p)\geq2p\geq\gamma\); both sides are nonnegative. Since \(M\geq10/\sqrt\gamma\), we obtain \(M\sin(2\theta)\geq10\). The absolute value of every sine is at most one. The exact average above therefore implies the paper's slightly weaker, and sufficient, equation (9):

<!-- claim:eq-9 -->
\[
\frac1M\sum_{\ell=0}^{M-1}\sin^2((2\ell+1)\theta)
\geq\frac12-\frac{1}{2M|\sin(2\theta)|}
\geq\frac9{20}.
\]

The half of the trial that chooses a uniform iteration count thus contributes at least \(9/40\) to its success probability. If instead \(p\geq1/2\), the half that chooses zero iterations contributes at least \(p/2\geq1/4\geq9/40\). These cases cover every \(p\geq\gamma\), including \(p=1\). A trial fails with probability at most \(31/40\) whenever the promise \(p\geq\gamma\) holds.
<!-- /passage:upper-small-probability -->

<a id="upper-amplification-proof"></a>
<!-- passage:upper-amplification-proof -->

For a fixed oracle input, each fresh trial has the same failure probability \(f\), and the fresh choices and registers make the failures independent. Hence the probability of \(N\) failures is \(f^N\leq(31/40)^N\leq\eta\). The last inequality follows by taking logarithms: \(N\ln(40/31)\geq\ln(1/\eta)\). If \(p=0\), the endpoint argument above gives \(f=1\), hence certain failure.

On a successful branch, the state in its successful trial is \(g\) up to global phase, regardless of its iteration count. Earlier failed trials occupy separate registers and can be discarded after their outcomes have been recorded. Keeping them also causes no problem: the designated output register is in the pure state \(g\) up to phase. Taking a mixture over iteration counts and over which trial first succeeded leaves the density operator \(|g\rangle\langle g|\) unchanged. Thus conditioning on success does not bias any measurement of that output state. This proves every correctness clause of Lemma 3.1.

For completeness, the source gives the following explicit version of the call bound, recorded here as `new-upper-call-cap`:

<!-- claim:new-upper-call-cap -->
\[
\operatorname{calls}(\gamma,\eta)
\leq N(2M+1)
\leq138\,\gamma^{-1/2}\ln(1/\eta).
\]

Here is the arithmetic. For \(x\geq1\), differentiating \(\ln x-2(x-1)/(x+1)\) gives \((x-1)^2/(x(x+1)^2)\geq0\), and the expression vanishes at one. At \(x=40/31\), this gives \(\ln(40/31)\geq18/71\geq1/4\). Also \(\ln2=\int_1^2u^{-1}\,du\geq1/2\). Consequently \(N\leq4\ln(1/\eta)+1\leq6\ln(1/\eta)\). Since \(M\leq10/\sqrt\gamma+1\) and \(\sqrt\gamma\leq1\), we have \(2M+1\leq23/\sqrt\gamma\). Multiplication gives 138. These estimates are deliberately uniform; there is no run that is allowed to exceed the bound because its success probability happens to be small.

**Lean evidence for amplification.** The source declarations `QuarticQuery.Amplification.Preparation.grover_rotation`, `QuarticQuery.Amplification.Preparation.phaseEq_normalised_good_iterate`, `QuarticQuery.Amplification.average_sin_sq`, `QuarticQuery.Amplification.average_sin_sq_ge_nine_twentieths`, and `QuarticQuery.Amplification.Preparation.trialFail_le` supply the geometric and probability steps. `QuarticQuery.Amplification.bounded_amplification` states the uniform procedure, the exact success-state assertion through phase-invariant observables, the failure guarantees, and the call cap. This is the corpus's exact tie for `lem-3.1`. It is a theorem about the abstract procedure type `QuarticQuery.Amplification.Proc`. The final quantum upper bound instead uses the separately compiled sampler theorem `QuarticQuery.Upper.Samples.amplify`, described below. The distinction does not weaken the argument, because those applications immediately measure the successful label. These are statements about the inspected source and the corpus's classifications; no compilation was performed for this record.
<!-- /passage:upper-amplification-proof -->


### 5.2. A tournament with probabilistic comparisons


<a id="upper-comparison-model"></a>
<!-- passage:upper-comparison-model -->

Fix an input oracle for the duration of the argument. There are \(m\geq2\) vertices. For each unordered pair of distinct vertices, use one designated coherent comparison circuit. An ordering convention determines which output bit means that the first named vertex wins. Let \(a_{ij}\) be the probability that \(i\) wins its comparison against \(j\), and define \(a_{ii}=0\). This is `def-aij`. The same circuit and opposite interpretations of its two outcomes give equation (10):

<!-- claim:eq-10 -->
\[
0\leq a_{ij}\leq1,
\qquad a_{ij}+a_{ji}=1\quad(i\ne j),
\qquad a_{ii}=0.
\]

No transitivity condition is imposed. Comparisons made in separate fresh registers have their designated probabilities, but the numbers need not be close to zero or one. A cycle of certain wins is allowed, as is a pair with winning probability exactly one half. In the algorithmic theorem, all pair circuits are available coherently, including under control of their indices, with a uniform cap of \(c\geq1\) bit queries per comparison and the same cap for its inverse. When a controlled query is implemented from an ordinary bit query, the constant overhead established below is included in \(c\).
<!-- /passage:upper-comparison-model -->

<a id="upper-tournament-parameters"></a>
<!-- passage:upper-tournament-parameters -->

For `def-T-eps`, put

<!-- claim:def-T-eps -->
\[
T=\left\lceil\log_2(1000m)\right\rceil,
\qquad \varepsilon=\frac{1}{1000T}.
\]

The base of the logarithm is part of the definition. In particular, \(2^T\geq1000m\). Call a vertex \(s\) dominant if it satisfies equation (11):

<!-- claim:eq-11 -->
\[
a_{sj}\geq1-\varepsilon\qquad(j\ne s).
\]

The theorem below is conditional on this property of \(s\). Its algorithm has no such promise: it runs and obeys its query cap for every comparison table satisfying equation (10). The property is only used to prove that a particular vertex is likely to occur in the returned list.
<!-- /passage:upper-tournament-parameters -->

<a id="upper-ideal-process"></a>
<!-- passage:upper-ideal-process -->

Begin with weights \(w_i=1\) and an empty ordered list \(L\). Write \(W=\sum_iw_i\). In one ideal step, if \(W>0\), choose a pivot \(p\) with probability \(w_p/W\), append it to \(L\), and make the update in equation (12):

<!-- claim:eq-12 -->
\[
w_i\longleftarrow w_i a_{ip}\qquad(1\leq i\leq m).
\]

If \(W=0\), leave the weights zero and append nothing. Run exactly \(T\) steps, with this zero state absorbing. This specifies `def-ideal-process` on every history. All weights remain nonnegative and at most one, because they are products of numbers in \([0,1]\). After a history \(p_1,\ldots,p_t\), the weight of \(i\) is the product of \(a_{ip_b}\) over \(b\leq t\). A selected vertex receives the factor \(a_{pp}=0\), so it has zero weight thereafter and cannot be selected again on a positive-weight step. These observations also describe what happens at histories of probability zero without requiring division by zero.
<!-- /passage:upper-ideal-process -->

<a id="upper-weight-drift"></a>
<!-- passage:upper-weight-drift -->

Condition on any current weights with \(W>0\). For pivot \(p\), the new total weight is \(\sum_iw_ia_{ip}\). Averaging over its probability \(w_p/W\) gives the first expression in equation (13). To evaluate its numerator, write it as the sum over ordered pairs \((i,p)\). The diagonal terms vanish because \(a_{ii}=0\). Pairing the term for \((i,p)\) with the term for \((p,i)\), for each unordered pair with \(i\ne p\), gives \(w_iw_p(a_{ip}+a_{pi})=w_iw_p\). The sum of the \(w_iw_p\) over unordered pairs is half of \(W^2-\sum_iw_i^2\). Therefore

<!-- claim:eq-13 -->
\[
\mathbb E[W_{\rm new}\mid w]
 =\frac1W\sum_{p,i}w_pw_i a_{ip}
 =\frac{W^2-\sum_iw_i^2}{2W}
 \leq\frac W2.
\]

At \(W=0\) both the current and next total weights are zero, so the last inequality still holds. Taking expectations over histories gives \(\mathbb E W_{t+1}\leq\tfrac12\mathbb E W_t\). Starting from \(W_0=m\) and applying this inequality \(T\) times proves `claim-expected-WT`:

<!-- claim:claim-expected-WT -->
\[
\mathbb E W_T\leq\frac{m}{2^T}.
\]

This calculation uses only complementary probabilities and nonnegativity. It applies equally to deterministic tournaments, cyclic tournaments, and comparisons whose probabilities are bounded away from both zero and one.
<!-- /passage:upper-weight-drift -->

<a id="upper-dominant-weight"></a>
<!-- passage:upper-dominant-weight -->

Suppose \(s\) is dominant and has not appeared among the first \(t\leq T\) pivots. Every factor contributing to its weight is then at least \(1-\varepsilon\), so `claim-weight-lb` is

<!-- claim:claim-weight-lb -->
\[
w_s(t)\geq(1-\varepsilon)^t
\geq1-t\varepsilon
\geq1-T\varepsilon
=\frac{999}{1000}>\frac12.
\]

The middle inequality follows by induction on \(t\). At \(t=0\) it is equality. Multiplying the bound at \(t\) by \(1-\varepsilon\geq0\) gives \(1-(t+1)\varepsilon+t\varepsilon^2\geq1-(t+1)\varepsilon\). Thus, until \(s\) is selected, the total weight is positive and exceeds one half. In particular, an absorbing zero state cannot be reached before selecting \(s\).

If \(s\) is missing from the ideal list at time \(T\), the same argument gives \(W_T>1/2\). The indicator of this event is at most \(2W_T\) pointwise. Taking expectations proves equation (14), without any separate regularity assumption on the weight distribution:

<!-- claim:eq-14 -->
\[
\Pr[s\notin L_T]
\leq\Pr[W_T\geq1/2]
\leq2\,\mathbb EW_T
\leq\frac{2m}{2^T}.
\]

**Lean evidence for the ideal process.** `QuarticQuery.Tournament.two_mul_weighted_sum` is the paired-sum identity; `QuarticQuery.Tournament.expected_weight_eq` and `QuarticQuery.Tournament.expected_weight_le_half` give equation (13). The corpus has no reviewed tie for that equation, although these declarations are present. `QuarticQuery.Tournament.expectFrom` defines the finite process, and `QuarticQuery.Tournament.expected_final_weight`, `QuarticQuery.Tournament.pow_le_weight`, `QuarticQuery.Tournament.dominant_weight_lb`, `QuarticQuery.Tournament.half_lt_total`, and `QuarticQuery.Tournament.ideal_miss_le` give the expectation, survival, and miss bounds. `QuarticQuery.Tournament.ideal_tournament` packages the ideal guarantee at `QuarticQuery.Tournament.Tval` and `QuarticQuery.Tournament.epsval`. The source stores the most recent pivot at the head of the list; products of real weights are independent of this bookkeeping order.
<!-- /passage:upper-dominant-weight -->

<a id="upper-stage-state"></a>
<!-- passage:upper-stage-state -->

We now implement a quantum version of one step. Fix the current classical pivot list \(p_1,\ldots,p_t\). Prepare a uniform index \(i\in[m]\), and, controlled by \(i\), run a fresh copy of the comparison with \(p_b\), for every \(b\leq t\). Let \(|\phi(i,p_b)\rangle\) denote the full normalized state of that copy, including its outcome bit and all workspace. For a self-comparison, set the outcome bit to false without querying the oracle. The prepared state is equation (15):

<!-- claim:eq-15 -->
\[
\frac1{\sqrt m}\sum_{i=1}^m |i\rangle
 \bigotimes_{b=1}^{t}|\phi(i,p_b)\rangle.
\]

The empty tensor product at \(t=0\) is a one dimensional state. Reversibly compute an additional success bit that is true precisely when every comparison outcome says that \(i\) won. Keep the individual outcomes and all the work registers. The preparation is a unitary, and its inverse reverses the comparisons and the success computation.
<!-- /passage:upper-stage-state -->

<a id="upper-stage-law"></a>
<!-- passage:upper-stage-law -->

For fixed \(i\), the different comparisons act on separate initially fixed registers. Projection onto all successful outcome bits is a tensor product of their success projections. Its squared norm is therefore the product of their squared norms, namely the product of \(a_{ip_b}\), which is \(w_i\). Distinct index values remain orthogonal. Summing their squared norms and remembering the initial factor \(1/\sqrt m\) proves `claim-success-prob`:

<!-- claim:claim-success-prob -->
\[
\Pr[\text{success and index }i]=\frac{w_i}{m},
\qquad
\Pr[\text{success}]=\frac Wm,
\qquad
\Pr[i\mid\text{success}]=\frac{w_i}{W}\quad(W>0).
\]

There is no interference between different decoded outcomes hidden inside a comparison: its outcome probability already includes its entire retained workspace. There is also no assumption that different pairs share a common deterministic orientation. What is multiplied here is the success probability of distinct, fresh uses of their specified circuits at one fixed oracle input.
<!-- /passage:upper-stage-law -->

<a id="upper-quantum-tournament"></a>
<!-- passage:upper-quantum-tournament -->

Apply Lemma 3.1 to this preparation with \(\gamma=1/(2m)\) and \(\eta=\varepsilon\). On reported failure, stop and return the current list. On success, measure the index, append it to the list, and proceed. Stop after at most \(T\) appended indices. These instructions define `construct-sampler` for every input and every history, whether or not a dominant vertex exists.

Conditioned on success, the amplified state is the normalized success component of the unamplified preparation. Measuring its index consequently has exactly the distribution \(w_i/W\). This exact conditional law is essential: a mere lower bound on the chance of obtaining some successful index would not justify the ideal weight calculation. When \(W=0\), the unamplified success probability is zero, and Lemma 3.1 reports failure with certainty.

The compiled version uses a useful finite-label statement. Let \(q_x(b)\) be the unamplified probability of a successful label \(b\), and put \(q_x=\sum_bq_x(b)\). There is a failure probability \(f_x\in[0,1]\) such that the output law has the following form, recorded as `new-upper-sampler-law`:

<!-- claim:new-upper-sampler-law -->
\[
\Pr[\bot]=f_x,
\qquad
\Pr[b]=(1-f_x)\frac{q_x(b)}{q_x}\quad(q_x>0),
\qquad
q_x\geq\gamma\Longrightarrow f_x\leq\eta,
\qquad
q_x=0\Longrightarrow f_x=1.
\]

This follows from the phase-independent success-state assertion just proved, followed by measurement of the label. The source proves this measured-law statement directly for its coherent samplers in `QuarticQuery.Upper.Samples.amplify`. For the tournament, \(q_x(i)=w_i/m\), so its normalized law is the ideal pivot law. Fresh trial registers preserve the proof literally. The formal compiler has a second implementation: after an amplified attempt, it measures a complete basis label, keeps the classical result, and applies a known permutation taking that measured basis vector to the fixed starting basis vector. Because the state is known after that full measurement, this reset is legitimate and uses no oracle call. It then runs the continuation. This is the alternative composition route recorded for `QuarticQuery.Upper.Samples.runs`.
<!-- /passage:upper-quantum-tournament -->

<a id="upper-coupling"></a>
<!-- passage:upper-coupling -->

We compare the real process with the ideal one on a common probability space. As long as their lists agree, let \(f(L)\) be the failure probability of the amplified sampler for that list. If \(W>0\), independently choose a possible ideal next pivot with distribution \(w_i/W\), and a Bernoulli variable that reports failure with probability \(f(L)\). On nonfailure, give both processes the chosen pivot. On failure, stop the real process and continue the ideal one with its ordinary transitions. This has the correct marginal distribution for each process: the real sampler's successful probability for pivot \(i\) is exactly \((1-f(L))w_i/W\). Independence here is a way to construct the coupling from that law; it is not an additional property demanded of the implementation.

Suppose \(s\) is dominant. At an agreed history of length at most \(T\) before \(s\) is selected, the preceding lower bound gives \(W>1/2\). Thus \(W/m\geq1/(2m)\), and \(f(L)\leq\varepsilon\). For each of the at most \(T\) stages, condition on the event that there has been no earlier disagreement and \(s\) has not yet appeared. The conditional chance of a new disagreement is at most \(\varepsilon\). Multiplying by the probability of the conditioning event and summing over the stages gives a total at most \(T\varepsilon\). No independence among these stage failures is needed.

If the ideal process selects \(s\) and there has been no disagreement before that selection, the real list already contains \(s\). A later failure cannot remove a previous entry. Consequently the real miss event is contained in the union of the ideal miss event and a disagreement before selecting \(s\). Equation (14) proves `claim-coupling`:

<!-- claim:claim-coupling -->
\[
\Pr[\text{the real list misses }s]
\leq\frac{2m}{2^T}+T\varepsilon.
\]

This argument deliberately stops charging failures after \(s\) has appeared. At those later histories the total weight can be arbitrarily small, and the sampler need not have failure probability at most \(\varepsilon\). The claim only needs the already recorded occurrence of \(s\).
<!-- /passage:upper-coupling -->

<a id="upper-tournament-cost"></a>
<!-- passage:upper-tournament-cost -->

At history length \(t\), the state preparation uses \(t\) controlled comparison circuits; the uniform superposition and the success conjunction are input independent. Its query cost and that of its inverse are at most a constant times \(c(t+1)\). Lemma 3.1 uses at most a constant times \(\sqrt m\ln(1/\varepsilon)\) calls to these preparations. The explicit limits on trials and iterations apply even when the success probability is below \(1/(2m)\). Summing the costs for \(t=0,\ldots,T-1\), and using \(\sum_{t=0}^{T-1}(t+1)=T(T+1)/2\), gives `claim-tournament-cost`:

<!-- claim:claim-tournament-cost -->
\[
\text{queries}
=O\!\left(c\sqrt m\,T^2\ln(1/\varepsilon)\right)
=O\!\left(c\sqrt m\,T^2\log T\right).
\]

The second equality uses \(1/\varepsilon=1000T\) and \(T\geq1\), indeed \(T\geq11\) when \(m\geq2\). The constants are absolute. Early stopping can only reduce this cost. This proves Proposition 3.2: uniformly for every family of coherently available comparison circuits satisfying the stated cap, one algorithm returns a list of at most \(T\) vertices, has the displayed query cap on every input, and contains every specified dominant vertex \(s\) with probability at least \(1-2m/2^T-T\varepsilon\). No estimate of the \(a_{ij}\)'s is required.
<!-- /passage:upper-tournament-cost -->

<a id="upper-tournament-evidence"></a>
<!-- passage:upper-tournament-evidence -->

**Lean evidence and the exact remaining difference for Proposition 3.2.** The declarations `QuarticQuery.Upper.stageLaw_some`, `QuarticQuery.Upper.sum_stageLaw_some`, and `QuarticQuery.Upper.stage_samples` identify and implement the weights. The source implementation may skip a later comparison once a previous one has failed; it retains the failed outcome and never marks that branch successful. The probability of surviving all comparisons is still their product. Thus it realizes the law above, without asserting that its complete workspace is literally the tensor state in equation (15).

`QuarticQuery.Upper.tval_lower` proves the coupling estimate by induction on histories in a form that also includes final verification. `QuarticQuery.Upper.tournament_runs` then produces an actual bit-query program. Its output type is Boolean: it passes the candidate list to a verifier and takes the disjunction of the verifier results. In particular, its theorem does not return a list, and its lower bound includes a final verifier error \(\varepsilon\). This is why the corpus correctly marks the tie for `prop-3.2` as partial. The ideal list theorem is formalized, and the quantum proof above reconstructs the paper's list statement, but the inspected Lean endpoint is the Boolean continuation needed below. We do not identify that endpoint with the stronger list-valued statement.

The implementation also pads every stage cost to the maximum possible \(T\) comparisons and charges the bit-query compiler's factor of two per abstract read. These changes preserve the claimed asymptotic bound. None of this reasoning requires a classical tournament with a fixed orientation to be extracted from the probabilistic comparisons.
<!-- /passage:upper-tournament-evidence -->

<a id="upper-continuation-induction"></a>
<!-- passage:upper-continuation-induction -->

We give the induction used by that Boolean continuation, so the difference in its statement also has a complete mathematical explanation. Fix verifier acceptance probabilities \(v(i)\in[0,1]\), and let \(V(L)\) be the probability that at least one fresh verification of a member of \(L\) accepts. Sequential verification gives \(V([])=0\) and \(V(i::L)=v(i)+(1-v(i))V(L)\). In particular \(0\leq V(L)\leq1\); if \(s\in L\), then \(V(L)\geq v(s)\); and if all \(v(i)\leq\varepsilon\), then \(V(L)\leq|L|\varepsilon\). Each assertion follows by induction on the list using the recursive rule, or equivalently by the union bound for the verifier outcomes.

Let \(R_n(L)\) be the acceptance probability with \(n\) tournament stages still available after history \(L\). With no stage remaining it is \(V(L)\). With a stage remaining, it is the sum of \(f(L)V(L)\), representing immediate sampler failure and verification of the present list, and \((1-f(L))\sum_i(w_i/W)R_{n-1}(i::L)\), representing a successful pivot and continuation. When \(W=0\), set the weighted sum to zero; the guaranteed \(f(L)=1\) makes the same formula correct. For positive \(W\), the weights in that sum are nonnegative and sum to one. It follows inductively that \(R_n(L)\in[0,1]\). If all \(v(i)\leq\varepsilon\), the same recursion gives \(R_n(L)\leq(|L|+n)\varepsilon\): an immediate stop has bound \(|L|\varepsilon\), and each successful successor has bound \((|L|+1+n-1)\varepsilon\). A convex combination preserves the larger bound.

For the lower bound, let \(I_n(L)\) be the probability that \(s\) is absent after \(n\) further ideal stages. Suppose \(0\leq\varepsilon\leq1\), \(s\) is dominant, \(v(s)\geq1-\varepsilon\), and a total horizon \(T_0\) satisfies \(T_0\varepsilon<1/2\). Suppose also that \(f(L)\leq\varepsilon\) for every history of length at most \(T_0\) missing \(s\), and \(f(L)=1\) whenever \(W=0\). The exact inductive assertion, recorded as `new-upper-continuation-bound`, is

<!-- claim:new-upper-continuation-bound -->
\[
R_n(L)\geq(1-\varepsilon)\bigl(1-I_n(L)-n\varepsilon\bigr)
\qquad(|L|+n\leq T_0).
\]

At \(n=0\), if \(s\) is in \(L\), the right side is \(1-\varepsilon\), which is at most \(V(L)\). Otherwise \(I_0(L)=1\) and the right side is zero. For a positive number of stages, a history already containing \(s\) continues to contain it after every pivot and at every stopping point. Induction in the recursion therefore gives \(R_n(L)\geq v(s)\geq1-\varepsilon\), which suffices because the right side is at most \(1-\varepsilon\).

For a history missing \(s\), its dominant weight is at least \(1-|L|\varepsilon>1/2\), so \(W>0\). The ideal miss probability is the weighted mean of the successor miss probabilities. Averaging the inductive lower bounds at successors gives a lower bound \(Q=(1-\varepsilon)(1-I_n(L)-(n-1)\varepsilon)\) for the successful continuation. The immediate-stop term is nonnegative, so \(R_n(L)\geq(1-f(L))Q\). We always have \(Q\leq1-\varepsilon\), even when \(Q\) is negative. If \(Q\geq0\), then \(f(L)Q\leq\varepsilon(1-\varepsilon)\); if \(Q<0\), then \(f(L)Q\leq0\leq\varepsilon(1-\varepsilon)\). Subtracting this upper bound from \(Q\) yields exactly the desired lower bound with \(n\varepsilon\). This proves the induction without assuming that failure probabilities at different histories are equal or independent.

At the empty history with \(n=T_0=T\), the ideal estimate gives \(I_T([])\leq2m/2^T\). Expanding the product in the lower bound and discarding its nonnegative cross term gives \(R_T([])\geq1-2m/2^T-T\varepsilon-\varepsilon\). This is the acceptance guarantee in `QuarticQuery.Upper.tournament_runs`, and it accounts for its additional verifier error. The source's `QuarticQuery.Upper.tval` and `QuarticQuery.Upper.missFrom` are \(R_n(L)\) and \(I_n(L)\), respectively, and `QuarticQuery.Upper.tval_lower` is the displayed assertion.
<!-- /passage:upper-continuation-induction -->


### 5.3. Decoding, comparison, and verification


<a id="upper-decode"></a>
<!-- passage:upper-decode -->

Return to the total function \(F_{k,m}\). Fix \(k\geq2\) and \(m=4^t\) with \(t\geq1\). As in the construction, write \(\ell=2t=\log_2m\) and \(r=40t=20\ell\). A column has \(r\) Forrelation instances whose promised values, when all are defined, form its address. The circuit used for the construction has size \(S=O_k(m\ell^2)\). We use the same \(T,\varepsilon\) as above.

For `def-decode`, run the quantum algorithm from Lemma 2.1\(ii\) on each of the \(r\) Forrelation instances in the selected column, reducing the error on each promised instance to at most \(\varepsilon/r\). Implement its trials and decision rule reversibly, retaining the outcome labels and all intermediate work. Its output register always contains an \(r\)-bit string; when some promises fail this string has no stipulated relation to a semantic address. The number of queries is nevertheless capped on every input. There is no loop that waits for a promise to become true.
<!-- /passage:upper-decode -->

<a id="upper-decode-cost"></a>
<!-- passage:upper-decode-cost -->

For fixed \(k\), an instance can be decoded with \(O_k(\ln(r/\varepsilon))\) queries. Running the \(r\) copies gives `claim-decode-cost`:

<!-- claim:claim-decode-cost -->
\[
\text{address-decoding queries}
=O_k\!\left(r\ln(r/\varepsilon)\right),
\qquad
\Pr[\text{correct address}]\geq1-\varepsilon
\quad\text{if all }r\text{ promises hold}.
\]

To prove the probability assertion, let \(E_h\) be the error event for instance \(h\). For promised instances, \(\Pr(E_h)\leq\varepsilon/r\). The event that the address is wrong is the union of these \(r\) events, whose probability is at most their sum, \(\varepsilon\). This union bound does not require independence. In the source implementation the copies are fresh, so the law of the address string is more specifically the product of their Boolean output laws.

The source uses a threshold on a retained count of Forrelation outcomes. If \(\delta=2^{-5k}\), its repetition count is \(n=\lceil16\delta^{-2}\ln(r/\varepsilon)\rceil\), up to the exact natural-number convention in `QuarticQuery.Forrelation.repetitions`. Each repetition has \(k\) abstract reads, so the address circuit has \(rnk\) such reads. This is the same error-reduction purpose as in the paper; the count and threshold remain in the workspace. Source declarations `QuarticQuery.Upper.decode_samples`, `QuarticQuery.Upper.addr_samples`, `QuarticQuery.Upper.addrLaw_good`, and `QuarticQuery.Upper.addrCost` give the circuit, law, correctness, and cost. The corpus has no reviewed Lean tie for `claim-decode-cost`, so these are additional source correspondences, not a promotion of its recorded evidence status.
<!-- /passage:upper-decode-cost -->

<a id="upper-comparator"></a>
<!-- passage:upper-comparator -->

For `def-comparison`, fix a numerical ordering of the columns. On a distinct pair, first place its smaller index first, so that both ordered calls use the same underlying circuit. Decode both addresses with fresh work registers. At the decoded address of the first column, read the pointer directed toward the second column and then the addressed entry of the second column's \(X\)-block. If that entry is zero, declare the second column disqualified. Do the reverse operation using the second decoded address to test whether the first column is disqualified. If exactly one is disqualified, the other wins. If both or neither are disqualified, the smaller column wins. A self-comparison always returns false and makes no pointer query.

Reading a pointer requires its \(\ell\) address bits, followed by the targeted \(X\)-bit. Reversible reading keeps the pointer and the target address available for uncomputation. Thus the two pointer tests use \(O(\ell+1)\) bit queries, with a constant factor if controlled reads are needed. Together with the two decodings, a comparison and its inverse have query cost \(c=O_k(r\ln(r/\varepsilon)+\ell)= (\log m)^{O_k(1)}\). The circuit is defined on all input strings. Reversing its gate sequence gives its inverse with the same number of queries because the bit oracle is its own inverse.
<!-- /passage:upper-comparator -->

<a id="upper-comparison-law"></a>
<!-- passage:upper-comparison-law -->

For `claim-comparison-state`, we check why the coherent calculation has the probabilities suggested by the classical description. After decoding, write the state as a sum over the two decoded labels, with every summand carrying those labels in dedicated retained registers. The subsequent pointer tests and winner computation are controlled by these labels and do not erase them. The final projection onto a winning output is block diagonal with respect to the retained labels. Thus the squared norm of that projection is the sum, over label pairs, of the squared norms of the corresponding projected summands. Cross terms vanish because distinct labels are orthogonal. Within one summand, the pointer test exactly reads the designated bits. Its contribution is therefore the decoding probability of those labels multiplied by the deterministic result of the comparison rule at those labels.

The result is precisely a classical mixture over the decoded labels. Retaining extra work within a label block changes neither this orthogonality nor the rule. In `QuarticQuery.Upper.Samples.bind`, this fact is proved by treating controlled subsequent computations as a direct sum of unitaries. The comparison circuit is assembled in `QuarticQuery.Upper.core_samples`; `QuarticQuery.Upper.firstWins` fixes the disqualification rule. The two possible winners exhaust the outcomes for each distinct unordered pair. Reversing the names of the pair merely complements which event is counted. Hence \(a_{ij}+a_{ji}=1\), while the self-comparison gives \(a_{ii}=0\). `QuarticQuery.Upper.cmpProb_isComparison` states these identities, and `QuarticQuery.Upper.cmpProb_unit` gives their probability bounds. This proves the hypotheses used in equation (10), even when neither decoded address is promised to be meaningful.
<!-- /passage:upper-comparison-law -->

<a id="upper-winner-dominates"></a>
<!-- passage:upper-winner-dominates -->

Suppose now that \(i^\star\) is a winning column. Its \(X\)-block consists entirely of ones, by the definition of a winner. A pointer from any opponent, at any decoded address, therefore cannot find a zero in that block. Thus \(i^\star\) is never disqualified. This statement is unconditional on the opponent's promises and on the opponent's decoded label.

The winner's own Forrelation promises hold, and its correct decoded address occurs with probability at least \(1-\varepsilon\). At that address, its pointer into each other column finds a zero, again by the definition of a winner. Whenever its decoding is correct, every opponent in the comparison is consequently disqualified and \(i^\star\) wins, regardless of the numerical tie convention. Correct decoding is thus a subset of the event that it wins. We obtain `claim-winner-dominates`:

<!-- claim:claim-winner-dominates -->
\[
a_{i^\star j}\geq1-\varepsilon\qquad(j\ne i^\star).
\]

This proof uses no correctness assertion for a nonwinning column's decoder. It also explains why independently amplifying an assumed comparison bias would have been unjustified: the available guarantee is a strong one-sided property of a true winner, while other pairs may have arbitrary probabilities. The source isolates the two deterministic facts in `QuarticQuery.winner_no_incoming_zero` and `QuarticQuery.winner_finds_zero`, and combines them with the address law in `QuarticQuery.Upper.cmpProb_winner`. The latter lower-bounds the winning probability by the probability of the true decoded address; `QuarticQuery.Upper.addrLaw_good` supplies \(1-\varepsilon\).
<!-- /passage:upper-winner-dominates -->

<a id="upper-verifier"></a>
<!-- passage:upper-verifier -->

For `def-verify`, use a fresh address decoding for the candidate column and measure its decoded address. Fix the resulting address \(a\). Lemma 2.2 provides a finite list of exact local tests. Their number is

<!-- claim:def-K -->
\[
K=m+(m-1)+r(S+2)=O_k(m\ell^3).
\]

The first \(m\) tests check that the candidate's \(X\)-block is all ones. The next \(m-1\) tests follow its pointers at address \(a\) and check a zero in each other column. For each of the \(r\) Forrelation instances, there are \(S\) tests checking the gate values in the proposed circuit transcript, and two checking the required outputs. These tests depend on the candidate and the fixed address, but are exact Boolean computations on the raw input. A gate test reads at most three bits, and a pointer test is an adaptive decision tree of depth at most \(\ell+1\). The uniform per-test depth is therefore \(\max\{3,\ell+1\}=O(\log m)\). We use the depth bound; it is not necessary that every pointer test depend on a fixed small set of input coordinates.

Prepare a uniform test label, compute whether that test fails, and mark failure of the test as success for an application of Lemma 3.1. Use \(\gamma=1/K\) and \(\eta=\varepsilon\). Reject the candidate if this search returns a failed test, and accept if it reports failure to find one. Decode and verify every column in the returned tournament list with fresh randomness, stopping if one is accepted; output one exactly in that event. The empty list produces zero.
<!-- /passage:upper-verifier -->

<a id="upper-verification-proof"></a>
<!-- passage:upper-verification-proof -->

For a fixed input, candidate, and decoded address, let \(h\) be the number of failed local tests. The search preparation has success probability \(h/K\), since the tests are exact and their labels are uniform. If \(h=0\), Lemma 3.1 has success probability zero and reports failure to find a test with certainty; the verifier accepts with certainty. If \(h\geq1\), its success probability is at least \(1/K\), and the verifier accepts with probability at most \(\varepsilon\).

Lemma 2.2 supplies the needed logical dichotomy. A nonwinner has at least one failed test at every address. This includes the case that its Forrelation strings violate their promises: if the test list at some address all passed, circuit consistency and the output tests would make that address a genuine winning address. Thus, after averaging over every possible decoded label, a nonwinner is accepted with probability at most \(\varepsilon\). A true winner has all tests passing at its true address. Its fresh decoder produces that address with probability at least \(1-\varepsilon\), and on that event verification accepts with certainty. Therefore the true winner is rejected with probability at most \(\varepsilon\). These are `claim-verify`:

<!-- claim:claim-verify -->
\[
\Pr[\text{accept a nonwinner}]\leq\varepsilon,
\qquad
\Pr[\text{reject the winner}]\leq\varepsilon.
\]

The search uses \(O(\sqrt K\ln(1/\varepsilon))\) calls to a uniform-test preparation and its inverse. Each preparation has \(O(\ell+1)\) bit-query cost. Adding the fresh address decoding yields \(O_k(r\ln(r/\varepsilon)+\sqrt K\ln(1/\varepsilon)(\ell+1))=\sqrt m(\log m)^{O_k(1)}\) queries. This is a cap for all values of \(h\), including zero. The algorithm can accept a nonwinner only by missing a failed test; it never accepts because it has assumed an unverified promise about the candidate.

The exact test sampler appears in `QuarticQuery.Upper.test_samples`. `QuarticQuery.Upper.testLaw_pass` and `QuarticQuery.Upper.testLaw_fail` establish the zero and positive cases, and `QuarticQuery.Upper.search_runs` implements their bounded search on the bit oracle. `QuarticQuery.Upper.verifyProb` averages over the decoded address. The two verifier inequalities are discharged inside `QuarticQuery.Upper.Fkm_QLe`. The corpus has no reviewed tie for `claim-verify`; these source declarations supply its individual mathematical components.
<!-- /passage:upper-verification-proof -->

<a id="upper-total-error"></a>
<!-- passage:upper-total-error -->

We now prove `claim-error` for every input of the total function. On a zero input, every column is a nonwinner. Condition on the complete tournament transcript and on its list, which contains at most \(T\) entries. Each subsequent fresh verification accepts its candidate with probability at most \(\varepsilon\), regardless of that transcript. For any fixed list, the probability of at least one false acceptance is at most \(T\varepsilon\), by the union bound. Averaging over the tournament transcript preserves this bound. Early stopping at the first acceptance makes no change to the event that at least one acceptance occurs.

On a one input, uniqueness of the winner gives a column \(i^\star\). The comparison argument makes it dominant. The tournament misses it with probability at most \(2m/2^T+T\varepsilon\). If it occurs in the list, its fresh verification accepts with probability at least \(1-\varepsilon\), even conditional on the previous transcript. Any earlier acceptance already gives the correct output one. Thus an erroneous zero output is contained in the union of the miss event and rejection of \(i^\star\) when it is verified. We obtain

<!-- claim:claim-error -->
\[
\Pr[\text{error}\mid F_{k,m}(x)=0]\leq T\varepsilon,
\qquad
\Pr[\text{error}\mid F_{k,m}(x)=1]
\leq\frac{2m}{2^T}+T\varepsilon+\varepsilon<\frac13.
\]

For the last numerical inequality, \(2^T\geq1000m\) gives \(2m/2^T\leq1/500\), and \(T\varepsilon=1/1000\). Also \(T\geq1\) gives \(\varepsilon\leq1/1000\). Their sum is at most \(1/250\), which is less than \(1/3\). The zero-input bound is smaller still. The formal source proves these constants in `QuarticQuery.Tournament.miss_bound_le`, `QuarticQuery.Tournament.Tval_mul_epsval`, and `QuarticQuery.Tournament.total_error_lt`. Its `QuarticQuery.Upper.tval_le` and `QuarticQuery.Upper.tval_lower` establish the two conditional probability estimates for the actual continuation, including history-dependent stage failure.
<!-- /passage:upper-total-error -->


### 5.4. Coherent access and the query cap


<a id="upper-oracle-access"></a>
<!-- passage:upper-oracle-access -->

We spell out `claim-coherent-access` because the algorithm uses addresses and candidate indices in superposition. The input oracle acts on a coordinate register, an answer bit, and workspace by sending \(|u,b,z\rangle\) to \(|u,b\mathbin\oplus x_u,z\rangle\). A superposed address is an allowed coordinate state for this same oracle. Computing the coordinate from already stored labels is an input independent reversible operation, so it contributes no query. A pointer is stored in \(\ell\) separate input bits. Reading its bits, reversibly forming the indicated coordinate, and querying that coordinate costs \(\ell+1\) ordinary queries before any desired uncomputation.

A controlled read can always be implemented with two ordinary bit queries. Start with a fresh answer ancilla zero. Query \(x_u\) into that ancilla, perform the desired action controlled jointly by its value and by the original control, and query \(x_u\) again to erase the ancilla. Keep the coordinate \(u\) unchanged until this second query. The desired action can be an XOR into an output register or a sign change. The resulting transformation is the controlled bit or phase query on every superposition of \(u\), control, and workspace, because the basis-state calculation applies linearly. The same construction works when the original control is false: both queries still occur, and their effects cancel.

An exact adaptive local test can be made coherent by retaining its previous query answers, using them to compute the next coordinate, and padding its computation to the fixed maximum depth. At a branch that has halted early, the remaining controlled reads are disabled. Every gate remains a fixed function of the retained labels. The query count is at most a constant times the decision-tree depth. Reversing the full circuit gives the inverse with the same cost. These operations justify coherent comparisons, their inverses, uniform local-test preparation, and the reflections used by amplification within the ordinary bit-oracle model.
<!-- /passage:upper-oracle-access -->

<a id="upper-read-compiler"></a>
<!-- passage:upper-read-compiler -->

The source provides a concrete compilation argument behind this accounting. An abstract read has a coordinate function on basis labels, an involutive permutation of those labels, and an optional sign. Applying that permutation does not change either its coordinate or its sign. Given a basis label, the compiler embeds the abstract register into the physical coordinate, answer-bit, and workspace registers, loads the queried bit, applies the indicated signed permutation if that bit is one, queries the unchanged coordinate again, and returns to the chosen embedding. On bit zero it is the identity; on bit one it is exactly the prescribed signed involution. Both actions preserve inner products. The finite isometries used to place the active register extend to unitaries on sufficiently large finite workspace by completing an orthonormal basis. This is why no unmentioned input-dependent gate is needed.

The source relation `QuarticQuery.Upper.IsCirc` is generated by input independent gates and these reads. Its composition, inverse, and controlled direct-sum constructions retain a read count. `QuarticQuery.Upper.compile_read` uses exactly two bit queries per read before the continuation; `QuarticQuery.Upper.compile_circ` sums this overhead over a circuit. `QuarticQuery.Upper.Samples.runs` adds measurement of the sampler label and the measured-basis reset described earlier. Its continuation laws show that the assembled finite program has exactly the sampler's output distribution. Finally, `QuarticQuery.Upper.Runs.toQLe` and `QuarticQuery.Upper.Runs.toQLePartial` convert a bounded program and its probability guarantees into the quantum-complexity predicate defined in `Model/Quantum.lean`.

In particular, the source's final bound concerns the same total input function, on every bit string, and the cap is a syntactic maximum over branches. It does not measure an average number of queries. It does not provide a bound on the number of elementary gates or the amount of workspace, which are free in the stated query model.
<!-- /passage:upper-read-compiler -->

<a id="upper-finite-budget"></a>
<!-- passage:upper-finite-budget -->

We can now state an exact finite budget before simplifying it asymptotically. This makes the padding, repetitions, and compilation constants explicit. Let \(n\) be the Forrelation repetition count for error \(\varepsilon/r\), let \(a=rnk\) be the address circuit's abstract read count, let \(c_c=2a+2(2t+1)\) be the comparison read count, and let \(c_0=\max\{3,2t+1\}\) be the uniform test read count. Write \(N=\lceil\ln(1/\varepsilon)/\ln(40/31)\rceil\), \(M_0=\lceil10\sqrt{2m}\rceil\), and \(M_1=\lceil10\sqrt K\rceil\). The supplied construction has the following budget, recorded as `new-upper-finite-budget`:

<!-- claim:new-upper-finite-budget -->
\[
B_{k,t}
 =T\bigl[2N(2M_0+1)T c_c\bigr]
  +T\bigl[2a+2N(2M_1+1)c_0\bigr].
\]

The first bracket is one tournament stage: at most \(N\) trials, at most \(2M_0+1\) preparation or inverse calls per trial, at most \(T c_c\) abstract reads per such call, and two bit queries per read. Every stage is padded to the maximum history length \(T\), and there are at most \(T\) stages. The second bracket is one verifier: \(2a\) bit queries for its fresh address decoder, followed by the amplified local-test search with its corresponding trial and iteration bounds. There are at most \(T\) candidates to verify. All random branches and all off-promise inputs obey this same integer budget.

`QuarticQuery.Upper.budget` is this expression in the source vocabulary. `QuarticQuery.Upper.Fkm_QLe` proves that it bounds \(Q(F_{k,m})\) for any supplied circuit that realizes the promised Forrelation predicate. Thus the correctness argument is established before using the size of the particular circuit chosen in the construction. The exact conversion factors in this budget are convenient upper bounds; the earlier expression with \(t\) comparisons at stage \(t\) gives the same asymptotic result with less padding.
<!-- /passage:upper-finite-budget -->

<a id="upper-asymptotic-bound"></a>
<!-- passage:upper-asymptotic-bound -->

The earlier estimates already prove Proposition 3.3. The tournament contributes \(O(c\sqrt m\,T^2\log T)\) queries, where \(c=(\log m)^{O_k(1)}\), and the at most \(T=O(\log m)\) verifications each cost \(\sqrt m(\log m)^{O_k(1)}\). Their sum has the same form. Coupled with the error bound, this gives `prop-3.3`:

<!-- claim:prop-3.3 -->
\[
Q(F_{k,m})\leq\sqrt m\,(\log m)^{O_k(1)}
\qquad(k\geq2,\ m=4^t,\ t\geq1).
\]

Here \(F_{k,m}\) uses the circuit fixed for that \(k,m\) in the construction. The implicit constants may depend on \(k\). The exponent statement concerns query complexity, and every input is covered. There is no appeal to Bansal and Sinha's randomized lower bound in this proof of the quantum upper bound.
<!-- /passage:upper-asymptotic-bound -->

<a id="upper-explicit-log6"></a>
<!-- passage:upper-explicit-log6 -->

The inspected source proves a stronger explicit exponent, which we record separately as `new-upper-log6`. There is a positive integer \(C_k\), depending only on \(k\), such that the particular Forrelation circuit used in the construction satisfies

<!-- claim:new-upper-log6 -->
\[
Q(F_{k,4^t})\leq C_k\,2^t(2t)^6
\qquad(t\geq1).
\]

We give the size arithmetic to make the independence of \(C_k\) from \(t\) explicit. Put \(\tau=2t\) and \(u=2^t\), so \(m=u^2\), \(r=20\tau\), and \(\tau\geq2\). Let \(C_F(k)\) be the fixed circuit-size constant with \(S\leq C_F(k)m\tau^2\). Define \(R_k=1+1920000\cdot2^{10k}\), \(C_c(k)=40R_kk+4\), and \(C_K(k)=42+20C_F(k)\). Each is independent of \(t\).

First, \(1000<2^{10}\) implies \(T\leq\tau+10\leq6\tau\). Hence \(1/\varepsilon=1000T\leq6000\tau\). Using \(\ln(1/\varepsilon)\leq1/\varepsilon\) and \(\ln(40/31)\geq1/4\), the ceiling defining \(N\) gives \(N\leq4/\varepsilon+1\leq24001\tau\). Likewise \(r/\varepsilon\leq120000\tau^2\). Since the decoder's repetition count is at most \(16\cdot2^{10k}\ln(r/\varepsilon)+1\), it is at most \(R_k\tau^2\). Thus \(a=rnk\leq20R_kk\tau^3\). The remaining comparison cost \(2(\tau+1)\) is at most \(4\tau^3\), so \(c_c\leq C_c(k)\tau^3\).

Second, the formula for \(K\) gives \(K=2m-1+20\tau(S+2)\leq C_K(k)m\tau^3\). For example, the circuit term is at most \(20C_F(k)m\tau^3\); the \(2m\) term is at most \(2m\tau^3\), and \(40\tau\leq40m\tau^3\). Because \(C_K(k)\geq1\) and \(\tau\geq1\), this implies \(\sqrt K\leq C_K(k)u\tau^2\). Also \(\sqrt{2m}\leq2u\). The ceilings consequently give \(2M_0+1\leq43u\) and \(2M_1+1\leq23C_K(k)u\tau^2\). Finally \(c_0\leq3\tau\).

Insert these bounds into the two brackets of \(B_{k,t}\). One tournament stage is at most \(48002\cdot258\,C_c(k)u\tau^5\): the factors are twice \(24001\tau\), then \(43u\), then \(6\tau\,C_c(k)\tau^3\). Its at most \(6\tau\) stages contribute at most \(6(48002\cdot258\,C_c(k))u\tau^6\). One verifier is at most \((40R_kk+48002\cdot69\,C_K(k))u\tau^4\). Here its decoder cost \(2a\) has been enlarged using \(u,\tau\geq1\), and its search term has factors twice \(24001\tau\), then \(23C_K(k)u\tau^2\), then \(3\tau\). Multiplying by \(T\leq6\tau\) and enlarging \(\tau^5\) to \(\tau^6\) gives the remaining contribution. Thus one may take \(C_k=6(48002\cdot258\,C_c(k))+6(40R_kk+48002\cdot69\,C_K(k))\), exactly the source's deliberately loose constant `QuarticQuery.Upper.budgetConst`.

`QuarticQuery.Upper.budget_le` proves this arithmetic for a circuit obeying the size bound. `QuarticQuery.Upper.Fkm_forrCircuit_QLe` instantiates the realizing circuit and supplies an explicit bounded quantum algorithm, while `QuarticQuery.Upper.Q_Fkm_le` gives the corresponding numerical complexity inequality. Their source statements include positive \(k\) in a slightly broader parameterization; the present construction uses \(k\geq2\). The corpus classifies these ties to Proposition 3.3 as stronger. This completes the quantum half of the family bounds with the same chosen circuit that appears in the total function.
<!-- /passage:upper-explicit-log6 -->


## 6. The classical lower bound

### 6.1. A direct product with a separate query cap on each input


<a id="CL-direct-product-statement"></a>
<!-- passage:CL-direct-product-statement -->
Let $P:D\to\{0,1\}$, where $D\subseteq\{0,1\}^{n}$, let $\mu$ be a probability distribution supported on $D$, and let $L,r$ be nonnegative integers. Suppose every deterministic tree of depth at most $L$ computes $P$, on an input distributed according to $\mu$, with success probability at most $\beta$. If $U_1,\ldots,U_r$ are independent with distribution $\mu$, a classical algorithm that makes at most $L$ queries to each input on every run has the following bound. It may choose its queries adaptively across inputs, use independent random coins, and receive additional information jointly independent of the whole input tuple.

<!-- claim:lem-4.1 -->
\[
\Pr\!\left[\text{the algorithm outputs }
\bigl(P(U_1),\ldots,P(U_r)\bigr)\right]\leq\beta^{r}.
\]

The separate cap is the essential hypothesis. A bound on the sum of the query counts alone would not justify this conclusion with the same exponent and base. The fair-decision-tree result goes back to Shaltiel [Shaltiel2003, §5, Definition 4, Theorem 5, and Lemma 7; the theorem there is formulated for XOR advantage](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html). Drucker's formulation gives the conditional product argument used in the preprint [Drucker2012, §1.3, Lemmas 3.1–3.2, and the final paragraph of §3](https://arxiv.org/abs/1005.0644v2). His headline Theorem 1.1 concerns a different global-budget statement. We recover the preprint's conditional argument first, then give the weighted induction used by the supplied Lean source.
<!-- /passage:CL-direct-product-statement -->

<a id="CL-product-law"></a>
<!-- passage:CL-product-law -->
Fix all independent information and coins, so that the algorithm is deterministic. Consider a transcript $\tau$ having positive probability. For each $h$, let $E_h(\tau)$ be the set of inputs whose bits agree with all answers recorded from $U_h$. Repeated queries add repeated copies of the same constraint and cause no difficulty. The event of seeing $\tau$ is exactly the Cartesian product of these sets. One inclusion follows from consistency of the observed answers. For the other, start with any tuple satisfying these constraints. The first query is fixed. Its answer is the recorded answer, so the deterministic algorithm chooses the second recorded query. Continuing inductively reproduces every recorded query and answer, including a stop decision if the transcript is terminal.

Independence before the run now implies the conditional product law.

<!-- claim:claim-product-law -->
\[
\mathcal L(U_1,\ldots,U_r\mid\tau)
=\bigotimes_{h=1}^{r}\mu(\,\cdot\mid E_h(\tau)).
\]

To verify the identity directly, the probability of a compatible tuple is its product mass divided by $\prod_h\mu(E_h(\tau))$, and this quotient is the product of the separate conditional masses. Positive probability of $\tau$ makes every denominator positive. This proves the independence assertion even though the schedule of queried inputs was adaptive. The corpus has no Lean tie for this conditional-law statement; the later weighted proof avoids introducing conditional distributions.
<!-- /passage:CL-product-law -->

<a id="CL-conditional-values"></a>
<!-- passage:CL-conditional-values -->
At transcript $\tau$, let $q_h$ be the number of queries already made to $U_h$, counting repetitions. Define $V_h(\tau)$ to be the largest conditional success probability for computing $P(U_h)$ with at most $L-q_h$ further queries, under its conditional law at $\tau$. There are finitely many trees of any fixed depth on a finite set of coordinates, so the maximum exists. The cap ensures $L-q_h\geq0$. This is `def-value-V`.

Suppose the next query is to input $h$. Querying that bit and then using an optimal continuation in either resulting branch is one permissible strategy under the old budget. Its success probability is the conditional average of the two new optimal values. Consequently,

<!-- claim:eq-16 -->
\[
\mathbb E\bigl[V_h(\tau')\mid\tau\bigr]\leq V_h(\tau).
\]

An answer of conditional probability zero contributes zero and need not be assigned a conditional optimization problem. The other inputs retain exactly their old conditional laws, by the product law, and exactly their old remaining budgets. Their values are unchanged. This reasoning also handles a repeated query: its answer is already determined, but the budget still decreases by one, which cannot improve the optimum. These are the exact claims of Eq. 16. Their source route in the corpus is prose-only.
<!-- /passage:CL-conditional-values -->

<a id="CL-supermartingale"></a>
<!-- passage:CL-supermartingale -->
Every $V_h$ is nonnegative. Multiplying the preceding conditional inequality by the unchanged product of the other factors gives the product supermartingale inequality.

<!-- claim:claim-supermartingale -->
\[
\mathbb E\!\left[\prod_{j=1}^{r}V_j(\tau')\,\middle|\,\tau\right]
\leq\prod_{j=1}^{r}V_j(\tau).
\]

There are at most $rL$ queries. After a branch stops, keep its values unchanged until this fixed horizon. Repeatedly summing the displayed inequality over the finite distribution of transcripts shows that the expected final product is at most its initial product. Initially each factor is at most $\beta$, by the one-input hypothesis, so the initial product is at most $\beta^r$.

At a terminal transcript, the chosen output vector is fixed. The conditional product law gives a product of the separate probabilities that its coordinates are correct. Each is at most the larger of the two output probabilities, and making no further query is an allowed continuation in the optimization defining $V_h$. Hence,

<!-- claim:claim-final-bound -->
\[
\Pr[\text{chosen vector correct}\mid\tau]
\leq\prod_{h=1}^{r}\max_{b\in\{0,1\}}
\Pr[P(U_h)=b\mid\tau]
\leq\prod_{h=1}^{r}V_h(\tau).
\]

Averaging proves the deterministic case of Lemma 4.1. This uses only a finite sequence of conditional averages; no limiting stopping theorem is needed. If $r=0$, the output is the empty vector and both sides equal one, using the empty-product convention. If $L=0$, the algorithm makes no input queries and the same product-of-best-guesses argument applies. The supermartingale and terminal claims have no separately checked declarations in the corpus. Their endpoint is proved by the following alternative route.
<!-- /passage:CL-supermartingale -->

<a id="CL-weighted-values"></a>
<!-- passage:CL-weighted-values -->
For the formal route, extend $\mu$ by zero outside $D$, and more generally allow a nonnegative weight $\nu$ on the whole finite input cube without requiring its total mass to be one. The weighted success of a constant answer $b$ is the sum of $\nu(x)$ over inputs with $P(x)=b$; the weighted success of a tree is the sum over inputs where its answer is correct. Inputs outside $D$ contribute zero. Write $\nu_{q,b}(x)=\nu(x)$ when $x_q=b$, and zero otherwise.

Define $W_c(\nu)$ recursively by the following finite maxima. If there are no input coordinates, the inner maximum is omitted.

<!-- claim:NCL-weighted-value -->
\[
\begin{aligned}
W_0(\nu)&=\max_{b\in\{0,1\}}\sum_{x:P(x)=b}\nu(x),\\
W_{c+1}(\nu)&=\max\!\left\{W_c(\nu),\ 
\max_q\bigl(W_c(\nu_{q,0})+W_c(\nu_{q,1})\bigr)\right\}.
\end{aligned}
\]

These values equal the maximum weighted success over trees of depth at most $c$. At $c=0$, the only choices are the two constants. Inductively, each candidate in the second line is achieved: the first is achieved by an old optimal tree, while a candidate indexed by $q$ is achieved by querying $q$ and using an optimal depth-$c$ tree in each branch. Conversely, a tree of depth at most $c+1$ is either a constant or begins with a query $q$. Splitting its weighted success by the answer to this query expresses it as the sum of its two branch successes under $\nu_{q,0}$ and $\nu_{q,1}$. The induction bounds these by the corresponding terms in the maximum. This proves the characterization in both directions. It also proves nonnegativity, monotonicity in the budget, and the fact that the sum of the two optimal branch values is at most the value before spending the query.

The definitions are `QuarticQuery.constSuccess`, `QuarticQuery.treeSuccess`, `QuarticQuery.restrictWeight`, and `QuarticQuery.budgetValue`. The characterization is obtained from `QuarticQuery.exists_tree_budgetValue_le` and `QuarticQuery.treeSuccess_le_budgetValue`; the branch inequality is `QuarticQuery.budgetValue_add_le`. These are existing source declarations, registered here as a new intermediate statement because their combined formulation has no pre-existing corpus row.
<!-- /passage:CL-weighted-values -->

<a id="CL-weighted-product"></a>
<!-- passage:CL-weighted-product -->
We prove a stronger weighted assertion by induction on a multi-input tree $T$. Give input $h$ its own nonnegative weight $\nu_h$ and its own remaining cap $c_h$. Require every branch of $T$ to use at most $c_h$ queries to that input. Let its weighted vector success be the sum over all input tuples of the product weight times the indicator that every output coordinate is correct. Then,

<!-- claim:NCL-weighted-product -->
\[
\sum_{u_1,\ldots,u_r\in D}
\left(\prod_{h=1}^{r}\nu_h(u_h)\right)
\mathbf 1\!\left[T(u_1,\ldots,u_r)
=(P(u_1),\ldots,P(u_r))\right]
\leq\prod_{h=1}^{r}W_{c_h}(\nu_h).
\]

For a leaf with output vector $s$, finite distributivity factors the left side into the product of the constant-answer successes for $s_h$. Each factor is bounded by $W_{c_h}(\nu_h)$, and all factors are nonnegative, proving the leaf case.

If the root queries coordinate $q$ of input $h$, then $c_h>0$. Split the sum into the two possible answers. In answer branch $b$, replace only $\nu_h$ by $\nu_{h,q,b}$, and replace only its cap by $c_h-1$. Both subtrees satisfy these new caps, including on their other branches. The induction hypothesis bounds each branch by its corresponding product of optimal values. All factors other than the $h$-th are the same in both products. Factoring them out leaves their product multiplied by $W_{c_h-1}(\nu_{h,q,0})+W_{c_h-1}(\nu_{h,q,1})$. The recursion bounds this last sum by $W_{c_h}(\nu_h)$. Multiplication preserves the inequality because the factored product is nonnegative. This proves the assertion for every tree, including arbitrary interleavings of queries among the inputs.

Taking $c_h=L$ and $\nu_h=\mu$, the one-input hypothesis and the characterization of $W_L$ give $W_L(\mu)\leq\beta$. The displayed inequality therefore proves Lemma 4.1. This is the exact argument in `QuarticQuery.guessSuccess_le_prod`, with `QuarticQuery.guessSuccess_leaf` and `QuarticQuery.guessSuccess_query` providing its two decompositions. `QuarticQuery.direct_product` is the deterministic specialization. The unnormalized weights remove the need for conditional laws and their zero-probability cases.
<!-- /passage:CL-weighted-product -->

<a id="CL-independent-information"></a>
<!-- passage:CL-independent-information -->
Finally restore the independent side information and random coins. Fixing them gives a deterministic capped tree and leaves the law of the input tuple equal to $\mu^{\otimes r}$. Its success is at most $\beta^r$, so averaging gives the same bound. The source states this averaging explicitly for finite families in `QuarticQuery.direct_product_average` and `QuarticQuery.direct_product_randomized`.

Arbitrary independent information has the same consequence. There are only finitely many possible deterministic capped trees: each has total depth at most $rL$, each internal node has a query label in a finite set, and each leaf has a label in the finite set $\{0,1\}^{r}$. Finiteness follows recursively on depth, since a tree is a leaf or a choice of one query label and two smaller trees. Group all side-information and coin outcomes according to the tree they induce. Their probabilities give a finite mixture, to which the source's averaging theorem applies. This finite-behavior reduction, recorded as `NCL-finite-capped`, bridges the ordinary formulation with arbitrary independent information to the finite family written in Lean. Independence means independence of the entire tuple; separate independence from each coordinate would not suffice.
<!-- /passage:CL-independent-information -->


### 6.2. The hard distribution and the hidden address


<a id="CL-minimax"></a>
<!-- passage:CL-minimax -->
Suppose $L<R(P)$, with $L$ a nonnegative integer. The domain $D$ is nonempty, since on an empty domain a zero-query constant algorithm is correct vacuously. We prove the finite minimax conclusion needed here in full.

<!-- claim:claim-minimax-mu -->
\[
\text{There exists a distribution }\mu\text{ on }D
\text{ such that }
\Pr_{x\sim\mu}[T(x)=P(x)]\leq\frac23
\quad\text{for every tree }T\text{ of depth at most }L.
\]

There are finitely many such trees, by induction on their depth. Associate to each tree $T$ the vector $a_T\in\mathbb R^{D}$ whose coordinate at $x$ is one if $T(x)=P(x)$ and zero otherwise. Let $K$ be the convex hull of these finitely many vectors. A point of $K$ is exactly the vector of success probabilities of a finite randomized mixture of depth-$L$ trees. Conversely, every such mixture is a permissible randomized algorithm. Zero-weight trees can be removed without changing any probability. Thus $L<R(P)$ says that $K$ does not intersect the closed upper orthant $C=[2/3,\infty)^{D}$.

For completeness, construct a separating distribution directly. For $a\in K$, its closest point in $C$ has coordinates $c_x=\max(a_x,2/3)$, since each squared coordinate difference is minimized separately. The squared distance to $C$ is a continuous function of $a$. The convex hull $K$ is compact, so choose $a\in K$ minimizing that distance, and let $c\in C$ be its closest point. The distance is positive: if it were zero, this minimizing point would belong to both sets. Put $v=c-a$. Every coordinate of $v$ is nonnegative, and $v\ne0$.

For any $b\in K$, the segment $a+\theta(b-a)$, $0\leq\theta\leq1$, remains in $K$. Minimality of the chosen pair implies that its squared distance to the fixed point $c$ is at least the minimum squared distance when $\theta\geq0$. Expanding this quadratic and taking its right derivative at zero gives $v\cdot(b-a)\leq0$. Whenever $v_x>0$, the definition of the nearest point forces $c_x=2/3$. Therefore $v\cdot c=(2/3)\sum_xv_x$, while $v\cdot a=v\cdot c-\|v\|^2$. Since $\sum_xv_x>0$, define $\mu(x)=v_x/\sum_yv_y$. This is a probability distribution on $D$. For every $b\in K$, the preceding inequalities give $\mu\cdot b\leq2/3-\|v\|^2/\sum_xv_x<2/3$. Applying this to every $a_T$ proves the displayed weak inequality, and therefore the required hard distribution.

This is the finite game form of the distributional minimax principle associated with Yao [Yao1977](https://doi.org/10.1109/SFCS.1977.24). The source proves the same endpoint, `QuarticQuery.exists_hard_distribution`, through `QuarticQuery.exists_mixed_row` and Mathlib's finite-dimensional Sion minimax theorem. `QuarticQuery.finite_depth_le` supplies the finite set of trees, and `QuarticQuery.exists_program_of_mixture` converts a mixed strategy to the source's randomized-program representation. The nearest-point proof above is a complete prose alternative to that minimax implementation. It requires no distribution from the analytic Forrelation lower bound.
<!-- /passage:CL-minimax -->

<a id="CL-address-guess"></a>
<!-- passage:CL-address-guess -->
Apply Lemma 4.1 with this $\mu$ and $\beta=2/3$. One distribution works for every number $r$ of independent instances. Every algorithm with at most $L$ queries to each instance, and arbitrary jointly independent additional information, satisfies the address-guessing bound.

<!-- claim:claim-address-guess -->
\[
\Pr\!\left[\widehat s=(P(U_1),\ldots,P(U_r))\right]
\leq(2/3)^r.
\]

The declarations `QuarticQuery.address_guess_le`, `QuarticQuery.address_guess_average`, and `QuarticQuery.exists_address_guess_bound` establish respectively the deterministic bound, independent finite averaging, and existence of one suitable hard distribution. The reduction from arbitrary independent information is the finite-behavior argument already given.
<!-- /passage:CL-address-guess -->


### 6.3. Coupled zero and one inputs


<a id="CL-generic-statement"></a>
<!-- passage:CL-generic-statement -->
We now prove the following nonasymptotic form of Proposition 4.2. Let $m=4^t$ with $t\geq1$, let $r=40t$, and let $P$ be a partial Boolean function on $km$ bits with an exact circuit $C$ having the stated domain and value outputs. Let $F$ be the total function built from this same pair $(P,C)$. For every integer $L$ satisfying $1\leq L\leq m$ and $L<R(P)$, the conclusion is

<!-- claim:prop-4.2-generic -->
\[
R(F)>\left\lfloor\frac{mL}{100}\right\rfloor.
\]

Define the integer budget used in the proof by

<!-- claim:eq-17 -->
\[
G=\left\lfloor\frac{mL}{100}\right\rfloor.
\]

Circuit size plays no role in this lower bound. Indeed, the source theorem allows an arbitrary finite input-coordinate type for $P$, so its conclusion is stronger in that respect. We retain the concrete formulation of the corpus here. Fix the hard distribution $\mu$ obtained above, and fix a deterministic tree $T$ of depth at most $G$.
<!-- /passage:CL-generic-statement -->

<a id="CL-dummy"></a>
<!-- passage:CL-dummy -->
Construct the dummy input $Y^{(0)}$ as follows. For each column $i$, choose $J_i$ uniformly from $[m]$, independently across columns. Give $X_i$ its unique zero at $J_i$, with all its other bits one. Choose every $A_{i,h}$ independently according to $\mu$, independently also of all $J_i$. Fill every cell $B_{i,s}$ with the same fixed blank pattern; the source takes all bits false. These choices define `def-dummy` exactly. They also show that the cells carry no information about the hard instances before planting.

For finite probability calculations, all expectations in the source are ordinary finite sums. `QuarticQuery.avg` is a weighted sum and `QuarticQuery.prodW` is a product weight. The identity `QuarticQuery.avg_resample` says that independently replacing one coordinate of a product-distributed tuple by a fresh draw from its original law preserves every expectation. To check it, first fix all the other coordinates and sum over the old and new coordinate. The summand after replacement is independent of the old coordinate, whose weights sum to one; what remains is exactly the original sum over the new coordinate. This identity will let us fix outside data without changing the averaged experiment.
<!-- /passage:CL-dummy -->

<a id="CL-planted"></a>
<!-- passage:CL-planted -->
Choose a column $I$ uniformly from $[m]$, independently of the entire dummy input. Form $Y^{(1)}$ from $Y^{(0)}$ by changing $X_I$ to $1^m$ and filling only $B_{I,s_I}$ with the correct transcripts on $A_{I,h}$ and with pointers $p_{I,s_I,j}=J_j$ for every $j\ne I$. The $A$-strings are unchanged. Since they are sampled from $D$, the true address $s_I$ exists at every sample point when the experiment is viewed directly on $D^{mr}\times[m]^m\times[m]$. This is `def-planted`.

Every dummy input has value zero, since each column contains a zero. Every planted input has value one: column $I$ is all ones, its address comes from promised inputs, its selected transcripts are the actual circuit evaluations, and its pointer into each rival column reaches that column's zero. Thus,

<!-- claim:claim-Y-values -->
\[
F(Y^{(0)})=0,
\qquad F(Y^{(1)})=1.
\]

The constructions are `QuarticQuery.dummy`, `QuarticQuery.trueAddr`, and `QuarticQuery.planted`; the two values are proved by `QuarticQuery.addressedF_dummy` and `QuarticQuery.addressedF_planted`. The formal weighted experiment ranges over the whole cube, with zero weight off $D$, so its one-input value assertion is required only on positive-weight sample points. This is equivalent to the experiment just described on the domain itself.
<!-- /passage:CL-planted -->

<a id="CL-first-difference"></a>
<!-- passage:CL-first-difference -->
The coupled inputs can differ only at the erased zero $X_I[J_I]$ and at coordinates of the planted cell $B_{I,s_I}$. If the deterministic tree has different outputs on the two inputs, its run on the dummy input must query a coordinate at which they differ. Prove this directly by induction down the run. Until the first different answer, the entire history is identical, and the next query or stop decision is identical. If every answer along the dummy run were the same on the planted input, both runs would therefore reach the same leaf. This contradicts different outputs.

For Boolean output indicators, the absolute difference of the two expected indicators is at most the probability that the outputs differ. The first-difference implication and a union bound then give

<!-- claim:eq-18 -->
\[
\left|\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]\right|
\leq
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
+\Pr[T\text{ on }Y^{(0)}\text{ queries a bit of }B_{I,s_I}].
\]

`QuarticQuery.QueryTree.exists_mem_path_ne` is the first-difference statement, and `QuarticQuery.eq_of_dummy_ne_planted` identifies the two possible classes of differing coordinates. `QuarticQuery.output_gap_le` packages the one-sided indicator inequality used later, with the cell event already divided into heavy and nonheavy cases. The absolute-value display is the direct prose consequence just proved; the exact exported final discrepancy theorem is one-sided.
<!-- /passage:CL-first-difference -->


### 6.4. How often can the erased zero be found?


<a id="CL-early-late"></a>
<!-- passage:CL-early-late -->
Let $Z$ be the number of columns whose unique zero is discovered during the dummy run. This is `def-Z`. Before a zero is discovered in column $i$, its location is conditionally uniform among the positions of that column not yet queried. To see this, fix a positive-probability full transcript. The event of realizing that transcript is the conjunction of the recorded constraints on each $J_i$ and each $A_{i,h}$, by the same deterministic-history induction used in the direct-product proof. For an undiscovered zero, its only constraints are exclusions of the distinct queried positions. The uniform prior on $J_i$ therefore remains uniform on the complement. The fixed blank cells impose no further restrictions. This proves `claim-uniform-zero` with the full adaptive history included in the conditioning.

The preprint splits discoveries into early and late ones. A discovery is early if fewer than $m/2$ distinct positions of its column had been queried before it. At any such query to a previously unqueried position, the conditional chance of discovering the zero is at most $2/m$; a repeated query cannot make a new discovery. Summing over the at most $G$ query times gives an expected number of early discoveries at most $2G/m$. Every late discovery belongs to a column receiving at least $m/2$ queries. On each run there are at most $2G/m$ such columns, because their query counts are disjoint parts of the total count. This proves $\mathbb E Z\leq4G/m$, including adaptivity and repetitions. The unused independent index $I$ then gives

<!-- claim:eq-19 -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
=\frac{\mathbb E Z}{m}
\leq\frac{4G}{m^2}.
\]

The equality follows by first conditioning on the complete dummy run: exactly $Z$ choices of the independent uniform $I$ have their zero discovered. This recovers `claim-EZ` and Eq. 19 as stated. The supplied source proves a stronger estimate by the following shorter induction, without conditional probabilities.
<!-- /passage:CL-early-late -->

<a id="CL-zero-worlds"></a>
<!-- passage:CL-zero-worlds -->
Fix one column and all data outside it. For each possible zero position $j\in[m]$, let $x^{j}$ be the complete input in which this column has its single zero at $j$, with the fixed outside data unchanged. For any subset $U\subseteq[m]$, let $D_U(T)$ count those $j\in U$ for which the run of $T$ on $x^j$ queries position $j$ of this column. Let $Q_U(T)$ be the sum, over $j\in U$, of the number of queries the run on $x^j$ makes to the column, counting repetitions and all queries after a discovery. We prove

<!-- claim:NCL-zero-worlds -->
\[
|U|D_U(T)\leq2Q_U(T).
\]

Induct on the tree. A leaf makes neither queries nor discoveries, so both sides vanish. At a query outside the column, its answer is identical in all worlds $x^j$; all worlds take the same subtree, and the query contributes nothing to either count. The induction hypothesis for that subtree proves the assertion.

Suppose instead the root queries position $p$ of the column. If $p\notin U$, every world follows the answer-one subtree. The discovery count is unchanged, while each world pays one extra query, so the induction hypothesis again suffices. If $p\in U$, put $V=U\setminus\{p\}$, $n=|V|$, and let $d$ and $q$ be respectively the discovery count and query sum for the answer-one subtree restricted to $V$. The induction hypothesis gives $nd\leq2q$, and $d\leq n$ because there are only $n$ worlds. The world $p$ discovers its zero immediately and pays at least one query; all other worlds pay one query before entering that same subtree. Thus $D_U(T)=1+d$ and $Q_U(T)\geq1+n+q$. Finally, expanding gives $(n+1)(1+d)=nd+n+d+1\leq2q+2n+1\leq2(q+n+1)$, which is at most $2Q_U(T)$. This completes the induction, including an empty $U$.

This is the argument of `QuarticQuery.zero_search_sum`. The abstract source permits arbitrary injectively labelled column coordinates and arbitrary identical outside data. `QuarticQuery.column_zero_bound` applies it to the dummy construction. No step presumes that queries are distinct or that a run stops when it discovers a zero.
<!-- /passage:CL-zero-worlds -->

<a id="CL-zero-average"></a>
<!-- passage:CL-zero-average -->
Take $U=[m]$ in the preceding inequality and divide by $m^2$. Conditional on fixed outside data, the probability that the column's uniform zero is found is at most $2/m$ times the expected number of queries to that column. Average this inequality over the outside data. The resampling identity described above justifies replacing the chosen zero location by each of its possible values while keeping all other data fixed.

Sum over the columns. On every run, the sum of the query counts to the $X$-columns is at most $G$; queries to other coordinates only reduce this available total. Linearity of expectation gives $\mathbb E Z\leq2G/m$. Independence of $I$ therefore yields the sharper bound

<!-- claim:NCL-erased-zero-two -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
\leq\frac{2G}{m^2}.
\]

`QuarticQuery.avg_foundZero_le`, `QuarticQuery.sum_xQueries_le`, and `QuarticQuery.avg_foundZero_I_le` are the corresponding averaged statements. The last is the exact displayed bound under the tree-depth hypothesis. This is the checked alternative route supporting the weaker Eq. 19, and it is the bound used in `QuarticQuery.tree_gap_le`.
<!-- /passage:CL-zero-average -->

<a id="CL-zero-optional"></a>
<!-- passage:CL-zero-optional -->
There is a further elementary improvement, separate from the source route just proved. It is recorded as a prose-only new statement and is unnecessary for Proposition 4.2. With the outside data still fixed, run the tree on the reference input in which this column contains only ones. Let $p_1,\ldots,p_d$ be the distinct column positions on this reference path in order of first appearance. If a possible zero position $j$ is absent from this list, its world $x^j$ follows the entire reference path and never discovers the zero. If $j=p_s$, its run agrees with the reference path until the first query to $p_s$, where it discovers the zero. It has made at least $s$ queries to the column by then. Thus exactly $d$ worlds discover their zero. The other $m-d$ worlds each make at least $d$ column queries, and the discovering worlds make at least $1,2,\ldots,d$ respectively. Their total query count is consequently at least $d(d+1)/2+(m-d)d=d(2m-d+1)/2\geq d(m+1)/2$.

Repeated queries can only increase these counts. Additional queries after a discovery can only increase them too. Queries outside the column may depend adaptively on earlier answers, but before the first zero the complete histories coincide, so the comparison with the reference path remains valid. Averaging over the fixed outside data is legitimate because the zero location is independent and uniform before it is exposed. We obtain $\mathbb E Z\leq2\mathbb E Q_X/(m+1)$, where $Q_X$ is the total number of queries to all $X$-columns, and hence

<!-- claim:NCL-erased-zero-mplusone -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
\leq\frac{2G}{m(m+1)}.
\]

This refinement has no supplied Lean proof. It also clarifies sharpness: scanning one column without repetition until its zero is found gives one discovery and expected cost $(m+1)/2$, attaining the expectation-cost inequality. As $m$ grows, the coefficient two in the coarser inequality $\mathbb E Z\leq2\mathbb E Q_X/m$ is asymptotically sharp. That scan has worst-case cost $m$, so it does not prove optimality of every fixed worst-case distinguishing budget. The supplied review's scan-to-completion example should be read with this expected-cost qualification.
<!-- /passage:CL-zero-optional -->


### 6.5. A capped simulator for the planted cell


<a id="CL-heavy"></a>
<!-- passage:CL-heavy -->
A column $i$ is heavy when, over the entire dummy run, the algorithm makes more than $L$ queries in total to $A_{i,1},\ldots,A_{i,r}$. Repeated queries count. This is `def-heavy`. If the run makes $q_i$ such queries, then $\sum_iq_i\leq G$. Each heavy column contributes more than $L$ to this sum, so in particular $L$ times the number of heavy columns is at most $G$. Since $L\geq1$, dividing by $mL$ and using the independent uniform $I$ gives

<!-- claim:eq-20 -->
\[
\Pr[I\text{ is heavy}]\leq\frac{G}{mL}.
\]

The source proves the counting inequality on each path in `QuarticQuery.avg_heavy_le`, using `QuarticQuery.aQueries` and `QuarticQuery.sum_aQueries_le`. This pointwise form is stronger than the displayed averaged statement. The threshold concerns the sum over all $r$ instances in a column; an even smaller cap on each separate instance will follow for the simulator.
<!-- /passage:CL-heavy -->

<a id="CL-simulator"></a>
<!-- passage:CL-simulator -->
Fix a column $i$ and a query time $q\in\{1,\ldots,G\}$. Give a simulator all the dummy data outside the $r$ strings $A_{i,1},\ldots,A_{i,r}$, and let those strings be its queried inputs. It receives the full vector $J$, all other columns' $A$-strings, and the fixed blank cells. This information is jointly independent of the target tuple. In particular, it does not receive the target strings themselves, their true address, or a target transcript.

The simulator follows the deterministic algorithm on the dummy input until its proposed $q$-th query. Queries outside the target strings are answered from the supplied outside data. A query to one of the target strings is made to the corresponding simulator input and charged against a single counter. The simulator aborts before making the $(L+1)$-st such query. If it reaches the proposed query at time $q$, and that proposed coordinate belongs to a cell $B_{i,s}$, it outputs the address $s$. Otherwise, including early termination and an abort, it outputs a fixed vector. It need not read the proposed cell bit to identify its address. This is `def-simulator`.

On every run, this procedure makes at most $L$ target queries in total, and therefore at most $L$ queries to each target instance. This cap holds for all target input tuples and all branches, independently of whether the original run would eventually be heavy. The other queries consume no target queries because their answers are present in the independent side information. Thus the address-guessing lemma applies to the simulator without any conditioning on its observed behavior.

The source construction is `QuarticQuery.simTree`; `QuarticQuery.depth_simTree_le` proves its total target-query cap and `QuarticQuery.eval_simTree` proves that it follows the intended run until the cap. The substitution lemmas `QuarticQuery.dummy_update_of_aTarget_none` and `QuarticQuery.dummy_update_of_aTarget_some` justify exactly which answers are outside data and which must come from the target oracle. Although a source parameter for a complete dummy input syntactically contains target coordinates, the first lemma shows that the simulator never accesses them through the free outside-data branch.
<!-- /passage:CL-simulator -->

<a id="CL-joint-event"></a>
<!-- passage:CL-joint-event -->
Consider the event that column $i$ is nonheavy over the entire dummy run and the proposed $q$-th query lies in $B_{i,s_i}$. On this event, every earlier prefix has at most $L$ target queries. The simulator has therefore not aborted and has followed the original run faithfully up to its proposed query. Its output is exactly $s_i$. Thus this joint event is contained in the simulator's success event, and the address-guessing bound gives

<!-- claim:eq-21 -->
\[
\Pr[i\text{ is nonheavy and query }q\text{ lies in }B_{i,s_i}]
\leq(2/3)^r.
\]

The event remains inside the probability. Conditioning on nonheaviness can change the distribution of the target inputs and invalidate the hard-distribution premise. The proof only uses containment in the success event of an algorithm whose cap holds on all branches. The source's `QuarticQuery.reachedCell` records the corresponding joint event of nonheaviness and some visit to the true cell. `QuarticQuery.cellGuess` and `QuarticQuery.cellGuess_of_cellOf` identify the proposed cell's address. The formal proof of the union over query times is `QuarticQuery.avg_reachedCell_le`; the corpus ties the individual-time argument to its simulator ingredients.
<!-- /passage:CL-joint-event -->

<a id="CL-cell-union"></a>
<!-- passage:CL-cell-union -->
If the dummy run visits the true cell of a nonheavy column, it does so at one of its at most $G$ query times. Summing the preceding probabilities over times gives at most $G(2/3)^r$. Average over the independent uniform choice of $I$, then add the probability that $I$ is heavy. We obtain

<!-- claim:eq-22 -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries a bit of }B_{I,s_I}]
\leq\frac{G}{mL}+G(2/3)^r.
\]

For $G=0$ the union is empty and the statement is immediate. For positive $G$, no disjointness of the visits is needed: the union bound only enlarges the probability when several times visit the same cell. `QuarticQuery.avg_reachedCell_le` provides the nonheavy term, and `QuarticQuery.avg_heavy_le` provides the remaining term. Both apply with every fixed outside configuration before the product averaging.
<!-- /passage:CL-cell-union -->


### 6.6. The discrepancy contradiction and the floors


<a id="CL-discrepancy"></a>
<!-- passage:CL-discrepancy -->
Combine the first-difference inequality with the erased-zero and cell bounds. Using the preprint's coefficient four recovers its displayed discrepancy exactly.

<!-- claim:eq-23 -->
\[
\left|\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]\right|
\leq\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\]

The checked erased-zero induction improves the first summand to $2G/m^2$. The exact conclusion exported by `QuarticQuery.tree_gap_le` is the following one-sided form, which is sufficient for the contradiction.

<!-- claim:NCL-checked-gap -->
\[
\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]
\leq\frac{2G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\]

Its proof averages `QuarticQuery.output_gap_le` over the product distribution of the $A$-strings, the zero positions $J$, and the independent planted column $I$. `QuarticQuery.coupledAvg` is that finite expectation. Normalization follows by factoring the finite product sums; exchanging their order is finite distributivity. The absolute-value form with coefficient two also follows from the earlier prose first-difference argument, but it is not the exact statement of this exported declaration.
<!-- /passage:CL-discrepancy -->

<a id="CL-tail-numeric"></a>
<!-- passage:CL-tail-numeric -->
For the chosen parameters, $G\leq mL/100\leq m^2/100$. Since $r=20\log_2m$, elementary laws of real powers give the preprint's tail estimate.

<!-- claim:claim-tail -->
\[
G(2/3)^r
\leq\frac1{100}m^{\,2-20\log_2(3/2)}
=o(1).
\]

The exponent is negative: $(3/2)^2>2$ implies $\log_2(3/2)>1/2$, so the exponent is less than $-8$. A positive power of $m$ diverges, and its reciprocal tends to zero, proving the limiting assertion along powers of four as well.

For a uniform finite estimate, the source uses $4/9\leq1/2$. Raising both sides to $20t$ gives $(2/3)^{40t}\leq(1/2)^{20t}=m^{-10}$. Hence the last term is at most $1/(100m^8)\leq1/100$. The other two terms follow directly from $G\leq mL/100$ and $1\leq L\leq m$. Altogether,

<!-- claim:claim-numeric -->
\[
\frac{4G}{m^2}\leq\frac4{100},
\qquad
\frac{G}{mL}\leq\frac1{100},
\qquad
G(2/3)^r\leq\frac1{100},
\qquad
\frac4{100}+\frac1{100}+\frac1{100}=\frac6{100}<\frac13.
\]

`QuarticQuery.twoThirds_pow_le` supplies the finite power bound; `QuarticQuery.discrepancy_le`, `QuarticQuery.discrepancy_lt_third`, and `QuarticQuery.discrepancy_parameters` supply the numerical conclusions. The corpus correctly marks the real-logarithm tail as only partially represented by this different, sufficient power estimate. No unspecified sufficiently large threshold is needed for the displayed discrepancy estimate.
<!-- /passage:CL-tail-numeric -->

<a id="CL-randomized-contradiction"></a>
<!-- passage:CL-randomized-contradiction -->
Suppose a randomized algorithm of worst-case query cost at most $G$ computed $F$ with error at most $1/3$ on every input. On each dummy input it would output one with probability at most $1/3$, because that input has value zero. On each planted input in the support it would output one with probability at least $2/3$, because that input has value one. Averaging these pointwise success requirements over the coupling would give an output-one probability gap of at least $1/3$.

On the other hand, fix its random coins. The resulting deterministic tree has depth at most $G$, so its gap is at most $6/100$ by the preceding estimate. Averaging over the coin choice preserves this upper bound. The two inequalities contradict $6/100<1/3$. Therefore no such randomized algorithm exists. The total function has finite randomized complexity, since reading all its bits gives an exact algorithm. Monotonicity of the budget predicate consequently turns the failure of a $G$-query algorithm into $R(F)>G$.

This proves Proposition 4.2 in its stated generic form. `QuarticQuery.addressedF_not_RLe` proves the contradiction for every choice of parameters satisfying the discrepancy bound; `QuarticQuery.addressedF_lower` inserts the floor budget; and `QuarticQuery.Gvalue_lt_R_addressedF` supplies the uniform numerical specialization. The latter theorem even permits $t=0$, when its other hypotheses make sense, and arbitrary finite input-coordinate types. The proof needs no quantum algorithm and no circuit size estimate. In the source's semantic winner definition, it uses the existence of consistent evaluation transcripts from `CircuitRealises`; circuit correctness is additionally what connects the function to the local output tests used by the upper bound.
<!-- /passage:CL-randomized-contradiction -->

<a id="CL-floors"></a>
<!-- passage:CL-floors -->
For the concrete family, fix $k\geq2$ and put $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$, as in Eq. 5. The earlier partial-function lower bound gives $L<R(P_{k,m})$ for all sufficiently large powers of four. We now verify the other hypotheses and the floor estimate explicitly, uniformly for $t\geq8$.

First, $4t^2\leq2^t$ for all integers $t\geq8$. At $t=8$ the two sides are equal. If the inequality holds at $t\geq8$, then $(t+1)^2\leq2t^2$, since $2t^2-(t+1)^2=t^2-2t-1\geq0$; multiplying the inductive inequality by two gives the next case. Since $1-1/k\geq1/2$ and $m\geq1$, we have $m^{1-1/k}\geq\sqrt m=2^t\geq(2t)^2$. Therefore $a=m^{1-1/k}/(2t)^2\geq1$. Its floor satisfies $\lfloor a\rfloor\geq a/2$: if $n=\lfloor a\rfloor\geq1$, then $a<n+1\leq2n$. In particular $L\geq1$. Also $1-1/k\leq1$ and $(2t)^2\geq1$, so $a\leq m$ and $L\leq m$.

Now $mL\geq4^8\geq200$, so the same floor estimate applied to $mL/100$ gives $G\geq mL/200\geq ma/400$. Consequently,

<!-- claim:NCL-explicit-floor -->
\[
\left\lfloor\frac m{100}
\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor\right\rfloor
\geq\frac1{400}\frac{m^{2-1/k}}{(\log_2m)^2}
\qquad(k\geq2, m=4^t, t\geq8).
\]

This supplies `claim-floor` with the explicit choice $c_k=1/400$ and a uniform arithmetic threshold. The original claim is therefore valid for every fixed $k\geq2$. `QuarticQuery.four_mul_sq_le_two_pow`, `QuarticQuery.sq_le_rpow`, `QuarticQuery.one_le_Lvalue`, and `QuarticQuery.Lvalue_le_mValue` establish the intermediate estimates; `QuarticQuery.Gvalue_ge` is the explicit floor bound. Its source signature writes $\log_2m=2t$, and `QuarticQuery.logb_mValue` identifies that expression with the one displayed here.
<!-- /passage:CL-floors -->

<a id="CL-concrete-lower"></a>
<!-- passage:CL-concrete-lower -->
Choose $t$ large enough for the partial-function lower bound and also $t\geq8$. The same exact circuit $C_{k,m}$ used to define the function and establish its upper bound then satisfies all hypotheses of the generic result. We conclude the concrete Proposition 4.2 and its asymptotic consequence.

<!-- claim:prop-4.2 -->
\[
R(F_{k,m})>
\left\lfloor\frac m{100}
\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor\right\rfloor
\quad\text{for every sufficiently large power of four }m.
\]

<!-- claim:cor-R-omega -->
\[
R(F_{k,m})=\Omega_k\!\left(\frac{m^{2-1/k}}{(\log m)^2}\right).
\]

The constants in the arithmetic lower bound are uniform; the threshold inherited from $L<R(P_{k,m})$ may depend on $k$. `QuarticQuery.Gvalue_lt_R_Fkm` proves the concrete conclusion with the explicit hypotheses $k\geq2$, $t\geq8$, and $L<R(P_{k,m})$. It remains conditional on that last premise at this point in the dependency order. `QuarticQuery.rpow_le_of_Gvalue_lt` combines the lower bound with the floor arithmetic. The earlier partial-function section is where the fixed-$k$ premise is discharged; the lower-bound module does not establish it by itself.
<!-- /passage:CL-concrete-lower -->


## 7. Comparing exponents and completing Theorem 1.1


<a id="ROOT-FAMILY-ASSEMBLY"></a>
<!-- passage:ROOT-FAMILY-ASSEMBLY -->
Fix an integer $k\geq2$. The Forrelation lower bound supplies an integer threshold $t_0(k)$ beyond which $L<R(P_{k,4^t})$. The circuit construction gives a circuit deciding the promise and value of the same $P_{k,4^t}$, with size $O_k(4^t(2t)^2)$. Use this circuit in the total function. The quantum upper bound and the planted-input lower bound now concern exactly the same circuit and total function. This order matters: separately existential upper and lower bounds for two unrelated circuits would not imply a separation.

For $t\geq\max\{8,t_0(k)\}$, the floor calculation already proved with the classical lower bound gives $G\geq m^{2-1/k}/(400(\log m)^2)$. The strict inequality $G<R(F_{k,m})$ therefore implies the real-valued lower estimate in equation $2$, with $c_k=1/400$. The quantum estimate has $b_k=6$ and a positive constant $C_k$ supplied by the algorithm. The threshold and the quantum constant depend on $k$. This proves the family assertion of Theorem 1.1 with all floors removed in the stated direction.

**Evidence.** `QuarticQuery.family_bounds` in `Results/Conditional.lean` produces one circuit carrying both the upper bound and the implication needed for the lower bound. `QuarticQuery.ForrelationLower.bansalSinhaLower` supplies its remaining premise. The use of `QuarticQuery.Gvalue_ge` in `Results/Exponent.lean` gives the constant $1/400$. `QuarticQuery.familyBounds_of_bansalSinha`, `QuarticQuery.Upper.familyBoundsAt_of_lower` and `QuarticQuery.theorem_1_1_unconditional` assemble the quantified family. The corpus's partial ties for equation $2$ describe component theorems; their composition with the discharged Forrelation premise proves the full assertion.
<!-- /passage:ROOT-FAMILY-ASSEMBLY -->

<a id="ROOT-RATIO"></a>
<!-- passage:ROOT-RATIO -->
### 7.1. A fixed family defeats every smaller power below its exponent

Let $0\leq\alpha<4$, and choose an integer $k\geq2$ satisfying $2-1/k>\alpha/2$. Keep this $k$ fixed while $m$ grows through sufficiently large powers of four. Set $\varepsilon=2-1/k-\alpha/2>0$, and abbreviate $b=b_k$, $C=C_k$, $c=c_k$. For $m\geq4$, the quantity $a=\sqrt m(\log m)^b$ is at least $1$. Since $Q(F_{k,m})\leq Ca$, we have $1+Q(F_{k,m})\leq(1+C)a$. Raising this inequality to the nonnegative power $\alpha$, and dividing the lower bound for $R$ by it, yields

<!-- claim:claim-exponent-ratio -->
\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ \geq\ \frac{c}{(1+C)^\alpha}\,
\frac{m^{\varepsilon}}{(\log m)^{2+\alpha b}}
\ \longrightarrow\ +\infty.
\]

Here is a direct proof of the limit, including real powers. Write $m=4^t$, so its varying factor is $2^{2\varepsilon t}/(2t)^{2+\alpha b}$. Its natural logarithm is $2\varepsilon t\ln2-(2+\alpha b)\ln(2t)$. For $u\geq1$, the integral formula for the logarithm gives $\ln u=\int_1^u s^{-1}ds\leq\int_1^u s^{-1/2}ds=2(\sqrt u-1)\leq2\sqrt u$. Thus $\ln(2t)/t\leq2\sqrt2/\sqrt t\to0$. Dividing the logarithm by $t$ leaves a quantity tending to the positive number $2\varepsilon\ln2$. The logarithm itself therefore tends to $+\infty$, which proves the displayed limit.

Given any proposed positive universal constant $D$, the ratio eventually exceeds $D$. Thus one of these total functions violates $R(f)\leq D(1+Q(f))^\alpha$. There is no issue of comparing undefined powers: every base is strictly positive. The case $\alpha=0$ is included.

**Evidence.** `QuarticQuery.eventually_gt_rpow` and its uniform precursor `exists_threshold_gap` prove the eventual strict comparison for arbitrary sequences satisfying the two bounds. They are partial ties to the displayed explicit ratio because the ratio itself and its particular constant are absent from their conclusions. The arithmetic above proves that literal ratio in prose. The Lean limit proof uses the library's exponential-versus-power asymptotic theorem; the integral estimate above gives an elementary route to the same comparison.
<!-- /passage:ROOT-RATIO -->

<a id="ROOT-NO-SMALLER"></a>
<!-- passage:ROOT-NO-SMALLER -->
### 7.2. The order of the choices

For every $0\leq\alpha<4$, the number $2-\alpha/2$ is positive. Choose an integer $k\geq2$ with $k>1/(2-\alpha/2)$; the unboundedness of the natural numbers supplies such a choice. Then $1/k<2-\alpha/2$, so $2-1/k>\alpha/2$. The previous argument applies after this choice. In particular,

<!-- claim:claim-no-smaller-exponent -->
\[
0\leq\alpha<4\quad\Longrightarrow\quad
\neg\exists C>0\ \forall n\geq1\ \forall f:\{0,1\}^n\to\{0,1\},\qquad
R(f)\leq C(1+Q(f))^\alpha.
\]

The construction's input coordinates form a finite disjoint union of finite blocks. The block $X$ alone is nonempty. Choose a bijection from that coordinate set to $[n]$, where $n\geq1$ is its cardinality. Reindexing the input by this bijection preserves $R$ and $Q$, as proved in the model section. Hence each structured input function is a legitimate counterexample to the universal statement over $\{0,1\}^n$. Its number of input bits may be very large; the definition of a universal query exponent places no restriction on that number.

Appendix A proves that $4$ is itself admissible. The set in the definition of $\alpha_{\mathrm{tot}}$ is therefore nonempty. The displayed exclusion implies that each of its members is at least $4$; admissibility of $4$ shows that this lower bound belongs to the set. It is consequently its minimum and its infimum. This proves $\alpha_{\mathrm{tot}}=4$ without invoking any convention for the infimum of an empty set.

For the cubic corollary, take $k=3$. Then $2-1/k=5/3>3/2$, so the ratio $R/(1+Q)^3$ tends to infinity. If a real constant $C$ satisfied $R(f)\leq C Q(f)^3$ universally, its maximum with $1$ would be positive and would also satisfy $R(f)\leq\max\{C,1\}(1+Q(f))^3$. The established contradiction for exponent $3$ disproves the original bound. This argument handles constants and a possibly nonpositive proposed $C$ without dividing by $Q(f)$.

**Evidence.** The choices and comparisons are formalized by `QuarticQuery.exists_nat_exponent`, `transport_bound`, `not_universalPower_of_familyBoundsAt`, `not_universalPower_of_family`, and `alphaTot_eq_four_of` in `Results/Exponent.lean`. The concrete family is supplied through `Results/Conditional.lean` and its premise is discharged in `Results/Unconditional.lean`. The latter file proves `alphaTot_eq_four_unconditional` and `cubic_bound_fails_unconditional`. Earlier files with explicitly conditional statements remain useful reusable theorems; their hypotheses do not remain assumptions of these final declarations.
<!-- /passage:ROOT-NO-SMALLER -->


## Appendix A. The universal quartic upper bound


<a id="ROOT-APPENDIX-INTRO"></a>
<!-- passage:ROOT-APPENDIX-INTRO -->
This appendix proves the universal estimate used to close Theorem 1.1. The argument combines the spectral adversary method, the spectral consequence of Huang's signed cube, and the maximum-monomial decision tree of Midrijānis. Aaronson, Ben-David, Kothari, Rao and Tal proved the resulting quartic upper bound [ABKRT2021, Theorem 2](https://arxiv.org/abs/2010.12629). Their spectral-sensitivity estimate is Lemma 9, and their degree estimate is Theorem 1. The corresponding numbering in the supplied flattened text extraction differs from the original PDF; the citations here use the PDF.

The Lean endpoint is `QuarticQuery.R_le_D_le_one_add_Q_pow_four` in `Appendix/TheoremA1.lean`. It obtains the explicit constant $20736$ through `Cslib.Quantum.complexity_le_mul_pow_four` and the query-model bridges. That is an alternative formal route. Lemmas A.2 through A.5 in the preprint's forms are not asserted to have been checked by that endpoint. The following proofs establish them in ordinary mathematics.
<!-- /passage:ROOT-APPENDIX-INTRO -->

<a id="ROOT-DEGREE-BLOCK"></a>
<!-- passage:ROOT-DEGREE-BLOCK -->
### A.1. Degree and sensitive blocks

Let $f:\{0,1\}^n\to\{0,1\}$ be total. A polynomial is multilinear if each variable has exponent at most one in each monomial. There is a multilinear polynomial agreeing with $f$ on the cube: sum over inputs $a$ the term $f(a)\prod_{i:a_i=1}x_i\prod_{i:a_i=0}(1-x_i)$. At a cube point $x$, exactly the factor indexed by $a=x$ is $1$, and all other factors vanish. Uniqueness follows by induction on $n$. A multilinear polynomial can be written uniquely as $p_0(x_1,\ldots,x_{n-1})+x_np_1(x_1,\ldots,x_{n-1})$. If it vanishes on the cube, evaluation at $x_n=0$ forces $p_0=0$ by induction, and evaluation at $x_n=1$ forces $p_1=0$. The case $n=0$ concerns a constant polynomial.

The degree $\deg(f)$ is the greatest size of a monomial with a nonzero coefficient in this representation. Every constant function, including zero, is assigned degree zero. An invertible affine change from input bits to signs and the inverse change each fail to increase degree, so the degree is unchanged. Changing a nonconstant Boolean output from $f$ to $1-2f$ multiplies every nonconstant coefficient by a nonzero number and therefore preserves degree. Constants remain degree zero by convention. This proves the convention recorded in `def-deg`.

For $B\subseteq[n]$, write $x^B$ for the input obtained by flipping exactly the coordinates in $B$. A sensitive block at $x$ is a nonempty $B$ with $f(x^B)\ne f(x)$. The block sensitivity $\operatorname{bs}(f,x)$ is the greatest number of pairwise disjoint sensitive blocks at $x$, and $\operatorname{bs}(f)$ is its maximum over inputs. Both maxima exist because the cube and its subsets are finite. A constant function has block sensitivity zero. These definitions give `def-bs`.
<!-- /passage:ROOT-DEGREE-BLOCK -->

<a id="ROOT-ADVERSARY-PERRON"></a>
<!-- passage:ROOT-ADVERSARY-PERRON -->
### A.2. A nonnegative spectral adversary bound

Index real matrices by the $2^n$ inputs. All matrix norms in this appendix are Euclidean operator norms. For a matrix $\Gamma$ and coordinate $i$, define its coordinate mask by

<!-- claim:def-Gamma-i -->
\[
(\Gamma_i)_{xy}=\Gamma_{xy}\,\mathbf1\{x_i\ne y_i\}.
\]

Suppose $\Gamma$ is real symmetric, entrywise nonnegative and nonzero. A real symmetric matrix has a real orthonormal eigenbasis, and its operator norm is the greatest absolute value of an eigenvalue. Choose a unit eigenvector $w$ attaining that absolute value. The vector $v=|w|$, with absolute values taken coordinatewise, is a nonnegative unit vector. Entrywise nonnegativity gives $v^{\mathsf T}\Gamma v\geq|w^{\mathsf T}\Gamma w|=\|\Gamma\|$. The opposite inequality follows from the operator norm and Cauchy–Schwarz. Thus equality holds. Expand $v$ in an orthonormal eigenbasis. Its Rayleigh quotient is a convex combination of the eigenvalues and equals their greatest possible value $\|\Gamma\|$; every nonzero coefficient must therefore belong to that eigenspace. We have proved

<!-- claim:claim-perron -->
\[
\Gamma v=\|\Gamma\|v,\qquad v_x\geq0,\qquad\sum_xv_x^2=1.
\]

This elementary argument supplies precisely the Perron-type assertion needed here, including matrices with several connected components.
<!-- /passage:ROOT-ADVERSARY-PERRON -->

<a id="ROOT-ADVERSARY-PROGRESS"></a>
<!-- passage:ROOT-ADVERSARY-PROGRESS -->
Assume in addition that $\Gamma_{xy}=0$ whenever $f(x)=f(y)$. Consider a quantum algorithm with cap $q$ and error at most $1/3$. It can be represented by pure states and a fixed sequence of at most $q$ query slots on a larger workspace. Here are the details needed to justify that representation. A projective measurement can be replaced by the isometry $\psi\mapsto\Pi\psi\otimes|1\rangle+(I-\Pi)\psi\otimes|0\rangle$; the two branches occupy orthogonal history states. An isometry on a subspace extends to a unitary by completing orthonormal bases. Later operations are controlled by the stored history. At the final measurement, orthogonality of histories makes the output probabilities the same sums of branch masses as in the adaptive program.

Align the branches by the number of queries already made. Before the next query slot, execute all required query-free steps coherently on each history until it either reaches its next query or has halted. The program is finite, so this requires finitely many controlled query-free operations. A halted branch can pass through a query slot unchanged by routing the query register to a dummy state with any fixed valid index and answer $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$. A bit oracle fixes this dummy state for every input. A controlled swap before and after the oracle supplies the routing. Thus all branches can use exactly $q$ slots, while halted branches acquire no change. A nonconstant function has $n\geq1$, so a valid dummy index exists. This is also the content of the supplied deferral bridge, though the subsequent adversary argument is not formalized there in this form.

Let $\psi_x^t$ be the normalized pure state at query time $t$, including all work and history registers. Define

<!-- claim:def-adv-progress -->
\[
W_t=\sum_{x,y}v_xv_y\Gamma_{xy}\langle\psi_x^t\mid\psi_y^t\rangle.
\]

Initially all states are the same input-independent unit vector, so $W_0=v^{\mathsf T}\Gamma v=\|\Gamma\|$. An input-independent unitary preserves every inner product and hence $W_t$. Only queries can change it. Just before a query, decompose the state into its query-index blocks as $\psi_x=\sum_i|i\rangle\phi_{x,i}$. Orthogonality gives $\sum_i\|\phi_{x,i}\|^2=1$. If $x_i=y_i$, the same answer-bit permutation acts on both block vectors and their inner product is unchanged. If $x_i\ne y_i$, the difference of the two inner products has absolute value at most $2\|\phi_{x,i}\|\|\phi_{y,i}\|$: each of the original and transformed inner products is at most that product in absolute value. Put $u_i(x)=v_x\|\phi_{x,i}\|$. Entrywise nonnegativity of the weights and the triangle inequality now give

<!-- claim:claim-per-query -->
\[
|W_{t+1}-W_t|
\leq2\sum_i u_i^{\mathsf T}\Gamma_i u_i
\leq2\max_i\|\Gamma_i\|.
\]

For the last inequality, each quadratic form is at most $\|\Gamma_i\|\|u_i\|^2$, and $\sum_i\|u_i\|^2=\sum_xv_x^2\sum_i\|\phi_{x,i}\|^2=1$. No normalization is performed separately on a zero-probability block.
<!-- /passage:ROOT-ADVERSARY-PROGRESS -->

<a id="ROOT-ADVERSARY-FINAL"></a>
<!-- passage:ROOT-ADVERSARY-FINAL -->
We next bound the overlap of final states on inputs with distinct outputs. Let $\Pi$ denote the final output-one projector. If $f(x)=0$ and $f(y)=1$, put $a=\|\Pi\psi_x\|^2\leq1/3$ and $b=\|\Pi\psi_y\|^2\geq2/3$. Orthogonal decomposition and Cauchy–Schwarz give $|\langle\psi_x|\psi_y\rangle|\leq\sqrt{ab}+\sqrt{(1-a)(1-b)}$. To maximize this expression on the stated rectangle, write $a=\sin^2u$ and $b=\sin^2v$, with $u,v\in[0,\pi/2]$. The expression becomes $\cos(v-u)$. The constraints imply $u\leq\arcsin(1/\sqrt3)$ and $v\geq\arcsin\sqrt{2/3}$. The smallest possible nonnegative angle difference occurs at these two boundaries, and cosine decreases on $[0,\pi/2]$. Therefore

<!-- claim:claim-final-overlap -->
\[
|\langle\psi_x^{\mathrm{final}}\mid\psi_y^{\mathrm{final}}\rangle|
\leq\frac{2\sqrt2}{3},\qquad
|W_{\mathrm{final}}|\leq\frac{2\sqrt2}{3}\|\Gamma\|.
\]

The second bound follows because every nonzero $\Gamma_{xy}$ joins opposite outputs and $\sum_{x,y}v_xv_y\Gamma_{xy}=\|\Gamma\|$. In particular, a fraction at least $1-2\sqrt2/3>0$ of the initial progress must be lost. Summing the per-query bound over $q$ queries proves the following lemma, with $c=(1-2\sqrt2/3)/2$.

<!-- claim:lem-A.2 -->
\[
Q(f)\ \geq\ c\,\frac{\|\Gamma\|}{\max_i\|\Gamma_i\|}
\quad\text{for every nonzero symmetric }\Gamma\geq0
\text{ with }\Gamma_{xy}=0\text{ when }f(x)=f(y).
\]

The denominator is positive. A nonzero entry of $\Gamma$ joins two inputs of opposite function value, hence two distinct inputs; they differ in at least one coordinate, whose mask contains that nonzero entry. The bound therefore involves no division by zero. The spectral adversary method in this form originates with Barnum, Saks and Szegedy [BSS2003](https://doi.org/10.1109/CCC.2003.1214419); Špalek and Szegedy give its equivalent formulations [SpalekSzegedy2006, Section 2 and Theorem 3.1](https://theoryofcomputing.org/articles/v002a001/). The proof above is included so that the particular constants, oracle convention and treatment of adaptive measurements can all be checked directly.

**Evidence.** `QuarticQuery.FixedSim.build` and `QuarticQuery.exists_fixedSequence` in `Bridge/Deferred.lean` check the conversion from adaptive programs to fixed query sequences. They provide only partial support for Lemma A.2. No declaration in the packet proves the displayed progress inequality, overlap inequality or spectral adversary statement in these forms. Their proofs here are prose proofs.
<!-- /passage:ROOT-ADVERSARY-FINAL -->

<a id="ROOT-BS-LAMBDA"></a>
<!-- passage:ROOT-BS-LAMBDA -->
### A.3. Two consequences of the adversary bound

Fix an input $x$ with $b=\operatorname{bs}(f,x)\geq1$ disjoint sensitive blocks $B_1,\ldots,B_b$. Form a graph with center $x$, leaves $x^{B_1},\ldots,x^{B_b}$, and one edge from the center to each leaf. Take its adjacency matrix as $\Gamma$, extending it by zero on all other inputs. The leaves are distinct because the blocks are nonempty and disjoint. Every edge joins opposite values of $f$, so Lemma A.2 applies.

On the span of the center basis vector and the normalized sum of the $b$ leaf vectors, the adjacency matrix is the two-by-two matrix with off-diagonal entries $\sqrt b$. Vectors on the leaves whose coordinates sum to zero lie in its kernel, as do all unused input vectors. Its operator norm is therefore $\sqrt b$. A coordinate $i$ belongs to at most one of the disjoint blocks. Consequently its mask contains either one edge or none. A one-edge adjacency matrix has eigenvalues $1,-1$, and zero on the remaining space, so every coordinate mask has norm at most one. Lemma A.2 gives $Q(f)\geq c\sqrt b$. Maximizing $b$ proves

<!-- claim:lem-A.3.bs -->
\[
\operatorname{bs}(f)\leq c^{-2}Q(f)^2=O(Q(f)^2).
\]

Now let $S_f$ be the adjacency matrix of the graph on all cube inputs whose edges join inputs differing in exactly one bit and having different function values. Define the spectral sensitivity by

<!-- claim:def-Sf -->
\[
\lambda(f)=\|S_f\|.
\]

If $f$ is nonconstant, this graph has an edge: follow a cube path between two inputs of distinct values and take the first step at which the value changes. For a fixed coordinate $i$, the edges differing in coordinate $i$ form a matching, because each input has exactly one neighbor in that coordinate. The corresponding masked matrix is a direct sum of one-edge matrices and zeros, so its norm is at most one. Applying Lemma A.2 with $\Gamma=S_f$ yields

<!-- claim:lem-A.3.lambda -->
\[
\lambda(f)\leq c^{-1}Q(f)=O(Q(f)).
\]

Together these are Lemma A.3 of the preprint. The second estimate is also Lemma 9 of Aaronson, Ben-David, Kothari, Rao and Tal [ABKRT2021](https://arxiv.org/abs/2010.12629). Both inequalities extend to constant functions because all three quantities vanish there.

**Evidence.** The supplied corpus gives no formal ties for Lemma A.3 or its two components. The explicit star and matching arguments above prove them in prose; the formal upper endpoint does not by itself certify these individual inequalities.
<!-- /passage:ROOT-BS-LAMBDA -->

<a id="ROOT-HUANG-RESTRICTION"></a>
<!-- passage:ROOT-HUANG-RESTRICTION -->
### A.4. Degree is bounded by squared spectral sensitivity

Assume $f$ is nonconstant and let $d=\deg(f)\geq1$. Express inputs and outputs as signs. Choose a degree-$d$ monomial with nonzero coefficient and let $S$ be its support. Restrict all other variables to any fixed signs. The coefficient of the full $S$-monomial survives: a term that could contribute to it would have to contain every variable in $S$, and no proper superset has a nonzero coefficient because $d$ is the maximum degree. The resulting sign-valued function $g$ on a $d$-dimensional subcube has nonzero coefficient on the product of all its variables.

The sign monomials are orthogonal under the uniform measure: the expectation of a nonempty product of independent uniform signs is zero, and the empty product has expectation one. Multiplying the polynomial for $g$ by the full product and averaging therefore extracts exactly its top coefficient. Thus $g$ has nonzero correlation with parity. Choose $\sigma\in\{-1,1\}$ with the sign of that correlation. Since both $g$ and $\sigma x_1\cdots x_d$ take signs, their product is $1$ when they agree and $-1$ when they disagree. Positive mean means agreement on more than half the inputs. Consequently

<!-- claim:claim-restrict-parity -->
\[
U=\{x\in\{-1,1\}^d:g(x)=\sigma x_1\cdots x_d\},\qquad
|U|>2^{d-1}.
\]

Every cube edge with both endpoints in $U$ changes $g$: parity changes on one-coordinate flips, and $g$ agrees with the same signed parity at both endpoints.
<!-- /passage:ROOT-HUANG-RESTRICTION -->

<a id="ROOT-HUANG-SPECTRUM"></a>
<!-- passage:ROOT-HUANG-SPECTRUM -->
Define a signed adjacency matrix for the $j$-cube recursively by

<!-- claim:def-huang -->
\[
H'_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
H'_{j+1}=\begin{pmatrix}H'_j&I\\I&-H'_j\end{pmatrix}.
\]

Each matrix is real symmetric. Its entrywise absolute value is the ordinary cube adjacency matrix: the diagonal blocks describe the two $j$-dimensional faces, and the identity blocks join corresponding vertices across the new coordinate. This is Huang's signed cube [Huang2019, Lemma 2.2 and the proof of Theorem 1.1](https://annals.math.princeton.edu/2019/190-3/p06).

Squaring the block matrix cancels the off-diagonal blocks and adds $I$ to the square of each diagonal block. Starting with $(H'_1)^2=I$, induction proves $(H'_j)^2=jI$. Its trace is zero, first by the base case and then by cancellation of the two diagonal blocks. A real symmetric eigenvalue $\theta$ must satisfy $\theta^2=j$, so it equals $\sqrt j$ or $-\sqrt j$. For $j\geq1$, trace zero makes their multiplicities equal. We have proved

<!-- claim:claim-huang-spectrum -->
\[
(H'_j)^2=jI,\qquad
\operatorname{spec}(H'_j)=\{+\sqrt j,-\sqrt j\},
\quad\text{each with multiplicity }2^{j-1}.
\]

The positive eigenspace of $H'_d$ has dimension $2^{d-1}$. The coordinate subspace consisting of vectors supported on $U$ has dimension $|U|>2^{d-1}$. In a vector space of dimension $2^d$, the dimension formula for the sum of two subspaces makes their intersection nonzero. Choose a nonzero real vector $v$ in this intersection and put $u=|v|$. Let $A_U$ denote the cube adjacency matrix restricted to $U$, extended by zero on its complement. Because $v$ is supported on $U$, termwise absolute values and the entrywise identity $|H'_d|=A_{\mathrm{cube}}$ yield

<!-- claim:claim-interlace -->
\[
u^{\mathsf T}A_Uu\geq v^{\mathsf T}H'_dv
=\sqrt d\,\|v\|^2=\sqrt d\,\|u\|^2.
\]

This is a dimension argument for the needed spectral comparison; no separate interlacing theorem is required. The vector $u$ is nonzero and nonnegative. Every edge of $A_U$ is an edge of the sensitivity graph of $g$, so replacing $A_U$ by that graph's adjacency matrix only increases its quadratic form on $u$. Embed $u$ into the original $n$-cube by setting all coordinates outside the chosen subcube to zero. Its norm is unchanged, and the quadratic form of $S_f$ on the embedded vector contains exactly the contributions of the restricted graph. The operator norm of $S_f$ is at least this Rayleigh quotient. Therefore $\lambda(f)\geq\sqrt d$, proving

<!-- claim:lem-A.4 -->
\[
\deg(f)\leq\lambda(f)^2.
\]

For a constant function, both sides are zero. The proof is the spectral consequence of Huang's construction used by Aaronson, Ben-David, Kothari, Rao and Tal [ABKRT2021, Theorem 1 and Section 3](https://arxiv.org/abs/2010.12629). Huang's paper proves the underlying signed-matrix estimate and identifies its spectral strength [Huang2019, remark after Theorem 1.1](https://annals.math.princeton.edu/2019/190-3/p06).

**Evidence.** The restriction, parity, signed-cube, spectrum and subspace claims have no formal ties in the supplied corpus. They are proved here in prose. They also explain explicitly why the argument controls spectral sensitivity, which is the quantity needed for the quantum bound.
<!-- /passage:ROOT-HUANG-SPECTRUM -->

<a id="ROOT-MONOMIAL-TREE"></a>
<!-- passage:ROOT-MONOMIAL-TREE -->
### A.5. A deterministic tree with at most $\operatorname{bs}(f)\deg(f)$ queries

The following algorithm is due to Midrijānis [Midrijanis2004, Lemma 3 and the proof of Theorem 4](https://arxiv.org/abs/quant-ph/0403168). Maintain the restriction of $f$ specified by the answers already queried. If it is constant, output that constant. Otherwise choose any monomial of greatest degree in the current multilinear polynomial and query all coordinates in its support. Update the restriction and repeat. Choices among monomials can be fixed in advance, so this is a deterministic algorithm. Each nonconstant round queries a nonempty set of previously unqueried variables; termination is therefore guaranteed.

Fix a complete input $x$, and consider one round on its execution path. Let $S$ be the support selected in that round. In the current restriction, additionally fix every still-unqueried variable outside $S$ to its value in $x$. The coefficient of the full $S$-monomial remains nonzero. Indeed, only a monomial containing all of $S$ could contribute to that coefficient, and maximal degree excludes a nonzero strict superset. The resulting function of $S$ is nonconstant, because its representing polynomial has a nonzero coefficient on a nonempty monomial.

A nonconstant Boolean function takes both output values. Hence there exists an assignment to $S$ whose output differs from the value at the assignment $x|_S$. Let $B$ be the coordinates where this assignment differs from $x|_S$. Then $B\subseteq S$ is nonempty. The previous queried variables and all other unqueried variables have been fixed to their values in the original input $x$, so flipping $B$ in the original $x$ changes the original $f(x)$. Thus $B$ is a sensitive block at the same original input. Blocks obtained in different rounds are disjoint because their queried supports are disjoint. This proves `claim-round-block` with its dependence on the original input made explicit.

There can be at most $\operatorname{bs}(f,x)$ rounds on this path. Restricting variables does not increase degree: substituting constants can only delete variables from monomials or cancel terms. Each round therefore queries at most $\deg(f)$ variables. The number of queries on input $x$ is at most $\operatorname{bs}(f,x)\deg(f)\leq\operatorname{bs}(f)\deg(f)$. Taking the maximum over all inputs proves

<!-- claim:lem-A.5 -->
\[
D(f)\leq\operatorname{bs}(f)\deg(f).
\]

If $f$ is constant, the algorithm stops immediately, and the inequality is again valid. The cited theorem's stated endpoint is a cubic bound in degree; the product bound used here is established inside its proof. This locator prevents crediting that theorem with a different literal statement.

**Evidence.** `claim-round-block` and `lem-A.5` have no formal tie in the supplied corpus. The complete algorithm and its per-input sensitive-block charging argument are the prose proof given here.
<!-- /passage:ROOT-MONOMIAL-TREE -->

<a id="ROOT-QUARTIC-UPPER"></a>
<!-- passage:ROOT-QUARTIC-UPPER -->
### A.6. Combining the estimates

For nonconstant total $f$, Lemma A.3 gives $\operatorname{bs}(f)\leq c^{-2}Q(f)^2$ and $\lambda(f)\leq c^{-1}Q(f)$. Lemma A.4 then gives $\deg(f)\leq c^{-2}Q(f)^2$. Substitution into Lemma A.5 gives $D(f)\leq c^{-4}Q(f)^4$. A deterministic algorithm is also a randomized one, so $R(f)\leq D(f)$. Constant functions have $D=R=Q=0$, hence satisfy the same bound. In particular,

<!-- claim:thm-A.1 -->
\[
R(f)\leq D(f)=O\bigl((1+Q(f))^4\bigr)
\qquad\text{for every total Boolean function }f,
\]

with one absolute constant, independent of both $f$ and its number of variables. This places $4$ in the admissible set defining $\alpha_{\mathrm{tot}}$ and completes the proof of Theorem 1.1.

**Evidence.** The same endpoint is checked by an alternative route in `QuarticQuery.D_le_of_QLe`, `D_le_Q_pow_four`, `R_le_D_le_one_add_Q_pow_four` and `universalPower_four`. Its explicit constant $20736$ is the one proved by the imported `Cslib.Quantum.complexity_le_mul_pow_four` route; the elementary adversary constants used in this appendix are not claimed to recover that numerical value. The imported dependency is pinned in the packet's `lake-manifest.json`. Its full source and a runnable Lean installation were not part of this reconstruction's available local environment, so the claim about that imported theorem is based on the checked-source record and its explicit use in the supplied file.
<!-- /passage:ROOT-QUARTIC-UPPER -->



## Appendix B. Exact statement catalogue and source correspondence


<a id="ROOT-CATALOGUE-INTRO"></a>
<!-- passage:ROOT-CATALOGUE-INTRO -->
This catalogue reproduces the original corpus statements without rewriting their text. Each entry points back to the passages that define, prove or explain it. Its evidence fields are those supplied by the original corpus, not new judgments or executions. The local evidence notes and LEAN_GAPS.md identify partial matches, alternative routes and corrections. Source paths are relative to the repository in the supplied packet. Mathematical changes and additional displayed claims remain separate in the two statement registries.
<!-- /passage:ROOT-CATALOGUE-INTRO -->


### def-log-convention


<a id="CAT-def-log-convention"></a>
<!-- passage:CAT-def-log-convention -->
<!-- claim:def-log-convention -->

> log means log_2, except where changing the base only changes an absolute constant. Ledger pinning: log in T (prop-3.2), r and l (eq-6) and L (eq-5) is exactly log_2.

**Mathematical passages:** [ROOT-LOGS](#ROOT-LOGS).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-log-convention -->


### def-partial-query


<a id="CAT-def-partial-query"></a>
<!-- passage:CAT-def-partial-query -->
<!-- claim:def-partial-query -->

> A partial Boolean function is a pair (D,P) with D a subset of {0,1}^N and P:D->{0,1}. An algorithm computes it if it is correct, with the stated error, on every x in D; behaviour off D is unconstrained.

**Mathematical passages:** [ROOT-PARTIAL](#ROOT-PARTIAL).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=outside.

**Original declaration ties:**

- `QuarticQuery.RLe_reindex_iff`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 335.
- `QuarticQuery.DLe_reindex_iff`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 344.
<!-- /passage:CAT-def-partial-query -->


### def-R


<a id="CAT-def-R"></a>
<!-- passage:CAT-def-R -->
<!-- claim:def-R -->

> For a (partial) Boolean function f, R(f) is the least q such that some probability distribution on deterministic decision trees of depth at most q satisfies Pr[T(x)=f(x)] >= 2/3 for every x in dom f. The query cap holds on every branch and every coin outcome.

**Mathematical passages:** [ROOT-PARTIAL](#ROOT-PARTIAL).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.DLe.toRLe`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 244.
- `QuarticQuery.RLe_R`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 264.
- `QuarticQuery.R_le_iff`: relation exact, route none; `lean/QuarticQuery/Model/Classical.lean`, line 278.
- `QuarticQuery.lt_R_iff`: relation exact, route none; `lean/QuarticQuery/Model/Classical.lean`, line 299.
- `QuarticQuery.lt_R_of_not_RLe`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 308.
- `QuarticQuery.R_reindex`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 353.
<!-- /passage:CAT-def-R -->


### def-query-oracle


<a id="CAT-def-query-oracle"></a>
<!-- passage:CAT-def-query-oracle -->
<!-- claim:def-query-oracle -->

> For x in {0,1}^n the bit oracle is the unitary O_x|i,b,z> = |i, b xor x_i, z>, with i in [n], b a bit, z a workspace label. It is self-inverse.

**Mathematical passages:** [ROOT-ORACLE](#ROOT-ORACLE).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.hadamardL`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 43.
- `QuarticQuery.hadamardL_hadamardL`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 60.
- `QuarticQuery.norm_hadamardL`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 76.
- `QuarticQuery.hadamard`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 88.
- `QuarticQuery.hadamard_hadamard`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 95.
- `QuarticQuery.hadamard_phaseOracle_hadamard`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 101.
- `QuarticQuery.hadamard_bitOracle_hadamard`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 115.
- `QuarticQuery.bitRun`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 120.
- `QuarticQuery.phaseGates`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 127.
- `QuarticQuery.run_phaseGates`: relation partial, route none; `lean/QuarticQuery/Bridge/Oracle.lean`, line 134.
- `QuarticQuery.bitOracleL`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 58.
- `QuarticQuery.bitOracle_add`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 68.
- `QuarticQuery.bitOracle_smul`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 73.
- `QuarticQuery.norm_bitOracle`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 78.
- `QuarticQuery.bitOracle_bitOracle`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 83.
<!-- /passage:CAT-def-query-oracle -->


### def-Q


<a id="CAT-def-Q"></a>
<!-- passage:CAT-def-Q -->
<!-- claim:def-Q -->

> Q(f) is the least q such that some quantum algorithm, with unrestricted query-free computation between uses of O_x and with at most q queries on every branch including all measurement outcomes, outputs f(x) with probability >= 2/3 for every x in dom f.

**Mathematical passages:** [ROOT-ORACLE](#ROOT-ORACLE).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.AdaptiveProgram.outputMass_nonneg`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 135.
- `QuarticQuery.AdaptiveProgram.outputMass_true_add_false`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 146.
- `QuarticQuery.Q_le_of_QLe`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 190.
- `QuarticQuery.QLe.reindex`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 257.
- `QuarticQuery.QLe_reindex_iff`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 267.
- `QuarticQuery.Q_reindex`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 276.
- `QuarticQuery.DLe.toQLe`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 390.
- `QuarticQuery.QLe_card`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 402.
- `QuarticQuery.QLe_Q`: relation partial, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 410.
- `QuarticQuery.Q_le_iff`: relation exact, route none; `lean/QuarticQuery/Model/Quantum.lean`, line 414.
- `QuarticQuery.Upper.Runs`: relation partial, route none; `lean/QuarticQuery/Upper/Compile.lean`, line 331.
- `QuarticQuery.Upper.Runs.bind`: relation partial, route none; `lean/QuarticQuery/Upper/Compile.lean`, line 354.
- `QuarticQuery.Upper.Runs.toQLePartial`: relation partial, route none; `lean/QuarticQuery/Upper/Compile.lean`, line 373.
- `QuarticQuery.Upper.Runs.toQLe`: relation partial, route none; `lean/QuarticQuery/Upper/Compile.lean`, line 386.
<!-- /passage:CAT-def-Q -->


### eq-1


<a id="CAT-eq-1"></a>
<!-- passage:CAT-eq-1 -->
<!-- claim:eq-1 -->

> alpha_tot = inf{alpha >= 0 : exists C_alpha < infinity such that for every n >= 1 and every total f:{0,1}^n->{0,1}, R(f) <= C_alpha (1+Q(f))^alpha}.

**Mathematical passages:** [ROOT-RESULT](#ROOT-RESULT).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-eq-1 -->


### eq-2


<a id="CAT-eq-2"></a>
<!-- passage:CAT-eq-2 -->
<!-- claim:eq-2 -->

> For fixed integer k>=2 and all sufficiently large powers of four m: Q(F_{k,m}) <= C_k sqrt(m) (log m)^{b_k} and R(F_{k,m}) >= c_k m^{2-1/k}/(log m)^2, with c_k,C_k,b_k>0 depending only on k.

**Mathematical passages:** [ROOT-RESULT](#ROOT-RESULT), [ROOT-ARCHITECTURE](#ROOT-ARCHITECTURE), [ROOT-FAMILY-ASSEMBLY](#ROOT-FAMILY-ASSEMBLY).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.family_bounds`: relation partial, route same; `lean/QuarticQuery/Results/Conditional.lean`, line 25.
- `QuarticQuery.familyBounds_of_bansalSinha`: relation partial, route same; `lean/QuarticQuery/Results/Conditional.lean`, line 38.
- `QuarticQuery.familyBoundsAt_of_parts`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 416.
- `QuarticQuery.Upper.familyBoundsAt_of_lower`: relation partial, route same; `lean/QuarticQuery/Upper/Bound.lean`, line 265.
<!-- /passage:CAT-eq-2 -->


### thm-1.1


<a id="CAT-thm-1.1"></a>
<!-- passage:CAT-thm-1.1 -->
<!-- claim:thm-1.1 -->

> alpha_tot = 4. More precisely, R(f) = O((1+Q(f))^4) for every total Boolean f, and eq-2 holds for each fixed integer k>=2.

**Mathematical passages:** [ROOT-RESULT](#ROOT-RESULT), [ROOT-ARCHITECTURE](#ROOT-ARCHITECTURE), [ROOT-EVIDENCE-CONVENTION](#ROOT-EVIDENCE-CONVENTION), [ROOT-FAMILY-ASSEMBLY](#ROOT-FAMILY-ASSEMBLY), [ROOT-NO-SMALLER](#ROOT-NO-SMALLER).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=alternative; reach=reached.

**Original declaration ties:**

- `QuarticQuery.alphaTot_eq_four_of_bansalSinha`: relation partial, route same; `lean/QuarticQuery/Results/Conditional.lean`, line 47.
- `QuarticQuery.theorem_1_1`: relation unassessed, route unassessed; `lean/QuarticQuery/Results/Conditional.lean`, line 53.
- `QuarticQuery.alphaTot_eq_four_of`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 243.
- `QuarticQuery.alphaTot_eq_four`: relation partial, route same; `lean/QuarticQuery/Results/Headline.lean`, line 21.
- `QuarticQuery.alphaTot_eq_four_unconditional`: relation partial, route alternative; `lean/QuarticQuery/Results/Unconditional.lean`, line 18.
- `QuarticQuery.theorem_1_1_unconditional`: relation exact, route alternative; `lean/QuarticQuery/Results/Unconditional.lean`, line 23.
<!-- /passage:CAT-thm-1.1 -->


### cor-cubic-refuted


<a id="CAT-cor-cubic-refuted"></a>
<!-- passage:CAT-cor-cubic-refuted -->
<!-- claim:cor-cubic-refuted -->

> It is false that R(f) = O(Q(f)^3) for all total Boolean f ([3, Conjecture 2]): no C satisfies R(f) <= C Q(f)^3 for all total f.

**Mathematical passages:** [ROOT-RESULT](#ROOT-RESULT), [ROOT-NO-SMALLER](#ROOT-NO-SMALLER).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.cubic_bound_fails_of_bansalSinha`: relation exact, route same; `lean/QuarticQuery/Results/Conditional.lean`, line 65.
- `QuarticQuery.cubic_refuted`: relation stronger, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 257.
- `QuarticQuery.cubic_refuted_bare`: relation exact, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 275.
- `QuarticQuery.cubic_bound_fails`: relation exact, route same; `lean/QuarticQuery/Results/Headline.lean`, line 33.
- `QuarticQuery.cubic_bound_fails_unconditional`: relation exact, route same; `lean/QuarticQuery/Results/Unconditional.lean`, line 42.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-cor-cubic-refuted -->


### def-walsh-sign


<a id="CAT-def-walsh-sign"></a>
<!-- passage:CAT-def-walsh-sign -->
<!-- claim:def-walsh-sign -->

> m=4^t. H is the m x m normalized Walsh-Hadamard matrix, H_{a,b}=m^{-1/2}(-1)^{<a,b>} for a,b in {0,1}^{log_2 m}. u=m^{-1/2}(1,...,1)^T. A bit a is identified with the sign (-1)^a. For z in {+-1}^m, D_z=diag(z).

**Mathematical passages:** [forr_definition](#forr_definition).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.walshN`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 21.
- `QuarticQuery.Forrelation.sum_walshN_mul`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 83.
- `QuarticQuery.Forrelation.walshZ`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 130.
- `QuarticQuery.Forrelation.W`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 134.
- `QuarticQuery.Forrelation.walshZ_mul_transpose`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 158.
- `QuarticQuery.Forrelation.W_mul_transpose`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 180.
<!-- /passage:CAT-def-walsh-sign -->


### eq-3


<a id="CAT-eq-3"></a>
<!-- passage:CAT-eq-3 -->
<!-- claim:eq-3 -->

> For z_1,...,z_k in {+-1}^m: Phi(z_1,...,z_k) = u^T D_{z_1} H D_{z_2} H ... H D_{z_k} u (k diagonals, k-1 copies of H), and delta = 2^{-5k}.

**Mathematical passages:** [forr_definition](#forr_definition).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.u`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 88.
- `QuarticQuery.Forrelation.signDiag`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 91.
- `QuarticQuery.Forrelation.alternate`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 104.
- `QuarticQuery.Forrelation.Phi_eq_matrix_product`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 158.
- `QuarticQuery.Forrelation.Phi_sq_le_one`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 259.
- `QuarticQuery.Forrelation.abs_Phi_le_one`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 266.
- `QuarticQuery.Forrelation.delta`: relation partial, route none; `lean/QuarticQuery/Forrelation/Promise.lean`, line 18.
- `QuarticQuery.Forrelation.H`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 139.
- `QuarticQuery.Forrelation.H_mul_H`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 200.
- `QuarticQuery.Forrelation.H_mem_orthogonalGroup`: relation partial, route none; `lean/QuarticQuery/Forrelation/Walsh.lean`, line 210.
<!-- /passage:CAT-eq-3 -->


### eq-4


<a id="CAT-eq-4"></a>
<!-- passage:CAT-eq-4 -->
<!-- claim:eq-4 -->

> P=P_{k,m} is the partial function on km bits with P=1 if Phi>=delta, P=0 if |Phi|<=delta/2, undefined otherwise. The two cases are disjoint.

**Mathematical passages:** [forr_definition](#forr_definition).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.cases_disjoint`: relation partial, route none; `lean/QuarticQuery/Forrelation/Promise.lean`, line 55.
- `QuarticQuery.Forrelation.P_eq_some_true_iff`: relation partial, route none; `lean/QuarticQuery/Forrelation/Promise.lean`, line 63.
- `QuarticQuery.Forrelation.P_eq_some_false_iff`: relation partial, route none; `lean/QuarticQuery/Forrelation/Promise.lean`, line 70.
- `QuarticQuery.Forrelation.P_eq_none_iff`: relation partial, route none; `lean/QuarticQuery/Forrelation/Promise.lean`, line 87.
- `QuarticQuery.Forrelation.P_eq_cases`: relation partial, route none; `lean/QuarticQuery/Forrelation/Promise.lean`, line 95.
- `QuarticQuery.Forrelation.census_true`: relation partial, route none; `lean/QuarticQuery/Forrelation/Sanity.lean`, line 20.
- `QuarticQuery.Forrelation.census_false`: relation partial, route none; `lean/QuarticQuery/Forrelation/Sanity.lean`, line 25.
- `QuarticQuery.Forrelation.census_none`: relation partial, route none; `lean/QuarticQuery/Forrelation/Sanity.lean`, line 30.
- `QuarticQuery.Forrelation.promise_nonempty_two_one`: relation partial, route none; `lean/QuarticQuery/Forrelation/Sanity.lean`, line 41.
- `QuarticQuery.Forrelation.Phi_negativeWitness`: relation partial, route none; `lean/QuarticQuery/Forrelation/Sanity.lean`, line 58.
- `QuarticQuery.Forrelation.P_negativeWitness`: relation partial, route none; `lean/QuarticQuery/Forrelation/Sanity.lean`, line 65.
<!-- /passage:CAT-eq-4 -->


### eq-5


<a id="CAT-eq-5"></a>
<!-- passage:CAT-eq-5 -->
<!-- claim:eq-5 -->

> L = L_{k,m} = floor(m^{1-1/k}/(log_2 m)^2).

**Mathematical passages:** [forr_definition](#forr_definition).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-eq-5 -->


### claim-bs-to-L


<a id="CAT-claim-bs-to-L"></a>
<!-- passage:CAT-claim-bs-to-L -->
<!-- claim:claim-bs-to-L -->

> For fixed k: for large m, c k^{-29} (m/log(km))^{1-1/k} > floor(m^{1-1/k}/(log_2 m)^2).

**Mathematical passages:** [forr_bs_translation](#forr_bs_translation).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=alternative; reach=reached.

**Original declaration ties:**

- `QuarticQuery.ForrelationLower.bansalSinhaLower`: relation exact, route alternative; `lean/QuarticQuery/Statement.lean`, line not supplied.

**Reviewed metadata correction:** the theorem `QuarticQuery.ForrelationLower.bansalSinhaLower` is in `lean/QuarticQuery/ForrelationLower/Main.lean`. It proves the eventual lower-bound endpoint. It does not state the isolated numerical Bansal–Sinha comparison.
<!-- /passage:CAT-claim-bs-to-L -->


### lem-2.1.i


<a id="CAT-lem-2.1.i"></a>
<!-- passage:CAT-lem-2.1.i -->
<!-- claim:lem-2.1.i -->

> For fixed k>=2 and all sufficiently large powers of four m, R(P_{k,m})>L with L as in eq-5.

**Mathematical passages:** [forr_threshold](#forr_threshold), [forr_attribution](#forr_attribution), [forr_bundle](#forr_bundle).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=alternative; reach=reached.

**Original declaration ties:**

- `QuarticQuery.ForrelationLower.bansalSinhaLower`: relation exact, route alternative; `lean/QuarticQuery/Statement.lean`, line not supplied.

**Reviewed metadata correction:** the theorem `QuarticQuery.ForrelationLower.bansalSinhaLower` is in `lean/QuarticQuery/ForrelationLower/Main.lean`. It proves the eventual lower-bound endpoint. It does not state the isolated numerical Bansal–Sinha comparison.
<!-- /passage:CAT-lem-2.1.i -->


### claim-proj-prob


<a id="CAT-claim-proj-prob"></a>
<!-- passage:CAT-claim-proj-prob -->
<!-- claim:claim-proj-prob -->

> Prepare u, apply D_{z_1} H ... H D_{z_k} right to left, measure the projection onto u. Each D uses one bit query (phase kickback), H and the projection use none. Success probability is exactly Phi^2: >=delta^2 on 1-inputs, <=delta^2/4 on 0-inputs.

**Mathematical passages:** [forr_quantum](#forr_quantum).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.successProb`: relation partial, route none; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 28.
- `QuarticQuery.Forrelation.successProb_eq`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 32.
- `QuarticQuery.Forrelation.failureProb_eq`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 40.
- `QuarticQuery.Forrelation.successProb_of_true`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 61.
- `QuarticQuery.Forrelation.successProb_of_false`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 67.
- `QuarticQuery.Upper.forr_samples`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 309.
<!-- /passage:CAT-claim-proj-prob -->


### lem-2.1.ii


<a id="CAT-lem-2.1.ii"></a>
<!-- passage:CAT-lem-2.1.ii -->
<!-- claim:lem-2.1.ii -->

> For every 0<eta<1/2 there is a quantum algorithm using O_k(1+log(1/eta)) bit queries that outputs P_{k,m}(z) with error <=eta for every z in dom P. It has a coherent implementation retaining all workspace. On every input, promised or not, measuring its output register yields a bit.

**Mathematical passages:** [forr_quantum](#forr_quantum), [forr_bundle](#forr_bundle), [upper-decode](#upper-decode), [upper-decode-cost](#upper-decode-cost).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.binomTail_small`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 141.
- `QuarticQuery.Forrelation.binomTail_large`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 160.
- `QuarticQuery.Forrelation.repetitions`: relation partial, route none; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 192.
- `QuarticQuery.Forrelation.repetitions_le`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 196.
- `QuarticQuery.Forrelation.threshold_correct`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 218.
- `QuarticQuery.Forrelation.threshold_correct_third`: relation partial, route same; `lean/QuarticQuery/Forrelation/Repetition.lean`, line 234.
- `QuarticQuery.Upper.Samples.count`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 56.
- `QuarticQuery.Upper.Samples.threshold`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 115.
- `QuarticQuery.Upper.Samples.pi`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 150.
- `QuarticQuery.Upper.hGate`: relation partial, route none; `lean/QuarticQuery/Upper/Decode.lean`, line 237.
- `QuarticQuery.Upper.forr_samples`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 309.
- `QuarticQuery.Upper.decode_samples`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 361.
- `QuarticQuery.Upper.decodeProb_correct`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 371.
- `QuarticQuery.Upper.P_runs`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 386.
- `QuarticQuery.Upper.P_QLe`: relation partial, route same; `lean/QuarticQuery/Upper/Decode.lean`, line 394.
<!-- /passage:CAT-lem-2.1.ii -->


### claim-N-phi


<a id="CAT-claim-N-phi"></a>
<!-- passage:CAT-claim-N-phi -->
<!-- claim:claim-N-phi -->

> With W=sqrt(m) H (entries +-1), N = z_1^T W D_{z_2} W ... W D_{z_k} (1,...,1)^T is an integer, Phi=N/M_{k,m}, and M_{k,m}=m (sqrt m)^{k-1} is a positive integer because m is a power of four.

**Mathematical passages:** [forr_integer](#forr_integer).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.layers`: relation partial, route none; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 92.
- `QuarticQuery.Forrelation.walkN`: relation partial, route none; `lean/QuarticQuery/Forrelation/Product.lean`, line 22.
- `QuarticQuery.Forrelation.numerator_eq_walk`: relation partial, route same; `lean/QuarticQuery/Forrelation/Product.lean`, line 71.
- `QuarticQuery.Forrelation.Phi_eq_matrix_product`: relation partial, route same; `lean/QuarticQuery/Forrelation/Product.lean`, line 158.
<!-- /passage:CAT-claim-N-phi -->


### claim-integer-tests


<a id="CAT-claim-integer-tests"></a>
<!-- passage:CAT-claim-integer-tests -->
<!-- claim:claim-integer-tests -->

> Phi>=delta iff 2^{5k} N >= M_{k,m}; and |Phi|<=delta/2 iff 2^{5k+1}|N| <= M_{k,m}. d is the disjunction, b the first comparison.

**Mathematical passages:** [forr_integer](#forr_integer).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.P_tests`: relation partial, route same; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 238.
- `QuarticQuery.Forrelation.forrCore_spec`: relation partial, route same; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 273.
- `QuarticQuery.Forrelation.delta_le_Phi_iff`: relation partial, route same; `lean/QuarticQuery/Forrelation/Promise.lean`, line 33.
- `QuarticQuery.Forrelation.abs_Phi_le_iff`: relation partial, route same; `lean/QuarticQuery/Forrelation/Promise.lean`, line 43.
<!-- /passage:CAT-claim-integer-tests -->


### claim-circuit-size


<a id="CAT-claim-circuit-size"></a>
<!-- passage:CAT-claim-circuit-size -->
<!-- claim:claim-circuit-size -->

> N is computed by k-1 unnormalized Walsh-Hadamard transforms, coordinate sign changes and a final signed sum. Each transform uses O(m log m) additions and subtractions; all intermediate integers have absolute value at most m^{O(k)}, so O_k(log m) bits suffice; hence Boolean size O_k(m (log m)^2).

**Mathematical passages:** [forr_circuit](#forr_circuit).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.abs_numerator_le`: relation partial, route same; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 203.
<!-- /passage:CAT-claim-circuit-size -->


### lem-2.1.iii


<a id="CAT-lem-2.1.iii"></a>
<!-- passage:CAT-lem-2.1.iii -->
<!-- claim:lem-2.1.iii -->

> There is a Boolean circuit C=C_{k,m} of fan-in at most two and size S=S_{k,m}=O_k(m (log m)^2), counting non-input gates, with output bits d,b such that for every input z: d=1 iff P_{k,m} is defined at z, and d=1 implies b=P_{k,m}(z). The circuit computes these outputs exactly on every input.

**Mathematical passages:** [forr_circuit](#forr_circuit), [forr_bundle](#forr_bundle).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Forrelation.realises_of_run`: relation partial, route none; `lean/QuarticQuery/Forrelation/Builder.lean`, line 231.
- `QuarticQuery.Forrelation.forrCircuit`: relation partial, route none; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 337.
- `QuarticQuery.Forrelation.forrCircuit_realises`: relation partial, route same; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 343.
- `QuarticQuery.Forrelation.forrConstant`: relation partial, route none; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 389.
- `QuarticQuery.Forrelation.forrCircuit_size_le`: relation partial, route same; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 466.
- `QuarticQuery.Forrelation.exists_circuit`: relation stronger, route same; `lean/QuarticQuery/Forrelation/Circuit.lean`, line 479.
<!-- /passage:CAT-lem-2.1.iii -->


### lem-2.1


<a id="CAT-lem-2.1"></a>
<!-- passage:CAT-lem-2.1 -->
<!-- claim:lem-2.1 -->

> Conjunction of lem-2.1.i, lem-2.1.ii and lem-2.1.iii for each fixed k>=2.

**Mathematical passages:** [forr_bundle](#forr_bundle).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-2.1 -->


### def-transcript


<a id="CAT-def-transcript"></a>
<!-- passage:CAT-def-transcript -->
<!-- claim:def-transcript -->

> For a fixed circuit, a transcript assigns a proposed bit to each non-input gate, including output gates. Input-wire values are not copied; they are read from the actual input.

**Mathematical passages:** [CL-transcripts](#CL-transcripts).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=outside.

**Original declaration ties:**

- `QuarticQuery.GateConsistent.unique`: relation partial, route none; `lean/QuarticQuery/Construction/Transcript.lean`, line 30.
- `QuarticQuery.existsUnique_gateConsistent`: relation partial, route none; `lean/QuarticQuery/Construction/Transcript.lean`, line 70.
<!-- /passage:CAT-def-transcript -->


### eq-6


<a id="CAT-eq-6"></a>
<!-- passage:CAT-eq-6 -->
<!-- claim:eq-6 -->

> r = ceil(20 log_2 m), l = log_2 m.

**Mathematical passages:** [CL-layout](#CL-layout).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.logb_mValue`: relation partial, route none; `lean/QuarticQuery/Results/Exponent.lean`, line 301.
<!-- /passage:CAT-eq-6 -->


### def-column-layout


<a id="CAT-def-column-layout"></a>
<!-- passage:CAT-def-column-layout -->
<!-- claim:def-column-layout -->

> The input has m columns. Column i contains: X_i in {0,1}^m; strings A_{i,1},...,A_{i,r} in {0,1}^{km} with no promise; and for each s in {0,1}^r a cell B_{i,s} holding, for each j != i, a pointer p_{i,s,j} in [m] encoded in l bits by a fixed bijection, and for each h in [r] an alleged evaluation transcript of C_{k,m} on A_{i,h}.

**Mathematical passages:** [CL-construction-context](#CL-construction-context), [CL-layout](#CL-layout).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=outside.

**Original declaration ties:**

- `QuarticQuery.pointerEquiv_bijective`: relation partial, route none; `lean/QuarticQuery/Construction/Winner.lean`, line 26.
- `QuarticQuery.existsUnique_pointer`: relation partial, route none; `lean/QuarticQuery/Construction/Winner.lean`, line 31.
<!-- /passage:CAT-def-column-layout -->


### def-eval-transcript


<a id="CAT-def-eval-transcript"></a>
<!-- passage:CAT-def-eval-transcript -->
<!-- claim:def-eval-transcript -->

> An evaluation transcript of C_{k,m} on A_{i,h} has one bit per non-input gate including output gates, and these gates are the count S. It is correct iff every bit equals the true value of that gate on input A_{i,h}.

**Mathematical passages:** [CL-transcripts](#CL-transcripts).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=none; reach=outside.

**Original declaration ties:**

- `QuarticQuery.circuitEval_gateConsistent`: relation partial, route none; `lean/QuarticQuery/Construction/Transcript.lean`, line 53.
- `QuarticQuery.gateConsistent_iff_eq_circuitEval`: relation exact, route none; `lean/QuarticQuery/Construction/Transcript.lean`, line 64.
<!-- /passage:CAT-def-eval-transcript -->


### eq-7


<a id="CAT-eq-7"></a>
<!-- passage:CAT-eq-7 -->
<!-- claim:eq-7 -->

> If every P(A_{i,h}) is defined, the true address of column i is s_i=(P(A_{i,1}),...,P(A_{i,r})) in {0,1}^r.

**Mathematical passages:** [CL-address-winner](#CL-address-winner).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=outside.

**Original declaration ties:**

- `QuarticQuery.winsAt_address_unique`: relation partial, route none; `lean/QuarticQuery/Construction/Winner.lean`, line 50.
<!-- /passage:CAT-eq-7 -->


### eq-8


<a id="CAT-eq-8"></a>
<!-- passage:CAT-eq-8 -->
<!-- claim:eq-8 -->

> Outward pointer condition at address s: X_j[p_{i,s,j}] = 0 for every j != i. Eq. 8 of the paper is the case s=s_i.

**Mathematical passages:** [CL-construction-context](#CL-construction-context), [CL-address-winner](#CL-address-winner).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-eq-8 -->


### def-winner


<a id="CAT-def-winner"></a>
<!-- passage:CAT-def-winner -->
<!-- claim:def-winner -->

> Column i is a winner iff X_i=1^m, every P(A_{i,h}) is defined, and the cell B_{i,s_i} contains correct evaluation transcripts on all A_{i,h} and pointers satisfying eq-8.

**Mathematical passages:** [CL-address-winner](#CL-address-winner).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-winner -->


### def-F


<a id="CAT-def-F"></a>
<!-- passage:CAT-def-F -->
<!-- claim:def-F -->

> F_{k,m}(y)=1 if some column of y is a winner, else 0. It is a total Boolean function on all input bit strings.

**Mathematical passages:** [CL-construction-context](#CL-construction-context), [CL-address-winner](#CL-address-winner).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.addressedF_eq_true_iff`: relation exact, route none; `lean/QuarticQuery/Construction/LocalTests.lean`, line 276.
- `QuarticQuery.addressedF_eq_true_iff_localTests`: relation partial, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 281.
- `QuarticQuery.winsAt_column_unique`: relation partial, route none; `lean/QuarticQuery/Construction/Winner.lean`, line 42.
- `QuarticQuery.winsAt_unique`: relation partial, route none; `lean/QuarticQuery/Construction/Winner.lean`, line 55.
<!-- /passage:CAT-def-F -->


### cor-unique-winner


<a id="CAT-cor-unique-winner"></a>
<!-- passage:CAT-cor-unique-winner -->
<!-- claim:cor-unique-winner -->

> For every input, at most one column is a winner.

**Mathematical passages:** [CL-unique](#CL-unique).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-cor-unique-winner -->


### def-win-at-address


<a id="CAT-def-win-at-address"></a>
<!-- passage:CAT-def-win-at-address -->
<!-- claim:def-win-at-address -->

> WinsAt(y,i,s) holds iff X_i=1^m, for every h the transcript in B_{i,s} on A_{i,h} is correct with outputs d=1 and b=s_h, and eq-8 holds at s. The paper's wording, i is a winner and s=s_i, is equivalent by claim-winner-fidelity.

**Mathematical passages:** [CL-fidelity](#CL-fidelity).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-def-win-at-address -->


### def-K


<a id="CAT-def-K"></a>
<!-- passage:CAT-def-K -->
<!-- claim:def-K -->

> K_{k,m} = m + (m-1) + r(S_{k,m}+2) = O_k(m (log m)^3).

**Mathematical passages:** [CL-local-tests](#CL-local-tests), [upper-verifier](#upper-verifier).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.card_testIndex`: relation partial, route none; `lean/QuarticQuery/Construction/LocalTests.lean`, line 132.
<!-- /passage:CAT-def-K -->


### lem-2.2.i


<a id="CAT-lem-2.2.i"></a>
<!-- passage:CAT-lem-2.2.i -->
<!-- claim:lem-2.2.i -->

> For every input y and (i,s) in [m] x {0,1}^r: i wins at s iff all K_{k,m} tests pass, namely (a) X_i[b]=1 for each b; (b) for each j != i, X_j[p_{i,s,j}]=0; (c) for each h and each non-input gate, the claimed value equals the gate function of its predecessors, read from the transcript or from A_{i,h}; (d) for each h, claimed d=1 and claimed b=s_h. Each test is computed by a deterministic adaptive bit-query decision tree of depth at most max(3,l+1), which is l+1 for m>=4: a pointer test reads l pointer bits, then the one target bit they select, while gate tests read at most three fixed bits. A pointer test is not a function of a small fixed set of bits: it can depend on all l+m pointer and target coordinates.

**Mathematical passages:** [CL-local-tests](#CL-local-tests), [CL-local-equivalence](#CL-local-equivalence), [upper-verifier](#upper-verifier).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.TestIndex`: relation partial, route none; `lean/QuarticQuery/Construction/LocalTests.lean`, line 129.
- `QuarticQuery.localTest`: relation partial, route none; `lean/QuarticQuery/Construction/LocalTests.lean`, line 143.
- `QuarticQuery.localTestTree`: relation partial, route none; `lean/QuarticQuery/Construction/LocalTests.lean`, line 174.
- `QuarticQuery.localTestTree_eval`: relation partial, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 193.
- `QuarticQuery.localTestTree_depth_le`: relation partial, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 219.
- `QuarticQuery.winsAt_iff_localTests`: relation partial, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 237.
- `QuarticQuery.exists_failing_localTest`: relation partial, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 268.
- `QuarticQuery.winsAt_iff_outputs`: relation partial, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 287.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-lem-2.2.i -->


### lem-2.2.ii


<a id="CAT-lem-2.2.ii"></a>
<!-- passage:CAT-lem-2.2.ii -->
<!-- claim:lem-2.2.ii -->

> Each test is evaluated exactly with O(log m) bit queries, also coherently with the same bound with test indices in superposition. The number of tests and the indexing convention are the same for every (i,s).

**Mathematical passages:** [CL-local-tests](#CL-local-tests), [CL-coherent-tests](#CL-coherent-tests), [upper-verification-proof](#upper-verification-proof).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.test_samples`: relation partial, route same; `lean/QuarticQuery/Upper/Verify.lean`, line 42.
- `QuarticQuery.Upper.search_runs`: relation partial, route same; `lean/QuarticQuery/Upper/Verify.lean`, line 108.
- `QuarticQuery.Upper.verifyProb`: relation partial, route none; `lean/QuarticQuery/Upper/Verify.lean`, line 127.
<!-- /passage:CAT-lem-2.2.ii -->


### lem-2.2


<a id="CAT-lem-2.2"></a>
<!-- passage:CAT-lem-2.2 -->
<!-- claim:lem-2.2 -->

> Conjunction of lem-2.2.i and lem-2.2.ii.

**Mathematical passages:** [CL-coherent-tests](#CL-coherent-tests).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-2.2 -->


### cor-local-dichotomy


<a id="CAT-cor-local-dichotomy"></a>
<!-- passage:CAT-cor-local-dichotomy -->
<!-- claim:cor-local-dichotomy -->

> A winner has an address at which every test passes; a nonwinner has a failing test at every address.

**Mathematical passages:** [CL-dichotomy](#CL-dichotomy).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-cor-local-dichotomy -->


### def-grover-trial


<a id="CAT-def-grover-trial"></a>
<!-- passage:CAT-def-grover-trial -->
<!-- claim:def-grover-trial -->

> M = ceil(10/sqrt(gamma)). A trial picks with probability 1/2 l=0, and with probability 1/2 a uniform l in {0,...,M-1}, applies l Grover iterations to A|0>, and measures the success bit. The procedure runs ceil(log(1/eta)/log(40/31)) trials with fresh registers, stopping at the first success.

**Mathematical passages:** [upper-grover-trial](#upper-grover-trial).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Amplification.Gate`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 43.
- `QuarticQuery.Amplification.Circuit`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 51.
- `QuarticQuery.Amplification.Circuit.calls`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 60.
- `QuarticQuery.Amplification.groverStep`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 63.
- `QuarticQuery.Amplification.groverCircuit`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 66.
- `QuarticQuery.Amplification.Preparation.grover`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 191.
- `QuarticQuery.Amplification.Proc`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 33.
- `QuarticQuery.Amplification.trialWeight`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 65.
- `QuarticQuery.Amplification.attempts`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 70.
- `QuarticQuery.Amplification.iterationBound`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 76.
- `QuarticQuery.Amplification.trialCount`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 79.
- `QuarticQuery.Amplification.Preparation.trialFail`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 148.
- `QuarticQuery.Amplification.Preparation.trialGain`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 152.
- `QuarticQuery.Amplification.expect_attempts`: relation partial, route same; `lean/QuarticQuery/Amplification/Procedure.lean`, line 163.
- `QuarticQuery.Amplification.attemptValue_eq_sum`: relation partial, route same; `lean/QuarticQuery/Amplification/Procedure.lean`, line 197.
- `QuarticQuery.Amplification.expect_attempts_eq_sum`: relation partial, route same; `lean/QuarticQuery/Amplification/Procedure.lean`, line 209.
- `QuarticQuery.Amplification.Preparation.one_sub_trialFail`: relation partial, route same; `lean/QuarticQuery/Amplification/Procedure.lean`, line 257.
<!-- /passage:CAT-def-grover-trial -->


### claim-grover-state


<a id="CAT-claim-grover-state"></a>
<!-- passage:CAT-claim-grover-state -->
<!-- claim:claim-grover-state -->

> For 0<p<1 write A|0>=sin(theta)|g>+cos(theta)|b>, 0<theta<pi/2, with g,b normalized in the successful and unsuccessful subspaces. After l Grover iterations the state is sin((2l+1)theta)|g>+cos((2l+1)theta)|b>. Hence measuring success yields |g> up to global phase, independently of l.

**Mathematical passages:** [upper-grover-geometry](#upper-grover-geometry).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Amplification.sin_mul_ampA_and_cos_mul_ampB`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 96.
- `QuarticQuery.Amplification.Preparation.iterate`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 194.
- `QuarticQuery.Amplification.Preparation.grover_apply`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 203.
- `QuarticQuery.Amplification.Preparation.grover_parts`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 265.
- `QuarticQuery.Amplification.Preparation.iterate_eq_amp`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 279.
- `QuarticQuery.Amplification.Preparation.angle`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 290.
- `QuarticQuery.Amplification.Preparation.angle_mem`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 311.
- `QuarticQuery.Amplification.Preparation.state_eq`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 324.
- `QuarticQuery.Amplification.Preparation.iterate_eq`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 343.
- `QuarticQuery.Amplification.Preparation.grover_rotation`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 355.
- `QuarticQuery.Amplification.Preparation.good_iterate`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 401.
- `QuarticQuery.Amplification.Preparation.norm_good_iterate_sq`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 407.
- `QuarticQuery.Amplification.Preparation.norm_bad_iterate_sq`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 416.
- `QuarticQuery.Amplification.Preparation.phaseEq_normalised_good_iterate`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 437.
- `QuarticQuery.Amplification.Preparation.good_iterate_of_prob_zero`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 454.
<!-- /passage:CAT-claim-grover-state -->


### claim-sin2theta


<a id="CAT-claim-sin2theta"></a>
<!-- passage:CAT-claim-sin2theta -->
<!-- claim:claim-sin2theta -->

> If gamma<=p<=1/2 then sin(2theta)=2 sqrt(p(1-p)) >= sqrt(gamma).

**Mathematical passages:** [upper-small-probability](#upper-small-probability).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Amplification.Preparation.sin_two_angle`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 462.
<!-- /passage:CAT-claim-sin2theta -->


### eq-9


<a id="CAT-eq-9"></a>
<!-- passage:CAT-eq-9 -->
<!-- claim:eq-9 -->

> If gamma<=p<=1/2 and M=ceil(10/sqrt(gamma)), then (1/M) sum_{l=0}^{M-1} sin^2((2l+1)theta) >= 1/2 - 1/(2M|sin 2theta|) >= 9/20.

**Mathematical passages:** [upper-average-exact](#upper-average-exact), [upper-small-probability](#upper-small-probability).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Amplification.sin_two_mul_sum_sin_sq`: relation partial, route same; `lean/QuarticQuery/Amplification/Average.lean`, line 20.
- `QuarticQuery.Amplification.average_sin_sq`: relation partial, route same; `lean/QuarticQuery/Amplification/Average.lean`, line 41.
- `QuarticQuery.Amplification.average_sin_sq_ge`: relation partial, route same; `lean/QuarticQuery/Amplification/Average.lean`, line 53.
- `QuarticQuery.Amplification.average_sin_sq_ge_nine_twentieths`: relation partial, route same; `lean/QuarticQuery/Amplification/Average.lean`, line 75.
<!-- /passage:CAT-eq-9 -->


### lem-3.1


<a id="CAT-lem-3.1"></a>
<!-- passage:CAT-lem-3.1 -->
<!-- claim:lem-3.1 -->

> For 0<gamma<=1/2 and 0<eta<1/2 there is a single procedure, black-box in A and A^{-1} and with call counts depending only on gamma and eta, using O(gamma^{-1/2} log(1/eta)) calls for every p and on every branch, such that for every state preparation A with a success bit, success probability p and, if p>0, normalized successful state |g>: it reports failure or produces a successful outcome; conditional on success the output is |g> up to global phase; if p>=gamma, failure probability <=eta; if p=0 it always reports failure.

**Mathematical passages:** [upper-amplification-statement](#upper-amplification-statement), [upper-amplification-proof](#upper-amplification-proof).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Amplification.pow_trialCount_le`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 35.
- `QuarticQuery.Amplification.callCap_amplify_le`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 75.
- `QuarticQuery.Amplification.Preparation.nine_fortieths_le`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 127.
- `QuarticQuery.Amplification.Preparation.trialFail_of_prob_zero`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 156.
- `QuarticQuery.Amplification.Proc.successProb`: relation partial, route none; `lean/QuarticQuery/Amplification/Bounded.lean`, line 174.
- `QuarticQuery.Amplification.Proc.failProb`: relation partial, route none; `lean/QuarticQuery/Amplification/Bounded.lean`, line 178.
- `QuarticQuery.Amplification.Proc.conditional`: relation partial, route none; `lean/QuarticQuery/Amplification/Bounded.lean`, line 182.
- `QuarticQuery.Amplification.expect_attempts_of_phase`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 200.
- `QuarticQuery.Amplification.bounded_amplification`: relation exact, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 242.
- `QuarticQuery.Amplification.IndexRegister`: relation partial, route none; `lean/QuarticQuery/Amplification/Bounded.lean`, line 300.
- `QuarticQuery.Amplification.IndexRegister.norm_read_goodState_sq`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 336.
- `QuarticQuery.Amplification.IndexRegister.norm_read_normalised_iterate_sq`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 349.
- `QuarticQuery.Amplification.IndexRegister.index_law_of_amplified`: relation partial, route same; `lean/QuarticQuery/Amplification/Bounded.lean`, line 358.
- `QuarticQuery.Amplification.Preparation`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 33.
- `QuarticQuery.Amplification.calls_groverCircuit`: relation partial, route same; `lean/QuarticQuery/Amplification/Geometry.lean`, line 71.
- `QuarticQuery.Amplification.Preparation.prob`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 148.
- `QuarticQuery.Amplification.Preparation.norm_sq_split`: relation partial, route none; `lean/QuarticQuery/Amplification/Geometry.lean`, line 228.
- `QuarticQuery.Amplification.Proc.callCap`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 42.
- `QuarticQuery.Amplification.Proc.expect`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 54.
- `QuarticQuery.Amplification.amplify`: relation partial, route none; `lean/QuarticQuery/Amplification/Procedure.lean`, line 82.
- `QuarticQuery.Amplification.callCap_attempts`: relation partial, route same; `lean/QuarticQuery/Amplification/Procedure.lean`, line 87.
- `QuarticQuery.Upper.prepOf`: relation partial, route none; `lean/QuarticQuery/Upper/Amplify.lean`, line 49.
- `QuarticQuery.Upper.lawOf_iterate_some`: relation partial, route same; `lean/QuarticQuery/Upper/Amplify.lean`, line 203.
- `QuarticQuery.Upper.Samples.attempts`: relation partial, route same; `lean/QuarticQuery/Upper/Amplify.lean`, line 247.
- `QuarticQuery.Upper.Samples.amplify`: relation partial, route same; `lean/QuarticQuery/Upper/Amplify.lean`, line 346.
- `QuarticQuery.Upper.trialCount_le`: relation partial, route none; `lean/QuarticQuery/Upper/Bound.lean`, line 21.
- `QuarticQuery.Upper.iterationBound_inv_le`: relation partial, route none; `lean/QuarticQuery/Upper/Bound.lean`, line 37.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-lem-3.1 -->


### def-aij


<a id="CAT-def-aij"></a>
<!-- passage:CAT-def-aij -->
<!-- claim:def-aij -->

> For a fixed oracle input and a coherent comparison circuit, a_{ij} is the probability that i is reported as defeating j when the result is measured, using one circuit per unordered pair; a_{ii}=0.

**Mathematical passages:** [upper-comparison-model](#upper-comparison-model).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-aij -->


### eq-10


<a id="CAT-eq-10"></a>
<!-- passage:CAT-eq-10 -->
<!-- claim:eq-10 -->

> a_{ij}+a_{ji}=1 for i != j, and a_{ii}=0.

**Mathematical passages:** [upper-comparison-model](#upper-comparison-model), [upper-comparison-law](#upper-comparison-law).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.cmpProb`: relation partial, route same; `lean/QuarticQuery/Upper/Columns.lean`, line 174.
<!-- /passage:CAT-eq-10 -->


### def-T-eps


<a id="CAT-def-T-eps"></a>
<!-- passage:CAT-def-T-eps -->
<!-- claim:def-T-eps -->

> For m>=2: T=ceil(log_2(1000m)), epsilon=1/(1000T).

**Mathematical passages:** [upper-tournament-parameters](#upper-tournament-parameters).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.Tval_mul_epsval`: relation partial, route none; `lean/QuarticQuery/Tournament/Ideal.lean`, line 314.
- `QuarticQuery.Tournament.miss_bound_le`: relation partial, route none; `lean/QuarticQuery/Tournament/Ideal.lean`, line 320.
- `QuarticQuery.Tournament.total_error_lt`: relation partial, route none; `lean/QuarticQuery/Tournament/Ideal.lean`, line 327.
<!-- /passage:CAT-def-T-eps -->


### eq-11


<a id="CAT-eq-11"></a>
<!-- passage:CAT-eq-11 -->
<!-- claim:eq-11 -->

> i_* is dominant if a_{i_* j} >= 1-epsilon for every j != i_*.

**Mathematical passages:** [upper-tournament-parameters](#upper-tournament-parameters).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-eq-11 -->


### def-ideal-process


<a id="CAT-def-ideal-process"></a>
<!-- passage:CAT-def-ideal-process -->
<!-- claim:def-ideal-process -->

> Ideal process: w_i=1 for all i, W=sum_i w_i. While W>0 sample p with probability w_p/W, append p to the list, update by eq-12. If W=0, leave list and weights unchanged. Run T steps.

**Mathematical passages:** [upper-ideal-process](#upper-ideal-process).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.expectFrom`: relation exact, route none; `lean/QuarticQuery/Tournament/Ideal.lean`, line 42.
<!-- /passage:CAT-def-ideal-process -->


### eq-12


<a id="CAT-eq-12"></a>
<!-- passage:CAT-eq-12 -->
<!-- claim:eq-12 -->

> Update w_i <- w_i a_{ip} for all i in [m].

**Mathematical passages:** [upper-ideal-process](#upper-ideal-process).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.weight`: relation exact, route none; `lean/QuarticQuery/Tournament/Ideal.lean`, line 35.
<!-- /passage:CAT-eq-12 -->


### eq-13


<a id="CAT-eq-13"></a>
<!-- passage:CAT-eq-13 -->
<!-- claim:eq-13 -->

> For W>0: E[W_new | w] = (1/W) sum_{p,i} w_p w_i a_{ip} = (W^2 - sum_i w_i^2)/(2W) <= W/2.

**Mathematical passages:** [upper-weight-drift](#upper-weight-drift).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-eq-13 -->


### claim-expected-WT


<a id="CAT-claim-expected-WT"></a>
<!-- passage:CAT-claim-expected-WT -->
<!-- claim:claim-expected-WT -->

> The bound of eq-13 also holds when W=0, hence E[W_T] <= m/2^T.

**Mathematical passages:** [upper-weight-drift](#upper-weight-drift).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.expected_final_weight`: relation exact, route same; `lean/QuarticQuery/Tournament/Ideal.lean`, line 212.
<!-- /passage:CAT-claim-expected-WT -->


### claim-weight-lb


<a id="CAT-claim-weight-lb"></a>
<!-- passage:CAT-claim-weight-lb -->
<!-- claim:claim-weight-lb -->

> If i_* satisfies eq-11 and has not been selected in t<=T steps, then w_{i_*} >= (1-epsilon)^t >= 1-T epsilon > 1/2. Hence W>0 until it is selected.

**Mathematical passages:** [upper-dominant-weight](#upper-dominant-weight).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.dominant_weight_lb`: relation partial, route same; `lean/QuarticQuery/Tournament/Ideal.lean`, line 239.
<!-- /passage:CAT-claim-weight-lb -->


### eq-14


<a id="CAT-eq-14"></a>
<!-- passage:CAT-eq-14 -->
<!-- claim:eq-14 -->

> Pr[i_* absent from the ideal list] <= Pr[W_T >= 1/2] <= 2m/2^T.

**Mathematical passages:** [upper-dominant-weight](#upper-dominant-weight).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.ideal_miss_le`: relation exact, route same; `lean/QuarticQuery/Tournament/Ideal.lean`, line 263.
<!-- /passage:CAT-eq-14 -->


### construct-sampler


<a id="CAT-construct-sampler"></a>
<!-- passage:CAT-construct-sampler -->
<!-- claim:construct-sampler -->

> Given pivots p_1,...,p_t with t<T: prepare uniform |i> over [m], compare i with each pivot in a fresh workspace, set the success bit iff every comparison says i defeats its pivot, keeping all garbage. Apply lem-3.1 with gamma=1/(2m), eta=epsilon. On failure stop and return the accumulated list; otherwise measure the index, append, and continue for at most T stages.

**Mathematical passages:** [upper-stage-state](#upper-stage-state), [upper-quantum-tournament](#upper-quantum-tournament).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.stageLaw`: relation partial, route none; `lean/QuarticQuery/Upper/Tournament.lean`, line 36.
- `QuarticQuery.Upper.stageLaw_some`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 43.
- `QuarticQuery.Upper.stage_samples`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 63.
<!-- /passage:CAT-construct-sampler -->


### eq-15


<a id="CAT-eq-15"></a>
<!-- passage:CAT-eq-15 -->
<!-- claim:eq-15 -->

> Pre-success state: m^{-1/2} sum_{i=1}^m |i> tensor_{b=1}^t |phi(i,p_b)>.

**Mathematical passages:** [upper-stage-state](#upper-stage-state), [upper-tournament-evidence](#upper-tournament-evidence).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-eq-15 -->


### claim-success-prob


<a id="CAT-claim-success-prob"></a>
<!-- passage:CAT-claim-success-prob -->
<!-- claim:claim-success-prob -->

> Conditional on index i the success probability is prod_{b=1}^t a_{i p_b} = w_i (empty product 1). Total success probability is W/m, and conditional on success the index has law w_i/W exactly.

**Mathematical passages:** [upper-stage-law](#upper-stage-law), [upper-tournament-evidence](#upper-tournament-evidence).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-success-prob -->


### claim-coupling


<a id="CAT-claim-coupling"></a>
<!-- passage:CAT-claim-coupling -->
<!-- claim:claim-coupling -->

> Until i_* is first selected, W/m >= 1/(2m), so at each such history the sampler fails with probability <=epsilon and otherwise follows the exact ideal pivot law. The real list contains i_* except with probability <= 2m/2^T + T epsilon.

**Mathematical passages:** [upper-coupling](#upper-coupling), [upper-tournament-evidence](#upper-tournament-evidence), [upper-continuation-induction](#upper-continuation-induction).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.tval_lower`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 239.
<!-- /passage:CAT-claim-coupling -->


### claim-tournament-cost


<a id="CAT-claim-tournament-cost"></a>
<!-- passage:CAT-claim-tournament-cost -->
<!-- claim:claim-tournament-cost -->

> Stage t uses O(c(t+1)) queries per call; lem-3.1 uses O(sqrt(m) log(1/epsilon)) calls; the sum over t<T is O(c sqrt(m) T^2 log T), a fixed cap on every branch.

**Mathematical passages:** [upper-tournament-cost](#upper-tournament-cost), [upper-finite-budget](#upper-finite-budget).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.budget_le`: relation partial, route same; `lean/QuarticQuery/Upper/Bound.lean`, line 60.
- `QuarticQuery.Upper.vall_runs`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 339.
- `QuarticQuery.Upper.tournament_runs`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 367.
<!-- /passage:CAT-claim-tournament-cost -->


### prop-3.2


<a id="CAT-prop-3.2"></a>
<!-- passage:CAT-prop-3.2 -->
<!-- claim:prop-3.2 -->

> Let m>=2, T=ceil(log_2(1000m)), epsilon=1/(1000T). For a coherent comparison circuit controlled by two candidate indices, reversible with all workspace retained, using at most c>=1 bit queries, with probabilities a_{ij} satisfying eq-10, there is a quantum algorithm making O(c sqrt(m) T^2 log T) queries on every branch and returning a list of at most T candidates such that, for every fixed oracle input and every i_* satisfying eq-11, the list contains i_* with probability >= 1-2m/2^T-T epsilon.

**Mathematical passages:** [upper-purpose](#upper-purpose), [upper-comparison-model](#upper-comparison-model), [upper-tournament-cost](#upper-tournament-cost), [upper-tournament-evidence](#upper-tournament-evidence).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Tournament.ideal_tournament`: relation partial, route same; `lean/QuarticQuery/Tournament/Ideal.lean`, line 338.
- `QuarticQuery.Upper.tval_le`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 178.
- `QuarticQuery.Upper.tournament_runs`: relation partial, route same; `lean/QuarticQuery/Upper/Tournament.lean`, line 367.
<!-- /passage:CAT-prop-3.2 -->


### def-decode


<a id="CAT-def-decode"></a>
<!-- passage:CAT-def-decode -->
<!-- claim:def-decode -->

> decode(i): run the algorithm of lem-2.1.ii on each A_{i,h}, h in [r], with error <= epsilon/r, retaining workspace. Output a string in {0,1}^r on every input.

**Mathematical passages:** [upper-decode](#upper-decode).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-decode -->


### claim-decode-cost


<a id="CAT-claim-decode-cost"></a>
<!-- passage:CAT-claim-decode-cost -->
<!-- claim:claim-decode-cost -->

> decode uses O_k(r log(r/epsilon)) = (log m)^{O_k(1)} queries. If all r instances are defined, the address is correct with probability >=1-epsilon. Otherwise it still returns some address.

**Mathematical passages:** [upper-decode-cost](#upper-decode-cost).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-decode-cost -->


### def-comparison


<a id="CAT-def-comparison"></a>
<!-- passage:CAT-def-comparison -->
<!-- claim:def-comparison -->

> Comparison of distinct columns, in sorted order: decode each in separate workspaces; read each column's pointer towards the other at its decoded address and inspect the pointed bit of the other's X string. A column disqualifies its opponent if that bit is 0. If exactly one disqualifies the other it is victorious, otherwise the smaller index. A self-comparison returns false without reading a pointer.

**Mathematical passages:** [upper-comparator](#upper-comparator).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-comparison -->


### claim-comparison-state


<a id="CAT-claim-comparison-state"></a>
<!-- passage:CAT-claim-comparison-state -->
<!-- claim:claim-comparison-state -->

> The comparison uses c=(log m)^{O_k(1)} queries; its reversal costs the same. Measurement probabilities agree with the classical description, since later operations are controlled on the decoded registers in the computational basis. The resulting a_{ij} satisfy eq-10.

**Mathematical passages:** [upper-comparator](#upper-comparator), [upper-comparison-law](#upper-comparison-law).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-comparison-state -->


### claim-winner-dominates


<a id="CAT-claim-winner-dominates"></a>
<!-- passage:CAT-claim-winner-dominates -->
<!-- claim:claim-winner-dominates -->

> If i_* is a winner then for every j != i_*, a_{i_* j} >= 1-epsilon, on every input, whether or not the opponent's instances are defined.

**Mathematical passages:** [upper-winner-dominates](#upper-winner-dominates).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.winner_no_incoming_zero`: relation partial, route same; `lean/QuarticQuery/Construction/Winner.lean`, line 62.
- `QuarticQuery.winner_finds_zero`: relation partial, route same; `lean/QuarticQuery/Construction/Winner.lean`, line 69.
- `QuarticQuery.Upper.cmpProb_winner`: relation partial, route same; `lean/QuarticQuery/Upper/Columns.lean`, line 223.
<!-- /passage:CAT-claim-winner-dominates -->


### def-verify


<a id="CAT-def-verify"></a>
<!-- passage:CAT-def-verify -->
<!-- claim:def-verify -->

> verify(i): decode and measure an address s afresh. Let A prepare a uniform test index and an exact failing-test flag at (i,s), with K tests. Apply lem-3.1 with gamma=1/K and eta=epsilon. Reject if a failed test is found, otherwise accept. Output 1 iff some listed candidate is accepted.

**Mathematical passages:** [upper-verifier](#upper-verifier).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-verify -->


### claim-verify


<a id="CAT-claim-verify"></a>
<!-- passage:CAT-claim-verify -->
<!-- claim:claim-verify -->

> A non-winner is accepted with probability <=epsilon, at every address. A true winner is rejected with probability <=epsilon, only by decoding error. Verification costs O(sqrt(K) log(1/epsilon) log m) = sqrt(m)(log m)^{O_k(1)} queries for the search, plus decoding.

**Mathematical passages:** [upper-verification-proof](#upper-verification-proof).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-verify -->


### claim-error


<a id="CAT-claim-error"></a>
<!-- passage:CAT-claim-error -->
<!-- claim:claim-error -->

> On a 0-input the error is at most T epsilon. On a 1-input it is at most 2m/2^T + T epsilon + epsilon < 1/3.

**Mathematical passages:** [upper-continuation-induction](#upper-continuation-induction), [upper-total-error](#upper-total-error).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-error -->


### claim-coherent-access


<a id="CAT-claim-coherent-access"></a>
<!-- passage:CAT-claim-coherent-access -->
<!-- claim:claim-coherent-access -->

> All superposed array accesses are ordinary bit queries. The global bit index is computed reversibly; a pointer is read in O(log m) queries; a controlled query uses load, use, unload, two queries.

**Mathematical passages:** [upper-oracle-access](#upper-oracle-access), [upper-read-compiler](#upper-read-compiler).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.ReadSpec`: relation partial, route none; `lean/QuarticQuery/Upper/Circuit.lean`, line 141.
- `QuarticQuery.Upper.ReadSpec.op`: relation partial, route none; `lean/QuarticQuery/Upper/Circuit.lean`, line 183.
- `QuarticQuery.Upper.sigmaOp`: relation partial, route none; `lean/QuarticQuery/Upper/Circuit.lean`, line 277.
- `QuarticQuery.Upper.IsCirc`: relation partial, route none; `lean/QuarticQuery/Upper/Circuit.lean`, line 342.
- `QuarticQuery.Upper.IsCirc.comp`: relation partial, route none; `lean/QuarticQuery/Upper/Circuit.lean`, line 372.
- `QuarticQuery.Upper.IsCirc.symm`: relation partial, route same; `lean/QuarticQuery/Upper/Circuit.lean`, line 379.
- `QuarticQuery.Upper.IsCirc.congr`: relation partial, route none; `lean/QuarticQuery/Upper/Circuit.lean`, line 412.
- `QuarticQuery.Upper.IsCirc.sigma`: relation partial, route same; `lean/QuarticQuery/Upper/Circuit.lean`, line 423.
- `QuarticQuery.Upper.addrLaw`: relation partial, route none; `lean/QuarticQuery/Upper/Columns.lean`, line 46.
- `QuarticQuery.Upper.addrLaw_good`: relation partial, route same; `lean/QuarticQuery/Upper/Columns.lean`, line 65.
- `QuarticQuery.Upper.core_samples`: relation partial, route same; `lean/QuarticQuery/Upper/Columns.lean`, line 143.
- `QuarticQuery.Upper.exists_gate_orth`: relation partial, route none; `lean/QuarticQuery/Upper/Compile.lean`, line 61.
- `QuarticQuery.Upper.compile_read`: relation partial, route same; `lean/QuarticQuery/Upper/Compile.lean`, line 151.
- `QuarticQuery.Upper.compile_circ`: relation partial, route same; `lean/QuarticQuery/Upper/Compile.lean`, line 217.
- `QuarticQuery.Upper.Samples.runs`: relation partial, route alternative; `lean/QuarticQuery/Upper/Compile.lean`, line 396.
- `QuarticQuery.Upper.Samples`: relation partial, route none; `lean/QuarticQuery/Upper/Sampler.lean`, line 115.
- `QuarticQuery.Upper.Samples.bind`: relation partial, route same; `lean/QuarticQuery/Upper/Sampler.lean`, line 241.
- `QuarticQuery.Upper.Samples.tree`: relation partial, route same; `lean/QuarticQuery/Upper/Sampler.lean`, line 300.
<!-- /passage:CAT-claim-coherent-access -->


### prop-3.3


<a id="CAT-prop-3.3"></a>
<!-- passage:CAT-prop-3.3 -->
<!-- claim:prop-3.3 -->

> For every fixed k>=2, Q(F_{k,m}) <= sqrt(m) (log m)^{O_k(1)}.

**Mathematical passages:** [upper-purpose](#upper-purpose), [upper-finite-budget](#upper-finite-budget), [upper-asymptotic-bound](#upper-asymptotic-bound), [upper-explicit-log6](#upper-explicit-log6).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Upper.budget_le`: relation partial, route same; `lean/QuarticQuery/Upper/Bound.lean`, line 60.
- `QuarticQuery.Upper.Fkm_forrCircuit_QLe`: relation stronger, route same; `lean/QuarticQuery/Upper/Bound.lean`, line 245.
- `QuarticQuery.Upper.Q_Fkm_le`: relation stronger, route same; `lean/QuarticQuery/Upper/Bound.lean`, line 251.
- `QuarticQuery.Upper.Fkm_QLe`: relation partial, route same; `lean/QuarticQuery/Upper/Verify.lean`, line 138.
<!-- /passage:CAT-prop-3.3 -->


### claim-product-law


<a id="CAT-claim-product-law"></a>
<!-- passage:CAT-claim-product-law -->
<!-- claim:claim-product-law -->

> For a deterministic algorithm, at every transcript tau of positive probability, the conditional law of (U_1,...,U_r) given tau is a product of separate conditional laws, because the event of obtaining tau is a Cartesian product of constraints on each input.

**Mathematical passages:** [CL-product-law](#CL-product-law).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-product-law -->


### def-value-V


<a id="CAT-def-value-V"></a>
<!-- passage:CAT-def-value-V -->
<!-- claim:def-value-V -->

> With q_h queries already made to U_h, V_h(tau) is the largest success probability for computing P(U_h) under its conditional law given tau using at most L-q_h further queries.

**Mathematical passages:** [CL-conditional-values](#CL-conditional-values).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-value-V -->


### eq-16


<a id="CAT-eq-16"></a>
<!-- passage:CAT-eq-16 -->
<!-- claim:eq-16 -->

> If the next query at tau addresses U_h then E[V_h(tau') | tau] <= V_h(tau). The conditional laws and budgets of the other inputs do not change.

**Mathematical passages:** [CL-conditional-values](#CL-conditional-values).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-eq-16 -->


### claim-supermartingale


<a id="CAT-claim-supermartingale"></a>
<!-- passage:CAT-claim-supermartingale -->
<!-- claim:claim-supermartingale -->

> E[prod_j V_j(tau') | tau] <= prod_j V_j(tau). The product is a supermartingale over at most rL queries.

**Mathematical passages:** [CL-supermartingale](#CL-supermartingale).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-supermartingale -->


### claim-final-bound


<a id="CAT-claim-final-bound"></a>
<!-- passage:CAT-claim-final-bound -->
<!-- claim:claim-final-bound -->

> At the final transcript tau, Pr[chosen vector correct | tau] <= prod_h max_b Pr(P(U_h)=b | tau) <= prod_h V_h(tau).

**Mathematical passages:** [CL-supermartingale](#CL-supermartingale).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-final-bound -->


### lem-4.1


<a id="CAT-lem-4.1"></a>
<!-- passage:CAT-lem-4.1 -->
<!-- claim:lem-4.1 -->

> Let P:D->{0,1}, D subset {0,1}^n, mu a distribution on D, L a nonnegative integer. Suppose every deterministic algorithm making at most L queries computes P under mu with success probability <=beta. If U_1,...,U_r are iid mu, every classical algorithm making at most L queries to each U_h, possibly randomized, adaptive among the r inputs, and given arbitrary additional information independent of (U_1,...,U_r), outputs (P(U_1),...,P(U_r)) with probability <=beta^r.

**Mathematical passages:** [CL-direct-product-statement](#CL-direct-product-statement), [CL-supermartingale](#CL-supermartingale), [CL-weighted-values](#CL-weighted-values), [CL-weighted-product](#CL-weighted-product), [CL-independent-information](#CL-independent-information).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=alternative; reach=reached.

**Original declaration ties:**

- `QuarticQuery.direct_product`: relation partial, route alternative; `lean/QuarticQuery/LowerBound/DirectProduct.lean`, line 304.
- `QuarticQuery.direct_product_average`: relation exact, route alternative; `lean/QuarticQuery/LowerBound/DirectProduct.lean`, line 316.
- `QuarticQuery.direct_product_randomized`: relation exact, route alternative; `lean/QuarticQuery/LowerBound/DirectProduct.lean`, line 327.
- `QuarticQuery.direct_product_of_depth_le`: relation weaker, route alternative; `lean/QuarticQuery/LowerBound/DirectProduct.lean`, line 342.
<!-- /passage:CAT-lem-4.1 -->


### claim-minimax-mu


<a id="CAT-claim-minimax-mu"></a>
<!-- passage:CAT-claim-minimax-mu -->
<!-- claim:claim-minimax-mu -->

> If L<R(P), there is a distribution mu on dom P, which is in particular nonempty, such that every deterministic tree of depth <=L has success probability <=2/3 under mu.

**Mathematical passages:** [CL-minimax](#CL-minimax).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.exists_hard_distribution`: relation exact, route same; `lean/QuarticQuery/LowerBound/Minimax.lean`, line 138.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-claim-minimax-mu -->


### eq-17


<a id="CAT-eq-17"></a>
<!-- passage:CAT-eq-17 -->
<!-- claim:eq-17 -->

> G = floor(mL/100).

**Mathematical passages:** [CL-generic-statement](#CL-generic-statement).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-eq-17 -->


### def-dummy


<a id="CAT-def-dummy"></a>
<!-- passage:CAT-def-dummy -->
<!-- claim:def-dummy -->

> Dummy input Y^(0): independently for each i, J_i uniform in [m], X_i has a single 0 at position J_i. All A_{i,h} are iid mu independent of the J_i. All cells B_{i,s} are one fixed blank pattern.

**Mathematical passages:** [CL-dummy](#CL-dummy).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.avg_resample`: relation partial, route none; `lean/QuarticQuery/LowerBound/Planted/Average.lean`, line 134.
- `QuarticQuery.dummy`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Inputs.lean`, line 50.
<!-- /passage:CAT-def-dummy -->


### def-planted


<a id="CAT-def-planted"></a>
<!-- passage:CAT-def-planted -->
<!-- claim:def-planted -->

> I is uniform in [m] and independent of Y^(0). Y^(1) is Y^(0) with X_I:=1^m and B_{I,s_I} filled with the correct transcripts and pointers p_{I,s_I,j}=J_j for j != I.

**Mathematical passages:** [CL-planted](#CL-planted).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.trueAddr`: relation partial, route none; `lean/QuarticQuery/LowerBound/Planted/Inputs.lean`, line 23.
- `QuarticQuery.planted`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Inputs.lean`, line 58.
<!-- /passage:CAT-def-planted -->


### claim-Y-values


<a id="CAT-claim-Y-values"></a>
<!-- passage:CAT-claim-Y-values -->
<!-- claim:claim-Y-values -->

> F_{k,m}(Y^(0))=0 and F_{k,m}(Y^(1))=1 for all sample points.

**Mathematical passages:** [CL-planted](#CL-planted).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.addressedF_dummy`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Inputs.lean`, line 97.
- `QuarticQuery.addressedF_planted`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Inputs.lean`, line 106.
<!-- /passage:CAT-claim-Y-values -->


### eq-18


<a id="CAT-eq-18"></a>
<!-- passage:CAT-eq-18 -->
<!-- claim:eq-18 -->

> For a deterministic algorithm with at most G queries, |Pr[outputs 1 on Y^(1)]-Pr[outputs 1 on Y^(0)]| <= Pr(the dummy run queries X_I[J_I]) + Pr(the dummy run queries any bit of B_{I,s_I}).

**Mathematical passages:** [CL-first-difference](#CL-first-difference).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.QueryTree.exists_mem_path_ne`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Coupling.lean`, line 43.
- `QuarticQuery.eq_of_dummy_ne_planted`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Inputs.lean`, line 70.
- `QuarticQuery.output_gap_le`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Main.lean`, line 33.
<!-- /passage:CAT-eq-18 -->


### def-Z


<a id="CAT-def-Z"></a>
<!-- passage:CAT-def-Z -->
<!-- claim:def-Z -->

> Z is the number of columns whose zero is discovered in the dummy run.

**Mathematical passages:** [CL-early-late](#CL-early-late).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-Z -->


### claim-uniform-zero


<a id="CAT-claim-uniform-zero"></a>
<!-- passage:CAT-claim-uniform-zero -->
<!-- claim:claim-uniform-zero -->

> Before the zero in a column is found, its location is uniform among positions of that column not yet queried, conditional on the full adaptive transcript.

**Mathematical passages:** [CL-early-late](#CL-early-late).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-uniform-zero -->


### claim-EZ


<a id="CAT-claim-EZ"></a>
<!-- passage:CAT-claim-EZ -->
<!-- claim:claim-EZ -->

> E Z <= 4G/m: an early discovery (fewer than m/2 distinct positions queried in that column before it) has probability <=2/m per query, giving <=2G/m in expectation; any other discovery lies in one of at most 2G/m columns receiving >=m/2 queries.

**Mathematical passages:** [CL-early-late](#CL-early-late).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-EZ -->


### eq-19


<a id="CAT-eq-19"></a>
<!-- passage:CAT-eq-19 -->
<!-- claim:eq-19 -->

> Pr(the dummy run queries X_I[J_I]) = E Z/m <= 4G/m^2.

**Mathematical passages:** [CL-early-late](#CL-early-late), [CL-zero-worlds](#CL-zero-worlds), [CL-zero-average](#CL-zero-average).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=alternative; reach=reached.

**Original declaration ties:**

- `QuarticQuery.zero_search_sum`: relation partial, route alternative; `lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean`, line 37.
- `QuarticQuery.foundZero`: relation partial, route none; `lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean`, line 157.
- `QuarticQuery.column_zero_bound`: relation partial, route alternative; `lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean`, line 167.
- `QuarticQuery.avg_foundZero_le`: relation partial, route alternative; `lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean`, line 192.
- `QuarticQuery.sum_xQueries_le`: relation partial, route alternative; `lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean`, line 210.
- `QuarticQuery.avg_foundZero_I_le`: relation stronger, route alternative; `lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean`, line 226.
<!-- /passage:CAT-eq-19 -->


### def-heavy


<a id="CAT-def-heavy"></a>
<!-- passage:CAT-def-heavy -->
<!-- claim:def-heavy -->

> Column i is heavy if, over the entire dummy run, the algorithm makes more than L queries in total to A_{i,1},...,A_{i,r}. Repeats count.

**Mathematical passages:** [CL-heavy](#CL-heavy).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-heavy -->


### eq-20


<a id="CAT-eq-20"></a>
<!-- passage:CAT-eq-20 -->
<!-- claim:eq-20 -->

> Pr(I is heavy) <= G/(mL).

**Mathematical passages:** [CL-heavy](#CL-heavy).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.avg_heavy_le`: relation stronger, route same; `lean/QuarticQuery/LowerBound/Planted/Heavy.lean`, line 42.
<!-- /passage:CAT-eq-20 -->


### def-simulator


<a id="CAT-def-simulator"></a>
<!-- passage:CAT-def-simulator -->
<!-- claim:def-simulator -->

> Fix i and t in {1,...,G}. A simulator receives all of the dummy input outside A_{i,1},...,A_{i,r}, runs the deterministic algorithm up to its proposed t-th query, and aborts before an (L+1)st query to those r strings in total. If it reaches time t and the proposed query is to a cell B_{i,s}, it outputs s; otherwise it outputs a fixed vector.

**Mathematical passages:** [CL-simulator](#CL-simulator).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-simulator -->


### eq-21


<a id="CAT-eq-21"></a>
<!-- passage:CAT-eq-21 -->
<!-- claim:eq-21 -->

> For each i and t: Pr(i is nonheavy and the t-th query is in B_{i,s_i}) <= (2/3)^r.

**Mathematical passages:** [CL-simulator](#CL-simulator), [CL-joint-event](#CL-joint-event).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.simTree`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Simulator.lean`, line 32.
- `QuarticQuery.depth_simTree_le`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Simulator.lean`, line 50.
- `QuarticQuery.eval_simTree`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Simulator.lean`, line 76.
- `QuarticQuery.reachedCell`: relation partial, route none; `lean/QuarticQuery/LowerBound/Planted/Simulator.lean`, line 131.
<!-- /passage:CAT-eq-21 -->


### eq-22


<a id="CAT-eq-22"></a>
<!-- passage:CAT-eq-22 -->
<!-- claim:eq-22 -->

> Pr(the dummy run queries B_{I,s_I}) <= G/(mL) + G(2/3)^r.

**Mathematical passages:** [CL-cell-union](#CL-cell-union).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.avg_reachedCell_le`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Simulator.lean`, line 172.
<!-- /passage:CAT-eq-22 -->


### eq-23


<a id="CAT-eq-23"></a>
<!-- passage:CAT-eq-23 -->
<!-- claim:eq-23 -->

> The output-probability difference is at most 4G/m^2 + G/(mL) + G(2/3)^r.

**Mathematical passages:** [CL-discrepancy](#CL-discrepancy).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.tree_gap_le`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Main.lean`, line 59.
<!-- /passage:CAT-eq-23 -->


### claim-tail


<a id="CAT-claim-tail"></a>
<!-- passage:CAT-claim-tail -->
<!-- claim:claim-tail -->

> G(2/3)^r <= (1/100) m^{2-20 log_2(3/2)} = o(1).

**Mathematical passages:** [CL-tail-numeric](#CL-tail-numeric).

**Original corpus evidence:** formal_statement=weaker; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.twoThirds_pow_le`: relation weaker, route alternative; `lean/QuarticQuery/Results/Exponent.lean`, line 429.
<!-- /passage:CAT-claim-tail -->


### claim-numeric


<a id="CAT-claim-numeric"></a>
<!-- passage:CAT-claim-numeric -->
<!-- claim:claim-numeric -->

> For m=4^t, r=40t, 1<=L<=m and G<=mL/100: 4G/m^2<=4/100, G/(mL)<=1/100, G(2/3)^r<=1/100, so eq-23 is at most 6/100<1/3.

**Mathematical passages:** [CL-tail-numeric](#CL-tail-numeric).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.discrepancy_le`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 443.
- `QuarticQuery.discrepancy_lt_third`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 471.
- `QuarticQuery.discrepancy_parameters`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 479.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-claim-numeric -->


### prop-4.2


<a id="CAT-prop-4.2"></a>
<!-- passage:CAT-prop-4.2 -->
<!-- claim:prop-4.2 -->

> For each fixed integer k>=2 and every sufficiently large power of four m, R(F_{k,m}) > G=floor(mL/100), with L=floor(m^{1-1/k}/(log_2 m)^2).

**Mathematical passages:** [CL-concrete-lower](#CL-concrete-lower).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Gvalue_lt_R_Fkm`: relation stronger, route same; `lean/QuarticQuery/LowerBound/Planted/Main.lean`, line 203.
<!-- /passage:CAT-prop-4.2 -->


### cor-R-omega


<a id="CAT-cor-R-omega"></a>
<!-- passage:CAT-cor-R-omega -->
<!-- claim:cor-R-omega -->

> For fixed k, R(F_{k,m}) = Omega_k(m^{2-1/k}/(log m)^2).

**Mathematical passages:** [ROOT-FAMILY-ASSEMBLY](#ROOT-FAMILY-ASSEMBLY), [CL-concrete-lower](#CL-concrete-lower).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.rpow_le_of_Gvalue_lt`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 409.
<!-- /passage:CAT-cor-R-omega -->


### claim-floor


<a id="CAT-claim-floor"></a>
<!-- passage:CAT-claim-floor -->
<!-- claim:claim-floor -->

> For sufficiently large m, floor((m/100) floor(m^{1-1/k}/(log m)^2)) >= c_k m^{2-1/k}/(log m)^2 after decreasing c_k>0.

**Mathematical passages:** [ROOT-FAMILY-ASSEMBLY](#ROOT-FAMILY-ASSEMBLY), [CL-floors](#CL-floors).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.Gvalue_ge`: relation stronger, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 365.
<!-- /passage:CAT-claim-floor -->


### claim-exponent-ratio


<a id="CAT-claim-exponent-ratio"></a>
<!-- passage:CAT-claim-exponent-ratio -->
<!-- claim:claim-exponent-ratio -->

> For fixed 0<=alpha<4 and integer k>=2 with 2-1/k>alpha/2: R(F_{k,m})/(1+Q(F_{k,m}))^alpha >= c_{k,alpha} m^{2-1/k-alpha/2}/(log m)^{2+alpha b_k}, which tends to infinity.

**Mathematical passages:** [ROOT-RATIO](#ROOT-RATIO).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.eventually_gt_rpow`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 118.
- `QuarticQuery.exists_nat_exponent`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 160.
<!-- /passage:CAT-claim-exponent-ratio -->


### claim-no-smaller-exponent


<a id="CAT-claim-no-smaller-exponent"></a>
<!-- passage:CAT-claim-no-smaller-exponent -->
<!-- claim:claim-no-smaller-exponent -->

> For every 0<=alpha<4, alpha does not belong to the set in eq-1, because a suitable k exists with k > 1/(2-alpha/2).

**Mathematical passages:** [ROOT-NO-SMALLER](#ROOT-NO-SMALLER).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.not_bound_of_familyBoundsAt`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 202.
- `QuarticQuery.not_universalPower_of_familyBoundsAt`: relation partial, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 220.
- `QuarticQuery.not_universalPower_of_family`: relation exact, route same; `lean/QuarticQuery/Results/Exponent.lean`, line 231.
- `QuarticQuery.no_universal_power`: relation partial, route same; `lean/QuarticQuery/Results/Headline.lean`, line 27.
<!-- /passage:CAT-claim-no-smaller-exponent -->


### def-D


<a id="CAT-def-D"></a>
<!-- passage:CAT-def-D -->
<!-- claim:def-D -->

> D(f) is the least depth of a deterministic decision tree computing f exactly on every input.

**Mathematical passages:** [ROOT-PARTIAL](#ROOT-PARTIAL).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=compared; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.QueryTree.toDecisionTree`: relation partial, route none; `lean/QuarticQuery/Bridge/DecisionTree.lean`, line 25.
- `QuarticQuery.QueryTree.ofDecisionTree`: relation partial, route none; `lean/QuarticQuery/Bridge/DecisionTree.lean`, line 30.
- `QuarticQuery.QueryTree.eval_toDecisionTree`: relation partial, route none; `lean/QuarticQuery/Bridge/DecisionTree.lean`, line 47.
- `QuarticQuery.QueryTree.depth_toDecisionTree`: relation partial, route none; `lean/QuarticQuery/Bridge/DecisionTree.lean`, line 56.
- `QuarticQuery.D_totalise_eq_complexity`: relation exact, route none; `lean/QuarticQuery/Bridge/DecisionTree.lean`, line 67.
- `QuarticQuery.DLe_length`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 231.
- `QuarticQuery.DLe_card`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 239.
- `QuarticQuery.DLe_D`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 268.
- `QuarticQuery.D_le_iff`: relation exact, route none; `lean/QuarticQuery/Model/Classical.lean`, line 282.
- `QuarticQuery.lt_D_iff`: relation exact, route none; `lean/QuarticQuery/Model/Classical.lean`, line 312.
- `QuarticQuery.lt_D_of_not_DLe`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 321.
- `QuarticQuery.D_reindex`: relation partial, route none; `lean/QuarticQuery/Model/Classical.lean`, line 358.
<!-- /passage:CAT-def-D -->


### def-deg


<a id="CAT-def-deg"></a>
<!-- passage:CAT-def-deg -->
<!-- claim:def-deg -->

> deg(f) is the degree of the unique real multilinear polynomial agreeing with f on the cube, with degree 0 for every constant function, including the zero function. With this convention it is unchanged by replacing input or output bits by signs.

**Mathematical passages:** [ROOT-DEGREE-BLOCK](#ROOT-DEGREE-BLOCK).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.

This row was already marked corrected in the supplied corpus. Its original historical text is not substituted for the current statement above.
<!-- /passage:CAT-def-deg -->


### def-bs


<a id="CAT-def-bs"></a>
<!-- passage:CAT-def-bs -->
<!-- claim:def-bs -->

> A nonempty B subset [n] is a sensitive block at x if flipping all bits of B changes f(x). bs(f) is the maximum over x of the number of pairwise disjoint sensitive blocks at x.

**Mathematical passages:** [ROOT-DEGREE-BLOCK](#ROOT-DEGREE-BLOCK).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-bs -->


### def-Gamma-i


<a id="CAT-def-Gamma-i"></a>
<!-- passage:CAT-def-Gamma-i -->
<!-- claim:def-Gamma-i -->

> For an input-indexed matrix Gamma, (Gamma_i)_{xy}=Gamma_{xy} 1{x_i != y_i}. Matrix norms are operator norms for the Euclidean norm.

**Mathematical passages:** [ROOT-ADVERSARY-PERRON](#ROOT-ADVERSARY-PERRON).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-Gamma-i -->


### claim-perron


<a id="CAT-claim-perron"></a>
<!-- passage:CAT-claim-perron -->
<!-- claim:claim-perron -->

> A nonzero real symmetric entrywise nonnegative Gamma has a nonnegative unit eigenvector v of eigenvalue ||Gamma||.

**Mathematical passages:** [ROOT-ADVERSARY-PERRON](#ROOT-ADVERSARY-PERRON).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-perron -->


### def-adv-progress


<a id="CAT-def-adv-progress"></a>
<!-- passage:CAT-def-adv-progress -->
<!-- claim:def-adv-progress -->

> W_t = sum_{x,y} v_x v_y Gamma_{xy} <psi_x^t | psi_y^t>, where psi_x^t is the purified state after t queries on input x.

**Mathematical passages:** [ROOT-ADVERSARY-PROGRESS](#ROOT-ADVERSARY-PROGRESS).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-adv-progress -->


### claim-per-query


<a id="CAT-claim-per-query"></a>
<!-- passage:CAT-claim-per-query -->
<!-- claim:claim-per-query -->

> Each query changes W by at most: |W_{t+1}-W_t| <= 2 sum_i u_i^T Gamma_i u_i <= 2 max_i ||Gamma_i||, where u_i(x)=v_x ||phi_{x,i}||.

**Mathematical passages:** [ROOT-ADVERSARY-PROGRESS](#ROOT-ADVERSARY-PROGRESS).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-per-query -->


### claim-final-overlap


<a id="CAT-claim-final-overlap"></a>
<!-- passage:CAT-claim-final-overlap -->
<!-- claim:claim-final-overlap -->

> If Pr[output 1] is <=1/3 on one state and >=2/3 on another, their overlap has absolute value <=2 sqrt(2)/3. Hence |W_final| <= (2 sqrt(2)/3)||Gamma||.

**Mathematical passages:** [ROOT-ADVERSARY-FINAL](#ROOT-ADVERSARY-FINAL).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-final-overlap -->


### lem-A.2


<a id="CAT-lem-A.2"></a>
<!-- passage:CAT-lem-A.2 -->
<!-- claim:lem-A.2 -->

> Let f be a nonconstant total Boolean function, Gamma a nonzero real symmetric entrywise nonnegative input-indexed matrix with Gamma_{xy}=0 whenever f(x)=f(y). Then Q(f) >= c ||Gamma|| / max_i ||Gamma_i|| for an absolute constant c>0.

**Mathematical passages:** [ROOT-ADVERSARY-PROGRESS](#ROOT-ADVERSARY-PROGRESS), [ROOT-ADVERSARY-FINAL](#ROOT-ADVERSARY-FINAL).

**Original corpus evidence:** formal_statement=partial; build=built_at_pin; comparator=not_run; route=none; reach=reached.

**Original declaration ties:**

- `QuarticQuery.FixedSim.build`: relation partial, route alternative; `lean/QuarticQuery/Bridge/Deferred.lean`, line 268.
- `QuarticQuery.exists_fixedSequence`: relation partial, route alternative; `lean/QuarticQuery/Bridge/Deferred.lean`, line 286.
<!-- /passage:CAT-lem-A.2 -->


### def-Sf


<a id="CAT-def-Sf"></a>
<!-- passage:CAT-def-Sf -->
<!-- claim:def-Sf -->

> S_f is the adjacency matrix on {0,1}^n of the graph joining inputs that differ in exactly one bit and have different f-values. lambda(f)=||S_f||.

**Mathematical passages:** [ROOT-BS-LAMBDA](#ROOT-BS-LAMBDA).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-Sf -->


### lem-A.3.bs


<a id="CAT-lem-A.3.bs"></a>
<!-- passage:CAT-lem-A.3.bs -->
<!-- claim:lem-A.3.bs -->

> For nonconstant total f, bs(f)=O(Q(f)^2).

**Mathematical passages:** [ROOT-BS-LAMBDA](#ROOT-BS-LAMBDA).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-A.3.bs -->


### lem-A.3.lambda


<a id="CAT-lem-A.3.lambda"></a>
<!-- passage:CAT-lem-A.3.lambda -->
<!-- claim:lem-A.3.lambda -->

> For nonconstant total f, lambda(f)=O(Q(f)).

**Mathematical passages:** [ROOT-BS-LAMBDA](#ROOT-BS-LAMBDA).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-A.3.lambda -->


### lem-A.3


<a id="CAT-lem-A.3"></a>
<!-- passage:CAT-lem-A.3 -->
<!-- claim:lem-A.3 -->

> Conjunction of lem-A.3.bs and lem-A.3.lambda.

**Mathematical passages:** [ROOT-BS-LAMBDA](#ROOT-BS-LAMBDA).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-A.3 -->


### claim-restrict-parity


<a id="CAT-claim-restrict-parity"></a>
<!-- passage:CAT-claim-restrict-parity -->
<!-- claim:claim-restrict-parity -->

> With f in sign form and d=deg f>=1, restricting variables outside a degree-d monomial's support gives g on the d-cube with nonzero parity correlation. So for some sigma in {-1,1}, U={x:g(x)=sigma x_1...x_d} has |U|>2^{d-1}, and every cube edge inside U changes g.

**Mathematical passages:** [ROOT-HUANG-RESTRICTION](#ROOT-HUANG-RESTRICTION).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-restrict-parity -->


### def-huang


<a id="CAT-def-huang"></a>
<!-- passage:CAT-def-huang -->
<!-- claim:def-huang -->

> H'_1=[[0,1],[1,0]], H'_{j+1}=[[H'_j,I],[I,-H'_j]]. Its entrywise absolute value is the cube adjacency matrix.

**Mathematical passages:** [ROOT-HUANG-SPECTRUM](#ROOT-HUANG-SPECTRUM).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-def-huang -->


### claim-huang-spectrum


<a id="CAT-claim-huang-spectrum"></a>
<!-- passage:CAT-claim-huang-spectrum -->
<!-- claim:claim-huang-spectrum -->

> (H'_j)^2=jI, trace H'_j=0, so H'_d has eigenvalues +-sqrt(d), each of multiplicity 2^{d-1}.

**Mathematical passages:** [ROOT-HUANG-SPECTRUM](#ROOT-HUANG-SPECTRUM).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-huang-spectrum -->


### claim-interlace


<a id="CAT-claim-interlace"></a>
<!-- passage:CAT-claim-interlace -->
<!-- claim:claim-interlace -->

> There is a nonzero v in the sqrt(d)-eigenspace supported on U; with u=|v|, u^T A_U u >= v^T H'_d v = sqrt(d)||u||^2.

**Mathematical passages:** [ROOT-HUANG-SPECTRUM](#ROOT-HUANG-SPECTRUM).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-interlace -->


### lem-A.4


<a id="CAT-lem-A.4"></a>
<!-- passage:CAT-lem-A.4 -->
<!-- claim:lem-A.4 -->

> Every nonconstant total Boolean f satisfies deg(f) <= lambda(f)^2.

**Mathematical passages:** [ROOT-HUANG-SPECTRUM](#ROOT-HUANG-SPECTRUM).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-A.4 -->


### claim-round-block


<a id="CAT-claim-round-block"></a>
<!-- passage:CAT-claim-round-block -->
<!-- claim:claim-round-block -->

> In each round of the algorithm on input x, with S the selected maximum-degree monomial's support in the current restriction, the restriction to S with all other unqueried variables set as in x is nonconstant. So some nonempty subset of S is a sensitive block at x. Blocks of different rounds are disjoint.

**Mathematical passages:** [ROOT-MONOMIAL-TREE](#ROOT-MONOMIAL-TREE).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-claim-round-block -->


### lem-A.5


<a id="CAT-lem-A.5"></a>
<!-- passage:CAT-lem-A.5 -->
<!-- claim:lem-A.5 -->

> Every total Boolean f satisfies D(f) <= bs(f) deg(f).

**Mathematical passages:** [ROOT-MONOMIAL-TREE](#ROOT-MONOMIAL-TREE).

**Original corpus evidence:** formal_statement=none; build=not_run; comparator=not_run; route=none; reach=none.

**Original declaration ties:** none. Source correspondences, when available, are described in the linked mathematical passage.
<!-- /passage:CAT-lem-A.5 -->


### thm-A.1


<a id="CAT-thm-A.1"></a>
<!-- passage:CAT-thm-A.1 -->
<!-- claim:thm-A.1 -->

> Every total Boolean function satisfies R(f) <= D(f) = O((1+Q(f))^4), with an absolute constant.

**Mathematical passages:** [ROOT-APPENDIX-INTRO](#ROOT-APPENDIX-INTRO), [ROOT-QUARTIC-UPPER](#ROOT-QUARTIC-UPPER).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=alternative; reach=reached.

**Original declaration ties:**

- `QuarticQuery.D_le_of_QLe`: relation partial, route alternative; `lean/QuarticQuery/Appendix/TheoremA1.lean`, line 25.
- `QuarticQuery.D_le_Q_pow_four`: relation partial, route alternative; `lean/QuarticQuery/Appendix/TheoremA1.lean`, line 52.
- `QuarticQuery.R_le_D_le_one_add_Q_pow_four`: relation exact, route alternative; `lean/QuarticQuery/Appendix/TheoremA1.lean`, line 57.
- `QuarticQuery.universalPower_four`: relation partial, route alternative; `lean/QuarticQuery/Appendix/TheoremA1.lean`, line 70.
<!-- /passage:CAT-thm-A.1 -->


### claim-address-guess


<a id="CAT-claim-address-guess"></a>
<!-- passage:CAT-claim-address-guess -->
<!-- claim:claim-address-guess -->

> Under mu from claim-minimax-mu, for U_1,...,U_r iid mu, every classical algorithm making at most L queries to each U_h, given information independent of (U_1,...,U_r), outputs (P(U_1),...,P(U_r)) with probability <=(2/3)^r.

**Mathematical passages:** [CL-address-guess](#CL-address-guess).

**Original corpus evidence:** formal_statement=exact; build=built_at_pin; comparator=not_run; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.address_guess_le`: relation partial, route same; `lean/QuarticQuery/LowerBound/Minimax.lean`, line 179.
- `QuarticQuery.address_guess_average`: relation exact, route same; `lean/QuarticQuery/LowerBound/Minimax.lean`, line 188.
- `QuarticQuery.exists_address_guess_bound`: relation partial, route same; `lean/QuarticQuery/LowerBound/Minimax.lean`, line 198.
<!-- /passage:CAT-claim-address-guess -->


### prop-4.2-generic


<a id="CAT-prop-4.2-generic"></a>
<!-- passage:CAT-prop-4.2-generic -->
<!-- claim:prop-4.2-generic -->

> Let m=4^t with t>=1 and r=40t. Let P be a partial function on km bits with an exact circuit C (d=1 iff defined, and d=1 implies b=P), and F the total function built from (P,C). If 1<=L<=m and L<R(P), then R(F)>floor(mL/100).

**Mathematical passages:** [CL-generic-statement](#CL-generic-statement), [CL-randomized-contradiction](#CL-randomized-contradiction).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=compared; route=same; reach=reached.

**Original declaration ties:**

- `QuarticQuery.addressedF_not_RLe`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Main.lean`, line 111.
- `QuarticQuery.addressedF_lower`: relation partial, route same; `lean/QuarticQuery/LowerBound/Planted/Main.lean`, line 180.
- `QuarticQuery.Gvalue_lt_R_addressedF`: relation stronger, route same; `lean/QuarticQuery/LowerBound/Planted/Main.lean`, line 190.
<!-- /passage:CAT-prop-4.2-generic -->


### claim-winner-fidelity


<a id="CAT-claim-winner-fidelity"></a>
<!-- passage:CAT-claim-winner-fidelity -->
<!-- claim:claim-winner-fidelity -->

> Given the correctness half of lem-2.1.iii: WinsAt(y,i,s) iff X_i=1^m, every P(A_{i,h}) is defined, s=s_i, the transcripts in B_{i,s} are correct, and eq-8 holds. Hence exists s, WinsAt(y,i,s) is the paper's winner condition.

**Mathematical passages:** [CL-fidelity](#CL-fidelity).

**Original corpus evidence:** formal_statement=stronger; build=built_at_pin; comparator=not_run; route=same; reach=outside.

**Original declaration ties:**

- `QuarticQuery.winsAt_iff_paperWinsAt`: relation stronger, route same; `lean/QuarticQuery/Construction/LocalTests.lean`, line 329.
<!-- /passage:CAT-claim-winner-fidelity -->



## Appendix C. References


<a id="ROOT-REFERENCES"></a>
<!-- passage:ROOT-REFERENCES -->
The bibliography file contains the full machine-readable entries and detailed locator notes. Every cited research work has a DOI or arXiv identifier when one is available. The supplied OpenAI manuscript and pinned code snapshots are explicitly identified by URL, revision or file hash where no such identifier was found.

- **OpenAI2026.** OpenAI. *A nearly quartic separation between randomized and quantum query complexity* (2026). [Primary source](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). Supplied 19-page PDF, SHA-256 a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e. The supplied manifest pins openai/math at 4eaee875. No DOI or arXiv identifier was located; none is invented.
- **ABKRT2021.** Scott Aaronson; Shalev Ben-David; Robin Kothari; Shravas Rao; Avishay Tal. *Degree vs. Approximate degree and quantum implications of Huang’s sensitivity theorem* (2021). [DOI 10.1145/3406325.3451047](https://doi.org/10.1145/3406325.3451047). Locators in this record use the arXiv v1 PDF: Theorem 1, degree versus spectral sensitivity; Theorem 2, universal quartic upper bound; Definition 7 and Lemma 9, spectral sensitivity; Section 7, Conjecture 2, printed page 20.
- **Huang2019.** Hao Huang. *Induced subgraphs of hypercubes and a proof of the sensitivity conjecture* (2019). [DOI 10.4007/annals.2019.190.3.6](https://doi.org/10.4007/annals.2019.190.3.6). Lemma 2.2, signed-cube spectrum; proof and subsequent spectral remark for Theorem 1.1.
- **Midrijanis2004.** Gatis Midrijānis. *Exact quantum query complexity for total boolean functions* (2004). [DOI 10.48550/arXiv.quant-ph/0403168](https://doi.org/10.48550/arXiv.quant-ph/0403168). Version 2, 27 March 2004. Lemma 3 and the proof of Theorem 4 give D(f) <= bs(f) deg(f); Theorem 4 itself states the resulting cubic bound in degree.
- **BSS2003.** Howard Barnum; Michael Saks; Mario Szegedy. *Quantum decision trees and semidefinite programming* (2003). [DOI 10.1109/CCC.2003.1214419](https://doi.org/10.1109/CCC.2003.1214419). Original spectral-adversary attribution confirmed in Spalek and Szegedy, Theorem 3.1 and reference 7. The original full text was not available in the packet or opened in this reconstruction; Appendix A supplies the complete argument used here.
- **SpalekSzegedy2006.** Robert Špalek; Mario Szegedy. *All quantum adversary methods are equivalent* (2006). [DOI 10.4086/toc.2006.v002a001](https://doi.org/10.4086/toc.2006.v002a001). Theorem 3.1 and equation (3.1) give the nonnegative spectral adversary formulation.
- **QuarticLeanPacket2026.** QuarticQuery project. *Supplied lean source and statement corpus for the nearly quartic query separation* (2026). Private source packet pinned at c7e0c9161f0ad898889bd9166e7b354acd42188d. Packet-relative source paths are used throughout. No public repository URL, DOI, or arXiv identifier is asserted.
- **ComplexitylibPin2026.** cslib-community contributors. *Complexitylib* (2026). [Primary source](https://github.com/cslib-community/complexitylib/tree/62ca5c21461b2482e8bd12b7cb9b4937d887a33a). Revision pinned by the supplied Lake manifest. The dependency source could not be retrieved during this reconstruction. Its imported theorem is identified from the supplied Appendix/TheoremA1.lean; no new build is claimed. No DOI or arXiv identifier applies to this pinned code citation.
- **AA18.** Scott Aaronson; Andris Ambainis. *Forrelation: A problem that optimally separates quantum from classical computing* (2018). [DOI 10.1137/15M1050902](https://doi.org/10.1137/15M1050902).
- **BS21.** Nikhil Bansal; Makrand Sinha. *k-forrelation optimally separates quantum and classical query complexity* (2021). [DOI 10.1145/3406325.3451040](https://doi.org/10.1145/3406325.3451040).
- **GTW21.** Uma Girish; Avishay Tal; Kewen Wu. *Fourier growth of parity decision trees* (2021). [DOI 10.4230/LIPIcs.CCC.2021.39](https://doi.org/10.4230/LIPIcs.CCC.2021.39).
- **SSW23.** Alexander A. Sherstov; Andrey A. Storozhenko; Pei Wu. *An optimal separation of randomized and quantum query complexity* (2023). [DOI 10.1137/22M1468943](https://doi.org/10.1137/22M1468943).
- **Tal20.** Avishay Tal. *Towards optimal separations between quantum and randomized query complexities* (2020). [Primary source](https://arxiv.org/abs/1912.12561).
- **Drucker2012.** Andrew Drucker. *Improved direct product theorems for randomized query complexity* (2012). [DOI 10.1007/s00037-012-0043-7](https://doi.org/10.1007/s00037-012-0043-7). Version 2, 9 May 2014. Relevant locators: Section 1.3; Lemmas 3.1–3.2, printed pp. 11–12; final paragraph of Section 3, printed p. 13. Theorem 1.1 has a different global-budget hypothesis.
- **Shaltiel2003.** Ronen Shaltiel. *Towards proving strong direct product theorems* (2003). [DOI 10.1007/s00037-003-0175-x](https://doi.org/10.1007/s00037-003-0175-x). Relevant locator: Section 5, Definition 4, Theorem 5 and Lemma 7, pp. 11–12 of the ECCC version. The statement is an XOR-advantage theorem for fair decision trees.
- **ABK2016.** Scott Aaronson; Shalev Ben-David; Robin Kothari. *Separations in query complexity using cheat sheets* (2016). [DOI 10.1145/2897518.2897644](https://doi.org/10.1145/2897518.2897644). Version 2, 9 July 2019. Relevant locators: Section 6.1, Definitions 14–15, printed pp. 20–21; Section 6.2, Lemma 17, printed p. 22. Use PDF numbering rather than the shifted extracted-TeX numbering.
- **GPW2018.** Mika Göös; Toniann Pitassi; Thomas Watson. *Deterministic communication vs. Partition number* (2018). [DOI 10.1137/16M1059369](https://doi.org/10.1137/16M1059369). ECCC TR15-050, revision text dated 5 September 2017. Relevant locators: Theorem 5 and Section 2.1, pp. 3–5 of the revision.
- **ABBLSS2015.** Andris Ambainis; Kaspars Balodis; Aleksandrs Belovs; Troy Lee; Miklos Santha; Juris Smotrovs. *Separations in query complexity based on pointer functions* (2015). [Primary source](https://arxiv.org/abs/1506.04719v3). Version 3, 26 October 2015. Relevant locator: Section 1, Use of a balanced tree, including the explicit discussion of direct pointers to one zero in every non-marked column. Also ECCC TR15-098, revision 2.
- **Yao1977.** Andrew Chi-Chih Yao. *Probabilistic computations: Toward a unified measure of complexity* (1977). [DOI 10.1109/SFCS.1977.24](https://doi.org/10.1109/SFCS.1977.24). Historical attribution for the distributional minimax principle; the needed finite-game proof is given in full in the reasoning record. Publisher metadata was verified; the original full text was not read in this pass.
- **BBHT1998.** Michel Boyer; Gilles Brassard; Peter Høyer; Alain Tapp. *Tight bounds on quantum searching* (1998). [DOI 10.1002/(SICI)1521-3978(199806)46:4/5<493::AID-PROP493>3.0.CO;2-P](https://doi.org/10.1002/%28SICI%291521-3978%28199806%2946:4/5%3C493::AID-PROP493%3E3.0.CO;2-P). Supplied text and proof locators refer to arXiv version 1 (23 May 1996), Section 4, Lemma 2 and Theorem 3. Journal pages follow the publisher record; its 493–505 differs from the arXiv metadata’s 493–506.
- **BHMT2002.** Gilles Brassard; Peter Høyer; Michele Mosca; Alain Tapp. *Quantum amplitude amplification and estimation* (2002). [DOI 10.1090/conm/305/05215](https://doi.org/10.1090/conm/305/05215). Proof locators use arXiv version 1 (15 May 2000), Section 2, Lemma 1 and equation (8).
- **DurrHoyer1996.** Christoph Dürr; Peter Høyer. *A quantum algorithm for finding the minimum* (1996). [Primary source](https://arxiv.org/abs/quant-ph/9607014). Version 2, revised 7 January 1999; Theorem 1 and Lemmas 1–2.
- **MandeParaasharSaurabh2023.** Nikhil S. Mande; Manaswi Paraashar; Nitin Saurabh. *Randomized and quantum query complexities of finding a king in a tournament* (2023). [DOI 10.4230/LIPIcs.FSTTCS.2023.30](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30). The proof locator Theorem 4.4 refers to the supplied arXiv text.
- **BenDavidKothari2026.** Shalev Ben-David; Robin Kothari. *Randomized query complexity can beat certificate complexity* (2026). [Primary source](https://arxiv.org/abs/2609.15063). Submitted 14 September 2026; Lemma 5 supplies the candidate-comparison-verification antecedent cited here.
<!-- /passage:ROOT-REFERENCES -->

