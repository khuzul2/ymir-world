# Ymir — Conflicts, Unclear Points & Blind Spots

The single register of everything that needs a decision before (and during) the manual.
Migrated out of `NOTES.md` and expanded by a full re-audit of the extracted corpus.

## How this works
- Each entry has an **ID**, a **type**, a **severity**, the **sources** that clash, 2–3
  **options**, and my **recommendation**. **Decision** stays blank until you choose.
- **Type:** `conflict` (sources disagree) · `unclear` (ambiguous/underspecified) ·
  `blind-spot` (missing, and its absence would break coherence — mystery that *doesn't*
  break anything is left alone on purpose).
- **Severity:** `high` (blocks a coherent bible / the "present") · `med` · `low` (cosmetic).
- **Status:** `OPEN` → `DECIDED` (with your call recorded in **Decision**).
- We walk these one at a time; your decisions get written into the relevant `canon/` files.

## Status board
_(filled in as we go; IDs are grouped COS / HIS / GEO / RAC / MAG / META)_

| ID | Title | Type | Sev | Status |
|----|-------|------|-----|--------|
| COS-1 | Public myth vs. the Great Lie — official line | conflict | high | OPEN |
| COS-2 | Which Catastrophe account is true | conflict | high | OPEN |
| COS-3 | Demon origin: Corrupted Essence vs. Plane of Chaos | conflict | med | OPEN |
| COS-4 | Are the six Elemental Gods the Adepti? | conflict | med | OPEN |
| COS-5 | Yogh in two pantheons | conflict | low | OPEN |
| COS-6 | Moons: one (Ishtar) vs. the red moon | unclear | low | OPEN |
| COS-7 | Helgedad Seamark's third goddess | conflict | low | OPEN |
| COS-8 | Valrin: god or bound-demon class | unclear | low | OPEN |
| COS-9 | Outer Gods as a third cosmic axis | unclear | low | OPEN |
| HIS-1 | The "present": 3027 vs. 3260 vs. ~3500 | conflict | high | OPEN |
| HIS-2 | Armora's rulers: Leonius vs. Vespertina | conflict | med | OPEN |
| HIS-3 | Morannagul's reign dates | conflict | low | OPEN |
| HIS-4 | Cartosa's sitting prince | conflict | low | OPEN |
| HIS-5 | Identity of the "two unnamed adventurers" | blind-spot | med | OPEN |
| GEO-1 | Sadhir: humans vs. Sarradhi lizardfolk | conflict | high | OPEN |
| GEO-2 | Qi-Long: six kingdoms vs. one empire | conflict | high | OPEN |
| GEO-3 | World-map vs. prose placement | conflict | med | OPEN |
| GEO-4 | Unnamed world-map regions | blind-spot | low | OPEN |
| RAC-1 | Creation myths vs. engineered-race truth | conflict | med | OPEN |
| RAC-2 | Playable-races set | unclear | med | OPEN |
| RAC-3 | Elf faction/sub-race taxonomy applied cleanly | unclear | low | OPEN |
| MAG-1 | Dragon origin: Great Worms vs. Adepti-made | conflict | med | OPEN |
| MAG-2 | Demon classification: Circles vs. Types vs. status | conflict | med | OPEN |
| MAG-3 | Magic realms: 4 realms vs. Arcano/Elementalism | unclear | med | OPEN |
| META-1 | Spelling: Ymir vs. Yimir | conflict | low | OPEN |
| META-2 | Currency units (ma/mb/mr/mo) undefined | blind-spot | low | OPEN |
| META-3 | Source authority when sources fork | unclear | high | OPEN |
| META-4 | System span: Rolemaster + D&D 4e → agnostic | unclear | low | OPEN |
| META-5 | "la Marea" / Maelstrom / Era della Marea naming | conflict | low | OPEN |

> Additional items from the re-audit are appended below the migrated set as they land.

---

# COSMOLOGY & THE GREAT LIE

### COS-1 · `conflict` · `high` · Public myth vs. the Great Lie — what's the official line?
- **What clashes:** The public creation myth (Ech → Mithra/Ahriman → six Twins) and the
  secret (the "gods" are the alien **Adepti**, who sealed the real **Ancient/Outer Gods**).
  These aren't a data conflict so much as a **design decision**: how "true" is the Great Lie?
