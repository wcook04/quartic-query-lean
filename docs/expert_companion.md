---
title: "The optimal randomized–quantum query exponent is four"
subtitle: "A companion to OpenAI's nearly quartic separation"
author: "Will Cook"
date: "November 2026"
bibliography: expert_companion.bib
link-citations: true
abstract: |
  There are total Boolean functions $F$ with $R(F)\ge Q(F)^{4-o(1)}$, where $R$ and $Q$ denote bounded-error randomized and quantum query complexity. With the known bound $R=O(Q^4)$, this shows that four is the optimal exponent relating the two measures for total functions, and it refutes the conjectured cubic relation of Aaronson, Ben-David, Kothari, Rao and Tal. The functions and both analyses are due to OpenAI; we give the complete argument with explicit constants. Each of $m$ columns carries its own array of certificates, addressed by the answers to logarithmically many hard Forrelation instances. Classically, the certificate of an unknown column stays out of reach until about $m^{1-1/k}$ queries have been spent in a constant fraction of the columns. A quantum algorithm decodes an address in polylogarithmically many queries and finds the winning column in about $\sqrt m$, by a tournament whose comparisons need to be reliable only for the winner. Together these give $R\approx Q^{4-2/k}$.
---

## 1. Introduction

A query algorithm reads its input one bit at a time and is charged only for the bits it reads. For a partial function $f$, let $R(f)$ and $Q(f)$ be the least worst-case numbers of queries made by a randomized, respectively quantum, algorithm that answers correctly with probability at least $2/3$ on every input in the domain of $f$. Quantum algorithms access the input $x$ only through the oracle $O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle$. All query bounds are worst case: they hold on every input, including inputs outside the domain, and on every random choice and measurement outcome. For total functions we measure the best polynomial relation between the two measures by
$$
\alpha_{\rm tot}=\inf\Bigl\{\alpha\ge0:\ \exists C_\alpha>0\ \forall n\ge1\ \forall f:\{0,1\}^n\to\{0,1\},\ \ R(f)\le C_\alpha\bigl(1+Q(f)\bigr)^\alpha\Bigr\}.
\tag{1}
$$
The constant $C_\alpha$ is uniform in $n$ and $f$, and the added one keeps the right side positive when $Q(f)=0$. We write $m=4^t$ for the number of columns of the construction and $\ell=\log_2 m$.

**Theorem 1** [@OpenAI2026, Theorem 1.1]**.** $\alpha_{\rm tot}=4$. More precisely, for each integer $k\ge2$ there are constants $c_k,C_k>0$ and $b_k$ and, for all sufficiently large powers of four $m$, total functions $F_{k,m}$, defined in §2, with
$$
Q(F_{k,m})\le C_k\sqrt m\,\ell^{b_k}
\qquad\text{and}\qquad
R(F_{k,m})\ge c_k\,\frac{m^{2-1/k}}{\ell^{2}}.
\tag{2}
$$

Aaronson, Ben-David, Kothari, Rao and Tal proved $D(f)=O(Q(f)^4)$ for every total $f$ [@ABKRT2021, Theorem 2], using Huang's sensitivity theorem [@Huang2019], and $R(f)\le D(f)$ gives the upper bound in Theorem 1. They also conjectured that $R(f)=O(Q(f)^3)$ [@ABKRT2021, Conjecture 2]. Taking $k=3$ in (2) gives exponent $10/3>3$ and refutes that conjecture, and choosing $k$ large excludes every exponent below four (§7). Theorem 1 therefore determines the optimal polynomial relation between $R$ and $Q$ for total functions.

The theorem, the functions and both analyses are OpenAI's [@OpenAI2026]. Our proofs make the constants explicit: $b_k=6$ (§4.3), $c_k=1/400$ (§5.5) and the threshold $t\ge13669\,k^2$ (§6), with one circuit $\mathcal C$ serving both bounds. The counting is in §§[5.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-explicit-log6), [6.6](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-floors) and [3.15](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_threshold) of the reasoning record [@Record2026].

### 1.1 Earlier separations

