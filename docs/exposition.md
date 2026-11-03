---
title: "Why the exponent is four"
subtitle: "An examples-first account of the nearly quartic separation between randomized and quantum query complexity"
author: "Will Cook"
date: "November 2026"
bibliography: exposition.bib
link-citations: true
---

# Introduction

The optimal power relating randomized and quantum query complexity of total Boolean functions is four [@OpenAI2026, Theorem 1.1]. A quantum algorithm can therefore save almost a fourth power in the number of input bits it needs to inspect, even when it must answer correctly on every possible input. We explain the construction through a four-column example, then prove the two bounds that produce this exponent.

**What a query costs.** Suppose four hidden bits are $0010$, and we want to know whether at least one is $1$. Reading positions $1$, $2$ and $3$ reveals $0$, $0$ and $1$, so we can stop after three queries. The same procedure needs four queries on $0000$. A query asks for one specified input bit; computation between queries, memory and the choice of the next position are free. The input is supplied through this access operation. We do not charge for building a physical oracle or claim a corresponding running-time speedup.

A randomized algorithm can use coins when choosing its queries. A quantum algorithm can apply the bit-reading operation to a superposition of positions; Section 1 gives the precise linear-algebra rule. Write $R(f)$ and $Q(f)$ for the smallest query budgets that compute $f$ with error at most $1/3$. Fix an input first: the probability of error is over the algorithm's coins or measurements. The budget is a **worst-case cap**, valid on every input and every branch, including branches on which the answer is wrong.

For OR on $n$ bits, randomized query complexity is $\Theta(n)$ and quantum query complexity is $\Theta(\sqrt n)$ [@BuhrmanDeWolf2002, §3; @deWolf2026, chapter 7]. This is the familiar quadratic advantage from quantum search. The family below approaches a fourth power.

For a partial function, the algorithm owes a correct answer only on a specified set of inputs, its *promise*. For example, search promised exactly one $1$ excludes the all-zero input, while ordinary OR must handle it. Such problems can have a very large quantum advantage. For a total function, defined on all bit strings of its input length, a polynomial bound is known. The question is the smallest power that works uniformly over all total functions and all input lengths. We write it as
$$
\alpha_{\rm tot}=\inf\bigl\{\alpha\ge0:\ \text{some constant }C\text{ gives }R(f)\le C\,(1+Q(f))^{\alpha}\text{ for every total }f\bigr\}.
$$
The $1+Q$ convention includes constant functions without exceptional cases.

**Theorem** [@OpenAI2026, Theorem 1.1]. $\alpha_{\rm tot}=4$. For every fixed integer $k\ge2$ there are total functions $F_{k,m}$, for all sufficiently large powers of four $m$, such that
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
\qquad
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2}.
$$
Here $C_k$ and the starting value of $m$ may depend on $k$. The explicit logarithm and coefficient are loose counts from the argument below. The source preprint asserts the nearly quartic separation without fixing them.

The construction has $m$ columns; its total number of input bits is much larger. One column may contain a valid certificate: stored data that, together with queried input bits, proves that this column wins. The certificate is hidden at an address given by several hard partial-function answers. A quantum algorithm can decode these addresses cheaply. It compares columns, builds a short list, and checks the certificates only for that list. The classical lower bound plants a certificate in a random column. A classical algorithm may spend enough queries to learn useful information about that column, or it may guess the cell without learning its address. The proof bounds both possibilities, as well as the chance of finding the one string bit changed by planting.

Ignoring logarithmic factors only for this calculation, the bounds have the form
$$
Q\ \lesssim\ \sqrt m,\qquad R\ \gtrsim\ m\,m^{1-1/k}
       = (\sqrt m)^{4-2/k}.
$$
These are an upper bound for $Q$ and a lower bound for $R$, not matching estimates for either measure. A fixed $k$ excludes every universal power below $4-2/k$; for example, $k=3$ gives the threshold $10/3$. Given any target power below four, we choose $k$ large enough and then let $m$ grow.

The matching universal bound $D(f)=O(Q(f)^4)$, where $D$ is deterministic query complexity, was proved by Aaronson, Ben-David, Kothari, Rao and Tal [-@ABKRT2020]. Since $R\le D$, it also bounds $R$. Their conjecture that $R(f)=O(Q(f)^3)$ is refuted by this family. The construction combines addressed certificates from cheat sheets [@ABK2016] with pointer functions [@GPW2018; @ABBLSS2017]; after building it, we will see why their combination obtains the extra power.

This account assumes finite-dimensional linear algebra, elementary conditional probability and asymptotic notation. It introduces quantum states and measurements in Section 1, phase queries in Section 3, and the amplitude-amplification operation in Section 4. The deeper inputs are stated precisely: the classical hardness of Forrelation, the finite minimax principle, and the universal quartic upper bound. The survey of Buhrman and de Wolf [-@BuhrmanDeWolf2002, §3] develops the query models; de Wolf's notes [-@deWolf2026, chapters 1, 2 and 7] give the quantum background.

