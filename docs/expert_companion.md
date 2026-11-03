---
title: "The optimal randomized–quantum query exponent is four"
subtitle: "A companion to OpenAI's nearly quartic separation"
author: "Will Cook"
date: "November 2026"
bibliography: expert_companion.bib
link-citations: true
abstract: |
  OpenAI's preprint constructs total Boolean functions $F$ with $R(F)\ge Q(F)^{4-o(1)}$. Since $R=O(Q^4)$ for every total function, the optimal exponent relating bounded-error randomized and quantum query complexity is exactly four, and the conjectured cubic bound of Aaronson, Ben-David, Kothari, Rao and Tal fails. The previous best separation was $R=Q^{3-o(1)}$, obtained from the cheat-sheet framework once Bansal and Sinha, and independently Sherstov, Storozhenko and Wu, proved an optimal partial separation. The new idea is to give each of $m$ columns its own array of certificate cells, addressed by the answers to hard Forrelation instances, so that a classical algorithm pays about $m^{1-1/k}$ queries per column across about $m$ columns, while a quantum algorithm finds the winning column in about $\sqrt m$ queries by comparisons in which a genuine winner beats every rival; this gives $R\approx Q^{4-2/k}$. This companion gives the argument with explicit constants, lists natural shortcuts that fail with a counterexample for each, and compares the statements of a Lean formalisation with the paper's.
---

## 1. The result and what is new

A query reads one input bit; computation between queries is free. For a partial function $f$, $R(f)$ and $Q(f)$ are the least worst-case numbers of queries made by a randomized, respectively quantum, algorithm that answers correctly with probability at least $2/3$ on every input in the domain of $f$. The query cap holds on every input, every random choice and every measurement branch, including inputs outside the domain. Quantum queries use $O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle$. For total functions put
$$
\alpha_{\rm tot}=\inf\Bigl\{\alpha\ge0:\ \exists C_\alpha>0\ \forall n\ge1\ \forall f:\{0,1\}^n\to\{0,1\},\ \ R(f)\le C_\alpha\bigl(1+Q(f)\bigr)^\alpha\Bigr\}.
\tag{1}
$$
One constant serves every input length and every function; the added one covers constant functions. Throughout, $\ell=\log_2 m$, and $m=4^t$ is a power of four.

**Theorem 1** [@OpenAI2026, Theorem 1.1]**.** $\alpha_{\rm tot}=4$. More precisely, for each integer $k\ge2$ there are constants $c_k,C_k>0$ and $b_k$ and, for all sufficiently large powers of four $m$, explicitly specified total functions $F_{k,m}$ with
$$
Q(F_{k,m})\le C_k\sqrt m\,\ell^{b_k}
\qquad\text{and}\qquad
R(F_{k,m})\ge c_k\,\frac{m^{2-1/k}}{\ell^{2}}.
\tag*{(2)\quad\textsf{P2}}
$$

Displays that match a display of the preprint carry its number after the letter P. The upper bound $R(f)\le D(f)=O(Q(f)^4)$ for total $f$ is due to Aaronson, Ben-David, Kothari, Rao and Tal [@ABKRT2021, Theorem 2], through Huang's sensitivity theorem [@Huang2019]. Already $k=3$ gives $4-2/k=10/3>3$, which refutes their Conjecture 2, $R(f)=O(Q(f)^3)$. Theorem 1 therefore settles the optimal polynomial relation between the two measures for total functions: the quartic bound cannot be improved by any power.