The table below lists the known exponents. The super-quadratic ones before this paper come from the cheat-sheet framework of Aaronson, Ben-David and Kothari [@ABK2016, §3.1]. A partial function $g$ on $n$ bits is composed with $h=\mathrm{AND}_{m'}\circ\mathrm{OR}_{m'}$, which has $R(h)=\Omega(m'^2)$, $Q(h)=O(m')$ and certificates of size $m'$. A quantum algorithm computes $g\circ h$ and Grover-checks a certificate of size $\widetilde O(nm')$ in $\widetilde O(m'+\sqrt{nm'})$ queries, while a randomized algorithm needs $\widetilde\Omega(R(g)\,m'^2)$. If $Q(g)$ is polylogarithmic and $R(g)=\widetilde\Omega(n^c)$, taking $m'=n$ gives $R=\widetilde\Omega(n^{2+c})$ against $Q=\widetilde O(n)$. Forrelation has $c=1/2$; Tal's bound for $k$-fold Rorrelation gives $c=2/3-o(1)$; and the optimal partial separations of Bansal and Sinha and of Sherstov, Storozhenko and Wu give $c=1-o(1)$. Since $R(g)\le n$ for every $g$, the AND–OR recipe stops at the cube, and Aaronson et al. conjectured that three is the truth for all total functions.

| Exponent $a$ with $R=Q^{a}$ (total $f$) | Source |
|---|---|
| $2$ | OR: Grover search and its matching lower bound |
| $5/2$, up to logarithms | Ben-David [@BenDavid2015]; cheat sheets with Forrelation [@ABK2016] |
| $8/3-o(1)$ | Tal [@Tal2020] |
| $3-o(1)$ | Bansal and Sinha [@BansalSinha2021]; independently Sherstov, Storozhenko and Wu [@SSW2023] |
| $4-o(1)$ | OpenAI [@OpenAI2026] |
| upper bound $4$ | $D=O(Q^4)$ [@ABKRT2021], via [@Huang2019] |

### 1.2 Overview of the construction

The input has $m$ columns. Column $i$ holds a string $X_i\in\{0,1\}^m$, $r=20\ell$ inputs $A_{i,1},\dots,A_{i,r}$ to a Forrelation partial function $P=P_{k,m}$, and a separate cell $B_{i,s}$ for every address $s\in\{0,1\}^r$ (Figure 1). The answers $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ select one cell of the column. Column $i$ wins if $X_i$ is all ones and its selected cell certifies $s_i$ and points to a zero in every other column; $F_{k,m}=1$ if some column wins.

![Column $i^\star$ is the winner: $X_{i^\star}$ is all ones, and the cell selected by the answers to its $r$ Forrelation instances points to a zero in every other column. No pointer from any other column can find a zero in $X_{i^\star}$, whatever address that column computes.](figures/expert_column.svg){width=90%}

For the classical lower bound we compare a zero-input, with one zero in each column, against a one-input that erases the zero of a uniformly random column and fills that column's selected cell (§5). The two inputs differ only in those two places. Finding the erased zero means finding one marked zero among $m$ columns of length $m$, which takes about $m^2$ queries.

For the cell, put $L\approx R(P)\approx m^{1-1/k}$ and note that a query to $B_{i,s}$ already names the address $s$. An algorithm making far fewer than $mL$ queries spends more than $L$ queries on the address inputs of only a small fraction of the columns. In any other column, a query to the true cell amounts to predicting all $r$ answers after at most $L$ queries to their instances, and a direct product theorem bounds the chance of that by $(2/3)^r$ per query. Since $L\le m$, neither difference is likely to be seen below about $mL$ queries. Hence
$$
R\approx m\cdot L\approx m^{2-1/k}.
$$
Quantumly, an address costs only polylogarithmically many queries and a search over the $m$ columns costs about $\sqrt m$, so $Q\approx\sqrt m$ up to logarithms and
$$
R\approx m^{2-1/k}=\bigl(\sqrt m\bigr)^{4-2/k}\approx Q^{4-2/k}.
$$

The quantum search needs care. Grover search for a winner would check each candidate by a Grover search over its $K\approx m$ local tests, at a total cost of about $\sqrt m\cdot\sqrt K\approx m$. Instead we compare two columns in polylogarithmically many queries, by decoding both addresses and following each column's pointer into the other. The winner $i^\star$ wins every comparison with high probability: its pointer finds a zero in the rival, and nothing can point to a zero in $X_{i^\star}=1^m$. This holds whatever the rival's address inputs are, including inputs outside the promise of $P$. A comparison between two losers can come out either way, with any probability, so the comparisons can form cycles or be unbiased; the tournament of §4.2 uses only the winner's guarantee.

### 1.3 Relation to earlier constructions

Addressing a certificate by the answers to hard partial instances is the cheat-sheet idea of Aaronson, Ben-David and Kothari [@ABK2016]. Here each of the $m$ columns has its own array of cells, so a classical algorithm pays for an address in a constant fraction of the columns while a quantum algorithm searches them in about $\sqrt m$ steps. The winning condition descends from the pointer functions of Göös, Pitassi and Watson [@GPW2018], which Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs developed into a nearly quartic separation of deterministic from quantum query complexity [@ABBLSS2017].

Their quartic function stores back pointers to the marked column, which make it easy for zero-error randomized algorithms, and reaches the zeros of the other columns through a balanced tree; without back pointers, the tree makes their functions hard even for bounded-error algorithms. They set direct pointers aside because one symbol holding all $m-1$ pointers makes the alphabet exponential [@ABBLSS2017, §1.3]. In $F_{k,m}$ a zero carries no pointer. The pointers that disqualify the other columns sit in the winner's selected cell, behind its hard address, as $m-1$ separate $\ell$-bit fields. A comparison reads only the field that points into its rival, in $\ell+1$ bit queries, and verification checks all of them by a Grover search over the local tests.

The partial function is the $k$-fold Forrelation problem of Aaronson and Ambainis [@AA2018]. Bansal and Sinha proved its randomized hardness in the explicit Walsh–Hadamard form, with the one-sided thresholds used here [@BansalSinha2021]. Sherstov, Storozhenko and Wu independently proved the optimal partial separation for $k$-fold Rorrelation with a uniformly random orthogonal matrix [@SSW2023, Theorem 1.1]. The construction uses the explicit form because it also needs an exact circuit of nearly linear size for the promise and the value of $P$ (property (iii) of §2).

Comparison search has close antecedents. Quantum minimum finding [@DH1996] searches a total order, and king finding [@MPS2023] searches a fixed tournament. Ben-David and Kothari [@BDK2026, Lemma 5] resolve each edge of a fixed tournament of candidate claims by exact local checks and then verify a sink or king. Ambainis, Iraids and Kokainis [@AIK2026, §6.1] keep the candidates that beat every pivot selected so far, in a fixed graph whose edges are computed approximately. These two papers use their searches to separate certificate complexity $C$ from $R$ and from $Q$, and in each a comparison has a fixed intended outcome. Quantum search with bounded-error inputs [@HMW2003] likewise needs every comparison to compute a fixed predicate with bounded error. In $F_{k,m}$ a comparison between two losing columns can have any probability, including $1/2$, and our tournament needs only the winner's one-sided guarantee (§4.2).

Section 2 defines the Forrelation promise and the total function, and Section 3 collects simplifications that fail, each with a counterexample. Sections 4 and 5 prove the quantum and randomized bounds in (2), Section 6 discusses the Forrelation lower bound, and Section 7 deduces $\alpha_{\rm tot}=4$. Section 8 describes the Lean formalisation of Theorem 1. A companion exposition [@Exposition2026] works through the construction on a four-column example, and the reasoning record [@Record2026] contains a full proof of every step.

## 2. The Forrelation promise and the total function

Fix $k\ge2$, $t\ge1$, $m=4^t$, $\ell=2t$ and $r=20\ell$, and identify a bit $a$ with the sign $(-1)^a$. Let $H$ be the normalised $m\times m$ Walsh–Hadamard matrix and $u=m^{-1/2}(1,\dots,1)^{\mathsf T}$. For sign vectors $z_1,\dots,z_k\in\{\pm1\}^m$ put
$$
\Phi(z)=u^{\mathsf T}\operatorname{diag}(z_1)\,H\operatorname{diag}(z_2)\,H\cdots H\operatorname{diag}(z_k)\,u,
\qquad \delta=2^{-5k},
\tag{3}
$$
so that $|\Phi|\le1$. The partial function $P=P_{k,m}$ on $km$ bits is
$$
P(z)=1\ \text{ if }\Phi(z)\ge\delta,\qquad P(z)=0\ \text{ if }|\Phi(z)|\le\delta/2,
\tag{4}
$$
and undefined otherwise; in particular a large negative $\Phi$ lies outside the promise. We use three properties of $P$ [@OpenAI2026, Lemma 2.1].

(i) For fixed $k$ and all large $m$, with $L=\bigl\lfloor m^{1-1/k}/\ell^2\bigr\rfloor$,
$$
L<R(P).
\tag{5}
$$
This follows from Bansal and Sinha's bound $R(P)=\Omega\bigl(k^{-29}(m/\log(km))^{1-1/k}\bigr)$ [@BansalSinha2021, Corollary 1.4]; Section 6 gives a second proof.

(ii) For $0<\eta<1/2$, a quantum algorithm with $O_k(1+\log(1/\eta))$ queries computes $P$ with error at most $\eta$ on its domain. It prepares $u$, applies the product in (3) and measures the projection onto $u$, which succeeds with probability $\Phi^2$; repetition separates $\Phi^2\ge\delta^2$ from $\Phi^2\le\delta^2/4$. The algorithm runs coherently with its workspace retained, and on every input it outputs some bit within the same cap. The interference test of Aaronson and Ambainis, which accepts with probability $(1+\Phi)/2$ [@AA2018, Proposition 6], would serve equally well, since only bounded error on the promise is used: property (iii) certifies the domain.

(iii) An exact fan-in-two Boolean circuit $\mathcal C$ of size $S\le200(k+1)^2m\ell^2$ outputs a domain bit, equal to one exactly on the domain of $P$, and a value bit equal to $P$ there. With the integer matrix $\sqrt m H$ we have $\Phi=N/m^{(k+1)/2}$ for an integer $N$, and the two cases of (4) become $2^{5k}N\ge m^{(k+1)/2}$ and $2^{5k+1}|N|\le m^{(k+1)/2}$, which fast Walsh transforms on $O_k(\ell)$-bit integers decide. The domain bit cannot be read off the projection statistic, which sees only $\Phi^2$ (row 1 of Table 1).

**The total function.** Column $i\in[m]$ consists of a string $X_i\in\{0,1\}^m$, strings $A_{i,1},\dots,A_{i,r}\in\{0,1\}^{km}$, and a cell $B_{i,s}$ for each $s\in\{0,1\}^r$. The cell holds an $\ell$-bit pointer $p_{i,s,j}\in[m]$ for each $j\ne i$ and $r$ alleged transcripts of $\mathcal C$, one bit per non-input gate. All of these are independent input bits. Column $i$ **wins** if $X_i=1^m$, every $P(A_{i,h})$ is defined, and the cell at $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ holds the true transcripts of $\mathcal C$ on each $A_{i,h}$ and pointers with
$$
X_j[p_{i,s_i,j}]=0\qquad\text{for every }j\ne i.
\tag{6}
$$
We set $F_{k,m}=1$ if some column wins and $F_{k,m}=0$ otherwise. The definition imposes no promise on the address inputs, pointers or transcripts, so $F_{k,m}$ is total. At most one column wins, since a winner's pointer into a second all-one column would find a zero there. In all, $F_{k,m}$ has $n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]=O_k(m^{22}\ell^3)$ input bits, since $2^r=m^{20}$.

**Local tests** [@OpenAI2026, Lemma 2.2]. For a pair $(i,s)$, the event that $i$ wins and $s=s_i$ is the conjunction of
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3)
$$
tests: $m$ tests $X_i[y]=1$, $m-1$ pointer tests, one consistency test per gate of each transcript, and two output tests per transcript (domain bit $1$, value bit $s_h$). Induction in topological order shows that a gate-consistent transcript is the true evaluation, so the output tests say that $P(A_{i,h})$ is defined and equals $s_h$. Thus every test passes at $(i,s_i)$ when $i$ wins, and when $i$ does not win some test fails at $(i,s)$ for every address $s$. A gate test makes at most three queries and a pointer test $\ell+1$ adaptive queries, and every test can be evaluated coherently, with its index in superposition, at a constant-factor overhead. The circuit size enters the quantum bound only through the cost $\sqrt K$ of verification (§4.3).

