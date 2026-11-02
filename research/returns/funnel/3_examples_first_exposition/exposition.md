# A nearly quartic query separation through worked examples

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

<!-- passage:abstract -->
## Abstract

The optimal universal exponent relating randomized and quantum bit-query complexity of total Boolean functions is four. OpenAI's construction gives, for each fixed integer \(k\ge2\), functions whose randomized complexity grows at least as \(m^{2-1/k}/(\log m)^2\), while their quantum complexity is at most \(\sqrt m\) times a power of \(\log m\). Together with the earlier universal quartic upper bound, these functions exclude every smaller universal exponent. We explain the construction through a complete four-column input, cyclic comparisons, an exact amplitude-amplification calculation, and a two-bit example showing why conditioning on an algorithm's query count can invalidate a lower-bound argument. A column's outward pointers make a genuine winner defeat every opponent whenever its own address is decoded correctly, including opponents with undefined addresses. A quantum tournament finds candidates using this asymmetric guarantee; a classical algorithm must search for a removed zero or discover a hidden certificate address. The result concerns query counts with unrestricted intervening computation. The powers \(4-2/k\) approach four with \(k\) fixed separately for each family; an exact fourth-power separation for one family is not established here. [OpenAI2026, Theorem 1.1; ABKRT2021, Theorem 2.]
<!-- /passage:abstract -->

<!-- passage:opening-board -->
## 1. A complete input with four columns

Consider four columns of bits. Read each column from top to bottom:

| Row | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 | 1 |
| 3 | 1 | 1 | 1 | 0 |
| 4 | 1 | 1 | 1 | 1 |

Write \(X_i\) for the string in column \(i\). Thus \(X_1=1111\), \(X_2=0111\), \(X_3=1011\), and \(X_4=1101\). Column 1 is the only all-one column. It also has pointers that identify the displayed zero in each other column: row 1 in column 2, row 2 in column 3, and row 3 in column 4. The destination column is fixed by the pointer's slot; the pointer stores only a row number.

The function we shall define asks whether some column has both an all-one string and a valid certificate containing such outward pointers. The certificate itself is stored at an address determined by other input bits. We first make every part of this arrangement explicit for a small example. It will be an instance of the general addressed construction in OpenAI's Section 2.2, with an elementary partial function replacing the hard one used in the separation theorem.

A *partial Boolean function* assigns a bit to some inputs and leaves the remaining inputs undefined. For this example use two input bits \(u,v\), with

\[
f(u,v)=
\begin{cases}
v,&u=0,\\
\text{undefined},&u=1.
\end{cases}
\tag{E1}
\]

The first bit says whether an answer is defined; the second supplies the answer when it is. The two-gate circuit with outputs \(d=\neg u\) and \(b=v\) computes domain membership and value exactly. A transcript is the proposed pair of gate values \((d,b)\). On input \(00\) the truthful transcript is \(10\); on input \(11\) it is \(01\).

Each column has two separate copies of the two-bit input, denoted \(A_{i,1},A_{i,2}\). If both partial answers are defined, their ordered pair is the column's *true address*. The four possible address labels are \(00,01,10,11\), and each column has one certificate cell at each label. We choose the address inputs as follows:

| Column \(i\) | \(A_{i,1}\) | \(A_{i,2}\) | True address | Address proposed by reading the \(v\)-bits |
|---|---|---|---|---|
| 1 | 00 | 00 | 00 | 00 |
| 2 | 11 | 11 | undefined | 11 |
| 3 | 00 | 00 | 00 | 00 |
| 4 | 00 | 00 | 00 | 00 |

The proposed address in column 2 is a perfectly usable array index. It is not a vector of defined answers to \(f\). This distinction will persist in the quantum algorithm: a decoding routine must produce an index on every input, although its correctness guarantee applies only when the partial instances are defined.
<!-- /passage:opening-board -->

<!-- passage:complete-cells -->
Each cell stores three pointers, one toward every other column, and two two-bit transcripts, one for each address input. Encode row numbers \(1,2,3,4\) by \(00,01,10,11\), respectively. The following table specifies the pointers. Its entries are row numbers in the indicated destination column.

| Source column | Toward 1 | Toward 2 | Toward 3 | Toward 4 |
|---|---:|---:|---:|---:|
| 1 | absent | 1 | 2 | 3 |
| 2 | 1 | absent | 2 | 1 |
| 3 | 1 | 2 | absent | 3 |
| 4 | 1 | 1 | 1 | absent |

In every cell of a given column, repeat its row of pointers and the truthful transcripts for its two address inputs. This repetition specifies all sixteen cells, including those never used by the proposed decoding. Within a cell, put the pointers in increasing destination-column order, followed by the two transcripts. The resulting cell words are:

| Column | Cell contents at each of \(00,01,10,11\) |
|---|---|
| 1 | 0001101010 |
| 2 | 0001000101 |
| 3 | 0001101010 |
| 4 | 0000001010 |

For example, column 1's word splits as \(00\mid01\mid10\mid10\mid10\): three row pointers and two transcripts. The entire input has sixteen \(X\)-bits, sixteen address-input bits, and sixteen ten-bit cells:

\[
16+16+16\cdot10=192\quad\text{input bits}.
\tag{E2}
\]

A column *wins at address \(s\)* when its own string is all ones, its two partial answers are defined and equal \(s\), the transcripts in cell \(s\) are correct, and that cell's outward pointers all land on zeros. Our example has a winner at column 1, address \(00\). In particular,

\[
X_2[1]=X_3[2]=X_4[3]=0.
\tag{E3}
\]

Column 2's truthful transcripts record undefined inputs, since each has \(d=0\). Truthfulness alone therefore does not make a certificate accepting. Columns 3 and 4 have defined addresses and truthful transcripts, but their own strings contain zeros. All the input bits have been specified, and the function's value is one.

There can be at most one winning column in any input. If \(i\) wins, its pointer toward each \(j\ne i\) certifies a zero in \(X_j\). That prevents \(j\) from being all ones. Moreover, a winning column has a unique true address because a defined partial function has one value on each of its inputs. These conclusions do not require correctness of any other column's proposed address. [OpenAI2026, Section 2.2.]
<!-- /passage:complete-cells -->

<!-- passage:local-checks -->
### Checking a fixed cell

At a specified column and address, verification consists of small tests. In our example, check the four bits of its own \(X\)-string, the three outward pointers, and the four claimed gate values. Finally, for each transcript require \(d=1\) and require \(b\) to equal the corresponding address bit. The number of tests is

\[
4+3+2(2+2)=15.
\tag{E4}
\]

A pointer test reads its two pointer bits and one destination bit. A gate test compares one claimed gate output with its actual input bit. The address inputs themselves are part of the input; their values are never accepted merely because the transcript says so.

At the proposed addresses from the first table, the numbers of failing tests are:

| Column | Proposed address | Failing tests |
|---|---|---:|
| 1 | 00 | 0 |
| 2 | 11 | 5 |
| 3 | 00 | 3 |
| 4 | 00 | 3 |

Column 2 fails its own-string test at row 1, its pointer tests toward columns 1 and 4, and both domain-output tests. Its gate transcripts remain truthful. This accounts for all five failures without treating undefinedness as an instruction to stop evaluating the total function.

