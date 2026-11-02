"""Validate this return's evidence contract and its supplied check results.

No original input is required. No Lean execution is implied. The accompanying
evidence_index.json records existing identifiers for reference validation only.
"""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent.parent


def read_json(name):
    return json.loads((root / name).read_text())


required = {
    "fidelity_audit.md", "sanity_theorems.json", "NEW_STATEMENTS.json",
    "STATEMENT_CHANGES.json", "LEAN_GAPS.md", "correspondence.json", "references.bib",
}
assert all((root / p).is_file() for p in required)
sanity = read_json("sanity_theorems.json")
new = read_json("NEW_STATEMENTS.json")
changes = read_json("STATEMENT_CHANGES.json")
crosswalk = read_json("correspondence.json")
index = read_json("checks/evidence_index.json")
existing = set(index["existing_statement_ids"])
known_lean = set(index["existing_lean_names_for_spelling"])

schemas = [
    (sanity, {"id", "statement", "proposed_lean", "expected_value", "source", "what_it_would_catch"}),
    (new, {"id", "statement", "why_needed", "depends_on", "proposed_lean", "route_note"}),
    (changes, {"id", "old", "new", "relation", "reason"}),
    (crosswalk, {"passage", "from", "to", "role", "statement_ids", "lean"}),
]
for rows, fields in schemas:
    for row in rows:
        assert fields <= row.keys(), (row, fields - row.keys())
for rows in (sanity, new, changes):
    assert len({r["id"] for r in rows}) == len(rows)
for row in sanity + new:
    assert row["status"] == "proposed_unelaborated", row["id"]
    assert row["elaboration_status"] == "proposed_unelaborated", row["id"]
    assert row["proposed_lean"].strip()
    assert row.get("lean_context")
    assert "sorry" not in row["proposed_lean"]

new_by_id = {r["id"]: r for r in new}
all_ids = existing | new_by_id.keys()
assert {r["id"] for r in sanity} <= new_by_id.keys()
for row in new:
    assert set(row["depends_on"]) <= all_ids, row["id"]


def visit(node, active, done):
    assert node not in active, ("dependency cycle", node)
    if node in done or node not in new_by_id:
        return
    active.add(node)
    for dep in new_by_id[node]["depends_on"]:
        visit(dep, active, done)
    active.remove(node)
    done.add(node)


done = set()
for node in new_by_id:
    visit(node, set(), done)

report = (root / "fidelity_audit.md").read_text()
assert "—" not in report
assert report.count("\\[") == report.count("\\]") == 4
anchors = list(re.finditer(r"<!-- passage:([A-Za-z0-9_-]+) -->", report))
names = [m.group(1) for m in anchors]
assert len(names) == len(set(names))
assert {r["passage"] for r in crosswalk} == set(names)
assert len(crosswalk) == len(names)
blocks = {}
for i, m in enumerate(anchors):
    end = anchors[i + 1].start() if i + 1 < len(anchors) else len(report)
    blocks[m.group(1)] = report[m.end():end].strip()
for row in crosswalk:
    block = blocks[row["passage"]]
    assert block.startswith(row["from"]), row["passage"]
    assert block.endswith(row["to"]), row["passage"]
    assert row["role"] in {"states", "defines", "proves", "explains", "uses", "mentions"}
    assert set(row["statement_ids"]) <= all_ids, row["passage"]
    assert set(row["lean"]) <= known_lean, row["passage"]
for anchor in index["displayed_math_anchors"]:
    assert "\\[" in blocks[anchor]

# All short new-claim references printed in prose must be registered.
mentioned_new = set(re.findall(r"`((?:sf-|sanity-|fidelity-literal-)[A-Za-z0-9_-]+)`", report))
assert mentioned_new <= new_by_id.keys(), mentioned_new - new_by_id.keys()
for row in changes:
    assert row["relation"] in {"stronger", "weaker", "equivalent", "corrected"}
    assert row["kind"] in {"evidence_description", "literature_digest", "citation_locator", "documentation_attribution"}
    assert set(row.get("affected_statement_ids", [])) <= existing

nc = read_json("negative_controls.json")
assert len({r["id"] for r in nc}) == len(nc)
for row in nc:
    assert {"id", "mutation", "independent_test", "expected_result", "status"} <= row.keys()
    assert row["status"] == "proposed_not_run"

bib = (root / "references.bib").read_text()
bib_keys = re.findall(r"@\w+\{([^,]+),", bib)
assert len(set(bib_keys)) == len(bib_keys)
assert bib.count("{") == bib.count("}")
assert {"OAI26", "BDW02", "BBCMW01", "ABKRT21", "BS21", "DW26", "SS06", "ComparatorDocs", "LeanPrivateNames"} <= set(bib_keys)

c = read_json("checks/classical_checks_output.json")
f = read_json("checks/construction_checks_output.json")
r = read_json("checks/reach_private_output.json")
p = read_json("checks/input_integrity_output.json")
assert c["all_assertions_passed"] and f["status"] == r["status"] == p["status"] == "passed"
assert c["or2_equal_mixture_success"] == ["2/3", "2/3", "2/3", "1"]
assert f["forrelation"]["promise_census"] == {"true": 104, "false": 48, "none": 104}
assert f["toy_addressed_function"]["inputs_enumerated"] == 262144
assert f["toy_addressed_function"]["accepted"] == 16384
assert len(f["forrelation"]["general_witness_finite_checks"]) == 21
assert p["manifest_members"] == 356 and p["all_sizes_and_sha256_match"]
assert r["old_public_closure"] != r["filter_after_closure"]
assert (root / "READ_SCOPE.md").is_file()
read_json("source_read_scope.json")

result = {
    "status": "passed",
    "scope": "artifact integrity, exact passage boundaries, reference registration, evidence labels, and finite diagnostic results; not Lean verification",
    "required_files_present": sorted(required),
    "sanity_checks": len(sanity),
    "new_statement_records": len(new),
    "proposed_description_corrections": len(changes),
    "proposed_negative_controls": len(nc),
    "anchored_passages": len(crosswalk),
    "displayed_math_blocks": report.count("\\["),
    "bibliography_entries": len(bib_keys),
    "report_sha256": hashlib.sha256(report.encode()).hexdigest(),
    "all_lean_proposals_unelaborated": True,
    "no_lean_or_comparator_run": True,
    "all_assertions_passed": True,
}
(root / "checks/validation_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
