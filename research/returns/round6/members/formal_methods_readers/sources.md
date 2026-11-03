# Sources, research and reading coverage

All packet paths below are relative to the original supplied archive. They identify sources; the return does not duplicate those files. **Read in full** means read for this reader-panel assessment, not independently proved correct. **Sampled** names the actual passages inspected. The findings combine explicit source observations with clearly identified editorial judgments.

## 1. What was read

### Current documents and instructions

Across the review, all three current Markdown documents were read in full, including the short papers’ generated source-link definitions and the record’s narrative, ordinary proofs, formal-correspondence paragraphs, appendices and 121 literal catalogue entries. The main reviewer read the complete supplied OpenAI preprint; the record and short-paper reviews also made targeted cross-checks against it. The assignment, all fourteen reader principles, all three supplied writing-method files and the source-status metadata were read. These documents supplied the task boundary and the current text to quote.

The current record Markdown is authoritative. `SOURCE_STATUS.json` says it has 694 changed lines relative to the accepted-review state and that its supplied PDF comes from an earlier Markdown edition. The two short PDFs have 14 pages each; the older record PDF has 125. Every PDF page was structurally inspected by extracting text and heading positions; selected pages were rendered and visually inspected. Visual inspection covered expert pages 11–12, exposition pages 12–13 and older-record pages 15 and 93. This was not a fresh render of the current record.

The attached pasted trace was sampled for the current assignment and revision context. It was not fully reread line by line, and its private correspondence is not reproduced. Its latest relevant directive agrees with the packet’s advice-only, no-rewriting scope.

### Formal artifacts and evidence rules read in full

| Packet source | Purpose in this review |
| --- | --- |
| `repository/lean/QuarticCorpus/Unconditional/Challenge.lean`, `Solution.lean`, `comparator.json` | Public definitions, four configured types, forwarding implementation and comparison scope. The challenge contains deliberate proof placeholders. |
| `repository/lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean` | Precise retained-state statement and its imported vocabulary boundary. |
| `repository/lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean` | Finite weighted-seed endpoint and independently stated comparison target. |
| `repository/lean/QuarticQuery/LowerBound/RealizedCaps.lean` | Clipping, recursive compliance, actual path/count and the joint success event. |
| `repository/lean/QuarticCorpus/Independent/Semantics.lean`, `SemanticMutations.lean`, `Controls/SharedAudit.lean` | Independently expected finite examples, nearby model mutations and the shared impossible-premise control. |
| `repository/lean/QuarticQuery/Paper/ConstructionFamily.lean` | Same-circuit witness and explicit-family/constant distinctions. |
| `repository/lean/scripts/Reach.lean` | What the dependency traversal actually visits and projects, including hidden-path witnesses. |
| `repository/docs/statement_evidence_contract.md` | Separate statement, route, reach, source-bound review and execution facts. |
| `previous_round/round5_statement_fidelity.md` | Later automated textual review; no assumption that its existence refreshes corpus bindings. |
| `previous_round/dispositions/reasoning_record.json` | Prior dispositions, especially the statement-first route, optional proofs, historical appendix, immutable ledger and expanded-support correction. |

Other material was **sampled**, not audited exhaustively: short-paper dispositions relevant to models, scopes, figures and evidence; `repository/docs/reasoning_record_correspondence.json` branch structure and selected entries; `repository/corpus/comparator_map.json` metadata, vocabulary and selected declarations; `repository/docs/lean_links.json` metadata, source pins and link roles; the `eq_21` signature and context in `ClassicalPlanted.lean`; selected SK exemplar openings and formal-scope passages; and selected revision summaries. The catalogue was read, but the large correspondence object and every formal proof were not independently rechecked.

## 2. Primary mathematical literature actually used

### S01 — OpenAI preprint: full supplied text

**OpenAI, _A Nearly Quartic Separation Between Randomized and Quantum Query Complexity_, 5 October 2026.** Packet: `paper/extracted.md` and `paper/source.pdf`.

The full extracted paper was read: introductory conventions and Theorem 1.1; addressed construction and Lemma 2.2; quantum tournament and verification; direct-product and planted-pair classical argument; final parameter choice and source roles. Its opening fixes worst-case bit queries, including internal randomness and measurement outcomes. The theorem and construction remain OpenAI’s contribution; the documents under review explain and formalise them. The review does not turn explanatory constants or later diagnostics into new original mathematics. See expert §1, record §§4.8, 5.5, 6.7 and Appendix B. [FX020, FX022–FX024, FX045, FX047]

