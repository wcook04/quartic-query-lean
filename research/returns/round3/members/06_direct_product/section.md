### 6.1. A direct product with a separate query cap on each input

<!-- Editorial integration: replace baseline §6.1 up to, but not including,
§6.2. Retain the existing §2.1 finite decision-tree and partial-function
conventions. The statement and proof below are independently readable.
The final application paragraph supplies the interface used in §6.5; it does
not assume an unpublished replacement for that section. -->

<!-- passage:CL-direct-product-statement -->
Independent instances remain hard to solve together when each has its own
query allowance. Adaptively choosing which instance to query does not remove
this restriction: at a fixed execution history the remaining inputs are still
independent, and one query can change only one factor in the product of the
one-input continuation values.

**Lemma 4.1 (capped direct product).** Let $D\subseteq\{0,1\}^{n}$, let
$P:D\to\{0,1\}$, let $\mu$ be a probability distribution supported on $D$,
and let $L,r\geq0$ be integers. Suppose that every deterministic Boolean-output
decision tree of depth at most $L$ has success probability at most $\beta$
for computing $P$ under $\mu$. Draw $U_1,\ldots,U_r$ independently from $\mu$.
A classical algorithm may choose queries adaptively among these inputs,
use random coins, and receive side information, provided that the side
information and coins together are independent of the entire tuple
$(U_1,\ldots,U_r)$. If it makes at most $L$ queries to each input on every
run, counting repeated queries, then

<!-- claim:lem-4.1 -->
\[
\Pr\!\left[\mathcal A(U_1,\ldots,U_r)
       =\bigl(P(U_1),\ldots,P(U_r)\bigr)\right]\leq\beta^r.
\tag{6.1}
\]

This is the statement of [OpenAI, §4.1, Lemma 4.1, pp. 11–12][openai].
Its one-input hypothesis concerns every bounded-depth strategy under a fixed
input law; it does not assert that every posterior encountered during the
algorithm is equally hard. The proof tracks the optimum under each posterior
with its remaining allowance. The case $L=0$ allows only constant guesses.
If $r=0$, the answer vector is empty and the bound is $1\leq1$.
<!-- /passage:CL-direct-product-statement -->

<!-- passage:CL-product-law -->
**Proof.** First fix the independent information and coins. The resulting
algorithm is a deterministic tree whose internal nodes ask for a coordinate
of one input and whose leaves output a vector in $\{0,1\}^r$. We return to
the averaging over this information after proving the deterministic case.

A history $\tau$ records, in order, the queried input, its queried coordinate,
and the answer. Write $H_\tau$ for the event that the run has this history
as a prefix. A terminal history additionally specifies that the tree has
reached its leaf. For each $h$, let $E_h(\tau)\subseteq D$ consist of the
inputs agreeing with every answer recorded from input $h$.

Consider a history with $\Pr(H_\tau)>0$. Its query schedule is compatible
with the deterministic tree. Every run with this history satisfies all the
local constraints. Conversely, any tuple satisfying them follows the same
history: its first answer agrees with the record; the deterministic choice
of the next query is therefore the recorded choice; induction repeats this
argument at every step. If the history ends at a leaf, the same argument
also gives the stop and its output. Thus

<!-- claim:claim-product-law -->
\[
 H_\tau=\bigcap_{h=1}^{r}\{U_h\in E_h(\tau)\},\qquad
 \Pr(H_\tau)=\prod_{h=1}^{r}\mu(E_h(\tau)),\qquad
 \mathcal L(U_1,\ldots,U_r\mid H_\tau)
   =\bigotimes_{h=1}^{r}\mu(\,\cdot\mid E_h(\tau)).
\tag{6.2}
\]

For the last identity, the conditional mass of a compatible tuple is its
product mass divided by $\prod_h\mu(E_h(\tau))$; the quotient factors into
the separate conditional masses. Every denominator is positive because
$H_\tau$ has positive probability. No independence between the bits within
one input is required.

The schedule qualification matters. An arbitrary string of proposed queries
can have consistent local bit constraints while asking a different first
query from the tree, so its actual execution event is empty. Contradictory
answers to a repeated query also give an empty event. We assign no conditional
law to either kind of impossible history. Such histories have zero weight
in all the finite averages below. Repeating a consistent answer leaves the
constraint set unchanged, although it still spends a query.
<!-- /passage:CL-product-law -->

<!-- passage:CL-conditional-values -->
Let $q_h(\tau)$ count the queries to input $h$ in $\tau$, including
repetitions. At a positive-probability history of the capped algorithm,
$q_h(\tau)\leq L$. To measure what can still be learned from that input,
define

