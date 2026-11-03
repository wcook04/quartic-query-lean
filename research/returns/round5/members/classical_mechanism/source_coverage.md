# Sources, citations and reading limits

Review date: **3 November 2026**. Assignment: the randomized lower-bound mechanism in both current drafts, its literature, teaching, and formal links. This report uses the supplied packet as the source of record. Online primary-source checks supplement it; a current website never silently replaces the packet’s bytes.

## Current-source binding

The input archive `quartic_r5_classical_mechanism.zip` is 8,293,515 bytes and has SHA-256:

```text
9a39116c7d5ca6168621b0754b9742eec64787e852ee5599fc6ae698e7486738
```

Its 74 members have distinct names and pass CRC validation. All 72 entries in its member manifest match their byte lengths and SHA-256 hashes; the other two members are the manifest and assignment. The assignment hash, all six draft hashes in `SOURCE_STATUS.json`, and the current reasoning-record Markdown hash also match. Detailed checks are in `checks/input_integrity.json`.

The packet records repository commit `752826a36192b25dc08e364a070eb03eb95dbc85` as provenance; the supplied file hashes identify the reviewed working bytes. `findings.json.source_sha256` copies the entire six-entry `drafts` object exactly. The reasoning-record Markdown is authoritative for this review: its SHA-256 is `1b677c780734209fd36fc206a17e4262f9124e290f84736e9573db8f1f88a986`. Its PDF was rendered from an earlier text, as the supplied status and diff explicitly disclose.

## What was actually read

“Read closely” below refers to the named sections, not a claim to have verified every theorem in an entire source. The complete current companion and exposition were read for context; the proof audit concentrated on the classical material.

| Source | Coverage and use |
|---|---|
| `READ_ME_FIRST.md`, `SOURCE_STATUS.json`, `manifest.json` | Read in full; instructions, task boundaries, source identities and file completeness checked. |
| `repository/docs/expert_companion.md` and `.bib` | Current text read throughout. Closely audited §§1.1–1.2, the classical ingredient in §2, relevant Table 1 rows, §§5–7 and Appendix A. Quantum sections were read as context, not independently proved. |
| `repository/docs/exposition.md` and `.bib` | Current text read throughout. Closely audited Overview, board conventions in §§1–2, classical hardness in §3, §§5–6 and the classical claims in §7. Bibliography checked for the cited classical works. |
| `paper/extracted.md` | Read the title/result, construction context, all of §4 including Lemma 4.1 and Proposition 4.2, and §5’s exponent argument. The full quantum analysis and universal-bound appendix were not independently audited. |
| `repository/docs/reasoning_record.md` | Closely read the complete classical chain in §§6.1–6.6: both direct-product formulations, history product law, independent information, realized-cap corollary, examples, minimax, planted laws, first difference, zero-search variants, simulator, union/average and floors. Sampled §6.7, §7 and formal-scope passages. Checked §3.16–§3.18 for the SSW comparison and source distinctions. Did not independently reprove the full analytic Forrelation development. |
| `Unconditional/Challenge.lean`, `Solution.lean`, `comparator.json` | Read in full. Definitions, four configured headline names, wrapper types and shared-circuit quantifiers inspected. This was a source inspection, not execution. |
| `Independent/RealizedCaps/Challenge.lean`, `Independent/Eq19/Challenge.lean`, `Planted/ZeroSearchSuccessor.lean` | Read in full. Checked finite seed quantification, the joint-event conclusion, the erased-zero conjunction, and the finite charging invariant. |
| `Paper/ClassicalPlanted.lean` | Read relevant definitions and theorem passages for the dummy/planted laws, zero identity, coefficient-two bound, simulator, per-time event and averages. Other Lean files were consulted only as needed for context. |
| `comparator_map.json`, `lean_links.json`, `LINK_MAP.json` | Inspected target metadata and the relevant declaration blocks. All link-map rows were read; 14 sampled Lean references across the two papers were independently checked against local ranges, representing nine distinct reference labels. See `checks/link_checks.json`. No fresh live-repository link-completeness or Comparator result is claimed. |
| Separate 5.5 MB trace attachment | Indexed and selectively read for the current assignment’s boundaries, latest closeout and the historical cap-definition excerpt. The full duplicated session/child history was not read line by line. It was not used as a current build receipt and is not republished in this return. |
| Three SK exemplars | Sampled short-paper opening and formal scope, exposition opening/structure, and long-record argument-map passages. Used only for reader-model and navigation comparison, not as mathematical evidence about query complexity. |

## Literature read closely or sampled

All page numbers below are the **printed pages of the identified edition**. For Shaltiel’s report the cover is printed page 0, so the PDF page index counted from 1 is one larger. The supplied extracted Markdown sometimes corrupts theorem labels; the PDF text was used to check numbering.

