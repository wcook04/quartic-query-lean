---
title: "The randomized–quantum query exponent for total functions is four"
subtitle: "A companion to OpenAI's nearly quartic separation"
author: "Will Cook"
date: "November 2026"
bibliography: expert_companion.bib
link-citations: true
abstract: |
  The optimal polynomial exponent relating bounded-error randomized and quantum query complexity of total Boolean functions is four. OpenAI's construction gives separating powers arbitrarily close to four by fixing a sufficiently large Forrelation order; uniform estimates also give one family with $R(F)\ge Q(F)^{4-o(1)}$. We reconstruct two steps in its proof: sampling a column with probability proportional to its chance of surviving previous comparisons, and converting a proposed certificate query into an address prediction with a fixed query cap. Each of the $m$ columns has certificates addressed by hard partial-function values. A classical algorithm must spend order $m$ times a query allowance below the hardness of one partial instance to find the planted certificate with substantial probability. For each fixed Forrelation order $k$, the quantum cost is $\widetilde O_k(\sqrt m)$, suppressing logarithms. Comparisons need to favour only the winning column; comparisons between losers may have arbitrary probabilities. A weighted tournament finds a short candidate list, and bounded-error search over exact local tests verifies it on every input. We also identify which statements the Lean development proves and compares.
---

## 1. Introduction

For total Boolean functions, how large can the gap between randomized and quantum query complexity be? Earlier constructions approached a cubic separation, whereas the best universal upper bound was quartic. OpenAI's nearly quartic construction closes this gap [@OpenAI2026]. Its winning column defeats every rival in a cheap comparison that follows suggested pointers, even when the rival's partial-function inputs violate their promises. Checking that a suggested certificate is valid is a separate, later operation.^[AI assistance: Will Cook directed the reconstruction; AI systems drafted the text and Lean proofs and performed the recorded checks.]

