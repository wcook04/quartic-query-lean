# A written proof of the constant 508 in the growing-k bound (for record §7.3)

The expert companion's §7 remark states

$$
R(F_t)\ge Q(F_t)^{4-\varepsilon(\ell)},\qquad
\varepsilon(\ell)=8\sqrt{\frac{10}{\ell}}+\frac{56\log_2\ell+508}{\ell},
$$

for $F_t=F_{k,4^t}$, $k=\lfloor\sqrt{t/20}\rfloor$, $t\ge80$ and $\ell=2t$. Record §7.3 (`#ROOT-GROWING-K`) proves this with $514$ in place of $508$.

The record's chain loses 20 in one step, the bound on $40k+\ell/k$. With that step sharpened, the same chain gives $4B-A\le2\sqrt{40\ell}+28\log_2\ell+237$. That proves the constant $474$, hence $508$ a fortiori. Every other step is the record's, unchanged. The record may adopt 508, to match the companion, or 474.

## The one changed step

The notation is the record's: $x=\sqrt{\ell/40}$, $k=\lfloor x\rfloor$, so $k\ge2$, $0\le x-k<1$ and $\ell=40x^2$.

The record bounds $40k+\ell/k$ by monotonicity and $k\ge x-1$, which gives $\le80x+40/(x-1)\le2\sqrt{40\ell}+40$. Instead, write the excess over $80x$ exactly:
$$
40k+\frac{\ell}{k}-80x=40k+\frac{40x^2}{k}-80x=\frac{40}{k}\bigl(k^2-2kx+x^2\bigr)=\frac{40(x-k)^2}{k}.
$$
Since $0\le x-k<1$ and $k\ge2$, this is less than $40/2=20$. Moreover $80x=2\sqrt{40\ell}$, because $\sqrt{40\ell}=\sqrt{1600x^2}=40x$. Hence
$$
40k+\frac{\ell}{k}\le2\sqrt{40\ell}+20 .
$$

## The full chain with the changed step

**Logarithms of the two bounds.** Let $A$ and $B$ be the base-two logarithms of the right sides of (7.6) and (7.5):
$$
A=\Bigl(2-\frac1k\Bigr)\ell-\log_2\bigl(1822500\,k^2\ln(4km)\bigr),\qquad
B=\frac\ell2+10k+53+\log_2k+6\log_2\ell .
$$
Here $B=\log_2\bigl(2^{53}k\,2^{10k}\,2^t\,\ell^6\bigr)$, since $t=\ell/2$. By (7.6) and (7.5), $\log_2R(F_t)>A$ and $\log_2Q(F_t)\le B$.

**The gap $4B-A$.** Expanding $4B$ and subtracting $A$ gives
$$
4B-A=40k+\frac{\ell}{k}+212+6\log_2k+\log_2 1822500+\log_2\ln(4km)+24\log_2\ell .
$$
The $2\ell$ terms cancel, the $\ell/k$ term comes from $-(2-1/k)\ell$, and $6\log_2 k=4\log_2k+2\log_2k$.

**Bounding the terms.**
1. $40k+\ell/k\le2\sqrt{40\ell}+20$, by the changed step above.
2. $6\log_2k\le6\log_2x=3\log_2(\ell/40)=3\log_2\ell-3\log_240<3\log_2\ell-15.96$, since $3\log_240=15.965\ldots$.
3. $\log_21822500<20.80$, since $\log_21822500=20.797\ldots$.
4. $\log_2\ln(4km)\le\log_2\ell$, because $\ln(4km)\le\ell$. This is the record's step: $\ln(4k)\le(1-\ln2)\,2t$ for $k\le2t/15$, so $\ln(4km)=\ln(4k)+2t\ln2\le2t=\ell$.

**Adding.**
$$
4B-A\le2\sqrt{40\ell}+(20+212-15.96+20.80)+(3+1+24)\log_2\ell
=2\sqrt{40\ell}+28\log_2\ell+236.84 .
$$
Hence $4B-A\le2\sqrt{40\ell}+28\log_2\ell+254$ with room to spare.

**From the gap to $\varepsilon(\ell)$.** Note that $2\cdot2\sqrt{40\ell}/\ell=4\sqrt{40/\ell}=8\sqrt{10/\ell}$. Therefore
$$
\frac{2(4B-A)}{\ell}\le8\sqrt{\frac{10}{\ell}}+\frac{56\log_2\ell+508}{\ell}=\varepsilon(\ell).
$$

**Conclusion.** This is the record's argument without change.
- If $4B\le A$, then $A\ge4B\ge(4-\varepsilon(\ell))B$.
- Otherwise $B\ge\ell/2$ gives $(4B-A)/B\le2(4B-A)/\ell\le\varepsilon(\ell)$, so again $A\ge(4-\varepsilon(\ell))B$.

$F_t$ is not constant, so $Q(F_t)\ge1$ and $\log_2Q(F_t)\ge0$.
- If $\varepsilon(\ell)<4$: $\log_2R(F_t)>A\ge(4-\varepsilon(\ell))B\ge(4-\varepsilon(\ell))\log_2Q(F_t)$.
- If $\varepsilon(\ell)\ge4$: the right side $Q(F_t)^{4-\varepsilon(\ell)}$ is at most $1\le R(F_t)$.

So $R(F_t)\ge Q(F_t)^{4-\varepsilon(\ell)}$ for every $t\ge80$.

## Numerical cross-check (not part of the proof)

Evaluating $4B-A-2\sqrt{40\ell}-28\log_2\ell$ exactly for every $t=80,\dots,19999$ and for $t=10^5,10^6,10^8$ gives a largest value of $232.50$. This is below the proved bound $236.84$, which is consistent. The same scan confirms $40(x-k)^2/k\le20$ at every point.

## Link status in the companion

The companion's §7 remark now links to record §7.3 at `#ROOT-GROWING-K`. Its §8 links to Appendix G.4 (`#checked-statements`) and G.8 (`#CL-direct-product-formal`). The anchors `ROOT-GROWING-K` and `CL-direct-product-formal` do not yet exist at the commit `tools/build_lean_links.py` pins (`e9dfefb`), so its `--check`, and hence `make check`, fails until `COMMIT` is bumped to a commit containing the revised record. The section labels in the companion's link text (§7.3, G.4, G.8) already follow the revised record.