The proofs below give $b_k=6$ (§4.3), $c_k=1/400$ (§5.5) and the threshold $t\ge13669\,k^2$ (§6), with one circuit $\mathcal C$ serving both bounds; the counting is in the reasoning record [@Record2026], [§5.4](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-explicit-log6), [§6.6](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-floors), [§3.15](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#forr_threshold). The theorem, the construction and both of its analyses are OpenAI's [@OpenAI2026]. In the Lean formalisation the [compared form of Theorem 1][thm-headline] has an existential logarithmic exponent and the lower bound $\lfloor mL/100\rfloor<R(F_{k,m})$ of (15) below, for the same circuit; the explicit constants $6$ and $1/400$ are proved by a [separate theorem][src-constants] that is built but has not been compared.

### 1.1 The history

| Exponent $a$ with $R=Q^{a}$ (total $f$) | Source |
|---|---|
| $2$ | OR: Grover search and its matching lower bound |
| $5/2$, up to logarithms | cheat sheets with Forrelation [@ABK2016] |
| $8/3-o(1)$ | Tal [@Tal2020] |
| $3-o(1)$ | Bansal and Sinha [@BansalSinha2021]; independently Sherstov, Storozhenko and Wu [@SSW2023] |
| $4-o(1)$ | OpenAI [@OpenAI2026] |
| upper bound $4$ | $D=O(Q^4)$ [@ABKRT2021], via [@Huang2019] |

The cheat-sheet arithmetic shows why this route stopped at the cube. In [@ABK2016, §3.1] a partial function $g$ on $n$ bits is composed with $h=\mathrm{AND}_{m'}\circ\mathrm{OR}_{m'}$, which has $R(h)=\Omega(m'^2)$, $Q(h)=O(m')$ and certificates of size $m'$. Computing $g\circ h$ and Grover-checking a certificate of size $\widetilde O(nm')$ costs $\widetilde O(m'+\sqrt{nm'})$ quantum queries, against $\widetilde\Omega(R(g)\,m'^2)$ classical ones. With Forrelation, $R(g)=\widetilde\Omega(\sqrt n)$ and $m'=n$ give $5/2$. An optimal partial separation, $R(g)=\widetilde\Omega(n)$ with $Q(g)$ polylogarithmic, gives $n^3$ against $n$, the cubic separation ABK anticipated "in a completely black-box manner". Improved partial separations then gave $8/3-o(1)$ and $3-o(1)$ in this framework, and ABKRT conjectured that three is the truth for all total functions.

### 1.2 The key mechanism

The input has $m$ columns. Column $i$ holds a string $X_i\in\{0,1\}^m$, $r=20\ell$ inputs $A_{i,1},\dots,A_{i,r}$ to a Forrelation partial function $P=P_{k,m}$, and a separate cell $B_{i,s}$ for every address $s\in\{0,1\}^r$ (Figure 1). The answers $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ select one cell, which should certify $s_i$ and point to a zero in every other column. The function asks whether some all-one column has such a cell.

![Column $i^\star$ is the winner: $X_{i^\star}$ is all ones, and the cell selected by the answers to its $r$ Forrelation instances points to a zero in every other column. No pointer from any other column can find a zero in $X_{i^\star}$, whatever address that column computes.](figures/expert_column.svg){width=90%}

*Classically*, a zero-input with one zero per column and a one-input that erases one random column's zero and fills its selected cell differ only there (§5). Searching the $X$-strings for the erased zero needs about $m^2$ queries. Reading the cell needs that column's address, about $L\approx R(P)\approx m^{1-1/k}$ queries in the column, or a lucky guess of $r$ bits; since the column is unknown, this route needs about $L$ queries in a constant fraction of the columns. As $L\le m$, both routes fail below about $mL$ queries, so
$$
R\approx m\cdot L\approx m^{2-1/k}.
$$
*Quantumly*, each address costs only polylogarithmically many queries, and the search over $m$ columns costs about $\sqrt m$, so $Q\approx\sqrt m$ up to logarithms, and
$$
R\approx m^{2-1/k}=\bigl(\sqrt m\bigr)^{4-2/k}\approx Q^{4-2/k}.
$$

The difficulty is the quantum search: Grover search for "column $i$ wins" would check about $m$ local tests per column and cost about $m$ in all. The outward pointers give a cheap substitute. Two columns can be compared in polylogarithmically many queries by decoding both addresses and following each one's pointer into the other. A genuine winner $i^\star$ wins every comparison with high probability: its pointer finds a zero in the rival, and nothing can point to a zero in $X_{i^\star}$. That holds whatever the rival's address inputs are, including inputs outside the promise of $P$. Comparisons between losers can be cyclic, unbiased or arbitrary, and a tournament with fractional weights tolerates exactly this (§4.2).

### 1.3 What is new

Addressing a certificate by partial-function answers comes from the cheat sheets [@ABK2016]; here each of $m$ columns has its own array, so a classical algorithm pays for an address in about $m$ columns while a quantum algorithm searches them in about $\sqrt m$ steps. The winning condition descends from the pointer functions of Göös, Pitassi and Watson [@GPW2018], developed by Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs [@ABBLSS2017], whose functions already separate deterministic from quantum query complexity with a nearly quartic power. GPW reach the zeros by a chain of pointers and Ambainis et al. by a balanced tree; Ambainis et al. set direct pointers aside because one symbol holding all $m-1$ pointers makes the alphabet exponential [@ABBLSS2017, §1.3]. Here each pointer is a separate $\ell$-bit field, read in $\ell+1$ bit queries, and these direct pointers are combined with cheat-sheet addressing.

The partial function is Aaronson and Ambainis's $k$-fold Forrelation [@AA2018]. Bansal and Sinha proved hardness of its explicit Walsh–Hadamard form, with the one-sided thresholds used here [@BansalSinha2021]; Sherstov, Storozhenko and Wu independently proved the optimal partial separation for $k$-fold rorrelation with a uniformly random orthogonal matrix [@SSW2023, Theorem 1.1].

Comparison search has close antecedents: quantum minimum finding [@DH1996] over totally ordered values, and king finding [@MPS2023] in a fixed tournament. Ben-David and Kothari [@BDK2026, Lemma 5] resolve each edge of a fixed tournament of candidate claims by exact local checks, find a sink or king and verify it, and Ambainis, Iraids and Kokainis [@AIK2026, §6.1] keep the candidates that beat every pivot selected so far in a fixed graph whose edges are computed approximately; both separate certificate complexity $C$ from $R$ and $Q$. In each, a comparison has a fixed intended outcome. Quantum search with bounded-error inputs [@HMW2003] does not apply directly either: it needs every comparison to compute a fixed predicate with bounded error, and here a comparison between two losing columns can have any probability, including exactly $1/2$. The new ingredient on the quantum side is a tournament that needs only the winner's one-sided guarantee (§4.2).

### 1.4 Plan

Section 2 defines the Forrelation promise and the total function, and Section 3 lists natural shortcuts that fail, each with a counterexample. Section 4 proves the quantum upper bound: bounded amplification, comparisons, the fractional-weight tournament and verification. Section 5 proves the randomized lower bound: a direct product with separate caps, the planted pair, the erased zero and the capped simulator. Section 6 states the Forrelation lower bound in the uniform form proved in Lean, and Section 7 deduces $\alpha_{\rm tot}=4$. Appendix A is a reading guide to the Lean statement of Theorem 1 and says, for each linked Lean result, whether it states the same as the paper, more, or less.

## 2. The construction

This section defines the partial function $P$ and the total function $F_{k,m}$, and records the local tests that both algorithms use.

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
$F_{k,m}=1$ exactly when some column wins. This is a total function: no promise is imposed on the address inputs, pointers or transcripts. There is at most one winner, since a winner's pointer into a second all-one column would find a zero there. In all, $F_{k,m}$ has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]=O_k(m^{22}\ell^3)$ input bits, since $2^r=m^{20}$; the parameter $m$ counts columns, and both bounds concern this one function.

**Local tests** [@OpenAI2026, Lemma 2.2]. For a fixed pair $(i,s)$, "$i$ wins and $s=s_i$" is the conjunction of
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3)
$$
tests: $m$ tests $X_i[y]=1$, $m-1$ pointer tests, one consistency test per gate of each transcript, and two output tests per transcript (domain bit $1$, value bit $s_h$). Induction in topological order shows that a gate-consistent transcript is the true evaluation, so the output tests say exactly that $P(A_{i,h})$ is defined and equals $s_h$. A gate test makes at most three queries and a pointer test $\ell+1$ adaptive queries. Every test can be evaluated coherently, with its index in superposition, at a constant-factor overhead in queries. Hence a winner passes all tests at its address, and a non-winning column fails some test at every address.

