"""One-time, idempotent v0.7 source migration; never changes learner records.

After this migration the Markdown, not this script, remains authoritative.
A paradigm_revision: 7 marker protects subsequent hand edits from replacement.
"""
from pathlib import Path
import hashlib
import re
from paradigms_v07 import SECTIONS

ROOT = Path(__file__).resolve().parents[1]


def revise_lesson(raw: str, day: int) -> str:
    match = re.match(r'\A---\n(.*?)\n---\n(.*)\Z', raw, re.S)
    if not match:
        raise ValueError(f'Day {day}: missing YAML frontmatter')
    metadata, body = match.groups()
    if re.search(r'(?m)^paradigm_revision:\s*7\s*$', metadata):
        return raw
    pattern = r'(?m)^## (?:Paradigm|Forms|Text)\n[\s\S]*?(?=^## |\Z)'
    replacement = '## Paradigm\n\n' + SECTIONS[day].strip() + '\n\n'
    revised, count = re.subn(pattern, lambda _: replacement, body, count=1)
    if count != 1:
        raise ValueError(f'Day {day}: could not find one main forms section')
    # Correct an imprecise gloss left by the earlier prose-only revision.
    revised = revised.replace('nominate a single man as *fer*, more than one as *fir*',
                              'use *fer* for a singular subject and *fir* for a plural subject')
    metadata = re.sub(r'(?m)^paradigm_revision:.*\n?', '', metadata).rstrip()
    return '---\n' + metadata + '\nparadigm_revision: 7\n---\n' + revised


def install_renderer(path: Path) -> None:
    """Patch the existing builder once, retaining its lesson/quiz/index logic."""
    raw = path.read_text(encoding='utf-8')
    if 'from table_tools import polish_page' in raw:
        return
    anchor = 'from course import Entry, read_curriculum, START_JST'
    if anchor not in raw:
        raise ValueError('Builder import changed; reconcile before applying migration')
    raw = raw.replace(anchor, anchor + '\nfrom table_tools import polish_page')
    # Every generated page passes through this wrapper, including the index/guide.
    marker = '\n\ndef lesson_link(idx):'
    if marker not in raw:
        raise ValueError('Builder shell boundary changed; refusing a blind patch')
    wrapper = '''\n\n_plain_shell = shell

def shell(title, body, day=None):
    return polish_page(_plain_shell(title, body, day))
'''
    raw = raw.replace(marker, wrapper + marker, 1)
    path.write_text(raw, encoding='utf-8')


def main():
    protected = {p: hashlib.sha256(p.read_bytes()).digest()
                 for p in (ROOT/'FIRST_28_DAYS.md', ROOT/'PROGRESS.md') if p.exists()}
    changed = 0
    for day in range(1, 29):
        path = ROOT / 'lessons' / f'OI-D{day:03d}.md'
        before = path.read_text(encoding='utf-8')
        after = revise_lesson(before, day)
        if after != before:
            path.write_text(after, encoding='utf-8')
            changed += 1
    install_renderer(ROOT/'scripts'/'build_site.py')
    for path, digest in protected.items():
        assert hashlib.sha256(path.read_bytes()).digest() == digest, f'Protected file changed: {path}'
    print(f'Paradigm revision 7: updated {changed} lessons; curriculum and progress unchanged.')


if __name__ == '__main__':
    main()
