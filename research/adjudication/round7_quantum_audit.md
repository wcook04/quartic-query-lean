# Round-seven quantum and literature audit

This is a mathematical adjudication of the quantum-specialist return, checked
against the reviewed manuscripts, selected primary literature, Lean declaration
types and existing receipts. It is advice to the three manuscript owners, not a
new proof, Lean build, Comparator run, human review or novelty certification.
No returned script was executed. The reviewer submissions remain evidence, not
instructions.

## Scope and source boundary

The principal input is
`research/returns/round7/members/quantum_specialists/feedback.json`, with 189
findings, together with that panel's `feedback_by_document.md` and
`literature_comparison.md`. Quantum-relevant findings from the newcomer,
editorial and lower-bound panels were checked as corroborating advice. These
are analytical perspectives; their confidence and agreement do not prove a
claim. The three manuscript sources were inspected, especially the complete
quantum arguments and formal-interface passages. The long classical and
Gaussian/Fourier proofs were not independently re-proved in this audit.

The reviewed baseline is identified by the panel's hashes:

| Source | SHA-256 in the reviewed return |
| --- | --- |
| `docs/expert_companion.md` | `57a21afe55f28ef9eb5200ba0bf8aae674e27a5c06b3d56b9c0230e277f2204e` |
| `docs/exposition.md` | `90f2152e7576ade93295e7020dccfce6966bf5cd0710a56327388f5d265433a8` |
| `docs/reasoning_record.md` | `41d6dae58694ff9010d417997dc40e95c3486b9133dc2a125c6843665f902d63` |

The audit was written while the manuscript owners were revising those files;
the decisions below do not certify their eventual revised bytes. Section
anchors and quoted phrases identify the baseline passages.

## Mathematical corrections to accept

| Findings | Decision and exact correction | Why |
| --- | --- | --- |
| QS116 | Accept. At record `#upper-amplification-statement`, require an input-independent, accessible success projector, or a stored success flag already produced by the preparation. Its reflection and measurement belong to the fixed register interface. | An arbitrary unknown input-dependent subspace is not a free input-independent gate. The application uses an accessible Boolean flag, so the correction preserves the argument. |
| QS130; round-six fidelity E14 | Accept. At record `#upper-quantum-tournament`, separate the ordinary implication from state preservation to measured-label preservation from the actual dependency of the compiled upper bound. | `Upper.Samples.amplify` is a separate measured/reset implementation; the upper bound is not implemented by deriving it from `Upper.uniformOpaqueAmplifier`. |
| QS138 | Accept. At record `#upper-comparison-law`, call the **output-probability calculation** a mixture over decoded labels. | The complete retained-label preparation is coherent. Orthogonal label blocks remove cross terms in the measured probability; they do not turn the global pure state into a classical mixture. |
| QS247; LS088 | Accept. Exposition §4's statement that all numbers of trials, iterations, stages and comparisons are fixed in advance must say that their **upper caps** are fixed in advance. Apply the same correction to the amplifier's number of preparations. | Random iteration counts, first-success stopping and tournament stopping make realized counts branch-dependent. The proof supplies an input-independent cap on every branch. |
| QS251 | Accept. Exposition §5's “At m=4 there is no hard distribution” is false. Say that the displayed asymptotic lower bound supplies no **positive** budget L at this size. | Here L=0. Equal mass on the promised opposite-output examples a+ and a0 is a zero-query hard law: any input-independent output is right with probability 1/2. The useful later argument requires L≥1 and division by L. |
| QS256 | Accept. Exposition answer 4 must distinguish proving alpha_tot≥3.5 from excluding a universal bound at exponent exactly 3.5. | For k=4, every alpha<3.5 has gap 2−1/4−alpha/2>0; hence all such powers are excluded and alpha_tot≥3.5. The logarithmic losses do not exclude alpha=3.5. Choosing k=5 excludes that endpoint too. |
| LS110 | Accept. Exposition answer 2 may say that columns 2 and 4 fail their string tests, but cannot claim certain rejection by the capped verifier. | Even with exact toy decoders and deterministic comparisons, a bounded-error search for a failed test can miss it. The exact failure of a test and the probability of finding it are different assertions. |
| QS008 | Accept. Put the small-Q(g) hypothesis before suppressing Q(g) in the historical AND–OR/cheat-sheet cost display, or retain the factor m′Q(g). | The general cost contains evaluation of the partial function. ABK's concrete construction explicitly chooses a constant-query g before simplifying its cost. |
| QS029 | Accept with precise attribution. Contrast this application's fixed threshold and retry cap with **BHMT Theorem 3's untruncated QSearch**, rather than claiming unknown-success-probability search only has expected bounds. | Timeouts and bounded-time search predate this work; see primary checks below. |
| QS255 | Accept. Say k=2 gives the cubic **leading exponent**, with the displayed logarithmic losses. | These bounds exclude powers strictly below three at k=2; they do not imply an exact cubic separation or refute the cubic universal bound. |

