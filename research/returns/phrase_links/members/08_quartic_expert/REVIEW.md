# Review: the expert companion, phrase by phrase

## 1. Completed return and scope

This return supplies a complete phrase layer for **packet 08_quartic_expert**, covering the assigned **paper lines 1–303**. It contains **241 exact phrase ties**, **177 declaration titles and reading notes**, and **eight topics**. Of the ties, **240 have Lean destinations**; one explanatory tie deliberately has no Lean destination because the paper identifies the combining calculation as written mathematics only. The files are `ties.json`, `topics.json`, `titles.json`, `notes.json` and this review.

The reference is the supplied source snapshot at commit `f192def14f95a3aff7da5866f35be7b565595e1d`. Every assigned paragraph, display, table and caption was considered. There is no unreviewed suffix. All **237 manifest-listed input files retain their original bytes**, including the paper and all Lean sources. This return does not edit the manuscript, create new Lean declarations, deploy the reader, or claim a new Lean build or Comparator run.

There is **no phrase seed** in this packet. Every tie therefore has `status: new`, and `removed` is empty. The existing paragraph selection IDs are accounted for in the migration table below; they are not misrepresented as old phrase IDs.

The intended reader knows the query model but is new to this construction and may not read Lean fluently. Each note starts with the mathematical object or claim, explains the conditions that matter, and translates the few Lean names needed to understand the selected statement. The goal is that a click resolves a local question: what is this object, what does this assertion require, and what does the declaration actually supply?

## 2. The argument made visible to a new reader

The reader needs a small number of distinctions before a dense formal statement becomes useful. These distinctions now determine the phrase boundaries, titles and reading notes.

### Input bits, addresses and certificates have different jobs

| Paper object | What it is | What the reader must not infer from its name |
| --- | --- | --- |
| $X_i$ | The $m$ input bits forming column $i$'s string. | A column is not automatically a valid candidate because its string is all ones. |
| $A_{i,h}$ | One input to the partial address function $P$. | It is not already an address bit, and it need not satisfy the promise. |
| $s_i$ | The vector of $P(A_{i,h})$ values when all are defined. | An arbitrary proposed address is not necessarily this true address. |
| $B_{i,s}$ | An arbitrary input cell indexed by column and address. | Its stored transcript and pointers are untrusted input bits. |
| A pointer | An $\ell$-bit row name, followed by a read of the selected string bit. | Reading one pointer is not a unit-cost read of a whole word or cell. |
| A winning certificate | The conjunction of the all-one string, promised address inputs, correct transcripts and outward zero pointers. | Decoding an address alone does not certify that the column wins. |

The corresponding ties separate all four winner conditions, the total function, uniqueness, gate consistency, output tests and the failure of some local test at **every** address of a nonwinner. The exact two-output circuit checks both domain membership and value. This is what makes the final function total even though its address function is partial.

### The quantum saving comes from separating candidate generation and verification

The comparison needs a reliable address only for a genuine winner. Its outward pointer finds a zero in a rival, while the rival cannot find a zero in the winner's all-one string. The rival's address inputs may be outside the promise. The notes state this asymmetry at the comparison theorem itself.

The tournament then produces a short list using those comparisons, and the verifier checks the list. The list theorem, comparison cost, fixed-address search, fresh decoding and complete budget have separate destinations. A theorem about a single stage is not offered as the full candidate-list theorem. The current `Paper.quantumTournament` really does supply a bounded list, its query cap and its inclusion probability.

The weights are analysis quantities. The algorithm prepares comparison states; it does not compute a numerical table of all $a_{ij}$ or all $w_i$. The product-weight definition, total-weight definition, expectation identity and state preparation therefore receive different cards. The note on the exact identity explains the cancellation: the terms for $(i,j)$ and $(j,i)$ have the same weight coefficient, and complementary comparison probabilities sum to one. No transitive ordering of losers is assumed.

### Three sampling probabilities must remain distinct

For a candidate $i$, the stage's joint success mass is $w_i/m$, the total success probability is $W/m$, and the conditional label law is $w_i/W$. The last expression is meaningful as a conditional probability only when $W>0$. Equation (6) is tied to a theorem stating all three expressions, and its note names the positive-total hypothesis.

The literal tensor preparation, its measured successful-label law and the physical amplified sampler are separately identified. Bounded amplification has an abstract call-count theorem and a physical implementation theorem. The notes explain which one is open, which query convention it uses, and why preservation of the conditional label law matters: amplifying success must not bias the next pivot.

### The classical argument uses the query index before the answer

A query to $B_{i,s}$ already names $s$. The simulator can therefore output the proposed cell address without reading that cell bit. The address is a simultaneous guess of independent hard values. The notes distinguish the time counter, the total target-query cap and the separate per-input caps used by the direct-product lemma.

The cap boundary is stated precisely: **having used exactly $L$ target queries does not itself abort the simulator**. It aborts only when an additional target query would exceed the cap. It can still reach the selected time and return the address of the next cell query.

The bounded event is “column $i$ is light **and** the selected query hits its true cell.” It is not a probability obtained by conditioning the hard distribution on being light. Independent outside data are fixed or averaged at the appropriate stage. A positive-probability transcript preserves the product structure needed by the continuation-value proof; conditioning on a future query-count event is a different operation.

### The quartic conclusion has an essential order of quantifiers

The upper and lower bounds belong to the **same** total function and the **same** circuit witness. For a proposed exponent $\alpha<4$, choose a fixed integer $k$ with $k>2/(4-\alpha)$, then let $m$ grow. The fixed-$k$ constants and threshold may depend on $k$. The notes keep that dependence visible and distinguish the finite floor bound, its eventual real-power consequence, and the universal quartic upper bound.

`alphaTot` is titled as an **infimum**, not a smallest exponent assumed to be attained. The arithmetic statement at $k=3$ is titled as the identity $4-2/k=10/3$, not as a self-contained separation theorem. The growing-$k$ schedule in Section 7 retains the paper's explicit boundary: the uniform Forrelation input is stated in Lean; the final combining calculation is written mathematics only.

## 3. Material manuscript finding

### A definite sign-notation correction at line 67

The paper says:

> we read bit $a$ of block $j$ as the sign $z_j(a)=(-1)^{a}$

Here $a$ is used both as the coordinate of $z_j(a)$ and as the Boolean value being exponentiated. Read literally as a coordinate, the sign no longer depends on the stored input bit. Lean's `bitSign` consumes a Boolean, and the Forrelation numerator applies it to the stored bit `z (h, path h)`.

A minimal correction is to distinguish the input bit from its coordinate, for example:

> If $x_j(a)$ is the bit at coordinate $a$ of block $j$, write its sign as $z_j(a)=(-1)^{x_j(a)}$.

Tie `p2-sign-coordinate` is `different`, with the exact reason recorded beside it. This is a local notation error. It is not evidence of a faulty Forrelation theorem, and the submitted manuscript is unchanged.

## 4. What the source supports, and where a link needs qualification

### Current paper-form statements supersede several historical gaps

The November 2 fidelity review is useful history, not the authority for a later snapshot. The current source supplies several results that the older review described as incomplete:

- `construction_lemma_2_1_complete` states the three required Forrelation properties together.
- `construction_lemma_2_1_ii_complete` includes a retained physical decoder, with its continuation behavior, rather than only a measured/reset logical sampler.
- `construction_equation_4` covers undefined inputs and disjointness; `construction_transcript_correct` identifies a consistent transcript with actual evaluation; `construction_local_dichotomy` includes failure at every address of a nonwinner.
- `equation_15` gives the literal tensor state with retained comparison workspaces.
- `quantumTournament` and `quantumTournament_list` supply the actual finite candidate list with its membership guarantee and branch cap.
- `Paper/ClassicalDirectProduct.lean` contains the printed route's transcript rectangles, conditional product law, continuation values, one-factor inequalities and finite conditional-expectation argument. The alternate subdistribution proof still exists, but it is no longer the only available route.
- The current classical source includes posterior uniformity, the per-time light-cell bound and absolute acceptance-gap statements.

These are findings from the supplied source text. They are not new execution receipts.

### Register width is narrower than an unrestricted signed-integer claim

At line 71, the concrete circuit-width theorem bounds modular register widths by $O_k(\ell)$. It does not by itself identify every stored register with an overflow-free unbounded signed integer. The separate ideal-arithmetic estimates in `ConstructionArithmetic.lean` do not silently supply that missing composition. The width phrase is consequently `part/weaker`.

The final circuit theorem still gives the required exact domain and value outputs. The qualification concerns what this particular width link establishes, not the validity of that endpoint.

### A proof endpoint does not certify every printed intermediate argument

The erased-zero endpoint $4G/m^2$ is present. Its Lean proof weakens a stronger $2G/m^2$ induction bound. Posterior uniformity is also present. The separate early/late counting estimates printed in the companion were not located as declarations, so the annotation does not claim that opening the endpoint checks that exact written route.

