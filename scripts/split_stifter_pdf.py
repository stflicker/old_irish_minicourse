"""Split your own copy of Stifter, *Sengoidelc* (2006), into small excerpts.

Why: the Google Drive connector returns only the first ~183,000 characters of a
file and refuses downloads over 10 MB, so the whole book cannot be read through
it. Small excerpts (a few lessons each) fit. The excerpts are for YOUR private
Drive only: do not commit them (the repository is public; the book is
copyrighted). `.gitignore` already excludes *.pdf under tools/stifter_excerpts.

Usage:
    python -m pip install pypdf
    python scripts/split_stifter_pdf.py /path/to/Sengoidelc.pdf [output_dir]

The text layer is kept, so the connector can extract the text. Page numbers:
printed page = PDF page - 12 for the scan with 402 PDF pages (check with
--offset if your copy differs).
"""
from __future__ import annotations
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter

# (file name, first printed page, last printed page, what it is for)
PARTS = [
    ("Stifter_S01_L04_mutations",        29,  34, "Lesson 4: initial mutations (L/N/H definitions)"),
    ("Stifter_S02_L06-07_o-stems_article", 41,  53, "Lessons 6-7: o-stems, raising/lowering, syncope, masculine/neuter article"),
    ("Stifter_S03_L08-09_verb_W1",        54,  58, "Lessons 8-9: the verb, W1 class, varia"),
    ("Stifter_S04_L10-11_a-stems_article", 59,  65, "Lessons 10-11: a-stems, ben, feminine article, a-adjectives"),
    ("Stifter_S05_L12-14_W2_poss_io",     66,  76, "Lessons 12-14: W2 verbs, endings prehistory, possessives, poem, io-stems"),
    ("Stifter_S06_L15-17_compound_ia_i",  77,  86, "Lessons 15-17: compound verbs, ia-stems, feminine i-stems"),
    ("Stifter_S07_L18-20_preps_S1_i",     87,  99, "Lessons 18-20: conjugated prepositions, S1 verbs, i-stems"),
    ("Stifter_S08_L21-22_S2_S3_texts",   100, 111, "Lessons 21-22: prepositions 2, S2/S3 verbs and their prehistory, Triads, tests"),
    ("Stifter_S09_L23-24_u_numbers_copula", 112, 121, "Lessons 23-24: u-stems, numerals, copula"),
]
APPENDIX_F_PDF_PAGES = (387, 399)   # Appendix F tables (incl. F.3 article survey, F.6/F.7 verb classes)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("out", type=Path, nargs="?", default=Path("tools/stifter_excerpts"))
    ap.add_argument("--offset", type=int, default=12, help="PDF page = printed page + offset")
    a = ap.parse_args()
    reader = PdfReader(str(a.pdf))
    n = len(reader.pages)
    a.out.mkdir(parents=True, exist_ok=True)
    jobs = [(name, first + a.offset, last + a.offset, note) for name, first, last, note in PARTS]
    jobs.append(("Stifter_S10_AppendixF_tables", *APPENDIX_F_PDF_PAGES, "Appendix F: tables (article survey, verb classes, copula)"))
    for name, first, last, note in jobs:
        if last > n:
            print(f"skip {name}: PDF has only {n} pages")
            continue
        w = PdfWriter()
        for i in range(first - 1, last):
            w.add_page(reader.pages[i])
        target = a.out / f"{name}.pdf"
        with open(target, "wb") as fh:
            w.write(fh)
        print(f"{target}  (PDF pp. {first}-{last}, {last-first+1} pages, {target.stat().st_size/1e6:.1f} MB)  {note}")


if __name__ == "__main__":
    main()
