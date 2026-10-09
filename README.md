# Sengoídelc — daily Old Irish (v0.4)

**Book:** David Stifter, *Sengoídelc: Old Irish for Beginners* (2006)  
**First scheduled lesson:** 10 October 2026, Japan time  
**Daily workload:** about 10–15 minutes

A small Markdown-led course with an interactive static HTML reader, an automatic **daily publication log**, and an optional ChatGPT notification. The learner has already studied the alphabet, phonology, orthography, mutations, and basic morphological terminology; the course begins at §6.4, with paradigms.

## Start here

- [**Try the HTML interface**](docs/index.html) → select Day 001.
- [Usage and setup](USAGE.md) → how to publish the site and enable the daily workflow.
- [The locked first 28 days](FIRST_28_DAYS.md) → the canonical topic order (copied *unchanged* from v0.2).
- [Progress](PROGRESS.md) → one row per scheduled day once the daily job runs.

## How the files relate

| File | Purpose |
|---|---|
| `FIRST_28_DAYS.md` | **The source of truth** for what Day N teaches |
| `CURRICULUM.md` | Overall textbook progression after these days |
| `lessons/OI-D###.md` | Actual authored content and questions for that day |
| `docs/days/###.html` | Built interactive page, generated from lesson Markdown |
| `PROGRESS.md` | Automatically receives the daily publication/awaiting-content row |
| `scripts/daily_publish.py` | Determines due day in Japan; updates the record |
| `scripts/build_site.py` | Builds all 28 pages from the Markdown |
| `.github/workflows/daily-publish.yml` | Runs the publication record and site build daily on GitHub |
| `PROTOCOL.md` | Authoring, quality, progression, and record rules |

## Important limits

- **Only Day 001 is fully authored and interactive today.** The 27 other days have honest curriculum-target pages, not invented grammar lessons.
- After GitHub repository creation, Pages Actions configuration, and a successful test run, `PROGRESS.md` **will gain a daily row**, either `published` or `awaiting_content`.
- To deliver a new substantive HTML lesson each day, a lesson Markdown file must first be written and committed. The ChatGPT daily task can be instructed to do that via a **connected GitHub account**, subject to available app actions/approval. The GitHub connection exists, but writing to a course repository from a scheduled task has not yet been tested.
- Buttons save learning results in the current browser. They cannot update `PROGRESS.md` in GitHub directly without another authenticated writing pathway. Learner completion is recorded only after a reply or explicit transfer.
- A ChatGPT scheduled task created in a Project does **not** have access to Project-uploaded files. Hosting the canonical syllabus in GitHub, and instructing the task to read that repository, avoids relying on Project attachments being available during a scheduled run.

There is **no paid API key** in this package and **no continuously running server**. GitHub Pages serves the static site; GitHub Actions performs the once-daily file update.