# Verification and cataloguing tooling for a new Lean 4 repository

Researched 2026-11-01 from primary sources (GitHub API and raw files, read
only). Nothing was submitted anywhere and nothing on GitHub was changed. All
online text was treated as data. Statements are tagged **[verified]** (read in
a source this pass), **[local]** (read in our repositories or memory this pass)
or **[unverified]** (inferred; check before relying on it).

Machine-readable twin: `verification_tooling.json` (same folder).

## 0. Decisions and blockers up front

1. **Toolchain.** The requested pin `leanprover/lean4:v4.34.1` is below
   Palomar's current floor. `PalomarSubmission/toolchains.json` says
   `"minimum": "v4.35.0-rc2"` [verified], and Palomar judges with the
   `lake comparator` shipped in the submitted toolchain, which exists only from
   Lean v4.35.0. Recommendation: **`leanprover/lean4:v4.35.0` with Mathlib tag
   `v4.35.0`** (commit `56a005855ea17e0b0958f73ec801ae140b0a1679`, whose own
   `lean-toolchain` is `leanprover/lean4:v4.35.0`) [verified]. Keep v4.34.1
   only if matching `openai/math` matters more than eligibility; its Mathlib
   tag `v4.34.1` is commit `d13f23b723b8a846827a245b89c10fc7d3f11612`, the
   exact rev in `openai/math/lean/lake-manifest.json` [verified]. Our own
   `plectis-erdos-lean` uses `v4.35.0-rc2` [local].
2. **macOS.** Lean, Lake, Mathlib cache, doc-gen4, leanblueprint, nanoda and
   the checkers run on Apple silicon. The **sandboxed** Comparator does not:
   `lake comparator` refuses to start unless on Linux with `bwrap`
   (`Check.lean`: "needs Linux namespaces", exit 2) [verified]; standalone
   Comparator needs `landrun`, a Linux Landlock tool [verified]. On this Mac
   you can only run the no-sandbox mode (trusted own code, not evidence for
   third parties) or a Linux CI/VM. No `docker`, `colima`, `podman`, `limactl`
   or `bwrap` is installed here [verified]. The existing GitHub workflow
   `plectis-erdos-lean/.github/workflows/palomar-replay.yml` is the sandboxed
   route [local].
3. **Disk.** The data volume is 92% full with about 18 GiB free [verified];
   the Palomar template measured about 7.7 GiB under `.lake/` for a Mathlib
   project plus more for doc-gen4 (`PalomarTemplate/README.md`) [verified]. No
   Lean toolchain is currently installed under `~/.elan/toolchains` [verified]
   (elan exists). Our memory notes toolchains live off the media drive.
4. **Comparator is not a proof of fidelity.** It proves Solution theorems have
   the same statements as Challenge and use only the permitted axioms; it says
   nothing about whether the Challenge states the paper's claim.

## 1. leanprover/comparator

- URL: https://github.com/leanprover/comparator (archived 2026-10-14;
  README "Deprecation": merged into Lean core at v4.35.0 as `lake comparator`
  and `lake check`) [verified].
- **Core route (recommended, Lean >= 4.35.0):** no separate install.
  Needs Linux, `bwrap` (bubblewrap, unprivileged user namespaces or setuid
  root), `git`, `env`. Binaries bundled in release toolchains: `lake`,
  `leanexport`, `leanchecker`, `nanoda_bin`, `con-ron` (also `leanchecker-paranoid`,
  `lean4lean`, `con-leche` for `--paranoid`) [verified in `Check.lean`,
  `lean4/src/CMakeLists.txt`]. Whether the `darwin_aarch64` tarball contains
  all of them is **[unverified]**; check with
  `ls "$(lean --print-prefix)/bin"` (the template script does exactly this).

```sh
# Linux, in the project root (needs a committed lake-manifest.json)
lake exe cache get
lake comparator --config comparator.json              # exit 0 accepted, 1 rejected, 2 could not start
lake comparator --config comparator.json --paranoid   # also lean4lean, nanoda, con-leche, con-ron, leanchecker-paranoid
lake check                                            # kernel replay of the project, no challenge (also --paranoid, --from-export)
# macOS, trusted own code only; the tool prints "this run is not trustworthy":
lake comparator --inadvisably-no-sandbox --config comparator.json
```

