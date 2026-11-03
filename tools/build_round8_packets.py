#!/usr/bin/env python3
"""Build the two round-eight feedback packets, one per short paper.

Round eight reuses the round-five to round-seven packet machinery (hash binding,
link map, leak checks, manifest, independent checker, the whole writing method and
the register measurement). It has two panels: referees of the expert companion and
newcomers and teachers reading the exposition. Each packet still carries all three
documents, so the reader can follow links into the long record, and it carries the
round-seven synthesis, revision notes, audits and verdicts as the previous round.

The record PDF is rendered from the current Markdown, so SOURCE_STATUS.json says so
and no since-PDF diff is attached.

    python3 tools/build_round8_packets.py --annexes ANNEXES --paper-annex PREPRINT \\
        --expert-pdf E.pdf --exposition-pdf X.pdf --record-pdf R.pdf \\
        --lean-exposition LEAN_EXPOSITION_CHECKOUT --dest NEW_FOLDER
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
import build_round6_packets as round6  # noqa: E402
import build_round7_packets as round7  # noqa: E402

base = round7.base
ROOT = base.ROOT
CAMPAIGN = "round8"
JOBS = {
    "expert_paper": "How specialist referees read the expert companion",
    "exposition": "How newcomers and teachers read the exposition",
}
PREFIX = {"expert_paper": "XP", "exposition": "EX"}
LITERATURE = {
    "expert_paper": [
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-ref-04-separations-in-query-complexity-based-on-p",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum", "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
        "quartic-ref-26-towards-optimal-separations-between-quantu", "quartic-ref-12-quantum-amplitude-amplification-and-estima",
        "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error", "quartic-ref-13-improved-direct-product-theorems-for-rando",
        "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i"],
    "exposition": [
        "quartic-lit-dewolf-quantum-computing-lecture-notes", "quartic-lit-buhrman-dewolf-decision-tree-survey",
        "quartic-ref-16-a-fast-quantum-mechanical-algorithm-for-da", "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-lit-bansal-sinha-qip2021-slides",
        "quartic-lit-aaronson-ambainis-bogdanov-quantum-vs-classical"],
}
CITED_ONLY_BY_JOB = {job: ["yao1977", "nisan1991", "bss2003"] for job in JOBS}
REQUESTS = ROOT / "research/requests/round8"
ADJUDICATION = "research/adjudication"
VERDICTS = {
    "quantum_specialists": "research/returns/round7/members/quantum_specialists/verdict.md",
    "newcomer_readers": "research/returns/round7/members/newcomer_readers/verdict.md",
    "editors_and_funnel": "research/returns/round7/members/editors_and_funnel/verdict.md",
    "lower_bound_specialists":
        "research/returns/round7/members/lower_bound_specialists/quartic_r7_lower_bound_specialists_return/verdict.md",
}
PREVIOUS = {
    **{f"previous_round/{name}": f"{ADJUDICATION}/{name}" for name in (
        "round7_synthesis.json", "round7_expert_revision.md", "round7_exposition_revision.md",
        "round7_record_revision.md", "round7_classical_audit.md", "round7_quantum_audit.md",
        "round7_cold_read.md", "round7_record_fidelity.md", "round6_statement_fidelity.md")},
    **{f"previous_round/verdicts/{panel}.md": path for panel, path in VERDICTS.items()},
}


def source_status(root, data, record_pdf):
    """The base status, corrected for a record PDF rendered from the current Markdown."""
    status, _ = original_source_status(root, data, record_pdf)
    record = status["record"]
    for key in ("pdf_rendered_from", "since_pdf_diff", "changed_lines"):
        record.pop(key, None)
    record["pdf_rendered_from"] = f"the current Markdown at repository commit {status['repository_commit']}"
    status["acceptance_gate"] = ("not applied: these hashes bind the packet to the exact bytes supplied; "
                                 "no human review of these editions is claimed.")
    return status, None


original_source_status = base.source_status


def packet_map(job, data):
    skills = ", ".join(f"[{name}](skills/{name})" for name in round7.SKILL_FILES)
    lines = [round6.base_packet_map(job, data).rstrip("\n"),
             "- Principles from readers of AI-produced mathematics: [reader_principles.md](reader_principles.md).",
             f"- The writing method: {skills}, and [the register stage](skills/register-stage.md).",
             "- The register stage for this round: [rules](register/REGISTER_RULES.md), "
             "[draft measurement](register/measurement.txt), [literature profile](register/profile.json).",
             "- The previous round: [cross-panel synthesis](previous_round/round7_synthesis.json), revision notes for "
             "[the expert companion](previous_round/round7_expert_revision.md), "
             "[the exposition](previous_round/round7_exposition_revision.md) and "
             "[the record](previous_round/round7_record_revision.md), the "
             "[classical](previous_round/round7_classical_audit.md) and "
             "[quantum](previous_round/round7_quantum_audit.md) audits, an "
             "[independent cold read](previous_round/round7_cold_read.md), "
             "[record fidelity](previous_round/round7_record_fidelity.md), "
             "[statement fidelity](previous_round/round6_statement_fidelity.md), and the four panel verdicts under "
             "`previous_round/verdicts/`."]
    return "\n".join(lines) + "\n"


def configure(lean_exposition=None):
    """Point the round-seven machinery at the two round-eight panels."""
    round7.configure(lean_exposition)
    round6.PREVIOUS = PREVIOUS
    base.CAMPAIGN, base.JOBS, base.PREFIX = CAMPAIGN, JOBS, PREFIX
    base.LITERATURE, base.CITED_ONLY_BY_JOB = LITERATURE, CITED_ONLY_BY_JOB
    base.packet_map = packet_map
    base.source_status = source_status
    round7.LITERATURE, round7.CITED_ONLY_BY_JOB, round7.JOBS = LITERATURE, CITED_ONLY_BY_JOB, JOBS


def index_text(audit, status, frozen):
    lines = ["# Quartic round-eight feedback packets", "",
             "Two feedback packets, one per short paper: specialist referees of the expert companion, and newcomers "
             "and teachers reading the exposition. Each panel gives comprehensive complaints and advice, reads a "
             "sample of the literature and searches online beyond it, and judges the general writing method as well "
             "as this instance; none rewrites.", "",
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
    with tempfile.TemporaryDirectory(prefix=".quartic-r8-", dir=dest.parent) as staging:
        for job, packet in packets.items():
            path = Path(staging) / f"quartic_r8_{job}.zip"
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
            "schema": "quartic-round8-batch-audit-v1", "status": "passed", "freeze_digest": frozen,
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
    parser.add_argument("--lean-exposition", type=Path, help="lean-exposition checkout or export carrying the method")
    parser.add_argument("--only", nargs="+", choices=list(JOBS))
    parser.add_argument("--dest", type=Path, help="new output folder outside the repository")
    args = parser.parse_args(argv)
    options = dict(root=ROOT, requests_dir=REQUESTS, annexes=args.annexes.resolve(),
                   paper_annex=args.paper_annex.resolve(), expert_pdf=args.expert_pdf.resolve(),
                   exposition_pdf=args.exposition_pdf.resolve(), record_pdf=args.record_pdf.resolve())
    jobs = args.only or list(JOBS)
    try:
        with tempfile.TemporaryDirectory(prefix="quartic-r8-register-") as work:
            configure(args.lean_exposition)
            round7.state["register"] = round7.build_register(round7.state["lean_exposition"], options["annexes"],
                                                             Path(work))
            if args.dest:
                for path in build_batch(jobs, args.dest, **options):
                    print(f"PASS {path}")
            else:
                packets = base.prepare_batch(jobs, **options)
                print(f"Validated {len(packets)} packet inputs; no ZIPs written. "
                      f"Freeze digest: {base.batch_digest(packets)}")
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"FAIL: {error}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
