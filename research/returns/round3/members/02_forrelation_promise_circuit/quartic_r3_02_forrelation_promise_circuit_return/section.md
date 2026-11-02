# Forrelation: its promise, quantum preparation, and exact circuit

<!-- passage:forr_scope -->
Replacement for §§3.1–3.5 of the supplied long reasoning record. This section uses the bit-query model of §2.2. It supplies the quantum and circuit conclusions consumed by §3.17; the randomized lower bound remains in §§3.6–3.16. Fix an integer $k\ge2$, let $t\ge1$ be an integer, and put $m=4^t$. All unqualified logarithms are base two; natural logarithms are written $\ln$. The input consists of $k$ blocks of $m$ bits.

The construction needs two ways of using the same partial function. A quantum procedure proposes its value with small error whenever the promise holds. An exact Boolean circuit certifies both that the promise holds and that a proposed value is correct. The first procedure must still produce an output on unpromised inputs; the second must identify those inputs exactly. OpenAI's Lemma 2.1(ii)–(iii) asks for these two properties [OAI26, §2.1, pp. 3–5].

<!-- /passage:forr_scope -->

<!-- passage:forr_definition -->
## 3.1. The normalized Walsh product and the promise

Index coordinates by $G=\mathbb F_2^{2t}$. The inner product $a\cdot b$ is taken in $\mathbb F_2$. A bit $x_r(a)$ represents the sign $z_r(a)=(-1)^{x_r(a)}$, so a true bit represents $-1$. Number blocks from $0$ to $k-1$, shifting the preprint's indices by one. Define

<!-- claim:def-walsh-sign -->
$$
W_{ab}=(-1)^{a\cdot b},\qquad H=m^{-1/2}W,
\qquad u=m^{-1/2}(1,\ldots,1)^{\mathsf T},
\qquad D_z=\operatorname{diag}(z).
$$

The normalization makes $H$ orthogonal. Indeed, the inner product of rows $a,c$ of $W$ is $\sum_{b\in G}(-1)^{(a+c)\cdot b}$. If $a=c$, this is $m$. Otherwise, choose a coordinate in which $a+c$ is one and pair every $b$ with the vector obtained by flipping that coordinate. Each pair cancels. Symmetry of $a\cdot b$ and the identity $z(a)^2=1$ now give

<!-- claim:NEW-FOR-01 -->
$$
WW^{\mathsf T}=mI,\qquad H^{\mathsf T}=H,\qquad H^2=I,
\qquad \|u\|_2=1,\qquad D_z^{\mathsf T}D_z=I.
$$

Define the real Forrelation value and threshold by

<!-- claim:eq-3 -->
$$
\Phi(z)=u^{\mathsf T}D_{z_0}H D_{z_1}H\cdots H D_{z_{k-1}}u,
\qquad \delta=2^{-5k}.
$$

There are $k$ diagonal matrices and $k-1$ Walsh matrices. Every factor preserves norm, so Cauchy–Schwarz gives $|\Phi(z)|\le1$ on every input. The partial function is

<!-- claim:eq-4 -->
$$
P_{k,m}(z)=
\begin{cases}
1,&\Phi(z)\ge\delta,\\
0,&|\Phi(z)|\le\delta/2,\\
\text{undefined},&\text{otherwise}.
\end{cases}
$$

Its two defined cases are disjoint because $\delta>0$. The positive threshold is essential to the stated problem: a value $\Phi=-1$ is unpromised. For example, at $k=2,m=4$, fixing the second block as $(-1,1,1,1)$ and varying the first produces $\Phi=1,0,-1$. Section 3.5 calculates all three cases and counts every input.

Aaronson and Ambainis introduced the $k$-fold quantity and its quantum interpretation [AA14/18, §1.1.3 and §3.2]. The parameterized promise above is Bansal–Sinha's equations (1.1)–(1.3), with their block length $N$ equal to our $m$; their Theorem 1.3 chooses $\delta=2^{-5k}$ [BS20v3]. Their $N=2^n$ permits any power of two. Our specialization $n=2t$ makes $m=4^t$, and hence $\sqrt m=2^t$, integral. It is useful for the exact arithmetic below and is not required for Walsh orthogonality or the quantum preparation. Aaronson–Ambainis's numerical promise thresholds are different, so that paper supplies the antecedent construction rather than these particular thresholds.

