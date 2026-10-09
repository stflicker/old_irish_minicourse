"""Build a static interactive HTML reader from Markdown files.

Canonical 28-day order is parsed directly from FIRST_28_DAYS.md.
Each complete lesson is an editable Markdown file with small YAML quiz metadata.
Unwritten days are visibly marked as awaiting content, never made-up lessons.
"""
from __future__ import annotations
from datetime import date
from html import escape
from pathlib import Path
import json
import re
import sys

import mistune
import yaml
from course import Entry, read_curriculum, START_JST

ROOT=Path(__file__).resolve().parents[1]
PAGES=ROOT/'docs'/'days'
MARKDOWN=mistune.create_markdown(plugins=['table','strikethrough'])


def e(v): return escape(str(v),quote=True)


def load_lesson(path:Path, entry:Entry):
    if not path.is_file():return None
    raw=path.read_text(encoding='utf-8')
    match=re.match(r'\A---\n(.*?)\n---\n(.*)\Z',raw,re.S)
    if not match:raise ValueError(f'{path.name}: YAML frontmatter is required')
    info=yaml.safe_load(match.group(1))
    if info['id']!=entry.lesson_id:raise ValueError(f'{path.name}: id must equal curriculum day')
    if not re.search(r'\b'+re.escape(entry.book.split(',')[0].split('-')[0].split(';')[0])+r'\b',info['stifter']):
        # Book references with ranges or special anchors are accepted, but warn.
        print(f'WARNING: section may not match for {path.name}',file=sys.stderr)
    if not info.get('questions'):raise ValueError(f'{path.name}: at least 1 question required')
    if len(info['questions'])>3: raise ValueError(f'{path.name}: keep 1 to 3 micro-questions')
    for q in info['questions']:
        if not (2<=len(q['options'])<=5):raise ValueError(f'{path.name}: 2 to 5 answer options')
        if not (0<=int(q['correct'])<len(q['options'])):raise ValueError(f'{path.name}: bad correct index')
    sections={}
    chunks=re.split(r'(?m)^## ([^\n]+)\n',match.group(2))
    for i in range(1,len(chunks)-1,2):sections[chunks[i].strip()]=MARKDOWN(chunks[i+1])
    info['sections']=sections
    return info


def shell(title,body,day: int|None=None):
    suffix=f' · Day {day:03d}' if day else ''
    day_label=f'DAY {day:03d} / 028' if day else 'CURRICULUM · 28 DAYS'
    css='../style.css' if day else 'style.css'
    home='../index.html' if day else 'index.html'
    return f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light"><meta name="theme-color" content="#153d33">
<title>{e(title)}{suffix} · Sengoídelc</title><link rel="stylesheet" href="{css}">
</head><body><header class="topbar"><span class="brand"><a href="{home}">SENGOÍDELC · OLD IRISH</a></span>
<span class="minor">{day_label}</span></header><main><noscript>JavaScript is disabled. The text and paradigm are available, but quizzes and local saving require a normal browser.</noscript>
{body}</main></body></html>'''


def lesson_link(idx):return f'{idx:03d}.html'


def navigation(entry):
    prev=f'<a href="{lesson_link(entry.day-1)}">← Day {entry.day-1:03d}</a>' if entry.day>1 else '<span>First day</span>'
    nxt=f'<a href="{lesson_link(entry.day+1)}">Day {entry.day+1:03d} →</a>' if entry.day<28 else '<span>End of 28-day block</span>'
    return f'<nav class="day-nav">{prev}<a href="../index.html">All 28 days</a>{nxt}</nav>'


def panel(label,title,body,pid,extra=''):
    return f'<article class="panel {extra}" id="{pid}"><div class="panelhead"><span class="index">{e(label)}</span></div><h2>{e(title)}</h2>{body}</article>'


def render_lesson(entry:Entry, data):
    available=data is not None
    if not available:
        focus=entry.target
        body=f'''<section class="hero"><div><div class="kicker">DAY {entry.day:03d} · STIFTER §{e(entry.book)}</div>
