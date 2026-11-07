# Changelog

Version numbers refer to the whole course package (content, site and scripts). `FIRST_28_DAYS.md` keeps its own schema version (0.2.0) because its topic table is locked.

## v0.7
- Dark theme (follows the system setting); `color-scheme: light dark`.
- Quiz: options are shuffled on each visit; wrong options are struck out and show the question's hint, then point back to the forms table after a second miss.
- Home page: each lesson shows `✓ recorded` (from `PROGRESS.md`, any device) or `quiz done here` (this browser), plus a summary line; review day when no lesson is scheduled.
- Single stylesheet (`tables.css` merged into `style.css`); Old Irish forms carry `lang="sga"`.
- Semantic paradigm tables with per-cell hide/reveal recall, effect badges and `tables.css`; `revise_paradigms.py` and `test_tables.py` validation.
- Historical-comparative content standard added to `PROTOCOL.md`.
- Completion is recorded only by an owner-submitted GitHub feedback Issue (replaces copy/export of a local record).

## v0.6
- Clearer paradigm presentation and distinct explanation layers.

## v0.5
- Historical morphology track in every lesson; `HISTORICAL_MORPHOLOGY.md` and `docs/history.html`.

## v0.4 and earlier
- Markdown-led lessons, static HTML reader, daily publication log (`PROGRESS.md`), GitHub Pages workflow.
