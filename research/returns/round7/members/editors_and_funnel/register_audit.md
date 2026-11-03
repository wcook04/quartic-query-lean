# Register measurement: useful prompts, unreliable verdicts

## What was examined

This audit reads `register/measurement.txt`, its numeric JSON, the 42-document profile, the rules, all five production skills and `reader_principles.md`. It does not rerun the profiler or infer an unobserved change in reader understanding. The three reported measurements describe the supplied files. Their labels and specimens can be checked against those files; no new software instrumentation is needed to identify the issues below.

The register stage's most useful principle is already explicit: a detector directs attention and cannot pass a paper. That distinction should govern the revision. The manuscripts have low or zero scores for several disfavoured words and still contain difficult sequencing, an audience mismatch, inaccurate local statements and stale navigation. Removing another semicolon cannot repair those problems.

## 1. The report's phrase “outside the literature range” overstates what its flag means

The JSON distinguishes `outside`, a threshold on distance from the corpus median, from `beyond_corpus`, an observation outside the corpus minimum and maximum. The text prints “outside the literature range” for the former. These are different tests. For example:

| Draft and feature | Draft value | Corpus minimum–maximum | Reported distance | Outside observed range? |
| --- | ---: | ---: | ---: | --- |
| Expert: mean paragraph length | 96.14 | 15.23–105.35 | +2.62 | No |
| Expert: triads per 1,000 words | 1.94 | 0–3.09 | +1.92 | No |
| Exposition: semicolons per 1,000 words | 6.96 | 0–58.74 | +2.33 | No |
| Exposition: “we” per 1,000 words | 4.53 | 1.00–34.89 | −1.54 | No |
| Record: heading rate | 5.65 | 0–5.66 | +1.95 | No |
| Record: negation rate | 8.84 | 1.13–9.27 | +1.76 | No |

The text reports 4, 4 and 6 threshold flags for the expert paper, exposition and record. Only 2, 1 and 2 features respectively lie beyond the observed minimum–maximum range. Neither count is a quality score. Rename the threshold label, retain both measures and explain the units. In particular, an IQR-scaled distance is neither a standard-deviation z score nor a probability of bad writing. Where the IQR is floored, the number is measured against the chosen floor, as the report itself acknowledges.

## 2. The comparison population does not represent three distinct reader tasks

All three drafts use the same profile. It contains research articles, a substantial lecture-note text, short notes and QIP slides. The metadata also includes two versions of the Ambainis–Iraids–Kokainis certificate-complexity paper as separate documents (`quartic-lit-ambainis-iraids-kokainis-certificate-v3` and `quartic-ref-05-near-optimal-separations-of-certificate-co`). Thus 42 is a count of profile entries, not necessarily 42 independent works.

Those entries can all inform reading. They should not silently have the same editorial role. An exposition's questions, pedagogical reminders and worked calculations serve a different purpose from a research abstract. A record with a statement catalogue and an evidence appendix also differs from an ordinary article. Compare matched genres and matched regions first; show the mixed corpus as a secondary descriptive view. Group multiple editions of the same work, choose a declared edition for the baseline, and preserve version differences for source comparison. This is a refinement of the existing instruction to select the closest genre, not a reason to enlarge the corpus indiscriminately.

The profile is not a test of whether a teaching move succeeds. Finding a move in papers from several fields shows that the move occurs there. It does not show that adding it improves this text. `skills/register-stage.md` should distinguish these two forms of evidence when it describes cross-field testing.

## 3. Where the detectors agree with close reading

**Paragraph length is a productive warning.** The expert introduction's contribution paragraph at line 31 combines constants, thresholds, the common circuit, counterexamples, two methodological observations, a uniform bound and Lean. The exposition's amplification paragraph at line 179 carries the successful-state law, two probability regimes, the random iteration count, two numerical success bounds, the repetition count and the worst-case conclusion. Both need fewer simultaneous obligations. The problem is visible without choosing a target mean length.

**Semicolon density identifies some difficult joins.** In the exposition, the local-test inventory at line 106 and the long introductory model sentence need examination at reading size. Several semicolons join changes of task or variables. Splitting at those changes can help. Semicolons that separate the four parallel winning conditions at line 88, however, improve parsing; replacing those mechanically would damage the sentence.

**Low variation can support an impression of uniform pacing.** The expert paper repeatedly opens a paragraph with a small conclusion and follows it with several qualifications. The reader gets little visual distinction between the decisive construction-specific reasoning and a supporting refinement. Varying paragraph roles and section weight will naturally vary rhythm. Deliberately engineering a numerical coefficient of variation would not establish that improvement.

