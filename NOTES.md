# NOTES — Open questions, gaps & contradictions

Working memory of the project. Items move out of here into `canon/` once settled.

## Legend
- ❓ **Open question** — needs an answer from you/your friends.
- 🕳️ **Gap** — the world needs this and no source covers it (candidate to invent).
- ⚔️ **Contradiction** — sources disagree; needs reconciliation.
- ✅ **Resolved** — settled; recorded here, then folded into canon.
- 📥 **Source** — a body of material imported into `sources/`.

---

## ✅ Resolved

### From Alessandro (2026-07-07)
- ✅ **Game system.** Played in **Rolemaster (RMSS/RMFRPG)**. The manual must be
  **system-agnostic** — describe the world, not the rules. Source docs (and the wiki)
  carry RM artefacts (TP/Training Packages, AF/AT, PF/hit points, BO/OB, "R&C" =
  *Races & Cultures*, the Essence/Mentalism/Channeling/Arcane realms); these get
  translated to plain setting language and mechanics stripped out. Logged in
  `magic.md`, `peoples.md`, `bestiary.md`, `items.md`.
- ✅ **"Ymir"** is simply the **name of the world** (not the Norse god). (Many sources
  — and the entire Fandom wiki — spell it "Yimir"; we standardise on **Ymir**. See
  Contradictions below.)
- ✅ **History** is to be **rebuilt** — but the sources preserve a LOT of it. A full
  master timeline (Forgotten Times → Era della Marea) is in `history.md`.
- ✅ **Tone.** High fantasy, deliberately **varied by region** — theocratic (Letia),
  steampunk/technocratic (Armora), eastern honour-culture (Qi-Long), grimdark
  (Helgedad), swashbuckling (Cartosa), alien/reptilian (Xebech), dark-demonic
  (Gaerwath). Regional-flavour is a manual design directive. Logged in `geography.md`.
- ✅ **Contributors** — treat the project as **independent** of how many people/
  campaigns fed it. (We still tag which *document/wiki page* a fact came from.)

### Resolved by the wiki extraction (2026-07-07)
- ✅ **The elves' three factions.** The "first faction" (return-home party) is the
  **Elfi Chiari (Light Elves)**, awaiting the *Ultimo Messaggero* in Alfheim; the
  moderates are the **Elfi Illuminati / Rinuncianti** (not the Grey Elves); the third
  are the **Elfi Oscuri (Dark Elves)**. The factions ("**Nhos**") cut *across* three
  orthogonal sub-races (Alti/Silvani/Grigi). Folded into `peoples.md`, `pantheon.md`.
- ✅ **The Primigeni humans.** Fire-born mythic progenitors, corrupted by an evil god,
  now near-extinct; the "Xebechani mysticism" link is confirmed. In `peoples.md`.
- ✅ **Famous player characters recorded.** The long-wanted roster of canonised PCs is
  now in `characters.md` — **~42 PCs** from *PG di Ymir* plus **~70 named figures**
  harvested from the six campaign chronicles.
- ✅ **A magic-item / materials corpus exists** and now has its own file `items.md`
  (named artefact weapons, the magic metals & stones, herbs, scrolls, wonders).

## Design directives (for the manual)
- Single **layered world bible**: player-facing text + boxed **GM-only** sections.
- **Regional flavour is a feature** — lean into the tonal contrast between regions.
- Keep the **canon/invented ledger** honest (`[CANON]`/`[INFERRED]`/`[INVENTED]`/
  `[CONFLICT]` tags throughout).

## 📥 Sources imported
- 📥 **13 legacy documents** (Player Guide, Cartosa Guida, Storia Letio, the regional
  docs, LIBRO ROSSO, etc.) — in `sources/raw/` + `sources/extracted/`.
- 📥 **Fandom wiki, fully imported AND mined into canon (2026-07-07).** The whole
  *World of Yimir Wiki* (75 pages, ~62k words) is in `sources/*/wiki-worldofymir/`,
  and its content has now been extracted into every `canon/` topic file (first pass).
  Remaining depth work is tracked under Gaps below.

## ❓ Foundational questions still open
- ❓ **Campaign present / "now".** Candidates: the **~3025 d.M.** "Great War / Guerra
  delle Macchine" in the Young Kingdoms (where the Player Guide ends) or the post-seal
  **Era della Marea** frontier (portals reopening, the Bewitched Tide, three Sovereign
  Demons loose, a new demon-continent). Which is the manual's default present?
  - ⚠️ Complication surfaced by the wiki: several *PG di Ymir* entries carry
    **far-future in-world dates** (e.g. 3518 d.M.) while one campaign is tagged "2003"
    (almost certainly the real-world play year). We need to know which numbers are
    in-world canon before fixing the timeline's endpoint. → `characters.md`.
- ❓ **Manual language.** Sources are in **Italian** (campaign chronicles partly in
  English); you write to me in English. Italian, English, or bilingual? (Proper nouns
  stay as-is regardless.)
- ❓ **Playable scope.** Which races/regions are *playable* vs. setting colour? The
  wiki adds many candidate lineages (Ibridi, Mezze Razze, Abominii, the Xebechani
  castes) — several explicitly "with the GM's consent." → `peoples.md`.

