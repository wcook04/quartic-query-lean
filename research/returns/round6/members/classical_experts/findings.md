# Located findings for the classical expert panel

This is the readable edition of findings.json. Both contain the same 54 findings, including 22 keeps. The order puts the largest decision points first, then narrower recommendations, then material to preserve. These are simulated research perspectives, not attributed opinions of real people. Source editions and actual reading coverage are in research_scope.md. The exact current-Markdown quotations were mechanically checked.

## Panel

| Perspective ID | Anchoring papers | What this reader already knows |
|---|---|---|
| cheat_sheet | Aaronson–Ben-David–Kothari, Separations in Query Complexity Using Cheat Sheets, arXiv:1511.01937v2; Ben-David, A Super-Grover Separation, arXiv:1506.08106 precursor. | Partial-to-total addressing, promise certificates, AND-OR cost arithmetic, blank-array hybrid lower bounds and critical exponents. |
| pointer_functions | Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs, Separations in Query Complexity Based on Pointer Functions, arXiv:1506.04719v3. | All-one marked columns, pointer chains/trees/back pointers, alphabet Booleanization, and distinct D/R0/R/Q separations. |
| communication_origin | Göös–Pitassi–Watson, Deterministic Communication vs. Partition Number, ECCC TR15-050, §2.1. | Unambiguous certificates, unique accepting witnesses, pointer paths, and the separation between query construction and communication lifting. |
| certificate_comparisons | Ben-David–Kothari, Randomized Query Complexity Can Beat Certificate Complexity, supplied arXiv:2609.15063v1, Lemma 5; Ambainis–Iraids–Kokainis, supplied arXiv:2609.11664v2, §6.1. | Generate/compare/verify architectures, fixed-orientation sink/king search, and why a C-versus-Q gap is a different statement from an R-versus-Q gap. |
| drucker_fair_product | Andrew Drucker, Improved Direct Product Theorems for Randomized Query Complexity, arXiv:1005.0644v2, §§1.2–1.3, Lemmas 3.1–3.2 and final paragraph of §3 | Distributional hardness, per-instance fair caps, conditional product laws, value-function supermartingales, global-budget direct products, and minimax. |
| shaltiel_fair_trees | Ronen Shaltiel, Towards proving strong direct product theorems, ECCC TR01-009, §1 and §5, Definition 4, Theorem 5, Lemma 7 | Why pooling computational resources can defeat ideal product parameters; fair paths; the distinction between XOR advantage under the uniform law and vector-output success under a general law. |
| finite_minimax | Drucker, arXiv:1005.0644v2, §2.1 and §5 (the minimax lemma); Yao 1977 is cited only and was not read | Bounded-depth randomized trees as finite mixtures, strict minimax separation below randomized complexity, and distributional lower bounds. |
| forrelation_interface | Aaronson–Ambainis, arXiv:1411.5729v1, §3.2; Tal, arXiv:1912.12561v1, introduction and Definition 5.5; Bansal–Sinha, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4; Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Theorem 1.1. | The Forrelation experiment, promise thresholds, optimal partial query separations, and the difference between an explicit Walsh matrix and a random orthogonal matrix. Wants to know the additional exact-certification interface consumed by totalization. |
| forrelation_analytic | Bansal–Sinha, arXiv:2008.07003v3, §1.2.1 and Theorem 3.2; Girish–Tal–Wu, arXiv:2103.11604, ordinary-tree overview and Lemma 1.9 in the inspected v2 text; Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Corollaries 4.14–4.15. | Gaussian chains, Fourier growth, restrictions, interpolation and martingale arguments. Distinguishes a raw derivative at a biased point from a uniform Fourier level, and a distribution-specific hardness theorem from a general Fourier estimate. |
| quantitative_parameters | Bansal–Sinha, arXiv:2008.07003v3, Theorem 1.3 and §5.4; Tal, arXiv:1912.12561v1, §1.1; Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Corollaries 4.14–4.15. | Fixed-parameter asymptotics, amplification costs when k grows, dependence on error and logarithmic factors, and the need to compare edition-specific statements in all their parameters. |
| universal_exponent | Huang, arXiv:1907.00847v2, Theorems 1.1 and 1.4; Aaronson–Ben-David–Kothari–Rao–Tal, arXiv:2010.12629v1, Theorem 2, Theorem 1 and Lemma 9. | The known D=O(Q^4) upper endpoint, the spectral-sensitivity/degree bridge, block sensitivity and quantifier order in universal powers. Wants the exact lower-bound family and a clear distinction between a universal exponent and an attained fourth-power family. |



## CX001 — question · high

**Document:** expert_companion. **Perspective:** drucker_fair_product.

**Locator:** §5.1, source comparison; repository/docs/expert_companion.md, line 198.

> while his headline theorem assumes one global budget

**Finding.** Why choose the exact fair-tree product bound rather than invoke Drucker's global-budget theorem, which already suffices for this simulator? With T=L, multiplicity r, epsilon=1/3 and alpha=3/r, the latter allows total cost L and gives 2(2/3)^r. For every admitted construction parameter, the doubled guessing term still gives the stated 6/100 discrepancy ceiling. The distinction between theorem statements is correct, but does not explain the methodological choice.

**Why it matters.** A reader who knows Drucker's theorem may infer that its global-budget version is unusable here, or spend time reconstructing an elementary adequate specialization. The construction-specific reduction should remain the centre of the lower-bound account.

**Suggested direction.** Explain the benefit of the exact fair formulation (the clean beta^r bound and transparent cap invariant), and distinguish a chosen proof route from an applicability obstruction. No replacement proof or stronger result is requested.

**Evidence and scope:**

- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)
- repository/docs/expert_companion.md; §5.4 total simulator cap L; §5.5 G<=m^2/100 and beta^r<=m^-10; Parameter substitution into the cited theorem, not a new theorem: alpha*epsilon*T*r=L; bound=2(2/3)^r. For actual r=20 log_2 m>=40, alpha<=1.
- literature/quartic-ref-13-improved-direct-product-theorems-for-rando/source.tex; Theorem 1.1, lines 313–314 (printed p. 4); partial functions, line 363 (p. 6); query model, lines 430–449; full proof, lines 504–606 (pp. 10–13); integer cap floor, line 556; Independent adversarial check recorded in direct_product_comparison.md. For actual r=40t>=40, alpha=3/r is in (0,1]; floor(alpha*epsilon*T*r)=L. The promise-supported product law, weak <=2/3 premise and jointly independent outside data meet the source contract. The result is an adequate 2*beta^r bound, not the sharp beta^r intermediate statement.



## CX002 — underweighted · high

**Document:** expert_companion. **Perspective:** pointer_functions.

**Locator:** 1.3 What is new; repository/docs/expert_companion.md, line 65; inspected PDF page 3.

> whose functions already separate deterministic from quantum query complexity with a nearly quartic power.

**Finding.** Which predecessor variant is being compared? The nearly quartic D-versus-Q variant also has an efficient zero-error randomized algorithm using back pointers. The same paper separately gives a balanced-tree variant without back pointers that is hard for Monte Carlo algorithms. The lineage paragraph should explain why these known ingredients did not already give the present R-versus-Q tradeoff.

**Why it matters.** The substantive transition is from D versus Q to R versus Q. A specialist will distinguish the back-pointer variant’s easy randomized search from the no-back-pointer variant’s more expensive stated quantum search; a blanket claim that older pointer functions are easy for randomized algorithms would be false.

**Suggested direction.** Briefly identify the near-quartic predecessor’s back-pointer tradeoff, acknowledge the Monte-Carlo-hard variant, and connect the current access discipline to the existing comparator and simulator: an X-zero alone reveals no certificate, and a useful outgoing certificate lies behind that column’s hard address. No new predecessor lower bound or barrier theorem is requested.

**Evidence and scope:**

- literature/quartic-ref-04-separations-in-query-complexity-based-on-p/extracted.md §1.3, lines 222–240 and 260–294: back pointers, balanced trees, and distinct f/g/h variants.
- Same source, corollary labeled cor:R0-D, lines 828–834: the near-quartic D-versus-Q family also has zero-error randomized complexity tilde O(n) at D=Omega(n^2); no-back-pointer Monte Carlo result and stated quantum search, lines 1194–1213.
- repository/docs/expert_companion.md §§2, 4.1–4.3 and 5.4; record §§4.2 and 6.5.



## CX003 — unclear · high

**Document:** reasoning_record. **Perspective:** forrelation_interface.

**Locator:** Reading guide, Required proof path table; compare §1 Dependencies and §3 ingredient preview; repository/docs/reasoning_record.md, line 16.

> Required proof path

**Finding.** The first route table places the full Forrelation hardness derivation (§§3.6–3.15) on the required path, although §1 says that the central construction can be read after §§3.1–3.5 and §3.17, and §3 expressly allows a reader to accept the hardness property and continue at §4. Which route should an expert who accepts the published supplier actually follow?