- **Standalone (Lean < 4.35, e.g. v4.34.1):** tag `v4.34.0` = commit
  `d03acab154d269c06e60e4de7e4cc85deebff94b`, its `lean-toolchain` is
  `leanprover/lean4:v4.34.0` [verified]. There is no `v4.34.1` tag for either
  comparator or lean4export [verified]. Our local note records building both at
  v4.34.0 and changing only their toolchain pins to v4.34.1, after which the
  builds, exporter tests and upstream core tests passed on Ubuntu 24.04
  aarch64 [local, `lean-exposition/docs/verification.md`].
  lean4export `v4.34.0` = `076e8e57707e813375e8f9da8bf989799ace9680` [verified].

```sh
git clone https://github.com/leanprover/comparator && git -C comparator checkout d03acab154d269c06e60e4de7e4cc85deebff94b
git clone https://github.com/leanprover/lean4export && git -C lean4export checkout 076e8e57707e813375e8f9da8bf989799ace9680
git clone https://github.com/Zouuup/landrun             # Linux only; go build -o landrun cmd/landrun/main.go
(cd comparator && lake build comparator)
(cd lean4export && lake build lean4export)
# in the project: binaries on PATH or COMPARATOR_LANDRUN / COMPARATOR_LEAN4EXPORT / COMPARATOR_NANODA
lake env /path/to/comparator/.lake/build/bin/comparator comparator.json
# macOS dev only: COMPARATOR_LANDRUN=<comparator>/scripts/fake-landrun.sh (no sandbox)
```

  The standalone README's security contract also wants `systemd-run
  --property=RestrictAddressFamilies=~AF_UNIX --user ...` around the call, and
  states `landrun` needs Linux 5.13+ [verified].
- **Config JSON** (core `Config` structure, `Check.lean`) [verified]:
  required `challenge_module`, `solution_module`, `theorem_names`,
  `permitted_axioms`; optional `definition_names`, `enable_nanoda`,
  `external_kernels` (map name to command array). `enable_nanoda` and
  `external_kernels` cannot be combined. Palomar accepts only the four
  required keys plus optional `definition_names` and `enable_nanoda` (ignored)
  and rejects `external_kernels`; `permitted_axioms` may only be
  `propext`, `Quot.sound`, `Classical.choice`; file at most 1 MiB [verified,
  `PalomarPolicy/CONTRIBUTING.md` 2.3].
- **Module structure.** Challenge and Solution are distinct dotted modules.
  Challenge holds each compared theorem with `sorry` (or any proof); Solution
  restates the same theorem with a real proof. Both must import the default
  prelude. Challenge's transitive imports are trusted; do not compile the
  Solution before the Challenge [verified, README].
- **What is compared** [verified, `Lake/Check/Compare.lean` at v4.35.0 and
  `PalomarSubmission/docs/comparator-declaration-closure.md`]: for each name in
  `theorem_names`, same kind and same type; then a worklist over every constant
  used in those types; each ordinary constant reached must have
  `challengeConst == solutionConst`, i.e. full `ConstantInfo` equality (the
  source throws "Const does not match" otherwise). Names in `theorem_names` or `definition_names` are holes, compared
  by type (definitions also by safety), body free. So you do not list helper
  definitions; the closure is followed mechanically.

### The ConstantInfo identity trap (confirmed)

Comparing only the type is not enough: every definition reachable from a
compared statement must be identical (value, reducibility hints, kind) in both
environments. Our 13 Sep 2026 run rejected seven of eight entries after eleven
green local builds, because Solution adapters either aliased Challenge defs
(`abbrev X := Src.X`) or re-declared the same text under different imports,
which elaborated differently (`_proof_1`, `_f`/`_sunfold` names) [local, memory
`feedback_palomar_comparator_constantinfo_identity.md`]. The source read this
pass confirms the mechanism (`if challengeConst != solutionConst then throw`).

**Layout that works [local memory; consistent with verified rules]:**
`Challenge.lean` is self-contained (Mathlib-only imports; Palomar forbids any
project-specific source in the Challenge import closure, so it cannot import
the project's Statement module). Generate or CI-diff
`Statement.lean` = Challenge minus its theorems, byte-for-byte, Mathlib-only.
Solution imports `Statement` and the proof development and drops every helper
the Challenge declares. The memory's claim that Solutions must import a
Mathlib-only Statement module is right **when the Challenge declares new
definitions**. If the compared statements use only Mathlib vocabulary (the
`PalomarTemplate` pattern), no Statement module is needed. Other traps from
our generator [local, memory `feedback_palomar_challenge_generator_mechanical_traps.md`]:
`set_option autoImplicit false` at the top of every Challenge (missing helper
names otherwise auto-bind and silently change the theorem); primed identifiers;
source `type: preprint` is not allowed. Avoid `private` declarations in
Statement/Challenge (private names embed the module name; **[unverified]**).
Always run a real Comparator replay; green `lake build` and axiom audits do not
detect this.

## 2. mathlib-initiative/formalization.yaml

- URL: https://github.com/mathlib-initiative/formalization.yaml ; schema
  `schema/v0.4.schema.json`, dispatcher `schema/formalization.schema.json`
  (accepts `v0.3`, `v0.4`; no `version` means latest). Repo HEAD
  `99c678e5` (2026-08-25) [verified]. The repo's only GitHub release is
  `v0.2` (stale); the file `version` string is what counts. `openai/math` uses
  `version: "v0.4"` [verified].
- **Schema-required (JSON Schema v0.4):** top level `project`, `sources`,
  `automation`, `review`. `project.name`, `project.authors`, `project.license`;
  `sources` minItems 1, each with `title`; `automation.methods` each with
  `method` (`manual|copilot|agent|autonomous|other`); `review.status`.
  The template says unknown keys are tolerated [verified].
- **Optional fields:** `project.description`, `project.responsible_maintainers`,
  `repository.{role: substantive-development|thin-wrapper, substantive_formalization.{id,revision}}`,
  `sources[].{authors,contributors[name,role],id,type,location,relationship
  (formalizes|adapts|independently-proves|background|other),note,license,
  author_endorsement}`, `related_formalizations[{id,relationship
  builds-on|adapts|independent|supersedes|other}]`, `classification.{arxiv,msc2020}`,
  `status.{scope,sorry_count,sorry_in_definitions,axioms,main_results[declaration,file,
  sorry_count,axioms,comparator_config,literature_dependencies]}`, `fidelity.divergences`,
  `review.{reviewers,notes}`, `alignment` (free YAML; suggested
  `namespace` and `statements[source,lean,module,status,note]`), `acknowledgements`.
  Sorry counts exclude the deliberate Challenge `sorry`.
- Validate: `check-jsonschema --schemafile https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/main/schema/formalization.schema.json formalization.yaml`.
- **Palomar's stricter minimum** (on top of the schema; `CONTRIBUTING.md` 3.1,
  3.2) [verified]: UTF-8, at most 256 KiB, no duplicate keys or merge keys;
  `project.description` nonempty, at most 10,000 chars; `project.authors` and
  `project.responsible_maintainers` nonempty and human only (no AI named);
  `project.license` equals the SPDX id detected from the root LICENSE;
  `classification.arxiv` 1 to 8 codes from Palomar's snapshot, `msc2020` 0 to 8;
  source origin rule: either one `type: original-proof` entry with
  relationship `other` (others only `background|other`) or at least one
  cited source with `formalizes|adapts|independently-proves`.
  Palomar also checks ORCID iDs if given (`scripts/orcid_validation.py`).
- Backend use: our `alignment.statements` is the natural paper-statement to
  Lean-declaration table; `status.main_results[].comparator_config` links each
  headline to its Comparator JSON.

## 3. Palomar and PalomarSubmission

- Org https://github.com/PalomarRegistry : `PalomarSubmission`
  (CI, HEAD `14aa8d6b3c2f14a8540605e37144560b9a00e7e7`, 2026-10-28),
  `PalomarTemplate` (starter), `PalomarPolicy` (`CONTRIBUTING.md` binding
  submitter standard), `PalomarServer`, `PalomarReviewer`, `PalomarWeb`,
  `PalomarDatabaseTools`. Submission form https://submit.palomar-registry.org/
  (agents: `/llms.txt`) [verified].
- **What a prepared submission needs** [verified, CONTRIBUTING 2 to 2.5]:
  public GitHub repo; project root with `lean-toolchain` (>= `v4.35.0-rc2`),
  exactly one of `lakefile.toml`/`lakefile.lean` (at most 1 MiB; manifest
  mandatory for `.lean`), committed `lake-manifest.json`, `formalization.yaml`,
  Challenge and Solution `.lean`, `comparator.json`, root `LICENSE`. Submit an
  exact 40-char commit SHA plus one comparator config path (one config = one
  entry). Repo at most 500 MiB, no submodules, no Git LFS pointers, no compiled
  artifacts outside `.lake`, every Git dependency a credential-free public
  `https://github.com/owner/repo` URL pinned to a 40-char SHA.
  **Every `.lean` file must use the module system (`module` header) and be at
  most 10,000 lines.** Challenge at most 1,000 lines and 100 KiB (warning above
  300 lines or 32 KiB). With Mathlib, `lean-toolchain` must equal the resolved
  Mathlib revision's toolchain exactly. Challenge import closure: Lean core,
  Mathlib, Tau Ceti or CSLib only; proof-only dependencies may be any pinned
  public repo.
