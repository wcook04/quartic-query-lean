# Understanding and auditing the nearly quartic query separation

## Reading this report

This is an advisory mathematical audit of OpenAI’s **A Nearly Quartic Separation Between Randomized and Quantum Query Complexity**, dated 5 October 2026, as supplied in the packet. It is not a new paper, a peer-review acceptance, or a formal verification. I read the entire manuscript, reviewed all 118 ledger entries, reconstructed its principal proof steps, checked the external Forrelation theorem’s interface against its original source, and checked the worked examples exactly. The detailed calculations are in `proof_audit.md`; each ledger entry has an individual review in `statement_review.json`.

**Assessment:** I did not find a fatal mathematical gap in the supplied proof. The two most delicate steps—the quantum tournament on off-promise inputs and the adaptive classical address-guessing bound—survive direct reconstruction. There is a real ledger error about pointer tests, several formalisation conventions to settle, a line-numbering convention to preserve, and a substantial difference between the present evidence and an unconditional Lean verification. The latest build notification in the supplied trace is a failure, not a successful check of `Drift.lean`.

Throughout, **[P]** means the supplied manuscript. A locator such as “P LF lines 221–236” refers to physical, one-based LF-delimited lines of the supplied `paper/extracted.md`, matching the original ledger. The source contains form-feed page breaks; do not use Python `splitlines()` for these locators, because it also splits form feeds. Numbered references such as **[6]** retain the manuscript’s numbering; public links and precise reading suggestions appear in `further_reading.json`. The statement review and audit findings also give file/section locations. External theorems are identified rather than treated as newly reproved here.

## 1. What the theorem actually says

Imagine a known Boolean function \(f\) whose input is hidden in an array of bits. You may ask for input bits, one query at a time. The task is to output the value of \(f\), with error at most \(1/3\) on **each** input. We charge for queries; other computation is free. The theorem asks how far quantum access can reduce this query count compared with the best classical randomized procedure. [P pp. 1–3, LF lines 16–43 and 117–123.]

For every fixed integer \(k\ge2\), the paper constructs total Boolean functions \(F_{k,m}\), for sufficiently large powers of four \(m\), satisfying

\[
Q(F_{k,m})\le C_k\sqrt m\,(\log m)^{b_k},\qquad
R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log m)^2}.
\]

Here \(R\) is randomized query complexity and \(Q\) is quantum query complexity. Ignore logarithms temporarily: the quantum algorithm pays roughly \(m^{1/2}\), while every classical algorithm pays roughly \(m^{2-1/k}\). Dividing the exponents gives

\[
\frac{2-1/k}{1/2}=4-\frac2k.
\]

This is why the result is **nearly quartic**. For any proposed universal exponent strictly below four, one can choose a fixed \(k\) large enough to beat it, then let \(m\) grow. The proof does not give a fixed-\(k\) family with an exact fourth-power lower bound. In particular, \(k=2\) reaches exponent three; \(k=3\) reaches \(10/3\) and already refutes the conjectured universal cubic relation. [P §5, LF lines 692–712; calculations reproduced below.]

