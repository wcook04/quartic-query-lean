# Quartic exposition: phrase links and cold-reader review

## Result and scope

This is a complete annotation return for **all of `paper/exposition.md`, lines 1–688**, in packet `09_quartic_exposition`. The source snapshot is commit `f192def14f95a3aff7da5866f35be7b565595e1d`. The five returned files are `ties.json`, `topics.json`, `titles.json`, `notes.json`, and this review. The paper and Lean source are unchanged.

The return contains **309 phrase ties, 375 declaration links, 239 distinct declarations across 57 source files, and nine topics**. Titles contain 4–12 words; notes contain 48–85 words. The median selected phrase is 79 characters and the longest is 322 characters. These counts describe the annotation, not a degree of mathematical verification.

The main editorial decision is to make each click answer the question raised by its own phrase. A definition should identify an object. A probability statement should name the event, distribution, and necessary conditions. A resource bound should say what is counted. A theorem about a measured output should not be presented as a theorem identifying an entire retained state. These distinctions make the material easier to learn and make the correspondence more honest.

There is no phrase-layer seed for this paper. All returned ties therefore have status `new`, and `removed` is empty. The 34 existing coarse selections were reviewed as navigation aids; their IDs are not misrepresented as seed phrase IDs. Their disposition is recorded below. The accompanying trace explains the intended four-layer reader pattern and the existing site work; it is historical context, not evidence that this return has been installed on the live site.

### What this review establishes

The review compares the supplied prose with the actual declaration types and relevant definitions or proof passages. It follows the Physlib exemplar's phrase, topic, title, and note layers. It does not infer fidelity from a matching name or a historical review label. Each non-`same` row has a local explanation; every `weaker` or `different` comparison is reproduced later with its exact paper quotation and Lean source.

No Lean build or new proof was attempted. In particular, the header of `Paper/ConstructionForrelationSharp.lean` describes its sharp physical witnesses as conditional on native elaboration of the one-query compiler. This review can report those supplied theorem statements and their source dependencies; it cannot certify that elaboration. The supplied checker tests the annotation structure and locations, not semantic equivalence or kernel acceptance.

This is a source-informed editorial assessment of what an unfamiliar reader would need, rather than an observed experiment with an independent human reader. The relevant source and historical review were available during the assessment. The packet does not include the referenced SVG figure assets or the separate reasoning record that defines the small teaching circuit. Neither those graphics nor the live reader interface was rendered in this task.

## 1. The distinctions a cold reader needs

### 1.1 A guessed address, a true address, and a valid certificate

These are the three objects most likely to become one vague idea in a reader's mind. The annotations keep them separate throughout.

| Object | What it means | What it does not establish |
| --- | --- | --- |
| A guessed address | The word returned by the bounded decoder. It returns a word on every input. | The guesses need not be right, and their existence does not establish promise membership. |
| The true address | The word of prescribed partial-function values, available mathematically when every digit is defined. | A definition using `Classical.choose` is not an algorithm that reads the address for free. |
| A valid certificate at a proposed cell | The local tests all pass: gates are consistent, the domain and value outputs are right, and the pointers reach zeros. | A transcript of a computation with domain output zero is not a winning certificate, even if its gates are internally consistent. |

This distinction should be visible at the first click, rather than deferred to a warning at the end. The notes on `PartialBool`, `promised`, `trueAddress`, the decoder, the actual circuit outputs, and the local tests now say which object is being defined or certified. The whole board remains a total Boolean input even when some of its address inputs are outside the promise.

The same principle separates *column* from *column string*. A column also contains address inputs and a large array of cells. A statement that a column's string is all ones says nothing by itself about those other bits. `readA x i h` denotes an entire mathematical string as a function; obtaining it as notation is not a single input query. Likewise, `decide (∃ i s, WinsAt …)` defines the Boolean board function, not an efficient evaluation algorithm.

### 1.2 What a pointer proves, and which column it concerns

A pointer stored in column $i$ that reaches a zero in column $j$ supplies evidence against $j$. Its supplier is $i$; its destination is $j$. The comparison rule uses both directions. The notes make the orientation explicit and give the self-comparison branch its own link, because the later diagonal identity $a_{ii}=0$ depends on it.

The winner theorem needs a correctly selected cell only for the winning column. It imposes no promise on the opponent's address inputs. This is why inaccurate behavior between losing columns does not destroy the tournament. A pairwise comparison, however, does not check all parts of a certificate; the final verifier still has a separate job.

### 1.3 Mathematical weights are not numbers computed by the algorithm

The weights are probabilities used to analyze the sampling law. The algorithm does not first estimate every $w_i$ and then sample from a stored vector of numbers. Its uniform preparation and accept flag generate joint mass $w_i/m$, and conditioning on acceptance yields $w_i/W$ when $W>0$.

This resolves an apparent contradiction in Section 4.2: “Stop if $W=0$” describes the ideal process, whereas the implemented procedure stops when its bounded sampling schedule fails or its list cap is reached. A short wording repair is **“In the ideal process, stop if $W=0$.”** The two procedures now have distinct destinations.

### 1.4 A four-entry amplitude list can abbreviate a larger state

The comparison workspace is retained. In the worked amplification example, the four displayed numbers are coefficients of four complete branches, including their workspace and flags. If $v_i$ denotes the complete normalized branch with column label $i$, those branches are orthogonal because the column labels differ. The reflection is about the full prepared vector in their span. Reflecting only the bare column register would not be the described operation.

The notes distinguish full-state amplitudes from marginal measurement probabilities. A marginal probability for column $i$ is a sum of squared moduli over all workspace configurations with that column label. The source's `State` type permits arbitrary vectors; the algorithm definition separately imposes a unit initial state. The opening measurement sentence would be clearer with “one complete register configuration” in its simple coordinate case, followed by the rule for measuring only one register when that is first needed.

### 1.5 Every probability claim needs its experiment

The classical argument has several different probabilities: a coupled-run disagreement, a marginal acceptance gap, finding an erased zero, visiting a true cell while light, and predicting an entire address. These events must retain their names when the reader opens Lean.

Likewise, fresh comparisons are independent after fixing the input, candidate column, and pivot history. Adaptively chosen later pairs need not be unconditionally independent. And in the direct-product argument, the entire outside-information seed is independent of the entire tuple of target inputs; being independent of each component separately is insufficient.

### 1.6 A cap and a success guarantee have different domains

Every query cap holds on every run, including erroneous runs and inputs outside a promise. Accuracy may require a promised digit, or an acceptance probability at least a threshold. The decoder always returns a digit within its cap; it is accurate under its promise. The amplifier always stops within its cap; its small failure probability requires $q\ge\gamma$. These quantifier orders now appear in the notes themselves.

