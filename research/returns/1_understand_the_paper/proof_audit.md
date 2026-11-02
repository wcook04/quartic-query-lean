# Detailed proof audit

This file joins the three independently reconstructed mathematical audits. All main-paper line references use physical LF-separated lines of the input packet’s `paper/extracted.md`. These analyses are manual checks; none is a Lean or Comparator receipt. The external Bansal-Sinha theorem is checked at its interface and remains a published dependency.

The individual JSON review files named inside sections have been merged into the single `statement_review.json` in this return.

# Independent audit of the quantum upper bound

## Conclusion and scope

I found no substantive mathematical gap in Section 3 of the supplied manuscript. In particular, the off-promise comparison, exact weighted sampling, history-dependent coupling, and worst-case query cap withstand direct calculation. This is a mathematical reading and reconstruction, not a Lean or circuit-level verification. It relies on the standard exact-unitary query model expressly allowed by the paper, and on the Section 2 construction and decoder specifications. All 31 Section 3 ledger entries have been reviewed in `quantum_statement_review.json`; their mathematical statements are correct. Line numbers in this audit and its review JSON count LF-separated lines in `paper/extracted.md`, matching the supplied ledger's `source_line` convention. Page form-feed characters do not create extra line numbers; PDF pages are also cited.

The materially delicate interfaces are:

1. The comparator must run the *same unordered-pair experiment* in both directions, so the two directed probabilities sum to one.
2. The decoder within a comparator is a bounded coherent repetition circuit. It is not the measured, variable-stopping amplifier of Lemma 3.1.
3. Sampling must retain the entire comparison workspace. Its success event is a conjunction on *fresh* workspaces; the resulting good-state distribution must be preserved exactly.
4. A pointer test uses logarithmically many *adaptive queries*. It generally depends on many more than logarithmically many input coordinates as a Boolean function.
5. A candidate is verified against exact circuit transcripts and pointer tests, not trusted because it won comparisons.

These are all respected by the supplied proof. Changing one of them in a formal implementation could invalidate the theorem without contradicting the elementary drift identity.

## 1. Bounded amplification: exact distribution and a worst-case cap

**Sources:** manuscript Lemma 3.1, pp. 7–8, lines 310–351; Boyer–Brassard–Høyer–Tapp, §4 Lemma 2; Brassard–Høyer–Mosca–Tapp, §2 Eq. (8).

Write the prepared state as

\[
|\psi\rangle=\sqrt p\,|g\rangle+\sqrt{1-p}\,|b\rangle
=\sin\theta\,|g\rangle+\cos\theta\,|b\rangle.
\]

For the Grover iterate

\[
G=(2|\psi\rangle\langle\psi|-I)(I-2\Pi_g),
\]

its matrix in the ordered basis \((|g\rangle,|b\rangle)\) is

\[
\begin{pmatrix}\cos 2\theta&\sin2\theta\\-\sin2\theta&\cos2\theta\end{pmatrix}.
\]

It sends \((\sin\theta,\cos\theta)\) to \((\sin3\theta,\cos3\theta)\); induction gives the displayed state after any iteration count. Thus projection onto success yields the same normalized vector \(|g\rangle\), up to a scalar sign. Arbitrary internal comparison garbage can be part of \(|g\rangle\). The argument does not require a uniform good-state distribution.

The exact random-length identity is

\[
\frac1M\sum_{j=0}^{M-1}\sin^2((2j+1)\theta)
=\frac12-\frac{\sin(4M\theta)}{4M\sin 2\theta}.
\]

It follows either by \(\sin^2x=(1-\cos2x)/2\) and a finite geometric sum, or directly from BBHT Lemma 2. For \(\gamma\le p\le1/2\),

\[
\sin2\theta=2\sqrt{p(1-p)}\ge\sqrt\gamma.
\]

With \(M=\lceil10/\sqrt\gamma\rceil\), the paper's weaker lower bound \(1/2-1/(2M|\sin2\theta|)\ge9/20\) is valid. A mixed trial uses this random length with probability one half. Its success probability is therefore at least \(9/40\) in this range. For \(p\ge1/2\), the other half of the trial, using zero Grover iterations, already succeeds with probability at least \(1/4\ge9/40\).

After

\[
J=\left\lceil\frac{\log(1/\eta)}{\log(40/31)}\right\rceil
\]

fresh trials, failure probability is at most \((31/40)^J\le\eta\). A trial uses at most \(2M-1\) calls to \(A\) or \(A^{-1}\): one initial preparation and two calls per Grover iteration. This proves a cap for every branch, including \(p<\gamma\) and \(p=0\). When \(p=0\), success is impossible. When \(p=1\), every trial succeeds.

Conditional on a particular successful trial and iteration count, the output vector is always \(|g\rangle\) up to global phase. Mixing over trial lengths and the first successful stopping time therefore leaves the output-register density matrix \(|g\rangle\langle g|\) unchanged. Classical records of trial choices may be retained; the claimed successful output state is the designated prepared-state register. The manuscript does not require the whole collection of trial-history registers to equal \(|g\rangle\).

**What would overturn this check:** an implementation that measures or discards a needed register inside \(A\), so that \(A^{-1}\) is not the inverse of the actual preparation; an amplifier that preserves only total success probability and changes relative good amplitudes; or a repeat-until-success implementation lacking the fixed cap above.

## 2. The ideal tournament: where the half-factor comes from

**Sources:** manuscript Proposition 3.2, pp. 8–9, lines 354–408.

Fix the full oracle input throughout. Let \(a_{ij}\) be comparator outcome probabilities, so \(0\le a_{ij}\le1\), \(a_{ij}+a_{ji}=1\) for distinct indices and \(a_{ii}=0\). The input is not redrawn between comparisons.

