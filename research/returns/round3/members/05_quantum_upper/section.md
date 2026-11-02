## 5. Quantum evaluation on every input


<!-- passage:upper-section-interface -->
**Scope of this replacement.** This is a replacement for §5 of the supplied long reasoning record. The mathematical result and construction are OpenAI's [OpenAI2026, §3, pp. 7–10]. The present contribution is a proof reconstruction and a correction of its formal correspondence, with an exact cyclic example. No mathematical claim of the source preprint is changed.

We use the ordinary bit oracle and the maximum-over-branches query convention of §2.2. The incoming facts from §4 are the definition of a winner at an address, uniqueness of a winner, and the equivalence between winning at that address and passing all the exact local tests. For $m=4^t$, $t\geq1$, these tests number $K=m+(m-1)+r(S+2)$, have decision-tree depth at most $\max\{3,\ell+1\}$, and use $\ell=2t=\log_2m$, $r=40t=20\ell$. The incoming partial-function ingredient from §3 is the actual bounded-query Forrelation algorithm and its error reduction, together with the fixed realizing circuit of size $S\leq C_F(k)m\ell^2$. Its correctness is promised-input correctness; its query cap holds on all inputs. We repeat the particular uses of these facts below. No future section return is assumed.

The output of this section is Proposition 3.3, with the more explicit bound $Q(F_{k,4^t})\leq C_k2^t(2t)^6$ for each fixed $k\geq2$. Every unqualified logarithm is base two; $\ln$ is natural. The constants may depend on that fixed $k$. Formal evidence is collected in §5.5 and the companion correspondence, rather than used as a substitute for the proof.
<!-- /passage:upper-section-interface -->


<a id="upper-purpose"></a>
<!-- passage:upper-purpose -->

The algorithm first produces a short list likely to contain the winning column, then checks the listed columns. Its central calculation is a drift identity: complementary comparison probabilities make the total surviving weight fall by at least half in expectation, while a true winner retains almost all its weight until it is selected. This works even if the other columns compare cyclically or have meaningless decoded addresses. Exact local verification subsequently rejects incorrect certificates. Both the search and the verification have a fixed query cap on every input, including inputs outside all the partial-function promises.

The organization into candidate generation, comparison and certificate checking also appears in Ben-David and Kothari [BDK2026, §3, Lemma 5, pp. 3–5]. Dürr and Høyer's minimum-finding algorithm uses ordered table values and a decreasing rank [DH1999, Theorem 1 and Lemmas 1–2, pp. 1–2]. Mande, Paraashar and Saurabh give a quantum algorithm for finding a king with exact edge-direction queries [MPS2023, Theorem 19, §4, pp. 30:11–30:13]. These are antecedents and comparisons; the fractional-weight argument here is the one in OpenAI's Proposition 3.2. In particular, the available comparisons need not be bounded-error evaluations of any fixed orientation.

The only complexity measure below is the number of calls to the ordinary input bit oracle. Input-independent unitaries, finite work registers, reversible arithmetic on indices and measurements are free in this measure. A bound first stated in calls to a preparation is converted explicitly to bit queries when that preparation is implemented.
<!-- /passage:upper-purpose -->


### 5.1. Amplification with a fixed stopping time


<a id="upper-amplification-statement"></a>
<!-- passage:upper-amplification-statement -->

**Lemma 3.1, with the quantifiers made explicit.** For every pair of real numbers $0<\gamma\leq 1/2$ and $0<\eta<1/2$, there is one procedure, depending on $\gamma,\eta$ and using a preparation $A$ as a black box, with the following property for every unitary $A$, every fixed input oracle, and every designated success subspace. Write $p$ for the probability that measuring $A|0\rangle$ in that subspace succeeds. The procedure returns either failure or a state. Every returned state is the normalized success component of $A|0\rangle$, up to global phase. If $p\geq\gamma$, its failure probability is at most $\eta$. If $p=0$, it fails with certainty. On every branch, for every $p\in[0,1]$, it uses $O(\gamma^{-1/2}\ln(1/\eta))$ calls to $A$ and $A^{-1}$. In particular, neither the procedure nor its stopping rule depends on knowing $p$. This is the successful-state assertion in OpenAI's Lemma 3.1; the output state refers to the designated returned register, including the original preparation's workspace.

