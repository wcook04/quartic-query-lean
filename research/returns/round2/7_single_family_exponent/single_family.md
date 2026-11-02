**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

# An explicit single family with randomized–quantum exponent tending to four

<!-- passage:abstract -->
**Abstract.** OpenAI's addressed-certificate construction admits a single explicit sequence of total Boolean functions with randomized–quantum query exponent $4-O(1/\sqrt{\log m})$. For $m=4^t$, $t\ge80$, choose $k=\lfloor\sqrt{(\log_2m)/20}\rfloor$. A uniform Forrelation lower bound and a coherent amplitude-estimation decoder give an exponent at least $4-8\sqrt5/\sqrt{\log_2m}-O(\log\log m/\log m)$. We give numerical constants and a threshold valid for the entire sequence. The repetition decoder in the supplied Lean development already gives the same order, with leading coefficient $8\sqrt{10}$ and a different choice of $k$. A diagonal sequence without an explicit rate follows from the original fixed-$k$ theorem alone.
<!-- /passage:abstract -->

## 1. The explicit family

<!-- passage:definitions -->
All complexities count worst-case bit queries with error at most $1/3$; computation between queries is unrestricted. Let $m=4^t$ and $s=\log_2m=2t$. Write $H$ for the normalized Walsh matrix of order $m$, $u=m^{-1/2}(1,\ldots,1)^\top$, and $D_z$ for the diagonal matrix of a sign vector $z$. The normalized $k$-Forrelation value on $km$ bits is $\Phi=u^\top D_{z_1}HD_{z_2}H\cdots HD_{z_k}u$, with bits identified with signs. Let $P_{k,m}$ be the partial Boolean function that is one when $\Phi\ge\delta$ and zero when $|\Phi|\le\delta/2$, where $\delta=2^{-5k}$; it is undefined elsewhere.

We use OpenAI's total function $F_{k,m}$, with its canonical exact Forrelation circuit. A column contains an $m$-bit data string, $r=20s$ Forrelation instances, and an array of $2^r$ certificate cells. A winning column has an all-one data string; the answers to its promised instances address a cell containing their correct circuit transcripts and pointers to zeros in every other column's data string. The total function asks whether a winning column exists. These definitions are those of OpenAI [1, §2, equations (3)–(8)].

We write $\ln$ for the natural logarithm. The variable $m$ is the number of columns. The full number of input bits is computed in §6.
<!-- /passage:definitions -->

<!-- passage:main-theorem -->
**Theorem 1.** For each integer $t\ge80$, set
\[
 m=4^t,\qquad s=2t,\qquad
 k=\left\lfloor\sqrt{s/20}\right\rfloor,\qquad F_m=F_{k,m}.
 \tag{1}
\]
Then $Q(F_m)>1$, and
\[
 R(F_m)>
 \frac{m^{2-1/k}}{466\,560\,000\,k^2\ln(4km)},
 \qquad
 Q(F_m)\le 2^{59}k2^{5k}\sqrt m\,s^6.
 \tag{2}
\]
In particular,
\[
 R(F_m)\ge Q(F_m)^{\,4-\varepsilon_5(s)},\qquad
 \varepsilon_5(s)=\frac{8\sqrt5}{\sqrt s}
       +\frac{56\log_2s+552}{s},
 \qquad
 \lim_{t\to\infty}\frac{\log R(F_{4^t})}{\log Q(F_{4^t})}=4.
 \tag{3}
\]
The finite exponent in (3) is a deliberately simple lower estimate. It can be negative near the starting threshold; the positive, more informative finite estimate is given in (18) below.

The construction and its separation mechanism are OpenAI's [1]. The improvement to the decoder uses the amplitude-estimation theorem of Brassard, Høyer, Mosca and Tapp [2, Theorem 12]. The uniform lower bound is obtained from the supplied Gaussian-chain proof, whose distributional antecedent is Bansal and Sinha [3] and whose decision-tree estimate uses the martingale method of Girish, Tal and Wu [4]. This result gives an explicit rate of approach to four. It does not establish a fourth-power separation up to a fixed polylogarithmic factor, or an optimal rate for these functions.
<!-- /passage:main-theorem -->

<!-- passage:proof-idea -->
The choice of $k$ balances two costs. The classical lower bound loses $m^{1/k}$, while a bounded-error decoder pays exponentially in $k$. With amplitude estimation, the principal terms in $\log_2R$ and $\log_2Q$ are $2s-s/k$ and $s/2+5k$. Balancing their losses selects $k$ near $\sqrt{s/20}$. To make this calculation uniform, we first choose the auxiliary classical budget directly from the available Forrelation estimate.
<!-- /passage:proof-idea -->

