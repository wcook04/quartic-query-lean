# Uniform Forrelation: research return

The main mathematical result is in **note.md**. It proves, using the published Fourier theorem of Sherstov, Storozhenko and Wu,

\[
R_{(1-\eta)/2}(P_{k,m})\ge
\frac{\eta^2}{162eC^2}
\left(\frac{m}{1+\ln(km)}\right)^{1-1/k}
\]

for \(k\ge2\), \(0<\eta\le1\), and power-of-two block size
\(m\ge24k\,32^{2k}\). Here \(C\) is the absolute constant in that Fourier theorem. A slightly smaller sufficient condition is
\(m\ge8\,32^{2k}\ln(8\,18^{k-1})\). The paper also reconstructs the numerical elementary bound

\[
R_{1/3}(P_{k,m})>
\frac{2}{18225}\,
\frac{m^{1-1/k}}{k^2\ln(4km)}
\]

under the same size condition, without the sharp external Fourier theorem.

## Files

| File | Purpose |
|---|---|
| note.md | Full mathematical argument, exact finite-parameter form, source comparisons, and scope. |
| references.bib | Verified bibliography with pinned versions and exact locators. |
| lean_blueprint.md | Small implementation targets, proofs, existing source dependencies, and unelaborated signatures. |
| checks.py | Standard-library exact rational and integer checks. Run with Python 3.10 or newer. |
| checks_output.txt | Recorded output from the final packaged version of the script. |
| bansal_sinha_section54.md | Independent source audit, a counterexample to the displayed comparison, the weaker surviving exponent, and a replacement argument. |
| NEW_STATEMENTS.json | Exact statements, dependencies, proposed signatures, and explicit formal-status distinctions. |
| STATEMENT_CHANGES.json | Changes relative to the earlier return and corrections to source interpretation. Historical source records are not modified. |
| correspondence.json | Anchored passages mapped to statement identifiers and existing source declarations. |
| LEAN_GAPS.md | Reading-order account of every remaining formal obligation and route difference. |
| read_receipt.json | Scoped reading and verification record, including source limitations. |

## Interpretation

The \(2/18225\) constant checks, including the existing padded depth. The earlier dimension threshold was sufficient but unnecessary for this argument. Conditioning the uniform distribution on every block except an endpoint gives an exponential tail and permits the smaller threshold above.

The inequality at Bansal–Sinha v3, `main.tex:1184`, has a missing logarithmic factor for \(k\ge3\). The original multi-level estimates yield denominator exponent \(1-1/[k(k-1)]\). The single-block argument with SSW restores \(1-1/k\) in the explicit range above. This is a diagnosis of a proof step and a replacement argument, not a counterexample to the theorem.

No new Lean compilation is claimed. The supplied model specializes block sizes to \(m=4^t\); the paper allows every power of two. The sharp Fourier theorem remains an explicit hypothesis in the proposed formal endpoint. The manuscript states the AI-assistance disclosure and has not received human review.

The finite tests supplement the universal proofs. The metadata checks verify filenames, JSON structure, passage endpoints, and statement references; they do not check the semantics of Lean types.
