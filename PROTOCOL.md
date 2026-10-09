# Daily Old Irish teaching and publication protocol (v0.4)

## Learner and pace

- Primary book: David Stifter, *Sengoídelc* (2006).
- No introductory phonetics, spelling, mutation, or morphological-terminology sessions. The learner knows Latin, Ancient Greek and Sanskrit.
- **One active focus**, sometimes with a short second historical-comparative track, per day; ~10–15 minutes.
- Plain, lively wording. No elaborate motivational language or long preambles.
- Every active grammar lesson: small paradigm or excerpt, one pointed explanation, one or two interactive questions, optional expandable comparison, and a compact progress record.

## Source authority

1. `FIRST_28_DAYS.md` defines the first 28 days' **order and topic**. Keep the present table unchanged without explicit learner approval.
2. `CURRICULUM.md` governs longer-term prerequisites and future expansion.
3. `lessons/OI-D###.md` holds the **authored scholarly content**, with citations and quiz answers. A lesson is never conjured merely from its topic label in the curriculum.
4. Each new lesson must identify the Stifter section; use Thurneysen and reliable academic editions for cross-checking, plus eDIL for historical lexicon, Matasović/McCone for comparative Celtic/PIE. Mark reconstruction with `*` and distinguish book paradigm from attested text.
5. Do not reproduce long copyrighted textbook passages; cite sections and use original short exercises or legitimate small excerpts with proper source attribution.

## Daily task, file publishing, record

- Calendar: Day 001 = **2026-10-10 JST**. Day N is calendar day N of the opening 28-day sequence. Delivery is independent of completion.
- Scheduled ChatGPT push: ~08:00–09:00 JST. Preferred deliverable is **a working HTML lesson link** matching this site's interface.
- For each new date, read the **repository's** `FIRST_28_DAYS.md` live if GitHub is connected. Identify today's row. If an authored `lessons/OI-D###.md` is missing, compose a short accurate lesson, verify forms against reliable evidence, and commit it to the repo if GitHub actions and approvals allow. **Do not pretend to have committed a file if not.**
- GitHub Action (direct Pages deployment; GitHub Pages Source must be **GitHub Actions**): ~07:20 JST updates `PROGRESS.md` to `published` if lesson content exists; otherwise `awaiting_content`. The site builder makes honest placeholders, not fabricated interactive grammar.
- A `published` row never proves completion; set `completed`, `in_progress`, `needs_revisit`, or `skipped` only on learner feedback. Preserve existing learner statuses when the daily Action reruns.
- If GitHub is not connected, the ChatGPT task should deliver the actual lesson **in chat**, provide a self-contained downloadable HTML file only if the file-creation tools really work in that task, and describe progress as **not yet synced**. Do not promise an unattested sandbox link or editing of a user's local file.

## HTML interactions

- All interactivity is plain browser JS, no external packages or API keys.
- Multiple-choice buttons respond immediately; answers can be retried without revealing the solution after an error. Hints and historical notes are expandable. Paradigm forms can be hidden and shown.
- `Mark complete` unlocks after all questions are answered correctly and stores a browser-local record.
- `Copy record` exports a Markdown row; `Download PROGRESS.md` exports browser-completed rows. These do **not** write the repository file.
- A server/API would be necessary for secure direct cross-device updates from the browser. It is not part of v0.4.

## Adjustments

- Follow the current first 28 targets unchanged unless explicitly amended during study. Missing work can be revisited without silently shifting the calendar sequence.
- New lesson content must be verified before the hosted link is presented as a complete interactive lesson.
- After Day 28, create an agreed continuation of dated targets from the macro-curriculum before daily publishing continues.