To keep the interface with the later lower bound fixed, retain

<!-- claim:eq-5 -->
$$
L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
$$

Here $\log_2m=2t>0$. No lower bound involving $L_{k,m}$ is proved in these five subsections.
<!-- /passage:forr_definition -->

<!-- passage:forr_integer -->
## 3.2. An integer numerator and exact promise tests

Expanding the matrix product uses one coordinate from each block. Removing its $k+1$ factors of $m^{-1/2}$—two from the boundary vectors and $k-1$ from the Walsh matrices—gives

<!-- claim:claim-N-phi -->
$$
\begin{aligned}
N(z)&=\sum_{(a_0,\ldots,a_{k-1})\in G^k}
  \left(\prod_{r=0}^{k-1}z_r(a_r)\right)
  \left(\prod_{r=0}^{k-2}W_{a_r,a_{r+1}}\right)\in\mathbb Z,\\
M&=m(\sqrt m)^{k-1}=2^{t(k+1)}>0,
\qquad \Phi(z)=\frac{N(z)}{M}.
\end{aligned}
$$

Each term in $N$ is a sign. This formula identifies the integer being computed, but evaluating its $m^k$ summands individually would be wasteful. Instead set $v_{k-1}=z_{k-1}$, and for $r=k-2,\ldots,0$ set $v_r=D_{z_r}Wv_{r+1}$. Then $N=\sum_a v_0(a)$. Expanding this recurrence recovers exactly the same path sum. The earlier norm bound gives the sharper final estimate $|N|\le M$.

Multiplying by the positive denominators gives the two exact tests

<!-- claim:claim-integer-tests -->
$$
\Phi\ge\delta\quad\Longleftrightarrow\quad2^{5k}N\ge M,
\qquad
|\Phi|\le\delta/2\quad\Longleftrightarrow\quad2^{5k+1}|N|\le M.
$$

Let $p_1$ and $p_0$ be the truth values of these respective comparisons. The desired Boolean outputs are

$$
d=p_1\lor p_0,\qquad b=p_1.
$$

Thus $d=1$ if and only if $P_{k,m}$ is defined, and then $b=P_{k,m}$. These output rules specify a total pair of Boolean functions. In particular, an unpromised input has $d=b=0$. This last statement describes the particular exact circuit; it places no restriction on the quantum procedure's answer off the promise.
<!-- /passage:forr_integer -->

<!-- passage:forr_quantum -->
## 3.3. The quantum promise algorithm, including amplification and coherence

Start the address register in $u$. For the fixed input $z$, write

$$
U_z=D_{z_0}H D_{z_1}H\cdots H D_{z_{k-1}},
\qquad \psi_z=U_zu.
$$

Apply this word from right to left. To implement $D_{z_r}$, put the oracle answer qubit in $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$. The bit oracle of §2.2 acts by

$$
O_x\bigl(|r,a\rangle|-\rangle\bigr)
 =(-1)^{x_r(a)}|r,a\rangle|-\rangle.
$$

The answer qubit remains in the same state, including for a superposition of addresses. A query-free permutation places the desired block label in the oracle address register. Each diagonal therefore needs one ordinary bit query, and each $H$ needs none. One preparation of $\psi_z$ uses $k$ bit queries on every input.

Let $\Pi=|u\rangle\langle u|$. The projection amplitude is $\langle u,\psi_z\rangle=\Phi(z)$, so the probability of the $\Pi$ outcome is

<!-- claim:claim-proj-prob -->
$$
p(z)=\|\Pi\psi_z\|^2=\Phi(z)^2,
\qquad
\begin{cases}
p(z)\ge\delta^2,&P_{k,m}(z)=1,\\
p(z)\le\delta^2/4,&P_{k,m}(z)=0.
\end{cases}
$$

The projection can be measured without queries: apply the inverse of a preparation of $u$, and test for the zero address. Squaring removes the sign of $\Phi$, which is harmless on the stated promise. It would not decide a different problem that required rejecting every large negative value.
<!-- /passage:forr_quantum -->

<!-- passage:forr_repetition -->
**An explicit error bound.** Put $c=\delta^2=2^{-10k}$. Repeat the trial $q$ times on fresh registers and let $S$ be the number of successes. Output one exactly when $S\ge qc/2$. The integer comparison means $S\ge\lceil qc/2\rceil$; equality is included in the one-output event. For independent Bernoulli trials with success probability $p$, multiplication of the one-trial moments gives

