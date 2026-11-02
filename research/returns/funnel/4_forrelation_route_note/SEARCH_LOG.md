# Literature search and reading record

**Search date:** 2 November 2026. **Cutoff:** publicly available work located on that date. This record concerns the Forrelation lower-bound route. It does not certify priority, completeness of citation indexes, or the formal verification of a new endpoint. The per-ingredient findings are in `prior_art.json`; version-pinned references are in `references.bib`. The accompanying `forward_citation_inventory.json` and `contemporary_screening.json` preserve the retrieved metadata and per-source screening boundaries.

## Main finding and its limit

No matching statement of the single-output-block, matched-index Stein chain was located. The ingredients and several close formulations have clear antecedents. Bansal and Sinha already supply the rounded Gaussian product chain and transformed integration-by-parts identity. Girish, Tal and Kewen Wu already give the ordinary-tree martingale, contracted-walk induction, Azuma and union-bound method. Tal explicitly asks about using only level k of a function and its restrictions for k-fold Rorrelation. Chattopadhyay, Gaitonde, Lee, Lovett and Shetty establish single-level tail control for restriction-closed families; Xinyu Wu obtains exact-level control for an XOR composition of independent two-fold Forrelation instances.

These comparisons support a narrow distinction for the proposed chain formula. They do not establish that nobody has previously derived it. The smooth rounded distribution here also differs from Tal’s sign-rounded distribution, so the note should not claim to solve his literal distributional question.

## Search coverage

Two public web-search engines were used for discovery, with primary papers, publisher pages, ECCC records and author pages used for substantive evidence. The search included the Bansal–Sinha and Girish–Tal–Wu titles, theorem terms, proof mechanisms, later uses and 2024–2026 work. Among the recorded exact queries were:

- `Forrelation "single" "Stein"`
- `Forrelation "antiderivative"`
- `"Forrelation" "exactly" "level" "interpolation"`
- `"biased" "decision trees" "martingale" Fourier growth`
- `"k-Forrelation" "improved" lower bound` with a recent-publication filter
- `"Forrelation" "Stein" interpolation 2024 2025 2026`
- `"Forrelation" "single-parameter"`
- `"Fourier growth" "biased" decision tree`

The queries often returned the original papers or irrelevant uses of the terminology. A negative query result was never treated as a proof of novelty.

### Forward citations

The public OpenAlex API was queried for works citing Bansal–Sinha’s STOC DOI `10.1145/3406325.3451040`, mapped to `W3049592525`, and GTW’s CCC DOI `10.4230/LIPIcs.CCC.2021.39`, mapped to `W3152113665`. The citation endpoints were:

- `https://api.openalex.org/works?filter=cites:W3049592525&per-page=200`
- `https://api.openalex.org/works?filter=cites:W3152113665&per-page=200`

They returned 22 and 5 records respectively. These are index records, not 27 independently verified relevant papers. The lists include self/version artifacts and omit known citations; for example, GTW explicitly cites BS but was absent from the retrieved BS list. Alternate arXiv/proceedings lookups mapped back to the same records. All returned titles/metadata were screened. Relevant full-source follow-ups were read at the scopes listed below; remaining records were screened by title/metadata only.

A Semantic Scholar graph request for the BS citation list returned HTTP 429. No complete Semantic Scholar or Google Scholar forward-citation list was obtained. The OpenAlex sweep was therefore supplemented with primary arXiv topic searches, ECCC records, author pages and the reference sections of the papers read. It must not be described as an exhaustive forward-citation search.

### Dated arXiv topic sweep

The public arXiv API query was:

`(ti:Forrelation OR abs:Forrelation) AND submittedDate:[202401010000 TO 202611022359]`

It returned 20 entries, using `start=0`, `max_results=100`, and descending submission date. Every returned abstract was read. Eight had relevant body sections inspected, listed in the contemporary table below. The other twelve were screened at abstract level only. The complete 20-entry inventory is:

