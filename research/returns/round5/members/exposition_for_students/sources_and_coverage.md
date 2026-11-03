# Sources, reading coverage and limits

Review date: 3 November 2026. The task is a critique of the supplied student exposition, for a strong graduate student who knows Grover, basic probability and decision trees. This return contains advice about the existing result. It contains no replacement manuscript, new theorem, new proof or formalization change.

## Which snapshot was reviewed

The authoritative draft identity is the six-entry drafts object in SOURCE_STATUS.json, copied without alteration into findings.json. The repository commit is provenance, not a substitute for those byte hashes.

| Item | Identity |
|---|---|
| Input packet | quartic_r5_exposition_for_students.zip |
| Input ZIP SHA-256 | 35c1076819fbad9ac31fa2c6baa6a2f6eaa4d09e1f1f2e0ee1132c36d12b2331 |
| Packet job | exposition_for_students |
| Repository provenance | 752826a36192b25dc08e364a070eb03eb95dbc85 |
| Current exposition Markdown SHA-256 | 3991d23ca802e1dd50e8c9217abf869035bac04c5febd5bd40bddf5f71de4dce |
| Supplied exposition PDF SHA-256 | 16c85a0f3e063eeb709a7824dc551305d84cb7b09a62c897cecd2bb06c4fb15e |
| Current reasoning-record Markdown SHA-256 | 1b677c780734209fd36fc206a17e4262f9124e290f84736e9573db8f1f88a986 |

All 69 manifest-listed input files passed byte-size and SHA-256 checks. The input ZIP has 71 members; its manifest and READ_ME_FIRST.md account for the additional two. The request hash recorded in the manifest also matches READ_ME_FIRST.md. The input ZIP passed its CRC check. None of the input bytes was edited.

The reasoning-record PDF was generated from an earlier Markdown revision, as SOURCE_STATUS.json says. Current Markdown controls this review. The packet's stated rebuild-in-progress is not used as a criticism. Existing build or Comparator receipts are evidence about their named targets, not a claim that this review reran them.

## Reading depth

Paths below identify members of the original input packet. They are not omitted attachments to this return.

| Source | Actual coverage and purpose |
|---|---|
| READ_ME_FIRST.md and SOURCE_STATUS.json | Read in full. Used to establish scope, audience, return schema and snapshot authority. |
| repository/docs/exposition.md | All 303 lines, including bibliography and link definitions. Every finding quotes this current Markdown exactly. |
| repository/docs/exposition.pdf | Every page, 1–13, visually inspected after rasterization; text extraction also checked page locations. All four figures render. No obvious clipping, label overlap, raw markup or margin overrun was observed. This is visual inspection of the supplied PDF, not a new typesetting build. |
| repository/docs/expert_companion.md | Substantive text through the references read; used for consistency, credit and proof navigation. The link-definition tail was checked selectively. Its PDF was not independently reviewed page by page. |
| paper/extracted.md and paper/source.pdf | Core §§1–5 read, including the tournament and classical-reduction proofs. Selected Appendix A passages checked. Not an independent audit of every appendix argument. Printed page locators in findings refer to the preprint's own numbering. |
| repository/docs/reasoning_record.md | Targeted reading of §§2.1–2.2 and 2.7–2.8; §3.3's quantum experiment, threshold and coherent retention; §3.4's finite circuit account; §§4.3–4.4 and 4.8; §§5.1–5.5; §§6.1, 6.4–6.5 and 6.7; §§7–7.2. Used for existing examples, model semantics, finite constants and exact proof destinations. Other sections were navigated or sampled. The long Gaussian/Forrelation lower-bound development was not re-audited in full. |
| repository/lean/QuarticCorpus/Unconditional/Challenge.lean, Solution.lean and comparator.json | Read in full, with local declaration, definition and configuration inspection. No Lean execution. |
| Independent/UniformAmplifier/Challenge.lean and Independent/RealizedCaps/Challenge.lean | Read in full. Checked the linked ranges against the actual quantified hypotheses and conclusions. |
| LINK_MAP.json; docs/lean_links.json; corpus/comparator_map.json | All exposition links independently inventoried. Relevant declaration/configuration entries, record joins and status distinctions checked. Broader corpus entries sampled. No blanket HTTP availability claim. |
| exemplars/expository.md | All substantive narrative sections, opening, §§1–7, further reading and sources/verification note. Final link-definition tail sampled. Used for teaching structure only. |
| exemplars/qaoa-sk/expository/main.pdf | Visual samples: pages 1, 4, 5, 12, 15 and 20. The other pages were not all visually reviewed. The other theorem's short paper and long record were not comprehensively reviewed. |
| The separate pasted-text attachment | Sampled its section map, relevant editorial exchanges and final handoff context. It is not a substitute for the hash-bound current drafts, and was not exhaustively audited. Its contents are not republished here. |

