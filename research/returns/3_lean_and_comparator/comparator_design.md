# Comparator design and Palomar preparation

**Advisory design; no Comparator run, build, submission, registration, CI dispatch, or repository change was performed in this audit.** Source inspection date: 1 November 2026. All Lean examples below are unbuilt designs. This document supersedes the packet's recommendation to downgrade to Lean 4.35.0.

## 1. Decisions

Keep `leanprover/lean4:v4.36.0-rc2` and the attached `complexitylib` pin. Use the Comparator shipped in that toolchain. Keep the mathematical statement vocabulary in a small, Mathlib-based public interface and prove bridges to imported complexitylib/quantum developments on the Solution side. Publish separate conditional and unconditional declarations. External mathematical inputs must be explicit parameters of the conditional theorem, never extra entries in `permitted_axioms`.

There is an immediate packaging constraint: Palomar's approved `leanprover/cslib` is **not** `cslib-community/complexitylib`. The latter is not in the checked allowlist. Its status as a CSLib community project does not make it an approved Challenge import. A Challenge importing the current project's definitions, which in turn import complexitylib, has the same problem. This is why the local Statement module and the independently compiled Challenge must be generated from the same small source blocks. This recommendation would change if the exact needed definitions were upstreamed into an approved canonical dependency, or Palomar changed its allowlist. [S4, S5]

| Item | Checked revision |
|---|---|
| Lean release `v4.36.0-rc2` | `b35cb10cf2ced51a2fd1880cfdbf75c71ab7a35a` |
| complexitylib | `62ca5c21461b2482e8bd12b7cb9b4937d887a33a` |
| CSLib, as resolved by complexitylib | `254e30e6d4299c51323aaeaf5f51a4763b375d4a` |
| Mathlib, as resolved by complexitylib | `69552756cd8a2d2d48763cf7279fd814d6a1224d` |
| PalomarSubmission | `14aa8d6b3c2f14a8540605e37144560b9a00e7e7` |
| PalomarPolicy | `28bd48b9b71bbb2a82c718ce761d5a4220ef8e60` |
| formalization.yaml schema | `99c678e569c7c4c0772db297c5ddd5e4c9b6322e` |
| PalomarTemplate | `2891de4c48955af824969a263d31b25e7a9a1406` |

The complexitylib, CSLib and Mathlib `lean-toolchain` files all specify `v4.36.0-rc2`. Palomar's checked floor is `v4.35.0-rc2`, so the submitted toolchain is above the minimum. This verifies declared compatibility, not that the proposed bridges compile. Recheck the exact manifest after any dependency change. In particular, do not combine the current complexitylib pin with the older Mathlib `d13f23b7...` from OpenAI's release. [S1, S5, S7]

## 2. What Comparator establishes

At the checked Lean revision, `Lake.Check.compareAt` compares each configured theorem's declaration kind and constant value header, including its type and universe parameters. `Compare.loop` follows constants used in the statement and requires full `ConstantInfo` equality for ordinary dependencies. It does not accept two differently named definitions merely because someone can prove them extensionally equal. Definitions listed in `definition_names` are deliberate holes: their type and safety must agree, but their body is allowed to differ. The separate `checkAxioms` walk inspects Solution proof dependencies; the replay kernels check the exported proofs. [S1, S2]

Consequences for this project:

1. A theorem checked under a named Forrelation hypothesis is a theorem **about the implication**. A zero-custom-axiom audit does not establish the hypothesis. Retain an explicit hypothesis inventory extracted from the theorem type.
2. A passed comparison cannot establish that the Challenge states the paper's claim, that its hypotheses are satisfiable, or that a changed complexity model is equivalent to the standard one. These are separate mathematical obligations.
3. Do not put `F`, the winner predicate, the promised Forrelation problem, `R`, `Q`, or the bit oracle in `definition_names`. Otherwise the central mathematical object can change while the configuration still passes. Keep the list empty for the proposed corpus.
4. If a supporting theorem is named in `theorem_names`, its proof is a hole even when another compared declaration refers to it. If it is not named and is reached by the comparison closure, its complete declaration must agree. Avoid relying on an unlisted sorried helper.
5. A successful `lake build` cannot replace comparison. A mismatch may concern only the statement environment, while both modules individually compile.

## 3. Module layout

Suggested files, relative to the existing `lean/` project root:

```text
QuarticQuery/Statement.lean
QuarticQuery/Model/Randomized.lean
QuarticQuery/Model/Quantum.lean
QuarticQuery/Model/Bridges.lean
QuarticQuery/Construction/...
QuarticQuery/Tournament/...
QuarticQuery/LowerBound/...
QuarticQuery/Forrelation/...
QuarticQuery/Appendix/...
QuarticQuery/Results/Conditional.lean
QuarticQuery/Results/Unconditional.lean
QuarticQuery.lean
QuarticCorpus/Construction/Challenge.lean
QuarticCorpus/Construction/Solution.lean
QuarticCorpus/Construction/comparator.json
QuarticCorpus/Tournament/...
QuarticCorpus/DirectProduct/...
QuarticCorpus/ConditionalFamily/...
QuarticCorpus/Forrelation/...
QuarticCorpus/FinalFamily/...
QuarticCorpus/UniversalUpperBound/...
verification/NegativeSolutions/...
verification/receipts/...
verification/challenge_sources.json
```

The seven groups are an initial allocation, not a measured claim that seven Palomar entries suffice. Split a group further if its exact statement dependency closure exceeds the byte/line budget. One local Comparator configuration can cover many related statements. A future Palomar entry is defined by one configuration and its chosen declarations, not by a source ledger's row count. Keep row-to-declaration mappings explicit for aliases, definitions, and prose assertions.

### Canonical statement source

Use `QuarticQuery.Statement` as the canonical public namespace. Generate the common definition blocks and import header into `Statement.lean` and into each independent Challenge. `Statement.lean` contains the definitions needed by the development; each Challenge contains the dependency-closed subset needed by its own theorems. Retain the same declaration names, source ordering within each closure, options, universe declarations, and imported instances. Generate declaration blocks structurally; do not strip theorems with a regex.

The public interface should contain actual definitions of the standard mathematical objects. A model field of the form `quantumBound : Prop` with no concrete algorithm semantics is not a replacement for quantum query complexity. Bridges to imported code are theorems proved on the Solution side, not prose assurances.

The independent Challenge cannot import `QuarticQuery.Statement` under the checked Palomar rules. The Solution **can** import it, plus the full proof development, and state the same named theorem with the proof supplied by the internal implementation. Do not let the Solution import the Challenge. Use internal theorem names distinct from the compared names to avoid duplicate declarations. [S4, S5]

The generation invariant is stronger than a text diff: the ordinary exported constants in each Challenge's dependency closure must equal those imported by its Solution. Byte-identical source with different imports, private names, or elaborator-generated helper names can still fail. The real Comparator run is the acceptance test. [S1, S2]

### Export gate for the supplied core-definition draft

The companion `core_definitions.lean` currently uses namespace `QuarticQuery`; the extra `.Statement` namespace in this design is an optional organisation choice, not a required renaming. Freeze whichever namespace the implementation adopts before creating receipts.

In the reviewed draft, `forrelationNumerator` constructs `Fin k` indices with `by omega`, `decodePointer` constructs a bounded index with a `by positivity` proof, and `predecessorValue` embeds a transitivity proof in a `Fin` constructor. These are specific places where elaboration may introduce module-dependent auxiliary proof names. The `by classical` bodies of `randomizedDepth`, `project` and `Fkm` also need to be included in the export comparison. There has been no build or export, so this is a risk to check, not a claim that these definitions already fail.

Make the first complete Challenge from this exact core before investing in the long proofs. Compile the canonical definition blocks twice under the actual distinct Statement and Challenge module names; export the entire ordinary-constant closure reached by a characterization theorem; inspect any `_private` or auto-generated dependency names; compare the exported constant information. Record the source-block hash, imports/options hash and exported-body hash in `challenge_sources.json`. Require the corresponding actual Comparator canary to pass at the selected toolchain. A core file of about 20 KiB does not measure the eventual whole Challenge: add all type dependencies, theorem statements, documentation and generated helpers before counting the final artifact.

Where auxiliary proof identity fails, replace anonymous index proofs with named public helper lemmas and have definitions refer directly to those lemmas. If the helper proof itself has module-dependent elaboration, put its identical *statement* in each Challenge, list the helper in `theorem_names`, and provide its real proof in the Statement/proof development. Comparator then checks the helper as an additional theorem hole while requiring the definition body to retain the same helper reference. These supporting lemmas are genuine additional compared claims; never solve the mismatch by opening the containing definition as a `definition_names` hole. Naming helpers is useful but is not, by itself, proof that auxiliary-name identity is fixed.

