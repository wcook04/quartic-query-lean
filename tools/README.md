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

Run these after a successful `lake build QuarticQuery`:

| Command | Effect |
| --- | --- |
| `python3 tools/build_challenges.py` | Regenerates each Comparator challenge from the statement file and its solution. |
| `python3 tools/record_evidence.py` | Records the compiled dependency closure and a build receipt. |
| `python3 tools/run_comparator.py` | Runs each bundle and negative control and writes receipts. |
| `python3 tools/build_corpus.py` | Regenerates the corpus from the ledger, ties and receipts. |

[build_challenges.py](build_challenges.py) keeps a challenge and its solution in
agreement by construction. A negative control counts only when Comparator rejects it
with the expected diagnostic, and a build deferred by a lock judges nothing.

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
cluster with a reading order for its job, a record skeleton generated from the
compiled dependency closure, and `BUILD_STATUS.md`, which reports which Lean
modules have an up-to-date `.olean`. The fidelity and four Lean coverage packets
also carry complexitylib's query-complexity source.

```sh
python3 tools/build_round2_packets.py --only 1_statement_fidelity --dest /path/to/output
```

Omit `--only` to build all five. This builder reads the current repository,
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
