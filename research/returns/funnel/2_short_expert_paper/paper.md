**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# The optimal exponent for randomized and quantum queries: a Lean formalisation

*Review manuscript, 2 November 2026*

<!-- passage:abstract -->
**Abstract.** The optimal exponent in a universal bound between bounded-error randomized and quantum query complexity of total Boolean functions is four. We describe a Lean formalisation of OpenAI's nearly quartic separation, including a proof of the fixed-parameter Forrelation lower bound used in the construction. A winning column points to a zero in every other column, while its own all-one string defeats every incoming zero witness. This permits comparisons against opponents whose address instances violate their promises. A tournament samples products of the resulting comparison probabilities, with amplitude amplification preserving the conditional sampling law. The classical argument couples inputs differing at one hidden zero and one addressed certificate, and uses a per-instance-capped direct product theorem. The formal development gives a sharper hidden-zero estimate and a proof of the direct product by induction on sub-distributions. Its Forrelation argument combines a single bias-scaling path with previously known decision-tree growth methods.
<!-- /passage:abstract -->

## 1. The result

<!-- passage:query-model -->
For a total Boolean function $f:\{0,1\}^n\to\{0,1\}$, let $R(f)$ and $Q(f)$ denote its randomized and quantum bit-query complexities, with error at most $1/3$ on every input. The cost is the maximum number of queries over inputs, random choices and measurement branches. Computation between queries is unrestricted. Quantum access is through the usual oracle

<!-- statement:def-query-oracle -->
$$
O_x|i,b,z\rangle=|i,b\mathbin{\oplus}x_i,z\rangle.
$$

Write

<!-- statement:eq-1 -->
$$
\alpha_{\rm tot}
=\inf\left\{\alpha\geq0:
 \exists C_\alpha>0\ \forall n\geq1\
 \forall f:\{0,1\}^n\to\{0,1\},\
 R(f)\leq C_\alpha(1+Q(f))^\alpha\right\}.
$$
<!-- /passage:query-model -->

<!-- passage:headline -->
**Theorem 1 (OpenAI, Theorem 1.1).** The optimal power is $\alpha_{\rm tot}=4$. More precisely, $R(f)=O((1+Q(f))^4)$ for every total Boolean function. For each fixed integer $k\geq2$, there are positive constants $c_k,C_k,b_k$ and total Boolean functions $F_{k,m}$, for all sufficiently large powers of four $m$, such that

<!-- statement:thm-1.1 eq-2 -->
$$
Q(F_{k,m})\leq C_k\sqrt m\,(\log m)^{b_k},
\qquad
R(F_{k,m})\geq c_k\frac{m^{2-1/k}}{(\log m)^2}.
\tag{1}
$$

The supplied development records Lean checks of this theorem with no Forrelation hypothesis: its endpoint declarations are `QuarticQuery.alphaTot_eq_four_unconditional` and `QuarticQuery.theorem_1_1_unconditional`. Section 7 specifies the recorded checks and the limits of the present source audit.
<!-- /passage:headline -->

<!-- passage:mechanism -->
The separation and its construction are OpenAI's [Theorem 1.1 and Sections 2–5][OAI]. The input has columns, each with a candidate certificate. A winning column has an all-one string and a correctly addressed certificate pointing to a zero in every other column. When its address is decoded correctly, it disqualifies every opponent. An opponent cannot disqualify the winner, even at an arbitrary address, because the winner's string contains no zero. This asymmetry is what permits a cheap comparison despite off-promise address inputs. Comparisons among the other columns may have arbitrary probabilities; the tournament needs only their pairwise complementarity.

For each fixed $k$, (1) gives power $4-2/k$ up to logarithmic factors. The theorem excludes every universal smaller power by choosing $k$ before letting $m$ grow. It does not establish a single fixed-$k$ family with a fourth-power separation.
<!-- /passage:mechanism -->

<!-- passage:prior-work-outline -->
The universal quartic upper bound is due to [Aaronson, Ben-David, Kothari, Rao and Tal (2021), Theorem 2][ABKRT]; their Conjecture 2 proposed the cubic randomized bound excluded here. Addressed certificates originate in the cheat-sheet construction of [Aaronson, Ben-David and Kothari (2016), Sections 3 and 6][ABK]. OpenAI combines a separate certificate array in each column with the outward pointers and the probabilistic tournament. Our subject is the formalisation of that argument and the changes made while expressing its statements precisely.

Section 2 defines the total function. Sections 3 and 4 prove its quantum and randomized bounds. Section 5 supplies the Forrelation lower bound in the form needed here; Section 6 completes the exponent argument. Section 7 describes the formal models and reproduction procedure. All logarithms in the construction are to base two. Constants carrying a subscript $k$ may depend on the fixed integer $k$.
<!-- /passage:prior-work-outline -->

## 2. A certificate in each column

### 2.1. The address problem

<!-- passage:forrelation-definition -->
Let $m=4^t$, let $H$ be the normalized Walsh–Hadamard matrix of order $m$, and put $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$. A bit $a$ represents the sign $(-1)^a$, and $D_z$ denotes the diagonal matrix with sign vector $z$. For $k$ sign vectors define

<!-- statement:eq-3 eq-4 -->
$$
\Phi(z_1,\ldots,z_k)
 =u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,
\qquad \delta=2^{-5k},
$$
$$
P_{k,m}(z)=
\begin{cases}
1,&\Phi(z)\geq\delta,\\
0,&|\Phi(z)|\leq\delta/2,
\end{cases}
$$

with $P_{k,m}$ undefined elsewhere. In particular, a large negative value of $\Phi$ is outside the promise. This is the normalized $k$-Forrelation problem of [Bansal and Sinha (2021), equations (1.1)–(1.3)][BS], following Aaronson and Ambainis. The orthogonality of $H$ gives $|\Phi|\leq1$.
<!-- /passage:forrelation-definition -->

<!-- passage:forrelation-properties -->
We use three properties of this partial function. First, for each fixed $k\geq2$ and all sufficiently large $m$,

<!-- statement:eq-5 lem-2.1.i -->
$$
R(P_{k,m})>L,
\qquad
L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
\tag{2}
$$

Bansal and Sinha's Corollary 1.4 implies (2); Section 5 describes the proof incorporated in Lean. Second, a quantum routine computes a promised answer with error at most $\eta$ using $O_k(1+\log(1/\eta))$ queries. To see the relevant gap, prepare the matrix product defining $\Phi$ and measure the projection onto $u$. Its success probability is $\Phi^2$, at least $\delta^2$ on a one-input and at most $\delta^2/4$ on a zero-input. Repetitions with a threshold decision give the bound. Keeping all outcomes in registers makes this preparation reversible. The routine has a fixed query cap and produces a bit on every input, including off the promise.
<!-- /passage:forrelation-properties -->