For a ledger row that is a definition, do not put a `def` into `theorem_names`: the axiom pass requires those targets to be theorems. Compare its explicit characterization/evaluation theorem and keep the definition in that theorem's ordinary dependency closure. Account separately for a definition that is only present as vocabulary and for a theorem proving the properties the manuscript attributes to it.

### Lean module system

Every submitted `.lean` source must have the `module` header; `lakefile.lean` is exempt from that header but shares the 10,000-line limit. The current attached `Drift.lean` lacks `module`, so it is not yet source-policy-ready. Port it using public imports/declarations and exposed definitions as needed. Lean's module system makes names private by default; definitions need exposure if clients must unfold them. [S5, S6]

For the small mathematical interface, the intended header is:

```lean
module

public import Mathlib.Data.Real.Basic
-- Add only the specific Mathlib modules needed by the interface.

set_option autoImplicit false

@[expose] public section

namespace QuarticQuery.Statement
-- Public, fully specified definitions generated identically into Challenges.
end QuarticQuery.Statement
```

This header is a draft, not a compiled minimal import list. Avoid private declarations and anonymous proof terms in public definition types. If a proof is needed to construct a subtype, prefer a named public helper that is itself fixed and checked. Adding `module` alone to the attached file is not a complete port.

Keep Challenges, intentional negative fixtures, and unfinished drafts outside the default proof-library target. `lake check` audits the default targets and rejects forbidden axioms anywhere in their exported development; a root module importing a deliberately sorried Challenge would defeat that check by design. Build Challenges separately through Comparator. [S3]

## 4. Conditional route: assumptions are mathematical arguments

Maintain precise propositions for each unfinished input, with source, model convention, parameter restrictions, error probability, and resource bound. The provisional API may package related propositions in a `Prop` structure, provided every field expands to a concrete statement. Do not create global `axiom` declarations for these inputs.

Illustrative signature shape, using names whose definitions belong in the core model design:

```lean
-- Unbuilt schematic signatures; predicates must be defined concretely.
theorem nearlyQuartic_of_inputs
    (hForrelationUpper : ForrelationQuantumUpperBound)
    (hForrelationLower : ForrelationRandomizedLowerBound)
    (hSearch : CoherentSearchImplementation)
    (hAmplification : ExactWeightSamplingImplementation) :
    NearlyQuarticFamilyBounds := by
  -- The assembled proof will use exactly these parameters.
  ...
```

Do not collapse the whole desired result into a hypothesis called `ExternalInputs`. The intermediate parameter inventory should expose the actual mathematical work remaining:

| Input admitted first as an explicit hypothesis | Required content | Removal test |
|---|---|---|
| Forrelation quantum upper bound | Concrete promise function, bit/phase-oracle bridge, correctness on the promise, query count with dependence on fixed `k` | A built algorithm theorem transports to the selected `Q` definition and replaces the parameter |
| Forrelation randomized lower bound | Correct promise support, input length, fixed-`k` quantifiers, hard distribution/error threshold, exact logarithmic factors needed by the paper | Bansal–Sinha-style proof or an exact imported theorem, followed by the randomized-model bridge |
| Quantum search/amplification implementation | A coherent unitary implementation with fresh workspaces; actual success distribution and charged forward/inverse oracle uses; expectation and truncation separated | Imported/ported amplitude-amplification theorem plus model bridge and resource proof; no generic search axiom left |
| Adaptive direct-product lemma | The precise per-instance cap, adaptive interleaving, transcript conditioning and success event used by the planted-input argument | A direct proof in the chosen classical query model; completion cannot be inferred from a theorem with a different budget convention |
| Appendix inputs, if temporarily isolated | Polynomial method and total-function complexity inequalities with their own exact models | Independent appendix chain closes, or the precise imported declarations are transported |

The construction, uniqueness of a winner, certificate verification, finite drift identity, classical weight evolution, and bookkeeping estimates should be proved directly without adding new external assumptions. Conditional statements should be named `_of_<inputs>` or placed in an explicitly conditional namespace, while unconditional statements get different names and records.

Each time a hypothesis is removed, add a theorem that applies the conditional result to its newly proved witness. Do not silently edit the existing public Challenge from conditional to unconditional: that changes the statement of record, so it needs a new source hash, comparison receipt, and source-to-Lean reading. Completion means the final theorem has only the paper's mathematical hypotheses, not that an assumption structure was instantiated by another unproved declaration.

