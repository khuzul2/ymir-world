# Ymir — Google Drive corpus manifest

Full catalogue of the Google Drive **"Ymir"** folder tree (owner: alessandro.petri@gmail.com),
pulled **2026-07-07**. This is the second, much larger batch of source material (the first
batch lives in `sources/raw/*` at the repo root).

Everything Ymir-relevant that could be pulled through the Drive connector is here; anything
**not** pulled is listed with the reason and a link, so nothing is lost — it can be fetched
later or re-exported.

## Legend
- ✅ **extracted** — text in `sources/extracted/ymir-drive/`
- 📦 **raw saved** — original binary in `sources/raw/ymir-drive/`
- 🖼️ **map** — image saved under `sources/raw/ymir-drive/maps/`
- 🚫 **too big** — over the connector's **10 MB** binary-download cap; not pulled
- ⏭️ **skipped** — deliberately not pulled (char sheets, stock art, generic non-Ymir netbooks)
- (folder ids link to Drive; file ids link to the file)

Drive links: folders → `https://drive.google.com/drive/folders/<id>` · files → `https://drive.google.com/file/d/<id>/view`

---

## Tree overview

```
Ymir/                                  (root folder 0B51K1jhM2wrFcDZlbTc3ZEctbjQ)
├─ YMIR/                               homebrew "YMIR" game system + lore   (0B51K1jhM2wrFQVIyTXJkRFVxcm8)
│  ├─ (files: Basic Rules, Talents, Atlas, Skills, Races, Armour, world maps)
│  ├─ Old/                             world "Ymir" tree + early rules + PC Graveyard  (0B51K1jhM2wrFM3p2RkJPMklJQnM)
│  │  └─ Ymir/                         maps & nations, campaigns, char sheets  (0B51K1jhM2wrFTEIwUzhoNVRzeFU)
│  │     ├─ 2 - Ymir - mappe e nazioni/  (0B51K1jhM2wrFRVBUMm1USThFUHc)  → per-nation folders (mostly maps)
│  │     ├─ 4 - Maps Ale/  · Oldies/ · 6 - Extras/ · 5 - Campaigns/ · 3 - Character Sheets/ · 1 - Regolamento base/
│  │     ├─ Pc Graveyard/  · Y2/ · Old Charasheet/ · Evoluzione Regolamento YmiRM/
│  ├─ Magic [Max]/                     full magic & summoning system   (0B51K1jhM2wrFczhncmJKX3Q0MTA)
│  │  └─ Old/  → Allspells/            A–Z spell compendium (9 rtf)     (0B51K1jhM2wrFQWl3VkI3RC1OQjQ)
│  ├─ Sheets & Cards/ · Combat [Ale]/ · Immagini per combat/  (char sheets / stock art)
├─ RMSS-RMFRP/ · Renaissance/ · AD&D2/  (generic systems; AD&D2 also holds a non-Ymir campaign)
└─ (loose: 2 GM random-generators, combat spreadsheets)
```

---

## YMIR/ — homebrew system + core lore  · folder `0B51K1jhM2wrFQVIyTXJkRFVxcm8`