$$
\mathbb E a^S=(1-p+pa)^q\qquad(a>0).
$$

If $p\le c/4$, Markov's inequality and $1+y\le e^y$ imply

$$
\begin{aligned}
\Pr[S\ge qc/2]
&\le e^{-qc/2}\mathbb E e^S\\
&\le\exp\bigl(-qc/2+qp(e-1)\bigr)
\le e^{-qc/16}.
\end{aligned}
$$

The last step uses $e-1\le7/4$. If $p\ge c$, the event $S<qc/2$ implies $e^{-S}>e^{-qc/2}$, and the same argument gives

$$
\begin{aligned}
\Pr[S<qc/2]
&\le e^{qc/2}\mathbb E e^{-S}\\
&\le\exp\bigl(qc/2-qp(1-e^{-1})\bigr)
\le e^{-qc/10}\le e^{-qc/16},
\end{aligned}
$$

using $1-e^{-1}\ge3/5$. Both numerical bounds follow from $5/2<e<11/4$: the exponential series through degree three gives the lower bound, and its tail from $1/4!$ is at most $(1/24)\sum_{j\ge0}5^{-j}=5/96$, giving the upper bound. Markov's inequality itself follows by integrating $Y\ge a\mathbf1_{Y\ge a}$ for a nonnegative random variable $Y$.

<!-- claim:NEW-FOR-02 -->
For any $0<\eta<1/2$, choose

$$
q=\left\lceil16\,2^{10k}\ln(1/\eta)\right\rceil.
$$

Then $qc/16\ge\ln(1/\eta)$, so either error probability is at most $\eta$. Also $q\le1+16\,2^{10k}\ln(1/\eta)$. This is a fixed repetition count, chosen before the input; no measurement outcome changes the query cap.
<!-- /passage:forr_repetition -->

<!-- passage:forr_coherent -->
**The same preparation with its workspace retained.** Decompose the one-trial state as

$$
\alpha_1=\Pi\psi_z,\qquad \alpha_0=(I-\Pi)\psi_z,
\qquad \langle\alpha_0,\alpha_1\rangle=0,
\qquad \|\alpha_1\|^2=p,\quad\|\alpha_0\|^2=1-p.
$$

Introduce a fresh flag qubit initially zero. The input-independent unitary $\Pi\otimes X+(I-\Pi)\otimes I$, where $X$ flips that qubit, maps the state to

$$
\alpha_0\otimes|0\rangle+\alpha_1\otimes|1\rangle.
$$

It is unitary because its two projector blocks are orthogonal and $X^2=I$. Apply it to each of the $q$ fresh trials and group the address registers before the flags by a query-free permutation. The resulting pure state is

<!-- claim:R3-FOR-COHERENT-LAW -->
$$
\sum_{h\in\{0,1\}^q}
 \left(\bigotimes_{j=1}^{q}\alpha_{h_j}\right)\otimes|h\rangle.
$$

The summands with different $h$ occupy orthogonal flag subspaces. Their squared norms are $p^{|h|}(1-p)^{q-|h|}$, where $|h|$ is Hamming weight. Reversibly compute $|h|$ into a count register and the predicate $[|h|\ge qc/2]$ into an output qubit. This requires no queries: the map $|h,a\rangle\mapsto|h,a\mathbin\oplus f(h)\rangle$ is a basis permutation for any fixed finite Boolean string-valued function $f$. Retain every address, flag, and count register.

For this very preparation, measuring the output qubit has the law

$$
\begin{aligned}
\mathcal L_z(1)
 &=\sum_{s=0}^{q}\mathbf1_{\{s\ge qc/2\}}
       {q\choose s}p(z)^s(1-p(z))^{q-s},\\
\mathcal L_z(0)&=1-\mathcal L_z(1).
\end{aligned}
$$

At $p=0$ or $1$, interpret the polynomial factors using $0^0=1$. Every term is nonnegative, and the binomial theorem gives total mass one on every input. The two tail estimates apply to this law because it is exactly the law obtained by measuring the trials individually. Thus the coherent implementation has the same promised accuracy, retains all workspace, and yields a Boolean output even when $P_{k,m}(z)$ is undefined.

<!-- claim:NEW-FOR-28 -->
The explicit phase implementation proves the ordinary query bound