<!-- passage:exact-circuit -->
Third, an exact fan-in-two circuit with $S=O_k(m(\log m)^2)$ non-input gates produces bits $d,b$, with $d=1$ exactly on the domain of $P_{k,m}$ and $b=P_{k,m}$ there. This exact domain test will certify a proposed address. If $W=\sqrt m\,H$, then

<!-- statement:claim-N-phi claim-integer-tests -->
$$
N=z_1^{\mathsf T}WD_{z_2}W\cdots WD_{z_k}{\bf1},
\qquad
M=m(\sqrt m)^{k-1},
\qquad \Phi=N/M,
$$
$$
\Phi\geq\delta\ \Longleftrightarrow\ 2^{5k}N\geq M,
\qquad
|\Phi|\leq\delta/2\ \Longleftrightarrow\ 2^{5k+1}|N|\leq M.
\tag{3}
$$

All quantities in the comparisons are integers. The unnormalized Hadamard transforms use $O(m\log m)$ additions and subtractions, and their intermediate values have $O_k(\log m)$ bits. Binary arithmetic therefore gives the stated Boolean circuit size. The domain output is the disjunction of the tests in (3); the value output is the first test. This is [OpenAI, Lemma 2.1(iii)][OAI], implemented by the formal circuit construction.
<!-- /passage:exact-circuit -->

### 2.2. Winners and local tests

<!-- passage:layout -->
Set $\ell=\log_2m=2t$ and $r=20\log_2m=40t$. Column $i$ contains a string $X_i\in\{0,1\}^m$, address instances $A_{i,1},\ldots,A_{i,r}\in\{0,1\}^{km}$, and its own array of cells $B_{i,s}$ indexed by $s\in\{0,1\}^r$. A cell contains one $\ell$-bit pointer $p_{i,s,j}\in[m]$ for each $j\neq i$, together with $r$ alleged evaluations of the exact circuit. Each evaluation stores one bit per non-input gate, including the outputs. Actual input bits are read from $A_{i,h}$ when needed; they are never accepted from a copied transcript.

If all address instances in column $i$ are promised, its true address is

<!-- statement:eq-7 -->
$$
s_i=(P(A_{i,1}),\ldots,P(A_{i,r})).
$$
<!-- /passage:layout -->

<!-- passage:winner-definition -->
A column is a *winner* if $X_i=1^m$, its true address is defined, and $B_{i,s_i}$ contains the correct circuit evaluations and pointers satisfying

<!-- statement:eq-8 -->
$$
X_j[p_{i,s_i,j}]=0\qquad(j\neq i).
\tag{4}
$$

The total Boolean function $F_{k,m}$ is one precisely when a winner exists. This imposes no promise on its input. Undefined address instances and false transcripts simply fail the winner predicate. There is at most one winning column: the pointer from one purported winner to another would find a zero in an all-one string.

For example, with four columns, an all-one $X_1$ can disqualify $X_2=1011$, $X_3=1101$ and $X_4=0111$ by pointing respectively to positions $2,3,1$. Those strings cannot disqualify $X_1$ at any pointer value. This illustrates the pointer condition only; the address instances and transcripts must still satisfy the separate conditions above.
<!-- /passage:winner-definition -->

<!-- passage:local-tests -->
For a specified pair $(i,s)$, the winner conditions are a conjunction of

<!-- statement:def-K lem-2.2.i -->
$$
K=m+(m-1)+r(S+2)=O_k(m(\log m)^3)
\tag{5}
$$

exact tests: one for each bit of $X_i$, one for each outward pointer, one for each stored gate value, and two for each transcript's outputs. The output tests require $d=1$ and $b=s_h$. A topological induction proves that consistent gate values form the unique correct evaluation.

Each test has a deterministic adaptive decision tree of depth at most $\max(3,\ell+1)$. A pointer test reads its $\ell$ pointer bits, then reads the selected target bit. The selected bit varies with the pointer, so this is a query-depth statement. It is not a bound on the number of fixed coordinates on which the test depends. A gate test reads at most three bits.

These tests also have coherent implementations with a constant-factor overhead: load the required input bits, compute the result reversibly, and unload. An input-dependent address is computed in registers before the relevant bit query. Consequently the same construction works with a superposed test index. A winner has one address at which every test passes, whereas a nonwinner has a failing test at every address.
<!-- /passage:local-tests -->

## 3. Quantum comparisons with arbitrary nonwinners

### 3.1. A comparison that tolerates off-promise inputs

<!-- passage:comparison -->
Fix an arbitrary input to $F_{k,m}$. We shall use

<!-- statement:def-T-eps -->
$$
T=\lceil\log_2(1000m)\rceil,\qquad
\epsilon=\frac1{1000T}.
\tag{6}
$$

Decode a column by computing each of its $r$ partial-function answers with error at most $\epsilon/r$. A winning column's whole address is correct with probability at least $1-\epsilon$. The query count is $O_k(r\log(r/\epsilon))$, and the decoder returns some address even when its instances are off promise.

To compare distinct columns, sort their indices and use a fixed circuit for that unordered pair. Decode both, read each column's pointer toward the other at its decoded address, and inspect both target bits. If exactly one column points to a zero, it wins the comparison; otherwise the smaller index wins. All address and work registers are retained. Let $a_{ij}$ be the probability of reporting $i$ as victorious over $j$, and set $a_{ii}=0$. Then

<!-- statement:eq-10 eq-11 -->
$$
a_{ij}+a_{ji}=1\quad(i\neq j),\qquad a_{ii}=0,
\qquad
a_{i_*j}\geq1-\epsilon\quad(j\neq i_*)
\tag{7}
$$

whenever $i_*$ is a winner. Only its own successful decoding is needed for the last inequality. Every opponent's incoming pointer fails against $X_{i_*}=1^m$, regardless of its decoded address. Retained address labels are orthogonal, so the coherent preparation has exactly the probabilities just described.
<!-- /passage:comparison -->

### 3.2. Amplification preserves the successful distribution

