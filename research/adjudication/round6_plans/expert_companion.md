# Round six: revision plan for the expert companion

Manuscript: `docs/expert_companion.md` at repository HEAD 9bdd443 (424 lines).
Dispositions: `research/adjudication/round6_dispositions/expert_companion.json` (65 rows, all quotes found at the stated lines of the current file).

Two operator directives arrived during adjudication and override the panels where they conflict:

1. The paper should look like a normal TCS paper, written as its cited papers are. It carries no hashes, toolchains, receipts, shell commands, code blocks or review-status ledgers. The formal check gets a short section in ordinary prose with readable links. Bureaucracy goes to the repository metadata or the long record.
2. Most of the panel feedback was meta. The real work is better mathematical prose. Mathematical-exposition findings (mechanism, predecessor tradeoff, Drucker, classical charge, quantum contracts) outrank evidence-presentation findings. **The main deliverable is the sentence-level line edit in §3 below.**

## 1. Clusters and decisions

| Cluster | Findings | Decision |
|---|---|---|
| C04 Direct-product choice | CX001, SX-038; keep CX039, CX040 | **Fix.** I checked CX001 against Drucker's Theorem 1.1 (arXiv:1005.0644v2). Take T=L, ε=1/3, α=3/r ≤ 3/40, with k=r copies. The total budget is exactly L and the bound is 2(2/3)^r. Drucker says his results also hold for partial functions. The §5.4 simulator has total cap L and independent side information, so the theorem applies. In (14) the guessing term becomes 2Gβ^r ≤ 2/(100m^8), so the 6/100 bound still holds. The current clause "while his headline theorem assumes one global budget" is true, but it reads as though the global theorem cannot be used. Replace it with the sufficiency remark and the real reason for the separate-cap form: it gives β^r exactly, it is the preprint's Lemma 4.1, and its proof takes five lines. |
| C05 Predecessor tradeoff | CX002, CX006, CX015, QX-016, CX031 | **Fix.** ABBLSS (ref-04) store back pointers in the D–Q function, which makes it easy for zero-error randomized algorithms. Their Monte-Carlo-hard variant drops the back pointers and reaches the zeros through a balanced tree. Say this, then say what changes here. A zero carries no pointer. The disqualifying certificate sits behind the winner's hard address, and a comparison reads one ℓ-bit field. In §1.1, state the cheat-sheet conversion once as R=Q^{2+c} with c=1/2, 2/3−o(1) and 1−o(1) (Tal's row checked in ref-26), and limit the scope claim to the AND–OR recipe. Credit Ben-David 2015 (arXiv:1506.08106) in the 5/2 row. |
| C06 Tournament mechanism | QX-005, QX-013, QX-019, QX-021; keep QX-038/039/040, CX053; decline QX-015 | **Fix.** Open §4.2 with AIK's survivor set and how its indicator becomes the product of comparison probabilities. State why a list suffices. Reduce Lemma 2 to its contract plus a two-sentence sketch, and compress the ℓ^6 count. QX-015 is declined: it asks for an explanation of why the BDK/AIK functions do not give R versus Q, which I could not verify (AIK's R₁=Θ(√C) runs the other way). |
| C08 Classical charge | CX010, CX021, CX030, CX032; keep CX035, CX038, CX041, CX045 | **Fix.** Rewrite the §1.2 heuristic around the actual operation: a light run that queries the true cell has named all r answers with at most L address queries. In §5, identify μ as the minimax law, not the planted law of §6. Label the parameter roles in §5.5. Credit the hidden-zero matrix to Ben-David 2015. |
| C07 Quantum contracts at point of use | QX-002, QX-009, QX-014, CX011; keep CX037 | **Fix.** Delete the overstated Lean clause at line 147. Keep "uses only the law of the measured label" and add "measure the label; it becomes the pivot". Add that any bounded-error decoder suffices because (iii) certifies the domain. Add that S enters only through √K. Add that the explicit Walsh form is needed because of (iii). |
| C09 Shortcut table | QX-018, CX023 (partially valid); keep SX-037 | **Keep all eight rows in §3** (three panels value them). Cut the row-7 explanation paragraph; it is already in record CL-conditioning-counterexample. Add one sentence routing rows 1–3 to §4 and rows 4–7 to §5. |
| C10 Growing k | CX017, FX015, SX-039 (cross: QX-003) | **Move the derivation to the record, keep a three-sentence remark.** I rechecked the arithmetic. R>⌊mL/100⌋ with R an integer gives R>mL/100 ≥ mX/200, hence the constant 1 822 500. A numeric sweep over t=80…5000 and up to 10^8 confirms R_lb ≥ Q_ub^{4−ε(ℓ)}. This is a sample check, not a proof. |
| C11 Forrelation supplier | CX012; keep CX046, CX048 | **Fix.** Add one sentence comparing (16) with Bansal–Sinha (better power of k, worse power of the logarithm). Say that (5) suffices for Theorem 1 and that (16) serves the remark. |
| C12 Opening and value | QX-017, SX-036; keep CX033, CX034, CX049, QX-052 | **Fix.** Demote the constants in the abstract. Shorten §1.4 and cite the exposition. |
| C02 Appendix size | QX-027, CX013, FX009, FX010, FX017; keep FX019 | **Fix by replacement.** A ~0.7-page section "The formal statement" replaces Appendix A. |
| C03 Formal semantics kept in prose | FX003, FX005, FX011, SX-040, FX007; keep FX018, FX020 | Keep only the differences that matter mathematically, in prose: existential log exponent and floor form; finite weighted seeds and recursive compliance in Lemma 4; the amplifier's basis-label success tests; nonempty sets defining R and Q (FX005 is a real point, since sInf ∅ = 0 would make an upper bound on Q vacuous). The rest goes to the record. |
| C01 Edition metadata | FX002, QX-006, CX014, SX-041, FX012 | **Fix by removal.** The facts are now verified. The code block says 659b571, the links pin e9dfefb, and the Unconditional receipt records a run at 9a0a5cd. `git diff` shows `lean/` byte-identical from 659b571 to HEAD. The README or record receives this correctly stated, and describes Reach.lean as printing a projection. |
| C13 Bit accounting | keep FX021 | Keep. |