## ⚔️ Contradictions logged

### Cosmology & the gods
- ⚔️ **Origin of the Elemental Gods.** Player Guide: the Six Divine Twins are **born
  of the Mithra/Ahriman contrast**. Wiki *Cosmologia*: a widespread **heresy** holds
  the six *are* the former **Adepti**, who seized divine power from — or defeated and
  exiled — the Ancient Gods (Dèi Esterni). → `pantheon.md`, `cosmology.md`.
- ⚔️ **Origin of Demons.** Player Guide states as fact that Ahriman made demons by
  corrupting Spirits; wiki *Entità* offers **three competing theories** (damned souls
  reincarnated / corrupted Spirits / incarnations of Dark Essence with their own
  will). Certainty vs. open debate. → `cosmology.md`.
- ⚔️ **Xhulhu vs Sguardo-sul-Nulla.** Earlier canon guessed the Xebechani god
  **Xhulhu** *was* the intruding outer god **Sguardo-sul-Nulla**. The wiki fixes
  Sguardo-sul-Nulla as the Outer God **Tuulhak-Xanar, "the Observer"** — so they now
  read as **distinct**. Also, "the Observer" is *also* the epithet of the Xebechani
  god **Heichpyel** (owl) — coincidence or mask? → `pantheon.md`.
- ⚔️ **"Il Disastro" = "La Catastrofe"?** Wiki *Dei Esterni*: the Disaster was caused
  by a botched **summoning of an Outer God**. Is this the same event as La Catastrofe
  (the birth of the Maelstrom)? Unconfirmed. → `pantheon.md`, `history.md`.
- ⚔️ **"Void beyond creation" vs "Spazio Esterno."** Player Guide's Void (Ahriman +
  demons) vs the wiki's Spazio/Vuoto Esterno (home of the exiled Ancient Gods) —
  same region or two? → `cosmology.md`.
- ❓ **Spirit plane vs Terra dei Sogni.** *Entità* conflates the Spirits' home with
  the "World of Dreams"; the *Terra dei Sogni* page describes a distinct Dreamlands
  ruled by the Outer Gods. One realm or two? → `cosmology.md`.

### The Sovereign Demons & the dragons
- ⚔️ **Sovereign Demon roster.** Player Guide table lists **Gaziel** (Lord of Wrath,
  bear) and gives **Abigor** a trident with no death-mark. Wiki *Entità* instead lists
  **Abbadon** (Lord of Torment, inverted trident — the very symbol the table gave
  Abigor: likely a **conflation**), gives Abigor an **axe**, gives **Ea** an **oyster**
  (not a kraken — corroborated by the *Ombra dell'Ostrica Blu*), and marks **six** dead
  (Abbadon, Abigor, Adramelek, Netunshiel, Ea, Saxul) vs the two the timeline dates.
  Which roster is authoritative? → `bestiary.md`, `pantheon.md`, `history.md`.
- ⚔️ **Dragon origins (three-way).** (a) primordial **Grandi Vermi** at the world's
  dawn; (b) top tier of natural **Hybrid Elementals** (`cosmology.md`); (c)
  **Adept-engineered bioweapons** set to guard Ymir's secrets (wiki *Draghi*, which
  also fixes the count at **20 True Dragons**). Reconcilable, but origin+dating are
  tangled. → `bestiary.md`, `cosmology.md`, `history.md`.

### History & dates
- ⚔️ **Elven schism: two or three groups?** Wiki *Cronologia* says the Anni della
  Discordia split the elves into **two**; the rest of canon (and the resolved faction
  scheme) says **three**. → `history.md`, `peoples.md`.
- ⚔️ **The 3025 war's name.** Player Guide "**the Great War**" vs wiki "**Guerra delle
  Macchine** (War of the Machines)" — same conflict, same factions, same start-year,
  two names. → `history.md`.
- ⚔️ **Morannagul's reign.** Existing canon: unified the Gaerwath in **2550 d.M.**
  Wiki: reigned **2198–3131 d.M.** → `geography.md`, `history.md`, `characters.md`.
- ⚔️ **Khorish/Korish.** Existing: founded 2160–2180 under **Athmokethepek I** alone.
  Wiki: **Korish**, founded ~end of the 23rd century, co-ruled with **Nefthi**.
  → `geography.md`, `history.md`.
- ⚔️ **Saxul's slayer.** Existing canon credits **Valdis Nemertine** (Battle of the
  Broken Land, 2563). *PG di Ymir* credits **Callidus's party** (incl. **Deedlit**).
  Same battle from the adventurers' side, or two events? → `characters.md`, `history.md`.

