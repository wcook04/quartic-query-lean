# Sources, reading coverage and limits

This is a referee report on the supplied **short expert companion**. The exposition, long record, literature and Lean sources were used to check its claims, attribution and navigation. The supplied current Markdown is authoritative. The report does not replace the manuscript, introduce a theorem, or request additional formalisation.

The principal conclusion is limited but substantive: no failure of the central separation was found in the arguments inspected. That is a mathematical reading judgment, not a formal certificate. The local mathematical errors are separated from attribution, navigation and editorial suggestions in `findings.json`.

## 1. The submitted material

| Source | Actual coverage and use |
| --- | --- |
| `READ_ME_FIRST.md` | Read in full, including the 14 predecessor-review topics and the instruction to take the newest completion claims as stated. The user's request for one ZIP determines the delivery format. |
| `paper/extracted.md` | The extracted text of the supplied 19-page preprint was read in full, including Appendix A and references. This supplied text, rather than an inaccessible remote copy, is the basis for the construction and proof comparison. |
| `repository/docs/expert_companion.md` and `.bib` | Read in full. Every final finding's quotation was checked against the current Markdown, not a predecessor. |
| `repository/docs/expert_companion.pdf` | All 13 pages inspected as rendered contact sheets; pages 1, 3, 5, 8, 10 and 11 additionally examined at larger resolution. PDF text and annotations were inspected for selected statements, headings and links. See `checks/pdf_review.json`. |
| `repository/docs/exposition.md` | Read through as supporting material. The construction, exponent account, comparison argument, example calculations and formal appendix were cross-checked where relevant. This is not a second full pedagogical referee report. |
| `repository/docs/exposition.pdf` | All 13 pages inspected in rendered contact sheets, especially the board and planted-pair figures. |
| `repository/docs/reasoning_record.md` | Targeted reading, not all 116 PDF pages or all current Markdown: §§2.1–2.5 on the query models and bridges; §2.8 on evidence boundaries; §3.15 on the uniform Forrelation estimate; §§3.16–3.18 on attribution and source scope; §§5.2–5.4 on comparison, amplification, coupling and cost; §§6.1 and 6.4–6.6 on capped products, erased zeros, simulation and discrepancy; §§7–7.2 on the fixed-parameter exponent deduction. The heading/anchor inventory and relevant surrounding passages were also inspected. |
| Record PDF and `reasoning_record.since_pdf.diff` | The version mismatch was checked through `SOURCE_STATUS.json` and the supplied two-line diff. The older PDF was not used to override current Markdown. No claim of a complete visual audit of its 116 pages is made. |
| `SOURCE_STATUS.json`, `manifest.json`, `LINK_MAP.json`, `repository/docs/lean_links.json`, `repository/corpus/comparator_map.json` | Parsed and checked. All 88 input-manifest entries matched their supplied bytes and hashes; the assignment hash was checked separately. The link inventory was independently checked against local supplied files. |
| Structural exemplars | Openings, section organization and formal-scope blocks of the short and expository SK examples were sampled for register. The long exemplar was not read through. These concern another theorem and provide no mathematical evidence here. |
| Supplementary pasted trace | Indexed and selectively searched for assignment, version and earlier-review context. It was not read end-to-end and was not treated as authority for the current mathematics. The report does not reproduce the trace. |

### Mechanisms inspected

The inspected proof spine comprises the separate per-column arrays and outward certificates; the winner's one-sided guarantee against unpromised rivals; the fractional-weight drift identity; retained-state sampling and history-conditional coupling; verification of the returned candidates; the planted dummy/one-input pair; the fair capped direct-product induction with jointly independent auxiliary information; the whole-run erased-zero identity; the fixed-time simulator's **joint** light-and-hit event; and the order of the fixed-parameter asymptotic quantifiers. The alternative analytic Forrelation proof was sampled for its assembly, hypotheses and attribution, not independently re-proved in full. The relevant current passages and distinctions are reflected in ER-004–008, ER-013, and ER-032–040.

## 2. Supplied primary literature

“Targeted” means the named sections or statements were read, with the listed PDF spots checked where appropriate. It does not mean that every proof and appendix of that source was audited. Version-specific locators below refer to the editions actually supplied. Some extracted Markdown renumbers statements; the PDF numbering is used when it differs.