Likewise, `eventually_gt_rpow` gives eventual domination of every fixed positive multiple of $(1+Q)^\alpha$ under the family bounds. It does not print the exact coefficient in the companion's displayed pointwise quotient inequality. The whole display is indivisible and that row is `part/weaker`; the note explains the relationship.

### Amplification geometry has nondegenerate hypotheses

The plane-and-direction theorem assumes $0<p<1$, and its normalized successful-direction conclusion also requires a nonzero new successful component. It gives agreement up to global phase. At $p=0$ there is no conditional successful direction; at $p=1$ the two-dimensional description degenerates. These qualifications are local to the geometric explanation. The general bounded-amplification contract separately handles zero success and supplies the relevant output-law guarantees.

### Elementary consequences and written extensions remain visible as such

No exported declaration was located for the complete displayed input-length equality and $O_k(m^{22}\ell^3)$ simplification, or for the entire sentence $2^r=m^{20}$. Their ingredients are present, but the arithmetic conclusion is not assigned a false exact match.

The general error-parameterized symbols $R_\varepsilon,Q_\varepsilon$ are not replaced by the fixed-error declarations as though those defined the whole family. The return ties the actual error-$1/3$ specializations. The AND conditioning example has no located finite-example declaration. The finite-tree averaging interface is not described as a separate measure-theoretic formalization of arbitrary auxiliary probability spaces.

The Section 7 comparisons with Bansal–Sinha, Sherstov–Storozhenko–Wu, and Špalek–Szegedy are expressly written mathematics only. This packet does not contain the full linked reconstruction needed to audit those detailed external-paper diagnoses, and no Lean endpoint is substituted for that missing evidence. The explicit growing-family calculation likewise remains an explanation tie with no Lean rows. Axioms, Comparator acceptance, authorship and execution claims in Section 8 remain provenance claims, not new proof badges.

## 5. Annotation and presentation decisions

### Eight mathematical topics

Topic describes where a phrase belongs in the argument. It does not describe whether the link is exact, partial or unsupported. A color can identify a topic, but should never be the only way to communicate it, or imply that every sentence of that color is verified.

| Topic | Purpose | Ties |
| --- | --- | ---: |
| Query complexity and the quartic exponent | The query model, the two complexity bounds and the order in which their parameters are chosen. | 38 |
| Forrelation and address decoding | The partial function that makes addresses cheap to decode quantumly and expensive to predict classically. | 35 |
| Columns and certificates | The input bits, the winning conditions and the local tests of a proposed certificate. | 23 |
| Pairwise comparisons | How two columns are compared when only a genuine winner has a reliable address. | 17 |
| Weighted tournament and amplification | How weighted sampling finds a short candidate list despite arbitrary comparisons between losers. | 38 |
| Verifying a candidate | How exact local tests turn the candidate list into a bounded-error algorithm on every input. | 25 |
| The planted input and erased zero | The two coupled input distributions and the cost of finding their changed zero. | 20 |
| Predicting the hidden address | The independent hard values, separate query caps and capped simulation behind the classical lower bound. | 45 |

### Titles and notes

Every named declaration has one plain title of 2–12 words and a note of 40–120 words. There are **12,218 words of reading notes**. Reused declarations have a single consistent card; short per-link notes explain a local contribution when needed. Titles use the mathematical quantity actually bounded: a success probability is not called an answer vector, a probability estimate is not called a query cost, and “with high probability” is not shortened into certainty.

The notes state meaningful hypotheses close to the claim: `hdef` for a defined true address, `hC : CircuitRealises C ...` for an exact circuit, `hw` for a winning certificate, `hW` for positive total weight, `hn` for enough repetitions, and the relevant hardness or cap premise. They explain common translations such as $m=4^t$, $\ell=2t$, $r=40t$, `R (totalise f)` and `Q (totalise f)`. A symbol such as `t` is explained where it counts pivots instead of the construction parameter.

The notes do not start with repository mechanics. Raw names, source files and proof status remain inspectable, but the first reading task is mathematical.

### Short spans, whole formulas and exact source locations

Ties use the supplied source bytes, with unique `after` anchors where needed. Displays remain whole. Separate claims receive separate targets; clauses of conjunctions can highlight their own lines. A proof-step tie highlights the actual local assertion and uses `relation: proof`; it does not pretend that the enclosing theorem's headline is the same sentence.

The supplied checker can accept a range that stops at a nested Lean `let ... :=` or includes the following documentation block. The additional review repaired those ranges: theorem highlights extend through the real conclusion, and definition highlights include the relevant body or fields. Complete surrounding declarations and their variables should remain available behind a narrow highlight.

For indivisible spans supported by several declarations, each row is judged on its own contribution. A `part/weaker` row can be an honest ingredient of a correct combined claim. The number of such rows is therefore **not a count of false mathematical claims**. The exhaustive appendix below identifies each exact limitation.

### Reader integration

The practical display order should be: the selected phrase, the plain title, the mathematical note, any local fidelity qualification, and the source with the exact range highlighted. Keep source context available without requiring a cold reader to start there.

Retain the paragraph selections as navigation routes, and use these ties for phrase-level opening. Some source names use OpenAI's equation numbers rather than this companion's: `eq_19`, `eq_21`, `eq_22` and `eq_23` support companion (8), (9), (10) and (11). The new titles avoid exposing that numbering mismatch as an unexplained jump.

Integration must respect the actual rendered elements. The abstract lives in YAML, some properties are in a Markdown table, and displays and figure captions have their own boundaries. This return validates source locations; it does not claim a browser-rendered interaction test. Do not insert tags into unsupported caption or image-alt syntax. Bind the phrase layer to the supplied paper hash and rerun resolution if the manuscript changes.

## 6. Coverage of the whole assigned range

The table records what was tied and what was deliberately left as prose or written mathematics. “No separate declaration found” is a source-location finding, not a claim that the mathematical sentence is false.

| Paper location | Coverage and deliberate boundary |
| --- | --- |
| Front matter and abstract, lines 1–20 | Headline bounds, exponent and key mechanisms receive local ties where a declaration states them. Metadata, authorship and review-status prose remain provenance. |
| Introduction and Theorem 1, lines 21–39 | Model, total functions, complexity, critical exponent, universal bound, same-family witnesses, full display (1), finite floor form and explicit constants are distinguished. Historical progress is left to its citations; the $k=3$ arithmetic identity is not promoted into the whole separation proof. |
| Technique overview, lines 40–53 | Winner definition and uniqueness, outward pointers, quantum listing/verification and classical prediction receive appropriate local links. Attribution, comparisons with previous constructions and organization remain explanatory. |
| Preliminaries, lines 55–57 | Worst-case caps, fixed-error complexities, promise-restricted correctness, bit oracle and pointer reads are tied. General error-parameterized notation, $[m]$ and hidden-constant conventions are not fabricated as declarations. |
| Forrelation properties, lines 59–65 | The three properties and each property in the table are tied. The “What it buys” column explains later uses. |
| Forrelation construction, lines 67–71 | $H$, $u$, $D_z$, the $(\Phi,\delta)$ display, promise, projection, retained decoder, negative values, numerator, transforms, width qualification and exact integer tests are separated. The sign notation is flagged. |
| Lemma 2, lines 73–80 | Every conclusion is covered, including the fixed-$k$ lower-bound display, coherent cap and exact circuit. Historical import and alternative proof route are explained rather than conflated. |
| Input layout, lines 84–90 | Parameters, strings, address inputs, true address, cells, pointers, transcripts and valid row words are tied. Full input-length arithmetic and the $2^r=m^{20}$ simplification remain untied. |
| Winning and local verification, lines 92–108 | Four winner clauses, totality, uniqueness, test branches, consistency, output failures, all-address failure, exact and asymptotic test counts and local costs are covered. |
| Interfaces and first figure, lines 110–118 | The deterministic and probabilistic winner guarantees are tied. Arbitrary loser behavior is an absence of a promise, not an assertion that every possible probability is attained. Row 6 is an illustrative example without a found finite Lean instance; the referenced SVG is absent. |
| Comparison, lines 119–130 | Separate decoders, pointer rule, self-comparison, error allocation, canonical experiment, $a_{ij}$, complementarity, dominance and forward/inverse costs are covered. |
| Tournament and drift, lines 132–150 | Proposition 3, list law, weight definitions, update, exact identity (5), expected halving, iterated expectation, surviving winner and ideal miss probability are covered. The motivating equation $w_iq_j=w_jq_i$ is not represented as an independently proved uniqueness theorem. |
| Quantum sampling, lines 152–163 | Full tensor preparation, success flag, product mass, distinct-label mass calculation, all three probabilities in (6) and positive-success conditioning are distinguished. Weights remain analysis quantities. |
| Amplification and list completion, lines 165–174 | Abstract and physical contracts, conditional law, geometry hypotheses, chosen threshold/error, stopping, coupling, final miss bound and tournament cap are covered. |
| Final verification and quantum bound, lines 176–183 | Fresh decoding, fixed-address test law, one-sided error, winner/nonwinner cases, complete errors and numeric slack are covered. The final $\ell^6$ budget is tied; sharper intermediate logarithmic simplifications are not falsely attributed to that coarse envelope. |
| Hard inputs, lines 184–204 | Dummy bit assignments, law, independent planting choice, planted winner and changed locations are distinct. The generic Yao principle and common-prefix explanation are not replaced by narrower declarations. Figure relationships are tied in the main prose; the referenced image is absent. |
| Erased zero, lines 206–214 | Discovery count, $\Pr(\text{erased zero})=\mathbb EZ/m$, posterior uniformity and display (8) are tied. The separate early/late estimates were not found as source statements. |
| Prediction and direct product, lines 216–226 | Cell-index information, answer vector, Lemma 5, rectangles, conditional product law, continuation inequalities and terminal bound are covered. The AND example remains written mathematics. |
| Heavy/light split and simulator, lines 228–254 | Heavy-column probability, exact cap, both simulator counters, event inclusion, simultaneous prediction, independent averaging, display (9) and complete cell-encounter estimate are covered. No conditional-on-light hardness claim is introduced. |
| Completing the classical bound, lines 256–262 | Three-term probability bound, scalar estimate, coin averaging and finite lower bound are separate. Discussion of scale and slack remains interpretation. |
| Exponent, lines 264–273 | Both floor estimates, named family constants, strict choice of $k$, eventual domination and absence of a smaller universal power are tied. The exact quotient coefficient is distinguished from the eventual-domination theorem. |
| Further results, lines 275–291 | Fixed-$k$ direct proof ingredients, uniform bound, sharper erased-zero result, alternate direct product and three quartic routes are tied. The growing-family calculation and external-paper diagnoses retain their written-only boundary. |
| Verification and references, lines 293–303 | Exact named theorem mentions are tied. Axiom reports, Comparator receipts, authorship, release references and reference-list markup remain provenance. |

