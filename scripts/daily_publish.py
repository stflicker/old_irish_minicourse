"""Add or update the one planned daily record row. Idempotent.

This logs RELEASE, NOT learner completion. A pending lesson is marked
'awaiting_content' rather than being falsely labelled published.
"""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
import sys

from course import entry_for_date, read_curriculum, today_jst

COLUMNS = '| Lesson | Date (JST) | Status | Minutes | Difficulty / 5 | Note |\n|---|---|---|---:|---:|---|'


def update(progress: Path, curriculum: Path, lessons: Path, now: date) -> tuple[str, bool]:
    entries = read_curriculum(curriculum)
    e = entry_for_date(entries, now)
    if not e:
        return 'Not in 001..028: no row added; extend syllabus before scheduling further.', False

    exists = (lessons / f'{e.lesson_id}.md').is_file()
    new_status = 'published' if exists else 'awaiting_content'
    lines = progress.read_text(encoding='utf-8').splitlines() if progress.exists() else [
        '# Progress', '',
        'One row per scheduled date. `published` is NOT the same as `completed`.', '',
        COLUMNS.split('\n')[0], COLUMNS.split('\n')[1]
    ]
    rendered=[]; replaced=False; changed=False
    for line in lines:
        if line.startswith('| ' + e.lesson_id + ' |'):
            replaced=True
            fields=[p.strip() for p in line.strip().strip('|').split('|')]
            if len(fields) != 6:
                raise ValueError('Malformed progress record line: '+line)
            # Never downgrade self-reported progress.
            if fields[2] in ('completed','needs_revisit','in_progress','skipped'):
                rendered.append(line)
                continue
            newline='| ' + ' | '.join([e.lesson_id,now.isoformat(),new_status, fields[3],fields[4],fields[5]]) + ' |'
            rendered.append(newline)
            changed |= line != newline
        else:
            rendered.append(line)
    if not replaced:
        rendered.append('| ' + ' | '.join([e.lesson_id,now.isoformat(),new_status,'—','—','—']) + ' |')
        changed=True
    if changed:
        progress.write_text('\n'.join(rendered).rstrip()+'\n',encoding='utf-8')
    return f'{e.lesson_id}: {new_status} ({now.isoformat()} JST)', changed


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--today', help='Override current Japan date, YYYY-MM-DD; useful for tests')
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    a=p.parse_args()
    when=date.fromisoformat(a.today) if a.today else today_jst()
    msg,changed=update(a.root/'PROGRESS.md',a.root/'FIRST_28_DAYS.md',a.root/'lessons',when)
    print(msg+ ('; updated PROGRESS.md' if changed else '; no file changes'))

if __name__=='__main__':
    main()