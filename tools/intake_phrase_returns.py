#!/usr/bin/env python3
"""Preserve the three phrase-tie returns and derive the maintained phrase sources.

Each accepted return (schema `phrase-ties/1`) ties Lean declarations to the exact
phrases of one paper that state them, groups the phrases under topics, and gives
each declaration a title, a reading note and a per-row fidelity judgement. The
returned files are copied unchanged under research/returns/phrase_links/ with a
manifest binding their bytes. The maintained copies in docs/reading_phrases/ bind
the same content to the manuscript bytes and the Lean source snapshot, with the
corrections listed in each file's `corrections`.

    python3 tools/intake_phrase_returns.py RETURNS_ACCEPTED_DIR
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_comparator_map import lean_blocks  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "research/returns/phrase_links"
SOURCES = ROOT / "docs/reading_phrases"
PACKETS = {
    "08_quartic_expert": ("expert", "docs/expert_companion.md"),
    "09_quartic_exposition": ("exposition", "docs/exposition.md"),
    "10_quartic_reconstruction": ("reconstruction", "docs/reasoning_record.md"),
}
MEMBERS = ("ties.json", "topics.json", "titles.json", "notes.json", "REVIEW.md", "packet.json")

# Returned titles that wrote mathematics in plain ASCII, keyed by their exact words. Each
# becomes a rich title with inline TeX and its Unicode reading, in the form
# docs/reading_declaration_titles.json uses.
TYPESET_TITLES = {
    'The addressed function needs more than floor mL/100 randomized queries': [
        'The addressed function needs more than $\\lfloor mL/100\\rfloor$ randomized queries',
        'The addressed function needs more than ⌊mL/100⌋ randomized queries'],
    'The classical query budget is at most m²/100': [
        'The classical query budget is at most $m^2/100$',
        'The classical query budget is at most m²/100'],
    'The erased zero is found with probability at most 4G/m²': [
        'The erased zero is found with probability at most $4G/m^2$',
        'The erased zero is found with probability at most 4G/m²'],
    'The erased-zero probability equals E Z/m': [
        'The erased-zero probability equals $\\mathbb{E}Z/m$',
        'The erased-zero probability equals 𝔼Z/m'],
    'The tournament needs O(c sqrt(m) T^2 log(T)) physical queries': [
        'The tournament needs $O(c\\sqrt{m}\\,T^2\\log T)$ physical queries',
        'The tournament needs O(c√m T² log T) physical queries'],
    'Searching for a failed test costs O(ell sqrt(K) log(1/epsilon)) queries': [
        'Searching for a failed test costs $O(\\ell\\sqrt{K}\\log(1/\\varepsilon))$ queries',
        'Searching for a failed test costs O(ℓ√K log(1/ε)) queries'],
    'Expected total weight after T pivots is at most m/2^T': [
        'Expected total weight after $T$ pivots is at most $m/2^T$',
        'Expected total weight after T pivots is at most m/2ᵀ'],
    'The complete query budget is at most C_k sqrt(m) ell^6': [
        'The complete query budget is at most $C_k\\sqrt{m}\\,\\ell^6$',
        'The complete query budget is at most Cₖ√m ℓ⁶'],
    'The erased-zero probability is at most 2G/m²': [
        'The erased-zero probability is at most $2G/m^2$',
        'The erased-zero probability is at most 2G/m²'],
    'A random column is heavy with probability at most G/(mL)': [
        'A random column is heavy with probability at most $G/(mL)$',
        'A random column is heavy with probability at most G/(mL)'],
    'At k=3, the expression 4−2/k equals 10/3': [
        'At $k=3$, the expression $4-2/k$ equals $10/3$',
        'At k = 3, the expression 4 − 2/k equals 10/3'],
    'The factor (2/3)^r is at most m⁻¹⁰': [
        'The factor $(2/3)^r$ is at most $m^{-10}$',
        'The factor (2/3)ʳ is at most m⁻¹⁰'],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def declaration_lines(cache, file):
    if file not in cache:
        text = (ROOT / file).read_text(encoding="utf-8")
        cache[file] = {}
        for block in lean_blocks(text):
            cache[file].setdefault(block["name"], []).append((block["line_start"], block["line_end"]))
    return cache[file]


def maintained(packet, rows, paper, manuscript, snapshot, commit):
    corrections = []
    blocks = {}
    ties = []
    for tie in rows["ties"]["ties"]:
        lean = []
        for link in tie["lean"]:
            file = "lean/" + link["file"]
            found = declaration_lines(blocks, file).get(link["name"], [])
            if len(found) != 1:
                raise ValueError(f"{packet}/{tie['id']}: {link['name']} is not declared once in {file}")
            first, last = found[0]
            row = {**link, "file": file}
            if "lines" in link:
                a, b = link["lines"]
                if b < first or a > last:
                    raise ValueError(f"{packet}/{tie['id']}: {link['name']} lines {a}-{b} lie outside {first}-{last}")
                clamped = [max(a, first), min(b, last)]
                if clamped != [a, b]:
                    row["lines"] = clamped
                    corrections.append({"tie": tie["id"], "declaration": link["name"], "returned_lines": [a, b],
                                        "lines": clamped, "reason": f"The returned range ran past the declaration, "
                                                                     f"lines {first}-{last}; it is cut to the declaration."})
            lean.append(row)
        ties.append({**tie, "lean": lean})
    titles = {}
    for name, title in rows["titles"].items():
        if title in TYPESET_TITLES:
            titles[name] = TYPESET_TITLES[title]
            corrections.append({"declaration": name, "returned_title": title, "title": TYPESET_TITLES[title],
                                "reason": "Mathematics written in plain ASCII is set as inline TeX with a Unicode reading."})
        else:
            titles[name] = title
    return {"schema": "quartic-reading-phrases-v1", "paper": paper, "manuscript": manuscript,
            "manuscript_sha256": digest((ROOT / manuscript).read_bytes()),
            "lean_source_snapshot_sha256": snapshot, "reviewed_lean_revision": commit,
            "return": f"research/returns/phrase_links/members/{packet}",
            "corrections": corrections, "topics": rows["topics"]["topics"], "ties": ties,
            "removed": rows["ties"].get("removed", []), "titles": titles, "notes": rows["notes"]}


def main(source):
    snapshot = json.loads((ROOT / "corpus/reading_dependencies.json").read_text())["source_snapshot_sha256"]
    manifest = {"source": "reader_phrase_links_typeb_20261120/returns_accepted", "members": {}}
    for packet, (paper, manuscript) in PACKETS.items():
        folder = source / packet
        config = json.loads((folder / "packet.json").read_text())
        if config["paper_key"] != paper or Path(config["paper"]).name != Path(manuscript).name:
            raise ValueError(f"{packet}: packet names another paper")
        rows = {name[:-5]: json.loads((folder / name).read_text()) for name in MEMBERS if name.endswith(".json")}
        if rows["ties"]["schema"] != "phrase-ties/1" or rows["ties"]["paper"] != paper:
            raise ValueError(f"{packet}: unexpected ties schema or paper")
        target = DEST / "members" / packet
        target.mkdir(parents=True, exist_ok=True)
        for name in MEMBERS:
            data = (folder / name).read_bytes()
            (target / name).write_bytes(data)
            manifest["members"][f"members/{packet}/{name}"] = {"size": len(data), "sha256": digest(data)}
        manifest.setdefault("source_commit", config["source_commit"])
        record = maintained(packet, rows, paper, manuscript, snapshot, config["source_commit"])
        SOURCES.mkdir(exist_ok=True)
        (SOURCES / f"{paper}.json").write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n")
        print(f"{paper}: {len(record['ties'])} ties, {len(record['titles'])} declarations, "
              f"{len(record['corrections'])} corrections")
    fixes = (source / "FIXES.md").read_bytes()
    (DEST / "FIXES.md").write_bytes(fixes)
    manifest["members"]["FIXES.md"] = {"size": len(fixes), "sha256": digest(fixes)}
    (DEST / "intake.json").write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("returns", type=Path, help="the returns_accepted folder")
    main(parser.parse_args().returns)