## 3. Simplifications that fail

Table 1 lists steps that are tempting to simplify, each with an instance on which the simplification is false. Rows 1–3 concern the quantum algorithm of §4, rows 4–7 the lower bound of §5, and row 8 the exponent of §7.

: Simplifications and their counterexamples. Here $\beta$ is the best one-instance success within the cap.

| Simplification | Counterexample | Used in |
|:-----------------------|:-------------------------------------------------|:-----------|
| Decide the promise from the projection statistic $\Phi^2$ | $k=2$, $m=4$, $z_1=z_2=(-1,1,1,1)$: $\Phi=-1$, so $\Phi^2=1$, yet $z$ is outside the promise | §2 (iii); [record §3.5](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_small_instance) |
| Treat comparisons as a total order, or as bounded-error queries to a fixed tournament | A deterministic three-cycle of losers is a fixed tournament with no total order; two losers each winning with probability $1/2$ have no bounded-error orientation | §4.2; [record §5.2](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-cyclic-example) |
| Output a column that wins every comparison | All-one column $1$ with a correct certificate except one pointer, into column $j>1$, that reaches a one: column $1$ wins every comparison by the tie-break, yet no column wins | §4.3 |
| Choose the planted column with a uniform marginal law | Query row $1$ of four columns, and choose $I$ uniformly among columns with a found zero, or among all four if there is none: $I$ is uniform, yet its zero is found with probability $175/256>\mathbb EZ/m=1/4$ | §5.3; [record §6.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-selection-independence-example) |
| Cap the address queries in expectation | Two-bit parity, $\beta=1/2$: a fair coin either computes both instances or guesses both; the expected cost is one query each, and the success $5/8$ exceeds $\beta^2$ | §5.1 |
| Allow side information independent of each input separately | $P(x)=x$ on one fair bit, cap $0$, inputs $X,Y$: given $S=X\oplus Y$, answering $(0,S)$ succeeds with probability $1/2>1/4$ | §5.1; [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-independent-information) |
| Condition on the caps being respected | AND on two uniform bits, $\beta=3/4$, two instances: success with the caps respected has probability $5/16\le\beta^2$, while success given that the caps are respected is $5/8>\beta^2$ | §5.4; [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-adaptive-example) |
| Let $k$ grow inside a fixed-$k$ threshold | "$t\ge2^k$" holds eventually for every fixed $k$ and fails for every $t$ when $k=t$ | §7 |

