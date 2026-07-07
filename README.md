# Ymir — World Bible Project

This repository collects the scattered material about **Ymir**, a fantasy world
that has hosted several tabletop RPG campaigns, and turns it into a single,
coherent game-world manual.

Ymir grew organically across campaigns and Game Masters, so the source material
is sparse, informal, and sometimes contradictory. The goal here is to preserve
all of it, reconcile it, fill the gaps, and produce a manual you can actually
run games from.

## How this works — two phases

### Phase 1 — Collect & structure
1. **Dump raw material** into `sources/` exactly as it is — notes, character
   sheets, maps, session logs, half-remembered rules, anything. Nothing gets
   thrown away or "cleaned up" at this stage.
2. **Extract & index** it into `canon/`, organized by topic (geography,
   factions, pantheon, history, magic, peoples, creatures, characters…).
   Every extracted fact is traceable back to its source.
3. **Track gaps & contradictions** in `NOTES.md` instead of silently smoothing
   them over.

### Phase 2 — Build the manual
4. **Design the manual's structure** together (see `manual/OUTLINE.md`).
5. **Draft each chapter**, reconciling contradictions with you and inventing
   connective tissue where the sources are thin.
6. **Keep canon honest**: anything invented to fill a gap is marked, so you
   always know what came from your table versus what was added.

## Repository layout

```
sources/        Raw material, preserved as-is
  raw/            Drop files here (docs, txt, images, PDFs, maps, scans)
  by-contributor/ Optional: one subfolder per person/campaign
canon/          Structured extraction of the world, by topic
manual/         The finished world bible, chapter by chapter
  OUTLINE.md      Proposed table of contents
NOTES.md        Running log of open questions, gaps, and contradictions
README.md       This file
```

## How to contribute material

Any of these work — mix freely:
- **Paste it in chat** and it gets filed into `sources/` for you.
- **Commit files** into `sources/raw/` (or `sources/by-contributor/<name>/`).
- **Point at Google Drive** docs and they get pulled in.

Don't worry about formatting or organization when contributing — raw and messy
is fine and expected. Structuring is the job of Phase 1.

## Convention: marking what's canon vs. invented

Throughout `canon/` and `manual/`, added/invented content is tagged so it's
never mistaken for original source material:

- `[CANON]` — drawn directly from your source material.
- `[INFERRED]` — reasoned from canon, not stated but strongly implied.
- `[INVENTED]` — newly created to fill a gap; needs your blessing.
- `[CONFLICT]` — sources disagree; see `NOTES.md` for the open question.