For a general fan-in-two circuit with \(S\) non-input gates, \(r\) address instances and \(m\) columns of length \(m\), the same verification uses

\[
K=m+(m-1)+r(S+2)
\tag{1}
\]

tests. Each gate test reads at most three bits. Each pointer test reads \(\log_2m\) pointer bits and one destination bit when \(m\) is a power of two. Passing every gate test forces a transcript to equal the actual circuit evaluation, by induction through the gates. The output tests then certify both definedness and the proposed address. Consequently all tests pass exactly at a winning column's true address. [OpenAI2026, Lemma 2.2.]
<!-- /passage:local-checks -->

<!-- passage:comparisons-and-false-positive -->
### Comparing two columns

Use the following comparison rule. Propose an address for each column; at those addresses, read each column's pointer toward the other. A column *disqualifies* its opponent when its pointer finds a zero there. If exactly one disqualifies the other, choose that column. If both or neither do, choose the smaller column index.

Column 1 disqualifies every opponent in our input. No opponent can disqualify it, because every possible row of \(X_1\) contains one. This includes column 2, whose proposed address \(11\) has no relation to a defined partial answer. The comparison never checks column 2's transcripts. The all-one target string itself prevents any purported pointer from finding a zero.

The comparison outcomes among the remaining columns form a cycle: column 2 defeats 3, column 3 defeats 4, and column 4 defeats 2. For example, column 2 points to row 2 of column 3, which is zero, while column 3 points to row 2 of column 2, which is one. The other two edges follow by the same explicit pointer tests. There is no consistent ranking of these three columns.

An additional modification explains the eventual need for verification. Change column 1's pointer toward column 2 at its proposed cell \(00\) from row 1 to row 2. That pointer now lands on one, so column 1 loses its winner status. The other columns still contain zeros, giving function value zero. Nevertheless, column 1 still wins every comparison. Against column 2, neither side disqualifies the other and the smaller-index rule chooses column 1; its comparisons with columns 3 and 4 are unchanged.

Thus pairwise dominance does not certify the function value. The comparison procedure supplies candidates, whose full certificates must subsequently be checked. In this modified cell exactly one local test fails. The distinction is already visible in 192 bits. [OpenAI2026, Section 3.3; the particular input and modification are computed here.]
<!-- /passage:comparisons-and-false-positive -->

<!-- passage:query-model -->
## 2. Queries and a tournament with a cycle

A classical *bit query* selects one physical input position and reads its bit. An algorithm can choose its next position using earlier answers. Randomized algorithms may also use random coins. Their cost is the maximum number of queries on any input and any random branch; correctness requires error at most \(1/3\) on each input.

A quantum state is represented by a unit vector with complex coordinates. The squared magnitude of a coordinate is the probability of observing its basis label. We write \(\lvert j,b,z\rangle\) for one such basis vector. A quantum query is the reversible operation

\[
O_x\lvert j,b,z\rangle=\lvert j,b\mathbin{\oplus}x_j,z\rangle,
\tag{2}
\]

where \(j\) is an input position, \(b\) a bit and \(z\) a workspace label. The same operation acts linearly on superpositions. It does not reveal a list of all the queried bits: measurement produces an outcome according to squared amplitudes, and subsequent interference determines which outcomes become likely. Quantum cost is also a bound on every branch, including branches created by measurement.

We write \(R(F)\) and \(Q(F)\) for the least randomized and quantum query costs under these conventions. Computation between queries is unrestricted. The address arithmetic, circuit wiring and rules of the problem are known to the algorithm, while the stored pointer bits, address inputs and transcripts must be queried. The input's total length is much larger than \(m\); \(m\) counts columns and the length of each \(X_i\), not all input bits. These conventions are those of [OpenAI2026, Section 1].
<!-- /passage:query-model -->

<!-- passage:cycle-weights -->
Return to the unmodified four-column input. Let \(a_{ij}\) be the probability that column \(i\) defeats column \(j\), with \(a_{ii}=0\). Here every comparison is deterministic, so

\[
(a_{ij})=
\begin{pmatrix}
0&1&1&1\\
0&0&1&0\\
0&0&0&1\\
0&1&0&0
\end{pmatrix}.
\tag{E5}
\]

The tournament maintains nonnegative weights. Initially all four weights are one. At each stage, choose a *pivot* with probability proportional to its weight, record it, and multiply every candidate's weight by its probability of defeating that pivot. A chosen pivot acquires weight zero because self-comparison has value zero. If the total weight becomes zero, the process stops.

The first-stage calculation is:

| Pivot | Pivot probability | New weights | New total |
|---|---:|---|---:|
| 1 | \(1/4\) | \((0,0,0,0)\) | 0 |
| 2 | \(1/4\) | \((1,0,0,1)\) | 2 |
| 3 | \(1/4\) | \((1,1,0,0)\) | 2 |
| 4 | \(1/4\) | \((1,0,1,0)\) | 2 |

Writing \(W_t\) for total weight after \(t\) stages, we obtain

\[
\mathbb E W_1=\frac{0+2+2+2}{4}=\frac32.
\tag{E6}
\]

If the first pivot is a loser, column 1 and one loser remain, each with weight one. The next pivot selects column 1 with probability \(1/2\); if it selects the loser, column 1 is then the only survivor. The probabilities that column 1 is still absent from the recorded list after one, two and three pivots are therefore

\[
\frac34,\qquad\frac38,\qquad0.
\tag{E7}
\]

The cyclic comparisons cause no difficulty for this calculation. The procedure does not repeatedly move to a supposedly better candidate in a ranking. Its analysis follows the total remaining weight and the weight of the genuine winner.
<!-- /passage:cycle-weights -->