<!-- passage:amplification-statement -->
We need a sampler with both a worst-case cost bound and the correct conditional output law. For $0<\gamma\leq1/2$ and $0<\eta<1/2$, [OpenAI, Lemma 3.1][OAI] gives one procedure, with call counts depending only on $\gamma,\eta$, using $O(\gamma^{-1/2}\log(1/\eta))$ calls to a preparation $A$ and its inverse. For every success probability $p$, it either fails or returns a successful outcome with the same conditional state as $A$. Its failure probability is at most $\eta$ when $p\geq\gamma$, and it always fails when $p=0$. The call cap holds on every branch for every $p$.

The procedure must be chosen before the oracle-dependent $p$ is known. Choosing a favourable number of Grover iterations separately for each input would not define the required query algorithm.
<!-- /passage:amplification-statement -->

<!-- passage:amplification-proof -->
For $0<p<1$, decompose the prepared state into normalized successful and unsuccessful components:

<!-- statement:claim-grover-state -->
$$
A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle.
$$

After $j$ Grover iterations it is

<!-- statement:claim-grover-state -->
$$
\sin((2j+1)\theta)|g\rangle+\cos((2j+1)\theta)|b\rangle.
\tag{8}
$$

Successful projection therefore leaves $|g\rangle$ up to phase. This is the two-dimensional rotation in [Brassard, Høyer, Mosca and Tapp (2002), Lemma 1 and equation (8)][BHMT].

Put $M=\lceil10/\sqrt\gamma\rceil$. In a trial, choose $j=0$ with probability $1/2$ and otherwise choose $j$ uniformly from $0,\ldots,M-1$. If $p\geq1/2$, the zero-iteration choice succeeds with probability at least $1/4$. If $\gamma\leq p\leq1/2$, then $\sin(2\theta)=2\sqrt{p(1-p)}\geq\sqrt\gamma$, and a geometric-series calculation gives

<!-- statement:eq-9 -->
$$
\frac1M\sum_{j=0}^{M-1}\sin^2((2j+1)\theta)
\geq\frac12-\frac1{2M|\sin(2\theta)|}
\geq\frac9{20}.
\tag{9}
$$

Thus each trial succeeds with probability at least $9/40$. A fixed $\lceil\log(1/\eta)/\log(40/31)\rceil$ trials suffice. Every successful trial has the same conditional state, so randomizing the iteration count and stopping at the first success preserve it. The cases $p=0,1$ follow directly. Random iteration counts have the antecedent of [Boyer, Brassard, Høyer and Tapp (1998), Section 4][BBHT].
<!-- /passage:amplification-proof -->

### 3.3. The fractional tournament

<!-- passage:tournament-drift -->
For a sequence of previously selected pivots $p_1,\ldots,p_t$, put $w_i=\prod_{b=1}^t a_{ip_b}$ and $W=\sum_iw_i$, with empty products equal to one. An ideal process samples the next pivot $p$ with probability $w_p/W$ and updates $w_i\leftarrow w_ia_{ip}$. If $W=0$, it stops. Pairing the terms indexed by $(i,p)$ and $(p,i)$ yields

<!-- statement:eq-13 -->
$$
\mathbb E[W_{\rm new}\mid w]
=\frac1W\sum_{p,i}w_pw_i a_{ip}
=\frac{W^2-\sum_iw_i^2}{2W}
\leq\frac W2.
\tag{10}
$$

The inequality also holds at the absorbing zero state. After $T$ stages, $\mathbb E W_T\leq m/2^T$. If the winner has never been selected, its weight is at least $(1-\epsilon)^T\geq1-T\epsilon>1/2$. Markov's inequality gives

<!-- statement:eq-14 -->
$$
\Pr[i_*\text{ absent from the ideal list}]
\leq \frac{2m}{2^T}.
\tag{11}
$$

This proof uses complementarity, without a ranking or transitivity among the candidates. Even a deterministic cycle among nonwinners causes no difficulty. Nor is a gap between their comparison probabilities and $1/2$ required.
<!-- /passage:tournament-drift -->

<!-- passage:tournament-sampler -->
To implement a stage, prepare a uniform candidate and compare it with each previous pivot in a fresh coherent workspace. Before marking success, the state is

<!-- statement:eq-15 -->
$$
\frac1{\sqrt m}\sum_{i=1}^m
 |i\rangle\bigotimes_{b=1}^t|\varphi(i,p_b)\rangle.
\tag{12}
$$

Mark success exactly when all comparisons favour $i$. The tensor product makes its conditional probability, for that index, equal to $w_i$. Orthogonality of the candidate labels then gives total probability $W/m$ and conditional index law $w_i/W$. Retaining garbage is essential: the successful state includes the comparison workspaces whose probabilities produce these weights.

Amplify with $\gamma=1/(2m)$ and $\eta=\epsilon$. Until $i_*$ is selected, its weight exceeds $1/2$, so the success threshold holds. At every previous history the real sampler either terminates with probability at most $\epsilon$ or produces exactly the ideal pivot law. Coupling stage by stage adds at most $T\epsilon$ to (11). No independence between a stage's failure probability and its history is used. Once the winner is listed, later termination cannot remove it.

If a comparison costs at most $c$ queries, stage $t$ uses $O(c(t+1))$ queries per preparation or reversal. Summing the amplification costs gives $O(c\sqrt m\,T^2\log T)$ queries and at most $T$ candidates. The cap holds even when no winner exists.
<!-- /passage:tournament-sampler -->

<!-- passage:tournament-formal-route -->
The formal quantum implementation proves the exact conditional law of the measured candidate label. Its repeated trials measure the full computational basis, read the candidate label, and reset the resulting known basis state; this supplies the distribution used above. The abstract full-state amplification theorem is proved separately. Likewise the final program's tournament theorem passes each candidate to a verifier, whereas the preprint states a stand-alone list-output theorem. The proof above explains that list formulation; the correspondence records the difference between these interfaces.
<!-- /passage:tournament-formal-route -->

### 3.4. Verification on every input

<!-- passage:candidate-verification -->
For each candidate, decode its address afresh and search its $K$ local tests for a failure. Preparing a uniform test index gives failure probability zero when all tests pass and at least $1/K$ otherwise. Amplification with threshold $1/K$ and error $\epsilon$ uses $O(\sqrt K\log(1/\epsilon)\log m)$ bit queries.

Exact testing cannot invent a failed test. A true winner is therefore accepted whenever its address is correctly decoded. For a nonwinner every address contains a failure, so its acceptance probability is at most $\epsilon$, including after an off-promise decoding. Accept if any candidate verifies. The two error bounds are

<!-- statement:claim-error -->
$$
\Pr[\text{error}\mid F_{k,m}=0]\leq T\epsilon,\qquad
\Pr[\text{error}\mid F_{k,m}=1]
\leq\frac{2m}{2^T}+T\epsilon+\epsilon<\frac13.
\tag{13}
$$

