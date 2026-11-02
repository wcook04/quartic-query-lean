# The retained four-term threshold

This note preserves the argument previously recorded as NEW-FOR-25. It is supplementary to the replacement section; its substantially larger sufficient threshold is not needed for the new §3.15. Nothing in this note changes the fixed-parameter statement or claims optimality of a cutoff.

<!-- passage:forr_historical_threshold -->
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

This proof preserves the former threshold route. The replacement section instead uses the current sharp uniform theorem to obtain the simpler sufficient threshold $t\ge13669k^2$. The latter is a new ordinary specialization; the current source also contains a separately named explicit, coarser threshold $t\ge3499200k^2$. No claim is made that either new wrapper was compiled during this review.
<!-- /passage:forr_historical_closure -->
