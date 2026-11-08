# Content design handoff (for the sessions that write and verify lessons)

*Written by the session that designed the “historical card” lessons (Days 1–7) and audited Days 1–28. From now on that session works only on visual design and site deployment; everything below is for whoever continues the **lesson content**.*

Read first: this file → `REVIEW_FIRST_28_DAYS.md` (factual errors) → `REVIEW_CONTENT_QUALITY.md` (focus, filler, missing derivation chains) → `NEXT_28_DAYS_DRAFT.md` (Days 029–056 outline) → the finished model lessons `lessons/OI-D001.md … OI-D007.md`.

---

## 1. The learner and the goal

* The learner knows Latin, Greek and Sanskrit and has done the alphabet, phonology, orthography, mutations and basic terminology. **Lesson 5 of Stifter is deliberately not taught**; do not add it unless asked.
* **Priority: historical-comparative morphology.** Every form should be traceable from PIE → Proto-Celtic → Primitive Irish → Old Irish, with the *process* shown, **in few words**.
* Language of the lessons: **English** (Day 7 was Chinese and has been rewritten in English).
* Textbook: Stifter, *Sengoídelc* (2006). The course follows its order. A lesson may be restructured if the content demands it; update the matching row in `FIRST_28_DAYS.md` (done for Days 1–7, now v0.3).
* Time budget: ~10–15 minutes, of which the historical card is optional (5–8).

## 2. What a lesson must contain (the “historical card” standard)

Frontmatter (`id, title, subtitle, category, stifter, minutes, word, questions, paradigm_revision: 7`), then three sections, **with exactly these headings** (the builder looks them up by name):