| File | id | Status | Notes |
|---|---|---|---|
| YMIR 1.0.7 - Basic Rules.docx | 0B51K1jhM2wrFdy1QVkZ5ZXBDdDA | ✅ 📦 | d100 "YMIR" core rules (Levels/Actions pillars) |
| YMIR 1.0.7 - Talents and Flaws.docx | 0B51K1jhM2wrFYmJqTG0wV0xnSzg | ✅ 📦 | Talents across 6 Paths (Combat/Summoning/Magic/Corruption/Faith/General) |
| YMIR 1.0.2 - Atlas.docx | 0B51K1jhM2wrFaTlQelAzTjhnWTA | ✅ 📦 | **Cosmogony** — Old Gods, Mithra/Ahriman, Dark Mana, races, Maelstrom |
| Ymir 1.0.5 Skills.doc | 0B51K1jhM2wrFSUtXQ2pjZl9oa1U | ✅ 📦 | Skills + Resistances |
| Ymir 1.0.2 - Races.xls | 0B51K1jhM2wrFdUtNSkNqa2hoR2s | ✅ 📦 | Playable-race stat data (legacy .xls, converted locally) |
| Armour.doc | 0B51K1jhM2wrFb2h2TV9ITC1WX3c | ✅ 📦 | Armour table |
| Temp. Per Bilanciamento Skill.xlsx | 0B51K1jhM2wrFb2swaW5rekVyRjQ | ⏭️ | pure skill-balancing math |
| YMIR.png | 0B51K1jhM2wrFY3d1enhVck5VWms | 🖼️ 📦 | world map (raster) |
| ymirexplored.png | 0B51K1jhM2wrFdlNxMzRUb1JfQkE | 🖼️ 📦 | "explored world" map (raster) |
| YMIR.psd | 0B51K1jhM2wrFVk8tbXBKVHlLMkk | 🖼️ | world map PSD (4.6 MB) → converted to `maps/YMIR.jpg` |

## YMIR/ (loose) & sibling generic folders
| File / folder | id | Status | Notes |
|---|---|---|---|
| Generatore di Situazioni Bifolche (Google Sheet) | 1WRjJHdb5HS-5LCQd7sXFosk-2_W0sjD3XWPvCiiipHs | ✅ | GM peasant-situation generator |
| Generatore di incontri (Google Sheet) | 11V-uf6Fl-ZPOexex5qH7NUUyf7bNqiR6Oj_Jb3oIO7E | ✅ | GM hostile-encounter generator |
| Tarter.xls / Scheda Combat Pulita.xls | 0B51K1jhM2wrFTElVaDNKMVdRREE / 0B51K1jhM2wrFZEJzcUg3VjlLY2c | ⏭️ | combat spreadsheets |
| RMSS-RMFRP/ (folder) | 0B51K1jhM2wrFRU1WRjlrUEY0MjA | ⏭️ | generic Rolemaster char sheets |
| Renaissance/ → Renaissance D100 black-powder SRD.pdf | 0B51K1jhM2wrFd1VuSmRWb1QwQ0E | ⏭️ | generic D100 SRD (possible system used for swashbuckling Cartosa) |
| AD&D2/ (folder) | 0B51K1jhM2wrFTjBtMy1Yd1RKXzQ | ⏭️/⚠️ | AD&D 2e netbooks (generic) **+ a non-Ymir campaign** (see below) |

