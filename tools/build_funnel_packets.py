#!/usr/bin/env python3
"""Build the five funnel ZIPs: long record, short paper, exposition, route note, reader.

Each ZIP stands alone. It carries the request, the preprint, the repository's
current statements, evidence and Lean source, the writing guides, the three
exemplar papers of the earlier project, and the sources its job needs. The
manifest records the SHA-256 of every member, and the archive is reread and
checked against it.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
from string import Formatter
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUESTS = ROOT / "research" / "requests" / "funnel"
HOME = pathlib.Path.home()
SOURCES = HOME / "src" / "quartic-query-sources" / "papers"
ANNEXES = HOME / "src" / "ai_workflow" / "annexes"
GUIDES = HOME / ".claude" / "skills" / "formal-math-exposition" / "references"
EXEMPLAR_REPO = HOME / "src" / "lean-exposition"
EXEMPLAR_REF = "origin/main"
EXEMPLARS = {
    "exemplars/long-reasoning-record.md": "papers/qaoa-sk/long/reasoning-record.md",
    "exemplars/short-paper.md": "papers/qaoa-sk/short/paper.md",
    "exemplars/expository.md": "papers/qaoa-sk/expository/main.md",
    "exemplars/short-correspondence.json": "papers/qaoa-sk/short/correspondence.json",
}
JOBS = {
    "1_long_reasoning_record": "The long reasoning record",
    "2_short_expert_paper": "The short expert paper",
    "3_examples_first_exposition": "The examples-first exposition",
    "4_forrelation_route_note": "The Forrelation lower-bound route",
    "5_reader_and_film": "The reader's map and the film",
}
# Cited works each job reads in full, by annex slug (TeX-backed text where held).
LITERATURE = {
    "1_long_reasoning_record": "all",
    "2_short_expert_paper": ["quartic-ref-02-separations-in-query-complexity-using-chea",
                             "quartic-ref-06-k-forrelation-optimally-separates-quantum",
                             "quartic-ref-13-improved-direct-product-theorems-for-rando",
                             "quartic-ref-12-quantum-amplitude-amplification-and-estima",
                             "arxiv-2103-11604"],
    "3_examples_first_exposition": [],
    "4_forrelation_route_note": ["quartic-ref-06-k-forrelation-optimally-separates-quantum",
                                 "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
                                 "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
                                 "quartic-ref-26-towards-optimal-separations-between-quantu",
                                 "quartic-lit-girish-forrelation-is-extremally-hard",
                                 "quartic-lit-bravyi-classical-algorithms-for-forrelation",
                                 "arxiv-2103-11604"],
    "5_reader_and_film": [],
}
REPOSITORY_FILES = ["README.md", "corpus/README.md", "corpus/statements.json",
                    "corpus/coverage.json", "corpus/evidence-graph.json", "corpus/ties.json",
                    "corpus/lean_dependencies.json", "research/intake/statement_ledger_notes.md",
                    "research/returns/adjudication.json", "research/returns/adjudication_notes.md"]


def render_request(job, requests_dir=REQUESTS):
    """Compose the shared template, the job request and the boundaries."""
    if job not in JOBS:
        raise ValueError(f"unknown packet: {job}")
    try:
        common = (requests_dir / "common.md").read_text(encoding="utf-8")
        boundary = (requests_dir / "boundaries.md").read_text(encoding="utf-8")
        body = (requests_dir / f"{job}.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise SystemExit(f"cannot read funnel request: {error}") from error
    fields = sorted(field for _, field, _, _ in Formatter().parse(common) if field is not None)
    if fields != ["boundary", "job", "title"]:
        raise SystemExit(f"{requests_dir / 'common.md'}: needs {{title}}, {{job}}, {{boundary}} once")
    return common.format(title=JOBS[job], job=body, boundary=boundary)


def git_bytes(repo, ref, path):
    result = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{path}"],
                            capture_output=True)
    if result.returncode:
        raise SystemExit(f"cannot read {ref}:{path} in {repo}")
    return result.stdout


def literature(job, annexes=ANNEXES):
    wanted = LITERATURE[job]
    if wanted == "all":
        slugs = sorted(p.name for p in annexes.glob("quartic-ref-*") if p.is_dir())
        slugs += ["arxiv-2103-11604"]
    else:
        slugs = wanted
    out = {}
    for slug in slugs:
        folder = annexes / slug
        if not (folder / "extracted.md").is_file():
            raise SystemExit(f"missing literature source: {folder}")
        for name in ("extracted.md", "annex_notes.json"):
            if (folder / name).is_file():
                out[f"literature/{slug}/{name}"] = folder / name
    return out


def members(job, *, root=ROOT, guides=GUIDES, annexes=ANNEXES,
            exemplar_repo=EXEMPLAR_REPO, exemplar_ref=EXEMPLAR_REF):
    """Map archive names to a file path or to bytes read from the exemplar repository."""
    if job not in JOBS:
        raise ValueError(f"unknown packet: {job}")
    paper = annexes / "openai-math-284-quartic-query-separation"
    out = {"paper/quartic-query-separation.pdf": paper / "source.pdf",
           "paper/extracted.md": paper / "extracted.md"}
    for name in REPOSITORY_FILES:
        out[f"repository/{name}"] = root / name
    for path in sorted((root / "docs").glob("*.md")):
        out[f"repository/docs/{path.name}"] = path
    lean = root / "lean"
    for path in sorted(lean.rglob("*")):
        relative = path.relative_to(lean)
        if path.is_file() and ".lake" not in relative.parts and path.suffix in {
                ".lean", ".json", ".toml"} or relative.as_posix() == "lean-toolchain":
            out[f"repository/lean/{relative.as_posix()}"] = path
    for path in sorted(guides.glob("*.md")):
        out[f"writing/{path.name}"] = path
    for name, source in EXEMPLARS.items():
        out[name] = (exemplar_repo, exemplar_ref, source)
    if job == "3_examples_first_exposition":
        returns = root / "research" / "returns" / "1_understand_the_paper"
        out["repository/research/returns/worked_examples.md"] = returns / "worked_examples.md"
        out["repository/tools/verify_examples.py"] = root / "tools/return_checks/verify_examples.py"
    out.update(literature(job, annexes))
    return out


def content(source):
    if isinstance(source, tuple):
        return git_bytes(*source)
    return source.read_bytes()


def build(job, dest, **sources):
    files = members(job, **sources)
    missing = [str(v) for v in files.values() if not isinstance(v, tuple) and not v.is_file()]
    if missing:
        raise SystemExit("missing sources: " + ", ".join(missing))
    data = {name: content(source) for name, source in files.items()}
    rows = [dict(member=name, source=str(source if not isinstance(source, tuple)
                                          else f"{source[0]}@{source[1]}:{source[2]}"),
                 bytes=len(blob), sha256=hashlib.sha256(blob).hexdigest())
            for (name, source), blob in zip(files.items(), data.values())]
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    manifest = json.dumps(dict(packet=job, repository_commit=commit,
                               source_paper="openai/math 4eaee875", members=rows), indent=1)
    path = dest / f"quartic_{job}.zip"
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
                        default=HOME / "Downloads" / "quartic_funnel_20261102")
    parser.add_argument("--only", choices=sorted(JOBS))
    args = parser.parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)
    for job in JOBS:
        if not args.only or args.only == job:
            build(job, args.dest)


if __name__ == "__main__":
    main()
