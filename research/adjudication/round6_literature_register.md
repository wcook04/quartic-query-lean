# Round 6: how the cited query-complexity literature writes, and where our three manuscripts differ

Scope: register only. No mathematics, claims or citations are judged here. All quoted specimens are at most 25 words and are moves to imitate, never text to copy. Source directories are under `scratchpad/r6packet/literature/` (shortened to the `quartic-ref-NN` or `quartic-lit-name` prefix) and `scratchpad/r6packet/paper/` for the OpenAI preprint. Locators in the literature are approximate (section or extracted-line number); locators in our manuscripts are line numbers in `docs/`.

Extraction caveat. Several literature files are raw PDF text: ligatures drop letters (the Buhrman and de Wolf survey loses every "c" before "t", "o" and "e"), display mathematics is lost, and in markdown files mathematics appears as `MATH`. Specimens from the survey are quoted with the letters restored. Sentence-length and parenthesis features are noisier on the PDF-derived files than on the markdown ones.

## (A) Reference set and what was read

Read in full or in the relevant sections (introduction, technique or overview section, one proof section, roadmap and closing material):

| Source | Role in the set | What was read |
|---|---|---|
| `paper` (OpenAI preprint, Oct 2026) | the genre target: a short, total-function separation | whole text: abstract, §1 to §1.3, §2 to §5, Appendix A heads |
| `quartic-ref-01` Aaronson and Ambainis, Forrelation | separation paper with conjecture and open questions | abstract, §1, open-question passages |
| `quartic-ref-02` Aaronson, Ben-David, Kothari, cheat sheets | the closest precursor for the cheat-sheet half; best "intuition then implementation" model | §1 results, overview of techniques, §3.1 intuition, §3.2 implementation, §6 proofs, acknowledgements |
| `quartic-ref-03` Aaronson, Ben-David, Kothari, Rao, Tal (degree vs approximate degree, Huang) | upper-bound side, open-problems section | first pages, roadmap |
| `quartic-ref-06` Bansal and Sinha, k-Forrelation | the partial-function ingredient; overview and techniques model | §1 to Organization, parts of the proof |
| `quartic-ref-23` Sherstov, Storozhenko, Wu | independent partial-function proof; related-work and "limitations of previous analyses" model | §1 (all subsections), start of §2 |
| `quartic-ref-26` Tal, Rorrelation | techniques section, related work, open questions | abstract, §1, §1.1, §1.3, §8 |
| `quartic-ref-13` Drucker, direct product | the direct-product ingredient; proof narration and credit | §1, "Our methods", proof of Theorem 1, "Questions for future work" |
| `quartic-lit-ambainis-iraids-kokainis` (and the duplicate in `quartic-ref-05`) | 2026 comparison-based separation, nearest in date and idea | introduction, credit sentences, end matter |
| `quartic-lit-zhang-shao-cyclic-forrelation` | 2026 paper, end matter only | AI disclosure |
| `quartic-lit-hoyer-lee-spalek-negative-weights` | how computation is reported | the passage reporting an SDP search |
| `quartic-lit-buhrman-dewolf-decision-tree-survey` | survey register | §1, §3.3, §4.2 |
| `quartic-lit-dewolf-quantum-computing-lecture-notes` | lecture-note register | preface, ch. 1, the quantum-walk chapter |

Measured only (no close reading): `quartic-ref-04`, `quartic-lit-aaronson-ambainis-bogdanov`. For the expository profile: `quartic-lit-aaronson-quantum-implications-of-huangs-sensitivity`, `quartic-lit-ben-david-a-super-grover-separation`, `quartic-lit-hoyer-mosca-dewolf`, `quartic-lit-montanaro`, `quartic-ref-10`, `quartic-ref-12`.

The remaining sources (about 25) were not read.

## (B) Moves table (research-paper genre)

The first column follows the checklist in `register-from-literature.md` step 2, plus the query-complexity items requested.

