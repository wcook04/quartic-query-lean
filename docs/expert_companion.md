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
  OpenAI constructed total Boolean functions for which no power smaller than four bounds randomized query complexity in terms of quantum query complexity. We explain the two reductions that make the separation possible. A certificate in one of $m$ columns points to a zero in every rival. Comparing two columns uses just their pointers into each other. Sampling each pivot according to its probability of defeating all earlier pivots at least halves the total surviving weight in expectation, however losing columns compare. Classically, a query to the winning certificate must specify its address, thereby predicting an entire vector of hard partial-function values. These arguments give quantum cost $\widetilde O_k(\sqrt m)$ and randomized cost $\widetilde\Omega_k(m^{2-1/k})$ for each fixed $k\ge2$.
---

## 1. The fourth power

A quantum algorithm looking for one valid certificate among $m$ candidates could search over all $m$ and verify each candidate it tries. If verification itself costs about $\sqrt m$ queries, this costs about $m$. OpenAI's construction [@OpenAI2026] makes one small part of a certificate useful on its own. The certificate contains a pointer disqualifying each rival, so two candidates can be compared at the cost of reading just the pointers they direct at one another, once their addresses are known. This is enough to find a short list. Only then does the algorithm pay for verification.^[Will Cook directed this reconstruction. AI systems drafted and revised the manuscripts and Lean proofs.]

What makes these certificates hard for a randomized algorithm is where the pointers are kept. Each candidate has an array. The address of the useful entry consists of answers to several instances of a partial function with a large classical–quantum gap. A quantum algorithm can read a valid address cheaply. A classical algorithm that so much as queries a *bit* of the right entry must first specify the entire address. Hiding the decisive entry in a random column multiplies the cost of solving one hard instance by the number of columns.

**Theorem 1** (OpenAI [@OpenAI2026, Theorem 1.1]). *For each fixed integer $k\ge2$ there are total Boolean functions $F_{k,m}$ indexed by powers of four $m\ge4$. With $\ell=\log_2m$ and a constant $C_k$ depending only on $k$,*
$$
 Q(F_{k,m})\le C_k\sqrt m\,\ell^6,
 \qquad R(F_{k,m})\ge \frac{m^{2-1/k}}{400\ell^2}.
\tag{1}
$$
*The quantum bound holds for all such $m$ and the randomized bound for all sufficiently large $m$. The optimal universal exponent in $R(f)=O((1+Q(f))^\alpha)$ for total Boolean $f$ is four.*

We count worst-case bit queries at error $1/3$. For a partial function, the error guarantee applies on its domain and the query cap on every input and branch. The explicit choices of logarithmic power and constant in (1) are those of this reconstruction. The universal upper bound follows from $R\le D$ and the theorem $D(f)=O(Q(f)^4)$ of Aaronson, Ben-David, Kothari, Rao and Tal, who conjectured that $R(f)=O(Q(f)^3)$ [@ABKRT2021, Conjecture 2]. Already $k=3$ in (1) excludes the cube.

The closest predecessors explain why it pays to compare candidates. Cheat sheets, introduced by Aaronson, Ben-David and Kothari [@ABK2016], also store certificates at addresses determined by hard partial functions. In their balanced AND–OR construction, a partial problem $P$ of dimension $m$ gives quantum cost $\widetilde O(m)$ and randomized lower bound $\widetilde\Omega(m^2R(P))$ when $Q(P)$ is polylogarithmic and its input length is of order $m$. Even using the optimal partial separations, this calculation gives at most a cubic power [@BansalSinha2021; @SSW2023]. OpenAI puts a cheat sheet in *each* column of a pointer function [@GPW2018; @ABBLSS2017]. The resulting randomized lower bound is smaller by a factor of $m$, but the quantum cost falls all the way to $\widetilde O(\sqrt m)$. We reconstruct these two bounds below.

## 2. The certificate

Take a partial Boolean function $P$ which is hard for randomized algorithms and cheap to evaluate quantumly. We also need a small exact circuit $\mathcal C$ with two outputs. One bit records whether the input belongs to the domain of $P$ and the other gives its value there. The circuit will have no role in a comparison. Its purpose is to let a verifier catch a false claim about the promise by checking one gate at a time.