- **Sources:** `cosmology.md` / `pantheon.md` (public) vs. `secret-the-great-lie.md`
  (welcome-page.txt, cosmologia.txt).
- **Options:** A) The Great Lie is **the settled hidden truth** (public myth is false).
  B) The Great Lie is **one leading theory** among several the manual keeps ambiguous.
  C) A **hybrid**: the Adepti are real usurpers, but real gods also exist (both layers true).
- **Recommendation:** A — commit to it as the GM-secret truth; it's the richest and the
  homepage states it outright. (C is a strong second if you want the gods to be *real* too.)
- **Decision:** _(pending)_

### COS-2 · `conflict` · `high` · Which Catastrophe account is canon?
- **What clashes:** Three tellings — (1) the Adepti **stole the Ancient Gods' power**;
  (2) they **botched an Outer-God evocation**; (3) they **accidentally summoned the
  Sovereign Demons** (the Player-Guide public myth). All end in the Maelstrom.
- **Sources:** welcome-page.txt / dei-esterni.txt / Player Guide, via `secret-the-great-lie.md`, `history.md`.
- **Options:** A) (1) is the truth, (3) is the public cover-story, (2) a garbled variant.
  B) Keep all three as in-world competing legends (no official truth). C) Merge: the theft
  ritual *is* what tore the seal and let the demons in — one event, three partial views.
- **Recommendation:** C — a single event that all three accounts describe partially; elegant
  and preserves every source.
- **Decision:** _(pending)_

### COS-3 · `conflict` · `med` · Demon origin: Corrupted Essence vs. the Plane of Chaos
- **What clashes:** Demons arise from **Essenza Corrotta** (welcome-page) vs. from the
  **Piano del Caos** and its "Sei Signori del Caos" (i-demoni-su-ymir.txt).
- **Sources:** `secret-the-great-lie.md`, `cosmology.md`.
- **Options:** A) Corrupted Essence is primary; the Plane of Chaos is *where* it pools
  (same thing, two names). B) Two distinct demon-origins (Ahriman's demons vs. Chaos-lords).
  C) Drop the Plane of Chaos as a superseded draft.
- **Recommendation:** A — unify them: the Plane of Chaos = the realm of Corrupted Essence.
- **Decision:** _(pending)_

### COS-4 · `conflict` · `med` · Are the six Elemental Gods actually the Adepti?
- **What clashes:** Public myth: the six Twins were **born from** Mithra & Ahriman. Heresy in
  the sources: the six Elemental Gods **are** the Adepti who stole divine power.
- **Sources:** cosmologia.txt / divinit-elementali.txt via `secret-the-great-lie.md`, `pantheon.md`.
- **Options:** A) The Elemental Gods are Adepti wearing divine masks (secret truth).
  B) Only Mithra/Ahriman are Adepti; the Twins are real (lesser) powers. C) All the "gods"
  including the Twins are Adepti.
- **Recommendation:** C, consistent with COS-1/A — the whole worshipped pantheon is Adepti.
- **Decision:** _(pending)_

### COS-5 · `conflict` · `low` · Yogh appears in two pantheons
- **What clashes:** **Yogh** (spider-god of poison/assassination) is listed under both the
  **Mithraic** pantheon (religione-mithraica) and the **Xebechani** pantheon (Player Guide).
- **Sources:** `pantheon.md`, `geography.md` (Ulan-Tang).
- **Options:** A) One god worshipped by both cultures under one name. B) Two distinct
  entities that share a name. C) Yogh is properly Xebechani; the Ulan-Tang cult is imported.
- **Recommendation:** A — a single cross-cultural god (fits Ulan-Tang's corruption theme).
- **Decision:** _(pending)_

### COS-7 · `conflict` · `low` · Helgedad's Seamark third goddess
- **What clashes:** Seamark's maternal triad is **Hudemia, Diis, Thal'Khal** (Helgedad.doc)
  vs. **Hudemia, Diis, Kur** (wiki).
- **Sources:** `pantheon.md`, `geography.md`, Helgedad digest.
- **Options:** A) **Thal'Khal** (a local goddess; keeps the regional flavour). B) **Kur**
  (already in the main pantheon; fewer new gods). C) Thal'Khal is a Seamark by-name for Kur.
