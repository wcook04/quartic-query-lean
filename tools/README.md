# Maintenance commands

Run these commands from the repository root with Python 3.10 or newer.
The top-level Python tools use only the standard library; commands that invoke
Lean or Comparator also need their pinned external tools. The imported finite
checker described below additionally needs NumPy.

## Check the repository

```sh
make check
```

This checks file placement, local README links and generated challenges/corpus
files, then runs the Python tests.
It does not compile Lean or check mathematical claims. To check the staged
version of files before committing, run:

```sh
python3 tools/check_repository.py --index
```

## Generate and check the Lean evidence

Freeze the intended Lean inputs before recording evidence:

| Command | Effect |
| --- | --- |
| `python3 tools/build_challenges.py` | Regenerates each Comparator challenge from the statement file and its solution. |
| `python3 tools/record_evidence.py` | Builds `QuarticQuery`, then records its compiled dependency closure and a source-bound build receipt. |
| `python3 tools/run_comparator.py` | Runs each bundle and negative control and writes receipts. |
| `python3 tools/build_corpus.py` | Regenerates the corpus from the ledger, ties and receipts. |

[build_challenges.py](build_challenges.py) keeps a challenge and its solution in
agreement by construction. A negative control counts only when Comparator rejects it
with the expected diagnostic, and a build deferred by a lock judges nothing.
Build and comparison producers append timestamped receipts; old runs remain
historical. Both check that their source/configuration hashes remain unchanged
during execution. The hashes bind local source and dependency pins, not the
bytes of external dependency checkouts. These are local verification runs, not
fresh-clone reproducibility certificates.

## Build research packets

[build_research_packets.py](build_research_packets.py) produces three ZIPs:
a paper audit, a literature review, and a formalisation planning packet. Each
contains instructions and a manifest with SHA-256 hashes. The builder reopens
each archive and verifies its contents against those hashes.

Review instruction text belongs in [research/requests/review/](../research/requests/review/). The
builder combines the common template, one job request and the boundaries into
`READ_ME_FIRST.md`. Edit those authored files and rebuild rather than editing
instructions inside generated ZIPs. See the [research guide](../research/README.md)
for the three requests and the evidence they ask reviewers to assess.

```sh
python3 tools/build_research_packets.py --help
```

The original local defaults remain supported:

```sh
python3 tools/build_research_packets.py --dest /path/to/output
```

Those defaults read cited PDFs from `~/src/quartic-query-sources/papers`, the
paper and extracted text from
`~/src/ai_workflow/annexes/openai-math-284-quartic-query-separation`, intake
records from this repository, and current source from `lean/`.
A clone does not supply those external inputs. Set their locations explicitly:

```sh
python3 tools/build_research_packets.py \
  --intake-dir /path/to/intake \
  --papers-dir /path/to/cited-pdfs \
  --paper-annex /path/to/paper-annex \
  --lean-dir /path/to/lean-project \
  --dest /path/to/output
```

The paper annex must contain `source.pdf` and `extracted.md`. The Lean project
must contain `QuarticQuery/Tournament/Drift.lean`, `lakefile.toml` and
`lean-toolchain`. The builder packages source; it does not compile it. Missing
required files stop that packet's build. Cited PDFs are selected from the
supplied directory; this does not establish that every citation has a copy.

Keep output ZIPs outside the source tree. The PDFs and packets may include
material with separate redistribution restrictions. The repository's licence
does not grant rights to those source papers.

Archive member names remain stable when source locations change. They are
consumed by the research instructions inside each packet; update both together
if the archive contract changes.

## Build writing packets

[build_funnel_packets.py](build_funnel_packets.py) packages the five
[writing requests](../research/requests/README.md): long record, short paper,
exposition, route note, and reader/film plan.

```sh
python3 tools/build_funnel_packets.py --help
python3 tools/build_funnel_packets.py --only 3_examples_first_exposition --dest /path/to/output
```