<!-- passage:drift -->
For the general calculation, suppose \(0\le a_{ij}\le1\), \(a_{ii}=0\), and \(a_{ij}+a_{ji}=1\) for distinct candidates. Given current weights \(w_i\ge0\), put \(W=\sum_iw_i\). When \(W>0\), the update after choosing pivot \(p\) is \(w'_i=w_i a_{ip}\), with pivot probability \(w_p/W\). Its expected total is

\[
\begin{aligned}
\mathbb E[W'\mid w]
 &=\frac1W\sum_{p,i}w_pw_i a_{ip}\\
 &=\frac{W^2-\sum_iw_i^2}{2W}
 \le\frac W2.
\end{aligned}
\tag{3}
\]

To see the middle equality, pair the term indexed by \((i,p)\) with the term indexed by \((p,i)\). Their probabilities add to one. Diagonal terms vanish. This pairing uses no transitivity and no preference for probabilities far from \(1/2\). If \(W=0\), define the next weights to remain zero; the inequality still holds without dividing by zero.

Suppose a distinguished candidate defeats each opponent with probability at least \(1-\epsilon\). Until it has itself been selected, its weight after \(t\) stages is at least \((1-\epsilon)^t\). Meanwhile, starting from \(m\) unit weights, repeated use of (3) gives \(\mathbb E W_t\le m/2^t\). A persistent candidate of weight at least \(1/2\) can therefore remain unselected only on an event whose probability is at most \(2m/2^t\). This follows directly from \(\mathbb EW_t\ge\frac12\Pr(W_t\ge\frac12)\). [OpenAI2026, Proposition 3.2, equations (12)–(14).]
<!-- /passage:drift -->

<!-- passage:fractional-example -->
Fractional weights matter even in a four-candidate example. Consider a separate abstract comparator in which candidate 1 defeats every opponent, and each pair of losers is decided by a fair coin. This comparator is not asserted to arise from the preceding input. After pivot 2 the weights are \((1,0,1/2,1/2)\), so the next pivot distribution is

\[
(1/2,0,1/4,1/4).
\tag{E8}
\]

If pivot 3 follows, the weights become \((1,0,0,1/4)\), giving candidate 1 probability \(4/5\) at the next stage. The miss probabilities after one through four stages are \(3/4,3/8,3/40,0\). At the intermediate weight vector \((1,0,1/2,1/2)\), formula (3) gives expected next total \(5/8\): selecting candidate 1 yields zero; selecting either remaining loser yields \(5/4\). The event of selecting candidate 1 and the event of selecting either remaining loser each have probability \(1/2\).

A quantum implementation must sample these particular distributions. Merely finding some candidate that can defeat previous pivots would provide a different process, to which the drift proof need not apply.
<!-- /passage:fractional-example -->

<!-- passage:amplification-example -->
## 3. Increasing success without changing the candidate law

Take three mutually orthogonal unit states, \(\lvert g_1\rangle,\lvert g_2\rangle,\lvert b\rangle\). The first two count as successful outcomes. Prepare

\[
\lvert\psi\rangle=
\frac3{10}\lvert g_1\rangle+
\frac4{10}\lvert g_2\rangle+
\frac{\sqrt3}{2}\lvert b\rangle.
\tag{E9}
\]

The squared amplitudes sum to one. Success has probability \(9/100+16/100=1/4\). Conditional on success, the normalized state is

\[
\lvert g\rangle=\frac35\lvert g_1\rangle+\frac45\lvert g_2\rangle,
\qquad
\Pr(g_1\mid\text{success})=\frac9{25},\quad
\Pr(g_2\mid\text{success})=\frac{16}{25}.
\tag{E10}
\]

Amplitude amplification increases the coefficient of this whole successful component. In this example a single Grover iteration makes success certain and produces \(\lvert g\rangle\). The two successful outcomes keep their unequal probabilities \(9/25\) and \(16/25\).

One can verify the iteration without numerical trigonometry. If the initial success probability is \(p\), the reflection pair multiplies each successful amplitude by \(3-4p\) and each unsuccessful amplitude by \(1-4p\). At \(p=1/4\), these factors are two and zero, respectively. Applying them to (E9) gives (E10). The accompanying program also performs the two reflections directly using exact arithmetic with numbers \(a+b\sqrt3\), where \(a,b\) are rational.
<!-- /passage:amplification-example -->

<!-- passage:amplification-general -->
In general, a preparation \(A\) with success probability \(0<p<1\) has a decomposition

\[
A\lvert0\rangle=\sin\theta\lvert g\rangle+
\cos\theta\lvert b\rangle,\qquad
p=\sin^2\theta,\quad0<\theta<\pi/2.
\tag{4}
\]

Here the two unit vectors are the normalized projections onto the successful and unsuccessful subspaces. Alternating reflections preserves their two-dimensional span. After \(j\) Grover iterations, the state is

\[
\sin((2j+1)\theta)\lvert g\rangle+
\cos((2j+1)\theta)\lvert b\rangle.
\tag{5}
\]

Whenever a successful outcome occurs, normalization leaves \(\lvert g\rangle\) up to a common phase. Every internal distinction between successful outcomes, including a candidate label and retained workspace, remains in that same state. This is the rotation calculation of Brassard, Høyer, Mosca and Tapp, Section 2, Lemma 1 and equation (8). [BHMT2002.]

The tournament does not know \(p\), and repeatedly trying until success would give an unbounded worst-case cost. OpenAI's Lemma 3.1 instead fixes \(0<\gamma\le1/2\) and an allowed failure probability \(0<\eta<1/2\), and gives a procedure using \(O(\gamma^{-1/2}\log(1/\eta))\) calls to \(A,A^{-1}\) on every branch. If \(p\ge\gamma\), it reports failure with probability at most \(\eta\). Conditional on success, it still produces the same \(\lvert g\rangle\). If \(p=0\), it always reports failure.

For completeness, the finite stopping rule has a simple quantitative explanation. Choose \(M=\lceil10/\sqrt\gamma\rceil\). With probability \(1/2\), perform no Grover iterations; otherwise choose their number uniformly from \(0,\ldots,M-1\). For \(p\ge1/2\) the first option alone succeeds with probability at least \(1/4\). For \(\gamma\le p\le1/2\), summing the squared sines in (5) bounds the second option's conditional success probability below by \(9/20\). A complete trial therefore succeeds with probability at least \(9/40\). A fixed number of independent trials makes failure at most \(\eta\), using the factor \(31/40\) for each failed trial. Every successful trial has the same normalized successful component, so randomizing the iteration count and stopping at the first success preserve its distribution. [OpenAI2026, Lemma 3.1, equation (9); BBHT1998, Section 4.]
<!-- /passage:amplification-general -->

<!-- passage:weighted-quantum-sampling -->
We can now implement the tournament weights without calculating their numerical values. Fix an input and a history of pivots \(p_1,\ldots,p_t\). Start with a uniform superposition of candidate labels. For each pivot, compare the candidate against it, using a fresh workspace for that comparison. Retain all the results and other workspace, and declare success when every comparison says that the candidate wins.

For a fixed candidate \(i\), these workspaces form a tensor product. Its conditional probability of passing every comparison is therefore \(\prod_{b=1}^t a_{ip_b}=w_i\). Distinct candidate labels are orthogonal. Consequently

\[
\Pr(\text{success})=\frac Wm,\qquad
\Pr(i\mid\text{success})=\frac{w_i}{W}
\quad(W>0).
\tag{6}
\]

This is the required pivot law. Fresh workspaces justify multiplying the success probabilities; retaining those workspaces permits reversal of the preparation. Discarding them prematurely would remove the reversible operation required by amplification. The successful state may contain substantial workspace correlated with the candidate. The calculation preserves that state before the candidate is measured.

As long as the distinguished candidate has not been selected and \(t\epsilon\le1/2\), its surviving weight is at least \(1/2\). Thus \(W/m\ge1/(2m)\), and bounded amplification can supply a pivot in \(O(\sqrt m\log(1/\eta))\) preparation calls with a prescribed failure allowance. The complete algorithm may stop if the sampler fails. At each fixed pivot history, conditional on that stage succeeding, its next pivot has exactly the ideal law already analyzed. Conditioning on the algorithm's entire history of successful sampling is unnecessary. [OpenAI2026, Proposition 3.2, equation (15) and its proof.]

The supplied formal implementation proves the successful candidate law directly. Its general theorem about preservation of the whole successful state is a separate result; the algorithm's proof uses the law of the measured label.
<!-- /passage:weighted-quantum-sampling -->

<!-- passage:and-example -->
## 4. A query cap cannot be imposed by conditioning

The classical lower bound will need to show that an algorithm cannot guess a whole address after making few queries to its inputs. Adaptivity creates a difficulty: whether a column receives few queries can itself reveal information about the answers. A two-bit example isolates this problem.

Let \(P(a,b)=a\land b\), with all four two-bit inputs equally likely. An algorithm restricted to one query has maximum success probability \(3/4\). If it queries \(a\), then observing zero settles the answer; observing one leaves the independent bit \(b\) unknown. The best conditional success probabilities are one and \(1/2\), respectively, giving \((1+1/2)/2=3/4\). Querying \(b\) is symmetric. Answering zero without a query already achieves the same success probability, and randomizing these choices cannot improve the optimum.

Now allow the following algorithm to make a second query: read \(a\); if it is zero, return zero; otherwise read \(b\) and return \(b\).

| Input | Queries made | Output | Correct? | At most one query? |
|---|---:|---:|---|---|
| 00 | 1 | 0 | yes | yes |
| 01 | 1 | 0 | yes | yes |
| 10 | 2 | 0 | yes | no |
| 11 | 2 | 1 | yes | no |

This algorithm is always correct. Let \(E\) be the event that it uses at most one query. We have

\[
\Pr(E)=\frac12,\qquad
\Pr(\text{correct}\mid E)=1>\frac34,\qquad
\Pr(E\text{ and correct})=\frac12.
\tag{E11}
\]

Conditioning has retained exactly the inputs on which the first observed bit settles the answer. The original one-query hardness bound concerns the uniform distribution on all four inputs. It does not bound the conditional success probability under this changed distribution.

Instead, modify the algorithm itself: abort before the second query and output zero on an aborted run. This simulator respects the one-query cap on every input. It succeeds on \(00,01,10\) and fails on \(11\), so its success probability is \(3/4\). Whenever the original algorithm is both correct and within its cap, the simulator has followed the same queries and is correct too. This implication bounds a joint event without conditioning away the hard inputs.

With two independent copies, the event that both original runs stay within their caps has probability \(1/4\); both answers are then correct. The two capped simulators are correct together with probability \(9/16\). The script checks the optimal value \(9/16\) even when queries to the two copies may be interleaved adaptively, with at most one query to each copy. These are finite examples of the distinction used in [OpenAI2026, Section 4.2, equation (21)].
<!-- /passage:and-example -->

<!-- passage:capped-product -->
### Independent inputs under adaptive scheduling

Here is the general fact. Let \(\mu\) be a distribution supported on the domain of a partial Boolean function \(P\), and suppose every deterministic algorithm making at most \(L\) queries computes \(P\) under \(\mu\) with probability at most \(\beta\). For \(r\) independent samples \(U_1,\ldots,U_r\) from \(\mu\), an algorithm making at most \(L\) queries to each input, on every branch, satisfies

\[
\Pr\bigl(\text{all }r\text{ answers are correct}\bigr)\le\beta^r.
\tag{7}
\]

The algorithm may choose which input to query next using everything observed so far. It may be randomized and may receive extra information jointly independent of the entire tuple \((U_1,\ldots,U_r)\). The restrictions are separate query caps and independence before the queries begin. This is the capped form of the direct-product argument developed by Drucker, following Shaltiel, and stated as OpenAI's Lemma 4.1. [Drucker2012, Section 1.3 and Lemmas 3.1–3.2; Shaltiel2003.]

To understand the proof, fix the independent extra information and the random coins. At a complete observed transcript, the constraints on the inputs say that certain coordinates of \(U_1\) have certain values, certain coordinates of \(U_2\) have certain values, and so on. Any tuple satisfying those constraints follows the same schedule, because each next query was determined by the earlier answers. The transcript event is therefore a product of separate constraints. Conditional on that transcript, the inputs remain independent, although their individual distributions have changed.

For each input, consider the best conditional success probability obtainable using its remaining allowance of queries. Denote these values by \(V_1,\ldots,V_r\). A query to input \(h\), followed by optimal continuation, is one permissible strategy in the definition of \(V_h\). Thus the conditional expected new value of \(V_h\) is at most its current value. The other values are unchanged. Consequently the product \(\prod_h V_h\) cannot increase in conditional expectation.

Initially each value is at most \(\beta\). At the end, conditional independence bounds the probability that the selected answer vector is correct by the product of the best remaining single-input success probabilities, and hence by \(\prod_hV_h\). Averaging proves (7). The individual values may rise on particular informative branches; only the expected product is controlled. This is why the argument survives adaptive scheduling while the conditional estimate in (E11) fails.

The supplied Lean proof of (7) uses induction with finite nonnegative input weights in place of this conditional-expectation argument. It establishes the capped statement used here by an alternative proof. Its probability estimates do not assume that the algorithm's decision to remain under a cap is independent of the input.
<!-- /passage:capped-product -->

<!-- passage:planted-example -->
## 5. Creating a winner by changing one column

We next make a zero-input and a nearby one-input. Use the same two-bit partial function and the same four-column layout as Section 1, but set every address input to \(00\), and initially set every cell bit to zero. Put one zero in each \(X_i\), at row numbers

\[
(J_1,J_2,J_3,J_4)=(4,1,2,3).
\tag{E12}
\]

The dummy input has strings \(1110,0111,1011,1101\). Every column has a zero, so none can win. All addresses are defined and equal \(00\), but this does not change the function value.

Choose column \(I=1\). Erase its zero by setting \(X_1[4]=1\), and fill cell \(B_{1,00}\) with the truthful transcripts and pointers to the other columns' zeros. That cell's word is \(0001101010\), exactly as in Section 1. Leave all other cells blank. The resulting input has a unique winner at column 1, address \(00\).

The two inputs differ at exactly five physical bits: the erased zero, two pointer bits in the newly filled cell, and its two domain-transcript bits. Some bits in that cell remain equal to their blank value. The pair differs from the opening example, where all cells in each column repeated a specified word and column 2 had undefined address inputs.

A deterministic algorithm receiving these two inputs gets identical answers until it queries either the erased-zero position or a bit of the filled cell that has changed. Its next query before that point is identical in both runs, because the whole earlier transcript is identical. Therefore a difference in output requires visiting one of those locations. Counting every visit to the filled cell gives a convenient upper bound, even when the particular queried bit is unchanged.

The finite checker verifies this construction for every choice of the four zero positions, planted column and two-bit target address. This enumeration checks the local mechanism. It supplies no classical hardness bound for the elementary partial function.
<!-- /passage:planted-example -->

<!-- passage:planted-distribution -->
For the lower bound, make the zero locations independent and uniform among the \(m\) rows, and choose the planted column \(I\) uniformly and independently. Generate all address inputs independently from a distribution under which computing the partial answer is hard. The dummy input still has one zero per column and blank cells. Planting erases \(X_I[J_I]\) and fills exactly \(I\)'s true-address cell with correct transcripts and pointers to the other hidden zeros.

On the dummy input, the algorithm's execution is independent of \(I\). This is the useful direction in which to analyze the pair: the selected column does not exist as visible input data during that run. The one-input is obtained only afterward through the coupling just described. In particular, the algorithm's observations of the dummy input can guide its choice of columns to inspect without changing the independent uniform choice of \(I\).

The two ways to distinguish the inputs have different costs. Discovering the erased zero means finding the hidden zero in the randomly selected column during the dummy run. Reaching the filled cell means either investing enough queries to learn that column's address or correctly guessing an entire vector of hard answers. Separate certificate arrays are essential: a cell query belongs to a particular column as well as to an address within it. [OpenAI2026, Section 4.2.]
<!-- /passage:planted-distribution -->

<!-- passage:forrelation-example -->
## 6. Replacing the toy address function by Forrelation

The construction above becomes a separation when quantum algorithms can compute its partial answers cheaply and classical algorithms require many queries. The required partial function is \(k\)-fold Forrelation, introduced by Aaronson and Ambainis [AA2018, Section 1.1.3]. A small matrix calculation will fix its normalization and explain what an undefined input can look like.

For \(m=4\), use the normalized Walsh–Hadamard matrix

\[
H=\frac12
\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad
v=(1,1,1,-1)^{\mathsf T}.
\tag{E13}
\]

Its rows are orthonormal, and direct multiplication gives \(Hv=v\). Represent an input bit \(a\) by the sign \((-1)^a\). For two sign vectors, define \(\Phi(z_1,z_2)=\frac14z_1^{\mathsf T}Hz_2\). The order-two promise uses \(\delta=2^{-10}=1/1024\): output one when \(\Phi\ge\delta\), output zero when \(|\Phi|\le\delta/2\), and leave the other inputs undefined.

| \(z_1\) | \(z_2\) | \(z_1^{\mathsf T}Hz_2\) | \(\Phi\) | Partial answer | Projection probability \(\Phi^2\) |
|---|---|---:|---:|---|---:|
| \((1,1,1,-1)\) | \(v\) | 4 | 1 | 1 | 1 |
| \((1,1,-1,1)\) | \(v\) | 0 | 0 | 0 | 0 |
| \((-1,-1,-1,1)\) | \(v\) | \(-4\) | \(-1\) | undefined | 1 |

The third row has the same projection probability as the first. A decoder based on this experiment can therefore propose one confidently on an undefined input. This is permitted by the partial problem's specification, and explains why a proposed address cannot by itself certify domain membership.

For an exact circuit calculation, put \(W=2H\), whose entries are integers. The numerator \(N=z_1^{\mathsf T}Wz_2\) takes values \(8,0,-8\) in the three rows, and \(\Phi=N/8\). The domain and value circuit tests

\[
2^{10}N\ge8,\qquad 2^{11}|N|\le8.
\tag{E14}
\]

Let \(b\) be the first test and \(d\) the disjunction of the two tests. Its output pairs \((d,b)\) are \((1,1),(1,0),(0,0)\). The undefined negative input therefore has truthful domain output zero, exactly as column 2 did in the toy construction.

The script enumerates all \(16\cdot16=256\) sign-vector pairs. It finds 104 one-inputs, 48 zero-inputs, and 104 undefined inputs, and verifies that the rational and integer definitions agree on every pair. These values illustrate equations (3)–(4) and Lemma 2.1 of [OpenAI2026]; the general Forrelation normalization and promise also appear in [BansalSinha2021, equations (1.1)–(1.3)].
<!-- /passage:forrelation-example -->

<!-- passage:forrelation-general -->
For general \(m\), a power of four, let \(H\) be the normalized Walsh–Hadamard matrix of order \(m\), and let \(u=m^{-1/2}(1,\ldots,1)^{\mathsf T}\). For a sign vector \(z\), write \(D_z\) for the diagonal matrix with entries \(z\). Given \(k\) sign vectors, define

\[
\Phi(z_1,\ldots,z_k)
=u^{\mathsf T}D_{z_1}H D_{z_2}H\cdots H D_{z_k}u,
\qquad \delta=2^{-5k},
\tag{8}
\]

and

\[
P_{k,m}(z)=
\begin{cases}
1,&\Phi(z)\ge\delta,\\
0,&|\Phi(z)|\le\delta/2,\\
\text{undefined},&\text{otherwise}.
\end{cases}
\tag{9}
\]

There are \(k-1\) occurrences of \(H\). Each diagonal matrix and \(H\) preserves Euclidean length, so \(|\Phi|\le1\). For fixed \(k\), the gap between the two promised projection probabilities is a positive constant independent of \(m\). Preparing \(u\), applying the matrices in right-to-left order, and testing projection onto \(u\) gives success probability \(\Phi^2\). A diagonal sign operation uses one phase query, obtainable from the bit oracle; the intervening Hadamard operations use none. Repetition separates the probabilities at least \(\delta^2\) and at most \(\delta^2/4\). Error at most \(\eta\) therefore costs \(O_k(1+\log(1/\eta))\) queries. The constants can depend strongly on \(k\). [OpenAI2026, Lemma 2.1(ii).]

Bansal and Sinha's lower bound, Theorem 1.3 and Corollary 1.4, gives, at fixed \(k\) and error \(1/3\), a randomized lower bound of order \((m/\log(km))^{1-1/k}\), with a positive constant depending on \(k\). It implies the weaker estimate needed here:

\[
R(P_{k,m})>L,\qquad
L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor
\tag{10}
\]

for all sufficiently large powers of four \(m\). The supplied Lean development proves this fixed-\(k\) estimate by another argument; its statement does not assert the full parameter dependence of Bansal and Sinha's theorem. [BansalSinha2021; OpenAI2026, Lemma 2.1(i).]

An exact circuit still determines the domain and value on every input. Using the integer matrix \(W=\sqrt m\,H\), the numerator of (8) is integral and its denominator is \(M_{k,m}=m(\sqrt m)^{k-1}\). A power of four makes \(\sqrt m\) an integer. The two comparisons become \(2^{5k}N\ge M_{k,m}\) and \(2^{5k+1}|N|\le M_{k,m}\). Walsh–Hadamard transforms use \(O(m\log m)\) additions and subtractions; the intermediate integers require \(O_k(\log m)\) bits. Implementing those operations with fan-in-two gates gives circuit size \(S=O_k(m(\log m)^2)\). This circuit supplies transcripts for the same local checks as Section 1. [OpenAI2026, Lemma 2.1(iii).]
<!-- /passage:forrelation-general -->

<!-- passage:hard-family-parameters -->
The hard total function uses \(m\) columns, \(r=20\log_2m\) separate address instances per column, and \(2^r\) cells in each column. Since \(m\) is a power of four, this \(r\) is already an integer. A column wins exactly when its string is all ones and its true-address cell contains correct transcripts and outward pointers to zeros in every other column. Call the resulting total function \(F_{k,m}\). All strings of physical input bits are allowed; an undefined address input simply prevents its column from winning.

For comparison with the opening example, the theorem's choice \(k=2,m=4\) gives

\[
r=40,\qquad 2^r=1{,}099{,}511{,}627{,}776,\qquad L=0.
\tag{E15}
\]

Even its smallest nontrivial four-column layout has over a trillion cells per column. The opening construction reduced \(r\) to two and replaced Forrelation by (E1) so every cell could be specified by hand. Its role is to explain the winner predicate and the comparison procedure. The asymptotic assertion (10) applies beyond a sufficiently large threshold; at this small parameter, \(L=0\) would yield \(G=0\) in the total-function lower bound below and gives no quantitative separation.

Addressed transcripts are part of the cheat-sheet framework of Aaronson, Ben-David and Kothari, with a preceding construction of Ben-David; pointer functions were developed by Göös, Pitassi and Watson and by Ambainis and collaborators. OpenAI's construction combines separate address arrays with outward zero witnesses and probabilistic comparisons that tolerate undefined opponents. [ABK2016, Sections 3.1–3.2 and 6.1; BenDavid2015, Section 3.1; GPW2015; ABBLSS2017; OpenAI2026, Section 2.]
<!-- /passage:hard-family-parameters -->

<!-- passage:main-theorem -->
## 7. The separation theorem

We can now state the result with its parameters. All logarithms below are to base two. The constants in the family bounds may depend on the fixed integer \(k\); the constant in the universal bound is independent of the function and its input length.

**Theorem (OpenAI, 2026, Theorem 1.1).** For total Boolean functions \(F:\{0,1\}^n\to\{0,1\}\), with \(n\ge1\), let \(R(F)\) and \(Q(F)\) count worst-case bit queries with error at most \(1/3\) on every input. There is an absolute constant \(C>0\) such that

\[
R(F)\le C(1+Q(F))^4
\tag{11}
\]

for every such function. For each fixed integer \(k\ge2\), there are constants \(c_k,C_k,b_k>0\) and, for all sufficiently large powers of four \(m\), total functions \(F_{k,m}\) of the addressed form above such that

\[
Q(F_{k,m})\le C_k\sqrt m\,(\log m)^{b_k},
\qquad
R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log m)^2}.
\tag{12}
\]