| Move | How these papers do it | Specimen (source, location) |
|---|---|---|
| First sentence of abstract | A direct statement of what is constructed or achieved, with the quantity in plain words. No history, no framing of the paper. | "We construct total Boolean functions with a nearly quartic separation between bounded-error randomized and quantum query complexity." (`paper`, abstract) ; "We achieve essentially the largest possible separation between quantum and classical query complexities." (ref-01, abstract) |
| Rest of abstract | Two to five more sentences: the exact bounds, then one sentence of consequence ("Thus ..."). Tal and Bansal-Sinha list what is proved as numbered items or one displayed bound. | "Thus the known quartic upper bound has the optimal exponent, disproving the conjectured cubic bound." (`paper`, abstract) |
| First sentence of introduction | A question or a one-clause statement of why the field cares. It never mentions the paper itself. | "How much can a quantum algorithm reduce the number of input bits needed to compute a total Boolean function?" (`paper`, §1); "Last year, Huang resolved a major open problem in the analysis of Boolean functions" (ref-03, §1) |
| Introduction opening paragraph content | Defines the two measures in two sentences, then the oracle in one displayed line, then "Computation between queries is unrestricted." | `paper` §1 first paragraph; ref-02 §1 second paragraph |
| Theorem 1 phrasing | Headline plus qualifier in one theorem: "The optimal power is α_tot = 4. More precisely, ..." with quantified constants. In earlier papers: "There exists a total function f such that R(f) = Ω̃(Q(f)^2.5)." Tilde notation for hidden polylogs; "o(1)" in the exponent; "explicit" flagged in corollaries. | `paper` Thm 1.1; ref-02 Thm 1; ref-06 Cor. 4 "There exists an explicit total boolean function f for which R(f) ≥ Q(f)^{3−o(1)}." |
| Where the main result is announced | Page one for the preprint (before the history). In longer papers, after one to two pages of background, under a heading "Our results" or "Results". | `paper` p. 1; ref-02 §1.1 "Results"; ref-06 "Our Results" |
| Novelty sentence after the theorem | Two short sentences: what was known, what is contributed. | "The universal upper bound is known. The contribution is the family in (2), which rules out every smaller power." (`paper`, after Thm 1.1) |
| Introducing prior work | Chronological, author names plus bracket key, one sentence per result stating what was proved, then a relation sentence. Names are given in full for up to six authors in running text. | "Pointer constructions introduced by Göös, Pitassi, and Watson [15] and developed by Ambainis, Balodis, Belovs, Lee, Santha, and Smotrovs [4] gave a nearly quartic separation" (`paper`, §1.1) |
| Crediting predecessors | Verbs of dependence in the main clause: "builds on", "built upon", "inspired by". The relation to concurrent work is a separate paragraph headed "Independent work", and states plainly that techniques are incomparable. | "Our construction builds on the work of Pabbaraju, who constructed a family of total Boolean functions" (ambainis-iraids-kokainis, §1); "Their result uses completely different techniques and is incomparable with ours." (ref-23, "Independent work by Bansal and Sinha") |
| Relation to near neighbours that differ | One concessive sentence that names the difference and the relevance. | "Their nearly quartic separations between certificate and quantum complexity concern a different classical measure, but their comparison-based viewpoint is particularly relevant here." (`paper`, §1.1) |
| Cheat sheets and pointers | Described in the order: what the quantum algorithm can compute that a classical algorithm cannot (the value of f), then "so we hide the certificate at the address given by those values", with the array size stated as a power of n. The questions are asked in prose and answered at once. | "What we would like is to hide the certificate somewhere in the input where only the quantum algorithm can find it." (ref-02, §3.1); "But what information do we have that is known only to the quantum algorithm? The value of f on the input!" (ref-02, overview) |
| Technique statement before proof | A section named "Overview of techniques", "Our Approach", "The construction and its two analyses" or "Our methods". It narrates the classical half and the quantum half in prose with no theorem numbers, and says what is simplified. | `paper` §1.2; ref-06 "Overview and Techniques", "Our Approach"; ref-13 "Our methods" |
| Simplifying in the overview | Declares the simplification and moves on. | "For the sake of simplicity, we ignore this complication altogether in the remainder of this discussion." (ref-23, "The partition") |
| Previous-approach and limitation passage | Names the earlier method, says concretely where it fails, one failure per paragraph. | "Previous approaches and their limitations." (ref-06 heading); "Limitations of previous analyses" (ref-23 heading) |
| Roadmap | One paragraph at the end of the introduction, one clause per section, sections cited by number. No bullets, no "this paper is organised as follows" repetition inside sections. | "Section 2 defines the function and its certificates. Sections 3 and 4 prove the two bounds in (2); Section 5 derives the optimal power." (`paper`, end of §1.2) |
| Section openings in the body | One of four moves: restate the claim being proved; "We now ..." plus the first step; "Recall ..."; or a one-line reminder of what the section is for, only when the section is long. | "In this section we prove Theorem 1, restated for convenience:" (ref-02, §3.2); "We start by showing that the usual algorithmic models can compute f_CS in roughly the number of queries they require" (ref-02, §6) |
| Proof narration | The first sentence of a proof says what object is analysed or what is fixed, not that a proof begins. "Fix ...", "Suppose, for contradiction, ...", "We analyze X and then implement Y". Interjections are rare. | "We analyze an ideal sampling process and then implement each of its steps quantumly." (`paper`, proof of Prop. 3.2); "To prove the claim, suppose for contradiction's sake that no such strategy for player 2 exists." (ref-13, §7) |
| Proof section of the preprint | Opens with a two-sentence plan, then subsection heads naming the step. | "We compare a distribution with one zero in every column to a coupled distribution in which one uniformly chosen column is made a winner." (`paper`, §4) |
| Notation | Mostly inline: "Let", "Fix", "Write". One short "Conventions" paragraph for logarithm base and constants. | "We write [m] = {1, ..., m} and use logarithms to base two, except in expressions where changing the base only changes an absolute constant." (`paper`, §1.3) |
| Section titles | Noun phrases naming the object: "An addressed certificate with outward pointers", "The tournament", "The optimal power", "Preliminaries", "Implementation", "Intuition". Appendix titles name the result: "The universal quartic bound". No question headings. Run-in headings (bold or italic) name an object, as in "Quantum Query Complexity of the k-fold Rorrelation Problem." | `paper` section list; ref-26 §1.1 |
| Limitations and open problems | Stated at the place they arise in one sentence, in the first person plural, plus a closing "Open questions" or "Questions for future work" section of three to six numbered or prose questions. | "Despite considerable efforts, we were not able to find a way forward within this framework." (ref-23, "Limitations of previous analyses"); "We would like to highlight several open questions that were mentioned throughout the manuscript." (ref-26, §8) |
| Hedging | Rare and located: one sentence of the form "there may still be room for improvement". No hedge after each claim. | "although there may still be room for improvement in some of our bounds" (ref-13, "Our results") |
| Reporting computation | A sentence in the introduction and a pointer to code or appendix. Concrete numbers, the tool named, the count of cases. | "we implemented both adversary bounds as semidefinite programs and used the convex optimization package SeDuMi for Matlab." (hoyer-lee-spalek, §1) |
| Reporting AI assistance (2026 papers) | One paragraph at the end of the paper, after acknowledgements, headed "Use of LLM tools" or "AI disclosure": what the tools did, then one sentence that the authors verified everything and take responsibility. It is not in the front matter. | "We reviewed, corrected, and independently verified all LLM-generated output and take full responsibility for the final manuscript" (ambainis-iraids-kokainis, end); "All mathematical statements and proofs were verified by the authors, who take full responsibility for the content of the paper." (zhang-shao, end) |
| Acknowledging errors | Plain. | "We thank Hardik Bansal for spotting an error in an earlier version of the proof of Theorem 1." (ref-02, acknowledgements) |
| Use of "we" | About 18 per 1000 words (corpus median). "We" is the author-reader pair for steps, and the authors for contributions: "we show", "we prove", "we ignore", "we hide". Credit for others' results uses names, never "we". | "Nevertheless, we show that the dependence on N is correct in the case q = 1." (aaronson-ambainis-bogdanov, §1) |
| Sentence length and variety | Median mean length about 20 tokens, 19% of sentences under ten tokens and 17% over thirty, with a spread of about 12 tokens. Exclamation and rhetorical questions occur once or twice per paper. | `profile_v2.json`; "Unfortunately, with elementary families defined as above, such a partition does not exist!" (ref-23, "The partition") |
| Parentheses and asides | About 8 parentheticals per 1000 words, used for scope remarks and cross-references. | "(Note that Simon's problem also provides a similar separation up to log factors.)" (ref-02, §3.1) |
| Small connectives | "Note that" about 0.7 per 1000 words; "Indeed", "Hence", "Thus", "Then" open about 13% of sentences. | "Note that for an even k = O(1) and an advantage η = δ/16, the above lower bound is ... and it matches the upper bound" (ref-06, Our Results) |
| Citation style | Numeric (preprint, ref-26) or alpha keys ([ABK16], [RT19], [AA14]) in the others, with a location when a specific result is used. | "They conjectured that randomized complexity satisfies the stronger relation R(f) = O(Q(f)^3) [3, Conjecture 2]." (`paper`, §1.1) |
| Closing paragraph | A conclusion paragraph is not the norm. The preprint ends its main text with a single three-sentence summary of the mechanism. Other papers end with open questions, then acknowledgements. | `paper` end of §5 |
| What the field's papers do not have | No evidence-status sentence after each theorem, no tables of "same, more or less" statements, no overview boxes, no per-section "This section proves ...", no bold labels in running prose, no reading guide that tells readers which parts to skip. | absence across all read sources |

