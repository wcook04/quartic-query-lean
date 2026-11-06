"""Attribute constants to retained, single-line original closing tactics.

Native parser ranges only schedule a shadow compilation inside caller ranges.
A low-memory reader accepts a retained marker payload only when erasing every
marker reproduces the declaration's entire compiled proof and unchanged type.
A completed compilation can produce no source hit.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from build_corpus import canonical_sha256, source_hashes
from record_reading_dependencies import ROOT, write_graph, native_output, exclusive_reader_capture
import record_reading_dependencies as dependency_capture
import record_proof_sites as reference_sites

PROGRAM = ROOT / "tools/ReadRetainedLines.lean"
OUTPUT = ROOT / "corpus/reading_retained_lines.json"


def fingerprint():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
            (Path(__file__), PROGRAM, Path(reference_sites.__file__), Path(dependency_capture.__file__))}


def schedule(manifest, snapshot, kernel):
    catalog = json.loads(manifest.read_bytes())
    def load(key):
        meta = catalog["resources"][key]
        raw = (manifest.parent / meta["href"]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != meta["sha256"]:
            raise ValueError(f"edition object changed: {key}")
        return json.loads(raw)
    view = load("selection/proof-map.json")
    if view["source_snapshot_sha256"] != snapshot or view["currentness"] != "current":
        raise ValueError("scheduling requires a current proof map of the same Lean sources")
    named = json.loads((ROOT / "corpus/reading_proof_sites.json").read_bytes())["nodes"]
    requests = defaultdict(set)
    for edge in view["edges"]:
        for cursor in edge["witnesses"].values():
            while cursor is not None:
                prev, kind, dep = view["paths"][cursor]
                caller = edge["from"] if prev is None else view["paths"][prev][2]
                if (kind == "value" and kernel[caller][kind][dep][0] == "body"
                        and not any(row[2] == "value" for row in named.get(caller, {}).get(dep, []))):
                    requests[caller].add(dep)
                cursor = prev
    return {c: sorted(ds) for c, ds in requests.items()}


def declaration_ranges(source, index, callers):
    """Use the compiled language-server index, including its primary-name check."""
    src = reference_sites.Source(source)
    ranges = {}
    for caller in callers:
        decl = index["decls"].get(caller)
        if decl is None:
            continue
        name_start, name_end = src.byte(*decl[4:6]), src.byte(*decl[6:8])
        if not reference_sites.names_token(caller, source[name_start:name_end].decode()):
            continue
        start, end = name_end, src.byte(*decl[2:4])
        if not 0 <= start < end <= len(source):
            raise ValueError(f"invalid declaration range for {caller}")
        ranges[caller] = [start, end]
    return ranges


def validated_rows(pairs, source, ranges, found):
    """Reject foreign callers, targets and source outside the native declaration."""
    rows = {}
    for caller, dep, lo, hi in sorted(found):
        bounds = ranges.get(caller)
        if (caller not in pairs or dep not in pairs[caller] or bounds is None
                or not bounds[0] <= lo < hi <= bounds[1] <= len(source)
                or b"\n" in source[lo:hi]):
            raise ValueError(f"unexpected retained use in {caller}")
        hits = rows.setdefault(caller, {}).setdefault(dep, [])
        if [lo, hi] not in hits:
            hits.append([lo, hi])
    return rows


def scheduled_spans(source, scoped):
    """Schedule native parser spans; attribution still requires a retained payload."""
    candidates = set()
    for caller, row in scoped.items():
        start, end = row["range"]
        for lo, hi in row.get("tactic_spans", []):
            if not start <= lo < hi <= end <= len(source) or b"\n" in source[lo:hi]:
                raise ValueError(f"invalid native tactic range for {caller}")
            candidates.add((lo, hi))
    # Nested tactics need disjoint replacements. Prefer the inner original node.
    kept = []
    for lo, hi in sorted(candidates, key=lambda span: (span[1] - span[0], span[0])):
        if not any(a < hi and lo < b for a, b in kept):
            kept.append((lo, hi))
    return sorted(kept)


def replay_module(lean, mod, source, scoped, max_rss_mib, native_env):
    """Compile one temporary shadow normally, then inspect only its own objects."""
    path = mod.replace(".", "/") + ".lean"
    scheduled = scheduled_spans(source, scoped)
    if not scheduled:
        return []
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        shadow = folder / path
        shadow.parent.mkdir(parents=True, exist_ok=True)
        frozen_source = folder / "original-source.lean"
        frozen_source.write_bytes(source)
        request = folder / "requests.json"
        request.write_text(json.dumps({"callers": scoped, "spans": scheduled}))
        command = ["lean", "-j1", "-M0", "--run", str(PROGRAM)]
        native_output([*command, "shadow", str(frozen_source), str(shadow), str(request)], lean, max_rss_mib, env=native_env)
        compiled = shadow.with_suffix(".olean")
        native_output(["lean", "-j1", "-M0", "-DautoImplicit=false", "-R", temp, "-o", str(compiled), str(shadow)],
                      lean, max_rss_mib, env=native_env)
        original = lean / ".lake/build/lib/lean" / Path(path).with_suffix(".olean")
        raw = native_output([*command, "inspect", str(original), str(compiled), str(request)], lean, max_rss_mib, env=native_env)
        return json.loads(raw)


def record(checkout, manifest, compare, jobs=1, max_rss_mib=4096, selected_modules=None):
    if jobs != 1:
        raise ValueError("native replay requires exactly one Lean job")
    sources = source_hashes(checkout)
    snapshot = canonical_sha256(sources)
    stamp = fingerprint()
    input_paths = [ROOT / "corpus/reading_dependencies.json", ROOT / "corpus/reading_kernel_paths.json"]
    if manifest:
        input_paths.extend([manifest, ROOT / "corpus/reading_proof_sites.json"])
    else:
        input_paths.append(OUTPUT)
    if OUTPUT.is_file() and OUTPUT not in input_paths:
        input_paths.append(OUTPUT)
    inputs = {p: p.read_bytes() for p in input_paths}
    previous = json.loads(inputs[OUTPUT]) if OUTPUT in inputs else {}
    graph = json.loads(inputs[input_paths[0]])
    kernel = json.loads(inputs[input_paths[1]])
    kernel_sha256 = hashlib.sha256(inputs[input_paths[1]]).hexdigest()
    if (checkout / "lean/lean-toolchain").read_text().strip() != graph["toolchain"]:
        raise ValueError("replay requires the inspected Lean toolchain")
    if sources != source_hashes(ROOT) or any(r["source_snapshot_sha256"] != snapshot for r in (graph, kernel)):
        raise ValueError("replay requires the inspected source snapshot")
    requests = schedule(manifest, snapshot, kernel["nodes"]) if manifest else json.loads(OUTPUT.read_bytes())["requests"]
    all_requests = requests
    modules = defaultdict(dict)
    for caller, deps in requests.items():
        node = graph["nodes"][caller]
        if not set(deps) <= set(node["value"]):
            raise ValueError(f"nondependency requested for {caller}")
        modules[node["module"]][caller] = deps
    if selected_modules:
        missing = set(selected_modules) - modules.keys()
        if missing:
            raise ValueError(f"no scheduled callers in modules: {sorted(missing)}")
        modules = {m: pairs for m, pairs in modules.items() if m in selected_modules}
        requests = {c: deps for pairs in modules.values() for c, deps in pairs.items()}
    previous_ok = (previous.get("schema") == "quartic-retained-lines-v1"
                   and previous.get("producers") == stamp
                   and previous.get("source_snapshot_sha256") == snapshot
                   and previous.get("toolchain") == graph["toolchain"]
                   and previous.get("kernel_sha256") == kernel_sha256)
    def module_pairs(pairs, module):
        return {c: ds for c, ds in pairs.items() if c in graph["nodes"] and graph["nodes"][c]["module"] == module}
    reusable = set()
    if previous_ok:
        candidates = set(previous["completed_modules"]) | previous.get("uninspected_modules", {}).keys()
        reusable = {m for m in candidates if module_pairs(previous["requests"], m)
                    and module_pairs(previous["requests"], m) == module_pairs(all_requests, m)}
    completed = set(previous.get("completed_modules", [])) & reusable
    uninspected = {m: error for m, error in previous.get("uninspected_modules", {}).items() if m in reusable}
    failed_attempts = {m: error for m, error in previous.get("failed_attempts", {}).items() if m in reusable}
    retained_callers = {c for c in previous.get("requests", {})
                        if c in graph["nodes"] and graph["nodes"][c]["module"] in reusable}
    rows = {c: row for c, row in previous.get("nodes", {}).items() if c in retained_callers}
    captured_ranges = {c: row for c, row in previous.get("declaration_ranges", {}).items() if c in retained_callers}
    requests = {**{c: previous["requests"][c] for c in retained_callers}, **requests}
    lean = checkout / "lean"
    # A missing/stale compiled object is an explicit prerequisite failure. Never
    # turn source-line inspection into a parallel build of the development.
    native_output(["lake", "--no-build", "build", "QuarticQuery"], lean, max_rss_mib)
    native_env = json.loads(native_output(["lake", "env", "python3", "-c",
        "import os,json; print(json.dumps(dict(os.environ)))"], lean, max_rss_mib))
    def inspect(item):
        mod, pairs = item
        path = mod.replace(".", "/") + ".lean"
        source = (lean / path).read_bytes()
        index = json.loads((lean / ".lake/build/lib/lean" / (mod.replace(".", "/") + ".ilean")).read_bytes())
        ranges = declaration_ranges(source, index, pairs)
        scoped = {c: {"targets": pairs[c], "range": bounds,
                      "tactic_spans": kernel["nodes"][c].get("tactic_spans", [])}
                  for c, bounds in ranges.items()}
        cache_id = hashlib.sha256(json.dumps([stamp, snapshot, mod, scoped], sort_keys=True).encode()).hexdigest()
        cache = lean / ".lake/build/quartic-retained-lines" / (cache_id + ".json")
        if cache.is_file() and not compare:
            return pairs, source, ranges, json.loads(cache.read_bytes())
        print(f"Replaying {mod}", flush=True)
        hits = replay_module(lean, mod, source, scoped, max_rss_mib, native_env)
        raw = json.dumps(hits).encode()
        cache.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=cache.parent, delete=False) as fp:
            fp.write(raw)
        Path(fp.name).replace(cache)
        return pairs, source, ranges, hits

    for item in sorted(modules.items()):
        try:
            pairs, source, ranges, found = inspect(item)
        except (RuntimeError, subprocess.CalledProcessError) as error:
            # Preserve completed native evidence; a resource-limited or rejected
            # replay supplies no attribution for this module and is never retried.
            reason = (f"native replay exited with code {error.returncode}"
                      if isinstance(error, subprocess.CalledProcessError) else str(error))
            if item[0] in completed:
                failed_attempts[item[0]] = reason
            else:
                uninspected[item[0]] = reason
            print(f"Uninspected {item[0]}: {reason}", flush=True)
            if isinstance(error, subprocess.CalledProcessError) and error.output:
                print(error.output.decode(errors="replace"), flush=True)
            if compare:
                raise ValueError(f"native retained replay failed for {item[0]}: {reason}") from error
            continue
        for caller in pairs:
            rows.pop(caller, None)
            captured_ranges.pop(caller, None)
        captured_ranges.update(ranges)
        rows.update(validated_rows(pairs, source, ranges, found))
        completed.add(item[0])
        uninspected.pop(item[0], None)
        failed_attempts.pop(item[0], None)
    if (sources != source_hashes(checkout) or sources != source_hashes(ROOT) or stamp != fingerprint()
            or any(p.read_bytes() != raw for p, raw in inputs.items())):
        raise ValueError("inspection inputs changed during replay")
    result = {"schema": "quartic-retained-lines-v1", "producers": stamp, "toolchain": graph["toolchain"],
              "source_snapshot_sha256": snapshot, "kernel_sha256": kernel_sha256,
              "requests": requests, "declaration_ranges": captured_ranges,
              "completed_modules": sorted(completed), "uninspected_modules": uninspected,
              "failed_attempts": failed_attempts, "nodes": rows}
    if compare:
        if result != json.loads(OUTPUT.read_bytes()):
            raise ValueError("retained lines differ from saved inspection")
    else:
        write_graph(result, OUTPUT)
    print(f"Confirmed retained proof lines in {len(rows)} declarations; "
          f"{len(completed)} completed modules, {len(uninspected)} uninspected modules")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--checkout", type=Path, default=ROOT)
    cli.add_argument("--select-from", type=Path, help="select candidate body dependencies from a local reading edition")
    cli.add_argument("--compare", action="store_true")
    cli.add_argument("--jobs", type=int, choices=(1,), default=1)
    cli.add_argument("--max-rss-mib", type=int, default=4096, help="live native process-tree RSS limit")
    cli.add_argument("--module", action="append", help="limit capture to this scheduled module; repeatable")
    args = cli.parse_args()
    checkout = args.checkout.resolve()
    with exclusive_reader_capture(checkout):
        record(checkout, args.select_from, args.compare, args.jobs, args.max_rss_mib, args.module)
