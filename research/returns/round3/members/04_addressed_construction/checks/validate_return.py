#!/usr/bin/env python3
"""Check this return and replay its exact example using only Python's stdlib.

Run from any directory. Optional --source-packet checks the original supplied
source hashes and statement identifiers. This script never invokes Lean.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_json(path):
    return json.loads(path.read_text())

def need(condition, message):
    if not condition:
        raise AssertionError(message)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-packet", type=Path)
    args = parser.parse_args()
    required = [
        "section.md", "correspondence.json", "NEW_STATEMENTS.json",
        "STATEMENT_CHANGES.json", "LEAN_GAPS.md", "references.bib",
        "source_read_receipt.json", "review_notes.md", "STYLE_RULES.json",
        "README.md", "integration_map.json", "examples/check_example.py",
        "examples/output.json", "examples/board.json", "examples/circuit.json",
        "examples/validation.json", "evidence/lean_audit.json",
        "evidence/interface_definitions.json",
    ]
    for name in required:
        need((ROOT / name).is_file(), "missing required file: " + name)
    json_files = sorted(ROOT.rglob("*.json"))
    for path in json_files:
        read_json(path)

    section = (ROOT / "section.md").read_text()
    need(not any(ord(c) < 32 and c not in "\n\t\r" for c in section),
         "unexpected control character in section")
    starts = re.findall(r"<!-- passage:([^ ]+) -->", section)
    ends = re.findall(r"<!-- /passage:([^ ]+) -->", section)
    need(starts == ends and len(starts) == len(set(starts)), "anchor mismatch")
    passages = dict(re.findall(
        r"<!-- passage:([^ ]+) -->\n(.*?)\n<!-- /passage:\1 -->",
        section, re.S))
    need(len(passages) == 19, "expected 19 stable passages")
    records = read_json(ROOT / "correspondence.json")
    need([r["passage"] for r in records] == starts, "correspondence order")
    known_roles = {"states", "defines", "proves", "explains", "uses", "mentions"}
    displays = []
    source_bindings = {}
    for record in records:
        anchor = record["passage"]
        content = passages[anchor]
        need(record["role"] in known_roles, "unknown correspondence role")
        need(content.startswith(record["from"]), "from boundary: " + anchor)
        need(content.endswith(record["to"]), "to boundary: " + anchor)
        need(record["lean"] == [s["declaration"] for s in record["lean_support"]],
             "Lean type membership: " + anchor)
        actual_displays = re.findall(r"\$\$\n(.*?)\n\$\$", content, re.S)
        need(actual_displays == [d["exact_display"] for d in record["displays"]],
             "display coverage: " + anchor)
        for support in record["lean_support"]:
            need(support["complete_type"], "empty full type")
            need(support["ordinary_premises"] is not None, "missing premises")
            need(support["actual_evidence"], "missing evidence")
            name = support["declaration"]
            if name in source_bindings:
                need(source_bindings[name] == support, "conflicting type record: " + name)
            source_bindings[name] = support
        for display in record["displays"]:
            need(display["lean"] == record["lean"], "display Lean mismatch")
            need(set(display["complete_lean_types"]) == set(display["lean"]),
                 "display full-type mismatch")
            tag = re.search(r"\\tag\{([^}]+)\}", display["exact_display"])
            need(tag and tag.group(1) == display["label"], "display tag mismatch")
            level = 0
            for token in re.findall(r"(?<!\\)[{}]", display["exact_display"]):
                level += 1 if token == "{" else -1
                need(level >= 0, "closing math brace without opener")
            need(level == 0, "unbalanced display braces")
            displays.append(display["label"])
        if "computation" in record:
            comp = record["computation"]
            for key in ("script", "output"):
                need(digest(ROOT / comp[key]) == comp[key + "_sha256"],
                     "stale computation digest")
    need(displays == ["4." + str(i) for i in range(1, 20)], "display numbering")
    no_displays = re.sub(r"\$\$\n.*?\n\$\$", "", section, flags=re.S)
    need(len(re.findall(r"(?<!\\)\$", no_displays)) % 2 == 0,
         "unpaired inline math delimiter")

    new = read_json(ROOT / "NEW_STATEMENTS.json")
    new_ids = {s["id"] for s in new}
    need(len(new) == len(new_ids) == 4, "supplemental statement identifiers")
    need(read_json(ROOT / "STATEMENT_CHANGES.json") == [], "canonical changes unexpected")
    for record in new:
        for field in ("statement", "why_needed", "depends_on", "proposed_lean", "route_note"):
            need(field in record, "new-statement field missing")
    for record in records:
        for identifier in record["statement_ids"]:
            need(identifier in new_ids or identifier in record["canonical_statement_text"],
                 "unresolved statement ID: " + identifier)
    style = read_json(ROOT / "STYLE_RULES.json")
    for rule in style["rules"]:
        need(rule["after"]["exact_excerpt"] in passages[rule["after"]["passage"]],
             "stale style after-excerpt")
        need(rule["limit"] and rule["source"]["locator"], "style scope missing")

    example_dir = ROOT / "examples"
    with tempfile.TemporaryDirectory(prefix="quartic-return-check-") as tmp:
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        process = subprocess.run(
            [sys.executable, "-B", str(example_dir / "check_example.py"),
             "--write-data", tmp],
            cwd=ROOT, env=env, capture_output=True, check=False
        )
        need(process.returncode == 0, "example failed: " + process.stderr.decode())
        need(process.stdout == (example_dir / "output.json").read_bytes(),
             "replayed stdout differs from output.json")
        for name in ("board.json", "circuit.json"):
            need((Path(tmp) / name).read_bytes() == (example_dir / name).read_bytes(),
                 "serialized example differs: " + name)
    example_receipt = read_json(example_dir / "validation.json")
    for name, expected in example_receipt["artifacts"].items():
        path = example_dir / name
        need(path.stat().st_size == expected["bytes"] and digest(path) == expected["sha256"],
             "example receipt binding: " + name)
    example = read_json(example_dir / "output.json")
    need(example["status"] == "all checks passed", "example status")

    source_check = {"requested": bool(args.source_packet)}
    if args.source_packet:
        packet = args.source_packet.resolve()
        inventory = read_json(packet / "manifest.json")
        for member in inventory["members"]:
            path = packet / member["member"]
            need(path.stat().st_size == member["bytes"] and digest(path) == member["sha256"],
                 "input manifest binding: " + member["member"])
        canonical = {s["id"]: s for s in read_json(packet / "repository/corpus/statements.json")}
        for record in records:
            for identifier, statement in record["canonical_statement_text"].items():
                need(canonical[identifier]["statement"] == statement,
                     "canonical text differs: " + identifier)
        for name, support in source_bindings.items():
            path = packet / support["file"]
            need(digest(path) == support["source_sha256"], "Lean source binding: " + name)
            if support["source_signature"]:
                need(support["source_signature"] in path.read_text(),
                     "exact source signature differs: " + name)
        for rule in style["rules"]:
            need(digest(packet / rule["source"]["file"]) == rule["source"]["sha256"],
                 "style source binding")
            need(rule["before"]["exact_excerpt"] in
                 (packet / rule["before"]["file"]).read_text(), "style before-excerpt")
        integration = read_json(ROOT / "integration_map.json")["replaces"]
        need(digest(packet / integration["file"]) == integration["sha256"],
             "integration source changed")
        source_check.update({
            "manifest_members": len(inventory["members"]),
            "bound_declarations": len(source_bindings),
            "canonical_statement_texts_match": True,
            "exact_present_source_signatures_match": True,
            "native_Lean_execution": False,
        })

    manifest_check = {"present": (ROOT / "manifest.json").exists()}
    if manifest_check["present"]:
        manifest = read_json(ROOT / "manifest.json")
        actual = sorted(
            str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
            if p.is_file() and p != ROOT / "manifest.json"
        )
        listed = [m["member"] for m in manifest["members"]]
        need(actual == listed, "manifest member inventory differs")
        for member in manifest["members"]:
            path = ROOT / member["member"]
            need(path.stat().st_size == member["bytes"] and digest(path) == member["sha256"],
                 "return manifest binding: " + member["member"])
        manifest_check.update({"members": len(listed), "all_bytes_and_hashes_match": True})

    result = {
        "status": "all checks passed",
        "scope": "Package correspondence, exact finite replay, optional supplied-source byte bindings; no Lean execution.",
        "python": sys.version.split()[0],
        "required_files_present": len(required),
        "json_files_parse": len(json_files),
        "passages": len(passages),
        "displays": displays,
        "fully_typed_declarations": len(source_bindings),
        "new_statements": len(new),
        "canonical_changes": 0,
        "style_rules": len(style["rules"]),
        "example_stdout_matches_saved_bytes": True,
        "example_circuit_and_board_match_saved_bytes": True,
        "example_receipt_hashes_match": True,
        "example_checks": {
            "circuit_inputs": example["exact_circuit"]["verified_inputs"],
            "candidate_pairs": len(example["candidate_checks"]),
            "local_test_evaluations": example["local_tests_evaluated_on_base_board"],
            "transcript_single_flips": example["single_selected_transcript_bit_flips_checked"],
            "parameters": example["parameters"],
            "winner": example["winner"],
            "domain_omission_counterexample": "passed",
            "equal_projection_law": "passed",
        },
        "source_bindings": source_check,
        "manifest": manifest_check,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
