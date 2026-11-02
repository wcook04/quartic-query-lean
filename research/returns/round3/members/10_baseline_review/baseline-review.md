# Baseline review: a nearly quartic randomized–quantum query separation

**Review date:** 2 November 2026. **Assignment:** round three, job 10, independent review of the frozen long-record baseline. **Disposition:** retain the fixed-parameter theorem and the central proof mechanism; repair the source attribution and replace the historical evidence commentary before integration. This is an AI-assisted advisory review, not a human referee report or an acceptance of concurrent section returns.

<a id="REVIEW-01"></a>
<!-- passage:REVIEW-01 -->
## 1. Conclusion and scope

The baseline contains a coherent, unusually detailed reconstruction of the fixed-\(k\) separation. Its strongest parts are the all-input treatment of the quantum algorithm, the exact conditional sampling law, the simulator that keeps nonheaviness inside a joint event, and the explicit argument that excludes every universal exponent below four. This review found no counterexample to the headline theorem and no new fatal break in those ordinary arguments. That is a bounded review conclusion, not a certification of every proof in the packet or in the literature.

The changes that matter most are substantive:

1. Section 3.6 must distinguish the bound **stated** by Bansal–Sinha from the logarithmic comparison actually supported by their displayed v3 proof. The packet already adjudicates that issue, and an independent recheck reproduces it.
2. Much of the long record's formal-evidence commentary describes an older source snapshot. The present packet supplies matching receipts and actual types for several claims that the baseline calls absent, partial, or prose-only.
3. Those updates must follow exact theorem types. In particular, a theorem returning a candidate list differs from one returning a Boolean verifier result, and an explicit rational adversary constant differs from the sharper constant chosen in the prose.
4. The central total-function construction appears only after eighteen Forrelation subsections. The independent Forrelation proof should remain complete and accessible, but it need not delay the construction, comparisons and planted-input argument.
5. The short and examples-first companions need real two-way proof links and a later evidence refresh. Their present prose is comparison material, not authority for a new claim.

The entire 4,766-line baseline, including all Appendix B entries and Appendix C, was assessed by the full-record reviewer. The primary reviewer separately read the main proof and Appendix A, the complete supplied preprint extraction, the original preprint's first page, the decisive Bansal–Sinha source passage, and selected exact Lean statements. The two actual companion manuscripts were read in full for scope and linkage. The five supplied writing texts were read in full by the full-record reviewer. The source receipt identifies the reviewer and scope of each read; it does not merge sampled literature into a claim of complete reading.

The accompanying pasted-text attachment was unavailable. Its filename is Pasted text(20261102-190842).txt. No instruction or mathematical content was inferred from it.
<!-- /passage:REVIEW-01 -->

<a id="REVIEW-02"></a>
<!-- passage:REVIEW-02 -->
## 2. The strongest theorem, with the quantifiers in order

The supplied OpenAI preprint, dated 5 October 2026, states
\[
\alpha_{\mathrm{tot}}=4,
\]
where \(\alpha_{\mathrm{tot}}\) is the infimum of the nonnegative exponents for which one constant bounds \(R(f)/(1+Q(f))^\alpha\) over every finite total Boolean function. Its quantitative family statement is:
\[
\forall k\ge2\;\exists c_k,C_k,b_k>0,\;t_0(k)\;
\forall t\ge t_0(k),\quad m=4^t:
\quad
Q(F_{k,m})\le C_k\sqrt m(\log_2m)^{b_k},
\quad
R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log_2m)^2}.
\]
The same \(F_{k,m}\) occurs in both estimates. These are worst-case bit-query budgets, including randomness and measurement branches, with error at most \(1/3\) on every input. Elementary computation and workspace are free in this model. These conventions are present in the preprint's first page and in the baseline's model section [OpenAI2026, Theorem 1.1 and §§1, 2; baseline ROOT-RESULT, ROOT-ORACLE].

