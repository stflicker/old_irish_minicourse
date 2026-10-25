"""Regression checks for every generated lesson and the v0.7 source migration."""
from pathlib import Path
import json
import unittest
from bs4 import BeautifulSoup
from paradigms_v07 import SECTIONS
from revise_paradigms import revise_lesson
from table_tools import polish_page

ROOT=Path(__file__).resolve().parents[1]


class CourseTables(unittest.TestCase):
    def test_all_twenty_eight_pages(self):
        for day in range(1,29):
            with self.subTest(day=day):
                path=ROOT/'docs'/'days'/f'{day:03d}.html'
                soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
                self.assertEqual(soup.html.get('data-table-revision'),'7')
                data=json.loads(soup.select_one('#lesson-data').string)
                self.assertEqual(data['id'],f'OI-D{day:03d}')
                self.assertIn(len(data['questions']),(1,2))
                self.assertNotIn('Lesson not yet published',soup.get_text())
                self.assertTrue(soup.select('#paradigm [data-recall]'))
                self.assertEqual(len(soup.select('#toggle-forms')),1)
                self.assertEqual(len(soup.select('#submit-feedback')),1)
                self.assertFalse(soup.select('#mark-complete,#copy-record,#download-record'))
                ids=[x['id'] for x in soup.select('[id]')]
                self.assertEqual(len(ids),len(set(ids)))
                for table in soup.select('table'):
                    rows=table.select('tr')
                    header=rows[0].find_all(['th','td'],recursive=False)
                    self.assertTrue(all(h.get_text(strip=True) for h in header))
                    for row in rows:
                        self.assertEqual(len(row.find_all(['th','td'],recursive=False)),len(header))
                    for col in range(len(header)):
                        values=[r.find_all(['td','th'],recursive=False)[col].get_text(strip=True) for r in rows[1:]]
                        self.assertFalse(values and all(v in ('','-','—') for v in values))
                    self.assertTrue(table.caption)
                    for th in header: self.assertEqual(th.get('scope'),'col')
                    if table.find_parent(id='paradigm'):
                        headings=[c.get_text(' ',strip=True) for c in header]
                        for col,h in enumerate(headings):
                            if 'form + effect' in h or 'article + effect' in h:
                                for row in rows[1:]:
                                    self.assertTrue(row.find_all(['td','th'],recursive=False)[col].select('.effect-badge'),(day,h))
                for cell in soup.select('#paradigm .form-cell'):
                    self.assertEqual(len(cell.select('[data-recall]')),1)
                for asset in soup.select('link[rel="stylesheet"],script[src]'):
                    value=asset.get('href',asset.get('src',''))
                    if not value.startswith('http'): self.assertIn('?v=',value)

    def test_day_three_has_both_number_effects(self):
        soup=BeautifulSoup((ROOT/'docs/days/003.html').read_text(),'html.parser')
        table=soup.select_one('#paradigm table')
        self.assertEqual(len(table.select('thead th')),3)
        self.assertEqual(len(table.select('[data-recall]')),10)
        self.assertEqual([a['data-effect'] for a in table.select('.effect-badge')],
                         ['0','L','L','N','L','0','N','H','L','H'])

    def test_migration_preserves_metadata_and_history(self):
        for day in range(1,29):
            before=f'---\nid: OI-D{day:03d}\nquestions: []\n---\n## Paradigm\nOld\n\n## One point\nKeep exactly.\n\n## Comparison (optional)\nHistorical text.\n'
            once=revise_lesson(before,day)
            self.assertEqual(revise_lesson(once,day),once)
            self.assertTrue(once.endswith('## One point\nKeep exactly.\n\n## Comparison (optional)\nHistorical text.\n'))
            self.assertIn(SECTIONS[day].strip(),once)

    def test_renderer_idempotence(self):
        path=ROOT/'docs/days/003.html'
        once=polish_page(path.read_text())
        self.assertEqual(polish_page(once),once)


if __name__=='__main__': unittest.main()
