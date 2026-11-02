#!/usr/bin/env python3
"""Audit supplied bytes/receipts. Does not run Lean or certify receipt authenticity."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet_root", type=Path)
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    packet = args.packet_root.resolve()
    repo = packet / "repository"
    spec = importlib.util.spec_from_file_location("frozen_build_corpus", repo / "tools/build_corpus.py")
    owner = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(owner)
    hashes = owner.source_hashes(repo)
    # Independent traversal of exactly the owner's documented binding scope.
    independently_hashed = {}
    for path in sorted((repo / "lean").rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(repo)
        directories = rel.parts[1:-1]
        if any(p.startswith(".") or p in {"build", "__pycache__"} for p in directories):
            continue
        if (path.suffix == ".lean" or path.name in {"lean-toolchain", "lakefile.toml", "lake-manifest.json"}
                or path.suffix == ".json" and "QuarticCorpus" in rel.parts):
            independently_hashed[rel.as_posix()] = digest(path)
    manifest = read(packet / "manifest.json")
    checks = {
        "independent_source_scope_agrees": hashes == independently_hashed,
        "snapshot_source_hashes_match": hashes == read(packet / "EVIDENCE_SNAPSHOT.json")["source_hashes"],
        "request_hash_matches": digest(packet / "READ_ME_FIRST.md") == manifest["request_sha256"],
        "paper_pdf_hash_matches": digest(packet / "paper/source.pdf") == manifest["paper_provenance"]["sha256"],
    }
    receipt_rows = []
    for path in sorted((repo / "corpus/receipts").glob("*.json")):
        record = read(path)
        receipt_rows.append({
            "path": path.relative_to(packet).as_posix(), "sha256": digest(path),
            "kind": record["kind"], "name": record["name"], "recorded_status": record["status"],
            "currentness_recomputed": owner.currentness(record, hashes),
            "bound_input_count": len(record.get("source_hashes", {})),
            "commit": record.get("commit"), "ran_at": record.get("ran_at"),
            "exit_code": record.get("exit_code"), "paranoid": record.get("paranoid"),
            "sandboxed": record.get("sandboxed"), "negative_control": record.get("negative_control"),
            "declarations": record.get("declarations", []),
        })
    closure_path = repo / "corpus/lean_dependencies.json"
    closure = read(closure_path)
    reached = set(closure["reached"])
    declared = set(closure["declared"])
    projected_edges = {(parent, child) for parent, children in closure["edges"].items() for child in children}
    witnesses = [(parent, item["to"], item["via"])
                 for parent, items in closure["hidden_paths"].items() for item in items]
    checks.update({
        "closure_current": owner.currentness(closure, hashes) == "current",
        "closure_unresolved_empty": not closure["unresolved_constants"],
        "closure_roots_present": set(closure["roots"]) <= reached <= declared,
        "hidden_witnesses_nonempty_and_projected": all(via and (parent, child) in projected_edges
                                                      for parent, child, via in witnesses),
    })
    root_receipts = [r for r in receipt_rows if r["kind"] == "lean_build"
                     and r["currentness_recomputed"] == "current" and r["recorded_status"] == "passed"]
    checks["root_receipt_declared_matches_export"] = bool(root_receipts) and all(
        set(r["declarations"]) == declared for r in root_receipts)
    audit_verdict = read(packet / "native_results/final-evidence/reviewed_axiom_audit_verdict.json")
    checks.update({
        "supplied_axiom_audit_source_bound": audit_verdict["source_hashes"] == hashes,
        "supplied_axiom_audit_log_hash_matches": digest(packet / "native_logs/final-evidence/reviewed-type-axiom-audit.log") == audit_verdict["log_sha256"],
        "supplied_axiom_audit_script_hash_matches": digest(packet / "native_sources/final-evidence/reviewed_axiom_audit.lean") == audit_verdict["audit_source_sha256"],
    })
    fixture_path = packet / "native_sources/native-inventory/ReachRegression.lean"
    checks["native_reach_fixture_has_actual_exporter_prefix"] = fixture_path.read_bytes().startswith(
        (repo / "lean/scripts/Reach.lean").read_bytes())
    reader = read(packet / "native_results/reader-acceptance/receipt.json")
    reader_graph_path = packet / "native_results/reader-acceptance/evidence-graph.json"
    checks["supplied_reader_graph_hash_matches_receipt"] = digest(reader_graph_path) == reader["graph_sha256"]
    current_graph_path = repo / "corpus/evidence-graph.json"
    current_graph = read(current_graph_path)
    controls_path = repo / "tools/return_checks/semantic_controls.py"
    toy = subprocess.run([sys.executable, str(controls_path)], capture_output=True, text=True)
    checks["toy_controls_exit_zero"] = toy.returncode == 0
    targets = ["QuarticQuery.R_le_iff", "QuarticQuery.Q_le_iff",
               "QuarticQuery.Paper.erasedZero_eq_expectedZeros_div",
               "QuarticQuery.Paper.expectedZeros_le_four", "QuarticQuery.Paper.eq_19",
               "QuarticQuery.avg_foundZero_I_le"]
    result = {
        "kind": "local byte-integrity and supplied-receipt audit; no native Lean execution",
        "scope": "These checks establish agreement of supplied bytes and recorded fields, not independent execution or receipt authenticity.",
        "packet_commit": manifest["repository_commit"],
        "archive_sha256": digest(args.archive) if args.archive else None,
        "source_input_count": len(hashes), "source_hashes": hashes,
        "checks": checks, "all_checks_passed": all(checks.values()),
        "receipt_counts": dict(Counter(r["currentness_recomputed"] for r in receipt_rows)),
        "receipts": receipt_rows,
        "closure": {"path": closure_path.relative_to(packet).as_posix(), "sha256": digest(closure_path),
                    "declared": len(declared), "reached": len(reached), "projected_edges": len(projected_edges),
                    "hidden_parent_count": len(closure["hidden_paths"]), "hidden_witness_count": len(witnesses),
                    "traversed_constants": closure["traversed_constants"],
                    "unresolved": closure["unresolved_constants"], "roots": closure["roots"]},
        "target_evidence": {target: {"declared": target in declared, "reached": target in reached,
            "current_build_receipts": [r["path"] for r in receipt_rows if target in r["declarations"]
                and r["kind"] == "lean_build" and r["currentness_recomputed"] == "current"],
            "current_comparison_receipts": [r["path"] for r in receipt_rows if target in r["declarations"]
                and r["kind"] == "comparator" and r["currentness_recomputed"] == "current"]} for target in targets},
        "supplied_axiom_audit": {k: audit_verdict[k] for k in ["passed", "checks", "declarations", "allowed_axioms", "native_exit_code", "boundary"]},
        "reader_receipt": {"source_hashes_match": reader["source_hashes"] == hashes,
            "recorded_passed": reader["passed"],
            "recorded_operations": [{"argv": o["argv"], "exit_code": o["exit_code"]} for o in reader["operations"]],
            "retained_graph_matches_current_graph": digest(reader_graph_path) == digest(current_graph_path),
            "retained_ties_match_current_ties": digest(repo / "corpus/ties.json") == reader["ties_sha256"],
            "native_extraction": False,
            "boundary": "Receipt validates/consumes its retained informal graph, not a Lean extraction and not necessarily the later current graph."},
        "current_graph": {"node_count": len(current_graph["nodes"]), "extraction_status": current_graph["extraction_status"],
            "source_ids": [s["id"] for s in current_graph["sources"]],
            "r2_live_count": sum(n["id"].startswith("r2-live-") for n in current_graph["nodes"])},
        "toy_controls": {"command": [sys.executable, str(controls_path)], "exit_code": toy.returncode,
            "source_sha256": digest(controls_path), "stdout_sha256": hashlib.sha256(toy.stdout.encode()).hexdigest(),
            "result": json.loads(toy.stdout) if toy.returncode == 0 else None, "stderr": toy.stderr},
        "limitations": ["No Lean, Lake, Comparator or native lean-exposition replay took place.",
            "Pinned dependency revisions do not hash dependency checkout bytes or executable bytes.",
            "Before/after source binding cannot detect a transient edit-and-revert during a supplied run.",
            "Most supplied build/comparison logs are summaries; receipt log hashes do not reconstruct missing complete logs.",
            "Currentness does not establish intended-statement fidelity, author review, or clean-clone reproducibility."],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": result["all_checks_passed"], "checks": checks,
                      "receipt_counts": result["receipt_counts"], "closure": result["closure"],
                      "reader_receipt": result["reader_receipt"]}, indent=2))
    return 0 if result["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
