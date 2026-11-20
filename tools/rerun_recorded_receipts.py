#!/usr/bin/env python3
"""Rerun the recorded commands behind the round-three and round-four receipts.

`run_comparator.py` covers the top-level bundles and negative fixtures. The
independent bundles under `lean/QuarticCorpus/Independent/` and their controls
were judged by commands recorded in `comparator-round*` receipts, and the
modules they need were built by `lean-build-round*-targeted` receipts. After any
Lean source change those receipts are stale. This program takes the latest
receipt of each such name, reruns exactly its recorded command (Comparator
sandboxed when QUARTIC_COMPARATOR_SANDBOX=1), and writes a new receipt bound to
the current sources. A rerun passes only when it reproduces the recorded
outcome: the same exit code, and for a negative control the same expected
diagnostic in the log.

A targeted build receipt keeps the recorded declaration list of its earlier
receipt and names that receipt in `declarations_from`; the build itself is
rerun. Use it only when the sources between the two receipts differ in comments
alone (see `corpus/migrations/`).

    QUARTIC_COMPARATOR_SANDBOX=1 python3 tools/rerun_recorded_receipts.py
"""

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
RECEIPTS = ROOT / "corpus" / "receipts"
LAKE = os.environ.get("LAKE", "lake")
SANDBOXED = os.environ.get("QUARTIC_COMPARATOR_SANDBOX") == "1"


def latest():
    chosen = {}
    for path in sorted(RECEIPTS.glob("*.json")):
        receipt = json.loads(path.read_text(encoding="utf-8"))
        name = receipt.get("name", "")
        wanted = ((receipt.get("kind") == "comparator" and name.startswith("round"))
                  or (receipt.get("kind") == "lean_build" and name.startswith("round")
                      and name.endswith("-targeted")))
        if wanted and receipt.get("status") == "passed" and "source_hashes" in receipt:
            if name not in chosen or receipt["ran_at"] > chosen[name][1]["ran_at"]:
                chosen[name] = (path, receipt)
    return [chosen[name] for name in sorted(chosen)]


def rerun(path, old):
    command = list(old["command"])
    if old["kind"] == "comparator" and SANDBOXED:
        command = [part for part in command if part != "--inadvisably-no-sandbox"]
    before = source_hashes(ROOT)
    result = subprocess.run([LAKE, *command[1:]], cwd=LEAN, capture_output=True, text=True)
    log = result.stdout + result.stderr
    unchanged = before == source_hashes(ROOT)
    reproduced = result.returncode == old.get("exit_code", 0)
    if old.get("expected_diagnostic"):
        reproduced = reproduced and old["expected_diagnostic"] in log
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=True,
                            capture_output=True, text=True).stdout.strip()
    ran_at = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    receipt = {key: value for key, value in old.items()
               if key not in {"receipt_file", "receipt_sha256", "log_sha256", "ran_at", "commit",
                              "source_hashes", "source_changed_during_run", "sandboxed", "tool"}}
    receipt.update({
        "status": "passed" if reproduced and unchanged else "failed",
        "commit": commit, "command": command, "exit_code": result.returncode,
        "source_hashes": before, "source_changed_during_run": not unchanged,
        "log_sha256": hashlib.sha256(log.encode("utf-8")).hexdigest(), "ran_at": ran_at,
        "rerun_of": path.name,
    })
    if old["kind"] == "comparator":
        receipt["sandboxed"] = SANDBOXED
        receipt["tool"] = ("lake comparator, sandboxed GitHub Actions rerun of a recorded command"
                           if SANDBOXED else "lake comparator, unsandboxed rerun of a recorded command")
    else:
        receipt["tool"] = "Lake targeted build, rerun of a recorded command"
        receipt["declarations_from"] = path.name
    stamp = ran_at.replace(":", "").replace(".", "")
    prefix = "comparator" if old["kind"] == "comparator" else "lean-build"
    out = RECEIPTS / f"{prefix}-{old['name']}-{stamp}.json"
    out.write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(f"{old['name']}: exit {result.returncode}, {receipt['status']}")
    if receipt["status"] != "passed":
        print(log[-1500:], file=sys.stderr)
    return receipt["status"] == "passed"


def main():
    builds = [item for item in latest() if item[1]["kind"] == "lean_build"]
    comparisons = [item for item in latest() if item[1]["kind"] == "comparator"]
    results = [rerun(path, old) for path, old in builds + comparisons]
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
