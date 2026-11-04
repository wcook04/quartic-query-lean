# Final adversarial quality check

## Scope and status

This is a model-emulated handling-editor quality pass on the integrated review, not a new independent referee report or a proof certification. I read all 174 accepted findings in the version of `output/return/feedback.json` inspected during this pass, including the consolidated comments, the full `feedback_by_document.md`, and `work/assemble_review.py`. The assembler at that point reported 220 candidate observations, 43 merged duplicate candidates and 3 rejected candidates. The parent is still revising the package, so **source finding IDs below are authoritative; XP9 numbers describe this inspected version only**.

I checked the most consequential claims against the current expert companion and the relevant current reasoning-record passages, especially the conditional sampler, local-test guard, simulator, growing-parameter budget and formal correspondence. I did not rerun Lean or Comparator, reconstruct the Gaussian estimates, inspect every external source again, or perform a new literature search. After the parent authorized a narrow narrative cleanup, I changed only the §5 paragraph in `feedback_by_document.md` that retained the withdrawn blanket provenance criticism. All other root-owned deliverables were left to central assembly.

## Parent disposition

The parent accepted the following cleanup after this report was drafted: drop **R013, Q048, C019, Q042 and E058**; retain the earlier rejection of **E053/Q056** and removal of **C054**; reduce **Q062** to low-severity receipt navigation; merge **E039/Q047**, **E024/Q004/Q015/C014**, and **Q043/E037**. The explanations below record the evidence for those decisions. The parent subsequently reported central assembly at166 accepted findings and8 rejected candidates; final XP9 numbering and all derived references remain centrally generated.

## Corrections before packaging

### 1. Remove the false first-stage-failure premise in Q048

**Inspected item:** XP9-091, Q048, expert companion line169.

The finding says the candidate list can be empty because the first bounded sampling attempt can fail. That premise is false for the actual construction supplied in the paper. At history length zero the preparation in (9) has an empty product of comparison successes, so its success probability is one. In the specified Lemma2 implementation, both the direct-measurement branch and every Grover-iteration branch then succeed. The first pivot is therefore returned. Later sampling failure returns a list that already contains that pivot.

The bare failure-upper-bound contract in Lemma2 permits an unnecessarily weaker implementation, but that does not make such failure a reachable branch of the stated implementation. Moreover “accept if any candidate is accepted” already gives the usual Boolean existential decision rule. **Preferred disposition: drop Q048.** If a complete output convention is still requested, frame it as optional specification style and remove the false claim about a reachable empty first-stage list.

### 2. Drop C019: the requested guard and implication are already present

**Inspected item:** XP9-054, C019, expert companion lines110–114.

The finding treats “the event that i wins and s=s_i” as an unguarded use of a partial address. Winning already requires all address blocks to be promised; the displayed event restricts to that winning domain before using its address. This is a conventional guarded mathematical predicate, not a need to assign an arbitrary address off promise.

More decisively, the proposed alternative repair is already in the same paragraph: consistency and the output tests force every P(A_i,h) to be defined and equal s_h, followed by the conclusion that a nonwinner fails some test for every proposed address. The local all-input soundness contract is therefore already explicit. **Preferred disposition: drop C019 rather than presenting it as a missing hypothesis.**

### 3. Drop R013: both the lead text and its exact destination identify ordinary transport

**Inspected item:** XP9-162, R013, expert companion line339; reasoning record lines6354–6385, `#CL-direct-product-formal`.

The lead text explicitly says “The record proves in ordinary mathematics” and the preceding sentence restricts the formal statement to finite weighted seeds. The exact record destination says that recursive-compliance/count equivalence is not a Lean theorem, explains the ordinary induction, and says arbitrary measurable randomness is handled by the ordinary finite-behavior reduction, not a Lean theorem. It also identifies the generic truncation corollary and combined identity as ordinary deductions.

The finding's requested formal-versus-ordinary scope distinction is already available both at first use and at the destination. A generic possibility that a reader might skim past it is not an additional defect. **Preferred disposition: drop R013.** This does not affect the separate, concrete C062 specialization of the cap-event result to the always-capped simulator.

