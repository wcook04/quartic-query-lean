# Sources, attribution, and evidence

## P1. The mathematical statement under review

**OpenAI.** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026. The governing version is the attached PDF and the public source at `openai/math` commit `4eaee875`.

- [Pinned PDF](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).
- [Pinned Section 4 TeX](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/sections/04-classical.tex).
- [Pinned Section 5 TeX](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/sections/05-exponent.tex).

The attached PDF has 433829 bytes and SHA256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`. A separately retrieved public PDF at the source pin matched those bytes exactly. The pinned TeX of both assigned sections was also retrieved and read. The web page reader could not open those two TeX pages; the raw source retrieval succeeded. That distinction is recorded here because a failed page view is not source evidence.

| Assigned claims | Exact paper location | Role |
| --- | --- | --- |
| Conditional product law, value, (16), product expectation, terminal bound | Section 4.1, pp. 11–12, proof of Lemma 4.1 | Target statements and proof route. |
| Budget, dummy and planted distributions | Section 4.2, p. 12, (17) and following definitions | Target definitions. |
| Coupling, hidden zero, discovery count, heavy columns, simulator | Section 4.2, pp. 12–13, (18)–(22) and intervening claims | Target probability statements. |
| Full gap, tail, numerical constants, randomized lower bound | Section 4.2, pp. 13–14, (23) and final paragraphs | Exact constants and quantifiers. |
| Quotient divergence | Section 5, p. 14 | Fixed-parameter exponent argument. |

The printed (18) and (23) describe a difference without literal absolute-value bars. The ledger's `eq-18` asks for the symmetric form. The new source proves that strengthening; the absence of bars is not reported as an error in the preprint.

## DP1. Conditional values and the product argument

**Andrew Drucker.** “Improved Direct Product Theorems for Randomized Query Complexity.” *Computational Complexity* **21**(2), 197–244 (2012). DOI: [10.1007/s00037-012-0043-7](https://doi.org/10.1007/s00037-012-0043-7).

Sources inspected: [author manuscript](https://people.csail.mit.edu/andyd/SDPT.pdf), [arXiv:1005.0644](https://arxiv.org/abs/1005.0644), and [author's institutional publication record](https://www.research.ed.ac.uk/en/publications/improved-direct-product-theorems-for-randomized-query-complexity/).

Use Section 1.3 for the method, Lemma 3.1 for the one-instance conditional optimum, Lemma 3.2 for conditional independence after an adaptive transcript, the following product calculation, and the final paragraph of Section 3 for separately capped algorithms. These locators refer to the inspected author manuscript, printed pp. 6–7 and 11–13. The global-budget statement of Theorem 1.1 is a different specialization. Drucker explains the relation to Shaltiel's method. This reference supplies attribution and a reconstructible proof antecedent; it does not supply Lean validation.

## DP2. The fairness restriction

**Ronen Shaltiel.** “Towards Proving Strong Direct Product Theorems.” *Computational Complexity* **12**(1–2), 1–22 (2003). DOI: [10.1007/s00037-003-0175-x](https://doi.org/10.1007/s00037-003-0175-x).

Sources inspected: [ECCC TR01-009](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html), [author's institutional publication record](https://cris.haifa.ac.il/en/publications/towards-proving-strong-direct-product-theorems/), and the supplied `literature/quartic-ref-22-towards-proving-strong-direct-product-theo/extracted.md`, Section 5, printed pp. 11–12.

Definition 4 caps the number of queries to each input on every root-to-leaf path. Theorem 5 and Lemma 7 are stated in XOR-advantage notation. They are the fairness antecedent, with the relation to an all-answers direct product explained by Drucker, Section 1.1, footnote 3. Do not cite Shaltiel's displayed theorem as if it literally had the present vector-output statement and arbitrary product prior.

## M1. Mathlib API audit

The dependency pin is [Mathlib `69552756cd8a2d2d48763cf7279fd814d6a1224d`](https://github.com/leanprover-community/mathlib4/tree/69552756cd8a2d2d48763cf7279fd814d6a1224d). A source archive at that exact commit was retrieved. The reviews consulted the finite sum/product, floor, real-power, logarithm, limit, and order APIs used in the new proofs. Detailed files and names are in the individual `source_reads/` receipts.

Source inspection confirms names and statements; it cannot settle elaboration, tactic execution, typeclass synthesis, module visibility, or generated declarations. The new files require the exact pinned compiler and dependency graph.

## R1. Project source and adjudication

The supplied source manifest identifies repository commit `4c7544f8dcdfc18d3ecf8476ebd8c1090cd46f15`. All 356 recorded members were checked for both byte length and SHA256, with no mismatch. This integrity check does not imply substantive reading of every file.

The exact statement objects for all assigned identifiers and their ties were inspected. Their source-line locators refer to `paper/extracted.md`. The latest adjudication governs earlier proposals, including:

- `F-TREE-GAP`: signed source theorem versus symmetric prose interpretation.
- `F-CLAIM-TAIL`: preserve the exact original logarithmic exponent; a weaker envelope remains a separate claim.
- `F-ZS-TIGHT`: the scan example does not prove coefficient-two tightness under a worst-case depth cap.
- `F-ZS-REFINE`: the optional sharper zero-search estimate is separate future work.
- `R1-AF-18` and the later pending tie: (17) is the definition of the floored budget, with Proposition 4.2 carrying the lower-bound assertion.

The older claim that the headline theorem still needs an external Forrelation hypothesis is superseded by the supplied unconditional source. The new asymptotic wrapper imports that existing unconditional development. It does not use the disputed display in Bansal and Sinha's Section 5.4 as a new external premise, and this return does not reopen that separately assigned investigation.

## Build-receipt limitation

`BUILD_STATUS.md` reports earlier compiled modules and identifies a root receipt at `16adedc16acca1e3a8d2963d4fd5655dcd0492d7`. The latest supplied adjudication explains that the receipt predates working-tree additions later committed with the unconditional Forrelation development. This return does not replay the build, inspect absent binary receipts, or alter the reported comparison results. A clean source pin with a matching build receipt is needed before any new status is promoted. The old status is reported evidence, and every new file remains unelaborated.

## Scope of literature claims

No novelty or priority claim is made for the conditional-value proof, the elementary coupling, the posterior calculation, or the asymptotic algebra. Earlier quantum upper bounds, cheat-sheet constructions, and Forrelation antecedents are context supplied by the project; this assignment does not re-prove their entire literature. The references above are the sources needed for the new Sections 4–5 explanation and its proof correspondence.
