---
title: "The randomized–quantum query exponent for total functions is four"
subtitle: "A companion to OpenAI's nearly quartic separation"
author: "Will Cook"
date: "November 2026"
bibliography: expert_companion.bib
link-citations: true
abstract: |
  The optimal polynomial exponent relating bounded-error randomized and quantum query complexity of total Boolean functions is four. OpenAI's construction attains $R(F)\ge Q(F)^{4-o(1)}$, matching the known universal quartic upper bound and refuting the conjectured cubic relation. We reconstruct the separation from its Forrelation and query-complexity ingredients and describe its Lean formalisation. Each of the $m$ columns has an array of certificates addressed by hard partial-function values. Under the hard input distribution, a classical algorithm is unlikely to find the planted certificate with a budget much smaller than the number of columns times the address-hardness scale. A quantum algorithm decodes an address cheaply and finds the winning column in about $\sqrt m$ queries. Its comparisons need to favour only that column; comparisons between other columns may have arbitrary probabilities. A weighted tournament handles this weaker guarantee, and exact certificate tests complete the algorithm on every input.
---

## 1. Introduction

For total Boolean functions, how large can the gap between randomized and quantum query complexity be? Earlier constructions approached a cubic separation, whereas the best universal upper bound was quartic. OpenAI's nearly quartic construction closes this gap [@OpenAI2026]. Its central feature is that a true certificate can defeat every rival in a cheap comparison, even when the rival's partial-function inputs violate their promises.

A query gives access to an input coordinate; computation between queries is free. A classical query reads one bit, while a quantum query applies
$O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle$, possibly in superposition over $i$. For a partial Boolean function $f$, write $R(f)$ and $Q(f)$ for the least query caps of randomized and quantum algorithms that compute $f$ with probability at least $2/3$ on every input in its domain. A cap holds on every input and every branch, including branches on inputs outside the promise. The optimal exponent for total functions is
$$
\alpha_{\rm tot}=\inf\Bigl\{\alpha\ge0:\ \exists C_\alpha>0\ \forall n\ge1\ \forall f:\{0,1\}^n\to\{0,1\},\ \ R(f)\le C_\alpha\bigl(1+Q(f)\bigr)^\alpha\Bigr\}.
\tag{1}
$$
The constant is uniform in $n$ and $f$; the added one includes constant functions.

**Theorem 1** [@OpenAI2026, Theorem 1.1]**.** $\alpha_{\rm tot}=4$. For each integer $k\ge2$ there is a constant $C_k>0$ such that, for all sufficiently large powers of four $m$, the total function $F_{k,m}$ defined in §2 satisfies, with $\ell=\log_2m$,
$$
Q(F_{k,m})\le C_k\sqrt m\,\ell^6
\qquad\text{and}\qquad
R(F_{k,m})\ge\frac{m^{2-1/k}}{400\ell^{2}}.
\tag{2}
$$

The exponent six and coefficient $1/400$ are explicit choices in this reconstruction. Aaronson, Ben-David, Kothari, Rao and Tal proved $D(f)=O(Q(f)^4)$ for total $f$, where $D$ is deterministic query complexity, using Huang's sensitivity theorem [@ABKRT2021; @Huang2019]. Since $R\le D$, this gives $\alpha_{\rm tot}\le4$. They conjectured $R(f)=O(Q(f)^3)$ [@ABKRT2021, Conjecture 2]. Taking $k=3$ in (2) gives a separation exponent $10/3>3$; choosing larger fixed $k$ excludes every exponent below four.

The theorem, construction and two analyses are OpenAI's. Our purpose is to explain how the two difficult reductions fit together: sampling a tournament with arbitrary loser-comparison probabilities, and turning a visit to a hidden certificate into a predictor of many hard answers. We prove these reductions below. The Forrelation hardness theorem, its efficient quantum algorithm and exact circuit, standard amplitude-amplification facts, finite minimax and the universal quartic upper bound are cited inputs. The reasoning record [@Record2026] supplies their detailed reconstruction, an additional uniform Forrelation estimate and the formal correspondence. The same circuit defines the function in both bounds of (2).

### 1.1 Earlier separations

