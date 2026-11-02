#!/usr/bin/env python3
"""Build the three independent Type B research ZIPs for the quartic separation."""
import argparse
import hashlib
import json
import pathlib
from string import Formatter
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
INTAKE = ROOT / "research" / "intake"
SOURCES = pathlib.Path.home() / "src" / "quartic-query-sources" / "papers"
ANNEX = pathlib.Path.home() / "src/ai_workflow/annexes/openai-math-284-quartic-query-separation"

REQUESTS = ROOT / "research" / "requests" / "review"

JOBS = {
    "1_understand_the_paper": "Understand and audit the paper",
    "2_ground_in_literature": "Ground every step in the literature",
    "3_lean_and_comparator": "Plan full Lean and Comparator checking",
}


def render_request(job, requests_dir=REQUESTS):
    """Compose authored instructions; archive names remain the packaging contract."""
    if job not in JOBS:
        raise ValueError(f"unknown packet: {job}")
    try:
        common = (requests_dir / "common.md").read_text(encoding="utf-8")
        boundary = (requests_dir / "boundaries.md").read_text(encoding="utf-8")
        body = (requests_dir / f"{job}.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise SystemExit(f"cannot read research request: {error}") from error
    try:
        fields = [field for _, field, spec, conversion in Formatter().parse(common)
                  if field is not None]
        if sorted(fields) != ["boundary", "job", "title"]:
            raise ValueError("expected {title}, {job} and {boundary} exactly once")
        return common.format(title=JOBS[job], job=body, boundary=boundary)
    except (KeyError, ValueError, IndexError) as error:
        raise SystemExit(f"invalid research request template {requests_dir / 'common.md'}: {error}") from error


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def members(job, *, intake=INTAKE, papers_dir=SOURCES, paper_annex=ANNEX,
            lean_dir=ROOT / "lean"):
    """Map stable archive names to configurable source owners."""
    if job not in JOBS:
        raise ValueError(f"unknown packet: {job}")
    out = {
        "corpus/statement_ledger.json": intake / "statement_ledger.json",
        "corpus/statement_ledger_notes.md": intake / "statement_ledger_notes.md",
        "corpus/commentary.json": intake / "commentary.json",
        "paper/quartic-query-separation.pdf": paper_annex / "source.pdf",
        "paper/extracted.md": paper_annex / "extracted.md",
        "literature/references_resolved.json": intake / "references_resolved.json",
    }
    if job.startswith(("1_", "2_")):
        out.update({f"literature/papers/{p.name}": p
                    for p in sorted(papers_dir.glob("*.pdf"))})
    if job.startswith(("1_", "3_")):
        out["lean/current/Drift.lean"] = lean_dir / "QuarticQuery/Tournament/Drift.lean"
    if job.startswith("3_"):
        for name in ("prior_art_quantum_lean.json", "prior_art_classical_lean.json",
                     "verification_tooling.md", "organisation_exemplars.md",
                     "internal_inheritance.md"):
            out[f"lean/{name}"] = intake / name
        for name in ("lakefile.toml", "lean-toolchain"):
            out[f"lean/current/{name}"] = lean_dir / name
    return out


def build(job, dest, **sources):
    files = members(job, **sources)
    missing = [str(v) for v in files.values() if not v.is_file()]
    if missing:
        raise SystemExit("missing sources: " + ", ".join(missing))
    keys = [k.casefold() for k in files]
    if len(keys) != len(set(keys)):
        raise SystemExit("case-colliding members")
    request = render_request(job)
    rows = [dict(member=k, source=str(v), bytes=v.stat().st_size, sha256=sha(v)) for k, v in files.items()]
    manifest = json.dumps(dict(packet=job, source_paper="openai/math 4eaee875", members=rows), indent=1)
    path = dest / f"quartic_{job}.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("READ_ME_FIRST.md", request)
        z.writestr("manifest.json", manifest)
        for k, v in files.items():
            z.write(v, k)
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:
            raise SystemExit(f"bad zip {path}")
        for row in rows:
            if hashlib.sha256(z.read(row["member"])).hexdigest() != row["sha256"]:
                raise SystemExit(f"hash mismatch {row['member']}")
    mb = path.stat().st_size / 1e6
    if mb > 500:
        raise SystemExit(f"{path} over 500 MB")
    print(f"{path}  {mb:.1f} MB  {len(rows) + 2} members")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", type=pathlib.Path, default=pathlib.Path.home() / "Downloads" / "quartic_type_b_20261101")
    ap.add_argument("--papers-dir", type=pathlib.Path, default=SOURCES,
                    help="directory containing cited-paper PDFs")
    ap.add_argument("--paper-annex", type=pathlib.Path, default=ANNEX,
                    help="directory containing source.pdf and extracted.md")
    ap.add_argument("--intake-dir", type=pathlib.Path, default=INTAKE,
                    help="directory containing research intake records")
    ap.add_argument("--lean-dir", type=pathlib.Path, default=ROOT / "lean",
                    help="Lean project containing QuarticQuery/ and Lake configuration")
    args = ap.parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)
    for job in JOBS:
        build(job, args.dest, intake=args.intake_dir,
              papers_dir=args.papers_dir, paper_annex=args.paper_annex,
              lean_dir=args.lean_dir)
