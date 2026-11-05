#!/usr/bin/env python3
"""Compile the three Quartic papers and their formal reading routes for a static host."""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from zipfile import ZipFile, BadZipFile

from build_comparator_map import PASSAGE, lean_blocks, record_passages
from reading_evidence import evidence_resources
from reading_selection import audit_bindings, selection_resources
from build_lean_links import RECORD_LINK, REPOSITORY, USE, statement_end

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    "expert": "docs/expert_companion.md",
    "exposition": "docs/exposition.md",
    "reconstruction": "docs/reasoning_record.md",
}
SUPPLEMENT = "docs/verification_details.md"
ROUTES = "docs/reading_routes.json"
PROOF_INDEX = re.compile(r"docs/proof_index\.md#([\w-]+)")
HEADING = re.compile(r"^(#{1,6}) (.+)$", re.M)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def unique(rows, key):
    result = {}
    for row in rows:
        ident = row[key]
        if ident in result:
            raise ValueError(f"duplicate {key}: {ident}")
        result[ident] = row
    return result


def line_at(text, offset):
    return text.count("\n", 0, offset) + 1


def locate_quote(text, quote, context):
    if not quote or text.count(quote) != 1:
        raise ValueError(f"{context}: expected one occurrence of {quote!r}")
    pos = text.index(quote)
    # Include the paragraph's display math up to the next blank line.
    before = text.rfind("\n\n", 0, pos)
    after = text.find("\n\n", pos + len(quote))
    start = before + 2 if before >= 0 else 0
    end = after if after >= 0 else len(text.rstrip("\n"))
    return {"lines": [line_at(text, start), line_at(text, end)],
            "quote": quote, "sha256": digest(text[start:end].encode())}


def video_entry(video, routes):
    if video is None:
        return None
    if not re.fullmatch(r"[a-zA-Z0-9_-]{11}", video["youtube_id"]):
        raise ValueError("invalid YouTube video ID")
    previous = -1
    for chapter in video["chapters"]:
        second = chapter["start_seconds"]
        if type(second) is not int or second <= previous or chapter["route"] not in routes:
            raise ValueError(f"invalid video chapter: {chapter}")
        previous = second
    return video


class Edition:
    """Capture sources once. A publishable edition must match a single Git tree."""
    def __init__(self, root):
        self.root = root
        self.commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        self.inputs = {}
        self.resources = {}

    def read(self, path):
        if path not in self.inputs:
            self.inputs[path] = (self.root / path).read_bytes()
        return self.inputs[path]

    def json(self, path):
        return json.loads(self.read(path))

    def add(self, path, value):
        self.resources[path] = encoded(value)

    def verify_commit(self):
        listing = subprocess.check_output(["git", "ls-tree", "-r", "-z", self.commit], cwd=self.root)
        blobs = {}
        for item in listing.split(b"\0"):
            if item:
                meta, path = item.split(b"\t", 1)
                blobs[os.fsdecode(path)] = meta.split()[-1].decode()
        for path, data in self.inputs.items():
            header = f"blob {len(data)}\0".encode()
            if blobs.get(path) != hashlib.sha1(header + data).hexdigest():
                raise ValueError(f"{path} differs from {self.commit[:12]}; commit the edition before exporting")


def document(edition, path, text, links):
    """Expose source bytes, assets, outline and the citations actually used in prose."""
    edition.resources[path] = edition.read(path)
    assets = set(re.findall(r"!\[[^\n]*?\]\((figures/[^\s)]+)\)", text))
    paper = Path(path)
    for asset in sorted(assets):
        target = (paper.parent / asset).as_posix()
        edition.resources[target] = edition.read(target)
    bib = paper.with_suffix(".bib").as_posix()
    if path in PAPERS.values():
        edition.resources[bib] = edition.read(bib)
    outline = []
    for m in HEADING.finditer(text):
        outline.append({"line": line_at(text, m.start()), "level": len(m[1]), "title": m[2]})
    cites = []
    record_links = []
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("[") and re.match(r"^\[[^\]]+\]:", line):
            continue
        for match in RECORD_LINK.finditer(line):
            record_links.append({"line": n, "revision": match[1], "anchor": match[2],
                                 "url": match[0]})
        labels = set(USE.findall(line)) & links.keys()
        for label in PROOF_INDEX.findall(line):
            if label not in links:
                raise ValueError(f"{path}:{n}: missing proof-index target {label}")
            labels.add(label)
        cites.extend({"line": n, "target": label} for label in sorted(labels))
    title = re.search(r'^title: "(.+)"$', text, re.M)
    heading = re.sub(r"\s*\{[^}]+\}$", "", outline[0]["title"])
    return {"path": path, "title": title[1] if title else heading,
            "outline": outline, "citations": cites, "record_links": record_links,
            "assets": sorted((paper.parent / a).as_posix() for a in assets),
            "bibliography": bib if path in PAPERS.values() else None}


def formal_sources(edition, registry):
    """Keep statement ranges and full declarations in the edition cited by the papers."""
    pin = registry["commit"]
    if not re.fullmatch(r"[0-9a-f]{40}", pin):
        raise ValueError("formal reading registry requires an immutable revision")
    blocks = {}
    sources = {}
    for label, target in registry["links"].items():
        path = target["path"]
        if not target["pinned"]:
            raise ValueError(f"unpinned formal target: {label}")
        if not path.endswith(".lean"):
            continue
        key = f"pinned/{pin}/{path}"
        if key not in edition.resources:
            raw = subprocess.check_output(["git", "cat-file", "blob", f"{pin}:{path}"], cwd=edition.root)
            edition.resources[key] = raw
            blocks[path] = {b["name"]: b for b in lean_blocks(raw.decode())}
        ranges = {}
        for name in target.get("declarations", []):
            block = blocks[path][name]
            ranges[name] = {"statement": [block["line_start"], statement_end(block)],
                            "declaration": [block["line_start"], block["line_end"]]}
        if ranges:
            starts, ends = zip(*(r["statement"] for r in ranges.values()))
            if target["lines"] != [min(starts), max(ends)]:
                raise ValueError(f"{label}: statement source range differs from registry")
        sources[label] = {"source": key, "ranges": ranges}
    return sources


def print_downloads(edition, folder, accepted):
    """Admit only adjudicated PDFs whose paper sources still match the print edition."""
    if folder is None:
        return {}
    revision = accepted["source_revision"]
    if not re.fullmatch(r"[a-f0-9]{40}", revision) or set(accepted["files"]) != set(PAPERS):
        raise ValueError("invalid print edition")
    inputs = [*PAPERS.values(), "docs/*.bib", "docs/figures", "tools/render_papers.py",
              "tools/render_reasoning_record.py", SUPPLEMENT]
    diff = subprocess.run(["git", "diff", "--quiet", revision, "--", *inputs], cwd=edition.root)
    if diff.returncode:
        raise ValueError(f"paper sources differ from print edition {revision[:12]}")
    adjudication = edition.read(accepted["adjudication"]).decode()
    downloads = {}
    for paper, spec in accepted["files"].items():
        path = Path(spec["file"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"invalid PDF path: {path}")
        if isinstance(folder, ZipFile):
            names = folder.namelist()
            if names.count(path.as_posix()) != 1:
                raise ValueError(f"missing or duplicate PDF: {path}")
            raw = folder.read(path.as_posix())
        else:
            raw = (folder / path).read_bytes()
        if digest(raw) != spec["sha256"] or spec["sha256"] not in adjudication:
            raise ValueError(f"{paper}: PDF differs from the adjudicated reading copy")
        key = "print/" + path.name
        edition.resources[key] = raw
        downloads[paper] = {"resource": key, "source_revision": revision,
                            "adjudication": accepted["adjudication"]}
    return downloads


def compile_edition(edition, pdf_directory=None):
    config = edition.json(ROUTES)
    routes = unique(config["routes"], "id")
    link_registry = edition.json("docs/lean_links.json")
    links = link_registry["links"]
    source_ranges = formal_sources(edition, link_registry)
    statements = unique(edition.json("corpus/statements.json"), "id")
    correspondence = edition.json("docs/reasoning_record_correspondence.json")
    comparison = edition.json("corpus/comparator_map.json")
    for path, expected in comparison["inputs"].items():
        if digest(edition.read(path)) != expected:
            raise ValueError(f"stale Comparator map input: {path}")
    documents = {**PAPERS, "verification": SUPPLEMENT}
    texts = {key: edition.read(path).decode() for key, path in documents.items()}
    papers = {key: document(edition, path, texts[key], links) for key, path in documents.items()}
    passages = {}
    for key in ("reconstruction", "verification"):
        text = texts[key]
        verified, errors = record_passages(text, correspondence, documents[key])
        if errors or len(list(PASSAGE.finditer(text))) != len(verified):
            raise ValueError(f"{key}: duplicate or unbound passage {errors}")
        for ident, row in verified.items():
            if ident in passages:
                raise ValueError(f"duplicate passage: {ident}")
            passages[ident] = {"document": key, "lines": [row["line_start"], row["line_end"]],
                               "sha256": row["sha256"], "claims": row["claims"],
                               "statement_ids": [c for c in row["claims"] if c in statements]}
    if passages.keys() != unique(correspondence["passages"], "id").keys():
        raise ValueError("correspondence contains missing passages")

    by_target = defaultdict(list)
    by_passage = defaultdict(list)
    compiled = []
    for ident, row in routes.items():
        anchor = row["reconstruction"]
        if anchor not in passages or passages[anchor]["document"] != "reconstruction":
            raise ValueError(f"{ident}: unknown reconstruction passage {anchor}")
        if not row["lean"] or set(row["lean"]) - links.keys():
            raise ValueError(f"{ident}: missing formal reading target")
        locations = {k: locate_quote(texts[k], row[k], f"{ident}/{k}") for k in ("expert", "exposition")}
        compiled.append({"id": ident, "title": row["title"], "locations": locations,
                         "reconstruction": anchor, "lean": row["lean"]})
        by_passage[anchor].append(ident)
        for label in row["lean"]:
            by_target[label].append(ident)

    # Preserve the origin of each reverse edge. A shared topic is an editorial judgment.
    declarations = defaultdict(lambda: {"targets": [], "statements": [], "passages": []})
    for label, target in links.items():
        for name in target.get("declarations", []):
            declarations[name]["targets"].append(label)
    for ident, statement in statements.items():
        for name in sorted({tie["declaration"] for tie in statement["lean"]}):
            declarations[name]["statements"].append(ident)
    for name, row in comparison["declarations"].items():
        for ref in row["record_references"]:
            anchor = ref["anchor"]
            if passages[anchor]["sha256"] != ref["passage_sha256"]:
                raise ValueError(f"{name}: stale formal passage reference {anchor}")
            declarations[name]["passages"].append({"id": anchor, "join": ref["join"]})

    # Record links in the short papers can intentionally cite an older reconstruction.
    # Offer a local jump only when both ends refer to exactly the same passage body.
    record_pins = {}
    record_citations = defaultdict(list)
    for key in PAPERS:
        for ref in papers[key]["record_links"]:
            pin = ref["revision"]
            anchor = ref["anchor"]
            if not anchor or anchor not in passages or pin == "main":
                continue
            if pin not in record_pins:
                old = subprocess.check_output(["git", "cat-file", "blob", f"{pin}:{PAPERS['reconstruction']}"],
                                              cwd=edition.root).decode()
                record_pins[pin] = {m[1]: digest(m[2].encode()) for m in PASSAGE.finditer(old)}
            if record_pins[pin].get(anchor) == passages[anchor]["sha256"]:
                ref["edition_passage"] = anchor
                record_citations[anchor].append({"document": key, "line": ref["line"]})

    cited_at = defaultdict(list)
    for key, paper in papers.items():
        for cite in paper["citations"]:
            cited_at[cite["target"]].append({"document": key, "line": cite["line"]})
    by_statement = defaultdict(list)
    for ident, passage in passages.items():
        for statement in passage["statement_ids"]:
            by_statement[statement].append(ident)

    entrances = config["entrances"]
    if set(entrances) != set(PAPERS):
        raise ValueError("each paper needs an audience entrance")
    for key, entry in entrances.items():
        if not all(entry.get(k) for k in ("audience", "question", "preview", "stops")):
            raise ValueError(f"incomplete audience entrance: {key}")
        if set(entry["stops"]) - routes.keys():
            raise ValueError(f"unknown reading stop: {key}")
    evidence_resources(edition, statements, by_statement, comparison, config["semantic_probes"])
    selection_resources(edition, config, papers, texts, passages, compiled, statements, links, comparison,
                        locate_quote)
    edition.add("reading.json", {"papers": papers, "entrances": entrances,
               "applications": "selection/applications.json",
               "downloads": print_downloads(edition, pdf_directory, config["print_edition"]),
               "fidelity": {ident: f"fidelity/{ident}.json" for ident in statements},
               "routes": compiled, "video": video_entry(config["video"], routes)})
    edition.add("provenance.json", {
        "papers": {"origin": "manuscript", "content": "Exact Markdown from the edition revision."},
        "routes": {"origin": "ai_authored_navigation", "source": ROUTES,
                   "content": "Paragraph and topic selections across accounts. Editorial reading suggestions."},
        "corpus/lean_dependencies.json": {"origin": "lean_environment",
            "producer": "lean/scripts/Reach.lean",
            "content": "Constant dependencies from types and bodies. See traversal_scope and hidden_paths."},
        "corpus/evidence-graph.json": {"origin": "statement_ledger",
            "producer": "tools/build_corpus.py", "content": "Informal dependencies between statement records."},
        "fidelity": {"origin": "reviewed_statement_ties", "source": "corpus/ties.json",
            "content": "Reviewer, effective relation, hypotheses and review freshness apply to each individual tie."},
        "applications": {"origin": "lean_environment_and_editorial_navigation",
            "producer": "tools/ReadApplications.lean", "source": "docs/reading_applications.json",
            "content": "Formal binder arguments are scoped to the compiled caller/callee pair. The source site "
                       "and associated passage are selected editorially. Paper equivalence uses the fidelity records."},
        "checks.json": {"origin": "comparator_configurations_and_receipts",
            "content": "Each configuration identifies its challenge, solution, permitted axioms and recorded outcome."},
        "axiom-audits.json": {"origin": "lean_print_axioms",
            "content": "Recorded transitive axioms for named declarations in the indexed round-three inspection."},
        "semantic_probes": {"origin": "authored_question_and_recorded_lean_example",
            "content": "A probe tests the named example or alternative definition. An empty list means no indexed probe."}})
    edition.add("passages.json", passages)
    edition.add("formal-sources.json", source_ranges)
    edition.add("reverse.json", {"routes_by_target": by_target, "routes_by_passage": by_passage,
               "citations_by_target": cited_at, "record_citations_by_passage": record_citations,
               "passages_by_statement": by_statement,
               "declarations": declarations})
    for path in ("docs/lean_links.json", "corpus/statements.json", "corpus/comparator_map.json",
                 "corpus/lean_dependencies.json", "corpus/evidence-graph.json"):
        edition.resources[path] = edition.read(path)


def atomic_write(dest, data):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False) as fp:
        tmp = Path(fp.name)
    try:
        tmp.write_bytes(data)
        os.chmod(tmp, 0o644)
        os.replace(tmp, dest)
    finally:
        tmp.unlink(missing_ok=True)


def export(edition, out):
    edition.verify_commit()
    resources = {}
    for path, data in sorted(edition.resources.items()):
        sha = digest(data)
        filename = f"objects/{sha}{Path(path).suffix}"
        atomic_write(out / filename, data)
        resources[path] = {"href": filename, "sha256": sha, "bytes": len(data)}
    manifest = {"schema": "quartic-reading-api-v1", "repository": REPOSITORY,
                "revision": edition.commit, "resources": resources}
    manifest["permalink"] = "edition-" + digest(encoded(manifest)) + ".json"
    raw = encoded(manifest)
    atomic_write(out / manifest["permalink"], raw)
    atomic_write(out / "index.json", raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--audit-bindings", metavar="CHECKOUT", type=Path, help="report every editorial binding affected by a manuscript draft")
    mode.add_argument("--check", action="store_true", help="validate working sources without writing")
    mode.add_argument("--output", type=Path, help="export the committed edition to this directory")
    media = parser.add_mutually_exclusive_group()
    media.add_argument("--pdf-archive", type=Path, help="portable ZIP of the three adjudicated render outputs")
    media.add_argument("--pdf-directory", type=Path, help="include the adjudicated three-paper render directory")
    args = parser.parse_args()
    try:
        edition = Edition(ROOT)
        if args.audit_bindings:
            report = audit_bindings(edition, args.audit_bindings, {**PAPERS, "verification": SUPPLEMENT},
                                    edition.json(ROUTES), locate_quote)
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return int(bool(report["needs_review"]))
        if args.pdf_archive:
            with ZipFile(args.pdf_archive) as archive:
                compile_edition(edition, archive)
        else:
            compile_edition(edition, args.pdf_directory)
        if args.output:
            export(edition, args.output)
        print(f"Quartic reading API: {len(edition.resources)} resources validated")
    except (OSError, KeyError, ValueError, BadZipFile, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"reading API: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
