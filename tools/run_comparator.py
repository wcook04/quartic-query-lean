#!/usr/bin/env python3
"""Run Comparator on each bundle and negative fixture and record what happened.

A positive bundle must be accepted. A negative fixture must be rejected with the
diagnostic listed in EXPECTED; a rejection for another reason, such as a broken
build, fails the run. A build deferred by the shared lock judged nothing, so it
writes no receipt. Results go to corpus/receipts/, which tools/build_corpus.py
reads. On this machine runs are unsandboxed, and receipts say so: the sandbox
protects a judge from hostile code, and here the code is our own.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
CORPUS = LEAN / "QuarticCorpus"
RECEIPTS = ROOT / "corpus/receipts"
LAKE = os.environ.get("LAKE", str(Path.home() / ".elan/bin/lake"))
DEFERRED = "Child exited with 75"
EXPECTED = {
    "WeakenedConclusion": "does not match",
    "SorryProof": "sorryAx",
    "ForeignAxiom": "cheat",
    "MissingDeclaration": "expected_weight_le_half",
    "ChangedDefinition": "IsComparison",
}


def git_head():
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=True,
                          capture_output=True, text=True).stdout.strip()


def wrapped(config):
    """Return the checked theorems and the proved theorems they restate."""
    names = json.loads(config.read_text(encoding="utf-8"))["theorem_names"]
    solution = (config.parent / "Solution.lean").read_text(encoding="utf-8")
    return names + re.findall(r"^\s*exact (QuarticQuery\.\S+)", solution, re.M)


def comparator(config, paranoid):
    command = [LAKE, "comparator", "--config", str(config.relative_to(LEAN)),
               "--inadvisably-no-sandbox"] + (["--paranoid"] if paranoid else [])
    result = subprocess.run(command, cwd=LEAN, capture_output=True, text=True)
    return command, result.returncode, result.stdout + result.stderr


def stamp(name, command, status, log, extra):
    return {
        "kind": "comparator",
        "name": name,
        "status": status,
        "commit": git_head(),
        "toolchain": (LEAN / "lean-toolchain").read_text(encoding="utf-8").strip(),
        "sandboxed": False,
        "command": ["lake", *command[1:]],
        "tool": "lake comparator, unsandboxed local run",
        "log_sha256": hashlib.sha256(log.encode("utf-8")).hexdigest(),
        "ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        **extra,
    }


def write(receipt):
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    path = RECEIPTS / f"comparator-{receipt['name']}.json"
    path.write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")


def run_bundle(config, paranoid):
    name = config.parent.name
    command, code, log = comparator(config, paranoid)
    if DEFERRED in log:
        print(f"{name}: deferred by the shared build lock, nothing judged")
        return False
    write(stamp(name, command, "passed" if code == 0 else "failed", log,
                {"declarations": wrapped(config), "paranoid": paranoid, "exit_code": code}))
    print(f"{name}: exit {code}")
    if code:
        print(log[-1500:], file=sys.stderr)
    return code == 0


def run_negative(config):
    name = config.stem
    command, code, log = comparator(config, False)
    if DEFERRED in log:
        print(f"negative {name}: deferred by the shared build lock, nothing judged")
        return False
    expected = EXPECTED[name]
    rejected = code == 1 and expected in log
    write(stamp(f"negative-{name}", command, "passed" if rejected else "failed", log,
                {"declarations": [], "expected_diagnostic": expected, "exit_code": code,
                 "negative_control": "rejected_as_expected" if rejected else "wrong_failure"}))
    print(f"negative {name}: exit {code}, {'rejected as expected' if rejected else 'WRONG FAILURE'}")
    if not rejected:
        print(log[-1500:], file=sys.stderr)
    return rejected


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--paranoid", action="store_true",
                        help="also run every external checker bundled with Lean")
    parser.add_argument("--only", help="run one bundle or negative fixture by name")
    args = parser.parse_args()
    results = []
    for config in sorted(CORPUS.glob("*/comparator.json")):
        if not args.only or args.only == config.parent.name:
            results.append(run_bundle(config, args.paranoid))
    for config in sorted((CORPUS / "Negative").glob("*.json")):
        if not args.only or args.only == config.stem:
            results.append(run_negative(config))
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
