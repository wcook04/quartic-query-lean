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


def inspect_reading_pdf(pdf, manifest, source_root):
    """Reproduce PDF-derived references and figure pixels; retain explicit limits."""
    import fitz
    if digest(pdf.read_bytes()) != manifest["pdf_sha256"]:
        raise ValueError("reading source belongs to a different original PDF")
    layout = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"]).decode()
    if digest(layout.encode()) != manifest["pdf_layout_sha256"]:
        raise ValueError("PDF extraction differs from pinned layout")
    bibliography = layout[layout.index("References\n"):]
    references = {}
    for match in re.finditer(r"(?m)^\s*\[(\d+)\]\s+([\s\S]*?)(?=^\s*\[\d+\]|\Z)", bibliography):
        text = re.sub(r"(?m)^\s*\d+\s*\f?\s*$", "", match[2]).replace("\f", "")
        text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
        references[int(match[1])] = " ".join(text.split())
    with fitz.open(pdf) as doc:
        names = doc.resolve_names()
        if {key: value["page"] + 1 for key, value in names.items()} != manifest["destinations"]:
            raise ValueError("original named destinations changed")
        ordered = sorted(((key[5:], value["page"] + 1, -value["to"][1]) for key, value in names.items()
                          if key.startswith("cite.")), key=lambda row: (row[1], row[2]))
        actual = [{"key": row[0], "number": i, "page": row[1], "text": references[i]}
                  for i, row in enumerate(ordered, 1)]
        if actual != manifest["references"]:
            raise ValueError("original reference text or citation numbering changed")
        figure = manifest["figure"]
        pix = doc[figure["pdf_page"] - 1].get_pixmap(matrix=fitz.Matrix(figure["scale"], figure["scale"]),
                                                   clip=fitz.Rect(figure["crop_points"]), alpha=False)
        stored = fitz.Pixmap(str(source_root / figure["path"]))
        if (pix.width, pix.height, pix.samples) != (stored.width, stored.height, stored.samples):
            raise ValueError("original figure differs from the pinned PDF crop")
    return {"references": len(actual), "figure_pixels": [pix.width, pix.height], "manual_pdf_review": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify the recorded source PDF, page breaks and destinations")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--reading-source", action="store_true", help="also reproduce the reading copy reference text, citation numbers and figure pixels")
    args = parser.parse_args()
    statements = {r["id"]: r for r in json.loads((ROOT / "corpus/statements.json").read_bytes())}
    if inspect(args.pdf, statements) != json.loads((ROOT / MAP).read_bytes()):
        parser.exit(1, "original preprint map differs\n")
    if args.reading_source:
        manifest = json.loads((ROOT / "docs/original_source/manifest.json").read_bytes())
        print(inspect_reading_pdf(args.pdf, manifest, ROOT / "docs/original_source"))
    print("Original PDF and statement location map verified")
