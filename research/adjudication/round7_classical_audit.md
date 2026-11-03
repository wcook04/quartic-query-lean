# Round seven: classical lower-bound audit

Prepared 3 November 2026. This is an independent AI audit of the classical
argument and its literature interfaces. Submitted review scores are not evidence
of correctness. The original returns remain unchanged; no returned program was
executed. This audit does not report a fresh Lean build or Comparator run.

## Scope and conclusion

The detailed classical proof in the reviewed record is sound at the level checked
here. Its generic statement is

\[
m=4^t,\quad t\ge1,\quad r=40t,\quad
1\le L\le m,\quad L<R(P)
\quad\Longrightarrow\quad
R(F_{P,C,m})>\left\lfloor mL/100\right\rfloor,
\]

for every finite-coordinate partial Boolean function and every circuit realizing
its domain and value. Circuit size does not enter this lower bound. The same
circuit can therefore be the efficient one needed by the quantum upper bound.

The main corrections are to probability claims in summaries, a toy-instance
caveat, an exercise's endpoint logic, and the description of a predecessor's
pointer condition. None supplies a counterexample to the separation theorem.

The audit used the lower-bound return's complete structured finding and method
registers, its classical reading notes and literature comparisons, and the
cross-panel findings listed below. The source proof inspection covers record
§6, its minimax and direct-product interfaces, the fixed-parameter argument and
§7.3, companion §4, and exposition §5 and the exponent exercises. The Forrelation
acceptance bridge was checked at record (F41)–(F42); a separate audit owns the
full analytic and quantum arguments. Round-six fidelity and literature records
were read as historical context, with current source taking precedence.

## Decisions on submitted findings

IDs below refer to `LS` in the lower-bound return, `QS` in the quantum return,
`NR` in the newcomer return and `EF` in the editors return. A keep is an explicit
decision to preserve an established invariant, not an assertion that every
surrounding sentence needs no revision.