## 4. The quantum upper bound

We now prove the upper bound in (2). The new step is a tournament whose comparisons between losers may be biased arbitrarily (§4.2). It needs a form of amplitude amplification with a fixed cap (Lemma 2), and the short list of candidates it returns is verified by local tests (§4.3). Put $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$.

**Lemma 2** (bounded amplification [@OpenAI2026, Lemma 3.1])**.** Let $\mathcal A$ be a state preparation with a success flag, success probability $p$, and normalised successful state $|g\rangle$ when $p>0$. For $0<\gamma\le1/2$ and $0<\eta<1/2$ there is a procedure making $O(\gamma^{-1/2}\log(1/\eta))$ calls to $\mathcal A$ and $\mathcal A^{-1}$ on every branch, for every $p$, that either reports failure or returns a success; conditional on success its output state is $|g\rangle$ up to a global phase. It fails with probability at most $\eta$ if $p\ge\gamma$, and always if $p=0$.

*Proof sketch.* Write $\mathcal A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle$. After $j$ Grover iterations the successful component is $\sin((2j+1)\theta)|g\rangle$ [@BHMT2002, §2, Lemma 1], so every successful measurement leaves $|g\rangle$. A trial with $j$ chosen uniformly below $M=\lceil10/\sqrt\gamma\rceil$ succeeds with constant probability whenever $p\ge\gamma$ [@BBHT1998, §4, Lemma 2], and a fixed number of fresh trials, stopping at the first success, gives the cap and the failure bound ([record §5.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-amplification-statement)). Search with an unknown success probability bounds its cost only in expectation [@BHMT2002, Theorem 3], which is why the number of trials is fixed in advance.

Our upper bound uses only the law of the label measured after a success.

### 4.1 Comparing two columns

To decode column $i$, we run the algorithm of §2 (ii) on each $A_{i,h}$ with error $\varepsilon/r$, at cost $O_k(r\log(r/\varepsilon))$. If all $r$ instances are promised, then the decoded address is $s_i$ with probability at least $1-\varepsilon$; otherwise the decoder still returns some address within the same cap. For an unordered pair $\{i,j\}$, we sort the indices and run one fixed circuit: decode both columns, read each column's pointer into the other at its decoded address, and inspect the bit it names. A column disqualifies the other if that bit is $0$. If exactly one column disqualifies the other, it is the victor; otherwise the smaller index is. A self-comparison is a loss. Let $a_{ij}$ be the probability that $i$ defeats $j$. Both orders run the same circuit, so
$$
a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0.
\tag{7}
$$
The decoded labels stay in orthogonal registers, so these are also the probabilities measured on the coherent circuit with its workspace retained. If $i^\star$ wins, no pointer finds a zero in $X_{i^\star}=1^m$, and whenever $i^\star$ is decoded correctly its pointer finds a zero in the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every $j\ne i^\star$, whatever the rival's address inputs. One comparison costs $c=O_k(\ell\log\ell)$ queries.

### 4.2 A tournament with probabilistic comparisons