[build_round2_packets.py](build_round2_packets.py) packages the seven
[round-two requests](../research/requests/round2/). Each ZIP adds the five
first-round returns, their adjudication, every annexed paper of the quartic
cluster with a reading order for its job, and a record skeleton generated from
the recorded dependency export with its source currentness. `BUILD_STATUS.md`
classifies the named saved build receipt against current source hashes and
reports local `.olean` existence and mtime as artifact observations only. Those
observations establish no source-current build or dependency reach. The fidelity
and four Lean coverage packets also carry complexitylib's query-complexity source.

```sh
python3 tools/build_round2_packets.py --only 1_statement_fidelity --dest /path/to/output
```

Omit `--only` to build all seven. This builder reads the current repository,
private annexes under `~/src/ai_workflow/annexes`, writing references under
`~/.claude/skills/formal-math-exposition/references`, and exemplar files from
`origin/main` in `~/src/lean-exposition`. Those external inputs are not included
in a clone. Unlike the review builder, its CLI exposes only job selection and
the output directory; inspect its source configuration before using a different
local setup. Packaging does not constitute review, publication or submission.

The maintained adjudication files now live in `research/adjudication/`.
The ZIPs include their current paths for README navigation.
For compatibility, they also carry them at their original
`repository/research/returns/adjudication*` member names, which the packet
instructions reference.

## Prepare focused round-three packets

[build_round3_packets.py](build_round3_packets.py) prepares the ten bounded
[round-three requests](../research/requests/round3/SELECTION.md). Use `--only`
with one or more job keys to select fewer. Each packet includes its selected
primary literature, a primary source reading list, the existing long-record
return, relevant earlier returns, maintained adjudications, and the complete
local Lean/configuration scope used by receipt hashes. It excludes `.lake`
and build artifacts. Writing guidance is included as readable text; the
exemplars are writing models about a different theorem.

All external inputs have explicit paths. Validate first; this command writes no
ZIPs and prints a digest of the exact inputs:

```sh
python3 tools/build_round3_packets.py \
  --paper-annex /path/to/openai-preprint-annex \
  --annexes /path/to/literature-annexes \
  --writing-skill /path/to/formal-math-exposition/SKILL.md \
  --writing-guides /path/to/formal-math-exposition/references \
  --exemplar-repo /path/to/lean-exposition \
  --exemplar-ref COMMIT \
  --dependency-root complexitylib=/path/to/pinned-complexitylib \
  --dependency-root cslib=/path/to/pinned-cslib \
  --only 01_models_evidence
```

The writing-reference directory must contain `the-deliverable.md`,
`mathematical-writing-mechanics.md`, `full-exposition-guide.md`, and
`register-from-literature.md`. The exemplar ref is resolved to a commit before
reading the four existing exemplar paths. The paper annex needs `source.pdf`
and `extracted.md`; selected literature needs its full extracted text and an
original PDF or TeX source. The exact supplied Špalek–Szegedy publisher edition
is selected explicitly. Missing primary sources fail rather than falling back
to locator notes. The manifest binds the supplied paper PDF by its actual hash
and includes supplied annex metadata, without inventing an upstream Git pin.

For each job's primary Lean seeds, the builder follows local imports and then
the `Complexity.*`/`Cslib.*` proof-source closure. Job 10 also starts from the
`QuarticQuery` root. Supply the dependency checkout directories explicitly with
`--dependency-root complexitylib=PATH` and `--dependency-root cslib=PATH` when
the selected closure needs them. Their HEAD revisions must match this project's
Lake manifest; selected source and license/configuration files must agree with
those commits. Missing selected imports stop packaging. `dependencies/` carries
those focused sources with licenses and configuration; `DEPENDENCY_SOURCES.json`
records the module list, hashes and pins. Traversal stops at Mathlib and Lean
foundations with their toolchain/package pins recorded. No whole Mathlib tree or
`.lake` build products are copied.