| Work and edition | Actual coverage | Use in this review |
| --- | --- | --- |
| Aaronson–Ambainis, [arXiv:1411.5729v1](https://arxiv.org/abs/1411.5729v1) | Targeted introduction and §1.1.3, including the k-fold definition and conjecture, supplied PDF p. 4. Not the full lower-bound proof. | Origin of the explicit Forrelation problem and conjecture. |
| Aaronson–Ben-David–Kothari, [arXiv:1511.01937v2](https://arxiv.org/abs/1511.01937v2) | Targeted introduction, Theorem 1, the conditional cubic consequence, §3.1 and start of §3.2; AND–OR/certificate discussion at printed pp. 9–10. | Total-function history, answer-based addressing and the scope of the particular cubic construction. |
| Aaronson–Ben-David–Kothari–Rao–Tal, [arXiv:2010.12629v1](https://arxiv.org/abs/2010.12629v1) | Targeted introduction and quartic upper-bound derivation; Theorem 2 at PDF p. 2 and Conjecture 2 at PDF p. 20 checked in the PDF. | Correct upper-bound credit and the conjecture addressed by the new separation. |
| Göös–Pitassi–Watson, ECCC TR15-050, supplied edition | Targeted §§2 and 2.1, printed pp. 4–5: alphabet convention, motivating all-one column, pointer-chain construction. Not the communication simulation proof. | Precise pointer-function antecedent and representation issues. |
| Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs, [arXiv:1506.04719v3](https://arxiv.org/abs/1506.04719v3) | Targeted abstract, introduction, main-result statements, pointer definition and §1.3. The “Use of a balanced tree” direct-pointer/exponential-alphabet paragraph was checked at PDF p. 6. | Direct pointers, bit-access costs and the distinction between earlier D-versus-Q and the present R-versus-Q result. |
| Tal, [arXiv:1912.12561v1](https://arxiv.org/abs/1912.12561v1) | Targeted abstract and introduction, including the 8/3 total-function consequence at printed pp. 2–3 and the random-orthogonal/Walsh distinction. Not the Fourier proof. | Intermediate historical exponent and the partial problem used to obtain it. |
| Bansal–Sinha, [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3) | Targeted introduction, promise/normalization, Theorem 1.3, Corollaries 1.4–1.5 at PDF p. 4, and the beginning of the technique overview. Not the full interpolation proof. | Hardness of the explicit Walsh promise used by the current construction. |
| Sherstov–Storozhenko–Wu, [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4) | Targeted §§1.1–1.3 and §1.8 in full, with technique-overview sampling. Theorem 1.1 at PDF p. 3, Theorem 1.5 at p. 4 and §1.8 at p. 10 checked. The record's use of the Fourier-growth corollaries was checked separately from the Rorrelation theorem; no full proof audit of Fourier growth. | Independent optimal separation; random orthogonal Rorrelation versus explicit Walsh Forrelation; correct attribution of the record's derived transfer. |
| Huang, [arXiv:1907.00847v2](https://arxiv.org/abs/1907.00847v2) | Targeted introduction, main statements and §2 signed-cube matrix lemmas. The subsequent main-theorem proof was not independently inspected. | The sensitivity theorem's role in the upper-bound history. |
| Ben-David–Kothari, [arXiv:2609.15063v1](https://arxiv.org/abs/2609.15063v1) | Supplied extracted text read through, especially §3 and Lemma 5's fixed-tournament reduction and final verification. | The nearest comparison/certificate predecessor and what changes in the off-promise probabilistic setting. |
| Ambainis–Iraids–Kokainis, [arXiv:2609.11664v2](https://arxiv.org/abs/2609.11664v2) | Targeted introduction, §§2–3 opening and §§6.1–6.3 through the beginning of Lemma 6.6's proof. Algorithm 4 and candidate identities at printed p. 12, fixed-edge comparison at p. 13, and source guarantee at p. 15 checked. | Candidate elimination and its fixed-edge hypothesis. The online landing page has a later v3; no v3 pagination was substituted for the supplied v2. |

The independent optimal total-function consequences of Bansal–Sinha and Sherstov–Storozhenko–Wu are preserved as shared credit. The correction in ER-001 concerns the **explicit Walsh conjecture**, not ownership of the optimal separation exponent. ER-008 similarly distinguishes the record's Walsh consequence of a Fourier-growth theorem from SSW's random-orthogonal lower bound. See the versioned primary sources above, especially SSW §1.8.

The following supplied items were not substantively read as original proofs for this report: Girish–Tal–Wu's *Fourier Growth of Parity Decision Trees*; Girish–Servedio's additional Forrelation paper; the Bansal–Sinha QIP slides; the Buhrman–de Wolf survey; Midrijanis; and Nisan–Szegedy. Where the long record's attribution to them was inspected, that is a reading of the record, not an independent verification of those papers. The cited-only originals of Yao (1977), Nisan (1991), and Barnum–Saks–Szegedy were not read. Shaltiel's original fair-product argument was not independently read; its provenance and role were checked in Drucker's primary treatment below.

## 3. Additional primary-source research

| Primary source | What was actually checked |
| --- | --- |
| [SSW, official arXiv HTML for v4](https://arxiv.org/html/2008.10223v4) | §§1.1–1.3 and §1.8, cross-checking the supplied PDF's explicit/random distinction and the discussion of Bansal–Sinha. HTML statement numbering was not substituted for the supplied PDF numbering. |
| [Høyer–Mosca–de Wolf, *Quantum Search on Bounded-Error Inputs*](https://arxiv.org/pdf/quant-ph/0304052) | Introduction, PDF pp. 1–2: fixed Boolean values computed with bounded error. This verifies the comparison-model distinction, not the whole robust-search proof. |
| [Dürr–Høyer, *A Quantum Algorithm for Finding the Minimum*](https://arxiv.org/pdf/quant-ph/9607014) | Two-page primary text, including the ordered-value model, Theorem 1, threshold changes and fixed timeout. |
| [Mande–Paraashar–Saurabh, FSTTCS 2023 publisher page](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.30) | Abstract, tournament definition/model and theorem summary. The full proof was not read. Arbitrary orientations of complete graphs include directed cycles; this supports ER-002. |
| [Drucker, *Improved Direct Product Theorems for Randomized Query Complexity*, arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644v2) | §1.3 at printed pp. 6–7 and Lemmas 3.1–3.2 at printed pp. 11–12: the fair per-instance-cap argument, product posterior and value process. The stronger total-budget theorem was not conflated with the capped statement used here. |

Source identities and editions were also checked on primary arXiv landing pages. No secondary commentary was used as authority for the mathematics. Tool access failures for two GitHub pages did not establish that the public links were broken; no such failure was promoted to a finding. Repository URLs in the retained link audit were checked against the supplied local bytes and pinned revision metadata, not a live remote checkout.

## 4. Lean statements and evidence

The following were read in full: the Unconditional `Challenge.lean`, `Solution.lean` and `comparator.json`; all six supplied Independent challenge files (ConstructionFull, Degree, Eq19, ModelZero, RealizedCaps and UniformAmplifier); `QuarticQuery/Paper/ConstructionFamily.lean`; and the supplied Lean README, Lake configuration and `scripts/Reach.lean`.

Additional targeted source reading covered the Construction challenge's compared block; `Upper/Bound.lean`'s abstract and explicit budgets; `Paper/ClassicalPlanted.lean`'s probability identities and per-time events; `LowerBound/Planted/ZeroSearchSuccessor.lean`'s statement; and `ForrelationLower/Uniform.lean`'s sharp endpoint. Exact source line ranges supporting individual findings are in their evidence arrays.

The four headline wrapper names and their quantifier structure match the supplied challenge, solution and Comparator configuration. The report distinguishes four kinds of evidence: bytes present in a packet, a reported build, a reported comparison run, and assessment that the statement expresses the intended mathematics. **No Lean build, Comparator run, or new compilation was performed.** The newest completion claims exempted by the brief were accepted as stated. ER-023 asks for a useful navigation link to existing run evidence; it does not dispute pending status.

## 5. Reproducible checks and their limits

- **Exact locators and binding:** every finding quote occurs verbatim in current Markdown and has at most 25 whitespace-delimited words. The six draft hashes are copied without change from `SOURCE_STATUS.json`. The full input manifest and assignment hash were verified.
- **Local navigation:** an independent scan found 77 used destinations across the two drafts, including three image references absent from the supplied 74-link map. Supplied local targets, explicit anchors and line-range existence were checked; the semantic usefulness of key targets was reviewed separately. An existing line range can still omit a theorem's conclusion.
- **Finite examples:** `checks/check_examples.py` uses integer enumeration and `fractions.Fraction` to reproduce five examples already in the draft/record. The returned JSON records the complete small computations. Restoring the record's omitted no-discovery fallback yields the advertised planting probability. These calculations validate the printed examples, not the general theorems.
- **PDFs:** the supplied PDFs were rasterized with Poppler and visually inspected. No replacement manuscript PDF was built. An automated expert-PDF word-box check found no words outside the physical page; it does not prove absence of every layout defect.
- **Return integrity:** `checks/validate_return.py` validates the return's file hashes, structured findings and finite results, and optionally checks the original source packet. The final ZIP was also checked for CRC errors, duplicate or unsafe member paths, and byte-for-byte agreement after extraction. The internal manifest describes every other file, not itself or the enclosing ZIP.

Each source-supported correction has its own evidence locator in the findings. The priorities in `verdict.md` are editorial judgments drawn from those findings; they are not additional claims of mathematical failure.