Forrelation is expected to dominate the remaining mathematics. The conditional route is therefore a useful intermediate outcome, but it must be described as conditional. This estimate would change if an independently checked theorem with matching input and error conventions were found.

## 5. Concrete Comparator configuration

Example configuration for a future tournament bundle; these declaration names are the proposed interface, not claims of existing compiled declarations:

```json
{
  "challenge_module": "QuarticCorpus.Tournament.Challenge",
  "solution_module": "QuarticCorpus.Tournament.Solution",
  "theorem_names": [
    "QuarticQuery.Checked.Tournament.expected_weight_eq",
    "QuarticQuery.Checked.Tournament.expected_weight_le_half"
  ],
  "definition_names": [],
  "permitted_axioms": ["propext", "Quot.sound", "Classical.choice"]
}
```

Do not use the current `QuarticQuery.Tournament.*` names for wrappers if importing the original proof module already declares them. Either make the proof module the Solution, or use distinct checked-wrapper names as above.

`enable_nanoda` is accepted but ignored by Palomar; `external_kernels` is not a submitter field. For local rehearsals, generate a separate protected configuration that names the toolchain's `nanoda_bin` and `con-ron` binaries. Do not commit that derived external-kernel configuration as the intended Palomar configuration. [S4, S5, S8]

## 6. Negative controls and their actual scope

Run a tiny positive control first. A negative run counts only if it reaches the intended semantic check and yields its expected diagnostic. A compiler error, missing dependency, exit 2, timeout, sandbox failure, or independent-kernel crash is not a successful negative control. The Palomar implementation explicitly distinguishes these outcomes; even exit 1 is ambiguous without the log. [S5, `comparator_verdict`]

| Fixture | Intended result | Required evidence |
|---|---|---|
| Correct named theorem, same public definitions | Accept | Exit 0 and all required kernels accept |
| Change `≤ W/2` to `≤ W` in Solution theorem only | Reject | `Challenge and solution theorem statement do not match` |
| Add/remove a Forrelation hypothesis in Solution only | Reject | Theorem-statement mismatch, not failure to elaborate |
| Change `F`, `Q`, oracle semantics, or comparison complementarity under the same public definition name on Solution side | Reject | `Const does not match between challenge and target` in ordinary closure |
| Proof of the correct theorem uses `sorry` | Reject | `Illegal axiom detected: 'sorryAx'` |
| Proof uses a custom Forrelation axiom | Reject | Illegal custom axiom diagnostic |
| Native computation proof depends on `Lean.ofReduceBool` | Reject | Illegal axiom diagnostic; use a kernel-checked proof route instead |
| A configured name is omitted or is a definition instead of a theorem | Reject | Missing-name or declaration-kind diagnostic |
| Source imports complexitylib in the Challenge | Reject at Palomar preparation/closure check | Exact forbidden-source-closure error; this is not a Comparator theorem mismatch |
| A Challenge exceeds byte/line limits | Reject at preparation | Exact size diagnostic with measured bytes and lines |

Also add semantic-review controls that Comparator alone **cannot** reject:

| Deliberate change | Why Comparator may accept | Independent gate |
|---|---|---|
| Weaken both Challenge and Solution together | They still agree | Frozen source statement hash, quantifier/model review, new reading required |
| Add `False` as a hypothesis to both | The implication is provable | Hypothesis inventory and satisfiability review |
| Put `F` in `definition_names`, then choose an easy replacement | Its value was explicitly left open | Policy that central definitions are never holes; compared characterization theorem if a genuine construction hole is unavoidable |
| Define “query cost” to ignore oracle uses | The chosen definition is internally consistent | Model-equivalence proof and resource accounting review |
| Record a conditional theorem as the unconditional paper theorem | Axiom audit sees no global custom axiom | Join validator comparing paper claim, formal statement relation, and open hypothesis inventory |

Calling these semantic controls “Comparator negatives” would overstate what the tool does. The combined release gate, rather than every individual checker, must reject them.

## 7. Palomar preparation dossier

The checked public interface rules are below. This project remains private in the historical trace. Preparing the files is possible now; an official `prepare` run clones a public GitHub commit, so it is not an offline check of that private snapshot. Do not publish a repository merely to complete a rehearsal. No public submission or registration is part of this task. [S4, S5]

### Source and paths

