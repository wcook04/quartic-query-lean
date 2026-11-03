---
title: "The optimal randomized–quantum query exponent is four"
subtitle: "A companion to OpenAI's nearly quartic separation"
author: "Will Cook"
date: "November 2026"
bibliography: expert_companion.bib
link-citations: true
abstract: |
  OpenAI's preprint constructs total Boolean functions $F$ with $R(F)\ge Q(F)^{4-o(1)}$. Since $R=O(Q^4)$ for every total function, the optimal exponent relating bounded-error randomized and quantum query complexity is exactly four, and the conjectured cubic bound of Aaronson, Ben-David, Kothari, Rao and Tal fails. The previous best separation was $R=Q^{3-o(1)}$, obtained from the cheat-sheet framework once Bansal and Sinha, and independently Sherstov, Storozhenko and Wu, proved an optimal partial separation. The new idea is to give each of $m$ columns its own array of certificate cells, addressed by the answers to hard Forrelation instances, so that a classical algorithm pays about $m^{1-1/k}$ queries per column across about $m$ columns, while a quantum algorithm finds the winning column in about $\sqrt m$ queries by comparisons in which a genuine winner beats every rival; this gives $R\approx Q^{4-2/k}$. This companion presents the full argument at the level an expert will want to check, lists the natural shortcuts that fail together with a counterexample for each, and explains how to check a Lean formalisation whose four headline theorems Comparator accepts against a 343-line statement file that imports only Mathlib.
---

## 1. The result

A query reads one input bit; computation between queries is free. For a partial function $f$, $R(f)$ and $Q(f)$ are the least worst-case numbers of queries made by a randomized, respectively quantum, algorithm that answers correctly with probability at least $2/3$ on every input in the domain of $f$. The query cap holds on every input, every random choice and every measurement branch, including inputs outside the domain. Quantum queries use $O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle$. For total functions put
$$
\alpha_{\rm tot}=\inf\Bigl\{\alpha\ge0:\ \exists C_\alpha>0\ \forall n\ge1\ \forall f:\{0,1\}^n\to\{0,1\},\ \ R(f)\le C_\alpha\bigl(1+Q(f)\bigr)^\alpha\Bigr\}.
\tag{1}
$$
One constant serves every input length and every function; the added one covers constant functions. Throughout, $\ell=\log_2 m$, and $m=4^t$ is a power of four.

**Theorem 1** [@OpenAI2026, Theorem 1.1]**.** $\alpha_{\rm tot}=4$. More precisely, for each integer $k\ge2$ there is a constant $C_k$ such that for every $t\ge13669\,k^2$ and $m=4^t$, one explicitly specified total function $F_{k,m}$ satisfies both
$$
Q(F_{k,m})\le C_k\sqrt m\,\ell^{6}
\qquad\text{and}\qquad
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{\ell^{2}}.
\tag*{(2)\quad\textsf{P2}}
$$

Displays that match a display of the preprint carry its number after the letter P. The preprint states (2) with unspecified constants $c_k,C_k,b_k$ and an unspecified threshold. The exponent six, the constant $1/400$ and the threshold come from explicit counting in the companion reasoning record [@Record2026, §§5.4, 6.6]. The upper bound $R(f)\le D(f)=O(Q(f)^4)$ for total $f$ is due to Aaronson, Ben-David, Kothari, Rao and Tal [@ABKRT2021, Theorem 2], through Huang's sensitivity theorem [@Huang2019]. Already $k=3$ gives $4-2/k=10/3>3$, which refutes their Conjecture 2, $R(f)=O(Q(f)^3)$.

The theorem, the construction and both of its analyses are OpenAI's [@OpenAI2026]. Addressing a certificate by the answers to partial-function instances comes from Aaronson, Ben-David and Kothari's cheat sheets [@ABK2016]. This companion explains the argument for a specialist reader, adds explicit constants and two short alternative arguments, and describes a Lean formalisation of the result (Appendix A). In that formalisation the [compared form of Theorem 1][thm-headline] has an existential logarithmic exponent and the lower bound $\lfloor mL/100\rfloor<R(F_{k,m})$ of (15) below, for the same circuit; the explicit constants $6$ and $1/400$ are proved by a [separate theorem][src-constants] that is built but has not been compared.

### 1.1 Where this sits

| Exponent $a$ with $R=Q^{a}$ (total $f$) | Source |
|---|---|
| $2$ | OR: Grover search and its matching lower bound |
| $5/2$, up to logarithms | cheat sheets with Forrelation [@ABK2016] |
| $8/3-o(1)$ | Tal [@Tal2020] |
| $3-o(1)$ | Bansal and Sinha [@BansalSinha2021]; independently Sherstov, Storozhenko and Wu [@SSW2023] |
| $4-o(1)$ | OpenAI [@OpenAI2026] |
| upper bound $4$ | $D=O(Q^4)$ [@ABKRT2021], via [@Huang2019] |

