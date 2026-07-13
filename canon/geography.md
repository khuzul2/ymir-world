# Geography

> The world and its regions. Ymir's regions are tonally distinct **by design** —
> each empire/kingdom has its own flair. Sources: the **world map** and three
> extracted maps (see `sources/maps/`), the **Player Guide** glossary, and the
> regional docs (**Cartosa Guida**, **Storia Letio**, **Helgedad**, **Gaerwath**,
> **Armora**, **Qi-Long**, **Sadhir**).

## Maps `[CANON — extracted, see sources/maps/]`
- **`world-map-ymir.png`** — hand-drawn world map (Player Guide frontispiece):
  many landmasses and island chains around a central ocean.
- **`regional-cartosa-principality.png`** — the Principato di Cartosa (two islands,
  ~20 settlements, 200 km scale).
- **`regional-qilong-provinces.png`** — colour map of the Qi-Long's six provinces.

`[CONFLICT/OPEN]` The world map's labels don't all match the prose names (e.g.
Helgedad's cities **Talwar/Kelhar** appear on a south-eastern island, though the
text calls Helgedad "one of the northernmost lands"). The hand-drawn map's
orientation and some spellings need reconciling with the docs — see `NOTES.md`.
Readable world-map labels include: **Armora** (central), **Khorish**, **Xuthal**,
**Itza**, **U-aj-tanis**, **Ljone del Saos**, **Solanthya**, **Hibernia**,
**Gwaerwath** (Gaerwath), **Sathe**, **Luveburk**, **Talwar/Kelhar**, **Meridian**,
**Cariba**, and a southern desert-continent (**Al-Jou, Al-Sidah, Gazal, Zabhola,
Tema-li, Ost-en-Mano, Dalkis, Thulos**).

### The Drive world-map layer `[CANON — ymir-drive: MAP-YMIR, MAP-ymirexplored (rasters in sources/raw/ymir-drive/maps/)]`
The Drive corpus contributes two large world maps (4429×2953 px, 2000 km scale bar) whose
**west→east layout** is canon map data:
- **Letia** — the large **western** continent; the **Regni Belligeranti** labelled as its
  **northern region** and the **Regni Giovani** as its **south-western arm** (both read as
  sub-regions of the Letia landmass — matching their history as Letio breakaways).
- **Cartosa & Meridian** — paired small islands **in the sea between Letia and Erg**.
- **Helgedad** — a **north-central** peninsula/isle (fits "coldest place on Ymir").
- **Erg** — the large **central** continent, with **Sadhir labelled as its southern
  region** (Grande Erg north + Sadhir desert south as one landmass).
- **Gaerwath** — a **ring/rose-shaped archipelago** in the central ocean **east of Erg**.
- **Qi-Long** — the large **north-eastern/eastern** landmass.
- **Ophiur** — an **east/south-east** landmass between Qi-Long and Xebech.
- **Xebech** — labelled **twice**: a small far-western island AND the large south-eastern
  landmass. A genuine map mystery, kept as such (colony? error? two Xebechs?).
- **Climate frame:** the north margin is banded "**Frozen Lands**" and the south margin
  "**Obsidian Lands**" — two named off-map world-edge regions; the world runs **cold
  (north) → hot (south)**.

`[NOTE]` The Drive maps also draw **two polar Maelstroms** (a **Cold Maelstrom** ring in the
north-central sea, a **Hot Maelstrom** ring in the south) and **no central vortex** — this is
**NOT adopted**: canon keeps **one central Maelstrom** (GEO-13); the claim is logged as
**HARV-5** in `conflicts.md`. Likewise, where this layer diverges from decided prose
placements (Cartosa/Meridian in the "warm southern seas"; GEO-12's SE Alfheim anchor; the
Sadhir on the southern desert-continent per the ADD-3 reconciliation), reconcile under the
GEO-3 clean-map project — do **not** silently re-anchor regions to this layer.

