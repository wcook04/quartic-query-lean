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

The upper bound $R(f)=O(Q(f)^4)$ was already known [@ABKRT2020, Theorem 2]. The new part is the family, which refutes the conjecture of the same authors that $R(f)=O(Q(f)^3)$ [@ABKRT2020, Conjecture 2].

**The reason for four, in one line.** The input has $m$ columns, and a hidden certificate sits in one of them:
$$
Q\approx\sqrt m,\qquad R\approx m\cdot L\ \text{ with }\ L\approx m^{1-1/k},\qquad\text{so}\qquad R\approx m^{2-1/k}=(\sqrt m)^{4-2/k}\approx Q^{4-2/k}.
$$
The quantum algorithm finds the right column by a search over $m$ columns in which each step costs only polylogarithmically many queries. A classical algorithm must be prepared to find the certificate in any of the $m$ columns, and locating it inside one column means computing an address, which costs $L$ queries there. Here $L$ is the classical cost of the partial function $k$-fold Forrelation, which is nearly linear in its input size of about $m$ bits. The polylogarithmic factors have been dropped from this display.

The exponent $4-2/k$ is below four for every $k$, so the theorem is proved in a fixed order of quantifiers. Given any $\alpha<4$, first choose one integer $k$ with $4-2/k>\alpha$, that is $k>2/(4-\alpha)$. Then keep $k$ fixed and let $m$ grow; the ratio $R/(1+Q)^\alpha$ tends to infinity, so no constant $C_\alpha$ exists. Every constant above depends on $k$, which is why $k$ is never allowed to grow with $m$ inside these bounds (Section 6).

**Where this sits.** Pointer functions of Göös, Pitassi and Watson, developed by Ambainis and coauthors, gave a nearly quartic separation between deterministic and quantum query complexity [@GPW2018; @ABBLSS2017]. For bounded-error randomized complexity, Aaronson, Ben-David and Kothari introduced cheat sheets and reached the power $5/2$ [@ABK2016]. They observed that their method gives a cubic separation in a black-box way from any partial function with randomized cost nearly linear in its input size and polylogarithmic quantum cost. Tal reached $8/3-o(1)$ [@Tal2020], and Bansal and Sinha, and independently Sherstov, Storozhenko and Wu, supplied such a partial function and reached $3-o(1)$ [@BansalSinha2021; @SSW2023]. The exponent here is $4-o(1)$, matching the upper bound.

Why the earlier route stops at three can be read from the same arithmetic. In the cheat-sheet function the partial function $g$ on $n$ bits is composed with AND-OR on $n^2$ bits, so that its domain has short certificates; then $R\approx R(g)\cdot n^2$ while $Q\approx n$ [@ABK2016, §3.1]. Since $R(g)$ is at most about $n\approx Q$, the partial function contributes one factor of $Q$ and the outer function two. In the construction below the partial-function inputs in each column have about $m$ bits while the quantum algorithm spends only about $\sqrt m$ queries in total, so $L\approx Q^2$, and the search over columns contributes another $m\approx Q^2$.

| Example | What it shows | § |
|:-----------------------------------|:------------------------------------------------------|:--|
| Three eight-bit inputs $a^+,a^0,a^-$ | the one-sided promise; a quantum test accepts an unpromised input | 1 |
| The four-column board (Figure 2) | addresses, transcripts, outward pointers, a winner | 2 |
| The board with a changed domain bit | why the circuit must certify the promise | 2 |
| The board with one pointer moved | a column can beat every rival and still not win | 4 |
| The board with cycled pointers (Figure 3) | losers can beat each other in a cycle; the search survives | 4 |
| The board as a planted pair (Figure 4) | the two places where the inputs differ | 5 |
| Discovered columns chosen dependently | a uniform marginal does not replace independence | 5 |
| AND with one and two instances | conditioning on a cheap run breaks the product bound | 5 |

Full proofs of every step are in the [long reasoning record](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md); "record §6.5" below refers to its sections. Standard arguments that a reader may know already are set in boxes and can be skipped.

# 1. Three eight-bit inputs

We start with the partial function at the smallest size, $k=2$ and $m=4$. An input has two blocks of four bits. A bit $x$ stands for the sign $(-1)^x$, so $0$ means $+1$ and $1$ means $-1$. With coordinates ordered $00,01,10,11$, let
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

