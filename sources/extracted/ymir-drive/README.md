# sources/extracted/ymir-drive/ — Google Drive corpus (extracted text)

Machine-extracted text from the **second source batch**, pulled from Alessandro's
Google Drive "Ymir" folder tree on **2026-07-07**. Originals are preserved under
`../../raw/ymir-drive/`; the full Drive catalogue (with links + what was skipped and
why) is in `../../raw/ymir-drive/DRIVE-MANIFEST.md`.

These are **derived files** — the originals in `../../raw/ymir-drive/` are ground truth.

## How extracted
- **.docx / .doc / .pdf / .odt / images** → Drive `read_file_content` (natural-language
  text; maps get a vision description + OCR'd labels).
- **.odt** (spellbook) → local `zipfile`/XML strip.
- **.rtf** → local brace-aware RTF parser (LibreOffice is non-functional in this container).
- **.xls** (Races) → local `xlrd` (all sheets → TSV).

## What this batch adds vs. the root `sources/` batch
The root batch was mostly **world/nation prose** (Player Guide, Cartosa, nations). This
batch is the group's **homebrew "YMIR" game system** (a Rolemaster-inspired d100 ruleset,
v1.0.0→1.0.7) plus the **cosmogony**, the **full magic/summoning system**, the **playable
races**, **world maps**, and a **canon player-character**. The system is mechanics, but it
carries a lot of embedded setting lore (gods, races, planes, summoned entities).

## Index — what each file holds

### Cosmogony & setting
| File | ~words | Holds |
|---|---:|---|
| `YMIR-1.0.2-Atlas.txt` | 1,800 | **Cosmogony.** Void+Mana → First Clash → 6 **Old Gods**; **New Gods Mithra & Ahriman** banish them; **Dark Mana** (cosmic cancer; Ahriman = corrupted Old God); 8 Elemental Planes; Demons & **Seven Demonic Circles**; First War (**Vanyr vs Asar**); races; the **Maelstrom**. |
| `YMIR-1.0.2-Races.txt` | 290 | **Playable races** + stat blocks: Common Man, **Asar, Aeryan, Tanoth, Dwergar, Xebechan (Xudra/Xion/Xattva), Nkishi** — bonuses, resistances, traits (Infravision, Magesense, natural weapons…). |

### Maps (vision OCR)
| File | ~words | Holds |
|---|---:|---|
| `MAP-ymirexplored.txt` | 430 | World map — **Regni Giovani, Regni Belligeranti, Letia, Cartosa, Erg, Helgedad, Gaerwath**. |
| `MAP-YMIR.txt` | 400 | World map — **Letia** (Regni Belligeranti/Giovani), **Erg** (Sadhir to the south), **Qi-Long** (NE), **Ophiur** (SE), Helgedad, **Xebech**; 2000 km scale. |
| `MAP-Gaerwath-3500dM.txt` | 1,160 | **Gaerwath archipelago**, dated **c.a. 3500 p.M.** — islands Kh'myr, Yr'thyr, Wag'myr, N'ysyr, Dr'hakyr, Moloch, Daarwyr, Gh'yrst, Isola del Caos, Cn'ethyr. |

### Characters
| File | ~words | Holds |
|---|---:|---|
| `PC-Mura.txt` | 600 | **Canon PC** from the "Pc Graveyard": **Kharim Abdul Jabbar**, lvl-2 Thief (Common Man, Essence realm); Ring of *Unseen III*, "Zephyr Hound (Cane delle Tempeste)". |