## 3. Where a natural shortcut fails

Each row of Table 1 is a step a reader may be tempted to simplify, with an instance showing that the simplification is false. Rows 3, 5 and 8 are checked in the table; the other rows link to the record passage that checks them. The right column also names the section that uses the correct argument.

: Natural shortcuts and their counterexamples. Here $\beta$ is the best one-instance success within the cap.

| Shortcut | Counterexample | Used in; checked in |
|:-----------------------|:-------------------------------------------------|:-----------|
| Decide the promise from the projection statistic $\Phi^2$ | $k=2$, $m=4$, $z_1=z_2=(-1,1,1,1)$: $\Phi=-1$, so $\Phi^2=1$, yet $z$ is outside the promise | §2 (iii); [record §3.5](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#forr_small_instance) |
| Treat comparisons as a total order, or as bounded-error queries to a fixed tournament | A deterministic three-cycle of losers is a fixed tournament with no total order; two losers each winning with probability $1/2$ have no bounded-error orientation | §4.2; [record §5.2](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-cyclic-example) |
| Output a column that wins every comparison | All-one column $1$ with a correct certificate except one pointer, into column $j>1$, reaching a one: column $1$ wins every comparison by the tie-break, yet no column wins | §4.3 |
| Choose the planted column with a uniform marginal law | Query row $1$ of four columns; choose $I$ uniformly among columns with a found zero, or among all four if none: $I$ is uniform, yet its zero is found with probability $175/256>\mathbb EZ/m=1/4$ | §5.3; [record §6.4](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-selection-independence-example) |
| Cap the address queries in expectation | Two-bit parity, $\beta=1/2$: a fair coin either computes both instances or guesses both; expected cost one each, success $5/8>\beta^2$ | §5.1 |
| Side information independent of each input separately | $P(x)=x$ on one fair bit, cap $0$, inputs $X,Y$: given $S=X\oplus Y$, answering $(0,S)$ succeeds with probability $1/2>1/4$ | §5.1; [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-independent-information) |
| Condition on the caps being respected | AND on two uniform bits, $\beta=3/4$, two instances: success with the caps has probability $5/16\le\beta^2$, success given the caps $5/8>\beta^2$ | §5.4; [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-adaptive-example) |
| Let $k$ grow inside a fixed-$k$ threshold | "$t\ge2^k$" holds eventually for every fixed $k$ and fails for every $t$ when $k=t$ | §7 |

The conditioning example in row 7 is the algorithm that queries bit $A_0$ of the first instance, then bit $B_{A_0}$ of the second, queries $A_0$ again if the two answers differ, and outputs $(0,0)$. Of the sixteen equally likely inputs, eight respect both caps and five of those are answered correctly.

## 4. The quantum upper bound

This section proves the upper bound in (2) with a fixed-cap amplifier, a comparison of two columns, a tournament that lists $O(\log m)$ candidates, and verification of each candidate.

Put $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$.

**Lemma 2** (bounded amplification [@OpenAI2026, Lemma 3.1])**.** Let $\mathcal A$ be a state preparation with a success flag, success probability $p$, and normalised successful state $|g\rangle$ when $p>0$. For $0<\gamma\le1/2$ and $0<\eta<1/2$ there is a procedure making $O(\gamma^{-1/2}\log(1/\eta))$ calls to $\mathcal A$ and $\mathcal A^{-1}$ on every branch, for every $p$, that either reports failure or returns a success; conditional on success its output state is $|g\rangle$ up to a global phase. It fails with probability at most $\eta$ if $p\ge\gamma$, and always if $p=0$.

*Sketch.* Write $\mathcal A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle$. After $j$ Grover iterations the successful component is $\sin((2j+1)\theta)|g\rangle$ [@BHMT2002, §2, Lemma 1], so every successful measurement leaves the same normalised state. A trial with $j$ chosen at random below $M=\lceil10/\sqrt\gamma\rceil$ succeeds with constant probability whenever $p\ge\gamma$ [@BBHT1998, §4, Lemma 2]. A fixed number of fresh trials, stopping at the first success, gives the cap and the failure bound, and leaves the conditional state unchanged ([record §5.1](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-amplification-statement)). Search with an unknown success probability bounds its cost only in expectation [@BHMT2002, Theorem 3].

The upper bound below uses only the law of the measured label. Lean proves this label law and also the full form of the lemma, with the original register returned in the normalised successful state; Appendix A compares both with Lemma 2.

### 4.1 Comparisons

To decode column $i$, run the algorithm of §2 (ii) on each $A_{i,h}$ with error $\varepsilon/r$, at cost $O_k(r\log(r/\varepsilon))$. If all $r$ instances are promised, the decoded address is $s_i$ with probability at least $1-\varepsilon$; otherwise some address is returned within the same cap. For an unordered pair $\{i,j\}$, sort the indices and run one fixed circuit: decode both columns, read each column's pointer into the other at its decoded address, and inspect the bit it names. A column disqualifies the other if that bit is $0$. If exactly one column disqualifies the other, it is the victor; otherwise the smaller index is. A self-comparison is a loss. Let $a_{ij}$ be the probability that $i$ defeats $j$. Because both orders use the same circuit,
$$
a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0.
\tag*{(7)\quad\textsf{P10}}
$$
If $i^\star$ wins, no pointer finds a zero in $X_{i^\star}=1^m$, and whenever $i^\star$ is decoded correctly its pointer finds a zero in the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every $j\ne i^\star$, whatever the rival's address inputs. The decoded labels stay in orthogonal registers, so these probabilities are the measured probabilities of the coherent circuit. One comparison costs $c=O_k(\ell\log\ell)$ queries.

### 4.2 A tournament with probabilistic comparisons

**Proposition 3** [@OpenAI2026, Proposition 3.2]**.** Let a comparison circuit, coherently controlled by two candidate indices, reversible with all its workspace retained and making at most $c$ queries on every input, report $i$ defeating $j$ with probabilities satisfying (7). A quantum algorithm with $O(c\sqrt m\,T^2\log T)$ queries on every branch returns at most $T$ candidates, and if some $i^\star$ has $a_{i^\star j}\ge1-\varepsilon$ for all $j\ne i^\star$, the list contains $i^\star$ with probability at least $1-2m2^{-T}-T\varepsilon$. Probabilities are over measurements, for a fixed input.

*Ideal process.* Start with weights $w_i=1$ and $W=\sum_iw_i$. For at most $T$ steps, and only while $W>0$, draw a pivot $\rho$ with probability $w_\rho/W$, append it to the list, and update $w_i\leftarrow w_i\,a_{i\rho}$. By (7), pairing the terms $(i,\rho)$ and $(\rho,i)$,
$$
\mathbb E[W_{\rm new}\mid w]=\frac1W\sum_{\rho,i}w_\rho w_i a_{i\rho}=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\tag*{(8)\quad\textsf{P13}}
$$
No order or transitivity enters, so cycles among losers do no harm. After $T$ steps $\mathbb EW\le m2^{-T}$. Until $i^\star$ is drawn its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$, so by Markov's inequality $i^\star$ is missing from the ideal list with probability at most $2m2^{-T}$.

*Exact sampling.* The algorithm never computes the weights. Given pivots $\rho_1,\dots,\rho_n$ with $n<T$, it prepares
$$
\frac1{\sqrt m}\sum_{i=1}^m|i\rangle\bigotimes_{b=1}^{n}|\phi(i,\rho_b)\rangle,
\tag*{(9)\quad\textsf{P15}}
$$
where $|\phi(i,\rho_b)\rangle$ is the full comparison state in a fresh workspace, and flags success when every comparison says that $i$ wins. For the fixed input and history, the tensor product gives success-and-label mass $m^{-1}\prod_ba_{i\rho_b}=w_i/m$, so the total success probability is $W/m$ and the label law conditional on success is exactly $w_i/W$. Apply Lemma 2 with $\gamma=1/(2m)$ and $\eta=\varepsilon$; on reported failure, stop and return the list ([record §5.2](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-quantum-tournament)).

*Coupling.* Until $i^\star$ is drawn, $W/m\ge1/(2m)$, so at every such history the stage fails with probability at most $\varepsilon$ and otherwise draws a pivot with exactly the ideal law. Coupling stage by stage, conditional on the entire past (the failure probabilities may depend on the history), adds at most $T\varepsilon$ to the miss probability, and a failure after $i^\star$ is listed does not remove it ([record §5.2](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-coupling)). Stage $n$ costs $O(c(n+1)\sqrt m\log(1/\varepsilon))$ queries whether or not a dominant candidate exists. Summing over $n<T$ proves the proposition. Full proof: [record §5.2](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-comparison-model).

### 4.3 Verification and the query count

Even a column that beats every rival with probability at least $1-\varepsilon$ need not win (row 3 of Table 1), so each listed candidate is verified. Decode its address afresh and measure it. At the measured address, a uniformly random one of the $K$ local tests fails with probability $0$ if all pass and at least $1/K$ otherwise; Lemma 2 with $\gamma=1/K$ and $\eta=\varepsilon$ searches for a failing test in $O(\sqrt K\,\ell\log(1/\varepsilon))$ queries. Reject the candidate if a failing test is found, and accept it otherwise. A non-winner fails some test at every address (§2), including addresses decoded from unpromised instances, so it is accepted with probability at most $\varepsilon$; a winner is accepted whenever its address is decoded correctly. Accept the input if some candidate is accepted. The error is at most $T\varepsilon$ on zero-inputs and at most $2m2^{-T}+T\varepsilon+\varepsilon<1/3$ on one-inputs. Pointers are read bit by bit and array indices are computed reversibly; a controlled query costs two ordinary queries. No unit-cost pointer oracle is assumed.

The exponent six in (2) comes from a deliberately loose count ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-finite-budget)), with $\log(1/\varepsilon)\le1/\varepsilon=O(\ell)$. A comparison costs $O_k(\ell^3)$; a tournament stage, padded to $T$ comparisons per call, uses $O(\ell)$ trials of $O(\sqrt m)$ iterations, so the $T$ stages cost $O_k(\sqrt m\,\ell^6)$. A verification costs a fresh decoder, $O_k(\ell^3)$, plus $O(\ell)$ trials of $O(\sqrt K)=O_k(\sqrt m\,\ell^{3/2})$ iterations of $O(\ell)$ queries, so the $T$ verifications cost $O_k(\sqrt m\,\ell^5)$ and the total is $O_k(\sqrt m\,\ell^6)$ ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#upper-explicit-log6)). Nothing below depends on the logarithmic exponent.