<!-- claim:def-value-V -->
\[
 V_h(\tau)=
 \max_{\operatorname{depth}(T)\leq L-q_h(\tau)}
 \Pr\!\left[T(U_h)=P(U_h)\mid U_h\in E_h(\tau)\right].
\tag{6.3}
\]

The maximization ranges over single-input deterministic trees. Such trees
are finite in number for a fixed depth: a depth-zero tree is one of two
leaves, and a tree of positive bounded depth is either a leaf or a choice of
one of $n$ coordinates and two smaller trees. Hence the maximum is attained.
Stopping immediately is allowed, so $1/2\leq V_h(\tau)\leq1$.

Suppose the next query asks coordinate $a$ of input $h$. There is a query
left in that input's allowance. For each answer $b$ of positive conditional
probability, choose a tree attaining $V_h(\tau b)$, where $\tau b$ appends
this query and answer. Querying $a$ first and then running the chosen tree
uses at most $L-q_h(\tau)$ queries. Its conditional success is the average
of those new optimal values. Optimality in (6.3) therefore gives

<!-- claim:eq-16 -->
\[
 \sum_{b:\,\Pr(U_h(a)=b\mid H_\tau)>0}
   \Pr(U_h(a)=b\mid H_\tau)\,V_h(\tau b)
   \leq V_h(\tau).
\tag{6.4}
\]

This is the finite form of the preprint's equation (16). A branch of
conditional probability zero contributes zero; any tree can be installed
on that unreachable branch without defining a posterior there. If the
coordinate was queried earlier, only its already-known answer is possible.
The budget decreases and its posterior is unchanged, which again cannot
increase the optimum.

For $j\neq h$, the local constraints, posterior, and remaining budget are
unchanged. Thus $V_j(\tau b)=V_j(\tau)$ on every positive-probability child.
This is where the transcript product law is used: learning a bit of $U_h$
does not change the conditional law of any other input.
<!-- /passage:CL-conditional-values -->

<!-- passage:CL-supermartingale -->
Let $Z(\tau)=\prod_{h=1}^{r}V_h(\tau)$. The other factors are unchanged
and nonnegative, so multiplying (6.4) by their product gives