For nonnegative weights \(w_i\), with \(W=\sum_iw_i>0\), select pivot \(p\) with probability \(w_p/W\), then set \(w'_i=w_i a_{ip}\). Pairing ordered terms gives

\[
\begin{aligned}
2\sum_{p,i}w_pw_i a_{ip}
&=\sum_{p\ne i}w_pw_i(a_{ip}+a_{pi})\\
&=\sum_{p\ne i}w_pw_i=W^2-\sum_iw_i^2.
\end{aligned}
\]

Consequently

\[
\mathbb E[W'\mid w]=\frac{W^2-\sum_iw_i^2}{2W}\le W/2.
\]

The diagonal correction is necessary. For example, equal initial weights on four candidates give expected next total \((16-4)/8=3/2\), not exactly two. The verbal claim should be “at most half in expectation,” not “half on every round.”

The zero-total state is absorbing; no division by zero occurs. Since \(W_0=m\), induction via conditional expectations gives \(\mathbb E W_T\le m/2^T\). No independence between stages or transitivity of comparisons is used.

If a dominant candidate \(i_*\) has not appeared in the first \(t\le T\) pivots, every factor in its weight is at least \(1-\epsilon\), so

\[
w_{i_*}\ge(1-\epsilon)^t\ge1-t\epsilon\ge1-T\epsilon=999/1000>1/2.
\]

The ideal process therefore cannot reach zero before selecting the winner. Missing it implies \(W_T>1/2\); Markov's inequality gives

\[
\Pr(i_*\text{ missing})\le2\mathbb E W_T\le2m/2^T.
\]

Selecting a pivot sets its own weight to zero. Thus the ideal list contains no repeated pivots and in fact has at most \(m\) entries even though the paper only needs the cap \(T\).

**What would overturn this check:** a purported comparison family with independently defined directional circuits that fails complementarity, negative weights or probabilities, or an update depending on sampled outcomes rather than the exact underlying comparison probabilities. The actual quantum sampler realizes the latter probabilities without estimating them.

## 3. Exact sampling from product weights

**Sources:** manuscript pp. 9–10, lines 409–448.

For a fixed classical pivot history \(h=(p_1,\dots,p_t)\), the preparation is

\[
|\Psi_h\rangle=\frac1{\sqrt m}\sum_i |i\rangle\bigotimes_{b=1}^t|\phi(i,p_b)\rangle.
\]

The overall state can be entangled. What matters is that, conditional on the basis index \(i\), different comparator workspaces are a tensor product. Each comparison starts on a fresh zero workspace, uses \(i,p_b\) as controls, and retains its output and garbage. Let “good” mean all \(t\) comparison outcomes say \(i\) defeats \(p_b\). The good squared norm at index \(i\) is

\[
\frac1m\prod_{b=1}^t a_{ip_b}=w_i/m.
\]

Distinct index basis vectors are orthogonal, so the total good probability is \(W/m\). Conditional on success, measurement of the index has exactly the law \(w_i/W\). This calculation uses no numerical representation of the probabilities and no approximate probability estimation.

Apply Lemma 3.1 with \(\gamma=1/(2m)\) and \(\eta=\epsilon\). Before the winner is chosen, \(W/m\ge1/(2m)\), so the sample fails with probability at most \(\epsilon\). On success its index distribution is the ideal kernel exactly.

At each history avoiding the winner, the real transition has the form

\[
K_{\mathrm{real},h}=(1-f_h)K_{\mathrm{ideal},h}+f_h\,\delta_{\mathrm{stop}},\qquad 0\le f_h\le\epsilon.
\]

This is a *history-dependent* mixture. A coupling can first choose whether the failure branch occurs, then couple the successful pivot to the ideal pivot. The sum of at most \(T\) conditional failure probabilities is at most \(T\epsilon\). After the winner has entered the list, any later early termination is harmless. Therefore

\[
\Pr(\text{real list misses }i_*)\le2m/2^T+T\epsilon.
\]

For arbitrary finite \(m\), preparing exactly \(m^{-1/2}\sum_{i=1}^m|i\rangle\) requires no query and is legal under the paper's unrestricted query-free-unitary convention (lines 24–25). Likewise, the later test count \(K\) need not be a power of two. A formal development restricted to an exact finite gate basis would need an approximation theorem and an added error budget; that restriction is not part of the paper.

The preparation and inverse at stage \(t\) use \(O(c(t+1))\) queries, while the amplifier makes \(O(\sqrt m\log(1/\epsilon))\) calls. Summing the arithmetic sequence of stage costs yields

\[
O\!\left(c\sqrt m T^2\log T\right).
\]

The stage cap, maximum Grover length and repetition count are fixed. This cap still holds if no dominant candidate exists or all remaining weights vanish.

## 4. Off-promise comparisons: why only one side needs to be right

**Sources:** manuscript pp. 9–10, lines 450–482; Lemma 2.1(ii), p. 4, lines 158–180; winner definition, p. 5, lines 221–236.

The decoder runs \(r\) Forrelation circuits with error \(\epsilon/r\) per promised input. A union bound bounds the chance of at least one wrong address bit by \(\epsilon\). Off the promise, each circuit still returns a bit with the same bounded query cost. Its output can be arbitrary, including highly biased; no “approximately correct” interpretation exists there.

For distinct columns, sort the pair and retain both decoded address registers. At the proposed cell in each column, read its pointer toward the other column, then query the target bit. If exactly one target is zero, that pointer's column wins; otherwise the smaller index wins. Running the same sorted-pair experiment guarantees complementarity. Retaining the decoded registers prevents interference between distinct address outcomes when later operations are classically controlled on those outcomes.

Suppose \(i_*\) is a true winner. Its own string is all ones. No pointer stored anywhere in any opposing column can find a zero there. This is true even if its opponent's decoded address is completely unconstrained or its transcript is fabricated. Whenever the winner's own address is decoded correctly, its outward pointer witnesses an actual zero in its opponent's string. Thus the winner disqualifies the opponent and cannot be disqualified in return. Only failure to decode the winner's own address can prevent this argument, giving \(a_{i_*j}\ge1-\epsilon\).

There is no union bound over all opponents in this step: the per-comparison guarantee is uniform over opponents, and the tournament lemma consumes that guarantee. Nor is there an assumption that one comparator outcome between nonwinners reflects a hidden consistent order.

A reversed-pointer construction would lose this simple one-sided protection. The manuscript's outward orientation is doing real mathematical work.

## 5. Verification and totality

**Sources:** Lemma 2.2, p. 6, lines 264–292; Section 3.3, p. 10, lines 483–512.

At a fixed candidate-address pair, all \(K\) local tests pass exactly when the candidate wins at that address. A transcript gate test queries at most three bits; a pointer test queries \(\ell\) pointer bits followed by one target bit, and hence has adaptive query depth \(\ell+1\). A pointer test is generally not a Boolean function of only \(O(\log m)\) fixed input coordinates: any of the \(m\) target bits can matter as the pointer varies.

Freshly decode and measure a proposed address. Prepare a uniform test index with an exact “failed test” flag. If every test passes, the good probability for this *failure search* is zero, and Lemma 3.1 cannot return a failed test. If any test fails, the good probability is at least \(1/K\), and the amplifier finds a failure with probability at least \(1-\epsilon\). In particular:

- A nonwinner has a failed test at every possible proposed address, so its acceptance probability is at most \(\epsilon\).
- A winner at its correct address has no failed test, so rejection is possible only through address-decoding error and has probability at most \(\epsilon\).

At most \(T\) verifications are performed. On a zero-input, the union bound gives \(T\epsilon=1/1000\). On a one-input, incorrect acceptance of some other candidate still gives the correct output one; the only relevant failures are missing the true winner or rejecting it. Thus the total one-input error is bounded by

\[
\frac{2m}{2^T}+T\epsilon+\epsilon
\le\frac1{500}+\frac1{1000}+\frac1{11000}<\frac13
\]

for \(m\ge2\), and the construction itself has \(m\ge4\).

A controlled oracle query does not require an extra oracle power. Query the addressed bit into a zero ancilla, apply the required controlled action using that ancilla, and query again to reset it. Pointer addresses are computed reversibly after loading their bits. The global cell index can be enormous as an integer but computing it is query-free in this model. No table is read for free.

## 6. Polylogarithmic accounting

Let \(x=\log_2m\). For fixed \(k\), \(r=O(x)\), \(T=O(x)\), \(\log(1/\epsilon)=O(\log x)\), and \(S=O_k(mx^2)\). Hence

\[
K=O_k(mx^3),\qquad c=O_k(x\log x).
\]

The tournament cost is

\[
O_k(\sqrt m\,x^3(\log x)^2),
\]

and all \(T\) verification searches cost

\[
O_k(\sqrt m\,x^{7/2}\log x).
\]

The \(T\) fresh decodings add only \(O_k(x^2\log x)\). These are dominated by \(O_k(\sqrt m(\log m)^4)\) for sufficiently large \(m\). This explicit nonoptimized logarithmic exponent is an audit derivation from the paper's bounds, not an extra claim required for its theorem. The manuscript correctly leaves the harmless logarithmic exponent unspecified. The missing additive decoder cost in the displayed verification-search expression does not invalidate the asymptotic upper bound.

## 7. Exact hand example for a nontransitive tournament

This is an abstract comparison example, not an enumeration of the full input's huge cell arrays. Set

\[
a=\begin{pmatrix}
0&1&1&1\\
0&0&1&0\\
0&0&0&1\\
0&1&0&0
\end{pmatrix}.
\]

Candidate 1 always wins. Among the other three candidates, 2 beats 3, 3 beats 4, and 4 beats 2. With initial weights \((1,1,1,1)\), pivot 1 leaves total weight zero. Pivot 2 leaves weights \((1,0,0,1)\); pivot 3 leaves \((1,1,0,0)\); pivot 4 leaves \((1,0,1,0)\). Each pivot is initially chosen with probability \(1/4\), so the expected new total is \(3/2\), matching the exact drift identity.

The probability of missing candidate 1 after one pivot is \(3/4\). Given that miss, the next pivot is candidate 1 or the sole remaining loser, each with probability \(1/2\), so the two-pivot miss probability is \(3/8\). If both first pivots are losers, the only remaining positive weight belongs to candidate 1, so the three-pivot miss probability is zero. The proof never needed to replace the cyclic losers with an ordered ranking.

## Read coverage and reproducibility boundary

Read the complete supplied main-paper text, including Sections 1–5, Appendix A and references. Visually inspected the rendered PDF's page 9, confirming tensor-product notation, the exact conditional law, the coupling paragraph, and \(O(c\sqrt mT^2\log T)\) cost. Read all Section 3 ledger rows and the entire attached ledger notes and commentary files as unreviewed context.

Reference reading performed for this subaudit:

- **BBHT, Tight bounds on quantum searching:** §4, Lemmas 1–2, in the attached `ref-11-boyer-1998.pdf`; independently checked the finite trigonometric sum. Other parts were searched for context, not fully audited.
- **BHMT, Quantum amplitude amplification and estimation:** §2 through Theorem 3 and its proof, especially Lemma 1 and Eq. (8), in the attached `ref-12-brassard-2002.pdf`. The later amplitude-estimation and exact-derandomization developments are unnecessary here and were not fully read.
- **Dürr–Høyer, A quantum algorithm for finding the minimum:** the complete two-page article, to establish the exact ordered-set setting and why its ordinary minimum-finding analysis is not an off-the-shelf proof of Proposition 3.2.
- **Grover, A fast quantum mechanical algorithm for database search:** introduction, model and algorithm in §§1–3, and the start of the diffusion calculation. This provides context; Lemma 3.1's stronger general-state property was checked in BHMT instead.

Primary web pages opened and bibliographic identities checked:

- https://arxiv.org/abs/quant-ph/9605034
- https://arxiv.org/abs/quant-ph/0005055
- https://arxiv.org/abs/quant-ph/9607014

No unprovided quantum-query library was assumed correct, no Lean build was run in this subaudit, and no full circuit simulation was used as a substitute for the algebra. The main remaining formal work is representing the exact coherent preparation, its reversible query cost, fresh workspaces, and the adaptive classical kernels in a single query-complexity model.


---

# Independent audit of the classical lower bound and final exponent

## Result and scope

I rederived every step of the supplied paper’s §§4–5. I found no mathematical gap in this portion of the argument under the stated worst-case bit-query model. In particular, the adaptive address-guessing step does not condition a hard distribution on the algorithm’s decision to leave a column lightly queried. It uses a capped simulator and an unconditional joint-event bound, which is the right construction.

This is a manual proof audit. I have not executed a Lean proof of these claims, run Comparator, or independently reproved the external Forrelation lower bound. The Bansal–Sinha theorem’s statement, normalization, thresholds, and error convention were checked against the supplied original paper. All 29 assigned ledger statements are mathematically correct in the paper’s global context. Several require those global assumptions to remain attached when formalized. Their original line numbers use physical LF-delimited lines and are not stale. The extracted paper contains form-feed page breaks; Python splitlines() would count those as additional lines. The accompanying JSON and all paper text locations below preserve the original physical LF convention.

The quantitative lower-bound argument is substantially more robust than its “sufficiently large” wording alone suggests: once `1 <= L < R(P)` and `L <= m` hold, its numerical contradiction works already for every allowed `m >= 4`. The unknown large threshold is needed to import Forrelation hardness and make `L` positive, not to make the final error sum small.

Primary source: `paper/quartic-query-separation.pdf`, §§4–5, printed pp. 11–14; `paper/extracted.md` lines 515–717.

## 1. Exact capped direct product

Fix independent auxiliary information and the random tape. This leaves a deterministic algorithm applied to independently sampled inputs `U_1,...,U_r`. A positive-probability transcript `tau` specifies a set `E_h` of allowed bit strings in each input. Its event is exactly

`{tau is observed} = E_1 x ... x E_r`.

The reason is not that adaptivity is irrelevant in general. It is that, once a tuple gives the same queried bit values, the algorithm’s next query is determined by those values, so that tuple follows the identical adaptive schedule. Consequently the posterior law factors:

`Pr[(U_1,...,U_r)=u | tau] = product_h Pr[U_h=u_h | E_h]`.

This statement is asserted only at positive-probability transcript nodes. It needs no artificial full-support assumption. Repeated queries impose redundant constraints but consume budget in the paper’s convention. [Main paper lines 538–546; Drucker, §1.3 and Lemma 3.2.]

Define `V_h(tau)` as the maximum success of a deterministic continuation on `U_h`, under this posterior, with at most `L-q_h` further queries. Finiteness makes the maximum attained. If the next query goes to `U_h`, the strategy “make that query, then use an optimal continuation for its answer” is an admissible pre-query strategy. Therefore

`E[V_h(tau') | tau] <= V_h(tau)`.

No other input’s posterior or remaining budget changes. Since the other values are nonnegative constants at this conditional step,

`E[product_j V_j(tau') | tau] <= product_j V_j(tau)`.

The special reason for the product inequality is essential: arbitrary products of supermartingales need not be supermartingales. Here exactly one factor changes and the others are conditionally unchanged. [Main paper lines 544–561; Drucker Lemma 3.1 and the proof following Lemma 3.2.]

There are at most `rL` target-input queries. Pad a shorter run by unchanged states. At its leaf, the conditional probability of a specified entire answer vector is the product of the corresponding single-answer posterior probabilities. This is at most the product of the posterior maxima, which is at most `product_h V_h` because each continuation may simply stop and guess. Initially every `V_h <= beta`. Taking expectations proves success at most `beta^r`. Averaging back over the independent side information and random tape preserves the inequality. [Main paper lines 560–573.]

### Assumptions that must survive transcription

- Each input has a separate cap of `L` queries; a mere aggregate cap `rL` is not the same theorem.
- Side information must be independent of the whole input tuple, not only individually independent of each coordinate.
- The algorithm has no other input-dependent oracle.
- The proof’s conditional product law is for a full observed deterministic transcript, not for arbitrary events determined by an adaptive run.

The paper meets these conditions. Its later simulator even uses at most `L` queries in total to all target instances, which implies the required separate caps.

### Attribution

This is an application and explicit restatement of established direct-product machinery, not a new direct-product theorem. The supplied Drucker PDF’s §1.3 says its fair-tree argument recasts Shaltiel’s method; Lemmas 3.1–3.2 present exactly the value function and posterior independence used here. The supplied Shaltiel PDF is an ECCC 2001 preprint, with fairness in §5 Definition 4 and an optimal XOR version in Theorem 5. The 2003 journal date in the bibliography is compatible with that earlier source, but its pagination should not be conflated with the journal’s. Links:

- [Drucker, arXiv:1005.0644v2](https://arxiv.org/abs/1005.0644), §1.3 and Lemmas 3.1–3.2.
- [Shaltiel, ECCC TR01-009](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html), supplied PDF §5.

## 2. Why a hard distribution exists

There are finitely many depth-at-most-`L` deterministic decision trees on the finite promise domain. The paper’s randomized model is exactly a probability distribution over such trees. The associated finite zero-sum game has entries `1{T(x)=P(x)}`. Finite minimax gives

`max_randomized_tree min_input success = min_input_distribution max_tree average_success`.

The left maximum is attained. If it were at least `2/3`, an `L`-query randomized algorithm would satisfy the definition of `R(P)`, contradicting `L<R(P)`. Hence it is strictly smaller than `2/3`. A minimizing distribution `mu` therefore makes every depth-`L` deterministic tree have success at most `2/3` (indeed, below it). This is enough for Lemma 4.1 with `beta=2/3`. [Main paper lines 575–589.]

The paper does not require `mu` to make the answer bit uniform, or to make each individual promise input equally likely. Such extra properties are not implied by minimax and are not used. The independently sampled instances all use this same hard distribution. The required external input is the statement `L<R(P)`, supplied by Bansal–Sinha. Their Eqs. (1.1)–(1.3), Theorem 1.3, and Corollary 1.4 match the main paper’s normalized Walsh–Hadamard form, promise threshold `delta=2^(-5k)`, and bounded error `1/3`. [Supplied `ref-06-bansal-2021.pdf`, printed pp. 2–4; [arXiv:2008.07003](https://arxiv.org/abs/2008.07003).]

## 3. The dummy/planted coupling

The dummy input has one independent uniform zero `J_i` in every `X_i`, all address instances drawn independently from `mu`, and a fixed blank pattern in every cell. It is a zero-input because no column’s own string is all ones. The blank pattern may accidentally contain correct pieces of some transcript; that does not matter.

Choose `I` uniformly and independently. Erase the single zero of `X_I` and fill only its true-address cell with correct evaluation transcripts and pointers `p_{I,s_I,j}=J_j`. All addresses are defined because the sample distribution is supported on promised inputs. Every winner condition is then satisfied by `I`, so the planted input is a one-input. [Main paper lines 600–607.]

Only `X_I[J_I]` and bits in `B_{I,s_I}` may differ between the coupled inputs. For a fixed deterministic tree, the two runs agree until their first queried difference. If the entire dummy run avoids that set, both runs and outputs are identical. Thus their difference in output-one probabilities is at most

`Pr(dummy run queries X_I[J_I]) + Pr(dummy run touches B_{I,s_I})`.

Counting any visit to the planted cell is conservative, since the queried bit may equal its old blank value. Importantly, both hitting events are measured in the dummy run. One must not mix together query counts taken from different modified runs. [Main paper lines 608–616.]

## 4. Finding the erased zero

Before a zero is queried, its posterior location is uniform among its column’s unqueried positions. The outside strings are independent and blank cells reveal nothing about `J_i`; a fixed transcript only excludes observed-one positions in `X_i`. This is again an adaptive transcript argument.

Call the first queried zero in a column early if fewer than `m/2` distinct positions of that column have previously been queried. Conditional on any preceding transcript, its probability at the next query is at most `2/m`. Summing over at most `G` queries gives expected early discoveries at most `2G/m`. Each remaining discovered column has already consumed at least `m/2` queries, so at most `2G/m` such columns exist on any execution. Thus

`E[Z] <= 4G/m`.

Because the whole dummy run is independent of `I`,

`Pr(dummy run queries X_I[J_I]) = E[Z]/m <= 4G/m^2`.

There is no problem if the algorithm infers an unqueried zero from the other `m-1` positions. Unless it queries that last position, it still has not read the bit that distinguishes the coupled inputs. The definition of `Z` counts actual zero queries. [Main paper lines 618–637.]

## 5. Reaching the planted certificate

A column is heavy if the complete dummy run spends more than `L` queries on that column’s address instances, summed across its `r` instances. If `L>=1`, a pathwise budget count gives at most `G/L` heavy columns. (The sharper denominator `L+1` is unnecessary.) Independence of `I` implies

`Pr(I is heavy) <= G/(mL)`.

For a nonheavy target the proof must retain adaptivity without changing `mu`. Fix a column `i` and original query number `t`. Give a simulator every dummy input bit outside the `r` target strings free. These outside values are independent of the target tuple because cells are blank in the dummy distribution. Simulate the tree and abort before its `(L+1)`-st target-string query. If its proposed `t`-th query goes to `B_{i,s}`, output `s`; otherwise output any fixed address. This is a legitimate address-guessing algorithm with at most `L` total target queries, and hence at most `L` per target instance. Its success is at most `(2/3)^r`.

Whenever the original dummy run is nonheavy in column `i` and queries the correct cell there at time `t`, the simulator has not aborted and outputs the correct full address. Therefore

`Pr(nonheavy(i) AND t-th query touches B_{i,s_i}) <= (2/3)^r`.

This is a joint-event bound, not a success bound conditioned on nonheaviness. It is valid even when the algorithm chooses which columns to pursue on the basis of what it has seen. Union over the `G` possible times, then average over `I`: the factor `m` from summing over columns is cancelled by the `1/m` averaging weight. Hence

`Pr(dummy run touches B_{I,s_I}) <= G/(mL) + G(2/3)^r`.

[Main paper lines 639–664.]

### A four-input warning against the tempting conditional argument

Let `P(a,b)=a AND b`, with both input bits uniform, and let `L=1`. The optimal one-query success is `3/4`: query either bit, answer zero if that bit is zero, and otherwise guess the unknown other bit. A zero-query answer zero also succeeds on `3/4` of inputs.

Now use an unrestricted adaptive policy: query `a`; if it is zero, stop and output zero; otherwise query `b`. Declare a run nonheavy when it uses at most `L=1` queries. Then

`Pr(correct | nonheavy)=1 > 3/4`,

but

`Pr(correct AND nonheavy)=1/2 <= 3/4`.

Conditioning has selected easy runs. This is why the paper’s capped-simulator proof must retain the unconditional joint event. This small example is an independently computed illustration, not a claim from the paper.

## 6. Constants and floors

The complete output-probability gap is bounded by

`D = 4G/m^2 + G/(mL) + G(2/3)^r`.

With `G=floor(mL/100)` and `1<=L<=m`, the first two terms are at most `4/100` and `1/100`. The paper takes `r=ceil(20 log_2 m)` and obtains

`G(2/3)^r <= (1/100) m^(2-20 log_2(3/2))`.

The exponent is approximately `-9.6992500144`, so the tail tends to zero. There is also a simple exact certificate suitable for formalization. Since `m` is a power of four, write `m=2^ell` with integer `ell>=2`; then `r=20ell`. The integer inequality

`2^31 = 2147483648 < 3486784401 = 3^20`

implies `(2/3)^20<2^(-11)`. Therefore

`G(2/3)^r < (m^2/100) m^(-11) = 1/(100m^9)`.

It follows that

`D < 1/20 + 1/(100m^9) <= 1/20 + 1/26214400 < 1/3`

for every allowed `m>=4`. Any randomized algorithm with a worst-case `G`-query cap obeys this estimate after fixing its coins and averaging. An algorithm correct with error at most `1/3` on every input would instead have output-one probability at most `1/3` on the dummy distribution and at least `2/3` on the planted distribution. Its gap would be at least `1/3`, a contradiction. [Main paper lines 665–679.]

To remove floors, put `A=m^(1-1/k)/(log_2 m)^2`. If `A>=2` and `m floor(A)/100>=2`, then

`floor((m/100) floor(A)) >= (m/200)floor(A) >= mA/400`.

Thus `1/400` is one possible lower-bound coefficient after imposing the relevant sufficiently-large threshold. The paper permits a constant depending on `k`; the necessary threshold still depends on `k`, including through the implicit constant in Bansal–Sinha’s theorem. No explicit numerical threshold for the full theorem is provided by this computation. [Main paper lines 695–702.]

## 7. Exponent and quantifiers

Given a proposed exponent `0<=alpha<4`, choose one integer

`k >= 2` with `k > 2/(4-alpha)`.

Then `e=2-1/k-alpha/2>0`. Hold this `k` fixed while `m` tends to infinity through powers of four. The quantum upper bound and the classical lower bound imply, after absorbing `1+Q` into a constant for large `m`,

`R(F_{k,m})/(1+Q(F_{k,m}))^alpha >= c_{k,alpha} m^e/(log m)^(2+alpha b_k)`.

The right-hand side tends to infinity. No universal constant can support that exponent. The known universal quartic upper bound supplies the other direction. This proves `alpha_tot=4`; it does not prove a family satisfying an exact fourth-power lower bound. For each fixed `k`, the exponent supplied by comparison is `4-2/k`, with logarithmic losses. [Main paper lines 703–712.]

In particular, `k=2` reaches the cubic exponent but does not refute a universal cubic upper bound. Any fixed `k>2` suffices to refute it asymptotically. The order of quantifiers is the essential point, and the paper handles it correctly.

## 8. Ledger and implementation issues

1. **Equation 17 must not become a circular proof prerequisite.** Its ledger row combines the definition of `G` with the asserted inequality `R(F)>G`, yet lists only `eq-5` as a dependency. `prop-4.2` then lists `eq-17` as a prerequisite. The statement itself is true, but a formal proof graph should let `eq-17` define the budget only and assign the inequality to `prop-4.2`, or make the former an explicit alias of the latter after proof. Otherwise an unproved copy of the target theorem could masquerade as an input.

2. **Keep the cap in the minimax row’s consequence.** `claim-minimax-mu` abbreviates its final sentence as a statement about guessing `r` independent answers. That consequence is correct with the separate `L`-query caps and independent side information of Lemma 4.1. It is not a bound on an unrestricted algorithm.

3. **Keep `r` in the numerical row’s hypotheses.** The strict bound in `claim-numeric` relies on the configured `r=ceil(20 log_2 m)` through `claim-tail`; the two displayed bounds `4G/m^2<=0.04` and `G/(mL)<=0.01` alone do not bound the third term.

4. **Do not replace worst-case cost by expected cost silently.** Fixing an arbitrary random tape yields a depth-`G` tree because the paper’s cap is uniform over all coin outcomes. That step fails without an additional argument for an expected-query model.

5. **Small illustrations do not instantiate the asymptotic lower bound.** At `m=4`, `r=40` and every column has `2^40` cell addresses. For every finite `k>=2`, `L=floor(4^(1-1/k)/4)=0`. A displayed four-column board can faithfully show a designated certificate and its pointers while leaving most cells implicit; a reduced-address board is a useful labelled toy, not a complete lower-bound instance.

None of these points overturns the paper’s classical proof. Items 1–3 matter when turning prose and ledger aliases into a formal corpus.

## 9. What would overturn this assessment

- A counterexample to the transcript-rectangle statement for the actual deterministic query model would break Lemma 4.1; none arises from adaptive query ordering alone.
- If supposedly free simulator side information were correlated with the target `A` tuple, the application would fail. The fixed blank-cell dummy input expressly prevents this.
- If the algorithm were given the planted index `I`, or if `I` were chosen based on its dummy transcript, the uniform averaging arguments would fail. The construction chooses an independent unobserved index.
- A mismatch between the actual promise problem and Bansal–Sinha’s theorem would remove the imported `L<R(P)` input. The normalized form and thresholds agree in the supplied papers.
- Formal execution could expose defects in a chosen Lean query model or implementation even when the paper argument is valid. No formal validation is claimed here.

## Reading record for this delegated audit

- Read the whole main paper through `paper/extracted.md`, including construction, quantum upper bound, lower bound, exponent argument, and appendix; mathematical audit responsibility was §§4–5.
- Read `READ_ME_FIRST.md`, the 29 assigned ledger rows, and relevant reference metadata.
- Read Drucker’s supplied PDF via layout-preserving text extraction: §1.3, Lemmas 3.1–3.2, and the surrounding proof in §3; checked primary arXiv metadata.
- Read Shaltiel’s supplied PDF: introduction and §5 fairness theorem/proof; checked ECCC original report metadata. Did not re-audit its unrelated communication-complexity sections.
- Read Bansal–Sinha’s supplied PDF: definition Eqs. (1.1)–(1.3), Proposition 1.2, Theorem 1.3, Corollary 1.4, and surrounding discussion; checked primary arXiv metadata. Did not independently reprove its Gaussian/Fourier lower-bound machinery.
- The assigned files were readable. No assumption is made that the source trace’s prior claimed validations have succeeded.


---

# Appendix A and attribution audit

## Scope and conclusion

This is an independent manual audit of Appendix A in the supplied 5 October 2026 manuscript, plus a comparison with the relevant original literature. I read the whole main manuscript, the intake ledger and its notes, the commentary file, and the reference metadata. The main PDF's pages 15–16 were also rendered and visually inspected, to check radicals and expressions that the text extraction separates across lines. The 21 Appendix A ledger IDs are reviewed individually in `appendix_statement_review.json`.

**No substantive mathematical error was found in Appendix A.** Its proof of the known bound is sound under the standard finite-dimensional quantum query model, with an explicit zero-degree convention for constant Boolean functions and a standard purification/controlled-query conversion. This conclusion is a mathematical reading and reconstruction of the arguments, not a Lean kernel check. The Appendix is established prior work: the construction and its near-quartic lower separation are not used anywhere in it. [Main manuscript, Appendix A, pp. 14–17; `paper/extracted.md:720–864`.]

Source locations below count physical LF (`\n`) lines, matching the ledger builder's `split('\n')` convention. The extraction contains formfeed page separators; Python `splitlines()` counts these too and produces different apparent locations. The ledger's line numbers are not stale.

One definition convention needs to be explicit. The phrase “degree is unchanged by replacing input or output bits by signs” needs the Boolean-complexity convention that every constant function has degree zero. If one imports an algebraic degree with `degree(0)=-infinity`, the blanket sentence is false for the zero function. The theorem already treats constants separately, so this is a definition repair rather than a gap in the quartic bound. [Main manuscript, lines 725–727 and 862–864.]

## A. Reconstructing and checking the appendix

### A.1 What must be shown

The proof factors into four inequalities:

\[
D(f)\leq \operatorname{bs}(f)\deg(f),\qquad
\operatorname{bs}(f)=O(Q(f)^2),\qquad
\deg(f)\leq\lambda(f)^2,\qquad
\lambda(f)=O(Q(f)).
\]

Here `bs` is block sensitivity and `lambda` is the Euclidean operator norm of the sensitivity graph's adjacency matrix. Multiplying gives `D(f)=O(Q(f)^4)`, while a deterministic tree is a special randomized algorithm, so `R(f)<=D(f)`. Constants satisfy `D=R=Q=0`. All constants in this argument are universal and independent of the input length and function. [Main manuscript, Lemmas A.3–A.5 and Theorem A.1; ABKRT, Theorems 1–3, below.]

The sensitive graph is different from the tournament used for the construction. Its vertices are **all input strings** of an arbitrary Boolean function; an edge joins two strings differing in one bit when that flip changes the answer. The tournament's vertices are the **columns of one fixed input**. Reusing a picture without making this distinction would be misleading. [Main manuscript, Sections 3.2 and A, lines 353–378 and 794–795.]

### A.2 The adversary bound, including the constants

Let `Gamma` be a nonzero real symmetric matrix with nonnegative entries, zero on pairs with equal function values. Write

\[
M=\max_i\|\Gamma_i\|,\qquad
(\Gamma_i)_{xy}=\Gamma_{xy}\mathbf 1\{x_i\ne y_i\}.
\]

The denominator is positive. Some entry `Gamma_xy` is positive; since it joins opposite outputs, `x != y`, and a coordinate where they differ retains that entry in `Gamma_i`.

**The starting vector does not require irreducibility.** Take a real unit eigenvector `z` at an eigenvalue of largest absolute value. Entrywise nonnegativity gives

\[
|z|^T\Gamma|z|\geq |z^T\Gamma z|=\|\Gamma\|.
\]

The opposite inequality follows from the operator norm, so `v=|z|` attains the top Rayleigh quotient. It is nonnegative, has unit norm, and, by the equality case for a symmetric matrix, is a top eigenvector. The proof only needs its Rayleigh quotient and nonnegative coordinates. This is an elementary alternative to invoking Perron–Frobenius as a black box. [Main manuscript, line 755; independent derivation from the spectral theorem.]

Purify the algorithm. Its normalized state on input `x` is `psi_x`, starting from an input-independent state. Set

\[
W_t=\sum_{x,y}v_xv_y\Gamma_{xy}\langle\psi_x^t,\psi_y^t\rangle.
\]

Initially `W_0=||Gamma||`; every input-independent unitary preserves every overlap. Before a query, decompose

\[
|\psi_x\rangle=\sum_i |i\rangle|\phi_{x,i}\rangle,
\qquad \sum_i\|\phi_{x,i}\|^2=1.
\]

When `x_i=y_i`, the oracle acts identically on both states in the `i` component. When they differ, the product of their oracle actions differs from the identity by norm at most two. Thus the overlap change in this component is at most `2||phi_x,i|| ||phi_y,i||`. Let `u_i(x)=v_x||phi_x,i||`. Summing with nonnegative weights gives

\[
|W_{t+1}-W_t|
\leq2\sum_i u_i^T\Gamma_i u_i
\leq2M\sum_i\|u_i\|^2
=2M,
\]

since

\[
\sum_i\|u_i\|^2
=\sum_xv_x^2\sum_i\|\phi_{x,i}\|^2=1.
\]

No assumption that states on different inputs are orthogonal has been used. In fact, their changing overlap is what the argument tracks. [Main manuscript, lines 756–781.]

At the end let `p` and `q` be the two output-one probabilities on opposite-output inputs, with `p<=1/3` and `q>=2/3`. Splitting the two unit vectors by the common output projector and applying Cauchy–Schwarz gives

\[
|\langle\psi_x,\psi_y\rangle|
\leq\sqrt{pq}+\sqrt{(1-p)(1-q)}
\leq\frac{2\sqrt2}{3}.
\]

For a direct check of the last maximization, write `p=sin^2(alpha)` and `q=sin^2(beta)`, with angles in `[0,pi/2]`. The expression becomes `cos(beta-alpha)`; the smallest allowed angle difference occurs at `p=1/3,q=2/3`. Consequently

\[
|W_{\rm final}|\leq\frac{2\sqrt2}{3}\|\Gamma\|.
\]

The total change is at least `(1-2sqrt(2)/3)||Gamma||`. If the purified circuit has `q` queries, then

\[
q\geq c_0\frac{\|\Gamma\|}{M},
\qquad c_0=\frac{1-2\sqrt2/3}{2}>0.
\]

Numerically `c_0` is about `0.0285955`; the exact expression is what matters. If an adaptive algorithm is first converted using at most two ordinary bit queries per controlled query slot, one can take `c=c_0/2`. The manuscript claims an unspecified absolute constant, so this overhead is harmless. A formalisation must nevertheless prove the conversion for its chosen quantum model. [Main manuscript, lines 750–754 and 784–792; Špalek–Szegedy, Section 2.1 and Theorem 3.1, for the conventional fixed-query model and spectral bound.]

**What would overturn this check?** A purported Lean model in which intermediate measurements, variable stopping, or controlled oracle uses cannot be represented in the same fixed query model would invalidate the formal bridge, not the finite-dimensional overlap calculation. The right response would be to repair/prove that model equivalence, not to assume it silently.

### A.3 The two applications of the adversary matrix

For block sensitivity, fix an input `x` with `b` disjoint sensitive blocks. Choose the star graph with centre `x` and one leaf for each input obtained by flipping one block. The leaves need not be neighbours of `x` in the ordinary cube: general adversary matrices may join any opposite-output inputs. The star has norm `sqrt(b)`, as seen on the two-dimensional span of the centre vector and the normalized sum of leaf vectors. Each coordinate belongs to at most one sensitive block, so `Gamma_i` has at most one undirected edge and norm at most one. This proves `Q(f)>=c sqrt(b)`.

For spectral sensitivity, choose `Gamma=S_f`. The sensitivity graph is nonzero for every nonconstant total Boolean function: any path in the connected cube between opposite-output inputs must contain a sensitive edge. Within one coordinate, its edges form a matching. A matching's adjacency matrix is a direct sum of `[[0,1],[1,0]]` blocks and zero blocks, so its norm is at most one. Hence `Q(f)>=c lambda(f)`. [Main manuscript, lines 798–810; ABKRT, Lemma 9.]

### A.4 Exact degree and Huang's signed cube

Take `d=deg(f)>=1`, use sign inputs and sign outputs, and choose a monomial with support `S`, `|S|=d`, and nonzero coefficient. Fix the other variables arbitrarily. A different term could change the coefficient of the full `S` monomial only if its support were a strict superset of `S`; this is impossible by maximal degree. The restriction `g` therefore has nonzero correlation with parity on its `d` variables.

Choose `sigma` to have the sign of that correlation, and let

\[
U=\{x:g(x)=\sigma\prod_{j=1}^d x_j\}.
\]

The correlation equals `sigma(2|U|/2^d-1)`, so `|U|>2^(d-1)`. Every cube edge entirely inside `U` changes parity and hence changes `g`; it is a sensitivity edge. [Main manuscript, lines 814–823.]

The recursion

\[
H'_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
H'_{j+1}=\begin{pmatrix}H'_j&I\\I&-H'_j\end{pmatrix}
\]

has the cube adjacency as its entrywise absolute value. Squaring cancels the off-diagonal blocks and gives `(H'_j)^2=jI`. The real symmetric matrix has only eigenvalues `sqrt(j)` and `-sqrt(j)`; its zero trace forces equal multiplicities. The positive eigenspace in dimension `d` therefore has dimension `2^(d-1)`.

The coordinate subspace supported on `U` has dimension `|U|>2^(d-1)`. The two dimensions sum to more than `2^d`, so the subspaces intersect in a nonzero vector `v`. For `u=|v|`, supported on `U`, termwise absolute values give

\[
u^T A_Uu\geq v^T H'_dv=\sqrt d\|u\|^2.
\]

Extending `u` by zero embeds this Rayleigh quotient in the original sensitivity graph, because every edge of `A_U` is sensitive. Thus `lambda(f)>=sqrt(d)`. The ledger ID `claim-interlace` is acceptable as an association with Huang's method, but this proof does not need to invoke Cauchy interlacing: the dimension-intersection argument suffices. [Main manuscript, lines 824–842; Huang, Lemma 2.2 and the spectral remark after Theorem 1.1; ABKRT, Theorem 1.]

**Important explanatory point:** citing only the headline sensitivity bound `deg(f)<=s(f)^2` loses the needed information. The argument uses Huang's stronger spectral conclusion, as made explicit by ABKRT. [ABKRT, Section 3.]

### A.5 Midrijanis's deterministic algorithm

Repeatedly choose a maximum-degree monomial of the current restricted polynomial and query all its variables. Break ties using a fixed order so this is a deterministic algorithm. Stop once the restricted function is constant.

Fix the actual full input `x`. In one round, after earlier queries have been set to their actual values, let `S` be the chosen monomial's support. Freeze every other unqueried variable to its value in `x`. The top coefficient on `S` survives by maximality, so the resulting function on `S` is nonconstant. There is therefore another assignment on `S` giving an output different from its value at `x|S`. Its set of changed coordinates is a nonempty sensitive block at the **original input `x`**. Different rounds use disjoint still-unqueried supports, so the blocks are disjoint. There can be at most `bs(f)` rounds, each using at most `deg(f)` queries because restricting variables never raises degree. [Main manuscript, lines 844–860; Midrijanis, Lemma 3 and proof of Theorem 4.]

The citation to Midrijanis is correct, with one useful locator refinement: his Theorem 4 is displayed as `D(f)<=2deg(f)^3`, but its proof first establishes the stronger product statement `D(f)<=bs(f)deg(f)` used here. Citing the theorem without pointing into its proof makes the source harder to check.

## B. What is and is not new in the construction

The following is a comparison with the sources read, not a claim to have exhausted the literature.

| Ingredient | Prior source checked | Role of the October manuscript |
|---|---|---|
| Forrelation and its quantumly cheap global correlation test | Aaronson–Ambainis, original Forrelation paper; Bansal–Sinha, Theorem 1.3 and Corollary 1.4 | Reuses this hard partial function as an address component. It does not prove a new Forrelation lower bound. |
| Hiding a certificate at an address formed from many partial-function answers | Aaronson–Ben-David–Kothari (ABK), Sections 3.1–3.2 and the general framework in Section 6 | Reuses the cheat-sheet mechanism, but installs a separate addressed array in each column. |
| Verifying an addressed certificate by Grover search over local violations | ABK, Section 3.2, especially its description of `f_CS` | Reuses the verification principle; here circuit transcripts make the promise and output of the concrete Forrelation gadget exactly checkable. |
| Pointers witnessing a special all-one column | Göös–Pitassi–Watson and Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs pointer constructions | Uses outward zero witnesses from the winning column, with the additional feature that the opponent cannot find a zero in that winner at any decoded address. |
| Candidate comparison followed by quantum source/sink finding and certificate verification | Ben-David–Kothari 2026, Section 3; Ambainis–Iraids–Kokainis 2026 v2, Sections 4 and 6 | Extends the comparison framework to actual outcome probabilities with no required margin or correctness for two nonwinners. |
| Near-cubic total `R` versus `Q` from very hard partial functions | Bansal–Sinha; Sherstov–Storozhenko–Wu (SSW), Theorem 1.5 via the ABK framework | The claimed improvement comes from the new total construction and its analyses, not a stronger partial-function separation. |
| Universal `D=O(Q^4)` | ABKRT, Theorem 2, using Huang | Reproves a known upper bound in Appendix A. |

### B.1 The precise comparison with ABK

In ABK, a vector of answers selects a single cheat-sheet cell. The cell certifies both that all partial inputs satisfy their promises and that their output vector really is its address. The quantum algorithm computes an address provisionally and then checks its certificate; an off-promise address does not by itself justify acceptance. ABK already treats that totality issue. [ABK, Section 3.2, pp. 12–13.]

The new obstruction occurs **before verification**, when trying to find which of many column-owned certificates should be examined. Directly Grover-searching all `m` candidates with a `sqrt(m)` verification routine would cost about `m` queries. The October construction instead compares candidates cheaply, identifies a short list, and pays the expensive certificate check only for that list. Its outward pointers make a true winner dominant even against opponents with undefined address gadgets. The proposition about fractional comparison probabilities is what lets this shortcut respect totality. [Main manuscript, Sections 2.2 and 3, especially lines 295–302 and 466–493.]

The classical construction must also obtain an extra factor of approximately `m` over single-gadget hardness. Per-column arrays and the independently planted winning column let the lower-bound argument charge for finding the relevant address in many possible columns. The capped direct-product estimate prevents an adaptive algorithm from bypassing this cost through many lucky address guesses. [Main manuscript, Sections 4.1–4.2 and lines 714–717.]

### B.2 Bansal–Sinha versus SSW

Bansal–Sinha prove the strong classical lower bound for the **explicit Walsh–Hadamard Forrelation** problem. Their proof uses Gaussian interpolation and integration-by-parts tools; those technical estimates are not rebuilt in the October paper. They are the external hard-gadget input. [Bansal–Sinha, Theorem 1.3, Corollary 1.4, and Section 1.2.]

SSW obtain a comparably strong quantum/classical separation using **Rorrelation with a random orthogonal matrix**, together with improved bounds on Fourier mass of decision trees. Their Section 1.3, Theorem 1.5, explicitly states a total-function separation with exponent `3-o(1)` by combining their partial-function separation with ABK. Their Section 1.5, Theorem 1.9, states the improved Fourier bound. Thus SSW deserve independent credit for reaching the nearly cubic record, but their theorem is not the cited source for this manuscript's exact Walsh–Hadamard thresholds or its small exact circuit. [SSW, Theorems 1.1, 1.5 and 1.9; Bansal–Sinha's arXiv abstract also explicitly distinguishes the independent Rorrelation result.]

### B.3 What the probabilistic tournament adds

Ben-David–Kothari's sporting-event construction uses proposal cards to resolve pairwise comparisons by exact local input queries, then calls a source/sink/king-finding routine on the resulting fixed directed graph. Ambainis–Iraids–Kokainis v2 defines an exact directed graph by comparing first-one locations; quantum bounded-error subroutines implement that graph, with carefully controlled cost and error. [BK, Section 3, pp. 3–5; AIK, Section 4 and Sections 6.1–6.3.]

In the October manuscript, two nonwinners' address gadgets may be off promise. Their comparison probability can be any value in `[0,1]`, including arbitrarily near `1/2`. Repetition does not provide uniformly cheap accurate access to an independently specified deterministic orientation in this case. The new process keeps fractional weights equal to products of those **actual** probabilities and implements the exact conditional weighted law by retaining fresh comparison workspaces. Complementarity gives the drift bound; dominance is required only for a genuine winner. This is a precise extension over the fixed-graph procedures in the cited works. [Main manuscript, Proposition 3.2 and lines 295–302, 409–448.]

This supports the wording “a new total construction and a tournament lemma accommodating arbitrary off-promise comparisons.” It does not support “the first use of tournaments,” “the invention of cheat sheets,” or “a new Forrelation separation.”

### B.4 Historical refinements

- ABK's arXiv record says it subsumes Ben-David's earlier `arXiv:1506.08106`. For a precise history of the 5/2 milestone, this earlier preprint can be mentioned, but calling it independent of the later joint paper would overstate what the sources establish. [ABK arXiv metadata, Comments.]
- ABKRT's arXiv record says it subsumes the earlier four-author `arXiv:2004.13231`; this is useful if dating the quartic upper bound. The manuscript's 2021 proceedings citation itself is correct. [ABKRT arXiv metadata, Comments.]
- The near-quartic certificate-versus-quantum results do **not** settle randomized-versus-quantum complexity: `C`, `R` and `D` are different measures. In particular BK's example has `C=Omega(n^2)`, `R=Otilde(n)` and `Q=Otilde(sqrt(n))`. Its randomized/quantum gap is only quadratic up to logarithms. [BK, Theorem 1.]

## C. A missing derivation in the intake notes can be supplied

The notes assert that this construction has `bs` and exact degree of order `m` up to logarithms without showing why. That claim can be justified as follows.

Fix a valid planted input and freeze every bit except the `m` bits in its winning string `X_I`. Every other column remains nonwinning because its frozen string contains a zero. The address, transcript and outward pointers of column `I` remain valid. Consequently the restricted function is exactly `AND_m`: column `I` wins if and only if all its `m` remaining bits are one. Hence `deg(F)>=m`, and at that all-one assignment the `m` singleton flips give `bs(F)>=m`.

Conversely, the proved quantum upper bound and Appendix A imply `bs(F),deg(F)<=m polylog(m)` for fixed `k`. This is an **additional deduction from the manuscript**, not a quoted theorem or an independent verification of its two main bounds. It assumes a valid planted input exists, as constructed in Section 4.2. [Main manuscript, lines 604–607, Proposition 3.3, and Lemmas A.3–A.4.]

## D. Sources, retrieval and reading coverage

The following primary URLs were verified or matched to the attached documents. Use theorem/section locators rather than a citation only to an abstract when supporting a proof detail.

1. **ABK:** Scott Aaronson, Shalev Ben-David and Robin Kothari, *Separations in query complexity using cheat sheets*, STOC 2016; attached arXiv v2. Read abstract/introduction, Sections 3.1–3.2 including the construction and relevant lower-bound context. [Primary arXiv](https://arxiv.org/abs/1511.01937); [author publication page](https://cs.uwaterloo.ca/~s4bendav/publication/abk-16/).
2. **ABKRT:** Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal, *Degree vs. approximate degree and quantum implications of Huang's sensitivity theorem*, STOC 2021. Read the introductory proof of Theorem 2, polynomial definitions, Section 3 including Theorem 1 and Lemma 9, and Section 7 including Conjecture 2. [Primary arXiv](https://arxiv.org/abs/2010.12629).
3. **Bansal–Sinha:** *k-Forrelation optimally separates quantum and classical query complexity*, STOC 2021. For this appendix/literature subtask, read and verified the primary abstract and its explicit statement of the relation to SSW; the parent audit owns the exact thresholds and detailed theorem matching. [Primary arXiv](https://arxiv.org/abs/2008.07003).
4. **SSW:** Alexander A. Sherstov, Andrey A. Storozhenko and Pei Wu, *An optimal separation of randomized and quantum query complexity*, SIAM J. Comput. 52(2), 2023. Read abstract, Sections 1.1–1.5 and the beginning of Section 1.6, including Theorems 1.1, 1.5 and 1.9. The long Fourier analysis proof was not re-proved in this subtask; the October construction does not invoke it as its external lower bound. [Primary arXiv](https://arxiv.org/abs/2008.10223); [author PDF](https://web.cs.ucla.edu/~sherstov/pdf/quantum-classical-query.pdf); [publisher](https://doi.org/10.1137/22M1468943).
5. **Huang:** *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, 2019. Read all substantive text, Sections 1–3, especially Lemma 2.2 and the proof and spectral remark after Theorem 1.1. [Primary arXiv](https://arxiv.org/abs/1907.00847).
6. **Midrijanis:** *Exact quantum query complexity for total Boolean functions*, 2004. Read the complete attached paper, including Lemma 3 and the proof of Theorem 4. [Primary arXiv](https://arxiv.org/abs/quant-ph/0403168).
7. **Špalek–Szegedy:** *All quantum adversary methods are equivalent*, 2006. Read Section 2.1's model and Section 3's spectral-adversary definition and Theorem 3.1. The equivalence proofs between all adversary formulations are not used by the manuscript's direct proof and were not re-audited. [Primary arXiv](https://arxiv.org/abs/quant-ph/0409116); [journal DOI](https://doi.org/10.4086/toc.2006.v002a001).
8. **Ben-David–Kothari:** *Randomized query complexity can beat certificate complexity*, attached arXiv:2609.15063v1, 14 September 2026. Read the full main mathematical text, Sections 1–3, and the acknowledgments; this gives the exact comparison with the sporting-event construction. The direct arXiv abstract fetch returned `DisabledError` in this session; the attached original PDF was readable and is the evidence used. [Primary arXiv URL](https://arxiv.org/abs/2609.15063).
9. **Ambainis–Iraids–Kokainis:** *Near-optimal separations of certificate complexity from randomized and quantum query complexity*, attached arXiv:2609.11664v2, 17 September 2026. Read Sections 1–2, the comparison-based idea in Section 4, and relevant parts of Sections 6.1–6.3 (definition of the graph, candidate sets, comparison guarantees and purified implementation). Its technical appendices were not independently audited. The direct arXiv abstract fetch returned `DisabledError`; use the supplied v2 for this comparison and do not silently substitute the newer version mentioned in intake metadata. [Cited v2](https://arxiv.org/abs/2609.11664v2).
10. **Pointer history:** Read the abstracts and introduction portions of the attached Göös–Pitassi–Watson and Ambainis et al. papers to check their roles in the historical comparison; their full lower-bound proofs were not required or audited here. [GPW primary ECCC](https://eccc.weizmann.ac.il/report/2015/050/); [Ambainis et al. primary arXiv](https://arxiv.org/abs/1506.04719).

All 23 attached literature PDFs were successfully text-extracted. This does not mean their entire contents were read; the list above records what this subtask actually read. The quantum and classical subaudits cover their own proof dependencies. The packet contains no PDF for references 7 (Barnum–Saks–Szegedy), 20 (Nisan), 21 (Nisan–Szegedy), or 27 (Yao); these four originals were not read in this subtask. The spectral result was checked using the manuscript's full proof and the supplied Špalek–Szegedy and ABKRT papers. This scope limitation should remain visible in the combined return.

The intake commentary was read as a collection of leads, not used as proof evidence. In particular, a commentator's request for digests does not establish that no digests existed, and an aggregator's failure to find a human proof review does not establish that nobody reviewed the paper. No claim about the complete current review state is justified by those snippets alone.
