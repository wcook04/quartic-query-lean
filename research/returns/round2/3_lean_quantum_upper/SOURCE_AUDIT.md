# Sources, attribution and the exact claims they support

The Section 3 mathematics is attributed to the supplied OpenAI preprint.
The new contribution here is proposed formal statement coverage, interface
construction and explanation. No claim of a new quantum algorithm, a new
amplitude-amplification principle, or priority over the cited literature is made.

## Primary content source

**[OAI] OpenAI. _A Nearly Quartic Separation Between Randomized and Quantum
Query Complexity_, 5 October 2026.** The source read for mathematical content
was the attached `paper/extracted.md`, Section 3, with the attached PDF available
for reference. Its public location is
[the official OpenAI repository PDF](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).
The public GitHub metadata resolved during this review; the public PDF endpoint
did not independently supply parseable mathematical content to the web reader.
Accordingly, content claims use the supplied paper, and no independent public
PDF comparison is claimed.

The relevant paper locations are Section 3.1 and Lemma 3.1 for bounded
amplification; Section 3.2 and Proposition 3.2 for the comparison tournament;
equations (10), (11), (13) and (15) for complementarity, dominance, drift and
the full preparation state; and Section 3.3 for decoding, comparison,
verification and the final error. The exact extracted source lines are retained
per statement in `coverage_plan.json`.

## Citations needed in the mathematical exposition