| Source and primary link | Exact sections inspected | Role and limit |
|---|---|---|
| [Drucker, arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2), 9 May 2014; journal publication 2012 | §§1.1–1.3; §3, especially Lemmas 3.1–3.2, pp. 11–12, and final fair-tree paragraph, p. 13; §4, pp. 13–14; Lemma 5.1, p. 14 | Read closely for fair versus global budgets, posterior values, source credit, counterexamples and minimax. Relevant supplement locations were also compared. Other generalizations in the paper were not audited. |
| [Shaltiel, ECCC TR01-009](https://eccc.weizmann.ac.il/report/2001/009/download/), 2001 | §1.1 and footnotes 1–2, printed p. 1; §3 obstruction; §5 Definition 4 and Theorem 5, printed p. 11, and Lemma 7, printed p. 12 | Read the fairness statement/proof and its XOR-advantage conventions. The communication-complexity proof in §4 and the 2003 journal text were not read in full. Do not transport report locators to journal pagination. |
| [Bansal–Sinha, arXiv:2008.07003v3](https://arxiv.org/pdf/2008.07003v3), 17 November 2020 | Introduction; definition (1.3), Proposition 1.2, classical upper bound and odd-\(k\) footnote 1, **p. 3**; Theorem 1.3 and Corollaries 1.4–1.5, p. 4 | Exact one-sided promise, fixed-\(k\) lower-bound transfer, matching upper exponent and total-separation application checked. The full Gaussian/interpolation proof was not independently verified. |
| [Sherstov–Storozhenko–Wu, arXiv:2008.10223v4](https://arxiv.org/pdf/2008.10223v4), 29 January 2023 | Theorem 1.1, p. 3; Theorem 1.5, p. 4; §1.8, p. 10; Corollaries 4.14–4.15 statements, p. 35 (latter proof continues p. 36) | Read the result statements and explicit comparison with Bansal–Sinha; checked the Fourier input used by record §3.16. Did not independently audit the full Fourier proof. |
| [Aaronson–Ben-David–Kothari, arXiv:1511.01937v2](https://arxiv.org/pdf/1511.01937v2), 9 July 2019 | Introduction; §3.1, pp. 9–10; §3.2, especially Lemma 6, pp. 12–13 and its blank-cell coupling, p. 13 | Read the relevant construction/lower-bound mechanism and exponent arithmetic. Later separating-function results were not audited. The cited publication is STOC 2016; these locators use the 2019 arXiv revision. |
| [Ambainis et al., arXiv:1506.04719v3](https://arxiv.org/pdf/1506.04719v3), 26 October 2015 | §§1.2–1.3, especially “Use of a balanced tree,” p. 6 | Read the pointer-function antecedent and the explicit discussion of direct outward pointers and its alphabet obstacle. Did not independently verify all separation constructions. |
| [Girish–Servedio, ITCS 2026, Article 72](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.72) | Introduction, Definition 3 and Theorem 4, p. 72:4 | Sampled the extremal two-function promise and principal theorem, and checked publisher metadata. Its different promise is not a replacement for the present one-sided \(k\)-fold ingredient. No extra citation is requested solely because this paper is supplied. |
| Beame–Kornerup–Whitmeyer, supplied arXiv:2609.26678v2 | Introductory classical/quantum direct-product context | Sampled only; no theorem from it is used to justify a finding. |
| Buhrman–de Wolf, supplied decision-tree survey | §3.2 randomized-tree model | Sampled only; not a substitute for reading Yao’s original. |

Primary online editions for Drucker, Shaltiel, Bansal–Sinha, SSW, cheat sheets and pointer functions were opened and compared at the relevant passages/metadata. The original OpenAI GitHub entry was also opened; the proof audit used the supplied preprint bytes. `citations.json` records primary URLs and locators without depending on transient search references.

### Cited only

**Yao (FOCS 1977, pp. 222–227)** and **Nisan (SIAM J. Comput. 20(6), 1991, pp. 999–1007)** were cited in the packet but their originals were not supplied or read. The recommendation to cite Yao is grounded in the preprint’s attribution and the standard formulation also inspected in Drucker’s Lemma 5.1. Other works appearing only in the drafts’ quantum/history references were not independently audited unless listed above.

## Visual and computational checks

The supplied expert and exposition PDFs each contain 13 pages. Both were text-extracted. Five existing pages were rasterised and visually inspected: expert pp. **7–8** and exposition pp. **9–10, 12**. The relevant planted figures are present in the PDFs. The malformed headings are visible on expert pp. 7–8. Figure 4 labels all address inputs as sampled from \(\mu\); it does not carry forward the earlier off-promise label.

Only those five pages received visual inspection. No new manuscript PDF was rendered. Exact rational enumeration checked the stated AND, expected-budget parity and dependent-column examples; those results are reproducible with `checks/finite_examples.py`. The numerical tail/floor arithmetic was checked separately in `review_notes.md`.

**No Lean build or Comparator run was performed.** Presence of a declaration, recorded comparison metadata, ordinary mathematical review and successful native execution remain distinct. The pending integration described by the packet was not treated as a defect. The two missing imported specifications and three missing SVG sources are limitations of what the supplied packet lets a reader inspect, not evidence of a false theorem or corrupt archive.
