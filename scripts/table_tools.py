"""Semantic, accessible table rendering. No column-number based recall logic."""
from __future__ import annotations
import hashlib
from pathlib import Path
import re
from bs4 import BeautifulSoup, NavigableString

EFFECT_LABELS = {
 'L': 'Lenition of the following closely connected word',
 'N': 'Nasalization of the following closely connected word',
 'H': 'Historical aspiration or gemination of the following word; often unwritten',
 '0': 'No regular L, N or H effect prescribed by this form',
}
CASE_HELP = {
 'Nom': 'Nominative: typically the subject or a predicate noun',
 'Gen': 'Genitive: typically a dependent noun: of ...',
 'Prep': 'Prepositional (called dative in other grammars): the case governed by many prepositions',
 'Dat': 'Dative (Stifter: prepositional): indirect object and the case after many prepositions',
 'Acc': 'Accusative: typically the direct object; also governed by some prepositions',
 'Voc': 'Vocative: direct address; the particle a has its own incoming lenition',
}
FORM_HEADERS = {
 'form','phrase','example phrase','element / form','abs form',
 'conj form after n\u00ed','sg form','pl form',
 'sg form + effect','pl form + effect',
 'sg article + effect','pl article + effect',
 'sg fused form + effect','pl fused form + effect','poss form + effect',
}


GLOSS = {
 'nom':'nominative','gen':'genitive','prep':'prepositional (Stifter\u2019s name for the dative)','acc':'accusative','voc':'vocative','dat':'dative',
 'sg':'singular','pl':'plural','masc':'masculine','fem':'feminine','neut':'neuter',
 'abs':'absolute','conj':'conjunct','deut':'deuterotonic','prot':'prototonic',
 'pres':'present','pret':'preterite','impf':'imperfect','fut':'future','cond':'conditional',
 'ind':'indicative','subj':'subjunctive','impv':'imperative','pass':'passive',
 'depo':'deponent','caus':'causative','iter':'iterative','denom':'denominative',
 'vn':'verbal noun','rel':'relative','poss':'possessive','dem':'demonstrative',
 'pal':'palatalized','npal':'non-palatalized',
}
_ORD = {'1':'1st','2':'2nd','3':'3rd'}
# "ind" is also an Old Irish word, so it counts as an abbreviation only after "pres".
GLOSS_RE = re.compile(r'\b(?:[123](?:sg|pl)|pres ind|' + '|'.join(sorted((k for k in GLOSS if k != 'ind'), key=len, reverse=True)) + r')\b', re.I)
GLOSS_SKIP = {'script','style','title','em','strong','code','pre','button'}


def gloss_title(token):
    low = token.lower()
    if low == 'pres ind': return 'present indicative'
    if low[0] in _ORD and low[1:] in ('sg','pl'):
        return f"{_ORD[low[0]]} person {GLOSS[low[1:]]}"
    return GLOSS.get(low)


def add_gloss(soup):
    """Wrap morphology abbreviations in <abbr class="gl"> (rendered in small capitals by CSS)."""
    for text in list(soup.find_all(string=GLOSS_RE)):
        if any(p.name in GLOSS_SKIP or 'hero-word' in (p.get('class') or []) or 'option' in (p.get('class') or [])
               or p.name == 'li' and p.find_parent('details') and p.find_parent('details').find('summary', string=re.compile('Manual answer key'))
               for p in text.parents if p.name):
            continue
        out = []; last = 0
        for m in GLOSS_RE.finditer(str(text)):
            out.append(NavigableString(str(text)[last:m.start()]))
            tag = soup.new_tag('abbr', attrs={'class': 'gl', 'title': gloss_title(m.group(0))})
            tag.string = m.group(0)
            out.append(tag); last = m.end()
        out.append(NavigableString(str(text)[last:]))
        for node in out: text.insert_before(node)
        text.extract()


