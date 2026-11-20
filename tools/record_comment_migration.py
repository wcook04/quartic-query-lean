#!/usr/bin/env python3
"""Record, or check, that local Lean sources changed in comments only.

A statement review binds the complete local source snapshot, so any byte change
in `lean/` makes it stale. When an edit touches comments alone, this program
compares the sources at a committed revision with the working tree and writes a
`lean_comment_only_migration` receipt when, for every file in the snapshot:

- the set of paths is unchanged;
- each non-Lean input (toolchain, lakefile, manifest, Comparator JSON) is
  byte-identical;
- each Lean file is byte-identical after `lean_comments.strip_comments`
  replaces every comment by one space and keeps its line breaks, so every line
  of code keeps its line number and every token boundary is kept;
- no changed file uses `#guard_msgs`, whose expected output is a doc comment.

The corpus then treats a review bound to the earlier snapshot as current for
the later one, through a single receipt whose maps match their digests and whose
later map is exactly the current one; it never chains receipts. Documentation
comments are part of a module's syntax and its stored docstrings; a review binds
a declaration's statement and proof, which they do not change. Build and Comparator receipts are never migrated: they need a
fresh run on the new bytes.

    python3 tools/record_comment_migration.py --from <commit>
    python3 tools/record_comment_migration.py --check
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from build_corpus import ROOT, canonical_sha256, source_hashes
from lean_comments import strip_comments

RECEIPTS = ROOT / "corpus" / "migrations"
KIND = "lean_comment_only_migration"


def blob(commit, path):
    return subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:{path}"],
                          check=True, capture_output=True).stdout


def sha(data):
    return hashlib.sha256(data).hexdigest()


def compare(commit, old_hashes, new_hashes, read_new):
    """Return the changed Lean paths, or raise if any change is not comment-only."""
    if set(old_hashes) != set(new_hashes):
        raise ValueError(f"source paths differ: {sorted(set(old_hashes) ^ set(new_hashes))}")
    changed = {}
    for path in sorted(old_hashes):
        if old_hashes[path] == new_hashes[path]:
            continue
        if not path.endswith(".lean"):
            raise ValueError(f"{path}: a non-Lean input changed")
        old, new = blob(commit, path), read_new(path)
        if sha(old) != old_hashes[path] or sha(new) != new_hashes[path]:
            raise ValueError(f"{path}: bytes do not match the recorded hashes")
        old_text, new_text = old.decode("utf-8"), new.decode("utf-8")
        if "#guard_msgs" in old_text or "#guard_msgs" in new_text:
            raise ValueError(f"{path}: uses #guard_msgs, whose expected output is a comment")
        old_code, new_code = strip_comments(old_text), strip_comments(new_text)
        if old_code != new_code:
            raise ValueError(f"{path}: code outside comments changed")
        changed[path] = {"from": old_hashes[path], "to": new_hashes[path],
                         "code_sha256": sha(new_code.encode("utf-8"))}
    return changed


def old_source_hashes(commit):
    listing = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", commit, "lean"],
                             check=True, capture_output=True, text=True).stdout.split()
    current = source_hashes(ROOT)
    keep = [p for p in listing if p in current or p.endswith((".lean", "lean-toolchain", "lakefile.toml",
                                                               "lake-manifest.json"))
            or (p.endswith(".json") and "/QuarticCorpus/" in p)]
    return {p: sha(blob(commit, p)) for p in sorted(keep) if "/." not in p}


def record(commit):
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", commit], check=True,
                            capture_output=True, text=True).stdout.strip()
    old, new = old_source_hashes(commit), source_hashes(ROOT)
    changed = compare(commit, old, new, lambda p: (ROOT / p).read_bytes())
    if not changed:
        print("no Lean source changed; nothing recorded")
        return 0
    ran_at = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    receipt = {
        "kind": KIND, "status": "passed", "from_commit": commit,
        "tool": "tools/record_comment_migration.py: comment-stripped Lean and all other inputs identical",
        "from_snapshot_sha256": canonical_sha256(old), "to_snapshot_sha256": canonical_sha256(new),
        "from_source_hashes": old, "to_source_hashes": new, "changed": changed, "ran_at": ran_at,
    }
    path = RECEIPTS / f"comment-migration-{ran_at.replace(':', '').replace('.', '')}.json"
    path.write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(f"{path.relative_to(ROOT)}: {len(changed)} Lean files changed in comments only")
    return 0


def check():
    """Validate every receipt; recompare the one whose later map is the current source."""
    current = source_hashes(ROOT)
    failures = 0
    for path in sorted(RECEIPTS.glob("comment-migration-*.json")):
        receipt = json.loads(path.read_text(encoding="utf-8"))
        try:
            if (receipt.get("kind") != KIND
                    or canonical_sha256(receipt["from_source_hashes"]) != receipt["from_snapshot_sha256"]
                    or canonical_sha256(receipt["to_source_hashes"]) != receipt["to_snapshot_sha256"]):
                raise ValueError("snapshot digests do not match their maps")
            if receipt["to_source_hashes"] != current:
                if receipt["to_snapshot_sha256"] == canonical_sha256(current):
                    raise ValueError("claims the current snapshot with a different map")
                continue
            changed = compare(receipt["from_commit"], receipt["from_source_hashes"], current,
                              lambda p: (ROOT / p).read_bytes())
            if changed != receipt["changed"]:
                raise ValueError("recorded changes do not match a fresh comparison")
        except (KeyError, ValueError, subprocess.CalledProcessError) as error:
            print(f"{path.relative_to(ROOT)}: {error}", file=sys.stderr)
            failures += 1
    if not failures:
        print("comment-only migrations verified")
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--from", dest="commit")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    return check() if args.check or not args.commit else record(args.commit)


if __name__ == "__main__":
    raise SystemExit(main())
