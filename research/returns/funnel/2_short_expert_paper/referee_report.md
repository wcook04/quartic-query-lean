# Referee report and response

**Manuscript:** *The optimal exponent for randomized and quantum queries: a Lean formalisation*  
**Review date:** 2 November 2026  
**Review status:** AI review only. The mathematical reviewers, formal-evidence reviewer and authoring agent are all language-model agents. This is not a human referee report and not a new Lean execution.

## Referee assessment

The manuscript's central claim is well chosen: the optimal universal exponent is four, with the separating construction proved for each fixed parameter and with the required Forrelation input supplied inside the development. The main mechanism is mathematical and memorable. The outward pointers make the winner robust against arbitrary opponent addresses, while the tournament's drift uses pairwise complementarity without a ranking of nonwinners.

After the corrections below, this review found no remaining concrete mathematical defect in the construction, quantum algorithm, planted lower bound, fixed-parameter Forrelation argument or exponent calculation. That conclusion has a defined scope. The supplied execution evidence has not been reproduced here, the release-source pin is different from the recorded replay pin, and the formal specifications have received no human semantic review. A claim of independent formal reproduction would exceed this return's evidence.

The exposition is sufficiently detailed for a query-complexity expert to inspect the consequential steps. Its least self-contained passage was the biased decision-tree growth bound; the revision now includes its contraction increments, stopped-process threshold and exceptional-event recurrence. The source correspondence is useful because it does not let the final theorem stand in for proofs of every intermediate display.

## I. Material objections

### 1. The source pin is not the replay pin

The manuscript could easily create the impression that the supplied bytes were independently replayed. The trace's paranoid record is at `d42fb67a7e060fb5386867dadf20a5903df39141`, whereas the manifest names `c7e0c9161f0ad898889bd9166e7b354acd42188d`. The recorded staging command suggests documentation and evidence work, but no complete inter-commit diff is supplied. Full receipts and individual external-kernel logs are also absent.

**Required response:** Identify both pins, report the historical run as local and unsandboxed, and distinguish it from the fresh source audit. Do not describe manifest integrity as proof-source authentication or a current build. The revision does all of this in Section 7 and `SOURCE_AUDIT.md`. A future release should replay the exact released source and archive complete outputs.

### 2. Comparator does not independently invent the intended mathematics

The challenge files import Mathlib only and are independently compiled. Their vocabulary is nevertheless copied from the same specification as the solution. Byte identity is valuable for fixing what must be proved, but it cannot discover a shared mistaken encoding.

**Required response:** Explain what the query models quantify over, how queries are charged, and which bridges connect the algorithm's bit oracle with the imported phase-oracle result. Retain the residual semantic-review obligation. Sections 1 and 7 make these points, and the audit records the empty-coordinate and constant-on-promise cases. The word “independent” is never used to suggest independently authored models.

### 3. The fixed-parameter Forrelation theorem must not borrow the full published theorem's status

The checked endpoint is eventual `L<R(P)` for each fixed `k≥2` with the squared logarithmic denominator. It does not prove Bansal–Sinha's full quantitative statement in `k` and the distinguishing advantage. The corpus's `claim-bs-to-L` tie is wrong: the final lower-bound theorem is not a proof of a separate comparison between two numerical expressions.

**Required response:** State the exact weaker scope and provide its proof. Remove the false exact-proof attribution from the return's correspondence. Section 5 and the companion records comply. The independent route uses previously known Gaussian and decision-tree growth methods, with explicit Girish–Tal–Wu credit and no priority claim.

The literature review also found an unresolved displayed logarithmic comparison in Bansal–Sinha v3 Section 5.4. The audit gives the precise algebra and version. This is not a refutation of their theorem and is not used to cast doubt on the independent fixed-parameter proof. The manuscript does not claim a complete re-verification of the published stronger result.

### 4. Exact conditional sampling requires more than a success bound

A sampler that merely succeeds often could distort the candidate law and invalidate the drift calculation. Moreover, measuring just the candidate label does not make all garbage known, so it does not justify resetting the preparation for a retry.

**Required response:** Prove preservation of the successful state for the abstract amplification procedure and identify the exact conditional-label statement used in the compiled sampler. Describe the full computational-basis measurement before reset. The draft initially described only label measurement; that was a real error of exposition and is corrected. The interface difference between the abstract theorem and the final program is also retained in the gap file.

### 5. The hidden-zero induction must charge all worlds

The phrase “over those worlds” could restrict the query-cost sum to worlds in which the zero is found. That would not be the invariant being proved. Likewise, “outside the column” incorrectly groups address and cell queries with queries to the one-zero string.

**Required response:** Hold every datum except the selected string's zero position fixed; sum query counts over every world indexed by `U`; distinguish queries to `X_i` from all other coordinates. These corrections now appear in Section 4.3. The induction obtains the factor two under a worst-case global query cap and makes no sharp-attainment claim.

### 6. The zero endpoint of the Gaussian path needs joint symmetry

A multilinear extension need not be affine in an entire block. Nor does the vanishing mean of each odd Gaussian factor suffice when the factors might be dependent.

**Required response:** Use coordinatewise multilinearity and an actual coordinate reflection of the transformed Gaussian vector, whose joint law is preserved by orthogonality. Explain that later blocks depend on later independent vectors. The revised Section 5.2 gives precisely this argument. Its mean-value parameter is existential and may depend on the test function; it is not silently replaced by a shared parameter or an unproved integral identity.

