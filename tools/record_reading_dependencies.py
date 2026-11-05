#!/usr/bin/env python3
"""Record typed Lean dependencies from a built, source-identical Quartic checkout."""
import argparse
from contextlib import contextmanager
import os
import signal
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from build_corpus import canonical_sha256, source_hashes

ROOT = Path(__file__).resolve().parents[1]
INSPECTOR = ROOT / "tools/ReadDependencies.lean"
OUTPUT = ROOT / "corpus/reading_dependencies.json"


@contextmanager
def exclusive_reader_capture(checkout):
    """Limit native proof-map inspections to one per built checkout.

    Hold the OS lock for the whole capture, including the Lake preflight. The
    lockfile can stay in the build cache. Closing its handle releases the lock.
    """
    directory = checkout / "lean/.lake/build"
    if not directory.is_dir():
        raise ValueError("proof-map inspection requires an existing built Lean checkout")
    with (directory / "quartic-reader-capture.lock").open("a+b") as handle:
        try:
            if os.name == "nt":
                import msvcrt
                if handle.tell() == 0:
                    handle.write(b"0")
                    handle.flush()
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise RuntimeError("another native proof-map inspection may already own the build cache") from exc
        yield


def native_output(command, cwd, max_rss_mib=4096, env=None):
    """Bound the live process tree by observed RSS; kill the owned group on failure."""
    with tempfile.TemporaryFile() as output:
        proc = subprocess.Popen(command, cwd=cwd, stdout=output, start_new_session=True, env=env)
        try:
            while True:
                try:
                    code = proc.wait(timeout=1)
                    break
                except subprocess.TimeoutExpired:
                    usage = subprocess.check_output(["ps", "-axo", "pid=,ppid=,rss="], text=True)
                    processes = [tuple(map(int, line.split())) for line in usage.splitlines()]
                    owned = {proc.pid}
                    while True:
                        children = {pid for pid, parent, _ in processes if parent in owned}
                        if children <= owned:
                            break
                        owned.update(children)
                    rss = sum(kib for pid, _, kib in processes if pid in owned)
                    if rss > max_rss_mib * 1024:
                        raise RuntimeError(f"native replay exceeded {max_rss_mib} MiB RSS budget")
            output.seek(0)
            if code:
                raise subprocess.CalledProcessError(code, command, output=output.read())
            return output.read()
        finally:
            if proc.poll() is None:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()


def write_graph(payload, destination):
    # One record per line makes a changed declaration visible in a Git diff.
    header = {k: v for k, v in payload.items() if k != "nodes"}
    with tempfile.NamedTemporaryFile(mode="w", dir=destination.parent, delete=False) as tmp:
        tmp.write(json.dumps(header, sort_keys=True)[:-1] + ', "nodes": {\n')
        for i, (name, node) in enumerate(sorted(payload["nodes"].items())):
            if i:
                tmp.write(",\n")
            tmp.write(json.dumps(name) + ":" + json.dumps(node, sort_keys=True, separators=(",", ":")))
        tmp.write("\n}}\n")
    output = Path(tmp.name)
    output.chmod(0o644)
    output.replace(destination)


def source_records(rows, raw):
    for row in rows:
        start, end = row["start"], row["end"]
        if not 0 <= start < end <= len(raw):
            raise ValueError("invalid application range returned by Lean")
        row["source_text"] = raw[start:end].decode()
    return sorted(rows, key=lambda r: (r["start"], r["end"], r["caller"], r["term"]["callee"]))


def application_pairs(config):
    return sorted({step["caller"] + "=" + name for journey in config["journeys"]
                   for step in journey["steps"] for name in step["callees"]})


def statement_targets(statements, probes):
    """Key observations by their defining module as well as their Lean name."""
    targets = {(t["file"], t["declaration"]) for row in statements for t in row["lean"]
               if t["review_evidence"] == "current"}
    targets.update((f"lean/QuarticCorpus/Independent/{p['file']}.lean",
                    "QuarticQuery.SemanticReview." + p["name"]) for p in probes)
    return sorted(path.removeprefix("lean/").removesuffix(".lean").replace("/", ".") + "/" + name
                  for path, name in targets)


