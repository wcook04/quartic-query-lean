# 4-minute film: Following the claim into Lean

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

Production design, supplied-snapshot scope. The spoken text is a draft for Will Cook; the mathematical result is credited to OpenAI. Exact data, captions and corpus identifiers below are production instructions. A caption showing a source status reports the supplied corpus; this return does not rerun Lean or Comparator. Mathematical fact, source report and proposed finite calculation remain distinguishable.

The example uses 0-based indices throughout, matching Lean's `Fin`; the preprint uses 1-based indices. Convert every visible index together if the production chooses the preprint convention. Never switch conventions within a shot. The actual family parameters are k=2, t=1, m=4, ℓ=2, r=40. At this size L=0, so the asymptotic lower-bound theorem supplies no lower bound for the example. Use the same four columns for all scenes, with a labelled change to the general hard distribution when the proof requires it.

One fixed supplied circuit C=QuarticQuery.Forrelation.forrCircuit 1 1 is used throughout; its first argument is k−1. Its actual evaluation transcripts are circuitEval C (A_{i,h}). The exact gate numbering is determined by that definition, although this film design does not materialize the transcript bit strings or its numerical size. Pointer bit encodings are `pointerEquiv 2` inverse images of the displayed row targets, with no unverified integer endianness assumption. All unspecified cell bits are false.

The exact finite computations are proposed new statements, not new separation mathematics. They belong in NEW_STATEMENTS.json and remain pending Lean evidence. The film's displayed asymptotic claims use the existing corpus rows, with all quantifiers retained in captions.

## Timing

These are planned edit windows. The word counts leave room for the indicated diagrams and pauses; no recorded presenter performance is claimed.

| Shot | Window | Spoken words | Words per minute if continuous |
| --- | --- | ---: | ---: |

| film4_s01 | 00:00–00:30 | 62 | 124.0 |

| film4_s02 | 00:30–01:05 | 66 | 113.1 |

| film4_s03 | 01:05–01:40 | 71 | 121.7 |

| film4_s04 | 01:40–02:20 | 79 | 118.5 |

| film4_s05 | 02:20–02:55 | 60 | 102.9 |

| film4_s06 | 02:55–03:25 | 61 | 122.0 |

| film4_s07 | 03:25–04:00 | 72 | 123.4 |

Total planned duration: 240 seconds. Total spoken words: 471.

Sources and exact editions: `sources.md`. Shared exact data: `visual_data.json`. Each spoken passage and picture has a separate correspondence anchor.

## 00:00–00:30 | Start from a sentence

**Spoken**

<!-- passage:film4_s01 -->
Take the claim we just saw: the optimal universal exponent is four. In the reader, selecting that sentence opens its exact mathematical wording beside the Lean declaration. The link also exposes every definition the statement depends on. We can ask whether the proof checks, whether the checked statement matches the paper, and whether its proof follows the explanation. Those are separate questions.
<!-- /passage:film4_s01 -->

**Picture and exact data**

<!-- passage:film4_s01_picture -->
Start with the same four-column diagram, then select thm-1.1. Left: Theorem 1.1 from printed page 1 of the supplied PDF, beginning “The optimal power is” and showing α_tot=4; retain its full family-bound clauses in the expandable paper panel. Put the normalized corpus statement in its own labelled tab. Right: `QuarticQuery.alphaTot_eq_four_unconditional : alphaTot = 4` with ‘optimal exponent clause’; a second tab opens the full source declaration `QuarticQuery.theorem_1_1_unconditional`. Do not portray the short equality alone as all of Theorem 1.1. Retain the theorem's complete binder list in an expandable textual panel.
<!-- /passage:film4_s01_picture -->

**Corpus statements:** `thm-1.1`, `eq-1`.

## 00:30–01:05 | Inspect the meaning

**Spoken**

<!-- passage:film4_s02 -->
Open quantum query complexity. The program and initial state are chosen before the input. Access to that input comes through the bit oracle. The cap covers every measurement branch. Then inspect the winner definition: an all-one column, defined address answers, correct transcripts and pointers to zeros elsewhere. These details determine what was proved. A familiar-looking theorem can mean something different when one of its definitions changes.
<!-- /passage:film4_s02 -->

**Picture and exact data**

<!-- passage:film4_s02_picture -->
Show only exact source excerpts from Statement.lean: in QLe, `∃ (w : ℕ) (ψ₀ : State ι w) (A : AdaptiveProgram ι w)` before `∀ x b`; in queryCap, `.measure _ yes no => max yes.queryCap no.queryCap`; in WinsAt the four conjuncts. Map paper notation to source names: O_x↔bitOracle, winning column↔WinsAt, total function↔addressedF/Fkm. Exact supplied-source locators: Statement.lean:144–148 (QLe, including its ConstantOnPromise alternative); :122–127 (queryCap); :277–284 (WinsAt); :102–105 (bitOracle). Show the whole definition when expanded, including the constant-function alternative.
<!-- /passage:film4_s02_picture -->

**Corpus statements:** `def-Q`, `def-query-oracle`, `def-winner`, `def-F`, `claim-winner-fidelity`.

## 01:05–01:40 | Compare against an independent challenge

**Spoken**

<!-- passage:film4_s03 -->
A challenge containing the required statements and vocabulary is compiled independently of the submitted proofs. The solution supplies proofs under matching names. Comparator checks the requested declarations, their statement dependencies and permitted axioms against that challenge. The bundles cover foundations, construction, tournament, separation and the unconditional result. The supplied records report acceptance in local rehearsals. The source package omits the original run receipts; these checks were not reproduced for this design.
<!-- /passage:film4_s03 -->

