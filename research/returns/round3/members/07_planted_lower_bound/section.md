# Planted inputs and the randomized lower bound

**Replacement scope.** This text replaces §§6.2–6.6 of the supplied long reasoning record. It uses the addressed function and the realizing circuit from §4, and the capped direct-product lemma already proved in the frozen baseline §6.1. Its output for §7 is Proposition 4.2 for the same circuit, together with the explicit base-two-logarithm lower constant \(1/400\). It does not assume that another round-three section has arrived.

**Authorship and evidence.** This is an AI-assisted advisory reconstruction of OpenAI's argument, with additional explanations and finite examples. No human review or new Lean execution is claimed. Formal correspondence and the supplied, source-matched build and axiom receipts are recorded in the accompanying files; the new conjunction wrapper is a proposal awaiting compilation.

### 6.2. The hard distribution and the hidden address

<!-- passage:CL-entry-interface -->
We first recall the objects needed below. Let \(P:D\to\{0,1\}\), where \(D\subseteq\{0,1\}^{n}\), and let \(C\) be a finite fan-in-two Boolean circuit with a domain output and a value output. The domain output is one exactly on \(D\); on \(D\), the value output equals \(P\). A circuit transcript records the values of all non-input gates. Topological evaluation supplies a unique transcript satisfying all gate checks.

For \(m=4^t\), \(t\ge1\), put \(\ell=\log_2m=2t\) and \(r=40t=20\log_2m\). Each of the \(m\) columns contains an \(m\)-bit string \(X_i\), \(r\) strings \(A_{i,1},\ldots,A_{i,r}\) of length \(n\), and a separate certificate cell \(B_{i,s}\) for each \(s\in\{0,1\}^{r}\). A cell contains a transcript for every \(A_{i,h}\) and an \(\ell\)-bit pointer into each other column. Every pointer encoding represents a row, since there are exactly \(2^\ell=m\) rows. When the \(A\)-strings of column \(i\) are promised, its true address is
\[
s_i=(P(A_{i,1}),\ldots,P(A_{i,r})).
\]
The total function \(F=F_{P,C,m}\) equals one exactly when some column \(i\) is all ones, all its \(A\)-strings are promised, and \(B_{i,s_i}\) contains correct transcripts and pointers to zeros in every other column.

The lower bound compares an input with one zero in every column against an input in which one column's zero is erased and its true cell is filled. A query algorithm must encounter one of those changes. The erased zero is hidden by the independent choice of the column. The filled cell is hidden by the difficulty of predicting an entire vector of partial-function values.

