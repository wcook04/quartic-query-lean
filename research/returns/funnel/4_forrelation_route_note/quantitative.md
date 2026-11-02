**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# Quantitative strength of the blockwise Stein route

<!-- passage:q-verdict -->
## Verdict and conventions

The conjectured improvement is proved as a mathematical deduction from the blockwise identity. The elementary martingale bound gives a uniform inverse-square dependence on $k$. Tal's Fourier bound gives an inverse-first-power dependence. The sharper Sherstov–Storozhenko–Wu bound gives a universal constant with no inverse polynomial in $k$, because its factor $\sqrt{\binom d k}$ supplies precisely the factor $k$ needed to compensate for amplification. The strong Fourier theorem is an external published input, and the resulting uniform query theorem is a new statement to formalise.

All logarithms in this document are natural. Put

$$

 k\ge2,\quad m=2^r,\quad n=km,\quad \delta=32^{-k},\quad
 a=18^{-(k-1)},\quad b=\frac3{16},\quad B=1+\ln n.

$$

Use the same promise $P_{k,m}$ and complexity notation as note.md, §1: $R_\varepsilon(P)$ is the minimum worst-case depth of a randomized tree with error at most $\varepsilon$ on every promised input. Thus a success guarantee $(1+\eta)/2$ corresponds to $R_{(1-\eta)/2}(P_{k,m})$. For $m=4^t$, $R_{1/3}(P_{k,m})=R(P\,k\,t)$ in the supplied Lean vocabulary. The analytic deductions hold for every power of two; the existing public Lean definitions restrict the formal endpoints to powers of four.

Lemma 3 of note.md, equations (6)–(7), gives the algebraic truncation

$$

 \Psi(x)=\frac1{2\sqrt{2+x^2}},\qquad
 \varphi(x)=\frac{x(3+x^2)}{2(2+x^2)^{3/2}},\qquad
 \varphi'(x)=\frac3{(2+x^2)^{5/2}}.

$$

It satisfies $|\varphi|\le1/2$, $\Psi\le1/(2\sqrt2)$, and $\varphi'\le3/(4\sqrt2)$. Hence every edge weight $\Psi(U)\varphi'(V)$ is at most $b=3/16$. The supplied `abs_cf_le` uses the coarser bounds $1$ and $3$, giving $3$ in place of $b$. All constants involving $b$ below are mathematical refinements of that existing Lean estimate.
<!-- /passage:q-verdict -->

<!-- passage:q-finite-comparison -->
## 1. The exact finite comparison

Let $\mathcal D$ be the rounded hard distribution of note.md, equation (9), with the same orientation of the Walsh matrix. Equations (16)–(18) of that note give

$$

 \mathbb E_{\mathcal D}\Phi\ge a,\qquad
 \mathbb E_{\mathcal U}\Phi^2=\frac1m,\qquad |\Phi|\le1.

$$

The first assertion follows from the same identity applied to $\Phi$: its path coefficients multiply the Gaussian path coefficients to give squares of matrix entries. For each Gaussian pair with unit variances, Jensen's inequality gives