- **Local rehearsal:** copy `PalomarTemplate/scripts/verify-comparator.sh`
  (Linux, needs `bwrap lake lean python3`): it injects the toolchain's `nanoda_bin`
  and `con-ron` as `external_kernels`, drops `enable_nanoda`, runs
  `lake exe cache get` then `lake comparator --config <tmp>`. Also
  `scripts/check-lean-sources.py` (module header and line caps) and
  `scripts/validate-formalization.rb`. A reusable GitHub workflow can be
  called as a predictive preflight at an exact commit:
  `uses: PalomarRegistry/PalomarSubmission/.github/workflows/submission.yml@<sha>`
  with `execution_profile: palomar-standard-v1`, `mode: preflight|full`,
  `request_id` of 12 lowercase alphanumerics, and `options` JSON containing
  `comparator_config_path` and `authorization_relationship`; results are
  advisory. Do not run these without explicit approval: a preflight on GitHub
  runs under the user's account and consumes Actions minutes (memory: private
  Actions minutes cost real money).
- **`verify_submission.py`** (6,600+ lines) has subcommands `capacity`,
  `prepare --event --work-dir --output --licensee`, `execute --work-dir --output
  --bwrap --bwrap-source-tag --workflow-url ...`; `prepare` is the local intake
  rehearsal (clones the public commit, checks root files, `formalization.yaml`,
  LICENSE via the `licensee` Ruby gem, toolchain floor, config keys, sizes). The
  four traps from our rehearsal [local, memory
  `project_palomar_official_prepare_rehearsal.md`]: `--licensee` must be the Bundler
  executable (`bundle exec ruby scripts/detect_license.rb`); `PALOMAR_JOB_STARTED_AT`
  is epoch seconds; `request_id` twelve lowercase alphanumerics; send
  `options.formalization_metadata_path` when metadata is not at the root.
  `prepare` does not run `execute` (protected Challenge build, Comparator under
  the sandbox). Its toolchain floor in that memory (v4.28.0 on 2026-09-13) is
  **stale**: now v4.35.0-rc2.