## 7. Migration of the 16 existing editorial selections

The old selection objects locate paragraphs or passage ranges and may carry an earlier source hash. They can remain useful navigation. The table gives the corresponding new phrase IDs in each selected range; a wider proof section naturally has additional ties outside that old range. Neither the old site data nor its navigation is changed by this return.

| Existing selection | Paper lines | New phrase destinations |
| --- | --- | --- |
| `expert/headline/0` | 29–35 | `thm1-universal-upper`, `thm1-quantifier-order`, `thm1-both-bounds`, `thm1-exponent` |
| `expert/certificate/0` | 92–92 | `p3-wins-summary` |
| `expert/comparison/0` | 123–123 | `q4-decode-two`, `q4-pointer-tests`, `q4-comparison-rule`, `q4-self-comparison`, `q4-winning-comparison` |
| `expert/weight/0` | 141–146 | `q4-initial-weight`, `q4-weight-update`, `q4-pivot-zero`, `q4-weighted-draw`, `q4-drift-display` |
| `expert/weight/1` | 148–148 | `q4-half-drift`, `q4-pair-cancellation` |
| `expert/pivot/0` | 152–163 | `q4-prepare-comparisons`, `q4-tensor-display`, `q4-success-flag`, `q4-independent-registers`, `q4-orthogonal-labels`, `q4-success-law-display`, `q4-ideal-label-law` |
| `expert/verification/0` | 178–178 | `q4-fresh-address`, `q4-uniform-test-dichotomy`, `q4-verification-search-cost`, `q4-accept-search-failure`, `q4-one-sided-testing`, `q4-winner-sure-at-address`, `q4-nonwinner-error` |
| `expert/planting/0` | 196–196 | `c5-dummy-object`, `c5-dummy-zero-rows`, `c5-address-law`, `c5-blank-cells`, `c5-dummy-loses`, `c5-independent-I`, `c5-planted-object`, `c5-plant-writing`, `c5-planted-winner` |
| `expert/erased-zero/0` | 208–208 | `c5-zero-count`, `c5-erased-identity`, `c5-unseen-zero` |
| `expert/erased-zero/1` | 210–214 | `c5-erased-bound` |
| `expert/address/0` | 218–218 | `c5-index-names-address`, `c5-address-values` |
| `expert/direct-product/0` | 240–252 | `c5-total-implies-separate`, `c5-separate-caps-used`, `c5-predictor-bound`, `c5-light-hit-simulates`, `c5-joint-event-chain`, `c5-query-times`, `c5-cell-visit-bound` |
| `expert/forrelation/0` | 59–59 | `p2-three-properties` |
| `expert/exponent/0` | 265–272 | `e-first-floor`, `e-second-floor`, `e-real-lower-bound`, `e-choose-k`, `e-ratio-display`, `e-no-smaller-power`, `e-k-three-range` |
| `expert/projection/0` | 67–71 | `p2-input-blocks`, `p2-sign-coordinate`, `p2-sign-query`, `p2-H`, `p2-u`, `p2-D`, `p2-Phi-delta`, `p2-promise`, `p2-projection`, `p2-gap`, `p2-retained-decoder`, `p2-negative-promise`, `p2-numerator`, `p2-transforms`, `p2-integer-width`, `p2-integer-tests`, `p2-denominator` |
| `expert/joint-event/0` | 240–252 | `c5-total-implies-separate`, `c5-separate-caps-used`, `c5-predictor-bound`, `c5-light-hit-simulates`, `c5-joint-event-chain`, `c5-query-times`, `c5-cell-visit-bound` |

## 8. Exhaustive weaker and different comparisons

There are **40 weaker rows** and **1 different row** among **258 individual Lean links**. The comparison is made against the selected phrase, with the surrounding paper hypotheses in scope. Many weaker rows supply complementary ingredients of one displayed formula or one compound claim. Where a full type is needed to understand a selected proof slice, it is quoted first, followed by the actual selected lines. Lean excerpts below are copied from the named files in the supplied snapshot.

### 8.1. `q4-preview-verify` — paper lines 43–43

**Paper phrase:**

> Checking that a given column wins costs about $\sqrt m$ quantum queries, by Grover search over its roughly $m$ local tests.

**Lean:** `QuarticQuery.Paper.quantumVerify` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 498–507:

```lean
theorem quantumVerify (hk : 1 ≤ k) (ht : 1 ≤ t)
    (hC : CircuitRealises C (P k t)) {n : ℕ} {ε : ℝ}
    (hε : 0 < ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n) :
    ∃ v : BitInput (Loc k t C) → Col t → ℝ,
      (∀ c, Runs (2 * addrCost k t n + searchCost t (Fintype.card (Tests t C)) ε)
        fun x b => bern (v x c) b) ∧
      (∀ x c, 0 ≤ v x c ∧ v x c ≤ 1) ∧
      (∀ x c, (¬ ∃ s, WinsAt (P k t) C (2 * t) (40 * t) x c s) → v x c ≤ ε) ∧
      (∀ x c s, WinsAt (P k t) C (2 * t) (40 * t) x c s → 1 - ε ≤ v x c) := by
```

**Exact comparison:** The type supplies a bounded verifier with its two correctness guarantees, but not the square-root asymptotic estimate or the local-test count asserted in the sentence.

**Lean:** `QuarticQuery.Paper.quantumVerify_search_query_bound` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 433–436:

```lean
theorem quantumVerify_search_query_bound (t K : ℕ) (hK : 2 ≤ K)
    {ε : ℝ} (hε : 0 < ε) (hε1 : ε < 1 / 2) :
    (searchCost t K ε : ℝ) ≤
      276 * Real.sqrt (K : ℝ) * Real.log (1 / ε) * (testCost t : ℝ) := by
```

**Exact comparison:** The type bounds fixed-address failed-test search under K ≥ 2 and 0 < ε < 1/2. It does not include fresh address decoding, complete winner verification or the substitution K = O_k(m ell^3).

### 8.2. `q4-preview-candidates` — paper lines 43–43

**Paper phrase:**

> The new construction instead lists a few candidates with cheap comparisons and verifies only those

**Lean:** `QuarticQuery.Paper.quantumTournament` — `QuarticQuery/Paper/QuantumTournamentFacts.lean`; `part/weaker`.

Selected source lines 287–303:

