# Round-four papers: editorial review

Reviewer: scientific editor (AI), 3 November 2026. Read-only review; no manuscript text was changed.

Papers reviewed:

- **Short expert paper (S)**: `research/returns/round4/members/02_short_expert/paper.md` and `paper.pdf` (16 pp., US Letter), with `references.bib`, `review_notes.md`, `LEAN_GAPS.md`.
- **Examples-first exposition (E)**: `research/returns/round4/members/03_examples_first/quartic_r4_03_examples_first/exposition.md` and `exposition.pdf` (14 pp., A4), with `checks/`.

Sources checked against: the preprint (`02_short_expert/source_packet/paper/extracted.md`, 19 pp.), the long record `docs/reasoning_record.md`, the cheat-sheet paper extraction (`source_packet/literature/quartic-ref-02-*/extracted.md`), the Comparator bundle `lean/QuarticCorpus/Unconditional/{Challenge.lean,Solution.lean,comparator.json}`, `lean/QuarticQuery/Paper/ConstructionFamily.lean`, the adversarial audit (`08_.../AUDIT.md`, `mathematical_addenda.md`, `repairs/companion_refresh_note.md`, `source_audit/evidence/historical_companion_audit.md`), the review notes of returns 04, 05 and 06.

Locators: `S md:L` is a line in `paper.md`; `S p.N` is a PDF page. Likewise `E md:L`, `E p.N`.

## Summary judgement

**Mathematics.** I found no mathematical error in either paper. I rechecked the hand-checkable claims: the 8-bit census (8, 96, 48, 96, 8; 104/48/104), the board pointers, the bit and test counts (5936, 371, 142607), the integer promise tests, the Grover average and 9/40 trial bound, the drift identity (10), the zero-search induction, the simulator's joint event, the AND example, the smoothing identities (Ψγ)′ = −φγ and φ′ = 3/q⁵, the acceptance-sandwich inequality (25), the error total 583/192000 at m = 4, and the growing-k arithmetic in S §6.1. All of them check. The audit (08) reached the same verdict on the underlying argument.

**What fails is reader placement and the formal-evidence layer.** Neither paper is yet fit to send:

1. S does not say where the result sits in the line of R-versus-Q separations: 2.5 (cheat sheets), then 8/3 (Tal), then 3 − o(1) (Bansal–Sinha, independently Sherstov–Storozhenko–Wu), now 4 − o(1). It does not credit pointer functions, and it mentions Aaronson–Ambainis without a reference entry. E credits the "addressed construction" to OpenAI alone and never mentions cheat sheets. The authors of the cheat-sheet, Forrelation and cubic-conjecture papers are among the paper's natural readers, and they will notice all of this on page 1.
2. Neither paper gives the one-line reason the exponent is four: R ≈ m·L with L ≈ m^{1−1/k}, against Q ≈ √m. Neither says what stopped the cheat-sheet method at the cube, or what the outward pointers and the tournament change. This is the route to the result that an expert reader needs before the details.
3. S does not give an expert reader a fast way to check whether the statement was correctly encoded. It names implementation theorems rather than the four configured Comparator targets in `Challenge.lean`. Its §7 is two pages of house evidence accounting. Some of its formal-status sentences are already stale or overclaimed relative to returns 04 and 06.
4. Both documents carry provenance debris, dead relative links and house vocabulary that mean nothing to an outside reader.

## 1. Findings ranked by importance

Severity scale: **critical** (must fix before sending), **high**, **medium**, **low**. IDs match `round4_papers.json`.

### P01 (critical, both): literature placement and attribution are not what this reader expects

- **S.** The paper never states the previous best exponent or the history of total-function R-vs-Q separations. The preprint (§1.1, `extracted.md` lines ~50–60) gives the record:
  - power 5/2 from Aaronson–Ben-David–Kothari cheat sheets [2];
  - 8/3 − o(1) from Tal [26];
  - 3 − o(1) from Bansal–Sinha [6] and, independently, Sherstov–Storozhenko–Wu [23].

  S cites none of Tal, SSW, Göös–Pitassi–Watson or Ambainis et al. (pointer functions). All are in S's own `references.bib` (`Tal2019v1`, `SherstovStorozhenkoWu2023`, `GPW2018`, `ABBLSS2015`) but are not cited in the text, so they are absent from the rendered list (S p.16).