The cheat-sheet arithmetic shows why the earlier route stopped at the cube. In [@ABK2016, §3.1] a partial function $g$ on $n$ bits is composed with $h=\mathrm{AND}_{m'}\circ\mathrm{OR}_{m'}$, which has $R(h)=\Omega(m'^2)$, $Q(h)=O(m')$ and certificates of size $m'$. A quantum algorithm computes $g\circ h$ and then checks a certificate of size $\widetilde O(nm')$ by Grover search, in $\widetilde O(m'+\sqrt{nm'})$ queries, while a classical algorithm needs $\widetilde\Omega(R(g)\,m'^2)$. With Forrelation, $R(g)=\widetilde\Omega(\sqrt n)$, and $m'=n$ gives $5/2$. With an optimal partial separation, $R(g)=\widetilde\Omega(n)$ and $Q(g)$ polylogarithmic, the same choice gives $n^3$ against $n$; ABK record that the framework yields a cubic separation "in a completely black-box manner" once such a $g$ exists. Improved partial separations then gave $8/3-o(1)$ and $3-o(1)$, and ABKRT conjectured that three is the truth.

Three further lines of work feed the construction. The $k$-fold Forrelation problem is Aaronson and Ambainis's [@AA2018]; the cheat-sheet paper records their conjecture that it achieves the optimal partial separation, which Bansal and Sinha and Sherstov, Storozhenko and Wu proved, and the one-sided thresholds used here are Bansal and Sinha's. The winning condition, a unique all-one column whose certificate exhibits a zero in every other column, descends from the pointer functions of Göös, Pitassi and Watson [@GPW2018], developed by Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs [@ABBLSS2017]; GPW reach the zeros through a chain of pointers, and the direct outward pointers used here are discussed by Ambainis et al. Finding a candidate by comparisons and then checking its certificate relates to quantum minimum finding [@DH1996] and king finding in tournaments [@MPS2023], and the preprint singles out the comparison-based separations of certificate complexity by Ben-David and Kothari [@BDK2026] and by Ambainis, Iraids and Kokainis [@AIK2026]. Quantum search with bounded-error inputs [@HMW2003] does not apply directly: it needs every comparison to compute a fixed predicate with bounded error, and here a comparison between two losing columns can have any probability, including exactly $1/2$.

### 1.2 The idea

The input has $m$ columns. Column $i$ holds a string $X_i\in\{0,1\}^m$, $r=20\ell$ inputs $A_{i,1},\dots,A_{i,r}$ to a Forrelation partial function $P=P_{k,m}$, and a separate cell $B_{i,s}$ for every address $s\in\{0,1\}^r$ (Figure 1). The answers $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ select one cell, which should certify $s_i$ and point to a zero in every other column. The function asks whether some all-one column has such a cell.

![Column $i^\star$ is the winner: $X_{i^\star}$ is all ones, and the cell selected by the answers to its $r$ Forrelation instances points to a zero in every other column. No pointer from any other column can find a zero in $X_{i^\star}$, whatever address that column computes.](figures/expert_column.svg){width=100%}

*Classically*, the hard distribution plants one winner in a uniformly random column of an input that has one zero in each column (§5). To see the planted cell an algorithm must either compute that column's address, which costs about $L\approx R(P)\approx m^{1-1/k}$ queries in that column, or guess an $r$-bit address that it cannot learn more cheaply. Since the column is unknown, it must invest about $L$ queries in a constant fraction of the $m$ columns, so
$$
R\approx m\cdot L\approx m^{2-1/k}.
$$
*Quantumly*, each address costs only polylogarithmically many queries, and the search over $m$ columns costs about $\sqrt m$, so $Q\approx\sqrt m$ up to logarithms, and
$$
R\approx m^{2-1/k}=\bigl(\sqrt m\bigr)^{4-2/k}\approx Q^{4-2/k}.
$$

The difficulty is the quantum search. Grover search for "column $i$ wins" would check about $K\approx m$ local tests in each column, at cost $\sqrt K\approx\sqrt m$ per evaluation and about $m$ in all. The outward pointers give a cheap substitute. Two columns can be compared in polylogarithmically many queries by decoding both addresses and following each one's pointer into the other. A genuine winner $i^\star$ wins every comparison with high probability: its pointer finds a zero in the rival, and nothing can point to a zero in $X_{i^\star}$. That holds whatever the rival's address inputs are, including inputs outside the promise of $P$. Comparisons between losers, however, can be cyclic, unbiased or arbitrary. Section 4 shows that a tournament with fractional weights tolerates exactly this behaviour, produces $O(\log m)$ candidates in $\sqrt m\cdot\mathrm{polylog}(m)$ queries, and leaves only those candidates to be verified.

## 2. The construction

Fix $k\ge2$, $t\ge1$, $m=4^t$, $\ell=2t$ and $r=20\ell$. Identify a bit $a$ with the sign $(-1)^a$. Let $H$ be the normalised $m\times m$ Walsh–Hadamard matrix and $u=m^{-1/2}(1,\dots,1)^{\mathsf T}$. For sign vectors $z_1,\dots,z_k\in\{\pm1\}^m$ put
$$
\Phi(z)=u^{\mathsf T}\operatorname{diag}(z_1)\,H\operatorname{diag}(z_2)\,H\cdots H\operatorname{diag}(z_k)\,u,
\qquad \delta=2^{-5k},
\tag*{(3)\quad\textsf{P3}}
$$
so $|\Phi|\le1$. The partial function $P=P_{k,m}$ on $km$ bits is
$$
P(z)=1\ \text{ if }\Phi(z)\ge\delta,\qquad P(z)=0\ \text{ if }|\Phi(z)|\le\delta/2,
\tag*{(4)\quad\textsf{P4}}
$$
and undefined otherwise; a large negative $\Phi$ is outside the promise. It has three properties [@OpenAI2026, Lemma 2.1].

(i) For fixed $k$ and all large $m$, with $L=\bigl\lfloor m^{1-1/k}/\ell^2\bigr\rfloor$,
$$
L<R(P).
\tag*{(5)\quad\textsf{P5}}
$$
This follows from Bansal and Sinha's bound $R(P)=\Omega\bigl(k^{-29}(m/\log(km))^{1-1/k}\bigr)$ [@BansalSinha2021, Corollary 1.4]; Section 6 describes the alternative proof used in Lean.

(ii) For $0<\eta<1/2$ a quantum algorithm with $O_k(1+\log(1/\eta))$ queries computes $P$ with error at most $\eta$ on its domain. It prepares $u$, applies the product in (3), and measures the projection onto $u$, which succeeds with probability $\Phi^2$; repetition separates $\Phi^2\ge\delta^2$ from $\Phi^2\le\delta^2/4$. It runs coherently with its workspace retained, and outputs some bit, within the same cap, on every input.

(iii) An exact fan-in-two Boolean circuit $\mathcal C$ of size $S\le200(k+1)^2m\ell^2$ outputs a domain bit, equal to one exactly on the domain of $P$, and a value bit equal to $P$ there. With the integer matrix $\sqrt m H$, $\Phi=N/m^{(k+1)/2}$ for an integer $N$, and the two cases of (4) become $2^{5k}N\ge m^{(k+1)/2}$ and $2^{5k+1}|N|\le m^{(k+1)/2}$, which fast Walsh transforms on $O_k(\ell)$-bit integers decide.

The exact domain bit matters because the projection statistic sees only $\Phi^2$ (row 1 of Table 1).

**The total function.** Column $i\in[m]$ consists of $X_i\in\{0,1\}^m$, strings $A_{i,1},\dots,A_{i,r}\in\{0,1\}^{km}$, and for each $s\in\{0,1\}^r$ a cell $B_{i,s}$ containing an $\ell$-bit pointer $p_{i,s,j}\in[m]$ for each $j\ne i$ and $r$ alleged transcripts of $\mathcal C$, one bit per non-input gate. All of these are independent input bits. Column $i$ **wins** if $X_i=1^m$, every $P(A_{i,h})$ is defined, and the cell at $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ holds the true transcripts of $\mathcal C$ on each $A_{i,h}$ and pointers with
$$
X_j[p_{i,s_i,j}]=0\qquad\text{for every }j\ne i.
\tag*{(6)\quad\textsf{P8}}
$$
$F_{k,m}=1$ exactly when some column wins. This is a total function: no promise is imposed on the address inputs, pointers or transcripts. There is at most one winner, since a winner's pointer into a second all-one column would find a zero there.

**Local tests** [@OpenAI2026, Lemma 2.2]. For a fixed pair $(i,s)$, "$i$ wins and $s=s_i$" is the conjunction of
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3)
$$
tests: $m$ tests $X_i[y]=1$, $m-1$ pointer tests, one consistency test per gate of each transcript, and two output tests per transcript (domain bit $1$, value bit $s_h$). Induction in topological order shows that a gate-consistent transcript is the true evaluation, so the output tests say exactly that $P(A_{i,h})$ is defined and equals $s_h$. A gate test makes at most three queries and a pointer test $\ell+1$ adaptive queries. Every test can be evaluated coherently, with its index in superposition, at a constant-factor overhead in queries. Hence a winner passes all tests at its address, and a non-winning column fails some test at every address.