### Geography
- ⚔️ **Alfheim vs Al'Fehim.** Existing: independent light-elf forest kingdom under a
  queen (capital Ost-en-Galad). Wiki (*Al'Fehim*): a **Gaerwath protectorate** on
  Qi-Long's NW border and a chief **Black Lotus** producer. Same place over time, or
  two places sharing a name? → `geography.md`.
- ⚔️ **Qi-Long: split or unified?** Existing: fragmented into **6 kingdoms** with
  plural **Dei-Drago** after the Mah-Dhol fall. Wiki: a **single empire of 6
  provinces** under one **Dio-Drago** emperor at **Tianqi** — possibly a later
  re-unification. → `geography.md`, `history.md`.
- ⚔️ **Meridian: republic or city?** Existing: independent **Repubblica di Meridian**.
  The wiki treats Meridian as a river-port **city within the Principality** — reads
  like an annexation-era (2830–3023) snapshot. → `geography.md`.
- ⚔️ **Helgedad's capital.** Existing: capital **Nortislong**. Wiki: no island-wide
  capital (six self-standing marches), **Kelmar** the largest city; plus internal wiki
  inconsistencies on Nortislong's location. → `geography.md`.
- 🕳️ **Isola dei Demoni (Isle of Demons).** New body raised in the southern hemisphere
  by the 3026 Invasion / the demon-continent of the Era della Marea — location and
  extent unknown. → `geography.md`, `history.md`.

### Peoples
- ⚔️ **Grey Elves = sea elves?** Wiki equates "gli elfi marini o Grigi"; the Player
  Guide glossary seemed to distinguish them. Also: Grey Elves are a **sub-race**, not
  the moderate faction (see Resolved). → `peoples.md`.
- ⚔️ **Tanoth sub-races: two or three?** Wiki: a bestial/feline race with **only two**
  sub-races (Ur-/Tal-Tanoth). Existing canon had a distinct third "plains Tanoth."
  → `peoples.md`.
- ⚔️ **Mixed Men — majority or minority?** Wiki: **Uomini Misti** are the *minority*
  (trace Primigeno blood); **Uomini Comuni** are the majority. First-pass canon called
  Mixed Men the majority. → `peoples.md`.
- ❓ **Elf homeworld: Niethel or Tchyo?** Existing canon: the Source/**Niethel**. Wiki
  *Tchyo* presents a dying elven homeworld. Same place under two names, or two stages?
  → `peoples.md`, `cosmology.md`.

### Items
- ⚔️ **The Elemental Lords "still mortal."** *Sangue Elementale* (wiki: Oggetti Vari)
  says the six Twins were **still mortal** when their blood was taken to feed the
  ritual that caused the Cataclysm — clashing with their divine birth in
  `pantheon.md`/`cosmology.md`. → `items.md`.
- ❓ **Two "Wars of the Waves."** Items describe a mythic **elemental** Guerra delle
  Onde; `history.md` records a mundane Cartosa–Meridian naval war (2320–2350). Same
  event mythologised, or two? → `items.md`, `history.md`.
- ❓ **Kramer's identity.** "Mithran" inquisitor (existing) vs "**Letian**" inquisitor
  **Heinrich Kramer** (*PG di Ymir*), lich form **M'Raker**. Almost certainly one
  figure; framing to settle. → `characters.md`.

### Spelling variants to standardise
- ⚔️ **World name:** "Ymir" vs "Yimir" (the whole wiki uses "Yimir") → **Ymir**.
- Other variants seen: **Korish/Khorish**, **Al'Fehim/Alfheim**,
  **Sohleguir/Sohleugir**, **Ulan-Tang/Ulang-Tang**. Pick one spelling per name when
  drafting the manual.

## 🕳️ Gaps / next extraction pass
- 🕳️ **Maps.** Still no world map extracted; several PDFs/docs embed maps (Cartosa's
  "Mappa del Principato", Player Guide's 462 images). The wiki improved *relative*
  placement (e.g. Gaerwath + Silver Isles once joined the mainland; Al'Fehim borders
  Qi-Long) but absolute cardinal placement of Xebech, the deserts, and the elf lands
  still needs a map. **Priority.**
- 🕳️ **LIBRO ROSSO DEL CONTROLLO MAGICO** (52 pp.) — the deep magic-system doc, still
  not mined; the authoritative rules of casting/control/limits. → `magic.md`.
- 🕳️ **Qi-Long.docx** — the Dragon-Gods' full nature (and the split-vs-unified
  question) await it. → `geography.md`, `bestiary.md`.
- 🕳️ **Gaerwath "Società"** section (Dark-Elf society) and the **Sadhir** gazetteer
  are only partly mined. → `peoples.md`, `geography.md`.
- 🕳️ **Maraviglie.pdf**, **Edizione Straordinaria.pdf** — not yet mined; may add
  wonders, local cults, or setting-wide institutions.
- 🕳️ **Under-described wiki stubs** to chase if a source surfaces: the Ibridi types
  (Rahab, Tritoni, Centauri, Satiri, Giganti); the many Mezze Razze / Razze Degenerate;
  the True Dragons' individual lore; a stat-block "monster manual" implied behind the
  bestiary pages.
- 🕳️ **Reconcile the campaign chronicles** (Gate to Unknown, A Steamclad Sky, A Black
  Sun Rising, 2011 – Back to war!, La Leggenda delle Rune Magiche, La caduta di
  Helgedad) into the timeline once the in-world-date question is settled.
