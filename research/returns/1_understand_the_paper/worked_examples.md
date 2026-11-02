# Worked examples with exact numbers

These examples separate three things: a small instance of the paper's actual winner construction; abstract instances of its probabilistic tournament; and a small adaptive-query example explaining the lower-bound proof. The arithmetic was checked with exact rational numbers by `verify_examples.py`. The checks illustrate finite mechanisms; they do not verify the asymptotic separation or the Bansal–Sinha lower bound.

Source locations below count LF-separated lines of the supplied `paper/extracted.md`, matching the ledger. Form-feed characters do not add line numbers. PDF pages refer to `quartic-query-separation.pdf`.

## 1. The smallest nondegenerate legal board

Choose \(m=4\) and \(k=2\). Four is the smallest power of four larger than one. The paper's parameter choices give

| Parameter | Exact value |
|---|---:|
| Number of columns and length of each \(X_i\) | \(m=4\) |
| Forrelation order | \(k=2\) |
| Address bits per column | \(r=\lceil20\log_2m\rceil=40\) |
| Bits per pointer | \(\ell=\log_2m=2\) |
| Tournament stage cap | \(T=\lceil\log_2(1000m)\rceil=12\) |
| Comparison and sampling error target | \(\epsilon=1/12000\) |
| Classical lower-bound parameter | \(L=\lfloor\sqrt4/(\log_2 4)^2\rfloor=0\) |

Thus this example cannot exhibit the paper's randomized lower bound, which requires sufficiently large \(m\) and \(L\ge1\). It can demonstrate the exact definition, totality, pointers and tournament.

There are already \(2^{40}=1,099,511,627,776\) cells per column. We will specify their contents by a rule and display only the cells used. Calling the *entire* input a tiny four-by-four board would be misleading.

**Source:** Section 2, pp. 3–6, lines 131–132, 206–220 and 269; Proposition 3.2, p. 8, lines 363–366; Section 4.1, p. 11, line 575.

## 2. Three eight-bit Forrelation inputs

Use

\[
H=\frac12\begin{pmatrix}
1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1
\end{pmatrix},\qquad
u=\frac12(1,1,1,1)^\mathsf T.
\]

For two sign vectors, the paper's formula becomes

\[
\Phi(z_1,z_2)=\frac14z_1^\mathsf T H z_2.
\]

Set \(v=(1,1,1,-1)^\mathsf T\). Direct multiplication gives \(Hv=v\). Since \(k=2\), the thresholds are \(\delta=1/1024\) and \(\delta/2=1/2048\).

| \(z_1\) | \(z_2\) | Dot product \(z_1^\mathsf THz_2\) | \(\Phi\) | Partial answer \(P\) | Projection probability \(\Phi^2\) |
|---|---|---:|---:|---|---:|
| \((1,1,1,-1)\) | \(v\) | \(4\) | \(1\) | \(1\) | \(1\) |
| \((1,1,-1,1)\) | \(v\) | \(0\) | \(0\) | \(0\) | \(0\) |
| \((-1,-1,-1,1)\) | \(v\) | \(-4\) | \(-1\) | Undefined | \(1\) |

The third row makes the promise issue concrete. The quantum projection experiment gives exactly the same success probability as on the first row, so the paper's threshold decoder returns one. Nevertheless, \(P\) is undefined there: a negative value of magnitude one satisfies neither defining case. Off-promise decoding does not certify domain membership.

The exact classical circuit distinguishes these cases. With \(W=2H\), its integer numerator is \(N=z_1^\mathsf TWz_2\), and \(\Phi=N/8\). The three numerators are \(8,0,-8\). Testing

\[
2^{10}N\ge8,\qquad 2^{11}|N|\le8
\]

gives circuit outputs \((d,b)=(1,1),(1,0),(0,0)\), respectively. A truthful transcript for the third input cannot pass the required output test \(d=1\).

The script enumerates all \(16\times16=256\) sign-vector pairs. It finds 104 one-inputs, 48 zero-inputs and 104 undefined inputs, and checks the integer tests against the partial definition for every pair.

**Source:** Lemma 2.1 and Eqs. (3)–(4), pp. 3–4, lines 134–197; output tests in Lemma 2.2, p. 6, lines 276–282. The values and enumeration are calculations for this example.

## 3. An actual winner with outward pointers

Assign every \(A_{i,h}\) the second Forrelation input above. These occupy separate input slots; we assign them equal values rather than identifying their bits. All 40 answers in each column are zero, giving true address \(0^{40}\). The projection probability is zero, so this address is decoded deterministically correctly by the paper's repeated-projection threshold procedure.

Display the four \(X\)-strings vertically:

| Row | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 | 1 |
| 3 | 1 | 1 | 1 | 0 |
| 4 | 1 | 1 | 1 | 1 |

