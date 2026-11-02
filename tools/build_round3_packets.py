#!/usr/bin/env python3
"""Prepare at most ten focused round-three packets; build only from an approved digest.

External inputs are explicit. The default invocation validates inputs and prints
their freeze digest without writing ZIPs. Existing packet builders are unchanged.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from string import Formatter
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_corpus as corpus  # noqa: E402
import build_funnel_packets as funnel  # noqa: E402
import check_packets  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
JOBS = {
    "01_models_evidence": "Query models and the statement/evidence contract",
    "02_forrelation_promise_circuit": "The Forrelation promise and its quantum circuit",
    "03_forrelation_lower_bound": "The Forrelation randomized lower bound",
    "04_addressed_construction": "The addressed total-function construction",
    "05_quantum_upper": "The quantum upper bound",
    "06_direct_product": "The randomized direct-product argument",
    "07_planted_lower_bound": "The planted lower bound and its asymptotics",
    "08_quartic_appendix_exponent": "The quartic upper bound and the separation exponent",
    "09_evidence_backend": "The source-bound evidence backend",
    "10_baseline_record_review": "The baseline reasoning record and its assembly plan",
}
LITERATURE = {
    "01_models_evidence": ["quartic-lit-buhrman-dewolf-decision-tree-survey",
        "quartic-lit-dewolf-quantum-computing-lecture-notes",
        "quartic-ref-08-quantum-lower-bounds-by-polynomials"],
    "02_forrelation_promise_circuit": ["quartic-ref-01-forrelation-a-problem-that-optimally-separ",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum"],
    "03_forrelation_lower_bound": ["quartic-ref-06-k-forrelation-optimally-separates-quantum",
        "arxiv-2103-11604", "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
        "quartic-ref-26-towards-optimal-separations-between-quantu"],
    "04_addressed_construction": ["quartic-ref-02-separations-in-query-complexity-using-chea",
        "quartic-ref-04-separations-in-query-complexity-based-on-p"],
    "05_quantum_upper": ["quartic-ref-12-quantum-amplitude-amplification-and-estima",
        "quartic-ref-11-tight-bounds-on-quantum-searching",
        "quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu",
        "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error",
        "quartic-lit-dewolf-quantum-computing-lecture-notes"],
    "06_direct_product": ["quartic-ref-13-improved-direct-product-theorems-for-rando",
        "quartic-ref-22-towards-proving-strong-direct-product-theo"],
    "07_planted_lower_bound": ["quartic-ref-13-improved-direct-product-theorems-for-rando",
        "quartic-ref-02-separations-in-query-complexity-using-chea",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum"],
    "08_quartic_appendix_exponent": ["quartic-ref-03-degree-vs-approximate-degree-and-quantum-i",
        "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo",
        "quartic-ref-19-exact-quantum-query-complexity-for-total-b",
        "quartic-lit-hoyer-lee-spalek-negative-weights",
        "quartic-ref-24-all-quantum-adversary-methods-are-equivale"],
    "09_evidence_backend": [],
    "10_baseline_record_review": ["quartic-ref-03-degree-vs-approximate-degree-and-quantum-i",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum", "arxiv-2103-11604",
        "quartic-ref-12-quantum-amplitude-amplification-and-estima",
        "quartic-ref-13-improved-direct-product-theorems-for-rando"],
}
# Patterns identify the primary read, not a new dependency or evidence registry.
FOCUS = {
    "01_models_evidence": ["lean/QuarticQuery/Model/*.lean", "lean/QuarticQuery/Bridge/*.lean",
        "docs/statement_evidence_contract.md", "tools/return_checks/semantic_controls.py"],
    "02_forrelation_promise_circuit": ["lean/QuarticQuery/Forrelation/*.lean",
        "lean/QuarticQuery/Upper/Decode.lean", "lean/QuarticQuery/Paper/Section2.lean",
        "lean/QuarticQuery/Paper/ConstructionForrelation*.lean",
        "lean/QuarticQuery/Paper/ConstructionArithmetic.lean"],
    "03_forrelation_lower_bound": ["lean/QuarticQuery/ForrelationLower/*.lean",
        "docs/forrelation_lower_bound_blueprint.md", "docs/forrelation_lower_bound_review.md",
        "docs/forrelation_route_prior_art.md"],
    "04_addressed_construction": ["lean/QuarticQuery/Construction/*.lean",
        *[f"lean/QuarticQuery/Paper/Construction{name}.lean" for name in
          ("Definitions", "Tests", "PointerSupport", "Coherent", "Complete")]],
    "05_quantum_upper": ["lean/QuarticQuery/Amplification/*.lean",
        "lean/QuarticQuery/Tournament/*.lean", "lean/QuarticQuery/Paper/Quantum*.lean",
        *[f"lean/QuarticQuery/Upper/{name}.lean" for name in
          ("Sampler", "Compile", "Amplify", "Tournament", "Columns", "Verify")]],
    "06_direct_product": ["lean/QuarticQuery/LowerBound/DirectProduct.lean",
        "lean/QuarticQuery/LowerBound/Minimax.lean",
        "lean/QuarticQuery/Paper/ClassicalDirectProduct.lean"],
    "07_planted_lower_bound": ["lean/QuarticQuery/LowerBound/Planted/*.lean",
        *[f"lean/QuarticQuery/Paper/Classical{name}.lean" for name in
          ("Planted", "UniformZero", "Asymptotics")]],
    "08_quartic_appendix_exponent": ["lean/QuarticQuery/Appendix/TheoremA1.lean",
        "lean/QuarticQuery/Paper/AppendixA*.lean", "lean/QuarticQuery/Results/*.lean"],
    "09_evidence_backend": ["tools/build_corpus.py", "tools/build_challenges.py",
        "tools/record_evidence.py", "tools/run_comparator.py", "lean/scripts/Reach.lean",
        "tests/test_build_corpus.py", "tests/test_record_evidence.py",
        "tests/test_build_challenges.py", "corpus/README.md", "docs/statement_evidence_contract.md",
        "lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean",
        "lean/QuarticQuery/Paper/ClassicalPlanted.lean", "tools/return_checks/semantic_controls.py"],
    "10_baseline_record_review": ["research/returns/funnel/1_long_reasoning_record/*",
        "research/returns/funnel/2_short_expert_paper/paper.md",
        "research/returns/funnel/3_examples_first_exposition/exposition.md"],
}
RETURNS = {
    "01_models_evidence": ["round2/1_statement_fidelity"],
    "02_forrelation_promise_circuit": ["round2/2_lean_construction"],
    "03_forrelation_lower_bound": ["funnel/4_forrelation_route_note", "round2/6_sharp_uniform_forrelation"],
    "04_addressed_construction": ["round2/2_lean_construction"],
    "05_quantum_upper": ["round2/3_lean_quantum_upper"],
    "06_direct_product": ["round2/4_lean_classical_lower"],
    "07_planted_lower_bound": ["round2/4_lean_classical_lower"],
    "08_quartic_appendix_exponent": ["round2/5_lean_appendix_a", "round2/7_single_family_exponent"],
    "09_evidence_backend": ["funnel/5_reader_and_film"],
    "10_baseline_record_review": ["funnel/2_short_expert_paper", "funnel/3_examples_first_exposition"],
}
GUIDES = ("the-deliverable.md", "mathematical-writing-mechanics.md",
          "full-exposition-guide.md", "register-from-literature.md")
SOURCE_SUFFIXES = {".md", ".json", ".lean", ".py", ".bib", ".txt", ".pdf", ".sha256"}
LITERATURE_SUPPLEMENTS = {
    "quartic-ref-24-all-quantum-adversary-methods-are-equivale": ["supplements/toc-2006-supplied.pdf"],
}
LITERATURE_ROLES = {
    "quartic-lit-buhrman-dewolf-decision-tree-survey": "Survey comparison for classical query-model conventions.",
    "quartic-lit-dewolf-quantum-computing-lecture-notes": "Quantum query-model and algorithm conventions; explanatory comparison.",
    "quartic-ref-08-quantum-lower-bounds-by-polynomials": "Polynomial-method source for comparing statement and model conventions.",
    "quartic-ref-01-forrelation-a-problem-that-optimally-separ": "Forrelation antecedent: promise and circuit comparison.",
    "quartic-ref-06-k-forrelation-optimally-separates-quantum": "k-fold Forrelation definitions and imported randomized lower bound; Thm 1.3 and section 5.4.",
    "arxiv-2103-11604": "Ordinary-tree martingale proof component; Lemma 1.9, not an automatically interchangeable model.",
    "quartic-ref-23-an-optimal-separation-of-randomized-and-qu": "Forrelation lower-bound comparison, including Corollary 4.14.",
    "quartic-ref-26-towards-optimal-separations-between-quantu": "Comparison with stronger Forrelation separation statements; inspect parameter scope.",
    "quartic-ref-02-separations-in-query-complexity-using-chea": "Cheat-sheet construction antecedent, not a proof of the current addressed construction.",
    "quartic-ref-04-separations-in-query-complexity-based-on-p": "Pointer-function construction antecedent and comparison.",
    "quartic-ref-12-quantum-amplitude-amplification-and-estima": "Amplitude amplification source: section 2, Lemma 1/equation (8), and Theorem 12 where applicable.",
    "quartic-ref-11-tight-bounds-on-quantum-searching": "Quantum-search bounds and algorithmic background.",
    "quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu": "Minimum-finding/tournament algorithm background.",
    "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error": "Search with bounded-error inputs; compare its exact assumptions with the current verifier.",
    "quartic-ref-13-improved-direct-product-theorems-for-rando": "Direct-product proof source, especially Lemmas 3.1–3.2; capped and global budgets differ.",
    "quartic-ref-22-towards-proving-strong-direct-product-theo": "Fair-XOR antecedent; distinguish its route and budget hypotheses.",
    "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i": "Universal quartic upper-bound source, Theorem 2.",
    "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo": "Hypercube sensitivity theorem used in the Appendix A route.",
    "quartic-ref-19-exact-quantum-query-complexity-for-total-b": "Deterministic complexity versus degree bound and coefficient comparison.",
    "quartic-lit-hoyer-lee-spalek-negative-weights": "Adversary-bound comparison/corroboration; separate from the unavailable BSS original.",
    "quartic-ref-24-all-quantum-adversary-methods-are-equivale": "Supplied publisher edition for adversary equivalence/coefficient comparison; separate from BSS.",
}
BACKEND_REQUIRED = {
    "lean-exposition": ["lean-exposition/" + name for name in (
        "src/lean_exposition/resources/schemas/graph.schema.json",
        "src/lean_exposition/resources/schemas/artifact.schema.json",
        "src/lean_exposition/resources/schemas/bundle.schema.json", "docs/contracts.md",
        "docs/verification.md", "src/lean_exposition/contracts.py", "src/lean_exposition/cli.py",
        "src/lean_exposition/extraction.py", "src/lean_exposition/consumer.py",
        "src/lean_exposition/verification.py")],
    "comparator": [],  # At least one explicitly identified primary source/doc member is required.
}


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def compose_request(job, common, body, boundary):
    fields = sorted(field for _, field, _, _ in Formatter().parse(common) if field is not None)
    if fields != ["boundary", "job", "title"]:
        raise ValueError("round-three common.md needs {title}, {job}, {boundary} exactly once")
    return common.format(title=JOBS[job], job=body, boundary=boundary)


def render_request(job, requests_dir):
    return compose_request(job, *[(requests_dir / name).read_text(encoding="utf-8")
        for name in ("common.md", f"{job}.md", "boundaries.md")])


def backend_status(sources, unavailable):
    unknown = set(unavailable) - set(BACKEND_REQUIRED)
    if unknown or any(not isinstance(reason, str) or not reason.strip() for reason in unavailable.values()):
        raise ValueError("backend unavailability needs a nonempty reason for lean-exposition or comparator")
    rows = []
    for group, required in BACKEND_REQUIRED.items():
        supplied = sorted(name for name in sources if name.startswith(group + "/"))
        missing = sorted(set(required) - set(sources))
        complete = bool(supplied) and not missing
        if not complete and group not in unavailable:
            raise ValueError(f"job 09 requires actual {group} contracts or an explicit --backend-unavailable reason")
        rows.append({"group": group, "status": "supplied" if complete else "incomplete_or_unavailable",
            "supplied_members": ["external_backend/" + name for name in supplied], "missing_required": missing,
            "limitation": unavailable.get(group) if not complete else None})
    return {"groups": rows, "interpretation": "Any incomplete group limits the assignment: mark its dependent "
            "native extraction/validation unassessed, and do not invent contract behavior from a missing source."}


def inputs(job, *, root, requests_dir, paper_annex, annexes, writing_skill,
           writing_guides, exemplar_repo, exemplar_ref, backend_sources=None,
           backend_unavailable=None, native_results=None, native_logs=None, native_sources=None):
    """Map portable members to (source, role), without reading ignored build trees."""
    if job not in JOBS:
        raise ValueError(f"unknown packet: {job}")
    if job == "09_evidence_backend":
        backend_status(backend_sources or {}, backend_unavailable or {})
    out = {}

    def add(name, source, role):
        check_packets.check_name(name)
        if name.casefold() in {key.casefold() for key in out}:
            raise ValueError(f"duplicate input member: {name}")
        if not isinstance(source, tuple) and not source.is_file():
            raise ValueError(f"missing required source: {source}")
        out[name] = (source, role)

    def repository(path, role):
        name = "repository/" + path.relative_to(root).as_posix()
        if name in out:
            if role == "primary_read":
                out[name] = (path, role)
            return
        add(name, path, role)

    def tree(folder, role):
        if not folder.is_dir():
            raise ValueError(f"missing required source directory: {folder}")
        for path in sorted(folder.rglob("*")):
            if path.is_file() and (path.suffix in SOURCE_SUFFIXES or path.name in {"LICENSE", "NOTICE"}) and not any(
                    part.startswith(".") or part == "__pycache__" for part in path.relative_to(folder).parts):
                repository(path, role)

    for name in ("README.md", "AGENTS.md", "CONTRIBUTING.md", "LICENSE", "Makefile",
                 "lean/README.md", "corpus/README.md", "research/returns/README.md",
                 "research/returns/round2/README.md", "research/returns/round2/intake.json",
                 "research/README.md", "research/intake/statement_ledger.json"):
        repository(root / name, "repository_context")
    for name in corpus.source_hashes(root):
        repository(root / name, "local_lean_and_pinned_configuration")
    for folder, role in ((root / "corpus", "recorded_evidence"),
                         (root / "research/adjudication", "maintained_adjudication"),
                         (root / "research/returns/funnel/1_long_reasoning_record", "baseline_advisory_return")):
        tree(folder, role)
    for folder in RETURNS[job]:
        tree(root / "research/returns" / folder, "prior_advisory_return")
    for pattern in ["lean/QuarticQuery/Statement.lean", *FOCUS[job]]:
        matches = sorted(path for path in root.glob(pattern) if path.is_file())
        if not matches:
            raise ValueError(f"primary source pattern has no files: {pattern}")
        for path in matches:
            repository(path, "primary_read")
    # Include executable evidence consumers so the receiver can inspect the raw contract.
    for path in sorted((root / "tools").glob("*.py")):
        repository(path, "evidence_and_packaging_tool_source")
    for name in ("common.md", "boundaries.md", "SELECTION.md", f"{job}.md"):
        add(f"requests/{name}", requests_dir / name, "authored_request")
    for name in ("source.pdf", "extracted.md"):
        add("paper/" + name, paper_annex / name, "primary_preprint")
    if (paper_annex / "annex_notes.json").is_file():
        add("paper/annex_notes.json", paper_annex / "annex_notes.json", "supplied_preprint_provenance")
    if (paper_annex / "source.tar.gz").is_file():
        add("paper/source.tar.gz", paper_annex / "source.tar.gz", "primary_preprint_tex")
    for slug in LITERATURE[job]:
        folder = annexes / slug
        add(f"literature/{slug}/extracted.md", folder / "extracted.md", "primary_literature_text")
        originals = [name for name in ("source.pdf", "source.tar.gz", "source.tex")
                     if (folder / name).is_file()]
        for name in LITERATURE_SUPPLEMENTS.get(slug, []):
            if not (folder / name).is_file():
                raise ValueError(f"missing selected literature edition: {folder / name}")
            originals.append(name)
        if not originals:
            raise ValueError(f"selected literature lacks original PDF or TeX source: {folder}")
        for name in [*originals, "annex_notes.json"]:
            if (folder / name).is_file():
                add(f"literature/{slug}/{name}", folder / name,
                    "literature_locator" if name == "annex_notes.json" else "primary_literature_original")
    add("writing/SKILL.md", writing_skill, "writing_guidance")
    for name in GUIDES:
        add("writing/" + name, writing_guides / name, "writing_guidance")
    for name, path in funnel.EXEMPLARS.items():
        add(name, (exemplar_repo, exemplar_ref, path), "style_exemplar_not_mathematical_evidence")
    if job == "09_evidence_backend":
        for name, path in sorted((backend_sources or {}).items()):
            add("external_backend/" + name, path, "external_tool_contract_source")
    for name, path in sorted((native_results or {}).items()):
        if not name.endswith(".json"):
            raise ValueError("native result members must be JSON records")
        add("native_results/" + name, path, "native_run_record_not_corpus_receipt")
    for name, path in sorted((native_logs or {}).items()):
        add("native_logs/" + name, path, "native_run_log")
    for name, path in sorted((native_sources or {}).items()):
        add("native_sources/" + name, path, "explicit_native_run_source")
    return out


def native_binding(row, hashes, root, extra_sources):
    """Compare an explicitly scoped native binding with included bytes only."""
    recorded = row.get("inputs_before", row.get("source_hashes"))
    if not isinstance(recorded, dict) or not recorded:
        return {"source_currentness": "legacy_unbound", "input_members": {}, "unresolved_inputs": []}
    if not all(isinstance(key, str) and isinstance(value, str) for key, value in recorded.items()):
        raise ValueError("native input bindings must map source labels to hash strings")
    members, unresolved, mismatches = {}, [], []
    for label, expected in recorded.items():
        key = label
        if Path(label).is_absolute():
            try:
                key = Path(label).relative_to(root).as_posix()
            except ValueError:
                key = None
        if key in hashes:
            member, actual = "repository/" + key, hashes[key]
        elif label in extra_sources:
            member, actual = extra_sources[label]
        else:
            unresolved.append(label)
            continue
        members[member] = expected
        if actual != expected:
            mismatches.append(member)
    if row.get("inputs_unchanged") is False:
        state = "inputs_changed_during_run"
    elif mismatches:
        state = "stale"
    elif unresolved:
        state = "unresolved_source_labels"
    elif "inputs_before" in row and row.get("inputs_unchanged") is not True:
        state = "input_stability_unrecorded"
    elif set(members) == {"repository/" + name for name in hashes}:
        state = "current"
    else:
        state = "current_for_recorded_inputs_only"
    return {"source_currentness": state, "input_members": members,
            "unresolved_inputs": unresolved, "mismatched_members": mismatches}


def evidence_snapshot(data, hashes, root, extra_sources=None):
    """Reclassify saved records against packet source bytes, not generated booleans."""
    receipts = []
    for name, blob in sorted(data.items()):
        if name.startswith("repository/corpus/receipts/") and name.endswith(".json"):
            row = json.loads(blob)
            receipts.append({key: row.get(key) for key in
                ("kind", "name", "status", "commit", "ran_at", "declarations", "negative_control")})
            receipts[-1].update(member=name, sha256=digest(blob),
                source_currentness=corpus.currentness(row, hashes))
    closure = json.loads(data["repository/corpus/lean_dependencies.json"])
    native = []
    for name, blob in sorted(data.items()):
        if name.startswith("native_results/"):
            row = json.loads(blob)
            if not isinstance(row, dict):
                raise ValueError(f"{name}: native result must be an object")
            entries = row.get("results", [row])
            if not isinstance(entries, list) or not all(isinstance(entry, dict) for entry in entries):
                raise ValueError(f"{name}: native results must be a list of objects")
            for entry in entries:
                native.append({"member": name, "sha256": digest(blob),
                    "target": entry.get("target"), "status": entry.get("status", "unspecified"),
                    "exit_code": entry.get("exit_code"), "log": entry.get("log"),
                    **native_binding(entry, hashes, root, extra_sources or {}),
                    "scope": "Scoped native run only; not declaration membership, Comparator or a global root build. "
                    "Absolute labels map only under the selected repository or to explicitly supplied native sources."})
    return {"format": "round3-packet-evidence-snapshot-v1", "source_hashes": hashes,
        "dependency_export": {"member": "repository/corpus/lean_dependencies.json",
            "sha256": digest(data["repository/corpus/lean_dependencies.json"]),
            "source_currentness": corpus.currentness(closure, hashes),
            "roots": closure.get("roots", []), "reached": closure.get("reached", [])},
        "receipts": receipts, "native_results": native,
        "interpretation": "Only passed, current receipts with exact declaration membership support "
            "a current result. Source presence, generated corpus booleans and artifact times do not. "
            "Pending/running/failed statuses remain as recorded; absence of a receipt does not imply a live build."}


def build_status(snapshot):
    lines = ["# Build status for the frozen packet inputs", "", snapshot["interpretation"], "",
        "The dependency export is `" + snapshot["dependency_export"]["source_currentness"] + "`. "
        "Reached membership is current only for a current export; a missing name in a stale or "
        "legacy export establishes no current exclusion.", "",
        "No build was run by this packet builder. Raw receipts and the source-bound reclassification "
        "are in `repository/corpus/` and `EVIDENCE_SNAPSHOT.json`. Compilation and mathematical "
        "fidelity remain separate judgments. `.olean` existence and mtime are not used.", "",
        "| Receipt | Recorded status | Source currentness |", "| --- | --- | --- |"]
    for row in snapshot["receipts"]:
        lines.append(f"| `{row['member']}` | `{row['status']}` | `{row['source_currentness']}` |")
    if not snapshot["receipts"]:
        lines += ["", "No saved receipts were supplied; build status is unknown."]
    if snapshot["native_results"]:
        lines += ["", "## Optional native run records", "",
            "These raw records and explicitly supplied logs preserve the native run's actual scope. "
            "A matching subset of hashes binds only the recorded inputs, not the full aggregate. "
            "A record without a source binding remains unbound even when its log names current paths.", ""]
        lines += [f"- `{row['member']}` / `{row['target']}`: recorded status `{row['status']}`, binding `{row['source_currentness']}`."
                  for row in snapshot["native_results"]]
    return ("\n".join(lines) + "\n").encode()


def literature_guide(job):
    lines = ["# Selected primary literature", ""]
    for i, slug in enumerate(LITERATURE[job], 1):
        lines.append(f"{i}. `{slug}`: {LITERATURE_ROLES.get(slug, 'Primary source selected by this job.')} "
                     "Read its original PDF/TeX with `extracted.md`; locator notes do not replace the paper.")
    lines += ["", "The OpenAI preprint is in `paper/`. No unselected annex is bundled. "
              "These local source copies do not establish public redistribution rights."]
    if "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error" in LITERATURE[job]:
        lines += ["", "File names are preserved: the bounded-error-search source.tar.gz is gzip-compressed "
                  "single TeX, despite that name."]
    if "quartic-ref-24-all-quantum-adversary-methods-are-equivale" in LITERATURE[job]:
        lines += ["", "The BSS original is not supplied; Høyer–Lee–Špalek and Špalek–Szegedy are separate "
                  "sources, not a substitute attributed to BSS."]
    return ("\n".join(lines) + "\n").encode()


def prepare(job, **options):
    """Read a complete immutable in-memory packet; fail if any input changes."""
    before_hashes = corpus.source_hashes(options["root"])
    files = inputs(job, **options)
    data = {name: funnel.content(source) for name, (source, _) in files.items()}
    request = compose_request(job, *[data["requests/" + name].decode("utf-8")
        for name in ("common.md", f"{job}.md", "boundaries.md")])
    fingerprint = {name: digest(blob) for name, blob in data.items()}
    # Regather names too: newly created source/receipt files must invalidate the freeze.
    after = inputs(job, **options)
    if (files != after or fingerprint != {name: digest(funnel.content(source))
            for name, (source, _) in after.items()}
            or before_hashes != corpus.source_hashes(options["root"])):
        raise ValueError("packet inputs changed while being read; freeze again")
    extra_sources = {str(source): (name, digest(data[name]))
        for name, (source, _) in files.items() if name.startswith("native_sources/")}
    snapshot = evidence_snapshot(data, before_hashes, options["root"], extra_sources)
    data["EVIDENCE_SNAPSHOT.json"] = encoded(snapshot)
    data["BUILD_STATUS.md"] = build_status(snapshot)
    if job == "09_evidence_backend":
        data["BACKEND_INPUT_STATUS.json"] = encoded(backend_status(
            options.get("backend_sources") or {}, options.get("backend_unavailable") or {}))
    focus = sorted({"repository/" + p.relative_to(options["root"]).as_posix()
        for pattern in ["lean/QuarticQuery/Statement.lean", *FOCUS[job]]
        for p in options["root"].glob(pattern) if p.is_file()})
    data["SOURCE_ROLES.md"] = ("# Source roles and reading order\n\n" + JOBS[job] + "\n\n"
        "Start with the authored request and the primary read below. The complete local Lean/config "
        "snapshot supports source-hash auditing; its presence does not establish compilation. Prior "
        "returns are advisory historical submissions, and maintained adjudications control acceptance. "
        "Literature folders contain full selected texts and available originals, not the whole annex.\n\n"
        + "\n".join("- `" + name + "`" for name in focus) + "\n\n"
        "Read `writing/the-deliverable.md` and the other included writing texts directly. Any private "
        "runtime paths or commands mentioned in their original prose are provenance, not prerequisites "
        "for this task. Use these enclosed bytes and the request; no private runtime is needed. "
        "Exemplars show writing structure only and supply no mathematical evidence for this paper.\n\n"
        "This is a focused research snapshot, not a full repository checkout or a promise that "
        "`make check` can run after extraction. In particular, round-two custody inputs are selected "
        "context and do not include every source archive governed by their original intake manifest. "
        "Use a full checkout for repository-wide checks. For job 09, inspect `BACKEND_INPUT_STATUS.json` "
        "before attempting the external extraction/validation assignment; explicit unavailable groups "
        "limit what the supplied sources support.\n").encode()
    data["literature/README.md"] = literature_guide(job)
    rows = [{"member": name, "source": str(files[name][0]), "role": files[name][1],
             "bytes": len(blob), "sha256": digest(blob)} for name, blob in data.items() if name in files]
    rows += [{"member": name, "source": "generated from hashed packet inputs", "role": "packet_navigation" if
              name != "EVIDENCE_SNAPSHOT.json" else "source_bound_evidence_reclassification",
              "bytes": len(blob), "sha256": digest(blob)} for name, blob in data.items() if name not in files]
    commit = subprocess.run(["git", "-C", str(options["root"]), "rev-parse", "HEAD"],
                            check=True, capture_output=True, text=True).stdout.strip()
    manifest = {"packet": job, "title": JOBS[job], "campaign": "round3", "repository_commit": commit,
        "source_paper": "Supplied preprint PDF, SHA-256 " + digest(data["paper/source.pdf"]),
        "paper_provenance": {"pdf_member": "paper/source.pdf", "sha256": digest(data["paper/source.pdf"]),
            "supplied_annex": str(options["paper_annex"]),
            "metadata_member": "paper/annex_notes.json" if "paper/annex_notes.json" in data else None},
        "primary_read": focus,
        "literature_roles": [{"slug": slug, "role": LITERATURE_ROLES.get(slug, "Primary source selected by this job.")}
                             for slug in LITERATURE[job]],
        "request_sha256": digest(request.encode()), "input_sha256": fingerprint, "members": rows}
    return {"data": data, "request": request, "manifest": manifest, "sources": files}


def batch_digest(prepared):
    return digest(encoded({job: packet["manifest"] for job, packet in sorted(prepared.items())}))


def prepare_batch(jobs, **options):
    if not jobs or len(jobs) != len(set(jobs)) or len(jobs) > 10:
        raise ValueError("select between one and ten distinct jobs")
    packets = {job: prepare(job, **options) for job in jobs}
    for job, packet in packets.items():
        current = inputs(job, **options)
        if (current != packet["sources"] or {name: digest(funnel.content(source))
                for name, (source, _) in current.items()} != packet["manifest"]["input_sha256"]):
            raise ValueError("packet inputs changed across the batch; freeze again")
    return packets


def write_archive(path, packet):
    """Use the established manifest contract and independent checker; never overwrite."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("READ_ME_FIRST.md", packet["request"])
        archive.writestr("manifest.json", encoded(packet["manifest"]))
        for name, blob in packet["data"].items():
            archive.writestr(name, blob)
    check_packets.audit(path)