<!-- claim:claim-supermartingale -->
\[
 \mathbb E[Z(\tau')\mid H_\tau]\leq Z(\tau),
\tag{6.5}
\]

where $\tau'$ is the history after the next query. This product inequality
does not follow merely from knowing that each factor separately has
nonincreasing expectation. It follows because exactly one factor can change
at a step, while the others are fixed by the current history.

The tree makes at most $rL$ queries. Keep $Z$ constant after an early stop
and sum (6.5) over positive-probability histories at each of these finitely
many steps. At the empty history each factor is at most $\beta$ by the
one-input hypothesis. Consequently the expected terminal product is at most
its initial value, which is at most $\beta^r$. This finite iteration needs
no limiting stopping theorem.

Write $U=(U_1,\ldots,U_r)$. At a terminal history, let $s=(s_1,\ldots,s_r)$
be the fixed answer vector.
The remaining product law and the option of stopping immediately give

<!-- claim:claim-final-bound -->
\[
\begin{aligned}
 \Pr[\mathcal A(U)=P^r(U)\mid H_\tau]
 &=\prod_{h=1}^{r}\Pr[P(U_h)=s_h\mid H_\tau]\\
 &\leq\prod_{h=1}^{r}\max_{b\in\{0,1\}}
               \Pr[P(U_h)=b\mid H_\tau]\\
 &\leq\prod_{h=1}^{r}V_h(\tau)=Z(\tau),
\end{aligned}
\tag{6.6}
\]

where $P^r(U)$ denotes $(P(U_1),\ldots,P(U_r))$. Averaging over the terminal
histories proves (6.1) for the deterministic algorithm. The comparison in
(6.6) bounds a conditional probability, rather than bounding the realized
success indicator pointwise by $Z$; on a successful input that indicator
can equal one while $Z<1$.
<!-- /passage:CL-supermartingale -->

<!-- passage:CL-independent-information -->
To restore arbitrary independent side information and coins, group their
outcomes by the capped deterministic tree they induce. There are only
finitely many such trees: their depth is at most $rL$, their query labels
belong to a finite set, and their leaf labels belong to $\{0,1\}^r$.
The same induction on depth used above proves this finiteness. If a
description of an algorithm includes unreachable branches, truncate those
branches before any excess query; this leaves its actual capped runs
unchanged and ensures the structural cap on every branch of the induced
tree. Thus even a continuous space of independent information yields a
finite mixture of relevant deterministic behaviors.

For each mixture component, independence leaves the input law equal to
$\mu^{\otimes r}$ and the success bound equal to $\beta^r$. The weighted
average has the same bound, completing the proof. Independence here is from
the whole input tuple, including jointly the information and the random
tape. Independence from each input separately would not justify this
argument. For example, take $P(x)=x$ on one fair bit, $L=0$, and two
independent inputs $X,Y$. Their parity $S=X\oplus Y$ is independent of
either input separately. Given $S$, the zero-query answer $(0,S)$ is
correct whenever $X=0$, with probability $1/2$, exceeding the bound
$(1/2)^2$ for jointly independent information. The proof uses the joint
condition directly. $\square$
<!-- /passage:CL-independent-information -->

<!-- passage:CL-joint-cap -->
**Corollary (success together with respecting the caps).** Under the
one-input and independence hypotheses of Lemma 4.1, let $\mathcal A$ be any
finite adaptive vector-output algorithm, with no cap imposed on every run.
Let $Q_h$ be its terminal number of queries to input $h$, counting
repetitions, and put $E=\{Q_h\leq L\text{ for every }h\}$. Then

<!-- claim:NCL-joint-cap -->
\[
 \Pr\!\left[\mathcal A(U)=P^r(U)\ \text{and}\ E\right]\leq\beta^r.
\tag{6.7}
\]

Construct $\mathcal A^{\leq L}$ by following $\mathcal A$ and stopping
immediately before the first query that would make some count $L+1$.
At such a stop output an arbitrary fixed vector. This modified algorithm
obeys every cap on every branch, including branches with inconsistent
repeated-query answers. On $E$, no prefix can exceed a terminal count, so
truncation never occurs and the two algorithms have identical outputs.
Every original run in the joint event in (6.7) is therefore a successful
run of $\mathcal A^{\leq L}$. Applying (6.1) proves (6.7). The truncation
can be performed after fixing the independent information and coins and
then averaged, just as above. $\square$

The event $E$ remains inside the probability in (6.7). Conditioning on $E$
can change both the independence of the inputs and their one-input
difficulty. If a conditional estimate were established by some separate
argument, multiplying it by $\Pr(E)$ would of course bound the joint event;
the point is that the hypotheses of Lemma 4.1 do not supply that conditional
estimate. The following example gives an explicit failure.
<!-- /passage:CL-joint-cap -->

<!-- passage:CL-adaptive-example -->
**An adaptive example.** Let $P(x_0,x_1)=x_0\wedge x_1$ on a uniform pair
of bits and set $L=1$. A one-query algorithm succeeds with probability at
most $\beta=3/4$: after reading a zero the answer is known, while after
reading a one the other fair bit leaves maximum success $1/2$. Averaging
gives $3/4$, also attained by the constant answer zero.

Take independent inputs $A=(A_0,A_1)$ and $B=(B_0,B_1)$. Query $A_0=a$,
then query $B_a=t$. If $a\neq t$, query $A_0$ again. In every case output
$(0,0)$. The second query is chosen adaptively; the repeated query spends
budget without gaining information. The cap event is $E=\{a=t\}$.

Each row below has probability $1/4$. Its compatible inputs form the
rectangle $\{A:A_0=a\}\times\{B:B_a=t\}$, and its conditional success
is the product of the two separate best-guess probabilities.

| $a$ | Second query | $t$ | Conditional success | Terminal counts | $E$ |
|---:|:---:|---:|:---:|:---:|:---:|
| 0 | $B_0$ | 0 | $1$ | $(1,1)$ | yes |
| 0 | $B_0$ | 1 | $1/2$ | $(2,1)$ | no |
| 1 | $B_1$ | 0 | $1/2$ | $(2,1)$ | no |
| 1 | $B_1$ | 1 | $1/4$ | $(1,1)$ | yes |

Writing $C$ for correctness of the output vector, the first and last rows
give

<!-- claim:NCL-adaptive-cap-example -->
\[
 \Pr(E)=\frac12,\qquad
 \Pr(C\cap E)=\frac5{16}\leq\frac9{16}=\beta^2,
 \qquad \Pr(C\mid E)=\frac58>\beta^2.
\tag{6.8}
\]

The cap event selects a union of rectangles, not a single execution
history. It creates dependence: under $E$, the probabilities of $A_0=0$
and $B_0=0$ are $1/2$ and $3/4$, whereas their joint probability is $1/2$,
rather than $3/8$. Truncating before the repeated query, with output $(0,0)$
at the new stops, gives a valid capped tree with success $9/16$ and proves
the required upper bound on $5/16$.

The same distribution distinguishes the two budget conditions. With a
total budget $rL=2$, an algorithm can compute $P(A)$ exactly and guess zero
for $P(B)$, succeeding with probability $3/4>9/16$. A total budget $L=1$,
on the other hand, implies the separate caps and does satisfy Lemma 4.1.
The exact calculation and enumeration in [worked_example.md](worked_example.md)
check all 16 input pairs, all 10 one-input trees of depth at most one, and
all 5,188 vector-output trees satisfying the separate caps. This finite check
illustrates the proof and its limits; the preceding argument proves the
general theorem.
<!-- /passage:CL-adaptive-example -->

<!-- passage:CL-weighted-values -->
**The proof with unnormalized weights.** There is also a direct finite-sum
proof that makes all impossible branches vanish automatically. Extend $\mu$
by zero outside $D$, and regard $P$ as a partial Boolean function on the full
cube, so off-promise inputs never count as correct. Let $\nu$ be any
nonnegative weight on that cube and
write $\nu_{a,b}(x)=\nu(x)\mathbf1_{\{x_a=b\}}$. Define

<!-- claim:NCL-weighted-value -->
\[
\begin{aligned}
 W_0(\nu)&=\max_{b\in\{0,1\}}\sum_{x\in D:P(x)=b}\nu(x),\\
 W_{c+1}(\nu)&=\max\!\left\{W_c(\nu),\
       \max_{a}\bigl(W_c(\nu_{a,0})+W_c(\nu_{a,1})\bigr)\right\}.
\end{aligned}
\tag{6.9}
\]

If there are no coordinates, the inner maximum is omitted. The first term
in the second line retains any strategy using the old allowance; the
remaining terms describe querying $a$ and using its two best continuations.

Induction proves that $W_c(\nu)$ is exactly the maximum weighted success
of a tree of depth at most $c$. At depth zero the two constants are the
only choices. At the next depth, each displayed candidate is attained by
an old optimal tree or by a query followed by two optimal smaller trees.
Conversely, every tree is a constant or starts with some query $a$; splitting
its success sum by that answer bounds it by the corresponding candidate.
This proves both directions. In particular, $W_c$ is nonnegative and
nondecreasing in $c$, and the two branch values with one fewer query sum
to at most the old value. A nonnegative weight of mass zero vanishes
pointwise, so all its success values are zero.
<!-- /passage:CL-weighted-values -->

<!-- passage:CL-weighted-product -->
Give input $h$ its own nonnegative weight $\nu_h$ and allowance $c_h$. For any
vector-output tree $T$ respecting these allowances on every branch, we claim

<!-- claim:NCL-weighted-product -->
\[
 \sum_{u_1,\ldots,u_r\in D}
    \left(\prod_{h=1}^{r}\nu_h(u_h)\right)
    \mathbf1_{\{T(u_1,\ldots,u_r)=(P(u_1),\ldots,P(u_r))\}}
 \leq\prod_{h=1}^{r}W_{c_h}(\nu_h).
\tag{6.10}
\]

We prove this by induction on $T$. At a leaf with output $s$, finite
distributivity factors the left side into
$\prod_h\sum_{x\in D:P(x)=s_h}\nu_h(x)$; every factor is bounded by
$W_{c_h}(\nu_h)$. At a query to coordinate $a$ of input $h$, we have
$c_h>0$. Split the success sum by the answer $b$. In that branch, replace
only $\nu_h$ by $\nu_{h,a,b}$ and only $c_h$ by $c_h-1$. The subtrees
obey those new allowances, so induction bounds their two successes by the
corresponding products. Every factor other than the $h$-th is the same.
Factoring those common nonnegative factors out leaves the sum
$W_{c_h-1}(\nu_{h,a,0})+W_{c_h-1}(\nu_{h,a,1})$, which (6.9) bounds by
$W_{c_h}(\nu_h)$. This proves (6.10). Taking $\nu_h=\mu$ and $c_h=L$
recovers (6.1), since the one-input hypothesis gives $W_L(\mu)\leq\beta$.
<!-- /passage:CL-weighted-product -->

<!-- passage:CL-normalization -->
The two proofs use the same one-factor calculation. At a positive history,
put $\nu_h^\tau=\mu\mathbf1_{E_h(\tau)}$. Dividing each tree's weighted
success by the positive mass $\mu(E_h(\tau))$ commutes with the finite
maximum defining its optimum. Hence

<!-- claim:NCL-product-normalization -->
\[
 V_h(\tau)=\frac{W_{L-q_h(\tau)}(\nu_h^\tau)}{\mu(E_h(\tau))},
 \qquad
 \Pr(H_\tau)\,Z(\tau)
   =\prod_{h=1}^{r}W_{L-q_h(\tau)}(\nu_h^\tau).
\tag{6.11}
\]

The second identity follows by cancelling the product of masses from
(6.2). Thus a transcript's probability times its normalized potential is
exactly its unnormalized product value. The weighted induction proves the
bound without divisions; the conditional proof explains why adaptivity
does not create an advantage.
<!-- /passage:CL-normalization -->

<!-- passage:CL-planted-interface -->
**Use in the planted argument.** In §6.5, a simulator fixes the dummy data
outside a target column and treats that column's $r$ partial-function
inputs as independent samples from the hard distribution. It stops before
its $(L+1)$-st target query in total, which implies the separate allowance
$L$ for every target input. Its outside data must be independent of the
whole target tuple; it cannot include the hidden true address. With
$\beta=2/3$, Lemma 4.1 bounds the simulator's probability of outputting the
true address by $(2/3)^r$.

If the original dummy run is nonheavy and its proposed query at a fixed
time visits the true-address cell, the simulator reaches that query without
truncation and outputs its address. The joint event is therefore contained
in simulator success. This gives the fixed-time bound used in equation (21)
of the preprint, after which §6.5 takes a union over query times. The
argument neither conditions the hard input law on nonheaviness nor requires
independence between the queries made at different times.
<!-- /passage:CL-planted-interface -->

<!-- passage:CL-literature-and-verification -->
**Sources and formal correspondence.** The proof above follows the
conditional-value argument in [OpenAI, §4.1][openai]. Its prior proof source
is [Drucker, arXiv:1005.0644v2, §1.3, Lemmas 3.1–3.2 on printed pp. 11–12,
and the last paragraph of §3 on p. 13][drucker]. Drucker's Theorem 1.1
instead treats a global budget $\alpha\varepsilon Tk$ and obtains
$(2^{\alpha\varepsilon}(1-\varepsilon))^k$; it is not the statement (6.1).
The earlier [Shaltiel, ECCC TR01-009, §5, Definition 4, Theorem 5, and
Lemma 7, printed pp. 11–12][shaltiel] defines fairness by at most a separate
allowance on every root-to-leaf path and proves an XOR-advantage inequality
in the report's uniform-input setting. Its advantage is $2\Pr[\mathrm{correct}]-1$.
These are related proof antecedents, with different stated targets and
input-law conventions; the vector-output claim for the present hard law
has been proved above.

The source `QuarticQuery.LowerBound.DirectProduct` proves (6.10) by
unnormalized induction and exports `QuarticQuery.direct_product` and its
finite-mixture versions. The additional source
`QuarticQuery.Paper.ClassicalDirectProduct` proves the transcript product
law, the conditional-value inequality, finite product iteration, and the
bound on actual terminal success, ending in
`QuarticQuery.Paper.classical_direct_product` and
`QuarticQuery.Paper.classical_direct_product_average`. It expresses finite
conditional expectations directly, without a Mathlib `Supermartingale`
instance. It reuses the one-input optimization lemmas, and does not invoke
the older multi-input direct-product theorem to prove its endpoint.

The supplied receipts record successful native compilation of these exact
source bytes; this review made no fresh Lean run. The headline dependency
closure still uses the unnormalized route, and no exact-declaration
Comparator pass is supplied for these helpers. The conditional-value file's
old “UNELABORATED” header predates the successful receipts. Exact types,
byte checks, declaration membership, and the limits
of the recorded evidence are in `correspondence.json`, `lean_types.json`,
and `LEAN_GAPS.md`. The arbitrary-information finite-behavior reduction,
the generic joint-event truncation corollary, and the combined identity
(6.11) are ordinary deductions supplied here; they are not new Lean builds
or new Comparator passes. The worked example is a separate exact finite
calculation. This replacement was prepared with AI assistance and has
received no human mathematical review.
<!-- /passage:CL-literature-and-verification -->

[openai]: https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf
[drucker]: https://arxiv.org/pdf/1005.0644v2
[shaltiel]: https://eccc.weizmann.ac.il/report/2001/009/download/