**Why it matters.** The table is the first allocation of reader effort. A reader familiar with the optimal partial separation can infer that a long rederivation is a prerequisite to seeing the new totalization, even though the later directions correctly say otherwise. The inconsistency undermines the valuable bypass added in the previous round.

**Suggested direction.** Make the opening route table agree with the existing citation-based construction route and the separate independent-proof route. Keep all proof locations and preserve the complete derivation for readers who choose it.

**Evidence and scope:**

- Current record §1, Dependencies and proof recovery; §3, The ingredient used by the construction, final sentence; §3.6 (F4)–(F5).
- OpenAI preprint Lemma 2.1(i), §2.1, printed pp. 3–4, imports the Forrelation lower bound.
- Bansal–Sinha, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, printed p. 4.
- Previous-round record disposition adds the ingredient preview; this finding concerns the remaining inconsistent table, not absence of the preview.



## CX004 — evidence_presentation · high

**Document:** exposition. **Perspective:** finite_minimax.

**Locator:** §7, final sentence; compare expert Appendix A and record §2.9; repository/docs/exposition.md, line 269.

> No recorded statement review yet covers the four compared theorems or these two statements

**Finding.** The exposition denies the existence of statement reviews that are supplied in this packet and explicitly cited by the expert companion. The record’s §2.9 also retains “no review” or outdated-review descriptions for the amplifier and direct product. This is an inconsistent account of existing evidence, not a request for another receipt audit.

**Why it matters.** A reader who checks the formal meaning cannot tell whether the asserted same/stronger/partial relationships were independently inspected or merely inferred by the writer. The correct absence of human review does not imply absence of the recorded independent AI statement review.

**Suggested direction.** Reconcile these statements against the supplied round-five statement-fidelity report, identifying its date, scope and nonhuman reviewer. Keep build, Comparator acceptance, statement-fidelity review and human mathematical review as separate facts; retain any genuinely source-specific limitations.

**Evidence and scope:**

- previous_round/round5_statement_fidelity.md, opening scope, “The four compared theorems,” and “Other cited results”; it explicitly says no Lean run and no proof judgment.
- Current expert Appendix A, paragraph following Table 2, cites an independent review of every cited statement and says both reviews were made without a person.
- Current record §2.9, amplifier/direct-product rows and final paragraph.
- Packet READ_ME_FIRST.md, State of the evidence, supplies this evidence status as a premise for the present review.



## CX005 — overweighted · high

**Document:** reasoning_record. **Perspective:** drucker_fair_product.

**Locator:** §6.1, optional second proof; repository/docs/reasoning_record.md, line 3117.

> #### Optional: a second proof with unnormalized weights

**Finding.** Section 6.1 occupies about 34.9% of the current classical section’s cleaned text (2,812 of 8,050 prose/math units), while the capped simulator in §6.5 occupies about 12.1% (975 units). Two complete proofs of the familiar fair direct product precede the construction-specific reduction. The normalization identity (6.11), which explains the second proof’s payoff, arrives after both.

**Why it matters.** An expert following the advertised required §§6.1–6.6 path encounters a long treatment of familiar value-function facts before the decisive reduction. Completeness is useful in a record, but does not itself identify a worthwhile first reading.

**Suggested direction.** Give an expert a route from the precise direct-product contract to the planted pair and simulator. Keep both full proofs in the record; identify their normalization relationship before the optional second proof, and give the simulator and joint-event reduction more of the compulsory reading budget. The estimates measure text load, not current rendered record pages.

**Evidence and scope:**

- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)
- repository/docs/reasoning_record.md; Reading guide required classical path; §§6.1–6.7; Whitespace-separated current Markdown units after removing HTML comments, anchors and link destinations: 213 opening units plus subsection counts 2812, 674, 710, 1166, 975, 942, 558, for 8050 in the whole §6. Shares are 2812/8050=34.93% and 975/8050=12.11%. These are reading-load estimates, not current PDF page counts.
- previous_round/dispositions/reasoning_record.json; LR-021; The subheadings/optional label were fixed; this finding concerns remaining expert weighting.
- repository/docs/reasoning_record.md; §6.1 #CL-normalization, equation (6.11)
- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)



## CX006 — unclear · medium

**Document:** expert_companion. **Perspective:** pointer_functions.

**Locator:** 1.3 What is new; repository/docs/expert_companion.md, line 65; inspected PDF page 3.

> Here each pointer is a separate $\ell$-bit field, read in $\ell+1$ bit queries

**Finding.** How does selective access to one pointer field change the cost accounting that made an exponential alphabet unacceptable in the predecessor? The juxtaposition can sound as though binary encoding alone solves the old obstacle.

**Why it matters.** A pointer-function expert will want the operation being charged: one local comparison reads two selected fields; it never reads the whole m-pointer symbol. The expensive global check is postponed.

**Suggested direction.** Make the selected-field operation and its role in comparison explicit beside the alphabet comparison; refer to the existing total bit count and final verification rather than suggesting an encoding trick alone gives the improvement.

**Evidence and scope:**

- literature/quartic-ref-04-separations-in-query-complexity-based-on-p/extracted.md “Use of a balanced tree,” lines 260–275; original PDF p. 6.
- repository/docs/expert_companion.md §2 input-size formula; §§4.1 and 4.3.



## CX007 — unclear · medium

**Document:** exposition. **Perspective:** cheat_sheet.

**Locator:** Overview, The reason for four; repository/docs/exposition.md, line 32; inspected PDF page 1.

> locating it inside one column means naming an address, which costs $L$ queries there.

**Finding.** The opening heuristic states a per-column cost as though every visit computes the address; the later proof correctly allows lucky guesses. The preceding roadmap also says “almost every column,” while the proof needs a constant fraction in the aggregate.

**Why it matters.** A classical lower-bound reader may reconstruct a false deterministic decision-tree claim from the introduction even though §5 proves the correct joint-event bound.

**Suggested direction.** Align this heuristic with the established two-channel lower bound, the lucky-guess alternative and the constant-fraction charging language already used in expert §1.2. Keep it intuitive, with the precise event in §5.

**Evidence and scope:**

- repository/docs/exposition.md Overview lines 26–32 and §5 lines 214–239.
- repository/docs/expert_companion.md §1.2 already includes lucky guesses, erased-zero search and a constant fraction.



## CX008 — unclear · high

**Document:** reasoning_record. **Perspective:** drucker_fair_product.

**Locator:** Reading guide, The mechanism; repository/docs/reasoning_record.md, line 10.

> A classical algorithm must pay about

**Finding.** The first mechanism paragraph says a classical algorithm must pay to learn an address across about m columns. As a literal description of every successful run, this is too categorical: the proof allows lucky address guesses, many cell probes, and the distinct erased-zero channel. The later §6 is correct; the expert companion's repaired §1.2 already states both routes and the guessing alternative.

**Why it matters.** The most reusable overview reintroduces the misleading learned-address intuition that the full proof carefully avoids. An expert can reasonably ask whether an information-acquisition assertion has been substituted for a joint-event probability bound.

**Suggested direction.** Bring this current-record overview into line with its existing §6 contract and the repaired companion, retaining a concise two-route probabilistic explanation. Do not expand every later passage or repeat the full proof.

**Evidence and scope:**

- repository/docs/expert_companion.md; §1.2, Classical mechanism paragraph
- repository/docs/reasoning_record.md; §6 opening; §6.5 #CL-joint-event
- previous_round/dispositions/expert_companion.json; CM-004 and ER-011; Those fixes landed in the expert paper. This finding is scoped to the current record's overview.



## CX009 — unclear · medium

**Document:** exposition. **Perspective:** cheat_sheet.

**Locator:** 5. The classical lower bound: a planted pair, Figure 4; repository/docs/exposition.md, line 197; inspected PDF page 10.

> The planted pair on the board of Section 2

**Finding.** Which data of the earlier board are reused in Figure 4? Section 2 has an unpromised address instance in column 2 and valid transcripts in every cell. The planted distribution instead samples every address input from the promised hard law and leaves every unplanted cell blank. The figure itself labels the new A-inputs by μ, so the issue is the handoff between the examples.

**Why it matters.** Reusing the board without announcing these resets can make a student believe the fixed off-promise board is a sample of the hard distribution. It is not evidence of asymptotic hardness at m=4 either.

**Suggested direction.** Identify the reused geometry and the reset address/cell data. Keep the m=4, r=2 picture explicitly illustrative of the coupling, with the large-m distribution carrying the lower bound.

**Evidence and scope:**

- repository/docs/exposition.md §2, lines 96–108; §5, lines 193–197.
- repository/docs/exposition.pdf pp. 4 and 10: earlier column 2 has no address; Figure 4 labels all address inputs as samples from μ.
- repository/docs/reasoning_record.md §4.3, line 1859, explicitly distinguishes the toy construction from a separation instance.



