#!/usr/bin/env python3
"""Freeze seven independent round-four jobs; build only after accepted record review."""

import argparse
import json
import os
import re
import posixpath
from pathlib import Path
import subprocess
import sys
import tempfile
from functools import lru_cache
import zipfile
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_round3_packets as previous
import check_repository as repository_checks

ROOT = Path(__file__).resolve().parents[1]
JOBS = {
    "02_short_expert": "A complete expert companion to the reviewed reasoning record",
    "03_examples_first": "A complete examples-first mathematical companion",
    "04_quantum_completion": "Coherent physical quantum completion across the construction",
    "05_classical_completion": "Classical-model and adaptive proof completion",
    "06_corpus_fidelity": "Whole-corpus fidelity and independent specifications",
    "07_publication_backend": "The existing evidence-to-publication backend in real use",
    "08_adversarial_audit": "Adversarial mathematics, comprehension and repair audit",
}
FOCUS = {
    "02_short_expert": ["lean/QuarticQuery.lean", "lean/QuarticQuery/Results/*.lean"],
    "03_examples_first": ["lean/QuarticQuery/Construction/*.lean", "lean/QuarticQuery/Upper/*.lean"],
    "04_quantum_completion": ["lean/QuarticQuery/Amplification/*.lean", "lean/QuarticQuery/Upper/*.lean",
        "lean/QuarticQuery/Paper/Quantum*.lean", "lean/QuarticQuery/Paper/ConstructionPhase.lean",
        "lean/QuarticQuery/Paper/ConstructionForrelation*.lean", "lean/QuarticQuery/Forrelation/*.lean"],
    "05_classical_completion": ["lean/QuarticQuery/LowerBound/*.lean", "lean/QuarticQuery/LowerBound/Planted/*.lean",
        "lean/QuarticQuery/Paper/Classical*.lean", "lean/QuarticQuery/Paper/Eq19*.lean"],
    "06_corpus_fidelity": ["lean/QuarticQuery.lean", "lean/QuarticQuery/Statement.lean",
        "lean/QuarticCorpus/Independent/**/*.lean", "corpus/statements.json", "docs/statement_evidence_contract.md"],
    "07_publication_backend": ["tools/build_corpus.py", "tools/record_evidence.py", "tools/run_comparator.py",
        "docs/statement_evidence_contract.md", "docs/reasoning_record_correspondence.json", "corpus/native_extractions/**/*.json"],
    "08_adversarial_audit": ["lean/QuarticQuery/Statement.lean", "lean/QuarticQuery/Results/*.lean",
        "lean/QuarticCorpus/Independent/**/*.lean"],
}
BASELINES = ["funnel/2_short_expert_paper/paper.md", "funnel/3_examples_first_exposition/exposition.md"]
CIRCUIT_RETURN = "round3/members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/"
APPENDIX_RETURN = "round3/members/08_reviewed/quartic_r3_08_return/"
RETURNS = {
    "02_short_expert": [BASELINES[0]], "03_examples_first": [BASELINES[1]],
    "04_quantum_completion": [CIRCUIT_RETURN + "LEAN_GAPS.md", CIRCUIT_RETURN + "section.md",
        "round3/members/05_quantum_upper/LEAN_GAPS.md", "round3/members/05_quantum_upper/section.md"],
    "05_classical_completion": ["round3/members/06_direct_product/LEAN_GAPS.md", "round3/members/06_direct_product/section.md",
        "round3/members/07_planted_lower_bound/LEAN_GAPS.md", "round3/members/07_planted_lower_bound/section.md"],
    "06_corpus_fidelity": ["round3/members/01_models_evidence/model_contract.json", APPENDIX_RETURN + "LEAN_GAPS.md",
        "round3/members/09_evidence_backend/LEAN_GAPS.md", "round3/members/09_evidence_backend/acceptance_cases.json"],
    "07_publication_backend": ["round3/members/09_evidence_backend/evidence-path.md",
        "round3/members/09_evidence_backend/backend/backend_notes.md",
        "round3/members/09_evidence_backend/backend/backend.patch",
        "round3/members/09_evidence_backend/backend/run_backend_acceptance.py",
        "round3/members/09_evidence_backend/backend/backend_acceptance_cases.json",
        "round3/members/09_evidence_backend/LEAN_GAPS.md", *BASELINES],
    "08_adversarial_audit": [*BASELINES, "round3/members/01_models_evidence/model_contract.json",
        CIRCUIT_RETURN + "LEAN_GAPS.md", "round3/members/04_addressed_construction/LEAN_GAPS.md",
        "round3/members/05_quantum_upper/LEAN_GAPS.md", "round3/members/06_direct_product/LEAN_GAPS.md",
        "round3/members/07_planted_lower_bound/LEAN_GAPS.md", APPENDIX_RETURN + "LEAN_GAPS.md"],
}
CORE_LITERATURE = ["quartic-ref-06-k-forrelation-optimally-separates-quantum", "arxiv-2103-11604",
    "quartic-ref-12-quantum-amplitude-amplification-and-estima", "quartic-ref-13-improved-direct-product-theorems-for-rando",
    "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i"]
WRITING_LITERATURE = [*CORE_LITERATURE, "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
    "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-ref-04-separations-in-query-complexity-based-on-p",
    "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo", "quartic-lit-hoyer-lee-spalek-negative-weights",
    "quartic-ref-24-all-quantum-adversary-methods-are-equivale"]