- **Pipeline** [verified, README and CONTRIBUTING 5]: prepare; install the
  submitted toolchain; compile Challenge against frozen canonical Mathlib;
  compute and verify the Challenge source closure; build the Solution in
  Palomar's bwrap sandbox; export both with `leanexport`; `lake comparator`
  judges, with Lean kernel plus NanoDa mandatory, con-ron attempted; report
  published as a run artifact. AI editorial review then checks statement to
  description alignment and research interest; it can find no blocking problem
  or block; it does not accept or endorse.
- **What registration means** [verified, CONTRIBUTING 8 to 9]: a consent step
  after the review. It publishes the redacted review, the source and the record;
  creates native public forks in `PalomarArchive` of the repo and every pinned
  dependency with immutable preservation tags; assigns `PALOMAR-YYYY-MM-DD-NNNNNN`;
  is permanent publication history (append-only since 2026-08-10); removal is by
  moderation tombstone only. Mechanical verification itself runs in a public
  GitHub Actions workflow, so repo, commit and the declared authorization
  relationship are public from the moment of submission. Submit only as a
  responsible author or maintainer. Admission intervals double per admitted
  start [local memory]. So: prepare only; registration and submission are
  consent steps for Will.
- Our own pins for a Palomar-style Linux replay (standalone route, historical)
  [local, `palomar-replay.yml`]: Comparator `575674928e239f5bc452aab72d1dd7b0f1326494`,
  lean4export `a3e35a584f59b390667db7269cd37fca8575e4bf`, landrun
  `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4`, NanoDa (robsimmons fork)
  `68d5ca9db226849b41a6fff59d796ff19d0a8840`. With toolchain >= 4.35 prefer the
  bundled tools and drop these.