## CX010 — underweighted · medium

**Document:** expert_companion. **Perspective:** drucker_fair_product.

**Locator:** §5.4, the capped simulator; repository/docs/expert_companion.md, line 234.

> If it reaches time $\tau$ and the $\tau$-th query lies in a cell $B_{i,s}$, it outputs $s$

**Finding.** The key reduction is that the location of a proposed cell query already names an entire answer vector, before any cell content is read. This sentence supplies the decisive operation, but only after the generic product proof and the planted setup. What exactly does the product theorem receive as its output, and why is that output available for free?

**Why it matters.** For a direct-product specialist the novel application is this extraction from a query address. Without foregrounding it, the proof can look like another explanation of independent hardness rather than an adaptive transcript reduction.

**Suggested direction.** Promote the existing address-extraction observation when introducing the classical mechanism, and point directly to the record's simulator trace. Keep its unconditional event inclusion beside the operation; no extra theorem is needed.

**Evidence and scope:**

- repository/docs/reasoning_record.md; §6.5 #CL-simulator and #CL-simulator-example
- paper/extracted.md; §4.2, Reaching the planted cell, printed p. 13, equation (21)



## CX011 — question · medium

**Document:** expert_companion. **Perspective:** forrelation_interface.

**Locator:** §2, Forrelation property (iii); compare §1.3 credit paragraph; repository/docs/expert_companion.md, line 101.

> An exact fan-in-two Boolean circuit $\mathcal C$

**Finding.** Which requirement makes the explicit Walsh version important to this totalization? The text correctly distinguishes the explicit-Walsh and random-orthogonal lower bounds, and then gives the fast exact circuit, but leaves the reader to connect the two facts: a partial query separation alone is not the full ingredient; efficient exact certification of its promise and value is also consumed by the construction.

**Why it matters.** Readers of the random-matrix separation may naturally ask why their optimal partial separation is not simply interchangeable here. The missing connection is about the existing three-part interface and certification cost, not about the validity or strength of their result.

**Suggested direction.** Connect the attribution paragraph to property (iii) and the existing Walsh-transform circuit explanation, pointing out which existing hypothesis would still need justification before substituting another partial function. Do not claim that random-matrix ingredients are impossible or request a new construction.

**Evidence and scope:**

- Current companion §2, properties (i)–(iii) and local-test count K; record §§3.4 and 3.17.
- OpenAI preprint Lemma 2.1(ii)–(iii), §2.1, and Lemma 2.2.
- Tal, arXiv:1912.12561v1, §1, pp. 1–3; Definition 5.5, p. 14, distinguishes random good matrices from the Hadamard matrix.
- Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Theorem 1.1 and §1.8; Bansal–Sinha, Theorem 1.3.



## CX012 — underweighted · medium

**Document:** expert_companion. **Perspective:** quantitative_parameters.

**Locator:** §6, opening paragraph and equation (16); repository/docs/expert_companion.md, line 262.

> This section states the only property of $P$ that the lower bound uses and the stronger form in which Lean proves it.

**Finding.** The corrected text no longer calls (16) a globally sharper replacement for the literature. A reader comparing results still has to assemble four distinct statements from separate locations: the target floor bound, Bansal–Sinha's stated k^−29 bound, the explicit k^−2/log bound (16), and the optional SSW-based variable-error comparison (F60). Their different k dependence, logarithmic powers, dimension conditions and evidence status are the useful comparison.

**Why it matters.** For fixed k, Bansal–Sinha's displayed logarithmic power 1−1/k is asymptotically better than the power one in (16); (16) instead supplies explicit constants and uniform parameter control. A specialist should be able to assess that tradeoff without mistaking 'stronger form' for a claim of domination over the cited theorem.

**Suggested direction.** Provide one compact comparison of the already-stated bounds, preferably at the linked record comparison destination, and identify which is sufficient for the totalization and which is used for the optional growing-k schedule. Keep the current corrected attribution and avoid resurrecting the removed blanket 'sharper' claim.

**Evidence and scope:**

- Current companion §2(i), §6 (16), §7 growing-k remark; record §3.6 (F3)–(F5), §3.15 (F43), Appendix E (F60), and §3.16 evidence scopes.
- Bansal–Sinha, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, p. 4.
- Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Corollaries 4.14–4.15, pp. 35–36: the external Fourier input, not an explicit-Walsh distribution theorem.
- Previous-round expert disposition removed the unspecific sharper-bound sentence; that fix is respected.



## CX013 — overweighted · medium

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** Appendix A, opening; repository/docs/expert_companion.md, line 287.

> This appendix lists everything a reader must read to answer that question.

**Finding.** The statement-checking appendix occupies about 2.46 of 14 rendered pages (17.6%), slightly more than the 2.41-page classical proof. Its complete object map, thirteen-row fidelity table, five checks, theorem list and reproduction instructions overrun the writing method’s promised one-page specialist entry.

**Why it matters.** This audience needs to recover the construction, common witness, model and checked statement. Treating the complete audit inventory as compulsory reading costs attention disproportionate to the new lower-bound mechanism, although the inventory itself is useful.

**Suggested direction.** Make a short first-pass route through the critical definitions, theorem quantifiers and evidence limitations; retain the full fidelity and object mapping at a clearly linked reference destination. Preserve the explicit compared/built distinctions and do not reduce statement fidelity to a badge.

**Evidence and scope:**

- Current expert Appendix A and Table 2; existing record §2.9 and Appendix B provide detailed reference destinations.
- Measured current expert PDF section spans in checks/page_weighting.json.
- skills/long-to-short/SKILL.md, Reference the Lean and Comparator evidence, prescribes a one-page appendix and the extensive inventory.



## CX014 — evidence_presentation · medium

**Document:** expert_companion. **Perspective:** universal_exponent.

**Locator:** Appendix A, Reproducing the check; repository/docs/expert_companion.md, line 351.

> The first line gives the versions of the recorded runs and the commit the links point to.

**Finding.** The reproduction block names commit 659b571, while the source and receipt links in the current companion are pinned to e9dfefbf11e6d1f380f122caa2349d4be78f2c1f. The sentence identifying these as the same commit is false as written. The packet separately records repository provenance 9bdd443ce9b5e2fa5a83d63e0bcb0d87fbed298a.

**Why it matters.** A specialist following the advertised small checking route must know which source snapshot each command and recorded result belongs to. Different commits can have legitimate roles, but a claim that they are identical blocks reproducibility.

**Suggested direction.** Identify the distinct roles of the recorded-run snapshot, the immutable linked source snapshot and the packet snapshot, or align the reproduction block with the intended one. This review does not infer that compilation or comparison failed.

**Evidence and scope:**

- Current expert Appendix A, reproduction code block: “# commit 659b571”.
- Current expert reference definitions [statement-file], [statement-receipt], [thm-all] and [src-reach], all pinned to e9dfefbf11e6d1f380f122caa2349d4be78f2c1f.
- SOURCE_STATUS.json, repository_commit.



## CX015 — question · medium

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** 1.1 The history; repository/docs/expert_companion.md, line 44; inspected PDF page 2.

> The cheat-sheet arithmetic shows why this route stopped at the cube.

**Finding.** Does “this route” mean the displayed AND-OR composition and standard cheat-sheet verification cost, or the whole cheat-sheet framework? The calculation explains the former. The paragraph should not leave a broader limitation implicit.

**Why it matters.** A reader familiar with arbitrary certifying functions in ABK will distinguish one optimized recipe from an impossibility claim about every cheat-sheet construction.

**Suggested direction.** Identify the scope as the displayed AND-OR/cheat-sheet recipe. Retain the existing cost comparison and its certificate-verification term; no new barrier theorem is requested.

**Evidence and scope:**

- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §§3.1–3.2, lines 1417–1431 and 1437–1487; generic framework §6.1, lines 1683–1704.
- repository/docs/exposition.md Overview, lines 36–38.



## CX016 — underweighted · medium

**Document:** reasoning_record. **Perspective:** forrelation_analytic.

**Locator:** §3.6, proof spine; §§3.10 and 3.16; repository/docs/reasoning_record.md, line 1000.

> To prove this indistinguishability, scale only the first block of Gaussian biases.

**Finding.** The optional derivation's most interesting reason to read it is the first-block interpolation: it produces one raw derivative per labelled block, with repeated derivatives vanishing by multilinearity. The opening spine states this, but the comparison with Bansal–Sinha's treatment of derivative levels k through k(k−1), and the role of the changed truncation, is dispersed across the later proof and credit paragraphs.

**Why it matters.** A reader who already knows the Gaussian-chain architecture needs to know what changes in the proof strategy before investing in the algebraic kernel and martingale details. This is a better reason for the rederivation to occupy space than numerical constants alone.