$$
Q_\eta(P_{k,m})\le k\left\lceil16\,2^{10k}\ln(1/\eta)\right\rceil
 =O_k(1+\log(1/\eta)).
$$

Here $Q_\eta$ is the minimum worst-case number of ordinary bit queries needed for error at most $\eta$ on every promised input, with the cap holding on every input. It extends §2.2's convention $Q=Q_{1/3}$. The coherent state just constructed also has that fixed cap.

<!-- claim:lem-2.1.ii -->
**Formal implementation of the asymptotic conclusion.** Instantiating the supplied coherent sampler at $q$ repetitions gives $qk$ abstract reads; its generic compiler uses at most $2qk$ physical bit queries. The complete Lemma 2.1(ii) wrapper packages this construction with a repetition count $n$ and law existentially quantified; its proof chooses $n=q$. It binds one isometry $F_z$, one initial basis state, one output labeling, and that isometry's measured law. The physical implementation applies the same $F_z$ before every subsequent continuation and adds at most $2nk$ to the continuation's cap. This connects coherence, the measured law, and the physical cost in one witness, proving the required $O_k(1+\log(1/\eta))$ conclusion. The explicit ceiling choice is supplied by the repetition and decoder theorems, rather than asserted by the wrapper's existential statement alone.

The local phase-kickback identity has also been compiled, but it does not yet supply a complete formal program with the sharper $qk$ physical cap. The sharper displayed inequality has the ordinary construction above. Likewise, the explicit tensor-state display explains our construction; the source's retained-isometry theorem does not assert an equality to that display in the same concrete register representation. Full theorem types and these distinctions are recorded in the correspondence files.

Aaronson–Ambainis also give an interference procedure with $\lceil k/2\rceil$ queries and acceptance probability $(1+\Phi)/2$ [AA14/18, Proposition 6, pp. 13–14; BS20v3, Proposition 1.2, p. 3]. That is a different test. The projection experiment already appears in [AA14/18, §3.2, Figure 1 and the paragraph before Proposition 6]; the version used in [OAI26, proof of Lemma 2.1(ii)] and here keeps its probability $\Phi^2$ throughout.
<!-- /passage:forr_coherent -->

<!-- passage:forr_circuit -->
## 3.4. The exact Boolean circuit

The integer tests in §3.2 require exact comparisons at their endpoints. We now implement them with a number of fan-in-two Boolean gates bounded by $O_k(m(\log m)^2)$.

**Fast Walsh multiplication.** On a vector of length $2^{h+1}$, split the coordinates according to their highest input bit. Writing $W_{2^h}$ for the unnormalized Walsh matrix on $h$ bits gives

<!-- claim:NEW-FOR-03 -->
$$
W_{2^{h+1}}(a_0,a_1)
 =\bigl(W_{2^h}a_0+W_{2^h}a_1,
        W_{2^h}a_0-W_{2^h}a_1\bigr).
$$

For an output index with highest bit zero, the two input halves contribute with the same sign. For highest bit one, their signs are opposite. This proves the formula coordinate by coordinate. There are $2^{h+1}$ scalar additions or subtractions at that split, in addition to the two transforms of size $2^h$. Starting with zero work at size one, the recurrence gives $m\log_2m$ scalar additions and subtractions for a transform of length $m$.

<!-- claim:claim-circuit-size -->
The numerator requires $k-1$ such transforms, $k$ sign layers, and a final sum. In the ideal integer recurrence, after $j$ full transforms every coordinate has magnitude at most $m^j$. During the next transform, a partial butterfly sum has at most $m$ terms, each bounded by $m^j$, so its magnitude is at most $m^{j+1}$. Sign changes preserve these bounds. Every prefix of the final sum is bounded by $m\,m^{k-1}=m^k$. Consequently $k\log_2m+2$ signed bits suffice for this ideal computation, and multiplying by the powers $2^{5k}$ and $2^{5k+1}$ adds only $O(k)$ bits. This proves the preprint's polynomial bound on the ideal intermediate integers.

The implemented circuit instead maintains congruences modulo one fixed power of two. Its arithmetic guarantee says that a $w$-bit word represents the intended integer modulo $2^w$. Addition, subtraction, and multiplication by a sign preserve that guarantee. Thus the implementation only needs a signed range bound for the three final comparison integers. A theorem about the magnitudes of ideal intermediate sums does not, on its own, identify every stored word with a signed intermediate value.
<!-- /passage:forr_circuit -->

