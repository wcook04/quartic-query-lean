---
title: "Why the optimal randomized–quantum query exponent is four"
subtitle: "An expert companion to the reviewed quartic separation record"
author: "Independent AI-assisted mathematical and source review"
date: "2 November 2026"
lang: en-US
fontsize: 11pt
geometry: margin=1in
colorlinks: true
linkcolor: NavyBlue
urlcolor: NavyBlue
---

**Abstract.** We reconstruct OpenAI’s nearly quartic separation for total Boolean functions, with the exact order of quantifiers and the current local formalization kept explicit. A certificate is stored at an address whose bits are answers to disjoint instances of a quantum-easy partial function. A quantum algorithm can compare columns before checking their certificates: a genuine winner defeats every rival, even when that rival’s address inputs violate the promise. Fractional tournament weights then locate a short candidate list. Classically, planting a winner changes only one hidden zero and one addressed cell. The decisive estimate bounds the joint event of reaching that cell and remaining within an address-query cap; conditioning on the cap would be invalid. We give these arguments, identify the shorter local Forrelation proof, and derive the universal exponent four. The same specified circuit satisfies an eventual lower bound with coefficient $1/400$ and a quantum upper bound with logarithmic exponent six. Detailed Lean types, source-bound checking records, and the remaining model correspondences are supplied separately.

## 1. The theorem and the mechanism {#expert-models}

For a finite partial Boolean function $P:D\to\{0,1\}$, $R(P)$ and $Q(P)$ denote bounded-error randomized and quantum bit-query complexity, with error at most $1/3$ on every promised input. The query cap holds on every input and every branch, including off-promise inputs. One algorithm is chosen before the input. In the quantum model the oracle is
\[
O_x|i,b,z\rangle=|i,b\mathbin{\oplus}x_i,z\rangle;
\]
intermediate measurements and classical control are allowed. A constant function, or an empty promise, needs no queries. An off-promise input is undefined, rather than a promised zero-input.

For total Boolean functions define
\[
\alpha_{\rm tot}=\inf\left\{\alpha\ge0:\ \exists C_\alpha>0\ 
 \forall n\ge1\ \forall f:\{0,1\}^n\to\{0,1\},\quad
 R(f)\le C_\alpha(1+Q(f))^\alpha\right\}.
\tag{1}
\]
The constant in this definition is independent of both the input length and the function. The added one handles zero-query functions without exceptional conventions.

### The precise result {#expert-theorem}

**Theorem 1 (OpenAI’s separation, with the record’s quantitative bounds).** For every integer $k\ge2$, there is a positive constant $C_k$ such that, for every sufficiently large power of four $m=4^t$, the same explicitly defined total function $F_{k,m}$ satisfies
\[
 Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
 \qquad
 R(F_{k,m})\ge\frac1{400}
       \frac{m^{2-1/k}}{(\log_2m)^2}.
\tag{2}
\]
The ordinary estimates in the record permit the sufficient threshold $t\ge13669k^2$. Consequently $\alpha_{\rm tot}=4$, and no universal cubic bound for $R$ in terms of $Q$ holds.

OpenAI’s Theorem 1.1 states the separation with unspecified positive constants and fixed-$k$ thresholds [1, p. 1]. The coefficient, logarithmic exponent, and sufficient threshold in (2) come from the integrated record. The current named Lean family theorem has an eventual threshold; the improved numerical threshold $13669k^2$ is an ordinary specialization, not a separately named compiled wrapper. The upper half of the exponent statement uses Aaronson–Ben-David–Kothari–Rao–Tal’s theorem $D(f)=O(Q(f)^4)$ for total functions [2, Theorem 2, p. 2].

The construction separates finding a certificate from checking it. Each column contains an ordinary bit string and many independent physical certificate cells. A vector of hard partial-function answers specifies which cell matters. A valid certificate proves that its own column is all ones and points to a zero in every other column. These outward pointers make a real winner easy to compare with any rival, without requiring reliable behavior from losing columns. Classically, the separate address arrays force an algorithm either to spend many queries on the planted column or to guess its entire address.