| Decision | Exact findings | Reason and required action |
| --- | --- | --- |
| Accept correction | LS001, LS061; QS003 | Replace pathwise address-learning necessity with the expensive-column/lucky-guess argument under the planted law. A successful execution can guess cheaply. |
| Accept correction | LS114; EF143 | A fixed column and fixed time give a joint bound by \((2/3)^r\). An any-time hit needs the union factor \(G\), and lightness stays inside the event. |
| Accept clarification | LS010; QS014 | The target zero is the zero in the independently selected hidden column. Finding an arbitrary zero is a different task. |
| Accept correction | LS036; QS054 | Residual uniformity applies before the first discovery in that column. Repeated reads give no new discovery. |
| Accept correction | LS093; QS252, EF128 | Condition on the observed transcript prefix before the next query, including all relevant past field queries. A completed transcript can already determine the event being predicted. |
| Accept correction | LS091; QS251, EF126 | At \(m=4\), opposite-valued promised inputs give a hard law for \(L=0\). The missing ingredient is a useful positive budget for the lower-bound application, including division by \(L\). |
| Accept correction | LS112 | \(k=4\) proves \(\alpha_{\rm tot}\ge3.5\), since it excludes every smaller exponent. It does not exclude the universal bound at the endpoint exponent \(3.5\). |
| Accept correction | LS105 | \(k=2\) gives polynomial threshold three with logarithmic losses; it does not establish or refute an endpoint cubic relation. |
| Accept correction | LS110 | Failed local tests are deterministic facts; the capped search verifier may miss a failed test. Exact toy decoders do not make the whole verification pipeline exact. |
| Accept clarification | LS096, LS104 | State \(1\le L\le m\) before dividing by \(L\); verify the second floor's positive range separately. |
| Accept correction | LS012 | ABBLSS require the highlighted zero in each nonmarked column to point back. Arbitrary other zeros need not do so. |
| Accept clarification | LS070, LS153 | Credit the earlier direct-pointer proposal together with its exponential-alphabet objection. Explain the present access to one indexed pointer field at its Boolean bit cost. |
| Accept bibliographic correction | LS204 | Match the CCC 2003 DOI to *Quantum query complexity and semi-definite programming*. The earlier manuscript title is a different edition. |
| Accept clarification | LS016; QS013, QS024 | Coordinates of the total function are separate and unconstrained. Probabilistic independence belongs to the sampled hard experiment. |
| Accept presentation repair | LS027, LS029, LS039, LS042, LS089, LS099, LS100, LS102, LS103, LS111, LS162, LS167, LS171, LS172, LS174, LS176, LS179, LS183, LS185, LS188, LS189 | Expose the generic theorem, one-factor update, common hard law, sampling dependencies, simulator trace, default-output inclusion, time union and column average. Preserve the full proofs while making their consumed interface explicit. |
| Accept navigation repair | LS115, LS118, LS155, LS161, LS201, LS202, LS203, LS210, LS212; NR154, NR156; EF146, EF209, EF210 | Update visible destination topics as well as link targets. Scope the fixed-\(k\) warning to its actual argument; §7.3 already supplies a uniform schedule. |
| Accept explanation | LS047, LS048 | The analytic law need not be promise-supported. Display the positive signal, uniform leakage and amplified error in (F42), and distinguish that law from the promise-supported minimax law. |
| Accept explanation | LS051, LS193, LS194, LS195; QS149, EF202 | Motivate the schedule from \(40k+\ell/k\). Its initial validity range need not give a useful positive exponent. Use a conservative constant for its mathematics, not to explain editorial synchronization. |
| Accept keep | LS011, LS017, LS028, LS030, LS031, LS038, LS040, LS041, LS044, LS046, LS048, LS050, LS055, LS056, LS057 | Preserve the predictor-from-query-position reduction, same circuit, strict minimax premise, accurate antecedents, correct budget levels and joint-event interpretation. For LS056 call \(\beta\) a success bound; toy values may be exact optima. |
| Accept keep | LS092, LS094, LS095, LS097, LS098, LS101, LS106 | Preserve dummy-run counting, the independence control, guessing, posterior-value example, conditional-event counterexample, three-budget explanation and fixed-parameter quantifier example. |
| Accept keep | LS116, LS137, LS141, LS145, LS150, LS160, LS163, LS164, LS165, LS166, LS169, LS170, LS173, LS175, LS177, LS178, LS180, LS182, LS184, LS186, LS190, LS192, LS196, LS213, LS214 | Preserve the mathematically necessary hypotheses and the accurate limits of each endpoint and proof route. |
| Accept independent explanatory calculation | NR190 | The simulator's \(1/8\) and \(1/4\) probabilities have the short derivation below; exhaustive zero-location enumeration need not carry this inference. |
| Accept as optional context | LS032 | Ben-David–Blais is relevant current direct-product literature. Its expected-cost maximum-distributional measure is not the fixed-law hard-cap premise here, so it is not a required replacement theorem. |
| Accept reallocation; decline expansion | LS037, LS052 | Moving optional constant details out of the short proof is justified. A stronger search theorem, a useful first numerical exponent and optimized constants are unnecessary for this revision. Preserve the true optional argument and its limits. |

Other lower-panel analytic, quantum, visual and register findings are outside this
audit's decision scope; the table is not a blanket rejection or approval of them.
No classical mathematical error finding listed above was rejected. Optional
editorial choices are distinguished from corrections required for truth.

## Checked proof interfaces

### One law, then independent copies

The premise \(L<R(P)\) concerns randomized algorithms with success at least
\(2/3\) on every promised input and a cap on every execution. Finitely many
depth-\(L\) trees give a compact convex hull of success vectors. It is disjoint
from \([2/3,\infty)^D\), and the record's nearest-point separation gives a
nonnegative normal vector and hence one promise-supported law \(\mu\) defeating
all those trees, with a strict common margin. This justifies choosing the law
before sampling the address inputs. The rounded Gaussian-chain law used to
prove Forrelation hardness is not substituted for \(\mu\).

### Adaptivity and separate caps

