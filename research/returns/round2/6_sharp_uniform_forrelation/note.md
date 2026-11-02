**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Uniform lower bounds for k-Forrelation from a single-block interpolation

<!-- passage:abstract -->
**Abstract.** For the usual $k$-Forrelation promise with threshold $32^{-k}$, we prove a randomized query lower bound of
$\eta^2(162eC^2)^{-1}[m/(1+\ln(km))]^{1-1/k}$ at success probability $(1+\eta)/2$, uniformly for $k\ge2$ and powers of two $m\ge24k\,32^{2k}$. Here $C$ is the absolute constant in the Fourier-weight theorem of Sherstov, Storozhenko and Wu. A self-contained Fourier estimate gives the numerical bound
$R_{1/3}>(2/18225)m^{1-1/k}/[k^2\ln(4km)]$ in the same range. Scaling one endpoint of a rounded Gaussian chain produces only derivatives of order $k$, evaluated at bounded biases. A coordinate-dependent restriction identity transfers the published Fourier bound to those derivatives. Conditioning on all blocks except one endpoint gives a subgaussian estimate that reduces the sufficient dimension threshold. We also isolate a logarithmic error in §5.4 of Bansal and Sinha's full preprint and give a replacement proof in the stated dimension range.
<!-- /passage:abstract -->

## 1. Definitions and results

<!-- passage:definition -->
Let $k\ge2$, let $m=2^r$ for an integer $r\ge0$, and let $H$ be the normalized Walsh matrix of order $m$. Thus $H_{a,b}=m^{-1/2}(-1)^{a\cdot b}$, with rows and columns indexed by $r$-bit strings. For $z=(z_0,\ldots,z_{k-1})\in\{-1,1\}^{km}$, define
\[
 \Phi(z)=\frac1m\sum_{p\in[m]^k}
       \prod_{j=0}^{k-1}z_j(p_j)
       \prod_{j=0}^{k-2}H_{p_{j+1},p_j},
 \qquad \delta=32^{-k}.                                      \tag{1}
\]
The partial Boolean function $P_{k,m}$ takes value $1$ when $\Phi\ge\delta$, takes value $0$ when $|\Phi|\le\delta/2$, and is undefined elsewhere. In particular, large negative values of $\Phi$ are outside the promise. The total input length is $n=km$; $m$ is the size of one block. This is the promise of Bansal and Sinha, Theorem 1.3, and of the supplied OpenAI preprint, equations (3)–(4). In the supplied statement list these definitions are eq-3 and eq-4.

Write $R_\varepsilon(P)$ for the minimum worst-case number of bit queries of a randomized decision tree with error at most $\varepsilon$ on every promised input. The worst case includes the algorithm's random coins. All logarithms below are natural. For comparison with the supplied Lean definitions we restrict to $m=4^t$; the mathematical arguments work for every power of two.
<!-- /passage:definition -->

<!-- passage:ssw-input -->
Fix an absolute constant $C\ge1$ such that every Boolean-valued decision tree $T$ of depth at most $d$ on $n$ sign variables satisfies
\[
 \sum_{|S|=j}|\widehat T(S)|
 \le C^j\sqrt{\binom dj}\,(1+\ln n)^{(j-1)/2},
 \qquad 1\le j\le n.                                        \tag{2}
\]
Such a constant exists by Sherstov, Storozhenko and Wu (2023), Corollary 4.14, printed p. 35 of arXiv:2008.10223v4. Their Corollary 4.15 allows arbitrary leaves in $[-1,1]$. The introductory Theorem 1.9 uses base-two logarithms; Corollary 4.14 already has the convention in (2). The statement leaves $C$ numerical but unspecified.
<!-- /passage:ssw-input -->

<!-- passage:sharp-result -->
**Theorem 1.** Let $C$ satisfy (2). For every integer $k\ge2$, every power of two $m\ge24k\,32^{2k}$, and every $0<\eta\le1$,
\[
 R_{(1-\eta)/2}(P_{k,m})\ge
 \frac{\eta^2}{162eC^2}
 \left(\frac{m}{1+\ln(km)}\right)^{1-1/k}.                    \tag{3}
\]
The conclusion also holds under the smaller, nonintegral sufficient threshold
\[
 m\ge 8\,32^{2k}\ln\!\left(8\,18^{k-1}\right).               \tag{4}
\]
The theorem is proved below using the published estimate (2). Its full quantitative statement and the new tail argument have not been compiled in Lean.
<!-- /passage:sharp-result -->

<!-- passage:elementary-result -->
**Theorem 2.** For every integer $k\ge2$ and every power of two satisfying either dimension condition in Theorem 1,
\[
 R_{1/3}(P_{k,m})>
 \frac{2}{18225}\,
 \frac{m^{1-1/k}}{k^2\ln(4km)}.                              \tag{5}
\]
Its proof uses an elementary stopped-martingale argument in place of (2). In particular, (5) holds under the earlier sufficient condition $m\ge2^{15k+2}$. The constant $2/18225$ survives the padded depth $50kL+1$ used by the supplied formal development.
<!-- /passage:elementary-result -->

<!-- passage:scope -->
Theorems 1 and 2 concern the same promise problem. Their constants and dimension restrictions are part of their statements. In terms of the input length $n=km$, the right side of (3) is
\[
 \frac{\eta^2}{162eC^2}
 \left(\frac{n}{k(1+\ln n)}\right)^{1-1/k}.                  \tag{6}
\]
Thus the absence of an additional inverse polynomial in $k$ is a statement relative to block size $m$. The proof gives no optimality claim for the remaining logarithm or for its numerical constants.