In particular, define the optimal universal exponent by

\[
\alpha_{\mathrm{tot}}
=\inf\left\{\alpha\ge0:
\begin{array}{l}
\text{some }C_\alpha>0\text{ satisfies }\\
R(F)\le C_\alpha(1+Q(F))^\alpha
\text{ for every total Boolean }F
\end{array}
\right\},
\tag{13}
\]

The conclusion is \(\alpha_{\mathrm{tot}}=4\). The universal upper bound in (11) is the earlier result of Aaronson, Ben-David, Kothari, Rao and Tal; the family lower bounds are OpenAI's contribution. [ABKRT2021, Theorem 2; OpenAI2026, Theorem 1.1.]

The input length of \(F_{k,m}\) is determined by its full arrays. It need not equal \(m\). The additive one in (11) and (13) includes constant functions, whose query complexities are zero.
<!-- /passage:main-theorem -->

<!-- passage:exponent-table -->
The exponents can be read before accounting for logarithms. The quantum upper bound has \(m\)-power \(1/2\), while the randomized lower bound has \(m\)-power \(2-1/k\). Dividing the latter by \(1/2\) gives:

| Fixed \(k\) | Randomized lower-bound power in \(m\) | Power relative to \(\sqrt m\) |
|---:|---:|---:|
| 2 | \(3/2\) | \(3\) |
| 3 | \(5/3\) | \(10/3\) |
| 4 | \(7/4\) | \(7/2\) |
| 5 | \(9/5\) | \(18/5\) |
| 10 | \(19/10\) | \(19/5\) |
| 20 | \(39/20\) | \(39/10\) |
| 100 | \(199/100\) | \(199/50\) |