Write $[m]=\{1,\ldots,m\}$ and $r=20\log_2m$. Column $i$ contains a string $X_i\in\{0,1\}^m$, $r$ inputs $A_{i,1},\ldots,A_{i,r}$ to $P$, and an array of cells $B_{i,s}$ indexed by $s\in\{0,1\}^r$. Each cell holds a proposed transcript of $\mathcal C$ on each of the $r$ inputs, together with one row pointer $p_{i,s,j}\in[m]$ for each $j\ne i$. A transcript supplies one bit per non-input gate in the fixed circuit. Every $\ell$-bit pointer encodes a row.

Column $i$ **wins** if $X_i=1^m$, all its address inputs belong to the domain of $P$, and the cell with label
$$
s_i=\bigl(P(A_{i,1}),\ldots,P(A_{i,r})\bigr)
$$
contains the true transcripts and points to a zero in every other column. The function outputs one if a column wins, zero otherwise. This defines a total Boolean function on the freely chosen input bits. In particular an off-promise column loses, whatever is written in its cells. Two winners are impossible because neither all-one column could point to a zero in the other.

![The all-one column $i^\star$ and its selected cell. Each other column has an array of its own. Following just the pointer for $j$ disqualifies that rival.](figures/expert_column.svg){width=85%}

For a proposed pair $(i,s)$, verification is an AND of local tests. Check all the bits of $X_i$, follow the $m-1$ pointers, and check each transcript against the circuit wiring and the claimed outputs $(1,s_h)$. If every gate agrees with its predecessors, induction through the circuit determines the whole transcript, including both outputs. Hence these tests pass precisely for a winning column at its correct address. With $S$ non-input gates there are
$$
 K=m+(m-1)+r(S+2)
\tag{2}
$$
tests, each costing at most $\max\{3,\ell+1\}$ bit queries. This count applies to the particular circuit whose transcripts the cells store. We fix that circuit once for both bounds.

**Choice of the partial function.** The construction uses $k$-fold Forrelation [@AA2018; @BansalSinha2021]. Let $H$ be the normalized Walsh–Hadamard matrix of order $m$, $u=m^{-1/2}(1,\ldots,1)^{\mathsf T}$, and $D_z$ the diagonal matrix of a sign vector. On $k$ sign vectors of length $m$ define
$$
 \Phi(z_1,\ldots,z_k)=u^{\mathsf T}D_{z_1}H D_{z_2}H\cdots H D_{z_k}u.
$$
With $\delta=2^{-5k}$, put $P=1$ for $\Phi\ge\delta$, $P=0$ for $|\Phi|\le\delta/2$, and leave $P$ undefined elsewhere. Using the circuit below in the column construction gives $F_{k,m}$.

Three facts about this choice explain its role [@OpenAI2026, Lemma 2.1]. First, applying the unitary product to $u$ and projecting onto $u$ succeeds with probability $\Phi^2$. The two promised cases are separated by a constant gap for fixed $k$. Repetition to error $\eta$ costs $O_k(1+\log(1/\eta))$ queries. Retaining the trial registers gives a reversible decoder with the same cost on arbitrary inputs. Second, the *signed* numerator of $\Phi$ can be computed exactly by $k-1$ unnormalized fast Walsh–Hadamard transforms on integers of $O_k(\ell)$ bits. Comparing that numerator to the two thresholds gives the required circuit with $S=O_k(m\ell^2)$ gates of fan-in at most two. This distinction matters for a large negative $\Phi$, which can have a large projection probability and still violate the promise. Third, the randomized lower bound of Bansal and Sinha [@BansalSinha2021, Corollary 1.4] gives, for fixed $k$ and sufficiently large $m$,
$$
 L:=\left\lfloor m^{1-1/k}/\ell^2\right\rfloor < R(P).
\tag{3}
$$
Thus $K=O_k(m\ell^3)$, and the $2^r=m^{20}$ cells per column give a Boolean input length polynomial in $m$. The quantum proof will use the decoder and the size of the circuit. The randomized proof needs only (3) and the ability to write a true certificate.