The quantum algorithm for $P$ prepares the uniform state, applies the sign and Walsh operations, and projects back onto the uniform state; the projection succeeds with probability $\Phi^2$. It succeeds with certainty on both $a^+$ and $a^-$. That is harmless for the partial function, which owes no answer on $a^-$. It will matter as soon as $P$ is placed inside a total function, because there every input needs an answer. This is the first distinction that must survive the whole argument: a cheap quantum test can accept an input that an exact certificate must reject.

All $256$ inputs can be classified by hand. The numerator takes the values $-8,-4,0,4,8$ with multiplicities $8,96,48,96,8$. The eight even-parity second blocks are the signed rows of $W$; each has a transform with one entry of size four, contributing $64$ inputs to each of the numerators $\pm4$. For each of the eight odd-parity blocks, every entry of the transform is $\pm2$, so varying the first block gives twice a sum of four free signs, with multiplicities $1,4,6,4,1$. Hence there are $104$ one-inputs, $48$ zero-inputs and $104$ unpromised inputs. At this size the classical lower bound is empty, since $L_{2,4}=\lfloor 2/4\rfloor=0$; the example checks conventions only.

# 2. One column, then four

**One column.** Figure 1 shows the general layout. Fix $k\ge2$, let $m=4^t$ and $\ell=\log_2m$. There are $m$ columns. Column $i$ holds

- a string $X_i\in\{0,1\}^m$;
- $r$ inputs $A_{i,1},\dots,A_{i,r}$ to the partial function $P=P_{k,m}$, each of $km$ bits;
- an array of $2^r$ cells $B_{i,s}$, one for each $s\in\{0,1\}^r$.

When all of its $A_{i,h}$ are promised, column $i$ has the **address** $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$. A cell holds $r$ circuit transcripts, explained below, and one $\ell$-bit pointer $p_{i,s,j}$ into each other column $j$. Every bit is an ordinary input bit, and every assignment of bits is allowed.

![One column of $F_{k,m}$. The answers to the $r$ address inputs select one of $2^r$ cells; the cell at the true address certifies those answers and points to a zero in every other column.](figures/exposition/fig1_column.svg){width=100%}

Column $i$ **wins** at address $s$ when four conditions hold: $X_i$ is all ones; every $A_{i,h}$ is promised with $P(A_{i,h})=s_h$; every transcript in $B_{i,s}$ is correct; and every pointer $p_{i,s,j}$ reaches a zero of $X_j$. The total function is $F(y)=1$ exactly when some column wins at some address. At most one pair wins. Two different winning columns are impossible, because a pointer from the first would find a zero in the all-one string of the second. Within one column, the promised values fix the address.

Our addressing comes from Aaronson, Ben-David and Kothari's cheat sheets, which store a certificate at the address formed by the answers to independent partial-function instances; they used about $10\log n$ copies, and here $r=20\log_2m$ [@ABK2016, §3.1]. The all-one column whose certificate points to zeros elsewhere descends from the pointer functions [@GPW2018; @ABBLSS2017]. The new features are a separate cell array in every column, pointers that point outward, and the tournament of Section 4.

**Four columns.** Now take $m=4$, $k=2$ and, so that the cells can be listed, only $r=2$ address inputs per column, with two-bit pointers decoded as $00,01,10,11\mapsto$ positions $1,2,3,4$. Set
$$
(X_1,X_2,X_3,X_4)=(1111,\ 0111,\ 1011,\ 1101).
$$
Columns $1,3,4$ have address inputs $(a^+,a^0)$, so their address is $10$. Column $2$ has $(a^-,a^0)$ and no address. In every cell, a pointer into column $2$ names position $1$, into column $3$ position $2$, into column $4$ position $3$, and a pointer into column $1$ names the position encoded by the cell's own address. Every transcript is the true evaluation of a fixed $180$-gate circuit described below.

