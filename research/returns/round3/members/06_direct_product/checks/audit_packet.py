#!/usr/bin/env python3
"""Recheck supplied packet bytes against manifests and native-receipt inputs.

Usage: python3 checks/audit_packet.py /path/to/unpacked/quartic_r3_06_direct_product
This validates recorded source bindings. It does not run Lean or authenticate
the original execution, inspect missing compiled artifacts, or prove fidelity.
"""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    root = args.packet.resolve()

    def read(name):
        return json.loads((root / name).read_text())

    manifest = read("manifest.json")
    failures = []
    for item in manifest["members"]:
        path = (root / item["member"]).resolve()
        assert path.is_relative_to(root), "Manifest path escapes packet"
        if not path.is_file():
            failures.append({"member": item["member"], "error": "missing"})
        elif path.stat().st_size != item["bytes"] or digest(path) != item["sha256"]:
            failures.append({"member": item["member"], "error": "byte/hash mismatch"})

    receipt_names = [
        "repository/corpus/receipts/lean-build-root-2026-11-02T182539383153+0000.json",
        "native_results/final-evidence/reviewed_axiom_audit_verdict.json",
        "repository/corpus/lean_dependencies.json",
    ]
    bindings = []
    for name in receipt_names:
        record = read(name)
        bad = []
        for local, expected in record["source_hashes"].items():
            path = (root / "repository" / local).resolve()
            assert path.is_relative_to(root), "Receipt path escapes packet"
            if not path.is_file() or digest(path) != expected:
                bad.append(local)
        bindings.append({"receipt": name, "sha256": digest(root / name),
                         "source_hashes_checked": len(record["source_hashes"]),
                         "mismatches": bad})
        failures.extend({"receipt": name, "input": x} for x in bad)

    native = read("native_results/native-retry-1/results.json")
    focused = next(x for x in native["results"]
                   if x["target"] == "QuarticQuery.Paper.ClassicalDirectProduct")
    bad = []
    for original, expected in focused["inputs_before"].items():
        assert "/lean/" in original, "Unrecognized recorded input prefix"
        relative = original.split("/lean/", 1)[1]
        path = (root / "repository/lean" / relative).resolve()
        assert path.is_relative_to(root), "Focused input escapes packet"
        if not path.is_file() or digest(path) != expected:
            bad.append(original)
    failures.extend({"focused_input": x} for x in bad)
    assert focused["status"] == "passed" and focused["exit_code"] == 0
    assert focused["inputs_unchanged"] is True

    audit = read(receipt_names[1])
    for key, name in [
        ("log_sha256", "native_logs/final-evidence/reviewed-type-axiom-audit.log"),
        ("audit_source_sha256", "native_sources/final-evidence/reviewed_axiom_audit.lean"),
    ]:
        if digest(root / name) != audit[key]:
            failures.append({"audit_material": name, "error": "hash mismatch"})
    assert audit["passed"] and audit["native_exit_code"] == 0

    build = read(receipt_names[0])
    deps = read(receipt_names[2])
    named = [
        "QuarticQuery.guessSuccess_le_prod",
        "QuarticQuery.direct_product",
        "QuarticQuery.exists_hard_distribution",
        "QuarticQuery.address_guess_le",
        "QuarticQuery.Paper.classical_transcript_product_law",
        "QuarticQuery.Paper.classical_transcript_conditional_expectation",
        "QuarticQuery.Paper.classical_success_le_terminal",
        "QuarticQuery.Paper.classical_direct_product",
        "QuarticQuery.Paper.classical_direct_product_average",
    ]
    membership = [{"declaration": n, "build_inventory": n in build["declarations"],
                   "dependency_inventory": n in deps["declared"],
                   "headline_reached": n in deps["reached"]} for n in named]
    assert all(x["build_inventory"] and x["dependency_inventory"] for x in membership)
    result = {
        "kind": "independent source-byte and recorded-membership check",
        "packet_commit": manifest["repository_commit"],
        "recorded_build_commit": build["commit"],
        "packet_members_checked": len(manifest["members"]),
        "receipt_input_bindings": bindings,
        "focused_native_target": focused["target"],
        "focused_recorded_status": focused["status"],
        "focused_recorded_exit_code": focused["exit_code"],
        "focused_local_inputs_checked": len(focused["inputs_before"]),
        "focused_recorded_inputs_unchanged": focused["inputs_unchanged"],
        "focused_input_mismatches": bad,
        "audit_log_and_source_hashes_match": not any("audit_material" in x for x in failures),
        "selected_declaration_membership": membership,
        "all_byte_checks_passed": not failures,
        "failures": failures,
        "fresh_lean_execution": False,
        "compiled_root_artifact_supplied": False,
        "independent_execution_reproduction": False,
        "scope": "Hash agreement and supplied record contents only; no new Lean, Comparator, or human review.",
    }
    print(json.dumps(result, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
