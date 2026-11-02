#!/usr/bin/env python3
"""Generate the corpus records from the ledger, Lean sources, ties and receipts.

Authored inputs:
  research/intake/statement_ledger.json   the statements of the preprint
  research/returns/adjudication.json      accepted corrections and added rows
  corpus/ties.json                        reviewed statement-to-Lean relations
  corpus/receipts/*.json                  results of actual builds and comparisons

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
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "research/intake/statement_ledger.json"
ADJUDICATION = ROOT / "research/returns/adjudication.json"
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


def receipts():
    return [json.loads(path.read_text(encoding="utf-8"))
            for path in sorted((CORPUS / "receipts").glob("*.json"))]


def statement_records(ledger, proposed, reviewed, runs):
    built = {name for run in runs if run["kind"] == "lean_build" and run["status"] == "passed"
             for name in run["declarations"]}
    compared = {name for run in runs if run["kind"] == "comparator" and run["status"] == "passed"
                for name in run["declarations"]}
    records = []
    for ident, row in ledger.items():
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
            ties.append({**tie,
                         "relation": review["relation"] if review else "unassessed",
                         "route": review["route"] if review else "unassessed",
                         "hypotheses": review.get("hypotheses", []) if review else [],
                         "note": review.get("note", "") if review else "",
                         "built": tie["declaration"] in built,
                         "compared": tie["declaration"] in compared})
        best = next((t for t in ties if t["relation"] in CHECKED and t["built"]), None)
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
                "formal_statement": (
                    "none" if not ties else
                    next((t["relation"] for t in ties if t["relation"] in CHECKED), None)
                    or next((t["relation"] for t in ties if t["relation"] in RELATIONS), "unassessed")),
                "formal_origin": "ours" if ties else "none",
                "build": "built_at_pin" if any(t["built"] for t in ties) else "not_run",
                "comparator": "compared" if best and best["compared"] else "not_run",
                "conditional": bool(best and best["hypotheses"]),
                "route": best["route"] if best else "none",
                "reach": "not_computed",
            },
        })
    return records


def node_status(record):
    evidence = record["evidence"]
    if evidence["comparator"] == "compared":
        return "conditional" if evidence["conditional"] else "kernel_checked"
    return "external" if record["id"] in EXTERNAL else "unverified"


def node_kind(record):
    if record["id"] in GOALS:
        return "goal"
    return "assumption" if record["id"] in EXTERNAL else "claim"


def evidence_graph(records, runs):
    ids = {record["id"] for record in records}
    evidence = [{"id": "paper_hash", "kind": "source_hash", "status": "not_run", "command": [],
                 "tool": "Pinned by revision; byte hash is recorded in the annex",
                 "source_ids": ["openai_preprint"], "subject_ids": [],
                 "details": "The preprint revision is pinned; this record is not a proof check."},
                {"id": "fidelity_review", "kind": "semantic_review", "status": "not_run",
                 "command": [], "tool": "Independent statement-fidelity reading not yet run",
                 "source_ids": ["openai_preprint"], "subject_ids": [],
                 "details": "AI readings exist in research/returns; none is an independent review."}]
    for index, run in enumerate(runs):
        evidence.append({"id": f"run_{index}", "kind": run["kind"], "status": run["status"],
                         "command": run["command"], "tool": run["tool"],
                         "source_ids": ["openai_preprint"], "subject_ids": [],
                         "details": run.get("details", "")})
    nodes = []
    for record in records:
        nodes.append({
            "id": record["id"], "kind": node_kind(record), "label": record["id"],
            "status": node_status(record), "assumption_ids": [],
            "evidence_ids": ["fidelity_review"], "citation_ids": [],
            "source_id": "openai_preprint",
            "locator": f"Section {record['section']}, extracted line {record['source_line']}",
            "statement": record["statement"],
        })
    edges = [{"from": dep, "to": record["id"], "kind": "supports", "evidence_ids": []}
             for record in records for dep in record["depends_on"] if dep in ids]
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
        "scope": ("Statement graph of the preprint, generated from the corrected ledger. Support "
                  "edges are authored dependencies, not extracted Lean dependencies. A node is "
                  "kernel_checked only through a reviewed tie and a Comparator receipt."),
        "extraction_status": "not_run",
        "notes": ["Generated by tools/build_corpus.py; edit the inputs, not this file."],
    }


def coverage(records, unknown=()):
    fields = ["formal_statement", "formal_origin", "build", "comparator", "route", "reach"]
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
    records = statement_records(ledger, proposed, reviewed, runs)
    return {
        CORPUS / "statements.json": records,
        CORPUS / "evidence-graph.json": evidence_graph(records, runs),
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