The current named-circuit theorem makes the family correspondence more explicit. QuarticQuery.Paper.construction_family_named fixes the circuit Forrelation.forrCircuit and proves both bounds for that circuit, with
\[
c_k=\frac1{400},\qquad b_k=6,\qquad C_k=\operatorname{Upper.budgetConst}(k).
\]
The lower-bound constant is uniform in \(k\); its sufficiently-large-size threshold need not be. The declaration also carries the realization and circuit-size conditions. QuarticQuery.Paper.construction_equation_two supplies the existential formulation in the preprint's square-root and logarithm notation. Both are present in the supplied source-bound root build. Neither is an individually compared declaration in the supplied Comparator receipts. Their complete types are retained in the correspondence and claim matrix.

For any proposed exponent \(0\le\alpha<4\), choose \(k\) so that
\[
\epsilon=2-\frac1k-\frac\alpha2>0.
\]
Hold this \(k\) fixed. The family gives
\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}
\ge
\frac{1}{400(1+C_k)^\alpha}
\frac{m^\epsilon}{(\log_2m)^{2+6\alpha}}
\longrightarrow\infty.
\]
Thus no universal constant works for that exponent. The known upper bound \(D(f)=O(Q(f)^4)\), together with \(R(f)\le D(f)\), supplies the upper endpoint [ABKRT2021, Theorem 2, printed p. 2]. Four is itself admissible, so it is the minimum of the admissible exponent set as well as its infimum.

**Boundary.** No fixed \(k\) in these estimates produces an exact fourth-power lower bound: its separation exponent is \(4-2/k\), with logarithmic losses. A useful explicit growing-\(k\) schedule needs a separately assembled quantitative theorem. The present source has a quantitative Forrelation auxiliary, discussed below, but this does not automatically validate the different growing-parameter candidate mentioned in the assignment.
<!-- /passage:REVIEW-02 -->

<a id="REVIEW-03"></a>
<!-- passage:REVIEW-03 -->
## 3. The proof mechanism and actual dependency order

The partial function \(P_{k,m}\) is quantumly cheap on its promise and classically hard. Its exact Boolean circuit has a different purpose: it permits verification that proposed partial-function answers are defined and correct. These jobs must remain separate.

Each of the \(m\) columns has an \(m\)-bit string, \(r=20\log_2m\) independent address instances, and an array of certificate cells. The address is the vector of partial-function answers. A winner has an all-one string and a valid cell at that address; the cell contains evaluation transcripts and points outward to a zero in every other column.

The direction of the pointers is decisive. A true winner's own cell disqualifies every opponent. No opponent, whatever its decoded address or promise status, can find a zero in the winner's all-one string. A candidate comparison therefore strongly favors a true winner even though comparisons between nonwinners may have arbitrary probabilities. This is what permits a total function to use a promise problem without imposing a global promise on its input [OpenAI2026, §§1.2, 2.2, 3.3; baseline CL-address-winner, upper-winner-dominates].

The quantum tournament samples with weights \(w_i\). Complementarity \(a_{ij}+a_{ji}=1\) implies
\[
\mathbb E[W_{\mathrm{new}}\mid w]
=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2,
\qquad W=\sum_iw_i.
\]
An unselected dominant candidate retains weight at least \(1-T\varepsilon>1/2\). The total expected weight shrinks, so the probability of missing that candidate is small. Coherent preparation and bounded amplification implement the conditional pivot distribution exactly as \(w_i/W\). This exact law, rather than success probability alone, is what licenses comparison with the ideal process. Local verification then rejects malformed certificates and off-promise candidates. The resulting quantum budget is capped on every branch [baseline upper-weight-drift through upper-total-error].

For the classical lower bound, the dummy input has one random zero in each column and blank cells. A uniformly chosen column is planted by erasing its zero and filling its true-address cell. The two executions agree until the algorithm queries the erased zero or the planted cell.