## 3. Where a natural shortcut fails

Each row of Table 1 is a step that a reader may be tempted to simplify, with an explicit instance showing that the simplification is false. Each instance is checked in the companion record or in its review material; the right column names the place where the correct argument is used.

: Natural shortcuts and their counterexamples. Here $\beta$ is the best one-instance success within the cap.

| Shortcut | Counterexample | Used in |
|:-------------------------|:----------------------------------------------------|:-------|
| Decide the promise from the projection statistic $\Phi^2$ | $k=2$, $m=4$, $z_1=z_2=(-1,1,1,1)$: $\Phi=-1$, so $\Phi^2=1$, yet $z$ is outside the promise | §2 (iii) |
| Treat comparisons as bounded-error queries to a fixed tournament | Three losers $a,b,c$ with $a$ beating $b$, $b$ beating $c$, $c$ beating $a$, each with probability $1$, or any pair at exactly $1/2$ | §4.2 |
| Output a column that wins every comparison | An all-one column $1$ whose certificate is correct except that its pointer into column $j>1$ reaches a one: nothing disqualifies column $1$ and the index tie-break awards it the comparison with $j$, yet no column wins | §4.3 |
| Choose the planted column with a uniform marginal law | Query row $1$ of each of four columns, then choose $I$ uniformly among columns where a zero was found: $I$ is still uniform, but its zero is found with probability $175/256$, against $\mathbb EZ/m=1/4$ | §5.3 |
| Cap the address queries in expectation | Two-bit parity, $\beta=1/2$: a shared fair coin either computes both instances exactly or guesses both; expected cost one per instance, success $5/8>\beta^2=1/4$ | §5.1 |
| Side information independent of each input separately | $P(x)=x$ on one fair bit, cap $0$, inputs $X,Y$: given $S=X\oplus Y$, answering $(0,S)$ succeeds with probability $1/2>1/4$ | §5.1 |
| Condition on the caps being respected | AND on two uniform bits, $\beta=3/4$, two instances: success together with the caps has probability $5/16\le9/16$, but success given the caps is $5/8>9/16$ | §5.4 |
| Let $k$ grow inside a fixed-$k$ threshold | "$t\ge2^k$" holds eventually for every fixed $k$ and fails for every $t$ when $k=t$ | §7 |

The conditioning example in row 7 is the algorithm that queries bit $A_0$ of the first instance, then bit $B_{A_0}$ of the second, queries $A_0$ again if the two answers differ, and outputs $(0,0)$. Of the sixteen equally likely inputs, eight respect both caps and five of those are answered correctly.

## 4. The quantum upper bound

Put $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$.

**Lemma 2** (bounded amplification [@OpenAI2026, Lemma 3.1])**.** Let $\mathcal A$ be a state preparation with a success flag, success probability $p$, and normalised successful state $|g\rangle$ when $p>0$. For $0<\gamma\le1/2$ and $0<\eta<1/2$ there is a procedure making $O(\gamma^{-1/2}\log(1/\eta))$ calls to $\mathcal A$ and $\mathcal A^{-1}$ on every branch, for every $p$, that either reports failure or returns a success; conditional on success its output state is $|g\rangle$ up to a global phase. It fails with probability at most $\eta$ if $p\ge\gamma$, and always if $p=0$.

*Sketch.* Write $\mathcal A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle$. After $j$ Grover iterations the successful component is $\sin((2j+1)\theta)|g\rangle$, so every successful measurement leaves the same normalised state. A trial uses $j=0$ with probability $1/2$ and otherwise $j$ uniform in $\{0,\dots,M-1\}$, $M=\lceil10/\sqrt\gamma\rceil$; the averaged success is at least $9/40$ whenever $p\ge\gamma$ [@BBHT1998, Lemma 2; @BHMT2002]. A fixed number of fresh trials, stopping at the first success, gives the cap and the failure bound, and leaves the conditional state unchanged. Lean proves the lemma in this full form: the amplified procedure returns the original register in the normalised successful state, with the exact success mass, within the stated cap ([Lean statement][cmp-amplifier]), and Comparator accepts that statement. The upper bound below uses only the law of the measured label, which the formal development of Theorem 1 proves.

