# Sources read, source editions, and limits

This inventory records the combined reading behind the 43 findings. It distinguishes reading a document, examining selected passages, inspecting an existing PDF, and checking a finite example. The panel models a strong graduate student and a lecturer using the prerequisites and presentation choices of primary literature. It is not a reader experiment, and no opinions are attributed to the named authors. Pedagogical judgments remain judgments: a source can establish a mathematical distinction or demonstrate a teaching practice without proving that a particular student will struggle.

All packet paths below are relative to the **original input ZIP**, not this return directory. The original sources are not duplicated in the return.

## 1. Attachment and edition boundaries

The working corpus was `quartic_r6_students_and_teachers.zip`: three current Markdown documents, their supplied PDFs, the target preprint, earlier review material, writing-method files, reader principles, source metadata, Lean sources and literature. The manifest lists **42 supplied literature items**, plus three cited-only references. Presence in this corpus does not mean substantive reading; the nine literature entries below specify the material actually used. The remaining corpus was available for locating references, but this report makes no claim to have read all 42 items.

`READ_ME_FIRST.md`, `reader_principles.md`, `SOURCE_STATUS.json`, `manifest.json` and the relevant link information supplied the assignment and provenance boundaries. The six draft hashes in `findings.json` reproduce the input status object. The manifest states that member hashes identify the supplied bytes and that the repository commit is provenance. Thus a repository commit, a source file, a recorded check and an instructional recommendation are kept separate.

**Current Markdown controls quotations and findings.** The source status explicitly warns that the current record Markdown differs from its accepted review and from the recorded PDF source edition. We therefore use `repository/docs/reasoning_record.pdf` for its actual pagination and visible contents, not as a certified rendering of every current Markdown passage. Its visible first page was inspected; no inference that a particular guide is absent follows merely from the edition warning. PDF measurements and Markdown reading judgments are distinguished in `weighting.md`.