**Picture and exact data**

<!-- passage:film4_s03_picture -->
Display five bundle labels from the actual directories, and open Unconditional/comparator.json. Show its exact `challenge_module`, `solution_module`, four `theorem_names`, and permitted axioms `[propext, Quot.sound, Classical.choice]`. Caption ‘No custom mathematical axioms; standard permitted foundations listed’. The challenge begins `public import Mathlib`; the solution imports the implementation. Mark raw receipts ‘referenced, absent in supplied ZIP’; no green imitation terminal output. The empty definition_names list supplies no definition holes; it does not turn off comparison of statement dependencies. Source: Lean Language Reference §25.1.5.8, Comparator, https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/; Lean v4.35.0 release notes, https://lean-lang.org/doc/reference/latest/releases/v4.35.0/. The supplied toolchain is v4.36.0-rc2. Exact bundle values and source excerpts are in checking_visual_data.json.
<!-- /passage:film4_s03_picture -->

**Corpus statements:** `thm-1.1`, `lem-2.1.i`.

## 01:40–02:20 | A changed definition can make a theorem vacuous

**Spoken**

<!-- passage:film4_s04 -->
Here is a deliberate wrong solution. It keeps the displayed theorem and adds an impossible requirement to the definition of a valid comparison: a proof of False. Under that assumption, any conclusion follows. Lean can check the resulting implication because no comparison satisfies its premise. Comparator should reject it because the definition differs from the challenge. Checking only the theorem's printed name or surface formula would miss this change. The supplied record reports that this negative case was rejected.
<!-- /passage:film4_s04 -->

**Picture and exact data**

<!-- passage:film4_s04_picture -->
Diff the actual ChangedDefinition.lean structure against Tournament.IsComparison in Statement.lean: retain `complementary`, `self_zero`; add `impossible : False`. Show exact proof term `ha.impossible.elim`. Then highlight `expected_weight_le_half` and the unchanged displayed conclusion. Label ‘supplied negative test; rejection reported, not rerun here’. The comparison test concerns eq-13. Do not imply this negative module contaminates the production proof imports.
<!-- /passage:film4_s04_picture -->

**Corpus statements:** `eq-10`, `eq-13`.

## 02:20–02:55 | What the other negative cases test

**Spoken**

<!-- passage:film4_s05 -->
The other cases make distinct changes: an unfinished proof using sorry; a new axiom asserting False; a weaker bound; and an omitted declaration. Their rejection tests whether the comparison catches these particular mistakes. It cannot establish that every possible mistake is detected, or review the English explanation. The valid solution must still prove the intended statement under the intended definitions.
<!-- /passage:film4_s05 -->

**Picture and exact data**

<!-- passage:film4_s05_picture -->
Show the four actual source modifications in separate rows: SorryProof: `sorry`; ForeignAxiom: `axiom cheat : False` and `cheat.elim`; WeakenedConclusion: RHS `W / 2`→`W`; MissingDeclaration: `expected_weight_le_half` absent. Reference corresponding Negative/*.json. Each row says ‘rejected according to supplied record’. No invented exit code or exact error string. Keep changed-definition test visible above as the fifth case.
<!-- /passage:film4_s05_picture -->

**Corpus statements:** `eq-13`.

## 02:55–03:25 | The proof route is visible too

**Spoken**

<!-- passage:film4_s06 -->
A checked endpoint does not certify every route to it. The paper returns a short tournament list; the formal program consumes the list inside a verifier, so that correspondence is partial. The Lean direct-product proof uses induction on subdistributions; the paper uses a supermartingale. The reader shows these differences beside the affected statements, while preserving the headline theorem's separately recorded status.
<!-- /passage:film4_s06 -->

**Picture and exact data**

<!-- passage:film4_s06_picture -->
Open prop-3.2: evidence formal_statement=partial, comparator=not_run; show the note on `QuarticQuery.Upper.tournament_runs`. Then lem-4.1: exact statement relation, alternative route; expand ties to distinguish the exact full statement declarations from the declaration reached by the headline. Finally thm-1.1: exact, built_at_pin, compared, alternative. Never merge these three rows into one confidence percentage. These values are verbatim supplied corpus fields; display does not promote them.
<!-- /passage:film4_s06_picture -->

**Corpus statements:** `prop-3.2`, `lem-4.1`, `thm-1.1`.

## 03:25–04:00 | What remains a mathematical judgement

**Spoken**

<!-- passage:film4_s07 -->
A kernel proof establishes a formal conclusion from its definitions and permitted foundations. It cannot decide whether those definitions capture the intended problem, whether the proof is new, or whether this film explains it faithfully. The supplied development records an unconditional theorem, AI review of statement fidelity and no human review. Our four-column calculation has its own pending formal statement. Following a claim through to its definitions makes these remaining questions inspectable.
<!-- /passage:film4_s07 -->

**Picture and exact data**

<!-- passage:film4_s07_picture -->
Return to the same four-column example. Side panel separates ‘formal derivation’, ‘paper-to-definition correspondence’, ‘attribution’, and ‘film explanation’. Display the exact three statuses from the main film's end card. Use no ‘100% verified’ claim. Link to the fidelity review with its historical snapshot label, current source declarations and NEW_STATEMENTS entries; do not treat the older review's conditional headline as the latest source state.
<!-- /passage:film4_s07_picture -->

**Corpus statements:** `thm-1.1`, `claim-winner-fidelity`.

**Proposed finite statements:** `reader-forrelation-yes`, `reader-forrelation-zero`, `reader-example-instance`.