## 5. The randomized lower bound

A planted one-input (§5.2) differs from a zero-input only at an erased zero and a filled cell; §5.3 bounds the chance of finding the first, and §5.4, through a direct product (§5.1), the second. The lower bound applies to any partial function $P$ with an exact circuit as in §2 (iii) and any integer $L$ with $1\le L\le m$ and $L<R(P)$. By finite minimax [@Yao1977] there is a law $\mu$ on the domain of $P$ under which every deterministic tree of depth at most $L$ succeeds with probability at most $\beta=2/3$; the maximum over randomized depth-$L$ algorithms is attained, and it is below $2/3$ because $L<R(P)$.

### 5.1 A direct product with separate caps

**Lemma 4** [@OpenAI2026, Lemma 4.1]**.** Let $U_1,\dots,U_r$ be independent with law $\mu$. An algorithm that makes at most $L$ queries to each $U_h$ on every branch, interleaving them adaptively, outputs $(P(U_1),\dots,P(U_r))$ with probability at most $\beta^r$. Its random coins and any side information are allowed if they are jointly independent of $(U_1,\dots,U_r)$.

*Proof.* For a nonnegative measure $\nu$ on the domain of $P$, let $V_d(\nu)$ be the largest $\nu$-weight of inputs on which a depth-$d$ tree answers correctly. Then $V_0(\nu)=\max_b\nu(P=b)$ and
$$
V_{d+1}(\nu)=\max\Bigl\{V_d(\nu),\ \max_y\bigl[V_d(\nu_{y,0})+V_d(\nu_{y,1})\bigr]\Bigr\},
$$
where $\nu_{y,b}$ is the restriction of $\nu$ to inputs with bit $y$ equal to $b$. For product measures $\nu_1\otimes\dots\otimes\nu_r$ and remaining budgets $L_1,\dots,L_r$, induction on a deterministic vector-output tree shows that its weight of fully correct inputs is at most $\prod_hV_{L_h}(\nu_h)$. At a leaf the correct weight factorises. A query to input $h$ restricts only $\nu_h$ and lowers only $L_h$, and its two branches are absorbed by the recursion; zero-weight branches need no division. Initially every factor is at most $\beta$. Fix the coins and side information, apply this bound, and average. $\square$

