# An adaptive two-input tree and a misleading conditional probability

Let \(A=(A_0,A_1)\) and \(B=(B_0,B_1)\) be independent uniform pairs of bits,
and let \(P(x)=x_0\wedge x_1\). Set the separate query cap to \(L=1\).
Every one-query algorithm for one input succeeds with probability at most
\(\beta=3/4\): after observing a zero it knows the answer, whereas after
observing a one its best success probability is \(1/2\). Their average is
\(3/4\), also achieved by the constant answer zero.

Consider this tree, which is allowed to exceed the cap on some runs:

1. Query \(A_0\), receiving \(a\).
2. Query \(B_a\), receiving \(t\). Thus the queried coordinate of \(B\)
   depends on the answer obtained from \(A\).
3. If \(a\ne t\), query \(A_0\) a second time.
4. Output \((0,0)\).

The repeated query reveals no new information, but it is still charged.
Consequently the event \(E\) that both per-input caps hold is exactly
\(\{a=t\}\). Each of the four histories following step 2 has probability
\(1/4\).

| \(a\) | Second query | \(t\) | Conditional probability both answers are correct | Final counts | Caps hold? |
|---:|:---:|---:|:---:|:---:|:---:|
| 0 | \(B_0\) | 0 | \(1\) | \((1,1)\) | Yes |
| 0 | \(B_0\) | 1 | \(1/2\) | \((2,1)\) | No |
| 1 | \(B_1\) | 0 | \(1/2\) | \((2,1)\) | No |
| 1 | \(B_1\) | 1 | \(1/4\) | \((1,1)\) | Yes |

For each fixed two-query history the compatible inputs form the rectangle
\(\{A:A_0=a\}\times\{B:B_a=t\}\), and their conditional law is the product
of the two uniform restricted laws. The coordinate \(a\) in the second
constraint is fixed once the history is fixed. The table entries are the
corresponding products of one-input continuation values with zero queries
remaining. They average to \(9/16=\beta^2\).

Let \(C\) be the event that the output vector is correct. Direct enumeration
gives

\[
\Pr(E)=\frac12,\qquad
\Pr(C\cap E)=\frac14+\frac1{16}=\frac5{16},\qquad
\Pr(C\mid E)=\frac58>\frac9{16}=\beta^2.
\]

The joint-event direct-product bound holds. The analogous conditional bound
fails. The event \(E\) is a union of transcript rectangles, and conditioning
on that union need not preserve independence. Indeed,

\[
\Pr(A_0=0\mid E)=\frac12,\qquad
\Pr(B_0=0\mid E)=\frac34,\qquad
\Pr(A_0=B_0=0\mid E)=\frac12\ne\frac38.
\]

To apply the all-branches capped theorem, truncate immediately before the
repeated query and output \((0,0)\) there. The truncated tree has at most one
query to each input on every branch. Every original run in \(C\cap E\)
remains successful for the truncated tree. Its success probability is
\(9/16\), bounding the original joint probability \(5/16\). Alternatively,
a potential killed on the attempted excess query retains only the first and
fourth table rows, with expectation \(5/16\).

The same input law also illustrates why a global budget \(rL\) cannot replace
the separate caps. With two queries in total, read both bits of \(A\), output
\(P(A)\) exactly, and guess zero for \(P(B)\). This succeeds with probability
\(3/4>9/16\). A global budget of \(L\), by contrast, implies every separate
cap of \(L\) and does satisfy the theorem.

## Exact check and its scope

Run `python3 checks/check_adaptive_example.py` from the return directory. The script checks all 16 input pairs
using exact rational arithmetic; verifies the transcript rectangle and
conditional product law at each positive history; checks that the repeated
queries are counted and their contradictory-answer branches have zero mass;
and verifies every fraction displayed above. It also
enumerates all 10 single-input Boolean-output trees of depth at most one and
all 5,188 two-input vector-output trees obeying the separate caps, finding
maximal successes \(3/4\) and \(9/16\), respectively.

This is an independently authored finite semantic check. It is neither a
proof of the general direct-product theorem nor a Lean compilation or
Comparator receipt.
