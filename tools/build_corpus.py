#!/usr/bin/env python3
"""Generate the corpus records from the ledger, Lean sources, ties and receipts.

Authored inputs:
  research/intake/statement_ledger.json   the statements of the preprint
  research/adjudication/adjudication.json      accepted corrections and added rows
  corpus/ties.json                        reviewed statement-to-Lean relations
  corpus/receipts/*.json                  results of actual builds and comparisons
  corpus/lean_dependencies.json           the compiled dependency closure

Generated outputs:
  corpus/statements.json      one record per statement, with separate evidence fields
  corpus/evidence-graph.json  the same statements in the lean-exposition graph schema
  corpus/coverage.json        counts for each evidence field, with no overall score

A `Ledger: <id>` line in a Lean doc comment only proposes a tie. A statement counts
as checked only through a reviewed relation in ties.json and a receipt that names
the declaration. Declaration presence never counts.
"""

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "research/intake/statement_ledger.json"
ADJUDICATION = ROOT / "research/adjudication/adjudication.json"
LEAN = ROOT / "lean/QuarticQuery"
CORPUS = ROOT / "corpus"
PAPER_REVISION = "4eaee875"
PAPER_URL = ("https://github.com/openai/math/blob/main/preprints/"
             "A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-"
             "October-5-2026/quartic-query-separation.pdf")
GOALS = ["thm-1.1"]
# The one input the preprint imports without proof.
EXTERNAL = {"lem-2.1.i"}
RELATIONS = {"exact", "stronger", "partial", "weaker"}
ROUTES = {"same", "alternative", "none"}
CHECKED = {"exact", "stronger"}
REVIEW_SCHEMA = "quartic-tie-review-v1"
DOC_TIE = re.compile(r"Ledger:\s*")
TIE_ID = re.compile(r"[A-Za-z][\w.-]*\w")
DECLARATION = re.compile(
    r"^(?:@\[[^\]]*\]\s*)*(?:noncomputable\s+)?(?:private\s+)?"
    r"(theorem|lemma|def|abbrev|structure|inductive)\s+(\S+)", re.M)


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rows():
    """Return the ledger with adjudicated changes applied, keeping the original hash."""
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    changes = json.loads(ADJUDICATION.read_text(encoding="utf-8"))["ledger_row_changes"]
    out = {}
    for row in ledger:
        change = changes.get(row["id"], {})
        merged = {**row, **{k: v for k, v in change.items() if k != "new_row"}}
        merged["original_statement_sha256"] = sha256(row["statement"])
        merged["corrected"] = merged["statement"] != row["statement"]
        out[row["id"]] = merged
    for key, change in changes.items():
        if key not in out:
            if not change.get("new_row"):
                raise ValueError(f"adjudication changes unknown row {key}")
            out[key] = {"id": key, **{k: v for k, v in change.items() if k != "new_row"},
                        "original_statement_sha256": None, "corrected": False, "added": True}
    return out


def tie_ids(text, start):
    """Read the comma-separated row ids after `Ledger:`; ids may contain dots."""
    ids = []
    while match := TIE_ID.match(text, start):
        ids.append(match.group())
        start = match.end()
        if text[start:start + 1] != ",":
            break
        start += 1
        while text[start:start + 1].isspace():
            start += 1
    return ids


def open_scopes(events, position):
    """Return the namespace parts open at `position`, closing sections too."""
    stack = []
    for at, kind, name in events:
        if at > position:
            break
        if kind == "end":
            count = len(name.split(".")) if name else 1
            del stack[-count:]
        else:
            stack.extend((kind, part) for part in (name.split(".") if name else [""]))
    return [part for kind, part in stack if kind == "namespace"]


def declared_ties(root=LEAN):
    """Map ledger ids to the declarations whose doc comments name them."""
    ties = {}
    for path in sorted(root.rglob("*.lean")):
        text = path.read_text(encoding="utf-8")
        events = [(match.start(), match.group(1), match.group(2))
                  for match in re.finditer(r"^(namespace|section|end)(?:[ \t]+(\S+))?[ \t]*$", text, re.M)]
        for doc in re.finditer(r"/--(.*?)-/", text, re.S):
            tie = DOC_TIE.search(doc.group(1))
            if not tie:
                continue
            found = DECLARATION.search(text, doc.end())
            if not found:
                continue
            name = ".".join(open_scopes(events, doc.start()) + [found.group(2)])
            for ident in tie_ids(doc.group(1), tie.end()):
                ties.setdefault(ident, []).append({
                    "declaration": name,
                    "kind": found.group(1),
                    "file": str(path.relative_to(ROOT)),
                    "line": text.count("\n", 0, found.start()) + 1,
                })
    return ties


def load_json(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def source_hashes(root=None):
    """Bind evidence to all local Lean sources and pinned build/comparison inputs.

    The scope is deliberately conservative: changing any Lean source invalidates
    every receipt, including a source outside the headline's import closure.
    Ignored Lake dependencies and build products are not local source inputs;
    lake-manifest.json records their pinned revisions, not their checkout bytes.
    """
    root = Path(root) if root is not None else ROOT
    hashes = {}
    for folder, directories, files in os.walk(root / "lean"):
        directories[:] = sorted(d for d in directories if not d.startswith(".")
                                and d not in {"build", "__pycache__"})
        for name in sorted(files):
            path = Path(folder) / name
            if (path.suffix == ".lean" or name in {
                    "lean-toolchain", "lakefile.toml", "lake-manifest.json"}
                    or (path.suffix == ".json" and "QuarticCorpus" in path.parts)):
                hashes[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(sorted(hashes.items()))


def currentness(record, hashes=None):
    """Historical passes remain visible but only bound, unchanged inputs are current."""
    recorded = record.get("source_hashes")
    if not isinstance(recorded, dict) or not recorded:
        return "legacy_unbound"
    return "current" if recorded == (source_hashes() if hashes is None else hashes) else "stale"


def canonical_sha256(value):
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")))


def expected_review_binding(ident, row, review, hashes):
    """The bytes a reviewer must bind after reviewing, never a review itself.

    The complete local-source snapshot includes declaration types, implicit
    context and all locally defined terms, as well as pinned dependencies.
    This deliberately invalidates on proof-only edits too. No producer writes
    this binding into authored ties or upgrades an old review automatically.
    """
    return {
        "schema": REVIEW_SCHEMA,
        "statement_id": ident,
        "statement_sha256": sha256(row["statement"]),
        "row_sha256": canonical_sha256(row),
        "declaration": review["declaration"],
        "judgment_sha256": canonical_sha256(
            {key: value for key, value in review.items() if key != "review_binding"}),
        "source_snapshot_sha256": canonical_sha256(hashes),
    }


def review_currentness(ident, row, review, hashes):
    """A fresh proof/comparison receipt cannot refresh a statement review."""
    if review is None:
        return "not_reviewed"
    if "review_binding" not in review:
        return "legacy_unbound"
    binding = review["review_binding"]
    expected = expected_review_binding(ident, row, review, hashes)
    if (not isinstance(binding, dict) or set(binding) != set(expected)
            or binding.get("schema") != REVIEW_SCHEMA
            or not all(isinstance(value, str) for value in binding.values())
            or any(not re.fullmatch(r"[0-9a-f]{64}", binding[key])
                   for key in expected if key.endswith("sha256"))):
        raise ValueError(f"{ident}/{review['declaration']}: malformed review_binding")
    return "current" if binding == expected else "stale"


def require_preprint_row(ident, row):
    """Withhold separately derived rows until mixed-source projection is supported.

    r2-live proposals retain their own source and dependency data in their
    adjudication owner. Even an explicit preprint source label must not silently
    turn those known helper statements into claims of the OpenAI preprint.
    """
    if ident.startswith("r2-live-") or row.get("source_id", "openai_preprint") != "openai_preprint":
        raise ValueError(f"{ident}: withheld from the preprint-only corpus; "
                         "preserve its own provenance and dependencies in the source owner")


def receipts():
    return [{**json.loads(path.read_text(encoding="utf-8")), "receipt_file": str(path.relative_to(ROOT)),
             "receipt_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in sorted((CORPUS / "receipts").glob("*.json"))]


def declaration_evidence(runs, kind, declaration, hashes):
    matching = [run for run in runs if run["kind"] == kind and run["status"] == "passed"
                and declaration in run.get("declarations", [])
                and not run.get("negative_control")]
    states = {currentness(run, hashes) for run in matching}
    return next((state for state in ("current", "stale", "legacy_unbound") if state in states), "not_run")


def reviewed_assumptions(review):
    """Keep theorem premises separate from additional, undischarged assumptions.

    Legacy hypotheses remain open unless a review explicitly supplies the new
    open_assumptions field. Merely listing premises is not a classification of
    every legacy hypothesis. Preserve the authored hypotheses for older readers.
    """
    review = review or {}
    fields = {"hypotheses": review.get("hypotheses", []),
              "premises": review.get("premises", []),
              "open_assumptions": review.get("open_assumptions", review.get("hypotheses", []))}
    for field, values in fields.items():
        if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
            raise ValueError(f"{review.get('declaration', 'unreviewed tie')}: {field} must be a list of strings")
    return fields


def statement_records(ledger, proposed, reviewed, runs, reached=None, hashes=None,
                      reach_currentness="legacy_unbound"):
    hashes = source_hashes() if hashes is None else hashes
    records = []
    for ident, row in ledger.items():
        require_preprint_row(ident, row)
        ties = []
        declared = proposed.get(ident, [])
        names = {tie["declaration"] for tie in declared}
        # A reviewed tie needs no doc comment, which keeps Statement.lean free of them.
        extra = [{"declaration": r["declaration"], "kind": r.get("kind", "definition"),
                  "file": r.get("file", "lean/QuarticQuery/Statement.lean"), "line": r.get("line")}
                 for r in reviewed.get(ident, []) if r["declaration"] not in names]
        for tie in declared + extra:
            review = next((r for r in reviewed.get(ident, [])
                           if r["declaration"] == tie["declaration"]), None)
            review_state = review_currentness(ident, row, review, hashes)
            build = declaration_evidence(runs, "lean_build", tie["declaration"], hashes)
            comparison = declaration_evidence(runs, "comparator", tie["declaration"], hashes)
            ties.append({**tie,
                         "relation": review["relation"] if review_state == "current" else "unassessed",
                         "route": review["route"] if review_state == "current" else "unassessed",
                         "reviewed_relation": review["relation"] if review else "unassessed",
                         "reviewed_route": review["route"] if review else "unassessed",
                         "review_evidence": review_state,
                         **({"review_binding": review["review_binding"]}
                            if review and "review_binding" in review else {}),
                         **reviewed_assumptions(review),
                         "note": review.get("note", "") if review else "",
                         "build_evidence": build,
                         "comparison_evidence": comparison,
                         "built": build == "current",
                         "compared": comparison == "current",
                         "reached": (None if reached is None or reach_currentness != "current"
                                     else tie["declaration"] in reached)})
        # The strongest evidence wins: compared before merely built, unconditional first.
        best = min((t for t in ties if t["relation"] in CHECKED and t["built"]),
                   key=lambda t: (not t["compared"], bool(t["open_assumptions"])), default=None)
        records.append({
            "id": ident,
            "kind": row["kind"],
            "section": row.get("section"),
            "source_line": row.get("source_line"),
            "statement": row["statement"],
            "statement_sha256": sha256(row["statement"]),
            "original_statement_sha256": row["original_statement_sha256"],
            "corrected": row["corrected"],
            "depends_on": row.get("depends_on", []),
            "external_inputs": row.get("external_inputs", []),
            "lean": ties,
            "evidence": {
                "review": next((state for state in ("current", "stale", "legacy_unbound")
                                if any(t["review_evidence"] == state for t in ties)), "not_reviewed"),
                "formal_statement": (
                    "none" if not ties else
                    next((t["relation"] for t in ties if t["relation"] in CHECKED), None)
                    or next((t["relation"] for t in ties if t["relation"] in RELATIONS), "unassessed")),
                "formal_origin": "ours" if ties else "none",
                "build": "built_at_pin" if any(t["built"] for t in ties) else "not_run",
                "comparator": "compared" if best and best["compared"] else "not_run",
                "conditional": bool(best and best["open_assumptions"]),
                # Optional metadata belongs to this selected declaration only.
                # Its absence means no current built tie was selected; [] is a
                # reviewed empty list, not an unknown assumption classification.
                **({"assumption_declaration": best["declaration"],
                    "premises": best["premises"], "open_assumptions": best["open_assumptions"]}
                   if best else {}),
                "route": best["route"] if best else "none",
                "reach": ("not_computed" if reached is None else
                          reach_currentness if reach_currentness != "current" else
                          "none" if not ties else
                          "reached" if any(t["reached"] for t in ties) else "outside"),
            },
        })
    return records


def node_status(record):
    # These nodes are informal preprint statements, not native exported formal
    # declarations. Local theorem receipts do not verify the statement-to-Lean
    # interpretation or satisfy the consumer's extraction/build contract.
    return "external" if record["id"] in EXTERNAL else "unverified"


def node_kind(record):
    if record["id"] in GOALS:
        return "goal"
    return "assumption" if record["id"] in EXTERNAL else "claim"


def evidence_graph(records, runs, hashes=None):
    hashes = source_hashes() if hashes is None else hashes
    ids = {record["id"] for record in records}
    for record in records:
        require_preprint_row(record["id"], record)
        missing = set(record["depends_on"]) - ids
        if missing:
            raise ValueError(f"{record['id']}: missing prerequisite rows: {', '.join(sorted(missing))}")
    evidence = [{"id": "paper_hash", "kind": "source_hash", "status": "not_run", "command": [],
                 "tool": "Pinned by revision; byte hash is recorded in the annex",
                 "source_ids": ["openai_preprint"], "subject_ids": [],
                 "details": "The preprint revision is pinned; this record is not a proof check."},
                {"id": "fidelity_review", "kind": "semantic_review", "status": "not_run",
                 "command": [], "tool": "Independent statement-fidelity reading not yet run",
                 "source_ids": ["openai_preprint"], "subject_ids": [],
                 "details": "AI readings exist in research/returns; none is an independent review."}]
    for index, run in enumerate(runs):
        details = run.get("details", "")
        # A negative control "passes" when Comparator rejects its altered solution.
        if run.get("negative_control") == "rejected_as_expected":
            details = (f"Altered solution {run['name']} rejected as expected "
                       f"(exit {run.get('exit_code')}, diagnostic "
                       f"\"{run.get('expected_diagnostic', '')}\"). {details}").strip()
        state = currentness(run, hashes)
        provenance = {"operation": run, "currentness": state}
        subjects = [record["id"] for record in records
                    if any(tie["declaration"] in run.get("declarations", []) for tie in record["lean"])]
        evidence.append({"id": f"run_{index}", "kind": "semantic_review", "status": "not_run",
                         "receipt": provenance,
                         **({"receipt_path": run["receipt_file"], "receipt_sha256": run["receipt_sha256"]}
                            if run.get("receipt_file") and run.get("receipt_sha256") else {}),
                         "command": run["command"],
                         "tool": "Projection of a local operation receipt; independent statement review not run",
                         "source_ids": ["openai_preprint"], "subject_ids": subjects,
                         "details": (details + f" Recorded {run['kind']} status: {run['status']}. "
                                     f"Evidence currentness: {state}. This is historical metadata, "
                                     "not a native lean-exposition proof/extraction receipt.").strip()})
    nodes = []
    for record in records:
        selected = record["evidence"]
        metadata = {"boundary": "Informal statement projection; no native formal declaration export or independent semantic verification."}
        evidence_ids = ["fidelity_review", *[item["id"] for item in evidence
                                            if record["id"] in item["subject_ids"]]]
        if record["lean"]:
            metadata_id = f"tie_review_{record['id']}"
            evidence_ids.append(metadata_id)
            evidence.append({
                "id": metadata_id, "kind": "semantic_review", "status": "not_run", "command": [],
                "tool": "Projection of authored reviews and proposed statement ties",
                "source_ids": ["openai_preprint"], "subject_ids": [record["id"]],
                "details": "Historical judgments and independent freshness states; not an independent semantic review or proof receipt.",
                "receipt": {"statement_evidence": selected, "ties": record["lean"],
                            **{field: selected[field]
                               for field in ("assumption_declaration", "premises", "open_assumptions")
                               if field in selected}},
            })
        if "assumption_declaration" in selected:
            metadata = {"declaration": selected["assumption_declaration"],
                        "boundary": (metadata["boundary"] + " Selected tied theorem metadata. Ordinary premises: "
                                     + ("; ".join(selected["premises"]) or "none")
                                     + ". Additional open assumptions: "
                                     + ("; ".join(selected["open_assumptions"]) or "none") + ".")}
        nodes.append({
            "id": record["id"], "kind": node_kind(record), "label": record["id"],
            "status": node_status(record), "assumption_ids": [],
            **metadata,
            "evidence_ids": evidence_ids, "citation_ids": [],
            "source_id": "openai_preprint",
            "locator": f"Section {record['section']}, extracted line {record['source_line']}",
            "statement": record["statement"],
        })
    edges = [{"from": record["id"], "to": dep, "kind": "supports", "evidence_ids": []}
             for record in records for dep in record["depends_on"]]
    return {
        "schema_version": "1.2",
        "id": "quartic-query-separation",
        "title": "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity",
        "selected_goals": GOALS,
        "sources": [{"id": "openai_preprint", "kind": "file", "url": PAPER_URL,
                     "revision": PAPER_REVISION, "license": "see upstream repository",
                     "redistribution": "reference_only"}],
        "citations": [],
        "nodes": nodes,
        "edges": edges,
        "evidence": evidence,
        "scope": ("Informal statement graph of the preprint, generated from the corrected ledger. Support "
                  "edges point from each consumer to its authored prerequisite, not an extracted Lean dependency. "
                  "Claim/goal nodes remain unverified and imported assumptions external. Actual current "
                  "build/comparison results remain in corpus records and metadata receipts, not native "
                  "lean-exposition verification/extraction evidence. "
                  "Ordinary reviewed theorem premises do not make a statement conditional; "
                  "explicit open_assumptions do, with hypotheses as the legacy fallback. "
                  "Selected assumption metadata is omitted when no current built tie exists; "
                  "its absence is unknown, whereas [] is an explicitly empty list. "
                  "Current statement alignment additionally requires a source-bound authored review; "
                  "builds and comparisons cannot refresh it. Separately derived r2-live rows are withheld. "
                  "Historical receipt status is preserved separately from currentness."),
        "extraction_status": "not_run",
        "notes": ["Generated by tools/build_corpus.py; edit the inputs, not this file."],
    }


def coverage(records, unknown=()):
    fields = ["review", "formal_statement", "formal_origin", "build", "comparator", "route", "reach"]
    return {
        "statements": len(records),
        "corrected": sum(r["corrected"] for r in records),
        "ledger_ids_without_a_row": sorted(unknown),
        **{field: dict(sorted(Counter(r["evidence"][field] for r in records).items()))
           for field in fields},
    }


def outputs():
    ledger = rows()
    runs = receipts()
    proposed = declared_ties()
    reviewed = load_json(CORPUS / "ties.json", {})
    closure = load_json(CORPUS / "lean_dependencies.json", None)
    hashes = source_hashes()
    records = statement_records(ledger, proposed, reviewed, runs,
                                set(closure["reached"]) if closure else None, hashes,
                                currentness(closure, hashes) if closure else "not_computed")
    return {
        CORPUS / "statements.json": records,
        CORPUS / "evidence-graph.json": evidence_graph(records, runs, hashes),
        CORPUS / "coverage.json": coverage(records, set(proposed) - set(ledger)),
    }


def render(value):
    return json.dumps(value, indent=1, ensure_ascii=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if a generated file is stale")
    args = parser.parse_args()
    stale = []
    for path, value in outputs().items():
        text = render(value)
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(path.name)
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(text, encoding="utf-8")
    if stale:
        print("stale, run tools/build_corpus.py: " + ", ".join(stale), file=sys.stderr)
        return 1
    print(render(outputs()[CORPUS / "coverage.json"]).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
