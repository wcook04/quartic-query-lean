# From a sentence to the statement it actually means

**AI assistance.** Will Cook directed the work. AI agents based on large language models produced the mathematics, the Lean proofs and this manuscript; no person has yet reviewed them.

## Entry from the worked example

<!-- passage:fidelity-1 -->
A reader clicks the outward pointer from the all-one column to a zero in another column. The explanation highlights the matching phrase, “a winner points to a zero in every other column,” and opens the exact fourth conjunct of `WinsAt`. The drawing, the sentence and the source definition stay selected together. Returning to the film or prose restores the same selection and scroll position. This is the basic interaction: an explanation remains attached to the mathematical object it describes. [Packet: `paper/extracted.md`, Section 2.2; `repository/lean/QuarticQuery/Statement.lean`, `WinsAt`.]

The reader can also select the sentence “the optimal universal exponent is four.” That opens `thm-1.1`, with `QuarticQuery.theorem_1_1_unconditional` selected by default. The older conditional declarations remain available in a secondary list. A declaration with a convenient short name must never displace the current unconditional theorem. [Packet: `repository/corpus/statements.json`, `thm-1.1`; `repository/lean/QuarticQuery/Results/Unconditional.lean`.]
<!-- /passage:fidelity-1 -->

## The reading surface

<!-- passage:fidelity-2 -->
Use a quiet, linear exposition with exact claims linked at their point of use. A short, adjacent label appears only when its distinction matters: “alternative proof,” “partial correspondence,” or “new example, not yet checked in Lean.” Full diagnostics live in the inspector. A single overall green status is unsuitable because the corpus separates statement agreement, builds, comparison, proof route and reach. [Packet: `repository/docs/statement_evidence_contract.md`; `repository/corpus/README.md`.]

On desktop, the inspector has two equal columns. The left contains the exact paper excerpt with its surrounding hypotheses. The right contains the complete source signature, preserving every binder. A narrow row below them contains evidence for the **selected declaration**, and a second row gives the paper record's unchanged evidence fields. On a phone, stack the same contents and retain a sticky statement identifier. Do not truncate hypotheses into a tooltip.

Use plain black and white text, clear mathematical typesetting, and a small number of saturated colors assigned to selected mathematical objects. Every color has a text label. Keyboard selection, back/forward navigation, readable focus outlines and reduced motion are part of the design. A reader can expand one dependency at a time without a moving graph displacing the selected sentence.
<!-- /passage:fidelity-2 -->

## Three texts, kept distinct

<!-- passage:fidelity-3 -->
| Text | What it is | Source |
| --- | --- | --- |
| Paper excerpt | The author's printed sentence or display, with its local hypotheses | `paper/quartic-query-separation.pdf`, with a page/paragraph locator and exact quote span |
| Corpus statement | A normalized, sometimes corrected ledger description | `statements.json[id].statement`, `corrected` and both statement hashes |
| Lean statement | The declaration type in its actual vocabulary | The resolved source declaration now; an elaborated type export when supplied |

The present corpus stores the normalized statement and a source-line hint. It does not store an exact paper quotation or the complete elaborated type. Those must be added as distinct fields. Never label normalized ledger prose “the exact paper sentence,” and never label a copied source signature “Lean's elaborated type.” [Packet: `repository/corpus/statements.json`, record schema; `AUDIT_FINDINGS.json`, AUDIT-11.]

For the headline, the source signature shown in this snapshot is:

```lean
theorem theorem_1_1_unconditional :
    alphaTot = 4 ∧ UniversalPower 4 ∧
      ∀ k : ℕ, 2 ≤ k → ∃ (S A : ℕ) (b : ℕ) (t₀ : ℕ), 0 < A ∧ ∀ t, max 1 t₀ ≤ t →
        ∃ C : Circuit (ForrelationCoord k t), CircuitRealises C (P k t) ∧
          C.size ≤ S * mValue t * (2 * t) ^ 2 ∧
          (Q (totalise (Fkm k t C)) : ℝ) ≤ (A : ℝ) * 2 ^ t * (2 * (t : ℝ)) ^ b ∧
          Gvalue (mValue t) (Lvalue k t) < R (totalise (Fkm k t C))
```

This is a verbatim source signature with the proof body omitted. It is not a new elaboration or a rerun. Its file hash is in the supplied `manifest.json`. The constants are chosen after `k` and before `t`; the circuit is chosen for each sufficiently large `t`; the same circuit occurs in both query bounds. The lower bound appears in the floor form. The inspector links to `Lvalue`, `Gvalue` and the floor-to-asymptotic declarations rather than silently replacing this displayed type with a differently worded theorem. [Packet: `repository/lean/QuarticQuery/Results/Unconditional.lean:23`; `repository/lean/QuarticQuery/Results/Exponent.lean`, `rpow_le_of_Gvalue_lt`; `repository/corpus/statements.json`, `claim-floor`, `eq-2`.]

The short signature `alphaTot_eq_four_unconditional : alphaTot = 4` is useful as a first view. Expanding it must expose `UniversalPower`, `RLe`, `QLe`, the bit oracle and all definitions those types use. It cannot remain an unexplained symbol beside a check mark.
<!-- /passage:fidelity-3 -->

## Evidence is attached to a relation

<!-- passage:fidelity-4 -->
The inspector displays:

1. **Statement agreement.** The reviewed relation between this exact paper record and this particular declaration. If only some clauses are covered, mark those clauses and give the residual claim in ordinary language.
2. **Open hypotheses.** Show the actual complete binder structure first. Distinguish mathematical assumptions still being supplied from ordinary quantified variables, and explain where any supplied hypothesis is discharged in the final theorem.
3. **Proof acceptance.** State the run, toolchain, source/dependency pin, export hashes and allowed axioms. The current packet reports local acceptance; it does not include the raw receipts or a fresh reproduction.
4. **Comparison.** Show the Challenge theorem, the Solution wrapper, their source dependencies and the Comparator verdict from the same run. “Comparison not recorded for this row” differs from “failed.”
5. **Route.** Explain whether the selected proof follows this part of the paper. A different proof of the same statement is useful evidence, but it does not certify omitted prose derivations.
6. **Headline use.** Show the selected declaration's membership in the recorded dependency closure and the root theorem. Keep this separate from exactness.

These are six separate facts. The display does not combine the best value of each field into a stronger claim than any one reviewed tie supports. For example, the row for Lemma 3.1 is exact and reached, but its exact state-level theorem is outside headline reach; the headline uses a partial sampler-level counterpart. The same issue occurs for the full randomized direct-product statement versus the deterministic instance consumed in the proof. [Packet: `repository/corpus/statements.json`, `lem-3.1`, `lem-4.1`; `repository/docs/statement_fidelity_review.md`, findings 4 and 6; `AUDIT_FINDINGS.json`, AUDIT-08.]
<!-- /passage:fidelity-4 -->

## Make the semantic risk inspectable

<!-- passage:fidelity-5 -->
A proof checker establishes consequences of definitions. Comparator checks that the Solution matches the independently compiled Challenge, including the relevant definitions. If both artifacts encode the wrong mathematical problem, their agreement does not identify that error. The reader needs a small, concrete set of questions at each definition. [Packet: `repository/docs/statement_evidence_contract.md`; `repository/docs/statement_fidelity_review.md`, “Definitions: what was tried and held”.]

| Definition | Question shown beside it | What the current source says |
| --- | --- | --- |
| `RLe`, `QLe` | Is the algorithm chosen before the input, and must it succeed on every required input? | Existential program choices precede the universal correctness condition. |
| `queryCap` | Are unfavorable random or measurement branches charged? | Query counts use a maximum over branches. |
| `bitOracle` | Is every input-dependent operation charged? | The input enters the quantum execution through the bit oracle. |
| `P` | Is a large negative correlation a zero input? | It is outside the promise unless the small-absolute-value test passes. |
| `CircuitRealises` | Are both domain membership and output value certified? | The domain output is true exactly on the promise, and the value output is correct there. |
| `WinsAt` | Does the winner's own cell point outward, and must the target bit be zero? | Its fourth conjunct says exactly that. |
| `addressedF` | Are malformed strings still inputs? | Every bit string is assigned a Boolean result. |
| `UniversalPower` | Is one constant required for every size and total function? | The constant is quantified before `n` and `f`. |

Each question links to the relevant source definition and to the AI review finding. A third-party reviewer can attach a comment to the exact definition hash and the exact paper clause. The review status states “AI review available; human review not reported.” It does not infer correctness from a title, a build count, or a prior AI review's conclusion.
<!-- /passage:fidelity-5 -->

## Handle the actual discrepancies in this packet

<!-- passage:fidelity-6 -->
The default headline remains the full unconditional result reported in the delivered snapshot. Historical review prose that calls the headline conditional is shown as an earlier review at its recorded pin. The current graph's stale `fidelity_review: not_run` string is retained in the raw data view and explained beside the actual review documents. [Packet: `repository/README.md`; `repository/docs/statement_fidelity_review.md`; `AUDIT_FINDINGS.json`, AUDIT-04 and AUDIT-05.]

Three examples deserve explicit treatment in the interface:

- **`claim-bs-to-L`.** The corpus calls its tie exact, although its declaration proves `L<R(P)` and the row states a different numerical comparison. Show “tie disputed: endpoint substituted for intermediate inequality.” The direct proof reaches `lem-2.1.i` without this paper step. Preserve the raw status and the audit finding. [AUDIT-01.]
- **Equation (19).** Highlight the stronger `2G/m²` inequality as the Lean conclusion, and leave the paper's `E Z/m` identity separately marked. Lean does not define that `Z` in this route. [AUDIT-09.]
- **Negative controls.** The visible outcome is “Comparator rejected this altered solution as expected.” The harness may record that test as `passed`. Do not display those wrong solutions as accepted proofs. [AUDIT-06.]

The map can switch between “paper argument” and “declarations used by the headline.” This is a switch between two relationships, with the same selected statement preserved. A paper edge is an authored dependency. A Lean edge is a recorded declaration dependency. The second view should expose when a paper step is bypassed, when several declarations jointly supply a statement, and when an exact supporting theorem is unused. It should never manufacture a single complete checked route by joining the two graphs indiscriminately.
<!-- /passage:fidelity-6 -->

## The compact evidence statement

<!-- passage:fidelity-7 -->
Use this factual statement once at the end of the main reading route, with details available on selection:

> The supplied snapshot reports an unconditional Lean proof of Theorem 1.1 and successful local Comparator checks, including rejection of the supplied wrong solutions. Some statements use different proofs from the preprint, and some explanatory correspondences are partial or unrecorded. AI agents have reviewed the definitions and the new lower-bound route; no person has yet reviewed them. This advisory inspected the supplied source and records and did not rerun Lean or Comparator.

The stored sentence should link to the exact snapshot, the run records, the route notes and the human-review status. “Unconditional” refers to mathematical hypotheses in the headline type. It does not mean that proof checking, interpretation of definitions, implementation trust or historical attribution have become assumption-free. [Packet: `repository/README.md`; `repository/lean/QuarticQuery/Results/Unconditional.lean`; `repository/corpus/statements.json`; `AUDIT_FINDINGS.json`.]
<!-- /passage:fidelity-7 -->