`2610.41694`, `2609.34659`, `2609.31596`, `2609.25680`, `2609.11830`, `2609.07060`, `2609.05201`, `2608.11970`, `2606.28483`, `2605.02051`, `2604.15248`, `2602.07503`, `2511.09551`, `2510.07193`, `2510.06385`, `2508.02514`, `2507.07231`, `2505.02939`, `2411.12730`, `2410.08051`.

The submission-date filter excludes older papers first posted before 2024 and revised later, while title/abstract search excludes papers mentioning Forrelation only in their bodies. The separate citation sweep and checks of older source versions partly address those limitations. They do not remove them.

## Sources and reading boundaries

The packet’s lower-bound blueprint, independent review and prior-art report were read. Their descriptions were compared with the primary papers rather than accepted as citation evidence. The supplied literature extractions were usable, but several contain corrupted equations or unresolved theorem labels; numbered claims below were checked in PDF text where necessary.

| Source and version | Material inspected | Principal locator/use |
|---|---|---|
| Aaronson–Ambainis, arXiv:1411.5729v1 / supplied extraction | Quantum-circuit statement, Gaussian Azuma and central-martingale sections; not the entire paper | Proposition 6; §3.4 Lemma 8; Lemma 16. The martingale object differs from Fourier growth. |
| Tal, arXiv:1912.12561v1 | Introduction and proof overview, §4 moments, §5.1–5.2, relevant §7/§8 statements | §1.3 pp. 8–9 and §8 p. 31 for the single-level question; Theorem 5.1; Definition 5.5 and Lemma 5.7. |
| Bansal–Sinha, arXiv:2008.07003v3 | Introduction, §§2–3 theorem interfaces, transformed identities in §4, branching mechanism in §5.1, §5.3 bias transfer and §5.4 amplification | Theorems 1.3, 3.1, 3.2, 3.4; Corollary 3.5; Lemmas 2.3, 2.4, 4.1, 4.3; Claim 5.11. The complete branching proof was not re-proved in this audit. |
| Sherstov–Storozhenko–Pei Wu, arXiv:2008.10223v4 | Introduction, §4.5 proof and its constant dependencies; selected preceding definitions | Theorem 1.9; Theorem 4.13; Corollary 4.14. Absolute constants in Theorem 2.5 and Lemma 3.1 remain unspecified numerically. The entire combinatorial decomposition proof was not re-audited. |
| Girish–Tal–Kewen Wu, arXiv:2103.11604v2 | Introduction, complete ordinary-tree argument in §1.3, adaptive Azuma lemmas, noisy posterior-increment statement | Lemma 1.9; Lemmas 3.3–3.4; Claim 6.1. Full parity cleanup and noisy-tree proofs were not audited. |
| Bravyi–Gosset–Grier–Schaeffer, arXiv:2102.06963v2 | Introduction and §3 estimator construction/variance argument | Theorem 4 (k-fold estimator), Theorem 6 (general amplitude estimator), Theorem 3 (quantum simulation). Graph/QAOA sections were outside scope. |
| Chattopadhyay et al., arXiv:2008.01316v3 | Introduction and central §3 theorem/proof; selected surrounding sections | Theorem 3.1; Lemmas 3.4–3.6. Not a full audit of all PRG applications. |
| Xinyu Wu, arXiv:2109.02732v1 | Full seven-page text | Lemma 2.2; Theorem 3.2. XOR of independent two-fold instances, distinct from the sequential chain. |
| Girish–Sinha–Tal–Kewen Wu, arXiv:2311.16057v2 | Introduction and Appendix A | Explicit use of BS Theorems 3.2 and 3.4 across levels k through k(k−1). No replacement chain formula in those sections. |
| Girish–Sinha–Tal–Kewen Wu, arXiv:2307.13926v1 | Introduction and martingale proof overview, term scan | Communication-protocol Fourier growth; not the complete 64-page proof. |

### Contemporary candidates examined beyond abstracts