**Counts:** 13 clusters. 36 fix (including 8 fix-by-removal), 22 keep, 6 move to record, 1 decline. No finding was rejected on mathematical grounds. CX001 was the one mathematical claim needing an independent check, and it holds.

## 2. Page budget (14 pages)

| Part | Now | Target | Change |
|---|---:|---:|---|
| Abstract, §1 | 3.05 | 2.8 | History collapses to one conversion sentence. §1.2 classical paragraph is rewritten, about the same length. §1.3 gains two sentences on back pointers and the Walsh form, loses the AIK detail (moved to §4.2). The Lean sentence at line 31 moves out. §1.4 is halved. |
| §2 | 1.1 | 1.15 | Two clauses (decoder choice, S→√K). |
| §3 | 0.7 | 0.5 | Row-7 paragraph cut, rows tightened. |
| §4 | 1.85 | 2.25 | Lemma 2 sketch shrinks (−0.15) and the ℓ^6 paragraph halves (−0.1). The AIK→weights opening, list contract and measured-pivot sentence take more space (+0.65). |
| §5 | 2.35 | 2.6 | Drucker remark, μ identification, address-naming emphasis, Ben-David credit, parameter roles. |
| §6 | 0.4 | 0.4 | Review sentence out, BS comparison in. |
| §7 | 0.4 | 0.4 | Remark shortened. Fixed-k paragraph kept. |
| Formal statement (old App. A) | 2.4 | 0.75 | Replaced. |
| Preparation note, references | 1.8 | 1.85 | +2 bib entries. |
| **Total** | 14.05 | ~12.7 | The surplus is not filled with prose. A shorter paper is acceptable. |

**Page one** must carry: the theorem with (2), the upper bound and its source, the k=3 refutation of the cubic conjecture, the history table, and the start of the mechanism. That is the current order with the constants paragraph shortened, so the table and the conversion sentence land on page one.

## 3. Line edit (main deliverable)

Each entry gives the paragraph's job, what is weak in its sentences and the intended improvement. The benchmark is how ABK, Tal, ABBLSS, AIK and Drucker write: a short motivating sentence, then the claim with its object as subject, "we" for the authors' steps, one idea per sentence, and no announcements of structure. Machine tics in this draft that recur below: sentences that announce their own role ("This section proves…", "The difficulty is…"), lists of three in a row, "exactly"/"genuine" as intensifiers, status words in mathematical sentences, and contrast frames.