```lean
theorem quantumTournament {ι Col : Type} [Fintype ι] [Inhabited ι]
    [Fintype Col] [DecidableEq Col] {cc : ℕ} {a : BitInput ι → Col → Col → ℝ}
    (hm : 2 ≤ Fintype.card Col) (hc : ∀ x, IsComparison (a x))
    (hcmp : ∀ i p, Samples cc fun x b => bern (a x i p) b) :
    let m := Fintype.card Col
    let T := Tval m
    let ε := epsval m
    ∃ C : ℕ, ∃ law : BitInput ι → QuantumCandidateList Col T → ℝ,
      (C : ℝ) ≤ 6072 * (cc : ℝ) * Real.sqrt (m : ℝ) *
        (T : ℝ) ^ 2 * Real.log (T : ℝ) ∧
      Samples (T * quantumStageReads m T cc ε) law ∧
      Runs C law ∧
      (∀ x o, 0 ≤ law x o) ∧
      (∀ x, ∑ o, law x o = 1) ∧
      ∀ x s, Dominant (a x) ε s →
        1 - 2 * (m : ℝ) / 2 ^ T - T * ε ≤
          ∑ o : QuantumCandidateList Col T, if s ∈ o.1 then law x o else 0 := by
```

**Exact comparison:** The type supplies the bounded candidate list and its cost for an abstract comparison circuit. It does not verify those candidates or substitute this construction’s comparison budget.

**Lean:** `QuarticQuery.Paper.quantumVerify_list` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 528–531:

```lean
theorem quantumVerify_list {cV : ℕ}
    {v : BitInput (Loc k t C) → Col t → ℝ}
    (hv : ∀ c, Runs cV fun x b => bern (v x c) b) (L : List (Col t)) :
    Runs (L.length * cV) fun x b => bern (vall (v x) L) b :=
```

**Exact comparison:** The type bounds verification of a supplied list by its length times the single-candidate budget. It does not generate the list or supply its comparison procedure.

### 8.3. `q4-preview-weight` — paper lines 47–47

**Paper phrase:**

> OpenAI's tournament instead samples pivots with weights equal to the probability of beating all earlier pivots

**Lean:** `QuarticQuery.Tournament.weight` — `QuarticQuery/Tournament/Ideal.lean`; `part/weaker`.

Selected source lines 35–37:

```lean
@[expose] def weight (a : ι → ι → ℝ) : List ι → ι → ℝ
  | [], _ => 1
  | p :: L, i => weight a L i * a i p
```

**Exact comparison:** The definition gives the product update of candidate weights. It does not itself define the distribution used to sample pivots or prove the independent-comparison probability interpretation.

**Lean:** `QuarticQuery.Tournament.expectFrom` — `QuarticQuery/Tournament/Ideal.lean`; `part/weaker`.

Selected source lines 42–47:

```lean
@[expose] noncomputable def expectFrom (a : ι → ι → ℝ) :
    ℕ → List ι → ((ι → ℝ) → List ι → ℝ) → ℝ
  | 0, L, g => g (weight a L) L
  | T + 1, L, g =>
      if total (weight a L) = 0 then expectFrom a T L g
      else ∑ p, weight a L p / total (weight a L) * expectFrom a T (p :: L) g
```

**Exact comparison:** The definition supplies sampling with ratios w_i/W and stopping at W = 0. The equality of each weight to the probability of winning fresh independent comparisons is not part of its type.

### 8.4. `p2-worst-case` — paper lines 57–57

**Paper phrase:**

> an algorithm with query cap $q$ makes at most $q$ queries on every input and every branch of its randomness or measurements

**Lean:** `QuarticQuery.RandomizedProgram.depth` — `QuarticQuery/Statement.lean`; `part/weaker`.

Selected source lines 66–67:

```lean
def RandomizedProgram.depth {ι : Type} (A : RandomizedProgram ι) : ℕ :=
  Finset.univ.sup fun j => (A.tree j).depth
```

**Exact comparison:** This declaration defines the randomized cap only; the same phrase also mentions measurement branches, covered by the accompanying quantum declaration.

**Lean:** `QuarticQuery.AdaptiveProgram.queryCap` — `QuarticQuery/Statement.lean`; `part/weaker`.

Selected source lines 122–127:

```lean
def AdaptiveProgram.queryCap {ι : Type} [Fintype ι] {w : ℕ} :
    AdaptiveProgram ι w → ℕ
  | .output _ => 0
  | .unitary _ next => next.queryCap
  | .query next => 1 + next.queryCap
  | .measure _ yes no => max yes.queryCap no.queryCap
```

**Exact comparison:** This declaration defines the quantum cap only; the same phrase also mentions randomized algorithms, covered by the accompanying randomized declaration.

### 8.5. `p2-free-computation` — paper lines 57–57

**Paper phrase:**

> computation between queries is free

**Lean:** `QuarticQuery.AdaptiveProgram.queryCap` — `QuarticQuery/Statement.lean`; `part/weaker`.

Enclosing declaration type or definition, lines 122–127:

```lean
def AdaptiveProgram.queryCap {ι : Type} [Fintype ι] {w : ℕ} :
    AdaptiveProgram ι w → ℕ
  | .output _ => 0
  | .unitary _ next => next.queryCap
  | .query next => 1 + next.queryCap
  | .measure _ yes no => max yes.queryCap no.queryCap
```

Selected source lines 125–125:

```lean
  | .unitary _ next => next.queryCap
```

**Exact comparison:** The displayed definition makes quantum unitary steps free; it does not separately state the classical decision-tree convention.

### 8.6. `p2-sign-coordinate` — paper lines 67–67

**Paper phrase:**

> we read bit $a$ of block $j$ as the sign $z_j(a)=(-1)^{a}$

**Lean:** `QuarticQuery.bitSign` — `QuarticQuery/Statement.lean`; `defines/different`.

Selected source lines 164–164:

```lean
def bitSign (b : Bool) : ℤ := if b then -1 else 1
```

**Exact comparison:** Lean applies bitSign to the stored Bool z (j,a); the printed exponent a denotes the coordinate in z_j(a), so the displayed formula omits the input value.

### 8.7. `p2-integer-width` — paper lines 71–71

**Paper phrase:**

> on integers of $O_k(\ell)$ bits

**Lean:** `QuarticQuery.Paper.construction_circuit_width` — `QuarticQuery/Paper/ConstructionForrelationCircuit.lean`; `part/weaker`.

Selected source lines 85–86:

```lean
theorem construction_circuit_width (l t : ℕ) (ht : 1 ≤ t) :
    widthTop l t + 1 ≤ (3 * l + 5) * (2 * t) := by
```

**Exact comparison:** Lean proves logarithmic width for the modular circuit registers; this theorem does not identify every stored intermediate with an overflow-free signed integer.

### 8.8. `q4-decode-two` — paper lines 123–123

**Paper phrase:**

> For $i\ne j$, decode addresses $s$ for $i$ and $t$ for $j$, each in its own workspace.

**Lean:** `QuarticQuery.Paper.quantumDecode` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 33–35:

```lean
theorem quantumDecode (hk : 1 ≤ k) (n : ℕ) (i : Col t) :
    Samples (addrCost k t n) fun (x : BitInput (Loc k t C)) s =>
      addrLaw n x i s :=
```

**Exact comparison:** The theorem supplies a coherent decoder for any one column i. Two independent address registers require composing two such decoders; their joint preparation is not the conclusion of this one declaration.

### 8.9. `q4-comparison-cost` — paper lines 130–130

**Paper phrase:**

> One comparison, or its inverse, uses $c=O_k(r\log(r/\varepsilon)+\ell)$ queries.

**Lean:** `QuarticQuery.Paper.quantumComparison_query_bound` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 267–272:

```lean
theorem quantumComparison_query_bound (ht : 1 ≤ t) {ε : ℝ}
    (hε : 0 < ε) (hε1 : ε ≤ 1) :
    ((2 * cmpCost k t (repetitions k (ε / (40 * t : ℕ))) : ℕ) : ℝ) ≤
      160 * (t : ℝ) * (k : ℝ) *
        (1 + 16 * (2 : ℝ) ^ (10 * k) * Real.log ((40 * t : ℕ) / ε)) +
      8 * (t : ℝ) + 4 := by
```

**Exact comparison:** The theorem gives the explicit physical budget for the implemented comparison. It does not by itself state that the inverse circuit has the same budget.

**Lean:** `QuarticQuery.Paper.quantumComparison_state` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 218–223:

```lean
theorem quantumComparison_state (hk : 1 ≤ k) (n : ℕ) (i j : Col t) :
    ∃ (Z : Type) (_ : Fintype Z) (o : Z) (out : Z → Bool)
      (F : BitInput (Loc k t C) → Reg Z ≃ₗᵢ[ℂ] Reg Z),
      IsCirc (cmpCost k t n) F ∧
      IsCirc (cmpCost k t n) (fun x => (F x).symm) ∧
      ∀ x b, lawOf (F x (rket o)) out b = bern (cmpProb n x i j) b := by
```

**Exact comparison:** The theorem supplies forward and inverse circuits with equal logical read counts. It does not itself give the logarithmic estimate or convert those reads to physical bit queries.

### 8.10. `q4-probability-weight` — paper lines 136–136

**Paper phrase:**

