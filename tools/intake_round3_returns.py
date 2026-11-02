#!/usr/bin/env python3
"""Preserve the specified round-three submissions without executing their code."""

import argparse
import hashlib
import json
import stat
import tempfile
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "research/returns/round3"
DOWNLOADS = Path.home() / "Downloads"
ATTACHMENTS = Path.home() / ".codex/attachments"
NAMES = (
    "models_evidence", "forrelation_promise_circuit", "forrelation_lower_bound",
    "addressed_construction", "quantum_upper", "direct_product",
    "planted_lower_bound", "reviewed", "evidence_backend", "baseline_review",
)
ATTACHMENT_IDS = (
    "d1e4fb2f-8565-4a53-8435-cbaa71a6f5ac", "f58b029b-1d73-4815-9080-1599ea40004b",
    "2cf251ce-014e-4413-ae2d-d8143cce0a18", "66642f7e-72ae-4eba-831a-4aeaa9b91384",
    "d6b9fe15-bc3d-4385-895d-c518f21d8e47", "410616a8-34ae-4d2a-bffb-eff71845b198",
    "87cc85f2-1def-4ee7-b20d-f5278d3d6c6f", "416a3915-453d-494b-bb13-984d7fd7c32a",
    "a85dc496-51b6-48c4-b701-040fc75775bd",
)


def digest(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def unpack(archive, target):
    """Reject traversal, links and collisions before writing any archive member."""
    with ZipFile(archive) as source:
        infos = source.infolist()
        seen = set()
        total = 0
        for info in infos:
            name = info.filename
            path = PurePosixPath(name)
            mode = info.external_attr >> 16
            if (not name or "\\" in name or name.startswith("/") or
                any(part in ("", ".", "..") for part in name.rstrip("/").split("/")) or
                path.is_absolute() or stat.S_ISLNK(mode) or
                (stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR))):
                raise ValueError(f"unsafe archive member: {name!r}")
            key = name.rstrip("/").casefold()
            if key in seen:
                raise ValueError(f"duplicate archive member: {name!r}")
            seen.add(key)
            total += info.file_size
            if total > 500_000_000:
                raise ValueError("archive exceeds extraction limit")
        result = []
        for info in infos:
            if info.is_dir():
                continue
            data = source.read(info)
            out = target.joinpath(*PurePosixPath(info.filename).parts)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(data)
            result.append({"path": info.filename, **digest(data)})
        return result


def main(session_packet):
    if DEST.exists():
        raise SystemExit(f"Refusing to overwrite {DEST}")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="round3-intake-", dir=DEST.parent) as temporary:
        stage = Path(temporary) / "round3"
        stage.mkdir()
        records = []
        for index, name in enumerate(NAMES, 1):
            ident = f"{index:02d}_{name}"
            archive_name = f"quartic_r3_{ident}_return.zip"
            archive_data = (DOWNLOADS / archive_name).read_bytes()
            archive_copy = stage / "archives" / archive_name
            archive_copy.parent.mkdir(exist_ok=True)
            archive_copy.write_bytes(archive_data)
            members = unpack(archive_copy, stage / "members" / ident)
            records.append({"id": ident, "archive": {"source": archive_name,
                "preserved": f"archives/{archive_name}", **digest(archive_data)},
                "members_root": f"members/{ident}", "members": members})
        attachments = []
        sources = [(ATTACHMENTS / source / "Pasted text.txt", source) for source in ATTACHMENT_IDS]
        sources.append((session_packet, None))
        for index, (source_path, attachment_id) in enumerate(sources, 1):
            attachment_data = source_path.read_bytes()
            attachment_path = f"attachments/input_{index:02d}.txt"
            attachment_copy = stage / attachment_path
            attachment_copy.parent.mkdir(exist_ok=True)
            attachment_copy.write_bytes(attachment_data)
            entry = {"preserved": attachment_path, **digest(attachment_data)}
            if index == 10:
                entry.update({"local_only": True, "role": "session_packet"})
            else:
                entry["source"] = attachment_id
            attachments.append(entry)
        (stage / "intake.json").write_text(json.dumps({"returns": records, "attachments": attachments}, indent=2) + "\n")
        stage.rename(DEST)
    print(f"Preserved {len(records)} archives and attachments at {DEST}")


def verify():
    """Verify preserved originals and members against their recorded hashes."""
    manifest = json.loads((DEST / "intake.json").read_text())
    for record in manifest["returns"]:
        archive = record["archive"]
        archive_path = DEST / archive["preserved"]
        if digest(archive_path.read_bytes()) != {k: archive[k] for k in ("bytes", "sha256")}:
            raise ValueError(f"archive mismatch: {archive_path}")
        with tempfile.TemporaryDirectory(prefix="round3-verify-") as temporary:
            extracted = unpack(archive_path, Path(temporary))
            if extracted != record["members"]:
                raise ValueError(f"archive members mismatch: {archive_path}")
        member_root = DEST / record["members_root"]
        actual = {p.relative_to(member_root).as_posix() for p in member_root.rglob("*") if p.is_file()}
        expected = {entry["path"] for entry in record["members"]}
        if actual != expected:
            raise ValueError(f"snapshot paths mismatch: {member_root}")
        for entry in record["members"]:
            path = member_root / entry["path"]
            if path.is_symlink() or digest(path.read_bytes()) != {k: entry[k] for k in ("bytes", "sha256")}:
                raise ValueError(f"snapshot bytes mismatch: {path}")
    for entry in manifest["attachments"]:
        path = DEST / entry["preserved"]
        if digest(path.read_bytes()) != {k: entry[k] for k in ("bytes", "sha256")}:
            raise ValueError(f"attachment mismatch: {path}")
    print(f"Verified {len(manifest['returns'])} archives and {len(manifest['attachments'])} attachments")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="verify an existing intake")
    parser.add_argument("--session-packet", type=Path,
                        help="local path to the tenth, private input (required for intake)")
    args = parser.parse_args()
    if args.verify:
        verify()
    elif args.session_packet is None:
        parser.error("--session-packet is required for intake")
    else:
        main(args.session_packet)