## 4. Independent checkers

| Tool | Status | Use |
| --- | --- | --- |
| `leanchecker` (was lean4checker) | built into every toolchain since v4.28.0; `leanprover/lean4checker` is archived (2026-03-25) | `lake env leanchecker Mod` ; `lake env leanchecker --fresh Mod` replays imports too. Same kernel, so it detects environment hacking, not kernel bugs. |
| nanoda | `ammkrn/nanoda_lib` (Rust, Apache-2.0, active 2026-10-29); bundled as `nanoda_bin` | independent kernel; takes a JSON config (`export_file_path`, `permitted_axioms`, `nat_extension`, ...). Our CI builds the `robsimmons/nanoda_lib` fork at `68d5ca9`. `cargo build --release --locked --bin nanoda_bin`; cargo present here, so macOS build is plausible, **[unverified]**. |
| con-ron, con-leche, lean4lean, leanchecker-paranoid | bundled in release toolchains; `--paranoid` runs them | Palomar runs con-ron after the mandatory checks. `digama0/lean4lean` is a Lean-written kernel (Apache-2.0). |
| SafeVerify | `GasStationManager/SafeVerify`, last push 2026-04-22; takes two `.olean` files; uses `Environment.replay`; bans `partial`/`unsafe`; branches pinned for old toolchains | lighter alternative to Comparator for single-file challenges; it does **not** sandbox compilation and does not compare transitive closure as Comparator does. Not recommended as primary. |
| checkdecls | `PatrickMassot/checkdecls`, last push 2025-04-02 | existence of declaration names; used by `leanblueprint checkdecls`. |
| `#print axioms` | built in | add `AxiomAudit.lean`-style file listing the headline theorems (as in `PalomarCorpus/*/AxiomAudit.lean` [local]); necessary, not sufficient. |

Recommended stack: Comparator (core) `--paranoid` in CI on Linux for the
headline statements; `leanchecker --fresh` on the whole root library as a cheap
second pass; axiom audit file.

## 5. leanblueprint and doc-gen4 (data a backend can read)

### doc-gen4

- https://github.com/leanprover/doc-gen4, tags `v4.35.0`, `v4.36.0-rc2` (match
  the toolchain; last push 2026-11-01) [verified]. `openai/math` pins
  `953c8992d174b4e56955e01e101d46668c68f2bb` for v4.34.1 [verified].
- Setup: nested `docbuild/lakefile.toml` (`packagesDir = "../.lake/packages"`,
  require `doc-gen4` with `rev = "v4.35.0"`, require the parent by `path = "../"`),
  then `MATHLIB_NO_CACHE_ON_UPDATE=1 lake update doc-gen4`, then
  `lake build <Lib>:docs`. Needs a C compiler (Xcode CLT on macOS). Serve with
  `python3 -m http.server` in `docbuild/.lake/build/doc`. The library must build.
- **Machine-readable outputs** [verified, `DocGen4/Output.lean`, `Output/ToJson.lean`]:
  under `docbuild/.lake/build/doc/declarations/`: `declaration-data-<Module>.bmp`
  per module, `declaration-data.bmp` (global index), `header-data.bmp`,
  `backrefs-<Module>.json`, `references.json`. Despite `.bmp` they are minified
  JSON. Per-module shape: `{name, declarations:[{info:{name,kind,doc,docLink,
  sourceLink,line}, header}], instances:[{name,className,typeNames}], imports:[...]}`.
  Global index: `{declarations:[[name,{kind,docLink}]], instances, modules:
  {name:{importedBy,url}}, instancesFor}`. HTML pages per module sit beside them.
  Use these for declaration inventory, kinds, docstrings, source lines.

