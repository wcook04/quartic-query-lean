#!/usr/bin/env python3
"""Build the four round-six expert-emulation critique packets.

Round six reuses the round-five packet machinery (hash binding, link map, leak
checks, manifest and independent checker) with four new panels. Each panel reads
the three documents as a community of cited-literature authors and asks why each
part exists. Every packet also carries the general writing skills, principles
distilled from outside readers of AI-produced mathematics, and the previous
round's verdicts, dispositions and reviews, so the panel can judge the method and
avoid repeating fixed findings.

    python3 tools/build_round6_packets.py --annexes ANNEXES --paper-annex PREPRINT \\
        --expert-pdf E.pdf --exposition-pdf X.pdf --record-pdf R.pdf --dest NEW_FOLDER
"""

import argparse
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_round5_packets as base  # noqa: E402

ROOT = base.ROOT
CAMPAIGN = "round6"
JOBS = {
    "quantum_experts": "How the quantum-algorithms community would read these documents",
    "classical_experts": "How the randomized-lower-bound and separations community would read these documents",
    "formal_methods_readers": "How formal-methods readers and sceptics would read the evidence",
    "students_and_teachers": "How strong students and their teachers would read the exposition",
}
PREFIX = {"quantum_experts": "QX", "classical_experts": "CX", "formal_methods_readers": "FX",
          "students_and_teachers": "SX"}
# Every panel gets the whole quartic literature: the preprint's cited papers and the
# directly related sources in the quartic annexes, so each can judge weighting
# against the full field and not only its own community.
EXTRA_CATALOG = {
    "quartic-ref-08-quantum-lower-bounds-by-polynomials": ("Beals–Buhrman–Cleve–Mosca–de Wolf, Quantum lower bounds by polynomials (JACM 2001)", "supplied PDF"),
    "quartic-ref-24-all-quantum-adversary-methods-are-equivale": ("Špalek–Szegedy, All quantum adversary methods are equivalent (Theory of Computing 2006)", "journal PDF"),
    "quartic-ref-25-graph-properties-and-circular-functions-ho": ("Sun–Yao, Graph properties and circular functions: how low can quantum query complexity go?", "supplied PDF"),
    "quartic-lit-aaronson-ambainis-bogdanov-quantum-vs-classical": ("Aaronson–Ambainis–Bogdanov–Yeung, On quantum versus classical query complexity", "ECCC TR21-115 rev. 2"),
    "quartic-lit-aaronson-quantum-implications-of-huangs-sensitivity": ("Aaronson–Ben-David–Kothari–Rao–Tal, quantum implications of Huang's sensitivity theorem (LaTeX source)", "arXiv source"),
    "quartic-lit-ambainis-iraids-kokainis-certificate-v3": ("Ambainis–Iraids–Kokainis, certificate complexity separations, later edition", "arXiv v3 source"),
    "quartic-lit-ben-david-a-super-grover-separation": ("Ben-David, A super-Grover separation between randomized and quantum query complexities", "arXiv source"),
    "quartic-lit-bravyi-classical-algorithms-for-forrelation": ("Bravyi–Gosset–Grier–Schaeffer, Classical algorithms for Forrelation", "arXiv source"),
    "quartic-lit-canonne-chen-mestre-quantumly-fast-classically-forrious": ("Canonne–Chen–Mestre, Quantumly fast and classically forrious", "arXiv source"),
    "quartic-lit-girish-fourier-spectrum-of-noisy-quantum-algorithms": ("Girish et al., Fourier spectrum of noisy quantum algorithms", "arXiv source"),
    "quartic-lit-montanaro-quantum-search-with-advice": ("Montanaro, Quantum search with advice (TQC 2010)", "supplied PDF"),
    "quartic-lit-wu-xor-forrelation-stochastic-calculus": ("Wu, XOR lemmas for Forrelation by stochastic calculus", "arXiv source"),
    "quartic-lit-zhang-shao-cyclic-forrelation": ("Zhang–Shao, cyclic Forrelation", "arXiv source"),
}
QUARTIC_LITERATURE = [*base.CATALOG, *EXTRA_CATALOG]
LITERATURE = {job: QUARTIC_LITERATURE for job in JOBS}
CITED_ONLY_BY_JOB = {job: ["yao1977", "nisan1991", "bss2003"] for job in JOBS}
SKILLS = Path(os.environ.get("LEAN_EXPOSITION", ROOT.parent / "lean-exposition")) / "skills"
SKILL_FILES = ("README.md", "long-to-short/SKILL.md", "record-to-expository/SKILL.md")
REQUESTS = ROOT / "research/requests/round6"
PREVIOUS = {
    "previous_round/round5_reviews.md": "research/adjudication/round5_reviews.md",
    "previous_round/round5_statement_fidelity.md": "research/adjudication/round5_statement_fidelity.md",
    "previous_round/round5_statement_fidelity.json": "research/adjudication/round5_statement_fidelity.json",
    "previous_round/round5_record_passage_audit.md": "research/adjudication/round5_record_passage_audit.md",
    **{f"previous_round/dispositions/{d}.json": f"research/adjudication/round5_dispositions/{d}.json"
       for d in ("expert_companion", "exposition", "reasoning_record")},
    **{f"previous_round/verdicts/{r}.md": f"research/returns/round5/members/{r}/verdict.md"
       for r in ("expert_referee_short", "quantum_mechanism", "classical_mechanism", "exposition_for_students",
                 "long_record_navigation_a", "long_record_navigation_b")},
}