The last column is \(4-2/k\). These entries compare the powers in proved bounds; they do not assert matching asymptotic formulas for either query complexity. Already \(k=3\) yields a power strictly above three. The logarithmic losses will disappear from the comparison with any strictly smaller power as \(m\) grows.
<!-- /passage:exponent-table -->

<!-- passage:quantum-comparison-proof -->
## 8. Proof of the two bounds

### Quantum queries: compare first, then verify

Fix an arbitrary physical input to \(F_{k,m}\). It may contain undefined Forrelation instances and incorrect transcripts. Decode a column's \(r\) address instances with error allowance \(\epsilon/r\) each. If all its partial answers are defined, a union bound makes the whole address correct with probability at least \(1-\epsilon\). Otherwise the routine still outputs an address, with the same fixed query cap. With \(\epsilon\) chosen in (15), fixed \(k\) and logarithmic \(r\), decoding costs a power of \(\log m\).

Compare two distinct columns by the rule from Section 1: decode both addresses, inspect the two outward pointers, and choose the sole disqualifier or the smaller index in a tie. For each unordered pair, use a single circuit with its indices sorted; report its winner in either ordered presentation. This ensures \(a_{ij}+a_{ji}=1\). Independently designed circuits for the two orderings would not by themselves give that identity.

If \(i^*\) is a genuine winner, its all-one string prevents every opponent from disqualifying it. Whenever its own address is decoded correctly, its pointer disqualifies the opponent. Thus

