#!/usr/bin/env python3
"""Check maintained Git candidates without traversing ignored Lake/build trees."""

import argparse
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT_FILES = {"README.md", "LICENSE", ".gitignore", "Makefile", "AGENTS.md"}
REQUIRED = {"README.md", "LICENSE", ".gitignore", "Makefile",
            "tools/check_repository.py", "tests/test_repository.py",
            "research/requests/common.md", "research/requests/boundaries.md",
            "research/requests/1_understand_the_paper.md",
            "research/requests/2_ground_in_literature.md",
            "research/requests/3_lean_and_comparator.md"}
EVIDENCE_SUFFIXES = {".md", ".json", ".txt", ".bib", ".csv", ".yaml", ".yml", ".toml"}
CACHE_PARTS = {".lake", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}
OUTPUT_SUFFIXES = {".zip", ".olean", ".ilean", ".pyc", ".o", ".so", ".dylib"}
LINK = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.decode(errors="replace").strip() or "Git failed")
    return result.stdout


class GitView:
    """A working tree or index; index reads never consult unstaged file contents."""

    def __init__(self, root, index=False):
        self.root = Path(root).resolve()
        self.index = index
        self.paths = set()
        self.modes = {}
        self.conflicts = set()
        # --stage includes tracked ignored paths and excludes staged removals.
        for row in git(self.root, "ls-files", "--stage", "-z").split(b"\0"):
            if not row:
                continue
            info, name = row.split(b"\t", 1)
            mode, _oid, stage = info.split()
            path = name.decode("utf-8", errors="surrogateescape")
            self.paths.add(path)
            self.modes[path] = mode.decode()
            if stage != b"0":
                self.conflicts.add(path)
        if not index:
            for name in git(self.root, "ls-files", "--others", "--exclude-standard", "-z").split(b"\0"):
                if name:
                    self.paths.add(name.decode("utf-8", errors="surrogateescape"))
            # An unstaged deletion is absent from the working candidate tree.
            self.paths = {p for p in self.paths if (self.root / p).exists() or (self.root / p).is_symlink()}

    def regular(self, path):
        if self.index:
            return self.modes.get(path) in {"100644", "100755"}
        target = self.root / path
        parts = PurePosixPath(path).parts
        return target.is_file() and not any(self.root.joinpath(*parts[:n]).is_symlink() for n in range(1, len(parts) + 1))

    def read(self, path):
        if self.index:
            return git(self.root, "show", ":" + path).decode("utf-8")
        return (self.root / path).read_text(encoding="utf-8")


def placement(path):
    p = PurePosixPath(path)
    if any(part in CACHE_PARTS for part in p.parts) or p.parts[0] == "build":
        return "generated output/cache must stay untracked"
    if p.suffix.lower() in OUTPUT_SUFFIXES:
        return "generated output/cache must stay untracked"
    if len(p.parts) == 1:
        return None if path in ROOT_FILES else "root file has no declared role"
    owner = p.parts[0]
    if owner == "research":
        return None if p.suffix.lower() in EVIDENCE_SUFFIXES else "research contains evidence and advisory notes; executable code belongs in tools or lean"
    if owner == "docs":
        return None if p.suffix.lower() in EVIDENCE_SUFFIXES | {".png", ".svg", ".jpg", ".jpeg", ".webp"} else "docs contains documentation and supporting assets"
    if owner in {"tools", "tests"}:
        return None if p.suffix in {".py", ".md"} else f"{owner} contains Python maintenance code and its documentation"
    if owner == "lean":
        return None if p.suffix in {".lean", ".toml", ".json", ".md"} or p.name in {"lean-toolchain", "LICENSE"} else "lean contains the Lake package and Lean sources"
    if owner == ".github" and len(p.parts) == 3 and p.parts[1] == "workflows" and p.suffix in {".yml", ".yaml"}:
        return None
    return "path has no declared directory role"


def check(view):
    errors = [f"{p}: required maintained file is missing" for p in sorted(REQUIRED - view.paths)]
    for path in sorted(view.paths):
        if path in view.conflicts:
            errors.append(f"{path}: unresolved index conflict")
            continue
        if not view.regular(path):
            errors.append(f"{path}: maintained candidates must be regular files")
            continue
        issue = placement(path)
        if issue:
            errors.append(f"{path}: {issue}")
        if PurePosixPath(path).name != "README.md":
            continue
        try:
            content = view.read(path)
        except (UnicodeError, OSError, RuntimeError) as error:
            errors.append(f"{path}: cannot read README: {error}")
            continue
        for match in LINK.finditer(content):
            target = match.group(1).strip("<>")
            try:
                url = urlsplit(target)
            except ValueError:
                errors.append(f"{path}: malformed link: {target}")
                continue
            if url.scheme or url.netloc or not url.path:
                continue
            decoded = unquote(url.path)
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), decoded))
            if decoded.startswith("/") or resolved == ".." or resolved.startswith("../"):
                errors.append(f"{path}: local link escapes repository: {target}")
            elif resolved != "." and resolved not in view.paths and not any(p.startswith(resolved.rstrip("/") + "/") for p in view.paths):
                errors.append(f"{path}: stale local link: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--index", action="store_true", help="check staged paths and staged README contents")
    args = parser.parse_args()
    try:
        errors = check(GitView(args.root, args.index))
    except (RuntimeError, OSError) as error:
        print(f"repository check: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository roles and README links pass" + (" (index)." if args.index else "."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