**Abstract (l.9).** *Job:* the result, its significance and the mechanism. *Weak:* the sentences are of even length. "The new idea is to give…" puts the mechanism inside a 70-word sentence that does three jobs (construction, classical cost, quantum cost). "genuine winner" is an intensifier. The closing list ("gives…, lists…, and compares…") reads as a contents list, and the constants lead it. *Improve:* split the mechanism into two sentences, construction then the two costs. Drop "genuine". End with one sentence saying the paper gives the complete argument with explicit constants and the failing shortcuts, and that the theorem is formalised in Lean. Do not mention comparison of statements.

**§1 opening, model paragraph (l.14).** *Job:* define R and Q for partial functions. *Weak:* "A query reads one input bit; computation between queries is free" is fine, but the next sentence stacks three conditions ("on every input, every random choice and every measurement branch, including inputs outside the domain"). *Improve:* keep the definitions. Turn the cap sentence into "Query bounds are worst case: they hold on every input, including inputs outside the domain, and on every branch." Introduce the oracle as "Quantum algorithms access x through O_x…".

**Display (1) and the sentence after (l.15–19).** *Job:* define α_tot. *Weak:* "One constant serves every input length and every function; the added one covers constant functions" is two jobs joined by a semicolon. "Throughout, ℓ=log₂m, and m=4^t is a power of four" introduces notation before m is defined. *Improve:* "The constant C_α is uniform in n and f; the term 1 accounts for constant functions, which have Q=0." Move the ℓ, m notation to the start of §1.2, where m first means something.

**Theorem 1 (l.21–26).** *Job:* the headline. *Weak:* "explicitly specified total functions" is a filler adjective. *Improve:* "total functions F_{k,m} (defined in §2)". Keep the display.

**Paragraph after Theorem 1 (l.29).** *Job:* the upper bound, the cubic refutation and why it settles the question. *Weak:* it opens with a typographic convention ("Displays that match… carry its number after the letter P"), the least important thing on the page. "the quartic bound cannot be improved by any power" is a tagline. *Improve:* move the P-number convention to a footnote-like sentence at the end of §1.4. Open with the ABKRT upper bound. End with "Theorem 1 therefore determines the optimal exponent for total functions."

**Constants paragraph (l.31).** *Job:* record the explicit constants and attribution. *Weak:* the reader meets three record links with section numbers in the middle of a sentence, then a Lean sentence with status vocabulary ("compared form", "built but has not been compared"). Two jobs. *Improve:* one sentence for the constants ("Our proofs give b_k=6, c_k=1/400 and the threshold t≥13669k², with the same circuit in both bounds"), with one link to the record. One sentence of credit ("The theorem, the construction and both analyses are OpenAI's"). The Lean content moves to the formal section.

**§1.1 table (l.35–42).** *Job:* the history. *Improve:* add Ben-David to the 5/2 row ("Ben-David; ABK"). No other change.

**§1.1 cheat-sheet paragraph (l.44).** *Job:* why the old route stopped at three. *Weak:* "shows why this route stopped at the cube" is self-announcing and too broad (CX015). The computation runs in two separate cases (5/2, then 3), and 8/3 is only named. The ABK quote is decoration. *Improve:* "In the cheat-sheet construction of [ABK, §3.1], a partial function g… is composed with AND∘OR… If Q(g) is polylogarithmic and R(g)=Ω̃(n^c), taking m'=n gives R=Ω̃(n^{2+c}) against Q=Õ(n). Forrelation has c=1/2; Tal's bound gives c=2/3−o(1); Bansal–Sinha and SSW give c=1−o(1), the cube ABKRT conjectured optimal." Drop the quoted phrase.

**§1.2 first paragraph (l.48).** *Job:* the object. *Weak:* "The function asks whether some all-one column has such a cell" uses a personified function. "which should certify" is vague. *Improve:* introduce m, ℓ, r here. "Column i is a *winner* if X_i is all ones and its selected cell certifies s_i and points to a zero of every other column; F=1 exactly when a winner exists."

**Figure 1 caption (l.50).** Keep. "whatever address that column computes" is good.