The same care applies to query units. A test evaluation can require several input-bit queries. A call to a preparation is not automatically one bit query. The verification-search note retains the local-test factor, and the overall budget adds the tournament and verification costs rather than multiplying two nested searches.

## 2. Priority repairs to the exposition

These are recommendations only; no prose has been altered in this return.

### 2.1 Correct the two “only the coefficient of g changes” statements

The Figure 3 caption at line 270 says that only the length of the component along $g$ changes. Appendix A.2, line 567, says that only its coefficient changes. The supplied rotation theorem states

$$
\sin((2u+1)\theta)g+\cos((2u+1)\theta)b.
$$

Both coefficients change. In the paper's own $q=1/4$ example, one step changes them from $(1/2,\sqrt3/2)$ to $(1,0)$. The invariant needed for the conditional column law is the **direction of the accepted component**: all its amplitudes receive one common scalar multiplier.

Suggested replacement for both occurrences:

> The accepted component changes only by a common scalar factor. Conditional on acceptance, the column probabilities therefore remain unchanged.

Both erroneous phrases have `different` links to the exact iterate formula. The classification draws attention to the mismatch; it is not a claim that the preservation of conditional probabilities is false.

### 2.2 Repair the return from Appendix B.1

Section 7.3 sends the reader to Appendix B.1 at line 467. The appendix's final instruction at line 625 returns to Section 7.4. That skips line 473, where the proof takes a union over the at most $G$ query times and establishes $(2/3)^r\le m^{-10}$. Both are needed in the final bound.

The return should rejoin at the final paragraph of Section 7.3, beginning **“For a fixed column $i$…”**. The appendix proves a per-predictor success bound. The reader then needs to see why that yields a bound for any cell query before reading the finishing contradiction. This is a concrete navigation defect with a precise repair, rather than a request for a longer explanation.

### 2.3 Replace an attainment claim by the lower bound actually used

Section 5.3 says that a two-block one-input may produce the measured position with probability “as small as” $\Phi^2=2^{-20}$. The inspected theorem proves $p\ge\delta^2$, not that some input attains equality. In the eight-bit example still active in the reader's mind, $\Phi=N/8$ with integer $N$, so $\Phi=2^{-10}$ cannot occur. This is an elementary inference from the supplied normalization, not a new Lean result.

Suggested replacement:

> On a promised two-block one-input, the promise guarantees a success probability of at least $\delta^2=2^{-20}$. We choose a repetition count that works with this guarantee.

Also replace “The examples have $\Phi=\pm1$” by “The extreme examples have $\Phi=\pm1$,” since the preceding examples include a zero case. A decisive projection outcome for the negative example does not imply that its address digit is defined. The section should signal explicitly when it moves from the eight-bit illustration to general block length.

### 2.4 Qualify the general tournament parameter claim

Line 248 says that “any $T=\log_2m+O(1)$” with $\varepsilon<1/(2T)$ gives a small constant error by the same argument. The ideal bound is $2m/2^T$. If $T=\log_2m+c$, this is $2^{1-c}$; an unspecified bounded additive term need not make it small. The choice $c=0$ yields only the useless bound two. This shows that the stated argument does not justify “any”; it does not prove a lower bound on the actual error for that choice.

For an ideal target error $\delta$, choose $T\ge\lceil\log_2(2m/\delta)\rceil$. The implemented sampler also has accumulated error $T\varepsilon$. A clear repair is:

> A sufficiently large constant added to $\log_2m$ makes the ideal omission probability small. Choosing $\varepsilon$ so that $T\varepsilon$ is small also controls failures of the actual sampler.

The paper's explicit choices already work. The broad “any” sentence is left untied rather than presented as a theorem.

### 2.5 State the missing conditions on whole-address guessing

Section 5.4 says a classical algorithm guessing an address succeeds with probability “about $(2/3)^r$.” The supplied direct-product theorem gives an **upper bound** under independent hard-distribution inputs and a separate $L$-query cap for each input on every branch. An unrestricted algorithm can read everything; the claim needs its restrictions even in a forward summary.

Suggested replacement:

> Under the hard distribution, an algorithm that uses at most $L$ queries to each address input has probability at most $(2/3)^r$ of recovering the whole address.

Section 7 and Appendix B then explain why interleaving the reads does not evade those separate caps. This phrase is linked as `weaker`, with the omitted hypotheses stated locally.

### 2.6 Distinguish the bound in (7.1) from the available averaged endpoint

Display (7.1) bounds the probability that two coupled runs differ. `Paper.eq_23_randomized` bounds the absolute difference of their marginal output-one probabilities. The latter can be strictly smaller: two coupled binary outputs can disagree frequently while their marginal probabilities agree, because disagreements in opposite directions cancel.

The source contains a pointwise first-difference argument and the separate zero and cell estimates needed for the ordinary mathematical assembly. No named theorem was found with the entire coupled-disagreement left-hand side of (7.1). The direct endpoint link is consequently `weaker`; the first-difference sentence has its own precise destination. This is a limitation of the linked endpoint, not a finding that the paper's coupling argument is false.

### 2.7 Keep two small scope issues explicit

The A.3 lower-tail row includes $\exp(-\rho c/8)$. The supplied `binomTail_large` states the weaker $\exp(-\rho c/16)$ bound, which still suffices for the given repetition count. This is an unsupported stronger intermediate claim relative to that source, not evidence that the familiar sharper estimate is mathematically false.

The randomized direct-product endpoint averages a finite seed type, `[Fintype S]`. The prose's coins and side information are unrestricted. The supplied `ExternalRandomness.lean` and `MeasurablePolicies.lean` distinguish their finite results from the arbitrary-measurable-seed transfer. Both relevant prose links report the finite restriction rather than implying that transfer has been supplied.

## 3. What changed in each part of the reading path

### Sections 1–2: models and the total board function

The cost model, state coordinates, normalization, measurement, free gates, phase kickback, and worst-case caps now have separate destinations. Definitions of $R$ and $Q$ are accompanied by the minimum-attainment equivalences, so “least” is not left as an unexplained infimum. The phase-oracle paragraph is connected to the physical bit-oracle theorem with its prepared-minus-register hypothesis visible.

The critical-exponent convention is also explicit. The formal predicate uses nonnegative exponents and $1+Q$, with one constant uniform over all positive input lengths and total functions. The prose writes $Q$ in its definition. For $Q\ge1$ the two bases differ by at most a factor of two, and the constant-query cases can be treated separately. The definition links are marked `different` because the written conventions differ; this is not a challenge to the value four. The introductory assertion for all real $\alpha<4$ also needs an elementary comparison with the $\alpha=0$ case for negative powers beyond the selected nonnegative-ratio theorem.

The board definition is split into stored bit kinds, pointer encoding, proposed gate outputs, prescribed addresses, winning conditions, total output, and uniqueness. At most one winner does not mean every board has a winner. The uniqueness proof does not require a promise on all columns, or circuit correctness. The small two-address-question examples are distinguished from the full parameter choice $r=40t$.