![The four-column board. Column 1 wins at address 10: its pointers reach $X_2[1]=X_3[2]=X_4[3]=0$. The dashed pointer from column 3's own true cell lands on a one, as every pointer into column 1 must.](figures/exposition/fig2_board.svg){width=100%}

Column $1$ wins at $10$ (Figure 2). Every other column has a zero in its own string and cannot win, so $F=1$. The board has $4(4+16+4(6+360))=5936$ bits.

**Transcripts.** Fix a circuit $C$ of fan-in two which outputs a domain bit $d$ and a value bit $b$: $(d,b)=(1,P(a))$ on promised inputs and $(0,0)$ otherwise. For $P_{2,4}$ there is an exact such circuit with $180$ gates, obtained by Shannon expansion of the truth tables; it gives $(1,1)$ on $a^+$, $(1,0)$ on $a^0$ and $(0,0)$ on $a^-$. A transcript proposes a value for every gate. It satisfies all gate equations exactly when it equals the true evaluation: by induction along the gate order, each gate's predecessors already agree with evaluation, so its own value is forced. This holds on every input, promised or not. So a winning cell certifies the promise through the domain bits and the address through the value bits.

**The domain bit is needed.** Change the board: set $X_1=0111$ and $X_2=1111$, and make every pointer into column $1$ name position $1$. Column $2$ is now all ones. At address $00$ its stored value bits $(0,0)$ agree with the address, its pointers find zeros in the other three columns, and every gate equation holds, because the transcripts are true evaluations. Its first domain bit is $0$, since $a^-$ is unpromised, so column $2$ does not win, and $F=0$. A function that checked only value bits would accept this board.

**Local tests.** Winning can be checked by small tests: $m$ tests of the column's own bits, $m-1$ pointer tests, $rS$ gate tests for a circuit of size $S$, and $2r$ tests that each domain bit is $1$ and each value bit equals $s_h$. Thus a candidate $(i,s)$ has
$$
K=2m-1+r(S+2)
$$
tests, each reading at most $\max(3,\ell+1)$ bits: a gate test reads one gate and two predecessors, and a pointer test reads $\ell$ pointer bits and then the one bit they select. All tests pass exactly when $(i,s)$ wins, so a nonwinner fails at least one test at every address. On the board $K=4+3+2(180+2)=371$. At $(1,10)$ all pass; at column $1$'s other three addresses the value tests fail; on the changed board, $(2,00)$ fails only its domain test.

# 3. The general partial function

For general $k$ and $m=4^t$, index each of $k$ sign blocks by $\{0,1\}^{2t}$, let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=(1,\dots,1)/\sqrt m$, and let $D_z$ be the diagonal matrix of signs $z$. $k$-fold Forrelation [@AA2018] is
$$
\Phi(z_1,\dots,z_k)=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,\qquad \delta=2^{-5k},
$$
with $P_{k,m}$ defined by the thresholds $\delta$ and $\delta/2$ exactly as before [@BansalSinha2021]. Since $H$ and each $D_z$ preserve length, $|\Phi|\le1$. The construction needs three facts about $P_{k,m}$.

*A cheap quantum decoder.* Applying one sign diagonal costs one query by phase kickback, and the Walsh transforms cost none, so one projection experiment uses $k$ queries and succeeds with probability $\Phi^2$. On the promise this is at least $c=\delta^2$ or at most $c/4$. Repeating $\rho=\lceil16c^{-1}\ln(1/\eta)\rceil$ times and accepting when at least $\rho c/2$ trials succeed gives error at most $\eta$ with $O_k(\log(1/\eta))$ queries, a cap that holds on every input.

::: {.aside title="Standard proof: the repetition bound"}
Let $S$ count successes among $\rho$ independent trials with success probability $p$. Then $\mathbb E\,a^{S}=(1-p+pa)^\rho\le e^{\rho p(a-1)}$. Markov's inequality with $a=e$ bounds a false acceptance, when $p\le c/4$, by $e^{-\rho c/2+\rho p(e-1)}\le e^{-\rho c/16}$. With $a=e^{-1}$ it bounds a false rejection, when $p\ge c$, by $e^{\rho c/2-\rho p(1-e^{-1})}\le e^{-\rho c/10}$. Both are at most $\eta$.
:::

*An exact circuit.* Because $\Phi$ has two boundary factors and $k-1$ internal factors of $m^{-1/2}$, $\Phi=N/2^{t(k+1)}$ for an integer $N$, computed by $k-1$ integer Walsh transforms with entries of $O_k(\log m)$ bits. The promise becomes two integer comparisons, $p_1=[2^{5k}N\ge2^{t(k+1)}]$ and $p_0=[2^{5k+1}|N|\le2^{t(k+1)}]$, with output $(d,b)=(p_1\lor p_0,\,p_1)$. A fast Walsh transform and ripple-carry arithmetic give a fan-in-two circuit with $S\le200(k+1)^2m(\log_2m)^2$ gates (record §3.4).

*Classical hardness.* For fixed $k$ and all sufficiently large $m$,
$$
R(P_{k,m})>L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor .
$$
This is the randomized lower bound of Bansal and Sinha for this one-sided promise [@BansalSinha2021, Theorem 1.3 and Corollary 1.4]; Sherstov, Storozhenko and Wu proved an optimal separation of the same kind independently [@SSW2023]. The record gives a separate derivation through rounded Gaussian chains and a decision-tree martingale (record §§3.6–3.15).

With these, the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. The parameter $m$ counts columns. Both bounds below are about this one function on these large inputs, and both use the same circuit.

# 4. The quantum algorithm: a tournament

The quantum algorithm must find the winner, if there is one, among $m$ columns. A direct search does not suffice. Checking that one column wins means reading its $m$ string bits and $m-1$ pointers, which costs about $\sqrt m$ quantum queries; a Grover search over $m$ columns with that check inside costs about $\sqrt m\cdot\sqrt m=m$, and then $R\approx Q^{2-1/k}$ only. The algorithm instead compares columns two at a time, where each comparison costs polylogarithmically many queries, searches with comparisons, and runs the expensive check only on a short list.

**Comparing two columns.** Decode the $r$ address inputs of each column with error $\varepsilon/r$ each, so a promised column gets its true address with probability at least $1-\varepsilon$. Then follow each decoded cell's pointer into the other column and read the bit it names. A zero disqualifies that column. If exactly one is disqualified, the other wins the comparison; otherwise the smaller index wins. Running the same procedure for the unordered pair makes the probabilities complementary: if $a_{ij}$ is the probability that $i$ beats $j$, then $a_{ij}+a_{ji}=1$ for $i\ne j$, and we set $a_{ii}=0$.

The outward pointers make comparisons against the winner reliable. The winner $i^\star$ has an all-one string, so no pointer from any rival, under any decoded label, finds a zero in it. When $i^\star$'s own address is decoded correctly, its true cell disqualifies the rival. So $a_{i^\star j}\ge1-\varepsilon$ for every $j$, whatever the rival's address inputs are, including inputs outside the promise. Nothing is claimed about comparisons between two losers.

**Beating every rival is not winning.** On the board of Figure 2, change only $p_{1,10,2}$ from position $1$ to position $2$. It now reads $X_2[2]=1$, so column $1$ fails one pointer test and $F=0$. Yet column $1$ still beats every rival under every rival label: against column $2$ neither is disqualified and the index rule picks column $1$, and against columns $3$ and $4$ its pointers still find zeros. A column that dominates the comparisons is only a candidate, and the final verification is logically necessary.

**Losers can form a cycle.** Return to Figure 2 and change three pointers between losers: column $2$'s pointer into column $4$ names position $1$, column $3$'s pointer into column $2$ names position $2$, and column $4$'s pointer into column $3$ names position $1$. Column $1$'s cell is untouched, so it still wins and $F=1$. Now (with exact decoding) column $2$ beats $3$, column $3$ beats $4$ and column $4$ beats $2$ (Figure 3). No ordering of the columns is consistent with the comparisons, so the search cannot rely on one.

![Comparisons on the board with cycled loser pointers. An arrow $i\to j$ means that $i$ beats $j$. The winner beats everyone; the three losers form a cycle.](figures/exposition/fig3_tournament.svg){width=62%}

**Weights instead of an order.** Keep a weight $w_i$ for each column, starting at $w_i=1$, and let $W=\sum_iw_i$. A stage chooses a pivot $p$ with probability $w_p/W$, adds it to a list, and multiplies each weight by its probability of beating the pivot: $w_i\leftarrow w_ia_{ip}$. The pivot's own weight becomes zero. On the cycled board:

| Pivot $p$ | New weights $(w_1,w_2,w_3,w_4)$ | New $W$ |
|---|---|---|
| $1$ | $(0,0,0,0)$ | $0$ |
| $2$ | $(1,0,0,1)$ | $2$ |
| $3$ | $(1,1,0,0)$ | $2$ |
| $4$ | $(1,0,1,0)$ | $2$ |

Each pivot has probability $1/4$, so the expected new total is $3/2$. In general, pairing the terms $w_iw_pa_{ip}$ and $w_pw_ia_{pi}$ and using $a_{ip}+a_{pi}=1$,
$$
\mathbb E[W'\mid w]=\frac1W\sum_{i,p}w_iw_pa_{ip}=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2,
$$
which here is $(16-4)/8=3/2$. No transitivity and no margin away from $1/2$ is used. After $T$ stages $\mathbb EW_T\le m/2^T$. Meanwhile the winner's weight stays at least $(1-\varepsilon)^T\ge1-T\varepsilon$ until it is chosen. With
$$
T=\lceil\log_2(1000m)\rceil,\qquad\varepsilon=\frac{1}{1000T},
$$
the winner keeps weight above $1/2$, so if it has not been chosen then $W_T>1/2$; by Markov's inequality this has probability at most $2m/2^T$. On the cycled board the winner is always chosen within three stages.

**Sampling a pivot quantumly.** After pivots $p_1,\dots,p_j$, prepare a uniform column $i$ together with a fresh comparison of $i$ against each earlier pivot, in fresh workspace, and mark success when $i$ wins them all. The comparisons are independent, and different values of $i$ are orthogonal, so
$$
\Pr(\text{success and column }i)=\frac1m\prod_{b=1}^{j}a_{ip_b}=\frac{w_i}m .
$$
Success has probability $W/m$, and conditioned on success the column is distributed exactly as $w_i/W$, the law of the ideal pivot. Amplitude amplification turns this into a sample in about $\sqrt{m/W}$ preparations. The winner's weight keeps $W>1/2$ until it is chosen, so a threshold $\gamma=1/(2m)$ suffices. Each stage fails with probability at most $\varepsilon$, so coupling with the ideal process adds at most $T\varepsilon$ to the miss probability, and a stage that fails after the winner has been listed cannot remove it.

::: {.aside title="Standard proof: amplification with a fixed cap"}
Let a preparation succeed with probability $p=\sin^2\theta$, writing its state as $\sin\theta\,g+\cos\theta\,b$ with $g$ and $b$ the normalised good and bad parts. Each Grover iteration rotates the plane of $g,b$ by $2\theta$, so after $j$ iterations the state is $\sin((2j+1)\theta)g+\cos((2j+1)\theta)b$ [@BHMT2002, Lemma 1]. Every successful outcome returns $g$, so conditioning on success leaves the law of the marked label unchanged. For a threshold $\gamma\le1/2$, let $J=\lceil10/\sqrt\gamma\rceil$. In one trial, with probability $1/2$ make no iteration, and otherwise choose $j$ uniformly from $0,\dots,J-1$. The identity
$$
\frac1J\sum_{j=0}^{J-1}\sin^2((2j+1)\theta)=\frac12-\frac{\sin(4J\theta)}{4J\sin2\theta}
$$
[@BBHT1998, Lemma 2] gives success at least $9/40$ from the uniform half when $\gamma\le p\le1/2$, since then $\sin2\theta\ge\sqrt\gamma$; when $p\ge1/2$ the zero-iteration half gives at least $1/4$. So $\lceil\ln(1/\eta)/\ln(40/31)\rceil$ trials fail with probability at most $\eta$, using $O(\gamma^{-1/2}\log(1/\eta))$ preparations on **every** branch and for every $p$. The cap does not depend on knowing $p$, which matters because the algorithm runs on inputs where no column wins.
:::

**Verification.** Finally check each of the at most $T$ listed columns. Decode its address afresh, then use amplification over the $K$ local tests, with threshold $1/K$, to search for a failing test. A nonwinner fails some test at every address and is rejected with probability at least $1-\varepsilon$. The winner, decoded correctly, fails none and is accepted. Adding up, the error is at most $T\varepsilon$ when $F=0$ and at most $2m/2^T+T\varepsilon+\varepsilon$ when $F=1$. At $m=4$ the second is $583/192000$, a check on the bookkeeping and nothing more.

**The count.** A comparison costs $O_k(r\log(r/\varepsilon))$ queries for decoding plus $2(\ell+1)$ for pointers. A stage uses $O(\sqrt m\log(1/\varepsilon))$ preparations, each with up to $T$ comparisons, and there are $T$ stages. Verifying one candidate costs $O(\sqrt K\log(1/\varepsilon))$ tests of $O(\log m)$ queries each, with $K=O_k(m(\log m)^3)$. Every factor besides $\sqrt m$ is a power of $\log m$, so $Q(F_{k,m})\le\sqrt m\,(\log m)^{O_k(1)}$. Bounding each factor crudely by a power of $2t=\log_2m$ (at most $6\cdot2t$ stages, at most $24001\cdot2t$ trials per stage, at most $6\cdot2t$ comparisons per preparation, and at most $C\cdot(2t)^3$ queries per comparison) gives
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 ,
$$
with $C_k$ depending only on $k$ (record §5.4). The exponent six is an artefact of this deliberately loose count. Two implementation points do not change it: a pointer is read as $\ell$ bit queries followed by one query at the computed position, and any controlled query can be made from two ordinary ones.

::: {.aside title="Remark: a returned state versus a measured label"}
Amplification is used inside other quantum steps, so one may ask whether it returns the original good state $g$ itself or only a label with the right distribution. The two differ: $|+\rangle$ and $|-\rangle$ give the same fair coin when measured, but a Hadamard gate followed by measurement tells them apart. The query bound above uses only the measured label of each pivot and candidate, whose law $w_i/W$ is exact, and the final projector is block-diagonal in those retained labels, so no cross terms arise. The rotation argument in the box above shows that the full normalised good state is returned (record §5.5).
The Lean development proves the measured-label law that the query bound uses. Lean also proves the stronger statement that the amplifier returns the full normalised good state on a designated register, although the separation does not need it.
:::

# 5. The classical lower bound: a planted pair

Fix $k$, let $m$ be large, and let $L=L_{k,m}$, so that $L<R(P)$. By the minimax theorem there is a distribution $\mu$ on promised inputs of $P$ under which every deterministic algorithm making $L$ queries is correct with probability at most $2/3$.

::: {.aside title="Standard proof: minimax for a finite set of trees"}
There are finitely many decision trees of depth $L$. Give each its vector of correctness indicators, one coordinate for each of the $D$ promised inputs, and let $K$ be the convex hull of these vectors. Since $L<R(P)$, no mixture of trees is correct with probability $2/3$ on every promised input, so $K$ is disjoint from the orthant $O=[2/3,\infty)^D$. Take closest points $a\in K$ and $c\in O$ and put $v=c-a\ne0$. Since $c$ is the nearest point of $O$ to $a$, we have $v\ge0$, and $c_x=2/3$ wherever $v_x>0$. Since $a$ is the nearest point of $K$ to $c$, we have $v\cdot(b-a)\le0$ for every $b\in K$. Hence $v\cdot b\le v\cdot a=\tfrac23\sum_xv_x-\|v\|^2$. Normalising $v$ to a probability distribution $\mu$ makes the average success of every tree less than $2/3$.
:::

**The pair.** Draw every address input independently from $\mu$. In each column $i$ choose one position $J_i$ uniformly and set $X_i$ to all ones except a zero at $J_i$. Leave every cell blank. This is the **dummy** input $Y^0$, and $F(Y^0)=0$. Now choose a column $I$ uniformly and independently of everything else. The **planted** input $Y^1$ erases the zero $X_I[J_I]$ and fills the true cell $B_{I,s_I}$ with correct transcripts and pointers to the zeros $J_j$ of the other columns. Column $I$ wins, so $F(Y^1)=1$. Figure 4 draws the pair on our board, with $I=1$ and $J=(4,1,2,3)$: the planted input is column $1$'s part of Figure 2.

![The planted pair on the board of Section 2, with $I=1$ and $J=(4,1,2,3)$. The two inputs differ only at $X_1[4]$ and in the cell $B_{1,10}$.](figures/exposition/fig4_planted.svg){width=86%}

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
For the inequality, a column's zero is uniform among the positions not yet read in that column. A discovery made while fewer than $m/2$ positions of its column have been read has probability at most $2/m$ per query, so such early discoveries number $2G/m$ in expectation; a later discovery needs at least $m/2$ queries in its column, which happens in at most $2G/m$ columns (record §6.4).

The independence of $I$ is what makes the identity true. Query one fixed position in each of four columns, so $\mathbb EZ=1$ and an independent $I$ is hit with probability $1/4$. Suppose instead that $I$ is chosen uniformly among the discovered columns whenever there are any. By symmetry $I$ is still uniform on its own, but now it is hit whenever some zero was found, with probability $1-(3/4)^4=175/256$. A uniform marginal is a weaker condition than independence from the run, and the proof needs independence.

**The true cell.** Reaching the true cell $B_{I,s_I}$ requires knowing $s_I$, a vector of $r$ hard answers. Call a column **heavy** if the dummy run makes more than $L$ queries to its address inputs. At most $G/L$ columns are heavy, so $\Pr(I\text{ heavy})\le G/(mL)$. For a light column, we show that the run reaches its true cell with probability at most about $(2/3)^r$ per query. The tool is a direct-product theorem with a separate cap on each instance.

::: {.aside title="Direct product with separate caps"}
Let $U_1,\dots,U_r$ be independent samples from $\mu$, and suppose every algorithm making at most $L$ queries to one sample is correct with probability at most $\beta$. Then an adaptive algorithm that makes at most $L$ queries to **each** $U_h$, and whose coins and side information are jointly independent of the whole tuple, outputs all $r$ answers correctly with probability at most $\beta^r$ [@Drucker2012, Lemmas 3.1–3.2].

*Proof.* Fix the coins and side information. At any reachable history, the inputs consistent with it form a product of one set per block, because determinism means the answers seen so far force each next query. So the posterior law is still a product. Let $V_h$ be the best success probability on block $h$ with the queries that block has left. A query to block $h$ can only lower the expected value of $V_h$, since querying and then playing optimally is one available strategy, and it leaves the other $V_j$ unchanged. Hence $\prod_hV_h$ has nonincreasing expectation. At a leaf the probability of being right on all blocks is at most $\prod_hV_h$, and initially it is at most $\beta^r$. Averaging over the coins and side information finishes the proof (record §6.1).

The separate caps matter: with a total budget of $rL$, an algorithm could spend everything on a few blocks. Joint independence also matters; pairwise or marginal independence of the side information from each $U_h$ is not enough (record §6.1).
Every distribution in this argument is finite, and the Lean development proves the direct product in that setting. Lean also proves it with coins and side information drawn from any finite probability space jointly independent of the inputs; a capped algorithm has finitely many deterministic behaviours, so the ordinary proof above extends this to arbitrary independent randomness.
:::

**Why the event must be joint.** It is tempting to argue that a run which stays light is a run of a capped algorithm, and so succeeds with probability at most $\beta^r$ given that it stays light. That conditional claim is false. Take $P=\text{AND}$ on the three promised inputs $01,10,11$, uniformly; any one-query algorithm is right with probability at most $\beta=2/3$. The algorithm that reads the first bit, outputs $0$ if it is $0$, and otherwise reads the second bit, stays within one query exactly on input $01$, where it is right. Its success conditioned on staying light is $1$. The true statement is about the joint event: the probability of being right **and** staying within the caps is $1/3\le\beta$. The same failure appears with two instances. Take AND on two uniform two-bit inputs $A$ and $B$, so $\beta=3/4$. The algorithm reads the first bit $a$ of $A$, then reads bit number $a+1$ of $B$, reads the first bit of $A$ again if the two answers differ, and always outputs $(0,0)$. Of the $16$ inputs, $8$ respect both caps and $5$ of those are answered correctly. So $\Pr(\text{correct and capped})=5/16\le9/16=\beta^2$, while $\Pr(\text{correct}\mid\text{capped})=5/8>9/16$.

**The simulator.** Fix a column $i$ and a query time $j\le G$. A simulator is given everything except the address inputs of column $i$: all zero positions, the other columns' address inputs and the blank cells, data jointly independent of column $i$'s tuple. It runs the dummy algorithm, answering other queries itself and forwarding queries to column $i$'s address inputs, and stops before the $(L+1)$-st of these. If the $j$-th query lands in a cell $B_{i,s}$, it outputs $s$; otherwise it outputs a fixed address. This simulator respects the cap $L$ on every instance, so by the direct product it outputs the true address with probability at most $(2/3)^r$. Whenever column $i$ is light and the $j$-th dummy query visits its true cell, the simulator has not stopped and outputs $s_i$. Hence
$$
\Pr(i\text{ light and query }j\text{ visits }B_{i,s_i})\le(2/3)^r .
$$
Summing over $j\le G$, averaging over the independent uniform $I$, and adding the heavy case,
$$
\Pr(\text{true cell visited})\le\frac{G}{mL}+G\left(\frac23\right)^r .
$$

**Finishing.** The gap is at most $4G/m^2+G/(mL)+G(2/3)^r$. With $r=40t$ and $m=4^t$, $(2/3)^2\le1/2$ gives $(2/3)^r\le m^{-10}$, and $G\le mL/100\le m^2/100$, so the gap is at most $4/100+1/100+1/(100m^8)<1/3$. A randomized algorithm computing $F$ with $G$ queries would accept dummy inputs with probability at most $1/3$ and planted ones with probability at least $2/3$. Fixing its coins gives deterministic algorithms whose gaps average to at least $1/3$, while each gap is below $1/3$, a contradiction. So
$$
R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor .
$$
Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm.

# 6. Exponent four, and the order of quantifiers

Insert $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$. For real $x\ge1$, $\lfloor x\rfloor\ge x/2$. Applying this to $L$ and to $mL/100$, for each fixed $k\ge2$ and all large $m$,
$$
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2},\qquad Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 .
$$
Fix $\alpha<4$, then an integer $k\ge2$ with $k>2/(4-\alpha)$. Then $d=2-1/k-\alpha/2>0$ and
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^{\alpha}}\ge c_{k,\alpha}\,\frac{m^{d}}{(\log_2m)^{2+6\alpha}}\longrightarrow\infty ,
$$
so no constant $C_\alpha$ works and $\alpha_{\rm tot}\ge4$. For $\alpha=3$, $k=3$ suffices, which refutes the cubic conjecture; $k=2$ gives exactly the cube and does not.