The argument uses the Gaussian-chain construction of Bansal and Sinha with an algebraic truncation and a single scaled block. The Fourier estimates are due to Tal, Sherstov–Storozhenko–Wu, and Girish–Tal–Wu in the forms specified below. The coordinate-dependent restriction calculation generalizes the identity recorded by Xinyu Wu. The supplied development contains the fixed-$k$ formal proof that motivated this reconstruction; no priority claim about the new quantitative deductions is made.

We first prove the interpolation identity, then the probability estimates. Sections 4–6 supply the restriction, Fourier and amplification bounds. Section 7 assembles the constants. Section 8 states what the comparison with Bansal and Sinha establishes.
<!-- /passage:scope -->

## 2. The interpolation identity

<!-- passage:extension -->
For $g:\{-1,1\}^n\to\mathbb R$, its multilinear extension is
\[
 \widetilde g(\mu)
   =\sum_{x\in\{-1,1\}^n}g(x)\prod_{i=1}^n\frac{1+\mu_i x_i}{2}
   =\sum_{S\subseteq[n]}\widehat g(S)\prod_{i\in S}\mu_i.      \tag{7}
\]
For $\mu\in[-1,1]^n$, it is the expectation under independent signs with means $\mu_i$. Both identities follow by expanding finite products. For a set $S$ of distinct coordinates, $\partial_S$ denotes one derivative in each coordinate. These are unnormalized derivatives. In particular, every repeated partial derivative $\partial_i^2\widetilde g$ vanishes.
<!-- /passage:extension -->

<!-- passage:kernel -->
**Lemma 3.** Put
\[
 \psi(x)=\frac1{2\sqrt{2+x^2}},\qquad
 \varphi(x)=\frac{x(3+x^2)}{2(2+x^2)^{3/2}}.
\]
Then $\varphi$ is odd,
\[
 \varphi'(x)=\frac3{(2+x^2)^{5/2}},\qquad
 |\varphi(x)|\le\frac12,\qquad
 0<\psi(x)\varphi'(y)\le\frac3{16}                           \tag{8}
\]
for all real $x,y$. The product bound is attained at $x=y=0$.

*Proof.* Differentiation gives the first formula. The function is increasing, with limits $\pm1/2$. An algebraic check of the bound is
$(2+u)^3-u(3+u)^2=8+3u>0$ for $u=x^2\ge0$. The two positive denominators are minimized at zero, giving
$\psi(x)\le1/(2\sqrt2)$ and $\varphi'(y)\le3/(4\sqrt2)$. Their product is at most $3/16$. We use $b=3/16$ below. ∎
<!-- /passage:kernel -->

