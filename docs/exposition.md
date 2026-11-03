---
title: "Why the exponent is four"
subtitle: "An examples-first account of the nearly quartic separation between randomized and quantum query complexity"
author: "Will Cook"
date: "November 2026"
bibliography: exposition.bib
link-citations: true
---

# Overview

A query algorithm reads the bits of an input $x\in\{0,1\}^n$ one at a time; computation between queries is free. A quantum query applies the oracle $O_x|j,b,w\rangle=|j,b\oplus x_j,w\rangle$ to a superposition of positions $j$, answer bits $b$ and workspace $w$. For a Boolean function $f$, $R(f)$ and $Q(f)$ are the least numbers of queries with which a randomized or quantum algorithm computes $f$ with error at most $1/3$ on every input. The query count is a worst case over inputs and over every random choice or measurement outcome.

For a **total** function, defined on every input, the two measures are polynomially related, and the question is the best power. Define $\alpha_{\rm tot}$ as the infimum of the $\alpha\ge0$ for which some constant $C_\alpha$ gives $R(f)\le C_\alpha(1+Q(f))^\alpha$ for every total Boolean function on every number of bits.

**Theorem** [@OpenAI2026, Theorem 1.1]. $\alpha_{\rm tot}=4$. For each fixed integer $k\ge2$ there are total functions $F_{k,m}$, for all sufficiently large powers of four $m$, with
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
\qquad
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2}.
$$
The preprint leaves the constants and the power of the logarithm unspecified; the explicit $6$ and $1/400$ come from the counts in Sections 4 and 6.

The upper bound $R(f)=O(Q(f)^4)$ was already known [@ABKRT2020, Theorem 2]. The new part is the family, which refutes the conjecture of the same authors that $R(f)=O(Q(f)^3)$ [@ABKRT2020, Conjecture 2].

**Who this is for, and where it goes.** This account is for a graduate student who knows the query models above and wants to see how such a separation is built and proved. The result settles how much quantum algorithms can gain over randomized ones on total functions, left open in 2020 between the proved quartic bound and the conjectured cubic one: the gain is the largest the upper bound allows. By the end the reader should be able to build the function on a four-column board, run the quantum tournament on it by hand, and rederive the classical bound with its constants. Three payoffs mark the route: one line of arithmetic that explains the exponent four (below); a tournament in which a column can beat every rival and still lose, and losers beat each other in a cycle, yet a weighted sampler finds the true winner (Section 4); and a planted pair of inputs, differing at one erased zero and one filled cell, that makes a classical algorithm pay for an address in almost every column (Section 5). Sections 1–3 build the objects, Section 6 assembles the exponent, and Section 7 says what the Lean proof checks.

**The reason for four, in one line.** The input has $m$ columns, and a hidden certificate sits in one of them:
$$
Q\approx\sqrt m,\qquad R\approx m\cdot L\ \text{ with }\ L\approx m^{1-1/k},\qquad\text{so}\qquad R\approx m^{2-1/k}=(\sqrt m)^{4-2/k}\approx Q^{4-2/k}.
$$
The quantum algorithm finds the right column by a search over $m$ columns in which each step costs only polylogarithmically many queries. A classical algorithm must be prepared to find the certificate in any of the $m$ columns, and locating it inside one column means naming an address, which costs $L$ queries there. Here $L$ is the classical cost of the partial function $k$-fold Forrelation, which is nearly linear in its input size of about $m$ bits. The polylogarithmic factors have been dropped from this display.

The exponent $4-2/k$ is below four for every $k$, so the quantifiers come in a fixed order: given $\alpha<4$, choose one $k>2/(4-\alpha)$, keep it fixed and let $m$ grow, so that $R/(1+Q)^\alpha\to\infty$. Every constant depends on $k$, which therefore never grows with $m$ (Section 6).

**Where this sits.** Pointer functions of Göös, Pitassi and Watson, developed by Ambainis and coauthors, gave a nearly quartic separation between deterministic and quantum query complexity [@GPW2018; @ABBLSS2017]. For bounded-error randomized complexity, Aaronson, Ben-David and Kothari introduced cheat sheets and reached the power $5/2$ [@ABK2016]. They observed that their method gives a cubic separation in a black-box way from any partial function with randomized cost nearly linear in its input size and polylogarithmic quantum cost. Tal reached $8/3-o(1)$ [@Tal2020], and Bansal and Sinha, and independently Sherstov, Storozhenko and Wu, supplied such a partial function and reached $3-o(1)$ [@BansalSinha2021; @SSW2023]. The exponent here is $4-o(1)$, matching the upper bound.

The same arithmetic shows why the earlier route stops at three. The cheat-sheet function composes a partial function $g$ on $n$ bits with AND-OR on $n^2$ bits, giving $R\approx R(g)\cdot n^2$ and $Q\approx n$ [@ABK2016, §3.1]; as $R(g)\lesssim n\approx Q$, the partial function contributes one factor of $Q$ and the outer function two. In the construction below the partial-function inputs in each column have about $m$ bits while the quantum algorithm spends only about $\sqrt m$ queries in total, so $L\approx Q^2$, and the search over columns contributes another $m\approx Q^2$.

| Example | What it shows | § |
|:-----------------------------------|:------------------------------------------------------|:--|
| Three eight-bit inputs $a^+,a^0,a^-$ | the one-sided promise; a quantum test accepts an unpromised input | 1 |
| The four-column board (Figure 2) | addresses, transcripts, outward pointers, a winner | 2 |
| The board with a changed domain bit | why the circuit must certify the promise | 2 |
| The board with one pointer moved | a column can beat every rival and still not win | 4 |
| The board with cycled pointers (Figure 3) | losers can beat each other in a cycle; the weights still halve | 4 |
| The board as a planted pair (Figure 4) | the two places where the inputs differ | 5 |
| Discovered columns chosen dependently | a uniform marginal does not replace independence | 5 |
| Pooled budgets, parity side information, AND | each hypothesis of the direct product is needed | 5 |