**Proposition 3** [@OpenAI2026, Proposition 3.2]**.** Let a comparison circuit, coherently controlled by two candidate indices, reversible with all its workspace retained and making at most $c$ queries on every input, report $i$ defeating $j$ with probabilities satisfying (7). A quantum algorithm with $O(c\sqrt m\,T^2\log T)$ queries on every branch returns at most $T$ candidates, and if some $i^\star$ has $a_{i^\star j}\ge1-\varepsilon$ for all $j\ne i^\star$, the list contains $i^\star$ with probability at least $1-2m2^{-T}-T\varepsilon$. Probabilities are over measurements, for a fixed input.

Ambainis, Iraids and Kokainis keep the set of candidates that beat every pivot drawn so far. We replace membership in that set by the weight $w_i=\prod_b a_{i\rho_b}$, the probability that $i$ beats every pivot $\rho_1,\rho_2,\dots$ drawn so far, and draw each new pivot with probability proportional to its weight. The total weight then halves in expectation at every step, while the winner keeps weight above $1/2$ until it is drawn, so it is drawn within $T$ steps with high probability. A list is enough because §4.3 verifies each listed candidate at a cost of about $\sqrt K$. Its length and its cost are bounded on every input; only the guarantee that it contains $i^\star$ requires a winner to exist.

*Ideal process.* Start with weights $w_i=1$ and $W=\sum_iw_i$. For at most $T$ steps, and only while $W>0$, draw a pivot $\rho$ with probability $w_\rho/W$, append it to the list, and update $w_i\leftarrow w_i\,a_{i\rho}$. Pairing the terms $(i,\rho)$ and $(\rho,i)$ by (7) gives
$$
\mathbb E[W_{\rm new}\mid w]=\frac1W\sum_{\rho,i}w_\rho w_i a_{i\rho}=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\tag{8}
$$
No order or transitivity enters, so cycles among losers do no harm. After $T$ steps $\mathbb EW\le m2^{-T}$. Until $i^\star$ is drawn its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$, so by Markov's inequality $i^\star$ is missing from the ideal list with probability at most $2m2^{-T}$.

*Exact sampling.* The algorithm never computes the weights. Given pivots $\rho_1,\dots,\rho_n$ with $n<T$, it prepares
$$
\frac1{\sqrt m}\sum_{i=1}^m|i\rangle\bigotimes_{b=1}^{n}|\phi(i,\rho_b)\rangle,
\tag{9}
$$
where $|\phi(i,\rho_b)\rangle$ is the full comparison state in a fresh workspace, and flags success when every comparison says that $i$ wins. For the fixed input and history, the tensor product gives success-and-label mass $m^{-1}\prod_ba_{i\rho_b}=w_i/m$. The total success probability is therefore $W/m$, and the label law conditional on success is $w_i/W$. We apply Lemma 2 with $\gamma=1/(2m)$ and $\eta=\varepsilon$ and measure the returned label, which becomes the next pivot; on reported failure we stop and return the list ([record §5.2](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-quantum-tournament)).

*Coupling.* Until $i^\star$ is drawn, $W/m\ge1/(2m)$, so at every such history the stage fails with probability at most $\varepsilon$ and otherwise draws a pivot with the ideal law. The failure probabilities may depend on the history, so we couple the two processes stage by stage, conditional on the entire past. This adds at most $T\varepsilon$ to the miss probability, and a failure after $i^\star$ is listed does not remove it ([record §5.2](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-coupling)). Stage $n$ costs $O(c(n+1)\sqrt m\log(1/\varepsilon))$ queries whether or not a dominant candidate exists, and summing over $n<T$ proves the proposition.

### 4.3 Verification and the query count

A column that beats every rival with probability at least $1-\varepsilon$ need not win (row 3 of Table 1), so we verify each listed candidate. We decode its address afresh and measure it. At the measured address, a uniformly random one of the $K$ local tests fails with probability $0$ if all pass and with probability at least $1/K$ otherwise, so Lemma 2 with $\gamma=1/K$ and $\eta=\varepsilon$ searches for a failing test in $O(\sqrt K\,\ell\log(1/\varepsilon))$ queries. We reject the candidate if a failing test is found and accept it otherwise, and we accept the input if some candidate is accepted.

A column that does not win fails some test at every address (§2), including addresses decoded from unpromised instances, so it is accepted with probability at most $\varepsilon$; the winner is accepted whenever its address is decoded correctly. The error is therefore at most $T\varepsilon$ on zero-inputs and at most $2m2^{-T}+T\varepsilon+\varepsilon<1/3$ on one-inputs. Pointers are read bit by bit, array indices are computed reversibly, and a controlled query costs two ordinary queries, so no unit-cost pointer oracle is assumed.

The exponent six in (2) comes from a deliberately loose count, with $\log(1/\varepsilon)\le1/\varepsilon=O(\ell)$. In this count a comparison costs $O_k(\ell^3)$, and a tournament stage, padded to $T$ comparisons per call, uses $O(\ell)$ trials of $O(\sqrt m)$ iterations, so the $T$ stages cost $O_k(\sqrt m\,\ell^6)$. A verification costs $O_k(\ell^3)$ for its decoder plus $O(\ell)$ trials of $O(\sqrt K)=O_k(\sqrt m\,\ell^{3/2})$ iterations of $O(\ell)$ queries, so the $T$ verifications cost $O_k(\sqrt m\,\ell^5)$. The total is $O_k(\sqrt m\,\ell^6)$ ([record §5.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-explicit-log6)), and nothing below depends on the logarithmic exponent.

## 5. The randomized lower bound