### Query-complexity-specific points in one line each

- Separations are stated as exponents of the weaker measure: "R(f) = Ω̃(Q(f)^{2.5})", "Q(f) ≥ deg~(f)^{4−o(1)}" (ref-02 Thm 1, Thm 3). The preprint writes the explicit bounds in a displayed line with named constants ck, Ck, bk and then says what they depend on in the same paragraph.
- "Total function" is a word the introduction defines or contrasts with "partial function" in one sentence, with the domain stated: "partial function (a function defined only on a subset of {0,1}^n)" (ref-02, §1.1).
- Lower-bound methods are discussed by naming the method, who introduced it, what it is known to prove, and one place where it fails: "Approximate degree has proved to be a fruitful lower bound technique ... where the original quantum adversary method cannot show nontrivial lower bounds." (ref-02, §1.2, condensed).
- Optimality of a result is placed right after the theorem: "optimal assuming the conjecture that D(f) = O(bs(f)^2)" (ref-02, after Thm 3), "so if true, the above separation is optimal up to o(1) factors" (ref-06, after Cor. 4).
- The tight upper bound is credited by name and location, once, near the theorem, not in every section.

## (C) Expository register (survey, lecture notes and similar sources)

Sources: Buhrman and de Wolf survey; de Wolf lecture notes; and as a measured group Aaronson on Huang's theorem, Ben-David's super-Grover note, Høyer-Mosca-de Wolf, Montanaro, ref-10 and ref-12.

What the expository sources do:

1. They speak to the reader in the first person plural and imperative: "Let us restrict attention to d-regular graphs", "We'll call a basis state good if x is a marked vertex" (de Wolf, quantum-walk chapter). They use contractions in lecture notes ("We'll").
2. They state the goal of a passage before doing it, informally, then do it: "Let us sketch the main idea for how to implement the reflection through |U⟩ up to small error." (de Wolf).
3. They use a problem box for definitions: "Consider the following problem: Input: ... Goal: ..." (de Wolf, collision and triangle problems).
4. Examples are numbered plainly and follow the statement they illustrate: "The biggest gap known between s(f) and bs(f) is quadratic and was exhibited by Rubinstein [37]: Example 1 ..." (Buhrman and de Wolf, §4.2).
5. They admit awkwardness and give motivation in a conversational clause: "This may seem like a stupid algorithm, but it has certain advantages." and "It may look contrived at first, but eventually will lead smoothly to Shor's and Grover's algorithm." (de Wolf, ch. 1 and walk chapter).
6. They signal difficulty plainly: "Getting a good upper bound for the checking cost C requires some more work, namely Grover search plus another quantum walk!" (de Wolf).
7. They use "Note that", "Clearly" and "It is not hard to see that" for routine steps: "Clearly, for all x we have s_x(f) ≤ bs_x(f) and bs_x(f) ≤ C_x(f)" (Buhrman and de Wolf, §4.2).
8. They cite as "referring to [30] for more details" and keep prerequisite material short: "We briefly sketch the framework of quantum computing, referring to [30] for more details." (Buhrman and de Wolf, §3.3).
9. Lecture notes carry practice material: exercises per chapter, hints in an appendix, and a dated change log ("Updated and corrected a few things") in the preface. A short preface says how the chapters were assembled and who contributed.
10. Pedagogical structure is a sequence of named objects, with the proof of each result immediately after its statement. There are no reading guides: the preface lists chapter dependencies in two sentences.
11. Bold is rare. Headings are noun phrases ("Quantum walks", "Applications", "Grover search", "Finding collisions").