## 2. A uniform classical bound

<!-- passage:uniform-bound -->
**Lemma 2.** For $k\ge2$ and $15k+2\le2t$, the Forrelation promise in §1 satisfies
\[
 R(P_{k,m})>X,
 \qquad X=\frac{m^{1-1/k}}{2\,332\,800\,k^2\ln(4km)}.
 \tag{4}
\]
Here the constant uses the coarse edge estimate already present in the supplied proof. The sharper edge estimate discussed in the earlier Forrelation note is unnecessary for the result below.
<!-- /passage:uniform-bound -->

<!-- passage:uniform-proof -->
*Proof.* The finite comparison inequality in the supplied Gaussian-chain argument has a direct uniform specialization. Suppose a successful randomized algorithm uses an integer budget $L\le X$. Put $a=18^{-(k-1)}$. Amplify by $50k$ independent runs, so that the error is at most $\epsilon=(8/9)^{25k}$, and pad its depth to $d=50kL+1$. The hard distribution has mean Forrelation at least $a$; the uniform distribution has second moment $1/m$. Consequently the acceptance-probability gap is at least
\[
 (1-\epsilon)(a-\delta)-\epsilon-\frac4{m\delta^2}
 \ge a-2\delta-2\epsilon
 \ge\frac{119}{144}a.
 \tag{5}
\]
Indeed, $18\cdot8^{25}<9^{25}$ gives $\epsilon\le a/18$, $32\delta\le a$, and $m\ge2^{15k+2}$ gives $4/(m\delta^2)\le\delta$.

For $L\ge1$, set $\Lambda=2k\ln(4km)$ and $K^2=8d\Lambda=16kd\ln(4km)$. In the finite Fourier estimate, the residual factor simplifies as $(2km)^k(4km)^k e^{-\Lambda}=2^{-k}$. The bound $L\le X$ gives
\[
 K^2\le\frac{1+1/(50k)}{54^2}m^{1-1/k},\qquad
 \left(\frac3{\sqrt m}\right)^{k-1}K^k\le\frac a{48},
 \qquad
 2^{-k}\left(\frac3{\sqrt m}\right)^{k-1}\le\frac a4.
 \tag{6}
\]
For the middle inequality use $(1+1/(50k))^k\le50/49<(9/8)^2$; for the last use $t\ge6$, which follows from the hypotheses. The finite comparison inequality bounds the same acceptance gap by the sum of the last two expressions in (6). This is at most $13a/48<119a/144$, contradicting (5). At depth zero the acceptance probability is input-independent; amplification would again have a positive gap under the two distributions, so this case is impossible as well. Thus no integer $L\le X$ succeeds. Apply this to $L=\lfloor X\rfloor$ and use the integrality of $R(P_{k,m})$ to obtain (4). ∎

This is the parameter assembly in `ForrelationLower/Uniform.lean`, based on `ForrelationLower.not_RLe_of_gap`. It uses the alternative Forrelation proof in place of the multilevel estimate in Bansal and Sinha's §5.4. The proof above does not require the disputed logarithmic simplification in that display.
<!-- /passage:uniform-proof -->

<!-- passage:auxiliary-budget -->
**Lemma 3.** If $k\ge2$, $t\ge64$, and $15k+2\le2t$, then, for every circuit realizing the Forrelation promise,
\[
 R(F_{k,m})>
 \frac{m^{2-1/k}}{466\,560\,000\,k^2\ln(4km)}.
 \tag{7}
\]
*Proof.* Choose $L=\lfloor X\rfloor$, with $X$ from (4). The hypotheses give $k\le t$ and $\ln(4km)\le6t$, while $m^{1-1/k}\ge2^t$. Thus
\[
 X\ge\frac{2^t}{13\,996\,800\,t^3}\ge2,
 \qquad 1\le L\le m,\qquad L\ge X/2.
 \tag{8}
\]
The numerical inequality holds at $t=64$ and persists because $2^t/t^3$ increases for integers $t\ge4$. The upper bound $X\le m$ follows from $m^{1-1/k}\le m$ and a denominator greater than one.

