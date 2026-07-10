# sources/extracted/wiki-worldofymir/ — World of Yimir Fandom wiki

Full extraction of the **World of Yimir** community wiki
(<https://worldofymir.fandom.com>), authored by Alessandro and friends —
the same table that produced the documents in `../`. Imported 2026-07-07.

**75 pages, ~62,422 words** (main namespace).

## Layout

- `../../raw/wiki-worldofymir/*.wikitext` — the raw MediaWiki source of each
  page, exactly as authored (the ground-truth original).
- `wiki-worldofymir/*.md` (this folder) — the same pages rendered to readable
  Markdown, each with a header linking back to its live URL, last-edit date,
  and wiki categories.

## How it was extracted

Pulled via the MediaWiki API (`api.php`) on 2026-07-07:

- **Raw:** `action=query&prop=revisions&rvslots=main` → verbatim wikitext.
- **Readable:** `action=parse&prop=text` → rendered HTML → Markdown via
  `html2text`; placeholder/broken-image artifacts stripped, blank runs
  collapsed. Categories from `action=parse&prop=categories`.

The wiki front page sits behind a Cloudflare browser check, but the API
endpoint answers normally, so the whole site came across cleanly.

> Language note: most pages are in **Italian** (setting material); the
> campaign reports are in **English**. Same as the rest of `sources/`.

## Page index

### Cosmology & the planes

| Page | ~words | File |
|------|-------:|------|
| [Entità](https://worldofymir.fandom.com/wiki/Entità) | 836 | `Entità.md` |
| [Cosmologia](https://worldofymir.fandom.com/wiki/Cosmologia) | 642 | `Cosmologia.md` |
| [Divinità Elementali](https://worldofymir.fandom.com/wiki/Divinità_Elementali) | 568 | `Divinità Elementali.md` |
| [Dei Esterni](https://worldofymir.fandom.com/wiki/Dei_Esterni) | 536 | `Dei Esterni.md` |
| [I Piani e il Multiverso](https://worldofymir.fandom.com/wiki/I_Piani_e_il_Multiverso) | 311 | `I Piani e il Multiverso.md` |

### History & chronology

| Page | ~words | File |
|------|-------:|------|
| [L'Era della Marea](https://worldofymir.fandom.com/wiki/L'Era_della_Marea) | 2,408 | `L'Era della Marea.md` |
| [Cronologia](https://worldofymir.fandom.com/wiki/Cronologia) | 1,254 | `Cronologia.md` |

### Regions & realms

| Page | ~words | File |
|------|-------:|------|
| [Helgedad](https://worldofymir.fandom.com/wiki/Helgedad) | 2,546 | `Helgedad.md` |
| [Cartosa e Meridian](https://worldofymir.fandom.com/wiki/Cartosa_e_Meridian) | 2,428 | `Cartosa e Meridian.md` |
| [Gaerwath](https://worldofymir.fandom.com/wiki/Gaerwath) | 1,880 | `Gaerwath.md` |
| [Il Grande Erg](https://worldofymir.fandom.com/wiki/Il_Grande_Erg) | 771 | `Il Grande Erg.md` |
| [Maelstrom](https://worldofymir.fandom.com/wiki/Maelstrom) | 485 | `Maelstrom.md` |
| [Qi-Long](https://worldofymir.fandom.com/wiki/Qi-Long) | 281 | `Qi-Long.md` |
| [Letia](https://worldofymir.fandom.com/wiki/Letia) | 178 | `Letia.md` |
| [Kyria](https://worldofymir.fandom.com/wiki/Kyria) | 174 | `Kyria.md` |
| [Isole d'Argento](https://worldofymir.fandom.com/wiki/Isole_d'Argento) | 108 | `Isole d'Argento.md` |
| [Alfheim](https://worldofymir.fandom.com/wiki/Alfheim) | 44 | `Alfheim.md` |

### Peoples & races

| Page | ~words | File |
|------|-------:|------|
| [Elfi](https://worldofymir.fandom.com/wiki/Elfi) | 457 | `Elfi.md` |
| [Fate](https://worldofymir.fandom.com/wiki/Fate) | 127 | `Fate.md` |
| [Gnomi](https://worldofymir.fandom.com/wiki/Gnomi) | 76 | `Gnomi.md` |

### Creatures & monsters

| Page | ~words | File |
|------|-------:|------|
| [Creature](https://worldofymir.fandom.com/wiki/Creature) | 1,548 | `Creature.md` |
| [Abominii](https://worldofymir.fandom.com/wiki/Abominii) | 768 | `Abominii.md` |
| [Draghi](https://worldofymir.fandom.com/wiki/Draghi) | 422 | `Draghi.md` |
| [Ibridi](https://worldofymir.fandom.com/wiki/Ibridi) | 89 | `Ibridi.md` |

### Items, materials & equipment

| Page | ~words | File |
|------|-------:|------|
| [Armi](https://worldofymir.fandom.com/wiki/Armi) | 2,690 | `Armi.md` |
| [Metalli e Pietre](https://worldofymir.fandom.com/wiki/Metalli_e_Pietre) | 1,325 | `Metalli e Pietre.md` |
| [Erbe](https://worldofymir.fandom.com/wiki/Erbe) | 761 | `Erbe.md` |
| [Armature e Scudi](https://worldofymir.fandom.com/wiki/Armature_e_Scudi) | 448 | `Armature e Scudi.md` |
| [Materiali](https://worldofymir.fandom.com/wiki/Materiali) | 415 | `Materiali.md` |

### Campaign reports (session write-ups)

| Page | ~words | File |
|------|-------:|------|
| [Gate to Unknown](https://worldofymir.fandom.com/wiki/Gate_to_Unknown) | 7,718 | `Gate to Unknown.md` |
| [A Steamclad Sky](https://worldofymir.fandom.com/wiki/A_Steamclad_Sky) | 7,615 | `A Steamclad Sky.md` |
| [A Black Sun Rising](https://worldofymir.fandom.com/wiki/A_Black_Sun_Rising) | 1,612 | `A Black Sun Rising.md` |
| [La Leggenda delle Rune Magiche](https://worldofymir.fandom.com/wiki/La_Leggenda_delle_Rune_Magiche) | 1,562 | `La Leggenda delle Rune Magiche.md` |
| [2011 - Back to war!](https://worldofymir.fandom.com/wiki/2011_-_Back_to_war!) | 219 | `2011 - Back to war!.md` |
| [La caduta di Helgedad](https://worldofymir.fandom.com/wiki/La_caduta_di_Helgedad) | 22 | `La caduta di Helgedad.md` |

### Wiki front matter

| Page | ~words | File |
|------|-------:|------|
| [World of Yimir Wiki](https://worldofymir.fandom.com/wiki/World_of_Yimir_Wiki) | 995 | `World of Yimir Wiki.md` |
| [Glossario](https://worldofymir.fandom.com/wiki/Glossario) | 319 | `Glossario.md` |

### Uncategorised on the wiki

| Page | ~words | File |
|------|-------:|------|
| [Oggetti Vari](https://worldofymir.fandom.com/wiki/Oggetti_Vari) | 3,316 | `Oggetti Vari.md` |
| [Religione Mithraica](https://worldofymir.fandom.com/wiki/Religione_Mithraica) | 1,417 | `Religione Mithraica.md` |
| [Scritti e Pergamene](https://worldofymir.fandom.com/wiki/Scritti_e_Pergamene) | 1,169 | `Scritti e Pergamene.md` |
| [PG di Ymir](https://worldofymir.fandom.com/wiki/PG_di_Ymir) | 945 | `PG di Ymir.md` |
| [Xebechani](https://worldofymir.fandom.com/wiki/Xebechani) | 942 | `Xebechani.md` |
| [Terra dei Sogni](https://worldofymir.fandom.com/wiki/Terra_dei_Sogni) | 712 | `Terra dei Sogni.md` |
| [Staffe, bacchette e bastoni](https://worldofymir.fandom.com/wiki/Staffe,_bacchette_e_bastoni) | 667 | `Staffe, bacchette e bastoni.md` |
| [Xidhe](https://worldofymir.fandom.com/wiki/Xidhe) | 642 | `Xidhe.md` |
| [Ur-Tanoth](https://worldofymir.fandom.com/wiki/Ur-Tanoth) | 610 | `Ur-Tanoth.md` |
| [Xudra](https://worldofymir.fandom.com/wiki/Xudra) | 582 | `Xudra.md` |
| [Xattva](https://worldofymir.fandom.com/wiki/Xattva) | 573 | `Xattva.md` |
| [Tal-Tanoth](https://worldofymir.fandom.com/wiki/Tal-Tanoth) | 561 | `Tal-Tanoth.md` |
| [Xion](https://worldofymir.fandom.com/wiki/Xion) | 558 | `Xion.md` |
| [Razze](https://worldofymir.fandom.com/wiki/Razze) | 494 | `Razze.md` |
| [Religione Elfi](https://worldofymir.fandom.com/wiki/Religione_Elfi) | 441 | `Religione Elfi.md` |
| [Società e Corporazioni](https://worldofymir.fandom.com/wiki/Società_e_Corporazioni) | 435 | `Società e Corporazioni.md` |
| [The Monster Mash](https://worldofymir.fandom.com/wiki/The_Monster_Mash) | 401 | `The Monster Mash.md` |
| [Nani](https://worldofymir.fandom.com/wiki/Nani) | 355 | `Nani.md` |
| [Stili Arti Marziali](https://worldofymir.fandom.com/wiki/Stili_Arti_Marziali) | 277 | `Stili Arti Marziali.md` |
| [Umani - Primigeni](https://worldofymir.fandom.com/wiki/Umani_-_Primigeni) | 233 | `Umani - Primigeni.md` |
| [Stili di Combattimento Armato](https://worldofymir.fandom.com/wiki/Stili_di_Combattimento_Armato) | 227 | `Stili di Combattimento Armato.md` |
| [Vlatch](https://worldofymir.fandom.com/wiki/Vlatch) | 222 | `Vlatch.md` |
| [Tchyo](https://worldofymir.fandom.com/wiki/Tchyo) | 205 | `Tchyo.md` |
| [Xebech](https://worldofymir.fandom.com/wiki/Xebech) | 178 | `Xebech.md` |
| [Mezze Razze](https://worldofymir.fandom.com/wiki/Mezze_Razze) | 176 | `Mezze Razze.md` |
| [Regni Giovani](https://worldofymir.fandom.com/wiki/Regni_Giovani) | 172 | `Regni Giovani.md` |
| [Sadhir](https://worldofymir.fandom.com/wiki/Sadhir) | 168 | `Sadhir.md` |
| [Religione Sohleugir](https://worldofymir.fandom.com/wiki/Religione_Sohleugir) | 164 | `Religione Sohleugir.md` |
| [Regni Belligeranti](https://worldofymir.fandom.com/wiki/Regni_Belligeranti) | 144 | `Regni Belligeranti.md` |
| [Sohleugir](https://worldofymir.fandom.com/wiki/Sohleugir) | 144 | `Sohleugir.md` |
| [Ophiur](https://worldofymir.fandom.com/wiki/Ophiur) | 140 | `Ophiur.md` |
| [Umani - Uomini](https://worldofymir.fandom.com/wiki/Umani_-_Uomini) | 132 | `Umani - Uomini.md` |
| [Zohàriti](https://worldofymir.fandom.com/wiki/Zohàriti) | 105 | `Zohàriti.md` |
| [Religione](https://worldofymir.fandom.com/wiki/Religione) | 104 | `Religione.md` |
| [Religione Nani](https://worldofymir.fandom.com/wiki/Religione_Nani) | 84 | `Religione Nani.md` |
| [Razze Degenerate](https://worldofymir.fandom.com/wiki/Razze_Degenerate) | 59 | `Razze Degenerate.md` |
| [Tanoth](https://worldofymir.fandom.com/wiki/Tanoth) | 25 | `Tanoth.md` |
| [Main Page *(redirect)*](https://worldofymir.fandom.com/wiki/Main_Page) | 5 | `Main Page.md` |
