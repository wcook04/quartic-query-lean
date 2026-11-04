# Classical specialist reread

**Outcome.** I reconstructed the classical lower-bound chain and the parameter assembly without finding a new mathematical defect in the inspected current text. The strongest surviving correction is a source-status sentence at lead line 3743. It should express the limited consequence of the source-display check, consistently with line 1642 and Appendix E. This is an evidence-scope correction, not a claim that Bansal–Sinha's theorem is false. Several delicate issues that could easily have invalidated this argument are explicitly and correctly handled now.

This is an informed specialist reread after the primary chronological pass was frozen and after the quantum specialist released the serial slot. It is not a second cold primary pass. The source-only preparation remains in `classical_source_notes.md` and `classical_sources.json`; those files were not rewritten. Additional SSW/GTW reading is recorded separately. No Lean, Lake, Comparator, or manuscript checker was run; no input source was modified. The exact exposure record is `classical_review_scope.json`.

## 1. The Forrelation lower-bound derivation

### What was checked

The current argument fixes the explicit Walsh promise and proves its hardness independently of the disputed final logarithmic simplification in Bansal–Sinha v3. I followed the chain from the multilinear extension through the algebraic truncation, the Gaussian interpolation, the decision-tree derivative estimate, the two promise-mass estimates, amplification, and the numerical contradiction. The substantive range was lead lines 854–1669, with the promise and integer normalization at 441–556. The quantum sampler and exact-circuit construction in §§3.3–3.5 were outside this specialist's core scope.

The main conceptual point is that the order-k derivative in (F22) is a derivative of the **full** multilinear extension at a nonzero bias. It is not merely the homogeneous degree-k Fourier part. Terms of higher degree survive by contributing their remaining bias factors. The text makes this distinction explicitly at (F24), including a degree-(k+1) example. Consequently the path identity does not throw away higher Fourier levels.

The successive integration-by-parts operations are consistent with the independence structure. Each new Gaussian layer is independent of the earlier layers already represented in the weight. Within a layer, U and HU are not independent, and the proof does not assume they are. The same-coordinate derivative that would create an unwanted term vanishes by multilinearity. The useful kernel is nonnegative and bounded by 3/16; its lower expectation estimate uses marginal second moments rather than a false product-independence claim. The finite polynomial and bounded smooth factors justify the displayed exchanges of derivatives and expectations.

For (F25), the coefficient array is fixed before the query path is sampled. Conditioning on a compatible transcript leaves unqueried centered variables independent and centered. A fresh query changes the degree-r process by one centered increment times a predictable degree-(r-1) process. The induction stops **before** the predictable coefficient violates its bound. This is the required treatment of a bad event; conditioning on all coefficients remaining small would not preserve the martingale. The proof's finite-horizon maximal estimate and union bound are adequate. Repeated queries contribute no fresh increment, and the leaf estimate bounds the expectation needed for the derivative sum. Girish–Tal–Wu's standard-tree overview, §1.3 and its truncation footnote, is an appropriate methodological antecedent; it is not being passed off as the literal biased-derivative theorem proved here. [CLS-S10]

The hard analytic law ν₁ need not be supported on the promise. This is addressed by two separate facts: its positive-promise mass is at least 31δ, and the uniform law has exceptional mass at most 4/(mδ²). The acceptance inequalities retain the exceptional term and use only 0≤A≤1 off promise. The proof then amplifies before comparing a small analytic distinguishing advantage with correctness. Nothing requires the analytic hard law to equal the later minimax law μ.

### Uniform constants

The constant arithmetic in §§3.14–3.15 is consistent. With τ=25k, the amplified error is at most 18^{-k}=a_k/18. The assumptions 15k+2≤2t and m=4^t make 4/(mδ²)≤δ, while δ≤a_k/32. Hence (F42) gives a lower gap at least 119a_k/144. Under the proposed depth cap, the main term in (F33) is at most a_k/3 and the residual is at most a_k/4. Their total 7a_k/12 is strictly smaller. In particular, the key cancellation uses

\[
800\cdot\frac{2}{18225}=\left(\frac8{27}\right)^2,
\qquad \frac3{16}\cdot\frac8{27}=\frac1{18}.
\]

This proves the stated strict estimate (F43), not just a non-strict asymptotic version. For the fixed-k allowance, ln(4km)≤6t gives the denominator 54675k²t. At t≥13669k², the inequality 4t≥54676k²>54675k² yields the claimed strict comparison with m^{1-1/k}/(4t²), hence with its floor. The eventual and explicit formulations are properly separated. The available Lean signature at `ForrelationLower/Uniform.lean:525–532` matches (F43); it does not establish that the 13669k² specialization was compiled.

Appendix D's older threshold is a valid, deliberately coarser consequence. The square of its main term is bounded by 9^h(C/(4t))^k, the chosen η₀ controls that term by δ²/4, and the residual and exceptional mass are each controlled separately. In its closure step, τ=30k makes the amplified error less than δ. The lower acceptance mass then contradicts the upper 3δ bound. This appendix is historical reconstruction, not a second assumption in the current proof.

### Source comparison and the SSW transfer

