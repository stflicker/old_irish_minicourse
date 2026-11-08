# Sengoídelc — daily Old Irish (v0.7)

**Book:** David Stifter, *Sengoídelc: Old Irish for Beginners* (2006)  
**First scheduled lesson:** 10 October 2026, Japan time  
**Daily workload:** about 10–15 minutes

A small Markdown-led course with an interactive static HTML reader, an automatic **daily publication log**. The learner has already studied the alphabet, phonology, orthography, mutations, and basic morphological terminology; the course begins at §6.4, with paradigms.

## Start here

- [**Try the HTML interface**](docs/index.html) → select Day 001.
- [Usage and setup](USAGE.md) → how to publish the site and enable the daily workflow.
- [The locked first 28 days](FIRST_28_DAYS.md) → the canonical topic order (copied *unchanged* from v0.2).
- [Progress](PROGRESS.md) → one row per scheduled day: `published` = page exists; `completed` = you submitted the feedback Issue.
- [Changelog](CHANGELOG.md) → what changed in each version.

## Historical morphology track (added v0.5)

Every daily lesson now offers an **expanded, open-by-default historical morphology section**: PIE reconstructed forms and functions; their Proto-Celtic/early Irish development; Old Irish inflection; and the distinction between regular sound change, inherited categories, analogical innovations and debated hypotheses. The core practical lesson stays around 10–15 minutes; the historical section adds about 5–8 optional minutes. [Comparative morphology guide](HISTORICAL_MORPHOLOGY.md).

## How the files relate

| File | Purpose |
|---|---|
| `FIRST_28_DAYS.md` | **The source of truth** for what Day N teaches |
| `CURRICULUM.md` | Overall textbook progression after these days |
| `lessons/OI-D###.md` | Actual authored content and questions for that day |
| `docs/days/###.html` | Built interactive page, generated from lesson Markdown |
| `HISTORICAL_MORPHOLOGY.md` | Comparative background, evidence standards and sources |
| `docs/history.html` | Published historical morphology guide |
| `PROGRESS.md` | Automatically receives the daily publication/awaiting-content row |
| `scripts/daily_publish.py` | Determines due day in Japan; updates the record |
| `scripts/build_site.py` | Builds all 28 pages from the Markdown |
| `.github/workflows/daily-publish.yml` | Runs the publication record and site build daily on GitHub |
| `PROTOCOL.md` | Authoring, quality, progression, and record rules |
| `CONTENT_DESIGN_HANDOFF.md` | How lessons are designed, sourced and verified (for content sessions) |
| `REVIEW_FIRST_28_DAYS.md`, `REVIEW_CONTENT_QUALITY.md`, `NEXT_28_DAYS_DRAFT.md` | Audit of Days 1–28 and the Days 29–56 outline |

## Important limits

- **All Days 001–028 have authored interactive Markdown lessons and generated HTML pages.** The historical morphology track has been expanded in each lesson. Structural build checks do not replace manual philological review; examples and reconstructions are cited and must be interpreted with their stated evidentiary limits.
- `PROGRESS.md` gains one row per scheduled day, either `published` or `awaiting_content` (written by the daily workflow); a row becomes `completed` only after you submit the feedback Issue.
- A new lesson needs a Markdown file in `lessons/` first (see `LESSON_TEMPLATE.md` and `PROTOCOL.md`). The workflow never invents grammar to fill a day.
- **After the last authored day (or on any day with no lesson), the home page offers a review of a randomly chosen earlier lesson**, stable for that Japan date, with an *Another review day* button. `daily_publish.py` prints the same pick; review days add no `PROGRESS.md` row.
- Quiz answers are kept in the browser only. Completion, minutes, difficulty and notes are recorded only when you submit the GitHub feedback Issue; the feedback workflow processes it.

There is **no paid API key** in this package and **no continuously running server**. GitHub Pages serves the static site; GitHub Actions performs the once-daily file update.