Equations (5)–(6) and the decoder cost prove $Q(F_{k,m})\leq\sqrt m(\log m)^{O_k(1)}$. All array accesses use the ordinary bit oracle: compute the global coordinate reversibly, read the physical pointer bits, then query the selected target. Controlled reads can be implemented by loading, using and unloading an input bit. No additional addressing oracle is assumed.
<!-- /passage:candidate-verification -->

## 4. The randomized lower bound

### 4.1. Independent answers under interleaved queries

<!-- passage:direct-product -->
We use the per-instance-capped direct product described in [Drucker (2012), Section 1.3 and Lemmas 3.1–3.2][DRU], following Shaltiel. Suppose $\mu$ is supported on the promise domain of a partial Boolean function $P$, and every deterministic depth-$L$ tree computes $P$ under $\mu$ with success at most $\beta$. On independent $U_1,\ldots,U_r\sim\mu$, any algorithm making at most $L$ queries to each input guesses all answers with probability at most $\beta^r$. Queries may be interleaved adaptively; independent side information and random coins are allowed.

The preprint proves this with a product of conditional optimal-success values. Lean uses an induction on nonnegative, unnormalized input weights. This removes division by transcript probabilities and treats zero-mass branches without a separate case.
<!-- /passage:direct-product -->

<!-- passage:weighted-recursion -->
For a nonnegative weight $\nu$ on one input, let $v_q(\nu)$ be the greatest weighted success of a depth-$q$ tree. If $\nu_{j,b}(x)=\nu(x)\mathbf1_{\{x_j=b\}}$, its recursion is

<!-- statement:new-dp-recursion -->
$$
\begin{aligned}
v_0(\nu)&=\max_{b\in\{0,1\}}\sum_{x:P(x)=b}\nu(x),\\
v_{q+1}(\nu)&=\max\left(\{v_q(\nu)\}\cup
 \{v_q(\nu_{j,0})+v_q(\nu_{j,1}):j\in[n]\}\right).
\end{aligned}
\tag{14}
$$

The first option permits any strategy using at most $q$ queries. Finiteness gives an attaining tree, and induction proves that this recursion bounds every tree of the specified depth.
<!-- /passage:weighted-recursion -->

<!-- passage:weighted-product -->
More generally, if a multi-input tree has remaining budgets $q_h$ and product weight $\prod_h\nu_h$, its weighted probability of guessing every answer is bounded by

<!-- statement:new-dp-weighted -->
$$
\text{weighted all-answer success}\leq\prod_{h=1}^r v_{q_h}(\nu_h).
\tag{15}
$$

Induct on the tree. At a leaf, the all-correct event is a Cartesian product, and its weight factors into the single-input constant-guess successes. At a query to input $h$, the two children restrict only $\nu_h$ and spend one unit only from $q_h$. Every other factor is unchanged and nonnegative. Factor these common terms out of the sum of the child bounds; (14) absorbs the two remaining terms. This proves (15) for an arbitrary adaptive query schedule.

Initially $q_h=L$ and $\nu_h=\mu$, so each factor is at most $\beta$. Fixing the independent side information and coins first, then averaging, proves the capped direct product. The formal lemmas are the weighted bound and its averaging consequences; the conditional-supermartingale proof is an alternative prose argument, not the checked derivation used here.
<!-- /passage:weighted-product -->

<!-- passage:minimax -->
By (2), finite minimax supplies a distribution $\mu$ on $\operatorname{dom}P$ under which every depth-$L$ tree has success at most $2/3$. Indeed, there are finitely many depth-$L$ trees; a mixture achieving success at least $2/3$ on every promised input would contradict $L<R(P)$. Minimax therefore supplies a single hard measure. The preceding direct product bounds any capped guess of $r$ independent answers by $(2/3)^r$.

The support condition matters. The Gaussian distributions used later to prove (2) need not be supported on the promise. The measure used for planting is obtained from minimax after the worst-case lower bound has been established.
<!-- /passage:minimax -->

### 4.2. A coupled pair of inputs

<!-- passage:planting -->
Construct a dummy input $Y^{(0)}$ by choosing, independently in each column, a uniform zero position $J_i\in[m]$ and setting every other bit of $X_i$ to one. Draw all $A_{i,h}$ independently from $\mu$, independently also of the zeros. Fill all cells with a fixed blank pattern. Every column contains a zero, so $F(Y^{(0)})=0$.

Choose $I$ uniformly from $[m]$, independently of the dummy input. Form $Y^{(1)}$ by erasing the zero of $X_I$ and filling its true-address cell with correct transcripts and the pointers $p_{I,s_I,j}=J_j$. All address instances are promised, so this gives a winner and $F(Y^{(1)})=1$.

Fix a deterministic tree of depth at most $G$, and inspect its dummy execution. Before its first query to the erased zero or to the filled cell, both executions see the same answers and therefore make the same subsequent queries. Their acceptance-probability difference is bounded by the probabilities of these two encounters. Counting any visit to the cell remains an upper bound even if the visited bit has not changed.
<!-- /passage:planting -->

### 4.3. Searching for the erased zero

<!-- passage:zero-search-induction -->
The formal proof improves the preprint's $4G/m^2$ estimate to $2G/m^2$. Fix all data except the zero position in one chosen string $X_i$, and allow that zero to range over a finite set $U$. Let $N_U$ count the worlds in which the tree finds that zero, and let $S_U$ sum the numbers of queries to $X_i$ over all worlds indexed by $U$, whether or not the zero is found. A tree induction gives $|U|N_U\leq2S_U$.

A query outside $X_i$ has the same answer in all these worlds and incurs no charge. A query to $X_i$ at a position outside $U$ goes to the same child in every world and increases the charge. For a query at $p\in U$, put $n=|U\setminus\{p\}|$, and let $N,S$ be the find count and subsequent query sum for the other $n$ worlds. The zero-at-$p$ world is found immediately; every other world pays for this query before continuing. Thus $N_U=1+N$ and $S_U\geq1+n+S$. Induction gives $nN\leq2S$, while $N\leq n$. Hence $(n+1)(1+N)\leq2S+2n+1\leq2S_U$, as required.

With $|U|=m$, division by the number of worlds bounds a column's find probability by $2/m$ times its expected query count. Sum over the columns, whose charged queries total at most $G$, and average over the independent $I$. The result is

