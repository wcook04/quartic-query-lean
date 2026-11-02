#!/usr/bin/env python3
"""Check a return package's structure, exact excerpts and digests, not its proofs.

Run from any directory. With the original packet available, pass
--source-packet PATH to additionally verify inspected type excerpts against it.
The default detects the original sibling directory used during authoring.
This standard-library script never executes Lean, Lake, Comparator or a network call.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-packet", type=Path)
parser.add_argument("--allow-no-manifest", action="store_true",
                    help="authoring-only pass before the final manifest exists")
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
source = args.source_packet or root.parent / "quartic_r3_01_models_evidence"
errors = []
checks = {}

def check(condition, message):
    if not condition:
        errors.append(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def read_json(rel):
    try:
        return json.loads((root / rel).read_text())
    except Exception as ex:
        errors.append(f"Cannot parse {rel}: {ex}")
        return None

required = [
    "section.md", "correspondence.json", "NEW_STATEMENTS.json", "STATEMENT_CHANGES.json",
    "LEAN_GAPS.md", "references.bib", "source_read_receipt.json", "review_notes.md",
    "STYLE_RULES.json", "model_contract.json", "statement_catalog.json",
    "verification_note.md", "README.md", "checks/check_models_exact.py",
    "checks/quantum_controls.py", "checks/semantic_controls.py", "checks/README.md",
    "checks/exact_checks_execution.json", "checks/source_integrity.json",
    "checks/classical_exact_output.json", "checks/quantum_exact_output.json",
    "checks/supplied_semantic_controls_output.json",
]
for rel in required:
    check((root / rel).is_file(), f"Missing required file: {rel}")
for p in root.rglob("*.json"):
    read_json(str(p.relative_to(root)))
if errors:
    print(json.dumps({"status": "failed", "errors": errors}, indent=2))
    sys.exit(1)

section = (root / "section.md").read_text()
opening = re.findall(r"<!-- passage:([^ ]+) -->", section)
closing = re.findall(r"<!-- /passage:([^ ]+) -->", section)
passages = {
    key: body.strip()
    for key, body in re.findall(r"<!-- passage:([^ ]+) -->\n(.*?)<!-- /passage:\1 -->", section, re.S)
}
check(len(opening) == len(set(opening)), "Duplicate passage anchors")
check(opening == closing, "Passage opening/closing inventory differs")
check(len(passages) == len(opening), "Unparsed or nested passage")
for anchor in ["ROOT-RESULT", "ROOT-ARCHITECTURE", "ROOT-LOGS", "ROOT-PARTIAL",
               "ROOT-ORACLE", "ROOT-EVIDENCE-CONVENTION"]:
    check(anchor in passages, f"Missing retained baseline anchor {anchor}")
types = read_json("model_contract.json")["declarations"]
type_map = {x["declaration"]: x for x in types}
check(len(types) == len(type_map), "Duplicate declaration in model contract")
catalog = read_json("statement_catalog.json")
canonical = {x["id"]: x for x in catalog["statements"]}
new = read_json("NEW_STATEMENTS.json")
new_by_id = {x["id"]: x for x in new}
check(len(new) == len(new_by_id), "Duplicate new-statement identifier")
check(not (set(canonical) & set(new_by_id)), "New statement collides with canonical ID")
check(read_json("STATEMENT_CHANGES.json") == [], "Unexpected canonical statement change")
all_ids = set(canonical) | set(new_by_id)
for x in catalog["statements"]:
    check(digest(x["statement"].encode()) == x["statement_sha256"],
          f"Canonical statement digest mismatch: {x['id']}")
for x in new:
    for key in ["id", "statement", "why_needed", "depends_on", "proposed_lean", "route_note"]:
        check(key in x, f"Missing proposal field {key}: {x.get('id')}")
    for dep in x["depends_on"]:
        check(dep in all_ids, f"Unresolved proposal dependency {x['id']} -> {dep}")
    for name in x.get("formal_ingredients", []):
        check(name in type_map, f"Unresolved formal ingredient in proposal: {name}")

cross = read_json("correspondence.json")
check({x["passage"] for x in cross} == set(passages), "Crosswalk passage set differs")
bib = (root / "references.bib").read_text()
bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib))
display_total = 0
claim_total = 0
for row in cross:
    p = row["passage"]
    body = passages[p]
    check(row["role"] in ["states", "defines", "proves", "explains", "uses", "mentions"],
          f"Invalid role: {p}")
    check(row["from"] == body[:len(row["from"])], f"Passage start mismatch: {p}")
    check(body.endswith(row["to"]), f"Passage end mismatch: {p}")
    check(digest(body.encode()) == row["passage_sha256"], f"Passage digest mismatch: {p}")
    actual = [m.group(0) for m in re.finditer(r"\\\[.*?\\\]", body, re.S)]
    check(len(actual) == row["display_count"], f"Display count mismatch: {p}")
    display_total += len(actual)
    seen = set()
    for c in row["load_bearing_claims"]:
        claim_total += 1
        check(c["from"] in body and c["to"] in body, f"Claim boundary mismatch: {p}/{c['claim']}")
        check(c["route"] in ["same", "alternative", "none"], f"Invalid route: {p}/{c['claim']}")
        for sid in c["statement_ids"]:
            check(sid in all_ids, f"Unresolved statement ID: {sid}")
        check(c["lean"] == [t["declaration"] for t in c["complete_lean_types"]],
              f"Type list/name mismatch: {p}/{c['claim']}")
        for t in c["complete_lean_types"]:
            name = t["declaration"]
            check(name.startswith("QuarticQuery."), f"Unqualified declaration: {name}")
            check(name in type_map, f"Missing declaration contract: {name}")
            if name in type_map:
                for key in ["complete_source_declaration_or_signature", "enclosing_lean_context",
                            "complete_type_with_implicit_binders", "source_sha256", "evidence"]:
                    check(t[key] == type_map[name][key], f"Type/evidence drift: {name}/{key}")
        for t in c["formal_ingredients"]:
            check(t["declaration"] in type_map, f"Missing ingredient contract: {t['declaration']}")
        for citation in c["citation_roles"]:
            check(citation["key"] in bib_keys, f"Missing bibliography key: {citation['key']}")
        for artifact in c["evidence"]["supporting_artifacts"]:
            check((root / artifact).is_file(), f"Missing supporting artifact: {artifact}")
        for d in c["displays"]:
            i = d["ordinal_in_passage"] - 1
            check(0 <= i < len(actual), f"Bad display ordinal: {p}/{i}")
            if 0 <= i < len(actual):
                check(d["exact_display"] == actual[i], f"Display excerpt mismatch: {p}/{i+1}")
                check(digest(actual[i].encode()) == d["sha256"], f"Display digest mismatch: {p}/{i+1}")
            lo, hi = d["span_in_trimmed_passage"]
            check(body[lo:hi] == d["exact_display"], f"Display span mismatch: {p}/{i+1}")
            seen.add(i+1)
    check(seen == set(range(1, len(actual)+1)), f"Display missing from correspondence: {p}")
    check(set(row["lean"]) == {n for c in row["load_bearing_claims"] for n in c["lean"]},
          f"Passage declaration union mismatch: {p}")
    check(set(row["statement_ids"]) == {n for c in row["load_bearing_claims"] for n in c["statement_ids"]},
          f"Passage statement union mismatch: {p}")

note = re.search(r"^\*\*Verification note\.\*\* .+$", section, re.M)
check(note is not None, "No central verification paragraph")
if note:
    check((root / "verification_note.md").read_text() == note.group(0) + "\n",
          "Central verification note differs from extracted paragraph")
check(section.count(r"\[") == section.count(r"\]") + section.count(r"\\["),
      "Display delimiter count is inconsistent (allowing TeX array row spacing)")
# Inline math spans must balance per line; strip code to avoid false matches.
for i, line in enumerate(section.splitlines(), 1):
    tick = chr(96)
    clean = re.sub(tick + "[^" + tick + "]*" + tick, "", line)
    check(len(re.findall(r"(?<!\\)\$", clean)) % 2 == 0, f"Unbalanced inline math at line {i}")
checks["math_markup"] = "delimiter balance only; no PDF/KaTeX rendering claim"

execution = read_json("checks/exact_checks_execution.json")
for run in execution["scripts"]:
    script = root / "checks" / run["script"]
    output = root / "checks" / run["json_output"]
    check(digest(script.read_bytes()) == run["script_sha256"],
          f"Exact-check script drift: {run['script']}")
    check(digest(output.read_bytes()) == run["output_sha256"],
          f"Exact-check output drift: {run['json_output']}")
    check(run["exit_code"] == 0 and run["stderr_empty"],
          f"Exact-check run failed: {run['script']}")
integrity = read_json("checks/source_integrity.json")
check(not integrity["manifest_failures"], "Source manifest failures recorded")
check(not integrity["input_sha256_failures"], "Input hash failures recorded")
check(not integrity["local_source_failures"], "Local source binding failures recorded")
check(integrity["lean_or_comparator_rerun"] is False, "Unexpected proof-tool execution claim")
checks["captured_exact_execution_receipt"] = "three successful recorded runs; script/output hashes match"

source_checks = 0
if source.is_dir():
    for t in types:
        p = source / t["source"]
        check(p.is_file(), f"Original type source missing: {p}")
        if p.is_file():
            content = p.read_bytes()
            check(digest(content) == t["source_sha256"], f"Original source digest mismatch: {t['source']}")
            check(t["complete_source_declaration_or_signature"] in content.decode(),
                  f"Original source excerpt mismatch: {t['declaration']}")
            source_checks += 1
    checks["original_source_type_excerpts"] = f"checked {source_checks} entries against supplied bytes"
else:
    checks["original_source_type_excerpts"] = "not rerun: original source packet unavailable; stored source digests retained"

manifest_path = root / "MANIFEST.json"
if manifest_path.is_file():
    manifest = read_json("MANIFEST.json")
    members = manifest["return_members"]
    expected = {x["path"] for x in members}
    present = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"}
    check(expected == present, "Manifest member set differs from return directory")
    for entry in members:
        p = root / entry["path"]
        if p.is_file():
            check(p.stat().st_size == entry["bytes"], f"Manifest byte count mismatch: {entry['path']}")
            check(digest(p.read_bytes()) == entry["sha256"], f"Manifest digest mismatch: {entry['path']}")
    checks["return_manifest"] = f"verified {len(members)} members; self excluded"
elif args.allow_no_manifest:
    checks["return_manifest"] = "not yet present; authoring pass only"
else:
    errors.append("Missing MANIFEST.json")

result = {
    "status": "passed" if not errors else "failed",
    "scope": "Internal packaging, exact source excerpts, references, boundaries and digests; not mathematical compilation.",
    "counts": {"passages": len(passages), "load_bearing_claims": claim_total,
               "display_equations": display_total, "source_types": len(types),
               "proposed_statements": len(new)},
    "checks": checks,
    "errors": errors,
    "lean_executed": False,
    "comparator_executed": False,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if not errors else 1)