The general planted-input argument applies to every $1\le L\le m$ with $L<R(P_{k,m})$. At $G=\lfloor mL/100\rfloor$ and $r=20s$, its conservative discrepancy bound satisfies
\[
 \frac{4G}{m^2}+\frac{G}{mL}
       +G\left(\frac23\right)^r
 \le\frac6{100}<\frac13,
 \qquad R(F_{k,m})>\left\lfloor\frac{mL}{100}\right\rfloor.
 \tag{9}
\]
Here $(2/3)^r\le m^{-10}$, $L\le m$, and $G\le mL/100$. The supplied induction proves the capped adaptive direct product used in this argument; this replaces the preprint's supermartingale route. Since $R(F_{k,m})$ is an integer, the last inequality in (9) implies $R(F_{k,m})>mL/100\ge mX/200$. Substituting (4) proves (7). ∎

The parameter $L$ is absent from the definition of $F_{k,m}$. The source corollary for the particular choice $L=\lfloor m^{1-1/k}/s^2\rfloor$ assumes $t\ge3\,499\,200k^2$. Lemma 3 avoids that additional condition by using the general planted-input theorem. This changes the analysis of the same total function.
<!-- /passage:auxiliary-budget -->

## 3. Quantum dependence on $k$

<!-- passage:existing-quantum -->
The repetition decoder in the supplied development uses
\[
 n_{\rm rep}=\left\lceil16\,2^{10k}\ln(1/\eta)\right\rceil,
 \qquad \eta=\frac1{20\,000s(s+10)}.
 \tag{10}
\]
Its compiled upper theorem holds for every $k\ge1,t\ge1$. Expanding its constant gives
\[
 \begin{split}
 B_{10}(k)={}&2\,972\,284\,080\,k(1+1\,920\,000\,2^{10k})\\
 &+79\,491\,312\,000(k+1)^2+1\,131\,887\,160,
 \end{split}
 \qquad
 Q(F_{k,m})\le B_{10}(k)\sqrt m\,s^6
               \le2^{53}k2^{10k}\sqrt m\,s^6.
 \tag{11}
\]
The powers of $k$ in the exact circuit size are quadratic. The address length, tournament length and accuracy parameters in (10) depend only on $s$. Thus the exponential factor in (11) comes from decoding the small Forrelation gap.
<!-- /passage:existing-quantum -->

<!-- passage:ae-decoder -->
**Lemma 4.** For $k\ge1$, $t\ge0$, and $0<\eta<1$, there is a coherent decoder for $P_{k,m}$, retaining all its workspace, with error at most $\eta$ on the promise and with at most
\[
 256k2^{5k}
 \left\lceil\frac{\ln(1/\eta)}{\ln(4/3)}\right\rceil
 \tag{12}
\]
bit queries on every input. The same expression is a valid conservative bound in the source's abstract read model.

*Proof.* Let $A$ be the $k$-phase-query preparation whose success probability is $p=\Phi^2$. Apply amplitude estimation [2, Theorem 12] with $M=32\,2^{5k}=32/\delta$. With probability at least $8/\pi^2>3/4$, the estimate satisfies
\[
 |\widetilde p-p|
 \le\frac{2\pi\sqrt{p(1-p)}}M+\frac{\pi^2}{M^2},
 \qquad
 \begin{cases}
  \widetilde p\le25\delta^2/64,&p\le\delta^2/4,\\
  \widetilde p\ge47\delta^2/64,&p\ge\delta^2.
 \end{cases}
 \tag{13}
\]
The first margin follows by inserting $\sqrt p\le\delta/2$ and $\pi<4$. For the second, write $u=\sqrt p\ge\delta$; then $(u-\delta)(u+3\delta/4)\ge0$ gives the bound throughout the yes range. Thresholding at $\delta^2/2$ therefore succeeds with probability above $3/4$. The probability comparison uses $\pi^2<32/3$, for example from $\pi<22/7$.

Run $2h$ independent copies, where $h=\lceil\ln(1/\eta)/\ln(4/3)\rceil$, and take a majority with fixed tie-breaking. Count every tie as an error when bounding the error probability. The exponential-moment bound for Bernoulli variables of mean at most $1/4$ gives error at most $(3/4)^h\le\eta$.

For query counting, keep the exact Grover iterate $-AS_0A^\dagger S_\chi$. The reflections $S_0$ and $S_\chi$ are input-independent; the conjugation by $A$ uses the oracle. Controlled versions include the leading minus sign as a fixed phase on the control. A controlled phase query can be implemented by loading the input bit, applying the controlled phase, and unloading it, for at most two bit queries. Thus one controlled iterate uses at most $4k$ queries, and the initial preparation at most $2k$. Since $M$ is a power of two, the controlled powers use $M-1$ iterates in total. One estimation run costs at most $2k+4k(M-1)\le4kM$; the $2h$ runs cost at most $8kMh=256k2^{5k}h$.

