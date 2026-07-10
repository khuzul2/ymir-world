# HARVEST REPORT — wiki-worldofymir (Fandom import) vs. our existing corpus & canon

> **What this is.** A parallel session imported the full *World of Yimir* Fandom wiki
> (75 pages, this folder) and built its own `canon/` from it. We already hold (a) an
> earlier **88-file export of the same wiki** (Wikidot-style `.txt` in `sources/raw/`,
> digested in `sources/extracted/wiki/*.md`) and (b) a `canon/` that has since evolved
> far beyond theirs. This report isolates **what this import adds that we do not
> already have**, judged **against OUR canon**, and flags conflicts without resolving
> them. Method: word-level sequence diff (difflib) of every Fandom page against its
> earlier-export counterpart, then manual reading of everything that showed genuine
> novelty; name-greps across `canon/`, `sources/extracted/wiki/`,
> `sources/extracted/batch2*/`, and `manual/`.
>
> **Bottom line:** the two exports are the **same wiki**; ~69 of 75 pages are
> content-identical to what we already digested. The real additions are **two brand-new
> pages** (*2011 - Back to war!*, *Vlatch*), **one page that was a stub and is now full**
> (*Scritti e Pergamene*, a 100-book library), **two pages rewritten in place** (*Qi-Long*,
> *Alfheim* — both last edited 2023, both colliding with decided canon), and **one new PC**
> (*PG di Ymir* → Ferdinando Montecarlos).

---

## 1. NEW / FULLER PAGES vs. our earlier 88-file export