- **Recommendation:** C — Thal'Khal = the Seamark cult-name of Kur; satisfies both.
- **Decision:** _(pending)_

### COS-6 · `unclear` · `low` · Moons — one or two?
- **What clashes:** **Ishtar** is "goddess of the Moon" (implying one), but the Cartosa
  timeline features a portentous **red moon** (3026).
- **Sources:** `calendar.md`, `pantheon.md`, `history.md`.
- **Options:** A) One moon that *reddens* as an omen. B) Two moons (one is the omen-moon /
  the waking Outer God's eye). C) The "red moon" is Sguardo-sul-Nulla, not a moon at all.
- **Recommendation:** C — tie the red moon to the Observer's awakening (already half-canon).
- **Decision:** _(pending)_

### COS-8 · `unclear` · `low` · Valrin — a god or a class of bound demon?
- **What clashes:** **Valrin** is both the Dark Elves' **warrior god** of the holy war and
  their **word for bound extraplanar "Forces" (demons)**.
- **Sources:** `pantheon.md`, `peoples.md` (Dark Elves).
- **Options:** A) One divine name applied to both the god and his servitor-forces (deliberate).
  B) Two unrelated uses of the word — rename one. C) The "Forces" are aspects/avatars of the god.
- **Recommendation:** A/C — the bound Forces are named for (and serve) the war-god Valrin.
- **Decision:** _(pending)_

### COS-9 · `unclear` · `low` · Is Sguardo-sul-Nulla an axis outside the Ech duality?
- **What clashes:** The Ech→Mithra/Ahriman duality is the public frame, but **Sguardo-sul-Nulla
  / Xhulhu** reads as an **Outer God** — a third, older cosmic axis.
- **Sources:** `pantheon.md`, `cosmology.md`, `secret-the-great-lie.md`.
- **Options:** A) Yes — the Outer/Ancient Gods are a **third axis** predating the Ech duality
  (which is itself an Adepti fiction). B) No — fold the Outer Gods into the existing duality.
  C) The Outer Gods are **beyond** the duality entirely (neither good nor evil, just *other*).
- **Recommendation:** A+C — the Ancient Gods precede and stand outside the (fake) duality; this
  is the engine of the Great Lie's horror.
- **Decision:** _(pending)_

---

# HISTORY & TIMELINE

### HIS-1 · `conflict` · `high` · When is "the present"?
- **What clashes:** **EM 2 = 3027 d.M.** (Libro Rosso) vs. **Bocca del Caos 3026–3260** vs.
  "current ≈ **3500 d.M.**" Different sources put the "now" centuries apart.
- **Sources:** `history.md`, `calendar.md`, cosmology digest.
- **Options:** A) Present = **~EM 2 / 3027** (freshest, best-attested; the Tide just broke).
  B) Present = **~3260** (end of the Bocca del Caos era — the Tide's aftermath settled).
  C) Present = **~3500** (a later stabilised age; treat 3027 material as recent history).
- **Recommendation:** A — the manual is most dramatic at the moment of upheaval; later dates
  become "possible futures."
- **Decision:** _(pending)_

### HIS-2 · `conflict` · `med` · Armora's ruler at the present
- **What clashes:** **Leonius VonGriffen** (schism with Letia + war) vs. **Vespertina
  VonGriffen** (reconciles with Letia vs. the orcs).
- **Sources:** `history.md`, `characters.md`, Armora docs / lera-della-marea.txt.
- **Options:** A) **Succession** — Leonius now, Vespertina his heir who later reconciles
  (depends on HIS-1's present). B) Vespertina rules now; Leonius is past. C) They co-rule /
  rival claimants during the chaos.
- **Recommendation:** A — cleanest; pin which one is "now" once HIS-1 is set.
- **Decision:** _(pending)_

### HIS-3 · `conflict` · `low` · Morannagul's reign dates
- **What clashes:** Gaerwath "unified under Morannagul **2550**" vs. wiki reign **2198–3131**.
- **Sources:** `history.md`, `peoples.md`, geography digest.
- **Options:** A) 2550 = the *unification*; 2198–3131 = his (very long, elf/undying) reign.
  B) One date is an error; pick 2550. C) He's "Morannagul l'Eterno" — an undying ruler, so
  the long span is literal.
