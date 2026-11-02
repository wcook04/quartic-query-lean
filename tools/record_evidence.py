#!/usr/bin/env python3
"""Record the compiled dependency closure and a build receipt.

Reads the built environment through lean/scripts/Reach.lean, so a declaration
counts as built only if it is in the compiled environment at this commit, and as
reached only if the headline's proof actually depends on it. Run after a
successful guarded build of the `QuarticQuery` target.
"""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
CORPUS = ROOT / "corpus"
LAKE = os.environ.get("LAKE", str(Path.home() / ".elan/bin/lake"))
ROOTS = ["QuarticQuery.theorem_1_1", "QuarticQuery.cubic_bound_fails_of_bansalSinha"]


def main():
    command = [LAKE, "env", "lean", "--run", "scripts/Reach.lean", *ROOTS]
    result = subprocess.run(command, cwd=LEAN, capture_output=True, text=True)
    lines = [line for line in result.stdout.splitlines() if line.startswith('{"')]
    if result.returncode or not lines:
        print(result.stdout[-800:] + result.stderr[-800:], file=sys.stderr)
        return 1
    closure = json.loads(lines[-1])
    (CORPUS / "lean_dependencies.json").write_text(
        json.dumps(closure, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=True,
                            capture_output=True, text=True).stdout.strip()
    receipt = {
        "kind": "lean_build", "name": "root", "status": "passed", "commit": commit,
        "toolchain": (LEAN / "lean-toolchain").read_text(encoding="utf-8").strip(),
        "command": ["lake", "env", "lean", "--run", "scripts/Reach.lean", *ROOTS],
        "tool": "Declarations read from the compiled environment",
        "declarations": closure["declared"],
        "ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    (CORPUS / "receipts").mkdir(exist_ok=True)
    (CORPUS / "receipts/lean-build-root.json").write_text(
        json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(f"{len(closure['reached'])} of {len(closure['declared'])} declarations reached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