Measured against an expository profile (8 documents: the six above plus Buhrman and de Wolf and the lecture notes), `exposition.md` is outside the range on: status vocabulary (+12.6 IQR), `we` rate (-2.0), meta-narration (+1.8), "note that" (-1.4), and sentences opening with Let/Suppose/Fix/Consider (-1.2). The file `scratchpad/register/profile_expository.json` holds that profile.

## (D) Measured distance per manuscript

Tool: `tools/meta/dissemination/mathematician_outreach_typeb/paper_register.py` (subcommands: `profile`, `compare`, `specimens`, `features`, `dump`, `list-features`). It reads markdown directly (`format: md`), counts prose only, and treats mathematics as one token. No conversion was needed.

Profile used: `scratchpad/register/profile_v2.json`, 11 documents: ref-01, ref-02, ref-03, ref-04, ref-06, ref-13, ref-23, ref-26, the OpenAI preprint, aaronson-ambainis-bogdanov, ambainis-iraids-kokainis. A first profile of 10 documents (`profile.json`, with `arxiv-2103-11604` in place of the preprint and ambainis-iraids-kokainis) gives the same ranking; both are in `scratchpad/register/`. Distances d are in corpus IQR units; a leave-one-out noise estimate is attached. The `*` mark means the corpus IQR was below the tool's floor.

Corpus medians [IQR] and ours (expert companion, exposition, record):

| Feature (per 1000 words unless stated) | Corpus median [IQR] | Companion | Exposition | Record | d (companion / exposition / record) |
|---|---|---|---|---|---|
| status vocabulary (Lean, Comparator, receipt, checked, record, ...) | 0.49 [0.30, 1.00] | 14.1 | 8.8 | 8.6 | +19.3 / +11.8 / +11.5 |
| rule-of-three lists | 0.59 [0.43, 0.80] | 3.40 | 1.25 | 2.33 | +7.6 / +1.8 / +4.7 |
| negations (not, no, never, without, ...) | 4.32 [3.25, 5.20] | 7.7 | 9.1 | 11.0 | +1.7 / +2.5 / +3.4 |
| "we" | 17.9 [10.8, 21.0] | 0.0 | 0.4 | 1.6 | -1.8 / -1.7 / -1.6 |
| intensifiers | 1.02 [0.89, 1.70] | 2.95 | 2.33 | 2.36 | +2.4 / +1.6 / +1.7 |
| share of sentences opening with a connective | 0.13 [0.094, 0.15] | 0.028 | 0.037 | 0.043 | -1.8 / -1.6 / -1.5 |
| "note that" | 0.67 [0.25, 1.02] | 0 | 0 | 0 | -0.9 each |
| sentences opening Let/Suppose/Fix | 0.069 (v1) | 0.044 | 0.040 | 0.021 | -0.7 / -0.8 / -1.4 (v1) |
| meta-narration ("Here is", "The key", "This section ...") | 0.20 [0.05, 0.74] | 1.13 | 1.25 | 0.61 | +1.4 / +1.5 / +0.6 |
| contrast framing ("rather than", "not X but Y") | 0.29 [0.16, 0.58] | 0.00 | 0.18 | 1.15 | -0.3 / -0.2 / +1.6 (v1: +1.62 for the record) |
| parentheticals | 8.2 [3.7, 10.3] | 5.9 | 6.4 | 2.1 | -0.5 / -0.4 / -2.3 (v1) |
| semicolons | 3.45 [0.46, 7.58] | 10.9 | 8.8 | 7.7 | +1.0 / +0.8 / +0.6 |
| mean sentence length (tokens) | 19.8 [17.2, 25.1] | 20.2 | 19.4 | 14.9 | -0.05 / -0.2 / -0.8 (v1) |
| share of sentences under 10 tokens | 0.19 [0.16, 0.21] | 0.20 | 0.20 | 0.30 | 0 / 0 / +1.6 (v1) |
| share of sentences over 30 tokens | 0.17 [0.10, 0.19] | 0.17 | 0.17 | 0.053 | 0 / 0 / -1.7 (v1) |
| paragraph length variation (CV) | 0.87 (v1) [0.80, 0.94] | 0.59 | 0.60 | about 0.85 (v1 d -0.2) | -2.0 / -1.9 / -0.2 (v1) |
| mean paragraph length (tokens) | 53.6 (v1) [40.6, 63.1] | 73.7 | 92.0 | 48.1 | +0.9 / +1.7 / -0.3 (v1) |

Reading the table:

- Features beyond the corpus range on all three manuscripts: status vocabulary, triads, negations, "we" absent, intensifiers, connective openers absent. These are the tool's strongest "look here" signals.
- Status vocabulary is a topic effect in part: our papers are about a Lean check, and the corpus has no formal check. The remedy is relocation, since 14 per 1000 words in the companion's body is 28 times the median; the corpus IQR tops out at 1.0.
- Sentence length in the companion and exposition sits at the corpus median (20.2 and 19.4 against 19.8), so "even sentence length" is not their problem. The measure that does differ is the paragraph shape: the companion and exposition have far less variation in paragraph length than the corpus and long average paragraphs (exposition 92 against a median of 54).
- The record is different: its sentences are short and choppy (30% under ten tokens, 5% over thirty), contrast framing is 4 times the median, and it has few parentheticals.
- No manuscript contains an em dash or a question heading, and none use AI-lexicon words. Word bans have already been satisfied; the remaining distance is structure.

