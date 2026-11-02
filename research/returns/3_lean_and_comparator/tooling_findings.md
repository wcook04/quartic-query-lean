# Tooling audit: evidence, corrections and licences

Audit date: 1 November 2026. This is a source audit, not an execution receipt. Public source files were opened through the public GitHub reader. Full commit identities were obtained from GitHub's commit endpoint. The initially read branch/tag files were subsequently re-fetched by full SHA and their contents compared equal. No private repository, mailbox, credentials, submission endpoint, or GitHub Actions dispatch was accessed.

## Conclusions that change the attached plan

1. **The toolchain decision has already moved on.** The trace's final build configuration and `lean/current/lakefile.toml` use complexitylib `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` with Lean `v4.36.0-rc2`. The earlier `verification_tooling.md` recommendation for `v4.35.0` was made before that change. Its pinned dependency manifest resolves CSLib `254e30e6d4299c51323aaeaf5f51a4763b375d4a` and Mathlib `69552756cd8a2d2d48763cf7279fd814d6a1224d`; all three selected toolchain files agree on `v4.36.0-rc2`. The exact Lean release commit is `b35cb10cf2ced51a2fd1880cfdbf75c71ab7a35a`. These are compatibility declarations, not successful build results.
2. **complexitylib is proof-side-only under the current Palomar allowlist.** The accepted CSLib repository is `leanprover/cslib`; there is no complexitylib alias or root. This changes how the advertised definitions must be presented. A theorem bridge to an imported model is needed, while the trusted Challenge keeps a compact independently auditable statement model.
3. **A `Statement` module is a useful implementation pattern, not a universal requirement of Comparator.** A Challenge that only uses existing Mathlib definitions needs no duplicated new definitions. When this paper introduces its own function/model definitions, the shared-source pattern is appropriate. It still needs an actual comparison because identical-looking text under different elaboration contexts need not yield identical `ConstantInfo`.
4. **The module system matters now.** `Drift.lean` begins with `import Mathlib`, not `module`. The checked Palomar source rule will reject that unchanged source. Public declarations, public imports and exposed definitions must be ported together; a header-only edit is insufficient. The actual source header test was inspected in `source_requirements.py`, not inferred from a README.
5. **An assumption library implemented with global axioms is incompatible with the intended release gate.** The organisational exemplar's suggestion of one external `axiom` per file is appropriate only for explicitly incomplete developments. For this project's conditional published theorems, use local theorem parameters. `permitted_axioms` remains a subset of `propext`, `Quot.sound`, `Classical.choice`.
6. **`#print axioms` is not a conditionality detector.** A theorem `H → C` can use no custom global axioms and still leave all the mathematics in `H`. Export both the axiom closure and the remaining mathematical parameter propositions.
7. **Exit codes need interpretation.** The core command returns 1 for several failures, including errors raised during execution. Palomar's `comparator_verdict` demands an anchored mismatch/illegal-axiom diagnostic, or Lean's actual rejection, before treating it as a mathematical rejection. A negative control that fails to compile has not tested the intended mismatch.
8. **Core `lake check` and Comparator have different roles.** `lake check` audits default targets without a Challenge. Therefore keep deliberate Challenge sorries and negative fixtures outside the default proof-root import closure. Comparator separately checks the specified named declarations against the independent Challenge.
9. **The full paranoid kernel suite is not exactly Palomar's acceptance policy.** Palomar requires Lean and NanoDa, then attempts con-ron separately and records supported capacity/support declines. A strict `--paranoid` run additionally requires all bundled kernels. Both are useful, but their outcomes should not be conflated.
10. **The historical build has no completion evidence in the attachment.** Root trace notes N017–N019 still describe job `b982m25tv` as running/downloading. Earlier failures occurred at old toolchains/cache download stages. Neither a running job nor an earlier failure proves the current Drift theorem succeeds or fails. No runtime/session handle from the trace is live in this audit.

## Exact source checks

