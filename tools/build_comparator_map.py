#!/usr/bin/env python3
"""Generate the Comparator reading map: each Challenge block beside its record passage.

Comparator trusts a Challenge file: the configured theorem statements and every
definition they depend on. This map splits every Challenge used by a Comparator
configuration into its declaration blocks and joins each block to:

  - the corpus statement IDs tied to it (corpus/statements.json), either directly
    or through the wrapper's proof text in the matching Solution;
  - the reasoning-record passages that state or mention it, with each passage
    hash checked against docs/reasoning_record.md;
  - the latest Comparator receipt for each configuration that uses the Challenge,
    with direct credit for configured targets only.

Plain-language glosses are quoted from existing record passages (anchor, passage
hash and excerpt hash), never authored here. A block with no record passage is
listed as an explicit gap. Dependency closure uses the recorded native export
where it has the declaration, and theorem-statement identifiers read from text
otherwise; the map states which basis applies. This is a reading aid. It does
not establish that any definition expresses the intended mathematics.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import build_corpus


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
CORPUS_LEAN = LEAN / "QuarticCorpus"
STATEMENT = LEAN / "QuarticQuery/Statement.lean"
RECORD = ROOT / "docs/reasoning_record.md"
CORRESPONDENCE = ROOT / "docs/reasoning_record_correspondence.json"
STATEMENTS = ROOT / "corpus/statements.json"
DEPENDENCIES = ROOT / "corpus/lean_dependencies.json"
OUTPUT = ROOT / "corpus/comparator_map.json"
SCHEMA = "quartic-comparator-reading-map-v1"

DECLARATION = re.compile(
    r"^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected)\s+)*"
    r"(theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+([^\s:({\[]+)")
SCOPE = re.compile(r"^(namespace|section|end)(?:[ \t]+(\S+))?[ \t]*$", re.M)
OPEN = re.compile(r"^open\s+(?:scoped\s+)?([^\n]+?)(?:\s+in)?\s*$", re.M)
IMPORT = re.compile(r"^(?:public\s+)?import\s+(\S+)", re.M)
IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*[A-Za-z0-9_']|[A-Za-z_]")
PASSAGE = re.compile(r"<!-- passage:([^ >]+) -->(.*?)<!-- /passage:\1 -->", re.S)
CLAIM = re.compile(r"<!-- claim:([^ >]+) -->")
BACKTICK = re.compile(r"`([^`\n]+)`")
EXACT = re.compile(r"^\s*exact\s+(@?[A-Za-z_][\w.']*)", re.M)


def sha256(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode("utf-8")).hexdigest()


def rel(path):
    return Path(path).resolve().relative_to(ROOT).as_posix()


def module_path(module):
    return LEAN / (module.replace(".", "/") + ".lean")


# ---------------------------------------------------------------- Lean blocks

def lean_blocks(text):
    """Split Lean source into top-level declaration blocks with namespaced names.

    A block starts at its doc comment, attributes or `open ... in` prefix and ends
    before the next column-0 line that is not a pattern-match arm.
    """
    lines = text.split("\n")
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line) + 1)
    events = [(m.start(), m.group(1), m.group(2)) for m in SCOPE.finditer(text)]
    blocks = []
    for index, line in enumerate(lines):
        found = DECLARATION.match(line)
        if not found:
            continue
        start = index
        while start > 0:
            previous = lines[start - 1]
            if previous.startswith("open ") and previous.rstrip().endswith(" in"):
                start -= 1
            elif previous.startswith("@["):
                start -= 1
            elif previous.rstrip().endswith("-/") and not previous.startswith("/-!"):
                at = start - 1
                while at >= 0 and not lines[at].startswith("/--"):
                    at -= 1
                if at < 0:
                    break
                start = at
            else:
                break
        end = index + 1
        while end < len(lines):
            following = lines[end]
            if following and not following[0].isspace() and not following.startswith("|"):
                break
            end += 1
        while end > index + 1 and not lines[end - 1].strip():
            end -= 1
        body = "\n".join(lines[start:end])
        doc = re.search(r"/--(.*?)-/", body, re.S)
        scopes = build_corpus.open_scopes(events, offsets[index])
        blocks.append({
            "name": ".".join(scopes + [found.group(2)]),
            "kind": found.group(1),
            "line_start": start + 1,
            "line_end": end,
            "sha256": sha256(body),
            "text": body,
            "doc_comment": " ".join(doc.group(1).split()) if doc else None,
            "namespace": ".".join(scopes),
        })
    return blocks


def statement_text(block):
    """The theorem's type: everything before its proof."""
    text = block["text"]
    cut = text.find(":= by")
    return text if cut < 0 else text[:cut]


