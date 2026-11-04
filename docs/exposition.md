---
title: "Why OpenAI’s query separation is nearly quartic"
subtitle: "An examples-first explanation of the optimal randomized–quantum exponent"
author: "Will Cook"
date: "November 2026"
bibliography: exposition.bib
link-citations: true
---

# Introduction

OpenAI proved that the optimal power relating randomized and quantum query complexity of total Boolean functions is four [@OpenAI2026, Theorem 1.1].[^ai] This exposition explains why, starting from a board with four columns. The theorem and construction are OpenAI's; our task is to make the two algorithms' very different access to that board understandable. An accompanying Lean development checks formal statements of the result. Section 7 explains what those checks cover, after the mathematical argument.

We assume finite-dimensional linear algebra, elementary conditional probability and asymptotic notation. By the end, the reader should be able to explain how cheap comparisons replace repeated certificate checks, and why guessing a certificate's address is also covered by the classical lower bound.

**What a query costs.** Suppose four hidden bits are $0010$, and we want to know whether any is $1$. Reading positions $1$, $2$ and $3$ answers yes after three queries; the same procedure needs four queries on $0000$. A query reads one input bit. Computation between queries, memory and the choice of the next position are free. A randomized algorithm may use coins; a quantum algorithm may apply the bit-reading operation to a superposition of positions. Section 1 gives that linear-algebra rule. We count calls to this access operation, not the time to build an oracle or perform the intervening computation.

Write $R(f)$ and $Q(f)$ for the smallest query budgets giving error at most $1/3$ on each input. Fix the input first; error probability is over the algorithm's coins or measurements. A budget is a **worst-case cap**, valid on every input and every branch, including wrong-answer branches. A *total* Boolean function assigns an answer to every bit string of its input length. For a *partial* function, correctness is required only on a specified set, its *promise*; the query cap still holds outside that set. For example, OR restricted to strings with zero or one $1$ is partial. A string with two $1$s is excluded, rather than assigned a third answer.

**Why a fourth power is possible.** Imagine an array of certificate cells attached to each column. A certificate is stored evidence that can be checked by reading input bits. One column may win: it is all ones, and its certificate points to a zero in every other column. The certificate's location is hidden by several hard partial-function answers.

On promised inputs, a quantum algorithm can find those answers cheaply. It does not check every candidate certificate. Instead it compares two columns by following their pointers into each other. A genuine winner defeats any rival with high probability: its outward pointer finds a zero, and no pointer into its all-one column can. These cheap comparisons produce a short list; only then does the algorithm pay to check certificates. This makes the quantum cost about $\sqrt m$, where $m$ is the number of columns.

For the classical lower bound, we hide a winner in an independently chosen column. A small budget cannot reveal much about the hard addresses in many columns. Nor can an algorithm avoid the problem simply by guessing cells: the position of every proposed cell query is a guess of all the address answers. Bounding these guesses and the queries that discover the planted column gives a lower bound of roughly $m$ times the difficulty of one address input. For suitable partial functions that difficulty is nearly $m$, giving nearly $m^2$ against $\sqrt m$.

**Theorem** [@OpenAI2026, Theorem 1.1]. The optimal exponent is $\alpha_{\rm tot}=4$. More concretely, for every fixed integer $k\ge2$, the construction gives total functions $F_{k,m}$ and a constant $C_k>0$ such that, for all sufficiently large powers of four $m$,
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6,
\qquad
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2}.
$$
The logarithm and coefficient are explicit, loose choices in this reconstruction. Ignoring logarithms for the moment, the two powers give $m^{2-1/k}=(\sqrt m)^{4-2/k}$. Choose $k$ large, then keep it fixed while $m$ grows: this rules out every universal exponent below four. Section 6 makes that quantifier argument precise. The matching universal upper bound, due to Aaronson, Ben-David, Kothari, Rao and Tal [-@ABKRT2020], shows that four suffices. Their conjectured cubic bound is therefore false.

Section 1 supplies three eight-bit inputs. Section 2 uses them to build a four-column board and a false certificate, showing why the promise must be checked. Section 3 states the partial-function properties needed at large sizes. Sections 4 and 5 develop the quantum and classical arguments on these examples; Section 6 combines their bounds. The small board illustrates the operations, not the large-size hardness theorem.

Three deeper results are accepted inputs: Forrelation hardness, finite minimax and the universal quartic upper bound. We teach the quantum operations used by the construction. Background is available in Buhrman and de Wolf's survey [-@BuhrmanDeWolf2002, §3] and de Wolf's notes [-@deWolf2026, chapters 1, 2 and 7]. For a shorter route, take one of Sections 4 and 5's bounds as an input: the quantum route develops Questions 1–2, the classical route Questions 1, 3–4. Both rejoin at Section 6 and Question 5. The [long reasoning record](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md) gives full proofs; the [expert companion](https://github.com/wcook04/quartic-query-lean/blob/9d9c444fa65ff78f05e5b7178fbce8375e828a52/docs/expert_companion.md) gives the specialist reconstruction and literature comparisons.

# 1. Three eight-bit inputs

We begin with the partial function at its smallest size, $k=2$ and $m=4$, where every value can be checked by hand. The construction will use the same $m$ for the width of a sign block and the number of columns. An input has two blocks of four bits, and a bit $x$ stands for the sign $(-1)^x$, so $0$ means $+1$ and $1$ means $-1$. Write $z_1,z_2\in\{\pm1\}^4$ for the sign vectors of the two blocks. We need a fixed change of basis that compares one hidden sign pattern with a transform of the other. With coordinates ordered $00,01,10,11$, let
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
The denominator $8=2\cdot2\cdot2$ normalizes both sign vectors and the Walsh matrix: $\Phi=\langle z_1/2,(W/2)(z_2/2)\rangle$. The partial function $P=P_{2,4}$ takes the value $1$ when $\Phi\ge\delta$ and $0$ when $|\Phi|\le\delta/2$; every other input lies outside its promise. In particular, a large **negative** value of $\Phi$ is outside the promise. At this size $\Phi$ is a multiple of $1/8$, so, on promised inputs at this size, the two cases are $\Phi>0$ and $\Phi=0$. The tiny threshold is inherited from the general construction; the examples below lie far from it.

Consider the three inputs
$$
a^+=0111\,1000,\qquad a^0=0100\,1000,\qquad a^-=1000\,1000.
$$
They share the second block $g=(-1,1,1,1)$, for which $Wg=(2,-2,-2,-2)$. Their first blocks $(1,-1,-1,-1)$, $(1,-1,1,1)$ and $g$ have inner products $8$, $0$ and $-8$ with $Wg$, so $\Phi(a^+)=1$, $\Phi(a^0)=0$ and $\Phi(a^-)=-1$. Thus $P(a^+)=1$, $P(a^0)=0$, and $a^-$ is outside the promise.

Let us read $\Phi$ geometrically. Write $u=\tfrac12(1,1,1,1)$ and $H=W/2$, the Walsh transform scaled to preserve length: the rows of $W$ are orthogonal and have squared length $4$, so $H^{\mathsf T}H=I$. Then $\Phi=\langle z_1/2,\,Hz_2/2\rangle$ measures how well the first sign pattern matches the Walsh transform of the second. Here $Hg/2=\tfrac12(1,-1,-1,-1)$. The normalized first block $z_1/2$ of $a^+$ matches it exactly; the normalized first block of $a^-$ has every sign reversed, and that of $a^0$ is orthogonal to it.

**From vectors to a query experiment.** The pure quantum states used here are unit vectors over the complex numbers; this experiment happens to have real amplitudes. The notation $|j\rangle$ denotes the $j$-th basis vector, so $\sum_j\alpha_j|j\rangle$ is just a vector with coordinates $\alpha_j$. Measuring in that basis returns $j$ with probability $|\alpha_j|^2$. More generally, the probability of projecting a unit vector $v$ onto a unit vector $u$ is $|\langle u,v\rangle|^2$. Input-independent unitary matrices, which preserve inner products, are free operations in the query model.

The bit oracle acts on a position register $j$, an answer bit $b$, and a workspace label $w$ by
$$
O_x|j,b,w\rangle=|j,b\oplus x_j,w\rangle.
$$
A register stores one component of the basis label; the tuple $(j,b,w)$ indexes the larger state space. The workspace $w$ can retain an earlier query answer or trial outcome. For example, on $x=0010$, the basis state $|3,0,w\rangle$ becomes $|3,1,w\rangle$. Here $\oplus$ is addition modulo two. With $b=0$, a basis-state query records $x_j$ in the answer register; on a superposition the same rule acts linearly. One application costs one query; measuring its result does not reveal all the input bits. To obtain a phase query, initialize the answer bit to $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$. A flip multiplies this vector by $-1$, so
$$
O_x(|j\rangle|-\rangle)=(-1)^{x_j}|j\rangle|-\rangle.
$$
Thus one bit query applies $D_z=\operatorname{diag}(z(1),\ldots,z(m))$ to the position register; this is *phase kickback*. For the eight-bit example, binary coordinates $00,01,10,11$ mean positions $1,2,3,4$ within a block. Block $h\in\{1,2\}$ and position $j$ address the full input at $4(h-1)+j$. Computing this position uses no queries; reading its bit costs one.

Read the experiment in time order: prepare $u$, apply $D_{z_2}$, then $H$, then $D_{z_1}$, and finally $H$ before measuring. Matrix products below act right to left. Only the two diagonal operations query the input. On $a^+$ these vectors are, in order,
$$
u=\tfrac12(1,1,1,1)\ \longmapsto\ \tfrac12(-1,1,1,1)
\ \longmapsto\ \tfrac12(1,-1,-1,-1)\ \longmapsto\ u.
$$