We now prove the lower bound in (2). A planted one-input (§5.2) differs from a zero-input only at an erased zero and a filled cell; §5.3 bounds the chance of finding the first, and §5.4 bounds the chance of finding the second through a direct product theorem (§5.1). The argument applies to any partial function $P$ with an exact circuit as in §2 (iii) and any integer $L$ with $1\le L\le m$ and $L<R(P)$. Since $L<R(P)$, the best worst-case success of a randomized algorithm of depth $L$, which is attained, is below $2/3$. By finite minimax [@Yao1977] there is therefore a law $\mu$ on the domain of $P$ under which every deterministic tree of depth at most $L$ succeeds with probability at most $\beta=2/3$. This law is supported on the promise. It need not be the planted law of §6, which gives mass to inputs outside the promise.

### 5.1 A direct product with separate caps

**Lemma 4** [@OpenAI2026, Lemma 4.1]**.** Let $U_1,\dots,U_r$ be independent with law $\mu$. An algorithm that makes at most $L$ queries to each $U_h$ on every branch, interleaving them adaptively, outputs $(P(U_1),\dots,P(U_r))$ with probability at most $\beta^r$. Its random coins and any side information are allowed if they are jointly independent of $(U_1,\dots,U_r)$.

*Proof.* We work with unnormalised measures, so that branches of probability zero need no conditioning. For a nonnegative measure $\nu$ on the domain of $P$, let $V_d(\nu)$ be the largest $\nu$-weight of inputs on which a depth-$d$ tree answers correctly. Then $V_0(\nu)=\max_b\nu(P=b)$ and
$$
V_{d+1}(\nu)=\max\Bigl\{V_d(\nu),\ \max_y\bigl[V_d(\nu_{y,0})+V_d(\nu_{y,1})\bigr]\Bigr\},
$$
where $\nu_{y,b}$ is the restriction of $\nu$ to inputs with bit $y$ equal to $b$. For product measures $\nu_1\otimes\dots\otimes\nu_r$ and remaining budgets $L_1,\dots,L_r$, induction on a deterministic vector-output tree shows that its weight of fully correct inputs is at most $\prod_hV_{L_h}(\nu_h)$. At a leaf the correct weight factorises. A query to input $h$ restricts only $\nu_h$ and lowers only $L_h$, and the recursion absorbs its two branches. Initially every factor is at most $\beta$. We fix the coins and side information, apply this bound, and average. $\square$

The caps must hold on every branch and the independence must be joint (rows 5 and 6 of Table 1). Per-path allowances go back to Shaltiel's fair trees, for XOR advantage under uniform inputs [@Shaltiel2003], and Drucker's Lemmas 3.1–3.2, specialised at the end of his §3, give this product bound [@Drucker2012]. Drucker's Theorem 1.1, with one global budget, would also serve. The simulator of §5.4 has total cap $L$, and his theorem with budget $L$, error $1/3$ and $\alpha=3/r$ bounds its success by $2\beta^r$, a factor of two that (14) absorbs. We use the separate-cap form because it gives $\beta^r$ exactly and has the short proof above ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-literature-and-verification)).

### 5.2 Planting a winner

Let $G=\lfloor mL/100\rfloor$. The **dummy input** $Y^{(0)}$ chooses rows $J_1,\dots,J_m\in[m]$ uniformly, puts a single zero at $X_i[J_i]$, draws every $A_{i,h}$ from $\mu$, all mutually independent, and leaves every cell blank. It has no winner. Choose $I\in[m]$ uniformly and independently of all of $Y^{(0)}$. The **planted input** $Y^{(1)}$ erases the zero of column $I$ and fills only the cell $B_{I,s_I}$, with the true transcripts and the pointers $p_{I,s_I,j}=J_j$, so column $I$ wins (Figure 2). The blank array and the single filled cell follow the cheat-sheet lower bound of Aaronson, Ben-David and Kothari [@ABK2016]. The search for one marked zero among one zero per column already appears in Ben-David's lower bound [@BenDavid2015]. The unknown column $I$ supplies the factor $m$.

![The two coupled inputs. They differ only at the erased zero $X_I[J_I]$ and inside the cell $B_{I,s_I}$; the address inputs, drawn from $\mu$, are the same in both.](figures/expert_planted.svg){width=80%}

Fix a deterministic tree $\mathcal T$ of depth at most $G$. Its runs on $Y^{(0)}$ and $Y^{(1)}$ agree until the run on $Y^{(0)}$ queries $X_I[J_I]$ or a bit of $B_{I,s_I}$, so
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|
\le\Pr[\mathcal T\text{ queries }X_I[J_I]]+\Pr[\mathcal T\text{ queries }B_{I,s_I}],
\tag{10}
$$
with both probabilities computed for the run on $Y^{(0)}$.

### 5.3 The erased zero

Let $Z$ be the number of columns whose zero the run on $Y^{(0)}$ queries. For fixed dummy data, exactly $Z$ of the $m$ choices of $I$ select a discovered zero, so
$$
\Pr[\mathcal T\text{ queries }X_I[J_I]]=\frac{\mathbb EZ}{m}.
\tag{11}
$$
This identity uses the independence of $I$ from the whole dummy run; a uniform marginal law for $I$ is not enough (row 4 of Table 1).

To bound $\mathbb EZ$ we count early and late discoveries, as the preprint does. A query to $X_i$ made while fewer than $m/2$ rows of $X_i$ have been queried finds the zero with probability at most $2/m$ given the past, since $J_i$ is uniform on the unqueried rows; these early discoveries number at most $2G/m$ in expectation. Any other discovery lies in a column that receives at least $m/2$ queries, and there are at most $2G/m$ such columns. Hence
$$
\mathbb EZ\le\frac{4G}m,\qquad
\Pr[\mathcal T\text{ queries }X_I[J_I]]\le\frac{4G}{m^2}.
$$
A sharper count gives $2G/(m(m+1))$ ([record §6.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-zero-optional)), which the constants below do not need.