The caps must hold on every branch and the independence must be joint (rows 5 and 6 of Table 1). Per-path allowances go back to Shaltiel's fair trees, for XOR advantage under uniform inputs [@Shaltiel2003]; Drucker's Lemmas 3.1–3.2, specialised at the end of his §3, give this product bound, while his headline theorem assumes one global budget [@Drucker2012] ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-literature-and-verification)). Lean proves a joint form of Lemma 4 for finitely many weighted seeds, compared in its own statement (Appendix A). Arbitrary independent coins and side information reduce to finitely many seeds, since a capped algorithm has finitely many deterministic behaviours; that reduction is an ordinary argument ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-independent-information)).

### 5.2 Planting a winner

Let $G=\lfloor mL/100\rfloor$. The **dummy input** $Y^{(0)}$ chooses rows $J_1,\dots,J_m\in[m]$ uniformly, puts a single zero at $X_i[J_i]$, draws every $A_{i,h}$ from $\mu$, all mutually independent, and leaves every cell blank. It has no winner. Choose $I\in[m]$ uniformly and independently of all of $Y^{(0)}$. The **planted input** $Y^{(1)}$ erases the zero of column $I$ and fills only the cell $B_{I,s_I}$ with the true transcripts and the pointers $p_{I,s_I,j}=J_j$; column $I$ wins (Figure 2). The blank array and the single filled cell follow the cheat-sheet lower bound of Aaronson, Ben-David and Kothari [@ABK2016]; the erased zero is a second channel, and the unknown column $I$ supplies the factor $m$.

![The two coupled inputs. They differ only at the erased zero $X_I[J_I]$ and inside the cell $B_{I,s_I}$; the address inputs, drawn from $\mu$, are the same in both.](figures/expert_planted.svg){width=80%}

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
This identity uses that $I$ is independent of the whole dummy run; a uniform marginal law is not enough (row 4 of Table 1). Lean proves (11) together with the bound $4G/m^2$ as a [compared statement][cmp-eq11], for [independent address inputs, zero rows and $I$][def-hit] ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-erased-zero-identity)).