### S02 — Buhrman–de Wolf: sampled standard query models

**Harry Buhrman and Ronald de Wolf, _Complexity measures and decision tree complexity: a survey_.** Packet: `literature/quartic-lit-buhrman-dewolf-decision-tree-survey/extracted.md`.

Read introductory context and §§3.1–3.3, printed pp. 5–8: randomized distributions over decision trees, worst-case cost/error conventions, and the quantum query model. This anchors questions about the same algorithm before the input quantifier, hard resource caps and the standard-model bridges. It does not by itself prove equivalence to every detail of the supplied Lean implementation. Those bridges are supplied in record §§2.2–2.5. [FX003–FX006, FX036–FX039]

### S03 — Beals et al.: sampled oracle model; convention caveat

**Beals–Buhrman–Cleve–Mosca–de Wolf, _Quantum lower bounds by polynomials_.** Packet: `literature/quartic-ref-08-quantum-lower-bounds-by-polynomials/extracted.md`.

Read §§3.1–3.2. The fixed-sequence quantum model and bit-XOR oracle are relevant to the quantum semantics questions. **The supplied edition describes classical randomized cost using an expected-query convention.** It is therefore not used as unqualified evidence that the record’s all-coin hard cap is the convention of every cited source. The Buhrman–de Wolf and preprint conventions supply the relevant hard-cap anchors here. This is a source-selection qualification, not a new defect alleged in the drafts.

### S04 — Høyer–Mosca–de Wolf: sampled subroutine assumptions

**Høyer–Mosca–de Wolf, _Quantum search on bounded-error inputs_.** Packet: `literature/quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error/extracted.md`.

Read the introduction, preliminaries and portions of the algorithm discussion. These ground the bounded-error-predicate reader’s expectations. The source is not used to certify the record’s whole retained-state amplification construction or to replace its precise interface. [FX007, FX035, FX041]

### S05 — Drucker: sampled adaptive product proof in detail

**Andrew Drucker, _Improved direct product theorems for randomized query complexity_, supplied arXiv v2.** Packet: `literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md`.

Read the introduction through the direct-product scope, §2.1 definitions, and §3’s conditional-value argument, transcript/product-law lemmas, product estimate and final fair-algorithm remark. Later extensions were not fully read. The source’s global-budget theorem is not silently substituted for the record’s separate-cap vector-output statement. The method is the relevant inheritance; the record gives the needed adaptation. The comparisons of seed spaces, cap events and conditioning are grounded in this distinction. [FX011, FX018, FX023, FX026, FX042–FX045]

### S06 — Cheat sheets: sampled construction framing

**Aaronson–Ben-David–Kothari, _Separations in query complexity using cheat sheets_.** Packet: `literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md`.

Read the introduction and main-result presentation. The panel uses its emphasis on total functions and certificate access to assess construction purpose, prior-route framing and contribution credit. This review does not claim a full independent audit of the paper’s construction sections. The current companion’s cubic-ceiling calculation is useful context and should survive compression. [Weighting: expert §1.1; FX034, FX047]

### S07 — Bansal–Sinha: sampled exact supplier and source credit

**Bansal–Sinha, _k-Forrelation optimally separates quantum and classical query complexity_, supplied arXiv v3.** Packet: `literature/quartic-ref-06-k-forrelation-optimally-separates-quantum/extracted.md`.

Read the introduction, explicit one-sided promise, Theorem 1.3, Corollary 1.4, total-function application and opening proof overview. This supports the attribution of the explicit Walsh Forrelation hardness ingredient and the distinction between importing that result and using an alternative formal proof route. The entire analytic proof and separate proceedings PDF were not reread. [FX017; expert §6; record §§3.16–3.18]

### S08 — Sherstov–Storozhenko–Wu: sampled independent-work comparison

**Sherstov–Storozhenko–Wu, _An optimal separation of randomized and quantum query complexity_, supplied arXiv v4.** Packet: `literature/quartic-ref-23-an-optimal-separation-of-randomized-and-qu/extracted.md`.

Read §1.8’s independent-work comparison. It separates the random-orthogonal construction from the explicit Walsh setting and identifies overlapping methods. This check supports preserving the repaired literature distinctions, not reopening them as missing or attributing one result to a different source. The remainder was not fully read.

### S09 — Aaronson et al.: sampled known upper-bound framing