base_inputs, base_packet_map = base.inputs, base.packet_map


def inputs(job, **options):
    """Round-five inputs for the drafts, plus round-six context for every panel."""
    root, record_pdf = options["root"], options["record_pdf"]
    files = base_inputs(job, **options)

    def add(member, source, role, label):
        base.check_packets.check_name(member)
        if member.casefold() not in {n.casefold() for n in files}:
            files[member] = (base.safe_source(source), role, label)

    add("reader_principles.md", root / "research/requests/round6/reader_principles.md", "reader_principles",
        "repository:research/requests/round6/reader_principles.md")
    for name in SKILL_FILES:
        add(f"skills/{name}", SKILLS / name, "writing_method", f"lean-exposition:skills/{name}")
    for member, path in PREVIOUS.items():
        add(member, root / path, "previous_round", "repository:" + path)
    for name in base.NAVIGATION_FILES:
        add("repository/" + name, root / name, "record_navigation_source", "repository:" + name)
    closure, _ = base.round4.linked_sources(root, {"repository/docs/reasoning_record.md": (root / "docs/reasoning_record.md", "")})
    for member, (source, _) in closure.items():
        add(member, source, "record_link_target", "repository:" + member.split("/", 1)[1])
    pdf_files, _ = base.round4.pdf_reading_sources(root, {"pdf": str(record_pdf),
                                                          "pdf_sha256": base.digest(Path(record_pdf).read_bytes())})
    for member, (source, _) in pdf_files.items():
        add(member, source, "record_pdf_link_target", "repository:" + member.split("/", 1)[1])
    return files


def packet_map(job, data):
    lines = [base_packet_map(job, data).rstrip("\n"),
             "- Principles from readers of AI-produced mathematics: [reader_principles.md](reader_principles.md).",
             "- The writing method: [skills README](skills/README.md), [record to short paper](skills/long-to-short/SKILL.md), "
             "[record to exposition](skills/record-to-expository/SKILL.md).",
             "- The previous round: [summary](previous_round/round5_reviews.md), "
             "[statement fidelity](previous_round/round5_statement_fidelity.md), "
             "[record passage audit](previous_round/round5_record_passage_audit.md), and the verdicts and per-finding "
             "dispositions under `previous_round/`."]
    return "\n".join(lines) + "\n"


def configure():
    """Point the round-five machinery at the round-six panels."""
    base.CAMPAIGN, base.JOBS, base.PREFIX = CAMPAIGN, JOBS, PREFIX
    base.CATALOG = {**base.CATALOG, **EXTRA_CATALOG}
    base.LITERATURE, base.CITED_ONLY_BY_JOB = LITERATURE, CITED_ONLY_BY_JOB
    base.inputs, base.packet_map = inputs, packet_map


