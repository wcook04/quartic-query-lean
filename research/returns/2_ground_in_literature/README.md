# Literature and attribution review: nearly quartic query separation

**Review date:** 1 November 2026.  
**Target:** OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, 5 October 2026, family 284; supplied packet identifies `openai/math 4eaee875`.  
**Purpose:** source audit, understanding and a checkable plan. This is not a draft paper, a completed independent proof verification, or a Lean certificate.

## Main assessment

The important imported claims fit the uses made of them in the supplied manuscript. I found no fatal citation mismatch or mathematical gap in the checked tournament, capped-product application, and upper-bound assembly. The most useful changes are to attribution, version control, the precision of two historical citations, and one incorrect formulation in the supplied ledger. The substantive external lower-bound input remains Bansal–Sinha; its theorem and parameter translation were checked, but its full Gaussian-interpolation proof was not independently reconstructed. [Manuscript §§2–4 and Appendix A; `citation_audit.json`, especially refs 3, 6, 11–13, 19, 22.]

The audit has **27 records: 23 `yes`, 4 `partly`**, and none `no` or `unclear`. `Yes` means the citation fits the **expressly described role**. A historical analogy need not be a theorem that implies the new result. `Partly` separates incomplete access from a literal statement mismatch; it does not mean that four steps of the proof have been shown false.

| Ref. | Why qualified | What to do |
|---|---|---|
| 16, Grover | The inspected original treats a unique marked item. | Pair it with BBHT [11] for zero, multiple and unknown numbers of solutions. |
| 20, Nisan | Original full text not recovered. | Keep historical attribution; use the precise descendant proofs in [8] and the Buhrman–de Wolf survey. Do not invent an original theorem number. |
| 25, Sun–Yao–Zhang | The stated result is SINK decision; locating the sink is not its explicit theorem. | In the tournament setting, [18] supplies a finding route via king search after reversing all edges. |
| 27, Yao | Original full text not recovered; the modern fixed-cost bounded-error version is not claimed as a verbatim 1977 statement. | Use the manuscript's finite correctness game and the clearly distinguished modern formulation. |

These reasons and the exact relevant source locations are in `citation_audit.json`. All 23 supplied reference PDFs were inspected to their relevant results. Two absent originals were recovered as primary text: BSS [7], §9.2 Theorem 4 in a public author upload, and Nisan–Szegedy [21], §3 of the original journal scan. Thus relevant passages of **25 original sources** were available; this is not a claim to have re-proved all 25 papers.

## What the mathematical claim actually says

For each **fixed** integer (k\ge2), and all sufficiently large powers of four (m), the manuscript proves bounds of the form

\[
Q(F_{k,m})\le C_k\sqrt m(\log m)^{b_k},\qquad
R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log m)^2}.
\]

The useful exponent comparison is (4-2/k), with logarithmic losses. To exclude a proposed universal exponent (\alpha<4), first choose fixed (k) with (2-1/k>\alpha/2), and then increase (m). The ratio (R/(1+Q)^\alpha) diverges because a positive power of (m) beats fixed powers of its logarithm. The known quartic upper bound supplies the opposite inequality for the infimum of universal exponents. This proves optimality of the exponent four; it does not produce a constant-factor equality (R=\Theta(Q^4)). [Manuscript Theorem 1.1, p.1; §5, p.14.]

For example, (k=3) already yields exponent (10/3) up to logarithms and suffices to rule out a universal cubic bound. At (k=2), the displayed lower and upper estimates alone do not refute the cubic conjecture. Constants and the threshold for sufficiently large (m) depend on (k); no uniform statement with (k=k(m)) was checked.

Also, (m) is a construction parameter, **not the total number of input bits**. From §2.2 the literal layout has

\[
n=m\left[m+rkm+2^r\big((m-1)\ell+rS\big)\right],
\quad r=20\log_2m,\quad \ell=\log_2m,
\]

where the equality for (r) holds because (m) is a power of four. Since (2^r=m^{20}) and (S=O_k(m\log^2m)), this gives (n=O_k(m^{22}\log^3m)) and already (n\ge m^2). This is an elementary derivation from the stated layout, not a tighter input-size theorem. The result counts bit queries and leaves computation between queries unrestricted. Its bounds should not be turned into finite numerical runtime predictions. [Manuscript §1 p.1; §2.2 p.5.]

## The source matches that matter most

### Bansal–Sinha is the exact hardness source

