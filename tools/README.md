# Maintenance commands

Run these commands from the repository root with Python 3.10 or newer.
The top-level Python tools use only the standard library; commands that invoke
Lean or Comparator also need their pinned external tools. The imported finite
checker described below additionally needs NumPy.

The [reading API compiler](build_reading_api.py) exports the three papers, cross-paper routes and formal sources. [Reading evidence](reading_evidence.py) joins their existing statement reviews and recorded checks. Run `make reading-api` for the [static data contract](../docs/reading_api.md).

[intake_round7_returns.py](intake_round7_returns.py) preserves four round-seven
archives and their members without running submitted scripts. Supply their source
directory with `--source-dir PATH`; `--verify` requires all extracted members,
including ignored scripts and checksum files, and checks archive hashes when
the local originals are present. A public clone without those local custody
files cannot complete this verification. See the [returns guide](../research/returns/README.md#round-seven-returns)
for the advisory inventory and custody boundary.

[build_round10_packets.py](build_round10_packets.py) builds the three current
chronological improvement reviews. Every packet carries all 42 retained query
literature sources, the preprint, the required supplementary mathematical
editions and six complete writing references, the exact merged writing-method
closure, and the full Lake-pinned Complexitylib source. The
[reviewed citation map](../research/requests/round10/citation_coverage.json)
covers every bibliography entry and Appendix C; its generated coverage report
separates original editions, alternatives and inaccessible originals.

```sh
python3 tools/build_round10_packets.py --annexes /path/to/annexes \
  --paper-annex /path/to/annexes/openai-math-284-quartic-query-separation \
  --expert-pdf /path/to/fresh-render/expert/expert_companion.pdf \
  --exposition-pdf /path/to/fresh-render/exposition/exposition.pdf \
  --record-pdf /path/to/fresh-render/record/reasoning_record.pdf \
  --lean-exposition /path/to/merged-lean-exposition-checkout \
  --supplementary-literature /path/to/supplement/manifest.json \
  --complexitylib /path/to/pinned-complexitylib-checkout \
  --dest /path/to/new-round10-batch
python3 tools/check_packets.py /path/to/new-round10-batch
```

The writing-method checkout must contain revision
`7bc9ef5d253d23527c6ccbd759c2eb24c0243ac7`; selected bytes must match that commit.
The `--complexitylib` checkout must contain the Lake-pinned revision; if omitted,
the builder reads `lean/.lake/packages/complexitylib`. It exports tracked Git
bytes and never runs submitted or dependency scripts. All three PDFs require
current native `render.json` receipts beside them, with visual inspection
recorded separately. The three original round-nine ZIPs and every submitted
member, including ignored scripts and JSONL, must exist at the paths in the
[intake inventory](../research/returns/round9/intake.json) and match its hashes.
A public clone without those local originals cannot build this campaign.

The required supplementary manifest has schema
`quartic-round10-supplementary-literature-v1` and a `sources` array. Each source
names `id`, `role` (`query-literature` or `writing-literature`), `title`,
`source_url`, `edition`, `edition_relation`, `citation_keys` and `files`.
Each file specifies its manifest-relative `path`, archive `member`, `bytes` and
`sha256`; provide a complete original PDF/TeX archive and an `extracted*.md` or
`extracted*.txt` full-text copy. Archive members belong under `literature/` or
`writing_literature/` according to the role. The citation map owns the required
source IDs. An earlier primary edition must remain labelled as earlier.

Omit `--dest` to validate inputs without publishing ZIPs. Use `TMPDIR` on an
appropriate scratch volume for the complete source exports. Existing batch
directories are refused, and source hashes are checked again before publication.
The generated `LITERATURE_COVERAGE.json`, `METHOD_PROVENANCE.json`,
`CODE_SOURCE_PROVENANCE.json` and native render receipts identify exactly what
was supplied; none claims a new proof build, mathematical review or reader test.
See the [selection](../research/requests/round10/SELECTION.md) for the assignment.

[build_round9_packets.py](build_round9_packets.py) builds three improvement-only
review packets, one each for the expert companion, exposition and full record.
It adds a chronological sentence audit, line-numbered reading copies, complete
round-eight text/JSON returns and revision notes, the local method refinements,
and fresh register measurements. See the [selection](../research/requests/round9/SELECTION.md).
Render all three PDFs first. Each must have its renderer's `render.json` beside
it; the builder rejects stale PDFs and changed render inputs. Hash validation
does not replace page-image inspection.

```sh
python3 tools/render_papers.py --output-dir /path/to/fresh-render
python3 tools/render_reasoning_record.py --output-dir /path/to/fresh-render/record
python3 tools/build_round9_packets.py --annexes /path/to/annexes \
  --paper-annex /path/to/annexes/openai-math-284-quartic-query-separation \
  --expert-pdf /path/to/fresh-render/expert/expert_companion.pdf \
  --exposition-pdf /path/to/fresh-render/exposition/exposition.pdf \
  --record-pdf /path/to/fresh-render/record/reasoning_record.pdf \
  --lean-exposition /path/to/lean-exposition --dest /path/to/new-batch
python3 tools/check_packets.py /path/to/new-batch
```

The local writing guide is retained at `repository/docs/writing_method.md`.
Its compatibility copy at `skills/quartic-writing-method.md` has relative links
rebased to the packaged repository paths, and the builder includes their source
closure. Frozen packets retain the exact bytes originally sent.

Outputs stay outside the checkout; use a volume that satisfies the renderer's
space reserve. The command reuses the frozen round-eight writer and existing
link/private-name checks. Nothing is sent. Omit `--dest` for input validation.

[build_round8_packets.py](build_round8_packets.py) builds two feedback packets,
one per short paper: specialist referees of the expert companion, and newcomers
and teachers reading the exposition. It reuses the round-seven machinery, including
the writing method and register measurement, and supplies the round-seven synthesis,
revision notes, audits and verdicts as the previous round. Pass the three PDFs rendered
from the current Markdown; the [selection](../research/requests/round8/SELECTION.md)
describes the panels. Run without `--dest` to validate the inputs without writing ZIPs.

The round-three intake uses [intake_round3_returns.py](intake_round3_returns.py) to
preserve and verify exact archive/member bytes. It does not execute submitted
code. The [round-four builder](build_round4_packets.py) reuses the preceding
packet machinery and requires an accepted review of the current integrated
record, bibliography, correspondence, corpus, Lean snapshot and exact rendered
PDF before writing archives. The accepted review's `pdf_sha256` must match the
PDF supplied through `--record-render`; a mechanical render does not certify its
own visual acceptance. The [selection](../research/requests/round4/SELECTION.md)
explains the seven substantial jobs and their shared release gate.

The explicit `--backend-sources`, `--method-sources` and
`--structural-exemplars` inputs select pinned implementations, task-relevant
skills with their supporting references, and actual SK/257 specimens. Use
`--context-report` for an external validation-only report of the per-job reading
maps, context manifests and source/link checks; it writes no ZIPs. Use `--help`
for the complete inputs and freeze procedure. Each packet carries the editable
long record and its matching PDF beside it, preserving relative reading links.
Curated packets support their named focused checks; they do not contain the
whole historical custody tree needed for every repository maintenance check.

The [round-five builder](build_round5_packets.py) packages five critique jobs
described in its [selection](../research/requests/round5/SELECTION.md). It reuses
the round-three archive writer and the round-four reading-link closure, applies
no acceptance gate, and instead binds each packet to the exact current draft,
PDF and record bytes in `SOURCE_STATUS.json`. `LINK_MAP.json` resolves every
draft link and checks its anchor or line range. The rendered draft PDFs are
explicit external inputs:

```sh
python3 tools/build_round5_packets.py --annexes /path/to/annexes \
  --paper-annex /path/to/annexes/openai-math-284-quartic-query-separation \
  --expert-pdf /path/to/expert_companion.pdf --exposition-pdf /path/to/exposition.pdf \
  --dest /path/to/new-batch
```

Without `--dest` it validates and prints a freeze digest; pass it back with
`--freeze-digest` to refuse a build whose inputs changed.

[render_papers.py](render_papers.py) renders the expert companion and the
exposition from `docs/` with Pandoc and Tectonic in one shared paper style. It
compiles the TikZ figure sources under `docs/figures/` (PDFs go to the output
directory, SVG copies next to the sources for GitHub) and refuses an output
directory inside the checkout. Default output is
`../_builds/quartic-r4/render/<paper>/` beside the checkout; it needs `pandoc`,
`tectonic` and `pdftocairo`. A render is not an inspection of the pages.

```sh
python3 tools/render_papers.py [--paper expert|exposition|all] [--output-dir DIR]
```

[render_reasoning_record.py](render_reasoning_record.py) renders a copied
manuscript snapshot with Pandoc and Tectonic, reusing the submitted round-three
layout sources. PDF and layout receipts belong outside the source tree. A
successful render is separate from inspection and mathematical review.
Authored HTML anchors become PDF destinations (`\hypertarget` plus `\label`, so
both Pandoc link forms resolve), and the five directory links name reviewed
files instead of nonexistent `<dir>/.pdf` targets. The render stops on an
unreviewed directory link, an anchorless internal link, a missing destination or
an undefined LaTeX reference. The [round-four backend adjudication](../research/adjudication/round4_backend.md)
records how the two returned repairs were merged.

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
| `python3 tools/build_comparator_map.py` | Regenerates `corpus/comparator_map.json`, the Challenge-to-record reading map. Run after the corpus. |
| `python3 tools/build_lean_links.py` | Regenerates the human-readable `docs/proof_index.md` from its authored introduction, `docs/lean_links.json`, and the Lean link definitions at the end of the expert companion, the exposition, reasoning record and verification reference. `COMMIT` selects Lean sources; `RECORD_COMMIT` independently selects the record edition for shorter-paper and bibliography links. |

After revising the record, run `rebind_record_passages.py --report PATH` and
`build_comparator_map.py`. Commit the record, then update `RECORD_COMMIT` and
run `build_lean_links.py`. Read the exact linked body before accepting the
destinations; anchor existence alone does not establish the promised proof.
Separating these pins lets an editorial record revision preserve its Lean links
and match the linked edition byte for byte. Re-render affected reading copies.

[build_challenges.py](build_challenges.py) keeps a challenge and its solution in
agreement by construction. A negative control counts only when Comparator rejects it
with the expected diagnostic, and a build deferred by a lock judges nothing.
Build and comparison producers append timestamped receipts; old runs remain
historical. Both check that their source/configuration hashes remain unchanged
during execution. The hashes bind local source and dependency pins, not the
bytes of external dependency checkouts. These are local verification runs, not
fresh-clone reproducibility certificates.

New Comparator receipts list only the configuration's `theorem_names` as
compared declarations. A source theorem used by a wrapper is not itself a
configured comparison target. Earlier receipts also inferred implementation
names by scanning `exact QuarticQuery.*` lines; that scan can include comments,
unrelated helpers or specializations. Keep those receipts intact, and treat
their extra names as wrapper-mediated historical claims requiring a separate
type correspondence. To obtain direct comparison evidence for a source theorem,
configure that theorem's own name in an independently compiled challenge and
solution. Changing the producer does not rerun a historical comparison.

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

## Run the independent round-three Lean checks

[return_checks/round3_formal.py](return_checks/round3_formal.py) runs the authored
equation (19), the construction theorem with physical-coordinate support, and
finite semantic modules serially, inspects theorem types and
axioms, then runs their six dedicated Comparator cases. It records the whole
local Lean/configuration inventory before and after execution, command logs and
an 8 GiB free-space reserve. It does not update corpus receipts or ties.

```sh
python3 tools/return_checks/round3_formal.py --timeout 900 --output /path/to/native-results
```

Use `--phase build`, `--phase audit` or `--phase compare` for a bounded rerun.
The intentionally shared impossible-premise case should be accepted: this
shows that agreement alone cannot establish mathematical meaning. The omitted
equality and changed threshold cases must be rejected with their intended
diagnostics; an unrelated build failure does not count. Outcomes and the
remaining evidence boundaries are in the
[formal adjudication](../research/adjudication/round3_formal.md).

The passage rebinder and Comparator map read both the mathematical account and its verification reference. Each passage and excerpt retains its actual file path and local line range. Moving an appendix changes its location, not its mathematical or checking status.

[reading_selection.py](reading_selection.py) binds exact reading selections and
prepares graph and reverse indexes. [reader.mjs](reader.mjs) consumes the static
edition, and [query_reading_api.mjs](query_reading_api.mjs) runs that client
headlessly. [ReadDependencies.lean](ReadDependencies.lean) and its
[recorder](record_reading_dependencies.py) own the optional native graph refresh.

[ReadApplications.lean](ReadApplications.lean) inspects the actual parameters and
proof obligations of selected Lean applications. The same recorder refreshes
them with `--applications` and independently checks them with
`--applications --compare`. [reading_applications.py](reading_applications.py)
binds them to manuscript topics and exact source excerpts.
