"""Capture Lean language-server reference ranges for compiled Quartic dependencies."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from build_corpus import canonical_sha256, source_hashes
from record_reading_dependencies import ROOT, write_graph

DESTINATION = ROOT / "corpus/reading_proof_sites.json"
PARSER = ROOT / "tools/ReadUseRegions.lean"


def producers():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__), PARSER)}


class Source:
    """Translate LSP (zero-based line, UTF-16 column) to original UTF-8 bytes."""
    def __init__(self, raw):
        self.raw = raw
        self.lines = raw.decode().split("\n")
        self.starts = []
        start = 0
        for line in self.lines:
            self.starts.append(start)
            start += len(line.encode()) + 1

    def byte(self, line, col):
        if not 0 <= line < len(self.lines) or col < 0:
            raise ValueError("invalid Lean reference position")
        units = self.lines[line].encode("utf-16-le")
        if 2*col > len(units):
            raise ValueError("Lean position outside source line")
        return self.starts[line] + len(units[:2*col].decode("utf-16-le").encode())


def record(checkout, compare=False):
    before = source_hashes(checkout)
    snapshot = canonical_sha256(before)
    graph_path = ROOT / "corpus/reading_dependencies.json"
    graph_bytes = graph_path.read_bytes()
    graph = json.loads(graph_bytes)
    stamp = producers()
    if before != source_hashes(ROOT) or snapshot != graph["source_snapshot_sha256"]:
        raise ValueError("dependency graph or build checkout differs from the current Lean sources")
    lean = checkout / "lean"
    subprocess.run(["lake", "build", "QuarticQuery"], cwd=lean, check=True)
    nodes = graph["nodes"]
    commands, starts, sites = {}, {}, defaultdict(lambda: defaultdict(set))
    for module in sorted({node["module"] for node in nodes.values()}):
        rel = module.replace(".", "/")
        src = Source((lean / (rel + ".lean")).read_bytes())
        index = json.loads((lean / ".lake/build/lib/lean" / (rel + ".ilean")).read_bytes())
        if index["version"] != 5 or index["module"] != module:
            raise ValueError(f"unexpected Lean reference index for {module}")
        for key, refs in index["references"].items():
            target = json.loads(key).get("c", {})
            name = target.get("n")
            if name not in nodes or target["m"] != nodes[name]["module"]:
                continue
            for usage in refs["usages"]:
                if len(usage) != 5:
                    continue
                l0, c0, l1, c1, caller = usage
                node = nodes.get(caller)
                if not node or node["module"] != module or not any(name in node[k] for k in ("value", "type", "structural")):
                    continue
                decl = index["decls"].get(caller)
                if not decl or l0 != l1:
                    continue
                low, high = src.byte(l0, c0), src.byte(l1, c1)
                begin, end = src.byte(*decl[:2]), src.byte(*decl[2:4])
                if not begin <= src.byte(*decl[6:8]) <= low < high <= end:
                    continue
                token = src.raw[low:high].decode()
                if not token or not (name == token or name.endswith("." + token)):
                    continue
                sites[caller][name].add((low, high))
                if caller not in commands:
                    commands[caller] = src.raw[begin:end].decode()
                    starts[caller] = begin
    with tempfile.TemporaryDirectory() as temp:
        inputs = Path(temp) / "commands.json"
        inputs.write_text(json.dumps(sorted(commands.items()), ensure_ascii=False))
        boundaries = json.loads(subprocess.check_output(["lake", "env", "lean", "--run", str(PARSER), str(inputs)], cwd=lean))
    if boundaries.keys() != commands.keys():
        raise ValueError("incomplete source-region inspection")
    rows = {}
    for caller, refs in sites.items():
        cut = boundaries[caller]
        if cut is not None:
            cut += starts[caller]
        rows[caller] = {dep: [[lo, hi, "type" if hi <= cut else "value" if lo >= cut else "unknown"]
                               if cut is not None else [lo, hi, "unknown"] for lo, hi in sorted(spans)]
                        for dep, spans in refs.items()}
    payload = {"schema": "quartic-lean-reference-sites-v1", "source_snapshot_sha256": snapshot,
               "producers": stamp, "toolchain": graph["toolchain"], "nodes": rows}
    if (source_hashes(checkout) != before or source_hashes(ROOT) != before or stamp != producers()
            or graph_path.read_bytes() != graph_bytes):
        raise ValueError("source inputs changed during reference inspection")
    if compare:
        if json.loads(DESTINATION.read_bytes()) != payload:
            raise ValueError("Lean reference sites differ from the saved inspection")
    else:
        write_graph(payload, DESTINATION)
    print(f"Recorded references in {len(rows)} compiled declarations")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=ROOT)
    parser.add_argument("--compare", action="store_true")
    args = parser.parse_args()
    record(args.checkout.resolve(), args.compare)