Bansal–Sinha v3 does state the lower bound quoted at (F4), including the k^{-29} factor and the logarithmic exponent 1-1/k. The identified display discrepancy is real: at a level r>k, the omitted factor is log(kN)^{(r/k-1)/2}; for fixed k≥3 this is unbounded with N. Appendix E correctly limits its conclusion to the displayed inference. Its replacement denominator exponent 1-1/[k(k-1)] makes every remaining logarithmic exponent nonpositive, and the displayed geometric-series bound is sufficient. The reciprocal-shaped exceptional-probability term in source (5.31) also conflicts with source Theorem 3.1; the replacement 4/(Nδ²) and threshold N≥4/δ³ are valid. [CLS-S02, v3 pp.37–38 and §3]

I also checked the source of (F56) directly in SSW v4, printed pp.35–36: Corollaries 4.14 and 4.15 give an absolute-C Fourier bound for ternary leaf labels and then all labels in [-1,1]. The proof of the extension is convex averaging over leaf signs. The current use has the right scope. [CLS-S09]

The restriction identity (F57) is valid monomial by monomial. The endpoint and interior free probabilities give a path probability (1/4)(3/4)^{k-2}; its reciprocal combined with the kernel factor is exactly 3/4^{k-1}. Restrictions do not increase depth. This derives (F58) from the Fourier theorem without importing a rorrelation input distribution. The variable-error amplification uses O(k/η²) runs; the binomial estimate contributes a factor k on taking the 2/k power. The cancellation claimed in (F59)–(F60) is therefore justified. The unspecified absolute constant remains unspecified, and the extension to power-of-two Walsh dimensions is explicitly ordinary mathematics rather than a claim about the frozen formal definition.

## 2. The capped direct product and hard law

All of §6 was read. Its probability argument is now unusually explicit about the distinctions that matter:

- The hard law is chosen after P and L, with one law defeating every depth-L tree. The finite convex-separation proof has the correct quantifier order and supplies a common strict margin. It does not assert balanced output labels.
- A deterministic compatible transcript defines a Cartesian product of constraints on the independent inputs. An arbitrary sequence of query-answer pairs need not be compatible; the text supplies a counterexample.
- The continuation value uses the **remaining** cap. Grafting two optimal child trees proves the one-step inequality. All factors except the queried input's factor remain unchanged, so their product has nonincreasing expectation.
- The terminal bound is on conditional success probability. It is not an invalid pointwise comparison between a zero-one success indicator and a fractional potential.
- The horizon is finite and may be padded after stopping. Side information and coins are fixed jointly; independence of each separately would not suffice.
- The realized cap event stays inside the probability. Truncation before the first excess query gives an event inclusion in the success event of a truly capped tree.

These points match the fair-algorithm specialization of Drucker's conditional-value argument. His global-budget theorem is different, and the current source comparison actually carries out its alternative substitution: α=3/r, ε=1/3 and T=L give a total cap L and success at most 2(2/3)^r. The altered constant still fits the discrepancy contradiction. Shaltiel's earlier fairness definition is correctly distinguished from his XOR-advantage conclusion. [CLS-S01, §§1.3,3,5; CLS-S03, §5]

The adaptive AND example, the XOR simulator example, and the three-input nonheavy example each check a distinct logical point. Their displayed probabilities agree with direct calculation. In particular, Pr(C|E)=5/8>9/16 in the first example does not conflict with Pr(C∩E)≤9/16; the simulator example has strictly more success than the original joint event because its default output can be correct.

The unnormalized induction (6.9)–(6.10) is an adequate second proof, including zero-mass branches. The identity (6.11) follows by normalization and cancellation of the transcript masses. The current formal-scope discussion appropriately distinguishes arbitrary independent information in the ordinary proof from finite weighted seed spaces in the inspected formal endpoints.

## 3. The planted lower bound

The experiment separates the independent variables from their derived objects correctly. Every zero position and every other column's address strings may be supplied to the target simulator. The target true address and evaluated transcript may not. The simulator runs on the blank dummy input; the filled cell is a derived modification of the paired planted input. The independent uniform column I is chosen outside the dummy run.

The first-difference argument bounds an absolute output-probability gap by visits to the erased zero or to the entire true-address cell. Counting a visit to any cell bit is a valid upper bound even if that bit happens not to change. The erased-zero identity follows by averaging the independent I after fixing the dummy data. The example changing the selection rule for I correctly demonstrates why a uniform marginal alone is insufficient.

The early/late estimate is sound under adaptive queries. A positive-probability transcript leaves an undiscovered zero uniform among the remaining rows. Early discoveries have conditional probability at most 2/m, and each late discovered column consumes at least m/2 queries. This yields E Z≤4G/m. The alternative world-count induction proves the coefficient-two estimate by a different route. The further reference-path argument yields 2/(m+1) times expected X-query cost; it is correctly not advertised as an optimal curve for each fixed worst-case budget.

