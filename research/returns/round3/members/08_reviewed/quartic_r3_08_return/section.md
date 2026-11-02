# Replacement for §7 and Appendix A

**Scope.** This is an advisory replacement for §7 and Appendix A of the supplied long reasoning record, not an integrated revision of the whole paper. It retains OpenAI's attribution for the separation and the cited authors' attribution for the universal upper bound.

**Neighboring inputs.** The section uses the bit-query models of §2; the fixed-parameter Forrelation lower bound and exact domain/value circuit of §3.17; the total function defined in §4; the worst-case quantum query cap of §5.4; and the planted lower bound and floor estimates of §6.6. Their exact consequences are restated below. All logarithms denoted by \(\log_2\) have base two; \(\ln\) denotes the natural logarithm. The parameter \(k\) is fixed before the size tends to infinity.

**Authorship and evidence.** This reconstruction was prepared with AI assistance from the supplied sources and current source-bound receipts. It introduces no new Lean source. The mathematical exposition, exact finite checks, existing native execution records, and Comparator results are distinguished in the accompanying correspondence and review notes.

## 7. The optimal exponent

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

<!-- passage:ROOT-RATIO -->
Fix \(0\leq\alpha<4\). Choose an integer \(k\geq2\) with
\[
k>\frac{2}{4-\alpha}.
\tag{7.2}
\]
This choice ensures that
\[
\delta=2-\frac1k-\frac\alpha2>0.
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
\frac{m^\delta}{(\log_2m)^{2+\alpha b_k}}
\qquad(t\geq\max\{t_0(k),1\}).
\tag{7.3}
\]

The right side tends to infinity. To see explicitly why its logarithmic denominator is harmless, put \(e=2+\alpha b_k\). For \(m=4^t\), the logarithm of its varying factor is
\[
\ln\!\left(\frac{m^\delta}{(\log_2m)^e}\right)
=2\delta t\ln2-e\ln(2t).
\]
For \(u\geq1\),
\[
\ln u=\int_1^u\frac{ds}{s}
\leq\int_1^u\frac{ds}{\sqrt s}
\leq2\sqrt u.
\]
Hence \(\ln(2t)/t\to0\), whereas \(2\delta\ln2>0\). The displayed logarithm tends to infinity, and so does the quotient in (7.3). This includes \(\alpha=0\); no division by \(Q\) is involved.

For a fixed \(k\), the argument applies exactly when \(\alpha<4-2/k\). For example, \(k=2\) supplies the threshold exponent three, and \(k=3\) supplies \(10/3\). Thus \(k=3\) already refutes a cubic universal bound. At \(\alpha=4-2/k\), the power gap \(\delta\) vanishes, and (7.3) alone supplies no divergence. No fixed finite \(k\) in this argument attains exponent four.
<!-- /passage:ROOT-RATIO -->

### 7.2. Excluding all smaller universal powers

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

<!-- passage:ROOT-EXPONENT-CORRESPONDENCE -->
The source preprint supplies the attribution for this exponent argument; the supplied Lean sources and frozen execution records support the formal claims separately. The named-circuit statement `QuarticQuery.Paper.construction_family_named` proves (7.1) for `Forrelation.forrCircuit (k-1) t`, with constant \(1/400\), logarithmic exponent six, the quantum constant `Upper.budgetConst k`, and the circuit-size bound in the same conclusion. `construction_equation_two` packages these facts existentially. Neither statement has an unproved Forrelation binder.

`QuarticQuery.Paper.classical_ratio_arithmetic` proves the finite quotient inequality. `classical_exponent_ratio` adds divergence of the explicit lower envelope and the quotient for abstract sequences satisfying the fixed-parameter bounds. `classical_Fkm_ratio` specializes all three conclusions to the named total-function family with \(b_k=6\). Thus the literal quotient and limit now have formal support; the older declaration `QuarticQuery.eventually_gt_rpow` supplies only the sufficient eventual strict comparison. The elementary integral argument above explains the same limit by a different proof.

