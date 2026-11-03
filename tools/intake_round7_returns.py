#!/usr/bin/env python3
"""Preserve the round-seven critique returns without executing their code.

Round-seven returns are expert-emulation critiques and small checking scripts, so
their extracted members are committed for readers; the original archives and the
returns' own scripts stay local. The manifest binds every archive and member by
size and SHA-256.
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from intake_round3_returns import digest, unpack  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "research/returns/round7"
RETURNS = (
    ("quantum_specialists", "quartic_r7_quantum_specialists_return.zip"),
    ("newcomer_readers", "quartic_r7_newcomer_readers_return.zip"),
    ("lower_bound_specialists", "quartic_r7_lower_bound_specialists_return.zip"),
    ("editors_and_funnel", "quartic_r7_editors_and_funnel_return.zip"),
)


def main(source_dir):
    if DEST.exists():
        raise SystemExit(f"Refusing to overwrite {DEST}")
    DEST.mkdir(parents=True)
    with tempfile.TemporaryDirectory(prefix="round7-intake-", dir=DEST) as temporary:
        stage = Path(temporary)
        records = []
        for ident, archive_name in RETURNS:
            archive_data = (source_dir / archive_name).read_bytes()
            archive_copy = stage / "archives" / archive_name
            archive_copy.parent.mkdir(exist_ok=True)
            archive_copy.write_bytes(archive_data)
            members = unpack(archive_copy, stage / "members" / ident)
            records.append({"id": ident, "archive": {"source": archive_name,
                "preserved": f"archives/{archive_name}", **digest(archive_data)},
                "members_root": f"members/{ident}", "members": members})
        for name in ("archives", "members"):
            (stage / name).rename(DEST / name)
        (DEST / "intake.json").write_text(json.dumps({"returns": records}, indent=2) + "\n")
    print(f"Preserved {len(records)} archives at {DEST}")


def verify():
    """Verify members, and local originals where present, against their hashes."""
    manifest = json.loads((DEST / "intake.json").read_text())
    archives_verified = 0
    for record in manifest["returns"]:
        archive = record["archive"]
        archive_path = DEST / archive["preserved"]
        if archive_path.exists():
            if digest(archive_path.read_bytes()) != {k: archive[k] for k in ("bytes", "sha256")}:
                raise ValueError(f"archive mismatch: {archive_path}")
            with tempfile.TemporaryDirectory(prefix="round7-verify-") as temporary:
                if unpack(archive_path, Path(temporary)) != record["members"]:
                    raise ValueError(f"archive members mismatch: {archive_path}")
            archives_verified += 1
        member_root = DEST / record["members_root"]
        for entry in record["members"]:
            path = member_root / entry["path"]
            if not path.exists():
                raise ValueError(f"local custody member missing: {path}; restore ignored members to verify intake")
            if path.is_symlink() or digest(path.read_bytes()) != {k: entry[k] for k in ("bytes", "sha256")}:
                raise ValueError(f"snapshot bytes mismatch: {path}")
    print(f"Verified all members of {len(manifest['returns'])} returns; "
          f"verified {archives_verified} local original archives")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="verify all locally preserved members (including ignored scripts); archives checked if present")
    parser.add_argument("--source-dir", type=Path, help="directory containing the four original ZIPs")
    args = parser.parse_args()
    if args.verify:
        try:
            verify()
        except (OSError, ValueError) as error:
            parser.exit(1, f"FAIL: {error}\n")
    elif args.source_dir is None:
        parser.error("--source-dir is required for intake")
    else:
        main(args.source_dir)
