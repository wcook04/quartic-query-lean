#!/usr/bin/env python3
"""Check maintained Git candidates without traversing ignored Lake/build trees."""

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from zipfile import BadZipFile, ZipFile
import zlib


ROOT_FILES = {"README.md", "CONTRIBUTING.md", "LICENSE", ".gitignore", "Makefile", "AGENTS.md", "CLAUDE.md"}
REQUIRED = {"README.md", "CONTRIBUTING.md", "LICENSE", ".gitignore", "Makefile",
            "tools/check_repository.py", "tests/test_check_repository.py",
            "research/requests/review/common.md", "research/requests/review/boundaries.md",
            "research/requests/review/1_understand_the_paper.md",
            "research/requests/review/2_ground_in_literature.md",
            "research/requests/review/3_lean_and_comparator.md"}
REQUIRED |= {
    "docs/README.md", "lean/README.md", "tests/README.md", "research/requests/README.md",
    "research/returns/round2/README.md", "research/returns/round2/intake.json",
    "research/returns/round3/README.md", "research/returns/round3/intake.json",
    "research/adjudication/adjudication.json", "research/adjudication/adjudication_notes.md",
    *{f"research/requests/funnel/{name}.md" for name in (
        "common", "boundaries", "1_long_reasoning_record", "2_short_expert_paper",
        "3_examples_first_exposition", "4_forrelation_route_note", "5_reader_and_film")},
}
RETIRED = {
    "research/returns/adjudication.json", "research/returns/adjudication_notes.md",
    *{f"research/requests/{name}.md" for name in (
        "common", "boundaries", "1_understand_the_paper", "2_ground_in_literature",
        "3_lean_and_comparator")},
}
EVIDENCE_SUFFIXES = {".md", ".json", ".jsonl", ".txt", ".bib", ".csv", ".yaml", ".yml", ".toml"}
CACHE_PARTS = {".lake", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}
OUTPUT_SUFFIXES = {".zip", ".olean", ".ilean", ".pyc", ".o", ".so", ".dylib"}
LINK = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
SNAPSHOT_ROOT = "research/returns/round2"
SNAPSHOT_MANIFEST = f"{SNAPSHOT_ROOT}/intake.json"
SNAPSHOT_IDS = {
    "1_statement_fidelity", "2_lean_construction", "3_lean_quantum_upper",
    "4_lean_classical_lower", "5_lean_appendix_a", "6_sharp_uniform_forrelation",
    "7_single_family_exponent",
}
ROUND3_ROOT = "research/returns/round3"
ROUND3_MANIFEST = f"{ROUND3_ROOT}/intake.json"
ROUND3_IDS = {
    "01_models_evidence", "02_forrelation_promise_circuit", "03_forrelation_lower_bound",
    "04_addressed_construction", "05_quantum_upper", "06_direct_product",
    "07_planted_lower_bound", "08_reviewed", "09_evidence_backend", "10_baseline_review",
}
# These submitted bytes are preserved locally, not published source candidates.
ROUND3_LOCAL_MEMBERS = {
    "members/02_forrelation_promise_circuit/quartic_r3_02_forrelation_promise_circuit_return/section.pdf",
}
ROUND3_PRIVATE_ATTACHMENT = "attachments/input_10.txt"
SHA256 = re.compile(r"[0-9a-f]{64}\Z")


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

    def read_bytes(self, path):
        if self.index:
            return git(self.root, "show", ":" + path)
        return (self.root / path).read_bytes()

    def read(self, path):
        return self.read_bytes(path).decode("utf-8")