**§1.2 classical paragraph (l.52).** *Job:* why R≈mL. *Weak:* this is the paragraph the classical panel flagged. "Reading the cell needs that column's address" asserts a per-run necessity the proof does not use. "this route needs about L queries in a constant fraction of the columns" is vague about why. "both routes fail" anthropomorphises. The display "R≈m·L" arrives before the reason is complete. *Improve:* rewrite as three sentences. (i) The zero-input and planted one-input differ only at the erased zero and the filled cell of a uniformly random column I. (ii) Finding the erased zero is a search for one marked zero among m columns, so it needs about m² queries. (iii) A run with far fewer than mL queries makes more than L queries to the address inputs of only a small fraction of columns. In any other column, a query to the true cell would name all r answers after at most L queries, which happens with probability at most β^r per query by the direct product theorem. Then the display.

**§1.2 quantum sentence and display (l.56–59).** Keep. "Quantumly, each address costs…" is good. Drop the duplicated "≈" chain if the display already shows it.

**§1.2 tournament paragraph (l.61).** *Job:* the quantum difficulty and its solution. *Weak:* "The difficulty is the quantum search" self-announces. "The outward pointers give a cheap substitute" is vague about what is substituted. The last sentence lists three adjectives ("cyclic, unbiased or arbitrary"). *Improve:* "Grover search for a winner would run all K≈m local tests per candidate, at total cost about m. Instead, two columns are compared in polylogarithmically many queries: decode both addresses and follow each column's pointer into the other." Keep the winner-protection sentences. End with "Comparisons between losers can be arbitrary, including cyclic or unbiased, and the tournament of §4.2 needs only the winner's guarantee."

**§1.3 first paragraph (l.65).** *Job:* lineage of addressing and pointers. *Weak:* one long chain of attributions ("descends from…, developed by…, whose functions already…"). The alphabet sentence and the final "these direct pointers are combined with" sentence leave the improvement implicit (CX002, CX006). *Improve:* "Addressing a certificate by the answers of hard partial instances is the cheat-sheet idea [ABK]; here every column has its own array of cells." Second sentence: GPW pointer functions, with ABBLSS. Then add: "ABBLSS's nearly quartic D–Q function stores back pointers to the marked column, which makes it easy for zero-error randomized algorithms; their variant without back pointers is hard for bounded-error algorithms but reaches the zeros through a balanced tree, because one symbol holding all m−1 pointers would make the alphabet exponential." Then: "Here a zero carries no pointer; the certificate that disqualifies the other columns lies behind the winner's hard address, its m−1 pointers are separate ℓ-bit fields, and a comparison reads only the field pointing into its rival." Check the ABBLSS sentence against ref-04 before writing.

**§1.3 Forrelation credit (l.67).** *Job:* credit the partial function. *Improve:* add the clause "The construction needs the explicit form, since it also uses the exact circuit (iii) of §2." Keep the rest (CX046).

**§1.3 comparison-search paragraph (l.69).** *Job:* antecedents of the tournament. *Weak:* five antecedents in two long sentences. "The new ingredient on the quantum side is…" self-announces. *Improve:* group by contract: DH (total order); MPS and BDK (fixed tournament, exact edges); AIK (fixed graph, approximate edges, candidates beating every pivot); HMW (fixed predicate, bounded error). Then one sentence on why none applies: a comparison between two losers can have any probability, including 1/2. Move the AIK-to-weights relation to §4.2.

**§1.4 Plan (l.73).** *Weak:* a sentence per section, the self-announcing pattern the register guide names. *Improve:* two sentences: Sections 2–3 give the construction and the failing shortcuts; Sections 4–7 prove the quantum bound, the randomized bound, the Forrelation input and the exponent, and Section 8 describes the Lean statement. Add "A companion exposition works the construction on a four-column example [Exposition]." End with the P-number convention.

**§2 opening line (l.77).** Delete ("This section defines…").

**§2 parameters, (3)–(4) (l.79–90).** Keep. "a large negative Φ is outside the promise" is good; keep it.

**(i) (l.92–97).** Keep. "Section 6 describes the alternative proof used in Lean" becomes "Section 6 gives a second proof."

**(ii) (l.99).** *Weak:* four short sentences of even rhythm. *Improve:* merge the algorithm description into one sentence. Add the decoder-choice clause (QX-009): "The interference test of [AA] with acceptance probability (1+Φ)/2 would serve as well; only bounded error on the promise is used, because (iii) certifies the domain." Keep "outputs some bit, within the same cap, on every input".

**(iii) (l.101) and l.103.** Keep the content. Fold the one-line paragraph "The exact domain bit matters…" into (iii) as its last sentence.

