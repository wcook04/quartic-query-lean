#!/usr/bin/env python3
"""Run bounded native round-four formal checks for returns 04, 05, 06 and 08, serially.

Outputs are local observations, not automatically registered corpus receipts.
Each negative comparison must fail with its named diagnostic; a compilation
failure is not a rejection. Comparator agreement is statement agreement under
shared definitions, never a semantic-fidelity certificate.
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
    # Return 05
    "QuarticQuery.LowerBound.RealizedCaps", "QuarticQuery.ExternalRandomness",
    "QuarticQuery.MeasurablePolicies", "QuarticQuery.LowerBound.RealizedCapsExternal",
    "QuarticQuery.Paper.RealizedCaps",
    PREFIX + "RealizedCaps.Solution", PREFIX + "RealizedCaps.NegativeCappedPremise",
    # Return 06
    "QuarticQuery.ForrelationLower.RealLeaves", "QuarticQuery.ForrelationLower.RealLeafGrowth",
    "QuarticQuery.ForrelationLower.RealLeafAdvantage", "QuarticQuery.ForrelationLower.RealLeafExplicit",
    PREFIX + "Round4", PREFIX + "Degree.NegativeMissingUniqueness",
    PREFIX + "ModelZero.NegativeClassicalOnly", PREFIX + "RealLeaves.NegativeZeroOnly",
    # Return 04
    "QuarticQuery.Upper.UniformEndpoint", "QuarticQuery.Upper.FinalBScalarPhysical",
    "QuarticQuery.Paper.ConstructionForrelationSharp", "QuarticQuery.Paper.ForrelationTensorSharp",
    PREFIX + "UniformAmplifier.Solution", PREFIX + "DecoderSharp.Solution",
    # Return 08 candidate
    "QuarticQuery.LowerBound.Planted.ZeroSearchSuccessor",
]
AUDITS = ["RealizedCaps/Inspect", "Degree/Inspect", "ModelZero/Inspect", "RealLeaves/Inspect",
          "Round4Inspect/Quantum", "Round4Inspect/ZeroSearch"]
# A specific intended diagnostic is required: compilation failure is not rejection.
COMPARISONS = [
    ("realized-caps-external", "RealizedCaps/comparator.json", 0, None),
    ("realized-caps-capped-premise", "RealizedCaps/negative-capped-premise.json", 1,
     "statement do not match"),
    ("degree-conventions", "Degree/comparator.json", 0, None),
    ("degree-missing-uniqueness", "Degree/negative-missing-uniqueness.json", 1,
     "statement do not match"),
    ("model-zero", "ModelZero/comparator.json", 0, None),
    ("model-zero-classical-only", "ModelZero/negative-classical-only.json", 1,
     "statement do not match"),
    ("real-leaves", "RealLeaves/comparator.json", 0, None),
    ("real-leaves-zero-only", "RealLeaves/negative-zero-only.json", 1,
     "statement do not match"),
    ("uniform-amplifier", "UniformAmplifier/comparator.json", 0, None),
    ("decoder-sharp", "DecoderSharp/comparator.json", 0, None),
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
    parser.add_argument("--only", action="append", help="limit comparisons to these labels")
    args = parser.parse_args()
    project = ROOT / "lean"
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    report = {"schema": "quartic-round4-formal-native-v1", "started_at":
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
            # `set_option pp.universes true` prints `Classical.choice.{u}`; strip universe suffixes.
            axioms = [re.sub(r"\.\{[^}]*\}", "", row)
                      for row in re.findall(r"depends on axioms: \[(.*?)\]", logtext, re.S)]
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
        for module in AUDITS:
            okay = run("audit-" + module.replace("/", "-"),
                       [args.lake, "env", "lean", "QuarticCorpus/Independent/" + module + ".lean"]) and okay
    if okay and args.phase in {"compare", "all"}:
        for label, config, expected, diagnostic in COMPARISONS:
            if args.only and label not in args.only:
                continue
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