### Sections 3–4: comparisons, weights, and a real list algorithm

The pointer rule, pair ordering, self-discard, and winner dominance receive distinct ties. The drift proof has separate links for pair cancellation, the exact expected-weight identity, the half bound, and its iteration. The fixed-comparison argument is a specialization of the more general weighted identity; no total ordering is assumed.

The quantum preparation is linked to the fresh-tensor-register theorem for all comparisons, not merely to an abstract sampler with the same labels. The amplification links separate geometry, the preserved conditional distribution, a finite schedule, and the actual bounded list law. `Paper.quantumTournament` now supplies the stronger symbolic omission bound $2m/2^T+T\varepsilon$. The notes do not charge the later verifier to that list theorem.

### Sections 5–6: physical decoding and exact verification

The sign conversion, Walsh matrix, norm preservation, signed amplitude, squared measurement probability, physical query budget, repetitions, threshold, and promised accuracy are separate claims. The current sharp source states a $k$-query Walsh witness and a repeated $nk$ decoder with retained transformations. Its elaboration qualification is recorded above; the older review's statement that these interfaces are absent is not copied forward.

`construction_forr_output_bits` supports the actual circuit's domain and value outputs, including the off-promise value convention. The generic `CircuitRealises` interface alone would not justify that convention: it constrains the value output only on the promise. The gate and transcript notes explain why an input wire reads an actual address bit while a predecessor wire reads a claimed transcript bit. The strong-induction argument shows every consistent transcript equals the true one, including arbitrarily many proposed corruptions.

Verification first measures a fresh address and fixes that cell, then searches its exact tests. The nonwinner result quantifies over every proposed cell, so an arbitrary off-promise decoder output cannot defeat soundness. An all-passing certificate is accepted with certainty. On a true board, the $T\varepsilon$ term in the final error analysis comes from tournament sampling; the final address estimate contributes the additional $\varepsilon$. On a false board, $T\varepsilon$ bounds the verifier's false positives over the list. Those different uses now have the correct notes.

### Section 7 and Appendix B: the experiment and the reduction

Independent sampling, the blank board, the selected column, the planted board, and the two Boolean answers have their own links. The discovery-count definition, indicator identity, uniform averaging, conditional unseen-zero law, and final erased-zero bound are separated. The current source supplies these intermediate statements, although its endpoint proof does not use every line of the exposition's early/late discovery argument.

The simulator's note resolves a plausible apparent information leak. Its base board syntactically contains the target strings, but only non-target replies use that board. `dummy_update_of_aTarget_none` shows that changing the target does not affect those replies; actual target reads are charged. Its original-tree clock and per-target read allowance are distinct counters.

Whole-run lightness implies the replay prefix fits the cap, not conversely. A query can occur before later spending makes the column heavy. A correct default address can also increase predictor success without witnessing a true-cell visit. The reduction needs an event inclusion, not equality. These directions of implication are retained in the notes.

Appendix B links the positive-mass history, local consistency sets, conditional product law, optimal remaining success, one-query inequality, unchanged other factors, leaf bound, and finite horizon. “Best success after a query” includes one fewer query left; otherwise the inequality can sound as though learning a bit cannot help. Independence is stated for the entire outside seed and target tuple.

### Section 8: the same family, the right order of limits

The source now has a theorem in the exact form of (8.1), `classical_Fkm_ratio`: an eventual lower envelope, divergence of that envelope, and divergence of the actual ratio, with logarithmic exponent $2+6\alpha$. The annotation uses it rather than a less informative abstract power-separation wrapper.

The order is fixed throughout: choose the proposed $\alpha<4$, choose a fixed $k\ge2$ with $\alpha<4-2/k$, and then increase $m=4^t$. The constants may depend on $k$ but remain fixed in that final limit. Both query bounds use the same circuit and hence the same total function. At fixed $k$, logarithmic losses make the exclusion strict; a table entry of three does not claim that this two-block calculation defeats the endpoint power three.

The universal half is separate from the family half. The source gives the explicit total-function bound $D\le20736Q^4$, and $R\le D$ transfers it to randomized algorithms. The unconditional endpoint has no remaining mathematical hypothesis in its supplied declaration type. This source reading is not a fresh compilation claim.

### Appendices A and E: cost units and retained output

The controlled-read construction, padding, inverse execution, component budgets, additive total, and explicit logarithmic bound are separate links. The two-query controlled-read construction in A.1 remains a correct description of that construction; the newer one-query compiler is not substituted simply because it is sharper. The A.2 schedule links its exact trigonometric average and finite budget, rather than attaching a looser estimate to the sharper display. In A.3 the literal fresh Walsh tensor witness is distinguished from a separately constructed threshold-decoder witness; equal laws do not establish that they are definitionally the same circuit.

Appendix E is calibrated to the current source. `finalB_retained_original` identifies a literal retained original $Z$ factor for a coordinate-success predicate `S : Z → Bool`. `finalB_physical_on_embedding` gives physical compilation of that same coordinate-success construction under a continuation. This is more than a label-only statement. The remaining qualification concerns one endpoint simultaneously combining an arbitrary success projector, physical compilation or uncomputation, and original-output identification. No such full-general endpoint was found. A description of the source should name that exact limitation rather than say merely “states are not retained.”

## 4. Notes written for the moment of uncertainty

The full set is in `notes.json`; the examples below illustrate the editorial standard. Each begins with the mathematical object or claim and then explains the binder or notation that could mislead a new reader.

### The address determined by all prescribed digits

The vector of prescribed answers to the address questions in one column. The binder `hdef : ∀ h, promised f (readA x i h)` requires every digit to be defined before this address can be formed. `Classical.choose` selects the Boolean value whose existence `hdef` asserts; it is a mathematical definition, not a query algorithm. If even one address input is outside the promise, this definition has no such hypothesis available.

### Conditioning on success preserves the label proportions

For nonnegative weights $q_b$ of positive total mass and a failure probability $0\le f<1$, conditioning the amplified law on success gives label $b$ with probability $q_b/\sum_cq_c$. The binders `hq0`, `hq`, `hf0` and `hf1` state those assumptions. In the tournament, $q_i=w_i/m$, so the ratio becomes $w_i/W$. This is a statement about measured labels; it does not identify the full quantum output state.

### The classical-to-quantum cost ratio grows without bound

For the canonical family, fixed $k\ge2$ and $0\le\alpha<4-2/k$, the ratio $R(F)/(1+Q(F))^\alpha$ has the lower bound in (8.1), and both that lower bound and the ratio tend to infinity. Lean writes $k=l+1$; `hk`, `hα` and `hs` give these parameter restrictions. A positive constant `d` is chosen before `t` grows, and the same named circuit defines both complexities.

