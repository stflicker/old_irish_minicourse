# Instructions for a connected GitHub daily task

**Prerequisite:** A repository URL and GitHub connector with read/write permission. Until then, use the embedded first-28 Markdown snapshot and deliver the lesson in chat; do not claim a hosted page is ready.

Each morning Japan time:

1. Read `FIRST_28_DAYS.md` in the linked repository. This is the canonical day/topic table. Start date: 2026-10-10 JST.
2. Determine the day number from the Japan date. Keep the first 28 topics in the given order.
3. Read `lessons/OI-D###.md`. If absent, author one 10–15-minute lesson following `LESSON_TEMPLATE.md`: small verified paradigm or text, one short explanation, 1–2 questions and optional comparative Celtic/IE note. Use reliable scholarly sources; do not invent paradigms or cite nonexistent quotations.
4. Commit the new Markdown file to the repository **if GitHub permissions and scheduled task tools support the write action**. If permissions require approval or the action fails, say so and send the lesson directly in chat as a fallback.
5. A GitHub Action publishes the Markdown as an interactive HTML page `docs/days/###.html` and adds the day's publication row to `PROGRESS.md`. If a page is still awaiting content, don't link to it as if complete.
6. Push the hosted HTML link in the ChatGPT notification **only when the file is verified published**. Otherwise push the full text-based lesson.
7. When the learner later replies with a score, minutes and difficulty, update `PROGRESS.md` in the repository if the connector permits and preserve it as confirmed feedback. Do not infer completion from mere publication.

No backend/database or OpenAI API key is necessary for the course scaffold. For fully unattended daily *authoring* the GitHub connector and scheduled task tool permissions must be tested; publishing alone is handled by GitHub Actions.