After fixing jointly independent side information and coins, an actual transcript
prefix is a product of local consistency events. Thus its posterior is a product
across whole input instances, although bits within an instance may be dependent.
The continuation value for instance \(h\) uses its posterior and its remaining
allowance \(L-q_h\). One query changes only that instance's factor. Factoring out
the other nonnegative factors proves the product inequality; an arbitrary
product of supermartingales would not suffice.

The weighted proof is the same calculation without posterior normalization. The
record's identity relating transcript mass times normalized potential to the
product of unnormalized values is correct. For an initially uncapped algorithm,
truncation before the first over-cap query contains the original event
`correct and compliant` in the capped algorithm's success event. It does not
justify success conditional on compliance.

The three relevant budgets must remain distinct: original total \(G\),
simulator total \(L\) in one column, and separate per-instance \(L\) caps. The
simulator's total cap implies every separate cap. A pooled cap \(rL\) does not.

### Planting and discovery

The dummy law samples all zero locations and address inputs independently and
uses fixed all-zero cells. An independent uniform \(I\) selects the planted
column. All right-hand events in the first-difference bound concern the dummy
run. Counting every selected-cell visit safely overcounts visits to changed
bits, because some filled bits remain zero.

If \(Z\) counts distinct discovered columns, averaging over \(I\) gives
\(\Pr[\text{selected zero hit}]=\mathbb EZ/m\). The query-prefix argument gives
the early-discovery probability at most \(2/m\), and at most \(2G/m\) late
columns can have received \(m/2\) reads. This proves \(4G/m^2\). The two optional
search proofs giving \(2G/m^2\) and \(2G/[m(m+1)]\) are also valid at their
stated scope; the latter is an expectation-cost charging refinement, not an
optimal worst-case success curve.

### Predicting a proposed address

For fixed \(i,q\), the simulator receives zero locations, other columns and
blank cells as free data, all jointly independent of the target tuple. Knowing
\(J_i\) is harmless: its target is the vector of partial-function values, not
the erased zero. It stops before target query \(L+1\), and at slot \(q\) outputs
the cell address encoded by the proposed coordinate before reading its bit.
Abort and irrelevant slots receive a fixed output, so it remains a total capped
predictor. Correct defaults merely enlarge success.

The event `column i light and slot q visits its true cell` is contained in
predictor success, hence has probability at most \(\beta^r\). A time union and
column average give

\[
\frac1m\sum_{i=1}^m\sum_{q=1}^G
\Pr[i\text{ light and slot }q\text{ hits its true cell}]
\le G\beta^r.
\]

Together with the heavy-column bound, this yields the three discrepancy terms
\(4G/m^2+G/(mL)+G\beta^r\). Since \(r=40t\),
\((2/3)^r\le m^{-10}\); with \(G\le mL/100\le m^2/100\), the sum is at most
\(6/100<1/3\). Correctness would instead give acceptance at least \(2/3\) on
the planted support and at most \(1/3\) on the dummy support. Averaging over
coins preserves both comparisons, giving the contradiction.

### The small simulator calculation

In the existing XOR toy write the target inputs as \((a,b)\) and \((c,d)\),
with four independent fair bits. On \(a=1\) the original tree remains light
and proposes address \(10\). This address is true exactly when \(b=0\) and
\(c=d\), so the joint light-and-hit probability is \(1/8\). On \(a=0\) the
predictor truncates and defaults to \(00\); it succeeds when \(b=0,c=d\),
adding \(1/8\). Thus predictor success is \(1/4=(1/2)^2\). A separate 16-tuple
enumeration written during this audit confirms these fractions; no returned
checker was run.

### Floors, exponents and a growing parameter

For \(k\ge2,t\ge8\), \(4t^2\le2^t\le m^{1-1/k}\). Therefore the unfloored
hardness scale is at least one, its floor loses at most a factor two, and
\(mL\ge4^8\ge200\) permits the second floor with another factor two. This
gives the displayed coefficient \(1/400\). For each fixed \(k\), the resulting
ratio diverges for \(\alpha<4-2/k\), and the choice is made in the order
\(\alpha\), fixed \(k\), constants and threshold, then \(m\to\infty\).