- **Aaronson–Ambainis.** S md:84 / p.3 says "following Aaronson and Ambainis" with no reference. AA is not in the rendered reference list, although `AA18` is in the .bib. For the author of Forrelation, k-fold Forrelation should be introduced as AA's problem. The cheat-sheet paper records that AA conjectured it achieves the optimal partial separation (ABK extraction line 23). Bansal–Sinha and SSW then proved the optimal separation.
- **Cheat sheets.** The cheat-sheet paper *is* cited in S (md:56, p.2; refs p.16), so the premise that S's bibliography omits it is wrong for this edition. The credit is one sentence, though. Readers who know the cheat-sheet construction will want the inheritance stated exactly:
  - from ABK: the address formed by the answers to O(log) independent partial-function instances, the certificate stored at that address and the evaluate-then-verify strategy. ABK use 10 log n copies (ABK extraction line 1431); here r = 20 log₂ m.
  - new here: a separate array per column, outward pointers and the tournament.

  ABK itself observes that the framework gives a cubic separation "in a completely black-box manner" if an optimal partial separation exists (ABK extraction line 23). That sentence frames the whole result: the cheat-sheet route stalls at 3, ABKRT conjectured 3 was the truth, and this construction shows it is not.
- **Pointer functions.** The winner condition (a unique all-one column whose certificate points to a zero in every other column) descends visibly from Göös–Pitassi–Watson pointer functions, developed by Ambainis et al. The long record credits this (`docs/reasoning_record.md` line 2148). S does not.
- **Comparison-based search.** The preprint calls Ben-David–Kothari 2026 [9] and Ambainis–Iraids–Kokainis 2026 [5] "particularly relevant" to the comparison viewpoint. It also cites quantum minimum finding [14] and king finding [18]. S omits all of these. Ben-David and Kothari, authors of the cheat-sheet paper, wrote [9]. `BDK2026`, `DH1999` and `MPS2023` are in S's .bib; Ambainis–Iraids–Kokainis is not.
- **Høyer–Mosca–de Wolf (search with bounded-error inputs).** This is the obvious alternative an expert will ask about. The record and return 04 explain why it does not apply: loser–loser comparisons need not be reliable. S does not say so.
- **E.** md:348 / p.13 says "The separation theorem and addressed construction are OpenAI's". This misattributes the addressing idea, which is ABK's. E's references (p.13–14) contain no ABK, GPW, ABBLSS, Tal or SSW. That is acceptable for students only if the attribution sentence is corrected and a three-line history is added.
- **ABKRT** is credited correctly in both papers: Theorem 2 for D = O(Q⁴) and Conjecture 2 for the cubic bound. Add Huang [17] as the ingredient.

### P02 (critical, both): the central idea is never put in one line

A reader's first need is the central idea, stated where it can be seen. S's §1 (md:49–53, p.2) explains the asymmetry of the pointers but never gives the arithmetic of the separation:

- quantum: about √m polylog, from a search over m columns in which each column costs polylog queries;
- classical: about m·L, because one must find the planted column and then find either its hidden zero or its address, and the address costs L ≈ m^{1−1/k};
- hence R ≈ m^{2−1/k} = (√m)^{4−2/k}.

Nor does S say why cheat sheets plus an optimal partial separation stop at 3, or what replacing the cheat-sheet outer function by a pointer-certified search buys. Concretely, a quantum search over columns must tolerate off-promise rivals, which is why the tournament is needed. The record has the R ≈ mL sentence (record §1.1, line ~95). E puts the theorem itself only in §9 (p.12). **Fix:** a half-page "idea" paragraph in S §1 and a one-page overview at the start of E, each with a figure of a column (string X_i, r address instances, the cell array, outward pointers). Any statement about why earlier methods stalled must be verified against ABK §3.1 and the preprint §1.1. Do not paraphrase from memory.

### P03 (critical, S): an expert reader cannot quickly check whether the statement was correctly encoded

The residual question a reader has about any Lean development is whether the statement was correctly encoded. S never points at `lean/QuarticCorpus/Unconditional/Challenge.lean` (343 lines, imports Mathlib only). That file is the complete statement a reader must audit:

- inputs and partial functions, lines 13–29;
- the classical model and R, lines 31–77;
- the adaptive quantum model, the oracle and Q, lines 79–140;
- Forrelation and P, lines 142–182;
- circuits and transcripts, lines 184–222;
- the addressed function `Fkm`, lines 223–283;
- `Lvalue`, `Gvalue`, `BansalSinhaLower`, `UniversalPower`, `alphaTot`, lines ~290–326;
- the four checked theorems at the end.

S's §7 (md:597–647, pp.14–15) is written in house evidence vocabulary ("exact-name comparison membership", "root build", "headline dependency traversals", "retained receipts"). It also names the implementation theorems `alphaTot_eq_four_unconditional` and `theorem_1_1_unconditional`, whereas the names Comparator actually compares are in `comparator.json`: `QuarticQuery.Checked.alpha_tot_eq_four`, `Checked.theorem_one_one`, `Checked.cubic_bound_fails` and `Checked.forrelation_lower_bound`. **Fix:** replace §7 with the one-page appendix specified in §4 below.

### P04 (high, S): formal-evidence claims overreach or mismatch the compared statement

