# Revision by the purpose of each paper

Baseline: `8195cc0`, 4 November 2026. The [intake](paper_purpose_intake.json)
preserves the four supplied conversations. Their repeated numerical ratings
are editorial opinions, not a measurement of mathematical quality or reader
learning. The requested deliverables are improved papers and a reusable account
of what makes each of the three paper types good.

## Decisions

The specialist paper must make the decisive proof ideas assessable without
requiring the long record to supply its intellectual centre. The exposition
must equip its stated reader to perform the central operations and connect them
into the theorem. The complete record must make every promised inference
recoverable along a coherent main route and at individual proof destinations.
The shared mathematical result and evidence boundary remain unchanged.

One repeated expert criticism is rejected on the current mathematical source.
The schedule in expert Appendix E and record §7.3 is
`k = floor(sqrt(t/20))`, not `floor(sqrt(t)/20)`. At `t = 80`, the former
is exactly 2. For all `t >= 80`, writing `x = sqrt(t/20) >= 2` gives
`15k + 2 <= 15x + 2 <= 16x <= 8x² <= 40x² = 2t`; the other
condition `t >= 32` also holds. Raising the stated threshold to 1600 would
answer an extraction-induced misreading, not repair the actual formula.
The finite exponent bound need not be informative at its admissible starting
point; the record already distinguishes that from its asymptotic conclusion.

## Shared writing method

The authoritative reusable guidance belongs in `wcook04/lean-exposition`,
`docs/authoring.md`, with the stage-specific skills and `docs/reader-review.md`
as consumers. The refinement defines the three paper purposes and their
success conditions, then requires a whole-paper judgment before release.
It addresses the failure that a sequence of correct local repairs can leave
the argument's emphasis and reading order unsatisfactory.

Transfer was checked by applying the purposes to weighted averaging and
induction: normalized weights and their extremal inequalities call for a
different expert, teaching and complete-proof treatment; the odd-number
identity likewise distinguishes the decisive induction step, teaching the
operation, and supplying the full quantified argument. Correct finite examples
do not replace either general proof. Expert fluency is an exception to imposing
remedial examples. These are author-executed transfer checks, not observed
human learning.

This pass is source-assisted author/agent revision. Neither the writer nor the
receiving review is described as a blind human reading. Lean source changes,
a new Lean build, external mathematical refereeing and a verified perfect score
are not claimed. Validation and the final edition are recorded separately after
rendering and inspection.

## Receiving inspection corrections

The first rendered record exposed three presentation defects: a retained
`samepage` wrapper around the expanded planting overview left a large blank
area, the first floated figure interrupted its following paragraph across
pages, and the four-row OR table split across pages. The first readback also
found §3.3 still naming Appendix B for references after that appendix had
become alternative classical arguments. These are repaired in the source and
checked in the successor PDF. Literal `BansalSinha2021` citation labels are
replaced with readable author names.

A second proposed mathematical correction is also declined: nested search on
this board gives quantum cost about m against classical cost m^(2-1/k), not
a nearly cubic separation. The nearly cubic ceiling belongs to a different,
balanced AND–OR cheat-sheet recipe. The revised papers distinguish these
comparisons.

## Substantive changes and whole-paper review

**Specialist companion.** The opening now explains the avoided nested-search
product. The exact circuit is given by the contract the proof needs, with its
full arithmetic available in the record. Winner dominance is visible beside
the construction. The algorithm precedes the potential argument, and the direct
product appears when a true-cell visit is turned into an address prediction.
The new mathematical conclusion joins the two uses of the same certificate.
A specialist can recover both reductions locally; the index and record support
the omitted suppliers without supplying the paper's central idea.

**Exposition.** The opening gives the actual four-column strings and the
certificate problem before the Walsh machinery. Its examples form a common
base board with separately declared changes. Sampling's joint mass is derived
before reversible-register mechanics. Reflection matrices and secondary
classical examples remain in appendices. The classical contradiction now leads
directly to the exponent calculation and a return to the board. The reader
route teaches what address, pointer, candidate and certificate each do; the
worked changed cases test distinct implications rather than relabelling an
abstract lemma. This is source-assisted agent assessment, not a recorded
human attempt.

