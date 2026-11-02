#!/usr/bin/env python3
"""Audit completed research ZIPs against their manifests without extracting them."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile
import zlib


RESERVED = {"READ_ME_FIRST.md", "manifest.json"}


def check_name(name):
    if (not name or "\\" in name or ":" in name or "\0" in name
            or any(part in {"", ".", ".."} for part in name.split("/"))):
        raise ValueError(f"invalid archive member path: {name!r}")


def audit(path):
    """Return manifest identity and payload count; raise on any integrity failure.

    Source labels are historical provenance, not paths to resolve on this machine.
    The request and manifest are readable ZIP entries but are not manifest-hashed.
    """
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            if info.compress_type not in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}:
                raise ValueError(f"{info.filename}: unsupported compression; expected stored or deflated")
        names = archive.namelist()
        for name in names:
            check_name(name)
        duplicates = [name for name, count in Counter(n.casefold() for n in names).items()
                      if count > 1]
        if duplicates:
            raise ValueError(f"duplicate or case-colliding members: {duplicates}")
        missing = RESERVED - set(names)
        if missing:
            raise ValueError(f"missing required members: {sorted(missing)}")
        request = archive.read("READ_ME_FIRST.md").decode("utf-8")
        if not request.strip():
            raise ValueError("READ_ME_FIRST.md is empty")
        manifest = json.loads(archive.read("manifest.json"))
        if not isinstance(manifest, dict):
            raise ValueError("manifest must be an object")
        for field in ("packet", "source_paper"):
            if not isinstance(manifest.get(field), str) or not manifest[field].strip():
                raise ValueError(f"manifest needs a nonempty {field}")
        rows = manifest.get("members")
        if not isinstance(rows, list) or not rows:
            raise ValueError("manifest members must be a nonempty list")
        declared = set()
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("member"), str):
                raise ValueError("each manifest row needs a member name")
            name = row["member"]
            check_name(name)
            if name in declared or name in RESERVED:
                raise ValueError(f"duplicate or reserved manifest member: {name}")
            declared.add(name)
            if not isinstance(row.get("source"), str) or not row["source"].strip():
                raise ValueError(f"{name}: missing source label")
            if type(row.get("bytes")) is not int or row["bytes"] < 0:
                raise ValueError(f"{name}: bytes must be a nonnegative integer")
            if not isinstance(row.get("sha256"), str) or not re.fullmatch(r"[0-9a-fA-F]{64}", row["sha256"]):
                raise ValueError(f"{name}: invalid SHA-256")
        payload = set(names) - RESERVED
        if declared != payload:
            raise ValueError(f"manifest coverage differs: missing from ZIP={sorted(declared - payload)}, "
                             f"unlisted in manifest={sorted(payload - declared)}")
        for row in rows:
            digest = hashlib.sha256()
            size = 0
            with archive.open(row["member"]) as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    size += len(chunk)
                    digest.update(chunk)
            if size != row["bytes"]:
                raise ValueError(f"{row['member']}: byte length mismatch")
            if digest.hexdigest() != row["sha256"].lower():
                raise ValueError(f"{row['member']}: SHA-256 mismatch")
        return manifest["packet"], len(rows)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path,
                        help="completed ZIPs or directories containing ZIPs (not recursive)")
    args = parser.parse_args(argv)
    paths = set()
    failed = False
    for path in args.paths:
        try:
            if path.is_dir():
                batch = [p for p in path.iterdir() if p.is_file() and p.suffix.lower() == ".zip"]
                if not batch:
                    raise ValueError("no ZIPs found")
                paths.update(p.resolve() for p in batch)
            else:
                paths.add(path.resolve())
        except (OSError, ValueError, RuntimeError) as error:
            print(f"FAIL {path}: {error}", file=sys.stderr)
            failed = True
    for path in sorted(paths):
        try:
            packet, count = audit(path)
        except (OSError, ValueError, RuntimeError, zipfile.BadZipFile, EOFError, zlib.error) as error:
            print(f"FAIL {path}: {error}", file=sys.stderr)
            failed = True
        else:
            print(f"PASS {path.name}: {packet}; {count} payload members")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
