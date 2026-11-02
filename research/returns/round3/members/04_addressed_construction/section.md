# 4. Transcripts, addressed certificates, and the total function

<!-- passage:AC-interface -->
This section replaces §4 of the long reasoning record. It uses the partial function and exact two-output circuit supplied by §3.17, and gives the local tests and comparison property used in §5.3. The construction and Lemma 2.2 are due to OpenAI [OpenAI2026, §2.2, pp. 5–6]; the comparison property appears in its §3.3, p. 10. All queries below reveal one physical input bit.

A winning column must do two things: contain an all-one string, and supply a zero in every other column. Its zero witnesses are stored in a cell whose address is determined by several partial-function values. Transcripts in that cell certify that these values are defined and that the proposed address is correct. This gives a total predicate even when many of the partial-function instances lie outside their promise. The outward direction of the pointers also makes the winner safe against an opponent whose decoded address is meaningless: every pointer into the winner still reaches a one.
<!-- /passage:AC-interface -->

## 4.1. What a transcript certifies

<!-- passage:AC-circuit -->
Let $P:D\to\{0,1\}$, where $D\subseteq\{0,1\}^{n}$, and let $C$ be a Boolean circuit of fan-in at most two. Number its $S$ non-input gates in topological order; its two designated outputs, $d$ and $b$, are included among these gates. We assume that, on every raw input $a\in\{0,1\}^{n}$,

$$
d_C(a)=1\quad\Longleftrightarrow\quad a\in D,
\qquad
a\in D\quad\Longrightarrow\quad b_C(a)=P(a).
\tag{4.1}
$$

The value output on an unpromised input is unrestricted. The domain output is required to be correct there as well. In the application, $P=P_{k,m}$, $n=km$, and §3.17 supplies a circuit with $S=O_k(m(\log_2m)^2)$. The construction below uses (4.1); its logical properties do not use a lower bound for computing $P$.
<!-- /passage:AC-circuit -->

<!-- passage:AC-transcripts -->
A transcript $\tau\in\{0,1\}^{S}$ proposes a value for every non-input gate. At a gate, an input predecessor is read from the actual string $a$, a gate predecessor is read from its earlier entry in $\tau$, and a constant predecessor is known without a query. We call the transcript *gate-consistent* when every proposed gate value agrees with that gate's Boolean truth table on these predecessor values. Let $\operatorname{ev}_C(a)$ denote the transcript obtained by evaluating the circuit in topological order.

**Transcript lemma.** For every circuit $C$, every input $a$, and every proposed transcript $\tau$,

$$
\operatorname{GateConsistent}(C,a,\tau)
\quad\Longleftrightarrow\quad
\tau=\operatorname{ev}_C(a).
\tag{4.2}
$$

**Proof.** The evaluated transcript satisfies each gate equation by its definition. For the converse, assume all gate equations hold. At the first gate, each predecessor is an input or a constant, so the claimed output equals the evaluated output. Suppose this has been proved for every earlier gate. Each predecessor of the next gate then has its evaluated value, and that gate's equation forces its claimed output to have its evaluated value too. Induction proves equality at every gate. This proof holds for inputs outside $D$, since $C$ is a total circuit. In particular, every input has exactly one gate-consistent transcript. ∎

Combining (4.1) and (4.2), gate consistency together with the two tests $\tau_d=1$ and $\tau_b=c$ certifies $a\in D$ and $P(a)=c$. Conversely, the true transcript of a promised input of value $c$ passes these tests. Both the gate equations and the domain-output test are needed: a correct transcript of an unpromised input has domain output zero.
<!-- /passage:AC-transcripts -->

## 4.2. Columns and their selected cells

<!-- passage:AC-layout -->
For the separation family, fix $k\geq2$ and $m=4^t$ with $t\geq1$. Put

$$
\ell=\log_2m=2t,
\qquad
r=\lceil20\log_2m\rceil=40t=20\ell.
\tag{4.3}
$$

The definitions and verification arguments below also make sense for any positive integer $r$. The choice $r=20\ell$ is used for the separation family and its size bounds; the finite example will use $r=2$.