In the abstract read model, the initial preparation costs $k$ reads and a controlled iterate costs $2k$, giving at most $2kM$ reads per estimation run and $128k2^{5k}h$ reads overall. Compilation at two bit queries per read also yields (12). We use the larger expression (12) as a conservative read cap below.

Omit the final measurements and retain every estimation and work register. Threshold and majority are fixed functions of the retained labels and can be computed reversibly. The fresh registers give the same product distribution as independent measured runs. The resulting circuit is unitary, has an inverse of the same cost, and can be controlled by a column index. On an input outside the promise it still has a fixed query cap and outputs a bit. These are the coherent properties required by the comparison algorithm. ∎
<!-- /passage:ae-decoder -->

<!-- passage:ae-assembly -->
For $t\ge1$, apply Lemma 4 at the error in (10). Write $T=s+10$, $\epsilon=1/(1000T)$, and let $S$ be the exact certificate circuit size. The source proves
\[
 S\le200(k+1)^2ms^2,\qquad
 K=2m-1+20s(S+2),\qquad v=\max(3,s+1).
 \tag{14}
\]
There are $K$ local tests, each costing at most $v$ reads. Decoding all $20s$ address bits to error $\epsilon/(20s)$ gives whole-address error at most $\epsilon$.

Let $d_\eta$ be the decoder read cap in (12), $a=20s\,d_\eta$, and $c=2a+2s+2$. A comparison decodes the two addresses and performs the two pointer tests at read cost at most $c$. A genuine winner defeats each opponent with probability at least $1-\epsilon$. For distinct candidates, the comparison always selects one of the two, so its probabilities are complementary on arbitrary inputs; self-comparison probabilities are set to zero. Each local test is exact. The final quantum search accepts a true certificate with certainty and accepts a false certificate with probability at most $\epsilon$. The bounded tournament and verification constructions therefore apply to this decoder.

For completeness, put $J(q)=\lceil10/\sqrt q\rceil$ and $N=\lceil\ln(1/\epsilon)/\ln(40/31)\rceil$. Their explicit total cost is at most
\[
 T\,N\,2\bigl(2J(1/(2m))+1\bigr)T c
 \; +\;
 T\left[2a+N\,2\bigl(2J(1/K)+1\bigr)v\right].
 \tag{15}
\]
This bound includes the factor two that compiles an abstract read to physical bit queries. Treating the already conservative cap (12) as a read cap is legitimate and leaves extra slack.

Since $\ln(4/3)\ge1/4$, $1/\eta=20\,000s(s+10)\le120\,000s^2$, and $\ln(1/\eta)\le1/\eta$, we have $h\le480\,000s^2+1$. Hence $d_\eta\le122\,880\,256\,k2^{5k}s^2$. The arithmetic bounding (15) is the same explicit arithmetic used to obtain (11). It gives
\[
 \begin{split}
 B_5(k)={}&2\,972\,284\,080\,k(1+122\,880\,256\,2^{5k})\\
 &+79\,491\,312\,000(k+1)^2+1\,131\,887\,160,
 \end{split}
 \qquad
 Q(F_{k,m})\le B_5(k)\sqrt m\,s^6
             \le2^{59}k2^{5k}\sqrt m\,s^6.
 \tag{16}
\]
For the last inequality use $(k+1)^2\le4k2^{5k}$ and compare the remaining integer coefficient $365\,235\,350\,724\,543\,720$ with $2^{59}$. The existing upper theorem is specialized to the repetition decoder. Lemma 4 requires a new coherent decoder and a new assembly of the address, comparison and verification laws; (16) is a mathematical proof of that extension.
<!-- /passage:ae-assembly -->

## 4. Optimizing the exponent

<!-- passage:thresholds -->
For the choice in (1), $k\ge2$ when $t\ge80$. Moreover $k\le\sqrt{t/10}\le t/15$, so $15k+2\le2t$. Thus Lemma 3 and (16) apply throughout the stated range; there is no residual threshold depending on a fixed $k$.
<!-- /passage:thresholds -->

