# Round-two literature cross-check

This is a bounded source check of the supplied literature against the round-two
returns. It does not independently verify their complete proofs, certify a
novelty claim, or report a new Lean or Comparator run. The source archives and
PDFs cited as local annexes are retained outside this repository and are not
included in a fresh clone. The public links below identify the works; the hashes
at the end identify the exact supplied bytes.

## Forrelation and the sharp uniform return

[Bansal and Sinha, arXiv:2008.07003v3](https://arxiv.org/abs/2008.07003v3),
Theorem 1.3 concerns the path Forrelation promise used here. In the supplied
`main.tex`, Theorem 3.2 uses Fourier levels from \(k\) through \(k(k-1)\),
Corollary 3.5 supplies the biased Fourier estimate, and §5.4 combines them.
The final comparison in that section replaces a logarithmic power
\((\ell-1)/2\) by \(\ell(1-1/k)/2\). Their ratio is
\(\log(kN)^{(\ell/k-1)/2}\), which grows for fixed \(k\) and every
\(\ell>k\); such a level occurs for \(k\ge3\). This checks a defect in the
displayed upper-bound comparison, not a counterexample to Theorem 1.3.

The exact archive has `main.tex` SHA-256
`800119f9f12877392a92e34ac380c61a50b2a297cee0a70511058580061f835b`.
The competing sums are on **lines 1180–1181**; line 1184 is the ensuing depth
threshold. The round-two [single-family source audit](../returns/round2/7_single_family_exponent/SOURCE_AUDIT.md)
has this locator; the [sharp-return audit](../returns/round2/6_sharp_uniform_forrelation/bansal_sinha_section54.md)
and the earlier second reading call the comparison line 1184. The mathematical
expression, rather than that mistaken line number, identifies the same issue.
The 14-page STOC proceedings version was supplied separately; its theorem
statement is present but it does not reproduce the full preprint's §5.4 display.

The [sharp uniform return](../returns/round2/6_sharp_uniform_forrelation/note.md)
proposes a separate single-endpoint interpolation and invokes
[Sherstov, Storozhenko and Wu, Corollary 4.14](https://arxiv.org/abs/2008.10223v4)
for its sharper Fourier estimate. Its exact result includes an unspecified
absolute constant and explicit lower bounds on block size. The return also
proposes a numerical weaker-log estimate using an elementary Fourier bound.
Those are the return's mathematical claims; this source check has not verified
the full argument or compiled either new quantitative endpoint. The previously
checked fixed-parameter development and the proposed uniform extension must
remain separate evidence records.

The supplied QIP 2021 slides describe
interpolation and derivative control at a high level (PDF pages 12–18); they
are explanatory context, not a complete proof or evidence that the proposed
single-block formula is new. [Xinyu Wu's STACS paper](https://doi.org/10.4230/LIPIcs.STACS.2022.60)
uses a stochastic approach for XORs of independent two-fold Forrelation
instances; its Lemma 2.2 is an antecedent for a restriction identity, not the
same sequential \(k\)-block promise. The supplied
[Girish–Servedio ITCS paper](https://doi.org/10.4230/LIPIcs.ITCS.2026.72),
Theorem 4, treats the extremal sign promise and proves an \(\widetilde\Omega(2^{n/4})\)
lower bound against randomized algorithms, including adaptive algorithms. It
does not replace the arbitrary-\(k\) path lower bound. The actual supplied
publisher PDF has 22 pages; it is now retained alongside the earlier arXiv
source.

[Zhang and Shao](https://arxiv.org/abs/2610.41694v1) study *cyclic* normalized
trace Forrelation. For fixed even \(k\ge4\) they state a tight
\(\Theta_k(N^{1-2/k})\) nonadaptive classical bound at constant additive error;
their separate adaptive lower bound is \(\Omega(N^{1/4})\) for \(k\ge4\) and
\(0<\epsilon<1/2\), with success probability at least \(2/3\).
These results cannot be transferred just by matching the word Forrelation:
the cyclic trace and the path amplitude are different functions. The abstract,
definitions and main statements were inspected; the collision proofs were not
re-audited.

## Direct products and the quantum upper bound

[Drucker's paper](https://arxiv.org/abs/1005.0644), §1.3 and Lemmas 3.1–3.2,
is the relevant antecedent for conditional one-instance values and their
product after an adaptive transcript. Its global-budget Theorem 1.1 is a
different statement from the separately capped version used in the return.
[Shaltiel, ECCC TR01-009](https://eccc.weizmann.ac.il/report/2001/009/),
Definition 4 and Theorem 5, is an earlier fairness antecedent stated in
XOR-advantage language. The [classical return's source map](../returns/round2/4_lean_classical_lower/sources.md)
gives the bridges; neither source citation certifies the returned Lean files.

[Beame, Kornerup and Whitmeyer, arXiv:2609.26678v2](https://arxiv.org/abs/2609.26678v2),
introduce a quantum *selective* task in which an algorithm chooses which
\(k\) out of \(m\) independent instances to answer, and state quantum strong
selective and Boolean-valued list-decoding direct-product theorems. These are
quantum results with different output and success conditions, not a replacement
for the classical distributional product argument. The introduction and
theorem statements were read; the proofs were not independently rederived.

The supplied [Høyer–Mosca–de Wolf source](https://arxiv.org/abs/quant-ph/0304052v2)
is *Quantum Search on Bounded-Error Inputs*, while
[Montanaro](https://arxiv.org/abs/0908.3066) studies quantum search with advice;
the assumptions and algorithmic interfaces differ. The [single-family return](../returns/round2/7_single_family_exponent/single_family.md)
proposes a coherent amplitude-estimation decoder to improve its quantitative
rate. The cited amplitude-estimation theorem does not by itself validate the
return's reversible composition or certify its proposed new Lean interface.

## Spectral-adversary coefficient

The supplied [Špalek–Szegedy publisher paper](https://theoryofcomputing.org/articles/v002a001/v002a001.pdf),
Theorem 3.1 and equation (3.1), prints
\(Q_\epsilon/(1-2\sqrt{\epsilon(1-\epsilon)})\ge SA\), with the usual
nonnegative spectral ratio and an ordinary bit oracle. For two-bit parity, the
four-cycle adjacency matrix has norm 2 and each coordinate mask has norm 1,
while one oracle call computes parity exactly. At \(\epsilon=1/100\), the
printed bound would require more than one query. This independently reproduces
the finite witness in the [round-two coefficient check](../returns/round2/5_lean_appendix_a/SOURCE_COEFFICIENT_CHECK.md).
The supplied [Høyer–Lee–Špalek author PDF](https://www.ucw.cz/~robert/papers/madv.pdf),
Definition 1 and Theorem 1 on printed page 3, gives the standard bound with
an additional factor \(1/2\). The exact-arithmetic witness script was rerun and
passed. This concerns the printed coefficient, not the paper's equivalences or
the quartic asymptotic conclusion; no author-confirmed erratum or newly compiled
Lean theorem is claimed. An earlier annex note also inserted an extra outer
square root in transcribing the 2006 display; that note has been corrected.

## Exact supplied-source inventory

The following SHA-256 values describe the bytes supplied for this check. The
five publisher or variant PDFs marked “supplement” are retained locally beside
the existing work-level annex, without replacing its primary substrate. The
four byte-identical sources are already present. Each local copy is subject to
its own rights review before redistribution; local retention is not permission
to publish. The Wu publisher page expressly states CC BY 4.0.

| Source | Local disposition | SHA-256 |
| --- | --- | --- |
| Høyer–Lee–Špalek, *Negative weights make adversaries stronger*, author PDF | New work-level annex | `45a0ed9c6122452c70db57da2356434ffba87389238eb11d0f3ae502842befad` |
| Girish–Servedio, ITCS 2026 PDF | Supplement to existing arXiv annex | `6ddca758ad889faed006ef129078304b710326bd1a860e6128bbad9743ef8426` |
| Bansal–Sinha, QIP 2021 slides | New presentation annex | `e430ef045d651b21134bcaf7c5d62723a6b809613ee5c702f6492138954395de` |
| Bansal–Sinha, STOC 2021 PDF | Supplement to full-version annex | `b3102c80c39e118a4d7fda9bf4b97a1b0f8e0b6a96af7eb5f1dac00ab8fc8d38` |
| Wu, STACS 2022 PDF | Supplement to arXiv annex | `c63da92c72e788efb2f7a66d1c0244f6582390e39c3da25949857dd663618050` |
| Beame–Kornerup–Whitmeyer, arXiv:2609.26678v2 source | New work-level annex | `82551889c93460a579592d65702b054b14f2677a75b0ba1f341156fe82380b44` |
| Shaltiel, TR01-009 PDF | Existing identical source | `70248ab80df12ff9fab1b2708a2fda7947bf6f22c44db5f7713e6252aaad2436` |
| Drucker, supplied 2014 PDF | Supplement to existing work | `c01932c63e62a314d18cd59b8f55066f2cb9cd426ce6dfa69aa996f1594a2459` |
| Montanaro, *Quantum search with advice* PDF | Existing identical source | `16d93e88d00b4b160e47e13081c310632fc06cd065ad0a3535234163752c86bb` |
| Høyer–Mosca–de Wolf, quant-ph/0304052v2 source | Existing identical source | `05d60dca2deb862e7d43848b4dc181422ab62dcc14b6a0e92e19db8c7a2e0907` |
| Zhang–Shao, arXiv:2610.41694v1 source | New work-level annex | `af391f6d5162d912272d84ab14e12fddaccec3a4d57cdc34c3b8ab7bf9e339fc` |
| Špalek–Szegedy, supplied publisher PDF | Supplement to existing work | `c7b946356a14102eef38037b32520b3e40f87896b8140dbcdac02a6969e20ee1` |
| Buhrman–de Wolf, decision-tree survey PDF | Existing identical source | `7002019660c498b652611acf5cdbe264ea9c4a139f8f4da6e82e12822e5d9122` |

The catalogue and bibliography checks are bounded to these sources and the
already recorded prior-art search. They do not establish that all related
work, later corrections, or possible versions have been found. No human review
or independent audit of the long paper proofs is asserted here.
