"""Join manuscript selections to Quartic's evidence and compiled proof graph."""
from collections import defaultdict
import hashlib
import re
import subprocess

from build_comparator_map import CLAIM, PASSAGE, lean_blocks
from build_corpus import canonical_sha256, source_hashes
from reading_applications import application_resources
from reading_board import board_example


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def graph_resources(edition):
    graph = edition.json("corpus/reading_dependencies.json")
    inspector = edition.read("tools/ReadDependencies.lean")
    current = (canonical_sha256(source_hashes(edition.root)) == graph["source_snapshot_sha256"]
               and sha(inspector) == graph["inspector_sha256"])
    info = {k: v for k, v in graph.items() if k not in {"nodes", "external_modules"}}
    info["currentness"] = "current" if current else "stale"
    nodes = graph["nodes"] if current else {}
    modules = defaultdict(dict)
    names = {}
    users = defaultdict(lambda: defaultdict(list))
    for name, node in nodes.items():
        modules[node["module"]][name] = node
        names[name] = node["module"]
        for kind in ("type", "value", "structural"):
            for dep in node[kind]:
                if dep in nodes:
                    users[dep][kind].append(name)
    for module, rows in modules.items():
        path = "lean/" + module.replace(".", "/") + ".lean"
        raw = edition.read(path)
        edition.resources[path] = raw
        blocks = {b["name"]: [b["line_start"], b["line_end"]] for b in lean_blocks(raw.decode())}
        edition.add(f"proof/{module}.json", {"source": path, "nodes": {
            n: {**r, "incoming": users[n], "lines": blocks.get(n)} for n, r in rows.items()}})
    dependencies = {p["name"]: {"url": p["url"], "revision": p["rev"]} for p in
                    edition.json("lean/lake-manifest.json")["packages"]}
    edition.add("selection/external.json", {"modules": graph.get("external_modules", {}) if current else {},
                                           "packages": dependencies})
    return info, names, graph["nodes"]


class BoundLocations:
    """Reorder freely; changing text under an editorial association requires rebinding it."""
    def __init__(self, edition, config, documents, texts, passages, locate_quote):
        self.edition, self.default = edition, config["bindings_revision"]
        self.documents, self.texts, self.passages = documents, texts, passages
        self.locate_quote = locate_quote
        self.history = {}

    def check(self, row, paper, *, quote=None, passage=None):
        revision = row.get("bound_at", {}).get(paper, self.default)
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError(f"{row['id']}: expected a full binding revision for {paper}")
        key = (revision, paper)
        if key not in self.history:
            text = subprocess.check_output(["git", "cat-file", "blob", f"{revision}:{self.documents[paper]}"],
                                           cwd=self.edition.root).decode()
            self.history[key] = (text, {m[1]: sha(m[2].encode()) for m in PASSAGE.finditer(text)})
        original, anchors = self.history[key]
        context = f"{row['id']}/{paper}"
        if passage is not None:
            loc = self.passages[passage]
            old = anchors.get(passage)
        else:
            loc = self.locate_quote(self.texts[paper], quote, context)
            old = self.locate_quote(original, quote, context)["sha256"]
        if old != loc["sha256"]:
            raise ValueError(f"{context}: selected text changed since {revision[:12]}; review its association "
                             f"and set bound_at.{paper} to the reviewed manuscript revision")
        return {**loc, "bound_at": revision}

    def context(self, topic, passage, revision):
        if passage not in self.passages:
            raise ValueError(f"{topic}: missing prerequisite passage {passage}")
        paper = self.passages[passage]["document"]
        row = {"id": topic, "bound_at": {paper: revision}}
        try:
            loc = self.check(row, paper, passage=passage)
        except ValueError as error:
            raise ValueError(f"{topic}: review prerequisite {paper}/{passage} and rebind its "
                             f"context_passages revision") from error
        return {"passage": passage, "paper": paper, "sha256": loc["sha256"], "bound_at": revision}