An address simulator receives only jointly independent outside information and aborts before its \((L+1)\)-st target query. It has an all-run cap. The event “this column is nonheavy and this query reaches its true cell” implies simulator success. Hence its probability is at most \((2/3)^r\). Conditioning the hard distribution on nonheaviness would not justify that conclusion; event containment does. The resulting discrepancy is less than \(1/3\), contradicting an algorithm correct with probability \(2/3\) on both coupled classes [baseline CL-simulator through CL-randomized-contradiction].
<!-- /passage:REVIEW-03 -->

<a id="REVIEW-04"></a>
<!-- passage:REVIEW-04 -->
### Dependency diagram

~~~mermaid
flowchart TD
    P["Forrelation: promise, circuit, query bounds"] --> F["Total function and local tests"]
    P --> M["Minimax and capped direct product"]
    F --> C["Outward-pointer comparisons"]
    C --> T["Exact-law amplification and tournament"]
    F --> V["Local verification"]
    T --> Q["Quantum upper bound"]
    V --> Q
    F --> G["Dummy–planted coupling"]
    M --> G
    G --> R["Randomized lower bound"]
    Q --> S["Same-family separation"]
    R --> S
    S --> E["Optimal exponent four"]
    A["Universal quartic upper bound"] --> E
~~~

The internal proof of the Forrelation lower bound has a separate dependency chain: finite-cube differentiation; bounded truncation and Stein identity; the uniform endpoint by reflections; one-block elimination; derivative growth for adaptive trees uniformly over biases; hard first moment and uniform second moment; amplification on promised inputs; then the explicit eventual-size estimate. None of the main quantum comparison or planted-input arguments requires following those Gaussian calculations before understanding the total function.

Appendix A is independent of the construction. Its dependency order is deferral to a fixed query sequence, nonnegative spectral adversary, the star and matching applications, the degree-dimensional restriction and Huang matrix, the Midrijānis decision tree, and the quartic conclusion. A proof graph should show that independence.
<!-- /passage:REVIEW-04 -->

<a id="REVIEW-05"></a>
<!-- passage:REVIEW-05 -->
## 4. The Bansal–Sinha correction
<!-- /passage:REVIEW-05 -->

<a id="REVIEW-06"></a>
<!-- passage:REVIEW-06 -->
### 4.1 What the source states

Bansal and Sinha's arXiv:2008.07003v3, Theorem 1.3 and Corollary 1.4, printed p. 4, state the lower-bound scale
\[
k^{-29}\left(\frac{m}{\log(km)}\right)^{1-1/k}
\]
at constant error for the same one-sided promise. Their \(N\) is one block's size \(m\), not the total input length \(km\). Theorem 1.3 writes the error as \(1/2-\eta/2\), so error \(1/3\) means \(\eta=1/3\) [BS21].

The baseline's elementary comparison of this scale with \(L\) is correct: for fixed \(k\), its ratio to \(m^{1-1/k}/(\log_2m)^2\) grows as a positive power of \(\log m\). The present Lean source also contains this numerical comparison in construction_claim_bs_to_L and construction_bs_comparison_chain. Those arithmetic theorems do not establish the source's randomized-query lower bound.
<!-- /passage:REVIEW-06 -->

<a id="REVIEW-07"></a>
<!-- passage:REVIEW-07 -->
### 4.2 What fails in the displayed argument

Set \(\Lambda=\log(km)\). In v3 §5.4, main.tex lines 1180–1181, the preceding valid level estimate contains
\[
m^{-\ell(1-1/k)/2}(8k)^{14\ell}(c_0d_1)^{\ell/2}
\Lambda^{(\ell-1)/2}.
\]
The next displayed expression replaces the logarithmic exponent by
\[
\frac{\ell}{2}\left(1-\frac1k\right).
\]
After matching the fixed constants, the ratio of the two expressions is
\[
\Lambda^{(\ell/k-1)/2}.
\]
It is unbounded for fixed \(\ell>k\). Such levels occur in the specified range \(k\le\ell\le k(k-1)\) when \(k\ge3\).