In supplied arXiv:2008.07003v3, equations (1.1)–(1.3), pp.2–3, use the same normalized Hadamard expression and the promise (\Phi\ge\delta) versus ( |\Phi|\le\delta/2), with (\delta=2^{-5k}). Theorem 1.3 and Corollary 1.4, p.4, give the required randomized lower bound after setting (N=m) and the advantage parameter to (1/3). The total primitive input has (km) bits. Restricting powers of two to powers of four is valid.

For fixed (k), the source lower bound divided by (m^{1-1/k}/(\log_2m)^2) grows proportionally to ( (\log m)^{1+1/k}), up to constants depending on (k). Hence the manuscript's strict (R(P)>L) holds eventually. The later hard distribution (\mu) comes from finite minimax on the promise domain. It is not simply the raw Gaussian-derived mixture used internally in the Bansal–Sinha proof. [Audit ref.6; `reading_paths.md`, §2.1 and §4.1.]

### The direct-product statement needs a per-input cap

Drucker's relevant locations are §1.3, pp.6–7, Lemmas 3.1–3.2, pp.11–12, and the fair specialization at the end of §3, p.13. His headline Theorem 1.1 has a different global-budget statement. Shaltiel is correctly credited as an earlier source of the fair-product idea; the supplied ECCC statement uses uniform inputs and parity advantage. [Audit refs 13, 22.]

The manuscript provides its own proof of the required arbitrary-distribution vector-success bound. Adaptive transcripts impose separate observed-bit constraints on independent inputs. Conditional optimum-success values yield a product supermartingale. In the application, the nonheavy-and-hit event is contained in capped-simulator success. It does not condition on being nonheavy and then incorrectly assume the original distribution survives. [Manuscript Lemma 4.1, pp.11–12; Eq.(21), p.13.]

### The quantum subroutine must preserve the distribution

BHMT [12], §2 Lemma 1 and Eq.(8), pp.5–7, supplies the invariant normalized successful state. BBHT [11], §4 Lemma 2, p.3, supplies the random-iteration calculation. The new manuscript gives the required fixed cap through its explicit mixture and fixed number of trials; expected-cost search alone would not suffice. [Manuscript Lemma 3.1, pp.7–8.]

For the tournament, the correct conditional index distribution is exactly (w_i/\sum_j w_j). Fresh reversible workspaces make the comparison success probabilities multiply, and the amplification lemma preserves the resulting conditional state. General comparisons between false candidates may have probabilities arbitrarily close to one half. A fixed-tournament algorithm or a noisy-input search theorem with a uniform bias hypothesis is therefore not a direct substitute. [Manuscript Proposition 3.2, pp.8–9; audit refs 5, 9, 14, 18; Høyer–Mosca–de Wolf supplement.]

## Attribution to retain and to refine

The older pointer papers already have an all-one column whose pointers lead to zeros in rival columns: GPW [15], §2.1 pp.4–5, and the pointer-tree construction [4], §3 pp.10–11. Outward zero witnesses by themselves should not be described as first introduced here.

The distinctive combination in the inspected literature is: direct per-rival witnesses inside separately hard-addressed cells; a comparison that protects the true winner even when the opponent's address instances are off promise; a tournament using the actual comparison probabilities; and the separate-array planted-input lower bound. This is an attribution assessment based on the sources inspected, not an exhaustive priority certification. An earlier theorem with the same assumptions and mechanism would change it. [Manuscript §§1.2, 2.2, 3.2–3.3, 4.2; `attribution_map.json`.]

Two historical additions deserve explicit inclusion. Ben-David's 2015 *A Super-Grover Separation* predates the general cheat-sheet paper. The quartic upper bound and cubic conjecture already appear in the four-author 2020 Aaronson–Ben-David–Kothari–Tal preprint: Theorem 1 p.2 and Conjecture 4 p.9. The cited five-author paper expands that work and uses different numbering. [Download records for arXiv:1506.08106 and arXiv:2004.13231; audit refs 2, 3.]

The upper-bound proof should retain the exact chain

\[
R\le D\le\operatorname{bs}\,\deg
\le O(Q^2)\lambda^2\le O(Q^4).
\]

The inequality (D\le\operatorname{bs}\deg) is in the **proof** of Midrijanis Theorem 4, pp.3–4. The necessary Huang consequence is the stronger spectral statement (\deg\le\lambda^2), used explicitly by ABKRT. Just quoting (\deg\le s^2) does not give this displayed chain. [Audit refs 3, 17, 19; manuscript Appendix A.]