There are $m$ columns, indexed by $[m]=\{1,\ldots,m\}$. Column $i$ contains the following disjoint blocks of input bits.

| Block | Contents |
|---|---|
| $X_i$ | A string of $m$ bits. |
| $A_{i,1},\ldots,A_{i,r}$ | $r$ strings of $n=km$ bits. |
| $B_{i,s}$, for each $s\in\{0,1\}^{r}$ | One $\ell$-bit pointer $p_{i,s,j}$ into each column $j\ne i$, and one length-$S$ transcript $\tau_{i,s,h}$ for each $h\in[r]$. |

A fixed bijection from $\{0,1\}^{\ell}$ to $[m]$ decodes the pointers. In an expression $X_j[p]$, the pointer word $p$ is decoded by this bijection before indexing. Because $m=2^{\ell}$, every pointer word names a row. A cell is a collection of bits: consulting a chosen pointer costs its $\ell$ individual bit queries. No promise restricts the $A$-strings or the contents of any cell.
<!-- /passage:AC-layout -->

<!-- passage:AC-winner -->
If every $A_{i,h}$ lies in $D$, its partial-function values determine the *true address*

$$
s_i=(P(A_{i,1}),\ldots,P(A_{i,r})).
\tag{4.4}
$$

If any of these instances is unpromised, the column has no true address. For an arbitrary candidate address $s$, define $W(y;i,s)$, where $y$ is the complete input, by the conjunction

$$
\begin{aligned}
&X_i[q]=1 &&\text{for every }q\in[m],\\
&A_{i,h}\in D\text{ and }P(A_{i,h})=s_h
&&\text{for every }h\in[r],\\
&\tau_{i,s,h}=\operatorname{ev}_C(A_{i,h})
&&\text{for every }h\in[r],\\
&X_j[p_{i,s,j}]=0 &&\text{for every }j\ne i.
\end{aligned}
\tag{4.5}
$$

Each occurrence of $P(A_{i,h})$ in (4.5) is restricted to the explicitly required domain. We say that $i$ *wins at $s$* when (4.5) holds, and that $i$ is a winner when it wins at some address. In that event the second line forces $s=s_i$, so this is exactly the paper's condition: the all-one column has valid transcripts and outward zero pointers in the cell at its true address. This semantic identification needs no circuit-correctness premise. Premise (4.1) will be used when the partial-function values are replaced by locally checkable output bits.
<!-- /passage:AC-winner -->

<!-- passage:AC-total-unique -->
Define

$$
F(y)=1\quad\Longleftrightarrow\quad
\exists i\in[m]\ \exists s\in\{0,1\}^{r},\ W(y;i,s),
\tag{4.6}
$$

and let $F(y)=0$ otherwise. This defines a total Boolean function: (4.5) is a predicate on finitely many input bits, and an unpromised instance simply prevents its column from satisfying it. No undefined partial-function value has to be supplied. With the specified $P_{k,m}$, $C_{k,m}$, and parameters (4.3), this is $F_{k,m}$.

**Uniqueness lemma.** For any $P,C$, pointer bijection, and complete input $y$, at most one pair $(i,s)$ satisfies (4.5).

**Proof.** Suppose $W(y;i,s)$ and $W(y;j,a)$ hold with $j\ne i$. The pointer from $B_{i,s}$ into column $j$ exhibits a zero in $X_j$. The winning condition for $j$ says that every bit of $X_j$ is one, a contradiction. Thus the columns agree. For a fixed column, the second line of (4.5) determines each address bit as the value of the same promised input, so the addresses agree as well. ∎

Totality and uniqueness use the semantic definition (4.5). The exact realization property (4.1) is needed for the verification procedure, rather than for these two logical conclusions.
<!-- /passage:AC-total-unique -->

## 4.3. A four-column instance

<!-- passage:AC-example-promise -->
The following example uses the actual partial function $P_{2,4}$. To keep the cells visible, take $r=2$, giving four cells per column; the separation family instead has $r=40$ at $m=4$. The example also uses a circuit synthesized from this finite truth table, rather than the asymptotic arithmetic circuit of §3. These choices make it an instance of the generic construction (4.5), not a small-size demonstration of the separation bound.