Measuring whether the resulting state lies along $u$ succeeds with probability
$$
\bigl|u^{\mathsf T}D_{z_1}HD_{z_2}u\bigr|^2=\Phi^2.
$$
A final $H$ sends $u$ to $|00\rangle$, so measuring the computational basis and asking for outcome $00$ performs this test. We call that event projection success, distinct from correctly decoding $P$. This **projection experiment** uses two queries. On $a^+$, $a^0$, $a^-$ its success probabilities are $1$, $0$, $1$. It distinguishes the two promised examples perfectly. It is not a general decoder after one trial. **Projection check.** For $1111\,1000$, calculate the signed amplitude $\Phi$ and then the projection probability. These are different quantities. The [answer](#answer-projection) is separated from the attempt. Section 3 repeats the experiment to separate the two sides of the promise.

The experiment accepts $a^-$ with certainty, just as it accepts $a^+$. This is harmless for $P$, which owes no answer on $a^-$. It matters as soon as $P$ sits inside a total function, which must answer on every input: there a cheap quantum test may accept an input that an exact certificate has to reject.

This small example illustrates the sign convention and the promise. It does not exhibit an asymptotic separation. The lower-bound budget introduced in Section 3 is zero at this size, so it gives no positive-budget separation here. Section 2 will prevent the off-promise response from producing a winning certificate.

# 2. One column, then four

A total function must answer on every input, including inputs outside the promise of $P$. The construction gives every column an array of certificates, addressed by the answers to $r$ instances of $P$. We describe one column in general, then a four-column board.

**One column.** Fix $k\ge2$, let $t\ge1$ be an integer, $m=4^t$ and $\ell=\log_2m$. The input has $m$ columns, and column $i$ holds

- a string $X_i\in\{0,1\}^m$;
- $r$ inputs $A_{i,1},\dots,A_{i,r}$ to the partial function $P=P_{k,m}$, each of $km$ bits (Section 3 defines the general family; here we need only its promise and output);
- an array of $2^r$ cells $B_{i,s}$, one for each $s\in\{0,1\}^r$.

Every bit is an input bit, and every assignment is allowed. In particular, stored certificates may be false. When all of its $A_{i,h}$ are promised, column $i$ has the **address** $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$. Each cell holds $r$ circuit transcripts (proposed gate values of a fixed classical Boolean circuit that computes both domain membership and the answer bit) and one $\ell$-bit pointer $p_{i,s,j}$ into each other column $j$. The $r$-bit address selects a cell; an $\ell$-bit pointer stored there selects a row of another column. These are different indices, even though both have length two in our small example.

![Schematic bit strips (not literal lengths). The strings of all columns, and the address inputs and cells of a winning column $i^\star$. The answers to the $r$ address inputs select one of $2^r$ cells; in a winner, that cell certifies the answers and points to a zero in every other column, while no pointer can find a zero in the winner's own all-one string.](figures/exposition/fig1_column.svg){width=94%}

\Needspace{10\baselineskip}

Column $i$ **wins** at address $s$ when all four conditions hold:

1. $X_i$ is all ones.
2. Every $A_{i,h}$ is promised, with $P(A_{i,h})=s_h$.
3. Every circuit transcript in $B_{i,s}$ is correct.
4. Every pointer $p_{i,s,j}$ reaches a zero of $X_j$.

Writing $y$ for the entire board of input bits, the total function is $F(y)=1$ exactly when some column wins at some address. At most one column can win: a pointer from one winner would have to find a zero in the all-one string of another. Within a column the promised values fix the address.

The addressing comes from the cheat sheets of Aaronson, Ben-David and Kothari, who store a certificate at the address formed by the answers to independent partial-function instances [-@ABK2016, §3.1]. We take $r=20\log_2m$. Under the hard input distribution of Section 5, the joint event that a proposed address is right and its column stays within a fixed query cap has probability at most $(2/3)^r\le m^{-10}$. The stopped simulator proves this bound for adaptive guesses; a union bound then covers the algorithm's query times. A quantum algorithm still decodes an address with polylogarithmically many queries, and the array has $2^r=m^{20}$ cells, polynomially many.

The all-one column whose certificate points to zeros elsewhere descends from pointer functions: Göös, Pitassi and Watson reach those zeros through a chain of pointers [-@GPW2018], and direct pointers to a zero in every other column appear in the work of Ambainis and coauthors [-@ABBLSS2017]. The source preprint combines these mechanisms [@OpenAI2026, §2]: every column has its own addressed array, and every cell points directly into every other column. The tournament of Section 4 relies on both. Ambainis and coauthors discuss direct pointers but reject the resulting exponentially large alphabet in their setting.

Each pointer is stored in ordinary bits, and a test pays for the bits it reads. A cell query means a query to one bit in a cell, never an entire payload at unit cost.

[]{#base-board}**Four columns: the base board.** Now take $m=4$ and $k=2$. To keep the cells few, each column has only $r=2$ address inputs, and a pointer has two bits, read as $00,01,10,11\mapsto$ positions $1,2,3,4$. The definitions of winning, of the local tests below and of the comparisons in Section 4 are unchanged. The board lacks the address length and the hardness that Sections 5 and 6 need, so it illustrates only the definitions and the algorithm. Set
$$
(X_1,X_2,X_3,X_4)=(1111,\ 0111,\ 1011,\ 1101).
$$
Columns $1,3,4$ have address inputs $(a^+,a^0)$, so their address is $10$; column $2$ has $(a^-,a^0)$ and no address. In every cell, the pointer into column $2$ names position $1$, the pointer into column $3$ position $2$ and the pointer into column $4$ position $3$; a pointer into column $1$ names the position encoded by the cell's own address. Every stored transcript gives the true gate values of a fixed circuit; its $180$ gates will enter the local-test count below.

![The four-column board. Column 1 wins at address 10: its pointers reach $X_2[1]=X_3[2]=X_4[3]=0$. The dashed pointer from column 3's own true cell lands on a one, as every pointer into column 1 must. Blue outlines mark the true cells of columns 3 and 4.](figures/exposition/fig2_board.svg){width=92%}

Column $1$ has a promised address $10$, true transcripts, an all-one string and pointers to the other columns' zeros, so it wins and $F=1$. The zeros in the other columns rule out rivals. At a wrong-address cell such as $B_{1,00}$ the gate equations still hold, but the first value bit is $1$ rather than the required $0$.

**Transcripts.** Fix a circuit $C$ of fan-in two (each gate receives at most two values) that outputs a domain bit $d$ and a value bit $b$, with $(d,b)=(1,P(a))$ on promised inputs $a$ and $(0,0)$ otherwise. The circuit is fixed and public, part of the definition of $F$; only its proposed gate values are stored in the input. A transcript proposes a value for every gate, and it satisfies all gate equations exactly when it equals the true evaluation: the circuit is acyclic and its gates are ordered after their predecessors, so by induction along that order, each gate's predecessors already agree with the evaluation, so its own value is forced. This holds on every input, promised or not, so a winning cell certifies the promise through its domain bits and the address through its value bits. For $P_{2,4}$, expanding its finite truth table gives such a circuit with $180$ gates in the supplied truth-table synthesis, which outputs $(1,1)$ on $a^+$, $(1,0)$ on $a^0$ and $(0,0)$ on $a^-$.

[]{#domain-bit-board}**The domain-bit board.** Starting from the base board in Figure 2, set $X_1=0111$ and $X_2=1111$, and make every pointer into column $1$ name position $1$. Column $2$ is now all ones. At address $00$ its stored value bits $(0,0)$ agree with the address, its pointers find zeros in the other three columns, and every gate equation holds, because the transcripts are true evaluations. Its first domain bit is $0$, since $a^-$ is unpromised, so column $2$ does not win, and $F=0$. The address inputs, transcripts and pointers into columns $2,3,4$ are unchanged. A function that checked only value bits would accept this board.

**Local tests.** A certificate can be checked by searching for a violated equation, without recomputing the full circuit. For a candidate $(i,s)$, the label $s$ is already known to the tester; reading a stored value to compare with it still costs a query.

There are $m$ string tests, each reading one bit of $X_i$ and checking that it is $1$. The $m-1$ pointer tests each read the $\ell$ bits of a stored pointer and then the bit it names, for $\ell+1$ queries, and check that this final bit is $0$.

For a circuit with $S$ gates, the $r$ transcripts supply $rS$ gate tests. Each reads the proposed gate value and at most two values feeding that gate, so it uses at most three queries. Gate equations check consistency with predecessors; the output tests additionally require the values that certify a winner. Finally, there are $2r$ output tests: $r$ check that the domain bits are $1$, and $r$ check that the value bits agree with the known address $s$. Each output test reads one stored bit.

\Needspace{8\baselineskip}

For a concrete gate check, use gates $1$ and $2$ of the supplied circuit, whose gate and input indices start at zero. Gate $1$ is the negation of input bit $6$; gate $2$ is the OR of gate $1$ and input bit $7$. On $a^+=01111000$, those two input bits, the seventh and eighth bits in the printed string, are both $0$, so the correct proposed values are $t_1=t_2=1$. The gate-$2$ test reads the stored $t_1=1$, the actual input bit $x_7=0$, and the stored $t_2=1$, and checks $1=1\lor0$. Changing only $t_2$ to $0$ is an allowed input assignment and makes this equation fail. The test does not recompute gate $1$: a separate test checks $t_1=\neg x_6$. A false transcript cannot satisfy every gate equation, by the induction above. As a local check, changing both $t_1,t_2$ to $0$ makes the OR equation pass, but the earlier equation $t_1=\neg x_6$ fail. Gate consistency cannot hide the first false value.

*Optional circuit check.* The gate list and its [256-input circuit truth-table check are in record §4.4](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#AC-example-tests). The circuit truth table, gate identities and local tests transfer unchanged; the checker's separate board has different decoder probabilities, as the linked passage explains.

On Figure 2, for example, the pointer test from $(1,10)$ into column $2$ reads the bits $00$ of $p_{1,10,2}$, then reads $X_2[1]=0$, and passes after $\ell+1=3$ queries. So a candidate $(i,s)$ has
$$
K=\underbrace{m}_{\text{string}}+\underbrace{(m-1)}_{\text{pointer}}+\underbrace{rS}_{\text{gate}}+\underbrace{2r}_{\text{output}}=2m-1+r(S+2)
$$
tests, each reading at most $\max(3,\ell+1)$ bits, and they all pass exactly when $(i,s)$ wins. A nonwinner therefore fails at least one test at every address. On the board $K=4+3+2(180+2)=371$. At $(1,10)$ every test passes, and at column $1$'s other three addresses a value test fails. On the domain-bit board, $(2,00)$ fails only its domain test, which is why the domain tests must be on the list.

[]{#question-1}**Question 1 (promise certification).** On the domain-bit board, make one row for each of column $2$'s four addresses. In each row name the domain and value outputs that fail and count them; no gate indices are required. ([Answer](#answer-1).)

# 3. The general partial function

The construction uses $k$-fold Forrelation through three facts, which we now state. For integers $k\ge2$ and $t\ge1$, put $m=4^t$ and index each of the $k$ sign blocks by $\{0,1\}^{2t}$. The earlier four-coordinate example is $t=1$. Its position register now has $m$ basis states. Define $W_{ab}=(-1)^{a\cdot b}$, where $a\cdot b$ is the parity of the coordinatewise binary products, $H=W/\sqrt m$, $u=(1,\dots,1)/\sqrt m$, and $D_z$ the diagonal matrix of signs $z$. Then $k$-fold Forrelation [@AA2018] is
$$
\Phi(z_1,\dots,z_k)=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u,\qquad \delta=2^{-5k},
$$
and $P_{k,m}$ is $1$ when $\Phi\ge\delta$, $0$ when $|\Phi|\le\delta/2$, and undefined otherwise [@BansalSinha2021]. Since $H$ and each $D_z$ preserve length, $|\Phi|\le1$.

*A cheap quantum decoder.* For any requested error $0<\eta<1/2$, the projection experiment of Section 1 extends to every $k$. Phase kickback uses one query per sign diagonal, so a trial uses $k$ queries and has projection probability $p=\Phi^2$. On the promise, either $p\ge c=\delta^2$ or $p\le c/4$. Start each trial in fresh registers and repeat independently
$$
\rho=\lceil16c^{-1}\ln(1/\eta)\rceil
$$
times; accept if at least $\rho c/2$ projections succeed. We use the following standard Chernoff estimates for the number $Z$ of successes in these independent Bernoulli trials:

| Promised case | Wrong decision | Tail bound used |
| --- | --- | --- |
| $p\ge c$ | $Z<\rho c/2$ | At most $\exp(-\rho c/8)$, hence at most $\exp(-\rho c/16)$. |
| $p\le c/4$ | $Z\ge\rho c/2$ | At most $\exp(-\rho c/16)$, by the upper tail at $p=c/4$ and monotonicity. |

Thus each error is at most $\eta$. The cap is $k\rho=O_k(\log(1/\eta))$ on every input. The subscript permits constants depending on $k$, here including $c^{-1}=2^{10k}$: cheap means fixed $k$ and growing $m$. Section 4 will retain the trial outcomes coherently instead of measuring them; their measurement probabilities and independence remain the same.

*An exact circuit.* There is a fixed circuit of fan-in two, with
$$
S\le200(k+1)^2m(\log_2m)^2
$$
gates, that outputs $(1,P(a))$ on promised inputs and $(0,0)$ otherwise. Its purpose is exact certification, including the promise test. Its near-linear size matters because the verifier will search $rS$ gate tests.

The circuit uses integer arithmetic. The two factors $1/\sqrt m$ in $u$ and the $k-1$ internal Walsh factors give $\Phi=N/2^{t(k+1)}$ for an integer $N$. A fast Walsh transform recursively transforms two half-size vectors, then adds and subtracts their corresponding entries. These split-and-combine steps compute the numerator using additions and subtractions, and integer comparisons decide the two thresholds exactly. For example, $\Phi\ge2^{-5k}$ is equivalent to $2^{5k}N\ge2^{t(k+1)}$; the small-value test is $2^{5k+1}|N|\le2^{t(k+1)}$. Words of $O(k\log m)$ bits suffice, including the threshold shifts. The [record's circuit construction](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#forr_circuit) gives the arithmetic and gate count. The quantum verifier checks a stored computation of this circuit; it does not run the entire circuit on each candidate.

*Classical hardness.* For fixed $k$ and all sufficiently large $m$,
$$
R(P_{k,m})>L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor .
$$
This is the consequence of the randomized lower bound of Bansal and Sinha for this one-sided promise [-@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. For fixed $k$, the source bound is at least a positive constant depending on $k$ times $m^{1-1/k}/(\log_2(km))^{1-1/k}$. Dividing this by the unfloored expression for $L_{k,m}$ gives a factor of order $(\log m)^{1+1/k}$, which tends to infinity and absorbs the constant. We take the hardness theorem as an input to this exposition. A shallow decision tree chooses each next bit from the earlier answers and stops within its query budget. Minimax turns its hardness into a distribution of hidden samples; the algorithm may know that law without being given the sampled bits. The underlying distinction is between a global correlation, detected by the interference experiment, and the small amount of evidence available to a shallow classical decision tree. Proving that distinction requires the analytic argument in [record §3.6–§3.16](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#forr_target); the picture alone is not a lower-bound proof.

A column contains $m$ string bits, $rkm$ address-input bits, and $2^r$ cells, each containing $(m-1)\ell$ pointer bits and $rS$ transcript bits. Thus the general function has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]$ input bits, which is $O_k(m^{22}(\log m)^3)$ since $2^r=m^{20}$. Thus the total input length is polynomial in $m$, although much larger than $m$. The three bracketed contributions are the column string, its address inputs, and its cell array. Here $n$ is the actual input length; $m$ controls the displayed query bounds. The comparison is between $R$ and $Q$ for this one function, with the same circuit; neither bound counts the time to read or allocate the whole input.

# 4. The quantum algorithm: a tournament

The quantum algorithm has to find the winner, if there is one, among $m$ columns, and a direct search costs too much. Checking one column means searching its $K$ local tests for a violation, including its string, pointers and circuit transcripts. Since $K=O_k(m\ell^3)$ and one local test costs $O(\ell)$ queries, verification costs $\sqrt K\,O(\ell)$ up to error-reduction logarithms. Suppressing these logarithmic factors, this is about $\sqrt m$ quantum queries, so a Grover search over $m$ columns with that check inside costs about $\sqrt m\cdot\sqrt m=m$, and would certify only a separation exponent $2-1/k$ from these upper and lower bounds. Instead we compare columns two at a time, at polylogarithmic cost per comparison, search with comparisons, and run the expensive check only on a short list of candidates. The algorithm has four steps.

1. Initialize an empty list.
2. Sample a pivot; on success, measure its column label and append it.
3. Repeat until $T$ pivots have been listed or a stage reports failure.
4. Verify every listed column and accept if one passes.

**Comparing two columns.** We decode the $r$ address inputs of each column with error $\varepsilon/r$ each, so that a promised column gets its true address with probability at least $1-\varepsilon$. Then we follow each decoded cell's pointer into the other column and read the bit it names; a zero there disqualifies the column pointed into. If exactly one column is disqualified, the other wins the comparison; if both are disqualified or neither is, the smaller index wins. We order each unordered pair by its indices, run this single experiment, and interpret its winner in the requested order. Exactly one candidate is declared the winner even in a tie. Reversing the requested order relabels the same experiment law; separate physical calls still start afresh. Thus if $a_{ij}$ is the probability that $i$ beats $j$, then $a_{ij}+a_{ji}=1$ for $i\ne j$. A column compared with itself loses without any query, and $a_{ii}=0$.

The comparison runs as a reversible circuit. A deterministic bit $f(z)$ can be recorded by $|z,b\rangle\mapsto|z,b\oplus f(z)\rangle$, an invertible map. Here $z$ includes the decoder labels and the trial registers from which they were computed. To see why retaining them matters, suppose two orthogonal label-and-workspace states occur with amplitudes $\sqrt p$ and $\sqrt{1-p}$, and the comparison rule gives outputs $1$ and $0$. Copying that rule into a fresh flag gives
$$
\bigl(\sqrt p\,|z_0\rangle+\sqrt{1-p}\,|z_1\rangle\bigr)|0\rangle
\longmapsto
\sqrt p\,|z_0\rangle|1\rangle+\sqrt{1-p}\,|z_1\rangle|0\rangle.
$$
Measuring the flag gives $1$ with probability $p$: the retained labels distinguish the branches, so their squared amplitudes add as in the classical experiment. The same reasoning sums over all decoder outcomes. During forward preparation we retain every trial, count, label and pointer-read answer; no would-be measurement is performed. The full inverse later undoes the flag computation, pointer reads and decoder preparations in reverse order. It acts on all these registers and has the same query cost. Retention during preparation and uncomputation by the full inverse are compatible.

Outward pointers make comparisons against the winner reliable. The winner $i^\star$ has an all-one string, so no pointer from any rival, under any decoded label, finds a zero in it. When $i^\star$'s own address is decoded correctly, its true cell disqualifies the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every rival $j\ne i^\star$, whatever the rival's address inputs are, including inputs outside the promise. Comparisons between two losers obey no such rule. The procedure defines their comparison probabilities; it need not be estimating an underlying ordered relation.

On our board the decoder outputs are deterministic: $a^+$ and $a^-$ produce label $1$, and $a^0$ produces $0$. Column $2$ therefore returns label $10$, although it has no true address. In the comparison of columns $1$ and $2$, cell $B_{1,10}$ points to $X_2[1]=0$, while $B_{2,10}$ points to $X_1[3]=1$. Only column $2$ is disqualified, so column $1$ wins. This exact behavior is special to the chosen inputs; general comparisons can have any of the probabilities described above.

**The false-pointer change: a dominating nonwinner.** On the board of Figure 2, change only $p_{1,10,2}$, from position $1$ to position $2$. It now reads $X_2[2]=1$, so column $1$ fails one pointer test and $F=0$. Yet column $1$ still beats every rival under every rival label. Against column $2$ neither column is disqualified and the index rule picks column $1$; against columns $3$ and $4$ its pointers still find zeros. A column that dominates the comparisons is therefore only a candidate, and a final verification is necessary.

**The cycle change: three losing columns.** We return to Figure 2 and change three pointers between losers, in every cell of their columns: column $2$'s pointer into column $4$ names position $1$, column $3$'s pointer into column $2$ names position $2$, and column $4$'s pointer into column $3$ names position $1$. Column $1$'s cells are untouched, so it still wins and $F=1$. Each loser's pointer into another loser is now the same in every cell, so these comparisons do not depend on the labels the decoders return. That matters for column $2$, whose input $a^-$ has no true address. For the first edge, column $2$ points to $X_3[2]=0$ while column $3$ now points to $X_2[2]=1$, so only $3$ is disqualified. The other two edges are checked the same way: column $2$ beats $3$, column $3$ beats $4$ and column $4$ beats $2$ (Figure 3), so no ordering of the columns agrees with the comparisons, and the search cannot sort them.

![Comparisons on the board with cycled loser pointers. An arrow $i\to j$ means that $i$ beats $j$; a dot in $p_{i,\cdot,j}$ means every cell of column $i$. The rows show the pointers that reach zeros; the three changed reverse pointers described in the text reach ones. The arrows out of column 1 come from its true cell and hold under every rival label.](figures/exposition/fig3_tournament.svg){width=55%}

Quantum minimum finding [@DH1996] needs a total order, and using quantum search with bounded-error inputs [@HMW2003] on these pair orientations would require fixed edge bits computed with bounded error. If two losers compare with probability $1/2$ in each direction, neither orientation is an underlying correct bit reported with probability greater than $1/2$; repetition cannot reveal such a bit. More generally their comparison probability is unrestricted, so our analysis uses only the identity $a_{ij}+a_{ji}=1$, which holds for every pair, winners and losers alike.

**An ideal process.** To analyse the search we compare it with a random process on weights. The weights are defined from the unknown probabilities $a_{ij}$; the algorithm never computes or estimates them. A weight measures the chance of beating all previously chosen pivots in fresh comparisons, not the chance that the column is a winner. The dominating nonwinner above can retain weight too: after pivot $2$ it still has weight $1$, may be sampled next, and is rejected by the test reading its false pointer to $X_2[2]=1$. Start with $w_i=1$ for every column and an empty list, and write $|w|=\sum_iw_i$. While $|w|>0$, a stage chooses a pivot $p$ with probability $w_p/|w|$, appends it to the list permanently, and multiplies each weight by its probability of beating the pivot, $w_i\leftarrow w_ia_{ip}$. The pivot's own weight becomes zero, since $a_{pp}=0$. Once $|w|=0$ the process is absorbed: the weights stay zero and nothing more is appended. On the cycled board we can compute the first stage directly.

If the first pivot is $1$, every weight becomes zero: the pivot loses to itself and every rival loses to it. The new weight vector is $(0,0,0,0)$ and its total is $0$.

If the first pivot is $2$, only columns $1$ and $4$ beat it, so the new weights are $(1,0,0,1)$. Pivots $3$ and $4$ instead give $(1,1,0,0)$ and $(1,0,1,0)$, respectively. Each of these three weight vectors has total $2$.

Pivot $1$ lists the winner and absorbs the process at once. Each pivot has probability $1/4$, so the expected new total is $3/2$, less than half the old total of $4$. In general, each unordered pair contributes $w_iw_p(a_{ip}+a_{pi})=w_iw_p$, and the diagonal terms vanish because $a_{ii}=0$. Hence $\sum_{i,p}w_iw_pa_{ip}=\sum_{i<p}w_iw_p=(|w|^2-\sum_iw_i^2)/2$. Thus
$$
\mathbb E\bigl[\,|w'|\;\big|\;w\bigr]=\frac1{|w|}\sum_{i,p}w_iw_pa_{ip}=\frac{|w|^2-\sum_iw_i^2}{2|w|}\le\frac{|w|}2,
$$
which on the cycled board is $(16-4)/8=3/2$; at $|w|=0$ the inequality holds trivially. The identity uses only $a_{ip}+a_{pi}=1$. The halving is an expectation bound; individual histories may lose weight slowly. It holds for cyclic comparisons and for comparisons of probability $1/2$ alike. By total expectation, $\mathbb E|w_{t+1}|\le\tfrac12\mathbb E|w_t|$; induction from $|w_0|=m$ gives $\mathbb E|w_T|\le m/2^T$.

There is one factor in a candidate's weight per selected pivot, even though the implementation may call the comparison circuit many times while sampling that pivot. Meanwhile the winner's weight stays at least $(1-\varepsilon)^T\ge1-T\varepsilon$ until it is chosen. We take
$$
T=\lceil\log_2(1000m)\rceil,\qquad\varepsilon=\frac{1}{1000T}.
$$
Then the winner keeps weight above $1/2$, so the process cannot be absorbed before the winner is listed, and if the winner is still missing after $T$ stages then $|w_T|>1/2$. Markov's inequality makes the link explicit:
$$
\Pr(\text{winner missing})\le\Pr(|w_T|>1/2)
 \le2\mathbb E|w_T|\le\frac{2m}{2^T}\le\frac1{500}.
$$

**Sampling a pivot.** The algorithm realises the ideal pivot law without knowing the weights. With no previous pivots the success flag is always $1$, so the first pivot is uniform. Now suppose measured pivots $p_1,\dots,p_j$ have been chosen. Every new attempt starts afresh and recomputes comparisons against this classical list. Prepare a uniform superposition over columns $i$ and, controlled by $i$, run a fresh copy of the comparison of $i$ against each $p_b$, each in its own new registers. Then compute a success flag that is $1$ when $i$ won all of them, and keep every register, so that reversing all the preparation gates inverts the whole preparation, as amplitude amplification requires. To find the success probability, fix the input, the pivot history and a value of $i$. The comparisons then act on separate fresh registers, so the probability that all of them report a win for $i$ is the product of the $a_{ip_b}$. The tensor product of register vectors obeys $(\sum_a u_a|a\rangle)\otimes(\sum_b v_b|b\rangle)=\sum_{a,b}u_av_b|a,b\rangle$. For two previous pivots, the two fresh comparison states are those two factors, and the preparation before computing the flag is
$$
\frac1{\sqrt m}\sum_i |i\rangle\,|\phi(i,p_1)\rangle\otimes|\phi(i,p_2)\rangle.
$$
Each $\phi$ contains fresh decoder labels, workspace and a win bit. A fresh flag records the AND of the two win bits; no register is erased or measured yet. For fixed $i$, the success probability is $a_{ip_1}a_{ip_2}$, the squared norm of its successful workspace component, not an amplitude. Different values of $i$ are orthogonal, so their probability masses add:
$$
\Pr(\text{success and column }i)=\frac1m\prod_{b=1}^{j}a_{ip_b}=\frac{w_i}m .
$$
Success has probability $|w|/m$. When $|w|>0$, conditioning on success gives exactly the ideal pivot law $w_i/|w|$. At $|w|=0$ success is impossible.

**A preparation on the board.** After a first pivot $2$, the weights are $(1,0,0,1)$. In a uniform preparation, columns $1$ and $4$ beat pivot $2$, column $3$ loses to it, and column $2$ loses to itself. Success and label $1$ have joint probability $1/4$, as do success and label $4$. Thus success has probability $1/2$, and the next pivot, conditional on success, is $1$ or $4$ with equal probability.

The same procedure also samples unequal weights. To see the distinction, consider the **fractional matrix example**, an abstract comparison law rather than another board mutation:
$$
a=\begin{pmatrix}0&1&1&1\\0&0&1/3&3/4\\0&2/3&0&2/5\\0&1/4&3/5&0\end{pmatrix}.
$$
Entry $a_{ip}$ is the probability that row $i$ beats column $p$. After pivot $2$ the weights, their sum, and the preparation's success probability are
$$
(w_1,w_2,w_3,w_4)=(1,0,2/3,1/4),\qquad |w|=23/12,\qquad q=23/48.
$$
The joint masses of success and each label are $(1/4,0,1/6,1/16)$. Dividing by $23/48$ gives the conditional pivot law $(12/23,0,8/23,3/23)$. The sampler does not choose uniformly among positive weights. These numbers are computed for the analysis; the quantum procedure obtains their law by running the comparisons themselves.

**Amplification with a fixed cap.** A single preparation may rarely succeed. Amplitude amplification can raise its chance of success with a suitable choice of iteration counts. Every iteration preserves the conditional pivot law whenever success has nonzero probability. Here is the linear-algebra reason [@BHMT2002, Lemma 1; @deWolf2026, chapter 7]. Write $q$ for the preparation's success probability, to distinguish it from a pivot label. For $0<q<1$, write the entire prepared state as
$$
\sqrt q\,g+\sqrt{1-q}\,b
 =\sin\theta\,g+\cos\theta\,b,
$$
where $g$ and $b$ are unit vectors in the success and failure subspaces. Both include the column register and **all** retained workspace. A phase flip on the success flag and a reflection about the prepared state give a rotation in the two-dimensional plane spanned by $g,b$. If $A$ is the full preparation and $|0\rangle$ its starting state, that reflection is
$$
R_{A0}=A(2|0\rangle\langle0|-I)A^{-1}.
$$
Read the product right to left: undo $A$, reflect about the starting basis vector, then prepare again. Both $A$ and $A^{-1}$ act on every retained register. In the ordered orthonormal basis $(g,b)$, the success phase flip and the displayed reflection have matrices
$$
S=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad
R_{A0}=\begin{pmatrix}-\cos2\theta&\sin2\theta\\\sin2\theta&\cos2\theta\end{pmatrix}.
$$
Their product $R_{A0}S=\left(\begin{smallmatrix}\cos2\theta&\sin2\theta\\-\sin2\theta&\cos2\theta\end{smallmatrix}\right)$ sends $(\sin\theta,\cos\theta)$ to $(\sin3\theta,\cos3\theta)$. Iterating this rotation $v$ times gives
$$
\sin((2v+1)\theta)\,g+\cos((2v+1)\theta)\,b.
$$
The coefficient of $g$ changes, but the relative label probabilities inside $g$ do not. Consequently, whenever success is reported, measuring just the column register gives the same conditional law as before amplification. A possible global sign of $g$ does not affect that law.

Since $q$ is unknown, we cannot choose the best rotation count: too many iterations can rotate past the success direction. A bounded randomized choice of iteration counts avoids this problem [@BBHT1998, Lemma 2]. We use the following form: for $0<\gamma\le1/2$ and $0<\eta<1/2$, the routine has a cap of $O(\gamma^{-1/2}\log(1/\eta))$ calls to the preparation and its inverse, preserves the conditional label law on success, and fails with probability at most $\eta$ whenever $q\ge\gamma$. If $q=0$, it reports failure with certainty; if $q=1$, every trial succeeds, as in the first uniform-pivot stage. The cap applies for every $q$, including $0<q<\gamma$, where no success guarantee is required. The [bounded amplification proof in record §5.1](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#upper-grover-trial) gives the guarantee for this explicit schedule. Set $M=\lceil10/\sqrt\gamma\rceil$ and $N=\lceil\ln(1/\eta)/\ln(40/31)\rceil$. In each fresh trial use zero iterations with probability $1/2$, and otherwise choose $v$ uniformly from $0,\ldots,M-1$. Stop at the first success, or after $N$ failures. Each trial uses at most $2M+1$ calls to $A$ or $A^{-1}$, so $N(2M+1)$ is an all-input cap. The record proves that each trial succeeds with probability at least $9/40$ when $q\ge\gamma$; the route accepts that averaged trigonometric estimate.

Every successful trial, for every chosen $v$, has the same normalized good state $g$ up to a global sign. Fresh initialization makes previous failures independent of the next trial. Mixing iteration counts, and then conditioning on which trial first succeeds, therefore mixes identical label distributions. The successful output of this capped routine has exactly the required pivot law.

On the board after pivot $2$, $q=1/2$ and $\theta=\pi/4$, so $\sin^2((2v+1)\pi/4)=1/2$ for every $v$. No single trial improves its success probability; $N$ fresh trials nevertheless fail with probability $2^{-N}$. The next exercise gives a case in which one iteration does improve it.

**A stage of the search.** Each stage amplifies the preparation with threshold $\gamma=1/(2m)$ and failure parameter $\varepsilon$, at a cost of $O(\sqrt m\log(1/\varepsilon))$ preparations whatever $|w|$ is. On success we measure the column register, and the outcome becomes the next pivot, a classical value that later preparations use. On reported failure the algorithm stops and passes its current list to verification; it also stops after $T$ pivots.

Before the winner is listed its weight exceeds $1/2$, so $|w|/m\ge\gamma$ and a stage fails with probability at most $\varepsilon$.

After the winner is listed, $|w|$ may be tiny or zero and the sampler may fail with certainty, but stopping cannot remove a listed column. Run the real and ideal processes together, using the same pivot whenever a real stage succeeds: their conditional pivot laws agree. On failure the real process stops. This joint construction is a coupling. Conditional on each common history before the winner is listed, failure has probability at most $\varepsilon$; summing over at most $T$ stages costs at most $T\varepsilon$. So the real list misses the winner with probability at most $2m/2^T+T\varepsilon$.

Return to the board after pivot $2$. If the next measured pivot is $1$, the winner has been listed and every weight becomes zero. The next stage fails with certainty, and the retained list $\{2,1\}$ goes to verification. A later failure cannot undo this earlier success.

[]{#question-2}**Question 2 (conditional sampling and overshoot).** Suppose instead that the measured pivot is $4$. Find the new weights, the success probability of a preparation and the next pivot. Starting from a fresh preparation each time, compare one iteration total with two iterations total. An iteration uses the entire preparation and its inverse, not one bit query. In a separate calculation, continue the fractional matrix example with pivot $4$: find the joint success masses and conditional label law. Multiply the current weights by the comparison probabilities; do not restart from all ones. ([Answer](#answer-2).)

**Verification.** Finally we check each listed column. Decode its address afresh with error at most $\varepsilon/r$ per instance, hence at most $\varepsilon$ for a promised whole address, and measure it. Then search for a failing local test among the $K$ tests of Section 2. The pivot sampler's success appends a candidate; here the search's success flag instead means **a violation was found**, so it rejects the candidate. If no violation is found, accept the candidate; output $1$ if any candidate is accepted, and $0$ otherwise, including when the list is empty.

A coherent test evaluation works on a superposition of test labels. It computes the next input position reversibly and retains earlier answers. To implement a read that is active only on some branches, query $x_j$ into a temporary bit, conditionally copy it to the answer bit, then query $j$ again to clear the temporary bit. This uses two ordinary oracle calls; on an inactive branch the answer and temporary bits are both restored. Padding to a common number of these controlled reads therefore has a fixed cap even in superposition. Running the computation backwards then restores its workspace. This implements the same tests using $O(\ell+1)$ bit queries per evaluation; [record §4.6](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#AC-coherent) gives the controlled implementation. No full transcript is read during a single test.

A nonwinner fails some test at **every** address, even a meaningless label decoded off promise. An input-independent unitary prepares the uniform state on the $K$ test labels at no query cost. The uniform preparation over tests therefore finds a violation with probability at least $1/K$. Amplifying with threshold $1/K$ and failure parameter $\varepsilon$ bounds false acceptance by $\varepsilon$. On the domain-bit board in Section 2, candidate $(2,00)$ fails exactly its first domain test; that one violation suffices. The dominating nonwinner from this section similarly fails a pointer test. The winner at its correctly decoded address has no violations, so the violation search certainly fails and the verifier accepts it.

When $F=1$, the output is wrong only if the list misses the winner or the winner's fresh decoding fails, with probability at most $2m/2^T+T\varepsilon+\varepsilon\le1/250$. When $F=0$, one of at most $T$ nonwinners must be falsely accepted, with probability at most $T\varepsilon\le1/1000$. Decoder errors within comparisons are already included in the actual probabilities $a_{ij}$. For $F=1$, the term $T\varepsilon$ covers premature sampler failure and the last $\varepsilon$ covers the winner's fresh address decoding. For $F=0$, $T\varepsilon$ instead covers missed violations in at most $T$ verifications. These are different cases, not additional comparison-decoder error terms.

**The count.** Every branch has a fixed cap, including branches that stop early or report failure. There are $T=O(\log m)$ stages; a stage makes $O(\sqrt m\log(1/\varepsilon))$ preparations, each using at most $T$ cheap comparisons. Verification checks at most $T$ candidates, each by searching its $K$ local tests. Thus, suppressing logarithmic factors,
$$
\text{tournament cost }\lesssim\sqrt m,
\qquad
\text{verification cost }\lesssim\sqrt K\lesssim_k\sqrt m.
$$
These costs add. In the direct search rejected at the start of this section, a certificate check was nested inside every search step and the costs multiplied. Paying for address decoding, pointer bits and error reduction gives
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6.
$$
[Appendix A.1](#quantum-query-count) totals those terms. The exponent six is a loose accounting choice; the square-root dependence is what the separation needs.

The earlier balanced AND–OR cheat-sheet recipe reaches at most a cubic exponent by its known analysis. [Appendix A.2](#earlier-recipe) explains that comparison after the two bounds have been proved.

# 5. The classical lower bound: a planted pair

We now show that $R(F_{k,m})>\lfloor mL/100\rfloor$, by planting a winner in a random column. Fix $k$, let $m$ be sufficiently large, and put $L=L_{k,m}<R(P)$, with $1\le L\le m$. By Yao's minimax principle [-@Yao1977] in its finite form, there is a distribution $\mu$ on promised inputs of $P$ under which every deterministic algorithm making at most $L$ queries is correct with probability at most $2/3$ ([record §6.2](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#CL-minimax) proves the finite form: regard promised inputs as rows and capped trees as columns of a zero-one correctness matrix, and seek one distribution on rows whose average is at most $2/3$ in every column). The quantifier matters: one distribution defeats **all** capped deterministic trees, rather than a different distribution for each tree. Minimax converts worst-case hardness against randomized algorithms into this common hard law. An algorithm correct on every promised input would also be correct on average under it. The law need not be uniform or efficiently samplable. Even knowing it would not reveal which hidden sample was drawn.

**The pair.** We draw every address input from $\mu$ and, in each column $i$, one position $J_i$ uniformly, all mutually independent. Set $X_i$ to all ones except a zero at $J_i$, and set every bit in every cell to zero, which we call **blank**. This is the **dummy** input $Y^0$, and $F(Y^0)=0$. We then choose a column $I$ uniformly, independently of everything else. The **planted** input $Y^1$ erases the zero $X_I[J_I]$ and fills the true cell $B_{I,s_I}$ with correct transcripts and with pointers to the zeros $J_j$ of the other columns. Column $I$ wins, so $F(Y^1)=1$.

Figure 4 shows a schematic realization of the planting operation, using the geometry of Section 2. Its displayed address is $s_I=10$ and its transcripts must be the true evaluations on the newly selected address inputs; they are not the fixed transcripts of Figure 2. At $m=4$ the stated threshold is $L=0$, so this picture illustrates the two changed locations, not a hard distribution at positive budget.

![A realization of the planted pair with $I=1$, $s_I=10$ and $J=(4,1,2,3)$. The address inputs are identical in the two panels. The filled cell's transcripts match those inputs. Only $X_1[4]$ and the cell $B_{1,10}$ change; their locations are revealed to the reader, hidden from the algorithm.](figures/exposition/fig4_planted.svg){width=90%}

Fixing all the coins of a randomized algorithm gives a deterministic decision tree. We first bound each such tree, then average over the coins. Fix a deterministic algorithm $\mathcal A$ making at most $G=\lfloor mL/100\rfloor$ queries. Its runs on $Y^0$ and $Y^1$ follow the same path until it first reads a bit where the inputs differ, and every such bit is the erased zero or lies in the true cell. For the pictured pair, an algorithm could read $X_2[1]=0$, choose from that answer to read $X_1[1]=1$, then choose $X_1[4]$. The first two answers and choices agree; the third answer is $0$ on the dummy input and $1$ on the plant. Any deterministic adaptive prefix behaves this way until its first differing answer. The run on $Y^0$ does not depend on $I$, which is chosen independently. Hence
$$
\bigl|\Pr[\mathcal A(Y^1)=1]-\Pr[\mathcal A(Y^0)=1]\bigr|
\le\Pr(\text{erased zero hit})+\Pr(\text{true cell visited}),
$$
where both events refer to the run on the dummy input. (Counting every visit to the true cell overcounts, since a filled bit may equal its blank value; that only weakens the bound.)

**The erased zero.** Let $Z$ be the number of columns whose zero the dummy run finds. Given the dummy data, exactly $Z$ of the $m$ choices of $I$ select a found zero, so
$$
\Pr(\text{erased zero hit})=\frac{\mathbb E Z}{m}\le\frac{4G}{m^2}.
$$
To bound $\mathbb EZ$, condition on the entire transcript prefix immediately before the next query, including earlier queries to every field. The cells are blank and the other fields are independent of the zero positions. Fixing an observed prefix constrains a zero only by the string bits already read: any two unread zero locations yield the same recorded answers and hence the same deterministic choices. An undiscovered zero is therefore uniform among its column's unread positions. Before its first discovery, a new query in a column with fewer than $m/2$ distinct positions read therefore finds its zero with probability at most $2/m$, giving at most $2G/m$ such discoveries in expectation. A repeat query makes no new discovery.

For the remaining, late discoveries, charge the already spent reads rather than a conditional probability. Each needs $m/2$ queries in its column, which happens in at most $2G/m$ columns: charge $m/2$ distinct string reads to each such column, from the same total budget $G$ ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#CL-early-late)).

\Needspace{11\baselineskip}

The identity $\Pr(\text{erased zero hit})=\mathbb EZ/m$ needs $I$ to be independent of the run. Query one fixed position in each of the four columns, so that $\mathbb EZ=1$ and an independent $I$ is hit with probability $1/4$. Suppose instead that $I$ is chosen uniformly among the columns where a zero was found, and uniformly among all four when none was found, which happens with probability $(3/4)^4=81/256$. By symmetry $I$ is still uniform on its own, but now it is hit whenever some zero was found, with probability $1-(3/4)^4=175/256$. A uniform marginal is a weaker condition than independence from the run, and the proof needs independence.

[]{#question-3}**Question 3 (independent planting).** With two fixed distinct positions queried per column, how often is an independent $I$ hit, and how often the dependent one? If later queries depend on earlier replies, which identity still holds for an independent $I$, and why? ([Answer](#answer-3).)

**The true cell.** The algorithm need not compute $s_I$ to reach $B_{I,s_I}$: it may guess an address or visit many cells. But a query in the true cell names, by its position alone, all $r$ hard answers $s_I$. Write a cell-bit coordinate as $(i,s,u)$: column $i$, cell label $s$, and bit offset $u$ within that cell. Parsing this chosen coordinate outputs $s$ without reading any input. Choosing the position is free; following a stored pointer is different because its bits must first be read. This proposed address is correct exactly on the true-cell event, and that is what we show to be unlikely.

**Whole-run budget.** Call a column **heavy** if the whole dummy run makes more than $L$ queries, in total, to its $r$ address inputs, and **light** otherwise. Queries after a cell visit still count: being below the threshold when that visit occurs does not make the whole run light. At most $G/L$ columns are heavy, so $\Pr(I\text{ heavy})\le G/(mL)$. For each column $i$ and each time $j\le G$, we bound by $(2/3)^r$ the probability that $i$ is light **and** the $j$-th dummy query lies in $i$'s true cell, using a direct product with a separate cap on each instance.

**Direct product with separate caps.** *Let $U_1,\dots,U_r$ be independent samples from $\mu$, and suppose every deterministic algorithm making at most $L$ queries to one sample is correct with probability at most $\beta$. Let an algorithm choose adaptively which sample to query, make at most $L$ queries to **each** $U_h$ on every run, and use coins and side information jointly independent of the whole tuple $(U_1,\dots,U_r)$. Then it outputs all $r$ answers correctly with probability at most $\beta^r$.*

**Why the event must be joint.** A run that stays light behaves like a capped algorithm, but it need not succeed with probability at most $\beta^r$ given that it stays light. Take $P=\text{AND}$ on the three promised inputs $01,10,11$, uniformly; any one-query algorithm is right with probability at most $\beta=2/3$. Read the first bit, output $0$ if it is $0$, and otherwise read the second bit. This algorithm stays within one query exactly on input $01$, where it is right, so its success given that it stays light is $1$. The true statement concerns the joint event: being right **and** staying within the caps has probability $1/3\le\beta$. This toy illustrates conditioning: it meets the one-query hard-law premise but has $R(P)=L=1$, so it does not instantiate the strict $L<R(P)$ regime of our construction ([reasoning record §6.5](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#CL-conditioning-counterexample)).

**The simulator.** Fix a column $i$ and a global dummy-query time $j\le G$. The hidden data are its address tuple $(A_{i,1},\ldots,A_{i,r})$. Give the simulator all zero positions, all other columns' address inputs, and the blank cells. These are jointly independent of the hidden tuple, and answer every query outside it. Let $q$ count only forwarded queries to the hidden tuple; global time $t$ counts all simulated queries.

1. Initialize $q=0$ and simulate the dummy tree from $t=1$.
2. Inspect the query position the tree proposes at time $t$. If $t=j$ and it is a cell-bit coordinate $(i,s,u)$, output $s$ and stop, without reading that cell bit.
3. Otherwise, if the query addresses the hidden tuple and $q=L$, output the fixed default address and stop **before** reading. If $q<L$, forward the query and increase $q$ by one. Answer any other query from the supplied data.
4. If time $j$ is reached without the target cell query, or the tree has already halted, output the default address. Otherwise continue to the next global time.

The default makes this a total algorithm on every history, including an abort. A lucky default can be correct, which only enlarges the simulator's success event.

Three budgets are in play. The dummy algorithm makes at most $G$ queries in all. The simulator makes at most $L$ queries to column $i$'s address inputs in total, which is also the threshold for heaviness. The direct product asks for at most $L$ queries to each of the $r$ instances. The second implies the third, since a total of $L$ is at most $L$ on each instance (the direct product would even allow $rL$). So on every run the simulator meets the hypotheses of the direct product, and its output, learned or guessed, is the true address with probability at most $(2/3)^r$. Whenever column $i$ is light and the $j$-th dummy query visits its true cell, the simulator has not stopped and outputs $s_i$. Hence
$$
\Pr(i\text{ light and query }j\text{ visits }B_{i,s_i})\le(2/3)^r ,
$$
with lightness inside the probability. The independent side information deliberately makes the simulator more informed than the original tree; the direct-product bound still applies to it. In event notation, $\{i\text{ light and query }j\text{ visits }B_{i,s_i}\}\subseteq\{\text{simulator outputs }s_i\}$. The implication goes one way: a lucky default guess can make the simulator correct without such a visit. This is why its unconditional success probability is an upper bound for the event we need.

A small trace makes the cap concrete. Use the [record's XOR example](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#CL-simulator-example), which changes the partial function to $P(a,b)=a\oplus b$. It numbers columns from $0$, so its target label $1$ denotes the second column, corresponding to column $2$ under the base board's numbering. In that separate toy, let the two inputs $(a,b)$ and $(c,d)$ be independent fair bit pairs, and set $L=1$. The dummy algorithm first reads an outside string bit, then $a$. Its third query is outside the target if $a=1$, and reads $c$ if $a=0$. Its fourth query proposes a bit in $B_{1,(a,0)}$.

| Global time | Proposed query | Forwarded count and action |
| --- | --- | --- |
| $1$ | Outside string bit | $q=0$; answer locally. |
| $2$ | $a$ | $q:0\to1$; forward. |
| $3$, $a=1$ | Outside target | $q=1$; answer locally. |
| $3$, $a=0$ | $c$ | $q=1=L$; stop before reading. |
| $4$, $a=1$ | Cell $B_{1,10}$ | $q=1$; output label $10$ without reading. |


If $a=1$, the simulator has spent its one target query learning $a$. It answers the third query from its outside information, then reaches the fourth query and outputs $10$, read from the proposed cell position. It does not read the bit in that cell.

If $a=0$, the proposed third query would read $c$, using a second target query. The simulator stops before that query and outputs the default address $00$. Its cap is enforced on this branch as well.

The first branch gives the light true-cell event exactly when $a=1,b=0,c=d$, with probability $1/8$. The simulator is also correct on $a=0,b=0,c=d$, another event of probability $1/8$. Its total success probability is $1/4$, the separate-cap bound $(1/2)^2$ for two fair XOR inputs. Aborting is part of the algorithm; we have not conditioned the input distribution on staying cheap.

[]{#question-4}**Question 4 (two clocks and the capped event).** Change the $a=0$ branch so that it proposes a query in $B_{1,00}$ at time $3$, before trying to read $c$. If the run stops after this cell query, what probability does the changed branch contribute, and what is the total probability of a light true-cell visit at either indicated time, including the unchanged $a=1$ branch at time $4$? What changes if the $a=0$ branch reads $c$ afterwards? Which fixed-time events must be bounded separately by the simulator lemma? ([Answer](#answer-4).)

For the general bound, sum over the $G$ possible query times first. For each fixed column, the chance of a light true-cell visit is at most $G(2/3)^r$. Now average over the independent uniform planted column $I$:
$$
\frac1m\sum_{i=1}^m G(2/3)^r=G(2/3)^r.
$$
There is no extra factor of $m$: we ask whether the independently selected column is hit, not whether any column is hit. Adding the heavy-column case gives
$$
\Pr(\text{true cell visited})\le\frac{G}{mL}+G\left(\frac23\right)^r.
$$

**Why the hypotheses matter.**

*Separate caps.* Take AND on two independent inputs, each uniform on all four two-bit strings; one query to an input gives $\beta=3/4$. A pooled budget of two queries computes the first answer exactly and guesses $0$ for the second, which is right with probability $3/4>9/16$.

*Joint independence.* For the identity on fair bits $X,Y$ with $L=0$, the side information $X\oplus Y$ is independent of each bit separately, yet the guess $(0,X\oplus Y)$ is right whenever $X=0$, with probability $1/2>1/4$.

[Appendix B](#direct-product-proof) proves the separate-cap lemma, including why adaptive interleaving preserves its product bound. We now combine the bounds on the two changed locations.

[]{#classical-finish}**Finishing.** The gap is at most $4G/m^2+G/(mL)+G(2/3)^r$. With $r=40t$ and $m=4^t$, the inequality $(2/3)^2\le1/2$ gives $(2/3)^r\le m^{-10}$, and $G\le mL/100\le m^2/100$, so the gap is at most $4/100+1/100+1/(100m^8)<1/3$. A randomized algorithm computing $F$ with $G$ queries would satisfy
$$
\Pr[\mathcal A(Y^1)=1]\ge2/3,\qquad
\Pr[\mathcal A(Y^0)=1]\le1/3,
$$
because every planted input is a $1$-input and every dummy input is a $0$-input. Subtracting gives a gap of at least $1/3$. For a coin string $\omega$, write $\Delta_\omega=\Pr[\mathcal A_\omega(Y^1)=1]-\Pr[\mathcal A_\omega(Y^0)=1]$. Averaging gives $|\mathbb E_\omega\Delta_\omega|\le\mathbb E_\omega|\Delta_\omega|<1/3$, contradicting the required signed gap. This uses the same input distributions for every coin string. So
$$
R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor .
$$
Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm. This is the $m\cdot L$ half of the arithmetic.

# 6. Exponent four, and the order of quantifiers

The two bounds explain the fourth power: for a large fixed $k$, nearly $m^2$ classical queries against about $\sqrt m$ quantum queries. We now make the statement uniform over functions and show why $k$ must be chosen before letting $m$ grow.

Define
$$
\alpha_{\rm tot}=\inf\bigl\{\alpha\ge0:\ \exists C>0\ \forall\text{ total }f,\quad R(f)\le C(1+Q(f))^\alpha\bigr\}.
$$
Here $f$ ranges over every map $\{0,1\}^n\to\{0,1\}$ and every integer $n\ge0$. The same constant $C$ must work for all of them; $1+Q$ includes constant functions. To refute an exponent $\alpha<4$, we will choose one fixed $k$ for which $R/(1+Q)^\alpha$ tends to infinity as $m$ grows.

First recover the stated coefficient. Put $x=m^{1-1/k}/(\log_2m)^2$. For fixed $k$, eventually $x\ge1$, and $L=\lfloor x\rfloor\ge x/2$. Since $R$ is an integer, $R>\lfloor mL/100\rfloor$ implies $R>mL/100$. This gives coefficient $1/200$, which we weaken to the advertised $1/400$. Thus for each fixed $k\ge2$ and all sufficiently large powers of four $m$,
$$
R(F_{k,m})\ge\frac{1}{400}\,\frac{m^{2-1/k}}{(\log_2m)^2},\qquad Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6 .
$$
Fix $0\le\alpha<4$, then an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $d=2-1/k-\alpha/2>0$. For $m\ge4$, $1+Q\le(1+C_k)\sqrt m(\log_2m)^6$. Since $\alpha\ge0$, replacing the denominator by this upper bound can only decrease the ratio, so, with $c_{k,\alpha}=1/[400(1+C_k)^\alpha]$ independent of $m$,
$$
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^{\alpha}}\ge c_{k,\alpha}\,\frac{m^{d}}{(\log_2m)^{2+6\alpha}}\longrightarrow\infty .
$$
The positive power $m^d$ outgrows the logarithm: the logarithm of the last factor is $d\log m-(2+6\alpha)\log\log_2m$, which tends to infinity. So no constant $C_\alpha$ works, and $\alpha_{\rm tot}\ge4$. For $\alpha=3$, $k=3$ suffices and refutes the cubic conjecture. For $k=2$ the leading powers have threshold three, but these bounds exclude only powers strictly below three.

All constants, including $C_k$ and the point from which the Forrelation bound holds, depend on $k$, so a $k$ that grows with $m$ cannot be substituted into these fixed-$k$ bounds without additional uniform estimates. That extension asks for one explicitly scheduled family with $k$ increasing and $R\ge Q^{4-o(1)}$, rather than separately refuting each fixed exponent. Appendix E of the expert companion and [Section 7.3 of the reasoning record](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#ROOT-GROWING-K) address it; the equality proved here does not require it. For example, for each fixed $k$ the condition $t\ge2^k$ holds for all large $t$, yet substituting $k=t$ asks for $t\ge2^t$, which never holds. The argument above chooses $\alpha$ first, then a single $k$, and only then lets $m$ grow.

[]{#question-5}**Question 5 (uniform constants and endpoint powers).** What does $k=4$ prove about $\alpha_{\rm tot}$? Which $k$ makes the displayed argument exclude the endpoint bound $R(f)\le C(1+Q(f))^{3.5}$ itself? ([Answer](#answer-5).)

The matching upper bound $D(f)=O(Q(f)^4)$ for every total $f$ [@ABKRT2020], and hence $R(f)=O(Q(f)^4)$, rests on Huang's sensitivity theorem [-@Huang2019]; the record reconstructs this quartic upper bound, including the signed-cube calculation used from Huang's argument ([Appendix A of the reasoning record](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#R3-A-RESULT)). Hence $\alpha_{\rm tot}=4$.

**Combined explanation.** Using the cycled board and the planted-pair/XOR examples, explain why the quantum list can contain a winner even when a later stage fails, and why any classical light visit gives a capped address prediction. Why does an arbitrary rival's off-promise decoder law not spoil comparison with a genuine winner? Explain which half of $\alpha_{\rm tot}=4$ these mechanisms establish and which half uses the imported universal theorem. Try this before reading the [rubric](#answer-combined). A one-route reader may quote the other route's bound.

# 7. The statement in Lean

**Optional statement-reading extension.** Use the [domain-bit board](#domain-bit-board) to identify the formal clause it violates. The linked challenge file states the mathematical obligations; its intentional `sorry` placeholders are filled by a separate [proof file][statement-solution] in the comparison check. Open the [winning condition][def-wins] and find the clause requiring each address input to be promised with the value named by its address. Look for `f (readA x i h) = some (s h)`: Here `x` is the whole board, `i` its column, `h` an address-input index, and `readA x i h` the corresponding input $A_{i,h}$. The function `f` is the partial function $P$, and `s h` is bit $h$ of the proposed $r$-bit address. `some` supplies a defined Boolean answer; `none` means outside the promise. It is exactly the clause that rejects the all-one, off-promise column\ $2$. The definitions live in one [statement file][statement-file] importing only Mathlib, Lean's shared mathematical library; it also specifies [$R$][def-R], [$Q$][def-Q], [the total function][def-F] and [$\alpha_{\rm tot}$][def-alpha]. The record explains [their agreement with the usual query models](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#R3-01-CLASSICAL).

The [four formal theorems][thm-all] establish $\alpha_{\rm tot}=4$, failure of every universal cubic bound, the Forrelation lower bound used here, and the total-function family theorem. The exponent and Forrelation conclusions match those above. The cubic challenge uses $Q^3$ rather than $(1+Q)^3$: constant functions have $R=0$, while a nonconstant Boolean function has $Q\ge1$ and hence $1+Q\le2Q$. The two universal cubic assertions are therefore equivalent after changing the constant.

For the **family bounds**, the compared theorem uses one circuit for both complexities, gives $\lfloor mL/100\rfloor<R$, and leaves the quantum logarithmic exponent unspecified. The [separate named-circuit theorem][src-constants] proves the printed six and $1/400$; it has recorded build and axiom-audit evidence, but is outside that comparison bundle. [Appendix G.4 of the reasoning record](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#formal-named-family) identifies that evidence and explains the source's historical “unelaborated” header.

Lean checks proofs of the formal statements; Comparator checks their agreement with separately compiled challenge statements. This does not check every step of this exposition or establish that a definition captures its intended meaning. Those are separate reading tasks. The exact statement map and recorded execution scope are in [Appendix G of the reasoning record](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#checked-statements).

# Answers to the questions {.unnumbered}

[]{#answer-projection}**Projection check.** The first sign block is $(-1,-1,-1,-1)$ and its dot product with $(2,-2,-2,-2)$ is $4$. Thus the signed amplitude is $\Phi=4/8=1/2$ and projection probability is $|\Phi|^2=1/4$.

[]{#answer-combined}**Combined-explanation rubric.** For the quantum route, derive the successful label law from fresh comparison registers, then explain why randomized iteration counts and first-success retries preserve it. A rival cannot point to a zero in an all-one winning column, whatever label its decoder returns. Retaining every measured pivot lets final verification recover a winner after a later sampling failure. For the classical route, partition the board into the hidden target tuple and jointly independent supplied data, give the stop-before-read rule and total default output, and show that a whole-run light visit is a subset of the capped predictor's success event; the converse need not hold. Finally choose the exponent, fix $k$, and grow $m$ through powers of four. This rules out every exponent below four. The imported universal bound makes four admissible. Using this rubric while explaining is guided practice, not an unaided test.

[]{#answer-1}**[Question 1](#question-1).** String, pointer and gate tests pass. Domain bits $(0,1)$ and value bits $(0,0)$ make the first domain test fail always, and a value test fail wherever the address differs from $00$: one failure at $00$, two at $01$ and $10$, three at $11$.

\Needspace{15\baselineskip}

[]{#answer-2}**[Question 2](#question-2).** Multiplying $(1,0,0,1)$ by $(a_{14},a_{24},a_{34},a_{44})=(1,0,1,0)$ gives $(1,0,0,0)$. A preparation succeeds with probability $1/4\ge\gamma$ and then yields column $1$; with $\theta=\pi/6$, one Grover iteration makes success certain, as $\sin^2(3\pi/6)=1$. A second iteration overshoots: $\sin^2(5\pi/6)=1/4$. For the fractional example the new weights are $(1,0,4/15,0)$, joint masses $(1/4,0,1/15,0)$, total success $19/60$, and conditional law $(15/19,0,4/19,0)$. Returning now to the cycled physical board, column $1$ passes verification from the list $\{2,4,1\}$. The fractional matrix specifies only sampler probabilities; certification uses the board's strings, pointers and transcripts. Columns $2$ and $4$ have failed string tests; the bounded-error verifier discovers those failures with its stated high probability, not with certainty.

[]{#answer-3}**[Question 3](#question-3).** Even for adaptive queries, independence gives $\Pr(\text{erased zero hit})=\mathbb EZ/4$ by conditioning on the complete dummy run. For the fixed two-position experiment, an independent $I$ is hit with probability $\mathbb EZ/4=1/2$; the dependent choice misses only when no zero is found, so it is hit with probability $1-(1/2)^4=15/16$. This product uses two distinct fixed positions in each column and independent zero locations. An adaptive policy preserves the complete-run identity but need not preserve that fixed-pattern product.

[]{#answer-4}**[Question 4](#question-4).** First assume that the changed branch stops after the cell query. The cell query now occurs after only one target query, so the simulator reaches it and outputs $00$. It is a true-cell query when $a=0,b=0,c=d$, with probability $(1/2)(1/2)(1/2)=1/8$. Including the unchanged $a=1$ branch gives total probability $1/4$. If the algorithm instead reads $c$ afterwards, the entire $a=0$ branch is heavy and contributes zero to the joint light-visit event. No query is deleted from the count. The remaining probability is $1/8$, from the unchanged $a=1$ branch. In the stopping version, the fixed-time probabilities are $1/8$ at time $3$ and $1/8$ at time $4$; their union is $1/4$.

[]{#answer-5}**[Question 5](#question-5).** $k=4$ excludes every power strictly below $3.5$, so it proves $\alpha_{\rm tot}\ge3.5$. To exclude the endpoint inequality itself by this argument, take $k>2/(4-3.5)=4$, for example $k=5$. At $k=4$ and $\alpha=3.5$, the ratio estimate has $d=0$ and only a reciprocal logarithmic factor; it does not diverge. At $k=5$, $d=2-1/5-3.5/2=1/20>0$, so it does diverge.

[^ai]: The theorem and construction are OpenAI's. This exposition and its Lean development were prepared with AI systems under the author's direction.

# Appendix A. Query counts and the earlier recipe {.unnumbered}

[]{#quantum-query-count}

## A.1 Counting the quantum queries

The main quantum argument in Section 4 uses the following count. It charges the same comparisons and local tests on every branch; early stopping can only reduce the cost.

**The count.** Early stopping and randomized iteration counts make the number of queries depend on the run. The caps are fixed in advance and hold on every input and branch. A comparison uses $O_k(r\log(r/\varepsilon))$ queries for its decoders and $O(\ell+1)$ for its pointers, including the constant overhead of a reversible implementation. We count the tournament first, then verification.

Each stage uses $O(\sqrt m\log(1/\varepsilon))$ preparations, and each preparation makes at most $T$ comparisons. There are at most $T$ stages. Multiplying these three factors bounds the entire tournament by $O(\sqrt m\,T^2\log(1/\varepsilon))$ comparisons.

Verification makes at most $T$ fresh address decodings. For each candidate it searches the $K$ local tests, using $O(\sqrt K\log(1/\varepsilon))$ test evaluations. Thus the list requires $O(T\sqrt K\log(1/\varepsilon))$ test evaluations in all.

In bit-query units the two costs add:
$$
O_k\!\left(\sqrt m\,T^2\log(1/\varepsilon)
 [r\log(r/\varepsilon)+\ell]
 +T[r\log(r/\varepsilon)+\sqrt K\log(1/\varepsilon)\ell]\right).
$$
The first bracket charges comparisons; the second charges fresh address decoding and local-test search. Here $r,T,1/\varepsilon=O(\ell)$ and $K=O_k(m\ell^3)$. Bounding $\log(1/\varepsilon)=O(\ell)$, $\log(r/\varepsilon)=O(\ell^2)$ and $\sqrt K=O_k(\sqrt m\,\ell^2)$ deliberately enlarges the logarithms and square root. These substitutions give $O_k(\sqrt m\,\ell^6)$ for the tournament and $O_k(\sqrt m\,\ell^5)$ for verification ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/4f8286795ff2eb1c4dd03e616a1b998b05727a88/docs/reasoning_record.md#upper-explicit-log6)). Therefore
$$
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^6.
$$
The tournament and short-list verification costs add, in place of the earlier nested search product $\sqrt m\sqrt K$. Here $m$ counts columns. The exponent six is an artefact of this loose count. Square-root dependence comes from amplifying pivot sampling and searching the local tests. The short list limits how many verifications are needed; it is the quantum half of the exponent calculation.

[]{#earlier-recipe}

## A.2 Why the balanced AND–OR recipe stops at a cube

In the cheat-sheet construction [@ABK2016, §3.1], each of the $n$ input bits of a partial function $g$ is replaced by the answer to its own AND–OR instance on $n^2$ bits, for $n^3$ bits overall before adding certificates. In one instance, write the bits as $n$ rows of $n$ bits; its answer is $1$ exactly when every row contains a $1$. A $1$-certificate selects one $1$ in every row; a $0$-certificate selects one entire zero row. Thus either answer has a certificate of $n$ bits. Reading those certificates determines the $n$-bit vector supplied to $g$; the fixed domain predicate of $g$ can then be checked by free computation. The certificate reads remain charged.

Up to logarithmic factors, the cited composition and cheat-sheet argument supplies randomized lower bound $R(g)n^2$ and quantum upper bound $n$ when $Q(g)$ is polylogarithmic in $n$, with polylogarithmic factors suppressed throughout this comparison. Reading all $n$ bits gives $R(g)\le n$, so this calculation reaches at most a cubic separation. Ben-David's earlier Forrelation construction [-@BenDavid2015] and cheat sheets first gave power $5/2$; Tal [-@Tal2020] reached $8/3-o(1)$, and the nearly linear partial-function bounds of Bansal and Sinha [-@BansalSinha2021] and Sherstov, Storozhenko and Wu [-@SSW2023] gave $3-o(1)$. In the present construction, an address instance has about $m$ bits while the quantum search costs about $\sqrt m$. The partial-function hardness can therefore contribute almost two powers of the quantum cost. Section 4 explains how comparisons make that square-root search possible.

[]{#direct-product-proof}

# Appendix B. The separate-cap direct product {.unnumbered}

This proves the lemma stated in Section 5. The input samples are independent, each has the same hard law, each individual cap holds on every branch, and the coins and side information are jointly independent of the entire tuple.

*Source note.* The separately capped setting goes back to Shaltiel's fair decision trees [-@Shaltiel2003]. The proof below is the conditional-value argument of Drucker's Lemmas 3.1–3.2, whose headline theorem uses one global budget instead [-@Drucker2012, §1.3 and the end of §3].

Fix the coins and side information. By joint independence the samples are still independent with law $\mu$, and the algorithm is a deterministic tree. Take a history $\tau$ of queries and answers that occurs with positive probability. Each recorded answer constrains only its own sample, and because the tree is deterministic, every tuple that agrees with these answers asks exactly these queries. So the tuples consistent with $\tau$ form a product $E_1(\tau)\times\dots\times E_r(\tau)$, and given $\tau$ the samples are independent with laws $\mu(\cdot\mid E_h(\tau))$.

Now measure the best success still available with the budget left. For the AND example, before querying it is $3/4$; after seeing a zero it is $1$, and after seeing a one with no queries left it is $1/2$. Let $q_h(\tau)$ count the queries to $U_h$ in $\tau$, and let $V_h(\tau)$ be the best probability of computing $P(U_h)$ under $\mu(\cdot\mid E_h(\tau))$ with at most $L-q_h(\tau)$ further queries. If the next query reads a bit of $U_h$, then querying it and continuing optimally is one strategy with that allowance, so averaging over the answer $b$,
$$
\sum_b\Pr(b\mid\tau)\,V_h(\tau b)\le V_h(\tau).
$$

One answer may raise $V_h$; only the average cannot. For the two uniform AND inputs above with caps of one query, observing first bit $0$ in $U_1$ gives $E_1=\{00,01\}$ and $E_2=\{00,01,10,11\}$; the second sample is still unrestricted. We have $V_1=V_2=3/4$ at the start; reading the first bit of $U_1$ makes $V_1=1$ or $1/2$ as the bit is $0$ or $1$, and $V_2$ stays $3/4$, so the product averages to $\tfrac12\cdot\tfrac34+\tfrac12\cdot\tfrac38=\tfrac9{16}$, its starting value.

In general the other samples keep their laws and allowances, so their values do not change, and $\prod_hV_h$ has nonincreasing expectation from step to step. It starts at most $\beta^r$. At a leaf with output $s$, the probability of being right given $\tau$ is $\prod_h\Pr(P(U_h)=s_h\mid\tau)\le\prod_hV_h(\tau)$. Averaging over leaves and then over the coins and side information finishes the proof; the query cap and the finite sets of input positions, answers and outputs allow only finitely many deterministic trees. Arbitrary independent randomness therefore reduces to a finite mixture of these behaviours.

Return to the [final gap bound in Section 5](#classical-finish).



# References {.unnumbered}

::: {#refs}
:::

<!-- lean-links -->
[def-F]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L274-L285
[def-Q]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L139-L140
[def-R]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L71-L74
[def-alpha]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L317-L318
[def-wins]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L262-L272
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-all]: https://github.com/wcook04/quartic-query-lean/blob/8357f268732746d1575e05e7de8c888e20ad3793/lean/QuarticCorpus/Unconditional/Challenge.lean#L326-L340
<!-- /lean-links -->