**Proof destinations.** The exact models and quantifiers are in [record §§1–2](record/reasoning_record.md#ROOT-RESULT); [formal groups F01–F02](formal/formal_sources.html#F01) give the current definitions and endpoint types. The construction below supplies both bounds for one circuit, rather than separately chosen witnesses.

## 2. The partial function and the addressed total function {#expert-forrelation}

Fix $k\ge2$ and $t\ge1$, set $m=4^t$, and identify a bit $a$ with the sign $(-1)^a$. Put $\ell=\log_2m=2t$ and $r=20\ell=40t$. Let $H$ be the normalized Walsh matrix of order $m$, indexed by $\mathbb F_2^{2t}$, and let $u=m^{-1/2}{\bf1}$. For $k$ sign blocks $z^{(0)},\ldots,z^{(k-1)}\in\{-1,1\}^m$, write
\[
 \Phi(z)=u^{\mathsf T}D_{z^{(0)}}H D_{z^{(1)}}H\cdots
                     H D_{z^{(k-1)}}u,
 \qquad \delta=2^{-5k}.
\tag{3}
\]
Here $D_z$ is diagonal with entries $z$. Orthogonality gives $|\Phi|\le1$. We use the one-sided promise
\[
 P_{k,m}(z)=
 \begin{cases}
 1,&\Phi(z)\ge\delta,\\
 0,&|\Phi(z)|\le\delta/2,
 \end{cases}
\tag{4}
\]
and leave all other inputs undefined. In particular, a large negative value is unpromised. This numerical promise is Bansal–Sinha’s [4, equations (1.1)–(1.3), pp. 2–3]; Aaronson–Ambainis supplies the alternating Walsh construction with different promise thresholds [3].

Three properties are needed. First, for fixed $k$ and sufficiently large $m$,
\[
 L:=\left\lfloor\frac{m^{1-1/k}}{\ell^2}\right\rfloor<R(P_{k,m}).
\tag{5}
\]
Second, for $0<\eta<1/2$, a coherent procedure computes the promised answer with error at most $\eta$ using $O_k(1+\ln(1/\eta))$ queries, with that cap on all inputs. The elementary experiment applies the alternating unitary in (3) and projects onto $u$; its success probability is $\Phi^2$. Repetition distinguishes probabilities at least $\delta^2$ from probabilities at most $\delta^2/4$. For example, $q=\lceil16\delta^{-2}\ln(1/\eta)\rceil$ trials and threshold $q\delta^2/2$ suffice by exponential-moment bounds. Retaining all work and computing the threshold reversibly gives a coherent label. On an unpromised input this remains some label with the same cap. It does not decide promise membership.

Third, an exact fan-in-two Boolean circuit $C=C_{k,t}$ produces a domain bit and a value bit, with
\[
 S:=|C|\le200(k+1)^2m\ell^2.
\tag{6}
\]
The domain bit is one exactly on the promise; there the value bit equals $P_{k,m}$. Exactness follows by replacing $H$ with the integral matrix $W=\sqrt mH$. If $\Phi=N/M$, where $M=m(\sqrt m)^{k-1}$ and $N$ is the corresponding integer numerator, the two tests are $2^{5k}N\ge M$ and $2^{5k+1}|N|\le M$. Fast Walsh transforms use $O(km\log m)$ arithmetic operations on $O_k(\log m)$-bit numbers. The specified circuit implements modular arithmetic with a final range argument, yielding (6). This exact domain computation is essential because the quantum projection statistic cannot distinguish positive and negative large correlations. [Record: promise, decoder, and circuit](record/reasoning_record.md#forr_definition); [formal F03](formal/formal_sources.html#F03).

### Columns, cells, and a unique winner {#expert-function}

A raw input consists, for each $i\in[m]$, of an $m$-bit string $X_i$, $r$ blocks $A_{i,h}$ of $km$ bits, and a separate cell $B_{i,s}$ for every $s\in\{0,1\}^r$. A cell contains an $\ell$-bit pointer into each other column and $r$ proposed $S$-bit circuit transcripts. Fix a bijection between $\ell$-bit words and rows in $[m]$. These are all independent input coordinates; no validity condition is imposed on the input space.

A pair $(i,s)$ **wins** when $X_i=1^m$, each $A_{i,h}$ is promised with answer $s_h$, the transcripts in $B_{i,s}$ are the actual evaluations of $C$, and its pointer into each $j\ne i$ reaches a zero of $X_j$. Define $F_{k,m}=1$ exactly when a winning pair exists. Thus $F_{k,m}$ is total even when every address block is unpromised or every transcript is false.

There is at most one winning pair. If two distinct columns won, the pointer from the first into the second would exhibit a zero in an all-one string. Within one column, the actual answers $P(A_{i,h})$ determine the only possible address. This uniqueness uses the semantics of the promise, rather than any reliability claim about an off-promise quantum decoder. [Record: layout and uniqueness](record/reasoning_record.md#AC-layout); [formal F04](formal/formal_sources.html#F04).

### Exact local verification {#expert-tests}

At a fixed pair $(i,s)$, winning is equivalent to all
\[
 K=m+(m-1)+r(S+2)
\tag{7}
\]
local tests passing: $m$ tests of the own-column bits, $m-1$ pointer tests, every gate-consistency test in each transcript, and two output tests per transcript requiring domain $=1$ and value $=s_h$. Induction in a topological gate order proves that a gate-consistent transcript equals the actual circuit evaluation. The domain-output test then excludes unpromised blocks, and the value-output test fixes the address.

A gate test uses at most three input queries. A pointer test reads its $\ell$ bits and then its target bit, using $\ell+1$ adaptive queries. This is a depth bound: the target test can depend on all $m$ possible target coordinates, so it is not a bound on fixed coordinate support. The tests have exact coherent evaluators with retained work; compute-copy-uncompute additionally supplies clean predicate oracles at constant-factor query overhead. From (6), $K=O_k(m\ell^3)$. [Record: local equivalence and coherent access](record/reasoning_record.md#AC-local-equivalence); [formal F05](formal/formal_sources.html#F05).

## 3. Quantum search with unreliable rivals {#expert-comparison}

Set $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$. Decode each of a column’s $r$ partial-function blocks to error $\varepsilon/r$. A promised column’s whole address is correct with probability at least $1-\varepsilon$; on any column the procedure returns a label with the same query cap. The decoding cost is $O_k(r\ln(r/\varepsilon))$.

For each unordered pair of distinct columns, sort their indices and use one fixed coherent circuit. Decode both, read each outward pointer at its decoded address, and inspect the indicated bit of the other column. A column disqualifies the other when that bit is zero. If exactly one disqualifies the other, declare it victorious; otherwise declare the smaller index victorious. A self-comparison reports a loss without making queries. Retain the decoded labels and all work. Let $a_{ij}$ be the probability that $i$ defeats $j$, and put $a_{ii}=0$. Using the same sorted-pair circuit guarantees
\[
 a_{ij}+a_{ji}=1\quad(i\ne j).
\tag{8}
\]
If $i_*$ is a true winner, no rival can point to a zero in $X_{i_*}=1^m$. Whenever $i_*$’s own address is decoded correctly, its pointer finds a zero in the rival. Hence $a_{i_*j}\ge1-\varepsilon$ for every $j\ne i_*$, irrespective of the rival’s promise status. Orthogonal retained address labels justify this measured-probability argument in the coherent circuit. The comparisons between losing columns may be cyclic or exactly unbiased. [1, §3.3]; [record: winner dominance](record/reasoning_record.md#upper-winner-dominates); [formal F06](formal/formal_sources.html#F06).

### Amplification and fractional weights {#expert-tournament}

We need amplification that preserves the successful label distribution and has a fixed cap when the success probability $p$ is unknown. Fix $0<\gamma\le1/2$ and $0<\eta<1/2$. For $0<p<1$, write
\[
 A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle,
 \qquad p=\sin^2\theta.
\]
After $j$ Grover iterations the successful component is $\sin((2j+1)\theta)|g\rangle$. Every successful projection therefore gives the same normalized state, up to phase. For $M=\lceil10/\sqrt\gamma\rceil$, a trial chooses $j=0$ with probability $1/2$, and otherwise chooses $j$ uniformly from $0,\ldots,M-1$. The identity
\[
 \frac1M\sum_{j=0}^{M-1}\sin^2((2j+1)\theta)
 =\frac12-\frac{\sin(4M\theta)}{4M\sin(2\theta)}
\tag{9}
\]
gives success at least $9/40$ whenever $p\ge\gamma$: use $\sin(2\theta)\ge\sqrt\gamma$ for $\gamma\le p\le1/2$, and the zero-iteration half for $p\ge1/2$. A fixed number $\lceil\ln(1/\eta)/\ln(40/31)\rceil$ of fresh trials gives failure at most $\eta$ and an all-branch cap $O(\gamma^{-1/2}\ln(1/\eta))$. If $p=0$, failure is certain; if $p=1$, every trial succeeds. Stopping at the first success preserves the successful label law. This is the bounded version of the usual amplification rotation used in [1, Lemma 3.1] and its antecedents [8–9].

Consider an ideal classical process with weights $w_i=1$, total $W=\sum_iw_i$, and, when $W>0$, pivot law $w_p/W$. Append the pivot and update $w_i\leftarrow w_i a_{ip}$. Keep zero weights absorbed when $W=0$. Complementarity (8) gives the exact identity
\[
 \mathbb E[W_{\rm new}\mid w]
 =\frac1W\sum_{p,i}w_pw_i a_{ip}
 =\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\tag{10}
\]
Thus $\mathbb EW_T\le m2^{-T}$. Until $i_*$ is selected, its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$. Markov’s inequality bounds the ideal miss probability by $2m2^{-T}$.

The quantum implementation never computes these real weights. Given previous pivots $p_1,\ldots,p_t$, it prepares a uniform label $i$ and a fresh comparison workspace for each pivot:
\[
 \frac1{\sqrt m}\sum_i|i\rangle
       \bigotimes_{b=1}^t|\phi(i,p_b)\rangle.
\tag{11}
\]
Flag success when every comparison says that $i$ wins. Fresh tensor factors give success-and-label mass $m^{-1}\prod_ba_{ip_b}=w_i/m$. Orthogonal labels give total success $W/m$, and conditional label law $w_i/W$. Apply bounded amplification with $\gamma=1/(2m)$, $\eta=\varepsilon$; stop on failure.

Until the winner first enters the list, $W/m>1/(2m)$. At every such history the stage fails with probability at most $\varepsilon$, and conditional on success has exactly the ideal pivot law. Couple stage by stage with the ideal process. Over at most $T$ stages the additional miss probability is at most $T\varepsilon$. Failures after the winner is selected do not remove it. The final list has length at most $T$, and
\[
 \Pr[i_*\text{ absent}]\le2m2^{-T}+T\varepsilon.
\tag{12}
\]
If a comparison costs $c$ bit queries, stage $t$ costs $O(c(t+1)\sqrt m\ln(1/\varepsilon))$, giving $O(c\sqrt mT^2\ln T)$ in total. This cap holds even when no dominant candidate exists. [1, Proposition 3.2, pp. 8–9]; [record: stage state and coupling](record/reasoning_record.md#upper-stage-state); [formal F07](formal/formal_sources.html#F07).

### Checking the list {#expert-quantum}

For each candidate, decode a fresh address and search for a failed local test. At that address, uniform sampling of the $K$ exact tests has failure-finding probability zero if all pass and at least $1/K$ otherwise. Bounded amplification with threshold $1/K$ finds a failure except with probability $\varepsilon$. Every address of a nonwinner has a failed test, so its false acceptance probability is at most $\varepsilon$. A winner is accepted whenever its new decoding is correct.

Accept the full input exactly when at least one listed candidate passes. The overall error is at most $T\varepsilon$ on a zero-input, and at most $2m2^{-T}+T\varepsilon+\varepsilon<1/3$ on a one-input. Comparisons cost $c=O_k(\ell^2)$; verification costs $O_k(r\ln(r/\varepsilon))+O(\sqrt K\,\ell\ln(1/\varepsilon))$ per candidate, including fresh decoding. Together with $T=O(\ell)$ and (7), these fit the deliberately loose bound $C_k\sqrt m\ell^6$. All array indices are computed reversibly; pointers are read bit by bit. A controlled bit query uses load, controlled use, and unload, costing two ordinary queries. No unit-cost pointer oracle is assumed. [Record: error and explicit budget](record/reasoning_record.md#upper-total-error); [formal F08](formal/formal_sources.html#F08).

## 4. The randomized lower bound {#expert-direct-product}

The lower bound applies to any partial function $P$ with an exact realizing circuit and integers $1\le L\le m$ satisfying $L<R(P)$. Finite minimax supplies a probability law $\mu$, supported on the promise, under which every depth-$L$ deterministic tree succeeds with probability at most $\beta=2/3$. The finite set of depth-bounded behaviors ensures attainment; otherwise a mixture succeeding on every promised input would contradict $L<R(P)$.

**Lemma 2 (capped direct product).** On independent inputs $U_1,\ldots,U_r\sim\mu$, any algorithm making at most $L$ queries to each input on every branch has probability at most $\beta^r$ of returning all $r$ answers. Queries may be interleaved adaptively. Random coins and free side information are allowed when jointly independent of the whole input tuple.

**Proof.** For a nonnegative, possibly unnormalized one-input measure $\nu$ supported on the promise, let $V_q(\nu)$ be the greatest weighted success of a depth-$q$ tree. Then
\[
 V_0(\nu)=\max_b\nu(P=b),\qquad
 V_{q+1}(\nu)=\max\left\{V_q(\nu),
 \max_a\big[V_q(\nu_{a,0})+V_q(\nu_{a,1})\big]\right\},
\tag{13}
\]
where $\nu_{a,b}$ restricts to inputs with bit $a$ equal to $b$. For product measures and individual remaining budgets $q_h$, induction on a vector-output tree bounds its all-answer weighted success by $\prod_hV_{q_h}(\nu_h)$. At a leaf the success mass factors. A query to input $h$ changes only that measure and decreases only that budget; its two branches are absorbed by (13), with every other nonnegative factor unchanged. Zero-mass branches cause no division. Initially each factor is at most $\beta$. Fix independent side information and coins, apply the deterministic bound, and average. $\square$

This is the separately capped product mechanism reviewed by Drucker, following Shaltiel [7, §1.3 and Lemmas 3.1–3.2], rather than a direct invocation of a theorem with only a global budget. The record also gives a conditional-transcript proof: a compatible deterministic history is a Cartesian product of constraints on the independent inputs, and the product of optimal continuation values is a supermartingale. The relevant terminal bound is on conditional success probability. [Record: weighted product proof](record/reasoning_record.md#CL-weighted-product); [formal F09](formal/formal_sources.html#F09).

### Planting and the erased zero {#expert-erased-zero}

Generate a dummy input $Y^{(0)}$ by choosing independent uniform rows $J_i\in[m]$, putting a single zero at $X_i[J_i]$, drawing all $A_{i,h}$ independently from $\mu$, and setting all certificate cells to zero. It is a zero-input. Choose $I\in[m]$ uniformly, independently of the entire dummy data. Obtain $Y^{(1)}$ by erasing the zero in column $I$ and filling only its true-address cell with actual transcripts and pointers to $J_j$ for every $j\ne I$. This is a one-input.

Fix a deterministic tree of cap $G=\lfloor mL/100\rfloor$. Its two runs agree until the dummy run queries either the erased zero or some bit of the filled cell. Consequently its absolute acceptance gap is at most the sum of these two encounter probabilities. Counting every visit to the changed cell is harmless even if that particular bit equals its old value.

Let $Z$ count columns whose zero is found in the dummy run. Independence of $I$ gives the exact selection identity
\[
 \Pr[\text{query }X_I[J_I]]=\frac{\mathbb EZ}{m}.
\tag{14}
\]
Before a zero is found, it remains uniform among the unqueried rows of that column, conditional on the full adaptive history. Discoveries preceded by fewer than $m/2$ distinct queries to their column have conditional probability at most $2/m$ per query, so their expected number is at most $2G/m$. Every remaining discovered column receives at least $m/2$ queries; there are at most $2G/m$ of them. Hence (14) is at most $4G/m^2$. Merely marginal uniformity of $I$ would not justify (14); independence from the dummy run is used exactly here. The formal development also has a stronger coefficient-two bound proved by a different finite-world induction. [Record: identity and early/late proof](record/reasoning_record.md#CL-erased-zero-identity); [formal F10](formal/formal_sources.html#F10).

### The joint event that controls address guessing {#expert-joint-event}

Call column $i$ heavy when the entire dummy run makes more than $L$ queries in total to its $r$ address blocks, counting repetitions. There are at most $G/L$ heavy columns, so $\Pr[I\text{ heavy}]\le G/(mL)$.

Fix a column $i$ and a query time $q\in\{0,\ldots,G-1\}$. Construct a simulator with oracle access to $U_h=A_{i,h}$. Give it all zero locations, all other columns’ address blocks, and the blank cells as independent free data. This excludes the target’s true address and its computed transcripts. Simulate the dummy tree, answering outside queries for free, and abort **before** its $(L+1)$-st target query. If the simulator reaches the proposed query at time $q$, and that location lies in cell $B_{i,s}$, output $s$ before reading the cell. Otherwise output a fixed vector.

This simulator has total target cap $L$, hence cap $L$ on each input, on every branch. If the original full dummy run is nonheavy in column $i$ and its time-$q$ query reaches the true cell, the simulator has not aborted and returns the true address. Under the original product law, therefore,
\[
 \begin{split}
 &\Pr[\,i\text{ nonheavy and time }q
            \text{ queries the true cell of }i\,]\\
 &\hspace{3em}\le\Pr[\text{capped simulator returns all }r\text{ answers}]
 \le(2/3)^r.
 \end{split}
\tag{15}
\]
This is an event inclusion, with no conditioning on nonheaviness. Union over the $G$ times and average over the independent uniform $I$; there is no extra factor $m$. Adding the heavy contribution gives
\[
 \Pr[\text{query the true cell of }I]
 \le\frac G{mL}+G(2/3)^r.
\tag{16}
\]

**Why conditioning fails.** Let $P=\mathrm{AND}$ on $D=\{01,10,11\}$, with the uniform law and $L=1$. Every one-query tree succeeds on at most two of these three inputs. A tree that reads the first bit, stops with output zero if it sees zero, and otherwise queries and outputs the second bit is always correct. Its one-query event is exactly $\{01\}$, so its success conditional on that event is one. Its joint success-and-cap probability is $1/3$. Truncating before the second query and outputting zero yields a genuinely capped tree with unconditional success $2/3$. Selection by a cap can therefore destroy the original hardness law.

The precise compiled per-time statement is now `QuarticQuery.Paper.eq_21`; its probability is the original-law conjunction in (15). It is included in the current root build, without an exact-name Comparator receipt, and is outside the two recorded headline dependency traversals. The headline lower bound uses the underlying simulator and union-bound route. [Record: simulator and joint event](record/reasoning_record.md#CL-simulator); [formal F11](formal/formal_sources.html#F11).

### The contradiction and its constants {#expert-lower-bound}

Equations (14)–(16) imply
\[
 |\Pr[A(Y^{(1)})=1]-\Pr[A(Y^{(0)})=1]|
 \le\frac{4G}{m^2}+\frac G{mL}+G(2/3)^r
 \le\frac6{100}<\frac13.
\tag{17}
\]
Indeed $G\le mL/100\le m^2/100$, and $r=40t$ gives $(2/3)^r\le m^{-10}$. This numerical estimate already holds whenever $1\le L\le m$; no further asymptotic argument is needed here. Fixing the coins of a randomized algorithm and averaging preserves (17). Correctness with error $1/3$ on every input would instead give an acceptance gap at least $1/3$, because the coupled distributions are supported on zero- and one-inputs. Thus $R(F_{k,m})>\lfloor mL/100\rfloor$.

For (5), $k\ge2$ and $t\ge8$ imply $4t^2\le2^t$, so $x=m^{1-1/k}/(2t)^2\ge1$ and $L=\lfloor x\rfloor\ge x/2$. Also $mL\ge200$, so $\lfloor mL/100\rfloor\ge mL/200\ge mx/400$. This proves the second inequality in (2), once the separate hardness threshold ensures $L<R(P_{k,m})$. [Record: discrepancy and floors](record/reasoning_record.md#CL-discrepancy); [formal F12](formal/formal_sources.html#F12).

## 5. The shorter Forrelation route and its scope {#expert-forrelation-proof}

The construction needs only (5). Bansal–Sinha states the stronger randomized lower bound $\Omega(\eta^2k^{-29}(m/\log(km))^{1-1/k})$ at error $(1-\eta)/2$ [4, Theorem 1.3 and Corollary 1.4, p. 4]. For fixed $k$, its constant-error consequence dominates $m^{1-1/k}/\log^2m$. The local formalization instead proves the needed ingredient through a shorter argument: a Gaussian interpolation in just the first block, followed by a biased derivative bound for ordinary decision trees. The Gaussian-chain and transformed integration-by-parts antecedents are Bansal–Sinha’s; the tree martingale method follows Girish–Tal–Kewen Wu [5, §1.3 and Lemma 1.9, p. 8]. The algebraic truncation and their assembly below are part of the local proof.

Define
\[
 \varphi(x)=\frac{x(3+x^2)}{2(2+x^2)^{3/2}},\qquad
 \Psi(x)=\frac1{2\sqrt{2+x^2}}.
\]
Then $|\varphi|\le1/2$, $\varphi'=3/(2+x^2)^{5/2}$, $\varphi=x\Psi-\Psi'$, and $0<\Psi(x)\varphi'(y)\le3/16$ for all real $x,y$. Independent standard Gaussian blocks $U_0,\ldots,U_{k-2}$, with $V_j=HU_j$, give a vector of sign biases
\[
 w_s=\big(s\varphi(U_0),\ \varphi(V_0)\varphi(U_1),\ldots,
       \varphi(V_{k-3})\varphi(U_{k-2}),\ \varphi(V_{k-2})\big),
\tag{18}
\]
with the middle list empty when $k=2$. Round independently conditional on these biases, obtaining a law $\nu_s$. Although later biases at $s=0$ are generally nonzero, sequential Gaussian reflections and multilinearity show that the resulting sign law $\nu_0$ is uniform.

For the multilinear extension $F_g$ of a decision-tree output $g\in[-1,1]$, $\mathbb E_{\nu_s}g=\mathbb EF_g(w_s)$ is polynomial in $s$. Its derivative starts in the first block. Gaussian integration by parts in the form $\mathbb E[\varphi(Z)G(Z)]=\mathbb E[\Psi(Z)G'(Z)]$ transfers it through successive blocks. Repeated differentiation in one Boolean coordinate vanishes by multilinearity. Each surviving chain acquires a Walsh entry and a factor $\Psi\varphi'$. Bounding these factors gives, for depth $d\ge1$,
\[
 |\mathbb E_{\nu_1}g-\mathbb E_{\nu_0}g|
 \le\left(\frac3{16\sqrt m}\right)^{k-1}
 \left[(16kd\ln(4km))^{k/2}+2^{-k}\right].
\tag{19}
\]
The derivative estimate behind (19) bounds the sum of absolute mixed derivatives at any bias vector with coordinates at most $1/2$ in magnitude. Revealing a fresh queried bit yields a centered factor $\xi_i=(z_i-\mu_i)/(1-\mu_i^2)$ of magnitude at most two; the degree-$j$ martingale increment is this factor times a contracted degree-$(j-1)$ polynomial. Stopping before a contracted lower-degree polynomial becomes large permits a martingale tail bound and induction on the derivative order. It avoids conditioning on a favorable future event. The full chain identity and stopped-martingale induction are [record §§3.9–3.11](record/reasoning_record.md#forr_path_formula).

The distribution $\nu_1$ need not be supported entirely on promised yes-inputs. The proof handles this explicitly. Put $a=18^{-(k-1)}\ge32\delta$. Direct Gaussian calculations give
\[
 \mathbb E_{\nu_1}\Phi\ge a,\qquad
 \mathbb E_{\nu_0}\Phi=0,\qquad
 \mathbb E_{\nu_0}\Phi^2=1/m.
\tag{20}
\]
Amplify a purported depth-$D$, error-$1/3$ solver with $50k$ trials to error $\epsilon\le(8/9)^{25k}\le a/18$, and let $A(z)$ be its acceptance probability. The one-sided promise gives, on every raw input,
\[
 (1-\epsilon)(\Phi-\delta)\le A
       \le\epsilon+4\Phi^2/\delta^2.
\tag{21}
\]
Thus its acceptance gap is at least $(1-\epsilon)(a-\delta)-\epsilon-4/(m\delta^2)$. When $m=4^t$ and $15k+2\le2t$, this is at least $119a/144$. A depth-zero solver has constant acceptance and hence zero gap, so we may assume $D\ge1$. But if $D\le(2/18225)m^{1-1/k}/(k^2\ln(4km))$, applying (19) to each amplified tree, with the harmless depth bound $50kD+1$, makes the gap at most $7a/12$. Contradiction proves the restricted uniform estimate
\[
 R(P_{k,m})>\frac2{18225}
       \frac{m^{1-1/k}}{k^2\ln(4km)}
 \quad(m=4^t,\ 15k+2\le2t).
\tag{22}
\]
For $t\ge13669k^2$, $\ln(4km)\le6t$ and $4t>54675k^2$; hence (22) exceeds $m^{1-1/k}/(4t^2)$, proving (5). The sharp uniform statement (22) is compiled in the supplied root build; its exact name has no Comparator acceptance. [Record: moments through threshold](record/reasoning_record.md#forr_moments); [formal F03](formal/formal_sources.html#F03).

Two literature boundaries matter. First, the supplied audit identifies two faulty displays in Bansal–Sinha v3, §5.4, p. 38: writing $\Lambda=\log(kN)$ and $j$ for its Fourier level, a logarithmic comparison drops a factor $\Lambda^{(j/k-1)/2}$, reaching $\Lambda^{(k-2)/2}$ at $j=k(k-1)$; equation (5.31) uses $\delta^2/(4N)$ where Theorem 3.1 gives $4/(N\delta^2)$. These are local proof-display issues, not counterexamples to its theorem. A weaker corrected comparison still suffices for (5), and the local route above avoids both displays. Second, Sherstov–Storozhenko–Pei Wu’s sharper Fourier-growth theorem [6, Corollaries 4.14–4.15, pp. 35–36] supplies a separate, shorter external comparison after a random-restriction conversion to biased derivatives. For $0<\eta<1$ and $m=4^t\ge2^{15k+2}$, that route gives $R_{(1-\eta)/2}(P_{k,m})\ge c\eta^2[m/(1+\ln(km))]^{1-1/k}$ for an unspecified absolute $c>0$. It is an ordinary argument using an external theorem, rather than the current Lean proof of (22). [Record: the display corrections](record/reasoning_record.md#forr_bs_mismatch) and [SSW comparison](record/reasoning_record.md#forr_ssw_comparison).

## 6. Assembling the family and extracting the exponent {#expert-family}

Choose the exact circuit `Forrelation.forrCircuit (k - 1) t`. The upper bound uses its size and coherent decoder. The lower bound applies to every exact realizing circuit, so it applies to this same choice. This closes the common-witness requirement in (2). [Record: family assembly](record/reasoning_record.md#ROOT-FAMILY-ASSEMBLY); [formal F13](formal/formal_sources.html#F13).

### Every smaller universal exponent fails {#expert-exponent}

Fix $0\le\alpha<4$. Choose an integer $k\ge2$ satisfying $k>2/(4-\alpha)$, and keep it fixed while $m\to\infty$ through powers of four. Then $e=2-1/k-\alpha/2>0$. For all sufficiently large $m$, (2) implies
\[
 \frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
 \ge\frac1{400(1+C_k)^\alpha}
       \frac{m^e}{(\log_2m)^{2+6\alpha}}
 \longrightarrow\infty.
\tag{23}
\]
A positive power exceeds every fixed power of a logarithm. Thus no constant $C_\alpha$ in (1) exists. For $\alpha=3$, $k=3$ already suffices. At the boundary $\alpha=4-2/k$, the power in (23) is zero and this argument supplies no divergence; a fixed $k$ does not furnish an exact quartic separation.

Conversely, the total-function upper bound [2] gives $R\le D\le C(1+Q)^4$. Its proof combines $D\le\operatorname{bs}(f)\deg(f)$, $\operatorname{bs}(f)=O(Q(f)^2)$, and $\deg(f)\le\lambda(f)^2=O(Q(f)^2)$, where $\lambda$ is the sensitivity-graph operator norm. The spectral degree inequality is the consequence of Huang’s signed-cube argument used in [2]. Full proofs and distinct formal coefficient routes are in [record Appendix A](record/reasoning_record.md#R3-A-RESULT). Four therefore belongs to the set defining (1), while no smaller nonnegative exponent does: $\alpha_{\rm tot}=4$. [Formal F14](formal/formal_sources.html#F14).

### An explicit diagonal consequence {#expert-diagonal}

The explicit ordinary budget in the record also permits a diagonal nearly quartic family. This is an additional deduction from those formulas, without a current named Lean wrapper. The existing bound `Upper.budgetConst_le_exponential` gives $C_k\le2^{53}k2^{10k}$; its exact statement and source are included in formal group F13. Set $k(t)=\lfloor\sqrt{t/13669}\rfloor$ for $t\ge54676$. Then $k\ge2$, $t\ge13669k^2$, and $k\to\infty$ while $k=O(\sqrt t)$. For the same family,
\[
 \begin{aligned}
 \log_2 R&\ge N_t:=4t-2t/k-\log_2 400-2\log_2(2t),\\
 \log_2(1+Q)&\le D_t:=t+10k+\log_2k+6\log_2(2t)+54.
 \end{aligned}
\tag{24}
\]
For $t\ge8$, $\log_2(2t)\le t/2$, so $N_t\ge2t-\log_2 400>0$ on the stated range; also $N_t<4t<4D_t$. Finally $N_t/t\to4$ and $D_t/t\to1$, because $k\to\infty$ and $k=O(\sqrt t)$. Hence $R\ge(1+Q)^{N_t/D_t}$, an explicit $4-o(1)$ lower exponent along this diagonal. It neither gives a constant-times fourth-power lower bound nor changes the proof of the canonical fixed-$k$ theorem.

## 7. What is formally checked {#expert-verification}

The supplied source contains the unconditional declarations

```lean
theorem alphaTot_eq_four_unconditional : alphaTot = 4
```

and `theorem_1_1_unconditional`, whose full type conjoins the exponent conclusion, the common-circuit separation family, and the universal quartic upper bound. Their meanings depend on the inspected definitions of the finite randomized and adaptive quantum models. Complete source signatures, enclosing contexts, definitions, receipt membership, and record anchors for the load-bearing claims appear in `correspondence.json` and the navigable [formal companion](formal/formal_sources.html#F15).

The retained current root build is dated 2 November 2026, 20:55 UTC, and records Lean 4.36.0-rc2. Fresh byte checks in this review verified all 152 selected Lean/configuration files against their current bindings and checked the current receipt files. The supplied record also contains passed, source-current Comparator runs for selected exact declarations. These are retained execution records; this review did not rerun Lean or Comparator, because neither executable is available in the review environment. Exact-name comparison membership is listed separately from build membership. A shared specification can contain a shared semantic error, so Comparator agreement does not establish the fidelity of a prose interpretation.

Several old limitations have been superseded: the current source has a standalone bounded-list tournament statement, literal tensor-stage wrappers, a conditional finite-transcript direct-product theorem, the per-time original-law conjunction `Paper.eq_21`, and absolute-gap discrepancy wrappers. Their existence, exact comparison status, and reach from the recorded headline roots differ; none should be inferred merely from another theorem’s name.

Two boundaries remain substantive. The physical query implementation proves the measured label law used by the algorithm; a bridge identifying its designated retained original quantum subsystem with the abstract successful state has not been supplied. This stronger state assertion is unnecessary for the formal query-complexity endpoint. Similarly, the finite direct-product development does not itself provide a general pushforward theorem from arbitrary independent external probability spaces into finite tree behaviors. The ordinary conditioning-and-averaging argument is separate from that formal interface. `LEAN_GAPS.md` states the precise obligations.

The separation theorem and original construction are credited to OpenAI. The local Lean development and alternative Forrelation argument are those supplied in the directed reconstruction. This companion reorganizes, checks, and explains that material; its quantitative diagonal remark is identified as an additional ordinary deduction. The source audit, finite diagnostics, and independent agent readings are not human peer review. The unavailable separately attached pasted-text file was not assessed. The complete reading and verification scope, including primary editions and failed public-source retrieval, is recorded in `source_read_receipt.json` and `review_notes.md`.

## References

1. **OpenAI.** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. Preprint, 5 October 2026, 19 pp. Supplied original PDF, SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`. Theorem 1.1, p. 1; construction §2; quantum tournament §3; randomized lower bound §4; universal bound Appendix A. [Supplied primary text](record/original_preprint.pdf).

2. **Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao, and Avishay Tal.** *Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem*. Assessed edition: [arXiv:2010.12629v1](https://arxiv.org/abs/2010.12629v1), 23 October 2020. Theorem 2, p. 2; cubic conjecture, Conjecture 2, p. 20. Published in STOC 2021, pp. 1330–1342.

3. **Scott Aaronson and Andris Ambainis.** *Forrelation: A Problem that Optimally Separates Quantum from Classical Computing*. Assessed edition: [arXiv:1411.5729v1](https://arxiv.org/abs/1411.5729v1), 21 November 2014. Alternating projection and separate interference procedure, pp. 13–14, Proposition 6. Published in *SIAM Journal on Computing* 47(3), 982–1038, 2018.

4. **Nikhil Bansal and Makrand Sinha.** *k-Forrelation Optimally Separates Quantum and Classical Query Complexity*. Assessed edition: [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3), 17 November 2020. Promise and Theorem 1.3/Corollary 1.4, pp. 2–4; Theorem 3.1, p. 16; Theorem 3.2 and Corollary 3.5, pp. 17–18; Lemma 4.3, p. 19; §5.4 and equation (5.31), p. 38. Published in STOC 2021, pp. 1303–1316.

5. **Uma Girish, Avishay Tal, and Kewen Wu.** *Fourier Growth of Parity Decision Trees*. Assessed edition: [arXiv:2103.11604v2](https://arxiv.org/abs/2103.11604v2), 13 May 2021. The ordinary-tree method is §1.3 and Lemma 1.9, p. 8. Published in CCC 2021, LIPIcs 200, 39:1–39:36.

6. **Alexander A. Sherstov, Andrey A. Storozhenko, and Pei Wu.** *An Optimal Separation of Randomized and Quantum Query Complexity*. Assessed edition: [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4), 29 January 2023. Corollaries 4.14–4.15 and real-valued leaf extension, pp. 35–36. Published in *SIAM Journal on Computing* 52(2), 525–567, 2023. The arXiv HTML rendition uses different corollary numbering.

7. **Andrew Drucker.** *Improved Direct Product Theorems for Randomized Query Complexity*. *Computational Complexity* 21(2), 197–244, 2012. Assessed edition: [arXiv:1005.0644v2](https://arxiv.org/abs/1005.0644v2), 9 May 2014. The capped strategy is §1.3, pp. 6–7; Lemmas 3.1–3.2, pp. 11–12; fair specialization, p. 13. These are antecedents to Lemma 2; its complete finite proof is given above.

8. **Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp.** *Quantum Amplitude Amplification and Estimation*. *Contemporary Mathematics* 305, 53–74, 2002. Assessed edition: [arXiv:quant-ph/0005055v1](https://arxiv.org/abs/quant-ph/0005055v1), 15 May 2000. Lemma 1, pp. 5–6; equation (8), p. 7; Theorem 3, p. 8, with proof through p. 10. The invariant two-dimensional rotation supplies the amplification geometry.

9. **Michel Boyer, Gilles Brassard, Peter Høyer, and Alain Tapp.** *Tight Bounds on Quantum Searching*. *Fortschritte der Physik* 46(4–5), 493–506, 1998. Assessed edition: [arXiv:quant-ph/9605034v1](https://arxiv.org/abs/quant-ph/9605034v1), 23 May 1996. Section 4, Lemma 2, p. 3; Theorem 3 and timeout discussion, p. 4. Randomized iteration counts are an antecedent to the bounded unknown-success procedure.