### 4. Finish removing the general §6 provenance complaint

**Inspected items:** E053/Q056 (already rejected in the inspected assembler), E058/XP9-145; narrative §5.

Dropping E053/Q056 and C054 is warranted. Line297 identifies a reconstruction imported from record §§3.6–3.15; line302 disclaims dominance and priority; line304 credits the Gaussian chain and identifies the changed truncation and newly proved moments; line323 supplies the detailed comparison. This is enough to identify the optional estimate as reconstructed work supplied by the record.

E058's stronger explanation that a reader “cannot assign proof ownership” at the departure is inconsistent with those preceding sentences. **Preferred disposition: drop E058**, rather than add another credit inventory at the start of the section. The distinct issues about the definition of ν1, the exact shallow-tree destination, convex mixtures, amplified depth and the changed allowance L remain concrete.

The narrative's phrase **“half-proved quantitative claim”** revives the rejected blanket completeness complaint. Replace it with the actual inference costs, for example: “Keep the imported bound's role explicit and show the mixture, amplified-depth and changed-budget transitions needed for its stated application.” No new analytic proof or novelty claim is required.

## Consistency and proportionality repairs

### 5. Treat Q042 consistently with the rejection of E030

**Inspected item:** XP9-083, Q042, line159.

The assembler rejects E030 because Lemma2 already supplies the p=0 endpoint. Q042 requests essentially the same zero-conditioning convention at the weighted-sampling application. Before line159, Lemma2 says p=0 gives certain failure; the operational description at line145 says failure returns the accumulated list; and the ideal process at line147 explicitly makes zero weight absorbing. Line159 states the label law conditional on success.

A local W>0 qualification can be harmless, but the endpoint and stopping behavior are not missing. **Recommendation: drop Q042 for consistency**, or clearly mark it as optional local notation rather than a separate algorithmic gap.

### 6. Reduce Q062 to receipt navigation, without implying a source-integrity problem

**Inspected item:** XP9-152, Q062, line333.

The mathematical present tense “Comparator checks” does not by itself claim that this prose revision was freshly or independently rerun. The root's reported comparison of all70 receipt-bound source hashes with the packaged files supports source agreement with the historical checking evidence. A date and revision at the evidence landing point can still help navigation.

Suggested scope: **low severity**, “Make the receipt date and source revision easy to find at the existing audit destination.” Remove the implication that the present-tense theorem statement suggests a fresh independent review, and do not describe a build or proof gap. The existing instruction not to request a rerun should remain.

### 7. Merge three remaining same-repair clusters

These are actionable observations, but separate counts obscure the repair unit.

| Current source IDs | Inspected XP9 items | One consolidated repair |
|---|---|---|
| Q047 + E039 | 089 + 090 | Separate the failed-test/amplifier/candidate polarity and state the accept/reject rule. The h/K two-case display is an implementation suggestion for the same paragraph repair. |
| E024/Q004 + Q015/C014 | 046 + 047 | Attribute the explicit coefficient200 to the chosen reconstruction and attach its precise gate-count destination. Keep Q014's gate-basis convention separate because it adds a different missing assumption behind the numerical coefficient. |
| Q043 + E037 | 084 + 085 | Reformat the two-stage example so the old-weight multiplication (2/3)(2/5)=4/15 appears beside the second update. A table and the product are compatible parts of one example repair. |

These merges should preserve useful secondary wording and source IDs, not inflate the number of independent mathematical problems.

## Consequential claims checked during this pass

The following checks delimit the corrections above; they are not additional review findings.