1. `## Paradigm` — one line `Following-word effects: [L] … [0] none…` (the builder folds it into a collapsible key), then the paradigm table(s). Headers `Case | Singular form + effect | Plural form + effect` give the hide-and-recall cells.
2. `## One point` — one rule, then a short **Quick answers** list. *Every doubt a learner could plausibly have must be answered here or in the card; if the sources do not answer it, say so* (see §4).
3. `## Comparison (optional)` — the **historical card**:
   * `### Historical card: <one question>`
   * a chain table: `Cell | PIE | Proto-Celtic | Primitive Irish | Old Irish` (use Stifter's columns; when he has no Proto-Celtic column, say so). `«` marks a replacement by analogy, exactly as Stifter does.
   * ≤ 4 numbered sound changes / replacements, each one sentence;
   * a `**Status.**` line using only: *Regular* / *Analogical («)* / *Open* (and what is open);
   * a `*Sources:*` line (see §4).

Budget: ≈ 450–600 words per lesson including tables (the old lessons were 600–900 with ~250 words of history that contained no chains). **Delete** disclaimers of the “do not equate X with Y” type, philosophical sentences (“exponence migration”), restatements of the table, and tangents (Romance article, *ser/estar*, Anatolian gender…). A warning is allowed only where a real misreading is likely, and once.

Quiz: 3 questions, one of them about the history; the correct option index must vary (the page shuffles options at runtime, but keep the keys varied); `explanation` and `hint` must be specific (no “check the table”).

## 3. Explanatory principles already established (reuse, don't re-derive)

* **Mutation = fossil of the lost ending.** Lenition [L] after a lost *vowel*; nasalization [N] after a lost *-n* (< *-n/-m*); aspiration/gemination [H] after a lost *-s*. Sources: EIEOL Grammar §6.1–6.3 (explicit) and Stifter §4.
* **Pattern read off Stifter's chains (state it as a pattern, not as Stifter's rule):** [H] follows endings that were *long vowel + h* (\*-ūh, \*-āh); short \*-ah, \*-ih leave nothing. **Open:** why the masculine nominative \*-os leaves no [H]; neither Stifter nor EIEOL says.
* **Root vowel follows the next vowel** (Day 3): before \*a → mid vowel (e, o); before \*ī/\*ū → high vowel (i, u). In *fer* the root vowel is original \*i (Stifter's chain), so *fer* is the *lowered* form; Stifter's formalism ({L}/{R}) describes the same forms from the other end. Raising is blocked before voiceless consonants (*ech*, not \*ich) — Stifter §6.5.
* **“Prepositional” = Stifter's name for the dative**, historically the merger of PIE dative \*-ōi, instrumental \*-oh₁ and ablative \*-ōd (Stifter p. 43).
* **Neuter nominative = old accusative** (\*-om), hence [N]. **Short neuter plural** continues \*-eh₂ (> \*-ā, [L]); **long plural** *-a* [H] is analogical («), copied from the ā-stems.
* **Initial \*kʷ**: Goidelic *c*, Brittonic *p* (*cenn* : Welsh *pen*); between vowels it lenited (*ech*).
* **Syncope** (Stifter §6.8.5): after final syllables were lost, the vowel of every second non-final syllable was deleted; a lost front vowel palatalizes the cluster.

## 4. Evidence rules (non-negotiable)

1. **Primary source: Stifter's own page.** Check superscripts and reconstructions on the **page image**, not on OCR text. (`pdftoppm -r 120 -f <pdf page> -l <pdf page> -png file.pdf out`; printed page = PDF page − 12.) In Stifter's phonemic script the glyph that looks like ρ is *r* and ν is *n*; macrons are lost in OCR.
2. **If Stifter has nothing, use a reliable source and name it.** Order of preference: EIEOL (Old Irish Online, UT Austin; fetchable), Thurneysen *GOI*, McCone 1996, Matasović 2009 (*Etymological Dictionary of Proto-Celtic*), Weiss (Cambridge, “Italo-Celtic”), Stifter 2023 *The rise of gemination in Celtic*, Holmer 1947. Wikipedia/Wiktionary only as secondary, and say “secondary”.
3. **Never state what you have not read.** If you only saw a search summary or an abstract, write “(summary only)” / “(not checked directly)” in the *Sources* line. Do not cite section numbers (Thurneysen §…, Stifter 2023 §8.1) you have not seen.
4. **Never invent forms.** Stifter gives no key for his §6.7 exercise (*macc, ball* …); do not supply forms from memory. Forms not in Stifter and not found in a source stay out of the lesson.
5. **When the sources disagree, say so in the lesson** and follow Stifter (the course's reference). Known case: the neuter article nom./acc. plural (Day 10): Stifter shows **no** mutation mark (p. 51, checked on the image); EIEOL §6.3 lists it among the [H] triggers.
6. **When the sources give no answer, write “Open” in the Status line** and say what is open. Do not guess.

### EIEOL map (verified live)
`https://lrc.la.utexas.edu/eieol/iriol/<page>#grammar_<id>`; the page number is a *lesson page* that carries several grammar sections:
`20` → §6 Initial Mutations (#grammar_1275; 6.1 Lenition 1276, 6.2 Nasalization 1277, 6.3 Spirant Mutation 1278), §9 case endings; `30` → §12 copula/substantive verb, **§13 o- and yo-stems** (1293), §14 adjective syntax, §15 pronouns incl. **15.3 possessives** (1298); `40` → §18 ā- and yā-stems, §19 numerals; `50` → §22 absolute/conjunct, §23 u-, i-, ī-stems, §24 adjective declensions; `60` → §27 past tenses, §28 s-stems, §30 demonstratives and **the article (§30.3, #grammar_1338)**; `70` → §32 present indicative, §33 consonantal stems, §35 prepositional pronouns. The old lessons wrongly sent article / adjective / ā-stem readers to `30`.

## 5. Practical notes for writing and building

* Build and test locally: `pip install -r scripts/requirements.txt; python scripts/build_site.py; python scripts/test_tables.py`. `docs/` is generated and committed.
* **Markdown traps**
  * Reconstructed forms must be written `\*ekʷos` (escaped). An unescaped `*…*` is italics and the star disappears. Do not use `*\*x*` or `***`: both render wrongly (the old lessons lost their stars this way).
  * YAML: quote any value that starts with `*` (e.g. `word: '*-o-'`); a bare `*` is an alias and breaks the build.
  * Do not nest `**bold *italic***`; write `**bold** *italic*`.
* **Table traps** (`scripts/table_tools.py`)
  * A table header named exactly `Form` (or any name in `FORM_HEADERS`) makes that column a hide-and-recall column. Use other names (`Spelling`, `Possible cells`…) for non-paradigm tables.
  * Every table needs non-blank headers and no entirely empty / dash-only column.
  * The test requires at least one recall cell in `#paradigm`; each lesson's `## Paradigm` must contain a standard paradigm table (Day 7 includes *ech* above the cross-language table for this reason).
  * `[L] [N] [H] [0]` anywhere in a table or text becomes a coloured badge.
* `paradigm_revision: 7` in the frontmatter protects hand-written lessons from `scripts/revise_paradigms.py` (which otherwise overwrites `## Paradigm`). Keep it in every lesson.
* The builder accepts 1–3 questions; `scripts/test_tables.py` was changed to allow 3.
* `FIRST_28_DAYS.md` is parsed by `scripts/course.py` (exactly 28 rows, `001…028`); the build warns if `stifter:` in the lesson does not contain the row's section number.
* Web access from the cloud session: a personal environment `old_irish_minicourse` allows `lrc.la.utexas.edu`, `en.wikipedia.org`, `en.wikisource.org`, `pmc.ncbi.nlm.nih.gov`, `archive.org`, `ia800605.us.archive.org`, `www.cambridge.org`, `en.wiktionary.org`. Observed: `curl` to EIEOL works; PMC answers with a bot-check page (do not try to bypass it); Wiktionary rate-limited (429); an `archive.org` fetch was refused by the session's permission classifier; `WebFetch` kept failing on newly allowed hosts. `WebSearch` works for summaries. Ask the user for text excerpts when a source cannot be read.
* **The Stifter PDF** is not in the repository and must not be committed (copyright; the repository is public). It lives in the user's Google Drive (the connector returns only the first ~183,000 characters, ≈ pp. 1–68) and was also attached to the session (full text layer, 402 PDF pages). A new session needs it re-attached.

## 6. State of the work

| Item | State |
|---|---|
| Days 1–7 | **Rewritten** as historical cards (commit `0af7bac`); to be reviewed by the learner |
| Days 8–28 | Old lessons, **not yet rewritten**; see the findings below |
| Days 29–56 | Topic-level draft only (`NEXT_28_DAYS_DRAFT.md`); no forms; needs Stifter pp. 77–121 per lesson |
| Quiz hint quality, boilerplate, links | Fixed in Days 1–7 only |

### Suggested order and data for Days 8–28
Use each lesson's Stifter figure for its chain (columns: Old Irish | Primitive Irish | Proto-Celtic | PIE):

| Days | Topic | Stifter data |
|---|---|---|
| 8–10 | masculine / neuter article (do the “article from demonstrative” story **once**, Day 8) | Ill. 7.1, 7.2 (pp. 50–51) |
| 11 | o-stem adjectives | Ill. 7.5 (phrases only; no chain) |
| 12–14 | W1 verbs, absolute / conjunct | Ill. 8.2; ending tables Ill. 12.2 (W1) |
| 15–17 | ā-stems, *cell*, *ben* | Ill. 10.1 (p. 59, checked), 10.2, 10.3 |
| 18–20 | feminine article, adjectives | Ill. 11.1, 11.2 |
| 21 | **replace**: *tuath* full-chain day (the old Day 21 repeats Day 15) | Ill. 10.1 |
| 22–24 | W2 verbs; two ending sets | Ill. 12.1, 12.3; **§12.3 note 6** (absolute/conjunct is *not* PIE primary/secondary; early loss of final \*-i, retained before enclitic particles; Old Welsh parallel) |
| 25 | possessives | Ill. 12.5 (checked) |
| 26 | poem | Stifter §13.1 (a normalized 11th-century scribe poem); add §13.2 varia |
| 27–28 | masculine / neuter io-stems | Ill. 14.1 (p. 74, checked), 14.2 |

### Known errors in Days 8–28 that must be fixed during the rewrite (details in `REVIEW_FIRST_28_DAYS.md`)
* **Day 10**: neuter article nom./acc. plural is shown [H]; Stifter p. 51 shows no mark; EIEOL says [H] → follow Stifter, mention the disagreement.
* **Days 22–23**: W2a is mainly *denominative*, W2b *causative/iterative* (*reithid* → *roithid*); the old lessons tie W2a to \*-eyé-.
* **Day 24**: must present Stifter's §12.3 ending tables and note 6 (Old Welsh parallel, loss of final \*-i); the “Cowgill particle” label and the Griffith (2020) citation need care (the chapter's real title is *“The ‘Cowgill particle’, preverbal* ceta *‘first’, and prepositional cleft sentences in the Old Irish glosses”*, pp. 239–268).
* **Day 26**: use Stifter's poem or label *Am gáeth i mmuir* honestly (later, normalized).
* **Day 27**: spellings must be *céili, céiliu, a chéili* (nom. pl. *céili*, acc. pl. *céiliu*); EIEOL §13 agrees.
* **Day 21 / 15 / 16, 8 / 9 / 18 / 19**: repeated history texts — one telling per topic.
* The Markdown nesting bug (literal `**`) is on 13 old pages; it disappears with the rewrite.
* References that are unverified or inappropriate: Scribd link to Thurneysen (remove); “Thurneysen §170a”, “§§240–241 *inna-mmaccu* Ml. 104d5” (check in *GOI*); Stifter 2023 “§8.1” (read the full text first — the PMC page is behind a bot check, ask the user); Luján and Le Mair links (not checked).

## 7. Checklist before a lesson is committed

1. Every form in every table checked against Stifter's page image (or a named source).
2. Chain table complete for the cells the lesson is about; `«` where Stifter has it.
3. Each “Quick answer” is true and sourced; unanswerable doubts are marked *Open*.
4. No disclaimer filler; ≈ 450–600 words; no repeated explanations from earlier lessons (refer back instead: “Day 3”).
5. Reconstruction stars visible in the rendered page (check the screenshot / text, not only the Markdown).
6. `python scripts/build_site.py && python scripts/test_tables.py` pass; no literal `**` in the page text.
7. *Sources* line honest about what was actually read.

## 8. Not your job (stays with the design / deployment session)

CSS, layout, dark mode, JS interactions, the home page, GitHub Pages and the workflow. Note for them: pushes from `claude/focused-newton-92w684` made the workflow fail in about one second with no steps run (runs #97–#100), which looks like the `github-pages` environment allowing only `main`; the rewritten pages go live only after a merge to `main`.
