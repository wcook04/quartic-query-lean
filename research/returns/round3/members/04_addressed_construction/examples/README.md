# An exact four-column example

This example illustrates the addressed certificate construction in the supplied
OpenAI preprint, §2.2 and Lemma 2.2 (printed pp. 5–6). It uses the actual
partial function $P_{2,4}$, with four-coordinate sign vectors and

\[
\Phi(z_1,z_2)=\frac{z_1^T Wz_2}{8},\qquad
W=\begin{pmatrix}
1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1
\end{pmatrix},\qquad \delta=2^{-10}.
\]

Bits represent signs by $a\mapsto(-1)^a$. The numerator $N=z_1^TWz_2$
is an integer. The checker uses the original comparisons

\[
P_{2,4}(a)=1\ \Longleftrightarrow\ 2^{10}N\geq8,
\qquad
P_{2,4}(a)=0\ \Longleftrightarrow\ 2^{11}|N|\leq8.
\]

All other inputs are outside the promise. Direct rational matrix evaluation
independently checks these integer comparisons on all 256 inputs.

## What is schematic

There are four columns and two pointer bits, as in the construction at $m=4$.
We use **two** address instances per column, so each column has four cells.
The separation family would instead use $r=40$, giving $2^{40}$ cells
per column. We also synthesize the exact two-output circuit from its finite
truth table, rather than use the preprint's efficient Walsh arithmetic circuit.
This synthesized circuit has $S=180$ non-input gates. Its domain and value
output gates are respectively 178 and 179 under zero-based gate numbering;
both gates are included in $S$. The circuit uses AND, OR, NOT and COPY,
each with at most two predecessors.

These choices preserve the certificate logic while making the full input easy
to inspect. They do not exemplify or establish the asymptotic separation, the
large-$m$ Forrelation lower bound, or the asymptotic circuit-size proof.
This is an ordinary exact computation, with no new Lean claim.

## The three address inputs

The space in each input word in the next table separates the two four-bit
blocks; it is not an input coordinate. Each transcript is the complete
180-bit evaluation of the synthesized circuit.

| Name | Eight input bits | $N$ | $\Phi$ | $P_{2,4}$ | Circuit $(d,b)$ |
|---|---|---:|---:|---:|---:|
| $a_+$ | `0000 0000` | 4 | $1/2$ | 1 | $(1,1)$ |
| $a_0$ | `0001 0010` | 0 | $0$ | 0 | $(1,0)$ |
| $a_-$ | `1111 0000` | −4 | $−1/2$ | undefined | $(0,0)$ |

For example, $a_0$ gives $z_1=(1,1,1,-1)$,

\[
Wz_2=(2,-2,2,2)^T,
\qquad z_1^TWz_2=2-2+2-2=0.
\]

## The complete board

Columns and rows in this description are numbered 1 through 4. Pointer words
are big endian: `00`, `01`, `10`, `11` indicate rows 1, 2, 3, 4. Addresses
are also big endian, with their first bit the first partial-function answer.

| Column | $X_i$ | Address inputs | Partial-function values |
|---|---|---|---|
| 1 | `1111` | $(a_+,a_0)$ | $(1,0)$ |
| 2 | `0111` | $(a_-,a_0)$ | $(\text{undefined},0)$ |
| 3 | `1011` | $(a_+,a_0)$ | $(1,0)$ |
| 4 | `1101` | $(a_+,a_0)$ | $(1,0)$ |

Every cell stores the correct evaluation transcripts for its column's two
address inputs. Every pointer into a column $j\in\{2,3,4\}$ points to
that column's unique zero, wherever that pointer occurs. Thus the pointers
from column 1 into columns 2, 3, 4 are `00`, `01`, `10`, respectively.
For every rival column and each cell address $s\in\{00,01,10,11\}$, its
pointer into column 1 is the word $s$. This specifies every pointer and every
cell, including unselected cells. The exact complete bit input is in
`board.json`; its circuit is in `circuit.json`.

Column 1 wins at address `10`. Its own four bits are one; all three pointers
reach zeros; both transcripts are correct; and their outputs are $(1,1)$
and $(1,0)$. The other addresses in column 1 fail at least one value-output
test. Every other column has a zero in its own $X$-block. Column 2 also has
no true address: its first partial-function input is outside the promise.

## Local tests and the query count

Here the exact number of tests per candidate is

\[
K=4+3+2(180+2)=371.
\]

The following counts are computed by reading individual physical input bits.
Repeated reads count as separate queries.

