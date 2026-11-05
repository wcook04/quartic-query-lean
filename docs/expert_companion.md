---
title: "Reconstructing OpenAI’s nearly quartic query separation"
subtitle: "Comparing candidates and predicting a hidden address"
author: "Will Cook"
date: "November 2026"
bibliography: expert_companion.bib
link-citations: true
header-includes:
  - \usepackage{float}
  - \floatplacement{figure}{H}
abstract: |
  OpenAI proved that four is the optimal exponent relating randomized and quantum query complexity for total Boolean functions. We reconstruct the two reductions. A certificate in one of $m$ columns points to a zero in every rival. A quantum algorithm reads these pointers in pairs and samples a short list before verifying any certificate. Even arbitrary comparison probabilities among losers cancel from the expected surviving weight if each pivot is drawn in proportion to its own weight. Classically, a query to the winning certificate has to name its address, predicting an entire vector of hard answers. A random choice of winning column makes it unlikely that an algorithm has spent enough queries there to do so. The resulting bounds are $\widetilde O_k(\sqrt m)$ quantum queries and $\widetilde\Omega_k(m^{2-1/k})$ randomized queries for each fixed $k\ge2$.
---

## 1. The fourth power

Suppose one of $m$ columns claims to be the only all-one column. To defeat a rival, it need only point to a zero there. Now give every column a proposed certificate with one pointer per rival. The genuine winner can use a single pointer to defeat *any* opponent, while even a fabricated certificate cannot point to a zero in the winner. OpenAI [@OpenAI2026] exploits this asymmetry to find a short list of candidates. Searching over $m$ columns with a full $\widetilde O(\sqrt m)$ verification at each step would cost $\widetilde O(m)$ queries. Comparing columns first puts the two searches in succession, each at cost $\widetilde O(\sqrt m)$.^[Will Cook directed this reconstruction. AI systems drafted and revised the manuscripts and Lean proofs.]

Where should the certificates be kept? Each column gets an array indexed by answers to instances of a partial function $P$. A quantum decoder can find the winner's address cheaply. To read even a single certificate bit, a classical algorithm must name an entire address before the bit comes back. A small budget leaves most columns scarcely queried. For a suitable $P$, the chance of guessing the address in any such column is tiny. Forrelation supplies such a $P$, together with a small exact circuit that lets the verifier reject false claims about its promise.

**Theorem 1** (OpenAI [@OpenAI2026, Theorem 1.1]). *For each fixed integer $k\ge2$ there are total Boolean functions $F_{k,m}$ indexed by powers of four $m\ge4$. With $\ell=\log_2m$ and a constant $C_k$ depending only on $k$,*
$$
 Q(F_{k,m})\le C_k\sqrt m\,\ell^6,
 \qquad R(F_{k,m})\ge \frac{m^{2-1/k}}{400\ell^2}.
\tag{1}
$$
*The quantum bound holds for all such $m$ and the randomized bound for all sufficiently large $m$. The optimal universal exponent in $R(f)=O((1+Q(f))^\alpha)$ for total Boolean $f$ is four.*

