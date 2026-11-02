# Mathematical and source review

This is a source-level review of the assigned Sections 1 and 2 task. The new Lean proof texts are unelaborated. The theorem names below identify proposed statements and proofs, not completed verification. Source locations refer to the attached packet unless a public URL is given.

## 1. The two principal lemmas need their clauses together

<!-- passage:review-1 -->

Lemma 2.1(ii) requires more than accuracy on promised inputs. Its query bound must apply to every input, it must always produce a Boolean outcome, and its workspace must be retainable coherently. The initial helper paired a coherent abstract sampler with a physical implementation of the same measured distribution. Review of `Upper/Compile.lean`, particularly `Samples.runs`, showed why that pair did not literally state one retained physical witness: that helper measures and resets. The complete theorem therefore opens the sampler witness and applies `compile_circ` directly to its isometry. The resulting continuation equation concerns that same witness and every embedded logical state.

This is a correction to the draft’s statement packaging, not to the preprint. The proof still uses the existing repetition count, error theorem and compiler. The fixed constant is selected before the size parameter and error tolerance. The all-input probability law is kept separate from the promised-input accuracy clause. See `construction_lemma_2_1_ii_complete` and the complete conjunction for Lemma 2.1.

For Lemma 2.2, a sampler that first prepares a uniform test index does not state the full arbitrary-superposition clause. The delivered direct-sum theorem has an explicit equality for the block at every index and every complex coefficient function. Each block applies the exact test isometry to its own starting ket. Exactness of the measured Boolean law forces every wrongly labelled basis amplitude to vanish, because a nonnegative squared amplitude is bounded by the total mass of that wrong outcome. This establishes the required state-level behavior. It retains workspace; no clean XOR oracle or ancilla-reset property is asserted.

The complete construction theorem then chooses a finite physical embedding and invokes `compile_circ` for those same witnesses. Its physical equality ranges over all embedded logical states, rather than states outside the embedding range. The generic direct-sum result is stated separately from this finite-family specialization. The preprint fixes the column and address while supplying test indices in superposition, so the formal order “for each column and address, there exists an implementation” matches its claim. [OpenAI26, Lemmas 2.1–2.2; source `Upper/Circuit.lean`, `Upper/Sampler.lean`, `Upper/Compile.lean`.]

<!-- /passage:review-1 -->

## 2. The promise is asymmetric, and the circuit must handle every input

<!-- passage:review-2 -->

The one-case of Forrelation uses a positive lower threshold on the correlation. The zero-case uses a small absolute value. A sufficiently negative correlation is outside the promise. Replacing the one-case with an absolute-value threshold would define a different problem. `construction_equation_4` retains all three possibilities, including undefined inputs and disjointness of the two defined cases. [OpenAI26, equations (3)–(4); BS20, equations (1.1)–(1.3).]

The circuit proof is correspondingly total. Its domain bit equals the disjunction of the two integer tests; its value bit equals the first integer test even on inputs outside the promise. The output-bit theorem exposes that behavior for the actual circuit gate list, rather than merely constraining the value bit when the domain bit is true. The denominator is a positive integer on the paper’s power-of-four family, and the normalization theorem identifies the integer matrix word with the real correlation. [OpenAI26, Lemma 2.1(iii) and its proof; `Forrelation/Circuit.lean`, `Forrelation/Promise.lean`.]

The supplied paper explicitly takes m through powers of four in the opening of Section 2. This is not a discrepancy introduced by the formalization. No extension to all powers of two is needed for the assigned result. [OpenAI26, `paper/extracted.md:131–132`.]

<!-- /passage:review-2 -->

## 3. Query counts: the local phase operation and the complete program

<!-- passage:review-3 -->

The direct projection algorithm has success probability equal to the square of the correlation. In Aaronson–Ambainis, this k-query construction appears in Section 3.2 immediately before Proposition 6. Proposition 6 concerns the different acceptance law based linearly on the correlation and uses half as many queries, rounded up. Citing Proposition 6 alone for the square-probability algorithm would identify the wrong construction. [AA15, Section 3.2, Figure 1 and the text before Proposition 6.]

`ConstructionPhase.lean` proves the physical one-call phase-kickback identity directly from the standard bit oracle. The hypothesis specifies the answer-qubit minus subspace by the relation between its two amplitudes. It permits arbitrary index amplitudes and entangled workspace, and a companion theorem preserves the subspace and normalization. The textbook oracle convention is the one described by de Wolf in Section 2.4. [dW26, printed pp. 17–18.]

The general compiler supplied in the repository charges two bit queries per abstract read. That produces a correct physical implementation of the projection test at cost 2k. The local one-call phase theorem has not been assembled with the entire Walsh/product/projection circuit into a tight `Runs k` witness. This is kept as a partial correspondence for the bundled projection row. The complete amplified Lemma 2.1(ii) has the required asymptotic bound with the available constant overhead.

<!-- /passage:review-3 -->

## 4. Exact arithmetic and the internal-register qualification