For $k=2,m=4$, write an eight-bit input as two four-bit strings, and convert each bit $a$ to the sign $(-1)^a$. With Walsh coordinates in the order $00,01,10,11$, the integer Walsh matrix and the exact Forrelation value are

$$
W_4=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad
N=z_1^{\mathsf T}W_4z_2,\qquad
\Phi=\frac{N}{8},\qquad \delta=2^{-10}.
\tag{4.7}
$$

Here $P_{2,4}=1$ when $\Phi\geq\delta$, $P_{2,4}=0$ when $|\Phi|\leq\delta/2$, and the other inputs are unpromised. For the three strings used below, direct multiplication gives:

| Eight-bit string | $N$ | $\Phi$ | Partial-function value | Exact outputs $(d,b)$ |
|---|---:|---:|---|---|
| $0000\,0000$ | $4$ | $1/2$ | $1$ | $(1,1)$ |
| $0001\,0010$ | $0$ | $0$ | $0$ | $(1,0)$ |
| $1111\,0000$ | $-4$ | $-1/2$ | undefined | $(0,0)$ |

For example, $W_4(1,1,1,1)^{\mathsf T}=(4,0,0,0)^{\mathsf T}$, which gives the first and third rows. In the second row, $z_1=(1,1,1,-1)$, $z_2=(1,1,-1,1)$, and $W_4z_2=(2,-2,2,2)$, whose inner product with $z_1$ is zero. The negative value in the last row is outside both parts of the one-sided promise; its large absolute value does not make it a 1-input.

The projection test of §3 has success probability $\Phi^2$. Thus the first and third rows both give probability $1/4$. Any fixed number of independent repetitions of this test, followed by a decision based only on their outcomes, has the same output law on these two inputs. A decoder can therefore produce the same plausible label for the positive input and this unpromised input. The exact domain circuit distinguishes them. This observation concerns the specified projection decoder, not every quantum algorithm.
<!-- /passage:AC-example-promise -->

<!-- passage:AC-example-board -->
Use these instances in the board below. A true address is shown only when both partial values are defined.

| Column $i$ | $X_i$ | $A_{i,1}$ | $A_{i,2}$ | True address |
|---:|---|---|---|---|
| $1$ | $1111$ | $00000000$ | $00010010$ | $10$ |
| $2$ | $0111$ | $11110000$ | $00010010$ | none |
| $3$ | $1011$ | $00000000$ | $00010010$ | $10$ |
| $4$ | $1101$ | $00000000$ | $00010010$ | $10$ |

Encode the rows $1,2,3,4$ by $00,01,10,11$, respectively. In $B_{1,10}$, store the true transcripts for column 1 and the pointer words

$$
p_{1,10,2}=00\longmapsto1,\qquad
p_{1,10,3}=01\longmapsto2,\qquad
p_{1,10,4}=10\longmapsto3.
\tag{4.8}
$$

The three targeted bits are $X_2[1]=X_3[2]=X_4[3]=0$. Column 1 therefore wins at $10$. Each other column has a zero of its own and cannot win. Column 2 additionally has an unpromised address instance. Its decoder may still output any two-bit string; that output does not define a semantic true address.

The accompanying checker specifies every remaining cell, rather than leaving any input bit unspecified. It stores the actual two transcripts in every cell of each column. At every cell, pointers into columns 2, 3, and 4 go to their respective zero rows; a rival's pointer into column 1 is encoded by that cell's two-bit address, so the four labels cover all four rows. Thus the rival's transcripts are internally consistent even though one has domain output zero. Its rejection will expose the domain-output requirement directly.
<!-- /passage:AC-example-board -->

## 4.4. The local tests

<!-- passage:AC-tests -->
Fix a candidate pair $(i,s)$. The partial-function conditions in (4.5) can be replaced by tests on the stored transcripts. Use the following list, writing $g_e(y;i,s)=1$ when the test with label $e$ passes.