The smallest transparent example is \(k=3,\ell=6\). The preceding term is proportional to \(m^{-2}d_1^3\Lambda^{5/2}\); the replacement has \(m^{-2}d_1^3\Lambda^2\). At \(d_1=a(m/\Lambda)^{2/3}\), their values are proportional to \(a^3\sqrt{\Lambda}\) and \(a^3\). The sum comparison therefore fails at the advertised depth scale, for any fixed adjustment of constants. This is a defect in the displayed upper-bound comparison, not an algorithm contradicting Theorem 1.3. The ensuing depth threshold is on line 1184.

The source's equation (5.31) has a separate reciprocal-\(\delta\) transcription: its earlier second-moment bound gives \(4/(m\delta^2)\). That correction changes the sufficiently-large-\(m\) threshold. It does not explain away the logarithmic discrepancy.

The correction belongs in §3.6 itself and in the source-role sentence of §3.16. It should neither be buried in a general disclaimer nor inflated into a claim that the source theorem is false. No author-confirmed correction was supplied or established in this review.
<!-- /passage:REVIEW-07 -->

<a id="REVIEW-08"></a>
<!-- passage:REVIEW-08 -->
### 4.3 Why the required fixed-parameter conclusion remains available

The local theorem ForrelationLower.bansalSinhaLower proves
\[
\forall k\ge2\;\exists t_0\;\forall t\ge t_0:
\quad L_{k,4^t}<R(P_{k,4^t})
\]
without a Bansal–Sinha lower-bound premise. The baseline §§3.7–3.15 reconstruct that separate proof.

There is also a useful, explicitly limited ordinary deduction from the valid Bansal–Sinha ingredients. With the source's own distributions and normalization, the level sum can be written
\[
\Lambda^{-1/2}\sum_{\ell=k}^{k(k-1)}
\left(\frac{Ck^{28}d_1\Lambda}{m^{1-1/k}}\right)^{\ell/2}.
\]
If the expression in parentheses is at most \(1/4\), this is at most \(2^{1-k}/\sqrt{\Lambda}\). For fixed \(k\) it eventually contradicts the positive acceptance gap obtained from their input-distribution theorem after constant-error amplification. This yields the sufficient scale
\[
R(P_{k,m})=\Omega_k\!\left(\frac{m^{1-1/k}}{\ln(km)}\right),
\]
which already exceeds \(L\) eventually.

The file source-audits/bs-weak-log-corollary.md gives the full deduction, including amplification, off-promise acceptance bounds, the geometric sum, size conditions and the final comparison. It imports the accurately stated Theorem 3.1, Theorem 3.2 and Corollary 3.5; their full proofs were not independently re-audited here. It establishes neither the sharper logarithmic source statement nor a new formal theorem. It is an optional source clarification, not a replacement for the maintained local proof.
<!-- /passage:REVIEW-08 -->

<a id="REVIEW-09"></a>
<!-- passage:REVIEW-09 -->
## 5. What the supplied formal evidence now says
<!-- /passage:REVIEW-09 -->

<a id="REVIEW-10"></a>
<!-- passage:REVIEW-10 -->
### 5.1 Keep the three versions distinct

| Object | Identifier | Meaning |
|---|---|---|
| Historical long-record source pin | c7e0c9161f0ad898889bd9166e7b354acd42188d | The pin explicitly named in baseline §2.3 |
| Packet repository commit | 1dd469dd0042b937b739da3bc211eeb60bdf7462 | Packaging revision in the round-three manifest |
| Commit recorded by current runs | 31e17dee667d1d72fa621da8e7d3d8ff5fc3960a | Run metadata, whose declared local inputs were checked against the packet |
| Baseline SHA-256 | a6d1ede97135064c2c1b54992bfe32caac76da93688e67a378eab8cca16947ff | The exact reviewed manuscript |
| Preprint PDF SHA-256 | a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e | The mathematical target revision |