**Suggested direction.** Use the existing proof-spine and literature-comparison material to identify the changed interpolation, the derivative object it controls and the corresponding published proof step together at the independent route's entry. Retain the explicit statement that the bounded searches establish no novelty or priority.

**Evidence and scope:**

- Current record §3.6 proof spine; §3.8 (F9)–(F11); §3.10 (F22)–(F24); §3.16 literature comparison.
- Bansal–Sinha, arXiv:2008.07003v3, §1.2.1, especially its general-k discussion; Theorem 3.2; transformed integration by parts in Lemma 4.3.
- Girish–Tal–Wu, arXiv:2103.11604v2, §1.3 ordinary-tree overview and Lemma 1.9, pp. 6–8; CCC version Lemma 9.



## CX017 — question · medium

**Document:** expert_companion. **Perspective:** quantitative_parameters.

**Locator:** §7, growing-k remark; repository/docs/expert_companion.md, line 283.

> **Remark** (letting $k$ grow)**.**

**Finding.** What reader task earns the full explicit growing-k schedule a place immediately after the fixed-k proof? The remark is mathematically separated from the infimum argument, but packs its uniform hypotheses, a different choice of L, an exponential-in-k quantum coefficient, a schedule and an explicit epsilon formula into one paragraph. Its purpose is harder to see than its arithmetic.

**Why it matters.** A reader checking that the universal exponent is four needs the preceding fixed-k argument. A reader interested in one quantified sequence needs the additional uniform estimates. Compressing both tasks together makes an optional refinement look like unfinished work in the main theorem, or like a stronger exact fourth-power claim, despite the correct caveats.

**Suggested direction.** State the purpose of this already-existing refinement as an optional explicit single-family schedule, and route its detailed arithmetic to the long account while retaining the uniform hypotheses and the no-Omega(Q^4) boundary at the entry. Do not ask for a better schedule or stronger theorem.

**Evidence and scope:**

- Current companion §7, fixed-parameter paragraph and growing-k remark; record §§7.1–7.2 explicitly separate a quantitative schedule from the universal-exponent theorem.
- OpenAI preprint §5, printed p. 14, proves the exponent by fixing k after alpha.
- Tal, arXiv:1912.12561v1, §1 and §1.1, pp. 2–3, explicitly accounts for 2^{O(k)} amplification when k grows.
- ABKRT, arXiv:2010.12629v1, Theorem 2 p. 2 and Conjecture 2 p. 20.



## CX018 — overweighted · medium

**Document:** reasoning_record. **Perspective:** universal_exponent.

**Locator:** Appendix A, opening; §A.6 formal-route table; repository/docs/reasoning_record.md, line 3911.

> This appendix reconstructs the known upper bound $R=O(Q^4)$ that makes four attainable.

**Finding.** The known upper endpoint is reconstructed in full and then compared through three implementation constants. This is appropriate reference material, but the opening guide treats Appendix A as part of the required proof path. For readers who know the degree/spectral-sensitivity theorem, why is accepting ABKRT's Theorem 2 not an equally explicit stopping point after the four-inequality bridge?

**Why it matters.** The new separation resolves an existing lower-versus-upper gap. Reconstructing general adversary estimates, rounding and alternate numerical coefficients can cost this audience more attention than confirming that the known upper theorem uses the same model and total-function hypothesis.

**Suggested direction.** Make the citation-based upper endpoint and the optional reconstruction equally clear in the reading routes. Retain the short conceptual bridge and exact credit; keep the three implementation constants available as audit material without making their comparison a mathematical obligation.

**Evidence and scope:**

- Current record Reading guide table; Appendix A opening, (A.2), §§A.2–A.6.
- ABKRT, arXiv:2010.12629v1, Theorem 2 and its short deduction on p. 2; Theorem 1 and Lemma 9, pp. 6–8.
- Huang, arXiv:1907.00847v2, Theorems 1.1 and 1.4; §2 and following spectral remark, pp. 3–5.
- OpenAI preprint Appendix A, printed pp. 14–17, expressly supplies the known bound for completeness.



## CX019 — overweighted · medium

**Document:** reasoning_record. **Perspective:** finite_minimax.

**Locator:** Reading guide; §2 Models, promises and query budgets; repository/docs/reasoning_record.md, line 14.

> A reader checking the theorem needs §1, the models in §2 and the required proof path below.

**Finding.** The route makes all of the standard model discussion an apparent prerequisite. Section 2 contains 5,459 of 50,865 cleaned text units (10.7% of the record, about 13.4 normalized page-equivalents), including full bridges, examples and evidence sections. A classical-query expert mainly needs the particular cap, promise, error and common-algorithm conventions before the construction.

**Why it matters.** A reader already fluent in bounded-depth randomized trees can lose the main construction before reaching it. The model bridges remain valuable for formal meaning, but a complete audit and an argument-level reading are different reader tasks.

**Suggested direction.** Identify a short conventions route and a separate full model-and-evidence audit route. Keep all definitions and equivalence arguments in the record and name where any nonstandard cap or promise convention is used. Do not replace a necessary hypothesis by an appeal to standardness.

**Evidence and scope:**

- Current record §§2.1–2.9, especially all-input syntactic caps in §2.3 and deferred measurements in §2.5.
- Drucker, arXiv:1005.0644v2, §2.1, sets the decision-tree model before using distributional hardness; the panel is assumed to know that model.
- checks/page_weighting.json, current Markdown load estimates and declared PDF limitation.



## CX020 — unclear · medium

**Document:** exposition. **Perspective:** drucker_fair_product.

**Locator:** §7, paragraph on amplification and the direct product; repository/docs/exposition.md, line 269.

> The separation needs neither

**Finding.** The immediate antecedent is the direct-product statement’s two limitations (finite randomness and compliance versus the count condition), but the explanation switches to measured-label amplification and finite distributions. It is unclear which two strengthenings “neither” excludes, and the sentence does not tell a reader where the cap condition used by the simulator is discharged.

**Why it matters.** This is exactly the place where a specialist asks whether a formally proved nearby statement supplies the actual reduction. An ambiguous pronoun can make a sound use look unsupported even when the correspondence is explained elsewhere.

**Suggested direction.** Identify separately the amplification guarantee consumed by the upper bound and the direct-product guarantee consumed by the capped simulator. Point to the existing cap argument and finite-randomness reduction. This is a presentation repair, not a request to formalize either missing generalization.

**Evidence and scope:**

- Current exposition §7, final paragraph.
- Current expert Appendix A, separate amplifier/label-law/direct-product rows.
- Current expert §5.4 and record §§6.1, 6.5, 6.7 for the cap and event treatment.



## CX021 — question · medium

**Document:** expert_companion. **Perspective:** finite_minimax.

**Locator:** §5, hard-law invocation; repository/docs/expert_companion.md, line 186.

> there is a law $\mu$ on the domain of $P$

**Finding.** Is this mu the rounded-Gaussian planted law discussed in §6, or a new promise-supported minimax law? The argument requires the latter, and the record explicitly says that it does not require the hard measure used in the analytic proof. This distinction matters because §6's planted law has off-promise mass.

**Why it matters.** A reader reconciling the Forrelation supplier with the address product can otherwise try to pass the analytic distribution directly into a lemma whose hypothesis requires support on the domain. This is an interface question, not a missing proof.

**Suggested direction.** Identify the role of the minimax law at the first handoff and point to the existing explanation. No explicit sampler, balanced output law, or new distributional theorem is required.

**Evidence and scope:**

- repository/docs/reasoning_record.md; §6.2 #CL-minimax, final sentence; §6.1 statement
- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)
- repository/docs/expert_companion.md; §6, paragraph stating the planted law is not supported on promised one-inputs



## CX022 — misplaced · medium

**Document:** exposition. **Perspective:** finite_minimax.

**Locator:** §5, opening minimax paragraph; repository/docs/exposition.md, line 193.

> separating that hull from the orthant $[2/3,\infty)$ in every coordinate

**Finding.** The round-five move from a convex-separation box to a parenthesis reduced length, but the first paragraph of the planted-pair section still detours through a convex hull, an orthant and its nonnegative normal before showing the pair. An expert accepts finite minimax, while a student who needs this argument needs the linked full proof.

**Why it matters.** This remains a change of mathematical setting at exactly the point where the document promises a concrete planted pair. Neither reader gains much from the compressed proof fragment.

**Suggested direction.** Keep the finite-minimax contract at this point and route the proof to the existing record §6.2. Let the planted pair follow immediately. Treat this as a residual effect of the prior fix, not an unaddressed missing citation.

**Evidence and scope:**

- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)
- repository/docs/reasoning_record.md; §6.2 #CL-minimax
- previous_round/dispositions/exposition.json; CM-016; The former box was replaced by the present parenthesis; the criterion here is reader interruption.



## CX023 — overweighted · medium

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** 3. Where a natural shortcut fails; repository/docs/expert_companion.md, line 120; inspected PDF page 5.