> With probabilistic comparisons we weight each candidate by the probability of being selected over every previous pivot in fresh, independent comparisons.

**Lean:** `QuarticQuery.Paper.quantumWeight_product` — `QuarticQuery/Paper/QuantumTournamentFacts.lean`; `part/weaker`.

Selected source lines 88–89:

```lean
theorem quantumWeight_product {Col : Type} (a : Col → Col → ℝ) (L : List Col) (i : Col) :
    weight a L i = (L.map fun p => a i p).prod := by
```

**Exact comparison:** The theorem identifies recursive weights with a product of comparison entries. It does not identify that product with a probability of independent quantum outcomes.

**Lean:** `QuarticQuery.Paper.tensor_success_mass` — `QuarticQuery/Paper/QuantumTensor.lean`; `part/weaker`.

Selected source lines 164–167:

```lean
theorem tensor_success_mass {Z : Type} [Fintype Z]
    (ψ : ℕ → Reg Z) (out : ℕ → Z → Bool) (t : ℕ) :
    lawOf (tensorVector ψ t) (tensorGood out t) true =
      ∏ b ∈ Finset.range t, lawOf (ψ b) (out b) true := by
```

**Exact comparison:** The theorem factors success mass for independent register vectors. It does not identify those individual masses with the a_ij entries or define the candidate weights.

### 8.11. `q4-weights-display` — paper lines 137–139

**Paper phrase:**

> $$
>  w_i=\prod_{h=1}^n a_{i\rho_h},\qquad W=\sum_i w_i.
> $$

**Lean:** `QuarticQuery.Tournament.weight` — `QuarticQuery/Tournament/Ideal.lean`; `part/weaker`.

Selected source lines 35–37:

```lean
@[expose] def weight (a : ι → ι → ℝ) : List ι → ι → ℝ
  | [], _ => 1
  | p :: L, i => weight a L i * a i p
```

**Exact comparison:** This definition supplies only w_i, including its product update. It does not define the displayed total W; that is the separate total declaration.

**Lean:** `QuarticQuery.Tournament.total` — `QuarticQuery/Tournament/Ideal.lean`; `part/weaker`.

Selected source lines 32–32:

```lean
@[expose] noncomputable def total (w : ι → ℝ) : ℝ := ∑ i, w i
```

**Exact comparison:** This definition supplies only W = sum_i w_i. It does not define the individual product weights displayed in the same formula.

### 8.12. `q4-pivot-zero` — paper lines 141–141

**Paper phrase:**

> the new weight of $j$ is zero.

**Lean:** `QuarticQuery.Tournament.weight` — `QuarticQuery/Tournament/Ideal.lean`; `part/weaker`.

Selected source lines 35–37:

```lean
@[expose] def weight (a : ι → ι → ℝ) : List ι → ι → ℝ
  | [], _ => 1
  | p :: L, i => weight a L i * a i p
```

**Exact comparison:** The recursive definition supplies the multiplication update. The conclusion that the new pivot’s weight is zero additionally needs the self_zero field of IsComparison.

**Lean:** `QuarticQuery.Tournament.IsComparison` — `QuarticQuery/Statement.lean`; `part/weaker`.

Selected source lines 302–304:

```lean
structure Tournament.IsComparison {ι : Type} (a : ι → ι → ℝ) : Prop where
  complementary : ∀ i j, i ≠ j → a i j + a j i = 1
  self_zero : ∀ i, a i i = 0
```

**Exact comparison:** The structure supplies the zero-diagonal assumption and complementarity. It does not define or carry out the weight update; multiplying by a_jj = 0 uses the separate weight definition.

**Local reading cue:** The zero diagonal is an assumption of the generic comparison table.

### 8.13. `q4-orthogonal-labels` — paper lines 156–156

**Paper phrase:**

> and states with distinct labels are orthogonal.

**Lean:** `QuarticQuery.Upper.lawOf_sigma` — `QuarticQuery/Upper/Sampler.lean`; `part/weaker`.

Selected source lines 58–60:

```lean
theorem lawOf_sigma {Γ : Type} [Fintype Γ] {Zf : Γ → Type} [∀ c, Fintype (Zf c)]
    (ψ : Reg (Σ c, Zf c)) (out : (Σ c, Zf c) → β) (b : β) :
    lawOf ψ out b = ∑ c, lawOf (slice c ψ) (fun z => out ⟨c, z⟩) b := by
```

**Exact comparison:** The theorem states additivity of measured masses over distinct labelled blocks, the probability consequence of orthogonality. It does not state an inner-product equality between distinct label vectors.

### 8.14. `q4-ideal-label-law` — paper lines 163–163

**Paper phrase:**

> The flagged branch therefore samples the next pivot from the ideal law, without the algorithm knowing any $a_{ij}$.

**Lean:** `QuarticQuery.Paper.equation_15_conditional_index` — `QuarticQuery/Paper/QuantumTensor.lean`; `part/weaker`.

Selected source lines 272–282:

```lean
theorem equation_15_conditional_index {Col Z : Type} [Fintype Col] [Nonempty Col]
    [Fintype Z] (ψ : Col → ℕ → Reg Z) (out : Col → ℕ → Z → Bool) (t : ℕ)
    (v : Reg (Σ _ : Col, TensorBasis Z t))
    (hv : ∀ i, slice i v =
      (((Real.sqrt ((Fintype.card Col : ℝ)⁻¹) : ℝ) : ℂ) • tensorVector (ψ i) t))
    (hW : 0 < ∑ i, ∏ b ∈ Finset.range t, lawOf (ψ i b) (out i b) true) (i : Col) :
    0 < (∑ j, lawOf v (tensorIndexOut out t) (some j)) ∧
    lawOf v (tensorIndexOut out t) (some i) /
        (∑ j, lawOf v (tensorIndexOut out t) (some j)) =
      (∏ b ∈ Finset.range t, lawOf (ψ i b) (out i b) true) /
        (∑ j, ∏ b ∈ Finset.range t, lawOf (ψ j b) (out j b) true) := by
```

**Exact comparison:** The theorem gives the exact conditional product-weight law under hv and hW > 0. It does not by itself exhibit the query circuit or express the absence of stored numerical a_ij values.

**Local reading cue:** The exact conditional law follows from the prepared state, without estimated comparison probabilities.

### 8.15. `q4-amplifier-cap` — paper lines 165–165

**Paper phrase:**

> For $0<\gamma\le1/2$ and $0<\eta<1/2$ there is a procedure making $O(\gamma^{-1/2}\log(1/\eta))$ calls to $A$ and $A^{-1}$ on every branch, for every $p$, that either reports failure or produces a successful outcome.

**Lean:** `QuarticQuery.Amplification.bounded_amplification` — `QuarticQuery/Amplification/Bounded.lean`; `part/weaker`.

Selected source lines 242–257:

```lean
theorem bounded_amplification {γ η : ℝ} (hγ : 0 < γ) (hγ1 : γ ≤ 1 / 2) (hη : 0 < η)
    (hη1 : η < 1 / 2) :
    (amplify γ η).callCap ≤ trialCount η * (2 * iterationBound γ + 1) ∧
    ((amplify γ η).callCap : ℝ) ≤ 138 * (Real.sqrt γ)⁻¹ * Real.log (1 / η) ∧
    ∀ {H : Type u} [NormedAddCommGroup H] [InnerProductSpace ℂ H] (A : Preparation H),
      (amplify γ η).successProb A + (amplify γ η).failProb A = 1 ∧
      (∀ h : Option H → ℝ, PhaseInvariant h →
        (amplify γ η).expect A h A.zero =
          (amplify γ η).successProb A * h (some A.goodState) +
          (amplify γ η).failProb A * h none) ∧
      (∀ k : H → ℝ, (∀ c : ℂ, ‖c‖ = 1 → ∀ v, k (c • v) = k v) →
        (amplify γ η).successProb A ≠ 0 →
        (amplify γ η).conditional A k = k A.goodState) ∧
      (amplify γ η).wrongStateMass A = 0 ∧
      (γ ≤ A.prob → (amplify γ η).failProb A ≤ η) ∧
      (A.prob = 0 → (amplify γ η).failProb A = 1) := by
```

**Exact comparison:** The all-branch call bound and successful-state assertions are stated for the abstract Proc model, not an AdaptiveProgram on the bit oracle. The separate physical label-law theorem supplies the implemented sampler contract.

**Local reading cue:** The abstract procedure has a uniform all-branch call cap; its physical label implementation is a separate theorem.

### 8.16. `q4-amplifier-label` — paper lines 165–165

**Paper phrase:**

> Conditional on success, the measured label has the same distribution as in the successful part of $A$'s state.

**Lean:** `QuarticQuery.Paper.quantum_amplified_label_law` — `QuarticQuery/Paper/QuantumAmplification.lean`; `part/weaker`.

Selected source lines 202–210:

```lean
theorem quantum_amplified_label_law {ι β : Type} [Fintype ι] [Inhabited ι] [Fintype β]
    {n : ℕ} {L : BitInput ι → Option β → ℝ} (h : Samples n L)
    {γ η : ℝ} (hγ : 0 < γ) (hη : 0 < η) :
    ∃ f : BitInput ι → ℝ,
      (∀ x, 0 ≤ f x ∧ f x ≤ 1) ∧
      (∀ x, γ ≤ ∑ b, L x (some b) → f x ≤ η) ∧
      (∀ x, ∑ b, L x (some b) = 0 → f x = 1) ∧
      Runs (trialCount η * (2 * ((2 * iterationBound γ + 1) * n)))
        (fun x => ampLaw (f x) (fun b => L x (some b))) :=
```

**Exact comparison:** The type supplies a physical program with output law ampLaw, but does not itself display the conditional-law equality. That equality also needs the positive-success hypotheses stated in quantum_amplified_conditional.

**Local reading cue:** Supplies the physical program realizing the preserved label law.

### 8.17. `q4-grover-plane` — paper lines 167–167

**Paper phrase:**

> The label law is preserved because each Grover iteration rotates within the plane spanned by the successful and unsuccessful components of $A$'s state, and so leaves the direction of the successful component unchanged.

**Lean:** `QuarticQuery.Paper.quantum_grover_state` — `QuarticQuery/Paper/QuantumAmplification.lean`; `states/weaker`.

Selected source lines 38–50:

```lean
theorem quantum_grover_state (A : Preparation H) (h0 : 0 < A.prob) (h1 : A.prob < 1) :
    (0 < A.angle ∧ A.angle < Real.pi / 2) ∧
    ‖A.goodState‖ = 1 ∧ ‖A.badState‖ = 1 ∧
    A.good A.goodState = A.goodState ∧ A.good A.badState = 0 ∧
    inner ℂ A.goodState A.badState = 0 ∧
    A.state = ((Real.sin A.angle : ℝ) : ℂ) • A.goodState +
      ((Real.cos A.angle : ℝ) : ℂ) • A.badState ∧
    ∀ ℓ : ℕ,
      A.iterate ℓ =
        ((Real.sin ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.goodState +
        ((Real.cos ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.badState ∧
      (A.good (A.iterate ℓ) ≠ 0 →
        PhaseEq (normalised (A.good (A.iterate ℓ))) A.goodState) := by
```

**Exact comparison:** The displayed geometric theorem requires h0 : 0 < A.prob and h1 : A.prob < 1; its direction conclusion also requires a nonzero successful component. The normalized successful vectors agree up to global phase (PhaseEq). At p = 0 there is no conditional successful direction; at p = 1 the two-dimensional formulation degenerates.

### 8.18. `q4-sampling-guarantee` — paper lines 169–169

**Paper phrase:**

> Before the winner is listed the flag probability $W/m$ exceeds $1/(2m)$

**Lean:** `QuarticQuery.Tournament.half_lt_total` — `QuarticQuery/Tournament/Ideal.lean`; `part/weaker`.

Selected source lines 254–257:

```lean
theorem half_lt_total {a : ι → ι → ℝ} {ε : ℝ} {s : ι} (ha : UnitValued a)
    (hε0 : 0 ≤ ε) (hε : ε ≤ 1) (hd : Dominant a ε s) {T : ℕ} (hT : (T : ℝ) * ε < 1 / 2)
    (L : List ι) (hlen : L.length ≤ T) (hs : s ∉ L) :
    1 / 2 < total (weight a L) :=
```

**Exact comparison:** The theorem supplies W > 1/2 while the dominant candidate is absent. It does not identify the preparation’s flag probability as W/m; division by positive m uses that separate law.

**Lean:** `QuarticQuery.Paper.quantumStage_success` — `QuarticQuery/Paper/QuantumTournamentFacts.lean`; `part/weaker`.

Selected source lines 158–167:

```lean
theorem quantumStage_success {Col : Type} [Fintype Col] [Nonempty Col]
    (a : Col → Col → ℝ) (ha : UnitValued a)
    (L : List Col) (hW : 0 < total (weight a L)) :
    (∀ o, 0 ≤ stageLaw a L o) ∧
    (∑ o, stageLaw a L o) = 1 ∧
    (0 < ∑ i, stageLaw a L (some i)) ∧
    (∀ i, stageLaw a L (some i) = weight a L i / Fintype.card Col) ∧
    (∑ i, stageLaw a L (some i)) = total (weight a L) / Fintype.card Col ∧
    (∀ i, stageLaw a L (some i) / (∑ j, stageLaw a L (some j)) =
      weight a L i / total (weight a L)) := by
```

**Exact comparison:** The theorem identifies the flag probability as W/m when W > 0. It does not supply W > 1/2 while the dominant candidate is absent.

### 8.19. `q4-amplified-stage` — paper lines 169–169

**Paper phrase:**

> each stage fails with probability at most $\varepsilon$ and otherwise appends a pivot drawn exactly from the ideal law.

**Lean:** `QuarticQuery.Paper.quantum_amplify_samples` — `QuarticQuery/Paper/QuantumAmplification.lean`; `part/weaker`.

Selected source lines 355–361:

```lean
theorem quantum_amplify_samples {n : ℕ} {L : BitInput ι → Option β → ℝ} (h : Samples n L) {γ η : ℝ}
    (hγ : 0 < γ) (hη : 0 < η) : ∃ f : BitInput ι → ℝ,
      (∀ x, 0 ≤ f x ∧ f x ≤ 1) ∧
      (∀ x, γ ≤ ∑ b, L x (some b) → f x ≤ η) ∧
      (∀ x, ∑ b, L x (some b) = 0 → f x = 1) ∧
      Samples (trialCount η * ((2 * iterationBound γ + 1) * n))
        fun x => ampLaw (f x) fun b => L x (some b) := by
```

**Exact comparison:** The theorem supplies the coherent amplifier’s failure guarantee and proportional successful-label law once its threshold hypothesis holds. It does not identify those label weights with the ideal pivot weights or append the label to a list.

**Lean:** `QuarticQuery.Paper.quantumStage_success` — `QuarticQuery/Paper/QuantumTournamentFacts.lean`; `part/weaker`.

Selected source lines 158–167:

```lean
theorem quantumStage_success {Col : Type} [Fintype Col] [Nonempty Col]
    (a : Col → Col → ℝ) (ha : UnitValued a)
    (L : List Col) (hW : 0 < total (weight a L)) :
    (∀ o, 0 ≤ stageLaw a L o) ∧
    (∑ o, stageLaw a L o) = 1 ∧
    (0 < ∑ i, stageLaw a L (some i)) ∧
    (∀ i, stageLaw a L (some i) = weight a L i / Fintype.card Col) ∧
    (∑ i, stageLaw a L (some i)) = total (weight a L) / Fintype.card Col ∧
    (∀ i, stageLaw a L (some i) / (∑ j, stageLaw a L (some j)) =
      weight a L i / total (weight a L)) := by
```

**Exact comparison:** The theorem supplies the unamplified stage’s joint, total and conditional probabilities. It does not bound amplified failure or update the returned list.

**Lean:** `QuarticQuery.Paper.quantumListLaw` — `QuarticQuery/Paper/QuantumTournament.lean`; `part/weaker`.

Selected source lines 75–79:

```lean
noncomputable def quantumListLaw (a : Col → Col → ℝ) (g : List Col → ℝ) :
    ℕ → List Col → List Col → ℝ
  | 0, L, out => pt L out
  | n + 1, L, out => g L * pt L out +
      (1 - g L) * ∑ p, weight a L p / total (weight a L) * quantumListLaw a g n (p :: L) out
```

**Exact comparison:** The definition supplies stopping on failure and prepending a successful pivot according to weight divided by total weight. It does not bound the failure function g L by epsilon or provide the coherent implementation.

### 8.20. `q4-fresh-address` — paper lines 178–178

**Paper phrase:**

> For each listed column, decode a fresh address with error at most $\varepsilon$ on promised inputs and measure it.

**Lean:** `QuarticQuery.Paper.quantumVerify_runs` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 355–358:

```lean
theorem quantumVerify_runs (hk : 1 ≤ k) (n cS : ℕ)
    (f : Col t → Addr t → BitInput (Loc k t C) → ℝ)
    (hRun : ∀ c s, Runs cS fun x b => bern (f c s x) b) (c : Col t) :
    Runs (2 * addrCost k t n + cS) fun x b => bern (verifyProb n f x c) b := by
```

**Exact comparison:** The theorem implements fresh decoding followed by fixed-address verification with an all-input cap. It assumes component verifier programs and does not state the decoder’s promised-input error bound.

**Lean:** `QuarticQuery.Paper.quantumDecode_correct` — `QuarticQuery/Paper/QuantumComparison.lean`; `part/weaker`.