| Test family | Number | Passing condition | Maximum bit queries |
|---|---:|---|---:|
| Column bits | $m$ | The selected bit of $X_i$ is one. | $1$ |
| Outward pointers | $m-1$ | The selected pointer reaches a zero in its designated other column. | $\ell+1$ |
| Gate equations | $rS$ | The claimed gate output equals its truth table on its two predecessors. | $3$ |
| Domain outputs | $r$ | The selected transcript's domain output is one. | $1$ |
| Value outputs | $r$ | The selected transcript's value output is $s_h$. | $1$ |

To make the index set independent of the candidate, list the other columns in increasing order, skipping $i$, and label their pointer tests by $[m-1]$. The common test set is

$$
E=[m]\;\sqcup\;[m-1]\;\sqcup\;
\bigl([r]\times([S]\sqcup\{d,b\})\bigr).
\tag{4.9}
$$

The labels $d,b$ in the last summand mean the two output *tests*. They are additional to the consistency tests at the corresponding output gates. Consequently

$$
K=|E|=m+(m-1)+r(S+2).
\tag{4.10}
$$

For example, if $S\leq A m\ell^2$ for a fixed integer $A$, then (4.3) gives

$$
K=2m-1+20\ell(S+2)
\leq(42+20A)m\ell^3.
\tag{4.11}
$$

Indeed, the circuit term contributes at most $20A m\ell^3$, while $2m\leq2m\ell^3$ and $40\ell\leq40m\ell^3$. Here $m\geq4$ and $\ell\geq2$. This is the bound $K=O_k(m(\log m)^3)$ once §3.17 supplies $A=A_k$.
<!-- /passage:AC-tests -->

<!-- passage:AC-local-equivalence -->
**Local verification lemma (classical part of OpenAI, Lemma 2.2).** Suppose $C$ satisfies (4.1). On every complete input $y$, and for every candidate $(i,s)$,

$$
W(y;i,s)\quad\Longleftrightarrow\quad
g_e(y;i,s)=1\text{ for every }e\in E.
\tag{4.12}
$$

Every test is computed by an exact deterministic adaptive decision tree of depth at most

$$
q_*=\max\{3,\ell+1\}=\ell+1
\qquad(m\geq4).
\tag{4.13}
$$

**Proof.** If all tests pass, the column-bit and pointer tests give the first and last lines of (4.5). For each $h$, the gate tests and (4.2) identify $\tau_{i,s,h}$ as the true evaluation of $C$ on $A_{i,h}$. Its two output tests then imply $A_{i,h}\in D$ and $P(A_{i,h})=s_h$, by (4.1). These are the remaining lines of (4.5). Conversely, (4.5) supplies actual transcripts of promised inputs with the required values, so every test passes.

For the query bound, a column or output test reads one bit. A gate test reads the claimed gate value and at most two predecessor values. An input predecessor is read from $A_{i,h}$; a gate predecessor is read from the stored transcript. A constant needs no query. A pointer test reads its $\ell$ pointer bits, computes their decoded row for free, and then queries the indicated target bit. These procedures are exact on every input, regardless of whether the candidate is a winner or its address instances are promised. Their largest depth is (4.13). ∎
<!-- /passage:AC-local-equivalence -->

<!-- passage:AC-dichotomy -->
It follows that a winning column has all tests passing at its unique true address. At every other address at least one test fails. If a column is a nonwinner, then every address has a failing test: an address at which all tests passed would contradict (4.12). This includes columns with an unpromised instance. Gate consistency cannot repair that instance, because a true transcript then has domain output zero; changing that output to one makes at least one gate equation fail.
<!-- /passage:AC-dichotomy -->

<!-- passage:AC-example-tests -->
For the four-column board, the supplied finite circuit has $S=180$ non-input gates, with domain and value outputs at gates 178 and 179 using zero-based gate numbering. Each candidate has

$$
K=4+3+2(180+2)=371
\tag{4.14}
$$

tests. At $(1,10)$, the four column tests, three pointer tests, 360 gate tests, two domain-output tests, and two value-output tests all pass. At $(1,00),(1,01),(1,11)$, respectively, there are $1,2,1$ failed tests: the proposed address disagrees with one or two true output bits, while every pointer still reaches its designated zero. Column 2 has a failing domain-output test at every address, despite all its gate equations being satisfied. Every pointer it directs into column 1 also reaches a one.

