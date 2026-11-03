# Review notes and verification of existing arguments

This file documents checks on arguments already present in the supplied sources. It contains no replacement manuscript or proposed new theorem. Finding numbers refer to the final `findings.json`.

## Mathematical assessment

The inspected randomized lower-bound proof has the required structure:

1. One hard law makes every depth-\(L\) deterministic solver fail often enough.
2. The dummy and planted inputs share the address data and differ only at the erased zero and the selected cell.
3. First-difference coupling reduces their acceptance gap to those two events, both measured on the dummy run.
4. Independence of the planted index gives the exact identity \(\Pr[\mathrm{hit}]=\mathbb E Z/m\).
5. A bounded-query search estimate controls the erased-zero event.
6. Heavy columns are few. For each remaining target/time, a simulator stops before query \(L+1\) to the target tuple. Its total cap implies every separate cap, and original-run light-and-correct is contained in simulator success.
7. A union over times and an average over the independent uniform column give \(G\beta^r\), without an extra factor \(m\).
8. Fixing and averaging coins preserves the deterministic discrepancy bound, contradicting a pointwise bounded-error solver.

These are the supplied preprint §4 and reasoning record §§6.1–6.6, not an additional proof offered by this return. The formal-scope criticisms concern how existing types are described and linked. They do not establish a failure of the mathematical theorem or of its Lean proof.

## Existing finite examples

All fractions below were recomputed exactly, not through simulation. See `checks/finite_checks.json` and the accompanying standard-library script.

| Existing example | Recomputed result | Interpretation |
|---|---|---|
| AND on the uniform promise \(\{01,10,11\}\) | One-query optimum \(2/3\); cap event and correct-and-capped both \(1/3\); conditional success \(1\) | The one-instance conditioning counterexample is correct. |
| Adaptive two-instance AND on 16 equally likely inputs | 8 capped, 5 correct-and-capped; joint \(5/16\), conditional \(5/8\), product bound \(9/16\) | The second counterexample is correct. The repeated query deliberately spends budget. |
| Same two-AND law with a pooled budget of two queries | Compute first AND exactly, guess zero for the second: success \(3/4>9/16\) | Existing record §6.1 supplies the missing pooled-cap teaching bridge. No adaptive allocation across instances is needed for this example. |
| Two parity instances with a shared fair coin selecting exact computation or zero-query guesses | Expected cost 1 per instance; success \(5/8>1/4\) | Expected caps cannot replace worst-case separate caps. |
| Four independent zero positions, one row queried in each column | \(\mathbb E Z=1\); independent-column hit \(1/4\); dependent selection hit \(175/256\) | The dependent selector has uniform marginals only after the no-discovery branch is completed symmetrically. |
| No-discovery branch of the preceding example | Probability \(81/256\); uniform fallback gives each index marginal \(1/4\) | This is the omitted sampling rule identified in CM-006. The record already specifies it. |

## Constants and quantifiers

The following checks use the formulas already displayed in the drafts and record. They do not independently prove the analytic Forrelation estimate on which the final threshold relies.

- For \(r=40t\), \(m=4^t\), the tail inequality follows from \((2/3)^2=4/9\le1/2\): \((2/3)^r\le2^{-20t}=m^{-10}\).
- With \(G\le mL/100\) and \(L\le m\), the companion’s sharper erased-zero term is at most \(2/100\), the heavy term at most \(1/100\), and the tail at most \(1/100\). Its \(4/100<1/3\) envelope is valid. The exposition’s coefficient-four search bound gives \(4/100+1/100+1/(100m^8)<1/3\); the record’s looser \(6/100\) envelope is also sufficient.
- The floor argument uses \(t\ge8\): \(4t^2\le2^t\le m^{1-1/k}\), with equality in the first inequality at \(t=8\). Applying the existing \(\lfloor x\rfloor\ge x/2\) estimate twice yields \(1/400\) in the required direction; \(mL\ge200\) is comfortably satisfied.
- The arithmetic in the explicit threshold is consistent: \(8\cdot13669=109352>109350\). Thus \(t\ge13669k^2\) gives the displayed strict comparison. This verifies the numerical transfer once the separate uniform Forrelation bound and its logarithmic estimate are assumed; it is not a re-verification of their full proofs.
- Fixed \(k\) is chosen before taking \(m\) large. The separate growing-\(k\) remark identifies additional uniform inputs. No exact \(R=\Omega(Q^4)\) conclusion is supplied by the fixed-\(k\) argument. Its signposting should survive revision (CM-028).