<!-- statement:new-zero-search-two -->
$$
\Pr[\text{dummy execution queries }X_I[J_I]]
\leq\frac{2G}{m^2}.
\tag{16}
$$

The induction permits adaptive queries and charges repeated coordinates, so the bound uses the stated worst-case query cap.
<!-- /passage:zero-search-induction -->

### 4.4. Guessing the planted address

<!-- passage:heavy-simulator -->
Call column $i$ heavy if the complete dummy run makes more than $L$ queries in total to $A_{i,1},\ldots,A_{i,r}$, counting repetitions. At most $G/L$ columns are heavy. Independence of $I$ therefore bounds the probability that the planted column is heavy by $G/(mL)$.

For a fixed column $i$ and query time $t$, give a simulator all the dummy data outside these $r$ address instances as free side information. That information is independent of the target instances. Simulate the original tree until it proposes query $t$, aborting before an $(L+1)$st query to the target instances in total. If the proposed query lies in $B_{i,s}$, output $s$ as the answer vector; otherwise output a fixed vector.

This simulator uses at most $L$ target queries in total, and therefore at most $L$ on each instance. On the joint event that $i$ is nonheavy and query $t$ visits $B_{i,s_i}$, it has not aborted and guesses correctly. The direct product thus gives

<!-- statement:eq-21 -->
$$
\Pr[i\text{ is nonheavy and query }t\text{ visits }B_{i,s_i}]
\leq(2/3)^r.
\tag{17}
$$

The joint event is essential. Conditioning the hard input law on the eventual choice of a nonheavy column can bias its answers; the simulator argument performs no such conditioning. Union-bound over $G$ times and average over $I$, then add the heavy contribution:

<!-- statement:eq-22 -->
$$
\Pr[\text{dummy execution visits }B_{I,s_I}]
\leq\frac{G}{mL}+G(2/3)^r.
\tag{18}
$$

The formal implementation bounds the union of the nonheavy-and-cell events directly. This is the same inference needed for (18), without a separately packaged per-time theorem.
<!-- /passage:heavy-simulator -->

<!-- passage:classical-gap -->
Define $\Delta=\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]$. The first-difference argument and (16), (18) yield the one-sided estimate

<!-- statement:new-planted-gap-two -->
$$
\Delta\leq\frac{2G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\tag{19}
$$

This is the direction formalised in the improved bound and the one required for the contradiction. Set $G=\lfloor mL/100\rfloor$. Eventually $1\leq L\leq m$, so the first two terms are at most $2/100$ and $1/100$. Since $r=20\log_2m$, the last term tends to zero. Thus (19) is less than $1/3$ for sufficiently large $m$.

The same estimate holds for any randomized mixture of depth-$G$ trees. An algorithm with error at most $1/3$ on every input would have acceptance probability at most $1/3$ on the dummy distribution and at least $2/3$ on the planted distribution, giving $\Delta\geq1/3$. This contradiction proves $R(F_{k,m})>G$ and, on removing the floors, the lower bound in (1). The circuit size was irrelevant to this lower-bound argument; only exact certification and the hardness of its address function were used.
<!-- /passage:classical-gap -->

## 5. The fixed-parameter Forrelation lower bound

### 5.1. The statement and its sources

<!-- passage:forrelation-scope -->
The remaining input is (2), with $k$ fixed before $m$ tends to infinity. [Bansal and Sinha, Theorem 1.3][BS], state the stronger bound $\Omega(k^{-29}(m/\log(km))^{1-1/k}\eta^2)$ for error $1/2-\eta/2$; Corollary 1.4 gives its bounded-error specialization. The Lean endpoint proves (2). It does not supply that theorem's uniform dependence on $k$ and $\eta$, and its logarithmic denominator is weaker.

The checked proof uses correlated Gaussian vectors, bounded coordinate means and integration by parts, as in Bansal and Sinha. Its interpolation changes one block of means, and its derivatives propagate along one chain of blocks. Its decision-tree growth argument uses the martingale method of [Girish, Tal and Wu, Section 1.3 and Lemma 9][GTW], applied directly to bounded biased signs. These methods have established sources. We claim an alternative proof of the stated fixed-$k$ input, with its details expressed in Lean; we make no priority claim for the method.
<!-- /passage:forrelation-scope -->

### 5.2. A bounded Gaussian path

<!-- passage:forrelation-truncation -->
For a function $g$ on signs, write $\widetilde g(\mu)$ for its expectation under independent signs with coordinate means $\mu$. This is its multilinear extension. Let $D_a g$ be half the difference between fixing coordinate $a$ to $+1$ and to $-1$. Then $\partial_a\widetilde g=\widetilde{D_ag}$ and $D_a^2g=0$.

The smoothing functions are algebraic:

<!-- statement:new-fl-truncation -->
$$
q(x)=\sqrt{2+x^2},\qquad
\Psi(x)=\frac1{2q(x)},\qquad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3},
\qquad \varphi'(x)=\frac3{q(x)^5}.
\tag{20}
$$

Here $\varphi$ is odd, $|\varphi|\leq1/2$, $0<\Psi\leq1$ and $0<\varphi'\leq3$. If $\gamma$ denotes the standard Gaussian density, then $(\Psi\gamma)'=-\varphi\gamma$. Consequently, for a standard Gaussian $Z$ and a continuously differentiable function $G$ with bounded $G$ and $G'$,