## 5. Fidelity conventions and exact comparisons

Of the **375 declaration links**, 324 are `same`, 31 `stronger`, 14 `weaker`, and six `different`. These are link counts, not counts of mathematical errors. A `part` or `proof` relation identifies the declaration's contribution; fidelity separately compares the scope of that contribution with the selected prose. A stronger source can cover arbitrary weights or a broader block count; a weaker source can introduce an extra hypothesis even when that hypothesis holds later in the exposition.

The following ledger includes **every weaker or different link**, in reading order. Each entry pairs the exact selected paper text with the actual source header, including its hypotheses and conclusion. Definitions include their defining expression. Namespace and surrounding variable context remain as in the cited file; the associated reading note explains the relevant implicit context. Long proof bodies are not reproduced merely to inflate a source quote. These source paths and line numbers refer to the supplied snapshot.

### `exp-1-phase-oracle` — weaker

**Paper, line 40:**

```text
A query acts on all positions at once: the amplitude attached to position $j$ is multiplied by $(-1)^{x_j}$, where $x_j$ is the bit stored there.
```

**Lean:** `QuarticQuery.Paper.construction_bitOracle_phase_kickback` — `lean/QuarticQuery/Paper/ConstructionPhase.lean`, lines 26–32.

```lean
theorem construction_bitOracle_phase_kickback
    (x : BitInput ι) (ψ : State ι w)
    (hminus : ∀ (i : ι) (z : Fin (w + 1)),
      ψ.ofLp (i, true, z) = -ψ.ofLp (i, false, z))
    (p : Basis ι w) :
    (bitOracle x ψ).ofLp p =
      (if x p.1 then (-1 : ℂ) else 1) * ψ.ofLp p := by
```

**Comparison:** The physical bit-oracle theorem requires hminus, the prepared minus answer register. It does not claim that an arbitrary bit-oracle state acquires only phases; Section 5.2 supplies this preparation.

### `exp-1-all-smaller-powers` — weaker

**Paper, line 65:**

```text
for each power $\alpha<4$, the ratio of $R(f)$ to $(1+Q(f))^\alpha$ can be arbitrarily large
```

**Lean:** `QuarticQuery.Paper.classical_Fkm_ratio` — `lean/QuarticQuery/Paper/ClassicalAsymptotics.lean`, lines 372–386.

```lean
theorem classical_Fkm_ratio (l : ℕ) (hk : 2 ≤ l + 1) {α : ℝ}
    (hα : 0 ≤ α) (hs : α / 2 < 2 - 1 / ((l + 1 : ℕ) : ℝ)) :
    ∃ d : ℝ, 0 < d ∧
      (∀ᶠ t : ℕ in atTop,
        d * (mValue t : ℝ) ^ (2 - 1 / ((l + 1 : ℕ) : ℝ) - α / 2) /
          Real.logb 2 (mValue t : ℝ) ^ (2 + α * 6) ≤
            (R (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ) /
              (1 + (Q (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ)) ^ α) ∧
      Tendsto (fun t : ℕ =>
        d * (mValue t : ℝ) ^ (2 - 1 / ((l + 1 : ℕ) : ℝ) - α / 2) /
          Real.logb 2 (mValue t : ℝ) ^ (2 + α * 6)) atTop atTop ∧
      Tendsto (fun t : ℕ =>
        (R (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ) /
          (1 + (Q (totalise (Fkm (l + 1) t (Forrelation.forrCircuit l t))) : ℝ)) ^ α)
        atTop atTop := by
```

**Comparison:** classical_Fkm_ratio assumes 0 ≤ α and α/2 < 2-1/k for a fixed k≥2; exists_nat_exponent chooses k for α<4. Negative α require the additional monotonicity observation, not stated by this declaration.

### `exp-1-critical-exponent-definition` — different

**Paper, line 65:**

```text
the infimum of the powers $\alpha$ for which $R(f)=O(Q(f)^\alpha)$ holds for all total $f$ the *critical exponent* of $R$ relative to $Q$
```

**Lean:** `QuarticQuery.alphaTot` — `lean/QuarticQuery/Statement.lean`, lines 329–329.

```lean
noncomputable def alphaTot : ℝ := sInf {α : ℝ | UniversalPower α}
```

**Comparison:** alphaTot takes the infimum of nonnegative α satisfying a uniform bound in (1+Q(f))^α; the sentence writes Q(f)^α without that restriction. The positive-Q bases are comparable, but the expressions are not literally identical.

### `exp-1-critical-exponent-definition` — different

**Paper, line 65:**

```text
the infimum of the powers $\alpha$ for which $R(f)=O(Q(f)^\alpha)$ holds for all total $f$ the *critical exponent* of $R$ relative to $Q$
```

**Lean:** `QuarticQuery.UniversalPower` — `lean/QuarticQuery/Statement.lean`, lines 323–326.

```lean
def UniversalPower (α : ℝ) : Prop :=
  0 ≤ α ∧ ∃ C : ℝ, 0 < C ∧
    ∀ n : ℕ, 1 ≤ n → ∀ f : TotalBool (Fin n),
      (R (totalise f) : ℝ) ≤ C * Real.rpow (1 + (Q (totalise f) : ℝ)) α
```

**Comparison:** UniversalPower quantifies 0≤α, one positive C, all positive n and all total f, and uses 1+Q(f) rather than the sentence’s Q(f).

### `exp-1-classical-scale` — different

**Paper, line 70:**

```text
$$
\underbrace{m}_{\text{possible winning columns}}\times\underbrace{m^{1-1/k}}_{\text{reads to learn one hidden address}}=m^{2-1/k}.
$$
```

**Lean:** `QuarticQuery.Paper.construction_equation_two` — `lean/QuarticQuery/Paper/ConstructionFamily.lean`, lines 58–67.

```lean
theorem construction_equation_two (k : ℕ) (hk : 2 ≤ k) :
    ∃ (S : ℕ) (c C : ℝ), 0 < c ∧ 0 < C ∧
      ∃ (b : ℕ), 0 < b ∧ ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
        ∃ Cir : Circuit (ForrelationCoord k t), CircuitRealises Cir (P k t) ∧
          Cir.size ≤ S * mValue t * (2 * t) ^ 2 ∧
          (Q (totalise (Fkm k t Cir)) : ℝ) ≤
            C * Real.sqrt (mValue t : ℝ) * (Real.logb 2 (mValue t : ℝ)) ^ b ∧
          c * Real.rpow (mValue t : ℝ) (2 - 1 / (k : ℝ)) /
              (Real.logb 2 (mValue t : ℝ)) ^ 2 ≤
            (R (totalise (Fkm k t Cir)) : ℝ) := by
```