### 7. The explicit growth and moment constants need a checkable derivation

The initial growth paragraph named the martingale method but did not show where the exceptional term came from. The moment paragraph similarly compressed the constant `1/18` into a reference to second moments.

**Required response:** Give the fresh-coordinate increment, stopping threshold, Azuma exponent and contraction-count recurrence. For the moment estimate, show the logarithmic tangent inequality and explain why Jensen works without independence of a coordinate and its Hadamard transform. Both additions are now in Section 5. No new displayed claim was introduced: the additions explain the existing advantage and moment displays.

### 8. Bibliographic accuracy is part of mathematical traceability

The first draft linked the cheat-sheet paper to arXiv:1506.04719, which is a different pointer-function paper. It also used an undefined Drucker reference label. The supplied extracted literature has numbering traps that could move theorem locators.

**Required response:** Verify titles, versions, authors and exact locators against primary sources. The ABK link is now arXiv:1511.01937v2; the Drucker link resolves; GTW uses the conference Lemma 9; BS uses arXiv v3 and its correct subject class. The BBHT page range follows the publisher. The BibTeX file parses successfully.

## II. Proof obligations pressed and satisfied

The following objections were tested during review. They were largely handled in the initial mathematical draft; they should not be presented as newly discovered errors.

1. **Off-promise opponents.** A genuine winner's successful decoding suffices to disqualify every rival. Every incoming pointer reads a one in its all-one string, regardless of the rival's address. Every nonwinner fails a local test at every address. The decoder's worst-case cap applies on unpromised inputs.

2. **Physical query cost.** The input includes physical bits for addresses, pointers and transcripts. Coherent access computes an address and then queries the corresponding bit. The circuit is input-independent between oracle calls. No word-sized free lookup is inserted.

3. **No nonwinner ordering.** The drift pairs `(i,j)` and `(j,i)` using complementarity. It requires neither transitivity nor a gap from one half among losing columns. The winner's unsampled weight remains large.

4. **History-dependent amplification.** Each stage is coupled to the ideal sampling law at its actual history. The error sum is bounded conditionally stage by stage. No independence assumption about failures is needed.

5. **Adaptive interleaving in the direct product.** At a query, only one weight factor is restricted and only that instance's budget decreases. Nonnegative common factors can be extracted, and the one-input recurrence absorbs both branches. Independent auxiliary information is fixed first and averaged afterwards.

6. **The nonheavy event.** The simulator stops before query `L+1` to its target instances. The proof bounds the joint event of nonheaviness and a correct cell encounter under the original input law. It does not condition the hard distribution on nonheaviness.

7. **Two different hard laws.** The Gaussian-rounded Forrelation distribution need not be promise-supported. The pointwise acceptance inequalities account for its off-promise inputs. The Section 4 hard distribution is obtained later by finite minimax and is promise-supported.

8. **Quantifier order.** A proposed exponent below four first determines a fixed `k`. That `k` determines constants and thresholds. Only then is `m` increased against an arbitrary proposed universal constant. The proof never requires bounds uniform in a growing `k`. Already `k=3` excludes a cubic universal bound.

## III. Changes actually made in response

| Draft issue | Revision made |
| --- | --- |
| Label-only measurement wording | Full basis measurement, known-state reset and conditional-label interface specified |
| Ambiguous cost sum | `S_U` explicitly sums over all worlds, including unsuccessful ones |
| Column/string ambiguity | The induction now distinguishes `X_i` queries from address, cell and other queries |
| Block-affinity claim | Replaced by coordinatewise multilinearity and Gaussian coordinate-reflection argument |
| Compressed growth step | Added polynomial contraction increment, stopping rule, Azuma tail and recurrence |
| Compressed positive moment | Added tangent-log bound, Jensen argument and normalization of squared path weights |
| Imported/local quartic-bound attribution | The local numerical theorem is described as derived through model bridges |
| Missing/incorrect links | Corrected Drucker label and ABK arXiv identifier; verified version-specific locators |
| Loose interpretation of budget recurrence | The no-extra-query option now explicitly permits any strategy using at most `q` queries |
| Defensive sharpness sentence | Replaced with the precise adaptive/repeated-query consequence; no sharpness claim is made |
| False and stale corpus evidence | Isolated the numerical implication with an empty Lean mapping; corrected theorem source/kind in the changes record |
| Uncompiled intermediate wrappers | Full proposed signatures supplied with explicit uncompiled status and statement-level gaps |

The final first page was rendered and inspected: it contains the exact headline theorem, its fixed-parameter bounds, the no-Forrelation-hypothesis status and the outward-pointer mechanism. The mathematical display identifiers, passage boundaries and bibliography were checked separately from the proof review.

## IV. What remains open after this review

The required future work is independent human review of the specification and argument, a replay at the exact release pin with complete receipts, and elaboration of the proposed statement-level wrappers if the team wants those displays individually registered in the formal corpus. The current source endpoint itself has no unresolved Forrelation premise.

This return supplies a review manuscript and traceable evidence records for the team's decision. It does not integrate changes into the repository, publish the work, claim author priority for known growth methods, or convert AI review into human approval.