### 5.4 The planted cell

Let $\lambda_i$ be the number of queries, counting repetitions, that the run on $Y^{(0)}$ makes to $A_{i,1},\dots,A_{i,r}$, and call column $i$ heavy if $\lambda_i>L$. At most $G/L$ columns are heavy, and therefore $\Pr[I\text{ heavy}]\le G/(mL)$.

The position of a query already names an address: a query to a bit of $B_{i,s}$ names $s$ before any content of the cell is read. We turn this into a predictor for the answers of one column. Fix a column $i$ and a time $\tau\in\{1,\dots,G\}$. A simulator receives as free information all of $Y^{(0)}$ outside $A_{i,1},\dots,A_{i,r}$, which is jointly independent of those $r$ inputs and does not reveal $s_i$. It runs $\mathcal T$, answering other queries from the free information and querying the $A_{i,h}$ itself, and it aborts before an $(L+1)$-st query to them in total. If it reaches time $\tau$ and the $\tau$-th query lies in a cell $B_{i,s}$, it outputs $s$; otherwise it outputs a fixed vector. Its total cap of $L$ on the $A_{i,h}$ implies a cap of $L$ on each, so Lemma 4 applies. If $i$ is not heavy and the $\tau$-th query of the original run lies in $B_{i,s_i}$, the simulator has not aborted and outputs $s_i$. Therefore
$$
\Pr\bigl[\,i\text{ is not heavy and the }\tau\text{-th query lies in }B_{i,s_i}\bigr]\le\beta^r .
\tag{12}
$$
This bounds a joint event under the original law. Conditioning on the event that $i$ is not heavy would change the law of the address inputs and can make the conditional success exceed $\beta^r$ (row 7 of Table 1). Summing (12) over the $G$ times, averaging over the independent $I$, and adding the heavy columns gives
$$
\Pr[\mathcal T\text{ queries }B_{I,s_I}]\le\frac G{mL}+G\beta^r
\tag{13}
$$
([record §6.5](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-simulator)).

### 5.5 The contradiction and the constants

By (10), (11) and (13), with $G\le mL/100\le m^2/100$ and $\beta^r=(2/3)^{20\ell}\le m^{-10}$,
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|\le\frac{4G}{m^2}+\frac G{mL}+G\beta^r\le\frac6{100}.
\tag{14}
$$
Each parameter has its own role here. The unknown column $I$ divides the first two terms by $m$, the address length $r=20\ell$ makes $\beta^r$ small enough to survive the union over $G$ query times, and the constants $1/100$ and $20$ leave slack. A randomized algorithm of worst-case cost $G$ is an average of such trees, so it satisfies (14) as well, whereas error at most $1/3$ on the zero-input $Y^{(0)}$ and the one-input $Y^{(1)}$ would force a gap of at least $1/3$. Hence, for every $P$ and $L$ as above,
$$
R(F_{k,m})>\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor.
\tag{15}
$$

For the constant in (2), take $k\ge2$ and $t\ge8$. Then $4t^2\le2^t\le m^{1-1/k}$, so $x=m^{1-1/k}/\ell^2\ge1$ and $L=\lfloor x\rfloor\ge x/2$; also $mL\ge200$, so $\lfloor mL/100\rfloor\ge mL/200\ge m^{2-1/k}/(400\ell^2)$. Section 6 gives $L<R(P_{k,m})$ for $t\ge13669k^2$. The full proof is in [§6 of the record](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-direct-product-statement), with this assembly in [§6.6](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-discrepancy).

## 6. The Forrelation lower bound

The lower bound uses only (5), the fixed-$k$, constant-error consequence of Bansal and Sinha's theorem [@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. A second proof, which the Lean formalisation follows, gives a bound uniform in $k$: for $m=4^t$ and $15k+2\le2t$,
$$
R(P_{k,m})>\frac{2}{18225}\,\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{16}
$$
For $t\ge13669k^2$ one has $15k+2\le2t$, $\ln(4km)\le6t$ and $8t^2>109350\,k^2t$, so (16) exceeds $m^{1-1/k}/\ell^2$ and implies (5). Compared with Bansal and Sinha's bound, (16) has a better power of $k$ and a worse power of the logarithm. Theorem 1 needs only (5); the uniformity of (16) in $k$ is used in the remark of §7.

The proof compares the uniform law with a planted law from Bansal and Sinha's rounded Gaussian chain and bounds a shallow tree's acceptance gap through derivatives of its multilinear extension, by a stopped-martingale induction in the style of Girish, Tal and Wu [@GTW2021]. The planted law is not supported on promised one-inputs. Because the promise is one-sided, a solver of cap $D$, amplified to small error and run as a tree of depth $50kD+1$, still separates the two laws by a constant multiple of $18^{-(k-1)}$, while the derivative bound forbids such a gap below the depth in (16). The full proof is in [§§3.6–3.15 of the record](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_target), assembled in [§3.15](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_uniform_assembly); [§3.16](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_credit) compares it with the published proofs.

## 7. The optimal exponent