The address-and-certificate mechanism has the cheat-sheet antecedent of Aaronson, Ben-David and Kothari [ABK2019v2, §6.1, Definitions 14–15, and §6.2, Lemma 17, pp. 20–22](https://arxiv.org/pdf/1511.01937v2). Lemma 17 concerns upper bounds for their cheat-sheet function. The separate arrays and outward pointers of the present function are accounted for in the proof below.
<!-- /passage:CL-entry-interface -->

<!-- passage:CL-minimax -->
Assume that \(L\) is a nonnegative integer and \(L<R(P)\). Here \(R\) uses a cap on every execution and success at least \(2/3\) on every promised input. The domain \(D\) is nonempty: an empty promise has zero-query complexity.

We need one probability distribution that makes every depth-\(L\) deterministic tree unsuccessful often enough:
<!-- claim:claim-minimax-mu -->
\[
\exists\mu\text{ on }D\quad
\forall T\text{ with }\operatorname{depth}(T)\le L,\qquad
\Pr_{x\sim\mu}[T(x)=P(x)]\le\frac23.
\]

Here is a finite proof of the minimax step. There are finitely many depth-\(L\) trees on \(n\) coordinates. For each such tree let \(a_T\in\mathbb R^D\) be its vector of correctness indicators, and let \(K\) be the convex hull of these vectors. A point of \(K\) is the success vector of one randomized mixture of depth-\(L\) trees. Thus \(K\) is disjoint from the closed orthant \(H=[2/3,\infty)^D\).

For \(a\in K\), its nearest point in \(H\) has coordinates \(c_x=\max(a_x,2/3)\). Compactness of \(K\) gives a pair \(a,c\) of minimum distance, and disjointness makes that distance positive. Set \(v=c-a\). Then \(v_x\ge0\), \(v\ne0\), and \(c_x=2/3\) whenever \(v_x>0\). For \(b\in K\), the point \(a+\theta(b-a)\) stays in \(K\) for \(0\le\theta\le1\). Its squared distance to the fixed point \(c\) is at least the minimum squared distance. Differentiating this quadratic from the right at zero gives \(v\cdot(b-a)\le0\). Consequently,
<!-- claim:NCL-strict-hard-distribution -->
\[
v\cdot b\le v\cdot a
=v\cdot c-\|v\|^2
=\frac23\sum_xv_x-\|v\|^2.
\]
The weights \(\mu(x)=v_x/\sum_yv_y\) form a probability distribution. Dividing the preceding inequality by the positive denominator proves the required bound, in fact with one positive strict margin for all the trees. This proof is the finite minimax argument; it does not require the hard measure used in the analytic proof of Forrelation hardness.
<!-- /passage:CL-minimax -->

<!-- passage:CL-address-guess -->
Apply the frozen baseline's Lemma 4.1 to independent \(U_1,\ldots,U_r\sim\mu\). If an algorithm makes at most \(L\) queries to each \(U_h\) on every execution, then
<!-- claim:claim-address-guess -->
\[
\Pr[\widehat s=(P(U_1),\ldots,P(U_r))]\le(2/3)^r.
\]
The algorithm may interleave its queries and use side information jointly independent of the whole tuple. Fixing that information and its random coins preserves the input law, so the deterministic bound can be averaged.

The prerequisite is the per-input-capped, or fair-algorithm, direct product. Its conditional-product proof is explained by Drucker [Drucker2014v2, §1.3, Lemmas 3.1–3.2, and the final paragraph of §3, pp. 6–7 and 11–13](https://arxiv.org/pdf/1005.0644v2), who attributes the fair case to Shaltiel. Drucker's headline theorem has a different global-budget statement. We use precisely the capped formulation proved in §6.1; no new direct-product result is assumed.
<!-- /passage:CL-address-guess -->

### 6.3. Coupled zero and one inputs

<!-- passage:CL-generic-statement -->
**Generic lower bound.** Let \(m=4^t\), \(t\ge1\), and \(r=40t\). Let \(P:D\to\{0,1\}\) be a partial Boolean function on a finite set of input coordinates, let \(C\) realize its promise and value, and let \(F_{P,C,m}\) be the addressed function just described. If
\[
1\le L\le m,\qquad L<R(P),
\]
then
<!-- claim:prop-4.2-generic -->
\[
R(F_{P,C,m})>\left\lfloor\frac{mL}{100}\right\rfloor.
\]
Circuit size is irrelevant to this implication.

Define the budget
<!-- claim:eq-17 -->
\[
G=\left\lfloor\frac{mL}{100}\right\rfloor
\tag{17}
\]
and fix a deterministic tree \(T\) of depth at most \(G\). Fix also the hard distribution \(\mu\) from §6.2. We construct both input distributions on one probability space.
<!-- /passage:CL-generic-statement -->

<!-- passage:CL-dummy -->
For each column \(i\), choose \(J_i\) independently and uniformly from its \(m\) rows. In the dummy input \(Y^{(0)}\), put
<!-- claim:def-dummy -->
\[
X_i[j]=
\begin{cases}
0,&j=J_i,\\
1,&j\ne J_i.
\end{cases}
\]
Independently draw every \(A_{i,h}\) from \(\mu\). Fill every bit of every cell \(B_{i,s}\) with zero. In particular, the blank cells reveal neither a zero location nor any value of \(P\).

All these probability spaces are finite. Expectations can therefore be read as finite sums with product weights. We will repeatedly fix all coordinates except one independent random variable and then average over that variable. Resampling a coordinate from its original law preserves the expectation: summing first over the old coordinate gives a factor one, leaving precisely the sum over its replacement.
<!-- /passage:CL-dummy -->

<!-- passage:CL-planted -->
Choose \(I\) uniformly from the \(m\) columns, independently of the entire dummy input. Obtain \(Y^{(1)}\) by replacing \(X_I\) by \(1^m\) and filling only \(B_{I,s_I}\). Put the actual evaluation transcript of \(C\) on \(A_{I,h}\) in its \(h\)-th transcript field, and give its pointer into column \(j\ne I\) the value \(J_j\). Every \(A_{i,h}\) is promised, so all true addresses exist. This defines the planted input.

Each dummy column has a zero, whereas column \(I\) of the planted input meets every winning condition. Thus
<!-- claim:claim-Y-values -->
\[
F_{P,C,m}(Y^{(0)})=0,\qquad
F_{P,C,m}(Y^{(1)})=1.
\]
If the finite sums are instead taken over the whole input cube with \(\mu=0\) outside \(D\), the second assertion is needed only at sample points of positive weight. This is the support convention of the Lean formulation.
<!-- claim:def-planted -->
<!-- /passage:CL-planted -->

<!-- passage:CL-tiny-planted-example -->
**A four-column instance.** To see the planting operation, temporarily take \(m=4\), \(r=2\), and \(P(a,b)=a\mathbin{\mathrm{xor}}b\) on all two-bit inputs. A two-gate circuit has domain output \(1\) and value output \(a\mathbin{\mathrm{xor}}b\); its transcript is \((1,P(a,b))\). Use zero-based row and column labels in this example.

Choose the zero positions and strings as follows.

| Column \(i\) | \(J_i\) | \(X_i\) in \(Y^{(0)}\) | \(A_{i,1}\) | \(A_{i,2}\) | \(s_i\) |
|---|---:|---|---|---|---|
| 0 | 2 | \(1101\) | \(00\) | \(01\) | \(01\) |
| 1 | 0 | \(0111\) | \(10\) | \(11\) | \(10\) |
| 2 | 3 | \(1110\) | \(10\) | \(11\) | \(10\) |
| 3 | 1 | \(1011\) | \(01\) | \(10\) | \(11\) |

Plant column \(I=1\). Its string becomes \(1111\), and cell \(B_{1,10}\) receives transcripts \((1,1)\) and \((1,0)\). Its pointers into columns \(0,2,3\) are \(2,3,1\), encoded as \(10,11,01\). These point to the displayed zeros, so the planted input has value one. All other cells remain blank.

The files [checks/planted_example.py](checks/planted_example.py) and [checks/planted_example.json](checks/planted_example.json) implement all 192 physical bit coordinates of this toy and evaluate its winning predicate directly. This is a finite instance of the generic addressed construction. Its partial function is XOR, its address length is \(2\), and the later example query budget is \(4\); it is not a Forrelation instance or a choice satisfying \(r=40t\) and \(G=\lfloor mL/100\rfloor\).
<!-- /passage:CL-tiny-planted-example -->

<!-- passage:CL-first-difference -->
The two coupled inputs can differ only at \(X_I[J_I]\) and inside \(B_{I,s_I}\). Until \(T\) receives a different answer, its histories on the two inputs coincide, so its next query or stopping decision also coincides. If the dummy execution never queries a differing bit, the two executions end at the same leaf.

For Boolean outputs, the absolute difference of expected output indicators is at most the probability that the outputs differ. The preceding implication and a union bound give
<!-- claim:eq-18 -->
\[
\begin{aligned}
\left|\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]\right|
&\le
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]\\
&\quad+
\Pr[T\text{ on }Y^{(0)}\text{ queries a bit of }B_{I,s_I}].
\end{aligned}
\tag{18}
\]
Equation (18) writes the absolute-value form of the preprint's one-sided first-difference comparison. The full cell visit is an upper bound on seeing a changed cell bit: some planted bits can equal their blank values. Every event on the right concerns the dummy run, whose law remains independent of \(I\).
<!-- /passage:CL-first-difference -->