The checker evaluates the partial function from the integer expression (4.7) and evaluates the Boolean circuit separately. It checks all 256 eight-bit inputs against the circuit's outputs, all 16 candidate pairs on the specified board against (4.5), and every one of the 360 single-bit changes to the selected transcripts. It also checks six witnesses showing that every coordinate of a two-bit-pointer/four-bit-target lookup is essential. All these finite checks pass.

A second board in the output isolates the domain test. Its off-promise column is all ones, its stored transcripts are the true ones, and its pointers reach zeros in all other columns. At the address named by its value-output bits, every test except one domain-output test passes. Removing the domain tests would accept this column incorrectly. With the full test list, the board has no winner and the function is zero.

The full gate list, complete base board, selected transcripts, test counts and construction of the second board are in `examples/circuit.json`, `examples/board.json`, and `examples/output.json`. Run `python3 examples/check_example.py` to reproduce the output using the Python standard library and exact integer or rational arithmetic. These are finite computational checks, separate from the general proofs above and from the supplied Lean evidence.
<!-- /passage:AC-example-tests -->

## 4.5. A shallow lookup can have large support

<!-- passage:AC-pointer-support -->
The pointer bound measures adaptive depth. It does not give a fixed set of only $\ell+1$ input coordinates on which the test depends. For one pointer test, its complete relevant coordinate set consists of the $\ell$ pointer bits and all $m$ bits of the target column. Each is essential when $\ell\geq1$.

To see this for a target bit, set the pointer to that row, hold every other coordinate fixed, and flip the selected bit. The test changes. To see it for a pointer bit, choose two pointer words differing only in that bit. The pointer bijection sends them to distinct rows. Assign different Boolean values to those two target bits and hold all other physical coordinates fixed. Changing the chosen pointer bit changes the test. Thus the support is exactly $m+\ell$, although every evaluation path reads only $\ell+1$ bits.

The four-column example has six essential coordinates and depth three. This corrects an earlier ledger description of fixed support. The original preprint already describes the adaptive lookup and requires no correction at this point [OpenAI2026, Lemma 2.2, p. 6].
<!-- /passage:AC-pointer-support -->

## 4.6. Coherent evaluation of an arbitrary test index

<!-- passage:AC-coherent -->
Fix $(i,s)$ and retain the test label $e$ in a register. There is a single coherent implementation of all tests for any superposition of labels. A precise form of the retained-workspace statement is

$$
\sum_{e\in E}\alpha_e\,|e\rangle|0_e\rangle
\longmapsto
\sum_{e\in E}\alpha_e\,|e\rangle|\psi_{e,y}\rangle,
\tag{4.15}
$$

where the coefficients $\alpha_e$ are arbitrary, each $\psi_{e,y}$ has norm one, and its output label equals $g_e(y;i,s)$ with certainty. Normalization of the whole state requires $\sum_e|\alpha_e|^2=1$; the linear identity itself holds without that restriction. The test workspaces can have index-dependent finite dimensions, embedded into one finite workspace. Their dimensions and initial states are fixed before the input is given. The index register is never measured: the controlled unitary has exactly the linear action (4.15). The index can become entangled with the final workspace state, which may depend on $y$ and remains available for inversion.

**Proof and query count.** For each test, use its decision tree from (4.13). At every level, retain the earlier answers and compute the next queried location by an input-independent reversible operation. The location can depend on those retained answers: this is how the pointer lookup works. Query into a fresh answer register and retain enough history to make each update reversible. A leaf determines the test output exactly. Pad shorter branches to the common depth $q_*$ with inactive reads. A controlled bit read can be implemented with two ordinary oracle calls: load the bit into a temporary register, use it conditionally, and query again to clear the temporary register. Hence all branches have a common physical query cap $2q_*$.

