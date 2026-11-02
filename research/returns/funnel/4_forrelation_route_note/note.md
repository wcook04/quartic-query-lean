**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Uniform Forrelation lower bounds from a single-block interpolation

<!-- passage:abstract -->
**Abstract.** We give a Gaussian integration-by-parts proof of the randomized query lower bound for the usual $k$-fold Forrelation promise. Scaling the first block of a rounded Gaussian chain produces an identity involving derivatives of order exactly $k$ at bounded biases. Each application of Stein's identity removes the factor created by the preceding application. An elementary martingale estimate gives the explicit bound $R_{1/3}(P_{k,m})>(2/18225)m^{1-1/k}/[k^2\ln(4km)]$ for $m\ge 2^{15k+2}$. Combining the same identity with the Fourier-weight theorem of Sherstov, Storozhenko and Wu gives $R_{(1-\eta)/2}(P_{k,m})\ge c\eta^2[m/(1+\ln(km))]^{1-1/k}$, with an absolute $c>0$. We specify $c$ in terms of the published Fourier constant and give the finite inequality before simplifying it. The Gaussian-chain distribution follows Bansal and Sinha; the elementary Fourier argument follows the decision-tree martingale method of Girish, Tal and Wu. The quantitative endpoints are paper deductions, distinct from the fixed-$k$ theorem in the supplied Lean development.
<!-- /passage:abstract -->

## 1. The result

<!-- passage:problem -->
Let $k\ge2$ and let $m$ be a power of two. Index the rows and columns of the normalized Walsh matrix $H$ by binary strings of length $\log_2m$, so $H_{a,b}=m^{-1/2}(-1)^{a\cdot b}$. It is real, symmetric and orthogonal. For sign vectors $z_0,\ldots,z_{k-1}\in\{-1,1\}^m$, put

$$
\Phi(z)=\frac1m\sum_{p\in[m]^k}
 \left(\prod_{r=0}^{k-1}z_r(p_r)\right)
 \left(\prod_{r=0}^{k-2}H_{p_{r+1},p_r}\right),
\qquad \delta=32^{-k}.
\tag{1}
$$

Define $P_{k,m}(z)=1$ when $\Phi(z)\ge\delta$, and $P_{k,m}(z)=0$ when $|\Phi(z)|\le\delta/2$; it is undefined otherwise. These are the thresholds in Bansal and Sinha (2020), Theorem 1.3, and in OpenAI (2026), equations (3)–(4). In the supplied corpus they have identifiers `eq-3` and `eq-4`. The mathematical definition here also permits odd $\log_2m$; the public Lean definition uses $m=4^t$.

For a partial function $P$, let $R_\varepsilon(P)$ denote the least worst-case number of bit queries of a randomized decision tree with error at most $\varepsilon$ on every input in the domain of $P$. The maximum is over inputs and random coins. On inputs outside the domain the algorithm is unrestricted. We use natural logarithms except where the base is written explicitly. The input length is $km$.
<!-- /passage:problem -->

<!-- passage:sharp-theorem -->
**Theorem 1.** Fix a universal constant $C\ge1$ such that every Boolean-valued depth-$d$ decision tree on $n$ sign variables satisfies

$$
 \sum_{|S|=j}|\widehat T(S)|
 \le C^j\sqrt{\binom d j}\,(1+\ln n)^{(j-1)/2}
 \quad (1\le j\le n).
\tag{2}
$$

Such a constant exists by Sherstov, Storozhenko and Wu (2023), Theorem 1.9 and Corollary 4.14. For every $k\ge2$, every power of two $m\ge2^{15k+2}$, and every $0<\eta\le1$,

$$
 R_{(1-\eta)/2}(P_{k,m})
 \ge \frac{\eta^2}{162eC^2}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.
\tag{3}
$$

Corollary 4.14 is already in the natural-log form (2); Theorem 1.9 states the equivalent base-two version. The source does not specify a numerical value for its absolute constant $C$. Formula (3) displays its entire contribution to the constant. This theorem is a mathematical consequence of the identity proved below and the cited Fourier theorem. Neither (2) nor (3) is established by a new Lean run in this return.
<!-- /passage:sharp-theorem -->

<!-- passage:elementary-theorem -->
There is also a completely numerical conclusion whose proof uses only the elementary Fourier estimate proved in §6.

**Theorem 2.** For every $k\ge2$ and every power of two $m\ge2^{15k+2}$,

$$
 R_{1/3}(P_{k,m})>
 \frac2{18225}\frac{m^{1-1/k}}{k^2\ln(4km)}.
\tag{4}
$$

The size restriction ensures that the uniform distribution puts sufficiently little mass outside the zero-promise region. A finite inequality in §7 retains the exact exceptional-mass term and can be used without this particular restriction. No assertion that (3) holds for all smaller $m$ is made.
<!-- /passage:elementary-theorem -->

