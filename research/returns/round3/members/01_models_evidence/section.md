<!-- Integration: replace §§1–2 of the frozen reasoning-record.md. Preserve the document title and AI-assistance disclosure. This section expects §3 to define and prove the properties of P_{k,m}, §4 to define F_{k,m}, §§5–6 to prove the quantum and randomized bounds, §7 to retain the full exponent argument, and Appendix A to supply the universal upper bound. Existing ROOT anchors are retained below. New source keys and statement proposals accompany this return. -->

## 1. The result and its scope

<a id="ROOT-RESULT"></a>
<!-- passage:ROOT-RESULT -->
For total Boolean functions, the optimal universal power relating bounded-error randomized and quantum query complexity is four. OpenAI's preprint constructs the functions that rule out every smaller power. The universal quartic upper bound was already known: Aaronson, Ben-David, Kothari, Rao and Tal proved that deterministic query complexity satisfies $D(f)=O(Q(f)^4)$, which also bounds randomized complexity because $R(f)\leq D(f)$. The attribution is to [OpenAI (2026), Theorem 1.1 and §1][OAI26] for the separation, and to [Aaronson et al., Theorem 2, printed p. 2 of arXiv v1][ABKRT20] for the upper bound.

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

The two inequalities concern the **same function** at each pair $(k,m)$. In the supplied development, one specified circuit family gives $b_k=6$ and permits $c_k=1/400$, after increasing the threshold. Its correspondence with the preprint and the recorded formal evidence are given in §2.7.
<!-- /passage:ROOT-RESULT -->

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

For a fixed $k$, this reasoning excludes powers strictly below $4-2/k$. It does not produce an exact fourth-power separation for that fixed $k$, and the theorem supplies no estimates uniform in a growing parameter $k=k(m)$. No such uniform assertion is needed for the conclusion about the infimum.

<!-- claim:cor-cubic-refuted -->
Already $k=3$ gives $4-2/k=10/3>3$, so

\[
\neg\exists C\in\mathbb R\ \forall n\geq1\
\forall f:\{0,1\}^n\to\{0,1\},\qquad R(f)\leq C Q(f)^3.
\]

This refutes [Aaronson et al., Conjecture 2, §7, printed p. 20 of arXiv v1][ABKRT20]. Replacing $C$ by $\max(C,1)$ would turn such a bound into a universal shifted cubic bound, already excluded above.
<!-- /passage:R3-01-QUANTIFIERS -->

<a id="ROOT-ARCHITECTURE"></a>
<!-- passage:ROOT-ARCHITECTURE -->
### 1.1. Certificates that disqualify every other candidate

The construction places an accepting certificate in one of $m$ columns. Each column has a string $X_i\in\{0,1\}^m$, several separate inputs to a partial function $P_{k,m}$, and an array of certificate cells. The values of those partial-function inputs determine the address of the relevant cell. For fixed $k$, quantum computation of each promised value is cheap, whereas classical computation is hard. A circuit transcript in the cell certifies the values that form its address.

A column wins if its string is all ones, its address is defined, its transcript is correct, and its cell points to a zero in every other column. These conditions define a total Boolean function: every input either has a winner or does not, regardless of whether any particular address instance satisfies its promise. There is at most one winner. If $i$ and $j\ne i$ both won, the pointer from $i$ would identify a zero in $X_j$, contradicting the requirement that $X_j$ be all ones.

The outward direction of these pointers explains the quantum construction. A genuine winner can use its own certificate to reject every opponent. No opponent's pointer can find a zero in the winner's all-one string. Thus the comparison with a winner remains reliable even when the opponent's address computation is off promise. Comparisons between two losing columns may behave arbitrarily. The tournament in §5 uses only the reliable comparisons involving a winner; a final verification rejects a candidate whose local tests fail. This is the mechanism described in [OpenAI, §1.2][OAI26].

For the randomized lower bound, begin with one hidden zero in every column and blank cells. Erase the zero in a random column and fill its correctly addressed cell with a valid certificate. The resulting input has a winner. A classical algorithm must encounter one of those changes to distinguish the two inputs. Finding the erased zero is rare under a small query cap; finding the filled cell requires enough information about its vector of hard partial-function values. The direct-product argument in §6 makes the second assertion precise for adaptive queries. Together they give a lower budget of order $mL$, while quantum evaluation costs order $\sqrt m$ times logarithmic factors.