\[
a_{i^*j}\ge1-\epsilon\qquad(j\ne i^*).
\tag{14}
\]

The opponent's decoding can behave arbitrarily. The guarantee comes from the two pointer directions checked explicitly on our toy input. The comparison circuit retains its workspace and has cost \(c\) bounded by a power of \(\log m\). [OpenAI2026, Section 3.3.]
<!-- /passage:quantum-comparison-proof -->

<!-- passage:quantum-tournament-proof -->
Choose

\[
T=\lceil\log_2(1000m)\rceil,\qquad
\epsilon=\frac1{1000T}.
\tag{15}
\]

Run at most \(T\) tournament stages. Until the genuine winner is selected, its ideal weight is at least \(1-T\epsilon=999/1000>1/2\). Section 2's drift calculation bounds its ideal miss probability by \(2m/2^T\). Section 3's sampler, with threshold \(1/(2m)\) and failure allowance \(\epsilon\), adds at most \(T\epsilon\) probability of stopping before finding it.

This last estimate uses a coupling at each fixed pivot history. On sampler success, choose the same pivot as in the ideal process. Before the winner is selected, the probability of sampler failure at that history is at most \(\epsilon\). Summing over the at most \(T\) stages bounds the probability of divergence. No assertion that failure probabilities are independent of the previous pivots is required.

At stage \(t\), comparing a candidate against the earlier pivots costs \(O(c(t+1))\) queries per preparation. Bounded amplification uses \(O(\sqrt m\log(1/\epsilon))\) preparation and inverse calls. Summing these costs gives

\[
O(c\sqrt m\,T^2\log T)
\tag{16}
\]

queries for a list of at most \(T\) candidates. The bound holds on every branch, even when no winner exists. This is OpenAI's Proposition 3.2. Its abstract list guarantee is stated more directly in the paper than in the supplied formal implementation, which combines the candidate recursion with the eventual verifier.
<!-- /passage:quantum-tournament-proof -->

<!-- passage:quantum-verification-proof -->
For each listed candidate, decode an address afresh and search the \(K\) local tests for a failure. The circuit-size bound and (1) give \(K=O_k(m(\log m)^3)\). A uniform test index has failure probability zero if all tests pass, and at least \(1/K\) if one fails. Bounded amplification finds a failed test, when one exists, with failure probability at most \(\epsilon\), using \(O(\sqrt K\log(1/\epsilon))\) test evaluations. Each test costs \(O(\log m)\) queries.

On a zero-input, every proposed cell has a failed test. Each candidate is therefore accepted with probability at most \(\epsilon\). On a one-input, the genuine winner passes every test whenever its address was decoded correctly. Exact testing never invents a failure in a valid certificate, so its rejection probability is at most \(\epsilon\).