These corrections concern local statements and evidence interfaces. They do not
provide a counterexample to the quantum upper bound or change the headline
theorem.

## Fractional example: checked exact arithmetic

Accept QS041/QS126/QS237/QS260 and NR073/LS087's diagnosis: a deterministic
cycle witnesses intransitivity but does not by itself teach sampling from
fractional weights. Keep the useful board, and add an explicitly **abstract
comparison-matrix example**. No addressed-board realization is asserted.

A particularly simple exact example has four vertices and

\[
 a_{12}=a_{13}=a_{14}=1,\quad
 a_{23}=1/3,\quad a_{24}=3/4,\quad a_{34}=2/5,
 \qquad a_{ji}=1-a_{ij},\quad a_{ii}=0.
\]

Vertex 1 is dominant. Starting with all weights one, if the first pivot is 2,
the new weights, total weight, preparation success probability and conditional
label law are respectively

\[
 (1,0,2/3,1/4),\qquad W=23/12,\qquad p=23/48,
 \qquad (12/23,0,8/23,3/23).
\]

The individual success-and-label masses are
\((1/4,0,1/6,1/16)\); dividing them by \(23/48\) gives the displayed law.
These rational calculations were checked directly. All pair probabilities
satisfy complementarity. Any such abstract finite matrix is compatible with
coherently controlled pair preparations: use a fixed two-outcome preparation
for each unordered pair and retain its flag/workspace. This observation does
not identify that preparation with the construction's particular decoder.

The alternative proposed in QS237 also works when explicitly defined: in the
record's four-candidate matrix, replace one complementary loser pair by
\(1/2,1/2\). After the stated pivot the weights become
\((1-\varepsilon,0,1/2,1)\), with total \(5/2-\varepsilon\), preparation success
\((5/2-\varepsilon)/4\), and the normalized conditional law. The owners may use
either example; using one across the funnel avoids competing numerical stories.

## Mechanism to preserve, and advice not to overinterpret

Accept QS034–035/QS040/QS262: explain the implemented loop before asking the
reader to analyze its weights. Each stage uses the already measured pivot
history, a uniform candidate label, fresh coherent comparison workspaces and a
success flag for beating every pivot. Amplification changes total success mass
while preserving the conditional pivot law. It never computes or estimates the
table of probabilities or weights.

The error guarantee is winner-only. The a_ij are **exact probabilities of the
actual comparison circuit**, incorporating decoder errors already. They are not
approximations to a hidden fixed orientation. Only the dominant vertex's
product weight needs the 1−epsilon guarantee across at most T pivots. No union
bound over all coherent comparison calls is required. Separate fresh registers
justify multiplying probabilities; retained label registers justify adding
orthogonal block probabilities.

Protect QS039/QS042/QS263 and LS025: couple stage by stage conditional on the
agreed history, and stop charging sampler disagreements once the winner is
listed. Global conditioning on all stages succeeding can bias the history.
Later termination cannot remove a previously listed winner. The verifier must
test every returned address, including off-promise decoded addresses; comparison
dominance alone is insufficient to certify an input is positive.

Accept the weighting advice QS028/QS115/QS243, NR077 and LS084: the short and
teaching papers need the capped-amplification contract, its zero-success clause
and the preserved conditional law; the full 9/40 arithmetic stays in record
§5.1. This is a division of explanatory work, not permission to remove the
record's proof. Accept NR075: the successful vector includes the label **and
retained preparation workspace**; a measured label marginal need not itself be
a pure state. Accept NR056/LS077: the elementary bridge
\(O_x(|j\rangle\otimes|{-}\rangle)=(-1)^{x_j}|j\rangle\otimes|{-}\rangle\)
explains why a diagonal input-sign layer costs one ordinary bit query.

Reject these stronger interpretations of otherwise useful advice:

- A three-cycle alone demonstrates the arbitrary-probability extension. It
  does not; a deterministic cycle is already a fixed tournament.