`QuarticQuery.exists_nat_exponent`, `not_universalPower_of_family`, and `alphaTot_eq_four_of` implement the choice of \(k\), exclusion of smaller exponents, and infimum argument. Their intermediate binders for family bounds and reindexing are discharged by the model and construction theorems. The final declarations `alphaTot_eq_four_unconditional`, `theorem_1_1_unconditional`, and `cubic_bound_fails_unconditional` have no mathematical assumption left open.

The timestamped root-build receipt contains all these names and binds the supplied source bytes. The reviewed type-and-axiom audit separately covers the newer named-family and quotient declarations. The timestamped Unconditional Comparator receipt covers the final compared declarations, not every explanatory helper. The challenges share the maintained definitions and theorem specifications; independent compilation does not make them independently authored mathematical tests. These statements consume the supplied receipts; this prose revision does not claim a new Lean execution.
<!-- /passage:ROOT-EXPONENT-CORRESPONDENCE -->


## Appendix A. The universal quartic bound

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
contradicting the explicit exact algorithm. The strict comparison is exact since \(99<625\). Høyer–Lee–Špalek's denominator two agrees with the progress argument and this witness. This discrepancy concerns the printed prefactor; it does not contradict the equivalence of adversary formulations or the quartic asymptotic bound. A separate older annex transcription inserted an extra square root around the entire denominator. Removing that transcription error does not restore the missing factor two. No author-confirmed erratum is claimed. Neither the sharper progress coefficient nor \(1/35\) is asserted to be the optimal constant over all possible lower-bound arguments. The accompanying exact-arithmetic script checks the four input states, oracle permutation, masks, eigenbasis, output probabilities and progress drop.
<!-- /passage:R3-A-PARITY-PREFACTOR -->

### A.3. Two applications of the same adversary theorem

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

<!-- passage:R3-A-SPECTRAL -->
Now take \(\Gamma=S_f\). For each coordinate, its sensitive edges form a partial matching: each input has only one neighbor obtained by flipping that coordinate. The masked matrix is a direct sum of matrices \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) and zeros, so its norm is at most one. If \(f\) is nonconstant, a path in the cube between opposite-output inputs contains a sensitive edge, so \(S_f\ne0\). Applying (A.3) gives
\[
 \lambda(f)\le35Q(f).
\tag{A.6}
\]
For a constant function, \(S_f=0\) and (A.6) is immediate. This is the sensitivity-graph application in [ABKRT, arXiv v1, Lemma 9, printed p. 8][ABKRT2020]; (A.5) and (A.6) are the two conclusions of OpenAI's Lemma A.3.
<!-- /passage:R3-A-SPECTRAL -->

### A.4. A maximum-degree face and Huang's signed cube

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

The second route proves the intermediate general-matrix, star, actual-face and recursive-matrix statements used in this appendix. Its larger numerical constant reflects the star estimate for block sensitivity. The hybrid keeps the stronger polynomial-method estimate and is exported separately. The first route is the one used by the current headline proof; the other two are separately compiled alternatives. The constants distinguish implementations of known inequalities; none establishes a sharp universal constant. The coefficients in the first and third rows are read from the pinned complexitylib proof and its project wrappers; the reconstruction of (A.1) uses the fully explained second row.
<!-- /passage:R3-A-ASSEMBLY -->

<!-- passage:R3-A-FORMAL -->
The current source-bound native receipts record successful compilation of the ten `Paper/AppendixA*.lean` modules and a successful post-root type and allowed-axiom audit for the reviewed declarations. This supersedes the historical “unelaborated” comments retained in the source and the baseline's statements that these intermediate theorems have no formal ties. No new Lean execution was performed for this prose revision. The complete types, exact source hashes and receipt locations are in the correspondence accompanying this section.

The general bound is `QuarticQuery.Paper.appendixA_lemmaA2`; its Perron and progress assumptions are proved by its dependencies and are not extra open hypotheses. The star and sensitivity estimates are `appendixA_lemmaA3_adversary`, the actual-face spectral degree theorem is `appendixA4_paper_route`, and the Midrijānis bridge is `appendixA_lemmaA5`, all in `QuarticQuery.Paper`. The cap-level and attained-minimum quartic statements are `appendixA_D_le_of_QLe` and `appendixA_D_le_Q_pow_four`; `appendixA_theoremA1` also includes \(R\le D\). The older `QuarticQuery.D_le_Q_pow_four` proves coefficient 20736, while `QuarticQuery.Paper.appendixA_D_le_Q_pow_four_hybrid` proves 19600.