def audit_bindings(edition, manuscript_root, documents, config, locate_quote):
    """Check all authored associations against a draft before regenerating the corpus."""
    texts = {k: (manuscript_root / p).read_text() for k, p in documents.items()}
    passages = {}
    for paper in ("reconstruction", "verification"):
        for m in PASSAGE.finditer(texts[paper]):
            if m[1] in passages:
                raise ValueError(f"duplicate draft passage: {m[1]}")
            passages[m[1]] = {"document": paper, "sha256": sha(m[2].encode())}
    binding = BoundLocations(edition, config, documents, texts, passages, locate_quote)
    issues = []
    checked = 0
    contexts = 0
    affected = {}
    for row in config["routes"] + config["selections"] + config["board_scenes"]:
        start = len(issues)
        for passage, revision in row.get("context_passages", {}).items():
            contexts += 1
            try:
                binding.context(row["id"], passage, revision)
            except ValueError as error:
                issues.append({"id": row["id"], "kind": "prerequisite_changed", "passage": passage,
                               "bound_at": revision, "draft_sha256": passages.get(passage, {}).get("sha256"),
                               "reason": str(error)})
        anchor = row.get("reconstruction") or row.get("passage")
        selectors = [(k, {"quote": q}) for k, quotes in row.get("quotes", {}).items() for q in quotes]
        selectors.extend((k, {"quote": row[k]}) for k in ("expert", "exposition") if k in row)
        if anchor in passages:
            selectors.append((passages[anchor]["document"], {"passage": anchor}))
        elif anchor is not None:
            issues.append({"id": row["id"], "kind": "locator_unresolved", "missing_passage": anchor})
        for paper, selector in selectors:
            checked += 1
            try:
                binding.check(row, paper, **selector)
            except ValueError as error:
                locatable = "passage" in selector or texts[paper].count(selector["quote"]) == 1
                kind = "selected_text_changed" if locatable else "locator_unresolved"
                issues.append({"id": row["id"], "paper": paper, "kind": kind, **selector, "reason": str(error)})
        kinds = {issue["kind"] for issue in issues[start:]}
        if kinds:
            affected[row["id"]] = {"selections_locatable": "locator_unresolved" not in kinds,
                                   "selection_text_as_bound": not (kinds - {"prerequisite_changed"}),
                                   "prerequisites_as_bound": "prerequisite_changed" not in kinds}
    return {"bindings_examined": checked, "prerequisites_examined": contexts, "needs_review": issues,
            "affected_topics": affected}