At each column's cell \(B_{i,0^{40}}\), set these pointer targets. Entries are **row numbers in the destination column**:

| Source column | To 1 | To 2 | To 3 | To 4 |
|---|---:|---:|---:|---:|
| 1 | — | 1 | 2 | 3 |
| 2 | 1 | — | 2 | 1 |
| 3 | 1 | 2 | — | 3 |
| 4 | 1 | 1 | 1 | — |

For definiteness, encode rows 1–4 by \(00,01,10,11\). In \(B_{1,0^{40}}\), put the truthful evaluations of the paper's fixed exact circuit \(C\) on all 40 address instances. Set other cell bits to zero except for the displayed pointers. Once \(C\) is chosen, its truthful transcripts are uniquely determined; we do not expand its unspecified gate list here.

Column 1 wins. Its own string is all ones; its address is defined; its transcript is correct; and its pointers find

\[
X_2[1]=X_3[2]=X_4[3]=0.
\]

Every other column fails the all-ones condition. No opponent can disqualify column 1, since all four possible pointer targets in \(X_1\) contain one.

If \(C\) has \(S\) non-input gates, the exact number of verification tests is

\[
K=4+3+40(S+2)=87+40S.
\]

Each cell contains \(6+40S\) bits. Each column contains four \(X\)-bits, \(40\cdot8=320\) address-instance bits and \(2^{40}\) cells. The complete input therefore has

\[
N_{\rm input}=1296+2^{42}(6+40S)
\]

bits. The four-by-four display is its visible pointer mechanism, not its complete storage footprint.

**Source:** winner definition and input layout, p. 5, lines 206–236; Lemma 2.2, p. 6, lines 264–292. Formula counts are direct substitutions.

### Breaking the promise does not defeat the winner

Change all 40 address instances of column 2 to the undefined negative example. Its decoder now returns \(1^{40}\), although no true address exists. Every pointer at that proposed cell still targets a one in \(X_1\). Column 1's correct outward pointer still finds \(X_2[1]=0\), so column 1 defeats column 2. The example does not require any correctness guarantee for column 2's decoding.

**Source:** off-promise comparison argument, p. 10, lines 466–482.

### Breaking a pointer exposes why verification is necessary

Instead leave the address instances unchanged, but change column 1's pointer toward column 2 from row 1 to row 2. It now points to \(X_2[2]=1\). Column 1 is no longer a winner, and nobody else can win, so \(F=0\).

Yet column 1 still defeats column 2 in the comparison: neither disqualifies the other, and the smaller-index tie-break chooses column 1. Its other comparisons are unchanged. A candidate can dominate the tournament while failing the actual winner definition. The final verifier detects the failed pointer test.

**Source:** comparison tie-break, p. 10, lines 466–471; verification, lines 483–494. This counterexample to “dominant implies winner” is an exact calculation, not a flaw in the paper, which does verify candidates.

## 4. The board's cyclic tournament

For the unchanged board, 2 disqualifies 3, 3 disqualifies 4, and 4 disqualifies 2. Each reverse pointer lands on one. The exact comparison matrix is

\[
a=\begin{pmatrix}
0&1&1&1\\0&0&1&0\\0&0&0&1\\0&1&0&0
\end{pmatrix},
\]

where row \(i\), column \(j\) means the probability that \(i\) defeats \(j\). The three losers form a cycle; they cannot be placed in a consistent best-to-worst order.

Start the *ideal* process with weights \((1,1,1,1)\). Each first pivot has probability \(1/4\).

| First pivot | Updated weights | Updated total |
|---|---|---:|
| 1 | \((0,0,0,0)\) | 0 |
| 2 | \((1,0,0,1)\) | 2 |
| 3 | \((1,1,0,0)\) | 2 |
| 4 | \((1,0,1,0)\) | 2 |

Thus \(\mathbb E W_1=(0+2+2+2)/4=3/2\). The drift identity agrees:

\[
\frac{W_0^2-\sum_iw_i^2}{2W_0}=\frac{16-4}{8}=\frac32.
\]

After a first loser pivot, the next pivot is equally likely to be candidate 1 or the sole surviving loser. If that loser is chosen, only candidate 1 remains. The exact miss probabilities after one, two and three pivots are therefore

\[
\frac34,\qquad\frac34\cdot\frac12=\frac38,\qquad0.
\]

These are probabilities for the ideal weight process. The bounded quantum implementation can additionally report a sampling failure; Proposition 3.2 accounts for that separately.

**Source:** ideal update, drift and sampling guarantee, pp. 8–9, lines 379–442. All listed probabilities were exhaustively enumerated over the finite pivot histories.

## 5. Fractional weights, without pretending to have a fixed order

This is a separate abstract instance of Proposition 3.2. We do **not** claim its comparator arises from the displayed board. Candidate 1 always defeats each opponent, and every pair of losers is decided by a fair coin:

\[
a=\begin{pmatrix}
0&1&1&1\\0&0&1/2&1/2\\0&1/2&0&1/2\\0&1/2&1/2&0
\end{pmatrix}.
\]

After pivot 2, the weights are \((1,0,1/2,1/2)\), with total two. The next pivot probabilities are

\[
(1/2,0,1/4,1/4).
\]

This is precisely what successful quantum sampling must preserve. Replacing each fractional comparison with a deterministic “which side is above one half?” rule would destroy this example's intended process.

If pivot 3 comes next, the weights become \((1,0,0,1/4)\). Hence the next pivot is 1 with probability \(4/5\) and 4 with probability \(1/5\). The ideal miss probabilities are

\[
\frac34,\quad\frac38,\quad\frac38\cdot\frac15=\frac3{40},\quad0.
\]

At the state after pivot 2, the expected next total is

\[
\frac{2^2-(1+1/4+1/4)}{2\cdot2}=\frac58.
\]

Directly, the next pivot is 1 with probability \(1/2\), giving zero total, or a loser with combined probability \(1/2\), giving total \(5/4\). The expectation is again \(5/8\).

**Source:** Proposition 3.2, especially Eqs. (12)–(15), pp. 8–9. This matrix and the exact calculations are constructed examples.

## 6. Amplification preserves relative successful probabilities

Take orthonormal states \(|g_1\rangle,|g_2\rangle,|b\rangle\), with the first two designated successful, and prepare

\[
|\psi\rangle=\frac3{10}|g_1\rangle+\frac4{10}|g_2\rangle+\frac{\sqrt3}{2}|b\rangle.
\]

The total success probability is \(9/100+16/100=1/4\). Conditional on success, the normalized state is

\[
|g\rangle=\frac35|g_1\rangle+\frac45|g_2\rangle,
\]

with outcome probabilities \(9/25\) and \(16/25\). Here \(\sin\theta=1/2\), so \(\theta=\pi/6\). One Grover iteration gives

\[
\sin(3\theta)|g\rangle+\cos(3\theta)|b\rangle=|g\rangle.
\]

Success has increased from \(1/4\) to one, but the two successful outcomes retain their unequal probabilities \(9/25,16/25\). Amplification has not made them uniform. This is the exact property required for the tournament's weighted law.

The script checks the same calculation without approximating \(\sqrt3\): one iteration multiplies each good amplitude by \(3-4p=2\) and the bad amplitude by \(1-4p=0\).

**Source:** Lemma 3.1, p. 7, lines 321–330; BHMT, §2 Eq. (8), https://arxiv.org/abs/quant-ph/0005055.

## 7. Why conditioning on “nonheavy” is dangerous

Consider the tiny partial-function analogue \(P(a,b)=a\land b\), defined on every two-bit input, with all four inputs equally likely. Set the query allowance to \(L=1\). The best success probability with at most one query is \(\beta=3/4\): after seeing a zero, answer zero; after seeing a one, the other bit remains a fair coin. Constantly answering zero also achieves \(3/4\).

Now run an algorithm that first queries \(a\). If \(a=0\), output zero immediately. If \(a=1\), query \(b\) and output it. This algorithm is always correct, but sometimes uses two queries.

| Input | Queries | Correct output | Uses at most \(L\) queries? |
|---|---:|---:|---|
| 00 | 1 | 0 | Yes |
| 01 | 1 | 0 | Yes |
| 10 | 2 | 0 | No |
| 11 | 2 | 1 | No |

Calling the first two runs “nonheavy” gives

\[
\Pr(\text{correct}\mid\text{nonheavy})=1>\beta.
\]

Conditioning has selected the easy inputs. The original one-query hardness statement says nothing that bounds this conditional success by \(3/4\).

The joint event has probability

\[
\Pr(\text{nonheavy and correct})=1/2.
\]

A simulator that aborts before the second query and outputs zero uses at most one query on *every* input. Its success probability is \(3/4\), and the joint event above implies simulator success. This is the valid comparison used in the paper. For two independent copies, the all-nonheavy joint event has probability \(1/4\), while the capped simulator succeeds on both with probability \(9/16\).

**Source:** Lemma 4.1, pp. 11–12, lines 528–573; the joint-event simulator, p. 13, lines 639–659. The AND example is illustrative and is not the paper's hard Forrelation distribution.

## Reproduce the checks

Run:

```bash
python verify_examples.py --output exact_example_results.json
```

The script uses Python's standard-library `Fraction`, exact matrix arithmetic and complete finite enumeration. It checks the 256 Forrelation pairs, the board's comparisons and broken-pointer variant, the ideal tournament histories, amplification ratios and one-query AND optimum. It does not instantiate the unspecified circuit \(C\) gate by gate or simulate the entire quantum algorithm.