**Complete record.** The construction precedes the formal quantifiers, while
the exact models remain in the main route. Existing construction and planting
figures are reused. One full direct-product proof remains in the classical
argument; alternative proofs and search refinements move to Appendix B with
their stable destinations. The analytic chapter states its uniform theorem,
explains its three proof movements and derives the two-block derivative step
before the three-block iteration. A mathematical conclusion follows the
universal bound; references follow the technical appendices. The complete
main argument and individual proof-entry routes were checked separately.

Rejected additions include another master reduction theorem, extra explanatory
boxes and wholesale renumbering. The exact sampling law, finite caps, independent
side information and off-promise qualifications remain because they explain
necessary inferences. The analytic martingale argument remains demanding; the
new entry calculation does not establish unassisted comprehension of that
whole proof by a new reader.

The shared refinement is merged at `fda2bbe499329247b7d5c58c9aa8764e9ce2d8c7`
in [lean-exposition PR 48](https://github.com/wcook04/lean-exposition/pull/48).
Both its local and fresh-clone suites ran 710 tests with two skips and no
failures; hosted CI passed. Installation, minimal CLI use, links and working
and staged layout checks also passed.

## Accumulated feedback and paper deliverables

The supplied three review conversations each contain successive assessments and
a final editorial brief. Their diagnoses, proposed remedies and later corrections
are preserved in the intake, rather than replaced by the following synthesis.
The context conversation preserves earlier review and writing-method history.

| Recurrent diagnosis | General deliverable | Application in this edition |
| --- | --- | --- |
| Specialist paper defends every detail with nearly equal emphasis | An independently assessable decisive argument | Expose the nested-search cost and place the algorithm before its analysis; retain exact supplier contracts. |
| Definitions arrive before the problem they solve | A motivated construction whose objects have identifiable uses | Put the board and its certificate problem before the exposition's Walsh calculation. |
| Many examples do not yet form one explanation | Command of the operation and a controlled changed case | Reuse a base board and distinguish its mutations; derive the sampling law before register details. |
| Complete facts are difficult to read continuously | Both a main proof route and usable individual proof destinations | Construction before quantifiers; one direct-product proof on the main route; alternative arguments in an appendix. |
| The analytic chapter reads as consecutive obligations | A recoverable multi-stage mathematical proof | State the uniform endpoint, explain its three movements, and show the two-block derivative before iteration. |
| Conclusions stop with technical or administrative details | A mathematical resolution of the opening question | Join the certificate's two roles and distinguish the fixed-parameter argument from its uniform refinement. |
| Local fixes accumulate instead of improving the document | Selection by audience, dependency and explanatory importance | Decline a new master theorem, arbitrary quotas and renumbering; relocate secondary material without losing proofs. |
| Rhetorical fluency hides objects or invents vocabulary | Literature-grounded prose with stable standard terminology | Apply the existing register stage and humanizer after mathematical editing; compare actual passages, not an annex inventory. |

These are outcomes of the reading document, not mandatory headings or additional
printed checklists. The shared authoring owner now includes a per-type account
of what opening, main argument and ending deliver, consumes accumulated feedback,
and connects that account to register review and all three authoring skills.
The language refinement is in lean-exposition PR 49. Its transfer cases preserve
normalization and induction hypothesis as terms with explained operations, and
reject replacing coupling by the weaker word connection.

The register comparison uses preserved TeX sources for numerical context.
An initial PDF-text profile was rejected for numerical interpretation after
inspection exposed split sentences and contents-page contamination. OpenAI and
Childs remain qualitative mathematical exemplars. The teaching profile has one
lecture source; the long-record profile uses extended research proofs, not a
matched population of complete reconstructions. Neither corpus distances nor
changes in phrase counts are treated as a quality score.

The first short-paper rerender overlapped the writer's final language edits;
the renderer rejected changed input bytes as designed. That output was not
accepted. Rendering restarted after explicit manuscript freeze.

PR 49 merged at `1e6fe1845c33fc87af0ba809a0e0873672f47b99` after
710 local tests (two skips, no failures), successful hosted checks, and
installation, layout, links and minimal CLI validation in a fresh clone.
Short-paper page inspection also kept the exact-sampling lead-in and exact-circuit
statement with their first displays using small space reservations, rather
than letting their opening sentences break at the page boundary.

The preserved feedback contains original trailing whitespace and extraction line
breaks. It remains byte-identical to the supplied attachments; whitespace checks
exclude only these four verbatim returns. Authored sources pass independently.

## Literature-grounded language review

The writer applied the existing register stage and both available humanizer
skills after the substantive revision, reading every section, caption, table
explanation, appendix, exercise and reference entry in sequence. Display
mathematics and link destinations were suppressed for this language reading;
it was not a fresh proof audit or an independent reader test.

The expert replaces supplier scale with the partial function's dimension
parameter, states correctness for comparisons involving the winner, and names
the capped simulator's conversion of a cell query into an address predictor.
The exposition replaces the cell is harder to hide with the need to bound
arbitrary address guesses, separates the transcript induction's premise from
the forced gate value, and identifies the absence of conditioning on query
count. The record replaces common-witness contract with the three properties
established for the same partial function, makes the winner-comparison condition
explicit, and names coupled inputs and valid certificates in its conclusion.
It removes a duplicated introduction and an incidental example-file report,
expands fifteen visible citation keys, and corrects the Göös–Pitassi–Watson
author order and title from the original title page.

| Inspected source | Actual scope | Writing decision |
| --- | --- | --- |
| OpenAI original | Extracted lines 1–112 and 353–410 | Fix the input and name the probability law before interpreting comparisons. |
| Aaronson–Ben-David–Kothari | Extracted lines 1327–1339, technique overview | Explain the need for domain certification before the addressed array. |
| Ambainis–Iraids–Kokainis v3 | TeX 361–398 and 557–630 | State the surviving-candidate invariant separately from accounting. |
| Ben-David–Kothari v1 | TeX 76–190 | Describe the check before its complexity consequence. |
| Childs, 2025 | Extracted lines 352–389, reversible computation | Retain intermediate registers before explaining inversion. |
| Knuth–Larrabee–Roberts | Extracted lines 1–250 and 1015–1086 | Keep parallel terminology and connect formulas by their inference. |
| Göös–Pitassi–Watson | Extracted lines 1–30, title page | Verify names, order and scholarly title. |

Source locations and editions are recorded in the existing
[passage-specific literature comparison](round10_further_literature.json) and
retained annex inventory. Parent receiving review also inspected the ABK
overview, BDK certificate argument and Knuth §1 items 4–15. No named author's
voice was imitated. Off-promise behavior, joint independence, original-law joint
events, fixed versus growing parameters, normalized successful states and
retained workspace remain explicit. Those are mathematical distinctions, not
rhetorical clutter.

Against the writer's pre-language snapshot, all 36 specialist, 42 exposition and
312 record displays were byte-identical, with passage, claim and explicit anchor
markers preserved. [The baseline preservation check](paper_purpose_preservation.json)
separately compares this complete revision with the published starting edition.

Final checks caught a stale current-bibliography digest after the record link was
pinned, and page inspection found a figure interrupting the four-step proof
overview and a four-row planting table split across pages. The existing reviewed
citation map is rebound to the current bibliography and references; the two small
reading units receive space reservations and are re-rendered. These repairs
change neither the argument nor the imported literature editions.

## Final reading edition

The [final validation](paper_purpose_validation.json) binds the 19-page specialist
companion, 27-page exposition and 96-page complete record to their source bytes.
All pages were inspected in contact sheets, with figures, tables and changed
reading transitions checked at readable size. Final link pinning left every
short-paper page pixel-identical to the inspected render. Repository checks ran
267 tests with two skips and no failures. No Lean theorem source changed and no
Lean rebuild or independent mathematical refereeing is claimed.

## Composition revision after d71775a

This is a further authoring pass over the published 19/27/96-page edition,
requested on 4 November 2026. The earlier validation above remains evidence for
that earlier edition. This pass is agent editorial work, not independent human
refereeing, measured reader learning, or a numerical quality rating.

The supplied reviews were treated as diagnoses of reader difficulties. The
specialist needed a shorter route through the two reductions; the learner needed
the sampling operation before its implementation; the record needed a continuous
classical proof and a clearer reason for the martingale calculation. The
fixed-parameter threshold and the exponent of the displayed nested-search
construction were retained, for the mathematical reasons already recorded above.

### Decisions in the three accounts

| Passage | Reader task and decision |
| --- | --- |
| Specialist opening and §3 | State what the reconstruction explains; consolidate repeated forecasts of the tournament proof. Keep the halving identity and exact conditional law locally assessable. |
| Specialist §4 | Put the direct-product guarantee beside its use and explain why a cell query predicts the address. Retain the whole-run event and the simulator's two counters. |
| Specialist appendices | Move the fractional-weight table and formal correspondence discussion out of the main reductions. Preserve their calculations and exact qualifications. |
| Exposition §3 | State the decoder and exact-circuit guarantees before their arithmetic. Move the Chernoff calculation and circuit-length accounting intact to Appendix A. |
| Exposition §4 | Consolidate the conditional sampling argument into a lemma. Give the plane-rotation proof before reversible preparation and finite repetition caps. Preserve fresh trials and the zero-success case. |
| Exposition §5 and appendices | Keep the verifier's guarantee in the main proof; place full controlled-query bookkeeping with the oracle implementation. Move the projection exercise and formal-proof navigation after the central argument. |
| Record §5 and Appendix E | Keep the exact amplification statement with its consumers; retain the full all-branch-cap and retained-state proofs in Appendix E. Preserve the alternative acceptance-probability induction there. |
| Record §6 | Order the proof by hard law, coupled inputs, erased-zero estimate, capped simulator, direct-product proof and final contradiction. State the direct-product lemma at the simulator's use. |
| Record §§8.9–8.10 | Name the common random bias before summing path derivatives. Explain revealed centered monomials, fresh-query increments, stopping, and the terminal polynomial's representation of a signed derivative sum. |
| Retained material | Keep the concrete boards, transcript induction, query-model conventions, independent side information, original-law joint events, fixed/growing-parameter distinction, source comparisons, and exact error bounds. These prevent specific mathematical misreadings. |

The sequential page review covered all three accounts, including appendices,
references and captions. It led to local repairs: a split short theorem, a
figure interrupting the specialist's proof, a split simulator procedure, a split
finite-parameter table, and stale reading directions after relocation. No visual
asset was invented; the existing renderer and figures were reused.

### Literature and language

The pass reopened Aaronson–Ben-David–Kothari's technique overview (§1.2,
arXiv:1511.01937v2), Ben-David–Kothari's abstract and concrete function definition
(arXiv:2609.15063v1, retained TeX lines 86–123), and
Ambainis–Iraids–Kokainis's quantum procedure and candidate invariant
(arXiv:2609.11664v3, retained TeX lines 557–585). Their relevant practices are
concrete: make the certification problem motivate the array; define what an
algorithm returns before estimating its cost; give the invariant next to the
procedure. The revision adapts these practices without borrowing sentences or
assuming that matching a named author's voice establishes quality.

