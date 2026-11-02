# Review notes and paper-authoring receipt

## Assessment

The replacement supplies a complete ordinary proof of the exact fixed-parameter Forrelation lower bound requested in the packet. The assessed proof does not assume its hard analytic step. It explicitly proves the rounded chain's zero endpoint, the Stein cascade, the biased derivative estimate, the promise moments and leakage bounds, amplification, and quantitative contradiction.

The supplied current development also proves the restricted sharp uniform endpoint. This return corrects older prose that still calls that endpoint proposed. It does not claim a fresh Lean run, a new Comparator result, human peer review, integration into the manuscript, or priority for the proof arrangement.

## Ranked, located corrections

| Priority | Location | Finding and disposition |
| --- | --- | --- |
| 1 | §3.15 F43; §3.16 final scope paragraph | The exact coefficient2/18225 theorem is already in Uniform.lean:527 and the current root/native/type-axiom records. State this current evidence, while retaining its absence from Comparator. |
| 1 | §3.14 F41–F42 | Neither distribution is assumed promise supported. Keep all-input acceptance inequalities and the exceptional uniform term4/(mδ²). |
| 1 | §3.10 F18–F23 | Show both repeated-derivative cancellations at k=3 and the earlier-only invariant for general k. Use one common MVT parameter; do not silently identify an integrated-in-s wrapper with exists_identity. |
| 1 | §3.11 F29–F32 | Keep the fresh-coordinate cylinder law and stop on the absolute value of contracted coefficients. Conditioning on a future good event is invalid. State B,R>0, integer d≥1, and positive K. |
| 1 | §3.16 F52–F55 | The BS v3 comparison is at physical main.tex1181, preceded by1180;1184 is the subsequent threshold. The lost factor is L^((r/k−1)/2). The separate reciprocal typo is at1173. Neither finding refutes the theorem. |
| 2 | §3.15 F50–F51 | The current uniform result gives the shorter sufficient threshold t≥13669k². Register it as a new ordinary consequence. The current named explicit Lean threshold is3499200k², not13669k². |
| 2 | §3.11 F25; §3.12 F33 | The exact source keeps K,Lambda parameters and uses v:Bool→Real. The2^-r tail follows by substitution. Arbitrary bounded real leaf labels are an ordinary generalization, registered separately. |
| 2 | §3.16 F56–F60 | The SSW theorem needs1≤r≤n and an unspecified absoluteC. The restriction coefficient is zero when its index set is not entirely free. Variable error, arbitrary powers of two, and external SSW remain outside current local endpoints. |
| 3 | §3.13 F35–F39 | Explain the hard mean with squared path coefficients and only marginal second moments. In the source, mass_ge gives a mean difference; ext_PhiF_zero is needed for the hard mean alone. |
| 3 | §3.16 citations | Correct equation references to F24, F22–F23 and F39; distinguish Kewen Wu from Pei Wu and the SSW PDF/HTML numbering. |

## Concrete simplification attempts

### Finite-polynomial interpolation

The original analytic architecture justifies differentiation under expectation. Here only the first block contains the interpolation parameter. Expand the finite multilinear extension in that parameter: its degree is at most m and each coefficient is a bounded measurable function of the Gaussian vectors. Averaging the finitely many coefficients produces a polynomial. Differentiation is then finite linearity.

This simplifies the exposition without changing the measure or the Stein argument. It is registered as r3-forr-polynomial-interpolation. It is not presented as a new compiled source lemma. Bounded coordinate derivatives are still checked for every Gaussian integration by parts.

### Shorter threshold from an already proved uniform result

For k≤t and m=4^t, ln(4km)≤6t. Thus the current strict sharp theorem gives

\[
R(P)>\frac{m^{1-1/k}}{54675k^2t}.
\]

When t≥13669k², the denominator is smaller than4t² because4·13669=54676>54675. This directly dominates the defining floor of Lvalue. The same argument gives the slightly smaller ceiling threshold in the section.

This was independently checked in the proof and source-alignment passes. It is a sufficient threshold, not an optimal one. The old four-term NEW-FOR-25 proof is preserved in historical_threshold.md rather than silently removed.

### Preserve the exact formal identity

An integral over s would be mathematically valid after the polynomial argument, but the source endpoint uses one common mean-value parameter. The revised section uses that literal structure. This reduces a correspondence mismatch and makes the pointwise derivative estimate apply at one shared bias.

### Conservative SSW comparison

The comparison uses the same second-moment leakage and old dimension condition m≥2^(15k+2). With amplified error at mostδ, F42 gives Γ≥a−4δ≥7a/8. This slightly weaker intermediate gap still gives the same coefficient1/(162eC²), through the factor(21/16)^(2/k)≥1. It avoids importing the round-two subgaussian null-tail argument into the main assignment.

## Mathematical taste assessment

The main mechanism is the passage of a raw derivative through the labelled blocks. The three-block calculation earns its space by showing exactly why the previous weight is untouched and both attempted repeated derivatives vanish. The general invariant then reads as an extension of a mechanism already visible.

