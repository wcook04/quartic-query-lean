# Round-seven independent AI cold read

This is an AI editorial and mathematical reading, not a human reader study,
peer review, fresh Lean build, or independent execution of Comparator. The
reviewer did not write either manuscript. Both short documents were read from
beginning to end, including their answers, formal-scope sections and
bibliographies. Selected changed passages of the record and actual Lean source
were then inspected. The record as a whole was not reread.

The result is a recoverable proof spine in both short documents, with two
concrete editorial regressions found and repaired. The useful tests are the
operations below, not a readability score or absence of flagged vocabulary.

## Review boundary

The source review ran while the writers completed revisions. The first full
expert PDF inspection covered all 15 pages of
`expert/expert_companion.pdf`, SHA-256
`fd80f7529edbf21b0242091bfe139fd2731b51f7b42f0af5b8384965f6150876`.
Its build manifest recorded expert source
`ed673084ceabcb5d9add35b6d055856f75c70fb0d6cf377248aadedb697706ad`.
The first full exposition PDF inspection covered all 20 pages of
`exposition/exposition.pdf`, SHA-256
`cf3288fe05d1d52114b1fe0eedb089b8de595759a86a9f2144c67a7504f7480a`.
Its build manifest recorded exposition source
`a0cdf38f2134fa9ad028ab42aded4a0735e4b0f661705743c8b614dde8959287`.
These paths are relative to the external build directory
`/Users/willcook/src/_builds/quartic-r7/render`.

The PNGs were opened individually at their full 90-dpi page size (about
745 by 1053 pixels), not assessed from a contact sheet. The production owner
is `tools/render_papers.py` (Pandoc, Tectonic and the existing TikZ sources),
as documented in `tools/README.md`. No new visual was authored by this reviewer.
Expert page 3 and exposition page 9 were additionally rendered in grayscale
with Poppler and opened at the same size. Their arrows, zero cells and labels
remain distinguishable without hue.

The writer subsequently adjusted the expert figure and pagination, and the
parent is refreshing immutable source links. The all-page observations above
belong to the stated PDFs; later builds require the follow-up inspection
record below. At this source checkpoint the manuscript hashes were:

| Source | SHA-256 |
|---|---|
| `docs/expert_companion.md` | `1fc60226cd4b7dd786026fba5797550b5f44c9e6b87213c2f305fa20526f41ce` |
| `docs/exposition.md` | `81127194d3f1fe7ba58c20414856ab76b1503760c558fc335ae1206655be82a0` |
| `docs/reasoning_record.md` | `193f698b2a8383864b229e44df3f3fcce853aa23c9f489f2cf7c097f15f218af` |

The directly sampled Lean files had these hashes (paths below are under
`lean/QuarticQuery/`):

| Source | SHA-256 |
|---|---|
| `Statement.lean` | `21e9421899572827f8051a2747412792971b0415e45ade85e434219b9badaced` |
| `Upper/Tournament.lean` | `43df9db7997f88667de7a3cfa7d7c7751aa1f32c40e9de474895335bcdb87b7c` |
| `Upper/Amplify.lean` | `49e808cc6acbb47ad066b1dcf33ac8d47da2f28d88c51d537564e6591eb0d9e1` |
| `LowerBound/RealizedCaps.lean` | `395ba4cf6a76a5a5c60639ef09be43de2e723b8378335b2700c5f88af28b4861` |
| `Paper/ClassicalPlanted.lean` | `b86c310788efd04527ce9977e6f1cb660cd6b2b6825dcb151ab33f1b94497c2f` |
| `Forrelation/Circuit.lean` | `b17824d0a3b6ee5a689822b04c18d20de9e72e1db119105584e9cbba60ae8f01` |

## What can be reconstructed

The headline is the universal exponent `alphaTot = 4`. A fixed `k` supplies
a total family with randomized lower bound of order
`m^(2-1/k)/(log m)^2` and quantum upper bound
`C_k sqrt(m) (log m)^6`. Choosing `k` after a proposed exponent below four
excludes that exponent. The universal quartic upper bound gives equality.
This is a formalisation and exposition of OpenAI's separation, with a
separately explained reconstruction of the analytic Forrelation input; it is
not a priority claim for the separation.

The construction's two jobs are now distinguishable. Independent hard answers
hide the selected certificate among many cells in a randomly selected column.
Outward pointers let a real winner beat every rival cheaply, including rivals
whose address blocks violate their promises. Fractional comparison weights
produce a short list; exact local certificate tests turn that list into a
decision on every input. The lower bound couples a dummy zero-input to a
planted one-input and bounds discovery of either changed location.

The in-document answer appendix was encountered during the full sequential
read. No blinded human exercise test is claimed. To test transfer rather than
repeat printed answers, the reviewer used the following variant questions;
their particular numerical answers are not supplied in the manuscript's
answer appendix. Each was worked out from the exposition before comparing
with the relevant formal or record passage.