## Objections considered and rejected

These checks prevent the report from asking the authors to repair correct material.

**A matching classical upper exponent is available.** An initial proposed criticism of the overview’s \(L\approx R(P)\approx m^{1-1/k}\) was withdrawn. Bansal–Sinha v3, printed p. 3, explicitly gives a randomized \(O(2^k m^{1-1/k}\delta^{-2})\) query upper bound for the exact promise; footnote 1 covers odd \(k\) via bounded block-multilinear approximation. For fixed \(k\), \(\delta=2^{-5k}\) is constant, so the overview’s scale, with logarithms suppressed, is defensible. A lower-bound-only claim about that cited source would be wrong. This does not remove the separate CM-004 issue: the overview must keep the erased-zero alternative when explaining necessary algorithmic behaviour. [Primary source](https://arxiv.org/pdf/2008.07003v3), p. 3.

**The rendered planted figure is not off-promise.** Figure 2’s earlier toy board contains an unpromised address input, but exposition Figure 4 replaces all address labels by samples from \(\mu\). It should not be reported as a mathematically inconsistent hard-distribution picture. The missing SVG source remains a reproducibility issue (CM-014).

**The pooled-cap AND example needs no new construction.** Record `CL-adaptive-example` already computes its \(3/4\) success under a two-query pooled budget. The general Shaltiel obstruction uses a further allocation mechanism; that mechanism is not necessary for this simple counterexample (CM-017).

**Intentional challenge placeholders are not proof evidence or proof failures.** The supplied Challenge files intentionally use `sorry` as specifications, with separate solutions/configurations. This review checked statement meaning and correspondence, not a standalone build of a specification.

**Missing files do not imply CRC corruption.** The source-figure omissions and imported-definition omissions coexist with a byte-consistent input manifest. Nor does a valid line range prove that the imported vocabulary has the intended semantics. These are different checks.

## Earlier editorial findings: current status within this job

| Earlier issue | Current assessment |
|---|---|
| History and credit | History sequence and cheat-sheet arithmetic are much improved (CM-034). Explicit Forrelation/rorrelation/Fourier distinctions, outward-pointer novelty and precise fair-tree provenance still need correction (CM-001, CM-007–008, CM-022–023). |
| One-line reason for four | Present in both drafts. Keep it; retain the erased-zero route in the classical preview (CM-004). |
| Quickly auditable formal statement | Headline guide works well (CM-029–031). Extend its definition-level navigation to auxiliary classical targets (CM-009–012, CM-021). |
| Formal scope overreach | Existential exponent versus explicit constants is now distinguished. Finite versus arbitrary probability-space wording still needs correction. Pending rebuild status was excluded from findings as instructed. |
| Known material versus delicate points | Core simulator details are explicit and should stay. The early minimax box and two overlapping AND examples still interrupt the exposition’s mechanism (CM-015–016, CM-019). Full quantum-section balance was outside this focused audit. |
| Rendered/document delivery defects | Two malformed headings and three omitted SVG sources remain (CM-013–014). No claim is made about uninspected PDF pages. |
| Independence and joint-event subtleties | Substantive proofs now handle them correctly (CM-024–026, CM-033). First descriptions and the finite counterexample still need the located repairs (CM-002–003, CM-005–006). |
| Exposition frame and figures | Overview, roadmap and examples are present. The planted-pair figure communicates the two changed locations. The original concern is substantially resolved, subject to the current source omissions. |
| Logarithmic exponent derivation | A derivation of the displayed six is present and its formal evidence is distinguished. The quantum cost calculation was not independently reconstructed in this classical review. |
| Notation and preprint equation numbers | Expert displays now carry P-number mappings. No separate classical notation defect was established. |
| Growing-\(k\) remark | Clearly separated and explicitly dependent on uniform inputs. The complete uniform analytic proof was not independently re-audited. |
| Abstract register | Main result, exponent mechanism and attribution appear before the formal audit claim. No additional classical-scope finding was needed. |
| Version-specific source criticism | Not prominent in the short drafts. The record keeps the version-specific issue separately; this review did not re-audit that disputed analytic step. |
| Internal project vocabulary | Main classical proofs use mathematical language. Detailed implementation names remain in formal evidence/navigation, where their role is explicit. |

The principal priorities are the exact findings, not this status table. Revisions should improve the existing argument without adding new mathematics or enlarging the manuscripts.