### Homebrew YMIR system (rules — mechanics, with embedded lore)
| File | ~words | Holds |
|---|---:|---|
| `YMIR-1.0.7-Basic-Rules.txt` | 4,700 | d100 core (Levels/Actions pillars, 6 Stats, creation); **Corruption** subsystem — Dark (pacts w/ Demons; **Ahriman**), Elemental, Mental/**Follia**. |
| `YMIR-1.0.0-Rules.txt` | 10,200 | Earlier "YmiR2" core rulebook (STR/DEX/CON/INT/LOG/SD; Power **Leagues**; Corruption; travel; substances). |
| `YMIR-1.0.7-Talents-and-Flaws.txt` | 6,600 | Talents across 6 **Paths**; **pantheon Patrons** (Mithra, Ishtar, Kur, Thurms, Gog, Yogh, Heis; dark master **Ahriman**); Summoning roles & **Pales**. |
| `YMIR-1.0.5-Skills.txt` | 1,600 | Skills, Resistances, Alchemy; **Summoning** (Evoke/Contact/Bind/Vessel/Possess; entities from "Pales"). |
| `YMIR-1.0.0-Combat.txt` | 3,100 | AP/PP round combat; Power Leagues (Mundane→Epic); worked example (Groll vs Amoth). |
| `YMIR-1.0.2-Combat.txt` | 2,280 | Combat v1.0.2 (Initiative, Snap/All-Out/Feint/Dodge). |
| `YMIR-Armour.txt` | 230 | Armour table (Cloth→Plate; special materials). |
| `YMIR-Armi.txt` | 110 | Weapons (Danno/Taglia/Allungo-Reach). |

### Magic & summoning system
| File | ~words | Holds |
|---|---:|---|
| `YMIR-1.0.2-Magic-and-Sorcery.txt` | 3,300 | Magic system — **Domains** (Elemental/Natural/Planar/Humane), Orders, Spell Failure; summoning **Leagues** priced in Corruption/souls (up to an "Ecatombe"). |
| `YMIR-1.0.3-Magia.txt` | 2,630 | Magic (Italian) — 9 **Ordini**, Stregoneria, Punti Potere. |
| `YMIR-1.0.3-Guarigione.txt` | 165 | Healing (Italian) — First Aid, pf/hit points. |
| `YMIR-1.0.3-Spells-Ale-Necro.txt` | 3,810 | Spell tables — **School of Necromancy** & Elemental. |
| `YMIR-1.0.4-Spells-Max-level.txt` | 23,000 | Spell compendium by **Order** (English). |
| `YMIR-Spellbook.txt` | 23,000 | "Ymir Spell Compendium" — spells tagged **Arcane/Divine**, Resistance Rolls. |
| `YMIR-Incantesimi.txt` | 340 | Schools of magic (Italian) — **Dominio Elementale**. |
| `YMIR-1.0.3-Summoning-Skill-Recap.txt` | 9,000 | Summoning recap — 5 effects × 4 entity types (Demon/Elemental/Spirit/Outsider). |
| `spellbook-fede.txt` | 2,600 | A player's YMIR spellbook ("Spellbook 2.0", Italian; spells by Order). |

### GM tools
| File | ~words | Holds |
|---|---:|---|
| `Gen-Situazioni-Bifolche.txt` | 1,100 | Random **peasant-situation** generator (Italian Mad-Libs table). |
| `Gen-Incontri.txt` | 380 | Random **hostile-encounter** generator (Italian). |

### Excluded — Forgiven Lands (AD&D2), not Ymir
A separate **AD&D 2e "Forgiven Lands"** campaign was found in Drive (own map & continuity;
villain *Duca di Nimard*). **Excluded per Alessandro** — not part of Ymir. It remains
catalogued (link-only) in `../../raw/ymir-drive/DRIVE-MANIFEST.md`.

## Not extractable (see manifest)
- The **large map PSDs** (`Ymir_50x75_300dpi` 130 MB print world map, `Letia Hexr` 130 MB hex
  map) exceed the Drive connector's **10 MB** download cap. The world map is here at raster
  res (`../../raw/ymir-drive/maps/YMIR.jpg`, `ymirexplored.png`, `YMIR.png`); the **Letia hex
  map has no raster alternative**. **Alessandro will supply these maps separately** — not to be
  re-attempted via the connector.
- The `Allspells/` folder was **generic d20 SRD (OGL)** spells, not Ymir — excluded.
- **Character sheets** and generic AD&D2/Rolemaster netbooks — skipped (catalogued in manifest).
