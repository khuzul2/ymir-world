#!/usr/bin/env python3
"""Build a single, self-contained HTML edition of The Ymir Compendium
from the Markdown chapters in manual/.  A4, two-column, black-on-white,
restrained 'illuminated manuscript' styling."""
import re, html, os, sys
from datetime import datetime, timezone

SRC = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(SRC)
MANUAL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "manual")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(MANUAL, "ymir-compendium.html")

FILES = [
    "00-front-matter.md", "00b-the-last-curator.md",
    "01-cosmogonia.md", "02-gods.md", "03-magic.md",
    "04-ages.md", "05-lay-of-the-land.md", "06-letia.md", "06b-censored-leaf.md",
    "07-young-kingdoms.md", "08-helgedad.md", "09-qi-long.md", "09b-xebech.md",
    "10-cartosa.md", "10b-sounding-report.md", "10c-silver-isles.md",
    "11-gaerwath-elves.md", "12-sadhir-deserts.md", "12b-ophiur.md",
    "12c-dreamlands.md", "12d-belligerent-kingdoms.md", "13-peoples.md",
    "14-beasts.md", "14b-figures-of-renown.md", "15-behind-the-veil.md",
    "15b-workbook.md", "15c-coda.md", "16-appendices.md",
]

# short narrator lines for the table of contents, keyed by file
NARRATOR = {
    "00b-the-last-curator.md": "the last Curator — who gathered the marked copies",
    "01-cosmogonia.md": "Xochiyayotl of Xebech, Star-Priest of the eldest people",
    "02-gods.md": "Fra' Teodabir, torch-priest of Hokhmah",
    "03-magic.md": "Sir Drusilde, Archmage of the Seventh Circle",
    "04-ages.md": "the Annalist of Solanthya",
    "05-lay-of-the-land.md": "the sea-diary of Ramiro Estioca of Cartosa",
    "06-letia.md": "the Annalist of Solanthya",
    "06b-censored-leaf.md": "the Clericate's rolls, strikes showing",
    "07-young-kingdoms.md": "The Armora Crier, a broadsheet",
    "08-helgedad.md": "Hrafnkel Ognirsson, skald of the Nortmaar",
    "09-qi-long.md": "the Pilgrim of the Thundering Gate",
    "09b-xebech.md": "Xochiyayotl, returning — a letter to a dead pupil",
    "10-cartosa.md": "Ramiro Estioca, with a factor's ledgers",
    "10b-sounding-report.md": "the Sohleugir, rendered by Sirvaneth of Elendor",
    "10c-silver-isles.md": "the Curator, in body-text at last",
    "11-gaerwath-elves.md": "Aelryn Vhaeloth i-Celeblyar, Dark-Elf Loremaster",
    "12-sadhir-deserts.md": "Adhima the Rakhama'i & Yusuf al-Marrah",
    "12b-ophiur.md": "Nyema of Ga'Namesh, Keeper of the Thousand Songs",
    "12c-dreamlands.md": "Hesper Vaneck of Armora, dream-pilot",
    "12d-belligerent-kingdoms.md": "Marghuz, through two disagreeing interpreters",
    "13-peoples.md": "Pips Quondam, a Tal-Tanoth traveller",
    "14-beasts.md": "Weck of the Long Road, huntsman of Therìos",
    "14b-figures-of-renown.md": "Frater Remigius Falx, Canon-Historian of the Holy Office",
    "15-behind-the-veil.md": "the Veiled Hand — GAME MASTER ONLY",
    "15b-workbook.md": "the Veiled Hand's Workbook — GAME MASTER ONLY",
    "15c-coda.md": "a note left unanswered",
    "16-appendices.md": "the Curator",
}

# ----------------------------------------------------------------------------
# inline markdown