| Family | Number | Pass at $(1,10)$ | Pass at $(2,00)$ | Maximum queries per test |
|---|---:|---:|---:|---:|
| Own column bits | 4 | 4 | 3 | 1 |
| Outward zero pointers | 3 | 3 | 2 | 3 |
| Gate consistency | 360 | 360 | 360 | 3 |
| Domain and value outputs | 4 | 4 | 3 | 1 |
| Total | 371 | 371 | 368 | 3 |

At rival label `00`, both value-output tests pass and the second domain test
passes. Its first domain test fails because its correct transcript has $d=0$.
The true transcripts therefore do not make its off-promise input valid.

The checker evaluates all 371 tests for all 16 candidate pairs, for 5,936
test evaluations. It independently compares their conjunction with the semantic
winner definition. Exactly the pair $(1,10)$ passes. Coincidentally, this
particular board also has 5,936 physical bits; the two counts refer to different
objects.

The pointer from $(1,10)$ to column 4 is read in this order: its first bit
is 1, its second bit is 0, then the algorithm queries $X_4[3]=0$. The
third query location depends on the first two answers. The separate exhaustive
six-variable lookup check shows that both pointer bits and all four target
bits are essential coordinates, although the adaptive query depth is three.
The full set of six witnesses is in `output.json`.

## Why an arbitrary rival label is harmless to a true winner

Condition on decoding column 1's correct label `10`. Its pointer into any
rival finds a zero. In the other direction every row of $X_1$ equals one,
so no rival pointer can disqualify column 1. The checker covers all three
rivals, all four proposed rival labels, and all four possible incoming pointer
targets: 48 cases. Column 1 wins every case. This is a deterministic conditional
fact. The probability bound $1-\varepsilon$ in the general proof follows
when the true winner's label is decoded with that probability; the checker
does not simulate a quantum decoder.

There is a concrete reason an off-promise rival can receive a plausible
decoded bit. For the preprint's specified projection test, the success
probability is the square of the Forrelation value. Here the positive input
has value $1/2$ and the off-promise input has value $-1/2$, so **both
projection success probabilities are exactly $1/4$**. Each has the same
single-trial law: failure with probability $3/4$, success with probability
$1/4$. For any fixed number of independent repetitions, an ordered pattern
with $h$ successes among $n$ trials has probability

\[
(1/4)^h(3/4)^{n-h}
\]

on either input. Any subsequent decision rule using only these outcomes
therefore has the same output distribution. In particular, the prescribed
threshold decoder can give the off-promise input the same plausible value
label as the positive input, while the exact circuit still rejects its
domain membership. The checker verifies the equality of the rational squared
values and, as a finite illustration, all eight ordered outcome probabilities
for three independent trials. The statement for any fixed number of trials
is the displayed product-law deduction. This comparison concerns this
projection decoder, not all quantum algorithms.

## A mutation that explains the domain test

Change $X_1$ to `1110` and $X_2$ to `1111`, keeping the address inputs
and true transcripts. Redirect every pointer into a column other than 2 to
that column's zero. Column 2 is now the sole all-one column and, at proposed
address `00`, all its outgoing pointers and gate tests pass. Both value-output
tests also pass. Its first domain-output test is the **sole** failure:
370 of the 371 tests pass, and the semantic total function equals zero.

If the two domain-output tests are omitted, all 369 remaining tests pass.
Thus gate consistency and a proposed value address alone would accept this
off-promise column incorrectly. This is a direct counterexample to dropping
domain recognition from the certificate checks.

A different corruption changes the rival's claimed domain output from zero
to one in its original cell `00`. All four output tests then pass, but the
domain output gate's consistency test fails. Finally, the checker flips each
of the 360 bits of column 1's two selected transcripts separately: every flip
breaks that gate's own equation and changes the total function to zero.
This last check covers individual flips, not every possible multi-bit forgery.

## Reproduction and scope

Run from this directory:

```sh
python3 check_example.py > reproduced.json
python3 check_example.py --write-data regenerated > reproduced.json
```

The first command emits the summary and checks; the second also regenerates
`circuit.json` and `board.json`. Output is deterministic and uses only Python's
standard library. No floating-point comparisons, external dependencies or
network requests are used.

Source scope assessed for this example: the packet request; baseline §§1.1,
3.17, 4 and 5.3; and the supplied preprint §2.2/Lemma 2.2. The example was
constructed independently from those definitions. It is a finite semantic
check and an exposition aid. It does not replace the general proof, audit
the entire separation, or certify the current Lean source.
