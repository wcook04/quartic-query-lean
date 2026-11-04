# Mathematical verification of the round-ten exposition

## Scope and conclusion

This is a retrospective mathematical check conducted after the primary reader's first-pass freeze. It is not an independent cold reading. I read the complete current `repository/docs/exposition.md`, checked the mechanisms listed below, inspected the stated cross-document destinations in the supplied snapshot, and wrote fresh exact-arithmetic checks for the finite examples. **No mathematical error was established within that scope.** This conclusion is narrower than an independent proof of the complete formal development or the analytic Forrelation lower bound.

The finite checks are in `finite_example_results.json`, produced by `verify_finite_examples.py`. The latter reads the preserved 180-gate circuit as JSON data and evaluates it with a newly written interpreter. No submitted checker, Lean build, Lake command, or Comparator process was executed. The mathematical checks and their boundaries are also recorded in `mathematical_checks.json`.

All manuscript line numbers below refer to the exact supplied Markdown, not a live repository branch. Cross-document links were followed to their corresponding local snapshot passages. **The supplied `LINK_MAP.json` explicitly marks all 13 exposition links to the reasoning record and its one link to the expert companion as `pinned_differs_from_packaged: true`.** Thus the checks below establish the adequacy of current packaged proof passages, not of the exact online prose destinations at revision `8357f268732746d1575e05e7de8c888e20ad3793`. Those pinned prose bytes were not retrieved by this verifier. Code-link identity is a separate metadata claim and was not inferred from the prose checks.

## 1. Exact finite examples

| Exposition location | Independent calculation | Result and scope |
| --- | --- | --- |
| §1, lines 55–100; answer at 498 | Multiply the displayed Walsh matrix by each sign block using integer arithmetic. | The three amplitudes are $1,0,-1$; their projection probabilities are $1,0,1$. The projection exercise gives amplitude $1/2$ and probability $1/4$. |
| §2, lines 145–165 | Evaluate all 256 eight-bit inputs through the supplied 180-gate list, and compare its two outputs with the exact rational promise inequalities. | Every circuit output agrees. Gates 1 and 2 have value 1 on the displayed $a^+$. There are 371 tests per candidate. |
| §2, lines 135–167; answer at 502 | Reconstruct all four column strings, all four cells per column, true transcripts, and pointer rules. Check each of the 16 candidate pairs. | The base board has the unique winner $(1,10)$. Column 1's failure counts at addresses $00,01,10,11$ are $1,2,0,1$. |
| §2, lines 147–167 | Apply exactly the domain-board changes and repeat the candidate checks. | There is no winner. Column 2 has failure counts $1,2,2,3$, and its only failure at $00$ is the first domain test. |
| §4, lines 229–243 | Apply the false-pointer mutation and the three cycle mutations separately, preserving the rest of the base board. | The false-pointer board has no winner but column 1 beats every rival for every rival label. The cycle has $2\to3\to4\to2$, and these edges hold for all 16 label pairs for each edge. Column 1 remains the unique winner. |
| §4, lines 239–247 and 269–279; answer at 506 | Use exact fractions for the transition matrices and multiply the old weights by the selected matrix column. | First-step totals on the cyclic board are $0,2,2,2$, with mean $3/2$. The fractional examples give $23/48$ and $19/60$, with the printed conditional laws. |
| §5, lines 375–377; answer at 508 | Enumerate all $4^4=256$ zero-position tuples and average the dependent selection rule exactly. | One fixed row per column gives independent hit probability $1/4$, dependent hit probability $175/256$, and a uniform dependent marginal. Two fixed rows give $1/2$ and $15/16$. |
| §5, lines 402–419; answer at 510 | Enumerate the 16 equally likely target tuples ((a,b,c,d)). | The original light visit has probability $1/8$; the capped simulator succeeds with probability $1/4$. The stopping modification contributes $1/8$ at each of times 3 and 4. A later second target query makes the first branch heavy, leaving $1/8$. |
| §5, lines 385 and 432–434 | Enumerate every one-query deterministic AND rule and the proposed pooled-budget and parity-side-information strategies. | The promised AND optimum is $2/3$; the full two-bit AND optimum is $3/4$. The displayed counterexamples give $1$ conditional success, $3/4>9/16$ pooled success, and $1/2>1/4$ parity-assisted success, respectively. |

These computations test the concrete examples and the circuit data. They do not establish large-parameter lower bounds, general quantum correctness, or any formal compilation claim.