All 447 file records in the input manifest matched their byte lengths and SHA-256 values. The current root-build receipt, 11 current Comparator records, dependency export and axiom-audit verdict matched their 124 declared local source/configuration hashes. Those 11 Comparator records comprise five positive bundles, five expected-rejection negative controls, and an additional paranoid Unconditional comparison; they are not eleven positive theorem bundles. All 45 per-module acceptance input closures checked against packet bytes also matched. Eleven older unbound receipts remain historical evidence; they were not silently promoted.

The recorded dependency export has 2,652 declared constants, 1,354 reached from two selected roots, and no unresolved constants within its reported scope. The recorded 258-declaration type/axiom audit has matching source and log hashes and reports only propext, Quot.sound and Classical.choice. These are descriptions of the supplied run records whose byte bindings were checked. This review did not execute Lean, replay Comparator, verify archived compiled artifacts, or independently rebuild the full pinned dependency closure.

The difference between commit labels is therefore handled by the actual input hashes. A dirty label or a successful earlier run alone would not suffice. The focused dependency sources and configuration improve inspectability, but do not turn this editorial pass into a cold build.
<!-- /passage:REVIEW-10 -->

<a id="REVIEW-11"></a>
<!-- passage:REVIEW-11 -->
### 5.2 Principal changes in evidence

The principal-claim matrix covers all 121 original catalogue rows and retains the selected exact types, ordinary premises, route, current root membership, Comparator membership and reach from the two headline roots. The following are the most consequential updates.

| Baseline passage | Current source support | Required wording |
|---|---|---|
| ROOT-RESULT; ROOT-FAMILY-ASSEMBLY | construction_family_named; construction_equation_two | Both inequalities now explicitly concern the same named circuit, with \(c=1/400,b=6\). |
| forr_bundle | construction_lemma_2_1_complete | A conjunction theorem is present; its quantum component retains the concrete coherent/compiler interface. |
| forr_bs_translation | construction_bs_comparison_chain | The arithmetic comparison is present. Its receipt does not certify the stronger literature theorem. |
| upper-tournament-evidence | quantumTournament_list, together with the theorem's coherent comparison premises | A list-valued theorem is now present. Keep the older Boolean-continuation proof as a separate implementation route. |
| CL-product-law | classical_transcript_product_law | The finite positive-mass conditional product law is now represented. |
| CL-conditional-values; CL-supermartingale | classical_eq_16_transcript; classical_transcript_conditional_expectation | Name the actual finite conditional formulations. Some broad ledger rows remain partial. |
| CL-discrepancy | eq_23_two and eq_23 | Current statements include absolute-value discrepancy bounds, including coefficient two. |
| CL-early-late | erasedZero_eq_expectedZeros_div; eq_19; erasedZero_le_two | The exact erased-zero probability identity is present as an additional export, although the row's older selected ties remain partial. |
| ROOT-RATIO | classical_exponent_ratio; classical_Fkm_ratio | The literal quotient envelope and divergence are now represented, with their hypotheses. |
| Appendix A | appendixA_lemmaA2 through appendixA_theoremA1 | An assembled paper-route upper bound exists in addition to the older library route. |
| Appendix B | The same old statements plus current matrix | Preserve the historical catalogue, but label it as historical and link current evidence separately. |

The positive Comparator bundles are selected statement comparisons, not individual comparisons of every new paper-level declaration. In particular, the new list, conditional-expectation and quantitative-uniform auxiliaries should not inherit a Comparator pass by association. The challenges are separately compiled and share the maintained vocabulary/specifications with the solutions. That checks agreement with the challenge; semantic review remains a different task.

