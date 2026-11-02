## Your job: the short expert paper (exposition; claims limited to what the evidence supports)

Write a short paper, about 6,000 to 9,000 words, for experts in query complexity. Its subject is the formalisation of the nearly quartic separation and what the formal work revealed about the argument. Title it by the strongest thing it settles.

1. Page one states Theorem 1.1 exactly and that it is checked in Lean with no hypothesis, then the one idea worth remembering, stated as a mechanism: why outward pointers let a genuine winner beat opponents whose address instances are off the promise, and why the probabilistic tournament needs no ordering of non-winners.
2. Give the proof at the level an expert checks it: the construction, the quantum upper bound (the tournament, exact conditional sampling under amplification, and verification), the classical lower bound (the planted coupling, the joint-event simulator, the capped direct product), and the optimal power with its quantifier order. Spend the most space on the hardest steps.
3. A section on the Forrelation lower bound by the new route, for fixed k: what it proves, what it does not prove relative to Bansal and Sinha's Theorem 1.3, and what is already known (`docs/forrelation_route_prior_art.md`: the growth bound follows Girish, Tal and Wu). Make no priority claim beyond what that search supports.
4. A section on what formalisation changed: the corrected statements (`research/returns/adjudication_notes.md`), the sharper constant `2G/m²`, the sub-distribution proof of Lemma 4.1, the decision-tree form of Lemma 2.2(i), and the model choices Comparator fixes, with the residual risk that a definition says something other than intended.
5. State exactly what is verified and how: kernel checking, Comparator statement identity, unsandboxed runs, AI-only review. A reader should be able to reproduce the check from the paper.

## Return one ZIP containing

- `paper.md`: the paper, with `<!-- passage:NAME -->` anchors; `references.bib`.
- `correspondence.json`, `NEW_STATEMENTS.json`, `STATEMENT_CHANGES.json`, `LEAN_GAPS.md` as specified above.
- `referee_report.md`: a hostile referee report on your own draft, then a list of the changes you made in response.