The order matters. All constants, including $C_k$ and the point from which the Forrelation bound holds, depend on $k$. One cannot substitute a $k$ that grows with $m$ into these fixed-$k$ bounds. A simple example shows the danger: for each fixed $k$, the condition $t\ge2^k$ holds for all large $t$, yet substituting $k=t$ asks for $t\ge2^t$, which never holds. The argument above avoids this by choosing $\alpha$ first, then a single $k$, then letting $m$ grow.

The matching upper bound is due to Aaronson, Ben-David, Kothari, Rao and Tal [@ABKRT2020, Theorem 2]: $D(f)=O(Q(f)^4)$ for every total $f$, and $R\le D$. In outline, the adversary method bounds block sensitivity by $O(Q^2)$ and spectral sensitivity by $O(Q)$; Huang's theorem bounds degree by the square of spectral sensitivity [@Huang2019]; and Midrijānis's decision tree gives $D\le\operatorname{bs}\cdot\deg$. Multiplying gives $D=O(Q^4)$; the record reconstructs this with the explicit constant $35^4$ (record Appendix A). Hence $\alpha_{\rm tot}=4$.

# 7. What the Lean development checks

The theorem has also been proved in the Lean proof assistant, and the statement can be checked without reading the proof. A single [statement file][statement-file] in the [public repository](https://github.com/wcook04/quartic-query-lean) contains every definition the statement uses: [decision trees][def-tree] and [finite random mixtures][def-randomized] of them, with [$R$][def-R] as the least worst-case depth achieving error at most $1/3$ on every promised input; [quantum programs][def-adaptive] whose only input access is the [bit oracle][def-oracle], with [$Q$][def-Q] as the least worst-case query count; [$k$-fold Forrelation and its promise][def-P]; [circuits][def-circuit], transcripts and [the function $F_{k,m}$][def-F]; and [$\alpha_{\rm tot}$][def-alpha]. It has 343 lines and imports only Mathlib. It states [four theorems][thm-all]: [$\alpha_{\rm tot}=4$][thm-alpha]; [the family statement of the overview][thm-headline], with the quantum bound in the form $C\sqrt m\,(\log_2 m)^b$ for some exponent $b$ and the classical bound $\lfloor mL/100\rfloor<R$, both for the same circuit; [the failure of every bound $R\le C\,Q^3$][thm-cubic]; and [the Forrelation lower bound][thm-forrelation] $L<R(P_{k,m})$ for each fixed $k$ and large $m$. Each link opens the exact lines.

An independent checker, Comparator, compiles this file and the proof separately, as [configured here][statement-config], and confirms that the proof establishes exactly these four statements, built from the file's own definitions, using only Lean's standard axioms. So a reader who accepts the definitions in that one file can trust the theorem without reading the proof. What remains for the reader is the question every formal proof leaves open: do these definitions mean $R$, $Q$ and the function intended? The file is short enough to answer that in one sitting. The Lean proof of the Forrelation lower bound follows its own route rather than Bansal and Sinha's, and no person has reviewed it yet.

Two further results are proved in Lean and accepted by Comparator: [the amplifier that returns the full good state][cmp-amplifier] (Section 4) and [the direct product with finite independent randomness][cmp-direct-product] (Section 5). The separation needs neither: its query bound uses only measured labels, and every distribution in its lower bound is finite.

# Note on preparation {.unnumbered}

The separation theorem and the construction are OpenAI's [@OpenAI2026]. Addressing certificates by partial-function answers comes from Aaronson, Ben-David and Kothari's cheat sheets [@ABK2016], and the all-one column with pointers to zeros from Göös, Pitassi and Watson [@GPW2018]. The comparison viewpoint has relatives in quantum minimum finding [@DH1996], king finding in tournaments [@MPS2023], and recent work of Ben-David and Kothari [@BDK2026] and of Ambainis, Iraids and Kokainis [@AIK2026]. This exposition and its Lean development were prepared with AI systems under the author's direction, and neither has yet had independent human review.

# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L20
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L280-L285
[def-P]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L175-L182
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-adaptive]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L101-L107
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-circuit]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L190-L199
[def-oracle]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L89-L94
[def-randomized]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L46-L60
[def-tree]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L33-L44
[statement-config]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/comparator.json
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/659b571510ed501a8fbfb11a82c83549cab42441/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