| Reader operation | Recovered answer and falsifier | Source check and disposition |
|---|---|---|
| Give an input with an all-one, off-promise candidate and decide totality. | Every assignment still has a Boolean answer. The candidate's true transcript has a false domain output; no address can make all tests pass. A second all-one column also prevents any winner, because an outward pointer cannot find its required zero. Totality does not require a decoder to decide the promise. | Exposition §2; expert §2; `Statement.lean::WinsAt` and `addressedF`. Reconstructed without inventing a promise on the total input. |
| Allow two losers to compare with probability exactly one half. Why does the winner survive? | Winner comparisons still satisfy `a[i*,j] >= 1-epsilon` because no rival pointer reaches a zero in the winner and the correctly decoded winner points to a rival zero. Pairing complementary probabilities gives half-drift without transitivity. Until selected, winner weight exceeds one half; a small expected total weight bounds the probability it remains unselected. | Expert §3.1–3.2; exposition §4; `Statement.lean::Tournament.IsComparison`; `Upper/Tournament.lean`. No fixed orientation or total-order hypothesis was silently added. |
| In the fractional example, choose pivot 3 rather than the printed pivot 2. Compute the next law. | The weights are `(1,1/3,0,3/5)`, total `29/15`; success has probability `29/60`; the conditional label law is `(15,5,0,9)/29`. If the next pivot is 4, the weights become `(1,1/4,0,0)`, giving conditional law `(4/5,1/5,0,0)`. Uniform selection among positive weights gives the wrong answer. | Fresh workspaces multiply probabilities, orthogonal labels add masses; `Upper/Tournament.lean::stageLaw_some` gives `weight/card`. `Upper/Amplify.lean::Samples.amplify` preserves the normalized successful-label law. These are abstract matrix calculations, not a claimed realisation by the Boolean board. |
| Stop immediately after listing a dominant candidate. Is acceptance justified? | No. Change the smallest-index all-one column's one outward pointer to a row containing one. Against that rival neither disqualifies the other, so the index tie-break still selects it; it beats the remaining rivals through correct pointers. A failed pointer test makes the total function zero. | Exposition §4 “A dominating column that does not win”; expert §3.3 and Appendix A. Verification is logically necessary, not merely error reduction for the tournament. |
| A tree guesses a cell without deliberately decoding an address. Where is the predictor's answer? | In the query position `B[i,s]` before its content is read. Fix `i` and the query time; simulate with independent outside data and a target-query cap, and output `s` at that proposed query. A correct visit implies correct prediction, while a lucky fallback can be correct without a visit. | Expert §4.4; exposition §5; record `CL-simulator`; `Paper/ClassicalPlanted.lean::avg_reachedCellAt_le` and `eq_21`. The one-way event inclusion and the averaging factor `1/m` explain why there is no extra factor `m`. |
| Move the XOR toy's cell query before its second target query, then perform that second query afterward. Does the cheap prefix make this a light-run event? | The simulator can predict at that prefix. The complete original run nevertheless exceeds `L=1`, so it is not in the joint nonheavy-and-visit event. If the original run stops at the cell, the new `a=0,b=0,c=d` event contributes `1/8`; together with the unchanged branch the event has probability `1/4`. | Record `CL-joint-event` and `CL-simulator-example`; exposition §5 and Question 3b. Lean bounds the prefix count by the complete path count using `List.take_sublist`; it does not identify prefix compliance with complete-run compliance. |
| Which fixed parameter excludes a proposed exponent 3.8? | `k=10` only excludes exponents strictly below 3.8. Take `k=11`, then let `m` tend to infinity. The ratio has positive power `2-1/11-3.8/2=1/110`; logarithms cannot keep it bounded. A growing `k` cannot be substituted in fixed-`k` estimates without uniform control. | Expert §6; exposition §6; `Statement.lean::UniversalPower` and `alphaTot`. Quantifier order and the direction of substituting the upper bound for `Q` are explicit. |

The numerical transfer checks were also recomputed using Python's exact
`Fraction` arithmetic and enumeration of the 16 XOR input tuples. This
confirmed the displayed values; it is a small arithmetic cross-check, not
formal verification of the general argument.

## Repairs, checked uncertainties, and reasons to retain material

1. **Repaired:** expert §3.2 contained the literal duplicated heading
   `*Ideal process.**Ideal process.*`. It was reported immediately to the
   expert writer and parent. The revised source and rendered expert page 7
   contain one correctly typeset heading.
2. **Repaired:** record `CL-simulator-example` had the broken join
   `at most \(1/2\),These last two probabilities` and repeated the same
   one-query XOR sentence later. It was reported to the record writer and
   parent. Source readback now begins the derivation with “These last two
   probabilities” and retains the final explanation of the `(1/2)^2` bound.