Full proofs of every step are in the [long reasoning record](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md); a reference such as "record §6.5" below links to the passage in that section. The boxed proof in Section 5 can be skipped; the statement it proves stands outside the box.

# 1. Three eight-bit inputs

This section fixes the partial function at the smallest size, $k=2$ and $m=4$, where every value can be checked by hand. An input has two blocks of four bits. A bit $x$ stands for the sign $(-1)^x$, so $0$ means $+1$ and $1$ means $-1$. With coordinates ordered $00,01,10,11$, let
$$
W=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad
\Phi(z_1,z_2)=\frac{z_1^{\mathsf T}Wz_2}{8},\qquad
\delta=2^{-10}.
$$
The partial function $P=P_{2,4}$ is $1$ when $\Phi\ge\delta$, is $0$ when $|\Phi|\le\delta/2$, and is undefined otherwise. A large **negative** value of $\Phi$ is outside the promise.

Our three inputs are
$$
a^+=0111\,1000,\qquad a^0=0100\,1000,\qquad a^-=1000\,1000.
$$
All three share the second block $g=(-1,1,1,1)$, and $Wg=(2,-2,-2,-2)$. Their first blocks $(1,-1,-1,-1)$, $(1,-1,1,1)$ and $g$ give numerators $8$, $0$ and $-8$, so $\Phi(a^+)=1$, $\Phi(a^0)=0$ and $\Phi(a^-)=-1$. Thus $P(a^+)=1$, $P(a^0)=0$, and $a^-$ is unpromised.

Write $u=\tfrac12(1,1,1,1)$ and $H=W/2$, the Walsh transform scaled to preserve length. Then $\Phi=\langle z_1/2,\,Hz_2/2\rangle$ measures how closely the first sign pattern matches the Walsh transform of the second. Here $Hg/2=\tfrac12(1,-1,-1,-1)$: the first block of $a^+$ matches it exactly, that of $a^-$ with every sign reversed, and that of $a^0$ is orthogonal to it. The quantum algorithm for $P$ starts in $u$, applies the signs $z_2$ (one query), then $H$, then the signs $z_1$ (a second query), and projects back onto $u$; since $\Phi=u^{\mathsf T}D_{z_1}HD_{z_2}u$, the projection succeeds with probability $\Phi^2$. It succeeds with certainty on both $a^+$ and $a^-$. That is harmless for the partial function, which owes no answer on $a^-$. It will matter as soon as $P$ is placed inside a total function, because there every input needs an answer. This is the first distinction that must survive the whole argument: a cheap quantum test can accept an input that an exact certificate must reject.