<!-- passage:finite-ratio -->
Define the explicit logarithmic bounds
\[
 A(s,k)=(2-1/k)s-\log_2\!\left(466\,560\,000\,k^2\ln(4k2^s)\right),
 \qquad
 D_5(s,k)=s/2+\log_2B_5(k)+6\log_2s.
 \tag{17}
\]
Equations (7) and (16) give $\log_2R>A(s,k)$ and $\log_2Q\le D_5(s,k)$. The universal total-function bound $R\le20736Q^4$ follows from the supplied formal route to Aaronson, Ben-David, Kothari, Rao and Tal's quartic bound [5]. Coordinate renaming transports that bound to the input type here. Along (1), $A(s,k)\ge s/2-30\ge50$, so $Q>1$. It follows that
\[
 \frac{\log R(F_m)}{\log Q(F_m)}>
 E_5(s):=\frac{A(s,k)}{D_5(s,k)}>0,
 \qquad R(F_m)>Q(F_m)^{E_5(s)}.
 \tag{18}
\]
These are lower bounds on the actual exponent, not evaluations of either optimal query complexity.
<!-- /passage:finite-ratio -->

<!-- passage:optimization-proof -->
To obtain the simple expression in (3), note that $k\le\sqrt s$, $\ln(4k2^s)\le2s$, and $466\,560\,000<2^{29}$. Thus
\[
 A(s,k)\ge2s-s/k-30-2\log_2s,
 \qquad
 D_5(s,k)\le s/2+5k+59+\tfrac{13}{2}\log_2s.
 \tag{19}
\]
The first bound is positive. Dividing in the correct direction, and then using a denominator of at least $s/2$, bounds $4-E_5(s)$ by
\[
 \frac2k+\frac{40k}s+\frac{56\log_2s+532}s.
 \tag{20}
\]
Put $x=\sqrt{s/20}$. The linear rounding errors cancel:
\[
 \frac2k+\frac{40k}s
 =\frac4x+\frac{2(k-x)^2}{kx^2}
 \le\frac{8\sqrt5}{\sqrt s}+\frac{20}s.
 \tag{21}
\]
This proves (3)'s finite inequality. Also $R\to\infty$ by (7), so the universal quartic bound forces $Q\to\infty$. The same bound gives $\log R/\log Q\le4+\log(20736)/\log Q$, proving the limit in (3).

For positive real $k$, the principal expression $2/k+40k/s$ is minimized at $k=\sqrt{s/20}$, with value $8\sqrt5/\sqrt s$. This optimizes the leading terms of these comparison estimates. It makes no optimality assertion about the query complexities themselves.
<!-- /passage:optimization-proof -->

<!-- passage:baseline -->
If the repetition decoder is retained, choose $k=\lfloor\sqrt{s/40}\rfloor$. The same proof uses $B_{10}$ in (17) and gives, for all $t\ge80$,
\[
 R(F_{k,m})\ge
 Q(F_{k,m})^{\,4-\varepsilon_{10}(s)},\qquad
 \varepsilon_{10}(s)=\frac{8\sqrt{10}}{\sqrt s}
                     +\frac{56\log_2s+524}{s}.
 \tag{22}
\]
This conclusion uses the existing quantum algorithm. Its remaining new work is the uniform lower-bound assembly, the choice of $L$, and the arithmetic of the diagonal schedule.
<!-- /passage:baseline -->

## 5. What uniformity adds

<!-- passage:diagonal -->
OpenAI's proof of Theorem 1.1 chooses $k$ first and keeps it fixed as $m\to\infty$ [1, §5]. Its fixed-$k$ estimates already imply a single diagonal family without an explicit rate. To see this, for each integer $j\ge2$ use $k=4j$. Choose an increasing threshold $T_j\ge j$ beyond which the fixed-$k$ bounds give $R\ge(1+Q)^{4-1/j}$ and $R\ge j$. At stage $t\ge T_2$, use the largest $j$ with $T_j\le t$, and define the finite prefix arbitrarily. Then $j\to\infty$, and the universal quartic bound again gives $Q\to\infty$ and exponent tending to four. This argument specifies no useful growth rate for $T_j$.

The distinction is therefore quantitative. Theorem 1 specifies $k$, all thresholds, and the deficit for every $t\ge80$. Slowly increasing $k$ was already discussed for the partial Forrelation problem by Bansal and Sinha [3, discussion preceding Corollary 1.4]. No priority claim is made for diagonalization or for the use of amplitude estimation.
<!-- /passage:diagonal -->

