# Sources, reading scope and evidence boundaries

Review date: 3 November 2026. Assignment: `quantum_mechanism`, round five.

The review is bound to the supplied current Markdown and the six draft hashes copied verbatim into `findings.json` from `SOURCE_STATUS.json`. The packet identifies repository commit `752826a36192b25dc08e364a070eb03eb95dbc85`, while expressly making the member hashes authoritative for working files. The record Markdown, rather than its earlier rendered PDF, governs proof quotations and locators.

## What was read

| Material | Actual coverage |
| --- | --- |
| `READ_ME_FIRST.md` | Read in full; the return follows its critique-only scope and requested finding schema. |
| `repository/docs/expert_companion.md` | Read §§1–4 and Appendix A closely; sampled §7 and surrounding classical/lower-bound material only for the quantum count, quantifiers and statement interface. No full classical-proof audit is claimed. |
| `repository/docs/exposition.md` | Read in full, with detailed review of §§2–4 and §7; its bibliography was inspected. |
| `paper/extracted.md` | Read the introduction/construction overview and quantum §3, including Lemma 3.1 and Propositions 3.2–3.3; other construction/local-test passages were consulted as needed. |
| `repository/docs/reasoning_record.md` | Read quantum §§5.1–5.4 closely, including the comparison model, exact sampling, cyclic example, coupling, verification and budgets; consulted §5.5 for interfaces and selected construction/correspondence passages. The whole 389 KB record was not read as a single audit. |
| Lean statement layer | Inspected the main Challenge's oracle, program, projection, probability, cost and headline definitions; main Solution and comparator configuration; the full supplementary amplifier Challenge; selected construction-family and upper-budget source; relevant comparator-map entries. |
| Navigation metadata | Inspected `LINK_MAP.json`, relevant `lean_links.json` entries and `comparator_map.json`; independently checked 12 local target ranges and eight record anchors. All sampled locations exist. QM-018 shows why existence alone is not enough. |
| Rendered drafts | Rendered the supplied expert PDF pp.5–7 and exposition PDF pp.6–8 to images and visually inspected them. The expert P10/P13/P15 labels were confirmed, including a close crop; all 14 P-number tags were matched in extracted PDF text. Other pages were not comprehensively inspected. No PDF was regenerated from manuscript source. |
| Writing exemplars | Sampled the opening and structure of `exemplars/short-paper.md` and `exemplars/expository.md`, including the exposition's separation of its main argument from optional calculations. These were register/structure references only; they supply no evidence about the quartic result. The exemplar long record and exemplar PDFs were not independently audited. |
| Attached 67,088-line trace | Selected late current-state and operator-correction passages were checked to preserve the assignment and evidence boundaries. The nested historical trace was not read exhaustively or used as proof evidence, and is not duplicated in this return. |

“Inspected” and “read” above refer to supplied source text or rendered pages, not execution of proofs. No Lean build, Comparator invocation or external-kernel run was made in this review. The new comparison/state assertions were treated as the working-draft state stipulated by the brief; pending execution status was not turned into criticism.

## Primary literature actually consulted

All mathematical comparisons below use primary papers. Online checks verified editions and, where stated, publication locators. They do not replace the supplied full texts with search snippets.

