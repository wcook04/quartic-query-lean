"""Capture the source of inherited parameters on the amplification proof paths."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess

from build_corpus import canonical_sha256, source_hashes
from record_proof_sites import Source, names_token
from record_reading_dependencies import ROOT, write_graph


# These modules contain the inherited section binders on the reader's proof paths.
MODULES = tuple("QuarticQuery.Amplification." + m for m in ("Geometry", "Bounded", "Procedure"))
INSPECTOR = ROOT / "tools/ReadParameterOrigins.lean"
OUTPUT = ROOT / "corpus/reading_parameter_origins.json"


def producers():
    files = (Path(__file__), INSPECTOR, ROOT / "tools/record_proof_sites.py")
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def record(checkout, compare):
    sources = source_hashes(checkout)
    snapshot = canonical_sha256(sources)
    graph_path = ROOT / "corpus/reading_dependencies.json"
    graph_bytes = graph_path.read_bytes()
    graph = json.loads(graph_bytes)
    fingerprint = producers()
    if sources != source_hashes(ROOT) or snapshot != graph["source_snapshot_sha256"]:
        raise ValueError("Lean sources and the dependency graph must agree")
    lean = checkout / "lean"
    subprocess.run(["lake", "build", "QuarticQuery"], cwd=lean, check=True)
    nodes = {}
    for module in MODULES:
        rel = module.replace(".", "/")
        source = Source((lean / (rel + ".lean")).read_bytes())
        index = json.loads((lean / ".lake/build/lib/lean" / (rel + ".ilean")).read_bytes())
        if index["version"] != 5 or index["module"] != module:
            raise ValueError(f"unexpected Lean index for {module}")
        # Corroborate the type constructor at the binder with the resolved token
        # from Lean's independent reference index.
        tokens = defaultdict(list)
        for key, info in index["references"].items():
            ref = json.loads(key).get("c", {})
            dep = ref.get("n")
            if dep not in graph["nodes"] or ref["m"] != graph["nodes"][dep]["module"]:
                continue
            for use in info["usages"]:
                if len(use) == 4 and use[0] == use[2]:
                    lo, hi = source.byte(*use[:2]), source.byte(*use[2:])
                    if names_token(dep, source.raw[lo:hi].decode()):
                        tokens[dep].append((lo, hi))
        print(f"Checking inherited parameters in {module}", flush=True)
        rows = json.loads(subprocess.check_output(
            ["lake", "env", "lean", "--run", str(INSPECTOR), module, rel + ".lean"], cwd=lean))
        origins = defaultdict(set)
        for row in rows:
            caller, dep = row["caller"], row["target"]
            graph_node = graph["nodes"].get(caller)
            decl = index["decls"].get(caller)
            if not graph_node or graph_node["module"] != module or not decl or dep not in graph_node["type"]:
                continue
            lo, hi = row["lo"], row["hi"]
            if hi > source.byte(*decl[:2]):
                continue
            hits = [(a, b) for a, b in tokens[dep] if lo <= a < b <= hi]
            if len(hits) == 1:
                origins[caller, dep, row["parameter"]].add((lo, hi, *hits[0], row["value"] and dep in graph_node["value"]))
        for (caller, dep, name), candidates in sorted(origins.items()):
            if len(candidates) == 1:
                lo, hi, a, b, value = candidates.pop()
                nodes.setdefault(caller, {}).setdefault(dep, []).append(
                    {"parameter": name, "binder": [lo, hi], "identifier": [a, b], "in_value_parameter": value})
    if (sources != source_hashes(checkout) or sources != source_hashes(ROOT)
            or graph_bytes != graph_path.read_bytes() or fingerprint != producers()):
        raise ValueError("inputs changed during parameter inspection")
    record = {"schema": "quartic-parameter-origins-v1", "source_snapshot_sha256": snapshot,
              "producers": fingerprint, "toolchain": graph["toolchain"], "nodes": nodes}
    if compare:
        if json.loads(OUTPUT.read_bytes()) != record:
            raise ValueError("inherited parameter observations differ from recorded inspection")
    else:
        write_graph(record, OUTPUT)
    print(f"Confirmed inherited parameters for {len(nodes)} declarations")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--checkout", type=Path, default=ROOT)
    cli.add_argument("--compare", action="store_true")
    args = cli.parse_args()
    record(args.checkout.resolve(), args.compare)