## 2. Query convention, decoding, and exact certification

### Worst-case query caps

The convention in exposition lines 14–26 is the one used by the supplied formal statement: the input is fixed before evaluating success probability, and every branch obeys the query budget. `Challenge.lean` lines 41–65 bound the depths of all supported deterministic trees; lines 101–137 define a syntactic maximum over quantum measurement branches. The circuit, initial state, and free transformations are chosen independently of the input. This prevents either proof from hiding expected-cost or input-dependent-computation assumptions.

The phase-kickback construction at exposition lines 78–98 uses one ordinary bit query for each sign diagonal. The whole-input coordinate $4(h-1)+j$ is computed without a query, and the full oracle remains the ordinary XOR oracle. The final Walsh transform implements projection onto $u$. The negative example is correctly outside the promise even though its projection experiment succeeds.

### Repetition and coherence

At lines 177–188, the promised probabilities obey $p\ge c$ or $p\le c/4$, where $c=2^{-10k}$. The lower-tail estimate $e^{-\rho c/8}$ is valid at $p=c$, and stochastic monotonicity extends it to larger $p$. For the small-probability case, the usual multiplicative upper tail at twice the mean gives the stronger exponent $e^{-\rho c/12}$ when $p=c/4$, so the printed $e^{-\rho c/16}$ is safe. The ceiling in the number of repetitions and the real threshold cause no gap: the event $Z\ge\rho c/2$ is the corresponding integer threshold event.

The record gives a separate elementary moment-generating-function proof of the shared $e^{-\rho c/16}$ bound at lines 589–629. Its retained-register construction at lines 631–681 establishes why the same Bernoulli law survives coherent evaluation. The exposition's fresh-register argument is valid **conditional on the fixed input and fixed candidate**; it does not assume independent input bits. The distinction matters because separate calls query the same fixed input oracle.

### Exact circuit and local tests

The denominator $2^{t(k+1)}$ in exposition line 196 follows from two factors $m^{-1/2}$ in the endpoint vectors and $k-1$ factors $m^{-1/2}$ in the Walsh matrices. The integer inequalities are equivalent to both promise thresholds, including their equality cases. The cited circuit section supplies the promised fan-in-two realization and the constant 200; the exposition does not claim that its small 180-gate truth-table circuit is the general arithmetic circuit.

The record's circuit implementation uses arithmetic modulo a power of two and recovers the signs of the final comparison integers. The exposition's shorter discussion of sufficient word length is a valid existence-level sketch, but should not be read as claiming that every intermediate stored word in the formal implementation is a signed integer without wraparound. That distinction is explicit in the linked record, lines 690–707 and 734–789.

Gate consistency alone does not certify the promise or address. The two output checks per instance supply those additional assertions. Acyclicity forces any completely gate-consistent transcript to equal the true evaluation. The total test count

\[
K=m+(m-1)+rS+2r
\]

therefore tests precisely the winning predicate. The pointer tests charge the ℓ pointer bits and the selected target bit, rather than treating an entire cell or a fixed set of target coordinates as one query. The coherent controlled-read implementation in exposition line 319 and record lines 1966–1998 pays two ordinary oracle calls per controlled read; it retains the selected coordinate through the cancelling call. This is sufficient for uniform-index evaluation and its inverse.

## 3. Tournament and verification

### Complementarity and winner dominance

The canonical unordered-pair experiment in line 215 establishes $a_{ij}+a_{ji}=1$ as an equality of laws. It does not say that separate physical calls share their randomness. The self-comparison rule supplies $a_{ii}=0$. Those are the exact assumptions used in the drift identity.

The winner's all-one string prevents its disqualification under **every** rival label. Decoding the winner correctly suffices to disqualify the rival, so only the winner's decoder accuracy contributes to $a_{i^\star j}\ge1-\varepsilon$. The arbitrary or off-promise behavior of the rival decoder is harmless. Conversely, the false-pointer example correctly shows why comparison dominance cannot replace the final certificate check.

### Drift and the ideal list

For nonnegative weights with total $W>0$, averaging the update over a pivot chosen with law $w_p/W$ gives