### 4.1 Comparisons

To decode column $i$, run the algorithm of §2 (ii) on each $A_{i,h}$ with error $\varepsilon/r$, at cost $O_k(r\log(r/\varepsilon))$. If all $r$ instances are promised, the decoded address is $s_i$ with probability at least $1-\varepsilon$; otherwise some address is returned within the same cap. For an unordered pair $\{i,j\}$, sort the indices and run one fixed circuit: decode both columns, read each column's pointer into the other at its decoded address, and inspect the bit it names. A column disqualifies the other if that bit is $0$. If exactly one column disqualifies the other, it is the victor; otherwise the smaller index is. A self-comparison is a loss. Let $a_{ij}$ be the probability that $i$ defeats $j$, with $a_{ii}=0$. Because both orders use the same circuit,
$$
a_{ij}+a_{ji}=1\qquad(i\ne j).
\tag*{(7)\quad\textsf{P10}}
$$
If $i^\star$ wins, no pointer finds a zero in $X_{i^\star}=1^m$, and whenever $i^\star$ is decoded correctly its pointer finds a zero in the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every $j\ne i^\star$, whatever the rival's address inputs. The decoded labels stay in orthogonal registers, so these probabilities are the measured probabilities of the coherent circuit. One comparison costs $c=O_k(\ell\log\ell)$ queries.

### 4.2 A tournament with probabilistic comparisons

**Proposition 3** [@OpenAI2026, Proposition 3.2]**.** Let a coherent comparison with cost $c$ satisfy (7). A quantum algorithm with $O(c\sqrt m\,T^2\log T)$ queries on every branch returns at most $T$ candidates, and if some $i^\star$ has $a_{i^\star j}\ge1-\varepsilon$ for all $j\ne i^\star$, the list contains $i^\star$ with probability at least $1-2m2^{-T}-T\varepsilon$.

*Ideal process.* Start with weights $w_i=1$ and $W=\sum_iw_i$. While $W>0$, draw a pivot $\rho$ with probability $w_\rho/W$, append it to the list, and update $w_i\leftarrow w_i\,a_{i\rho}$. By (7), pairing the terms $(i,\rho)$ and $(\rho,i)$,
$$
\mathbb E[W_{\rm new}\mid w]=\frac1W\sum_{\rho,i}w_\rho w_i a_{i\rho}=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\tag*{(8)\quad\textsf{P13}}
$$
No order or transitivity enters: cycles among losers only make the weights fall faster. After $T$ steps $\mathbb EW\le m2^{-T}$. Until $i^\star$ is drawn its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$, so by Markov's inequality $i^\star$ is missing from the ideal list with probability at most $2m2^{-T}$.

*Exact sampling.* The algorithm never computes the weights. Given pivots $\rho_1,\dots,\rho_n$ with $n<T$, it prepares
$$
\frac1{\sqrt m}\sum_{i=1}^m|i\rangle\bigotimes_{b=1}^{n}|\phi(i,\rho_b)\rangle,
\tag*{(9)\quad\textsf{P15}}
$$
where $|\phi(i,\rho_b)\rangle$ is the full comparison state in a fresh workspace, and flags success when every comparison says that $i$ wins. The tensor product gives success-and-label mass $m^{-1}\prod_ba_{i\rho_b}=w_i/m$, so the total success probability is $W/m$ and the label law conditional on success is exactly $w_i/W$. Apply Lemma 2 with $\gamma=1/(2m)$ and $\eta=\varepsilon$; on reported failure, stop and return the list.

