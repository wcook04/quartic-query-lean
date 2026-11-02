#!/usr/bin/env python3
"""Run proposed semantic checks on a separately prepared, pinned Lean project.

This program does not install tools, update dependencies, copy sources, or alter
the evidence registry. Copy this return's lean/QuarticCorpus/Independent folder
into a disposable pinned project's lean/QuarticCorpus before running it.

It reports missing runtime/inputs as not_run, not as expected Lean rejection.
The shared impossible-premise Comparator case is explicitly a blind-spot
demonstration; accepting it would not validate its intended mathematical meaning.
Source binding is delegated to the prepared repository's
tools/build_corpus.py::source_hashes(project.parent). A missing owner is an
explicit blocker; there is no independently maintained globbing fallback.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
BUILD_TARGETS = [
    "QuarticCorpus.Independent.Semantics",
    "QuarticCorpus.Independent.SemanticMutations",
    "QuarticCorpus.Independent.Controls.SharedAudit",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source_hash_owner(project: Path):
    """Reuse the repository-owned binding scope; never invent a partial fallback."""
    owner_path = project.parent / "tools" / "build_corpus.py"
    if not owner_path.is_file():
        raise RuntimeError(f"Required source-hash owner is unavailable: {owner_path}")
    spec = importlib.util.spec_from_file_location("quartic_r3_build_corpus_owner", owner_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load source-hash owner: {owner_path}")
    owner = importlib.util.module_from_spec(spec)
    old_bytecode_setting = sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode = True
        spec.loader.exec_module(owner)
    except Exception as exc:
        raise RuntimeError(f"Cannot import source-hash owner {owner_path}: {exc}") from exc
    finally:
        sys.dont_write_bytecode = old_bytecode_setting
    function = getattr(owner, "source_hashes", None)
    if not callable(function):
        raise RuntimeError(f"Source-hash owner lacks callable source_hashes: {owner_path}")
    return owner_path, function


def invoke(command: list[str], project: Path, output: Path, label: str) -> dict:
    record = {"command": command, "cwd": str(project), "ran_at":
              datetime.now(timezone.utc).isoformat()}
    try:
        result = subprocess.run(command, cwd=project, text=True, capture_output=True)
    except FileNotFoundError as exc:
        record.update(status="not_run", native_run_started=False,
                      exit_code=None, error=str(exc))
        return record
    log = result.stdout + result.stderr
    logpath = output / f"{label}.log"
    logpath.write_text(log, encoding="utf-8")
    record.update(status="command_completed", native_run_started=True,
                  exit_code=result.returncode, log=logpath.name,
                  log_sha256=digest(logpath))
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True,
                        help="Path to the prepared pinned project's lean directory")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--lake", default="lake")
    parser.add_argument("--unsandboxed-local", action="store_true",
                        help="Use Comparator's local-rehearsal flag for these known specimens")
    args = parser.parse_args()
    project, output = args.project.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "quartic-r3-semantic-run-v1",
        "run_started_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Actual-definition Lean tests and separately labelled Comparator controls.",
        "runner_sha256": digest(Path(__file__).resolve()),
        "status": "not_run",
        "commands": [],
        "cases": [],
        "limitations": [],
    }
    expected = json.loads((HERE / "source-hashes.json").read_text())
    baseline_files = ["QuarticQuery/Statement.lean", "QuarticQuery/Model/Classical.lean",
                      "lean-toolchain", "lakefile.toml", "lake-manifest.json"]
    mismatches = []
    for rel in baseline_files:
        path = project / rel
        wanted = expected[f"repository/lean/{rel}"]
        if not path.is_file() or digest(path) != wanted:
            mismatches.append(rel)
    report["frozen_input_mismatches"] = mismatches
    missing_overlay = []
    for supplied in sorted((HERE / "lean" / "QuarticCorpus" / "Independent").rglob("*")):
        if supplied.is_file():
            rel = supplied.relative_to(HERE / "lean")
            installed = project / rel
            if not installed.is_file() or digest(installed) != digest(supplied):
                missing_overlay.append(str(rel))
    report["missing_or_changed_overlay"] = missing_overlay
    try:
        owner_path, source_hashes = load_source_hash_owner(project)
        before = source_hashes(project.parent)
    except Exception as exc:
        report["status"] = "blocked_source_hash_owner"
        report["limitations"].append(str(exc))
        report["cases"] = [{"id": name, "status": "not_run",
                            "reason": "repository source-hash owner unavailable or failed"}
                           for name in ["actual_definition_semantics", "mutation_detection_proofs",
                                        "changed_threshold_comparator", "shared_impossible_comparator"]]
        (output / "run.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(json.dumps({"status": report["status"], "receipt": str(output / "run.json"),
                          "error": str(exc)}, indent=2))
        return 2
    report["source_hash_owner"] = {
        "path": str(owner_path), "sha256": digest(owner_path),
        "function": "source_hashes", "argument": str(project.parent),
        "scope": "Existing repository-owned source/configuration binding; no fallback globs.",
    }
    report["source_hashes_before"] = before
    version = invoke([args.lake, "--version"], project, output, "lake-version")
    report["commands"].append(version)
    if version.get("exit_code") != 0 or mismatches or missing_overlay:
        report["limitations"].append(
            "Native tests were not started: supply the pinned runtime, exact baseline, and overlay.")
        for name in ["actual_definition_semantics", "mutation_detection_proofs",
                     "changed_threshold_comparator", "shared_impossible_comparator"]:
            report["cases"].append({"id": name, "status": "not_run"})
    else:
        build = invoke([args.lake, "build", *BUILD_TARGETS], project, output, "semantic-build")
        report["commands"].append(build)
        built = build.get("exit_code") == 0
        report["cases"].append({"id": "actual_definition_semantics",
                                "status": "built" if built else "build_failed"})
        report["cases"].append({"id": "mutation_detection_proofs",
                                "status": "built" if built else "build_failed"})
        if built:
            inspect = invoke([args.lake, "env", "lean",
                              "QuarticCorpus/Independent/Inspect.lean"],
                             project, output, "semantic-inspection")
            report["commands"].append(inspect)
            report["inspection_completed"] = inspect.get("exit_code") == 0
            for name, config, expected_exit, diagnostic in [
                ("changed_threshold_comparator", "threshold_mutation.json", 1,
                 "Const does not match between challenge and target 'Round3.ThresholdSpec.Eligible'"),
                ("shared_impossible_comparator", "shared_blind_spot.json", 0, None),
            ]:
                command = [args.lake, "comparator", "--config",
                           f"QuarticCorpus/Independent/Controls/{config}"]
                if args.unsandboxed_local:
                    command.append("--inadvisably-no-sandbox")
                result = invoke(command, project, output, name)
                report["commands"].append(result)
                log = (output / result["log"]).read_text() if result.get("log") else ""
                matches = result.get("exit_code") == expected_exit
                if diagnostic:
                    matches = matches and diagnostic in log
                status = "unexpected_result"
                if not result.get("native_run_started"):
                    status = "not_run"
                elif matches:
                    status = ("rejected_as_expected" if expected_exit else
                              "accepted_shared_bad_spec_blind_spot")
                report["cases"].append({"id": name, "status": status,
                                        "expected_exit": expected_exit,
                                        "expected_diagnostic": diagnostic,
                                        "is_semantic_correctness_certificate": False})
        else:
            for name in ["changed_threshold_comparator", "shared_impossible_comparator"]:
                report["cases"].append({"id": name, "status": "not_run",
                                        "reason": "semantic build did not pass"})
    after = source_hashes(project.parent)
    report["source_hashes_after"] = after
    report["source_changed_during_run"] = before != after
    report["source_hash_owner_changed_during_run"] = (
        digest(owner_path) != report["source_hash_owner"]["sha256"])
    report["runner_changed_during_run"] = (
        digest(Path(__file__).resolve()) != report["runner_sha256"])
    statuses = {case["status"] for case in report["cases"]}
    allowed = {"built", "rejected_as_expected", "accepted_shared_bad_spec_blind_spot"}
    complete = bool(statuses) and statuses <= allowed
    complete = complete and report.get("inspection_completed", False) and before == after
    complete = complete and not report["source_hash_owner_changed_during_run"]
    complete = complete and not report["runner_changed_during_run"]
    report["status"] = "executed_as_expected" if complete else "incomplete_or_failed"
    report["sandboxed_comparator"] = not args.unsandboxed_local
    (output / "run.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": report["status"], "receipt": str(output / "run.json"),
                      "case_statuses": report["cases"]}, indent=2))
    return 0 if complete else 2


if __name__ == "__main__":
    sys.exit(main())