3. **Checked and retained:** exposition §3 says the selected exact circuit
   outputs `(0,0)` off promise. `CircuitRealises` alone has a weaker contract,
   so that declaration did not initially justify this sentence. Actual
   `Forrelation/Circuit.lean::finish` sets `b = not s1` and
   `d = b or (not s2 and not s3)`; the `vb` and `vd` equations in
   `forrCircuit_realises` therefore give `d=false => b=false`. Record
   `forr_final_signs` exposes the same construction as `b=p1`, `d=p1 or p0`.
   The stronger sentence is valid for the chosen circuit and should stay.
4. **Retain both tournament examples:** the concrete board demonstrates why
   off-promise rivals and a cycle are harmless; the abstract fractional
   matrix tests a genuinely different operation, sampling unequal weights.
   Calling the latter a realisation by the former would be false. The
   separation is now explicit in both short papers.
5. **Retain the local-test gate calculation:** checking gate 2 by reading
   its two predecessor values and its stored output explains why a test does
   not recompute the circuit. The separate topological induction explains
   why false predecessors cannot defeat the complete set of tests.
6. **Retain the three-budget paragraph and the XOR fallback calculation:**
   these remove two distinct temptations—using an expected cap and
   conditioning on lightness. The simulator's total cap `L` is stronger than
   the lemma's per-instance cap, while its unconditional success event is
   larger than the target joint event. Removing either distinction would
   shorten the account at the cost of its hardest lower-bound inference.
7. **Retain the fixed-`k` endpoint exercise:** it catches the tempting but
   wrong inference that `k=4` alone refutes a power-3.5 inequality. No extra
   growing-parameter analysis is needed to prove `alphaTot=4`.

One attempted simplification was to replace the capped simulator paragraph
with “a light column cannot reveal all its address bits.” That sentence is
not an adequate proof: the query can guess rather than learn, lightness is
an event about the original complete run, and conditional success on that
event can be one. The existing predictor construction is the economical
correct explanation and is retained.

## Primary-source writing comparison

The relevant comparison is how the sources expose the same hard inference,
not whether the manuscripts resemble a named author's style.

- [Drucker, arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2), §3,
  Lemmas 3.1–3.2: the first lemma defines the best remaining success
  probability and proves its average cannot increase after a query; the
  second separately proves product structure after a transcript. The
  exposition's proof box now supplies both steps. The expert's unnormalised
  value recursion is a concise alternative that avoids null-history
  conditioning. Retain the two treatments for their different readers.
- [Brassard–Høyer–Mosca–Tapp, arXiv:quant-ph/0005055v1](https://arxiv.org/pdf/quant-ph/0005055v1),
  §2, Lemma 1 and equation (8): the two-dimensional invariant subspace
  identifies the unchanged successful direction. The exposition uses that
  direction to explain preservation of the label law, rather than only
  quoting a search cost. Its discussion of the fixed cutoff then addresses
  the all-branch cap needed here; the expert identifies the expected-cost
  QSearch theorem separately. This is an explanatory use of the source,
  not a claim that bounded search is new.

These two primary sources were opened for the passages named above. This
review did not independently re-audit every bibliographic attribution or
the Forrelation analytic lower bound. The specialist audit files own those
broader checks.

## Render observations and final scope

All equations and table cells in the inspected short-paper pages were
readable, with no observed clipping, missing mathematical glyphs, overlapping
text, or broken visible reference marker. The expert's Appendix A table fits
on page 15. All rendered bibliography entries were visually inspected
(expert pages 13–14, exposition pages 18–20); this is a formatting inspection,
not verification of every entry's metadata. Both PDFs include their AI-use
disclosures. The exposition has a full-page tournament figure; its empty
space is a layout choice, not missing argument.

The revised figure 3's pointer labels show the winning forward pointers;
the preceding text changes the reverse pointers so that they miss. Checking
both directions recovers the cycle `2 beats 3 beats 4 beats 2`. The added
label and caption make that relationship explicit; no graph correction is
required. Figure 4 reveals the selected column and address to the reader
only. It does not claim that the algorithm is given either one.

Coverage: short-paper sources and inspected PDFs **assessed in full**;
record amplification, tournament sampling, final circuit outputs,
simulator, joint event and XOR trace **assessed at the named passages**;
Lean definitions and selected implementation lemmas **sampled directly**;
analytic Forrelation proof, universal quartic proof, all other record
sections, complete Lean dependency closure and fresh formal execution
**unassessed by this review**. The printed answers are explanations, not
observations of learners. No result here establishes human comprehension or
community acceptance.

The mathematical conclusion and the two principal reductions are now
reconstructible at their stated scopes. The remaining release action for
this audit is to bind and inspect the final rerender after link/bibliography
refresh, rather than treating an earlier PDF's inspection as transferable.

### Final-rerender follow-up

Pending the parent's stable-output signal; only the exact earlier editions
above are covered by the all-page inspection at this checkpoint.