Selected source lines 54–59:

```lean
theorem quantumDecode_correct (hk : 1 ≤ k) (ht : 1 ≤ t)
    {n : ℕ} {ε : ℝ} (hε : 0 < ε) (hε1 : ε ≤ 1)
    (hn : repetitions k (ε / (40 * t : ℕ)) ≤ n)
    {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t}
    (hs : ∀ h, P k t (readA x i h) = some (s h)) :
    1 - ε ≤ addrLaw n x i s :=
```

**Exact comparison:** The theorem bounds the promised-input address error under hs and hn. It does not state that verification uses a fresh measured address or provide the subsequent verifier program.

### 8.21. `q4-uniform-test-dichotomy` — paper lines 178–178

**Paper phrase:**

> At this fixed address $s$, a uniformly chosen test of the $K$ tests in (2) fails with probability zero if all tests pass and at least $1/K$ otherwise.

**Lean:** `QuarticQuery.Upper.testLaw_pass` — `QuarticQuery/Upper/Verify.lean`; `part/weaker`.

Selected source lines 62–64:

```lean
theorem testLaw_pass {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t}
    (h : ∀ e, localTest C (2 * t) (40 * t) x i s e = true) :
    ∑ b, testLaw x i s (some b) = 0 := by
```

**Exact comparison:** This theorem supplies only the all-tests-pass case: successful failed-test mass is zero. The positive lower bound when a test fails is a separate theorem.

**Lean:** `QuarticQuery.Upper.testLaw_fail` — `QuarticQuery/Upper/Verify.lean`; `part/weaker`.

Selected source lines 68–70:

```lean
theorem testLaw_fail {x : BitInput (Loc k t C)} {i : Col t} {s : Addr t} {e₀ : Tests t C}
    (h : localTest C (2 * t) (40 * t) x i s e₀ = false) :
    (Fintype.card (Tests t C) : ℝ)⁻¹ ≤ ∑ b, testLaw x i s (some b) := by
```

**Exact comparison:** This theorem supplies only the case with a failed test e0: failed-test mass is at least 1/K. The zero-mass case when all tests pass is a separate theorem.

### 8.22. `c5-joint-event-chain` — paper lines 241–245

**Paper phrase:**

> $$
>  \Pr[i\text{ light and query }\tau\text{ is in }B_{i,s_i}]
>  \ \le\ \Pr[\text{predictor outputs }s_i]\ \le\ \beta^r.
> \tag{9}
> $$

**Lean:** `QuarticQuery.Paper.avg_reachedCellAt_le` — `QuarticQuery/Paper/ClassicalPlanted.lean`; `part/weaker`.

Enclosing declaration type or definition, lines 295–301:

```lean
theorem avg_reachedCellAt_le {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ} {ρ : ℝ}
    (hμ : ∀ x, 0 ≤ μ x) (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (hguess : ∀ U : OutTree (Fin r × κ) (Fin r → Bool), (U.capped fun _ => L) →
      guessSuccess f (fun _ => μ) U ≤ ρ)
    (T : QueryTree (BitLoc ℓ r S κ)) (J : Column ℓ → Column ℓ)
    (A : Column ℓ → Fin r → BitInput κ) (i : Column ℓ) (t : ℕ) :
    avg (prodW μ) (fun U => reachedCellAt f L T J (Function.update A i U) i t) ≤ ρ := by
```

Selected source lines 305–333:

```lean
  calc avg (prodW μ) (fun U => reachedCellAt f L T J (Function.update A i U) i t)
      ≤ guessSuccess f (fun _ => μ) sim := by
        refine sum_le_sum fun U _ => ?_
        change prodW μ U * reachedCellAt f L T J (Function.update A i U) i t ≤
          prodW μ U *
            (if ∀ h, f (U h) = some (sim.eval (Function.uncurry U) h) then 1 else 0)
        have hnonneg : 0 ≤ prodW μ U := prodW_nonneg hμ U
        by_cases hz : prodW μ U = 0
        · simp only [hz, zero_mul, le_refl]
        have hprom : ∀ h, promised f (U h) := fun h =>
          hdom _ (ne_zero_of_prodW_ne_zero hz h)
        set x : BitInput (BitLoc ℓ r S κ) := dummy J (Function.update A i U) with hx
        by_cases hev : ¬ HeavyColumn L T (Function.update A i U) J i ∧
            ∃ q, (T.path x)[t]? = some q ∧
              cellOf q = some (i, trueAddr f (Function.update A i U i))
        · obtain ⟨hnh, q, hq, hcell⟩ := hev
          rw [Function.update_self] at hcell
          have hc : ((T.path x).take t).countP (fun q => (aTarget i q).isSome) ≤ L :=
            ((List.take_sublist t _).countP_le).trans (not_lt.mp hnh)
          have hs : sim.eval (Function.uncurry U) = trueAddr f U :=
            eval_simTree x (Function.uncurry U) (fun _ hq' => dummy_update_of_aTarget_none hq')
              (fun _ _ hq' => dummy_update_of_aTarget_some hq') T t L hq
              (cellGuess_of_cellOf hcell) hc
          have hone : ∀ h, f (U h) = some (sim.eval (Function.uncurry U) h) := fun h => by
            rw [hs]
            exact f_eq_trueAddr (hprom h)
          have hevent : reachedCellAt f L T J (Function.update A i U) i t = 1 :=
            ind_true ⟨hnh, q, hq, by rw [Function.update_self]; exact hcell⟩
          simp only [hevent, if_pos hone, mul_one, le_refl]
```

**Exact comparison:** The highlighted proof establishes the first inequality, joint light-hit probability at most simulator success, for each fixed outside choice A,J. This excerpt does not state the final beta^r bound under the full dummy law.

**Local reading cue:** Pointwise simulation gives the first inequality before averaging the independent outside data.

**Lean:** `QuarticQuery.Paper.eq_21` — `QuarticQuery/Paper/ClassicalPlanted.lean`; `part/weaker`.

Selected source lines 342–348:

```lean
theorem eq_21 {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : ∑ x, μ x = 1)
    (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (hard : ∀ U : QueryTree κ, U.depth ≤ L → treeSuccess f μ U ≤ 2 / 3)
    (T : QueryTree (BitLoc ℓ r S κ)) (i : Column ℓ) (t : ℕ) :
    avg (prodW (prodW μ)) (fun A => avg (prodW (unif ℓ)) fun J =>
      reachedCellAt f L T J A i t) ≤ ((2 : ℝ) / 3) ^ r := by
```

**Exact comparison:** This theorem gives the first-to-last inequality with beta=2/3 under the full dummy law. It omits the middle quantity, the predictor's success probability.

**Local reading cue:** The combined joint-event bound after averaging outside data and applying the capped direct-product estimate.

### 8.23. `e-ratio-display` — paper lines 266–271

**Paper phrase:**

> $$
>  \frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
>  \ \ge\ \frac{1}{400(1+C_k)^\alpha}\,
>  \frac{m^{2-1/k-\alpha/2}}{(\log_2 m)^{2+6\alpha}}
>  \ \longrightarrow\ \infty.
> $$

**Lean:** `QuarticQuery.eventually_gt_rpow` — `QuarticQuery/Results/Exponent.lean`; `part/weaker`.

Selected source lines 118–123:

```lean
theorem eventually_gt_rpow {c C D s α : ℝ} (b : ℕ) {Rt Qt : ℕ → ℝ}
    (hc : 0 < c) (hC : 0 < C) (hD : 0 < D) (hα : 0 ≤ α) (hs : α / 2 < s)
    (hQ0 : ∀ t, 0 ≤ Qt t)
    (hQ : ∀ᶠ t : ℕ in atTop, Qt t ≤ C * 2 ^ t * (2 * (t : ℝ)) ^ b)
    (hR : ∀ᶠ t : ℕ in atTop, c * ((4 : ℝ) ^ t) ^ s / (2 * (t : ℝ)) ^ 2 ≤ Rt t) :
    ∀ᶠ t : ℕ in atTop, D * (1 + Qt t) ^ α < Rt t := by
```

**Exact comparison:** The theorem states eventual R_t>D(1+Q_t)^α for any supplied positive D under the family bounds. It does not state the full displayed pointwise quotient inequality with coefficient 1/[400(1+C_k)^α].

**Local reading cue:** Supplies eventual domination; the exact displayed coefficient is an arithmetic calculation in the text.

### 8.24. `f-gaussian-transform` — paper lines 280–280

**Paper phrase:**

> pairing Gaussian vectors with their Walsh transforms

**Lean:** `QuarticQuery.ForrelationLower.Vc` — `QuarticQuery/ForrelationLower/Walk.lean`; `part/weaker`.

Selected source lines 37–37:

```lean
noncomputable def Vc (u : PC l n → ℝ) (r : ℕ) (b : n) : ℝ := ∑ i, H b i * Uc u r i
```