## The world at large `[CANON]`
`[CANON — decision GEO-13]` Ymir is a **globe** — a spherical world — dominated by one great
**Central Ocean (Oceano Centrale)** with the **Maelstrom** at its heart (→ `cosmology.md`).
The drowned ancient capital **Ragash** lies beneath the Maelstrom. `[CANON — decision BAT-2]`
Keep **Ragash** (the **Adepti** capital the Catastrophe turned into the Maelstrom) distinct
from **Xanadu** (the **Xebechani fortress-city** that houses the **Rune Magiche** →
`magic.md`) — two different places. Ancient **portals** — the Adepts' network and the
Xebechani **Vere Vie** — reconnect distant regions (reactivated in the Era della Marea).
`[CANON — decision GEO-11, refined]` **Two distinct upheavals** reshaped the map — keep them
separate: **(1) La Catastrofe** (the *primordial* event, ~year 0 d.M. — the Adepti ritual that
birthed the Maelstrom; → `history.md`, `cosmology.md`) broke the **Gaerwath** and the **Isole
d'Argento** off the main continent into archipelagos; **(2) il Grande Prosciugamento** (the Great
Drying, ~2400 d.M. — a *separate*, later cataclysm) dried the inland **Sadhir** sea into salt
desert (→ Sadhir section below). Do not conflate the two under one name.

## Regions & powers

### Letia / Impero Letio (the sacred North) `[CANON]`
The great northern **theocratic empire** of the **Church of Mithra**, ruled by a
**Teocrate**; at its height (1555 d.M.) held nearly all northern Ymir. Long decline:
the Young Kingdoms broke away (2200s), Helgedad seceded (2600), the Church took full
command (2610). `[CANON — decision GEO-8]` Its **capital-seat is Solanthya** (seat of the
**Alto Teocrate**); on the world map the label **"Solanthya"** stands for **greater Letia** as
a whole. Aggressively missionary; now waging war on Armora. Tone: high-fantasy sacred empire.
`[CANON — letia.txt]` **~300 million** people (mostly Human); temperate; split into small
**marches and baronies**. Ruled by the **Clericato di Mithra** under the **sommo sacerdote
di Mithra** at **Solanthya**. All races welcome **except orcs, dark elves, and followers of
the Tenebre**; one may not openly profess a non-Mithra cult. Home to the **Monti Bianchi**
(White Mountains) and **Naughrit** — one of the greatest dwarven strongholds on Ymir. (Lost
eastern lands became the **Regni Belligeranti**; a succession crisis spawned the **Regni
Giovani**.) → `factions.md`, `pantheon.md`

### The Regni Giovani (Young Kingdoms) — steampunk frontier `[CANON]`
Broke from Letio in the **War of the Princes** (2200–2230). Realms include **Armora,
Wald, Zaalesha** (one bloc in the 3025 Great War) and **Vallanya, Caeldir, Tydriell**
(the other), plus the dark armies of the ancient dragon **Gwalgamaur** as a third
side. This is Ymir's **magitech/steampunk** zone.
- **Armora** — a **Granducato (Grand Duchy)** ruled by **Granduke Leonius VonGryffen**
  (styled *il Tecnocrate*). A fog-wreathed industrial city of **seven districts**:
  **Città Alta** (Ducal Palace), **Distretto Militare** (Barracks), **Città Nuova**
  (Academy of Elemental Studies), **Distretto Mercantile** (the Casino), **Città
  Bassa** (red-light quarter), **Ghetto Nanico** (dwarf quarter, House of the
  Council), **Zona Industriale** (Guild of Artificers). Steam trams, airships,
  submarines (Nautilo), ornithopters, Automata, Leyden-jar tech (→ `magic.md`,
  `factions.md`). In religious schism with Letia: the Granduke founded the breakaway
  **Chiesa Armorita di Mithra** and is at war with the Empire.
- **Caeldir** — origin of the steam-lance; a magitech realm.

### Helgedad — the Frozen Hell (grimdark North) `[CANON — Helgedad.doc]`
A far-northern island, the coldest place on Ymir ("**Inferno Gelato**"). Once six
imperial **Marche (Marches)**, each with a noble house and city:
1. **Kelmark** (SW) — House **Rudstar**, city **Kelmar** (largest city); horse-knights
   of **Thurms**; the 400 km **Vallo di Aslund** (Wall of Aslund) built against the
   northern barbarians by **Aslund the Swordless** of the Tenth Legion.
2. **Tallvar** (SE) — House **Talvain**, city **Tallvar** (first Imperial city; most
   trade with the southern continent); cults of Thurms and Heis (gambling).