**Total function paragraph (l.105–110).** *Weak:* the definition sentence is about 90 words. The bit count sentence ends with "the parameter m counts columns, and both bounds concern this one function", a reminder doing a second job. *Improve:* split the column contents (one sentence) from the winning condition (one sentence plus display). Keep the uniqueness argument. End the bit count at "since 2^r=m^{20}".

**Local tests (l.112–116).** *Weak:* "Hence a winner passes all tests at its address, and a non-winning column fails some test at every address" is right but arrives after the cost details. *Improve:* state the dichotomy first, then the count K and the costs, then add the clause (QX-014) "so the circuit size enters the quantum bound only through the √K cost of verification (§4.3)".

**§3 opening and table (l.120–133).** *Weak:* "Each row… is a step a reader may be tempted to simplify" addresses the reader. "Rows 3, 5 and 8 are checked in the table" is ledger language. *Improve:* "Table 1 lists simplifications that fail, each with a counterexample; rows 1–3 concern the quantum algorithm of §4 and rows 4–7 the lower bound of §5." Tighten the row wording. Keep all rows.

**Row-7 paragraph (l.135).** Delete (record CL-conditioning-counterexample).

**§4 opening (l.139–141).** *Weak:* the opening announces four steps as a list. *Improve:* "The new step is a tournament whose comparisons may be biased arbitrarily between losers (§4.2). It needs a form of amplitude amplification with a fixed cap (Lemma 2) and ends with verification of a short list (§4.3)." Then define T and ε.

**Lemma 2 (l.143).** Keep the statement. It is the contract.

**Sketch (l.145).** *Weak:* four citations and a record link in five sentences, all standard. *Improve:* two sentences. The successful component after j iterations is a multiple of |g⟩ [BHMT], so success leaves |g⟩. A random iteration count below 10/√γ succeeds with constant probability [BBHT], and a fixed number of trials gives the cap. Then the record link. Drop the "expected cost" sentence or keep it as one clause.

**Line 147.** Keep "The upper bound uses only the law of the measured label." Delete the Lean sentence (QX-002).

**§4.1 (l.151–156).** *Weak:* "Because both orders use the same circuit" comes after the rule it justifies, which is fine. "The decoded labels stay in orthogonal registers, so these probabilities are the measured probabilities of the coherent circuit" is the point-of-use contract and should precede "Hence a_{i⋆j}≥1−ε". *Improve:* reorder the last three sentences: contract, then winner bound, then cost.

**Proposition 3 (l.160).** Keep.

**New sentences before *Ideal process* (QX-005, QX-013).** "Ambainis, Iraids and Kokainis keep the candidates that beat every pivot so far. Here that indicator becomes the weight w_i=∏_b a_{iρ_b}: each comparison multiplies a candidate's weight by its probability of winning, the total weight halves in expectation, and only the winner is guaranteed to keep weight above 1/2. A list suffices because verifying a listed candidate costs O(√K) queries; its length and cost are bounded on every input, and it contains i⋆ when a winner exists."

**Ideal process (l.162–167).** *Weak:* "No order or transitivity enters, so cycles among losers do no harm" is good. "By (7), pairing the terms…" is good. Keep. The last sentence chains three claims. Split it at "so by Markov's inequality".

**Exact sampling (l.169–174).** *Weak:* "The algorithm never computes the weights" is a strong opener; keep it. The paragraph omits the measurement. *Improve:* after the Lemma 2 sentence add "Measure the returned label; it is the next pivot." Keep display (9) and the mass computation (QX-039, CX053).

**Coupling (l.176).** Keep the substance (QX-040). Split the long middle sentence. Move "Full proof:" to the end as one link.

**§4.3 first paragraph (l.180).** *Weak:* seven sentences that alternate algorithm and error. *Improve:* order it as algorithm (decode, measure, search for a failing test, reject or accept), then soundness and completeness, then the error totals, then the bit-access sentence (FX021 keep).

**§4.3 second paragraph (l.182).** *Improve:* compress to two sentences: the stage and verification costs give O_k(√m ℓ^6), counted loosely in record §5.4, and nothing depends on the exponent.

**§5 opening (l.186).** *Weak:* three jobs (roadmap, hypotheses, minimax) in one paragraph. "the maximum over randomized depth-L algorithms is attained, and it is below 2/3 because L<R(P)" is dense. *Improve:* first a one-sentence roadmap. Then the hypotheses on P and L. Then minimax with the identification (CX021): "this μ is supported on the promise and need not be the planted law of §6".