Fix $0\le\alpha<4$ and choose an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $e=2-1/k-\alpha/2>0$. Keep $k$ fixed and let $m=4^t$ grow. For $t\ge13669k^2$, (2) with $b_k=6$ and $c_k=1/400$ gives $1+Q(F_{k,m})\le(1+C_k)\sqrt m\,\ell^6$ and
$$
\frac{R(F_{k,m})}{\bigl(1+Q(F_{k,m})\bigr)^\alpha}\ge\frac{1}{400(1+C_k)^\alpha}\,\frac{m^{e}}{\ell^{2+6\alpha}}\longrightarrow\infty,
$$
so no $C_\alpha$ in (1) exists. With the upper bound of [@ABKRT2021], $\alpha_{\rm tot}=4$. The quantifiers come in the order: the exponent $\alpha$, then one fixed $k$, then its constants and threshold, then $m\to\infty$, with one circuit $\mathcal C$ serving both bounds in (2). For fixed $k$ this excludes exponents below $4-2/k$ only, and it gives no separation of the form $R=\Omega(Q^4)$.

**Remark** (letting $k$ grow)**.** A single family with $k$ growing in $m$ needs bounds uniform in $k$ (row 8 of Table 1). The bounds (16) and (15) and the [explicit quantum bound][src-budget-exponential] $Q(F_{k,m})\le2^{53}k\,2^{10k}\sqrt m\,\ell^6$ supply them. With $k=\lfloor\sqrt{t/20}\rfloor$ and $t\ge80$, a comparison of logarithms gives $R(F_t)\ge Q(F_t)^{4-\varepsilon(\ell)}$ for $F_t=F_{k,4^t}$, where $\varepsilon(\ell)=8\sqrt{10/\ell}+(56\log_2\ell+508)/\ell$ ([record §7.3](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#ROOT-GROWING-K)). The exponent tends to four, and the family still gives no bound $R=\Omega(Q^4)$.

## 8. The formal statement

Theorem 1 and the failure of the cubic bound are formalised in Lean 4 with Mathlib [@Repo2026]. The [statement file][statement-file] imports only Mathlib. It contains the definitions of §§1–2 and the statements of four theorems: [$\alpha_{\rm tot}=4$][thm-alpha], [the family of Theorem 1][thm-headline], [the failure of every bound $R(f)\le C\,Q(f)^3$][thm-cubic], and [the Forrelation bound (5) beyond some threshold][thm-forrelation]. Their [proofs][statement-solution] are compiled separately, and the Comparator tool checks that the compiled proofs have exactly these statements and use only Lean's standard axioms (propositional extensionality, quotient soundness and choice).

The definitions follow §1. A randomized algorithm is a finite mixture of decision trees with positive weights, and a quantum algorithm applies unitaries fixed before the input and reaches $x$ only through $O_x$. Query caps count oracle calls on every branch, so they hold on every input, and both models must succeed with probability at least $2/3$ on every promised input. These are the usual models: grouping the random choices of a capped algorithm gives a finite mixture ([§2.2 of the record](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#R3-01-CLASSICAL)), and a capped quantum program has the output probabilities of a fixed query sequence with measurements deferred ([§2.5](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#R3-01-BRIDGES)).

The quantities $R$, $Q$ and $\alpha_{\rm tot}$ are infima, and an empty infimum would make an upper bound vacuous. The sets defining $R$ and $Q$ are nonempty because reading every bit is an admissible algorithm (§§[2.2](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#R3-01-CLASSICAL) and [2.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#R3-01-ADAPTIVE) of the record), and the set defining $\alpha_{\rm tot}$ is nonempty because the formal Theorem 1 also proves the power bound with exponent four.

The formal Theorem 1 quantifies as $\forall k\ge2\ \exists S,A,b,t_0\ \forall t\ge\max(1,t_0)\ \exists\mathcal C$. One circuit $\mathcal C$ realising $P_{k,4^t}$, of size at most $S\,m(2t)^2$, serves both $Q(F_{k,m})\le A\,2^t(2t)^b$ and $\lfloor mL/100\rfloor<R(F_{k,m})$. Its logarithmic exponent $b$ is existential, and its lower bound is the floor form (15), which gives the form in (2) once $t\ge8$. The constants $b=6$ and $1/400$ are proved in a [separate theorem][src-constants] for a named circuit.

Lean also proves the [uniform bound (16)][src-forrelation-uniform] and the following forms of the lemmas of §§4–5. The [amplification lemma][cmp-amplifier] is proved for one procedure fixed before the preparation, for success flags that test basis labels: it returns the successful state of $\mathcal A$ tensored with an auxiliary vector, with the exact success mass. The upper bound uses a separate measured form, for a procedure that measures the label and resets its workspace, which fixes the [law of the measured label][src-amplify-measured]; Lean does not identify the two procedures. The [direct product lemma][cmp-direct-product] is proved for finitely many weighted random seeds. It bounds the probability of [success together with compliance][def-compliant], where compliance is a recursive condition on the tree that encodes the caps, and so it also covers trees that exceed them. The reduction from arbitrary independent randomness to finitely many seeds and the identification of compliance with per-input query counts are ordinary arguments (§[6.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-independent-information) and Appendix [G.8](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-direct-product-formal) of the record). Appendix [G.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#checked-statements) of the record lists every formal statement cited here together with its relation to the printed one.

## Use of AI tools

This paper and its Lean development were prepared with AI systems under the author's direction. Sources, proofs and the full argument are in the repository [@Repo2026] and the reasoning record [@Record2026].

## References

::: {#refs}
:::

<!-- lean-links -->
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[def-compliant]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L111-L120
[src-amplify-measured]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticQuery/Upper/Amplify.lean#L345-L352
[src-budget-exponential]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticQuery/Upper/Bound.lean#L286-L290
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[src-forrelation-uniform]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