3. **Nortislong** (west coast) — House **Geidmund**, city **Nortislong**; the **Norsi**
   (totem-spirit tradition); the **Foresta d'Inverno** (Winter Forest).
4. **Grudgemark** (center-west) — House **Tannermar**, city **Grudgeburg**; allied with
   the dwarves; famed road-builders and the **Case di Guarigione** (Healing Houses).
5. **Nortmaar** (free land) — the warrior **Vorskgen** clans, united ~50 years ago
   under the **Ulding** (seat **Nortcastle**); ancestor/sacred-weapon cult, berserkers.
6. **Seamark** — House **Ognir**, port **Harbor**; sailors; the triple-goddess cult of
   **Hudemia, Diis, Thal'Khal** (the **Torre Splendente** temple).
Dwarves hold the **Aule Dorate** (Golden Halls, Monti Aestyr) and ancient **Stonebridge**
(Monti di Bruma), linked by old tunnels — and older, non-dwarf passages below. Sylvan
elves hide in the **Bosco di Caelebawn**. The **Landa Gelida** (Frozen Waste) to the
north holds ruins and evil things; the sorcerer **Signore dell'Oblio** once dwelt in
the Aestyr. Longship types: **Drakkar, Knarr, Dromen**. Recently ravaged by the **Wars
of the Wolves** (3015–3024). → `factions.md`, `history.md`

### Alfheim & the Gaerwath (elf lands) `[CANON — Gaerwath.doc]`
`[CANON — decision GEO-12]` The elf lands cluster in the **south-east**: **Alfheim** is
anchored **near the Gaerwath and the Isole d'Argento**, in that SE island cluster (not in the
north). → world-map reconciliation, open questions.
- **Alfheim** — realm of the **light elves**; capital **Ost-en-Galad** ("the Shining
  City"); ruled by a queen (the line of **Inanna the Splendent**) and a Council.
  `[CONFLICT → HARV-2]` The wiki's 2023 rewrite instead describes "**Al'Fehim**" as a
  **Gaerwath protectorate** and Loto-Nero producer — possibly the *post-Ouroboros
  resettlement* snapshot; logged, not adopted.
- **Gaerwath** (Elvish "**Sea of Sorcery**") — an **archipelago** of the **Dark Elves**,
  where they were exiled after the schism; treacherous magic-cloaked seas crossable
  only with elven guidance; cities of "dark beauty" linked by undersea roads and magic
  bridges; a slave society (orcs, humans). Ruled by an **Emperor** who is also supreme
  pontiff; the Dark-Elf caste order (**Lyar/Nath/Gash**) → `peoples.md`. Unified under
  **Morannagul** (2550). → `peoples.md`, `history.md`
  `[CANON — ymir-drive: MAP-Gaerwath-3500dM]` The Drive corpus holds a full **national map
  of the Gaerwath dated "c.a. 3500 p.M."** — essentially the manual-present (~3518 d.M.,
  HIS-1), and the only *dated* national map in the corpus:
  - **Ten named islands**: **Cn'ethyr** (north — holds the capital **G'nethyr**),
    **Kh'myr**, **Yr'thyr**, **Wag'myr**, **Daarwyr**, **Moloch**, **N'ysyr**, **Gh'yrst**,
    **Dr'hakyr**, and the bare, settlement-less **Isola del Caos**; plus a small unnamed
    isle holding **Gh'anuss / Selva Ignota / L'ykry**.
  - **Thirteen stepped Ziggurat temples** (Hywon, Golog, Thelog, Ghom'a, Hr'yth, Wyaya,
    Agar, Mooloch, **A'rwo**, Gh'yrst, T'alan, Wag'myr, Ah'rkan) — a temple-building,
    death-worship register; the **A'rwo Ziggurat** (on N'ysyr) is apparently named for
    **Arvo**, the Dark Elves' Essence-dust currency (→ `magic.md`, `economy.md`).
  - **Soul/dream/death toponymy** confirming the culture: *Fiume dei Pensieri*, *Fiume di
    Anime*, *Lago degli Infanti*, *Foresta dei Sedici Pianti*, *Canale di Sangue*, and the
    **Palazzo delle Aule dei Sogni** (Palace of the Halls of Dreams — a Dreamlands hook);
    a **Medusa/Gorgon-head compass medallion** serves as the national emblem. Dozens more
    settlement names in the transcript (`sources/extracted/ymir-drive/MAP-Gaerwath-3500dM.txt`)
    — ready place-name stock.