**Lemma 4 and proof (l.190–196).** Keep. Add to the proof's first line (SX-038) "We work with unnormalised measures so that branches of probability zero need no conditioning."

**Paragraph after Lemma 4 (l.198).** *Weak:* this mixes attribution, a Lean status sentence and a reduction sentence. The Drucker clause misleads (CX001). *Improve:* first sentence: the caps must hold on every branch and the independence must be joint (rows 5, 6). Second: attribution, Shaltiel's fair trees, Drucker's Lemmas 3.1–3.2. Third (new): "Drucker's Theorem 1.1, with total budget L (T=L, ε=1/3, α=3/r), also bounds the simulator of §5.4, by 2β^r; the factor two is absorbed in (14). The separate-cap form gives β^r exactly and has the short proof above." Move the Lean and seed-reduction sentences to the formal section.

**§5.2 (l.202).** *Weak:* "The blank array… follow the cheat-sheet lower bound…; the erased zero is a second channel, and the unknown column I supplies the factor m" makes three claims in one sentence. *Improve:* split them. Credit the erased-zero matrix: "a hidden zero in each column with one of them marked, as in Ben-David's lower bound [BenDavid2015]".

**(10) paragraph (l.206–212).** Keep.

**§5.3 (l.216–228).** *Weak:* the Lean sentence (l.221) interrupts the argument. "count early and late discoveries, as the preprint does" is good. *Improve:* delete the Lean sentence (it goes to the formal section). Keep the counterexample pointer. Keep the refinement sentence as one clause.

**§5.4 (l.232–244).** *Weak:* the decisive operation is in the middle of a long sentence (CX010). *Improve:* open the second paragraph with "The location of a query already names an address: a query to a cell B_{i,s} names s before any of its bits is read." Then describe the simulator. Keep the joint-event paragraph (CX041).

**§5.5 (l.248–258).** *Improve:* after (14) add the parameter-roles sentence (CX030). Keep the averaging argument (CX045). The constants paragraph becomes two sentences.

**§6 (l.262–271).** *Weak:* "This section states the only property… and the stronger form in which Lean proves it" self-announces and is status-laden. *Improve:* "The lower bound uses only (5), the fixed-k, constant-error consequence of Bansal and Sinha's theorem. A different proof gives the uniform bound (16)." Then the comparison sentence (CX012): (16) has a better power of k and a worse power of the logarithm. Keep the proof summary (CX048). Delete the last paragraph (FX017).

**§7 (l.275–281).** Delete the opening announcement. Keep the derivation and the quantifier sentence (CX049, QX-052).

**Remark (l.283).** *Improve:* three sentences. Letting k grow with m needs bounds uniform in k: (16), (15) and Q(F)≤2^{53}k2^{10k}√mℓ^6. With k=⌊√(t/20)⌋ they give R(F_t)≥Q(F_t)^{4−ε(ℓ)}, with ε(ℓ) as stated. This is still no bound R=Ω(Q^4). Link to the new record §7.4. Drop "built in Lean but not compared".

**New §8 "The formal statement" (replaces Appendix A).** Target is about ten sentences, modelled on the exemplar's "Formal scope".
1. Theorem 1 and the cubic refutation are formalised in Lean 4 with Mathlib [repository link]. The statement file imports only Mathlib and contains the definitions of §1–§2; the proofs are compiled separately, and Comparator checks that they prove exactly these statements with the standard axioms.
2. Modelling choices that match §1: worst-case caps on every branch; randomized algorithms as finite mixtures of trees (record §2.2); quantum algorithms with unitaries fixed before the input and access only through O_x, equivalent to a fixed query sequence with deferred measurement (record §2.5); every promised input must reach success at least 2/3.
3. Infima: R and Q are least elements of nonempty sets because reading every bit is admissible (record §§2.2, 2.4). The set defining α_tot is nonempty because the statement also proves the power bound with exponent four.
4. The formal Theorem 1 quantifies as ∀k ∃S,A,b,t₀ ∀t ∃𝒞, with one circuit for both bounds. Its logarithmic exponent is existential and its lower bound is ⌊mL/100⌋<R; the constants 6 and 1/400 are proved in a separate Lean theorem [link].
5. Lean also proves (16) [link], Lemma 4 for finitely many weighted random seeds with caps as a recursive compliance condition (the reduction from general independent randomness and the identification with query counts are ordinary arguments, record §6.1), and the amplification lemma for success tests on basis labels with exact success mass [link].
6. Full statement-by-statement correspondence: record §2.9.

