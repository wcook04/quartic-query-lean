#!/usr/bin/env python3
"""Build the seven round-two ZIPs: fidelity, four Lean coverage jobs, sharp Forrelation, exponent.

Each ZIP stands alone. Beyond what the funnel packets carry, it holds the five
first-round returns as `previous_round/`, the funnel adjudication, every annexed
paper of the quartic cluster (TeX-extracted text and, where held, the original
arXiv source) with a reading order for its job, a record skeleton generated from
the recorded dependency export with its source currentness, and BUILD_STATUS.md
separating recorded evidence from local artifact observations. The manifest
records the SHA-256 of every member, and the archive
is reread and checked against it.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import zipfile
from string import Formatter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_funnel_packets as funnel  # noqa: E402
import build_corpus as corpus_evidence  # noqa: E402

ROOT = funnel.ROOT
REQUESTS = ROOT / "research" / "requests" / "round2"
ANNEXES = funnel.ANNEXES
COMPLEXITYLIB = ROOT / "lean" / ".lake" / "packages" / "complexitylib"
QUERY_LIB = "Complexity/Computability/QueryComplexity"
JOBS = {
    "1_statement_fidelity": "A hostile audit of what the formal statements mean",
    "2_lean_construction": "Lean for Sections 1 and 2: query models, Forrelation, the construction",
    "3_lean_quantum_upper": "Lean for Section 3: the quantum upper bound",
    "4_lean_classical_lower": "Lean for Sections 4 and 5: the randomized lower bound and the exponent",
    "5_lean_appendix_a": "Lean for Appendix A: the universal quartic upper bound",
    "6_sharp_uniform_forrelation": "The sharp uniform Forrelation lower bound",
    "7_single_family_exponent": "One family with exponent 4 - o(1)",
}
# Annex slugs each job should read first; every packet carries the whole cluster.
PRIORITY = {
    "1_statement_fidelity": ["quartic-lit-buhrman-dewolf-decision-tree-survey",
                             "quartic-lit-dewolf-quantum-computing-lecture-notes",
                             "quartic-ref-08-quantum-lower-bounds-by-polynomials",
                             "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i",
                             "quartic-ref-24-all-quantum-adversary-methods-are-equivale",
                             "quartic-ref-06-k-forrelation-optimally-separates-quantum"],
    "2_lean_construction": ["quartic-ref-06-k-forrelation-optimally-separates-quantum",
                            "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
                            "quartic-ref-02-separations-in-query-complexity-using-chea",
                            "quartic-ref-04-separations-in-query-complexity-based-on-p",
                            "quartic-ref-05-near-optimal-separations-of-certificate-co",
                            "quartic-lit-dewolf-quantum-computing-lecture-notes"],
    "3_lean_quantum_upper": ["quartic-ref-12-quantum-amplitude-amplification-and-estima",
                             "quartic-ref-11-tight-bounds-on-quantum-searching",
                             "quartic-ref-16-a-fast-quantum-mechanical-algorithm-for-da",
                             "quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu",
                             "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error",
                             "quartic-lit-montanaro-quantum-search-with-advice",
                             "quartic-lit-dewolf-quantum-computing-lecture-notes"],
    "4_lean_classical_lower": ["quartic-ref-13-improved-direct-product-theorems-for-rando",
                               "quartic-ref-22-towards-proving-strong-direct-product-theo",
                               "quartic-ref-02-separations-in-query-complexity-using-chea",
                               "quartic-ref-09-randomized-query-complexity-can-beat-certi",
                               "quartic-ref-06-k-forrelation-optimally-separates-quantum"],
    "5_lean_appendix_a": ["quartic-ref-03-degree-vs-approximate-degree-and-quantum-i",
                          "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo",
                          "quartic-lit-aaronson-quantum-implications-of-huangs-sensitivity",
                          "quartic-ref-24-all-quantum-adversary-methods-are-equivale",
                          "quartic-ref-08-quantum-lower-bounds-by-polynomials",
                          "quartic-lit-nisan-szegedy-degree-of-boolean-functions",
                          "quartic-lit-buhrman-dewolf-decision-tree-survey"],
    "6_sharp_uniform_forrelation": ["quartic-ref-06-k-forrelation-optimally-separates-quantum",
                                    "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
                                    "arxiv-2103-11604",
                                    "quartic-lit-wu-xor-forrelation-stochastic-calculus",
                                    "quartic-ref-26-towards-optimal-separations-between-quantu",
                                    "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
                                    "quartic-lit-girish-forrelation-is-extremally-hard",
                                    "quartic-lit-canonne-chen-mestre-quantumly-fast-classically-forrious",
                                    "quartic-lit-girish-fourier-spectrum-of-noisy-quantum-algorithms"],
    "7_single_family_exponent": ["quartic-ref-06-k-forrelation-optimally-separates-quantum",
                                 "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
                                 "quartic-ref-02-separations-in-query-complexity-using-chea",
                                 "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i",
                                 "quartic-ref-12-quantum-amplitude-amplification-and-estima",
                                 "quartic-ref-13-improved-direct-product-theorems-for-rando",
                                 "quartic-lit-montanaro-quantum-search-with-advice"],
}
WITH_COMPLEXITYLIB = {"1_statement_fidelity", "2_lean_construction", "3_lean_quantum_upper",
                      "4_lean_classical_lower", "5_lean_appendix_a"}
EXTRA_REPOSITORY = ["research/adjudication/funnel_adjudication.json",
                    "research/adjudication/funnel_adjudication_notes.md",
                    "research/adjudication/bansal_sinha_section54_second_reading.md",
                    "research/returns/README.md"]
PREVIOUS_SUFFIXES = {".md", ".json", ".bib", ".txt", ".pdf"}


def render_request(job, requests_dir=REQUESTS):
    """Compose the shared template, the job request and the boundaries."""
    if job not in JOBS:
        raise ValueError(f"unknown packet: {job}")
    try:
        common = (requests_dir / "common.md").read_text(encoding="utf-8")
        boundary = (requests_dir / "boundaries.md").read_text(encoding="utf-8")
        body = (requests_dir / f"{job}.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise SystemExit(f"cannot read round-two request: {error}") from error
    fields = sorted(field for _, field, _, _ in Formatter().parse(common) if field is not None)
    if fields != ["boundary", "job", "title"]:
        raise SystemExit(f"{requests_dir / 'common.md'}: needs {{title}}, {{job}}, {{boundary}} once")
    return common.format(title=JOBS[job], job=body, boundary=boundary)


def cluster_slugs(annexes=ANNEXES):
    slugs = sorted(p.name for p in annexes.iterdir()
                   if p.is_dir() and p.name.startswith(("quartic-ref-", "quartic-lit-")))
    return slugs + ["arxiv-2103-11604"]


def literature(job, annexes=ANNEXES):
    out = {}
    for slug in cluster_slugs(annexes):
        folder = annexes / slug
        if not (folder / "extracted.md").is_file():
            raise SystemExit(f"missing literature source: {folder}")
        for name in ("extracted.md", "annex_notes.json", "source.tar.gz"):
            if (folder / name).is_file():
                out[f"literature/{slug}/{name}"] = folder / name
    missing = [slug for slug in PRIORITY[job] if not (annexes / slug).is_dir()]
    if missing:
        raise SystemExit("missing priority literature: " + ", ".join(missing))
    return out


def literature_guide(job, annexes=ANNEXES):
    lines = ["# Literature in this packet", "",
             "Each folder is one annexed paper: `extracted.md` (text, from the authors' TeX where "
             "held), `annex_notes.json` (our locator and relevance notes) and, where present, "
             "`source.tar.gz` (the original arXiv source). Prefer the TeX for exact statements.", "",
             "## Read first for this job", ""]
    lines += [f"{i}. `{slug}`" for i, slug in enumerate(PRIORITY[job], 1)]
    lines += ["", "## Everything else held", ""]
    lines += [f"- `{slug}`" for slug in cluster_slugs(annexes) if slug not in PRIORITY[job]]
    return ("\n".join(lines) + "\n").encode()


def record_skeleton(root=ROOT):
    """Group tied declarations, qualifying recorded reach by source currentness."""
    deps = json.loads((root / "corpus/lean_dependencies.json").read_text(encoding="utf-8"))
    freshness = corpus_evidence.currentness(deps, corpus_evidence.source_hashes(root))
    statements = json.loads((root / "corpus/statements.json").read_text(encoding="utf-8"))
    rows = statements["statements"] if isinstance(statements, dict) else statements
    tied, placed = {}, set()
    for row in rows:
        for tie in row.get("lean", []):
            tied.setdefault(tie["declaration"], []).append(row)
    reached = set(deps["reached"])
    by_file = {}
    for row in rows:
        for tie in row.get("lean", []):
            by_file.setdefault(tie.get("file") or "(unlocated)", set()).add(tie["declaration"])
    lines = ["# Record skeleton", "",
             "Generated from `corpus/lean_dependencies.json` (the recorded dependency export for "
             f"{', '.join(f'`{r}`' for r in deps['roots'])}) and `corpus/statements.json`. Sections "
             "follow the Lean modules that carry tied declarations, foundations first; each lists the "
             "tied declarations, whether the headline reaches them, and the paper statements tied to "
             "them with their stored evidence fields. Statements with no Lean tie are listed at the end.", "",
             f"Dependency-export source currentness: `{freshness}`. Only a `current` export establishes "
             "reach for these source bytes. Membership in a stale or legacy unbound export is historical; "
             "absence from it does not establish that the current headline omits a declaration. "
             "Regenerate corpus records after changing their inputs.", ""]
    order = ["Statement", "Model", "Bridge", "Construction", "Forrelation/", "ForrelationLower",
             "Amplification", "Tournament", "Upper", "LowerBound", "Appendix", "Paper", "Results"]

    def rank(path):
        return next((i for i, key in enumerate(order) if key in path), len(order)), path

    for path in sorted(by_file, key=rank):
        lines += [f"## `{path}`", ""]
        for name in sorted(by_file[path]):
            if freshness == "current":
                mark = "reached" if name in reached else "outside the current headline closure"
            else:
                membership = "recorded reached" if name in reached else "not recorded reached"
                mark = f"{membership}; current reach unknown ({freshness})"
            lines.append(f"- `{name}` ({mark})")
            for row in tied.get(name, []):
                ev = row["evidence"]
                tie = next(t for t in row["lean"] if t["declaration"] == name)
                lines.append(f"  - `{row['id']}` ({row['kind']}, §{row.get('section')}): relation "
                             f"{tie.get('relation')}, route {tie.get('route')}; statement "
                             f"{ev.get('formal_statement')}, build {ev.get('build')}, comparator "
                             f"{ev.get('comparator')}, reach {ev.get('reach')}")
                placed.add(row["id"])
        lines.append("")
    lines += ["## Paper statements with no Lean tie", ""]
    lines += [f"- `{row['id']}` ({row['kind']}, §{row.get('section')})"
              for row in rows if row["id"] not in placed]
    return ("\n".join(lines) + "\n").encode()


def build_status(root=ROOT):
    """Separate a named historical receipt from artifact existence and mtime observations."""
    build = root / "lean" / ".lake" / "build" / "lib" / "lean"
    modules = sorted(p for p in (root / "lean" / "QuarticQuery").rglob("*.lean"))
    receipt = json.loads((root / "corpus/receipts/lean-build-root.json").read_text(encoding="utf-8"))
    freshness = corpus_evidence.currentness(receipt, corpus_evidence.source_hashes(root))
    lines = ["# Build status at packet time", "",
             f"Named historical receipt `corpus/receipts/lean-build-root.json`: commit "
             f"`{receipt.get('commit')}`, recorded status `{receipt.get('status')}`, "
             f"source currentness `{freshness}`. This paragraph does not select newer timestamped receipts.", "",
             "The table reports local artifact existence and modification times only. A `.olean` newer "
             "than source does not bind its contents to the current source bytes or establish a new build. "
             "Use current source-bound corpus receipts for build evidence; compilation is separate from review.", "",
             "| Module | .olean artifact exists | Artifact mtime >= source mtime |", "| --- | --- | --- |"]
    for path in modules:
        rel = path.relative_to(root / "lean")
        olean = build / rel.with_suffix(".olean")
        fresh = olean.is_file() and olean.stat().st_mtime >= path.stat().st_mtime
        lines.append(f"| `{rel}` | {'yes' if olean.is_file() else 'no'} | {'yes' if fresh else 'no'} |")
    return ("\n".join(lines) + "\n").encode()


def members(job, root=ROOT, annexes=ANNEXES):
    out = funnel.members("1_long_reasoning_record", root=root, annexes=annexes)
    out = {name: source for name, source in out.items() if not name.startswith("literature/")}
    for name in EXTRA_REPOSITORY:
        out[f"repository/{name}"] = root / name
    for path in sorted((root / "research" / "returns" / "funnel").rglob("*")):
        if path.is_file() and path.suffix in PREVIOUS_SUFFIXES:
            out[f"previous_round/{path.relative_to(root / 'research/returns/funnel').as_posix()}"] = path
    for path in sorted((root / "tools" / "return_checks").glob("funnel*.py")):
        out[f"previous_round/scripts/{path.name}"] = path
    if job in WITH_COMPLEXITYLIB:
        base = COMPLEXITYLIB / QUERY_LIB
        if not base.is_dir():
            raise SystemExit(f"missing complexitylib source: {base}")
        for path in sorted(base.rglob("*.lean")):
            out[f"complexitylib/{QUERY_LIB}/{path.relative_to(base).as_posix()}"] = path
    out.update(literature(job, annexes))
    return out


def build(job, dest):
    files = members(job)
    missing = [str(v) for v in files.values() if not isinstance(v, tuple) and not v.is_file()]
    if missing:
        raise SystemExit("missing sources: " + ", ".join(missing))
    data = {name: funnel.content(source) for name, source in files.items()}
    data["literature/README.md"] = literature_guide(job)
    data["skeleton/record_skeleton.md"] = record_skeleton()
    data["BUILD_STATUS.md"] = build_status()
    sources = {**{k: str(v if not isinstance(v, tuple) else f"{v[0]}@{v[1]}:{v[2]}")
                  for k, v in files.items()},
               "literature/README.md": "generated", "skeleton/record_skeleton.md": "generated",
               "BUILD_STATUS.md": "generated"}
    rows = [dict(member=name, source=sources[name], bytes=len(blob),
                 sha256=hashlib.sha256(blob).hexdigest()) for name, blob in data.items()]
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    manifest = json.dumps(dict(packet=job, campaign="round2", repository_commit=commit,
                               source_paper="openai/math 4eaee875", members=rows), indent=1)
    path = dest / f"quartic_r2_{job}.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("READ_ME_FIRST.md", render_request(job))
        archive.writestr("manifest.json", manifest)
        for name, blob in data.items():
            archive.writestr(name, blob)
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise SystemExit(f"bad zip {path}")
        for row in rows:
            if hashlib.sha256(archive.read(row["member"])).hexdigest() != row["sha256"]:
                raise SystemExit(f"hash mismatch {row['member']}")
    print(f"{path}  {path.stat().st_size / 1e6:.1f} MB  {len(rows) + 2} members")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dest", type=pathlib.Path,
                        default=funnel.HOME / "Downloads" / "quartic_round2_20261102")
    parser.add_argument("--only", choices=sorted(JOBS))
    args = parser.parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)
    for job in JOBS:
        if not args.only or args.only == job:
            build(job, args.dest)


if __name__ == "__main__":
    main()