def selection_resources(edition, config, papers, texts, passages, compiled, statements, links, comparison,
                        locate_quote, original, original_rows):
    documents = {k: v["path"] for k, v in papers.items()}
    binding = BoundLocations(edition, config, documents, texts, passages, locate_quote)
    graph, names, recorded_names = graph_resources(edition)
    registry = edition.json("docs/lean_links.json")
    # A frozen declaration can have identical words under changed definitions.
    same_snapshot = subprocess.run(["git", "diff", "--quiet", registry["commit"], "--", "lean"],
                                   cwd=edition.root).returncode == 0
    current_sources = {}
    selections = {k: [] for k in papers}
    treatments = defaultdict(list)
    topics = {}
    by_name = defaultdict(list)

    def add(paper, ident, loc, **fields):
        item = {"id": ident, "paper": paper, "lines": loc["lines"], **fields}
        for key in ("sha256", "bound_at", "quote"):
            if key in loc:
                item[key] = loc[key]
        selections[paper].append(item)
        if "topic" in fields:
            treatments[fields["topic"]].append(item)
        return item

    def targets(labels):
        roots = []
        for label in labels:
            target = links[label]
            path = target["path"]
            for name in target.get("declarations", []):
                file = "lean/" + names.get(name, "").replace(".", "/") + ".lean"
                # Same spelling in a frozen Challenge and the implementation is insufficient.
                if path not in current_sources:
                    key = f"pinned/{registry['commit']}/{path}"
                    current_sources[path] = edition.resources.get(key) == edition.read(path)
                joins = []
                if same_snapshot and path == file and current_sources[path]:
                    joins.append({"name": name, "basis": "same_implementation_bytes"})
                elif same_snapshot and current_sources[path] and path.endswith("/Challenge.lean"):
                    row = comparison["declarations"].get(name, {})
                    for challenge in comparison["challenges"]:
                        if challenge["path"] == path:
                            # Only use solution references witnessed in the paired Solution source.
                            for cfg in challenge["configurations"]:
                                if cfg["role"] != "positive" or name not in cfg["theorem_names"]:
                                    continue
                                solution = edition.read(cfg["solution"]).decode()
                                block = next((b for b in lean_blocks(solution) if b["name"] == name), None)
                                for impl in row.get("solution_proof_references", []):
                                    if block and impl in names and impl in block["text"]:
                                        joins.append({"name": impl, "basis": "solution_proof_reference",
                                                      "source": cfg["solution"]})
                roots.append({"label": label, "name": name, "url": target["url"], "graph_joins": joins})
        return roots

    formal_targets = {label: targets([label]) for label in links}
    plans = {r["id"]: r for r in config["routes"]}
    for row in [*compiled, *config["selections"]]:
        ident = row["id"]
        if ident in topics:
            raise ValueError(f"duplicate selection ID {ident}")
        plan = plans.get(ident, row)
        anchor = row.get("reconstruction") or row["passage"]
        p = passages[anchor]
        ids = plan.get("statements", [])
        if set(ids) - statements.keys() or set(plan.get("lean", [])) - links.keys():
            raise ValueError(f"{ident}: unknown statement or registry label")
        # Constituent references require a real declaration in the recorded inspection.
        for name in plan.get("declarations", []):
            if name not in recorded_names:
                raise ValueError(f"{ident}: unknown constituent {name}")
        topics[ident] = {"id": ident, "title": row["title"], "kind": row.get("kind", "reading_route"),
                         "note": plan.get("note"), "statements": ids, "labels": plan.get("lean", []),
                         "constituents": plan.get("declarations", []), "passage": anchor}
        if "correspondence_scope" in plan:
            topics[ident]["correspondence_scope"] = plan["correspondence_scope"]
        topics[ident]["context_passages"] = [
            binding.context(ident, passage, revision)
            for passage, revision in plan.get("context_passages", {}).items()]
        if plan.get("figure"):
            if plan["figure"] not in edition.resources:
                raise ValueError(f"{ident}: missing figure")
            topics[ident]["figure"] = plan["figure"]
        paper = p["document"]
        loc = binding.check(plan, paper, passage=anchor)
        add(paper, f"{paper}/{ident}", loc, topic=ident, treatment=topics[ident]["kind"])
        quotes = plan.get("quotes", {})
        if ident in plans:
            quotes = {k: [plan[k]] for k in ("expert", "exposition")}
        for paper, selectors in quotes.items():
            for i, quote in enumerate(selectors):
                loc = binding.check(plan, paper, quote=quote)
                treatment = {"expert": "specialist_discussion", "exposition": "general_exposition"}[paper]
                if plan.get("kind") == "illustrates" and paper == "exposition":
                    treatment = "illustration"
                add(paper, f"{paper}/{ident}/{i}", loc, topic=ident, treatment=treatment)

    for ident, passage in passages.items():
        add(passage["document"], "passage/" + ident, passage, passage=ident,
            statements=passage["statement_ids"])
    for paper in ("reconstruction", "verification"):
        text = texts[paper]
        for body in PASSAGE.finditer(text):
            markers = list(CLAIM.finditer(body[2]))
            for i, marker in enumerate(markers):
                claim = marker[1]
                if claim not in statements:
                    continue
                start = body.start(2) + marker.start()
                stop = body.start(2) + (markers[i+1].start() if i+1 < len(markers) else len(body[2]))
                content = text[start:stop].rstrip()
                first = text.count("\n", 0, start) + 1
                loc = {"lines": [first, first + content.count("\n")], "sha256": sha(content.encode())}
                add(paper, f"claim/{body[1]}/{claim}/{i}", loc, claim=claim, passage=body[1], statements=[claim])
    for paper, doc in papers.items():
        for cite in doc["citations"]:
            line, label = cite["line"], cite["target"]
            add(paper, f"cite/{paper}/{line}/{label}", {"lines": [line, line]}, label=label)
        for ref in doc["record_links"]:
            if anchor := ref.get("edition_passage"):
                line = ref["line"]
                add(paper, f"reference/{paper}/{line}/{anchor}", {"lines": [line, line]},
                    referenced_passage=anchor, statements=passages[anchor]["statement_ids"])

    relations = config["argument_links"]
    for rel in relations:
        if rel["source"] not in topics or rel["target"] not in topics:
            raise ValueError(f"unknown endpoint in editorial link: {rel}")

    # Invert the same bindings used for forward resolution; retain the reason for each match.
    def index(name, paper, ident, basis, **evidence):
        ref = {"paper": paper, "selection": ident, "basis": basis, **evidence}
        if ref not in by_name[name]:
            by_name[name].append(ref)

    scenes = {}
    for scene in config["board_scenes"]:
        rows = []
        for i, quote in enumerate(scene["quotes"]["exposition"]):
            loc = binding.check(scene, "exposition", quote=quote)
            rows.append(add("exposition", f"exposition/{scene['id']}/{i}", loc, treatment="worked_example"))
        scenes[scene["id"]] = {"id": scene["id"], "question": scene["question"], "selections": rows}
    if config["entrances"]["exposition"]["first_selection"] != scenes["known-pair"]["selections"][0]["id"]:
        raise ValueError("exposition must open on the query example")
    edition.add("selection/board.json", board_example(texts["exposition"], scenes))
    selections["original"] = original_rows
    document_index = {p: {"path": path, "format": "markdown", "sha256": sha(edition.read(path)),
                          "lines": len(texts[p].splitlines())} for p, path in documents.items()}
    document_index["original"] = original
    coverage = {}
    by_statement = defaultdict(list)
    for paper, rows in selections.items():
        covered = set()
        topic_ids = set()
        for row in rows:
            if topic_id := row.get("topic"):
                topic_ids.add(topic_id)
            topic = topics.get(row.get("topic"), {})
            ids = set(row.get("statements", [])) | set(topic.get("statements", []))
            covered.update(ids)
            for sid in sorted(ids):
                by_statement[sid].append({"paper": paper, "id": row["id"]})
                for tie in statements[sid]["lean"]:
                    index(tie["declaration"], paper, row["id"], f"statement:{sid}",
                          statement=sid, source=tie["file"], relation=tie["relation"], review=tie["review_evidence"])
            for name in topic.get("constituents", []):
                index(name, paper, row["id"], "editorial_constituent")
            for label in topic.get("labels", []) + ([row["label"]] if "label" in row else []):
                for target in formal_targets[label]:
                    index(target["name"], paper, row["id"], f"label:{label}")
                    for join in target["graph_joins"]:
                        index(join["name"], paper, row["id"], join["basis"])
        coverage[paper] = {"source_sha256": document_index[paper]["sha256"], "selections": len(rows),
                           "linked_ledger_statements": len(covered), "editorial_topics": len(topic_ids),
                           "scope": "published_paper_statement_index" if paper == "original" else "indexed_manuscript_selections"}
        edition.add(f"selection/{paper}.json", rows)

    edition.add("selection/by-statement.json", by_statement)
    application_resources(edition, graph, recorded_names, topics)
    edition.add("selection/arguments.json", {"topics": topics, "treatments": treatments, "links": relations})
    used_by = defaultdict(list)
    for row in statements.values():
        for dep in row["depends_on"]:
            used_by[dep].append(row["id"])
    edition.add("selection/statement-users.json", used_by)
    edition.add("selection/targets.json", formal_targets)
    edition.add("selection/reverse.json", by_name)
    edition.add("selection/index.json", {"schema": "quartic-selection-v1", "revision": edition.commit,
               "documents": document_index,
               "graph": graph, "modules": names, "registry_revision": registry["commit"]})
    edition.resources["reader.mjs"] = edition.read("tools/reader.mjs")
    return coverage