## 3. Finding a winner by comparison

### 3.1 What one comparison reveals

Suppose $i$ wins. Once its address is known, its pointer into any rival $j$ reads a zero. Now choose *any* cell in column $j$ and follow its pointer back into $i$. That pointer reads a one. The rival can therefore take part in a comparison even if none of its address inputs obey the promise.

Let $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$. Run the decoder on all $r$ inputs to a column with individual error $\varepsilon/r$. On a winning column its address is then correct with probability at least $1-\varepsilon$. For a pair of columns decode both addresses and follow the two pointers. A column whose pointer finds a zero defeats a column whose pointer finds a one. Break ties by smaller index. Use a single coherent circuit for each unordered pair, retaining the decoder registers, and set the self-comparison flag to loss. If $a_{ij}$ denotes the probability that $i$ defeats $j$ on the given input, then
$$
 a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0,
 \qquad a_{i^\star j}\ge1-\varepsilon\quad(j\ne i^\star)
\tag{4}
$$
whenever $i^\star$ wins. The comparison and its inverse each cost $c=O_k(r\log(r/\varepsilon)+\ell)=O_k(\ell\log\ell)$ queries.

### 3.2 A tournament with probabilistic comparisons

When comparisons have fixed outcomes, one can pick a random pivot and keep the candidates that beat it, as in the surviving-set algorithm of Ambainis, Iraids and Kokainis [@AIK2026, §6.1]. Roughly half the set disappears and a candidate beating everyone survives until picked. Here comparisons between losers need not even have a fixed underlying orientation. OpenAI's tournament [@OpenAI2026, Proposition 3.2] makes the survival probability itself the sampling weight.

After pivots $\rho_1,\ldots,\rho_n$, give candidate $i$ weight
$$
 w_i=\prod_{b=1}^n a_{i\rho_b},\qquad W=\sum_i w_i.
$$
Initially every weight is one. When $W>0$, draw the next pivot $\rho$ with probability $w_\rho/W$ and multiply each weight $w_i$ by $a_{i\rho}$. The new pivot drops out since $a_{\rho\rho}=0$. To see how much mass survives, draw two candidates independently from the current weights. On distinct draws, exchangeability and complementarity give either draw an equal chance of defeating the other. Coincident draws contribute nothing. In symbols,
$$
 \mathbb E[W_{\rm new}\mid w]
 =\frac1W\sum_{i,j}w_i w_j a_{ij}
 =\frac{W^2-\sum_i w_i^2}{2W}
 \le\frac W2.
\tag{5}
$$
For each pair of losers the two directions occur with the same coefficient. Their individual biases disappear from the answer.

Stop on extinction, keeping $W=0$ thereafter. After $T$ steps the expected weight is at most $m2^{-T}$. Yet as long as $i^\star$ has not been drawn, its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$. Thus the probability of missing it is at most $2m2^{-T}$.

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
The first draw, with no pivots, always succeeds. At later stages the flag can be rare. Until the winner is drawn, however, its own contribution ensures that the flag probability exceeds $1/(2m)$.