The converse bound was already known: every total Boolean function satisfies \(R(f)\le D(f)=O((1+Q(f))^4)\), where \(D\) is exact deterministic query complexity. The new contribution is the family showing that this exponent cannot be lowered for randomized complexity. The earlier upper-bound paper is Aaronson, Ben-David, Kothari, Rao and Tal [3], Theorem 2; its Conjecture 2 proposes the stronger cubic relation. [P §1.1 and Appendix A; [ABKRT](https://arxiv.org/abs/2010.12629).]

This is a result about input-query complexity. It does not claim a practical fourth-power improvement in elapsed time, memory, gate count or data-loading cost. That distinction is especially visible here: the input contains a very large array of certificate cells.

## 2. The basic objects, before the construction

### Randomized and quantum queries

A deterministic decision tree chooses a bit to inspect, branches on its value, and eventually outputs a bit. Its depth is the largest number of queries on any path. A randomized algorithm is a probability distribution over such trees. \(R(f)\) is the least depth cap for which that mixture is correct with probability at least \(2/3\) on every allowed input. It is a worst-case cap, including every possible random tape. The lower bound does not use expected cost. [P LF lines 18–25 and 575–589.]

The quantum oracle is the reversible map

\[
O_x|i,b,z\rangle=|i,b\oplus x_i,z\rangle.
\]

The index \(i\) names the bit, \(b\) is an answer bit, and \(z\) is workspace. This map acts linearly on superpositions. Quantum interference can make a useful global feature of the input affect the eventual measurement distribution. It does not provide a list of all the input bits in one query. \(Q(f)\) counts uses of this oracle, with arbitrary input-independent operations between queries. The paper permits exact finite-dimensional unitaries, measurements, and classical control with a uniform query cap. [P LF lines 20–25, 507–512 and 751–754.]

### Partial and total functions

A **partial** Boolean function has a specified domain \(D\subseteq\{0,1\}^n\). Its algorithm only has to be correct when the input belongs to \(D\); this restriction is its promise. A **total** Boolean function has a required answer on every bit string. Large quantum advantages for promise problems do not automatically yield equally large advantages for total functions. [P LF lines 117–150; [1], introductory definitions.]

The decoder used in this construction has two separate obligations: correctness on the promise, and a fixed query cap plus a well-defined output bit on all inputs. Off-promise correctness has no meaning, but off-promise execution still needs to be controlled. The full function \(F\) must also reject invalid accepting witnesses exactly according to its total definition.

### Certificates and cheat sheets

A certificate for \(f(x)\) is a partial assignment to input coordinates that forces that value: every full input extending that assignment has the same function value. Knowing which certificate to inspect can be much easier than finding it. In a cheat-sheet construction, input space contains a large table of proposed certificates; the answers to several hard partial-function instances jointly specify the address of the relevant table cell. The certificate must also establish that these answers are valid. [P LF lines 58–63 and 73–83; [ABK](https://arxiv.org/abs/1511.01937), §3.2 and §6.]

Here the proof’s certificates take the concrete form of gate-by-gate circuit transcripts and pointers. A transcript is an untrusted claim about a computation. Local consistency tests compare it against actual input bits and earlier gate values. If all the tests pass, induction through the circuit establishes the whole computation.

## 3. Forrelation: the source of the hidden address

Let \(m=4^t\). Write \(H\) for the \(m\times m\) normalized Walsh–Hadamard matrix and \(u=(1,\ldots,1)^T/\sqrt m\). Each input bit is represented by a sign, \(a\mapsto(-1)^a\). If \(z\in\{\pm1\}^m\), let \(D_z\) be the diagonal matrix with diagonal \(z\). Define

\[
\Phi(z_1,\ldots,z_k)
=u^T D_{z_1}H D_{z_2}H\cdots H D_{z_k}u,
\qquad \delta=2^{-5k}.
\]

There are \(k\) diagonal sign matrices and \(k-1\) Walsh transforms. These are orthogonal matrices and \(u\) is a unit vector, so \(|\Phi|\le1\). Define the partial function

\[
P_{k,m}(z)=
\begin{cases}
1,&\Phi(z)\ge\delta,\\
0,&|\Phi(z)|\le\delta/2,
\end{cases}
\]

leaving all other inputs outside the domain. The positive 1-condition is intentional. For example, \(\Phi=-1\) is undefined. Replacing it by \(|\Phi|\ge\delta\) changes the promise problem. [P §2.1, LF lines 134–150.]

### Why the quantum answer is cheap

Start in \(u\), apply the matrix product from right to left, and measure whether the result lies along \(u\). The success probability is exactly \(\Phi^2\). A diagonal sign change takes one phase query, implementable with the standard bit oracle; the Walsh transforms and projection require no input queries. Thus this experiment costs \(k\) queries. [P LF lines 174–180.]

On a promised 1-input its success probability is at least \(\delta^2\); on a promised 0-input it is at most \(\delta^2/4\). For fixed \(k\), that is a fixed positive gap. Repeat independently and threshold the observed frequency between those two values. For example, thresholding at \(5\delta^2/8\) and applying the elementary Hoeffding bound gives error at most

\[
\exp(-9n\delta^4/32)
\]

after \(n\) repetitions. Taking \(n\ge32\log(1/\eta)/(9\delta^4)\) therefore suffices. This is a deliberately loose explicit derivation of the stated \(O_k(1+\log(1/\eta))\) query bound. The hidden dependence on \(k\) is large; the theorem holds \(k\) fixed.

The measurements can be deferred: retain each trial’s outcome and workspace and compute the threshold decision reversibly. The output is then a coherent bit register, with the same measurement law. Retaining the workspace is essential because later routines must reverse the preparation.

### Why the classical answer is hard

Bansal and Sinha [6], Theorem 1.3 and Corollary 1.4, prove a randomized lower bound of the form

\[
\Omega\!\left(k^{-29}\left(\frac{m}{\log(km)}\right)^{1-1/k}\right)
\]

at error \(1/3\). Their Eqs. (1.1)–(1.3) use exactly the same normalized Walsh transform, threshold \(2^{-5k}\), and one-sided 1-case. Their matrix dimension is \(N\), corresponding here to \(m\); the whole input length is \(km\). Powers of four are a permitted subsequence of their powers-of-two dimensions. [Supplied `ref-06-bansal-2021.pdf`, pp. 2–4; [primary source](https://arxiv.org/abs/2008.07003).]

The paper weakens this bound to

\[
L=\left\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\right\rfloor,
\qquad R(P_{k,m})>L
\]

for sufficiently large \(m\). For fixed \(k\), the ratio of the published lower bound to the unfloored expression for \(L\) grows like a positive constant times \((\log m)^{1+1/k}\), so this weakening is justified. This audit checked that interface. It did not independently reprove the entire Gaussian/Fourier argument underlying Bansal–Sinha.

## 4. Why an exact circuit accompanies a cheap quantum decoder

The decoder proposes an answer; it does not certify that the input is promised. The construction therefore also needs a total, exact Boolean circuit whose outputs are

\[
d=1\iff P\text{ is defined},\qquad d=1\Longrightarrow b=P.
\]

Set \(W=\sqrt m H\), whose entries are integers \(\pm1\). Then

\[
N=z_1^T W D_{z_2}W\cdots W D_{z_k}\mathbf1\in\mathbb Z,
\qquad \Phi=\frac{N}{M},\quad M=m(\sqrt m)^{k-1}.
\]

The denominator \(M\) is integral because \(m\) is a power of four. Promise membership reduces to the exact integer comparisons

\[
2^{5k}N\ge M,\qquad 2^{5k+1}|N|\le M.
\]

Let \(d\) be their disjunction and \(b\) the first comparison. No rounding or approximate numerical arithmetic is involved. [P LF lines 181–203.]

The integer numerator is computed by \(k-1\) fast Walsh transforms. Each transform takes \(O(m\log m)\) additions or subtractions. A safe bound on intermediate magnitudes, including the final sum, is \(m^k\); signed integers therefore need \(O_k(\log m)\) bits. Standard ripple-carry arithmetic has bounded fan-in and linear size in bit width. Compiling the transforms, sign changes, sum and comparisons gives

\[
S=O_k(m(\log m)^2)
\]

non-input gates. This size bound is essential: an arbitrary truth-table circuit would be exact but could make certificate verification far too expensive. Circuit depth is not the resource being bounded here.

## 5. The total input and the outward-pointer rule

Set \(r=\lceil20\log_2m\rceil\) and \(\ell=\log_2m\). Each column \(i\in[m]\) contains:

1. A visible string \(X_i\in\{0,1\}^m\).
2. \(r\) instances \(A_{i,1},\ldots,A_{i,r}\) of the \(km\)-bit Forrelation gadget, with no promise imposed by the total input format.
3. A cell \(B_{i,s}\) for each address \(s\in\{0,1\}^r\). Each cell contains a pointer to one position in every other column and \(r\) alleged circuit transcripts.

A pointer has \(\ell\) bits, and all \(2^\ell=m\) bit strings encode a valid target. Thus there is no invalid-pointer encoding case. If all the address instances are defined, their answers specify the true address

\[
s_i=(P(A_{i,1}),\ldots,P(A_{i,r})).
\]

Column \(i\) wins if its visible string is all ones, all its address instances are defined, its true-address cell contains correct transcripts, and its pointers land on zeros in **every other column**. The function \(F\) returns one exactly when some winner exists. [P §2.2, LF lines 206–236.]

Every part of this definition is a predicate on bits. Undefined address inputs mean that a column fails a winner requirement. They do not leave the value of \(F\) undefined. Two winners cannot coexist: one would point to a zero in the other’s all-one string.

The direction of the pointers is the key. A genuine winner supplies its own evidence against each rival. Every rival, at every possible cell address, fails to find a zero in the winner’s all-one string. This remains true if the rival’s decoder is completely unreliable.

The total input length is

\[
n=m\bigl[m+rkm+2^r((m-1)\ell+rS)\bigr].
\]

Since \(m=4^t\), \(r=40t\) and \(2^r=m^{20}\). The format is polynomially large in \(m\), with \(n=O_k(m^{22}(\log m)^3)\), but certainly not small. Query access charges for the individual bits read in those arrays; it does not charge for storing the input or computing the global index between queries. [Derived from P’s layout and circuit-size bound.]

## 6. How to check a proposed witness exactly

At any proposed pair \((i,s)\), use these local tests:

| Test type | Number | Exact classical bit queries per test |
|---|---:|---:|
| Each own-string bit is 1 | \(m\) | 1 |
| Pointer to each rival lands on 0 | \(m-1\) | \(\ell+1\) |
| Each claimed gate agrees with its predecessors | \(rS\) | At most 3 |
| Each transcript claims \(d=1\), \(b=s_h\) | \(2r\) | 1 each |

The total is

\[
K=m+(m-1)+r(S+2)=O_k(m(\log m)^3).
\]

If all gate tests pass, topological induction forces the transcript to equal the actual circuit evaluation. The output tests then establish domain membership and the proposed address. Hence all \(K\) tests pass if and only if \(i\) wins at \(s\). A nonwinner has a failing test at **every** address. [P Lemma 2.2, pp. 6, LF lines 264–292.]

**Ledger correction:** a pointer test uses only \(\ell+1\) adaptive queries, but it can depend on all \(m+\ell\) pointer-and-target bits as a Boolean function. For any target bit, choose the pointer to select it; flipping that bit can flip the answer. Thus “function of \(O(\log m)\) input bits” is wrong if it means a fixed small set of relevant coordinates. Formalise a bounded-depth lookup procedure, not a small-support function.

The tests also run coherently: load the needed bits, compute the flag reversibly, then uncompute. Reading a pointer in superposition followed by its selected target is ordinary coherent bit-oracle access. Controlled access can be implemented with two oracle calls through an ancilla. These overheads are constant factors.

## 7. Comparing two columns, including unpromised ones

Using a full verifier as the predicate in an outer search over all \(m\) columns would give a straightforward cost of roughly \(\sqrt m\cdot\sqrt m=m\) queries, ignoring logarithms. Cheap pairwise comparisons let the paper locate a short candidate list before paying the roughly \(\sqrt m\)-query cost of full verification. [P §3, especially LF lines 363–448 and 483–505.]

Decode each of a pair of columns, with per-instance error at most \(\epsilon/r\), retaining both workspaces. At each proposed address, read that column’s pointer toward its opponent. A zero at the destination disqualifies the opponent. If exactly one column disqualifies the other, it wins the comparison; otherwise the smaller index wins. Always run the experiment with the pair sorted into the same order. [P §3.3, LF lines 450–482.]

For a fixed full input, let \(a_{ij}\) be the probability that the experiment declares \(i\) victorious over \(j\). Using the same unordered-pair experiment ensures

\[
a_{ij}+a_{ji}=1\quad(i\ne j),\qquad a_{ii}=0.
\]

Suppose \(i_*\) is a genuine winner. Its own decoded address is correct with probability at least \(1-\epsilon\), by a union bound across its \(r\) instances. Whenever it is correct, its outward pointer finds a zero in the opponent. The opponent’s pointer can never find a zero in \(X_{i_*}\), whatever address it proposes. Therefore

\[
a_{i_*j}\ge1-\epsilon\quad\text{for every }j\ne i_*.
\]

No correctness assumption about the opponent’s decoder was used. Nor is a union bound over all \(m\) opponents needed here: the tournament consumes a uniform per-comparison guarantee. Comparisons among nonwinners can be cyclic or have probabilities arbitrarily close to \(1/2\).

A dominant candidate need not be a genuine winner. The worked examples give an exact four-column case where changing a required zero pointer makes \(F=0\), yet the smaller-index tie-break leaves the candidate’s comparison victories unchanged. The final exact verification is therefore indispensable.

## 8. The tournament: the calculation that makes the search work

For analysis, start with weights \(w_i=1\), total \(W=m\). At each step choose a pivot \(p\) with probability \(w_p/W\), record it, and update

\[
w_i\leftarrow w_i a_{ip}.
\]

These are analytical weights. The quantum algorithm will sample their distribution without computing them numerically. If \(W=0\), the ideal process stops changing. [P Proposition 3.2, LF lines 363–448.]

Pair the ordered terms \((i,p)\) and \((p,i)\). Complementarity gives

\[
\begin{aligned}
\mathbb E[W_{\rm new}\mid w]
&=\frac1W\sum_{p,i}w_pw_i a_{ip}\\
&=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2.
\end{aligned}
\]

Thus the expected total weight after \(T\) steps is at most \(m/2^T\). It is **at most half in expectation**, not exactly half and not a pathwise decrease by a fixed factor. With four initial unit weights, the exact expected next total is \(3/2\).

If the true winner has not yet appeared, each multiplication of its weight uses a factor at least \(1-\epsilon\). Set

\[
T=\lceil\log_2(1000m)\rceil,\qquad\epsilon=\frac1{1000T}.
\]

After at most \(T\) unselected rounds its weight is at least

\[
(1-\epsilon)^T\ge1-T\epsilon=999/1000>1/2.
\]

Missing the winner therefore implies \(W_T>1/2\). Markov’s inequality gives

\[
\Pr(\text{ideal list misses the winner})\le\frac{2m}{2^T}.
\]

There is no ordering or transitivity assumption. Only complementary pair probabilities and the protected winner’s weight matter.

### How the quantum algorithm samples those weights

Given earlier pivots \(p_1,\ldots,p_t\), prepare a uniform superposition of candidates. For each candidate, compare it with each pivot in a fresh workspace. Mark success if it wins every comparison. Conditional on candidate \(i\), the workspaces are a tensor product, so success probability is

\[
\prod_{b=1}^t a_{ip_b}=w_i.
\]

The total success probability is \(W/m\), and conditioned on success the candidate distribution is exactly \(w_i/W\). Fresh workspaces give independence **conditional on the candidate index**; the entire state need not be unentangled. [P LF lines 409–429.]

Before the winner is selected, \(W/m\ge1/(2m)\). Bounded amplitude amplification can therefore produce a sample using \(O(\sqrt m\log(1/\epsilon))\) calls to this preparation or its inverse, failing with probability at most \(\epsilon\). It preserves the exact conditional distribution, as explained next. On failure the algorithm returns its existing list.

At each history before the winner appears, the real transition is the ideal pivot distribution with probability \(1-f_h\), or termination with probability \(f_h\le\epsilon\). The failure probability can depend on the whole history; the coupling does not require independence across stages. Summing across at most \(T\) stages adds at most \(T\epsilon\) to the miss probability. Once the winner is listed, later termination cannot remove it. [P LF lines 430–438.]

## 9. Why amplification preserves the sampled distribution

Write an arbitrary preparation as

\[
A|0\rangle=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle,
\]

where \(|g\rangle\) is its entire normalized successful component, including workspace. A Grover iteration rotates in the two-dimensional span of \(|g\rangle,|b\rangle\). After \(j\) iterations the state is

\[
\sin((2j+1)\theta)|g\rangle+\cos((2j+1)\theta)|b\rangle.
\]

Whenever success is observed, the normalized successful state is still \(|g\rangle\), up to a global phase. Relative probabilities among successful candidates are unchanged. The distinction matters: merely increasing total success probability would not establish the tournament’s exact transition law. [P Lemma 3.1, LF lines 310–351; BBHT [11], §4; BHMT [12], §2.]

The unknown-success-probability routine uses a mixture of zero Grover iterations and a uniformly random iteration count below \(M=\lceil10/\sqrt\gamma\rceil\). For \(\gamma\le p\le1/2\), the finite trigonometric sum gives average success at least \(9/20\); for \(p\ge1/2\), the zero-iteration half alone gives success at least \(1/4\). Thus the mixed trial succeeds with probability at least \(9/40\) whenever \(p\ge\gamma\). A fixed number of trials reduces failure to \(\eta\). All branch lengths are capped, even if \(p<\gamma\) or \(p=0\).

This is established amplitude-amplification machinery. The important use here is preserving the complete successful state and its weighted candidate distribution while retaining a worst-case query bound.

## 10. Completing the quantum algorithm

For each listed candidate, decode its address afresh and search the \(K\) exact local tests for a failure. Preparing a uniform test and its exact failure flag has success probability zero if all tests pass and at least \(1/K\) otherwise. Apply bounded amplification with \(\gamma=1/K\) and failure tolerance \(\epsilon\). [P LF lines 483–501.]

If the candidate is a nonwinner, every address contains a failed test, so it is accepted with probability at most \(\epsilon\). If it is a winner and its fresh address is correct, no test fails, so a false failure cannot be reported. Its rejection probability is at most its decoding error \(\epsilon\).

Output one if any candidate is accepted. On a zero-input, at most \(T\epsilon=1/1000\) total false-accept probability is possible. On a one-input, error is at most

\[
\frac{2m}{2^T}+T\epsilon+\epsilon
\le\frac1{500}+\frac1{1000}+\frac1{11000}<\frac13.
\]

To check costs explicitly, put \(x=\log_2m\). The comparator has cost \(c=O_k(x\log x)\), and \(K=O_k(mx^3)\). The tournament costs \(O_k(\sqrt m x^3(\log x)^2)\). All \(T\) verifications together cost \(O_k(\sqrt m x^{7/2}\log x)\), with their fresh decodings dominated by these terms. This directly implies the paper’s \(\sqrt m\operatorname{polylog}(m)\) bound; even an unoptimized exponent four on \(\log m\) suffices eventually. This logarithmic sharpening is a check derived from the paper, not necessary to its theorem.

## 11. The classical lower bound: two nearly identical inputs

The lower bound starts with a distribution over dummy inputs. Put one independent uniform zero \(J_i\in[m]\) in each \(X_i\), draw all \(A_{i,h}\) independently from a hard distribution \(\mu\) for \(P\), and make every cell a fixed blank pattern. There is no winner, since every column has a zero. [P §4.2, LF lines 600–603.]

Now choose a hidden independent uniform column \(I\), erase its zero, and fill its true-address cell with correct transcripts and pointers to every other zero \(J_j\). This planted input has a winner. The two coupled inputs differ only at \(X_I[J_I]\) and inside \(B_{I,s_I}\). A deterministic algorithm’s two executions are identical until it queries one of these possible differences. Hence the difference between its output-one probabilities is at most the probability that its **dummy run** visits either changed location. [P LF lines 604–616.]

The hard distribution \(\mu\) follows from finite minimax. If \(L<R(P)\), no mixture of depth-\(L\) decision trees can be correct with probability \(2/3\) on every promised input. Finite minimax therefore supplies a distribution under which every depth-\(L\) tree succeeds with probability at most \(2/3\). The answer bits need not be unbiased; the proof does not assume uniform addresses. [P LF lines 575–589.]

### A. Finding the erased zero is unlikely

Let \(Z\) count columns whose zero is actually queried in the dummy run. Until a column’s zero is seen, it remains uniform among that column’s unqueried positions, even given the adaptive transcript. Blank cells reveal no information about it.

A zero found before \(m/2\) distinct positions of its column have been inspected is an early discovery. Each query has conditional probability at most \(2/m\) of such a discovery, so at most \(2G/m\) early discoveries occur in expectation during \(G\) queries. Every later discovery belongs to a column that already consumed at least \(m/2\) queries; there are at most \(2G/m\) such columns on any path. Thus \(\mathbb E Z\le4G/m\). Independence of the hidden \(I\) gives

\[
\Pr(\text{dummy run queries }X_I[J_I])=\frac{\mathbb EZ}{m}\le\frac{4G}{m^2}.
\]

Inferring where an unqueried zero must be does not read the changed bit: the coupling only needs to bound actual queries. [P LF lines 618–637.]

### B. Finding the filled cell requires learning or guessing its address

Call a column heavy if the complete dummy run spends more than \(L\) queries on its address instances, counting repeats. There are at most \(G/L\) heavy columns, so

\[
\Pr(I\text{ heavy})\le\frac{G}{mL}.
\]

For a fixed target column and a fixed query time, consider the joint event that the column is nonheavy and the algorithm reaches its true cell at that time. Reaching the cell requires naming the whole vector of \(r\) hard answers. A capped direct-product argument bounds this joint event by \((2/3)^r\). This is where adaptivity must be handled carefully. [P LF lines 639–664.]

## 12. Why adaptivity does not defeat the address bound

Consider independent inputs \(U_1,\ldots,U_r\sim\mu\), with a separate cap of \(L\) queries to each. Fix any independent auxiliary information and the algorithm’s coins. An observed transcript of the resulting deterministic algorithm specifies separate restrictions on the bits of each input. Every tuple satisfying those restrictions follows the same query schedule. Therefore the event of that transcript is a Cartesian product, and the inputs remain independent under their separate posterior distributions. [P Lemma 4.1, LF lines 528–543; Drucker [13], §1.3 and Lemmas 3.1–3.2.]

Let \(V_h\) be the best achievable success probability for input \(h\), given its current posterior and its remaining budget \(L-q_h\). If the next query addresses \(h\), then

\[
\mathbb E[V_h'\mid\text{transcript}]\le V_h.
\]

Otherwise making that query and following its optimal continuation would beat the definition of \(V_h\). Every other input’s posterior and budget remain unchanged. Consequently the product \(\prod_hV_h\) cannot increase in conditional expectation. This is a special product argument, not a claim that arbitrary products of supermartingales have that property. At termination the probability that the entire answer vector is correct is at most this product. Initially each \(V_h\le2/3\), so success is at most \((2/3)^r\). [P LF lines 544–573.]

The application must **not** condition \(\mu\) on the target column being nonheavy. That event can select unusually easy inputs. Instead fix a target column \(i\) and query time \(t\). Give a simulator all dummy data outside that column’s address instances, which is independent of them. It simulates the algorithm but aborts before its \((L+1)\)-st target query. If the proposed \(t\)-th query addresses a cell \(B_{i,s}\), it outputs \(s\) as its guess. This simulator obeys even the stronger cap of \(L\) total queries to the target instances.

Whenever the original run is nonheavy in column \(i\) **and** queries \(B_{i,s_i}\) at time \(t\), the simulator succeeds. Thus the probability of this joint event is at most \((2/3)^r\). Union-bound over \(G\) times and average over uniform \(I\), then add the heavy case:

\[
\Pr(\text{dummy run visits }B_{I,s_I})
\le\frac{G}{mL}+G(2/3)^r.
\]

There is no additional factor \(m\): it cancels in the averaging over \(I\). The dummy’s blank cells are also essential; giving a simulator filled certificate data could leak the target answers. [P LF lines 645–664.]

## 13. Constants, floors, and the exponent conclusion

Take \(G=\lfloor mL/100\rfloor\). The total difference in output-one probabilities is at most

\[
\frac{4G}{m^2}+\frac{G}{mL}+G(2/3)^r.
\]

For \(1\le L\le m\), the first terms sum to at most \(1/20\). There is an exact integer check for the tail: \(2^{31}<3^{20}\), hence \((2/3)^{20}<2^{-11}\). Since \(r=20\ell\) and \(m=2^\ell\),

\[
G(2/3)^r<\frac1{100m^9}.
\]

The total is therefore less than \(1/3\) for every allowed \(m\ge4\) satisfying these hardness assumptions. Yet an algorithm correct on both distributions with worst-case error \(1/3\) would have output-one probabilities differing by at least \(1/3\). Contradiction. Fixing and averaging a randomized algorithm’s coins preserves this proof because every random tape obeys the same query cap. [P LF lines 665–679; exact integer strengthening derived here.]

The floors only change the constant. If \(A=m^{1-1/k}/(\log_2m)^2\ge2\) and \(m\lfloor A\rfloor/100\ge2\), then

\[
\left\lfloor\frac m{100}\lfloor A\rfloor\right\rfloor\ge\frac{mA}{400}.
\]

The external Forrelation bound still supplies an unspecified sufficiently-large threshold; this calculation does not make that threshold explicit.

Now fix any \(\alpha<4\), \(\alpha\ge0\), and choose a fixed integer \(k>2/(4-\alpha)\), with \(k\ge2\). The exponent \(e=2-1/k-\alpha/2\) is positive, and

\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ge c_{k,\alpha}\frac{m^e}{(\log m)^{2+\alpha b_k}}\longrightarrow\infty.
\]

Thus every smaller universal exponent fails. The known quartic upper bound establishes that four itself works. This is the precise optimal-exponent statement. [P §5.]

## 14. Where the universal quartic upper bound comes from

Appendix A is independent of the new construction. Its ingredients are:

\[
\operatorname{bs}(f)=O(Q(f)^2),\qquad
\deg(f)\le\lambda(f)^2=O(Q(f)^2),\qquad
D(f)\le\operatorname{bs}(f)\deg(f).
\]

Here block sensitivity counts disjoint sets of bits whose flips change an answer at one input; degree is the degree of the multilinear polynomial representing the Boolean function; and \(\lambda\) is the operator norm of its sensitivity graph’s adjacency matrix. [P Appendix A, LF lines 720–864.]

The spectral adversary argument measures how quickly queries can make opposite-output states distinguishable. A star built from disjoint sensitive blocks gives the block-sensitivity bound; coordinate edges in a sensitivity graph are matchings, giving \(\lambda=O(Q)\). Huang’s signed-cube construction turns a surviving degree-\(d\) monomial into a sensitivity subgraph with spectral norm at least \(\sqrt d\). Finally, repeatedly querying a maximum-degree monomial uses at most \(\deg(f)\) queries per round, and each round witnesses a disjoint sensitive block at the actual input, so there are at most \(\operatorname{bs}(f)\) rounds. Multiplying yields \(D=O(Q^4)\). The full calculations and their source attribution are in `proof_audit.md`.

For formalisation, use degree zero for every constant Boolean function, including the zero function. A polynomial library’s convention \(\deg0=-\infty\) is a different convention and would make the ledger’s blanket bit/sign-invariance statement false without this adjustment. Constant functions separately need no queries.

## 15. What is inherited, and what changes in this paper

| Prior source | What it already supplies | What the present manuscript adds or changes |
|---|---|---|
| Aaronson–Ambainis [1] | Forrelation and its quantum/classical query framework | Uses the established gadget as address data. |
| ABK [2], §3.2 and §6 | A certificate table addressed by several partial-function answers; quantum certificate verification | Gives each candidate column its own address table and outward evidence against rivals. |
| Bansal–Sinha [6], Theorem 1.3 and Corollaries 1.4–1.5 | Explicit Walsh–Hadamard Forrelation hardness; a near-cubic total separation through earlier cheat sheets | Uses that same hardness in a different total construction, obtaining the extra factor from many possible winning columns. |
| Sherstov–Storozhenko–Wu [23], Theorem 1.5 | Independent near-cubic total separation, via a random-orthogonal Rorrelation gadget and cheat sheets | Does not supply the new off-promise weighted tournament. Do not identify its gadget with the exact Walsh circuit used here. |
| Ben-David–Kothari [9], §3; Ambainis–Iraids–Kokainis [5] | Candidate-witness comparisons and quantum sink/source search in certificate-complexity separations | Allows arbitrary fractional comparison probabilities among nonwinners, without a uniform gap around \(1/2\). |
| BBHT/BHMT [11–12] | General amplitude amplification and unknown-success search | Uses preservation of the full successful state to implement exact multiplicative-weight sampling. |
| Drucker/Shaltiel [13,22] | Per-instance capped direct-product techniques | Combines them with the planted-cell coupling to charge for many independent possible winner addresses. |
| ABKRT/Huang [3,17] | The universal quartic upper bound | Shows its exponent cannot be improved for randomized complexity. |

The defensible novelty is the **combination** of separately addressed column certificates, their outward pointers, a probabilistic-comparison tournament robust to off-promise behaviour, and the planted lower bound. It would be inaccurate to claim invention of cheat sheets, Forrelation hardness, quantum search, or adaptive direct-product arguments. These comparisons were made against the supplied original papers; exact theorem/section locators and public links are in the bibliography and proof audit.

## 16. A concrete plan for the formal corpus

The fastest useful formal route is modular, with the theorem boundary visible at every stage:

1. **Fix one semantics.** Define total/partial functions, bounded-depth randomized trees, a standard bit oracle, quantum procedures, and their query costs. Prove the bridge between adaptive and purified algorithms. Preserve all-input caps for decoder routines.
2. **Prove the total witness layer.** Define the cell layout and `WinsAt`, prove gate-check equivalence, winner uniqueness, and failure at every address of a nonwinner. Treat pointer tests as adaptive lookups.
3. **Complete the classical theorem for a generic partial function.** Prove finite minimax, the capped direct product, the simulator/coupling estimates, and the exact numerical tail. State the assumption \(L<R(P)\) explicitly.
4. **Complete the classical probability part of the tournament.** The supplied drift identity is only one algebraic ingredient. Add probability ranges, nonnegative weights, the absorbing zero case, winner survival, Markov, and adaptive coupling.
5. **Prove the quantum realization.** Formalise the reversible comparator, tensor-product success preparation, distribution-preserving bounded amplification, exact local-test search, and branchwise costs.
6. **Instantiate Forrelation and assemble.** Prove the efficient exact circuit and coherent decoder. A theorem that still assumes Bansal–Sinha remains conditional; removing that hypothesis requires a checked proof or a verified imported theorem with the same definitions.

Do not turn numbered displays into accidental assumptions: `eq-5` currently combines the definition of \(L\) with its lower-bound assertion, and `eq-17` combines the definition of \(G\) with the conclusion of Proposition 4.2. Definitions and theorem aliases should be separated in the proof dependency graph.

The supplied `Drift.lean` contains proposed proofs of finite sum identities and an inequality from complementarity. Its structure does not itself require \(0\le a_{ij}\le1\) or nonnegative weights, because the algebra does not need those assumptions. A probability interpretation does. Its contents establish neither a quantum sampler nor the separation theorem. Moreover, the attached trace’s final build attempt failed during setup/cache work with exit code 144; no successful build or Comparator receipt is supplied, and no theorem-level compiler error was established. These are evidence boundaries, not reasons to discard the mathematical plan. [Supplied Lean file; trace turn 22; `trace_context_review.md`.]

For an explanation aimed at a first reader, begin with the four-column board and the pointer direction, show how false contenders can survive comparison, then explain exact verification. Introduce the hidden address only after those mechanisms are visible. The weight-halving calculation and the joint-event simulator then answer two specific questions: why quantum search can find a candidate cheaply, and why classical adaptivity cannot cheaply locate the planted certificate. The worked examples follow this order.
