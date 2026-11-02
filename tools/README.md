# Maintenance commands

Run these commands from the repository root with Python 3.10 or newer.
They use only the standard library.

## Check the repository

```sh
make check
```

This checks file placement and local README links, then runs the Python tests.
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

Instruction text belongs in [research/requests/](../research/requests/). The
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