To bound $\mathbb EZ$, count early and late discoveries, as the preprint does. A query to $X_i$ made while fewer than $m/2$ rows of $X_i$ have been queried finds the zero with probability at most $2/m$ given the past, since $J_i$ is uniform on the unqueried rows; these early discoveries number at most $2G/m$ in expectation. Any other discovery lies in a column that receives at least $m/2$ queries, and there are at most $2G/m$ such columns. Hence
$$
\mathbb EZ\le\frac{4G}m,\qquad
\Pr[\mathcal T\text{ queries }X_I[J_I]]\le\frac{4G}{m^2}.
$$
A reference-input count sharpens this to $2G/(m(m+1))$ ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-zero-optional)); the constants below do not need it.

### 5.4 The planted cell

Let $\lambda_i$ be the number of queries, counting repetitions, that the run on $Y^{(0)}$ makes to $A_{i,1},\dots,A_{i,r}$, and call column $i$ heavy if $\lambda_i>L$. At most $G/L$ columns are heavy, so $\Pr[I\text{ heavy}]\le G/(mL)$.

Fix a column $i$ and a time $\tau\in\{1,\dots,G\}$. A simulator receives as free information all of $Y^{(0)}$ outside $A_{i,1},\dots,A_{i,r}$, which is jointly independent of those $r$ inputs and does not reveal $s_i$. It runs $\mathcal T$, answering other queries from the free information and querying the $A_{i,h}$ itself, and aborts before an $(L+1)$-st query to them in total. If it reaches time $\tau$ and the $\tau$-th query lies in a cell $B_{i,s}$, it outputs $s$; otherwise it outputs a fixed vector. Its total cap on the $A_{i,h}$ is $L$, so Lemma 4 applies. If $i$ is not heavy and the $\tau$-th query of the original run lies in $B_{i,s_i}$, the simulator has not aborted and outputs $s_i$. Therefore
$$
\Pr\bigl[\,i\text{ is not heavy and the }\tau\text{-th query lies in }B_{i,s_i}\bigr]\le\beta^r .
\tag*{(12)\quad\textsf{P21}}
$$
This bounds a joint event under the original law. Conditioning on the cheap event "$i$ is not heavy" would change the law of the address inputs and can make the conditional success exceed $\beta^r$ (row 7 of Table 1). A union bound over the $G$ times, an average over the independent $I$, and the heavy columns give
$$
\Pr[\mathcal T\text{ queries }B_{I,s_I}]\le\frac G{mL}+G\beta^r
\tag*{(13)\quad\textsf{P22}}
$$
([record §6.5](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-simulator)).

### 5.5 The contradiction and the constants

