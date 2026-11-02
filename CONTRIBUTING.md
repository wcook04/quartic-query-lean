# Working on the repository

Start with the [repository map](README.md#repository-map). Choose the source
owner below before editing, then check the affected work from the repository
root. Python maintenance commands need Python 3.10 or newer, Git and Make.

| Change | Edit here | Validate |
| --- | --- | --- |
| Lean definitions or proofs | [Lean project](lean/README.md) | Build the affected modules with the pinned toolchain; record build and comparison evidence separately. |
| A statement's reviewed relation to Lean | [ties.json](corpus/ties.json) | Follow the [evidence contract](docs/statement_evidence_contract.md), regenerate the corpus, then `make check`. |
| A review decision | [Adjudication](research/adjudication/) | Preserve the original submission, update maintained decisions and regenerate affected corpus records. |
| Instructions for a research batch | [Request campaigns](research/requests/README.md) | Edit templates, run their tests, rebuild the affected packets and audit the completed ZIPs. |
| A maintenance command | [Tools](tools/README.md) and its matching [test module](tests/README.md) | Run the focused test module, then `make check`. |
| Navigation or file placement | The relevant directory guide and [layout checker](tools/check_repository.py) | Find consumers before a move; run `make check-layout` and `make check-index`. |

The [corpus guide](corpus/README.md#producers-and-inputs) identifies which data
is reviewed, recorded or generated. Edit the source owner and run its producer;
do not repair generated JSON by hand. Source presence, successful compilation,
Comparator acceptance and a review of mathematical meaning are separate facts.

## Names and moves

Python commands use `snake_case.py`; tests use `test_<command>.py`. Lean file
paths define import names, so a move needs an import and consumer review.
Statement IDs, declaration names, recorded receipts and archive member paths
may have consumers outside the repository. Preserve them during a cleanup.

Keep returns as submitted and corrections under `research/adjudication/`.
Each request campaign has its own directory. Store generated ZIPs outside the
checkout; keep dependencies and build products untracked.

## Run the relevant checks

```sh
make check-layout     # File roles and local navigation links
make check-generated  # Challenges and corpus match their sources
make check-tests      # Python maintenance-tool tests
make check            # All three; does not build Lean
```

For one tool, use unittest discovery with its matching filename:

```sh
python3 -m unittest discover -s tests -p 'test_check_packets.py'
```

Use the [maintenance guide](tools/README.md) for generator, Lean evidence and
packet-building commands. Tests use temporary output directories; they must
not rewrite a live batch or rely silently on private source checkouts.

## Check a completed packet batch

The independent [packet checker](tools/check_packets.py) reads ZIPs without
extracting or modifying them. Pass a completed batch directory or one or more
ZIP paths:

```sh
python3 tools/check_packets.py /path/to/completed-batch
python3 tools/check_packets.py /path/to/one-packet.zip
```

It checks unique member paths, complete manifest coverage, byte lengths and
SHA-256 hashes. Every ZIP gets a result, and any failure returns a nonzero exit
code. It accepts the review, funnel, round-two and round-three manifest formats, including
compatibility aliases and historical source labels that are unavailable locally.
It reads stored or deflated members, the formats used by these builders.
Directory selection includes only ZIPs directly inside that directory.

Run it after construction finishes. A pass establishes agreement with the
embedded manifest, not source freshness, mathematical correctness or whether
every expected job in a campaign is present. The checker requires a readable `READ_ME_FIRST.md` and manifest, but does not
compare them with an earlier version. Round three additionally records
`request_sha256` in its manifest; verify it when auditing that campaign. The
manifest itself is not self-hashed. Preserve sent archives as snapshots;
make revised packets in a new output directory.

## Shared work and commits

Inspect `git status --short` before editing. While another agent is building a
packet, leave its builders, templates and selected inputs unchanged. The funnel
and round-two builders include root README, Lean and corpus guides and
`docs/*.md`; documentation can therefore be an active input too.

Stage only your own files, inspect `git diff --cached`, then run:

```sh
make check-index
```

This checks the staged paths and navigation contents, even if working files
differ. It does not run tests against the staged version. Report which checks
ran, the commit and any checks that still need their external prerequisites.