Job 09 requires actual external contracts via `--backend-source MEMBER=PATH`.
Under the `lean-exposition/` member prefix, supply `docs/contracts.md`,
`docs/verification.md`, `src/lean_exposition/{contracts,cli,extraction,consumer,verification}.py`, and
`src/lean_exposition/resources/schemas/{graph,artifact,bundle}.schema.json`.
Supply primary Comparator documentation or source under `comparator/`, identifying
an installed toolchain source edition when that is the source being supplied.
If a group cannot be supplied, explicitly record
`--backend-unavailable 'comparator=reason'` or the corresponding
`lean-exposition` reason. `BACKEND_INPUT_STATUS.json` then marks the assignment
limited: dependent extraction or validation remains unassessed. An empty
backend input set cannot silently satisfy job 09.

After the source owners settle the intended inputs and approve that digest,
repeat the same command with `--build --freeze-digest DIGEST --dest /path/to/new-output`.
The destination must be outside the repository. A changed input or an existing
selected archive stops the build. The builder checks source/input hashes before
and after packaging, checks each temporary ZIP with
[check_packets.py](check_packets.py), and publishes without replacing existing
files. No sent packet is updated in place.

`EVIDENCE_SNAPSHOT.json` recomputes raw receipt and dependency-export currentness
against the included Lean/configuration bytes. `BUILD_STATUS.md` preserves
recorded statuses, including pending/running states, separately from currentness;
it never infers a live build from a missing receipt or a pass from an artifact's
mtime. Generated corpus booleans are supplied as recorded, not used to upgrade
evidence. Packaging runs no Lean build and establishes no mathematical review.
The existing round-one and round-two builder interfaces remain available.

Use `--native-result MEMBER=PATH` for optional raw native-run JSON,
`--native-log MEMBER=PATH` for accompanying logs, and
`--native-source MEMBER=PATH` for actual fixture or runner sources outside this
repository. Records retain their original statuses and hashes. Per-target
`inputs_before` labels map to included bytes only under the selected canonical
repository or to explicitly supplied native sources. A matching subset is
reported as current for those inputs only; foreign labels, skipped targets,
source drift and input changes during execution remain distinct. Module runs
do not establish declaration membership, Comparator success or a global build.

The ZIP is a focused research snapshot rather than a full checkout capable of
`make check`. In particular, selected round-two context does not contain every
custody archive required by that batch's intake manifest. Use a full checkout
for repository-wide checks.

## Check independent finite semantics

[return_checks/semantic_controls.py](return_checks/semantic_controls.py) compares
independently specified small examples with deliberately mutated Python models:

```sh
python3 tools/return_checks/semantic_controls.py
```

It covers zero-query promises, worst-case depth, the inclusive success threshold,
a Forrelation witness and a toy shared impossible comparison. The shared toy
truth tables agree while admitting no witness. The command does not read Lean,
compare any Lean definition or run Comparator; its output is finite diagnostic
evidence only. [Its tests](../tests/test_semantic_controls.py) exercise each
mutation and the independently specified answers.

## Reproduce checks supplied with reviews

[return_checks/verify_examples.py](return_checks/verify_examples.py) uses the
standard library and accepts an explicit output path:

```sh
python3 tools/return_checks/verify_examples.py --output /path/to/exact_example_results.json
```

[return_checks/finite_checks.py](return_checks/finite_checks.py) requires NumPy
and writes beside its own script. Keep the imported script unchanged; run a copy
in a temporary directory so generated JSON does not enter `tools/`:

```sh
check_dir=$(mktemp -d)
cp tools/return_checks/finite_checks.py "$check_dir/finite_checks.py"
python3 "$check_dir/finite_checks.py"
```

The printed output identifies the generated file. These programs reproduce finite
examples from advisory reviews; their output is not a Lean proof or a replacement
for the saved review records. The original return instructions and manifests
remain under [research/returns/](../research/returns/README.md).