Section 1 supplies three small inputs. Section 2 turns them into a total function, including a false certificate that explains why the promise must be checked. Section 3 states the three properties of Forrelation that we need. Sections 4 and 5 prove the quantum upper bound and the classical lower bound, and Section 6 combines them. A reader interested in quantum algorithms can take Section 5's bound as given; a reader interested in lower bounds can take Section 4's bound as given. The optional box proves the direct-product lemma. By the end, the reader should be able to trace a certificate, sample the next tournament pivot, and explain why planting a winner is hard to detect. The [long reasoning record](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md) gives complete proofs; the [expert companion](https://github.com/wcook04/quartic-query-lean/blob/main/docs/expert_companion.md) gives the specialist argument and its relation to the literature.

# 1. Three eight-bit inputs

We begin with the partial function at its smallest size, $k=2$ and $m=4$, where every value can be checked by hand. An input has two blocks of four bits, and a bit $x$ stands for the sign $(-1)^x$, so $0$ means $+1$ and $1$ means $-1$. Write $z_1,z_2\in\{\pm1\}^4$ for the sign vectors of the two blocks. With coordinates ordered $00,01,10,11$, let
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
The partial function $P=P_{2,4}$ takes the value $1$ when $\Phi\ge\delta$ and $0$ when $|\Phi|\le\delta/2$; every other input lies outside its promise. In particular, a large **negative** value of $\Phi$ is outside the promise. At this size $\Phi$ is a multiple of $1/8$, so the promise simply asks whether $\Phi>0$ or $\Phi=0$.

Consider the three inputs
$$
a^+=0111\,1000,\qquad a^0=0100\,1000,\qquad a^-=1000\,1000.
$$
They share the second block $g=(-1,1,1,1)$, for which $Wg=(2,-2,-2,-2)$. Their first blocks $(1,-1,-1,-1)$, $(1,-1,1,1)$ and $g$ have inner products $8$, $0$ and $-8$ with $Wg$, so $\Phi(a^+)=1$, $\Phi(a^0)=0$ and $\Phi(a^-)=-1$. Thus $P(a^+)=1$, $P(a^0)=0$, and $a^-$ is outside the promise.

Let us read $\Phi$ geometrically. Write $u=\tfrac12(1,1,1,1)$ and $H=W/2$, the Walsh transform scaled to preserve length: the rows of $W$ are orthogonal and have squared length $4$, so $H^{\mathsf T}H=I$. Then $\Phi=\langle z_1/2,\,Hz_2/2\rangle$ measures how well the first sign pattern matches the Walsh transform of the second. Here $Hg/2=\tfrac12(1,-1,-1,-1)$. The first block of $a^+$ matches it exactly, the first block of $a^-$ matches it with every sign reversed, and the first block of $a^0$ is orthogonal to it.

**From vectors to a query experiment.** A quantum state is a unit vector. The notation $|j\rangle$ denotes the $j$-th basis vector, so $\sum_j\alpha_j|j\rangle$ is just a vector with coordinates $\alpha_j$. Measuring in that basis returns $j$ with probability $|\alpha_j|^2$. More generally, the probability of projecting a unit vector $v$ onto a unit vector $u$ is $|\langle u,v\rangle|^2$. Input-independent unitary matrices, which preserve inner products, are free operations in the query model.

The bit oracle acts on a position register $j$, an answer bit $b$, and a workspace label $w$ by
$$
O_x|j,b,w\rangle=|j,b\oplus x_j,w\rangle.
$$
Here $\oplus$ is addition modulo two. With $b=0$, a basis-state query records $x_j$ in the answer register; on a superposition the same rule acts linearly. One application costs one query; measuring its result does not reveal all the input bits. Section 3 shows how to use it to apply a diagonal sign matrix $D_z=\operatorname{diag}(z_1,\ldots,z_m)$ in one query.

Start in $u$, apply $D_{z_2}$, then $H$, then $D_{z_1}$. Measuring whether the resulting state lies along $u$ succeeds with probability
$$
\bigl|u^{\mathsf T}D_{z_1}HD_{z_2}u\bigr|^2=\Phi^2.
$$
An input-independent change of basis can send $u$ to a designated basis vector before this measurement. This **projection experiment** uses two queries. On $a^+$, $a^0$, $a^-$ its success probabilities are $1$, $0$, $1$. It distinguishes the two promised examples perfectly. It is not a general decoder after one trial: $1111\,1000$ has $\Phi=1/2$ and succeeds with probability $1/4$. Section 3 repeats the experiment to separate the two sides of the promise.

The experiment accepts $a^-$ with certainty, just as it accepts $a^+$. This is harmless for $P$, which owes no answer on $a^-$. It matters as soon as $P$ sits inside a total function, which must answer on every input: there a cheap quantum test may accept an input that an exact certificate has to reject.

This small example illustrates the sign convention and the promise. The classical query threshold in Section 3 is $L_{2,4}=0$, so it gives no positive-budget separation here. Section 2 will prevent the off-promise response from producing a winning certificate.

# 2. One column, then four

A total function must answer on every input, including inputs outside the promise of $P$. The construction gives every column an array of certificates, addressed by the answers to $r$ instances of $P$. We describe one column in general, then a four-column board.

**One column.** Fix $k\ge2$, let $m=4^t$ and $\ell=\log_2m$. The input has $m$ columns, and column $i$ holds

- a string $X_i\in\{0,1\}^m$;
- $r$ inputs $A_{i,1},\dots,A_{i,r}$ to the partial function $P=P_{k,m}$, each of $km$ bits;
- an array of $2^r$ cells $B_{i,s}$, one for each $s\in\{0,1\}^r$.

Every bit is an input bit, and every assignment is allowed. In particular, stored certificates may be false. When all of its $A_{i,h}$ are promised, column $i$ has the **address** $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$. Each cell holds $r$ circuit transcripts (proposed values of all gates of a fixed circuit) and one $\ell$-bit pointer $p_{i,s,j}$ into each other column $j$. The $r$-bit address selects a cell; an $\ell$-bit pointer stored there selects a row of another column. These are different indices, even though both have length two in our small example.

![The strings of all columns, and the address inputs and cells of a winning column $i^\star$. The answers to the $r$ address inputs select one of $2^r$ cells; in a winner, that cell certifies the answers and points to a zero in every other column, while no pointer can find a zero in the winner's own all-one string.](figures/exposition/fig1_column.svg){width=94%}

Column $i$ **wins** at address $s$ when all four conditions hold:

1. $X_i$ is all ones.
2. Every $A_{i,h}$ is promised, with $P(A_{i,h})=s_h$.
3. Every circuit transcript in $B_{i,s}$ is correct.
4. Every pointer $p_{i,s,j}$ reaches a zero of $X_j$.

The total function is $F(y)=1$ exactly when some column wins at some address. At most one column can win: a pointer from one winner would have to find a zero in the all-one string of another. Within a column the promised values fix the address.

The addressing comes from the cheat sheets of Aaronson, Ben-David and Kothari, who store a certificate at the address formed by the answers to independent partial-function instances [-@ABK2016, §3.1]. They used about $10\log n$ copies; we take $r=20\log_2m$. Under the hard input distribution of Section 5, this length suppresses even repeated guesses made with too few queries: the bound $(2/3)^r\le m^{-10}$ that one guess is right stays negligible after a union bound over all of a classical algorithm's queries (Section 5). A quantum algorithm still decodes an address with polylogarithmically many queries, and the array has $2^r=m^{20}$ cells, polynomially many. The all-one column whose certificate points to zeros elsewhere descends from pointer functions: Göös, Pitassi and Watson reach those zeros through a chain of pointers [-@GPW2018], and direct pointers to a zero in every other column appear in the work of Ambainis and coauthors [-@ABBLSS2017]. The source preprint combines these mechanisms [@OpenAI2026, §2]: every column has its own addressed array, and every cell points directly into every other column. The tournament of Section 4 relies on both. Ambainis and coauthors discuss direct pointers but reject the resulting exponentially large alphabet in their setting. Here each pointer is stored in ordinary bits, and a test pays for those bits: it reads just the indexed pointer it needs, not a whole cell at unit cost.

**Four columns.** Now take $m=4$ and $k=2$. To keep the cells few, each column has only $r=2$ address inputs, and a pointer has two bits, read as $00,01,10,11\mapsto$ positions $1,2,3,4$. The definitions of winning, of the local tests below and of the comparisons in Section 4 are unchanged. The board lacks the address length and the hardness that Sections 5 and 6 need, so it illustrates only the definitions and the algorithm. Set
$$
(X_1,X_2,X_3,X_4)=(1111,\ 0111,\ 1011,\ 1101).
$$
Columns $1,3,4$ have address inputs $(a^+,a^0)$, so their address is $10$; column $2$ has $(a^-,a^0)$ and no address. In every cell, the pointer into column $2$ names position $1$, the pointer into column $3$ position $2$ and the pointer into column $4$ position $3$; a pointer into column $1$ names the position encoded by the cell's own address. Every stored transcript gives the true gate values of a fixed circuit; its $180$ gates will enter the local-test count below.

![The four-column board. Column 1 wins at address 10: its pointers reach $X_2[1]=X_3[2]=X_4[3]=0$. The dashed pointer from column 3's own true cell lands on a one, as every pointer into column 1 must. Blue outlines mark the true cells of columns 3 and 4.](figures/exposition/fig2_board.svg){width=92%}

Column $1$ wins at $10$ (Figure 2); every other column has a zero in its own string, so $F=1$.

**Transcripts.** Fix a circuit $C$ of fan-in two (each gate receives at most two values) that outputs a domain bit $d$ and a value bit $b$, with $(d,b)=(1,P(a))$ on promised inputs $a$ and $(0,0)$ otherwise. The circuit is fixed and public, part of the definition of $F$; only its proposed gate values are stored in the input. A transcript proposes a value for every gate, and it satisfies all gate equations exactly when it equals the true evaluation: by induction along the gate order, each gate's predecessors already agree with the evaluation, so its own value is forced. This holds on every input, promised or not, so a winning cell certifies the promise through its domain bits and the address through its value bits. For $P_{2,4}$, expanding its finite truth table gives such a circuit with $180$ gates, which outputs $(1,1)$ on $a^+$, $(1,0)$ on $a^0$ and $(0,0)$ on $a^-$. The gate list and a finite checker are linked from [record §4.4](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#AC-example-tests). That checker tests the circuit on all 256 inputs, but its named board uses different positive and negative strings, of amplitude $\pm1/2$. Our board uses $a^+$ and $a^-$ of amplitude $\pm1$: the certificate geometry agrees, while the decoder probabilities differ.

**The domain bit is needed.** Let us change the board: set $X_1=0111$ and $X_2=1111$, and make every pointer into column $1$ name position $1$. Column $2$ is now all ones. At address $00$ its stored value bits $(0,0)$ agree with the address, its pointers find zeros in the other three columns, and every gate equation holds, because the transcripts are true evaluations. Its first domain bit is $0$, since $a^-$ is unpromised, so column $2$ does not win, and $F=0$. A function that checked only value bits would accept this board.

**Local tests.** A certificate can be checked by searching for a violated equation, without recomputing the full circuit. For a candidate $(i,s)$, the label $s$ is already known to the tester; reading a stored value to compare with it still costs a query.

There are $m$ string tests, each reading one bit of $X_i$ and checking that it is $1$. The $m-1$ pointer tests each read the $\ell$ bits of a stored pointer and then the bit it names, for $\ell+1$ queries, and check that this final bit is $0$.

For a circuit with $S$ gates, the $r$ transcripts supply $rS$ gate tests. Each reads the proposed gate value and at most two values feeding that gate, so it uses at most three queries. Finally, there are $2r$ output tests: $r$ check that the domain bits are $1$, and $r$ check that the value bits agree with the known address $s$. Each output test reads one stored bit.

For a concrete gate check, use gates $1$ and $2$ of the supplied circuit, whose gate and input indices start at zero. Gate $1$ is the negation of input bit $6$; gate $2$ is the OR of gate $1$ and input bit $7$. On $a^+=01111000$, those two input bits are both $0$, so the correct proposed values are $t_1=t_2=1$. The gate-$2$ test reads the stored $t_1=1$, the actual input bit $x_7=0$, and the stored $t_2=1$, and checks $1=1\lor0$. Changing only $t_2$ to $0$ makes this equation fail. The test does not recompute gate $1$: a separate test checks $t_1=\neg x_6$. A false transcript cannot satisfy every gate equation, by the induction above.

On Figure 2, for example, the pointer test from $(1,10)$ into column $2$ reads the bits $00$ of $p_{1,10,2}$, then reads $X_2[1]=0$, and passes after $\ell+1=3$ queries. So a candidate $(i,s)$ has
$$
K=2m-1+r(S+2)
$$
tests, each reading at most $\max(3,\ell+1)$ bits, and they all pass exactly when $(i,s)$ wins. A nonwinner therefore fails at least one test at every address. On the board $K=4+3+2(180+2)=371$. At $(1,10)$ every test passes, and at column $1$'s other three addresses a value test fails. On the changed board, $(2,00)$ fails only its domain test, which is why the domain tests must be on the list.

[]{#question-1}**Question 1.** On the changed board, which of column $2$'s tests fail at each of its four addresses? ([Answer](#answer-1).)

**Why the earlier construction gave a cube.** In the cheat-sheet construction [@ABK2016, §3.1], a partial function $g$ on $n$ bits is first composed with AND-OR on $n^2$ bits. Write these bits as $n$ rows of $n$ bits. A $1$-certificate selects one $1$ in every row; a $0$-certificate selects one entire zero row. Thus either answer has a certificate of $n$ bits. Certifying the outputs of the inner AND-OR functions lets one certify that the input to $g$ satisfies its promise.

Up to logarithmic factors, this recipe has randomized lower bound $R(g)n^2$ and quantum upper bound $n$ when $g$ has very small quantum cost. Reading all $n$ bits gives $R(g)\le n$, so this calculation reaches at most a cubic separation. Ben-David's earlier Forrelation construction [-@BenDavid2015] and cheat sheets first gave power $5/2$; Tal [-@Tal2020] reached $8/3-o(1)$, and the nearly linear partial-function bounds of Bansal and Sinha [-@BansalSinha2021] and Sherstov, Storozhenko and Wu [-@SSW2023] gave $3-o(1)$. In the present construction, an address instance has about $m$ bits while the quantum search costs about $\sqrt m$. The partial-function hardness can therefore contribute almost two powers of the quantum cost. Section 4 explains how comparisons make that square-root search possible.

# 3. The general partial function

The construction uses $k$-fold Forrelation through three facts, which we now state. For general $k$ and $m=4^t$, index each of $k$ sign blocks by $\{0,1\}^{2t}$, and let $W_{ab}=(-1)^{a\cdot b}$, where $a\cdot b$ is the parity of the coordinatewise binary products, $H=W/\sqrt m$, $u=(1,\dots,1)/\sqrt m$, and $D_z$ the diagonal matrix of signs $z$. Then $k$-fold Forrelation [@AA2018] is
$$
\Phi(z_1,\dots,z_k)=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,\qquad \delta=2^{-5k},
$$
and $P_{k,m}$ is defined by the thresholds $\delta$ and $\delta/2$ as before [@BansalSinha2021]. Since $H$ and each $D_z$ preserve length, $|\Phi|\le1$.

*A cheap quantum decoder.* For any requested error $0<\eta<1/2$, the projection experiment of Section 1 extends to every $k$. To see why one sign diagonal costs one bit query, put the answer register in $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$. Flipping this register multiplies it by $-1$, so
$$
O_x\bigl(|j\rangle|-\rangle\bigr)=(-1)^{x_j}|j\rangle|-\rangle.
$$
By linearity, the position register acquires exactly the diagonal signs; this is *phase kickback*. Thus each sign diagonal costs one query, and the Walsh transforms cost none, so one run uses $k$ queries and succeeds with probability $\Phi^2$. On the promise, this probability is at least $c=\delta^2$ or at most $c/4$. Repeating it $\rho=\lceil16c^{-1}\ln(1/\eta)\rceil$ times and accepting when at least $\rho c/2$ runs succeed decides $P$ with error at most $\eta$, by a Chernoff bound, using $O_k(\log(1/\eta))$ queries on every input. The subscript $k$ permits constants depending on $k$; here the factor $c^{-1}=2^{10k}$ is one such dependence.

*An exact circuit.* There is a fixed circuit of fan-in two, with
$$
S\le200(k+1)^2m(\log_2m)^2
$$
gates, that outputs $(1,P(a))$ on promised inputs and $(0,0)$ otherwise. Its purpose is exact certification, including the promise test. Its near-linear size matters because the verifier will search $rS$ gate tests.

The circuit uses integer arithmetic. The two factors $1/\sqrt m$ in $u$ and the $k-1$ internal Walsh factors give $\Phi=N/2^{t(k+1)}$ for an integer $N$. A fast Walsh transform computes the numerator using additions and subtractions, and integer comparisons decide the two thresholds exactly. The [record's circuit construction](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#forr_circuit) gives the arithmetic and gate count. The quantum verifier checks a stored computation of this circuit; it does not run the entire circuit on each candidate.

*Classical hardness.* For fixed $k$ and all sufficiently large $m$,
$$
R(P_{k,m})>L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor .
$$
This is the consequence of the randomized lower bound of Bansal and Sinha for this one-sided promise [-@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. We take it as an input to this exposition. The underlying distinction is between a global correlation, detected by the interference experiment, and the small amount of evidence available to a shallow classical decision tree. Proving that distinction requires the analytic argument in [record §3.6–§3.16](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#forr_target); the picture alone is not a lower-bound proof.

With these choices the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. Thus the total input length is polynomial in $m$, although much larger than $m$. The comparison is between $R$ and $Q$ for this one function, with the same circuit; neither bound counts the time to read or allocate the whole input.

# 4. The quantum algorithm: a tournament

The quantum algorithm has to find the winner, if there is one, among $m$ columns, and a direct search costs too much. Checking one column means searching its $K$ local tests for a violation, including its string, pointers and circuit transcripts. Suppressing logarithmic factors, this costs about $\sqrt m$ quantum queries, so a Grover search over $m$ columns with that check inside costs about $\sqrt m\cdot\sqrt m=m$, and would give only $R\approx Q^{2-1/k}$. Instead we compare columns two at a time, at polylogarithmic cost per comparison, search with comparisons, and run the expensive check only on a short list of candidates. Start with an empty list, repeatedly sample and append a pivot, stop at a fixed cap or a reported sampling failure, and verify the columns accumulated so far.

**Comparing two columns.** We decode the $r$ address inputs of each column with error $\varepsilon/r$ each, so that a promised column gets its true address with probability at least $1-\varepsilon$. Then we follow each decoded cell's pointer into the other column and read the bit it names; a zero there disqualifies the column pointed into. If exactly one column is disqualified, the other wins the comparison; otherwise the smaller index wins. We order each unordered pair by its indices, run this single experiment, and interpret its winner in the requested order. Thus both orders use the same experiment, so if $a_{ij}$ is the probability that $i$ beats $j$, then $a_{ij}+a_{ji}=1$ for $i\ne j$. A column compared with itself loses without any query, and $a_{ii}=0$.

The comparison runs as a reversible circuit. Each would-be measurement outcome stays in a register; counts and decoded labels are computed from those registers without measuring them. Its trials, counts and decoded labels remain in workspace, the pointers are read at positions computed from those labels, and the outcome goes to a fresh bit, so the comparison is a unitary whose inverse has the same query cost. Because the decoded labels are never erased, branches with different labels stay orthogonal and cannot interfere. The outcome bit therefore has exactly the probability that the classical rule gives when the labels are drawn from the decoders' output distribution, with the input and the pair fixed. Thus the reversible implementation has the stated output law and can also be run backwards.

Outward pointers make comparisons against the winner reliable. The winner $i^\star$ has an all-one string, so no pointer from any rival, under any decoded label, finds a zero in it. When $i^\star$'s own address is decoded correctly, its true cell disqualifies the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every rival $j\ne i^\star$, whatever the rival's address inputs are, including inputs outside the promise. Comparisons between two losers obey no such rule. The procedure defines their comparison probabilities; it need not be estimating an underlying ordered relation.

On our board the decoder outputs are deterministic: $a^+$ and $a^-$ produce label $1$, and $a^0$ produces $0$. Column $2$ therefore returns label $10$, although it has no true address. In the comparison of columns $1$ and $2$, cell $B_{1,10}$ points to $X_2[1]=0$, while $B_{2,10}$ points to $X_1[3]=1$. Only column $2$ is disqualified, so column $1$ wins. This exact behavior is special to the chosen inputs; general comparisons can have any of the probabilities described above.

**A dominating column that does not win.** On the board of Figure 2, change only $p_{1,10,2}$, from position $1$ to position $2$. It now reads $X_2[2]=1$, so column $1$ fails one pointer test and $F=0$. Yet column $1$ still beats every rival under every rival label. Against column $2$ neither column is disqualified and the index rule picks column $1$; against columns $3$ and $4$ its pointers still find zeros. A column that dominates the comparisons is therefore only a candidate, and a final verification is necessary.

**A cycle among losers.** We return to Figure 2 and change three pointers between losers, in every cell of their columns: column $2$'s pointer into column $4$ names position $1$, column $3$'s pointer into column $2$ names position $2$, and column $4$'s pointer into column $3$ names position $1$. Column $1$'s cells are untouched, so it still wins and $F=1$. Each loser's pointer into another loser is now the same in every cell, so these comparisons do not depend on the labels the decoders return. That matters for column $2$, whose input $a^-$ has no true address. Column $2$ beats $3$, column $3$ beats $4$ and column $4$ beats $2$ (Figure 3), so no ordering of the columns agrees with the comparisons, and the search cannot sort them.

![Comparisons on the board with cycled loser pointers. An arrow $i\to j$ means that $i$ beats $j$; a dot in $p_{i,\cdot,j}$ means every cell of column $i$. The rows show the winning pointers, which reach zeros; the three changed reverse pointers described in the text reach ones. The arrows out of column 1 come from its true cell and hold under every rival label.](figures/exposition/fig3_tournament.svg){width=55%}

Quantum minimum finding [@DH1996] needs a total order, and using quantum search with bounded-error inputs [@HMW2003] on these pair orientations would require fixed edge bits computed with bounded error. Two losers may compare with any probability, even $1/2$, so our analysis uses only the identity $a_{ij}+a_{ji}=1$, which holds for every pair, winners and losers alike.

**An ideal process.** To analyse the search we compare it with a random process on weights. The weights are defined from the unknown probabilities $a_{ij}$; the algorithm never computes or estimates them. A weight measures the chance of beating all previously chosen pivots in fresh comparisons, not the chance that the column is a winner. The dominating nonwinner above can retain weight too. Start with $w_i=1$ for every column and an empty list, and write $|w|=\sum_iw_i$. While $|w|>0$, a stage chooses a pivot $p$ with probability $w_p/|w|$, appends it to the list permanently, and multiplies each weight by its probability of beating the pivot, $w_i\leftarrow w_ia_{ip}$. The pivot's own weight becomes zero, since $a_{pp}=0$. Once $|w|=0$ the process is absorbed: the weights stay zero and nothing more is appended. On the cycled board we can compute the first stage directly.

If the first pivot is $1$, every weight becomes zero: the pivot loses to itself and every rival loses to it. The new weight vector is $(0,0,0,0)$ and its total is $0$.

If the first pivot is $2$, only columns $1$ and $4$ beat it, so the new weights are $(1,0,0,1)$. Pivots $3$ and $4$ instead give $(1,1,0,0)$ and $(1,0,1,0)$, respectively. Each of these three weight vectors has total $2$.

Pivot $1$ lists the winner and absorbs the process at once. Each pivot has probability $1/4$, so the expected new total is $3/2$, less than half the old total of $4$. In general, each unordered pair contributes $w_iw_p(a_{ip}+a_{pi})=w_iw_p$, and the diagonal terms vanish because $a_{ii}=0$. Pairing the terms gives
$$
\mathbb E\bigl[\,|w'|\;\big|\;w\bigr]=\frac1{|w|}\sum_{i,p}w_iw_pa_{ip}=\frac{|w|^2-\sum_iw_i^2}{2|w|}\le\frac{|w|}2,
$$
which on the cycled board is $(16-4)/8=3/2$; at $|w|=0$ the inequality holds trivially. The identity uses only $a_{ip}+a_{pi}=1$. The halving is an expectation bound; individual histories may lose weight slowly. It holds for cyclic comparisons and for comparisons of probability $1/2$ alike, and after $T$ stages it gives $\mathbb E|w_T|\le m/2^T$.

Meanwhile the winner's weight stays at least $(1-\varepsilon)^T\ge1-T\varepsilon$ until it is chosen. We take
$$
T=\lceil\log_2(1000m)\rceil,\qquad\varepsilon=\frac{1}{1000T}.
$$
Then the winner keeps weight above $1/2$, so the process cannot be absorbed before the winner is listed, and if the winner is still missing after $T$ stages then $|w_T|>1/2$. Markov's inequality makes the link explicit:
$$
\Pr(\text{winner missing})\le\Pr(|w_T|>1/2)
 \le2\mathbb E|w_T|\le\frac{2m}{2^T}\le\frac1{500}.
$$

**Sampling a pivot.** The algorithm realises the ideal pivot law without knowing the weights. With no previous pivots the success flag is always $1$, so the first pivot is uniform. Now suppose measured pivots $p_1,\dots,p_j$ have been chosen. Every new attempt starts afresh and recomputes comparisons against this classical list. Prepare a uniform superposition over columns $i$ and, controlled by $i$, run a fresh copy of the comparison of $i$ against each $p_b$, each in its own new registers. Then compute a success flag that is $1$ when $i$ won all of them, and keep every register, so that reversing all the preparation gates inverts the whole preparation, as amplitude amplification requires. To find the success probability, fix the input, the pivot history and a value of $i$. The comparisons then act on separate fresh registers, so the probability that all of them report a win for $i$ is the product of the $a_{ip_b}$. Different values of $i$ are orthogonal, so these probabilities add:
$$
\Pr(\text{success and column }i)=\frac1m\prod_{b=1}^{j}a_{ip_b}=\frac{w_i}m .
$$
Success has probability $|w|/m$. When $|w|>0$, conditioning on success gives exactly the ideal pivot law $w_i/|w|$. At $|w|=0$ success is impossible.

**A preparation on the board.** After a first pivot $2$, the weights are $(1,0,0,1)$. In a uniform preparation, columns $1$ and $4$ beat pivot $2$, column $3$ loses to it, and column $2$ loses to itself. Success and label $1$ have joint probability $1/4$, as do success and label $4$. Thus success has probability $1/2$, and the next pivot, conditional on success, is $1$ or $4$ with equal probability.

The same procedure also samples unequal weights. To see the distinction, consider an **abstract comparison matrix**, rather than a new claim about the board. Column $1$ beats every rival with certainty. Among the other columns take $a_{23}=1/3$, $a_{24}=3/4$, $a_{34}=2/5$, and reverse probabilities summing to one. After pivot $2$ the weights, their sum, and the preparation's success probability are
$$
(w_1,w_2,w_3,w_4)=(1,0,2/3,1/4),\qquad |w|=23/12,\qquad p=23/48.
$$
The joint masses of success and each label are $(1/4,0,1/6,1/16)$. Dividing by $23/48$ gives the conditional pivot law $(12/23,0,8/23,3/23)$. The sampler does not choose uniformly among positive weights. These numbers are computed for the analysis; the quantum procedure obtains their law by running the comparisons themselves.

**Amplification with a fixed cap.** A single preparation may rarely succeed. Amplitude amplification increases its chance of success while preserving the conditional pivot law. Here is the linear-algebra reason [@BHMT2002, Lemma 1; @deWolf2026, chapter 7]. For $0<p<1$, write the entire prepared state as
$$
\sqrt p\,g+\sqrt{1-p}\,b
 =\sin\theta\,g+\cos\theta\,b,
$$
where $g$ and $b$ are unit vectors in the success and failure subspaces. Both include the column register and **all** retained workspace. A phase flip on the success flag and a reflection about the prepared state give a rotation in the two-dimensional plane spanned by $g,b$. The latter reflection uses the preparation, its inverse, and a reflection about the starting state. After $j$ Grover iterations the state is
$$
\sin((2j+1)\theta)\,g+\cos((2j+1)\theta)\,b.
$$
The coefficient of $g$ changes, but the relative label probabilities inside $g$ do not. Consequently, whenever success is reported, measuring just the column register gives the same conditional law as before amplification. A possible global sign of $g$ does not affect that law.

Since $p$ is unknown, we cannot choose the best rotation count: too many iterations can rotate past the success direction. A bounded randomized choice of iteration counts avoids this problem [@BBHT1998, Lemma 2]. We use the following form: for $0<\gamma\le1/2$ and $0<\eta<1/2$, the routine has a cap of $O(\gamma^{-1/2}\log(1/\eta))$ calls to the preparation and its inverse, preserves the conditional label law on success, and fails with probability at most $\eta$ whenever $p\ge\gamma$. If $p=0$, it reports failure with certainty. The cap applies for every $p$, including $0<p<\gamma$, where no success guarantee is required. The [bounded amplification proof in record §5.1](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#upper-amplification-proof) gives the trial counts.

On the board after pivot $2$, $p=1/2$ and $\theta=\pi/4$, so $\sin^2((2j+1)\pi/4)=1/2$ for every $j$. This case shows preservation of the label law without improvement of the success probability. The next exercise gives a case in which one iteration does improve it.

**A stage of the search.** Each stage amplifies the preparation with threshold $\gamma=1/(2m)$ and failure parameter $\varepsilon$, at a cost of $O(\sqrt m\log(1/\varepsilon))$ preparations whatever $|w|$ is. On success we measure the column register, and the outcome becomes the next pivot, a classical value that later preparations use. On reported failure the algorithm stops and passes its current list to verification; it also stops after $T$ pivots. Before the winner is listed its weight exceeds $1/2$, so $|w|/m\ge\gamma$ and a stage fails with probability at most $\varepsilon$. After the winner is listed, $|w|$ may be tiny or zero and the sampler may fail with certainty, but stopping cannot remove a listed column. To couple the real and ideal processes, use the same pivot whenever a real stage succeeds: their conditional pivot laws agree. On failure the real process stops. Conditional on each common history before the winner is listed, failure has probability at most $\varepsilon$; summing over at most $T$ stages costs at most $T\varepsilon$. So the real list misses the winner with probability at most $2m/2^T+T\varepsilon$.

Return to the board after pivot $2$. If the next measured pivot is $1$, the winner has been listed and every weight becomes zero. The next stage fails with certainty, and the retained list $\{2,1\}$ goes to verification. A later failure cannot undo this earlier success.

[]{#question-2}**Question 2.** Suppose instead that the measured pivot is $4$. Find the new weights, the success probability of a preparation and the next pivot. What does one Grover iteration do here? Multiply the current weights by the comparison probabilities; do not restart from all ones. ([Answer](#answer-2).)

**Verification.** Finally we check each listed column. Decode its address afresh with error at most $\varepsilon/r$ per instance, hence at most $\varepsilon$ for a promised whole address, and measure it. Then search for a failing local test among the $K$ tests of Section 2. Here the search's success flag means **a violation was found**. If no violation is found, accept the candidate; output $1$ if any candidate is accepted, and $0$ otherwise, including when the list is empty.

A coherent test evaluation works on a superposition of test labels. It computes the next input position reversibly, retains earlier answers, and pads shorter branches to a common query cap. Running the computation backwards then restores its workspace. This implements the same tests using $O(\ell+1)$ bit queries per evaluation; [record §4.6](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#AC-coherent) gives the controlled implementation. No full transcript is read during a single test.

A nonwinner fails some test at **every** address, even a meaningless label decoded off promise. The uniform preparation over tests therefore finds a violation with probability at least $1/K$. Amplifying with threshold $1/K$ and failure parameter $\varepsilon$ bounds false acceptance by $\varepsilon$. On the changed board in Section 2, candidate $(2,00)$ fails exactly its first domain test; that one violation suffices. The dominating nonwinner from this section similarly fails a pointer test. The winner at its correctly decoded address has no violations, so the violation search certainly fails and the verifier accepts it.

When $F=1$, the output is wrong only if the list misses the winner or the winner's fresh decoding fails, with probability at most $2m/2^T+T\varepsilon+\varepsilon\le1/250$. When $F=0$, one of at most $T$ nonwinners must be falsely accepted, with probability at most $T\varepsilon\le1/1000$. Decoder errors within comparisons are already included in the actual probabilities $a_{ij}$.

**The count.** Early stopping and randomized iteration counts make the number of queries depend on the run. The caps are fixed in advance and hold on every input and branch. A comparison uses $O_k(r\log(r/\varepsilon))$ queries for its decoders and $O(\ell+1)$ for its pointers, including the constant overhead of a reversible implementation. We count the tournament first, then verification.

Each stage uses $O(\sqrt m\log(1/\varepsilon))$ preparations, and each preparation makes at most $T$ comparisons. There are at most $T$ stages. Multiplying these three factors bounds the entire tournament by $O(\sqrt m\,T^2\log(1/\varepsilon))$ comparisons.

Verification makes at most $T$ fresh address decodings. For each candidate it searches the $K$ local tests, using $O(\sqrt K\log(1/\varepsilon))$ test evaluations. Thus the list requires $O(T\sqrt K\log(1/\varepsilon))$ test evaluations in all.

Since $r,T,1/\varepsilon=O(\ell)$, $K=O_k(m\ell^3)$, and a test costs $O(\ell)$ queries, loose estimates give $O_k(\sqrt m\,\ell^6)$ for the tournament and $O_k(\sqrt m\,\ell^5)$ for verification ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#upper-explicit-log6)). Therefore
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6.
$$
The exponent six is an artefact of this loose count. The square root comes from sampling a pivot and from checking only a short list; it is the quantum half of the exponent calculation.

# 5. The classical lower bound: a planted pair

We now show that $R(F_{k,m})>\lfloor mL/100\rfloor$, by planting a winner in a random column. Fix $k$, let $m$ be sufficiently large, and put $L=L_{k,m}<R(P)$, with $1\le L\le m$. By Yao's minimax principle [-@Yao1977] in its finite form, there is a distribution $\mu$ on promised inputs of $P$ under which every deterministic algorithm making $L$ queries is correct with probability at most $2/3$ ([record §6.2](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#CL-minimax) proves the finite form). The quantifier matters: one distribution defeats **all** capped deterministic trees, rather than a different distribution for each tree. Minimax converts worst-case hardness against randomized algorithms into this common hard law. The law need not be uniform or efficiently samplable; it is a tool for the analysis, not information given to the algorithm.

**The pair.** We draw every address input from $\mu$ and, in each column $i$, one position $J_i$ uniformly, all mutually independent. Set $X_i$ to all ones except a zero at $J_i$, and set every bit in every cell to zero, which we call **blank**. This is the **dummy** input $Y^0$, and $F(Y^0)=0$. We then choose a column $I$ uniformly, independently of everything else. The **planted** input $Y^1$ erases the zero $X_I[J_I]$ and fills the true cell $B_{I,s_I}$ with correct transcripts and with pointers to the zeros $J_j$ of the other columns. Column $I$ wins, so $F(Y^1)=1$.

Figure 4 draws the pair on the board of Section 2. The planted cell is column $1$'s cell of Figure 2, but the address inputs are now samples from $\mu$ and every other cell is blank. At $m=4$ the stated threshold is $L=0$, so this picture illustrates the locations of the changes, not the positive-budget lower bound. The selected column and its address are visible to the reader of the figure, hidden from the algorithm.

![The planted pair on the four-column board, with $I=1$ and $J=(4,1,2,3)$. Address inputs are samples from $\mu$ and unplanted cells are blank. The two inputs differ only at $X_1[4]$ and in the cell $B_{1,10}$; the plant and its address are revealed to the reader, not to the algorithm.](figures/exposition/fig4_planted.svg){width=76%}

Fixing all the coins of a randomized algorithm gives a deterministic decision tree. We first bound each such tree, then average over the coins. Fix a deterministic algorithm $\mathcal A$ making at most $G=\lfloor mL/100\rfloor$ queries. Its runs on $Y^0$ and $Y^1$ follow the same path until it first reads a bit where the inputs differ, and every such bit is the erased zero or lies in the true cell. The run on $Y^0$ does not depend on $I$, which is chosen independently. Hence
$$
\bigl|\Pr[\mathcal A(Y^1)=1]-\Pr[\mathcal A(Y^0)=1]\bigr|
\le\Pr(\text{erased zero hit})+\Pr(\text{true cell visited}),
$$
where both events refer to the run on the dummy input. (Counting every visit to the true cell overcounts, since a filled bit may equal its blank value; that only weakens the bound.)

**The erased zero.** Let $Z$ be the number of columns whose zero the dummy run finds. Given the dummy data, exactly $Z$ of the $m$ choices of $I$ select a found zero, so
$$
\Pr(\text{erased zero hit})=\frac{\mathbb E Z}{m}\le\frac{4G}{m^2}.
$$
To bound $\mathbb EZ$, condition on the entire transcript prefix immediately before the next query, including earlier queries to every field. The cells are blank and the other fields are independent of the zero positions, so an undiscovered zero is uniform among its column's unread positions. Before its first discovery, a new query in a column with fewer than $m/2$ distinct positions read therefore finds its zero with probability at most $2/m$, giving at most $2G/m$ such discoveries in expectation. A repeat query makes no new discovery. Any other discovery needs $m/2$ queries in its column, which happens in at most $2G/m$ columns ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#CL-early-late)).

The identity $\Pr(\text{erased zero hit})=\mathbb EZ/m$ needs $I$ to be independent of the run. Query one fixed position in each of the four columns, so that $\mathbb EZ=1$ and an independent $I$ is hit with probability $1/4$. Suppose instead that $I$ is chosen uniformly among the columns where a zero was found, and uniformly among all four when none was found, which happens with probability $(3/4)^4=81/256$. By symmetry $I$ is still uniform on its own, but now it is hit whenever some zero was found, with probability $1-(3/4)^4=175/256$. A uniform marginal is a weaker condition than independence from the run, and the proof needs independence.

[]{#question-3}**Question 3.** With two fixed positions queried per column, how often is an independent $I$ hit, and how often the dependent one? ([Answer](#answer-3).)

**The true cell.** The algorithm need not compute $s_I$ to reach $B_{I,s_I}$: it may guess an address or visit many cells. But a query in the true cell names, by its position alone, all $r$ hard answers $s_I$. Choosing that position is free: it already contains a proposed address, unlike a pointer stored in the input whose bits must be read. This proposed address is correct exactly on the true-cell event, and that is what we show to be unlikely. Call a column **heavy** if the dummy run makes more than $L$ queries, in total, to its $r$ address inputs, and **light** otherwise. At most $G/L$ columns are heavy, so $\Pr(I\text{ heavy})\le G/(mL)$. For each column $i$ and each time $j\le G$, we bound by $(2/3)^r$ the probability that $i$ is light **and** the $j$-th dummy query lies in $i$'s true cell, using a direct product with a separate cap on each instance.

**Direct product with separate caps.** *Let $U_1,\dots,U_r$ be independent samples from $\mu$, and suppose every deterministic algorithm making at most $L$ queries to one sample is correct with probability at most $\beta$. Let an algorithm choose adaptively which sample to query, make at most $L$ queries to **each** $U_h$ on every run, and use coins and side information jointly independent of the whole tuple $(U_1,\dots,U_r)$. Then it outputs all $r$ answers correctly with probability at most $\beta^r$.*

Both hypotheses are needed. Take AND on two independent inputs, each uniform on all four two-bit strings; one query to an input gives $\beta=3/4$. A pooled budget of two queries computes the first answer exactly and guesses $0$ for the second, which is right with probability $3/4>9/16$. For the identity on fair bits $X,Y$ with $L=0$, the side information $X\oplus Y$ is independent of each bit separately, yet the guess $(0,X\oplus Y)$ is right whenever $X=0$, with probability $1/2>1/4$. The separately capped setting goes back to Shaltiel's fair decision trees [-@Shaltiel2003]. The proof below is the conditional-value argument of Drucker's Lemmas 3.1–3.2, whose headline theorem uses one global budget instead [-@Drucker2012, §1.3 and the end of §3].

::: {.aside title="Proof of the direct product"}
Fix the coins and side information. By joint independence the samples are still independent with law $\mu$, and the algorithm is a deterministic tree. Take a history $\tau$ of queries and answers that occurs with positive probability. Each recorded answer constrains only its own sample, and because the tree is deterministic, every tuple that agrees with these answers asks exactly these queries. So the tuples consistent with $\tau$ form a product $E_1(\tau)\times\dots\times E_r(\tau)$, and given $\tau$ the samples are independent with laws $\mu(\cdot\mid E_h(\tau))$. Let $q_h(\tau)$ count the queries to $U_h$ in $\tau$, and let $V_h(\tau)$ be the best probability of computing $P(U_h)$ under $\mu(\cdot\mid E_h(\tau))$ with at most $L-q_h(\tau)$ further queries. If the next query reads a bit of $U_h$, then querying it and continuing optimally is one strategy with that allowance, so averaging over the answer $b$,
$$
\sum_b\Pr(b\mid\tau)\,V_h(\tau b)\le V_h(\tau).
$$
One answer may raise $V_h$; only the average cannot. For the two uniform AND inputs above with caps of one query, observing first bit $0$ in $U_1$ gives $E_1=\{00,01\}$ and $E_2=\{00,01,10,11\}$; the second sample is still unrestricted. We have $V_1=V_2=3/4$ at the start; reading the first bit of $U_1$ makes $V_1=1$ or $1/2$ as the bit is $0$ or $1$, and $V_2$ stays $3/4$, so the product averages to $\tfrac12\cdot\tfrac34+\tfrac12\cdot\tfrac38=\tfrac9{16}$, its starting value. In general the other samples keep their laws and allowances, so their values do not change, and $\prod_hV_h$ has nonincreasing expectation from step to step. It starts at most $\beta^r$. At a leaf with output $s$, the probability of being right given $\tau$ is $\prod_h\Pr(P(U_h)=s_h\mid\tau)\le\prod_hV_h(\tau)$. Averaging over leaves and then over the coins and side information finishes the proof; since a capped algorithm has finitely many deterministic behaviours, arbitrary independent randomness reduces to a finite mixture of them.
:::

**Why the event must be joint.** A run that stays light behaves like a capped algorithm, but it need not succeed with probability at most $\beta^r$ given that it stays light. Take $P=\text{AND}$ on the three promised inputs $01,10,11$, uniformly; any one-query algorithm is right with probability at most $\beta=2/3$. Read the first bit, output $0$ if it is $0$, and otherwise read the second bit. This algorithm stays within one query exactly on input $01$, where it is right, so its success given that it stays light is $1$. The true statement concerns the joint event: being right **and** staying within the caps has probability $1/3\le\beta$.

**The simulator.** We convert a visit to the true cell into a predictor of all address bits. Fix a column $i$ and a query time $j\le G$. A simulator is given everything except the address inputs of column $i$: all zero positions, the other columns' address inputs and the blank cells, which are jointly independent of column $i$'s tuple. It runs the dummy algorithm, answering other queries itself and forwarding queries to column $i$'s address inputs, and it stops before the $(L+1)$-st forwarded query. If the run reaches time $j$ and the $j$-th query lies in a cell $B_{i,s}$, the simulator outputs $s$, read off from the position of that query without reading the cell; otherwise it outputs a fixed address. It has a defined output even when it aborts; a default guess may happen to be correct, which only enlarges its success event.

Three budgets are in play. The dummy algorithm makes at most $G$ queries in all. The simulator makes at most $L$ queries to column $i$'s address inputs in total, which is also the threshold for heaviness. The direct product asks for at most $L$ queries to each of the $r$ instances. The second implies the third, since a total of $L$ is at most $L$ on each instance (the direct product would even allow $rL$). So on every run the simulator meets the hypotheses of the direct product, and its output, learned or guessed, is the true address with probability at most $(2/3)^r$. Whenever column $i$ is light and the $j$-th dummy query visits its true cell, the simulator has not stopped and outputs $s_i$. Hence
$$
\Pr(i\text{ light and query }j\text{ visits }B_{i,s_i})\le(2/3)^r ,
$$
with lightness inside the probability. The implication goes one way: the light true-cell visit makes the simulator correct, but a lucky default guess can make the simulator correct without such a visit. This is why its unconditional success probability is an upper bound for the event we need.

A small trace makes the cap concrete. Use the [record's XOR example](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#CL-simulator-example), which changes the partial function to $P(a,b)=a\oplus b$ and numbers columns from $0$. In target column $1$, let the two inputs $(a,b)$ and $(c,d)$ be independent fair bit pairs, and set $L=1$. The dummy algorithm first reads an outside string bit, then $a$. Its third query is outside the target if $a=1$, and reads $c$ if $a=0$. Its fourth query proposes a bit in $B_{1,(a,0)}$.

If $a=1$, the simulator has spent its one target query learning $a$. It answers the third query from its outside information, then reaches the fourth query and outputs $10$, read from the proposed cell position. It does not read the bit in that cell.

If $a=0$, the proposed third query would read $c$, using a second target query. The simulator stops before that query and outputs the default address $00$. Its cap is enforced on this branch as well.

The first branch gives the light true-cell event exactly when $a=1,b=0,c=d$, with probability $1/8$. The simulator is also correct on $a=0,b=0,c=d$, another event of probability $1/8$. Its total success probability is $1/4$, the separate-cap bound $(1/2)^2$ for two fair XOR inputs. Aborting is part of the algorithm; we have not conditioned the input distribution on staying cheap.

[]{#question-4}**Question 4.** Change the $a=0$ branch so that it proposes a query in $B_{1,00}$ at time $3$, before trying to read $c$. Can that run now contribute to the light true-cell event? What is the event's probability if the run stops after the cell query? ([Answer](#answer-4).)

For the general bound, sum over the $G$ possible query times first. For each fixed column, the chance of a light true-cell visit is at most $G(2/3)^r$. Now average over the independent uniform planted column $I$:
$$
\frac1m\sum_{i=1}^m G(2/3)^r=G(2/3)^r.
$$
There is no extra factor of $m$. Adding the heavy-column case gives
$$
\Pr(\text{true cell visited})\le\frac{G}{mL}+G\left(\frac23\right)^r.
$$

**Finishing.** The gap is at most $4G/m^2+G/(mL)+G(2/3)^r$. With $r=40t$ and $m=4^t$, the inequality $(2/3)^2\le1/2$ gives $(2/3)^r\le m^{-10}$, and $G\le mL/100\le m^2/100$, so the gap is at most $4/100+1/100+1/(100m^8)<1/3$. A randomized algorithm computing $F$ with $G$ queries would satisfy
$$
\Pr[\mathcal A(Y^1)=1]\ge2/3,\qquad
\Pr[\mathcal A(Y^0)=1]\le1/3,
$$
because every planted input is a $1$-input and every dummy input is a $0$-input. Subtracting gives a gap of at least $1/3$. But the randomized algorithm is an average of deterministic trees whose gaps are all bounded by the same quantity strictly below $1/3$. So
$$
R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor .
$$
Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm. This is the $m\cdot L$ half of the arithmetic.

# 6. Exponent four, and the order of quantifiers

Let us combine the two bounds. Insert $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$ and use $\lfloor x\rfloor\ge x/2$ for real $x\ge1$, once for $L$ and once for $mL/100$. Both quantities tend to infinity for fixed $k$, so both floor estimates hold once $m$ is sufficiently large. So for each fixed $k\ge2$ and all large $m$,
$$
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2},\qquad Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 .
$$
Fix $0\le\alpha<4$, then an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $d=2-1/k-\alpha/2>0$. Since $\alpha\ge0$, the map $x\mapsto(1+x)^\alpha$ is nondecreasing, so replacing $Q$ by its upper bound can only decrease the ratio, and
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^{\alpha}}\ge c_{k,\alpha}\,\frac{m^{d}}{(\log_2m)^{2+6\alpha}}\longrightarrow\infty .
$$
The positive power $m^d$ outgrows the logarithm: the logarithm of the last factor is $d\log m-(2+6\alpha)\log\log_2m$, which tends to infinity. So no constant $C_\alpha$ works, and $\alpha_{\rm tot}\ge4$. For $\alpha=3$, $k=3$ suffices and refutes the cubic conjecture. For $k=2$ the leading powers have threshold three, but these bounds exclude only powers strictly below three.

All constants, including $C_k$ and the point from which the Forrelation bound holds, depend on $k$, so a $k$ that grows with $m$ cannot be substituted into these fixed-$k$ bounds without additional uniform estimates. The companion and record treat such an extension; it is not needed here. For example, for each fixed $k$ the condition $t\ge2^k$ holds for all large $t$, yet substituting $k=t$ asks for $t\ge2^t$, which never holds. The argument above chooses $\alpha$ first, then a single $k$, and only then lets $m$ grow.

[]{#question-5}**Question 5.** What does $k=4$ prove about $\alpha_{\rm tot}$? Which $k$ makes the displayed argument exclude the endpoint bound $R(f)\le C(1+Q(f))^{3.5}$ itself? ([Answer](#answer-5).)

The matching upper bound $D(f)=O(Q(f)^4)$ for every total $f$ [@ABKRT2020], and hence $R(f)=O(Q(f)^4)$, rests on Huang's sensitivity theorem [-@Huang2019]; its proof is reconstructed in the record ([record Appendix A](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#R3-A-RESULT)). Hence $\alpha_{\rm tot}=4$.

Before leaving the argument, try to explain it using the two examples. Why can the classical algorithm notice the plant only at an erased zero or a changed cell? Why does an early cell guess already propose all the address bits? On the quantum side, why can a dominating column still need verification, and why does keeping every pivot protect a winner found before a later sampling failure? These are the steps that turn the two query bounds into the fourth power.

# 7. The statement in Lean

The changed board of Section 2 gives a concrete way to inspect the formal statement. Open the [winning condition][def-wins] and find the clause requiring each address input to be promised with the value named by its address. It is exactly the clause that rejects the all-one, off-promise column\ $2$. The definitions live in one [statement file][statement-file] importing only Mathlib; it also specifies [$R$][def-R], [$Q$][def-Q], [the total function][def-F] and [$\alpha_{\rm tot}$][def-alpha]. The record explains [their agreement with the usual query models](https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/docs/reasoning_record.md#R3-01-CLASSICAL).

The [four formal theorems][thm-all] establish $\alpha_{\rm tot}=4$, failure of every universal cubic bound, the Forrelation lower bound used here, and the total-function family theorem. The first three have the same conclusions as the corresponding statements above. The formal family theorem asserts the existence of an exact circuit realizing $P$, states the classical bound as $\lfloor mL/100\rfloor<R$, and leaves the logarithmic power in the quantum bound unspecified; the explicit power six is counted in this exposition and the record. Lean checks the [proofs][statement-solution], and Comparator checks them against separately compiled challenge statements. Reading the definitions remains necessary to judge what those statements mean.

# Answers to the questions {.unnumbered}

[]{#answer-1}**[Question 1](#question-1).** String, pointer and gate tests pass. Domain bits $(0,1)$ and value bits $(0,0)$ make the first domain test fail always, and a value test fail wherever the address differs from $00$: one failure at $00$, two at $01$ and $10$, three at $11$.

[]{#answer-2}**[Question 2](#question-2).** Multiplying $(1,0,0,1)$ by $(a_{14},a_{24},a_{34},a_{44})=(1,0,1,0)$ gives $(1,0,0,0)$. A preparation succeeds with probability $1/4\ge\gamma$ and then yields column $1$; with $\theta=\pi/6$, one Grover iteration makes success certain, as $\sin^2(3\pi/6)=1$. Column $1$ passes verification from the list $\{2,4,1\}$. Columns $2$ and $4$ have failed string tests; the bounded-error verifier discovers those failures with its stated high probability, not with certainty.

[]{#answer-3}**[Question 3](#question-3).** An independent $I$ is hit with probability $\mathbb EZ/4=1/2$; the dependent choice misses only when no zero is found, so it is hit with probability $1-(1/2)^4=15/16$.

[]{#answer-4}**[Question 4](#question-4).** Yes. The cell query now occurs after only one target query, so the simulator reaches it and outputs $00$. It is a true-cell query when $a=0,b=0,c=d$, with probability $(1/2)(1/2)(1/2)=1/8$. Including the unchanged $a=1$ branch gives total probability $1/4$. If the algorithm instead reads $c$ afterwards, the whole run becomes heavy; that later query must also be excluded before calling the event light.

[]{#answer-5}**[Question 5](#question-5).** $k=4$ excludes every power strictly below $3.5$, so it proves $\alpha_{\rm tot}\ge3.5$. To exclude the endpoint inequality itself by this argument, take $k>2/(4-3.5)=4$, for example $k=5$. Its threshold is $4-2/5=3.6>3.5$.

# Use of AI tools {.unnumbered}

The theorem and the construction are OpenAI's [@OpenAI2026]. This exposition and its Lean development were prepared with AI systems under the author's direction.

# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean#L274-L285
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-wins]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/c16d5deb2545f1e32a45eb4fa841ebffcdf403a3/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
<!-- /lean-links -->