<!-- passage:relation-to-literature -->
Bansal and Sinha's Theorem 1.3 gives a lower bound of order $k^{-29}\eta^2[m/\log(km)]^{1-1/k}$. Their Theorem 3.2 controls a rounded Gaussian chain by biased Fourier levels from $k$ through $k(k-1)$. We use the same pattern of independent Gaussian layers and products in the intermediate blocks, with an algebraic truncation and a different interpolation. Only the first block is scaled. The derivative created on entering an intermediate block removes the dependence that could send the next differentiation back into that block.

Tal (2019), §1.3, asked whether control of the $k$th Fourier level could suffice for a different analysis of $k$-fold Rorrelation. The identity here applies to a smooth rounded distribution and controls derivatives at biased points. It therefore addresses a close formulation of that question; it does not identify Tal's sign-rounded distribution with the distribution used here. Single-level control also appears in fractional pseudorandom generators (Chattopadhyay et al., 2021) and in Wu's analysis of XOR-Forrelation (2021), Theorem 3.2. The particular single-block Stein chain was not located in the sources searched through 2 November 2026. This is a bounded search finding, not a priority claim.

The proof begins with the multilinear extension and an elementary Stein identity. Section 3 proves the interpolation identity. Section 4 verifies the promise mass, and §5 treats amplification. Section 6 proves the elementary Fourier estimate. Section 7 proves both quantitative theorems. The only substantive theorem imported into the proof of Theorem 1 is (2); the proof of Theorem 2 is supplied in full.
<!-- /passage:relation-to-literature -->

## 2. Multilinear extension and a bounded Stein kernel

<!-- passage:cube-extension -->
For $g:\{-1,1\}^n\to\mathbb R$, write $\widetilde g$ for its multilinear extension, equivalently its expectation under independent signs with prescribed means:

$$
 \widetilde g(\mu)=\sum_{x\in\{-1,1\}^n}g(x)
       \prod_{i=1}^n\frac{1+\mu_ix_i}{2}
 =\sum_{S\subseteq[n]}\widehat g(S)\prod_{i\in S}\mu_i,
 \qquad \mu\in[-1,1]^n.
\tag{5}
$$

Here $\widehat g(S)=2^{-n}\sum_xg(x)\prod_{i\in S}x_i$. The equality follows by expanding the product in the first expression and interchanging finite sums. In particular, $\widetilde g(0)$ is the uniform mean of $g$, the extension preserves inequalities on this cube, and $\partial_i^2\widetilde g=0$. For a set $S$ of distinct coordinates, $\partial_S$ means one derivative in each coordinate. This raw derivative convention avoids normalization factors from biased orthonormal bases.
<!-- /passage:cube-extension -->

<!-- passage:kernel -->
Put

$$
 \Psi(x)=\frac1{2\sqrt{2+x^2}},\qquad
 \varphi(x)=\frac{x(3+x^2)}{2(2+x^2)^{3/2}},\qquad
 \varphi'(x)=\frac3{(2+x^2)^{5/2}}.
\tag{6}
$$

**Lemma 3.** The function $\varphi$ is odd, increasing and bounded in absolute value by $1/2$. Moreover,

$$
 0<\Psi(x)\le\frac1{2\sqrt2},\qquad
 0<\varphi'(x)\le\frac3{4\sqrt2},\qquad
 0<\Psi(x)\varphi'(y)\le\frac3{16}.
\tag{7}
$$

*Proof.* Differentiation gives (6). Positivity of the derivative and the limits $\varphi(\pm\infty)=\pm1/2$ prove the first assertions. Each denominator in (7) is minimized at zero. Multiplying the two bounds gives the last one. We shall write $b=3/16$. ∎
<!-- /passage:kernel -->

<!-- passage:stein -->
**Lemma 4.** If $G:\mathbb R\to\mathbb R$ is continuously differentiable and both $G$ and $G'$ are bounded, then, for a standard normal $Z$,