def unique_object(pairs):
    """Reject ambiguous JSON rather than silently accepting a duplicate key."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def snapshot_manifest(view):
    """Read the bounded intake manifest in the same Git view as its members."""
    if SNAPSHOT_MANIFEST not in view.paths or not view.regular(SNAPSHOT_MANIFEST):
        # The ordinary required-file/regular-file checks report these cases.
        return None, []
    if SNAPSHOT_MANIFEST in view.conflicts:
        return None, []
    try:
        manifest = json.loads(view.read(SNAPSHOT_MANIFEST), object_pairs_hook=unique_object)
    except (UnicodeError, OSError, RuntimeError, ValueError) as error:
        return None, [f"{SNAPSHOT_MANIFEST}: cannot read intake manifest: {error}"]

    errors = []
    if not isinstance(manifest, dict) or set(manifest) != {"format", "snapshots"}:
        return None, [f"{SNAPSHOT_MANIFEST}: expected format and snapshots"]
    if manifest["format"] != "return-snapshots-v1":
        errors.append(f"{SNAPSHOT_MANIFEST}: unsupported format")
    snapshots = manifest["snapshots"]
    if not isinstance(snapshots, dict):
        return None, errors + [f"{SNAPSHOT_MANIFEST}: snapshots must be an object"]
    if set(snapshots) != SNAPSHOT_IDS:
        errors.append(f"{SNAPSHOT_MANIFEST}: snapshot IDs must match the seven round-two returns")

    for name, snapshot in snapshots.items():
        label = f"{SNAPSHOT_MANIFEST}: {name}"
        if name not in SNAPSHOT_IDS:
            continue
        if not isinstance(snapshot, dict) or set(snapshot) != {"archive", "members"}:
            errors.append(f"{label}: expected archive and members")
            continue
        archive = snapshot["archive"]
        if (not isinstance(archive, dict) or set(archive) != {"name", "sha256"}
                or archive["name"] != f"quartic_r2_{name}_return.zip"
                or not isinstance(archive["sha256"], str)
                or not SHA256.fullmatch(archive["sha256"])):
            errors.append(f"{label}: invalid archive name or SHA-256")
        members = snapshot["members"]
        if not isinstance(members, dict) or not members:
            errors.append(f"{label}: members must be a nonempty object")
            continue
        for member, record in members.items():
            member_path = PurePosixPath(member)
            if (not member or not member_path.parts or member_path.is_absolute() or member_path.as_posix() != member
                    or any(part in {".", ".."} for part in member_path.parts)
                    or "\\" in member or "\0" in member):
                errors.append(f"{label}: invalid member path: {member!r}")
            if (not isinstance(record, dict) or set(record) != {"size", "sha256"}
                    or type(record["size"]) is not int or record["size"] < 0
                    or not isinstance(record["sha256"], str)
                    or not SHA256.fullmatch(record["sha256"])):
                errors.append(f"{label}: invalid member record: {member!r}")
    return (None if errors else manifest), errors


def snapshot_members(manifest):
    return {
        f"{SNAPSHOT_ROOT}/{name}/{member}": record
        for name, snapshot in manifest["snapshots"].items()
        for member, record in snapshot["members"].items()
    }


def safe_member_path(value):
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value:
        return False
    path = PurePosixPath(value)
    return (bool(path.parts) and not path.is_absolute() and path.as_posix() == value
            and all(part not in {".", ".."} for part in path.parts))


def byte_record(record):
    return (type(record.get("bytes")) is int and record["bytes"] >= 0
            and isinstance(record.get("sha256"), str)
            and SHA256.fullmatch(record["sha256"]) is not None)


def round3_manifest(view):
    """Return admitted public members, local-only paths and schema errors.

    Read the manifest and source bytes only through the selected Git view. Sender
    programs are opaque source evidence: this checker never imports or runs them.
    Local ZIPs, the submitted PDF and the private session packet are not required
    in either Git view, and are rejected if added to it.
    """
    if (ROUND3_MANIFEST not in view.paths or not view.regular(ROUND3_MANIFEST)
            or ROUND3_MANIFEST in view.conflicts):
        return None, set(), []
    try:
        manifest = json.loads(view.read(ROUND3_MANIFEST), object_pairs_hook=unique_object)
    except (UnicodeError, OSError, RuntimeError, ValueError) as error:
        return None, set(), [f"{ROUND3_MANIFEST}: cannot read intake manifest: {error}"]
    if not isinstance(manifest, dict) or set(manifest) != {"returns", "attachments"}:
        return None, set(), [f"{ROUND3_MANIFEST}: expected returns and attachments"]
    errors, members = [], {}
    local = {f"{ROUND3_ROOT}/{p}" for p in ROUND3_LOCAL_MEMBERS | {ROUND3_PRIVATE_ATTACHMENT}}

    def error(message):
        errors.append(f"{ROUND3_MANIFEST}: {message}")

    def admit(path, record):
        full = f"{ROUND3_ROOT}/{path}"
        if full in members:
            error(f"duplicate preserved path: {path!r}")
        elif full not in local:
            members[full] = {"size": record["bytes"], "sha256": record["sha256"]}

    returns = manifest["returns"]
    seen_ids = set()
    if not isinstance(returns, list):
        error("returns must be a list")
        returns = []
    for row in returns:
        if not isinstance(row, dict) or set(row) != {"id", "archive", "members_root", "members"}:
            error("invalid return record")
            continue
        name = row["id"]
        if not isinstance(name, str) or name not in ROUND3_IDS:
            error(f"invalid return ID: {name!r}")
            continue
        if name in seen_ids:
            error(f"duplicate return ID: {name}")
        seen_ids.add(name)
        root = f"members/{name}"
        if row["members_root"] != root:
            error(f"{name}: members_root must be {root!r}")
        archive = row["archive"]
        archive_name = f"quartic_r3_{name}_return.zip"
        if (not isinstance(archive, dict)
                or set(archive) != {"source", "preserved", "bytes", "sha256"}
                or archive["source"] != archive_name
                or archive["preserved"] != f"archives/{archive_name}" or not byte_record(archive)):
            error(f"{name}: invalid archive record")
        local.add(f"{ROUND3_ROOT}/archives/{archive_name}")
        records = row["members"]
        if not isinstance(records, list) or not records:
            error(f"{name}: members must be a nonempty list")
            continue
        seen_paths = set()
        for record in records:
            if (not isinstance(record, dict) or set(record) != {"path", "bytes", "sha256"}
                    or not byte_record(record)):
                error(f"{name}: invalid member record")
                continue
            path = record["path"]
            if not safe_member_path(path):
                error(f"{name}: invalid member path: {path!r}")
                continue
            if path in seen_paths:
                error(f"{name}: duplicate member path: {path!r}")
            seen_paths.add(path)
            admit(f"{root}/{path}", record)
    if seen_ids != ROUND3_IDS:
        error("return IDs must match the ten round-three returns")
    attachments = manifest["attachments"]
    seen_attachments = set()
    expected = {f"attachments/input_{i:02d}.txt" for i in range(1, 11)}
    if not isinstance(attachments, list):
        error("attachments must be a list")
        attachments = []
    for record in attachments:
        if not isinstance(record, dict):
            error("invalid attachment record")
            continue
        path = record.get("preserved")
        private = path == ROUND3_PRIVATE_ATTACHMENT
        keys = {"preserved", "bytes", "sha256"} | ({"local_only", "role"} if private else {"source"})
        if (set(record) != keys or not byte_record(record)
                or not isinstance(path, str) or path not in expected
                or (private and (record["local_only"] is not True or record["role"] != "session_packet"))
                or (not private and (not isinstance(record["source"], str) or not record["source"]))):
            error("invalid attachment record")
            continue
        if path in seen_attachments:
            error(f"duplicate attachment path: {path!r}")
        seen_attachments.add(path)
        admit(path, record)
    if seen_attachments != expected:
        error("attachment paths must match the ten supplied inputs")
    return (None if errors else members), local, errors


def check_archives(manifest, archive_dir):
    """Optionally compare the manifest with the original, externally kept ZIPs."""
    errors = []
    for name, snapshot in sorted(manifest["snapshots"].items()):
        archive = snapshot["archive"]
        path = Path(archive_dir) / archive["name"]
        try:
            archive_bytes = path.read_bytes()
        except OSError as error:
            errors.append(f"{path}: cannot read original archive: {error}")
            continue
        if hashlib.sha256(archive_bytes).hexdigest() != archive["sha256"]:
            errors.append(f"{path}: archive SHA-256 differs from intake manifest")
        try:
            with ZipFile(io.BytesIO(archive_bytes)) as original:
                infos = [info for info in original.infolist() if not info.is_dir()]
                names = [info.filename for info in infos]
                if len(names) != len(set(names)):
                    errors.append(f"{path}: archive contains duplicate member paths")
                    continue
                missing = set(snapshot["members"]) - set(names)
                extra = set(names) - set(snapshot["members"])
                if missing or extra:
                    errors.append(f"{path}: archive member set differs (missing={sorted(missing)!r}, extra={sorted(extra)!r})")
                for info in infos:
                    if info.filename not in snapshot["members"]:
                        continue
                    content = original.read(info)
                    record = snapshot["members"][info.filename]
                    if (len(content) != record["size"]
                            or hashlib.sha256(content).hexdigest() != record["sha256"]):
                        errors.append(f"{path}: archive member differs from intake manifest: {info.filename}")
        except (BadZipFile, EOFError, OSError, RuntimeError, ValueError, zlib.error) as error:
            errors.append(f"{path}: cannot verify archive members: {error}")
    return errors


def placement(path, snapshot=False):
    if path in RETIRED:
        return "superseded source location; see research/README.md for the maintained owner"
    p = PurePosixPath(path)
    if any(part in CACHE_PARTS for part in p.parts) or p.parts[0] == "build":
        return "generated output/cache must stay untracked"
    if p.suffix.lower() in OUTPUT_SUFFIXES:
        return "generated output/cache must stay untracked"
    if snapshot:
        return None
    if len(p.parts) == 1:
        return None if path in ROOT_FILES else "root file has no declared role"
    owner = p.parts[0]
    if owner == "research":
        return None if p.suffix.lower() in EVIDENCE_SUFFIXES else "research contains evidence and advisory notes; executable code belongs in tools or lean"
    if owner == "corpus":
        return None if p.suffix.lower() in {".json", ".md"} else "corpus contains statement records and receipts"
    if owner == "docs":
        return None if p.suffix.lower() in EVIDENCE_SUFFIXES | {".png", ".svg", ".jpg", ".jpeg", ".webp", ".tex"} else "docs contains documentation, figure sources and supporting assets"
    if path in {"tools/ReadDependencies.lean", "tools/ReadApplications.lean", "tools/ReadStatementEvidence.lean", "tools/ReadUseRegions.lean",
                "tools/reader.mjs", "tools/query_reading_api.mjs"}:
        return None  # Compiled-environment inspector and static reading API client.
    if owner in {"tools", "tests"}:
        return None if p.suffix in {".py", ".md"} else f"{owner} contains Python maintenance code and its documentation"
    if owner == "lean":
        return None if p.suffix in {".lean", ".toml", ".json", ".md"} or p.name in {"lean-toolchain", "LICENSE"} else "lean contains the Lake package and Lean sources"
    if owner == "site":
        if len(p.parts) > 1 and p.parts[1] in {"dist", "public"}:
            return "generated output/cache must stay untracked"
        return None if p.suffix in {".ts", ".tsx", ".css", ".json", ".md", ".html", ".mjs", ".svg"} or p.name == ".gitignore" else "site contains the reading website's TypeScript, styles and build configuration"
    if owner == ".github" and len(p.parts) == 3 and p.parts[1] == "workflows" and p.suffix in {".yml", ".yaml"}:
        return None
    return "path has no declared directory role"


def check(view, archive_dir=None):
    errors = [f"{p}: required maintained file is missing" for p in sorted(REQUIRED - view.paths)]
    manifest, manifest_errors = snapshot_manifest(view)
    errors.extend(manifest_errors)
    members = snapshot_members(manifest) if manifest is not None else {}
    round3_members, round3_local, round3_errors = round3_manifest(view)
    errors.extend(round3_errors)
    if round3_members is not None:
        members.update(round3_members)
    for path in sorted(set(members) - view.paths):
        errors.append(f"{path}: submitted snapshot member is missing")
    for path in sorted(view.paths):
        if path in view.conflicts:
            errors.append(f"{path}: unresolved index conflict")
            continue
        if not view.regular(path):
            errors.append(f"{path}: maintained candidates must be regular files")
            continue
        in_round2 = path.startswith(SNAPSHOT_ROOT + "/") and path not in {
            SNAPSHOT_MANIFEST, f"{SNAPSHOT_ROOT}/README.md",
        }
        in_round3 = path.startswith(ROUND3_ROOT + "/") and path not in {
            ROUND3_MANIFEST, f"{ROUND3_ROOT}/README.md",
        }
        in_snapshot = in_round2 or in_round3
        if in_round3 and path in round3_local:
            errors.append(f"{path}: local-only submitted input must stay untracked")
            continue
        if (in_round2 and manifest is None) or (in_round3 and round3_members is None):
            # No snapshot is admitted until the manifest is readable and valid.
            continue
        if in_snapshot and path not in members:
            errors.append(f"{path}: unmanifested snapshot member")
            continue
        issue = placement(path, snapshot=in_snapshot)
        if issue:
            errors.append(f"{path}: {issue}")
        if in_snapshot:
            try:
                content = view.read_bytes(path)
            except (OSError, RuntimeError) as error:
                errors.append(f"{path}: cannot read snapshot member: {error}")
                continue
            record = members[path]
            if len(content) != record["size"] or hashlib.sha256(content).hexdigest() != record["sha256"]:
                errors.append(f"{path}: submitted snapshot bytes differ from intake manifest")
            # Submitted READMEs describe the sender's tree, not maintained navigation.
            continue
        if PurePosixPath(path).name not in {"README.md", "CONTRIBUTING.md", "AGENTS.md"}:
            continue
        try:
            content = view.read(path)
        except (UnicodeError, OSError, RuntimeError) as error:
            errors.append(f"{path}: cannot read navigation document: {error}")
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
    if archive_dir is not None and manifest is not None:
        errors.extend(check_archives(manifest, archive_dir))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--index", action="store_true", help="check staged paths and staged navigation contents")
    parser.add_argument("--archive-dir", type=Path, help="also verify the original round-two ZIPs in this external directory")
    args = parser.parse_args()
    try:
        errors = check(GitView(args.root, args.index), args.archive_dir)
    except (RuntimeError, OSError) as error:
        print(f"repository check: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository roles and navigation links pass" + (" (index)." if args.index else "."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