<!-- statement:new-fl-stein -->
$$
\mathbb E[\varphi(Z)G(Z)]
=\mathbb E[\Psi(Z)G'(Z)].
\tag{21}
$$

Integration by parts proves (21): the bounded factor and Gaussian decay remove the boundary term. This identity supplies both a bounded bias and a controlled derivative weight.
<!-- /passage:forrelation-truncation -->

<!-- passage:forrelation-path -->
Index the $k$ sign blocks by $0,\ldots,k-1$. Take independent standard Gaussian vectors $U_0,\ldots,U_{k-2}\in\mathbb R^m$ and put $V_j=HU_j$. For $s\in[0,1]$, give block $0$ the coordinate means $s\varphi(U_0)$, interior block $j$ the means $\varphi(V_{j-1})\varphi(U_j)$, and block $k-1$ the means $\varphi(V_{k-2})$; products are coordinatewise. Denote this vector of means by $w_s$. Every coordinate has magnitude at most $1/2$.

Conditionally on the Gaussians, round these means to independent signs. Let $\mathcal D$ be the resulting law at $s=1$. At $s=0$ the averaged law is uniform. This assertion requires averaging: most coordinates of $w_0$ are not zero. First clear the zero-mean first block. Each nonconstant monomial in the next block contains a nonempty product of odd factors $\varphi(V_0(a))$. A coordinate reflection of $V_0$ preserves its joint Gaussian law and reverses that monomial; all later blocks depend only on later independent Gaussian vectors. Averaging therefore clears this block as well. Iterating clears all blocks. Orthogonality of $H$ supplies the reflection invariance at each step.

Apply the ordinary mean-value theorem to $s\mapsto\mathbb E\widetilde g(w_s)$. Differentiation starts in block $0$. Applying (21) in $U_0(a_0)$ cannot differentiate that same sign coordinate again, since its second multilinear derivative vanishes. It instead differentiates the next block, introducing $H_{a_1a_0}\Psi(U_0(a_0))\varphi'(V_0(a_1))$. Repeating this argument passes to the next independent Gaussian vector. Previously accumulated weights depend only on earlier vectors, so they introduce no extra derivatives.

For some $s\in(0,1)$, depending on $g$, the result is

<!-- statement:new-fl-path -->
$$
\mathbb E_{\mathcal D}g-\mathbb E_{\rm unif}g
=\sum_{a_0,\ldots,a_{k-1}}
\mathbb E\!\left[
c_a(U)\,
\partial_{0,a_0}\cdots\partial_{k-1,a_{k-1}}
\widetilde g(w_s)\right],
\tag{22}
$$

<!-- statement:new-fl-path-weight -->
$$
c_a(U)=\prod_{j=0}^{k-2}
H_{a_{j+1}a_j}\Psi(U_j(a_j))\varphi'(V_j(a_{j+1})),
\qquad
|c_a(U)|\leq(3/\sqrt m)^{k-1}.
$$

Thus only $k$-fold derivatives, one coordinate from each block, need a bound. These derivatives are evaluated at biased product measures. Equation (22) does not assert that the uniform Fourier coefficients above degree $k$ vanish. The formal proof uses the displayed mean-value identity; its parameter $s$ need not be shared by different functions.
<!-- /passage:forrelation-path -->

### 5.3. Growth along an adaptive decision tree

<!-- passage:forrelation-growth -->
Let $g$ be the acceptance indicator of a deterministic tree of depth at most $d$, where $d\geq1$. At a fixed vector of means $|\mu_a|\leq1/2$, set $\xi_a=(Z_a-\mu_a)/(1-\mu_a^2)$ for independent signs $Z_a$. These centered variables satisfy $|\xi_a|\leq2$. Biased derivatives of $\widetilde g$ are expectations of $g$ against products of distinct $\xi_a$.

To bound a sum of absolute derivatives, choose the signs of their coefficients and form the corresponding degree-$k$ polynomial. Put $N=km$. For a revealed coordinate set $B$, consider $C_j(B)=\sum_{J\subseteq B,\ |J|=j}c_J\prod_{a\in J}\xi_a$, where $|c_J|\leq1$. A fresh query to coordinate $q$ changes this polynomial by $\xi_q C_{j-1}^{(q)}(B)$, with contracted coefficients $c_{J\cup\{q\}}$. A repeated query changes nothing. The fresh factor is centered conditionally on the preceding answers.

Stop at the first time a contraction exceeds $\kappa^{j-1}$ in absolute value. Through that query, the increments have magnitude at most $2\kappa^{j-1}$, since their coefficients use previously revealed values. For either sign, Azuma's bound at threshold $\kappa^j$ is $\exp(-\kappa^2/(8d))$. Set $\kappa^2=8d\Lambda$. If $p_j$ is the worst threshold-crossing probability over the coefficient arrays, the two signs and at most $N$ contractions give $p_j\leq2e^{-\Lambda}+2Np_{j-1}$, starting with $p_0=0$. Thus $p_j\leq(4N)^j e^{-\Lambda}$. At a leaf, the good-event bound is $\kappa^k$ and the unconditional finite-coordinate bound is $(2N)^k$. Conditional expectation clears the unrevealed centered variables, so these bounds control the required expectation against $g$. The stopped-process estimate is applied before any conditioning on the good event.

This is the growth mechanism of [Girish, Tal and Wu, Lemma 9][GTW]. The formal proof works directly with the biased variables above, so it needs no separate random-restriction transfer theorem. With $\Lambda>0$ and $\kappa>0$ satisfying $\kappa^2=8d\Lambda$, the resulting estimate, combined with (22), is

<!-- statement:new-fl-advantage -->
$$
\left|\mathbb E_{\mathcal D}g-\mathbb E_{\rm unif}g\right|
\leq
\left(\frac3{\sqrt m}\right)^{k-1}
\left\{\kappa^k+(2km)^k(4km)^k e^{-\Lambda}\right\}.
\tag{23}
$$

Indeed, the sum of the absolute biased $k$-fold derivatives over any family of distinct $k$-element coordinate sets is at most the expression in braces. The sets in (22) form such a family. Its coefficient bound can therefore be taken outside the sum and the Gaussian expectation.

Choose $\Lambda=2k\ln(4km)$, where $\ln$ is the natural logarithm. The second term in braces is at most one. For $d=2\tau L+1$, fixed $k$ and fixed integer $\tau$, the first contribution to (23) is $O_{k,\tau}((\log m)^{-k/2})$, by (2)'s definition of $L$. The remaining contribution also tends to zero. Thus the right side is eventually at most any prescribed positive constant depending on $k$.
<!-- /passage:forrelation-growth -->

### 5.4. Turning moments into a promise lower bound

<!-- passage:forrelation-moments -->
The two laws just used are not supported entirely on the Forrelation promise. We need estimates that account for the unpromised region. The checked moment calculations give

<!-- statement:new-fl-moments -->
$$
\mathbb E_{\rm unif}\Phi=0,\qquad
\mathbb E_{\rm unif}\Phi^2=\frac1m,\qquad
\mathbb E_{\mathcal D}\Phi\geq18^{-(k-1)}.
\tag{24}
$$

For the first two identities, expand the multilinear path polynomial and use the orthogonality of distinct sign monomials. For the last, apply the chain calculation to $\Phi$ itself. Matching Hadamard entries occur in squares. The remaining factors are positive Gaussian expectations of $\Psi$ times $\varphi'$. The tangent bound for the logarithm at $3$ gives $\Psi(x)\varphi'(y)\geq18^{-1}\exp(-[(x^2-1)+5(y^2-1)]/6)$. For two standard Gaussian coordinates, Jensen's inequality and their unit second moments give expectation at least $1/18$. No independence between those two coordinates is needed. Different links use independent vectors $U_j$, and the squared Hadamard path weights sum to one after the outer normalization. This gives the last inequality in (24). The formal calculation iterates the same expectations.
<!-- /passage:forrelation-moments -->

<!-- passage:forrelation-gap -->
Suppose that an $L$-query randomized algorithm computes $P_{k,m}$ with error at most $1/3$. Repeat it $2\tau$ times and take a majority, with a fixed tie rule. Its error on promised inputs is at most $\varepsilon_0=(8/9)^\tau$, and every deterministic tree in the resulting mixture has depth at most $2\tau L$. Write $a(z)$ for its acceptance probability.

On all inputs, including unpromised ones, we have $(1-\varepsilon_0)(\Phi(z)-\delta)\leq a(z)$ and $a(z)\leq\varepsilon_0+4\Phi(z)^2/\delta^2$. For the first inequality, use the promised one-input guarantee when $\Phi\geq\delta$; elsewhere the left side is nonpositive. For the second, use the promised zero-input guarantee when $|\Phi|\leq\delta/2$; elsewhere its right side is at least one. Averaging and applying (24) gives

<!-- statement:new-fl-gap -->
$$
\mathbb E_{\mathcal D}a-\mathbb E_{\rm unif}a
\geq
(1-\varepsilon_0)\bigl(18^{-(k-1)}-\delta\bigr)
-\varepsilon_0-\frac4{\delta^2m}.
\tag{25}
$$

Choose $\tau$ after fixing $k$, so that $\varepsilon_0\leq\delta$. For $k\geq2$, $18^{-(k-1)}\geq32\delta$ and $\delta\leq1/1024$. Hence, once $m$ is large enough, (25) is greater than $\delta$. But (23), applied to each tree and averaged over the mixture, is eventually at most $\delta$. This contradiction proves (2).

The Gaussian law serves only to rule out a shallow randomized algorithm. The hard distribution used in Section 4 is obtained afterwards by finite minimax and is supported on promised inputs. Identifying these two distributions would invalidate the direct-product application.
<!-- /passage:forrelation-gap -->

## 6. The exponent and its quantifiers

<!-- passage:exponent -->
Fix a proposed universal exponent $\alpha<4$, with $\alpha\geq0$. Choose an integer $k\geq2$ such that $4-2/k>\alpha$, then keep $k$ fixed. For the family in (1),

<!-- statement:claim-exponent-ratio -->
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\geq c_{k,\alpha}
\frac{m^{\,2-1/k-\alpha/2}}
     {(\log m)^{\,2+\alpha b_k}}
\longrightarrow\infty.
\tag{26}
$$

The positive power of $m$ dominates the fixed logarithmic power. Given any proposed constant $C_\alpha$, choose $m$ beyond the family threshold and large enough that this ratio exceeds $C_\alpha$. Thus no $\alpha<4$ is a universal exponent. The order is: choose $\alpha$, choose $k$, fix all constants and thresholds belonging to that $k$, then choose $m$ against $C_\alpha$. Letting $k$ vary with $m$ would require bounds uniform in $k$, which (1) does not supply.

The universal quartic upper bound supplies the reverse inequality for $\alpha_{\rm tot}$. The formal development derives $D(f)\leq20736\,Q(f)^4$ from the imported complexity library through the model bridges, then uses $R(f)\leq D(f)$. Its mathematical source is [Aaronson et al., Theorem 2][ABKRT]. This proof route does not reproduce every intermediate lemma of the preprint's Appendix A.

Already $k=3$ gives exponent $10/3$ up to logarithms, so the ratio $R(F_{3,m})/(1+Q(F_{3,m}))^3$ diverges. The separate formal endpoint `QuarticQuery.cubic_bound_fails_unconditional` records this consequence. The full family, with arbitrarily large fixed $k$, establishes $\alpha_{\rm tot}=4$.
<!-- /passage:exponent -->

## 7. What the formalisation establishes

### 7.1. Mathematical statements and models

<!-- passage:formal-changes -->
Three changes are visible in the mathematics. The hidden-zero argument proves the constant $2$ in (16), improving the preprint's constant $4$. The direct-product theorem is proved by induction on nonnegative, unnormalised weights, which handles zero-mass branches without conditional probabilities. Finally, a local certificate test is specified by its adaptive query depth: its target coordinate can depend on the pointer it has just read.

The formal quantum model also makes several obligations explicit. Query count is a worst-branch cap; amplification has a fixed repetition count. An off-promise address computation still returns an address within that cap. A fresh comparison workspace is allocated for each factor in the sampling product. Successful amplification preserves the required conditional law, and the measured sampler resets a known full basis state before retrying. These details connect the probabilistic tournament to a finite quantum program.

Some useful intermediate formulations have different formal counterparts. The general list-output tournament statement in the preprint is implemented in the final upper bound by running the verifier inside the tournament and bounding acceptance. The abstract amplification theorem proves preservation of the full normalized good state; the sampler used by the final algorithm has a directly proved conditional label law. Neither observation weakens the final query bound, but each matters when matching a displayed paper statement to a declaration.

The main result has no unproved Forrelation hypothesis. A historical declaration named `BansalSinhaLower` describes the needed fixed-$k$ proposition; `ForrelationLower.bansalSinhaLower` proves it. Earlier notes in the supplied packet describe the formerly conditional state. The current endpoint and its dependency closure take precedence over those notes. The accompanying correspondence and gap files distinguish exact statements, changed proof routes, short deductions and absent statement-level matches.
<!-- /passage:formal-changes -->

<!-- passage:specification -->
The frozen statements define bit inputs, partial Boolean functions, deterministic trees, finite randomized mixtures, finite-dimensional quantum programs and their query bounds. Bridge theorems relate the adaptive bit-oracle model used for the construction to the fixed-sequence phase-oracle model used by the imported quartic bound. The intended resource is the same worst-case number of bit queries throughout.

The [Lean Comparator][COMP] checks proposed proofs against fixed challenge declarations and an allowed axiom list. The supplied positive challenges import Mathlib and reproduce the same statement vocabulary; they do not import the candidate solution as their specification. Their definition blocks are byte-identical in the supplied files. This prevents a candidate proof from silently changing the challenge's function or complexity definitions.

The challenge vocabulary and the solution vocabulary nevertheless come from the same formal specification. They were not independently designed mathematical models. Kernel checking validates a term against its stated type, and Comparator validates the permitted type and dependencies. Neither process establishes that those definitions perfectly express the intended informal theorem. The model choices, the bit/phase bridges and the translation of the displayed asymptotic claim therefore remain substantive review obligations.
<!-- /passage:specification -->

### 7.2. Evidence and reproduction

<!-- passage:verification-evidence -->
The supplied trace records successful kernel builds and accepted Comparator runs for the Construction, Foundations, Separation, Tournament and Unconditional bundles. It also records five deliberately invalid submissions being rejected and a successful `--paranoid` replay of the Unconditional bundle. The configured axiom allowance is exactly `propext`, `Quot.sound` and `Classical.choice`. The candidate proof subtree contains no proof holes or additional mathematical axioms; challenge holes and negative-test fixtures are separate.

These were local, unsandboxed rehearsals. The commands in the trace used `--inadvisably-no-sandbox`; no official external verification service is claimed. The recorded paranoid replay is pinned to commit `d42fb67a7e060fb5386867dadf20a5903df39141`. The packet identifies the later source commit `c7e0c9161f0ad898889bd9166e7b354acd42188d`. The trace describes intervening documentation and corpus work, but the supplied material does not include a complete diff proving the two source states identical.

For this manuscript, AI reviewers inspected the supplied proof sources, reconstructed the main arguments, checked the packet hashes and compared the challenge vocabularies. No person has reviewed the work. Lean and Lake are unavailable in the present authoring environment, so this manuscript reports the recorded execution evidence and a fresh source audit, without claiming a fresh kernel or Comparator run. Full archived Comparator receipts and several repository helper scripts are also absent from the packet. These limits are recorded in `SOURCE_AUDIT.md`.
<!-- /passage:verification-evidence -->

<!-- passage:reproduction -->
To reproduce the mathematical checks, obtain the supplied source tree or an authorized checkout of the [formalisation repository][LEAN]. The repository was private at the recorded closeout; public availability is not assumed. Work in its `lean` directory, use `leanprover/lean4:v4.36.0-rc2`, and preserve the manifest's dependency pins. In particular, the complexity-library revision is `62ca5c21461b2482e8bd12b7cb9b4937d887a33a`, Mathlib is `69552756cd8a2d2d48763cf7279fd814d6a1224d`, and CSLib is `254e30e6d4299c51323aaeaf5f51a4763b375d4a`.

With those dependencies available, run:

```sh
lake build QuarticQuery
lake comparator --config QuarticCorpus/Unconditional/comparator.json --paranoid
lake env lean --run scripts/Reach.lean \
  QuarticQuery.theorem_1_1_unconditional \
  QuarticQuery.cubic_bound_fails_unconditional
```

The Comparator command above requests its default sandbox policy. The historical local run appended `--inadvisably-no-sandbox`; reproducing that run must be described accordingly. The other positive configurations are in the corresponding bundle directories. Their negative fixtures are expected to fail. The reachability script inspects the dependency closure and is supplementary to kernel checking. Repository-wide Python automation mentioned in the trace cannot be reproduced from this packet alone because its `tools` directory was not supplied.

A successful reproduction should retain the exact commit and dependency pins, command lines, exit statuses and complete outputs. Human review should then focus on the stated models, the challenge definitions and the passage-level correspondence, particularly the off-promise comparison, conditional sampling law and unconditioned joint event. Those are the points at which the informal argument can otherwise conceal a stronger assumption.
<!-- /passage:reproduction -->

## References

<!-- passage:references -->
**[OAI]** OpenAI. *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. Preprint, 5 October 2026, supplied at `openai/math` revision `4eaee875`. Theorem 1.1; Sections 2–5; Appendix A. [Source directory][OAI].

**[ABK]** Scott Aaronson, Shalev Ben-David and Robin Kothari. “Separations in Query Complexity Using Cheat Sheets.” *Proceedings of STOC 2016*, pp. 863–876. Sections 3 and 6 of the full version. [arXiv:1511.01937v2][ABK].

**[ABKRT]** Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal. “Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem.” *Proceedings of STOC 2021*, pp. 1330–1342. Theorem 2; Conjecture 2. [arXiv:2010.12629][ABKRT].

**[BS]** Nikhil Bansal and Makrand Sinha. “$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity.” *Proceedings of STOC 2021*, pp. 1303–1316. Theorem 1.3; Corollary 1.4; Sections 4–5 in the full version. [arXiv:2008.07003v3][BS].

**[GTW]** Uma Girish, Avishay Tal and Kewen Wu. “Fourier Growth of Parity Decision Trees.” *CCC 2021*, LIPIcs 200, 39:1–39:36. Section 1.3 and Lemma 9 in the conference version. [doi:10.4230/LIPIcs.CCC.2021.39][GTW].

**[Dru]** Andrew Drucker. “Improved Direct Product Theorems for Randomized Query Complexity.” *Computational Complexity* 21(2), 197–244, 2012. Section 1.3; Lemmas 3.1–3.2. [arXiv:1005.0644v2][DRU].

**[BHMT]** Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp. “Quantum Amplitude Amplification and Estimation.” *Contemporary Mathematics* 305, 53–74, 2002. Lemma 1 and equation (8). [arXiv:quant-ph/0005055][BHMT].

**[BBHT]** Michel Boyer, Gilles Brassard, Peter Høyer and Alain Tapp. “Tight Bounds on Quantum Searching.” *Fortschritte der Physik* 46(4–5), 493–505, 1998. Unknown-number-of-solutions search. [arXiv:quant-ph/9605034][BBHT].

**[Lean]** Will Cook, director; AI-produced development. *quartic-query-lean*. Supplied source revision `c7e0c9161f0ad898889bd9166e7b354acd42188d` and accompanying trace. [Repository][LEAN]. Access restrictions and execution evidence are described in Section 7 and `SOURCE_AUDIT.md`.

**[Comp]** Lean project. *Comparator*. Documentation of statement comparison and trusted-dependency checks, consulted 2 November 2026. [Official documentation][COMP].
<!-- /passage:references -->

[OAI]: https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026
[ABK]: https://arxiv.org/abs/1511.01937v2
[ABKRT]: https://arxiv.org/abs/2010.12629
[BS]: https://arxiv.org/html/2008.07003v3
[GTW]: https://doi.org/10.4230/LIPIcs.CCC.2021.39
[DRU]: https://arxiv.org/pdf/1005.0644v2
[BHMT]: https://arxiv.org/pdf/quant-ph/0005055
[BBHT]: https://arxiv.org/abs/quant-ph/9605034
[LEAN]: https://github.com/wcook04/quartic-query-lean
[COMP]: https://reservoir.lean-lang.org/@leanprover/Comparator
