#!/usr/bin/env python3
"""Build the four round-seven feedback packets.

Round seven reuses the round-five and round-six packet machinery (hash binding,
link map, leak checks, manifest and independent checker) with four feedback
panels that ask for comprehensive complaints and advice on all three stages of
the funnel. Each panel receives a sample of the literature chosen for it and is
asked to search online beyond it. Every packet carries the whole writing method:
the lean-exposition skills, the register stage with its rules, a profile of the
quartic literature and a measurement of each draft, the reader principles and
the round-six dispositions, plans and fidelity review.

    python3 tools/build_round7_packets.py --annexes ANNEXES --paper-annex PREPRINT \\
        --expert-pdf E.pdf --exposition-pdf X.pdf --record-pdf R.pdf \\
        --lean-exposition LEAN_EXPOSITION_CHECKOUT --dest NEW_FOLDER
"""

import argparse
import datetime
import json
import os
import re
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_round6_packets as round6  # noqa: E402

base = round6.base
ROOT = base.ROOT
CAMPAIGN = "round7"
JOBS = {
    "newcomer_readers": "How readers new to query complexity read the three documents",
    "quantum_specialists": "How the quantum-algorithms community reads the three documents",
    "lower_bound_specialists": "How the randomized lower-bound and separations community reads the three documents",
    "editors_and_funnel": "How editors and referees read the prose and follow the funnel",
}
PREFIX = {"newcomer_readers": "NR", "quantum_specialists": "QS", "lower_bound_specialists": "LS",
          "editors_and_funnel": "EF"}
# A sample per panel; each request asks the panel to search online beyond it.
LITERATURE = {
    "newcomer_readers": [
        "quartic-lit-dewolf-quantum-computing-lecture-notes", "quartic-lit-buhrman-dewolf-decision-tree-survey",
        "quartic-ref-16-a-fast-quantum-mechanical-algorithm-for-da", "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-lit-bansal-sinha-qip2021-slides",
        "quartic-ref-23-an-optimal-separation-of-randomized-and-qu"],
    "quantum_specialists": [
        "quartic-ref-12-quantum-amplitude-amplification-and-estima", "quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu",
        "quartic-ref-18-randomized-and-quantum-query-complexities", "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum", "quartic-ref-05-near-optimal-separations-of-certificate-co",
        "quartic-ref-09-randomized-query-complexity-can-beat-certi", "quartic-lit-ben-david-a-super-grover-separation"],
    "lower_bound_specialists": [
        "quartic-ref-13-improved-direct-product-theorems-for-rando", "quartic-ref-22-towards-proving-strong-direct-product-theo",
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-ref-04-separations-in-query-complexity-based-on-p",
        "quartic-ref-23-an-optimal-separation-of-randomized-and-qu", "quartic-ref-26-towards-optimal-separations-between-quantu",
        "quartic-lit-girish-forrelation-is-extremally-hard", "quartic-ref-09-randomized-query-complexity-can-beat-certi"],
    "editors_and_funnel": [
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-ref-06-k-forrelation-optimally-separates-quantum",
        "quartic-ref-23-an-optimal-separation-of-randomized-and-qu", "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i",
        "quartic-ref-05-near-optimal-separations-of-certificate-co", "quartic-lit-dewolf-quantum-computing-lecture-notes",
        "quartic-lit-aaronson-ambainis-bogdanov-quantum-vs-classical"],
}
CITED_ONLY_BY_JOB = {job: ["yao1977", "nisan1991", "bss2003"] for job in JOBS}
REQUESTS = ROOT / "research/requests/round7"
SKILL_FILES = ("README.md", "source-to-graph/SKILL.md", "graph-to-long/SKILL.md", "long-to-short/SKILL.md",
               "record-to-expository/SKILL.md", "register/SKILL.md")