| Page (this folder) | vs. earlier export | What it adds |
|---|---|---|
| **`2011 - Back to war!.md`** (last ed. 2023-05-24) | **No counterpart at all.** (The earlier export's extra campaign stubs — `campagna-di-trento---2007.txt`, `campagne-di-venezia.txt` — are empty shells, not this page.) | A complete (if telegraphic) 4-chapter campaign synopsis set in a later era: world war, **M'Raker** (= Kramer as lich) leading undead armies, the **gods banished from Ymir**, fall of Armora, phylactery-hunt to the **Ophiur**, quest to restore chosen gods. Five PCs w/ players, three NPCs. → §5 for full detail. |
| **`Vlatch.md`** (last ed. 2017-12-02) | **No counterpart at all.** "Vlatch" appears nowhere else in our whole corpus (raw, digests, batch2, canon, manual). | A triple-natured mystery: future **Xebechani chronomantic agents**, a **mana-parasite phenomenon**, and/or **Adepti-era time-scrying machines**. Introduces **Cronomanzia** ("the supreme arcane art of time-manipulation") and the **heretical crypt-archive of the Alto Clericato di Solanthya**. → §2. |
| **`Scritti e Pergamene.md`** (last ed. 2010-10-30) | Earlier `scritti-e-pergamene.txt` was a **stub** (only *Tomo della Falsa Sapienza* + the *Pergamene Dimenticate*). | The **full library: 100 numbered books/tomes** with titles, authors, and (RM-mechanical) effects — none of the 100 entries was in the earlier export or our digests. → §2 (magic.md/pantheon.md/characters.md feeds). NB the new page *drops* the two stub items (they survive in `oggetti-vari` / our raw). |
| **`Qi-Long.md`** (last ed. **2023-05-24**) | **Rewritten in place, 100% different text.** Old page = six warring kingdoms, six named Dei-Drago (Huolong'nan, Seishima Tatsumoto, Weichong-Shanxuan, Kuangshuang Long, Jiu-Yaofeng, Qiulei-Senbei) + six kingdom names. That old text survives **only** in our `sources/raw/qi-long.txt`. | New text = the **unified empire**: six provinces each ruled by one of the **Grandi Sette Imperiali**, the unseen **Dio-Drago** emperor at **Tianqi**, minor sects regulating all business. Nearly verbatim the *Onore e Memoria* material already in our `canon/factions.md` — **corroboration**, but presented as the *present* (conflict → §4.1). |
| **`Alfheim.md`** (last ed. **2023-05-24**) | **Rewritten in place, 100% different text.** Old page = light-elf forest kingdom, capital **Ost-en-Galad**, queen + Council (survives only in `sources/raw/alfheim.txt`). | New text (43 words): "**Al'Fehim** è un **protettorato del Gaerwath** situato al **confine nord-ovest del Qi-Long**… uno dei maggiori produttori di **Loto Nero** di tutto Ymir" (pop. 6.5M, mostly elves). Conflict + a tempting reconciliation → §4.2. |
| **`PG di Ymir.md`** (last ed. 2011-03-04) | Identical except **one added entry**. | **Ferdinando Montecarlos** — "Pathfinder freelance nato e cresciuto a Cartosa. Player: Alessio." New name to the entire corpus. |
| `La caduta di Helgedad.md` | Same one-line stub, trivially reworded. | Nothing new. |

**Everything else** (Entità, Cronologia, L'Era della Marea, Helgedad, Gaerwath, Cartosa e Meridian, the races, religions, items pages, and the campaign reports *Gate to Unknown* (= our `riassunto-sessioni-prima-di-luned-04-06-2007.txt`), *A Steamclad Sky*, *A Black Sun Rising*, *The Monster Mash*, *La Leggenda delle Rune Magiche*) is **content-identical** to the earlier export modulo formatting; all already digested in `sources/extracted/wiki/*.md` and mined into canon.

**Retention note (reverse direction):** the earlier export holds ~17 pages **absent from this Fandom import** — notably `arcadia.txt` (~2.1k words), `i-demoni-su-ymir.txt`, `folletti.txt`, `malattie.txt`, `talenti.txt`, `corruzione*.txt`, `geografia.txt`, `oggetti-ed-artefatti-di-ymir.txt`, `ymir--d-d-4e-personaggi.txt`. Do **not** treat this import as a superset; keep both.

---

## 2. NEW LORE not in our canon — by target canon file

*(Judged against `canon/*.md`; each bullet cites its wiki page. Items are ready to
integrate as `[CANON — wiki: <page>]` unless flagged.)*

### → `canon/characters.md`
- **Ferdinando Montecarlos** — freelance *pathfinder*, born and raised in **Cartosa** (player: Alessio). *(PG di Ymir — 2011 addition; absent from every other source.)*
- **M'Raker** — the **lich name Heinrich Kramer takes** after 3026. Under it he leads world-spanning undead armies, **banishes the gods from Ymir's universe**, hides his **phylactery in the Ophiur** (reached via the Ophirite coasts), and schemes to re-enter Ymir **disguised as a demigod** when the gods are restored. Major forward-extension of the canon Kramer arc. *(2011 - Back to war!)*
- **Alexander Corvinus, "Il Perfetto"** — PC of the 2011 campaign (player: Mura). Cross-check: *PG di Ymir* (both exports) has "**Corvinus Alexander** — Aristocratico Armorita rinnegato, studioso delle arti oscure. Player: **Daniel**." Same character, different player at the table — flag on merge; the "renegade Armorite aristocrat, student of the dark arts" backstory is in our sources but **not yet in canon**.
- **Allanon-Ra** — PC (player: Pojer). New name. The **-Ra** suffix matches **War-Ra**, "assassino di Ulan-Tang appartenente alla **famiglia nobiliare dei Ra**" (*PG di Ymir*) — `[INFERRED]` a member of the same Ulan-Tang noble family (see §4.6 on the "Ra" family vs. canon's five houses).
- **War-Ra "Secundus"** and **Gundar il Massacratore "Primus"** — returning Gate-to-Unknown veterans; the **Primus/Secundus** epithets are new and unexplained (successors? clones? — cf. the soulclone motif around Sigurd/Isidoro in batch2). War-Ra exists in our digests but **not yet in `characters.md`**; Gundar's epithet "il Massacratore" is attested in *PG di Ymir* and now the campaign. *(2011 - Back to war!)*
- **Topramesk il Giallo** and **Tofango** appear as living **NPCs** of the 2011 campaign — consistent with Topramesk's Dreamlands persistence; for Tofango see conflict §4.5.
- **New named figures from the 100-book library** *(Scritti e Pergamene)*: **Victor van Bodich** (planar/elemental theorist), **J-Ckva'Nce** (author of the *Grande Compendio delle Arti Magiche*; Xebechani-register name), **Dreyfus il Sadhirita** (scholar of the Adepti), **Tara Mandika Ratnam** (authored *Amare e Legare*; plausibly the PC Tara, the deposed Ophirite princess), **Mugraash lo skrifano** (orc chronicler — *"Ztoria di Krande Imperum"*, orc-accented history of the Regni Belligeranti), and **San Dwayne l'Edificatore** — the PC **Dwayne Soylen** (Thurms-paladin temple-builder, *PG di Ymir*) evidently **canonised as a saint** with a hagiography (*Vita di San Dwayne, l'Edificatore*). Also the two rival biographies of the pirate **Rodrigo** (one "a cura di **Diego Alehandro de la Corona**" — the PC bard; its bonus is *Conoscenza Mostri*, a wink that Rodrigo was a monster) — feeds the canon "Roberto Rodrigo l'Armorita" legend.

### → `canon/history.md`
- **A later "World at War" era** *(2011 - Back to war!)*: Ymir shaken by a **world war** among (a) **M'Raker's undead**, (b) the **Federazione Letia**, (c) **i Cani del Qi-Long**, "guidati dai **Draghi che si sono destati e riuniti**" (the dragons awakened *and reunited*). **Armora is besieged and falls** to the undead. The PCs discover **the gods are gone from Ymir — banished by a powerful sorcerer** (M'Raker), and must work out **how, and which, gods to bring back**. No in-world date on the page; the campaign is real-world 2011 and sits after Gate to Unknown (3026). Placement is a decision (see §4.3) — candidates: within the Nuova Era del Caos (3026–3260), or at/after the ~3518 present (the *PG di Ymir* 3518-tagged entries and the 3518 world map are the same authorial layer).
- **The dragons "destati e riuniti"** corroborates canon's Era-della-Marea dragon-waking (Ouroboros) and extends it: the Qi-Long dragons end up **reunited and leading armies** ("i Cani del Qi-Long"). → also `bestiary.md`.
- **Predicted-future canon** *(Vlatch)*: "secondo alcuni antichi testi," the Xebechani **will create the Vlatch in a distant future** to repel **an ultimate great Demon Invasion**; the Vlatch's time-paradoxes **will change Ymir's history**. A prophecy-grade device — GM-layer material (pairs with `secret-the-great-lie.md`).

### → `canon/magic.md` (or a new `canon/items.md` — see §3)
- **Cronomanzia** — named as "la **suprema arte arcana** della manipolazione del tempo" *(Vlatch)*. Our canon has **no time-magic discipline at all**; this names one and reserves it for (future) Xebechani craft. Candidate for the realms/disciplines section.
- **The Vlatch** *(Vlatch — full page, all three readings are in-world theories)*:
  1. **Entities**: implacable chronomancy-infused agents the Xebechani will build against the last Demon Invasion; source of history-altering paradoxes.
  2. **Phenomenon**: a rare, unexplained **parasitic energy** appearing at extreme Essence concentrations, feeding on ambient mana and **substituting itself for it**; long-term effects unknown; dismissed as fantasy by most arcanists. (Hooks straight into our Essence/Arvo/Risonanza material.)
  3. **Artifacts**: per heretical manuscripts in the deepest crypts of the **Alto Clericato di Solanthya**, one or more bizarre **machines from the Adepti era — or from a possible far future** — able to **show past and future events**; none ever recovered.
- **The library of 100 named books** *(Scritti e Pergamene — entirely new)*. Standouts for canon (drop the RM bonuses, keep existence/lore):
  - **Sacred scriptures**: *Il Libro degli Abissi* (holy book of **Hudemia**), *Parole al Vento* (of **Heis** — reading it erodes sanity, fitting the Mad God), *Il Libro dei Precetti* (of **Thurms**), *La Ruota del Fato* (**Sohleugir** scripture — names the canon "Wheel" creed's book). → also `pantheon.md`.
  - **Forbidden/outer**: *Litanie per il Grande Agothu* (demon-pacts; independently attested in batch2 — `campaigns-a`/`Atto 2`, sold by the necromancer Korak Garth), *Il Libro degli Estranei* (teaches a **rite to summon a Natharl'Nacna** — the Void-dwelling eldest demons of batch2's `Demoni.txt`; first source that makes them *summonable*), *Oltre la Soglia*, *Il Tomo della Magia Nera* (many copies, each one random evil discipline), *Lo Specchio Nero*, *Osservazioni sui Corpi Confinanti* ("Dark Entities" — batch2's "Corpi Confinati" motif), *La Chiave d'Argento* (Dreamlands lore; Lovecraft nod).
  - **Adepti/tech**: *Le Macchine degli Adepti*, *Apparati Leggendari*, *Annotazioni a proposito degli Adepti* (Dreyfus il Sadhirita), *Inventare l'Impossibile* (Automata), *Motori a Vapore*, the two *Manuale di Meta-Taumaturgia Meccanica* course-books (Armora's magitech curriculum in-world), *Guida alla vita Artificiale*, *Sulla Costruzione di Golem Servitori*, *La Magna Opera ovvero i Segreti della Vita* (simulacra).
  - **Histories/ethnographies** that confirm canon topics have in-world literature: *Declino e Caduta dell'Impero Letio*, *Breve Storia di Cartosa*, *La Guerra dei Principi*, *La Battaglia della Terra Infranta*, *La Leggenda dell'Occhio di Kzorr* (ties to batch2's Helgedad module), *I Regni Neri* (Ophiur), *Il Paese delle Sabbie* (Grande Erg), *L'Isola delle Nebbie* (Kyria), *Le Guerre dei Goblin* (dwarf history), *Ztoria di Krande Imperum* (orc self-history!), *Elfi: il popolo della Shulma* (names the elves "the people of the Shulma" — ties to the canon Exile/Messaggero prophecy), *Gli Arawak di Cartosa*, *Le Origini degli N'Kishi*, *Il Cargo: alle Origini del Mito* (scholarship on the M'Bantha cargo-belief), *Comprendere gli Xebechani*, *I Sohleugir e le loro abitudini*, *I Figli della Notte* (two volumes: Licantropi, Vampiri).
  - **Sanity-eroding volumes** (a motif): *Manuale Pratico di Chirurgia Composita* (author: the PC **Ruben Montoya**), *Tomo della Stolidità Vermiglia*, *Parole al Vento*.
- `[NOTE]` The page is heavily Rolemaster-mechanical (skill bonuses, spell-list access, "Sanità" rolls); strip per META-4/META-7 and tag "RM".

### → `canon/factions.md`
- **Alto Clericato di Solanthya — heretical crypt-archive**: the Letian high clergy keeps **heretical manuscripts in its deepest crypts** (the Vlatch dossier among them). First attestation that the Church *curates* forbidden knowledge — a strong GM hook onto the Inclusivist/Popolare schism material. *(Vlatch)*
- **Federazione Letia** — a **federal** form of the Letian polity, belligerent of the 2011 world war. New polity-form (canon knows Impero Letio → Church rule → schism, never a "Federation"). Era-dependent — park with the §4.3 placement question. *(2011 - Back to war!)*
- **I Cani del Qi-Long** ("the Dogs of the Qi-Long") — the dragon-led Qi-Long war machine of the same war. New faction name. *(2011 - Back to war!)*

### → `canon/geography.md`
- **Al'Fehim (Gaerwath protectorate)** — see conflict §4.2; if reconciled as the **post-Ouroboros resettlement of Alfheim**, it *fills* the canon gap "Alfheim's fall and resettlement" (`history.md` ~3518 line) with concrete facts: Gaerwath protectorate, NW border of Qi-Long, **major Loto Nero producer**, pop. ~6.5M, still mostly elves. *(Alfheim, 2023 text)*
- **Ophiur** as the hiding place of **M'Raker's phylactery** ("le coste ophirite"). *(2011 - Back to war!)*
- `[NOTE]` The 2011 page's "deserto di **Xxx**" is an authorial placeholder — the desert where M'Raker was sought is deliberately unnamed; do not invent a name silently.

### → `canon/pantheon.md` / `canon/secret-the-great-lie.md`
- **The gods can be banished from Ymir's universe by mortal sorcery** — M'Raker does it; restoring them requires a ritual/choice of *which* gods return, and a sufficiently disguised impostor (M'Raker as "semidio") can slip in among them. Theologically explosive; sits far more comfortably in the **Great-Lie GM layer** (if the worshipped "gods" are Adepti-usurpers, a supreme lich *could* bar them) than in the public myth. *(2011 - Back to war!)*
- Sacred books per god (see library, above).

### → `canon/bestiary.md`
- **Vlatch (as entities)** — chronomantic, implacable, artificial; candidate "unique/mystery entities" entry cross-referencing magic.md. *(Vlatch)*
- **Natharl'Nacna summonability** via *Il Libro degli Estranei* (crosslink batch2 `Demoni.txt` where they are VI-type-equivalent Void demons). *(Scritti e Pergamene)*

---

## 3. Their `canon/items.md` — assessment & merge verdict

*(Their file: `…/scratchpad/harvest/wiki/canon/items.md`, 34 KB — a canon file we never created.)*

**Verdict: high-quality but ~90% redundant with what we already hold; merge selectively, don't adopt wholesale.**

- **Coverage vs. OUR sources:** nearly everything in it (demon-forged triad Mannaia/Schiantatrice/Rovinatrice, elemental blades, Strappacarne/Mieticorpi/Mietianime, Morgenstern, Pugnale del Rituale Blasfemo, Oblivion, Spada di Valdis, Piccolo Artiglio, Ascia di Droan, Pugni di Hexor, Elethar, all armour/shields, all staves/rods, the Door-of-Despair apparatus, Corona della Stregoneria, the dark relics, Gwynder's luck-set, Topramesk's ring, the metals/stones/herbs) is **already captured, with the same details, in our digest `sources/extracted/wiki/magic-items-society.md`** (§§2, 4, 5, 6) — both corpora contain the same item pages.
- **Coverage vs. OUR canon:** `canon/magic.md` deliberately keeps only a compact summary (named blades, materials list, herbs, Door-of-Despair pointer) and defers the rest to the digest. Their items.md therefore **does** contain plenty of item lore "beyond our canon/magic.md sections" — but it's lore we already hold at digest level, not new information.
- **What is genuinely new in their file:** only the **Scritti e Pergamene library section** (from the fuller Fandom page, §1) — the ~100-book catalogue and its curated standouts table (*La Chiave d'Argento*, *Il Libro degli Estranei*/Natharl'Nacna, the four sacred scriptures, the "forbidden-knowledge costs sanity" motif).
- **What should be merged into our canon:**
  1. **Structure**: adopt a `canon/items.md` (or expand magic.md with *Armour & shields*, *Staves & rods*, *Miscellaneous wonders*, *Scrolls & writings* subsections) — their file is a ready-made, mechanics-stripped, well-cited draft; validate each entry against our digest wording before lifting.
  2. **The 100-book library** (the only net-new content) — integrate per §2.
  3. **Their connective [INFERRED] glosses worth keeping:** (a) the **three unnamed demon lieutenants** of the Demon Wars implied by the weapon triad (open hook for bestiary/history); (b) the **"two Wars of the Waves" question** — Frangionde/Bulusture/Armatura delle Profondità imply a *mythic elemental* Guerra delle Onde vs. our mundane Cartosa–Meridian naval war (2320–2350): **not yet an entry in our `conflicts.md`; add it**; (c) the lost twin blade **Tessionde** as a quest hook.
  4. **Named minor figures** (Kellar, Tshot, Radamantis the first Nosferatu, Droan, Urkhramest il Devoto, King Lorith, Hans Schlecht, Urikal, Gwynder, Taros, the Re Morto) — in our digest but not in `canon/characters.md`; their "Unregistered makers & owners" list is a good checklist.
- **Where their file is BEHIND our canon — do not regress during merge:**
  - Their open question "the **Notturni** … are otherwise unattested in canon" is **answered by our canon**: `bestiary.md` has the full Notturni entry (Additions.md; homeworld **Naxtis**, source of **Umbra**, the "Lavoro/Compito").
  - Their `[CONFLICT]` "the six Elemental Lords were **still mortal**" vs. divine birth: our machinery already frames this (decision **COS-4 = A** — real elemental gods whose names/cults the Adepti co-opted; re-audit **COS-14** — the six Ragash companions ↔ the six Elemental Gods). The "mortal-era blood" reading slots into the GM layer rather than contradicting the public myth. Keep as a COS-4/COS-14 footnote, not a new conflict.
  - Their "Dreamlands are unmapped — add to cosmology" is stale for us: **COS-16** already places the Dreamlands as a region of the Spirit World.
  - Their Oblivion entry retains the Kramer-commission framing; our **HIS-13** ruling (Oblivion = **Tofango's** axe, demon-bound, hermit ending) is the decided canon — merge their forging detail (Hagelbarn, Hans Schlecht, the corrupt-Urikal purpose) under our ruling.

---

## 4. CONFLICTS with our canon (flagged, not resolved)

1. **Qi-Long: empire-as-present (wiki 2023) vs. six-kingdoms-present (decision GEO-2 = A).**
   *Their side:* `Qi-Long.md` (last edited **2023-05-24** — the newest authorial statement in the corpus) describes the **unified empire** — six provinces under the Grandi Sette, the unseen **Dio-Drago** at **Tianqi** — in the **present tense**, and **replaced** the old six-warring-kingdoms page outright.
   *Our side:* `canon/geography.md` + `factions.md` (GEO-2): present = **six independent, mutually hostile Dragon-God kingdoms**; the Tianqi empire is ancient backstory; the old page's six named Dei-Drago and kingdom names are canon detail.
   *Stakes:* the 2023 rewrite suggests the authors' latest intent may be the empire model (or a re-unification after the dragons "si sono destati **e riuniti**" — see 2011 campaign, which would let *both* be true in sequence: six kingdoms → dragons reunited → one dragon-led empire/army). Decision needed; do not silently keep GEO-2.

2. **Alfheim: independent light-elf realm (canon GEO-12) vs. Al'Fehim, Gaerwath protectorate (wiki 2023).**
   *Their side:* `Alfheim.md` (2023): **Al'Fehim** = **protectorate of the Gaerwath**, on the **NW border of Qi-Long**, major **Loto Nero** producer, 6.5M inhabitants, mostly elves.
   *Our side:* `canon/geography.md`: Alfheim = light-elf realm, capital **Ost-en-Galad**, queen + Council, anchored in the **SE elf-lands cluster** near Gaerwath/Isole d'Argento (GEO-12); `history.md`: **Ouroboros destroys Alfheim** in the Era della Marea; "Alfheim's fall and **resettlement**" is background to the ~3518 present.
   *Possible reconciliation to consider (flag only):* the 2023 text is a **post-fall snapshot** — after Ouroboros, the Dark Elves took the broken realm as a protectorate ("Al'Fehim") and turned it into a Black-Lotus plantation. That fills our resettlement gap but contradicts the **location** (NW of Qi-Long vs. SE cluster) unless the Gaerwath/Qi-Long adjacency is itself re-examined.

3. **The 2011 world war vs. the "Nuovo Equilibrio" present (~3518).**
   *Their side:* *2011 - Back to war!* — full world war (undead vs. Federazione Letia vs. dragon-led Qi-Long), **Armora falls**, **the gods are gone**.
   *Our side:* `history.md` (HIS-1): the manual's present ≈ **3518 d.M.**, "an uneasy, ominous calm," ~250 years into the Nuovo Equilibrio; Armora ruled by the Vespertina-line; the 3025 Great War has *different* belligerents (Armora-bloc vs. Vallanya-bloc vs. Gwalgamaur).
   *Stakes:* if the 2011 campaign is placed near the 3518 layer (its sibling *PG di Ymir* entries carry 3518 tags), the "calm" framing breaks — or the war becomes the **future** the 3518 calm is ominously pregnant with (which would be a gift, not a bug). Needs a placement ruling before any of §2's 2011-derived facts enter `history.md`.

4. **Kramer's affiliation (cosmetic).** Canon: "former **Mithran** inquisitor"; *PG di Ymir*: "**Inquisitore Letio** … trasferitosi a **Solantia**." In our model the Letio state church *is* Mithra's, so this is one identity — but normalize the wording (and Solantia/Solanthya per HIS-16) when merging.

5. **Tofango's end.** Canon `[CANON]` (characters.md, magic.md): the demon-axe drove him mad and "he **ended his life as a hermit** atop a remote mountain." *2011 - Back to war!* lists **Tofango as a living NPC** in a later era. Either the campaign predates his hermit-death (possible), or it extends his life again. Flag on the characters.md entry; don't rewrite his ending yet.

6. **The Ulan-Tang "famiglia nobiliare dei Ra."** *PG di Ymir* assigns War-Ra (and by pattern Allanon-Ra) to a noble family "**Ra**"; canon `geography.md` lists **five** Ulan-Tang houses — **Ishra, Tyarreth, Miraz, Gaib, Gadash** (name-pattern: Asternak-**Gaib**, Sazar-**Gadash**, Bal-**Ishra**). "Ra" is either a sixth family, a short form of Ishra, or an inconsistency. Minor; flag in conflicts.md.

7. **Corvinus's player** — Daniel (*PG di Ymir*) vs. Mura (*2011*). Table-history trivia; note only so the two records aren't "corrected" against each other.

*(Known conflicts that this import merely re-states — the Entità Sovereign-Demon roster variants (Abbadon/Ea-oyster vs. our Player-Guide table), the Elemental-Lords-mortal line, Meridian-as-city, Cronologia's two-way elf schism — were all present in the earlier export, are recorded in our digests, and are already governed by existing decisions/entries. Nothing new to log from them.)*

---

## 5. Campaign-page finds

### "2011 - Back to war!" — the one genuinely new campaign page
*(Categories: Campaign Report; last edited 2023-05-24; Italian; telegraphic outline style.)*

**Cast — PCs (character (epithet), player):**
- **War-Ra** (Secundus) — Chini *(returning; Ulan-Tang assassin of the Ra family)*
- **Gundar il Massacratore** (Primus) — Tarter *(returning)*
- **Alexander Corvinus** (Il Perfetto) — Mura
- **Allanon-Ra** (Pojer) — Pojer
- **???** (???) — Adami *(a fifth PC, never named on the page)*

**Cast — NPCs:** **Topramesk il Giallo**, **Heinrich Kramer**, **Tofango**.

**Synopsis by chapter:**
1. *Layers of Past and Future* — party assembly (the Primus/Secundus "layers" framing is unexplained on the page).
2. *A World at War* — Ymir shaken by a **world war** among **M'Raker's undead**, the **Federazione Letia**, and the **Cani del Qi-Long** led by the **awakened and reunited Dragons**. The PCs are in **Armora**, besieged by the undead; **Armora falls**. They discover **the gods are no longer on Ymir — banished by a powerful sorcerer**.
3. *M'Raker* — the sorcerer-king of the undead is **M'Raker = (Heinrich) Kramer**. Sought in the unnamed desert ("deserto di Xxx"), he proves to be a **lich**; his **phylactery is in the Ophiur**. The party travels via **Cartosa** to the **Ophirite coasts** hunting it.
4. *Il ritorno degli Dei* — the PCs must find a way to **bring gods back into Ymir's universe**, and must **choose carefully which ones**; **Kramer will disguise himself as a divinity** to slip back onto Ymir as a **demigod**.

**Canonical-event candidates** (pending the §4.3 placement ruling): fall of Armora to the undead; the banishment and selective restoration of the gods; M'Raker's phylactery-in-Ophiur; the dragons' reunification behind the Qi-Long armies; existence of a "Federazione Letia."

**Named characters we lack** (→ `characters.md`): **M'Raker** (as Kramer's lich identity), **Alexander Corvinus**, **Allanon-Ra**, **Ferdinando Montecarlos** (via the sibling *PG di Ymir* edit); plus promotion of **War-Ra** from digest-only to canon.

### All other campaign pages
*Gate to Unknown* (7.6k words — identical to our `riassunto-sessioni-prima-di-luned-04-06-2007.txt`; the Fandom title confirms the campaign's proper name), *A Steamclad Sky*, *A Black Sun Rising*, *The Monster Mash*, *La Leggenda delle Rune Magiche*, and the *La caduta di Helgedad* stub are **unchanged** from the earlier export and already fully mined (digest: `sources/extracted/wiki/history-campaigns.md`; canon: `history.md` §"Canonical campaign events", `characters.md`). No new events or names found in them by the diff.

---

*Report generated 2026-07-10. Diff artifacts: shingle/sequence comparison scripts in the session scratchpad; ground truth pairs = `sources/extracted/wiki-worldofymir/*.md` (Fandom, this folder) vs. `sources/raw/*.txt` (earlier Wikidot-style export).*