LITERATURE = {
    "02_short_expert": WRITING_LITERATURE, "03_examples_first": WRITING_LITERATURE,
    "04_quantum_completion": ["quartic-ref-01-forrelation-a-problem-that-optimally-separ",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum", "quartic-ref-12-quantum-amplitude-amplification-and-estima",
        "quartic-ref-11-tight-bounds-on-quantum-searching", "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error",
        "quartic-lit-dewolf-quantum-computing-lecture-notes"],
    "05_classical_completion": ["quartic-ref-13-improved-direct-product-theorems-for-rando",
        "quartic-ref-22-towards-proving-strong-direct-product-theo", "quartic-ref-02-separations-in-query-complexity-using-chea"],
    "06_corpus_fidelity": [*WRITING_LITERATURE, "quartic-lit-buhrman-dewolf-decision-tree-survey",
        "quartic-ref-08-quantum-lower-bounds-by-polynomials", "quartic-ref-19-exact-quantum-query-complexity-for-total-b",
        "quartic-ref-23-an-optimal-separation-of-randomized-and-qu", "quartic-ref-26-towards-optimal-separations-between-quantu"],
    "07_publication_backend": [], "08_adversarial_audit": [*WRITING_LITERATURE,
        "quartic-lit-buhrman-dewolf-decision-tree-survey", "quartic-ref-08-quantum-lower-bounds-by-polynomials",
        "quartic-ref-19-exact-quantum-query-complexity-for-total-b",
        "quartic-ref-23-an-optimal-separation-of-randomized-and-qu", "quartic-ref-26-towards-optimal-separations-between-quantu"],
}
WRITING_JOBS = {"02_short_expert", "03_examples_first", "08_adversarial_audit"}
BACKEND_JOBS = {"07_publication_backend"}
RENDER_SOURCES = [CIRCUIT_RETURN + "checks/" + name for name in ("render_section.py", "pdf_header.tex", "pdf_layout.lua")]
REVIEWED_FILES = ("docs/reasoning_record.bib", "docs/reasoning_record_correspondence.json", "corpus/statements.json")
digest, encoded = previous.digest, previous.encoded
batch_digest, write_archive = previous.batch_digest, previous.write_archive


def render_request(job, requests_dir):
    return (requests_dir / "common.md").read_text().format(title=JOBS[job],
        job=(requests_dir / f"{job}.md").read_text(),
        boundary=(requests_dir / "boundaries.md").read_text())


def review_status(root, receipt=None, record_render=None):
    record_hash = digest((root / "docs/reasoning_record.md").read_bytes())
    if receipt is None:
        return {"status": "pending", "record_sha256": record_hash}
    row = json.loads(receipt.read_bytes())
    if row.get("status") != "accepted" or row.get("record_sha256") != record_hash:
        raise ValueError("review receipt must accept the exact current record_sha256")
    if not row.get("reviewer") or not row.get("review_scope"):
        raise ValueError("review receipt needs reviewer and review_scope")
    reviewed = row.get("reviewed_files")
    if not isinstance(reviewed, dict) or set(reviewed) != set(REVIEWED_FILES):
        raise ValueError("review receipt reviewed_files must name bibliography, correspondence and corpus statements exactly")
    for name in REVIEWED_FILES:
        if reviewed[name] != digest((root / name).read_bytes()):
            raise ValueError(f"review receipt is stale for reviewed file: {name}")
    snapshot = previous.corpus.canonical_sha256(previous.corpus.source_hashes(root))
    if row.get("source_snapshot_sha256") != snapshot:
        raise ValueError("review receipt source_snapshot_sha256 is stale for current Lean/configuration sources")
    if not re.fullmatch(r"[0-9a-f]{64}", row.get("pdf_sha256", "")):
        raise ValueError("accepted review receipt requires the visually reviewed pdf_sha256")
    if record_render is not None and row["pdf_sha256"] != record_render_status(root, record_render)["pdf_sha256"]:
        raise ValueError("accepted review PDF hash is stale for the explicit rendered layout")
    return row


def structural_inputs(spec_path):
    """Read explicitly selected, immutable structural specimens without changing old pins."""
    if spec_path is None:
        raise ValueError("writing/reader packets require --structural-exemplars with reviewed 257 and SK sources")
    spec = json.loads(spec_path.read_bytes())
    rows = spec.get("sources")
    if spec.get("schema") != "quartic-structural-exemplars-v1" or not isinstance(rows, list):
        raise ValueError("invalid structural exemplar selection schema")
    files, families = {}, set()
    for row in rows:
        member, family = row.get("member", ""), row.get("family")
        previous.check_packets.check_name(member)
        if not member.startswith("writing/structural/") or member.casefold() in {n.casefold() for n in files}:
            raise ValueError("structural exemplar members need distinct writing/structural/ paths")
        if not re.fullmatch(r"[0-9a-f]{40}", row.get("commit", "")) or not row.get("reading_route"):
            raise ValueError("structural exemplar requires immutable Git commit and actual reading_route")
        source = (Path(row["repository"]).resolve(), row["commit"], row["path"])
        actual = digest(content(source))
        if actual != row.get("sha256"):
            raise ValueError(f"structural exemplar hash mismatch: {member}")
        files[member] = (source, "source_guided_structural_specimen_not_quartic_evidence")
        families.add(family)
    if not {"257", "sk", "graph-to-long"} <= families:
        raise ValueError("structural selection must include actual 257, SK and graph-to-long specimens")
    files["writing/STRUCTURAL_EXEMPLARS.json"] = (spec_path, "explicit_structural_selection_provenance")
    return files


@lru_cache(maxsize=4096)
def immutable_content(repository, commit, path):
    return previous.funnel.content((repository, commit, path))


def content(source):
    return immutable_content(*source) if isinstance(source, tuple) else previous.funnel.content(source)


def backend_inputs(spec_path):
    if spec_path is None:
        raise ValueError("backend job requires --backend-sources with the actual pinned runtime and test closure")
    spec = json.loads(spec_path.read_bytes())
    if spec.get("schema") != "quartic-backend-sources-v1" or not spec.get("sources"):
        raise ValueError("invalid backend source selection")
    files = {"external_backend/SOURCE_SELECTION.json": (spec_path, "explicit_backend_source_provenance")}
    for row in spec["sources"]:
        name = row["member"]
        previous.check_packets.check_name(name)
        if not name.startswith("external_backend/") or name in files or not re.fullmatch(r"[0-9a-f]{40}", row.get("commit", "")):
            raise ValueError("backend sources require distinct portable members and immutable commits")
        source = (Path(row["repository"]).resolve(), row["commit"], row["path"])
        if digest(content(source)) != row.get("sha256"):
            raise ValueError(f"backend source hash mismatch: {name}")
        files[name] = (source, "pinned_existing_backend_runtime_test_or_reference")
    for required in spec.get("required_members", []):
        if required not in files:
            raise ValueError(f"missing backend source closure member: {required}")
    return files


def method_inputs(spec_path, job):
    if spec_path is None:
        raise ValueError("each job requires --method-sources with exact portable methods and reference closure")
    spec = json.loads(spec_path.read_bytes())
    if spec.get("schema") != "quartic-method-sources-v1":
        raise ValueError("invalid method source selection")
    files = {"methods/SOURCE_SELECTION.json": (spec_path, "task_adapted_method_provenance")}
    for row in spec.get("sources", []):
        if job not in row.get("jobs", []):
            continue
        name = row["member"]
        previous.check_packets.check_name(name)
        path = Path(row["path"]).resolve()
        if not name.startswith("methods/") or name in files or not row.get("version") or not row.get("application"):
            raise ValueError("method sources need distinct members, version and job-specific application")
        if not path.is_file() or digest(path.read_bytes()) != row.get("sha256"):
            raise ValueError(f"method source hash mismatch: {name}")
        files[name] = (path, "exact_method_source_with_portable_task_adaptation")
    if len(files) == 1:
        raise ValueError(f"no task-specific method context for {job}")
    return files


def record_render_status(root, receipt_path=None):
    if receipt_path is None:
        return {"status": "pending", "source_sha256": digest((root / "docs/reasoning_record.md").read_bytes())}
    row = json.loads(receipt_path.read_bytes())
    if row.get("schema") != "quartic-reasoning-record-render-v1" or row.get("status") != "rendered_requires_visual_review" or row.get("source_unchanged") is not True:
        raise ValueError("record render needs an actually rendered source-unchanged receipt")
    if row.get("source_sha256") != digest((root / "docs/reasoning_record.md").read_bytes()):
        raise ValueError("record render is stale for current Markdown")
    pdf = Path(row["pdf"])
    if not pdf.is_file() or row.get("pdf_sha256") != digest(pdf.read_bytes()):
        raise ValueError("record render PDF hash mismatch")
    if not re.fullmatch(r"[0-9a-f]{64}", row.get("renderer_sha256", "")):
        raise ValueError("record render requires renderer provenance")
    return row


@lru_cache(maxsize=16)
def pdf_urls(pdf, pdf_sha256):
    result = subprocess.run(["pdfinfo", "-url", str(pdf)], check=True, capture_output=True, text=True)
    return tuple(match.group(3) for line in result.stdout.splitlines()
        if (match := re.match(r"^\s*(\d+)\s+(\S+)\s+(.+)$", line)))


def pdf_reading_sources(root, render):
    root = root.resolve()
    files, links = {}, []
    for target in pdf_urls(Path(render["pdf"]), render["pdf_sha256"]):
        url = urlsplit(target)
        if url.scheme == "file":
            raise ValueError(f"PDF has nonportable file URL: {target}")
        if url.scheme or url.netloc or not url.path:
            continue
        decoded = unquote(url.path)
        path = root / "docs" / decoded
        try:
            relative = path.resolve().relative_to(root)
        except ValueError:
            raise ValueError(f"PDF reading link escapes repository: {target}") from None
        if decoded.startswith("/") or "attachments" in [part.lower() for part in relative.parts] or re.fullmatch(
                r"input_?10(?:[._-].*)?", relative.name, re.I):
            raise ValueError(f"PDF reading link names private/nonportable source: {target}")
        path = root / relative
        member = "repository/" + relative.as_posix()
        if path.is_file():
            if path.is_symlink():
                raise ValueError(f"PDF reading link uses symlink: {target}")
            files[member] = (path, "pdf_linked_reading_source")
        elif not path.is_dir():
            raise ValueError(f"missing PDF reading link target: {target}")
        links.append({"link": target, "target": member, "kind": "directory" if path.is_dir() else "file"})
    return files, {"schema": "quartic-pdf-reading-links-v1", "pdf_sha256": render["pdf_sha256"], "links": links,
        "scope": "Poppler pdfinfo URL annotation targets, resolved beside repository/docs/reasoning_record.pdf. "
        "Named destinations, visual reading and non-URL PDF actions belong to the independent render review."}


def linked_sources(root, selected):
    """Follow maintained reading links; immutable submissions remain leaf evidence."""
    root = root.resolve()
    files = {name: value for name, value in selected.items() if name.startswith("repository/")}
    queue, visited, links, directories = [], set(), [], []

    def maintained(path):
        rel = path.resolve().relative_to(root).as_posix()
        return path.suffix.lower() == ".md" and not rel.startswith(("research/returns/", "research/intake/"))

    def safe(path):
        try:
            relative = path.resolve().relative_to(root)
        except ValueError:
            raise ValueError(f"reading link escapes repository: {path}") from None
        if any(part.lower() == "attachments" for part in relative.parts) or re.fullmatch(
                r"input_?10(?:[._-].*)?", relative.name, re.I):
            raise ValueError(f"reading link names private attachment: {relative}")
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents if parent != root and root in parent.parents):
            raise ValueError(f"reading link uses symlink: {relative}")
        return root / relative

    def include(path):
        path = safe(path)
        if not path.is_file():
            raise ValueError(f"missing load-bearing reading link target: {path}")
        name = "repository/" + path.relative_to(root).as_posix()
        files.setdefault(name, (path, "linked_reading_source"))
        if maintained(path) and path not in visited:
            queue.append(path)
        return name

    for source, _ in list(files.values()):
        if not isinstance(source, tuple) and source.suffix.lower() == ".md" and maintained(source):
            queue.append(safe(source))
    while queue or directories:
        if not queue:
            folder = directories.pop()
            prefix = "repository/" + folder.relative_to(root).as_posix().rstrip("/") + "/"
            if not any(name.startswith(prefix) for name in files):
                for path in sorted(folder.iterdir()):
                    if path.is_file() and not path.name.startswith(".") and path.suffix not in {".pyc", ".olean", ".ilean", ".zip"}:
                        include(path)
            if not any(name.startswith(prefix) for name in files):
                raise ValueError(f"linked directory has no packaged reading source or guide: {folder}")
            continue
        source = queue.pop()
        if source in visited:
            continue
        visited.add(source)
        text = source.read_text(encoding="utf-8")
        targets = [match.group(1).strip("<>") for match in repository_checks.LINK.finditer(text)]
        targets += [match.group(1) or match.group(2) for match in re.finditer(
            r"(?m)^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", text)]
        for target in targets:
            try:
                url = urlsplit(target)
            except ValueError as error:
                raise ValueError(f"malformed reading link in {source}: {target}") from error
            if url.scheme or url.netloc or not url.path:
                continue
            decoded = unquote(url.path)
            if decoded.startswith("/"):
                raise ValueError(f"absolute reading link escapes portable repository: {target}")
            path = safe(source.parent / decoded)
            row = {"from": "repository/" + source.relative_to(root).as_posix(), "link": target,
                "target": "repository/" + path.relative_to(root).as_posix(), "fragment": url.fragment}
            links.append(row)
            if path.is_dir():
                row["kind"] = "directory"
                directories.append(path)
                guide = next((path / name for name in ("README.md", "SELECTION.md") if (path / name).is_file()), None)
                if guide:
                    row["guide"] = include(guide)
            else:
                row["kind"] = "file"
                include(path)
    return files, {"schema": "quartic-reading-link-closure-v1", "links": links,
        "interpretation": "Maintained local reading links resolve to exact packaged files or represented directories. "
        "research/returns/**/README.md custody/sender guides and immutable submitted prose are leaf provenance; "
        "their historical internal links are not claimed to work in this packet. Direct manuscript links "
        "to any private attachment still fail. Fragments are recorded; "
        "anchor semantics and mathematical fidelity require their separate manuscript review."}


def inputs(job, *, root, requests_dir, paper_annex, annexes, writing_skill,
           writing_guides, exemplar_repo, exemplar_ref, dependency_roots=None,
           review_receipt=None, structural_exemplars=None, backend_sources=None, method_sources=None, record_render=None):
    if job not in JOBS:
        raise ValueError(f"unknown round-four job: {job}")
    files = {}

    def add(name, source, role):
        previous.check_packets.check_name(name)
        if name.casefold() in {n.casefold() for n in files}:
            return
        if not isinstance(source, tuple):
            if not source.is_file() or source.is_symlink():
                raise ValueError(f"missing or nonregular selected source: {source}")
            if "attachments" in source.parts or source.name == "input_10.txt":
                raise ValueError("private session attachment cannot enter a packet")
        files[name] = (source, role)

    def repo(path, role):
        add("repository/" + path.relative_to(root).as_posix(), path, role)

    for name in ("README.md", "AGENTS.md", "CONTRIBUTING.md", "LICENSE", "Makefile",
                 "lean/README.md", "corpus/README.md", "docs/reasoning_record.md",
                 "research/intake/statement_ledger.json"):
        repo(root / name, "integrated_record" if name == "docs/reasoning_record.md" else "repository_context")
    for folder in ("docs", "corpus", "research/adjudication"):
        for path in sorted((root / folder).rglob("*")):
            if path.is_file() and path.suffix in previous.SOURCE_SUFFIXES and not any(
                    p.startswith(".") or p in {"attachments", "__pycache__"}
                    for p in path.relative_to(root / folder).parts):
                repo(path, "maintained_adjudication" if folder.endswith("adjudication") else "recorded_context")
    for name in previous.corpus.source_hashes(root):
        repo(root / name, "exact_lean_and_pinned_configuration")
    # Reuse the aggregate import closure walker, so every supplied Lean module's
    # non-Mathlib proof dependencies are source-complete and pinned.
    dependencies, _ = previous.dependency_sources("10_baseline_record_review", root, dependency_roots or {})
    for name, source in dependencies.items():
        add(name, source, "pinned_non_mathlib_proof_dependency_source")
    for name in RENDER_SOURCES:
        repo(root / "research/returns" / name, "reused_renderer_implementation_source")
    for name in RETURNS[job]:
        repo(root / "research/returns" / name, "selected_historical_advisory_return")
    for pattern in ("*.py", "return_checks/*.py"):
        for path in sorted((root / "tools").glob(pattern)):
            repo(path, "evidence_and_packaging_consumer")
    for name in ("common.md", "boundaries.md", "SELECTION.md", f"{job}.md"):
        add("requests/" + name, requests_dir / name, "authored_request")
    for name in ("source.pdf", "extracted.md"):
        add("paper/" + name, paper_annex / name, "primary_preprint")
    for name in ("annex_notes.json", "source.tar.gz"):
        if (paper_annex / name).is_file():
            add("paper/" + name, paper_annex / name, "preprint_provenance_or_original_source")
    for slug in LITERATURE[job]:
        folder = annexes / slug
        add(f"literature/{slug}/extracted.md", folder / "extracted.md", "primary_literature_text")
        originals = [name for name in ("source.pdf", "source.tar.gz", "source.tex") if (folder / name).is_file()]
        if not originals:
            raise ValueError(f"primary literature original missing: {folder}")
        for name in previous.LITERATURE_SUPPLEMENTS.get(slug, []):
            if not (folder / name).is_file():
                raise ValueError(f"missing selected literature edition: {folder / name}")
            originals.append(name)
        for name in [*originals, "annex_notes.json"]:
            if (folder / name).is_file():
                add(f"literature/{slug}/{name}", folder / name, "primary_literature_original_or_locator")
    if job in WRITING_JOBS:
        add("writing/SKILL.md", writing_skill, "portable_writing_guidance")
        for name in previous.GUIDES:
            add("writing/" + name, writing_guides / name, "portable_writing_guidance")
            add("writing/references/" + name, writing_guides / name, "writing_skill_reference_closure")
        for name, path in previous.funnel.EXEMPLARS.items():
            add(name, (exemplar_repo, exemplar_ref, path), "writing_exemplar_not_mathematical_evidence")
        for name, (source, role) in structural_inputs(structural_exemplars).items():
            add(name, source, role)
    for name, (source, role) in method_inputs(method_sources, job).items():
        add(name, source, role)
    if job in BACKEND_JOBS:
        for path in sorted((root / "tests").rglob("*")):
            if path.is_file() and path.suffix in {".py", ".json", ".md", ".txt"} and "__pycache__" not in path.parts:
                repo(path, "quartic_backend_regression_test_or_fixture")
        for path in sorted((root / "research/requests").rglob("*.md")):
            repo(path, "maintained_request_fixture_for_packaging_regressions")
        for name, (source, role) in backend_inputs(backend_sources).items():
            add(name, source, role)
    if record_render:
        render = record_render_status(root, record_render)
        add("repository/docs/reasoning_record.pdf", Path(render["pdf"]), "matched_integrated_record_reading_copy")
        add("record_render/render.json", record_render, "source_and_pdf_bound_render_receipt")
        for name, (source, role) in pdf_reading_sources(root, render)[0].items():
            add(name, source, role)
    if review_receipt:
        add("INTEGRATED_RECORD_REVIEW.json", review_receipt, "current_integrated_record_review")
    closure, _ = linked_sources(root, files)
    for name, (source, role) in closure.items():
        add(name, source, role)
    return files


def context_link_report(data):
    """Check relative references in supplied methods/specimens without requiring private runtimes."""
    links, provenance_leaves = [], []
    for name, blob in sorted(data.items()):
        if not name.endswith(".md") or not name.startswith(("methods/", "writing/", "external_backend/")):
            continue
        if "/lean-exposition/" in name:
            relative = name.split("/lean-exposition/", 1)[1]
            # Match the existing backend scripts/check_links.py source-owner scope.
            # Captured test documents use declared logical authoring paths, not
            # their fixture-directory paths; frozen upstream READMEs retain sender context.
            authored = (relative in {"README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "SECURITY.md", "examples/README.md", "site/README.md"}
                or relative.startswith(("docs/", "skills/", "lean/", "papers/"))
                or bool(re.fullmatch(r"examples/[^/]+/README\.md", relative)))
            if not authored:
                provenance_leaves.append(name)
                continue

        text = blob.decode("utf-8")
        text = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text)
        text = re.sub(r"`[^`\n]+`", "", text)
        targets = [m.group(1).strip("<>") for m in repository_checks.LINK.finditer(text)]
        targets += [m.group(1) or m.group(2) for m in re.finditer(
            r"(?m)^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", text)]
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            decoded = unquote(url.path)
            member = posixpath.normpath(posixpath.join(posixpath.dirname(name), decoded))
            if decoded.startswith("/") or member.startswith("../"):
                raise ValueError(f"method/specimen reference escapes packet: {name} -> {target}")
            if member not in data and not any(n.startswith(member.rstrip("/") + "/") for n in data):
                raise ValueError(f"missing method/specimen reference closure: {name} -> {target}")
            links.append({"from": name, "link": target, "target": member})
    return {"schema": "quartic-context-link-closure-v1", "links": links, "source_owner_provenance_leaves": provenance_leaves,
        "scope": "Relative links in exact supplied method/specimen and backend Markdown, excluding code "
        "examples; lean-exposition authored-document scope matches its scripts/check_links.py. Captured test "
        "fixtures and frozen third-party upstream provenance retain their original logical/source context. Remote links and unavailable private CLI "
        "commands are not prerequisites; source roles and portable application remain explicit."}


def prepare(job, **options):
    hashes = previous.corpus.source_hashes(options["root"])
    files = inputs(job, **options)
    data = {name: content(source) for name, (source, _) in files.items()}
    fingerprint = {name: digest(blob) for name, blob in data.items()}
    request = data["requests/common.md"].decode().format(title=JOBS[job],
        job=data[f"requests/{job}.md"].decode(), boundary=data["requests/boundaries.md"].decode())
    if hashes != previous.corpus.source_hashes(options["root"]) or any(
            digest(data["repository/" + name]) != value for name, value in hashes.items()):
        raise ValueError("Lean source changed while reading; freeze again")
    review = review_status(options["root"], options.get("review_receipt"), options.get("record_render"))
    snapshot = previous.evidence_snapshot(data, hashes, options["root"])
    data["EVIDENCE_SNAPSHOT.json"] = encoded(snapshot)
    data["CONTEXT_LINK_CLOSURE.json"] = encoded(context_link_report(data))
    data["BUILD_STATUS.md"] = previous.build_status(snapshot)
    data["REVIEW_GATE.json"] = encoded(review)
    render = record_render_status(options["root"], options.get("record_render"))
    data["RECORD_RENDER_STATUS.json"] = encoded(render)
    if render["status"] != "pending":
        _, pdf_report = pdf_reading_sources(options["root"], render)
        for row in pdf_report["links"]:
            if row["kind"] == "file" and row["target"] not in data or row["kind"] == "directory" and not any(
                    name.startswith(row["target"].rstrip("/") + "/") for name in data):
                raise ValueError(f"PDF reading target is not represented in packet: {row['target']}")
        data["PDF_READING_LINKS.json"] = encoded(pdf_report)
    _, link_report = linked_sources(options["root"], files)
    data["READING_LINK_CLOSURE.json"] = encoded(link_report)
    _, provenance = previous.dependency_sources("10_baseline_record_review", options["root"], options.get("dependency_roots") or {})
    provenance["members"] = {n: digest(b) for n, b in data.items() if n.startswith("dependencies/")}
    data["DEPENDENCY_SOURCES.json"] = encoded(provenance)
    focus = sorted({"repository/" + p.relative_to(options["root"]).as_posix()
        for pattern in FOCUS[job] for p in options["root"].glob(pattern) if p.is_file()})
    if not focus:
        raise ValueError(f"no primary Lean source selected for {job}")
    data["literature/README.md"] = ("# Focused primary literature\n\n" + "\n".join(
        "- `" + slug + "`: " + previous.LITERATURE_ROLES.get(slug, "Primary source selected for this endpoint.")
        for slug in LITERATURE[job]) + "\n\nRead each supplied original with extracted.md and locator metadata. "
        "Use the exact editions and locators in the frozen record bibliography, distinguishing journal "
        "metadata from the inspected preprint. Høyer–Lee–Špalek and Špalek–Szegedy are separate sources; "
        "the original BSS text is not supplied or claimed read. The inspected Špalek–Szegedy publisher "
        "edition, when selected, is supplements/toc-2006-supplied.pdf. These literature files supply "
        "mathematical authority for their stated roles; writing specimens under writing/ do not.\n").encode()
    data["SOURCE_ROLES.md"] = ("# Reading route\n\nRead READ_ME_FIRST.md, REVIEW_GATE.json, "
        "repository/docs/reasoning_record.md (whole record for writing/reader jobs; roadmap and complete "
        "relevant sections plus neighboring interfaces for focused formal jobs) and maintained adjudications. Then read the primary "
        "Lean sources below with EVIDENCE_SNAPSHOT.json and BUILD_STATUS.md. Old returns are advisory; "
        "the integrated record and adjudications supersede their accepted passages. No sibling packet "
        "output is an input. All seven jobs can start independently.\n\n" + "\n".join("- `" + n + "`" for n in focus)
        + "\n\nRead original literature PDFs/TeX alongside extracted.md and provenance notes; primary "
        "preprint is paper/. Writing exemplars concern another theorem and establish no quartic claims. "
        "READING_LINK_CLOSURE.json records maintained link targets and preserves linked model contracts and examples. "
        "DEPENDENCY_SOURCES.json records pinned proof sources and the Mathlib/foundation stopping boundary. "
        "Historical research/returns/**/README.md custody/sender guides are leaf provenance; their internal "
        "links are not asserted portable. Direct manuscript links to private attachments are forbidden. "
        "This is an auditable source snapshot requiring the declared Lean/Mathlib environment. Focused Python "
        "tests use enclosed sources and temporary fixtures. Repository-wide layout/intake checks and make check "
        "need the omitted custody archive members and are not promised on this partial packet.\n").encode()
    method_selection = json.loads(data["methods/SOURCE_SELECTION.json"])
    routes = [dict(member=row["member"], version=row["version"], application=row["application"])
        for row in method_selection["sources"] if job in row.get("jobs", [])]
    method_entries = {"methods/PORTABLE_APPLICATION.md", "methods/mathematical-reasoning/SKILL.md"}
    if job in {"04_quantum_completion", "05_classical_completion"}:
        method_entries.add("methods/mathematical-reasoning/references/tao-writing-and-reading-gate.md")
    if job in {"06_corpus_fidelity", "07_publication_backend"}:
        method_entries.update({"methods/lean-exposition/skills/source-to-graph/SKILL.md",
            "methods/lean-exposition/docs/verification.md", "methods/lean-exposition/docs/contracts.md"})
    if job == "07_publication_backend":
        method_entries.update({"methods/lean-exposition/docs/bundle-consumers.md", "methods/lean-exposition/docs/authoring.md",
            "methods/lean-exposition/docs/web-api.md"})
    if job == "08_adversarial_audit":
        method_entries.update({"methods/lean-exposition/docs/reader-review.md",
            "methods/lean-exposition/skills/graph-to-long/SKILL.md"})
    entry_routes = [row for row in routes if row["member"] in method_entries]
    data["JOB_READ_MAP.md"] = ("# " + JOBS[job] + "\n\nStart with the full editable integrated record, bibliography, "
        "correspondence and its matched PDF beside it. Inspect REVIEW_GATE.json and EVIDENCE_SNAPSHOT.json "
        "before using an evidence claim. The request defines the complete outcome and boundaries.\n\n"
        "## Primary mathematical and implementation entry points\n\n" + "\n".join("- `" + name + "`" for name in focus)
        + "\n\n## Method entry points for this job\n\n" + "\n".join(
            "- `" + row["member"] + "`: " + row["application"] for row in entry_routes)
        + "\n\nRead methods/PORTABLE_APPLICATION.md before applying original method files: private "
        "workspace routes are source context, never receiving-environment prerequisites. Follow the actual "
        "local references preserved with each method. The full supporting reference closure is available in "
        "the source selection; it is not an initial exhaustive-reading assignment. Rendering requires external Pandoc, Tectonic and "
        "Poppler tools; their binaries and TeX caches are not enclosed. The renderer and its exact reused "
        "render_section.py/pdf_header.tex/pdf_layout.lua sources are included. For selected primary papers use literature/README.md "
        "and the record bibliography's exact editions and locators.\n\n"
        + ("Read writing/STRUCTURAL_EXEMPLARS.json for the exact SK/257 source passages, roles and "
           "pins. For job 02 enter lean-exposition/skills/long-to-short/SKILL.md and "
           "lean-exposition/papers/qaoa-sk/short/paper.md "
           "and plectis-erdos/paper/257/erdos-257-mersenne-support-subseries.tex under writing/structural/. "
           "For job 03 enter lean-exposition/skills/record-to-expository/SKILL.md and "
           "lean-exposition/papers/qaoa-sk/expository/main.md; "
           "use the 257 short-paper worked structures honestly, without inventing a separate 257 exposition. "
           "For job 08 enter the examined long SK/257 arguments and the reader-review method. Inspected long "
           "records and exact local reference closure remain available for proof destinations.\n\n" if job in WRITING_JOBS else "")
        + ("Backend source is external_backend/lean-exposition: start with AGENTS.md and docs/contracts.md, "
           "then bundle.py::assemble_bundle, consumer.py::ConsumerSession/query_papers/query_reading, "
           "extraction.py, verification.py, web.py and CLI. Full pinned runtime/resources/tests/example "
           "closure is supplied for actual installation and reproduction; it is not a second mathematical authority. "
           "Quartic tests and their small fixtures are also supplied. Begin with python3 -m unittest discover "
           "-s tests -p test_build_corpus.py and -p test_review_freshness.py from repository/, then add "
           "the adapter regression commands you actually verify. Full layout/intake checks require omitted "
           "custody records and cannot be claimed on this partial snapshot.\n" if job in BACKEND_JOBS else "")
    ).encode()
    counts = {}
    for _, role in files.values():
        counts[role] = counts.get(role, 0) + 1
    data["CONTEXT_MANIFEST.json"] = encoded({"schema": "quartic-job-context-v1", "job": job, "title": JOBS[job],
        "primary_read": focus, "literature": [{"slug": slug, "role": previous.LITERATURE_ROLES.get(slug,
            "Primary source for the assigned endpoint; inspect the frozen bibliography locator.")} for slug in LITERATURE[job]],
        "methods": routes, "member_roles": counts, "record_sha256": review["record_sha256"],
        "matched_render_status": render["status"], "independent_jobs": True,
        "all_input_members": sorted(files), "reading_link_receipt": "READING_LINK_CLOSURE.json"})
    rows = [{"member": name, "source": str(files[name][0]) if name in files else "generated from hashed inputs",
        "role": files[name][1] if name in files else "packet_navigation_or_evidence_reclassification",
        "bytes": len(blob), "sha256": digest(blob)} for name, blob in data.items()]
    commit = subprocess.run(["git", "-C", str(options["root"]), "rev-parse", "HEAD"],
        check=True, capture_output=True, text=True).stdout.strip()
    manifest = {"campaign": "round4", "packet": job, "title": JOBS[job], "repository_commit": commit,
        "source_paper": "Supplied OpenAI preprint PDF SHA-256 " + digest(data["paper/source.pdf"]),
        "request_sha256": digest(request.encode()), "record_sha256": digest(data["repository/docs/reasoning_record.md"]),
        "review_gate": review, "primary_read": focus, "input_sha256": fingerprint, "members": rows,
        "literature": LITERATURE[job], "interpretation": "Commit is provenance; the complete member hashes bind working bytes."}
    return {"data": data, "request": request, "manifest": manifest, "sources": files}


def prepare_batch(jobs, **options):
    if not jobs or len(jobs) != len(set(jobs)) or not set(jobs) <= set(JOBS):
        raise ValueError("select distinct maintained round-four jobs")
    packets = {job: prepare(job, **options) for job in jobs}
    for job, packet in packets.items():
        current = inputs(job, **options)
        if current != packet["sources"] or {n: digest(content(s)) for n, (s, _) in current.items()} != packet["manifest"]["input_sha256"]:
            raise ValueError("inputs changed across batch; freeze again")
    return packets


def build_batch(jobs, dest, freeze_digest, **options):
    dest, root = dest.resolve(), options["root"].resolve()
    if dest == root or root in dest.parents:
        raise ValueError("output must be outside the repository")
    if dest.exists():
        raise FileExistsError("choose a new output folder; never overwrite prior batches")
    if not freeze_digest or review_status(root, options.get("review_receipt"), options.get("record_render")).get("status") != "accepted":
        raise ValueError("build requires accepted current review receipt and freeze digest")
    if record_render_status(root, options.get("record_render")).get("status") == "pending":
        raise ValueError("build requires matched --record-render PDF and receipt")
    packets = prepare_batch(jobs, **options)
    if batch_digest(packets) != freeze_digest:
        raise ValueError("inputs differ from freeze digest")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".quartic-r4-", dir=dest.parent) as staging:
        for job, packet in packets.items():
            write_archive(Path(staging) / f"quartic_r4_{job}.zip", packet)
        if batch_digest(prepare_batch(jobs, **options)) != freeze_digest:
            raise ValueError("inputs changed during packaging")
        dest.mkdir()  # exclusive directory creation; no old output can be replaced
        published = []
        try:
            for path in Path(staging).iterdir():
                output = dest / path.name
                os.link(path, output)
                published.append(output)
        except BaseException:
            for path in published:
                path.unlink()
            if not any(dest.iterdir()):
                dest.rmdir()
            raise
    return [dest / f"quartic_r4_{job}.zip" for job in jobs]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--requests-dir", type=Path)
    for name in ("paper-annex", "annexes", "writing-skill", "writing-guides", "exemplar-repo"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--exemplar-ref", required=True)
    parser.add_argument("--dependency-root", action="append", default=[])
    parser.add_argument("--review-receipt", type=Path)
    parser.add_argument("--backend-sources", type=Path)
    parser.add_argument("--method-sources", type=Path)
    parser.add_argument("--context-report", type=Path, help="optional external validation-only manifest/context report; creates no ZIP")
    parser.add_argument("--record-render", type=Path, help="explicit renderer receipt binding current Markdown and PDF")
    parser.add_argument("--structural-exemplars", type=Path,
        help="explicit immutable Git source selection for actual 257, examined SK and graph-to-long specimens")
    parser.add_argument("--only", nargs="+", choices=sorted(JOBS))
    parser.add_argument("--dest", type=Path)
    parser.add_argument("--freeze-digest")
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args(argv)
    if args.build and (not args.dest or not args.freeze_digest or not args.review_receipt or not args.record_render):
        parser.error("--build requires --dest, --freeze-digest, --review-receipt and --record-render")
    try:
        roots = {}
        for item in args.dependency_root:
            name, sep, path = item.partition("=")
            if not sep or not path or name in roots:
                raise ValueError("dependency roots need distinct NAME=PATH pairs")
            roots[name] = Path(path).resolve()
        options = {name: getattr(args, name).resolve() for name in
            ("root", "paper_annex", "annexes", "writing_skill", "writing_guides", "exemplar_repo")}
        options.update(requests_dir=(args.requests_dir or args.root / "research/requests/round4").resolve(),
            dependency_roots=roots, review_receipt=args.review_receipt.resolve() if args.review_receipt else None,
            structural_exemplars=args.structural_exemplars.resolve() if args.structural_exemplars else None,
            backend_sources=args.backend_sources.resolve() if args.backend_sources else None,
            method_sources=args.method_sources.resolve() if args.method_sources else None,
            record_render=args.record_render.resolve() if args.record_render else None,
            exemplar_ref=subprocess.run(["git", "-C", str(args.exemplar_repo), "rev-parse", "--verify",
                args.exemplar_ref + "^{commit}"], check=True, capture_output=True, text=True).stdout.strip())
        jobs = args.only or list(JOBS)
        if args.build:
            for path in build_batch(jobs, args.dest, args.freeze_digest, **options):
                print(f"PASS {path}")
        else:
            packets = prepare_batch(jobs, **options)
            if args.context_report:
                report_path = args.context_report.resolve()
                if report_path == options["root"] or options["root"] in report_path.parents:
                    raise ValueError("context report must be outside the repository")
                report_path.parent.mkdir(parents=True, exist_ok=True)
                report_path.write_bytes(encoded({"campaign": "round4", "freeze_digest": batch_digest(packets),
                    "delivery": "validation only; no ZIPs", "packets": {job: {"manifest": packet["manifest"],
                        "context": json.loads(packet["data"]["CONTEXT_MANIFEST.json"]),
                        "reading_links": json.loads(packet["data"]["READING_LINK_CLOSURE.json"]),
                        "context_links": json.loads(packet["data"]["CONTEXT_LINK_CLOSURE.json"]),
                        "pdf_links": json.loads(packet["data"].get("PDF_READING_LINKS.json", b"{}"))}
                        for job, packet in packets.items()}}))
            print(f"Validated {len(packets)} packet inputs; no ZIPs written.")
            print("Freeze digest: " + batch_digest(packets))
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"FAIL: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
