"""Join authored reading paths to source sites and captured Lean application arguments."""
from collections import defaultdict
from fractions import Fraction
import hashlib
import re

from build_comparator_map import lean_blocks


def witnessed_occurrences(records, caller, callee, raw, low, high):
    """Only return source observations wholly contained in this authored excerpt."""
    spans = defaultdict(list)
    for row in records:
        if row["caller"] != caller or row["term"]["callee"] != callee:
            continue
        start, end = row["start"], row["end"]
        if not 0 <= start < end <= len(raw):
            raise ValueError(f"{caller}: invalid elaboration span")
        if raw[start:end].decode() != row["source_text"]:
            raise ValueError(f"{caller}: source bytes differ from recorded occurrence")
        if low <= start and end <= high:
            spans[start, end].append(row["term"])
    found = []
    for (start, end), terms in sorted(spans.items()):
        if len(terms) == 1:
            found.append({"utf8_bytes": [start, end], "text": raw[start:end].decode(),
                          "term": terms[0], "basis": "original_syntax_and_matching_body_expr"})
    return found


def obligation_notes(step, steps, uses):
    notes = []
    for rule in step.get("obligations", []):
        use = next((u for u in uses if u["declaration"] == rule["callee"]), None)
        if use is None or len(rule["match"]) != 1:
            raise ValueError(f"{step['id']}: invalid obligation selector")
        matches = []
        for number, term in enumerate(use["compiled_uses_in_caller"]):
            for arg in term["arguments"]:
                if arg["binder"] != rule["binder"] or not arg["proof"]:
                    continue
                key, value = next(iter(rule["match"].items()))
                if key == "project_constant":
                    matched = value in arg["project_constants"]
                elif key in {"argument", "head_constant"}:
                    matched = arg[key] == value
                else:
                    raise ValueError(f"unknown proof argument selector {key}")
                if matched:
                    matches.append({"compiled_use_index": number, "type": arg["type"], "basis": arg["basis"]})
        if not matches:
            raise ValueError(f"{step['id']}: no compiled proof for obligation {rule['binder']}")
        note = {"callee": rule["callee"], "binder": rule["binder"], "evidence": matches,
                "explanation": rule["explanation"]}
        if assembly := rule.get("assembly"):
            later = steps[assembly["step"]]
            if assembly["provider"] not in later["callees"] or assembly["applied"] not in later["site"]:
                raise ValueError(f"{step['id']}: unsupported assembly link")
            note["assembly"] = {**assembly, "basis": "editorial_link_to_witnessed_step"}
        notes.append(note)
    return notes