**Comparison:** The family theorem gives an eventual lower bound c m^(2-1/k)/(log₂m)². It does not assert an exact product cost or the explanatory split of the two factors; this display intentionally suppresses logarithms.

### `exp-1-fourth-power-limit` — different

**Paper, line 73:**

```text
As $k$ grows, $m^{2-1/k}$ approaches $m^2=(\sqrt m)^4$.
```

**Lean:** `QuarticQuery.familyExponent_tendsto` — `lean/QuarticQuery/Results/Exponent.lean`, lines 142–142.

```lean
theorem familyExponent_tendsto : Tendsto familyExponent atTop (nhds 4) := by
```

**Comparison:** The theorem states lim_{k→∞}(4-2/k)=4, a numerical exponent limit. The displayed sentence is about powers of m; fixed-k query bounds and then growing m are a further step.

### `exp-2-pointer-read-budget` — weaker

**Paper, line 99:**

```text
following a pointer costs $\ell+1$ queries: $\ell$ to read the row number and one to read the bit it names.
```

**Lean:** `QuarticQuery.Paper.construction_test_depth` — `lean/QuarticQuery/Paper/ConstructionTests.lean`, lines 39–42.

```lean
theorem construction_test_depth (t : ℕ) (ht : 1 ≤ t)
    {κ : Type} (C : Circuit κ) (r : ℕ) (i : Column (2 * t))
    (s : Address r) (e : TestIndex (2 * t) r C.size) :
    (localTestTree C (2 * t) r i s e).depth ≤ 2 * t + 1 := by
```

**Comparison:** construction_test_depth states an upper bound ≤2t+1 for local tests on m=4^t with t≥1. It is not an equality or a lower bound for every pointer-following procedure.

### `exp-4-independent` — weaker

**Paper, line 194:**

```text
Fresh comparisons are independent of each other.
```

**Lean:** `QuarticQuery.Paper.tensor_success_mass` — `lean/QuarticQuery/Paper/QuantumTensor.lean`, lines 164–167.

```lean
theorem tensor_success_mass {Z : Type} [Fintype Z]
    (ψ : ℕ → Reg Z) (out : ℕ → Z → Bool) (t : ℕ) :
    lawOf (tensorVector ψ t) (tensorGood out t) true =
      ∏ b ∈ Finset.range t, lawOf (ψ b) (out b) true := by
```

**Comparison:** The formal product law concerns a fixed family of fresh tensor-register comparisons. Adaptive choices of later pairs are not asserted to be unconditionally independent.

### `exp-4-survival` — weaker

**Paper, line 246:**

```text
While $i^\star$ is not yet on a list of at most $T$ pivots, its weight is therefore at least $(1-\varepsilon)^T\ge1-T\varepsilon$.
```

**Lean:** `QuarticQuery.Tournament.dominant_weight_lb` — `lean/QuarticQuery/Tournament/Ideal.lean`, lines 239–242.

```lean
theorem dominant_weight_lb {a : ι → ι → ℝ} {ε : ℝ} {s : ι} (ha : UnitValued a)
    (hε0 : 0 ≤ ε) (hε : ε ≤ 1) (hd : Dominant a ε s) {T : ℕ} (hT : (T : ℝ) * ε < 1 / 2)
    (L : List ι) (hlen : L.length ≤ T) (hs : s ∉ L) :
    (1 - ε) ^ T ≤ weight a L s ∧ 1 - (T : ℝ) * ε ≤ (1 - ε) ^ T ∧ 1 / 2 < weight a L s := by
```

**Comparison:** The declaration additionally assumes 0 ≤ ε ≤ 1 and Tε < 1/2 to prove its further strict half bound. The printed product/Bernoulli estimate does not require Tε < 1/2; the later chosen parameters satisfy it.

### `exp-4-caption-direction` — different

**Paper, line 269:**

```text
Only the length of the component along $g$ changes, so the accepted columns keep their relative amplitudes.
```

**Lean:** `QuarticQuery.Amplification.Preparation.iterate_eq` — `lean/QuarticQuery/Amplification/Geometry.lean`, lines 343–346.

```lean
theorem iterate_eq (ℓ : ℕ) :
    A.iterate ℓ =
      ((Real.sin ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.goodState +
      ((Real.cos ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.badState := by
```

**Comparison:** Both coefficients change: sin((2u+1)θ) multiplies g and cos((2u+1)θ) multiplies b. What is preserved is the direction of the accepted component, not the length of the rejected component.

### `exp-5-smallest-probability-wording` — weaker

**Paper, line 343:**

```text
a one-input may give $00$ with probability as small as $\Phi^2=2^{-20}$
```

**Lean:** `QuarticQuery.Forrelation.successProb_of_true` — `lean/QuarticQuery/Forrelation/Repetition.lean`, lines 61–62.

```lean
theorem successProb_of_true (k t : ℕ) (hk : 1 ≤ k) (z : BitInput (ForrelationCoord k t))
    (h : P k t z = some true) : delta k ^ 2 ≤ successProb z := by
```

**Comparison:** Lean proves successProb ≥ delta² for a promised one-input, not existence of an input attaining equality. In the eight-bit case Φ = N/8, so Φ = 2⁻¹⁰ cannot occur.

### `exp-5-capped-address-guessing` — weaker

**Paper, line 358:**

```text
a classical algorithm guessing a whole address succeeds with probability about $(2/3)^r$
```

**Lean:** `QuarticQuery.Paper.classical_direct_product` — `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`, lines 880–884.

```lean
theorem classical_direct_product {f : PartialBool κ} {μ : BitInput κ → ℝ}
    {L : ℕ} {β : ℝ} (hμ : ∀ x, 0 ≤ μ x) (hμ1 : classicalMass μ = 1)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ β)
    (T : OutTree (Fin r × κ) (Fin r → Bool)) (hT : T.capped fun _ => L) :
    guessSuccess f (fun _ => μ) T ≤ β ^ r := by
```

**Comparison:** The bound is at most β^r under a mass-one product hard distribution and a cap of L queries to each input on every branch; set β = 2/3. The phrase omits these restrictions and suggests a rate rather than an upper bound.

### `exp-7-disagreement-bound` — weaker

**Paper, line 406:**

```text
$$
\Pr[\text{the two runs differ}]
\le
\underbrace{\frac{4G}{m^2}}_{\text{find the erased zero}}
+
\underbrace{\frac{G}{mL}}_{\text{read the planted column heavily}}
+
\underbrace{G\Bigl(\frac23\Bigr)^r}_{\text{guess its address while light}}.
\tag{7.1}
$$
```

**Lean:** `QuarticQuery.Paper.eq_23_randomized` — `lean/QuarticQuery/Paper/ClassicalPlanted.lean`, lines 465–474.