def opened_namespaces(text):
    names = []
    for found in OPEN.finditer(text):
        names.extend(part for part in found.group(1).split() if part[0].isupper())
    return names


def resolver(known, namespace, opened):
    """Resolve an identifier as Lean would try its enclosing and opened namespaces."""
    parts = namespace.split(".") if namespace else []
    prefixes = [".".join(parts[:n]) for n in range(len(parts), 0, -1)] + opened + [""]

    def resolve(token):
        token = token.lstrip("@").rstrip(".")
        for prefix in prefixes:
            name = f"{prefix}.{token}" if prefix else token
            if name in known:
                return name
        return None
    return resolve


def without_comments(text):
    text = re.sub(r"/-.*?-/", " ", text, flags=re.S)
    return re.sub(r"--[^\n]*", " ", text)


def identifiers(text, resolve):
    text = without_comments(text)
    found = set()
    for token in IDENTIFIER.findall(text):
        name = resolve(token)
        if name:
            found.add(name)
    return found


def generated_member(name, local):
    """Constructors, fields and recursors belong to their displayed declaration."""
    parts = name.split(".")
    return any(".".join(parts[:n]) in local for n in range(1, len(parts)))


def closure(roots, edges, local_edges):
    """Transitive dependencies: native edges where recorded, textual edges otherwise."""
    seen, stack, basis = set(), list(roots), {}
    while stack:
        name = stack.pop()
        if name in seen:
            continue
        seen.add(name)
        if name in edges:
            basis[name] = "native_dependency_export"
            stack.extend(edges[name])
        elif name in local_edges:
            basis[name] = "textual_identifiers"
            stack.extend(local_edges[name])
    return seen, basis


# ------------------------------------------------------------- record passages

def record_passages(record_text, correspondence):
    """Return verified passages keyed by anchor, with claim segments and line numbers."""
    expected = {p["id"]: p for p in correspondence["passages"]}
    passages, mismatched = {}, []
    for found in PASSAGE.finditer(record_text):
        anchor, body = found.group(1), found.group(2)
        start_line = record_text.count("\n", 0, found.start(2)) + 1
        digest = sha256(body)
        if anchor not in expected or expected[anchor]["sha256"] != digest:
            mismatched.append(anchor)
            continue
        claims = {}
        markers = list(CLAIM.finditer(body))
        for n, marker in enumerate(markers):
            stop = markers[n + 1].start() if n + 1 < len(markers) else len(body)
            claims.setdefault(marker.group(1), (marker.end(), stop))
        passages[anchor] = {"body": body, "body_offset": found.start(2), "line_start": start_line,
                            "line_end": record_text.count("\n", 0, found.end(2)) + 1,
                            "sha256": digest, "claims": expected[anchor]["claims"],
                            "claim_segments": claims}
    return passages, mismatched


def excerpt(record_text, passage, start, stop):
    """An exact, stripped substring of a verified passage, with its record lines."""
    body = passage["body"]
    while start < stop and body[start].isspace():
        start += 1
    while stop > start and body[stop - 1].isspace():
        stop -= 1
    text = body[start:stop]
    first = passage["body_offset"] + start
    return {"line_start": record_text.count("\n", 0, first) + 1,
            "line_end": record_text.count("\n", 0, first + len(text)) + 1,
            "excerpt_sha256": sha256(text), "excerpt": text}


def paragraph_around(body, position):
    start = body.rfind("\n\n", 0, position)
    stop = body.find("\n\n", position)
    return (0 if start < 0 else start + 2), (len(body) if stop < 0 else stop)


def aliases(name):
    """Names by which the record may cite a declaration in backticks."""
    found = {name}
    if name.startswith("QuarticQuery.Checked."):
        found.add("Checked." + name.rsplit(".", 1)[1])
    elif name.startswith("QuarticQuery."):
        found.add(name[len("QuarticQuery."):])
    return found


def backtick_mentions(passages, names):
    index = {}
    for name in names:
        for alias in aliases(name):
            index.setdefault(alias, set()).add(name)
    mentions = {}
    for anchor, passage in passages.items():
        for found in BACKTICK.finditer(passage["body"]):
            first = found.group(1).split()[0].rstrip(",.;:")
            for name in index.get(first, ()):
                mentions.setdefault(name, {}).setdefault(anchor, (first, found.start(), len(index[first]) > 1))
    return mentions