Accept if any candidate passes verification. The error on a zero-input is at most \(T\epsilon\), and on a one-input it is at most

\[
\frac{2m}{2^T}+T\epsilon+\epsilon<\frac13.
\tag{17}
\]

As a numerical check, at \(m=4\) the choices are \(T=12\) and \(\epsilon=1/12000\), making the expression in (17) exactly

\[
\frac8{4096}+\frac1{1000}+\frac1{12000}
=\frac{583}{192000}<\frac13.
\tag{E16}
\]

This numerical substitution checks the error accounting, independently of whether a particular small instance is hard. The same construction with sufficiently large \(m\) proves the quantum bound in (12). Coherent cell accesses remain ordinary bit queries: compute a global position reversibly, read the pointer bits individually, and query the resulting target. Keeping and reversing the workspace changes query counts by constant factors. [OpenAI2026, Proposition 3.3.]
<!-- /passage:quantum-verification-proof -->

<!-- passage:hard-distribution -->
### Randomized queries: two ways to discover the plant

Take \(L\) from (10), with \(m\) sufficiently large that \(1\le L<R(P_{k,m})\). Finite minimax supplies a distribution \(\mu\) on the partial function's domain under which every depth-\(L\) deterministic decision tree has success probability at most \(2/3\). Indeed, randomized depth-\(L\) algorithms are mixtures of finitely many deterministic trees. If every input distribution admitted average success greater than \(2/3\), minimax would give such a mixture with success at least \(2/3\) on every promised input, contradicting \(L<R(P_{k,m})\). [OpenAI2026, Section 4.1; Yao1977.]

Construct the dummy and planted inputs from Section 5 with these independently drawn address instances. Fix a deterministic algorithm using at most

\[
G=\left\lfloor\frac{mL}{100}\right\rfloor
\tag{18}
\]

queries, and analyze its dummy run. Its output can distinguish the coupled pair only if it queries the removed-zero position or reaches the planted cell:

\[
\left|\Pr(\text{output }1\text{ on planted})
-\Pr(\text{output }1\text{ on dummy})\right|
\le
\Pr(\text{removed zero queried})+
\Pr(\text{planted cell reached}).
\tag{19}
\]

Here both probabilities on the right refer to queries in the dummy run, with the same independent choice of \(I\). This is the first-difference argument illustrated by the five-bit modification.
<!-- /passage:hard-distribution -->

<!-- passage:zero-search -->
Let \(Z\) be the number of columns whose hidden zero is found during that run. Before a column's zero has been found, its row is uniform among that column's unqueried positions, even conditional on the entire adaptive transcript. The address instances and other columns are independent of its zero, and all certificate cells are blank.

Call a discovery early if fewer than \(m/2\) distinct positions in its column have previously been queried. Any query has conditional probability at most \(2/m\) of making an early discovery. The expected number of early discoveries is therefore at most \(2G/m\). Every remaining discovery is in a column that receives at least \(m/2\) queries, and there are at most \(2G/m\) such columns. Hence \(\mathbb EZ\le4G/m\).

The independent uniform choice of \(I\) now gives

\[
\Pr(\text{removed zero queried})=\frac{\mathbb EZ}{m}
\le\frac{4G}{m^2}.
\tag{20}
\]

The paper uses this early/late argument. The supplied Lean proof obtains the stronger bound \(2G/m^2\) by averaging the finite search cost within each column, and then weakens it where (20) is used. These are different proofs of the search estimate.
<!-- /passage:zero-search -->

<!-- passage:heavy-and-capped -->
Call a column *heavy* if the algorithm makes more than \(L\) queries in total to its \(r\) address inputs during the dummy run. There are at most \(G/L\) heavy columns. Since \(I\) is independent and uniform,

\[
\Pr(I\text{ is heavy})\le\frac{G}{mL}.
\tag{21}
\]

For the remaining event, fix a column \(i\) and a query time \(t\le G\). Give a simulator all dummy-input data outside the \(r\) address inputs of column \(i\). These data are independent of those inputs. Simulate the algorithm up to its proposed \(t\)-th query, aborting before its \((L+1)\)-st query to the target address inputs in total. If the proposed query is to a cell of column \(i\), output that cell's address; otherwise output a fixed arbitrary address.

This simulator makes at most \(L\) queries in total to the target instances, so in particular it obeys the cap \(L\) on each one. The direct-product bound (7) limits its probability of guessing all \(r\) answers to \((2/3)^r\).

If column \(i\) is nonheavy and the original run proposes a query to its true-address cell at time \(t\), the simulator has not aborted and outputs the correct address. We therefore obtain the joint-event bound

\[
\Pr\bigl(i\text{ is nonheavy and query }t
\text{ addresses }B_{i,s_i}\bigr)\le(2/3)^r.
\tag{22}
\]

This is the same implication as in the AND example. Conditioning on nonheaviness would be invalid. Stopping the simulator before it exceeds the cap makes the direct-product theorem applicable under the original product distribution.

Union bound over the \(G\) times, and average over the independent uniform choice of the planted column. Averaging over columns introduces no extra factor of \(m\). Adding the heavy-column event gives

\[
\Pr(\text{planted cell reached})
\le\frac{G}{mL}+G(2/3)^r.
\tag{23}
\]

Together, (19), (20) and (23) bound the difference of output probabilities by \(4G/m^2+G/(mL)+G(2/3)^r\). [OpenAI2026, equations (18)–(23).]
<!-- /passage:heavy-and-capped -->

<!-- passage:discrepancy-constants -->
The constants can be checked without estimating logarithms numerically. Write \(m=4^t\), so \(r=40t\). Since \((2/3)^2=4/9\le1/2\),

\[
(2/3)^r\le2^{-20t}=m^{-10}.
\tag{24}
\]

Assume \(1\le L\le m\) and \(G\le mL/100\), as holds for the parameters used above when \(m\) is sufficiently large. The first two terms in the discrepancy are at most \(4/100\) and \(1/100\). Also \(G\le m^2/100\), so its last term is at most \(1/(100m^8)\le1/100\). Thus

\[
\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r
\le\frac6{100}<\frac13.
\tag{25}
\]

This elementary polynomial bound is the simplification used in the supplied Lean proof. The preprint instead retains the sharper real exponent in its vanishing-tail calculation; either estimate suffices for the same randomized lower bound.

A correct randomized algorithm would output one with probability at most \(1/3\) on every dummy input and at least \(2/3\) on every planted input. Averaging would make its two output probabilities differ by at least \(1/3\). Bound (25) contradicts that conclusion. The estimate applies to randomized algorithms by fixing their coins and then averaging, since the query cap holds on every branch. Hence \(R(F_{k,m})>G\). The two integer floors lose only constant factors once \(m\) is large, yielding the randomized bound in (12).
<!-- /passage:discrepancy-constants -->

<!-- passage:optimal-exponent -->
### Excluding every exponent below four

Fix \(0\le\alpha<4\). Choose an integer \(k\ge2\) such that \(2-1/k>\alpha/2\), and keep it fixed. The two bounds in (12) imply, for a positive constant depending only on \(k,\alpha\),

