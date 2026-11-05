"""Join authored reading paths to source sites and captured Lean application arguments."""
from collections import defaultdict
import hashlib

from build_comparator_map import lean_blocks


def application_resources(edition, graph, nodes, topics):
    plan = edition.json("docs/reading_applications.json")
    inspection = edition.json("corpus/reading_applications.json")
    program = edition.read("tools/ReadApplications.lean")
    snapshot = graph["source_snapshot_sha256"]
    if inspection["schema"] != "quartic-lean-applications-v1":
        raise ValueError("unknown Lean application inspection")
    if not (inspection["inspector_sha256"] == hashlib.sha256(program).hexdigest()
            and plan["source_snapshot_sha256"] == inspection["source_snapshot_sha256"] == snapshot
            and graph["toolchain"] == inspection["toolchain"]):
        raise ValueError("review reading applications and refresh the Lean inspection")
    index = {"currentness": graph["currentness"], "source_snapshot_sha256": snapshot,
             "inspector_sha256": inspection["inspector_sha256"],
             "journeys": {}, "by_topic": defaultdict(list), "by_declaration": defaultdict(list)}
    if graph["currentness"] != "current":
        edition.add("selection/applications.json", index)
        return

    blocks = {}

    def declaration(name):
        if name not in nodes:
            raise ValueError(f"unknown application declaration {name}")
        source = "lean/" + nodes[name]["module"].replace(".", "/") + ".lean"
        if source not in blocks:
            blocks[source] = {b["name"]: b for b in lean_blocks(edition.read(source).decode())}
        if name not in blocks[source]:
            raise ValueError(f"missing source declaration for {name}")
        return source, blocks[source][name]

    for journey in plan["journeys"]:
        ident = journey["id"]
        if (ident in index["journeys"] or not journey["steps"] or not journey["topics"]
                or set(journey["topics"]) - topics.keys()):
            raise ValueError(f"invalid application journey {ident}")
        path = f"applications/{ident}.json"
        index["journeys"][ident] = {"title": journey["title"], "resource": path}
        for topic in journey["topics"]:
            index["by_topic"][topic].append(ident)
        steps = []
        declarations = set(journey["interfaces"])
        for name in declarations:
            declaration(name)
        for step in journey["steps"]:
            if step["topic"] not in journey["topics"]:
                raise ValueError(f"{ident}: unknown step topic {step['topic']}")
            caller = step["caller"]
            source, block = declaration(caller)
            site = step["site"]
            if not site or block["text"].count(site) != 1:
                raise ValueError(f"{caller}: changed or ambiguous application site")
            start = block["line_start"] + block["text"][:block["text"].index(site)].count("\n")
            uses = []
            declarations.add(caller)
            for callee in step["callees"]:
                terms = [row for row in inspection["callers"].get(caller, []) if row["callee"] == callee]
                if not terms or callee not in nodes[caller]["value"] or callee.rsplit(".", 1)[-1] not in site:
                    raise ValueError(f"{caller}: unwitnessed use of {callee}")
                uses.append({"declaration": callee, "kind": "value", "compiled_uses_in_caller": terms})
                declarations.add(callee)
            steps.append({"title": step["title"], "topic": step["topic"], "caller": caller, "source": source, "text": site,
                          "lines": [start, start + site.count("\n")], "uses": uses})
        for name in sorted(declarations):
            index["by_declaration"][name].append(ident)
        edition.add(path, {**journey, "steps": steps})
    edition.add("selection/applications.json", index)