def returned_lean_lists(correspondence):
    """Passages whose returned correspondence explicitly lists a Lean name."""
    named = {}
    for source in correspondence.get("returned_correspondence", []):
        for record in source.get("records", []):
            for name in record.get("lean", []):
                named.setdefault(name, set()).add((record["passage"], source["path"]))
    return named


# ------------------------------------------------------------------- receipts

def receipt_summary(run, hashes):
    return {"receipt": run["receipt_file"], "receipt_sha256": run["receipt_sha256"],
            "ran_at": run.get("ran_at"), "status": run["status"],
            "currentness": build_corpus.currentness(run, hashes),
            "declaration_scope": run.get("declaration_scope", "historical_configured_plus_scanned"),
            **({"negative_control": run["negative_control"]} if run.get("negative_control") else {})}


def configurations(runs, hashes):
    configs = []
    for path in sorted(CORPUS_LEAN.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if "challenge_module" not in data:
            continue
        key = rel(path)
        matching = sorted((run for run in runs if run["kind"] == "comparator"
                           and build_corpus.comparator_config(run) == key),
                          key=lambda run: run.get("ran_at") or "")
        positive = [run for run in matching if run["status"] == "passed" and not run.get("negative_control")]
        controls = [run for run in matching if run.get("negative_control")]
        configs.append({
            "path": key,
            "challenge": rel(module_path(data["challenge_module"])),
            "solution": rel(module_path(data["solution_module"])),
            "theorem_names": data["theorem_names"],
            "role": "negative_control" if controls and not positive else "positive",
            "receipts_recorded": len(matching),
            "latest_receipt": receipt_summary((positive or controls or [None])[-1], hashes)
            if (positive or controls) else None,
            "current_positive_receipts": sum(build_corpus.currentness(run, hashes) == "current"
                                             for run in positive),
        })
    return configs


# ----------------------------------------------------------------------- build

def build():
    hashes = build_corpus.source_hashes()
    runs = build_corpus.receipts()
    record_bytes = RECORD.read_bytes()
    record_text = record_bytes.decode("utf-8")
    correspondence = json.loads(CORRESPONDENCE.read_text(encoding="utf-8"))
    passages, mismatched = record_passages(record_text, correspondence)
    dependencies = json.loads(DEPENDENCIES.read_text(encoding="utf-8"))
    edges = dependencies["edges"]
    known = set(dependencies["declared"]) | set(edges)
    statements = json.loads(STATEMENTS.read_text(encoding="utf-8"))
    ties = {}
    for record in statements:
        for tie in record["lean"]:
            ties.setdefault(tie["declaration"], []).append({
                "statement_id": record["id"], "relation": tie["relation"],
                "review_evidence": tie["review_evidence"],
                "comparison_credit": tie.get("comparison_credit", "none")})
    claim_passages = {}
    for anchor, passage in passages.items():
        for ident in passage["claims"]:
            claim_passages.setdefault(ident, []).append(anchor)
    configs = configurations(runs, hashes)
    statement_source = {block["name"]: block for block in lean_blocks(STATEMENT.read_text(encoding="utf-8"))}

    challenges, declarations = [], {}
    inputs = {rel(p): sha256(p.read_bytes()) for p in (STATEMENT, RECORD, CORRESPONDENCE, STATEMENTS, DEPENDENCIES)}
    for path in sorted({config["challenge"] for config in configs}):
        file = ROOT / path
        text = file.read_text(encoding="utf-8")
        inputs[path] = sha256(file.read_bytes())
        users = [c for c in configs if c["challenge"] == path]
        blocks = lean_blocks(text)
        local = {block["name"] for block in blocks}
        resolve = resolver(known | local, "", opened_namespaces(text))
        local_edges = {}
        for block in blocks:
            find = resolver(known | local, block["namespace"], opened_namespaces(text))
            local_edges[block["name"]] = identifiers(
                statement_text(block) if block["kind"] in {"theorem", "lemma"} else block["text"], find) - {block["name"]}
        imports = IMPORT.findall(text)
        pinned = {}
        imported_surface = set()
        for config in users:
            if config["role"] != "positive":
                continue
            for target in config["theorem_names"]:
                reached, basis = closure(local_edges.get(target, set()), edges, local_edges)
                for name in reached & local:
                    pinned.setdefault(name, {})[target] = basis.get(name, "textual_identifiers")
                imported_surface |= {n for n in reached - local
                                     if n.startswith(("QuarticQuery.", "Round3."))
                                     and not generated_member(n, local)}
        solutions = {}
        for config in users:
            source = ROOT / config["solution"]
            inputs[config["solution"]] = sha256(source.read_bytes())
            inputs[config["path"]] = sha256((ROOT / config["path"]).read_bytes())
            for block in lean_blocks(source.read_text(encoding="utf-8")):
                proof = block["text"].split("-- proof", 1)[-1] if "-- proof" in block["text"] else block["text"]
                solutions.setdefault(block["name"], set()).update(EXACT.findall(proof))
        entries = []
        for block in blocks:
            name = block["name"]
            targeted = [c for c in users if name in c["theorem_names"]]
            positive = [c for c in targeted if c["role"] == "positive"]
            if positive:
                latest = positive[-1]["latest_receipt"]
                comparison = {"credit": "direct", "basis": "configured_theorem_name",
                              "configurations": [c["path"] for c in targeted], "latest_receipt": latest}
            elif name in pinned:
                config = next(c for c in users if c["role"] == "positive"
                              and set(c["theorem_names"]) & set(pinned[name]))
                comparison = {"credit": "statement_dependency",
                              "basis": sorted(set(pinned[name].values())),
                              "configured_targets_depending_on_it": sorted(pinned[name]),
                              "latest_receipt": config["latest_receipt"]}
            else:
                comparison = {"credit": "not_in_any_configured_statement",
                              "basis": "no configured theorem of this Challenge depends on it"}
            entry = {key: block[key] for key in ("name", "kind", "line_start", "line_end", "sha256")}
            entry["comparison"] = comparison
            if targeted and not positive:
                entry["negative_control_configurations"] = [c["path"] for c in targeted]
            entries.append(entry)
            if name not in declarations:
                source = statement_source.get(name)
                declarations[name] = {
                    "kind": block["kind"],
                    "doc_comment": block["doc_comment"],
                    "defined_in": ({"path": rel(STATEMENT), "line_start": source["line_start"],
                                    "line_end": source["line_end"], "sha256": source["sha256"]}
                                   if source and source["sha256"] == block["sha256"] else
                                   {"path": path, "line_start": block["line_start"],
                                    "line_end": block["line_end"], "sha256": block["sha256"]}),
                    "solution_proof_references": sorted(solutions.get(name, set())),
                }
            elif declarations[name]["kind"] != block["kind"]:
                raise ValueError(f"{name}: conflicting declaration kinds across challenges")
        challenges.append({
            "path": path, "sha256": inputs[path],
            "generated_by_build_challenges": text.startswith("module\n\n-- Generated by tools/build_challenges.py"),
            "imports": imports,
            "imports_project_modules": any(not module.startswith("Mathlib") for module in imports),
            # The dependency export covers the public QuarticQuery projection only;
            # declarations from these imported modules are not traced above.
            "imports_outside_dependency_export": [m for m in imports if m.startswith("QuarticCorpus.")],
            "configurations": [{k: c[k] for k in ("path", "solution", "role", "theorem_names", "latest_receipt",
                                                   "current_positive_receipts", "receipts_recorded")}
                               for c in users],
            "imported_trust_surface": {
                "declarations_outside_this_file": len(imported_surface),
                "sample": sorted(imported_surface)[:25],
                "note": ("The configured statements depend on these project declarations, which this "
                         "file imports rather than displays. They are part of what Comparator trusts.")
                if imported_surface else "None found: every recorded dependency is displayed in this file."},
            "blocks": entries,
        })

    mentions = backtick_mentions(passages, declarations)
    returned = returned_lean_lists(correspondence)
    for name, info in declarations.items():
        links = [{**tie, "join": "statement_tie"} for tie in ties.get(name, [])]
        for reference in info["solution_proof_references"]:
            for tie in ties.get(reference, []):
                links.append({**tie, "join": "solution_proof_reference", "via": reference,
                              "note": "Wrapper proof text names this declaration; no type correspondence is recorded."})
        info["statement_ids"] = links
        references = []
        for link in links:
            for anchor in claim_passages.get(link["statement_id"], []):
                references.append({"anchor": anchor, "join": "statement_claim",
                                   "statement_id": link["statement_id"], "via": link["join"]})
        for anchor, (alias, _, ambiguous) in sorted(mentions.get(name, {}).items(),
                                                    key=lambda item: passages[item[0]]["line_start"]):
            references.append({"anchor": anchor, "join": "backtick_mention", "alias": alias,
                               **({"ambiguous_alias": True} if ambiguous else {}),
                               "passage_claims": passages[anchor]["claims"]})
        for anchor, source in sorted(returned.get(name, ())):
            if anchor in passages:
                references.append({"anchor": anchor, "join": "returned_correspondence_lean_list",
                                   "source": source})
        unique, seen = [], set()
        for reference in references:
            key = (reference["anchor"], reference["join"], reference.get("statement_id"))
            if key not in seen:
                seen.add(key)
                passage = passages[reference["anchor"]]
                unique.append({**reference, "passage_sha256": passage["sha256"],
                               "passage_lines": [passage["line_start"], passage["line_end"]]})
        info["record_references"] = unique
        info["primary_gloss"] = primary_gloss(record_text, passages, unique, mentions.get(name, {}))
        info["gap"] = None if unique else "no_record_passage"

    coverage = summarize(challenges, declarations)
    return {
        "schema": SCHEMA,
        "generated_by": "tools/build_comparator_map.py",
        "boundary": ("Reading aid joining Comparator's trusted Challenge text to existing record passages, "
                     "corpus statement ties and recorded receipts. Glosses are exact record excerpts. Joins by "
                     "backtick mention or wrapper proof text are textual and labelled. No Lean or Comparator "
                     "run, semantic review or new prose is produced here."),
        "credit_vocabulary": {
            "direct": "A configured theorem name of a positive Comparator configuration.",
            "statement_dependency": "A displayed definition that a configured theorem's statement depends on.",
            "not_in_any_configured_statement": "Displayed in the Challenge but not used by a configured statement.",
            "wrapper_mediated_historical": ("On statement links: the corpus tie is to the implementation that "
                                            "the wrapper's proof names, which only older receipts listed."),
        },
        "inputs": dict(sorted(inputs.items())),
        "record": {"path": rel(RECORD), "sha256": sha256(record_bytes),
                   "passages_verified": len(passages), "passages_in_correspondence": len(correspondence["passages"]),
                   "passage_hash_mismatches": sorted(mismatched)},
        "dependency_export": {"path": rel(DEPENDENCIES),
                              "currentness": build_corpus.currentness(dependencies, hashes)},
        "coverage": coverage,
        "challenges": challenges,
        "declarations": dict(sorted(declarations.items())),
    }


def primary_gloss(record_text, passages, references, mentions):
    """Choose the quoted record text a reader sees first; never compose new text."""
    order = [("statement_claim", "statement_tie"), ("statement_claim", "solution_proof_reference"),
             ("backtick_mention", None), ("returned_correspondence_lean_list", None)]
    for join, via in order:
        for reference in references:
            if reference["join"] != join or (via and reference.get("via") != via):
                continue
            passage = passages[reference["anchor"]]
            if join == "statement_claim" and reference["statement_id"] in passage["claim_segments"]:
                start, stop = passage["claim_segments"][reference["statement_id"]]
            elif join == "backtick_mention":
                start, stop = paragraph_around(passage["body"], mentions[reference["anchor"]][1])
            else:
                continue
            return {"anchor": reference["anchor"], "join": join,
                    **({"statement_id": reference["statement_id"]} if "statement_id" in reference else {}),
                    "passage_sha256": passage["sha256"],
                    **excerpt(record_text, passage, start, stop)}
    return None


def summarize(challenges, declarations):
    blocks = [(c["path"], b) for c in challenges for b in c["blocks"]]
    credit = Counter(b["comparison"]["credit"] for _, b in blocks)
    with_passage = [b for _, b in blocks if declarations[b["name"]]["record_references"]]
    with_ids = [b for _, b in blocks if declarations[b["name"]]["statement_ids"]]
    gaps = sorted({b["name"] for _, b in blocks if declarations[b["name"]]["gap"]})
    return {
        "challenge_files": len(challenges),
        "challenge_blocks": len(blocks),
        "distinct_declarations": len(declarations),
        "blocks_with_record_passage": len(with_passage),
        "blocks_with_statement_id": len(with_ids),
        "blocks_with_direct_statement_tie": sum(
            any(link["join"] == "statement_tie" for link in declarations[b["name"]]["statement_ids"])
            for _, b in blocks),
        "blocks_by_comparison_credit": dict(sorted(credit.items())),
        "distinct_declarations_with_record_passage": sum(bool(d["record_references"]) for d in declarations.values()),
        "distinct_declarations_with_statement_id": sum(bool(d["statement_ids"]) for d in declarations.values()),
        "distinct_declarations_with_primary_gloss": sum(d["primary_gloss"] is not None for d in declarations.values()),
        "gaps_no_record_passage": gaps,
    }


def render(value):
    return json.dumps(value, indent=1, ensure_ascii=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if corpus/comparator_map.json is stale")
    args = parser.parse_args()
    value = build()
    text = render(value)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            print("stale, run tools/build_comparator_map.py: comparator_map.json", file=sys.stderr)
            return 1
    else:
        OUTPUT.write_text(text, encoding="utf-8")
    print(render(value["coverage"]).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
