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
import subprocess
import sys

from build_corpus import source_hashes


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
CORPUS = LEAN / "QuarticCorpus"
RECEIPTS = ROOT / "corpus/receipts"
LAKE = os.environ.get("LAKE", str(Path.home() / ".elan/bin/lake"))
DEFERRED = "Child exited with 75"
EXPECTED = {
    "WeakenedConclusion": "statement do not match",
    "SorryProof": "sorryAx",
    "ForeignAxiom": "cheat",
    "MissingDeclaration": "expected_weight_le_half",
    "ChangedDefinition": "IsComparison",
}


def git_head():
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=True,
                          capture_output=True, text=True).stdout.strip()


def compared_declarations(config):
    """Return exactly the configured theorem targets, never proof-text mentions.

    Comparator compares these declarations' types. A theorem mentioned in a
    wrapper proof can be specialized, occur in an unrelated helper, or even be
    mentioned only in a comment. Such text does not establish that the theorem
    itself was compared. Record an implementation alias only through a separate
    reviewed/type-checked correspondence, or compare its own name directly.
    """
    names = json.loads(config.read_text(encoding="utf-8"))["theorem_names"]
    if (not isinstance(names, list)
            or not all(isinstance(name, str) and name.strip() for name in names)
            or len(names) != len(set(names))):
        raise ValueError(f"{config}: theorem_names must be a list of distinct nonempty names")
    return names


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
        "ran_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        **extra,
    }


def write(receipt):
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    stamp = receipt["ran_at"].replace(":", "").replace(".", "")
    path = RECEIPTS / f"comparator-{receipt['name']}-{stamp}.json"
    path.write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")


def run_bundle(config, paranoid):
    name = config.parent.name
    before = source_hashes(ROOT)
    declarations = compared_declarations(config)
    command, code, log = comparator(config, paranoid)
    if code == 75 or DEFERRED in log:
        print(f"{name}: deferred by the shared build lock, nothing judged")
        return False
    unchanged = before == source_hashes(ROOT)
    write(stamp(name, command, "passed" if code == 0 and unchanged else "failed", log,
                {"declarations": declarations, "paranoid": paranoid, "exit_code": code,
                 "declaration_scope": "configured_theorem_names_only",
                 "source_hashes": before, "source_changed_during_run": not unchanged}))
    print(f"{name}: exit {code}")
    if code:
        print(log[-1500:], file=sys.stderr)
    if not unchanged:
        print(f"{name}: inputs changed during comparison; receipt cannot establish current evidence",
              file=sys.stderr)
    return code == 0 and unchanged


def run_negative(config):
    name = config.stem
    before = source_hashes(ROOT)
    command, code, log = comparator(config, False)
    if code == 75 or DEFERRED in log:
        print(f"negative {name}: deferred by the shared build lock, nothing judged")
        return False
    expected = EXPECTED[name]
    unchanged = before == source_hashes(ROOT)
    rejected = code == 1 and expected in log and unchanged
    write(stamp(f"negative-{name}", command, "passed" if rejected else "failed", log,
                {"declarations": [], "expected_diagnostic": expected, "exit_code": code,
                 "source_hashes": before, "source_changed_during_run": not unchanged,
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