**Exact comparison:** Vc defines V=HU for an arbitrary finite matrix and coordinate vector. Gaussian sampling and specialization to the Walsh matrix are supplied by the surrounding construction, not this definition.

### 8.25. `f-three-quartic-routes` — paper lines 290–290

**Paper phrase:**

> states the universal quartic bound along three routes with different constants

**Lean:** `QuarticQuery.D_le_Q_pow_four` — `QuarticQuery/Appendix/TheoremA1.lean`; `part/weaker`.

Selected source lines 52–53:

```lean
theorem D_le_Q_pow_four (f : TotalBool (Fin n)) :
    D (totalise f) ≤ 20736 * Q (totalise f) ^ 4 :=
```

**Exact comparison:** This declaration gives the imported route with coefficient 20736; it does not state the other two proof routes.

**Local reading cue:** Imported complexitylib route: 20736.

**Lean:** `QuarticQuery.Paper.appendixA_D_le_Q_pow_four` — `QuarticQuery/Paper/AppendixA.lean`; `part/weaker`.

Selected source lines 61–62:

```lean
theorem appendixA_D_le_Q_pow_four (f : TotalBool (Fin n)) :
    D (totalise f) ≤ 1500625 * Q (totalise f) ^ 4 :=
```

**Exact comparison:** This declaration gives the reconstructed appendix route with coefficient 1500625; it does not state the other two proof routes.

**Local reading cue:** Reconstructed appendix route: 1500625.

**Lean:** `QuarticQuery.Paper.appendixA_D_le_Q_pow_four_hybrid` — `QuarticQuery/Paper/AppendixA.lean`; `part/weaker`.

Selected source lines 105–106:

```lean
theorem appendixA_D_le_Q_pow_four_hybrid (f : TotalBool (Fin n)) :
    D (totalise f) ≤ 19600 * Q (totalise f) ^ 4 :=
```

**Exact comparison:** This declaration gives the hybrid route with coefficient 19600; it does not state the other two proof routes.

**Local reading cue:** Hybrid route: 19600.


## 9. Stronger comparisons

The **26 stronger rows** record actual extra scope, such as arbitrary addressed constructions or $k\ge1$ instead of the paper's $k\ge2$. They do not claim that every theorem with more conjuncts is a stronger version of an unrelated sentence. The exact differences are recorded here and in `fidelity_note`.

| Phrase ID | Declaration | Extra scope |
| --- | --- | --- |
| `a-family` | `QuarticQuery.Paper.construction_family_named` | Lean gives the same family with explicit logarithmic losses, b=6 and c=1/400, and a specified realizing circuit; the abstract suppresses these details. |
| `i-known-quartic-bound` | `QuarticQuery.D_le_Q_pow_four` | Lean supplies the explicit universal coefficient 20736 rather than only asserting existence of a big-O constant. |
| `i-finite-lower` | `QuarticQuery.Paper.prop_4_2` | Lean proves this for every circuit realizing P; the prose discusses the specified circuit family. |
| `p3-overview-unique` | `QuarticQuery.Paper.construction_unique_winner` | Lean proves uniqueness for arbitrary partial functions, circuits and address lengths, not only the Forrelation family. |
| `p3-overview-zero` | `QuarticQuery.winner_finds_zero` | The deterministic pointer conclusion holds for every addressed construction, not only the Forrelation family. |
| `p3-overview-no-incoming` | `QuarticQuery.winner_no_incoming_zero` | Lean quantifies over every rival and every address in an arbitrary addressed construction. |
| `p2-table-decoder` | `QuarticQuery.Paper.construction_lemma_2_1_ii_complete` | Lean supplies the decoder already for k ≥ 1, while this paper fixes k ≥ 2. |
| `p2-table-circuit` | `QuarticQuery.Paper.construction_lemma_2_1_iii` | Lean gives the explicit O_k(m(log₂m)²) size and also covers k = 1. |
| `p2-Phi-delta` | `QuarticQuery.Paper.construction_equation_3` | The matrix-product identity is proved under 1 ≤ k, including the paper's k ≥ 2 range. |
| `p2-negative-promise` | `QuarticQuery.Forrelation.P_eq_none_iff` | Lean characterizes every undefined input; the paper uses the large-negative-value case of that characterization. |
| `p2-lemma-decoder` | `QuarticQuery.Paper.construction_lemma_2_1_ii_complete` | Lean proves this for all k ≥ 1 and every t, while the lemma is stated for fixed k ≥ 2 and sufficiently large powers of four. |
| `p2-lemma-circuit` | `QuarticQuery.Paper.construction_lemma_2_1_iii` | Lean covers k ≥ 1 and every t ≥ 1, so the circuit statement holds for all m = 4^t ≥ 4 rather than only eventually. |
| `p3-all-ones` | `QuarticQuery.winner_no_incoming_zero` | Lean covers all rivals and addresses in every addressed construction, independently of Forrelation. |
| `p3-pointer-valid` | `QuarticQuery.Paper.construction_pointer_encoding` | Lean also proves that every row has exactly one encoding, for every natural ell. |
| `p3-unique` | `QuarticQuery.Paper.construction_unique_winner` | The theorem holds for arbitrary f, C, ell and r; no circuit-realization hypothesis is needed. |
| `p3-transcript-induction` | `QuarticQuery.Paper.construction_transcript_correct` | Lean also states existence and uniqueness of the consistent transcript for every circuit and input. |
| `p3-failed-gate` | `QuarticQuery.Paper.construction_transcript_correct` | The theorem gives an equivalence with the true evaluation and uniqueness; this phrase uses its contrapositive. |
| `p3-nonwinner-every-address` | `QuarticQuery.Paper.construction_local_dichotomy` | Lean proves both winner and nonwinner directions for every partial function and every realizing circuit. |
| `p3-K` | `QuarticQuery.card_testIndex` | The exact count is proved for arbitrary ell, r and S; the paper substitutes m = 2^ell and r = 20ell. |
| `p3-K-growth` | `QuarticQuery.Paper.construction_K_family` | The theorem covers k ≥ 1 and every t ≥ 1 with one B chosen before t. |
| `p3-interface-verification` | `QuarticQuery.Paper.construction_local_dichotomy` | Lean proves the generic two-sided dichotomy for any partial function and realizing circuit. |
| `q4-drift-display` | `QuarticQuery.Tournament.expected_weight_eq` | The Lean identity permits arbitrary real weights and comparison entries; only complementarity, a zero diagonal and W > 0 are required. |
| `q4-half-drift` | `QuarticQuery.Tournament.expected_weight_le_half` | Lean proves the algebraic inequality for arbitrary real weights and comparison entries with IsComparison and W > 0; the probability interpretation additionally uses nonnegative weights. |
| `c5-guess-tail` | `QuarticQuery.twoThirds_pow_le` | Lean bounds the factor (2/3)^(40t) itself by m^(-10) for every natural t. Multiplication by the nonnegative G gives the printed bound at m=4^t, r=40t=20 ell. |
| `e-choose-k` | `QuarticQuery.exists_nat_exponent` | Lean assumes only α<4, so it also covers negative α; its conclusion uses the equivalent inequality α/2<2−1/k. |
| `f-mean-separation` | `QuarticQuery.ForrelationLower.mass_ge` | Lean gives the explicit positive mean gap (1/18)^(k−1), while the prose asserts separation without a constant. |

## 10. Validation and remaining scope

The supplied checker passes on the integrated return. It checks exact quote resolution, non-overlap, formula boundaries, source declaration locations, line containment and required annotation metadata. An additional audit checked fully qualified namespaces, title/note coverage, note lengths, short link-note lengths, obvious truncated nested-let conclusions, omitted definition bodies and source-file integrity. The semantic review separately read the linked source statements and important proof slices; independent section reviews cross-checked the quantum probability/circuit distinctions and the final theorem's quantifiers.

All titles meet the requested 2–12 word limit and all reading notes meet the 40–120 word range. The exact paper SHA-256 is `dbd3a8c83e7961b61f07810557f715f09476160319fca085dcbb636c1d9548b1`. Repeated expressions such as $r=20\ell$ and $K=O_k(m\ell^3)$ are located in their intended paragraphs through the unique section anchors; later occurrences do not make those selections ambiguous. Ranges intended to show a complete theorem extend through its conclusion; definition ranges include the relevant body or fields. Narrow clause and proof-step highlights retain their intentional local scope.

No Lean compilation, dependency-axiom audit, Comparator execution, browser rendering or human-reader study was performed. The deliverable is the reviewed annotation layer and source comparison requested by this packet. All assigned lines were covered; deliberate omissions and the manuscript correction are recorded above.

Final output of `python3 tools/check_return.py <return-folder>` from the supplied packet:

```text
241 ties (240 with Lean), 177 declarations, 8 topics, 0 removed
PASS
```