**Some formal material still interrupts the main argument.** This is a placement issue in the long record, particularly when implementation terminology enters an ordinary mathematical derivation. The location matters more than the total word count. A dedicated evidence appendix may properly contain many technical names.

## 4. Where the detectors flag useful material

| Detector and supplied specimen | Editorial judgment | Better treatment |
| --- | --- | --- |
| Expert status vocabulary: “The formal upper bound uses the measured form of Lemma 2” in §7 | The relation between implementations is mathematically consequential. | Preserve the distinction; improve its sentence shape and destination. |
| Expert triads: “Aaronson, Ben-David and Kothari” | Three authors' names are attribution, not a rhythmic vice. | Exempt author lists and citations before proposing a prose repair. |
| Exposition intensifier: “every transcript” or “exactly when” | Universal scope and equivalence are the mathematics. | Classify logical force separately from empty emphasis. |
| Exposition semicolons in the four winning conditions | Four parallel clauses define one conjunction. | Retain or format for comprehension; do not optimize a punctuation count. |
| Record apparatus specimens from G.2 and G.7 | These sections exist to expose formal interfaces. | Score body and evidence apparatus separately. |
| Record heading rate from Appendix B | A searchable catalogue needs many short destinations. | Exclude the catalogue from body-navigation judgments, while reviewing its labels for clarity. |
| Negation: an off-promise input has no required answer | This prevents a false interpretation of totalization. | Keep the negative fact beside the relevant operation. |
| Low “we” rate | Impersonal definitions and theorem statements may be appropriate. | Introduce a reader-inclusive “we” only for an actual calculation or choice. |

The first status-vocabulary specimens are often simply “Lean,” “formalisation,” “record” or a reference to a proof destination. A blanket instruction to lower that score conflicts with the task of making support inspectable. Distinguish repetitive self-advertisement from a useful link or a mathematical restriction.

## 5. What the measurements miss

The report records an exposition mean sentence length of 19.2 words, close to the corpus median of 19.3. That does not detect the missing operational bridge from a bit oracle to phase kickback, the sudden use of an inverse coherent preparation, or the unannounced change from a deterministic teaching board to a probability distribution. The hardest paragraph may consist of short sentences whose prerequisites have not been taught.

The measurements also miss the difference between an upper cap chosen in advance and a realized number of queries, the toy-size hard-distribution wording, and the exercise's distinction between excluding an endpoint exponent and lower-bounding an infimum. They miss a four-column figure drawn with eight-bit strings. They miss return pointers whose anchors exist but whose displayed section numbers name a different section. These are reader-facing defects, not matters of cadence.

The profiler's own specimens show another limitation: the expert paragraph-variation list includes its YAML front matter. Before treating a prose statistic as comparable, inspect what text was counted, whether display mathematics was joined across paragraphs, and whether captions, references, catalogue rows and code were separated. The packet does not contain the profiler implementation, so this audit diagnoses the visible specimen and recommends checking the extraction; it does not claim to have found the exact parser defect.

## 6. A better way to use the existing stage

Keep the paragraph-by-paragraph reading requirement. For each paragraph, record the reader's local goal, the operation they can now perform, and any actual difficulty. The disposition may be retain, shorten, move, split or explain. A useful sentence does not need replacement merely to demonstrate effort. This preserves the user's demand that every sentence receive attention while reducing revisions that change meaning without improving comprehension.

Let the numerical report nominate passages for inspection. Require an editorial reason tied to a specific reader before making a change. Evaluate the revised passage against that reason, then check that formulas, hypotheses, probability conditioning, quantified witnesses and link destinations still match. Changes in an aggregate metric are secondary observations.

For this packet, the highest-value check is an unassisted reconstruction task: can the intended reader explain why an off-promise rival cannot defeat a true winner, why the list still needs verification, and why a cell query counts as an address prediction without assuming that the address was first computed? The current four-column example and capped simulator make those tasks possible. They should drive the next revision.

## 7. The exported method is incomplete as an inventory

The register skill and its stage guide describe 26 rules. The supplied `register_rules.json` and human-readable rules contain 17: RG-01, RG-02, RG-06, RG-09, RG-11, RG-13, RG-14, RG-15, RG-16, RG-17, RG-18, RG-19, RG-20, RG-21, RG-22, RG-24 and RG-26. Missing are RG-03, RG-04, RG-05, RG-07, RG-08, RG-10, RG-12, RG-23 and RG-25. Several absent IDs are referenced by the skills or measured features. Supply the referenced rules or identify this as a selected export. This internal mismatch does not imply archive corruption; all supplied payload hashes match the input manifest.
