"""Replay exact addresses of project dependencies in Lean's compiled declarations."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import os
from tempfile import TemporaryDirectory

from build_comparator_map import lean_blocks
from build_corpus import canonical_sha256, source_hashes
from reading_proof_map import KINDS, ROOT as THEOREM, closure
import record_reading_dependencies as native
from record_reading_dependencies import ROOT, exclusive_reader_capture, native_output, write_graph
import record_proof_sites as reference_sites
from record_proof_sites import Source, names_token

PROGRAM = ROOT / "tools/ReadKernelPaths.lean"
OUTPUT = ROOT / "corpus/reading_kernel_paths.json"


def fingerprint():
    producers = (Path(__file__), PROGRAM, Path(reference_sites.__file__), Path(native.__file__))
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in producers}


def record(checkout, compare, max_rss_mib):
    graph_file = ROOT / "corpus/reading_dependencies.json"
    graph_raw = graph_file.read_bytes()
    graph = json.loads(graph_raw)
    snapshot = graph["source_snapshot_sha256"]
    sources = source_hashes(checkout)
    stamp = fingerprint()
    if sources != source_hashes(ROOT) or canonical_sha256(sources) != snapshot:
        raise ValueError("built checkout, local sources and dependency snapshot must agree")
    lean = checkout / "lean"
    if (lean / "lean-toolchain").read_text().strip() != graph["toolchain"]:
        raise ValueError("toolchain differs from the recorded dependency graph")
    native_output(["lake", "--no-build", "build", "QuarticQuery"], lean, max_rss_mib)
    nodes = graph["nodes"]
    reachable = closure(nodes, THEOREM)
    titles_path = ROOT / "docs/reading_helper_titles.json"
    titles = titles_path.read_bytes()
    helper_names = set(json.loads(titles))
    signatures = set()
    definitions = {}
    commands = {}
    ctor_refs = defaultdict(list)
    for mod in sorted({nodes[n]["module"] for n in reachable}):
        rel = mod.replace(".", "/")
        source = Source((lean / (rel + ".lean")).read_bytes())
        blocks = {b["name"] for b in lean_blocks(source.raw.decode())}
        signatures.update(n for n in helper_names & reachable if nodes[n]["module"] == mod and n not in blocks)
        index = json.loads((lean / ".lake/build/lib/lean" / (rel + ".ilean")).read_bytes())
        if index["module"] != mod or index["version"] != 5:
            raise ValueError(f"unexpected native reference index for {mod}")
        for caller, pos in index["decls"].items():
            if caller not in reachable:
                continue
            start, end = source.byte(*pos[:2]), source.byte(*pos[2:4])
            a, b = source.byte(*pos[4:6]), source.byte(*pos[6:8])
            if names_token(caller, source.raw[a:b].decode()):
                commands[caller] = (start, source.raw[start:end].decode(), [a-start, b-start])
        for key, info in index["references"].items():
            target = json.loads(key).get("c", {})
            name = target.get("n")
            if name in reachable and nodes[name]["module"] == target.get("m"):
                for u in info["usages"]:
                    if len(u) == 5 and u[4] in reachable and nodes[u[4]]["structural"]:
                        a, b = source.byte(*u[:2]), source.byte(*u[2:4])
                        if names_token(name, source.raw[a:b].decode()):
                            ctor_refs[u[4]].append((name, a, b))
            pos = info.get("definition")
            if target.get("m") != mod or name not in reachable or not pos or len(pos) != 5:
                continue
            if pos[4] not in reachable or nodes[pos[4]]["module"] != mod:
                continue
            lo, hi = source.byte(*pos[:2]), source.byte(*pos[2:4])
            if names_token(name, source.raw[lo:hi].decode()):
                definitions[name] = {"owner": pos[4], "bytes": [lo, hi], "lines": [pos[0]+1, pos[2]+1]}
    requests = {n: {**{k: sorted(set(nodes[n][k]) & reachable) for k in KINDS},
                    "signature": n in signatures} for n in sorted(reachable)}
    for name, (_, command, pos) in commands.items():
        requests[name].update(command=command, id=pos)
    with TemporaryDirectory() as temp:
        path = Path(temp) / "requests.json"
        by_module = defaultdict(dict)
        for name, row in requests.items():
            by_module[nodes[name]["module"]][name] = row
        path.write_text(json.dumps(by_module))
        env = {**os.environ, "LEAN_PATH": native_output(["lake", "env", "printenv", "LEAN_PATH"],
                                                       lean, max_rss_mib).decode().strip()}
        rows = json.loads(native_output(["lean", "-j1", "--run", str(PROGRAM), str(path)],
                                        lean, max_rss_mib, env=env))
    if rows.keys() != requests.keys():
        raise ValueError("Lean did not inspect all requested declarations")
    for caller, req in requests.items():
        row = rows[caller]
        for k in KINDS:
            if set(req[k]) != set(row.get(k, {})):
                raise ValueError(f"missing compiled witnesses for {caller} ({k})")
        if req["signature"] and not row.get("signature"):
            raise ValueError(f"missing compiled signature for {caller}")
        if caller in definitions:
            row["written_definition"] = definitions[caller]
    for owner, row in rows.items():
        regions = row.pop("source_regions", None)
        if not regions:
            continue
        start, text, _ = commands[owner]
        absolute = lambda span: [start + span[0], start + span[1]]
        # Nested tactics can overlap. Prefer the smallest original tactic so all
        # tagged replacements can coexist in one compilation of the module.
        selected = []
        for lo, hi in sorted(regions["tactics"], key=lambda span: (span[1] - span[0], span[0])):
            if not any(a < hi and lo < b for a, b in selected):
                selected.append([lo, hi])
        if selected:
            row["tactic_spans"] = [absolute(span) for span in sorted(selected)]
        if result := regions["result"]:
            a, b = result
            if b"\n" not in text.encode()[a:b]:
                row["result_line"] = absolute(result)
        for binder in regions["binders"]:
            a, b = absolute(binder["domain"])
            for name in binder["names"]:
                row.setdefault("written_domains", {}).setdefault(name, []).append([a, b])
        for ctor in regions["constructors"]:
            pos = absolute(ctor["name"])
            matches = [n for n in row.get("structural", {}) if definitions.get(n, {}).get("bytes") == pos
                       and definitions[n]["owner"] == owner and row["structural"][n][0] == "constructors"]
            if len(matches) != 1:
                continue
            n, = matches
            lo, hi = absolute(ctor["signature"])
            for dep, a, b in ctor_refs[owner]:
                if lo <= a < b <= hi and dep in rows[n].get("type", {}):
                    rows[n].setdefault("constructor_uses", {}).setdefault(dep, []).append([a, b])
    if (source_hashes(checkout) != sources or source_hashes(ROOT) != sources or fingerprint() != stamp
            or graph_file.read_bytes() != graph_raw or titles_path.read_bytes() != titles):
        raise ValueError("inspection inputs changed during capture")
    payload = {"schema": "quartic-kernel-paths-v1", "producers": stamp, "toolchain": graph["toolchain"],
               "source_snapshot_sha256": snapshot, "dependency_sha256": hashlib.sha256(graph_raw).hexdigest(),
               "nodes": rows}
    if compare:
        if json.loads(OUTPUT.read_bytes()) != payload:
            raise ValueError("kernel paths differ from the recorded inspection")
    else:
        write_graph(payload, OUTPUT)
    print(f"Verified kernel addresses in {len(rows)} declarations")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--checkout", type=Path, default=ROOT)
    cli.add_argument("--compare", action="store_true")
    cli.add_argument("--max-rss-mib", type=int, default=6144, help="live native process-tree RSS limit")
    args = cli.parse_args()
    with exclusive_reader_capture(args.checkout.resolve()):
        record(args.checkout.resolve(), args.compare, args.max_rss_mib)