```lean
theorem eq_23_randomized {f : PartialBool κ} {μ : BitInput κ → ℝ} {L G : ℕ}
    (tr : BitInput κ → Fin S → Bool) (hL : 1 ≤ L)
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : ∑ x, μ x = 1)
    (hdom : ∀ x, μ x ≠ 0 → promised f x)
    (hard : ∀ U : QueryTree κ, U.depth ≤ L → treeSuccess f μ U ≤ 2 / 3)
    (P : RandomizedProgram (BitLoc ℓ r S κ)) (hP : P.depth ≤ G) :
    |plantedAvg μ f tr (fun x => P.success x true) -
        dummyAvg μ (fun x => P.success x true)| ≤
      4 * (G : ℝ) / ((2 ^ ℓ : ℕ) : ℝ) ^ 2 +
        (G : ℝ) / (((2 ^ ℓ : ℕ) : ℝ) * (L : ℝ)) + (G : ℝ) * ((2 : ℝ) / 3) ^ r := by
```

**Comparison:** The exposition bounds the coupled event that the two runs differ. Lean bounds only the absolute difference of their output-one probabilities, which can be smaller; its type also states the hard-distribution and L≥1 premises explicitly.

### `exp-7-small-discrepancy` — weaker

**Paper, line 417:**

```text
With $G=\lfloor mL/100\rfloor$ the sum is below $1/3$.
```

**Lean:** `QuarticQuery.discrepancy_parameters` — `lean/QuarticQuery/Results/Exponent.lean`, lines 479–482.

```lean
theorem discrepancy_parameters {k t : ℕ} (hk : 2 ≤ k) (ht : 8 ≤ t) :
    4 * (Gvalue (mValue t) (Lvalue k t) : ℝ) / (mValue t : ℝ) ^ 2 +
        (Gvalue (mValue t) (Lvalue k t) : ℝ) / ((mValue t : ℝ) * (Lvalue k t : ℝ)) +
        (Gvalue (mValue t) (Lvalue k t) : ℝ) * ((2 : ℝ) / 3) ^ (40 * t) < 1 / 3 := by
```

**Comparison:** The Lean theorem supplies this inequality for k≥2 and t≥8, with m=4^t and the defined L and G. The preview sentence does not yet state that threshold.

### `exp-7-final-numeric` — weaker

**Paper, line 485:**

```text
the sum is at most $4/100+1/100+1/(100m^8)<1/3$
```

**Lean:** `QuarticQuery.Paper.classical_numeric_components` — `lean/QuarticQuery/Paper/ClassicalAsymptotics.lean`, lines 154–162.

```lean
theorem classical_numeric_components {t : ℕ} {L G : ℝ}
    (hL1 : 1 ≤ L) (hLm : L ≤ (mValue t : ℝ))
    (hG : G ≤ (mValue t : ℝ) * L / 100) :
    4 * G / (mValue t : ℝ) ^ 2 ≤ 4 / 100 ∧
    G / ((mValue t : ℝ) * L) ≤ 1 / 100 ∧
    G * ((2 : ℝ) / 3) ^ (40 * t) ≤ 1 / 100 ∧
    4 * G / (mValue t : ℝ) ^ 2 + G / ((mValue t : ℝ) * L) +
      G * ((2 : ℝ) / 3) ^ (40 * t) ≤ 6 / 100 ∧
    (6 / 100 : ℝ) < 1 / 3 := by
```

**Comparison:** Lean states the weaker third-term bound 1/100 and total bound 6/100<1/3, rather than the displayed sharper third-term bound 1/(100m^8).

### `app-a2-good-direction` — different

**Paper, line 566:**

```text
Only the coefficient of $g$ changes; given a successful measurement, the probabilities of the column numbers are still the squared coordinates in the direction $g$, summed over the other registers.
```

**Lean:** `QuarticQuery.Amplification.Preparation.iterate_eq` — `lean/QuarticQuery/Amplification/Geometry.lean`, lines 343–346.

```lean
theorem iterate_eq (ℓ : ℕ) :
    A.iterate ℓ =
      ((Real.sin ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.goodState +
      ((Real.cos ((2 * ℓ + 1) * A.angle) : ℝ) : ℂ) • A.badState := by
```

**Comparison:** The source changes both coefficients, sin((2u+1)θ) for g and cos((2u+1)θ) for b. The correct invariant is that the accepted component changes only by a scalar.

### `app-a3-large-mean-tail` — weaker

**Paper, line 590:**

```text
At most $\exp(-\rho c/8)$, hence at most $\exp(-\rho c/16)$.
```

**Lean:** `QuarticQuery.Forrelation.binomTail_large` — `lean/QuarticQuery/Forrelation/Repetition.lean`, lines 160–161.

```lean
theorem binomTail_large (n : ℕ) {p c : ℝ} (h1 : p ≤ 1) (hc : 0 < c) (hp : c ≤ p) :
    1 - binomTail n p (n * (c / 2)) ≤ Real.exp (-(n * c / 16)) := by
```

**Comparison:** The theorem bounds the lower tail by exp(-n*c/16); it does not state the sharper exp(-n*c/8) intermediate bound printed here.

### `app-a4-absorbing-the-lower-bound-constant` — weaker

**Paper, line 603:**

```text
Dividing by $m^{1-1/k}/(\log_2m)^2$ gives a factor of order $(\log m)^{1+1/k}$, which tends to infinity and absorbs the constant.
```

**Lean:** `QuarticQuery.Paper.construction_bs_comparison_chain` — `lean/QuarticQuery/Paper/ConstructionForrelationComparison.lean`, lines 84–93.

```lean
theorem construction_bs_comparison_chain (k : ℕ) (hk : 2 ≤ k)
    (c : ℝ) (hc : 0 < c) :
    ∃ t₀ : ℕ, ∀ t : ℕ, t₀ ≤ t →
      (Lvalue k t : ℝ) ≤ (mValue t : ℝ) ^ (1 - 1 / (k : ℝ)) /
        (Real.logb 2 (mValue t : ℝ)) ^ 2 ∧
      (mValue t : ℝ) ^ (1 - 1 / (k : ℝ)) /
          (Real.logb 2 (mValue t : ℝ)) ^ 2 <
        c * (k : ℝ) ^ (-29 : ℤ) *
          ((mValue t : ℝ) / Real.logb 2 ((k : ℝ) * (mValue t : ℝ))) ^
            (1 - 1 / (k : ℝ)) := by
```

**Comparison:** The statement proves the eventual strict comparison for every positive constant c at fixed k ≥ 2. It does not state the ratio asymptotic of order (log m)^(1+1/k).

### `app-b-independent-seed` — weaker

**Paper, line 613:**

```text
The algorithm may also use random coins and other data drawn jointly independently of the inputs.
```

**Lean:** `QuarticQuery.Paper.classical_direct_product_average` — `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`, lines 902–909.