Top contributing sentences the tool quotes, per manuscript and feature (shortened to the opening words):

Companion, status vocabulary:
- L325 "The recorded run on the current sources used Comparator's paranoid mode, which also rechecks with the external kernels bundled with Lean."
- L73 "Appendix A is a reading guide to the Lean statement of Theorem 1 and says, for each linked Lean result, whether it states the same as the paper, more, or less."
- L31 "In the Lean formalisation the compared form of Theorem 1 has an existential logarithmic exponent and the lower bound ... for the same circuit".

Companion, triads:
- L14 "The query cap holds on every input, every random choice and every measurement branch, including inputs outside the domain."
- L61 "Comparisons between losers can be cyclic, unbiased or arbitrary, and a tournament with fractional weights tolerates exactly this (§4.2)."
- L65 "The winning condition descends from the pointer functions of Göös, Pitassi and Watson ... developed by Ambainis, Balodis, Belovs, Lee, Santha and Smotrovs".

Exposition, status vocabulary and negation:
- L267 "An independent checker, Comparator, compiles the statement file and the proof separately ... and confirms that the proof establishes exactly these four statements".
- L51 "Full proofs of every step are in the long reasoning record; a reference such as 'record §6.5' below links to the passage in that section."
- L148 "No ordering of the columns is consistent with the comparisons, so the search cannot sort them."
- L167 "No transitivity and no margin away from 1/2 is used."
- L269 "The separation needs neither: its query bound uses only the law of the measured label, a partial form of amplification that fixes the label law and not the state"

Record, status vocabulary, triads, negation:
- L487 "The receipt of 3 November 2026 records acceptance of the four configured targets on the integrated round-four sources"
- L469 "Four kinds of evidence are kept apart throughout this record: an ordinary proof, a successful Lean build with its axiom audit, a Comparator comparison of a configured statement, and review of whether a formal definition models the intended mathematics."
- L4209 "The record retains every candidate tie, full available source types, ordinary premises, additional assumptions, mathematical-fidelity judgments, source hashes, and separate build, Comparator and dependency-reach evidence."
- L516 "It does not establish that those definitions model the paper; §§2.7-2.8 and the finite controls address that question, and no human review of the definitions or proofs is claimed."
- L3540 "No supplied Lean declaration proves this refinement, and Proposition 4.2 needs neither it nor an optimality assertion."

## (E) Tic inventory per manuscript

Counts are from `grep` over the file; line numbers are those of `docs/` at the time of reading.

### E1. `expert_companion.md` (14-page expert paper)

1. Self-announcing structure.
   - Headings L12 "## 1. The result and what is new", L46 "### 1.2 The key mechanism", L63 "### 1.3 What is new", L118 "## 3. Where a natural shortcut fails".
   - Every section opens with a statement of purpose: L77 "This section defines the partial function P and the total function F_{k,m}", L139 "This section proves the upper bound in (2) with a fixed-cap amplifier", L262, L275 "This section turns (2) into α_tot=4 and records the order of quantifiers."
   - L61 "The difficulty is the quantum search:".
   - L71 to L73 §1.4 "Plan" as a separate heading with a paragraph that begins each clause "Section N proves".
2. Repeated attribution sentence: L31 "The theorem, the construction and both of its analyses are OpenAI's." Also every display carries a preprint tag (`\textsf{P2}`, `P3`, `P8`, `P17`, `P21` ...) and L27 explains them: "Displays that match a display of the preprint carry its number after the letter P."
3. Repeated evidence-status sentences.
   - L31 "...the explicit constants ... are proved by a separate theorem that is built but has not ..."; L271 "No person has yet reviewed this Lean proof."; L325 recorded Comparator run; L349 "What it does not establish." (a bold label); Appendix A L285 to L360 with a same, more or less table.
   - Only four lines mention a receipt or recorded run, but 14.1 status words per 1000 words arise because the Lean vocabulary appears in the body prose and the abstract (L9 "compares the statements of a Lean formalisation with the paper's").
4. Intensifiers and exactness words: "exactly" 13 times, including L9 "is exactly four" (abstract), L110 "F_{k,m}=1 exactly when some column wins", L176 "exactly the ideal law", L216, L294 "the oracle is exactly O_x"; "genuine" twice (abstract and L61, "a genuine winner beats every rival"); "precisely", "explicitly" (L21 "explicitly specified total functions"), "directly" once each.
5. Contrast and negation chains (7.7 per 1000 words, 1.7 IQR above): L110 "no promise is imposed on the address inputs, pointers or transcripts"; L61 "nothing can point to a zero in X_{i*}"; L69 "does not apply directly either: it needs every comparison to compute a fixed predicate". Few explicit "not X but Y" patterns (the tool counts contrast at 0.00).
6. Rule-of-three lists: 3.4 per 1000 words, the largest gap of any non-status feature (+7.6 IQR). Locators: L14, L61, L65, L69; also the abstract ("an optimal partial separation ... and independently ...").
7. Flat asyndeton: connective openers 2.8% of sentences against 13%. Paragraphs are uniform in length (CV 0.59 against 0.87).
8. Semicolon density 10.9 per 1000 words (corpus 3.45).
9. Repository links in running prose: L31 and many others embed `https://github.com/.../reasoning_record.md#...` in the sentence, e.g. "[§5.4](https://github.com/wcook04/quartic-query-lean/blob/e9dfefbf...)". The reference papers cite results as [3, Conjecture 2], never by URL in prose.
10. Question headings: none. Em dashes: none. Bold-run-in labels: L349 "**What it does not establish.**", "**The total function.**" (L~104), "**Local tests**".