> Each row of Table 1 is a step a reader may be tempted to simplify

**Finding.** Why must a separation specialist read all eight counterexamples before seeing the two main proofs? This table mixes the decisive off-promise comparison issue with standard conditional-probability and quantifier warnings, several before their quantities have been used.

**Why it matters.** It gives familiar technical safeguards almost the same visual weight as the new comparison/planted-cell mechanism, and interrupts the construction-to-proof route.

**Suggested direction.** Keep the table as a scan or optional route and distinguish the two or three construction-specific obstacles from supporting checks. Put each detailed probability example next to its use, preserving its record destination.

**Evidence and scope:**

- repository/docs/expert_companion.md §§3–5 and Table 1.
- reader_principles.md principles 2, 4 and 6.
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §§3.1–3.2 motivates the promise/certificate obstruction before giving the formal lower-bound machinery.



## CX024 — misplaced · low

**Document:** exposition. **Perspective:** certificate_comparisons.

**Locator:** §4, Amplification with a fixed cap; repository/docs/exposition.md, line 181.

> One trial makes no iteration with probability $1/2$

**Finding.** The main tournament narrative pauses for the 9/40 trial-success and ln(40/31) repetition calculation. For this panel the useful interface is the all-input cap, behavior at zero success and exact conditional label law; the displayed numerical recipe adds less than the surrounding explanation of how the sampler realizes the ideal pivot process.

**Why it matters.** The selection mechanism is unfamiliar enough to deserve space. Familiar amplification arithmetic interrupts that mechanism without changing the reader’s understanding of why losing comparisons may remain arbitrary.

**Suggested direction.** Keep the complete amplification contract in the main flow and make the numerical derivation optional, with its existing §5.1 proof destination. Keep the all-branch cap and zero-success clause visible; no extra theorem or quantum routine is requested.

**Evidence and scope:**

- Current exposition §4, Sampling a pivot quantumly and Amplification with a fixed cap.
- Current record §5.1 provides the full amplification proof; expert §4 gives a shorter interface and sketch.
- The cited BBHT and BHMT statements were used through their displayed roles in these drafts; this review does not claim an independent full reading of those papers.



## CX025 — question · medium

**Document:** reasoning_record. **Perspective:** forrelation_analytic.

**Locator:** Appendix E, The sharper external Fourier comparison; repository/docs/reasoning_record.md, line 6027.

> Here is the transfer, to specify exactly what is being compared.

**Finding.** What is the intended payoff of the external comparison (F56)–(F60): identifying the price of the self-contained martingale bound, explaining why a general Fourier theorem can be transferred while a rorrelation distribution theorem cannot, or recording a separate variable-error estimate? All three are present, but the appendix groups this argument with the version-specific Bansal–Sinha display check under one broad source-comparison heading.

**Why it matters.** For this audience the restriction identity (F57) and the cancellation of the amplification factor in (F60) are more informative than a generic 'sharper' label. Its role is different from checking a printed proof step, and it must not be mistaken for either compared Lean endpoint.

**Suggested direction.** Give the two existing Appendix E parts distinct reader purposes and make the external transfer's payoff visible before its algebra. Preserve the stated unspecified absolute Fourier constant, variable-error scope, power-of-two domain and ordinary-mathematics status; do not ask to improve or formalize it.

**Evidence and scope:**

- Current record Appendix E, (F56)–(F60), and §3.16 validation scope.
- Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Corollaries 4.14–4.15, pp. 35–36, including real leaf labels and unspecified absolute C.
- Tal, arXiv:1912.12561v1, Theorem 5.1, Corollary 5.3 and Definition 5.5, pp. 13–14, distinguish the older Fourier estimate and good-matrix hypothesis.
- No transfer of the SSW or Tal random-orthogonal hard distribution is asserted.



## CX026 — underweighted · medium

**Document:** reasoning_record. **Perspective:** communication_origin.

**Locator:** 4.8 Attribution and formal correspondence; repository/docs/reasoning_record.md, line 2091.

> The chain differs from the direct outward pointers here.

**Finding.** What logical role of the GPW pointer certificate survives the change of geometry? The comparison currently emphasizes a chain versus direct edges, but GPW’s central purpose is to specify a unique accepting witness while preserving hard search.

**Why it matters.** A reader from the communication/partition side recognizes the certificate idea through unambiguity, rather than through the drawing alone. That connection explains why the unique-winner proof is worth retaining.

**Suggested direction.** Use the existing uniqueness argument to explain the inherited witness role, and separate it from the new reliable-comparison use of outward pointers. No communication lifting result or new certificate-complexity bound is requested.

**Evidence and scope:**

- literature/quartic-ref-15-deterministic-communication-vs-partition-n/extracted.md §2.1, lines 179–225; particularly the nondeterministic pointer-walk certificate at 208–214.
- repository/docs/reasoning_record.md §4.2, uniqueness lemma (4.5)–(4.6), and §4.7 winner dominance.



## CX027 — overweighted · low

**Document:** reasoning_record. **Perspective:** quantitative_parameters.

**Locator:** §3.15, paragraph after (F51); repository/docs/reasoning_record.md, line 1679.

> The smaller threshold $\lceil54675k^2/4\rceil$ also follows from (F43) and (F50), because the first inequality is already strict.

**Finding.** The second sufficient threshold improves the already enormous integer cutoff by less than one unit of the k^2 coefficient, while changing neither the proof route nor the asymptotic conclusion. The paragraph correctly disclaims optimality, but it has no stated reader use beyond retaining a numerical consequence.

**Why it matters.** For this panel, the meaningful quantitative point is that the independent bound has explicit uniform control. Presenting a second near-identical cutoff alongside that point gives routine numerical sharpening the same local emphasis as the parameter dependence that matters.

**Suggested direction.** Keep the one threshold used by the rest of the documents in the proof flow. Treat the smaller cutoff as optional accounting material or explain an existing downstream use if there is one; do not optimize the cutoff.

**Evidence and scope:**

- Current record §3.15, (F43), (F50)–(F51) and the following threshold paragraphs; companion §§1 and 6 use 13669k^2.
- OpenAI preprint Lemma 2.1(i) requires an eventual fixed-k threshold, not a numerical optimum.
- Bansal–Sinha, arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4.



## CX028 — overweighted · low

**Document:** exposition. **Perspective:** pointer_functions.

**Locator:** 2. One column, then four, Transcripts; repository/docs/exposition.md, line 106; inspected PDF page 4.

> For $P_{2,4}$ there is an exact such circuit with $180$ gates

**Finding.** How much of the exact 180-gate/5936-bit bookkeeping does this reader need before reaching the comparison algorithm? The off-promise domain-bit counterexample is the conceptual point; the exact implementation size is a reproducibility detail.

**Why it matters.** The construction occupies several pages before the decisive search idea. Experts and their students who already know circuit transcripts need an explicit route past numerical inventory.

**Suggested direction.** Keep the four-column object and changed-domain-bit example in the main route; make gate-list size and full-board bit count a small optional check with the existing exact checker link.

**Evidence and scope:**

- repository/docs/exposition.md §2, lines 104–114.
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §3.1, lines 1421–1431, explains certificates by their verification role before implementation details.
- reader_principles.md principles 3 and 6.



## CX029 — misplaced · low

**Document:** reasoning_record. **Perspective:** pointer_functions.

**Locator:** 4.5 A shallow lookup can have large support; repository/docs/reasoning_record.md, line 2008.

> Thus the support is exactly $m+\ell$, although every evaluation path reads only $\ell+1$ bits.

**Finding.** The support-versus-depth diagnostic is correct and useful for auditing the formal model, but why is it on the unmarked construction path? Neither the classical lower bound nor the quantum local-test cap requires the exact support count.

**Why it matters.** The record risks making a repair to an earlier ledger look like a separate ingredient of the mathematical separation.

**Suggested direction.** Mark this diagnostic as optional or give a one-line use label, while preserving its anchor and full argument for readers inspecting the formal statement.

**Evidence and scope:**

- repository/docs/reasoning_record.md §§4.4–4.6, especially (4.12)–(4.16).
- repository/docs/reasoning_record.md §4.8 explains that essential-coordinate support strengthens the printed lemma.
- paper/extracted.md Lemma 2.2 uses adaptive local-test depth, not a support claim.



## CX030 — question · low

**Document:** expert_companion. **Perspective:** drucker_fair_product.

**Locator:** §5.5, the tail and constants; repository/docs/expert_companion.md, line 248.

> $\beta^r=(2/3)^{20\ell}\le m^{-10}$

**Finding.** Which parameter choices are structural, and which provide numerical slack? The address length r defeats a union over at most G adaptive probes, L is the one-instance hardness budget, and m supplies the unknown-column factor. The present display verifies the constants but leaves those design roles implicit.

**Why it matters.** Readers may spend effort on the numeral 20 or the coefficient 6/100 instead of recognising the exact source of the lower bound. This matters especially when the paper has already promoted several explicit constants on page one.