<!-- passage:forr_boolean_arithmetic -->
**Arithmetic using fan-in-two gates.** For bits $a,b,c$, form $r=a\mathbin\oplus b$, the sum bit $s=r\mathbin\oplus c$, and the carry $d=(a\land b)\lor(r\land c)$. These are five gates. Checking the possibilities for the number of ones gives $s+2d=a+b+c$. A chain of $w$ such adders, after multiplying the identities by successive powers of two, gives the sum modulo $2^w$; the final carry is discarded.

For conditional subtraction, xor each bit of the second word with a control bit and use that control as the initial carry. When it is zero, the result is addition. When it is one, complementing a word of value $B$ gives $2^w-1-B$, and the initial carry changes this to $-B\pmod{2^w}$. There are $w$ additional xor gates. Starting from a zero first word gives multiplication by a sign. The implementation uses the following counts, including its explicit constant-true gate for subtraction:

<!-- claim:NEW-FOR-04 -->
$$
\begin{array}{c|c}
\text{operation on }w\text{-bit words}&\text{non-input gates}\\\hline
A+B\pmod{2^w}&6w\\
A-B\pmod{2^w}&6w+1\\
(-1)^bB\pmod{2^w}&6w
\end{array}
$$

Zero wires and reuse of wires cost no gates in the stated circuit model, which allows arbitrary Boolean truth functions of at most two inputs. Induction on the Walsh recurrence yields

$$
\operatorname{whtCost}(w,h)\le h2^h(6w+1).
$$

Indeed, after two transforms of length $2^h$, the $2^h$ additions and $2^h$ subtractions cost $2^h(12w+1)$; combining this with the two induction bounds proves the inequality at $h+1$. Because the same arithmetic identities hold modulo $2^w$, the circuit computes a residue of $N$ exactly.
<!-- /passage:forr_boolean_arithmetic -->

<!-- passage:forr_final_signs -->
**Recovering the three final signs.** Put $s=5k$, $e=t(k+1)$, and choose

$$
w=s+3+e.
$$

Since $M=2^e$, the needed integers are

$$
A=2^sN-M,\qquad B=M-2^{s+1}N,
\qquad C=M+2^{s+1}N.
$$

From $|N|\le M$, all three absolute values are at most $(2^{s+1}+1)M$. This is strictly less than $2^{s+2}M=2^{w-1}$. Write $\operatorname{neg}(T)$ for the high bit of the residue of $T$ modulo $2^w$. For every integer $T$ in the interval $[-2^{w-1},2^{w-1})$, this bit is one precisely when $T<0$: a nonnegative $T$ already lies in the lower half, whereas a negative $T$ has residue $2^w+T$ in the upper half. Therefore

<!-- claim:NEW-FOR-05 -->
$$
p_1=\neg\operatorname{neg}(A),\qquad
p_0=\neg\operatorname{neg}(B)\land\neg\operatorname{neg}(C).
$$

The first predicate is $2^{5k}N\ge M$. The second is the pair of inequalities $-M\le2^{5k+1}N\le M$, equivalently $2^{5k+1}|N|\le M$. Equality is accepted in both tests. Set $b=p_1$ and $d=p_1\lor p_0$. Three gates suffice after the sign wires: one negates the first sign, one computes the conjunction of the other two negated signs, and one forms the disjunction.

This proves the output guarantee on every input. The arithmetic is performed through residues, but the outputs are the ordinary integer comparisons because the tested integers have just been proved to lie in the signed range. No floating-point approximation enters.
<!-- /passage:forr_final_signs -->

<!-- passage:forr_circuit_size -->
**Size and circuit transcripts.** For fixed $k$, $w=5k+3+t(k+1)=O_k(t)$. There are $O(km\log m)$ arithmetic operations, each costing $O(w)$ gates, and $\log_2m=2t$. Hence the total size is $O_k(m(\log m)^2)$.

The maintained circuit admits the explicit bound

<!-- claim:NEW-FOR-29 -->
$$
S\le200(k+1)^2m(\log_2m)^2\qquad(k\ge1,\ t\ge1).
$$