We use worst-case bit-query caps and error at most $1/3$. For a partial function the cap applies on every input and branch, the error bound on its domain. The power six and coefficient $1/400$ in (1) are explicit choices in this reconstruction.^[The [complete reconstruction](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md) derives the supporting results, including the [uniform estimates](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#ROOT-GROWING-K) for a growing $k$. The [theorem index](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md) gives the Lean proofs of the optimal exponent and the quantitative bounds.]

Aaronson, Ben-David, Kothari, Rao and Tal proved the upper bound $R\le D=O(Q^4)$ and conjectured $R=O(Q^3)$ [@ABKRT2021, Conjecture 2]. The balanced AND–OR cheat sheets of Aaronson, Ben-David and Kothari [@ABK2016, §3], using optimal partial separations [@BansalSinha2021; @SSW2023], give powers approaching three.

\Needspace{8\baselineskip}

OpenAI gives each column of a pointer function [@GPW2018; @ABBLSS2017] its own cheat sheet. For a partial function on $\Theta_k(m)$ bits with a polylogarithmic quantum decoder, an exact circuit of size $\widetilde O_k(m)$ and $1\le L\le m$ below its randomized complexity, the same one-instance lower bound gives these estimates up to logarithms:
$$
\begin{array}{lcc}
 & \text{quantum upper bound} & \text{randomized lower bound} \\
 \text{balanced AND–OR cheat sheet} & m & m^2 L \\
 \text{one array per column} & \sqrt m & m L .
\end{array}
$$
For Forrelation one may take $L=\widetilde\Omega_k(m^{1-1/k})$. Giving up a factor of $m$ on the classical side while halving the quantum exponent takes the separation from $3-1/k$ to $4-2/k$. Already $k=3$ rules out the cube.

## 2. The certificate

A convincing all-one column needs two kinds of evidence. Its pointers must exhibit a zero in each rival, and the cell containing them must really be the one named by its address inputs. An exact Boolean circuit $\mathcal C$ for the domain and value of $P$ supplies the latter evidence. Its first output is one exactly on the promise, and its second equals $P$ there. Fix its wiring once. A proposed evaluation can then be checked gate by gate, even on an input for which the quantum decoder has no correctness guarantee.

Write $[m]=\{1,\ldots,m\}$ and $r=20\log_2m$. Column $i$ contains a string $X_i\in\{0,1\}^m$, $r$ inputs $A_{i,1},\ldots,A_{i,r}$ to $P$, and an array of cells $B_{i,s}$ indexed by $s\in\{0,1\}^r$. Each cell holds a proposed transcript of $\mathcal C$ on each of the $r$ inputs, together with one row pointer $p_{i,s,j}\in[m]$ for each $j\ne i$. A transcript supplies one bit per non-input gate in the fixed circuit. Every $\ell$-bit pointer encodes a row.

Column $i$ **wins** if $X_i=1^m$, all its address inputs belong to the domain of $P$, and the cell with label
$$
s_i=\bigl(P(A_{i,1}),\ldots,P(A_{i,r})\bigr)
$$
contains the true transcripts and points to a zero in every other column. The function outputs one if a column wins, zero otherwise. This defines a total Boolean function on the freely chosen input bits. In particular an off-promise column loses, whatever is written in its cells. Two winners are impossible because neither all-one column could point to a zero in the other.

![The all-one column $i^\star$ and its selected cell. Each other column has an array of its own. Following just the pointer for $j$ disqualifies that rival.](figures/expert_column.svg){width=85%}

If a claimed address $s$ is false, where can a verifier catch it? Test the $m$ bits of $X_i$ and follow the $m-1$ outward pointers. For each address input test the transcript against every gate of $\mathcal C$ and test the two outputs against $(1,s_h)$. A consistent transcript must be the true evaluation, by induction in circuit order. A fabricated transcript therefore fails at some gate, and a true transcript for an undefined input or wrong answer fails an output test. In particular a losing column has a defect at *every* address. This gives the verifier a search problem with
$$
 K=m+(m-1)+r(S+2)
\tag{2}
$$
tests, where $S$ counts non-input gates of fan-in at most two. Each test reads at most $\max\{3,\ell+1\}$ bits. Both query bounds concern this same circuit and the function encoded by its cells.

The next two arguments use only the following properties of $k$-fold Forrelation [@OpenAI2026, Lemma 2.1]. A reversible decoder for $P$ with error $\eta$ on its domain costs $O_k(1+\log(1/\eta))$ queries on every input. An exact circuit as above has $S=O_k(m\ell^2)$, making $K=O_k(m\ell^3)$. Finally, for fixed $k$ and sufficiently large $m$,
$$
 L:=\left\lfloor m^{1-1/k}/\ell^2\right\rfloor < R(P).
\tag{3}
$$
We use the first two properties to find a certificate and the third to hide it. Section 5 identifies the promise and the circuit that supply them.

## 3. Finding a winner by comparison

### 3.1 What one comparison reveals

Decode the two column addresses, follow the two pointers directed at each other, and favour the column whose pointer finds a zero when the other finds a one. Break ties by smaller index. Suppose $i^\star$ wins. With its address decoded correctly, its pointer finds a zero. Whichever cell its rival decodes, the return pointer goes into $X_{i^\star}=1^m$ and reads a one. This comparison works even when none of the rival's address inputs obeys the promise.

Write $\varepsilon$ for the allowed error in decoding a promised column. Running the decoder on each address bit with error $\varepsilon/r$ suffices. Use the same coherent circuit for each unordered pair, retaining both decoded addresses, and assign a loss to self-comparison. Since the two directions now denote complementary outcomes of *one* comparison, the probabilities $a_{ij}=\Pr[i\text{ defeats }j]$ on a fixed input satisfy
$$
 a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0.
\tag{4}
$$
Only the winning column has a dominance guarantee, $a_{i^\star j}\ge1-\varepsilon$ for every $j\ne i^\star$. The probabilities between losers may lie anywhere in $[0,1]$. One comparison or its inverse costs $c=O_k(r\log(r/\varepsilon)+\ell)$ queries.

### 3.2 A tournament with probabilistic comparisons

**Probabilistic tournament** [@OpenAI2026, Proposition 3.2]. *Given a reversible $c$-query comparison satisfying (4), controlled by the candidate indices, a quantum algorithm returns $O(\log m)$ candidates using $\widetilde O(c\sqrt m)$ queries on every input. If a candidate loses to each rival with probability at most $b/\log_2(2m)$ for a sufficiently small absolute constant $b>0$, the list contains it with probability at least $0.99$.*

For fixed comparison outcomes one can keep precisely the candidates that beat all previous pivots and draw uniformly from this set [@AIK2026, §6.1]. For fractional comparisons the analogue of membership is the probability of beating those pivots in fresh comparisons. After pivots $\rho_1,\ldots,\rho_n$, this gives weights
$$
 w_i=\prod_{h=1}^n a_{i\rho_h},\qquad W=\sum_i w_i.
$$
\Needspace{9\baselineskip}

Initially all weights are one. A pivot $j$ updates $w_i$ to $w_i a_{ij}$ and removes itself. How should we draw $j$ once the weights are unequal? For a pivot law $q$, the pair $i,j$ contributes $w_i q_j a_{ij}+w_j q_i a_{ji}$ to the expected remaining mass. A uniform pivot leaves the larger weight on one direction. To cancel the bias we need equal coefficients, $w_i q_j=w_j q_i$. Drawing $j$ with probability $w_j/W$ achieves this for every pair. Hence, while $W>0$,
$$
 \mathbb E[W_{\rm new}\mid w]
 =\frac1W\sum_{i,j}w_i w_j a_{ij}
 =\frac{W^2-\sum_i w_i^2}{2W}
 \le\frac W2.
\tag{5}
$$
The sum pairs two independent draws from the weights. On distinct draws either is equally likely to defeat the other, and coincident draws contribute zero.

Stop on extinction, keeping $W=0$ thereafter. After $T$ steps the expected mass is at most $m2^{-T}$. An unselected dominant candidate, however, still has weight at least $(1-\varepsilon)^T\ge1-T\varepsilon$. Take $T=\lceil\log_2(1000m)\rceil$ to make the first quantity small and $\varepsilon=1/(1000T)$ to keep the second above $1/2$. Missing this candidate now requires more than half a unit of weight to survive. By Markov's inequality that happens with probability at most $2m2^{-T}$.

How does the algorithm draw this pivot? It has access to the comparison circuit but none of the numbers $a_{ij}$. Fix the measured pivots so far. Prepare a uniform superposition of $i$, and, controlled on $i$, compare it with each pivot using a fresh workspace. If $|\phi(i,\rho_b)\rangle$ is the entire state of one comparison, the preparation produces
$$
 \frac1{\sqrt m}\sum_i |i\rangle\bigotimes_{b=1}^n |\phi(i,\rho_b)\rangle.
$$
Flag the event that *all* comparisons favour $i$. Within a fixed label the independent comparison registers multiply the success probabilities. Across distinct labels their masses add. Consequently
$$
 \Pr[i\text{ and flag}]=\frac{w_i}{m},\qquad
 \Pr[\text{flag}]=\frac Wm,\qquad
 \Pr[i\mid\text{flag}]=\frac{w_i}{W}.
\tag{6}
$$
The same half unit of surviving weight pays for this draw. Before the dominant candidate has been selected, its contribution alone gives flag probability $W/m>1/(2m)$. Thus a procedure that can amplify from threshold $1/(2m)$ will suffice throughout the part of the run where failure matters.

For a reversible preparation and a query-free flag, bounded amplitude amplification at threshold $\gamma$ costs $O(\gamma^{-1/2}\log(1/\eta))$ calls to the preparation and its inverse on every branch. If the flag probability is at least $\gamma$, failure has probability at most $\eta$. What matters here is the label it returns on success. Grover rotations preserve the direction of the flagged component, so every successful trial has exactly the conditional law in (6) [@BBHT1998; @BHMT2002; @OpenAI2026, Lemma 3.1]. The [bounded schedule](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#upper-small-probability) works without knowing the flag probability.

Set $\gamma=1/(2m)$ and $\eta=\varepsilon$. Append the measured pivot on success, stopping on failure or after $T$ draws. At every history before the dominant candidate appears, we can couple a successful transition to the ideal draw, with probability at most $\varepsilon$ of stopping instead. Consequently
$$
 \Pr[i^\star\text{ absent from the list}]\le 2m2^{-T}+T\varepsilon.
\tag{7}
$$
Only the measured pivots persist. A stage with $n$ pivots rebuilds their comparisons for $O(c(n+1)\sqrt m\log T)$ queries. Summing over the $T$ stages gives the worst-case cap $O(c\sqrt m\,T^2\log T)$ and proves the tournament assertion.

### 3.3 Paying for verification

The tournament must find the winner on a one-input. On a zero-input it may return *any* list of at most $T$ columns. Even a column with false transcripts might beat every rival. The verifier must reject such a column at whichever address its decoder supplies.

For each listed column decode a fresh address with error at most $\varepsilon$ on promised inputs, then search the $K$ local tests at that address for a defect. A uniform test flags a defect with probability at least $1/K$ whenever any test fails. Evaluating the test reversibly and using the bounded search above costs $O(\ell\sqrt K\log(1/\varepsilon))$ queries. Accept if the search finds no defect for some column. At the winner's true address no test can flag, so listing the winner and decoding it correctly suffice for acceptance. A one-input is rejected with probability at most (7) plus $\varepsilon$. On a zero-input every proposed pair has a defect by §2. Fresh searches give a false-acceptance probability of at most $T\varepsilon$, conditional on any list. Both errors are below $1/3$.

Inserting $T=O(\ell)$, $c=O_k(\ell\log\ell)$ and $K=O_k(m\ell^3)$ gives
$$
 \underbrace{O_k\bigl(\sqrt m\,\ell^3(\log\ell)^2\bigr)}_{\text{tournament}}
 +\underbrace{O_k\bigl(\sqrt m\,\ell^{7/2}\log\ell\bigr)}_{\text{verification}}
 \;\le\; C_k\sqrt m\,\ell^6 .
$$
The number of columns controls the first square root, the number of local tests the second. Their scales match because each column has $m$ rows and its circuit has size $m$ up to logarithms.

## 4. A cell query predicts an address

### 4.1 Planting one certificate

For the **dummy input** $Y^{(0)}$, choose the row $J_i$ of the sole zero in $X_i$ independently and uniformly in each column. Draw all address inputs independently from a law $\mu$ on the promise of $P$, independently also of the zero positions, and set every cell bit to zero. Every column loses. Choose $I$ uniformly and independently of the entire dummy input. For the **planted input** $Y^{(1)}$, erase the zero in column $I$ and fill its true cell $B_{I,s_I}$ with the correct transcripts and the pointers $J_j$ to the other zeros. Column $I$ wins.

![One draw of the coupled inputs, with $I=3$. All of the address problems have the same inputs in the two panels. The planted winner differs from the corresponding losing column only in its bit strip and its addressed cell.](figures/expert_planted.svg){width=100%}

The blank-array argument for cheat sheets [@ABK2016, Lemma 6] applies with an extra possible discovery, the erased zero [@BenDavid2015, §5.1]. Run a deterministic tree on the dummy board. It has exactly the same transcript on the planted board until it queries the erased position or a bit of the filled cell. The acceptance gap is at most the sum of the two discovery probabilities on the dummy run, which knows nothing about $I$. To reach the right cell, the tree can investigate a few columns deeply and hope $I$ is among them, or it can try addresses in many columns after learning little about each.

For any integer $1\le L\le m$ with $L<R(P)$, minimax gives a $\mu$ under which every deterministic depth-$L$ tree computes $P$ with success at most $\beta=2/3$ [@Yao1977]. Give the tree on the board $G=\lfloor mL/100\rfloor$ queries. We first bound the chance of bypassing the address search altogether.

### 4.2 Searching for the erased zero

If the tree discovers $Z$ zeros, the probability that one of them belongs to column $I$ is exactly $\mathbb E Z/m$. Before discovery, a column's zero is uniform among the rows not yet queried there, even given the entire transcript. Until half the rows have been queried, a query makes a new discovery with probability at most $2/m$. We expect at most $2G/m$ such early discoveries. Each remaining discovery costs at least $m/2$ queries to its column, so the run has at most $2G/m$ late discoveries. Hence
$$
 \Pr[\text{query }X_I[J_I]]\le\frac{4G}{m^2}.
\tag{8}
$$

### 4.3 Predicting the filled cell

To query a bit of $B_{i,s}$ the tree has to announce $s$ in the query index. At the right cell this is a prediction of all $r$ answers in column $i$. Call a column *heavy* if the full dummy run makes more than $L$ queries to its address inputs, counting repetitions. There are at most $G/L$ such columns on any run. Because $I$ is independent of that run,
$$
 \Pr[I\text{ heavy}]\le\frac{G}{mL}.
$$

For a column that receives few queries we need the separate-cap direct product [@Drucker2012, §3; @OpenAI2026, Lemma 4.1]. Under $\mu^{\otimes r}$ a predictor with at most $L$ queries to each input on every branch succeeds on the whole answer vector with probability at most $\beta^r$. Queries may be interleaved adaptively, and any auxiliary information and coins must be jointly independent of the tuple.

Fix the auxiliary information and coins. A transcript restricts each input separately, so their posterior laws are still independent. Let $V_h$ be the best probability of answering input $h$ under its posterior with its remaining allowance. A query to $h$ cannot increase $V_h$ in expectation, since that query followed by the best continuation was already an available strategy. It leaves all other factors fixed. Thus $\prod_h V_h$ is a supermartingale with initial value at most $\beta^r$. At a leaf independence makes the chance that *all* guesses are right at most $\prod_h V_h$. Taking expectations proves the bound.[^product]

[^product]: The [decision-tree proof](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#CL-product-law) gives the posterior argument in full.

The catch is that a column may end up light because of the answers read there. Conditioning on lightness can change their law. We instead cap a predictor on *every* input and ask which runs it reproduces.

Fix a column $i$ and a time $\tau\le G$. Embed the predictor’s unknown tuple, drawn from $\mu^{\otimes r}$, as the address inputs of column $i$. It samples everything else on the dummy board itself, including the zero in column $i$. Now simulate the tree through its $\tau$-th query. Other columns, all bit strips and all blank cells can be answered from the sampled board. Only a query to an address input of column $i$ costs the predictor a query. Stop *before* making the $(L+1)$-st such query in total. If the tree's query at time $\tau$ is in $B_{i,s}$, output $s$ before reading the cell. On any other query at that time, on abort, or if the tree has already halted, output a fixed vector.

This predictor respects the cap on every run. Its chance of success is therefore at most $\beta^r$ under the original product law. Now consider a dummy run in which $i$ was light and query $\tau$ hit its true cell. Every prefix was within budget, so the simulator followed that run to time $\tau$ and output $s_i$. We have proved the *joint* bound
$$
 \Pr[i\text{ light and query }\tau\text{ is in }B_{i,s_i}]
 \ \le\ \Pr[\text{predictor outputs }s_i]\ \le\ \beta^r.
\tag{9}
$$
For each fixed column there are at most $G$ opportunities to make this prediction. Average over the independent choice of $I$ and add the chance of a heavy column to obtain
$$
 \Pr[\text{query }B_{I,s_I}]
 \le \frac G{mL}+\frac1m\sum_{i=1}^m G\beta^r
 = \frac G{mL}+G\beta^r .
\tag{10}
$$

### 4.4 The randomized bound

Combining (8) and (10), the gap between the acceptance probabilities on the two laws is at most
$$
 \frac{4G}{m^2}+\frac G{mL}+G(2/3)^r <\frac13.
\tag{11}
$$
Here $G\le mL/100\le m^2/100$, and $r=20\log_2m$ makes $(2/3)^r\le m^{-10}$ small enough for all $G$ guesses. The same address length keeps the $2^r=m^{20}$ cells per column polynomial in number. Averaging over coins gives (11) for a randomized tree, while correctness with error at most $1/3$ on both supports would force a gap of at least $1/3$. Thus every such construction requires more than $\lfloor mL/100\rfloor$ randomized queries. For (3) at fixed $k$, the erased-zero term is $O(L/m)=o(1)$ and the lucky-address term also vanishes. The term that fixes the budget is $G/(mL)$, the bound on the fraction of deeply queried columns.

## 5. Forrelation and the optimal exponent

The partial function supplying these parameters is the Walsh–Hadamard form of $k$-fold Forrelation [@AA2018; @BansalSinha2021]. Let $H$ be the normalized Walsh–Hadamard matrix of order $m$, $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$, and $D_z$ the diagonal matrix of a sign vector. For $k$ such vectors of length $m$, put
$$
 \Phi=u^{\mathsf T}D_{z_1}H D_{z_2}H\cdots H D_{z_k}u,\qquad \delta=2^{-5k}.
$$
Set $P=1$ when $\Phi\ge\delta$, $P=0$ when $|\Phi|\le\delta/2$, and leave $P$ undefined elsewhere. Applying the unitary product to $u$ and projecting onto $u$ succeeds with probability $\Phi^2$. For fixed $k$ the two promised cases have a constant gap, giving the claimed decoder by repetition with trial registers retained. This experiment loses the sign: a large negative $\Phi$ can pass the projection test and still be outside the promise. For the exact circuit, compute the signed numerator by $k-1$ unnormalized fast Walsh–Hadamard transforms on integers of $O_k(\ell)$ bits and compare it to the thresholds above. This yields both domain and value bits in $O_k(m\ell^2)$ fan-in-two gates [@OpenAI2026, Lemma 2.1]. The lower bound of Bansal and Sinha [@BansalSinha2021, Corollary 1.4] gives (3). Fixing this circuit in the cells defines $F_{k,m}$.

For sufficiently large $m$, the floor in (3) gives $L\ge m^{1-1/k}/(2\ell^2)$ and $\lfloor mL/100\rfloor\ge mL/200$, proving the randomized inequality of (1). Now fix $0\le\alpha<4$. Choose $k\ge2$ with $k>2/(4-\alpha)$ and hold it fixed as $m$ grows through powers of four. By (1),
$$
 \frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
 \ \ge\ \frac{1}{400(1+C_k)^\alpha}\,
 \frac{m^{2-1/k-\alpha/2}}{(\log_2 m)^{2+6\alpha}}
 \ \longrightarrow\ \infty.
$$
The quantum algorithm can use a candidate's chances of beating its rivals without ever calculating those chances. It pays separately for finding candidates and checking their certificates. The classical algorithm must commit to a certificate's address merely to inspect it, and pays the one-instance hardness across $m$ possible columns. These costs on the same total function exclude every exponent below four.

## References

::: {#refs}
:::

<!-- lean-links -->
<!-- /lean-links -->
