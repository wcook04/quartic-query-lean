# Sources read and limits of the review

This is an editorial, navigation and statement-to-evidence review of the supplied round-five snapshot. The findings concern the current Markdown. Existing PDFs were inspected as publication outputs, with the disclosed older record-PDF paragraph treated as a known version difference. The latest amplifier, independent-randomness, model-sanity and sharper-search additions were judged as stated, as the brief requires; their parallel rebuild status was not treated as a defect.

## Exact source boundary

- Packet job: `long_record_navigation`.
- Input archive: `quartic_r5_long_record_navigation(1).zip`; SHA-256 `1ba7b1337f45fcb641918038825fb64cb6981cfce5c2da6ea3f45d858b8f5803`.
- Current record: `repository/docs/reasoning_record.md`; SHA-256 `1b677c780734209fd36fc206a17e4262f9124e290f84736e9573db8f1f88a986`.
- Pasted trace: `Pasted text(20261103-030543).txt`; SHA-256 `ff07a77387545a85a24b6d4a7e91e5f57a24c698a17f52577149c8bf67a2ac22`.
- All six draft hashes from the supplied `SOURCE_STATUS.json` are copied unchanged into `findings.json`. The original status object is preserved in `evidence/source_status.json`.
- All 162 archive members passed CRC checking. Every one of the 160 entries in the packet's member manifest matched its recorded byte count and SHA-256. That integrity result is compatible with an incomplete link inventory: three referenced SVGs were never included as members. See `evidence/packet_integrity.json` and LR-006.

## Reading coverage

| Material | Coverage and use |
| --- | --- |
| `READ_ME_FIRST.md`, `SOURCE_STATUS.json`, record/PDF diff | Read in full; used to fix scope and distinguish the current text from known parallel work. |
| Current long record | Full structural and editorial reading of all 5,945 lines, including every catalogue row and Appendix D. A second pass checked the central quantum, classical, exponent and formal-interface passages. This is not an independent reproof of every theorem. |
| Current expert companion and exposition | Read through the mathematical narrative, formal appendices and reference destinations. All direct record links and every supplied Lean-link entry were checked; selected local counterexamples and wording were examined independently. |
| Supplied OpenAI preprint | All mathematical sections and Appendix A read, using the supplied extraction and PDF text; references inspected. Its PDF has 19 pages. The preprint is the mathematical source being explained, not a publication-acceptance certificate. |
| Link inventories | All four incoming record links assessed individually, including their semantic landing points. All 78 enumerated reading-closure destinations checked locally. Independent parsing found 77 short-draft destinations against 74 in `LINK_MAP.json`. All 199 direct internal record links resolve to 339 unique explicit IDs in the Markdown. |
| Formal sources | Unconditional Challenge, Solution and configuration read in full. Complete or relevant statement types examined in Construction, ConstructionFull, ConstructionFamily, UniformAmplifier, RealizedCaps, Degree, ModelZero and Eq19; relevant declaration passages examined in Upper/Bound, ForrelationLower/Uniform, ClassicalPlanted and the Eq19 wrappers. All 47 entries of `lean_links.json` checked for local target and range availability. |
| Formal records | Central name/configuration joins, receipt metadata and named-declaration membership read; seven relevant source hashes checked against the supplied root-build receipt. Thirteen central catalogue observations and printed theorem types were sampled. The multi-megabyte correspondence and native graphs were queried selectively, not read exhaustively. The 17 claim traces state their source and evidence boundaries individually. |
| SK long-record exemplar | Overview, heading structure, §2.1 and §§12–13 sampled; PDF page 2 visually inspected and its annotation structure checked. Used only for proof/evidence organization and rendering comparison. It has no current-companion return links to praise or copy. Its mathematics was not audited. |
| Other SK exemplars and earlier returns | Not read exhaustively. Selected earlier evidence summaries and examples were followed only where the current record points to them; no global endorsement of their content is made. |
| Pasted agent trace | Structural header, top-level context summary and closeout/status excerpts sampled. The 5.5 MB trace was not read exhaustively. It provided background about the work's boundaries; no finding relies on an unverified statement in the trace. |

## Primary literature actually consulted

