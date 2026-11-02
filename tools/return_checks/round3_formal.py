#!/usr/bin/env python3
"""Run bounded native round-three Eq19 and semantic checks, serially.

Outputs are local observations, not automatically registered corpus receipts.
The shared-bad-spec acceptance is an expected demonstration of Comparator's
semantic blind spot; it is never a semantic correctness certificate.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
import re
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from build_corpus import source_hashes

PREFIX = "QuarticCorpus.Independent."
TARGETS = [
    "QuarticQuery.Paper.Eq19Complete", "QuarticQuery.Paper.Eq19Whole",
    "QuarticQuery.Paper.ConstructionFull",
    PREFIX + "Eq19.Spec", PREFIX + "Eq19.PathControls", PREFIX + "Eq19.Bridge",
    PREFIX + "Eq19.Solution", PREFIX + "Eq19.WholeSolution",
    PREFIX + "Semantics", PREFIX + "SemanticMutations",
    PREFIX + "Controls.SharedSolution", PREFIX + "Controls.SharedAudit",
]
# A specific intended diagnostic is required: compilation failure is not rejection.
COMPARISONS = [
    ("construction-support", "ConstructionFull/comparator.json", 0, None),
    ("eq19-independent", "Eq19/comparator.json", 0, None),
    ("eq19-direct", "Eq19/whole-comparator.json", 0, None),
    ("eq19-missing-equality", "Eq19/negative-inequality-only.json", 1,
     "statement do not match"),
    ("threshold-mutation", "Controls/threshold_mutation.json", 1,
     "Const does not match between challenge and target 'Round3.ThresholdSpec.Eligible'"),
    ("shared-bad-spec-blindness", "Controls/shared_blind_spot.json", 0, None),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--phase", choices=("build", "audit", "compare", "all"), default="all")
    parser.add_argument("--lake", default="lake")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--reserve-gib", type=float, default=8)
    args = parser.parse_args()
    project = ROOT / "lean"
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    report = {"schema": "quartic-round3-formal-native-v1", "started_at":
              datetime.now(timezone.utc).isoformat(), "project": str(project),
              "runner_sha256": digest(Path(__file__)), "phase": args.phase,
              "reserve_bytes": int(args.reserve_gib * 1024**3), "operations": [],
              "source_hashes": source_hashes(ROOT),
              "source_hash_owner_sha256": digest(ROOT / "tools/build_corpus.py"),
              "scope": "Targeted local native runs; no global build or human semantic review.",
              "comparator_sandboxed": False}

    def save():
        temporary = output / "run.json.tmp"
        temporary.write_text(json.dumps(report, indent=2) + "\n")
        temporary.replace(output / "run.json")

    def run(label, argv, expected=0, diagnostic=None):
        before = source_hashes(ROOT)
        logpath = output / (label + ".log")
        record = {"label": label, "command": argv, "expected_exit": expected,
                  "expected_diagnostic": diagnostic, "log": str(logpath),
                  "started_at": datetime.now(timezone.utc).isoformat()}
        report["operations"].append(record)
        free = shutil.disk_usage(project).free
        record["free_bytes_before"] = free
        if free < report["reserve_bytes"]:
            record["status"] = "blocked_disk_reserve"
            save()
            return False
        start = time.monotonic()
        with logpath.open("w") as log:
            proc = subprocess.Popen(argv, cwd=project, stdout=log, stderr=subprocess.STDOUT,
                                    start_new_session=True)
            while proc.poll() is None:
                if (time.monotonic() - start > args.timeout or
                        shutil.disk_usage(project).free < report["reserve_bytes"]):
                    record["stop_reason"] = "timeout_or_disk_reserve"
                    os.killpg(proc.pid, signal.SIGTERM)
                    try:
                        proc.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        os.killpg(proc.pid, signal.SIGKILL)
                        proc.wait()
                    break
                time.sleep(0.5)
        logtext = logpath.read_text()
        record.update(exit_code=proc.returncode, seconds=round(time.monotonic() - start, 2),
                      log_sha256=digest(logpath), source_inputs_unchanged=before == source_hashes(ROOT),
                      free_bytes_after=shutil.disk_usage(project).free)
        if label.startswith("audit-") and proc.returncode == 0:
            allowed = {"propext", "Quot.sound", "Classical.choice"}
            axioms = re.findall(r"depends on axioms: \[(.*?)\]", logtext, re.S)
            record["axiom_sets"] = [sorted(set(re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", row))) for row in axioms]
            record["axiom_policy_passed"] = bool(axioms) and all(set(row) <= allowed for row in record["axiom_sets"])
        passed = (record.get("axiom_policy_passed", True) and proc.returncode == expected and "stop_reason" not in record and
                  record["source_inputs_unchanged"] and
                  (not diagnostic or diagnostic in logtext))
        record["status"] = "passed" if passed else "failed"
        if not passed:
            record["diagnostic_tail"] = logtext[-8000:]
        save()
        print(label + ": " + record["status"], flush=True)
        return passed

    okay = True
    if args.phase in {"build", "all"}:
        okay = run("targeted-build", [args.lake, "build", *[t + ":olean" for t in TARGETS]])
    if okay and args.phase in {"audit", "all"}:
        for module in ["Eq19/Audit", "Inspect"]:
            okay = run("audit-" + module.replace("/", "-"),
                       [args.lake, "env", "lean", "QuarticCorpus/Independent/" + module + ".lean"]) and okay
    if okay and args.phase in {"compare", "all"}:
        for label, config, expected, diagnostic in COMPARISONS:
            okay = run(label, [args.lake, "comparator", "--config",
                              "QuarticCorpus/Independent/" + config,
                              "--inadvisably-no-sandbox"], expected, diagnostic) and okay
    report["source_inputs_unchanged"] = report["source_hashes"] == source_hashes(ROOT)
    report["runner_unchanged"] = report["runner_sha256"] == digest(Path(__file__))
    report["source_hash_owner_unchanged"] = report["source_hash_owner_sha256"] == digest(ROOT / "tools/build_corpus.py")
    okay = okay and report["source_inputs_unchanged"] and report["runner_unchanged"] and report["source_hash_owner_unchanged"]
    report["status"] = "passed" if okay else "failed_or_incomplete"
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    save()
    return 0 if okay else 1


if __name__ == "__main__":
    raise SystemExit(main())
