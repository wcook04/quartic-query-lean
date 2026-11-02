# Independent source audit — addressed construction (round 3, job 04)

## Verdict

The construction and off-promise comparison argument in the assigned primary source are mathematically sound at the scope checked. No correction to OpenAI §2.2 or Lemma 2.2 is justified by this review. The useful improvements are a fully specified small example, a sharply stated arbitrary-index coherent oracle, explicit bit accounting, and accurate attribution. The false fixed-support claim belongs to earlier ledger wording; it is absent from the original paper, which expressly describes an adaptive pointer lookup.

This is an advisory independent AI reading, not human review and not a Lean execution. It assesses the ordinary construction assuming the exact two-output circuit property supplied by the preceding section. It does not prove the Forrelation lower bound, tournament algorithm, planted lower bound, or final exponent comparison.

## Primary source and exact locators

**OpenAI.** *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, dated 5 October 2026 in the supplied PDF. The authoritative local bytes are `paper/source.pdf`, SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e` (433829 bytes); `paper/extracted.md` SHA-256 `8b3f43c78cce1d1f56b343d3fec1b72a9389b66d3ba0cad7c279886ac9f48d3a` (64021 bytes). Its official public file URL is https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf .

Assessed: §1.3 p.3 (bit-query convention, fixed query cap including off-promise input); opening of §2 p.3; final circuit-interface discussion of §2.1 pp.4–5; §2.2 in full pp.5–6, including Figure 1's caption and Lemma 2.2 proof; §3.3 pp.9–10 through the comparison and verification interfaces. The following are direct uses of this source, not claimed original results:

- Column layout, `r=ceil(20 log_2 m)` and `ell=log_2 m`, true address (7), and outward-zero condition (8): p.5.
- Totality and column uniqueness: p.5, with the explanation in Figure 1 p.6.
- All local tests, exact cardinality `m+(m−1)+r(S+2)`, topological transcript induction, pointer's `ell+1` adaptive queries and at most three gate-test queries: Lemma 2.2, p.6.
- Coherent evaluation for indices supplied in superposition, including input-dependent lookup and controlled-oracle implementation: final proof paragraph of Lemma 2.2 p.6.
- One true address at which every test passes; each address of a nonwinner has a failing test: immediately following Lemma 2.2 p.6.
- Fixed-order pair comparison, retaining decoded labels, and the inequality `a_{i* j} >= 1-epsilon` regardless of the other column's promise: §3.3 p.10.

The online GitHub page was opened and confirms the file's identity; it does not expose mathematical PDF text to the search service. Both attempted raw-PDF browser forms failed (application/octet-stream unsupported; GitHub raw route disabled). The mathematical reading above uses the supplied PDF, freshly extracted by `pdftotext -layout`, and its matched supplied extraction. Do not describe this as independent byte-for-byte confirmation against a freshly downloaded public PDF. Official primary-source search confirms the preprint title/author/date and abstract.

## Cheat-sheet antecedent: exact edition and numbering trap

**Scott Aaronson, Shalev Ben-David, Robin Kothari.** *Separations in query complexity using cheat sheets*. STOC 2016, pp.863–876, DOI https://doi.org/10.1145/2897518.2897644 . The edition actually inspected is arXiv:1511.01937v2, 9 July 2019: https://arxiv.org/abs/1511.01937v2 and https://arxiv.org/pdf/1511.01937v2 .

Local `literature/quartic-ref-02-separations-in-query-complexity-using-chea/source.pdf`: SHA-256 `64380c861d0e0296a53c998a0109d62bf446529414001f8e46615991b558e4bc`, 393155 bytes. The PDF identifies v2 on its first page. The exact v2 TeX archive `source.tar.gz` has SHA-256 `8b878b7b4c67206924b8cc32e586c5ad1ec918ffcb60d665b7ea26dddaffa5ff`, 38431 bytes, containing `cheat37_arXiv_v2.tex`. The supplied `extracted.md` has SHA-256 `39745f19fdbaad3fd6542cee69cd8fdabe02771f975e676aa2e375a208873e32`, 145399 bytes.

Assessed: §6.1 pp.20–21 (Definitions 14–15, adjacent explanation); §6.2 p.22 (Lemma 17 and its proof). Sampled: Theorem 16 on p.21 and the introduction for context. Do not rely on the extraction's independently numbered theorem environments: the required PDF **Definitions 14–15 and Lemma 17** appear there as **Definitions 10–11 and Lemma 13**. This offset was verified directly against the PDF and online arXiv PDF, not merely accepted from annex notes.

The exact historical roles are:

1. Definition 14 specifies a total certifying function for a partial function. An off-promise input admits no accepting certificate, and on a promised input an accepting certificate certifies its value. The all-zero certificate is designated invalid.
2. Definition 15 addresses one of `2^c` candidate certificate cells by the `c` values of independent input instances. It explicitly produces a total Boolean function, accepting only when the constituent promises and addressed certificates are valid.
3. Lemma 17 proves the evaluate-then-check upper-bound strategy for **that cheat-sheet function**. It explains why a proposed address on a bad input is harmless when the certificate checker rejects every off-promise input.

These are antecedents and conceptual comparisons, not theorem transfers to the new multi-column function. In particular, the extra factor `m` in its classical lower bound and its outward-pointer tournament do not follow from ABK Lemma 17 or Theorem 16. This section should not state or imply that a standard cheat-sheet theorem already proves the addressed construction's separation.

Suggested concise attribution: “The use of the partial-function answers as an address follows the cheat-sheet framework of Aaronson, Ben-David and Kothari [v2, Definitions 14–15]; their Lemma 17 explains the evaluate-then-check strategy. Here each column has its own cell array, and the selected cell additionally certifies a zero in each competing column.”

## Pointer antecedent: the omitted qualifier matters

**Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha, Juris Smotrovs.** *Separations in Query Complexity Based on Pointer Functions*, arXiv:1506.04719v3, 26 October 2015. https://arxiv.org/abs/1506.04719v3 and https://arxiv.org/pdf/1506.04719v3 .

Local PDF SHA-256 `1b7803487ac696b1f8d81ee7bc26d55ed7a3c4ff4b78928faa269b71358fe66c`, 313343 bytes. Its first page identifies v3. Exact source archive SHA-256 `21e2427ccdf2794bdb9d1154bf4a81ca665589680bf478413020829dca0c2c5d`, 33228 bytes; pertinent source member `goos.tex`. Supplied extraction SHA-256 `30eacb1b152e26be43fb8f656b065c1ae6e1a25782eb0fcc13c544e246baacd2`, 82924 bytes.

Assessed: §1.2 pp.5–6, “Our technique and pointer functions”, including “Back pointers”, “Making partial functions total”, and “Use of a balanced tree”; inspected the final direct-pointer paragraph both in the PDF and `goos.tex` lines 357–358. Sampled: first page and abstract for identity; start of §2 p.7 for query-alphabet distinction. Other separation theorems were not assessed.

The precise relevant passage is p.6, final paragraph of “Use of a balanced tree”. The authors explicitly discuss replacing the balanced tree by direct pointers from the distinguished element to a zero in each other column. They immediately observe that the alphabet then becomes exponential, spoiling that construction's Boolean-function use. Omitting the qualifier while presenting the present bit bounds would blur two different access models. Here a cell's `(m−1)ell` pointer bits are actual input coordinates; the algorithm reads the selected pointer's `ell` bits and then one target bit. No cell or entire pointer vector is available for one query.

Suggested concise attribution: “Ambainis et al. already discuss direct pointers to a zero in every non-marked column [v3, §1.2 p.6], alongside the alphabet cost that makes them unsuitable for their particular encoding. In the present construction, all pointer bits are explicit Boolean coordinates and the cost of reading a selected pointer is counted.”

This is a historical comparison; it does not claim the present theorem is an instance of theirs or that direct outward pointers were introduced here. If the revised section retains detailed claims about Göös–Pitassi–Watson beyond this contextual attribution, that separate primary source must be inspected; this audit did not inspect it.

## Ordinary mathematical checks and proof simplifications

### 1. Exact transcript equivalence

Use one topological induction: for every raw input `x`, `GateConsistent(C,x,tr)` iff `tr=ev_C(x)`. This holds outside the promise because the Boolean circuit is total. Then apply the exact circuit property `d(x)=1 iff x in D` and `x in D => b(x)=P(x)` to convert transcript output checks into definedness and the correct address bit. The circuit property is genuinely needed for this bridge; it is not needed merely to restate the semantic winner predicate.

### 2. Totality, uniqueness and dichotomy

Define the semantic winning-at-address predicate without ever evaluating `P(x)` off-domain: “`x in D` and `P(x)=s_h`” for each instance. Since the input has finitely many columns/cells and every predicate is Boolean, `F=1` iff a witness exists defines a total function. A fixed-length pointer word always names a row because `m=2^ell` and the encoding is a bijection.

Column uniqueness is one contradiction: the outgoing pointer of one alleged winner certifies a zero in the other winner's all-one block. Address uniqueness is pointwise uniqueness of each defined partial-function value. Consequently there is at most one winning pair. All tests passing gives the winning predicate by transcript induction and output correctness; its contrapositive gives a failing test at every address of every nonwinner.

### 3. Depth is not support

For one pointer test, write its Boolean output as `not X[p]`. Its deterministic algorithm reads all `ell` pointer bits followed by `X[p]`. This is depth `ell+1`. Every target coordinate is essential: set the pointer to it and flip that bit. Every pointer coordinate is essential: choose two pointer words differing only there, put different values at their two different targets, and hold the other coordinates fixed. Thus all `m+ell` relevant coordinates can belong to the support. No correction to Lemma 2.2 is required.

### 4. Coherence and physical query units

State the stronger coherent interface separately from the sampler:

`|i,s,q,b,0_work> -> |i,s,q,b XOR test_q(y;i,s),0_work>`

for arbitrary test label `q` and arbitrary superpositions of retained `(i,s,q)`. A family of deterministic adaptive trees of common maximum depth `d=max(3,ell+1)` gives such an implementation by reversible computation of each next location, retained query history, copying the Boolean output, and uncomputation. Padding inactive branches and implementing controlled calls must be included in the constant factor; safest source-faithful bound is `O(d)` physical calls to the bit oracle. Uniform-index preparation is a consequence obtained by preparing `K^{-1/2} sum_q |q>` first, an input-independent operation with zero query cost. A theorem about only the uniform sampler does not by itself state arbitrary-index evaluation.

### 5. Off-promise comparison

Let `i*` be a genuine winner and fix any opponent `j`, any label produced by `j`'s decoder, and any pointer stored at that label. Every row of `X_{i*}` is one, so this pointer cannot disqualify the winner. On the event that the winner's own decoder returns its true address, its outgoing pointer reaches a zero in `X_j`; hence the winner defeats `j` without invoking a tie rule. Therefore `Pr[i* defeats j] >= Pr[decode i* = s_{i*}] >= 1-epsilon`. The rival's decoder need not be accurate, promised, independent, or semantically interpretable for this implication. The actual circuit uses retained label registers, making the probability calculation a mixture of orthogonal branches. No statement about comparisons between two nonwinners follows or is required here.

## Web verification receipt (2026-11-02)

Search-service refs below are tool references for the parent to reopen before using in final citations:

- `turn0view0`: arXiv abstract page, ABK v2; confirms authors, date, journal reference and DOI.
- `turn1view1`, reopened as `turn3view0` (lines 1456 onward) and `turn3view1` (lines 1610 onward): ABK exact v2 PDF, Definitions 14–15 and Lemma 17.
- `turn0view1`: arXiv abstract page, pointer v3; confirms authors and date.
- `turn1view2`, reopened as `turn3view2` (lines 334 onward): pointer exact v3 PDF, §1.2 p.6 direct-pointer passage and alphabet warning.
- `turn0view2` / `turn2search0`: official OpenAI GitHub PDF file page, metadata only.
- `turn2academia3`: primary-source search result for the official OpenAI preprint, confirming title, date, author and abstract.
- `turn1view0`, `turn3view3`: failed raw-PDF retrievals; not mathematical evidence.

Source text was paraphrased here; no lengthy quotations are needed. Citations in the final section should prioritize the supplied exact editions and paper page/theorem locators. Do not cite these web metadata pages alone as if they exposed OpenAI's Lemma 2.2 proof.

## Reading receipt

Fully assessed at assigned scope: baseline §1.1, §3.17, §4, §5.3; primary source §2.2 and neighboring circuit/comparison interfaces; ABK required definitions and lemma; pointer required §1 passages. Sampled: README and research README for provenance, manifests and relevant annex identity notes, source TeX specifically at the direct-pointer passage, ABK Theorem 16. Unassessed: baseline remainder, unrelated literature results, Lean corpus proof/native evidence (separately assigned), full writing guides (root author handles these), missing pasted text attachment. No native Lean run was attempted by this auditor.