The record follows these dependencies: §3 establishes the partial-function ingredients; §4 defines the columns, transcripts and total function; §§5–6 prove its quantum and randomized bounds; §7 compares exponents. Appendix A gives the independent universal upper bound. The finite model examples below explain the conventions used throughout; they are not small instances of the separation construction.
<!-- /passage:ROOT-ARCHITECTURE -->

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

<!-- passage:R3-01-IDENTITY -->
**One-bit identity.** For $f(x)=x_0$, both labels occur, so zero queries are impossible. One classical query returns the bit, and one quantum bit query on $|0,0,z\rangle$ followed by measuring the answer does the same. Thus

\[
D(\mathrm{id}_1)=R(\mathrm{id}_1)=Q(\mathrm{id}_1)=1.
\]
<!-- /passage:R3-01-IDENTITY -->

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

<!-- passage:R3-01-OFFPROMISE -->
**An off-promise input is not a false input.** On one bit, let $f(1)=1$ and leave $f(0)$ undefined. The constant-one algorithm has success one on the entire promise and zero query cost. Consequently $D(f)=R(f)=Q(f)=0$. Replacing its undefined value by false creates one-bit identity, whose three complexities are one. This numerical difference detects a change of problem. Empty promises and partial functions on empty coordinate sets also have all three complexities zero. For every one of these examples, a chosen program's cap remains a bound on its off-promise executions.
<!-- /passage:R3-01-OFFPROMISE -->

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
### 2.7. Formal correspondence and verification

Theorem and equation numbers refer to the OpenAI preprint; section numbers refer to this record unless another source is named. The source snapshot is the supplied round-three packet, labeled `1dd469dd0042b937b739da3bc211eeb60bdf7462`. The current source-bound receipts used here name `31e17dee667d1d72fa621da8e7d3d8ff5fc3960a`; their complete local Lean and configuration hash dictionaries agree with the enclosed bytes. The exact declarations, signatures, premises, receipt paths and source digests used here are in `correspondence.json` and `model_contract.json`.

**Verification note.** The supplied source-bound receipts record a successful root build and comparisons including the Foundations, Separation and Unconditional bundles; the latter also records a paranoid pass. Their local source and configuration hashes and the cited declaration membership have been independently checked against this packet. The challenges compile separately but mechanically share the maintained definitions and theorem specifications, so their agreement establishes conformity to that specification; source review and independently specified examples address its intended mathematical meaning. The dependency export records use in the headline proofs separately from compilation. This review rechecked byte bindings and exact finite examples; it did not rerun Lean or Comparator, and the supplied record reports no human review. Dependency pins are bound, but the external checkout bytes and native compiled artifacts needed for a full replay are not enclosed.

The real-power family (2) is stated directly by `Paper.construction_equation_two`; the named circuit and constants are stated by `Paper.construction_family_named`. The separately compared `theorem_1_1_unconditional` packages the family using the integer lower bound $R(F_{k,m})>\lfloor mL/100\rfloor$, with $L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor$. Floor removal and the full source types are recorded in the correspondence. The build and comparison statuses in the following table belong to those exact declarations.

For the table, `I,J` are finite types, `f : PartialBool I`, `q,T,w : ℕ`, `x : BitInput I`, `ψ : State I w`, `A : AdaptiveProgram I w`, `b : Bool`, `i : I`, and `z : Fin (w+1)`, unless a row says otherwise. The displayed source types are read with those explicit parameters. Full family and bridge types, including all circuit and workspace quantifiers, are expanded without omission in `model_contract.json`. “Build” means declaration membership in the supplied current root receipt. “Comparison” identifies a named compared wrapper, not every declaration used by its proof. An entry marked `unknown` has no current named comparison receipt in this packet.