## YMIR/Old/ — early rules, world tree, PC Graveyard · folder `0B51K1jhM2wrFM3p2RkJPMklJQnM`
| File | id | Status | Notes |
|---|---|---|---|
| YMIR 1.0.0 - Rules.pdf | 0B51K1jhM2wrFUEVEekZ4emJfUEE | ✅ 📦 | early full rulebook ("YmiR2") |
| YMIR 1.0.0 - Combat.docx | 0B51K1jhM2wrFSFJXRV9hMU1UUm8 | ✅ 📦 | early combat chapter |
| Character sheets (.pdf/.xlsx ×7), Critical Hits (.xlsx ×2) | — | ⏭️ | char sheets (per Alessandro) |
| **Pc Graveyard/** → (RIP) Mura_02.pdf | 0B51K1jhM2wrFQW1LdzFJZ3pHd0E | ✅ 📦 | **canon PC** — Kharim Abdul Jabbar, lvl-2 Thief |
| Y2/ · Old Charasheet/ · Evoluzione Regolamento YmiRM/ | — | ⏭️ | char sheets / rules-evolution history (empty or sheets) |

### YMIR/Old/Ymir/ — world: maps, nations, campaigns · folder `0B51K1jhM2wrFTEIwUzhoNVRzeFU`
- **2 - Ymir - mappe e nazioni/** `0B51K1jhM2wrFRVBUMm1USThFUHc` — per-nation folders. Most are **empty** or contain only map subfolders:
  - **Gaerwath/Mappa nazione/** → Map - Gaerwath c.a. 3500 p.M..jpg `0B51K1jhM2wrFTlVyRGZOSU8wZ1k` — 🖼️ 📦✅ (archipelago; vision-OCR'd for island names)
  - Letia, Sadhir, Regni giovani, Qi Long, Ophiur, Meridian, Helgedad, Cartosa, Alfheim — folders present, **no downloadable files** (empty / map-placeholder subfolders)
  - `- Mappa Ymir e generiche del continente/` `0B51K1jhM2wrFY2g3Y0E4dGRnX2M` → **Ymir_50x75_300dpi_0.3.psd** `0B51K1jhM2wrFdWdPR3NBMTFDbGc` — 🚫 **130 MB print world map (over 10 MB cap)**
- **4 - Maps Ale/** `0B51K1jhM2wrFcWZrWjZPb0FUVGs` → **Letia Hexr.psd** `0B51K1jhM2wrFaXlpX2pmak1OZm8` — 🚫 **130 MB Letia hex map (over cap; no raster alternative)**
- **5 - Campaigns/** `0B51K1jhM2wrFa2ZJVXp2T24xSTA` → "2011,2012 - PBM - If you want peace" `0B51K1jhM2wrFWkdqb2tzM1YtSU0` (→ Schede PG, empty) · "2011 - A World at War" (empty)
- **1 - Regolamento base/** `0B51K1jhM2wrFZmFDbTBpY1RiTFk` → 01 Current Release (empty) · 02 WIP → **Ymir Redux** `0B51K1jhM2wrFTXlSSXBQc1JQQlE` (empty rewrite folder) · 03 Oldies (empty)
- **Oldies/** → Atlanti → Qilong → ispirazione (empty) · **6 - Extras/** → Pics (empty) · **3 - Character Sheets/** → Oldies (empty)

## YMIR/Magic [Max]/ — magic & summoning system · folder `0B51K1jhM2wrFczhncmJKX3Q0MTA`
| File | id | Status | Notes |
|---|---|---|---|
| YMIR 1.0.2 - Magic and Sorcery.docx | 0B51K1jhM2wrFdWJvM0pjVERPNkU | ✅ 📦 | magic system (Domains, Orders, PP) |
| YMIR 1.0.3 - Magia.doc | 0B51K1jhM2wrFajBXcHc5aEZObkU | ✅ 📦 | magic (Italian) |
| YMIR 1.0.3 - Guarigione.doc | 0B51K1jhM2wrFdDdQQUd1THg3ODA | ✅ 📦 | healing (Italian) |
| YMIR 1.0.3 - Spells Ale Necro.docx | 0B51K1jhM2wrFS25CYS15enNtNVk | ✅ 📦 | Necromancy & Elemental spell tables |
| YMIR 1.0.4 - Spells Max level.odt | 0B51K1jhM2wrFUEpGRU1CRnc1TDA | ✅ 📦 | spell compendium (~23k words) |
| Spellbook.pdf | 0B51K1jhM2wrFejNCc1F1Tkl3ZjQ | ✅ 📦 | "Ymir Spell Compendium" |
| spellbook (fede).odt | 0B51K1jhM2wrFOXBkbTBkZnhQeEU | ✅ 📦 | a player's spellbook |
| YMIR 1.0.3 - Summoning Skill Recap (draft).xlsx | 0B51K1jhM2wrFMVd5QXVTQUxZN0U | ✅ 📦 | Summoning (Evoke/Contact/Bind/Vessel/Possess) |
| Incantesimi.doc (in Old/) | 0B51K1jhM2wrFYll6WDIzVEpEWHc | ✅ 📦 | schools of magic (Italian) |
| spellbook (fede).rtf / SpellsRedux.rtf / Spell Failure.pdf / Improvised Magic.xlsx / note*.xls | — | ⏭️ | duplicates / mechanics-only |
| **Old/Allspells/** → SpellsA-B … T-Z (.rtf ×9) | folder 0B51K1jhM2wrFQWl3VkI3RC1OQjQ | ⏭️ | **generic d20 SRD spells (OGL)** — NOT Ymir homebrew (they read "Sor/Wiz N", "Components: V,S,M,F", Open Game Content). A reference stash; excluded to keep the corpus clean. Link-only. |

## YMIR/Combat [Ale]/Old/ · folder `0B51K1jhM2wrFV2hIeXpvX1dJMUE`
| File | id | Status | Notes |
|---|---|---|---|
| YMIR 1.0.2 - Combat.docx | 0B51K1jhM2wrFVWdGWnpnUGhPSmc | ✅ 📦 | combat chapter |
| Armi.doc | 0B51K1jhM2wrFR0RGTmRCMkwzMm8 | ✅ 📦 | weapons (Danno/Taglia/Allungo) |
| Combat Actions Recap (.xlsx/.pdf), combat cheatsheet ita.xls | — | ⏭️ | mechanics recaps |

## YMIR/Immagini per combat/ · folder `0B51K1jhM2wrFNmtsSnQxaDdBWU0`
- ⏭️ ~70 **stock fantasy wallpaper JPGs** (Warhammer/MTG/generic art) used as VTT status icons + `comune_cap_pr_regione.xls` (Italian postal data). Not Ymir lore.

## AD&D2/Campagna Estate 2014/ — ⚠️ separate non-Ymir campaign · folder `0B51K1jhM2wrFSWtFTDVPS2R5V3M`
"The Forgiven Lands" — an **AD&D 2e** campaign, **not the Ymir setting** (own map & continuity; villain "Duca di Nimard"). Captured for review under `sources/extracted/ymir-drive/_uncertain-forgiven-lands/`:
| File | id | Status |
|---|---|---|
| Plot.docx | 0B51K1jhM2wrFUHpTalJ6bzNSRVU | ✅ 📦 (quarantined) |
| House Rules.docx | 0B51K1jhM2wrFQk9VWHB1cG8ySFk | ✅ 📦 (quarantined) |
| Locations.rtf | 0B51K1jhM2wrFa2lqZ2MyazNxU2s | ✅ 📦 (quarantined) |
| The Forgiven Lands.jpg (12 MB) | 0B51K1jhM2wrFQ0U3bnJiS2lNNXc | 🚫 over 10 MB cap |
| The Forgiven Lands.psd (375 MB) | 0B51K1jhM2wrFNHVqcFRzYWN6SVU | 🚫 over 10 MB cap |
| Session xlsx (Tomb of Archduke Dairyon, Dungeon Escape), netbook pdfs | — | ⏭️ |

---

## Not recoverable through current tools (need action)
The Drive connector caps binary downloads at **10 MB**. These maps exceed it:
| Map | id | Size | Raster alternative? |
|---|---|---|---|
| Ymir_50x75_300dpi_0.3.psd (print world map) | 0B51K1jhM2wrFdWdPR3NBMTFDbGc | 130 MB | yes — `maps/YMIR.jpg`, `maps/ymirexplored.png` (lower res) |
| Letia Hexr.psd (Letia hex map) | 0B51K1jhM2wrFaXlpX2pmak1OZm8 | 130 MB | **none** |
| The Forgiven Lands.psd / .jpg | 0B51K1jhM2wrFNHVqcFRzYWN6SVU / 0B51K1jhM2wrFQ0U3bnJiS2lNNXc | 375 MB / 12 MB | (non-Ymir) |

**To recover:** re-export each to a **<10 MB flattened JPG/PNG in Drive** (then it can be pulled),
or fetch via the raw Google Drive API with OAuth (not exposed through the current MCP tool).
