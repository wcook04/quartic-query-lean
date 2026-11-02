# The randomized lower bound for the specified Forrelation promise

**Replacement scope.** This text replaces §§3.6–3.16 of the supplied long reasoning record. It uses the promise, sign convention and Walsh normalization of §3.1, restated below, and supplies precisely the randomized lower-bound component consumed by §3.17. The quantum algorithm and exact circuit remain separate components. The numerical threshold derived in §3.15 is an ordinary consequence of the current uniform theorem; the final paragraph distinguishes that deduction from the statements covered by the supplied Lean receipts.

### 3.6. The statement and the proof

<!-- passage:forr_target -->
Let $k\ge2$ and $t\ge0$ be integers, let $m=4^t$, and index each of the $k$ input blocks by binary strings of length $2t$. A bit $x$ represents the sign $(-1)^x$. Write

<!-- claim:eq-3 -->
\[
H_{a,b}=m^{-1/2}(-1)^{a\cdot b},\qquad
u=m^{-1/2}(1,\ldots,1)^{\mathsf T},\qquad
\Phi(z)=u^{\mathsf T}D_{z_0}H D_{z_1}H\cdots H D_{z_{k-1}}u,
\qquad \delta=2^{-5k}=32^{-k}.
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

This is the lower-bound assertion of OpenAI's Lemma 2.1(i), with exactly its normalization and promise [OpenAI2026Quartic, §2.1, pp. 3–4]. The proof below supplies the explicit sufficient choice $t_0(k)=13669k^2$. All analytic logarithms below are natural; the logarithm in $L_{k,m}$ is base two.
<!-- /passage:forr_target -->

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

<!-- passage:forr_proof_spine -->
The direct proof constructs two distributions on the whole sign cube. The first is uniform. The second is obtained by rounding a chain of correlated Gaussian vectors to signs. Their Forrelation means differ, but a shallow decision tree has nearly the same expectation under both distributions. To prove this indistinguishability, scale only the first block of Gaussian biases. Differentiation starts in that block; Gaussian integration by parts then moves the derivative through one coordinate of each successive block. Every attempted return to a coordinate already differentiated vanishes by multilinearity. The resulting order-$k$ derivative sum is controlled by a martingale along the decision tree.

Two moment estimates turn this expectation comparison into a promise lower bound. Because neither distribution is entirely supported on the promise, the algorithm is first amplified, and its behavior on unpromised inputs is bounded only by the interval $[0,1]$. The same estimates give a uniform numerical lower bound. Comparing that bound with $L_{k,m}$ proves (F3).
<!-- /passage:forr_proof_spine -->

### 3.7. Multilinear expectation and derivatives

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

proving (F25). The proof also gives the weaker bound with residual $1$ used in the original fixed-parameter presentation. All constants are uniform in the bias, the tree and the selected subset family.
<!-- /passage:forr_tree_derivative -->

### 3.12. Indistinguishability of shallow trees

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

The lower bound also ensures that both promise values occur in these dimensions. If one of them were absent, a constant zero-query algorithm would compute the partial function on its domain, contradicting (F43). The previous four-term, much larger sufficient threshold is still valid; its derivation is retained in the companion historical-threshold note so that replacing the exposition does not erase that argument.
<!-- /passage:forr_threshold -->

### 3.16. Literature comparison and the scope of the conclusion

<!-- passage:forr_credit -->
The proof above uses a known Gaussian-chain architecture and a known decision-tree growth strategy. Bansal and Sinha's Theorem 1.3 is the original quantitative lower-bound theorem for the promise in (F2); their §3 supplies the Gaussian-pair and conditional-rounding antecedent, and their Lemma 4.3 supplies the transformed integration-by-parts antecedent. Their truncation is the Gaussian distribution function minus $1/2$. The algebraic function (F9) used here defines a different hard distribution. Accordingly, (F16), (F22), and (F39) were proved for this distribution, rather than imported from their promise-mass theorem.

The adaptive-path martingale in §3.11 follows the ordinary-tree discussion of Girish, Tal, and **Kewen Wu**, arXiv:2103.11604v2, §1.3 and Lemma 1.9, pp. 6–8; the conference version numbers the corresponding result Lemma 9. That source motivates the contracted coefficient arrays and induction on degree. The centered variables, bounded-bias constants, repeated-query treatment, and stopped-process estimate used here were stated and proved explicitly. This attribution does not claim that the cited lemma already has the exact raw-derivative statement (F25).

The one-block interpolation isolates one raw derivative in each labelled block. As (F24) makes explicit, this does not discard the higher uniform Fourier levels of the test function. The bounded search and source comparison in this return establish neither priority nor novelty for this arrangement.
<!-- /passage:forr_credit -->

#### The displayed comparison in Bansal–Sinha §5.4

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

<!-- passage:forr_validation_scope -->
Finally, the mathematical statements have distinct formal and evidential scopes. The supplied current source proves the exact fixed-$k$ proposition as QuarticQuery.ForrelationLower.bansalSinhaLower, and the current ordinary and paranoid Unconditional Comparator receipts explicitly list it. The sharper restricted endpoint (F43) is also already present as QuarticQuery.forrelation_lower_uniform_sharp: it is explicitly listed in the current root-build receipt, has an accepted focused Uniform build, and its elaborated type and standard axiom list are printed in the successful reviewed audit. It is **not** listed in Comparator. Older prose calling this endpoint merely proposed is superseded by those source-matched records.

The new threshold (F51), the finite-polynomial explanation of differentiation, and the comparison deduction (F57)–(F60) are ordinary mathematics in this section. No separately compiled Lean wrapper for those formulations is claimed. The ordinary proof of (F25) allows arbitrary bounded real leaf labels; the local interface uses a Boolean-output tree followed by one fixed map from its two output values into $[-1,1]$, which suffices for acceptance probabilities. In particular, (F60) depends on an external Fourier theorem and allows variable error and every power-of-two dimension; it is not the type of either existing endpoint. The source and evidence checks here recomputed the recorded local file hashes, but did not run Lean afresh. Exact declaration types, premises, source bindings, and the limits of each receipt are recorded in the accompanying correspondence and evidence files.
<!-- /passage:forr_validation_scope -->