<!-- passage:review-4 -->

The circuit’s endpoint correctness and size come from the existing modular arithmetic construction. Its `Enc` invariants record residues modulo a power of two; exact sign information is proved where the final comparisons require it. Consequently the exact output and size theorem is valid through that formal route without an additional theorem saying that every intermediate register equals an unrestricted integer.

`ConstructionArithmetic.lean` supplies explicit bounds for the ideal integer recurrence, prefixes of the final signed sum, and offset butterfly blocks. Repeated triangle inequalities give the polynomial magnitude estimate needed in the paper’s informal circuit argument. These statements concern the ideal integers. A register-by-register relation between those integers and the concrete modular implementation has not been supplied. [OpenAI26, proof of Lemma 2.1(iii); `Forrelation/Arithmetic.lean`, `Forrelation/Product.lean`, `Forrelation/Circuit.lean`.]

No overflow counterexample was found or proved. A coarse triangle bound exceeding a selected representation range does not establish that an actual intermediate value reaches that bound. The residual is therefore recorded as missing formal correspondence, with the exact circuit endpoint retained.

<!-- /passage:review-4 -->

## 5. Adaptive pointer tests and valid certificates

<!-- passage:review-5 -->

A pointer test reads the pointer word and then the selected target bit. Its adaptive query depth is logarithmic, even though each possible target position can influence the Boolean function. The preprint already states this correctly. The fixed-support error identified in the earlier review belonged to an old ledger statement. The delivered proof exposes the exact tree evaluation and depth and gives an explicit essential-coordinate argument for the lookup function. The blueprint records the exact scope of any transport into the complete input coordinate type. [OpenAI26, Lemma 2.2, proof; adjudication `R1-AF-00`, `R2-LR1`, `R3-LA-01`.]

The equivalence between passing output tests and having a defined correct partial-function answer requires `CircuitRealises C f`. A syntactically consistent transcript of an incorrect circuit would not suffice. That premise is retained in the addressed-winner/test equivalence and local dichotomy. Winner uniqueness itself uses only the all-ones condition and the outward zero pointer, so it does not require circuit correctness. [Source `Construction/Transcript.lean`, `Construction/Winner.lean`, `Construction/LocalTests.lean`.]

<!-- /passage:review-5 -->

## 6. The numerical comparison and the published lower-bound proof

<!-- passage:review-6 -->

The inequality comparing the floored quantity L with a positive multiple of the Bansal–Sinha asymptotic expression is a numerical statement. The delivered proof makes the positive constant explicit and includes the unfloored middle term. It does not use the repository theorem named `bansalSinhaLower` as a substitute for this comparison. That separate theorem supplies the fixed-k complexity lower bound used by the family. [Adjudication `F-EQ1-EQUIV` for the analogous constant convention in equation (1); `funnel_adjudication_notes.md` for the corrected `claim-bs-to-L` tie; `ForrelationLower/Main.lean`.]

The attached two independent readings of Bansal–Sinha v3 identify a specific failure in the third inequality of the Section 5.4 display, `main.tex:1184`. Reading the source confirms the exponent mismatch: at level j, the logarithmic factor before the step has exponent (j−1)/2, while the asserted bound uses j(1−1/k)/2. Their difference is (j/k−1)/2, which is positive for j>k. The displayed level range includes such levels when k≥3. This invalidates that step as written; it does not by itself prove the theorem false. [BS20, Section 5.4; supplied `bansal_sinha_section54_second_reading.md`.]

The required fixed-k lower bound in the Lean source uses its own Gaussian/Fourier argument and has a weaker logarithmic denominator sufficient for the construction. The present return records that alternative proof route. It does not claim to settle the sharp external logarithmic factor or the other round-two research tasks.

<!-- /passage:review-6 -->

## 7. Attribution requires the whole relevant source passage

<!-- passage:review-7 -->

The addressed certificate has the standard role of checking a partial-function answer and its promise. Aaronson, Ben-David and Kothari give the general certifying-function and cheat-sheet definitions in the versioned source at Definitions 14 and 15. The numbering in the packet’s text extraction differs, so the bibliography uses the official numbering. This is an antecedent for the certificate role, without attributing the whole quartic construction to that paper. [ABK16, Section 6.1.]

Ambainis and coauthors’ main pointer constructions use balanced trees. However, the same Section 1.3 explicitly discusses direct pointers from the special element to a zero in every nonmarked column and explains their alphabet cost. A comparison that reads only the balanced-tree paragraph misses that passage. This refines the scope of the prior adjudication and precludes a novelty claim for the bare direct-zero-pointer idea. It is a bibliographic proposal for the receiving team, not a silent amendment of the existing adjudication. [ABB+15, Section 1.3, “Use of a balanced tree”.]

The contribution attributable to the attached OpenAI paper remains the particular construction and separation it states. The formal wrappers, strengthened finite constants and explicit bridges in this return are identified by their statements; no literature search is treated as evidence of originality.

<!-- /passage:review-7 -->