Some corpus rows deliberately combine several assertions. For example, the matrix spectrum row includes square, trace, symmetry, eigenvalue classification and multiplicities; these are supplied by several declarations, rather than by the multiplicity theorem alone. Likewise the per-query row and the final-overlap row each have separate supporting estimates. Their correspondence remains partial at a single primary declaration even though the named additional declarations have current compilation evidence. The polynomial-definition prose includes an ordinary uniqueness proof beyond the one Fourier-degree bridge. The exact parity witness above is an ordinary mathematical and finite-computational check, with no supplied Lean theorem for its exact one-query algorithm. Comparator acceptance of the existing separation wrapper does not constitute a separate comparison of each new Appendix declaration.
<!-- /passage:R3-A-FORMAL -->


### References for these sections

These citations retain the exact editions and locators used above. The arXiv numbering of ABKRT belongs to its 2020 preprint; the work subsequently appeared at STOC 2021. The Høyer–Lee–Špalek locator is to the 29-page author PDF, not the ten-page proceedings edition. The supplied Huang PDF is arXiv:1907.00847v2; the Annals edition cited here was also inspected at printed pp. 952–953. The supplied OpenAI PDF, rather than a newly fetched public copy, is the source for §5 and Appendix A.

- **[OpenAI2026]** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, preprint, 5 October 2026, §5 and Appendix A, printed pp. 14–17. Supplied PDF SHA-256: `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.
- **[ABKRT2020]** Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal, *Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem*, arXiv:2010.12629v1, 23 October 2020. Theorem 1, printed pp. 1 and 6–7; Theorem 2 and its proof, p. 2; Definition 7, p. 6; Lemma 9, p. 8; Conjecture 2, p. 20.
- **[Huang2019]** Hao Huang, *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, Annals of Mathematics 190(3) (2019), 949–955. Lemma 2.2, p. 952; the proof of Theorem 1.1 and its spectral remark, p. 953. DOI: `10.4007/annals.2019.190.3.6`.
- **[Midrijanis2004]** Gatis Midrijānis, *Exact quantum query complexity for total Boolean functions*, arXiv:quant-ph/0403168v2, 27 March 2004. Lemma 3 and the proof of Theorem 4, printed pp. 3–4.
- **[SS2006]** Robert Špalek and Mario Szegedy, *All Quantum Adversary Methods are Equivalent*, Theory of Computing 2 (2006), 1–18. Oracle and norm conventions, §§2.1 and 2.4, printed pp. 4–5; Theorem 3.1 and equation (3.1), p. 6; repeated coefficient in the proof, p. 14. DOI: `10.4086/toc.2006.v002a001`. The numerical-prefactor qualification is proved above.
- **[HLS2007]** Peter Høyer, Troy Lee and Robert Špalek, *Negative weights make adversaries stronger*, 29-page author PDF; Definition 1 and Theorem 1, printed p. 3. Work published in STOC 2007, 526–535; the cited theorem locator is to the author PDF.
- **[BSS2003]** Howard Barnum, Michael Saks and Mario Szegedy, *Quantum decision trees and semidefinite programming*, CCC 2003, 179–193, DOI `10.1109/CCC.2003.1214419`. Historical attribution as given by the inspected sources; original full text unavailable and not independently inspected.

[OpenAI2026]: https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf
[ABKRT2020]: https://arxiv.org/abs/2010.12629v1
[Huang2019]: https://annals.math.princeton.edu/2019/190-3/p06
[Midrijanis2004]: https://arxiv.org/abs/quant-ph/0403168v2
[SS2006]: https://theoryofcomputing.org/articles/v002a001/v002a001.pdf
[HLS2007]: https://www.ucw.cz/~robert/papers/madv.pdf