$$
 \mathbb E[\varphi(Z)G(Z)]
   =\mathbb E[\Psi(Z)G'(Z)].
\tag{8}
$$

*Proof.* Let $\gamma(x)=(2\pi)^{-1/2}e^{-x^2/2}$. Direct differentiation gives $\varphi=x\Psi-\Psi'$ and hence $(\Psi\gamma)'=-\varphi\gamma$. Integrate the derivative of $\Psi G\gamma$ on $[-A,A]$ and let $A$ tend to infinity. Its boundary values tend to zero because $\Psi G$ is bounded. Both integrands are dominated by a constant times $\gamma$, so dominated convergence proves (8). Conditional application proves the same identity in any coordinate of a vector of independent standard normals. ∎

This is Gaussian integration by parts with a chosen antiderivative. Bansal and Sinha, Lemma 4.3, supply a transformed identity for their Gaussian-cdf truncation. The present algebraic choice keeps the kernel bounded with the explicit constant in (7).
<!-- /passage:stein -->

## 3. Interpolation through the first block

<!-- passage:chain-definition -->
For this section let $H$ be any real orthogonal $m\times m$ matrix, and put $l=k-1$. Draw independent standard Gaussian vectors $U_0,\ldots,U_{l-1}\in\mathbb R^m$, and set $V_r=HU_r$. Write $X_r(a)=\varphi(U_r(a))$ and $Y_r(a)=\varphi(V_r(a))$. For $0\le s\le1$ define a bias vector with $k$ blocks by

$$
 \begin{aligned}
 w_s(0,a)&=sX_0(a),\\
 w_s(r,a)&=Y_{r-1}(a)X_r(a) &&(1\le r\le k-2),\\
 w_s(k-1,a)&=Y_{k-2}(a).
 \end{aligned}
\tag{9}
$$

Its endpoint blocks have absolute value at most $1/2$, and its intermediate blocks have absolute value at most $1/4$. Conditional on the Gaussians, draw independent signs with means $w_1$. Denote their unconditional law by $\mathcal D_H$. Thus $\mathbb E_{\mathcal D_H}g=\mathbb E_U\widetilde g(w_1)$. We use the orientation $V_r(b)=\sum_aH_{b,a}U_r(a)$ throughout; it determines the order of the matrix indices below.
<!-- /passage:chain-definition -->

<!-- passage:zero-endpoint -->
**Lemma 5.** For every $g:\{-1,1\}^{km}\to\mathbb R$,

$$
 \mathbb E_U\widetilde g(w_0)=\widetilde g(0).
\tag{10}
$$

*Proof.* Block 0 is zero at $s=0$. Consequently $U_0$ now enters only through the next block, which is $Y_0X_1$ if $k>2$, and $Y_0$ if $k=2$. The coordinates of $V_0$ are independent standard normals, since $H$ is orthogonal. Conditional on all later Gaussian vectors, the coordinates of $Y_0$ are therefore independent, have mean zero, and are bounded. Integrating the multilinear polynomial sets that entire block to zero: in each nonconstant monomial at least one independent mean-zero factor remains. After each elimination, $U_r$ enters only through the next block, with factor $Y_rX_{r+1}$ for an intermediate block and $Y_r$ for the final block. The same conditional calculation eliminates it. Repeating through the final block gives (10). All expectations are finite because $\widetilde g$ is bounded on the compact cube. ∎
<!-- /passage:zero-endpoint -->

<!-- passage:path-identity -->
For a path $p=(p_0,\ldots,p_{k-1})\in[m]^k$, let $S_p=\{(r,p_r):0\le r<k\}$ and put

$$
 A_p(U)=\prod_{r=0}^{k-2}
       H_{p_{r+1},p_r}\Psi(U_r(p_r))\varphi'(V_r(p_{r+1})).
\tag{11}
$$

**Proposition 6.** For every real orthogonal $H$ and every real function $g$ on the sign cube,

$$
 \mathbb E_{\mathcal D_H}g-\mathbb E_{\mathcal U}g
 =\int_0^1\sum_{p\in[m]^k}
       \mathbb E_U\left[A_p(U)\,
          \partial_{S_p}\widetilde g(w_s)\right]\,ds,
\tag{12}
$$

where $\mathcal U$ is the uniform law on that cube.

*Proof.* Put $h(s)=\mathbb E_U\widetilde g(w_s)$. The integrand is a polynomial in $s$ with bounded coefficients, so differentiation under expectation gives $h'(s)=\sum_a\mathbb E[X_0(a)\partial_{(0,a)}\widetilde g(w_s)]$.

Fix $a$ and apply (8) in $U_0(a)$. The derivative can enter block 0 through $X_0(a)$, or block 1 through the coordinates $Y_0(b)$. The first possibility differentiates the already differentiated coordinate $(0,a)$ a second time and is zero. The second gives the factor $H_{b,a}\varphi'(V_0(b))X_1(b)$ and the derivative $\partial_{(1,b)}\partial_{(0,a)}\widetilde g(w_s)$. When $k=2$, block 1 is the final block and $X_1(b)$ is absent, so the calculation is already finished.

For $k>2$, apply (8) next in $U_1(b)$. The factor $\Psi(U_0(a))\varphi'(V_0(b))$ depends only on $U_0$, so this differentiation does not affect it. The dependence through the coordinate $(1,b)$ again produces a repeated partial derivative and vanishes. Differentiating block 2 produces one matrix entry, one $\varphi'$ factor and, unless this is the final block, one $X_2$ factor. Inductively, after entering block $r$, the accumulated weight depends only on $U_0,\ldots,U_{r-1}$; the remaining factor $X_r(p_r)$ is attached to the coordinate already removed by $\partial_{(r,p_r)}$.

This proves $h'(s)=\sum_p\mathbb E[A_p\partial_{S_p}\widetilde g(w_s)]$. Every use of (8) is legitimate: the cube has finite dimension, all partial derivatives of its multilinear polynomial are bounded on the bias cube, and $\varphi$, $\varphi'$ and the finite matrix coefficients bound the required one-coordinate derivatives. The accumulated weights are also bounded. Integrating from 0 to 1 and using (10) proves (12). ∎
<!-- /passage:path-identity -->

<!-- passage:three-block-example -->
For $k=3$, the bias is $(s\varphi(U),\varphi(HU)\varphi(U'),\varphi(HU'))$. Starting with the derivative in $(0,a)$, the first integration by parts produces a factor $\varphi(U'(b))$ at the coordinate $(1,b)$ just differentiated. The second integration by parts removes it. The resulting term is

$$
 H_{b,a}H_{c,b}\,\mathbb E\!\left[
 \Psi(U_a)\varphi'((HU)_b)
 \Psi(U'_b)\varphi'((HU')_c)
 \partial_{(0,a),(1,b),(2,c)}\widetilde g(w_s)\right].
\tag{13}
$$

There is one index in each block. This example displays the repeated-derivative cancellation used at every step of the general proof.
<!-- /passage:three-block-example -->

<!-- passage:biased-level-meaning -->
Equation (12) uses derivatives of order $k$ at a common bias vector. It does not assert that only degree-$k$ coefficients of $g$ under the uniform measure affect the answer. Expanding (5) gives

$$
 \partial_S\widetilde g(\mu)
    =\sum_{T\supseteq S}\widehat g(T)\prod_{i\in T\setminus S}\mu_i.
\tag{14}
$$

Higher uniform levels enter this derivative. The uniformity of the Fourier estimate over the relevant biases is therefore a required hypothesis. It is supplied either directly in §6 or by restrictions in §7.
<!-- /passage:biased-level-meaning -->

<!-- passage:advantage -->
Let $\|H\|_{\max}=\max_{a,b}|H_{a,b}|$. Taking absolute values in (12) and using (7) gives

$$
 \left|\mathbb E_{\mathcal D_H}g-\mathbb E_{\mathcal U}g\right|
 \le (b\|H\|_{\max})^{k-1}
     \sup_{s,U}\sum_{p\in[m]^k}
          |\partial_{S_p}\widetilde g(w_s)|.
\tag{15}
$$

The paths give distinct coordinate sets, so no factor of $k!$ enters this sum. For Walsh $H$, its entry bound is $m^{-1/2}$. The supplied Lean theorem `advantage_le` proves an estimate of this form with the coarser edge constant $3$, followed by its elementary Fourier estimate. Formula (15) with $b=3/16$ is a separate strengthening in this note.
<!-- /passage:advantage -->

## 4. The promise under the two distributions

<!-- passage:general-moments -->
For an arbitrary real orthogonal $H$, define $\Phi_H$ by (1) using that matrix and the same index order. In matrix notation it is $m^{-1}{\bf1}^{\mathsf T}D_{z_{k-1}}H D_{z_{k-2}}\cdots H D_{z_0}{\bf1}$. Orthogonality and the unit norm of every sign-diagonal matrix imply $|\Phi_H|\le1$. Distinct paths give distinct Fourier monomials, and every row of $H$ has squared entries summing to 1. Thus

$$
 \mathbb E_{\mathcal U}\Phi_H=0,\qquad
 \mathbb E_{\mathcal U}\Phi_H^2
   =\frac1{m^2}\sum_{p\in[m]^k}\prod_{r<k-1}H_{p_{r+1},p_r}^2
   =\frac1m.
\tag{16}
$$

The last path sum equals $m$ by summing successively from $p_0$ through $p_{k-2}$. This proves the second moment without a tail estimate for the hard distribution.
<!-- /passage:general-moments -->

<!-- passage:positive-mean -->
**Lemma 7.** For every orthogonal $H$,

$$
 \mathbb E_{\mathcal D_H}\Phi_H\ge18^{-(k-1)}.
\tag{17}
$$

*Proof.* For each path, $\partial_{S_p}\Phi_H=m^{-1}\prod_{r<k-1}H_{p_{r+1},p_r}$ is constant. Applying (12) to $g=\Phi_H$ therefore replaces each matrix entry by its square. For the Gaussian pair $U_r(p_r),V_r(p_{r+1})$, both marginal second moments equal 1. They need not be independent. Jensen's inequality for the exponential and concavity of the logarithm give

$$
 \begin{aligned}
 \mathbb E[\Psi(U)\varphi'(V)]
 &=\frac32\mathbb E\exp\!\left(-\tfrac12\ln(2+U^2)-\tfrac52\ln(2+V^2)\right)\\
 &\ge\frac32\exp\!\left(-\tfrac12\mathbb E\ln(2+U^2)-\tfrac52\mathbb E\ln(2+V^2)\right)
 \ge\frac1{18}.
 \end{aligned}
\tag{18}
$$

Indeed, each logarithmic expectation is at most $\ln3$. The logarithms are integrable since they are bounded below and bounded above by a constant plus the squared variable. The Gaussian layers indexed by $r$ are independent, so the expectations of the layer factors multiply for a fixed path. The squared path coefficients sum to $m$, as in (16). Formula (17) follows. ∎
<!-- /passage:positive-mean -->

<!-- passage:promise-gap -->
Return to Walsh $H$, put $a=18^{-(k-1)}$, and define

$$
 p=\frac{a-\delta}{1-\delta},\qquad
 q=\min\left\{1,\frac4{m\delta^2}\right\},\qquad
 \Gamma(\varepsilon)=(1-\varepsilon)p-\varepsilon-q.
\tag{19}
$$

**Lemma 8.** If $A(z)\in[0,1]$ is the acceptance probability of an algorithm with error at most $\varepsilon\in[0,1]$ on the promise, then

$$
 \mathbb E_{\mathcal D_H}A-\mathbb E_{\mathcal U}A
     \ge\Gamma(\varepsilon).
\tag{20}
$$

*Proof.* Since $\Phi\le1$, its mean is at most $\delta+(1-\delta)\Pr_{\mathcal D_H}(\Phi\ge\delta)$. Equation (17) makes this positive-promise probability at least $p$. On that event $A\ge1-\varepsilon$, and elsewhere $A\ge0$. Under the uniform law, (16) and Markov's inequality give $\Pr(|\Phi|>\delta/2)\le q$. On its complement $A\le\varepsilon$, and everywhere $A\le1$, so $\mathbb E_{\mathcal U}A\le\varepsilon+q$. Subtract these two estimates. ∎

Neither distribution is asserted to be supported on the promise. This is why error reduction is needed before comparing their acceptance probabilities. Large negative values of $\Phi$ remain outside the promise, as in the original definition.
<!-- /passage:promise-gap -->

## 5. Error reduction

<!-- passage:amplification -->
Suppose a randomized depth-$L$ tree is correct on every promised input with probability at least $(1+\eta)/2$, where $0<\eta\le1$. Run it independently $2\tau$ times, for an integer $\tau\ge1$, and take a majority, resolving ties in any fixed way. The depth is at most $2\tau L$, and the error satisfies

$$
 \varepsilon_\tau\le(1-\eta^2)^\tau\le e^{-\tau\eta^2}.
\tag{21}
$$

*Proof.* For $\eta<1$, let $W_i$ indicate an erroneous run on one fixed promised input and put $r=(1-\eta)/2$. Count a tie as an error. For $\lambda>0$, exponential Markov gives $\Pr(\sum_{i=1}^{2\tau}W_i\ge\tau)\le e^{-\lambda\tau}(1-r+re^\lambda)^{2\tau}$. Choosing $e^\lambda=(1+\eta)/(1-\eta)$ gives $(1-\eta^2)^\tau$. The bound is uniform over promised inputs. For $\eta=1$ every run is correct. The final exponential estimate follows from $1-u\le e^{-u}$. ∎

When the original error is $1/3$, one has $\eta=1/3$ and the first bound is $(8/9)^\tau$. The corresponding formal lemma `exists_amplified` uses $2\tau$ repetitions. Averaging a deterministic-tree bound over the finite mixture of amplified trees preserves that bound.
<!-- /passage:amplification -->

## 6. An elementary Fourier estimate under bias

<!-- passage:elementary-growth -->
**Lemma 9.** Let $n\ge1$, and let $T:\{-1,1\}^n\to[0,1]$ be computed by a deterministic decision tree of depth at most $d\ge1$, with real leaves in $[0,1]$. Let $|\mu_i|\le1/2$. For every integer $j\ge1$ and every family $\mathcal F$ of distinct $j$-element coordinate sets,

$$
 \sum_{S\in\mathcal F}|\partial_S\widetilde T(\mu)|
 \le(16jd\ln(4n))^{j/2}+2^{-j}.
\tag{22}
$$

*Proof.* Under the product measure of means $\mu$, set $\xi_i=(X_i-\mu_i)/(1-\mu_i^2)$. These variables are independent, centered, and bounded by 2 in absolute value. Direct summation in one coordinate, then iteration over distinct coordinates, gives $\partial_S\widetilde T(\mu)=\mathbb E_\mu[T(X)\prod_{i\in S}\xi_i]$. Set $c(S)$ equal to the sign of this derivative for $S\in\mathcal F$, and zero for the other $j$-element sets.

For any coefficient array of degree $r$ bounded by 1, and any set $Q$ of revealed coordinates, define the chaos $Y_r^c(Q)=\sum_{S\subseteq Q,\ |S|=r}c(S)\prod_{i\in S}\xi_i$. Let $Q_i$ be the coordinates revealed after $i$ queries, held fixed after an early leaf so every process has horizon $d$. If a new coordinate $u$ is queried, its increment is $\xi_uY_{r-1}^{c^u}(Q)$, where $c^u(S)=c(S\cup\{u\})$ for $u\notin S$ and is zero otherwise. This increment has conditional mean zero. A repeated query gives a zero increment.

Fix $\Lambda>0$ and put $K=\sqrt{8d\Lambda}$. We prove by induction on $r$ the maximal bound

$$
 \Pr\!\left(\max_{i\le d}|Y_r^c(Q_i)|>K^r\right)
       \le(4n)^r e^{-\Lambda}.
\tag{23}
$$

For $r=0$ the event is empty. For the induction step, stop the degree-$r$ martingale before a query whenever one of the $n$ contracted degree-$(r-1)$ chaoses exceeds $K^{r-1}$. Prior to stopping, its increments have absolute value at most $2K^{r-1}$. The conditional exponential inequality for a centered $Z$ with $|Z|\le D$ is $\mathbb E[e^{\lambda Z}\mid\mathcal F]\le e^{\lambda^2D^2/2}$: bound the exponential by its secant on $[-D,D]$ and use $\cosh u\le e^{u^2/2}$, which follows term by term from their power series.

For the stopped martingale $Z_i$, with $Z_0=0$, put $M_i=\exp(\lambda Z_i-\lambda^2D^2i/2)$. The conditional inequality gives $\mathbb E[M_{i+1}\mid\mathcal F_i]\le M_i$. Let $\sigma$ be the first time that $Z_i>R$, capped at $d$. Iterated conditioning for $M_{\min(i,\sigma)}$ gives $\mathbb E M_\sigma\le1$. On crossing, $M_\sigma\ge\exp(\lambda R-\lambda^2D^2d/2)$, so the crossing probability is at most $\exp(-\lambda R+\lambda^2D^2d/2)$. Taking $\lambda=R/(dD^2)$ gives the claimed maximal bound $e^{-R^2/(2dD^2)}$.

Taking $R=K^r$ and $D=2K^{r-1}$, the bound for both signs is $2e^{-\Lambda}$. The induction hypothesis and a union bound give stopping probability at most $n(4n)^{r-1}e^{-\Lambda}$. Their sum is at most $(4n)^re^{-\Lambda}$ for $n,r\ge1$, proving (23). The use of a stopped process matters: conditioning on all the increment bounds would not preserve the martingale argument.

At a leaf, the unrevealed coordinates retain their product distribution and their centered means. The conditional expectation of the full degree-$j$ chaos is therefore its restriction to the set queried along that leaf. Since $T$ is constant on a leaf, the sum in (22) equals $\mathbb E[T(X)Y_j^c(Q_d)]$. On the good event its absolute value is bounded by $K^j$. On every outcome, $|Y_j^c(Q_d)|\le(2n)^j$. Consequently the sum is at most $K^j+(2n)^j(4n)^je^{-\Lambda}$. Choose $\Lambda=2j\ln(4n)$. The latter term becomes $2^{-j}$ and $K^2=16jd\ln(4n)$, proving (22). ∎

This is the standard decision-tree argument of Girish, Tal and Wu (2021), §1.3 and Lemma 1.9, carried out under a bounded biased measure. The supplied Lean development has a parameterized version in `sum_abs_ext_Dl_le`. The numerical specialization (22), including its smaller residual term, has not been compiled as a new declaration here.
<!-- /passage:elementary-growth -->

## 7. Quantitative consequences

<!-- passage:finite-elementary -->
Let an algorithm for $P_{k,m}$ have depth $L\ge1$ and success at least $(1+\eta)/2$. Amplify it $2\tau$ times and take any upper bound $\varepsilon\in[0,1]$ from (21). Combining (15), (20), and (22), and then averaging over the random coins, gives the finite inequality

$$
 \Gamma(\varepsilon)\le
 \left(\frac b{\sqrt m}\right)^{k-1}
 \left[(32k\tau L\ln(4km))^{k/2}+2^{-k}\right].
\tag{24}
$$

No asymptotic limit or unspecified threshold occurs in (24). If $L=0$, the acceptance function is constant, so a positive $\Gamma$ already gives a contradiction.
<!-- /passage:finite-elementary -->

<!-- passage:elementary-proof -->
*Proof of Theorem 2.* Suppose that $L$ is at most the right side of (4). Choose $\tau=25k$. The integer inequality $18\cdot8^{25}<9^{25}$ gives $\varepsilon\le18^{-k}=a/18$. Also $\delta\le a/32$, and $m\ge2^{15k+2}$ gives $q\le\delta$. Since $0<p\le1$, (19) gives $\Gamma\ge p-2\varepsilon-q\ge a-2\delta-2\varepsilon\ge119a/144>3a/4$. Hence $L>0$.

The assumption on $L$ implies $800k^2L\ln(4km)\le(8/27)^2m^{1-1/k}$. Using $b(8/27)=1/18$, the main term on the right side of (24) is at most $(8/27)a$. Its remaining term is at most $a/4$, since $2^{-k}\le1/4$ and $b/\sqrt m\le1/18$. Their sum is $59a/108<3a/4$, contradicting the preceding lower bound. ∎
<!-- /passage:elementary-proof -->

<!-- passage:restriction-transfer -->
For the sharper Fourier theorem we first pass from uniform to biased derivatives. Independently in each coordinate, leave the variable free with probability $v_i>0$, fix it to $+1$ with probability $(1-v_i+\mu_i)/2$, and fix it to $-1$ with probability $(1-v_i-\mu_i)/2$. This is a probability distribution whenever $|\mu_i|\le1-v_i$. Write $g_\rho$ for the resulting restriction, still regarded as a function of $n$ variables that ignores the fixed ones. Expanding (5) monomial by monomial gives

$$
 \mathbb E_\rho\widehat {g_\rho}(S)
        =\left(\prod_{i\in S}v_i\right)\partial_S\widetilde g(\mu).
\tag{25}
$$

Indeed, a monomial contributes precisely when all coordinates in $S$ stay free, contributing the displayed product, and every coordinate of the monomial outside $S$ is fixed, whose signed expectation is $\mu_i$. The constant choice $v_i=1/2$ is Wu's (2021) Lemma 2.2, in raw-derivative notation. Taking absolute values before summing bounds derivative weight by the corresponding uniform weight of restrictions.

At $\mu=w_s$, choose $v_i=1/2$ in the endpoint blocks and $v_i=3/4$ in the intermediate blocks. For every path $S_p$ the product is $(1/4)(3/4)^{k-2}$. Every restricted tree still has depth at most $d$. Applying (2) to each restriction yields

$$
 \sum_{p\in[m]^k}|\partial_{S_p}\widetilde T(w_s)|
 \le4(4/3)^{k-2}C^k\sqrt{\binom d k}\,
                 (1+\ln(km))^{(k-1)/2}.
\tag{26}
$$
<!-- /passage:restriction-transfer -->

<!-- passage:finite-sharp -->
Since $b^{k-1}4(4/3)^{k-2}=3/4^{k-1}$, the sharper counterpart of (24) is

$$
 \Gamma(\varepsilon)\le
 \frac{3C^k}{4^{k-1}}\sqrt{\binom{2\tau L}{k}}
      \left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
\tag{27}
$$

This is the strongest finite inequality established by this calculation before relaxing the binomial coefficient. If $\Gamma>0$, it first forces $2\tau L\ge k$. Applying $\binom{2\tau L}k\le(2e\tau L/k)^k$ and rearranging gives

$$
 L\ge\frac{k}{2e\tau C^2}
       \left(\frac{\Gamma(\varepsilon)4^{k-1}}3\right)^{2/k}
       \left(\frac m{1+\ln(km)}\right)^{1-1/k}.
\tag{28}
$$

One may choose any $\tau\ge1$ and any valid amplification bound in (27). Optimizing them can improve numerical constants and the convenient size threshold. It does not require a new interpolation identity.
<!-- /passage:finite-sharp -->

<!-- passage:sharp-proof -->
*Proof of Theorem 1.* Choose $\tau=\lceil5k\ln2/\eta^2\rceil$. Then (21) gives $\varepsilon\le\delta$, and $\tau\le(5\ln2+1/2)k/\eta^2<4k/\eta^2$. The size hypothesis gives $q\le\delta$. Since $(1-\delta)p=a-\delta$, we get $\Gamma\ge a-3\delta\ge29a/32$. Therefore

$$
 \left(\frac{\Gamma4^{k-1}}3\right)^{2/k}
 \ge\frac4{81}\left(\frac{87}{64}\right)^{2/k}
 \ge\frac4{81}.
\tag{29}
$$

Substituting this and the upper bound for $\tau$ into (28) proves (3). ∎

The factor $k$ in the numerator of (28) comes from $\sqrt{\binom d k}$. It cancels the linear cost in $k$ of error reduction. Using Tal's earlier $C_T^kd^{k/2}(1+\ln n)^{(k-1)/2}$ estimate leaves a factor $k^{-1}$. Using (22) leaves $k^{-2}$ and replaces the logarithmic denominator power $1-1/k$ by 1. These are three different consequences of the same identity.
<!-- /passage:sharp-proof -->

## 8. Formal correspondence and scope

<!-- passage:formal-boundary -->
For $m=4^t$, (1) agrees with the frozen `QuarticQuery.Phi`, and the promise agrees with `QuarticQuery.P`. The supplied theorem `QuarticQuery.ForrelationLower.bansalSinhaLower` proves the corpus statement `lem-2.1.i`: for each fixed $k\ge2$, all sufficiently large $t$ satisfy $R(P_{k,4^t})>\lfloor(4^t)^{1-1/k}/(\log_2 4^t)^2\rfloor$. The Forrelation proof follows the alternative route reconstructed here; the original preprint imports that lower bound from Bansal and Sinha.

The new endpoints (3) and (4) do not follow merely by unpacking the existential threshold in that theorem. Their proofs use quantitative intermediate statements, sharpen the edge bound, and, for (3), import (2). The integral form (12) also differs from the existing exported mean-value form, which asserts the existence of one $s\in(0,1)$. The complete correspondence, proposed statements and outstanding formal obligations are in `correspondence.json`, `NEW_STATEMENTS.json` and `LEAN_GAPS.md`. The source inspection found no error in the blockwise mathematical argument. Lean and Comparator were not rerun in this environment; the attached trace records earlier local runs.

The absence of an explicit inverse polynomial in $k$ in (3) is relative to the block size $m$. In terms of the total input length $n=km$, its right side is $(\eta^2/(162eC^2))[n/(k(1+\ln n))]^{1-1/k}$. The threshold also restricts $k$ to at most $(\log_2m-2)/15$. These restrictions are part of the quantitative statement.
<!-- /passage:formal-boundary -->

<!-- passage:limitations -->
Orthogonality is used to make the zero endpoint uniform and to compute the second moment. Entrywise smallness is used in the advantage estimate (15). The argument does not require the stronger random-matrix properties used in Tal's moment analysis; in particular the sharp decision-tree theorem (2) can be used for Walsh Forrelation independently of the random-orthogonal application in Sherstov, Storozhenko and Wu.

The promised mean supplied by (17) decays exponentially with $k$. Error reduction is consequently part of this proof, even at constant initial error. A method proving a sufficiently strong concentration statement for the hard distribution might alter that cost or the size threshold. No such concentration statement is assumed here. The logarithmic factor in (3) comes from (2); the present calculation does not establish its optimality for this particular promise problem.
<!-- /passage:limitations -->

## References used in the proof

- **Aaronson and Ambainis (2018).** *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing*. SIAM Journal on Computing 47(3), 982–1038. [arXiv:1411.5729](https://arxiv.org/abs/1411.5729). Definition of the Forrelation family and its query-complexity context.
- **Bansal and Sinha (2020; STOC 2021).** *$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity*. [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3). Theorem 1.3, Corollary 1.4, Theorems 3.2–3.4, Lemma 4.3 and §5.3.
- **Sherstov, Storozhenko and Wu (2023).** *An Optimal Separation of Randomized and Quantum Query Complexity*. SIAM Journal on Computing 52(2), 525–567. [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4). Theorem 1.9, Theorem 4.13 and Corollary 4.14; logarithm convention in §2.1.
- **Girish, Tal and Wu (2021).** *Fourier Growth of Parity Decision Trees*. CCC 2021, LIPIcs 200, 39:1–39:36. [DOI](https://doi.org/10.4230/LIPIcs.CCC.2021.39). Standard-decision-tree argument in §1.3 and Lemma 1.9; maximal martingale estimates in §3.2.
- **Tal (2019; FOCS 2020).** *Towards Optimal Separations between Quantum and Randomized Query Complexities*. [arXiv:1912.12561](https://arxiv.org/abs/1912.12561). The single-level question in §1.3, Fourier growth in Theorem 5.1, and the Walsh obstruction to the separate moment method after Definition 5.5.
- **Wu (2021).** *Analyzing XOR-Forrelation through Stochastic Calculus*. [arXiv:2109.02732](https://arxiv.org/abs/2109.02732). Lemma 2.2 and Theorem 3.2.
- **Chattopadhyay, Gaitonde, Lee, Lovett and Shetty (2021).** *Fractional Pseudorandom Generators from Any Fourier Level*. [arXiv:2008.01316v3](https://arxiv.org/abs/2008.01316v3). Single-level control for restriction-closed families, a related antecedent with a different construction.
- **OpenAI (2026).** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026. Supplied preprint, equations (3)–(5) and Lemma 2.1(i). Its total-function construction and theorem are OpenAI's; the present note concerns the alternative proof of its Forrelation input.

Bibliographic records and the broader dated search are supplied in `references.bib` and `prior_art.json`.
