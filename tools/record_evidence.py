#!/usr/bin/env python3
"""Record the compiled dependency closure and a build receipt.

Build the `QuarticQuery` target before reading its environment through Reach.lean.
Importing an existing .olean alone cannot establish that current source builds.
Receipts bind the unchanged source/configuration bytes around both operations;
old receipts remain historical rather than being overwritten.
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
CORPUS = ROOT / "corpus"
LAKE = os.environ.get("LAKE", str(Path.home() / ".elan/bin/lake"))
ROOTS = ["QuarticQuery.theorem_1_1_unconditional", "QuarticQuery.cubic_bound_fails_unconditional"]


def main():
    before = source_hashes(ROOT)
    build_command = [LAKE, "build", "QuarticQuery"]
    build = subprocess.run(build_command, cwd=LEAN, capture_output=True, text=True)
    if build.returncode:
        print(build.stdout[-800:] + build.stderr[-800:], file=sys.stderr)
        return 1
    command = [LAKE, "env", "lean", "--run", "scripts/Reach.lean", *ROOTS]
    result = subprocess.run(command, cwd=LEAN, capture_output=True, text=True)
    lines = [line for line in result.stdout.splitlines() if line.startswith('{"')]
    if result.returncode or not lines:
        print(result.stdout[-800:] + result.stderr[-800:], file=sys.stderr)
        return 1
    closure = json.loads(lines[-1])
    if before != source_hashes(ROOT):
        print("Lean inputs changed during build/inspection; no evidence recorded", file=sys.stderr)
        return 1
    missing = set(ROOTS) - set(closure["declared"])
    if missing or closure.get("unresolved_constants"):
        print("Incomplete dependency inspection; no evidence recorded", file=sys.stderr)
        return 1
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=True,
                            capture_output=True, text=True).stdout.strip()
    receipt = {
        "kind": "lean_build", "name": "root", "status": "passed", "commit": commit,
        "toolchain": (LEAN / "lean-toolchain").read_text(encoding="utf-8").strip(),
        "command": ["lake", "build", "QuarticQuery"],
        "inspection_command": ["lake", "env", "lean", "--run", "scripts/Reach.lean", *ROOTS],
        "tool": "Successful Lake target build, then declarations read from its compiled environment",
        "source_hashes": before,
        "log_sha256": hashlib.sha256((build.stdout + build.stderr + result.stdout + result.stderr)
                                     .encode("utf-8")).hexdigest(),
        "declarations": closure["declared"],
        "ran_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
    }
    closure.update(source_hashes=before, ran_at=receipt["ran_at"], commit=commit)
    (CORPUS / "lean_dependencies.json").write_text(
        json.dumps(closure, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    (CORPUS / "receipts").mkdir(exist_ok=True)
    stamp = receipt["ran_at"].replace(":", "").replace(".", "")
    (CORPUS / "receipts" / f"lean-build-root-{stamp}.json").write_text(
        json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(f"{len(closure['reached'])} of {len(closure['declared'])} declarations reached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