### leanblueprint

- https://github.com/PatrickMassot/leanblueprint, PyPI `leanblueprint` 0.0.20
  (2025-12-23); depends on `plastexdepgraph` 0.0.5, graphviz dev libs
  (`brew install graphviz` on macOS) [verified]. `pip install leanblueprint`.
  `leanblueprint new` scaffolds `blueprint/src/{web.tex,print.tex,content.tex,
  macros/}`; `leanblueprint web|pdf|checkdecls|all|serve`.
- LaTeX macros: `\lean{decl,...}`, `\leanok`, `\uses{label,...}`, `\notready`,
  `\mathlibok`, `\proves`, `\discussion{n}`. Dependency-graph colors encode
  stated/proved/fully_proved states.
- Outputs: HTML under `blueprint/web/` (including the dependency-graph
  document page) and a PDF; **no stable JSON export from leanblueprint itself
  [unverified, none found in README]**. For JSON, use LeanArchitect.
- **LeanArchitect** https://github.com/hanwenzhu/LeanArchitect (tag `v4.35.0`,
  Apache-2.0, push 2026-10-28) [verified]: `@[blueprint "label" (statement := /-- ... -/)]`
  on Lean declarations, `lake build :blueprint` writes LaTeX under
  `.lake/build/blueprint/`, and **`lake build :blueprintJson`** writes the
  nodes as JSON in `.lake/build/blueprint`. Best source for a statement
  catalogue graph (labels, `\uses` edges, sorry-free status).
  Its import adds a dependency, so keep `import Architect` out of the
  Challenge and Statement modules (they may import Mathlib only).

## 6. Mathlib cache, Lake pinning and toolchain matching

```toml
# lakefile.toml
name = "QuarticQueryLean"
version = "0.1.0"
defaultTargets = ["QuarticQueryLean", "Challenge", "Solution"]

[[require]]
name = "mathlib"
scope = "leanprover-community"          # or git = "https://github.com/leanprover-community/mathlib4.git"
rev = "v4.35.0"                         # tag; manifest records the commit

[leanOptions]
autoImplicit = false
```

```sh
# lean-toolchain: leanprover/lean4:v4.35.0   (must equal Mathlib's own lean-toolchain at the rev)
lake update            # writes lake-manifest.json; commit it
lake exe cache get     # downloads prebuilt Mathlib oleans (macOS arm64 supported by upstream cache [unverified])
lake build
```

- Palomar rejects a mismatch between `lean-toolchain` and the resolved Mathlib
  revision's `lean-toolchain` (including patch and rc suffix) [verified].
  Our repo pins tag `v4.35.0-rc2` = `065356127b1dc0016f66b7283ce0ce2c4055aa55`
  [local manifest, verified against mathlib tags].
- Cache trust: Comparator's README says `lake exe cache get` before running is
  acceptable if you trust the cache; Palomar has `docs/mathlib-cache-trust.md`.
  Palomar compiles the Challenge against frozen canonical Mathlib output.
- Tag table [verified]: Mathlib `v4.34.1` = `d13f23b7...`; `v4.35.0` =
  `56a00585...`; `v4.35.0-rc2` = `06535612...`; master toolchain currently
  `v4.36.0-rc2`. Lean releases: v4.34.1 (2026-09-24), v4.35.0 (2026-10-12).
  `lean4` release assets include `darwin_aarch64`.
- Disk planning: budget about 8 GiB for Mathlib `.lake`, plus doc-gen4
  `docbuild/.lake`. Never commit `.lake`.

## 7. Local practice and guidance from our repositories [local]

- `lean-exposition/docs/verification.md`: Comparator exit codes (core: 0, 1, 2;
  2 means could not start, recorded as unavailable not rejected); keep
  failed and unavailable receipts; negative fixtures must reach the intended
  stage; a no-sandbox local run is not security evidence; a passing wrapper
  status is not an authenticated inner verdict; Comparator does not prove
  equivalence of different formulations and `definition_names` holes need a
  separate check that the intended construction was filled.