<h1>Lesson not yet published</h1><p class="lead">{e(focus)}</p><div class="meta"><span class="pill">{e(entry.date_jst)}</span><span class="pill">Content pending</span></div></div><div class="hero-word" aria-hidden="true">{entry.day:03d}</div></section>
{panel('CURRICULUM TARGET','Scheduled focus',f'<p>{e(focus)}</p><p class="small">This topic comes from FIRST_28_DAYS.md. The actual grammar, paradigm, and interactive questions have not been authored or verified yet. No completed lesson is being claimed.</p>','missing')}
{navigation(entry)}<footer class="foot">The daily ChatGPT push still provides a text lesson if the HTML file has not yet been published.</footer>'''
        return shell(f'Day {entry.day:03d} — pending',body,entry.day)
    title=data['title']; subtitle=data['subtitle']; word=data.get('word','')
    sect=data['sections']
    main_section=sect.get('Paradigm') or sect.get('Text') or sect.get('Forms') or '<p>See the cited Stifter section.</p>'
    point=sect.get('One point','')
    comparison=sect.get('Comparison (optional)',sect.get('Comparison',''))
    q_html=[]
    for i,q in enumerate(data['questions']):
        buttons=''.join(f'<button type="button" class="option" data-option="{j}" data-question="{i}">{e(option)}</button>' for j,option in enumerate(q['options']))
        q_html.append(f'<div class="question"><h3>{i+1}. {e(q["prompt"])}</h3><div class="options">{buttons}</div><p class="feedback" id="feedback-{i}" aria-live="polite"></p></div>')
    score=f'<div class="score"><div class="bar" id="scorebar" role="progressbar" aria-valuemin="0" aria-valuemax="{len(data["questions"])}" aria-valuenow="0" aria-label="Correct quiz answers"><div id="fill"></div></div><span id="score">0 / {len(data["questions"])} correct</span></div>'
    practice=score+''.join(q_html)
    practice+='<details><summary>Hints (open only if needed)</summary><div class="inside"><ol>' + ''.join('<li>'+e(q.get('hint','Try reading the table once more.'))+'</li>' for q in data['questions']) + '</ol></div></details>'
    practice+='<details><summary>Manual answer key (if the buttons are blocked)</summary><div class="inside"><ol>' + ''.join('<li>'+e(q['options'][int(q['correct'])])+'</li>' for q in data['questions']) + '</ol></div></details>'
    record='''<div class="form-row"><label for="minutes">Time (min)</label><input id="minutes" type="number" min="1" max="180" placeholder="e.g. 12" inputmode="numeric"></div>
<div class="form-row"><label for="difficulty">Difficulty</label><select id="difficulty"><option value="">Not rated</option><option value="1">1/5 · Easy</option><option value="2">2/5</option><option value="3">3/5</option><option value="4">4/5</option><option value="5">5/5 · Hard</option></select></div>
<div class="form-row"><label for="note">Note</label><input id="note" type="text" maxlength="120" placeholder="Optional"></div>
<div class="buttons"><button class="btn btn-main" id="mark-complete" disabled>Mark complete</button><button class="btn" id="copy-record" disabled>Copy record</button><button class="btn" id="download-record" disabled>Download PROGRESS.md</button></div>
<div class="buttons"><button class="btn" id="reset-practice">Reset practice</button></div>
<p id="status" class="status" aria-live="polite">Answer all questions to unlock completion.</p>
<div class="manual" id="manual-box" hidden><label for="manual-text">Select and copy the record:</label><textarea id="manual-text" readonly></textarea></div>
<p class="note">Saved only in this browser. Export the Markdown record or report completion in ChatGPT. This does not directly write back to the hosted GitHub file.</p>'''
    compare_panel=panel('04 / COMPARISON','Historical note',f'<details><summary>Show comparison</summary><div class="inside content">{comparison}</div></details>','comparison','historical') if comparison else ''
    body=f'''<section class="hero" aria-labelledby="title"><div>