- **Comparison wording.** S md:624 / p.15 says the two implementation names "have current comparison evidence". Return 06 showed that the receipt producer credited names merely mentioned in `Solution.lean`, including names inside comments. Eight of the twelve rows with comparison credit, `thm-1.1` among them, relied only on such inferred aliases. The repository has since restricted receipts to configured targets (commit `235e2c8`). Accurate wording: "Comparator compares the configured theorems `Checked.alpha_tot_eq_four`, `Checked.theorem_one_one`, `Checked.cubic_bound_fails` and `Checked.forrelation_lower_bound`; their solutions are one-line applications of the implementation theorems."
- **Theorem 1 display versus what was compared.** S Theorem 1 (md:34–41, p.1) displays exponent 6 and constant 1/400. Those come from `QuarticQuery.Paper.construction_family_named` (`lean/QuarticQuery/Paper/ConstructionFamily.lean:30–40`), which has build evidence but no Comparator check; S §7.2 admits this. The compared `Checked.theorem_one_one` (Challenge.lean, final block) is weaker: it gives an existential exponent b and the floor form ⌊mL/100⌋ < R. Theorem 1 should say which part each kind of evidence covers.
- **Dangling and stale references.** The [Lean] reference (md:668, p.16) cites revision `c7e0c916…` and a `SOURCE_AUDIT.md` that is not in the bundle. The audit identifies `c7e0c916` as part of an older commit narrative. Cite the exact commit at which the final, sandboxed Comparator run is recorded.

### P05 (high, both): stale or conditional formal-status sentences after returns 04, 05 and 06

These claims are being rebuilt independently and are unverified. Each sentence below must therefore be written conditionally, or held until the rebuild receipt exists.

- **Retained-state amplification.**
  - S md:278, md:608 and md:626 (pp.6, 14, 15) say "A stronger retained-original-quantum-state bridge is not supplied".
  - E md:178 / p.7 says the interfaces "do not assert the missing designated-subsystem factorization".
  - Return 04 (`04_quantum_completion/quantum_return/review_notes.md`) claims that `Upper.uniformOpaqueAmplifier` and `finalB_physical_on_embedding` now prove, in Lean, the retained original subsystem with exact success mass.
  - Until the rebuild passes, write: "An ordinary proof that amplification returns the full normalised good state is given in [record §5.5 / ref]; a Lean proof has been submitted and is being independently rebuilt. The query bound uses only the measured label law, which is proved." After a passing rebuild, drop the conditional and cite the declarations.
- **External randomness.**
  - S md:626 says the finite product development "does not itself establish a general pushforward theorem for arbitrary independent external probability spaces".
  - Return 05 supplies a complete ordinary proof for arbitrary measurable action-at-history seeds. Its Lean candidates were not compiled in its own environment.
  - Write: "ordinary proof given; formal version pending".
- **List-output tournament.**
  - S md:278 and md:608 imply that the list-output tournament exists only inside the verifier recursion.
  - The audit's refresh note (`repairs/companion_refresh_note.md`) records that `Paper.quantumTournament` and `Paper.equation_15` exist with root-build evidence, outside the headline reach and with no Comparator check.
  - E md:243 already says this; S should match.
- Use the audit's replacement paragraphs in `repairs/companion_refresh_note.md` as the starting text, updated for 04 and 06.

### P06 (high, S): pages are spent in the wrong places for this reader

Approximate allocation in the rendered S:

| Section | Pages | The expert reader needs |
|---|---|---|
| §1 Result | 1.6 | Yes, plus history and the idea (P01, P02) |
| §2 Construction | 1.7 | Yes; add a figure |
| §3 Quantum | 2.7 | Statement-level amplification (he co-knows BHMT/BBHT); full care for off-promise comparison, drift, exact law w_i/W, coupling with history-dependent failure |
| §4 Classical | 3.0 | Yes, the most delicate part; keep |
| §5 Forrelation lower bound | 2.7 | Mostly no; BS/SSW are known to him. One page: statement, what Lean proves (fixed k, weaker log), that it is in the compared bundle, no human review |
| §6 Exponent | 1.3 | Keep the quantifier paragraph; reduce §6.1 to a remark (P12) |
| §7 Formal layer | 2.0 | Replace with the 1-page appendix (P03) |
| References | 1.0 | Expand (P01) |

He will find the following obvious: the oracle and the definitions of R and Q, Forrelation and its Φ² projection algorithm, the Grover rotation (S eqs. (8)–(9) proved in full on p.5), minimax (S md:342), Markov, R ≤ D, and D = O(Q⁴). He will want the delicate points proved carefully, in one place (P08). There are no figures and no tables; every page has the same grey density.

### P07 (high, S; medium, E): provenance debris and broken navigation in the rendered PDFs