**Suggested direction.** Label the purpose of each parameter where the three error terms are assembled, and identify the constants as slack. Do not optimise them or add a stronger bound.

**Evidence and scope:**

- paper/extracted.md; §4.2, equations (20)–(23), printed p. 13; summary paragraph on printed p. 14
- repository/docs/expert_companion.md; §5.5, equations (14)–(15)



## CX031 — credit · low

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** 1.1 The history, table; repository/docs/expert_companion.md, line 38; inspected PDF page 2.

> cheat sheets with Forrelation [@ABK2016]

**Finding.** The 5/2 row is a correct citation to the general framework, but a chronological history could acknowledge Ben-David’s June 2015 precursor, later subsumed by ABK. That precursor already states both 5/2 and the conditional cubic improvement.

**Why it matters.** The current table may be read as a priority history rather than a deliberately selective dependency history.

**Suggested direction.** Either label the table as a selected lineage or add the precursor in the existing 5/2 row or its note. Describe it as subsequently subsumed, not as an independent competing discovery.

**Evidence and scope:**

- literature/quartic-lit-ben-david-a-super-grover-separation/extracted.md Introduction lines 7–9 and construction lines 21–29.
- https://arxiv.org/abs/1506.08106 (submission 26 June 2015).
- https://arxiv.org/abs/1511.01937v2 (comments explicitly state that v1 subsumes 1506.08106).



## CX032 — credit · low

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** 5.2 Planting a winner; repository/docs/expert_companion.md, line 202; inspected PDF page 8.

> the erased zero is a second channel

**Finding.** Could the lineage of the erased-zero channel also be stated? The single filled cell is now correctly credited to ABK. Ben-David’s earlier composition lower bound already uses one random zero per column and a randomly chosen marked zero, so this component also has an identifiable antecedent.

**Why it matters.** The innovation is the arrangement and joint charging argument for this function. Crediting both ingredients makes that claim easier for specialists to assess.

**Suggested direction.** Retain the existing attribution to ABK and, if giving component-level provenance, add a precise antecedent for the marked-zero search ingredient. Avoid presenting the familiar hidden-zero method as a new lower-bound technique.

**Evidence and scope:**

- literature/quartic-lit-ben-david-a-super-grover-separation/extracted.md “Forandlation Lower Bound,” lines 65–71; “Lower Bound for g,” lines 75–91.
- paper/extracted.md §1.2, lines 99–112, labels the combined planted/capped argument.



## CX033 — keep · keep

**Document:** expert_companion. **Perspective:** certificate_comparisons.

**Locator:** 1.3 What is new; repository/docs/expert_companion.md, line 69; inspected PDF page 3.

> In each, a comparison has a fixed intended outcome.

**Finding.** Keep this precise distinction between earlier certificate-comparison algorithms and the fractional-probability tournament. It correctly identifies the relevant obstacle after the previous round’s cycle correction.

**Why it matters.** A reader of the certificate-separation papers can see exactly why a fixed-orientation subroutine is not being imported without checking its hypothesis.

**Suggested direction.** Preserve the distinction between predecessor comparisons with a fixed intended outcome and the current fractional comparator. Identify the predecessor results as certificate-complexity-versus-randomized and certificate-complexity-versus-quantum separations, and distinguish those from the present randomized-versus-quantum separation.

**Evidence and scope:**

- literature/quartic-ref-09-randomized-query-complexity-can-beat-certi/extracted.md §3, Lemma 5, lines 90–102: a fixed orientation is queried by exact local checks.
- literature/quartic-ref-05-near-optimal-separations-of-certificate-co/extracted.md §6.1, lines 586–615: candidate sets are defined in a fixed graph after classification.
- previous_round/dispositions/expert_companion.json records the repaired cycle/bounded-error distinction.



## CX034 — keep · keep

**Document:** expert_companion. **Perspective:** pointer_functions.

**Locator:** 1.2 The key mechanism, Figure 1; repository/docs/expert_companion.md, line 50; inspected PDF page 2.

> No pointer from any other column can find a zero in $X_{i^\star}$

**Finding.** Keep the first construction figure and the matching outward-pointer explanation. The figure ties an address computation to a selected cell and a concrete disqualification test, including the winner’s protection against arbitrary rival labels.

**Why it matters.** This is the nonstandard interface that turns a large accepting certificate into a cheap comparison. It earns space even for readers who know cheat sheets.

**Suggested direction.** Preserve the arrow meanings, selected-cell distinction and all-one winner; use this figure as the reference object for later cost comparisons.

**Evidence and scope:**

- repository/docs/expert_companion.md §1.2 and Figure 1; expert_companion.pdf p. 2.
- paper/extracted.md §1.2, lines 78–95.



## CX035 — keep · keep

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** 5.2 Planting a winner, Figure 2; repository/docs/expert_companion.md, line 204; inspected PDF page 8.

> They differ only at the erased zero $X_I[J_I]$ and inside the cell $B_{I,s_I}$

**Finding.** Keep the coupled-input figure and the immediate first-difference inequality. It exposes exactly which physical queries can reveal the planted bit and separates the two channels in a way the familiar one-cell cheat-sheet picture does not.

**Why it matters.** The specialist can audit the lower bound by matching its two terms to two visible changes, instead of inferring what is coupled from a probability calculation.

**Suggested direction.** Preserve the shared address inputs, the single filled cell, and the statement that both hit events are evaluated on the dummy run.

**Evidence and scope:**

- repository/docs/expert_companion.md §5.2, equation (10); expert_companion.pdf p. 8.
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §3.2 blank-array comparison, lines 1495–1500.



## CX036 — keep · keep

**Document:** exposition. **Perspective:** cheat_sheet.

**Locator:** 2. One column, then four, The domain bit is needed; repository/docs/exposition.md, line 108; inspected PDF page 5.

> A function that checked only value bits would accept this board.

**Finding.** Keep the changed-board domain-bit example. It demonstrates why totalization requires exact certification of promise membership, despite a quantum decoder that may return a plausible address off promise.

**Why it matters.** This gives a student a concrete operation that connects the older cheat-sheet promise issue to the present total function; a generic explanation of circuit consistency would not supply it.

**Suggested direction.** Retain the single failing domain test and its later connection to all-address soundness in final verification.

**Evidence and scope:**

- repository/docs/exposition.md §2 lines 106–114 and §4 Verification.
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §3.1, lines 1417–1425, motivates the difficulty of certifying a partial-function promise.



## CX037 — keep · keep

**Document:** expert_companion. **Perspective:** pointer_functions.

**Locator:** 2. The construction, Local tests; repository/docs/expert_companion.md, line 116; inspected PDF page 5.

> a non-winning column fails some test at every address.

**Finding.** Keep the universal quantifier over addresses in local verification. This supplies total-input soundness even for off-promise rivals and false dominant candidates, and it belongs beside the construction rather than only in the formal appendix.

**Why it matters.** It prevents the tempting but incorrect substitution of comparison dominance for acceptance, while explaining why the final verification handles every raw input.

**Suggested direction.** Preserve the gate/domain/value distinction and the link from this all-address fact to §4.3.

**Evidence and scope:**

- repository/docs/expert_companion.md §2 Local tests and §4.3.
- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §3.2, lines 1481–1485: evaluate-then-verify uses promise-certifying cheat sheets.



## CX038 — keep · keep

**Document:** expert_companion. **Perspective:** cheat_sheet.

**Locator:** 5.2 Planting a winner; repository/docs/expert_companion.md, line 202; inspected PDF page 8.

> The blank array and the single filled cell follow the cheat-sheet lower bound

**Finding.** Keep the newly explicit attribution of the blank-array/filled-cell coupling, and the explanation that the unknown column supplies the additional m factor.

**Why it matters.** It distinguishes familiar lower-bound structure from the multi-column charging that the reader must actually inspect.

**Suggested direction.** Preserve this sentence through compression. Any extra historical note should refine this attribution rather than displace it.

**Evidence and scope:**

- literature/quartic-ref-02-separations-in-query-complexity-using-chea/extracted.md §3.2, lines 1495–1500.
- previous_round/dispositions/expert_companion.json CM-022 records this as a fixed omission.



## CX039 — keep · keep

**Document:** expert_companion. **Perspective:** shaltiel_fair_trees.

**Locator:** §5.1, attribution; repository/docs/expert_companion.md, line 198.

> Per-path allowances go back to Shaltiel's fair trees, for XOR advantage under uniform inputs

**Finding.** Keep this qualified attribution and the adjacent distinction between Drucker's fair specialization and global-budget theorem. It correctly separates resource convention, input-law convention and target quantity instead of naming a vaguely equivalent direct-product theorem.

**Why it matters.** The panel can recognise its own literature without being told that a uniform-law XOR theorem literally states the present vector-output result under mu.

