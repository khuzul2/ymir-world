# sources/ — Raw material

Everything about Ymir, preserved **exactly as received**. This directory is the
ground truth. Nothing here should be edited for style or "corrected" — if a note
contradicts another note, both stay, and the contradiction gets logged in the
top-level `NOTES.md`.

## Processing status
Which sources have been mined into canon is tracked in **`PROCESSING.md`** +
**`manifest.tsv`** (hash-based). After any new upload, run
`python3 scripts/source_status.py` to see what's new or changed.

## Where to put things

- `raw/` — the default dumping ground. Any file type: `.md`, `.txt`, `.pdf`,
  images of maps or handwritten notes, exported chat logs, spreadsheets.
- `by-contributor/<name>/` — optional, if it's useful to keep each person's or
  each campaign's material separate (helps later when sources disagree and we
  need to know *whose* version something is).

## Naming suggestion (not required)

`YYYY-<topic>-<contributor>.md`, e.g. `2019-fall-of-eastmarch-alessandro.md`.
Anything is fine though — legibility of the pile matters more than a strict scheme.

## A few prompts to jog memory (for whoever's contributing)

Even one-line fragments are valuable. Things that are easy to forget you know:
- Place names, and what happened there
- Factions / nations / guilds / cults, and who runs them
- Gods, spirits, religions, and how magic is understood in-world
- Big historical events, wars, cataclysms, "the time when…"
- Recurring NPCs and famous player characters
- House rules or setting-specific mechanics
- Maps, even rough or partial
- Anything that was "obviously true" at your table but never written down
