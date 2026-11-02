"""Reproduce Reach.lean's private-name filtering defect on a synthetic graph.

This models the actual name-prefix decisions, not Lean elaboration. The sibling
Lean fixture must separately be compiled and loaded by the real extractor.
"""
import json
from pathlib import Path

root = "QuarticQuery.ReachRegression.publicRoot"
wrapper = "_private.ReachPrivateFixture.0.QuarticQuery.ReachRegression.privateWrapper"
leaf = "QuarticQuery.ReachRegression.publicLeaf"
graph = {root: [wrapper], wrapper: [leaf], leaf: []}


def project_name(name):
    return name.split(".")[0] == "QuarticQuery"


def old_dependencies(name):
    seen, out, todo = set(), [], list(graph[name])
    while todo:
        current = todo.pop()
        if current in seen:
            continue
        seen.add(current)
        # The real second branch also requires this prefix. Even if isInternal
        # is true for wrapper, that prefix is false, so nothing is traversed.
        if project_name(current):
            out.append(current)
    return out


def closure(edges):
    seen, todo = set(), [root]
    while todo:
        current = todo.pop()
        if current in seen:
            continue
        seen.add(current)
        todo.extend(edges(current))
    return seen


old = closure(old_dependencies)
complete = closure(lambda name: graph[name])
display = {name for name in complete if project_name(name)}
assert old == {root}
assert display == {root, leaf}
assert wrapper in complete and not project_name(wrapper)
report = {
    "status": "passed",
    "kind": "synthetic algorithmic regression; no Lean run",
    "graph": graph,
    "old_public_closure": sorted(old),
    "complete_raw_closure": sorted(complete),
    "filter_after_closure": sorted(display),
    "all_assertions_passed": True,
}
Path(__file__).with_name("reach_private_output.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