<!-- passage:obstruction -->
The displayed estimates do not yield a deficit $O(\log s/s)$. Their principal losses require both $1/k=O(\log s/s)$ and $k/s=O(\log s/s)$, which would force $k=\Omega(s/\log s)$ and $k=O(\log s)$. Those requirements are incompatible as $s\to\infty$. This diagnoses the exponential decoder cost within this proof. Improving the classical factor $k^2$ to $k$, or to an absolute constant, affects the $O(\log s/s)$ remainder. A compatible construction with decoder cost polynomial in $k$ would remove the dominant obstruction. The ordinary amplitude-estimation improvement halves the exponential coefficient and preserves the square-root-logarithm order.
<!-- /passage:obstruction -->

## 6. Input length and numerical evaluation

<!-- passage:input-length -->
The four disjoint kinds of input coordinates give the exact input length
\[
 n=m^2(1+20ks)+m^{21}\bigl[(m-1)s+20sS\bigr].
 \tag{23}
\]
The pointer coordinates alone contribute $(m-1)m^{21}s$. Using (14), for $k\ge1$ and $s\ge2$,
\[
 (m-1)m^{21}s\le n\le4022(k+1)^2m^{22}s^3.
 \tag{24}
\]
For either schedule, $k\le\sqrt s$ gives $n\le16088m^{22}s^4<2^{14}m^{22}s^4$, while $s(m-1)\ge m$. Consequently $22s\le\log_2n\le22s+4\log_2s+14$, and $\log_2n=22s+O(\log s)$. Thus the rate also has order $1/\sqrt{\log n}$ when expressed using physical input length. The sequence is indexed by powers of four in its column parameter; no padding theorem for every prescribed input length is needed for this assertion.
<!-- /passage:input-length -->

<!-- passage:numerics -->
The accompanying numerical evaluation uses the exact expanded constants $B_5$ and $B_{10}$, evaluates (17)–(18) for explicit integers $t$, and checks the schedule hypotheses. Its exponent is the guaranteed ratio $A/D$, never a measured value of $\log R/\log Q$. The complexity bounds are evaluated in logarithmic form. The calculations illustrate the proved inequalities; finite numerical tests do not establish an asymptotic theorem.
<!-- /passage:numerics -->

<!-- passage:evidence -->
**Formal evidence.** The supplied build record supports the earlier quantum upper bound, the finite Forrelation contradiction theorem, and the general planted lower bound. It expressly lists `ForrelationLower/Uniform.lean` as uncompiled. Lemma 2's uniform assembly, the single-family theorems, and the amplitude-estimation decoder and its composition are proved here in ordinary mathematics and are not asserted to be kernel-checked. The new formal interfaces include a coherent `Samples` statement; a standalone bounded-error `QLe` statement would omit the reversibility and control needed in §3. No Lean compiler is available in this review environment, and no new Lean or Comparator run was performed. Exact declarations, source locations, proposed signatures and outstanding obligations accompany this section. The supplied build receipt also has a commit-currentness qualification recorded in the source audit.
<!-- /passage:evidence -->

## References

<!-- passage:references -->
1. **OpenAI.** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. 5 October 2026. [Preprint](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). Theorem 1.1; §2 construction; Proposition 3.2 and §3.3; Proposition 4.2; §5.
2. **Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp.** *Quantum Amplitude Amplification and Estimation*. Contemporary Mathematics 305 (2002), 53–74. [arXiv:quant-ph/0005055](https://arxiv.org/abs/quant-ph/0005055). Theorem 12 and the algorithm immediately preceding it. The supplied arXiv version places Theorem 12 on printed page 19.
3. **Nikhil Bansal and Makrand Sinha.** *$k$-Forrelation Optimally Separates Quantum and Classical Query Complexity*. STOC 2021, 1303–1316. [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3). Theorem 1.3, Corollary 1.4 and the preceding growing-$k$ discussion; §5.4 for the separately audited logarithmic display.
4. **Uma Girish, Avishay Tal and Kewen Wu.** *Fourier Growth of Parity Decision Trees*. CCC 2021, LIPIcs 200, 39:1–39:36. [DOI:10.4230/LIPIcs.CCC.2021.39](https://doi.org/10.4230/LIPIcs.CCC.2021.39); [arXiv:2103.11604v2](https://arxiv.org/abs/2103.11604v2). ArXiv §1.3 and Lemma 1.9 (conference Lemma 9) for the standard decision-tree martingale argument; §3.2 for maximal inequalities.
5. **Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal.** *Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem*. STOC 2021, 1330–1342. [arXiv:2010.12629](https://arxiv.org/abs/2010.12629). The universal quartic upper bound; the explicit constant used here is supplied by the formal development's model bridge.
<!-- /passage:references -->
