"""Append self-reported completion to PROGRESS.md without publishing private details by accident.

Example:
  python scripts/update_completion.py OI-D001 --minutes 12 --difficulty 2 --note 'Genitive understood'
Use ONLY after the learner reports completion.
"""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
from course import read_curriculum, today_jst
from daily_publish import update


def main():
    p=argparse.ArgumentParser()
    p.add_argument('id', help='OI-D001 ... OI-D028')
    p.add_argument('--minutes',type=int,required=True)
    p.add_argument('--difficulty',type=int,required=True)
    p.add_argument('--note', default='—')
    p.add_argument('--status',choices=['completed','in_progress','needs_revisit','skipped'],default='completed')
    p.add_argument('--on', help='YYYY-MM-DD JST; defaults to today')
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    a=p.parse_args()
    valid={e.lesson_id for e in read_curriculum(a.root/'FIRST_28_DAYS.md')}
    if a.id not in valid: p.error(f'Unexpected lesson id: {a.id}')
    if not 1<=a.minutes<=180: p.error('minutes must be 1..180')
    if not 1<=a.difficulty<=5: p.error('difficulty must be 1..5')
    if '\\|' in a.note or '|' in a.note: p.error('Do not use | in notes')
    date_str=a.on or today_jst().isoformat()
    progress=a.root/'PROGRESS.md'
    lines=progress.read_text(encoding='utf-8').splitlines()
    new='| ' + ' | '.join([a.id,date_str,a.status,str(a.minutes),str(a.difficulty),a.note.strip().replace('\n',' ') or '—']) + ' |'
    found=False
    for i,line in enumerate(lines):
        if line.startswith('| '+a.id+' |'):
            lines[i]=new;found=True;break
    if not found: lines.append(new)
    progress.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    print(f'Updated {a.id}: {a.status}')

if __name__=='__main__':main()