#!/usr/bin/env python3
"""Register a passed native rerun's operations as fresh corpus receipts.

A rerun of tools/return_checks/round3_formal.py (or round4_formal.py) writes a
run.json of local observations. This copies each operation into corpus/receipts/
using the latest earlier receipt of the same name as the template for its fixed
fields (tool, scope, control semantics), and replaces everything the new run
determines: commit, source hashes, log digest, exit code and time. Positive
comparisons list exactly their configured theorem names. Nothing is registered
unless the whole run passed on one unchanged source inventory that still equals
the current tree.

    python3 tools/return_checks/register_rerun.py --run DIR/run.json --prefix round3
"""

import argparse
from datetime import datetime
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from build_corpus import source_hashes  # noqa: E402
from run_comparator import compared_declarations  # noqa: E402

RECEIPTS = ROOT / "corpus/receipts"


def template(name):
    """The latest receipt registered under `name`, or None."""
    paths = sorted(RECEIPTS.glob(f"{name}-2*.json"))
    return json.loads(paths[-1].read_text(encoding="utf-8")) if paths else None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--prefix", required=True, help="receipt name prefix, e.g. round3")
    args = parser.parse_args()
    run = json.loads(args.run.read_text(encoding="utf-8"))
    hashes = source_hashes(ROOT)
    if (run.get("status") != "passed" or not run.get("source_inputs_unchanged")
            or run["source_hashes"] != hashes):
        raise SystemExit("run did not pass on the current source inventory; nothing registered")
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=True,
                            capture_output=True, text=True).stdout.strip()
    toolchain = (ROOT / "lean/lean-toolchain").read_text(encoding="utf-8").strip()
    started = datetime.fromisoformat(run["started_at"])
    stamp = started.isoformat(timespec="microseconds").replace(":", "").replace(".", "")
    written = []
    for operation in run["operations"]:
        label = operation["label"]
        if label.startswith("audit-"):
            continue  # recorded on the targeted-build receipt as inspection commands
        kind = "lean_build" if label == "targeted-build" else "comparator"
        name = f"{args.prefix}-targeted" if kind == "lean_build" else f"{args.prefix}-{label}"
        base = template(("lean-build-" if kind == "lean_build" else "comparator-") + name)
        if base is None:
            raise SystemExit(f"no earlier receipt to take fixed fields from: {name}")
        receipt = {**base, "status": operation["status"], "commit": commit, "toolchain": toolchain,
                   "source_hashes": hashes, "source_changed_during_run": False,
                   "ran_at": operation["started_at"], "exit_code": operation["exit_code"],
                   "log_sha256": operation["log_sha256"],
                   "command": ["lake", *operation["command"][1:]]}
        if kind == "lean_build":
            receipt.pop("exit_code")
        elif operation["expected_exit"] == 0 and not base.get("negative_control"):
            config = ROOT / "lean" / operation["command"][operation["command"].index("--config") + 1]
            receipt["declarations"] = compared_declarations(config)
            receipt["declaration_scope"] = "configured_theorem_names_only"
        path = RECEIPTS / f"{'lean-build' if kind == 'lean_build' else 'comparator'}-{name}-{stamp}.json"
        path.write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
        written.append(path.name)
    print("\n".join(written))


if __name__ == "__main__":
    main()