$$

 \begin{aligned}
 \mathbb E[\Psi(U)\varphi'(V)]
 &=\frac32\mathbb E\exp\!\left(-\tfrac12\ln(2+U^2)-\tfrac52\ln(2+V^2)\right)\\
 &\ge\frac32\exp\!\left(-\tfrac12\mathbb E\ln(2+U^2)-\tfrac52\mathbb E\ln(2+V^2)\right)\\
 &\ge\frac32e^{-3\ln3}=\frac1{18}.
 \end{aligned}

$$

The Gaussian layers are independent. For an orthogonal $H$, the sum of squared path weights is $m$; after the leading $1/m$, this gives $a$. Flatness of the Hadamard matrix is needed for the upper bound on individual path weights, and is unnecessary for this mean calculation.

Define the exact lower and upper estimates from note.md, equation (19)

$$

 p=\frac{a-\delta}{1-\delta},\qquad
 q=\min\left(1,\frac4{m\delta^2}\right),\qquad
 \Gamma(\varepsilon)=(1-\varepsilon)p-\varepsilon-q.
 \tag{F1}

$$

Because $\mathbb E\Phi\le\delta+(1-\delta)\Pr(\Phi\ge\delta)$, the hard distribution has positive-promise mass at least $p$. Markov's inequality applied to $\Phi^2$ gives uniform exceptional mass at most $q$. Every acceptance function $A\in[0,1]$ with error at most $\varepsilon$ on the promise therefore satisfies

$$

 \mathbb E_{\mathcal D}A-\mathbb E_{\mathcal U}A\ge\Gamma(\varepsilon).
 \tag{F2}

$$

This is Lemma 8, equation (20), of note.md. It treats inputs outside the promise solely through $0\le A\le1$. It remains valid for every finite $k,m$; it becomes informative when the displayed $\Gamma$ is positive.

Given a depth-$L$ randomized algorithm with success at least $(1+\eta)/2$, where $0<\eta\le1$, and any integer $\tau\ge1$, run it independently $2\tau$ times and take a majority. Counting every tie as an error only enlarges the error event. Chernoff's exponential argument yields

$$

 \varepsilon\le(1-\eta^2)^\tau\le e^{-\tau\eta^2},\qquad d\le2\tau L.
 \tag{F3}

$$

Equation (F3) is note.md, equation (21). For $0<\eta<1$, to see the first bound, let $W_i$ be the indicator of an erroneous run, with $\mathbb E W_i\le(1-\eta)/2$, and apply Markov's inequality to $\exp(\lambda\sum W_i)$ with $e^\lambda=(1+\eta)/(1-\eta)$. The resulting product is $(1-\eta^2)^\tau$. For $\eta=1$, every run is correct. In particular, for $\eta=1/3$, the exact bound is $(8/9)^\tau$, matching `exists_amplified`. Its depth is $2\tau L$.
<!-- /passage:q-finite-comparison -->

<!-- passage:q-elementary-finite -->
### 1.1 Elementary growth, with all constants

For every integer $n\ge1$, depth-$d\ge1$ tree $T$ on $n$ variables with leaf values in $[0,1]$, every bias $|\mu_i|\le1/2$, and any family of distinct $k$-subsets,

$$

 \sum_{S}\left|\partial_S\widetilde T(\mu)\right|
 \le (16kd\ln(4n))^{k/2}+2^{-k}.
 \tag{F4}

$$

This is note.md, Lemma 9, equation (22); §4 below also gives its proof. Applying the blockwise identity and $d\le2\tau L$ yields

$$

 \Gamma(\varepsilon)
 \le \left(\frac b{\sqrt m}\right)^{k-1}
 \left[(32k\tau L\ln(4km))^{k/2}+2^{-k}\right].
 \tag{F5}

$$

Equation (F5) is note.md, equation (24). Its explicit inversion is useful when $m$ is below the convenient uniform threshold. If $T_0=2^{-k}(b/\sqrt m)^{k-1}$ and $\Gamma(\varepsilon)>T_0$, this solves exactly to

$$

 L\ge\frac{m^{1-1/k}}{32k\tau\ln(4km)}
 \left(\frac{\Gamma(\varepsilon)-T_0}{b^{k-1}}\right)^{2/k}.
 \tag{F6}

$$

Equations (F1), (F3), and (F5) are a finite-parameter criterion. They make no implicit threshold assumption. The choice of $\tau$ can be optimised numerically, or left as a free positive integer.
<!-- /passage:q-elementary-finite -->

<!-- passage:q-sharp-finite -->
### 1.2 Sharp Fourier growth

Fix a universal $C\ge1$ for which the Sherstov–Storozhenko–Wu theorem holds in the following natural-log convention:

$$

 \sum_{|S|=k}|\widehat T(S)|
 \le C^k\sqrt{\binom d k}\,(1+\ln n)^{(k-1)/2}.
 \tag{F7}

$$

Their Corollary 4.14 in [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4) gives (F7) directly with natural logarithms. Choose $C$ from that corollary. The introductory Theorem 1.9 writes a base-two logarithm instead; if one starts from its constant $C_2$, the sufficient conversion is $C=C_2/\sqrt{\ln2}$, since $1+\log_2 n\le(1+\ln n)/\ln2$. No conversion is necessary when Corollary 4.14 is used directly. The published universal constant is unspecified. Theorem 4.13 gives intermediate constants $58C_0c_0$, where $C_0$ and $c_0$ themselves come from Theorem 2.5 and Lemma 3.1 without certified numerical values. Thus a fully numerical value for the $C$ in (F7) is not available from the cited statement. Every dependence on it below is displayed. This is equation (2) of note.md.

To transfer (F7), independently leave coordinate $i$ free with probability $p_i$, fix it to $+1$ with probability $(1-p_i+\mu_i)/2$, and fix it to $-1$ with probability $(1-p_i-\mu_i)/2$. These probabilities are valid when $|\mu_i|\le1-p_i$. Expanding in monomials proves

$$

 \mathbb E_\rho\widehat {T_\rho}(S)
 =\left(\prod_{i\in S}p_i\right)\partial_S\widetilde T(\mu).
 \tag{F8}

$$

Equation (F8) is note.md, equation (25). The special choice $p_i=1/2$ is the raw-derivative restriction identity in Wu, [arXiv:2109.02732](https://arxiv.org/abs/2109.02732), Lemma 2.2. It gives the direct factor $2^k$, without having to convert normalised biased Fourier coefficients. At the biases of the blockwise path, the first and last blocks have magnitude at most $1/2$, and every interior block has magnitude at most $1/4$. Choose $p_i=1/2$ on the two endpoint blocks and $p_i=3/4$ on the interior blocks. Every path chooses one coordinate from each block, so its product of free probabilities is

$$

 \frac14\left(\frac34\right)^{k-2}.

$$

Taking absolute values in (F8), summing over paths, and applying (F7) to each restriction gives the factor $4(4/3)^{k-2}$. Since

$$

 b^{k-1}\,4\left(\frac43\right)^{k-2}=\frac3{4^{k-1}},

$$

the strongest finite estimate in this calculation is

$$

 \boxed{\quad
 \Gamma(\varepsilon)
 \le\frac{3C^k}{4^{k-1}}
 \sqrt{\binom{2\tau L}{k}}
 \left(\frac{1+\ln(km)}m\right)^{(k-1)/2}.
 \quad}
 \tag{F9}

$$

Equation (F9) is note.md, equation (27). If $2\tau L<k$, the right side is zero, already contradicting a positive $\Gamma$. Otherwise, $\binom{2\tau L}{k}\le(2e\tau L/k)^k$. Solving gives

$$

 \boxed{\quad
 L\ge\frac{k}{2e\tau C^2}
 \left(\frac{\Gamma(\varepsilon)\,4^{k-1}}3\right)^{2/k}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.
 \quad}
 \tag{F10}

$$

Equation (F10) is note.md, equation (28). It is a quantitative implication of a particular growth theorem, with no hidden constant. It is not a claim that the absolute numerical constant, the threshold in $m$, or the logarithmic loss is optimal.
<!-- /passage:q-sharp-finite -->

<!-- passage:q-elementary-uniform -->
## 2. Two simple uniform theorems

### The elementary theorem using the actual truncation

Theorem 2 of note.md, equation (4), holds for every power of two. At the public Lean dimensions, it reads: for every integer $k\ge2$ and every $m=4^t\ge2^{15k+2}$,

$$

 \boxed{\quad R(P\,k\,t)>
 \frac2{18225}\frac{m^{1-1/k}}{k^2\ln(4km)}.\quad}
 \tag{E1}

$$

Proof. Suppose a successful depth-$L$ algorithm has $L$ at most the displayed quantity. Use $\tau=25k$ and $2\tau$ repetitions. The exact integer inequality $18\cdot8^{25}<9^{25}$ gives $\varepsilon\le18^{-k}=a/18$. The identity $32\delta=32^{-(k-1)}\le a$ gives $\delta\le a/32$. The size hypothesis gives $q\le\delta$. Since $0<p\le1$,

$$

 \Gamma(\varepsilon)\ge p-2\varepsilon-q
 \ge a-2\delta-2\varepsilon
 \ge\frac{119}{144}a>\frac34a.

$$

A depth-zero algorithm has constant acceptance probability and cannot have this positive gap, so $L\ge1$. Put $d=50kL$. Then

$$

 16kd\ln(4km)=800k^2L\ln(4km)
 \le\left(\frac8{27}\right)^2m^{1-1/k}.

$$

The main term in (F5) is consequently at most $(8/27)a$, since $b(8/27)=1/18$. The remaining term is at most $a/4$, because $2^{-k}\le1/4$ and $b/\sqrt m\le1/18$. Thus the advantage is at most $59a/108<3a/4$, a contradiction.

Every constant in (E1) is numerical. The supplied Lean theorems prove the needed identity, promise moments, amplification and a parameterised growth estimate. They do not yet state (E1), the sharpened edge bound $b=3/16$, or the exact specialised growth corollary (F4). Those are new, straightforward mathematical consequences to formalise.
<!-- /passage:q-elementary-uniform -->

<!-- passage:q-sharp-uniform -->
### The theorem using Sherstov–Storozhenko–Wu

With $C$ fixed as in (F7), for every $k\ge2$, every power of two $m\ge2^{15k+2}$, and $0<\eta\le1$,

$$

 \boxed{\quad R_{(1-\eta)/2}(P_{k,m})\ge
 \frac{\eta^2}{162eC^2}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.\quad}
 \tag{S1}

$$

This is note.md, Theorem 1, equation (3). In particular, at $m=4^t$ and error $1/3$,

$$

 R(P\,k\,t)\ge\frac1{1458eC^2}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}.
 \tag{S2}

$$

Proof. Choose $\tau=\lceil5k\ln2/\eta^2\rceil$. Then $\varepsilon\le e^{-\tau\eta^2}\le\delta$, and $\tau\le(5\ln2+1/2)k/\eta^2<4k/\eta^2$. Also $q\le\delta$. Since

$$

 (1-\delta)p=a-\delta,

$$

we have $\Gamma(\varepsilon)\ge a-3\delta\ge29a/32$. Consequently,

$$

 \left(\frac{\Gamma(\varepsilon)4^{k-1}}3\right)^{2/k}
 \ge\frac4{81}\left(\frac{87}{64}\right)^{2/k}
 \ge\frac4{81}.

$$

Substitution into (F10) proves (S1). Set $\eta=1/3$ for (S2).

The finite formula (F9) is stronger than (S1). For example, choosing amplification relative to $a$ instead of $\delta$ improves the numerical constant. No such improvement changes the zero inverse-polynomial loss in $k$.
<!-- /passage:q-sharp-uniform -->

<!-- passage:q-k-comparison -->
## 3. Where the powers of k enter

For comparison, let $C_T\ge1$ be a universal constant in the natural-log form of Tal’s decision-tree Fourier bound, [arXiv:1912.12561](https://arxiv.org/abs/1912.12561), Theorem 5.1:

$$

 \sum_{|S|=k}|\widehat T(S)|\le C_T^k d^{k/2}(1+\ln n)^{(k-1)/2}.

$$

The same endpoint/interior restriction gives (F9) with $\sqrt{\binom{2\tau L}k}$ replaced by $(2\tau L)^{k/2}$. The same calculation then gives

$$

 R_{(1-\eta)/2}(P_{k,m})\ge\frac{\eta^2}{162kC_T^2}
 \left(\frac m{1+\ln(km)}\right)^{1-1/k}

$$

in the same parameter range. Thus there are three different valid conclusions:

| Fourier input | Growth at level $k$ | Lower-bound shape |
|---|---|---|
| Elementary stopped martingale | $(16kd\ln(4km))^{k/2}+2^{-k}$ | $c\,m^{1-1/k}/[k^2\ln(4km)]$, with the numerical $c=2/18225$ for error $1/3$ |
| Tal | $C_T^k d^{k/2}B^{(k-1)/2}$ | $\eta^2(162kC_T^2)^{-1}(m/B)^{1-1/k}$ |
| Sherstov–Storozhenko–Wu | $C^k\sqrt{\binom d k}B^{(k-1)/2}$ | $\eta^2(162eC^2)^{-1}(m/B)^{1-1/k}$ |

Bansal and Sinha's [Theorem 1.3](https://arxiv.org/abs/2008.07003v3) states the $k^{-29}\eta^2(m/\log(km))^{1-1/k}$ lower-bound scale. Its $k^{-28}$ loss arises in their multilevel comparison, and another $k^{-1}$ comes from amplification. The blockwise route removes the first loss. The sharp factorial improvement in Fourier growth cancels the remaining amplification loss. These are mathematical comparisons to the cited quantitative theorem. They make no priority claim about the improved deduction.

The size restriction $m\ge2^{15k+2}$ must be retained in the uniform theorem. It makes the uniform exceptional probability at most $\delta$. A fixed-$k$ asymptotic theorem hides this threshold in $t_0(k)$, while a uniform theorem must display it. The finite formula (F9), with its exact $\Gamma$, records what this proof gives outside that convenient regime. The claim that (S1) holds for all $k,m$ without a replacement argument is not established here.
<!-- /passage:q-k-comparison -->

<!-- passage:q-growth-proof -->
## 4. Complete elementary proof of (F4)

Fix an integer $n\ge1$ and a product measure with means $|\mu_i|\le1/2$, and set

$$

 \xi_i(x_i)=\frac{x_i-\mu_i}{1-\mu_i^2}.

$$

These variables are independent, centred, and satisfy $|\xi_i|\le2$. Direct summation in one coordinate gives

$$

 \partial_S\widetilde T(\mu)
 =\mathbb E_\mu\left[T(X)\prod_{i\in S}\xi_i(X_i)\right]

$$

for every set $S$ of distinct coordinates. Choose coefficients $c(S)\in\{-1,0,1\}$ equal to the signs of the derivatives in the selected family and zero elsewhere. Their degree-$k$ chaos is

$$

 Y_k^c(Q)=\sum_{\substack{S\subseteq Q\\|S|=k}}c(S)\prod_{i\in S}\xi_i(X_i).

$$

Reveal $X$ along the deterministic tree, and let $Q_j$ be the set of coordinates seen after $j$ queries. Repeated queries leave $Q_j$ unchanged. After an early leaf, keep $Q_j$ fixed so the process has a common horizon $d$. If the next fresh coordinate is $u$, then

$$

 Y_{\ell}^c(Q_{j+1})-Y_{\ell}^c(Q_j)
 =\xi_u(X_u)Y_{\ell-1}^{c^u}(Q_j),\qquad c^u(S)=c(S\cup\{u\}).

$$

In the contracted coefficient array, define $c^u(S)=0$ when $u\in S$; the displayed formula applies when $u\notin S$. The increment is centred conditionally on the transcript. Set $K=\sqrt{8d\Lambda}$, where $d\ge1$ and $\Lambda>0$. For all coefficient arrays with magnitude at most one, we prove

$$

 \Pr\left(\max_{j\le d}|Y_\ell^c(Q_j)|>K^\ell\right)
 \le(4n)^\ell e^{-\Lambda}.
 \tag{M1}

$$

For $\ell=0$, the event is empty. For the induction step, stop before the first query for which some coefficient chaos $Y_{\ell-1}^{c^u}$ has magnitude greater than $K^{\ell-1}$. The stopped martingale has increments of magnitude at most $2K^{\ell-1}$. Hoeffding's elementary conditional moment estimate is

$$

 \mathbb E[e^{\lambda Z}\mid\mathcal F]\le e^{\lambda^2D^2/2}
 \quad\text{when }\mathbb E[Z\mid\mathcal F]=0,\quad |Z|\le D.

$$

It follows by bounding $e^{\lambda z}$ by the secant joining its endpoint values at $\pm D$, averaging, and using $\cosh u\le e^{u^2/2}$. Let $Z_i$ be the stopped degree-$\ell$ martingale, with $Z_0=0$, and set $M_i=\exp(\lambda Z_i-\lambda^2D^2i/2)$. The conditional inequality gives $\mathbb E[M_{i+1}\mid\mathcal F_i]\le M_i$. If $\sigma$ is the first crossing of $Z_i>R$, capped at $d$, iterated conditioning for $M_{\min(i,\sigma)}$ gives $\mathbb E M_\sigma\le1$. On crossing, $M_\sigma\ge\exp(\lambda R-\lambda^2D^2d/2)$. Hence the crossing probability is at most $\exp(-\lambda R+\lambda^2D^2d/2)$. Taking $\lambda=R/(dD^2)$ gives $\exp[-R^2/(2dD^2)]$. Apply the same argument to the negative martingale. For both signs with $R=K^\ell$ and $D=2K^{\ell-1}$, the resulting bound is $2e^{-\Lambda}$.

The probability of stopping is at most $n(4n)^{\ell-1}e^{-\Lambda}$ by the induction hypothesis and a union bound over $u$. Therefore the crossing probability is at most

$$

 [2+n(4n)^{\ell-1}]e^{-\Lambda}\le(4n)^\ell e^{-\Lambda}.

$$

This proof uses a stopped martingale before applying the exponential estimate. Conditioning a martingale on the event that all increment bounds hold would not justify the estimate.

At a leaf, every unqueried centred variable still has conditional mean zero and the product law on unqueried coordinates is unchanged. The conditional expectation of the full degree-$k$ chaos is therefore $Y_k^c(Q_d)$. Since $T$ is constant on a leaf,

$$

 \sum_S|\partial_S\widetilde T(\mu)|
 =\mathbb E_\mu[T(X)Y_k^c(Q_d)].

$$

The terminal chaos is bounded by $(2n)^k$ on every outcome and by $K^k$ when the crossing event is absent. Thus

$$

 \sum_S|\partial_S\widetilde T(\mu)|
 \le K^k+(2n)^k(4n)^k e^{-\Lambda}.

$$

Set $\Lambda=2k\ln(4n)$. The second term is $2^{-k}$, and $K^2=16kd\ln(4n)$, proving (F4). This is the standard decision-tree martingale mechanism described by Girish, Tal and Wu, [CCC 2021](https://doi.org/10.4230/LIPIcs.CCC.2021.39), §1.3 and Lemma 1.9, run directly under a bounded biased product measure.
<!-- /passage:q-growth-proof -->

<!-- passage:q-coarse-uniform -->
## 5. The uniform endpoint using the existing coarse Lean estimates

The exact existing theorem QuarticQuery.ForrelationLower.not_RLe_of_gap can prove the following conservative new endpoint without sharpening the edge kernel:

$$

 \boxed{\quad
 R(P\,k\,t)>
 \frac1{2332800}
 \frac{m^{1-1/k}}{k^2\ln(4km)},
 \qquad k\ge2,\quad m=4^t\ge2^{15k+2}.
 \quad}

$$

The proof assembles existing estimates into a new uniform endpoint. That endpoint has not been compiled.

Take $\tau=25k$, $\Lambda=2k\ln(4km)$, $d=2\tau L+1=50kL+1$, and $K=\sqrt{8d\Lambda}$, as required by the existing finite contradiction theorem. If $L\ge1$ and

$$

 L\le \frac1{2332800}
 \frac{m^{1-1/k}}{k^2\ln(4km)},

$$

then

$$

 K^2=16kd\ln(4km)
 \le\frac1{54^2}
 \left(1+\frac1{50k}\right)m^{1-1/k}.

$$

Here $800/2332800=1/54^2$. Therefore the main part of the existing coarse $3^{k-1}$ advantage estimate is at most

$$

 \frac{a}{54}\left(1+\frac1{50k}\right)^{k/2}
 \le\frac{a}{48}.

$$

For the last inequality, use

$$

 \left(1+\frac1{50k}\right)^k
 =\sum_{j=0}^k\binom kj(50k)^{-j}
 \le\sum_{j=0}^k50^{-j}
 \le\frac{50}{49}<\left(\frac98\right)^2.

$$

The existing tail term specialises exactly to $2^{-k}(3/\sqrt m)^{k-1}$. Under the size hypothesis $\sqrt m\ge54$, it is at most $a/4$. Thus the full existing advantage upper bound is at most $13a/48$.

The weaker promise gap used by QuarticQuery.ForrelationLower.not_RLe_of_gap, without the denominator $1-\delta$, still satisfies

$$

 (1-\varepsilon)(a-\delta)-\varepsilon-\frac4{m\delta^2}
 \ge a-2\delta-2\varepsilon
 \ge\frac{119}{144}a.

$$

The first inequality uses $a-\delta\le1$. The last uses $\varepsilon=(8/9)^{25k}\le a/18$, $\delta\le a/32$, and $4/(m\delta^2)\le\delta$. Since $13/48<119/144$, the existing gap condition holds strictly.

If $L=0$, every depth-zero tree is constant. Its mixture has the same expectation under the two distributions, contradicting the positive gap just established. Hence the endpoint has no omitted zero-depth case.
<!-- /passage:q-coarse-uniform -->

<!-- passage:q-evidence -->
## 6. Formal status and source locations

No new Lean build was run for this return. The conclusions above are mathematical deductions. Their evidence separates into the following cases.

- The source already contains the blockwise identity in mean-value form, the promise mean and uniform second moment, the parameterised biased Fourier estimate, error-$1/3$ amplification, and a finite-parameter contradiction theorem.
- The uniform endpoint with $1/2332800$ requires a new parameter assembly of those estimates, with the exact padding $d=50kL+1$ already present in the finite contradiction theorem.
- The endpoint with $2/18225$ also uses the sharpened kernel bound $3/16$, and uses the elementary growth specialization with residual term $2^{-k}$.
- The endpoint from SSW additionally uses its published Fourier theorem and the profile restriction. This external theorem has not been formalised in the supplied development.
- The finite inversion (F6), the displayed numerical Tal-only comparison, and the error-$1/3$ corollary (S2) are registered in NEW_STATEMENTS.json.

The relevant supplied source files, with full declaration names, are:

| File in the supplied repository | Declaration or purpose |
|---|---|
| lean/QuarticQuery/ForrelationLower/Walk.lean | QuarticQuery.ForrelationLower.exists_identity; QuarticQuery.ForrelationLower.Int_eq_paths; QuarticQuery.ForrelationLower.abs_cf_le |
| lean/QuarticQuery/ForrelationLower/Cascade.lean | QuarticQuery.ForrelationLower.integral_ext_wv_zero and QuarticQuery.ForrelationLower.advantage_le |
| lean/QuarticQuery/ForrelationLower/Promise.lean | QuarticQuery.ForrelationLower.mass_ge and QuarticQuery.ForrelationLower.ext_PhiF_sq |
| lean/QuarticQuery/ForrelationLower/TreeGrowth.lean | QuarticQuery.ForrelationLower.sum_abs_ext_Dl_le and QuarticQuery.ForrelationLower.hit_chaos_le |
| lean/QuarticQuery/ForrelationLower/Amplify.lean | QuarticQuery.ForrelationLower.exists_amplified |
| lean/QuarticQuery/ForrelationLower/Main.lean | QuarticQuery.ForrelationLower.not_RLe_of_gap and QuarticQuery.ForrelationLower.bansalSinhaLower |
| lean/QuarticQuery/Statement.lean | QuarticQuery.P, QuarticQuery.R, QuarticQuery.mValue, QuarticQuery.Lvalue and QuarticQuery.BansalSinhaLower |

The use of the full-path identity in integral form follows note.md, Proposition 6, equation (12). The supplied exported theorem is a mean-value version asserting one parameter in $(0,1)$. The strengthened bounds are therefore not described as statements already checked in Lean. The exact return-wide mapping is in correspondence.json, NEW_STATEMENTS.json, and LEAN_GAPS.md.

Primary literature used for the quantitative comparison:

- Nikhil Bansal and Makrand Sinha, [$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity](https://arxiv.org/abs/2008.07003v3), Theorem 1.3, Corollary 1.4, Theorem 3.2, and the main lower-bound proof.
- Alexander A. Sherstov, Andrey A. Storozhenko, and Pei Wu, [An Optimal Separation of Randomized and Quantum Query Complexity](https://arxiv.org/abs/2008.10223v4), Theorem 1.9 and Corollary 4.14. The latter states the required bound with natural logarithms. Theorem 4.13 exposes intermediate constants, but no numerical universal constant is certified by the statement.
- Avishay Tal, [Towards Optimal Separations between Quantum and Randomized Query Complexities](https://arxiv.org/abs/1912.12561), Theorem 5.1.
- Uma Girish, Avishay Tal, and Kewen Wu, [Fourier Growth of Parity Decision Trees](https://doi.org/10.4230/LIPIcs.CCC.2021.39), §1.3, Lemma 1.9, and the martingale estimates in §3.2.
- Xinyu Wu, [Analyzing XOR-Forrelation through Stochastic Calculus](https://arxiv.org/abs/2109.02732), Lemma 2.2. The more general free-probability identity used here follows by the displayed monomial calculation.

The improvement proved here concerns the quantitative consequence of the inspected route. It is not an assertion of priority. The search findings and their limits are recorded separately in prior_art.json.
<!-- /passage:q-evidence -->

