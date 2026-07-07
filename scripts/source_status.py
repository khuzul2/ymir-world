#!/usr/bin/env python3
"""Track which raw Ymir sources have been processed into canon.

Every file under sources/raw/ is recorded in sources/manifest.tsv with a content
hash and a processing status. Because a hash is stored, a re-uploaded/edited file
is detected as CHANGED (not silently treated as already-done).

Manifest format: sources/manifest.tsv  (tab-separated; first line is the header)
  columns: status <TAB> source <TAB> sha12 <TAB> processed_into <TAB> notes
  status values:
    processed  - mined into canon / a digest
    pending    - present but NOT yet processed  (this is the work queue)
    stub       - looked at; empty or near-empty, nothing to extract

Usage:
  python3 scripts/source_status.py                 # scan & report NEW / CHANGED / PENDING
  python3 scripts/source_status.py init            # first-time: register all current files
  python3 scripts/source_status.py register        # add NEW files to the manifest as 'pending'
  python3 scripts/source_status.py mark <src> <status> [processed_into] [notes...]
                                                   # update one file's status
Exit code is non-zero when there is anything to do (NEW, CHANGED, or PENDING),
so it can gate the "start the manual" step in CI or a hook.
"""
import os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "sources", "raw")
MANIFEST = os.path.join(ROOT, "sources", "manifest.tsv")
HEADER = ["status", "source", "sha12", "processed_into", "notes"]
IGNORE = {".gitkeep", ".DS_Store"}


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def scan_raw():
    """Return {relpath: sha12} for every file under sources/raw/."""
    out = {}
    for dirpath, _, files in os.walk(RAW):
        for fn in files:
            if fn in IGNORE:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, RAW)
            out[rel] = sha12(full)
    return out


def guess_processed_into(rel, full):
    ext = os.path.splitext(rel)[1].lower()
    try:
        size = os.path.getsize(full)
    except OSError:
        size = 1
    if size <= 1:
        return "stub", "-", "empty file"
    if ext in (".doc", ".docx", ".pdf"):
        return "processed", "documents -> sources/extracted/*.txt + canon", ""
    if ext == ".png":
        return "processed", "maps -> sources/maps/", ""
    if ext == ".txt":
        # near-empty wiki stubs
        try:
            with open(full, encoding="utf-8", errors="replace") as f:
                lines = [l for l in f.read().splitlines() if l.strip()]
        except OSError:
            lines = ["x"]
        if len(lines) <= 1:
            return "stub", "wiki (empty/redirect)", "1 line or fewer"
        return "processed", "wiki -> sources/extracted/wiki/ digests", ""
    return "pending", "-", ""


def load_manifest():
    rows = {}
    if not os.path.exists(MANIFEST):
        return rows
    with open(MANIFEST, encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.rstrip("\n")
            if not line or (i == 0 and line.startswith("status\t")):
                continue
            parts = line.split("\t")
            while len(parts) < 5:
                parts.append("")
            status, source, s12, into, notes = parts[:5]
            rows[source] = {"status": status, "sha12": s12, "processed_into": into, "notes": notes}
    return rows


def write_manifest(rows):
    lines = ["\t".join(HEADER)]
    for source in sorted(rows):
        r = rows[source]
        lines.append("\t".join([r["status"], source, r["sha12"], r["processed_into"], r["notes"]]))
    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def cmd_init():
    if os.path.exists(MANIFEST):
        print("manifest already exists; use 'register' to add new files, or delete it to re-init.")
        return 1
    raw = scan_raw()
    rows = {}
    for rel, h in raw.items():
        status, into, notes = guess_processed_into(rel, os.path.join(RAW, rel))
        rows[rel] = {"status": status, "sha12": h, "processed_into": into, "notes": notes}
    write_manifest(rows)
    print(f"initialized manifest with {len(rows)} files -> {os.path.relpath(MANIFEST, ROOT)}")
    return 0


def cmd_register():
    raw = scan_raw()
    rows = load_manifest()
    added = 0
    for rel, h in raw.items():
        if rel not in rows:
            rows[rel] = {"status": "pending", "sha12": h, "processed_into": "-", "notes": ""}
            added += 1
    write_manifest(rows)
    print(f"registered {added} new file(s) as 'pending'.")
    return 0


def cmd_mark(argv):
    if len(argv) < 2:
        print("usage: mark <source> <status> [processed_into] [notes...]")
        return 2
    source, status = argv[0], argv[1]
    into = argv[2] if len(argv) > 2 else None
    notes = " ".join(argv[3:]) if len(argv) > 3 else None
    rows = load_manifest()
    if source not in rows:
        print(f"'{source}' not in manifest (run 'register' first)")
        return 2
    rows[source]["status"] = status
    if into is not None:
        rows[source]["processed_into"] = into
    if notes is not None:
        rows[source]["notes"] = notes
    write_manifest(rows)
    print(f"marked {source} -> {status}")
    return 0


def cmd_scan():
    raw = scan_raw()
    rows = load_manifest()
    new, changed, pending = [], [], []
    for rel, h in sorted(raw.items()):
        if rel not in rows:
            new.append(rel)
        elif rows[rel]["sha12"] != h:
            changed.append(rel)
        elif rows[rel]["status"] == "pending":
            pending.append(rel)
    missing = [s for s in rows if s not in raw]
    total = len(raw)
    processed = sum(1 for s in rows if rows[s]["status"] == "processed" and s in raw)
    stub = sum(1 for s in rows if rows[s]["status"] == "stub" and s in raw)
    print(f"sources/raw: {total} files | processed {processed} | stub {stub} | "
          f"pending {len(pending)} | NEW {len(new)} | CHANGED {len(changed)}")
    for label, items in (("NEW (unregistered)", new), ("CHANGED (hash differs)", changed),
                         ("PENDING (registered, not processed)", pending),
                         ("MISSING (in manifest, not on disk)", missing)):
        if items:
            print(f"\n{label}:")
            for it in items:
                print(f"  - {it}")
    todo = len(new) + len(changed) + len(pending)
    if todo == 0:
        print("\nAll sources processed. Nothing pending. ✓")
    else:
        print(f"\n{todo} item(s) need attention. Run 'register' to queue NEW files, "
              f"then process and 'mark' them.")
    return 1 if todo else 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "scan"
    if cmd == "init":
        return cmd_init()
    if cmd == "register":
        return cmd_register()
    if cmd == "mark":
        return cmd_mark(sys.argv[2:])
    if cmd in ("scan", "status"):
        return cmd_scan()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
