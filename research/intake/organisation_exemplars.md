# Organisation exemplars for Lean paper-formalisation repos

Read on 2026-11-01 via `gh api` only (git trees + raw contents); nothing cloned, nothing written to GitHub. All repo text is treated as data. SHAs are the default-branch head at read time. "Not read" means the tree was listed but file bodies were not opened.

## Per-project notes

### leanprover-community/mathlib4 @ 16b5a1bae01ff8aadfe0e4bcf490c12a66a965c3 (master)
Inspected: root listing; `lakefile.lean`; `Wanted.lean`, `Wanted/**` (17 stub files); `docs/100.yaml`; `scripts/README.md`, `scripts/nolints.json`, `scripts/` listing; `Mathlib/Tactic/Linter/` listing; `.github/workflows/` listing, `export_crossrefs.yml`, `technical_debt_metrics.yml`, `decls-diff.yml`; `Archive/`, `Counterexamples/`, `MathlibTest/`, `DownstreamTest/` listings.
- Layout: library `Mathlib/<Area>/…` mirrors subject; `Archive/` (showpieces), `Counterexamples/`, `MathlibTest/`, `Wanted/` (statements of desired results as separate lib), `DownstreamTest/` each have their own root `*.lean` importing everything.
- Gates: lint options set once in `lakefile.lean` (`mathlibStandardSet`, header linter, `longFile` 1500, `autoImplicit false`); `lintDriver`; `scripts/nolints.json` is a machine-readable exemption list; weekly "technical debt counters" workflow; per-PR declarations diff comment from an import-graph artifact; `shake` for unused imports; deprecation tooling (`add_deprecations.sh`, `fix_deprecations.py`).
- Machine outputs: `@[wikidata]`, `@[stacks]`, `@[kerodon]` tagged declarations are exported to `crossrefs.json` (name, file, line, ids) and pushed to a separate repo by `export_crossrefs.yml`; `docs/100.yaml` (Freek's 100 theorems: title, decl, authors) is validated by `scripts/yaml_check.py` and consumed by the website repo.
- Trust split: CI automation that touches GitHub or secrets lives in a separate repo (`mathlib-ci`), `scripts/` keeps only local tools (stated in `scripts/README.md`).

### AlexKontorovich/PrimeNumberTheoremAnd (PNT+) @ 127b50e33f6033e2147921167a117af96d9ba4ea (main)
Inspected: root listing; `lakefile.toml`; `CONTRIBUTING.md`; `.github/workflows/` listing and `build.yml`; `PrimeNumberTheoremAnd/Rectangle.lean`, `Wiener.lean` (blueprint attribute sites); `blueprint/src/blueprint.tex`, `web.tex`; `scripts/` listing. Not read: `PULL_REQUEST_STYLE.md`, `intentions.yml`, `update.yml`.
- Layout: flat topical files `PrimeNumberTheoremAnd/*.lean`, plus `Mathlib/` (upstream-bound), `Tactic/`, `Unused/`, `IEANTN/`, `Backlund/`; `blueprint/src/`, `home_page/` (Jekyll), `errata/`, `examples/`, `scripts/`.
- Blueprint now generated from Lean: `require LeanArchitect`; `@[blueprint "label" (title) (statement := /-- LaTeX -/) (proof := /-- LaTeX -/) (latexEnv := "lemma") (discussion := 561)]` on the declaration; `build-args: :blueprint`; `blueprint.tex` only `\input`s `.lake/build/blueprint/library/PrimeNumberTheoremAnd`. `blueprint_comment /-- … -/` carries prose between nodes. `discussion := N` ties a node to a GitHub issue number.
- Contributor flow: issue comments `claim` / `disclaim` / `propose #PR` / `withdraw #PR` / `awaiting-review` drive a GitHub project board via workflows; separate `PULL_REQUEST_STYLE.md` (AI-assisted contribution section) and an `auto-label-ai-disclosure.yml` workflow.
- Docs: `leanprover-community/docgen-action` (blueprint + API docs) and `upstreaming-dashboard-action` (what can move to Mathlib).

### teorth/analysis @ a19a5bfadc616467562995b75f46035232841943 (main)
Inspected: root listing; `Analysis/` listing; `README.md`; `CONTRIBUTING.md`; `literate.toml`; `Analysis/Section_2_2.lean` head; `.github/workflows/build_book.yml`.
- Layout: one Lean file per textbook section, `Section_<ch>_<sec>.lean`, plus `Appendix_*`, `*_epilogue` (bridge to Mathlib), `Misc/`, `MeasureTheory/` (excluded from the book via `literate.toml`).
- Paper-to-Lean link is the filename and in-docstring numbering ("Definition 2.2.1"); exercises are `sorry`; README lists every section with Verso page, docs, and source links (hand-written).
- Style rule worth noting: faithfulness over golfing; `warn.sorry=false` set on purpose. CI builds, then doc-gen, then a Verso "book"; Python tests cover the preview tooling.

### teorth/equational_theories @ 843bf996358a57ea53c57e748b352750978239f2 (main)
Inspected: root and `scripts/` listings; `equational_theories/` listing (Generated/, EndToEnd/, Equations/, ManuallyProved/); `EquationalResult.lean` (first ~140 lines); `EndToEnd/README.md`; `CONTRIBUTING.md`; `data/README.md`; `.github/workflows/lint.yml`, `blueprint-paper.yml`; head of `full_entries.json`.
- The strongest machine-readable design seen: attribute `@[equational_result]` on a theorem parses its type into an `Entry {name, filename, line, variant, proven}` stored in a persistent environment extension; the handler runs `collectAxioms` and throws on any axiom outside `propext, Classical.choice, Quot.sound` (a special `Conjecture.conjectureAx` flips the entry to `proven := false`). `scripts/extract_implications.lean` dumps it; `full_entries.json`, `data/*.csv.zip`, `outcomes.json.zip` are the published snapshots; dashboards, graphs and the "most wanted" list are generated from these by `scripts/generate_*.py`.
- Layout: hand proofs in `ManuallyProved/`, machine-found results in `Generated/` (one folder per generator), a final `EndToEnd/` that checks a certificate covering all pairs; extra kernels `scripts/lean4_checker`, `scripts/lean4lean_checker`.
- Hygiene: pre-push hook script, lint workflow bans `import Mathlib` and lines over 100 characters, project board with claim flow, snapshots dated in the filename (`2024-11-10-outcomes.json.zip`).

### ImperialCollegeLondon/FLT @ a3210204ad8876e851e32f73dd97d882bf1ccd0a (main)
Inspected: root and `FLT/` listings; `README.md`; `CONTRIBUTING.md`; `lakefile.toml`; `FLT/Assumptions/README.md`, `Mazur.lean` head; `FLT/Proof.lean` head; `blueprint-verso/BLUEPRINT_VERSO_HINTS.md`, `Chapters/Level02ReductionToPrimeCase.lean` head; `.github/workflows/blueprint.yml`. Not read: `api-docs.yml`, `tasks.py`, `FLTTest/`.
- `FLT/Proof.lean` is the "main spine": statements B_1..B_12 and a chain of implications, so the whole argument is readable in one file.
- `FLT/Assumptions/`: one `axiom` per file, each a precisely cited theorem known by 1989, with a README index and a GitHub issue per axiom. `FLT/Slop/` is a quarantine folder for low-quality AI output. `KnownIn1980s/` for definitions of known material.
- `blueprint-verso/` is a second blueprint in Verso: `:::definition "label" (parent := "…") (lean := "FLT.Bosses.B2")` directives bind prose to a declaration name.
- Gates: precise-imports check in a `style_lint` job; `lean-action` with `build`, `test`, `lint`, `mk_all-check`; `checkdecls` dependency (verifies every `\lean{}` name exists); `warn.sorry=false`; expensive API docs built on demand and republished from a release asset to keep merges fast.

### fpvandoorn/carleson @ 52cba54d4b7b444e937c7abbc67835afa2a0bb16 (master)
Inspected: root and `blueprint/` listings; `formalization.yaml` (full); `comparator_config.json`; `Challenge.lean`; `Solution.lean`; `.github/workflows/push.yml`; `review_checklist.md`. Not read: `CONTRIBUTING.md`, `tasks.py`.
- `Challenge.lean` states the headline theorems as `:= sorry` with primed names; `Solution.lean` proves each by aliasing the real theorems (`:= @classical_carleson`); `comparator_config.json` lists `challenge_module`, `solution_module`, `theorem_names`, `permitted_axioms`. CI builds `Carleson Challenge Solution`.
- `formalization.yaml` (v0.4) records `status.sorry_count`, `sorry_in_definitions`, `axioms`, and per main result `{declaration, file, sorry_count, axioms, comparator_config, literature_dependencies}`; also `fidelity.divergences`, `review.status`, `automation.methods`.
- Paper is built in CI (`paper/main.tex` to `docs/paper.pdf`) next to the blueprint; `Carleson.ToMathlib` is the upstreaming staging namespace (`search-root` of the upstreaming dashboard).

### teorth/pfr @ 7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f (master)
Inspected: root, `PFR/`, `PFRPalomar/`, `blueprint/src/chapter/` listings; `formalization.yaml` head; `comparator.json`; `blueprint/src/chapter/entropy_pfr.tex` head; `.github/workflows/push.yml` (first 60 lines); `tasks.py` head.
- Classic leanblueprint: chapters in `blueprint/src/chapter/*.tex`, one per Lean topic file; each environment carries `\label{}`, `\lean{decl}`, `\leanok`, `\uses{labels}`; proofs get their own `\uses`.
- `PFRPalomar/{Challenge,Solution}.lean` plus `comparator.json` give six theorems checked with permitted axioms; the `formalization.yaml` description states the result as "no sorry outside the six deliberate holes".
- Style CI extra: `PFR/Mathlib` may not import other `PFR.*` modules (upstream-ready subtree rule); "file dependencies" step on master.

### google-deepmind/formal-conjectures @ d995ef5d306637c0a2e489c7e579647168d7df2f (main)
Inspected: root, `FormalConjecturesUtil/` and `scripts/` listings; `AGENTS.md`; `STATEMENTS.md`; `PROOFS.md`; `FormalConjectures/ErdosProblems/1.lean`; `FormalConjecturesUtil/Attributes/Basic.lean` (grep of types); `scripts/extract_names.lean` head; `scripts/check_erdos_status.py` head; `build-and-docs.yml` step names; `Linters/FormalProofLinter.lean` head. Not read: `CONTRIBUTING.md`, individual linters other than the proof one, `generate_fc_subsets.py`.
- Statement repo: nearly everything is `sorry` by design. Layout by source (`ErdosProblems/<n>.lean`, `Arxiv/`, `Books/`, `Wikipedia/`, `OEIS/`…), shared maths in `FormalConjecturesForMathlib/` (no `sorry`, no `native_decide`, Mathlib quality), tooling in `FormalConjecturesUtil/`, tooling tests in `FormalConjecturesTest/`, curated `Subsets/`.
- Per-statement metadata as attributes: `@[category research open|research solved|textbook|test|API, AMS 5 11, formal_proof using lean4 at "<url>#L…", question yes_no|value]`. Value questions define `<theorem>.answer := sorry` first. Linters enforce category, docstring, AMS, imports, copyright header, and that a conditional `formal_proof` names its sorried hypotheses.
- `lake exe extract_names` reads built `.olean` files and emits JSON of names, statements, categories, subjects, proof links. `check_erdos_status.py` diffs repo status against upstream `teorth/erdosproblems` `problems.yaml` and can open issues.
- Rules worth stealing: "never add `axiom`, `opaque`, or `constant`"; `#print axioms` before claiming proved; `AGENTS.md` with a short, imperative contract; `∃ x, P x → Q` trap checklist; boundary-case table (`ZMod 0`, `x/0`, `sInf ∅`).

### openai/math, `lean/` folder @ 4eaee87548250b2682affda7d05d947c05554bae (main; repo tree truncated at 55173 entries, so `lean/` read through the contents API)
Inspected: `README.md` (root), `lean/` listing, `lean/OAI/` top listing, `lean/ComparatorChallenges/` listing, `AffineBernstein.json` and `.lean`, `ComparatorChallenges/README.md`, `lean/formalization.yaml` (head, source list, `status.main_results` start, dependency list), `lean/docs/017.md`, `lean/README.md`, `CONTENTS.md` head, `.github/workflows/` listing. Not read: `history.md`, `lean/patches/`, `lean/OAI/Internal/`.
- One big library `OAI/<Subject>/<Result>/Main.lean`; one `ComparatorChallenges/<Name>.lean` + `<Name>.json` per headline result (challenge module, solution module, `theorem_names`, `definition_names`, `permitted_axioms`, `enable_nanoda`).
- `lean/formalization.yaml` is a catalogue: `sources` (one per paper, `id` is a relative path to the PDF), `status.main_results` rows `{comparator_config, declaration, file}`, related repos with pins. `lean/docs/NNN.md` is a per-family scope note: what the formalization proves, what it leaves out, table linking the comparator file. Family numbers join papers, docs, and Lean.
- Honest scope text ("Partial progress", "outside this selected statement") sits beside each result.

### math-inc/strongpnt @ 2f5835c322314f55f1026ec2f139d704b7c45c69 (main) and math-inc/Sphere-Packing-Lean @ 1e98fb493088948ca7bbf47d7faed49cc5b39fc4 (main)
Inspected: strongpnt tree, `README.md`, `blueprint/src` listing; Sphere-Packing root and `SpherePacking/Dim24` listing, `README.md`, `Makefile`, `CONTRIBUTING.md` head, workflow listing, `build.yml` step names. Compared against `thefundamentaltheor3m/Sphere-Packing-Lean` @ 77cf0a0c104f2e31501eab04d88bbc068d61c169 by tree only.
- strongpnt: Lean files named by blueprint chapter (`PNT1_ComplexAnalysis.lean` to `PNT5_Strong.lean`) with matching `blueprint/src/PNT/PNT*.tex`; README declares which files were generated by the agent, which were adapted from PNT+, and scale (about 25k lines, 1.1k declarations). Dependency graph and PDF linked from README badges.
- Sphere-Packing: same blueprint repository grew from about 20k to about 180k lines; subject folders `Dim8/`, `Dim24/`, `Basic/`, `CohnElkies/`, `ModularForms/`; deep `AppendixA/…` trees with one file per computation; workflows `01-claim-issues` to `05-awaiting-review` replicate the claim/propose flow; `Makefile` wraps `leanblueprint pdf|web|serve`. README states provenance and that line counts are post-cleanup.

### Tooling checked: hanwenzhu/LeanArchitect @ c948bae1767330bb4cf09071f47752a10311d7d2; PatrickMassot/leanblueprint @ 56e066d30fb7b608a63f4241fee80982d7eae3ef; mathlib-initiative/formalization.yaml @ 99c678e569c7c4c0772db297c5ddd5e4c9b6322e; leanprover/comparator @ 865edc14486c3388e9225daa971da8e157488c3e
- LeanArchitect README: statement/proof readiness inferred from sorry-freeness, dependencies inferred from constants, `sorry_using` / `uses` / `proofUses` overrides, `notReady`, `mathlibOk` inferred from module path, `lake build :blueprintJson` emits nodes as JSON, converter script from classic leanblueprint.
- leanblueprint: manual `\leanok`, `\uses`, `\lean{}`, `\notready`, `\mathlibok`, `\proves`; `leanblueprint checkdecls` verifies names.
- formalization.yaml: root-level self-report, JSON Schema at `schema/v0.4.schema.json`, versioned dispatcher; deliberately omits what the toolchain already states.
- comparator README says it was merged into Lean core as `lake comparator` and `lake check` from Lean v4.35.0 and recommends migrating; PNT+ already pins `v4.35.0`.

## Practices worth copying, ranked

1. **Declare headline results in a Challenge file and check them with a pinned config** (`Challenge.lean` with `sorry`, `Solution.lean` aliasing the real theorems, JSON listing theorem names and permitted axioms `propext, Classical.choice, Quot.sound`). Source: carleson, pfr `PFRPalomar/`, openai/math `ComparatorChallenges/`; tool moved into `lake comparator`/`lake check` (comparator README). This is the only gate that fails when a statement is quietly changed.
2. **Register results through an attribute that parses the type and records axioms at elaboration time**, storing `{name, file, line, status}` in an environment extension and rejecting forbidden axioms immediately. Source: equational_theories `EquationalResult.lean`; same idea in formal-conjectures attributes and Mathlib's `@[stacks]` export. Gives a website backend its data without scraping.
3. **Per-statement metadata as attributes with linters**: category/status, subject code, question kind, external proof link, source reference; `lake exe extract_names` style exporter reading `.olean`. Source: formal-conjectures `Attributes/Basic.lean`, `scripts/extract_names.lean`.
4. **Root `formalization.yaml` (v0.4) for project-level status**, with `main_results` rows pointing at declaration, file, comparator config, sorry count, axioms. Source: carleson, pfr, openai/math, schema repo. Generate the counts instead of typing them (see avoid list).
5. **Blueprint generated from Lean, not parallel LaTeX**: `@[blueprint "label" (statement …) (proof …)]` with inferred `uses` and readiness from sorry-freeness, JSON output via `lake build :blueprintJson`. Source: LeanArchitect, PNT+. Fall back to leanblueprint plus `checkdecls` only where hand-written LaTeX is needed (pfr, FLT).
6. **One Lean file per source section, named after the source numbering**, with docstrings quoting "Definition 2.2.1"-style numbers. Source: teorth/analysis; strongpnt `PNT1..5` aligned to `blueprint/src/PNT/PNT*.tex`; pfr chapters to topic files. This is the cheapest paper-to-Lean link and is machine-checkable by filename.
7. **A spine file that states the whole argument as a chain of named reductions**, so a reader sees the proof shape without reading the library. Source: FLT `Proof.lean`.
8. **Make external assumptions explicit and countable**: one `axiom` per file in `Assumptions/` with a citation and issue number, README index; ban axioms elsewhere. Source: FLT `Assumptions/`, formal-conjectures STATEMENTS.md ("never add axiom/opaque/constant"), `literature_dependencies` in formalization.yaml.
9. **Separate statements, reusable maths, tooling, and tooling tests** into distinct libraries with import rules and a "no sorry here" zone. Source: formal-conjectures (`FormalConjectures` vs `FormalConjecturesForMathlib` vs `Util` vs `Test`), mathlib `Wanted/`, `Archive/`, `Counterexamples/`.
10. **Quarantine folders**: `Slop/` for unreviewed generated work, `Generated/` per generator, `Unused/`, `ToMathlib`/`Mathlib/` for upstream-bound code with a CI rule that it imports nothing project-specific. Source: FLT, equational_theories, PNT+, carleson, pfr CI step.
11. **CI gates that are cheap and text-level**: forbid `import Mathlib`, line length 100, `mk_all-check`, lint driver, linter set defined once in the lakefile, workflow lint (`actionlint`), pinned action SHAs. Source: FLT/equational_theories/carleson workflows, mathlib `lakefile.lean`.
12. **Machine-readable exemption and metrics lists**: `nolints.json`, weekly technical-debt counters, PR declarations diff, dated data snapshots. Source: mathlib; equational_theories `data/2024-11-10-*`.
13. **Contributor flow encoded as issue-comment commands** (`claim`, `disclaim`, `propose #n`, `withdraw #n`, `awaiting-review`) driving a board and labels, plus an AI-disclosure label and a PR style guide. Source: PNT+, FLT, equational_theories, Sphere-Packing workflows `01`..`05`.
14. **Agent contract file**: short `AGENTS.md` linking `STATEMENTS.md`, `PROOFS.md`; checklist for faithfulness (quantifier order, vacuous hypotheses, `0`/empty boundary cases). Source: formal-conjectures.
15. **Family-keyed scope notes** `docs/NNN.md` that state what the formalization proves and omits, with a link to the comparator file. Source: openai/math `lean/docs/`.
16. **Slow jobs off the merge path**: API docs built on demand and re-published from a release asset. Source: FLT `blueprint.yml`, `api-docs.yml`.
17. **Separate trusted CI scripts from developer scripts** (and from the repo that holds secrets). Source: mathlib `scripts/README.md`, `mathlib-ci`.
18. **Statement-vs-source drift check against the upstream registry** (`check_erdos_status.py` opening issues on mismatch). Source: formal-conjectures; worth copying for any paper whose status lives elsewhere.

## Practices to avoid, with reasons

- **`warn.sorry=false` as a standing setting** (FLT, teorth/analysis, PNT+ patterns): a build succeeds and shows no signal. Keep warnings on and count sorries in a gate instead.
- **Hand-typed `sorry_count` and `axioms` in `formalization.yaml`** (carleson's numbers are prose-adjacent and can go stale): generate them from `#print axioms` over the declared main results in CI and fail on drift.
- **Prose claims of completeness** such as "no sorry outside the six holes" in a description field: not checked by anything. Put the claim in the comparator config instead.
- **Manually maintained `\leanok` / `\uses`** (classic leanblueprint, pfr): drifts from the code; `checkdecls` catches missing names but not wrong status or missing dependencies. Prefer inferred status (LeanArchitect).
- **Two blueprints in one repo** (FLT has `blueprint/` and `blueprint-verso/`): two sources of truth for the same statement bindings. Pick one.
- **Hand-written README section tables with per-section links** (teorth/analysis): 3 links per row by hand; generate from the file list.
- **A single huge library with deep per-result subtrees** (Sphere-Packing `Dim24/…/AppendixA/…`, openai/math `OAI/`): fine for archival, hard to build selectively (openai/math README warns to compile small portions and to work around `vm.max_map_count`). For a single paper, keep depth at three levels.
- **Status as free text or directory placement** (`Unused/`, `Slop/`, `Generated/` without a recorded reason): fine as quarantine, but status must also live in a queryable field per declaration.
- **Giant generated files with no generator provenance** (equational_theories `Generated/*` is saved with its generator name, but `data/` snapshots are zips): record generator command, input hash, and date next to the output.
- **Depending on a deprecated checker invocation** (comparator binary plus `landrun`, `lean4export` on PATH): the README says to migrate to `lake comparator` / `lake check` in Lean v4.35.0 and later; pin the Lean version and use the core command.
- **Kitchen-sink root** (mathlib has 8+ dot-directories and ~50 workflows; PNT+ has Jekyll site, errata, examples): copy mathlib's ideas, not its volume. A single-paper repo needs about five workflows at most.
- **Importing all of Mathlib** (`import Mathlib`): banned by three of the repos' CI for build time and dependency hygiene. Keep the ban.

## Gaps in this survey

- Did not open `Unused/` or `Slop/` contents, so the rules for their use are inferred from names and READMEs only.
- Did not read PNT+ `PULL_REQUEST_STYLE.md`, `intentions.yml` or `update.yml`, nor the Sphere-Packing blueprint `.tex` bodies.
- `thefundamentaltheor3m/Sphere-Packing-Lean` compared by tree listing only; `leanprover-community` lean-blueprint example repo name did not resolve (404) and was skipped.
- No project was built or run; CI behaviour is read from workflow files, not from observed runs.