Three further type boundaries must remain visible. The generic physical compiler charges twice the logical read count, whereas the direct phase-kickback prose construction gives the sharper count. A measured output law does not describe every retained workspace register. The complete local-test wrapper fixes its candidate and address before choosing its workspace witness, so its type should not be quoted as one already-exported circuit operating on all candidate/address superpositions. None of these differences changes the fixed-parameter asymptotic estimate. The optional erased-zero improvement with denominator \(m(m+1)\) also remains a separate ordinary proof without an identified current formal theorem.
<!-- /passage:REVIEW-11 -->

<a id="REVIEW-12"></a>
<!-- passage:REVIEW-12 -->
### 5.3 The Appendix A constant requires an exact comparison

The baseline chooses
\[
c_*=\frac{1-2\sqrt2/3}{2}
\]
in its adversary lemma. The current convenient endpoint appendixA_lemmaA2 uses \(1/35\). It yields
\[
\lambda(f)\le35Q(f),\quad
\operatorname{bs}(f)\le1225Q(f)^2,\quad
D(f)\le1500625Q(f)^4.
\]
The inequality \(1/35<c_*\) follows by squaring the equivalent positive comparison \(\sqrt2<99/70\). Thus this rational endpoint is sufficient for the paper's existential-constant claim and slightly weaker than the particular constant in the baseline.

The sharper factor occurs in appendixA_adversary_of_perron, but that theorem explicitly takes a Perron witness and a fixed-sequence algorithm. Other declarations supply those ingredients. The exact correspondence must record that composition, rather than declaring the rational endpoint an exact match for the sharpened display.

There are three legitimate source routes: the older imported constant 20736; the assembled star/Huang/Midrijānis route with constant \(35^4=1500625\); and an optional hybrid using polynomial-method block sensitivity, with constant 19600. Constants from one route must not be attributed to the proof of another. The separate earlier Špalek–Szegedy coefficient issue is not the Bansal–Sinha logarithm issue and does not refute the adversary-method equivalences.
<!-- /passage:REVIEW-12 -->

<a id="REVIEW-13"></a>
<!-- passage:REVIEW-13 -->
### 5.4 A quantitative auxiliary is now present

QuarticQuery.forrelation_lower_uniform_sharp states, under \(k\ge2\) and \(15k+2\le2t\),
\[
\frac{2}{18225}\,
\frac{(4^t)^{1-1/k}}{k^2\ln(4k4^t)}
<R(P_{k,4^t}).
\]
It has current root-build membership and appears in the recorded type/axiom audit. It is outside the two selected headline-root dependency closures and is not an individually compared declaration. The word “sharp” is its local identifier; it does not identify the sharper logarithmic expression in Bansal–Sinha.

No assembled growing-\(k\) family theorem was found in the supplied source search. This auxiliary merits a source-index entry and separate integration decision. It does not alter the version-bound preprint theorem under review.
<!-- /passage:REVIEW-13 -->

<a id="REVIEW-14"></a>
<!-- passage:REVIEW-14 -->
## 6. Concrete improvements that survived checking
<!-- /passage:REVIEW-14 -->

<a id="REVIEW-15"></a>
<!-- passage:REVIEW-15 -->
### 6.1 Expose two Stein eliminations before the general induction

The hardest passage for a cold reader is §3.10. Its general statement is short enough to conceal why derivatives of already created analytic weights do not proliferate.