| Paper | Scope and relevance |
|---|---|
| Girish–Servedio, [arXiv:2508.02514v1](https://arxiv.org/abs/2508.02514v1) | Theorem 1.4 and bent-function/collision construction overview. The randomized lower bound permits adaptive algorithms, for the extremal Φ=±1 promise. |
| Girish, [arXiv:2510.06385v3](https://arxiv.org/abs/2510.06385v3) | Introduction and §2.1 Theorems 2.4/2.6. The current title is *Fourier Spectrum of Noisy Quantum Algorithms*. Theorem 2.6 uses signed levels 3 and 6 for a weaker-promise three-fold problem. |
| Canonne–Chen–Mestre, [arXiv:2602.07503v2](https://arxiv.org/abs/2602.07503v2) | Main theorem, nonadaptivity discussion and Appendix D disclosure. Near-square-root extremal lower bound is nonadaptive. |
| Escudero Gutiérrez–Saucedo–Palazuelos, [arXiv:2609.05201v1](https://arxiv.org/abs/2609.05201v1) | Introduction and highest-level Fourier theorem statements. Quantum-query polynomial inequalities; not an ordinary-tree or chain proof. |
| Vasconcelos, [arXiv:2609.07060v1](https://arxiv.org/abs/2609.07060v1) | Introduction, §2.3 and main statements. Explicit-input QAC⁰ upper bound, with classical hardness imported from existing work. |
| Mantri, [arXiv:2609.11830v1](https://arxiv.org/abs/2609.11830v1) | Introduction and §1.2.3. Explicitly reproduces the multiple-level BS criterion for a Fourier-hierarchy application. |
| Bouland et al., [arXiv:2609.25680v1](https://arxiv.org/abs/2609.25680v1) | Technical overview, Theorem 6.4 and Lemma 6.5 with proof. Two-fold sign-rounded Forrelation and smooth convex extensions controlled by gradient/Hessian norms through covariance interpolation. |
| Zhang–Shao, [arXiv:2610.41694v1](https://arxiv.org/abs/2610.41694v1) | Introduction and main-result/proof-method statements. Cyclic Forrelation has a different collision construction and query exponent. Full collision proof not audited. |

## Version corrections and access limitations

- **Bansal–Sinha:** the later 2020 version has δ=2⁻⁵ᵏ and Fourier levels k through k(k−1). Earlier versions had an inverse-polylogarithmic advantage and a different level range. The note cites v3.
- **Sherstov–Storozhenko–Wu:** v4 (29 January 2023) is the journal-version preprint. Corollary 4.14 uses natural logarithms. Its constant is absolute but not numerically fixed in the source.
- **Girish–Servedio:** the packet’s prior-art note incorrectly describes its lower bound as nonadaptive. Preprint Theorem 1.4, corresponding to proceedings Theorem 4, covers randomized adaptive algorithms.
- **Canonne–Chen–Mestre:** v2 (1 October 2026) explicitly reports a gap in v1 and replaces the construction/proof. Only the current nonadaptive theorem was used.
- **Girish’s noisy-quantum paper:** v3 (18 June 2026) explicitly corrects an important issue in previous main-theorem proofs. That version was used.
- **Classical upper bound:** Bravyi et al. repair the general simulation argument whose earlier Aaronson–Ambainis proof contained a critical error. The accurate locator for the k-fold upper bound is Bravyi et al. Theorem 4; Theorem 6 is the more general estimator.

All central papers needed for the comparisons were accessible through the supplied packet or public arXiv PDFs. Some PDF opens failed in the web reader; direct public PDF retrieval supplied readable text. SIAM publisher pages exposed metadata/abstracts with a full-text access wall; public author preprints supplied the relevant text. The Semantic Scholar citation endpoint remained unavailable after its rate-limit response. No account, mailbox, credentials or private source was accessed. Sources read only in part are identified above, and no full-text absence claim is based on an abstract-only screen.