```lean
theorem classical_direct_product_average {S : Type} [Fintype S]
    {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ} {β : ℝ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : classicalMass μ = 1)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ β)
    {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) (hp1 : ∑ s, p s = 1)
    (T : S → OutTree (Fin r × κ) (Fin r → Bool))
    (hT : ∀ s, (T s).capped fun _ => L) :
    ∑ s, p s * guessSuccess f (fun _ => μ) (T s) ≤ β ^ r := by
```

**Comparison:** The source declaration averages over a finite seed type S via [Fintype S]. The prose permits jointly independent coins and data without stating a finite-seed restriction; the arbitrary-measurable-seed transfer is not supplied here.

### `app-b-final-average` — weaker

**Paper, line 625:**

```text
then over the coins and other data proves the bound.
```

**Lean:** `QuarticQuery.Paper.classical_direct_product_average` — `lean/QuarticQuery/Paper/ClassicalDirectProduct.lean`, lines 902–909.

```lean
theorem classical_direct_product_average {S : Type} [Fintype S]
    {f : PartialBool κ} {μ : BitInput κ → ℝ} {L : ℕ} {β : ℝ}
    (hμ : ∀ x, 0 ≤ μ x) (hμ1 : classicalMass μ = 1)
    (hard : ∀ T : QueryTree κ, T.depth ≤ L → treeSuccess f μ T ≤ β)
    {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) (hp1 : ∑ s, p s = 1)
    (T : S → OutTree (Fin r × κ) (Fin r → Bool))
    (hT : ∀ s, (T s).capped fun _ => L) :
    ∑ s, p s * guessSuccess f (fun _ => μ) (T s) ≤ β ^ r := by
```

**Comparison:** The average over coins and other data is explicitly over a finite seed type S in this source theorem; the prose states no such restriction.

## 6. Material left untied and declarations not found

All assigned lines were considered. Untied prose is not an unreported stopping point. It includes history, reading instructions, teaching questions, repeated consequences, and concrete examples for which the packet contains no matching instance. A general correctness theorem is not used to pretend that a particular handwritten gate list, board, or arithmetic trace has been instantiated in Lean.

| Paper range | Coverage and deliberate boundary |
| --- | --- |
| 1–12, front matter and overview | The mathematical headline and universal upper bound are tied. Authorship, provenance, and reading guidance remain prose. |
| 14–90, query model and scale | Definitions, physical phase condition, worst-case costs, universal exponent, family bounds, and exponent arithmetic are tied. The exact sixteen-bit introductory board and its query trace have no matching finite instance selected. The factorized classical cost is marked as explanatory, rather than an exact product-cost theorem. |
| 91–142, board and certificates | Stored positions, addresses, pointers, transcripts, the winner, totality, and uniqueness are tied. The literal small-board fillings and pointer mutations are examples. No complete input-cardinality theorem stating the later $O_k(m^{22}(\log m)^3)$ bound was found. |
| 143–186, comparisons and cycles | The rule and its robustness, cost contributions, and general drift identity are tied. The pictured cycle and its four survivor counts are not replaced by a theorem about some different abstract cycle. The hypothetical nested-search algorithm is not claimed as an implemented source algorithm. |
| 187–251, weights and the three claims | Product weights, conditional sampling, pair cancellation, drift, survival, and omission are tied. The fractional numerical table is not a separate formal instance. No dedicated uniqueness theorem for the proportional sampling law was found. The overbroad “any” parameter statement is reported above. |
| 252–280, coherent sampling | Tensor preparation, flag probabilities, reflections, rotation, preserved conditional law, finite schedule, and actual list law are tied. The exact four-column numerical executions and small-angle heuristic are illustrations. The false caption sentence is explicitly flagged. |
| 281–363, Forrelation | Definitions, promises, matrix identities, final-state and measurement laws, query caps, repetition, whole addresses, and comparisons are tied. The named negative witness has exact source statements. No declarations evaluating the displayed positive/zero strings, full four-vector trace, or the projection exercise were found. |
| 364–402, exact checking and the algorithm | Actual circuit outputs, builders, transcripts, local tests, count and depth, verification soundness, error, and final quantum cost are tied. The particular dishonest $+2$ transcript fragment and modified four-column example are not supplied as finite formal instances. Duplicate orchestration sentences are not all linked to one broad endpoint. |
| 403–491, classical lower bound | The coupling objects, discovery identity, conditional uniformity, heavy-column count, simulator, event containment, product-bound application, and lower-bound endpoint are tied. No literal instance of the $175/256$ counterexample, promised-AND example, or XOR advice example was found. The printed early/late discovery decomposition is not the endpoint theorem's proof route. The full coupled-disagreement endpoint remains distinct from the formal marginal gap. |
| 492–530, exponent four | The exact ratio limit, choice of fixed $k$, table's exclusion conditions, deterministic universal bound, and unconditional conclusion are tied. Elementary arithmetic and the final recap do not receive redundant copies of the same theorem. |
| 531–579, A.1–A.2 | Cost conversions, subroutine and total budgets, geometry, sharp average, schedule, and failure law are tied. No literal theorem presenting the two individual matrices as the paper's matrix pair was selected; their product action and the underlying reflections are linked. |
| 580–606, A.3–A.4 | Repetition, binomial count, needed tail bounds, integer normalization, thresholds, and eventual comparison are tied. The sharper $1/8$ tail and the precise logarithmic ratio order have narrower source support. The separate 180-gate teaching circuit and complete board-cardinality result are not present as matching declarations. |
| 607–648, Appendix B | The direct-product proof's intermediate conditional-law and value statements are tied. The one-query AND calculation and four-query parity instance, including $1/8+1/8=1/4$, have no matching concrete source evaluation. The replay mechanism itself is tied. |
| 649–656, Appendix C | Historical attribution and explanation of earlier certificate approaches are not Lean assertions. No unrelated theorem is substituted for them. |
| 657–674, Appendix D | The answer about the fixed-$k$ exponent is tied to its actual arithmetic and family results. Other numerical answers and explanatory recapitulations are not passed off as newly located finite Lean examples. |
| 675–688, Appendix E and references | Measured-law and retained-factor claims, winner definition, and endpoints are tied at their actual scope. Bibliographic and editorial material stays untied. |

### Two particularly important missing instances

**The 180-gate teaching circuit is not the canonical circuit in the source.** Appendix A.4 cites an absent `reasoning_record.md#AC-example-tests`. It assigns domain output to gate 178 and value output to gate 179, the last gate. The supplied `forrCircuit` instead puts its domain output at `coreSize+2`, the last gate, and its value output at `coreSize`. This is concrete evidence that the numbered teaching circuit is a separate gate list. Its $S=180$, $K=371$, and 5936-bit totals remain unclaimed as Lean instances. Their elementary counting arithmetic is consistent conditional on that circuit, but the generic circuit theorem cannot certify that missing construction.