**Aaronson–Ben-David–Kothari–Rao–Tal, _Degree vs. approximate degree and quantum implications of Huang’s sensitivity theorem_.** Packet: `literature/quartic-ref-03-degree-vs-approximate-degree-and-quantum-i/extracted.md`.

Read the introductory result framing, including the total-function quartic upper bound. The extraction has damaged mathematical macros; no new correction depends on precision recovered from garbled extraction. The report relies on the current record and supplied statement review for its separate implementation routes and constants, and does not claim an independent reproving of the source theorem. [FX046; record Appendix A]

### S10 — de Wolf lecture notes: sampled state and measurement distinctions

**Ronald de Wolf, _Quantum computing lecture notes_.** Packet: `literature/quartic-lit-dewolf-quantum-computing-lecture-notes/extracted.md`.

Read measurement/projector/POVM discussion, quantum-circuit construction, deferred measurement and the distinction between output probabilities and retained state. These support the semantic reason to preserve the record’s state-versus-label counterexample. They do not establish the particular missing bridge in this formalisation. [FX035, FX041]

### Sources present or cited but not independently read

All other supplied literature entries were available for navigation or citation context but were not read in full for this pass. In particular, a source named in a draft’s existing bibliography is not automatically a source this report has verified. Shaltiel’s source is discussed by the record, but no separate attribution verdict on it is asserted here.

The assignment’s three **cited-only** works remain cited-only: Yao, FOCS 1977 pp. 222–227; Nisan, SIAM Journal on Computing 20(6):999–1007 (1991); Barnum–Saks–Szegedy, CCC 2003 pp. 179–193. They were not represented as read. The SK exemplars were sampled for method transfer only; their mathematics was not assessed.

## 3. External primary-source research

Access date: **3 November 2026**. These checks clarify public tool contracts and source identity. They do not independently reproduce the supplied historical runs. Current online documentation must not silently replace the packet’s toolchain/configuration evidence.

| Key | Primary source and inspected scope | Use in the report |
| --- | --- | --- |
| W01 | [Lean reference: Validating a Lean Proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), especially statement meaning, Comparator and trust assumptions | Supports separating proof validity under definitions from whether those definitions mean the intended theorem. Used in FX048 and the audit-route interpretation. |
| W02 | [Lean Lake reference](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/), “Challenges and External Checkers” and comparator options | Confirms configured theorem comparisons, allowed axioms, external checkers and separate sandbox controls. Used only to interpret the existing companion qualification, not to allege a failed check. |
| W03 | [Lean 4.35.0 release notes](https://lean-lang.org/doc/reference/latest/releases/v4.35.0/), Comparator integration highlights | Version-context lookup: avoided treating the old standalone tool’s CLI as authoritative for the packet’s integrated `lake comparator` invocation. |
| W04 | [Official leanprover/comparator repository](https://github.com/leanprover/comparator), archive notice and README | Historical tool-context check. The current integrated-tool documentation takes precedence for general behavior; exact packet runs remain supplied evidence. |
| W05 | [OpenAI’s official preprint PDF location](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf) | Confirmed official placement and title. The mathematical body was read from the supplied packet, not claimed to have been downloaded anew or hash-matched remotely. |
| W06 | [Drucker, arXiv:1005.0644](https://arxiv.org/abs/1005.0644), abstract/metadata lookup | Source identity and global-budget framing; detailed reasoning came from the supplied primary text S05. |

## 4. How observations became findings

The most concrete corrections are supported by direct current-source comparisons: the exposition’s absence-of-review sentence against the supplied round-five review; the companion’s commit sentence against its own generated links; the record’s count-language endpoint against `actualComplies`/`actualCount`; and the nonnegative-alpha requirement at the denominator substitution. Other findings are deliberately questions or reader-design judgments, such as which route should be first or whether optional detail earns its space. The report does not promote those judgments into observed human reactions.

The comparisons preserve successful previous-round fixes: finite seeds, shared specification blindness, deliberate challenge placeholders, same-circuit quantifiers, explicit constants, joint events, fresh decoder costs, fixed-tournament versus total-order distinctions and expanded-diagnostic credit. Where a new finding touches a repaired issue, its `previous_round_relation` explains the remaining local problem.

## 5. Work not performed

No Lean compilation, Comparator invocation, receipt re-verification, example-checker execution, fresh current-record PDF render, formal binding refresh, independent human reading trial or complete new correctness proof was performed. No input manuscript, formal source or skill was modified. The integrity and validation scripts check files, locators and packaging; they are not theorem checkers.