A query gives access to an input coordinate; computation between queries is free. A classical query reads one bit, while a quantum query applies
$O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle$, possibly in superposition over $i$. Arbitrary input-independent unitary computation and finite workspace are free; no gate-time or space bound is asserted. For a partial Boolean function $f$, write $R(f)$ and $Q(f)$ for the least query caps of randomized and quantum algorithms that compute $f$ with probability at least $2/3$ on every input in its domain. A cap holds on every input and every branch, including inputs outside the promise. A promised-input cap can be enforced by stopping after that many queries, without changing promised-input behaviour; the coherent padding is described in [record §2.5](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#R3-01-BRIDGES). The optimal exponent for total functions is
$$
\alpha_{\rm tot}=\inf\Bigl\{\alpha\ge0:\ \exists C_\alpha>0\ \forall n\ge1\ \forall f:\{0,1\}^n\to\{0,1\},\ \ R(f)\le C_\alpha\bigl(1+Q(f)\bigr)^\alpha\Bigr\}.
\tag{1}
$$
The constant is uniform in $n$ and $f$; the added one includes constant functions.

**Theorem 1** (OpenAI's separation [@OpenAI2026, Theorem 1.1], with reconstructed constants)**.** $\alpha_{\rm tot}=4$. For each integer $k\ge2$ there is a constant $C_k>0$ such that, for all sufficiently large powers of four $m$, the total function $F_{k,m}$ defined in §2 satisfies, with $\ell=\log_2m$,
$$
Q(F_{k,m})\le C_k\sqrt m\,\ell^6
\qquad\text{and}\qquad
R(F_{k,m})\ge\frac{m^{2-1/k}}{400\ell^{2}}.
\tag{2}
$$

The quantum estimate holds for every $m=4^t$, $t\ge1$; only the randomized estimate needs a sufficiently large size for fixed $k$. The exponent six and coefficient $1/400$ are explicit choices in this reconstruction. Aaronson, Ben-David, Kothari, Rao and Tal proved $D(f)=O(Q(f)^4)$ for total $f$, where $D$ is deterministic query complexity, using Huang's sensitivity theorem [@ABKRT2021; @Huang2019]. Since $R\le D$, this gives $\alpha_{\rm tot}\le4$. They conjectured $R(f)=O(Q(f)^3)$ [@ABKRT2021, Conjecture 2]. Taking $k=3$ in (2) excludes every exponent below $10/3$, hence the cubic bound; larger fixed $k$ exclude every exponent below four.

The theorem, construction and two analyses are OpenAI's. We reconstruct the conditional tournament sampler and the capped address predictor, giving an unnormalised direct-product proof, finite counterexamples and explicit constants. The predictor outputs the address named by one proposed cell query and stops before exceeding its allowance. The reasoning record [@Record2026] supplies the longer derivations and formal correspondence; the supplier results are stated where they enter below. Both bounds in (2) use the same circuit, because the function's input stores transcripts of that chosen circuit.

### 1.1 Overview of the construction

The input has $m=4^t$ columns. Column $i$ holds a string $X_i\in\{0,1\}^m$, $r=O(\log m)$ inputs $A_{i,1},\dots,A_{i,r}$ to a Forrelation partial function $P=P_{k,m}$, and a cell $B_{i,s}$ for each address $s\in\{0,1\}^r$. When all its instances are promised, their answers form the true address $s_i$. Column $i$ wins if $X_i=1^m$ and the selected cell stores gate-value transcripts certifying these answers and points to a zero in every other column. The function is one exactly when a column wins.

![Schematic bit strips (not literal lengths). The winning column $i^\star$ is all ones. Its selected cell certifies its address and points to a zero in every other column. Every column has its own address blocks and cell array; the winner's array is enlarged here. No pointer into $X_{i^\star}$ can find a zero.](figures/expert_column.svg){width=90%}

A direct Grover search over columns would verify each candidate by searching its $K=\widetilde O_k(m)$ local tests. The resulting cost, roughly $\sqrt m\sqrt K$, is too large. Instead, compare two columns by decoding their addresses and following each column's pointer into the other. The winner defeats every rival with high probability: its pointer reaches a zero, and the rival's pointer reaches a one. This remains true when the rival's address inputs violate the promise. Two losing columns can defeat each other with any probabilities, including $1/2$.

The proof assigns weights equal to accumulated survival probabilities. The coherent tournament in §3 samples their normalized law without estimating the weights, producing a list of $O(\log m)$ candidates that contains the winner with high probability. We then verify the listed candidates.

Classically, both places where a winner can be detected are hidden. Start with one zero in each column and every certificate cell blank. Independently select a uniform column $I$, erase its zero, and fill its true cell. This changes one bit and one certificate block. Discovering the erased bit requires finding the zero of the hidden selected column, rather than just any zero. Conditional on the tested algorithm's run on the unplanted input, which finds $Z$ zeros, the independent choice of $I$ selects one of them with probability $Z/m$ (§4.3).

For the filled cell, let $1\le L\le m$ be an integer query allowance with $L<R(P)$. A total budget much smaller than $mL$ permits more than $L$ queries across a column's $r$ address blocks in only a small fraction of columns. In a run using at most $L$ such queries, a visit to that column's true cell names all $r$ hard answers by its position. A direct product bound controls the joint event of this visit and the at-most-$L$ condition under the original hard law. The same total cap also caps each block. Guessing logarithmically many independent answers is polynomially unlikely, enough for a union over all query times. Thus the randomized cost is $\Omega(mL)$. For fixed $k$, suppressing logarithms, $L$ has scale $m^{1-1/k}$, while the quantum cost is $\widetilde O_k(\sqrt m)$. The resulting separation exponent is
$$
\frac{2-1/k}{1/2}=4-\frac2k.
$$

### 1.2 Earlier separations

Ben-David gave the first super-quadratic separation for total functions, $R=\widetilde\Omega(Q^{5/2})$, by turning Forrelation into a total function [@BenDavid2015]. Aaronson, Ben-David and Kothari reached the same exponent with cheat sheets [@ABK2016, §3.1]. Their framework totalizes partial functions; the certificate and query costs determine how much separation survives.

In their AND–OR construction, a partial function $g$ on $n$ bits with polylogarithmic quantum query complexity is composed with $h=\mathrm{AND}_{m'}\circ\mathrm{OR}_{m'}$. This inner function has $R(h)=\Omega(m'^2)$, $Q(h)=O(m')$ and certificates of size $m'$. Certificates for all $n$ inner values certify the input to the outer promise. For the total cheat-sheet function $f$, a quantum algorithm computes $g\circ h$ and Grover-checks these certificates, of total size $\widetilde O(nm')$. The randomized analysis first lower-bounds $g\circ h$ and then transfers that bound through the cheat-sheet construction [@ABK2016, §3.2]:
$$
Q(f)=\widetilde O\bigl(m'+\sqrt{nm'}\bigr),\qquad R(f)=\widetilde\Omega\bigl(R(g)\,m'^2\bigr).
$$
Here $\widetilde O$ and $\widetilde\Omega$ suppress logarithmic factors, with construction parameters fixed. If $R(g)=\widetilde\Omega(n^c)$, setting $m'=n$ gives $R=\widetilde\Omega(n^{2+c})$ against $Q=\widetilde O(n)$. More generally, $m'=n^a$ with $a\ge0$ gives the exponent ratio
$$
\frac{c+2a}{\max\{a,(1+a)/2\}}.
$$
For $0\le c\le1$ this increases up to $a=1$ and is nonincreasing thereafter. Since $R(g)\le n$, the balanced AND–OR recipe certifies at most the cube. Forrelation, Tal's random-orthogonal-matrix variant (Rorrelation), and the optimal partial separations of Bansal–Sinha and Sherstov–Storozhenko–Wu give the successive total powers $5/2$, $8/3-o(1)$ and $3-o(1)$ [@Tal2020; @BansalSinha2021; @SSW2023].

At a matched supplier scale $m$, the old balanced recipe has quantum cost $\widetilde O(m)$ and classical lower bound $\widetilde\Omega(m^2R(P))$. The new construction uses $\widetilde O(\sqrt m)$ quantum queries against $\widetilde\Omega(mR(P))$. Reducing the quantum cost by a square root is what permits the exponent to approach four.

### 1.3 Relation to earlier constructions

Addressing a certificate by the answers to hard partial instances is the cheat-sheet idea of Aaronson, Ben-David and Kothari [@ABK2016]. Here each of the $m$ columns has its own array of cells, so the classical lower bound charges address queries across many possible planted columns, while the quantum algorithm searches them in about $\sqrt m$ steps. The winning condition descends from the pointer functions of Göös, Pitassi and Watson [@GPW2018], which Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs developed into a nearly quartic separation of deterministic from quantum query complexity [@ABBLSS2017].

In the predecessor giving the nearly quartic deterministic–quantum separation, each highlighted zero has a back pointer to the marked column; these pointers permit an efficient zero-error randomized algorithm. In $F_{k,m}$ a zero carries no pointer. Instead, the winner's selected cell holds $m-1$ separate $\ell$-bit pointer fields, and its address is found by computing the partial-function values. A comparison requests only the field into its rival, at cost $\ell+1$ bit queries. Verification checks all fields by Grover search over the local tests.

This field access differs from the direct-pointer symbol set aside in [@ABBLSS2017, §1.3]: reading that entire symbol would reveal all $m-1$ pointers and cost order $m\log m$ bits. That paper uses a balanced tree to reach the highlighted leaves; its separate variant without back pointers is hard even for bounded-error randomized algorithms. The present construction hides direct pointer fields behind a hard address.

The partial function is the $k$-fold Forrelation problem of Aaronson and Ambainis [@AA2018]. Bansal and Sinha proved its randomized hardness in the explicit Walsh–Hadamard form, with the one-sided thresholds used here [@BansalSinha2021]. Sherstov, Storozhenko and Wu independently proved the optimal partial separation for $k$-fold Rorrelation with a uniformly random orthogonal matrix [@SSW2023, Theorem 1.1]. The construction uses the explicit form because it also needs an exact circuit of nearly linear size for the promise and the value of $P$ (property (iii) of §2).

The closest comparison-search antecedent is the surviving-candidate set of Ambainis, Iraids and Kokainis [@AIK2026, §6.1]: retain candidates that defeat every previously selected pivot. Their oracle supplies bounded-error access to fixed edge directions. OpenAI's tournament replaces set membership by a product of exact comparison probabilities, accommodating arbitrary probabilities between losers. Section 3.2 shows that expected total surviving weight falls by at least a factor two and constructs an exact conditional sampler. Bounded-error quantum search [@HMW2003] can already search a fixed candidate-validity predicate, but evaluating that predicate costs about $\sqrt K$ local tests, leaving the nested-search cost above.

Other comparison models have different contracts: minimum finding assumes a total order [@DH1996]; king finding seeks a vertex reaching every other in at most two steps in a fixed tournament [@MPS2023]. Ben-David and Kothari use fixed comparisons of candidate claims followed by verification [@BDK2026, Lemma 5]. None of these contracts supplies the arbitrary loser probabilities needed here.

Section 2 gives the function and its local tests. Section 3 constructs the candidate list by halving expected total weight, and §4 proves the randomized lower bound; §5 completes the fixed-parameter exponent proof, and §6 gives the optional uniform refinement. Section 7 relates the theorem to Lean. Appendix A records counterexamples to tempting simplifications, and the companion exposition [@Exposition2026] develops a four-column example.

## 2. The Forrelation promise and the total function

Fix integers $k\ge2$, $t\ge1$, $m=4^t$, $\ell=2t$ and $r=20\ell$, and identify a bit $a$ with the sign $(-1)^a$. Powers of four make $\sqrt m$ integral for the exact circuit below; the factor $20$ makes address guessing small enough for the union bound in §4. Let $H$ be the normalised $m\times m$ Walsh–Hadamard matrix and $u=m^{-1/2}(1,\dots,1)^{\mathsf T}$. For sign vectors $z_1,\dots,z_k\in\{\pm1\}^m$ put
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
and undefined otherwise; in particular a large negative $\Phi$ lies outside the promise. Hardness hides an address, quantum decoding reads it cheaply, and an exact circuit decides domain membership on every input and gives the value on the domain. We use three properties of $P$, which we cite from [@OpenAI2026, Lemma 2.1]; the explanatory sketches following (ii) and (iii) are expanded in §§[3.3](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_quantum) and [3.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_circuit) of the record.

(i) For fixed $k$ and all large $m$, with $L=\bigl\lfloor m^{1-1/k}/\ell^2\bigr\rfloor$,
$$
L<R(P).
\tag{5}
$$
This follows from Bansal and Sinha's bound $R(P)=\Omega\bigl(k^{-29}(m/\log(km))^{1-1/k}\bigr)$ [@BansalSinha2021, Corollary 1.4] Their dimension $N$ is our $m$, so the total input length is $km$ (see §5).

(ii) For $0<\eta<1/2$, a quantum algorithm makes $O_k(1+\log(1/\eta))$ queries on every input and computes $P$ with error at most $\eta$ on its domain. The explicit cap in [record §3.3](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_quantum) has dependence $O(k\delta^{-2}\log(1/\eta))$.

*Decoder sketch.* The projection circuit [@AA2018, §3.2, Figure 1] prepares $u$, applies the matrices in (3) from right to left, using one phase query per sign diagonal, and measures the projection onto $u$. Its success probability is $\Phi^2$. Repeat the trial $O(\delta^{-2}\log(1/\eta))$ times and accept when the success fraction is at least $\delta^2/2$. This threshold lies between the zero-case mean, at most $\delta^2/4$, and the one-case mean, at least $\delta^2$; multiplicative Chernoff bounds give the required error.

Retaining the trial outcome bits and computing the threshold reversibly gives a coherent decoder with its workspace kept (record §3.3). It has the same cap off the promise, with arbitrary output. The subsequent constants use this projection decoder. Aaronson and Ambainis's interference test, with acceptance probability $(1+\Phi)/2$ [@AA2018, Proposition 6], is another possible decoder; exact domain membership is still supplied separately by (iii).

(iii) An exact Boolean circuit $\mathcal C$ of fan-in at most two outputs a domain bit, equal to one exactly on the domain of $P$, and a value bit equal to $P$ there. We use the record's realization with $S\le200(k+1)^2m\ell^2$ non-input gates, including its two outputs. Gates may compute any fixed Boolean function of at most two earlier wires; the gate convention and count are derived in [record §3.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_circuit).

*Circuit sketch.* With the integer matrix $\sqrt mH$, write $\Phi=N/m^{(k+1)/2}$ for an integer $N$. Fast Walsh transforms on $O_k(\ell)$-bit integers compute $N$ exactly. The circuit then tests $2^{5k}N\ge m^{(k+1)/2}$ and $2^{5k+1}|N|\le m^{(k+1)/2}$, the two cases of (4). There are $O(\ell)$ transform layers and $O_k(\ell)$ bit operations per addition, giving the two logarithmic factors. The projection statistic cannot decide the domain, because it sees only $\Phi^2$ (Appendix A.1).

**The total function.** Column $i\in[m]$ consists of $X_i\in\{0,1\}^m$, strings $A_{i,1},\dots,A_{i,r}\in\{0,1\}^{km}$, and a cell $B_{i,s}$ for each $s\in\{0,1\}^r$. The cell holds an $\ell$-bit pointer $p_{i,s,j}\in[m]$ for each $j\ne i$ and $r$ alleged transcripts of $\mathcal C$, one bit per non-input gate in its fixed topological numbering. No wiring data are supplied by the input. Every $\ell$-bit pointer word names a row, with no null pointer, so even a false certificate or wrongly decoded cell can be followed. These coordinates are freely assignable; the alleged transcripts need not be true.

Column $i$ **wins** if $X_i=1^m$, every $P(A_{i,h})$ is defined, and the cell at $s_i=(P(A_{i,1}),\dots,P(A_{i,r}))$ holds the true transcripts of $\mathcal C$ on each $A_{i,h}$ and pointers with
$$
X_j[p_{i,s_i,j}]=0\qquad\text{for every }j\ne i.
\tag{6}
$$
We set $F_{k,m}=1$ if some column wins and $F_{k,m}=0$ otherwise. The definition imposes no promise on the address inputs, pointers or transcripts, so $F_{k,m}$ is total. At most one column wins: a second all-one column would make the first column's required pointer test impossible.

The function depends on $\mathcal C$, because its cells hold that circuit's transcripts. For each $k,m$ we fix one circuit with property (iii), and use it for both bounds in (2). The lower bound holds for every such circuit; the upper bound uses its size $S$.

The encoding length, distinct from the column dimension $m$, is
$$
N_{k,m}=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr]=O_k(m^{22}\ell^3).
$$
The addressed cells dominate this count: each column has $2^r=m^{20}$ cells. Thus $F_{k,m}$ is defined on a finite Boolean cube of polynomial size in $m$ for fixed $k$.

**Local tests** [@OpenAI2026, Lemma 2.2]. For a pair $(i,s)$, the event that $i$ wins and $s=s_i$ is the conjunction of
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3)
$$
tests: $m$ tests $X_i[y]=1$, $m-1$ pointer tests, $rS$ gate-consistency tests, and $2r$ output tests (domain bit $1$, value bit $s_h$). The output tests are additional to the consistency tests at the output gates: consistency determines their values, while the two tests enforce the required domain and answer. Induction in topological order shows that a gate-consistent transcript is the true evaluation, so the output tests say that $P(A_{i,h})$ is defined and equals $s_h$. Thus every test passes at $(i,s_i)$ when $i$ wins, and when $i$ does not win some test fails at $(i,s)$ for every address $s$.