Before/after register comparisons use the previous edition's retained TeX
profiles, with the same genre limitations: two related research papers for the
specialist and record, one de Wolf lecture-note source for the exposition.
PDF extraction was used only for qualitative reading. The comparisons and
baseline manuscripts are retained with the delivered PDFs under `register/`.
Sentence-length movement is small; the substantive changes concern order and
allocation. Flagged semicolons separating algorithm steps and negations that
state off-promise or conditioning restrictions were deliberately retained.
The profiler's apparatus and stock-lexicon rates are zero in both editions;
these results do not measure mathematical understanding.

### Propagation and transfer

The existing shared authoring ontology, reader review, and all three transition
skills are updated in lean-exposition commit `527796f`, based on merged PR 49.
They distinguish the decisive inference, the guarantee needed at its use, and
the derivation implementing that guarantee. They also require a reverse outline
when successive revisions have accumulated repeated explanations, and a reading
of the actual PDF transition after relocation.

Two differently shaped applications test that distinction. In the teaching
paper, the sampling-law proof stays in the main argument while the Chernoff and
integer-circuit accounting move to supporting calculations. In the long record,
the probability-space construction comes before the simulator; the exact
product bound appears at the simulator and its complete proof follows. The
exception is equally concrete: moving the plane-rotation argument out of this
exposition would hide the operation the paper promises to teach. Likewise, a
paper whose contribution is a comparison of two proofs should keep those proofs
adjacent. This is editorial transfer evidence, not a reader study.