### Qi-Long — the six Dragon-God kingdoms (the wuxia East) `[CANON — decision GEO-2 = six kingdoms]`
**Present day: six independent, mutually hostile kingdoms**, each ruled by its own rival
**Dio-Drago (Dragon-God)** and resisted by one of six secret societies (collectively "**La
Triade**" — see `factions.md`). The six warred to a centuries-long stalemate. **Ancient backstory:**
a single **Vero Dio Drago (True Dragon-God)** once reigned over a unified empire from the **Capitale
della Luce** (the **Tianqi** empire of the maps / *Onore e Memoria*); that unity is long gone — the
present six Dragon-Gods are successors/usurpers. (The **Mah-Dhol** empire fell 1900–1920.) The White
Mongoose society serves an absent Dragon-God "not yet of this world," awaiting his return. Tone:
honour-culture wuxia/xianxia with martial sects. → `factions.md`
`[NOTE]` Two Dragon-God name-sets exist (2008 vs. revised) — pick the revised set (BAT-6). The
Tianqi/empire framing survives as **history**, not the present.

### Xebech — the reptilian homeland (alien East) `[CANON]`
Jungle-city homeland of the **Xebechani**. Its lost northern part is
**Loquitchatzotech** (Isle of Death), yielded in a 75-year undead war (2020–2095).
Ancient, half-forgotten technology (the Pozze, the Vere Vie). → `peoples.md`

### Sadhir — the Shining Desert (South) `[CANON — decision GEO-1 = layered]`
**Two eras, both canon.** Once a shallow inland sea dotted with **human island-kingdoms** — the
**Sadhiriti**, ruled by a **human sultan** from cities like **Al-Sidath** and **Al-Jabur**, with
**Marid djinn** and salt-wraiths (Gash-Azr). Then the **Grande Prosciugamento** (the Great Drying,
~2400 d.M. — a *later* cataclysm, **not** the primordial La Catastrofe) dried the sea into the
blinding **salt desert** of ruins, the **Deserto Scintillante** — and in the age that followed the
**matriarchal Sarradhi lizardfolk** rose to rule over the drowned human ruins (the Sultanate of
Zarash-Sur, Kalzharan, the Wheel of Life; with **hermit-crab** subject folk). So the region reads
**human-kingdoms-beneath, Sarradhi-sultanate-above**. Haunted throughout by the undead **Blue
Oyster Cult** of the demon **Ea**. → `peoples.md`, `factions.md`, `bestiary.md`
`[CONFLICT resolved]` The human "Leggende del Sadhir" and the English gazetteer's Sarradhi are the
**two eras**, not rival accounts.
`[CANON — decision FRAG-5/FRAG-7; source: sources/raw/Fragments.pdf, Fragment A]` **Deep-past
southern lore.** In the old texts the whole southern landmass — the **Sadhir** and **Ophiur**
together — is called **Mandolia**, an **archaic name used in Adepti-era writings** (no map redraw;
the modern names stand). It was the old southern seat of the Adepti: **Ört di Xand, the Fifth
Adept, ruled south-east Mandolia** from **Xand** (his home-region/city, in the SE — the Sadhir /
Ophiur reach). In the far SE Sadhir, deep in the **Deserto Scintillante** (Shimmering Desert),
stands the **temple of the forgotten god Jerbal** (→ `pantheon.md`) — a small monastic order that
guards Ört's **manuscript** locating the four fragments of the **Gem of Ört** (→ `items.md`). An
old royal city, **Hasl'Aret** — the source's variant *Hasl'Af*, normalised — kept a **treasury**
where the Gem was rumoured (falsely) to have ended up. `[INFERRED]` The archaic **Ophith** spelling
of the Fragments normalises to **Ophiur** (decision FRAG-7).

### Deep-past dungeon-sites of the south (the Halls of Taros) `[CANON — decision FRAG-5/D5; source: sources/raw/Fragments.pdf, Fragment C]`
A cluster of ruin-sites in the **southern lands** (Sadhir / Ophiur / old Mandolia), placed near the
Adepti's old southern seat and Jerbal's temple — the deep-past dungeon the **Diary of Loregar**
maps (→ `items.md`, `characters.md`):
- **The Peak of Ulmar** — a mountain whose **south slope** is the route's starting landmark.
- **The Plain of the Stelae** — reached ~half a day north-east of Ulmar's south slope; a field of
  standing stones holding the **Stele of the Martyr**, which bears the **Runes of Power** that once
  adorned the **Crown of the Four Kings** (→ `items.md`), with the **symbols of the Four Kings** at
  its base (the lock the Halls-of-Taros amulet keys).
- **The Crypts of Audin** — the passage beneath the Stele opens down into these crypts, threaded by
  stones marked with the **Sign of Vor** (press the seventh).
- **The Halls of Taros** — the deep goal above the Crypts, named for **Taros, pupil of the Adept
  Svelos** (→ `secret-the-great-lie.md`, `characters.md`). `[INVENTED — decision FRAG-5]` Exact
  coordinates are deliberately left unfixed (a "lost site" the map does not mark); the south is the
  ruled placement, not a surveyed point.

**Two imperial cities of the Fragments (placement soft) `[CANON — Fragments.pdf; INFERRED placement]`:**
- **Valentia** — an **imperial city** whose great **Imperial Library** holds records of the deep
  past (the diarist Loregar read there of a trap in the Halls of Taros). `[INFERRED]` "Imperial"
  most naturally reads as the **Letian Empire**, but the Fragments do not fix it — it may be a seat
  of an older empire; left unplaced pending a source.
- **Mileus** — home city of the historian **Tarogald of Mileus**, author of *De Daemonomachia* (→
  `items.md`, `characters.md`). Location unfixed by the source.

### The Grande Erg, Ulan-Tang & Khorish (deserts) `[CANON — il-grande-erg.txt]`
Desert lands. **Khorish** — the "**Regno dei Faraoni Eterni**" ruled by the eternal pharaoh
**Athmokethepek I** and his wife **Nefthi**, sustained by mass **necromantic slave-labour**
(founded 2160–2180; the wiki dates its rise to the late 23rd century — see NOTES). **Ulan-Tang**
— a city-state on the river **Tang** (once sacred to **Ishtar**), now the corrupt seat of the
**spider-god Yogh**, its High Priest **Sazar-Gadash** (a demon-son of Asmodeus who murdered his
predecessor Azim-Mulath); five colour-coded noble houses (Ishra, Tyarreth, Miraz, Gaib, Gadash);
the drug **Loto Nero**; the **Distesa Arida**. → `factions.md`, `pantheon.md`

### Cartosa & Meridian (swashbuckling South) `[CANON — full sourcebook]`
See `factions.md`/`peoples.md` and the map. Two islands in the warm southern seas:
the **Principato di Cartosa** (pirate/naval monarchy under the Carrillo) and the rival
**Repubblica di Meridian**. Mountains **Sierra Plata** (Cartosa isle) & **Sierra
Grande** (Meridian isle); the **Coste Gemelle**; jungles and semi-arid plains. Map
settlements: Cartosa, Meridian, Garzona, Portejo, Puerto Nuevo, Puerto Escudo, Santa
Hermana, Vila Loca, Madeira, Cay, La Roca, Forte León, Puerto Esperanza, Suaponé,
Matinica, Punta del Toro, Costa Sileña, Capo Estello. Rivers: Rio Grande, Rio Tapajero,
Rio Plata, Xingu.

### Ophiur — the wild continent (far South) `[CANON — Additions.md]`
A largely wild, unexplored continent **south of the Qi-Long**, part lush tangled jungle, part
towering mountains (the **Monti Bui** and **Monti Tartaruga**), part broad savanna. Its peoples are
lumped together by Letii and Cartosani as "**I Popoli Neri**," but Ophiur holds many kingdoms and
cultures. Major settlements sit on the coasts or on the Sadhir/Qi-Long borders.
- **La Coalizione d'Avorio (Ivory Coalition)** — allied but independent mercantile city-states,
  chiefly coastal: **Zabhula**, **Akhon**, **Ga'Namesh**. Rich on resources scarce elsewhere but
  abundant in Ophiur: precious minerals, **orihalcum**, **shald**, **loto** and other substances.
- **Grande Regno di Tarkur** — an **Ur-Tanoth kingdom** spanning most of the savanna, whose whole
  culture turns on **la Tempesta** (the Storm): an energy present in all creation, an eternal cycle
  of birth and destruction. All races are touched by it, the Ur hold, but only they can perceive it;
  they follow its wanderings across the savanna as their mission. Three castes: the **Cercatori**
  (who "scent" the Storm and guide the migrations), the **Sacerdoti** (who see, hear, and touch it),
  and the rest of the tribe. → `peoples.md`
- **Libera Città di Gazal** — ancient free city at the feet of the Monti Bui; said to be the former
  capital of a great empire, now largely ruined; magnet for merchants, adventurers, thieves and
  brigands seeking Ophiur's riches and, above all, the vast mysterious **undercity** beneath it.
- **Horatli** — a city in a half-hidden valley beneath **Mount Horat**, highest peak of the Monti
  Tartaruga; seat of a mysterious conclave of mages and arcanists.
- **The unexplored jungle** — the deep interior, where legend places fantastic cities of gold and
  jewels, inhabited by vampires and foul demons.
Legends: creatures of the **most ancient races**, on Ymir since the world's origins, surviving the
Wars of the Mages in the deep jungle; demons and vampires haunting the old ruins (some tribes pay
them regular sacrifice for protection); and the **Giardino di Xiombarg**, hidden in Ophiur's heart —
warded by ancient guardians, its miraculous plants said to cure any disease or affliction.
`[INFERRED — map reconciliation]` The old hand-drawn world map's southern desert-continent labels
**Gazal** and **Zabhola (=Zabhula)** now resolve to Ophiur — the great southern landmass holds the
Sadhir on its western reach and Ophiur eastward toward the Qi-Long (partially resolves GEO-4).

### Isole d'Argento (Silver Isles) `[CANON]`
Island realm of the **Folletti**; capital **Elendor**, seat of the **Council of
Peoples** (the **Seggio di Cristallo**, built 2590–2595). Broken from the continent by
the Catastrofe. → `factions.md`

### Kyria (the Mist-Isle) `[CANON — kyria.txt]`
A fog-wrapped north-western island, **untouched by the Catastrofe** and isolated since the
Demon Wars. Home to **~500,000 Ur-Tanoth** "beast-humanoids"; its sole town, **Thonis**,
shelters human and elf refugees.

### Other worlds & the Dreamlands `[CANON — see secret-the-great-lie.md]`
- **La Terra dei Sogni (the Dreamlands)** — the plane of dreamers' souls, ruled by the Outer
  Gods; contains steampunk **Arcadia** (reached by lucid dreaming through Ragash, guarded by
  Topramesk). → `cosmology.md`, `secret-the-great-lie.md`
- **The Isola dei Demoni (Isle of Demons)** — a NEW continent dragged up from the demon-world
  when the Sovereign Demons' prison cracked in the Era della Marea. → `history.md`
- **The Adepti's other worlds** — Tchyo, Omalgat, Naxtis, Zend, X-01, Ouronos, Gwart, Seelie:
  the planets of the old galactic empire, homeworlds of the engineered races. → `secret-the-great-lie.md`

### Mysterious & dangerous places `[CANON]`
- **il Groviglio (the Tangle)** — forest with the **Cuore del Caos** at its centre (1600 d.M.).
- **Ulan-Tang** — ancient portal where **Sguardo-sul-Nulla** entered Ymir (3026 d.M.); see the desert section above.
- **The Maelstrom / former Ragash** — the world's dead, dangerous heart.
- **Il Mondo dei Sogni (the Dream World)** — a plane reached (dangerously) via Armora's
  experimental **Oniroscopio**. → `magic.md`

---
### Open questions
- **Reconcile the world map with the prose** — placement of Letia, Helgedad, Xebech,
  Qi-Long, and the elf lands relative to the labelled map regions (Solanthya, Hibernia,
  Ljone del Saos, etc.). Some map regions (Xuthal, Itza, U-aj-tanis, Sathe, Luveburk,
  Al-Sidah…) have no prose yet — candidates to invent or ask about.
- Maps are embedded in some **.doc** files (Helgedad, Armora) that `antiword` can't
  extract — a `.doc` image-extraction pass could surface regional maps.
- **Cartosa.doc** vs **Cartosa Guida.pdf** — reconcile the two Cartosa texts.
