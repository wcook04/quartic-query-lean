# What this quantum-algorithms panel finds worth reading

This is an expert-reader review of the supplied working drafts, with attribution checks against named primary sources. It is not a new proof of the separation, an independent human referee report, or a claim to establish priority. The current documents have already repaired the important round-five sampling, stopping, cap, and independence errors. The remaining recommendations should be judged against those repaired texts. Exact current-source quotations and locations are in `findings.json`; literature coverage and editions are in `sources_read.md`.

## 1. The contribution should be explained through the invariant

The construction makes a partial-function decoder usable inside a total-function algorithm without requiring meaningful answers on losing columns. A genuine winning column has a valid address and outward pointers to zeros in all rivals. No rival address can find a zero in that winner’s all-one string. Consequently, a comparison needs the winner’s own decoder to be correct; it does not require the rival decoder to satisfy a promise. That local semantic fact is the bridge from the addressed construction to the probabilistic tournament. It is already explained correctly and should remain prominent. [Current companion §§1.2, 2, 4.1; record §§4.2, 4.7, 5.3; supplied preprint Lemma 2.2 and Proposition 3.3.]

The genuinely informative next object is the product weight. For a fixed input and classical pivot history, the record sets

\[
w_i=\prod_{p\text{ previously selected}}a_{ip},\qquad W=\sum_iw_i.
\]

Fresh comparison workspaces give success-and-label mass \(w_i/m\). Thus an unamplified preparation succeeds with probability \(W/m\), and, conditional on success, the measured label has distribution \(w_i/W\). The weights are analytical quantities; the algorithm does not calculate or estimate them. The exact law, rather than a generic promise to return a good label, is what lets the physical procedure inherit the ideal process. [Companion §4.2, display (9); record §5.2, `upper-stage-state`, `upper-stage-law`.]

The ideal step samples a pivot \(j\) with that law and replaces \(w_i\) by \(w_i a_{ij}\). Since \(a_{ij}+a_{ji}=1\) and \(a_{ii}=0\), the existing proof obtains