There is a short way to recover the constant from the constructor costs. The Walsh recurrence solves exactly to $\operatorname{whtCost}(w,2t)=tm(12w+1)$. The numerator layers use one constant gate, $k$ layers of $m$ sign multiplications, and $k-1$ transforms. Adding the final sum, repeated doublings, three comparisons, and three output gates gives

<!-- claim:R3-FOR-CIRCUIT-SIZE -->
$$
S=6w\bigl((k+1)m+5k+t(k+1)+4\bigr)
 +(k-1)tm(12w+1)+7.
$$

For the inequality, put $a=k+1$. Since $t\ge1$, we have $w\le6at$. The bracket is at most $7amt$: use $am\le amt$, $at\le amt$, and $5k+4\le5a\le5amt$. Therefore its contribution is at most $252a^2mt^2$. Since $12w+1\le13w$ and $k-1\le a$, the transform contribution is at most $78a^2mt^2$. Finally $a^2mt^2\ge1$, so

$$
S\le337a^2mt^2\le800a^2mt^2
 =200(k+1)^2m(\log_2m)^2.
$$

This accounting is an ordinary derivation from the same constructors. It bounds the actual gate list, including its repeated doublings; the closed-form cost identity is not a newly compiled Lean theorem.

<!-- claim:lem-2.1.iii -->
Thus, for each $k\ge2$ and $t\ge1$, there is a fan-in-at-most-two circuit $C_{k,m}$ with the displayed bound and outputs

$$
d(z)=1\Longleftrightarrow z\in\operatorname{dom}P_{k,m},
\qquad d(z)=1\Longrightarrow b(z)=P_{k,m}(z).
$$

Each new gate reads only input wires, constants, or earlier gates. Evaluating in gate order therefore produces a transcript satisfying every local gate equation. Conversely, induction on the gate index shows that any transcript satisfying all those equations must equal that evaluation: once the predecessors agree, the truth function fixes the next gate. The later total construction uses this uniqueness to check a purported address locally. Its quantum decoder proposes the address using §3.3; the exact circuit certifies that each address instance is promised and that the corresponding answer is correct. The small-input example below makes the need for both operations explicit.
<!-- /passage:forr_circuit_size -->

<!-- passage:forr_small_instance -->
## 3.5. A complete check of the smallest nontrivial instance

Take $k=2,t=1,m=4$, in coordinate order $00,01,10,11$. Then $M=8$, $\delta=2^{-10}$, and

$$
W=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad
g=\begin{pmatrix}-1\\1\\1\\1\end{pmatrix},\qquad
Wg=\begin{pmatrix}2\\-2\\-2\\-2\end{pmatrix}.
$$

Holding the second block equal to $g$, compute $N=z_0^{\mathsf T}Wg$. This gives three examples with the same normalization and oracle convention:

<!-- claim:R3-FOR-THREE-EXAMPLES -->

| First sign block $z_0$ | First bit block | $N$ | $\Phi$ | $P_{2,4}$ | Projection probability $\Phi^2$ | Exact circuit $(d,b)$ |
| --- | --- | ---: | ---: | --- | ---: | --- |
| $(1,-1,-1,-1)$ | $(0,1,1,1)$ | $8$ | $1$ | $1$ | $1$ | $(1,1)$ |
| $(1,-1,1,1)$ | $(0,1,0,0)$ | $0$ | $0$ | $0$ | $0$ | $(1,0)$ |
| $(-1,1,1,1)$ | $(1,0,0,0)$ | $-8$ | $-1$ | undefined | $1$ | $(0,0)$ |

The common second bit block is $(1,0,0,0)$. On the last input the quantum projection succeeds with certainty and the repeated procedure outputs one, while the circuit correctly reports that the promise fails. This is permitted by Lemma 2.1(ii) and is why the total construction must verify promise membership separately.

We can count all $16^2=256$ inputs without relying on a computer. Each row of $W$ has an even number of negative entries, as does its negative. The eight signed rows are distinct, since distinct Walsh rows are orthogonal, and they exhaust the eight even-parity sign vectors. If $z_1$ is one of them, $Wz_1$ has exactly one nonzero coordinate, equal to $4$ or $-4$. Of the sixteen first blocks, eight give $N=4$ and eight give $N=-4$. These second blocks contribute 64 of each.