def index_text(audit, status, frozen):
    lines = ["# Quartic round-six critique packets", "",
             "Four expert-emulation panels on the expert companion, exposition and long record. Each panel reads as a "
             "community of cited-literature authors, asks why each part exists and returns a ZIP of located findings; "
             "none rewrites.", "",
             f"Repository commit `{status['repository_commit']}`. Freeze digest `{frozen}`.", ""]
    for row in audit:
        lines.append(f"- [{row['job']}]({row['archive']}): {JOBS[row['job']]} ({row['bytes']} bytes; SHA-256 "
                     f"`{row['sha256']}`; {len(row['literature_present'])} literature sources supplied).")
    lines += ["", "[Batch audit](batch-audit.json). Send each ZIP to a fresh session with no other context.", ""]
    return "\n".join(lines)


def build_batch(jobs, dest, **options):
    dest, root = Path(dest).resolve(), options["root"].resolve()
    if dest == root or root in dest.parents:
        raise ValueError("output must be outside the repository")
    if dest.exists():
        raise FileExistsError("choose a new output folder; never overwrite an earlier batch")
    packets = base.prepare_batch(jobs, **options)
    frozen = base.batch_digest(packets)
    dest.parent.mkdir(parents=True, exist_ok=True)
    audit = []
    with tempfile.TemporaryDirectory(prefix=".quartic-r6-", dir=dest.parent) as staging:
        for job, packet in packets.items():
            path = Path(staging) / f"quartic_r6_{job}.zip"
            base.previous.write_archive(path, packet)
            name, count = base.check_packets.audit(path)
            with zipfile.ZipFile(path) as archive:
                base.check_readme_links(archive.read("READ_ME_FIRST.md").decode(), {n: b"" for n in archive.namelist()})
            audit.append({"job": job, "archive": path.name, "bytes": path.stat().st_size,
                          "sha256": base.digest(path.read_bytes()), "payload_members": count,
                          "request_sha256": packet["manifest"]["request_sha256"],
                          "literature_present": LITERATURE[job], "literature_cited_only": CITED_ONLY_BY_JOB[job],
                          "checker": "passed"})
        if base.batch_digest(base.prepare_batch(jobs, **options)) != frozen:
            raise ValueError("inputs changed during packaging; build again")
        status = json.loads(next(iter(packets.values()))["data"]["SOURCE_STATUS.json"])
        (Path(staging) / "batch-audit.json").write_bytes(base.encoded({
            "schema": "quartic-round6-batch-audit-v1", "status": "passed", "freeze_digest": frozen,
            "jobs": list(jobs), "source_status": status, "archives": audit,
            "built_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}))
        (Path(staging) / "INDEX.md").write_text(index_text(audit, status, frozen), encoding="utf-8")
        dest.mkdir()
        for path in Path(staging).iterdir():
            os.link(path, dest / path.name)
    return [dest / row["archive"] for row in audit]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--annexes", type=Path, required=True)
    parser.add_argument("--paper-annex", type=Path, required=True)
    parser.add_argument("--expert-pdf", type=Path, required=True)
    parser.add_argument("--exposition-pdf", type=Path, required=True)
    parser.add_argument("--record-pdf", type=Path, required=True)
    parser.add_argument("--only", nargs="+", choices=list(JOBS))
    parser.add_argument("--dest", type=Path, help="new output folder outside the repository")
    args = parser.parse_args(argv)
    configure()
    options = dict(root=ROOT, requests_dir=REQUESTS, annexes=args.annexes.resolve(),
                   paper_annex=args.paper_annex.resolve(), expert_pdf=args.expert_pdf.resolve(),
                   exposition_pdf=args.exposition_pdf.resolve(), record_pdf=args.record_pdf.resolve())
    jobs = args.only or list(JOBS)
    try:
        if args.dest:
            for path in build_batch(jobs, args.dest, **options):
                print(f"PASS {path}")
        else:
            packets = base.prepare_batch(jobs, **options)
            print(f"Validated {len(packets)} packet inputs; no ZIPs written. Freeze digest: {base.batch_digest(packets)}")
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"FAIL: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
