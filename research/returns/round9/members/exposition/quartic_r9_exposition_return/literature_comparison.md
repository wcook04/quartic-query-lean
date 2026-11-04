# Literature comparison: operations, not a style average

Access date: **4 November 2026**. Source IDs below resolve to the edition, URL, actual reading scope and limitations in evidence/source_inventory.json. “Read” means the named passages were consulted, not that the complete work was read. No outside-source quotation is reproduced here.

The comparison asks which particular explanation would help a reader perform the next operation in this exposition. It does not rank whole papers or infer teaching effectiveness from publication venue. The supplied register profile covers 42 heterogeneous documents; its median is not an acceptance threshold for a first exposition.

## 1. Establish the access model through an executable operation

### S05 — Ronald de Wolf, *Quantum Computing: Lecture Notes*

**Edition and scope:** arXiv:1907.09415v6, 27 August 2026; selected passages in Chapters 1, 2 and 7, including the query passage at extracted lines 345–356 and the search/amplification passages and exercises around 931–1082. [Versioned source](https://arxiv.org/abs/1907.09415v6).

The relevant pattern is immediate movement from an addressed input to the XOR oracle, its reversible action, and the phase-query interpretation. For this exposition, the useful repair is to show how the block label and within-block coordinate select one position of the full input, then perform the short phase-kickback calculation there. That connects the displayed matrix path to its query charge. Chapter 7's intermediate-state exercises also support asking for an operation, rather than treating recognition of notation as mastery.

The packet's full notes were not read. The extracted Grover figure was damaged; the comparison concerns its accompanying mathematical explanation, not the quality of unseen pixels.

### S06 — Harry Buhrman and Ronald de Wolf, *Complexity Measures and Decision Tree Complexity: A Survey*

**Edition and scope:** author preprint dated 10 October 2002; TCS 288(1), 21–43; selected introduction and §§3.1–3.3, printed pp.5–8. Printed p.5 was also visually checked because the extraction loses characters. [Author PDF](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf).

The survey makes the decision tree a concrete object before using its complexity: query nodes, answer branches, output leaves, and depth. Its randomized-node and distribution-over-trees descriptions make the fixed-coin argument easier to recognize. The local transfer is a one-sentence tree definition before “shallow trees,” followed by a small finite-game interpretation when minimax is first used. The exposition need not reproduce the survey's later catalogue of complexity measures.

### S18 — Andris Ambainis, *Understanding Quantum Algorithms via Query Complexity*

**Edition and scope:** arXiv:1712.06349v1, 18 December 2017; selected introduction and §2.1. [Text](https://arxiv.org/html/1712.06349v1).

The inspected passage separates randomized and quantum algorithms, specifies worst-case query caps, and presents quantum execution as alternating input-independent transformations and oracle calls. This is a useful model for the resource language in the opening: compare query budgets rather than the number of individually observed bits. The 2017 survey's historical separation bounds are not used as present-day bounds.

### S19 — Andrew M. Childs, *Lecture Notes on Quantum Algorithms*

**Edition and scope:** title-page date 17 April 2025; §1.4 “Reversible computation,” printed pp.2–3, and §§21.1–21.2, printed pp.97–98. [Author notes](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

The reversible-computation passage gives the stored-intermediate-values construction and the optional clean-output procedure in a short operational sequence. The query section also makes the ability to skip an oracle call explicit. The useful transfer is one controlled-read example for the exposition's branch padding. A retained-workspace evaluator already suffices for the verifier; this comparison does **not** justify demanding a clean oracle or an extra copying step where none is needed.

## 2. Show what the quantum transformation actually does

### S12 — Scott Aaronson, *Introduction to Quantum Information Science*

**Edition and scope:** Fall 2018 title page; selected §§17.1–17.2, printed pp.133–137, and §§22.1.2–22.1.3, pp.181–184. [Lecture notes](https://www.scottaaronson.com/qclec.pdf).

The inspected sequence explains why an oracle must be reversible, why retaining work changes interference, and how reflections generate the search motion. Those are separable learner operations. A two-label retained-workspace calculation and a two-dimensional reflection calculation would do more for this exposition than another inventory of registers. This is a comparison of explanation order, not an endorsement of every formula in the notes.

### S20–S21 — CMU course notes

**S20:** John Wright, lecture; Tom Tseng, scribe. “Lecture 4: Grover's Algorithm,” 21 September 2015. §§1–2.3 and selected reflection discussion inspected. [Lecture 4](https://www.cs.cmu.edu/~odonnell/quantum15/lecture04.pdf).

Its opening states the search output and charged resource before the transformation. The numbering change to binary labels is made explicit. That is the relevant precedent for the exposition's several coordinate conventions, not a reason to add a general quantum-computing chapter.

**S21:** Ryan O'Donnell, lecture; Linus Hamilton, scribe. “Lecture 5: Quantum Query Complexity,” 23 September 2015. §§1–3 and the opening examples of §4 inspected. [Lecture 5](https://www.cs.cmu.edu/~odonnell/quantum15/lecture05.pdf).

The recap names a unique-solution restriction and sends its removal to a defined exercise; the examples separate input, promise and output. Its workspace caution also gives an operational reason for uncomputation. The comparison uses those teaching choices. It does not import an unrestricted equivalence between a bare phase oracle and a bit oracle.

The lecturer's attempts to use CMU's 2018 Lectures 18 and 19 yielded title-only content or timeouts. They are not evidence for any recommendation.

### S07 — Lov K. Grover, original search paper

**Scope:** supplied STOC 1996/arXiv quant-ph/9605043 text, opening and §1 only; remainder not read. [Identifier](https://arxiv.org/abs/quant-ph/9605043).

The useful historical comparison is its early concrete search task and resource question. Its older informal language is not a substitute for the modern oracle definition. The exposition already distinguishes query cost from runtime; the remaining improvement is precision in the informal fourth-power gloss.

## 3. Separate the amplification law from the stopping contract

### S15 — Boyer, Brassard, Høyer and Tapp

**Edition and scope:** *Tight Bounds on Quantum Searching*, arXiv quant-ph/9605034v1, 23 May 1996; §3.1 and §4, Lemma 2, one-based PDF p.3. The 1998 journal typesetting was not read. [Version retrieved](https://arxiv.org/pdf/quant-ph/9605034).

The t=N/4 example gives a concrete single-iteration success calculation. Lemma 2 then gives the average success for a uniformly randomized iteration count. Together they separate overshoot from the unknown-success strategy. The exposition can use its existing q=1/4 example and state the finite trial schedule; it need not add a new search example. Exact cap and conditional-law requirements still come from the packet's bounded lemma, not from an unspecified appeal to this paper.

### S16 — Brassard, Høyer, Mosca and Tapp

**Edition and scope:** *Quantum Amplitude Amplification and Estimation*, arXiv quant-ph/0005055v1, 15 May 2000; §2 operator definition and Lemma 1, plus Theorem 3 and QSearch. [Version retrieved](https://arxiv.org/pdf/quant-ph/0005055).

The operator formula fixes the order of the reflections and its two-subspace action. Theorem 3's QSearch has an expected-cost guarantee and runs indefinitely at zero success. This makes the distinction essential: the exposition requires a bounded routine that returns failure on some histories. A useful local account would give the ordered two-reflection calculation and the finite schedule, then explain why every successful trial has the same label law. It should not silently substitute the untruncated algorithm.

### S04 and S02 — The preprint and the current expert companion

**Scope:** OpenAI preprint Lemma 3.1 and proof, extracted lines 305–355; companion §3, Lemma 2. These are supplied sources, read after the first-pass freezes.

These passages already supply the missing local bridge from fixed Grover iterates to randomized counts and first-success stopping. They also make the endpoint and direct-measurement branch visible. The recommendation is to bring the required interface into the lead at its use, not to invent a stronger sampler or propose additional formalization.

## 4. Introduce Forrelation and totalization by the job each component performs

### S08 — Aaronson and Ambainis, *Forrelation*

**Edition and scope:** supplied arXiv:1411.5729v1; §§3.1–3.2, printed pp.12–14; journal publication SICOMP 2018. [Version identifier](https://arxiv.org/abs/1411.5729v1).

The inspected material distinguishes the projection experiment from the interference test in Proposition 6. Their acceptance probabilities differ. The exposition deliberately uses the sufficient k-query projection decoder, so the existence of a ceil(k/2)-query alternative is not a defect. The useful comparison is explicit association of each circuit with the statistic it measures, followed by the promise used to interpret that statistic. A small circuit or an ordered matrix trace can carry that information.

### S09 — Aaronson, Ben-David and Kothari, *Separations in Query Complexity Using Cheat Sheets*

**Edition and scope:** supplied arXiv:1511.01937v2, STOC 2016; introduction and §3.1, with the start of §3.2. [Version identifier](https://arxiv.org/abs/1511.01937v2).

The construction motivation proceeds through a failure of naive totalization, the need for certification, the cost of the inner composition, and the role of the hidden certificate address. Each object answers a preceding problem. In the lead, detailed predecessor arithmetic currently interrupts the new board before its quantum mechanism is available. Relocating that comparison after the new search mechanism would permit an actual cost comparison while retaining immediate credit where the borrowed idea enters.

### S10 and S13 — Bansal and Sinha

**Supplied slides, S10:** QIP 2021 opening slides on the query model, total versus partial functions, two-Forrelation geometry and circuit were skimmed/read as extracted text. They are an orientation source, not a proof of the analytic lower bound.

**Research paper, S13:** arXiv:2008.07003v3, 17 November 2020; equation (1.3), Theorem 1.3, Corollary 1.4 and a selected §5.4 passage were checked. [Versioned PDF](https://arxiv.org/pdf/2008.07003v3).

The paper supplies the one-sided promise and a fixed-k lower bound with parameter and logarithmic factors. The lead's simpler L follows by weakening that bound for sufficiently large m. A short explanation of how logarithmic slack absorbs the fixed constants would connect the imported theorem to the exact displayed threshold. This is an elementary comparison of estimates; it is not a reconstruction of the analytic proof.

### S11 — Aaronson, Ambainis, Bogdanov, Cheung and Dinesh

**Edition and scope:** supplied *On Quantum versus Classical Query Complexity*, ECCC TR21-115 revision 2; title, abstract and introduction opening only. [Report metadata](https://eccc.weizmann.ac.il/report/2021/115/).

The supplied overview discusses a correction to an earlier classical-simulation argument. This reinforces the need to bind historical statements to editions. The packet README incorrectly substitutes an author label ending in Yeung; the actual five-author list is recorded in the source inventory. That is a packet metadata correction, not an extra lead-manuscript finding.

## 5. Preserve the budget and conditioning in a lower-bound explanation

### S17 — Andrew Drucker, *Improved Direct Product Theorems for Randomized Query Complexity*

**Edition and scope:** author PDF matching the 2012 journal version; selected §3 definitions and Lemmas 3.1–3.2, printed pp.10–12. [Author PDF](https://people.csail.mit.edu/andyd/SDPT.pdf).

The inspected proof separates conditional input distributions from an optimal continuation value, then uses their relationship. That is the right conceptual comparison for the optional proof. Its pooled-budget theorem must not be relabeled as the packet's separate-per-instance cap. The lead already explains the continuation inequality; an initial proposal alleging that explanation was absent was withdrawn. The remaining teaching opportunity is the fixed-transcript product constraint and the later event-to-predictor application.

### S03 — The packaged reasoning record as a supporting source

The precise record landings were inspected for the tasks promised by the lead: toy circuit applicability, coherent test evaluation, bounded trial schedule, logarithmic accounting, minimax, early/late discoveries and the stopped XOR simulator. These were targeted reads, not an end-to-end reading of the long record.

Several repairs therefore require moving a short existing explanation into the lead, rather than new mathematics. The current package and embedded URL revision differ; direct remote fetches were restricted. The review establishes what the local landing supplies and reports the historical link-map evidence separately.

## 6. State which result closes the exponent argument

### S14 — Aaronson, Ben-David, Kothari, Rao and Tal

**Edition and scope:** *Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem*, arXiv:2010.12629v1; introduction and Conjecture 2, printed p.20. [Paper](https://arxiv.org/pdf/2010.12629).

The inspected passages support the universal quartic bound and the historical cubic conjecture. The lead should make the division of work observable in its final assessment: its family rules out smaller uniform exponents, while the imported universal theorem makes four admissible. Choosing fixed k before sending m to infinity is part of that explanation. The full proof and Huang's original paper were not audited here.

## Teaching-source limits and proposed use

The four perspectives are anchored in these sources as *kinds of reader*, not as opinions attributed to their authors. The undergraduate is assumed to have probability, linear algebra and algorithms; the physicist has first-course circuit knowledge; the other-field mathematician can handle mathematical abstraction but lacks query-model vocabulary; the lecturer evaluates reconstructible operations and assignment obligations.

The supplied SK exposition was consulted by the lecturer only at its opening and selected changed-case questions and answers. It supports a structural comparison: a changed assumption should force a learner to identify which argument still applies. It was not used as another paper to review or as a statistical prose baseline.

Yao's original paper, Nisan, Barnum–Saks–Szegedy and the other unread research references are explicitly listed as unread in the inventory. Presence in the packet or bibliography does not count as consultation. A proposed teaching repair remains an editorial inference until tested with actual readers.