<!-- passage:stein -->
**Lemma 4.** If $Z$ is standard normal and $G,G'$ are bounded and continuous, with $G$ continuously differentiable, then
\[
 \mathbb E[\varphi(Z)G(Z)]
   =\mathbb E[\psi(Z)G'(Z)].                                \tag{9}
\]
*Proof.* Direct differentiation gives $\varphi=x\psi-\psi'$. If $\gamma$ is the standard normal density, then $(\psi\gamma)'=-\varphi\gamma$. Integrate $(\psi G\gamma)'$ over $[-M,M]$ and let $M$ tend to infinity. The boundary term vanishes, and the two integrands are bounded by a constant times $\gamma$. Dominated convergence proves (9). The same proof applies conditionally in a coordinate of a vector of independent standard normals. ∎
<!-- /passage:stein -->

<!-- passage:chain -->
For the next two sections, $H$ may be any real orthogonal matrix of order $m$. Take independent standard Gaussian vectors $U_0,\ldots,U_{k-2}$ and put $V_j=HU_j$. For $s\in[0,1]$, define the bias vector $w_s$ by
\[
 \begin{aligned}
 w_s(0,a)&=s\varphi(U_0(a)),\\
 w_s(j,a)&=\varphi(V_{j-1}(a))\varphi(U_j(a))
                    &&(1\le j\le k-2),\\
 w_s(k-1,a)&=\varphi(V_{k-2}(a)).
 \end{aligned}                                             \tag{10}
\]
Endpoint biases have magnitude at most $1/2$, and intermediate biases have magnitude at most $1/4$. Conditional on these Gaussians, draw independent signs with means $w_1$. Call their unconditional distribution $\mathcal D_H$. Write $\mathcal U$ for the uniform distribution on the sign cube.
<!-- /passage:chain -->

<!-- passage:zero-endpoint -->
**Lemma 5.** For every function $g$ on the sign cube,
\[
 \mathbb E_U\widetilde g(w_0)=\widetilde g(0)
                           =\mathbb E_{\mathcal U}g.        \tag{11}
\]
*Proof.* At $s=0$, the first block is zero. In each surviving monomial, $U_0$ occurs only through the next block. Orthogonality makes the coordinates of $V_0$ independent standard normals, so the coordinates of $\varphi(V_0)$ are independent and centered. Conditional on the later Gaussian layers, every monomial using this next block has expectation zero. Integrating $U_0$ therefore replaces that block by zero. Repeat the same argument with $U_1$, then the remaining layers. Only the constant coefficient of $g$ survives. ∎
<!-- /passage:zero-endpoint -->

<!-- passage:path-identity -->
For $p=(p_0,\ldots,p_{k-1})\in[m]^k$, let $S_p$ be the set containing coordinate $(j,p_j)$ in each block, and define
\[
 A_p(U)=\prod_{j=0}^{k-2}
    H_{p_{j+1},p_j}\psi(U_j(p_j))\varphi'(V_j(p_{j+1})).
\]
**Proposition 6.** For every function $g$ on the sign cube and every orthogonal $H$,
\[
 \mathbb E_{\mathcal D_H}g-\mathbb E_{\mathcal U}g
   =\int_0^1\sum_{p\in[m]^k}
       \mathbb E_U\!\left[A_p(U)\,
                    \partial_{S_p}\widetilde g(w_s)\right]\,ds.       \tag{12}
\]
*Proof.* Let $h(s)=\mathbb E_U\widetilde g(w_s)$. The integrand is a polynomial in $s$ with bounded random coefficients. Thus
$h'(s)=\sum_a\mathbb E[\varphi(U_0(a))\partial_{(0,a)}\widetilde g(w_s)]$.
Apply (9) in $U_0(a)$. Differentiation through block $0$ produces a repeated derivative and vanishes. Differentiation through block $1$ gives
$H_{b,a}\varphi'(V_0(b))$ and the next derivative $\partial_{(1,b)}$; when that block is intermediate, it also gives $\varphi(U_1(b))$.

The accumulated factor now depends only on $U_0$. Applying (9) in $U_1(b)$ leaves that factor unchanged. Differentiation through coordinate $(1,b)$ again vanishes because it repeats a derivative. Differentiation through the next block supplies one further matrix entry, one derivative of $\varphi$, and the factor from the next Gaussian layer. This induction continues through the final block. At every stage, the accumulated weight depends only on Gaussian layers already processed.

All applications of (9) are justified by boundedness: the extension is a polynomial on a compact bias cube, its finitely many derivatives are bounded there, and $\varphi$, $\varphi'$ and the finite matrix entries bound its one-coordinate derivatives. The induction gives the integrand in (12) for $h'(s)$. Integrate from $0$ to $1$ and use (11). ∎
<!-- /passage:path-identity -->

<!-- passage:worked-chain -->
For $k=3$, the biases are
$(s\varphi(U),\,\varphi(HU)\varphi(U'),\,\varphi(HU'))$.
The two integrations by parts give the summand
\[
 H_{b,a}H_{c,b}\,
 \mathbb E\!\left[
   \psi(U_a)\varphi'((HU)_b)
   \psi(U'_b)\varphi'((HU')_c)
   \partial_{(0,a),(1,b),(2,c)}\widetilde g(w_s)\right].        \tag{13}
\]
The factor $\varphi(U'_b)$ produced by the first integration occurs at the coordinate just differentiated. This is what makes the repeated derivative disappear at the next step.

The derivatives in (12) have order $k$ at a biased point. Expanding (7) gives
\[
 \partial_S\widetilde g(\mu)
   =\sum_{T\supseteq S}\widehat g(T)
      \prod_{i\in T\setminus S}\mu_i.                        \tag{14}
\]
Consequently, coefficients at higher uniform Fourier levels can affect the derivative. The estimates below control this dependence uniformly over the relevant biases.
<!-- /passage:worked-chain -->

<!-- passage:advantage -->
For Walsh $H$, $|H_{a,b}|=m^{-1/2}$. Proposition 6 and Lemma 3 imply
\[
 |\mathbb E_{\mathcal D_H}g-\mathbb E_{\mathcal U}g|
 \le\left(\frac b{\sqrt m}\right)^{k-1}
       \sup_{s,U}\sum_{p\in[m]^k}
                 |\partial_{S_p}\widetilde g(w_s)|.          \tag{15}
\]
Each path determines a distinct coordinate set, so the sum has no multiplicity of $k!$. More generally, replace $m^{-1/2}$ by $\max_{a,b}|H_{a,b}|$ for an arbitrary orthogonal matrix.
<!-- /passage:advantage -->

## 3. The two promise probabilities

<!-- passage:moments -->
**Lemma 7.** For the polynomial $\Phi_H$ defined by (1) with an orthogonal matrix $H$,
\[
 |\Phi_H|\le1,\qquad
 \mathbb E_{\mathcal U}\Phi_H=0,\qquad
 \mathbb E_{\mathcal U}\Phi_H^2=\frac1m,\qquad
 \mathbb E_{\mathcal D_H}\Phi_H\ge a:=18^{-(k-1)}.            \tag{16}
\]
*Proof.* In matrix notation,
$m\Phi_H=\mathbf1^{\mathsf T}D_{z_{k-1}}H D_{z_{k-2}}\cdots H D_{z_0}\mathbf1$.
Every sign-diagonal factor and every $H$ is orthogonal. Cauchy–Schwarz and
$\|\mathbf1\|_2=\sqrt m$ prove the first inequality.
Distinct paths in (1) give distinct nonconstant Fourier monomials. Their uniform means vanish, and orthogonality of those monomials reduces the second moment to
$m^{-2}\sum_p\prod_j H_{p_{j+1},p_j}^2=1/m$.
The path sum equals $m$ by successive row-sum-of-squares identities.

For the hard mean, apply (12) to $\Phi_H$. Its derivative along $S_p$ is the constant
$m^{-1}\prod_j H_{p_{j+1},p_j}$, so each matrix entry is squared. For any two jointly Gaussian variables $X,Y$ with standard normal marginals,
\[
 \begin{aligned}
 \mathbb E[\psi(X)\varphi'(Y)]
 &=\frac32\mathbb E\exp\!\left[
      -\tfrac12\ln(2+X^2)-\tfrac52\ln(2+Y^2)\right]\\
 &\ge\frac32\exp\!\left[
      -\tfrac12\mathbb E\ln(2+X^2)-\tfrac52\mathbb E\ln(2+Y^2)\right]
 \ge\frac1{18}.                                            \tag{17}
 \end{aligned}
\]
The first inequality is Jensen's inequality for the exponential; the second uses concavity of $\ln$ and $\mathbb E(2+X^2)=\mathbb E(2+Y^2)=3$. The logarithms are integrable because they are bounded below and grow at most quadratically. Independence of the Gaussian layers multiplies the edge means along a fixed path. The squared path coefficients sum to $m$, proving the last assertion of (16). ∎
<!-- /passage:moments -->

<!-- passage:subgaussian -->
**Lemma 8.** For uniform independent sign blocks and every real orthogonal $H$,
\[
 \mathbb E_{\mathcal U}e^{\lambda\Phi_H}
       \le e^{\lambda^2/(2m)}\quad(\lambda\in\mathbb R),
 \qquad
 \Pr_{\mathcal U}(|\Phi_H|>u)
       \le2e^{-mu^2/2}\quad(u>0).                           \tag{18}
\]
*Proof.* Condition on the first $k-1$ blocks. The last block remains a vector of independent uniform signs, and
$\Phi_H=\sum_{j=1}^m c_jz_{k-1}(j)$.
The coefficient vector is $1/m$ times an orthogonal product applied to the first sign vector. Hence
\[
 \sum_{j=1}^m c_j^2=\frac1m.                                \tag{19}
\]
Conditional independence gives
$\mathbb E[e^{\lambda\Phi_H}\mid z_0,\ldots,z_{k-2}]
 =\prod_j\cosh(\lambda c_j)\le
 \exp(\lambda^2\sum_jc_j^2/2)$.
For completeness, $\cosh v\le e^{v^2/2}$ follows termwise from
$(2r)!\ge2^rr!$. This proves the moment-generating-function bound after averaging.
Exponential Markov with $\lambda=mu$ bounds the upper tail by $e^{-mu^2/2}$. Apply the same argument to $-\Phi_H$ and add. ∎

This estimate concerns the uniform distribution. It requires no concentration theorem for $\mathcal D_H$.
<!-- /passage:subgaussian -->

<!-- passage:gap -->
For the Walsh problem, define
\[
 p=\frac{a-\delta}{1-\delta},\qquad
 q_M=\min\!\left(1,\frac4{m\delta^2}\right),\qquad
 q_*=\min\!\left(1,\frac4{m\delta^2},2e^{-m\delta^2/8}\right).
                                                               \tag{20}
\]
Here $p$ is a lower bound for the positive-promise mass under $\mathcal D_H$. Either $q_M$ or $q_*$ is an upper bound for the uniform mass outside the zero promise.

**Lemma 9.** Let $A:\{-1,1\}^{km}\to[0,1]$ have error at most $\varepsilon\in[0,1]$ on the promise. For either choice of $q$ in (20),
\[
 \begin{aligned}
 \mathbb E_{\mathcal D_H}A-\mathbb E_{\mathcal U}A
 &\ge \Gamma_*(\varepsilon,q)
        :=(1-\varepsilon)(p-q)-\varepsilon\\
 &\ge \Gamma(\varepsilon,q)
        :=(1-\varepsilon)p-\varepsilon-q.                   \tag{21}
 \end{aligned}
\]
*Proof.* By (16), $a\le\delta+(1-\delta)\Pr_{\mathcal D_H}(\Phi\ge\delta)$, which gives $p$. Markov applied to the second moment gives $q_M$; Lemma 8 with $u=\delta/2$ gives the extra term in $q_*$. On the positive promise $A\ge1-\varepsilon$ and elsewhere $A\ge0$. Under the uniform law, $A\le\varepsilon$ on the zero promise and $A\le1$ elsewhere. Thus its uniform mean is at most $\varepsilon+(1-\varepsilon)q$. Subtract. The two gap expressions differ by $\varepsilon q\ge0$. ∎

The quantities in (20) are certified bounds on masses. They need not equal the actual masses. Neither distribution is asserted to be supported on the promise.
<!-- /passage:gap -->

## 4. Coordinate-dependent restrictions

<!-- passage:restriction -->
**Lemma 10.** Let $\mu\in[-1,1]^n$ and let $0\le v_i\le1-|\mu_i|$. Independently in each coordinate, leave $i$ free with probability $v_i$, fix it to $+1$ with probability $(1-v_i+\mu_i)/2$, and fix it to $-1$ with probability $(1-v_i-\mu_i)/2$. Regard each restriction $g_\rho$ as a function of all $n$ variables, ignoring the fixed coordinates. Then for every $S\subseteq[n]$,
\[
 \mathbb E_\rho\widehat{g_\rho}(S)
       =\left(\prod_{i\in S}v_i\right)
          \partial_S\widetilde g(\mu).                     \tag{22}
\]
*Proof.* All probabilities are nonnegative and sum to one. Both sides are linear in $g$, so consider the monomial $\prod_{i\in T}x_i$.
If $S\nsubseteq T$, both sides vanish. Otherwise its coefficient at $S$ after restriction is nonzero exactly when all coordinates in $S$ remain free and all coordinates in $T\setminus S$ are fixed. The signed expectation of a fixed coordinate is
$(1-v_i+\mu_i)/2-(1-v_i-\mu_i)/2=\mu_i$.
Independence gives the product of the free probabilities over $S$ and of $\mu_i$ over $T\setminus S$, as required. ∎

The special case $v_i=1/2$ appears in Xinyu Wu (2021), Lemma 2.2. That source credits earlier restriction identities. Formula (22) is an elementary coordinate-dependent extension.
<!-- /passage:restriction -->

<!-- passage:path-restriction -->
For the biases (10), choose $v_i=1/2$ in the endpoint blocks and $v_i=3/4$ in every intermediate block. Every path $S_p$ has the same free-probability product
$\frac14(\frac34)^{k-2}$.
Taking absolute values in (22), summing over these distinct path sets, and applying (2) to each restricted tree gives
\[
 \sum_p|\partial_{S_p}\widetilde T(w_s)|
 \le4(4/3)^{k-2}C^k\sqrt{\binom dk}
                (1+\ln(km))^{(k-1)/2}.                    \tag{23}
\]
Restrictions do not increase depth. The ambient dimension may remain $km$ even when some coordinates have been fixed; this avoids any empty-domain logarithm convention.
<!-- /passage:path-restriction -->

## 5. An elementary Fourier bound under bias

<!-- passage:growth -->
**Lemma 11.** Let $n,d,j\ge1$. Suppose $T:\{-1,1\}^n\to\{0,1\}$ is computed by a depth-at-most-$d$ deterministic decision tree, $|\mu_i|\le1/2$, and $\mathcal F$ is a family of distinct $j$-element coordinate sets. Then
\[
 \sum_{S\in\mathcal F}|\partial_S\widetilde T(\mu)|
 \le (16jd\ln(4n))^{j/2}+2^{-j}.                            \tag{24}
\]
The argument below is the standard-decision-tree martingale method of Girish, Tal and Kewen Wu (2021), §1.3 and Lemma 1.9, under a bounded biased product measure.
<!-- /passage:growth -->

<!-- passage:growth-proof -->
*Proof.* Under that measure put $\xi_i=(X_i-\mu_i)/(1-\mu_i^2)$. These independent variables are centered and have absolute value at most $2$. Direct averaging in one coordinate, followed by iteration, gives
\[
 \partial_S\widetilde T(\mu)
   =\mathbb E_\mu\!\left[T(X)\prod_{i\in S}\xi_i\right].      \tag{25}
\]
Choose coefficients $c(S)\in\{-1,0,1\}$ to be the signs of these derivatives on $\mathcal F$ and zero on the other $j$-sets.
For any coefficient array of degree $r$ with magnitude at most one, and any revealed set $Q$, let
$Y_r^c(Q)=\sum_{S\subseteq Q,\ |S|=r}c(S)\prod_{i\in S}\xi_i$.
Along the tree, a fresh query $u$ changes it by
$\xi_uY_{r-1}^{c^u}(Q)$, where $c^u(S)=c(S\cup\{u\})$ for $u\notin S$ and is zero otherwise. The increment has conditional mean zero. Repeated queries and steps after a leaf have zero increment, so the process has a common horizon $d$.

Fix $\Lambda>0$ and set $K=\sqrt{8d\Lambda}$. We claim, uniformly over the coefficient arrays,
\[
 \Pr\!\left(\max_{i\le d}|Y_r^c(Q_i)|>K^r\right)
       \le(4n)^re^{-\Lambda}.                              \tag{26}
\]
For $r=0$ the event is empty. For $r\ge1$, stop before the first query for which any of the $n$ contracted degree-$(r-1)$ chaoses exceeds $K^{r-1}$ in magnitude. The stopped martingale has increments bounded by $2K^{r-1}$.

Here is the maximal estimate used for this stopped process. If a centered increment $Z$ satisfies $|Z|\le D$, the secant bound for the exponential gives
$\mathbb E[e^{\lambda Z}\mid\mathcal F]\le\cosh(\lambda D)\le e^{\lambda^2D^2/2}$.
For the partial sums $M_i$, the process
$\exp(\lambda M_i-\lambda^2D^2i/2)$ is a nonnegative supermartingale. Stop at its first crossing of $M_i>R$, capped at $d$. Iterated conditional expectation gives a crossing probability at most
$\exp(-\lambda R+\lambda^2D^2d/2)$.
Minimizing at $\lambda=R/(dD^2)$ gives $e^{-R^2/(2dD^2)}$.
Apply this to both signs with $R=K^r$ and $D=2K^{r-1}$ to obtain $2e^{-\Lambda}$.
The induction hypothesis bounds the probability of stopping by
$n(4n)^{r-1}e^{-\Lambda}$.
Since $2+n(4n)^{r-1}\le(4n)^r$, (26) follows.
This proof stops the process before applying the inequality; conditioning on a favorable future event would not justify the martingale estimate.

At a leaf, unqueried coordinates retain their centered product law. Since $T$ is constant on each leaf, (25) and conditional expectation identify the desired sum with
$\mathbb E_\mu[T(X)Y_j^c(Q_d)]$.
The terminal chaos has magnitude at most $(2n)^j$ everywhere and at most $K^j$ outside the event in (26). Hence
\[
 \sum_{S\in\mathcal F}|\partial_S\widetilde T(\mu)|
 \le K^j+(2n)^j(4n)^je^{-\Lambda}.
\]
Choose $\Lambda=2j\ln(4n)$. The last term is exactly $2^{-j}$ and $K^2=16jd\ln(4n)$, proving (24). ∎
<!-- /passage:growth-proof -->

## 6. Amplification and finite comparisons

<!-- passage:amplification -->
**Lemma 12.** Suppose a depth-$L$ randomized tree succeeds with probability at least $(1+\eta)/2$ on every promised input, where $0<\eta\le1$. For every integer $\tau\ge1$, majority vote on $2\tau$ independent executions has depth at most $2\tau L$ and error at most
\[
 \varepsilon_\tau=(1-\eta^2)^\tau\le e^{-\tau\eta^2}.         \tag{27}
\]
*Proof.* Count ties as errors. For $\eta<1$, the error indicators are independent with probabilities at most $r=(1-\eta)/2$. Exponential Markov bounds the probability of at least $\tau$ errors by
$e^{-\lambda\tau}(1-r+re^\lambda)^{2\tau}$.
The choice $e^\lambda=(1+\eta)/(1-\eta)$ gives the first bound. If $\eta=1$, all executions succeed. Finally, $1-u\le e^{-u}$ gives the second bound. The construction and estimates are uniform over promised inputs. ∎
<!-- /passage:amplification -->

<!-- passage:finite-elementary -->
Take either upper bound $\varepsilon\in[0,1]$ supplied by (27) and either $q$ from (20). Applying Lemma 11 and (15) to each deterministic tree in the amplified mixture gives, for $L\ge1$,
\[
 \Gamma_*(\varepsilon,q)
 \le\left(\frac b{\sqrt m}\right)^{k-1}
     \left[(32k\tau L\ln(4km))^{k/2}+2^{-k}\right].           \tag{28}
\]
The same inequality holds with the smaller $\Gamma$. If $L=0$, the acceptance probability is constant on all inputs, so any strictly positive lower gap is already a contradiction.
One may replace $2\tau L$ by any larger integer depth bound inside the application of (24).
<!-- /passage:finite-elementary -->

<!-- passage:finite-sharp -->
Using (23) in place of Lemma 11, and the identity
$b^{k-1}4(4/3)^{k-2}=3/4^{k-1}$, gives the sharper finite comparison
\[
 \boxed{\quad
 \Gamma_*(\varepsilon,q)
 \le \frac{3C^k}{4^{k-1}}
       \sqrt{\binom{2\tau L}{k}}
       \left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
 \quad}                                                    \tag{29}
\]
This inequality includes all finite parameters, before relaxing the binomial coefficient. In particular, a positive gap forces $2\tau L\ge k$.
For any positive lower bound $\gamma\le\Gamma_*(\varepsilon,q)$, the elementary estimate
$\binom dk\le(ed/k)^k$ yields
\[
 L\ge
 \frac{k}{2e\tau C^2}
 \left(\frac{\gamma4^{k-1}}3\right)^{2/k}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.                   \tag{30}
\]
The binomial estimate follows from $\binom dk\le d^k/k!$ and
$\ln(k!)\ge\int_1^k\ln x\,dx=k\ln k-k+1$.
Equations (28)–(30), with a freely chosen integer $\tau$ and the exact defined gap, are stronger than the simplified uniform corollaries.
<!-- /passage:finite-sharp -->

## 7. Constants and dimension restrictions

<!-- passage:threshold -->
The dimension condition (4) implies
$2e^{-m\delta^2/8}\le a/4$, hence $q_*\le a/4$.
It follows from the simpler integer condition because
\[
 \ln(8/a)=\ln8+(k-1)\ln18<3k,\qquad
 24k\,32^{2k}\le2^{15k+2}\quad(k\ge2).                      \tag{31}
\]
The inequality $\ln18<3$ has the exact certificate
$\sum_{j=0}^6 3^j/j!>18$; $\ln8<3$ follows as well.
For the second comparison, cancel $4\cdot32^{2k}$ and use $6k\le32^k$, proved by induction.
These thresholds also imply $\sqrt m\ge4$, which will suffice for the elementary residual term.
<!-- /passage:threshold -->

<!-- passage:sharp-proof -->
*Proof of Theorem 1.* Set
$\tau=\lceil5k\ln2/\eta^2\rceil$.
Then $\varepsilon_\tau\le\delta$ and
$\tau\le(5\ln2+1/2)k/\eta^2<4k/\eta^2$.
Here $k\ge2$ and $\eta\le1$ absorb the rounding by $1/2$, and
$\ln2<7/10$ follows from
$\sum_{j=0}^4(7/10)^j/j!>2$.
Since $\delta\le a/32$ and $(1-\delta)p=a-\delta$, Lemma 9 gives
\[
 \Gamma(\varepsilon_\tau,q_*)
 \ge a-2\delta-a/4\ge\frac{11a}{16}.                        \tag{32}
\]
For every $\alpha\ge2/3$,
\[
 \left(\frac{\alpha a\,4^{k-1}}3\right)^{2/k}
     =\frac4{81}\left(\frac{3\alpha}{2}\right)^{2/k}
     \ge\frac4{81}.                                        \tag{33}
\]
We may use $\alpha=11/16$, since $3\alpha/2=33/32>1$. Substitute (32)–(33) and the upper bound for $\tau$ into (30). The coefficient is
$(8eC^2)^{-1}(4/81)=1/(162eC^2)$, proving (3). ∎
<!-- /passage:sharp-proof -->

<!-- passage:elementary-proof -->
*Proof of Theorem 2.* Suppose a successful depth-$L$ algorithm satisfies the reverse of (5). At error $1/3$, choose $\tau=25k$. The integer inequality $18\cdot8^{25}<9^{25}$ implies
$\varepsilon_\tau\le(8/9)^{25k}\le a/18$.
Also $\delta\le a/32$, $p\ge a-\delta$ and $p\le1$. Therefore
\[
 \Gamma(\varepsilon_\tau,q_*)
 \ge a-\delta-2\varepsilon_\tau-a/4
 \ge\frac{175a}{288}.                                      \tag{34}
\]
This excludes $L=0$. For $L\ge1$, use the padded depth $d=50kL+1$ in (24). The assumed bound on $L$ gives
\[
 16kd\ln(4km)
 \le \left(\frac8{27}\right)^2
       \left(1+\frac1{50k}\right)m^{1-1/k},                 \tag{35}
\]
because $800(2/18225)=(8/27)^2$.
The padding is uniformly harmless:
\[
 \left(1+\frac1{50k}\right)^k
 \le\sum_{j=0}^k50^{-j}\le\frac{50}{49}
 <\left(\frac98\right)^2.                                  \tag{36}
\]
Indeed, expand the left side and use $\binom kj\le k^j$.
Since $b(8/27)=1/18$, the main term of (28), with this padded depth, is at most
$(8/27)(9/8)a=a/3$.
Its residual term is at most $a/4$: we have
$2^{-k}\le1/4$ and $b/\sqrt m\le1/18$.
Thus the upper advantage is at most $7a/12=168a/288$, contradicting (34). This proves the strict bound in (5). ∎
<!-- /passage:elementary-proof -->

<!-- passage:original-constant -->
The requested $2/18225$ theorem at $m\ge2^{15k+2}$ can also be proved without Lemma 8. That threshold gives $q_M\le\delta$, so the same amplification gives
\[
 \Gamma(\varepsilon_\tau,q_M)
 \ge a-2\delta-2\varepsilon_\tau
 \ge\frac{119a}{144}>\frac{7a}{12}.                         \tag{37}
\]
All the other steps, including the padding estimate, are unchanged. This is the shortest route to formalizing the precise originally requested theorem. The subgaussian lemma then strengthens its dimension range.

The numerical improvement over the uncompiled coarse uniform source is
\[
 \frac{2/18225}{1/2332800}=256.
\]
It is the square of the factor $16$ gained when the edge estimate $3$ is replaced by $3/16$. A formal proof must actually replace that edge estimate in the finite advantage theorem; the existing theorem with the coefficient $3$ cannot be invoked as though it had the sharper coefficient.
<!-- /passage:original-constant -->

<!-- passage:finite-range -->
The condition $q_*\le a/4$ is sufficient and is not necessary. In (29), one can retain $\Gamma_*$ and optimize the integer $\tau$. Even with $\varepsilon\le\delta$, the simpler condition
$q_*\le a/3-2\delta$ suffices for Theorem 1's constant, because it makes $\Gamma\ge2a/3$. Its right side is positive for every $k\ge2$.

There is also an exact limit to what the two stated mass bounds alone can yield. As the amplified error tends to zero, the gap tends to $p-q$. Thus this comparison can give a positive limiting gap precisely when $q<p$. With $q=q_M$ this means
\[
 m>\frac{4(1-\delta)}{\delta^2(a-\delta)}.                   \tag{38}
\]
With the subgaussian term as the chosen bound, it suffices that
$m>8\delta^{-2}\ln(2/p)$.
These are statements about the present probability estimates. A failure of either sufficient condition is not a query algorithm or a lower-bound impossibility theorem.
<!-- /passage:finite-range -->

<!-- passage:small-dimension -->
Some restriction on size is unavoidable for a positive lower bound on this promise. At $m=1$, $\Phi$ is a product of signs and takes only the values $\pm1$. The zero promise is empty, so the function is constantly $1$ on its domain and has randomized query complexity zero.
There is a nontrivial two-dimensional example as well: for $m=2,k=2$, multiplying a sign vector by the Walsh matrix gives one zero coordinate and one coordinate of magnitude $\sqrt2$. Consequently $\Phi$ is always $\pm1/\sqrt2$, again leaving the zero promise empty at $\delta=32^{-2}$.
These examples preclude a literal positive lower bound for every size. They do not address a fixed-$k$, sufficiently-large-$m$ asymptotic statement.
<!-- /passage:small-dimension -->

## 8. Logarithms and comparison with earlier proofs

<!-- passage:comparison -->
Put $B=1+\ln(km)$ and retain the dimension conditions of Theorem 1. Applying three Fourier estimates to the same identity gives the following bounds.

| Fourier input | Lower bound obtained |
| --- | --- |
| Elementary biased martingale estimate (24), at error $1/3$ | $\displaystyle \frac{2}{18225}\frac{m^{1-1/k}}{k^2\ln(4km)}$, strictly |
| Tal's estimate $C_T^k d^{k/2}B^{(k-1)/2}$, for a sufficiently large absolute $C_T$ | $\displaystyle \frac{\eta^2}{162kC_T^2}(m/B)^{1-1/k}$ |
| Sherstov–Storozhenko–Wu estimate (2) | $\displaystyle \frac{\eta^2}{162eC^2}(m/B)^{1-1/k}$ |

For Tal's row, perform the same restriction calculation and inversion with $d^{k/2}$ in place of $\sqrt{\binom dk}$. The factor $k$ in (30) is then absent, yielding the displayed coefficient. The estimate can be obtained directly from Tal (2019), Theorem 5.1; a constant-factor change of the universal constant permits restrictions and the natural-log convention.

The logarithmic denominator power supplied by (2) is $1-1/k$. Its binomial factor also cancels the linear cost in $k$ of amplification. A claim that this logarithm is optimal for $P_{k,m}$ would require a separate argument.
<!-- /passage:comparison -->

<!-- passage:bs-failure -->
Bansal and Sinha's Theorem 1.3 states a scale
$\Omega(k^{-29}\eta^2[m/\log(km)]^{1-1/k})$.
Their full preprint's §5.4 combines Theorem 3.2 and Corollary 3.5 over levels
$k\le\ell\le k(k-1)$.
Writing $L_0=\log(km)$, the third inequality in its final display replaces the exponent $(\ell-1)/2$ of $L_0$ by $\ell(1-1/k)/2$. Their difference is
\[
 \frac{\ell-1}{2}-\frac{\ell(1-1/k)}2
       =\frac{\ell/k-1}{2}.                                \tag{39}
\]
It is positive for $\ell>k$. At the top level the missing factor is
$L_0^{(k-2)/2}$, which is unbounded as $m$ grows at any fixed $k\ge3$.
The original display therefore does not justify its stated logarithmic exponent. Its first two estimates give the valid weaker scale
\[
 \Omega\!\left(
 \frac{\eta^2}{k^{29}}\,
 \frac{m^{1-1/k}}{[\log(km)]^{1-1/[k(k-1)]}}
 \right)                                                   \tag{40}
\]
in a sufficiently large dimension where its promise gap is positive.
The companion audit proves this conclusion, checks the comparison of full sums, and separates the logarithmic issue from a reciprocal typo in equation (5.31).
<!-- /passage:bs-failure -->

<!-- passage:bs-repair -->
Theorem 1 supplies an alternative proof of the desired logarithmic power in its explicit dimension range, with stronger dependence on $k$. The identity (12) uses only order-$k$ biased derivatives, so no higher-level exponent must be replaced by the level-$k$ exponent. Using the SSW theorem inside the original multilevel sum would leave the logarithmic mismatch in (39).

For every fixed $k$, the dimension threshold in Theorem 1 is eventually satisfied, so it recovers the stated fixed-$k$ asymptotic scale. A claim covering every pair $(k,m)$ beyond the explicit range is not established here. In particular, the theorem does not by itself settle any assertion about a growing-$k$ regime outside that range.
<!-- /passage:bs-repair -->

## 9. Formal correspondence

<!-- passage:formal-status -->
The supplied source already contains the multilinear extension, the Stein kernel identity, a mean-value form of the single-block calculation, the zero-endpoint identity, the promise moments for Walsh matrices, a parameterized martingale estimate, amplification at error $1/3$, and the eventual fixed-$k$ lower bound. Its exported identity asserts the existence of one interpolation parameter; the integral formulation (12) is reconstructed above.

The newly proposed statements are the sharp edge and path-coefficient bounds, the specialized logarithmic growth estimate, the exact promise-probability comparison, coordinate-dependent restriction transfer, variable-error amplification, the subgaussian moment and tail estimates, and the uniform quantitative conclusions. The external SSW theorem is an explicit additional formalization obligation. The file Uniform.lean has no compiled output according to the supplied BUILD_STATUS.md; its $1/2332800$ theorem is source text in this review.

No Lean compiler or Lake executable was available on the current PATH, and no Lean, Comparator, or independent-kernel run was performed here. All proposed Lean blocks in the companion blueprint are marked unelaborated. The exact-arithmetic script checks the constant algebra and finite examples; the analytic proofs above supply the universal statements. The correspondence and gap files identify the exact existing declarations used and the new obligations. The original total-function construction and nearly quartic theorem are OpenAI's; this note studies their Forrelation input.
<!-- /passage:formal-status -->

## References

- N. Bansal and M. Sinha, [$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity](https://arxiv.org/abs/2008.07003v3), arXiv v3, 17 November 2020; STOC 2021, pp. 1303–1316, [DOI](https://doi.org/10.1145/3406325.3451040). Theorems 1.3, 3.1, 3.2; Corollary 3.5; Lemma 4.3; §5.4 of the full version.
- A. A. Sherstov, A. A. Storozhenko and P. Wu, [An Optimal Separation of Randomized and Quantum Query Complexity](https://arxiv.org/pdf/2008.10223v4), SIAM Journal on Computing 52(2), 2023, pp. 525–567, [DOI](https://doi.org/10.1137/22M1468943). Theorem 1.9; Corollaries 4.14 and 4.15, printed p. 35 of the cited arXiv PDF. The HTML conversion has different numbering at these locations.
- A. Tal, [Towards Optimal Separations between Quantum and Randomized Query Complexities](https://arxiv.org/abs/1912.12561), arXiv, 2019; FOCS 2020, pp. 228–239, [DOI](https://doi.org/10.1109/FOCS46700.2020.00030). Theorem 5.1 and §1.3.
- U. Girish, A. Tal and K. Wu, [Fourier Growth of Parity Decision Trees](https://doi.org/10.4230/LIPIcs.CCC.2021.39), CCC 2021, LIPIcs 200, 39:1–39:36. Standard-decision-tree argument in §1.3 and Lemma 1.9.
- X. Wu, [Analyzing XOR-Forrelation through Stochastic Calculus](https://arxiv.org/abs/2109.02732), arXiv, 2021; STACS 2022, LIPIcs 219, 60:1–60:7, [DOI](https://doi.org/10.4230/LIPIcs.STACS.2022.60). Lemma 2.2.
- S. Aaronson and A. Ambainis, [Forrelation: A Problem That Optimally Separates Quantum from Classical Computing](https://arxiv.org/abs/1411.5729), SIAM Journal on Computing 47(3), 2018, pp. 982–1038, [DOI](https://doi.org/10.1137/15M1050902). Forrelation family and query-complexity context.
- OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, supplied preprint dated 5 October 2026, equations (3)–(5) and Lemma 2.1(i). The supplied PDF is the version used; no public identifier is inferred.