def inline(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    codes = []
    def code_sub(m):
        codes.append(html.escape(m.group(1)))
        return '\x00%d\x00' % (len(codes) - 1)
    text = re.sub(r'`([^`]+)`', code_sub, text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
    text = re.sub('\x00(\\d+)\x00', lambda m: '<code>' + codes[int(m.group(1))] + '</code>', text)
    return text

# ----------------------------------------------------------------------------
# block tokeniser

def tokenise(md):
    lines = md.split('\n')
    blocks = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if s == '':
            i += 1; continue
        if s == '---':
            blocks.append(('hr',)); i += 1; continue
        if line.startswith('#'):
            m = re.match(r'(#+)\s*(.*)', line)
            blocks.append(('h', len(m.group(1)), m.group(2).strip())); i += 1; continue
        if line.startswith('>'):
            q = []
            while i < n and lines[i].startswith('>'):
                content = lines[i][1:]
                if content.startswith(' '):
                    content = content[1:]
                q.append(content.rstrip())
                i += 1
            blocks.append(('quote', q)); continue
        if re.match(r'\s*-\s+', line):
            items = []
            while i < n and re.match(r'\s*-\s+', lines[i]):
                item = re.sub(r'\s*-\s+', '', lines[i], count=1).strip()
                i += 1
                while (i < n and lines[i].strip() and not re.match(r'\s*-\s+', lines[i])
                       and not lines[i].startswith(('#', '>', '|')) and lines[i].strip() != '---'):
                    item += ' ' + lines[i].strip(); i += 1
                items.append(item)
            blocks.append(('ul', items)); continue
        if line.startswith('|'):
            t = []
            while i < n and lines[i].startswith('|'):
                t.append(lines[i]); i += 1
            blocks.append(('table', t)); continue
        # paragraph
        p = [line.strip()]; i += 1
        while (i < n and lines[i].strip() and not lines[i].startswith(('#', '>', '|'))
               and not re.match(r'\s*-\s+', lines[i]) and lines[i].strip() != '---'):
            p.append(lines[i].strip()); i += 1
        blocks.append(('p', ' '.join(p)))
    return blocks

# ----------------------------------------------------------------------------
# quote classification & rendering

def classify(qlines):
    full = ' '.join(x for x in qlines if x)
    low = full.lower()
    if any(x and x.lstrip('> ').startswith('✒') for x in qlines):
        return 'postil'
    if 'in the margin' in low or 'gm only' in low:
        return 'margin'
    if "curator's note" in low or low.rstrip().endswith('the curator*') or low.rstrip().endswith('the curator'):
        return 'curator'
    if 'al-marrah' in low:
        return 'rebuttal'
    if "factor's ledger" in low or 'factor’s ledger' in low:
        return 'ledger'
    first = next((x for x in qlines if x), '')
    if not first.lstrip().startswith('*'):
        return 'verse'
    return 'quote'

def split_paras(qlines):
    paras, cur = [], []
    for l in qlines:
        if l.strip() == '':
            if cur: paras.append(' '.join(cur)); cur = []
        else:
            cur.append(l.strip())
    if cur: paras.append(' '.join(cur))
    return paras

# reader-marginalia ("postils") — per-hand sigil + ink class, matched by a keyword
# in the byline. Order matters: more specific keys first.
HANDS = [
    ('xochiyayotl', '✧', 'xochi'),
    ('morannagul', '❈', 'moran'),
    ('yellow', '◐', 'yellow'),
    ('barely a hand', '✝', 'struck'), ('the same hand', '✝', 'struck'),
    ('kramer', '✝', 'struck'), ('m——', '✝', 'struck'),
    ('the night', '▬', 'night'),
    ('nefthi', '☥', 'pharaoh'), ('pharaoh', '☥', 'pharaoh'),
    ('leonard', '▽', 'leonard'), ('**l.**', '▽', 'leonard'),
    ('censor', '✠', 'censor'),
    ('last curator', '⌘', 'keeper'),
    ('cadet', '✎', 'cadet'),
    ('crier', '▤', 'crier'),
    ('bravaso', '§', 'bravaso'),
    ('al-marrah', '‡', 'yusuf'), ('yusuf', '‡', 'yusuf'),
    ('drusilde', '⟐', 'drusilde'),
    ('adept-hunter', '⊕', 'adepthunter'), ('adept hunter', '⊕', 'adepthunter'),
    ('loregar', '⌖', 'loregar'),
]

def hand_style(meta_low):
    for key, sigil, cls in HANDS:
        if key in meta_low:
            return sigil, cls
    return '✒', 'humble'

def render_postils(qlines):
    out = ['<div class="postils">']
    for raw in qlines:
        if not raw.strip():
            continue
        m = re.match(r'^((?:>\s*)*)', raw)
        depth = raw[:m.end()].count('>')
        line = raw[m.end():].lstrip()
        if not line.startswith('✒'):
            out.append('<div class="postil-cont">%s</div>' % inline(line))
            continue
        line = line[1:].strip()
        if ' — ' in line:
            meta, body = line.split(' — ', 1)
        else:
            meta, body = line, ''
        sigil, cls = hand_style(meta.lower())
        depth_cls = ' postil-reply' if depth >= 1 else ''
        indent = ' style="margin-left:%dmm"' % (6 * depth) if depth else ''
        inner = ('<span class="postil-sigil">%s</span> '
                 '<span class="postil-by">%s</span>' % (sigil, inline(meta)))
        if body:
            inner += ' <span class="postil-text">%s</span>' % inline(body)
        out.append('<div class="postil hand-%s%s"%s>%s</div>' % (cls, depth_cls, indent, inner))
    out.append('</div>')
    return '\n'.join(out)

def render_quote(qlines):
    kind = classify(qlines)
    if kind == 'postil':
        return render_postils(qlines)
    if kind == 'verse':
        rows = []
        for l in qlines:
            rows.append(inline(l.strip()) if l.strip() else '')
        body = '<br>\n'.join(r if r else '<span class="sp"></span>' for r in rows)
        return '<div class="verse">%s</div>' % body

    paras = split_paras(qlines)
    label = None
    if kind == 'margin':
        # peel the "⟡ IN THE MARGIN ⟡" label line at the raw-line level so the
        # body paragraphs (which follow on separate lines) are preserved
        raw = list(qlines)
        joined_upper = ' '.join(raw).upper()
        idx = next((k for k, l in enumerate(raw) if l.strip()), None)
        firstclean = re.sub(r'[⟡*\s]', '', raw[idx]).upper() if idx is not None else ''
        if firstclean.startswith('INTHEMARGIN'):
            label = 'In the Margin · the Veiled Hand'
            del raw[idx]
            paras = split_paras(raw)
        elif 'GM ONLY' in joined_upper:
            label = 'For the Game Master alone'
            paras = split_paras([l.replace('⟡', '') for l in raw])
        else:
            label = 'In the Margin · the Veiled Hand'
            paras = split_paras(raw)
    elif kind == 'curator':
        label = "The Curator"
        if paras:
            paras[0] = re.sub(r"^\*Curator's note\.\*\s*", "", paras[0])
    elif kind == 'rebuttal':
        label = 'A rebuttal, in the margin'
    elif kind == 'ledger':
        label = "The Factor's ledger"

    inner = ''
    if label:
        inner += '<div class="aside-label">%s</div>' % html.escape(label)
    for p in paras:
        inner += '<p>%s</p>' % inline(p)
    return '<aside class="aside %s">%s</aside>' % (kind, inner)

def render_table(tlines):
    rows = []
    for tl in tlines:
        cells = [c.strip() for c in tl.strip().strip('|').split('|')]
        rows.append(cells)
    # drop separator row (---)
    sep = lambda r: all(set(c) <= set('-: ') and c for c in r)
    out = ['<table>']
    header_done = False
    for idx, r in enumerate(rows):
        if sep(r):
            header_done = True; continue
        tag = 'th' if (idx == 0) else 'td'
        out.append('<tr>' + ''.join('<%s>%s</%s>' % (tag, inline(c), tag) for c in r) + '</tr>')
    out.append('</table>')
    return '\n'.join(out)

def render_block(b, in_body, state):
    t = b[0]
    if t == 'hr':
        return '<div class="rule">❧</div>'
    if t == 'h':
        lvl = min(b[1], 4)
        return '<h%d>%s</h%d>' % (lvl, inline(b[2]), lvl)
    if t == 'quote':
        return render_quote(b[1])
    if t == 'ul':
        return '<ul>' + ''.join('<li>%s</li>' % inline(it) for it in b[1]) + '</ul>'
    if t == 'table':
        return render_table(b[1])
    if t == 'p':
        text = b[2] if len(b) > 2 else b[1]
        stripped = text.strip()
        cls = []
        if stripped.startswith('*Colophon.*'):
            return '<p class="colophon">%s</p>' % inline(stripped)
        if stripped.startswith('**') and stripped.endswith('**') and stripped.count('**') == 2:
            cls.append('attribution')
        if stripped.startswith('*(') and stripped.endswith(')*'):
            cls.append('sketch')
        if in_body and not state.get('dropped') and 'attribution' not in cls:
            cls.append('dropcap'); state['dropped'] = True
        c = ' class="%s"' % ' '.join(cls) if cls else ''
        return '<p%s>%s</p>' % (c, inline(stripped))
    return ''

# ----------------------------------------------------------------------------
# section assembly

def split_sections(blocks):
    hr_idx = [i for i, b in enumerate(blocks) if b[0] == 'hr']
    first_hr = hr_idx[0] if hr_idx else len(blocks)
    colo = None
    for i, b in enumerate(blocks):
        if b[0] == 'p' and b[1].lstrip().startswith('*Colophon.*'):
            colo = i
    head = blocks[:first_hr]
    if colo is not None:
        body = blocks[first_hr + 1:colo]
        colophon = blocks[colo]
    else:
        body = blocks[first_hr + 1:]
        colophon = None
    while body and body[-1][0] == 'hr':
        body = body[:-1]
    return head, body, colophon

def render_head(head):
    out = []
    for b in head:
        out.append(render_block(b, False, {}))
    return '\n'.join(out)

def render_body(body):
    state = {}
    out = []
    for b in body:
        out.append(render_block(b, True, state))
    return '\n'.join(out)

def render_chapter(fid, blocks, is_gm=False):
    head, body, colophon = split_sections(blocks)
    parts = ['<section class="sheet chapter%s" id="%s">' % (' gm' if is_gm else '', fid)]
    parts.append('<header class="chapter-head">')
    parts.append(render_head(head))
    parts.append('</header>')
    parts.append('<div class="body">')
    parts.append(render_body(body))
    parts.append('</div>')
    if colophon:
        parts.append('<div class="colophon-wrap">%s</div>' % render_block(colophon, False, {}))
    parts.append('</section>')
    return '\n'.join(parts)

# ----------------------------------------------------------------------------

def build():
    sections = []

    # --- file 00 : split into cover + preface ---------------------------------
    md0 = open(os.path.join(MANUAL, FILES[0]), encoding='utf-8').read()
    blk0 = tokenise(md0)
    head0, body0, colo0 = split_sections(blk0)
    # cover from head0 (title lines are h1/h3/h4)
    cover_title = next((b[2] for b in head0 if b[0] == 'h' and b[1] == 1), 'THE YMIR COMPENDIUM')
    cover_subs = [b[2] for b in head0 if b[0] == 'h' and b[1] > 1]
    cover = ['<section class="sheet cover" id="cover">']
    cover.append('<div class="cover-inner">')
    cover.append('<div class="cover-orn">✵</div>')
    cover.append('<h1 class="cover-title">%s</h1>' % inline(cover_title))
    if cover_subs:
        cover.append('<p class="cover-sub">%s</p>' % inline(cover_subs[0]))
    cover.append('<div class="cover-rule">❦ ✵ ❧</div>')
    cover.append('<p class="cover-imprint">Assembled at the Crystal Seat of Elendor<br>'
                 'in the years of the New Equilibrium &middot; ~3518 <span class="sc">d.M.</span></p>')
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    cover.append('<p class="cover-stamp">this impression last edited %s</p>' % stamp)
    cover.append('</div></section>')
    sections.append('\n'.join(cover))

    # preface = body0 (starts with "## Preface of the Curator")
    pref = ['<section class="sheet chapter" id="preface">']
    pref.append('<div class="body">')
    st = {}
    for b in body0:
        pref.append(render_block(b, True, st))
    pref.append('</div>')
    if colo0:
        pref.append('<div class="colophon-wrap">%s</div>' % render_block(colo0, False, {}))
    pref.append('</section>')
    preface_html = '\n'.join(pref)

    # --- table of contents ----------------------------------------------------
    toc = ['<section class="sheet toc" id="toc">']
    toc.append('<h1 class="toc-title">The Compendium</h1>')
    toc.append('<p class="toc-lead">being a true gathering of the tales, histories, and doctrines '
               'of the world of Ymir, as its own peoples tell them</p>')
    toc.append('<div class="rule">❧</div>')
    toc.append('<ol class="toc-list">')
    toc.append('<li><a href="#preface"><span class="toc-ch">Preface of the Curator</span>'
               '<span class="toc-nar">the Curator</span></a></li>')

    chapter_htmls = []
    for fid_i, fname in enumerate(FILES[1:], start=1):
        md = open(os.path.join(MANUAL, fname), encoding='utf-8').read()
        blocks = tokenise(md)
        sid = 'ch%02d' % fid_i
        is_gm = 'behind-the-veil' in fname
        head, _, _ = split_sections(blocks)
        title = next((b[2] for b in head if b[0] == 'h' and b[1] == 1), fname)
        nar = NARRATOR.get(fname, '')
        gmc = ' class="gm"' if is_gm else ''
        toc.append('<li%s><a href="#%s"><span class="toc-ch">%s</span>'
                   '<span class="toc-nar">%s</span></a></li>'
                   % (gmc, sid, inline(title), inline(nar)))
        chapter_htmls.append(render_chapter(sid, blocks, is_gm))

    toc.append('</ol>')
    toc.append('<p class="toc-foot">The body of each chapter is its author’s own account. '
               'Notes marked <em>the Curator</em> reconcile the voices; the shaded margins of '
               '<em>the Veiled Hand</em> are for the Game Master alone.</p>')
    toc.append('</section>')
    toc_html = '\n'.join(toc)

    body_html = '\n'.join(sections + [toc_html, preface_html] + chapter_htmls)
    return CSS_TEMPLATE.replace('__BODY__', body_html)

# ----------------------------------------------------------------------------
CSS_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Ymir Compendium</title>
<style>
:root{
  --ink:#1c1712;
  --page:#ffffff;
  --desk:#d9d3c4;
  --rubric:#7b1f1e;      /* manuscript red */
  --rubric-soft:#8c3b32;
  --gilt:#8a6d2f;        /* muted gold-brown */
  --muted:#5c5346;
  --line:#d9cdb2;
  --gm-panel:#eceae3;
  --gm-line:#3a3a44;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua","URW Palladio L",Georgia,"Times New Roman",serif;
  --display:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{
  background:var(--desk);
  color:var(--ink);
  font-family:var(--serif);
  font-size:10.6pt;
  line-height:1.5;
  -webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 50% -10%, #e7e1d3 0%, #d9d3c4 55%, #cfc8b6 100%);
  background-attachment:fixed;
}

/* ---- the A4 sheet ---- */
.sheet{
  width:210mm;
  min-height:297mm;
  margin:9mm auto;
  padding:22mm 20mm 20mm;
  background:var(--page);
  box-shadow:0 2px 6px rgba(40,30,15,.28),0 14px 40px rgba(40,30,15,.22);
  position:relative;
  border:1px solid #efe9db;
}
.sheet::before{ /* faint inner keyline, like a printed border */
  content:"";position:absolute;inset:9mm;
  border:1px solid #e9e1cc;pointer-events:none;
}
.sheet.cover::before{inset:12mm;border:1px double var(--gilt);}

/* ---- cover ---- */
.cover{display:flex;align-items:center;justify-content:center;text-align:center;}
.cover-inner{max-width:150mm;padding:0 6mm;}
.cover-orn{font-size:34pt;color:var(--rubric);line-height:1;margin-bottom:10mm;}
.cover-title{
  font-family:var(--display);
  font-size:40pt;line-height:1.02;margin:0 0 8mm;
  color:var(--rubric);
  letter-spacing:.04em;font-weight:600;
  text-transform:uppercase;
}
.cover-sub{font-size:14pt;font-style:italic;color:var(--ink);margin:0 0 5mm;line-height:1.35;}
.cover-sub2{font-size:11pt;color:var(--muted);margin:0 0 10mm;font-style:italic;}
.cover-rule{color:var(--gilt);font-size:15pt;letter-spacing:.5em;margin:6mm 0 9mm;}
.cover-imprint{font-size:10.5pt;color:var(--muted);line-height:1.7;letter-spacing:.02em;}
.cover-stamp{margin-top:2.2em;font-size:8pt;color:var(--muted);opacity:.75;font-style:italic;letter-spacing:.04em;}
.sc{font-variant:small-caps;letter-spacing:.05em;}

/* ---- table of contents ---- */
.toc-title{font-family:var(--display);text-align:center;color:var(--rubric);
  font-size:26pt;letter-spacing:.06em;text-transform:uppercase;margin:4mm 0 3mm;font-weight:600;}
.toc-lead{text-align:center;font-style:italic;color:var(--muted);max-width:130mm;margin:0 auto 4mm;}
.toc-list{list-style:none;margin:6mm 0 0;padding:0;}
.toc-list li{border-bottom:1px dotted var(--line);}
.toc-list a{display:flex;align-items:baseline;gap:1.2em;text-decoration:none;color:var(--ink);
  padding:2.9mm 2mm;}
.toc-list a:hover{background:#faf6ec;}
.toc-list a::before{content:"\2767";color:var(--gilt);font-size:8pt;flex:0 0 auto;
  position:relative;top:-.15em;}
.toc-ch{font-size:11.4pt;flex:1;}
.toc-nar{font-style:italic;color:var(--muted);font-size:9.4pt;text-align:right;max-width:56mm;}
.toc-list li.gm .toc-ch{color:var(--gm-line);}
.toc-list li.gm .toc-nar{color:var(--gm-line);font-variant:small-caps;letter-spacing:.04em;}
.toc-foot{margin-top:8mm;font-size:9.4pt;color:var(--muted);font-style:italic;text-align:center;
  border-top:1px solid var(--line);padding-top:4mm;}

/* ---- chapter head ---- */
.chapter-head{margin-bottom:8mm;text-align:center;}
.chapter-head h1{
  font-family:var(--display);
  color:var(--rubric);
  font-size:21pt;line-height:1.12;margin:0 0 3mm;
  letter-spacing:.04em;text-transform:uppercase;font-weight:600;
}
.chapter-head h2{
  font-family:var(--display);
  font-size:12.5pt;font-weight:400;font-style:italic;color:var(--ink);
  margin:0 auto 5mm;max-width:150mm;line-height:1.35;
}
.chapter-head h3,.chapter-head h4{font-family:var(--display);font-weight:400;}
.chapter-head p.attribution{
  font-size:10pt;color:var(--muted);max-width:150mm;margin:0 auto;
  font-style:normal;line-height:1.4;
}
.chapter-head p.attribution strong{font-weight:400;font-style:italic;}
.chapter-head .aside{max-width:160mm;margin-left:auto;margin-right:auto;text-align:left;}
.chapter-head::after{content:"\2766 \2735 \2767";display:block;color:var(--gilt);
  letter-spacing:.4em;font-size:11pt;margin-top:6mm;}

/* preface has no head; give its first heading rubric treatment */
#preface .body h2{color:var(--rubric);}

/* ---- two-column body ---- */
.body{
  column-count:2;
  column-gap:9mm;
  column-rule:1px solid #ece5d3;
  text-align:justify;
  hyphens:auto;
  -webkit-hyphens:auto;
}
.body p{margin:0 0 2.6mm;orphans:2;widows:2;}
.body p.sketch{font-style:italic;color:var(--muted);text-align:center;}
.body h2,.body h3,.body h4{
  column-span:all;
  font-family:var(--display);
  color:var(--rubric-soft);
  text-align:left;
  margin:5mm 0 3mm;
  line-height:1.2;
}
.body h2{font-size:14pt;letter-spacing:.02em;border-bottom:1px solid var(--line);padding-bottom:2mm;}
.body h3{font-size:12pt;font-style:italic;color:var(--gilt);}
.body h4{font-size:11pt;font-style:italic;color:var(--muted);}
.body > h2:first-child,.body > h3:first-child{margin-top:0;}

/* drop cap */
.body p.dropcap::first-letter{
  font-family:var(--display);
  float:left;font-size:40pt;line-height:.82;
  padding:2mm 2mm 0 0;color:var(--rubric);font-weight:600;
}

/* lists */
.body ul{margin:0 0 3mm;padding-left:5mm;list-style:none;}
.body ul li{margin:0 0 1.8mm;position:relative;padding-left:4mm;}
.body ul li::before{content:"\2767";position:absolute;left:-1mm;color:var(--gilt);font-size:8pt;top:.2em;}

/* ---- asides (span both columns) ---- */
.aside{
  column-span:all;
  margin:4mm 0;
  padding:4mm 5mm 3mm;
  font-size:9.7pt;
  line-height:1.42;
  text-align:left;
  hyphens:none;
}
.aside p{margin:0 0 2mm;}
.aside p:last-child{margin-bottom:0;}
.aside-label{
  font-family:var(--display);
  font-variant:small-caps;letter-spacing:.12em;
  font-size:8.6pt;margin-bottom:2mm;
}

/* curator: scholarly, warm, understated */
.aside.curator{
  border-left:2px solid var(--gilt);
  background:#fbf8f0;
  font-style:italic;
  color:#40372a;
}
.aside.curator .aside-label{color:var(--gilt);font-style:normal;}

/* the factor's ledger & the rebuttal voice */
.aside.ledger{
  border-left:2px solid #b9a06a;background:#faf7ee;color:#4a4234;font-style:italic;
}
.aside.ledger .aside-label{color:var(--gilt);font-style:normal;}
.aside.rebuttal{
  border-left:3px double var(--rubric-soft);background:#faf4f1;color:#3a2723;
  margin-left:8mm;
}
.aside.rebuttal .aside-label{color:var(--rubric-soft);font-style:normal;}
.aside.quote{border-left:2px solid var(--line);background:#faf8f2;font-style:italic;color:#443b2d;}

/* the Veiled Hand — GM margins: a shaded, bordered panel that reads 'other' */
.aside.margin{
  background:var(--gm-panel);
  border:1px solid #c8c6bd;
  border-left:4px solid var(--gm-line);
  color:#24242c;
  font-style:italic;
  box-shadow:inset 0 0 0 1px #f4f3ee;
}
.aside.margin .aside-label{
  color:var(--gm-line);font-style:normal;
  display:flex;align-items:center;gap:.5em;
}
.aside.margin .aside-label::before{content:"\27E1";font-size:11pt;font-style:normal;}
.aside.margin p{color:#2b2b33;}

/* postils — reader-marginalia accreted over time (a hand per ink) */
.postils{margin:2.4mm 0;}
.postil{
  font-family:var(--serif);font-style:italic;font-size:8.8pt;line-height:1.42;
  margin:1.5mm 0;padding:.6mm 0 .6mm 3mm;border-left:2px solid currentColor;
  color:var(--muted);
}
.postil-reply{border-left-style:dotted;}
.postil-sigil{font-style:normal;font-weight:700;margin-right:.35em;}
.postil-by{font-weight:700;font-style:normal;}
.postil-by em{font-weight:400;font-style:italic;opacity:.75;}
.postil-cont{font-style:italic;font-size:8.8pt;color:var(--muted);padding-left:3mm;}
.postil del{color:var(--rubric);text-decoration:line-through;}
.hand-xochi{color:#7f8ba0;}
.hand-moran{color:#5b4a86;}
.hand-yellow{color:#a9801a;}
.hand-struck{color:#6e4f3a;}
.hand-night{color:#3a3d44;}
.hand-pharaoh{color:#9c7c2e;}
.hand-leonard{color:#9a3f45;}
.hand-censor{color:#a12f2c;}
.hand-keeper{color:#6f6650;}
.hand-cadet{color:#5f6b78;}
.hand-crier{color:#5f5a4f;}
.hand-bravaso{color:#7a6444;}
.hand-yusuf{color:#8a6a3d;}
.hand-drusilde{color:#2f8a80;}
.hand-adepthunter{color:#6b4a2f;}
.hand-loregar{color:#566b6b;}
.hand-humble{color:#8a7a63;}

/* verse (the skald) */
.verse{
  column-span:all;
  margin:4mm auto;
  padding:2mm 0;
  text-align:center;
  font-style:italic;
  color:#463a2a;
  font-size:10.4pt;
  line-height:1.5;
  border-top:1px solid var(--line);
  border-bottom:1px solid var(--line);
}
.verse .sp{display:inline-block;height:.6em;}

/* tables (appendices) */
.body table{
  column-span:all;
  width:100%;border-collapse:collapse;margin:3mm 0 5mm;font-size:9.4pt;
}
.body th{
  font-family:var(--display);text-align:left;background:#f3ecd9;color:var(--ink);
  border-bottom:1.5px solid var(--gilt);padding:2mm 2.5mm;font-weight:600;font-style:italic;
}
.body td{border-bottom:1px solid #e7dfca;padding:1.8mm 2.5mm;vertical-align:top;}
.body tr:nth-child(even) td{background:#faf7ee;}

/* rules / dividers */
.rule{text-align:center;color:var(--gilt);font-size:13pt;margin:5mm 0;letter-spacing:.3em;}
.body .rule{column-span:all;}

/* colophon */
.colophon-wrap{margin-top:8mm;padding-top:4mm;border-top:1px solid var(--line);}
.colophon{font-size:8.5pt;color:var(--muted);line-height:1.4;text-align:left;font-style:italic;}
.colophon code{font-style:normal;}

/* inline code (file references) */
code{
  font-family:"Iowan Old Style",Palatino,Georgia,serif;
  font-style:italic;font-size:.94em;color:var(--gilt);
  background:#f6f2e6;padding:0 .2em;border-radius:2px;
}
.aside code,.colophon code{background:transparent;padding:0;}
strong{font-weight:600;}
.body em,.aside em{}

/* ---- GM chapter (Behind the Veil) gets a distinct edge ---- */
.sheet.gm{background:#fbfbf9;}
.sheet.gm::before{border-color:#cfcfc8;}
.sheet.gm .chapter-head h1{color:var(--gm-line);}
.sheet.gm .chapter-head h2{color:#33333c;}
.sheet.gm .body h2{color:var(--gm-line);border-color:#d5d5cd;}
.sheet.gm .body h3{color:#5a5a4a;}
.sheet.gm .body p.dropcap::first-letter{color:var(--gm-line);}
.sheet.gm .chapter-head::after{color:var(--gm-line);}

/* ---- responsive: phones read single-column ---- */
@media (max-width:820px){
  body{font-size:11pt;}
  .sheet{width:auto;min-height:0;margin:4mm;padding:9mm 6mm;}
  .sheet::before{inset:4mm;}
  .body{column-count:1;}
  .cover-title{font-size:30pt;}
  .toc-list a{flex-wrap:wrap;}
  .toc-nar{text-align:left;max-width:none;flex-basis:100%;}
  .aside.rebuttal{margin-left:3mm;}
}

/* ---- print: real A4 pages ---- */
@media print{
  body{background:#fff;background-image:none;}
  .sheet{
    width:auto;min-height:0;margin:0;padding:0;
    box-shadow:none;border:none;break-before:page;
  }
  .sheet:first-of-type{break-before:auto;}
  .sheet::before{display:none;}
  .cover{min-height:90vh;}
  a{color:inherit;text-decoration:none;}
  @page{size:A4;margin:18mm 16mm;}
}
</style>
</head>
<body>
__BODY__
</body>
</html>
"""

if __name__ == '__main__':
    out = build()
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)
    print("wrote", OUT, "(%d bytes)" % len(out.encode('utf-8')))