Sorting all $256$ inputs by the parity of the second block gives $104$ one-inputs, $48$ zero-inputs and $104$ unpromised inputs ([record §3.5](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#forr_small_instance)). At this size the classical lower bound is empty, since $L_{2,4}=\lfloor 2/4\rfloor=0$; the example checks conventions only. What it gives is the one-sided promise and a quantum test that cannot tell $a^+$ from $a^-$, which the domain bit of Section 2 repairs.

# 2. One column, then four

This section builds the total function, first one column in general and then a four-column board used for the rest of the paper.

**One column.** Figure 1 shows the general layout. Fix $k\ge2$, let $m=4^t$ and $\ell=\log_2m$. There are $m$ columns. Column $i$ holds

- a string $X_i\in\{0,1\}^m$;
- $r$ inputs $A_{i,1},\dots,A_{i,r}$ to the partial function $P=P_{k,m}$, each of $km$ bits;
- an array of $2^r$ cells $B_{i,s}$, one for each $s\in\{0,1\}^r$.

When all of its $A_{i,h}$ are promised, column $i$ has the **address** $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$. A cell holds $r$ circuit transcripts, explained below, and one $\ell$-bit pointer $p_{i,s,j}$ into each other column $j$. Every bit is an ordinary input bit, and every assignment of bits is allowed.

![One column of $F_{k,m}$, drawn for a winning column $i^\star$. The answers to the $r$ address inputs select one of $2^r$ cells. In a winner, the cell at the true address certifies those answers and points to a zero in every other column; in any other column, the selected cell may hold anything.](figures/exposition/fig1_column.svg){width=94%}

Column $i$ **wins** at address $s$ when four conditions hold: $X_i$ is all ones; every $A_{i,h}$ is promised with $P(A_{i,h})=s_h$; every transcript in $B_{i,s}$ is correct; and every pointer $p_{i,s,j}$ reaches a zero of $X_j$. The total function is $F(y)=1$ exactly when some column wins at some address. At most one pair wins. Two different winning columns are impossible, because a pointer from the first would find a zero in the all-one string of the second. Within one column, the promised values fix the address.

Our addressing comes from Aaronson, Ben-David and Kothari's cheat sheets, which store a certificate at the address formed by the answers to independent partial-function instances; they used about $10\log n$ copies, and here $r=20\log_2m$ [@ABK2016, §3.1]. The all-one column whose certificate exhibits zeros elsewhere descends from the pointer functions [@GPW2018; @ABBLSS2017]. Göös, Pitassi and Watson reach those zeros through a chain of pointers; direct pointers to a zero in every other column are already discussed by Ambainis and coauthors [@ABBLSS2017]. What is new is the combination: an addressed cell array in every column, direct outward pointers in each cell, and the tournament of Section 4 that exploits them.

**Four columns.** Now take $m=4$, $k=2$ and, so that the cells can be listed, only $r=2$ address inputs per column, with two-bit pointers decoded as $00,01,10,11\mapsto$ positions $1,2,3,4$. Set
$$
(X_1,X_2,X_3,X_4)=(1111,\ 0111,\ 1011,\ 1101).
$$
Columns $1,3,4$ have address inputs $(a^+,a^0)$, so their address is $10$. Column $2$ has $(a^-,a^0)$ and no address. In every cell, a pointer into column $2$ names position $1$, into column $3$ position $2$, into column $4$ position $3$, and a pointer into column $1$ names the position encoded by the cell's own address. Every transcript is the true evaluation of a fixed $180$-gate circuit described below.

![The four-column board. Column 1 wins at address 10: its pointers reach $X_2[1]=X_3[2]=X_4[3]=0$. The dashed pointer from column 3's own true cell lands on a one, as every pointer into column 1 must.](figures/exposition/fig2_board.svg){width=92%}

Column $1$ wins at $10$ (Figure 2). Every other column has a zero in its own string and cannot win, so $F=1$. The board has $4(4+16+4(6+360))=5936$ bits.

**Transcripts.** Fix a circuit $C$ of fan-in two which outputs a domain bit $d$ and a value bit $b$: $(d,b)=(1,P(a))$ on promised inputs and $(0,0)$ otherwise. For $P_{2,4}$ there is an exact such circuit with $180$ gates, obtained by Shannon expansion of the truth tables; it gives $(1,1)$ on $a^+$, $(1,0)$ on $a^0$ and $(0,0)$ on $a^-$. Its gate list and a checker for every count on this board are linked from [record §4.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#AC-example-tests); everything else below can be checked by hand. A transcript proposes a value for every gate. It satisfies all gate equations exactly when it equals the true evaluation: by induction along the gate order, each gate's predecessors already agree with evaluation, so its own value is forced. This holds on every input, promised or not. So a winning cell certifies the promise through the domain bits and the address through the value bits.

**The domain bit is needed.** Change the board: set $X_1=0111$ and $X_2=1111$, and make every pointer into column $1$ name position $1$. Column $2$ is now all ones. At address $00$ its stored value bits $(0,0)$ agree with the address, its pointers find zeros in the other three columns, and every gate equation holds, because the transcripts are true evaluations. Its first domain bit is $0$, since $a^-$ is unpromised, so column $2$ does not win, and $F=0$. A function that checked only value bits would accept this board.

**Local tests.** Winning can be checked by small tests: $m$ tests of the column's own bits, $m-1$ pointer tests, $rS$ gate tests for a circuit of size $S$, and $2r$ tests that each domain bit is $1$ and each value bit equals $s_h$. Thus a candidate $(i,s)$ has
$$
K=2m-1+r(S+2)
$$
tests, each reading at most $\max(3,\ell+1)$ bits: a gate test reads one gate and two predecessors, and a pointer test reads $\ell$ pointer bits and then the one bit they select. All tests pass exactly when $(i,s)$ wins, so a nonwinner fails at least one test at every address. On the board $K=4+3+2(180+2)=371$. At $(1,10)$ all pass; at column $1$'s other three addresses the value tests fail; on the changed board, $(2,00)$ fails only its domain test. So a winner is unique and certified by $K$ small exact tests, and the domain tests are essential.

# 3. The general partial function

This section states the three facts about general $k$-fold Forrelation that the two bounds use. For general $k$ and $m=4^t$, index each of $k$ sign blocks by $\{0,1\}^{2t}$, let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=(1,\dots,1)/\sqrt m$, and let $D_z$ be the diagonal matrix of signs $z$. $k$-fold Forrelation [@AA2018] is
$$
\Phi(z_1,\dots,z_k)=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,\qquad \delta=2^{-5k},
$$
with $P_{k,m}$ defined by the thresholds $\delta$ and $\delta/2$ exactly as before [@BansalSinha2021]. Since $H$ and each $D_z$ preserve length, $|\Phi|\le1$. The construction needs three facts about $P_{k,m}$.

*A cheap quantum decoder.* Applying one sign diagonal costs one query by phase kickback, and the Walsh transforms cost none, so one projection experiment uses $k$ queries and succeeds with probability $\Phi^2$. On the promise this is at least $c=\delta^2$ or at most $c/4$. Repeating $\rho=\lceil16c^{-1}\ln(1/\eta)\rceil$ times and accepting when at least $\rho c/2$ trials succeed gives error at most $\eta$ with $O_k(\log(1/\eta))$ queries, by a Chernoff bound on the number of successes ([record §3.3](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#forr_repetition)); the cap holds on every input.

*An exact circuit.* Because $\Phi$ has two boundary factors and $k-1$ internal factors of $m^{-1/2}$, $\Phi=N/2^{t(k+1)}$ for an integer $N$, computed by $k-1$ integer Walsh transforms with entries of $O_k(\log m)$ bits. The promise becomes two integer comparisons, $p_1=[2^{5k}N\ge2^{t(k+1)}]$ and $p_0=[2^{5k+1}|N|\le2^{t(k+1)}]$, with output $(d,b)=(p_1\lor p_0,\,p_1)$. A fast Walsh transform and ripple-carry arithmetic give a fan-in-two circuit with $S\le200(k+1)^2m(\log_2m)^2$ gates ([record §3.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#forr_circuit_size)).

*Classical hardness.* For fixed $k$ and all sufficiently large $m$,
$$
R(P_{k,m})>L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor .
$$
This is the randomized lower bound of Bansal and Sinha for this one-sided promise [@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. Sherstov, Storozhenko and Wu independently obtained the optimal partial separation through rorrelation, a problem built from random orthogonal matrices [@SSW2023]. The record gives a separate derivation through rounded Gaussian chains and a decision-tree martingale ([record §§3.6–3.15](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#forr_target)).

With these, the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. The parameter $m$ counts columns. Both bounds below are about this one function on these large inputs, and both use the same circuit.

# 4. The quantum algorithm: a tournament

The quantum algorithm must find the winner, if there is one, among $m$ columns. A direct search does not suffice. Checking that one column wins means reading its $m$ string bits and $m-1$ pointers, which costs about $\sqrt m$ quantum queries; a Grover search over $m$ columns with that check inside costs about $\sqrt m\cdot\sqrt m=m$, and then $R\approx Q^{2-1/k}$ only. The algorithm instead compares columns two at a time, where each comparison costs polylogarithmically many queries, searches with comparisons, and runs the expensive check only on a short list.

**Comparing two columns.** Decode the $r$ address inputs of each column with error $\varepsilon/r$ each, so a promised column gets its true address with probability at least $1-\varepsilon$. Then follow each decoded cell's pointer into the other column and read the bit it names. A zero disqualifies that column. If exactly one is disqualified, the other wins the comparison; otherwise the smaller index wins. Both orders of a pair use the same procedure, so if $a_{ij}$ is the probability that $i$ beats $j$, then $a_{ij}+a_{ji}=1$ for $i\ne j$, and we set $a_{ii}=0$.

The comparison runs as a reversible circuit: the decoders' trials, counts and decoded labels stay unmeasured in workspace, the pointers are read at positions computed from those labels, and the outcome goes to a fresh bit. So it is a unitary whose inverse has the same query cost, and since distinct decoded labels sit in orthogonal registers, each outcome has the probability given by the classical rule averaged over decoded labels ([record §5.3](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-comparison-law)).

The outward pointers make comparisons against the winner reliable. The winner $i^\star$ has an all-one string, so no pointer from any rival, under any decoded label, finds a zero in it. When $i^\star$'s own address is decoded correctly, its true cell disqualifies the rival. So $a_{i^\star j}\ge1-\varepsilon$ for every rival $j\ne i^\star$, whatever the rival's address inputs are, including inputs outside the promise. Nothing is claimed about comparisons between two losers.

**Beating every rival is not winning.** On the board of Figure 2, change only $p_{1,10,2}$ from position $1$ to position $2$. It now reads $X_2[2]=1$, so column $1$ fails one pointer test and $F=0$. Yet column $1$ still beats every rival under every rival label: against column $2$ neither is disqualified and the index rule picks column $1$, and against columns $3$ and $4$ its pointers still find zeros. A column that dominates the comparisons is only a candidate, and the final verification is logically necessary.

**Losers can form a cycle.** Return to Figure 2 and change three pointers between losers, in every cell of their columns: column $2$'s pointer into column $4$ names position $1$, column $3$'s pointer into column $2$ names position $2$, and column $4$'s pointer into column $3$ names position $1$. Column $1$'s cells are untouched, so it still wins and $F=1$. Each loser's pointer into another loser is now the same in every cell, so the comparisons below do not depend on which labels the decoders return; this matters for column $2$, whose input $a^-$ has no true address. Column $2$ beats $3$, column $3$ beats $4$ and column $4$ beats $2$ (Figure 3). No ordering of the columns is consistent with the comparisons, so the search cannot sort them.

![Comparisons on the board with cycled loser pointers. An arrow $i\to j$ means that $i$ beats $j$; a dot in $p_{i,\cdot,j}$ means every cell of column $i$. The winner beats everyone; the three losers form a cycle.](figures/exposition/fig3_tournament.svg){width=42%}

Search by comparisons relates to quantum minimum finding [@DH1996], which assumes a total order, to king finding in tournaments [@MPS2023], which allows deterministic cycles, and to the comparison-based separations of certificate complexity [@BDK2026; @AIK2026]. Quantum search with bounded-error inputs [@HMW2003] needs every comparison to compute a fixed predicate with bounded error, but a comparison between two losers can have any probability, including exactly $1/2$; the tournament below uses the $a_{ij}$ themselves.

**An ideal process for the analysis.** The analysis compares the algorithm with a random process on weights. The weights are defined from the unknown probabilities $a_{ij}$; the algorithm never computes or estimates them. Start with $w_i=1$ for every column and an empty list, and write $|w|=\sum_iw_i$. While $|w|>0$, a stage chooses a pivot $p$ with probability $w_p/|w|$, appends it to the list, and multiplies each weight by its probability of beating the pivot: $w_i\leftarrow w_ia_{ip}$. The pivot's own weight becomes zero, since $a_{pp}=0$. Once $|w|=0$ the process is absorbed: the weights stay zero and nothing more is appended. On the cycled board, pivot $1$ lists the winner and absorbs the process:

| Pivot $p$ | New weights $(w_1,w_2,w_3,w_4)$ | New $|w|$ |
|---|---|---|
| $1$ | $(0,0,0,0)$ | $0$ |
| $2$ | $(1,0,0,1)$ | $2$ |
| $3$ | $(1,1,0,0)$ | $2$ |
| $4$ | $(1,0,1,0)$ | $2$ |

Each pivot has probability $1/4$, so the expected new total is $3/2$. In general, pairing the terms $w_iw_pa_{ip}$ and $w_pw_ia_{pi}$ and using $a_{ip}+a_{pi}=1$,
$$
\mathbb E\bigl[\,|w'|\;\big|\;w\bigr]=\frac1{|w|}\sum_{i,p}w_iw_pa_{ip}=\frac{|w|^2-\sum_iw_i^2}{2|w|}\le\frac{|w|}2,
$$
which here is $(16-4)/8=3/2$; at $|w|=0$ the inequality holds trivially. No transitivity and no margin away from $1/2$ is used. After $T$ stages $\mathbb E|w_T|\le m/2^T$. Meanwhile the winner's weight stays at least $(1-\varepsilon)^T\ge1-T\varepsilon$ until it is chosen. With
$$
T=\lceil\log_2(1000m)\rceil,\qquad\varepsilon=\frac{1}{1000T},
$$
the winner keeps weight above $1/2$, so the process cannot be absorbed before the winner is listed, and if the winner is missing after $T$ stages then $|w_T|>1/2$; by Markov's inequality this has probability at most $2m/2^T$. On the cycled board the winner is always chosen within three stages. If the winner wins only with probability $1-\varepsilon$, pivot $2$ leaves weights $(1-\varepsilon,0,0,1)$ and the next pivot is the winner with probability $(1-\varepsilon)/(2-\varepsilon)$ ([record §5.2](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-cyclic-example)).

**Sampling a pivot quantumly.** The algorithm realises the ideal pivot law without knowing the weights. After pivots $p_1,\dots,p_j$, prepare a uniform superposition over columns $i$ and, controlled by $i$, run a fresh copy of the comparison of $i$ against each $p_b$, each in its own new registers. Then compute a success flag that is $1$ when $i$ won all of them, and keep every register. Running the comparison circuits backwards inverts this preparation, as amplitude amplification requires. Fix the input, the pivot history and a value of $i$. The comparisons then act on separate fresh registers, so the probability that all of them report a win for $i$ is the product of the $a_{ip_b}$. Different values of $i$ are orthogonal, so these probabilities add:
$$
\Pr(\text{success and column }i)=\frac1m\prod_{b=1}^{j}a_{ip_b}=\frac{w_i}m .
$$
Success has probability $|w|/m$, and conditioned on success the column has exactly the ideal pivot law $w_i/|w|$.

Amplify with threshold $\gamma=1/(2m)$ and failure parameter $\varepsilon$ (next paragraph). This uses $O(\sqrt m\log(1/\varepsilon))$ preparations on every branch, whatever $|w|$ is, and keeps the conditional law. On success the algorithm appends that column and continues; on reported failure it stops and passes its current list to verification. It also stops after $T$ pivots. Before the winner is listed its weight exceeds $1/2$, so $|w|/m\ge\gamma$ and a stage fails with probability at most $\varepsilon$. After the winner is listed nothing is claimed: $|w|$ may be tiny or zero, and the sampler may then fail with certainty, but stopping cannot remove a listed column. Coupling the real and ideal processes until the first failure, each stage before the winner is listed adds at most $\varepsilon$ to the chance of disagreement, so the real list misses the winner with probability at most $2m/2^T+T\varepsilon$ ([record §5.2](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-coupling)).

**Amplification with a fixed cap.** Let a preparation succeed with probability $p=\sin^2\theta$, with normalised good part $g$. After $j$ Grover iterations the good component is $\sin((2j+1)\theta)\,g$ [@BHMT2002, Lemma 1], so every successful outcome returns $g$ itself and conditioning on success keeps the law of the marked label. One trial makes no iteration with probability $1/2$ and otherwise a uniform number below $\lceil10/\sqrt\gamma\rceil$; averaging $\sin^2((2j+1)\theta)$ over $j$ [@BBHT1998, Lemma 2] shows that a trial succeeds with probability at least $9/40$ whenever $p\ge\gamma$. So $\lceil\ln(1/\eta)/\ln(40/31)\rceil$ trials, stopping at the first success, use $O(\gamma^{-1/2}\log(1/\eta))$ preparations on **every** branch and for every $p$, fail with probability at most $\eta$ when $p\ge\gamma$, and fail with certainty when $p=0$ ([record §5.1](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-amplification-proof)). The cap does not depend on knowing $p$, which matters because the algorithm runs on inputs where no column wins.

**Verification.** Finally check each listed column. Decode its address afresh and measure it, then use amplification over the $K$ local tests, with threshold $1/K$, to search for a failing test; accept when none is found. Output $1$ if some candidate is accepted, and $0$ otherwise, including when the list is empty. A nonwinner fails some test at every address, including a meaningless label decoded off the promise (the changed board of Section 2 shows why the domain tests must be among them), so it is accepted with probability at most $\varepsilon$. The winner, decoded correctly, fails none and is accepted. Adding up, the error is at most $T\varepsilon$ when $F=0$ and at most $2m/2^T+T\varepsilon+\varepsilon\le1/250$ when $F=1$.

**The count.** Every count of trials, iterations, stages and comparisons is fixed in advance, so this cap holds on every input and branch. A comparison costs $c=O_k(r\log(r/\varepsilon))$ queries for its decoders plus $2(\ell+1)$ for its pointers. At most $T$ stages, each with $O(\sqrt m\log(1/\varepsilon))$ preparations of at most $T$ comparisons, cost $O(c\sqrt m\,T^2\log(1/\varepsilon))$. Verification treats at most $T$ candidates, each with a fresh decoding of $O_k(r\log(r/\varepsilon))$ queries and $O(\sqrt K\log(1/\varepsilon))$ test evaluations of $O(\log m)$ queries, with $K=O_k(m(\log m)^3)$. Both totals are $\sqrt m\,(\log m)^{O_k(1)}$. For an explicit power, bound each factor by a power of $\ell=\log_2m$: $\log(1/\varepsilon)$ by $1/\varepsilon=O(\ell)$, the comparison cost by $O_k(\ell^3)$ and $\sqrt K$ by $O_k(\sqrt m\,\ell^2)$. The tournament then costs $O_k(\sqrt m\,\ell^6)$ and verification $O_k(\sqrt m\,\ell^5)$, so
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 ,
$$
with $C_k$ depending only on $k$ ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-explicit-log6)). The exponent six is an artefact of this deliberately loose count. A pointer is read as $\ell$ bit queries followed by one query at the computed position, and any controlled query can be made from two ordinary ones; both change only constants. This is the $\sqrt m$ half of the arithmetic in the overview.

# 5. The classical lower bound: a planted pair

This section proves $R(F_{k,m})>\lfloor mL/100\rfloor$ by planting a winner in a random column. Fix $k$, let $m$ be large, and let $L=L_{k,m}$, so that $L<R(P)$. By Yao's minimax principle [@Yao1977] in its finite form, there is a distribution $\mu$ on promised inputs of $P$ under which every deterministic algorithm making $L$ queries is correct with probability at most $2/3$. (A randomized algorithm of depth $L$ is a mixture of finitely many trees, so its success vector lies in the convex hull of theirs; separating that hull from the orthant $[2/3,\infty)$ in every coordinate gives a nonnegative normal, which normalises to $\mu$; [record §6.2](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-minimax).)

**The pair.** Draw every address input from $\mu$ and, in each column $i$, one position $J_i$ uniformly, all mutually independent. Set $X_i$ to all ones except a zero at $J_i$, and leave every cell blank. This is the **dummy** input $Y^0$, and $F(Y^0)=0$. Now choose a column $I$ uniformly and independently of everything else. The **planted** input $Y^1$ erases the zero $X_I[J_I]$ and fills the true cell $B_{I,s_I}$ with correct transcripts and pointers to the zeros $J_j$ of the other columns. Column $I$ wins, so $F(Y^1)=1$. Figure 4 draws the pair on our board, with $I=1$ and $J=(4,1,2,3)$: the planted input is column $1$'s part of Figure 2.

![The planted pair on the board of Section 2, with $I=1$ and $J=(4,1,2,3)$. The two inputs differ only at $X_1[4]$ and in the cell $B_{1,10}$.](figures/exposition/fig4_planted.svg){width=76%}

Fix a deterministic algorithm $\mathcal A$ making at most $G=\lfloor mL/100\rfloor$ queries. Its runs on $Y^0$ and on $Y^1$ follow the same path until it first reads a bit where they differ. So
$$
\bigl|\Pr[\mathcal A(Y^1)=1]-\Pr[\mathcal A(Y^0)=1]\bigr|
\le\Pr(\text{erased zero hit})+\Pr(\text{true cell visited}),
$$
where both events refer to the run on the dummy input. The run on $Y^0$ does not depend on $I$, which is chosen independently.

**The erased zero.** Let $Z$ be the number of columns whose zero the dummy run finds. Given the dummy data, exactly $Z$ of the $m$ choices of $I$ select a found zero, so
$$
\Pr(\text{erased zero hit})=\frac{\mathbb E Z}{m}\le\frac{4G}{m^2}.
$$
For the inequality, an undiscovered zero is uniform among its column's unread positions, so a discovery while fewer than $m/2$ of them are read has probability at most $2/m$ per query, giving $2G/m$ early discoveries in expectation; a later one needs $m/2$ queries in its column, which happens in at most $2G/m$ columns ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-early-late)).

The independence of $I$ is what makes the identity true. Query one fixed position in each of four columns, so $\mathbb EZ=1$ and an independent $I$ is hit with probability $1/4$. Suppose instead that $I$ is chosen uniformly among the columns where a zero was found, and uniformly among all four when none was found, which happens with probability $(3/4)^4=81/256$. By symmetry $I$ is still uniform on its own, but now it is hit whenever some zero was found, with probability $1-(3/4)^4=175/256$ ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-selection-independence-example)). A uniform marginal is a weaker condition than independence from the run, and the proof needs independence.

**The true cell.** The algorithm need not compute $s_I$ to reach $B_{I,s_I}$; it may guess an address or visit many cells. But a query in the true cell names the $r$ hard answers $s_I$, and that is what must be unlikely. Call a column **heavy** if the dummy run makes more than $L$ queries to its address inputs. At most $G/L$ columns are heavy, so $\Pr(I\text{ heavy})\le G/(mL)$. For each column we bound the joint probability that it is light **and** a fixed query visits its true cell by $(2/3)^r$. The tool is a direct-product theorem with a separate cap on each instance.

**Direct product with separate caps.** *Let $U_1,\dots,U_r$ be independent samples from $\mu$, and suppose every deterministic algorithm making at most $L$ queries to one sample is correct with probability at most $\beta$. Let an algorithm choose adaptively which sample to query, make at most $L$ queries to **each** $U_h$ on every run, and use coins and side information jointly independent of the whole tuple $(U_1,\dots,U_r)$. Then it outputs all $r$ answers correctly with probability at most $\beta^r$.*

Both hypotheses are needed. For AND on two independent uniform two-bit inputs, $\beta=3/4$ with one query each, but a pooled budget of two queries computes the first answer and guesses $0$ for the second, right with probability $3/4>9/16$. For the identity on fair bits $X,Y$ with $L=0$, the side information $X\oplus Y$ is independent of each bit separately, yet the guess $(0,X\oplus Y)$ is right whenever $X=0$, with probability $1/2>1/4$ ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-independent-information)). The separately capped setting goes back to Shaltiel's fair decision trees [@Shaltiel2003]. The proof below is the conditional-value argument of Drucker's Lemmas 3.1–3.2, whose headline theorem instead uses one global budget [@Drucker2012, §1.3 and the end of §3].

::: {.aside title="Proof of the direct product"}
Fix the coins and side information; by joint independence the samples are still independent with law $\mu$, and the algorithm is a deterministic tree. Take a history $\tau$ of queries and answers that occurs with positive probability. Each recorded answer constrains only its own sample, and because the tree is deterministic, every tuple that agrees with these answers asks exactly these queries. So the tuples consistent with $\tau$ form a product $E_1(\tau)\times\dots\times E_r(\tau)$, and given $\tau$ the samples are independent with laws $\mu(\cdot\mid E_h(\tau))$. Let $q_h(\tau)$ count the queries to $U_h$ in $\tau$, and let $V_h(\tau)$ be the best probability of computing $P(U_h)$ under $\mu(\cdot\mid E_h(\tau))$ with at most $L-q_h(\tau)$ further queries. If the next query reads a bit of $U_h$, then querying it and continuing optimally is one strategy with that allowance, so averaging over the answer $b$,
$$
\sum_b\Pr(b\mid\tau)\,V_h(\tau b)\le V_h(\tau).
$$
One answer may raise $V_h$; only the average cannot. The other samples keep their laws and allowances, so their values do not change, and $\prod_hV_h$ has nonincreasing expectation from step to step. It starts at most $\beta^r$. At a leaf with output $s$, the probability of being right given $\tau$ is $\prod_h\Pr(P(U_h)=s_h\mid\tau)\le\prod_hV_h(\tau)$. Averaging over leaves and then over the coins and side information finishes the proof ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-product-law)).

Every distribution in this argument is finite. A capped algorithm has finitely many deterministic behaviours, so arbitrary independent randomness reduces to a finite mixture of them; Section 7 says what Lean proves.
:::

**Why the event must be joint.** A run that stays light behaves like a capped algorithm, but it need not succeed with probability at most $\beta^r$ given that it stays light. Take $P=\text{AND}$ on the three promised inputs $01,10,11$, uniformly; any one-query algorithm is right with probability at most $\beta=2/3$. Read the first bit, output $0$ if it is $0$, and otherwise read the second bit: this stays within one query exactly on input $01$, where it is right, so its success given that it stays light is $1$. The true statement is about the joint event: being right **and** staying within the caps has probability $1/3\le\beta$. With two instances the cap event can also make initially independent samples dependent ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-adaptive-example)).

**The simulator.** Fix a column $i$ and a query time $j\le G$. A simulator is given everything except the address inputs of column $i$: all zero positions, the other columns' address inputs and the blank cells. These are jointly independent of column $i$'s tuple. It runs the dummy algorithm, answering other queries itself and forwarding queries to column $i$'s address inputs, and stops before the $(L+1)$-st of these. If the run reaches time $j$ and the $j$-th query lies in a cell $B_{i,s}$, it outputs $s$, read off from the position of that query without reading the cell; otherwise it outputs a fixed address. It respects the cap $L$ on every instance and run, so by the direct product its output, learned or guessed, is the true address with probability at most $(2/3)^r$. Whenever column $i$ is light and the $j$-th dummy query visits its true cell, the simulator has not stopped and outputs $s_i$. Hence
$$
\Pr(i\text{ light and query }j\text{ visits }B_{i,s_i})\le(2/3)^r ,
$$
with lightness inside the probability ([record §6.5](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-simulator) traces the simulator on a small board, including a run where it stops). Summing over $j\le G$ gives $G(2/3)^r$ for each fixed column. Averaging over the independent uniform $I$ divides the sum over the $m$ columns by $m$, so no factor $m$ appears, and adding the heavy case,
$$
\Pr(\text{true cell visited})\le\frac{G}{mL}+G\left(\frac23\right)^r .
$$

**Finishing.** The gap is at most $4G/m^2+G/(mL)+G(2/3)^r$. With $r=40t$ and $m=4^t$, $(2/3)^2\le1/2$ gives $(2/3)^r\le m^{-10}$, and $G\le mL/100\le m^2/100$, so the gap is at most $4/100+1/100+1/(100m^8)<1/3$. A randomized algorithm computing $F$ with $G$ queries would accept dummy inputs with probability at most $1/3$ and planted ones with probability at least $2/3$. Fixing its coins gives deterministic algorithms whose gaps average to at least $1/3$, while each gap is below $1/3$, a contradiction. So
$$
R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor .
$$
Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm. This is the $m\cdot L$ half of the arithmetic.

# 6. Exponent four, and the order of quantifiers

This section combines the two bounds into the exponent. Insert $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$. For real $x\ge1$, $\lfloor x\rfloor\ge x/2$. Applying this to $L$ and to $mL/100$, for each fixed $k\ge2$ and all large $m$,
$$
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2},\qquad Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 .
$$
Fix $\alpha<4$, then an integer $k\ge2$ with $k>2/(4-\alpha)$. Then $d=2-1/k-\alpha/2>0$ and
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^{\alpha}}\ge c_{k,\alpha}\,\frac{m^{d}}{(\log_2m)^{2+6\alpha}}\longrightarrow\infty ,
$$
so no constant $C_\alpha$ works and $\alpha_{\rm tot}\ge4$. For $\alpha=3$, $k=3$ suffices, which refutes the cubic conjecture; $k=2$ gives exactly the cube and does not.