The entire construction is controlled by $e$. Its action is the direct sum of the individual test unitaries, so linearity gives (4.15) for arbitrary complex coefficients. Distinct index blocks remain orthogonal, and the output in each block is the correct test value. This proves the arbitrary-index coherent part of Lemma 2.2, with retained workspace and at most $2(\ell+1)$ ordinary bit queries for $m\geq4$.
<!-- /passage:AC-coherent -->

<!-- passage:AC-clean-oracle -->
If a later routine needs the work registers reset, there is a further compute–copy–uncompute step. Controlled query-free gates prepare the fixed index-dependent starting states from a common all-zero ancilla and restore that convention at the end. Apply the implementation in (4.15), XOR its exact output label into a separate target bit, and apply the full inverse implementation. Since the computed output is certain in each index block, copying it leaves that block's workspace unchanged. The inverse therefore restores its starting state, giving

$$
|e\rangle|b\rangle|0_{\rm work}\rangle
\longmapsto
|e\rangle|b\mathbin\oplus g_e(y;i,s)\rangle|0_{\rm work}\rangle
\tag{4.16}
$$

with at most $4q_*$ physical queries. This statement also acts on arbitrary superpositions of the label and target, by linearity. It is an ordinary corollary proved here; the supplied construction theorem explicitly packages the retained-workspace form (4.15), rather than the reset-workspace interface (4.16).
<!-- /passage:AC-clean-oracle -->

<!-- passage:AC-uniform-sampler -->
Uniform-index evaluation is a particular use of (4.15). Prepare the input-independent state $K^{-1/2}\sum_e|e\rangle$ and run the controlled evaluator. If $h$ tests fail, the probability of observing a failed test is $h/K$, because the index blocks are orthogonal and each test is exact. Thus all tests passing gives failure-detection probability zero, while a nonwinner at any proposed address gives probability at least $1/K$. The later search routine uses the evaluator and its inverse with the retained work registers. A theorem only about this uniform distribution would not, by itself, supply the arbitrary-index action (4.15).
<!-- /passage:AC-uniform-sampler -->

## 4.7. Why a winner defeats an unpromised opponent

<!-- passage:AC-comparison -->
For distinct columns $i,j$, the comparison routine in §5.3 decodes one address label for each column. At those labels it follows the pointer from each column into the other, disqualifying a column if the other column's pointer finds a zero in its $X$-string. If exactly one is disqualified, the other wins; a fixed rule resolves the remaining cases. Each decoded label is a bit string on every raw input, even when it has no relation to a true address. Its production has a fixed query cap on every input.

Fix $0<\varepsilon<1/2$, and suppose $i^\star$ is a genuine winner. For any opponent $j\ne i^\star$, every proposed rival address $a$, and every pointer stored there,

$$
X_{i^\star}[p_{j,a,i^\star}]=1.
\tag{4.17}
$$

This follows solely from the winner's all-one string. It never gets disqualified. Whenever its own decoder returns its true address $s_{i^\star}$, its outward pointer satisfies

$$
X_j[p_{i^\star,s_{i^\star},j}]=0,
\tag{4.18}
$$

so the rival does get disqualified. The tie rule is unused on this event. Therefore

$$
\Pr[i^\star\text{ wins against }j]
\ \geq\ \Pr[\widehat s_{i^\star}=s_{i^\star}]
\ \geq\ 1-\varepsilon.
\tag{4.19}
$$

For the last inequality, run the promised decoder on each of the winner's $r$ instances with error at most $\varepsilon/r$, and use the union bound. All those promises hold by (4.5). No correctness assumption about the rival decoder, or independence between its output and the winner's output, is needed for the event inclusion. In the coherent implementation the decoded labels are retained in orthogonal registers; the later pointer operations are controlled by them. Projection onto a comparison result therefore adds the probabilities of the corresponding label blocks, making the same event calculation valid.

In the example, column 2 can propose $00$, $01$, $10$, or $11$, and can direct its incoming pointer to any of the four rows of column 1. It always reads a one. The true cell $B_{1,10}$ always points to the zero at row 1 of column 2. The checker verifies this for all 16 rival-label/target choices, and for all 48 choices obtained by including the other two rivals. This is the property used by the tournament in §5; comparisons between two nonwinners remain unrestricted.
<!-- /passage:AC-comparison -->

