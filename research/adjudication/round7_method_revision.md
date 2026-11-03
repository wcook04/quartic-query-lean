# Round seven: revision of the mathematical writing method

This is an editorial adjudication of all 84 method findings, not a claim that
84 independent rules were missing. The reviewed packet contained 20 quantum,
24 newcomer, 16 lower-bound and 24 editor findings. Most requests sharpen an
existing decision or identify a failed application. The revisions preserve the
four transitions and the register stage; no runtime orchestration or new skill
family is introduced.

The method base is `wcook04/lean-exposition` commit
`5a9a3ab` (PRs #40–42). Work is on `codex/quartic-r7-writing-method`, in an
isolated checkout; the original `codex/reader-map-performance` checkout was
preserved. The current method revision is uncommitted pending integration.
The rule inventory remains 26 IDs, six adopted and twenty candidate. Eight
existing rule bodies or limits are refined. Prior instances, specimens and
corpus observations remain; new history distinguishes those observations from
reader-effectiveness evidence. The method decisions follow the existing
review loop and generalise-uppropagate: source inspection, specific decision,
two materially different transfer cases, exception, then smallest owner.

## The decisions that change

**Allocate explanation by the next operation.** A research companion can import
a familiar supplier's contract; a teaching article must enable the unfamiliar
operation; a record must make its derivation recoverable. Opening obligations
compete for attention. The former one-page theorem/history/example-map demand
is replaced with enough context to enter the next example, immediate credit,
and a precise theorem at the point its definitions support it. Detailed
historical arithmetic can follow the construction. This is a change to
`skills/record-to-expository/SKILL.md` and `skills/long-to-short/SKILL.md`, not a
new demand for more introductory material. Existing prerequisite and
changed-case instructions are retained. A named course never substitutes for
the agreed reader's ability to perform the needed step.

**Preserve meaning through editorial movement.** The shared
`docs/authoring.md` now makes event, time scope, available information and type
of guarantee explicit at a consequential rewrite. A fixed cap differs from a
fixed realised count; a completed transcript can reveal future information.
Exercises are checked against their exact endpoint or infimum question. A toy
case's uninformative bound need not imply that its object does not exist.
Figures must agree with their data and support the operation they promise.
The long-record skill checks displayed labels, target arguments and return
instructions after reordering. These decisions protect prose and teaching;
they do not require a new theorem or a five-field inventory in every paragraph.

**Use register evidence to make an editorial decision.** `skills/register/SKILL.md`
and `docs/register-stage.md` now select genre and region, inspect extracted
prose, distinguish editions, and treat a successful keep decision positively.
Metric movement is descriptive. Corpus occurrence does not establish teaching
effectiveness. RG-01/02 own source selection and the full-document pass;
RG-06/21 reconcile navigation with reference apparatus; RG-16/17/19 preserve
mathematical subjects, negatives, genuine classifications and attribution;
RG-26 checks the operation and data in a figure. RG-16's former measured-label
specimen is preserved as history and replaced with a scoped procedure example.
No rule is added. Arbitrary list cardinalities and a universal punctuation ban
are rejected as clarity tests. Their historical origin is retained honestly.

The quartic consumer `docs/writing_method.md` also changes: the stale
`b05c31c` reference, expert-only audience, one-page statement appendix and
absolute no-expansion rule no longer govern the exposition. `docs/README.md`
now routes to the three current accounts and this method record.

## Literature actually inspected

The following readings informed decisions, with limited scope. They are
original sources, not merely the reviewers' descriptions. No prose is copied
as a writing template and no full-proof audit is claimed.

- Shalev Ben-David, *Query Complexity Basics*, CS867/QIC890 notes, §§1.1–1.2,
  PDF pp.1–3: the black-box task and OR precede the decision-tree cost; the
  recursive tree is then executed in words. This supports task-to-operation
  ordering, not a mandatory OR prelude in every field.
  [Source](https://cs.uwaterloo.ca/~s4bendav/files/CS867QIC890S22QueryBasics.pdf).
- Ronald de Wolf, *Quantum Computing: Lecture Notes*, arXiv:1907.09415v6,
  §§7.1–7.3, especially the geometric argument and the amplitude-amplification
  reuse: the two reflections are explained before their rotation is reused.
  The full-space caveat in §7.2 protects a necessary distinction despite its
  negations. This is evidence for teaching an operation and retaining semantic
  negatives, not evidence that our readers learned it.
  [Exact edition](https://arxiv.org/html/1907.09415v6).
- Farhi, Goldstone, Gutmann and Zhou, *The Quantum Approximate Optimization
  Algorithm and the Sherrington–Kirkpatrick Model at Infinite Size*, Quantum 6,
  759 (2022), §4, pp.4–5, equations (13)–(22): the fixed-parameter moment
  theorem is followed by distinct concentration statements over instances
  and measurements. Read from the unmodified licensed PDF retained in
  `lean-exposition/docs/annex/`. This supports retaining the event and fixed
  parameters when summarising, rather than importing a vague concentration
  slogan. The extraction contains damaged math glyphs, so it was used with
  equation locators as a reading aid, not as a clean punctuation baseline.
  [Publisher](https://doi.org/10.22331/q-2022-07-07-759).

The revised skills ask for a source passage doing the same job, not a fixed
number of first pages. No exhaustive recent-novelty search was performed by
this method pass; source-age and novelty questions remain with the paper's
literature review. No source is called obsolete merely because it is old.

## Transfer trials on existing papers

These are agent-executed editorial trials against actual existing source
passages. They neither modify those papers nor simulate observed human data.
The source hashes below preserve the tested editions.

### Probability: zero-temperature SK exposition

Inspected `papers/qaoa-sk/expository/main.md` at method base `5a9a3ab`:
opening; §1's two-spin calculation; §2's cumulative-mass example and general
identity. The reader is promised algebra and calculus. The opening names the
contact/curvature contradiction; §2 first performs the weighted-area count.
The task was to recover what its integral counts, then change the weights.
For masses two at 1/4 and one at 3/4, both area counts give 7/4. Exchanging
those masses gives 5/4. Dividing by the total mass three would instead turn
that integral into an average and lose the stated object. Six exact rational
checks across this and the next trial were executed successfully.

Decision: retain the successful first calculation and its explicit
non-probability boundary. An attempted style-driven shortening to a probability
average is rejected. The theorem's general integral identity still requires
its stated nonnegative interchange input; the finite example cannot prove it.
The revised opening rule does not require adding theorem notation and all
analytic supplier constants before this operation. The standard Gaussian
variance facts can be imported at their use; their existence does not remove
the need to teach how the weights are used. This tests the reader-operation,
semantic-preservation and positive-keep principles in an analytic setting.

### Number theory: Erdős 257 exposition

Inspected `paper/257/erdos257-expository-sums-never-fractions.tex` in
`plectis-erdos-257-register` at `ec12b2c136c9f20f605d8956ac0d7309e708cc35`:
§1; “Average complete attempts”; “The same choices for any admissible set”;
and the answers for `chk:columns` and `chk:order`. Its opening multiplies a
concrete reciprocal Mersenne sum by 255 before presenting the full supported
class. This is a useful exception to a rigid theorem-and-history-first page.

The task was to recover why rows cannot choose separate multipliers. For the
printed row n=9 and column k=12, the fractional part is 7/511. Recomputing
the two displayed nonzero rows across k=4,8,12,16 confirms that averaging
complete columns equals summing row averages, whereas adding separate row
minima gives a strictly smaller quantity than any displayed column total.
The three row groups in the final argument have three different jobs: zero
initial rows, completed finite cycles and the uniformly controlled far tail.
Decision: keep all three groups; rewriting the list into two or four items
for a cadence score would obscure the proof. Preserve the order
`t -> Q -> T -> M`, since the far-tail bound depends on the already fixed Q.
This tests the same methods on discrete arithmetic and quantifier order,
without adding any number-theory condition to a general writing rule.

### Exceptions and failed generalisations

The SK short paper's theorem and Erdős 257 short paper's weighted-support theorem
address specialists with the needed definitions. The method does not require
replacing their statements with beginner calculations. A supplier proof can
stay on the main route if the agreed reader needs its inference; “standard”
alone is not a reason to hide it. A reference record with distinct statement-
audit and mathematical entry tasks can retain a branching guide; one sequential
note may need none. A schematic may illustrate geometry while a quantitative
bound is vacuous, if that boundary is named. Finally, the de Wolf full-space
reflection caveat and the SK non-probability distinction refute a blanket ban
on negation or comparison. These exceptions prevent the local quartic repair
from becoming a universal manuscript outline or punctuation code.

## Finding-by-finding dispositions

“Refined” names an actual method edit; “existing rule” means the method already
contains the safeguard and the manuscript application must be judged separately;
“local choice” retains advice at this example's scope; “implementation” assigns
a concrete owner outside prose guidance; “rejected generalisation” states the
part not adopted. These are method dispositions, not assertions that every
manuscript passage has passed final review.

Owner abbreviations: **A** = `docs/authoring.md`; **E** = exposition skill;
**S** = short-paper skill; **L** = long-record skill; **R** = register skill
and `docs/register-stage.md`; **RG-nn** = operative `rules.json` entry.


### editors_and_funnel

| ID | Disposition | Decision and owner |
| --- | --- | --- |
| M01 | existing rule | E first consequential operation test already fixes the requested audience; an added course prerequisite cannot close the manuscript issue. |
| M02 | refined | E/S opening paragraphs replace fixed page obligations with the next reader decision; detailed predecessor arithmetic may follow the construction. |
| M03 | existing rule | E/S/L retain distinct teaching, selection and reconstruction jobs; apply by reallocating suppliers, not by enforcing three different statements. |
| M04 | refined | A active-object check and RG-02 cover prose verbs and fixed budgets versus realised actions. |
| M05 | refined | A checks the question’s exact endpoint, infimum or attainment target before accepting its arithmetic. |
| M06 | refined | E example procedure and RG-26 bind literal counts, parameters and caption to the operation shown. |
| M07 | refined | A toy-boundary paragraph distinguishes a missing useful hypothesis from nonexistence at degenerate parameters. |
| M08 | existing rule | E already checks what symmetry hides and uses one changed case only when the later inference needs it. |
| M09 | refined | L destination paragraph and RG-06 check visible labels, argument and return after section movement. |
| M10 | existing rule | L formal audit and S verification paragraph already distinguish ordinary transport, endpoints and execution; retain those relations. |
| M11 | refined | RG-02 and S/R replace presumptive rewriting with equally legitimate retain, move, shorten, split and explain decisions. |
| M12 | rejected generalisation | RG-19 removes the instruction to turn three items into two or four; functional list cardinality comes from the mathematics. |
| M13 | refined | RG-16/17 retain semantic negatives and meaningful comparisons; author punctuation preference is not a clarity law. |
| M14 | refined | RG-06 removes its conflict with RG-21: separate legitimate entry tasks warrant a compact branching guide. |
| M15 | refined | R and RG-21 interpret body and appendix separately; apparatus frequency does not decide whether evidence is usefully placed. |
| M16 | implementation | register.py text report now distinguishes threshold distance from observed min/max; the register-audit owner implements and tests it. |
| M17 | refined | R/RG-01 require declared genre, comparable region and one edition per work in a baseline; a mixed shelf stays contextual. |
| M18 | refined | R requires register dump and source-page extraction inspection; register-audit owns the YAML parser repair. |
| M19 | refined | R remeasurement evaluates the stated reader repair first and reports metric movement descriptively, including justified movement away. |
| M20 | implementation | Round-seven packet builder must preserve 26 operative rules and ID closure; R now states that export boundary; intake owns repair. |
| M21 | refined | R and stage guide label historical domain probes descriptive; observed human reconstruction remains unperformed here. |
| M22 | refined | A closes historical findings against current passages as resolved, regressed, superseded or unresolved; plans alone do not close them. |
| M23 | existing rule | A already requires exact editions and source locators; the new source-job paragraph reinforces source metadata and historical role. |
| M24 | existing rule | A retains a bounded completion test and adds result-linked reconstruction tasks; minor preferences do not become extra release gates. |

### quantum_specialists

| ID | Disposition | Decision and owner |
| --- | --- | --- |
| MF01 | implementation | Canonical main already has all 26 bodies; intake repairs list sanitisation in the packet export, and R requires reference closure. |
| MF02 | refined | RG-01/R select genre and region rather than forcing three documents toward one mixed-corpus distribution. |
| MF03 | refined | R inspect-before-measure instruction separates damaged extraction and nonprose; register-audit repairs YAML while preserving abstract content. |
| MF04 | refined | RG-19 and R classify flagged words by mathematical role before editing; author lists and logical force survive false positives. |
| MF05 | refined | RG-02/S require a concrete benefit and recheck semantic invariants; whole-document inspection does not mandate churn. |
| MF06 | refined | RG-16 replaces the underspecified measured-label specimen with a named measure/reset procedure and retains the former wording as superseded history. |
| MF07 | refined | S/E openings now permit relocating constants and secondary comparisons after their objects; no extra overview paragraph is required. |
| MF08 | existing rule | S antecedent comparison already checks hypotheses and interfaces; the quartic oracle/guarantee/resource comparison is a local application. |
| MF09 | existing rule | E operation-level audience test is retained; actual branch, measurement and next-stage operations must be supplied to the requested reader. |
| MF10 | local choice | Use the existing fractional calculation or an explicitly abstract comparison table; reject any implication that an abstract table is a realised full input. |
| MF11 | existing rule | E/S distinguish supplier contract, reason and constants; moving amplifier arithmetic is an allocation repair, not a new universal omission rule. |
| MF12 | refined | A available-information check and E figure/algorithm distinction prevent proof-only quantities becoming algorithm knowledge; no repeated five-field form. |
| MF13 | existing rule | A first-use and S statement-preservation rules already require a premise before the formula that uses it; no new formula-order rule is needed. |
| MF14 | refined | L and RG-06 check semantic arrival and return as one changed route, including readable labels. |
| MF15 | existing rule | L selects a complete argument relative to explicit imports; a broad completeness adjective does not oblige proving every textbook input. |
| MF16 | rejected generalisation | RG-17/19 reject punctuation or list-count restrictions as evidence of clarity, retaining meaningful comparisons and real classifications. |
| MF17 | existing rule | A exact source scope and edition rule survives; no generic demand to replace older versions, and this method pass claims no novelty search. |
| MF18 | refined | A/R separate corpus occurrence, editorial judgment, agent reconstruction and observed readers; no human-learning result is inferred. |
| MF19 | refined | RG-06 reconciles one sequential roadmap with legitimate branching reference tasks; L restores only local objects at entry. |
| MF20 | refined | Eight existing RG owners and shared A are amended; no new IDs, parallel checklist or quartic-specific procedure is installed. |

### newcomer_readers

| ID | Disposition | Decision and owner |
| --- | --- | --- |
| NR-M01 | existing rule | E already forbids raising a fixed audience; accept only operations assumed for that reader, locally taught or explicitly imported. |
| NR-M02 | refined | E replaces about-a-page theorem/history/map prescription with sufficient context for the next example. |
| NR-M03 | existing rule | E prerequisite ladder already asks what the reader can do; applied through query/phase/measurement operations, not another terminology list. |
| NR-M04 | local choice | Retain the deterministic example and use the record’s nonuniform calculation to reveal a needed distinction; no example-count requirement. |
| NR-M05 | refined | E treats example data, law and conventions together; a linked changed example must state its reset. |
| NR-M06 | refined | A separates endpoint exclusion and an infimum bound when validating exercises. |
| NR-M07 | refined | A current-passage disposition check rejects an unimplemented plan as evidence of repair. |
| NR-M08 | refined | L/RG-06 check displayed number and topic with target and return; syntactic link validity is insufficient. |
| NR-M09 | refined | A retains event, conditioning and single-trial versus whole-run scope in a probability synopsis. |
| NR-M10 | existing rule | E/S notation-collision checks already apply across the reader’s memory span; p-as-probability versus p-as-cost is a local rename decision. |
| NR-M11 | refined | R/RG-01 make genre-matched teaching and proof comparisons primary; slides do not set paragraph-length targets. |
| NR-M12 | refined | R requires representative extraction/source inspection and unavailable-metric disclosure when damaged text cannot support comparison. |
| NR-M13 | refined | RG-19 explicitly exempts author names, exhaustive cases and real parallel objects from ornamental triad repair. |
| NR-M14 | refined | RG-21/R separate audit appendices from the proof route for apparatus interpretation. |
| NR-M15 | refined | R asks for a reader difficulty behind a flag; short sentences can still conceal an unfamiliar operation. |
| NR-M16 | implementation | R specifies export inventory/reference closure; intake repairs missing active rules instead of pretending detectors supply their text. |
| NR-M17 | refined | RG-06 no longer bans long-record guides that RG-21 permits for different entry tasks. |
| NR-M18 | refined | RG-02/R allow deliberate preservation and require meaning checks around consequential split/merge edits. |
| NR-M19 | refined | E/RG-26 require a concrete figure operation, matched data and a distinction between explanatory and algorithmic information. |
| NR-M20 | local choice | The stopped-simulator task targets the main reduction using existing material; no compulsory simulator exercise is added to the general skill. |
| NR-M21 | refined | R/A add job-matched teaching passages beyond an opening sample and require honest inspected scope. |
| NR-M22 | existing rule | S already distinguishes a named recipe’s bottleneck from framework impossibility; A preserves date and source role. |
| NR-M23 | existing rule | E’s question/answer separation and next-output checks succeeded; preserve them rather than add another instruction. |
| NR-M24 | refined | A/R explicitly identify simulated readers and agent tasks; actual recruited-reader evidence remains absent. |

### lower_bound_specialists

| ID | Disposition | Decision and owner |
| --- | --- | --- |
| M01 | refined | RG-02 and S/R replace the always-rewrite incentive with a positive keep decision and exact event/cap preservation. |
| M02 | refined | L/RG-06 inspect each moved destination’s incoming labels and distinct returns, not just one working anchor. |
| M03 | refined | A literature paragraph compares quantified objects, accepted inputs, access costs and implemented versus rejected source proposals. |
| M04 | refined | RG-19 removes arbitrary recardinalisation; three author names and three genuine budgets remain functional lists. |
| M05 | refined | R/RG-21 judge formal prose by checked claim, limitation and region; neither zero nor high apparatus rate establishes success. |
| M06 | refined | RG-06 now permits the branching guide already allowed by RG-21 when reader tasks differ. |
| M07 | refined | RG-26/E check finite figure data independently in each document and distinguish schematics. |
| M08 | existing rule | A bidirectional correspondence already reaches claim-bearing summaries; exercise, caption and catalogue scope are retained in current reconciliation. |
| M09 | existing rule | E fixed-reader first-use test already applies; a new prerequisite course is an unresolved mismatch, not a successful repair. |
| M10 | refined | A validates the exact endpoint/infimum/attainment question independently of the supplied parameter recipe. |
| M11 | refined | A semantic guarantee and RG-02 check preserve deterministic, conditional, high-probability and capped claims across stages. |
| M12 | existing rule | E already carries an example across the decisive transition; the stopped-simulator changed case applies that rule without inflating exercise counts. |
| M13 | refined | A temporal-conditioning paragraph forbids future observations when predicting the next action; formal filtration notation is optional. |
| M14 | refined | A toy-boundary paragraph names the missing hypothesis or useful estimate; object nonexistence needs its own justification. |
| M15 | existing rule | E already tests the main route with optional supplier proof skipped; the current rendered passage, not the plan, must realise that choice. |
| M16 | refined | R judges flagged paragraphs by instructional job and accepts justified metric divergence; question counts do not measure the main inference. |

## Applied document lessons and evidence boundary

The expert writer reports replacing pathwise-sounding lower-bound language
with distributional events, preserving dummy-run history, and moving routine
amplifier arithmetic while expanding the tensorisation, stopped-simulator and
promise-transfer inferences. Its abstract fractional sampler is explicitly an
abstract example, not an asserted input realisation. The exposition writer
reports executable query/oracle/phase steps, sampler execution before
amplification, a whole-register conditional-law explanation, and a stopped-XOR
simulation with a one-way event. Both retain successful passages and report
metric movement without using it as acceptance. These are writer-reported
applications pending the integrated current-edition review; the final prose and
render evidence, not these reports, decides manuscript acceptance. The record
owner supplies its own current passage and reading-route audit.

Rejected blanket conclusions are recorded above: no universal introductory
page shape; no expansion prohibition; no forced rewrite of sound prose; no
forced two/four-item lists; no shared research median for all genres; no claim
that low apparatus rate certifies good formal exposition; no source-age rule;
no efficacy inference from corpus occurrence or simulated reader success.
The method remains a substantive writing practice with concrete reader tasks,
not a detector pass/fail system.

## Validation and integration

- Eight refined rule entries retain all 26 IDs and historical evidence;
  `python3 scripts/register_rules.py validate` passes.
- `python3 scripts/check_layout.py` passes (918 maintained files).
- `python3 scripts/check_links.py` passes (48 authored documents).
- Six exact rational transfer checks pass for the two existing-paper cases.
  They check finite reconstruction and rejected compression, not the general
  mathematical theorems.
- The current register test module passes all 43 tests using
  `PYTHONPATH=src /Users/willcook/src/lean-exposition/.venv/bin/python -m unittest discover -s tests -p test_register.py -v`.
  The minimal example's `validate` and `inspect` commands pass in that environment;
  their retained extraction remains partial and is not semantic certification.
- `git diff --check` passes in both repositories; quartic `make check-layout`
  passes after the consumer-navigation update.
- Runtime register fixes and regression tests are owned by the register-audit
  agent; packet-export fixes are owned by intake. Their final receipts and the
  full integration suite are reported by the parent. No submitted review script
  was executed. No human reader experiment was performed.
- No commit has been made by this method agent. The parent owns scoped commits,
  final method revision binding, public PR decisions and manuscript acceptance.

### Tested source identities

- `expository/main.md` SHA-256 `c17d1e4e497443c153dbfaed9967804be060f37981ee446a2f3daf79a50f2f7a`.
- `short/paper.md` SHA-256 `0cab99e62e04475d45ef7ab47579feee2be323ae8b9c4108d1e26adbd1ba36a2`.
- `257/erdos257-expository-sums-never-fractions.tex` SHA-256 `27275fec09eb84e1bd833411f9e30ed4e8bfae35ab711d373cc7395bd1845002`.
- `257/erdos-257-mersenne-support-subseries.tex` SHA-256 `dc3986fdadf0e875ef95894e7cab1eb36f42dddfcf2bceb1eea588e556a3fd0b`.