The following supplied papers were read at the stated passages. Their arXiv edition metadata was also checked online on 3 November 2026. The online records confirm bibliographic identity; mathematical comparisons below rely on the supplied passages, without asserting byte identity between a live PDF and the packet copy.

### Aaronson, Ben-David and Kothari — cheat sheets

**Read:** supplied PDF pages 4 and 9–10, including §3.1 and the start of §3.2; corresponding extracted text sampled. These passages explain the partial-function/domain-certification obstacle, composition with AND-OR, and addressing certificates by answers to several instances. They support the restored attribution and provide a useful model of an interface followed by its implementation. They do not establish the new multi-column construction.

**Edition:** *Separations in query complexity using cheat sheets*, STOC 2016, arXiv:1511.01937v2. [Official edition record](https://arxiv.org/abs/1511.01937v2). Packet directory: `literature/quartic-ref-02-separations-in-query-complexity-using-chea/`.

### Bansal and Sinha — Forrelation

**Read:** supplied PDF page 4, Theorem 1.3 and Corollaries 1.4–1.5; page 38, §5.4 and its displayed comparisons. These locate the one-sided-promise lower bound and the earlier total-function consequence. The source-version discussion in record §3.16 was checked against the displayed PDF calculation. This review makes no claim that the cited theorem is false and proposes no replacement theorem. The TeX line numbers preserved by the record were not independently re-audited.

**Edition:** *k-Forrelation Optimally Separates Quantum and Classical Query Complexity*, STOC 2021, arXiv:2008.07003v3. [Official edition record](https://arxiv.org/abs/2008.07003v3). Packet directory: `literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/`.

### Brassard, Høyer, Mosca and Tapp — amplitude amplification

**Read:** supplied PDF §2, pages 6–7, especially equation (8) and its surrounding state calculation. This identifies the successful-state rotation used by the record. The record and supplied preprint separately specify the fixed trial count and all-branch cap needed here; an expected-cost result alone would not supply that guarantee.

**Edition:** *Quantum Amplitude Amplification and Estimation*, published 2002; inspected preprint arXiv:quant-ph/0005055v1. [Official edition record](https://arxiv.org/abs/quant-ph/0005055v1). Packet directory: `literature/quartic-ref-12-quantum-amplitude-amplification-and-estima/`.

### Drucker — capped direct products

**Read:** supplied PDF page 6, §1.3; pages 11–12, Lemmas 3.1–3.2 and the product-potential calculation. These passages establish the relevant methodological antecedent: a posterior product law and a potential that changes in only one factor per query. Drucker explicitly credits the earlier fair-algorithm argument to Shaltiel. The record's joint-event simulator and its particular application remain the reconstruction's responsibility.

**Edition:** *Improved Direct Product Theorems for Randomized Query Complexity*, Computational Complexity 21(2), 197–244 (2012); arXiv:1005.0644v2, updated 2014. [Official edition record](https://arxiv.org/abs/1005.0644v2). Packet directory: `literature/quartic-ref-13-improved-direct-product-theorems-for-rando/`.

### References retained without a claim of independent reading

Yao's FOCS 1977 paper was cited only, as the packet directs. Shaltiel's original paper, the other pointer-function and tournament papers, the sensitivity/adversary sources, and the additional Fourier-growth papers were not independently read for this return. Their roles were checked against the current record and supplied preprint where relevant; this is not a substitute for inspecting those originals.

## PDF inspection

Complete annotation and destination structures were inspected for the record and the sampled exemplar. Text and outlines were inspected for both shorter PDFs. Existing pages were rasterized with PyMuPDF for visual inspection; no manuscript PDF was regenerated or edited.

- Record: visual pages 3, 13, 35, 51, 77, 90, 108 and 116; targeted annotation checks additionally covered pages 21, 44, 87 and 91.
- Expert companion: visual page 8; literal heading markers and outline entries also checked on page 7.
- Exposition: visual pages 4, 8 and 9, including both concrete figures whose SVG files are missing.
- SK exemplar: visual page 2; all 42 internal link actions checked for existing named destinations.

This is a targeted layout review, not visual inspection of every PDF page or a check of every possible PDF reader. Live GitHub availability and all external links were not retested. No Lean build, Comparator run, native dependency extraction, or execution of submitted checking scripts was performed. The supplied receipts were read as evidence of their stated earlier runs.