### E2. `exposition.md` (14-page examples-first exposition)

1. Self-announcing structure.
   - L26 "**Who this is for, and where it goes.**" (a paragraph of purpose and payoffs, including "Three payoffs mark the route:").
   - L28 "**The reason for four, in one line.**"; L36 "**Where this sits.**"; a table of examples (L44 to L49) with the heading column "What it shows".
   - L55 "This section fixes the partial function at the smallest size"; L80, L118, L193, L249 are each "This section builds/states/proves/combines ...".
   - Bold run-in leads at L140 "**Comparing two columns.**", L230 "**Why the event must be joint.**".
   - Nine hits of "Here is/are/the" (e.g. L74 "Here $Hg/2=...$").
2. Cross-reference to the other manuscript after nearly every step, which makes the exposition read as a pointer layer: L51 "a reference such as 'record §6.5' below links to the passage"; L132 "(record §§3.6-3.15)"; L185 "(record §5.4)".
3. Status passage: L263 to L269, "# 7. What the Lean development checks" with L267 "An independent checker, Comparator, compiles the statement file and the proof separately ... and confirms that the proof establishes exactly these four statements". This is a whole chapter whereas the corpus has a sentence.
4. Intensifiers: "exactly" 13 times (L177 "exactly the ideal pivot law", L257 "k=2 gives exactly the cube and does not.", L114 "All tests pass exactly when (i,s) wins", L122 "exactly as before").
5. Negation 9.1 per 1000 words; "not X" statements, e.g. L148 "No ordering of the columns is consistent", L167 "No transitivity and no margin away from 1/2 is used." L181 "The cap does not depend on knowing m, which matters because ...".
6. Paragraph shape: mean 92 tokens (corpus 54) and uniform (CV 0.60). Almost no "Let us", "Suppose", "Note that"; no "we" (0.36 per 1000 words) in a text that is meant to teach.
7. Examples labelled by a table rather than by "Example 1" in the flow; no exercises, no "It is not hard to see".
8. Em dashes none; question headings none; the chapter titles "# 1. Three eight-bit inputs", "# 2. One column, then four" are noun phrases and fit the expository register.

### E3. `reasoning_record.md` (125-page long record)

1. Sentence rhythm unlike the corpus: mean 14.9 tokens, 30% under ten tokens, 5% over thirty. Stacks of short declaratives: L3 "AI agents produced the local Lean formalization, explanatory additions and this manuscript. OpenAI authored the separation theorem and source preprint; ... No human mathematical review or publication acceptance is claimed."
2. Self-announcing structure at scale. Front matter L6 to L15: "Reading guide" with four bold-labelled paragraphs "**The result.**", "**The mechanism.**", "**What is new.**", "**Who each part is for.**", then a table. Twelve section openers "This section ..." (L27, L140, L520, L1734, L2107, L2812, L3800). Seventy-eight "Here is/are". "The record follows these dependencies:" L113; "Dependencies and proof recovery" (bold label).
3. Evidence-status vocabulary repeated by design: "Formal correspondence" subsections at §4.8, §5.5, §6.7 (L3769), §7.3 (L3895), each a paragraph of Lean declaration names with sentences such as "Thus even a complete conjunction theorem for (19) does not formalize the early/late proof" and "A matching build, an axiom audit, a Comparator result, review of the intended statement and human review are different kinds of evidence." (L3794). L469 "Four kinds of evidence are kept apart throughout this record". Twenty-nine hits of "receipt" or "recorded run". The tool places status vocabulary at 8.6 per 1000 words (+11.5 IQR).
4. Contrast framing: 1.15 per 1000 words (the only manuscript beyond the corpus here). Locators: L381 "**An off-promise input is not a false input.**" (a bold not-X label); L1722 "It supplies an eventual threshold rather than the explicit ..."; "They do not acquire formal status from a nearby endpoint theorem." (L3794); "The finite model examples below explain the conventions used throughout; they are not small instances of the separation construction." (L113); "its earlier uncompiled status does not describe a later maintained declaration" (L3777).
5. Negation 11.0 per 1000 words (+3.4 IQR). L516 and L3540 above; L88 "It does not produce an exact fourth-power separation for that fixed m, and these fixed-m total-family bounds do not supply the joint uniform control".
6. Rule-of-three lists 2.3 per 1000 words: L4209 (a seven-item list), L3: "explanatory additions and this manuscript".
7. Intensifiers: "exactly" 67, "precisely" 10, "explicitly" 16, "directly" 10, "genuine" 4, "merely" 7.
8. Scaffolding comments in the prose: `<!-- passage:... -->`, `<a id="...">`, `<!-- claim:eq-10 -->`. These are not visible in a rendered PDF but they dominate the source and signal machine assembly to a reader of the markdown.
9. Few parentheticals (2.1 per 1000 words against 8.2) and few connective openers (4.3%).
10. AI attribution on page one (L3 "AI assistance and attribution"). The 2026 papers in the set put such a statement at the end.
11. No question headings; no em dashes.

## (F) Style rules for the revisers

Each rule names its specimens. "Corpus" means the 11-document profile in (D). Rules 1 to 15, 23 and 24 and 25 apply to all three manuscripts unless stated; 16 to 18 are record-specific; 19 to 22 are exposition-specific.

1. **Open the abstract with the construction and the exponent in plain words.** One sentence says what is built and what it separates; one sentence says the consequence; then one clause on the technique. Keep history out of the abstract. Specimens: "We construct total Boolean functions with a nearly quartic separation between bounded-error randomized and quantum query complexity." (`paper`, abstract); "Thus the known quartic upper bound has the optimal exponent, disproving the conjectured cubic bound." (`paper`, abstract).