| Source | Exact consulted locators and role |
| --- | --- |
| **OpenAI, _A Nearly Quartic Separation Between Randomized and Quantum Query Complexity_ (5 October 2026)** | Supplied `paper/extracted.md` and corresponding source PDF identity. §1.1 distinguishes C-versus-Q antecedents; §3.1 gives bounded amplification; §3.2 gives the fractional tournament and stopped coupling; §3.3 gives measured-address verification. [Official preprint repository](https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026). The frozen supplied version is the reviewed version. |
| **Brassard–Høyer–Mosca–Tapp (BHMT)** | [arXiv:quant-ph/0005055v1](https://arxiv.org/abs/quant-ph/0005055v1); published 2002. Supplied `literature/quartic-ref-12-quantum-amplitude-amplification-and-estima/extracted.md`, §2 through Theorem 3 and QSearch: Lemma 1 and equation (8) give the two-dimensional action and successful component; Theorem 3 states expected-cost search without knowing the success probability. Amplitude-estimation sections were not reviewed. |
| **Boyer–Brassard–Høyer–Tapp (BBHT)** | [arXiv:quant-ph/9605034v1](https://arxiv.org/abs/quant-ph/9605034v1); published 1998. Supplied `literature/quartic-ref-11-tight-bounds-on-quantum-searching/extracted.md`, §4 Lemmas 1–2, the randomized-iteration search and Theorem 3. Lemma 2 supplies the average of the squared sine; the record/preprint supplies the particular bounded wrapper used here. Remainder sampled only. |
| **Høyer–Mosca–de Wolf (HMW)** | [arXiv:quant-ph/0304052v2](https://arxiv.org/abs/quant-ph/0304052v2), ICALP 2003. Supplied `literature/quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error/extracted.md`, §1 and §3: each subroutine approximates a fixed Boolean value with a uniform error bound. The algorithm and amplification/error-reduction interface were consulted; later applications were not audited. The online metadata says v2 only corrected an affiliation. |
| **Dürr–Høyer (DH)** | [arXiv:quant-ph/9607014v2](https://arxiv.org/abs/quant-ph/9607014v2), 1999 revision of the 1996 note. The complete supplied two-page text was read: §§1–3, Theorem 1, Lemmas 1–2, decreasing-rank analysis and the capped minimum-search routine. Local path: `literature/quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu/extracted.md`. |
| **Mande–Paraashar–Saurabh (MPS)** | Supplied [arXiv:2308.02472v1](https://arxiv.org/abs/2308.02472v1), `literature/quartic-ref-18-randomized-and-quantum-query-complexities/extracted.md`: abstract, §1, Definition 1.1, §1.2.2, and §4 Observation 4.1/Lemma 4.2/Theorem 4.4. These fix one bit per edge and sample a surviving deterministic set. The [published FSTTCS 2023 paper](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30) was also opened to verify Definition 1, Observation 16, Lemma 17 and Theorem 19. Theorem 19 is on p.30:11; the source section and algorithm extend across pp.30:9–30:13. Published Theorem 19 and supplied-v1 Theorem 4.4 are edition-specific locators. Lower-bound proofs were not audited. |
| **Ben-David–Kothari (BDK), _Randomized query complexity can beat certificate complexity_** | [arXiv:2609.15063v1](https://arxiv.org/abs/2609.15063v1). Supplied `literature/quartic-ref-09-randomized-query-complexity-can-beat-certi/extracted.md`: mathematical sections §1, §2 and §3, especially Lemma 5's virtual list, exact local comparison, SINK/king-finding step and final verification. These are C-versus-R and C-versus-Q statements. Source metadata was verified online. |
| **Ambainis–Iraids–Kokainis (AIK), _Near-Optimal Separations of Certificate Complexity from Randomized and Quantum Query Complexity_** | [arXiv:2609.11664v2](https://arxiv.org/abs/2609.11664v2). Supplied `literature/quartic-ref-05-near-optimal-separations-of-certificate-co/extracted.md`: introduction and quantum §6.1–6.2, especially the fixed candidate set U(W), equations (3)–(8), and Lemmas 6.1–6.3. Approximate edge-direction implementations and variable-time membership tests are not the arbitrary-probability sampler of the reviewed preprint. Later exact/zero-error sections and appendices were not fully read. Title and v2 revision metadata were verified online. |

The packet's Grover, BBBV, Aaronson–Ambainis, cheat-sheet and de Wolf lecture-note files were not independently reviewed in full for this job. General historical references to them are assessed only where supported by the current drafts, preprint and directly consulted quantum sources; this return does not offer a new audit of their theorems. Barnum–Saks–Szegedy is cited-only in the input packet and was not read or used as independent evidence.

## Key existing proof destinations

These are anchors in the supplied current `repository/docs/reasoning_record.md`, not requests for additional mathematics.

| Question | Existing destination |
| --- | --- |
| What bounded amplification promises | `upper-amplification-statement` |
| Which original register is returned | `upper-returned-register` in §5.1 |
| What coherent comparison access is assumed | `upper-comparison-model` |
| Why HMW is not directly applicable | `upper-bounded-error-comparison` |
| What happens at W = 0 | `upper-ideal-process` and `upper-quantum-tournament` |
| Why probabilities multiply, then add | `upper-stage-state` and `upper-stage-law` |
| An existing fractional numerical example | `upper-cyclic-example` |
| How history-dependent failures are coupled | `upper-coupling` |
| Fresh measured-address verification | `upper-verifier` and `upper-verification-proof` |
| Two bit queries for a controlled read | `upper-oracle-access` |
| Whole finite query budget | `upper-finite-budget` |
| The deliberately loose exponent six | `upper-explicit-log6` |

The long-record public path is [docs/reasoning_record.md](https://github.com/wcook04/quartic-query-lean/blob/main/docs/reasoning_record.md); append the relevant anchor for navigation. Local existence and content were checked against the frozen packet. Remote availability of every manuscript GitHub link was not tested, and the return makes no claim that a `main` link remains bound to these exact bytes.

## Checks that support the return

The input ZIP's CRC test passed. All 73 members listed in its manifest matched both byte count and SHA-256; the request hash, six draft hashes and current record hash also matched. All 38 finding quotations were checked as exact substrings of the applicable current Markdown and contain at most 25 whitespace-delimited words. Per-finding source lines and hashes are in `validation.json`.

Finite arithmetic spot-checks reproduced the existing four-column weight totals 0, 2, 2, 2; their expectation 3/2; the m = 4 error bound 583/192000; and the record's fractional next-pivot probabilities 11999/23999 and 12000/23999. These support the specific examples and local criticisms. They are not new proofs or a formal verification of the quantum algorithm.

The checksum manifest and included validator cover the return files. After extraction, the validator can also recheck every quote against the original packet when supplied with `--packet`. Archive integrity establishes that the delivered bytes can be read; mathematical correctness remains the reasoned assessment set out in the located findings.