The martingale proof states what is known at a query before using centeredness. Its stopping rule is the conceptual point; the finite exponential calculation supports it. This is preferable to citing a Fourier bound without showing how its measure and normalization match the application.

The moment calculation uses the same path coefficients as the cascade. Squaring the Walsh entries exposes the positive contribution and explains why no independence of correlated Gaussian coordinates is necessary. The final proof uses the simplest sufficient parameter choices and records what is and is not optimized.

The main remaining reader cost is the density of the derivative-growth proof. The section spends that cost on a complete argument, as requested for the long record. The separate evidence ledger prevents types and receipt inventories from interrupting those calculations.

## Paper-authoring receipt

**Target reader.** A researcher comfortable with basic query complexity, finite Fourier expansions, elementary Gaussian integration and conditional expectation, but not assumed to know the local Lean library or the previous notes.

**Contribution.** A self-contained replacement of §§3.6–3.16, with the exact promise and all-t fixed-k quantifiers, a complete direct proof, an explicit sufficient threshold, precise source comparison, and a traceable formal/evidence map. It is one contribution to the long record, not a final integrated paper.

**Proof spine.** Finite multilinear extension; bounded truncation and Stein identity; rounded Gaussian chain; reflected uniform endpoint; one-block differentiation; repeated Stein elimination; adaptive biased derivative growth; uniform and hard moments;2τ-run error reduction; all-input acceptance gap; sharp uniform estimate; floor threshold.

**Hard step made visible.** Both the repeated-coordinate cancellation and the safe stopping of the adaptive chaos are proved. Their hypotheses are not hidden under theorem names.

**Concrete example and limits.** The k=3 calculation writes all chain-rule terms. It is an explanatory instance, not a substitute for the general earlier-only induction. The monomial z_i z_j example fixes the raw derivative normalization.

**Claim/Lean alignment.** The fixed-k endpoint matches BansalSinhaLower exactly after unfolding. The current sharp endpoint keeps k,t natural, k≥2,15k+2≤2t, m=4^t, error1/3, and the frozen promise. The section labels the polynomial wrapper, the stronger threshold and arbitrary real-leaf generalization ordinary. SSW is external. Complete verbatim source interfaces plus ambient contexts are supplied; five selected declarations also have exact supplied elaborated #check output. There is no claim to have freshly reconstructed every minimized implicit-binder list.

**Citation roles.** OpenAI specifies the target. BS supplies the original theorem and Gaussian-chain antecedent; its identified display is audited separately. GTW supplies the adaptive martingale ancestry. SSW supplies the comparison-only external Fourier theorem. Tal supplies context; no rorrelation distribution theorem is transferred. Exact editions, page/theorem labels, primary URLs and archive hashes are recorded.

**Cold-reader difficulty and disposition.** Three separate model passes reviewed the whole ordinary proof, literature comparison, and source/evidence alignment. They found local precision defects—positivity, positive degree, absolute-value stopping, random-domain coefficient convention, and several cross-references—which were corrected. They reported no remaining substantive mathematical defect in the assigned proof. Reports retain their read snapshots and chronology; these are not independent human endorsements.

**Exact open boundary.** No fresh Lean/Lake executable was available. Supplied current successful records were audited with matching local byte bindings. The sharp uniform endpoint is not Comparator-listed. No local formal SSW theorem, arbitrary-error endpoint, smaller subgaussian threshold, arbitrary-power-of-two public endpoint, or newly compiled13669k² wrapper is claimed. External dependency installations and compiled object files were not independently replayed. The semantic review restates and checks the intended promise and normalization in ordinary mathematics; no separately compiled independent semantic challenge was produced.

**Rendering and validation.** No PDF or typeset rendering of the return was produced. The requested Markdown source was read, its math delimiters and every numbered reference checked, and all numbered/unnumbered displays mapped. The bibliography is version-specific text, not a rendered citation-engine output. The literature reviewer visually inspected the supplied BS p.38 and SSW p.35 source-PDF renderings. The return checker verifies JSON, statement IDs, exact excerpt boundaries, declaration membership fields, hashes, and exact rational/integer constants. Those checks are not a kernel proof of the mathematics.

**Unavailable material.** Pasted text(20261102-190827).txt was unavailable. No content or extra instruction was inferred from it.

## Evidence controls

The evidence sidecars distinguish source presence, root receipt membership, exact Comparator membership, individual type/axiom output, focused native build, and headline dependency reach. These statuses are not interchangeable.

The root and both Comparator records bind124 local source/configuration files; all hashes match. The accepted Uniform retry-3 target binds16 inputs; all match. The reviewed audit source, log and verdict match their recorded hashes. Historical preparation metadata marked unexecuted is not used as the successful verdict; older failures on different source hashes are not applied to the current endpoint.

The source snapshot was not modified. The return manifest describes every deliverable member except itself, avoiding a recursive self-hash. Reproducible structural and exact arithmetic checks are included. This record does not replace the integrating team's review or assert that any proposed wrapper has been accepted.
