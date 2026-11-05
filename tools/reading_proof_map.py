"""Build the reader's paper-linked view of the headline Lean dependency closure."""
from collections import defaultdict, deque
import re

from build_comparator_map import lean_blocks

ROOT = "QuarticQuery.theorem_1_1_unconditional"
KINDS = ("value", "type", "structural")
# The opening cards and declarations whose source comments use only shorthand.
CAPTIONS = {
    "theorem_1_1_unconditional": "The nearly quartic separation for total Boolean functions",
    "alphaTot_eq_four_unconditional": "The optimal universal exponent is four",
    "family_bounds": "One circuit family witnesses both query bounds",
    "universalPower_four": "The universal quartic upper bound",
    "ForrelationLower.bansalSinhaLower": "Randomized hardness of the Forrelation promise problem",
    "Amplification.Preparation.grover": "The Grover iteration on a prepared state",
    "Amplification.groverCircuit": "Prepare a state and apply the Grover iterations",
    "Forrelation.P_eq_some_true_iff": "Forrelation at or above the threshold gives output one",
    "Forrelation.P_eq_some_false_iff": "Small absolute Forrelation gives output zero",
    "addressedF_eq_true_iff": "The addressed board accepts exactly when a column wins",
    "card_testIndex": "The number of local tests for a candidate column",
}


def neighbours(nodes, name):
    for kind in KINDS:
        for dep in nodes[name][kind]:
            if dep in nodes:
                yield kind, dep


def closure(nodes, root):
    seen = {root}
    queue = deque([root])
    while queue:
        for _, dep in neighbours(nodes, queue.popleft()):
            if dep not in seen:
                queue.append(dep)
                seen.add(dep)
    return seen


def map_edges(nodes, visible):
    """One shortest witnessed path per first-hop kind and next visible declaration.

    Each search stops when it reaches a card. Its predecessor tree is shared by
    all targets, so long common runs of helpers are stored only once.
    """
    edges = defaultdict(dict)
    walks = []
    # Every hop points back to its prefix. The first hop starts at the edge's source.
    prefixes = {}
    def hop(prefix, kind, target):
        key = (prefix, kind, target)
        if key not in prefixes:
            prefixes[key] = len(walks)
            walks.append(key)
        return prefixes[key]

    for source in sorted(visible):
        for first in KINDS:
            pending = deque((None, first, dep) for dep in nodes[source][first] if dep in nodes)
            seen = {source}
            while pending:
                prefix, kind, dep = pending.popleft()
                if dep in seen:
                    continue
                seen.add(dep)
                witness = hop(prefix, kind, dep)
                if dep in visible:
                    edges[source, dep][first] = witness
                else:
                    pending.extend((witness, k, n) for k, n in neighbours(nodes, dep) if n not in seen)
    # Discard dead ends: only prefixes used by an actual card-to-card witness travel.
    used = set()
    for witnesses in edges.values():
        for w in witnesses.values():
            while w is not None and w not in used:
                used.add(w)
                w = walks[w][0]
    ids = {w: i for i, w in enumerate(sorted(used))}
    paths = [[ids.get(walks[w][0]), *walks[w][1:]] for w in ids]
    return ([{"from": a, "to": b, "witnesses": {k: ids[w] for k, w in witnesses.items()}}
             for (a, b), witnesses in sorted(edges.items())], paths)


def declaration_info(edition, nodes, blocks, name):
    module = nodes[name]["module"]
    path = "lean/" + module.replace(".", "/") + ".lean"
    if module not in blocks:
        blocks[module] = {b["name"]: b for b in lean_blocks(edition.read(path).decode())}
    block = blocks[module].get(name)
    # Lean can name constructor projections and compiler-generated proof terms
    # for which the source index has no separate declaration.
    info = {"module": module, "source": path, "lines": None, "kind": None, "title": None}
    if block:
        comment = re.sub(r"\bLedger:\s*.*?(?:\.(?=\s|$)|$)", "", block["doc_comment"] or "").strip()
        comment = re.sub(r"^[A-Z][0-9]+\.\s+", "", comment)
        caption = CAPTIONS.get(name.removeprefix("QuarticQuery.")) or comment
        info.update(kind=block["kind"], lines=[block["line_start"], block["line_end"]],
                    title=re.split(r"(?<=\.)\s+", caption, maxsplit=1)[0] or None)
    return info


def proof_map(edition, graph, nodes, by_name, selections, statements):
    result = {"schema": "quartic-proof-map-v1", "revision": edition.commit, "root": ROOT,
              "currentness": graph["currentness"], "source_snapshot_sha256": graph["source_snapshot_sha256"]}
    if graph["currentness"] != "current":
        return result
    reachable = closure(nodes, ROOT)
    cards = {}
    locations = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
    blocks = {}
    for name in sorted((reachable & by_name.keys()) | {ROOT}):
        module = nodes[name]["module"]
        path = "lean/" + module.replace(".", "/") + ".lean"
        ties = {}
        linked = False
        for ref in by_name.get(name, []):
            # A registry label can refer to a frozen Challenge with the same name.
            # Only its verified implementation join, or an explicit source tie, qualifies.
            if ref["basis"].startswith("label:") or (ref.get("source") and ref["source"] != path):
                continue
            linked = True
            locations[ref["paper"]][ref["selection"]][name].add(ref["basis"])
            if sid := ref.get("statement"):
                if sid not in ties:
                    tie = next(t for t in statements[sid]["lean"] if t["file"] == path and t["declaration"] == name)
                    ties[sid] = {"relation": tie["relation"], "review": tie["review_evidence"], "route": tie["route"]}
        if not linked and name != ROOT:
            continue
        info = declaration_info(edition, nodes, blocks, name)
        if not info["title"] or not info["lines"]:
            raise ValueError(f"proof map: provide a reader caption and source range for {name}")
        cards[name] = {**info, "statements": ties}
    edges, paths = map_edges(nodes, cards)
    hidden = {target for _, _, target in paths} - cards.keys()
    helper_resource = "selection/proof-helpers.json"
    edition.add(helper_resource, {"revision": edition.commit, "source_snapshot_sha256": result["source_snapshot_sha256"],
                "helpers": {name: declaration_info(edition, nodes, blocks, name) for name in sorted(hidden)}})
    # One deterministic tree of real map edges for the initial layout. Other evidence
    # edges remain available, including alternative parents and reciprocal uses.
    adjacent = defaultdict(list)
    for edge in edges:
        adjacent[edge["from"]].append(edge)
    parent = {ROOT: None}
    queue = deque([ROOT])
    while queue:
        source = queue.popleft()
        for edge in sorted(adjacent[source], key=lambda e: (
                not any(paths[w][0] is None for w in e["witnesses"].values()),
                "value" not in e["witnesses"], e["to"])):
            dep = edge["to"]
            if dep not in parent:
                parent[dep] = source
                queue.append(dep)
    if parent.keys() != cards.keys():
        raise ValueError("disconnected headline proof map")
    for name in cards:
        cards[name]["parent"] = parent[name]
    papers = {paper: [{"id": r["id"], **({"page": r["location"]["page"]} if "location" in r else {"lines": r["lines"]}),
                       "bindings": {n: sorted(bases) for n, bases in locations[paper][r["id"]].items()}} for r in rows] for paper, rows in selections.items()}
    return {**result, "helper_resource": helper_resource, "closure_size": len(reachable), "cards": cards, "edges": edges, "paths": paths, "papers": papers}