## 4.8. Attribution and formal correspondence

<!-- passage:AC-attribution -->
The use of partial-function answers to address a certificate array follows Aaronson, Ben-David and Kothari's cheat-sheet framework [ABK2019, §6.1, Definitions 14–15, pp. 20–21]. Their Lemma 17, p. 22, supplies the evaluate-then-check strategy for their cheat-sheet function, including rejection of certificates for unpromised inputs. The present proof establishes the properties of the particular multi-column construction (4.5); it does not obtain its later separation bounds by applying that lemma.

Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs explicitly discuss direct pointers from a distinguished element to a zero in every other column [ABBLSS2015, §1.2, p. 6]. They also explain the exponential alphabet cost of that choice in their encoding. Here all pointer bits are explicit Boolean input coordinates, and reading a selected pointer is charged accordingly. These citations identify antecedents of the ingredients; the construction analyzed in this section is the one in OpenAI's preprint.
<!-- /passage:AC-attribution -->

<!-- passage:AC-evidence -->
The exact source declarations and complete types are recorded in `correspondence.json` and `evidence/lean_audit.json`. In particular, `QuarticQuery.gateConsistent_iff_eq_circuitEval` gives (4.2), `QuarticQuery.winsAt_unique` gives pair uniqueness, and `QuarticQuery.winsAt_iff_localTests` gives (4.12) under `CircuitRealises C P`. The semantic bridge `QuarticQuery.winsAt_iff_paperWinsAt` has no such premise because both sides already refer to the partial function.

`QuarticQuery.Paper.construction_lemma_2_2_complete` packages the count, finite size bound, local-test equivalence, adaptive depth, arbitrary-index retained-workspace implementation, and physical query cap for the same circuit witnesses. Its premises $t\geq1$, `CircuitRealises C (P k t)`, and the circuit-size bound are exactly the supplied circuit properties. `QuarticQuery.Paper.construction_pointer_every_physical_coordinate` supplies the essential-coordinate witnesses for the support argument. The clean oracle (4.16) and the explicit finite example have the separate ordinary-proof and computational status stated above.

The frozen packet includes a source-bound successful root-build receipt for the cited declarations. A later selected type/axiom audit includes the newer Paper construction wrappers; membership of that audit is recorded separately for every name and is not asserted for all older core declarations. Their 124 recorded local Lean/configuration hashes match the supplied bytes; this review did not rerun Lean. The current Construction Comparator receipt compares the four source theorems `winsAt_unique`, `existsUnique_gateConsistent`, `winner_no_incoming_zero`, and `winner_finds_zero`, together with their checked wrappers. It does not compare the newer complete local-test theorem. Old source comments and earlier returns calling those files unelaborated describe an earlier stage; the exact receipts and their scope are retained in the evidence sidecar. No human review is claimed.
<!-- /passage:AC-evidence -->

### References for this section

- **[OpenAI2026]** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, supplied preprint dated 5 October 2026. §2.1, pp. 3–5; §2.2 and Lemma 2.2, pp. 5–6; §3.3, pp. 9–10. [Official source at the supplied public pin](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). Mathematical assessment uses the attached PDF, SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.
- **[ABK2019]** Scott Aaronson, Shalev Ben-David and Robin Kothari, *Separations in query complexity using cheat sheets*, arXiv:1511.01937v2, 9 July 2019; originally published in STOC 2016, pp. 863–876, DOI [10.1145/2897518.2897644](https://doi.org/10.1145/2897518.2897644). Locators use the inspected v2 PDF: §6.1, Definitions 14–15, pp. 20–21; §6.2, Lemma 17, p. 22. [Exact inspected edition](https://arxiv.org/pdf/1511.01937v2).
- **[ABBLSS2015]** Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha and Juris Smotrovs, *Separations in Query Complexity Based on Pointer Functions*, arXiv:1506.04719v3, 26 October 2015. §1.2, especially the direct-pointer discussion on p. 6. [Exact inspected edition](https://arxiv.org/pdf/1506.04719v3).