METHOD_DOCS = ("docs/register-stage.md",)
REGISTER_FILES = ("REGISTER_RULES.md", "register_rules.json", "profile.json", "measurement.json", "measurement.txt")
ADJUDICATION = "research/adjudication"
PREVIOUS = {
    "previous_round/round6_statement_fidelity.md": f"{ADJUDICATION}/round6_statement_fidelity.md",
    "previous_round/round6_literature_register.md": f"{ADJUDICATION}/round6_literature_register.md",
    "previous_round/round6_record_passage_audit.md": f"{ADJUDICATION}/round6_record_passage_audit.md",
    **{f"previous_round/dispositions/{d}.json": f"{ADJUDICATION}/round6_dispositions/{d}.json"
       for d in ("expert_companion", "exposition", "reasoning_record")},
    **{f"previous_round/plans/{p}.md": f"{ADJUDICATION}/round6_plans/{p}.md"
       for p in ("expert_companion", "exposition", "reasoning_record")},
    **{f"previous_round/verdicts/{r}.md": f"research/returns/round6/members/{r}/verdict.md"
       for r in ("quantum_experts", "classical_experts", "formal_methods_readers")},
    "previous_round/verdicts/students_and_teachers.md":
        "research/returns/round6/members/students_and_teachers/quartic_r6_students_and_teachers_return/verdict.md",
}
DRAFT_STAGES = {"short": "docs/expert_companion.md", "expository": "docs/exposition.md",
                "long": "docs/reasoning_record.md"}

state = {"lean_exposition": None, "register": None}


def sanitize_register(data, measurements, patterns, referenced_ids=()):
    """Remove private evidence records without dropping their parent rules.

    Core rule text and identity must survive byte-for-byte. If a private marker
    occurs there, stop rather than rewriting the rule or silently exporting it.
    Other nested structures retain the conservative round-five behavior.
    """
    def named(value):
        return any(p.search(json.dumps(value, ensure_ascii=False)) for p in patterns)

    def clean(value):
        if isinstance(value, list):
            return [clean(v) for v in value if not (
                isinstance(v, dict) and any(named(item) for item in v.values()
                                            if isinstance(item, str)))]
        if isinstance(value, dict):
            return {k: clean(v) for k, v in value.items()}
        if isinstance(value, str):
            for pattern in patterns:
                value = pattern.sub("a cited author", value)
        return value

    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        raise ValueError("register rules inventory is missing or empty")
    ids = [r.get("id") for r in rules]
    if any(not isinstance(rid, str) or not rid for rid in ids) or len(ids) != len(set(ids)):
        raise ValueError("register rule IDs must be nonempty and unique")
    core = ("id", "title", "rule", "limit", "status", "scopes", "failure", "detector", "probe")
    result = {k: clean(v) for k, v in data.items() if k != "rules"}
    result["rules"] = []
    for rule in rules:
        for key in core:
            if key in rule and named(rule[key]):
                raise ValueError(f"private marker in core register rule field: {rule['id']} / {key}")
        exported = {k: clean(v) for k, v in rule.items()
                    if not (k == "example" and named(v))}
        if any(exported.get(k) != rule.get(k) for k in core):
            raise ValueError(f"core register rule changed: {rule['id']}")
        result["rules"].append(exported)
    if [r["id"] for r in result["rules"]] != ids:
        raise ValueError("register rule inventory changed")
    for measurement in measurements:
        for feature, row in measurement.get("features", {}).items():
            unresolved = set(row.get("rules", [])) - set(ids)
            if unresolved:
                raise ValueError(f"unresolved register rule references in {feature}: {sorted(unresolved)}")
    unresolved = set(referenced_ids) - set(ids)
    if unresolved:
        raise ValueError(f"unresolved writing-method rule references: {sorted(unresolved)}")
    if named(result):
        raise ValueError("private marker remains in register export")
    result["export_note"] = ("Private-reader specimens, examples, instances and history records may be omitted; "
                             "rule identities and core text are retained.")
    return result