The proposed insertion takes \(k=3\), with biases
\[
w_s=(sX_0,\;Y_0X_1,\;Y_1).
\]
Differentiating the first block gives \(X_0(a)\mathcal E_{w_s}D_{0,a}g\). Stein integration in \(U_0(a)\) has two possible contributions. The first repeats \(D_{0,a}\) and vanishes by multilinearity. The second moves to the middle block and leaves
\[
H_{ba}\Psi(U_0(a))\varphi'(V_0(b))X_1(b)
\,\mathcal E_{w_s}D_{0,a}D_{1,b}g.
\]
Now the old weight depends only on \(U_0\). Stein in \(U_1(b)\) leaves it fixed; the middle-block repeated derivative vanishes, and the last block contributes \(H_{cb}\Psi(U_1(b))\varphi'(V_1(c))\). The surviving term has one cube derivative in each block. This is exactly the structure needed for the induction.

The ready replacement accounts for every chain-rule term and preserves the preceding dominated-convergence justification. It also says that the mean value theorem is applied to the whole scalar function \(h_g\), producing one common parameter for all paths. The outcome is a successful explanatory expansion of an existing proof, with no new Lean check or novelty claim.

A further small example prevents a misleading compression. If \(b\ne c\) and
\[
g(z)=z_{0,a}z_{1,b}z_{1,c},
\]
then
\[
\mathcal E_\mu[D_{0,a}D_{1,b}g]=\mu_{1,c}.
\]
Thus an order-two derivative at nonzero bias can contain information from degree three. It would be wrong to replace the needed biased derivative estimate by a bound only on degree-two coefficients at uniform bias. This example does not assert a nonzero final Gaussian expectation for that odd monomial.
<!-- /passage:REVIEW-15 -->

<a id="REVIEW-16"></a>
<!-- passage:REVIEW-16 -->
### 6.2 Make the amplification resource explicit

The baseline's Lemma 3.1 wording expands “success bit” to “every designated success subspace”. Add that its projector is fixed and input independent and that the corresponding reflection is available without input queries, or retain the preprint's success-bit formulation. The actual applications use retained flags, so they satisfy this condition. This is a resource clarification in the general statement; the tournament application does not need a new algorithm [BHMT2002, §2, Lemma 1 and equation (8); baseline upper-amplification-statement, upper-grover-geometry].
<!-- /passage:REVIEW-16 -->

<a id="REVIEW-17"></a>
<!-- passage:REVIEW-17 -->
### 6.3 Preserve the parts already doing their job

The nonheavy simulator argument should survive compression essentially intact. The all-input acceptance inequalities in §3.14 should also stay beside the distributions: the hard distribution is not supported only on yes inputs and uniform measure is not supported only on no inputs. The final verification proof must continue to cover every possible decoded address on a zero input.

The finite Forrelation census was independently reproduced from the \(4\times4\) Walsh matrix: 104 yes inputs, 48 no inputs and 104 unpromised inputs out of 256. The negative witness has \(\Phi=-1\) and is unpromised. This is a useful check of sign and threshold semantics; it is not evidence for a growing-dimension lower bound. The script and exact output are included.
<!-- /passage:REVIEW-17 -->

<a id="REVIEW-18"></a>
<!-- passage:REVIEW-18 -->
## 7. Assembly plan and ownership

Keep the main reading path focused on the total function. Retain the Forrelation promise, exact circuit interface, small instance, lower-bound statement and a direct link to its independent proof. Move the full internal analysis now in §§3.7–3.16 into a dedicated proof appendix, retaining every mathematical passage and its stable anchor. Keep the qualified source comparison close to the main lower-bound interface. The full proof remains the authority for the local endpoint after the move.

Consolidate repeated build and declaration inventories into a versioned evidence appendix and the machine-readable correspondence. Preserve short local statements of genuine mathematical differences: the bit-query cost, extra assumptions, sharper versus rational constants and alternative proof routes. A reader should not have to parse a list of Lean identifiers between consecutive mathematical steps.

The transfer map should connect the short paper's construction, quantum, classical, Forrelation and exponent sections to the corresponding long-record passages. The exposition should link its four-column toy, tournament, conditioning warning and Forrelation transition to the actual proofs. Its toy address problem is correctly limited; it should not be presented as a small full instance of the asymptotic construction. The companion manuscripts currently have passage comments but lack matching real HTML anchors, so add stable rendered anchors before creating fragment links.

The numbered owners recoverable from the task context are: 01 models/evidence; 02 Forrelation promise/circuit; 03 Forrelation lower bound; 05 quantum upper; 06 direct product; 07 planted lower; and 09 backend. Construction and Appendix/exponent changes are assigned by section title where the exact number is not supplied. Global order, Appendix B, bibliography and two-way companion links belong to the later integrator. No recommendation assumes that a concurrent return already exists or has been accepted.
<!-- /passage:REVIEW-18 -->

<a id="REVIEW-19"></a>
<!-- passage:REVIEW-19 -->
## 8. Understanding, economy and useful next questions

| Dimension | Assessment | Evidence and concrete disposition |
|---|---|---|
| Mechanism and understanding | Demonstrated; placement needs improvement | The outward pointers and exact-law tournament explain the total-function gain. Move the construction earlier and preserve its off-promise argument. |
| Elegance and proof economy | Partial | The two proofs of the Forrelation ingredient and repeated evidence paragraphs interrupt the main path. Preserve both proofs in distinct roles and consolidate metadata. |
| Structural yield | Demonstrated | The zero-search proof improves a constant and explains its expected-cost sharpness. Keep the distinction from optimal worst-case distinguishing cost. |
| Transfer and connections | Demonstrated within scope | The tournament is reusable for coherent complementary comparisons with one dominant candidate. Drucker's conditional values are an antecedent for the capped argument, not an interchangeable global-budget theorem. |
| Fertility and question selection | Partial, appropriately bounded | First determine which exact source claim a sharper logarithmic result would establish; separately assemble any chosen growing-\(k\) family with all prerequisites. Do not add a speculative programme to this record. |
| Difficulty and negative knowledge | Demonstrated | Nonzero-bias derivatives retain higher-degree terms; off-promise comparisons need no orientation gap; conditioning on nonheaviness changes the experiment. Keep these precise failure boundaries. |
| Shared reuse | Partial | Complete ordinary proofs are present, but the current evidence map and companion links need repair. The returned matrix and transfer plan supply reviewable targets. |

Two mathematical follow-ups deserve priority only if the integrating team chooses to extend scope. First, establish the exact sharper logarithmic source statement or locate a valid correction, with the level-six case as an immediate diagnostic. Second, assemble a quantitative growing-parameter family from actual checked auxiliaries and an explicit schedule, auditing both the quantum constant and the lower-bound size condition. Neither follow-up is required to retain the fixed-\(k\) theorem.

The immediate editorial work is already concrete in repairs.json and replacements.md. Acceptance should be against those located changes and the later integrated manuscript, followed by its ordinary rendering and source-link checks. This return does not edit, merge, publish or declare acceptance of the baseline.
<!-- /passage:REVIEW-19 -->

<a id="REVIEW-20"></a>
<!-- passage:REVIEW-20 -->
## 9. Deliverable and validation guide

- baseline-review.md is this review.
- repairs.json contains ranked, located replacements and structural moves with owners, benefits and validation conditions.
- coverage-map.json and source_read_receipt.json distinguish assessed, sampled, unavailable and unassessed scope.
- correspondence.json and principal-claim-matrix.json retain literal boundaries, exact types and evidence distinctions.
- LEAN_GAPS.md records remaining correspondence and validation boundaries in section order.
- source-audits/bs-source-audit.md, source-audits/bs-weak-log-corollary.md and stein-k3-replacement.md preserve the detailed source calculation and worked improvement.
- references.bib, STYLE_RULES.json and review_notes.md record editions, writing moves and the required authoring receipt.
- manifest.json binds every returned member's bytes and source versions; validation.json reports the checks actually run.

The delivered review is Markdown/JSON/BibTeX and reproducible Python. No final integrated manuscript or new publication PDF was produced or rendered. Source PDF checks were bounded to the stated original pages, and finite arithmetic was run independently. The supplied Lean receipts are source-bound evidence; this session supplied the hash and semantic/type comparison, not a new kernel run.
<!-- /passage:REVIEW-20 -->