- `plectis-erdos-lean`: `lean-toolchain` v4.35.0-rc2, `lakefile.toml` with one
  `lean_lib` per entry, `PalomarCorpus/E*/{Challenge.lean,AxiomAudit.lean,
  comparator.json,formalization.yaml}`, `Solutions/PalomarCorpus/E*`,
  workflows `lean.yml` (build with cache restore), `palomar-replay.yml`
  (sharded Comparator replay, all actions pinned by SHA, Challenge compiled from
  source each job, per-entry receipt JSON), `release-gate.yml`, scripts
  `check_axiom_budget.py`, `palomar_entry_names.py`, `palomar_replay_shard.py`,
  `verify_snapshot.py`. Reusable as the pattern; its inline Comparator build
  step can be replaced by the bundled `lake comparator` at v4.35.0.

## 8. Suggested repository skeleton for quartic-query-lean

```
lean-toolchain                 leanprover/lean4:v4.35.0
lakefile.toml                  mathlib rev v4.35.0, autoImplicit=false, libs below
lake-manifest.json             committed
LICENSE  (Apache-2.0)          formalization.yaml (v0.4)   README.md
Challenge.lean                 module; Mathlib imports only; set_option autoImplicit false; defs + sorry theorems
QuarticQuery/Statement.lean    byte-equal to Challenge minus theorems (CI diff)  [only if Challenge declares defs]
QuarticQuery/...               full development; Solution imports Statement + development
Solution.lean                  same theorem statements, real proofs, no helper redeclared
comparator.json                four keys + optional definition_names
AxiomAudit.lean                #print axioms for every headline theorem
docbuild/lakefile.toml         doc-gen4 v4.35.0
blueprint/                     leanblueprint + LeanArchitect (optional)
scripts/                       check-lean-sources.py, validate-formalization.rb, verify-comparator.sh (from template)
.github/workflows/             lean.yml (build), comparator.yml (Linux, bundled lake comparator --paranoid)
```

One Comparator config per Palomar entry; if every statement of the paper should
be checked, use one config per paper or per theorem group and keep each
Challenge under 1,000 lines. Per-theorem `AxiomAudit` plus `docs` JSON gives the
catalogue; the Comparator receipt gives the statement-level assurance.

## 9. Open items, all unverified here

1. Darwin toolchain contains `leanexport`, `nanoda_bin`, `con-ron`: check after
   installing v4.35.0.
2. Whether Mathlib's cache serves macOS arm64 for tag `v4.35.0`: run
   `lake exe cache get` (a download; needs go-ahead).
3. Private-declaration behaviour across module names (see section 1).
4. Nothing here was built or run; only sources were read.

## Source URLs

- https://github.com/leanprover/comparator (README, tags, `lean-toolchain`)
- https://github.com/leanprover/lean4/blob/v4.35.0/src/lake/Lake/CLI/Check.lean
- https://github.com/leanprover/lean4/blob/v4.35.0/src/lake/Lake/Check/Compare.lean
- https://github.com/leanprover/lean4/blob/v4.35.0/src/lake/Lake/CLI/Help.lean
- https://github.com/leanprover/lean4export
- https://github.com/Zouuup/landrun
- https://github.com/mathlib-initiative/formalization.yaml
- https://github.com/openai/math/blob/main/lean/formalization.yaml
- https://github.com/PalomarRegistry/PalomarSubmission
- https://github.com/PalomarRegistry/PalomarTemplate
- https://github.com/PalomarRegistry/PalomarPolicy/blob/main/CONTRIBUTING.md
- https://github.com/leanprover/lean4checker
- https://github.com/ammkrn/nanoda_lib
- https://github.com/GasStationManager/SafeVerify
- https://github.com/digama0/lean4lean
- https://github.com/leanprover/doc-gen4
- https://github.com/PatrickMassot/leanblueprint
- https://github.com/hanwenzhu/LeanArchitect
- https://github.com/leanprover-community/mathlib4 (tags)