No table, no "compared/built", no review or sandbox sentence, no hashes, no commands.

**Note on preparation (l.362).** Keep the AI-assistance line and credit OpenAI. Do not mention review.

## 4. Ordered edit list

1. Abstract l.9: line edit plus demoted constants (QX-017).
2. §1 l.14–31: line edits. Move the P convention to §1.4. Shrink l.31 to constants and credit, with Lean content to §8 (FX020).
3. §1.1 l.38 Ben-David row (CX031). Rewrite l.44 with the 2+c conversion (QX-016, CX015).
4. §1.2 l.48, l.52 classical rewrite (CX010), l.61.
5. §1.3 l.65 back pointers and selected field (CX002, CX006). l.67 Walsh clause (CX011). l.69 regrouping.
6. §1.4 l.73 shortened, with exposition citation (SX-036).
7. §2 l.77 deleted. l.99 decoder clause (QX-009). l.103 folded. l.105 split. l.116 reordered plus √K clause (QX-014).
8. §3 l.120 rewritten, rows tightened, l.135 deleted (QX-018, CX023).
9. §4 l.139 opening. l.145 sketch to two sentences (QX-019). l.147 Lean sentence deleted (QX-002). l.156 reordered. New sentences after Prop 3 (QX-005, QX-013). l.174 "measure the label". l.176 split. l.180 reordered. l.182 compressed (QX-021).
10. §5 l.186 μ identification (CX021). l.196 normalisation clause (SX-038). l.198 Drucker rewrite (CX001). l.202 split plus Ben-David (CX032). l.221 Lean sentence out. l.234 address-naming first (CX010). l.248 parameter roles (CX030).
11. §6 l.262 rewritten plus comparison (CX012). l.271 deleted (FX017).
12. §7 l.275 announcement out. l.283 remark to three sentences plus record link (CX017).
13. l.285–358 Appendix A replaced by §8 (C02, C03). Reproduction block deleted (C01).
14. Bibliography: add BenDavid2015 (arXiv:1506.08106) and Exposition2026.
15. Regenerate links with `tools/build_lean_links.py` (unused def-* labels drop out). Render with `tools/render_papers.py`. Inspect every page at reading size, and check that no hash or command is visible.

## 5. Coordination

- **Reasoning record:**
  - (a) Add the Drucker sufficiency remark (T=L, ε=1/3, α=3/r → 2β^r, absorbed in (14)) to CL-literature-and-verification and CL-address-guess.
  - (b) Add a new §7.4 with the growing-k derivation moved from the companion remark: X∈[2,m] for 15k+2≤2t and t≥32; L=⌊X⌋; R>mL/100≥mX/200 = m^{2−1/k}/(1 822 500 k² ln 4km); k=⌊√(t/20)⌋ for t≥80; ε(ℓ). Replace §7.2's "a separate result" with a link to it.
  - (c) §2.9 receives Table 2 and the object map. Correct the amplifier relation to "uniform in 𝒜, exact success mass, basis-label success tests" (SX-040). Mark per bundle whether definitions are Mathlib-only or imported (FX009).
  - (d) Repository README or record Appendix F receives the reproduction metadata, stated correctly: links pinned at e9dfefb; Unconditional Comparator run at 9a0a5cd in paranoid, unsandboxed mode; `lean/` identical from 659b571 to HEAD; Reach.lean prints a projection of the closure.
- **Exposition:** cite the companion reciprocally if its owner wishes. The CX007/SX-004 heuristic corrections should match the new §1.2 classical wording.
- **Statement fidelity recheck required** for every sentence of the new §8 against `lean/QuarticCorpus/Unconditional/Challenge.lean` (lines 311–340), `QuarticQuery/Paper/ConstructionFamily.lean#L28-L40`, `ForrelationLower/Uniform.lean#L525-L532`, `LowerBound/RealizedCaps.lean` (actualComplies l.52, actualCount l.104, compliantSuccess) and `Independent/UniformAmplifier/Challenge.lean`. Pay particular attention to the quantifier sentence, the floor form and the "only Mathlib" claim.
- **Literature to recheck while writing:** the ABBLSS variant sentence (ref-04 §1 and the function list at l.283–289), and the Ben-David 2015 bibliographic data.
