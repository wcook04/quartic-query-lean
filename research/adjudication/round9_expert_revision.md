# Round-nine expert-companion revision

The companion now carries the fixed-parameter exponent proof and the uniform
single-family deduction as visibly different arguments. Its central reductions
have usable local contracts: the tournament proposition fixes its stage/error
regime before the input, and the direct-product lemma includes the one-instance
hard-law premise and integer caps. The simulator proof identifies its two clocks,
its halt/default branch, the original product law and the terminal-to-prefix
implication. No Lean source was changed, and these editorial checks are not a new
Lean or Comparator run.

## Findings and manuscript changes

The [individual dispositions](round9_dispositions/expert_companion.json) cover all
166 XP9 findings, plus 58 supporting-account observations returned by the record
and exposition reviews. Each row preserves the baseline locator and gives an
exact revised quote and location. The 50 record observations and eight exposition
observations are historical cross-checks, not 58 additional newly discovered
faults. Record-only consequences of prior XP083, XP088 and XP095 remain assigned
to the corresponding record findings; XP196 concerns the exposition and is owned
by that manuscript's revision.

The largest repairs concern the actual inferences:

- The abstract identifies fixed Forrelation order and the separate uniform
  schedule. Taking order three excludes every power below 10/3; the logarithmic
  losses are not silently removed.
- The construction separates decoder and exact-domain-circuit contracts from
  their sketches. It gives the decoder threshold, retained registers, gate
  convention, transcript ordering, total pointer decoding, encoding length and
  local-test query cap where those objects enter.
- Proposition 3 states its actual `T` and `epsilon` choices. The proof indexes
  terminal weight, gives the miss-event inclusion used by Markov, specifies the
  empty history, and writes the real transition mass before coupling. The
  two-pivot example shows multiplication into an existing fractional weight.
- Lemma 5 now states its premise locally. Its proof fixes independent information
  before conditioning on a transcript, gives the product-law invariant, the leaf
  bound and the positive-allowance query case. The alternative Drucker theorem
  is instantiated with its actual expression `(2^(1/r) beta)^r = 2 beta^r`.
- The planted-cell bound displays the light-hit event before the column average
  and time union. The contradiction names its three error terms, justifies
  averaging randomized trees, and supplies the two floor inequalities.
- The uniform section connects the depth estimate to randomized acceptance
  probabilities and includes the amplified cap and the incompatible gap margins.
  Its growing-family consequence changes to `L=floor X` explicitly, states both
  uniform complexity bounds, and explains why both complexities diverge.
- The formal account distinguishes fixed-order comparison evidence, built-only
  quantitative results, an ordinary growing-family deduction, and the measured
  label versus retained-state interfaces. It identifies the historical receipt
  without claiming new execution.

Four suggestions are deliberately not adopted as proposed. The existing
fixed-edge comparisons suffice without adding another king-finding citation;
the reusable amplification lemma stays before its applications; the concise
minimax attainment clause remains useful at the strict threshold; and no
unverified personal-responsibility declaration is invented for the named author.
The factual AI disclosure is preserved and repeated tersely in a first-page
footnote. The contribution's two operations appear together in the first-page
abstract; the fuller contribution paragraph follows the theorem on page two.
That is an explicit alternative to moving the entire paragraph onto page one.

## Writing sources applied

These are passage-level adaptations, not a numerical style ranking or a claim
that an exemplar proves the quartic argument. The packet's local source files
were inspected; review descriptions alone did not supply the following choices.

| Inspected source passage | Editorial operation applied here |
| --- | --- |
| Drucker, *Improved Direct Product Theorems for Randomized Query Complexity*, arXiv:1005.0644v2, introduction and §3, especially the separation of resource assumptions from success guarantees | Lemma 5 states the one-instance premise and separate all-branch caps before its proof. The alternative global-budget theorem has a visible parameter substitution, so the two resource contracts cannot be mistaken for one another. |
| Brassard–Høyer–Mosca–Tapp, *Quantum Amplitude Amplification and Estimation*, arXiv:quant-ph/0005055v1, §2, Lemma 1 and Theorems 2–3 | Lemma 2 first identifies the invariant successful direction, then the finite trial schedule. The expected-cost QSearch statement stays next to, and distinct from, the all-branch cap used here. |
| Aaronson–Ben-David–Kothari, *Separations in Query Complexity Using Cheat Sheets*, arXiv:1511.01937v2, §§3.1–3.2 | The history presents what the certificate allows the algorithm to do before its cost pair; the two randomized transfers are named separately. The new construction is compared at matched supplier scale. |
| Supplied short-paper exemplar, *Full Support and Positive Density in the Zero-Temperature SK Model*, abstract and §1 through the main theorem | The abstract distinguishes inherited result, reconstructed mechanism and further consequence. The theorem heading attaches attribution and reconstructed constants to their respective roles; a later optional consequence does not silently become the main proof's conclusion. |
| `lean-exposition/skills/long-to-short/SKILL.md`, reader model and omitted-proof procedure; `docs/authoring.md`, assumption/citation tracking | Keep the sampler and capped predictor as the specialist paper's two explanatory tasks. Link the floor calculation, uniform bound, trial estimate and retained-state argument to the actual different destinations that supply them. |

The edition-sensitive bibliography entries now identify the inspected arXiv or
ECCC version while retaining journal metadata. In particular, the AA projection
and interference locators refer to arXiv v1; Drucker's locators refer to v2;
Shaltiel's fair-tree locators refer to ECCC TR01-009. This records source identity,
not fresh research priority or independent verification.

## Figures and validation

The two existing TikZ sources were adapted. Figure 1 labels the enlarged address
inputs as belonging to the winner. Figure 2 uses one shared sampled address-array
label with arrows into both panels and identifies the filled cell's transcripts
and pointers. The diagrams retain their schematic and small-instance scope.
Their SVG projections are regenerated by the existing paper renderer.

The 18-page provisional export was inspected page by page in contact sheets and
at larger size at the figures, direct-product calculation and uniform-bound
transition. The added resource-accounting displays and bibliography fit without
overfull boxes. The section-3 opening and the two-clock sentence remain intact
on their pages. The contribution is complete in the first-page abstract. The
receiving editor owns the final source-link pin, final export and repository-wide
checks; the final round-nine validation receipt records that delivered edition.

Authoring checks resolved every record fragment used by the revised companion,
checked source text for control characters and unmatched inline-math delimiters,
and compared the new finite constants and proof steps to their record and source
arguments. One intermediate scripted draft introduced a carriage-return escape
in a formula and another copied the wrong alternative direct-product expression;
both were caught and corrected before the delivered disposition snapshot. The
lesson is to treat mathematical replacement strings as code, inspect rendered
formulas, and recheck a cited theorem's actual substitution rather than relying
on the reviewer paraphrase. No new mathematical result or formal evidence is
inferred from these repairs.
