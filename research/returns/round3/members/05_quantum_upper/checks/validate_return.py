"""Read-only consistency and byte-integrity checks for this section return.

This checker does not execute Lean, establish mathematical truth, or verify
the provenance of an execution receipt. The original packet remains the
authority for the source bytes whose hashes and types are recorded here.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import re
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-unsealed", action="store_true",
                        help="pre-packaging check only; do not require MANIFEST.json")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    checks = []
    errors = []

    def check(ok, name, detail):
        checks.append({"check": name, "status": "passed" if ok else "failed",
                       "detail": detail})
        if not ok:
            errors.append(name)

    required = [
        "README.md", "section.md", "correspondence.json", "NEW_STATEMENTS.json",
        "STATEMENT_CHANGES.json", "LEAN_GAPS.md", "references.bib",
        "source_read_receipt.json", "review_notes.md", "STYLE_RULES.json",
        "declaration_types.json", "statement_catalogue.json",
        "EVIDENCE_CORRECTIONS.json", "cyclic_example.md",
        "checks/input_integrity.json", "checks/lean_evidence_audit.json",
        "checks/tournament_example.py", "checks/tournament_example.json",
        "checks/state_example.py", "checks/state_example.json",
    ]
    missing = [name for name in required if not (root / name).is_file()]
    check(not missing, "required_deliverables", {"missing": missing})
    if missing:
        print(json.dumps({"status": "failed", "checks": checks}, indent=2))
        return 1

    json_files = sorted(root.rglob("*.json"))
    records = {}
    invalid = []
    for path in json_files:
        try:
            records[path.relative_to(root).as_posix()] = json.loads(path.read_text())
        except (UnicodeError, json.JSONDecodeError) as exc:
            invalid.append({"file": path.name, "error": str(exc)})
    check(not invalid, "json_parse", {"files": len(json_files), "errors": invalid})
    if invalid:
        print(json.dumps({"status": "failed", "checks": checks}, indent=2))
        return 1

    section = (root / "section.md").read_text()
    pairs = list(re.finditer(r"<!-- passage:(.*?) -->(.*?)<!-- /passage:\1 -->",
                             section, re.S))
    bodies = {m[1]: m[2].strip() for m in pairs}
    starts = re.findall(r"<!-- passage:(.*?) -->", section)
    ends = re.findall(r"<!-- /passage:(.*?) -->", section)
    check(len(pairs) == len(starts) == len(ends) == len(set(starts))
          and starts == ends, "passage_pairing",
          {"passages": len(pairs), "unique": len(set(starts))})

    corr = records["correspondence.json"]
    corr_names = [r["passage"] for r in corr]
    check(corr_names == starts, "correspondence_coverage",
          {"passages": len(corr_names), "same_order_as_section": corr_names == starts})
    catalogue = {r["id"]: r for r in records["statement_catalogue.json"]}
    selected = {r["name"]: r for r in records["declaration_types.json"]["declarations"]}
    audited = {r["name"]: r for r in records["checks/lean_evidence_audit.json"]["declarations"]}
    source_members = {r["member"]: r for r in records["source_read_receipt.json"]["members"]}
    used_names = set()
    used_ids = set()
    mapping_problems = []
    displays_count = 0
    roles = {"states", "defines", "proves", "explains", "uses", "mentions"}
    for row in corr:
        name = row["passage"]
        body = bodies.get(name, "")
        if not body.startswith(row["from"]) or not body.endswith(row["to"]):
            mapping_problems.append(name + ": boundary excerpt mismatch")
        if row["role"] not in roles:
            mapping_problems.append(name + ": unsupported role")
        if len(row["lean"]) != len(set(row["lean"])):
            mapping_problems.append(name + ": repeated Lean name")
        if row["lean"] != [d["declaration"] for d in row["complete_lean_types"]]:
            mapping_problems.append(name + ": type/name order mismatch")
        ids = row["statement_ids"]
        used_ids.update(ids)
        if any(s not in catalogue for s in ids):
            mapping_problems.append(name + ": statement ID absent from catalogue")
        inline_claims = re.findall(r"<!-- claim:(.*?) -->", body)
        if not set(inline_claims).issubset(ids):
            mapping_problems.append(name + ": inline claim not mapped")
        displays = [d.strip() for d in re.findall(r"\$\$(.*?)\$\$", body, re.S)]
        if displays != [d["exact_latex"] for d in row["displays"]]:
            mapping_problems.append(name + ": display text mismatch")
        displays_count += len(displays)
        for item in row["complete_lean_types"]:
            decl_name = item["declaration"]
            used_names.add(decl_name)
            if decl_name not in selected or decl_name not in audited:
                mapping_problems.append(name + ": undeclared type record " + decl_name)
                continue
            audit = audited[decl_name]
            if selected[decl_name] != audit:
                mapping_problems.append(decl_name + ": selected audit record changed")
            if item["complete_source_statement"] != audit["source_statement"]:
                mapping_problems.append(decl_name + ": signature mismatch")
            if item["printed_elaborated_type"] != audit.get("printed_full_type"):
                mapping_problems.append(decl_name + ": printed type mismatch")
            if item["ambient_source_variables"] != audit["ambient_source_variables"]:
                mapping_problems.append(decl_name + ": ambient variables mismatch")
            member = item["source"]["member"]
            digest = item["source"]["sha256"]
            if member not in source_members or digest != source_members[member]["sha256"]:
                mapping_problems.append(decl_name + ": source digest mismatch")
    check(not mapping_problems, "exact_correspondence",
          {"mapped_displays": displays_count, "statement_ids": len(used_ids),
           "selected_declarations": len(used_names), "problems": mapping_problems})
    check(used_names == set(selected), "selected_type_coverage",
          {"used": len(used_names), "recorded": len(selected)})

    new_statements = records["NEW_STATEMENTS.json"]
    check(len({s["id"] for s in new_statements}) == len(new_statements)
          and all(s["id"] in catalogue and catalogue[s["id"]]["record"] == s
                  for s in new_statements),
          "new_statement_identity", {"entries": len(new_statements)})
    check(records["STATEMENT_CHANGES.json"] == [],
          "canonical_statement_changes", "No canonical statement text was changed.")

    bib = (root / "references.bib").read_text()
    bib_keys = re.findall(r"@\w+\{([^,\s]+),", bib)
    cited_keys = set(re.findall(r"\[([A-Z][A-Za-z0-9]+),", section))
    correspondence_keys = {c["key"] for r in corr for c in r["citation_roles"]}
    correspondence_keys.discard("packet-native-evidence")
    check(len(bib_keys) == len(set(bib_keys))
          and (cited_keys | correspondence_keys).issubset(bib_keys),
          "bibliography_keys",
          {"entries": len(bib_keys),
           "unresolved": sorted((cited_keys | correspondence_keys) - set(bib_keys))})

    styles = records["STYLE_RULES.json"]["rules"]
    style_problems = [r["id"] for r in styles
                      if r["after"]["exact_excerpt"] not in bodies.get(r["after"]["passage"], "")]
    check(not style_problems, "style_after_excerpts",
          {"rules": len(styles), "unresolved": style_problems})

    control_chars = [ord(c) for c in section if ord(c) < 32 and c not in "\n\t"]
    odd_dollar_lines = [i for i, line in enumerate(section.splitlines(), 1)
                        if len(re.findall(r"(?<!\\)\$", line)) % 2]
    # The delivered section deliberately places both ends of inline math on one line.
    check(not control_chars and not odd_dollar_lines
          and sum(line.strip() == "$$" for line in section.splitlines()) % 2 == 0,
          "section_math_delimiters",
          {"control_characters": control_chars, "odd_dollar_lines": odd_dollar_lines})

    finite = ["checks/tournament_example.json", "checks/state_example.json"]
    check(all(records[p]["status"] == "passed" for p in finite),
          "recorded_finite_checks", finite)
    integrity = records["checks/input_integrity.json"]
    check(integrity["status"] == "passed"
          and integrity["listed_members_checked"] == len(source_members),
          "input_integrity_record",
          {"members": len(source_members),
           "scope": "Recorded custody check, not a rerun against the original ZIP."})
    for label in ["fresh_lean_execution", "fresh_comparator_execution"]:
        check(all(r["evidence_state"][label] is False for r in corr),
              label + "_boundary", "No fresh formal execution claimed.")

    manifest = records.get("MANIFEST.json")
    if manifest is None:
        check(args.allow_unsealed, "return_byte_manifest",
              "Not sealed yet." if args.allow_unsealed else "MANIFEST.json missing.")
    else:
        manifest_problems = []
        expected = {r["member"] for r in manifest["members"]}
        actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
        if actual - {"MANIFEST.json"} != expected:
            manifest_problems.append({
                "missing_from_manifest": sorted(actual - {"MANIFEST.json"} - expected),
                "missing_from_disk": sorted(expected - actual)})
        for row in manifest["members"]:
            path = root / row["member"]
            if Path(row["member"]).is_absolute() or ".." in Path(row["member"]).parts:
                manifest_problems.append({"unsafe_member": row["member"]})
                continue
            if not path.is_file():
                continue
            data = path.read_bytes()
            if len(data) != row["bytes"] or sha256(data).hexdigest() != row["sha256"]:
                manifest_problems.append({"mismatch": row["member"]})
        check(not manifest_problems, "return_byte_manifest",
              {"hashed_members": len(manifest["members"]),
               "self_exclusion": "MANIFEST.json is intentionally not self-hashed.",
               "problems": manifest_problems})

    result = {
        "schema": "quartic-r3-05-return-validation-v1",
        "status": "passed" if not errors else "failed",
        "checks": checks,
        "errors": errors,
        "scope": "Read-only structure and recorded byte-integrity consistency; not Lean, Comparator, mathematical proof, source-provenance certification, or rendered-page QA.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