## Literature supplied in the packet

1. **Ronald de Wolf, Quantum computing: lecture notes, arXiv:1907.09415v6.** Sampled chapter 7 (Grover, unknown success count and amplitude amplification) and the chapter 11 query-model introduction. The amplitude-amplification discussion supplies the teaching standard behind ES-003: a unitary preparation and its inverse need to be identified. Source: literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md; [versioned identifier](https://arxiv.org/abs/1907.09415v6).

2. **Harry Buhrman and Ronald de Wolf, Complexity measures and decision tree complexity: a survey, TCS 2002.** Read selected introduction, address-function and polynomial-preliminary passages, and §§3.1–3.2 on deterministic/randomized query models. Used for ES-028 and the audience calibration. The supplied extraction has damaged characters; only recoverable text was used. Source: literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md and source.pdf.

3. **Scott Aaronson and Andris Ambainis, Forrelation: A Problem That Optimally Separates Quantum from Classical Computing, supplied arXiv:1411.5729v1.** Read the introductory quantum explanation, §1.1.1, and §3.2, printed pp. 13–14. Checked the distinction between the k-query projection experiment and the improved half-query construction. Used for ES-017 and the retained three-input example. This is the supplied preprint version, not a claim to have checked the final SICOMP pagination. [Versioned PDF](https://arxiv.org/pdf/1411.5729v1).

4. **Scott Aaronson, Shalev Ben-David and Robin Kothari, Separations in query complexity using cheat sheets, supplied arXiv:1511.01937v2.** Read the introduction and §3.1 construction. Used to assess the history and inherited addressing idea, without treating the earlier framework as a proof of this construction. [Versioned PDF](https://arxiv.org/pdf/1511.01937v2).

5. **Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao and Avishay Tal, Degree vs. approximate degree and quantum implications of Huang's sensitivity theorem, supplied arXiv:2010.12629v1.** Directly checked the original PDF's Theorem 2 on PDF page 2, which states the quartic D-versus-Q upper bound, and Conjecture 2 on PDF page 20, concerning the cubic R-versus-Q conjecture. The supplied extracted Markdown misnumbers material because of unprocessed restatement commands and also contains damaged mathematical symbols. The exposition's Theorem 2 citation is correct against the PDF; it is not a finding. [Versioned PDF](https://arxiv.org/pdf/2010.12629v1).

The packet also contains Grover, Boyer–Brassard–Høyer–Tapp, Brassard–Høyer–Mosca–Tapp, Huang and Bansal–Sinha QIP slides. These were available as supporting material but were not each read completely. Amplification claims were checked through the supplied preprint/record and de Wolf's notes; this review does not claim an independent full reading of every original amplification paper. Yao (FOCS 1977, pp. 222–227) and Nisan (SIAM J. Comput. 20(6), 1991, pp. 999–1007) were listed as cited-only and were not read.

## Additional primary sources actually consulted

These lookups were used to resolve specific credit, promise, model or proof-structure questions. They do not expand the assignment to new mathematics.

| Primary source | Checked passage and use |
|---|---|
| Ambainis et al., Separations in Query Complexity Based on Pointer Functions, arXiv:1506.04719v3 | §1.3, “Use of a balanced tree,” printed p. 6, explicitly discusses direct pointers from a distinguished element to a zero in every other column and the associated alphabet cost. Supports the narrow credit correction ES-006; does not establish that paper contained this entire addressed-array construction. [PDF](https://arxiv.org/pdf/1506.04719v3). |
| Nikhil Bansal and Makrand Sinha, k-Forrelation Optimally Separates Quantum and Classical Query Complexity, STOC 2021 | Equation (1.3), Proposition 1.2, Theorem 1.3 and Corollaries 1.4–1.5; printed pp. 1304–1305 contain the lower-bound and separation statements. Checked one-sided promise conventions and the cited history. [Primary CWI copy](https://ir.cwi.nl/pub/30886/30886.pdf). |
| Peter Høyer, Michele Mosca and Ronald de Wolf, Quantum Search on Bounded-Error Inputs, arXiv:quant-ph/0304052v2 | §1, printed pp. 1–2, specifies bounded-error subroutines for fixed Boolean values. Used to check ES-023's distinction from arbitrary loser comparison outcomes; no claim that the latter falls directly under this search theorem. [PDF](https://arxiv.org/pdf/quant-ph/0304052v2). |
| Andrew Drucker, Improved Direct Product Theorems for Randomized Query Complexity | Author-deposited full text, §3, Lemmas 3.1–3.2, author page labels 10–11 (PDF pages 12–13 with deposit cover). Checked conditional product posteriors and continuation values for ES-010. The deposit is associated with the 2011 conference version; the exposition cites the 2012 journal publication. The locator here describes the actual deposited file, not unverified journal pagination. [University deposit](https://www.pure.ed.ac.uk/ws/files/19272888/Drucker_2012_Improved_direct_product_theorems_for_randomized_query_complexity.pdf). |
| OpenAI, A Nearly Quartic Separation Between Randomized and Quantum Query Complexity, October 2026 preprint | Official repository location verified; the supplied PDF/text controls detailed claims. Theorem 1.1 gives an existential logarithmic exponent, while the explicit exponent 6 and lower-bound coefficient 1/400 used in the exposition have their more precise support in the reasoning record (ES-021). [Pinned preprint](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). |

## Checks and how to interpret them

The finite enumeration in checks/check_examples.py verifies the N=4 Forrelation census and named inputs, the tournament table, the two-instance AND counterexample, and the independent/dependent selection probabilities. It also verifies the displayed board and local-test arithmetic conditional on S=180, and the m=4 error fraction. Results are in checks/exact_examples.json. It does not establish the existence of a particular 180-gate netlist.

All four figures are visible in the supplied exposition PDF. However, Figure 2 and Figure 4's SVG source files are missing from the packet, and the supplied link map omits those two references. The independent inventory finds 25 distinct destinations versus 23 exposition entries in the supplied map. This supports a source-packaging finding, not a claim of a damaged or incomplete rendered PDF.

PDF text-span measurements support the print-legibility finding ES-020: principal label sizes are approximately 7.02, 8.37, 7.25 and 6.54 points in Figures 1–4 respectively; representative subscripts are 5.01, 5.98, 5.18 and 4.67 points. Figure 4 has the strongest size/contrast concern; Figure 3 adds rotation. These measurements supplement visual judgment rather than impose an arbitrary font-size rule.

Two tempting criticisms were rejected after checking: the planted-pair construction already redraws all address blocks from the promised distribution, so the earlier off-promise losing column is not evidence of a support error; and the sensitivity-paper theorem-number mismatch is an extraction defect, not a wrong PDF citation. ES-008 is limited to the local quantifier on a stage-failure sentence. The adjoining text and source proof supply the intended restriction, so it is not presented as a counterexample to the final theorem.

No Lean compilation, Comparator execution, fresh mathematical proof audit, circuit-netlist execution, or new manuscript typesetting was performed. The review distinguishes source presence, previously recorded build evidence, configured Comparator targets and mathematical meaning. Advice to expose an existing argument is not a request for a new theorem or new formalization.
