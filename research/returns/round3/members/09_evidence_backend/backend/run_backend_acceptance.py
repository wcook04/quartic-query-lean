#!/usr/bin/env python3
"""Replay Python-only residual checks against an original and patched snapshot.

This records no native proof or Comparator pass. The transition examples use
mock operation receipts; the corpus dry runs consume actual supplied receipts.
Neither run mutates authored ties, historical receipts, or generated outputs.
"""

import argparse
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, root):
    spec = importlib.util.spec_from_file_location(name, root / "tools/build_corpus.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def summarize(module):
    outputs = module.outputs()
    records = outputs[module.CORPUS / "statements.json"]
    graph = outputs[module.CORPUS / "evidence-graph.json"]
    return {
        "coverage": outputs[module.CORPUS / "coverage.json"],
        "lean_tie_count": sum(len(record["lean"]) for record in records),
        "review_states": dict(Counter(tie.get("review_evidence", "not_enforced")
                                      for record in records for tie in record["lean"])),
        "reviewed_relation_counts": dict(Counter(tie.get("reviewed_relation", tie["relation"])
                                                  for record in records for tie in record["lean"])),
        "build_facts": dict(Counter(tie["build_evidence"]
                                     for record in records for tie in record["lean"])),
        "comparison_facts": dict(Counter(tie["comparison_evidence"]
                                          for record in records for tie in record["lean"])),
        "graph": {"nodes": len(graph["nodes"]), "edges": len(graph["edges"]),
                  "node_statuses": dict(Counter(node["status"] for node in graph["nodes"])),
                  "extraction_status": graph["extraction_status"],
                  "source_ids": [source["id"] for source in graph["sources"]]},
        "generated_byte_hashes_not_written_to_corpus": {
            str(path.relative_to(module.ROOT)): hashlib.sha256(module.render(value).encode()).hexdigest()
            for path, value in outputs.items()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", type=Path, required=True)
    parser.add_argument("--patched", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    original = load("original_corpus", args.original.resolve())
    patched = load("patched_corpus", args.patched.resolve())
    args.out.mkdir(parents=True, exist_ok=True)
    hashes_before = {"lean/Definition.lean": "a" * 64, "lean/Theorem.lean": "b" * 64}
    hashes_after = {**hashes_before, "lean/Definition.lean": "c" * 64}
    ledger = {"s": {"kind": "lemma", "statement": "Zero satisfies the equality-to-zero predicate.",
                     "original_statement_sha256": None, "corrected": False, "depends_on": []}}
    review = {"declaration": "A.permits_zero", "relation": "exact", "route": "same",
              "premises": [], "open_assumptions": [], "reviewed_by": "synthetic fixture only"}
    review["review_binding"] = patched.expected_review_binding("s", ledger["s"], review, hashes_before)
    runs = [{"kind": kind, "status": "passed", "declarations": ["A.permits_zero"],
             "source_hashes": hashes_after, "command": ["mock", kind]}
            for kind in ("lean_build", "comparator")]
    before_record = original.statement_records(ledger, {}, {"s": [review]}, runs, hashes=hashes_after)[0]
    after_record = patched.statement_records(ledger, {}, {"s": [review]}, runs, hashes=hashes_after)[0]
    assert before_record["evidence"]["comparator"] == "compared"
    assert after_record["evidence"]["comparator"] == "not_run"
    assert after_record["lean"][0]["build_evidence"] == "current"
    assert after_record["lean"][0]["comparison_evidence"] == "current"
    assert after_record["lean"][0]["review_evidence"] == "stale"
    helper = {"r2-live-helper": {**ledger["s"], "source_id": "derived_research"}}
    old_helper_records = original.statement_records(helper, {}, {}, [], hashes={})
    old_helper_graph = original.evidence_graph(old_helper_records, [], hashes={})
    assert old_helper_graph["nodes"][0]["source_id"] == "openai_preprint"
    try:
        patched.statement_records(helper, {}, {}, [], hashes={})
    except ValueError as error:
        helper_rejection = str(error)
    else:
        raise AssertionError("derived helper was not withheld")
    missing = deepcopy(ledger)
    missing["s"]["depends_on"] = ["r2-live-helper"]
    old_missing = original.evidence_graph(
        original.statement_records(missing, {}, {}, [], hashes={}), [], hashes={})
    assert old_missing["edges"] == []
    try:
        patched.evidence_graph(patched.statement_records(missing, {}, {}, [], hashes={}), [], hashes={})
    except ValueError as error:
        dependency_rejection = str(error)
    else:
        raise AssertionError("missing prerequisite was silently dropped")

    input_paths = ["corpus/ties.json", "research/intake/statement_ledger.json",
                   "research/adjudication/adjudication.json", "corpus/lean_dependencies.json"]
    before_input_hashes = {key: digest(args.original / key) for key in input_paths}
    original_corpus = summarize(original)
    patched_corpus = summarize(patched)
    assert before_input_hashes == {key: digest(args.original / key) for key in input_paths}
    assert before_input_hashes == {key: digest(args.patched / key) for key in input_paths}
    assert original.source_hashes() == patched.source_hashes()
    assert original_corpus["build_facts"] == patched_corpus["build_facts"]
    assert original_corpus["comparison_facts"] == patched_corpus["comparison_facts"]

    test_runs = []
    for label, root in (("original", args.original), ("patched", args.patched)):
        command = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
        result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=60)
        log = args.out / f"{label}-python-tests.log"
        log.write_text(result.stdout + result.stderr)
        test_runs.append({"label": label, "command": command, "cwd": str(root),
                          "exit_code": result.returncode, "log": log.name, "log_sha256": digest(log),
                          "scope": "Python tests; external operations mocked; native integrations skipped unless explicitly installed"})
        if result.returncode:
            raise RuntimeError(f"{label} tests failed; see {log}")
    files = ["tools/build_corpus.py", "tests/test_build_corpus.py", "tests/test_record_evidence.py",
             "tests/test_build_challenges.py", "tests/test_review_freshness.py",
             "docs/statement_evidence_contract.md", "corpus/README.md"]
    report = {
        "schema": "quartic-r3-backend-acceptance-v1",
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "script_sha256": digest(Path(__file__)),
        "scope": "Actual Python execution, mocked transition receipts, read-only supplied-corpus regeneration. No Lean, Comparator, native extraction or installed-consumer validation claimed.",
        "definition_edit_and_rebuild": {"operation_receipts": "mocked", "old_snapshot": hashes_before,
                                       "new_snapshot": hashes_after, "original": before_record,
                                       "patched": after_record},
        "derived_helper": {"original_wrong_source_id": old_helper_graph["nodes"][0]["source_id"],
                           "patched_rejection": helper_rejection},
        "missing_dependency": {"original_edges": old_missing["edges"],
                               "patched_rejection": dependency_rejection},
        "supplied_source_snapshot": {"inputs": len(original.source_hashes()),
                                     "snapshot_sha256": patched.canonical_sha256(original.source_hashes()),
                                     "unchanged_in_patch": True},
        "authored_and_recorded_inputs_unchanged": before_input_hashes,
        "original_corpus_dry_run": original_corpus,
        "patched_corpus_dry_run": patched_corpus,
        "test_runs": test_runs,
        "original_files": {path: digest(args.original / path) for path in files if (args.original / path).exists()},
        "patched_files": {path: digest(args.patched / path) for path in files if (args.patched / path).exists()},
    }
    (args.out / "backend-acceptance.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"tests": [{"label": run["label"], "exit_code": run["exit_code"]} for run in test_runs],
                      "patched_coverage": patched_corpus["coverage"],
                      "report": str(args.out / "backend-acceptance.json")}, indent=2))


if __name__ == "__main__":
    main()