### 6.4. Discoveries and the erased zero

<!-- passage:CL-erased-zero-identity -->
Let \(Z\) count the columns whose unique zero is queried during the complete dummy run:
<!-- claim:def-Z -->
\[
Z=\sum_{i=1}^{m}
\mathbf1\{T\text{ on }Y^{(0)}\text{ queries }X_i[J_i]\}.
\]
Repeated queries to a discovered zero still contribute only one to \(Z\). After fixing all the dummy data, \(Z\) is fixed and exactly \(Z\) of the \(m\) possible choices of \(I\) select a discovered zero. Averaging over \(I\), and then over the dummy data, gives the exact identity
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
=\frac{\mathbb EZ}{m}.
\]
This identity needs independence and uniformity of \(I\), but no depth bound and no hardness assumption on \(P\). A separate search estimate will bound its right-hand side.
<!-- /passage:CL-erased-zero-identity -->

<!-- passage:CL-early-late -->
Before the zero in a column has been discovered, its conditional location is uniform among that column's unqueried rows. To include adaptivity, fix a positive-probability transcript prefix. A deterministic tree follows that prefix exactly on inputs satisfying its recorded query answers: induction over the prefix proves the reverse implication as well as the forward one. Thus the prefix event gives separate constraints on the independent \(J_i\)'s and \(A\)-strings. For an undiscovered \(J_i\), the constraints merely exclude the distinct rows already queried. The blank cells add no constraint. Therefore, if \(u\) rows remain,
<!-- claim:claim-uniform-zero -->
\[
\Pr[J_i=j\mid\text{that prefix}]
=
\begin{cases}
1/u,&j\text{ is unqueried in column }i,\\
0,&j\text{ was queried there}.
\end{cases}
\]
Positive probability of the prefix ensures \(u>0\). Repeated queries impose no new exclusion.