The supplied target preprint is **OpenAI, _A Nearly Quartic Separation Between Randomized and Quantum Query Complexity_, 5 October 2026**, at `paper/extracted.md` and `paper/source.pdf`. Its bibliography gives this [pinned GitHub PDF URL](https://github.com/openai/math/blob/4eaee875/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf). We read the supplied local text from the exact packet bytes at the scopes below; **the pinned remote PDF was not independently retrieved or verified**. The preprint is the construction being explained, not external confirmation of its theorem. The separate supplied conversation trace was indexed and sampled around the current request and packet preparation; its roughly 4 MB were not read end to end or used as mathematical authority.

## 2. Current documents and supporting packet material

### Read completely

- **`repository/docs/exposition.md`:** all sections, bibliography references and generated link definitions. This was the primary review target. Multiple independent readings informed the student, lecturer and mechanism perspectives.
- **`repository/docs/expert_companion.md`:** the complete body and generated links were read during integration. Independent subreviews concentrated on the opening, construction, quantum interfaces, direct-product proof, parameter discussion and Appendix A. Complete reading here does not mean independently proving every assertion.
- **Assignment and method:** `READ_ME_FIRST.md`, `reader_principles.md`, `skills/README.md`, `skills/record-to-expository/SKILL.md`, and `skills/long-to-short/SKILL.md`. These support the method findings and distinguish a weak instruction from failure to apply an instruction already present.
- **`previous_round/dispositions/exposition.json`:** every disposition, including the earlier repairs to examples, hypotheses, proof links and evidence wording. Earlier verdicts and selected expert/record dispositions were also consulted to avoid proposing already completed repairs.

### Read selectively, with boundaries

**`repository/docs/reasoning_record.md`.** The reading guide and §1 were read completely, as was §7. Targeted reading covered the query-model definitions in §2; the Forrelation setup and repetition discussion in §3.3; the complete small-instance census in §3.5; the ingredient interface; local tests around `#AC-example-tests`; the amplifier contract, proof and returned-register explanation in §5.1; the tournament preparation and worked example in §5.2; and the classical mechanisms in §§6.1–6.5. The simulator, its four-query trace, abort branch, joint event and union-bound use were read through the §6.6 introduction. Appendix B's introductory role and selected correspondence passages were read, not its entire catalogue.

Particularly important destinations were `#upper-stage-state`, `#upper-cyclic-example`, `#CL-product-law`, `#CL-adaptive-example`, `#CL-normalization`, `#CL-first-difference`, `#CL-heavy`, `#CL-simulator`, `#CL-joint-event` and `#CL-simulator-example`. The normalization passage explicitly connects the conditional and unnormalized proofs; the simulator passages establish which budgets are shared and which are per instance. These are existing explanations to direct readers toward. The long Gaussian hardness development and all formal correspondence entries were **not** read in full.

**`paper/extracted.md`.** Targeted reading covered §1, including the historical and proof overviews; the §2 ingredients and construction interfaces; §§3.1–3.2 on amplification and the tournament; §4's planted-pair lower bound; and §5's parameter argument. Appendix A was not read completely. The preprint was used to distinguish what the construction already proves from what its teaching documents omit, compress or differently emphasize. For example, its overview already distinguishes exposing the erased zero from guessing the hidden address, and §4.2 explains why counting every cell visit is a safe overestimate.

**Figures, earlier reviews and Lean text.** The complete sources of `repository/docs/figures/exposition/fig3_tournament.tex` and `fig4_planted.tex` were read to check the table and planted-example conventions. Earlier expert/record dispositions and statement-fidelity material were sampled for the particular fixes at issue. The exemplars about another theorem were not used as a substantive mathematical comparison. A small amount of Lean statement text was inspected for evidence wording, especially `repository/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean`, lines 37–48. Its factorization, exact success mass and positivity clauses show why SX-040 asks for the actual comparison reason rather than declaring that the formal statement cannot be stronger.

### PDF scope

All **14 supplied exposition pages** were rendered to images and visually inspected. The expert companion's first page and the record's first page were also visually inspected. Text extraction measured headings across all three PDFs: 14, 14 and 125 pages respectively. These measurements establish space allocation, not reading time. Selected literature PDF pages were inspected or text-extracted to resolve theorem numbering, as specified below. No new manuscript PDF was typeset, and there was no full visual inspection of all expert-companion or record pages.

## 3. Primary literature used

The links below identify primary manuscripts or author-hosted material. Exact arXiv versions matter: an online revision date need not equal a conference or journal publication year. Primary pages were opened to verify bibliographic identities and versions; detailed comparisons use the supplied full text. Search results were not substituted for the technical passages. Where extraction renumbered a proposition or lemma, the source PDF supplied its printed number.

### 1. Buhrman–de Wolf: query-model background

Harry Buhrman and Ronald de Wolf, **_Complexity Measures and Decision Tree Complexity: A Survey_**, _Theoretical Computer Science_ (2002). [Author-hosted PDF](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), dated 10 October 2002. Packet: `literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md` and `source.pdf` in that directory.

**Read:** introduction, the §2 definitions including the address-function discussion, and §§3.1–3.3 on deterministic, randomized and quantum query models; §§4–5 were sampled. The extraction has OCR damage, so only unambiguous passages supported claims. This anchors the assumed student's knowledge of query cost, worst-branch conventions, oracle access and reversible simulation. It supports SX-001's prerequisite discussion without assuming familiarity with the new construction. The survey was not read completely.

### 2. de Wolf: quantum algorithms and teaching practice

Ronald de Wolf, **_Quantum Computing: Lecture Notes_**, [arXiv:1907.09415v6](https://arxiv.org/abs/1907.09415v6), 27 August 2026. Packet: `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`; accompanying `source.tar.gz`.

**Read:** preface and revision notes; bit- and phase-query explanations and selected Chapter 2 exercises; Chapter 7's Grover and amplitude-amplification development, variants and exercises; selected notation, asymptotic and probability material in Appendix 23.1–23.2. The organization of hints was sampled. This supports prerequisite and assignment-route questions, the need to reconstruct actual sampler states and probabilities, and changed-case tasks in SX-001–003, SX-007 and SX-019–020. Exercises demonstrate a teaching comparator, not measured educational effectiveness. The remaining chapters were not read as a book.

### 3. Aaronson–Ben-David–Kothari: why cheat sheets incur a certification cost

Scott Aaronson, Shalev Ben-David and Robin Kothari, **_Separations in Query Complexity Using Cheat Sheets_**, STOC 2016; [arXiv:1511.01937v2](https://arxiv.org/abs/1511.01937v2), revised 9 July 2019. Packet: `literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md`, with `source.pdf` and `source.tar.gz`.

**Read:** overview-of-techniques material and §3.1; §3.2's opening construction, checking and first-difference discussion was sampled. Especially relevant are extracted lines 1331–1337 and 1417–1431: domain certification motivates the AND-OR step, and multiple hard answers address the cheat-sheet array. This grounds SX-005 and SX-011: explaining the purpose of the earlier construction and the address length is more informative than giving exponent arithmetic alone. Later separation proofs were not comprehensively reviewed.

### 4. Bansal–Sinha: the precise partial-function ingredient

Nikhil Bansal and Makrand Sinha, **_k-Forrelation Optimally Separates Quantum and Classical Query Complexity_**, STOC 2021; [arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3), 17 November 2020. Packet: `literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/extracted.md`, `source.pdf`, and `source.tar.gz`; a proceedings PDF is also supplied under `supplements/`.

**Read:** introductory definitions, results and early proof overview; the first five source-PDF pages were checked to establish the printed numbering of Proposition 1.2, Theorem 1.3 and Corollary 1.4. Proposition 1.2's sign-sensitive experiment accepts with probability \((1+\Phi)/2\); the exposition's chosen projection test has probability \(\Phi^2\). This supports the limited comparison in SX-010, not a charge that the chosen test is invalid. The explicit hard promise also anchors SX-015 and the optional external-ingredient route in SX-042. The complete Gaussian proof was not independently reviewed.

### 5. Drucker: adaptive direct products

Andrew Drucker, **_Improved Direct Product Theorems for Randomized Query Complexity_**, _Computational Complexity_ 21 (2012); [arXiv:1005.0644v2](https://arxiv.org/abs/1005.0644v2), 9 May 2014. Packet: `literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md`, `source.pdf`, `source.tex`, and `supplements/supplied-2014.pdf`.

**Read:** introductory motivation, especially §1.3, and §3 through the observation about fair algorithms. PDF pages 11–12 were text-checked for Lemmas 3.1–3.2, which the conversion renumbers. The relevant mechanism is a continuation value with remaining budget, a product posterior at a fixed full transcript, and one-factor change per query. This supports SX-028, SX-030 and SX-038. The fair per-instance-cap application is distinguished from the paper's more general pooled-budget theorem; the review does not import the latter merely from its title. Other theorem variants were not fully read.

### 6. Brassard–Høyer–Mosca–Tapp: what amplification guarantees

Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp, **_Quantum Amplitude Amplification and Estimation_**, _Contemporary Mathematics_ 305 (2002); [arXiv:quant-ph/0005055v1](https://arxiv.org/abs/quant-ph/0005055v1), 15 May 2000. Packet: `literature/quartic-ref-12-quantum-amplitude-amplification-and-estima/extracted.md`, `source.pdf` and `source.tex`.

**Read:** §2 through Theorem 3. Rotation preserves the good-state direction, while the unknown-success-probability QSearch result has an expected-cost formulation and can run forever at zero success mass. This supports preserving the exposition's unconditional cap and stopping rule, SX-021–022, and separating the returned-state guarantee from other conclusions in SX-040. The amplitude-estimation development was not reviewed. The new fixed-cap formulation remains a statement of the supplied preprint and record, not a theorem credited verbatim to this source.

### 7. Høyer–Mosca–de Wolf: the interface of bounded-error search

Peter Høyer, Michele Mosca and Ronald de Wolf, **_Quantum Search on Bounded-Error Inputs_**, ICALP 2003; [arXiv:quant-ph/0304052v2](https://arxiv.org/abs/quant-ph/0304052v2), 14 April 2003. Packet: `literature/quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error/extracted.md` and `source.tar.gz`.

**Read:** §§1–2 and the beginning of §3. The base algorithms compute fixed bit-values with a bounded-error margin. An arbitrary comparison between losing candidates need not supply that interface. This helped assess the failed-shortcut explanations and the distinction among dominance, a valid witness and a reliable predicate, especially the material preserved by SX-017 and SX-037. The review does not claim that every robust-search construction fails; it checks the hypotheses of this cited route. Later proof details were not fully reviewed.

### 8. Ambainis et al.: pointer-function credit

Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha and Juris Smotrovs, **_Separations in Query Complexity Based on Pointer Functions_**, _JACM_ (2017); [arXiv:1506.04719v3](https://arxiv.org/abs/1506.04719v3), 26 October 2015. Packet: `literature/quartic-ref-04-separations-in-query-complexity-based-on-p/extracted.md`, `source.pdf` and `source.tar.gz`.

**Read:** introduction, the Göös–Pitassi–Watson construction motivation and balanced-tree discussion, particularly extracted lines 260–275. Direct pointers are explicitly discussed there, with exponential alphabet size identified as the concern. This verifies that the current historical framing should preserve ingredient-level credit instead of presenting direct pointers as unprecedented. It helped prevent repetition of earlier repaired attribution findings. The later algorithms were not read in full; no new priority judgment is claimed.

### 9. Sherstov–Storozhenko–Wu: supplementary historical cross-check

Alexander A. Sherstov, Andrey A. Storozhenko and Pei Wu, **_An Optimal Separation of Randomized and Quantum Query Complexity_**, _SIAM Journal on Computing_ (2023); [arXiv:2008.10223v4](https://arxiv.org/abs/2008.10223v4). Packet: `literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/extracted.md`, `source.pdf` and `source.tar.gz`.

**Sampled only:** introductory §1.8, “Independent work by Bansal and Sinha,” extracted lines 184–198. This describes the concurrent results and distinguishes explicit Forrelation from the random-matrix construction and their different techniques. It supports careful historical context, not a review of either full hardness proof. The version is identified by the packet; this supplementary entry does not claim an additional independent remote-version check.

## 4. What the checks establish

Exact quotation checks tie findings to current Markdown. The delivered finite-example script checks the supplied small Forrelation universe, selected sampler probabilities and elementary probability/cap examples. These computations clarify already existing illustrations; they neither prove the asymptotic separation nor establish formal correctness. The one-shot decoder diagnostic, for instance, concerns the raw projection experiment and does not contradict the amplified decoder.

No Lean compilation, kernel replay, Comparator invocation or formal-receipt rerun was performed. The assignment supplied the accepted formal-check status as context. SX-040 concerns the explanation of a comparison label; SX-041 concerns a visible comment-to-link edition mismatch. Neither reopens the accepted checks or infers that a theorem failed.

Yao 1977, Nisan 1991 and Barnum–Saks–Szegedy 2003 remain **cited only** and were not read. Other supplied literature, including sources mentioned through another author's bibliography, is not silently promoted to “read.” No exhaustive source-code audit or independent proof of the full preprint is claimed. Recommendations about examples, optional routes and assessment tasks are this panel's advice, distinguished throughout from mathematical facts credited to the preprint, current drafts or primary literature.