def record_statements(root, before, compare):
    program = ROOT / "tools/ReadStatementEvidence.lean"
    inspector = program.read_bytes()

    def selection():
        rows = json.loads((ROOT / "corpus/statements.json").read_bytes())
        probes = json.loads((ROOT / "docs/reading_routes.json").read_bytes())["semantic_probes"]
        return statement_targets(rows, probes)

    targets = selection()
    modules = sorted({target.split("/")[0] for target in targets})
    subprocess.run(["lake", "build", *modules], cwd=root / "lean", check=True)
    raw = subprocess.check_output(["lake", "env", "lean", "--run", str(program), *targets], cwd=root / "lean")
    rows = json.loads(raw)
    if (set(rows) != set(targets) or selection() != targets or inspector != program.read_bytes()
            or source_hashes(root) != before or source_hashes(ROOT) != before):
        raise ValueError("statement inspection incomplete or inputs changed during recording")
    payload = {"source_snapshot_sha256": canonical_sha256(before),
               "inspector_sha256": hashlib.sha256(inspector).hexdigest(),
               "toolchain": (root / "lean/lean-toolchain").read_text().strip(), "declarations": rows}
    path = ROOT / "corpus/reading_statement_evidence.json"
    if compare:
        if json.loads(path.read_bytes()) != payload:
            raise ValueError("independent statement inspection differs from the saved observations")
    else:
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as tmp:
            json.dump(payload, tmp, ensure_ascii=False, indent=2, sort_keys=True)
            tmp.write("\n")
        recorded = Path(tmp.name)
        recorded.chmod(0o644)
        recorded.replace(path)
    print(f"{'Reproduced' if compare else 'Recorded'} types and axioms for {len(rows)} declarations")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=ROOT,
                        help="checkout with the same Lean sources and its own Lake cache")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--statements", action="store_true", help="inspect types and axioms for reviewed links and semantic examples")
    modes.add_argument("--applications", action="store_true",
                        help="inspect formal arguments for the reader's selected caller/callee pairs")
    parser.add_argument("--compare", action="store_true", help="repeat the selected native inspection and compare without writing")
    args = parser.parse_args()
    if args.compare and not (args.applications or args.statements):
        parser.error("--compare requires --applications or --statements")
    root = args.checkout.resolve()
    before = source_hashes(root)
    if before != source_hashes(ROOT):
        parser.error("build checkout differs from edition's Lean sources")
    if args.statements:
        return record_statements(root, before, args.compare)
    program = ROOT / "tools/ReadApplications.lean" if args.applications else INSPECTOR
    inspector = program.read_bytes()
    pairs = []
    if args.applications:
        selection = ROOT / "docs/reading_applications.json"
        config = json.loads(selection.read_text())
        pairs = application_pairs(config)
    subprocess.run(["lake", "build", "QuarticQuery"], cwd=root / "lean", check=True)
    raw = subprocess.check_output(["lake", "env", "lean", "--run", str(program), *pairs], cwd=root / "lean")
    inspection = json.loads(raw)
    nodes = inspection["callers"] if args.applications else inspection["nodes"]
    if not nodes or source_hashes(root) != before or source_hashes(ROOT) != before or inspector != program.read_bytes():
        parser.error("empty inspection or inputs changed during recording")
    provenance = {"source_snapshot_sha256": canonical_sha256(before),
                  "inspector_sha256": hashlib.sha256(inspector).hexdigest(),
                  "toolchain": (root / "lean/lean-toolchain").read_text().strip()}
    if args.applications:
        if {caller + "=" + row["callee"] for caller, rows in nodes.items() for row in rows} != set(pairs):
            parser.error("compiled applications differ from requested pairs")
        graph = json.loads((ROOT / "corpus/reading_dependencies.json").read_text())
        sites = {}
        for module in config["occurrence_modules"]:
            chosen = [pair for pair in pairs if graph["nodes"][pair.split("=")[0]]["module"] == module]
            if not chosen:
                parser.error(f"no application pairs selected in {module}")
            path = module.replace(".", "/") + ".lean"
            result = subprocess.check_output(["lake", "env", "lean", "--run", str(program),
                                              "--source", module, path, *chosen], cwd=root / "lean")
            sites[module] = source_records(json.loads(result), (root / "lean" / path).read_bytes())
        if source_hashes(root) != before or source_hashes(ROOT) != before or program.read_bytes() != inspector:
            parser.error("inspection inputs changed while locating occurrences")
        latest = json.loads(selection.read_text())
        if pairs != application_pairs(latest) or latest["occurrence_modules"] != config["occurrence_modules"]:
            parser.error("application selection changed during inspection")
        payload = {**provenance, "schema": "quartic-lean-applications-v2", **inspection, "source_occurrences": sites}
        destination = ROOT / "corpus/reading_applications.json"
        if args.compare:
            if json.loads(destination.read_text()) != payload:
                parser.error("independent application extraction differs from the recorded inspection")
            print("Independent Lean application extraction matched the recorded inspection")
            return
        with tempfile.NamedTemporaryFile(mode="w", dir=destination.parent, delete=False) as tmp:
            json.dump(payload, tmp, sort_keys=True, ensure_ascii=False, indent=2)
            tmp.write("\n")
        recorded = Path(tmp.name)
        recorded.chmod(0o644)
        recorded.replace(destination)
        print(f"Recorded {len(pairs)} selected declaration pairs")
        return
    write_graph({**provenance, "schema": "quartic-reading-dependencies-v1",
                 "module": "QuarticQuery", **inspection}, OUTPUT)
    print(f"Recorded {len(nodes)} declarations in {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