Call a discovery early when fewer than \(m/2\) distinct positions of its column were queried beforehand. At a query that can make an early discovery, more than \(m/2\) positions remain, so its conditional discovery probability is at most \(2/m\). A repeated query makes no new discovery. Put a zero contribution after a branch stops; summing over the fixed horizon of \(G\) query times gives expected early discoveries at most \(2G/m\).

Every late discovery belongs to a column that receives at least \(m/2\) queries. The column query counts sum to at most \(G\), hence on every execution there are at most \(2G/m\) such columns. Each contributes at most one discovery. Writing \(Z=Z_{\mathrm{early}}+Z_{\mathrm{late}}\), we obtain
<!-- claim:claim-EZ -->
\[
\mathbb EZ_{\mathrm{early}}\le\frac{2G}{m},
\qquad
Z_{\mathrm{late}}\le\frac{2G}{m},
\qquad
\mathbb EZ\le\frac{4G}{m}.
\]
Together with the exact identity, this proves the complete display of the preprint:
<!-- claim:eq-19 -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
=\frac{\mathbb EZ}{m}
\le\frac{4G}{m^2}.
\tag{19}
\]
The equality, the endpoint bound, and this early/late derivation are distinct assertions. The supplied Lean evidence supports the first two through separate declarations; the endpoint's formal proof uses the alternative argument below.
<!-- /passage:CL-early-late -->

<!-- passage:CL-zero-worlds -->
**An alternative search estimate.** Fix one column and all data outside it. For every possible zero position \(j\), let \(x^j\) denote the input with its unique zero at \(j\) in that column. The worlds \(x^j\) agree on every outside bit. For \(U\subseteq[m]\), let \(D_U(T)\) count the worlds \(j\in U\) in which \(T(x^j)\) queries that zero, and let \(Q_U(T)\) sum the numbers of queries to this column over all these worlds. Repetitions and queries after discovering the zero are counted in \(Q_U(T)\).

We prove by induction on \(T\) that
<!-- claim:NCL-zero-worlds -->
\[
|U|D_U(T)\le2Q_U(T).
\]
A leaf has both counts zero. At a query outside the column, all worlds take the same subtree and incur no column query, so its induction hypothesis applies. At a column query to \(p\notin U\), all worlds take the answer-one subtree and each incurs one additional query; the inequality follows again.

If \(p\in U\), put \(V=U\setminus\{p\}\), \(n=|V|\), and write \(d=D_V(T_1)\), \(q=Q_V(T_1)\) for the answer-one subtree. Then \(nd\le2q\) by induction and \(d\le n\). World \(p\) finds its zero immediately, and all \(n+1\) worlds pay the root query. Therefore
\[
D_U(T)=1+d,\qquad Q_U(T)\ge n+1+q,
\]
and
\[
(n+1)(1+d)=nd+n+d+1
\le2q+2n+1
\le2(q+n+1)
\le2Q_U(T).
\]
This proves the inequality, including \(U=\varnothing\), without any assumption that a run stops after finding the zero.
<!-- /passage:CL-zero-worlds -->

<!-- passage:CL-zero-average -->
Take \(U=[m]\) and average uniformly over its \(m\) worlds. The preceding inequality says that this column's discovery probability is at most \(2/m\) times its expected query count. Average over the independent outside data and sum over the columns. If \(Q_X\) is the total number of queries to the \(X\)-bits, then \(Q_X\le G\) on every run, so
\[
\mathbb EZ\le\frac{2}{m}\mathbb E Q_X\le\frac{2G}{m}.
\]
The exact selection identity now yields
<!-- claim:NCL-erased-zero-two -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
\le\frac{2G}{m^2}.
\]
This is a stronger endpoint obtained by a different proof. It does not prove that the early/late decomposition was formalized, and it makes no assertion about the optimal distinguishing success at a fixed worst-case budget.
<!-- /passage:CL-zero-average -->