**The full input-size formula is assembled from components.** The layout theorem counts columns, address coordinates, and address labels; the circuit theorem supplies a gate-size bound. No declaration explicitly stating the complete input cardinality or its final $O_k(m^{22}(\log m)^3)$ growth was found. The review does not equate a component-count theorem with that missing assembled statement. The theorem that both complexity bounds concern one and the same function is present and linked.

No declaration named by the returned ties is missing from its cited file. The absence claims here concern particular mathematical statements or examples searched for, not broken output links. Source statements newly present in this snapshot—including the discovery identity, conditional zero law, actual list process, tensor preparation, physical decoder interfaces, direct-product development, exact ratio limit, and unconditional exponent endpoint—replace several stale absence diagnoses in the historical review.

## 7. Disposition of the existing coarse selections

The original selections remain useful reading routes. They are not a phrase seed and are not deleted or renamed by this return. The table records how each route's mathematical content is treated. Where a route identifies a concrete example or figure without a matching source instance, that limitation is deliberate.

| Existing selection | Paper lines | Disposition |
| --- | --- | --- |
| `exposition/headline/0` | 498 | Split the family quantifiers, shared circuit, explicit bounds, and fixed-parameter limit; use the current exact family declarations. |
| `exposition/certificate/0` | 128 | Split the winning conditions, pointer meaning, total output, and uniqueness; the concrete certificate example remains an illustration. |
| `exposition/comparison/0` | 145 | Keep the opening finite-board computation as an example; tie the general two-pointer rule in the next paragraph. |
| `exposition/weight/0` | 229–242 | Separate the pair cancellation, exact expectation identity, and half-weight consequence. |
| `exposition/weight/1` | 244 | Separate one-step drift, the ideal zero-weight branch, and the iterated expectation bound. |
| `exposition/pivot/0` | 260 | Retain the worked example as a reading route; link the full preparation and reflection at their actual claims, explaining retained workspace. |
| `exposition/verification/0` | 391–395 | Split fresh decoding, its measured mixture, exact test search, one-sided acceptance, and nonwinner soundness. |
| `exposition/planting/0` | 425 | Split the independent sampling, blank board, selected column, planted cell, and two Boolean answers. |
| `exposition/erased-zero/0` | 439 | Give conditional uniformity its own theorem; restrict the numerical endpoint to the hit bound rather than the entire paragraph. |
| `exposition/erased-zero/1` | 433 | Split discovery counting, indicator identity, averaging, and the exact probability identity. |
| `exposition/address/0` | 457 | Separate fixed target/time, simulator definition, independent outside data, clock, cap, and output rule. |
| `exposition/direct-product/0` | 467 | Expose the separate per-input cap and hard-distribution assumptions; link the actual direct-product development. |
| `exposition/forrelation/0` | 351–356 | Tie the complete matrix display, promise threshold, physical query cap, and hardness scale separately. |
| `exposition/exponent/0` | 500–508 | Separate numerical exponent arithmetic, the fixed choice of k, and the exact ratio limit (8.1). |
| `exposition/cycle/0` | 179 | Preserve as an illustration; the weighted drift theorem supports the general claim, not this literal cycle instance. |
| `exposition/cycle/1` | 185 | Figure asset is absent; no unrelated abstract cycle is presented as an evaluation of the pictured board. |
| `exposition/projection/0` | 335 | Tie the general squared-probability law and exact named negative witness; do not claim a formal evaluation of the absent zero-example instance. |
| `exposition/joint-event/0` | 459 | Separate lightness, prefix replay, and event containment; keep the direction of implication explicit. |
| `cite/exposition/677/src-amplification` | 677 | Split measured-law and retained-original-factor claims, retaining the precise arbitrary-projector limitation. |
| `cite/exposition/679/def-wins` | 679 | Link the winner definition at its actual scope, separately from the final theorems cited in the same sentence. |
| `cite/exposition/679/thm-alpha` | 679 | Link the current unconditional exponent theorem; do not copy the older conditional absence diagnosis. |
| `cite/exposition/679/thm-headline` | 679 | Link the current unconditional family endpoint with its own title and note. |
| `reference/exposition/539/AC-coherent` | 539 | Use the actual controlled-read construction, padding, and inverse statements; no dependency on the absent reasoning-record page. |
| `reference/exposition/547/upper-explicit-log6` | 547 | Link the separate cost contributions and the overall explicit quantum bound. |
| `reference/exposition/599/forr_circuit` | 599 | Link integer normalization and threshold rules of the canonical construction; do not identify it with the separate 180-gate example. |
| `exposition/known-pair/0` | 16 | Teaching question; no matching concrete sixteen-bit Lean instance was found. |
| `exposition/known-pair/1` | 18–23 | Teaching table; no claim that a generic board theorem evaluates these exact entries. |
| `exposition/known-pair/2` | 25 | Concrete reading trace remains an example, rather than an unrelated decision-tree theorem. |
| `exposition/known-pair/3` | 27 | Tie the one-query cost definition; retain the hidden-board exercise as illustration. |
| `exposition/hidden-zeros/0` | 29 | Randomization intuition remains prose; formal independent sampling appears in Section 7. |
| `exposition/hidden-zeros/1` | 31 | Scaling intuition remains prose; the rigorous source lower bound is linked at its later endpoint. |
| `exposition/pointer-check/0` | 128 | Split general certificate conditions from the particular displayed board. |
| `exposition/pointer-check/1` | 147 | Split the Boolean pointer rule, pair sorting, diagonal branch, and winner robustness. |
| `exposition/pointer-check/2` | 149 | Preserve the pointer-mutation counterexample as a teaching route without asserting a missing finite Lean instantiation. |

## 8. Validation and limits of the receipt

The supplied checker was run on the complete merged return. It checks quote location and paragraph or display boundaries, whole formulas, nonoverlap, required fields, declared source-name suffixes, in-declaration ranges, and title lengths. Additional review checked Markdown table-cell boundaries, note lengths, link-note lengths, full namespace prefixes, and whether highlighted source ranges actually reach the cited conclusion. Shared declarations have one title and one reconciled note across the paper.

This extra audit corrected one cross-cell table phrase, highlights that stopped inside named arguments or an initial `let` rather than at the conclusion, and the misattribution of the true-input $T\varepsilon$ term to verification. The final table phrases remain in individual cells; formulas are whole. A SHA-256 comparison against the supplied manifest found the paper and all 195 Lean files unchanged. No live-site integration, SVG inspection, or Lean execution is included in the receipt.

The review is complete through line 688. The quoted final output below is from the supplied checker on this returned folder, not from a shard, a substituted checker, or a Lean build.

```text
309 ties (309 with Lean), 239 declarations, 9 topics, 0 removed
PASS
```
