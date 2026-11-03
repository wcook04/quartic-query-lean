---
title: "Why the exponent is four"
subtitle: "An examples-first account of the nearly quartic separation between randomized and quantum query complexity"
author: "Will Cook"
date: "November 2026"
bibliography: exposition.bib
link-citations: true
---

# Introduction

A query algorithm computes a Boolean function $f$ of an input $x\in\{0,1\}^n$ by reading bits of $x$; we charge only for the bits it reads. A randomized algorithm chooses each position from its coins and the answers so far. A quantum algorithm reads through the oracle $O_x|j,b,w\rangle=|j,b\oplus x_j,w\rangle$, which it may apply to a superposition of positions $j$, answer bits $b$ and workspace states $w$. We write $R(f)$ and $Q(f)$ for the least number of queries with which a randomized or a quantum algorithm computes $f$ with error at most $1/3$ on every input, where the count is the worst case over inputs and over every coin flip or measurement outcome.

For a partial function, which owes an answer only on a promised set of inputs, the measures can be far apart: the function of Section 1 has quantum cost independent of its input size and nearly linear classical cost. For a **total** function, defined on every input, $R$ is bounded by a polynomial in $Q$, and the question is how large the power must be. Let
$$
\alpha_{\rm tot}=\inf\bigl\{\alpha\ge0:\ \text{some constant }C\text{ gives }R(f)\le C\,(1+Q(f))^{\alpha}\text{ for every total }f\bigr\}.
$$

**Theorem** [@OpenAI2026, Theorem 1.1]. $\alpha_{\rm tot}=4$. More precisely, for each fixed integer $k\ge2$ there are total functions $F_{k,m}$, defined for all sufficiently large powers of four $m$, with
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
\qquad
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2},
$$
where $C_k$ depends only on $k$.

The upper bound $R(f)=O(Q(f)^4)$ for every total $f$ is due to Aaronson, Ben-David, Kothari, Rao and Tal [-@ABKRT2020, Theorem 2], who conjectured that the truth is $R(f)=O(Q(f)^3)$ [@ABKRT2020, Conjecture 2]. The family $F_{k,m}$ refutes that conjecture and shows that no power below four suffices. The preprint does not fix the constants or the power of the logarithm; the values $6$ and $1/400$ come from the counts in Sections 4 and 6.

The exponent comes from one line of arithmetic. The input of $F_{k,m}$ has $m$ columns, and a certificate that $F=1$ sits in one of them. Up to logarithmic factors,
$$
Q\approx\sqrt m,\qquad R\approx m\cdot L\ \text{ with }\ L\approx m^{1-1/k},\qquad\text{so}\qquad R\approx m^{2-1/k}=(\sqrt m)^{4-2/k}\approx Q^{4-2/k}.
$$
Each column holds $r=20\log_2m$ instances of $k$-fold Forrelation, a partial function on about $m$ bits, and their $r$ answers form an address that selects the cell where the column's certificate would sit. A quantum algorithm computes addresses cheaply and searches the $m$ columns, and each step of its search costs only polylogarithmically many queries. For the classical bound, we plant a certificate in a random column of an input on which $F=0$. To notice the change, an algorithm must either find the one zero that planting erased or query the planted cell, and a query to a cell already names all $r$ answers. Learning them costs about $L$ queries, the classical cost of one instance; with fewer queries to the column, a direct-product theorem makes the whole address right with probability at most $(2/3)^r$. Since the planted column is unknown, a classical algorithm has to spend about $L$ queries in a constant fraction of the $m$ columns. As $4-2/k<4$, Section 6 fixes $\alpha<4$ first, then one $k>2/(4-\alpha)$, and only then lets $m$ grow.

Pointer functions, introduced by Göös, Pitassi and Watson [-@GPW2018] and developed by Ambainis and coauthors [-@ABBLSS2017], gave a nearly quartic separation between deterministic and quantum query complexity. For bounded-error randomized complexity, Aaronson, Ben-David and Kothari introduced cheat sheets and reached the power $5/2$ [-@ABK2016]. They observed that their method turns any partial function with nearly linear randomized cost and polylogarithmic quantum cost into a cubic separation. Tal reached $8/3-o(1)$ [-@Tal2020], and Bansal and Sinha [-@BansalSinha2021], and independently Sherstov, Storozhenko and Wu [-@SSW2023], supplied such a partial function and reached $3-o(1)$.

Let us see why that route stops at three. The cheat-sheet function composes a partial function $g$ on $n$ bits with AND-OR on $n^2$ bits [@ABK2016, §3.1]. AND-OR is there because its small certificates make it cheap to certify that an input of the composed function is promised. Its price is the outer cost: $R\approx R(g)\cdot n^2$ while $Q\approx n$. Since $R(g)\lesssim n\approx Q$, the partial function contributes one factor of $Q$ and AND-OR the other two. In $F_{k,m}$ each partial-function input has about $m$ bits while the quantum algorithm spends about $\sqrt m$ queries, so $L\approx Q^2$, and the search over $m\approx Q^2$ columns supplies two more factors.

This account is written for a graduate student who knows the query models above, as set out in §3 of the survey by Buhrman and de Wolf [-@BuhrmanDeWolf2002]. We also use Grover search and amplitude amplification when only a lower bound on the success probability is known, which chapter 7 of de Wolf's lecture notes [-@deWolf2026] covers, together with the uncomputation that runs a reversible circuit backwards to clean its workspace; Appendix B of the notes gives the Markov and Chernoff bounds we need. Finally, we use Yao's minimax principle [-@Yao1977] and conditional probability along the branches of a decision tree. By the end, the reader should be able to build the function on a four-column board, run the quantum tournament on it by hand, and explain why a classical algorithm must pay for an address in a constant fraction of the columns.