REFERENCE = {
 'Cases': [('nom','nominative: the subject'),('gen','genitive: of ...'),
           ('prep','prepositional: the case after many prepositions; Stifter\u2019s name for what other grammars call the dative (dat)'),
           ('acc','accusative: the object'),('voc','vocative: direct address')],
 'Number, gender, person': [('sg, pl','singular, plural'),('masc, fem, neut','masculine, feminine, neuter'),
           ('1sg, 2sg, 3sg, 1pl, 2pl, 3pl','1st, 2nd, 3rd person singular or plural')],
 'Verb forms': [('abs','absolute: ending used with nothing before the verb'),('conj','conjunct: ending used after a particle or preverb'),
           ('deut, prot','deuterotonic (stress on the 2nd element), prototonic (stress on the 1st)'),
           ('pres, pret, impf, fut, cond','present, preterite, imperfect, future, conditional'),
           ('ind, subj, impv','indicative, subjunctive, imperative'),('pass','passive'),
           ('depo','deponent: a verb with active meaning but its own endings (with an extra r)'),
           ('denom','denominative: a verb made from a noun or adjective'),
           ('caus','causative: \u2018makes someone do X\u2019'),('iter','iterative: repeated action'),
           ('vn','verbal noun: the abstract noun that does the work of an infinitive'),('rel','relative form of a verb'),
           ('poss, dem','possessive, demonstrative')],
 'Marks on the next word': [('[L]','lenition: the first consonant is softened (c, t, p become ch, th, ph; b, d, g, m, s, f are lenited too but this is often not written)'),
           ('[N]','nasalization: stops are voiced or get a nasal before them (c to g, t to d, p to b; b to mb, d to nd, g to ng), a vowel gets n-; often not written'),
           ('[H]','aspiration: h- before a vowel, doubling (gemination) of a consonant'),('[0]','no mutation')],
 'Palatalization': [('pal, npal','palatalized, non-palatalized: a consonant said with the tongue raised towards the hard palate, or not (older grammars: \u201cslender\u201d and \u201cbroad\u201d)'),
           ('C\u2032, C','Stifter\u2019s notation for a pal and an npal consonant in his ending tables'),
           ('spelling','a pal consonant is often shown by an i or e next to it (chaitt), an npal one by a, o or u (catt)')],
}


def reference_panel(soup):
    details = soup.new_tag('details', attrs={'class': 'effect-key ref-key'})
    summary = soup.new_tag('summary'); summary.string = 'Reference: abbreviations, marks on the next word, palatalization'
    details.append(summary)
    box = soup.new_tag('div', attrs={'class': 'ref-body'})
    for heading, rows in REFERENCE.items():
        sec = soup.new_tag('section'); h = soup.new_tag('h4'); h.string = heading; sec.append(h)
        dl = soup.new_tag('dl')
        for term, meaning in rows:
            dt = soup.new_tag('dt'); dt.string = term; dd = soup.new_tag('dd'); dd.string = meaning
            dl.append(dt); dl.append(dd)
        sec.append(dl); box.append(sec)
    details.append(box)
    add_effect_badges(soup, box)
    return details


def add_effect_badges(soup, root=None):
    for text in list((root or soup).find_all(string=re.compile(r'\[(?:L|N|H|0)\]'))):
        if text.parent.name in ('script','style','title'):
            continue
        fragments = re.split(r'(\[(?:L|N|H|0)\])', str(text))
        for fragment in fragments:
            if re.fullmatch(r'\[(L|N|H|0)\]', fragment):
                code = fragment[1:-1]
                tag = soup.new_tag('abbr', attrs={'class': ['effect-badge', 'effect-' + code],
                                                'title': EFFECT_LABELS[code],
                                                'aria-label': EFFECT_LABELS[code],
                                                'data-effect': code})
                tag.string = code
                text.insert_before(tag)
            elif fragment:
                text.insert_before(NavigableString(fragment))
        text.extract()


def make_button(soup, text, **attrs):
    button = soup.new_tag('button', attrs={'type': 'button', **attrs})
    button.string = text
    return button


def tag_old_irish(soup):
    """Mark Old Irish word forms lang="sga" so screen readers do not read them as English.

    Only unambiguous places are tagged: paradigm form cells, the big hero word, and the
    italic headword in paradigm headings. Free prose is left alone (it mixes languages).
    """
    targets = soup.select('.form-answer > strong, .form-answer > em, #paradigm .content h3 em')
    hero = soup.select_one('.hero-word')
    if hero and not hero.get_text(strip=True).isdigit() and hero.get_text(strip=True) != 'OI':
        targets.append(hero)
    for tag in targets:
        tag['lang'] = 'sga'