<!-- passage:CL-zero-optional -->
**An expectation-cost refinement.** The baseline contains a further ordinary refinement, which we retain separately. With the outside data fixed, run \(T\) on the reference input in which the selected column is all ones. List the distinct column positions on that reference path as \(p_1,\ldots,p_d\), in order of first appearance. A world with zero at \(p_s\) follows the reference path until that position is queried, so it discovers the zero and incurs at least \(s\) column queries. A world whose zero is absent from the list follows the whole reference path, incurs at least \(d\) column queries, and never discovers the zero. Hence exactly \(d\) worlds discover it, and their total query count together with the other worlds is at least
\[
1+\cdots+d+(m-d)d
=\frac{d(2m-d+1)}2
\ge\frac{d(m+1)}2.
\]
Averaging as above gives
<!-- claim:NCL-erased-zero-mplusone -->
\[
\mathbb EZ\le\frac{2}{m+1}\mathbb E Q_X,
\qquad
\Pr[T\text{ on }Y^{(0)}\text{ queries }X_I[J_I]]
\le\frac{2G}{m(m+1)}.
\]
Scanning one column without repetition until its zero is found attains the first, expectation-cost inequality, since its expected cost is \((m+1)/2\). Its worst-case cost is \(m\); this example does not establish an optimal success curve for each prescribed worst-case budget. No supplied Lean declaration proves this \(m+1\) refinement, and Proposition 4.2 needs neither it nor an optimality assertion.
<!-- /passage:CL-zero-optional -->

### 6.5. A capped simulator for the planted cell

<!-- passage:CL-heavy -->
Let \(q_i\) be the number of queries made during the complete dummy run to the strings \(A_{i,1},\ldots,A_{i,r}\), counting repetitions. Call column \(i\) heavy when \(q_i>L\). Since \(\sum_iq_i\le G\), the number of heavy columns is at most \(G/L\). Conditional on the dummy run, \(I\) is still uniform. Thus
<!-- claim:def-heavy -->
<!-- claim:eq-20 -->
\[
\Pr[I\text{ is heavy}]\le\frac{G}{mL}.
\tag{20}
\]
The threshold concerns the sum of the queries to all \(r\) strings of a column. In particular, a nonheavy run uses at most \(L\) queries to each of those strings.
<!-- /passage:CL-heavy -->

<!-- passage:CL-simulator -->
Fix a column \(i\) and a time \(q\in\{1,\ldots,G\}\). The simulator's queried inputs are the \(r\) strings of that column. Give it the independent outside data: every \(J_j\), all the \(A\)-strings of the other columns, and the fixed blank cells. It receives no target string, target address, or target transcript as side information.

Simulate \(T\) on the dummy input up to its proposed \(q\)-th query. Answer every outside query from the supplied data. Answer a query to one of the target strings by making the corresponding oracle query, charging it against one shared counter. Abort before that counter would exceed \(L\). If time \(q\) is reached and the proposed query is to \(B_{i,s}\), output \(s\). If the simulated run terminates, aborts, or proposes a different kind of coordinate, output a fixed vector. Identifying the proposed cell's address requires no query to its contents.
<!-- claim:def-simulator -->

For every possible tuple of target inputs, this simulator makes at most \(L\) target queries in total. It therefore satisfies each of the \(r\) separate caps in Lemma 4.1. The cap holds even on branches where the original tree would eventually make column \(i\) heavy. Because the outside data are jointly independent of the target tuple, the simulator's unconditional success is at most \((2/3)^r\).
<!-- /passage:CL-simulator -->

<!-- passage:CL-simulator-example -->
Return to the four-column XOR example and use \(L=1\), with both target strings independently uniform. Consider a four-query tree that first reads \(X_0[0]\), then the first bit \(a\) of \(A_{1,1}\). If \(a=1\), its third query is \(X_2[1]\); if \(a=0\), its third query is the first bit of \(A_{1,2}\). Its fourth query reads the first transcript's domain bit in \(B_{1,(a,0)}\), and it outputs that bit.

For the displayed planted configuration, the target first bit is \(1\). The simulator for \(i=1,q=4\) behaves as follows.

| Time | Proposed query | Simulator action | Target queries used |
|---|---|---|---:|
| 1 | \(X_0[0]\) | Answer \(1\) from the outside data. | 0 |
| 2 | First bit of \(A_{1,1}\) | Query the target oracle and receive \(1\). | 1 |
| 3 | \(X_2[1]\) | Answer \(1\) from the outside data. | 1 |
| 4 | Domain bit in \(B_{1,10}\) | Output address \(10\), before reading the cell bit. | 1 |

The original tree receives \(0\) at time four on the dummy input and \(1\) on the displayed planted input. The simulator uses the blank dummy data and stops before that answer. On the other branch, \(a=0\), it aborts before the second target query at time three. Thus its cap does not depend on retrospectively selecting the cheap executions.