*Coupling.* Until $i^\star$ is drawn, $W/m\ge1/(2m)$, so at every such history the stage fails with probability at most $\varepsilon$ and otherwise draws a pivot with exactly the ideal law. Coupling stage by stage, conditional on the entire past (the failure probabilities may depend on the history), adds at most $T\varepsilon$ to the miss probability, and a failure after $i^\star$ is listed does not remove it. Stage $n$ costs $O(c(n+1)\sqrt m\log(1/\varepsilon))$ queries whether or not a dominant candidate exists. Summing over $n<T$ proves the proposition. Full proof: [record §5.2](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md#upper-ideal-process).

### 4.3 Verification and the query count

Even a column that beats every rival with probability at least $1-\varepsilon$ need not win (row 3 of Table 1), so each listed candidate is verified. Decode its address afresh. At that fixed address, a uniformly random one of the $K$ local tests fails with probability $0$ if all pass and at least $1/K$ otherwise; Lemma 2 with $\gamma=1/K$ and $\eta=\varepsilon$ finds a failing test, if there is one, in $O(\sqrt K\,\ell\log(1/\varepsilon))$ queries. A non-winner is accepted with probability at most $\varepsilon$, and a winner is accepted whenever its address is decoded correctly. Accept the input if some candidate is accepted. The error is at most $T\varepsilon$ on zero-inputs and at most $2m2^{-T}+T\varepsilon+\varepsilon<1/3$ on one-inputs. Pointers are read bit by bit and array indices are computed reversibly; a controlled query costs two ordinary queries. No unit-cost pointer oracle is assumed.

The exponent six in (2) is a deliberately loose count of the explicit budget [@Record2026, §5.4]: $T=O(\ell)$ stages, each padded to $T$ comparisons per call; $O(\ell)$ amplification trials, from bounding $\log(1/\varepsilon)$ by $1/\varepsilon$; $O(\sqrt m)$ iterations; and a comparison cost bounded by $O_k(\ell^3)$. This gives $\sqrt m\,\ell^6$ for the tournament, and the $T$ verifications cost less. Nothing below depends on the logarithmic exponent.

## 5. The randomized lower bound

The lower bound applies to any partial function $P$ with an exact circuit as in §2 (iii) and any integer $L$ with $1\le L\le m$ and $L<R(P)$. By finite minimax [@Yao1977] there is a law $\mu$ on the domain of $P$ under which every deterministic tree of depth at most $L$ succeeds with probability at most $\beta=2/3$; the maximum over randomized depth-$L$ algorithms is attained, and it is below $2/3$ because $L<R(P)$.

### 5.1 A direct product with separate caps

**Lemma 4** [@OpenAI2026, Lemma 4.1]**.** Let $U_1,\dots,U_r$ be independent with law $\mu$. An algorithm that makes at most $L$ queries to each $U_h$ on every branch, interleaving them adaptively, outputs $(P(U_1),\dots,P(U_r))$ with probability at most $\beta^r$. Its random coins and any side information are allowed if they are jointly independent of $(U_1,\dots,U_r)$.

*Proof.* For a nonnegative measure $\nu$ on the domain of $P$, let $V_d(\nu)$ be the largest $\nu$-weight of inputs on which a depth-$d$ tree answers correctly. Then $V_0(\nu)=\max_b\nu(P=b)$ and
$$
V_{d+1}(\nu)=\max\Bigl\{V_d(\nu),\ \max_y\bigl[V_d(\nu_{y,0})+V_d(\nu_{y,1})\bigr]\Bigr\},
$$
where $\nu_{y,b}$ is the restriction of $\nu$ to inputs with bit $y$ equal to $b$. For product measures $\nu_1\otimes\dots\otimes\nu_r$ and remaining budgets $L_1,\dots,L_r$, induction on a deterministic vector-output tree shows that its weight of fully correct inputs is at most $\prod_hV_{L_h}(\nu_h)$. At a leaf the correct weight factorises. A query to input $h$ restricts only $\nu_h$ and lowers only $L_h$, and its two branches are absorbed by the recursion; zero-weight branches need no division. Initially every factor is at most $\beta$. Fix the coins and side information, apply this bound, and average. $\square$

The caps must hold on every branch and the independence must be joint (rows 5 and 6 of Table 1). This is the separately capped mechanism of Shaltiel and Drucker [@Shaltiel2003; @Drucker2012, §1.3 and Lemmas 3.1–3.2]. Lean proves Lemma 4 with coins and side information drawn from an arbitrary finite probability space jointly independent of the inputs ([Lean statement][cmp-direct-product]), and Comparator accepts that statement; because a capped algorithm has finitely many deterministic behaviours, this covers arbitrary independent randomness.
### 5.2 Planting a winner

Let $G=\lfloor mL/100\rfloor$. The **dummy input** $Y^{(0)}$ chooses independent uniform rows $J_1,\dots,J_m\in[m]$, puts a single zero at $X_i[J_i]$, draws every $A_{i,h}$ independently from $\mu$, and leaves every cell blank. It has no winner. Choose $I\in[m]$ uniformly and independently of all of $Y^{(0)}$. The **planted input** $Y^{(1)}$ erases the zero of column $I$ and fills only the cell $B_{I,s_I}$ with the true transcripts and the pointers $p_{I,s_I,j}=J_j$; column $I$ wins (Figure 2).

![The two coupled inputs. They differ only at the erased zero $X_I[J_I]$ and inside the cell $B_{I,s_I}$; the address inputs, drawn from $\mu$, are the same in both.](figures/expert_planted.svg){width=100%}

Fix a deterministic tree $\mathcal T$ of depth at most $G$. Its runs on $Y^{(0)}$ and $Y^{(1)}$ agree until the run on $Y^{(0)}$ queries $X_I[J_I]$ or a bit of $B_{I,s_I}$, so
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|
\le\Pr[\mathcal T\text{ queries }X_I[J_I]]+\Pr[\mathcal T\text{ queries }B_{I,s_I}],
\tag*{(10)\quad\textsf{P18}}
$$
with both probabilities computed for the run on $Y^{(0)}$.

### 5.3 The erased zero

Let $Z$ be the number of columns whose zero the run on $Y^{(0)}$ queries. For fixed dummy data exactly $Z$ of the $m$ choices of $I$ select a discovered zero, so
$$
\Pr[\mathcal T\text{ queries }X_I[J_I]]=\frac{\mathbb EZ}{m}.
\tag*{(11)\quad\textsf{P19}}
$$
This identity uses that $I$ is independent of the whole dummy run; a uniform marginal law is not enough (row 4 of Table 1).

To bound $\mathbb EZ$, fix column $i$ and all data outside $X_i$, and run $\mathcal T$ on the reference input in which $X_i=1^m$. Let $y_1,\dots,y_v$ be the distinct rows of $X_i$ it queries, in order of first query. If $J_i=y_n$, the run follows the reference run until it queries $y_n$, so it discovers the zero after at least $n$ queries to $X_i$; if $J_i$ is not among the $y_n$, it is the reference run, makes at least $v$ queries to $X_i$, and discovers nothing. Averaging over the uniform $J_i$, the discovery probability is $v/m$, and the expected number $q_i$ of queries to $X_i$ is at least $\bigl(\tfrac{v(v+1)}2+(m-v)v\bigr)/m\ge\tfrac{v(m+1)}{2m}$. Hence the discovery probability is at most $2q_i/(m+1)$. Averaging over the outside data and summing over columns, with $\sum_iq_i\le G$,
$$
\mathbb EZ\le\frac{2G}{m+1},\qquad
\Pr[\mathcal T\text{ queries }X_I[J_I]]\le\frac{2G}{m(m+1)}.
$$
The preprint's early-and-late count gives $4G/m^2$, which also suffices. Lean proves (11) with the bound $4G/m^2$ as a [directly compared statement][cmp-eq11], and proves the bound $2G/m^2$ by an [induction over the $m$ possible zero positions][src-zero-two]. The counting inequality behind $2G/(m(m+1))$ is proved in Lean by the [same induction with $|U|+1$ in place of $|U|$][src-zero-successor]; the averaging step from it to the probability bound is the ordinary argument above.
### 5.4 The planted cell

Let $\lambda_i$ be the number of queries, counting repetitions, that the run on $Y^{(0)}$ makes to $A_{i,1},\dots,A_{i,r}$, and call column $i$ heavy if $\lambda_i>L$. At most $G/L$ columns are heavy, so $\Pr[I\text{ heavy}]\le G/(mL)$.

Fix a column $i$ and a time $\tau\in\{1,\dots,G\}$. A simulator receives as free information all of $Y^{(0)}$ outside $A_{i,1},\dots,A_{i,r}$, which is jointly independent of those $r$ inputs and does not reveal $s_i$. It runs $\mathcal T$, answering other queries from the free information and querying the $A_{i,h}$ itself, and aborts before an $(L+1)$-st query to them in total. If it reaches time $\tau$ and the $\tau$-th query lies in a cell $B_{i,s}$, it outputs $s$; otherwise it outputs a fixed vector. Its total cap on the $A_{i,h}$ is $L$, so Lemma 4 applies. If $i$ is not heavy and the $\tau$-th query of the original run lies in $B_{i,s_i}$, the simulator has not aborted and outputs $s_i$. Therefore
$$
\Pr\bigl[\,i\text{ is not heavy and the }\tau\text{-th query lies in }B_{i,s_i}\bigr]\le\beta^r .
\tag*{(12)\quad\textsf{P21}}
$$
This bounds a joint event under the original law. Conditioning on the cheap event "$i$ is not heavy" would change the law of the address inputs and can make the conditional success exceed $\beta^r$ (row 7 of Table 1). A union bound over the $G$ times, an average over the independent $I$, and the heavy columns give
$$
\Pr[\mathcal T\text{ queries }B_{I,s_I}]\le\frac G{mL}+G\beta^r.
\tag*{(13)\quad\textsf{P22}}
$$

### 5.5 The contradiction and the constants

By (10), (11) and (13), with $G\le mL/100\le m^2/100$ and $\beta^r=(2/3)^{20\ell}\le m^{-10}$,
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|\le\frac{2G}{m(m+1)}+\frac G{mL}+G\beta^r\le\frac4{100}.
\tag*{(14)\quad\textsf{P23}}
$$
A randomized algorithm of worst-case cost $G$ is an average of such trees, so it satisfies (14) as well, whereas error at most $1/3$ on the zero-input $Y^{(0)}$ and the one-input $Y^{(1)}$ would force a gap of at least $1/3$. Hence, for every $P$ and $L$ as above,
$$
R(F_{k,m})>\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor.
\tag*{(15)\quad\textsf{P17}}
$$
For the constant in (2), take $k\ge2$ and $t\ge8$. Then $4t^2\le2^t\le m^{1-1/k}$, so $x=m^{1-1/k}/\ell^2\ge1$ and $L=\lfloor x\rfloor\ge x/2$; also $mL\ge200$, so $\lfloor mL/100\rfloor\ge mL/200\ge m^{2-1/k}/(400\ell^2)$. Section 6 gives $L<R(P_{k,m})$ for $t\ge13669k^2$. Full proof: [record §6](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md#CL-discrepancy).

## 6. The Forrelation lower bound

The construction needs only (5), the fixed-$k$, constant-error consequence of Bansal and Sinha's theorem [@BansalSinha2021, Theorem 1.3 and Corollary 1.4]; Sherstov, Storozhenko and Wu prove a sharper bound [@SSW2023]. The Lean formalisation proves (5) by a different and shorter route, in the following uniform form: for $m=4^t$ and $15k+2\le2t$,
$$
R(P_{k,m})>\frac{2}{18225}\,\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{16}
$$
For $t\ge13669k^2$ one has $\ln(4km)\le6t$ and $8t^2>109350\,k^2t$, so (16) exceeds $m^{1-1/k}/\ell^2$ and implies (5).

*Route.* Interpolate between the uniform law $\mathcal D_0$ and a planted law $\mathcal D_1$ along a path that is Gaussian in the first block only: independent Gaussian blocks determine sign biases for all $k$ blocks, the signs are rounded independently from those biases, and sequential Gaussian reflections show that the endpoint $\mathcal D_0$ is exactly uniform. For a depth-$d$ tree, the derivative of its acceptance along the path starts in the first block and is moved through successive blocks by Gaussian integration by parts, each step contributing one Walsh entry and a bounded factor. The resulting mixed derivatives of the tree's multilinear extension are bounded by a stopped-martingale induction in the style of Girish, Tal and Wu [@GTW2021], which stops before a contracted lower-degree polynomial becomes large and so avoids conditioning on a favourable future event. This yields
$$
\bigl|\mathbb E_{\mathcal D_1}g-\mathbb E_{\mathcal D_0}g\bigr|\le\Bigl(\frac{3}{16\sqrt m}\Bigr)^{k-1}\Bigl[\bigl(16kd\ln(4km)\bigr)^{k/2}+2^{-k}\Bigr]
$$
for every depth-$d$ tree with output $g\in[-1,1]$. The Gaussian chain and the transformed integration by parts are Bansal and Sinha's; the tree martingale follows Girish, Tal and Wu.

The planted law $\mathcal D_1$ is not supported on promised one-inputs, and the proof handles this directly. With $\mathbb E_{\mathcal D_1}\Phi\ge\vartheta_k=18^{-(k-1)}$, $\mathbb E_{\mathcal D_0}\Phi=0$ and $\mathbb E_{\mathcal D_0}\Phi^2=1/m$, a solver amplified to error $\epsilon\le\vartheta_k/18$ has acceptance probability $A(z)$ satisfying, on every input,
$$
(1-\epsilon)(\Phi-\delta)\le A\le\epsilon+4\Phi^2/\delta^2,
$$
because the promise is one-sided. Taking expectations, the acceptance gap is at least $\tfrac{119}{144}\vartheta_k$, while the derivative bound caps it at $\tfrac{7}{12}\vartheta_k$ below the depth in (16). Full proof: [record §§3.6–3.15](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md#forr_target).

The [compared Lean theorem][thm-forrelation] states (5) for each fixed $k$ with an unspecified threshold; the [uniform estimate (16)][src-forrelation-uniform] is built but has not been compared. No person has yet reviewed this Lean proof.

## 7. The exponent

Fix $0\le\alpha<4$ and choose an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $e=2-1/k-\alpha/2>0$. Keep $k$ fixed and let $m=4^t$ grow. For $t\ge13669k^2$, (2) gives $1+Q(F_{k,m})\le(1+C_k)\sqrt m\,\ell^6$ and
$$
\frac{R(F_{k,m})}{\bigl(1+Q(F_{k,m})\bigr)^\alpha}\ge\frac{1}{400(1+C_k)^\alpha}\,\frac{m^{e}}{\ell^{2+6\alpha}}\longrightarrow\infty,
$$
so no $C_\alpha$ in (1) exists. With the upper bound of [@ABKRT2021], $\alpha_{\rm tot}=4$. The order of quantifiers is: the exponent $\alpha$, then one fixed $k$, then its constants and threshold, then $m\to\infty$, with one circuit $\mathcal C$ serving both bounds in (2). For fixed $k$ this excludes exponents below $4-2/k$ only; it gives no separation of the form $R=\Omega(Q^4)$.

**Remark** (one explicit sequence)**.** Letting $k$ grow requires control uniform in $k$ (row 8 of Table 1). Three ingredients supply it: the uniform estimate (16), the bound (15) for every admissible $L$, and the explicit quantum budget $Q(F_{k,m})\le2^{53}k\,2^{10k}\sqrt m\,\ell^6$, valid for all $k,t\ge1$. For $2\le k\le t$ and $t\ge32$, the right side $X$ of (16) satisfies $2\le X\le m$; taking $L=\lfloor X\rfloor\ge X/2$ in (15) gives $R(F_{k,m})>m^{2-1/k}/\bigl(1822500\,k^2\ln(4km)\bigr)$. For every integer $t\ge80$ put $k=\lfloor\sqrt{t/20}\rfloor$, so that $15k+2\le2t$, and $F_t=F_{k,4^t}$. Comparing $\log_2R>(2-1/k)\ell-\log_2\bigl(1822500\,k^2\ln(4km)\bigr)$ with $\log_2Q\le\ell/2+10k+53+\log_2k+6\log_2\ell$ gives
$$
R(F_t)\ge Q(F_t)^{4-\varepsilon(\ell)},\qquad
\varepsilon(\ell)=\frac{8\sqrt{10}}{\sqrt{\ell}}+\frac{56\log_2\ell+508}{\ell},
$$
and, with the universal quartic bound, $\log R(F_t)/\log Q(F_t)\to4$. The deficit is $O(1/\sqrt{\log m})$; this single sequence still gives no bound of the form $R=\Omega(Q^4)$. The remark is an ordinary deduction with no Lean counterpart, and the [quantum budget][src-budget] it uses is built in Lean but has not been compared.

<!-- pdf-page-break -->

## Appendix A. Checking the statement

A proof checker establishes that a proof proves its stated type. What remains is whether the formal statement says what Theorem 1 says. This appendix lists everything a reader must read to answer that question. The [statement file][statement-file] in the repository [@Repo2026] has 343 lines and imports only Mathlib. Its definitions follow in file order, each linked to its lines.

| Object | Meaning in the file |
|:-------------------------------|:-------------------------------------------------------------|
| [Partial functions][def-partial] and [totalisation][def-totalise] | A missing value marks an input outside the promise; totalising $f$ promises every input. |
| [Trees][def-tree] and [randomized algorithms][def-randomized] | Depth charges repeated queries. A randomized algorithm is a finite mixture of trees with positive real weights summing to $1$. |
| [The test $R\le d$][def-RLe] and [the cost $R$][def-R] | Some mixture of depth at most $d$ succeeds with probability at least $2/3$ on every promised input; $R$ is the least such $d$. |
| [Basis states][def-basis] and [the oracle][def-oracle] | Basis $\lvert i,b,z\rangle$ with a finite workspace $z$; the oracle is exactly $O_x$. |
| [Quantum algorithms][def-adaptive] | Unitaries fixed before the input, oracle calls, and binary measurements of sets of basis states, with classical branching. |
| [The query cap][def-querycap] | The largest number of oracle calls over all branches, defined syntactically and so valid on every input. |
| [The test $Q\le c$][def-QLe] and [the cost $Q$][def-Q] | A constant function on the promise, or a unit initial state and a program within the cap that succeeds with probability at least $2/3$ on every promised input; $Q$ is the least such cap. |
| [The numerator $N$][def-numerator] and [$P$][def-P] | $N$ as a sum over Walsh paths; $P$ by the integer tests of §2 (iii). |
| [Circuits][def-circuit] and [exact circuits for $P$][def-realises] | Fan-in-two circuits; the domain bit is $1$ exactly on the promise, and there the value bit is $P$. |
| [Input bits][def-bitloc], [winning][def-wins], [$F_{k,m}$][def-F] | The four kinds of input bit; the winning condition (6); $F_{k,m}$ with $\ell=2t$ and $r=40t$. |
| [The budget $L$][def-L] and [the depth $G$][def-G] | $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$ and $G=\lfloor mL/100\rfloor$. |
| [Hardness][def-bansal-sinha], [power bound][def-universal], [$\alpha_{\rm tot}$][def-alpha] | Statement (5); membership in the set of (1); $\alpha_{\rm tot}$ as the infimum of that set. |

The file also defines a [comparison predicate][def-comparison] that the four theorems do not use.

**The four compared theorems**, in the [closing lines][thm-all] of the file.

1. [The exponent][thm-alpha]: $\alpha_{\rm tot}=4$.
2. [The family][thm-headline]: $\alpha_{\rm tot}=4$, the universal bound $R\le C(1+Q)^4$, and for each $k\ge2$ there are naturals $S$, $A>0$, $b$ and $t_0$ such that for every $t\ge\max(1,t_0)$ some circuit $\mathcal C$ realising $P_{k,4^t}$ has $|\mathcal C|\le S\,m(2t)^2$, $Q(F_{k,m})\le A\,2^t(2t)^b$ and $\lfloor mL/100\rfloor<R(F_{k,m})$, where $F_{k,m}$ is built from that same $\mathcal C$.
3. [The cubic bound fails][thm-cubic]: no real $C$ has $R(f)\le C\,Q(f)^3$ for all total $f$.
4. [Forrelation is hard][thm-forrelation]: (5) holds for every $k\ge2$, beyond some threshold.

The exponent $b$ is existential here. The values $b=6$ and $1/400$ are proved by a [stronger form of the family theorem][src-constants], which is built but has not been compared.

**Five things to check.**

1. *Error and cost.* The bound $2/3\le$ success is non-strict and required on every promised input, and caps are worst case over all branches.
2. *Input access.* Quantum unitaries are chosen before the input, and the only access to the input is $O_x$.
3. *Totality.* [Totalisation][def-totalise] imposes no promise, so $F_{k,m}$ is total.
4. *The infimum.* [$\alpha_{\rm tot}$][def-alpha] is an infimum of reals, and Mathlib's infimum of the empty set is $0$; the [family theorem][thm-headline] also proves the [power bound][def-universal] with exponent $4$, so the set is nonempty.
5. *Quantifier order.* The order is $\forall k\ \exists S,A,b,t_0\ \forall t\ \exists\mathcal C$, with one $\mathcal C$ for both bounds.

Two further sanity theorems test the models directly: [$D(f)$, $R(f)$ and $Q(f)$ are zero][cmp-zero-cost] exactly when all promised inputs share one value, and the [degree used in the universal bound][cmp-degree] is the degree of the unique multilinear representation. Both are proved in Lean and accepted by Comparator.
**What Comparator establishes.** The challenge file and the solution are compiled separately. For each theorem named in [the configuration][statement-config], the solution's declaration has the same type as the challenge's, built from the challenge's definitions, so a solution cannot redefine $R$, $Q$ or $F$. The proofs use only Lean's three standard axioms: propositional extensionality, soundness of quotients and choice. The run used Comparator's paranoid mode, which rechecks with the external kernels bundled with Lean, and [five deliberately wrong solutions][cmp-negative] (a changed definition, a foreign axiom, a missing declaration, an unfinished proof, a weakened conclusion) are rejected in the same setup. Besides the four theorems, [Lemma 2.2 of the preprint][cmp-lemma22-full] and [its parts][cmp-lemma22], and [(11) with the bound $4G/m^2$][cmp-eq11], are compared in their own statements.

**What it does not establish.** Whether the definitions model the intended query models is what the reader is checking: both sides come from one specification, so a modelling error shared by both would pass. Theorems that are not configured targets, such as the [constants theorem][src-constants] and the [per-time event (12)][src-per-time], are built without comparison. The recorded runs were local and unsandboxed. No person has reviewed the definitions or the Forrelation proof.

**Reproducing the check.** The recorded runs used the versions in the first line below; the statement file is identical at the commit the links above point to. From `lean/`, the last command runs a [dependency printer][src-reach] that lists the closure the kernel checked; the recorded Comparator runs added `--inadvisably-no-sandbox`.

```
# commit c996e486, toolchain leanprover/lean4:v4.36.0-rc2, Mathlib 69552756cd8a
lake build QuarticQuery
lake comparator --config QuarticCorpus/Unconditional/comparator.json --paranoid
lake env lean --run scripts/Reach.lean QuarticQuery.Checked.theorem_one_one
```

## Note on preparation

This companion and its Lean development were prepared with AI systems under the author's direction. Sources, proofs and run records are in the repository [@Repo2026]; full proofs of every step are in the companion reasoning record [@Record2026].

## References

::: {#refs}
:::

<!-- lean-links -->
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/main/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L20
[cmp-degree]: https://github.com/wcook04/quartic-query-lean/blob/main/lean/QuarticCorpus/Independent/Degree/Challenge.lean#L14-L20
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/main/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[cmp-eq11]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Independent/Eq19/Challenge.lean#L19-L24
[cmp-lemma22]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Construction/Challenge.lean
[cmp-lemma22-full]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean#L14-L41
[cmp-negative]: https://github.com/wcook04/quartic-query-lean/tree/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Negative
[cmp-zero-cost]: https://github.com/wcook04/quartic-query-lean/blob/main/lean/QuarticCorpus/Independent/ModelZero/Challenge.lean#L11-L14
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L280-L285
[def-G]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L302-L303
[def-L]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L297-L300
[def-P]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L175-L182
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-QLe]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L133-L137
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-RLe]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L62-L65
[def-adaptive]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L101-L107
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-bansal-sinha]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L305-L309
[def-basis]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L84-L87
[def-bitloc]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L232-L238
[def-circuit]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L190-L199
[def-comparison]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L289-L293
[def-numerator]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L160-L166
[def-oracle]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L89-L94
[def-partial]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L18-L19
[def-querycap]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L109-L116
[def-randomized]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L46-L60
[def-realises]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L215-L221
[def-totalise]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L21-L22
[def-tree]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L33-L44
[def-universal]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L311-L315
[def-wins]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272
[src-budget]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticQuery/Upper/Bound.lean#L86-L90
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[src-forrelation-uniform]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532
[src-per-time]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L340-L348
[src-reach]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/scripts/Reach.lean
[src-zero-successor]: https://github.com/wcook04/quartic-query-lean/blob/main/lean/QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean#L17-L22
[src-zero-two]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L213-L219
[statement-config]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/comparator.json
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/752826a36192b25dc08e364a070eb03eb95dbc85/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