A gate test reads its proposed output and at most two predecessors, from the address input or transcript as appropriate, and checks the fixed Boolean gate equation. Its cap is three queries; a pointer test uses $\ell+1$ adaptive queries. Test enumeration and wire locations are fixed and query-free. Pad shorter tests with disabled reads to the common cap $\max\{3,\ell+1\}$, retain the answers, and compute their indices reversibly. This gives coherent access with the test index in superposition at constant-factor overhead; a controlled read uses at most two ordinary queries (record §§[4.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-local-tests)–[4.6](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-coherent-tests)). The circuit size enters through $\sqrt K$ local-test evaluations, with the $O(\ell)$ query cost of each test paid separately.

## 3. The quantum upper bound

The upper bound has two parts: produce a short list containing the winner, then verify that list. The list is obtained by a tournament that needs no reliability guarantee for comparisons between losers. Put $T=\lceil\log_2(1000m)\rceil$ for the maximum list length and $\varepsilon=1/(1000T)$ as a common subroutine error budget.

The sampling step uses the following bounded form of amplitude amplification. Its essential feature is preservation of the conditional output law: below, the preparation succeeds with probability $W/m$, where $W$ is the total surviving weight and, on success, samples a label proportionally to its weight. The routine need not know $W$.

**Lemma 2** (bounded amplification [@OpenAI2026, Lemma 3.1])**.** Let $\mathcal A$ be a reversible state preparation with a designated success bit and output label. The success test reads the designated flag produced by $\mathcal A$; the test itself is fixed independently of the input and requires no oracle queries. Let its success probability be $p$. Given $0<\gamma\le1/2$ and $0<\eta<1/2$, one procedure, fixed from $\gamma$, $\eta$ and the register interface without knowing $p$, makes $O(\gamma^{-1/2}\log(1/\eta))$ calls to $\mathcal A$ and $\mathcal A^{-1}$ on every branch and either reports failure or returns a successful label. Conditional on success, the label has exactly its law under $\mathcal A$ conditional on the original preparation succeeding. Failure has probability at most $\eta$ if $p\ge\gamma$, and occurs surely if $p=0$.

*Proof.* The case $p=0$ cannot yield success. For $0<p<1$, write $\mathcal A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle$, where $\sin^2\theta=p$, $0<\theta<\pi/2$, and $|g\rangle$ is the normalised successful component. The standard iterate $-\mathcal A S_0\mathcal A^{-1}S_{\rm good}$ uses reflections about the zero state and the fixed success subspace. It changes only the two coefficients, so a successful measurement always leaves $|g\rangle$ up to global phase [@BHMT2002, §2, Lemma 1].