<div class="kicker">{e(data['category'])} · STIFTER §{e(data['stifter'])}</div>
<h1 id="title">{e(title)}</h1><p class="lead">{e(subtitle)}</p>
<div class="meta"><span class="pill">{e(data.get('minutes',12))} minutes</span><span class="pill">{len(data['questions'])} questions</span><span class="pill">Scheduled {entry.date_jst}</span></div>
</div><div class="hero-word" aria-hidden="true">{e(word)}</div></section>
<div class="layout"><div>
{panel('01 / FORMS','Paradigm or text','<div class="tablebar"><button class="btn" id="toggle-forms" type="button" aria-pressed="false">Hide forms for recall</button></div><div class="content">'+main_section+'</div>','paradigm')}
{panel('02 / FOCUS','One point','<div class="callout content">'+point+'</div>','notice')}
{compare_panel}
</div><div>
{panel('03 / PRACTICE','Check yourself',practice,'practice')}
{panel('05 / RECORD','Save this session',record,'record')}
</div></div>{navigation(entry)}
<footer class="foot">Textbook reference: Stifter (2006), §{e(data['stifter'])}. The content of this Markdown lesson is separately authored and should not be mistaken for a quotation from the book.</footer>
<script id="lesson-data" type="application/json">{json.dumps({'id':entry.lesson_id,'questions':data['questions']},ensure_ascii=False).replace('</','<\\/')}</script>
<script src="../app.js" defer></script>'''
    return shell(title,body,entry.day)


def render_index(entries, available):
    trs=[]
    for x in entries:
        status='Ready' if x.day in available else 'Not authored'
        flag='badge-due' if x.day in available else 'badge-wait'
        target=MARKDOWN(x.target)
        trs.append(f'<tr data-day="{x.day}"><td><a href="days/{x.day:03d}.html">{x.day:03d}</a></td><td>{e(x.date_jst)}</td><td>§{e(x.book)}</td><td>{target}</td><td class="{flag}">{status}</td></tr>')
    body='''<section class="hero"><div><div class="kicker">CURRICULUM · FIRST 28 DAYS</div><h1>Old Irish, a little every day</h1>
<p class="lead">Paradigms, short exercises, and occasional Celtic/Indo-European comparisons.</p>
<div class="meta"><span class="pill">Stifter (2006)</span><span class="pill">10–15 minutes/day</span><span class="pill">Daily from 10 Oct 2026</span></div></div>
<div class="hero-word" aria-hidden="true">OI</div></section>
<section class="panel"><div class="panelhead"><span class="index">TODAY'S STUDY</span><span id="today-label" class="minute">Asia/Tokyo</span></div>
<h2 id="today-heading">Find today's lesson</h2><p id="today-explainer" class="aside">The date in Japan selects the next scheduled topic, not your completion state.</p>
<div class="buttons"><a class="btn btn-main" id="today-link" href="days/001.html" style="text-decoration:none">Open scheduled day</a><a class="btn" href="days/001.html" style="text-decoration:none">Try Day 001 demo</a></div>
</section>
<section class="panel index-list"><div class="panelhead"><span class="index">CURRICULUM FROM FIRST_28_DAYS.MD</span></div><h2>Lessons</h2>
<table class="plan-table"><thead><tr><th>Day</th><th>Japan date</th><th>Stifter</th><th>Focus</th><th>Content</th></tr></thead><tbody>'''+''.join(trs)+'''</tbody></table><p class="legend">The topic list is built from <code>FIRST_28_DAYS.md</code>. 'Not authored' means the interactive grammar lesson has not been verified and published yet.</p></section>
<footer class="foot"><p>Each completed lesson stores a session record in your browser, exportable as Markdown. The website itself has no access to your private ChatGPT messages or local files.</p></footer>
<script>const start=Date.UTC(2026,9,10);let s=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Tokyo',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());let p=s.match(/(\\d{4})-(\\d{2})-(\\d{2})/);if(!p){let a=new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Tokyo',year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(new Date());let ob=Object.fromEntries(a.map(v=>[v.type,v.value]));p=[0,ob.year,ob.month,ob.day]};let idx=Math.floor((Date.UTC(+p[1],+p[2]-1,+p[3])-start)/864e5)+1;if(idx<1)idx=1;if(idx>28)idx=28;document.getElementById('today-heading').textContent='Day '+String(idx).padStart(3,'0');document.getElementById('today-link').href='days/'+String(idx).padStart(3,'0')+'.html';document.querySelector('tr[data-day="'+idx+'"]').classList.add('today-row');document.getElementById('today-label').textContent=s+' JST';</script>'''
    return shell('Daily Old Irish',body)


def main():
    entries=read_curriculum(ROOT/'FIRST_28_DAYS.md')
    PAGES.mkdir(parents=True,exist_ok=True)
    ready=set()
    for ent in entries:
        content=load_lesson(ROOT/'lessons'/f'{ent.lesson_id}.md',ent)
        if content:ready.add(ent.day)
        (PAGES/lesson_link(ent.day)).write_text(render_lesson(ent,content),encoding='utf-8')
    (ROOT/'docs'/'index.html').write_text(render_index(entries,ready),encoding='utf-8')
    print(f'Built {len(entries)} scheduled pages, {len(ready)} with authored interactive lessons')

if __name__=='__main__':main()