"""Read-only checks on an extracted original input archive.

Usage: python -I check_packet_integrity.py /path/to/input/extraction
Output is written beside this script, never into the supplied input.
This checks bytes and specific source/graph observations, not Lean validity.
"""
import hashlib
import json
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Pass the extracted original input directory.")
base = Path(sys.argv[1]).resolve()
manifest = json.loads((base / "manifest.json").read_text())
members = manifest["members"]
seen = set()
for row in members:
    rel = Path(row["member"])
    assert not rel.is_absolute() and ".." not in rel.parts
    assert row["member"] not in seen
    seen.add(row["member"])
    p = base / rel
    data = p.read_bytes()
    assert len(data) == row["bytes"], row["member"]
    assert hashlib.sha256(data).hexdigest() == row["sha256"], row["member"]

graph = json.loads((base / "repository/corpus/lean_dependencies.json").read_text())
reached = set(graph["reached"])
declared = set(graph["declared"])
oracle = (base / "repository/lean/QuarticQuery/Bridge/Oracle.lean").read_text()
deferred = (base / "repository/lean/QuarticQuery/Bridge/Deferred.lean").read_text()
extractor = (base / "repository/lean/scripts/Reach.lean").read_text()
assert "private theorem norm_pair" in oracle
assert "norm_invSqrtTwo_sq" in oracle[oracle.index("private theorem norm_pair"):oracle.index("private theorem norm_pair") + 500]
assert "QuarticQuery.norm_hadamardL" in reached
assert "QuarticQuery.norm_invSqrtTwo_sq" in declared
assert "QuarticQuery.norm_invSqrtTwo_sq" not in reached
assert "QuarticQuery.FixedSim.query" in reached
query_edges = graph["edges"]["QuarticQuery.FixedSim.query"]
assert "QuarticQuery.exists_gate" not in query_edges
assert "QuarticQuery.hadamard_phaseOracle_hadamard" not in query_edges
assert "hadamard_phaseOracle_hadamard" in deferred
assert "else if c.isInternal && (`QuarticQuery).isPrefixOf c then" in extractor

actual = {str(p.relative_to(base)) for p in base.rglob("*") if p.is_file()}
report = {
    "status": "passed",
    "verification_kind": "read-only byte integrity and source/graph consistency observations; not compilation",
    "repository_commit_recorded": manifest["repository_commit"],
    "manifest_members": len(members),
    "unique_manifest_members": len(seen),
    "all_sizes_and_sha256_match": True,
    "extracted_files": len(actual),
    "unlisted_files": sorted(actual - seen),
    "compiled_objects_in_archive": len(list(base.rglob("*.olean"))),
    "raw_receipts_present": (base / "repository/corpus/receipts").exists(),
    "private_path_observation": {
        "root": "QuarticQuery.norm_hadamardL",
        "source_private_helper": "norm_pair",
        "source_leaf": "QuarticQuery.norm_invSqrtTwo_sq",
        "root_reached": True,
        "leaf_declared": True,
        "leaf_reached": False,
    },
    "FixedSim_query_reported_edges": query_edges,
    "specific_compiled_cause": "unconfirmed without matching compiled environment; snapshot drift may also contribute",
}
Path(__file__).with_name("input_integrity_output.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