| Citation | Exact role | Locator used |
| --- | --- | --- |
| **[BHMT]** Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp. _Quantum Amplitude Amplification and Estimation_. arXiv:quant-ph/0005055, v1 (2000). | Two-dimensional amplitude-amplification dynamics and preservation of the good component up to a phase. | Section 2, Lemma 1; equation (8), printed pp. 5–7 in the inspected version. [Primary text](https://arxiv.org/html/quant-ph/0005055v1). |
| **[BBHT]** Michel Boyer, Gilles Brassard, Peter Høyer and Alain Tapp. _Tight bounds on quantum searching_. arXiv:quant-ph/9605034, v1 (1996). | Exact average over a uniformly selected Grover iteration count. This supports the estimate used for equation (9). | Section 4, Lemma 2, printed p. 3 of v1. [Primary PDF](https://arxiv.org/pdf/quant-ph/9605034v1). |
| **[Grover]** Lov K. Grover. _A fast quantum mechanical algorithm for database search_. arXiv:quant-ph/9605043 (1996). | Historical credit for quantum search, if the background paragraph introduces it. The exact finite-trial proof here is supported by the more specific sources above and the supplied preprint. | Original algorithm and [primary record](https://arxiv.org/abs/quant-ph/9605043). |

In the averaging formula of BBHT Lemma 2, the oscillatory correction has
denominator `4 M sin(2θ)`. The weaker lower estimate used in the supplied
preprint's equation (9) follows from that identity in its stated parameter
range. The preprint's mixture includes a zero-iteration branch, which handles
the high-success regime separately. The fixed number of repeated trials and
the explicit charged-product estimate are derived in the supplied argument
and proposed source; the table does not attribute those exact constants to
BBHT or BHMT.

BHMT Theorem 3 addresses expected running time for unknown success probability,
and its stated procedure runs forever when the initial success probability is
zero. Section 3 here needs a finite branch cap, defined even on zero-success
inputs. Cite BHMT for the amplitude dynamics and the appropriate prior method;
cite the supplied Lemma 3.1 and its proof for the bounded procedure used here.
The normalized good-state statement must retain its global-phase qualification,
and conditioning is used only on a positive event.

## Related work checked for possible substitutions

The following papers clarify why superficially similar search results do not
automatically supply the exact theorem required here. These are comparisons of
hypotheses and conclusions, not assertions of novelty or impossibility.

**[HMW] Peter Høyer, Michele Mosca and Ronald de Wolf. _Quantum Search on
Bounded-Error Inputs_. arXiv:quant-ph/0304052, v2 (2003).** Section 3, after
Facts 1 and 2, assumes that every Boolean input predicate is computed by a
unitary with success probability at least 9/10. See
[the primary text](https://arxiv.org/html/quant-ph/0304052v2).
In the tournament, the nonwinner-versus-nonwinner probabilities can be arbitrary
fractional values, including values near one half; only the dominant candidate
has the required one-sided advantage against every other candidate. The
inference is that HMW's theorem cannot be substituted merely by treating all
comparisons as bounded-error evaluations of a hidden deterministic ordering.
It remains useful background for coherent search using imperfect subroutines.

**[Montanaro] Ashley Montanaro. _Quantum search with advice_. arXiv:0908.3066
(2009), author PDF dated 14 September 2009.** The abstract and Sections 1 and
1.2 define query complexity averaged over an advice distribution. See
[the author PDF](https://people.maths.bris.ac.uk/~csxam/papers/advice.pdf) and
[the arXiv record](https://arxiv.org/abs/0908.3066).
The present theorem requires a fixed worst-case branch cap for each oracle
input. The inference is that an advice-distribution expected-cost guarantee
does not establish that cap without another argument. No uncertain constants
from secondary annex metadata are used here.

**[DH] Christoph Dürr and Peter Høyer. _A Quantum Algorithm for Finding the
Minimum_. arXiv:quant-ph/9607014 (1996).** The
[primary record](https://arxiv.org/abs/quant-ph/9607014) concerns finding a
minimum in a table of values. The fractional comparisons permitted here need
not arise from such a total order. This is a hypothesis mismatch relevant to
direct substitution. It is not a claim that minimum-finding ideas are unrelated
to the proof.

**[de Wolf] Ronald de Wolf. _Quantum Computing: Lecture Notes_.
arXiv:1907.09415, public record checked at v6 (27 August 2026).**
[Primary record](https://arxiv.org/abs/1907.09415).
These notes are background for the query model and coherent simulation.
The detailed statements in this package use the supplied model declarations
and exact primary references above. The full lecture notes were not audited.

## Lean source credit and statement evidence

The supplied `Amplification/Geometry.lean` header credits an adaptation of
Troy Lee's `Quantum/Amplitude/Geometry.lean`. The supplied
`Amplification/Average.lean` header credits an adaptation of Troy Lee's
`Quantum/Amplitude/TrigSum.lean`. The accepted adjudication F-CODE-PROV records
these as adapted proofs, not imported external modules. That is the precise
provenance claim retained here. The external original files were not independently
audited in this review.

The following supplied findings govern the proposed changes:

| Finding | Consequence for this package |
| --- | --- |
| `F-TOURN` | An actual finite bounded-list `Samples` output is supplied for Proposition 3.2. The existing Boolean continuation is retained for the final decision theorem. |
| `F-STAGE-LAW` | The full tensor state has its own construction. The existing short-circuit stage is used only for the successful-law statement it actually proves. |
| `F-CODE-PROV` | The Troy Lee adaptation credit is preserved. |
| `F-EXACT-REACH` | Source presence, compilation, reviewed correspondence and headline reach remain distinct statuses. |
| `M-1` | Amplification parameters and the procedure are selected before the preparation or oracle input. |

Primary Lean support is named by full declaration in `coverage_plan.json` and
`blueprint.md`. These names refer to supplied source or proposed source, with
their status stated separately. Public current API documentation consulted for
some list operations was a source-name check; it was not verification against
the pinned compiler or Mathlib revision.

## Audit limits

The literature checks cover the precise hypotheses used above. They are not a
complete novelty or priority search for all weighted tournaments. The supplied
paper's Section 3 and relevant Lean source were inspected; lower-bound sections,
unrelated prior-round proposals and external calibration manuscripts were not
reviewed in full. The statement-by-statement and team reading scopes are in
`READ_SCOPE.json`.

All external retrievals in this review were read-only. No mailbox, account,
credential request, repository publication or original-source modification was
used. Public-source checks were made on 2 November 2026.