The documented 2021 correction to Aaronson–Ambainis concerns an older classical simulation proof. Include Bravyi–Gosset–Grier–Schaeffer and the revised correction note if explaining that surrounding optimality claim. It does not invalidate the Bansal–Sinha lower bound used here. Tal's earlier ECCC bug was corrected before the supplied arXiv version; preserve that chronology. [Audit refs 1, 6, 26; `historical_corrections.json`.]

## Ledger changes and verification plan

The concrete correction is `lem-2.2.i`: replace “depends on at most (\ell+1) bits” with “has an adaptive decision tree of depth at most (\ell+1)” for a pointer test. At (m=4), a two-bit pointer selecting one of four target bits yields a function of six relevant variables, yet takes only three queries. The manuscript states the correct query bound. The ledger's unconditional “Audit: correct” note should not survive unchanged. [Manuscript Lemma 2.2 p.6; `ledger_recommendations.json`, LR1.]

Also separate generic minimax existence, its Forrelation instantiation, and the direct-product consequence. The existing conditional assertion is not false, but an instantiated dependency graph must record how (L<R(P)) is supplied. LR2 gives both a split and a conservative combined-row option. LR3–LR5 retain the fixed-(k) quantifiers, amplification contract, and joint-event argument.

For subsequent checking, isolate a generic partial-function theorem with an explicit hard distribution, prove the classical coupling and capped product lemma, and instantiate the hardness only at the end. On the quantum side, prove the full amplification contract before the tournament. Keep the established Appendix A upper bound as an independent branch. Any future formal result must identify the oracle, totality, worst-case query cap, error convention, quantifiers, and exact theorem corresponding to the manuscript. No repository files were changed in this advisory round. [Detailed route and checkable intermediate outputs: `reading_paths.md`.]

## Public discussion and remaining limits

There are existing family-specific explanations, including Latent Seminar and a six-lesson AI-authored course. The earlier suggestion that nobody had explained the result needs updating. Neither inspected resource establishes a completed independent check. `new_commentary.json` contains 20 new or revised records; `commentary_recheck.json` accounts for all 16 input entries and removes unsupported inferences. One newly inspected digest confuses (m) with input length. [See each record's URL and scope note.]

No completed independent verification or specific published fatal error was found in the inspected public material. This is a scoped research result, not proof of absence. Important outstanding items are the original Nisan 1991 and Yao 1977 texts; the reported v3 of Ambainis–Iraids–Kokainis; the inaccessible complexitylib PR and MathVision repository; and a current pinned code/build/statement audit. The de Wolf lecture-note URL served conflicting cached version metadata, so its edition must be pinned before reusing pagination. Talks were identified, not watched or transcribed. [Full boundaries: `review_receipt.json` and per-source `read_status`.]

## Contents and conventions

| File | Use |
|---|---|
| `citation_audit.json` | All 27 citations, exact claims/locators, fit decisions and limitations. |
| `downloads.json` | 52 ranked recommendations, including the original bibliography and supplementary sources. Direct PDFs are preferred where available; this is a download plan, not a bundle of third-party PDFs. |
| `reading_paths.md` | Per-section reading order, exact pages and questions to settle. |
| `attribution_map.json` | 30 idea/provenance records, separating established ingredients from the manuscript's combination. |
| `new_commentary.json` | 20 revised/new public-discussion records in the input schema. |
| `commentary_recheck.json` | Disposition of every input commentary entry. |
| `source_versions.json` | Bibliographic year versus inspected edition, with supplied source hashes. |
| `statement_sources.json` | Navigation for all 118 input ledger IDs; this is not a proof-status ledger. |
| `ledger_recommendations.json` | Five concrete corrections or contract-retention recommendations. |
| `historical_corrections.json` | Earlier correction history, kept distinct from commentary on the 2026 preprint. |
| `review_receipt.json` | Input checksums, search coverage, unread material and validation scope. |
| `deliverable_manifest.json` | Sizes and checksums for the delivered files. |

Bracketed reference numbers are the manuscript's bibliography numbers, resolved in the audit. Relative paths beginning `paper/`, `literature/` or `corpus/` refer to the **original supplied packet**, not files silently duplicated in this return. All page numbers refer to the expressly named inspected edition; where printed and PDF pages differ, both are given. The return does not grant redistribution rights for linked papers. Public readability and an explicit reuse licence are recorded separately.
