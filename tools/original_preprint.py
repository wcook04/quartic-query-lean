"""Bind the preprint's statement index to physical pages of OpenAI's published PDF."""
import argparse
from bisect import bisect_right
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REVISION = "4eaee87548250b2682affda7d05d947c05554bae"
TITLE = "A Nearly Quartic Separation Between Randomized and Quantum Query Complexity"
FILE = "preprints/" + TITLE.replace(" ", "-") + "-October-5-2026/quartic-query-separation.pdf"
PDF_URL = f"https://raw.githubusercontent.com/openai/math/{REVISION}/{FILE}"
MAP = "docs/original_preprint.json"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def coordinates_hash(statements):
    coordinates = sorted((sid, row["source_line"]) for sid, row in statements.items())
    return digest(json.dumps(coordinates, separators=(",", ":")).encode())


def inspect(pdf, statements):
    # These tools are required only to reproduce the saved PDF position map.
    import fitz
    layout = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"])
    lines = layout.decode().split("\n")
    starts = [1] + [i for i, line in enumerate(lines, 1) if line.startswith("\f") and line != "\f"]
    with fitz.open(pdf) as doc:
        if len(starts) != len(doc):
            raise ValueError("PDF pages differ from layout breaks")
        destinations = {k: v["page"] + 1 for k, v in doc.resolve_names().items()
                        if k.startswith(("equation.", "theorem."))}
    return {"sha256": digest(pdf.read_bytes()), "pages": len(starts), "page_start_lines": starts,
            "layout_sha256": digest(layout), "coordinates_sha256": coordinates_hash(statements),
            "destinations": destinations}


def original_paper(edition, statements, pdf=None):
    receipt = edition.json(MAP)
    if coordinates_hash(statements) != receipt["coordinates_sha256"]:
        raise ValueError("preprint statement coordinates changed; verify the PDF position map")
    doc = {"title": TITLE, "format": "pdf", "author": "OpenAI", "sha256": receipt["sha256"],
           "source_revision": REVISION, "url": PDF_URL, "pages": receipt["pages"],
           "formalization": "Quartic project", "statement_coverage": "corpus/coverage.json",
           "review_scope": "Lean comparisons assess the maintained ledger wording. Open the PDF for the published wording.", "selection": "selection/original.json"}
    if pdf is not None:
        raw = pdf.read_bytes()
        if digest(raw) != doc["sha256"]:
            raise ValueError("original PDF differs from OpenAI's pinned release")
        doc["resource"] = "print/original.pdf"
        edition.resources[doc["resource"]] = raw
    rows = []
    for sid, statement in statements.items():
        page = bisect_right(receipt["page_start_lines"], statement["source_line"])
        loc = {"page": page, "url": f"{PDF_URL}#page={page}"}
        # Only exactly numbered statements get a named destination. A local
        # generalization of a proposition keeps a page-level reference.
        label = re.fullmatch(r"(eq|lem|prop|thm)-([A\d]+(?:\.\d+)?)", sid)
        if label:
            prefix = "equation" if label[1] == "eq" else "theorem"
            dest = f"{prefix}.{label[2]}"
            if receipt["destinations"].get(dest) != page:
                raise ValueError(f"{sid}: PDF destination differs from its ledger page")
            loc["destination"] = dest
        rows.append({"id": f"original/{sid}", "paper": "original", "statements": [sid],
                     "location": loc, "ledger_corrected": statement["corrected"],
                     "added_in_review": statement["original_statement_sha256"] is None})
    return doc, rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify the recorded source PDF, page breaks and destinations")
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    statements = {r["id"]: r for r in json.loads((ROOT / "corpus/statements.json").read_bytes())}
    if inspect(args.pdf, statements) != json.loads((ROOT / MAP).read_bytes()):
        parser.exit(1, "original preprint map differs\n")
    print("Original PDF and statement location map verified")