- **A.3 dominance:** The integrated narrative and E067/Q066 correctly resolve the earlier rejected concern. Every rival pointer reads one in all-one column1. Its own read is zero or one. Both (0,1) and (1,1) select column1 because it wins ties. No decoder-correctness premise is needed.
- **Growing k:** The integrated C060/E059/Q057/Q060 finding correctly treats the old-threshold mismatch as a missing local allowance switch, not an inconsistent theorem. The record takes X=(2/18225)m^(1−1/k)/(k² ln(4km)), L=floor X, and obtains R>m^(2−1/k)/(1822500 k² ln(4km)). The exact coefficient in the advice is correct.
- **Sampling law:** The narrative distinguishes exact conditional labels, history-dependent success and a stopped stagewise coupling. It does not incorrectly condition the whole completed process on universal success. The numerical two-stage example agrees with the stated weights and probabilities.
- **Amplification cutoff:** E031/Q026 is an explicitness request, not a disproof of asymptotic existence. The secondary comment correctly acknowledges that an O-cutoff description can serve an existence sketch. Preserve that qualification when presenting the merged finding.
- **Verifier semantics:** Accepting a false candidate on a one-input still gives the correct Boolean output. The narrative preserves this distinction. The no-defect-found outcome is not represented as an exact certificate.
- **Classical event:** The simulator has a total cap L on all target address blocks, hence cap L on each. Its true-cell-hit/lightness event is bounded under the original law, not a conditioned hard distribution. No extra factor m is required after the independent-label average. The early-halt fallback finding is supported by the lead text's missing case.
- **Parity example:** E070/Q067/C065 identifies a real omitted local input law. Independence across two instances alone does not imply the one-query parity optimum1/2; uniform inputs are required.
- **Formal output interfaces:** Q063 and Q064 are supported by record AppendixG.7. The abstract opaque retained-factor statement is distinct from the compiled measured-label law; the unproved stronger physical-subsystem transport is not a premise of the headline upper bound. The bounded-list theorem exists as a separately built counterpart, while headline roots use measured labels and Boolean continuation. The review does not call either a missing headline proof.
- **Specification placeholders and links:** The narrative treats intentional statement-file `sorry` placeholders as specification syntax paired with separately compiled proofs. It does not call older pinned links broken solely because their current packaged bytes differ. `LINK_MAP.json` does record the pinned/current byte distinction, so that evidence attribution is supported.

## Assembly and reading-claim checks

The inspected JSON has 174 unique accepted IDs, and every primary quoted locator is an exact substring of its stated current source lines. The inspected count identity is consistent:220−43−3=174. The assembler preserves source IDs when merging and includes an explicit rejected-hypothesis disposition for A.3.

The narrative's limitations are appropriately bounded: no new Lean/Comparator execution, no independent proof of every analytic estimate, and no full supporting-record/exposition review. Its frozen-pass statement distinguishes reconstructed unit annotations from a literal timestamped diary. No claim of human referees or independent blind reviewers should be added during final packaging.

The in-progress `feedback.json` has an empty `sources_read` list. Before delivery, populate it from the actual source registers or provide an unambiguous reference to the packaged register; do not let an empty field masquerade as completed source accounting. Regenerate derived counts, IDs, coverage, verdict references and adjudication after the final removals and merges.

No new finding is recommended to replace the removed observations. The package should become shorter and more accurate.

## Authorized final narrative cleanup

After central adjudication, I searched `feedback_by_document.md` specifically for remnants of C019, Q048, Q042, R013 and E058. The narrative did not assert an undefined unguarded address, a reachable failed first-stage empty list, a missing zero-weight stop convention, or a missing ordinary-versus-formal distinction. The §5 paragraph still framed the optional estimate as needing a general claim boundary. I replaced only that paragraph with the surviving concrete actions: define ν1 and link its construction, target equation(F33), identify the truncation’s operative property, and expose the averaged-acceptance/amplified-depth connection. This removes the withdrawn provenance premise without discarding the supported local dependency findings. No additional findings or literature searches were added.


## Final counting note

The final assembly contains 166 distinct actions from 219 submitted candidates: 46 duplicate candidates were consolidated and 7 were rejected centrally. C019 was withdrawn by its originating lens before final assembly, together with C023 and C054. Earlier references to eight central rejections included C019 before that withdrawal; the final machine-readable counts govern.