2. **Start the introduction with a field question, then define R, Q and the oracle in four sentences.** Do not describe the manuscript's role in the first paragraph. Specimen: "How much can a quantum algorithm reduce the number of input bits needed to compute a total Boolean function?" (`paper`, §1). Replace the "The result and what is new" heading with "Introduction".

3. **State Theorem 1 with "More precisely", then give two plain sentences on what is known and what is new.** Delete the sections titled "What is new" and "The key mechanism". Specimen: "The universal upper bound is known. The contribution is the family in (2), which rules out every smaller power" (`paper`, after Thm 1.1). Credit the theorem's authors once, at this point.

4. **Credit with verbs of dependence in the main clause, one sentence per predecessor, and put the difference in a second sentence.** Use "builds on", "developed by", "gave", "incomparable", never a contrast frame. Specimens: "Our construction builds on the work of Pabbaraju, who constructed a family" (ambainis-iraids-kokainis, §1); "Their nearly quartic separations ... concern a different classical measure, but their comparison-based viewpoint is particularly relevant here." (`paper`, §1.1).

5. **Give each external result a bracketed key with a location and keep repeated attribution out of the prose.** Use [3, Conjecture 2] or an alpha key such as [ABK16] consistently; remove the repeated "is OpenAI's" sentences and the P-numbers on each display (put the correspondence in one table in the appendix); replace in-sentence repository URLs with "see the record, §5.4" once per section. Specimen: "[3, Conjecture 2]" (`paper`, §1.1).

6. **Use "we" for proof steps and for contributions, about 15 to 20 per 1000 words.** "We analyze", "we apply Lemma 2", "we hide", "we ignore this complication". Use names for what others proved. The corpus median is 17.9 and all three manuscripts are near zero. Specimens: "We analyze an ideal sampling process and then implement each of its steps quantumly." (`paper`, proof of Prop. 3.2); "To achieve this, we hide a 'cheat sheet' in the input that contains all the information the quantum algorithm needs." (ref-02, overview).

7. **Replace "key mechanism", "plan" and "This section ..." with the field's three devices: a technique section in prose, one roadmap paragraph, and section openings that start the work.** The technique section narrates the classical half and the quantum half, says what it simplifies, and names where earlier approaches stall. The roadmap is one paragraph of one clause per section. Section openers restate the claim, say "We now ...", or begin with "Recall ...". Specimens: "For the sake of simplicity, we ignore this complication altogether in the remainder of this discussion." (ref-23); "Section 2 defines the function and its certificates. Sections 3 and 4 prove the two bounds in (2)" (`paper`); "In this section we prove Theorem 1, restated for convenience:" (ref-02).

8. **Introduce the cheat-sheet-style construction by the question the algorithm cannot answer, then answer it.** For the pointer and address mechanism, write the problem the construction solves in the order the preprint and ABK do: what the quantum algorithm can compute that a classical algorithm cannot, then where the certificate is hidden. A rhetorical question is acceptable once, answered in the next sentence. Specimen: "But what information do we have that is known only to the quantum algorithm? The value of f on the input!" (ref-02).

9. **Start proofs with the object, not with the announcement.** "Fix a deterministic algorithm making at most G queries." "Suppose, for contradiction, that ..." "Take a history τ ...". Use "Note that" and "Observe that" for side facts, at about 0.7 per 1000 words (all three manuscripts have none). Use "Clearly" or "It is not hard to see" only for one-line facts. Specimens: "To prove the claim, suppose for contradiction's sake that no such strategy for player 2 exists." (ref-13); "Note that for an even k = O(1) ... the above lower bound is ... and it matches the upper bound" (ref-06).

10. **Delete intensifiers that carry no mathematics.** Keep "exactly" only where it contrasts with "approximately" or "at most" in a statement; delete "genuine winner" (say "the winner"), "explicitly specified", "precisely", "merely", "directly". Target at or below 1.5 per 1000 words (corpus median 1.0; manuscripts 2.3 to 3.0). Specimens of the same claims in the field's wording: "The contribution is the family in (2)" (not "exactly the family"), "such a partition does not exist!" (ref-23, where emphasis is typographic and rare).

11. **State positive claims. Where a contrast is true, give it as two sentences naming both objects.** Remove "not X but Y", "rather than", "does not describe" frames, and bold not-X labels such as "An off-promise input is not a false input." (record L381). Corpus rate 0.3 per 1000 words; the record is at 1.15. Replace with the field's relation sentence: "The techniques of [SSW20] are incomparable to ours as their main focus is on proving optimal bounds on the Fourier weights of decision trees." (ref-06, Independent Work).

12. **Cut the negation chains by half.** Convert "No X is used" and "does not depend on" into the positive fact ("The cap holds for every m"; "The argument uses only the law of the measured label"). Target 4 to 5 per 1000 words; manuscripts are 7.7, 9.1 and 11.0. Worst sentences to rewrite first: exposition L167 "No transitivity and no margin away from 1/2 is used."; record L3540 "No supplied Lean declaration proves this refinement, and Proposition 4.2 needs neither it nor an optimality assertion."

13. **Break rule-of-three lists.** Use two items, or four named objects, or a full clause. The corpus has 0.6 per 1000 words, the companion 3.4. Rewrite first: companion L14 "every input, every random choice and every measurement branch", L61 "cyclic, unbiased or arbitrary".