def build_register(lean_exposition, annexes, out, title="Round seven: writing"):
    """Run the lean-exposition register stage on the frozen drafts against the quartic literature."""
    sys.path.insert(0, str(Path(lean_exposition) / "src"))
    from lean_exposition import register  # noqa: E402
    literature = sorted(str(annexes / slug / "extracted.md") for slug in base.CATALOG
                        if (annexes / slug / "extracted.md").is_file())
    drafts = {stage: str(ROOT / path) for stage, path in DRAFT_STAGES.items()}
    register.build_packet_inputs(drafts, literature, str(out), title, job="")
    rules_path = out / "register/register_rules.json"
    data = json.loads(rules_path.read_text(encoding="utf-8"))
    measurements = json.loads((out / "register/measurement.json").read_text(encoding="utf-8"))
    method_paths = [Path(lean_exposition) / "skills" / name for name in SKILL_FILES]
    method_paths += [Path(lean_exposition) / name for name in METHOD_DOCS]
    references = set()
    method_paths.append(out / "register/measurement.txt")
    for path in method_paths:
        references.update(re.findall(r"\bRG-\d+\b", path.read_text(encoding="utf-8")))
    data = sanitize_register(data, measurements, base.reader_leak_patterns(), references)
    register.validate_rules(data)
    relevant = [r for r in data["rules"] if any(s in r["scopes"] for s in drafts)]
    rules_path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    rendered = register.render_rules(relevant, "Register rules for these drafts")
    rendered += "\nPrivate-reader specimens, examples, instances and history records may be omitted; rule text is retained.\n"
    (out / "register/REGISTER_RULES.md").write_text(rendered, encoding="utf-8")
    return out / "register"


def inputs(job, **options):
    """Round-six inputs, then the whole writing method and the register measurement."""
    files = round6.inputs(job, **options)

    def add(member, source, role, label):
        base.check_packets.check_name(member)
        if member.casefold() not in {n.casefold() for n in files}:
            files[member] = (base.safe_source(source), role, label)

    lean_exposition = Path(state["lean_exposition"])
    for name in METHOD_DOCS:
        add(f"skills/{Path(name).name}", lean_exposition / name, "writing_method", f"lean-exposition:{name}")
    for name in REGISTER_FILES:
        add(f"register/{name}", Path(state["register"]) / name, "register_stage", f"generated:register/{name}")
    return files


def packet_map(job, data):
    skills = ", ".join(f"[{name}](skills/{name})" for name in SKILL_FILES)
    lines = [round6.base_packet_map(job, data).rstrip("\n"),
             "- Principles from readers of AI-produced mathematics: [reader_principles.md](reader_principles.md).",
             f"- The writing method: {skills}, and [the register stage](skills/register-stage.md).",
             "- The register stage for this round: [rules](register/REGISTER_RULES.md), "
             "[draft measurement](register/measurement.txt), [literature profile](register/profile.json).",
             "- The previous round: [statement fidelity](previous_round/round6_statement_fidelity.md), "
             "[literature register](previous_round/round6_literature_register.md), "
             "[record passage audit](previous_round/round6_record_passage_audit.md), and the plans, verdicts and "
             "per-finding dispositions under `previous_round/`."]
    return "\n".join(lines) + "\n"


def configure(lean_exposition=None, register_dir=None):
    """Point the round-five and round-six machinery at the round-seven panels."""
    round6.configure()
    round6.SKILLS = Path(lean_exposition or os.environ.get("LEAN_EXPOSITION", ROOT.parent / "lean-exposition")) / "skills"
    round6.SKILL_FILES, round6.PREVIOUS = SKILL_FILES, PREVIOUS
    base.CAMPAIGN, base.JOBS, base.PREFIX = CAMPAIGN, JOBS, PREFIX
    base.LITERATURE, base.CITED_ONLY_BY_JOB = LITERATURE, CITED_ONLY_BY_JOB
    base.inputs, base.packet_map = inputs, packet_map
    state["lean_exposition"] = round6.SKILLS.parent
    state["register"] = register_dir


def index_text(audit, status, frozen):
    lines = ["# Quartic round-seven feedback packets", "",
             "Four feedback panels on the long record, the expert companion and the exposition. Each panel gives "
             "comprehensive complaints and advice, reads a sample of the literature and searches online beyond it, "
             "and judges the general writing method as well as this instance; none rewrites.", "",
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
    with tempfile.TemporaryDirectory(prefix=".quartic-r7-", dir=dest.parent) as staging:
        for job, packet in packets.items():
            path = Path(staging) / f"quartic_r7_{job}.zip"
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
            "schema": "quartic-round7-batch-audit-v1", "status": "passed", "freeze_digest": frozen,
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
        with tempfile.TemporaryDirectory(prefix="quartic-r7-register-") as work:
            configure(args.lean_exposition)
            state["register"] = build_register(state["lean_exposition"], options["annexes"], Path(work))
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
