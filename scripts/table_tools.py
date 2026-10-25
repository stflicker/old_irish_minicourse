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
 'Nominative': 'Typically the subject or a predicate noun',
 'Genitive': 'Typically a dependent noun: of ...',
 'Prepositional': 'The case also called dative; governed by appropriate prepositions',
 'Accusative': 'Typically the direct object; also governed by some prepositions',
 'Vocative': 'Direct address; the particle a has its own incoming lenition',
}
FORM_HEADERS = {
 'form','phrase','example phrase','element / form','absolute form',
 'conjunct form after n\u00ed','singular form','plural form',
 'singular form + effect','plural form + effect',
 'singular article + effect','plural article + effect',
 'singular fused form + effect','plural fused form + effect','possessive form + effect',
}


def add_effect_badges(soup):
    for text in list(soup.find_all(string=re.compile(r'\[(?:L|N|H|0)\]'))):
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
    if not soup.find('link', attrs={'data-table-styles': True}):
        link = soup.new_tag('link', rel='stylesheet', href=prefix+'tables.css')
        link['data-table-styles'] = '7'
        soup.head.append(link)
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
                    if p.get_text(' ',strip=True).startswith('Following-word effects:')), None)
        if key:
            details = soup.new_tag('details', attrs={'class':'effect-key'})
            summary = soup.new_tag('summary')
            summary.string = 'L / N / H / 0 - how to read the following-word markers'
            details.append(summary)
            key.replace_with(details)
            details.append(key)
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
        tip.string = 'Hide both singular and plural together, or tap any form to practise one cell. Tab + Enter also works.'
        toolbar.insert_after(tip)
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
    return str(soup)