- **Recommendation:** A+C — unification 2550 within an eternal reign; fits "l'Eterno."
- **Decision:** _(pending)_

### HIS-4 · `conflict` · `low` · Who sits the throne of Cartosa?
- **What clashes:** Gazetteer: Prince **Rodriguez XIII** (heir Alberto V). Timeline: **Alberto
  V** accedes in **3017**.
- **Sources:** `characters.md`, `history.md`.
- **Options:** A) Book written just before Alberto's 3017 accession; at the present, **Alberto
  V reigns**. B) Keep Rodriguez XIII if present < 3017. C) Two different in-world "presents."
- **Recommendation:** A — Alberto V reigns at EM 2.
- **Decision:** _(pending)_

### HIS-5 · `blind-spot` · `med` · Who are the "two unnamed adventurers" who opened the Tide?
- **What clashes:** Canon says two unnamed adventurers used the six Relics; the campaign logs
  imply the **A Steamclad Sky** party (and/or the villain **Leonard**).
- **Sources:** `history.md`, history-campaigns digest.
- **Options:** A) Canonise the **Steamclad Sky PCs** as the two (name them). B) Keep them
  **deliberately unnamed** (mystery). C) It was the **villain Leonard** + a bound entity.
- **Recommendation:** B unless you want your PCs enshrined — then A. Low stakes, your call.
- **Decision:** _(pending)_

---

# GEOGRAPHY

### GEO-1 · `conflict` · `high` · Sadhir — human city-states or Sarradhi lizardfolk?
- **What clashes:** Wiki `sadhir.txt`: human cities (Al-Jasul/Al-Sidath), **no lizardfolk**.
  English `Sadhir_Compiled_Gazetteer.docx`: a **matriarchal Sarradhi lizardfolk sultanate**
  (Zarash-Sur, Kalzharan…). Two incompatible pictures of the same region.
- **Sources:** `geography.md`, geography digest, Sadhir gazetteer.
- **Options:** A) **Gazetteer wins** — Sarradhi sultanate is canon (richer, self-consistent);
  fold the human cities in as subject/independent settlements. B) **Wiki wins** — human
  Sadhir; treat the gazetteer as a non-canon reimagining. C) **Layered** — humans ruled the
  old Sadhir; the Sarradhi rose after the sea dried (a timeline that lets both be true).
- **Recommendation:** C — the "inland sea dried into desert" event is a natural hinge that
  makes both accounts sequential rather than contradictory.
- **Decision:** _(pending)_

### GEO-2 · `conflict` · `high` · Qi-Long — six independent kingdoms or one empire?
- **What clashes:** Wiki `qi-long.txt`: **six independent warring kingdoms**, each with its
  own Dragon-God. `Onore e Memoria`.docx: **one empire**, hidden Dragon-God emperor at
  Tianqi, six **sect**-governed provinces.
- **Sources:** `geography.md`, `factions.md`, geography digest, Qi-Long docx + maps.
- **Options:** A) **One empire** (the docx + the maps back it; the six "kingdoms" = the six
  provinces/sects). B) **Six kingdoms** (post-imperial fracture; the emperor is a figurehead
  or myth). C) **Timeline split** — empire historically, fracturing into six by the present.
- **Recommendation:** A or C — the empire framing is map-backed; C lets the Tide be the thing
  that's fracturing it "now."
- **Decision:** _(pending)_

### GEO-3 · `conflict` · `med` · The hand-drawn world map vs. the prose
- **What clashes:** Helgedad reads as "far north" but its cities (Talwar/Kelhar) sit
  **south-east** on the world map; region placements generally don't line up with the text.
- **Sources:** `geography.md`, `sources/maps/`.
- **Options:** A) **Prose wins**; treat the hand-map as a rough, mislabelled sketch and
  commission a clean map. B) **Map wins**; rewrite directional prose to match. C) The map is
  one hemisphere/oriented differently; reconcile case-by-case.
- **Recommendation:** A — prose + a new clean canonical map we build from the reconciled facts.
- **Decision:** _(pending)_