The current growing-\(k\) calculation uses uniform estimates, rather than
substitution into a fixed-parameter eventual claim. Its loss contains
\(40k+\ell/k\), balanced near \(\sqrt{\ell/40}\). For
\(k=\lfloor\sqrt{t/20}\rfloor\), the displayed rounding identity gives an
additional loss less than 20; the ensuing bound actually permits 474 in place
of 508, so 508 is conservative. At \(t=80\), its displayed epsilon is about
7.73767: the inequality is valid but uninformative there because the exponent
is negative and \(Q,R\ge1\). The asymptotic approach to four is the useful
conclusion; \(R=\Omega(Q^4)\) is not established.

## Primary literature checked independently

- [Drucker, arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2): Theorem 1.1,
  partial-function extension at the end of §1.2, conditional-value and posterior
  arguments in §3, and its final fair-algorithm specialization. Substitution of
  source copy count \(r\), \(T=L\), error \(1/3\) and \(\alpha=3/r\) gives total
  budget \(L\) and success at most \(2(2/3)^r\). The extra factor is absorbed by
  the numerical slack. This is a valid alternative to the exact separate-cap
  bound, not an inapplicable theorem.
- [Shaltiel, ECCC TR01-009](https://eccc.weizmann.ac.il/report/2001/009/download):
  definition of fairness and §5's XOR-advantage result. The historical
  attribution should preserve the uniform-input and XOR target conventions;
  Drucker supplies the directly relevant product formulation and proof route.
- [Ambainis et al., arXiv:1506.04719v3](https://arxiv.org/pdf/1506.04719v3): §1.3,
  especially the highlighted-zero back pointers and the discussion of replacing
  the tree by direct pointers. Arbitrary zeros may point elsewhere. Treating all
  outgoing pointers as one alphabet symbol causes the stated exponential
  alphabet obstruction; the present selected-field access must retain bit cost.
- [Aaronson–Ben-David–Kothari, arXiv:1511.01937v2](https://arxiv.org/pdf/1511.01937v2):
  cheat-sheet construction and certificate motivation, used for the mechanism
  comparison rather than a claim that the present function is the same one.
- [Ben-David, arXiv:1506.08106v1](https://arxiv.org/pdf/1506.08106): §5.1 uses a
  random marked zero among independently placed column zeros; §5.2 compares an
  empty array with one valid cheat-sheet cell and extracts prospective addresses
  from the queried cells. These directly support the local predecessor credit
  for the two hiding mechanisms, without identifying the resulting functions.
- [Ben-David–Blais, arXiv:2512.08268v1](https://arxiv.org/html/2512.08268v1):
  metadata, introduction and §2.3. The paper is marked FOCS 2025 and uses maximum
  distributional expected query cost. It is relevant context with a distinct
  interface, not a missing premise of this proof.
- [Bansal–Sinha, arXiv:2008.07003v3](https://arxiv.org/pdf/2008.07003v3): §3,
  especially Figure 1, supplies the Gaussian-pair chain, shifted product and
  rounding by coordinate means. The revised companion correctly identifies its
  changed algebraic truncation and reproves the required moments.
- [Girish–Tal–Wu, CCC 2021](https://drops.dagstuhl.de/storage/00lipics/lipics-vol200-ccc2021/LIPIcs.CCC.2021.39/LIPIcs.CCC.2021.39.pdf):
  §1.3 and Lemma 9, printed p. 39:8, give the ordinary-tree martingale increment
  and coefficient contraction induction. Footnote 2 specifies stopping instead
  of conditioning on the good event. This supports the revised local method
  attribution; it does not attribute the record's explicit bounded-bias
  derivative constants to the cited lemma.
- [Rutgers' BSS proceedings record](https://www.researchwithrutgers.org/en/publications/quantum-query-complexity-and-semi-definite-programming/):
  the CCC 2003 title, pages and DOI agree with LS204's proposed repair. This is
  bibliographic verification, not inspection of the original BSS proof.

## Formal evidence boundary

Source inspection confirms the unnormalized direct product in
`lean/QuarticQuery/LowerBound/DirectProduct.lean`, clipping and realized compliance
in `RealizedCaps.lean`, the finite external-seed wrapper in
`RealizedCapsExternal.lean`, minimax in `Minimax.lean`, and the planted simulator
and lower bound in `LowerBound/Planted/`. The wrapper bounds joint success and
recursive compliance for initially uncapped trees. Identifying recursive
compliance with observed per-input counts and reducing arbitrary independent
randomness to finitely many behaviors remain ordinary arguments at the scope
the record states.

The recorded realized-caps external receipt
`comparator-round4-realized-caps-external-2026-11-03T023317151864+0000.json` and the
headline receipt `comparator-Unconditional-2026-11-03T121735042729+0000.json` both
report passes. On 3 November this audit recomputed all 13 bound source hashes in
each receipt under `LowerBound/` and `Statement.lean`; all matched. This is a
source-binding check of recorded evidence, not a new proof build or comparison.

## Method consequences

Accept lower-panel M01, M03, M08, M10, M11, M12, M13 and M14 for the existing
method owners: summary edits must preserve the exact event, time scope,
conditioning, budget modality and quantifier order; adapted gadgets need source
quantifiers and access costs; negative scope statements and exercise answers are
claim-bearing occurrences. A toy failing a useful positive-budget hypothesis
does not imply nonexistence of its hard law. An infimum goal and exclusion of an
endpoint inequality need separate checks. Require an executed central reduction
and its exceptional branch when peripheral examples do not teach that transition.

Accept M02's semantic-route lesson, and M04/M16's warning against treating a
functional list or an indispensable budget paragraph as a style-detector error.
These refine existing rules; they do not justify more universal checklists or
rewriting a mathematically accurate paragraph without a specific reader benefit.

## Final revision binding

Manuscripts were being revised concurrently while this audit was prepared. The
following bytes have received a final targeted reread; the hashes identify the
scope independently of any later rendering or link-rebinding changes.

| Source | SHA-256 | Final reread scope and result |
| --- | --- | --- |
| `docs/expert_companion.md` | `1fc60226cd4b7dd786026fba5797550b5f44c9e6b87213c2f305fa20526f41ce` | Classical overview and attribution, §§4–6, formal direct-product description and cap counterexamples pass. In particular (12) is joint and fixed-time; the column average and time union are explicit; the off-promise comparison includes the pointwise bridge and signal/error/leakage inequality, with depth and error ranges. |
| `docs/exposition.md` | `81127194d3f1fe7ba58c20414856ab76b1503760c558fc335ae1206655be82a0` | Introduction's one-sided bounds and expensive/guess dichotomy, §5's minimax, first-difference, prefix, caps and simulator, §6's fixed-parameter quantifiers, and Questions/Answers 2–5 pass. The final prefix paragraph expressly restricts new discoveries and excludes repeats; the toy caveat concerns its zero budget, not nonexistence of a hard law. |
| `docs/reasoning_record.md` | `193f698b2a8383864b229e44df3f3fcce853aa23c9f489f2cf7c097f15f218af` | Opening and §6 overview joint scopes, changed classical proof interfaces, simulator probabilities, finite tail, fixed-parameter quantifiers, §7.3 arithmetic, catalogue scope and BSS edition correction pass. The earlier full §6 inspection remains the proof basis; this reread specifically checks the revisions and their propagation. |

The independent checks in this audit also recomputed the adaptive AND example:
8 of 16 tuples comply, 5 comply and succeed, and conditional success is 5/8.
The new exposition exercise distinguishes a cell query reached before truncation
from whole-run lightness: a later excess target query still makes that run heavy.
Its answer and the revised endpoint exercise were checked against their exact
questions, rather than only against a sufficient parameter recipe.

A later automated source-link rebind changes these hashes. It may be rebound to
this audit only after inspecting that diff and confirming the mathematical text
and exercised destinations retain the meanings checked here.