The distinction between a fixed bound and an expected bound matters here. Boyer, Brassard, Høyer, and Tapp analyze a random number of Grover iterations when the number of solutions is unknown [BBHT1996, arXiv v1, §4, Lemma 2 and Theorem 3, pp. 3–4](https://arxiv.org/abs/quant-ph/9605034v1). Brassard, Høyer, Mosca, and Tapp extend the underlying two dimensional analysis to arbitrary preparation algorithms [BHMT2000, arXiv v1, §2, Lemma 1 and equation (8), pp. 5–7](https://arxiv.org/abs/quant-ph/0005055v1). The expected-cost searches in those sources do not by themselves give the all-branch cap needed here. We give OpenAI's bounded construction in full. BHMT's Theorem 12 concerns amplitude estimation and is not the amplification result used in this proof.
<!-- /passage:upper-amplification-statement -->

<a id="upper-grover-geometry"></a>
<!-- passage:upper-grover-geometry -->

Let $\Pi$ be the orthogonal projection onto the success subspace, let $\psi=A|0\rangle$, and let $p=\|\Pi\psi\|^2$. First suppose $0<p<1$. Define $g=\Pi\psi/\sqrt p$ and $b=(I-\Pi)\psi/\sqrt{1-p}$. Orthogonality of the two projection ranges gives orthonormal vectors $g,b$, and normalization of $\psi$ gives $\psi=\sqrt p\,g+\sqrt{1-p}\,b$. There is a unique $\theta\in(0,\pi/2)$ such that $\sin\theta=\sqrt p$. Its cosine is $\sqrt{1-p}$.

The success reflection is $S_\chi=I-2\Pi$. The reflection about the reference state is $S_0=I-2|0\rangle\langle0|$. Choose the Grover iterate $G=-AS_0A^{-1}S_\chi$. The minus sign is a global phase, so it has no query cost. Conjugating $S_0$ by $A$ gives $I-2|\psi\rangle\langle\psi|$. Consequently $G=(2|\psi\rangle\langle\psi|-I)S_\chi$. Both factors preserve the span of $g,b$. On coordinates in the ordered basis $g,b$, $S_\chi$ changes the sign of the first coordinate. Multiplying it by the reflection about $\psi$ gives the matrix with rows $(\cos(2\theta),\sin(2\theta))$ and $(-\sin(2\theta),\cos(2\theta))$.

Applying this matrix to a vector with coordinates $(\sin\alpha,\cos\alpha)$ gives $(\sin(\alpha+2\theta),\cos(\alpha+2\theta))$, by the addition formulas. Induction on the nonnegative integer $\ell$, beginning at $\alpha=\theta$, therefore proves the state and success formula in `claim-grover-state`:

<!-- claim:claim-grover-state -->
$$
G^\ell\psi
 =\sin((2\ell+1)\theta)g+\cos((2\ell+1)\theta)b,
\qquad
\Pr[\text{success after }\ell]=\sin^2((2\ell+1)\theta).
$$

Projection onto success removes the $b$ term. Whenever success has nonzero probability, the normalized result is $g$ or $-g$. This conclusion concerns the whole workspace, including registers that $A$ has used to record intermediate data. It is stronger than a statement about the probability of a success flag alone.

At $p=0$, the state lies in the failure subspace. The success reflection leaves it unchanged, and the reflection about $\psi$ leaves $\psi$ unchanged. Thus every iterate has zero success probability. At $p=1$, the success reflection sends $\psi$ to $-\psi$, and every iterate remains a scalar multiple of $\psi$ in the success subspace. These cases require no definition of a normalized zero component.
<!-- /passage:upper-grover-geometry -->

<a id="upper-grover-trial"></a>
<!-- passage:upper-grover-trial -->

For `def-grover-trial`, choose the following two integers, using natural logarithms in the second expression:

<!-- claim:def-grover-trial -->
$$
M=\left\lceil\frac{10}{\sqrt\gamma}\right\rceil,
\qquad
N=\left\lceil\frac{\ln(1/\eta)}{\ln(40/31)}\right\rceil.
$$

In one trial, set $\ell=0$ with probability $1/2$; with the remaining probability $1/2$, choose $\ell$ uniformly from $0,\ldots,M-1$. Prepare $\psi$, apply $G^\ell$, and measure success. Run at most $N$ such trials on fresh initialized registers, stopping at the first success. Return failure if none succeeds. Equivalently, the probability assigned to an iteration count $\ell<M$ is $1/(2M)$, with an additional $1/2$ assigned to zero. This is a finite distribution selected before any access to the input.

One preparation followed by $\ell$ iterates uses $2\ell+1$ calls to $A$ or $A^{-1}$. The elementary reflections $S_0$ and $S_\chi$ contribute no additional calls to $A$ or $A^{-1}$. Since $\ell<M$, the actual count in a trial is at most $2M-1$; the formal construction uses the convenient upper bound $2M+1$. Stopping after $N$ trials therefore gives a syntactic cap independently of the input and of the outcomes. We have not used a success assumption to establish this cap.
<!-- /passage:upper-grover-trial -->

<a id="upper-average-exact"></a>
<!-- passage:upper-average-exact -->

The randomized iteration count is controlled by the exact averaging identity of BBHT [BBHT1996, §4, Lemma 2, p. 3]. It strengthens the inequality in OpenAI's equation (9):

<!-- claim:new-upper-average-exact -->
$$
\frac1M\sum_{\ell=0}^{M-1}\sin^2((2\ell+1)\theta)
 =\frac12-\frac{\sin(4M\theta)}{4M\sin(2\theta)}
 \quad(M\geq1,\ \sin(2\theta)\ne0).
$$

To prove it, use $\sin^2 u=(1-\cos(2u))/2$. The difference between $\sin(4(\ell+1)\theta)$ and $\sin(4\ell\theta)$ is $2\sin(2\theta)\cos((4\ell+2)\theta)$. Summing this equality over $\ell=0,\ldots,M-1$ cancels every interior sine term and leaves $\sin(4M\theta)$. Dividing by the nonzero $2\sin(2\theta)$ gives the sum of the cosine terms. Substituting into the sum of the squared sines and dividing by $M$ proves the identity. Multiplication by $\sin(2\theta)$ gives an identity without division, valid also at the endpoints; the displayed quotient is used only when its denominator is nonzero.
<!-- /passage:upper-average-exact -->

<a id="upper-small-probability"></a>
<!-- passage:upper-small-probability -->

Suppose now that $\gamma\leq p\leq1/2$. The sine addition formula and the definitions of $\theta,g,b$ give `claim-sin2theta`:

<!-- claim:claim-sin2theta -->
$$
\sin(2\theta)=2\sqrt{p(1-p)}\geq\sqrt\gamma.
$$

Indeed, $1-p\geq1/2$, so the square of the left side is $4p(1-p)\geq2p\geq\gamma$; both sides are nonnegative. Since $M\geq10/\sqrt\gamma$, we obtain $M\sin(2\theta)\geq10$. The absolute value of every sine is at most one. The exact average above therefore implies the paper's slightly weaker, and sufficient, equation (9):

<!-- claim:eq-9 -->
$$
\frac1M\sum_{\ell=0}^{M-1}\sin^2((2\ell+1)\theta)
\geq\frac12-\frac{1}{2M|\sin(2\theta)|}
\geq\frac9{20}.
$$

The half of the trial that chooses a uniform iteration count thus contributes at least $9/40$ to its success probability. If instead $p\geq1/2$, the half that chooses zero iterations contributes at least $p/2\geq1/4\geq9/40$. These cases cover every $p\geq\gamma$, including $p=1$. A trial fails with probability at most $31/40$ whenever the promise $p\geq\gamma$ holds.
<!-- /passage:upper-small-probability -->

<a id="upper-amplification-proof"></a>
<!-- passage:upper-amplification-proof -->

For a fixed oracle input, each fresh trial has the same failure probability $f$, and the fresh choices and registers make the failures independent. Hence the probability of $N$ failures is $f^N\leq(31/40)^N\leq\eta$. The last inequality follows by taking logarithms: $N\ln(40/31)\geq\ln(1/\eta)$. If $p=0$, the endpoint argument above gives $f=1$, hence certain failure.

On a successful branch, the state in its successful trial is $g$ up to global phase, regardless of its iteration count. Earlier failed trials occupy separate registers and can be discarded after their outcomes have been recorded. Keeping them also causes no problem: the designated output register is in the pure state $g$ up to phase. Taking a mixture over iteration counts and over which trial first succeeded leaves the density operator $|g\rangle\langle g|$ unchanged. Thus conditioning on success does not bias any measurement of that output state. This proves every correctness clause of Lemma 3.1.

The padded product charged by the implementation itself satisfies the following bound:

<!-- claim:new-upper-call-cap -->
$$
\operatorname{calls}(\gamma,\eta)
\leq N(2M+1)
\leq138\,\gamma^{-1/2}\ln(1/\eta).
$$

Here is the arithmetic. For $x\geq1$, differentiating $\ln x-2(x-1)/(x+1)$ gives $(x-1)^2/(x(x+1)^2)\geq0$, and the expression vanishes at one. At $x=40/31$, this gives $\ln(40/31)\geq18/71\geq1/4$. Also $\ln2=\int_1^2u^{-1}\,du\geq1/2$. Consequently $N\leq4\ln(1/\eta)+1\leq6\ln(1/\eta)$. Since $M\leq10/\sqrt\gamma+1$ and $\sqrt\gamma\leq1$, we have $2M+1\leq23/\sqrt\gamma$. Multiplication gives 138. These estimates are deliberately uniform; there is no run that is allowed to exceed the bound because its success probability happens to be small.

A positive original success probability also makes conditioning legitimate: the zero-iteration half of each trial succeeds with probability at least $p/2>0$, and $N\geq1$. Thus the total success probability is positive whenever $p>0$. At $p=0$ we assert certain failure and make no conditional-state assertion on a null event.
<!-- /passage:upper-amplification-proof -->

<a id="upper-returned-register"></a>
<!-- passage:upper-returned-register -->
The retained registers deserve a precise interpretation. On a successful measured history, route the first successful trial's entire original register to a fixed output register. Its state is $g$ up to phase. Earlier unsuccessful registers, iteration-count records and the chosen trial index are additional registers. Keeping all of them does not change the output register's pure reduced state $|g\rangle\langle g|$. If the history is retained coherently, the phase of each history can be absorbed into its auxiliary amplitude: after the fixed routing, the unnormalized successful component factors as $g\otimes\xi$, with $\|\xi\|^2$ equal to the success probability. This is a statement about a designated subsystem; it does not identify the whole enlarged workspace with the smaller vector $g$.

A coherent implementation may run all $N$ trial registers and then route the first success, which keeps the same padded cap. It needs no controlled access to an otherwise opaque preparation unitary. To control a Grover iterate, apply $A$ and $A^{-1}$ unconditionally, control only the fixed reflections $S_0,S_\chi$, and apply the minus sign as a phase on the true control. On a false control the reflections are identities and $AA^{-1}=I$; on a true control the operation is $G$. The iteration-count record therefore controls only input-independent gates. Every trial has a fixed schedule of preparation calls, and its success projection can be recorded coherently in an auxiliary flag. After routing, the common factor $g$ on every successful history gives the stated factorization. In particular, the first trial alone gives total success probability at least $p/2$ when $p>0$.

<!-- claim:r3-q-labels-do-not-determine-state -->
Equality of label distributions alone would be insufficient. Write $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$. The vectors
$$
 |+\rangle\otimes|0\rangle
 \quad\hbox{and}\quad
 \frac{|0\rangle|0\rangle+|1\rangle|1\rangle}{\sqrt2}
$$
give the same uniform computational-basis distribution on the first register. In the first vector that register is pure $|+\rangle$; in the second it has density matrix $I/2$. Measuring it in the $\{|+\rangle,|-\rangle\}$ basis distinguishes the two laws: the probability of $+$ is respectively $1$ and $1/2$. This elementary example explains why the formal successful-label theorem cannot by itself certify the full successful-state assertion. It does not contradict the ordinary proof of Lemma 3.1 just given.
<!-- /passage:upper-returned-register -->


### 5.2. A tournament with probabilistic comparisons


<a id="upper-comparison-model"></a>
<!-- passage:upper-comparison-model -->

Fix an input oracle for the duration of the argument. There are $m\geq2$ vertices. For each unordered pair of distinct vertices, use one designated coherent comparison circuit. An ordering convention determines which output bit means that the first named vertex wins. Let $a_{ij}$ be the probability that $i$ wins its comparison against $j$, and define $a_{ii}=0$. This is `def-aij`. The same circuit and opposite interpretations of its two outcomes give equation (10):

<!-- claim:eq-10 -->
$$
0\leq a_{ij}\leq1,
\qquad a_{ij}+a_{ji}=1\quad(i\ne j),
\qquad a_{ii}=0.
$$

No transitivity condition is imposed. Comparisons made in separate fresh registers have their designated probabilities, but the numbers need not be close to zero or one. A cycle of certain wins is allowed, as is a pair with winning probability exactly one half. In the algorithmic theorem, all pair circuits are available coherently, including under control of their indices, with a uniform cap of $c\geq1$ bit queries per comparison and the same cap for its inverse. When a controlled query is implemented from an ordinary bit query, the constant overhead established below is included in $c$.
<!-- /passage:upper-comparison-model -->

<a id="upper-bounded-error-comparison"></a>
<!-- passage:upper-bounded-error-comparison -->
Høyer, Mosca and de Wolf [HMW2003, arXiv v2, §1, pp. 1–3, and §3, pp. 4–7] study search when each underlying Boolean predicate is computed correctly with probability at least $9/10$. Their result is relevant background on searching with imperfect subroutines. An arbitrary loser–loser comparison here need not satisfy such a correctness guarantee for either orientation: its probability may be $1/2$, or arbitrarily close to $1/2$. That result therefore does not directly turn these comparisons into a fixed tournament oracle. We will use the comparison probabilities themselves. The final search, once an address has been fixed, has exact Boolean tests.
<!-- /passage:upper-bounded-error-comparison -->


<a id="upper-tournament-parameters"></a>
<!-- passage:upper-tournament-parameters -->

For `def-T-eps`, put

<!-- claim:def-T-eps -->
$$
T=\left\lceil\log_2(1000m)\right\rceil,
\qquad \varepsilon=\frac{1}{1000T}.
$$

The base of the logarithm is part of the definition. In particular, $2^T\geq1000m$. Call a vertex $s$ dominant if it satisfies equation (11):

<!-- claim:eq-11 -->
$$
a_{sj}\geq1-\varepsilon\qquad(j\ne s).
$$

The theorem below is conditional on this property of $s$. Its algorithm has no such promise: it runs and obeys its query cap for every comparison table satisfying equation (10). The property is only used to prove that a particular vertex is likely to occur in the returned list.
<!-- /passage:upper-tournament-parameters -->

<a id="upper-ideal-process"></a>
<!-- passage:upper-ideal-process -->

Begin with weights $w_i=1$ and an empty ordered list $L$. Write $W=\sum_iw_i$. In one ideal step, if $W>0$, choose a pivot $p$ with probability $w_p/W$, append it to $L$, and make the update in equation (12):

<!-- claim:eq-12 -->
$$
w_i\longleftarrow w_i a_{ip}\qquad(1\leq i\leq m).
$$

If $W=0$, leave the weights zero and append nothing. Run exactly $T$ steps, with this zero state absorbing. This specifies `def-ideal-process` on every history. All weights remain nonnegative and at most one, because they are products of numbers in $[0,1]$. After a history $p_1,\ldots,p_t$, the weight of $i$ is the product of $a_{ip_b}$ over $b\leq t$. A selected vertex receives the factor $a_{pp}=0$, so it has zero weight thereafter and cannot be selected again on a positive-weight step. These observations also describe what happens at histories of probability zero without requiring division by zero.
<!-- /passage:upper-ideal-process -->

<a id="upper-weight-drift"></a>
<!-- passage:upper-weight-drift -->

Condition on any current weights with $W>0$. For pivot $p$, the new total weight is $\sum_iw_ia_{ip}$. Averaging over its probability $w_p/W$ gives the first expression in equation (13). To evaluate its numerator, write it as the sum over ordered pairs $(i,p)$. The diagonal terms vanish because $a_{ii}=0$. Pairing the term for $(i,p)$ with the term for $(p,i)$, for each unordered pair with $i\ne p$, gives $w_iw_p(a_{ip}+a_{pi})=w_iw_p$. The sum of the $w_iw_p$ over unordered pairs is half of $W^2-\sum_iw_i^2$. Therefore

<!-- claim:eq-13 -->
$$
\mathbb E[W_{\rm new}\mid w]
 =\frac1W\sum_{p,i}w_pw_i a_{ip}
 =\frac{W^2-\sum_iw_i^2}{2W}
 \leq\frac W2.
$$

At $W=0$ both the current and next total weights are zero, so the last inequality still holds. Taking expectations over histories gives $\mathbb E W_{t+1}\leq\tfrac12\mathbb E W_t$. Starting from $W_0=m$ and applying this inequality $T$ times proves `claim-expected-WT`:

<!-- claim:claim-expected-WT -->
$$
\mathbb E W_T\leq\frac{m}{2^T}.
$$

This calculation uses only complementary probabilities and nonnegativity. It applies equally to deterministic tournaments, cyclic tournaments, and comparisons whose probabilities are bounded away from both zero and one.
<!-- /passage:upper-weight-drift -->

<a id="upper-dominant-weight"></a>
<!-- passage:upper-dominant-weight -->

Suppose $s$ is dominant and has not appeared among the first $t\leq T$ pivots. Every factor contributing to its weight is then at least $1-\varepsilon$, so `claim-weight-lb` is

<!-- claim:claim-weight-lb -->
$$
w_s(t)\geq(1-\varepsilon)^t
\geq1-t\varepsilon
\geq1-T\varepsilon
=\frac{999}{1000}>\frac12.
$$

The middle inequality follows by induction on $t$. At $t=0$ it is equality. Multiplying the bound at $t$ by $1-\varepsilon\geq0$ gives $1-(t+1)\varepsilon+t\varepsilon^2\geq1-(t+1)\varepsilon$. Thus, until $s$ is selected, the total weight is positive and exceeds one half. In particular, an absorbing zero state cannot be reached before selecting $s$.

If $s$ is missing from the ideal list at time $T$, the same argument gives $W_T>1/2$. The indicator of this event is at most $2W_T$ pointwise. Taking expectations proves equation (14), without any separate regularity assumption on the weight distribution:

<!-- claim:eq-14 -->
$$
\Pr[s\notin L_T]
\leq\Pr[W_T\geq1/2]
\leq2\,\mathbb EW_T
\leq\frac{2m}{2^T}.
$$

The conclusion uses only complementarity and the lower bounds on the distinguished row. No comparison between two other candidates needs to be consistent with an ordering.
<!-- /passage:upper-dominant-weight -->

<a id="upper-stage-state"></a>
<!-- passage:upper-stage-state -->

We now implement a quantum version of one step. Fix the current classical pivot list $p_1,\ldots,p_t$. Prepare a uniform index $i\in[m]$, and, controlled by $i$, run a fresh copy of the comparison with $p_b$, for every $b\leq t$. Let $|\phi(i,p_b)\rangle$ denote the full normalized state of that copy, including its outcome bit and all workspace. For a self-comparison, set the outcome bit to false without querying the oracle. The prepared state is equation (15):

<!-- claim:eq-15 -->
$$
\frac1{\sqrt m}\sum_{i=1}^m |i\rangle
 \bigotimes_{b=1}^{t}|\phi(i,p_b)\rangle.
$$

The empty tensor product at $t=0$ is a one dimensional state. Reversibly compute an additional success bit that is true precisely when every comparison outcome says that $i$ won. Keep the individual outcomes and all the work registers. The preparation is a unitary, and its inverse reverses the comparisons and the success computation.
<!-- /passage:upper-stage-state -->

<a id="upper-stage-law"></a>
<!-- passage:upper-stage-law -->

For fixed $i$, the different comparisons act on separate initially fixed registers. Projection onto all successful outcome bits is a tensor product of their success projections. Its squared norm is therefore the product of their squared norms, namely the product of $a_{ip_b}$, which is $w_i$. Distinct index values remain orthogonal. Summing their squared norms and remembering the initial factor $1/\sqrt m$ proves `claim-success-prob`:

<!-- claim:claim-success-prob -->
$$
\Pr[\text{success and index }i]=\frac{w_i}{m},
\qquad
\Pr[\text{success}]=\frac Wm,
\qquad
\Pr[i\mid\text{success}]=\frac{w_i}{W}\quad(W>0).
$$

There is no interference between different decoded outcomes hidden inside a comparison: its outcome probability already includes its entire retained workspace. There is also no assumption that different pairs share a common deterministic orientation. What is multiplied here is the success probability of distinct, fresh uses of their specified circuits at one fixed oracle input.
<!-- /passage:upper-stage-law -->

<!-- passage:upper-cyclic-example -->
**An exact four-candidate example.** <!-- claim:r3-q-cyclic-example --> Let the candidates be $s,a,b,c$.
Here $T=\lceil\log_2(4000)\rceil=12$ and
$\varepsilon=1/12000$. The entry in row $i$, column $j$ of the
following table is the probability that $i$ defeats $j$.

| $a_{ij}$ | $s$ | $a$ | $b$ | $c$ |
|---|---:|---:|---:|---:|
| $s$ | $0$ | $1-\varepsilon$ | $1-\varepsilon$ | $1-\varepsilon$ |
| $a$ | $\varepsilon$ | $0$ | $1$ | $0$ |
| $b$ | $\varepsilon$ | $0$ | $0$ | $1$ |
| $c$ | $\varepsilon$ | $1$ | $0$ | $0$ |

The candidate $s$ is dominant, while the other three have the cycle
$a$ defeats $b$, $b$ defeats $c$, and $c$ defeats $a$.
There is no total ordering consistent with these three certain comparisons.

Suppose the first pivot is $a$. The weights become
$$
 (w_s,w_a,w_b,w_c)=(11999/12000,0,0,1),
 \qquad W=23999/12000.
$$
The unamplified preparation succeeds with probability
$W/4=23999/48000$. Conditioned on success, the next pivot is
$s$ with probability $11999/23999$ and $c$ with probability
$12000/23999$. Bounded amplification changes the probability of obtaining
a sample, while preserving these two conditional probabilities exactly.
If the next pivot is $c$, the only remaining positive weight is
$w_s=(11999/12000)^2$, so the following successful sample is $s$.

The first-step total weight is $3\varepsilon$ if the pivot is $s$,
and $2-\varepsilon$ for each of the other three pivots. Since the first
pivot is uniform, its expected value is
$$
 \frac{3\varepsilon+3(2-\varepsilon)}4=\frac32
 =\frac{4^2-4}{2\cdot4}.
$$
This is the exact drift identity in a cyclic example. The ideal process selects
$s$ within three pivots with probability one. The example illustrates the
weight calculation and conditional law; it is neither a construction of the
full addressed-certificate input nor a proof of the general tournament bound.
<!-- /passage:upper-cyclic-example -->


<a id="upper-quantum-tournament"></a>
<!-- passage:upper-quantum-tournament -->

Apply Lemma 3.1 to this preparation with $\gamma=1/(2m)$ and $\eta=\varepsilon$. On reported failure, stop and return the current list. On success, measure the index, append it to the list, and proceed. Stop after at most $T$ appended indices. These instructions define `construct-sampler` for every input and every history, whether or not a dominant vertex exists.

Conditioned on success, the amplified state is the normalized success component of the unamplified preparation. Measuring its index consequently has exactly the distribution $w_i/W$. This exact conditional law is essential: a mere lower bound on the chance of obtaining some successful index would not justify the ideal weight calculation. When $W=0$, the unamplified success probability is zero, and Lemma 3.1 reports failure with certainty.

The compiled version uses a useful finite-label statement. Let $q_x(b)$ be the unamplified probability of a successful label $b$, and put $q_x=\sum_bq_x(b)$. There is a failure probability $f_x\in[0,1]$ such that the output law has the following form, recorded as `new-upper-sampler-law`:

<!-- claim:new-upper-sampler-law -->
$$
\Pr[\bot]=f_x,
\qquad
\Pr[b]=(1-f_x)\frac{q_x(b)}{q_x}\quad(q_x>0),
\qquad
q_x\geq\gamma\Longrightarrow f_x\leq\eta,
\qquad
q_x=0\Longrightarrow f_x=1.
$$

This follows from the phase-independent successful-state assertion, followed by measurement of the label. For $q_x>0$ and $f_x<1$, the successful mass is $1-f_x>0$, so division by it gives the conditional law $q_x(b)/q_x$. These are the hypotheses for interpreting the ratio as a conditional probability. For the bounded procedure above, $p>0$ implies $f_x<1$; in the tournament, the stronger bound $f_x\leq\varepsilon<1$ holds at every history before the dominant vertex has been selected. At $q_x=0$, the only output is failure. No conditional law is assigned to that event. Substituting $q_x(i)=w_i/m$ gives the ideal pivot law whenever it is used.
<!-- /passage:upper-quantum-tournament -->

<a id="upper-coupling"></a>
<!-- passage:upper-coupling -->

We compare the real process with the ideal one on a common probability space. As long as their lists agree, let $f(L)$ be the failure probability of the amplified sampler for that list. If $W>0$, independently choose a possible ideal next pivot with distribution $w_i/W$, and a Bernoulli variable that reports failure with probability $f(L)$. On nonfailure, give both processes the chosen pivot. On failure, stop the real process and continue the ideal one with its ordinary transitions. This has the correct marginal distribution for each process: the real sampler's successful probability for pivot $i$ is exactly $(1-f(L))w_i/W$. Independence here is a way to construct the coupling from that law; it is not an additional property demanded of the implementation.

Suppose $s$ is dominant. At an agreed history of length at most $T$ before $s$ is selected, the preceding lower bound gives $W>1/2$. Thus $W/m\geq1/(2m)$, and $f(L)\leq\varepsilon$. For each of the at most $T$ stages, condition on the event that there has been no earlier disagreement and $s$ has not yet appeared. The conditional chance of a new disagreement is at most $\varepsilon$. Multiplying by the probability of the conditioning event and summing over the stages gives a total at most $T\varepsilon$. No independence among these stage failures is needed.

If the ideal process selects $s$ and there has been no disagreement before that selection, the real list already contains $s$. A later failure cannot remove a previous entry. Consequently the real miss event is contained in the union of the ideal miss event and a disagreement before selecting $s$. Equation (14) proves `claim-coupling`:

<!-- claim:claim-coupling -->
$$
\Pr[\text{the real list misses }s]
\leq\frac{2m}{2^T}+T\varepsilon.
$$

This argument deliberately stops charging failures after $s$ has appeared. At those later histories the total weight can be arbitrarily small, and the sampler need not have failure probability at most $\varepsilon$. The claim only needs the already recorded occurrence of $s$.
<!-- /passage:upper-coupling -->

<a id="upper-tournament-cost"></a>
<!-- passage:upper-tournament-cost -->

At history length $t$, the state preparation uses $t$ controlled comparison circuits; the uniform superposition and the success conjunction are input independent. Its query cost and that of its inverse are at most a constant times $c(t+1)$. Lemma 3.1 uses at most a constant times $\sqrt m\ln(1/\varepsilon)$ calls to these preparations. The explicit limits on trials and iterations apply even when the success probability is below $1/(2m)$. Summing the costs for $t=0,\ldots,T-1$, and using $\sum_{t=0}^{T-1}(t+1)=T(T+1)/2$, gives `claim-tournament-cost`:

<!-- claim:claim-tournament-cost -->
$$
\text{queries}
=O\!\left(c\sqrt m\,T^2\ln(1/\varepsilon)\right)
=O\!\left(c\sqrt m\,T^2\log T\right).
$$

The second equality uses $1/\varepsilon=1000T$ and $T\geq1$, indeed $T\geq11$ when $m\geq2$. The constants are absolute. Early stopping can only reduce this cost. This proves Proposition 3.2: uniformly for every family of coherently available comparison circuits satisfying the stated cap, one algorithm returns a list of at most $T$ vertices, has the displayed query cap on every input, and contains every specified dominant vertex $s$ with probability at least $1-2m/2^T-T\varepsilon$. No estimate of the $a_{ij}$'s is required.
<!-- /passage:upper-tournament-cost -->

<a id="upper-padded-tournament-budget"></a>
<!-- passage:upper-padded-tournament-budget -->
For the exact compiled accounting, let $c_{\mathrm{rd}}$ be the number of logical reads in a comparison, let $M_0=\lceil10\sqrt{2m}\rceil$, and retain $N=\lceil\ln(1/\varepsilon)/\ln(40/31)\rceil$. The compiler uses two physical bit queries per logical read. Padding every stage to $T$ comparisons therefore gives
<!-- claim:r2-quantum-tournament-budget-6072 -->
$$
 B_{\mathrm{list}}
 =2T^2c_{\mathrm{rd}}N(2M_0+1)
 \leq6072\,c_{\mathrm{rd}}\sqrt m\,T^2\ln T.
$$
Indeed the padded-product bound above gives the intermediate upper bound

$$
 276\,c_{\mathrm{rd}}\sqrt{2m}\,T^2\ln(1000T).
$$
Since $T\geq2$, $\ln(1000T)\leq11\ln T$, using $1000\leq2^{10}$, and $\sqrt{2m}\leq2\sqrt m$. Multiplying the constants gives $276\cdot2\cdot11=6072$. This estimate bounds the actual padded product, rather than inferring a bound on that product from a smaller procedure's call count. If a comparison is initially given with $c$ ordinary bit queries, each such query is one logical read in this representation, so the same bound with $c_{\mathrm{rd}}=c$ proves the order asserted in Proposition 3.2. For the concrete construction below, logical-read and physical-query counts are kept separate.
<!-- /passage:upper-padded-tournament-budget -->


<a id="upper-tournament-evidence"></a>
<!-- passage:upper-tournament-evidence -->

The list guarantee can also be expressed as a probability law on the finite set
$$
 \mathcal L_T=\{L:\ L\text{ is a list of candidates and }|L|\leq T\}.
$$
<!-- claim:r2-quantum-coherent-list-witness -->
There is one input-independent bounded sampler, with output law $\lambda_x$ on $\mathcal L_T$, such that for every input $x$, $\lambda_x(L)\geq0$, $\sum_L\lambda_x(L)=1$, and, for every dominant $s$,
$$
 \sum_{L:\,s\in L}\lambda_x(L)
 \geq1-\frac{2m}{2^T}-T\varepsilon.
$$
The sampler is chosen before both $x$ and $s$. It does not need to know which vertex is dominant. An indicator of membership of a particular $s$ is used only in the analysis. The current formal list theorem has precisely this order of quantifiers. The older Boolean continuation, useful for final verification, is a separate implementation of the same search idea; its additional verifier error is explained next.
<!-- /passage:upper-tournament-evidence -->

<a id="upper-continuation-induction"></a>
<!-- passage:upper-continuation-induction -->

We give the induction used by that Boolean continuation, so the difference in its statement also has a complete mathematical explanation. Fix verifier acceptance probabilities $v(i)\in[0,1]$, and let $V(L)$ be the probability that at least one fresh verification of a member of $L$ accepts. Sequential verification gives $V([])=0$ and $V(i::L)=v(i)+(1-v(i))V(L)$. In particular $0\leq V(L)\leq1$; if $s\in L$, then $V(L)\geq v(s)$; and if all $v(i)\leq\varepsilon$, then $V(L)\leq|L|\varepsilon$. Each assertion follows by induction on the list using the recursive rule, or equivalently by the union bound for the verifier outcomes.

Let $R_n(L)$ be the acceptance probability with $n$ tournament stages still available after history $L$. With no stage remaining it is $V(L)$. With a stage remaining, it is the sum of $f(L)V(L)$, representing immediate sampler failure and verification of the present list, and $(1-f(L))\sum_i(w_i/W)R_{n-1}(i::L)$, representing a successful pivot and continuation. When $W=0$, set the weighted sum to zero; the guaranteed $f(L)=1$ makes the same formula correct. For positive $W$, the weights in that sum are nonnegative and sum to one. It follows inductively that $R_n(L)\in[0,1]$. If all $v(i)\leq\varepsilon$, the same recursion gives $R_n(L)\leq(|L|+n)\varepsilon$: an immediate stop has bound $|L|\varepsilon$, and each successful successor has bound $(|L|+1+n-1)\varepsilon$. A convex combination preserves the larger bound.

For the lower bound, let $I_n(L)$ be the probability that $s$ is absent after $n$ further ideal stages. Suppose $0\leq\varepsilon\leq1$, $s$ is dominant, $v(s)\geq1-\varepsilon$, and a total horizon $T_0$ satisfies $T_0\varepsilon<1/2$. Suppose also that $f(L)\leq\varepsilon$ for every history of length at most $T_0$ missing $s$, and $f(L)=1$ whenever $W=0$. The exact inductive assertion, recorded as `new-upper-continuation-bound`, is

<!-- claim:new-upper-continuation-bound -->
$$
R_n(L)\geq(1-\varepsilon)\bigl(1-I_n(L)-n\varepsilon\bigr)
\qquad(|L|+n\leq T_0).
$$

At $n=0$, if $s$ is in $L$, the right side is $1-\varepsilon$, which is at most $V(L)$. Otherwise $I_0(L)=1$ and the right side is zero. For a positive number of stages, a history already containing $s$ continues to contain it after every pivot and at every stopping point. Induction in the recursion therefore gives $R_n(L)\geq v(s)\geq1-\varepsilon$, which suffices because the right side is at most $1-\varepsilon$.

For a history missing $s$, its dominant weight is at least $1-|L|\varepsilon>1/2$, so $W>0$. The ideal miss probability is the weighted mean of the successor miss probabilities. Averaging the inductive lower bounds at successors gives a lower bound $Q=(1-\varepsilon)(1-I_n(L)-(n-1)\varepsilon)$ for the successful continuation. The immediate-stop term is nonnegative, so $R_n(L)\geq(1-f(L))Q$. We always have $Q\leq1-\varepsilon$, even when $Q$ is negative. If $Q\geq0$, then $f(L)Q\leq\varepsilon(1-\varepsilon)$; if $Q<0$, then $f(L)Q\leq0\leq\varepsilon(1-\varepsilon)$. Subtracting this upper bound from $Q$ yields exactly the desired lower bound with $n\varepsilon$. This proves the induction without assuming that failure probabilities at different histories are equal or independent.

At the empty history with $n=T_0=T$, the ideal estimate gives $I_T([])\leq2m/2^T$. Expanding the product in the lower bound and discarding its nonnegative cross term gives $R_T([])\geq1-2m/2^T-T\varepsilon-\varepsilon$. This is the acceptance guarantee in `QuarticQuery.Upper.tournament_runs`, and it accounts for its additional verifier error. For a list-membership event, use the perfect indicator $v(i)=\mathbf1_{\{i=s\}}$ only in this analysis. The same induction starts from $1-I_0(L)$ and has no factor $1-\varepsilon$, yielding $1-I_n(L)-n\varepsilon$. It therefore gives the list guarantee without an extra verifier error. This analytical choice is not an oracle supplied to the sampler.
<!-- /passage:upper-continuation-induction -->


### 5.3. Decoding, comparison, and verification


<a id="upper-decode"></a>
<!-- passage:upper-decode -->

Return to the total function $F_{k,m}$. Fix $k\geq2$ and $m=4^t$ with $t\geq1$. As in the construction, write $\ell=2t=\log_2m$ and $r=40t=20\ell$. A column has $r$ Forrelation instances whose promised values, when all are defined, form its address. The circuit used for the construction has size $S=O_k(m\ell^2)$. We use the same $T,\varepsilon$ as above.

For `def-decode`, run the quantum algorithm from Lemma 2.1(ii) on each of the $r$ Forrelation instances in the selected column, reducing the error on each promised instance to at most $\varepsilon/r$. Implement its trials and decision rule reversibly, retaining the outcome labels and all intermediate work. Its output register always contains an $r$-bit string; when some promises fail this string has no stipulated relation to a semantic address. The number of queries is nevertheless capped on every input. There is no loop that waits for a promise to become true.
<!-- /passage:upper-decode -->

<a id="upper-decode-cost"></a>
<!-- passage:upper-decode-cost -->

For fixed $k$, an instance can be decoded with $O_k(\ln(r/\varepsilon))$ queries. Running the $r$ copies gives `claim-decode-cost`:

<!-- claim:claim-decode-cost -->
$$
\text{address-decoding queries}
=O_k\!\left(r\ln(r/\varepsilon)\right),
\qquad
\Pr[\text{correct address}]\geq1-\varepsilon
\quad\text{if all }r\text{ promises hold}.
$$

To prove the probability assertion, let $E_h$ be the error event for instance $h$. For promised instances, $\Pr(E_h)\leq\varepsilon/r$. The event that the address is wrong is the union of these $r$ events, whose probability is at most their sum, $\varepsilon$. This union bound does not require independence. In the source implementation the copies are fresh, so the law of the address string is more specifically the product of their Boolean output laws.

The source uses a threshold on a retained count of Forrelation outcomes. If $\delta=2^{-5k}$, its repetition count is $n=\lceil16\delta^{-2}\ln(r/\varepsilon)\rceil$, using the natural ceiling in `QuarticQuery.Forrelation.repetitions`. Each repetition has $k$ abstract reads, so the address circuit has $rnk$ such reads. This is the same error-reduction purpose as in the paper; the count and threshold remain in the workspace. The declared address labels remain available throughout the later controlled computations, which is what makes their probability analysis valid.
<!-- /passage:upper-decode-cost -->

<a id="upper-comparator"></a>
<!-- passage:upper-comparator -->

For `def-comparison`, fix a numerical ordering of the columns. On a distinct pair, first place its smaller index first, so that both ordered calls use the same underlying circuit. Decode both addresses with fresh work registers. At the decoded address of the first column, read the pointer directed toward the second column and then the addressed entry of the second column's $X$-block. If that entry is zero, declare the second column disqualified. Do the reverse operation using the second decoded address to test whether the first column is disqualified. If exactly one is disqualified, the other wins. If both or neither are disqualified, the smaller column wins. A self-comparison always returns false and makes no pointer query.

Reading a pointer requires its $\ell$ address bits, followed by the targeted $X$-bit. Reversible reading keeps the pointer and the target address available for uncomputation. Thus the two pointer tests use $O(\ell+1)$ bit queries, with a constant factor if controlled reads are needed. Together with the two decodings, a comparison and its inverse have query cost $c=O_k(r\ln(r/\varepsilon)+\ell)= (\log m)^{O_k(1)}$. The circuit is defined on all input strings. Reversing its gate sequence gives its inverse with the same number of queries because the bit oracle is its own inverse.
<!-- /passage:upper-comparator -->

<a id="upper-comparison-law"></a>
<!-- passage:upper-comparison-law -->

For `claim-comparison-state`, we check why the coherent calculation has the probabilities suggested by the classical description. After decoding, write the state as a sum over the two decoded labels, with every summand carrying those labels in dedicated retained registers. The subsequent pointer tests and winner computation are controlled by these labels and do not erase them. The final projection onto a winning output is block diagonal with respect to the retained labels. Thus the squared norm of that projection is the sum, over label pairs, of the squared norms of the corresponding projected summands. Cross terms vanish because distinct labels are orthogonal. Within one summand, the pointer test exactly reads the designated bits. Its contribution is therefore the decoding probability of those labels multiplied by the deterministic result of the comparison rule at those labels.

The result is precisely a classical mixture over the decoded labels. Retaining extra work within a label block changes neither this orthogonality nor the rule. Controlled subsequent computations are a direct sum of unitaries on these label blocks. The two possible winners exhaust the outcomes for each distinct unordered pair. Reversing the names of the pair merely complements which event is counted. Hence $a_{ij}+a_{ji}=1$, while the self-comparison gives $a_{ii}=0$. This proves the hypotheses used in equation (10), even when neither decoded address is promised to be meaningful.
<!-- /passage:upper-comparison-law -->

<a id="upper-winner-dominates"></a>
<!-- passage:upper-winner-dominates -->

Suppose now that $i^\star$ is a winning column. Its $X$-block consists entirely of ones, by the definition of a winner. A pointer from any opponent, at any decoded address, therefore cannot find a zero in that block. Thus $i^\star$ is never disqualified. This statement is unconditional on the opponent's promises and on the opponent's decoded label.

The winner's own Forrelation promises hold, and its correct decoded address occurs with probability at least $1-\varepsilon$. At that address, its pointer into each other column finds a zero, again by the definition of a winner. Whenever its decoding is correct, every opponent in the comparison is consequently disqualified and $i^\star$ wins, regardless of the numerical tie convention. Correct decoding is thus a subset of the event that it wins. We obtain `claim-winner-dominates`:

<!-- claim:claim-winner-dominates -->
$$
a_{i^\star j}\geq1-\varepsilon\qquad(j\ne i^\star).
$$

This proof uses no correctness assertion for a nonwinning column's decoder. It also explains why independently amplifying an assumed comparison bias would have been unjustified: the available guarantee is a strong one-sided property of a true winner, while other pairs may have arbitrary probabilities. Only the true winner's decoder correctness is used. The two deterministic facts are that it cannot be disqualified and that its true-address pointers disqualify every opponent.
<!-- /passage:upper-winner-dominates -->

<a id="upper-verifier"></a>
<!-- passage:upper-verifier -->

For `def-verify`, use a fresh address decoding for the candidate column and measure its decoded address. Fix the resulting address $a$. Lemma 2.2 provides a finite list of exact local tests. Their number is

<!-- claim:def-K -->
$$
K=m+(m-1)+r(S+2)=O_k(m\ell^3).
$$

The first $m$ tests check that the candidate's $X$-block is all ones. The next $m-1$ tests follow its pointers at address $a$ and check a zero in each other column. For each of the $r$ Forrelation instances, there are $S$ tests checking the gate values in the proposed circuit transcript, and two checking the required outputs. These tests depend on the candidate and the fixed address, but are exact Boolean computations on the raw input. A gate test reads at most three bits, and a pointer test is an adaptive decision tree of depth at most $\ell+1$. The uniform per-test depth is therefore $\max\{3,\ell+1\}=O(\log m)$. We use the depth bound; it is not necessary that every pointer test depend on a fixed small set of input coordinates.

Prepare a uniform test label, compute whether that test fails, and mark failure of the test as success for an application of Lemma 3.1. Use $\gamma=1/K$ and $\eta=\varepsilon$. Reject the candidate if this search returns a failed test, and accept if it reports failure to find one. Decode and verify every column in the returned tournament list with fresh randomness, stopping if one is accepted; output one exactly in that event. The empty list produces zero.
<!-- /passage:upper-verifier -->

<a id="upper-verification-proof"></a>
<!-- passage:upper-verification-proof -->

For a fixed input, candidate, and decoded address, let $h$ be the number of failed local tests. The search preparation has success probability $h/K$, since the tests are exact and their labels are uniform. If $h=0$, Lemma 3.1 has success probability zero and reports failure to find a test with certainty; the verifier accepts with certainty. If $h\geq1$, its success probability is at least $1/K$, and the verifier accepts with probability at most $\varepsilon$.

Lemma 2.2 supplies the needed logical dichotomy. A nonwinner has at least one failed test at every address. This includes the case that its Forrelation strings violate their promises: if the test list at some address all passed, circuit consistency and the output tests would make that address a genuine winning address. Thus, after averaging over every possible decoded label, a nonwinner is accepted with probability at most $\varepsilon$. A true winner has all tests passing at its true address. Its fresh decoder produces that address with probability at least $1-\varepsilon$, and on that event verification accepts with certainty. Therefore the true winner is rejected with probability at most $\varepsilon$. These are `claim-verify`:

<!-- claim:claim-verify -->
$$
\Pr[\text{accept a nonwinner}]\leq\varepsilon,
\qquad
\Pr[\text{reject the winner}]\leq\varepsilon.
$$

The search uses $O(\sqrt K\ln(1/\varepsilon))$ calls to a uniform-test preparation and its inverse. Each preparation has $O(\ell+1)$ bit-query cost. Adding the fresh address decoding yields $O_k(r\ln(r/\varepsilon)+\sqrt K\ln(1/\varepsilon)(\ell+1))=\sqrt m(\log m)^{O_k(1)}$ queries. This is a cap for all values of $h$, including zero. The algorithm can accept a nonwinner only by missing a failed test; it never accepts because it has assumed an unverified promise about the candidate.

Here $K\geq m\geq4$, so $0<1/K\leq1/2$, as required by Lemma 3.1. For the tournament, $m\geq2$ likewise gives $0<1/(2m)\leq1/2$; in both uses $0<\varepsilon<1/2$.
<!-- /passage:upper-verification-proof -->

<a id="upper-total-error"></a>
<!-- passage:upper-total-error -->

We now prove `claim-error` for every input of the total function. On a zero input, every column is a nonwinner. Condition on the complete tournament transcript and on its list, which contains at most $T$ entries. Each subsequent fresh verification accepts its candidate with probability at most $\varepsilon$, regardless of that transcript. For any fixed list, the probability of at least one false acceptance is at most $T\varepsilon$, by the union bound. Averaging over the tournament transcript preserves this bound. Early stopping at the first acceptance makes no change to the event that at least one acceptance occurs.

On a one input, uniqueness of the winner gives a column $i^\star$. The comparison argument makes it dominant. The tournament misses it with probability at most $2m/2^T+T\varepsilon$. If it occurs in the list, its fresh verification accepts with probability at least $1-\varepsilon$, even conditional on the previous transcript. Any earlier acceptance already gives the correct output one. Thus an erroneous zero output is contained in the union of the miss event and rejection of $i^\star$ when it is verified. We obtain

<!-- claim:claim-error -->
$$
\Pr[\text{error}\mid F_{k,m}(x)=0]\leq T\varepsilon,
\qquad
\Pr[\text{error}\mid F_{k,m}(x)=1]
\leq\frac{2m}{2^T}+T\varepsilon+\varepsilon<\frac13.
$$

For the last numerical inequality, $2^T\geq1000m$ gives $2m/2^T\leq1/500$, and $T\varepsilon=1/1000$. Also $T\geq1$ gives $\varepsilon\leq1/1000$. Their sum is at most $1/250$, which is less than $1/3$. The zero-input bound is smaller still. The fresh verifier acts on a fixed classical input, so its guarantee remains valid after conditioning on earlier outcomes. Neither this conditioning nor the union bound requires independent tournament failures.
<!-- /passage:upper-total-error -->


### 5.4. Coherent access and the query cap


<a id="upper-oracle-access"></a>
<!-- passage:upper-oracle-access -->

We spell out `claim-coherent-access` because the algorithm uses addresses and candidate indices in superposition. The input oracle acts on a coordinate register, an answer bit, and workspace by sending $|u,b,z\rangle$ to $|u,b\mathbin\oplus x_u,z\rangle$. A superposed address is an allowed coordinate state for this same oracle. Computing the coordinate from already stored labels is an input independent reversible operation, so it contributes no query. A pointer is stored in $\ell$ separate input bits. Reading its bits, reversibly forming the indicated coordinate, and querying that coordinate costs $\ell+1$ ordinary queries before any desired uncomputation.

A controlled read can always be implemented with two ordinary bit queries. Start with a fresh answer ancilla zero. Query $x_u$ into that ancilla, perform the desired action controlled jointly by its value and by the original control, and query $x_u$ again to erase the ancilla. Keep the coordinate $u$ unchanged until this second query. The desired action can be an XOR into an output register or a sign change. The resulting transformation is the controlled bit or phase query on every superposition of $u$, control, and workspace, because the basis-state calculation applies linearly. The same construction works when the original control is false: both queries still occur, and their effects cancel.

An exact adaptive local test can be made coherent by retaining its previous query answers, using them to compute the next coordinate, and padding its computation to the fixed maximum depth. At a branch that has halted early, the remaining controlled reads are disabled. Every gate remains a fixed function of the retained labels. The query count is at most a constant times the decision-tree depth. Reversing the full circuit gives the inverse with the same cost. These operations justify coherent comparisons, their inverses, uniform local-test preparation, and the reflections used by amplification within the ordinary bit-oracle model.
<!-- /passage:upper-oracle-access -->

<a id="upper-read-compiler"></a>
<!-- passage:upper-read-compiler -->

The source provides a concrete compilation argument behind this accounting. An abstract read has a coordinate function on basis labels, an involutive permutation of those labels, and an optional sign. Applying that permutation does not change either its coordinate or its sign. Given a basis label, the compiler embeds the abstract register into the physical coordinate, answer-bit, and workspace registers, loads the queried bit, applies the indicated signed permutation if that bit is one, queries the unchanged coordinate again, and returns to the chosen embedding. On bit zero it is the identity; on bit one it is exactly the prescribed signed involution. Both actions preserve inner products. The finite isometries used to place the active register extend to unitaries on sufficiently large finite workspace by completing an orthonormal basis. This is why no unmentioned input-dependent gate is needed.

Composing these read implementations adds their caps, and reversing their logical circuit uses the same number of reads. A circuit of $q$ logical reads is consequently implemented with at most $2q$ ordinary bit queries, also when its indices are superposed. For classical-label continuations, one may measure the complete computational-basis state and then apply a basis permutation taking the known outcome back to the fixed initial basis state. This reset has no query cost. Its classical output law is exact, but the measurement is not an implementation of returning an unmeasured original quantum state. This distinction explains the two amplification interfaces discussed in §5.5.

The final bound thus concerns the same total input function, on every bit string, with a syntactic maximum over branches. It does not measure an average number of queries. It does not provide a bound on the number of elementary gates or the amount of workspace, which are free in the stated query model.
<!-- /passage:upper-read-compiler -->

<a id="upper-finite-budget"></a>
<!-- passage:upper-finite-budget -->

We can now state an exact finite budget before simplifying it asymptotically. This makes the padding, repetitions, and compilation constants explicit. Let $n$ be the Forrelation repetition count for error $\varepsilon/r$, let $a=rnk$ be the address circuit's abstract read count, let $c_c=2a+2(2t+1)$ be the comparison read count, and let $c_0=\max\{3,2t+1\}$ be the uniform test read count. Write $N=\lceil\ln(1/\varepsilon)/\ln(40/31)\rceil$, $M_0=\lceil10\sqrt{2m}\rceil$, and $M_1=\lceil10\sqrt K\rceil$. The supplied construction has the following budget, recorded as `new-upper-finite-budget`:

<!-- claim:new-upper-finite-budget -->
$$
B_{k,t}
 =T\bigl[2N(2M_0+1)T c_c\bigr]
  +T\bigl[2a+2N(2M_1+1)c_0\bigr].
$$

The first bracket is one tournament stage: at most $N$ trials, at most $2M_0+1$ preparation or inverse calls per trial, at most $T c_c$ abstract reads per such call, and two bit queries per read. Every stage is padded to the maximum history length $T$, and there are at most $T$ stages. The second bracket is one verifier: $2a$ bit queries for its fresh address decoder, followed by the amplified local-test search with its corresponding trial and iteration bounds. There are at most $T$ candidates to verify. All random branches and all off-promise inputs obey this same integer budget.

The preceding construction and error analysis prove that this integer budget bounds $Q(F_{k,m})$ for every realizing circuit with the stated local tests. Correctness is therefore established before substituting the size of the particular circuit chosen in §4. The exact conversion factors in this budget are convenient upper bounds; the earlier expression with $t$ comparisons at stage $t$ gives the same asymptotic result with less padding.
<!-- /passage:upper-finite-budget -->

<a id="upper-asymptotic-bound"></a>
<!-- passage:upper-asymptotic-bound -->

The earlier estimates already prove Proposition 3.3. The tournament contributes $O(c\sqrt m\,T^2\log T)$ queries, where $c=(\log m)^{O_k(1)}$, and the at most $T=O(\log m)$ verifications each cost $\sqrt m(\log m)^{O_k(1)}$. Their sum has the same form. Coupled with the error bound, this gives `prop-3.3`:

<!-- claim:prop-3.3 -->
$$
Q(F_{k,m})\leq\sqrt m\,(\log m)^{O_k(1)}
\qquad(k\geq2,\ m=4^t,\ t\geq1).
$$

Here $F_{k,m}$ uses the circuit fixed for that $k,m$ in the construction. The implicit constants may depend on $k$. The exponent statement concerns query complexity, and every input is covered. There is no appeal to Bansal and Sinha's randomized lower bound in this proof of the quantum upper bound.
<!-- /passage:upper-asymptotic-bound -->

<a id="upper-explicit-log6"></a>
<!-- passage:upper-explicit-log6 -->

For the particular circuit fixed in §4, the same budget gives the explicit logarithmic exponent six. There is a positive integer $C_k$, depending only on $k$, such that the particular Forrelation circuit used in the construction satisfies

<!-- claim:new-upper-log6 -->
$$
Q(F_{k,4^t})\leq C_k\,2^t(2t)^6
\qquad(t\geq1).
$$

We give the size arithmetic to make the independence of $C_k$ from $t$ explicit. Put $\tau=2t$ and $u=2^t$, so $m=u^2$, $r=20\tau$, and $\tau\geq2$. For the chosen circuit, set $C_F(k)=200(k+1)^2$, the source circuit-size constant, so $S\leq C_F(k)m\tau^2$. Define $R_k=1+1920000\cdot2^{10k}$, $C_c(k)=40R_kk+4$, and $C_K(k)=42+20C_F(k)$. Each is independent of $t$.

First, $1000<2^{10}$ implies $T\leq\tau+10\leq6\tau$. Hence $1/\varepsilon=1000T\leq6000\tau$. Using $\ln(1/\varepsilon)\leq1/\varepsilon$ and $\ln(40/31)\geq1/4$, the ceiling defining $N$ gives $N\leq4/\varepsilon+1\leq24001\tau$. Likewise $r/\varepsilon\leq120000\tau^2$. Since the decoder's repetition count is at most $16\cdot2^{10k}\ln(r/\varepsilon)+1$, it is at most $R_k\tau^2$. Thus $a=rnk\leq20R_kk\tau^3$. The remaining comparison cost $2(\tau+1)$ is at most $4\tau^3$, so $c_c\leq C_c(k)\tau^3$.

Second, the formula for $K$ gives $K=2m-1+20\tau(S+2)\leq C_K(k)m\tau^3$. For example, the circuit term is at most $20C_F(k)m\tau^3$; the $2m$ term is at most $2m\tau^3$, and $40\tau\leq40m\tau^3$. Because $C_K(k)\geq1$ and $\tau\geq1$, this implies $\sqrt K\leq C_K(k)u\tau^2$. Also $\sqrt{2m}\leq2u$. The ceilings consequently give $2M_0+1\leq43u$ and $2M_1+1\leq23C_K(k)u\tau^2$. Finally $c_0\leq3\tau$.

Insert these bounds into the two brackets of $B_{k,t}$. One tournament stage is at most $48002\cdot258\,C_c(k)u\tau^5$: the factors are twice $24001\tau$, then $43u$, then $6\tau\,C_c(k)\tau^3$. Its at most $6\tau$ stages contribute at most $6(48002\cdot258\,C_c(k))u\tau^6$. One verifier is at most $(40R_kk+48002\cdot69\,C_K(k))u\tau^4$. Here its decoder cost $2a$ has been enlarged using $u,\tau\geq1$, and its search term has factors twice $24001\tau$, then $23C_K(k)u\tau^2$, then $3\tau$. Multiplying by $T\leq6\tau$ and enlarging $\tau^5$ to $\tau^6$ gives the remaining contribution. Thus one may take $C_k=6(48002\cdot258\,C_c(k))+6(40R_kk+48002\cdot69\,C_K(k))$, exactly the source's deliberately loose constant `QuarticQuery.Upper.budgetConst`.

This completes the quantum half of the family bounds with the same chosen circuit that appears in the total function. It proves the bound for each fixed $k$; no randomized lower bound and no growing-$k$ estimate is used.
<!-- /passage:upper-explicit-log6 -->


### 5.5. Formal correspondence and the remaining state specification

<a id="upper-current-formal-scope"></a>
<!-- passage:upper-current-formal-scope -->
The current packet contains a successful source-bound root build receipt and later exact-type/axiom auditing, in addition to focused module passes. The former record labels its commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`, while the packet manifest labels its repository commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`. For the local Lean/configuration closure, all 124 supplied source hashes agree across the current files, evidence snapshot, root receipt, dependency export and axiom verdict. This makes the recorded evidence applicable to those exact bytes despite the differing commit labels. It is not a fresh Lean execution in this review. The recorded toolchain is `leanprover/lean4:v4.36.0-rc2`; the dependency pins are preserved in the source receipt.

The following distinctions determine the formal claims in this section.

| Ordinary statement | Current formal support and its scope |
|---|---|
| Grover rotation and returned successful state in Lemma 3.1 | `QuarticQuery.Amplification.bounded_amplification` proves the complete abstract `Proc` assertion, including phase-invariant observables, zero wrong-state mass, zero-success failure and a uniform call cap. |
| Physical successful-label amplification | `QuarticQuery.Upper.Samples.amplify` gives the measured `Runs` law used by the final bound. `QuarticQuery.Paper.quantum_amplify_samples` gives a coherent `Samples` realization of the same label law with retained workspace. Neither type identifies a designated physical output subsystem with the original normalized successful state. |
| Full tensor state in equation (15) | `QuarticQuery.Paper.equation_15` supplies the literal fresh-register tensor construction; `quantumWorkspace_uniformize` and `quantumTensorStage_of_samples` supply the common-workspace realization. The alternative `Upper.stage_samples` can omit later work after failure. Its successful index law agrees, without equality of the full retained states. |
| List-valued Proposition 3.2 | `QuarticQuery.Paper.quantumTournament` now supplies an actual finite bounded-list `Samples` witness, its `Runs` implementation, a normalized nonnegative law, the dominant-membership estimate and the explicit 6072 query bound. The older claim that only a Boolean endpoint exists is obsolete for this packet. |
| Decoder, comparison and verification | The current `Paper.quantumDecode_correct`, `quantumComparison_state`, `quantumWinner_dominates`, `quantumVerify` and `quantumError_bound` expose the corresponding laws and all-input budgets. Correctness assumptions on promised Forrelation instances remain explicit. |
| Proposition 3.3 and the exponent six | `QuarticQuery.Upper.Fkm_forrCircuit_QLe` gives the algorithmic upper bound; `Upper.Q_Fkm_le` gives its numerical complexity form. `Upper.budget_le` bounds the actual integer budget. The formal parameter is $k=l+1$, $m=4^t$, $t\geq1$. |

The supplied dependency export for `theorem_1_1_unconditional` and `cubic_bound_fails_unconditional` reaches the older measured/Boolean upper-bound route, including `Samples.amplify` and `Q_Fkm_le`. It does not reach the new `Paper` list and tensor wrappers. This is a fact about those specified proof roots; it does not negate the wrappers' compilation or their mathematical statements. Exact-name Comparator coverage is narrower again: in particular, the Tournament bundle compares two drift wrappers, not the new list theorem. The companion files record declaration membership, complete available types and these evidence dimensions separately. Historical “UNELABORATED” comments in integrated source files do not override newer source-bound passing receipts.
<!-- /passage:upper-current-formal-scope -->

<a id="upper-missing-physical-state"></a>
<!-- passage:upper-missing-physical-state -->
The remaining formal target for the complete physical reading of Lemma 3.1 can be stated without ambiguity. Fix a finite original Hilbert space $H$ with its computational basis, a basis state $h_0$, a fixed success projector $\Pi$ on $H$, and a concrete oracle-dependent unitary circuit $A_x$ with at most $q$ logical reads. Put $p_x=\|\Pi A_x|h_0\rangle\|^2$ and, only when $p_x>0$, put $g_x=\Pi A_x|h_0\rangle/\sqrt{p_x}$.

<!-- claim:r3-q-physical-state-bridge -->
For fixed $0<\gamma\leq1/2$ and $0<\eta<1/2$, the desired theorem must construct a finite auxiliary register $J$ with fixed initial state $j_0$, a final success predicate on $J$, and a coherent unitary $B_x$ on $H\otimes J$. The construction includes a specified input-independent routing that places the complete first successful original register in the designated $H$ slot. Write $\Pi_{\rm out}=I_H\otimes\Pi_J$ for the final auxiliary-flag success projection and
$$
 \Psi_x=B_x(|h_0\rangle\otimes|j_0\rangle),
 \qquad s_x=\|\Pi_{\rm out}\Psi_x\|^2.
$$
The required statement is
$$
 \begin{aligned}
 &0\leq s_x\leq1,\qquad
   p_x\geq\gamma\Longrightarrow s_x\geq1-\eta,\qquad
   p_x=0\Longrightarrow\Pi_{\rm out}\Psi_x=0,\\
 &p_x>0\Longrightarrow s_x\geq p_x/2>0,\\
 &p_x>0\Longrightarrow
   \exists\,\xi_x\in J:\quad
       \Pi_{\rm out}\Psi_x=g_x\otimes\xi_x
       \quad\hbox{and}\quad\|\xi_x\|^2=s_x.
 \end{aligned}
$$
It must give a logical-read circuit cap $qN(2M+1)$ and transport this same circuit through the physical compiler with cap at most $2qN(2M+1)$ ordinary bit queries, on arbitrary embedded input states and continuations. This arbitrary-state clause concerns correctness of the compiler; the amplification guarantee concerns the specified initial state. All these bounds hold on every input, whether or not $p_x\geq\gamma$.

To express the preprint's black-box uniformity, the underlying program with slots for $A$ and $A^{-1}$ must be fixed by $\gamma,\eta$ and the register/query interface before the preparation oracle is supplied. Its branches, $M,N$ and cap cannot depend on $p_x$. The auxiliary space, routing and all non-oracle gates are input-independent. An equivalent adaptive formulation gives the same normalized original-register state, up to phase, on every positive-mass successful history. The finite-coordinate version and an explicitly uncompiled proposed interface are in the accompanying gap record.

The ordinary fresh-trial/routing argument in §5.1 supplies the mathematical construction. The packet does not supply a source-bound Lean theorem of this full physical type. In particular, the coherent composition can retain a copy of a successful output label in auxiliary registers, and the measured compilation route reads a complete basis label. A proof of the displayed factorization, or an equivalent output-subsystem theorem after a specified uncomputation, is still needed before promoting the physical wrapper to the full state claim. This missing formal bridge is not an extra assumption in the proof of Proposition 3.3: that proof uses only measured labels, whose law is already supplied by the compiled route.
<!-- /passage:upper-missing-physical-state -->

### References for §5

- **OpenAI2026.** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026. Supplied PDF SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`, §3, Lemma 3.1 and Propositions 3.2–3.3, printed pp. 7–10. This is the mathematical target and attribution source; the public GitHub location was confirmed, while the supplied bytes are the reviewed edition.
- **BHMT2000.** Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp, *Quantum Amplitude Amplification and Estimation*, [arXiv:quant-ph/0005055v1](https://arxiv.org/abs/quant-ph/0005055v1), 15 May 2000. §2, Lemma 1 and equation (8), printed pp. 5–7, supply the rotation mechanism. Theorem 12, p. 19, concerns estimation. Published in *Contemporary Mathematics* **305**, 53–74 (2002); locators here use the inspected arXiv edition.
- **BBHT1996.** Michel Boyer, Gilles Brassard, Peter Høyer and Alain Tapp, *Tight bounds on quantum searching*, [arXiv:quant-ph/9605034v1](https://arxiv.org/abs/quant-ph/9605034v1), 23 May 1996. §4, Lemma 2, p. 3, supplies the averaged identity; Theorem 3, p. 4, is an expected-time search result. A journal version appeared in *Fortschritte der Physik* **46** (1998); the mathematical locators here use the inspected arXiv edition.
- **DH1999.** Christoph Dürr and Peter Høyer, *A quantum algorithm for finding the minimum*, [arXiv:quant-ph/9607014v2](https://arxiv.org/abs/quant-ph/9607014v2), revised 7 January 1999, original July 1996. Theorem 1 and Lemmas 1–2, pp. 1–2; ordered-value context, not a premise for arbitrary probabilistic comparisons.
- **HMW2003.** Peter Høyer, Michele Mosca and Ronald de Wolf, *Quantum Search on Bounded-Error Inputs*, [arXiv:quant-ph/0304052v2](https://arxiv.org/abs/quant-ph/0304052v2), 14 April 2003. §1, pp. 1–3, gives the fixed-predicate correctness hypothesis; §3, pp. 4–7, gives the search construction; §5, pp. 8–9, discusses its imperfect-verifier generalization; the AND–OR applications are in §4. ICALP 2003, LNCS **2719**, 291–299. Comparison only; no imported proof step here.
- **BDK2026.** Shalev Ben-David and Robin Kothari, *Randomized query complexity can beat certificate complexity*, [arXiv:2609.15063v1](https://arxiv.org/abs/2609.15063v1), 14 September 2026. §3, Lemma 5, pp. 3–5; antecedent for generating candidates, comparing and checking certificates.
- **MPS2023.** Nikhil S. Mande, Manaswi Paraashar and Nitin Saurabh, *Randomized and Quantum Query Complexities of Finding a King in a Tournament*, [FSTTCS 2023, LIPIcs **284**, Article 30](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30), pp. 30:1–30:19. Theorem 19 in §4, pp. 30:11–30:13, concerns a fixed orientation with exact edge queries. The theorem number is that of the linked published edition.