The exact enumeration in the accompanying example fixes other columns' \(A\)-strings, ranges over all \(4^4\) zero-position vectors and all \(16\) target tuples, and independently ranges over the four choices of \(I\). It obtains
\[
\mathbb EZ=\frac38,\qquad
\Pr[\text{erased-zero hit}]=\frac3{32}
=\frac{\mathbb EZ}{4},
\]
and
\[
\Pr[\text{target 1 nonheavy and time 4 visits its true cell}]
=\frac18
\le
\Pr[\text{capped simulator correct}]
=\frac14.
\]
For uniform two-bit XOR, a one-query algorithm succeeds with probability at most \(1/2\), so \(1/4=(1/2)^2\) is the relevant two-input bound. These are exact finite computations for this toy and this conditional outside configuration. They illustrate the reduction; the general inequalities follow from the proofs.
<!-- /passage:CL-simulator-example -->

<!-- passage:CL-joint-event -->
Return to the general parameters and the hard distribution from §6.2. Suppose the complete dummy run makes column \(i\) nonheavy and proposes a query in \(B_{i,s_i}\) at time \(q\). Every preceding prefix then uses at most \(L\) target queries. The simulator has followed the original run without aborting and outputs \(s_i\). The joint event is therefore contained in the simulator's success event:
<!-- claim:eq-21 -->
\[
\Pr[i\text{ is nonheavy and query }q\text{ lies in }B_{i,s_i}]
\le(2/3)^r.
\tag{21}
\]
The event remains inside the probability. We have not changed the target input distribution by conditioning on nonheaviness.
<!-- /passage:CL-joint-event -->

<!-- passage:CL-conditioning-counterexample -->
That distinction is necessary in general. On the promised two-bit inputs \(\{01,10,11\}\), let \(P\) be AND and let \(\mu\) be uniform. Every one-query algorithm has success at most \(2/3\): after either coordinate is queried, one answer identifies a unique input and the other leaves two equally likely, oppositely labelled inputs.

A tree that queries the first bit can stop and correctly output \(0\) on the answer-zero branch, and query the second bit on the answer-one branch. With cap \(L=1\), the complete original run is nonheavy exactly on input \(01\). Its conditional success given nonheaviness is therefore \(1\). A simulator that aborts before the second query and defaults to \(0\) has unconditional success \(2/3\), while correct-and-nonheavy has probability \(1/3\). The unconditional bound is valid and the conditional bound \(1\le2/3\) is false. The example file checks all three inputs and every deterministic one-query tree.
<!-- /passage:CL-conditioning-counterexample -->

<!-- passage:CL-cell-union -->
If the dummy run visits the true cell of a nonheavy column \(i\), one of its at most \(G\) query times witnesses that visit. Union bounding (21) over the times gives probability at most \(G(2/3)^r\) for each fixed \(i\). Average over the independent uniform \(I\), then add (20):
<!-- claim:eq-22 -->
\[
\Pr[T\text{ on }Y^{(0)}\text{ queries a bit of }B_{I,s_I}]
\le\frac{G}{mL}+G(2/3)^r.
\tag{22}
\]
There is no extra factor \(m\): averaging the identical per-column upper bound divides the sum over the \(m\) columns by \(m\). Repeated cell visits cause no problem for a union bound. If \(G=0\), the union of query-time events is empty.
<!-- /passage:CL-cell-union -->

### 6.6. The discrepancy contradiction and the floors

