# A nearly quartic separation between randomized and quantum queries: a complete reasoning record

**AI assistance and attribution.** Will Cook directed this reconstruction. AI agents produced the local Lean formalization, explanatory additions and this manuscript. OpenAI authored the separation theorem and source preprint; the earlier mathematical ingredients retain their named authors' credit. No human mathematical review or publication acceptance is claimed.

## 1. The result and its scope

<a id="ROOT-RESULT"></a>
<!-- passage:ROOT-RESULT -->
For total Boolean functions, the optimal universal power relating bounded-error randomized and quantum query complexity is four. OpenAI's preprint constructs the functions that rule out every smaller power. The universal quartic upper bound was already known: Aaronson, Ben-David, Kothari, Rao and Tal proved that deterministic query complexity satisfies $D(f)=O(Q(f)^4)$, which also bounds randomized complexity because $R(f)\leq D(f)$. The attribution is to [OpenAI (2026), Theorem 1.1 and §1][OpenAI2026] for the separation, and to [Aaronson et al., Theorem 2, printed p. 2 of arXiv v1][ABKRT2020] for the upper bound.

A query accesses one input bit. Computation between queries is free. The quantities $R(f)$ and $Q(f)$ are the least **worst-case query caps** for randomized and quantum algorithms whose success probability is at least $2/3$ on each permitted input. In particular, the cap applies to every random choice and every measurement branch. Section 2 gives the precise models.

<!-- claim:eq-1 -->
Define

\[
\alpha_{\mathrm{tot}}
=\inf\left\{\alpha\geq0:\ 
  \exists C_\alpha>0\ \forall n\geq1\ 
  \forall f:\{0,1\}^n\to\{0,1\},\quad
  R(f)\leq C_\alpha(1+Q(f))^\alpha
\right\}.
\tag{1}
\]

One constant must work for every input length and every total function. The preprint permits any finite real constant; the positive-constant formulation in (1) is equivalent, since a witness $C$ can be replaced by $\max(C,1)$. The additive $1$ includes constant functions without requiring a convention for $0^0$.

<!-- claim:thm-1.1 -->
**Theorem 1.1 (OpenAI).** The optimal power is $\alpha_{\mathrm{tot}}=4$. More precisely, there is an absolute constant $C>0$ such that every total Boolean function satisfies

\[
R(f)\leq C(1+Q(f))^4.
\]

For each fixed integer $k\geq2$, there are positive constants $c_k,C_k,b_k$, a threshold $m_0(k)$, and total Boolean functions $F_{k,m}$, defined for all powers of four $m\geq m_0(k)$, for which

<!-- claim:eq-2 -->
\[
Q(F_{k,m})\leq C_k\sqrt m\,(\log_2 m)^{b_k},
\qquad
R(F_{k,m})\geq c_k\frac{m^{2-1/k}}{(\log_2 m)^2}.
\tag{2}
\]

The two inequalities concern the **same function** at each pair $(k,m)$. In the supplied development, one specified circuit family gives $b_k=6$ and permits $c_k=1/400$, after increasing the threshold. Its correspondence with the preprint and the recorded formal evidence are given in §§2.7–2.8.
<!-- /passage:ROOT-RESULT -->

<a id="R3-01-QUANTIFIERS"></a>
<!-- passage:R3-01-QUANTIFIERS -->
The order of choices in (2) is essential: choose $k$, then its constants and threshold, then let $m$ grow through powers of four. This suffices to exclude every universal power below four. Indeed, fix $0\leq\alpha<4$ and choose an integer $k\geq2$ with $k>2/(4-\alpha)$. Then

<!-- claim:claim-exponent-ratio -->
\[
2-\frac1k-\frac\alpha2>0,
\qquad
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\geq
\frac{c_k}{(1+C_k)^\alpha}
\frac{m^{\,2-1/k-\alpha/2}}
     {(\log_2m)^{\,2+\alpha b_k}}
\longrightarrow\infty.
\]

For sufficiently large $m$, the upper bound in (2) gives

\[
1+Q(F_{k,m})\leq(1+C_k)\sqrt m\,(\log_2m)^{b_k};
\]

raising this positive inequality to the nonnegative power $\alpha$ proves the displayed ratio bound. A positive power of $m$ exceeds every fixed power of its logarithm, so no constant $C_\alpha$ in (1) exists. The universal upper bound places $4$ in the defining set, and that set is nonempty and bounded below by zero. Its infimum is therefore $4$. Section 7 retains the complete parameter argument.

For a fixed $k$, this reasoning excludes powers strictly below $4-2/k$. It does not produce an exact fourth-power separation for that fixed $k$, and these fixed-$k$ total-family bounds do not supply the joint uniform control needed for a growing-$k$ total-function schedule. No such uniform assertion is needed for the conclusion about the infimum.

<!-- claim:cor-cubic-refuted -->
Already $k=3$ gives $4-2/k=10/3>3$, so

\[
\neg\exists C\in\mathbb R\ \forall n\geq1\
\forall f:\{0,1\}^n\to\{0,1\},\qquad R(f)\leq C Q(f)^3.
\]

This refutes [Aaronson et al., Conjecture 2, §7, printed p. 20 of arXiv v1][ABKRT2020]. Replacing $C$ by $\max(C,1)$ would turn such a bound into a universal shifted cubic bound, already excluded above.
<!-- /passage:R3-01-QUANTIFIERS -->

<a id="ROOT-ARCHITECTURE"></a>
<!-- passage:ROOT-ARCHITECTURE -->
### 1.1. Certificates that disqualify every other candidate

The construction places an accepting certificate in one of $m$ columns. Each column has a string $X_i\in\{0,1\}^m$, several separate inputs to a partial function $P_{k,m}$, and an array of certificate cells. The values of those partial-function inputs determine the address of the relevant cell. For fixed $k$, quantum computation of each promised value is cheap, whereas classical computation is hard. A circuit transcript in the cell certifies the values that form its address.

A column wins if its string is all ones, its address is defined, its transcript is correct, and its cell points to a zero in every other column. These conditions define a total Boolean function: every input either has a winner or does not, regardless of whether any particular address instance satisfies its promise. There is at most one winner. If $i$ and $j\ne i$ both won, the pointer from $i$ would identify a zero in $X_j$, contradicting the requirement that $X_j$ be all ones.

The outward direction of these pointers explains the quantum construction. A genuine winner can use its own certificate to reject every opponent. No opponent's pointer can find a zero in the winner's all-one string. Thus the comparison with a winner remains reliable even when the opponent's address computation is off promise. Comparisons between two losing columns may behave arbitrarily. The tournament in §5 uses only the reliable comparisons involving a winner; a final verification rejects a candidate whose local tests fail. This is the mechanism described in [OpenAI, §1.2][OpenAI2026].

For the randomized lower bound, begin with one hidden zero in every column and blank cells. Erase the zero in a random column and fill its correctly addressed cell with a valid certificate. The resulting input has a winner. A classical algorithm must encounter one of those changes to distinguish the two inputs. Finding the erased zero is rare under a small query cap; finding the filled cell requires enough information about its vector of hard partial-function values. The direct-product argument in §6 makes the second assertion precise for adaptive queries. Together they give a lower budget of order $mL$, while quantum evaluation costs order $\sqrt m$ times logarithmic factors.

The record follows these dependencies: §3 establishes the partial-function ingredients; §4 defines the columns, transcripts and total function; §§5–6 prove its quantum and randomized bounds; §7 compares exponents. Appendix A gives the independent universal upper bound. The finite model examples below explain the conventions used throughout; they are not small instances of the separation construction.
<!-- /passage:ROOT-ARCHITECTURE -->


<a id="record-dependencies"></a>
**Dependencies and proof recovery.** The central construction can be read after §§3.1–3.5 and the precise ingredient statement in §3.17; §§3.6–3.16 recover the full independent classical-hardness argument when needed. They remain in their original numbered location so every returned proof locator stays usable.