| Definition or theorem | Source type or exact conclusion | Inputs and ordinary premises | Additional mathematical assumptions | Source-bound evidence |
| --- | --- | --- | --- | --- |
| Partial functions | `PartialBool I = BitInput I → Option Bool`; `totalise : TotalBool I → PartialBool I` | Domain-and-value form translates to this type; no totality assumed | None | Build; exact domain/correctness wrappers built; named comparison `unknown` |
| Deterministic and randomized budgets | `DLe, RLe : PartialBool I → ℕ → Prop`; `D, R : PartialBool I → ℕ` | One tree/mixture, global depth cap, correctness on defined inputs | None | Build; `D_le_iff`, `R_le_iff` compared in Foundations |
| Quantum budgets | `QLe : PartialBool I → ℕ → Prop`; `Q : PartialBool I → ℕ` | Constant-on-promise alternative or one normalized state and capped program before all inputs | None | Build; `Q_le_iff` compared in Foundations |
| Read-all bounds | `R f ≤ D f`, `Q f ≤ D f`, `D f ≤ Fintype.card I` | Arbitrary finite Boolean promise | None | Build and Foundations comparison of each inequality |
| Renaming | `R (reindex e f) = R f`, and the analogous `D`, `Q` equalities | `e : I ≃ J` | None | Build; R and Q compared in Foundations; D comparison `unknown` |
| Oracle | `bitOracle x (ket (i,b,z)) = ket (i,xor b (x i),z)`; involution; a complex linear isometry equivalence | Every input and basis label | None | Build, including exact `Paper.construction_query_oracle`; named comparison `unknown` |
| Output masses | `0 ≤ A.outputMass x ψ b`; `A.outputMass x ψ true + A.outputMass x ψ false = ‖ψ‖^2` | Any vector; unit norm makes the two masses a probability distribution | None | Build; named comparison `unknown` |
| Deferred measurement | `∃ W', entry, U, S, ∀ x ψ, measureProb (run U (entry ψ) x T) S = A.outputMass x ψ true` | `A : AdaptiveProgram (Fin n) w`; `A.queryCap ≤ T`; all witness types as in `exists_fixedSequence` | None beyond the stated cap | Build; named comparison `unknown` |
| Universal exponent | `UniversalPower : ℝ → Prop`; `alphaTot = sInf {α : ℝ \| UniversalPower α}` | Total functions on `Fin n`, $n\geq1$; $\alpha\geq0$ | None | Build; equivalent finite-constant and infimum wrappers built; their named comparison `unknown` |
| Family (2) | `Paper.construction_equation_two (k : ℕ) (hk : 2 ≤ k)`; full type in the contract | Fixed $k\geq2$, then one set of constants and threshold; one circuit at each size satisfies both bounds | None; fixed-parameter Forrelation fact supplied inside the proof | Build and supplied selected axiom audit; named comparison `unknown` |
| Complete Theorem 1.1 | `alphaTot = 4 ∧ UniversalPower 4 ∧` the common-circuit eventual family in floor form | Range and threshold occur inside the conclusion | None | Build; Unconditional comparison, including recorded paranoid pass |
| Exponent alone | `alphaTot_eq_four_unconditional : alphaTot = 4` | No parameters or hypotheses | None | Build and Unconditional comparison |
| Cubic refutation | `¬ ∃ C : ℝ, ∀ n : ℕ, 1 ≤ n → ∀ f : TotalBool (Fin n), (R (totalise f) : ℝ) ≤ C * (Q (totalise f) : ℝ)^3` | Total functions; one common real constant | None | Build and Unconditional comparison |
| Universal upper bound | `universalPower_four : UniversalPower 4` | Total functions as in the definition | None | Build; Separation comparison; headline proof uses the imported complexitylib route |
| Exact examples of §2.6 | The stated costs and finite success tables | The explicitly named promises and functions | None in the ordinary proofs | Ordinary proofs and exact finite arithmetic; exact example Lean/Comparator receipts `unknown` |

The distinction between ordinary premises and additional assumptions belongs to a declaration's actual type. For example, $k\geq2$ is a parameter restriction in (2). In contrast, `family_bounds` retains `Lvalue k t < R (P k t)` in its lower-bound clause, and `theorem_1_1` has the explicit parameter `h : BansalSinhaLower`. Those statements remain conditional when cited on their own. The unconditional wrappers supply the fixed-parameter lower bound internally; their names and types are different.

The exact-arithmetic checker supplied with this section verifies the small truth tables, the one-query classical OR obstruction and the two-bit quantum interference calculation. The packet's separate finite semantic controls also distinguish per-input algorithm selection, a weakened success threshold, false completion of an undefined value, minimum rather than maximum branch cost, a strict rather than inclusive success threshold, and two deliberately wrong promise/comparison specifications. Matching these finite controls neither proves general model equivalence nor constitutes a Lean or Comparator execution. Conversely, a compared theorem about the shared specification does not establish its intended meaning merely by passing the comparison.
<!-- /passage:ROOT-EVIDENCE-CONVENTION -->

[OAI26]: https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf
[ABKRT20]: https://arxiv.org/pdf/2010.12629v1
[BDW02]: https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf
[DW26]: https://arxiv.org/abs/1907.09415v6
[BBCMW98]: https://arxiv.org/abs/quant-ph/9802049v3
[BBCMW01]: https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf
