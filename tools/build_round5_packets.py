#!/usr/bin/env python3
"""Build the five round-five critique packets, bound by hash to the current draft bytes."""

import argparse
import datetime
import difflib
import json
import os
from pathlib import Path
import posixpath
import re
import subprocess
import sys
import tempfile
import zipfile
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_round4_packets as round4
import check_repository as repository_checks

previous = round4.previous  # round three: digest, encoding, request composition, archive writer
check_packets = previous.check_packets
digest, encoded = previous.digest, previous.encoded

ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN = "round5"
JOBS = {
    "expert_referee_short": "Referee the short expert companion",
    "quantum_mechanism": "The quantum upper bound in both papers",
    "classical_mechanism": "The randomized lower bound in both papers",
    "exposition_for_students": "Could a strong student learn the result from the exposition?",
    "long_record_navigation": "The long record as the destination of the short paper's links",
}
PREFIX = {"expert_referee_short": "ER", "quantum_mechanism": "QM", "classical_mechanism": "CM",
          "exposition_for_students": "ES", "long_record_navigation": "LR"}
DRAFTS = ("docs/expert_companion.md", "docs/exposition.md")
REPOSITORY_FILES = (
    "docs/expert_companion.md", "docs/expert_companion.bib", "docs/exposition.md", "docs/exposition.bib",
    "docs/reasoning_record.md", "docs/reasoning_record.bib",
    "lean/QuarticCorpus/Unconditional/Challenge.lean", "lean/QuarticCorpus/Unconditional/Solution.lean",
    "lean/QuarticCorpus/Unconditional/comparator.json", "corpus/comparator_map.json",
    "lean/scripts/Reach.lean", "lean/QuarticQuery/Paper/ConstructionFamily.lean",
    "lean/lean-toolchain", "lean/lakefile.toml", "lean/lake-manifest.json", "lean/README.md", "LICENSE")
OPTIONAL_FILES = ("docs/lean_links.json",)
NAVIGATION_FILES = ("docs/reasoning_record_correspondence.json", "docs/reasoning_record_review.json",
                    "docs/statement_evidence_contract.md")
REVIEW_RECEIPT = "docs/reasoning_record_review.json"
EXEMPLAR_ROOT = "research/returns/round4/members/02_short_expert/source_packet"
EXEMPLARS = {
    "exemplars/long-reasoning-record.md": "exemplars/long-reasoning-record.md",
    "exemplars/short-paper.md": "exemplars/short-paper.md",
    "exemplars/expository.md": "exemplars/expository.md",
    "exemplars/qaoa-sk/long/reasoning-record.pdf": "writing/structural/lean-exposition/papers/qaoa-sk/long/reasoning-record.pdf",
    "exemplars/qaoa-sk/short/paper.pdf": "writing/structural/lean-exposition/papers/qaoa-sk/short/paper.pdf",
    "exemplars/qaoa-sk/expository/main.pdf": "writing/structural/lean-exposition/papers/qaoa-sk/expository/main.pdf",
}
REPOSITORY_URL = re.compile(r"^https://github\.com/wcook04/quartic-query-lean/(blob|tree)/([^/]+)/(.+)$")

# Exact editions were read from each supplied original's first page.
CATALOG = {
    "quartic-ref-01-forrelation-a-problem-that-optimally-separ": ("Aaronson–Ambainis, Forrelation (SICOMP 2018)", "arXiv:1411.5729v1"),
    "quartic-ref-02-separations-in-query-complexity-using-chea": ("Aaronson–Ben-David–Kothari, Separations in query complexity using cheat sheets (STOC 2016)", "arXiv:1511.01937v2"),
    "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i": ("Aaronson–Ben-David–Kothari–Rao–Tal, Degree vs. approximate degree and quantum implications of Huang's sensitivity theorem (STOC 2021)", "arXiv:2010.12629v1"),
    "quartic-ref-04-separations-in-query-complexity-based-on-p": ("Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs, Separations in query complexity based on pointer functions (JACM 2017)", "arXiv:1506.04719v3"),
    "quartic-ref-05-near-optimal-separations-of-certificate-co": ("Ambainis–Iraids–Kokainis, Near-optimal separations of certificate complexity from randomized and quantum query complexity (2026)", "arXiv:2609.11664v2"),
    "quartic-ref-06-k-forrelation-optimally-separates-quantum": ("Bansal–Sinha, k-Forrelation optimally separates quantum and classical query complexity (STOC 2021)", "arXiv:2008.07003v3; STOC proceedings PDF in supplements/"),
    "quartic-ref-09-randomized-query-complexity-can-beat-certi": ("Ben-David–Kothari, Randomized query complexity can beat certificate complexity (2026)", "arXiv:2609.15063v1"),
    "quartic-ref-10-strengths-and-weaknesses-of-quantum-comput": ("Bennett–Bernstein–Brassard–Vazirani, Strengths and weaknesses of quantum computing (SICOMP 1997)", "arXiv:quant-ph/9701001v1"),
    "quartic-ref-11-tight-bounds-on-quantum-searching": ("Boyer–Brassard–Høyer–Tapp, Tight bounds on quantum searching (1998)", "arXiv:quant-ph/9605034v1"),
    "quartic-ref-12-quantum-amplitude-amplification-and-estima": ("Brassard–Høyer–Mosca–Tapp, Quantum amplitude amplification and estimation (2002)", "arXiv:quant-ph/0005055v1"),
    "quartic-ref-13-improved-direct-product-theorems-for-rando": ("Drucker, Improved direct product theorems for randomized query complexity (Comput. Complexity 2012)", "arXiv:1005.0644v2; journal-era PDF in supplements/"),
    "quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu": ("Dürr–Høyer, A quantum algorithm for finding the minimum (1996)", "arXiv:quant-ph/9607014v2"),
    "quartic-ref-15-deterministic-communication-vs-partition-n": ("Göös–Pitassi–Watson, Deterministic communication vs. partition number (FOCS 2015)", "ECCC TR15-050"),
    "quartic-ref-16-a-fast-quantum-mechanical-algorithm-for-da": ("Grover, A fast quantum mechanical algorithm for database search (STOC 1996)", "arXiv:quant-ph/9605043"),
    "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo": ("Huang, Induced subgraphs of hypercubes and a proof of the sensitivity conjecture (Annals 2019)", "arXiv:1907.00847v2"),
    "quartic-ref-18-randomized-and-quantum-query-complexities": ("Mande–Paraashar–Saurabh, Randomized and quantum query complexities of finding a king in a tournament (FSTTCS 2023)", "arXiv:2308.02472v1"),
    "quartic-ref-22-towards-proving-strong-direct-product-theo": ("Shaltiel, Towards proving strong direct product theorems (Comput. Complexity 2003)", "ECCC TR01-009"),
    "quartic-ref-23-an-optimal-separation-of-randomized-and-qu": ("Sherstov–Storozhenko–Wu, An optimal separation of randomized and quantum query complexity (SICOMP 2023)", "arXiv:2008.10223v4"),
    "quartic-ref-26-towards-optimal-separations-between-quantu": ("Tal, Towards optimal separations between quantum and randomized query complexities (FOCS 2020)", "arXiv:1912.12561v1"),
    "arxiv-2103-11604": ("Girish–Tal–Wu, Fourier growth of parity decision trees (CCC 2021)", "arXiv:2103.11604"),
    "quartic-lit-girish-forrelation-is-extremally-hard": ("Girish–Servedio, Forrelation is extremally hard (ITCS 2026)", "arXiv:2508.02514v1; ITCS publisher PDF in supplements/"),
    "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error": ("Høyer–Mosca–de Wolf, Quantum search on bounded-error inputs (ICALP 2003)", "arXiv:quant-ph/0304052"),
    "quartic-lit-hoyer-lee-spalek-negative-weights": ("Høyer–Lee–Špalek, Negative weights make adversaries stronger (STOC 2007)", "arXiv:quant-ph/0611054"),
    "quartic-lit-buhrman-dewolf-decision-tree-survey": ("Buhrman–de Wolf, Complexity measures and decision tree complexity: a survey (Theoretical Computer Science 2002)", "supplied author PDF"),
    "quartic-ref-19-exact-quantum-query-complexity-for-total-b": ("Midrijanis, Exact quantum query complexity for total Boolean functions (2004)", "arXiv:quant-ph/0403168v2"),
    "quartic-lit-nisan-szegedy-degree-of-boolean-functions": ("Nisan–Szegedy, On the degree of Boolean functions as real polynomials (Comput. Complexity 1994)", "Comput. Complexity 4:301–313, journal PDF"),
    "quartic-lit-dewolf-quantum-computing-lecture-notes": ("de Wolf, Quantum computing: lecture notes", "arXiv:1907.09415v6"),
    "quartic-lit-bansal-sinha-qip2021-slides": ("Bansal–Sinha, k-Forrelation optimally separates quantum and classical query complexity, QIP 2021 talk slides", "conference slides"),
    "quartic-lit-beame-kornerup-whitmeyer-quantum-direct-products": ("Beame–Kornerup–Whitmeyer, quantum direct product theorems (2026)", "arXiv:2609.26678v2"),
}
HISTORY = ["quartic-ref-01-forrelation-a-problem-that-optimally-separ", "quartic-ref-02-separations-in-query-complexity-using-chea",
           "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i", "quartic-ref-04-separations-in-query-complexity-based-on-p",
           "quartic-ref-15-deterministic-communication-vs-partition-n", "quartic-ref-26-towards-optimal-separations-between-quantu",
           "quartic-ref-06-k-forrelation-optimally-separates-quantum", "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
           "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo"]
COMPARISON = ["quartic-ref-09-randomized-query-complexity-can-beat-certi", "quartic-ref-05-near-optimal-separations-of-certificate-co"]
LITERATURE = {
    "expert_referee_short": [*HISTORY, *COMPARISON, "arxiv-2103-11604", "quartic-lit-girish-forrelation-is-extremally-hard",
        "quartic-lit-bansal-sinha-qip2021-slides", "quartic-lit-buhrman-dewolf-decision-tree-survey",
        "quartic-ref-19-exact-quantum-query-complexity-for-total-b", "quartic-lit-nisan-szegedy-degree-of-boolean-functions"],
    "quantum_mechanism": ["quartic-ref-12-quantum-amplitude-amplification-and-estima", "quartic-ref-11-tight-bounds-on-quantum-searching",
        "quartic-lit-hoyer-mosca-dewolf-quantum-search-bounded-error", "quartic-ref-14-a-quantum-algorithm-for-finding-the-minimu",
        "quartic-ref-18-randomized-and-quantum-query-complexities", *COMPARISON, "quartic-ref-16-a-fast-quantum-mechanical-algorithm-for-da",
        "quartic-ref-10-strengths-and-weaknesses-of-quantum-comput", "quartic-ref-01-forrelation-a-problem-that-optimally-separ",
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-lit-dewolf-quantum-computing-lecture-notes"],
    "classical_mechanism": ["quartic-ref-13-improved-direct-product-theorems-for-rando", "quartic-ref-22-towards-proving-strong-direct-product-theo",
        "quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-ref-04-separations-in-query-complexity-based-on-p",
        "quartic-ref-06-k-forrelation-optimally-separates-quantum", "quartic-ref-23-an-optimal-separation-of-randomized-and-qu",
        "quartic-lit-girish-forrelation-is-extremally-hard", "quartic-lit-beame-kornerup-whitmeyer-quantum-direct-products",
        "quartic-lit-buhrman-dewolf-decision-tree-survey"],
    "exposition_for_students": ["quartic-lit-dewolf-quantum-computing-lecture-notes", "quartic-lit-buhrman-dewolf-decision-tree-survey",
        "quartic-ref-01-forrelation-a-problem-that-optimally-separ", "quartic-ref-02-separations-in-query-complexity-using-chea",
        "quartic-ref-03-degree-vs-approximate-degree-and-quantum-i", "quartic-ref-16-a-fast-quantum-mechanical-algorithm-for-da",
        "quartic-ref-11-tight-bounds-on-quantum-searching", "quartic-ref-12-quantum-amplitude-amplification-and-estima",
        "quartic-ref-17-induced-subgraphs-of-hypercubes-and-a-proo", "quartic-lit-bansal-sinha-qip2021-slides"],
    "long_record_navigation": ["quartic-ref-02-separations-in-query-complexity-using-chea", "quartic-ref-06-k-forrelation-optimally-separates-quantum",
        "quartic-ref-12-quantum-amplitude-amplification-and-estima", "quartic-ref-13-improved-direct-product-theorems-for-rando"],
}
# Sources the drafts or preprint cite that have no local original. Identifiers come from the preprint's bibliography.
CITED_ONLY = {
    "yao1977": ("Yao, Probabilistic computations: toward a unified measure of complexity", "FOCS 1977, pp. 222–227 (preprint ref. [27]); no arXiv version"),
    "nisan1991": ("Nisan, CREW PRAMs and decision trees", "SIAM J. Comput. 20(6):999–1007, 1991 (preprint ref. [20])"),
    "bss2003": ("Barnum–Saks–Szegedy, Quantum query complexity and semidefinite programming", "CCC 2003, pp. 179–193 (preprint ref. [7])"),
}
CITED_ONLY_BY_JOB = {
    "expert_referee_short": ["yao1977", "nisan1991", "bss2003"],
    "quantum_mechanism": ["bss2003"],
    "classical_mechanism": ["yao1977", "nisan1991"],
    "exposition_for_students": ["yao1977", "nisan1991"],
    "long_record_navigation": ["yao1977"],
}
LITERATURE_FILES = ("extracted.md", "source.pdf", "source.tar.gz", "source.tex")
# Packets name no individual reader and carry no correspondence or transcript.
# Generic markers live here; patterns naming a specific person stay outside the
# repository, one regular expression per line, in the file named by
# QUARTIC_PRIVATE_READER_PATTERNS (default ~/.config/quartic/private_reader_patterns.txt).
GENERIC_LEAKS = (r"round4_papers", r"email exchange", r"\btextfile\b", r"\btranscript of an interview\b")
PRIVATE_PATTERNS = Path(os.environ.get(
    "QUARTIC_PRIVATE_READER_PATTERNS",
    Path.home() / ".config/quartic/private_reader_patterns.txt"))


def reader_leak_patterns(path=PRIVATE_PATTERNS):
    private = []
    if Path(path).is_file():
        private = [line.strip() for line in Path(path).read_text(encoding="utf-8").splitlines()
                   if line.strip() and not line.lstrip().startswith("#")]
    return [re.compile(p, re.I) for p in (*GENERIC_LEAKS, *private)]


READER_LEAKS = reader_leak_patterns()
PRIVATE_PARTS = {".codex", ".claude", "attachments", "Library"}
EXCLUDED_MEMBERS = re.compile(r"(^|/)(round4_papers\.(md|json)|input_?10[^/]*)$", re.I)
TEXT_SUFFIXES = {".md", ".json", ".lean", ".bib", ".txt", ".tex", ".toml", ".diff"}


def render_request(job, requests_dir):
    texts = [(requests_dir / name).read_text(encoding="utf-8") for name in ("common.md", f"{job}.md", "boundaries.md")]
    fields = sorted(f for _, f, _, _ in __import__("string").Formatter().parse(texts[0]) if f is not None)
    if fields != ["boundary", "job", "title"]:
        raise ValueError("round-five common.md needs {title}, {job} and {boundary} exactly once")
    return texts[0].format(title=JOBS[job], job=texts[1], boundary=texts[2])


def safe_source(path):
    path = Path(path)
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"missing or nonregular source: {path}")
    if PRIVATE_PARTS & set(path.resolve().parts) or re.fullmatch(r"input_?10(?:[._-].*)?", path.name, re.I):
        raise ValueError(f"private source cannot enter a packet: {path}")
    return path


def git(root, *args, check=True):
    return subprocess.run(["git", "-C", str(root), *args], check=check, capture_output=True)


def accepted_record(root):
    """Return the accepted record hash and, when Git still holds those bytes, the accepted text."""
    receipt = root / REVIEW_RECEIPT
    if not receipt.is_file():
        return None, None
    accepted = json.loads(receipt.read_bytes()).get("record_sha256")
    log = git(root, "log", "--format=%H", "-n", "200", "--", "docs/reasoning_record.md", check=False)
    for commit in log.stdout.decode().split():
        blob = git(root, "show", f"{commit}:docs/reasoning_record.md", check=False)
        if blob.returncode == 0 and digest(blob.stdout) == accepted:
            return accepted, (commit, blob.stdout)
    return accepted, None


def anchors(text):
    found = set(re.findall(r"<a\s+(?:id|name)=\"([^\"]+)\"", text)) | set(re.findall(r"\{#([^}\s]+)", text))
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*(?:\{[^}]*\})?$", text):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        found.add(slug)
    return found


def link_targets(text):
    text = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text)
    text = re.sub(r"`[^`\n]+`", "", text)
    targets = [m.group(1).strip("<>") for m in repository_checks.LINK.finditer(text)]
    targets += [m.group(1) or m.group(2) for m in re.finditer(r"(?m)^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", text)]
    targets += re.findall(r"<(https?://[^>\s]+)>", text)
    return targets


def resolve_draft_links(root):
    """Map every draft link to a packet member; relative links must resolve, remote ones are recorded."""
    rows, members = [], {}
    for draft in DRAFTS:
        text = (root / draft).read_text(encoding="utf-8")
        for target in link_targets(text):
            url = urlsplit(target)
            row = {"from": "repository/" + draft, "link": target}
            match = REPOSITORY_URL.match(f"{url.scheme}://{url.netloc}{url.path}") if url.scheme else None
            if not url.scheme and not url.netloc:
                if not url.path:
                    row.update(kind="same_document_anchor", anchor=url.fragment,
                               anchor_found=url.fragment in anchors(text))
                    rows.append(row)
                    continue
                path = posixpath.normpath(posixpath.join(posixpath.dirname(draft), unquote(url.path)))
                ref, kind = None, "relative"
            elif match:
                kind, ref, path = "repository_" + match.group(1), match.group(2), unquote(match.group(3)).rstrip("/")
            else:
                row["kind"] = "external"
                rows.append(row)
                continue
            if path.startswith(("../", "/")):
                raise ValueError(f"draft link escapes the repository: {draft} -> {target}")
            local = root / path
            row.update(kind=kind, ref=ref, member="repository/" + path, exists_locally=local.exists())
            if kind == "relative" and not local.is_file():
                raise ValueError(f"missing draft link target: {draft} -> {target}")
            if local.is_file():
                members["repository/" + path] = safe_source(local)
                current = local.read_bytes()
                pinned = None
                if ref and re.fullmatch(r"[0-9a-f]{7,40}", ref):
                    shown = git(root, "show", f"{ref}:{path}", check=False)
                    pinned = shown.stdout if shown.returncode == 0 else None
                    row["pinned_revision_available"] = pinned is not None
                    if pinned is not None:
                        row["pinned_differs_from_packaged"] = pinned != current
                checked = pinned if pinned is not None else current
                fragment = url.fragment
                if fragment:
                    lines = re.fullmatch(r"L(\d+)(?:-L(\d+))?", fragment)
                    if lines:
                        count = checked.count(b"\n") + (0 if checked.endswith(b"\n") else 1)
                        row["line_range_valid"] = int(lines.group(1)) >= 1 and int(lines.group(2) or lines.group(1)) <= count
                    elif path.endswith(".md"):
                        row["anchor_found"] = fragment in anchors(checked.decode("utf-8"))
            elif local.is_dir():
                row["directory"] = True
            rows.append(row)
    problems = [r for r in rows if r.get("anchor_found") is False or r.get("line_range_valid") is False
                or (r["kind"].startswith("repository") and not r.get("exists_locally"))]
    return members, {"schema": "quartic-round5-link-map-v1", "links": rows, "problem_count": len(problems),
        "interpretation": "Repository URLs map to the packaged current file at repository/<path>. Line ranges and "
        "anchors are checked against the pinned revision when the link names a commit that Git still holds, "
        "otherwise against the packaged file. A problem row is a reader-visible defect worth a finding."}


def inputs(job, *, root, requests_dir, annexes, paper_annex, expert_pdf, exposition_pdf, record_pdf):
    if job not in JOBS:
        raise ValueError(f"unknown round-five job: {job}")
    files = {}

    def add(member, source, role, label):
        check_packets.check_name(member)
        if EXCLUDED_MEMBERS.search(member):
            raise ValueError(f"excluded member cannot enter a packet: {member}")
        if member.casefold() in {n.casefold() for n in files}:
            return
        files[member] = (safe_source(source), role, label)

    for name in REPOSITORY_FILES:
        add("repository/" + name, root / name, "current_draft_or_statement", "repository:" + name)
    for name in OPTIONAL_FILES:
        if (root / name).is_file():
            add("repository/" + name, root / name, "optional_lean_link_index", "repository:" + name)
    add("repository/docs/expert_companion.pdf", expert_pdf, "rendered_working_draft", "external:expert_companion.pdf")
    add("repository/docs/exposition.pdf", exposition_pdf, "rendered_working_draft", "external:exposition.pdf")
    add("repository/docs/reasoning_record.pdf", record_pdf, "record_reading_copy", "external:reasoning_record.pdf")
    linked, _ = resolve_draft_links(root)
    for member, source in linked.items():
        add(member, source, "draft_link_target", "repository:" + member.split("/", 1)[1])
    for name in ("source.pdf", "extracted.md"):
        add("paper/" + name, paper_annex / name, "primary_preprint", "annex:preprint/" + name)
    for member, path in EXEMPLARS.items():
        add(member, root / EXEMPLAR_ROOT / path, "writing_exemplar_other_theorem", "repository:" + EXEMPLAR_ROOT + "/" + path)
    for slug in LITERATURE[job]:
        folder = annexes / slug
        found = [name for name in LITERATURE_FILES if (folder / name).is_file()]
        if "extracted.md" not in found or len(found) < 2:
            raise ValueError(f"literature original or text missing; list it as cited-only instead: {folder}")
        supplements = sorted(p.name for p in (folder / "supplements").glob("*.pdf")) if (folder / "supplements").is_dir() else []
        for name in found:
            add(f"literature/{slug}/{name}", folder / name, "primary_literature", f"annex:{slug}/{name}")
        for name in supplements:
            add(f"literature/{slug}/supplements/{name}", folder / "supplements" / name, "primary_literature_edition",
                f"annex:{slug}/supplements/{name}")
    if job == "long_record_navigation":
        for name in NAVIGATION_FILES:
            add("repository/" + name, root / name, "record_navigation_source", "repository:" + name)
        closure, _ = round4.linked_sources(root, {"repository/docs/reasoning_record.md": (root / "docs/reasoning_record.md", "")})
        for member, (source, _) in closure.items():
            add(member, source, "record_link_target", "repository:" + member.split("/", 1)[1])
        pdf_files, _ = round4.pdf_reading_sources(root, {"pdf": str(record_pdf), "pdf_sha256": digest(Path(record_pdf).read_bytes())})
        for member, (source, _) in pdf_files.items():
            add(member, source, "record_pdf_link_target", "repository:" + member.split("/", 1)[1])
    return files


def source_status(root, data, record_pdf):
    accepted, earlier = accepted_record(root)
    current = data["repository/docs/reasoning_record.md"]
    status = {"schema": "quartic-round5-source-status-v1",
        "status": "unreviewed working drafts",
        "drafts": {name: digest(data[name]) for name in sorted(data) if name.startswith("repository/docs/")
                   and name.rsplit("/", 1)[-1].split(".")[0] in {"expert_companion", "exposition"}},
        "record": {"markdown_sha256": digest(current), "pdf_sha256": digest(data["repository/docs/reasoning_record.pdf"]),
                   "accepted_review_record_sha256": accepted, "markdown_matches_accepted_review": digest(current) == accepted},
        "repository_commit": git(root, "rev-parse", "HEAD").stdout.decode().strip(),
        "acceptance_gate": "not applied: the record was edited after its accepted review and the corpus was regenerated; "
            "these hashes bind the packet to the exact bytes supplied."}
    diff = None
    if earlier is not None and digest(current) != accepted:
        commit, old = earlier
        diff = "".join(difflib.unified_diff(old.decode().splitlines(True), current.decode().splitlines(True),
            f"accepted/{commit[:12]}/docs/reasoning_record.md", "current/docs/reasoning_record.md")).encode()
        status["record"]["pdf_rendered_from"] = f"the accepted Markdown, as last changed at commit {commit}"
        status["record"]["since_pdf_diff"] = "repository/docs/reasoning_record.since_pdf.diff"
        status["record"]["changed_lines"] = sum(1 for line in diff.decode().splitlines()
                                                if line[:1] in "+-" and not line.startswith(("+++", "---")))
    return status, diff


def literature_section(job, data):
    lines = ["## Literature in this packet", ""]
    for slug in LITERATURE[job]:
        citation, identifier = CATALOG.get(slug, (slug, "see extracted.md"))
        originals = sorted(n for n in data if n.startswith(f"literature/{slug}/") and not n.endswith("extracted.md"))
        lines.append(f"- {citation}; {identifier}. Text: [extracted.md](literature/{slug}/extracted.md); original: "
                     + ", ".join(f"[{n.rsplit('/', 1)[-1]}]({n})" for n in originals) + ".")
    lines += ["", "## Cited but not supplied", "",
              "Use these identifiers and locators only; do not claim to have read them.", ""]
    lines += [f"- {CITED_ONLY[key][0]}: {CITED_ONLY[key][1]}." for key in CITED_ONLY_BY_JOB[job]]
    return "\n".join(lines) + "\n"


def packet_map(job, data):
    rows = [("The expert companion", "repository/docs/expert_companion.md", "repository/docs/expert_companion.pdf"),
            ("The exposition", "repository/docs/exposition.md", "repository/docs/exposition.pdf"),
            ("The long reasoning record", "repository/docs/reasoning_record.md", "repository/docs/reasoning_record.pdf"),
            ("The preprint", "paper/extracted.md", "paper/source.pdf")]
    lines = ["## Packet map", ""]
    lines += [f"- {label}: [Markdown]({md}), [PDF]({pdf})." for label, md, pdf in rows]
    lines += ["- Source hashes and draft status: [SOURCE_STATUS.json](SOURCE_STATUS.json); every draft link and its target: "
              "[LINK_MAP.json](LINK_MAP.json).",
              "- The Lean statement: [Challenge.lean](repository/lean/QuarticCorpus/Unconditional/Challenge.lean), "
              "[Solution.lean](repository/lean/QuarticCorpus/Unconditional/Solution.lean), "
              "[comparator.json](repository/lean/QuarticCorpus/Unconditional/comparator.json), "
              "[comparator_map.json](repository/corpus/comparator_map.json), "
              "[ConstructionFamily.lean](repository/lean/QuarticQuery/Paper/ConstructionFamily.lean).",
              "- Exemplars about another theorem: [long record](exemplars/long-reasoning-record.md) "
              "([PDF](exemplars/qaoa-sk/long/reasoning-record.pdf)), [short paper](exemplars/short-paper.md) "
              "([PDF](exemplars/qaoa-sk/short/paper.pdf)), [expository paper](exemplars/expository.md) "
              "([PDF](exemplars/qaoa-sk/expository/main.pdf))."]
    if "repository/docs/lean_links.json" in data:
        lines.append("- The Lean-link index: [lean_links.json](repository/docs/lean_links.json).")
    if "repository/docs/reasoning_record.since_pdf.diff" in data:
        lines.append("- Record text changed since its PDF: [diff](repository/docs/reasoning_record.since_pdf.diff).")
    if job == "long_record_navigation":
        lines.append("- The record's own link targets: [READING_LINK_CLOSURE.json](READING_LINK_CLOSURE.json).")
    lines.append("- Every member and its SHA-256: `manifest.json`.")
    return "\n".join(lines) + "\n"


def check_readme_links(request, data):
    for target in link_targets(request):
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        member = posixpath.normpath(unquote(url.path))
        if member not in data and member != "manifest.json" and not any(n.startswith(member.rstrip("/") + "/") for n in data):
            raise ValueError(f"READ_ME_FIRST link does not resolve inside the packet: {target}")


def check_reader_leaks(data, request):
    blobs = dict(data, **{"READ_ME_FIRST.md": request.encode()})
    for name, blob in blobs.items():
        if name.startswith(("literature/", "paper/")) or Path(name).suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = blob.decode("utf-8", "ignore")
        for pattern in READER_LEAKS:
            match = pattern.search(text)
            if match:
                raise ValueError(f"packet member names a private reader or source: {name}: {match.group(0)!r}")
        if "/.codex/" in text:
            raise ValueError(f"packet member references a private agent path: {name}")


def prepare(job, **options):
    root = options["root"]
    files = inputs(job, **options)
    data = {name: source.read_bytes() for name, (source, _, _) in files.items()}
    status, diff = source_status(root, data, options["record_pdf"])
    if diff is not None:
        data["repository/docs/reasoning_record.since_pdf.diff"] = diff
    data["SOURCE_STATUS.json"] = encoded(status)
    _, link_map = resolve_draft_links(root)
    data["LINK_MAP.json"] = encoded(link_map)
    if job == "long_record_navigation":
        _, closure = round4.linked_sources(root, {"repository/docs/reasoning_record.md": (root / "docs/reasoning_record.md", "")})
        data["READING_LINK_CLOSURE.json"] = encoded(closure)
    request = (render_request(job, options["requests_dir"]).rstrip() + "\n\n" + packet_map(job, data) + "\n"
               + literature_section(job, data) + f"\nUse the finding prefix `{PREFIX[job]}`.\n")
    check_readme_links(request, data)
    check_reader_leaks(data, request)
    if any(digest((root / n).read_bytes()) != digest(data["repository/" + n]) for n in REPOSITORY_FILES):
        raise ValueError("a repository input changed while reading; build again")
    labels = {name: (label, role) for name, (_, role, label) in files.items()}
    rows = [{"member": name, "source": labels.get(name, ("generated from hashed inputs",))[0],
             "role": labels.get(name, (None, "generated_navigation"))[1], "bytes": len(blob), "sha256": digest(blob)}
            for name, blob in sorted(data.items())]
    manifest = {"campaign": CAMPAIGN, "packet": job, "title": JOBS[job],
        "repository_commit": status["repository_commit"],
        "source_paper": "OpenAI preprint PDF SHA-256 " + digest(data["paper/source.pdf"]),
        "request_sha256": digest(request.encode()), "drafts": status["drafts"], "record": status["record"],
        "literature_present": LITERATURE[job], "literature_cited_only": CITED_ONLY_BY_JOB[job],
        "members": rows, "interpretation": "Member hashes bind the exact working bytes; the commit is provenance only."}
    return {"data": data, "request": request, "manifest": manifest}


def prepare_batch(jobs, **options):
    if not jobs or len(jobs) != len(set(jobs)) or not set(jobs) <= set(JOBS):
        raise ValueError("select distinct round-five jobs")
    return {job: prepare(job, **options) for job in jobs}


def batch_digest(packets):
    return previous.batch_digest(packets)


def build_batch(jobs, dest, freeze_digest=None, **options):
    dest, root = Path(dest).resolve(), options["root"].resolve()
    if dest == root or root in dest.parents:
        raise ValueError("output must be outside the repository")
    if dest.exists():
        raise FileExistsError("choose a new output folder; never overwrite an earlier batch")
    packets = prepare_batch(jobs, **options)
    frozen = batch_digest(packets)
    if freeze_digest and frozen != freeze_digest:
        raise ValueError("inputs differ from the freeze digest")
    dest.parent.mkdir(parents=True, exist_ok=True)
    audit = []
    with tempfile.TemporaryDirectory(prefix=".quartic-r5-", dir=dest.parent) as staging:
        for job, packet in packets.items():
            path = Path(staging) / f"quartic_r5_{job}.zip"
            previous.write_archive(path, packet)
            name, count = check_packets.audit(path)
            with zipfile.ZipFile(path) as archive:
                check_readme_links(archive.read("READ_ME_FIRST.md").decode(), {n: b"" for n in archive.namelist()})
            audit.append({"job": job, "archive": path.name, "bytes": path.stat().st_size, "sha256": digest(path.read_bytes()),
                "payload_members": count, "request_sha256": packet["manifest"]["request_sha256"],
                "literature_present": LITERATURE[job], "literature_cited_only": CITED_ONLY_BY_JOB[job],
                "link_problems": json.loads(packet["data"]["LINK_MAP.json"])["problem_count"], "checker": "passed"})
        if batch_digest(prepare_batch(jobs, **options)) != frozen:
            raise ValueError("inputs changed during packaging; build again")
        status = json.loads(next(iter(packets.values()))["data"]["SOURCE_STATUS.json"])
        (Path(staging) / "batch-audit.json").write_bytes(encoded({"schema": "quartic-round5-batch-audit-v1",
            "status": "passed", "freeze_digest": frozen, "jobs": list(jobs), "source_status": status, "archives": audit,
            "built_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}))
        (Path(staging) / "INDEX.md").write_text(index_text(audit, status, frozen), encoding="utf-8")
        dest.mkdir()  # exclusive: an existing batch is never replaced
        for path in Path(staging).iterdir():
            os.link(path, dest / path.name)
    return [dest / row["archive"] for row in audit]


def index_text(audit, status, frozen):
    lines = ["# Quartic round-five critique packets", "",
        "Five independent referee packets on the current expert companion, exposition and long record. Each referee "
        "returns located findings and a short verdict; none rewrites. The drafts are unreviewed working drafts bound by hash.", "",
        f"Repository commit `{status['repository_commit']}`. Freeze digest `{frozen}`.", ""]
    for row in audit:
        lines.append(f"- [{row['job']}]({row['archive']}): {JOBS[row['job']]} ({row['bytes']} bytes; SHA-256 "
                     f"`{row['sha256']}`; {len(row['literature_present'])} literature sources supplied, "
                     f"{len(row['literature_cited_only'])} cited only).")
    lines += ["", "[Batch audit](batch-audit.json). Send each ZIP to a fresh session with no other context.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--requests-dir", type=Path)
    parser.add_argument("--annexes", type=Path, required=True, help="folder holding the literature annexes")
    parser.add_argument("--paper-annex", type=Path, required=True, help="folder holding the preprint source.pdf and extracted.md")
    parser.add_argument("--expert-pdf", type=Path, required=True, help="rendered docs/expert_companion.md")
    parser.add_argument("--exposition-pdf", type=Path, required=True, help="rendered docs/exposition.md")
    parser.add_argument("--record-pdf", type=Path, help="rendered record; default docs/reasoning_record.pdf")
    parser.add_argument("--only", nargs="+", choices=list(JOBS))
    parser.add_argument("--dest", type=Path, help="new output folder outside the repository")
    parser.add_argument("--freeze-digest")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    options = dict(root=root, requests_dir=(args.requests_dir or root / "research/requests/round5").resolve(),
        annexes=args.annexes.resolve(), paper_annex=args.paper_annex.resolve(), expert_pdf=args.expert_pdf.resolve(),
        exposition_pdf=args.exposition_pdf.resolve(),
        record_pdf=(args.record_pdf or root / "docs/reasoning_record.pdf").resolve())
    jobs = args.only or list(JOBS)
    try:
        if args.dest:
            for path in build_batch(jobs, args.dest, args.freeze_digest, **options):
                print(f"PASS {path}")
        else:
            packets = prepare_batch(jobs, **options)
            print(f"Validated {len(packets)} packet inputs; no ZIPs written.")
            print("Freeze digest: " + batch_digest(packets))
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"FAIL: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
