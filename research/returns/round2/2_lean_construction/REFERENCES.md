# Sources and exact locators

The local paths below are relative to the input attachment. Public links identify primary sources. The mathematics of the attached OpenAI preprint is attributed to OpenAI. Source inspection and bibliographic verification are distinct from compilation of the proposed Lean proofs.

## OpenAI26

**OpenAI.** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*. 5 October 2026.

- Supplied PDF: `paper/quartic-query-separation.pdf`.
- SHA256: `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`.
- Source pin recorded by the attachment: `openai/math 4eaee875`.
- [Public repository document](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).
- Assigned locators: Section 1.3, equations (1)–(8), Lemmas 2.1–2.2 and their proofs; `paper/extracted.md:18–44,117–295`.
- The public file page was retrieved. The mathematical reading used the supplied PDF extraction and source records; the pinned raw PDF fetch was unavailable.

## AA15

**Scott Aaronson and Andris Ambainis.** *Forrelation: A Problem that Optimally Separates Quantum from Classical Computing*. arXiv:1411.5729.

- [Primary arXiv record](https://arxiv.org/abs/1411.5729).
- Held source: `literature/quartic-ref-01-forrelation-a-problem-that-optimally-separ/`, arXiv v1.
- Exact locator for the direct projection test: Section 3.2, Figure 1 and the k-query construction immediately before Proposition 6.
- Proposition 6 instead gives the distinct half-query construction, rounded up, with acceptance probability linear in the correlation.
- Reading scope: held extraction lines 585–760, covering Sections 3.1–3.2 and Proposition 6.

## BS20

**Nikhil Bansal and Makrand Sinha.** *k-Forrelation Optimally Separates Quantum and Classical Query Complexity*. arXiv:2008.07003v3.

- [Versioned primary text](https://arxiv.org/html/2008.07003v3).
- Exact promise/normalization: equations (1.1)–(1.3), and Proposition 1.2 for their quantum test.
- Cited lower bound: Theorem 1.3 and Corollary 1.4.
- Held TeX: `main.tex:213–240` for normalization and promise, `261–278` for the main lower-bound statements, `767–799` for Fourier-weight ingredients, and `1166–1191` for Section 5.4.
- The inequality qualification concerns `main.tex:1184`, the third inequality in the main display. It is supported by the supplied independent adjudication and a direct reading of the TeX. No claim that Theorem 1.3 is false is made.

## dW26

**Ronald de Wolf.** *Quantum Computing: Lecture Notes*. arXiv:1907.09415v6, 27 August 2026.

- [Versioned arXiv record](https://arxiv.org/abs/1907.09415v6).
- [Author’s PDF](https://homepages.cwi.nl/~rdewolf/qcnotes.pdf).
- Exact oracle and phase-kickback locator: Section 2.4, printed pp. 17–18.
- Query model and partial domains: Section 11.1, printed p. 89.
- Held source: `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md:345–353,1582–1592`.
- The author’s current PDF and the versioned record were checked; the supplied extraction anchors the local reading.

## ABK16

**Scott Aaronson, Shalev Ben-David and Robin Kothari.** *Separations in Query Complexity Using Cheat Sheets*. arXiv:1511.01937v2.

- [Versioned primary text](https://arxiv.org/html/1511.01937v2).
- Exact locator: Section 6.1, Definition 14 (certifying function), Definition 15 (cheat-sheet version), Theorem 16 and Lemma 17.
- The packet’s source extraction uses different numbering for these items. Use the official versioned numbering when citing them in a manuscript.
- Used for the addressed-certificate role and total verification of partial inputs.

## ABB+15

**Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha and Juris Smotrovs.** *Separations in Query Complexity Based on Pointer Functions*. arXiv:1506.04719v3.

- [Versioned primary text](https://arxiv.org/html/1506.04719v3).
- Exact locator: Section 1.3, “Use of a balanced tree”, including the paragraph immediately following the tree analysis that discusses direct pointers to a zero in every nonmarked column.
- Held extraction: `literature/quartic-ref-04-separations-in-query-complexity-based-on-p/extracted.md:260–275`.
- Used for bibliographic scope, not as a formal proof dependency of the new modules.

## Formal source and adjudication

The formal source is `repository/lean/` at the attachment’s repository commit `4c7544f8dcdfc18d3ecf8476ebd8c1090cd46f15`. The full dependency revisions are in the supplied `lean/lake-manifest.json`.

The source/evidence record consists of `repository/corpus/statements.json`, `ties.json`, `lean_dependencies.json` and the attached receipts, interpreted with `BUILD_STATUS.md`. Relevant review verdicts are in `repository/research/adjudication/adjudication.json`, `funnel_adjudication.json`, `funnel_adjudication_notes.md` and `bansal_sinha_section54_second_reading.md`.

The return preserves the current adjudicated rows. Previous-round drafts are proposal history and do not establish checked statements. The exact read scope, including files read only in part, is recorded in `SOURCE_RECEIPT.json` and `source_records/contribution_reading_receipts.json`.