- Use one exact future 40-character commit SHA for the project and every Git dependency. Retain credential-free public GitHub dependency URLs in `lake-manifest.json`; `rev` is the resolved commit, even where `inputRev` records a tag or branch.
- The current nested `lean/` project is allowed. A future request would set `project_path` to `lean`; comparator and metadata paths are **repository-relative**, e.g. `lean/QuarticCorpus/Tournament/comparator.json` and `lean/formalization.yaml`.
- Put exactly one Lakefile in the selected project, commit the resolved manifest, keep `lean-toolchain` in the project or repository root, and keep one conventional unambiguous licence file at the repository root. Nested-project selection does not move the repository's licence rule into `lean/`.
- Every committed Lean source in the submitted repository needs the module-system header and at most 10,000 physical lines, except the Lakefile header exemption. This includes fixtures and contained projects; `.git` and `.lake` are excluded from the source scan.
- Each Challenge must be at most 102,400 bytes and 1,000 physical lines. A warning begins above 32,768 bytes or 300 lines. Measure UTF-8 bytes, not characters. Do not hide definitions as holes to fit the limit.
- Source checkout cap: 500 MiB. Lakefile and comparator configuration caps: 1 MiB each. Metadata cap: 256 KiB. Root licence file cap: 1 MiB. No symlink substitutes for the required files; no submitted-repository submodules; no Git LFS pointers; no compiled artifacts outside `.lake`.
- Challenge and Solution names must be distinct legal dotted module names, and resolve to regular source files inside the selected project. Challenge transitive imports must be exactly within approved canonical source closures.

These requirements were checked against PalomarSubmission's code and policy, including `source_requirements.py`, `load_comparator_config`, `allowed_roots`, `package_allowlist`, `repository_license_file`, and `prepare`. [S4, S5]

### Metadata

Use `formalization.yaml` version `v0.4`, with a concise description that names the exact formalized scope. Include human authors and responsible maintainers, root SPDX licence, source records, mathematical subject classifications, automation methods, and an accurate pre-submission review status. AI systems belong under automation, not authorship. The formalization is source-based: cite the OpenAI preprint with `type: paper`, `relationship: formalizes` (or accurately scoped `adapts`), and the exact paper hash/version. `type: preprint` is not in the checked Palomar vocabulary. The older template comments describe freer source types, so follow the current validator/policy instead of copying that comment. [S4, S9]

Record additional hypotheses and changed models in `status.scope`, `fidelity.divergences`, and per-result `literature_dependencies`; export the real axiom set and result types from built declarations. Never hand-type a zero-sorry or unconditional status before extraction. Classification should describe query complexity/quantum computation (candidate arXiv categories `cs.CC`, `quant-ph`), subject to checking the registry's taxonomy snapshot. Do not invent an ORCID or author endorsement. Mark independent review as absent unless actually performed.

### Rehearsal and evidence

On a suitable Linux environment, first compile the proof-only target from the locked manifest. Then run the positive and negative controls and all per-bundle comparisons. Commands are intended future checks, not completed checks:

```sh
lake build QuarticQuery
lake comparator --config QuarticCorpus/Tournament/comparator.json --paranoid
lake env leanchecker --fresh QuarticQuery
lake check --paranoid
```

The full `--paranoid` policy is stricter than current Palomar's requirement: Palomar requires Lean and NanoDa and separately attempts con-ron, allowing recognized support/capacity declines with explicit evidence. A paranoid run can therefore fail when Palomar's recorded mandatory checks would pass. Retain the individual kernel outcomes. A no-sandbox development run is not equivalent to the intended sandboxed receipt. [S3, S5]

For a future explicitly authorized public snapshot, the checked verifier command shape is:

```sh
python scripts/verify_submission.py prepare \
  --event /absolute/path/event.json \
  --work-dir /absolute/path/fresh-work \
  --output /absolute/path/prepare-report.json \
  --licensee /absolute/path/to/bundle
```

`--licensee` is the Bundler executable: the verifier itself invokes `bundle exec ruby scripts/detect_license.rb`. It is not a shell command string. The subcommand for capacity is `check-capacity`, not `capacity`. The event uses `inputs.repository`, `inputs.commit`, a 12-character lowercase-alphanumeric `inputs.request_id`, and a JSON-string `inputs.options` holding string-valued options including comparator path, project path and authorization relationship. This document deliberately supplies no completed event claiming authorization. `prepare` checks and clones the source; `execute` is the protected build/export/judging phase. A successful preparation report is not a proof receipt. [S5, S10]

## 8. Receipts and corpus joins