Ben-David gave the first super-quadratic separation for total functions, $R=\widetilde\Omega(Q^{5/2})$, by turning Forrelation into a total function [@BenDavid2015]. Aaronson, Ben-David and Kothari then reached the same exponent with cheat sheets [@ABK2016, §3.1], a framework that turns any partial separation into a total one, and the later exponents below four came from it. In their construction a partial function $g$ on $n$ bits with polylogarithmic quantum query complexity is composed with $h=\mathrm{AND}_{m'}\circ\mathrm{OR}_{m'}$, which has $R(h)=\Omega(m'^2)$, $Q(h)=O(m')$ and certificates of size $m'$. Certificates for all $n$ inner values certify the input to the outer promise. For the resulting total cheat-sheet function $f$, a quantum algorithm computes $g\circ h$ and Grover-checks these certificates, of total size $\widetilde O(nm')$, while the randomized lower bound retains the cost of $g\circ h$:
$$
Q(f)=\widetilde O\bigl(m'+\sqrt{nm'}\bigr),\qquad R(f)=\widetilde\Omega\bigl(R(g)\,m'^2\bigr).
$$
Here $\widetilde O$ and $\widetilde\Omega$ suppress logarithmic factors, with construction parameters fixed. If $R(g)=\widetilde\Omega(n^c)$, setting $m'=n$ gives $R=\widetilde\Omega(n^{2+c})$ against $Q=\widetilde O(n)$. Forrelation has $c=1/2$; Tal's bound for $k$-fold Rorrelation, the random-orthogonal-matrix variant, gives $c=2/3-o(1)$; and the optimal partial separations of Bansal and Sinha and of Sherstov, Storozhenko and Wu give $c=1-o(1)$. Since $R(g)\le n$ for every $g$, the AND–OR recipe stops at the cube, and Aaronson et al. conjectured that three is the truth for all total functions.

Grover search for OR and its matching lower bound give the basic quadratic separation. The constructions above then achieve $R\ge Q^{a-o(1)}$ with $a=5/2$ for Ben-David and for the cheat-sheet construction [@BenDavid2015; @ABK2016], $a=8/3$ for Tal [@Tal2020], and $a=3$ for Bansal–Sinha and independently Sherstov–Storozhenko–Wu [@BansalSinha2021; @SSW2023]. OpenAI's construction reaches $a=4$ [@OpenAI2026]. These are lower bounds for separating families; the universal upper bound is $R\le D=O(Q^4)$ [@ABKRT2021; @Huang2019].

### 1.2 Overview of the construction

The input has $m=4^t$ columns. Column $i$ holds a string $X_i\in\{0,1\}^m$, $r=20\log_2m$ inputs $A_{i,1},\dots,A_{i,r}$ to a Forrelation partial function $P=P_{k,m}$, and a cell $B_{i,s}$ for each address $s\in\{0,1\}^r$. When all its instances are promised, their answers form the true address $s_i$. Column $i$ wins if $X_i=1^m$ and the selected cell certifies these answers and points to a zero in every other column. The function is one exactly when a column wins.

<!-- pdf-page-break -->

![The winning column $i^\star$ is all ones. Its selected cell certifies its address and points to a zero in every other column. Every column has its own address blocks and cell array; the winner's array is enlarged here. No pointer into $X_{i^\star}$ can find a zero.](figures/expert_column.svg){width=90%}

A direct Grover search over columns would verify each candidate by searching its $K=\widetilde O_k(m)$ local tests. The resulting cost, roughly $\sqrt m\sqrt K$, is too large. Instead, compare two columns by decoding their addresses and following each column's pointer into the other. The winner defeats every rival with high probability: its pointer reaches a zero, and the rival's pointer reaches a one. This remains true when the rival's address inputs violate the promise. Two losing columns can defeat each other with any probabilities, including $1/2$. The tournament in §3 uses these probabilities as weights to produce a short list containing the winner, after which we verify the listed candidates.

Classically, both places where a winner can be detected are hidden. Start with one zero in each column and every certificate cell blank. Independently select a uniform column $I$, erase its zero, and fill its true cell. This changes one bit and one certificate block. Discovering the erased bit requires finding the zero of the hidden selected column, rather than just any zero. Conditional on a dummy run that finds $Z$ zeros, the independent choice of $I$ selects one of them with probability $Z/m$ (§4.3).

For the filled cell, let $L<R(P)$ be the available hardness scale. A total budget much smaller than $mL$ permits more than $L$ address queries in only a small fraction of the columns. For any other column, a query to its true cell names all $r$ hard answers by its position. A direct product bound makes each such guess unlikely; a union bound covers all query times. Thus the randomized cost is $\Omega(mL)$. For fixed $k$, suppressing logarithms, $L$ has scale $m^{1-1/k}$, while the quantum cost is $\widetilde O_k(\sqrt m)$. The resulting separation exponent is
$$
\frac{2-1/k}{1/2}=4-\frac2k.
$$

### 1.3 Relation to earlier constructions

Addressing a certificate by the answers to hard partial instances is the cheat-sheet idea of Aaronson, Ben-David and Kothari [@ABK2016]. Here each of the $m$ columns has its own array of cells, so the classical lower bound charges address queries across many possible planted columns, while the quantum algorithm searches them in about $\sqrt m$ steps. The winning condition descends from the pointer functions of Göös, Pitassi and Watson [@GPW2018], which Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs developed into a nearly quartic separation of deterministic from quantum query complexity [@ABBLSS2017].

In the back-pointer construction giving that nearly quartic separation, the highlighted zero leaf in each non-marked column points back to the marked column. Those back pointers permit an efficient zero-error randomized algorithm. A balanced tree leads to the highlighted leaves; a separate variant without back pointers is hard even for bounded-error randomized algorithms. Direct pointers, with one symbol holding all $m-1$ of them, were set aside because they make the alphabet exponential [@ABBLSS2017, §1.3]. In $F_{k,m}$ a zero carries no pointer. The pointers that disqualify the other columns are stored in the winner's selected cell, which is located by computing the winner's address, as $m-1$ separate $\ell$-bit fields. A comparison reads only the field that points into its rival, in $\ell+1$ bit queries, and verification checks all of them by a Grover search over the local tests.

The partial function is the $k$-fold Forrelation problem of Aaronson and Ambainis [@AA2018]. Bansal and Sinha proved its randomized hardness in the explicit Walsh–Hadamard form, with the one-sided thresholds used here [@BansalSinha2021]. Sherstov, Storozhenko and Wu independently proved the optimal partial separation for $k$-fold Rorrelation with a uniformly random orthogonal matrix [@SSW2023, Theorem 1.1]. The construction uses the explicit form because it also needs an exact circuit of nearly linear size for the promise and the value of $P$ (property (iii) of §2).

The closest comparison-search antecedent is the surviving-candidate set of Ambainis, Iraids and Kokainis [@AIK2026, §6.1]: retain candidates that defeat every previously selected pivot. Their comparisons approximate a fixed graph. OpenAI's tournament replaces set membership by a product of exact comparison probabilities, so it also accommodates arbitrary probabilities between losers. Section 3.2 proves the resulting half-drift and sampling identities. Minimum finding assumes a total order [@DH1996]; king finding seeks a vertex reaching every other in at most two directed steps in a fixed tournament [@MPS2023]. Ben-David and Kothari also use fixed comparisons of candidate claims, followed by verification [@BDK2026, Lemma 5]. These are different input guarantees from the one needed here. Bounded-error quantum search [@HMW2003] remains applicable to a fixed candidate-validity predicate, but that predicate costs about $\sqrt K$ queries to evaluate, which is the nested-search cost above.

Section 2 gives the function and its local tests. Section 3 constructs the candidate list by halving total weight, and §4 proves the randomized lower bound; §§5–6 supply the Forrelation estimate and deduce the optimal exponent. Section 7 relates the theorem to Lean. Appendix A records counterexamples to tempting simplifications, and the companion exposition [@Exposition2026] develops a four-column example.

## 2. The Forrelation promise and the total function

Fix $k\ge2$, $t\ge1$, $m=4^t$, $\ell=2t$ and $r=20\ell$, and identify a bit $a$ with the sign $(-1)^a$. Powers of four make $\sqrt m$ integral for the exact circuit below; the factor $20$ makes address guessing small enough for the union bound in §4. Let $H$ be the normalised $m\times m$ Walsh–Hadamard matrix and $u=m^{-1/2}(1,\dots,1)^{\mathsf T}$. For sign vectors $z_1,\dots,z_k\in\{\pm1\}^m$ put
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
and undefined otherwise; in particular a large negative $\Phi$ lies outside the promise. We use three properties of $P$, which we cite from [@OpenAI2026, Lemma 2.1]; properties (ii) and (iii) are proved in §§[3.3](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_repetition) and [3.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_circuit) of the record.

(i) For fixed $k$ and all large $m$, with $L=\bigl\lfloor m^{1-1/k}/\ell^2\bigr\rfloor$,
$$
L<R(P).
\tag{5}
$$
This follows from Bansal and Sinha's bound $R(P)=\Omega\bigl(k^{-29}(m/\log(km))^{1-1/k}\bigr)$ [@BansalSinha2021, Corollary 1.4] (see §5).

(ii) For $0<\eta<1/2$, a quantum algorithm with $O_k(1+\log(1/\eta))$ queries computes $P$ with error at most $\eta$ on its domain.

It prepares $u$, applies the matrices in (3) from right to left, using one phase query for each sign diagonal, and measures the projection onto $u$, which succeeds with probability $\Phi^2$; repetition separates $\Phi^2\ge\delta^2$ from $\Phi^2\le\delta^2/4$. The algorithm can be run coherently with its workspace kept. On inputs outside the domain it still halts within the same query cap, with an arbitrary output. The interference test of Aaronson and Ambainis, which accepts with probability $(1+\Phi)/2$ [@AA2018, Proposition 6], would serve equally well: we need bounded error only on the promise, because membership in the domain is checked separately by the circuit of (iii).

(iii) An exact Boolean circuit $\mathcal C$ of fan-in at most two, with $S\le200(k+1)^2m\ell^2$ non-input gates including its two output gates, outputs a domain bit, equal to one exactly on the domain of $P$, and a value bit equal to $P$ there. With the integer matrix $\sqrt m H$ we have $\Phi=N/m^{(k+1)/2}$ for an integer $N$, and the two cases of (4) become $2^{5k}N\ge m^{(k+1)/2}$ and $2^{5k+1}|N|\le m^{(k+1)/2}$, which fast Walsh transforms on $O_k(\ell)$-bit integers decide. The domain bit cannot be read off the projection statistic, which sees only $\Phi^2$ (Appendix A.1).

**The total function.** Column $i\in[m]$ consists of a string $X_i\in\{0,1\}^m$, strings $A_{i,1},\dots,A_{i,r}\in\{0,1\}^{km}$, and a cell $B_{i,s}$ for each $s\in\{0,1\}^r$. The cell holds an $\ell$-bit pointer $p_{i,s,j}\in[m]$ for each $j\ne i$ and $r$ alleged transcripts of $\mathcal C$, one bit per non-input gate. These are separate, freely assignable input coordinates; the alleged transcripts may be false. Column $i$ **wins** if $X_i=1^m$, every $P(A_{i,h})$ is defined, and the cell at $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ holds the true transcripts of $\mathcal C$ on each $A_{i,h}$ and pointers with
$$
X_j[p_{i,s_i,j}]=0\qquad\text{for every }j\ne i.
\tag{6}
$$
We set $F_{k,m}=1$ if some column wins and $F_{k,m}=0$ otherwise. The definition imposes no promise on the address inputs, pointers or transcripts, so $F_{k,m}$ is total. At most one column wins: a second all-one column would make the first column's required pointer test impossible.

The function depends on the circuit $\mathcal C$, because its cells hold transcripts of $\mathcal C$. For each $k$ and $m$ we fix one circuit with property (iii), and both bounds in (2) are proved for the function built from it. The lower bound holds for every such circuit; the upper bound uses the size $S$ of the fixed one. Since $2^r=m^{20}$, the total input length is $m[m+rkm+2^r((m-1)\ell+rS)]=O_k(m^{22}\ell^3)$, polynomial in $m$ for fixed $k$.

**Local tests** [@OpenAI2026, Lemma 2.2]. For a pair $(i,s)$, the event that $i$ wins and $s=s_i$ is the conjunction of
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3)
$$
tests: $m$ tests $X_i[y]=1$, $m-1$ pointer tests, one consistency test per gate of each transcript, and two output tests per transcript (domain bit $1$, value bit $s_h$). The output tests are additional to the consistency tests at the output gates: consistency determines their values, while the two tests enforce the required domain and answer. Induction in topological order shows that a gate-consistent transcript is the true evaluation, so the output tests say that $P(A_{i,h})$ is defined and equals $s_h$. Thus every test passes at $(i,s_i)$ when $i$ wins, and when $i$ does not win some test fails at $(i,s)$ for every address $s$. A gate test makes at most three queries and a pointer test $\ell+1$ adaptive queries, and every test can be evaluated coherently, with its index in superposition, at a constant-factor overhead (record §§[4.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-local-tests)–[4.6](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-coherent-tests)). The circuit size enters the quantum bound only through the cost $\sqrt K$ of verification (§3.3).

## 3. The quantum upper bound

The upper bound has two parts: produce a short list containing the winner, then verify that list. The list is obtained by a tournament that needs no reliability guarantee for comparisons between losers. Put $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$.

The sampling step uses the following bounded form of amplitude amplification. Its essential feature is preservation of the conditional output law, including when the success probability is unknown.

**Lemma 2** (bounded amplification [@OpenAI2026, Lemma 3.1])**.** Let $\mathcal A$ be a reversible state preparation with a designated success bit and output label. The success test is fixed independently of the input and requires no oracle queries. Let its success probability be $p$. Given $0<\gamma\le1/2$ and $0<\eta<1/2$, a procedure makes $O(\gamma^{-1/2}\log(1/\eta))$ calls to $\mathcal A$ and $\mathcal A^{-1}$ on every branch and either reports failure or returns a successful label. Conditional on success, the label has exactly its original law under $\mathcal A$. Failure has probability at most $\eta$ if $p\ge\gamma$, and occurs surely if $p=0$.

*Proof.* The case $p=0$ cannot yield success. For $p>0$, write $\mathcal A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle$, with $|g\rangle$ the normalised successful component. Grover iterations change only the two coefficients, so a successful measurement always leaves $|g\rangle$ up to global phase [@BHMT2002, §2, Lemma 1]. A trial mixes a direct measurement with a uniformly random number of Grover iterations up to $O(\gamma^{-1/2})$. The direct measurement handles $p\ge1/2$; the averaged Grover probability is bounded below by a constant for $\gamma\le p\le1/2$ [@BBHT1998, §4, Lemma 2]. A fixed $O(\log(1/\eta))$ number of fresh trials gives the claimed cap and failure bound. Stopping at the first success therefore preserves its conditional label law. $\square$

The cutoff gives a worst-case bound even when $p<\gamma$. The untruncated QSearch routine of [@BHMT2002, Theorem 3] instead gives an expected-cost guarantee. The numerical trial estimate and the retained-state version are in [§5.1 of the record](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-small-probability); the tournament uses only the measured label law.

### 3.1 Comparing two columns

To decode column $i$, we run the algorithm of §2 (ii) on each $A_{i,h}$ with error $\varepsilon/r$, at cost $O_k(r\log(r/\varepsilon))$. If all $r$ instances are promised, then the decoded address is $s_i$ with probability at least $1-\varepsilon$; otherwise the decoder still returns some address within the same cap. For an unordered pair, we sort the indices as $i<j$ and run one fixed circuit: decode both columns and follow their pointers into each other. If the pointers from $i$ and $j$ find bits $(0,1)$, then $i$ defeats $j$; for $(1,0)$, $j$ defeats $i$. Equal bits give a tie, which $i$ wins as the smaller index. A self-comparison is a loss. For this fixed input, let $a_{ij}$ be the probability that $i$ defeats $j$. Both orders run the same circuit, so
$$
a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0.
\tag{7}
$$
The decoded labels stay in orthogonal registers, so branches with different labels do not interfere, and the coherent circuit, with its workspace retained, reports $i$ defeating $j$ with the same probabilities $a_{ij}$. If $i^\star$ wins, no pointer finds a zero in $X_{i^\star}=1^m$, and whenever $i^\star$ is decoded correctly its pointer finds a zero in the rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every $j\ne i^\star$, whatever the rival's address inputs. The $a_{ij}$ are exact circuit probabilities; only comparisons involving the winner need a correctness guarantee. One comparison costs $c=O_k(\ell\log\ell)$ queries.

### 3.2 A tournament with probabilistic comparisons

**Proposition 3** [@OpenAI2026, Proposition 3.2]**.** Suppose a reversible comparison circuit is coherently controlled by two candidate indices, retains all its workspace, and uses at most $c$ queries on every input. For each fixed input, its probabilities $a_{ij}$ satisfy (7). There is a quantum algorithm using $O(c\sqrt m\,T^2\log T)$ queries on every branch and returning at most $T$ candidates. If some $i^\star$ satisfies $a_{i^\star j}\ge1-\varepsilon$ for all $j\ne i^\star$, the list contains $i^\star$ with probability at least $1-2m2^{-T}-T\varepsilon$.

For deterministic comparisons, the candidates that defeat every previous pivot form a surviving set [@AIK2026, §6.1]. For probabilistic comparisons we assign candidate $i$ the weight $w_i=\prod_ba_{i\rho_b}$ after pivots $\rho_1,\rho_2,\dots$ have been selected. This is its probability of defeating all those pivots in fresh comparisons, conditional on the fixed input and pivot history. It requires no independence among input bits. We draw the next pivot in proportion to these weights.

The algorithm starts with an empty list. At each of at most $T$ stages it prepares the comparison experiment (9) from the measured pivot history, applies Lemma 2, and either appends the measured label or stops on failure. It then returns the list. The length and query cap hold even if there is no dominant candidate; the probability of including $i^\star$ is proved by the ideal process below.

*Ideal process.* Start with weights $w_i=1$ and $W=\sum_iw_i$. For at most $T$ steps, and only while $W>0$, draw a pivot $\rho$ with probability $w_\rho/W$, append it to the list, and update $w_i\leftarrow w_i\,a_{i\rho}$. Pairing the terms $(i,\rho)$ and $(\rho,i)$ by (7) gives
$$
\mathbb E[W_{\rm new}\mid w]=\frac1W\sum_{\rho,i}w_\rho w_i a_{i\rho}=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\tag{8}
$$
Thus the expected new total weight is at most half the old total. No order or transitivity enters, so cycles among losers do no harm. If $W$ reaches zero we keep it zero for the remaining analysis steps; then $\mathbb EW\le m2^{-T}$ after $T$ steps. Until $i^\star$ is drawn its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$, so by Markov's inequality $i^\star$ is missing from the ideal list with probability at most $2m2^{-T}$.

*Exact sampling.* The algorithm never computes the weights. Given pivots $\rho_1,\dots,\rho_n$ with $n<T$, it prepares
$$
\frac1{\sqrt m}\sum_{i=1}^m|i\rangle\bigotimes_{b=1}^{n}|\phi(i,\rho_b)\rangle,
\tag{9}
$$
where $|\phi(i,\rho_b)\rangle$ is the full comparison state in a fresh workspace, and flags success when every comparison says that $i$ wins. For a fixed label, the fresh workspaces multiply the success probabilities; orthogonal labels then add their masses. Thus, for the fixed input and history, the success-and-label mass is $m^{-1}\prod_ba_{i\rho_b}=w_i/m$. The total success probability is therefore $W/m$, and the label law conditional on success is $w_i/W$. We apply Lemma 2 with $\gamma=1/(2m)$ and $\eta=\varepsilon$ and take the returned label as the next pivot; on reported failure we stop and return the list.

For example, in an abstract four-candidate comparison let candidate $1$ defeat all others surely, and let $a_{23}=1/3$, $a_{24}=3/4$, $a_{34}=2/5$, with complementary reverse probabilities and zero diagonal. After pivot $2$, the weights are $(1,0,2/3,1/4)$. The preparation succeeds with probability $23/48$, and its conditional label law is $(12/23,0,8/23,3/23)$. These fractional weights illustrate the proposition; no realisation by the four-column Boolean example is assumed.

*Coupling.* Until $i^\star$ is drawn, $W/m\ge1/(2m)$, so at every such history the stage fails with probability at most $\varepsilon$ and otherwise draws a pivot with the ideal law. The failure probabilities may depend on the history, so we couple the two processes stage by stage, conditional on the entire past. This adds at most $T\varepsilon$ to the miss probability, and a failure after $i^\star$ is listed does not remove it. With $n$ previous pivots, a stage costs $O(c(n+1)\sqrt m\log(1/\varepsilon))$ queries whether or not a dominant candidate exists, where $n+1$ harmlessly covers the empty history, and summing over $n<T$ proves the proposition. A longer version of this proof is in [§5.2 of the record](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-quantum-tournament).

### 3.3 Verification and the query count

Pairwise dominance does not imply a valid certificate: the smallest-index all-one column can win every tie while one of its pointers is false (Appendix A.3). We therefore verify each listed candidate. We decode its address afresh and measure it. At the measured address, a uniformly random one of the $K$ local tests fails with probability $0$ if all pass and with probability at least $1/K$ otherwise, so Lemma 2 with $\gamma=1/K$ and $\eta=\varepsilon$ searches for a failing test in $O(\sqrt K\,\ell\log(1/\varepsilon))$ queries. The search reports either a defect or no defect found. We reject on a defect, accept the candidate otherwise, and accept the input if any candidate is accepted.

A column that does not win fails some test at every address (§2), including addresses decoded from unpromised instances, so it is accepted with probability at most $\varepsilon$; the winner is accepted whenever its address is decoded correctly. On a zero-input, a union bound over the list gives error at most $T\varepsilon$. On a one-input, rejection requires either missing the winner, of probability at most $2m2^{-T}+T\varepsilon$, or decoding its address incorrectly during verification, of probability at most $\varepsilon$ conditional on any prior history. Earlier acceptance of a false candidate cannot hurt this one-input decision. The total is below $1/3$. Pointers are read bit by bit, array indices are computed reversibly, and a controlled read can be implemented with at most two ordinary queries.

One comparison costs $c=O_k(\ell\log\ell)$ queries, so Proposition 3 costs $O(c\sqrt m\,T^2\log T)$. Verifying $T$ candidates costs
$$
O_k\bigl(T\ell\log\ell+T\sqrt K\,\ell\log T\bigr).
$$
Since $T=O(\ell)$ and $K=O_k(m\ell^3)$, both costs are at most $C_k\sqrt m\,\ell^6$. This deliberately loose common bound holds on every input and branch. The [explicit count in record §5.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-explicit-log6) gives $C_k\le2^{53}k\,2^{10k}$; the exponent argument needs only that $C_k$ is fixed when $k$ is fixed.

## 4. The randomized lower bound

The classical argument uses only the hardness of the partial function and correctness of its certificate circuit. Write $F_{P,\mathcal C,m}$ for the construction of §2 with these choices. We prove
$$
R(F_{P,\mathcal C,m})>\left\lfloor\frac{mL}{100}\right\rfloor
\qquad\text{whenever }1\le L\le m\text{ and }L<R(P).
$$
Forrelation enters only when we choose $L$ at the end.

Choose a law $\mu$ on the domain of $P$ under which every deterministic depth-$L$ tree has success at most $\beta=2/3$. Such a law exists by finite minimax [@Yao1977]: because $L<R(P)$, the best worst-case success at cap $L$ is below $2/3$, and compactness ensures that the optimum is attained. We use $r$ independent samples from this law to hide an address. A planted one-input will differ from a zero-input only at one erased zero and one filled cell. The two discovery probabilities are bounded in §§4.3–4.4.

### 4.1 A direct product with separate caps

**Lemma 4** [@OpenAI2026, Lemma 4.1]**.** Let $U_1,\dots,U_r$ be independent with law $\mu$. An algorithm that makes at most $L$ queries to each $U_h$ on every branch, interleaving them adaptively, outputs $(P(U_1),\dots,P(U_r))$ with probability at most $\beta^r$. Its random coins and any side information are allowed if they are jointly independent of $(U_1,\dots,U_r)$.

*Proof.* We work with unnormalised measures, so that branches of probability zero need no conditioning. For a nonnegative measure $\nu$ on the domain of $P$, let $V_d(\nu)$ be the largest $\nu$-weight of inputs on which a depth-$d$ tree answers correctly. Then $V_0(\nu)=\max_b\nu(P=b)$ and
$$
V_{d+1}(\nu)=\max\Bigl\{V_d(\nu),\ \max_y\bigl[V_d(\nu_{y,0})+V_d(\nu_{y,1})\bigr]\Bigr\},
$$
where $\nu_{y,b}$ is the restriction of $\nu$ to inputs with bit $y$ equal to $b$. For product measures $\nu_1\otimes\dots\otimes\nu_r$ and remaining budgets $L_1,\dots,L_r$, induction on a deterministic vector-output tree shows that its weight of fully correct inputs is at most $\prod_hV_{L_h}(\nu_h)$. At a leaf the correct weight factorises. At a query to coordinate $y$ of input $h$, only $\nu_h$ and $L_h$ change. The sum of the two inductive bounds is
$$
\left(\prod_{j\ne h}V_{L_j}(\nu_j)\right)
\left[V_{L_h-1}(\nu_{h,y,0})+V_{L_h-1}(\nu_{h,y,1})\right]
\le\prod_jV_{L_j}(\nu_j).
$$
The unchanged factors can be taken outside the sum precisely because the law is a product. Initially every factor is at most $\beta$. We fix the coins and side information, apply this bound, and average. $\square$

We use this separate-cap form for its exact factor $\beta^r$ and short proof. Per-path allowances go back to Shaltiel's fair trees, for XOR advantage under uniform inputs [@Shaltiel2003]; Drucker's Lemmas 3.1–3.2 and the fair specialisation at the end of §3 give the product bound used here [@Drucker2012]. The caps must hold on every branch, and side information must be jointly independent of the inputs (Appendices A.5–A.6).

Drucker's global-budget Theorem 1.1 would also suffice. The simulator below has total cap $L$, and substituting $T=L$, error $1/3$ and $\alpha=3/r$ gives $2\beta^r$. The extra factor two is absorbed by (14).

### 4.2 Planting a winner

Let $G=\lfloor mL/100\rfloor$. Sample all rows $J_i\in[m]$ uniformly and all address inputs $A_{i,h}$ from $\mu$, mutually independently. In the **dummy input** $Y^{(0)}$, put the sole zero of column $i$ at row $J_i$ and set every certificate-cell bit to zero. Each $X_i$ contains a zero, so this is a zero-input.

Next choose $I\in[m]$ uniformly and independently of the entire dummy input. Form the **planted input** $Y^{(1)}$ by changing $X_I[J_I]$ to one and filling $B_{I,s_I}$ with the true transcripts and pointers $p_{I,s_I,j}=J_j$. Column $I$ now wins. All address inputs, and all other coordinates, remain unchanged (Figure 2). The blank-array and single-filled-cell argument follows Aaronson, Ben-David and Kothari [@ABK2016]; the hidden selected zero follows Ben-David [@BenDavid2015]. Here the unknown column will supply the factor $m$.

![The two coupled inputs with $m=4$ and $I=3$, illustrating the construction rather than its large-parameter hardness threshold. They differ only at the erased zero $X_I[J_I]$ and inside the cell $B_{I,s_I}$; the address inputs, drawn from $\mu$, are the same in both.](figures/expert_planted.svg){width=100%}

Fix a deterministic tree $\mathcal T$ of depth at most $G$. Its runs on $Y^{(0)}$ and $Y^{(1)}$ agree until the run on $Y^{(0)}$ queries $X_I[J_I]$ or a bit of $B_{I,s_I}$, so
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|
\le\Pr[\mathcal T\text{ queries }X_I[J_I]]+\Pr[\mathcal T\text{ queries }B_{I,s_I}],
\tag{10}
$$
with both probabilities computed for the run on $Y^{(0)}$. A visit to the selected cell is counted even if the queried bit remains zero after planting; this only enlarges the event covering a first difference.

### 4.3 The erased zero

Let $Z$ be the number of columns whose zero the run on $Y^{(0)}$ queries. For fixed dummy data, exactly $Z$ of the $m$ choices of $I$ select a discovered zero, so
$$
\Pr[\mathcal T\text{ queries }X_I[J_I]]=\frac{\mathbb EZ}{m}.
\tag{11}
$$
The independence of $I$ from the whole dummy run is essential; a uniform marginal law alone does not give (11) (Appendix A.4).

To bound $\mathbb EZ$ we count early and late discoveries, as the preprint does. Before the first discovery in column $i$, its zero is uniform on the rows not yet queried, conditional on the entire past. If fewer than $m/2$ distinct rows have been queried there, a new query discovers the zero with probability at most $2/m$; a repeat query makes no new discovery. These early discoveries number at most $2G/m$ in expectation. Any other discovery lies in a column that receives at least $m/2$ queries, and there are at most $2G/m$ such columns. Hence
$$
\mathbb EZ\le\frac{4G}m,\qquad
\Pr[\mathcal T\text{ queries }X_I[J_I]]\le\frac{4G}{m^2}.
$$

### 4.4 The planted cell

Let $\lambda_i$ be the number of queries, counting repetitions, that the run on $Y^{(0)}$ makes to $A_{i,1},\dots,A_{i,r}$, and call column $i$ heavy if $\lambda_i>L$. At most $G/L$ columns are heavy, and therefore $\Pr[I\text{ heavy}]\le G/(mL)$.

The position of a query already names an address: a query to a bit of $B_{i,s}$ names $s$ before any content of the cell is read. We turn this into a predictor for the answers of one column. Fix a column $i$ and a time $\tau\in\{1,\dots,G\}$. A simulator receives as free information all of $Y^{(0)}$ outside $A_{i,1},\dots,A_{i,r}$, which is jointly independent of those $r$ inputs and does not reveal $s_i$. It runs $\mathcal T$, answering other queries from the free information and querying the $A_{i,h}$ itself, and it aborts before an $(L+1)$-st query to them in total. If it reaches time $\tau$ and the $\tau$-th query lies in a cell $B_{i,s}$, it outputs $s$ before reading the cell; if it aborts or the query has another form, it outputs a fixed vector.

This predictor has total cap $L$ on the $A_{i,h}$, hence cap $L$ on each, so Lemma 4 bounds its success by $\beta^r$. If $i$ is not heavy and the $\tau$-th query of the original run lies in $B_{i,s_i}$, the simulator has not aborted and outputs $s_i$. Therefore
$$
\Pr\bigl[\,i\text{ is not heavy and the }\tau\text{-th query lies in }B_{i,s_i}\bigr]\le\beta^r .
\tag{12}
$$
This bounds a joint event under the original law. Conditioning on $i$ not being heavy would change the law of the address inputs and can make the conditional success exceed $\beta^r$ (Appendix A.7). For each fixed column, a union bound over at most $G$ query times gives $G\beta^r$. Averaging over $I$ gives
$$
\frac1m\sum_{i=1}^m\sum_{\tau=1}^G
\Pr[i\text{ not heavy and query }\tau\text{ hits }B_{i,s_i}]
\le G\beta^r.
$$
The $m$ column terms cancel against the averaging factor. Adding the heavy-column probability yields
$$
\Pr[\mathcal T\text{ queries }B_{I,s_I}]\le\frac G{mL}+G\beta^r.
\tag{13}
$$
The record traces this simulator on a small example ([§6.5](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-simulator)).

### 4.5 The contradiction and the constants

By (10), (11) and (13), with $G\le mL/100\le m^2/100$ and $\beta^r=(2/3)^{20\ell}\le m^{-10}$,
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|\le\frac{4G}{m^2}+\frac G{mL}+G\beta^r\le\frac6{100}.
\tag{14}
$$
The random column $I$ divides the first two terms by $m$, the address length $r=20\ell$ makes $\beta^r$ small enough to survive the union over $G$ query times, and the constants $1/100$ and $20$ are chosen with room to spare. A randomized algorithm of worst-case cost $G$ is an average of such trees, so it satisfies (14) as well, whereas correctness with error at most $1/3$ on every input in the two supports, averaged over their laws, would force a gap of at least $1/3$. Hence, for every $P$ and $L$ as above,
$$
R(F_{P,\mathcal C,m})>\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor.
\tag{15}
$$

For $P=P_{k,m}$ take $L$ from (5). The floors lose only constants: once (5) holds and $t\ge8$, (15) gives $R(F_{k,m})\ge m^{2-1/k}/(400\ell^2)$. The full rounding calculation is in [record §6.6](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-discrepancy). The exponent loss $1/k$ and the denominator $\ell^2$ come from the selected Forrelation hardness scale; the address length absorbs the union over query times without another power loss. The optional improvement of the erased-zero probability to $2G/[m(m+1)]$ is given in [record §6.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-zero-optional).

## 5. The Forrelation lower bound

The main separation needs the fixed-$k$ estimate (5), which follows from Bansal and Sinha's theorem for the explicit Walsh–Hadamard promise [@BansalSinha2021, Theorem 1.3 and Corollary 1.4]. Their lower bound exceeds $m^{1-1/k}/\ell^2$ for every fixed $k$ and all sufficiently large $m$. This is the analytic hardness input to the construction.

The reconstruction in [record §§3.6–3.15](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_target) gives a further estimate with explicit dependence on $k$: for $m=4^t$ and $15k+2\le2t$,
$$
R(P_{k,m})>\frac{2}{18225}\,\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{16}
$$
This improves the power of $k$ in the cited bound while worsening the logarithmic power. Its purpose here is to give an explicit sufficient threshold, $t\ge13669k^2$, for (5), and to permit the growing-$k$ family at the end of §6. The comparison and threshold calculation are in [record §3.15](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_threshold).

The proof of (16) compares the uniform law $\mathcal U$ with a correlated law $\nu_1$ built from the Gaussian-pair chain of Bansal and Sinha [@BansalSinha2021, §3]. It uses a different algebraic truncation, so the required moment estimates are proved afresh. A stopped-martingale argument bounds derivatives of a decision tree's multilinear extension, following the ordinary-tree method of Girish, Tal and Wu [@GTW2021, §1.3 and Lemma 9]. Together these give, for a depth-$d$ acceptance probability $A$, where $d\ge1$,
$$
\left|\mathbb E_{\nu_1}A-\mathbb E_{\mathcal U}A\right|
\le\left(\frac3{16\sqrt m}\right)^{k-1}
\left[(16kd\ln(4km))^{k/2}+2^{-k}\right].
$$
The controlling powers are $d^{k/2}$ and $m^{-(k-1)/2}$. For fixed $k$, a constant distinguishing advantage therefore requires depth of scale $m^{1-1/k}$, up to logarithms.

A solver is correct only on the promise, while $\nu_1$ also has off-promise mass. The bridge is a pointwise comparison. If $A$ has promise error at most $0\le\eta\le1/2$, then
$$
(1-\eta)(\Phi-\delta)\le A\le\eta+4\Phi^2/\delta^2.
$$
On the one-promise the lower bound follows from correctness; elsewhere its left side is nonpositive. On the zero-promise the upper bound follows from correctness; elsewhere its right side is at least one. The moment bounds $\mathbb E_{\nu_1}\Phi\ge a_k:=18^{-(k-1)}$ and $\mathbb E_{\mathcal U}\Phi^2=1/m$ consequently imply
$$
\mathbb E_{\nu_1}A-\mathbb E_{\mathcal U}A
\ge(1-\eta)(a_k-\delta)-\eta-\frac4{m\delta^2}.
$$
This displays the positive signal, error and uniform-law leakage in the same inequality. Constant error would swamp the exponentially small signal. Repetition reduces $\eta$ below $a_k/18$ using $O(k)$ runs; the dimension condition in (16) controls the leakage. The lower gap then contradicts the shallow-tree bound, yielding (16). The full assembly is in [record §§3.14–3.15](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_promise_gap).

The law $\nu_1$ used in this analytic proof is distinct from the minimax law $\mu$ of §4, which is supported entirely on the promise. The source comparison in [record §3.16](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_credit) identifies the borrowed ingredients and the estimates reconstructed here.

## 6. The optimal exponent

Fix $0\le\alpha<4$ and choose an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $e=2-1/k-\alpha/2>0$. Keep $k$ fixed and let $m=4^t$ grow. For $t\ge13669k^2$, (2) gives $1+Q(F_{k,m})\le(1+C_k)\sqrt m\,\ell^6$ and
$$
\frac{R(F_{k,m})}{\bigl(1+Q(F_{k,m})\bigr)^\alpha}\ge\frac{1}{400(1+C_k)^\alpha}\,\frac{m^{e}}{\ell^{2+6\alpha}}\longrightarrow\infty,
$$
so no $C_\alpha$ in (1) exists. With the upper bound of [@ABKRT2021], $\alpha_{\rm tot}=4$. The quantifiers come in the order: the exponent $\alpha$, then one fixed $k$, then its constants and threshold, then $m\to\infty$, with the same function $F_{k,m}$ in both bounds of (2). For fixed $k$ this excludes exponents below $4-2/k$.

**Remark** (one family approaching four)**.** A growing choice of $k$ needs uniform estimates; fixed-$k$ thresholds alone do not suffice (Appendix A.8). Bound (16), the generic lower bound (15), and the [explicit quantum estimate][src-budget-exponential] supply them. Taking $k=\lfloor\sqrt{t/20}\rfloor$ gives a single family $F_t=F_{k,4^t}$ with
$$
R(F_t)\ge Q(F_t)^{4-o(1)}.
$$
The calculation, including a finite error term in the exponent, is in [record §7.3](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#ROOT-GROWING-K). Its force is asymptotic; the argument does not give $R=\Omega(Q^4)$.

## 7. The formal statement

The Lean development proves [$\alpha_{\rm tot}=4$][thm-alpha], [the separating family][thm-headline], [failure of the cubic bound][thm-cubic], and [eventual Forrelation hardness][thm-forrelation] without open mathematical hypotheses. Their [statement file][statement-file] imports only Mathlib. Comparator checks the separately compiled [proofs][statement-solution] against these statements using Lean's standard axioms. The universal quartic upper bound is included, through complexitylib [@Complexitylib2026].

The definitions use the error and all-branch caps of §1. The two model bridges identify a capped randomized algorithm with a finite mixture of trees ([record §2.2](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#R3-01-CLASSICAL)) and an adaptive quantum algorithm with a fixed query sequence having the same output law ([record §2.5](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#R3-01-BRIDGES)). Reading every input bit makes the sets defining $R$ and $Q$ nonempty, and the quartic upper bound makes the set in (1) nonempty.

The compared family theorem supplies, for each fixed $k$, constants and a threshold, then one circuit for each sufficiently large $m$ that serves both complexity bounds. It states an existential logarithmic exponent and the floor lower bound (15). A [separate theorem for the fixed explicit circuit][src-constants] gives the choices $6$ and $1/400$ in (2). Lean also proves the [uniform estimate (16)][src-forrelation-uniform].

Two auxiliary interfaces merit distinction. The formal upper bound uses a sampler that measures its output label and resets the workspace; its [exact conditional label law][src-amplify-measured] is the form needed in Lemma 2. A separate result [retains the successful state][cmp-amplifier], for success tests on basis labels. The formal [direct product result][cmp-direct-product] bounds [success together with cap compliance][def-compliant] for finitely many weighted random seeds. Reduction of arbitrary independent randomness to finite seeds, and identification of recursive compliance with per-input counts, are ordinary bridges to Lemma 4 ([record §6.1 and Appendix G.8](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-direct-product-formal)). The complete statement correspondence and checking details are in [record Appendix G](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#checked-statements).

## Use of AI tools

Will Cook directed the reconstruction; AI systems drafted the text and Lean proofs and performed the recorded checks. The separation theorem, construction and original analyses are OpenAI's. Sources and proofs are in the repository [@Repo2026] and reasoning record [@Record2026].

## References

::: {#refs}
:::

<!-- pdf-page-break -->

## Appendix A. Simplifications that fail

The following examples show why the hypotheses used above cannot simply be dropped. Here $\beta$ is a one-instance success bound; in the finite examples it is the exact optimum. The cap examples test the general direct-product hypotheses, including the zero-query case, rather than the final construction's large-parameter regime.

### A.1 The projection statistic does not test the promise

Take $k=2$, $m=4$ and $z_1=z_2=(-1,1,1,1)$. Then $\Phi=-1$, so $\Phi^2=1$, yet $z$ lies outside the promise. The projection experiment therefore cannot supply the domain bit required in §2 (iii). The complete calculation is in [record §3.5](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#forr_small_instance).

### A.2 Comparisons need not describe an order or fixed orientation

A deterministic three-cycle of losers is a fixed tournament with no total order. If two losers instead defeat each other with probability $1/2$, neither orientation is computed with bounded error. The tournament of §3.2 accommodates both cases because it uses the exact comparison probabilities. See [record §5.2](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#upper-cyclic-example).

### A.3 A dominant column need not win

Let column $1$ be all ones and every other column contain a zero. Give column $1$ a correct certificate except for one pointer into a column $j>1$ that reaches a one. Column $1$ defeats every rival, using the tie-break against $j$, yet no column wins. This is why §3.3 verifies the candidate list rather than accepting a column on the strength of its comparisons.

### A.4 A uniform marginal choice need not be independent

Query row $1$ of four columns. Choose $I$ uniformly among columns whose zero was found, or among all four if none was found. The marginal law of $I$ is uniform, but its zero was found with probability
$$
\frac{175}{256}>\frac{\mathbb EZ}{m}=\frac14.
$$
Thus the identity in §4.3 requires independence of $I$ from the whole dummy run. The computation is in [record §6.4](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-selection-independence-example).

### A.5 Expected caps do not give the direct-product bound

Consider two independent instances of two-bit parity. With a cap of one query to each, the one-instance success is $\beta=1/2$. Now toss a fair coin: on one outcome read all four bits, and on the other guess both answers. The expected cost is one query per instance, but the probability of getting both answers right is
$$
\frac12+\frac12\cdot\frac14=\frac58>\beta^2.
$$
The separate caps in §4.1 must therefore hold on every branch.

### A.6 Separate independence does not imply joint independence

Let $P(x)=x$ on one fair bit and take query cap zero. For independent fair inputs $X,Y$, the side information $S=X\oplus Y$ is independent of each input separately. Given $S$, answering $(0,S)$ succeeds with probability $1/2$, although the product of the two one-instance optima is $1/4$. Lemma 4 consequently requires side information jointly independent of the entire input tuple. See [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-independent-information).

### A.7 Conditioning on compliance changes the success probability

Take independent instances $A,B$ of AND on two uniform bits. With cap one query per instance, the exact one-instance optimum is $\beta=3/4$. Query $A_0$, then $B_{A_0}$; query $A_0$ again if the answers differ; and output $(0,0)$. The caps hold on eight of the sixteen inputs, and the output is right on five of those eight. Hence
$$
\Pr[\text{success and compliance}]=\frac5{16}\le\beta^2,
\qquad
\Pr[\text{success}\mid\text{compliance}]=\frac58>\beta^2.
$$
The first probability is the joint event bounded in §4.4. Replacing it by the conditional probability invalidates the argument. The full trace is in [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/d234866c93b0878087d948d2abd8247b3a6fff7e/docs/reasoning_record.md#CL-adaptive-example).

### A.8 Fixed-parameter thresholds do not justify a growing parameter

The condition $t\ge2^k$ holds eventually for every fixed $k$, yet fails for every $t$ when $k=t$. The growing-$k$ family in §6 therefore uses estimates uniform in $k$, rather than substituting a varying parameter into an eventual fixed-$k$ statement.

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