- The abstract fractional matrix is realized by the displayed four-column
  board. No such realization was supplied or checked.
- There is a new separation theorem because the record supplies constants,
  a uniform-in-k supplier, or a different proof route. OpenAI supplies the
  original construction and separation analysis.
- A fixed-time cap or timeout is a new quantum-search primitive. It is not.
- HMW search cannot be used in this project at all. It can search an
  appropriate fixed Boolean verification predicate; arbitrary loser-pair
  probabilities simply do not give its fixed-target bounded-error premise.
- A passing comparison proves that the shared formal vocabulary faithfully
  models the informal theorem. It proves conformity to the compared
  specification; semantic fidelity is a separate review question.

## Primary-literature checks

These are targeted reads, not claims to have independently audited every proof
in every work. No outside quotation is needed for the decisions.

| Primary source and inspected location | Checked consequence for the manuscripts |
| --- | --- |
| [BHMT, arXiv v1](https://arxiv.org/pdf/quant-ph/0005055v1), §2, two-dimensional geometry and Theorem 3 | Amplification preserves the successful direction. The specific QSearch theorem has expected preparation cost when p>0 and runs forever when p=0. Specify accessible success testing/reflection; do not attribute every possible unknown-p procedure's behavior to that theorem. |
| [BBHT, arXiv v1](https://arxiv.org/pdf/quant-ph/9605034v1), §4, Lemma 2, Theorem 3 and following paragraph | Random Grover iteration counts and the averaging estimate are standard. The final paragraph explicitly treats zero solutions with an appropriate timeout and bounded error when solutions exist. |
| [Dürr–Høyer, arXiv v2](https://arxiv.org/pdf/quant-ph/9607014v2), complete two-page paper, especially algorithm step 2 | The input values lie in an ordered set. The algorithm explicitly interrupts after a prescribed time, using expected-time analysis to prove bounded-error success. Ordinary minimum finding and timeouts therefore are appropriate antecedents, not the new arbitrary-loser-probability result. |
| [Høyer–Mosca–de Wolf, arXiv v2](https://arxiv.org/pdf/quant-ph/0304052v2), introduction and bounded-error-input contract | The algorithms compute fixed target bits with bounded error. A loser pair at probability 1/2 has no preferred fixed bit satisfying that premise. This does not obstruct using quantum search for the genuine local-test predicate later. |
| [Ambainis–Iraids–Kokainis, arXiv v2](https://arxiv.org/pdf/2609.11664v2), introduction and §6, especially U(W), Lemmas 6.4–6.6 | The source maintains genuine candidate sets in a fixed directed complete graph, uses approximate direction routines/variable-time search, and has a source-survival invariant. The present product weights generalize set membership by allowing arbitrary loser-pair probabilities directly. Its separation is between certificate complexity and quantum/randomized complexity; C must not be silently replaced by R. |
| [Ben-David–Kothari, arXiv v1](https://arxiv.org/pdf/2609.15063v1), §3, sink reduction and final verification | Exact local elimination rules define a fixed orientation, with deterministic tie rules for invalid/duplicate candidates. A sink algorithm supplies a candidate and verification follows. Candidate generation followed by checking therefore has direct antecedents; the arbitrary-probability interface is the relevant contrast. |
| [Mande–Paraashar–Saurabh, publisher abstract](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30) | A king reaches every other vertex in at most two directed edges, in a fixed tournament supplied through edge-direction queries. This supports the expert companion's stated output contract. Only the abstract and publication metadata were inspected in this audit, not the full king-finding proof. |
| [Aaronson–Ben-David–Kothari, arXiv v2](https://arxiv.org/pdf/1511.01937v2), §§3.1–3.2 | The concrete AND–OR composition first chooses a constant-query partial g. A generic historical cost display cannot suppress Q(g) before making the corresponding premise. The claimed cubic ceiling must remain scoped to the displayed recipe, not every conceivable cheat-sheet construction. |
| [Bansal–Sinha, arXiv v3](https://arxiv.org/pdf/2008.07003v3), introduction, Theorem 1.3 and Corollary 1.4 | The supplier is explicit Walsh Forrelation, with exponential-in-k quantum cost and a randomized lower bound carrying k-dependence. The fixed-k weakened supplier, uniform refinement, and growing-k diagonal argument must remain distinct statements. The source also explicitly contrasts Tal's random-orthogonal-matrix Rorrelation with explicit Walsh Forrelation. |

OpenAI's official PDF was retrieved from its
[preprint directory](https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026)
and read locally at Theorem 1.1, Lemma 2.2 and §§3.1–3.3. Its SHA-256 was
`a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.
It supplies the winner-only probabilistic-comparison argument, bounded
amplification, fresh-workspace sampling, stopped coupling and all-address
verification. It states a fixed-k polylogarithmic upper bound, rather than the
record's chosen exponent six and explicit constants. The audit found no basis
to transfer authorship of that separation to the companions.

## Quantitative and formal-source checks

`Paper.construction_family_named` in
`lean/QuarticQuery/Paper/ConstructionFamily.lean` states both bounds for the
**same named** `Forrelation.forrCircuit`, with a fixed k and an eventual
threshold: logarithmic exponent six, lower coefficient 1/400, and
`Upper.budgetConst k` as quantum constant. The headline compared family instead
uses existential constants and a floor-form lower bound. Do not say that its
configured Comparator target literally fixes b=6 or 1/400.

`Upper.Q_Fkm_le_exponential` in `Upper/Bound.lean` states
\(Q\le2^{53}k2^{10k}2^t(2t)^6\), for the named circuit and t≥1.
`ForrelationLower.forrelation_lower_uniform_sharp` in
`ForrelationLower/Uniform.lean` requires k≥2 and 15k+2≤2t and states the strict
lower bound with coefficient 2/18225, denominator
\(k^2\ln(4km)\), and numerator \(m^{1-1/k}\). These declarations support
reporting a separately available uniform estimate; they do not make arbitrary
substitution k=k(m) valid in an otherwise fixed-k statement. The particular
diagonal specialization and its exact sufficient threshold remain ordinary
mathematical derivations unless separately matched to named Lean statements.

`Upper.Samples.amplify` (`Upper/Amplify.lean`, theorem at line 346 in the audited
source) supplies the capped measured law. `Upper.uniformOpaqueAmplifier`
(`Upper/UniformEndpoint.lean`) separately supplies one choice gate fixed before
all opaque preparations, a retained original-register factorization and exact
success mass for a coordinate Boolean success predicate. The independent
UniformAmplifier challenge imports maintained model definitions; the headline
Unconditional challenge imports only Mathlib. Keep those comparison boundaries
visible without turning the main narrative into a receipt inventory.

The existing paranoid Unconditional receipt
`corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json`
records exit code zero for exactly four configured targets, toolchain
`leanprover/lean4:v4.36.0-rc2`, source commit
`9a0a5cdace28594058f6df59b9b2e45a9e7c1a4f`, and an unsandboxed local run. It is
existing execution evidence. This audit neither reran it nor enlarged its
configured declaration scope. Intentional `sorry` in a Challenge specification
is not a missing proof in the separately compiled Solution, and a historic
“unelaborated” authoring comment in a source file is not evidence that its later
recorded build failed.

## Handoff

The high-priority corrections and fractional arithmetic were sent directly to
the expert, exposition and record owners. Their revisions should preserve the
same-circuit witness, fixed-k quantifier order, exact conditional pivot law,
winner-only reliability, full retained-workspace interpretation and the
distinction between ordinary proof, Lean compilation, configured comparison and
semantic model review. The final manuscripts require their own post-edit
source/link/render checks; this report makes no claim that those checks have
already passed.

## Post-edit quantum review

At `2026-11-03T20:04:45Z`, the following source bytes were the inspected
post-edit snapshots. This is a targeted mathematical review of the passages
listed below, not an assertion that every line of each new edition has received
a fresh independent proof audit. Later source or link-pin edits require a new
snapshot binding.

| Source | SHA-256 |
| --- | --- |
| `docs/expert_companion.md` | `ed673084ceabcb5d9add35b6d055856f75c70fb0d6cf377248aadedb697706ad` |
| `docs/exposition.md` | `9497eb959769e5882f917f254538823bb424208abe0bae63bdcfec4a387c98f3` |
| `docs/reasoning_record.md` | `26275890279bdac2acf2e44cfa2bcc1139d1bb9786d54096303ebcdec086fc58` |

The expert companion's rewritten quantum argument and §7 were checked again
against the actual declaration types. The fixed accessible success flag,
fractional comparison calculation, winner-only error accounting, exact pivot
law, all-address verifier and measured/reset versus retained-state distinction
are sound. Its new §5 pointwise acceptance bounds and expectation gap were
checked algebraically. The separate classical auditor confirmed the precise
Bansal–Sinha Gaussian-chain and Girish–Tal–Wu stopped-martingale ancestry; the
record's numerical constants are not thereby attributed to those sources.

The exposition's new oracle bridge, phase-kickback identity, projection example,
full-workspace good/bad vectors, two-reflection operation, unequal-weight
example, stopped sampler, verifier and answers 2 and 4 were checked. The
amplification range was corrected to `0<gamma≤1/2`, matching the cited contract;
all its applications satisfy this. The HMW comparison now correctly concerns
an attempted use on fixed pair orientations. Reversibility now explicitly
reverses all preparation gates. The final bounds `1/250` on one-input error and
`1/1000` on zero-input error follow from the stated T and epsilon, including the
smallest board's T=12. There is no claim of certain rejection of a false
candidate by bounded-error verification.

The new gate-2 trace was checked against
`research/returns/round3/members/04_addressed_construction/examples/circuit.json`:
gate 1 is NOT input 6, gate 2 is OR of gate 1 and input 7, with zero-based
indices. On `01111000`, both input bits are zero and both gates have value one.
An independently written, data-only evaluator also checked every one of the
256 eight-bit inputs of that JSON circuit against the explicit Walsh promise;
all matched, including the domain and value output gates. It did not execute
the supplied Python checker. The circuit has 180 non-input gates and the toy
board has `4+3+2(180+2)=371` tests.

Exact rational arithmetic independently checked the expert/exposition example,
its joint label masses, complementarity and initial drift `3/2`. It also
checked the record's adjacent fractional variant: after changing only
`a_ab=a_ba=1/2`, its weights are `(11999/12000,0,1/2,1)`, total
`29999/12000`, preparation success `29999/48000` and conditional law
`(11999,0,6000,12000)/29999`. Its before-winner and after-winner failure cases
respect the stopped coupling. Both examples are explicitly abstract comparison
tables, not purported realizations by the teaching board.

The record's new success-projector qualification, measured-law paragraph and
output-mixture wording preserve the intended quantum state distinctions.
Its new physical Forrelation-implementation paragraph was checked against
`ConstructionForrelationComplete.lean` and
`ConstructionForrelationQuantum.lean`: the same F, output labeling and law
belong to the retained witness; the continuation equation applies on arbitrary
embedded states; n is existential in the wrapper and instantiated to the
repetition count by its proof; the generic physical cap is 2nk, while the
sharper nk phase-query construction is stated as ordinary mathematics. The
G.7 physical-transport remainder remains distinct from the already accepted
opaque retained-factor theorem and is not added as a premise to the final
quantum upper bound.

No counterexample or unresolved quantum mathematical blocker was found in
these inspected revisions. This review did not rerun Lean, Comparator or PDF
rendering, and it does not certify general semantic equivalence of every formal
definition with every conventional quantum model.

## Narrow final follow-up

The final exposition adjustment was read directly at its stage-coupling and
verification paragraphs. Using one common pivot at a successful stage is a
valid coupling because the real sampler's conditional law is exactly the ideal
pivot law at the common history. The failure probability is bounded conditional
on that history until the winner is listed, so the sum over at most T stages
still costs at most T epsilon. The ideal process can continue after the real
one stops; no global conditioning on all stages succeeding is being used.

The verifier now explicitly requests error epsilon/r for each partial-function
instance, hence error at most epsilon for the whole promised address by a union
bound. This is the correct error used in its final one-input bound. The expert
companion's last change to successful-state preservation explicitly allows a
global phase; this preserves, and clarifies, the conditional-label argument.
The record's replacement of “hard distribution” by “hard law” changes no
probability object or hypothesis.

The latest inspected snapshots for this narrow follow-up are:

| Source | SHA-256 |
| --- | --- |
| `docs/expert_companion.md` | `1fc60226cd4b7dd786026fba5797550b5f44c9e6b87213c2f305fa20526f41ce` |
| `docs/exposition.md` | `96d78d906eb378337b445ecf20c79c93b61aa2b0036128f51dd8014736b82b17` |
| `docs/reasoning_record.md` | `3298d076249aa85e15b00f8e66574d882e799647f406ee2486ab9130b18457b0` |

These supplement the earlier snapshots rather than rewriting their history.
The final page-break and bibliography changes do not supply proof evidence.
Later punctuation or link-pin changes should be recorded by the final
validation owner as a distinct byte rebind; this follow-up makes no claim to
have inspected future bytes. No new mathematical issue was found, and no
Lean, Comparator or rendering execution was performed by this audit.
