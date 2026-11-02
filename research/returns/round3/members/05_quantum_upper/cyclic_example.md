<!-- passage:upper-cyclic-example -->
**An exact four-candidate example.** Let the candidates be \(s,a,b,c\).
Here \(T=\lceil\log_2(4000)\rceil=12\) and
\(\varepsilon=1/12000\). The entry in row \(i\), column \(j\) of the
following table is the probability that \(i\) defeats \(j\).

| \(a_{ij}\) | \(s\) | \(a\) | \(b\) | \(c\) |
|---|---:|---:|---:|---:|
| \(s\) | \(0\) | \(1-\varepsilon\) | \(1-\varepsilon\) | \(1-\varepsilon\) |
| \(a\) | \(\varepsilon\) | \(0\) | \(1\) | \(0\) |
| \(b\) | \(\varepsilon\) | \(0\) | \(0\) | \(1\) |
| \(c\) | \(\varepsilon\) | \(1\) | \(0\) | \(0\) |

The candidate \(s\) is dominant, while the other three have the cycle
\(a\) defeats \(b\), \(b\) defeats \(c\), and \(c\) defeats \(a\).
There is no total ordering consistent with these three certain comparisons.

Suppose the first pivot is \(a\). The weights become
\[
 (w_s,w_a,w_b,w_c)=(11999/12000,0,0,1),
 \qquad W=23999/12000.
\]
The unamplified preparation succeeds with probability
\(W/4=23999/48000\). Conditioned on success, the next pivot is
\(s\) with probability \(11999/23999\) and \(c\) with probability
\(12000/23999\). Bounded amplification changes the probability of obtaining
a sample, while preserving these two conditional probabilities exactly.
If the next pivot is \(c\), the only remaining positive weight is
\(w_s=(11999/12000)^2\), so the following successful sample is \(s\).

The first-step total weight is \(3\varepsilon\) if the pivot is \(s\),
and \(2-\varepsilon\) for each of the other three pivots. Since the first
pivot is uniform, its expected value is
\[
 \frac{3\varepsilon+3(2-\varepsilon)}4=\frac32
 =\frac{4^2-4}{2\cdot4}.
\]
This is the exact drift identity in a cyclic example. The ideal process selects
\(s\) within three pivots with probability one. The example illustrates the
weight calculation and conditional law; it is neither a construction of the
full addressed-certificate input nor a proof of the general tournament bound.
<!-- /passage:upper-cyclic-example -->