14. **Move all status and verification material out of the body.** The body states each theorem once, plainly, with no sentence about a build, a Comparator run, a receipt, a review or a same-more-less comparison. Put one sentence in the introduction ("The theorem has also been checked in Lean; Appendix A explains what is and is not compared") and one appendix. Keep the "no human review" sentence once, in the front or end matter, not after theorems. Corpus status vocabulary is 0.5 per 1000 words; target at or below 2 in the body. Specimen of the field's manner for computation: "we implemented both adversary bounds as semidefinite programs and used the convex optimization package SeDuMi for Matlab." (hoyer-lee-spalek, §1) and the preprint, which reports nothing of the kind in its body.

15. **Place the AI statement at the end of each manuscript, titled "Use of LLM tools" or "AI disclosure", in two to four sentences, with verification and responsibility stated.** Specimens: "We reviewed, corrected, and independently verified all LLM-generated output and take full responsibility for the final manuscript" (ambainis-iraids-kokainis, end matter); "All mathematical statements and proofs were verified by the authors, who take full responsibility for the content of the paper." (zhang-shao, end matter). This applies equally to the record (currently L3). Attribution of the theorem to OpenAI stays in the introduction.

16. **Vary sentence length in the record toward the corpus: merge runs of short declaratives with "since", "so", "because" and "where".** Aim for about 19% of sentences under ten tokens and 17% over thirty; the record has 30% and 5%. Specimen of a long mathematical sentence in the field: "Their nearly quartic separations between certificate and quantum complexity concern a different classical measure, but their comparison-based viewpoint is particularly relevant here." (`paper`).

17. **Turn the record's scaffolding into prose.** Replace the bold four-paragraph "Reading guide" (L8 to L15) and the dependency tables with one introduction in the manner of rule 3 and a roadmap paragraph. Remove the "Formal correspondence" subsections from §4.8, §5.5, §6.7, §7.3 and keep one section (the existing §2.9 and Appendix B) for them. The HTML passage and claim comments belong in a separate build file.

18. **Give the record the connective openers and parentheticals the corpus has.** Use Thus, Hence, Then, Indeed, Since, In particular to start about 13% of sentences (record: 4%) and put scope remarks in parentheses at about 8 per 1000 words (record: 2). Specimen: "(Note that Simon's problem also provides a similar separation up to log factors.)" (ref-02, §3.1).

19. **Write the exposition in the lecture-note voice: invite, motivate, admit.** Open steps with "Let us ...", "Consider the following problem:", "We'll call ...". Say when something looks odd and why it is fine. Specimens: "Let us sketch the main idea for how to implement the reflection through |U⟩" (de Wolf); "This may seem like a stupid algorithm, but it has certain advantages." (de Wolf); "It may look contrived at first, but eventually will lead smoothly to Shor's and Grover's algorithm." (de Wolf).

20. **Number examples in the flow ("Example 1") and put each directly after the statement it illustrates; delete the table of examples and the "Who this is for" paragraph.** Use a three-sentence preface instead, in the manner of the survey introduction. Specimen: "The biggest gap known between s(f) and bs(f) is quadratic and was exhibited by Rubinstein [37]: Example 1 ..." (Buhrman and de Wolf, §4.2).

21. **Remove record cross-references from the exposition except at theorems.** Replace "(record §5.4)" after each step with one sentence at the start ("Complete proofs are in the long record") and a pointer next to each of the three headline statements. The exposition should read on its own, as the lecture notes do with their "referring to [30] for more details".

22. **Replace bold run-in leads with noun-phrase run-in headings or nothing.** Keep "**Comparing two columns.**" style only if it names an object, as Tal's run-in heading does. Delete "**The reason for four, in one line.**", "**Where this sits.**", "**Who this is for, and where it goes.**", "**What it does not establish.**". Specimen of the allowed form: "Quantum Query Complexity of the k-fold Rorrelation Problem." (ref-26, §1.1).

23. **Shape paragraphs like the corpus: mixed lengths, none above about 120 tokens, some of one or two sentences.** The corpus has a CV of 0.87 and a mean near 54; the exposition averages 92 with CV 0.60. Split the long expository paragraphs at each new object.

24. **Open and close the discussion of limits in the field's way.** Say a limit once, at the place it matters, in the first person: "Despite considerable efforts, we were not able to find a way forward within this framework." (ref-23). Finish the paper with a short "Open questions" section of three to six items: "We would like to highlight several open questions that were mentioned throughout the manuscript." (ref-26, §8) and "Questions for future work" (ref-13). Delete the sentence that qualifies each remark.

25. **Name the run-in section titles as objects.** Use "Overview of the proof", "Preliminaries", "The tournament", "The planted pair", "The exponent", "Proof of Theorem 1", "Open questions", "Acknowledgements", "Use of LLM tools". Never "What is new", "Where a natural shortcut fails", "The key mechanism". Specimens: "An addressed certificate with outward pointers", "The optimal power", "Appendix A The universal quartic bound" (`paper`).

## Notes for the revisers

- Re-run the comparison after revision: `python3 tools/meta/dissemination/mathematician_outreach_typeb/paper_register.py compare --profile /private/tmp/claude-501/-Users-willcook-src-ai-workflow/478fb70d-14ae-4bb7-931c-2f5ceb39c7a3/scratchpad/register/profile_v2.json --matrix docs/expert_companion.md docs/exposition.md docs/reasoning_record.md`. Success is movement of status vocabulary, "we", negation, triads, intensifiers and connective openers toward the IQR, not entry into it on every feature. The tool is a detector, and a good paper can sit outside the range on a feature for a reason.
- The corpus has no formal verification analogue, so rule 14 follows the closest practice available (computation in one sentence plus a pointer, AI use in end matter). It is a judgement, not a reading of the literature.
- Files written for this report: `scratchpad/register/profile.json`, `profile_v2.json`, `profile_expository.json`, `matrix.txt`, `cmp_*.txt`, `features.json`.
