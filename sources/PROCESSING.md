# Source processing tracker

With material arriving in batches (and a second contributor/agent adding files in
parallel), we track exactly which sources have been mined into canon and which are new.

## The pieces
- **`manifest.tsv`** — one row per file in `raw/`, with a content **hash** and a
  **status** (`processed` / `pending` / `stub`) and where it was `processed_into`.
  Because the hash is stored, a file that is **re-uploaded or edited** shows up as
  **CHANGED**, not silently treated as done.
- **`../scripts/source_status.py`** — scans `raw/`, diffs it against the manifest, and
  reports what needs attention.

## The loop (run every time new sources may have arrived)
```
git pull origin <branch>                         # get any new uploads
python3 scripts/source_status.py                 # what's NEW / CHANGED / PENDING?
python3 scripts/source_status.py register        # queue NEW files as 'pending'
# … extract & fold each pending file into canon (and a digest if large) …
python3 scripts/source_status.py mark "<file>" processed "<where it went>"
git add -A && git commit && git push             # manifest travels with the work
```
`source_status.py` exits **non-zero** while anything is NEW/CHANGED/PENDING, so it can
gate the "start the manual" step — we only begin the manual when it reports clean.

## Status meanings
| status | meaning |
|--------|---------|
| `processed` | mined into `canon/` (and/or a digest under `extracted/`) |
| `pending` | present but **not yet** processed — the work queue |
| `stub` | looked at; empty/near-empty/redirect — nothing to extract |

## Current state
Initialized against the full corpus (documents + wiki export + maps). Run
`python3 scripts/source_status.py` for the live count.