def build_batch(jobs, dest, freeze_digest, **options):
    dest = dest.resolve()
    root = options["root"].resolve()
    if dest == root or root in dest.parents:
        raise ValueError("keep output ZIPs outside the repository")
    paths = [dest / f"quartic_r3_{job}.zip" for job in jobs]
    if any(os.path.lexists(path) for path in paths):
        raise FileExistsError("destination already contains a selected archive; choose a new directory")
    prepared = prepare_batch(jobs, **options)
    if batch_digest(prepared) != freeze_digest:
        raise ValueError("inputs differ from the approved freeze digest; validate and approve again")
    dest.mkdir(parents=True, exist_ok=True)
    temporary = []
    published = []
    try:
        for path, packet in zip(paths, prepared.values()):
            with tempfile.NamedTemporaryFile(prefix=".quartic-r3-", suffix=".zip", dir=dest, delete=False) as stream:
                tmp = Path(stream.name)
            temporary.append(tmp)
            write_archive(tmp, packet)
        if batch_digest(prepare_batch(jobs, **options)) != freeze_digest:
            raise ValueError("packet inputs changed during packaging; no archives retained")
        for path, tmp in zip(paths, temporary):
            os.link(tmp, path)  # Atomic exclusive publication, including a concurrent destination race.
            published.append(path)
        return paths
    except BaseException:
        for path in published:
            path.unlink()
        raise
    finally:
        for path in temporary:
            path.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--requests-dir", type=Path)
    parser.add_argument("--paper-annex", type=Path, required=True)
    parser.add_argument("--annexes", type=Path, required=True)
    parser.add_argument("--writing-skill", type=Path, required=True)
    parser.add_argument("--writing-guides", type=Path, required=True)
    parser.add_argument("--exemplar-repo", type=Path, required=True)
    parser.add_argument("--exemplar-ref", required=True, help="Git commit or ref; resolved to an immutable commit")
    parser.add_argument("--backend-source", action="append", default=[], metavar="MEMBER=PATH",
                        help="actual external schema/contract source, included only in job 09")
    parser.add_argument("--backend-unavailable", action="append", default=[], metavar="GROUP=REASON",
                        help="explicit job 09 limitation for lean-exposition or comparator inputs")
    parser.add_argument("--native-result", action="append", default=[], metavar="MEMBER=PATH",
                        help="optional raw native run JSON, included without promoting it to a corpus receipt")
    parser.add_argument("--native-log", action="append", default=[], metavar="MEMBER=PATH",
                        help="optional raw log explicitly accompanying native run records")
    parser.add_argument("--native-source", action="append", default=[], metavar="MEMBER=PATH",
                        help="optional actual native fixture/runner source outside the repository")
    parser.add_argument("--only", nargs="+", choices=sorted(JOBS), help="omit to select all ten")
    parser.add_argument("--dest", type=Path)
    parser.add_argument("--build", action="store_true", help="write ZIPs after approved input freeze")
    parser.add_argument("--freeze-digest", help="exact digest printed by the validation invocation")
    args = parser.parse_args(argv)
    if args.build and (not args.dest or not args.freeze_digest):
        parser.error("--build requires --dest and --freeze-digest")
    try:
        def named_sources(items):
            sources = {}
            for item in items:
                name, separator, path = item.partition("=")
                check_packets.check_name(name)
                if not separator or not path or name.casefold() in {key.casefold() for key in sources}:
                    raise ValueError("source options need distinct MEMBER=PATH pairs")
                sources[name] = Path(path).resolve()
            return sources
        resolved = subprocess.run(["git", "-C", str(args.exemplar_repo), "rev-parse",
            "--verify", args.exemplar_ref + "^{commit}"], check=True, capture_output=True, text=True).stdout.strip()
        unavailable = {}
        for item in args.backend_unavailable:
            group, separator, reason = item.partition("=")
            if not separator or group in unavailable:
                raise ValueError("--backend-unavailable needs distinct GROUP=REASON pairs")
            unavailable[group] = reason
        options = dict(root=args.root.resolve(), requests_dir=(args.requests_dir or
            args.root / "research/requests/round3").resolve(), paper_annex=args.paper_annex.resolve(),
            annexes=args.annexes.resolve(), writing_skill=args.writing_skill.resolve(),
            writing_guides=args.writing_guides.resolve(), exemplar_repo=args.exemplar_repo.resolve(),
            exemplar_ref=resolved, backend_sources=named_sources(args.backend_source),
            backend_unavailable=unavailable,
            native_results=named_sources(args.native_result), native_logs=named_sources(args.native_log),
            native_sources=named_sources(args.native_source))
        jobs = args.only or list(JOBS)
        if args.build:
            for path in build_batch(jobs, args.dest, args.freeze_digest, **options):
                print(f"PASS {path}")
        else:
            prepared = prepare_batch(jobs, **options)
            print(f"Validated {len(prepared)} packet inputs; no ZIPs written.")
            print("Freeze digest: " + batch_digest(prepared))
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"FAIL: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
