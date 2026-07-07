# sources/extracted/ — Machine-extracted text

Plain-text extractions of the original documents in `../raw/`, so the material is
readable, searchable, and diff-able. **These are derived files** — the originals in
`../raw/` remain the ground truth. If an extraction looks wrong, check the original.

## How they were extracted
- **PDFs** → text + image counts via **PyMuPDF** (`fitz`). Page breaks marked
  `===== [page N] =====`.
- **.docx** → unzipped `word/document.xml`, tags stripped to text.
- **.doc** (Word 97–2003 / OLE2) → **antiword** with UTF-8 mapping (LibreOffice
  refused these files in this environment). Italian accents preserved.

All 13 source files extracted successfully (~46,000 words total).

## Source index — what each document is

| Document | Type | ~words | What it holds |
|----------|------|-------:|---------------|
| **Player Guide.pdf** | PDF, 33 pp (462 imgs) | 12,560 | **Keystone.** Origin myth, races, full pantheon & cosmogony, extraplanar taxonomy, Sovereign Demons, calendar/zodiac, master chronology, glossary. |
| **Cartosa Guida.pdf** | PDF, 31 pp (17 imgs) | 13,520 | **Full sourcebook** for the Principality of Cartosa & Republic of Meridian: history, territory, peoples, politics/law, religion, guilds & noble houses, equipment, combat styles, map. |
| **LIBRO+ROSSO+DEL+CONTROLLO+MAGICO.pdf** | PDF, 52 pp (52 imgs) | 10,701 | The **magic system** ("Red Book of Magic Control"). *Not yet mined.* |
| **Maraviglie.pdf** | PDF, 5 pp (50 imgs) | 1,626 | "Marvels/Wonders" — likely artefacts/wonders/creatures. *Not yet mined.* |
| **Edizione Straordinaria.pdf** | PDF, 1 p | 487 | "Special Edition" — a broadsheet/news piece? *Not yet mined.* |
| **Qi-Long_ Onore e Memoria.docx** | DOCX (9.4 MB, imgs) | 588 | The **Qi-Long** (eastern realm), "Honour and Memory." *Not yet mined.* |
| **Sadhir_Compiled_Gazetteer.docx** | DOCX | 465 | Gazetteer of the **Sadhir** (desert region). *Not yet mined.* |
| **Storia dell'impero Letio.doc** | DOC | 224 | Brief **history of the Letio Empire** (the Dark Days). Read in full. |
| **Cartosa.doc** | DOC | 2,365 | Earlier/parallel **Cartosa** text; overlaps the PDF sourcebook. *Partly read.* |
| **Armora - città.doc** | DOC | 190 | The city of **Armora** (technocratic Young Kingdom). *Not yet mined.* |
| **Helgedad.doc** | DOC | 2,403 | The island realm of **Helgedad** (grimdark north). *Not yet mined.* |
| **Gaerwath.doc** | DOC | 1,245 | The **Gaerwath** — Dark Elf homeland & society. *Partly read.* |
| **elfi oscuri.doc** | DOC | 318 | **Dark Elves** — caste system, demon-binding, Arvo. Read in full. |

## Extraction status legend
- **Mined into canon:** Player Guide, Storia Letio, elfi oscuri, Cartosa Guida
  (pp.1–15), **Helgedad, Gaerwath, Armora, Edizione Straordinaria, Qi-Long, Sadhir,
  Maraviglie, LIBRO ROSSO** (framing + four realms). **Maps extracted** → `../maps/`.
- **Partly mined / to revisit:** Cartosa Guida (pp.16–31: equipment, combat styles),
  Cartosa.doc (overlaps the PDF), LIBRO ROSSO (deep spell/tactics detail per realm).
- Tracked in `../../NOTES.md`.
