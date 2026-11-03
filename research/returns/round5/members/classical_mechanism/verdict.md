# Verdict: classical mechanism

**The planted-pair lower-bound proof survives this review. The drafts need substantive corrections before publication, principally to explanation, attribution and inspectability.** The first-difference coupling, erased-zero identity, capped simulator, joint-event bound, averaging over the planted column, and final randomized contradiction are sound in the proof passages examined. The stated finite examples and lower-bound constants check out, subject to completing one sampling rule.

The return contains **34 located findings: 23 revision items and 11 keeps**. None alleges a failure of the separation theorem. The three high-priority items concern a source conflation and two misleading descriptions of the central mechanism.

## Five changes that matter most

1. **Correct the Forrelation attribution (CM-001).** Separate Bansal–Sinha’s explicit Walsh-Hadamard result, SSW’s random-orthogonal rorrelation result, and the record’s deduction from SSW’s Fourier-growth theorem. SSW §1.8, p. 10 explicitly explains the distinction. Also qualify the exposition’s outward-pointer novelty claim (CM-008).

2. **State the right event from the start (CM-002–004).** Visiting a true cell can result from a lucky address guess. The direct product bounds “light and correct at this query time,” not success conditional on lightness. The overview must also retain the alternative of detecting the erased zero.

3. **Complete the probability model and its teaching examples (CM-005–007, CM-015, CM-017).** State mutual independence of the zero positions and address inputs. Restore the uniform fallback when the four-column example finds no zero, an event of probability (81/256). Distinguish separate worst-case caps, a pooled budget, and conditioning on cheap runs. Use the existing record’s examples and exact Drucker/Shaltiel locators.

4. **Make auxiliary formal statements inspectable (CM-009–012, CM-021).** Distinguish the finite-seed formal theorem from the ordinary reduction covering arbitrary independent randomness. Expose the definitions behind `compliantSuccess`, `hitProbability` and `expectedCount`; identify helper invariants as such. The advertised full-proof link should enter the full classical argument.

5. **Repair the delivered reading path (CM-013–016, CM-019–020).** Two subsection headings render as raw Markdown. Three SVG sources are missing although the PDF pictures exist. Move the minimax proof behind the mechanism or its precise record link, and give the second AND example a distinct teaching purpose.

## Keep

Preserve the two-event coupling, identity-before-estimate order, explicit whole-run independence, short unnormalized direct-product proof, total-cap-to-separate-caps reduction, same-circuit conclusion, and fixed-k quantifier order. The history arithmetic and headline Lean statement guide are substantial improvements. The numerical constants need no repair on the checks performed.

**Scope:** source-based mathematical and editorial review; no manuscript rewrite, new result, Lean compilation or Comparator execution. Sources and reading limits are listed in `source_coverage.md`; findings carry exact locators and citations.