Use bounded amplitude amplification with this lower threshold. For a reversible preparation with a query-free success flag, threshold $\gamma\in(0,1/2]$ and error $\eta\in(0,1/2)$, a fixed schedule of $O(\gamma^{-1/2}\log(1/\eta))$ calls to the preparation and its inverse produces a flagged outcome with probability at least $1-\eta$ whenever the original success probability is at least $\gamma$. It reports failure if no trial succeeds. The cap holds for all success probabilities. Grover rotations preserve the direction of the successful component, so *every* successful trial gives exactly the conditional law in (6) [@BBHT1998; @BHMT2002; @OpenAI2026, Lemma 3.1]. The [finite amplification schedule](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#upper-small-probability) gives the worst-case cap.

Take $\gamma=1/(2m)$ and $\eta=\varepsilon$. Measure the next pivot and append it on success, stopping on failure or after $T$ pivots. At any history before the winner appears, a successful step has the ideal transition law and a failed step has probability at most $\varepsilon$. Couple each successful transition to the ideal draw at that history. Premature stopping adds at most $T\varepsilon$ to the miss probability, giving
$$
 \Pr[i^\star\text{ absent from the list}]\le 2m2^{-T}+T\varepsilon.
\tag{7}
$$
Only the measured list persists between stages. Rebuilding $n$ comparisons and amplifying costs $O(c(n+1)\sqrt m\log T)$ queries at a stage with $n$ pivots. The whole list costs $O(c\sqrt m\,T^2\log T)$ on every input, including those on which no column wins.

### 3.3 Paying for verification

A column can beat all its rivals and still carry a false transcript, since comparison never reads a transcript bit. For each listed column, decode a fresh address as in §3.1 and search its $K$ local tests for a defect. Choose a test in superposition, evaluate it reversibly, and flag a failure. One faulty test gives flag probability at least $1/K$. Bounded amplification therefore finds a defect, when one exists, with error at most $\varepsilon$ at cost $O(\ell\sqrt K\log(1/\varepsilon))$. If all tests pass it can never report a defect. Accept if a listed column passes this search.

On a zero-input, each trial column has a defect at *every* address, so fresh verification gives error at most $T\varepsilon$ even for an adaptively chosen list. On a one-input, listing the winner and decoding its address correctly suffice for acceptance. The rejection probability is at most (7) plus $\varepsilon$, below $1/3$. Inserting $T=O(\ell)$, $c=O_k(\ell\log\ell)$ and $K=O_k(m\ell^3)$ gives
$$
 \underbrace{O_k\bigl(\sqrt m\,\ell^3(\log\ell)^2\bigr)}_{\text{tournament}}
 +\underbrace{O_k\bigl(\sqrt m\,\ell^{7/2}\log\ell\bigr)}_{\text{verification}}
 \;\le\; C_k\sqrt m\,\ell^6 .
$$
One pays for searching among columns and for searching within certificates in succession. Nesting the second search inside the first would have lost a factor of order $\sqrt m$ up to logarithms.

## 4. A cell query predicts an address

Fix any $1\le L\le m$ with $L<R(P)$. The claim is that $G=\lfloor mL/100\rfloor$ queries do not suffice to compute the total function. By minimax [@Yao1977], choose a distribution $\mu$ supported on the promise of $P$ under which every deterministic tree of depth at most $L$ has success at most $\beta=2/3$. The values of $P$ under $\mu$ need not be fair bits. The direct-product bound below will supply the cost of guessing a string of them.

### 4.1 Planting one certificate

On a **dummy input** $Y^{(0)}$, place one zero at a uniform row $J_i$ in each column, with ones elsewhere in $X_i$. Draw all $mr$ address inputs independently from $\mu$, independently also of the mutually independent $J_i$, and leave every certificate cell blank (all bits zero). Every column loses. Now choose a column $I$ uniformly and independently of this entire input. Erase its zero and fill the one cell $B_{I,s_I}$ with the true transcripts in that column and the pointers $J_j$ into all its rivals. The resulting **planted input** $Y^{(1)}$ has a winner.

![One draw of the coupled inputs, with $I=3$. All of the address problems have the same inputs in the two panels. The planted winner differs from the corresponding losing column only in its bit strip and its addressed cell.](figures/expert_planted.svg){width=100%}

This is the blank-array argument for cheat sheets [@ABK2016, Lemma 6], with an extra change at the erased zero [@BenDavid2015, §5.1]. Run a deterministic tree on the dummy input. Until it queries the erased zero or a bit of the filled cell, it would receive the same replies on the planted input and hence make the same queries. Bounding the acceptance gap reduces to bounding these two discovery probabilities, both measured on the dummy run. In that run the tree never sees any information about $I$.

### 4.2 Searching for the erased zero

If the tree discovers $Z$ zeros, the probability that one of them belongs to column $I$ is exactly $\mathbb E Z/m$. Before discovery, a column's zero is uniform among the rows not yet queried there, even given the entire transcript. Until half the rows have been queried, a query makes a new discovery with probability at most $2/m$. We expect at most $2G/m$ such early discoveries. Each remaining discovery costs at least $m/2$ queries to its column, so the run has at most $2G/m$ late discoveries. Hence
$$
 \Pr[\text{query }X_I[J_I]]\le\frac{4G}{m^2}.
\tag{8}
$$

### 4.3 Predicting the filled cell

To query a bit of $B_{i,s}$ the tree has to announce $s$ in the query index. At the right cell this is a prediction of all $r$ answers in column $i$. A tree might learn the entire address in a few favourite columns. Call a column *heavy* if the full dummy run makes more than $L$ queries to its address inputs, counting repetitions. There are at most $G/L$ such columns on any run. Because $I$ is independent of that run,
$$
 \Pr[I\text{ heavy}]\le\frac{G}{mL}.
$$

What can the tree predict in a light column? For independent inputs of law $\mu$, the chance of predicting all $r$ answers is at most $\beta^r$ under a separate cap of $L$ queries to each input, however the queries are interleaved [@Drucker2012, §3; @OpenAI2026, Lemma 4.1]. The product bound allows coins and side information jointly independent of the target tuple. Indeed, a fixed transcript restricts each input separately, so its unnormalized law still factors. For each factor take the greatest mass on which it can still be answered correctly with its remaining allowance. The product bounds the correct mass at a leaf. At an internal node only one input is queried, and the two continuation values for that factor sum to at most its current value. Backwards induction gives the product of the initial optima, at most $\beta^r$. The [separate-cap proof](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#CL-weighted-values) spells out the recurrence.

There is a small trap in applying this bound. Whether a column ends up light may depend on answers already read there. Conditioning on lightness can therefore change the law of the very inputs we need to predict. Instead, impose a cap on an algorithm for predicting the address, and ask which runs it reproduces.

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
Indeed $G\le mL/100\le m^2/100$, and $r=20\log_2 m$ gives $(2/3)^r\le m^{-10}$. This is where the logarithmic address length is spent. Averaging over coins gives the same bound for a randomized tree, whereas error at most $1/3$ on both supports requires a gap of at least $1/3$. Thus more than $\lfloor mL/100\rfloor$ queries are necessary. The argument works for any partial $P$ with $L<R(P)$ and any exact circuit certifying its domain and value in this construction.

For the $L$ in (3) and sufficiently large $m$, $L\ge m^{1-1/k}/(2\ell^2)$ and $\lfloor mL/100\rfloor\ge mL/200$. We obtain the randomized inequality of (1) for precisely the circuit used in the quantum algorithm.

## 5. Optimality

The hidden column contributes a factor of $m$ to the classical bound, and predicting its address contributes $m^{1-1/k}$ up to logarithms. Quantumly, selection and verification each cost $\widetilde O_k(\sqrt m)$. These are the two powers of the same parameter that matter. Fix $\alpha<4$ with $\alpha\ge0$ and choose $k>2/(4-\alpha)$, $k\ge2$. Then (1) gives
$$
 \frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
 \ \ge\ \frac{1}{400(1+C_k)^\alpha}\,
 \frac{m^{2-1/k-\alpha/2}}{(\log_2 m)^{2+6\alpha}}
 \ \longrightarrow\ \infty
$$
as $m$ tends to infinity through powers of four with this $k$ fixed. Thus every power below four fails, and the quartic upper bound for total functions is sharp in its exponent.

The [complete proof reconstruction](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md) also derives the Forrelation estimates and the universal upper bound. Its [uniform estimates](https://github.com/wcook04/quartic-query-lean/blob/5c676e2438c4b09ce3d4e2e9177518477f50ce2e/docs/reasoning_record.md#ROOT-GROWING-K) permit $k$ to grow in one explicit family. The accompanying Lean development proves the optimal exponent and the quantitative separating bounds. Its tournament proof uses the law of the measured labels in (6). The [theorem index](https://github.com/wcook04/quartic-query-lean/blob/main/docs/proof_index.md) gives the formal statements and their proofs.

## References

::: {#refs}
:::

<!-- lean-links -->
<!-- /lean-links -->