def application_resources(edition, graph, nodes, topics):
    plan = edition.json("docs/reading_applications.json")
    inspection = edition.json("corpus/reading_applications.json")
    program = edition.read("tools/ReadApplications.lean")
    snapshot = graph["source_snapshot_sha256"]
    if inspection["schema"] != "quartic-lean-applications-v2":
        raise ValueError("unknown Lean application inspection")
    if set(plan["occurrence_modules"]) != set(inspection["source_occurrences"]):
        raise ValueError("refresh the selected source-occurrence inspections")
    if not (inspection["inspector_sha256"] == hashlib.sha256(program).hexdigest()
            and plan["source_snapshot_sha256"] == inspection["source_snapshot_sha256"] == snapshot
            and graph["toolchain"] == inspection["toolchain"]):
        raise ValueError("review reading applications and refresh the Lean inspection")
    index = {"currentness": graph["currentness"], "source_snapshot_sha256": snapshot,
             "inspector_sha256": inspection["inspector_sha256"], "occurrence_modules": plan["occurrence_modules"],
             "journeys": {}, "by_topic": defaultdict(list), "by_declaration": defaultdict(list)}
    if graph["currentness"] != "current":
        edition.add("selection/applications.json", index)
        return

    family_overview = None
    blocks = {}
    offsets = {}

    def declaration(name):
        if name not in nodes:
            raise ValueError(f"unknown application declaration {name}")
        source = "lean/" + nodes[name]["module"].replace(".", "/") + ".lean"
        if source not in blocks:
            raw = edition.read(source)
            blocks[source] = {b["name"]: b for b in lean_blocks(raw.decode())}
            offsets[source] = [0]
            for line in raw.splitlines(keepends=True):
                offsets[source].append(offsets[source][-1] + len(line))
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
        authored = {s["id"]: s for s in journey["steps"]}
        if len(authored) != len(journey["steps"]):
            raise ValueError(f"{ident}: duplicate step ID")
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
            raw = edition.read(source)
            prefix = block["text"][:block["text"].index(site)].encode()
            low = offsets[source][block["line_start"] - 1] + len(prefix)
            high = low + len(site.encode())
            if raw[low:high].decode() != site:
                raise ValueError(f"{caller}: source byte range differs")
            uses = []
            declarations.add(caller)
            for callee in step["callees"]:
                terms = [row for row in inspection["callers"].get(caller, []) if row["callee"] == callee]
                spelling = re.escape(callee.rsplit(".", 1)[-1])
                mentioned = re.search(r"(?<![\w'])" + spelling + r"(?![\w'])", site)
                if not terms or callee not in nodes[caller]["value"] or not mentioned:
                    raise ValueError(f"{caller}: unwitnessed use of {callee}")
                module = nodes[caller]["module"]
                exact = witnessed_occurrences(inspection["source_occurrences"].get(module, []),
                                               caller, callee, raw, low, high)
                status = "unresolved_in_excerpt" if module in inspection["source_occurrences"] else "module_not_inspected"
                if exact:
                    status = "witnessed"
                uses.append({"declaration": callee, "kind": "value", "occurrence_status": status,
                             "attribution": "exact_source_occurrence" if exact else "source_associated",
                             "compiled_term_scope": "declaration", "occurrences": exact,
                             "compiled_uses_in_caller": terms})
                declarations.add(callee)
            result = {"id": step["id"], "title": step["title"], "topic": step["topic"],
                      "mechanism": step["mechanism"], "caller": caller, "source": source, "text": site,
                      "lines": [start, start + site.count("\n")], "uses": uses,
                      "obligations": obligation_notes(step, authored, uses)}
            if step.get("shared_board"):
                identity = inspection["same_board"][caller]
                if not set(identity["bounds"]).issubset(nodes[caller]["type"]):
                    raise ValueError(f"{caller}: board bounds differ from the declaration type")
                result["shared_board"] = identity
            steps.append(result)
        for name in sorted(declarations):
            index["by_declaration"][name].append(ident)
        presentation = {}
        if "overview" in journey:
            seen = set()
            assigned = []
            for stage in journey["overview"]:
                if stage["id"] in seen or set(stage["after"]) - seen:
                    raise ValueError(f"{ident}: invalid reading order in overview")
                seen.add(stage["id"])
                assigned.extend(stage["steps"])
            if sorted(assigned) != sorted(s["id"] for s in steps):
                raise ValueError(f"{ident}: overview must assign every inspected step exactly once")
            if ident == "forrelation-family":
                presentation["scaling"] = {
                    "topic": "exponent", "scope": "leading_powers_ignoring_logarithmic_factors",
                    "parameters": "For each proposed exponent below four, choose k large enough, keep k fixed, then let t grow in the admissible family.",
                    "examples": [{"k": k, "quantum_power_in_m": "1/2",
                                  "classical_power_in_m": str(Fraction(2*k-1, k)),
                                  "classical_power_in_sqrt_m": str(Fraction(4*k-2, k))}
                                 for k in (2, 3, 4, 8, 16)]}
                family_overview = {"overview": journey["overview"], "scaling": presentation["scaling"]}
        edition.add(path, {**journey, **presentation, "steps": steps})
    edition.add("selection/applications.json", index)
    return family_overview