\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ge c_{k,\alpha}
\frac{m^{\,2-1/k-\alpha/2}}{(\log m)^{2+\alpha b_k}}
\longrightarrow\infty.
\tag{26}
\]

The power of \(m\) is strictly positive, so it eventually dominates the fixed power of its logarithm. For the proposed cubic relation, choosing \(k=3\) makes the numerator's exponent \(1/6\); choosing \(k=2\) would make it zero and would not give this contradiction. The exponent table in Section 7 records this distinction.

Consequently no uniform constant \(C_\alpha\) can bound the ratio for \(\alpha<4\). No uniform estimate in a growing \(k\) is being invoked: a proposed exponent determines one fixed \(k\), after which only \(m\) tends to infinity. [OpenAI2026, Section 5.]

For the other direction, Aaronson, Ben-David, Kothari, Rao and Tal proved \(D(F)=O(Q(F)^4)\) for total Boolean functions, where \(D\) is exact deterministic query complexity. Their proof combines Huang's sensitivity theorem with quantum adversary bounds and a deterministic decision-tree estimate. Since a deterministic algorithm is also a randomized algorithm, \(R(F)\le D(F)\). Thus exponent four is admissible in (13), and (26) proves that its infimum is four. [ABKRT2021, Theorem 2 and its proof; Huang2019.]

The supplied Lean proof of the universal upper bound imports an earlier formal development from complexitylib and supplies a bridge from its quantum model. It does not formalize the sequence of auxiliary lemmas in OpenAI's Appendix A as written. The universal statement used to finish this proof has that alternative formal justification.
<!-- /passage:optimal-exponent -->

<!-- passage:verification-scope -->
## 9. Sources, checks and reproduction

The separation theorem and construction are OpenAI's. This exposition reconstructs their proof and adds finite examples. The supplied source snapshot contains a hypothesis-free Lean statement of the optimal exponent and the quantitative family, including a proof of the fixed-\(k\) Forrelation lower bound. Its records report successful builds and comparisons with independently compiled statement files. We inspected the source, statement records and recorded commands; Lean and Comparator were not rerun for this manuscript. Their source-level correspondence has been reviewed by AI agents, with no human review reported.

The finite calculations were independently recomputed by [examples.py](examples.py), using Python's standard library and exact arithmetic. They have not been newly proved in Lean. A general theorem in the supplied source can explain why an example behaves as it does without certifying this particular encoded input or calculation. [correspondence.json](correspondence.json) gives the exact source statements and declaration names for each passage; [LEAN_GAPS.md](LEAN_GAPS.md) identifies missing specializations, differing proof arguments and limitations of the supplied records. The proposed signatures in [NEW_STATEMENTS.json](NEW_STATEMENTS.json) are requests for formalization, not completed proofs.

From the extracted ZIP, run the following command with Python 3:

    python3 examples.py > examples_output.regenerated.txt

The result reproduces [examples_output.txt](examples_output.txt). The program enumerates the small inputs and pivot histories; it checks the reflection calculation, the capped-query examples, and the integer and rational Forrelation definitions. It neither simulates the full asymptotic quantum algorithm nor replaces its proofs. [figures.md](figures.md) specifies diagrams using those same exact data.
<!-- /passage:verification-scope -->

<!-- passage:references -->
## References

The bracketed keys match entries in [references.bib](references.bib). Section and theorem numbers for older papers refer to the full versions linked here.

- **[OpenAI2026] OpenAI.** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. Preprint, 5 October 2026. [Official manuscript](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). Theorem 1.1, Sections 2–5 and Appendix A.
- **[AA2018] Scott Aaronson and Andris Ambainis.** *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing*. SIAM Journal on Computing 47(3), 982–1038, 2018. [Full version](https://arxiv.org/pdf/1411.5729v1), Section 1.1.3, for the \(k\)-fold primitive.
- **[BansalSinha2021] Nikhil Bansal and Makrand Sinha.** *\(k\)-Forrelation Optimally Separates Quantum and Classical Query Complexity*. STOC 2021, 1303–1316. [Full version, v3](https://arxiv.org/pdf/2008.07003v3), equations (1.1)–(1.3), Theorem 1.3 and Corollary 1.4.
- **[ABKRT2021] Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal.** *Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem*. STOC 2021, 1330–1342. [Full version](https://arxiv.org/pdf/2010.12629v1), Theorem 2; Conjecture 2 states the former cubic randomized conjecture.
- **[Huang2019] Hao Huang.** *Induced Subgraphs of Hypercubes and a Proof of the Sensitivity Conjecture*. Annals of Mathematics 190(3), 949–955, 2019. [Published article](https://annals.math.princeton.edu/2019/190-3/p06).
- **[BHMT2002] Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp.** *Quantum Amplitude Amplification and Estimation*. Contemporary Mathematics 305, 53–74, 2002. [Full version](https://arxiv.org/pdf/quant-ph/0005055v1), Section 2, Lemma 1 and equation (8).
- **[BBHT1998] Michel Boyer, Gilles Brassard, Peter Høyer and Alain Tapp.** *Tight Bounds on Quantum Searching*. Fortschritte der Physik 46(4–5), 493–506, 1998. [Full version](https://arxiv.org/pdf/quant-ph/9605034), Section 4.
- **[Drucker2012] Andrew Drucker.** *Improved Direct Product Theorems for Randomized Query Complexity*. Computational Complexity 21(2), 197–244, 2012. [Full version, v2](https://arxiv.org/pdf/1005.0644v2), Section 1.3 and Lemmas 3.1–3.2.
- **[Shaltiel2003] Ronen Shaltiel.** *Towards Proving Strong Direct Product Theorems*. Computational Complexity 12(1–2), 1–22, 2003. [Earlier ECCC report](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html). Historical source for the separate-cap argument discussed by Drucker.
- **[BenDavid2015] Shalev Ben-David.** *A Super-Grover Separation Between Randomized and Quantum Query Complexities*. Preprint, 2015. [Full version](https://arxiv.org/pdf/1506.08106), Section 3.1.
- **[ABK2016] Scott Aaronson, Shalev Ben-David and Robin Kothari.** *Separations in Query Complexity Using Cheat Sheets*. STOC 2016, 863–876. [Full version, v2](https://arxiv.org/pdf/1511.01937v2), Sections 3.1–3.2 and 6.1.
- **[GPW2015] Mika Göös, Toniann Pitassi and Thomas Watson.** *Deterministic Communication vs. Partition Number*. FOCS 2015, 1077–1088. [Full version](https://eccc.weizmann.ac.il/report/2015/050/download/), Section 2.1 and the proof of Theorem 5.
- **[ABBLSS2017] Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha and Juris Smotrovs.** *Separations in Query Complexity Based on Pointer Functions*. Journal of the ACM 64(5), Article 32, 2017. [Accessible conference version](https://ir.cwi.nl/pub/25080/25080.pdf).
- **[Yao1977] Andrew Chi-Chih Yao.** *Probabilistic Computations: Toward a Unified Measure of Complexity*. FOCS 1977, 222–227. [Publisher record](https://doi.org/10.1109/SFCS.1977.24). Historical attribution for minimax in randomized complexity; the finite application is explained in Section 8.
<!-- /passage:references -->