| Source inspected | What it establishes | What it does not establish |
|---|---|---|
| Lean `Lake/Check/Compare.lean` at `b35cb10...` | Statement equality, full ordinary declaration closure, named-definition-hole behavior | Equality of informal mathematical meanings |
| Lean `Lake/Check/Axioms.lean` at the same pin | Allowed axiom traversal through Solution proof/definition dependencies | Truth of explicit theorem hypotheses |
| Lean `Lake/CLI/Check.lean` at the same pin | Sandbox requirements, bundled-kernel handling, config fields, export/check commands | That binaries run in this particular workspace |
| PalomarSubmission `toolchains.json` at `14aa8d6...` | Minimum `v4.35.0-rc2` | Successful source or theorem checking |
| PalomarSubmission approved roots at the same pin | Exact three canonical roots and closure/alias policy | Approval of every repository under a related organisation |
| PalomarSubmission `verify_submission.py` (targeted functions) | Config/path/limit checks, licence detector invocation, kernel policy, protected exports, error classification | A successful prepare/execute run |
| PalomarSubmission `source_requirements.py` (full) | Module and physical-line rules, source traversal | Lean elaboration of a module header |
| PalomarPolicy CONTRIBUTING (relevant sections) | Submitter-facing source, metadata, licence and scope contract | Endorsement of this formalisation or its suitability |
| formalization.yaml v0.4 schema | Portable metadata structure | Validation of any proposed metadata file here |
| PalomarTemplate Challenge/script/license | Working design pattern and reuse terms | That its older explanatory comments supersede the current validator |

The design document's source list contains full pinned URLs. The pinned source inspection receipt is `sources/tooling_source_receipt.json`. The public source copies were also read during this audit; copying the entire third-party source tree is unnecessary for this design return.

## Licence inspection for tooling recommended here

| Component | Licence observed at the pinned source | Reuse decision |
|---|---|---|
| Lean 4 comparison, checker and CLI sources | Apache-2.0; root LICENSE and file headers read | Use the pinned released toolchain; if copying source, retain relevant notices |
| PalomarSubmission verifier/scripts | MIT; root licence read | Prefer executing a pinned checkout; if adapting scripts, retain copyright/permission notice |
| PalomarPolicy text, prompts and schemas | CC0-1.0 dedication; root licence read | Cite the exact policy revision |
| PalomarTemplate | Apache-2.0; root licence read | Adapt its rehearsal pattern with attribution/notices if copying code |
| mathlib-initiative/formalization.yaml | Apache-2.0; root licence read | Use the pinned schema; retain licence when vendoring |

The design adds no third-party code beyond short API/configuration examples. It does not recommend a new licence for the user's mathematical source PDFs. A code repository's licence does not automatically license every cited paper; keep their metadata separate. Licences of the mathematical libraries themselves are covered by the model/prior-art audit.

Pinned licence URLs:

- [Lean](https://github.com/leanprover/lean4/blob/b35cb10cf2ced51a2fd1880cfdbf75c71ab7a35a/LICENSE)
- [PalomarSubmission](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/LICENSE)
- [PalomarPolicy](https://github.com/PalomarRegistry/PalomarPolicy/blob/28bd48b9b71bbb2a82c718ce761d5a4220ef8e60/LICENSE)
- [PalomarTemplate](https://github.com/PalomarRegistry/PalomarTemplate/blob/2891de4c48955af824969a263d31b25e7a9a1406/LICENSE)
- [formalization.yaml](https://github.com/mathlib-initiative/formalization.yaml/blob/99c678e569c7c4c0772db297c5ddd5e4c9b6322e/LICENSE)

## Input coverage and boundaries

Read in full: `READ_ME_FIRST.md`; `lean/verification_tooling.md`; `lean/organisation_exemplars.md`; `lean/internal_inheritance.md`; `lean/current/Drift.lean`; `lean/current/lakefile.toml`; `lean/current/lean-toolchain`. The historical root trace's relevant prompt, final progress/build state and Comparator child scope were inspected. The complete 45,031-line trace contains duplicated command/output/patch representations and other agents' mathematical research; this audit did not pretend that searching those is a fresh verification of their claims. Root trace locations used: lines 8001–8140 and 8142–8164; Comparator child begins at 27848, with final findings/prompt at 34594–34623. The trace's own section index is offset from the actual physical line numbers in this attachment.

Not available here: the user's historical private repositories, Mac filesystem, old session jobs, private build logs beyond the attached trace, and the missing machine-readable tooling twin mentioned in the packet. None was accessed or reconstructed. Existing claims about disk capacity, installed Mac tools, CI costs, or remote repository cleanliness are historical observations, not new facts about the current environment.

## What would overturn the principal recommendations

- Direct Challenge imports of complexitylib become acceptable only after the exact declarations move into an approved canonical source closure, or the verified Palomar policy changes.
- The self-contained statement interface could be reduced if the chosen quantum model is proved equivalent to a compact standard definition already in an approved library.
- A failed actual v4.36.0-rc2 build would reopen implementation compatibility; matching toolchain strings alone do not settle that.
- A completed later receipt for `b982m25tv` would replace the attachment's “not yet verified” status; it is absent from this packet.
- A real Comparator result is needed to settle generated-declaration identity. A source hash or a mathematical equivalence proof cannot substitute for that runtime check.
- Palomar policy/toolchain changes after the checked commits require a new readiness pass. This report does not claim permanent eligibility.