### GEO-4 · `blind-spot` · `low` · Unnamed regions on the world map
- **What clashes:** Map labels with no prose: Xuthal, Itza, U-aj-tanis, Sathe, Luveburk,
  Hibernia, Ljone del Saos, Al-Sidah, Cariba, etc.
- **Sources:** `sources/maps/world-map-ymir.png`, `geography.md`.
- **Options:** A) Leave them as unexplored frontier (mystery — fine). B) Assign the obvious
  ones (e.g., Solanthya = Letia's seat) and invent brief gazetteer stubs for the rest.
  C) Ask you/your friends what these were in play.
- **Recommendation:** A for most (frontier is good), C for any that saw play.
- **Decision:** _(pending)_

---

# PEOPLES & RACES

### RAC-1 · `conflict` · `med` · Creation myths vs. the engineered-race truth
- **What clashes:** Each race's myth (Niethel, Durkaam, the Ancestors) vs. the secret that
  they're **Adepti bio-engineering** across a galactic empire.
- **Sources:** `peoples.md`, `secret-the-great-lie.md`, peoples digest.
- **Options:** A) Myths are **in-world false beliefs**; engineered truth is the secret (parallels
  COS-1/A). B) Myths are **literally true**; the "engineered" account is Adepti propaganda.
  C) Both partly true (the Adepti *shaped* peoples who already existed).
- **Recommendation:** A — consistent with the Great Lie; each race's myth becomes a
  beautiful in-world error.
- **Decision:** _(pending)_

### RAC-2 · `unclear` · `med` · Which races are playable?
- **What clashes:** Undecided. Sources imply a "core seven Pure Races" + many exotics/half-races.
- **Sources:** `races-index.md`.
- **Options:** A) **Core seven** (Humans, Xebechani, Dwarves, Elves, Folletti, Tal-Tanoth,
  Sohleugir) standard; rest exotic/GM-discretion. B) Core seven **only**. C) Wide-open
  (include Sarradhi, half-races, etc. as standard).
- **Recommendation:** A — the default from the Player Guide; flexible without sprawl.
- **Decision:** _(pending)_

### RAC-3 · `unclear` · `low` · Is the elf faction/sub-race split applied cleanly?
- **What clashes:** Factions (Chiari/Illuminati/Oscuri) are orthogonal to sub-races
  (Alti/Silvani/Grigi/marini); earlier canon conflated "Grey = moderates."
- **Sources:** `peoples.md`.
- **Options:** A) Adopt the orthogonal model everywhere (done in `peoples.md`; verify the rest).
  B) Simplify to just the three factions for the player-facing text. C) Keep both axes but add
  a table so it's legible.
- **Recommendation:** A + C — orthogonal model with a clarifying table in the manual.
- **Decision:** _(pending)_

---

# MAGIC & CREATURES

### MAG-1 · `conflict` · `med` · Dragon origin — primordial Great Worms or Adepti-made?
- **What clashes:** "**Grandi Vermi** appear at the world's dawn" vs. "**20 True Dragons
  engineered by the Adepti** as living weapons."
- **Sources:** `bestiary.md`, `cosmology.md`, creatures digest, `secret-the-great-lie.md`.
- **Options:** A) The dawn Great Worms are the **wild stock** the Adepti later engineered the
  20 True Dragons from. B) Two separate lineages (primordial worms vs. made dragons).
  C) "Dawn Great Worms" is myth; the Adepti origin is the truth (parallels the Great Lie).
- **Recommendation:** A — one lineage, engineered from primordial stock; keeps both facts.
- **Decision:** _(pending)_

### MAG-2 · `conflict` · `med` · Demon classification & count
- **What clashes:** Demons are ranked in **six Circles** + "Beyond the Circles," but a creature
  is tagged "**VI tipo**" (Type VI); and the Sovereign roster is ~18 yet only 3 survive the Tide.
- **Sources:** `bestiary.md`, `pantheon.md`, creatures digest.
- **Options:** A) "Type VI" = "sixth Circle" (same scale, sloppy label) — normalise to Circles.
  B) Types and Circles are two different systems (power tier vs. hierarchy). C) Drop "Types."