In a fresh trial, use a direct measurement with probability $1/2$; otherwise choose a uniform $j\in\{0,\dots,M-1\}$ Grover iterations, with $M=\lceil10/\sqrt\gamma\rceil$. The direct branch covers $p\ge1/2$, including $p=1$, without a normalized failure component. For $\gamma\le p\le1/2$, the averaged Grover probability is at least $9/20$ [@BBHT1998, arXiv v1, §4, Lemma 2; [record §5.1](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#upper-small-probability)]. Thus every trial succeeds with probability at least $9/40$. A fixed $O(\log(1/\eta))$ number of trials gives the cap and failure bound. Each successful trial has the same conditional label law, so stopping at the first success preserves it. $\square$

The cutoff gives a worst-case bound even when $p<\gamma$. The untruncated QSearch routine of [@BHMT2002, Theorem 3] instead has an expected-cost guarantee. The record gives the [numerical trial bound](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#upper-small-probability) and the separate [retained-output-state argument](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#upper-returned-register); the tournament uses only the measured label law.

### 3.1 Comparing two columns

To decode column $i$, run §2(ii) on each $A_{i,h}$ with error $\varepsilon/r$, at cost $O_k(r\log(r/\varepsilon))$. If all $r$ instances are promised, the decoded address is $s_i$ with probability at least $1-\varepsilon$; otherwise the decoder still returns some address within the same cap.

For a pair of distinct columns, sort their indices as $i<j$, retaining the original labels or a swap tag so that this operation is reversible. Run one fixed circuit that decodes both and follows their pointers into each other. In the ordered pair of bits read from $X_j$ and $X_i$, respectively, $(0,1)$ makes $i$ win and $(1,0)$ makes $j$ win. Equal bits give a tie, won by the smaller index $i$. A self-comparison sets the losing flag without decoding or following a pointer. For this fixed input, let $a_{ij}$ be the probability that $i$ defeats $j$. Both orders run the same circuit, so
$$
a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0.
\tag{7}
$$
The comparison reads pointers, leaving transcript checking to verification. It retains the decoded labels as unchanged controls in orthogonal registers; consequently their success masses add without interference. Keeping all registers gives a reversible preparation with these same probabilities $a_{ij}$.

If $i^\star$ wins, no pointer finds a zero in $X_{i^\star}=1^m$, and whenever $i^\star$ is decoded correctly its pointer finds a zero in its rival. Hence $a_{i^\star j}\ge1-\varepsilon$ for every $j\ne i^\star$, whatever the rival's address inputs. Only comparisons involving the winner need a correctness guarantee. The query cost is $c=O_k(r\log(r/\varepsilon)+\ell)=O_k(\ell\log\ell)$, since $r,T=\Theta(\ell)$ and $1/\varepsilon=1000T$.

### 3.2 A tournament with probabilistic comparisons

**Proposition 3** [@OpenAI2026, Proposition 3.2]**.** Let $m\ge2$ be an integer, $T=\lceil\log_2(1000m)\rceil$ and $\varepsilon=1/(1000T)$. Suppose a reversible comparison circuit is coherently controlled by two candidate indices, retains its workspace, and uses at most $c$ queries on every input, as does its inverse. For every fixed input its probabilities satisfy (7). One algorithm, fixed by $m$ and this circuit interface before the input is supplied, uses $O(c\sqrt m\,T^2\log T)$ queries on every branch and returns at most $T$ candidates. If some $i^\star$ satisfies $a_{i^\star j}\ge1-\varepsilon$ for all $j\ne i^\star$, the list contains it with probability at least $1-2m2^{-T}-T\varepsilon$.

For deterministic comparisons, the candidates that defeat every previous pivot form a surviving set [@AIK2026, §6.1]. For probabilistic comparisons we assign candidate $i$ the weight $w_i=\prod_{b=1}^n a_{i\rho_b}$ after $n$ pivots $\rho_1,\dots,\rho_n$ have been selected. These are analysis quantities; the algorithm never computes the weights. The weight $w_i$ is candidate $i$'s probability of defeating all those pivots in fresh comparisons, conditional on the fixed input and pivot history. It requires no independence among input bits. The target law for the next pivot is proportional to these weights.

The algorithm starts with an empty list. At each of at most $T$ stages it compares a uniformly superposed candidate with every measured pivot in fresh registers, flagging success when all comparisons are won, as in (9), applies Lemma 2, and either appends the measured label or stops on failure. It then returns the list. The length and query cap hold even if there is no dominant candidate; the probability of including $i^\star$ is proved by the ideal process below.

*Ideal process.* Start with weights $w_i=1$ and $W=\sum_iw_i$. For at most $T$ steps, and only while $W>0$, draw a pivot $\rho$ with probability $w_\rho/W$, append it to the list, and update $w_i\leftarrow w_i\,a_{i\rho}$. The selected pivot's weight becomes zero, so it cannot be selected again. The pivot law contributes $w_\rho/W$; pairing the terms $(i,\rho)$ and $(\rho,i)$ by (7) gives
$$
\mathbb E[W_{\rm new}\mid w]=\frac1W\sum_{\rho,i}w_\rho w_i a_{i\rho}=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\tag{8}
$$
Thus the expected new total weight is at most half the old total. No order or transitivity enters, so cycles among losers do no harm. Write $W_n$ for the weight after $n$ pivots, keeping it zero after extinction. Then $\mathbb EW_T\le m2^{-T}$. If $i^\star$ is absent after $T$ steps, its weight is at least $(1-\varepsilon)^T\ge1-T\varepsilon>1/2$. Hence the miss event is contained in $\{W_T>1/2\}$, whose probability is at most $2m2^{-T}$ by Markov's inequality.

*Exact sampling.* Only the measured pivot list persists between stages, so each stage rebuilds its comparisons in fresh workspace; this rebuilding is charged below. The first stage has no pivots and is a uniform label superposition with success certain. Given $\rho_1,\dots,\rho_n$ with $n<T$, prepare
$$
\frac1{\sqrt m}\sum_{i=1}^m|i\rangle\bigotimes_{b=1}^{n}|\phi(i,\rho_b)\rangle,
\tag{9}
$$
where $|\phi(i,\rho_b)\rangle$ is the full comparison state in a fresh workspace. The global success flag computes the conjunction of the comparison flags while retaining those flags. For a fixed label, the fresh workspaces multiply the success probabilities; orthogonal labels then add their masses. Thus, for the fixed input and history, the success-and-label mass is $m^{-1}\prod_ba_{i\rho_b}=w_i/m$. The total success probability is therefore $W/m$, and the label law conditional on success is $w_i/W$. We apply Lemma 2 with $\gamma=1/(2m)$ and $\eta=\varepsilon$ and take the returned label as the next pivot; on reported failure we stop and return the list.

For example, in an abstract four-candidate comparison let candidate $1$ defeat all others surely, and let $a_{23}=1/3$, $a_{24}=3/4$, $a_{34}=2/5$, with complementary reverse probabilities and zero diagonal. After pivot $2$, the weights are $(1,0,2/3,1/4)$. The preparation succeeds with probability $23/48$, and its conditional label law is $(12/23,0,8/23,3/23)$. If pivot $4$ is selected next, multiplying the existing weights, in particular $(2/3)(2/5)=4/15$, gives $(1,0,4/15,0)$, with success probability $19/60$ and conditional law $(15/19,0,4/19,0)$. These fractional weights illustrate the proposition; no realisation by the four-column Boolean example is assumed.

*Coupling.* At a pivot history $h$ before $i^\star$ is selected, $W/m\ge1/(2m)$. If the sampler's failure probability there is $f(h)\le\varepsilon$, its real next-label probability is exactly $(1-f(h))w_i/W$; its remaining mass $f(h)$ stops the procedure. Couple a successful transition to the ideal draw at each such history. A union bound over the at most $T$ opportunities to stop adds at most $T\varepsilon$ to the ideal miss probability. Once $i^\star$ is listed, later failure cannot remove it.

With $n$ previous pivots, a preparation uses at most $O(c(n+1))$ queries, including a harmless allowance for the empty history. Its amplified stage therefore costs $O(c(n+1)\sqrt m\log(1/\varepsilon))$ on every input. Summing $n+1$ over $n<T$ gives $T(T+1)/2$, and $\log(1/\varepsilon)=O(\log T)$ proves the stated cap. The record supplies the [full theorem, stagewise coupling and finite cost calculation](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#upper-tournament-statement).

### 3.3 Verification and the query count

Pairwise dominance does not imply a valid certificate: the smallest-index all-one column can win every tie while one of its pointers is false (Appendix A.3). We therefore verify each listed candidate. Decode its address afresh and measure it. At that address, a uniformly random local test fails with probability zero if all $K$ tests pass and at least $1/K$ otherwise. Lemma 2 with $\gamma=1/K$ and $\eta=\varepsilon$ searches for a failing test in $O(\sqrt K\,\ell\log(1/\varepsilon))$ queries.

The search reports either a defect or no defect found. Reject the candidate on a defect, accept it otherwise, and accept the input if any candidate is accepted.

A nonwinning column fails some test at every address (§2), including addresses decoded from unpromised inputs. Fresh verifier randomness acts on the same fixed input, so its acceptance probability is at most $\varepsilon$ conditional on any selected list and earlier history. The winner is accepted whenever its address is decoded correctly.

On a zero-input, a union bound over the list gives error at most $T\varepsilon$. On a one-input, rejection requires missing the winner, of probability at most $2m2^{-T}+T\varepsilon$, or decoding its address incorrectly during verification, of probability at most $\varepsilon$. Earlier acceptance of a false candidate cannot hurt this decision. Since $2m2^{-T}\le1/500$, $T\varepsilon=1/1000$ and $\varepsilon\le1/1000$, the error is below $1/3$.

One comparison costs $c=O_k(\ell\log\ell)$ queries, so Proposition 3 costs $O(c\sqrt m\,T^2\log T)$. For verification, the first term below decodes $T$ addresses and the second searches their local tests:
$$
O_k\bigl(T\ell\log\ell+T\sqrt K\,\ell\log T\bigr).
$$
Since $T=O(\ell)$ and $K=O_k(m\ell^3)$, the tournament costs $O_k(\sqrt m\,\ell^3(\log\ell)^2)$ and the verification costs $O_k(\sqrt m\,\ell^{7/2}\log\ell)$. Both are at most $C_k\sqrt m\,\ell^6$ for $\ell\ge2$. This deliberately loose common bound holds on every input and branch for all $k\ge2$, $t\ge1$. The fixed-parameter exponent proof needs only that $C_k$ is fixed when $k$ is; §6 gives the uniform envelope for a growing $k$.

## 4. The randomized lower bound

**Proposition 4 (classical reduction).** Let $P:D\to\{0,1\}$, with $D\subseteq\{0,1\}^n$, be a finite partial Boolean function. Fix an exact fan-in-two circuit $\mathcal C$ whose domain bit is $1$ exactly on $D$ and whose value bit equals $P$ there. For integers $L\ge1$ and $t\ge1$, put $m=4^t$ and form the total function $F_{P,\mathcal C,m}$ as in §2, with $r=20\log_2m$ address instances per column and that same circuit in every transcript. Then
$$
R(F_{P,\mathcal C,m})>\left\lfloor\frac{mL}{100}\right\rfloor
\qquad\text{whenever }1\le L\le m\text{ and }L<R(P).
$$
Forrelation enters only when we choose $L$ at the end. This reduction imposes no circuit-size restriction; size matters only for quantum verification.

Choose a law $\mu$ on the domain of $P$ under which every deterministic tree of depth at most $L$ has success at most $\beta=2/3$. Such a law exists by finite minimax [@Yao1977] ([record §6.2](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-minimax)): because $L<R(P)$, the best worst-case success at cap $L$ is below $2/3$, and compactness ensures that the optimum is attained. We use $r$ independent samples from this law to hide an address. Their answer bits need not be uniform; even constant-output trees are covered by the success bound. A planted one-input will differ from a zero-input only at one erased zero and one filled cell. The two discovery probabilities are bounded in §§4.3–4.4.

### 4.1 A direct product with separate caps

The eventual predictor outputs the address named by one proposed cell query. The following lemma bounds its success. A reader may temporarily take the lemma's contract, continue to the simulator in §4.4, and return here after (12), before the union over query times.

**Lemma 5** [@OpenAI2026, Lemma 4.1]**.** Let $L\ge0$ and $r\ge1$ be integers, and let $\mu$ be a law on the domain of $P$ under which every deterministic tree of depth at most $L$ has success at most $\beta$. Let $U_1,\dots,U_r$ be independent with law $\mu$. An algorithm that makes at most $L$ queries to each $U_h$ on every branch, interleaving them adaptively, outputs $(P(U_1),\dots,P(U_r))$ with probability at most $\beta^r$. Its coins and side information may be arbitrary if jointly independent of the entire input tuple.

*Proof.* Fix the coins and side information first; joint independence leaves the input law $\mu^{\otimes r}$. We work with unnormalised measures so that zero-probability branches need no conditioning. For a nonnegative measure $\nu$ on the domain of $P$, let $V_d(\nu)$ be the largest $\nu$-weight of correct inputs for any tree of depth at most $d$. Then $V_0(\nu)=\max_b\nu(P=b)$ and
$$
V_{d+1}(\nu)=\max\Bigl\{V_d(\nu),\ \max_y\bigl[V_d(\nu_{y,0})+V_d(\nu_{y,1})\bigr]\Bigr\},
$$
where $\nu_{y,b}$ restricts $\nu$ to inputs whose bit $y$ is $b$. The first alternative keeps any strategy using at most $d$ queries; the second queries $y$ and chooses an optimal continuation for each reply.

A fixed adaptive transcript restricts each input separately, so its unnormalised law still factors. For product measures $\nu_1\otimes\dots\otimes\nu_r$ and remaining allowances $L_1,\dots,L_r$, induction on the tree bounds the fully correct weight by $\prod_hV_{L_h}(\nu_h)$. At a leaf output $b$, that weight is $\prod_h\nu_h(P=b_h)$, at most this product because each $V_{L_h}$ permits a constant answer. A query to coordinate $y$ of input $h$ is legal only if $L_h\ge1$; it changes only $\nu_h$ and $L_h$. The two inductive bounds sum to
$$
\left(\prod_{j\ne h}V_{L_j}(\nu_j)\right)
\left[V_{L_h-1}(\nu_{h,y,0})+V_{L_h-1}(\nu_{h,y,1})\right]
\le\prod_jV_{L_j}(\nu_j).
$$
The unchanged factors can be taken outside the sum precisely because the law is a product. Initially every factor is at most $\beta$. Average over the previously fixed coins and side information to finish. $\square$

The [weighted-value proof in the record](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-weighted-values) gives the same unnormalised recurrence. We use this separate-cap form for its exact factor $\beta^r$ and short proof. Per-path allowances go back to Shaltiel's fair trees, for XOR advantage under uniform inputs [@Shaltiel2003, ECCC version, §5, Definition 4 and Theorem 5]; Drucker's Lemmas 3.1–3.2 and the fair specialisation at the end of §3 give the product bound used here [@Drucker2012]. The caps must hold on every branch, and side information must be jointly independent of the inputs (Appendices A.5–A.6).

Drucker's global-budget Theorem 1.1 would also suffice. The simulator below has total cap $L$. The substitution $T=L$, error $1/3$ and $\alpha=3/r$ is admissible since $r=20\ell\ge40$, and gives $(2^{1/r}\beta)^r=2\beta^r$ ([record §6.1](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-literature-and-verification)). This factor-two alternative still leaves the discrepancy below $1/3$.

### 4.2 Planting a winner

Let $G=\lfloor mL/100\rfloor$. Sample all rows $J_i\in[m]$ uniformly and all address inputs $A_{i,h}$ from $\mu$, mutually independently. In the **dummy input** $Y^{(0)}$, put the sole zero of column $i$ at row $J_i$ and set every certificate-cell bit to zero. Each $X_i$ contains a zero, so this is a zero-input. No separate invalid-cell marker is needed: the all-one condition already fails in every column.

Next choose $I\in[m]$ uniformly and independently of the entire dummy input. Form the **planted input** $Y^{(1)}$ by changing $X_I[J_I]$ to one and filling $B_{I,s_I}$ with the true transcripts and pointers $p_{I,s_I,j}=J_j$. Column $I$ now wins. All address inputs, and all other coordinates, remain unchanged (Figure 2). The blank-array and single-filled-cell argument follows Aaronson, Ben-David and Kothari [@ABK2016, §3.2]; the hidden selected zero follows Ben-David [@BenDavid2015, §5.1]. The latent choice $I$ is not a separate input field: only its erased zero and filled cell reveal it. This hidden column supplies the factor $m$.

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

To bound $\mathbb EZ$, count early and late discoveries. Before a column's first discovery, its zero remains uniform on its unqueried rows conditional on the entire past: the transcript excludes only rows read there, since the other data are independent and all cells are blank. Before $m/2$ distinct rows have been queried, a new query finds the zero with probability at most $2/m$; a repeat query makes no new discovery. Let $E_\tau$ indicate an early discovery at query slot $\tau$, putting $E_\tau=0$ after halting. Summing conditional expectations over the at most $G$ slots gives $\mathbb E\sum_\tau E_\tau\le2G/m$.

Every late discovery is in a column receiving at least $m/2$ queries. There are at most $2G/m$ such columns on any run. Hence
$$
\mathbb EZ\le\frac{4G}m,\qquad
\Pr[\mathcal T\text{ queries }X_I[J_I]]\le\frac{4G}{m^2}.
$$

### 4.4 The planted cell

Let $\lambda_i$ count all queries, including repetitions, to $A_{i,1},\dots,A_{i,r}$ over the entire dummy run. Call $i$ heavy if $\lambda_i>L$. Pathwise, $\sum_i\lambda_i\le G$, so at most $G/L$ columns are heavy. Conditional on that run, the independent uniform $I$ is heavy with probability equal to their number divided by $m$. Thus $\Pr[I\text{ heavy}]\le G/(mL)$.

A query to a bit of $B_{i,s}$ names $s$ before reading any cell content. To turn this into a predictor, fix a column $i$ and an original-tree query time $\tau\in\{1,\dots,G\}$. This clock counts all queries; the simulator's cap counts only queries to the target address inputs.

The simulator receives all of $Y^{(0)}$ outside $A_{i,1},\dots,A_{i,r}$ as free information. These data are jointly independent of the target inputs and do not reveal $s_i$: they comprise outside address inputs, zero locations and blank cells. The simulated tree still receives only the replies it asks for.

Run $\mathcal T$, answering other queries from the free information and querying the target $A_{i,h}$ directly. Abort before an $(L+1)$-st target query in total. If time $\tau$ is reached and its query is in $B_{i,s}$, output $s$ before reading the cell. On abort, earlier termination of $\mathcal T$, or any other query form, output a fixed vector.

The [trace in record §6.5](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-simulator-example) uses a different supplier, total two-bit XOR, with zero-based labels. It shows the two clocks and stopping before the second target query.

The predictor has total target cap $L$, hence cap $L$ on each block, so Lemma 5 bounds its success by $\beta^r$. If the terminal count $\lambda_i\le L$, every prefix also uses at most $L$ target queries. Thus whenever the original run is light and its $\tau$-th query is in $B_{i,s_i}$, the simulator reaches that query and outputs $s_i$. For fixed $i,\tau$, averaging the original target product law and independent outside dummy data gives
$$
\Pr\bigl[\,i\text{ is not heavy and the }\tau\text{-th query lies in }B_{i,s_i}\bigr]\le\beta^r .
\tag{12}
$$
This bounds a joint event under the original law. Conditioning on $i$ not being heavy would change the law of the address inputs and can make the conditional success exceed $\beta^r$ (Appendix A.7). For each fixed column, a union bound over at most $G$ query times gives $G\beta^r$. Averaging over $I$ gives
$$
\begin{aligned}
\Pr[I\text{ light and }B_{I,s_I}\text{ visited}]
&\le\frac1m\sum_{i=1}^m\sum_{\tau=1}^G
\Pr[i\text{ light and query }\tau\text{ hits }B_{i,s_i}]\\
&\le G\beta^r.
\end{aligned}
$$
The $m$ column terms cancel against the averaging factor. Adding the heavy-column probability yields
$$
\Pr[\mathcal T\text{ queries }B_{I,s_I}]\le\frac G{mL}+G\beta^r.
\tag{13}
$$
If $G=0$, the time union is empty and no cell is visited; no simulator is required.

### 4.5 The contradiction and the constants

By (10), (11) and (13), with $G\le mL/100\le m^2/100$ and $\beta^r=(2/3)^{20\ell}\le m^{-10}$ because $20\log_2(3/2)>10$,
$$
\bigl|\Pr[\mathcal T(Y^{(1)})=1]-\Pr[\mathcal T(Y^{(0)})=1]\bigr|\le\frac{4G}{m^2}+\frac G{mL}+G\beta^r\le\frac6{100}.
\tag{14}
$$
The erased-zero, heavy-column and light-cell terms are at most $4/100$, $1/100$ and $1/(100m^8)\le1/100$, respectively. The random column $I$ supplies the factor $1/m$ in the first two terms; the address length absorbs the union over $G$ query times in the third.

A randomized algorithm of cap $G$ is an average of deterministic trees. The absolute difference of its two acceptance probabilities is at most the average of their absolute differences, so (14) still holds. Yet correctness with error at most $1/3$ on every input in both supports would force an averaged gap of at least $1/3$. Hence, for every $P$ and $L$ above,
$$
R(F_{P,\mathcal C,m})>\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor.
\tag{15}
$$

For $P=P_{k,m}$ take $L$ from (5) and write $a=m^{1-1/k}/\ell^2$. If $t\ge8$, then $a\ge1$ and $mL\ge200$. The elementary estimate $\lfloor x\rfloor\ge x/2$ for $x\ge1$ gives $L\ge a/2$ and $G\ge mL/200\ge ma/400$. Thus (15) implies the lower bound in (2). The [floor calculation in record §6.6](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-floors) verifies the size conditions. The exponent loss $1/k$ and denominator $\ell^2$ come from the selected Forrelation allowance; the address length handles the time union without another power loss.[^zero-refinement]

[^zero-refinement]: The optional sharper erased-zero probability $2G/[m(m+1)]$ is proved in [record §6.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-zero-optional). It is not needed for (2).

## 5. Completing the fixed-parameter proof

The main separation needs the fixed-$k$ estimate (5). Bansal and Sinha's theorem for the explicit Walsh–Hadamard promise gives $R(P)\ge c k^{-29}(m/\log_2(km))^{1-1/k}$ in its asymptotic range [@BansalSinha2021, arXiv v3, Theorem 1.3 and Corollary 1.4]. For fixed $k$ and $m\ge k$, its ratio to $m^{1-1/k}/\ell^2$ is at least $c k^{-29}2^{-(1-1/k)}\ell^{1+1/k}$, which tends to infinity. This supplies (5); the record also proves the needed weaker hardness estimate directly.


Fix $0\le\alpha<4$ and choose an integer $k\ge2$ with $k>2/(4-\alpha)$, so that $e=2-1/k-\alpha/2>0$. Keep $k$ fixed and let $m=4^t$ grow. For all sufficiently large $t$ (depending on this fixed $k$), (2) gives $1+Q(F_{k,m})\le(1+C_k)\sqrt m\,\ell^6$ and
$$
\frac{R(F_{k,m})}{\bigl(1+Q(F_{k,m})\bigr)^\alpha}\ge\frac{1}{400(1+C_k)^\alpha}\,\frac{m^{e}}{\ell^{2+6\alpha}}\longrightarrow\infty,
$$
so no $C_\alpha$ in (1) exists. With the upper bound of [@ABKRT2021], $\alpha_{\rm tot}=4$. The quantifiers come in the order: the exponent $\alpha$, then one fixed $k$, then its constants and threshold, then $m\to\infty$, with the same function $F_{k,m}$ in both bounds of (2). For fixed $k$ this excludes exponents below $4-2/k$.

## 6. Optional uniform refinement

The reconstruction in [record §§3.6–3.15](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_target) gives a further estimate with explicit dependence on $k$: for $m=4^t$ and $15k+2\le2t$,
$$
R(P_{k,m})>\frac{2}{18225}\,\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{16}
$$
The estimate has different parameter dependence from the cited bound; its value here is explicit uniform control, not a claim of dominance or priority. Its purpose here is to give an explicit sufficient threshold, $t\ge13669k^2$, for (5), and to permit the growing-$k$ family below. The comparison and threshold calculation are in [record §3.15](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_threshold).

The proof compares the uniform law $\mathcal U$ with a correlated law $\nu_1$ on $k$ sign blocks of length $m$. Draw $k-1$ independent Gaussian vectors, pair each with its Walsh transform, apply a bounded bias function to their coordinates, and round independently to signs conditional on those biases. The blockwise construction is in [record §3.9](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_distribution); $\nu_1$ may put mass off the promise and differs from the minimax law $\mu$ of §4. The Gaussian-pair architecture is Bansal and Sinha's [@BansalSinha2021, §3]. The record's algebraic bias function gives elementary moment and kernel estimates ([§3.8](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_stein)).

For the exponent, the important step is the following shallow-tree estimate. Interpolating the first block passes a derivative through all $k$ blocks. A stopped-martingale bound controls the resulting order-$k$ derivative sum, following Girish, Tal and Wu [@GTW2021, §1.3 and Lemma 9]. The assembly in [record §3.12, (F33)](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_advantage) gives, for the acceptance function $A$ of a depth-$d$ tree with $d\ge1$,
$$
\left|\mathbb E_{\nu_1}A-\mathbb E_{\mathcal U}A\right|
\le\left(\frac3{16\sqrt m}\right)^{k-1}
\left[(16kd\ln(4km))^{k/2}+2^{-k}\right].
$$
Linearity and the triangle inequality extend the bound to convex mixtures of such trees, hence to an algorithm's acceptance probability $A\in[0,1]$. The controlling powers are $d^{k/2}$ and $m^{-(k-1)/2}$: for fixed $k$, constant distinguishing advantage requires depth of scale $m^{1-1/k}$, up to logarithms.

A solver is correct only on the promise, while $\nu_1$ also has off-promise mass. The bridge is a pointwise comparison. Let $0\le\eta\le1/2$. If $A$ has error at most $\eta$ on promised inputs, then
$$
(1-\eta)(\Phi-\delta)\le A\le\eta+4\Phi^2/\delta^2.
$$
On the one-promise, $\Phi-\delta\le1$ and correctness gives the lower bound; elsewhere $\Phi-\delta\le0$. On the zero-promise, correctness gives the upper bound; elsewhere $4\Phi^2/\delta^2>1\ge A$. The moment bounds $\mathbb E_{\nu_1}\Phi\ge a_k:=18^{-(k-1)}$ and $\mathbb E_{\mathcal U}\Phi^2=1/m$ consequently imply
$$
\mathbb E_{\nu_1}A-\mathbb E_{\mathcal U}A
\ge(1-\eta)(a_k-\delta)-\eta-\frac4{m\delta^2}.
$$
This displays the signal, error and uniform-law leakage together. Constant error would swamp the exponentially small signal. Repetition reduces $\eta$ below $a_k/18$ using $O(k)$ runs; for an original cap $D$, the record uses the padded cap $d=50kD+1$. The dimension condition gives $4/(m\delta^2)\le\delta$, and the lower gap is at least $119a_k/144$. If $D$ were at most the right side of (16), the shallow-tree bound would be at most $7a_k/12$, a contradiction. The [assembly in record §§3.14–3.15](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_uniform_assembly) derives these margins and the coefficient $2/18225$.

The source comparison in [record §3.16](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_credit) identifies the borrowed ingredients and the estimates reconstructed here.

**Consequence (one family approaching four).** This uses a new allowance from (16), not the fixed-$k$ threshold for (5). Put
$$
X=\frac2{18225}\frac{m^{1-1/k}}{k^2\ln(4km)},\qquad L=\lfloor X\rfloor.
$$
For $15k+2\le2t$ and $t\ge32$, the [calculation in record §7.3](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#ROOT-GROWING-K) gives $2\le X<m$, so (15) applies. Its lower bound and the [uniform quantum estimate](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#ROOT-GROWING-K) give
$$
\begin{aligned}
R(F_{k,4^t})&>\frac{m^{2-1/k}}{1822500\,k^2\ln(4km)},\\
Q(F_{k,4^t})&\le2^{53}k\,2^{10k}\sqrt m\,\ell^6.
\end{aligned}
$$
The quantum inequality holds for every $k\ge2,t\ge1$. Take $k=\lfloor\sqrt{t/20}\rfloor$ for $t\ge80$, which satisfies the classical conditions as well. The family $F_t=F_{k,4^t}$ then satisfies, as $t\to\infty$,
$$
R(F_t)\ge Q(F_t)^{4-o(1)}.
$$
The choice balances the classical exponent loss of order $1/k$ against the quantum overhead of order $k/t$ from $2^{10k}$. The finite exponent loss proved in [record §7.3](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#ROOT-GROWING-K) is $O(t^{-1/2}+\log t/t)$. The displayed classical bound diverges, and $R=O((1+Q)^4)$ forces $Q(F_t)\to\infty$ as well. Thus the asymptotic separation is nonvacuous, though it does not give $R=\Omega(Q^4)$.

## 7. The formal statement

The Lean development proves [$\alpha_{\rm tot}=4$][thm-alpha], [the fixed-$k$ separating family][thm-headline], [failure of the cubic bound][thm-cubic], and [eventual Forrelation hardness][thm-forrelation] without open mathematical hypotheses. The [Mathlib-only statement file][statement-file] is the specification; separately compiled [proofs][statement-solution] are compared against it. The 3 November 2026 Comparator receipt and its axiom and execution conventions are recorded in [Appendix G.3–G.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#checked-statements). No new execution is claimed here. The universal quartic upper bound is included through complexitylib [@Complexitylib2026], with its mathematical source and versioned implementation identified in [Appendix G.9](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#ROOT-EXPONENT-CORRESPONDENCE).

The definitions use the error and all-branch caps of §1. The two model bridges identify a capped randomized algorithm with a finite mixture of trees ([record §2.2](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#R3-01-CLASSICAL)) and an adaptive quantum algorithm with a fixed query sequence having the same output law ([record §2.5](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#R3-01-BRIDGES)). These identifications preserve the query cap and the output law.

The compared family theorem supplies, for each fixed $k$, constants and a threshold, then one circuit for each sufficiently large $m$ serving both bounds. It states an existential logarithmic exponent and the floor bound (15). The [fixed-circuit theorem][src-constants] gives the choices $6$ and $1/400$ in (2). It and the [uniform Forrelation estimate (16)][src-forrelation-uniform] have recorded build and axiom-audit evidence but are outside the configured comparison bundle; [Appendix G.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#checked-statements) identifies those observations and their source editions. The growing-family calculation in §6 is an ordinary deduction from the uniform bounds, not a clause of the compared fixed-$k$ statement.

The upper-bound implementation needs the [exact measured-label law][src-amplify-measured] of Lemma 2. The headline proof composes that law with verification through a Boolean continuation; a separate formal theorem supplies the candidate-list formulation. The [retained-state result][cmp-amplifier] uses an abstract opaque-preparation interface and success predicates on basis labels. Its additional physical-state correspondence is distinguished from the established label law in [Appendix G.7](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#upper-missing-physical-state).

The formal [direct-product theorem][cmp-direct-product] bounds [success together with cap compliance][def-compliant] for finitely many weighted seeds. For our truncated simulator, compliance holds on every input, so this joint-event bound becomes the unconditional success bound used in (12). The record supplies the ordinary translations from arbitrary independent randomness to finite seeds and from recursive compliance to per-input counts ([§6.1 and Appendix G.8](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-direct-product-formal)). Full statement correspondence and checking scope are in [Appendix G](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#checked-statements).

## Use of AI tools

Will Cook directed the reconstruction; AI systems drafted the text and Lean proofs and performed the recorded checks. The separation theorem, construction and original analyses are OpenAI's. Sources and proofs are in the repository [@Repo2026] and reasoning record [@Record2026].

## References

::: {#refs}
:::


## Appendix A. Simplifications that fail

The examples protect three inferences: A.1–A.3 concern construction and verification, A.4–A.7 concern independent planting and capped prediction, and A.8 concerns the optional change of parameter. They show why the hypotheses used above cannot simply be dropped. Here $\beta$ is a one-instance success bound; in the finite examples it is the exact optimum. The cap examples test the general direct-product hypotheses, including the zero-query case, rather than the final construction's large-parameter regime.

### A.1 The projection statistic does not test the promise

Take $k=2$, $m=4$ and $z_1=z_2=(-1,1,1,1)$. Then $\Phi=-1$, so $\Phi^2=1$, yet $z$ lies outside the promise. The projection experiment therefore cannot supply the domain bit required in §2 (iii). The complete calculation is in [record §3.5](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#forr_small_instance). In the Walsh ordering $00,01,10,11$, $H(-1,1,1,1)^{\mathsf T}=(1,-1,-1,-1)^{\mathsf T}$, so the quadratic product is $-4/4=-1$.

### A.2 Comparisons need not describe an order or fixed orientation

A deterministic three-cycle of losers is a fixed tournament with no total order. If two losers instead defeat each other with probability $1/2$, this comparator's output law is not bounded-error access to either fixed orientation. The tournament of §3.2 accommodates both cases because it uses the exact comparison probabilities. See [record §5.2](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#upper-cyclic-example).

### A.3 A dominant column need not win

Let column $1$ be all ones and every other column contain a zero. Give column $1$ a correct certificate except for one pointer into a column $j>1$ that reaches a one. Every rival pointer reads one in $X_1$, whatever address its decoder returns. Column $1$ defeats every rival, using the smallest-index tie-break against $j$, yet no column wins. This is why §3.3 verifies the candidate list rather than accepting a column on the strength of its comparisons.

### A.4 A uniform marginal choice need not be independent

On a dummy board with independent uniform zero positions, query row $1$ of four columns. Choose $I$ uniformly among columns whose zero was found, or among all four if none was found. Column-permutation symmetry makes the marginal law of $I$ uniform, including the no-discovery branch, but its zero was found with probability
$$
1-(3/4)^4=\frac{175}{256}>\frac{\mathbb EZ}{m}=\frac14.
$$
Thus the identity in §4.3 requires independence of $I$ from the whole dummy run. The computation is in [record §6.4](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-selection-independence-example).

### A.5 Expected caps do not give the direct-product bound

Consider two-bit parity on two independent uniformly random two-bit strings. With a cap of one query to each, the one-instance success is $\beta=1/2$. Now toss a fair coin: on one outcome read all four bits, and on the other guess both answers. The expected cost is one query per instance, but the probability of getting both answers right is
$$
\frac12+\frac12\cdot\frac14=\frac58>\beta^2.
$$
The separate caps in §4.1 must therefore hold on every branch.

### A.6 Separate independence does not imply joint independence

Let $P(x)=x$ on one fair bit and take query cap zero. For independent fair inputs $X,Y$, the side information $S=X\oplus Y$ is independent of each input separately. Given $S$, answering $(0,S)$ succeeds with probability $1/2$, although the product of the two one-instance optima is $1/4$. Lemma 5 consequently requires side information jointly independent of the entire input tuple. See [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-independent-information).

### A.7 Conditioning on compliance changes the success probability

Take independent instances $A,B$ of AND on two uniform bits. With cap one query per instance, the exact one-instance optimum is $\beta=3/4$. Query $A_0$, then $B_{A_0}$; query $A_0$ again if the answers differ; and output $(0,0)$. The redundant repeat query makes the run noncompliant exactly when the two observed bits differ. The one-query optimum is $1/2+1/4=3/4$: a zero determines AND, while after a one the unqueried fair bit must be guessed. The caps therefore hold on the two equal-answer branches, eight of the sixteen inputs, and the output is right on five of those eight: both observed bits zero gives four correct completions; both one gives only the completion with both unqueried bits zero. Hence
$$
\Pr[\text{success and compliance}]=\frac5{16}\le\beta^2,
\qquad
\Pr[\text{success}\mid\text{compliance}]=\frac58>\beta^2.
$$
The first has the joint-event form used in §4.4. Compliance in this example is distinct from terminal lightness there. Replacing it by the conditional probability invalidates the argument. The full trace is in [record §6.1](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#CL-adaptive-example).

### A.8 Fixed-parameter thresholds do not justify a growing parameter

The condition $t\ge2^k$ holds eventually for every fixed $k$, yet fails for every $t$ when $k=t$. The growing-$k$ family in §6 therefore uses the new allowance $L=\lfloor X\rfloor$ from (16) and estimates uniform in $k$; [record §7.3](https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/docs/reasoning_record.md#ROOT-GROWING-K) checks that switch. An eventual fixed-$k$ statement alone does not permit the substitution.

<!-- lean-links -->
[cmp-amplifier]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean#L17-L52
[cmp-direct-product]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean#L18-L25
[def-compliant]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticQuery/LowerBound/RealizedCaps.lean#L111-L120
[src-amplify-measured]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticQuery/Upper/Amplify.lean#L345-L352
[src-budget-exponential]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticQuery/Upper/Bound.lean#L286-L290
[src-constants]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticQuery/Paper/ConstructionFamily.lean#L28-L40
[src-forrelation-uniform]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticQuery/ForrelationLower/Uniform.lean#L525-L532
[statement-file]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Unconditional/Challenge.lean
[statement-solution]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Unconditional/Solution.lean
[thm-alpha]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Unconditional/Challenge.lean#L326
[thm-cubic]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Unconditional/Challenge.lean#L336-L338
[thm-forrelation]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Unconditional/Challenge.lean#L340
[thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/b8db5326715e5a4ce6996cde0768b92b5fcd5177/lean/QuarticCorpus/Unconditional/Challenge.lean#L328-L334
<!-- /lean-links -->