<!-- passage:CL-discrepancy -->
Combining (18), (19), and (22) gives an absolute-value strengthening of the preprint's one-sided discrepancy estimate, with the same right-hand side:
<!-- claim:eq-23 -->
\[
\left|\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]\right|
\le\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\tag{23}
\]
The alternative search proof also gives
<!-- claim:new-r2-planted-gap-absolute-two -->
\[
\left|\Pr[T(Y^{(1)})=1]-\Pr[T(Y^{(0)})=1]\right|
\le\frac{2G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\]
The older core theorem proves the corresponding one-sided inequality, recorded in the baseline as NCL-checked-gap. The absolute-value bound above follows from the coupling argument and the stronger search estimate; the supplied Paper wrapper states that stronger endpoint. These formal endpoints do not identify the alternative proof with the paper's early/late derivation.
<!-- claim:NCL-checked-gap -->
<!-- /passage:CL-discrepancy -->

<!-- passage:CL-tail-numeric -->
Since \(1\le L\le m\) and \(G\le mL/100\), we have \(G\le m^2/100\). The chosen address length gives the paper's exact logarithmic tail:
<!-- claim:claim-tail -->
\[
G(2/3)^r
\le\frac1{100}m^{\,2-20\log_2(3/2)}
=o(1).
\]
Indeed, \((2/3)^{20\log_2m}=m^{-20\log_2(3/2)}\), and \((3/2)^2>2\) implies \(\log_2(3/2)>1/2\). The exponent is therefore less than \(-8\).

For the contradiction there is also a uniform finite estimate. From \(4/9\le1/2\) and \(r=40t\),
\[
(2/3)^{40t}\le2^{-20t}=m^{-10}.
\]
Thus
<!-- claim:claim-numeric -->
\[
\frac{4G}{m^2}\le\frac4{100},
\qquad
\frac{G}{mL}\le\frac1{100},
\qquad
G(2/3)^r\le\frac1{100m^8}\le\frac1{100},
\]
and
\[
\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r
\le\frac6{100}<\frac13.
\]
The weaker coefficient four already suffices. No further large-\(m\) condition is needed for this numerical step once \(1\le L\le m\) is known.
<!-- /passage:CL-tail-numeric -->

<!-- passage:CL-randomized-contradiction -->
Suppose a randomized algorithm with worst-case query cost at most \(G\) computed \(F_{P,C,m}\) with error at most \(1/3\) on every input. Every dummy input is a zero-input and every supported planted input is a one-input. Averaging the pointwise correctness requirements gives an output-one probability gap of at least \(2/3-1/3=1/3\).

Fix the algorithm's random coins. The resulting deterministic tree has depth at most \(G\), so its gap is at most \(6/100\). Averaging over the coins preserves that upper bound, contradicting the preceding lower bound. Since the total function has finitely many input bits, reading all of them computes it exactly; its randomized complexity is therefore a finite minimum. The absence of a budget-\(G\) algorithm implies \(R(F_{P,C,m})>G\), proving the generic theorem.

In the finite input model, random coins can be represented by a finite mixture of bounded-depth trees: there are only finitely many possible trees, so group coin outcomes by the tree they induce. This is an ordinary finite-behavior reduction. The Lean model directly uses finite mixtures; no theorem constructing a pushforward from an arbitrary external probability space is claimed here.
<!-- /passage:CL-randomized-contradiction -->

<!-- passage:CL-forrelation-input -->
We now return to the Forrelation family. Fix \(k\ge2\), let \(P=P_{k,m}\) on \(km\) bits, and choose
\[
L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
\]
The required prerequisite from §3 is that \(L<R(P_{k,m})\) for all sufficiently large powers of four \(m\).

For comparison, Bansal–Sinha [BS2020v3, Theorem 1.3 and Corollary 1.4, printed p. 4](https://arxiv.org/pdf/2008.07003v3) state, with promise threshold \(\delta=2^{-5k}\), a lower bound
\[
\Omega\!\left(k^{-29}
\left(\frac{m}{\log(km)}\right)^{1-1/k}\right)
\]
at error \(1/3\). Their block dimension is \(m\); the full input has \(km\) bits. For fixed \(k\) and \(m\ge k\), the ratio of a positive constant multiple of this bound to \(m^{1-1/k}/(\log_2m)^2\) is bounded below by a positive \(k\)-dependent constant times \((\log_2m)^{1+1/k}\). It tends to infinity, giving the strict prerequisite eventually.

This comparison identifies the original literature input and the exact strength used. The separate source audit of Bansal–Sinha v3 §5.4 concerns the displayed comparison at source lines 1180–1181: for a summation level \(j>k\), its logarithm exponents differ by \((j/k-1)/2\). The threshold at line 1184 is a subsequent statement. That discrepancy requires a separate argument for that displayed comparison; it does not refute the stated theorem. The present section consumes only the fixed-\(k\) prerequisite already established in the supplied §3 and its formal endpoint. It does not undertake a full re-audit of the sharper parameter-uniform theorem.
<!-- /passage:CL-forrelation-input -->

<!-- passage:CL-floors -->
We verify the remaining arithmetic with a threshold independent of \(k\). For every integer \(t\ge8\),
\[
4t^2\le2^t.
\]
There is equality at \(t=8\). If the inequality holds at \(t\ge8\), then \((t+1)^2\le2t^2\), because \(t^2-2t-1\ge0\). Hence \(4(t+1)^2\le8t^2\le2^{t+1}\), proving the induction.

Put \(a=m^{1-1/k}/(2t)^2\), where \(m=4^t\). Since \(1/2\le1-1/k\le1\),
\[
m^{1-1/k}\ge\sqrt m=2^t\ge(2t)^2,
\qquad
1\le a\le m.
\]
For every real \(x\ge1\), its natural floor satisfies \(\lfloor x\rfloor\ge x/2\): if \(b=\lfloor x\rfloor\), then \(b\ge1\) and \(x<b+1\le2b\). Thus \(1\le L\le m\) and \(L\ge a/2\).

Also \(mL\ge4^8\ge200\). Apply the same floor estimate to \(mL/100\):
\[
G\ge\frac{mL}{200}\ge\frac{ma}{400}.
\]
Since \(\log_2m=2t\), this gives the explicit form of the baseline floor statement:
<!-- claim:claim-floor -->
<!-- claim:NCL-explicit-floor -->
\[
\left\lfloor\frac m{100}
\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor\right\rfloor
\ge
\frac1{400}\frac{m^{2-1/k}}{(\log_2m)^2}
\quad(k\ge2,\ m=4^t,\ t\ge8).
\]
Both floors have been bounded in the direction needed for a lower bound.
<!-- /passage:CL-floors -->

<!-- passage:CL-concrete-lower -->
Choose \(t\) beyond both \(8\) and the fixed-\(k\) Forrelation threshold. Take the particular circuit \(C_{k,m}\) already used in §4 to define \(F_{k,m}\) and in §5 to prove its quantum upper bound. It realizes the same promise and value, so the generic lower theorem applies to this circuit.

**Proposition 4.2 (OpenAI).** For each fixed integer \(k\ge2\), for every sufficiently large power of four \(m\), the total function from the construction satisfies
<!-- claim:prop-4.2 -->
\[
R(F_{k,m})>
\left\lfloor\frac m{100}
\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor\right\rfloor.
\]
Together with the floor calculation, this yields
<!-- claim:cor-R-omega -->
\[
R(F_{k,m})\ge
\frac1{400}\frac{m^{2-1/k}}{(\log_2m)^2}
=\Omega_k\!\left(\frac{m^{2-1/k}}{(\log m)^2}\right).
\]
The explicit arithmetic coefficient is uniform in \(k\); the threshold supplied by Forrelation hardness may depend on the fixed \(k\). For natural logarithms the corresponding explicit coefficient is \((\ln 2)^2/400\).

The generic proof works for every realizing circuit, with a threshold independent of that circuit. Thus the same circuit can witness both sides of the eventual separation. Section 7 combines this lower bound with the upper bound on that function, obtaining exponent \(4-2/k\) up to logarithms for fixed \(k\). Varying the fixed choice of \(k\) rules out each universal exponent below four. No single fixed \(k\) in this argument gives an exact fourth-power family.
<!-- /passage:CL-concrete-lower -->

## Formal correspondence for this replacement

<!-- passage:CL-formal-scope -->
The accompanying correspondence records complete source signatures, available compiler-reported types, hypotheses, proof routes and receipt identities. It distinguishes the following facts.

- The exact identity in (19) is stated by QuarticQuery.Paper.erasedZero_eq_expectedZeros_div. The supplied current source-bound build and transitive axiom audit include it. Its algebraic identity is valid for arbitrary finite real weights; nonnegativity and normalization enter when the sums are interpreted as probabilities.
- QuarticQuery.Paper.eq_19 states only the upper bound. The exact identity and the bound are separately available, while the current corpus tie for the whole chained display remains partial. The proposed [lean/Eq19Complete.lean](lean/Eq19Complete.lean) conjoins the identity with the divided expected-zero bound. That new wrapper has not been compiled.
- QuarticQuery.Paper.uniform_zero_given_transcript states the positive-probability transcript posterior. QuarticQuery.Paper.expectedZeros_le_four proves the endpoint through the stronger zero-search induction; it does not formalize the early/late split.
- The supplied Paper wrappers state the absolute (18), the individual-time joint event (21), the cell bound (22), and the absolute discrepancy (23). The core one-sided discrepancy theorem is a separate, sufficient endpoint. In the source simulator, the proposed query time is zero-based; prose time \(q\) corresponds to source index \(q-1\).
- The exact logarithmic tail bound, its envelope limit, and the elementary finite power estimate are separately supplied. They have different statements and should retain distinct correspondence.
- QuarticQuery.Paper.prop_4_2 and QuarticQuery.Paper.prop_4_2_forrCircuit discharge the eventual fixed-\(k\) hardness premise through the supplied Forrelation theorem. The core Gvalue_lt_R_Fkm theorem remains explicitly conditional at its own type. Successful compilation of the former is not a reason to erase the binder from the latter.
- The \(m+1\) refinement, the elementary convex-separation proof, arbitrary-coin finite-behavior reduction, and the new finite examples are ordinary arguments or computations at their stated scope. They do not acquire formal proof status from nearby endpoint theorems.

These statements concern the frozen sources and receipts in the supplied packet. A matching build, an axiom audit, a Comparator result, intended-statement correspondence and human review remain separate kinds of evidence.
<!-- /passage:CL-formal-scope -->
