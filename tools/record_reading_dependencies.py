#!/usr/bin/env python3
"""Record typed Lean dependencies from a built, source-identical Quartic checkout."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from build_corpus import canonical_sha256, source_hashes

ROOT = Path(__file__).resolve().parents[1]
INSPECTOR = ROOT / "tools/ReadDependencies.lean"
OUTPUT = ROOT / "corpus/reading_dependencies.json"


def write_graph(payload, destination):
    # One record per line makes a changed declaration visible in a Git diff.
    header = {k: v for k, v in payload.items() if k != "nodes"}
    with tempfile.NamedTemporaryFile(mode="w", dir=destination.parent, delete=False) as tmp:
        tmp.write(json.dumps(header, sort_keys=True)[:-1] + ', "nodes": {\n')
        for i, (name, node) in enumerate(sorted(payload["nodes"].items())):
            if i:
                tmp.write(",\n")
            tmp.write(json.dumps(name) + ":" + json.dumps(node, sort_keys=True, separators=(",", ":")))
        tmp.write("\n}}\n")
    output = Path(tmp.name)
    output.chmod(0o644)
    output.replace(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=ROOT,
                        help="checkout with the same Lean sources and its own Lake cache")
    args = parser.parse_args()
    root = args.checkout.resolve()
    before = source_hashes(root)
    inspector = INSPECTOR.read_bytes()
    if before != source_hashes(ROOT):
        parser.error("build checkout differs from edition's Lean sources")
    subprocess.run(["lake", "build", "QuarticQuery"], cwd=root / "lean", check=True)
    raw = subprocess.check_output(["lake", "env", "lean", "--run", str(INSPECTOR)], cwd=root / "lean")
    inspection = json.loads(raw)
    nodes = inspection["nodes"]
    if not nodes or source_hashes(root) != before or source_hashes(ROOT) != before or inspector != INSPECTOR.read_bytes():
        parser.error("empty inspection or inputs changed during recording")
    payload = {"schema": "quartic-reading-dependencies-v1", "module": "QuarticQuery",
               "source_snapshot_sha256": canonical_sha256(before),
               "inspector_sha256": hashlib.sha256(inspector).hexdigest(),
               "toolchain": (root / "lean/lean-toolchain").read_text().strip(),
               **inspection}
    write_graph(payload, OUTPUT)
    print(f"Recorded {len(nodes)} declarations in {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