- **Recommendation:** A — one scale (Circles), treat "Type VI" as sixth-Circle.
- **Decision:** _(pending)_

### MAG-3 · `unclear` · `med` · How many magic realms, and where does "Arcano" sit?
- **What clashes:** The Libro Rosso gives **four** realms (Mentalismo, Flusso, Essenza,
  Corrotti); elsewhere Cartosa registers **Essenza / Mentalismo / Arcano**; plus Elementalism.
- **Sources:** `magic.md`.
- **Options:** A) Four realms are canonical; "Arcano" = the unified/high realm (Rolemaster
  Arcane), Elementalism = a branch of Essenza. B) Realms = Essence/Mentalism/Channeling(Flusso)/
  Arcane; "Corrotti" is a corruption *state*, not a realm. C) Present magic thematically
  (no realm-system) since the manual is system-agnostic.
- **Recommendation:** B for the in-world model + C for presentation — describe the realms as
  traditions, with "Corrotti" as corruption, and keep mechanics out.
- **Decision:** _(pending)_

---

# META / CROSS-CUTTING

### META-1 · `conflict` · `low` · Spelling: Ymir vs. Yimir
- **What clashes:** Both spellings appear across sources.
- **Options:** A) **Ymir** everywhere (already standard). B) Yimir. C) Ymir with an in-world
  note that Yimir is an archaic/regional spelling.
- **Recommendation:** A (optionally C as flavour).
- **Decision:** _(pending)_

### META-2 · `blind-spot` · `low` · Currency is never defined
- **What clashes:** Prices use **ma / mb / mr / mo** with no defined system.
- **Sources:** Cartosa/Maraviglie/magic digest.
- **Options:** A) Define a simple coinage (e.g., mo=gold, ma=silver, mb=bronze, mr=copper) in
  an appendix. B) Leave money abstract/region-specific. C) Ask if there was a set system.
- **Recommendation:** A — a light standard coinage in the appendix; confirm the letters with you.
- **Decision:** _(pending)_

### META-3 · `unclear` · `high` · Source authority when sources disagree
- **What clashes:** We have the **wiki**, an **English "compiled" gazetteer**, the original
  **PDFs/DOCs**, and **D&D-4e-tagged** files — and they fork (Sadhir, Qi-Long, dates…).
- **Options:** A) Precedence order: **original PDFs/Player Guide > wiki > compiled gazetteer >
  4e files** (oldest-official first). B) **Wiki is newest/most-complete → wins.** C) Case-by-case
  by which is richer/more-consistent (what I've been doing).
- **Recommendation:** A as a default tie-breaker, overridable case-by-case — and you're the
  final arbiter. **Deciding this resolves many downstream forks at once.**
- **Decision:** _(pending)_

### META-5 · `conflict` · `low` · "la Marea" vs. "il Maelstrom" vs. "Era della Marea"
- **What clashes:** The Dark-Elf doc references "**la Marea**" as a *past* cutting-off event;
  the era **d.M.** = *dopo il Maelstrom*; the current **Era della Marea** is a *later* event.
  Risk of three "Marea/Maelstrom" meanings blurring.
- **Sources:** `peoples.md` (Dark Elves), `calendar.md`, `history.md`.
- **Options:** A) The Dark Elves' "la Marea" **is** the Era-della-Marea Bewitched Tide (they
  name the current cataclysm). B) It's a *separate* regional term for the Maelstrom's original
  isolation. C) Rename in the manual to keep the three distinct (Maelstrom / Isolation / Tide).
- **Recommendation:** A + C — treat it as the Bewitched Tide, and use crisp distinct names in
  the manual to avoid confusion.
- **Decision:** _(pending)_

### META-4 · `unclear` · `low` · The material spans Rolemaster and D&D 4e
- **What clashes:** Sources carry both Rolemaster and D&D-4e mechanics; the manual is to be
  system-agnostic.
- **Options:** A) Strip **all** mechanics; describe everything in plain setting terms (agreed
  direction). B) Keep light stat hooks in an appendix. C) Produce a system-agnostic core + an
  optional conversion appendix.
- **Recommendation:** A (with C as a possible later add-on).
- **Decision:** _(pending)_

---

## Re-audit additions
_(populated from the five domain audits — appended below once merged)_