The order matters. All constants, including $C_k$ and the point from which the Forrelation bound holds, depend on $k$. One cannot substitute a $k$ that grows with $m$ into these fixed-$k$ bounds. A simple example shows the danger: for each fixed $k$, the condition $t\ge2^k$ holds for all large $t$, yet substituting $k=t$ asks for $t\ge2^t$, which never holds. The argument above avoids this by choosing $\alpha$ first, then a single $k$, then letting $m$ grow.

The matching upper bound is due to Aaronson, Ben-David, Kothari, Rao and Tal [@ABKRT2020, Theorem 2]: $D(f)=O(Q(f)^4)$ for every total $f$, and $R\le D$. Its proof combines adversary bounds on block sensitivity and spectral sensitivity, Huang's sensitivity theorem [@Huang2019] and Midrijānis's decision tree; the record reconstructs it with the explicit constant $35^4$ ([record Appendix A](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#R3-A-RESULT)). Hence $\alpha_{\rm tot}=4$.

# 7. What the Lean development checks

The theorem has also been proved in the Lean proof assistant, and the statement can be checked without reading the proof. A single [statement file][statement-file] in the [public repository](https://github.com/wcook04/quartic-query-lean), 343 lines importing only Mathlib, contains every definition the statement uses; its proofs are deliberate placeholders, and the proofs themselves are in [the solution file][statement-solution]. Five definitions carry the content. [The budget test for $R$][def-RLe] asks for one [finite random mixture][def-randomized] of [decision trees][def-tree] of depth at most $t$ that is right with probability $2/3$ on every promised input. [The budget test for $Q$][def-QLe] asks the same of one [quantum program][def-adaptive] that reaches the input only through the [bit oracle][def-oracle] and whose [query cap][def-querycap], a maximum over every branch, is at most $t$. [The winning condition][def-wins] is the four conditions of Section 2, inside [the function $F_{k,m}$][def-F] built from [$k$-fold Forrelation and its promise][def-P] and [circuits][def-circuit]. [The universal power bound][def-universal] asks for one $C$ with $R(f)\le C(1+Q(f))^\alpha$ for every total $f$. [$R$][def-R], [$Q$][def-Q] and [$\alpha_{\rm tot}$][def-alpha] are the least values passing these tests. The file states [four theorems][thm-all]. [$\alpha_{\rm tot}=4$][thm-alpha] is the same as the theorem of the overview. [The family statement][thm-headline] matches the overview's family, for some exact circuit realising $P$, with one weakening: the power of the logarithm in the quantum bound is some exponent $b$. Its classical bound $\lfloor mL/100\rfloor<R$ implies the $1/400$ form once $t\ge8$ (Section 6); it also states $\alpha_{\rm tot}=4$, the universal quartic bound and the circuit size, with one circuit for both bounds. The explicit $6$ and $1/400$ are proved in [a separate theorem][src-constants] that is built but not compared. [The failure of every bound $R\le C\,Q^3$][thm-cubic] is the same as the refutation of the cubic conjecture, and [the Forrelation lower bound][thm-forrelation] is the same as the hardness fact of Section 3, $L<R(P_{k,m})$ for each fixed $k$ and large $m$. Each link opens the exact lines.

An independent checker, Comparator, compiles the statement file and the proof separately, as [configured here][statement-config] ([a recorded run][statement-receipt]), and confirms that the proof establishes exactly these four statements, built from the statement file's own definitions, using only Lean's standard axioms. So a reader who accepts the definitions in that one file can trust the theorem without reading the proof. What remains is the question every formal proof leaves open: do these definitions mean $R$, $Q$ and the function intended? The five definitions above are where to answer it. The Lean proof of the Forrelation lower bound follows its own route rather than Bansal and Sinha's, and no person has reviewed it yet.

Two further results are proved in Lean and accepted by Comparator against their own statements. [Bounded amplification][cmp-amplifier] ([configuration][amplifier-config], [proof][amplifier-solution]) has a stronger conclusion than Section 4 states: a successful run returns the original register in the normalised good state, with the exact success mass ([record §5.1](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-returned-register)). Its setting is narrower: success must be a predicate on the basis labels of a finite register, and reducing a general success projector to that form is not yet proved in Lean. [The direct product][cmp-direct-product] ([configuration][direct-product-config]) bounds [the joint event][def-compliant] of answering all $r$ instances correctly while staying within every cap, for algorithms that need not respect the caps, which is stronger than Section 5's statement. It is weaker in two ways: coins and side information range over a finite space, with arbitrary randomness reduced to that case only by the ordinary argument of Section 5, and its cap condition is checked along the run and not yet proved in Lean to equal the count condition. The separation needs neither: its query bound uses only [the law of the measured label][src-amplify-measured], a partial form of amplification that fixes the label law and not the state, and every distribution in its lower bound is finite. No recorded statement review yet covers the four compared theorems or these two statements; the relations above are read from the statements themselves.

# Note on preparation {.unnumbered}

The separation theorem and the construction are OpenAI's [@OpenAI2026]; Section 2 credits their ingredients. This exposition and its Lean development were prepared with AI systems under the author's direction, and neither has yet had independent human review.

# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
[amplifier-config]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Independent/UniformAmplifier/comparator.json
[amplifier-solution]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Independent/UniformAmplifier/Solution.lean
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L274-L285
[def-P]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L175-L182
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-QLe]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L133-L137
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-RLe]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L62-L65
[def-adaptive]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L101-L107
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-circuit]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L190-L199
[def-compliant]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L111-L120
[def-oracle]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L89-L94
[def-querycap]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L109-L116
[def-randomized]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L46-L60
[def-tree]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L33-L44
[def-universal]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L311-L315
[def-wins]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272
[direct-product-config]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Independent/RealizedCaps/comparator.json
[src-amplify-measured]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticQuery/Upper/Amplify.lean#L345-L352
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[statement-config]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/comparator.json
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-receipt]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