\[
\mathbb E[W'\mid w]
=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2
\]

when \(W>0\). A true winner’s weight remains large until that winner is selected, because only its one-sided comparison guarantee is needed. Before selection this provides the success-mass threshold for the capped sampler. After selection, subsequent failure cannot remove the winner from the returned list. The coupling therefore stops charging failures at the right event, rather than demanding a uniform success threshold for every later history. These are the ideas to protect when reducing detail. [Companion §4.2, Ideal process / Exact sampling / Coupling; record §5.2, `upper-ideal-process`, `upper-coupling`.]

## 2. What changes relative to the nearby algorithms

The related-work paragraph now names the correct antecedents. A stronger next revision would connect their mathematical objects to the invariant above, rather than add more names.

| Source and inspected locator | Object the reader already understands | What changes in the present argument |
|---|---|---|
| Dürr–Høyer, Theorem 1 and Lemmas 1–2 | A threshold in an ordered table; ranks explain improvement, and a timeout converts the cost analysis into bounded completion. | Cyclic comparisons have no global rank. Fractional mass replaces the rank-based account of progress. |
| Mande–Paraashar–Saurabh, §4; published Theorem 19 | A fixed tournament, common-neighbourhood sampling and a king that exists on every tournament input. | The reusable theorem returns a bounded list containing a nearly dominant candidate when one exists; it is not a general probabilistic KING solver. |
| Høyer–Mosca–de Wolf, §§1–3 | Coherent bounded-error evaluators of fixed Boolean predicates with a uniform correctness margin. | A loser pair may have probability exactly one half, so neither orientation is computed with a uniform margin. A deterministic cycle alone would not establish this obstruction. |
| AIK v2, §§6.1–6.3, equations (3)–(4), (8)–(10) | The hard set \(U(W)\) of candidates beating all previous pivots, with fixed intended edges after input/classification choices; variable-time sampling with controlled point probabilities. | Products of actual comparison probabilities give soft survival weights. With binary probabilities they become membership indicators, but the algorithms’ sampling contracts, costs and outputs are not identical. |
| BDK v1, Theorem 1 and Lemma 5 | Exact local candidate comparisons, a virtual candidate list, champion search and final certificate verification. | Cheap quantum search alone does not force high randomized complexity; the new per-column address hardness supplies the additional classical charge. |

Sources are identified by full title, edition, local path and primary URL in `sources_read.md`. BDK directs arcs from loser to winner and calls the winner a sink; a comparison table must normalize orientation before treating source/sink terminology as a mathematical distinction. AIK’s approximate-membership sampling should not be called exactly uniform. These qualifications prevent an attractive analogy from becoming a false reduction. [S-DH; S-MPS; S-HMW; S-AIK; S-BDK.]

The BDK comparison is particularly useful: its displayed construction has \(C=\Omega(n^2)\), \(R=\widetilde O(n)\), and \(Q=\widetilde O(\sqrt n)\). A quartic separation involving \(C\) can coexist with an essentially quadratic \(R\)-versus-\(Q\) relation. The present lower bound has to establish the cost of hard addresses in many different columns. The current documents say which measures differ; adding this already-published parameter comparison would explain why the difference matters. [BDK Theorem 1; companion §§1.2–1.3, 5.2–5.4.]

## 3. Which quantum contract is actually consumed

There are three different reasons to discuss coherence, and they should not be compressed into a single stronger/weaker label.

| Contract | Why it matters here | Current evidence boundary |
|---|---|---|
| Retain decoder and comparison workspace so the preparation and its inverse are available. | Needed inside coherent amplification and the fresh-register product construction. | The record constructs this explicitly; it is not a demand to keep the entire adaptive tournament coherent. |
| Preserve the exact law of the measured pivot label. | Sufficient for the drift/coupling argument and the headline upper bound. | This is the physical measured-law route the record identifies as used. |
| Return a specified original register in its normalized successful state. | A stronger composable state contract, interesting independently of the measured tournament. | A compared opaque-preparation theorem really provides a retained-factor identity and logical cap. The record does not claim the complete stronger physical output-subsystem wrapper. |

The last boundary must not be described as “only a label law has been proved,” because that would deny the real opaque-state theorem. Nor should the opaque theorem be silently identified with the complete physical wrapper. The existing §5.5 explanation is careful; it should be visible at the first short-paper claim. [Record §§5.1, 5.2, 5.4–5.6; `UniformAmplifier/Challenge.lean`; supplied round-five statement-fidelity review.]

The pivot measurement is also worth one explicit sentence of explanation: coherence is maintained within a preparation/amplification call, the successful index is measured, and subsequent preparations use the resulting classical history. This makes the sufficiency of a measured-label theorem natural. BHMT supplies the familiar preservation of the good direction; the problem-specific content is the all-input cap and its use to implement the exact conditional pivot law. [BHMT §2, Lemma 1 and equation (8); BBHT §4, Lemma 2; record §5.2.]

## 4. What the Forrelation experiment and circuit are doing

The squared projection experiment follows the preprint and has success probability \(\Phi^2\). The cited literature also has a signed interference experiment with probability \((1+\Phi)/2\), using \(\lceil k/2\rceil\) queries for one experiment. That is not the cost of a complete constant-error decoder at a shrinking promise threshold; error reduction still matters. Both procedures are already documented, so the review asks for the reason for the selected experiment, not a replacement algorithm or an improved bound. [AA §3.2, Figure 1 / Proposition 6; BS Proposition 1.2 and its amplification consequence; record §3.3 final paragraph.]

The negative-\(\Phi\) example remains excellent. It shows that this projection statistic cannot certify the one-sided promise. A signed promised decoder would still not be an exact all-input domain recognizer, so it would not remove the domain-bit obligation. The exact Boolean circuit has a separate job: its domain/value transcripts become locally checkable certificates. Its size \(S\) enters the local-test count \(K=m+(m-1)+r(S+2)\), which enters short-list verification cost. That chain is why a quantum specialist should care about nearly linear circuit size; the ripple-carry details can remain in the complete record. [Companion §2 and §4.3; exposition §§1–3; record §§3.3–3.5, 4.1, 4.4, 5.3–5.4.]

The long supplier reconstruction deserves its own expert route. It changes the truncation/distribution and reorganizes the derivative argument; the record already explains how this differs from BS and relates to GTW. Move a compact statement of that distinction to the route entrance. The uniform estimate’s better \(k\)-dependence and worse logarithmic dependence are not an unqualified domination of the full published BS theorem. Its role as a strengthening of the particular fixed-\(k\) consequence needed here is a different comparison. No priority claim follows from this review. [Record §§3.6, 3.8, 3.10, 3.15–3.16; BS Introduction and §5.4; GTW Introduction / technical overview; supplied statement-fidelity review.]

## 5. Explain the exponent history by the cost that stayed fixed

The current companion correctly derives the two endpoint cheat-sheet calculations. The following is a compact reading of those existing source results, not a new limitation theorem:

| Cited stage | Partial randomized exponent \(c\), suppressing logarithms | Total exponent in the cited balanced cheat-sheet route | What changed |
|---|---:|---:|---|
| ABK using Forrelation | \(1/2\) | \(2+c=5/2\) | Initial partial-function hardness inside the composition. |
| Tal | \(2/3-o(1)\) | \(8/3-o(1)\) | Stronger partial hardness. |
| BS; independently SSW for rorrelation | \(1-o(1)\) | \(3-o(1)\) | Essentially optimal partial hardness; the cited outer cost balance remains. |
| Present per-column addressed construction | \(R(P)\approx m^{1-1/k}\) | \(4-2/k\), from \(mR(P)\) versus \(\sqrt m\) | The outer construction distributes the hard address cost over many columns. |

At the balanced parameter choice in the cited ABK route, composing with AND–OR gives classical cost about \(n^{2+c}\), while computing the composition and checking its certificate costs about \(n\) quantumly, up to logarithms. The point is what stopped this particular route at the cube once its partial supplier was near optimal. It is not a claim that every conceivable cheat-sheet variant has a cubic ceiling. [ABK §3.1; Tal Introduction / total-function application; BS main corollaries; SSW Introduction applications; companion §1.1.]

For the actual theorem, the fixed-\(k\) argument suffices: choose \(\alpha<4\), then fixed \(k>2/(4-\alpha)\), then let \(m\) grow. Both bounds must concern the same circuit-defined function. The newer growing-\(k\) remark is optional and uses already stated uniform ingredients; its missing detailed destination in the record is a recoverability issue, not a gap in the fixed-\(k\) proof. Neither argument gives a literal \(R=\Omega(Q^4)\) statement. [Companion §7; exposition §6; record §7.]

## 6. Where this panel would pause or stop

These are predicted friction points, not observations of real participants.

| Perspective | Likely pause or stopping point | What would make continuing worthwhile |
|---|---|---|
| Forrelation algorithms | Projection statistic and domain circuitry before the choice of experiment is explained. | The existing signed-test comparison and the S→K→verification dependency. |
| Amplitude amplification | Standard geometry before the tournament’s required contract. | The capped sampler interface and exact distribution it must preserve. |
| Bounded-error search | A cycle offered without a separate no-margin discussion. | The current repaired distinction, kept at first use. |
| Minimum finding | An array of counterexamples for later classical machinery before the new progress measure. | Rank-to-weight comparison, then the invariant. |
| King finding | A “tournament” whose output contract is only implicit. | Unconditional cap/list size, conditional containment, and final verification. |
| Certificate separations | Merely naming a different classical measure. | The published C,R,Q comparison and the extra address-hardness obstruction. |
| Cheat sheets | A chronology of exponents without the intermediate arithmetic. | The 2+c explanation followed by the changed outer balance. |
| Forrelation lower bounds | Many pages of reconstructed analysis before the source-to-reconstruction map. | An early map plus a reason for the altered truncation. |
| Fourier growth | A first-block derivative argument mistaken for ignoring higher Fourier levels. | The existing biased-derivative warning and expansion, preserved. |
| Formal-model inspection | Contradictory review labels or an unqualified “full form” claim. | Current status by scope, exact used model, and representation-specific contracts. |

The contribution of these documents is explanatory and evidential: they make the source theorem, dependencies, subtle events and formal statement inspectable. The packet does not supply a human reading experiment establishing that the presentation succeeds. The review therefore makes concrete, source-located predictions and protects worked examples that actually demonstrate the claimed distinctions. `reader_principles.md` assesses all fourteen supplied criteria on that basis.