For each run store: source commit; selected project; toolchain and full Lean commit; exact manifest hash; Challenge/Solution/configuration hashes; declaration names; dependency closure; exported theorem types; axiom list; explicit mathematical hypotheses; required checker names and binary digests; command and working directory; exit status; stage; log hash; negative-control expected/actual result. Also store failures and unavailable results.

Every ledger row should join to one of: a compared theorem; a definition and its checked characterization theorem; a prose-only assertion with a reason why no Lean proposition is appropriate; or an explicitly open formalization obligation. A definition's presence is not a proof of the paper's claims about it. A theorem may cover several ledger rows, but each relation needs its own statement-level reading. Keep build, comparison, mathematical fidelity, informal proof review, and conditionality as separate fields, following the useful data-model separation in the attached `lean/internal_inheritance.md`.

The release criterion is not “118 rows have names.” It is that every mathematical assertion has a faithful formal statement, each claimed proof has a pinned receipt, and no remaining substantive hypothesis is represented as proved. For the final separation, include the actual function construction and model-equivalence statements in that obligation set.

## Sources

- **S1** Lean comparison implementation: [`Lake/Check/Compare.lean`](https://github.com/leanprover/lean4/blob/b35cb10cf2ced51a2fd1880cfdbf75c71ab7a35a/src/lake/Lake/Check/Compare.lean), especially `compareAt`, `definitionHoleMatches`, `Compare.loop`.
- **S2** Lean axiom traversal: [`Lake/Check/Axioms.lean`](https://github.com/leanprover/lean4/blob/b35cb10cf2ced51a2fd1880cfdbf75c71ab7a35a/src/lake/Lake/Check/Axioms.lean), `checkAxioms`, `Axioms.loop`.
- **S3** Lean execution/configuration: [`Lake/CLI/Check.lean`](https://github.com/leanprover/lean4/blob/b35cb10cf2ced51a2fd1880cfdbf75c71ab7a35a/src/lake/Lake/CLI/Check.lean), `Config`, `mkContext`, `verifyMatch`, `runComparator`, `standardAxioms`, `checkProject`; [Lean 4.35 release notes](https://lean-lang.org/doc/reference/latest/releases/v4.35.0/).
- **S4** [PalomarPolicy CONTRIBUTING](https://github.com/PalomarRegistry/PalomarPolicy/blob/28bd48b9b71bbb2a82c718ce761d5a4220ef8e60/CONTRIBUTING.md), sections 2, 3, 5, 6.
- **S5** [PalomarSubmission verifier](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/scripts/verify_submission.py), [approved roots](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/allowed-challenge-repositories.json), [source rules](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/scripts/source_requirements.py), [toolchains](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/toolchains.json), [declaration-closure note](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/docs/comparator-declaration-closure.md).
- **S6** [Lean reference: source files and modules](https://lean-lang.org/doc/reference/latest/Source-Files-and-Modules/), sections 5.3–5.6; [PalomarTemplate Challenge](https://github.com/PalomarRegistry/PalomarTemplate/blob/2891de4c48955af824969a263d31b25e7a9a1406/Challenge.lean).
- **S7** [complexitylib manifest](https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/lake-manifest.json), [complexitylib toolchain](https://github.com/cslib-community/complexitylib/blob/62ca5c21461b2482e8bd12b7cb9b4937d887a33a/lean-toolchain), [resolved CSLib toolchain](https://github.com/leanprover/cslib/blob/254e30e6d4299c51323aaeaf5f51a4763b375d4a/lean-toolchain), [resolved Mathlib toolchain](https://github.com/leanprover-community/mathlib4/blob/69552756cd8a2d2d48763cf7279fd814d6a1224d/lean-toolchain).
- **S8** [PalomarTemplate rehearsal script](https://github.com/PalomarRegistry/PalomarTemplate/blob/2891de4c48955af824969a263d31b25e7a9a1406/scripts/verify-comparator.sh).
- **S9** [formalization.yaml v0.4 schema](https://github.com/mathlib-initiative/formalization.yaml/blob/99c678e569c7c4c0772db297c5ddd5e4c9b6322e/schema/v0.4.schema.json); [current metadata validator](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/scripts/submission_contract.py).
- **S10** [workflow input validation](https://github.com/PalomarRegistry/PalomarSubmission/blob/14aa8d6b3c2f14a8540605e37144560b9a00e7e7/scripts/workflow_inputs.py) and `submission_request` in S9.