\[
\mathbb E[W'\mid w]
=\frac{1}{W}\sum_{i,p}w_iw_pa_{ip}
=\frac{W^2-\sum_iw_i^2}{2W}
\le W/2.
\]

The process remains at zero after absorption. Hence $\mathbb E W_T\le m2^{-T}$ also holds on absorbed histories. Until the winner is selected, its weight is at least $1-T\varepsilon>1/2$, so a missing winner implies $W_T>1/2$; Markov then supplies the printed bound. There is one factor per listed pivot, not per physical comparison call during amplification.

### Successful label law and capped amplification

For a fixed pivot history, orthogonal candidate labels and fresh comparison workspaces give joint mass $w_i/m$. This is a probability, not an amplitude. Dividing by $W/m$ gives the ideal law. In the two-dimensional amplification argument, $g$ contains the candidate register **and all original workspace**. The reflection and success flip alter its scalar coefficient but not its normalized label law. The matrix multiplication in lines 292–297 has the correct signs.

The bounded schedule in line 301 is justified by record lines 2128–2197: the direct half covers success probability at least $1/2$, the randomized iteration half supplies at least $9/40$ in the remaining promised range, and $N$ fresh failures have probability at most $(31/40)^N\le\eta$. The call cap holds even below the threshold. Each successful trial has the same normalized successful state up to phase, so conditioning on the first successful trial does not introduce label bias. At probability zero, no conditional law is asserted; at probability one, the endpoint argument is deterministic.

### Stopping and final verification

The coupling in lines 307–313 only requires sampler success bounds before the winner is listed. Conditional on each common history, the real successful transition is the ideal pivot law; the extra stopping probability is at most ε. Once a winner is stored in the list, later failure cannot remove it. Summing over at most $T$ histories adds $T\varepsilon$, without an assumption that failure probabilities are independent across stages.

The violation search has the correct polarity: finding a defect rejects a candidate; finding no defect accepts it. A nonwinner fails some test at every proposed address, so its false acceptance probability is at most ε conditional on the selected list and the past, because verification starts afresh. On a one-input, accepting a false candidate early still gives the correct Boolean answer. Thus the two error accounts in line 323 require no extra error term for comparison decoding.

The cost expression in lines 325–337 consistently adds the tournament and final-list verification. With $r,T,1/\varepsilon=O(\ell)$, $K=O_k(m\ell^3)$, and the deliberately enlarged logarithmic bounds, the respective costs are $O_k(\sqrt m\ell^6)$ and $O_k(\sqrt m\ell^5)$. The sharper counts in companion lines 207–211 also imply the same displayed sixth-power bound. There is no inconsistency between the two accounts.

## 4. Planted lower bound

### One hard distribution and two changed locations

The finite minimax consequence at line 350 is valid: failure of every cap-$L$ randomized strategy supplies one distribution defeating all deterministic trees of that cap. The record's finite convex-separation proof even supplies a strict common margin below $2/3$. The exposition and record transpose the payoff-matrix row/column convention; this is harmless.

The dummy input is zero because every column contains a zero, irrespective of whether a blank cell happens to satisfy some transcript conditions. Planting changes only the selected zero bit and bits in its true cell. Identical deterministic adaptive histories persist until the first changed answer. Counting every queried bit of the true cell may overcount unchanged bits, and therefore gives a valid upper bound.

The independent selection of $I$ gives the exact identity $\Pr(\text{erased zero hit})=\mathbb EZ/m$. Given a complete compatible query prefix, each zero is constrained only by the string bits read in its column: the other latent fields are independent and all cells are blank. An undiscovered zero is uniform over unread rows. Early discoveries contribute at most $2G/m$ in expectation, and late discoveries occur in at most $2G/m$ columns pathwise. The factor $4G/m^2$ follows.

### The direct product and stopped simulator

The direct product uses separate deterministic caps on every instance and side information jointly independent of the full input tuple. A compatible positive-probability transcript is a product of per-instance constraints, even when the query schedule is adaptive. Only one continuation value changes at a query, so multiplying its conditional expectation inequality by the other fixed, nonnegative factors is legitimate. At a leaf, conditional success is bounded by the product of continuation values. Arbitrary independent coins and side information reduce to finitely many capped deterministic behaviors because the input positions, branch depth and output alphabet are finite. These are sufficient hypotheses; a global expected cap or pairwise independence would not suffice.

The simulator at lines 387–400 is genuinely capped on **every** target tuple. It stops before a query that would exceed the total target cap $L$; this cap implies $L$ separately on every instance. Inspecting the proposed global coordinate at time $j$ does not read a cell bit. The simulator's outside information is independent of the entire target tuple, including the target column's independent zero position. The complete-run light event is used solely for the containment

\[
\{\text{light and true-cell query at time }j\}
\subseteq
\{\text{capped predictor outputs the true address}\}.
\]

No conditioning on lightness occurs. Default guesses may be correct, so replacing containment by equality would be wrong. The manuscript states the one-way implication correctly. Reversing the order of the target-cell detection and the cap test would be needlessly restrictive; the printed order correctly allows a cell query after exactly $L$ target reads.

For each fixed column, the union over global query times costs $G(2/3)^r$. Averaging over the independent uniform planted column cancels the apparent factor $m$. The heavy-column count is a whole-run count, so it is compatible with the cap-event used in the simulator lemma. A later target query can make a prior cheap-looking visit fall outside the light event; Question 4 and its answer correctly expose this.

### Constants and randomized contradiction

Since $r=40t$, $(2/3)^r\le(1/2)^{20t}=m^{-10}$. The three discrepancy terms are at most $4/100$, $1/100$, and $1/(100m^8)$, strictly below $1/3$. The two input distributions do not depend on the randomized algorithm's coin string, so averaging the deterministic absolute discrepancies is valid. A correct cap-$G$ algorithm would require a signed gap of at least $1/3$, yielding the contradiction.

The floor shortcut in line 470 is correct: an integer $R>\lfloor z\rfloor$ satisfies $R>z$. Together with $\lfloor x\rfloor\ge x/2$ for $x\ge1$, the exposition obtains the stronger coefficient $1/200$ and then weakens it to $1/400$. The record and companion use a second floor estimate; this is a difference of presentation, not of conclusion.

## 5. Quantifiers and formal statement strength

For a fixed $0\le\alpha<4$, taking $k>2/(4-\alpha)$ gives the positive exponent $d=2-1/k-\alpha/2$. All constants are then fixed before $m\to\infty$. The ratio lower bound diverges, because any positive power dominates the fixed logarithmic power. The zero exponent at $k=4,\alpha=3.5$ does not refute that endpoint; $k=5$ does. These calculations and Question 5's answer are correct.

The source preprint's Theorem 1.1 has existential constants and a logarithmic exponent; the exposition explicitly identifies six and $1/400$ as reconstructed choices. `Challenge.lean` lines 328–334 similarly state an existential logarithmic exponent and the floor lower bound. `ConstructionFamily.lean` lines 30–54 are a genuinely stronger named-circuit statement: the same explicit `forrCircuit` appears in both inequalities with six and $1/400$. Its old preparation-time comment is not a new execution result, and the exposition does not treat it as one.

The formal winning predicate, lines 266–272 of the challenge, includes the exact `some` clause rejecting the off-promise domain board. `CircuitRealises` at lines 217–221 requires the value bit to be correct **on** the promise, but does not itself force the value bit to zero off the promise. The explicit circuit does have that stronger behavior; the exposition's generic reference to a circuit realizing $P$ does not silently strengthen the formal family theorem.

One benign endpoint convention is worth recording for statement readers: exposition line 22 permits input length zero, whereas the companion and formal `UniversalPower` quantify over $n\ge1$. The extra length-zero functions are constant and have $R=Q=0$, so the admissible-exponent set is unchanged. This is an equivalence bridge, not a defect in the mathematical claim. Likewise, the cubic $Q^3$ and $(1+Q)^3$ assertions are equivalent up to a constant because nonconstant Boolean functions require at least one query.

The ordinary deductions above do not establish a new Lean or Comparator run. The four `sorry` terms in the challenge are intentional statement placeholders. The separately supplied solution invokes the established declarations; checking those proof terms and all dependencies requires an actual trusted Lean execution, outside this review's task.

## 6. Cross-document destinations inspected

| Exposition origin | Local destination inspected | What the destination provides |
| --- | --- | --- |
| Line 159 | Record §4.4, lines 1926–1946, anchor `AC-example-tests`; accompanying gate-list JSON | Exact small-circuit gate numbering, the 371 tests, links to preserved check evidence, and the explicit warning that the checker board has different decoder probabilities. |
| Line 196 | Record §3.4, lines 686–800, anchor `forr_circuit` and following arithmetic sections | Integer/modular construction, final signed comparisons, gate model, explicit size bound. |
| Line 301 | Record §5.1, lines 2073–2197, anchor `upper-grover-trial` within the section | All-input schedule, averaged trigonometric estimate, first-success conditional-state argument, and fixed call cap. |
| Line 319 | Record §4.6, lines 1959–1998, anchor `AC-coherent` | Superposed test-index implementation, controlled-read overhead and retained workspace. |
| Line 337 | Record §5.4, lines 2728–2748, anchor `upper-explicit-log6` | Explicit polynomial logarithmic accounting for the same circuit family. |
| Line 350 | Record §6.2, lines 3287–3313, anchor `CL-minimax` | Self-contained finite separation argument yielding a common hard law. |
| Line 371 | Record §6.4, lines 3438–3502, anchor `CL-early-late` | Selection identity, transcript conditioning, early/late estimate. |
| Line 402 | Record §6.5, lines 3567–3662, especially anchor `CL-simulator-example` | Matching XOR trace, zero-based-label warning, joint-event inclusion, union bound. |
| Line 480 | Record §7.3, lines 3902–3970, anchor `ROOT-GROWING-K` | A separate growing-parameter schedule from uniform estimates; this is not needed by the fixed-parameter proof reviewed here. Its underlying analytic uniform supplier was not re-proved in this audit. |
| Line 484 | Record Appendix A opening, lines 3972–3988, anchor `R3-A-RESULT` | The stated universal bound and source/route distinction. The complete appendix proof was not re-audited. |
| Lines 490–494 | Challenge lines 31–140, 217–285, 295–340; complete Solution; ConstructionFamily lines 1–76 | Exact models, winning predicate, four challenge statements, and stronger named-circuit constants. |

The model explanations linked at line 490 were additionally inspected at record lines 186–350. The Forrelation destination linked at line 202 was inspected through its statement, literature translation and proof overview at lines 854–932; the subsequent analytic proof was outside this audit.

## 7. Literature reading and limits

- **OpenAI, _A Nearly Quartic Separation Between Randomized and Quantum Query Complexity_, supplied preprint dated 5 October 2026.** Read the supplied extracted text at lines 1–64, 151–203, 363–448 and 528–586: headline quantifiers, the three partial-function properties, tournament argument, and direct product. This establishes correspondence with the supplied source, not public provenance of that preprint.
- **Bansal–Sinha, arXiv:2008.07003v3.** Read supplied extracted text lines 1–88 and independently extracted the supplied PDF's printed page 4, which actually labels the relevant results Theorem 1.3 and Corollary 1.4. These match the one-sided promise, threshold $2^{-5k}$, and fixed-$k$ lower-bound consequence used in the exposition. The Markdown conversion renumbers some theorems, so the PDF was used to verify the citation. The whole analytic proof was not reread. Source identifier: <https://arxiv.org/abs/2008.07003v3>.
- **Aaronson–Ben-David–Kothari–Rao–Tal, arXiv:2010.12629v1, title-page arXiv date 23 October 2020.** Inspected PDF pages 1–2, including Theorem 2 and its proof from the stated degree bound, and the extracted Conjecture 2 passage. The quartic $D$-versus-$Q$ theorem is the imported upper bound used here. The full degree/spectral argument was not independently verified. Source identifier: <https://arxiv.org/abs/2010.12629v1>.
- **Drucker, arXiv:1005.0644v2, 9 May 2014.** Read the supplied full-text extraction lines 455–595, covering Lemmas 3.1–3.2, the product-potential proof and the fair-algorithm specialization. The exposition accurately uses the separately capped specialization rather than presenting the paper's global-budget headline theorem as identical. Source identifier: <https://arxiv.org/abs/1005.0644v2>.

No new web retrieval was performed by this verifier; these were supplied primary texts. General current-literature and pedagogical comparison work belongs to the separate literature reviewer. The full reasoning record, all literature annexes, proofs of every imported theorem, dependency source implementations, render appearance, and historical build receipts were outside this mathematical audit's inspected scope.

## 8. Consequences for editorial findings

The mathematical check does **not** justify new error findings about reversed Grover signs, absent cap control, a missing factor $m$, conditioning on lightness, uncharged whole-cell reads, or a claimed growing-$k$ conclusion from fixed-$k$ constants. The current exposition already handles these points. If the editorial review recommends a shorter schedule discussion, relocated direct-product proof, a different example, or reduced formal-evidence detail, its acceptance criteria should preserve the concrete contracts above.

The strongest useful revision constraints are: keep the exact successful-label law; keep the stop-before-read rule and the direction of event containment; keep whole-run lightness and joint independence; keep the same circuit in both family bounds; and keep the order α, then fixed $k$, then growing $m$. These are mathematical dependencies of a redesign, not praise-only findings or requests for new theorems.