| Mathematical object | Exact use | Complete argument |
| --- | --- | --- |
| Bit-query models and promises | Fix the meaning of every complexity bound | [§2](#ROOT-PARTIAL) |
| One-sided Forrelation, coherent decoder, exact circuit | Define and certify each address | [§§3.1–3.5](#forr_definition), [§3.17](#forr_bundle) |
| Forrelation randomized lower bound | Supply a hard law at cap $L$ | [§§3.6–3.16](#forr_target) |
| Total addressed function and local tests | Fix the same function for both bounds | [§4](#AC-interface) |
| Complementary comparisons and exact successful-label law | Obtain the all-input quantum cap | [§5](#upper-purpose) |
| Capped product, planting and first difference | Obtain the randomized lower bound | [§6](#CL-direct-product-statement) |
| Fixed-$k$ quotient and universal bound | Prove the optimal exponent is four | [§7](#ROOT-FAMILY-ASSEMBLY), [Appendix A](#R3-A-RESULT) |
| Exact claim statements and declared proof boundaries | Recover formal correspondence without replacing the proofs | [Appendix B](#ROOT-CATALOGUE-INTRO) |

The earlier [short expert draft](../research/returns/funnel/2_short_expert_paper/) and [examples-first draft](../research/returns/funnel/3_examples_first_exposition/) are preserved advisory returns. They have not been refreshed against this integration. Their main theorem belongs to §§1 and 7 here; their construction, tournament and planted proof belong to §§4, 5 and 6.

## 2. Models, promises and query budgets

<a id="ROOT-LOGS"></a>
<!-- passage:ROOT-LOGS -->
Unqualified logarithms in the construction are base two. Natural logarithms are written $\ln$ when analytic estimates require them. The size parameter is $m=4^t=2^{2t}$, so $\log_2m=2t$ and $\sqrt m=2^t$ exactly. Changes of logarithm base in asymptotic estimates affect constants only; they must not silently change the integers defined by a floor or a ceiling. The source definitions at $t=0$, or at other parameters outside the stated ranges, are totalized mathematical expressions. They do not enlarge the domain of the asymptotic theorem.
<!-- /passage:ROOT-LOGS -->

<a id="ROOT-PARTIAL"></a>
<!-- passage:ROOT-PARTIAL -->
### 2.1. Inputs and partial functions

Let $I$ be a finite set of coordinates and put $\mathcal X_I=\{0,1\}^I$. A partial Boolean function is a domain $\mathcal D\subseteq\mathcal X_I$ together with a map $f:\mathcal D\to\{0,1\}$. Equivalently, it is a map from $\mathcal X_I$ to $\{\mathrm{none},\mathrm{some}(0),\mathrm{some}(1)\}$: `none` means that no correctness requirement is imposed at that input. This is the source type `PartialBool I`. Taking the defined inputs as the domain and their unique Boolean labels as the values reverses the translation.

An algorithm for a partial function is one algorithm that works on every promised input. Its behavior outside $\mathcal D$ can be arbitrary, but its query cap still applies there. In particular, the program, its random probabilities and its quantum starting state cannot be chosen after learning the input. This separates the quantifiers “there is an algorithm, for every input” from the incorrect “for every input, there is an algorithm.”

The source operation `totalise` embeds an **already total** function $g:\mathcal X_I\to\{0,1\}$ by sending $x$ to `some (g x)`. It does not complete a partial function by replacing `none` with false. When a read-all algorithm needs an output off promise, it may choose false there; that is a choice of algorithm, not a change to $f$. The translation and its correctness conditions are proved by the domain wrappers in `Paper/ConstructionModels.lean`.
<!-- /passage:ROOT-PARTIAL -->

<a id="R3-01-CLASSICAL"></a>
<!-- passage:R3-01-CLASSICAL -->
### 2.2. Deterministic trees and finite random mixtures

A deterministic query tree has a Boolean label at every leaf and a coordinate $i\in I$ at every internal node. At that node, the next subtree is selected by the input bit $x_i$. Write $T(x)$ for the resulting output. The source charges the syntactic depth

\[
\operatorname{depth}(\operatorname{leaf}(b))=0,
\qquad
\operatorname{depth}(\operatorname{query}(i,T_0,T_1))
=1+\max\{\operatorname{depth}(T_0),\operatorname{depth}(T_1)\}.
\]

Repeated queries are charged again. A repeated query can create a branch inconsistent with answers already obtained; syntactic depth still counts it. Such branches can be removed by carrying the previously known answers down the tree and replacing a repeated query by its consistent child. Evaluation is unchanged and depth cannot increase. In the resulting tree every path has a consistent input assignment, so its depth is attained on an input. Thus this convention preserves the minimum worst-case query cost.

<!-- claim:def-D -->
The predicate $D_{\leq}(f,q)$, written `DLe f q` in Lean, means that there is one tree $T$ of depth at most $q$ with $T(x)=f(x)$ for every $x\in\mathcal D$. Define

\[
D(f)=\min\{q\in\mathbb N:D_{\leq}(f,q)\}.
\]

A randomized program is a finite list of trees $T_1,\ldots,T_s$ with real weights $p_j>0$ and $\sum_jp_j=1$. It selects $j$ independently of the input and runs $T_j$. Its depth is $\max_j\operatorname{depth}(T_j)$, and its success probability on a promised input is $\sum_{j:T_j(x)=f(x)}p_j$. Positive weights merely discard entries of probability zero; the normalization forces $s\geq1$.

<!-- claim:def-R -->
Write $R_{\leq}(f,q)$, or `RLe f q`, for the existence of such a mixture with depth at most $q$ and success at least $2/3$ on every promised input. The randomized complexity is

\[
R(f)=\min\left\{q\in\mathbb N:\
\exists(p_j,T_j)_{j=1}^s\quad
\begin{array}{l}
p_j>0,\quad \sum_jp_j=1,\quad \operatorname{depth}(T_j)\leq q\ \text{for every }j,\\[2pt]
\displaystyle \sum_{j:T_j(x)=f(x)}p_j\geq\frac23\ \text{for every }x\in\mathcal D
\end{array}\right\}.
\]

This is the distribution-over-trees convention in [Buhrman and de Wolf, §§3.1–3.2, printed pp. 5–6][BDW02]. For fixed $I$ and $q$, there are finitely many trees of depth at most $q$: at depth zero there are two leaves, and a larger tree chooses a coordinate and two smaller trees. Fixing all random choices of a capped randomized algorithm selects one such tree; grouping outcomes that select the same tree gives a finite mixture. Conversely, a finite distribution can be selected with finitely many biased coin choices before reading the input. These observations preserve the cap and pointwise success probabilities. They use the allowed arbitrary real biases; a separate restriction to a bounded number of fair coin flips requires care at an exact error threshold.

The minima exist. Query all coordinates once, then output the prescribed value on the promise and any bit elsewhere. This tree has depth at most $|I|$, including when $I$ is empty. A tree is also a one-element randomized mixture. The admissible budgets are therefore nonempty upward-closed subsets of $\mathbb N$, giving

\[
R(f)\leq q\iff R_{\leq}(f,q),\qquad
D(f)\leq q\iff D_{\leq}(f,q),\qquad
R(f)\leq D(f)\leq |I|.
\]

In the source these minima are natural-number infima. The read-all witness is what makes them minima of nonempty sets; the value assigned to an empty infimum does no work. The constructor-by-constructor translation to complexitylib's `DecisionTree` preserves both evaluation and depth, and gives the exact equality `D_totalise_eq_complexity` for total functions.
<!-- /passage:R3-01-CLASSICAL -->

<a id="ROOT-ORACLE"></a>
<!-- passage:ROOT-ORACLE -->
### 2.3. The oracle and finite workspaces

For nonempty $I$, use a finite-dimensional complex Hilbert space with basis $|i,b,z\rangle$, where $i\in I$, $b\in\{0,1\}$, and $z$ is a workspace label. The source uses $z\in\operatorname{Fin}(w+1)$, $w\in\mathbb N$, so the workspace is nonempty. All gates are input-independent linear isometries of this space. In finite equal dimensions an isometry is surjective and hence unitary. No bound on gate count, gate synthesis or workspace size is part of query complexity.

<!-- claim:def-query-oracle -->
The bit oracle acts by

\[
O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle.
\]

It permutes an orthonormal basis and is its own inverse, so it is unitary. With the answer bit in $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$, one call multiplies the amplitude at $i$ by $(-1)^{x_i}$. With the answer bit in $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$, the same call acts as the identity; this is an idle bit query. For a converse that preserves one query, retain the control bit: define

\[
P_x|i,b,z\rangle=(-1)^{b x_i}|i,b,z\rangle.
\]

If $H_b$ denotes a Hadamard on that bit, $H_bP_xH_b=O_x$, because $HZH=X$ on the answer bit when $x_i=1$ and $HIH=I$ when $x_i=0$. Thus the bit oracle and this **controlled phase oracle** are interchangeable at one call. A bare oracle $|i\rangle\mapsto(-1)^{x_i}|i\rangle$, without a control or idle facility, does not justify the converse: complementing every input bit changes that oracle only by a global sign. The distinction appears in [de Wolf, v6, §2.4, printed pp. 17–18, footnote 7 and Exercise 10][DW26]. In this edition §2.3 is “Quantum parallelism.”

The finite coordinate projector onto a basis subset $S$ is $\Pi_S$. A two-outcome measurement uses the branches $\Pi_S\psi$ and $(I-\Pi_S)\psi$. These span orthogonal subspaces and have squared norms summing to $\|\psi\|^2$. General binary orthogonal projectors can be put into this form by an input-independent change of orthonormal basis. An arbitrary normalized pure starting state can likewise be prepared from a chosen basis vector by a free unitary. These finite-dimensional conventions agree with the standard query model described in [Buhrman and de Wolf, §3.3][BDW02] and the measurement conventions in [de Wolf, §§1.2.2 and 2.1.2][DW26].
<!-- /passage:ROOT-ORACLE -->

<a id="R3-01-ADAPTIVE"></a>
<!-- passage:R3-01-ADAPTIVE -->
### 2.4. Measurements, probability mass and the quantum minimum

A source program is a finite expression made from four operations: return a Boolean answer; apply a unitary and continue; apply the oracle and continue; or measure a basis subset and follow one of two continuations. Its query cap is zero at a return, unchanged at a unitary, increased by one at a query, and the maximum of the two continuation caps at a measurement. Even a branch of probability zero for a particular input is charged by this syntactic cap. This makes the cap independent of the input, including off-promise inputs.

Keep branch vectors unnormalized. For program $A$, input $x$, vector $\psi$, and output bit $b$, let $M_A(x,\psi,b)$ denote its output mass. A return of $a$ contributes $\|\psi\|^2$ if $a=b$ and zero otherwise. A gate or query substitutes the transformed vector into the continuation. A measurement with continuations $A_1,A_0$ gives

\[
M_A(x,\psi,b)
=M_{A_1}(x,\Pi_S\psi,b)
 +M_{A_0}(x,(I-\Pi_S)\psi,b).
\]

<!-- claim:ROOT-MASS -->
For every starting vector, including the zero vector,

\[
M_A(x,\psi,b)\geq0,
\qquad
M_A(x,\psi,1)+M_A(x,\psi,0)=\|\psi\|^2.
\]

Both claims follow by structural induction. At a return they are immediate. A unitary or oracle preserves the norm, so the induction hypothesis applies after that transformation. At a measurement, nonnegativity is preserved by addition; summing over the two output bits and applying the induction hypotheses gives $\|\Pi_S\psi\|^2+\|(I-\Pi_S)\psi\|^2=\|\psi\|^2$. Thus a normalized starting vector gives an ordinary probability distribution. Renormalizing each branch and then adding its mass without restoring the branch probability would fail this identity.

<!-- claim:def-Q -->
The predicate `QLe f q` is the following disjunction:

\[
\begin{split}
&\bigl[\exists b\in\{0,1\}\ \forall x\in\mathcal D,\ f(x)=b\bigr]\\
&\quad\lor\
\bigl[\exists w,\psi_0,A:\ \|\psi_0\|=1,\ 
  \operatorname{cap}(A)\leq q,\ 
  \forall x\in\mathcal D,\ M_A(x,\psi_0,f(x))\geq2/3\bigr].
\end{split}
\]

Every existential choice in the second clause precedes the input quantifier. The first clause permits a constant answer with no query register. It is redundant when a nonempty query register is available, but necessary for the source representation when $I=\varnothing$: there is then one possible input and no unit vector in the zero-dimensional indexed query space. Every partial Boolean function on that singleton input set is constant on its promise, including an empty promise. The clause therefore supplies exactly the expected zero-query behavior.

Define $Q(f)=\min\{q\in\mathbb N:\text{`QLe f q'}\}$. To see that this minimum exists, simulate a deterministic tree. On a nonempty coordinate set, prepare the basis state for its next query with answer bit zero, query once, measure the answer bit, and follow the corresponding child. Each child has its own input-independent basis permutation preparing its next coordinate. The classical history is already encoded by the program branch. Induction on the tree gives the same output and no larger cap. Constant trees, including those on empty coordinates, use the first clause. Hence

\[
Q(f)\leq D(f)\leq |I|,
\qquad
Q(f)\leq q\iff\text{`QLe f q'}.
\]

As in the classical case, nonemptiness and monotonicity of admissible budgets justify the source's natural-number infimum.
<!-- /passage:R3-01-ADAPTIVE -->

<a id="R3-01-BRIDGES"></a>
<!-- passage:R3-01-BRIDGES -->
### 2.5. Renaming coordinates and deferring measurements

A bijection $e:I\to J$ changes only the names of the queried bits. If $f^e(y)=f(y\circ e)$, relabel every classical query node by $e$. Evaluation and depth are unchanged. For quantum programs the corresponding basis permutation relabels the query register, conjugates each gate and projector, and transports the initial vector. It intertwines the two bit oracles; induction on the program preserves both output masses and the cap. Applying the inverse permutation gives

\[
R(f^e)=R(f),\qquad D(f^e)=D(f),\qquad Q(f^e)=Q(f).
\]

This is why structured coordinates in the construction can be replaced by $\operatorname{Fin}(n)$ in (1).

The deferred-measurement bridge has a more specific guarantee than a statement that measurements may be postponed. For $A$ on $\operatorname{Fin}(n)$ with cap at most $T$, the source constructs a larger finite workspace, an input-independent entry isometry $E$, a fixed sequence of $T$ controlled phase queries separated by input-independent gates, and a final accepting projector $\Pi$, such that

\[
\left\|\Pi\,U_TP'_xU_{T-1}\cdots P'_xU_0E\psi\right\|^2
=M_A(x,\psi,1)
\quad\text{for every }x\text{ and every }\psi.
\]

Here $P'_x$ is the controlled phase oracle on the enlarged workspace. The source induction retains, besides the entry map, an auxiliary isometry $J$ satisfying $P'_xJ=JP_x$. An output branch accepts either its whole space or the empty set; padding queries preserve its norm, although they may change its state. A free gate is absorbed into the entry map. At a measurement, if $E_1,E_0$ are the continuation entry maps, enter their direct sum through

\[
\psi\longmapsto E_1\Pi_S\psi\oplus E_0(I-\Pi_S)\psi.
\]

This is an isometry, the gates and oracle act block by block, and acceptance masses add. For a query followed by a continuation with entry $L$ and compatible embedding $J$, extend the isometry $J\phi\mapsto LH_b\phi$ from $\operatorname{range}(J)$ to an input-independent unitary $Z$ of the larger finite space. The extension exists because the two isometric ranges have equal dimension, as do their orthogonal complements. Starting through $JH_b$, one controlled phase query followed by $Z$ gives

\[
ZP'_xJH_b\psi=LH_bP_xH_b\psi=LO_x\psi.
\]

The remaining $T-1$ queries run the continuation. The output case allows both measurement continuations to be padded to the same $T$, so structural induction gives the displayed mass identity with exactly $T$ queries. This padding preserves acceptance mass; the source does not require a completed branch's state to remain unchanged.

This is the statement of `exists_fixedSequence`. It preserves the accepting mass for all inputs and all starting vectors; it does not identify final states or permit discarding a workspace when a later computation needs it. Conversely, a finite bit-query sequence followed by a binary basis measurement is directly a finite adaptive program, by writing its gates and queries as successive constructors. The general bridge, rather than the finite examples in §2.6, is what connects the formal model to the fixed-sequence model used by the imported universal upper bound.
<!-- /passage:R3-01-BRIDGES -->

<a id="R3-01-ZERO"></a>
<!-- passage:R3-01-ZERO -->
### 2.6. Exact small examples

**Zero queries.** For a finite coordinate set,

\[
R(f)=0\quad\Longleftrightarrow\quad D(f)=0
\quad\Longleftrightarrow\quad Q(f)=0
\quad\Longleftrightarrow\quad
f\text{ is constant on its promise}.
\]

A constant answer proves one direction. For the converse, a zero-depth tree is a leaf, and a zero-depth random mixture has an input-independent output distribution. A zero-query quantum program also has input-independent masses: induct on its syntax, observing that a query constructor is impossible at cap zero and that gates, projections and branch rules are input-independent. If both Boolean labels occurred on the promise, correctness would require the same distribution to put mass at least $2/3$ on each label. Their masses sum to one, a contradiction. This is an ordinary proof of the stated characterizations; the earlier fidelity return proposes corresponding Lean checks, but the packet supplies no successful receipt for those exact example declarations.
<!-- /passage:R3-01-ZERO -->

<a id="R3-01-IDENTITY"></a>
<!-- passage:R3-01-IDENTITY -->
**One-bit identity.** For $f(x)=x_0$, both labels occur, so zero queries are impossible. One classical query returns the bit, and one quantum bit query on $|0,0,z\rangle$ followed by measuring the answer does the same. Thus

\[
D(\mathrm{id}_1)=R(\mathrm{id}_1)=Q(\mathrm{id}_1)=1.
\]
<!-- /passage:R3-01-IDENTITY -->

<a id="R3-01-OR"></a>
<!-- passage:R3-01-OR -->
**Two-bit OR and the endpoint $2/3$.** With equal probabilities choose one of three trees: output $1$, query and output $x_0$, or query and output $x_1$. The maximum depth is one, and the exact successes are

| Input | OR | Constant $1$ | Output $x_0$ | Output $x_1$ | Success probability |
| --- | ---: | ---: | ---: | ---: | ---: |
| $00$ | 0 | 1 | 0 | 0 | $2/3$ |
| $01$ | 1 | 1 | 0 | 1 | $2/3$ |
| $10$ | 1 | 1 | 1 | 0 | $2/3$ |
| $11$ | 1 | 1 | 1 | 1 | $1$ |

Zero queries are impossible. A deterministic one-query tree reads at most one coordinate, and cannot distinguish $00$ from the input whose other bit alone is $1$. Therefore

\[
R(\mathrm{OR}_2)=1,\qquad D(\mathrm{OR}_2)=2.
\]

The inclusive threshold is material. Under the uniform distribution on $00,01,10$, every deterministic tree of depth at most one is correct on at most two of those three inputs. A mixture therefore has average success at most $2/3$, and cannot succeed with probability strictly greater than $2/3$ at every input. Requiring strict success above $2/3$ raises the classical cap to two. This argument also shows that finite sampling with arbitrary biases cannot simply be replaced by a fixed finite number of fair flips: to attain the optimum, all supported response functions must be among $1,x_0,x_1$, and the three pointwise requirements force their aggregate probabilities to be $1/3$ each. Those probabilities are not dyadic.

The selector can also be sampled quantumly before any input query: prepare three orthogonal selector states with amplitudes $1/\sqrt3$, measure the selector using binary coordinate projections, and follow the corresponding constant or one-query program. A larger finite workspace holds the selector. The branch cap is one and the success table is unchanged, so $Q(\mathrm{OR}_2)=1$ as well. The upper bound on one-query **classical** success above is not a quantum optimal-success statement.
<!-- /passage:R3-01-OR -->

<a id="R3-01-OFFPROMISE"></a>
<!-- passage:R3-01-OFFPROMISE -->
**An off-promise input is not a false input.** On one bit, let $f(1)=1$ and leave $f(0)$ undefined. The constant-one algorithm has success one on the entire promise and zero query cost. Consequently $D(f)=R(f)=Q(f)=0$. Replacing its undefined value by false creates one-bit identity, whose three complexities are one. This numerical difference detects a change of problem. Empty promises and partial functions on empty coordinate sets also have all three complexities zero. For every one of these examples, a chosen program's cap remains a bound on its off-promise executions.
<!-- /passage:R3-01-OFFPROMISE -->

<a id="R3-01-PARITY"></a>
<!-- passage:R3-01-PARITY -->
**Two-bit parity checks the cost convention.** For $x_0\oplus x_1$, any deterministic one-query tree is correct on exactly half the four inputs. The same is true on average for every mixture, ruling out pointwise success $2/3$; reading both bits is exact. A quantum algorithm instead prepares

\[
\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|-\rangle.
\]

After one bit query and a Hadamard on the index register, its index amplitudes are

\[
\frac{(-1)^{x_0}+(-1)^{x_1}}2\quad\text{and}\quad
\frac{(-1)^{x_0}-(-1)^{x_1}}2.
\]

Measuring the index returns the parity exactly. The zero-query argument excludes cost zero, so

\[
D(\mathrm{XOR}_2)=R(\mathrm{XOR}_2)=2,
\qquad Q(\mathrm{XOR}_2)=1.
\]

The supplied 1998 version of Beals et al., §3.2 and the paragraph following Proposition 6.4, measures classical randomized cost by **expected** queries. Its exact classical parity figure must not be imported into the present cap model. The later author-hosted journal version changes §3.2 to worst-case query cost and states the corresponding classical parity bound after Proposition 6.4. We cite these separately as [Beals et al. (1998)][BBCMW98] and [Beals et al. (2001)][BBCMW01]. The calculation above directly establishes the two-bit values needed here.
<!-- /passage:R3-01-PARITY -->

<a id="ROOT-EVIDENCE-CONVENTION"></a>
<!-- passage:ROOT-EVIDENCE-CONVENTION -->
### 2.7. What the formal models establish

The formal interpretation starts with the order of the mathematical choices: choose one algorithm, then require its correctness and its query cap for every relevant input. A theorem about a differently quantified algorithm, a different promise, or only one part of a displayed conjunction would not establish the same statement. The definitions in §§2.1–2.5 make these choices explicit. Here we describe their formal counterparts and the particular translations used later. Complete source signatures, including the circuit and workspace quantifiers, are accessible in the retained [model contract](../research/returns/round3/members/01_models_evidence/model_contract.json) and [declaration correspondence](../research/returns/round3/members/01_models_evidence/correspondence.json); [Appendix B](#ROOT-CATALOGUE-INTRO) follows every numbered source claim.

**The partial function and its domain.** For a finite coordinate type $I$, the formal object `PartialBool I` is the function type `BitInput I → Option Bool`. A defined value records both membership in the promise and the required answer. An undefined value imposes no correctness requirement. This is the domain-and-value description of §2.1, with no assumption of totality. The operation `totalise` embeds a total Boolean function into this type by defining its value everywhere. It is that embedding, rather than an arbitrary completion of a partial function, which appears in the total-function separation statements.

**One algorithm and a global cap.** The predicates `DLe`, `RLe` and `QLe` take a partial Boolean function and a natural-number budget; `D`, `R` and `Q` are natural-number complexities. In the classical cases, the witness is one decision tree or one mixture of trees, with a global depth cap and correctness on all defined inputs. In the quantum case, the witness is either the explicitly constant-on-promise alternative or one normalized initial state and one capped program, chosen before the input. This includes the constant and empty-promise cases without selecting an algorithm separately for each input. None of these definitions assumes a lower-bound theorem or any property of Forrelation.

For every finite Boolean promise the read-all construction gives
\[
 R(f)\le D(f),\qquad Q(f)\le D(f),\qquad D(f)\le |I|.
\]
An equivalence $e:I\simeq J$ simply renames the coordinates. The three complexities of `reindex e f` equal the corresponding complexities of $f$. These statements concern arbitrary finite promises: their only ordinary premises are the specified finite coordinate types and, for renaming, the equivalence. The results `D_le_iff`, `R_le_iff` and `Q_le_iff` connect the numerical complexities to the budget predicates. The uniform choice and global cap remain inside those predicates; they cannot be discarded when applying the numerical inequalities.

**The physical query and its output law.** With $x$ a bit input, $i\in I$, a response bit $b$, and workspace label $z\in\operatorname{Fin}(w+1)$, the oracle acts by
\[
 \operatorname{bitOracle}_x|i,b,z\rangle
   =|i,b\mathbin{\oplus}x_i,z\rangle.
\]
It is an involutive complex linear isometry equivalence, for every input and every basis label. The exact construction wrapper is `Paper.construction_query_oracle`. For an adaptive program $A$ and an arbitrary state vector $\psi$, the two output masses obey
\[
 \operatorname{outputMass}_A(x,\psi,b)\ge0,
 \qquad
 \operatorname{outputMass}_A(x,\psi,\mathsf{true})
 +\operatorname{outputMass}_A(x,\psi,\mathsf{false})=\|\psi\|^2.
\]
Normalization makes these masses a probability distribution. The identities themselves do not require a unit vector; this distinction matters when an intermediate branch carries unnormalized mass.

**Deferring measurements with the same witnesses.** For an adaptive program on $\operatorname{Fin}(n)$ with workspace parameter $w$ and query cap at most $T$, `exists_fixedSequence` supplies an enlarged workspace, an entry map, a fixed sequence $U$ and an output event $S$. All these witnesses are chosen before the input and initial vector. For every $x$ and $\psi$, the mass of $S$ after the length-$T$ sequence on the entered vector equals the original program's true-output mass. For a normalized vector these masses are probabilities. In symbols, the quantifier order is
\[
 \exists W',\operatorname{entry},U,S\quad\forall x,\psi:\qquad
 \operatorname{measureProb}\bigl(\operatorname{run}
 U(\operatorname{entry}\psi)\,x\,T,S\bigr)
 =\operatorname{outputMass}_A(x,\psi,\mathsf{true}).
\]
The full witness types are those of the linked source contract. The stated cap is the only additional premise of this translation. In particular, this output-law theorem should not be read as identifying a designated retained subsystem with an arbitrary normalized successful state; the stronger amplification issue is isolated in §5.5.

**The family and the universal exponent.** `UniversalPower` is a predicate on real exponents, and the formal `alphaTot` is the infimum of the exponents satisfying it. Its quantifiers range over total Boolean functions on $\operatorname{Fin}(n)$, with $n\ge1$ and exponent $\alpha\ge0$, as in (1). The finite-constant and infimum formulations are explicitly related by the source wrappers. No Forrelation hypothesis belongs to this definition.

For fixed $k\ge2$, `Paper.construction_equation_two` gives the real-power family bound (2), and `Paper.construction_family_named` names its circuit and constants. The constants and threshold are chosen after $k$ and before the size, and one circuit at each size satisfies both the quantum upper bound and the randomized lower bound. The fixed-parameter Forrelation estimate is supplied inside the unconditional proof. The complete declaration `theorem_1_1_unconditional` packages the common-circuit eventual family in the integer form
\[
 R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor,
 \qquad
 L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor,
\]
together with `alphaTot = 4` and `UniversalPower 4`. Its range and threshold occur inside the conclusion. The floor-removal argument and full types are recorded in the correspondence; the integer statement and the real-power statement should not be conflated merely because they describe the same family.

The parameter-free `alphaTot_eq_four_unconditional` gives the exponent alone. The cubic refutation states that there is no common real constant $C$ for which
\[
 \bigl(R(\operatorname{totalise}f)\bigr)_{\mathbb R}
 \le C\bigl(Q(\operatorname{totalise}f)\bigr)_{\mathbb R}^{3}
\]
for every $n\ge1$ and total $f$ on $\operatorname{Fin}(n)$. The universal upper endpoint `universalPower_four` proves `UniversalPower 4`; the headline proof uses the imported complexity-library route described in Appendix A. These are unconditional declarations. By contrast, `family_bounds` retains the premise `Lvalue k t < R (P k t)` in its lower-bound clause, and `theorem_1_1` has the explicit parameter `h : BansalSinhaLower`. Citing either of those conditional suppliers alone does not remove its hypothesis. A restriction such as $k\ge2$ and an unproved lower-bound assumption play different mathematical roles, and their actual types preserve that difference.

### 2.8. Execution evidence and checks of meaning

Theorem and equation numbers refer to the OpenAI preprint; section numbers refer to this record unless another source is named. The section-specific build and comparison descriptions report the frozen snapshots inspected in the retained returns, principally proof checkpoint `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a` and packet checkpoint `1dd469dd0042b937b739da3bc211eeb60bdf7462`. The returned review checked agreement of the complete local Lean and configuration hash dictionaries with the enclosed source bytes despite the different commit labels. Those historical receipts do not certify later edits. [Appendix B](#ROOT-CATALOGUE-INTRO) and [the dated integration review](reasoning_record_review.json) give the maintained record's evidence boundary.

The frozen receipts record a successful root build and comparisons in the Foundations, Separation and Unconditional bundles; Unconditional also records a paranoid pass. In Foundations the named comparisons include `D_le_iff`, `R_le_iff`, `Q_le_iff`, each of the three read-all inequalities, and the $R$ and $Q$ renaming equalities. The $D$ renaming equality is built but has no named comparison in that packet. The partial-domain/correctness wrappers, oracle wrapper, output-mass identities, deferred-measurement theorem, and equivalent universal-exponent formulations likewise have build support there, without a named comparison. The real-power family has a build and a supplied selected axiom audit, without a named comparison. Unconditional compares the complete floor-form theorem, exponent endpoint and cubic refutation; Separation compares the universal upper endpoint. Comparison membership belongs to those exact declarations, not automatically to every declaration used by their proofs. An absent named comparison is recorded as unknown, rather than inferred from a nearby passing wrapper.

The challenges compile separately but mechanically share the maintained definitions and theorem specifications. Their agreement therefore establishes conformity to that specification; source review and independently specified examples address its mathematical meaning. The dependency export separately records which declarations are used by particular headline proof roots. It is not another compilation or comparison result. The retained return rechecked source-byte bindings and exact finite examples without rerunning Lean or Comparator. Its dependency pins are bound, but it does not enclose the external checkout bytes and native compiled artifacts needed for a full replay. It reports no human review.

The examples in §2.6 establish their stated costs by ordinary proofs and exact finite arithmetic. The section's exact-arithmetic checker verifies the truth tables, the one-query classical OR obstruction and the two-bit quantum interference calculation; that frozen record has no exact-example Lean or Comparator receipts. Its separate finite semantic controls distinguish per-input algorithm selection, a weakened success threshold, false completion of an undefined value, minimum rather than maximum branch cost, a strict rather than inclusive success threshold, and two deliberately wrong promise/comparison specifications. These are different failure modes of the intended model, so matching the controls is useful evidence about the definitions. It does not prove general model equivalence or constitute a Lean or Comparator execution. Conversely, a comparison of a shared specification does not, merely by passing, establish that specification's intended meaning. Ordinary proofs, full declaration types, Lean execution, Comparator execution and review of mathematical fidelity remain separate throughout this record.


The maintained [semantic controls](../lean/QuarticCorpus/Independent/Semantics.lean) give independently specified finite expectations directly against the project definitions: one-bit identity cannot have randomized cap zero; the three-way OR mixture has success $(2/3,2/3,2/3,1)$ and randomized complexity one; the true-only promise has randomized and quantum complexity zero; and the pair of sign blocks $(-1,1,1,1)$ has Forrelation value $-1$ and lies outside the one-sided promise. A concrete fair comparison matrix also witnesses that the actual tournament predicate is nonempty. These checks import the actual definitions but do not obtain their expected answers from generated Challenge statements. The [mutation checks](../lean/QuarticCorpus/Independent/SemanticMutations.lean) show how changing the algorithm/input quantifier order, making the threshold strict, taking an absolute value in the high Forrelation branch, or completing the undefined input by false changes the selected answers. Their scope is these precise examples, not a proof that every semantic mismatch has been excluded.

A separate [shared-specification control](../lean/QuarticCorpus/Independent/Controls/SharedAudit.lean) makes the limitation of comparison concrete. Its deliberately bad tournament predicate adds an impossible field. Two modules can agree on the resulting vacuous assertion, whereas the independent expected matrix cannot satisfy that predicate. The changed-threshold and inequality-only controls instead ask comparison to distinguish different types or definitions. The dated review records their actual native outcomes separately from the mathematical detection statements; a positive comparison of the deliberately shared bad specification is evidence of agreement, not of a correct model.

**Current targeted verification.** The integration's [native receipt of 2 November 2026](../corpus/receipts/lean-build-round3-targeted-2026-11-02T204814950389+0000.json) records successful builds and type/axiom inspection for the two equation (19) conjunctions, the independently specified product experiment, the construction strengthened by the support diagnostic, and the named finite semantic checks. All 18 inspected declarations use only `propext`, `Classical.choice` and `Quot.sound` as transitive axioms. On the same source snapshot, the dedicated Comparators accepted the [construction conjunction](../corpus/receipts/comparator-round3-construction-support-2026-11-02T204814950389+0000.json), the [independent product-law target](../corpus/receipts/comparator-round3-eq19-independent-2026-11-02T204814950389+0000.json), and [`eq19_whole`](../corpus/receipts/comparator-round3-eq19-direct-2026-11-02T204814950389+0000.json). The other whole-display wrapper, `eq_19_complete`, has build and axiom evidence but no separate Comparator receipt; acceptance is not transferred between the two forms.

The deliberate [missing-equality](../corpus/receipts/comparator-round3-eq19-missing-equality-2026-11-02T204814950389+0000.json) and [changed-threshold](../corpus/receipts/comparator-round3-threshold-mutation-2026-11-02T204814950389+0000.json) cases were rejected for their intended mismatches. The [shared impossible-premise case](../corpus/receipts/comparator-round3-shared-bad-spec-blindness-2026-11-02T204814950389+0000.json) was accepted, exactly as the blind-spot experiment predicts. Its receipt is a negative-control record with no credited paper declarations, not a semantic correctness certificate. These are targeted source-bound results. The dated integration review separately records the global build, comparisons and dependency export; their scope is not inferred from the targeted runs.

**Current global verification.** The same source snapshot also has a successful [root build and dependency export](../corpus/receipts/lean-build-root-2026-11-02T205500674428+0000.json). The refreshed [Foundations](../corpus/receipts/comparator-Foundations-2026-11-02T205755119082+0000.json), [Construction](../corpus/receipts/comparator-Construction-2026-11-02T205620278544+0000.json), [Tournament](../corpus/receipts/comparator-Tournament-2026-11-02T210431678518+0000.json), [Separation](../corpus/receipts/comparator-Separation-2026-11-02T210108868598+0000.json) and [Unconditional](../corpus/receipts/comparator-Unconditional-2026-11-02T211003816536+0000.json) bundles all passed their named comparisons; Unconditional also passed a separate [paranoid check](../corpus/receipts/comparator-Unconditional-2026-11-02T212245429608+0000.json). The existing controls for a changed definition, foreign axiom, missing declaration, admitted proof and weakened conclusion were rejected for their intended reasons. The full receipt inventory is retained in the integrated correspondence.

Every catalogue row now has a current mathematical-fidelity review and at least one qualifying built declaration. This does not make every complete row a Lean theorem or a compared theorem: the reviewed relations remain 51 exact, 31 stronger and 39 partial. Only 4 rows (Lemma 2.2, its parts (i) and (ii), and equation (19)) have direct comparison evidence: Comparator was configured with their own declarations. Eight more, including Theorem 1.1 and the definitions of $R$, $Q$ and $D$, were credited by earlier receipts only because a compared wrapper theorem restates them; that credit is recorded as wrapper-mediated, not as a comparison of the declaration itself. The other rows' comparison state is `not_run` under the evidence policy, not an inference that no historical comparison ever occurred. Dependency reach is a further question about particular proof roots, recorded independently of build and comparison. The remaining formal boundaries, including arbitrary-information transport and the physical successful-state bridge, are still stated explicitly.

**Inspecting the selected formal dependencies.** The [recorded native views](../corpus/native_extractions/round3/README.md) expose the complete selected local closures for the direct equation (19) conjunction, the independently specified product-law conjunction, and the finite semantic goals. They retain the actual adapter reports, graphs, selected views, build receipts and successful validate/select/inspect commands. Their local reports have complete scope, but each exported graph remains explicitly partial at external Mathlib, Init and Batteries declarations. These views make the stated formal objects and their dependencies inspectable; they are not an additional proof, a mathematical-fidelity judgment or a fresh-clone reproducibility result.

<!-- /passage:ROOT-EVIDENCE-CONVENTION -->

## 3. Forrelation: promise, circuit, and randomized hardness

<a id="forr_scope"></a>
<!-- passage:forr_scope -->
We use the bit oracle and quantum query model of §§2.3–2.4. It supplies the quantum and circuit conclusions consumed by §3.17; the randomized lower bound remains in §§3.6–3.16. Fix an integer $k\ge2$, let $t\ge1$ be an integer, and put $m=4^t$. All unqualified logarithms are base two; natural logarithms are written $\ln$. The input consists of $k$ blocks of $m$ bits.

The construction needs two ways of using the same partial function. A quantum procedure proposes its value with small error whenever the promise holds. An exact Boolean circuit certifies both that the promise holds and that a proposed value is correct. The first procedure must still produce an output on unpromised inputs; the second must identify those inputs exactly. OpenAI's Lemma 2.1(ii)–(iii) asks for these two properties [OpenAI2026, §2.1, pp. 3–5].

<!-- /passage:forr_scope -->

<a id="forr_definition"></a>
<!-- passage:forr_definition -->
### 3.1. The normalized Walsh product and the promise

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

Aaronson and Ambainis introduced the $k$-fold quantity and its quantum interpretation [AA18, §1.1.3 and §3.2]. The parameterized promise above is Bansal–Sinha's equations (1.1)–(1.3), with their block length $N$ equal to our $m$; their Theorem 1.3 chooses $\delta=2^{-5k}$ [BansalSinha2021]. Their $N=2^n$ permits any power of two. Our specialization $n=2t$ makes $m=4^t$, and hence $\sqrt m=2^t$, integral. It is useful for the exact arithmetic below and is not required for Walsh orthogonality or the quantum preparation. Aaronson–Ambainis's numerical promise thresholds are different, so that paper supplies the antecedent construction rather than these particular thresholds.

To keep the interface with the later lower bound fixed, retain

<!-- claim:eq-5 -->
$$
L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
$$

Here $\log_2m=2t>0$. No lower bound involving $L_{k,m}$ is proved in these five subsections.
<!-- /passage:forr_definition -->

<a id="forr_integer"></a>
<!-- passage:forr_integer -->
### 3.2. An integer numerator and exact promise tests

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

<a id="forr_quantum"></a>
<!-- passage:forr_quantum -->
### 3.3. The quantum promise algorithm, including amplification and coherence

Start the address register in $u$. For the fixed input $z$, write

$$
U_z=D_{z_0}H D_{z_1}H\cdots H D_{z_{k-1}},
\qquad \psi_z=U_zu.
$$

Apply this word from right to left. To implement $D_{z_r}$, put the oracle answer qubit in $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$. The bit oracle of §2.3 acts by

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

<a id="forr_repetition"></a>
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

<a id="forr_coherent"></a>
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

Here $Q_\eta$ is the minimum worst-case number of ordinary bit queries needed for error at most $\eta$ on every promised input, with the cap holding on every input. It extends §2.4's convention $Q=Q_{1/3}$. The coherent state just constructed also has that fixed cap.

<!-- claim:lem-2.1.ii -->
**Formal implementation of the asymptotic conclusion.** Instantiating the supplied coherent sampler at $q$ repetitions gives $qk$ abstract reads; its generic compiler uses at most $2qk$ physical bit queries. The complete Lemma 2.1(ii) wrapper packages this construction with a repetition count $n$ and law existentially quantified; its proof chooses $n=q$. It binds one isometry $F_z$, one initial basis state, one output labeling, and that isometry's measured law. The physical implementation applies the same $F_z$ before every subsequent continuation and adds at most $2nk$ to the continuation's cap. This connects coherence, the measured law, and the physical cost in one witness, proving the required $O_k(1+\log(1/\eta))$ conclusion. The explicit ceiling choice is supplied by the repetition and decoder theorems, rather than asserted by the wrapper's existential statement alone.

The local phase-kickback identity has also been compiled, but it does not yet supply a complete formal program with the sharper $qk$ physical cap. The sharper displayed inequality has the ordinary construction above. Likewise, the explicit tensor-state display explains our construction; the source's retained-isometry theorem does not assert an equality to that display in the same concrete register representation. Full theorem types and these distinctions are recorded in the correspondence files.

Aaronson–Ambainis also give an interference procedure with $\lceil k/2\rceil$ queries and acceptance probability $(1+\Phi)/2$ [AA18, Proposition 6, pp. 13–14; BansalSinha2021, Proposition 1.2, p. 3]. That is a different test. The projection experiment already appears in [AA18, §3.2, Figure 1 and the paragraph before Proposition 6]; the version used in [OpenAI2026, proof of Lemma 2.1(ii)] and here keeps its probability $\Phi^2$ throughout.
<!-- /passage:forr_coherent -->

<a id="forr_circuit"></a>
<!-- passage:forr_circuit -->
### 3.4. The exact Boolean circuit

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

<a id="forr_boolean_arithmetic"></a>
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

<a id="forr_final_signs"></a>
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

<a id="forr_circuit_size"></a>
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

<a id="forr_small_instance"></a>
<!-- passage:forr_small_instance -->
### 3.5. A complete check of the smallest nontrivial instance

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

The [exact checker](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/checks/) independently compares direct path summation, dense Walsh multiplication, butterfly multiplication, both integer tests, and an append-only Boolean-gate reconstruction on every input at $k=2,t=1$. It also checks all 4,096 inputs at $k=3,t=1$. All arithmetic is integral or rational. These are finite semantic checks; the ordinary proofs above establish the parameterized conclusions.
<!-- /passage:forr_small_instance -->

<a id="forr_current_evidence"></a>
<!-- passage:forr_current_evidence -->
### Formal support and source scope

The source assessed here is the packet snapshot labeled `1dd469dd0042b937b739da3bc211eeb60bdf7462`. Its timestamped root-build receipt matches all 124 supplied local Lean/configuration files; the relevant integrated helper modules also have source-matched native passes. The supplied audit prints the principal helper theorem types and reports only the permitted Lean axioms. These are inspected records of previous runs. The returned section review did not run Lean or Comparator anew, and no Comparator receipt supplied with that return names these Forrelation helper declarations. This integration’s current root build and exact comparison scope are recorded separately in §2.8.

The reviewed wrappers jointly state the normalization, promise, and integer numerator: `construction_walsh_definitions`, `construction_equation_3`, `construction_equation_4`, and `construction_N_phi`. The two threshold equivalences and the actual all-input output rules are split between `construction_integer_tests` and `construction_forr_output_bits`. The coherent physical conclusion is `construction_lemma_2_1_ii_complete`. The circuit endpoint and bound are `Forrelation.exists_circuit` and `construction_lemma_2_1_iii`. The finite census is recorded in `Forrelation.Sanity`.

Two exact correspondences remain narrower than the surrounding ordinary proof: the supplied implementation has a $2qk$, rather than a formally packaged $qk$, bit-query cap; and the arithmetic contracts establish modular representation with correct final signs, rather than a signed interpretation of every intermediate register. Neither qualification weakens Lemma 2.1(ii)–(iii). The packet also contains `construction_lemma_2_1_complete`, a conjunction including the separately proved randomized lower bound; its presence updates the old evidence sentence in §3.17, without supplying a new proof of that lower bound in this section. Exact types, premises, routes, and receipt references are in [correspondence.json](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/correspondence.json) and [LEAN_GAPS.md](../research/returns/round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/LEAN_GAPS.md).
<!-- /passage:forr_current_evidence -->

### 3.6. The statement and the proof

<a id="forr_target"></a>
<!-- passage:forr_target -->
Let $k\ge2$ and $t\ge0$ be integers, let $m=4^t$, and index each of the $k$ input blocks by binary strings of length $2t$. A bit $x$ represents the sign $(-1)^x$. Write

<!-- claim:eq-3 -->
\[
\begin{aligned}
H_{a,b}&=m^{-1/2}(-1)^{a\cdot b},
&u&=m^{-1/2}(1,\ldots,1)^{\mathsf T},\\
\Phi(z)&=u^{\mathsf T}D_{z_0}H D_{z_1}H\cdots H D_{z_{k-1}}u,
&\delta&=2^{-5k}=32^{-k}.
\end{aligned}
\tag{F1}
\]

The inner product $a\cdot b$ is taken over the two-element field, and $D_z$ is the diagonal matrix with diagonal $z$. Distinct Walsh rows are orthogonal: in their inner product, flipping a coordinate where their labels differ pairs opposite signs. Consequently $H^{\mathsf T}=H$ and $H^2=I$. Every sign diagonal is orthogonal and $\|u\|_2=1$, so $|\Phi(z)|\le1$.

The partial Boolean function is

<!-- claim:eq-4 -->
\[
P_{k,m}(z)=
\begin{cases}
1,&\Phi(z)\ge\delta,\\
0,&|\Phi(z)|\le\delta/2,\\
\text{undefined},&\text{otherwise}.
\end{cases}
\tag{F2}
\]

The positive yes condition matters: a large negative value is outside the promise. Let $R(P)$ be the least integer query cap of a randomized bit-query decision tree with error at most $1/3$ on every promised input. The cap holds on every input and every random branch. Such a cap exists because reading all $km$ bits computes the promise function on its domain.

**Theorem.** For every fixed integer $k\ge2$, there is an integer $t_0(k)$ such that, for every $t\ge t_0(k)$,

<!-- claim:lem-2.1.i -->
\[
R(P_{k,4^t})>
L_{k,4^t},\qquad
L_{k,m}=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
\tag{F3}
\]

This is the lower-bound assertion of OpenAI's Lemma 2.1(i), with exactly its normalization and promise [OpenAI2026, §2.1, pp. 3–4]. The proof below supplies the explicit sufficient choice $t_0(k)=13669k^2$. All analytic logarithms below are natural; the logarithm in $L_{k,m}$ is base two.
<!-- /passage:forr_target -->

<a id="forr_bs_translation"></a>
<!-- passage:forr_bs_translation -->
Bansal and Sinha's stated Theorem 1.3 and Corollary 1.4 give, for this same promise and error $1/3$, a lower bound

<!-- claim:claim-bs-to-L -->
\[
R(P_{k,m})\ge c k^{-29}
\left(\frac{m}{\log_2(km)}\right)^{1-1/k}
\tag{F4}
\]

for an absolute $c>0$ in the theorem's asymptotic range. Their block size $N$ is $m$, and the total input length is $km$. For fixed $k$ and $m\ge k$, the ratio of the right side of (F4) to the unfloored expression in (F3) is at least

\[
c k^{-29}2^{-(1-1/k)}(\log_2m)^{1+1/k},
\tag{F5}
\]

which tends to infinity. This explains the preprint's use of the published theorem [BansalSinha2021, arXiv v3, Theorem 1.3 and Corollary 1.4, p. 4]. Section 3.16 identifies a logarithmic mismatch in one displayed step of that version's proof. We therefore keep the literature implication (F4)–(F5) separate from the complete direct proof that follows.
<!-- /passage:forr_bs_translation -->

<a id="forr_proof_spine"></a>
<!-- passage:forr_proof_spine -->
The direct proof constructs two distributions on the whole sign cube. The first is uniform. The second is obtained by rounding a chain of correlated Gaussian vectors to signs. Their Forrelation means differ, but a shallow decision tree has nearly the same expectation under both distributions. To prove this indistinguishability, scale only the first block of Gaussian biases. Differentiation starts in that block; Gaussian integration by parts then moves the derivative through one coordinate of each successive block. Every attempted return to a coordinate already differentiated vanishes by multilinearity. The resulting order-$k$ derivative sum is controlled by a martingale along the decision tree.

Two moment estimates turn this expectation comparison into a promise lower bound. Because neither distribution is entirely supported on the promise, the algorithm is first amplified, and its behavior on unpromised inputs is bounded only by the interval $[0,1]$. The same estimates give a uniform numerical lower bound. Comparing that bound with $L_{k,m}$ proves (F3).
<!-- /passage:forr_proof_spine -->

### 3.7. Multilinear expectation and derivatives

<a id="forr_cube"></a>
<!-- passage:forr_cube -->
Let $I$ be a finite coordinate set and $g:\{-1,1\}^I\to\mathbb R$. Its multilinear extension is

<!-- claim:NEW-FOR-06 -->
\[
F_g(\mu)=\mathcal E_\mu g
=\sum_{z\in\{-1,1\}^I}g(z)
   \prod_{i\in I}\frac{1+\mu_i z_i}{2}.
\tag{F6}
\]

For $|\mu_i|\le1$, these factors define independent signs of means $\mu_i$: their weights are nonnegative and sum to one. Thus $F_g$ is an expectation on that cube, and $|F_g(\mu)|\le\max_z|g(z)|$. For arbitrary real $\mu$, the same finite sum defines a polynomial, affine in each coordinate.

For one coordinate $i$, the discrete difference

\[
\partial_i g(z)=\frac{g(z_{i\leftarrow1})-g(z_{i\leftarrow-1})}{2}
\]

is independent of $z_i$. Separating the two terms with signs $+1$ and $-1$ in (F6) gives

<!-- claim:NEW-FOR-07 -->
\[
\partial_i F_g(\mu)=F_{\partial_i g}(\mu),\qquad
\partial_i^2F_g=0,\qquad
\partial_i\partial_jF_g=\partial_j\partial_iF_g.
\tag{F7}
\]

Here the derivative on the left is an ordinary polynomial derivative; the subscript on the right is the discrete difference just defined. Every iterated discrete derivative remains bounded in absolute value by $\max|g|$. For example, $g(z)=z_i z_j$, with $i\ne j$, has $F_g(\mu)=\mu_i\mu_j$, $\partial_iF_g=\mu_j$, $\partial_i\partial_jF_g=1$, and $\partial_i^2F_g=0$.

When $|\mu_i|<1$, define the centered derivative character

\[
\xi_i(z_i)=\frac{z_i-\mu_i}{1-\mu_i^2}.
\]

The one-coordinate identity

\[
\frac{1+\mu_i z_i}{2}\,\xi_i(z_i)=\frac{z_i}{2}
\]

and finite multiplication over distinct coordinates imply

\[
\partial_JF_g(\mu)
=\mathcal E_\mu\!\left[g(z)\prod_{i\in J}\xi_i(z_i)\right],
\qquad
\mathcal E_\mu\xi_i=0,
\qquad
|\mu_i|\le\tfrac12\ \Longrightarrow\ |\xi_i|\le2.
\tag{F8}
\]

The set $J$ contains no repeated coordinate, and $\partial_J$ means one derivative in each coordinate of $J$. These raw derivatives will let us work directly under a biased product measure, without converting to an orthonormal biased Fourier basis.
<!-- /passage:forr_cube -->

### 3.8. A bounded Gaussian integration identity

<a id="forr_stein"></a>
<!-- passage:forr_stein -->
We need bounded biases and an integration-by-parts identity that removes them one at a time. Put

<!-- claim:NEW-FOR-08 -->
\[
q(x)=\sqrt{2+x^2},\qquad
\Psi(x)=\frac1{2q(x)},\qquad
\varphi(x)=\frac{x(3+x^2)}{2q(x)^3}.
\tag{F9}
\]

Differentiation gives

\[
\varphi'(x)=\frac3{q(x)^5},\qquad
\Psi'(x)=-\frac{x}{2q(x)^3},\qquad
\varphi=x\Psi-\Psi'.
\tag{F10}
\]

The function $\varphi$ is odd and $|\varphi|\le1/2$. For the latter bound, square the nonnegative sides of $|x|(3+x^2)\le q(x)^3$ and use

\[
(2+x^2)^3-x^2(3+x^2)^2=8+3x^2\ge0.
\]

Since both denominators in the next product are minimized at zero,

<!-- claim:r2-sharp-kernel -->
\[
0<\Psi(x)\varphi'(y)
=\frac{3}{2\sqrt{2+x^2}(2+y^2)^{5/2}}
\le\frac3{16}.
\tag{F11}
\]

Equality holds at $x=y=0$. This sharp product estimate will be used only after the integration identity is established. Both $\Psi$ and $\varphi$, and the derivatives of these two functions used below, are bounded.

Let $\gamma(x)=(2\pi)^{-1/2}e^{-x^2/2}$. Equation (F10) gives $(\Psi\gamma)'=-\varphi\gamma$. If $G$ is continuously differentiable and both $G$ and $G'$ are bounded, integration of $(\Psi G\gamma)'$ over $[-A,A]$, followed by $A\to\infty$, yields

<!-- claim:NEW-FOR-09 -->
\[
\mathbb E[\varphi(Z)G(Z)]
=\mathbb E[\Psi(Z)G'(Z)],\qquad Z\sim N(0,1).
\tag{F12}
\]

Indeed, the boundary term tends to zero, and the two remaining integrands are bounded multiples of the Gaussian density. Holding other independent Gaussian coordinates fixed gives the coordinatewise version; the uniform bounds used below ensure absolute integrability when those coordinates are subsequently averaged.

We also use two elementary facts about a standard Gaussian vector $U\in\mathbb R^m$. If $e$ is a unit vector, then $R_eU=U-2\langle e,U\rangle e$ has the same law as $U$: the transformation is orthogonal, preserves $\|U\|_2^2$, and has Jacobian of absolute determinant one. Further,

<!-- claim:NEW-FOR-10 -->
\[
\mathbb E\langle e,U\rangle^2=\sum_i e_i^2=1,
\tag{F13}
\]

because independent centered standard coordinates have covariance $I$. These are statements about the underlying product Gaussian measure. The pair $(U,HU)$ is correlated and is never assigned an independent product law.

Gaussian integration by parts and bounded truncation have antecedents in Bansal–Sinha [BansalSinha2021, §4, especially Lemma 4.3]. Their truncation is the Gaussian distribution function minus $1/2$. Formula (F9) makes a different choice, so its resulting distribution and moment bounds are proved here.
<!-- /passage:forr_stein -->

### 3.9. The rounded Gaussian chain and its zero endpoint

<a id="forr_distribution"></a>
<!-- passage:forr_distribution -->
Write $\ell=k-1$. Draw independent standard Gaussian vectors $U_0,\ldots,U_{\ell-1}\in\mathbb R^m$, and set

\[
V_j=HU_j,\qquad X_j(a)=\varphi(U_j(a)),\qquad Y_j(a)=\varphi(V_j(a)).
\]

For $0\le s\le1$, give each coordinate of the $k$-block sign cube the bias

<!-- claim:NEW-FOR-11 -->
\[
w_s(r,a)=
\begin{cases}
sX_0(a),&r=0,\\
Y_{r-1}(a)X_r(a),&1\le r<\ell,\\
Y_{\ell-1}(a),&r=\ell.
\end{cases}
\tag{F14}
\]

Conditional on all the Gaussian vectors, draw signs independently with these means. Their unconditional distribution is denoted by $\nu_s$, so

\[
\mathbb E_{\nu_s}g=h_g(s):=\mathbb E_U F_g(w_s(U)).
\tag{F15}
\]

The endpoint coordinates have bias of magnitude at most $1/2$; the middle coordinates have magnitude at most $1/4$. The product weights in (F6) therefore show that $\nu_s$ is a probability distribution on the entire finite cube. The hard distribution is $\nu_1$.

We now prove that $\nu_0$ is uniform. At $s=0$, block zero already has zero bias. Suppose that every earlier block and some coordinates of the current block $r\ge1$ have been set to zero inside the extension. For a remaining coordinate $a$ in block $r$, reflect $U_{r-1}$ across the unit row $H_{a,*}$. This negates $V_{r-1}(a)$ and leaves every other coordinate of $V_{r-1}$ unchanged by row orthogonality. It can change the coordinates of $X_{r-1}$, but they appear only in the preceding block, which has already been cleared. All other Gaussian layers are unchanged.

Oddness of $\varphi$ therefore negates only the selected uncleared bias. Gaussian invariance leaves the average unchanged, while affinity of $F_g$ in that bias says that the average of its values at opposite biases is its value at zero. We may thus clear this coordinate without changing the expectation. Clearing finitely many coordinates and then finitely many blocks proves

<!-- claim:NEW-FOR-12 -->
\[
h_g(0)=F_g(0)=\mathbb E_{\mathcal U}g,
\tag{F16}
\]

where $\mathcal U$ is the uniform distribution on the sign cube. The argument applies to every $g$, so it identifies the whole distribution, not only its first moments.
<!-- /passage:forr_distribution -->

### 3.10. Moving the derivative through the blocks

<a id="forr_identity"></a>
<!-- passage:forr_identity -->
For fixed Gaussian vectors, $F_g(w_s(U))$ is a polynomial in $s$ of degree at most $m$. Its finitely many coefficients are bounded functions of $U$, because all factors $X_j,Y_j$ are bounded. Taking expectations coefficient by coefficient shows that $h_g$ is itself a polynomial. In particular, differentiation commutes with the Gaussian average by finite linearity, and the ordinary chain rule gives

<!-- claim:r3-forr-polynomial-interpolation -->
\[
h_g'(s)=\sum_a\mathbb E_U
\left[X_0(a)\,\partial_{(0,a)}F_g(w_s(U))\right].
\tag{F17}
\]

Apply (F12) in $U_0(a)$. The derivative can enter bias $(0,a)$, where it creates a repeated derivative and vanishes, or a coordinate of the next block. If $k\ge3$, the latter produces a matrix entry and the factor $\varphi'(V_0(b))X_1(b)$; the next Stein identity removes $X_1(b)$. If $k=2$, the next block is already the last one and there is no $X_1$ factor. The following three-block calculation makes both cancellations explicit.
<!-- /passage:forr_identity -->

<a id="forr_three_blocks"></a>
<!-- passage:forr_three_blocks -->
For $k=3$, write $U,U'$ for the two independent Gaussian layers, $V=HU$, $V'=HU'$, and $F=F_g$. The three biases are

\[
w_s=(s\varphi(U),\ \varphi(V)\varphi(U'),\ \varphi(V')).
\]

Write $F_{0a,1b}$ for the indicated mixed derivative. The first full coordinate derivative is

<!-- claim:r2-sharp-worked-chain -->
\[
\frac{\partial}{\partial U_a}F_{0a}(w_s)
=s\varphi'(U_a)\underbrace{F_{0a,0a}(w_s)}_{0}
 +\sum_bH_{b,a}\varphi'(V_b)\varphi(U'_b)F_{0a,1b}(w_s).
\tag{F18}
\]

Hence (F17) becomes

\[
h_g'(s)=\sum_{a,b}H_{b,a}\mathbb E
\left[\Psi(U_a)\varphi'(V_b)\varphi(U'_b)F_{0a,1b}(w_s)\right].
\tag{F19}
\]

The accumulated factor $\Psi(U_a)\varphi'(V_b)$ is independent of the entire layer $U'$. For the next application of (F12), the remaining derivative is

\[
\frac{\partial}{\partial U'_b}F_{0a,1b}(w_s)
=\varphi(V_b)\varphi'(U'_b)
     \underbrace{F_{0a,1b,1b}(w_s)}_{0}
 +\sum_cH_{c,b}\varphi'(V'_c)F_{0a,1b,2c}(w_s).
\tag{F20}
\]

Thus

\[
h_g'(s)=\sum_{a,b,c}H_{b,a}H_{c,b}\mathbb E
\left[\Psi(U_a)\varphi'(V_b)\Psi(U'_b)\varphi'(V'_c)
F_{0a,1b,2c}(w_s)\right].
\tag{F21}
\]

The same index $b$ enters and leaves the middle block. The factor $\varphi(U'_b)$ in (F19) is the factor removed by Stein; it is not differentiated as part of the remaining function. This distinction explains why no additional term arises.
<!-- /passage:forr_three_blocks -->

<a id="forr_path_formula"></a>
<!-- passage:forr_path_formula -->
For general $k$, the induction has the following invariant. After entering block $j$, its selected coordinate $(j,p_j)$ has already been differentiated, the unremoved factor is $X_j(p_j)$, and all accumulated weights depend only on $U_0,\ldots,U_{j-1}$. Differentiating in $U_j(p_j)$ therefore leaves those weights fixed. Its contribution through the same-block bias is zero, and its contributions through the next block supply

\[
H_{p_{j+1},p_j}\Psi(U_j(p_j))\varphi'(V_j(p_{j+1})).
\]

At the last block there is no further $X$ factor. For $k=2$ the first Stein step already reaches that block. Define the coordinate set of a path by $S_p=\{(r,p_r):0\le r<k\}$. Induction gives, for every $s\in[0,1]$,

<!-- claim:NEW-FOR-13 -->
\[
h_g'(s)=\sum_{p\in[m]^k}
\left(\prod_{j<\ell}H_{p_{j+1},p_j}\right)
\mathbb E_U\left[
\left(\prod_{j<\ell}\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))\right)
\partial_{S_p}F_g(w_s(U))\right].
\tag{F22}
\]

Each Stein application is to a bounded function with a bounded continuous coordinate derivative: the extension is a finite polynomial on a bounded bias box, and the other relevant factors are bounded smooth functions. The sums are finite, and the underlying Gaussian measure is always the same product measure on the independent $U_j$. There is no differentiation of a Gaussian covariance and no use of a density for the singular pair $(U_j,HU_j)$.

Since $h_g$ is a polynomial, the mean value theorem supplies one common $s_*\in(0,1)$ such that

\[
\mathbb E_{\nu_1}g-\mathbb E_{\mathcal U}g=h_g'(s_*).
\tag{F23}
\]

The parameter may depend on $g$, but it is shared by every path in (F22). This lets us bound the sum of absolute derivatives at one bias before taking the Gaussian average.

Order $k$ at a biased point does not mean degree $k$ under the uniform measure. Expanding (F6) in uniform Fourier characters gives

<!-- claim:r2-sharp-worked-chain -->
\[
\partial_JF_g(\mu)
=\sum_{T\supseteq J}\widehat g(T)
    \prod_{i\in T\setminus J}\mu_i,
\qquad
\widehat g(T)=2^{-|I|}\sum_zg(z)\prod_{i\in T}z_i.
\tag{F24}
\]

Higher uniform degrees remain in this expression. The next estimate is therefore proved uniformly over all biases of magnitude at most $1/2$.
<!-- /passage:forr_path_formula -->

### 3.11. Derivative growth along a decision tree

<a id="forr_tree_growth"></a>
<!-- passage:forr_tree_growth -->
**Lemma.** Let $I$ have $n\ge1$ coordinates. Suppose that a deterministic decision tree with integer depth cap $d\ge1$ computes a real function $g$ with leaf values in $[-1,1]$. For every bias $|\mu_i|\le1/2$, every integer $r\ge1$, and every family $\mathcal J$ of distinct $r$-element subsets of $I$,

<!-- claim:r2-sharp-growth -->
\[
\sum_{J\in\mathcal J}|\partial_JF_g(\mu)|
\le \bigl(16rd\ln(4n)\bigr)^{r/2}+2^{-r}.
\tag{F25}
\]

The proof is a bounded-bias version of the ordinary-tree martingale argument in Girish–Tal–Wu [GirishTalWu2021, arXiv v2, §1.3 and Lemma 1.9, p. 8; conference Lemma 9]. We give it explicitly because the measure, raw derivative normalization and numerical constants are needed here.

Fix $\mu$, and take independent signs with these means. Their characters $\xi_i$ from (F8) are independent, centered and bounded by $2$. Let $Q_j$ be the set of coordinates revealed after $j$ queries. A repeated query leaves this set unchanged. After reaching a leaf, hold the set fixed, so the process has the deterministic horizon $d$.

For each degree $r$ and coefficient array $|c(J)|\le1$, put

<!-- claim:NEW-FOR-14 -->
\[
Y_r^c(Q,z)=
\sum_{\substack{J\subseteq Q\\|J|=r}}c(J)\prod_{i\in J}\xi_i(z_i).
\tag{F26}
\]

For a fresh coordinate $q\notin Q$, splitting the subsets according to whether they contain $q$ gives

\[
Y_r^c(Q\cup\{q\},z)-Y_r^c(Q,z)
=\xi_q(z_q)Y_{r-1}^{c^q}(Q,z),
\tag{F27}
\]

where $c^q(J)=c(J\cup\{q\})$ when $q\notin J$, and $c^q(J)=0$ when $q\in J$. The contracted array remains bounded by one.
<!-- /passage:forr_tree_growth -->

<a id="forr_tree_leaves"></a>
<!-- passage:forr_tree_leaves -->
Adaptivity does not change the conditional distribution of a fresh coordinate. A reachable root-to-node path specifies exactly the values of its distinct queried coordinates. Conversely, every input with those values follows that path, by induction through the tree. The path event is therefore a cylinder under the original product measure. All unqueried coordinates retain their independent laws on that event. In particular, (F27) is a centered increment conditional on the query history.

The same observation gives the identity used at leaves. A monomial involving an unqueried centered coordinate has conditional expectation zero. A monomial supported on the leaf's queried set is already determined. Since $g$ is constant at a leaf,

<!-- claim:NEW-FOR-27 -->
\[
\mathcal E_\mu[g(z)Y_r^c(I,z)]
=\mathbb E_\mu[g(z)Y_r^c(Q_d,z)].
\tag{F28}
\]

Equivalently, the right side is the sum over reachable leaves of their cylinder probabilities times their output and terminal chaos. Each leaf probability is the product of the answer probabilities at its distinct queried coordinates; a repeated query contributes no additional factor. A zero-probability leaf contributes zero, so this finite-sum proof does not condition on a null event.
<!-- /passage:forr_tree_leaves -->

<a id="forr_tree_stopping"></a>
<!-- passage:forr_tree_stopping -->
We prove a maximal estimate for (F26). If a centered random variable $W$ lies in $[-B,B]$, convexity of the exponential gives

<!-- claim:NEW-FOR-15 -->
\[
\mathbb E e^{\lambda W}
\le \cosh(\lambda B)
\le e^{\lambda^2B^2/2}.
\tag{F29}
\]

The first inequality follows by averaging the secant line through the endpoint values of the exponential. The second follows term by term from $(2j)!\ge2^j j!$. The same argument holds conditionally when the centeredness and bound hold for the conditional law.

Let $B>0$, $R>0$, and let $d\ge1$ be an integer. For a martingale $Z_j$ starting at zero whose increments have absolute value at most $B$, (F29) makes

\[
M_j=\exp\!\left(\lambda Z_j-\frac{\lambda^2B^2j}{2}\right)
\]

a nonnegative supermartingale. Stop additionally at the first time $Z_j>R$, capped at $d$. Iterated conditional expectation over these at most $d$ steps gives expectation at most one for the stopped $M$. On the crossing event its value is at least $\exp(\lambda R-\lambda^2B^2d/2)$. Taking $\lambda=R/(B^2d)$ and applying the same argument to $-Z$ yields

<!-- claim:NEW-FOR-16 -->
\[
\Pr\!\left(\max_{j\le d}|Z_j|>R\right)
\le2\exp\!\left(-\frac{R^2}{2B^2d}\right).
\tag{F30}
\]

Only finite-horizon conditional expectation has been used.

Fix $\Lambda>0$ and put $K=\sqrt{8d\Lambda}>0$. We claim, for every bounded coefficient array and every $r\ge0$, that

<!-- claim:NEW-FOR-17 -->
\[
\Pr\!\left(\max_{j\le d}|Y_r^c(Q_j,z)|>K^r\right)
\le(4n)^r e^{-\Lambda}.
\tag{F31}
\]

For $r=0$, the expression is the constant $c(\varnothing)$, of magnitude at most one, so the event is empty. Suppose the claim holds at degree $r-1$. Stop the degree-$r$ process before any step at which one of the $n$ contracted degree-$(r-1)$ expressions has absolute value greater than $K^{r-1}$. By induction and a union bound, the probability of such a failure is at most

\[
n(4n)^{r-1}e^{-\Lambda}.
\]

Before it is stopped, (F27) has a centered increment of magnitude at most $B=2K^{r-1}$; after stopping its increment is zero. Apply (F30) with $R=K^r$. Its exponent is

\[
\frac{R^2}{2B^2d}=\frac{K^2}{8d}=\Lambda.
\]

Until a coefficient failure the original and stopped processes agree. The probability of a crossing for the original process is consequently at most

\[
\bigl(2+n(4n)^{r-1}\bigr)e^{-\Lambda}
\le(4n)^r e^{-\Lambda},
\]

which proves (F31). Stopping is essential here. Conditioning on the future event that every coefficient bound holds would not preserve the martingale property; Girish–Tal–Wu explicitly make this distinction in their footnote 2.
<!-- /passage:forr_tree_stopping -->

<a id="forr_tree_derivative"></a>
<!-- passage:forr_tree_derivative -->
At any leaf, the crude bound $|Y_r^c|\le(2n)^r$ follows by bounding the number of subsets by $n^r$ and each product by $2^r$. Outside the crossing event in (F31), the better bound is $K^r$. Hence (F28) and $|g|\le1$ give

\[
\left|\mathcal E_\mu[gY_r^c(I,\cdot)]\right|
\le K^r+(2n)^r(4n)^r e^{-\Lambda}.
\tag{F32}
\]

Choose $c(J)$ to be the sign of $\partial_JF_g(\mu)$ for $J\in\mathcal J$, and zero for the remaining $r$-sets. Equation (F8) makes the expression on the left of (F32) the desired sum of absolute derivatives. Finally, choose

\[
\Lambda=2r\ln(4n),\qquad K^2=16rd\ln(4n).
\]

The residual term becomes

\[
\frac{(2n)^r(4n)^r}{(4n)^{2r}}=2^{-r},
\]

proving (F25). <!-- claim:NEW-FOR-18 -->
Since $2^{-r}\le1$, the proof also gives the original bound $\sum_{J\in\mathcal J}|\partial_JF_g(\mu)|\le(16rd\ln(4n))^{r/2}+1$. All constants are uniform in the bias, the tree and the selected subset family.
<!-- /passage:forr_tree_derivative -->

### 3.12. Indistinguishability of shallow trees

<a id="forr_advantage"></a>
<!-- passage:forr_advantage -->
A path in (F22) chooses one coordinate from each labeled block. Its set $S_p$ has size $k$, and two paths produce the same set only if they agree in every block. Thus the path family is eligible for (F25), without a factor of $k!$.

For the Walsh matrix, every product of $k-1$ absolute matrix entries is $m^{-(k-1)/2}$. The product of the remaining edge factors is at most $(3/16)^{k-1}$ by (F11). Take the triangle inequality in (F22), put the finite path sum inside the Gaussian expectation, and apply (F25) pointwise at the common bias $w_{s_*}(U)$. We obtain

<!-- claim:r2-sharp-advantage -->
\[
\left|\mathbb E_{\nu_1}g-\mathbb E_{\mathcal U}g\right|
\le
\left(\frac{3}{16\sqrt m}\right)^{k-1}
\left[\bigl(16kd\ln(4km)\bigr)^{k/2}+2^{-k}\right].
\tag{F33}
\]

This holds for every real-valued tree of depth at most $d\ge1$ and leaf values in $[-1,1]$. It also holds for a convex mixture of such trees, by linearity of expectation and the triangle inequality. A randomized acceptance probability is such a mixture: on a finite coordinate set with a fixed depth cap, there are only finitely many possible deterministic bit-query trees, so arbitrary random coins can be collected into their probabilities.

For comparison with the previous draft, (F33) immediately implies its coarser estimate

<!-- claim:NEW-FOR-19 -->
\[
\left|\mathbb E_{\nu_1}g-\mathbb E_{\mathcal U}g\right|
\le
\left(\frac{3}{\sqrt m}\right)^{k-1}
\left[\bigl(16kd\ln(4km)\bigr)^{k/2}+1\right].
\tag{F34}
\]

The stronger scalar product is now available in the supplied source, so we retain it for the numerical assembly.
<!-- /passage:forr_advantage -->

### 3.13. The moments that place mass in the promise

<a id="forr_moments"></a>
<!-- passage:forr_moments -->
Expand the Walsh product into paths:

\[
\Phi(z)=\frac1m\sum_{p\in[m]^k}
\left(\prod_{j<k}z_j(p_j)\right)
\left(\prod_{j<k-1}H_{p_{j+1},p_j}\right).
\tag{F35}
\]

The orientation agrees with (F1) because $H$ is symmetric. Under uniform independent signs, each path monomial has mean zero. Two different paths disagree in at least one block, and the product of their monomials then contains a coordinate appearing once, so their mixed expectation is zero. Each path multiplied by itself contributes one. There are $m^k$ paths, each with squared coefficient $m^{-(k+1)}$, giving

<!-- claim:NEW-FOR-20 -->
\[
\mathbb E_{\mathcal U}\Phi=0,\qquad
\mathbb E_{\mathcal U}\Phi^2=\frac1m.
\tag{F36}
\]

For the hard mean, the elementary inequality $e^v\ge1+v$, with $v=(x^2-1)/3$, implies

<!-- claim:NEW-FOR-21 -->
\[
q(x)\le\sqrt3\,e^{(x^2-1)/6},\qquad
\Psi(x)\varphi'(y)\ge
\frac1{18}\exp\!\left[-\frac{x^2-1}{6}-\frac{5(y^2-1)}6\right].
\tag{F37}
\]

For a fixed path $p$, let

\[
T_p=\sum_{j<k-1}
\left(\frac{U_j(p_j)^2-1}{6}
      +\frac{5(V_j(p_{j+1})^2-1)}6\right).
\]

Every selected $U$ coordinate has second moment one; so does every selected $V$ coordinate, by (F13) for the corresponding unit Walsh row. Therefore $\mathbb E T_p=0$. Moreover, $T_p\ge-(k-1)$, so $e^{-T_p}$ is bounded, and $T_p$ is integrable. Multiplying (F37) along the path and using $e^{-T_p}\ge1-T_p$ gives

\[
\mathbb E_U\prod_{j<k-1}
\Psi(U_j(p_j))\varphi'(V_j(p_{j+1}))
\ge18^{-(k-1)}.
\tag{F38}
\]

This calculation needs the marginal second moments; it does not assume independence between a selected $U$ coordinate and its correlated $V$ coordinate.

Apply (F22)–(F23) with $g=\Phi$. Since $\Phi$ has one variable in each block, its path derivative is the constant

\[
\partial_{S_p}F_\Phi
=\frac1m\prod_{j<k-1}H_{p_{j+1},p_j}.
\]

Multiplying by the path coefficient already in (F22) yields the nonnegative number

\[
\frac1m\prod_{j<k-1}H_{p_{j+1},p_j}^{\,2}=m^{-k}.
\]

There are $m^k$ paths, and (F38) applies to each one. The uniform mean is zero, so

<!-- claim:NEW-FOR-22 -->
\[
\mathbb E_{\nu_1}\Phi\ge a_k:=18^{-(k-1)}
\ge32^{-(k-1)}=32\delta.
\tag{F39}
\]

For example, $\Phi\le\delta+\mathbf1_{\{\Phi\ge\delta\}}$ gives
$\nu_1(\Phi\ge\delta)\ge a_k-\delta\ge31\delta$. Markov's inequality applied to (F36) gives
$\mathcal U(|\Phi|>\delta/2)\le4/(m\delta^2)$.
These estimates concern the same two distributions throughout the proof. We will use pointwise acceptance inequalities below so that all inputs outside the promise are handled explicitly.
<!-- /passage:forr_moments -->

### 3.14. Error reduction and inputs outside the promise

<a id="forr_amplification"></a>
<!-- passage:forr_amplification -->
Suppose a randomized algorithm of query cap $D$ has error at most $1/3$ on the promise. Run it independently $2\tau$ times and take a majority, with any fixed rule for ties. On a promised input a wrong majority requires at least $\tau$ erroneous runs. If $E_i$ indicates an erroneous run, then $\mathbb E2^{E_i}\le4/3$. Independence and Markov's inequality give

<!-- claim:NEW-FOR-23 -->
\[
\Pr(\text{wrong majority})
\le2^{-\tau}(4/3)^{2\tau}=(8/9)^\tau.
\tag{F40}
\]

The amplified cap is $2\tau D$ on every input and every random branch. We may use the larger integer $d=2\tau D+1$ in (F33); this ensures $d\ge1$ even if $D=0$.
<!-- /passage:forr_amplification -->

<a id="forr_promise_gap"></a>
<!-- passage:forr_promise_gap -->
Let $A(z)\in[0,1]$ be any acceptance probability with promise error at most $\varepsilon\in[0,1]$. At every input,

<!-- claim:NEW-FOR-24 -->
\[
(1-\varepsilon)(\Phi(z)-\delta)
\le A(z)
\le\varepsilon+\frac{4\Phi(z)^2}{\delta^2}.
\tag{F41}
\]

For the lower inequality, correctness gives $A\ge1-\varepsilon$ when $\Phi\ge\delta$, and $\Phi-\delta\le1$ there. If $\Phi<\delta$, the left side is nonpositive. For the upper inequality, correctness gives $A\le\varepsilon$ when $|\Phi|\le\delta/2$; otherwise $4\Phi^2/\delta^2>1\ge A$. Thus no correctness assertion is made on an unpromised input.

Taking expectations and using (F36) and (F39), we obtain

\[
\mathbb E_{\nu_1}A-\mathbb E_{\mathcal U}A
\ge (1-\varepsilon)(a_k-\delta)
       -\varepsilon-\frac4{m\delta^2}.
\tag{F42}
\]

The hard distribution may place much of its mass outside the yes promise. Its positive-promise mass is only bounded below by a quantity exponentially small in $k$. Error $1/3$ would therefore be too large for this comparison; (F40) provides the required reduction. The finite contradiction is obtained whenever the right side of (F42) exceeds the right side of (F33) at the amplified depth.
<!-- /passage:forr_promise_gap -->

### 3.15. A uniform estimate and the fixed-parameter threshold

<a id="forr_uniform_assembly"></a>
<!-- passage:forr_uniform_assembly -->
The estimates already proved give a useful quantitative statement.

**Proposition.** For integers $k\ge2$ and $t\ge0$ with $15k+2\le2t$, and $m=4^t$,

<!-- claim:r2-sharp-original-constant -->
\[
R(P_{k,m})>
\frac2{18225}\,
\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{F43}
\]

The dimension condition is equivalently $m\ge2^{15k+2}$. In particular all denominators are positive.

*Proof.* Suppose an algorithm has cap $D$ at most the displayed quantity. Set $\tau=25k$ and $\varepsilon=(8/9)^{25k}$. The exact integer inequality
$18\cdot8^{25}<9^{25}$ implies

\[
\varepsilon\le18^{-k}=\frac{a_k}{18},
\qquad \delta\le\frac{a_k}{32},
\qquad \frac4{m\delta^2}\le\delta.
\tag{F44}
\]

The last inequality is precisely where the stated dimension condition is used. Since $a_k-\delta\le1$, (F42) gives a gap at least

\[
a_k-2\delta-2\varepsilon
\ge\left(1-\frac1{16}-\frac19\right)a_k
=\frac{119}{144}a_k.
\tag{F45}
\]

If $D=0$, the acceptance probability is constant on the entire cube, so its two expectations agree, contradicting (F45). Hence $D\ge1$.

Use padded depth $d=50kD+1$ in (F33), matching the finite formal interface. The assumption on $D$ and the equality $800(2/18225)=(8/27)^2$ imply

\[
16kd\ln(4km)
\le\left(\frac8{27}\right)^2
       \left(1+\frac1{50k}\right)m^{1-1/k}.
\tag{F46}
\]

The binomial theorem gives

\[
\left(1+\frac1{50k}\right)^k
\le\sum_{j=0}^k50^{-j}
\le\frac{50}{49}
<\left(\frac98\right)^2.
\tag{F47}
\]

Indeed, $\binom kj\le k^j$ bounds each term. With $b=3/16$, the main term in (F33) is therefore at most

\[
\begin{aligned}
\left(\frac b{\sqrt m}\right)^{k-1}
      \bigl(16kd\ln(4km)\bigr)^{k/2}
&\le b^{k-1}\left(\frac8{27}\right)^k
       \left(1+\frac1{50k}\right)^{k/2}\\
&\le\frac8{27}\,a_k\frac98=\frac{a_k}{3},
\end{aligned}
\tag{F48}
\]

where $b(8/27)=1/18$ and $k(1-1/k)=k-1$ cancel all powers of $m$. The dimension condition implies $\sqrt m\ge54$, and $b\le3$, so the residual satisfies

\[
2^{-k}\left(\frac b{\sqrt m}\right)^{k-1}
\le\frac{a_k}{4}.
\tag{F49}
\]

Consequently the advantage is at most $7a_k/12$, strictly below $119a_k/144$. This contradicts (F45). Applying the contradiction at the least successful integer cap proves (F43). $\square$
<!-- /passage:forr_uniform_assembly -->

<a id="forr_threshold"></a>
<!-- passage:forr_threshold -->
We now derive (F3) with an explicit threshold. If $1\le k\le t$ and $m=4^t$, then

\[
\ln(4km)=\ln(4k)+2t\ln2
\le(4k-1)+2t\le6t.
\tag{F50}
\]

Here $\ln x\le x-1$ for $x>0$ and $\ln2\le1$ suffice. For $k\ge2$ and $t\ge13669k^2$, we have $k\le t$, $t>0$, and $15k+2\le2t$. The proposition therefore applies, and

<!-- claim:r3-forr-explicit-fixed-threshold -->
\[
\begin{aligned}
R(P_{k,4^t})
&>\frac2{18225}\,
   \frac{m^{1-1/k}}{k^2\ln(4km)}\\
&\ge\frac{m^{1-1/k}}{54675k^2t}\\
&>\frac{m^{1-1/k}}{4t^2}
 \ge\left\lfloor\frac{m^{1-1/k}}{(2t)^2}\right\rfloor.
\end{aligned}
\tag{F51}
\]

The strict comparison follows from
$4t\ge54676k^2>54675k^2$.
Since $\log_2(4^t)=2t$, the final floor is exactly $L_{k,4^t}$. This proves the theorem for every $t\ge13669k^2$, with the order of quantifiers required by §3.17. No subsequence or growing-$k$ total-function conclusion is needed.

The smaller threshold $\lceil54675k^2/4\rceil$ also follows from (F43) and (F50), because the first inequality is already strict. The simpler integer multiple above is sufficient. Both are ordinary specializations of the quantitative theorem, not optimality claims about the first dimension where the lower bound holds.

The lower bound also ensures that both promise values occur in these dimensions. If one of them were absent, a constant zero-query algorithm would compute the partial function on its domain, contradicting (F43). The previous four-term, much larger sufficient threshold is still valid; its derivation is retained in [the historical-threshold derivation in Appendix D](#forr_historical_threshold) so that replacing the exposition does not erase that argument.
<!-- /passage:forr_threshold -->

### 3.16. Literature comparison and the scope of the conclusion

<a id="forr_attribution"></a>
<a id="forr_credit"></a>
<!-- passage:forr_credit -->
The proof above uses a known Gaussian-chain architecture and a known decision-tree growth strategy. Bansal and Sinha's Theorem 1.3 is the original quantitative lower-bound theorem for the promise in (F2); their §3 supplies the Gaussian-pair and conditional-rounding antecedent, and their Lemma 4.3 supplies the transformed integration-by-parts antecedent. Their truncation is the Gaussian distribution function minus $1/2$. The algebraic function (F9) used here defines a different hard distribution. Accordingly, (F16), (F22), and (F39) were proved for this distribution, rather than imported from their promise-mass theorem.

The adaptive-path martingale in §3.11 follows the ordinary-tree discussion of Girish, Tal, and **Kewen Wu**, arXiv:2103.11604v2, §1.3 and Lemma 1.9, pp. 6–8; the conference version numbers the corresponding result Lemma 9. That source motivates the contracted coefficient arrays and induction on degree. The centered variables, bounded-bias constants, repeated-query treatment, and stopped-process estimate used here were stated and proved explicitly. This attribution does not claim that the cited lemma already has the exact raw-derivative statement (F25).

The one-block interpolation isolates one raw derivative in each labelled block. As (F24) makes explicit, this does not discard the higher uniform Fourier levels of the test function. The bounded searches and source comparisons in the retained reviews establish neither priority nor novelty for this arrangement.
<!-- /passage:forr_credit -->

#### The displayed comparison in Bansal–Sinha §5.4

<a id="forr_bs_mismatch"></a>
<!-- passage:forr_bs_mismatch -->
Fix the version before making the comparison. In arXiv:2008.07003v3, printed p. 38, the supplied source archive has SHA-256
f48a3225662484d12e19bf03412478cf87a388f7c2e33c69a4d7f2078202e015.
Its physical main.tex lines 1180 and 1181 contain the two successive bounds; line 1184 states the subsequent depth threshold.

Write $\alpha=1-1/k$, $L=\log(kN)$, and $h=k(k-1)$. Up to an absolute constant $A>0$, the preceding level-$r$ term is

\[
T_r=(Ak^{28}d_1)^{r/2}N^{-\alpha r/2}L^{(r-1)/2},
\qquad k\le r\le h.
\tag{F52}
\]

The following display replaces the exponent $(r-1)/2$ of $L$ by $\alpha r/2$. The lost factor is

\[
L^{(r-1)/2-\alpha r/2}
=L^{(r/k-1)/2}.
\tag{F53}
\]

At $r=k$ it is one. For fixed $k\ge3$ and $r=h$, it is $L^{(k-2)/2}$, which is unbounded as $N$ grows. More concretely, choose integer $d_1$ asymptotic to $c k^{-28}N^\alpha/L^\alpha$, with any fixed $c>0$. The last term of the preceding bound then grows as a positive constant times $L^{(k-2)/2}$, while the proposed following finite sum stays bounded. Thus a change of absolute constants cannot justify this comparison. This calculation compares two displayed upper-bound expressions; it neither constructs an algorithm nor disproves Bansal and Sinha's theorem.

The displayed multilevel estimates themselves do yield the sufficient replacement

\[
d_1\le c k^{-28}
\frac{N^{1-1/k}}{L^{\,1-1/[k(k-1)]}}.
\tag{F54}
\]

Indeed, the logarithmic exponent after substitution into (F52) is
$(r/h-1)/2\le0$. For $L\ge1$ the sum is at most
$\sum_{r=k}^{h}(Ac)^{r/2}$. Taking $Ac\le128^{-2}$ bounds it by
$128^{1-k}/127<32^{-k}/4$. This proves a corrected sufficient comparison from those estimates. Its logarithmic exponent is less than two, so, for each fixed $k$, even this weaker estimate eventually dominates the target in (F3), after the stated order-$k$ amplification cost. The direct proof above provides a separate route with explicit constants.

There is also a separate reciprocal error in the displayed equation (5.31), physical main.tex line 1173. It subtracts $\delta^2/(4N)$; Theorem 3.1 gives the exceptional uniform probability $4/(N\delta^2)$. Using acceptance in $[0,1]$ on all inputs, a safe lower gap is

\[
6\delta-2\delta-\frac4{N\delta^2},
\tag{F55}
\]

which is at least $3\delta$ when $N\ge4/\delta^3$. The need to retain the exceptional mass is the same reason for keeping the last term of (F42). The statement here concerns the identified v3 displays; it is not an assertion about an author-approved correction or an exhaustive search of later versions.
<!-- /passage:forr_bs_mismatch -->

#### The sharper external Fourier comparison

<a id="forr_ssw_comparison"></a>
<!-- passage:forr_ssw_comparison -->
Sherstov, Storozhenko, and **Pei Wu** prove a stronger Fourier-growth theorem. The version read here is arXiv:2008.10223v4: PDF Corollaries 4.14 and 4.15, printed pp. 35–36; the corresponding HTML conversion calls them Corollaries 4.12 and 4.13. There is an absolute $C\ge1$ such that every depth-$d$ tree $g$ on $n\ge1$ coordinates, with leaves in $[-1,1]$, satisfies, for $1\le r\le n$,

\[
\sum_{|S|=r}|\widehat g(S)|
\le C^r\sqrt{\binom dr}\,(1+\ln n)^{(r-1)/2}.
\tag{F56}
\]

The cited corollary does not give a certified numerical value of $C$. This is an **external theorem used only for the following comparison**; the proof of (F43) does not assume it.

Here is the transfer, to specify exactly what is being compared. Independently leave coordinate $i$ free with probability $p_i$, and fix it to signs with probabilities $(1-p_i+\mu_i)/2$ and $(1-p_i-\mu_i)/2$. These are valid if $0\le p_i\le1$ and $|\mu_i|\le1-p_i$. Define $\widehat {g_\rho}(S)=0$ unless every coordinate of $S$ is free; otherwise it is the usual Fourier coefficient on the free cube. A monomial expansion gives

\[
\mathbb E_\rho\widehat {g_\rho}(S)
=\left(\prod_{i\in S}p_i\right)\partial_S F_g(\mu).
\tag{F57}
\]

At the path biases, take $p_i=1/2$ on the first and last blocks and $p_i=3/4$ on the interior blocks. Every path has free-probability product $\frac14(3/4)^{k-2}$. The path sets are distinct, so the triangle inequality, (F56)–(F57), (F11), and (F22)–(F23) give

\[
\left|\mathbb E_{\nu_1}g-\mathbb E_{\nu_0}g\right|
\le\frac{3C^k}{4^{k-1}}\sqrt{\binom dk}
\left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
\tag{F58}
\]

This uses $(3/16)^{k-1}\,4(4/3)^{k-2}=3/4^{k-1}$. Restrictions do not increase depth; a restriction with no free coordinates contributes zero at positive degree. Thus there is no hidden division by the number of surviving variables.

For comparison with a variable-error statement, let $R_\varepsilon$ denote the same worst-case query model at error $\varepsilon$. If a depth-$D$ algorithm has error $(1-\eta)/2$, where $0<\eta\le1$, majority of $2\tau$ independent runs has error at most $(1-\eta^2)^\tau\le e^{-\tau\eta^2}$. For $0<\eta<1$ the first inequality follows by applying Markov's inequality to the exponential of the error count with multiplier $(1+\eta)/(1-\eta)$; at $\eta=1$ every run is correct.

Assume $m$ is a power of two with $m\ge2^{15k+2}$, and take
$\tau=\lceil5k\ln2/\eta^2\rceil<4k/\eta^2$.
The amplified error and the uniform exceptional mass are both at most $\delta$. The proof of (F42) therefore gives a gap $\Gamma\ge a_k-4\delta\ge7a_k/8$. If $2\tau D<k$, (F58) is zero, a contradiction. Otherwise use
$\binom{2\tau D}{k}\le(2e\tau D/k)^k$ and solve (F58):

\[
\begin{aligned}
D&\ge\frac{k}{2e\tau C^2}
 \left(\frac{\Gamma4^{k-1}}3\right)^{2/k}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k},\\
\left(\frac{\Gamma4^{k-1}}3\right)^{2/k}
&\ge\frac4{81}\left(\frac{21}{16}\right)^{2/k}
\ge\frac4{81}.
\end{aligned}
\tag{F59}
\]

Consequently the comparison route proves, assuming (F56),

\[
R_{(1-\eta)/2}(P_{k,m})
\ge\frac{\eta^2}{162eC^2}
\left(\frac m{1+\ln(km)}\right)^{1-1/k}.
\tag{F60}
\]

The extension from powers of four to powers of two in this ordinary calculation uses only the existence of the normalized Walsh matrix; it is not an extension of the frozen Lean definition. After taking the $2/k$ power, the binomial estimate supplies a factor of $k$ that cancels the order-$k/\eta^2$ amplification cost. The elementary derivative bound also carries its own factor of $k$, explaining its larger loss. Tal's earlier Fourier-growth work provides historical context, but its random-orthogonal distribution and “good matrix” hypothesis are not a theorem for the explicit Walsh promise [Tal2019v1, §§5.1–5.2, Theorem 5.1 and Definition 5.5, pp. 13–14]. Neither that distribution theorem nor SSW's rorrelation distribution theorem is being transferred here. The only external mathematical input to (F60), beyond the proof above, is (F56).
<!-- /passage:forr_ssw_comparison -->

<a id="forr_validation_scope"></a>
<!-- passage:forr_validation_scope -->
Finally, the mathematical statements have distinct formal and evidential scopes. The supplied reviewed source proves the exact fixed-$k$ proposition as QuarticQuery.ForrelationLower.bansalSinhaLower, and the recorded ordinary and paranoid Unconditional Comparator receipts explicitly list it. The sharper restricted endpoint (F43) is also already present as QuarticQuery.forrelation_lower_uniform_sharp: it is explicitly listed in the recorded root-build receipt, has an accepted focused Uniform build, and its elaborated type and standard axiom list are printed in the successful reviewed audit. It is **not** listed in Comparator. Older prose calling this endpoint merely proposed is superseded by those source-matched records.

The new threshold (F51), the finite-polynomial explanation of differentiation, and the comparison deduction (F57)–(F60) are ordinary mathematics in this section. No separately compiled Lean wrapper for those formulations is claimed. The ordinary proof of (F25) allows arbitrary bounded real leaf labels; the local interface uses a Boolean-output tree followed by one fixed map from its two output values into $[-1,1]$, which suffices for acceptance probabilities. In particular, (F60) depends on an external Fourier theorem and allows variable error and every power-of-two dimension; it is not the type of either existing endpoint. The returned section review recomputed the recorded local file hashes without a fresh Lean run. This integration’s later native execution is recorded in §2.8 and does not supply new wrappers for the ordinary formulations just distinguished. Exact declaration types, premises, source bindings, and the limits of each receipt are recorded in the accompanying correspondence and evidence files.
<!-- /passage:forr_validation_scope -->

### 3.17. The complete Forrelation ingredient

<a id="forr_bundle"></a>
<!-- passage:forr_bundle -->
For each fixed integer $k\ge2$, set $m=4^t$, $\delta=2^{-5k}$, and
$L_{k,m}=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$. The same partial function
$P_{k,m}$ defined in §3.1 has the following three properties.

<!-- claim:lem-2.1 -->
1. For every integer $t\ge13669k^2$, $R(P_{k,4^t})>L_{k,4^t}$, by §3.15.
2. For every $t\ge1$ and $0<\eta<1/2$, one coherent quantum preparation has a Boolean output on every input and error at most $\eta$ on every promised input. Its workspace is retained, and its all-input bit-query cap is $O_k(1+\log(1/\eta))$, by §3.3.
3. For every $t\ge1$, one fan-in-at-most-two circuit $C_{k,t}$ of size at most $200(k+1)^2m(\log_2m)^2$ has a domain bit $d$ and value bit $b$ with $d(x)=1$ exactly when $P_{k,m}(x)$ is defined, and $b(x)=P_{k,m}(x)$ on that domain, by §3.4.

This is the conjunction required in OpenAI's Lemma 2.1. Its common threshold can be the largest of the thresholds just stated; its quantum accuracy is quantified after $k,t$ and can be chosen for each later decoder call. The quantum and circuit procedures share the same normalization, bit/sign convention, and one-sided promise. No quantum correctness is asserted off promise. The circuit recognizes membership exactly there as well as on the domain. These are the different guarantees used in §4 and §5.

The recorded source contains `QuarticQuery.Paper.construction_lemma_2_1_complete`, whose conclusion packages all three parts, including the retained-isometry physical implementation of part (ii). It supplies an eventual threshold rather than the explicit ordinary specialization $13669k^2$. Its generic physical compiler charges $2qk$ queries for $q$ repetitions, whereas the explicit phase construction in §3.3 has the ordinary cap $qk$. Both give the stated asymptotic bound; the sharper cap and explicit threshold are not promoted to the exact compiled type. Declaration-specific evidence and the full returned signatures are retained in [the correspondence](reasoning_record_correspondence.json).
<!-- /passage:forr_bundle -->

### 3.18. Sources for the Forrelation argument

<a id="forr_references"></a>
<!-- passage:forr_references -->
Aaronson–Ambainis supplies the alternating Walsh construction and its projection experiment. Bansal–Sinha supplies the exact one-sided promise and the stated quantitative classical theorem. The direct proof in §§3.7–3.15 uses a different algebraic truncation and a first-block interpolation, with the ordinary-tree martingale method of Girish–Tal–Wu as its antecedent. The external Sherstov–Storozhenko–Wu Fourier theorem is used only for the separate comparison (F60). The version-specific logarithmic defect in Bansal–Sinha v3 is proved in §3.16; it is not a counterexample to their theorem. Complete editions and locators are in [Appendix C](#ROOT-REFERENCES).
<!-- /passage:forr_references -->

## 4. Transcripts, addressed certificates, and the total function

<a id="CL-construction-context"></a>
<a id="AC-interface"></a>
<!-- passage:AC-interface -->
This section uses the partial function and exact two-output circuit supplied by §3.17, and gives the local tests and comparison property used in §5.3. The construction and Lemma 2.2 are due to OpenAI [OpenAI2026, §2.2, pp. 5–6]; the comparison property appears in its §3.3, p. 10. All queries below reveal one physical input bit.

A winning column must do two things: contain an all-one string, and supply a zero in every other column. Its zero witnesses are stored in a cell whose address is determined by several partial-function values. Transcripts in that cell certify that these values are defined and that the proposed address is correct. This gives a total predicate even when many of the partial-function instances lie outside their promise. The outward direction of the pointers also makes the winner safe against an opponent whose decoded address is meaningless: every pointer into the winner still reaches a one.
<!-- /passage:AC-interface -->

### 4.1. What a transcript certifies

<a id="AC-circuit"></a>
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

<a id="CL-transcripts"></a>
<a id="AC-transcripts"></a>
<!-- passage:AC-transcripts -->
A transcript $\tau\in\{0,1\}^{S}$ proposes a value for every non-input gate. At a gate, an input predecessor is read from the actual string $a$, a gate predecessor is read from its earlier entry in $\tau$, and a constant predecessor is known without a query. We call the transcript *gate-consistent* when every proposed gate value agrees with that gate's Boolean truth table on these predecessor values. Let $\operatorname{ev}_C(a)$ denote the transcript obtained by evaluating the circuit in topological order.

<!-- claim:NCL-transcript-characterization -->
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

### 4.2. Columns and their selected cells

<a id="CL-layout"></a>
<a id="AC-layout"></a>
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

<a id="CL-address-winner"></a>
<a id="CL-fidelity"></a>
<a id="AC-winner"></a>
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

<a id="CL-unique"></a>
<a id="AC-total-unique"></a>
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

### 4.3. A four-column instance

<a id="AC-example-promise"></a>
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

<a id="AC-example-board"></a>
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

### 4.4. The local tests

<a id="CL-local-tests"></a>
<a id="AC-tests"></a>
<!-- passage:AC-tests -->
Fix a candidate pair $(i,s)$. The partial-function conditions in (4.5) can be replaced by tests on the stored transcripts. Use the following list, writing $g_e(y;i,s)=1$ when the test with label $e$ passes.

**Column tests.** There is one test for each of the $m$ bits of $X_i$. It passes exactly when that bit is one, so it uses one query.

**Pointer tests.** For each of the $m-1$ other columns, the test reads the selected outward pointer in $B_{i,s}$ and checks that it reaches a zero in its designated target column. It first reads the $\ell$ pointer bits, decodes the row without a query, and then reads that target bit. Thus its worst-case depth is $\ell+1$, even though its target coordinate depends on the earlier answers.

**Gate tests.** For each of the $r$ stored transcripts and each of its $S$ non-input gates, the test checks that the claimed output equals the gate's truth table on its two predecessors. There are $rS$ such tests. Each reads the claimed value and at most two predecessor values, using at most three queries. An input predecessor is read from the actual address string; a gate predecessor is read from the transcript; a constant needs no query.

**Output tests.** For each $h\in[r]$, one test requires the transcript's domain output to be one, and another requires its value output to equal $s_h$. These are $r$ domain tests and $r$ value tests, each using one query. They check the meaning of the output bits after gate consistency has been checked: consistency alone does not assert either that the input is promised or that its value is the chosen address bit.

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

<a id="CL-local-equivalence"></a>
<a id="AC-local-equivalence"></a>
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

The explicit procedures defining the tests use at most one, three or $\ell+1$ queries, as appropriate. They are exact on every input, regardless of whether the candidate is a winner or its address instances are promised. Their largest depth is (4.13). ∎
<!-- /passage:AC-local-equivalence -->

<a id="CL-dichotomy"></a>
<a id="AC-dichotomy"></a>
<!-- passage:AC-dichotomy -->
It follows that a winning column has all tests passing at its unique true address. At every other address at least one test fails. If a column is a nonwinner, then every address has a failing test: an address at which all tests passed would contradict (4.12). This includes columns with an unpromised instance. Gate consistency cannot repair that instance, because a true transcript then has domain output zero; changing that output to one makes at least one gate equation fail.
<!-- /passage:AC-dichotomy -->

<a id="AC-example-tests"></a>
<!-- passage:AC-example-tests -->
For the four-column board, the supplied finite circuit has $S=180$ non-input gates, with domain and value outputs at gates 178 and 179 using zero-based gate numbering. Each candidate has

$$
K=4+3+2(180+2)=371
\tag{4.14}
$$

tests. At $(1,10)$, the four column tests, three pointer tests, 360 gate tests, two domain-output tests, and two value-output tests all pass. At $(1,00),(1,01),(1,11)$, respectively, there are $1,2,1$ failed tests: the proposed address disagrees with one or two true output bits, while every pointer still reaches its designated zero. Column 2 has a failing domain-output test at every address, despite all its gate equations being satisfied. Every pointer it directs into column 1 also reaches a one.

The checker evaluates the partial function from the integer expression (4.7) and evaluates the Boolean circuit separately. It checks all 256 eight-bit inputs against the circuit's outputs, all 16 candidate pairs on the specified board against (4.5), and every one of the 360 single-bit changes to the selected transcripts. It also checks six witnesses showing that every coordinate of a two-bit-pointer/four-bit-target lookup is essential. All these finite checks pass.

A second board in the output isolates the domain test. Its off-promise column is all ones, its stored transcripts are the true ones, and its pointers reach zeros in all other columns. At the address named by its value-output bits, every test except one domain-output test passes. Removing the domain tests would accept this column incorrectly. With the full test list, the board has no winner and the function is zero.

The full gate list, complete base board, selected transcripts, test counts and construction of the second board are in [examples/circuit.json](../research/returns/round3/members/04_addressed_construction/examples/circuit.json), [examples/board.json](../research/returns/round3/members/04_addressed_construction/examples/board.json), and [examples/output.json](../research/returns/round3/members/04_addressed_construction/examples/output.json). From [the preserved construction return](../research/returns/round3/members/04_addressed_construction/), run `python3 examples/check_example.py` to reproduce the output using the Python standard library and exact integer or rational arithmetic. These are finite computational checks, separate from the general proofs above and from the supplied Lean evidence.
<!-- /passage:AC-example-tests -->

### 4.5. A shallow lookup can have large support

<a id="AC-pointer-support"></a>
<!-- passage:AC-pointer-support -->
The pointer bound measures adaptive depth. It does not give a fixed set of only $\ell+1$ input coordinates on which the test depends. For one pointer test, its complete relevant coordinate set consists of the $\ell$ pointer bits and all $m$ bits of the target column. Each is essential when $\ell\geq1$.

To see this for a target bit, set the pointer to that row, hold every other coordinate fixed, and flip the selected bit. The test changes. To see it for a pointer bit, choose two pointer words differing only in that bit. The pointer bijection sends them to distinct rows. Assign different Boolean values to those two target bits and hold all other physical coordinates fixed. Changing the chosen pointer bit changes the test. Thus the support is exactly $m+\ell$, although every evaluation path reads only $\ell+1$ bits.

The four-column example has six essential coordinates and depth three. This corrects an earlier ledger description of fixed support. The original preprint already describes the adaptive lookup and requires no correction at this point [OpenAI2026, Lemma 2.2, p. 6].
<!-- /passage:AC-pointer-support -->

### 4.6. Coherent evaluation of an arbitrary test index

<a id="CL-coherent-tests"></a>
<a id="AC-coherent"></a>
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

<a id="AC-clean-oracle"></a>
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

<a id="AC-uniform-sampler"></a>
<!-- passage:AC-uniform-sampler -->
Uniform-index evaluation is a particular use of (4.15). Prepare the input-independent state $K^{-1/2}\sum_e|e\rangle$ and run the controlled evaluator. If $h$ tests fail, the probability of observing a failed test is $h/K$, because the index blocks are orthogonal and each test is exact. Thus all tests passing gives failure-detection probability zero, while a nonwinner at any proposed address gives probability at least $1/K$. The later search routine uses the evaluator and its inverse with the retained work registers. A theorem only about this uniform distribution would not, by itself, supply the arbitrary-index action (4.15).
<!-- /passage:AC-uniform-sampler -->

### 4.7. Why a winner defeats an unpromised opponent

<a id="AC-comparison"></a>
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

### 4.8. Attribution and formal correspondence

<a id="AC-attribution"></a>
<!-- passage:AC-attribution -->
Göös, Pitassi and Watson use a unique all-one column with a pointer chain through one zero in each other column [GPW2018, Theorem 5 and §2.1, pp. 3–5 of the ECCC revision](https://eccc.weizmann.ac.il/report/2015/050/). The chain differs from the direct outward pointers here. The use of partial-function answers to address a certificate array follows Aaronson, Ben-David and Kothari's cheat-sheet framework [ABK2019, §6.1, Definitions 14–15, pp. 20–21]. Their Lemma 17, p. 22, supplies the evaluate-then-check strategy for their cheat-sheet function, including rejection of certificates for unpromised inputs. The present proof establishes the properties of the particular multi-column construction (4.5); it does not obtain its later separation bounds by applying that lemma.

Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs explicitly discuss direct pointers from a distinguished element to a zero in every other column [ABBLSS2015, §1.3, “Use of a balanced tree,” pp. 5–6]. They also explain the exponential alphabet cost of that choice in their encoding. Here all pointer bits are explicit Boolean input coordinates, and reading a selected pointer is charged accordingly. These citations identify antecedents of the ingredients; the construction analyzed in this section is the one in OpenAI's preprint.
<!-- /passage:AC-attribution -->

<a id="AC-evidence"></a>
<!-- passage:AC-evidence -->
The exact source declarations and complete types are recorded in [correspondence.json](../research/returns/round3/members/04_addressed_construction/correspondence.json) and [evidence/lean_audit.json](../research/returns/round3/members/04_addressed_construction/evidence/lean_audit.json). In particular, `QuarticQuery.gateConsistent_iff_eq_circuitEval` gives (4.2), `QuarticQuery.winsAt_unique` gives pair uniqueness, and `QuarticQuery.winsAt_iff_localTests` gives (4.12) under `CircuitRealises C P`. The semantic bridge `QuarticQuery.winsAt_iff_paperWinsAt` has no such premise because both sides already refer to the partial function.

`QuarticQuery.Paper.construction_lemma_2_2_complete` packages the count, finite size bound, local-test equivalence, adaptive depth, arbitrary-index retained-workspace implementation, and physical query cap for the same circuit witnesses. Its premises $t\geq1$, `CircuitRealises C (P k t)`, and the circuit-size bound are exactly the supplied circuit properties. `QuarticQuery.Paper.construction_pointer_every_physical_coordinate` supplies the essential-coordinate witnesses for the support argument. The maintained [full support wrapper](../lean/QuarticQuery/Paper/ConstructionFull.lean), `construction_lemma_2_2_with_support`, conjoins those witnesses with every clause of the complete evaluator theorem. For each pointer test, every bit of the pointer word and every possible target coordinate has two full physical inputs differing only at that coordinate on which the test values differ. The witnesses and the evaluator use the same circuit. The printed Lemma 2.2 asserts the test count and adaptive/coherent query bounds; it does not separately assert this essential-coordinate diagnostic. The diagnostic strengthens the printed lemma and is included in the expanded maintained ledger to exclude the erroneous fixed-support interpretation discussed in §4.5. The older complete evaluator is partial relative to that expanded ledger row, not because the printed lemma requires an additional support clause. Its current source-bound execution evidence is recorded separately in the integration receipt. The clean oracle (4.16) and the explicit finite example have the separate ordinary-proof and computational status stated above.

The frozen packet includes a source-bound successful root-build receipt for the cited declarations. A later selected type/axiom audit includes the newer Paper construction wrappers; membership of that audit is recorded separately for every name and is not asserted for all older core declarations. Their 124 recorded local Lean/configuration hashes match the supplied packet bytes; the returned section review did not rerun Lean. The current integration separately performed the root build and targeted construction comparison recorded in §2.8. The recorded Construction Comparator receipt compares the four source theorems `winsAt_unique`, `existsUnique_gateConsistent`, `winner_no_incoming_zero`, and `winner_finds_zero`, together with their checked wrappers. It does not compare the newer complete local-test theorem. Old source comments and earlier returns calling those files unelaborated describe an earlier stage; the exact receipts and their scope are retained in the evidence sidecar. No human review is claimed.
<!-- /passage:AC-evidence -->

## 5. Quantum evaluation on every input


<a id="upper-section-interface"></a>
<!-- passage:upper-section-interface -->
The mathematical result and construction are OpenAI's [OpenAI2026, §3, pp. 7–10]. The present contribution is a proof reconstruction and a correction of its formal correspondence, with an exact cyclic example. No mathematical claim of the source preprint is changed.

We use the ordinary bit oracle and the maximum-over-branches query convention of §2.4. The incoming facts from §4 are the definition of a winner at an address, uniqueness of a winner, and the equivalence between winning at that address and passing all the exact local tests. For $m=4^t$, $t\geq1$, these tests number $K=m+(m-1)+r(S+2)$, have decision-tree depth at most $\max\{3,\ell+1\}$, and use $\ell=2t=\log_2m$, $r=40t=20\ell$. The incoming partial-function ingredient from §3 is the actual bounded-query Forrelation algorithm and its error reduction, together with the fixed realizing circuit of size $S\leq C_F(k)m\ell^2$. Its correctness is promised-input correctness; its query cap holds on all inputs. We repeat the particular uses of these facts below. 

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

<a id="upper-cyclic-example"></a>
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
The sampler is chosen before both $x$ and $s$. It does not need to know which vertex is dominant. An indicator of membership of a particular $s$ is used only in the analysis. The recorded formal list theorem has precisely this order of quantifiers. The older Boolean continuation, useful for final verification, is a separate implementation of the same search idea; its additional verifier error is explained next.
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
The reviewed packet contains a successful source-bound root build receipt and later exact-type/axiom auditing, in addition to focused module passes. The former record labels its commit `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`, while the packet manifest labels its repository commit `1dd469dd0042b937b739da3bc211eeb60bdf7462`. For that frozen local Lean/configuration closure, all 124 supplied source hashes agree across the packet files, evidence snapshot, root receipt, dependency export and axiom verdict. This makes the recorded evidence applicable to those exact bytes despite the differing commit labels. Those are retained earlier executions; the current integration’s new native runs are recorded separately in §2.8. The recorded toolchain is `leanprover/lean4:v4.36.0-rc2`; the dependency pins are preserved in the source receipt.

The fully qualified names and exact types are indexed in the correspondence; the shorter declaration names below identify their mathematical roles. The formal upper bound follows the same progression as the ordinary proof: amplify a successful outcome, combine trials into a bounded list, decode and verify a candidate, and then bound the integer budget. The state information carried at each step is part of the claim.

**From a successful state to its measured label.** `bounded_amplification` proves the complete abstract `Proc` assertion of Lemma 3.1, including phase-invariant observables, zero wrong-state mass, failure when the success probability is zero, and a uniform call cap. At the physical-program level, `Samples.amplify` supplies the measured `Runs` law used by the final bound. `quantum_amplify_samples` gives a coherent `Samples` realization of that same label law with retained workspace. Neither of the latter two types identifies a designated physical output subsystem with the original normalized successful state. The abstract theorem and the physical label law therefore support different conclusions; the missing identification is stated precisely below.

**Fresh registers and a bounded list.** The literal tensor construction in equation (15) is supplied by `equation_15`. The declarations `quantumWorkspace_uniformize` and `quantumTensorStage_of_samples` realize its stages in a common workspace. The alternative `Upper.stage_samples` may omit later work after failure: it gives the same successful index law, without equality of the full retained states. Proposition 3.2 only needs the specified list law. The declaration `quantumTournament` supplies an actual finite bounded-list `Samples` witness, its `Runs` implementation, a normalized nonnegative law, the dominant-membership estimate and the explicit 6072 query bound. Thus the older Boolean-only description does not describe this packet's available list theorem.

**Decoding, verification and the final budget.** The declarations `Paper.quantumDecode_correct`, `quantumComparison_state`, `quantumWinner_dominates`, `quantumVerify` and `quantumError_bound` expose the corresponding laws and all-input budgets. Correctness premises for promised Forrelation instances remain explicit; the budget does not disappear on unpromised inputs. For $k=l+1$, $m=4^t$ and $t\ge1$, `Fkm_forrCircuit_QLe` gives the algorithmic upper bound of Proposition 3.3, `Upper.Q_Fkm_le` gives its numerical complexity form, and `Upper.budget_le` bounds the actual integer budget by the expression with logarithmic exponent six. These steps use the measured laws already available, so the remaining full-state specification is not an extra assumption of the final upper bound.

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

To express the preprint's black-box uniformity, the underlying program with slots for $A$ and $A^{-1}$ must be fixed by $\gamma,\eta$ and the register/query interface before the preparation oracle is supplied. Its branches, $M,N$ and cap cannot depend on $p_x$. The auxiliary space, routing and all non-oracle gates are input-independent. An equivalent adaptive formulation gives the same normalized original-register state, up to phase, on every positive-mass successful history. The finite-coordinate version and an explicitly uncompiled proposed interface are in the [quantum gap record](../research/returns/round3/members/05_quantum_upper/LEAN_GAPS.md).

The ordinary fresh-trial/routing argument in §5.1 supplies the mathematical construction. The packet does not supply a source-bound Lean theorem of this full physical type. In particular, the coherent composition can retain a copy of a successful output label in auxiliary registers, and the measured compilation route reads a complete basis label. A proof of the displayed factorization, or an equivalent output-subsystem theorem after a specified uncomputation, is still needed before promoting the physical wrapper to the full state claim. This missing formal bridge is not an extra assumption in the proof of Proposition 3.3: that proof uses only measured labels, whose law is already supplied by the compiled route.
<!-- /passage:upper-missing-physical-state -->

## 6. The classical lower bound

### 6.1. A direct product with a separate query cap on each input

<a id="CL-direct-product-statement"></a>
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

This is the statement of [OpenAI, §4.1, Lemma 4.1, pp. 11–12][OpenAI2026].
Its one-input hypothesis concerns every bounded-depth strategy under a fixed
input law; it does not assert that every posterior encountered during the
algorithm is equally hard. The proof tracks the optimum under each posterior
with its remaining allowance. The case $L=0$ allows only constant guesses.
If $r=0$, the answer vector is empty and the bound is $1\leq1$.
<!-- /passage:CL-direct-product-statement -->

<a id="CL-product-law"></a>
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

<a id="CL-conditional-values"></a>
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

<a id="CL-supermartingale"></a>
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

<a id="CL-independent-information"></a>
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

<a id="CL-joint-cap"></a>
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

<a id="CL-adaptive-example"></a>
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
The exact calculation and enumeration in [worked_example.md](../research/returns/round3/members/06_direct_product/worked_example.md)
check all 16 input pairs, all 10 one-input trees of depth at most one, and
all 5,188 vector-output trees satisfying the separate caps. This finite check
illustrates the proof and its limits; the preceding argument proves the
general theorem.
<!-- /passage:CL-adaptive-example -->

<a id="CL-weighted-values"></a>
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

<a id="CL-weighted-product"></a>
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

<a id="CL-normalization"></a>
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

<a id="CL-planted-interface"></a>
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

<a id="CL-literature-and-verification"></a>
<!-- passage:CL-literature-and-verification -->
**Sources and formal correspondence.** The proof above follows the
conditional-value argument in [OpenAI, §4.1][OpenAI2026]. Its prior proof source
is [Drucker, arXiv:1005.0644v2, §1.3, Lemmas 3.1–3.2 on printed pp. 11–12,
and the last paragraph of §3 on p. 13][Drucker2012]. Drucker's Theorem 1.1
instead treats a global budget $\alpha\varepsilon Tk$ and obtains
$(2^{\alpha\varepsilon}(1-\varepsilon))^k$; it is not the statement (6.1).
The earlier [Shaltiel, ECCC TR01-009, §5, Definition 4, Theorem 5, and
Lemma 7, printed pp. 11–12][Shaltiel2001] defines fairness by at most a separate
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

The supplied receipts record successful native compilation of the packet’s exact
source bytes; the returned section review made no fresh Lean run. The current
integration’s new root build and comparison scope are recorded in §2.8. The headline dependency
closure still uses the unnormalized route, and no exact-declaration
Comparator pass is supplied for these helpers. The conditional-value file's
old “UNELABORATED” header predates the successful receipts. Exact types,
byte checks, declaration membership, and the limits
of the recorded evidence are in [correspondence.json](../research/returns/round3/members/06_direct_product/correspondence.json), [lean_types.json](../research/returns/round3/members/06_direct_product/lean_types.json),
and [LEAN_GAPS.md](../research/returns/round3/members/06_direct_product/LEAN_GAPS.md). The arbitrary-information finite-behavior reduction,
the generic joint-event truncation corollary, and the combined identity
(6.11) are ordinary deductions supplied here; they are not new Lean builds
or new Comparator passes. The worked example is a separate exact finite
calculation. This reconstruction has received no human mathematical review.
<!-- /passage:CL-literature-and-verification -->

### 6.2. The hard distribution and the hidden address

<a id="CL-entry-interface"></a>
<!-- passage:CL-entry-interface -->
We first recall the objects needed below. Let \(P:D\to\{0,1\}\), where \(D\subseteq\{0,1\}^{n}\), and let \(C\) be a finite fan-in-two Boolean circuit with a domain output and a value output. The domain output is one exactly on \(D\); on \(D\), the value output equals \(P\). A circuit transcript records the values of all non-input gates. Topological evaluation supplies a unique transcript satisfying all gate checks.

For \(m=4^t\), \(t\ge1\), put \(\ell=\log_2m=2t\) and \(r=40t=20\log_2m\). Each of the \(m\) columns contains an \(m\)-bit string \(X_i\), \(r\) strings \(A_{i,1},\ldots,A_{i,r}\) of length \(n\), and a separate certificate cell \(B_{i,s}\) for each \(s\in\{0,1\}^{r}\). A cell contains a transcript for every \(A_{i,h}\) and an \(\ell\)-bit pointer into each other column. Every pointer encoding represents a row, since there are exactly \(2^\ell=m\) rows. When the \(A\)-strings of column \(i\) are promised, its true address is
\[
s_i=(P(A_{i,1}),\ldots,P(A_{i,r})).
\]
The total function \(F=F_{P,C,m}\) equals one exactly when some column \(i\) is all ones, all its \(A\)-strings are promised, and \(B_{i,s_i}\) contains correct transcripts and pointers to zeros in every other column.

The lower bound compares an input with one zero in every column against an input in which one column's zero is erased and its true cell is filled. A query algorithm must encounter one of those changes. The erased zero is hidden by the independent choice of the column. The filled cell is hidden by the difficulty of predicting an entire vector of partial-function values.

The address-and-certificate mechanism has the cheat-sheet antecedent of Aaronson, Ben-David and Kothari [ABK2019, §6.1, Definitions 14–15, and §6.2, Lemma 17, pp. 20–22](https://arxiv.org/pdf/1511.01937v2). Lemma 17 concerns upper bounds for their cheat-sheet function. The separate arrays and outward pointers of the present function are accounted for in the proof below.
<!-- /passage:CL-entry-interface -->

<a id="CL-minimax"></a>
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

<a id="CL-address-guess"></a>
<!-- passage:CL-address-guess -->
Apply Lemma 4.1 of §6.1 to independent \(U_1,\ldots,U_r\sim\mu\). If an algorithm makes at most \(L\) queries to each \(U_h\) on every execution, then
<!-- claim:claim-address-guess -->
\[
\Pr[\widehat s=(P(U_1),\ldots,P(U_r))]\le(2/3)^r.
\]
The algorithm may interleave its queries and use side information jointly independent of the whole tuple. Fixing that information and its random coins preserves the input law, so the deterministic bound can be averaged.

The prerequisite is the per-input-capped, or fair-algorithm, direct product. Its conditional-product proof is explained by Drucker [Drucker2012, §1.3, Lemmas 3.1–3.2, and the final paragraph of §3, pp. 6–7 and 11–13](https://arxiv.org/pdf/1005.0644v2), who attributes the fair case to Shaltiel. Drucker's headline theorem has a different global-budget statement. We use precisely the capped formulation proved in §6.1; no new direct-product result is assumed.
<!-- /passage:CL-address-guess -->

### 6.3. Coupled zero and one inputs

<a id="CL-generic-statement"></a>
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

<a id="CL-dummy"></a>
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

<a id="CL-planted"></a>
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

<a id="CL-tiny-planted-example"></a>
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

The files [checks/planted_example.py](../research/returns/round3/members/07_planted_lower_bound/checks/planted_example.py) and [checks/planted_example.json](../research/returns/round3/members/07_planted_lower_bound/checks/planted_example.json) implement all 192 physical bit coordinates of this toy and evaluate its winning predicate directly. This is a finite instance of the generic addressed construction. Its partial function is XOR, its address length is \(2\), and the later example query budget is \(4\); it is not a Forrelation instance or a choice satisfying \(r=40t\) and \(G=\lfloor mL/100\rfloor\).
<!-- /passage:CL-tiny-planted-example -->

<a id="CL-first-difference"></a>
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

<a id="CL-erased-zero-identity"></a>
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

<a id="CL-selection-independence-example"></a>
<!-- passage:CL-selection-independence-example -->
**Why the selected column must be independent.** Take four columns with independent uniform zero locations and query row zero in every column. This finite example has budget four; it is not the asymptotic choice $G=\lfloor mL/100\rfloor$. Each query finds a zero with probability $1/4$, so $\mathbb EZ=1$. An independent uniform column $I$ is hit with probability $1/4=\mathbb EZ/4$.

Now change only the rule for selecting $I$: after the queries, choose uniformly among the columns where a zero was found, and choose uniformly among all four if no zero was found. Symmetry under column permutations still makes $\Pr[I=i]=1/4$ for every $i$. But the selected zero is now hit exactly when at least one discovery occurred, with probability
\[
1-(3/4)^4=\frac{175}{256}>\frac14.
\]
Thus a uniform marginal law for $I$ does not suffice for the identity in (19); its independence from the whole dummy run is essential. The [retained independence checker](../research/returns/round3/members/09_evidence_backend/checks/eq19_independence_control.py) enumerates this finite experiment. This ordinary counterexample concerns the altered selection rule, not the preprint's independent experiment, and no Lean theorem for this example is asserted.
<!-- /passage:CL-selection-independence-example -->


<a id="CL-early-late"></a>
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

<a id="CL-zero-worlds"></a>
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

<a id="CL-zero-average"></a>
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

<a id="CL-zero-optional"></a>
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

<a id="CL-heavy"></a>
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

<a id="CL-simulator"></a>
<!-- passage:CL-simulator -->
Fix a column \(i\) and a time \(q\in\{1,\ldots,G\}\). The simulator's queried inputs are the \(r\) strings of that column. Give it the independent outside data: every \(J_j\), all the \(A\)-strings of the other columns, and the fixed blank cells. It receives no target string, target address, or target transcript as side information.

Simulate \(T\) on the dummy input up to its proposed \(q\)-th query. Answer every outside query from the supplied data. Answer a query to one of the target strings by making the corresponding oracle query, charging it against one shared counter. Abort before that counter would exceed \(L\). If time \(q\) is reached and the proposed query is to \(B_{i,s}\), output \(s\). If the simulated run terminates, aborts, or proposes a different kind of coordinate, output a fixed vector. Identifying the proposed cell's address requires no query to its contents.
<!-- claim:def-simulator -->

For every possible tuple of target inputs, this simulator makes at most \(L\) target queries in total. It therefore satisfies each of the \(r\) separate caps in Lemma 4.1. The cap holds even on branches where the original tree would eventually make column \(i\) heavy. Because the outside data are jointly independent of the target tuple, the simulator's unconditional success is at most \((2/3)^r\).
<!-- /passage:CL-simulator -->

<a id="CL-simulator-example"></a>
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

The exact enumeration in the [planted example](../research/returns/round3/members/07_planted_lower_bound/checks/planted_example.py) fixes other columns' \(A\)-strings, ranges over all \(4^4\) zero-position vectors and all \(16\) target tuples, and independently ranges over the four choices of \(I\). It obtains
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

<a id="CL-joint-event"></a>
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

<a id="CL-conditioning-counterexample"></a>
<!-- passage:CL-conditioning-counterexample -->
That distinction is necessary in general. On the promised two-bit inputs \(\{01,10,11\}\), let \(P\) be AND and let \(\mu\) be uniform. Every one-query algorithm has success at most \(2/3\): after either coordinate is queried, one answer identifies a unique input and the other leaves two equally likely, oppositely labelled inputs.

A tree that queries the first bit can stop and correctly output \(0\) on the answer-zero branch, and query the second bit on the answer-one branch. With cap \(L=1\), the complete original run is nonheavy exactly on input \(01\). Its conditional success given nonheaviness is therefore \(1\). A simulator that aborts before the second query and defaults to \(0\) has unconditional success \(2/3\), while correct-and-nonheavy has probability \(1/3\). The unconditional bound is valid and the conditional bound \(1\le2/3\) is false. The example file checks all three inputs and every deterministic one-query tree.
<!-- /passage:CL-conditioning-counterexample -->

<a id="CL-cell-union"></a>
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

<a id="CL-discrepancy"></a>
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

<a id="CL-tail-numeric"></a>
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

<a id="CL-randomized-contradiction"></a>
<!-- passage:CL-randomized-contradiction -->
Suppose a randomized algorithm with worst-case query cost at most \(G\) computed \(F_{P,C,m}\) with error at most \(1/3\) on every input. Every dummy input is a zero-input and every supported planted input is a one-input. Averaging the pointwise correctness requirements gives an output-one probability gap of at least \(2/3-1/3=1/3\).

Fix the algorithm's random coins. The resulting deterministic tree has depth at most \(G\), so its gap is at most \(6/100\). Averaging over the coins preserves that upper bound, contradicting the preceding lower bound. Since the total function has finitely many input bits, reading all of them computes it exactly; its randomized complexity is therefore a finite minimum. The absence of a budget-\(G\) algorithm implies \(R(F_{P,C,m})>G\), proving the generic theorem.

In the finite input model, random coins can be represented by a finite mixture of bounded-depth trees: there are only finitely many possible trees, so group coin outcomes by the tree they induce. This is an ordinary finite-behavior reduction. The Lean model directly uses finite mixtures; no theorem constructing a pushforward from an arbitrary external probability space is claimed here.
<!-- /passage:CL-randomized-contradiction -->

<a id="CL-forrelation-input"></a>
<!-- passage:CL-forrelation-input -->
We now return to the Forrelation family. Fix \(k\ge2\), let \(P=P_{k,m}\) on \(km\) bits, and choose
\[
L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor.
\]
The required prerequisite from §3 is that \(L<R(P_{k,m})\) for all sufficiently large powers of four \(m\).

For comparison, Bansal–Sinha [BansalSinha2021, Theorem 1.3 and Corollary 1.4, printed p. 4](https://arxiv.org/pdf/2008.07003v3) state, with promise threshold \(\delta=2^{-5k}\), a lower bound
\[
\Omega\!\left(k^{-29}
\left(\frac{m}{\log(km)}\right)^{1-1/k}\right)
\]
at error \(1/3\). Their block dimension is \(m\); the full input has \(km\) bits. For fixed \(k\) and \(m\ge k\), the ratio of a positive constant multiple of this bound to \(m^{1-1/k}/(\log_2m)^2\) is bounded below by a positive \(k\)-dependent constant times \((\log_2m)^{1+1/k}\). It tends to infinity, giving the strict prerequisite eventually.

This comparison identifies the original literature input and the exact strength used. The separate source audit of Bansal–Sinha v3 §5.4 concerns the displayed comparison at source lines 1180–1181: for a summation level \(j>k\), its logarithm exponents differ by \((j/k-1)/2\). The threshold at line 1184 is a subsequent statement. That discrepancy requires a separate argument for that displayed comparison; it does not refute the stated theorem. The present section consumes only the fixed-\(k\) prerequisite established in §3 and its formal endpoint. It does not undertake a full re-audit of the sharper parameter-uniform theorem.
<!-- /passage:CL-forrelation-input -->

<a id="CL-floors"></a>
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

<a id="CL-concrete-lower"></a>
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

### 6.7. Formal correspondence

<a id="CL-formal-scope"></a>
<!-- passage:CL-formal-scope -->
The retained [planted correspondence](../research/returns/round3/members/07_planted_lower_bound/correspondence.json) records the packet's complete source signatures, compiler-reported types, hypotheses and historical receipts. The [integrated correspondence](reasoning_record_correspondence.json) adds the maintained conjunction wrappers and keeps each evidence observation bound to its own source.

**The whole equation (19).** `QuarticQuery.Paper.erasedZero_eq_expectedZeros_div` states the exact identity. Its algebraic form is valid for arbitrary finite real weights; nonnegativity and normalization are needed to interpret the averages as probabilities. The older `Paper.eq_19` states only the hit-probability upper bound. The maintained source now has two explicit conjunctions: [Eq19Whole](../lean/QuarticQuery/Paper/Eq19Whole.lean), `Paper.eq19_whole`, gives the equality together with the hit-probability bound; [Eq19Complete](../lean/QuarticQuery/Paper/Eq19Complete.lean), `Paper.eq_19_complete`, gives the equality together with the bound on the divided expectation. Both use one nonnegative normalized law $\mu$, one deterministic query tree $T$ and its cap $\operatorname{depth}(T)\le G$. Their formal column size is $2^\ell$, with $\ell=2t$ giving the paper's $m=4^t$. No promise-support or hardness premise is needed for this row. These are the complete alternatives
\[
 \begin{aligned}
 &\left(\Pr[\mathrm{hit}]=\frac{\mathbb E Z}{m}\right)
 \ \wedge\ 
 \left(\Pr[\mathrm{hit}]\le\frac{4G}{m^2}\right),\\
 &\left(\Pr[\mathrm{hit}]=\frac{\mathbb E Z}{m}\right)
 \ \wedge\ 
 \left(\frac{\mathbb E Z}{m}\le\frac{4G}{m^2}\right).
 \end{aligned}
\]
The exact execution evidence belongs to each named declaration and is reported in the dated integration receipt. The unchanged returned proposal remains historical provenance; its earlier uncompiled status does not describe a later maintained declaration.

**An independently written product experiment.** The [independent specification](../lean/QuarticCorpus/Independent/Eq19/Spec.lean) defines the reference input coordinate by coordinate, the event that a column's zero lies on the query path, and the number of distinct discovered columns. It writes the law as explicit products: all address strings have independent mass $\mu$, every zero position is independently uniform, and the selected column has a further independent factor $1/m$. Its expectations do not use the maintained definitions `dummy`, `foundZero`, `coupledAvg`, `discoveredZeros` or `expectedZeros`. The [bridge](../lean/QuarticCorpus/Independent/Eq19/Bridge.lean) identifies each of those objects before transporting the complete conjunction. It still shares the project's coordinate, query-tree, path and depth interfaces; that declared boundary is tested by separate finite path controls. The direct actual-vocabulary comparison and this explicit-product comparison therefore check different things. Neither identifies the alternative search proof with the paper's early/late argument.

**The expectation estimate and its route.** `Paper.uniform_zero_given_transcript` states the positive-probability transcript posterior. `Paper.expectedZeros_le_four` obtains the endpoint through the stronger zero-search induction. Thus even a complete conjunction theorem for (19) does not formalize the early/late proof of $\mathbb E Z$ in §6.4. The distinction concerns the proof route and the compound expectation row, not the truth of the displayed endpoint.

**The simulator and the eventual lower bound.** The Paper wrappers state the absolute form of (18), the individual-time joint event (21), the cell bound (22), and the absolute discrepancy (23). The core one-sided discrepancy theorem remains a separate sufficient endpoint. Prose query time $q$ corresponds to the source's zero-based index $q-1$. The exact logarithmic tail bound, its envelope limit and the elementary finite power estimate have separate statements. Finally, `Paper.prop_4_2` and `Paper.prop_4_2_forrCircuit` supply the eventual fixed-$k$ hardness premise using the Forrelation theorem. The core `Gvalue_lt_R_Fkm` keeps that premise in its own type. A proof of an unconditional wrapper does not erase the binder of a conditional supplier.

The $m+1$ refinement, elementary convex-separation proof, arbitrary-coin finite-behaviour reduction and finite examples are ordinary arguments or computations at their stated scope. They do not acquire formal status from a nearby endpoint theorem. A matching build, an axiom audit, a Comparator result, review of the intended statement and human review are different kinds of evidence.

<!-- /passage:CL-formal-scope -->

## 7. The optimal exponent

<a id="ROOT-FAMILY-ASSEMBLY"></a>
<!-- passage:ROOT-FAMILY-ASSEMBLY -->
The construction proves that every proposed universal power below four fails. Together with the quartic upper bound in Appendix A, this gives
\[
\alpha_{\mathrm{tot}}=4.
\]
Here \(R\) and \(Q\) are the minimum worst-case query caps for success probability at least \(2/3\) on every input. The exponent is defined by
\[
\alpha_{\mathrm{tot}}=\inf\left\{\alpha\geq0:
\exists K>0\ \forall n\geq1\ \forall f:\{0,1\}^n\to\{0,1\},
\quad R(f)\leq K(1+Q(f))^\alpha\right\}.
\]
The universal bound must hold with one constant for every total Boolean function and every input length. The construction parameter is chosen after the proposed exponent; the function's size then tends to infinity while that parameter remains fixed. This is the argument of [OpenAI (2026), §5, printed p. 14][OpenAI2026].

We first collect the two estimates for the same functions. Let \(k\geq2\) be fixed, write \(m=4^t\), and let \(C_{k,t}\) be the exact circuit for the promise and value of \(P_{k,m}\) constructed in §3.17. In the notation of §4, set \(F_{k,m}=F_{k,m}[C_{k,t}]\). The quantum estimate of §5.4 and the randomized estimate of §6.6 give constants \(C_k>0\), \(b_k\in\mathbb N\), and \(t_0(k)\) such that
\[
Q(F_{k,m})\leq C_k\sqrt m\,(\log_2m)^{b_k},
\qquad
R(F_{k,m})\geq\frac1{400}\,
\frac{m^{2-1/k}}{(\log_2m)^2}
\qquad(t\geq t_0(k)).
\tag{7.1}
\]
The proved quantum estimate permits \(b_k=6\) for every \(k\). Its constant and the threshold may depend on \(k\), and they are independent of \(t\). The circuit has size \(O_k(m(\log_2m)^2)\). Both inequalities in (7.1) use this circuit: choosing unrelated witnesses for the two estimates would not give a separation. These are the conclusions of [OpenAI (2026), Propositions 3.3 and 4.2][OpenAI2026], with the explicit logarithmic power and floor constant supplied by the accompanying formal development.

For completeness, the lower estimate follows from the two nested floors without an asymptotic convention. The elementary estimate \(4t^2\leq2^t\) holds for integers \(t\geq8\): equality holds at eight, and \((t+1)^2\leq2t^2\) propagates it. Since \(1-1/k\geq1/2\), the quantity \(a=m^{1-1/k}/(2t)^2\) is at least one. For any real \(a\geq1\), putting \(j=\lfloor a\rfloor\) gives \(a<j+1\leq2j\), and hence \(\lfloor a\rfloor\geq a/2\). Also \(m\lfloor a\rfloor\geq4^8\geq200\). The floor budget
\[
G=\left\lfloor\frac{m\lfloor a\rfloor}{100}\right\rfloor
\]
therefore satisfies \(G\geq m\lfloor a\rfloor/200\geq ma/400\). Proposition 4.2 gives \(R(F_{k,m})>G\) after the fixed-\(k\) Forrelation threshold. Enlarging \(t_0(k)\) to include eight proves (7.1).
<!-- /passage:ROOT-FAMILY-ASSEMBLY -->

### 7.1. A fixed parameter and a strict exponent gap

<a id="ROOT-RATIO"></a>
<!-- passage:ROOT-RATIO -->
Fix \(0\leq\alpha<4\). Choose an integer \(k\geq2\) with
\[
k>\frac{2}{4-\alpha}.
\tag{7.2}
\]
This choice ensures that
\[
\varepsilon_\alpha=2-\frac1k-\frac\alpha2>0.
\]
Keep \(k\) fixed from now on. Since \(\sqrt m(\log_2m)^{b_k}\geq1\) for \(m\geq4\), the upper estimate in (7.1) gives
\[
1+Q(F_{k,m})\leq(1+C_k)\sqrt m\,(\log_2m)^{b_k}.
\]
All bases are positive, and \(\alpha\geq0\), so exponentiation preserves this inequality. Combining it with the lower estimate yields the finite quotient bound
\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\geq
\frac{1}{400(1+C_k)^\alpha}\,
\frac{m^{\varepsilon_\alpha}}{(\log_2m)^{2+\alpha b_k}}
\qquad(t\geq\max\{t_0(k),1\}).
\tag{7.3}
\]

The right side tends to infinity. To see explicitly why its logarithmic denominator is harmless, put \(e=2+\alpha b_k\). For \(m=4^t\), the logarithm of its varying factor is
\[
\ln\!\left(\frac{m^{\varepsilon_\alpha}}{(\log_2m)^e}\right)
=2\varepsilon_\alpha t\ln2-e\ln(2t).
\]
For \(u\geq1\),
\[
\ln u=\int_1^u\frac{ds}{s}
\leq\int_1^u\frac{ds}{\sqrt s}
\leq2\sqrt u.
\]
Hence \(\ln(2t)/t\to0\), whereas \(2\varepsilon_\alpha\ln2>0\). The displayed logarithm tends to infinity, and so does the quotient in (7.3). This includes \(\alpha=0\); no division by \(Q\) is involved.

For a fixed \(k\), the argument applies exactly when \(\alpha<4-2/k\). For example, \(k=2\) supplies the threshold exponent three, and \(k=3\) supplies \(10/3\). Thus \(k=3\) already refutes a cubic universal bound. At \(\alpha=4-2/k\), the power gap \(\varepsilon_\alpha\) vanishes, and (7.3) alone supplies no divergence. No fixed finite \(k\) in this argument attains exponent four.
<!-- /passage:ROOT-RATIO -->

### 7.2. Excluding all smaller universal powers

<a id="ROOT-NO-SMALLER"></a>
<!-- passage:ROOT-NO-SMALLER -->
Let \(K>0\) be any proposed universal constant. With \(k\) already chosen by (7.2), the quotient in (7.3) exceeds \(K\) for every sufficiently large \(t\). Thus the corresponding function violates
\[
R(f)\leq K(1+Q(f))^\alpha.
\tag{7.4}
\]
The construction uses a finite nonempty set of input coordinates. A bijection with \([n]\), where \(n\geq1\) is its cardinality, preserves both query complexities: rename the queried coordinate, leaving every answer, probability, and query count unchanged. Consequently the structured function is also a counterexample among the total functions \(\{0,1\}^n\to\{0,1\}\) quantified in (7.4).

We have proved that every \(0\leq\alpha<4\) fails the universal bound. Negative exponents are outside the defining set for \(\alpha_{\mathrm{tot}}\), whose definition requires \(\alpha\geq0\). Appendix A proves that four belongs to that set. Thus the set is nonempty, each of its members is at least four, and four itself is a member. Four is its minimum and therefore its infimum.

For the unshifted cubic statement, suppose some real \(K\) satisfied \(R(f)\leq KQ(f)^3\) for all total \(f\). Because \(Q(f)\geq0\), replacing \(K\) by \(\max\{K,1\}\) and then \(Q(f)^3\) by \((1+Q(f))^3\) would imply (7.4) with \(\alpha=3\) and a positive constant. The \(k=3\) family contradicts that statement. No assumption that \(Q(f)>0\) is needed. This is the universal cubic conjecture in [Aaronson, Ben-David, Kothari, Rao and Tal, arXiv:2010.12629v1, §7, Conjecture 2, printed p. 20][ABKRT2020].

The proof chooses the parameters in the order
\[
\alpha<4\ ;\quad k=k(\alpha)\ ;\quad K>0\ ;\quad t\text{ sufficiently large}.
\]
A family with a quantitative schedule \(k=k(t)\) requires additional uniform estimates and is a separate result. It is not needed for the theorem just proved.
<!-- /passage:ROOT-NO-SMALLER -->

### 7.3. Formal correspondence

<a id="ROOT-EXPONENT-CORRESPONDENCE"></a>
<!-- passage:ROOT-EXPONENT-CORRESPONDENCE -->
The source preprint supplies the attribution for this exponent argument; the supplied Lean sources and frozen execution records support the formal claims separately. The named-circuit statement `QuarticQuery.Paper.construction_family_named` proves (7.1) for `Forrelation.forrCircuit (k-1) t`, with constant \(1/400\), logarithmic exponent six, the quantum constant `Upper.budgetConst k`, and the circuit-size bound in the same conclusion. `construction_equation_two` packages these facts existentially. Neither statement has an unproved Forrelation binder.

`QuarticQuery.Paper.classical_ratio_arithmetic` proves the finite quotient inequality. `classical_exponent_ratio` adds divergence of the explicit lower envelope and the quotient for abstract sequences satisfying the fixed-parameter bounds. `classical_Fkm_ratio` specializes all three conclusions to the named total-function family with \(b_k=6\). Thus the literal quotient and limit now have formal support; the older declaration `QuarticQuery.eventually_gt_rpow` supplies only the sufficient eventual strict comparison. The elementary integral argument above explains the same limit by a different proof.

`QuarticQuery.exists_nat_exponent`, `not_universalPower_of_family`, and `alphaTot_eq_four_of` implement the choice of \(k\), exclusion of smaller exponents, and infimum argument. Their intermediate binders for family bounds and reindexing are discharged by the model and construction theorems. The final declarations `alphaTot_eq_four_unconditional`, `theorem_1_1_unconditional`, and `cubic_bound_fails_unconditional` have no mathematical assumption left open.

The timestamped root-build receipt contains all these names and binds the supplied source bytes. The reviewed type-and-axiom audit separately covers the newer named-family and quotient declarations. The timestamped Unconditional Comparator receipt covers the final compared declarations, not every explanatory helper. The challenges share the maintained definitions and theorem specifications; independent compilation does not make them independently authored mathematical tests. These descriptions identify the earlier supplied receipts. The current integration also performed the new root build, named comparisons and paranoid check recorded in §2.8; that execution does not create additional helper theorems or extend the earlier selected type-and-axiom audit.
<!-- /passage:ROOT-EXPONENT-CORRESPONDENCE -->


## Appendix A. The universal quartic bound

<a id="ROOT-APPENDIX-INTRO"></a>
<a id="R3-A-RESULT"></a>
<!-- passage:R3-A-RESULT -->
Every total Boolean function satisfies
\[
 R(f)\le D(f)\le 35^4 Q(f)^4
       =1{,}500{,}625\,Q(f)^4.
\tag{A.1}
\]
Here \(D\) is exact deterministic query complexity and \(R,Q\) use error at most \(1/3\), with a worst-case query cap. The constant is independent of the function and its number of input bits. Constant functions have zero query complexity, so the estimate includes the zero-dimensional cube. In particular, \(R(f)\le 1{,}500{,}625(1+Q(f))^4\); this is the upper endpoint needed in §7.

The quartic upper bound is due to [Aaronson, Ben-David, Kothari, Rao and Tal, arXiv:2010.12629v1, Theorem 2, printed p. 2][ABKRT2020]. We reconstruct the argument of [OpenAI's Appendix A, printed pp. 14–17][OpenAI2026], keeping its two applications of the nonnegative adversary method. One bounds block sensitivity, the other spectral sensitivity. Huang's signed cube converts spectral sensitivity into a degree bound; Midrijānis's decision tree then multiplies degree by block sensitivity. The explicit coefficient in (A.1) belongs to the supplied implementation and is not an optimality claim.
<!-- /passage:R3-A-RESULT -->

### A.1. Degree, sensitive blocks and the sensitivity graph

<a id="ROOT-DEGREE-BLOCK"></a>
<a id="R3-A-DEFINITIONS"></a>
<!-- passage:R3-A-DEFINITIONS -->
Let \(f:\{0,1\}^n\to\{0,1\}\) be total. Its unique real multilinear representation is obtained by interpolating on the cube:
\[
 p_f(x)=\sum_{a\in\{0,1\}^n}
 f(a)\prod_{i:a_i=1}x_i\prod_{i:a_i=0}(1-x_i).
\]
At a cube point only its own interpolation term survives. For uniqueness, write a polynomial vanishing on the cube as \(p_0+x_np_1\). Evaluation at \(x_n=0\) and then \(x_n=1\), followed by induction, gives \(p_0=p_1=0\). We write \(\deg(f)\) for its largest nonzero monomial size and assign degree zero to both constant functions. Invertible affine changes between bits and signs preserve this degree: each direction does not increase degree. Replacing a nonconstant output by its sign \(1-2f\) also preserves degree, since it rescales every nonconstant coefficient by \(-2\).

For \(B\subseteq[n]\), let \(x^B\) be obtained from \(x\) by flipping exactly the coordinates in \(B\). A sensitive block at \(x\) is a nonempty \(B\) with \(f(x^B)\ne f(x)\). Define \(\operatorname{bs}(f,x)\) as the largest number of pairwise disjoint sensitive blocks at \(x\), and \(\operatorname{bs}(f)=\max_x\operatorname{bs}(f,x)\).

The sensitivity graph has the cube inputs as vertices and an edge between two inputs exactly when they differ in one coordinate and have different function values. Let \(S_f\) be its real adjacency matrix and put
\[
 \lambda(f)=\|S_f\|.
\]
Every matrix norm below is the operator norm for the Euclidean norm; there is no normalization by the number of vertices. These quantities will enter through
\[
 \operatorname{bs}(f)\le 35^2Q(f)^2,
 \qquad \lambda(f)\le35Q(f),
 \qquad \deg(f)\le\lambda(f)^2,
 \qquad D(f)\le\operatorname{bs}(f)\deg(f).
\tag{A.2}
\]
The two adversary estimates in (A.2) use different matrices: edges corresponding to a sensitive block may flip several coordinates and need not be edges of \(S_f\).
<!-- /passage:R3-A-DEFINITIONS -->

### A.2. The nonnegative adversary bound

<a id="ROOT-ADVERSARY-PERRON"></a>
<a id="ROOT-ADVERSARY-PROGRESS"></a>
<a id="ROOT-ADVERSARY-FINAL"></a>
<a id="R3-A-ADVERSARY"></a>
<!-- passage:R3-A-ADVERSARY -->
Let \(\Gamma\) be a nonzero real symmetric matrix indexed by cube inputs, with nonnegative entries and \(\Gamma_{xy}=0\) whenever \(f(x)=f(y)\). For a coordinate \(i\), define
\[
 (\Gamma_i)_{xy}=\Gamma_{xy}\mathbf1_{\{x_i\ne y_i\}},
 \qquad M=\max_i\|\Gamma_i\|.
\]
Then
\[
 Q(f)\ge
 \frac{1-2\sqrt2/3}{2}\frac{\|\Gamma\|}{M}
 \ge\frac1{35}\frac{\|\Gamma\|}{M}.
\tag{A.3}
\]
The denominator is positive: a nonzero entry joins distinct opposite-output inputs, and some coordinate distinguishes those inputs. Its mask is therefore nonzero. In particular, the hypotheses already force \(f\) to be nonconstant and \(n\ge1\).

We first choose a nonnegative unit vector \(v\) with \(\Gamma v=\|\Gamma\|v\). By the spectral theorem there is a real unit eigenvector \(w\) whose eigenvalue has absolute value \(\|\Gamma\|\). For \(v=|w|\), entrywise nonnegativity implies
\[
 v^{\mathsf T}\Gamma v\ge
 |w^{\mathsf T}\Gamma w|=\|\Gamma\|.
\]
The reverse bound follows from the operator norm. Equality in the Rayleigh quotient makes \(v\) an eigenvector for \(\|\Gamma\|\). This argument needs neither irreducibility nor positive definiteness.

Consider an algorithm with error at most \(1/3\) and query cap \(q\). Randomness can be purified. A projective measurement \(\{\Pi,I-\Pi\}\) can be stored coherently by the isometry
\[
\psi\longmapsto \Pi\psi\otimes|1\rangle+(I-\Pi)\psi\otimes|0\rangle.
\]
The two histories are orthogonal, and subsequent gates are controlled by the stored history, so the final output probabilities reproduce the sums of branch probabilities. Between successive query slots, controlled input-independent operations carry each live branch to its next query. For a halted branch, swap its query register with an auxiliary register prepared at a fixed valid index with answer \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). Every bit oracle fixes that auxiliary state. Swapping back after the query restores the branch's original registers. The program is finite and each branch has at most \(q\) queries, so the resulting fixed sequence has exactly \(q\) oracle slots and the same output probabilities. The input-independent isometries extend to unitaries after enlarging the workspace. Thus this conversion preserves the query cap; it introduces no extra factor two into (A.3).

Let \(\psi_x^t\) be its normalized pure state after \(t\) slots, including its histories. Track the complex-valued progress
\[
 W_t=\sum_{x,y}v_xv_y\Gamma_{xy}
           \langle\psi_x^t,\psi_y^t\rangle.
\]
Initially all states agree, so \(W_0=\|\Gamma\|\), and every input-independent unitary preserves \(W_t\). Just before a query write
\(\psi_x=\sum_i|i\rangle\phi_{x,i}\), where
\(\sum_i\|\phi_{x,i}\|^2=1\). If \(x_i=y_i\), the same answer permutation acts on both vectors. Otherwise the change of their inner product has absolute value at most
\(2\|\phi_{x,i}\|\|\phi_{y,i}\|\). With
\(u_i(x)=v_x\|\phi_{x,i}\|\), the triangle inequality and nonnegative weights give
\[
 |W_{t+1}-W_t|
 \le2\sum_i u_i^{\mathsf T}\Gamma_i u_i
 \le2M\sum_i\|u_i\|^2
 =2M.
\tag{A.4}
\]
The last equality uses \(\sum_xv_x^2=1\). In the equivalent controlled-phase oracle used by the Lean source, only the active control subspace contributes, so the same calculation uses \(\sum_i\|u_i\|^2\le1\), which is sufficient.

For the final overlap, let \(\Pi\) be the output-one projector and suppose \(f(x)=0,f(y)=1\). Put \(a=\|\Pi\psi_x\|^2\le1/3\) and \(b=\|\Pi\psi_y\|^2\ge2/3\). Orthogonal decomposition and Cauchy–Schwarz imply
\[
 |\langle\psi_x,\psi_y\rangle|
 \le\sqrt{ab}+\sqrt{(1-a)(1-b)}
 \le\frac{2\sqrt2}{3}.
\]
For the last inequality, write \(a=\sin^2u,b=\sin^2v\) with \(u,v\in[0,\pi/2]\). The expression is \(\cos(v-u)\); the constraints force its maximum to occur at \(a=1/3,b=2/3\). Summing this inequality against the weights gives
\( |W_q|\le(2\sqrt2/3)\|\Gamma\|\).
Telescoping (A.4), and then using the reverse triangle inequality, yields
\[
 (1-2\sqrt2/3)\|\Gamma\|
 \le |W_0-W_q|\le2qM.
\]
This proves the first inequality in (A.3), by taking \(q=Q(f)\). The exact comparison
\[
\frac29<\left(\frac{33}{70}\right)^2
\quad\text{since}\quad 9800<9801
\]
gives \((1-2\sqrt2/3)/2>1/35\), proving the second inequality. The reciprocal of the sharper coefficient is \(18+12\sqrt2<35\).

The same calculation works at any error \(0\leq\epsilon<1/2\). Define \(Q_\epsilon\) using that error and the same query cap. Replacing the endpoint probabilities by \(\epsilon\) and \(1-\epsilon\) gives
\[
Q_\epsilon(f)\geq
\frac{1-2\sqrt{\epsilon(1-\epsilon)}}2
\frac{\|\Gamma\|}{\max_i\|\Gamma_i\|}.
\]
The spectral adversary method is attributed to Barnum, Saks and Szegedy by both inspected adversary sources; the original BSS full text was not supplied or inspected. [Høyer, Lee and Špalek's author PDF, Definition 1 and Theorem 1, printed p. 3][HLS2007], states this coefficient. The numerical coefficient printed in [Špalek–Szegedy's publisher edition, Theorem 3.1 and equation (3.1), printed p. 6][SS2006], requires the qualification below. The arbitrary-error statement here is an ordinary deduction from the displayed argument; the project exports the fixed-error specialization.
<!-- /passage:R3-A-ADVERSARY -->

<a id="R3-A-PARITY-PREFACTOR"></a>
<!-- passage:R3-A-PARITY-PREFACTOR -->
**The prefactor can be checked on two bits.** For \(f(x_0,x_1)=x_0\oplus x_1\), put \(|-\rangle=(|0\rangle-|1\rangle)/\sqrt2\) and prepare
\[
 \frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|{-}\rangle.
\]
One ordinary bit-oracle call gives
\[
 \frac{(-1)^{x_0}|0\rangle+(-1)^{x_1}|1\rangle}{\sqrt2}
       \otimes|{-}\rangle.
\]
A Hadamard on the index register turns this into
\((-1)^{x_0}|x_0\oplus x_1\rangle\otimes|{-}\rangle\).
Measuring the index computes parity exactly with one query.

In input order \(00,01,10,11\), choose
\[
 \Gamma=
 \begin{pmatrix}
 0&1&1&0\\1&0&0&1\\1&0&0&1\\0&1&1&0
 \end{pmatrix}.
\]
An orthonormal eigenbasis is obtained by dividing the vectors
\[
(1,1,1,1),\quad(1,1,-1,-1),\quad
(1,-1,1,-1),\quad(1,-1,-1,1)
\]
by two. Their eigenvalues are \(2,0,0,-2\), and each coordinate mask is a permutation matrix consisting of two disjoint edges. Thus \(\|\Gamma\|=2\) and \(M=1\). With \(v=(1,1,1,1)/2\), the progress drops from \(W_0=2\) to \(W_1=0\): every edge joins opposite parities, whose post-query index states are orthogonal. This attains the factor two in (A.4).

The Špalek–Szegedy display, under its ordinary bit-oracle convention in §2.1, printed p. 4, would instead imply
\(Q_\epsilon(f)\ge(1-2\sqrt{\epsilon(1-\epsilon)})\|\Gamma\|/M\).
At \(\epsilon=1/100\), this gives
\[
 Q_{1/100}(f)\ge2-\frac{\sqrt{99}}{25}>1,
\]
contradicting the explicit exact algorithm. The strict comparison is exact since \(99<625\). Høyer–Lee–Špalek's denominator two agrees with the progress argument and this witness. This discrepancy concerns the printed prefactor; it does not contradict the equivalence of adversary formulations or the quartic asymptotic bound. A separate older annex transcription inserted an extra square root around the entire denominator. Removing that transcription error does not restore the missing factor two. No author-confirmed erratum is claimed. Neither the sharper progress coefficient nor \(1/35\) is asserted to be the optimal constant over all possible lower-bound arguments. The [exact-arithmetic checks](../research/returns/round3/members/08_reviewed/quartic_r3_08_return/checks/) check the four input states, oracle permutation, masks, eigenbasis, output probabilities and progress drop.
<!-- /passage:R3-A-PARITY-PREFACTOR -->

### A.3. Two applications of the same adversary theorem

<a id="ROOT-BS-LAMBDA"></a>
<a id="R3-A-STAR"></a>
<!-- passage:R3-A-STAR -->
Fix an input \(x\) and pairwise disjoint sensitive blocks \(B_1,\ldots,B_b\), first with \(b\geq1\). Their flipped inputs are distinct and have value opposite to \(f(x)\). Form the star with center \(x\), these \(b\) leaves, and no other edges. Its adjacency is an admissible nonzero \(\Gamma\). On the span of the center vector and the normalized sum of leaf vectors it acts by
\[
 \begin{pmatrix}0&\sqrt b\\\sqrt b&0\end{pmatrix};
\]
it vanishes on the orthogonal complement within the leaf coordinates and on all unused vertices. Therefore \(\|\Gamma\|=\sqrt b\). When \(b=0\), the matrix is zero and this identity still holds.

A coordinate belongs to at most one of the disjoint blocks, so its mask keeps at most one undirected star edge and has norm at most one. For \(b\ge1\), (A.3) gives \(\sqrt b\le35Q(f)\); the conclusion is automatic at \(b=0\). Taking the maximum over sensitive families and inputs gives
\[
 \operatorname{bs}(f)\le1225Q(f)^2.
\tag{A.5}
\]
The disjointness condition is essential to the unit mask bound. A family of overlapping blocks can leave several edges in the same mask.
<!-- /passage:R3-A-STAR -->

<a id="R3-A-SPECTRAL"></a>
<!-- passage:R3-A-SPECTRAL -->
Now take \(\Gamma=S_f\). For each coordinate, its sensitive edges form a partial matching: each input has only one neighbor obtained by flipping that coordinate. The masked matrix is a direct sum of matrices \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) and zeros, so its norm is at most one. If \(f\) is nonconstant, a path in the cube between opposite-output inputs contains a sensitive edge, so \(S_f\ne0\). Applying (A.3) gives
\[
 \lambda(f)\le35Q(f).
\tag{A.6}
\]
For a constant function, \(S_f=0\) and (A.6) is immediate. This is the sensitivity-graph application in [ABKRT, arXiv v1, Lemma 9, printed p. 8][ABKRT2020]; (A.5) and (A.6) are the two conclusions of OpenAI's Lemma A.3.
<!-- /passage:R3-A-SPECTRAL -->

### A.4. A maximum-degree face and Huang's signed cube

<a id="ROOT-HUANG-RESTRICTION"></a>
<a id="R3-A-FACE"></a>
<!-- passage:R3-A-FACE -->
We prove
\[
 \deg(f)\le\lambda(f)^2.
\tag{A.7}
\]
The assertion is immediate for constants. Otherwise write inputs and outputs as signs, and put \(d=\deg(f)\ge1\). Choose a nonzero monomial with support \(S\) of size \(d\). Fix every coordinate outside \(S\) to any signs. A term contributing to the full \(S\)-coefficient after restriction must originally contain \(S\); maximal degree excludes a nonzero coefficient on a strict superset. Thus the top coefficient survives unchanged for every outside assignment.

Let \(g:\{-1,1\}^d\to\{-1,1\}\) be one such restricted function. Products of distinct sign coordinates are orthogonal under uniform averaging, so its top coefficient is
\(\mathbb E[g(y)y_1\cdots y_d]\ne0\).
Choose \(\sigma\in\{-1,1\}\) making this correlation positive. Then
\[
 U=\{y:g(y)=\sigma y_1\cdots y_d\}
 \quad\hbox{satisfies}\quad |U|>2^{d-1}.
\tag{A.8}
\]
Indeed, the sign \(\sigma g(y)y_1\cdots y_d\) equals \(1\) on \(U\) and \(-1\) off \(U\); its positive mean is exactly the strict majority assertion. Every cube edge internal to \(U\) changes \(g\), because parity changes across that edge.
<!-- /passage:R3-A-FACE -->

<a id="ROOT-HUANG-SPECTRUM"></a>
<a id="R3-A-HUANG"></a>
<!-- passage:R3-A-HUANG -->
Define the signed cube adjacency by
\[
 H'_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 H'_{j+1}=\begin{pmatrix}H'_j&I\\I&-H'_j\end{pmatrix}.
\tag{A.9}
\]
It is real symmetric and its entrywise absolute value is ordinary cube adjacency. Block multiplication gives \((H'_j)^2=jI\), since the off-diagonal blocks cancel, and \(\operatorname{tr}H'_j=0\). For \(j\ge1\), its only eigenvalues are the distinct numbers \(\sqrt j\) and \(-\sqrt j\). Their multiplicities sum to \(2^j\), and trace zero makes them equal, hence each is \(2^{j-1}\). This is [Huang's signed-matrix calculation, Annals edition, Lemma 2.2, printed p. 952][Huang2019]. The condition \(j\ge1\) belongs to the multiplicity statement: with the convenient extension \(H'_0=(0)\), there is only the eigenvalue zero on a one-dimensional space.

The positive eigenspace of \(H'_d\) has dimension \(2^{d-1}\), while the subspace of vectors supported on \(U\) has dimension \(|U|>2^{d-1}\). Their dimensions sum to more than \(2^d\), so their intersection contains a nonzero real vector \(v\). Put \(u=|v|\) coordinatewise. If \(A_U\) denotes the unsigned cube adjacency induced on \(U\), extended by zero, then
\[
 u^{\mathsf T}A_Uu
 \ge v^{\mathsf T}H'_dv
 =\sqrt d\,\|v\|^2
 =\sqrt d\,\|u\|^2.
\tag{A.10}
\]
The first inequality follows term by term from \(|H'_d|=A_{\rm cube}\) and the support of \(v\). Every edge of \(A_U\) is a sensitivity edge of \(g\). Because \(u\ge0\), adding the other sensitivity edges can only increase its quadratic form. Embed \(u\) into the original cube by the selected face map and set it to zero elsewhere. The embedding preserves its norm; the quadratic form of \(S_f\) on the extended vector is the restricted sensitivity quadratic form. Therefore \(\lambda(f)\ge\sqrt d\), proving (A.7).

This is the spectral consequence of Huang's construction used in [ABKRT, arXiv v1, Theorem 1 and its §3 proof, printed pp. 6–7][ABKRT2020]. Huang also records the spectral-radius consequence after his proof of Theorem 1.1, printed p. 953. The dimension argument above supplies the needed comparison without a general interlacing theorem. The formal multiplicity proof uses a local variation: multiplying coordinates by their parity signs anticommutes with \(H'_d\), so it sends each positive-root eigenvector to a negative-root eigenvector and conversely. The square and trace identities are separately checked. The resulting eigenvector and extension argument agree with (A.8)–(A.10).
<!-- /passage:R3-A-HUANG -->

### A.5. Midrijānis's decision tree

<a id="ROOT-MONOMIAL-TREE"></a>
<a id="R3-A-MIDRIJANIS"></a>
<!-- passage:R3-A-MIDRIJANIS -->
For every total Boolean function,
\[
 D(f)\le\operatorname{bs}(f)\deg(f).
\tag{A.11}
\]
The algorithm repeatedly considers the restriction determined by the answers so far. If it is constant, it outputs that value. Otherwise it selects a maximum-degree monomial and queries every still-free variable in its support. Fixing a deterministic order for the choices gives an ordinary decision tree. Each nonconstant round queries a nonempty set of new coordinates, so it terminates.

Fix one full input \(x\), and consider a round on its execution path. Let \(S\) be the support selected in the current restriction. Fix all other still-free variables to their values in \(x\). As in A.4, the nonzero coefficient on \(S\) survives because a maximum-degree support has no nonzero strict superset. The resulting function of \(S\) is nonconstant and therefore takes a value opposite to its value at \(x|_S\). The coordinates where such an assignment differs from \(x|_S\) form a nonempty block \(B\subseteq S\).

All coordinates outside \(B\) have their values from the same original input \(x\), including the earlier query answers. Hence \(f(x^B)\ne f(x)\). Different rounds select disjoint supports, so their resulting blocks are pairwise disjoint sensitive blocks at that original \(x\). The number of rounds on this path is at most \(\operatorname{bs}(f,x)\). Restriction does not increase degree, and each round queries at most \(\deg(f)\) coordinates. Its total query count is at most \(\operatorname{bs}(f,x)\deg(f)\le\operatorname{bs}(f)\deg(f)\), proving (A.11). Constants stop immediately.

Midrijānis proves the maximal-monomial property in [Lemma 3 and the product estimate inside the proof of Theorem 4, arXiv:quant-ph/0403168v2, printed pp. 3–4][Midrijanis2004]. Theorem 4's stated conclusion is the further cubic bound in degree. Its algorithm applies the maximal-monomial lemma only to nonconstant restrictions, as above; the empty monomial of a constant function would not supply a sensitive block. Theorem 5 concerns exact quantum complexity and is not the bounded-error ingredient used here.
<!-- /passage:R3-A-MIDRIJANIS -->

### A.6. The quartic estimate and its formal routes

<a id="ROOT-QUARTIC-UPPER"></a>
<a id="R3-A-ASSEMBLY"></a>
<!-- passage:R3-A-ASSEMBLY -->
Equations (A.6) and (A.7) give \(\deg(f)\le1225Q(f)^2\). Multiplying by (A.5) in (A.11) gives
\[
 D(f)\le(1225Q(f)^2)(1225Q(f)^2)
       =1{,}500{,}625Q(f)^4.
\]
A deterministic tree is a randomized algorithm whose distribution is concentrated on that tree, so \(R(f)\le D(f)\). This proves (A.1) and supplies the admissible exponent four.

Three separate formal bounds are present in the supplied source. Their constants come from the indicated ingredients:

| Formal route | Block sensitivity | Spectral sensitivity | Quartic coefficient |
| --- | --- | --- | ---: |
| Existing complexitylib route | \(\operatorname{bs}\le16Q^2\), polynomial method | \(\lambda\le36Q\), specialized progress | \(16\cdot36^2=20736\) |
| Literal Appendix A assembly | \(\operatorname{bs}\le35^2Q^2\), star adversary | \(\lambda\le35Q\), general adversary | \(35^4=1500625\) |
| Separate hybrid | \(\operatorname{bs}\le16Q^2\), polynomial method | \(\lambda\le35Q\), general adversary | \(16\cdot35^2=19600\) |

The second route proves the intermediate general-matrix, star, actual-face and recursive-matrix statements used in this appendix. Its larger numerical constant reflects the star estimate for block sensitivity. The hybrid keeps the stronger polynomial-method estimate and is exported separately. The first route is the one used by the recorded headline proof; the other two are separately compiled alternatives. The constants distinguish implementations of known inequalities; none establishes a sharp universal constant. The coefficients in the first and third rows are read from the pinned complexitylib proof and its project wrappers; the reconstruction of (A.1) uses the fully explained second row.
<!-- /passage:R3-A-ASSEMBLY -->

<a id="R3-A-FORMAL"></a>
<!-- passage:R3-A-FORMAL -->
The reviewed source-bound native receipts record successful compilation of the ten `Paper/AppendixA*.lean` modules and a successful post-root type and allowed-axiom audit for the reviewed declarations. This supersedes the historical “unelaborated” comments retained in the source and the baseline's statements that these intermediate theorems have no formal ties. The Appendix-specific type-and-axiom audit is retained evidence from the earlier review. The current integration also performed a new root build and the named comparisons recorded in §2.8; it does not claim a new Appendix-specific type-and-axiom audit. The complete types, exact source hashes and receipt locations are in the [Appendix A correspondence](../research/returns/round3/members/08_reviewed/quartic_r3_08_return/correspondence.json).

The general bound is `QuarticQuery.Paper.appendixA_lemmaA2`; its Perron and progress assumptions are proved by its dependencies and are not extra open hypotheses. The star and sensitivity estimates are `appendixA_lemmaA3_adversary`, the actual-face spectral degree theorem is `appendixA4_paper_route`, and the Midrijānis bridge is `appendixA_lemmaA5`, all in `QuarticQuery.Paper`. The cap-level and attained-minimum quartic statements are `appendixA_D_le_of_QLe` and `appendixA_D_le_Q_pow_four`; `appendixA_theoremA1` also includes \(R\le D\). The older `QuarticQuery.D_le_Q_pow_four` proves coefficient 20736, while `QuarticQuery.Paper.appendixA_D_le_Q_pow_four_hybrid` proves 19600.

Some corpus rows deliberately combine several assertions. For example, the matrix spectrum row includes square, trace, symmetry, eigenvalue classification and multiplicities; these are supplied by several declarations, rather than by the multiplicity theorem alone. Likewise the per-query row and the final-overlap row each have separate supporting estimates. Their correspondence remains partial at a single primary declaration even though the named additional declarations have compilation evidence for the reviewed snapshot. The polynomial-definition prose includes an ordinary uniqueness proof beyond the one Fourier-degree bridge. The exact parity witness above is an ordinary mathematical and finite-computational check, with no supplied Lean theorem for its exact one-query algorithm. Comparator acceptance of the existing separation wrapper does not constitute a separate comparison of each new Appendix declaration.
<!-- /passage:R3-A-FORMAL -->

## Appendix B. Mathematical statement catalogue

<a id="ROOT-CATALOGUE-INTRO"></a>
<!-- passage:ROOT-CATALOGUE-INTRO -->
This is a reference catalogue for the argument in §§2–7 and Appendix A. It preserves all 121 original claim IDs, the exact maintained statement of each claim, and a direct link to its proof or explanation. The groups follow the mathematical dependencies. Their introductory paragraphs identify formal boundaries which would otherwise be obscured by listing many component declarations.

The exhaustive declaration inventory belongs to the [correspondence record](reasoning_record_correspondence.json): it retains every candidate tie, full available source types, ordinary premises, additional assumptions, mathematical-fidelity judgments, source hashes, and separate build, Comparator and dependency-reach evidence. The [dated review receipt](reasoning_record_review.json) identifies the exact corpus observation used for this catalogue. A source-fidelity judgment is not an execution receipt; a passing execution for one declaration does not certify its neighbours. The current observation is kept separately from the immutable [baseline catalogue](../research/returns/funnel/1_long_reasoning_record/reasoning-record.md#ROOT-CATALOGUE-INTRO) and [121-row historical audit](../research/adjudication/round3_appendix_audit.json). Historical absence claims are not carried forward as current facts.

The quotations below are the maintained ledger's literal claim text, including its plain-text notation; the linked argument gives the mathematical notation and complete reasoning. Corrections to a historical quotation, including the Bansal–Sinha-to-$L$ and Huang rows, are identified by their original and maintained hashes in the correspondence. This compact catalogue does not replace either the proofs or that full evidence record.
<!-- /passage:ROOT-CATALOGUE-INTRO -->

### B.1. Functions, budgets and separation

The first group fixes the objects quantified over in the theorem. Read §§2.1–2.8 for the promise, the common algorithm and the all-input cap. The exact function-model and separation wrappers now have source-bound mathematical-fidelity reviews. The global logarithm convention is prose: the available logarithm lemmas establish its separate numerical uses rather than one theorem asserting the entire convention. The real-power family and the floor-form headline remain distinct conjunctions, joined by the floor argument in §7.

#### def-log-convention

<a id="CAT-def-log-convention"></a>
<!-- passage:CAT-def-log-convention -->
<!-- claim:def-log-convention -->

> log means log_2, except where changing the base only changes an absolute constant. Ledger pinning: log in T (prop-3.2), r and l (eq-6) and L (eq-5) is exactly log_2.

**Argument:** [§2](#ROOT-LOGS).

<!-- /passage:CAT-def-log-convention -->

#### def-partial-query

<a id="CAT-def-partial-query"></a>
<!-- passage:CAT-def-partial-query -->
<!-- claim:def-partial-query -->

> A partial Boolean function is a pair (D,P) with D a subset of {0,1}^N and P:D->{0,1}. An algorithm computes it if it is correct, with the stated error, on every x in D; behaviour off D is unconstrained.

**Argument:** [§2.1](#ROOT-PARTIAL).

<!-- /passage:CAT-def-partial-query -->

#### def-R

<a id="CAT-def-R"></a>
<!-- passage:CAT-def-R -->
<!-- claim:def-R -->

> For a (partial) Boolean function f, R(f) is the least q such that some probability distribution on deterministic decision trees of depth at most q satisfies Pr[T(x)=f(x)] >= 2/3 for every x in dom f. The query cap holds on every branch and every coin outcome.

**Argument:** [§2.1](#ROOT-PARTIAL), [§2.2](#R3-01-CLASSICAL).

<!-- /passage:CAT-def-R -->

#### def-query-oracle

<a id="CAT-def-query-oracle"></a>
<!-- passage:CAT-def-query-oracle -->
<!-- claim:def-query-oracle -->

> For x in {0,1}^n the bit oracle is the unitary O_x|i,b,z> = |i, b xor x_i, z>, with i in [n], b a bit, z a workspace label. It is self-inverse.

**Argument:** [§2.3](#ROOT-ORACLE).

<!-- /passage:CAT-def-query-oracle -->

#### def-Q

<a id="CAT-def-Q"></a>
<!-- passage:CAT-def-Q -->
<!-- claim:def-Q -->

> Q(f) is the least q such that some quantum algorithm, with unrestricted query-free computation between uses of O_x and with at most q queries on every branch including all measurement outcomes, outputs f(x) with probability >= 2/3 for every x in dom f.

**Argument:** [§2.3](#ROOT-ORACLE), [§2.4](#R3-01-ADAPTIVE).

<!-- /passage:CAT-def-Q -->

#### eq-1

<a id="CAT-eq-1"></a>
<!-- passage:CAT-eq-1 -->
<!-- claim:eq-1 -->

> alpha_tot = inf{alpha >= 0 : exists C_alpha < infinity such that for every n >= 1 and every total f:{0,1}^n->{0,1}, R(f) <= C_alpha (1+Q(f))^alpha}.

**Argument:** [§1](#ROOT-RESULT).

<!-- /passage:CAT-eq-1 -->

#### eq-2

<a id="CAT-eq-2"></a>
<!-- passage:CAT-eq-2 -->
<!-- claim:eq-2 -->

> For fixed integer k>=2 and all sufficiently large powers of four m: Q(F_{k,m}) <= C_k sqrt(m) (log m)^{b_k} and R(F_{k,m}) >= c_k m^{2-1/k}/(log m)^2, with c_k,C_k,b_k>0 depending only on k.

**Argument:** [§1](#ROOT-RESULT), [§1.1](#ROOT-ARCHITECTURE), [§7](#ROOT-FAMILY-ASSEMBLY).

<!-- /passage:CAT-eq-2 -->

#### thm-1.1

<a id="CAT-thm-1.1"></a>
<!-- passage:CAT-thm-1.1 -->
<!-- claim:thm-1.1 -->

> alpha_tot = 4. More precisely, R(f) = O((1+Q(f))^4) for every total Boolean f, and eq-2 holds for each fixed integer k>=2.

**Argument:** [§1](#ROOT-RESULT), [§1.1](#ROOT-ARCHITECTURE), [§2.7](#ROOT-EVIDENCE-CONVENTION), [§7](#ROOT-FAMILY-ASSEMBLY), [§7.2](#ROOT-NO-SMALLER).

<!-- /passage:CAT-thm-1.1 -->

#### cor-cubic-refuted

<a id="CAT-cor-cubic-refuted"></a>
<!-- passage:CAT-cor-cubic-refuted -->
<!-- claim:cor-cubic-refuted -->

> It is false that R(f) = O(Q(f)^3) for all total Boolean f ([3, Conjecture 2]): no C satisfies R(f) <= C Q(f)^3 for all total f.

**Argument:** [§1](#ROOT-RESULT), [§7.2](#ROOT-NO-SMALLER), [§1](#R3-01-QUANTIFIERS).

<!-- /passage:CAT-cor-cubic-refuted -->

### B.2. The Forrelation supplier

Sections 3.1–3.5 construct the promise procedure and exact circuit; §§3.6–3.16 prove the randomized lower bound. The complete Lemma 2.1 wrapper and its component wrappers are available. Component facts about projection probability, threshold arithmetic and circuit size still require their surrounding definitions and translations: a partial tie to one of these rows is not automatically an exact proof of the whole prose row. The corrected Bansal–Sinha-to-$L$ statement is preserved below; its historical wording and the source-version discrepancy remain visible in the correspondence and §3.18. The ordinary sharp phase implementation costs $qk$, whereas the generic compiled route has the separately proved $2qk$ cap.

#### def-walsh-sign

<a id="CAT-def-walsh-sign"></a>
<!-- passage:CAT-def-walsh-sign -->
<!-- claim:def-walsh-sign -->

> m=4^t. H is the m x m normalized Walsh-Hadamard matrix, H_{a,b}=m^{-1/2}(-1)^{<a,b>} for a,b in {0,1}^{log_2 m}. u=m^{-1/2}(1,...,1)^T. A bit a is identified with the sign (-1)^a. For z in {+-1}^m, D_z=diag(z).

**Argument:** [§3.1](#forr_definition).

<!-- /passage:CAT-def-walsh-sign -->

#### eq-3

<a id="CAT-eq-3"></a>
<!-- passage:CAT-eq-3 -->
<!-- claim:eq-3 -->

> For z_1,...,z_k in {+-1}^m: Phi(z_1,...,z_k) = u^T D_{z_1} H D_{z_2} H ... H D_{z_k} u (k diagonals, k-1 copies of H), and delta = 2^{-5k}.

**Argument:** [§3.1](#forr_definition), [§3.18](#forr_references).

<!-- /passage:CAT-eq-3 -->

#### eq-4

<a id="CAT-eq-4"></a>
<!-- passage:CAT-eq-4 -->
<!-- claim:eq-4 -->

> P=P_{k,m} is the partial function on km bits with P=1 if Phi>=delta, P=0 if |Phi|<=delta/2, undefined otherwise. The two cases are disjoint.

**Argument:** [§3.1](#forr_definition), [§3.18](#forr_references).

<!-- /passage:CAT-eq-4 -->

#### eq-5

<a id="CAT-eq-5"></a>
<!-- passage:CAT-eq-5 -->
<!-- claim:eq-5 -->

> L = L_{k,m} = floor(m^{1-1/k}/(log_2 m)^2).

**Argument:** [§3.1](#forr_definition).

<!-- /passage:CAT-eq-5 -->

#### claim-bs-to-L

<a id="CAT-claim-bs-to-L"></a>
<!-- passage:CAT-claim-bs-to-L -->
<!-- claim:claim-bs-to-L -->

> For fixed k>=2 and the positive constant c of the Bansal-Sinha bound: for all sufficiently large powers of four m, c k^{-29} (m/log(km))^{1-1/k} > floor(m^{1-1/k}/(log_2 m)^2).

**Argument:** [§3.6](#forr_bs_translation), [§3.18](#forr_references).

<!-- /passage:CAT-claim-bs-to-L -->

#### lem-2.1.i

<a id="CAT-lem-2.1.i"></a>
<!-- passage:CAT-lem-2.1.i -->
<!-- claim:lem-2.1.i -->

> For fixed k>=2 and all sufficiently large powers of four m, R(P_{k,m})>L with L as in eq-5.

**Argument:** [§3.15](#forr_threshold), [§3.16](#forr_attribution), [§3.17](#forr_bundle), [§3.18](#forr_references).

<!-- /passage:CAT-lem-2.1.i -->

#### claim-proj-prob

<a id="CAT-claim-proj-prob"></a>
<!-- passage:CAT-claim-proj-prob -->
<!-- claim:claim-proj-prob -->

> Prepare u, apply D_{z_1} H ... H D_{z_k} right to left, measure the projection onto u. Each D uses one bit query (phase kickback), H and the projection use none. Success probability is exactly Phi^2: >=delta^2 on 1-inputs, <=delta^2/4 on 0-inputs.

**Argument:** [§3.3](#forr_quantum).

<!-- /passage:CAT-claim-proj-prob -->

#### lem-2.1.ii

<a id="CAT-lem-2.1.ii"></a>
<!-- passage:CAT-lem-2.1.ii -->
<!-- claim:lem-2.1.ii -->

> For every 0<eta<1/2 there is a quantum algorithm using O_k(1+log(1/eta)) bit queries that outputs P_{k,m}(z) with error <=eta for every z in dom P. It has a coherent implementation retaining all workspace. On every input, promised or not, measuring its output register yields a bit.

**Argument:** [§3.3](#forr_quantum), [§3.17](#forr_bundle), [§5.3](#upper-decode), [§5.3](#upper-decode-cost), [§3.3](#forr_coherent).

<!-- /passage:CAT-lem-2.1.ii -->

#### claim-N-phi

<a id="CAT-claim-N-phi"></a>
<!-- passage:CAT-claim-N-phi -->
<!-- claim:claim-N-phi -->

> With W=sqrt(m) H (entries +-1), N = z_1^T W D_{z_2} W ... W D_{z_k} (1,...,1)^T is an integer, Phi=N/M_{k,m}, and M_{k,m}=m (sqrt m)^{k-1} is a positive integer because m is a power of four.

**Argument:** [§3.2](#forr_integer).

<!-- /passage:CAT-claim-N-phi -->

#### claim-integer-tests

<a id="CAT-claim-integer-tests"></a>
<!-- passage:CAT-claim-integer-tests -->
<!-- claim:claim-integer-tests -->

> Phi>=delta iff 2^{5k} N >= M_{k,m}; and |Phi|<=delta/2 iff 2^{5k+1}|N| <= M_{k,m}. d is the disjunction, b the first comparison.

**Argument:** [§3.2](#forr_integer).

<!-- /passage:CAT-claim-integer-tests -->

#### claim-circuit-size

<a id="CAT-claim-circuit-size"></a>
<!-- passage:CAT-claim-circuit-size -->
<!-- claim:claim-circuit-size -->

> N is computed by k-1 unnormalized Walsh-Hadamard transforms, coordinate sign changes and a final signed sum. Each transform uses O(m log m) additions and subtractions; all intermediate integers have absolute value at most m^{O(k)}, so O_k(log m) bits suffice; hence Boolean size O_k(m (log m)^2).

**Argument:** [§3.4](#forr_circuit).

<!-- /passage:CAT-claim-circuit-size -->

#### lem-2.1.iii

<a id="CAT-lem-2.1.iii"></a>
<!-- passage:CAT-lem-2.1.iii -->
<!-- claim:lem-2.1.iii -->

> There is a Boolean circuit C=C_{k,m} of fan-in at most two and size S=S_{k,m}=O_k(m (log m)^2), counting non-input gates, with output bits d,b such that for every input z: d=1 iff P_{k,m} is defined at z, and d=1 implies b=P_{k,m}(z). The circuit computes these outputs exactly on every input.

**Argument:** [§3.4](#forr_circuit), [§3.17](#forr_bundle), [§3.4](#forr_circuit_size).

<!-- /passage:CAT-lem-2.1.iii -->

#### lem-2.1

<a id="CAT-lem-2.1"></a>
<!-- passage:CAT-lem-2.1 -->
<!-- claim:lem-2.1 -->

> Conjunction of lem-2.1.i, lem-2.1.ii and lem-2.1.iii for each fixed k>=2.

**Argument:** [§3.17](#forr_bundle), [§3.18](#forr_references).

<!-- /passage:CAT-lem-2.1 -->

### B.3. The addressed total function

Section 4 constructs one total function from a circuit and explains every local test. The complete support wrapper `construction_lemma_2_2_with_support` conjoins physical-coordinate essentiality with the test count, exact evaluation, decision-tree bound and arbitrary-index coherent access. The printed Lemma 2.2 states the count and adaptive/coherent query clauses. Essentiality is an additional diagnostic in the expanded maintained ledger, so the new conjunction strengthens the printed lemma. The older `construction_lemma_2_2_complete` is partial relative to that expanded row, rather than deficient for omitting a support clause demanded by the original printed lemma. Layout, the addressed predicate and the test-count definition also have component ties; their complete mathematical interpretation is given by the common construction, not by a name alone. The winner-fidelity claim uses the same circuit and its correct transcript.

#### def-transcript

<a id="CAT-def-transcript"></a>
<!-- passage:CAT-def-transcript -->
<!-- claim:def-transcript -->

> For a fixed circuit, a transcript assigns a proposed bit to each non-input gate, including output gates. Input-wire values are not copied; they are read from the actual input.

**Argument:** [§4.1](#CL-transcripts).

<!-- /passage:CAT-def-transcript -->

#### eq-6

<a id="CAT-eq-6"></a>
<!-- passage:CAT-eq-6 -->
<!-- claim:eq-6 -->

> r = ceil(20 log_2 m), l = log_2 m.

**Argument:** [§4.2](#CL-layout).

<!-- /passage:CAT-eq-6 -->

#### def-column-layout

<a id="CAT-def-column-layout"></a>
<!-- passage:CAT-def-column-layout -->
<!-- claim:def-column-layout -->

> The input has m columns. Column i contains: X_i in {0,1}^m; strings A_{i,1},...,A_{i,r} in {0,1}^{km} with no promise; and for each s in {0,1}^r a cell B_{i,s} holding, for each j != i, a pointer p_{i,s,j} in [m] encoded in l bits by a fixed bijection, and for each h in [r] an alleged evaluation transcript of C_{k,m} on A_{i,h}.

**Argument:** [§4](#CL-construction-context), [§4.2](#CL-layout).

<!-- /passage:CAT-def-column-layout -->

#### def-eval-transcript

<a id="CAT-def-eval-transcript"></a>
<!-- passage:CAT-def-eval-transcript -->
<!-- claim:def-eval-transcript -->

> An evaluation transcript of C_{k,m} on A_{i,h} has one bit per non-input gate including output gates, and these gates are the count S. It is correct iff every bit equals the true value of that gate on input A_{i,h}.

**Argument:** [§4.1](#CL-transcripts).

<!-- /passage:CAT-def-eval-transcript -->

#### eq-7

<a id="CAT-eq-7"></a>
<!-- passage:CAT-eq-7 -->
<!-- claim:eq-7 -->

> If every P(A_{i,h}) is defined, the true address of column i is s_i=(P(A_{i,1}),...,P(A_{i,r})) in {0,1}^r.

**Argument:** [§4.2](#CL-address-winner).

<!-- /passage:CAT-eq-7 -->

#### eq-8

<a id="CAT-eq-8"></a>
<!-- passage:CAT-eq-8 -->
<!-- claim:eq-8 -->

> Outward pointer condition at address s: X_j[p_{i,s,j}] = 0 for every j != i. Eq. 8 of the paper is the case s=s_i.

**Argument:** [§4](#CL-construction-context), [§4.2](#CL-address-winner).

<!-- /passage:CAT-eq-8 -->

#### def-winner

<a id="CAT-def-winner"></a>
<!-- passage:CAT-def-winner -->
<!-- claim:def-winner -->

> Column i is a winner iff X_i=1^m, every P(A_{i,h}) is defined, and the cell B_{i,s_i} contains correct evaluation transcripts on all A_{i,h} and pointers satisfying eq-8.

**Argument:** [§4.2](#CL-address-winner).

<!-- /passage:CAT-def-winner -->

#### def-F

<a id="CAT-def-F"></a>
<!-- passage:CAT-def-F -->
<!-- claim:def-F -->

> F_{k,m}(y)=1 if some column of y is a winner, else 0. It is a total Boolean function on all input bit strings.

**Argument:** [§4](#CL-construction-context), [§4.2](#CL-address-winner).

<!-- /passage:CAT-def-F -->

#### cor-unique-winner

<a id="CAT-cor-unique-winner"></a>
<!-- passage:CAT-cor-unique-winner -->
<!-- claim:cor-unique-winner -->

> For every input, at most one column is a winner.

**Argument:** [§4.2](#CL-unique).

<!-- /passage:CAT-cor-unique-winner -->

#### def-win-at-address

<a id="CAT-def-win-at-address"></a>
<!-- passage:CAT-def-win-at-address -->
<!-- claim:def-win-at-address -->

> WinsAt(y,i,s) holds iff X_i=1^m, for every h the transcript in B_{i,s} on A_{i,h} is correct with outputs d=1 and b=s_h, and eq-8 holds at s. The paper's wording, i is a winner and s=s_i, is equivalent by claim-winner-fidelity.

**Argument:** [§4.2](#CL-fidelity).

<!-- /passage:CAT-def-win-at-address -->

#### def-K

<a id="CAT-def-K"></a>
<!-- passage:CAT-def-K -->
<!-- claim:def-K -->

> K_{k,m} = m + (m-1) + r(S_{k,m}+2) = O_k(m (log m)^3).

**Argument:** [§4.4](#CL-local-tests), [§5.3](#upper-verifier).

<!-- /passage:CAT-def-K -->

#### lem-2.2.i

<a id="CAT-lem-2.2.i"></a>
<!-- passage:CAT-lem-2.2.i -->
<!-- claim:lem-2.2.i -->

> For every input y and (i,s) in [m] x {0,1}^r: i wins at s iff all K_{k,m} tests pass, namely (a) X_i[b]=1 for each b; (b) for each j != i, X_j[p_{i,s,j}]=0; (c) for each h and each non-input gate, the claimed value equals the gate function of its predecessors, read from the transcript or from A_{i,h}; (d) for each h, claimed d=1 and claimed b=s_h. Each test is computed by a deterministic adaptive bit-query decision tree of depth at most max(3,l+1), which is l+1 for m>=4: a pointer test reads l pointer bits, then the one target bit they select, while gate tests read at most three fixed bits. A pointer test is not a function of a small fixed set of bits: it can depend on all l+m pointer and target coordinates.

**Argument:** [§4.4](#CL-local-tests), [§4.4](#CL-local-equivalence), [§5.3](#upper-verifier).

<!-- /passage:CAT-lem-2.2.i -->

#### lem-2.2.ii

<a id="CAT-lem-2.2.ii"></a>
<!-- passage:CAT-lem-2.2.ii -->
<!-- claim:lem-2.2.ii -->

> Each test is evaluated exactly with O(log m) bit queries, also coherently with the same bound with test indices in superposition. The number of tests and the indexing convention are the same for every (i,s).

**Argument:** [§4.4](#CL-local-tests), [§4.6](#CL-coherent-tests), [§5.3](#upper-verification-proof).

<!-- /passage:CAT-lem-2.2.ii -->

#### lem-2.2

<a id="CAT-lem-2.2"></a>
<!-- passage:CAT-lem-2.2 -->
<!-- claim:lem-2.2 -->

> Conjunction of lem-2.2.i and lem-2.2.ii.

**Argument:** [§4.6](#CL-coherent-tests).

<!-- /passage:CAT-lem-2.2 -->

#### cor-local-dichotomy

<a id="CAT-cor-local-dichotomy"></a>
<!-- passage:CAT-cor-local-dichotomy -->
<!-- claim:cor-local-dichotomy -->

> A winner has an address at which every test passes; a nonwinner has a failing test at every address.

**Argument:** [§4.4](#CL-dichotomy).

<!-- /passage:CAT-cor-local-dichotomy -->

#### claim-winner-fidelity

<a id="CAT-claim-winner-fidelity"></a>
<!-- passage:CAT-claim-winner-fidelity -->
<!-- claim:claim-winner-fidelity -->

> Given the correctness half of lem-2.1.iii: WinsAt(y,i,s) iff X_i=1^m, every P(A_{i,h}) is defined, s=s_i, the transcripts in B_{i,s} are correct, and eq-8 holds. Hence exists s, WinsAt(y,i,s) is the paper's winner condition.

**Argument:** [§4.2](#CL-fidelity).

<!-- /passage:CAT-claim-winner-fidelity -->

### B.4. Amplification and the returned state

Section 5.1 gives the state calculation and bounded fresh-trial procedure. The abstract `Proc` theorem matches the abstract amplification assertion, including its successful state and cap. The implemented upper bound uses a physical label-law theorem. Those two statements do not supply the missing identification of a designated physical output subsystem; §5.5 states that stronger target completely. Thus an exact abstract tie for Lemma 3.1 must not be read as closing the physical-state bridge. Trial parameters, mixture and recursion have separate formal suppliers.

#### def-grover-trial

<a id="CAT-def-grover-trial"></a>
<!-- passage:CAT-def-grover-trial -->
<!-- claim:def-grover-trial -->

> M = ceil(10/sqrt(gamma)). A trial picks with probability 1/2 l=0, and with probability 1/2 a uniform l in {0,...,M-1}, applies l Grover iterations to A|0>, and measures the success bit. The procedure runs ceil(log(1/eta)/log(40/31)) trials with fresh registers, stopping at the first success.

**Argument:** [§5.1](#upper-grover-trial).

<!-- /passage:CAT-def-grover-trial -->

#### claim-grover-state

<a id="CAT-claim-grover-state"></a>
<!-- passage:CAT-claim-grover-state -->
<!-- claim:claim-grover-state -->

> For 0<p<1 write A|0>=sin(theta)|g>+cos(theta)|b>, 0<theta<pi/2, with g,b normalized in the successful and unsuccessful subspaces. After l Grover iterations the state is sin((2l+1)theta)|g>+cos((2l+1)theta)|b>. Hence measuring success yields |g> up to global phase, independently of l.

**Argument:** [§5.1](#upper-grover-geometry).

<!-- /passage:CAT-claim-grover-state -->

#### claim-sin2theta

<a id="CAT-claim-sin2theta"></a>
<!-- passage:CAT-claim-sin2theta -->
<!-- claim:claim-sin2theta -->

> If gamma<=p<=1/2 then sin(2theta)=2 sqrt(p(1-p)) >= sqrt(gamma).

**Argument:** [§5.1](#upper-small-probability).

<!-- /passage:CAT-claim-sin2theta -->

#### eq-9

<a id="CAT-eq-9"></a>
<!-- passage:CAT-eq-9 -->
<!-- claim:eq-9 -->

> If gamma<=p<=1/2 and M=ceil(10/sqrt(gamma)), then (1/M) sum_{l=0}^{M-1} sin^2((2l+1)theta) >= 1/2 - 1/(2M|sin 2theta|) >= 9/20.

**Argument:** [§5.1](#upper-average-exact), [§5.1](#upper-small-probability).

<!-- /passage:CAT-eq-9 -->

#### lem-3.1

<a id="CAT-lem-3.1"></a>
<!-- passage:CAT-lem-3.1 -->
<!-- claim:lem-3.1 -->

> For 0<gamma<=1/2 and 0<eta<1/2 there is a single procedure, black-box in A and A^{-1} and with call counts depending only on gamma and eta, using O(gamma^{-1/2} log(1/eta)) calls for every p and on every branch, such that for every state preparation A with a success bit, success probability p and, if p>0, normalized successful state |g>: it reports failure or produces a successful outcome; conditional on success the output is |g> up to global phase; if p>=gamma, failure probability <=eta; if p=0 it always reports failure.

**Argument:** [§5.1](#upper-amplification-statement), [§5.1](#upper-amplification-proof).

<!-- /passage:CAT-lem-3.1 -->

### B.5. Tournament sampling

The matrix inequalities lead to the ideal process and its shrinking expected weight in §5.2. The implemented sampler must then be related to that process. The literal tensor equation and the finite bounded-list theorem are now explicit declarations. Some component rows about the sampler, coupling and cost retain partial ties because each row combines a construction or interpretation with an estimate. The list theorem supplies one common witness and the complete list-law conclusion; it does not assert equality of every retained tensor state in the alternative measured route.

#### def-aij

<a id="CAT-def-aij"></a>
<!-- passage:CAT-def-aij -->
<!-- claim:def-aij -->

> For a fixed oracle input and a coherent comparison circuit, a_{ij} is the probability that i is reported as defeating j when the result is measured, using one circuit per unordered pair; a_{ii}=0.

**Argument:** [§5.2](#upper-comparison-model).

<!-- /passage:CAT-def-aij -->

#### eq-10

<a id="CAT-eq-10"></a>
<!-- passage:CAT-eq-10 -->
<!-- claim:eq-10 -->

> a_{ij}+a_{ji}=1 for i != j, and a_{ii}=0.

**Argument:** [§5.2](#upper-comparison-model), [§5.3](#upper-comparison-law).

<!-- /passage:CAT-eq-10 -->

#### def-T-eps

<a id="CAT-def-T-eps"></a>
<!-- passage:CAT-def-T-eps -->
<!-- claim:def-T-eps -->

> For m>=2: T=ceil(log_2(1000m)), epsilon=1/(1000T).

**Argument:** [§5.2](#upper-tournament-parameters).

<!-- /passage:CAT-def-T-eps -->

#### eq-11

<a id="CAT-eq-11"></a>
<!-- passage:CAT-eq-11 -->
<!-- claim:eq-11 -->

> i_* is dominant if a_{i_* j} >= 1-epsilon for every j != i_*.

**Argument:** [§5.2](#upper-tournament-parameters).

<!-- /passage:CAT-eq-11 -->

#### def-ideal-process

<a id="CAT-def-ideal-process"></a>
<!-- passage:CAT-def-ideal-process -->
<!-- claim:def-ideal-process -->

> Ideal process: w_i=1 for all i, W=sum_i w_i. While W>0 sample p with probability w_p/W, append p to the list, update by eq-12. If W=0, leave list and weights unchanged. Run T steps.

**Argument:** [§5.2](#upper-ideal-process).

<!-- /passage:CAT-def-ideal-process -->

#### eq-12

<a id="CAT-eq-12"></a>
<!-- passage:CAT-eq-12 -->
<!-- claim:eq-12 -->

> Update w_i <- w_i a_{ip} for all i in [m].

**Argument:** [§5.2](#upper-ideal-process).

<!-- /passage:CAT-eq-12 -->

#### eq-13

<a id="CAT-eq-13"></a>
<!-- passage:CAT-eq-13 -->
<!-- claim:eq-13 -->

> For W>0: E[W_new | w] = (1/W) sum_{p,i} w_p w_i a_{ip} = (W^2 - sum_i w_i^2)/(2W) <= W/2.

**Argument:** [§5.2](#upper-weight-drift).

<!-- /passage:CAT-eq-13 -->

#### claim-expected-WT

<a id="CAT-claim-expected-WT"></a>
<!-- passage:CAT-claim-expected-WT -->
<!-- claim:claim-expected-WT -->

> The bound of eq-13 also holds when W=0, hence E[W_T] <= m/2^T.

**Argument:** [§5.2](#upper-weight-drift).

<!-- /passage:CAT-claim-expected-WT -->

#### claim-weight-lb

<a id="CAT-claim-weight-lb"></a>
<!-- passage:CAT-claim-weight-lb -->
<!-- claim:claim-weight-lb -->

> If i_* satisfies eq-11 and has not been selected in t<=T steps, then w_{i_*} >= (1-epsilon)^t >= 1-T epsilon > 1/2. Hence W>0 until it is selected.

**Argument:** [§5.2](#upper-dominant-weight).

<!-- /passage:CAT-claim-weight-lb -->

#### eq-14

<a id="CAT-eq-14"></a>
<!-- passage:CAT-eq-14 -->
<!-- claim:eq-14 -->

> Pr[i_* absent from the ideal list] <= Pr[W_T >= 1/2] <= 2m/2^T.

**Argument:** [§5.2](#upper-dominant-weight).

<!-- /passage:CAT-eq-14 -->

#### construct-sampler

<a id="CAT-construct-sampler"></a>
<!-- passage:CAT-construct-sampler -->
<!-- claim:construct-sampler -->

> Given pivots p_1,...,p_t with t<T: prepare uniform |i> over [m], compare i with each pivot in a fresh workspace, set the success bit iff every comparison says i defeats its pivot, keeping all garbage. Apply lem-3.1 with gamma=1/(2m), eta=epsilon. On failure stop and return the accumulated list; otherwise measure the index, append, and continue for at most T stages.

**Argument:** [§5.2](#upper-stage-state), [§5.2](#upper-quantum-tournament).

<!-- /passage:CAT-construct-sampler -->

#### eq-15

<a id="CAT-eq-15"></a>
<!-- passage:CAT-eq-15 -->
<!-- claim:eq-15 -->

> Pre-success state: m^{-1/2} sum_{i=1}^m |i> tensor_{b=1}^t |phi(i,p_b)>.

**Argument:** [§5.2](#upper-stage-state), [§5.2](#upper-tournament-evidence).

<!-- /passage:CAT-eq-15 -->

#### claim-success-prob

<a id="CAT-claim-success-prob"></a>
<!-- passage:CAT-claim-success-prob -->
<!-- claim:claim-success-prob -->

> Conditional on index i the success probability is prod_{b=1}^t a_{i p_b} = w_i (empty product 1). Total success probability is W/m, and conditional on success the index has law w_i/W exactly.

**Argument:** [§5.2](#upper-stage-law), [§5.2](#upper-tournament-evidence).

<!-- /passage:CAT-claim-success-prob -->

#### claim-coupling

<a id="CAT-claim-coupling"></a>
<!-- passage:CAT-claim-coupling -->
<!-- claim:claim-coupling -->

> Until i_* is first selected, W/m >= 1/(2m), so at each such history the sampler fails with probability <=epsilon and otherwise follows the exact ideal pivot law. The real list contains i_* except with probability <= 2m/2^T + T epsilon.

**Argument:** [§5.2](#upper-coupling), [§5.2](#upper-tournament-evidence), [§5.2](#upper-continuation-induction).

<!-- /passage:CAT-claim-coupling -->

#### claim-tournament-cost

<a id="CAT-claim-tournament-cost"></a>
<!-- passage:CAT-claim-tournament-cost -->
<!-- claim:claim-tournament-cost -->

> Stage t uses O(c(t+1)) queries per call; lem-3.1 uses O(sqrt(m) log(1/epsilon)) calls; the sum over t<T is O(c sqrt(m) T^2 log T), a fixed cap on every branch.

**Argument:** [§5.2](#upper-tournament-cost), [§5.4](#upper-finite-budget).

<!-- /passage:CAT-claim-tournament-cost -->

#### prop-3.2

<a id="CAT-prop-3.2"></a>
<!-- passage:CAT-prop-3.2 -->
<!-- claim:prop-3.2 -->

> Let m>=2, T=ceil(log_2(1000m)), epsilon=1/(1000T). For a coherent comparison circuit controlled by two candidate indices, reversible with all workspace retained, using at most c>=1 bit queries, with probabilities a_{ij} satisfying eq-10, there is a quantum algorithm making O(c sqrt(m) T^2 log T) queries on every branch and returning a list of at most T candidates such that, for every fixed oracle input and every i_* satisfying eq-11, the list contains i_* with probability >= 1-2m/2^T-T epsilon.

**Argument:** [§5](#upper-purpose), [§5.2](#upper-comparison-model), [§5.2](#upper-tournament-cost), [§5.2](#upper-tournament-evidence).

<!-- /passage:CAT-prop-3.2 -->

### B.6. Decoding and verification

Sections 5.3–5.4 put decoding, tournament comparison and verification into one algorithm and bound its actual cap. Several source rows describe complete procedures or their state interpretation, while their named ties expose only particular laws or numerical bounds. These partial component correspondences are compatible with the complete final quantum upper endpoint. Promise correctness and all-input budget control have different domains and are retained separately in the ordinary argument and the formal witnesses.

#### def-decode

<a id="CAT-def-decode"></a>
<!-- passage:CAT-def-decode -->
<!-- claim:def-decode -->

> decode(i): run the algorithm of lem-2.1.ii on each A_{i,h}, h in [r], with error <= epsilon/r, retaining workspace. Output a string in {0,1}^r on every input.

**Argument:** [§5.3](#upper-decode).

<!-- /passage:CAT-def-decode -->

#### claim-decode-cost

<a id="CAT-claim-decode-cost"></a>
<!-- passage:CAT-claim-decode-cost -->
<!-- claim:claim-decode-cost -->

> decode uses O_k(r log(r/epsilon)) = (log m)^{O_k(1)} queries. If all r instances are defined, the address is correct with probability >=1-epsilon. Otherwise it still returns some address.

**Argument:** [§5.3](#upper-decode-cost).

<!-- /passage:CAT-claim-decode-cost -->

#### def-comparison

<a id="CAT-def-comparison"></a>
<!-- passage:CAT-def-comparison -->
<!-- claim:def-comparison -->

> Comparison of distinct columns, in sorted order: decode each in separate workspaces; read each column's pointer towards the other at its decoded address and inspect the pointed bit of the other's X string. A column disqualifies its opponent if that bit is 0. If exactly one disqualifies the other it is victorious, otherwise the smaller index. A self-comparison returns false without reading a pointer.

**Argument:** [§5.3](#upper-comparator).

<!-- /passage:CAT-def-comparison -->

#### claim-comparison-state

<a id="CAT-claim-comparison-state"></a>
<!-- passage:CAT-claim-comparison-state -->
<!-- claim:claim-comparison-state -->

> The comparison uses c=(log m)^{O_k(1)} queries; its reversal costs the same. Measurement probabilities agree with the classical description, since later operations are controlled on the decoded registers in the computational basis. The resulting a_{ij} satisfy eq-10.

**Argument:** [§5.3](#upper-comparator), [§5.3](#upper-comparison-law).

<!-- /passage:CAT-claim-comparison-state -->

#### claim-winner-dominates

<a id="CAT-claim-winner-dominates"></a>
<!-- passage:CAT-claim-winner-dominates -->
<!-- claim:claim-winner-dominates -->

> If i_* is a winner then for every j != i_*, a_{i_* j} >= 1-epsilon, on every input, whether or not the opponent's instances are defined.

**Argument:** [§5.3](#upper-winner-dominates).

<!-- /passage:CAT-claim-winner-dominates -->

#### def-verify

<a id="CAT-def-verify"></a>
<!-- passage:CAT-def-verify -->
<!-- claim:def-verify -->

> verify(i): decode and measure an address s afresh. Let A prepare a uniform test index and an exact failing-test flag at (i,s), with K tests. Apply lem-3.1 with gamma=1/K and eta=epsilon. Reject if a failed test is found, otherwise accept. Output 1 iff some listed candidate is accepted.

**Argument:** [§5.3](#upper-verifier).

<!-- /passage:CAT-def-verify -->

#### claim-verify

<a id="CAT-claim-verify"></a>
<!-- passage:CAT-claim-verify -->
<!-- claim:claim-verify -->

> A non-winner is accepted with probability <=epsilon, at every address. A true winner is rejected with probability <=epsilon, only by decoding error. Verification costs O(sqrt(K) log(1/epsilon) log m) = sqrt(m)(log m)^{O_k(1)} queries for the search, plus decoding.

**Argument:** [§5.3](#upper-verification-proof).

<!-- /passage:CAT-claim-verify -->

#### claim-error

<a id="CAT-claim-error"></a>
<!-- passage:CAT-claim-error -->
<!-- claim:claim-error -->

> On a 0-input the error is at most T epsilon. On a 1-input it is at most 2m/2^T + T epsilon + epsilon < 1/3.

**Argument:** [§5.2](#upper-continuation-induction), [§5.3](#upper-total-error).

<!-- /passage:CAT-claim-error -->

#### claim-coherent-access

<a id="CAT-claim-coherent-access"></a>
<!-- passage:CAT-claim-coherent-access -->
<!-- claim:claim-coherent-access -->

> All superposed array accesses are ordinary bit queries. The global bit index is computed reversibly; a pointer is read in O(log m) queries; a controlled query uses load, use, unload, two queries.

**Argument:** [§5.4](#upper-oracle-access), [§5.4](#upper-read-compiler).

<!-- /passage:CAT-claim-coherent-access -->

#### prop-3.3

<a id="CAT-prop-3.3"></a>
<!-- passage:CAT-prop-3.3 -->
<!-- claim:prop-3.3 -->

> For every fixed k>=2, Q(F_{k,m}) <= sqrt(m) (log m)^{O_k(1)}.

**Argument:** [§5](#upper-purpose), [§5.4](#upper-finite-budget), [§5.4](#upper-asymptotic-bound), [§5.4](#upper-explicit-log6).

<!-- /passage:CAT-prop-3.3 -->

### B.7. Direct product and independent information

Section 6.1 gives both the conditional-transcript argument and the unnormalized-mass induction. The product law and terminal estimates have exact suppliers, while the value function, one-step calculation and supermartingale rows require several components. In particular, equation (16) includes both the queried factor and the unchanged factors. The available direct-product and address-guess declarations quantify finite seed spaces. The rows below allow arbitrary independent information: their ordinary reduction to a finite distribution on bounded-depth behaviours is supplied in §6.1, but no formal pushforward theorem identifying those two interfaces is asserted.

#### claim-product-law

<a id="CAT-claim-product-law"></a>
<!-- passage:CAT-claim-product-law -->
<!-- claim:claim-product-law -->

> For a deterministic algorithm, at every transcript tau of positive probability, the conditional law of (U_1,...,U_r) given tau is a product of separate conditional laws, because the event of obtaining tau is a Cartesian product of constraints on each input.

**Argument:** [§6.1](#CL-product-law).

<!-- /passage:CAT-claim-product-law -->

#### def-value-V

<a id="CAT-def-value-V"></a>
<!-- passage:CAT-def-value-V -->
<!-- claim:def-value-V -->

> With q_h queries already made to U_h, V_h(tau) is the largest success probability for computing P(U_h) under its conditional law given tau using at most L-q_h further queries.

**Argument:** [§6.1](#CL-conditional-values).

<!-- /passage:CAT-def-value-V -->

#### eq-16

<a id="CAT-eq-16"></a>
<!-- passage:CAT-eq-16 -->
<!-- claim:eq-16 -->

> If the next query at tau addresses U_h then E[V_h(tau') | tau] <= V_h(tau). The conditional laws and budgets of the other inputs do not change.

**Argument:** [§6.1](#CL-conditional-values).

<!-- /passage:CAT-eq-16 -->

#### claim-supermartingale

<a id="CAT-claim-supermartingale"></a>
<!-- passage:CAT-claim-supermartingale -->
<!-- claim:claim-supermartingale -->

> E[prod_j V_j(tau') | tau] <= prod_j V_j(tau). The product is a supermartingale over at most rL queries.

**Argument:** [§6.1](#CL-supermartingale).

<!-- /passage:CAT-claim-supermartingale -->

#### claim-final-bound

<a id="CAT-claim-final-bound"></a>
<!-- passage:CAT-claim-final-bound -->
<!-- claim:claim-final-bound -->

> At the final transcript tau, Pr[chosen vector correct | tau] <= prod_h max_b Pr(P(U_h)=b | tau) <= prod_h V_h(tau).

**Argument:** [§6.1](#CL-supermartingale).

<!-- /passage:CAT-claim-final-bound -->

#### lem-4.1

<a id="CAT-lem-4.1"></a>
<!-- passage:CAT-lem-4.1 -->
<!-- claim:lem-4.1 -->

> Let P:D->{0,1}, D subset {0,1}^n, mu a distribution on D, L a nonnegative integer. Suppose every deterministic algorithm making at most L queries computes P under mu with success probability <=beta. If U_1,...,U_r are iid mu, every classical algorithm making at most L queries to each U_h, possibly randomized, adaptive among the r inputs, and given arbitrary additional information independent of (U_1,...,U_r), outputs (P(U_1),...,P(U_r)) with probability <=beta^r.

**Argument:** [§6.1](#CL-direct-product-statement), [§6.1](#CL-supermartingale), [§6.1](#CL-weighted-values), [§6.1](#CL-weighted-product), [§6.1](#CL-independent-information).

<!-- /passage:CAT-lem-4.1 -->

#### claim-minimax-mu

<a id="CAT-claim-minimax-mu"></a>
<!-- passage:CAT-claim-minimax-mu -->
<!-- claim:claim-minimax-mu -->

> If L<R(P), there is a distribution mu on dom P, which is in particular nonempty, such that every deterministic tree of depth <=L has success probability <=2/3 under mu.

**Argument:** [§6.2](#CL-minimax).

<!-- /passage:CAT-claim-minimax-mu -->

#### claim-address-guess

<a id="CAT-claim-address-guess"></a>
<!-- passage:CAT-claim-address-guess -->
<!-- claim:claim-address-guess -->

> Under mu from claim-minimax-mu, for U_1,...,U_r iid mu, every classical algorithm making at most L queries to each U_h, given information independent of (U_1,...,U_r), outputs (P(U_1),...,P(U_r)) with probability <=(2/3)^r.

**Argument:** [§6.2](#CL-address-guess).

<!-- /passage:CAT-claim-address-guess -->

### B.8. Planting, discoveries and truncation

Sections 6.2–6.7 prove the planted lower bound. The complete equality-and-bound row (19) needs a conjunction theorem; a stronger probability inequality alone does not cover its equality clause. The independently uniform column is essential to that equality, as the finite selection example shows. The early/late proof of $\mathbb E Z$ and the stronger alternative search proof remain different arguments; formal support for the alternative estimate does not formalize the early/late decomposition. Likewise, the planted-average definition accepts a transcript chooser, so correctness of that transcript is an additional separately proved property. The arbitrary independent information in the address guess has the finite-seed boundary described in B.7. Signed and absolute-gap versions are distinguished in the entries and their correspondence.

#### eq-17

<a id="CAT-eq-17"></a>
<!-- passage:CAT-eq-17 -->
<!-- claim:eq-17 -->

> G = floor(mL/100).

**Argument:** [§6.3](#CL-generic-statement).

<!-- /passage:CAT-eq-17 -->

#### def-dummy

<a id="CAT-def-dummy"></a>
<!-- passage:CAT-def-dummy -->
<!-- claim:def-dummy -->

> Dummy input Y^(0): independently for each i, J_i uniform in [m], X_i has a single 0 at position J_i. All A_{i,h} are iid mu independent of the J_i. All cells B_{i,s} are one fixed blank pattern.

**Argument:** [§6.3](#CL-dummy).

<!-- /passage:CAT-def-dummy -->

#### def-planted

<a id="CAT-def-planted"></a>
<!-- passage:CAT-def-planted -->
<!-- claim:def-planted -->

> I is uniform in [m] and independent of Y^(0). Y^(1) is Y^(0) with X_I:=1^m and B_{I,s_I} filled with the correct transcripts and pointers p_{I,s_I,j}=J_j for j != I.

**Argument:** [§6.3](#CL-planted).

<!-- /passage:CAT-def-planted -->

#### claim-Y-values

<a id="CAT-claim-Y-values"></a>
<!-- passage:CAT-claim-Y-values -->
<!-- claim:claim-Y-values -->

> F_{k,m}(Y^(0))=0 and F_{k,m}(Y^(1))=1 for all sample points.

**Argument:** [§6.3](#CL-planted).

<!-- /passage:CAT-claim-Y-values -->

#### eq-18

<a id="CAT-eq-18"></a>
<!-- passage:CAT-eq-18 -->
<!-- claim:eq-18 -->

> For a deterministic algorithm with at most G queries, |Pr[outputs 1 on Y^(1)]-Pr[outputs 1 on Y^(0)]| <= Pr(the dummy run queries X_I[J_I]) + Pr(the dummy run queries any bit of B_{I,s_I}).

**Argument:** [§6.3](#CL-first-difference).

<!-- /passage:CAT-eq-18 -->

#### def-Z

<a id="CAT-def-Z"></a>
<!-- passage:CAT-def-Z -->
<!-- claim:def-Z -->

> Z is the number of columns whose zero is discovered in the dummy run.

**Argument:** [§6.4](#CL-early-late), [§6.4](#CL-erased-zero-identity).

<!-- /passage:CAT-def-Z -->

#### claim-uniform-zero

<a id="CAT-claim-uniform-zero"></a>
<!-- passage:CAT-claim-uniform-zero -->
<!-- claim:claim-uniform-zero -->

> Before the zero in a column is found, its location is uniform among positions of that column not yet queried, conditional on the full adaptive transcript.

**Argument:** [§6.4](#CL-early-late).

<!-- /passage:CAT-claim-uniform-zero -->

#### claim-EZ

<a id="CAT-claim-EZ"></a>
<!-- passage:CAT-claim-EZ -->
<!-- claim:claim-EZ -->

> E Z <= 4G/m: an early discovery (fewer than m/2 distinct positions queried in that column before it) has probability <=2/m per query, giving <=2G/m in expectation; any other discovery lies in one of at most 2G/m columns receiving >=m/2 queries.

**Argument:** [§6.4](#CL-early-late).

<!-- /passage:CAT-claim-EZ -->

#### eq-19

<a id="CAT-eq-19"></a>
<!-- passage:CAT-eq-19 -->
<!-- claim:eq-19 -->

> Pr(the dummy run queries X_I[J_I]) = E Z/m <= 4G/m^2.

**Argument:** [§6.4](#CL-early-late), [§6.4](#CL-zero-worlds), [§6.4](#CL-zero-average).

<!-- /passage:CAT-eq-19 -->

#### def-heavy

<a id="CAT-def-heavy"></a>
<!-- passage:CAT-def-heavy -->
<!-- claim:def-heavy -->

> Column i is heavy if, over the entire dummy run, the algorithm makes more than L queries in total to A_{i,1},...,A_{i,r}. Repeats count.

**Argument:** [§6.5](#CL-heavy).

<!-- /passage:CAT-def-heavy -->

#### eq-20

<a id="CAT-eq-20"></a>
<!-- passage:CAT-eq-20 -->
<!-- claim:eq-20 -->

> Pr(I is heavy) <= G/(mL).

**Argument:** [§6.5](#CL-heavy).

<!-- /passage:CAT-eq-20 -->

#### def-simulator

<a id="CAT-def-simulator"></a>
<!-- passage:CAT-def-simulator -->
<!-- claim:def-simulator -->

> Fix i and t in {1,...,G}. A simulator receives all of the dummy input outside A_{i,1},...,A_{i,r}, runs the deterministic algorithm up to its proposed t-th query, and aborts before an (L+1)st query to those r strings in total. If it reaches time t and the proposed query is to a cell B_{i,s}, it outputs s; otherwise it outputs a fixed vector.

**Argument:** [§6.5](#CL-simulator).

<!-- /passage:CAT-def-simulator -->

#### eq-21

<a id="CAT-eq-21"></a>
<!-- passage:CAT-eq-21 -->
<!-- claim:eq-21 -->

> For each i and t: Pr(i is nonheavy and the t-th query is in B_{i,s_i}) <= (2/3)^r.

**Argument:** [§6.5](#CL-simulator), [§6.5](#CL-joint-event).

<!-- /passage:CAT-eq-21 -->

#### eq-22

<a id="CAT-eq-22"></a>
<!-- passage:CAT-eq-22 -->
<!-- claim:eq-22 -->

> Pr(the dummy run queries B_{I,s_I}) <= G/(mL) + G(2/3)^r.

**Argument:** [§6.5](#CL-cell-union).

<!-- /passage:CAT-eq-22 -->

#### eq-23

<a id="CAT-eq-23"></a>
<!-- passage:CAT-eq-23 -->
<!-- claim:eq-23 -->

> The output-probability difference is at most 4G/m^2 + G/(mL) + G(2/3)^r.

**Argument:** [§6.6](#CL-discrepancy).

<!-- /passage:CAT-eq-23 -->

#### claim-tail

<a id="CAT-claim-tail"></a>
<!-- passage:CAT-claim-tail -->
<!-- claim:claim-tail -->

> G(2/3)^r <= (1/100) m^{2-20 log_2(3/2)} = o(1).

**Argument:** [§6.6](#CL-tail-numeric).

<!-- /passage:CAT-claim-tail -->

#### claim-numeric

<a id="CAT-claim-numeric"></a>
<!-- passage:CAT-claim-numeric -->
<!-- claim:claim-numeric -->

> For m=4^t, r=40t, 1<=L<=m and G<=mL/100: 4G/m^2<=4/100, G/(mL)<=1/100, G(2/3)^r<=1/100, so eq-23 is at most 6/100<1/3.

**Argument:** [§6.6](#CL-tail-numeric).

<!-- /passage:CAT-claim-numeric -->

#### prop-4.2

<a id="CAT-prop-4.2"></a>
<!-- passage:CAT-prop-4.2 -->
<!-- claim:prop-4.2 -->

> For each fixed integer k>=2 and every sufficiently large power of four m, R(F_{k,m}) > G=floor(mL/100), with L=floor(m^{1-1/k}/(log_2 m)^2).

**Argument:** [§6.6](#CL-concrete-lower).

<!-- /passage:CAT-prop-4.2 -->

#### cor-R-omega

<a id="CAT-cor-R-omega"></a>
<!-- passage:CAT-cor-R-omega -->
<!-- claim:cor-R-omega -->

> For fixed k, R(F_{k,m}) = Omega_k(m^{2-1/k}/(log m)^2).

**Argument:** [§7](#ROOT-FAMILY-ASSEMBLY), [§6.6](#CL-concrete-lower).

<!-- /passage:CAT-cor-R-omega -->

#### prop-4.2-generic

<a id="CAT-prop-4.2-generic"></a>
<!-- passage:CAT-prop-4.2-generic -->
<!-- claim:prop-4.2-generic -->

> Let m=4^t with t>=1 and r=40t. Let P be a partial function on km bits with an exact circuit C (d=1 iff defined, and d=1 implies b=P), and F the total function built from (P,C). If 1<=L<=m and L<R(P), then R(F)>floor(mL/100).

**Argument:** [§6.3](#CL-generic-statement), [§6.6](#CL-randomized-contradiction).

<!-- /passage:CAT-prop-4.2-generic -->

### B.9. Passing to the exponent

Section 7 removes the floor and compares exponents for each fixed $k$. The same-family upper and lower estimates are used together. The threshold may depend on $k$; no joint growing-$k$ schedule is inferred. The no-smaller-exponent declaration and the stronger numerical suppliers have their full quantifier order recorded in the correspondence.

#### claim-floor

<a id="CAT-claim-floor"></a>
<!-- passage:CAT-claim-floor -->
<!-- claim:claim-floor -->

> For sufficiently large m, floor((m/100) floor(m^{1-1/k}/(log m)^2)) >= c_k m^{2-1/k}/(log m)^2 after decreasing c_k>0.

**Argument:** [§7](#ROOT-FAMILY-ASSEMBLY), [§6.6](#CL-floors).

<!-- /passage:CAT-claim-floor -->

#### claim-exponent-ratio

<a id="CAT-claim-exponent-ratio"></a>
<!-- passage:CAT-claim-exponent-ratio -->
<!-- claim:claim-exponent-ratio -->

> For fixed 0<=alpha<4 and integer k>=2 with 2-1/k>alpha/2: R(F_{k,m})/(1+Q(F_{k,m}))^alpha >= c_{k,alpha} m^{2-1/k-alpha/2}/(log m)^{2+alpha b_k}, which tends to infinity.

**Argument:** [§7.1](#ROOT-RATIO), [§1](#R3-01-QUANTIFIERS).

<!-- /passage:CAT-claim-exponent-ratio -->

#### claim-no-smaller-exponent

<a id="CAT-claim-no-smaller-exponent"></a>
<!-- passage:CAT-claim-no-smaller-exponent -->
<!-- claim:claim-no-smaller-exponent -->

> For every 0<=alpha<4, alpha does not belong to the set in eq-1, because a suitable k exists with k > 1/(2-alpha/2).

**Argument:** [§7.2](#ROOT-NO-SMALLER).

<!-- /passage:CAT-claim-no-smaller-exponent -->

### B.10. The universal upper bound

Appendix A keeps the complexity-library headline constant, the literal appendix calculation and the hybrid calculation separate. Its formal ties include exact or stronger endpoints and partial correspondence for several definitions, progress estimates and rounding steps. The corrected Huang statement requires $d\ge1$ for two distinct eigenvalues with equal multiplicities; at $d=0$ the matrix is the singleton zero matrix. The printed adversary prefactor is discussed with an explicit parity witness in §A.2. No statement about a corrected convention is silently substituted for what the cited edition prints.

#### def-D

<a id="CAT-def-D"></a>
<!-- passage:CAT-def-D -->
<!-- claim:def-D -->

> D(f) is the least depth of a deterministic decision tree computing f exactly on every input.

**Argument:** [§2.1](#ROOT-PARTIAL), [§2.2](#R3-01-CLASSICAL).

<!-- /passage:CAT-def-D -->

#### def-deg

<a id="CAT-def-deg"></a>
<!-- passage:CAT-def-deg -->
<!-- claim:def-deg -->

> deg(f) is the degree of the unique real multilinear polynomial agreeing with f on the cube, with degree 0 for every constant function, including the zero function. With this convention it is unchanged by replacing input or output bits by signs.

**Argument:** [§A.1](#ROOT-DEGREE-BLOCK).

<!-- /passage:CAT-def-deg -->

#### def-bs

<a id="CAT-def-bs"></a>
<!-- passage:CAT-def-bs -->
<!-- claim:def-bs -->

> A nonempty B subset [n] is a sensitive block at x if flipping all bits of B changes f(x). bs(f) is the maximum over x of the number of pairwise disjoint sensitive blocks at x.

**Argument:** [§A.1](#ROOT-DEGREE-BLOCK).

<!-- /passage:CAT-def-bs -->

#### def-Gamma-i

<a id="CAT-def-Gamma-i"></a>
<!-- passage:CAT-def-Gamma-i -->
<!-- claim:def-Gamma-i -->

> For an input-indexed matrix Gamma, (Gamma_i)_{xy}=Gamma_{xy} 1{x_i != y_i}. Matrix norms are operator norms for the Euclidean norm.

**Argument:** [§A.2](#ROOT-ADVERSARY-PERRON).

<!-- /passage:CAT-def-Gamma-i -->

#### claim-perron

<a id="CAT-claim-perron"></a>
<!-- passage:CAT-claim-perron -->
<!-- claim:claim-perron -->

> A nonzero real symmetric entrywise nonnegative Gamma has a nonnegative unit eigenvector v of eigenvalue ||Gamma||.

**Argument:** [§A.2](#ROOT-ADVERSARY-PERRON).

<!-- /passage:CAT-claim-perron -->

#### def-adv-progress

<a id="CAT-def-adv-progress"></a>
<!-- passage:CAT-def-adv-progress -->
<!-- claim:def-adv-progress -->

> W_t = sum_{x,y} v_x v_y Gamma_{xy} <psi_x^t | psi_y^t>, where psi_x^t is the purified state after t queries on input x.

**Argument:** [§A.2](#ROOT-ADVERSARY-PROGRESS).

<!-- /passage:CAT-def-adv-progress -->

#### claim-per-query

<a id="CAT-claim-per-query"></a>
<!-- passage:CAT-claim-per-query -->
<!-- claim:claim-per-query -->

> Each query changes W by at most: |W_{t+1}-W_t| <= 2 sum_i u_i^T Gamma_i u_i <= 2 max_i ||Gamma_i||, where u_i(x)=v_x ||phi_{x,i}||.

**Argument:** [§A.2](#ROOT-ADVERSARY-PROGRESS).

<!-- /passage:CAT-claim-per-query -->

#### claim-final-overlap

<a id="CAT-claim-final-overlap"></a>
<!-- passage:CAT-claim-final-overlap -->
<!-- claim:claim-final-overlap -->

> If Pr[output 1] is <=1/3 on one state and >=2/3 on another, their overlap has absolute value <=2 sqrt(2)/3. Hence |W_final| <= (2 sqrt(2)/3)||Gamma||.

**Argument:** [§A.2](#ROOT-ADVERSARY-FINAL).

<!-- /passage:CAT-claim-final-overlap -->

#### lem-A.2

<a id="CAT-lem-A.2"></a>
<!-- passage:CAT-lem-A.2 -->
<!-- claim:lem-A.2 -->

> Let f be a nonconstant total Boolean function, Gamma a nonzero real symmetric entrywise nonnegative input-indexed matrix with Gamma_{xy}=0 whenever f(x)=f(y). Then Q(f) >= c ||Gamma|| / max_i ||Gamma_i|| for an absolute constant c>0.

**Argument:** [§A.2](#ROOT-ADVERSARY-PROGRESS), [§A.2](#ROOT-ADVERSARY-FINAL).

<!-- /passage:CAT-lem-A.2 -->

#### def-Sf

<a id="CAT-def-Sf"></a>
<!-- passage:CAT-def-Sf -->
<!-- claim:def-Sf -->

> S_f is the adjacency matrix on {0,1}^n of the graph joining inputs that differ in exactly one bit and have different f-values. lambda(f)=||S_f||.

**Argument:** [§A.3](#ROOT-BS-LAMBDA).

<!-- /passage:CAT-def-Sf -->

#### lem-A.3.bs

<a id="CAT-lem-A.3.bs"></a>
<!-- passage:CAT-lem-A.3.bs -->
<!-- claim:lem-A.3.bs -->

> For nonconstant total f, bs(f)=O(Q(f)^2).

**Argument:** [§A.3](#ROOT-BS-LAMBDA).

<!-- /passage:CAT-lem-A.3.bs -->

#### lem-A.3.lambda

<a id="CAT-lem-A.3.lambda"></a>
<!-- passage:CAT-lem-A.3.lambda -->
<!-- claim:lem-A.3.lambda -->

> For nonconstant total f, lambda(f)=O(Q(f)).

**Argument:** [§A.3](#ROOT-BS-LAMBDA).

<!-- /passage:CAT-lem-A.3.lambda -->

#### lem-A.3

<a id="CAT-lem-A.3"></a>
<!-- passage:CAT-lem-A.3 -->
<!-- claim:lem-A.3 -->

> Conjunction of lem-A.3.bs and lem-A.3.lambda.

**Argument:** [§A.3](#ROOT-BS-LAMBDA).

<!-- /passage:CAT-lem-A.3 -->

#### claim-restrict-parity

<a id="CAT-claim-restrict-parity"></a>
<!-- passage:CAT-claim-restrict-parity -->
<!-- claim:claim-restrict-parity -->

> With f in sign form and d=deg f>=1, restricting variables outside a degree-d monomial's support gives g on the d-cube with nonzero parity correlation. So for some sigma in {-1,1}, U={x:g(x)=sigma x_1...x_d} has |U|>2^{d-1}, and every cube edge inside U changes g.

**Argument:** [§A.4](#ROOT-HUANG-RESTRICTION).

<!-- /passage:CAT-claim-restrict-parity -->

#### def-huang

<a id="CAT-def-huang"></a>
<!-- passage:CAT-def-huang -->
<!-- claim:def-huang -->

> H'_1=[[0,1],[1,0]], H'_{j+1}=[[H'_j,I],[I,-H'_j]]. Its entrywise absolute value is the cube adjacency matrix.

**Argument:** [§A.4](#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-def-huang -->

#### claim-huang-spectrum

<a id="CAT-claim-huang-spectrum"></a>
<!-- passage:CAT-claim-huang-spectrum -->
<!-- claim:claim-huang-spectrum -->

> For d>=1, (H'_d)^2=dI and trace H'_d=0; H'_d has eigenvalues +-sqrt(d), each of multiplicity 2^{d-1}.

**Argument:** [§A.4](#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-claim-huang-spectrum -->

#### claim-interlace

<a id="CAT-claim-interlace"></a>
<!-- passage:CAT-claim-interlace -->
<!-- claim:claim-interlace -->

> There is a nonzero v in the sqrt(d)-eigenspace supported on U; with u=|v|, u^T A_U u >= v^T H'_d v = sqrt(d)||u||^2.

**Argument:** [§A.4](#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-claim-interlace -->

#### lem-A.4

<a id="CAT-lem-A.4"></a>
<!-- passage:CAT-lem-A.4 -->
<!-- claim:lem-A.4 -->

> Every nonconstant total Boolean f satisfies deg(f) <= lambda(f)^2.

**Argument:** [§A.4](#ROOT-HUANG-SPECTRUM).

<!-- /passage:CAT-lem-A.4 -->

#### claim-round-block

<a id="CAT-claim-round-block"></a>
<!-- passage:CAT-claim-round-block -->
<!-- claim:claim-round-block -->

> In each round of the algorithm on input x, with S the selected maximum-degree monomial's support in the current restriction, the restriction to S with all other unqueried variables set as in x is nonconstant. So some nonempty subset of S is a sensitive block at x. Blocks of different rounds are disjoint.

**Argument:** [§A.5](#ROOT-MONOMIAL-TREE).

<!-- /passage:CAT-claim-round-block -->

#### lem-A.5

<a id="CAT-lem-A.5"></a>
<!-- passage:CAT-lem-A.5 -->
<!-- claim:lem-A.5 -->

> Every total Boolean f satisfies D(f) <= bs(f) deg(f).

**Argument:** [§A.5](#ROOT-MONOMIAL-TREE).

<!-- /passage:CAT-lem-A.5 -->

#### thm-A.1

<a id="CAT-thm-A.1"></a>
<!-- passage:CAT-thm-A.1 -->
<!-- claim:thm-A.1 -->

> Every total Boolean function satisfies R(f) <= D(f) = O((1+Q(f))^4), with an absolute constant.

**Argument:** [§7.3](#ROOT-APPENDIX-INTRO), [§A.6](#ROOT-QUARTIC-UPPER).

<!-- /passage:CAT-thm-A.1 -->

## Appendix C. References and inspected editions

<a id="ROOT-REFERENCES"></a>
<!-- passage:ROOT-REFERENCES -->
The editions and theorem locators below are those assessed in the retained section returns. In-text citations distinguish a theorem used as a premise, an antecedent, a comparison and a disputed displayed step. The integration uses those source assessments; it does not claim a new full reading of every cited external work. Machine-readable records are in [reasoning_record.bib](reasoning_record.bib).

<a id="ref-OpenAI2026"></a>

- **OpenAI2026.** OpenAI. *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. 2026. [Inspected edition or source](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). Preprint dated 5 October 2026. Mathematical target throughout this record. The retained reviewed PDF has SHA-256 a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e.

<a id="ref-BDW02"></a>

- **BDW02.** Harry Buhrman and Ronald de Wolf. *Complexity Measures and Decision Tree Complexity: A Survey*. 2002. Theoretical Computer Science. 21–43. [Inspected edition or source](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf). Author PDF dated 10 October 2002; supplied PDF SHA-256 7002019660c498b652611acf5cdbe264ea9c4a139f8f4da6e82e12822e5d9122. Sections 3.1–3.3, printed pages 5–8, supply the model conventions. Section 3.2 explicitly allows biased coins, takes maximum supported depth, and uses inclusive success at least 2/3. Section 3.3 uses a fixed sequence of input-independent gates and bit queries. Standard exposition, not a proof of the new separation.

<a id="ref-DW26"></a>

- **DW26.** Ronald de Wolf. *Quantum Computing: Lecture Notes*. 2026. [Inspected edition or source](https://arxiv.org/abs/1907.09415v6). Version 6, 27 August 2026. Supplied source archive SHA-256 2ffd080924542b6de1409a1dbd73efcb85e99bc0d3cc2daac5e3eeba84ef2535. Measurement: Section 1.2.2, printed pages 4–6, and Section 2.1.2, pages 14–15. Oracle and phase query: Section 2.4, printed pages 17–18, especially printed footnote 7; Chapter 2, Exercise 10 distinguishes controlled and uncontrolled phase queries. Section 2.3 is Quantum parallelism; the earlier Section 2.3/footnote 17 locator is corrected. Official author PDF independently consulted at https://homepages.cwi.nl/~rdewolf/qcnotes.pdf.

<a id="ref-BBCMW98"></a>

- **BBCMW98.** Robert Beals and Harry Buhrman and Richard Cleve and Michele Mosca and Ronald de Wolf. *Quantum Lower Bounds by Polynomials*. 1998. [Inspected edition or source](https://arxiv.org/abs/quant-ph/9802049v3). Conference/arXiv-era version, separately identified from the journal manuscript. The supplied PDF has SHA-256 afec116657493976b70df7dcb8b174c8c0be55a9337d9e035afd5f1fc4d9cd4c. Section 3.2, PDF page 4, defines classical randomized cost using expected queries on a worst-case input; the paragraph following Proposition 6.4, PDF page 9, uses that convention for parity. The arXiv v3 metadata dates it 30 September 1998; no byte identity with a newly downloaded arXiv PDF is asserted. Author-hosted conference PDF also consulted: https://homepages.cwi.nl/~rdewolf/publ/qc/focs98.pdf.

<a id="ref-BBCMW01"></a>

- **BBCMW01.** Robert Beals and Harry Buhrman and Richard Cleve and Michele Mosca and Ronald de Wolf. *Quantum Lower Bounds by Polynomials*. 2001. Journal of the ACM. 778–797. [Inspected edition or source](https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf). Added external comparison, accessed 2 November 2026. Author-hosted journal manuscript, Section 3.2 printed page 7, uses worst-case randomized query cost; Proposition 6.4 and adjoining paragraph, printed page 17, give quantum parity cost ceil(N/2) and classical bounded-error cost N. The assessment is confined to these passages and version identity. Do not attach the older conference version's expected-cost convention to this journal edition.

<a id="ref-ABKRT2020"></a>

- **ABKRT2020.** Aaronson, Scott and Ben-David, Shalev and Kothari, Robin and Rao, Shravas and Tal, Avishay. *Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem*. 2020. [Inspected edition or source](https://arxiv.org/abs/2010.12629v1). Version 1, 23 October 2020. Theorem 1: pp. 1 and 6–7; Theorem 2 and its deduction: p. 2; Definition 7: p. 6; Lemma 9: p. 8; Conjecture 2: p. 20. Locators refer to the original PDF, not flattened extraction numbering.

<a id="ref-AA18"></a>

- **AA18.** Scott Aaronson and Andris Ambainis. *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing*. 2018. SIAM Journal on Computing. 982–1038. [Inspected edition or source](https://arxiv.org/abs/1411.5729v1). Mathematical locators refer to the inspected arXiv v1, 21 November 2014, not journal pagination: Section 1.1.3, p. 4; Section 3.2, Figure 1 and Proposition 6, pp. 13–14. Projection probability Phi squared and the separate interference probability (1+Phi)/2 must be distinguished. Journal metadata is supplied for attribution.

<a id="ref-BansalSinha2021"></a>

- **BansalSinha2021.** Nikhil Bansal and Makrand Sinha. *$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity*. 2021. Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing. 1303–1316. [Inspected edition or source](https://arxiv.org/abs/2008.07003v3). Full-version mathematical locators refer to arXiv v3, 17 November 2020: Theorem 1.3 and Corollary 1.4, p. 4; Theorems 3.1–3.4, pp. 16–17; Corollary 3.5, p. 18; Lemma 4.3, p. 19; Section 5.4, p. 38. In supplied v3 main.tex, the disputed comparison is physical line 1181; line 1184 is the later threshold.

<a id="ref-GirishTalWu2021"></a>

- **GirishTalWu2021.** Uma Girish and Avishay Tal and Kewen Wu. *Fourier Growth of Parity Decision Trees*. 2021. 36th Computational Complexity Conference (CCC 2021). 39:1–39:36. [Inspected edition or source](https://arxiv.org/abs/2103.11604v2). Mathematical locators use arXiv v2, 13 May 2021: Section 1.3, pp. 6–8, and Lemma 1.9, p. 8. In the CCC 2021 version the corresponding result is Lemma 9, p. 39:8.

<a id="ref-SherstovStorozhenkoWu2023"></a>

- **SherstovStorozhenkoWu2023.** Alexander A. Sherstov and Andrey A. Storozhenko and Pei Wu. *An Optimal Separation of Randomized and Quantum Query Complexity*. 2023. SIAM Journal on Computing. 525–567. [Inspected edition or source](https://arxiv.org/abs/2008.10223v4). Locators refer to arXiv v4, 29 January 2023: PDF Corollaries 4.14–4.15, p. 35; the real-valued proof continues p. 36. The HTML conversion calls these Corollaries 4.12–4.13. The absolute Fourier constant is unspecified.

<a id="ref-Tal2019v1"></a>

- **Tal2019v1.** Avishay Tal. *Towards Optimal Separations between Quantum and Randomized Query Complexities*. 2019. [Inspected edition or source](https://arxiv.org/abs/1912.12561v1). Version 1, 29 December 2019; published at FOCS 2020. Context only: Theorem 5.1 and Corollary 5.3, p. 13; Definition 5.5 and Lemma 5.7, p. 14.

<a id="ref-ABK2019"></a>

- **ABK2019.** Aaronson, Scott and Ben-David, Shalev and Kothari, Robin. *Separations in Query Complexity Using Cheat Sheets*. 2016. Proceedings of the 48th Annual ACM Symposium on Theory of Computing. 863–876. [Inspected edition or source](https://arxiv.org/pdf/1511.01937v2). Edition inspected: arXiv v2, 9 July 2019. Printed Section 6.1, Definitions 14–15, pp. 20–21; Section 6.2, Lemma 17, p. 22. These appear as Definitions 10–11 and Lemma 13 in the supplied environment-numbered Markdown extraction. Historical antecedent and algorithmic comparison; no theorem transfer to this multi-column construction.

<a id="ref-ABBLSS2015"></a>

- **ABBLSS2015.** Ambainis, Andris and Balodis, Kaspars and Belovs, Aleksandrs and Lee, Troy and Santha, Miklos and Smotrovs, Juris. *Separations in Query Complexity Based on Pointer Functions*. 2015. [Inspected edition or source](https://arxiv.org/pdf/1506.04719v3). Edition inspected: arXiv v3, 26 October 2015. Section 1.3, pp. 5–6; final paragraph of Use of a balanced tree, p. 6, discusses direct pointers and immediately gives the exponential-alphabet qualification. Historical comparison, not an imported bit-query theorem.

<a id="ref-BHMT2000"></a>

- **BHMT2000.** Brassard, Gilles and Høyer, Peter and Mosca, Michele and Tapp, Alain. *Quantum Amplitude Amplification and Estimation*. 2000. [Inspected edition or source](https://arxiv.org/abs/quant-ph/0005055v1). Inspected arXiv v1. Section 2, Lemma 1, printed pages 5–6, and equation (8), page 7: amplification geometry and successful component. Theorem 3, pages 8–9: expected-time unknown-success search, not the all-branch cap. Theorem 12, page 19, is amplitude estimation. Published version: Contemporary Mathematics 305 (2002), pages 53–74; locators in this record refer to v1.

<a id="ref-BBHT1996"></a>

- **BBHT1996.** Boyer, Michel and Brassard, Gilles and Høyer, Peter and Tapp, Alain. *Tight Bounds on Quantum Searching*. 1996. [Inspected edition or source](https://arxiv.org/abs/quant-ph/9605034v1). Inspected arXiv v1. Section 4, Lemma 2, printed page 3: exact average for a random number of Grover iterations. Theorem 3 and subsequent timeout discussion, page 4: unknown-number expected-time search. The fixed capped construction is proved separately in §5.1. Journal version: Fortschritte der Physik 46 (1998); its pagination is not used for these locators.

<a id="ref-DH1999"></a>

- **DH1999.** Dürr, Christoph and Høyer, Peter. *A Quantum Algorithm for Finding the Minimum*. 1999. [Inspected edition or source](https://arxiv.org/abs/quant-ph/9607014v2). Inspected revised arXiv v2; original preprint July 1996. Theorem 1 and Lemmas 1–2, pages 1–2. Historical comparison only: ordered values and rank improvement do not supply a proof for arbitrary probabilistic comparisons.

<a id="ref-HMW2003"></a>

- **HMW2003.** Høyer, Peter and Mosca, Michele and de Wolf, Ronald. *Quantum Search on Bounded-Error Inputs*. 2003. [Inspected edition or source](https://arxiv.org/abs/quant-ph/0304052v2). Inspected arXiv v2. Section 1, pages 1–3: uniform bounded-error access to fixed Boolean predicates. Section 3, pages 4–7: search construction. Section 4: AND–OR applications. Section 5, pages 8–9: imperfect-verifier generalization. Hypothesis comparison only; arbitrary loser comparisons need not satisfy the fixed-predicate correctness guarantee. Published in ICALP 2003, LNCS 2719, pages 291–299; locators here use v2.

<a id="ref-BDK2026"></a>

- **BDK2026.** Ben-David, Shalev and Kothari, Robin. *Randomized Query Complexity Can Beat Certificate Complexity*. 2026. [Inspected edition or source](https://arxiv.org/abs/2609.15063v1). Inspected arXiv v1, Section 3, Lemma 5, pages 3–5. Antecedent for candidate generation, tournament comparison and certificate checking; no theorem from this source is imported as a premise of the fractional-weight proof.

<a id="ref-MPS2023"></a>

- **MPS2023.** Mande, Nikhil S. and Paraashar, Manaswi and Saurabh, Nitin. *Randomized and Quantum Query Complexities of Finding a King in a Tournament*. 2023. 43rd IARCS Annual Conference on Foundations of Software Technology and Theoretical Computer Science (FSTTCS 2023). 30:1–30:19. [Inspected edition or source](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30). Inspected published edition. Theorem 19, Section 4, pages 30:11–30:13, including the nearby proof and Algorithm 4. Exact direction queries to a fixed tournament; contextual comparison only. The baseline's Theorem 4.4 locator does not match this edition.

<a id="ref-Drucker2012"></a>

- **Drucker2012.** Drucker, Andrew. *Improved Direct Product Theorems for Randomized Query Complexity*. 2012. Computational Complexity. 197–244. [Inspected edition or source](https://arxiv.org/abs/1005.0644v2). Assessed arXiv version 2, 9 May 2014, and supplied pinned TeX. All locators use arXiv printed pagination: Section 1.3, pp. 6–7; Lemmas 3.1–3.2, pp. 11–12; fair specialization at the end of Section 3, p. 13. Relevant passages of the earlier supplied PDF agree; complete edition identity was not established

<a id="ref-Shaltiel2001"></a>

- **Shaltiel2001.** Shaltiel, Ronen. *Towards Proving Strong Direct Product Theorems*. 2001. [Inspected edition or source](https://eccc.weizmann.ac.il/report/2001/009/). Assessed ECCC report: Section 1.1, p. 1, definitions of success/advantage and footnotes 1–2; Section 5, Definition 4 and Theorem 5, printed p. 11, and Lemma 7, p. 12. These are PDF pages 12–13. Later journal publication: Computational Complexity 12(1–2):1–22 (2003); journal-edition theorem numbering not assessed

<a id="ref-Huang2019"></a>

- **Huang2019.** Huang, Hao. *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*. 2019. Annals of Mathematics. 949–955. [Inspected edition or source](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf). Published edition inspected at Lemma 2.2, p. 952, and the proof and spectral remark for Theorem 1.1, p. 953. The supplied six-page source is instead arXiv:1907.00847v2; its corresponding locators are pp. 4–5.

<a id="ref-Midrijanis2004"></a>

- **Midrijanis2004.** Midrijānis, Gatis. *Exact quantum query complexity for total Boolean functions*. 2004. [Inspected edition or source](https://arxiv.org/abs/quant-ph/0403168v2). Version 2, 27 March 2004. Lemma 3, p. 3; proof of Theorem 4, pp. 3–4, especially its final paragraph for D(f) <= deg(f) bs(f). Theorem 5 concerns exact, not bounded-error, quantum query complexity.

<a id="ref-HLS2007"></a>

- **HLS2007.** Høyer, Peter and Lee, Troy and Špalek, Robert. *Negative weights make adversaries stronger*. 2007. [Inspected edition or source](https://www.ucw.cz/~robert/papers/madv.pdf). The inspected 29-page author PDF: Definition 1 and Theorem 1, printed p. 3. Version-2 metadata is dated 24 April 2007; byte identity of the author PDF and arXiv PDF was not established. Theorem 1 attributes the nonnegative spectral bound, including denominator two, to Barnum–Saks–Szegedy. Related conference publication: STOC 2007, pp. 526–535, DOI 10.1145/1250790.1250867.

<a id="ref-SS2006"></a>

- **SS2006.** Špalek, Robert and Szegedy, Mario. *All Quantum Adversary Methods are Equivalent*. 2006. Theory of Computing. 1–18. [Inspected edition or source](https://theoryofcomputing.org/articles/v002a001/v002a001.pdf). Publisher edition. Oracle convention: Section 2.1, p. 4; operator norm: Section 2.4, p. 5; Theorem 3.1 and equation (3.1): p. 6; closing proof: p. 14. The printed error prefactor lacks a factor 1/2 under those conventions; the exact two-bit parity witness checks this local discrepancy without disputing the nonnegative-adversary equivalences.

<a id="ref-BSS2003"></a>

- **BSS2003.** Barnum, Howard and Saks, Michael and Szegedy, Mario. *Quantum decision trees and semidefinite programming*. 2003. Proceedings of the 18th IEEE Annual Conference on Computational Complexity. 179–193. [Inspected edition or source](https://doi.org/10.1109/CCC.2003.1214419). Historical attribution only, verified through Hoyer–Lee–Spalek Theorem 1 and Spalek–Szegedy reference 7. Original full text was not supplied or independently inspected in this review.

<a id="ref-ComplexitylibPinned"></a>

- **ComplexitylibPinned.** complexitylib contributors. *complexitylib: pinned Lean source dependency*. [Inspected edition or source](https://github.com/cslib-community/complexitylib/tree/62ca5c21461b2482e8bd12b7cb9b4937d887a33a). Revision read from the supplied lake-manifest.json and DEPENDENCY_SOURCES.json. Exact proof-source and run evidence are recorded separately in correspondence.json; a source citation alone does not assert successful compilation. No repository commit date or individual author list is inferred.

<a id="ref-GPW2018"></a>

- **GPW2018.** Mika Göös, Toniann Pitassi and Thomas Watson. *Deterministic communication vs. Partition number*. SIAM Journal on Computing (2018), DOI [10.1137/16M1059369](https://doi.org/10.1137/16M1059369). The retained baseline assessment uses [ECCC TR15-050](https://eccc.weizmann.ac.il/report/2015/050/), revision text dated 5 September 2017, Theorem 5 and §2.1, pp. 3–5. Historical construction antecedent; this integration does not claim a fresh full reading.

<!-- /passage:ROOT-REFERENCES -->

[OpenAI2026]: https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf
[BDW02]: https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf
[DW26]: https://arxiv.org/abs/1907.09415v6
[BBCMW98]: https://arxiv.org/abs/quant-ph/9802049v3
[BBCMW01]: https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf
[ABKRT2020]: https://arxiv.org/abs/2010.12629v1
[AA18]: https://arxiv.org/abs/1411.5729v1
[BansalSinha2021]: https://arxiv.org/abs/2008.07003v3
[GirishTalWu2021]: https://arxiv.org/abs/2103.11604v2
[SherstovStorozhenkoWu2023]: https://arxiv.org/abs/2008.10223v4
[Tal2019v1]: https://arxiv.org/abs/1912.12561v1
[ABK2019]: https://arxiv.org/pdf/1511.01937v2
[ABBLSS2015]: https://arxiv.org/pdf/1506.04719v3
[BHMT2000]: https://arxiv.org/abs/quant-ph/0005055v1
[BBHT1996]: https://arxiv.org/abs/quant-ph/9605034v1
[DH1999]: https://arxiv.org/abs/quant-ph/9607014v2
[HMW2003]: https://arxiv.org/abs/quant-ph/0304052v2
[BDK2026]: https://arxiv.org/abs/2609.15063v1
[MPS2023]: https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30
[Drucker2012]: https://arxiv.org/abs/1005.0644v2
[Shaltiel2001]: https://eccc.weizmann.ac.il/report/2001/009/
[Huang2019]: https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf
[Midrijanis2004]: https://arxiv.org/abs/quant-ph/0403168v2
[HLS2007]: https://www.ucw.cz/~robert/papers/madv.pdf
[SS2006]: https://theoryofcomputing.org/articles/v002a001/v002a001.pdf
[BSS2003]: https://doi.org/10.1109/CCC.2003.1214419
[ComplexitylibPinned]: https://github.com/cslib-community/complexitylib/tree/62ca5c21461b2482e8bd12b7cb9b4937d887a33a


## Appendix D. The earlier sufficient threshold

The following complete derivation uses the coarse estimate (F34). The stronger estimate (F43) gives the simpler threshold in §3.15; retaining this argument makes the change of constants and the former proof recoverable.

<a id="forr_historical_threshold"></a>
<!-- passage:forr_historical_threshold -->
<!-- claim:NEW-FOR-25 -->
Fix integers $k=\ell+1\ge2$ and $\tau\ge0$, and a real $0<\delta\le1$. Define

\[
C=16k(2\tau+1)(\ln(4k)+2),\qquad
\eta_0=\min\left(1,\frac{\delta^2}{4\cdot9^\ell}\right)
\]

and

\[
t_0=\max\left\{
8,\left\lceil C/\eta_0\right\rceil,
\left\lceil2\cdot3^\ell/\delta\right\rceil,
\left\lceil4/\delta^3\right\rceil
\right\}.
\tag{H1}
\]

For every integer $t\ge t_0$, put $m=4^t$,
$X=m^{1-1/k}/(2t)^2$, $L=\lfloor X\rfloor$ and $d=2\tau L+1$.
We claim that the coarse advantage expression (F34), at this depth, is at most $\delta$, and that $4/(m\delta^2)\le\delta$.

First, $4t^2\le2^t$ for every integer $t\ge8$. At $t=8$ it is an equality. If it holds at $t\ge8$, then
$(t+1)^2/t^2\le(9/8)^2<2$, proving the next case.
Since $1-1/k\ge1/2$, we have $m^{1-1/k}\ge2^t$, so $X\ge1$. It follows that

\[
d\le(2\tau+1)X,\qquad
\ln(4km)\le(\ln(4k)+2)t.
\tag{H2}
\]

Using $k(1-1/k)=\ell$, the square of the main term in (F34) is therefore at most

\[
9^\ell\left(\frac C{4t}\right)^k.
\tag{H3}
\]

The threshold gives $C/(4t)\le\eta_0/4\le\eta_0\le1$.
Thus (H3) is at most $9^\ell\eta_0\le\delta^2/4$.
The main term is nonnegative and is at most $\delta/2$.

The residual in (F34) is $3^\ell2^{-t\ell}$.
Since $\ell\ge1$, $2^t\ge t$, and $t\ge2\cdot3^\ell/\delta$, it is at most
$3^\ell/t\le\delta/2$. This proves the claimed advantage bound.
Also $4^t\ge t\ge4/\delta^3$, so $4/(m\delta^2)\le\delta$.
These estimates prove the precise ordinary statement NEW-FOR-25.
<!-- /passage:forr_historical_threshold -->

<a id="forr_historical_closure"></a>
<!-- passage:forr_historical_closure -->
For the frozen promise, take $\delta=32^{-k}$ and choose
$\tau=30k$. The exact integer inequality $32\cdot8^{30}<9^{30}$
gives $(8/9)^\tau<\delta$. If a randomized cap-$L$ algorithm existed,
(F40) would provide an amplified acceptance probability $A$ with error
$\varepsilon<\delta$ and depth at most $2\tau L$.

The uniform expectation is at most
$\varepsilon+4/(m\delta^2)<2\delta$.
The coarse advantage just proved would then imply
$\mathbb E_{\nu_1}A<3\delta$.
On the other hand, (F39) and $|\Phi|\le1$ give positive-promise mass at least
$31\delta$, so correctness on yes inputs implies

\[
\mathbb E_{\nu_1}A
\ge(1-\varepsilon)31\delta
\ge\frac{31}{2}\delta>3\delta,
\]

a contradiction. Thus $L<R(P_{k,4^t})$ for every $t\ge t_0$.

This proof preserves the former threshold argument. Section 3.15 uses the sharp uniform theorem to obtain the simpler sufficient threshold $t\ge13669k^2$. The latter is a new ordinary specialization; the reviewed source also contains a separately named explicit, coarser threshold $t\ge3499200k^2$. The ordinary specialization is not being promoted to a separately named Lean theorem; current execution evidence for the existing source declarations is recorded in §2.8.
<!-- /passage:forr_historical_closure -->