The heavy-column count uses total target-string calls, including repetitions, over the complete dummy run. At fixed i and time q, the simulator has one charged counter and a separate original query clock. It stops before charged call L+1 and reads the proposed address from the query coordinate. On the nonheavy, correct-cell event it reaches that time and outputs the true address. This is an inclusion, not equality and not conditioning. The per-time union followed by the independent average over I gives G(2/3)^r with no stray factor m.

The final numerical estimate is valid already for m=4^t, t≥1, 1≤L≤m: (2/3)^{40t}≤m^{-10}, and the three terms sum to at most 6/100<1/3. Fixing a randomized algorithm's coins preserves its worst-case cap, which is the hypothesis needed for this averaging contradiction. No expected-budget theorem is silently substituted. The floor lower bound with coefficient 1/400 follows for t≥8 and applies to the same realizing circuit used by the upper bound.

## 4. Fixed and growing parameters

The fixed-parameter argument has the right quantifier order: choose α<4, then a fixed k>2/(4-α), then exceed each proposed universal constant by taking t sufficiently large. The exponent gap is 2-1/k-α/2>0, and the logarithmic denominator is dominated by that positive power. At the boundary α=4-2/k, the displayed ratio no longer implies divergence, as the text explicitly says. The same-function witness and the reindexing to an ordinary Boolean cube are explained.

The growing-k section uses (F43), not the much larger sufficient threshold 13669k². Its choice k=⌊√(t/20)⌋ satisfies the actual hardness condition and the floor admissibility conditions. The classical estimate is obtained from R>⌊mL/100⌋ and integrality before using L≥X/2, so it legitimately improves the floor accounting for this route. The balance between 40k and ℓ/k is correct; the loss from rounding k down is less than 20. The 508 in ε(ℓ) is slack, not an arithmetic necessity, and is labeled as such. The case ε≥4 is handled separately using Q,R≥1. Unbounded R together with the universal quartic bound forces unbounded Q. Thus the section supports the advertised 4-o(1) family without claiming R=Ω(Q⁴).

The explicit quantum envelope in (7.5) was used here as the result of the preceding quantum analysis. I checked its displayed constant expansion and the elementary inequalities leading to 2^{53}k2^{10k}; I did not independently reconstruct the quantum circuit compiler in this pass.

## 5. Surviving correction and optional editorial opportunity

### CLS-C01: narrow the residual source-status assertion

**Location:** lead line 3743, within `CL-forrelation-input`; compare line 1642 and Appendix E lines 6008, 6028, 6050. **Kind:** evidence-scope wording. **Severity:** medium editorial correction; no mathematical blocker established. **Discovery status:** independently checked after the parent supplied a historical-audit pointer to the surviving sentence; not an unprompted discovery.

The sentence says **“the stated theorem stands.”** The surrounding source check has established that a particular displayed step fails and that this does not by itself refute the theorem. Those are different statements from an affirmative certification of the source theorem or its original proof. The current record supplies its own fixed-k proof, a sharper uniform estimate, and an optional externally based comparison; these should retain their distinct provenance. In particular, the SSW comparison offers a separate argument in its stated parameter regime, not an author-approved repair to Bansal–Sinha v3.

**Concrete replacement:** “Appendix E identifies a defect in one displayed step; that defect does not by itself refute Bansal and Sinha's theorem. This section uses the prerequisite proved independently in §3.” If affirmative revalidation is intended instead, identify the exact alternative theorem, its hypotheses and its parameter range. Do not infer that revalidation solely from the fact that a counterexample to the theorem has not been supplied.

### Optional: one comparison table for the three hardness interfaces

This is an explanatory opportunity, not a missing proof or a new required finding. A small table near §3.6 could compare the stated Bansal–Sinha estimate, the direct uniform estimate (F43), and the SSW-based comparison (F60): which one is invoked, its k/logarithm dependence, its dimension threshold, and whether its numerical constant is explicit. The current text contains these distinctions but distributes them over the main proof and Appendix E. Such a table would make the reason for choosing (F43) in §7.3 immediately visible without changing the mathematics or lengthening the proof. The direct-product and planted sections already provide the necessary conceptual bridges and should not be expanded merely to produce more findings.

## 6. Statement destinations and limits

I compared available statement text for the uniform lower bound, conditional-value direct product, finite-seed cap-event theorem, fixed-time joint event, complete equation (19), named-family bounds, and named-family ratio. The inspected signatures agree with the scope descriptions used above. `Uniform.lean` also contains an older explicit 3499200k² threshold; that is not the sharper ordinary 13669k² specialization. Missing from the local supplied subset were the linked `Upper/Bound.lean`, `LowerBound/Planted/Main.lean`, `Paper/Section4.lean`, and `ZeroSearchSuccessor.lean`; I reported those access limits to the parent and did not fabricate inspection of them. No execution status is newly certified here. The formal-methods perspective is responsible for its own subsequent examination of source and retained receipts.

**Source key:** CLS-S01 Drucker; CLS-S02 Bansal–Sinha; CLS-S03 Shaltiel; CLS-S09 Sherstov–Storozhenko–Wu; CLS-S10 Girish–Tal–Wu. Full editions, URLs, source hashes, passage locators and access limitations are in `classical_sources.json` and `classical_source_addendum.json`.
