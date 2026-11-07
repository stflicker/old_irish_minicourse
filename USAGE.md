# Usage and setup (v0.7)

## Daily use

1. Open the site's home page: *Today's study* selects the lesson for the current **Japan date** (or a review day when there is no lesson).
2. Open the lesson, read Stifter's cited section, and complete the two short quiz questions.
3. Solve both questions. Answers are kept in **that browser** (localStorage) only.
4. Fill in minutes, difficulty and an optional note, then click **Submit completion via GitHub Issue**. Press **Submit new issue** on the GitHub page that opens: the feedback workflow records the row in `PROGRESS.md`. Opening the form alone does not count.

`published` means an HTML lesson was made available, **not** that you studied it. Missed lessons stay incomplete until you report them.

## Hosting and automation (already set up)

The site is served by **GitHub Pages** (Settings → Pages → Source: *GitHub Actions*) and everything runs from `.github/workflows/daily-publish.yml`:

- **Daily at 02:17 JST** (and on manual *Run workflow*, and on pushes that touch lessons, scripts or site assets) it records `published` / `awaiting_content` in `PROGRESS.md`, rebuilds `docs/` and deploys it. GitHub may delay scheduled runs.
- **When you open a feedback Issue** titled `[Old Irish Feedback] OI-D###` (owner only) it imports the row into `PROGRESS.md`, then rebuilds.
- Workflow permissions must allow *Read and write* (Settings → Actions → General) so the workflow can commit `PROGRESS.md`.

The workflow does **not** write lessons. A new day needs `lessons/OI-D###.md` committed first; we deliberately avoid publishing AI-invented declensional forms just to fill a schedule.

**When there is no lesson for a day** (including every day after Day 028), the home page's *Today's study* card switches to **Review**: it picks one earlier authored lesson at random, fixed for that Japan date so a refresh does not change it, and *Another review day* picks a different one. `python scripts/daily_publish.py --today YYYY-MM-DD` prints the same pick for that date. Review days add no row to `PROGRESS.md`.

**Privacy:** the repository is public, so `PROGRESS.md` and any note you type into a feedback Issue are visible. Keep notes minimal.

## Running locally

You can open [docs/index.html](docs/index.html) or any `docs/days/###.html` directly in a desktop browser; the quiz works without a server (some phone file viewers block JavaScript).

## Technical maintenance

- Edit `FIRST_28_DAYS.md` only if we explicitly agree to change the syllabus. The current first 28 topics are fixed.
- Add verified content using `LESSON_TEMPLATE.md` as `lessons/OI-D002.md`, etc.
- Build locally: `python -m pip install -r scripts/requirements.txt` followed by `python scripts/build_site.py`.
- Test a date without affecting the real record: use a throwaway copy of the repository, then `python scripts/daily_publish.py --today 2026-10-10`.
- After Day 028, extend `FIRST_28_DAYS.md` and add lesson files before expecting further HTML pages; until then the home page shows review days. `CURRICULUM.md` is a unit map, not a numbered daily sequence.
- To add completion by hand (missed Issue): `python scripts/update_completion.py OI-D001 --minutes 12 --difficulty 2 --note 'Done'`, then commit `PROGRESS.md`.