Section 1 computes $k$-fold Forrelation on three eight-bit inputs, and Section 2 builds the total function on a four-column board that carries every later example. Section 3 states the facts about Forrelation that the bounds use. In Section 4 a column can beat every rival and still fail to win, and losers can beat each other in a cycle, yet a weighted sampler lists the winner. Section 5 plants a winner in a random column, Section 6 assembles the exponent, and Section 7 describes the Lean statement. A course on quantum algorithms can read Sections 1–4 and 6, and a course on lower bounds Sections 1–3, 5 and 6, each taking the other bound as given. The boxed proof may be skipped, and the questions in the text have answers at the end. Complete proofs of every step are in the [long reasoning record](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md), and the [expert companion](https://github.com/wcook04/quartic-query-lean/blob/main/docs/expert_companion.md) gives a shorter account for specialists, with more comparison to earlier constructions.

# 1. Three eight-bit inputs

We begin with the partial function at its smallest size, $k=2$ and $m=4$, where every value can be checked by hand. An input has two blocks of four bits, and a bit $x$ stands for the sign $(-1)^x$, so $0$ means $+1$ and $1$ means $-1$. With coordinates ordered $00,01,10,11$, let
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
The partial function $P=P_{2,4}$ takes the value $1$ when $\Phi\ge\delta$ and $0$ when $|\Phi|\le\delta/2$; every other input lies outside its promise. In particular, a large **negative** value of $\Phi$ is outside the promise.

Consider the three inputs
$$
a^+=0111\,1000,\qquad a^0=0100\,1000,\qquad a^-=1000\,1000.
$$
They share the second block $g=(-1,1,1,1)$, for which $Wg=(2,-2,-2,-2)$. Their first blocks $(1,-1,-1,-1)$, $(1,-1,1,1)$ and $g$ have inner products $8$, $0$ and $-8$ with $Wg$, so $\Phi(a^+)=1$, $\Phi(a^0)=0$ and $\Phi(a^-)=-1$. Thus $P(a^+)=1$, $P(a^0)=0$, and $a^-$ is outside the promise.

Let us read $\Phi$ geometrically. Write $u=\tfrac12(1,1,1,1)$ and $H=W/2$, the Walsh transform scaled to preserve length. Then $\Phi=\langle z_1/2,\,Hz_2/2\rangle$ measures how well the first sign pattern matches the Walsh transform of the second. Here $Hg/2=\tfrac12(1,-1,-1,-1)$. The first block of $a^+$ matches it exactly, the first block of $a^-$ matches it with every sign reversed, and the first block of $a^0$ is orthogonal to it.

The same number is the amplitude of a two-query experiment. Start in $u$, apply the signs $z_2$ with one query, apply $H$, apply the signs $z_1$ with a second query, and project onto $u$. Since $\Phi=u^{\mathsf T}D_{z_1}HD_{z_2}u$, this **projection experiment** succeeds with probability $\Phi^2$. On our three inputs the probabilities are $1$, $0$ and $1$, so a single run happens to decide them. That is a feature of the chosen inputs: the one-input $1111\,1000$ has $\Phi=1/2$, and one run accepts it with probability only $1/4$. Section 3 repeats the experiment to separate the two sides of the promise.

The experiment accepts $a^-$ with certainty, just as it accepts $a^+$. This is harmless for $P$, which owes no answer on $a^-$. It matters as soon as $P$ sits inside a total function, which must answer on every input: there a cheap quantum test may accept an input that an exact certificate has to reject.

Of all $256$ inputs, $104$ are one-inputs, $48$ are zero-inputs and $104$ lie outside the promise ([record §3.5](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#forr_small_instance)). At this size the classical bound is empty, since $L_{2,4}=\lfloor 2/4\rfloor=0$, so the example tests conventions only. Section 2 repairs the acceptance of $a^-$ with a domain bit.

# 2. One column, then four

A total function must answer on every input, including inputs outside the promise of $P$. The construction gives every column an array of certificates, addressed by the answers to $r$ instances of $P$. We describe one column in general, then a four-column board.

**One column.** Fix $k\ge2$, let $m=4^t$ and $\ell=\log_2m$. The input has $m$ columns, and column $i$ holds

- a string $X_i\in\{0,1\}^m$;
- $r$ inputs $A_{i,1},\dots,A_{i,r}$ to the partial function $P=P_{k,m}$, each of $km$ bits;
- an array of $2^r$ cells $B_{i,s}$, one for each $s\in\{0,1\}^r$.

Every bit is an input bit, and every assignment is allowed. When all of its $A_{i,h}$ are promised, column $i$ has the **address** $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$. Each cell holds $r$ circuit transcripts, described below, and one $\ell$-bit pointer $p_{i,s,j}$ into each other column $j$.

![One column of $F_{k,m}$, drawn for a winning column $i^\star$. The answers to the $r$ address inputs select one of $2^r$ cells; in a winner, that cell certifies the answers and points to a zero in every other column.](figures/exposition/fig1_column.svg){width=94%}

Column $i$ **wins** at address $s$ when four conditions hold: $X_i$ is all ones; every $A_{i,h}$ is promised with $P(A_{i,h})=s_h$; every transcript in $B_{i,s}$ is correct; and every pointer $p_{i,s,j}$ reaches a zero of $X_j$. The total function is $F(y)=1$ exactly when some column wins at some address. At most one column can win, since a pointer from one winner would have to find a zero in the all-one string of the other, and within a column the promised values fix the address.

The addressing comes from the cheat sheets of Aaronson, Ben-David and Kothari, who store a certificate at the address formed by the answers to independent partial-function instances [-@ABK2016, §3.1]. They used about $10\log n$ copies; we take $r=20\log_2m$. This length makes a guessed address hopeless even after many attempts: in Section 5 the chance $(2/3)^r\le m^{-10}$ that one guess is right survives a union bound over every query of a classical algorithm. A quantum algorithm still decodes an address with polylogarithmically many queries, and the array has $2^r=m^{20}$ cells, polynomially many. The all-one column whose certificate points to zeros elsewhere descends from pointer functions: Göös, Pitassi and Watson reach those zeros through a chain of pointers [-@GPW2018], and direct pointers to a zero in every other column appear in the work of Ambainis and coauthors [-@ABBLSS2017]. The new combination is an addressed cell array in every column with direct outward pointers in every cell, which the tournament of Section 4 exploits.

**Four columns.** Now take $m=4$ and $k=2$. To keep the cells few, each column has only $r=2$ address inputs, and a pointer has two bits, read as $00,01,10,11\mapsto$ positions $1,2,3,4$. The definitions of winning, of the local tests below and of the comparisons in Section 4 are unchanged. The board lacks the address length and the hardness that Sections 5 and 6 need, so it illustrates only the definitions and the algorithm. Set
$$
(X_1,X_2,X_3,X_4)=(1111,\ 0111,\ 1011,\ 1101).
$$
Columns $1,3,4$ have address inputs $(a^+,a^0)$, so their address is $10$; column $2$ has $(a^-,a^0)$ and no address. In every cell, the pointer into column $2$ names position $1$, the pointer into column $3$ position $2$ and the pointer into column $4$ position $3$; a pointer into column $1$ names the position encoded by the cell's own address. Every transcript is the true evaluation of a fixed $180$-gate circuit.

![The four-column board. Column 1 wins at address 10: its pointers reach $X_2[1]=X_3[2]=X_4[3]=0$. The dashed pointer from column 3's own true cell lands on a one, as every pointer into column 1 must.](figures/exposition/fig2_board.svg){width=92%}

Column $1$ wins at $10$ (Figure 2); every other column has a zero in its own string, so $F=1$.

**Transcripts.** Fix a circuit $C$ of fan-in two that outputs a domain bit $d$ and a value bit $b$, with $(d,b)=(1,P(a))$ on promised inputs $a$ and $(0,0)$ otherwise. The circuit is fixed and public, part of the definition of $F$; only its proposed gate values are stored in the input. A transcript proposes a value for every gate, and it satisfies all gate equations exactly when it equals the true evaluation: by induction along the gate order, each gate's predecessors already agree with the evaluation, so its own value is forced. This holds on every input, promised or not, so a winning cell certifies the promise through its domain bits and the address through its value bits. For $P_{2,4}$, Shannon expansion of the truth tables gives such a circuit with $180$ gates, which outputs $(1,1)$ on $a^+$, $(1,0)$ on $a^0$ and $(0,0)$ on $a^-$. Its gate list and a short script checking every count on this board are linked from [record §4.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#AC-example-tests).

**The domain bit is needed.** Let us change the board: set $X_1=0111$ and $X_2=1111$, and make every pointer into column $1$ name position $1$. Column $2$ is now all ones. At address $00$ its stored value bits $(0,0)$ agree with the address, its pointers find zeros in the other three columns, and every gate equation holds, because the transcripts are true evaluations. Its first domain bit is $0$, since $a^-$ is unpromised, so column $2$ does not win, and $F=0$. A function that checked only value bits would accept this board.

**Local tests.** Let us break the winning condition into small tests, each reading a few bits. There are $m$ tests that the bits of $X_i$ are ones; $m-1$ pointer tests, each reading the $\ell$ bits of a pointer $p_{i,s,j}$ and then the bit of $X_j$ they name; $rS$ gate tests for a circuit of size $S$, each reading one proposed gate value and the two values feeding it; and $2r$ output tests, that each domain bit is $1$ and each value bit equals $s_h$. On Figure 2, for example, the pointer test from $(1,10)$ into column $2$ reads the bits $00$ of $p_{1,10,2}$, then reads $X_2[1]=0$, and passes after $\ell+1=3$ queries. So a candidate $(i,s)$ has
$$
K=2m-1+r(S+2)
$$
tests, each reading at most $\max(3,\ell+1)$ bits, and they all pass exactly when $(i,s)$ wins. A nonwinner therefore fails at least one test at every address. On the board $K=4+3+2(180+2)=371$. At $(1,10)$ every test passes, and at column $1$'s other three addresses a value test fails. On the changed board, $(2,00)$ fails only its domain test, which is why the domain tests must be on the list.

[]{#question-1}**Question 1.** On the changed board, which of column $2$'s tests fail at each of its four addresses? ([Answer](#answer-1).)

# 3. The general partial function

The construction uses $k$-fold Forrelation through three facts, which we now state. For general $k$ and $m=4^t$, index each of $k$ sign blocks by $\{0,1\}^{2t}$, and let $W_{ab}=(-1)^{a\cdot b}$, $H=W/\sqrt m$, $u=(1,\dots,1)/\sqrt m$, and $D_z$ the diagonal matrix of signs $z$. Then $k$-fold Forrelation [@AA2018] is
$$
\Phi(z_1,\dots,z_k)=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,\qquad \delta=2^{-5k},
$$
and $P_{k,m}$ is defined by the thresholds $\delta$ and $\delta/2$ as before [@BansalSinha2021]. Since $H$ and each $D_z$ preserve length, $|\Phi|\le1$.

*A cheap quantum decoder.* The projection experiment of Section 1 extends to every $k$. Applying one sign diagonal costs one query by phase kickback, and the Walsh transforms cost none, so one run uses $k$ queries and succeeds with probability $\Phi^2$. On the promise, this probability is at least $c=\delta^2$ or at most $c/4$. Repeating it $\rho=\lceil16c^{-1}\ln(1/\eta)\rceil$ times and accepting when at least $\rho c/2$ runs succeed decides $P$ with error at most $\eta$, by a Chernoff bound, using $O_k(\log(1/\eta))$ queries on every input.

*An exact circuit.* Because $\Phi$ has two boundary factors and $k-1$ internal factors of $m^{-1/2}$, $\Phi=N/2^{t(k+1)}$ for an integer $N$, which $k-1$ integer Walsh transforms compute with entries of $O_k(\log m)$ bits. The promise becomes two integer comparisons, $p_1=[2^{5k}N\ge2^{t(k+1)}]$ and $p_0=[2^{5k+1}|N|\le2^{t(k+1)}]$, with output $(d,b)=(p_1\lor p_0,\,p_1)$. A fast Walsh transform and ripple-carry arithmetic give a circuit of fan-in two with $S\le200(k+1)^2m(\log_2m)^2$ gates.

*Classical hardness.* For fixed $k$ and all sufficiently large $m$,
$$
R(P_{k,m})>L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor .
$$
This is the randomized lower bound of Bansal and Sinha for this one-sided promise [-@BansalSinha2021, Theorem 1.3 and Corollary 1.4].

With these choices the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. For the board of Section 2, with $r=2$ and $S=180$, the same formula gives $4\,(4+16+4(6+360))=5936$ bits. Both bounds concern this one function, with the same circuit.

# 4. The quantum algorithm: a tournament

The quantum algorithm has to find the winner, if there is one, among $m$ columns, and a direct search costs too much. Checking that one column wins means reading its $m$ string bits and following its $m-1$ pointers, which costs about $\sqrt m$ quantum queries, so a Grover search over $m$ columns with that check inside costs about $\sqrt m\cdot\sqrt m=m$, and would give only $R\approx Q^{2-1/k}$. Instead we compare columns two at a time, at polylogarithmic cost per comparison, search with comparisons, and run the expensive check only on a short list of candidates.

**Comparing two columns.** We decode the $r$ address inputs of each column with error $\varepsilon/r$ each, so that a promised column gets its true address with probability at least $1-\varepsilon$. Then we follow each decoded cell's pointer into the other column and read the bit it names; a zero there disqualifies the column pointed into. If exactly one column is disqualified, the other wins the comparison; otherwise the smaller index wins. Both orders of a pair run the same procedure, so if $a_{ij}$ is the probability that $i$ beats $j$, then $a_{ij}+a_{ji}=1$ for $i\ne j$. A column compared with itself loses without any query, and $a_{ii}=0$.

The comparison runs as a reversible circuit. Its trials, counts and decoded labels stay unmeasured in workspace, the pointers are read at positions computed from those labels, and the outcome goes to a fresh bit, so the comparison is a unitary whose inverse has the same query cost. Distinct decoded labels sit in orthogonal registers, so each outcome has the probability given by the classical rule averaged over decoded labels.

Outward pointers make comparisons against the winner reliable. The winner $i^\star$ has an all-one string, so no pointer from any rival, under any decoded label, finds a zero in it. When $i^\star$'s own address is decoded correctly, its true cell disqualifies the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every rival $j\ne i^\star$, whatever the rival's address inputs are, including inputs outside the promise. Comparisons between two losers obey no such rule.

**A dominating column that does not win.** On the board of Figure 2, change only $p_{1,10,2}$, from position $1$ to position $2$. It now reads $X_2[2]=1$, so column $1$ fails one pointer test and $F=0$. Yet column $1$ still beats every rival under every rival label. Against column $2$ neither column is disqualified and the index rule picks column $1$; against columns $3$ and $4$ its pointers still find zeros. A column that dominates the comparisons is therefore only a candidate, and a final verification is necessary.

**A cycle among losers.** We return to Figure 2 and change three pointers between losers, in every cell of their columns: column $2$'s pointer into column $4$ names position $1$, column $3$'s pointer into column $2$ names position $2$, and column $4$'s pointer into column $3$ names position $1$. Column $1$'s cells are untouched, so it still wins and $F=1$. Each loser's pointer into another loser is now the same in every cell, so these comparisons do not depend on the labels the decoders return. That matters for column $2$, whose input $a^-$ has no true address. Column $2$ beats $3$, column $3$ beats $4$ and column $4$ beats $2$ (Figure 3), so no ordering of the columns agrees with the comparisons, and the search cannot sort them.

![Comparisons on the board with cycled loser pointers. An arrow $i\to j$ means that $i$ beats $j$; a dot in $p_{i,\cdot,j}$ means every cell of column $i$.](figures/exposition/fig3_tournament.svg){width=42%}

Quantum minimum finding [@DH1996] needs a total order, and quantum search with bounded-error inputs [@HMW2003] needs each comparison to compute a fixed predicate with bounded error, whereas two losers may compare with any probability, even $1/2$. King finding [@MPS2023] and the certificate-complexity separations of Ben-David and Kothari [-@BDK2026] and of Ambainis, Iraids and Kokainis [-@AIK2026] also search by comparisons. Our tournament works with the probabilities $a_{ij}$ themselves.

**An ideal process.** To analyse the search we compare it with a random process on weights. The weights are defined from the unknown probabilities $a_{ij}$; the algorithm never computes or estimates them. Start with $w_i=1$ for every column and an empty list, and write $|w|=\sum_iw_i$. While $|w|>0$, a stage chooses a pivot $p$ with probability $w_p/|w|$, appends it to the list, and multiplies each weight by its probability of beating the pivot, $w_i\leftarrow w_ia_{ip}$. The pivot's own weight becomes zero, since $a_{pp}=0$. Once $|w|=0$ the process is absorbed: the weights stay zero and nothing more is appended. On the cycled board, the first stage gives the following weights.

| Pivot $p$ | New weights $(w_1,w_2,w_3,w_4)$ | New $|w|$ |
|---|---|---|
| $1$ | $(0,0,0,0)$ | $0$ |
| $2$ | $(1,0,0,1)$ | $2$ |
| $3$ | $(1,1,0,0)$ | $2$ |
| $4$ | $(1,0,1,0)$ | $2$ |

Pivot $1$ lists the winner and absorbs the process at once. Each pivot has probability $1/4$, so the expected new total is $3/2$, less than half the old total of $4$. In general, pairing the terms $w_iw_pa_{ip}$ and $w_pw_ia_{pi}$ and using $a_{ip}+a_{pi}=1$ gives
$$
\mathbb E\bigl[\,|w'|\;\big|\;w\bigr]=\frac1{|w|}\sum_{i,p}w_iw_pa_{ip}=\frac{|w|^2-\sum_iw_i^2}{2|w|}\le\frac{|w|}2,
$$
which on the cycled board is $(16-4)/8=3/2$; at $|w|=0$ the inequality holds trivially. The identity uses only $a_{ip}+a_{pi}=1$. It holds for cyclic comparisons and for comparisons of probability $1/2$ alike, and after $T$ stages it gives $\mathbb E|w_T|\le m/2^T$.

Meanwhile the winner's weight stays at least $(1-\varepsilon)^T\ge1-T\varepsilon$ until it is chosen. We take
$$
T=\lceil\log_2(1000m)\rceil,\qquad\varepsilon=\frac{1}{1000T}.
$$
Then the winner keeps weight above $1/2$, so the process cannot be absorbed before the winner is listed, and if the winner is still missing after $T$ stages then $|w_T|>1/2$. By Markov's inequality this has probability at most $2m/2^T\le1/500$.

**Sampling a pivot.** The algorithm realises the ideal pivot law without knowing the weights. Suppose pivots $p_1,\dots,p_j$ have been chosen. Prepare a uniform superposition over columns $i$ and, controlled by $i$, run a fresh copy of the comparison of $i$ against each $p_b$, each in its own new registers. Then compute a success flag that is $1$ when $i$ won all of them, and keep every register, so that running the comparison circuits backwards inverts the whole preparation, as amplitude amplification requires. To find the success probability, fix the input, the pivot history and a value of $i$. The comparisons then act on separate fresh registers, so the probability that all of them report a win for $i$ is the product of the $a_{ip_b}$. Different values of $i$ are orthogonal, so these probabilities add:
$$
\Pr(\text{success and column }i)=\frac1m\prod_{b=1}^{j}a_{ip_b}=\frac{w_i}m .
$$
Success has probability $|w|/m$, and conditioned on success the column has exactly the ideal pivot law $w_i/|w|$.

**Amplification with a fixed cap.** Let a preparation succeed with probability $p=\sin^2\theta$, with normalised good part $g$. After $j$ Grover iterations the good component is $\sin((2j+1)\theta)\,g$ [@BHMT2002, Lemma 1], so every successful outcome returns $g$ itself, and conditioning on success keeps the law of the marked label. Since $p$ is unknown, each trial uses a random number of iterations below $\lceil10/\sqrt\gamma\rceil$ for a threshold $\gamma$ [@BBHT1998, Lemma 2]. A fixed number of such trials uses $O(\gamma^{-1/2}\log(1/\eta))$ preparations on every branch, fails with probability at most $\eta$ when $p\ge\gamma$, and fails with certainty when $p=0$ ([record §5.1](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-amplification-proof) gives the constants). The cap does not depend on $p$, and that matters, because the algorithm also runs on inputs where no column wins.

**A stage of the search.** Each stage amplifies the preparation with threshold $\gamma=1/(2m)$ and failure parameter $\varepsilon$, at a cost of $O(\sqrt m\log(1/\varepsilon))$ preparations whatever $|w|$ is. On success we measure the column register, and the outcome becomes the next pivot, a classical value that later preparations use. On reported failure the algorithm stops and passes its current list to verification; it also stops after $T$ pivots. Before the winner is listed its weight exceeds $1/2$, so $|w|/m\ge\gamma$ and a stage fails with probability at most $\varepsilon$. After the winner is listed, $|w|$ may be tiny or zero and the sampler may fail with certainty, but stopping cannot remove a listed column. Coupling the real and ideal processes until the first failure, each stage before the winner is listed adds at most $\varepsilon$ to the chance that they disagree. So the real list misses the winner with probability at most $2m/2^T+T\varepsilon$.

Let us run one stage on the cycled board, after a first pivot $2$, so that the weights are $(1,0,0,1)$. Every address input on the board is $a^+$, $a^0$ or $a^-$, whose projection experiments succeed with probability $1$, $0$ or $1$, so the decoders are exact and the comparisons deterministic. In the preparation, column $1$ and column $4$ beat pivot $2$, column $3$ loses to it, and column $2$ loses to itself without a query. The flag is $1$ on the branches $i=1$ and $i=4$, each of probability $1/4$, so success has probability $1/2\ge\gamma=1/8$ and the conditional law of the column is $(1/2,0,0,1/2)$. Here $\theta=\pi/4$, and $\sin^2((2j+1)\pi/4)=1/2$ for every $j$, so Grover iterations leave the success probability where it is. On success we measure the column and obtain pivot $1$ or pivot $4$, each with probability $1/2$. If it is $1$, the winner is listed, every weight is zero, the next stage fails with certainty, and the list $\{2,1\}$ goes to verification.

[]{#question-2}**Question 2.** Suppose instead that the measured pivot is $4$. Find the new weights, the success probability of a preparation and the next pivot. What does one Grover iteration do here? ([Answer](#answer-2).)

**Verification.** Finally we check each listed column. Decode its address afresh and measure it, then amplify over the $K$ local tests, with threshold $1/K$, to search for a failing test, and accept the column if none is found. The output is $1$ if some candidate is accepted and $0$ otherwise (in particular, $0$ for an empty list). A nonwinner fails some test at every address, including a meaningless label decoded off the promise, so it is accepted with probability at most $\varepsilon$; the changed board of Section 2 shows why the domain tests must be among them. The winner, decoded correctly, fails no test and is accepted. When $F=1$, the output is wrong only if the list misses the winner or the winner's fresh decoding fails, which has probability at most $2m/2^T+T\varepsilon+\varepsilon\le1/250$. When $F=0$, it is wrong only if one of at most $T$ nonwinners is accepted, which has probability at most $T\varepsilon\le1/1000$. Decoding errors inside comparisons are already part of the $a_{ij}$.

**The count.** Let us total the queries. Every number of trials, iterations, stages and comparisons is fixed in advance, so the query bound holds on every input and every branch. A comparison costs $c=O_k(r\log(r/\varepsilon))$ queries for its decoders plus $2(\ell+1)$ for its pointers. At most $T$ stages, each with $O(\sqrt m\log(1/\varepsilon))$ preparations of at most $T$ comparisons, cost $O(c\sqrt m\,T^2\log(1/\varepsilon))$. Verification treats at most $T$ candidates, each with a fresh decoding of $O_k(r\log(r/\varepsilon))$ queries and $O(\sqrt K\log(1/\varepsilon))$ test evaluations of $O(\log m)$ queries, where $K=O_k(m(\log m)^3)$. As $r$, $T$ and $1/\varepsilon$ are $O(\ell)$, crude bounds give $O_k(\sqrt m\,\ell^6)$ for the tournament and $O_k(\sqrt m\,\ell^5)$ for verification ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#upper-explicit-log6)), so
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 ,
$$
with $C_k$ depending only on $k$; the power six is an artefact of this loose count. This is the $\sqrt m$ half of the arithmetic in the introduction.

# 5. The classical lower bound: a planted pair

We now show that $R(F_{k,m})>\lfloor mL/100\rfloor$, by planting a winner in a random column. Fix $k$, let $m$ be large and $L=L_{k,m}<R(P)$. By Yao's minimax principle [-@Yao1977] in its finite form, there is a distribution $\mu$ on promised inputs of $P$ under which every deterministic algorithm making $L$ queries is correct with probability at most $2/3$ ([record §6.2](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-minimax) proves the finite form).

**The pair.** We draw every address input from $\mu$ and, in each column $i$, one position $J_i$ uniformly, all mutually independent. Set $X_i$ to all ones except a zero at $J_i$, and leave every cell blank. This is the **dummy** input $Y^0$, and $F(Y^0)=0$. We then choose a column $I$ uniformly, independently of everything else. The **planted** input $Y^1$ erases the zero $X_I[J_I]$ and fills the true cell $B_{I,s_I}$ with correct transcripts and with pointers to the zeros $J_j$ of the other columns. Column $I$ wins, so $F(Y^1)=1$.

Figure 4 draws the pair on the board of Section 2. The planted cell is column $1$'s cell of Figure 2, but the address inputs are now samples from $\mu$ and every other cell is blank. At $m=4$ there is no hard distribution, so the picture shows only where the two inputs differ.

![The planted pair on the four-column board, with $I=1$ and $J=(4,1,2,3)$. Address inputs are samples from $\mu$ and unplanted cells are blank. The two inputs differ only at $X_1[4]$ and in the cell $B_{1,10}$.](figures/exposition/fig4_planted.svg){width=76%}

Fix a deterministic algorithm $\mathcal A$ making at most $G=\lfloor mL/100\rfloor$ queries. Its runs on $Y^0$ and $Y^1$ follow the same path until it first reads a bit where the inputs differ, and every such bit is the erased zero or lies in the true cell. The run on $Y^0$ does not depend on $I$, which is chosen independently. Hence
$$
\bigl|\Pr[\mathcal A(Y^1)=1]-\Pr[\mathcal A(Y^0)=1]\bigr|
\le\Pr(\text{erased zero hit})+\Pr(\text{true cell visited}),
$$
where both events refer to the run on the dummy input. (Counting every visit to the true cell overcounts, since a filled bit may equal its blank value; that only weakens the bound.)

**The erased zero.** Let $Z$ be the number of columns whose zero the dummy run finds. Given the dummy data, exactly $Z$ of the $m$ choices of $I$ select a found zero, so
$$
\Pr(\text{erased zero hit})=\frac{\mathbb E Z}{m}\le\frac{4G}{m^2}.
$$
To bound $\mathbb EZ$, condition on the whole transcript of the dummy run. The cells are blank and the other fields are independent of the zero positions, so an undiscovered zero is uniform among its column's unread positions. A query to a column with fewer than $m/2$ positions read therefore finds its zero with probability at most $2/m$, giving at most $2G/m$ such discoveries in expectation. Any other discovery needs $m/2$ queries in its column, which happens in at most $2G/m$ columns ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-early-late)).

The identity $\Pr(\text{erased zero hit})=\mathbb EZ/m$ needs $I$ to be independent of the run. Query one fixed position in each of the four columns, so that $\mathbb EZ=1$ and an independent $I$ is hit with probability $1/4$. Suppose instead that $I$ is chosen uniformly among the columns where a zero was found, and uniformly among all four when none was found, which happens with probability $(3/4)^4=81/256$. By symmetry $I$ is still uniform on its own, but now it is hit whenever some zero was found, with probability $1-(3/4)^4=175/256$. A uniform marginal is a weaker condition than independence from the run, and the proof needs independence.

[]{#question-3}**Question 3.** With two fixed positions queried per column, how often is an independent $I$ hit, and how often the dependent one? ([Answer](#answer-3).)

**The true cell.** The algorithm need not compute $s_I$ to reach $B_{I,s_I}$: it may guess an address or visit many cells. But a query in the true cell names, by its position alone, all $r$ hard answers $s_I$, and that is what we show to be unlikely. Call a column **heavy** if the dummy run makes more than $L$ queries, in total, to its $r$ address inputs, and **light** otherwise. At most $G/L$ columns are heavy, so $\Pr(I\text{ heavy})\le G/(mL)$. For each column we bound by $(2/3)^r$ the probability that it is light **and** a fixed query visits its true cell, using a direct product with a separate cap on each instance.

**Direct product with separate caps.** *Let $U_1,\dots,U_r$ be independent samples from $\mu$, and suppose every deterministic algorithm making at most $L$ queries to one sample is correct with probability at most $\beta$. Let an algorithm choose adaptively which sample to query, make at most $L$ queries to **each** $U_h$ on every run, and use coins and side information jointly independent of the whole tuple $(U_1,\dots,U_r)$. Then it outputs all $r$ answers correctly with probability at most $\beta^r$.*

Both hypotheses are needed. Take AND on two independent inputs, each uniform on all four two-bit strings; one query to an input gives $\beta=3/4$. A pooled budget of two queries computes the first answer exactly and guesses $0$ for the second, which is right with probability $3/4>9/16$. For the identity on fair bits $X,Y$ with $L=0$, the side information $X\oplus Y$ is independent of each bit separately, yet the guess $(0,X\oplus Y)$ is right whenever $X=0$, with probability $1/2>1/4$. The separately capped setting goes back to Shaltiel's fair decision trees [-@Shaltiel2003]. The proof below is the conditional-value argument of Drucker's Lemmas 3.1–3.2, whose headline theorem uses one global budget instead [-@Drucker2012, §1.3 and the end of §3].

::: {.aside title="Proof of the direct product"}
Fix the coins and side information. By joint independence the samples are still independent with law $\mu$, and the algorithm is a deterministic tree. Take a history $\tau$ of queries and answers that occurs with positive probability. Each recorded answer constrains only its own sample, and because the tree is deterministic, every tuple that agrees with these answers asks exactly these queries. So the tuples consistent with $\tau$ form a product $E_1(\tau)\times\dots\times E_r(\tau)$, and given $\tau$ the samples are independent with laws $\mu(\cdot\mid E_h(\tau))$. Let $q_h(\tau)$ count the queries to $U_h$ in $\tau$, and let $V_h(\tau)$ be the best probability of computing $P(U_h)$ under $\mu(\cdot\mid E_h(\tau))$ with at most $L-q_h(\tau)$ further queries. If the next query reads a bit of $U_h$, then querying it and continuing optimally is one strategy with that allowance, so averaging over the answer $b$,
$$
\sum_b\Pr(b\mid\tau)\,V_h(\tau b)\le V_h(\tau).
$$
One answer may raise $V_h$; only the average cannot. For the two uniform AND inputs above with caps of one query, $V_1=V_2=3/4$ at the start; reading the first bit of $U_1$ makes $V_1=1$ or $1/2$ as the bit is $0$ or $1$, and $V_2$ stays $3/4$, so the product averages to $\tfrac12\cdot\tfrac34+\tfrac12\cdot\tfrac38=\tfrac9{16}$, its starting value. In general the other samples keep their laws and allowances, so their values do not change, and $\prod_hV_h$ has nonincreasing expectation from step to step. It starts at most $\beta^r$. At a leaf with output $s$, the probability of being right given $\tau$ is $\prod_h\Pr(P(U_h)=s_h\mid\tau)\le\prod_hV_h(\tau)$. Averaging over leaves and then over the coins and side information finishes the proof; since a capped algorithm has finitely many deterministic behaviours, arbitrary independent randomness reduces to a finite mixture of them.
:::

**Why the event must be joint.** A run that stays light behaves like a capped algorithm, but it need not succeed with probability at most $\beta^r$ given that it stays light. Take $P=\text{AND}$ on the three promised inputs $01,10,11$, uniformly; any one-query algorithm is right with probability at most $\beta=2/3$. Read the first bit, output $0$ if it is $0$, and otherwise read the second bit. This algorithm stays within one query exactly on input $01$, where it is right, so its success given that it stays light is $1$. The true statement concerns the joint event: being right **and** staying within the caps has probability $1/3\le\beta$.

**The simulator.** Fix a column $i$ and a query time $j\le G$. A simulator is given everything except the address inputs of column $i$: all zero positions, the other columns' address inputs and the blank cells, which are jointly independent of column $i$'s tuple. It runs the dummy algorithm, answering other queries itself and forwarding queries to column $i$'s address inputs, and it stops before the $(L+1)$-st forwarded query. If the run reaches time $j$ and the $j$-th query lies in a cell $B_{i,s}$, the simulator outputs $s$, read off from the position of that query without reading the cell; otherwise it outputs a fixed address.

Three budgets are in play. The dummy algorithm makes at most $G$ queries in all. The simulator makes at most $L$ queries to column $i$'s address inputs in total, which is also the threshold for heaviness. The direct product asks for at most $L$ queries to each of the $r$ instances. The second implies the third, since a total of $L$ is at most $L$ on each instance (the direct product would even allow $rL$). So on every run the simulator meets the hypotheses of the direct product, and its output, learned or guessed, is the true address with probability at most $(2/3)^r$. Whenever column $i$ is light and the $j$-th dummy query visits its true cell, the simulator has not stopped and outputs $s_i$. Hence
$$
\Pr(i\text{ light and query }j\text{ visits }B_{i,s_i})\le(2/3)^r ,
$$
with lightness inside the probability. ([Record §6.5](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#CL-simulator) traces the simulator, including a run where it stops, on a four-column XOR example with $L=1$ and positions numbered from $0$.) Summing over $j\le G$ gives $G(2/3)^r$ for each fixed column. Averaging over the independent uniform $I$ divides the sum over the $m$ columns by $m$, so no factor $m$ appears, and adding the heavy case gives
$$
\Pr(\text{true cell visited})\le\frac{G}{mL}+G\left(\frac23\right)^r .
$$

**Finishing.** The gap is at most $4G/m^2+G/(mL)+G(2/3)^r$. With $r=40t$ and $m=4^t$, the inequality $(2/3)^2\le1/2$ gives $(2/3)^r\le m^{-10}$, and $G\le mL/100\le m^2/100$, so the gap is at most $4/100+1/100+1/(100m^8)<1/3$. A randomized algorithm computing $F$ with $G$ queries would have gap at least $1/3$, yet it is an average of deterministic algorithms whose gaps are each below $1/3$. So
$$
R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor .
$$
Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm. This is the $m\cdot L$ half of the arithmetic.

# 6. Exponent four, and the order of quantifiers

Let us combine the two bounds. Insert $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$ and use $\lfloor x\rfloor\ge x/2$ for real $x\ge1$, once for $L$ and once for $mL/100$. Both are at least $1$ once $t\ge8$, since then $m^{1-1/k}/(\log_2 m)^2\ge2^t/(4t^2)\ge1$. So for each fixed $k\ge2$ and all large $m$,
$$
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2},\qquad Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 .
$$
Fix $0\le\alpha<4$, then an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $d=2-1/k-\alpha/2>0$. Since $\alpha\ge0$, the upper bound on $Q$ may replace $Q$ in the denominator, and
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^{\alpha}}\ge c_{k,\alpha}\,\frac{m^{d}}{(\log_2m)^{2+6\alpha}}\longrightarrow\infty .
$$
So no constant $C_\alpha$ works, and $\alpha_{\rm tot}\ge4$. For $\alpha=3$, $k=3$ suffices and refutes the cubic conjecture; $k=2$ gives exactly the cube.

All constants, including $C_k$ and the point from which the Forrelation bound holds, depend on $k$, so a $k$ that grows with $m$ cannot be substituted into these bounds. For example, for each fixed $k$ the condition $t\ge2^k$ holds for all large $t$, yet substituting $k=t$ asks for $t\ge2^t$, which never holds. The argument above chooses $\alpha$ first, then a single $k$, and only then lets $m$ grow.

[]{#question-4}**Question 4.** Which $k$ does the argument choose to show $\alpha_{\rm tot}\ge3.5$? ([Answer](#answer-4).)

The matching upper bound $D(f)=O(Q(f)^4)$ for every total $f$ [@ABKRT2020, Theorem 2], with $R\le D$, rests on Huang's sensitivity theorem [-@Huang2019]; the record reconstructs it with the constant $35^4$ ([record Appendix A](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#R3-A-RESULT)). Hence $\alpha_{\rm tot}=4$.

# 7. The statement in Lean

The theorem has also been proved in the Lean proof assistant. Every definition it needs sits in a single [statement file][statement-file] in the [public repository](https://github.com/wcook04/quartic-query-lean), which imports only Mathlib. There [$R$][def-R] is defined through [finite random mixtures][def-randomized] of [decision trees][def-tree], and [$Q$][def-Q] as the least [query cap][def-querycap], taken over every measurement branch, of a [quantum program][def-adaptive] that reaches the input only through the [bit oracle][def-oracle]. The file also defines [the function $F_{k,m}$][def-F] by [the winning condition][def-wins] of Section 2, and [$\alpha_{\rm tot}$][def-alpha]. It states [four theorems][thm-all]. Three say what the statements above say: $\alpha_{\rm tot}=4$, the failure of every bound $R\le C\,Q^3$, and the Forrelation bound of Section 3. The fourth is the family theorem for some exact circuit realising $P$, with the classical bound in the form $\lfloor mL/100\rfloor<R$ and the power of the logarithm in the quantum bound left unspecified. An independent checker confirms that the [proofs][statement-solution] establish exactly these statements.

What a reader can usefully check is whether the definitions say what is intended. A good place to begin is the second clause of the winning condition, which asks that every address input be promised with the value the address names: it is the clause column $2$ fails on the changed board of Section 2. The record explains [why the definitions of $R$ and $Q$ agree with the usual ones](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/docs/reasoning_record.md#R3-01-CLASSICAL).

# Answers to the questions {.unnumbered}

[]{#answer-1}**[Question 1](#question-1).** String, pointer and gate tests pass. Domain bits $(0,1)$ and value bits $(0,0)$ make the first domain test fail always, and a value test fail wherever the address differs from $00$: one failure at $00$, two at $01$ and $10$, three at $11$.

[]{#answer-2}**[Question 2](#question-2).** Multiplying $(1,0,0,1)$ by $(a_{14},a_{24},a_{34},a_{44})=(1,0,1,0)$ gives $(1,0,0,0)$. A preparation succeeds with probability $1/4\ge\gamma$ and then yields column $1$; with $\theta=\pi/6$, one Grover iteration makes success certain, as $\sin^2(3\pi/6)=1$. Verification then accepts column $1$ from the list $\{2,4,1\}$ and rejects $2$ and $4$ by the zeros in their own strings.

[]{#answer-3}**[Question 3](#question-3).** An independent $I$ is hit with probability $\mathbb EZ/4=1/2$; the dependent choice misses only when no zero is found, so it is hit with probability $1-(1/2)^4=15/16$.

[]{#answer-4}**[Question 4](#question-4).** It needs $k>2/(4-3.5)=4$, so $k=5$, with exponent $4-2/5=3.6>3.5$; as $k=2$ for the cube, $k=4$ gives exactly $3.5$ and does not suffice.

# Use of AI tools {.unnumbered}

The theorem and the construction are OpenAI's [@OpenAI2026]. This exposition and its Lean development were prepared with AI systems under the author's direction.

# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L274-L285
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-adaptive]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L101-L107
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-oracle]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L89-L94
[def-querycap]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L109-L116
[def-randomized]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L46-L60
[def-tree]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L33-L44
[def-wins]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf11e6d1f380f122caa2349d4be78f2c1f/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
<!-- /lean-links -->
