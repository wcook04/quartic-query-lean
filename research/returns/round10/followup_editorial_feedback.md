Overall, I’d give it about 8/10 for technical mathematical writing. It is a serious, carefully structured research companion, and considerably stronger than a typical AI-generated mathematical exposition. But I wouldn't yet call it an exceptionally polished paper.

My assessment, having read the full 18 pages:

| Dimension                                 | Score  |
| ----------------------------------------- | ------ |
| Mathematical precision of exposition      | 9/10   |
| Logical organization                      | 8.5/10 |
| Technical prose                           | 8.5/10 |
| Pedagogical clarity                       | 6.5/10 |
| Attribution and scholarly positioning     | 8/10   |
| Visual presentation                       | 8/10   |
| Readiness for external expert circulation | 7.5/10 |

These scores concern the writing and presentation, not an independent verification of every proof.

## What is particularly strong

1\. It is unusually precise. The paper consistently distinguishes assumptions, proof obligations, conclusions, and verification status. For example, the randomized lower-bound argument in §4 carefully separates the original probability law from the truncated predictor. This is exactly the sort of distinction specialists look for.

2\. The mathematical architecture is good. The progression from construction (§2), to quantum upper bound (§3), to randomized lower bound (§4), to exponent (§5), is coherent. The two key mechanisms—the probabilistic tournament and the capped address predictor—are correctly given substantial prominence.

3\. It avoids vague claims. The treatment of the Lean development on pages 12–13 distinguishes compared statements, separately built proofs, and ordinary deductions rather than presenting everything as equally verified. That is an important credibility strength.&#x20;

expert_companion.pdf



4\. The counterexamples are excellent editorial choices. Appendix A anticipates natural but invalid simplifications. That makes the exposition more convincing and valuable to a reader attempting to reconstruct the arguments.

## What prevents it being a 9/10

The biggest problem is conceptual compression. Almost every sentence is doing mathematical work, but readers are frequently asked to absorb several new concepts before understanding why they matter.

For example, the abstract describes the capped address predictor, truncation, and preservation of the original input law before the reader has encountered the planted-input construction. These are important ideas, but their significance is not immediately apparent.&#x20;

expert_companion.pdf



The paper also mixes three purposes: explaining OpenAI's theorem, providing a detailed proof reconstruction, and reporting Lean verification. All three are worthwhile, but their relationship could be clearer at the beginning.

There is also a concrete navigation issue: pages 12–13 refer to Appendix G, although this PDF contains only Appendices A–D. The links point to the separate reasoning record, but the text should explicitly say Appendix G of the reasoning record. A specialist reading the PDF offline could reasonably think material is missing.

Finally, the title is slightly risky. The main theorem is clearly attributed to OpenAI in the body, but the headline could initially suggest that the author is announcing the result. For a reconstruction, the provenance should be unmistakable from the title itself.

## The three changes I would prioritize

1\. Make the contribution unmistakable. Explain in the first half-page exactly what OpenAI established, what this companion reconstructs, and what the formalization additionally establishes. A title such as Reconstructing the nearly quartic randomized–quantum query separation would help.

2\. Add a genuinely intuitive proof roadmap. Before the formal construction, explain in approximately 250 words why a winning column is cheap to locate quantumly, why its hard-to-find address obstructs classical algorithms, and how these two features produce the fourth power. Figure 1 is helpful, but it does not entirely replace this explanation.

3\. Simplify the main narrative. Keep the crucial hypotheses and proofs, but move more constants, implementation details, and verification bookkeeping into supporting material. In particular, the optional uniform refinement in §6 interrupts the natural progression from the headline theorem to its formal verification.

## My overall judgement

For a specialist in quantum query complexity, the writing is already credible and worth reading. It does not have the usual problems of generic AI writing: empty transitions, inflated claims of novelty, or explanations that conceal the assumptions.

Its weakness is almost the opposite: it is so intent on being exact that it sometimes neglects the reader's developing understanding.

The best mathematical exposition makes a difficult result feel inevitable after the reader has understood it. This paper makes the result feel carefully justified, but not yet inevitable.

I think a focused editorial revision could bring it from 8/10 to 9/10 without changing the mathematical substance. The opportunity is primarily to improve hierarchy, motivation, and the clarity of the paper's contribution—not to add more technical detail.