**Suggested direction.** Preserve the qualifiers and precise record locator when shortening; any new global-budget comparison should augment this correct distinction.

**Evidence and scope:**

- [literature/quartic-ref-22-towards-proving-strong-direct-product-theo/extracted.md](https://eccc.weizmann.ac.il/eccc-reports/2001/TR01-009/index.html); §1.1, footnotes 1–2; §5 Definition 4, Theorem 5 and Lemma 7, printed pp. 11–12
- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)



## CX040 — keep · keep

**Document:** expert_companion. **Perspective:** drucker_fair_product.

**Locator:** §5.1, unnormalized proof; repository/docs/expert_companion.md, line 196.

> zero-weight branches need no division.

**Finding.** The compact weighted-value proof earns space even for a specialist when the paper promises an independently inspectable finite argument. It handles arbitrary promise-supported measures and impossible branches without artificial full-support assumptions.

**Why it matters.** A concise self-contained proof makes the exact cap interface credible and exposes the one-factor induction. Its value is clarity of the contract, not a claim of new direct-product mathematics.

**Suggested direction.** Retain this short proof or its exact destination if the expert route is shortened; do not replace it with an unspecified appeal to independent instances.

**Evidence and scope:**

- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)
- repository/docs/reasoning_record.md; §6.1 #CL-weighted-values and #CL-weighted-product



## CX041 — keep · keep

**Document:** expert_companion. **Perspective:** drucker_fair_product.

**Locator:** §5.4, simulator cap; repository/docs/expert_companion.md, line 234.

> Its total cap on the $A_{i,h}$ is $L$, so Lemma 4 applies.

**Finding.** The simulator obeys a total cap L, which implies every separate per-instance cap, on every run. The original algorithm need not be fair. The light-and-correct event is embedded in the success event of this genuinely capped algorithm, not analysed after conditioning on lightness.

**Why it matters.** This is the exact logical bridge that licenses the direct product under adaptive allocation. Weakening it to a heuristic statement about learning an address would lose the lower bound.

**Suggested direction.** Keep the total-to-separate cap implication and event inclusion together, including the abort rule before query L+1.

**Evidence and scope:**

- repository/docs/expert_companion.md; §5.4, equation (12)
- repository/docs/reasoning_record.md; §6.5 #CL-simulator and #CL-joint-event
- paper/extracted.md; §4.2, equation (21), printed p. 13



## CX042 — keep · keep

**Document:** reasoning_record. **Perspective:** finite_minimax.

**Locator:** §6.4, erased-zero identity; repository/docs/reasoning_record.md, line 3429.

> This identity needs independence and uniformity of \(I\), but no depth bound and no hardness assumption on \(P\).

**Finding.** The exact selection identity is correctly separated from the adaptive-search estimate. This identifies the assumptions doing different jobs and prevents a stronger search inequality from being mistaken for the full equality-and-bound statement.

**Why it matters.** A specialist can audit the two information channels independently. The distinction also explains what the compared conjunction establishes without confusing proof route with endpoint.

**Suggested direction.** Preserve identity-before-estimate order and whole-run independence, while keeping alternative search constants off the main route.

**Evidence and scope:**

- repository/docs/reasoning_record.md; §6.4 #CL-erased-zero-identity and #CL-early-late
- paper/extracted.md; §4.2, equation (19), printed p. 13



## CX043 — keep · keep

**Document:** exposition. **Perspective:** finite_minimax.

**Locator:** §5, final paragraph; repository/docs/exposition.md, line 245.

> Nothing here depends on the size of the circuit, so the bound holds for the same circuit as the quantum algorithm.

**Finding.** This sentence discharges an important quantifier obligation: the lower bound applies to every realizing circuit, so the quantum construction and classical lower bound concern the same total function.

**Why it matters.** A separation requires matching the function, not merely two existential witnesses with similar notation. This concise explanation is more useful than repeating the floor arithmetic.

**Suggested direction.** Keep the same-circuit conclusion in both short accounts and its precise generic formulation in the record.

**Evidence and scope:**

- repository/docs/reasoning_record.md; §6.3 #CL-generic-statement; §6.6 #CL-concrete-lower



## CX044 — keep · keep

**Document:** reasoning_record. **Perspective:** drucker_fair_product.

**Locator:** §6.1, statement explanation; repository/docs/reasoning_record.md, line 2853.

> it does not assert that every posterior encountered during the
> algorithm is equally hard.

**Finding.** The one-input premise quantifies all capped strategies under a fixed initial law, not every posterior law. The value-function proof correctly permits lucky answers to increase conditional predictability and only controls the appropriate average.

**Why it matters.** This is the substantive reason a product proof survives adaptivity. It is a useful hypothesis explanation even when the reader knows the theorem.

**Suggested direction.** Retain this distinction and the one-changing-factor argument. If examples are reduced, these two explanations have higher value than elementary numerical cap counterexamples.

**Evidence and scope:**

- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)
- repository/docs/reasoning_record.md; §6.1 #CL-conditional-values and #CL-supermartingale



## CX045 — keep · keep

**Document:** expert_companion. **Perspective:** finite_minimax.

**Locator:** §5.5, randomized contradiction; repository/docs/expert_companion.md, line 253.

> A randomized algorithm of worst-case cost $G$ is an average of such trees

**Finding.** The final lower-bound transfer is a direct averaging argument over bounded-depth trees. It does not require a second minimax step or a new global hard distribution, and the same coupled pair works against every such deterministic tree.

**Why it matters.** This avoids unnecessary machinery and makes clear that the distribution pair is fixed before the tested algorithm's random tape. The strict contradiction uses a gap below 1/3.

**Suggested direction.** Keep this succinct finishing argument and the explicit all-input worst-case cap convention.

**Evidence and scope:**