def polish_page(html: str, *, assets_dir: Path | None = None) -> str:
    """Wrap tables without changing their cell count; identify answer cells by meaning."""
    soup = BeautifulSoup(html, 'html.parser')
    if soup.html is None:
        raise ValueError('Expected a complete HTML page')
    if soup.html.get('data-table-revision') == '7':
        return str(soup)
    soup.html['data-table-revision'] = '7'
    assets_dir = assets_dir or Path(__file__).resolve().parents[1] / 'docs'
    is_lesson = soup.select_one('#lesson-data') is not None
    prefix = '../' if is_lesson else ''
    # Version all local assets so a deployment cannot combine old CSS/JS with new HTML.
    for tag, attr in [(t,'href') for t in soup.select('link[rel="stylesheet"]')] + [(t,'src') for t in soup.select('script[src]')]:
        value = tag.get(attr,'').split('?')[0]
        local = assets_dir / Path(value).name
        if local.is_file():
            tag[attr] = value + '?v=' + hashlib.sha256(local.read_bytes()).hexdigest()[:12]
    add_effect_badges(soup)
    paradigm = soup.select_one('#paradigm')
    if paradigm:
        oldbar = paradigm.select_one('.tablebar')
        if oldbar:
            oldbar.decompose()
        content = paradigm.select_one('.content')
        key = next((p for p in content.find_all('p', recursive=False)
                    if p.get_text(' ',strip=True).startswith(('Following-word effects:', 'Mutation of the next word:'))), None)
        if key:
            key.decompose()   # replaced by the reference panel below
        toolbar = soup.new_tag('div', attrs={'class':'recall-toolbar', 'role':'group', 'aria-label':'Paradigm recall controls'})
        toolbar.append(make_button(soup, 'Hide all forms', id='toggle-forms',
                                   **{'class':'btn','aria-pressed':'false','disabled':''}))
        if paradigm.select_one('.effect-badge'):
            toolbar.append(make_button(soup, 'Hide effect clues', id='toggle-effects',
                                       **{'class':'btn','aria-pressed':'false','disabled':''}))
        counter = soup.new_tag('span', attrs={'id':'recall-count','class':'recall-count','aria-live':'polite'})
        counter.string = 'Recall controls load with JavaScript.'
        toolbar.append(counter)
        content.insert_before(toolbar)
        tip = soup.new_tag('p', attrs={'class':'recall-help'})
        tip.string = 'Hide both sg and pl together, or tap any form to practise it alone. Tab + Enter also works.'
        toolbar.insert_after(tip)
        content.insert(0, reference_panel(soup))
    for index, table in enumerate(list(soup.find_all('table')),1):
        if table.find_parent(class_='table-scroll'):
            continue
        rows = table.find_all('tr')
        if not rows:
            raise ValueError('Empty table')
        header_cells = rows[0].find_all(['th','td'], recursive=False)
        headers = [c.get_text(' ',strip=True) for c in header_cells]
        if not all(headers):
            raise ValueError(f'Blank table header: {headers}')
        for row in rows:
            if len(row.find_all(['th','td'],recursive=False)) != len(headers):
                raise ValueError(f'Ragged table under {headers}')
        # Empty spacer columns are rejected, never silently inserted or rendered.
        for column in range(len(headers)):
            values = [r.find_all(['th','td'],recursive=False)[column].get_text(' ',strip=True) for r in rows[1:]]
            if values and all(v in ('', '\u2014', '-') for v in values):
                raise ValueError(f'Uninformative empty column: {headers[column]}')
        in_paradigm = table.find_parent(id='paradigm') is not None
        form_columns = [i for i,h in enumerate(headers) if h.casefold() in FORM_HEADERS] if in_paradigm else []
        title_heading = table.find_previous(['h3','h2'])
        title = title_heading.get_text(' ',strip=True) if title_heading else 'Reference table'
        table_id = f'study-table-{index}'
        table['id'] = table_id
        table['class'] = ['study-table', 'paradigm-table' if in_paradigm else 'reference-table']
        table['data-form-columns'] = ','.join(map(str,form_columns))
        caption = soup.new_tag('caption', attrs={'class':'sr-only'})
        caption.string = title
        table.insert(0,caption)
        for header in header_cells:
            header.name='th'; header['scope']='col'
        if in_paradigm and len(headers)==3 and form_columns==[1,2]:
            table['class'].append('paired-forms')
            group=soup.new_tag('colgroup')
            for cls in ('label-column','form-column','form-column'):
                group.append(soup.new_tag('col',attrs={'class':cls}))
            table.insert(1,group)
        for row_index,row in enumerate(rows[1:],1):
            cells=row.find_all(['td','th'],recursive=False)
            label=cells[0].get_text(' ',strip=True)
            if 0 not in form_columns:
                cells[0].name='th';cells[0]['scope']='row';cells[0]['class']='row-label'
                if label in CASE_HELP: cells[0]['title']=CASE_HELP[label]
            for column in form_columns:
                cell=cells[column]
                cell['class']='form-cell'
                cell['data-form-column']=str(column)
                prompt_label = label if 0 not in form_columns else f'Row {row_index}'
                cell['data-cell-label']=f'{prompt_label} / {headers[column]} / {title}'
                button=make_button(soup,'',**{'class':'recall-cell','data-recall':'',
                    'aria-pressed':'false','title':'Hide this form for recall'})
                answer=soup.new_tag('span',attrs={'class':'form-answer'})
                for child in list(cell.contents): answer.append(child.extract())
                button.append(answer)
                hidden=soup.new_tag('span',attrs={'class':'reveal-prompt','aria-hidden':'true'})
                hidden.string='Reveal'
                button.append(hidden)
                cell.append(button)
        wrapper=soup.new_tag('div',attrs={'class':'table-scroll','role':'region','aria-label':title,
                                        'tabindex':'0'})
        table.wrap(wrapper)
        if in_paradigm and form_columns:
            controls=soup.new_tag('div',attrs={'class':'table-controls'})
            controls.append(make_button(soup,'Hide this table',**{'class':'btn btn-quiet','data-table-toggle':table_id,
                            'aria-controls':table_id,'aria-pressed':'false','disabled':''}))
            wrapper.insert_before(controls)
    tag_old_irish(soup)
    add_gloss(soup)
    return str(soup)