The other eight second blocks have odd parity. Their coordinatewise product with any even-parity Walsh row has odd parity, so its four signs sum to $2$ or $-2$. Thus every coordinate of $Wz_1$ is $2$ times a sign. As $z_0$ ranges over all sign vectors, $N$ is twice a sum of four freely chosen signs. For each such $z_1$, the multiplicities at $N=-8,-4,0,4,8$ are $1,4,6,4,1$. Adding the two classes yields

| Numerator $N$ | $-8$ | $-4$ | $0$ | $4$ | $8$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Number of inputs | $8$ | $96$ | $48$ | $96$ | $8$ |

Every positive value is at least $\Phi=1/2>\delta$, every negative value is at most $-1/2<-\delta/2$, and the zero values satisfy the zero case of the promise. Consequently

<!-- claim:NEW-FOR-26 -->
$$
\#P_{2,4}^{-1}(1)=104,\qquad
\#P_{2,4}^{-1}(0)=48,\qquad
\#\{z:P_{2,4}(z)\text{ undefined}\}=104.
$$

The accompanying checker independently compares direct path summation, dense Walsh multiplication, butterfly multiplication, both integer tests, and an append-only Boolean-gate reconstruction on every input at $k=2,t=1$. It also checks all 4,096 inputs at $k=3,t=1$. All arithmetic is integral or rational. These are finite semantic checks; the ordinary proofs above establish the parameterized conclusions.
<!-- /passage:forr_small_instance -->

<!-- passage:forr_current_evidence -->
### Formal support and source scope

The source assessed here is the packet snapshot labeled `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Its timestamped root-build receipt matches all 124 supplied local Lean/configuration files; the relevant integrated helper modules also have source-matched native passes. The supplied audit prints the principal helper theorem types and reports only the permitted Lean axioms. These are inspected records of previous runs. This review did not run Lean or Comparator anew, and no supplied Comparator receipt names the Forrelation helper declarations in this section.

The current wrappers jointly state the normalization, promise, and integer numerator: `construction_walsh_definitions`, `construction_equation_3`, `construction_equation_4`, and `construction_N_phi`. The two threshold equivalences and the actual all-input output rules are split between `construction_integer_tests` and `construction_forr_output_bits`. The coherent physical conclusion is `construction_lemma_2_1_ii_complete`. The circuit endpoint and bound are `Forrelation.exists_circuit` and `construction_lemma_2_1_iii`. The finite census is recorded in `Forrelation.Sanity`.

Two exact correspondences remain narrower than the surrounding ordinary proof: the supplied implementation has a $2qk$, rather than a formally packaged $qk$, bit-query cap; and the arithmetic contracts establish modular representation with correct final signs, rather than a signed interpretation of every intermediate register. Neither qualification weakens Lemma 2.1(ii)–(iii). The packet also contains `construction_lemma_2_1_complete`, a conjunction including the separately proved randomized lower bound; its presence updates the old evidence sentence in §3.17, without supplying a new proof of that lower bound in this section. Exact types, premises, routes, and receipt references are in `correspondence.json` and `LEAN_GAPS.md`.
<!-- /passage:forr_current_evidence -->

<!-- passage:forr_references -->
### References used in these subsections

- **[OAI26]** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026, §2.1, equations (3)–(5), Lemma 2.1(ii)–(iii), pp. 3–5. The supplied PDF is the mathematical source for this assignment; SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`. [Public source link](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).
- **[AA14/18]** Scott Aaronson and Andris Ambainis, *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing*, *SIAM Journal on Computing* **47**(3), 982–1038 (2018), DOI [10.1137/15M1050902](https://doi.org/10.1137/15M1050902). Mathematical locators here refer to the inspected [arXiv:1411.5729v1](https://arxiv.org/abs/1411.5729v1), 21 November 2014: §1.1.3, p. 4; §3.2 and Proposition 6, pp. 13–14. The journal metadata is not a claim that the journal pagination was used for these proofs.
- **[BS20v3]** Nikhil Bansal and Makrand Sinha, *$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity*, [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3), 17 November 2020: equations (1.1)–(1.3), Proposition 1.2, pp. 2–3; Theorem 1.3 and Corollary 1.4, p. 4. Published in *STOC 2021*, 1303–1316, DOI [10.1145/3406325.3451040](https://doi.org/10.1145/3406325.3451040). This section uses the normalized promise and quantum comparison; it does not re-audit the classical lower-bound proof.
<!-- /passage:forr_references -->