By (10), (11) and (13), with $G\le mL/100\le m^2/100$ and $\beta^r=(2/3)^{20\ell}\le m^{-10}$,
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|\le\frac{4G}{m^2}+\frac G{mL}+G\beta^r\le\frac6{100}.
\tag*{(14)\quad\textsf{P23}}
$$
A randomized algorithm of worst-case cost $G$ is an average of such trees, so it satisfies (14) as well, whereas error at most $1/3$ on the zero-input $Y^{(0)}$ and the one-input $Y^{(1)}$ would force a gap of at least $1/3$. Hence, for every $P$ and $L$ as above,
$$
R(F_{k,m})>\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor.
\tag*{(15)\quad\textsf{P17}}
$$
For the constant in (2), take $k\ge2$ and $t\ge8$. Then $4t^2\le2^t\le m^{1-1/k}$, so $x=m^{1-1/k}/\ell^2\ge1$ and $L=\lfloor x\rfloor\ge x/2$; also $mL\ge200$, so $\lfloor mL/100\rfloor\ge mL/200\ge m^{2-1/k}/(400\ell^2)$. Section 6 gives $L<R(P_{k,m})$ for $t\ge13669k^2$. Full proof: [record §6](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-direct-product-statement), with this assembly in [record §6.6](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#CL-discrepancy).

## 6. The Forrelation lower bound

This section states the only property of $P$ that the lower bound uses and the stronger form in which Lean proves it. The construction needs only (5), the fixed-$k$, constant-error consequence of Bansal and Sinha's theorem [@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. The Lean formalisation proves (5) by a different route, in the following uniform form: for $m=4^t$ and $15k+2\le2t$,
$$
R(P_{k,m})>\frac{2}{18225}\,\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{16}
$$
For $t\ge13669k^2$ one has $15k+2\le2t$, $\ln(4km)\le6t$ and $8t^2>109350\,k^2t$, so (16) exceeds $m^{1-1/k}/\ell^2$ and implies (5).

The proof compares the uniform law with a planted law from Bansal and Sinha's rounded Gaussian chain and bounds a shallow tree's acceptance gap through derivatives of its multilinear extension, by a stopped-martingale induction in the style of Girish, Tal and Wu [@GTW2021]. The planted law is not supported on promised one-inputs. Because the promise is one-sided, a solver of cap $D$, amplified to small error and run as a tree of depth $50kD+1$, still separates the two laws by a constant multiple of $18^{-(k-1)}$, while the derivative bound forbids such a gap below the depth in (16). Full proof: [record §§3.6–3.15](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#forr_target), assembled in [§3.15](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#forr_uniform_assembly); [§3.16](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#forr_credit) compares it with the published proofs.

Lean proves (16) and the fixed-$k$ statement (5), which is compared; Appendix A gives their status. No person has yet reviewed this Lean proof.

## 7. The exponent

This section turns (2) into $\alpha_{\rm tot}=4$ and records the order of quantifiers.

Fix $0\le\alpha<4$ and choose an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $e=2-1/k-\alpha/2>0$. Keep $k$ fixed and let $m=4^t$ grow. For $t\ge13669k^2$, (2) with $b_k=6$ and $c_k=1/400$ gives $1+Q(F_{k,m})\le(1+C_k)\sqrt m\,\ell^6$ and
$$
\frac{R(F_{k,m})}{\bigl(1+Q(F_{k,m})\bigr)^\alpha}\ge\frac{1}{400(1+C_k)^\alpha}\,\frac{m^{e}}{\ell^{2+6\alpha}}\longrightarrow\infty,
$$
so no $C_\alpha$ in (1) exists. With the upper bound of [@ABKRT2021], $\alpha_{\rm tot}=4$. The order of quantifiers is: the exponent $\alpha$, then one fixed $k$, then its constants and threshold, then $m\to\infty$, with one circuit $\mathcal C$ serving both bounds in (2). For fixed $k$ this excludes exponents below $4-2/k$ only; it gives no separation of the form $R=\Omega(Q^4)$.

**Remark** (letting $k$ grow)**.** This needs control uniform in $k$ (row 8 of Table 1), which (16), (15) and the [explicit bound][src-budget-exponential] $Q(F_{k,m})\le2^{53}k\,2^{10k}\sqrt m\,\ell^6$ supply. If $15k+2\le2t$ and $t\ge32$, the right side $X$ of (16) lies in $[2,m]$, and $L=\lfloor X\rfloor$ in (15) gives $R(F_{k,m})>m^{2-1/k}/(1822500\,k^2\ln(4km))$. Taking $k=\lfloor\sqrt{t/20}\rfloor$, $t\ge80$, and comparing logarithms gives $R(F_t)\ge Q(F_t)^{4-\varepsilon(\ell)}$ for $F_t=F_{k,4^t}$, with $\varepsilon(\ell)=8\sqrt{10/\ell}+(56\log_2\ell+508)/\ell$; this still gives no bound $R=\Omega(Q^4)$. The deduction is ordinary; the quantum bound it uses is built in Lean but not compared.

## Appendix A. Checking the statement

A proof checker establishes that a proof proves its stated type. What remains is whether the formal statement says what Theorem 1 says. This appendix lists everything a reader must read to answer that question. The [statement file][statement-file] in the repository [@Repo2026] has 343 lines and imports only Mathlib. Its definitions follow in file order, each linked to its lines.

| Object | Meaning in the file |
|:------------------|:-------------------------------------------------------------------------|
| [Partial functions][def-partial], [totalisation][def-totalise] | A missing value marks an input outside the promise; totalising promises every input. |
| [Trees][def-tree], [randomized algorithms][def-randomized] | Depth charges repeats; a randomized algorithm is a finite mixture of trees with positive real weights. |
| [$R\le d$][def-RLe], [$R$][def-R] | Some mixture of depth at most $d$ succeeds with probability at least $2/3$ on every promised input; $R$ is the least $d$. |
| [Basis][def-basis], [oracle][def-oracle] | Basis $\lvert i,b,z\rangle$ with finite workspace $z$; the oracle is exactly $O_x$. |
| [Quantum algorithms][def-adaptive] | Unitaries fixed before the input, oracle calls, binary measurements of sets of basis states, classical branching. |
| [The query cap][def-querycap] | The most oracle calls on any branch, defined syntactically and so valid on every input. |
| [Output probability][def-output-mass] | Branch states stay unnormalised; an answer's probability is the total squared norm of the branches giving it. |
| [$Q\le c$][def-QLe], [$Q$][def-Q] | Constant on the promise, or a unit initial state and a program within the cap with output probability at least $2/3$ on every promised input. |
| [$N$][def-numerator], [$P$][def-P] | $N$ as a sum over Walsh paths; $P$ by the integer tests of §2 (iii). |
| [Circuits][def-circuit], [consistency][def-gate], [exactness][def-realises] | A gate-consistent transcript applies every gate to its inputs; the domain bit is $1$ exactly on the promise, and there the value bit is $P$. |
| [Bits][def-bitloc], [pointers][def-pointer], [winning][def-wins], [$F_{k,m}$][def-F] | Four kinds of input bit; an $\ell$-bit field read as a column; condition (6); $F_{k,m}=1$ when some column wins, $\ell=2t$, $r=40t$. |
| [$L$][def-L], [$G$][def-G] | $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$ and $G=\lfloor mL/100\rfloor$. |
| [Hardness][def-bansal-sinha], [power bound][def-universal], [$\alpha_{\rm tot}$][def-alpha] | Statement (5); membership in the set of (1); its infimum. |

The file also defines an unused [comparison predicate][def-comparison]. That these models agree with the usual ones, a capped program here having the output probabilities of a fixed query sequence with measurements deferred, is proved in [record §§2.2–2.5](https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/docs/reasoning_record.md#R3-01-BRIDGES).

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


**What Comparator establishes.** The statement file gives each theorem a placeholder in place of a proof; the [proofs][statement-solution] are in a separate solution file, and the two are compiled separately. For each theorem named in [the configuration][statement-config], the solution's declaration has the same type as the challenge's, built from the challenge's definitions, so a solution cannot redefine $R$, $Q$ or $F$. The proofs use only Lean's three standard axioms: propositional extensionality, soundness of quotients and choice. The [recorded run][statement-receipt] on the current sources used Comparator's paranoid mode, which also rechecks with the external kernels bundled with Lean. [Five deliberately wrong solutions][cmp-negative] (a changed definition, a foreign axiom, a missing declaration, an unfinished proof, a weakened conclusion) are rejected against the Tournament statement bundle, which is built the same way.

**How the linked Lean statements compare with the paper.** A formal proof can establish a nearby statement in place of the printed one. Table 2 says, for each central result linked above, whether its Lean statement is the same, stronger or partial, and what differs; "compared" means accepted by Comparator in its own configuration, "built" means compiled with the standard axioms only.

: Lean statements of the central results against the paper.

| Paper | Lean | Status | Relation and difference |
|:-----------|:--------------|:---------|:-------------------------------------------------------|
| (2) | [family theorem][thm-headline] | compared | Same, for some exact circuit realising $P$; existential exponent $b$; lower bound as $\lfloor mL/100\rfloor<R$, which gives the $1/400$ form once $t\ge8$ |
| $6$, $1/400$ | [constants theorem][src-constants] | built | Stronger: explicit constants for the named circuit |
| (5) | [hardness][thm-forrelation] | compared | Same, beyond an unspecified threshold; route of §6 |
| (16) | [uniform estimate][src-forrelation-uniform] | built | Same |
| Lemma 2.2 | [full statement][cmp-lemma22-full] | compared | Stronger: exact test count, physical cap $2(2t+1)$, essential pointer coordinates |
| Lemma 2 | [full form][cmp-amplifier] | compared | Stronger conclusion (the returned state); success must be a test on basis labels, and the routine reduction from a general projector is not formalised |
| Lemma 2 | [label law][src-amplify-measured] | built | Weaker: cap, failure bounds and the law of the measured label, not the state; the form Theorem 1 uses |
| Lemma 4 | [joint form][cmp-direct-product] | compared | Stronger in covering uncapped trees, bounding [success with compliance][def-compliant]; weaker in allowing only finitely many weighted seeds, and path compliance is not proved equal to the per-input caps |
| (11) | [identity and bound][cmp-eq11] | compared | Stronger: (11) with $\mathbb EZ/m\le4G/m^2$, any $m=2^\ell$, over [independent data][def-hit] |
| $\frac{2G}{m(m+1)}$ | [counting inequality][src-zero-successor] | built | Weaker: the charging inequality behind the refinement in §5.3; the averaging to a probability is ordinary |
| (12) | [per-time event][src-per-time] | built | Same |
| Winners | [four facts about winners][cmp-lemma22] | compared | Different statements, used beside Lemma 2.2: the unique-winner corollary, unique gate-consistent transcripts, and the two halves of winner dominance |
| Models | [zero costs][cmp-zero-cost], [degree][cmp-degree] | compared | Sanity checks: $D$, $R$, $Q$ vanish exactly on functions constant on the promise; the degree is that of the unique multilinear representation |

The relations come from the repository's recorded [statement reviews](https://github.com/wcook04/quartic-query-lean/blob/main/corpus/ties.json) and an [independent review of every cited statement](https://github.com/wcook04/quartic-query-lean/blob/main/research/adjudication/round5_statement_fidelity.md), both made without a person; they agree except on the four facts about winners, which this table follows the later review in classifying.

**What it does not establish.** Whether the definitions model the intended query models is what the reader is checking: both sides come from one specification, so a modelling error shared by both would pass. The recorded runs were local and unsandboxed. No person has reviewed the definitions or the Forrelation proof.

**Reproducing the check.** The first line gives the versions of the recorded runs and the commit the links point to. From `lean/`, the last command runs a [dependency printer][src-reach] that lists the closure the kernel checked; the recorded Comparator runs added `--inadvisably-no-sandbox`.

```
# commit 659b571, toolchain leanprover/lean4:v4.36.0-rc2, Mathlib 69552756cd8a
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
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52
[cmp-degree]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/Degree/Challenge.lean#L14-L20
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[cmp-eq11]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/Eq19/Challenge.lean#L19-L24
[cmp-lemma22]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Construction/Challenge.lean
[cmp-lemma22-full]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean#L14-L60
[cmp-negative]: https://github.com/wcook04/quartic-query-lean/tree/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Negative
[cmp-zero-cost]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/ModelZero/Challenge.lean#L11-L14
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L274-L285
[def-G]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L302-L303
[def-L]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L297-L300
[def-P]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L175-L182
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-QLe]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L133-L137
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-RLe]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L62-L65
[def-adaptive]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L101-L107
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-bansal-sinha]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L305-L309
[def-basis]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L84-L87
[def-bitloc]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L232-L238
[def-circuit]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L190-L199
[def-comparison]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L289-L293
[def-compliant]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L111-L120
[def-gate]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L208-L213
[def-hit]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/Eq19/Spec.lean#L65-L76
[def-numerator]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L160-L166
[def-oracle]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L89-L94
[def-output-mass]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L96-L126
[def-partial]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L18-L19
[def-pointer]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L249-L260
[def-querycap]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L109-L116
[def-randomized]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L46-L60
[def-realises]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L215-L221
[def-totalise]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L21-L22
[def-tree]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L33-L44
[def-universal]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L311-L315
[def-wins]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272
[src-amplify-measured]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/Upper/Amplify.lean#L345-L352
[src-budget-exponential]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/Upper/Bound.lean#L286-L290
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[src-forrelation-uniform]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532
[src-per-time]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/Paper/ClassicalPlanted.lean#L340-L348
[src-reach]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/scripts/Reach.lean
[src-zero-successor]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean#L17-L22
[statement-config]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/comparator.json
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-receipt]: https://github.com/wcook04/quartic-query-lean/blob/main/corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