- paper/extracted.md; §4.2, final paragraph, printed p. 13
- [literature/quartic-ref-13-improved-direct-product-theorems-for-rando/extracted.md](https://arxiv.org/abs/1005.0644v2); §1.2 Theorem 1.1; §1.3; §3 Lemmas 3.1–3.2 and final paragraph (printed pp. 4, 6–7, 11–13)



## CX046 — keep · keep

**Document:** expert_companion. **Perspective:** forrelation_interface.

**Locator:** §1.3, Forrelation credit paragraph; repository/docs/expert_companion.md, line 67.

> Bansal and Sinha proved hardness of its explicit Walsh–Hadamard form

**Finding.** Keep the explicit division of credit: Aaronson–Ambainis introduced the k-fold Forrelation quantity and quantum interpretation; Bansal–Sinha supply hardness of the explicit Walsh promise and these thresholds; SSW independently obtain the optimal partial separation for rorrelation with a random orthogonal matrix.

**Why it matters.** These results settle closely related separation questions through different ingredients. The current wording makes the construction recognizable to the literature and avoids attaching the random-matrix distribution theorem to the explicit Walsh promise.

**Suggested direction.** Preserve this corrected distinction in any compression, and continue to distinguish SSW's separate general Fourier-growth theorem when invoking Appendix E.

**Evidence and scope:**

- Aaronson–Ambainis, arXiv:1411.5729v1, §1.1.3 p. 4 and §3.2 pp. 13–14.
- Bansal–Sinha, arXiv:2008.07003v3, equations (1.1)–(1.3), Theorem 1.3 and Corollary 1.4.
- Sherstov–Storozhenko–Wu, arXiv:2008.10223v4, Theorem 1.1 and §1.8.
- Tal, arXiv:1912.12561v1, §1 and Definition 5.5.
- Previous-round expert dispositions identify and fix this exact attribution issue; no recurrence is alleged.



## CX047 — keep · keep

**Document:** reasoning_record. **Perspective:** forrelation_analytic.

**Locator:** §3.10, after (F23); repository/docs/reasoning_record.md, line 1271.

> Order $k$ at a biased point does not mean degree $k$ under the uniform measure.

**Finding.** The distinction between raw derivatives at biased points and uniform level-k Fourier coefficients is one of the most valuable technical explanations in the independent Forrelation proof. Equation (F24) explicitly shows why the higher uniform Fourier levels have not been discarded.

**Why it matters.** A specialist can otherwise read the one-path interpolation as an unjustified reduction to degree k, which would obscure the connection to the published Fourier-growth approach and make the proof look stronger for the wrong reason.

**Suggested direction.** Keep this warning attached to the path identity, and preserve the precise attribution that the GTW ordinary-tree lemma motivates the martingale but does not already state the exact biased raw-derivative estimate proved here.

**Evidence and scope:**

- Current record §3.10, (F22)–(F24); §3.11 (F25); §3.16 GTW attribution.
- Bansal–Sinha, arXiv:2008.07003v3, §1.2.1 and Theorem 3.2.
- Girish–Tal–Wu, arXiv:2103.11604v2, §1.3 ordinary-tree discussion and Lemma 1.9, pp. 6–8 (CCC Lemma 9).



## CX048 — keep · keep

**Document:** expert_companion. **Perspective:** forrelation_interface.

**Locator:** §6, proof summary; repository/docs/expert_companion.md, line 269.

> The planted law is not supported on promised one-inputs.

**Finding.** Keep the warning about promise support and the amplified acceptance-gap argument. It identifies a real obstacle: a positive planted Forrelation mean does not produce a hard law already supported on yes-inputs, and a promise solver has no correctness guarantee outside its domain.

**Why it matters.** This is a substantive reason the analytic proof needs moment estimates, amplification and pointwise bounds. The record's inequalities handle the off-promise inputs explicitly; replacing that explanation by a generic appeal to a planted hard distribution would lose the valid inference.

**Suggested direction.** Preserve the short warning in the companion and the pointwise acceptance inequalities (F41)–(F42) in the record. If shortening routine amplification algebra, retain the worst-case cap and the quantitative gap needed by the proof.

**Evidence and scope:**

- Current record §§3.13–3.15, especially (F39), (F41)–(F42) and depth 50kD+1.
- Tal, arXiv:1912.12561v1, §1.1, pp. 3–4, discusses yes-mass that is not known to be near one.
- Bansal–Sinha, arXiv:2008.07003v3, Theorem 3.1 and §5.4.



## CX049 — keep · keep

**Document:** expert_companion. **Perspective:** universal_exponent.

**Locator:** §7, final sentence of fixed-k paragraph; repository/docs/expert_companion.md, line 281.

> For fixed $k$ this excludes exponents below $4-2/k$ only; it gives no separation of the form $R=\Omega(Q^4)$.

**Finding.** The exact claim is now correctly distinguished from an exact fourth-power separation. The proof chooses alpha first, then one fixed k, then lets m grow; k=3 already excludes the cubic conjecture, while the known upper endpoint makes four the minimum admissible universal power.

**Why it matters.** This is the central scientific conclusion. Confusing the infimum statement, a fixed-k family and a growing-k schedule would overstate the theorem even if every displayed family bound were true.

**Suggested direction.** Preserve the order-of-choices paragraph, the same-circuit condition and the no-Omega(Q^4) sentence. The optional growing-k schedule should remain secondary to this complete proof.

**Evidence and scope:**

- Current companion §7; record §§1 and 7.1–7.2.
- OpenAI preprint Theorem 1.1, equation (1), and §5, printed p. 14.
- ABKRT, arXiv:2010.12629v1, Theorem 2, p. 2, and Conjecture 2, p. 20.



## CX050 — keep · keep

**Document:** exposition. **Perspective:** forrelation_interface.

**Locator:** §1, conclusion of the eight-bit example; repository/docs/exposition.md, line 76.

> the example checks conventions only.

**Finding.** The small example earns its place because it tests the sign convention and the distinction between a projection decoder and an exact domain test. The text now correctly says that L=0 at this size, so the finite table is not evidence of classical hardness.

**Why it matters.** The positive and negative large-Forrelation inputs have identical projection probability. That concrete collision explains why the total function needs a certificate of promise membership, a point that remains useful even to readers who already know the partial separation.

**Suggested direction.** Retain the three contrasting inputs and their domain-bit interpretation. Keep the explicit limitation on what the example demonstrates rather than expanding the enumeration into a miniature lower-bound discussion.

**Evidence and scope:**

- Current exposition §1, three-input example and final paragraph; record §3.5.
- Aaronson–Ambainis, arXiv:1411.5729v1, §3.2: projection experiment versus Proposition 6's interference probability (1+Phi)/2, pp. 13–14.
- Bansal–Sinha, arXiv:2008.07003v3, equations (1.1)–(1.3), and Theorem 1.3's one-sided thresholds.



## CX051 — keep · keep

**Document:** reasoning_record. **Perspective:** universal_exponent.

**Locator:** Appendix A, opening explanation of the upper bound; repository/docs/reasoning_record.md, line 3924.

> Huang's signed cube converts spectral sensitivity into a degree bound;

**Finding.** Keep the conceptual four-link bridge: block sensitivity is O(Q^2), spectral sensitivity is O(Q), Huang's signed cube gives degree at most spectral sensitivity squared, and deterministic complexity is at most degree times block sensitivity. The record correctly uses different adversary matrices for the first two estimates.

**Why it matters.** Merely naming the sensitivity conjecture would not explain why the universal exponent is four. This bridge credits the precise ingredient recovered from Huang's proof and the ABKRT application, while showing the exact role of totality.

**Suggested direction.** Retain the bridge as the main mathematical entry to the appendix, even if the numerical constants and alternative formal assemblies receive less prominence.

**Evidence and scope:**

- Current record Appendix A, (A.2), §§A.3–A.6.
- Huang, arXiv:1907.00847v2, Lemmas 2.2–2.3 and proof of Theorem 1.1; spectral remark on p. 5.
- ABKRT, arXiv:2010.12629v1, Theorem 1, Definition 7 and Lemma 9, pp. 6–8; deduction of Theorem 2, p. 2.
- The Midrijanis source was not independently reread in this subreview; its role is corroborated by ABKRT's deduction and the current record's §A.5.



## CX052 — keep · keep

**Document:** reasoning_record. **Perspective:** quantitative_parameters.

**Locator:** Appendix E, Bansal–Sinha §5.4 comparison; repository/docs/reasoning_record.md, line 5988.

> This calculation compares two displayed upper-bound expressions; it neither constructs an algorithm nor disproves Bansal and Sinha's theorem.

**Finding.** The appendix confines its source criticism to an identified displayed comparison in a specified arXiv version, gives the actual unbounded logarithmic ratio, and expressly separates that observation from the truth of the stated lower-bound theorem. That evidential boundary should survive any shortened report.

**Why it matters.** Without the boundary, an independent formal proof could be marketed as repairing or superseding a literature theorem when the evidence establishes only a problem in one printed inference. The current record is careful about both credit and the exact claim checked.

**Suggested direction.** Keep the inspected version and exact step locator with the calculation. Do not generalize the observation to other editions or to the theorem without separately inspected evidence, and keep it off the construction's required reading route.

**Evidence and scope:**

- Current record Appendix E, (F52)–(F55), with its supplied v3 source locator.
- Independently inspected supplied Bansal–Sinha arXiv:2008.07003v3 PDF, §5.4, printed p. 38: the preceding sum has logarithmic exponent (r−1)/2 and the proposed following sum exponent r(1−1/k)/2; their ratio is log(kN)^{(r/k−1)/2}.
- The same supplied page prints delta^2/(4N) in (5.31), while the current record separately explains its uniform-tail calculation. No later-edition claim is made.



## CX053 — keep · keep

**Document:** expert_companion. **Perspective:** certificate_comparisons.

**Locator:** §4.2, implementation of the ideal pivot process; repository/docs/expert_companion.md, line 169.

> The algorithm never computes the weights.

**Finding.** Keep the distinction between analytical weights and physical operations. The coherent preparation samples a label with successful mass w_i/m; bounded amplification preserves the conditional label law while enforcing a worst-case cap even when success probability is tiny or zero. That makes the ideal analysis a usable algorithm.

**Why it matters.** Classical construction experts can follow the tournament calculation yet reasonably wonder how unknown comparison probabilities are accessed. This interface answers the operational question without requiring an oracle for the weights.

**Suggested direction.** Preserve the exact successful-label law, the retained-workspace requirement, and the stopping argument after the winner has been listed. Compress numerical amplification details only after preserving this connection.

**Evidence and scope:**

- Current expert §4.2, Ideal process and implementation paragraphs; exposition §4, Sampling a pivot quantumly.
- Current record §§5.1–5.2, successful-label law and real/ideal coupling.
- OpenAI preprint Proposition 3.2 and §3.2.



## CX054 — keep · keep

**Document:** reasoning_record. **Perspective:** universal_exponent.

**Locator:** Appendix B, opening; repository/docs/reasoning_record.md, line 4207.

> This is a reference catalogue for the argument in §§2–7 and Appendix A.

**Finding.** Keep Appendix B’s explicit reference role, stable 121 claim identifiers, proof destinations and group introductions explaining formal boundaries. The catalogue is useful to a reader who arrives with a particular claim, rather than as consecutive mathematical exposition.

**Why it matters.** A long record should preserve recoverable argument and statement identity. Removing this material to improve a first-pass reading would defeat a different, legitimate use; forcing every reader through it would also misallocate effort.

**Suggested direction.** Retain the reference catalogue and its stable destinations while excluding it from the compulsory continuous route. Preserve the distinction between historical evidence fields and the current observation.

**Evidence and scope:**

- Current record Appendix B opening and groups B.1–B.10.
- Previous-round record dispositions preserve the catalogue’s literal statement/identifier role rather than reformatting it into another narrative.
- This review inspected the catalogue text; it did not rerun its historical formal-source audit.