- **S.**
  - An "Authorship and provenance" paragraph sits above the title (p.1), and there is no author line.
  - The subtitle reads "reconstructed download edition".
  - The closing "Reading and evidence scope" paragraph (md:687, p.16) discusses "the prior assistant's temporary scratch-path ZIP".
  - Seven "Full proof and source-bound context" links (md:63, 166, 301, 424, 555, 599, p.2–14) point to `source_packet/repository/docs/reasoning_record.md#…`, which is dead in a standalone PDF.
  - The Mathlib/CSLib hash line overruns the right margin (p.15).
  - The reference list cites a missing `SOURCE_AUDIT.md` (p.16).
- **E.**
  - The author line is "An AI-authored mathematical companion to OpenAI's construction", with no responsible human.
  - Red links point to `sources/repository/…` relative paths (pp.2–13).
  - Bibliography entries carry SHA-256 values, "no downloaded byte identity is asserted" and "the pinned primary URL was unavailable to this session" (p.13).
- **Both.** Replace the record links with a public URL plus section number (for example "long record, §6.5"), or remove them.

### P08 (medium, S): the delicate points are present but not signposted, and two are imprecise

S treats the off-promise comparison (md:182–193), complementarity through a single unordered-pair circuit (md:182), the joint event (md:383–404) and the quantifier order (md:570) well. Gaps:

- **Erased-zero identity.** The identity Pr[erased zero hit] = E[Z]/m, which holds only because I is independent of the whole dummy run, is never stated. S md:364 goes straight to an averaged tree bound. E md:276 / p.10 has the decisive counterexample (choosing among discovered columns keeps I's marginal uniform but gives 175/256 instead of 1/4); the audit has a three-column version (19/27). S should state the identity and give one counterexample line.
- **Joint independence.** S md:306 / p.7 says "independent side information and random coins are allowed". The condition needed is that coins and side information are jointly independent of the whole tuple. Pairwise or marginal independence fails: audit §4.1 has the S = X ⊕ R example. E md:280 gets this right.
- **Recommendation:** a short table early in S, "Where a natural shortcut fails", with one row per delicate point and its counterexample:
  - Φ = −1 accepted by the projection test but off-promise (E's a⁻);
  - an off-promise rival;
  - a dominant candidate that is not a winner (E md:188);
  - an expected rather than branchwise cap (audit's 5/8 parity example);
  - conditioning on cheapness (AND);
  - a dependent planted index;
  - growing k inside a fixed-k threshold (E md:344).

  This shows a working model of what the reader already knows, and it is cheap because every counterexample already exists in the returns.

### P09 (medium, E): examples are well chosen but the frame is missing

**What works.**

- The 8-bit census (E §1) is concise and checks signs, the one-sided promise and the a⁻ trap. I verified the counts.
- The reduced board (E §2) with its "changed board" (domain bit the only failing test) and the "dominance is not winning" variant (E md:188) are the best teaching items in either paper.
- The AND example and the uniform-marginal counterexample are both well placed.

**What is missing.**

- A statement of the theorem and a road map before §1. The theorem first appears in §9, p.12.
- Any figure. The board is described in prose only, though it is the obvious figure: four columns, the strings, the pointers, the winning cell.
- Any history.

**What is overlong for strong students.**

- The canonical-lift paragraph (E md:65: 3563 gates, 142607 tests, Lean coordinate renaming).
- The residue-width circuit details (md:102).
- Inline Lean names throughout.
- The full minimax and Chernoff proofs (fine as boxed asides).
- §5, which comes too early (the retained-state issue matters only after the tournament) and is stale (P05).

**Example to add.** The one-instance AND example shows conditioning beating β. Return 05's two-instance version uses AND on the full uniform domain with β = 3/4: joint probability 5/16 and conditional success 5/8, against β² = 9/16. It shows the product bound itself failing, which is the actual danger. Verify it against 05's checks before use.

### P10 (medium, S): the stated log exponent 6 is not derived

S Theorem 1 states (log₂ m)⁶ (md:38), but §3.4 concludes only √m (log m)^{O_k(1)} (md:296). E md:237–241 jumps similarly. Either give the count (tournament O(c√m T² log T) with c = O_k(r log(r/ε)), plus T verifications of cost O(√K log(1/ε) log m)), or say that 6 is what the formal budget `Upper.budgetConst` accounting gives. An expert reader will look for this.

### P11 (medium, S): notation collisions

- M is both m(√m)^{k−1} (md:108) and ⌈10/√γ⌉ (md:221).
- T is the number of stages (md:175) and a decision tree (md:409).
- t is the exponent in m = 4^t, the pivot count (md:237) and a query time (md:381).
- G is the classical budget and a test function in (21) (md:450).
- N is the Forrelation numerator, km (md:498) and, implicitly, the trial count.
- s is an address and the interpolation parameter s ∈ [0,1] (md:463).
- q is a budget (md:312) and the function q(x) (md:443).
- γ is the amplification threshold and the Gaussian density (md:450).
- E uses s for the winning column (md:186) and q for both repetitions and query time.

Equation numbers in S are the paper's own (1)–(26), while the text also cites the preprint's numbers; add the preprint number in brackets at each display that matches one, for example (16) [preprint (19)]. Expert readers will read the two side by side.

### P12 (medium, S): the growing-k section should be replaced or demoted

S §6.1 (md:578–595, pp.13–14) is arithmetically correct given its inputs, which I checked. It rests on two things: the threshold t ≥ 13669k² holding uniformly in k for the 1/400 bound, and a constant lemma `Upper.budgetConst_le_exponential` that has build evidence only. The audit's addendum A (`mathematical_addenda.md` §A) gives a fully explicit schedule from verified ingredients:

- t ≥ 80, k = ⌊√(t/20)⌋;
- R(F_t) ≥ Q(F_t)^{4−ε(s)} with ε(s) = 8√10/√s + (56 log₂ s + 508)/s and s = log₂ m;
- log R / log Q → 4.

That is interesting to an expert reader as a remark: a single explicit sequence with deficit O(1/√log m). Replace §6.1 with a half-page remark built on addendum A. Label it as an ordinary deduction checked by AI, not a Lean theorem, and keep the warning that it is not R = Ω(Q⁴).

### P13 (medium, S): the abstract is unreadable and leads with minor formal improvements

The abstract (md:8, p.1) uses "column", "all-one string", "address instances" and "incoming zero witness" before defining any of them. It advertises the 2G/m² versus 4G/m² constant and the "induction on sub-distributions", which do not matter to this reader; the record and audit already have 2G/(m(m+1)) as an ordinary refinement. It also does not say that the Lean Forrelation proof is AI-produced and has had no human review (README: "No person has reviewed it yet"). **Fix:** five plain sentences:

1. the result and that it refutes ABKRT Conjecture 2;
2. the previous best exponent, 3 − o(1);
3. the idea in one sentence;
4. what this companion adds: a reader's path, a Lean formalisation checked by Comparator against a 343-line Mathlib-only statement file, and an alternative fixed-k Forrelation lower bound;
5. the evidence status: AI-produced, no human review.

### P14 (medium, S and E): treatment of the Bansal–Sinha v3 display

E md:123 mentions a "version-specific logarithmic mismatch in a displayed proof step of Bansal–Sinha v3"; S is silent. The record (§3.16) and audit (§5.2) describe a specific display on printed p.38 of v3 and are careful to say it does not refute the theorem. For a reader who knows both authors' work, either:

- omit it, since the separation needs only the stated Corollary 1.4 and the Lean route is independent; or
- give one neutral footnote with the exact locator and the sentence "this concerns one displayed comparison, not the theorem".

It must never appear as a headline. Consider telling the authors privately before any public statement.

### P15 (medium, S): §7.1 and §7.2 mix ordinary mathematics with execution history

S md:604–628 lists what Lean "makes explicit". That content belongs in the appendix (P03) as two short lists: what the formal models fix, and what remains a review obligation (the model choices, the bit/phase bridge, the asymptotic translation). S md:618 already says this well and should be kept almost verbatim.

### P16 (low, both): house jargon in reader-facing text

Terms to remove or define:

- **S.** "integrated record", including in the Theorem 1 title (md:34); "reviewed record"; "source-bound" (7 times); "packet" (12); "retained receipts"; "supplied" (about 15); "headline" (5); "wrapper" (3); "frozen".
- **E.** "proof destination" (3 times); "supplier", including a section title (§3, md:69); "correspondence artifact"; "maintained explicit bound"; "formal conjunction exports".

Neither paper contains the record's F-codes (F43, F60) or the phrase "record anchor". Keep it that way.

### P17 (low, E): attribution and author line for student readers

E should carry the same attribution S has: Will Cook directed; AI agents produced the formalisation and text; the theorem and construction are OpenAI's; no human review. Cite AA by its published venue (SICOMP 2018), not only arXiv v1.

### P18 (low, S): reproduction commands

S md:636–644 is correct about `scripts/Reach.lean` and the sandbox flag; `tools/run_comparator.py` appends `--inadvisably-no-sandbox`. In the appendix, state plainly that the recorded local runs were unsandboxed rehearsals. After the rebuild, give the commit, toolchain `v4.36.0-rc2` and pins, and the exact command whose output is quoted.

## 2. Reader model and length recommendations

### Expert readers (S)

**Will find obvious and skim:** the query model and the oracle; Forrelation, its Φ² projection algorithm and the reason a negative Φ matters once stated; amplitude amplification and the random-iteration trick; minimax; Markov and union bounds; D = O(Q⁴) and Huang; cheat sheets as a framework; Drucker/Shaltiel-type direct products.

**Will want proved carefully** (this is where S should spend its pages):

1. **The construction.** Why the domain bit is needed for a one-sided promise; why the all-one winner defeats every rival at any address; why transcripts are checked against real input bits.
2. **The tournament.** Complementarity from one unordered-pair circuit; the drift identity with no transitivity and no gap from 1/2; why nonwinner cycles are harmless.
3. **Exact sampling.** Fresh workspaces give product weights; amplification keeps the conditional law; coupling with history-dependent failure probabilities.
4. **Verification.** Why it is still needed, by the dominance-without-winning example.
5. **The planted pair.** The first-difference argument; the identity Pr = E[Z]/m and why I must be independent.
6. **The capped direct product.** Separate caps, joint independence of side information, and the joint rather than conditional event, with the AND trap.
7. **Quantifier order.** Fixed k, the same circuit for both bounds, and why letting k grow is a separate statement.
8. **Encoding.** Whether the Lean statement of R, Q and α_tot is the one he means.

**Recommended length for S:** a 10–11 page main text, a 1-page Lean appendix and 1–1.5 pages of references, about 13 pages in all, down from 16. The preprint is 19 pages; a companion longer than about two-thirds of it is not a pre-digest. An expert reader will give it one sitting.

| Part | Pages |
|---|---|
| Abstract; result; history table; the idea with figure | 1.5 |
| Construction, with figure and the four-column example | 1.5 |
| "Where a shortcut fails" table | 0.5 |
| Quantum (comparison, drift, sampling, verification; amplification as a stated lemma with a 4-line proof sketch) | 2.0 |
| Classical (planting, erased zero, simulator, direct product) | 2.5 |
| Forrelation lower bound (statement, route, status) | 1.0 |
| Exponent and quantifiers; growing-k remark | 1.0 |
| Appendix: checking the Lean statement | 1.0 |
| References | 1.0–1.5 |

Send it with a half-page cover note. Point to E for students and to the long record for full proofs, by section number and public URL.

### Strong students (E)

They will know Grover, basic probability and decision trees. They may not know Forrelation, query lower-bound technique, minimax or direct products. They need the frame first, then the examples, then proofs they can skip.

**Recommended length for E:** 12–15 pages A4, about the same as now. Spend it differently:

- add a 1-page overview (theorem, the R ≈ mL vs Q ≈ √m arithmetic, the history in three lines);
- add 3–4 figures: the column and cell layout, the reduced board, a tournament with a cycle among losers, and the planted pair;
- cut about 1 page of provenance, Lean names and circuit-lift detail;
- move the minimax, Chernoff and direct-product proofs into skippable boxes;
- defer the state-versus-label section to after the tournament, and update it (P05).

The pitch should be "explain without going fully technical": at present E is fully technical in places and non-technical nowhere.

## 3. Assessment of each requested question

1. **Correctness and fidelity:** no mathematical errors found. The overclaims and mismatches are P04 (comparison names; displayed versus compared Theorem 1), P05 (stale formal status), P10 (exponent 6 undeclared), P08 (joint independence imprecise) and P01 (E's misattribution).
2. **Literature placement:** P01. The previous best exponent, verified from preprint §1.1, is 3 − o(1) (Bansal–Sinha; independently Sherstov–Storozhenko–Wu), after 8/3 − o(1) (Tal) and 5/2 (ABK cheat sheets). The cheat-sheet paper is cited in S but under-explained, and missing from E. Pointer functions are missing from both. AA is missing as a reference in S. ABKRT is credited correctly.
3. **Reader model and length:** §2 above.
4. **Lean and Comparator layer:** P03, P04 and §4 below.
5. **Exposition:** P09 and P17.
6. **Presentation:** P07, P11, P16 and P13.

## 4. Specification of the one-page Lean appendix (for S)

Title: "Checking the statement". It should contain exactly the following.

1. **One sentence of purpose.** A proof checker certifies that a proof matches its stated type. This page lists the statement a reader must check, so the remaining question (does the formal statement say what the theorem says?) can be answered in about 15 minutes.
2. **The file.** `lean/QuarticCorpus/Unconditional/Challenge.lean`, 343 lines, importing only Mathlib, with a line-range map:

   | Lines | Contents |
   |---|---|
   | 13–29 | Inputs, partial functions and `totalise` |
   | 31–77 | Decision trees, with depth charging repeated queries; finite mixtures with real positive weights; `RLe` (success ≥ 2/3 on every promised input); R as the least such budget |
   | 79–140 | The quantum model: basis ι × Bool × workspace; `bitOracle` (exactly O_x); `AdaptiveProgram` (arbitrary input-independent isometries, oracle calls, adaptive basis measurements); a syntactic per-branch `queryCap`; `QLe`, including the constant-function case |
   | 142–182 | Forrelation and P by exact integer tests |
   | 184–283 | Circuits, transcripts, the winner predicate and `Fkm` |
   | ~290–326 | L, G, `BansalSinhaLower`, `UniversalPower` and `alphaTot` |

3. **The four compared theorems,** each in mathematical notation beside its Lean name:
   - `alpha_tot_eq_four`;
   - `theorem_one_one`: α_tot = 4, the universal quartic bound, and for each k ≥ 2 constants S, A, b, t₀ with, for all t ≥ t₀, one circuit C realising P of size ≤ S·m·(2t)², Q(F) ≤ A·√m·(2t)^b and ⌊mL/100⌋ < R(F) **for the same C**;
   - `cubic_bound_fails`;
   - `forrelation_lower_bound`.

   State plainly that b is existential here, and that b = 6 and the constant 1/400 come from a built but uncompared theorem.
4. **Five things to check:**
   1. error ≤ 1/3 is non-strict and holds on every promised input, and caps are worst case over all branches;
   2. quantum unitaries are input-independent and the only input access is O_x;
   3. `totalise` imposes no promise on F;
   4. `alphaTot` is an `sInf`. Mathlib returns 0 for the infimum of an empty set, so "α_tot = 4" alone could in principle hide an empty set; `theorem_one_one` also proves `UniversalPower 4`, which closes that gap;
   5. the quantifier order is ∀k ∃ constants ∃t₀ ∀t ∃C, with one C for both bounds.
5. **What Comparator certifies.** The challenge and the solution are compiled separately. For each configured theorem name, the solution's declaration has the same type as the challenge's, and that type is built from the challenge's definitions, so a solution cannot redefine R, Q or F. The proof uses only `propext`, `Quot.sound` and `Classical.choice`. `--paranoid` re-checks with Lean's other kernels. Five deliberately wrong solutions are rejected.
6. **What it does not certify.**
   - Both sides are generated from one specification (`Statement.lean`), so a modelling error shared by both passes. A deliberately vacuous shared specification also passes.
   - Theorems not configured as targets (for example `construction_family_named`, `Paper.eq_21`, the retained-state amplifier) are only built, not compared.
   - The recorded local runs were unsandboxed.
   - No human has reviewed the definitions or the Forrelation proof.
7. **Commands and pins.** Commit, toolchain, `lake build QuarticQuery`, the Comparator command and the reachability script.

## 5. Revision brief for the author

You are revising two documents for expert readers in query complexity and their students. Do not change the mathematics except where this brief says so. Every changed factual or formal-status sentence must be checked against the cited file before you write it. Do not cite anything from memory.

**Inputs to read first:**

- the preprint, `research/returns/round4/members/02_short_expert/source_packet/paper/extracted.md` (§1.1 for history; the reference list);
- the cheat-sheet paper extraction, `source_packet/literature/quartic-ref-02-*/extracted.md` (line 23; §3.1);
- `lean/QuarticCorpus/Unconditional/Challenge.lean`, `Solution.lean` and `comparator.json`;
- `lean/QuarticQuery/Paper/ConstructionFamily.lean:30–40`;
- the audit's `mathematical_addenda.md` §A and `repairs/companion_refresh_note.md`;
- `04_quantum_completion/quantum_return/review_notes.md`;
- `05_classical_completion/.../review_notes.md` (items 1 and 4);
- `06_corpus_fidelity/quartic_r4_06_return/review_notes.md` §3;
- this review's §4.

**Short paper (target: about 13 pages, US Letter or A4, with at least two figures):**

1. Delete the pre-title provenance paragraph, the "reconstructed download edition" subtitle, and the closing "Reading and evidence scope" paragraph. Add a byline: "Will Cook (direction); text and formalisation produced with AI assistance. The theorem and construction are OpenAI's. No human has reviewed this companion or the Lean development."
2. Rewrite the abstract as five plain sentences (P13).
3. Add §1.1, "Where this sits".
   - A table of exponents: 5/2 (ABK 2016, cheat sheets), 8/3 − o(1) (Tal), 3 − o(1) (Bansal–Sinha; independently Sherstov–Storozhenko–Wu), 4 − o(1) (OpenAI 2026), against the upper bound O(Q⁴) (ABKRT, via Huang).
   - ABK's remark that the cheat-sheet method gives a cubic separation from an optimal partial separation, and ABKRT Conjecture 2.
   - Credit k-fold Forrelation to Aaronson–Ambainis, and their conjecture that it achieves the optimal separation.
   - Credit pointer functions (Göös–Pitassi–Watson; Ambainis et al.) for the all-one column with pointers to zeros.
   - Credit ABK for addressing by partial-function answers, noting their 10 log n copies against r = 20 log₂ m here.
   - Credit comparison-based search: Dürr–Høyer, king finding, Ben-David–Kothari 2026, Ambainis–Iraids–Kokainis 2026.
   - Say in one sentence why Høyer–Mosca–de Wolf does not apply: loser–loser comparisons are unreliable.
   - Add the missing entries to the rendered references from `references.bib`. Ambainis–Iraids–Kokainis (arXiv:2609.11664v2) must be added from the preprint's reference [5]; check the arXiv record first.
4. Add §1.2, "The idea", half a page with a figure of one column.
   - State Q ≈ √m·polylog against R ≈ m·L with L ≈ m^{1−1/k}, so the exponent is 4 − 2/k.
   - Explain what the outward pointers buy (a winner beats any rival at any address) and why a tournament rather than Grover search is needed (rival comparisons may be off-promise and arbitrary).
   - Any claim about why earlier methods stalled must be traceable to ABK §3.1 or preprint §1.1–1.2.
5. Add a half-page table, "Where a natural shortcut fails", with one row per delicate point and its counterexample (P08). Take every counterexample from E, the audit or return 05, and cite where it is verified.
6. Section 3: state the amplification lemma, keeping both the cap clause and the conditional-law clause. Replace the full Grover derivation with a 4-line sketch citing BHMT Lemma 1 and BBHT Lemma 2. Keep the drift, sampling, coupling and verification arguments in full. Give the query count that yields (log m)⁶, or say that 6 comes from the formal budget accounting (P10).
7. Section 4:
   - State Pr[erased zero hit] = E[Z]/m and give the one-line dependent-index counterexample.
   - In the direct product, require coins and side information to be jointly independent of the whole tuple.
   - Present 2G/m² as a remark, not a contribution.
8. Section 5: cut to one page. State (2); say that Lean proves it by an alternative route (Gaussian path plus the Girish–Tal–Wu growth method), in the weaker fixed-k form; say it is one of the four compared theorems; say no human has reviewed it. Handle the Bansal–Sinha v3 display per P14: omit it, or give one neutral footnote.
9. Section 6: keep the quantifier paragraph. Replace §6.1 with a half-page remark based on audit addendum A (t ≥ 80, k = ⌊√(t/20)⌋, R ≥ Q^{4−ε(s)}, log R/log Q → 4), labelled as an ordinary deduction checked by AI, not a Lean theorem and not R = Ω(Q⁴).
10. Replace §7 with the one-page appendix specified in §4 of this review.
    - Name the configured targets `QuarticQuery.Checked.*`.
    - Display `theorem_one_one` in mathematical notation and say which constants are compared and which are only built.
    - Use conditional wording for every claim from returns 04, 05 and 06 until the independent rebuild produces a receipt. For example: "A Lean proof that amplification returns the full good state has been submitted and is being independently rebuilt; the separation does not depend on it."
    - After the rebuild, replace the conditionals with exact declaration names and the commit.
11. Remove all relative links into `source_packet/`. Refer to the long record by public URL and section number.
12. Remove house terms (P16). Fix the notation collisions (P11) by renaming: M_amp → J for the iteration range; stage count T → τ_max or K_T; tree → 𝒯; query time → j; test function G → h; km → N′. Add preprint equation numbers in brackets at matching displays.
13. Re-render and inspect every page at 100%: no overfull lines (the p.15 hash line), at least two figures, and no table wider than the text block.

**Exposition (target: 12–15 pages A4, 3–4 figures):**

1. Add a byline and attribution matching S. Correct md:348 to: "The separation theorem and the construction are OpenAI's; addressing certificates by partial-function answers comes from Aaronson, Ben-David and Kothari's cheat sheets, and the all-one column with pointers to zeros from Göös, Pitassi and Watson." Add those references, Tal, SSW, and AA by its published venue.
2. Add a 1-page overview before §1:
   - the theorem in words and symbols;
   - the R ≈ mL vs Q ≈ √m arithmetic;
   - a three-line history;
   - a map of which example illustrates which step.
3. Add figures:
   - the column, address and cell layout;
   - the reduced board of §2, drawn with the winning cell and pointers;
   - a 3–4 node tournament with a cycle among losers and the winner's weight;
   - the planted pair (dummy vs planted, the two changed locations).
4. Keep the 8-bit census, the changed board, the dominance-without-winning example, the uniform-marginal counterexample and the AND example. Add the two-instance AND example from return 05 (β = 3/4; joint 5/16; conditional 5/8 > β² = 9/16) after verifying it against 05's checks.
5. Cut or box:
   - the canonical-lift paragraph (md:65);
   - the residue-width detail (md:102);
   - inline Lean names, moved to a final half-page "Where this is checked" list;
   - the minimax and Chernoff proofs, as boxed asides;
   - bibliography provenance (hashes, "byte identity", "unavailable to this session").
6. Move §5 (state versus label) after the tournament, as a short boxed remark. Update it per P05 with conditional wording.
7. Remove the "supplier" and "proof destination" vocabulary and the relative `sources/…` links. Rename the winning column from s to i⋆.
8. Derive or attribute the (log m)⁶ exponent (P10).

**Do not:**

- claim any Lean or Comparator result that lacks a receipt from the current rebuild;
- describe the Forrelation proof as reviewed;
- present the 2G/m² constant or the growing-k remark as headline contributions;
- state anything about Bansal–Sinha's paper beyond the one neutral footnote;
- use "certifies" for Comparator in the sense of semantic fidelity.
